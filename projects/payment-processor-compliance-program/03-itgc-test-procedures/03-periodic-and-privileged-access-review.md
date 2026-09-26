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
| SOC 1 / ITGC | Access to Programs and Data | Periodic access reviews are performed and documented; inappropriate access is remediated in a timely manner. |

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
3. Check for mitigating factors (example: a late removal for a privileged account, but the identity provider account was disabled on the termination date and logs show no activity). In PCI DSS work, do not call this a "compensating control"; that term has a formal meaning in the standard.
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

## Sample Workpaper: Q2 2026 Privileged Access Review

**Review Period:** Q2 2026 (April 1, 2026 to June 30, 2026)

**Review Campaign ID:** SN-ACCESSREV-2026-Q2-PRIV

**Review Start Date:** July 1, 2026

**Review Completion Date:** July 9, 2026

**Population Source:** AWS IAM Identity Center permission sets for production accounts; Okta super admin group; ServiceNow admin role; GitHub org admin; legacy batch system root/sudo

**Population Count:** 16 privileged accounts

**Reviewers:** Cloud Platform Engineering Manager (AWS), IAM Manager (Okta), IT Operations Manager (ServiceNow, legacy), AppSec Lead (GitHub)

**Management Sign-off:** Director of IT Operations, signed July 10, 2026

### Sample Selection

The test procedure calls for 25 accounts, but the population has only 16 privileged accounts, so all 16 were tested (100% sample).

| # | Account Username | System | Reviewer | Decision | Certified Date | Removal Ticket | Result |
|---|------------------|--------|----------|----------|----------------|----------------|--------|
| 1 | alice.admin@keystone.example | AWS Admin | Cloud Eng Mgr | Approved | 2026-07-01 | N/A | Pass |
| 2 | bob.platform@keystone.example | AWS Admin | Cloud Eng Mgr | Approved | 2026-07-01 | N/A | Pass |
| 3 | charlie.db@keystone.example | RDS DBA | Cloud Eng Mgr | Approved | 2026-07-02 | N/A | Pass |
| 4 | david.iam@keystone.example | Okta Super Admin | IAM Manager | Approved | 2026-07-02 | N/A | Pass |
| 5 | eve.snow@keystone.example | ServiceNow Admin | IT Ops Mgr | Approved | 2026-07-02 | N/A | Pass |
| 6 | frank.gh@keystone.example | GitHub Org Admin | AppSec Lead | Approved | 2026-07-02 | N/A | Pass |
| 7 | grace.ops@keystone.example | AWS Admin | Cloud Eng Mgr | Approved | 2026-07-06 | N/A | Pass |
| 8 | henry.contractor@contractorco.example | AWS Admin | Cloud Eng Mgr | Remove | 2026-07-06 | RITM-45678 | **Exception (see below)** |
| 9 | iris.batch@keystone.example | Legacy sudo | IT Ops Mgr | Approved | 2026-07-07 | N/A | Pass |
| 10 | jack.security@keystone.example | AWS Admin | Cloud Eng Mgr | Approved | 2026-07-07 | N/A | Pass |
| 11 | karen.cloud@keystone.example | AWS Admin | Cloud Eng Mgr | Approved | 2026-07-08 | N/A | Pass |
| 12 | larry.incident@keystone.example | ServiceNow Admin | IT Ops Mgr | Approved | 2026-07-08 | N/A | Pass |
| 13 | monica.db@keystone.example | RDS DBA | Cloud Eng Mgr | Approved | 2026-07-08 | N/A | Pass |
| 14 | nathan.deploy@keystone.example | GitHub Org Admin | AppSec Lead | Approved | 2026-07-09 | N/A | Pass |
| 15 | olivia.access@keystone.example | Okta Super Admin | IAM Manager | Approved | 2026-07-09 | N/A | Pass |
| 16 | paul.batch@keystone.example | Legacy root | IT Ops Mgr | Approved | 2026-07-09 | N/A | Pass |

**Summary:** 15 of 16 accounts passed all attributes. One exception: account #8, where removal was not completed within the 5-business-day standard.

### Exception Detail: Account #8

**Account:** henry.contractor@contractorco.example (fictional contractor)

**System:** AWS IAM Identity Center, production accounts

**Facts:**
- The contractor's engagement ended Friday, May 29, 2026.
- His Okta account was disabled that day by the end date set on contractor accounts at provisioning (ACC-02).
- During a 2025 incident, two AWS permission set assignments had been made directly in IAM Identity Center instead of through an Okta group. Disabling the Okta account did not remove them.
- The Q2 review flagged them on Monday, July 6, 2026. Removal request RITM-45678 was opened the same day, due July 13.
- The request was assigned to an IAM engineer who was on PTO, and nothing escalated it. The IAM Manager found it while reviewing overdue requests on July 16.
- The assignments were removed Friday, July 17, 2026.

**Deviation:** Removal was completed 9 business days (11 calendar days) after the review flagged it. That is 4 business days past Keystone's 5-business-day standard.

**Root Cause (inquiry with IAM Manager):**
1. The offboarding workflow does not cover direct permission set assignments made outside Okta groups.
2. Removal requests do not escalate automatically when the assignee is unavailable.

**Mitigating Factors (did the delay matter?):**
- IAM Identity Center authenticates only through Okta SSO, and the Okta account was disabled on May 29.
- The IAM credential report shows no IAM user or access keys for this person.
- CloudTrail shows zero events for the identity between May 29 and July 17.

No access occurred, and the issue is limited to one account.

**Impact on Control Effectiveness:** The review worked as designed. It found the leftover access, and management acknowledged the results. The deviation is that the removal finished late. The direct-assignment gap is referred to TP-02 (termination and deprovisioning) for evaluation under ACC-02.

**Auditor's Determination:** One isolated deviation with no unauthorized access. The control operated with one exception. Recommendations: auto-escalate overdue removal requests, and check for direct assignments at offboarding.

**Remediation:**
- On August 3, 2026, the IAM Manager added a ServiceNow rule that escalates removal requests open more than 3 business days, and tested it with a sample request.
- The offboarding workflow now runs a report of the departing user's direct IAM Identity Center assignments.

**How This Would Be Reported:**

- **Internal testing:** Reported to the audit lead and the control owner as one deviation, with its root cause, mitigating factors, and remediation.
- **SOC 2 Type 2 (and SOC 1, where this control supports an access control objective):**
  - The service auditor describes the deviation in the tests of controls and results. For example: "For 1 of 16 accounts flagged for removal, access was removed 9 business days after the review, exceeding the 5-business-day requirement."
  - The auditor then decides whether the control still achieved the criterion or objective. With the mitigating evidence above, an unmodified opinion is likely.
  - Management can add a response in the report section the auditor does not give an opinion on.
- **PCI DSS ROC:**
  - A ROC has no "observation" finding. The QSA concludes whether each requirement is In Place or Not in Place.
  - The QSA would look at 8.2.5 (access for terminated users is immediately revoked) and 7.2.4 (review performed at least every six months, inappropriate access addressed, management acknowledgment).
  - Okta was disabled on the termination date and was the only way to authenticate, and the review caught and removed the leftover assignments. So In Place is supportable if the QSA agrees no other access path existed.
  - The 5-day clock is Keystone policy, not a PCI DSS requirement.
- **GovRAMP:** If the 3PAO identified this during the annual assessment, it would go on the POA&M as an AC-2 / AC-6(7) weakness until the remediation evidence is accepted.

## Test Conclusion

Based on the procedures performed, the control is designed appropriately and operated effectively during the period tested, with one isolated deviation that was remediated in August 2026.

**Tested by:** [Auditor name]

**Tested on:** [Date]

**Result:** 1 exception, remediated (see workpaper)
