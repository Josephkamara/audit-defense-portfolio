# Test Procedure 02: Termination and Deprovisioning

**Control Reference:** ACC-02

**Control Statement:** Employee terminations entered in the HRIS trigger automated Okta deactivation on the termination date. Contractor terminations are submitted by the sponsoring manager through a ServiceNow offboarding task. Accounts outside Okta (legacy batch system, database local accounts) are removed by the system owner the same business day.

**Control Owner:** IAM Manager

**Frequency:** Recurring (event-driven)

**Nature:** IT-dependent manual

**Type:** Preventive

**Key Control:** Yes

## Control Objective

To ensure that access to in-scope systems is removed promptly when an individual's employment or contractor engagement ends, preventing unauthorized access by terminated individuals.

## Applicable Framework Requirements

- **PCI DSS v4.0.1:** 8.2.5, 8.2.4
- **SOC 2:** CC6.2, CC6.3
- **NIST SP 800-53 Rev 5:** AC-2, AC-2(3), PS-4, PS-7
- **SOX ITGC:** Access to Programs and Data

## Population and Sample Size

**Population:** All employee and contractor terminations during the review period (HRIS export and contractor roster with end dates).

**Sample size:** All terminations during the period if fewer than 30; otherwise 25 to 40 terminations stratified by employee vs. contractor and month.

## Test Steps

1. **Obtain the termination population:**
   - Employee terminations: HRIS export with termination date and reason.
   - Contractor terminations: Contractor roster with end dates and sponsoring manager.
   - Reconcile to HR's official termination list to confirm completeness.

2. **For each sampled termination:**
   - **Okta deactivation:** Check Okta System Log for user.lifecycle.deactivate event. Confirm the deactivation occurred on the termination date (for employees) or within 1 business day (for contractors whose offboarding task may have been submitted the day before the last day).
   - **AWS access removal:** Check AWS IAM Identity Center assignments; confirm no active permission sets. Check AWS IAM for any lingering IAM users; confirm deleted or access keys deactivated.
   - **Legacy system accounts:** For terminated users who had legacy batch system access, SSH to the server and confirm the account is removed or disabled (`cat /etc/passwd`, `passwd -S username` to check lock status). For database accounts, confirm dropped or revoked (`psql -c "\du"`).
   - **ServiceNow offboarding task (contractors):** Confirm a ServiceNow offboarding task was created by the sponsoring manager, assigned to the IAM team, and completed same business day or next business day.

3. **Check for any lingering access:**
   - For a sample of terminated users, check current Okta directory, AWS, ServiceNow, GitHub to confirm the account is no longer active.

## Sample Attributes

| Attribute | Expected | How to Test |
|-----------|----------|-------------|
| Okta deactivation on termination date | Deactivate event date = termination date | Compare HRIS termination date to Okta log event timestamp |
| AWS access removed | No active permission sets or IAM users | Query AWS for the terminated user's identity; confirm not found or inactive |
| Legacy accounts removed same day | Account removed or disabled | Check /etc/passwd, database user list |
| Offboarding task completed (contractors) | Task created, assigned, closed same/next day | Inspect ServiceNow offboarding task |
| No lingering access | Account not present in current directory | Search Okta/AWS/etc. for the terminated user |

## Exception Example

**Exception:** One contractor termination (john.tempworker@vendor.example, end date May 15, 2026) had Okta account disabled on May 15 as expected (contractor accounts carry an end date set at provisioning), but the ServiceNow offboarding task was not created until May 22 (7 calendar days late). The offboarding task's completion triggered removal of the user's GitHub collaborator access, which was not removed until May 23.

**Root Cause:** The sponsoring manager was out of the office the week of May 15 and did not submit the offboarding task before leaving. No backup process existed for manager absences.

**Compensating Control:** The contractor's Okta account was disabled on time, so the contractor could not authenticate to GitHub through SSO. GitHub access without SSO authentication was not possible because Keystone enforces SAML SSO for the organization.

**Remediation:** HR updated the offboarding checklist to require sponsoring managers to submit contractor offboarding tasks at least 3 business days before the end date. Implemented June 1, 2026.
