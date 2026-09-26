# 12-Month Compliance Calendar and KPIs

**Fictional company, sample data, for portfolio demonstration only.**

## Purpose

This calendar shows all recurring compliance activities for Keystone Civic Payments' PCI DSS, SOC 1, SOC 2, and GovRAMP programs. It ensures that reviews, assessments, testing, and submissions occur on schedule and that no audit-critical deadline is missed.

## 12-Month Compliance Calendar (2026-2027)

| Month | PCI DSS | SOC 1 / SOC 2 | GovRAMP | Other |
|-------|---------|---------------|---------|-------|
| **January** | ASV quarterly scan (Q1); Internal vulnerability scan | SOC audit planning meeting (for period ending March 31, 2027) | Monthly ConMon submission (POA&M, scans, inventory) | Annual risk assessment kickoff |
| **February** | Segmentation penetration test (semiannual #1); PCI scope confirmation (semiannual #1) | | Monthly ConMon submission | |
| **March** | Internal vulnerability scan | SOC 2 Type 2 fieldwork begins (period ending March 31); SOC 1 Type 2 fieldwork | Monthly ConMon submission | Annual incident response tabletop exercise |
| **April** | ASV quarterly scan (Q2); Internal vulnerability scan | SOC audit fieldwork continues; Evidence requests due | Monthly ConMon submission | |
| **May** | | SOC reports issued (SOC 1 Type 2, SOC 2 Type 2) | Monthly ConMon submission | |
| **June** | Internal vulnerability scan; Policy annual review (12.1.2) | | Monthly ConMon submission | Semiannual access review (all non-privileged accounts) |
| **July** | ASV quarterly scan (Q3); Internal vulnerability scan | | Monthly ConMon submission | Annual technology EOL review (12.3.4) |
| **August** | Segmentation penetration test (semiannual #2); PCI scope confirmation (semiannual #2) | | Monthly ConMon submission | |
| **September** | Internal vulnerability scan; Annual penetration test (internal external application layer) | | Monthly ConMon submission | Annual DR test |
| **October** | ASV quarterly scan (Q4); Internal vulnerability scan; PCI ROC planning meeting | | Monthly ConMon submission | |
| **November** | Internal vulnerability scan | | Monthly ConMon submission | Annual cryptographic cipher and protocol review (12.3.3) |
| **December** | PCI DSS ROC fieldwork begins; Internal vulnerability scan | | Monthly ConMon submission; GovRAMP annual 3PAO assessment | Annual business continuity plan review |

### Quarterly Activities (Every Quarter)

- **Access reviews:** Privileged and CDE access (ACC-04), Q1/Q2/Q3/Q4
- **Operational reviews:** GOV-06 (PCI program owner confirms daily log reviews, NSC reviews, configuration standards, alert response, change management are operating)
- **Batch restore tests:** OPS-02 (payment database and legacy batch database restore tests, Q1/Q2/Q3/Q4)

### Monthly Activities (Every Month)

- **Internal vulnerability scans:** VUL-01 (authenticated scans, high/critical findings remediated and rescanned)
- **Capacity reviews:** OPS-04 (CloudWatch alarms, auto scaling, capacity planning)
- **Inventory reconciliation:** OPS-05 (in-scope system inventory reconciled, GovRAMP inventory workbook updated)
- **GovRAMP ConMon submission:** GOV-08 (POA&M, scans, inventory, executive summary)
- **Risk Committee meeting:** GOV-07 (review open issues, POA&M, remediation tracker)

### Weekly Activities (Every Week or More Often)

- **Payment page change detection:** CHG-08 (automated, runs every few hours; alerts reviewed weekly minimum per 11.6.1 TRA)

### Daily Activities (Every Day)

- **Backups:** OPS-01 (AWS Backup daily RDS and EBS, legacy batch nightly)
- **Batch job monitoring:** OPS-03 (settlement, remittance, ACH file generation; failures and control-total mismatches create incidents)
- **Log review and alert response:** LOG-03, LOG-04 (SIEM correlation rules, SOC triage, critical control failure alerts)

### Event-Driven Activities (As Needed)

- **User provisioning:** ACC-01 (access requests submitted and approved many times per day)
- **Terminations:** ACC-02 (HRIS termination triggers Okta deactivation; contractor offboarding tasks)
- **Change management:** CHG-01, CHG-02, CHG-05 (production changes require approval; deployed many times per day through CI/CD)
- **Significant change review:** CHG-06 (flagged changes trigger scope impact review, new system hardening checklist, post-change scans)
- **Vendor onboarding:** VEN-02 (security due diligence and contract review for new vendors)
- **Incident response:** IR-04 (security incidents logged, investigated, and resolved)

---

## Key Dates and Deadlines

| Event | Target Date | Owner | Notes |
|-------|-------------|-------|-------|
| PCI DSS ROC fieldwork begins | December 2026 | Director of GRC | Annual assessment; QSA on-site or remote for 2-3 weeks |
| PCI DSS ROC and AOC issued | February 2027 | Director of GRC | Annual revalidation; new AOC delivered to the acquirer, card brands, and agency customers before the prior AOC is 12 months old. All future-dated v4.0 requirements have been mandatory since March 31, 2025. |
| SOC 2 Type 2 report period ends | March 31, 2027 | Director of GRC | 12-month period (April 1, 2026 - March 31, 2027) |
| SOC 1 and SOC 2 fieldwork | March - April 2027 | Director of GRC | Auditor on-site or remote for 3-4 weeks |
| SOC 1 and SOC 2 reports issued | May 2027 | Director of GRC | Reports delivered to state agency customers |
| GovRAMP annual authorization renewal | December 2026 | Director of GRC | Submitted to GovRAMP PMO; decision within 60 days |
| Annual penetration test | September 2026 | CISO | Internal, external, and application-layer testing; retest critical/high findings |
| Segmentation testing (semiannual) | February and August 2026 | CISO | Service provider requirement (11.4.6); test all segmentation methods |
| Annual risk assessment | January - March 2026 | Director of GRC | Enterprise risk assessment with Risk Committee approval |
| Annual DR test | September 2026 | IT Operations Manager | Regional failover of payment API, legacy batch restore; results against RTO/RPO |
| Annual IR tabletop | March 2026 | Security Operations Manager | Tabletop exercise with notification procedures included |

---

## Compliance KPIs

Keystone tracks the following key performance indicators monthly and reports them to the Risk Committee.

### 1. Overdue Remediation Items

**Definition:** Number of open items in the remediation tracker (05-gap-analysis/remediation-tracker.csv) or GRC platform issue register past their target due date.

**Target:** Zero overdue high-risk items; fewer than 3 overdue medium-risk items.

**Measured:** Monthly, as of the last day of the month.

**Reported to:** Risk Committee (monthly)

**Escalation:** Any high-risk item overdue > 7 days escalates to the CISO and Director of GRC.

### 2. Access Review Completion Rate

**Definition:** Percentage of access reviews completed by the due date.

**Target:** 100% completion within 5 business days of the review campaign launch.

**Measured:** Quarterly (for privileged and CDE access); semiannually (for all other access).

**Reported to:** Risk Committee (monthly, showing the most recent completed review)

**Escalation:** If completion rate < 100%, the IAM Manager escalates to the Director of IT Operations to follow up with overdue reviewers.

### 3. Vulnerability Remediation SLA Compliance

**Definition:** Percentage of vulnerabilities remediated within the SLA (critical 15 days, high 30 days, moderate 90 days, low 180 days).

**Target:** 95% or higher.

**Measured:** Monthly, from the vulnerability management system (Tenable, Qualys, or internal tracker).

**Reported to:** Risk Committee (monthly)

**Escalation:** Vulnerabilities past SLA are added to the GovRAMP POA&M (if in GovRAMP scope) and escalated to the system owner's manager.

### 4. Control Exceptions by Domain

**Definition:** Number of control exceptions (deviations from expected control operation) identified during testing or audits, grouped by control domain (Governance, Access, Change, Operations, Logging, Vulnerability, Network, Encryption, Incident Response, Vendor, Physical, HR, Data Retention, Business Continuity).

**Target:** Fewer than 5 exceptions per quarter across all domains; zero repeat exceptions (same control failing twice).

**Measured:** Quarterly, from audit workpapers and internal testing results.

**Reported to:** Risk Committee (quarterly)

**Escalation:** Repeat exceptions trigger a root cause analysis and remediation plan approved by the Director of GRC.

### 5. GovRAMP POA&M Aging

**Definition:** Number of open POA&M items by age bucket (0-30 days, 31-60 days, 61-90 days, 90+ days).

**Target:** Zero items in the 90+ days bucket (all items closed or approved for extension by GovRAMP PMO).

**Measured:** Monthly, from the POA&M.

**Reported to:** Risk Committee (monthly); GovRAMP PMO (monthly as part of ConMon submission)

**Escalation:** Items approaching 90 days escalate to the CISO and Director of GRC for risk acceptance decision or extension request.

### 6. Audit Finding Closure Rate

**Definition:** Percentage of audit findings (from PCI ROC, SOC audit, GovRAMP assessment, or internal audit) closed within 90 days of issuance.

**Target:** 100% of high-priority findings closed within 90 days; 90% or higher for all findings.

**Measured:** Quarterly.

**Reported to:** Risk Committee (quarterly)

**Escalation:** Findings open > 90 days require a written status update to the Risk Committee and executive sponsor approval to extend the closure date.

---

## Calendar Maintenance

- **Owner:** Director of GRC
- **Update frequency:** This calendar is reviewed and updated quarterly to reflect any changes in audit schedules, new compliance obligations, or shifts in testing cadence.
- **Distribution:** Shared with all control owners, the Risk Committee, and the audit teams (PCI QSA, SOC auditor, GovRAMP assessor).

---

## Integration with Audit Schedules

### PCI DSS ROC

- **Audit period:** 12 months (typically January 1, 2026 - December 31, 2026)
- **Fieldwork:** December 2026 - January 2027
- **Report issuance:** February 2027
- **Keystone's preparation:** Evidence requests due by mid-December; PBC list provided to QSA in November.

### SOC 1 and SOC 2 Type 2

- **Audit period:** 12 months (April 1, 2026 - March 31, 2027)
- **Fieldwork:** March - April 2027
- **Report issuance:** May 2027
- **Keystone's preparation:** Evidence requests due by end of March; interim testing in December 2026.

### GovRAMP Continuous Monitoring

- **Submission frequency:** Monthly (due by the 10th of the following month)
- **Annual authorization renewal:** December 2026
- **Keystone's preparation:** POA&M and scans prepared by the 5th of each month; reviewed by Director of GRC before submission.

By following this calendar and tracking these KPIs, Keystone ensures that its multi-framework compliance program operates continuously and that audit-critical deadlines are never missed.
