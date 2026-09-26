# Test Procedure 05: Backup and Restore

**Control Reference:** OPS-01, OPS-02

**Control Statement:** AWS Backup plans take daily backups of production RDS and critical EBS volumes with 35-day retention, cross-region copy, and vault lock. The legacy batch database is backed up nightly to encrypted storage. Backup failures open a ServiceNow incident. Restores of the payment database and the legacy batch database are tested quarterly. Data integrity is checked and results are documented and reviewed.

**Control Owner:** IT Operations Manager

**Frequency:** Daily (backups), Quarterly (restore tests)

**Nature:** Automated (backups), Manual (restore tests)

**Type:** Corrective

**Key Control:** Yes (OPS-01), Yes (OPS-02)

## Control Objective

To ensure that critical systems and data can be recovered in the event of data loss, corruption, or disaster, and that backups are tested to confirm recoverability.

## Applicable Framework Requirements

- **PCI DSS v4.0.1:** Not explicitly required, but implied by business continuity obligations and operational resilience.
- **SOC 2:** A1.2 (backups), A1.3 (restore testing)
- **NIST SP 800-53 Rev 5:** CP-9, CP-9(8), CP-9(1), CP-4
- **SOX ITGC:** Computer Operations

## Population and Sample Size

**Backup jobs (OPS-01):**

- **Population:** All daily backup jobs for the review period (365 job runs for the payment database, 365 for the legacy database).
- **Sample size:** 20 to 40 backup job runs, stratified by month and system.

**Restore tests (OPS-02):**

- **Population:** Quarterly restore tests (4 per year per system, 8 total for the payment database and legacy database).
- **Sample size:** 2 restore tests, one per system, from the review period.

## Test Steps for OPS-01 (Backups)

1. **Obtain backup job history:**
   - AWS Backup: Use AWS Backup Audit Manager to export job history with job ID, resource (RDS instance ID, EBS volume ID), start time, end time, status, backup vault, recovery point retention.
   - Legacy batch system: Export backup script logs from the server showing date, database name, backup file path, status.

2. **For each sampled backup job:**
   - Confirm the job ran on the scheduled date (daily).
   - Confirm the job completed successfully (status = Completed, no errors in logs).
   - Confirm retention is set correctly (35 days for AWS Backup, 35 days for legacy).
   - Confirm cross-region copy is enabled (AWS Backup only; check recovery points in secondary region).
   - Confirm vault lock is enabled (AWS Backup only; immutable backups cannot be deleted before retention expires).

3. **Test backup failure alerting:**
   - Ask IT Operations Manager to show a recent backup failure incident (or simulate one in a test environment).
   - Confirm a ServiceNow incident was opened automatically (integration between AWS Backup / backup script and ServiceNow).
   - Confirm the incident was assigned to the correct team and resolved.

## Test Steps for OPS-02 (Restore Tests)

1. **Obtain restore test documentation:**
   - For each quarterly restore test, obtain the test record with: date performed, tester name, database restored (payment or legacy), restore target (test environment, not production), data integrity checks performed, result (pass/fail), reviewer sign-off.

2. **For the sampled restore test:**
   - Confirm the test was performed quarterly (four times per year, approximately 90 days apart).
   - Confirm the restore was to a non-production environment (restoring to production would overwrite live data).
   - Confirm data integrity checks were performed:
     - **Row count comparison:** Number of rows in restored database matches the backup source at the time the backup was taken.
     - **Checksum comparison:** For critical tables (example: transactions table), a checksum or hash of the data matches the source.
     - **Sample query:** A sample transaction or record was queried and confirmed readable.
   - Confirm the test result is documented (pass/fail).
   - Confirm a reviewer signed off (IT Operations Manager or Director of IT Operations).

## Sample Attributes

| Attribute | Expected | How to Test |
|-----------|----------|-------------|
| Backup job ran daily | Job exists for each day | Check job history for gaps |
| Backup completed successfully | Status = Completed | Inspect job log |
| Retention set correctly | 35 days | Check backup plan configuration or job metadata |
| Cross-region copy enabled | Recovery points exist in secondary region | Query AWS Backup for secondary region recovery points |
| Vault lock enabled | Vault lock status = Enabled | Inspect AWS Backup vault settings |
| Failure alert opened incident | Incident created when job fails | Test or inspect a past failure incident |
| Restore test performed quarterly | Four tests per year | Check test documentation dates |
| Data integrity verified | Row count, checksum, sample query documented | Inspect test record |
| Reviewer sign-off | Signature or approval present | Inspect test record |

## Exception Example

**Exception:** Restore test for Q2 2026 (payment database) was performed on July 8, 2026, which is 98 days after the Q1 restore test (April 1, 2026). Policy requires quarterly (approximately 90 days).

**Root Cause:** The IT Operations Manager who normally performs restore tests was on extended leave in late June, and the backup restore test was not assigned to a backup team member. The test was completed 8 days late when the manager returned.

**Compensating Control:** Daily backups continued to run successfully during the period (confirmed by sampling daily backup jobs for June 2026). No data loss occurred, and the late restore test confirmed that backups were recoverable.

**Remediation:** Cross-training plan implemented for restore test procedures; a backup team member (senior systems administrator) was trained and added to the quarterly restore test schedule.
