# Test Procedure 06: Batch Job Monitoring

**Control Reference:** OPS-03

**Control Statement:** Nightly settlement, remittance, and ACH file jobs are scheduled and monitored. Failures and control-total mismatches create ServiceNow incidents that are resolved, and reruns are approved and documented.

**Control Owner:** Payment Operations Manager

**Frequency:** Daily

**Nature:** IT-dependent manual

**Type:** Detective

**Key Control:** Yes

## Control Objective

To ensure that critical nightly batch jobs run successfully, that failures are detected and resolved promptly, and that control totals reconcile to confirm data completeness and accuracy.

## Applicable Framework Requirements

- **PCI DSS v4.0.1:** Not explicitly required, but operational integrity supports data integrity obligations.
- **SOC 2:** CC7.2, CC7.4
- **NIST SP 800-53 Rev 5:** SI-4
- **SOX ITGC:** Computer Operations

## Population and Sample Size

**Population:** All nightly batch job runs for the review period (365 job runs per job type; 3 job types = approximately 1,095 job runs total).

**Sample size:** 20 to 40 batch job runs, stratified by job type (settlement, remittance, ACH file generation) and month.

## Test Steps

1. **Obtain batch job history:**
   - For AWS Lambda/Step Functions jobs (settlement, remittance): Export CloudWatch Logs or Step Functions execution history with execution ID, start time, end time, status (Succeeded/Failed), control totals (if logged).
   - For legacy batch system (ACH file generation): Export job scheduler logs (cron logs or job management tool) with job name, date, status, log file path.

2. **For each sampled batch job run:**
   - **Job ran on schedule:** Confirm the job started at the expected time (example: settlement runs at 02:00 UTC daily).
   - **Job completed successfully or failure handled:** If status = Succeeded, confirm control totals reconciled (see below). If status = Failed, confirm a ServiceNow incident was opened.
   - **Control totals reconciled:** For settlement and remittance jobs, confirm the control total log entry shows:
     - Total transaction count processed
     - Total transaction amount
     - Expected count and amount (from the source query or prior job output)
     - Variance (actual - expected)
     - Variance within acceptable tolerance (example: $0.00 for settlement; tolerance defined in policy)
   - **Failures handled:**
     - For a sampled failure (if any), confirm a ServiceNow incident was created automatically or manually.
     - Confirm the incident was assigned to the Payment Operations team.
     - Confirm the incident was resolved (root cause documented, job rerun approved and completed).
     - Confirm the rerun was approved by the Payment Operations Manager or Director of IT Operations before execution (no automatic reruns without approval).

3. **Test a mismatch scenario (if available):**
   - If a control-total mismatch occurred during the period (example: settlement job calculated $1,234,567.89 but expected $1,234,560.00, variance $7.89), confirm:
     - Incident was opened.
     - Root cause was investigated (example: late transaction posted after the source query ran).
     - Mismatch was resolved or accepted with documented justification.

## Sample Attributes

| Attribute | Expected | How to Test |
|-----------|----------|-------------|
| Job ran on schedule | Start time ≈ scheduled time (within 5 minutes) | Compare job start timestamp to schedule |
| Job completed successfully | Status = Succeeded, no errors | Inspect job log |
| Control totals reconciled | Variance = $0.00 or within tolerance | Inspect control total log entry or report |
| Failure opened incident | Incident created for failed jobs | Search ServiceNow incidents for job name and date |
| Incident resolved | Status = Resolved or Closed | Inspect incident record |
| Rerun approved | Approval documented before rerun | Inspect ServiceNow incident approval history or comment |

## Exception Example

**Exception:** Settlement job on June 15, 2026 failed at 02:05 UTC due to a temporary database connection timeout. The job was rerun at 02:45 UTC by the on-call Payment Operations engineer without documented approval. The rerun succeeded. A ServiceNow incident (INC-34567) was created at 02:10 UTC and closed at 03:00 UTC with the note "job rerun successful."

**Root Cause:** The on-call engineer followed the verbal approval process (called the Payment Operations Manager, received verbal approval to rerun), but the approval was not documented in the ServiceNow incident before the rerun.

**Compensating Control:** The rerun was approved verbally, and the job rerun was logged in the incident record. The Payment Operations Manager confirmed the verbal approval occurred (inquiry with the manager).

**Remediation:** Updated the incident response runbook to require documenting approval in the ServiceNow incident comments before executing a rerun. Training reminder sent to the Payment Operations team on June 20, 2026.

**Impact:** Isolated procedural gap, not a control design failure. The job rerun was authorized, and the control total reconciled after the rerun (variance $0.00).
