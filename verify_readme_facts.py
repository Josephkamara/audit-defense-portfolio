#!/usr/bin/env python3
"""
Verify that facts in new READMEs exist in the project's original files.
Extracts capitalized names and numbers from README, checks against index.html and main branch README.
"""
import re
import subprocess
import sys
from pathlib import Path

def get_capitalized_phrases(text):
    """Extract multi-word capitalized phrases (potential company names, products)."""
    # Match sequences of capitalized words (2+ words)
    pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b'
    return set(re.findall(pattern, text))

def get_numbers(text):
    """Extract numbers with context (e.g., '250 employees', '40,000')."""
    # Match numbers with commas, possibly followed by text
    pattern = r'\b(\d{1,3}(?:,\d{3})+|\d+)\b'
    return set(re.findall(pattern, text))

def get_specific_names(text):
    """Extract specific product/company names in quotes or all-caps short names."""
    names = set()
    # Names in quotes or parentheses
    pattern = r'[""""]([A-Z][A-Za-z\s]+)[""""]'
    names.update(re.findall(pattern, text))
    # All-caps acronyms (3-10 chars)
    pattern = r'\b([A-Z]{3,10})\b'
    names.update(re.findall(pattern, text))
    return names

def check_project(project_name):
    """Check one project's README against its source files."""
    project_path = Path(f"projects/{project_name}")
    readme_path = project_path / "README.md"
    index_path = project_path / "index.html"
    
    if not readme_path.exists():
        return None
    
    # Get current README content
    with open(readme_path) as f:
        new_readme = f.read()
    
    # Get original README from main branch
    try:
        result = subprocess.run(
            ["git", "show", f"main:projects/{project_name}/README.md"],
            capture_output=True, text=True, check=True
        )
        old_readme = result.stdout
    except subprocess.CalledProcessError:
        old_readme = ""
    
    # Get index.html
    if index_path.exists():
        with open(index_path) as f:
            index_html = f.read()
    else:
        index_html = ""
    
    # Combine source materials
    source_text = old_readme + "\n" + index_html
    
    # Extract added content (skip sections that were in original)
    # Focus on "The Fictional Company" and "Read This in 3 Minutes" sections
    added_sections = []
    if "## The Fictional Company" in new_readme:
        start = new_readme.find("## The Fictional Company")
        end = new_readme.find("##", start + 5)
        if end == -1:
            end = len(new_readme)
        added_sections.append(new_readme[start:end])
    
    if "## Read This in 3 Minutes" in new_readme:
        start = new_readme.find("## Read This in 3 Minutes")
        end = new_readme.find("##", start + 5)
        if end == -1:
            end = len(new_readme)
        added_sections.append(new_readme[start:end])
    
    added_text = "\n".join(added_sections)
    
    # Extract facts from added content
    added_caps = get_capitalized_phrases(added_text)
    added_numbers = get_numbers(added_text)
    added_names = get_specific_names(added_text)
    
    # Filter out common generic terms
    generic_terms = {
        "The Fictional Company", "Read This", "Fictional Company", 
        "What Is", "Key Results", "Key Decision", "Key Finding",
        "Trust Services", "Trust Services Criteria", "Security Rule",
        "Business Associate", "Type II", "Annual Report", "Cloud Storage",
        "Identity Center", "Access Controls", "Risk Management",
        "Data Protection", "System Security", "Compliance Program",
        "Service Provider", "High Risk", "Machine Readable"
    }
    added_caps = added_caps - generic_terms
    
    # Check what's not in source
    missing_caps = []
    for phrase in added_caps:
        if phrase not in source_text:
            missing_caps.append(phrase)
    
    missing_numbers = []
    for num in added_numbers:
        if num not in source_text:
            missing_numbers.append(num)
    
    missing_names = []
    for name in added_names:
        if name not in source_text and name not in ["README", "CSV", "HTML", "AWS", "GCP", "NIST", "PCI", "SOC", "ISO", "HIPAA"]:
            missing_names.append(name)
    
    if missing_caps or missing_numbers or missing_names:
        return {
            "project": project_name,
            "missing_caps": sorted(missing_caps),
            "missing_numbers": sorted(missing_numbers),
            "missing_names": sorted(missing_names)
        }
    
    return None

def main():
    projects = [
        "risk-acceptance-memo",
        "iso27001-statement-of-applicability",
        "soc2-access-review-automation",
        "third-party-risk-management",
        "pci-dss-network-segmentation",
        "grc-control-automation",
        "cloud-access-compliance-scanner",
        "multicloud-sox-itgc-control-mapping",
        "fedramp-20x-poam",
        "agentic-ai-risk-assessment",
        "eu-ai-act-high-risk-classification"
    ]
    
    print("Checking for invented facts in new READMEs...\n")
    
    issues = []
    for project in projects:
        result = check_project(project)
        if result:
            issues.append(result)
    
    if not issues:
        print("✓ All READMEs verified: no invented facts found.")
        return 0
    
    print(f"✗ Found invented facts in {len(issues)} project(s):\n")
    for issue in issues:
        print(f"  {issue['project']}:")
        if issue['missing_caps']:
            print(f"    Capitalized phrases not in source: {', '.join(issue['missing_caps'])}")
        if issue['missing_numbers']:
            print(f"    Numbers not in source: {', '.join(issue['missing_numbers'])}")
        if issue['missing_names']:
            print(f"    Names not in source: {', '.join(issue['missing_names'])}")
        print()
    
    return 1

if __name__ == "__main__":
    sys.exit(main())
