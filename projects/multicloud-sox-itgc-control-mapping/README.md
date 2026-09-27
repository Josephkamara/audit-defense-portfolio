# Multi-Cloud SOX ITGC Control Mapping

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to map six SOX IT general controls to native evidence sources in AWS and GCP when the two clouds expose evidence through completely different services, and how to separate what a script can pull from what a SOX tester still has to judge.

## The Fictional Company

**Streamline Workflow, Inc.** (fictional). About 75 employees. Remote-first SaaS company providing project management software. Production environment split across AWS (us-east-1, ECS, RDS, S3) and GCP (us-central1, GKE, Cloud SQL, Cloud Storage). Public company (SOX 404(b) in scope). External auditor relies on IT audit team to test six SOX IT general controls: access provisioning (ACC-01), termination (ACC-02), privileged access review (ACC-04), change management (CHG-01), segregation of duties in deployment (CHG-05), and backup monitoring (OPS-01). The IT audit team needs a control-to-evidence map that works in both clouds.

## Read This in 3 Minutes

If you have three minutes:

1. **The challenge:** AWS and GCP organize access evidence differently. AWS uses IAM Identity Center for workforce access, with permission sets assigned to groups. GCP uses Workspace groups and IAM bindings, with roles granted at the project or resource level. AWS logs to CloudTrail. GCP logs to Cloud Logging (formerly Stackdriver). The same control (ACC-01, access provisioning) pulls evidence from different services in each cloud. A SOX tester needs one control definition and two evidence maps.
2. **The mapping:** For each control, define the control objective (what the control does), the population (what gets tested), and the evidence source in both AWS and GCP. Example: ACC-04 (privileged access review). Objective: privileged access reviewed quarterly and certified by managers. Population: all users with admin or write access to production. AWS evidence: IAM Identity Center assignments (permission set + group + user), pulled via `list-account-assignments`. GCP evidence: IAM policy bindings at the project level, pulled via `gcloud projects get-iam-policy`. Both populations export to CSV, both get reviewed in the same ServiceNow campaign.
3. **What a script can pull and what it cannot:** A script can pull the population (who has access), the access level (read vs. write vs. admin), and the timestamps (when access was granted, when it was last used). A script cannot judge whether a developer needs admin access to a test environment (that is manager judgment), whether a 4-day delay in contractor offboarding is acceptable (that is exception analysis), or whether a deployment role assigned to a CI/CD service account instead of a human is a segregation of duties violation (that is control design judgment). The mapping document states which decisions are automated and which require human review.

## Frameworks Covered

SOX IT General Controls (ITGC), mapped to SOC 2 Trust Services Criteria as the reference control framework (CC6 for access, CC8 for change, CC7 for operations)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full control mapping with control objectives, populations, AWS and GCP evidence sources, sample CLI commands, and the line between automated evidence pulls and human judgment |
| `README.md` | This file |

## Key Mapping

Six controls mapped across AWS and GCP. ACC-01 (access provisioning): Identity Center assignments (AWS), IAM bindings (GCP). ACC-02 (termination): HRIS-to-Okta deprovisioning with SCIM, confirmed via Okta user state export. ACC-04 (privileged access review): Identity Center assignments (AWS), IAM bindings at project level (GCP), both reviewed quarterly in ServiceNow. CHG-01 (change management): GitHub branch protection, pull request approval, ServiceNow change record. CHG-05 (segregation of duties): GitHub Actions OIDC roles (AWS), Workload Identity Federation service accounts (GCP). OPS-01 (backup monitoring): AWS Backup vault compliance (AWS), Cloud SQL backup status (GCP). Each control has one objective, one test procedure, and two evidence maps.
