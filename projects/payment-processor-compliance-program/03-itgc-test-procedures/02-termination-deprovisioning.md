# Test Procedure 02: Termination and Deprovisioning

**Control Reference:** ACC-02

**Control Statement:** Employee terminations entered in the HRIS trigger automated Okta deactivation on the termination date with SCIM deprovisioning to downstream apps (ServiceNow, GitHub, GRC platform, Splunk). Contractor terminations are submitted by the sponsoring manager through a ServiceNow offboarding task. Accounts outside Okta (legacy batch system local accounts, database local accounts) are removed manually by the system owner the same business day.

**Control Owner:** IAM Manager

**Frequency:** Recurring (event-driven)

**Nature:** Hybrid

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

**For Okta-managed accounts (employees and most contractors):** Full-population analytic. Compare every HRIS and contractor roster termination to the Okta `user.lifecycle.deactivate` timestamp, SCIM deprovision events in downstream apps (ServiceNow, GitHub, GRC platform, Splunk), and IAM Identity Center assignments. Flag any Okta deactivation later than the termination date, SCIM event later than same business day after Okta deactivation, or remaining Identity Center assignments.

**For legacy batch and database accounts:** Test all terminated users who had legacy access (expected fewer than 5 per year); if more than 25, sample 25.

**Population:** All employee and contractor terminations during the review period (HRIS export and contractor roster with end dates).

## Test Steps

1. **Obtain the termination population:**
   - Employee terminations: HRIS export with termination date and reason.
   - Contractor terminations: Contractor roster with end dates and sponsoring manager.
   - Reconcile to HR's official termination list to confirm completeness.

2. **For Okta-managed accounts (full population):**
   - Export all HRIS terminations with termination date.
   - Export all Okta `user.lifecycle.deactivate` events for the period with user identifier and timestamp.
   - Export all SCIM deprovision events from downstream apps (ServiceNow, GitHub, GRC platform, Splunk) for the period.
   - Join the exports on user identifier. Flag any row where:
     - Okta deactivation timestamp is after the HRIS termination date (should be same day)
     - SCIM deprovision timestamp in any downstream app is more than 1 business day after the Okta deactivation
   - Investigate and document any flagged exceptions.

3. **For legacy batch and database accounts (sample):**
   - For each sampled termination who had legacy system access, SSH to the server and confirm the account is removed or disabled (`cat /etc/passwd`, `passwd -S username` to check lock status). For database accounts, confirm dropped or revoked (`psql -c "\du"`).
   - Confirm removal occurred the same business day as the termination date.

4. **Check for any lingering access:**
   - For a sample of terminated users from both the Okta full-population test and the legacy system sample, check current Okta directory, AWS, ServiceNow, GitHub to confirm the account is no longer active.

## Sample Attributes

| Attribute | Expected | How to Test |
|-----------|----------|-------------|
| Okta deactivation on termination date | Deactivate event date = termination date | Full-population analytic: join HRIS terminations to Okta deactivate events and flag late deactivations |
| SCIM deprovision within 1 business day | SCIM event within 1 business day of Okta deactivation | Full-population analytic: join Okta deactivations to SCIM deprovision events in downstream apps |
| Legacy accounts removed same day | Account removed or disabled | Sample: check /etc/passwd, database user list for sampled terminations |
| No lingering access | Account not present in current directory | Sample both Okta and legacy terminated users; search Okta/AWS/GitHub/ServiceNow |

## Exception Example

**Exception:** One contractor termination (john.tempworker@vendor.example, end date May 15, 2026) had Okta account disabled on May 15 as expected (contractor accounts carry an end date set at provisioning), but the ServiceNow offboarding task was not created until May 22 (7 calendar days late). The offboarding task's completion triggered removal of the user's GitHub collaborator access, which was not removed until May 23.

**Root Cause:** The sponsoring manager was out of the office the week of May 15 and did not submit the offboarding task before leaving. No backup process existed for manager absences.

**Mitigating Factors:** The contractor's Okta account was disabled on time, so the contractor could not authenticate to GitHub through SSO. GitHub access without SSO authentication was not possible because Keystone enforces SAML SSO for the organization.

**Remediation:** HR updated the offboarding checklist to require sponsoring managers to submit contractor offboarding tasks at least 3 business days before the end date. Implemented June 1, 2026.
