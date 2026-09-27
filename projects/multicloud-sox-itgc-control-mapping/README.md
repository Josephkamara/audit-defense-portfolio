# Multi-Cloud SOX ITGC Control Mapping

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to map six SOX IT general controls to native evidence sources in AWS and GCP when the two clouds expose evidence through completely different services, and how to separate what a script can pull from what a SOX tester still has to judge.

## The Fictional Company

A fictional SaaS company running production across both AWS and GCP. Public company (SOX 404(b) in scope). External auditor relies on IT audit team to test six SOX IT general controls: access provisioning, termination, privileged access review, change management, segregation of duties in deployment, and backup monitoring. The IT audit team needs a control-to-evidence map that works in both clouds.

## Read This in 3 Minutes

If you have three minutes:

1. **The challenge:** AWS and GCP organize access evidence differently. AWS uses one identity service for workforce access, with permission sets assigned to groups. GCP uses workspace groups and access bindings, with roles granted at the project or resource level. AWS logs to one service. GCP logs to another. The same control (access provisioning) pulls evidence from different services in each cloud. A SOX tester needs one control definition and two evidence maps.
2. **The mapping:** For each control, define the control objective (what the control does), the population (what gets tested), and the evidence source in both AWS and GCP. Example: privileged access review. Objective: privileged access reviewed quarterly and certified by managers. Population: all users with admin or write access to production. AWS evidence: identity center assignments (permission set, group, user). GCP evidence: access policy bindings at the project level. Both populations export to CSV, both get reviewed in the same campaign.
3. **What a script can pull and what it cannot:** A script can pull the population (who has access), the access level (read vs. write vs. admin), and the timestamps (when access was granted, when it was last used). A script cannot judge whether a developer needs admin access to a test environment (that is manager judgment), whether a delay in contractor offboarding is acceptable (that is exception analysis), or whether a deployment role assigned to a CI/CD service account instead of a human is a segregation of duties violation (that is control design judgment). The mapping document states which decisions are automated and which require human review.

## Frameworks Covered

SOX IT General Controls (ITGC), mapped to SOC 2 Trust Services Criteria as the reference control framework (CC6 for access, CC8 for change, CC7 for operations)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full control mapping with control objectives, populations, AWS and GCP evidence sources, sample CLI commands, and the line between automated evidence pulls and human judgment |
| `README.md` | This file |

## Key Mapping

Six controls mapped across AWS and GCP. Access provisioning: identity center assignments (AWS), access bindings (GCP). Termination: HRIS-to-identity-provider deprovisioning with SCIM, confirmed via identity provider user state export. Privileged access review: identity center assignments (AWS), access bindings at project level (GCP), both reviewed quarterly. Change management: repository branch protection, pull request approval, change record. Segregation of duties: CI/CD service account roles (AWS), federated service accounts (GCP). Backup monitoring: backup vault compliance (AWS), backup status (GCP). Each control has one objective, one test procedure, and two evidence maps.
