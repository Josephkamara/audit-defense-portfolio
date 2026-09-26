# Test Procedure 03: Periodic and Privileged Access Review

**Control Reference:** ACC-04

**Control Statement:** Privileged and CDE access is reviewed quarterly and all other user access to in-scope systems at least every six months. Reviewers certify each account, inappropriate access is removed and tracked to completion, and management acknowledges the results.

**Control Owner:** IAM Manager (process); System Owners (reviewers)

**Frequency:** Quarterly

**Nature:** IT-dependent manual

**Type:** Detective

**Key Control:** Yes

## Control Objective

To ensure that user access to in-scope systems remains appropriate for current job responsibilities, that privileged and CDE access is reviewed more frequently than standard access due to higher risk, and that inappropriate access identified during reviews is promptly removed.

## Why This Matters

Access reviews are a detective control. They do not prevent inappropriate access from being granted in the first place (that is ACC-01, provisioning with approval), but they catch access that should have been removed when someone changed roles or left the company, or access that was granted temporarily and never removed. For privileged access (admin, root, database DBA) and CDE access (systems that store, process, or transmit cardholder data), the risk of inappropriate access is higher, so PCI DSS 7.2.4 requires more frequent review.

## Applicable Framework Requirements

| Framework | Requirement | Specific Language |
|-----------|-------------|-------------------|
| PCI DSS v4.0.1 | 7.2.4 | "All user accounts and related access privileges, including third-party/vendor accounts, are reviewed as follows: At least once every six months. Privileged user accounts are reviewed at least once every three months. Anomalies are addressed." |
| SOC 2 | CC6.2, CC6.3 | "Logical access is reviewed periodically. The entity authorizes, modifies, or removes access based on changes in job responsibilities, terminations, or changes in authorizations." |
| NIST SP 800-53 Rev 5 | AC-2, AC-6(7) | "Review accounts for compliance with account management requirements [Assignment: organization-defined frequency]; and if accounts are not in compliance, take [Assignment: organization-defined actions]. Review roles and privileges [Assignment: organization-defined frequency] to validate the need for such roles and privileges; and reassign or remove roles and privileges, if necessary." |
| SOX ITGC | Access to Programs and Data | Periodic access reviews are performed and documented; inappropriate access is remediated in a timely manner. |

**Keystone's defined frequency:** Privileged and CDE access quarterly; all other access semiannually.

## Population Definition and IPE

**Population:** All active user accounts (human and service accounts) in the in-scope systems as of the review date.

**In-scope systems for this control:**
- Okta (all application assignments for in-scope apps)
- AWS IAM Identity Center (permission sets for production accounts)
- AWS IAM (direct IAM users and roles, if any remain; Keystone is migrating to Identity Center)
- Legacy batch system (Linux OS accounts, PostgreSQL database users)
- GitHub (organization membership and repository access for production repos)
- ServiceNow (roles and groups for production instance)

**Privileged accounts:** Defined as AWS admin roles, database DBA roles, Okta super admin, ServiceNow admin, GitHub org admin, Linux root or sudo access.

**CDE accounts:** Defined as any account with direct access to CDE systems (payment API, tokenization service, payment database, settlement processor, legacy batch system).

### How to Obtain the Population

1. **Okta:** Export from Okta Admin Console > Reports > Users, filtered by Status = Active, exported to CSV with username, email, groups, last login date. Cross-check user count against the HR roster (HRIS export) to confirm completeness.
2. **AWS:** Run AWS IAM Identity Center CLI command `aws sso-admin list-permission-sets` and `aws sso-admin list-account-assignments` for each production account. For IAM users (legacy), run `aws iam get-credential-report` and filter by password\_enabled = true or access\_key\_active = true.
3. **Legacy batch system:** SSH to the server, run `cat /etc/passwd` for Linux accounts, `psql -c "\du"` for PostgreSQL users. Export to CSV.
4. **GitHub:** Use GitHub API or `gh` CLI: `gh api /orgs/keystone-civic-payments/members --paginate` for org members, then repository-level collaborators for production repos.
5. **ServiceNow:** Navigate to User Administration > Users, filter by Active = true, export user list with roles and groups.

### IPE (Information Produced by the Entity)

For each population source, document:

- **Source system and date/time of export** (so the auditor can verify the period)
- **Parameters and filters applied** (example: "Active users only, exported 2026-09-15 at 14:32 UTC")
- **Completeness check** (example: Okta user count reconciles to HRIS roster; AWS accounts reconcile to the AWS Organizations member account list)
- **Accuracy check** (example: Sampled 5 Okta users and traced to HRIS; sampled 3 AWS permission sets and confirmed assignments in the console)

If the population does not reconcile or if the export parameters are unclear, the auditor will treat the population as incomplete or inaccurate, and the test cannot be completed.

## Sample Size

**Keystone's risk-based approach:**

- **Privileged accounts:** Review all privileged accounts every quarter (population typically 12-18 accounts). Sample size = 100% due to high risk.
- **CDE accounts:** Review all CDE accounts every quarter (population typically 25-35 accounts). Sample size = 100% due to PCI scope.
- **Other accounts:** Review all other accounts semiannually. Sample size for audit testing = 25 accounts per review period, stratified by system (Okta, AWS, ServiceNow, GitHub) and selected randomly from the population.

**Audit testing sample size (auditor tests the review, not the full population):**

Since the control operates quarterly (4 times per year for privileged/CDE, 2 times per year for other), the auditor will sample 2 review periods and test the review completeness and evidence for those periods.

For each sampled review period:

- Confirm the population was complete and accurate (IPE testing)
- Select 25 accounts from the review results and confirm:
  - The reviewer certified the account as appropriate or flagged for removal
  - If flagged, a removal ticket was created
  - The removal ticket was completed within the defined SLA (5 business days per policy)
  - Management signed off on the review results

## Test Steps

### Step 1: Inquiry with the IAM Manager

Ask the IAM Manager to describe:

- How the access review process works (who reviews, how often, what they review)
- How reviewers are selected (system owners review their own systems; manager reviews their direct reports' access)
- How the review is documented (ServiceNow access review campaign)
- What happens if a reviewer finds inappropriate access (removal ticket is created and tracked to completion)
- How management acknowledges the results (Director of IT Operations signs off on the campaign summary)

Document the responses. Inquiry alone is not sufficient; it establishes understanding only.

### Step 2: Observation of the Review Tool

Ask the IAM Manager to show the ServiceNow access review module configuration:

- Review campaign template (frequency, scope, reviewers, instructions)
- Sample review screen showing how a reviewer certifies or flags an account
- Automated reminders and escalation for overdue reviews

Take screenshots or record the configuration. Observation confirms the tool exists and is configured as described.

### Step 3: Inspection of Design

Review the access review policy document and confirm:

- Privileged and CDE access is reviewed quarterly
- All other access is reviewed at least semiannually
- Reviewers are defined (system owners, managers)
- Removal SLA is defined (5 business days per Keystone's policy)
- Management sign-off is required

### Step 4: Test of Operating Effectiveness (Reperformance)

Select 2 review periods from the past 12 months (example: Q2 2026 and Q3 2026 for privileged/CDE; H1 2026 for other access).

For each selected period:

1. **Obtain the review results export** from ServiceNow: campaign ID, reviewer, account, decision (approved / remove), date certified, removal ticket ID (if flagged).
2. **Reconcile the population reviewed to the population obtained (IPE):** Confirm all accounts from the source export appear in the review results. If any accounts are missing, ask why.
3. **Select 25 accounts** from the review results (stratified by decision: 20 approved, 5 flagged for removal, if available).
4. **For approved accounts:**
   - Confirm the reviewer certified the account as appropriate (decision = approved, date stamp present).
   - If the account is privileged or CDE, confirm it still has a documented business need (tie to role matrix or approval ticket from ACC-01).
5. **For flagged accounts:**
   - Confirm a removal ticket was created (ticket ID in the review results).
   - Open the ticket in ServiceNow and confirm:
     - The ticket was assigned to the correct team (IAM, system owner)
     - The ticket was completed (status = Resolved or Closed)
     - The completion date was within 5 business days of the review certification date
     - Evidence of removal is attached (example: Okta System Log user.group.membership.remove event, AWS CLI output showing permission set unassigned)
6. **For each review period:**
   - Confirm management signed off on the campaign summary (Director of IT Operations signature or email approval in ServiceNow).

Document results in a workpaper (see sample below).

### Step 5: Test for Exceptions

An exception occurs if:

- An account was missing from the review (population incomplete)
- A reviewer did not certify the account (blank decision)
- A flagged account's removal ticket was not created
- A removal ticket was completed late (more than 5 business days)
- A removal ticket shows "completed" but the access was not actually removed (confirmed by checking the current state in the source system)
- Management did not sign off on the review results

For each exception:

1. Document the specific deviation (what was expected vs. what was found)
2. Perform inquiry with the control owner to determine root cause
3. Check for compensating controls (example: a late removal for a privileged account, but the account was disabled on the termination date, so the delay in full removal had no security impact)
4. Determine whether the exception is isolated or systemic (is it one account or a pattern?)
5. Report the exception to the audit lead and recommend remediation

## Sample Attributes Table

| Attribute | Expected Result | How to Test |
|-----------|-----------------|-------------|
| Frequency | Privileged/CDE quarterly; other semiannually | Confirm review campaign creation dates in ServiceNow; Q1, Q2, Q3, Q4 for privileged; H1, H2 for other |
| Population completeness | All active accounts reviewed | Reconcile review population to source system exports (Okta, AWS, etc.) |
| Reviewer certification | Each account has a decision (approved or remove) and date stamp | Inspect review results; no blank decisions |
| Removal ticket created | Flagged accounts have a removal ticket ID | Inspect review results; trace ticket ID to ServiceNow |
| Removal timely | Removal completed within 5 business days | Calculate business days between review date and ticket closed date; confirm ≤ 5 |
| Removal effective | Access was actually removed in the source system | For sampled flagged accounts, check current access in Okta/AWS/etc.; confirm account no longer has access |
| Management sign-off | Director of IT Operations signed off on campaign summary | Inspect campaign summary report; look for signature or email approval |

## Sample Workpaper: Q3 2026 Privileged Access Review

**Review Period:** Q3 2026 (July 1, 2026 - September 30, 2026)

**Review Campaign ID:** SN-ACCESSREV-2026-Q3-PRIV

**Review Start Date:** October 1, 2026

**Review Completion Date:** October 8, 2026

**Population Source:** AWS IAM Identity Center permission sets for production accounts; Okta super admin group; ServiceNow admin role; GitHub org admin; legacy batch system root/sudo

**Population Count:** 16 privileged accounts

**Reviewers:** Cloud Platform Engineering Manager (AWS), IAM Manager (Okta), IT Operations Manager (ServiceNow, legacy), AppSec Lead (GitHub)

**Management Sign-off:** Director of IT Operations, signed October 10, 2026

### Sample Selection

25 accounts requested per test procedure; population is only 16 privileged accounts; testing all 16 (100% sample).

| # | Account Username | System | Reviewer | Decision | Certified Date | Removal Ticket | Result |
|---|------------------|--------|----------|----------|----------------|----------------|--------|
| 1 | alice.admin@keystone.example | AWS Admin | Cloud Eng Mgr | Approved | 2026-10-02 | N/A | Pass |
| 2 | bob.platform@keystone.example | AWS Admin | Cloud Eng Mgr | Approved | 2026-10-02 | N/A | Pass |
| 3 | charlie.db@keystone.example | RDS DBA | Cloud Eng Mgr | Approved | 2026-10-03 | N/A | Pass |
| 4 | david.iam@keystone.example | Okta Super Admin | IAM Manager | Approved | 2026-10-03 | N/A | Pass |
| 5 | eve.snow@keystone.example | ServiceNow Admin | IT Ops Mgr | Approved | 2026-10-04 | N/A | Pass |
| 6 | frank.gh@keystone.example | GitHub Org Admin | AppSec Lead | Approved | 2026-10-04 | N/A | Pass |
| 7 | grace.ops@keystone.example | AWS Admin | Cloud Eng Mgr | Approved | 2026-10-05 | N/A | Pass |
| 8 | henry.contractor@secureconsult.example | AWS Admin | Cloud Eng Mgr | Remove | 2026-10-05 | CHG-45678 | **Exception (see below)** |
| 9 | iris.batch@keystone.example | Legacy sudo | IT Ops Mgr | Approved | 2026-10-06 | N/A | Pass |
| 10 | jack.security@keystone.example | AWS Admin | Cloud Eng Mgr | Approved | 2026-10-06 | N/A | Pass |
| 11 | karen.cloud@keystone.example | AWS Admin | Cloud Eng Mgr | Approved | 2026-10-07 | N/A | Pass |
| 12 | larry.incident@keystone.example | ServiceNow Admin | IT Ops Mgr | Approved | 2026-10-07 | N/A | Pass |
| 13 | monica.db@keystone.example | RDS DBA | Cloud Eng Mgr | Approved | 2026-10-07 | N/A | Pass |
| 14 | nathan.deploy@keystone.example | GitHub Org Admin | AppSec Lead | Approved | 2026-10-08 | N/A | Pass |
| 15 | olivia.access@keystone.example | Okta Super Admin | IAM Manager | Approved | 2026-10-08 | N/A | Pass |
| 16 | paul.batch@keystone.example | Legacy root | IT Ops Mgr | Approved | 2026-10-08 | N/A | Pass |

**Summary:** 15 of 16 accounts tested passed. 1 exception (account #8, contractor access not removed timely).

### Exception Detail: Account #8

**Account:** henry.contractor@secureconsult.example

**System:** AWS IAM Identity Center, production accounts

**Issue:** Contractor engagement ended August 31, 2026 per contract. Access was flagged for removal during the Q3 privileged access review on October 5, 2026. Removal ticket CHG-45678 was created October 5, opened to the IAM team. Ticket was completed October 18, 2026 (9 business days late per 5-business-day SLA). Access was removed October 18, confirmed by checking AWS IAM Identity Center assignments (no active sessions, permission sets unassigned).

**Deviation:** Removal was 9 business days late (14 calendar days from review date to removal completion).

**Root Cause (inquiry with IAM Manager):** The contractor's Okta account was disabled on the termination date (August 31) per ACC-02, so he could not authenticate. However, the IAM team did not receive the termination notification from the sponsoring manager until the access review flagged it in October. The delay in creating the removal ticket and completing it was due to the ticket being assigned to a team member who was on PTO, and no escalation occurred until the IAM Manager manually reviewed overdue tickets on October 17.

**Compensating Control Assessment:** The contractor's Okta account was disabled on the termination date, so even though his AWS permission set assignments were not removed until October 18, he could not authenticate through Okta SSO to reach AWS. No AWS access occurred between August 31 and October 18 (confirmed by checking CloudTrail logs for the user's identity; zero events). The late removal had no security impact because the authentication layer (Okta) was already disabled.

**Impact on Control Effectiveness:** The control operated as designed for 15 of 16 accounts. The one exception was an isolated operational failure (assignee on PTO, no escalation), not a systemic control design failure. The compensating control (Okta deactivation at termination) prevented unauthorized access.

**Auditor's Determination:** Exception is noted as an isolated deviation, not a control deficiency. Recommend management implement an escalation rule in ServiceNow for overdue removal tickets (auto-assign to IAM Manager if open > 3 business days).

**Remediation (documented in ticket CHG-45678):** IAM Manager added a ServiceNow business rule on November 1, 2026 to auto-escalate access removal tickets open longer than 3 business days. Tested by creating a test ticket and confirming auto-assignment after 3 days.

**How This Would Be Reported:**

- **PCI ROC:** Noted as an observation (not a compensatory control deficiency) in the testing details for Requirement 7.2.4. QSA confirms remediation was implemented.
- **SOC 2 Type 2:** Noted in the testing of CC6.2/CC6.3 as "one instance of untimely removal, compensating control operated effectively, management implemented corrective action." Does not rise to a reportable exception because the underlying authentication control prevented access.
- **SOX ITGC:** Noted in the management letter as a process improvement opportunity. No impact on the financial statement audit opinion because the access was never used and the delay was isolated.
- **GovRAMP:** Reported on the POA&M as a finding, closed same month after remediation implemented.

## Test Conclusion

Based on the test procedures performed, the control is designed and operating effectively, with one isolated exception remediated within the same quarter. The control provides reasonable assurance that user access is reviewed periodically and inappropriate access is removed in a timely manner.

**Tested by:** [Auditor name]

**Tested on:** [Date]

**Result:** No exceptions (or "1 exception, remediated, see workpaper")
