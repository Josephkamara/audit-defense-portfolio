# Evidence Quality Checklist

**Fictional company, sample data, for portfolio demonstration only.**

## Purpose

This checklist ensures that evidence provided to auditors meets quality standards for completeness, accuracy, and auditability. Poor-quality evidence leads to re-requests, delays, and audit findings.

## Checklist

Use this checklist before submitting evidence to the PCI QSA, SOC service auditor, or GovRAMP 3PAO.

### 1. Is the evidence system-generated?

**Preferred:** CSV export, JSON log file, API output, database query result, CLI output.

**Acceptable with caveats:** Screenshot (only if the system does not export data, and only if parameters and timestamps are visible).

**Not acceptable as sole evidence:** Manually created Excel file with no source data export, Word document describing what the control owner says happened, email saying "this control is working."

**Why it matters:** Auditors trust system-generated evidence more than human-created summaries because system-generated evidence is harder to manipulate.

### 2. Are the query parameters and filters visible?

If the evidence is a report or export, can the auditor see:

- What was queried? (example: "All active Okta users")
- What filters were applied? (example: "Status = Active, exported 2026-09-15")
- What date range? (example: "Logs from 2026-01-01 to 2026-09-30")
- Who ran the query? (example: username or API key ID)
- When was it exported? (example: timestamp on the file or in the report header)

**Why it matters:** Without parameters, the auditor cannot verify that the evidence covers the right population or period. They will ask you to re-run the query with parameters documented.

### 3. Does the population reconcile?

If the control says "all terminated users" or "all access requests," does the population in your evidence reconcile to the source of truth?

**Example:**

- Evidence: Okta System Log showing 12 user deactivation events in Q3 2026.
- Source of truth: HRIS termination report showing 12 terminations in Q3 2026.
- Reconciliation: 12 = 12, population is complete.

If the numbers do not match, document the difference:

- Are there terminations in the HRIS that are not in Okta? (Why? Contractor not in Okta? Termination date in the future?)
- Are there deactivations in Okta that are not in the HRIS? (Why? Manual deactivation? Duplicate account cleanup?)

**Why it matters:** Auditors test completeness. If the population is incomplete, they cannot rely on the test results.

### 4. Is the evidence in an editable format without the source?

**Not acceptable:** An Excel file where the control owner exported data from ServiceNow, pasted it into Excel, added manual columns (example: "Reviewed by: Jane"), and sent only the Excel file.

**Acceptable:** The original ServiceNow CSV export AND the Excel file with the manual columns, so the auditor can trace the Excel data back to the source.

**Why it matters:** If the evidence is only an editable file, the auditor cannot verify that the data is accurate. They will ask for the source export.

### 5. Does the evidence tie to the period under audit?

- SOC 2 Type 2: 12 months (example: October 1, 2025 to September 30, 2026).
- PCI DSS ROC: The assessment period (typically 12 months).
- GovRAMP ConMon: Monthly (current month and prior 11 months).
- SOX ITGC: The financial statement period (typically fiscal year).

If the evidence covers only 10 months and says "the last two months were the same," that is not acceptable. The auditor will ask for evidence for all 12 months.

**Why it matters:** The opinion covers a specific period. Evidence outside that period does not count.

### 6. Is reviewer sign-off present where required?

If the control statement says "reviewed by management" or "approved by the Director of IT Operations," the evidence must show:

- Who reviewed or approved (name and title)
- When they reviewed or approved (date)
- What they reviewed (the specific report, campaign, or results)
- What decision they made (approved, escalated, remediation required)

**Acceptable:** Email from the Director with "I reviewed the Q3 access review results, approved," dated October 10, 2026, with the access review summary attached.

**Not acceptable:** The access review summary with no email, no signature, and the control owner saying "the Director reviewed it verbally."

**Why it matters:** Verbal approvals are not auditable. The auditor will ask for documented approval.

### 7. Are samples stratified appropriately?

When the population is large (example: 1,500 access requests per year), the auditor will sample. Your evidence should include the full population export, not just the sampled items.

**Good practice:** Provide the full population export (example: all 1,500 access requests) plus a clearly marked sample selection showing which 25 to 60 requests the auditor should test.

**Why it matters:** The auditor needs to verify that the sample was drawn from the complete population, not cherry-picked.

### 8. Are exceptions documented?

If a control operated 15 times successfully and failed once, document the exception:

- What was the deviation? (example: access removed 4 business days past the 5-day standard)
- What was the root cause? (example: direct assignment outside Okta groups; assignee on PTO, no escalation)
- Were there mitigating factors? (example: identity provider account disabled at termination, no logged activity)
- What remediation was implemented? (example: auto-escalation rule added to ServiceNow)

**Why it matters:** Auditors expect exceptions. Hiding exceptions or claiming 100% success when there were failures erodes trust. Documenting exceptions and remediation shows control maturity.

### 9. Are timestamps in the correct timezone?

If your systems log in UTC but your policy says "within 1 business day" (which depends on business hours in your local timezone), clarify the timezone in the evidence.

**Example:** "Access removal completed within 1 business day. Termination date: May 15, 2026 08:00 Eastern. Removal completed: May 15, 2026 20:00 UTC (16:00 Eastern), same business day."

**Why it matters:** Timezone confusion leads to false findings (the auditor thinks you were late when you were not).

### 10. Are file names and folder structure clear?

**Good:**

- `PBC-012_ACC-04_Q3-2026_Access-Review-Campaign-Export.csv`
- `PBC-012_ACC-04_Q3-2026_Removal-Tickets.pdf`
- `PBC-012_ACC-04_Management-Signoff-Email.pdf`

**Bad:**

- `export.csv`
- `file1.pdf`
- `Screenshot 2026-09-15 at 3.42.18 PM.png`

**Why it matters:** Auditors receive hundreds of files. Clear file names tied to PBC request IDs save time and reduce errors.

## Avoiding Re-Requests Across PCI, SOC, and GovRAMP

Keystone is assessed by three different parties: the PCI QSA, the CPA firm that issues SOC 1 and SOC 2, and the GovRAMP 3PAO. They all ask for overlapping evidence, but they phrase the requests differently.

### One Control, Many Evidence Requests

**Example: ACC-06 (MFA for CDE access)**

- **PCI QSA asks:** "Provide evidence that MFA is enforced for all non-console access into the CDE per 8.4.2, and for all remote access that could reach the CDE per 8.4.3."
- **SOC auditor asks:** "Provide evidence that multi-factor authentication is required per CC6.1."
- **GovRAMP assessor asks:** "Provide evidence of IA-2(1), IA-2(2), and IA-2(8) implementation."
- **SOC 1 service auditor asks:** "Provide evidence supporting the logical access control objective for the payment database."

**The evidence is the same for all four:**

1. Okta authentication policy configuration showing MFA enforcement (screenshot or policy export).
2. Okta System Log showing per-session MFA challenges for a sample of logins (JSON or CSV export).
3. MFA exception register (if any exceptions exist).

**How to avoid re-requests:**

- Map the control in advance using the unified control matrix. ACC-06 maps to PCI 8.4.1 to 8.4.3, SOC 2 CC6.1 and CC6.6, NIST IA-2 enhancements, and the SOC 1 access objective.
- When the PCI QSA requests evidence for 8.4.2, provide the evidence once and note: "This evidence also satisfies SOC 2 CC6.1, NIST IA-2, and SOX ITGC access controls."
- Give each auditor a copy of the same evidence file, with the PBC request ID updated to match their request list. Do not re-export the same Okta System Log three times with three different filenames.

### Evidence Repository Structure

Keystone uses a shared Google Drive folder for audit evidence, organized by control ID (not by auditor):

```
Audit Evidence 2026/
  ACC-01 User Provisioning/
    ServiceNow-Access-Request-Export-2026.csv
    Sample-Access-Requests-with-Approvals.pdf
  ACC-04 Access Review/
    Q1-2026-Privileged-Access-Review-Export.csv
    Q2-2026-Privileged-Access-Review-Export.csv
    Q3-2026-Privileged-Access-Review-Export.csv
    Q4-2026-Privileged-Access-Review-Export.csv
    Management-Signoff-Emails.pdf
  ACC-06 MFA/
    Okta-Authentication-Policy-Config.pdf
    Okta-System-Log-MFA-Challenges-Sample.csv
    MFA-Exception-Register.xlsx
```

Each auditor gets a shared link to the relevant folders, not separate copies of the evidence.

### Cross-Reference Document

Create a one-page mapping document for the auditors:

| Control ID | PCI DSS Req | SOC 2 TSC | NIST 800-53 | SOX ITGC | Evidence Location |
|------------|-------------|-----------|-------------|----------|-------------------|
| ACC-01 | 7.2.1, 7.2.2, 8.2.1 | CC6.2, CC6.3 | AC-2, AC-6 | Access | `ACC-01 User Provisioning/` |
| ACC-04 | 7.2.4 | CC6.2, CC6.3 | AC-2, AC-6(7) | Access | `ACC-04 Access Review/` |
| ACC-06 | 8.4.1, 8.4.2, 8.4.3, 8.5.1 | CC6.1, CC6.6 | IA-2(1), IA-2(2), IA-2(8) | Access | `ACC-06 MFA/` |

Give this mapping to each auditor at the start of the audit. They can see that one piece of evidence satisfies multiple requests and avoid asking for the same thing twice.

## Evidence Quality Failures (Examples)

### Failure: Screenshot with no parameters

**What the auditor received:** A screenshot of the Okta user list showing 150 active users.

**What was missing:** The screenshot does not show the filter ("Status = Active"), the date the screenshot was taken, or the total user count if pagination is in use.

**Result:** Auditor asked for a CSV export with parameters visible. Three-day delay.

### Failure: Excel file with no source

**What the auditor received:** An Excel file showing 25 access requests with manager approval dates, created by the IAM Manager.

**What was missing:** The source ServiceNow export showing the same data.

**Result:** Auditor asked for the ServiceNow CSV export to verify the Excel file was accurate. Two-day delay.

### Failure: Incomplete population

**What the auditor received:** Okta System Log showing 10 user deactivation events in Q3 2026.

**What was missing:** The HRIS termination report showing 12 terminations in Q3 2026. Two terminations are missing from the Okta log.

**Result:** Auditor asked why the population is incomplete. Root cause: two contractors were never added to Okta (they only had legacy batch system access). The control owner had to provide an explanation and evidence of deactivation for those two contractors from the legacy system.

### Failure: Evidence outside the audit period

**What the auditor received:** Internal vulnerability scan reports for January 2026 through November 2026 (11 months).

**What was missing:** December 2026 scan report (the audit period is January 1, 2026 to December 31, 2026).

**Result:** Auditor asked for the December scan report. One-day delay.

### Failure: No reviewer sign-off

**What the auditor received:** Q3 access review results showing all accounts were reviewed and no inappropriate access was found.

**What was missing:** Management sign-off from the Director of IT Operations.

**Result:** Auditor asked for documented management acknowledgment. The Director had reviewed it verbally but never signed off in writing. The IAM Manager had to ask the Director to send an email approval retroactively.

## Summary

High-quality evidence is:

1. System-generated, not manually created
2. Includes parameters and filters
3. Reconciles to the source of truth
4. Provided with source exports, not just editable summaries
5. Covers the full audit period
6. Includes documented reviewer sign-off where required
7. Includes the full population, not just samples
8. Documents exceptions and remediation
9. Uses clear timezones
10. Uses clear file names

Map evidence to controls once using the unified control matrix, and share the same evidence with all auditors to avoid re-requests.
