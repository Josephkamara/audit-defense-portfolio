# Cloud Access Compliance Scanner

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to automate evidence collection for four access and data-protection controls with real working code, a test suite, and a design document that states what each control requires, what evidence proves it, and why each check would pass or fail a third-party test.

## The Fictional Company

A fictional payment processor (Keystone Civic Payments in the case study) with cloud-hosted infrastructure. Four access and data-protection controls automated: stale access keys, MFA required for console access, wildcard policies prohibited, and storage buckets not publicly accessible. The scanner runs in CI/CD before each deployment and produces workpaper-shaped findings.

## Read This in 3 Minutes

If you have three minutes:

1. **What the scanner checks:** Four controls mapped to SOC 2 and SOX ITGC requirements. Stale access keys (access review): any access key not rotated in 90 days is a finding. MFA enforcement (access controls): any user with console access and no MFA device is a finding. Wildcard policies (least privilege): any policy with wildcard action and wildcard resource is a finding. Public storage buckets (data protection): any storage bucket with public read or write access is a finding.
2. **How it runs:** The scanner is a Python script using the cloud provider SDK to query the account. It runs against a test account seeded with deliberate violations (one stale key, one user without MFA, one wildcard policy, one public bucket) to confirm the checks work. A test suite with mocking and time-shifting validates the logic. The test suite runs in under two seconds. In production, the scanner runs in CI/CD and writes findings to a file that feeds the compliance platform.
3. **Why this is not just a script:** The write-up includes the control objective for each check, the evidence specification (what data the check pulls and why that data proves the control), and the pass/fail criteria an auditor would use. The test suite confirms the checks catch violations and do not generate false positives. This is evidence an auditor can rely on, not a script that somebody says works.

## Frameworks Covered

SOC 2 Trust Services Criteria (CC6.1, CC6.2, CC6.6, CC6.7), SOX IT General Controls (access to programs and data)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full write-up with control objectives, evidence specifications, pass/fail criteria, and links to the code |
| `code/scanner.py` | Python scanner using boto3 to check stale keys, missing MFA, wildcard policies, and public S3 buckets |
| `code/test_scanner.py` | 10-test pytest suite with moto and freezegun |
| `code/requirements.txt` | Python dependencies (boto3, pytest, moto, freezegun) |
| `README.md` | This file |

## Key Results

The scanner runs in under 2 seconds in the test environment and catches all four violation types. The test suite confirms no false positives (a recently rotated key does not trigger the stale key check, a bucket with bucket-owner-full-control does not trigger the public access check). In production, the scanner backs up quarterly access reviews (ACC-05, ACC-06) and continuous monitoring checks (ACC-08, ACC-14). It does not replace the quarterly manager review, but it finds exceptions between reviews.
