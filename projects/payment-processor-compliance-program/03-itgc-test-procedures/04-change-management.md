# Test Procedure 04: Change Management

**Control Reference:** CHG-01, CHG-02, CHG-05

**Control Statement:** Production changes to applications and infrastructure require a ServiceNow change record with risk rating, test evidence, and approval by the change advisory board or a pre-approved standard change model before deployment. GitHub branch protection requires at least one approving review from someone other than the author and passing status checks before merge. Only the CI/CD deployment role can change production; emergency changes get retrospective approval within two business days.

**Control Owner:** Director of Engineering

**Frequency:** Recurring (many times per day)

**Nature:** IT-dependent manual

**Type:** Preventive

**Key Control:** Yes

## Control Objective

To ensure that changes to production systems are authorized, tested, and documented before deployment, reducing the risk of unintended outages or security gaps introduced by changes.

## Applicable Framework Requirements

- **PCI DSS v4.0.1:** 6.5.1, 1.2.2 (network changes), 6.5.4 (separation of duties)
- **SOC 2:** CC8.1
- **NIST SP 800-53 Rev 5:** CM-3, CM-4, CM-3(2), CM-5
- **SOX ITGC:** Program Change

## Population and Sample Size

**Population:** All production changes (application code, infrastructure as code, configuration changes) deployed during the review period. Typically 200-400 changes per month.

**Sample size:** 25 to 60 changes, stratified by change type (application, infrastructure, emergency), risk level (standard, normal, high), and month.

## Test Steps

1. **Obtain the change population:**
   - ServiceNow change records with type = Production, status = Closed or Implemented, deployed during the period.
   - Include emergency changes (retrospective approval).

2. **For each sampled change:**
   - **Change record exists:** Confirm a ServiceNow change record was created before deployment (or within 2 business days for emergency changes).
   - **Risk rating documented:** Confirm risk rating (standard/normal/high) is filled in.
   - **Test evidence attached:** Confirm test results, staging deployment log, or pre-production validation is attached or referenced.
   - **Approval before deployment:**
     - For normal and high-risk changes: Confirm CAB approval or Director of Engineering approval is documented in ServiceNow before the deployment timestamp.
     - For standard changes: Confirm the change matches a pre-approved standard change model (example: routine patch, certificate renewal).
     - For emergency changes: Confirm retrospective CAB approval occurred within 2 business days.
   - **GitHub pull request linked:** Confirm the change record links to a GitHub pull request (for code/IaC changes).
   - **Branch protection enforced:** Open the linked pull request in GitHub; confirm at least one approving review from someone other than the author, and that status checks (CI pipeline) passed before merge.
   - **Deployment actor:** Check deployment logs (GitHub Actions run log, CloudTrail for Terraform applies); confirm the deployment was performed by the CI/CD service account (GitHub Actions OIDC role), not a human user, except for approved emergency break-glass access.

## Sample Attributes

| Attribute | Expected | How to Test |
|-----------|----------|-------------|
| Change record created | Record exists, created before deployment (or within 2 days for emergency) | Compare change created timestamp to deployment timestamp |
| Risk rating documented | Field is filled | Inspect ServiceNow change record |
| Test evidence present | Attachment or reference exists | Inspect ServiceNow attachments or linked test results |
| Approval before deployment | Approval timestamp < deployment timestamp | Compare approval timestamp to deployment log timestamp |
| GitHub PR approval | ≥1 approving review, status checks passed | Inspect GitHub PR approval history and status checks |
| Deployment by CI/CD | Deployer = service account, not human | Check CloudTrail or GitHub Actions run log for identity |

## Exception Example

**Exception:** One emergency change (CHG-98765, deployed May 20, 2026 at 03:15 UTC to fix a payment API outage) was deployed by a human engineer (alice.admin@keystone.example) using break-glass AWS console access instead of through the CI/CD pipeline. Retrospective CAB approval was documented May 21 (within 2 business days per policy). The deployment was successful and resolved the outage.

**Root Cause:** The GitHub Actions pipeline was unavailable due to a GitHub.com service disruption (confirmed by checking GitHub status page for May 20, 2026). The engineer used approved emergency access (just-in-time elevation, session logged in CloudTrail) to deploy the fix manually via AWS console.

**Compensating Control:** The emergency change followed the documented break-glass procedure (ticket created, CISO notified, session logged). The change was reviewed and approved retrospectively the next business day.

**Remediation:** No remediation required; this is a documented exception path for pipeline unavailability. The control operated as designed for 59 of 60 sampled changes.
