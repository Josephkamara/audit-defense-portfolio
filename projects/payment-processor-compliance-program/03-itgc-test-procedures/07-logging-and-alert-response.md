# Test Procedure 07: Logging and Alert Response

**Control Reference:** LOG-03, LOG-04

**Control Statement:** SIEM correlation rules review security events and logs from CDE, critical, and security components daily. Alerts are triaged by the SOC, and exceptions are investigated and resolved. Other components are reviewed at the frequency set in the TRA. Failures of critical security control systems generate alerts. Failures are responded to promptly, with cause, duration, and remediation documented.

**Control Owner:** Security Operations Manager

**Frequency:** Daily (log review), Continuous (alert monitoring)

**Nature:** IT-dependent manual

**Type:** Detective

**Key Control:** Yes

## Control Objective

To ensure that security events and anomalies are detected through log review and alerting, that alerts are triaged and investigated promptly, and that failures of critical security controls are detected and remediated.

## Applicable Framework Requirements

- **PCI DSS v4.0.1:** 10.4.1, 10.4.1.1, 10.4.2, 10.4.2.1, 10.4.3 (log review and alert response); 10.7.2, 10.7.3 (critical control failures)
- **SOC 2:** CC7.2, CC7.3
- **NIST SP 800-53 Rev 5:** AU-6, AU-6(1), AU-6(3), SI-4, AU-5, SI-4(5)
- **SOX ITGC:** Not directly mapped (no SOX column in matrix)

## Population and Sample Size

**Log review and alerts (LOG-03):**

- **Population:** All SIEM alert queue entries for the review period (typically 500-2,000 alerts per month).
- **Sample size:** 25 to 60 alerts, stratified by alert severity (critical, high, medium, low), month, and source system.

**Critical control failures (LOG-04):**

- **Population:** All critical control failure alerts for the review period (example: GuardDuty stopped reporting, CloudTrail log file validation failed, anti-malware service stopped).
- **Sample size:** All critical control failure alerts during the period if fewer than 25; otherwise 25 alerts stratified by failure type and month.

## Test Steps for LOG-03 (Log Review and Alert Response)

1. **Obtain SIEM alert queue export:**
   - Export from Splunk (or the SIEM in use) with alert ID, date/time generated, source system, alert rule name, severity, assigned to, triage timestamp, investigation timestamp, status (Open/In Progress/Resolved/Closed), resolution notes.

2. **Confirm daily review occurred:**
   - For CDE and critical systems, confirm alerts are generated daily (or that the SIEM dashboard was accessed daily by the SOC, indicating active monitoring).
   - Check SOC shift logs or SIEM access logs to confirm a SOC analyst reviewed the alert queue each day.

3. **For each sampled alert:**
   - **Alert was triaged:** Confirm a SOC analyst assigned the alert and documented an initial triage decision (escalate, investigate, close as false positive) within the defined SLA (example: critical alerts triaged within 15 minutes, high within 1 hour, medium within 4 hours per Keystone's policy).
   - **Investigation documented:** If the alert was escalated for investigation, confirm investigation notes are present in the alert record (what was checked, findings, root cause if identified).
   - **Resolution or escalation:** Confirm the alert was closed with a documented resolution (false positive, benign, remediated, escalated to incident response).
   - **Incident created if warranted:** If the alert indicated a real security event (example: GuardDuty finding a compromised instance), confirm a ServiceNow incident was created and linked to the alert.

4. **Test automated log review mechanisms (PCI 10.4.1.1):**
   - Confirm SIEM correlation rules exist and are enabled (example: rule for failed SSH login attempts, rule for AWS root account usage, rule for database access from unauthorized IP).
   - Confirm at least one rule has generated an alert during the period (evidence the rule is active, not just configured).

## Test Steps for LOG-04 (Critical Control Failures)

1. **Obtain critical control failure alert history:**
   - Export from SIEM or monitoring tool showing heartbeat/health check alerts for critical controls: network security controls (firewall rule changes), IDS/IPS, change detection (CHG-08), anti-malware (EDR), physical access control alerts (colocation facility), logical access control alerts (Okta service status), audit logging (CloudTrail, VPC Flow Logs), segmentation (security group changes), log review itself (SIEM ingestion lag), automated security testing (vulnerability scans, penetration tests).

2. **For each sampled critical control failure alert:**
   - **Alert was generated:** Confirm an alert was created when the control failure occurred.
   - **Response was prompt:** Confirm the alert was acknowledged and investigated within the defined SLA (example: critical control failures escalated to Security Operations Manager within 30 minutes).
   - **Cause documented:** Confirm the root cause is documented in the alert or incident record (example: "GuardDuty stopped reporting due to AWS service disruption, confirmed by AWS status page").
   - **Duration documented:** Confirm the start and end time of the failure is documented (when the alert fired, when the control was restored).
   - **Remediation documented:** Confirm the action taken to restore the control is documented (example: "CloudTrail re-enabled, log file validation confirmed, backfilled logs from S3 bucket").

## Sample Attributes for LOG-03

| Attribute | Expected | How to Test |
|-----------|----------|-------------|
| Daily review occurred | Alert queue accessed or reviewed daily | Check SOC shift logs or SIEM access logs |
| Alert triaged within SLA | Triage timestamp - alert generated timestamp ≤ SLA | Calculate time difference |
| Investigation documented | Investigation notes present for escalated alerts | Inspect alert record |
| Resolution documented | Alert status = Resolved or Closed, with resolution notes | Inspect alert record |
| Incident created if warranted | ServiceNow incident linked for real security events | Trace alert to incident (if applicable) |
| Automated rules enabled | SIEM correlation rules active and generating alerts | Inspect SIEM rule list and sample alert generated by rule |

## Sample Attributes for LOG-04

| Attribute | Expected | How to Test |
|-----------|----------|-------------|
| Failure alert generated | Alert exists for the failure | Search SIEM or monitoring tool for alert |
| Response within SLA | Acknowledged timestamp - alert generated timestamp ≤ SLA | Calculate time difference |
| Cause documented | Root cause field or comment is filled | Inspect alert or incident record |
| Duration documented | Start and end timestamps present | Inspect alert or incident record |
| Remediation documented | Action taken to restore control is documented | Inspect alert or incident record |

## Exception Example for LOG-03

**Exception:** One high-severity alert (ALERT-78901, generated September 10, 2026 at 08:45 UTC, rule "Excessive failed AWS API calls from single IAM user") was not triaged until 10:15 UTC (1 hour 30 minutes after generation). Policy requires high-severity alerts to be triaged within 1 hour.

**Root Cause:** The SOC analyst on shift was handling a concurrent critical alert (a GuardDuty finding of a compromised EC2 instance, which took priority). The excessive failed API calls alert was queued behind the critical alert. Once the critical alert was escalated to the Security Operations Manager, the analyst triaged the high-severity alert.

**Compensating Control:** The failed API calls were investigated and determined to be a misconfigured CI/CD script (not an attack). The script was corrected. The 30-minute delay in triage did not result in any security impact.

**Remediation:** Recommended adding a second SOC analyst during peak hours (business day coverage) to reduce triage queue delays. Management approved additional staffing, implemented October 2026.

## Exception Example for LOG-04

**Exception:** A CloudTrail log file validation failure alert (ALERT-99234, generated August 5, 2026 at 14:00 UTC) was acknowledged but not documented with root cause or remediation steps. The alert was closed August 5 at 15:30 UTC with status "Resolved" and no notes.

**Root Cause (inquiry with Security Operations Manager):** The analyst who investigated the alert verbally reported the issue to the manager (AWS service-side delay in log file validation, no actual tampering detected), but did not document the investigation in the alert record. The manager closed the alert after confirming the issue was benign.

**Compensating Control:** CloudTrail logs were intact and unchanged (confirmed by spot-checking log files in S3 and verifying their signatures). No security impact occurred.

**Remediation:** Updated SOC procedures to require documenting the investigation outcome in the alert record before closing, even for false positives or benign findings. Training reminder sent to SOC team August 10, 2026.
