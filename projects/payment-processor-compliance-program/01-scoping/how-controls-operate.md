# How Controls Operate (Scenario Assumptions)

This document describes how Keystone Civic Payments' (fictional) controls operate, distinguishing between automated infrastructure-as-code configurations and manual or IT-dependent processes. This distinction determines how each control is tested.

## AWS Controls Are Built as Code

**Scenario assumption:** Network security controls (security groups, NACLs, Transit Gateway routes), IAM Identity Center permission sets, S3 bucket policies, KMS key policies, CloudTrail, AWS Config rules, and logging settings are defined in Terraform in GitHub.

**Change management:**
- Changes go through a pull request with `terraform plan` output attached, peer review under branch protection (CHG-02), and a linked ServiceNow change record (CHG-01).
- Only the GitHub Actions deployment role, through OIDC, applies to production (CHG-05).

## Continuous Monitoring

**Scenario assumption:** AWS Config rules and conformance packs detect drift from the Terraform baseline. AWS Security Hub runs the AWS Foundational Security Best Practices standard and the PCI DSS v4.0.1 standard, which Security Hub has supported since December 2024.

**Automated evidence:**
- GuardDuty findings and failed Config and Security Hub checks open ServiceNow tickets automatically.
- The GRC platform (a Vanta, Drata, Secureframe, or OneTrust class tool) pulls pass/fail results from AWS, Okta, GitHub, and ServiceNow as automated evidence.

## Legacy Colocation Batch System Stays Manual

**Scenario assumption:** The batch server and its database cannot be managed by Terraform. Its controls are manual or IT-dependent manual, with a defined cadence:
- Local account listing reviewed quarterly (GAP-014 scope)
- OS and database security parameters exported and compared to the baseline quarterly
- Firewall rule review every six months (NET-02)
- Nightly backup job check and quarterly restore test (OPS-02)
- Cage access list reviewed quarterly (PHY-01)
- Wireless scan quarterly (NET-06)

## How Testing Changes

This is the auditor point:

**Automated, Terraform-defined configuration can be tested as a test of one:** Inspect the configuration once at a point in time and confirm it matches the requirement. That works only if the IT general controls over that configuration operated all period: change management (CHG-01, CHG-02, CHG-05) and privileged access (ACC-05, ACC-13). Add the AWS Config compliance timeline for the period, which shows no unremediated drift.

If the ITGCs are not effective, fall back to testing the configuration at multiple points in the period.

**Manual controls keep frequency-based samples:** See the table in 02-control-matrix/README.md and the detailed test procedures in folder 03-itgc-test-procedures.

**PCI QSAs** examine configurations and do not use the term "test of one". The same evidence still supports their testing.

## Where Automated Evidence Can Mislead

An automated check that proves the wrong thing (MFA enrollment instead of a per-session challenge) passes two audits and fails PCI. Automated evidence needs a human-reviewed evidence specification.

See [the GRC Control Automation project](../../grc-control-automation/) for the cautionary tale: a GRC engineering team built one control crosswalk to satisfy SOC 2, ISO 27001, and PCI DSS at once. The mapping was correct. The automated evidence was not. Two audits missed it. A PCI QSA didn't.

## Worked Example: Cloud Access Compliance Scanner

See [the Cloud Access Compliance Scanner](../../cloud-access-compliance-scanner/) as the primary worked example. It is working boto3 code that runs repeatable access checks against an AWS account and produces workpaper-shaped findings on every run. That is the kind of continuous, automated evidence this section describes.

The scanner is tested against a mocked copy of a Keystone sandbox account, seeded with deliberate violations so every check fires. In Keystone's production accounts, these checks back up ACC-05 (no human IAM users), ACC-06 (MFA enforcement), ACC-08 (service account inventory), and ACC-14 (unused access removal). The expected production result is zero findings apart from the two documented break-glass users.

## Note on Expanded Scope

**Scenario assumption (optional one-liner):** If a second cloud were in scope, the same pattern would apply with that cloud's native policy-as-code and posture tools.

See GAP-010 in the gap analysis. AWS Config rules do not yet cover all CDE instances, which limits TP-AUTO reliance until that gap closes.

---

**Fictional company, sample data.** Keystone Civic Payments is built for this walkthrough. The company, scenario, and all data are invented to demonstrate how infrastructure as code and continuous monitoring change control testing.
