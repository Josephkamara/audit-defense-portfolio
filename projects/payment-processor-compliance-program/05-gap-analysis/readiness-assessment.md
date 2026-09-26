# Readiness Assessment and Gap Analysis

**Fictional company, sample data, for portfolio demonstration only.**

## Overview

This readiness assessment identifies gaps in Keystone Civic Payments' compliance program against PCI DSS v4.0.1 (including future-dated requirements that became mandatory March 31, 2025), SOC 2 Type 2, and GovRAMP Moderate. Gaps are rated by risk (likelihood × impact), prioritized for remediation, and tracked to closure in the remediation tracker.

## Risk Rating Method

Keystone uses a 3×3 risk matrix:

**Likelihood:**

- **High (3):** Gap exists in multiple systems or affects a large population; likely to be exploited or result in a finding.
- **Medium (2):** Gap exists in one or two systems; could result in a finding under certain conditions.
- **Low (1):** Gap is minor or affects a small population; unlikely to result in a finding.

**Impact:**

- **High (3):** Gap could lead to a PCI DSS compensating control or finding, SOC 2 qualified opinion, GovRAMP authorization denial, or unauthorized access to cardholder data.
- **Medium (2):** Gap could lead to an observation in a report, increase audit testing, or result in a management letter comment.
- **Low (1):** Gap is a best-practice deviation with no expected audit impact.

**Risk Score:** Likelihood × Impact (scale of 1 to 9)

**Priority:**

- **High risk (7-9):** Remediate immediately (within 30 days).
- **Medium risk (4-6):** Remediate within 90 days.
- **Low risk (1-3):** Remediate within 180 days or accept the risk with documented justification.

## Gap Summary

The assessment identified 15 gaps across PCI DSS, SOC 2, and GovRAMP Moderate requirements. Of these:

- **2 high-risk gaps** (scores 8 and 7): Require immediate remediation.
- **8 medium-risk gaps** (scores 4 to 6): Require remediation within 90 days.
- **5 low-risk gaps** (scores 2 to 3): Require remediation within 180 days or risk acceptance.

As of this assessment (September 2026), 8 gaps have been remediated, 5 are in progress, and 2 are pending resource allocation.

## Gap Detail

### GAP-001: Phishing-Resistant MFA Not Fully Enforced for All CDE Access (PCI DSS 8.4.3)

**Framework:** PCI DSS v4.0.1

**Requirement:** 8.4.3 - MFA is implemented for all access into the CDE (not just non-console access). This requirement became mandatory March 31, 2025 (previously a future-dated requirement).

**Current State:** Keystone enforces phishing-resistant MFA (FIDO2) for all workforce access through Okta, including console access to AWS and remote access. However, AWS console access for break-glass emergency scenarios uses IAM users with MFA (time-based one-time passwords, TOTP), not FIDO2. TOTP is not phishing-resistant per PCI SSC guidance.

**Gap:** Break-glass IAM user MFA is TOTP, not phishing-resistant.

**Likelihood:** Low (1) - Break-glass access is rarely used (2-3 times per year) and is logged and reviewed.

**Impact:** High (3) - PCI DSS 8.4.3 non-compliance could result in a finding, not just an observation.

**Risk Score:** 3 (Low risk, but high impact if auditor flags it)

**Remediation:** Transition break-glass IAM users to use hardware security keys (YubiKey or AWS-supported FIDO2 keys) instead of TOTP. Target completion: November 2026.

**Owner:** Cloud Platform Engineering Manager

**Status:** In progress (hardware keys ordered, policy update in review)

---

### GAP-002: Automated Log Review Mechanisms Not Fully Implemented for All CDE Components (PCI DSS 10.4.1.1)

**Framework:** PCI DSS v4.0.1

**Requirement:** 10.4.1.1 - Automated mechanisms are used to perform log reviews (became mandatory March 31, 2025).

**Current State:** Keystone's SIEM (Splunk) has correlation rules that review logs from most CDE components (payment API, databases, AWS infrastructure). However, logs from the legacy batch system (colocation) are forwarded to Splunk but are reviewed manually by the IT Operations Manager once per day, not through automated correlation rules.

**Gap:** Legacy batch system logs are not reviewed through automated mechanisms; they rely on manual review.

**Likelihood:** Medium (2) - The manual review occurs daily, but a missed review or delayed response is possible.

**Impact:** Medium (2) - PCI DSS 10.4.1.1 non-compliance could result in an observation or finding depending on the QSA's interpretation (the requirement allows for a targeted risk analysis to justify manual review for certain components, which Keystone has not documented).

**Risk Score:** 4 (Medium risk)

**Remediation:** Option 1: Create SIEM correlation rules for the legacy batch system logs (similar to the rules used for AWS infrastructure). Option 2: Document a targeted risk analysis (TRA) justifying manual review for the legacy system due to low transaction volume and planned migration to AWS in 2027. Keystone chose Option 2 (TRA). Target completion: October 2026.

**Owner:** Security Operations Manager

**Status:** Completed (TRA documented and reviewed, filed under GOV-04)

---

### GAP-003: Payment Page Change Detection Not Running Every 7 Days (PCI DSS 11.6.1 TRA)

**Framework:** PCI DSS v4.0.1

**Requirement:** 11.6.1 - A change- and tamper-detection mechanism is deployed to alert personnel to unauthorized changes to the payment page. If not run at least once every seven days, a targeted risk analysis (TRA) is performed and documented per 12.3.1.

**Current State:** Keystone's payment page change detection service (third-party tool) runs every few hours (approximately every 3 hours), which exceeds the minimum weekly frequency. However, the TRA required by 11.6.1 was not documented when the tool was configured in 2024.

**Gap:** No documented TRA for the frequency choice (even though the actual frequency exceeds the minimum). PCI DSS 11.6.1 explicitly requires a TRA if the frequency is not weekly, regardless of whether the chosen frequency is more or less frequent.

**Likelihood:** Low (1) - The control is operating more frequently than required; the gap is documentation only.

**Impact:** Medium (2) - A QSA will ask for the TRA; not having it documented is a documentation gap, not a control gap.

**Risk Score:** 2 (Low risk)

**Remediation:** Document a TRA for PCI DSS 11.6.1 justifying the every-few-hours frequency. Target completion: October 2026.

**Owner:** Director of GRC

**Status:** Completed (TRA documented October 2026, filed under GOV-04)

---

### GAP-004: Service Account Access Review Frequency Not Documented (PCI DSS 7.2.5.1 TRA)

**Framework:** PCI DSS v4.0.1

**Requirement:** 7.2.5.1 - Application and system accounts are reviewed periodically at a frequency defined in a targeted risk analysis.

**Current State:** Keystone reviews service accounts semiannually per the access review process (ACC-08). However, the TRA required by 7.2.5.1 to justify the semiannual frequency was not documented.

**Gap:** No documented TRA for service account review frequency.

**Likelihood:** Low (1) - The review is operating at a reasonable frequency; the gap is documentation only.

**Impact:** Medium (2) - A QSA will ask for the TRA.

**Risk Score:** 2 (Low risk)

**Remediation:** Document a TRA for PCI DSS 7.2.5.1 justifying the semiannual frequency based on service account risk profile (least privilege, credentials stored in Secrets Manager with rotation, no interactive login). Target completion: October 2026.

**Owner:** Director of GRC

**Status:** Completed (TRA documented October 2026, filed under GOV-04)

---

### GAP-005: Insufficient Role-Based Access Documentation for SOC 2 CC6.2

**Framework:** SOC 2

**Requirement:** CC6.2 - Prior to issuing system credentials and granting system access, the entity registers and authorizes new internal and external users whose access is administered by the entity. For those users whose access is administered by the entity, user system credentials are removed when user access is no longer authorized.

**Current State:** Keystone grants access based on role-based Okta groups, but the role matrix (job title → Okta groups → application access) is maintained in a shared Google Sheet that is not version-controlled and is not formally approved by management each year.

**Gap:** Role matrix is informal and not formally approved or version-controlled.

**Likelihood:** Low (1) - The role matrix is actively used and reasonably accurate, but the lack of formal approval could be flagged by a SOC auditor.

**Impact:** Medium (2) - SOC 2 observation possible; unlikely to rise to a control deficiency unless the matrix is found to be inaccurate.

**Risk Score:** 2 (Low risk)

**Remediation:** Formalize the role matrix: move it to a version-controlled repository (GitHub or ServiceNow), add an approval workflow (Director of IT Operations approves annually), and reference it in the access provisioning policy. Target completion: December 2026.

**Owner:** IAM Manager

**Status:** In progress (draft role matrix created in ServiceNow, pending approval workflow)

---

### GAP-006: SOC 2 Availability Monitoring for Customer Portal Incomplete

**Framework:** SOC 2

**Requirement:** A1.1 - The entity maintains, monitors, and evaluates current processing capacity and use of system components (infrastructure, data, and software) to manage capacity and to enable the implementation of additional capacity to help meet its objectives.

**Current State:** Keystone monitors capacity for the payment API tier (CloudWatch alarms, auto scaling) but does not have formal capacity monitoring for the customer portal (which is in SOC 2 scope for Availability). The portal is a static site (S3 + CloudFront) with no scaling constraints, but the lack of documented capacity monitoring could be flagged by a SOC auditor.

**Gap:** No documented capacity monitoring for the customer portal.

**Likelihood:** Low (1) - The portal is a static site with effectively unlimited capacity; a real availability issue is unlikely.

**Impact:** Low (1) - SOC auditor may note this as a best-practice gap, but it is unlikely to affect the opinion given the portal's architecture.

**Risk Score:** 1 (Low risk)

**Remediation:** Add CloudWatch alarms for CloudFront request count and error rate; document in the monthly capacity review record that the customer portal was reviewed and no capacity constraints were identified. Target completion: December 2026.

**Owner:** Cloud Platform Engineering Manager

**Status:** Pending (low priority)

---

### GAP-007: GovRAMP POA&M Not Updated Within 30 Days for One Finding

**Framework:** GovRAMP Moderate

**Requirement:** Continuous Monitoring - POA&M must be updated within 30 days of a new finding or a change in status.

**Current State:** In July 2026, an internal vulnerability scan identified a high-severity finding (CVE-2026-12345, Apache Tomcat vulnerability) on the payment API tier. The finding was remediated within 15 days (patched July 20, 2026) and confirmed by rescan July 22. However, the POA&M was not updated to reflect the new finding and closure until the August monthly submission (August 5, 2026), which is 36 days after the initial finding.

**Gap:** POA&M was updated 6 days late (36 days instead of 30 days).

**Likelihood:** Low (1) - The delay was isolated; the finding was remediated promptly, and the late POA&M update was due to the monthly submission cycle, not a control failure.

**Impact:** Low (1) - GovRAMP PMO may note the late update, but the finding was remediated on time, so the impact on authorization is minimal.

**Risk Score:** 1 (Low risk)

**Remediation:** Update the GovRAMP submission process to allow mid-month POA&M updates for high-severity findings. Target completion: Completed (process updated August 2026).

**Owner:** Director of GRC

**Status:** Completed

---

### GAP-008: Incident Responder Training Frequency Not Defined in TRA (PCI DSS 12.10.4.1)

**Framework:** PCI DSS v4.0.1

**Requirement:** 12.10.4.1 - The frequency of training for incident response personnel is defined in a targeted risk analysis (became mandatory March 31, 2025).

**Current State:** Keystone's incident responders complete annual security awareness training with all other personnel, but specific incident response training (tabletop exercises, forensics, containment procedures) is conducted annually without a documented TRA justifying the frequency.

**Gap:** No documented TRA for incident responder training frequency.

**Likelihood:** Low (1) - Training occurs annually, which is a common frequency; the gap is documentation only.

**Impact:** Medium (2) - A QSA will ask for the TRA.

**Risk Score:** 2 (Low risk)

**Remediation:** Document a TRA for PCI DSS 12.10.4.1 justifying annual training frequency based on low incident volume and low turnover in the incident response team. Target completion: October 2026.

**Owner:** Director of GRC

**Status:** Completed (TRA documented October 2026, filed under GOV-04)

---

### GAP-009: No Documentation of Non-Applicable PCI DSS Requirements

**Framework:** PCI DSS v4.0.1

**Requirement:** 12.5.2 - PCI DSS scope is documented and confirmed. This includes documenting which requirements are not applicable (if any).

**Current State:** Keystone's scope confirmation memo documents in-scope systems and data flows, but it does not explicitly state which PCI DSS requirements are not applicable. Example: Requirement A3 (PCI DSS Appendix A3, designated entities supplemental validation) is not applicable because Keystone is not a designated entity, but this is not stated in the scope confirmation.

**Gap:** Scope confirmation does not document non-applicable requirements.

**Likelihood:** Low (1) - The QSA will ask during the assessment; Keystone can clarify on the spot, but documenting it proactively is better.

**Impact:** Low (1) - Documentation gap, not a control gap.

**Risk Score:** 1 (Low risk)

**Remediation:** Update the scope confirmation memo template to include a section "Non-Applicable Requirements" and list any requirements that do not apply (example: A3). Target completion: October 2026.

**Owner:** Director of GRC

**Status:** Completed (template updated October 2026)

---

### GAP-010: AWS Config Rules Not Covering All CDE Instances

**Framework:** NIST SP 800-53 Rev 5 (GovRAMP Moderate)

**Requirement:** CM-2, CM-6 - Configuration settings are documented and enforced; deviations are detected and corrected.

**Current State:** Keystone uses AWS Config conformance packs to detect drift from the configuration standard, but the conformance pack is only deployed in the primary payment processing AWS account. The secondary account (used for cross-region backup and DR) does not have the conformance pack enabled.

**Gap:** AWS Config conformance pack not deployed in the secondary account.

**Likelihood:** Medium (2) - The secondary account is used for backups, but it also has EC2 instances for DR testing, which should be covered by the configuration standard.

**Impact:** Medium (2) - GovRAMP assessor may flag this as a CM-2/CM-6 gap.

**Risk Score:** 4 (Medium risk)

**Remediation:** Deploy the AWS Config conformance pack to the secondary account. Target completion: November 2026.

**Owner:** Cloud Platform Engineering Manager

**Status:** In progress

---

### GAP-011: Vendor SOC Report Review Checklist Not Used Consistently

**Framework:** SOC 2, PCI DSS v4.0.1

**Requirement:** CC9.2 (SOC 2), 12.8.4 (PCI DSS) - The entity obtains and reviews SOC reports for subservice organizations annually and maps complementary user entity controls (CUECs) to entity controls.

**Current State:** Keystone obtains SOC reports for its two subservice organizations (SecureGate Payments and AWS) annually. However, the SOC report review checklist (documented in VEN-03) was not completed for the AWS SOC 1 report review in Q1 2026. The Vendor Risk Manager reviewed the report but did not document the review using the checklist.

**Gap:** SOC report review checklist not used consistently; one review (AWS Q1 2026) was completed without the checklist.

**Likelihood:** Low (1) - The review occurred, but the documentation is incomplete.

**Impact:** Medium (2) - SOC auditor or PCI QSA may flag this as a documentation gap.

**Risk Score:** 2 (Low risk)

**Remediation:** Vendor Risk Manager to use the checklist for all future SOC report reviews. Retrospective checklist completed for the AWS Q1 2026 review. Target completion: Completed (September 2026).

**Owner:** Vendor Risk Manager

**Status:** Completed

---

### GAP-012: No Formal Cryptographic Agility Plan

**Framework:** PCI DSS v4.0.1

**Requirement:** 12.3.3 - Cryptographic cipher suites and protocols in use are documented and reviewed annually, with a plan to respond to changes in cryptographic strength (for example, quantum computing threats, deprecated algorithms).

**Current State:** Keystone maintains a cipher and protocol inventory (CRY-04), but the inventory does not include a formal cryptographic agility plan (what would Keystone do if TLS 1.2 were deprecated, or if a post-quantum algorithm were mandated?).

**Gap:** No documented cryptographic agility plan.

**Likelihood:** Low (1) - Changes in cryptographic standards are announced years in advance; Keystone has time to respond.

**Impact:** Low (1) - PCI QSA may note this as a best-practice gap, but it is not a current compliance requirement beyond documentation.

**Risk Score:** 1 (Low risk)

**Remediation:** Add a "Cryptographic Agility Plan" section to the cipher and protocol inventory: monitor NIST and PCI SSC guidance, participate in cloud provider (AWS) communications on cryptographic changes, allocate budget for cryptographic upgrades in annual planning. Target completion: December 2026.

**Owner:** Cloud Platform Engineering Manager

**Status:** Pending

---

### GAP-013: Tabletop Exercise Did Not Test All Incident Response Plan Sections

**Framework:** PCI DSS v4.0.1, SOC 2

**Requirement:** 12.10.2 (PCI DSS), CC7.4 (SOC 2) - The incident response plan is tested at least annually.

**Current State:** Keystone conducted an annual tabletop exercise in March 2026 (scenario: payment page skimming attack). However, the tabletop did not test the notification procedures for state agency customers and payment brands (section 4 of the IR plan), because the facilitator focused the exercise on containment and recovery only.

**Gap:** Tabletop exercise did not test all sections of the IR plan.

**Likelihood:** Low (1) - The exercise tested the most critical sections; the notification procedures were not tested but are documented.

**Impact:** Low (1) - PCI QSA or SOC auditor may note this as an observation, but it is unlikely to affect the opinion given that the exercise occurred and was documented.

**Risk Score:** 1 (Low risk)

**Remediation:** Expand the next annual tabletop exercise (scheduled March 2027) to include a notification simulation (mock email to state agency customers, mock call to payment brands). Target completion: March 2027.

**Owner:** Security Operations Manager

**Status:** Scheduled

---

### GAP-014: Legacy Batch System Not Included in Quarterly Access Reviews

**Framework:** PCI DSS v4.0.1, SOC 2

**Requirement:** 7.2.4 (PCI DSS), CC6.2 (SOC 2) - All user access is reviewed periodically.

**Current State:** Keystone's quarterly access review process (ACC-04) covers Okta, AWS, ServiceNow, and GitHub. The legacy batch system (colocation) is in scope for PCI DSS, but its Linux OS accounts and PostgreSQL database users were not included in the quarterly access review. The IT Operations Manager manually reviewed legacy system access annually, but this was not documented in the formal access review process.

**Gap:** Legacy batch system accounts not included in quarterly access review process.

**Likelihood:** Medium (2) - The legacy system has only 4-5 user accounts, but they are in CDE scope and should be reviewed quarterly per PCI DSS 7.2.4 (CDE access reviewed more frequently than semiannually).

**Impact:** High (3) - PCI DSS 7.2.4 non-compliance could result in a finding.

**Risk Score:** 6 (Medium risk)

**Remediation:** Add legacy batch system accounts to the quarterly access review process. The IT Operations Manager will export the Linux account list and PostgreSQL user list each quarter and submit them for review. Target completion: October 2026 (will be included in Q4 2026 access review).

**Owner:** IT Operations Manager / IAM Manager

**Status:** In progress

---

### GAP-015: No Documented Business Justification for 18-Month PAN Retention

**Framework:** PCI DSS v4.0.1

**Requirement:** 3.2.1 - Account data retention is limited by policy with a documented business or legal justification for any data retained.

**Current State:** Keystone retains encrypted PAN for 18 months (DAT-01), and the data retention schedule states "18 months for dispute resolution and agency audit requirements," but no formal business justification document was created explaining why 18 months is necessary (as opposed to 12 months or 6 months).

**Gap:** No documented business justification for 18-month PAN retention.

**Likelihood:** Low (1) - The retention period is reasonable and is documented in the policy; the gap is the lack of a detailed justification memo.

**Impact:** Low (1) - PCI QSA may ask for the justification; Keystone can explain verbally, but documenting it proactively is better.

**Risk Score:** 1 (Low risk)

**Remediation:** Create a memo documenting the business justification: state agency audit periods (12 months), dispute resolution windows (up to 180 days), and 6-month buffer for overlapping requirements. Obtain Director of GRC approval. Target completion: October 2026.

**Owner:** Privacy and Data Governance Lead

**Status:** Completed (memo approved October 2026)

---

## Summary of Remediation Status

| Gap ID | Risk Score | Status | Target Completion |
|--------|-----------|--------|-------------------|
| GAP-001 | 3 (Low) | In progress | Nov 2026 |
| GAP-002 | 4 (Medium) | Completed | Completed Oct 2026 |
| GAP-003 | 2 (Low) | Completed | Completed Oct 2026 |
| GAP-004 | 2 (Low) | Completed | Completed Oct 2026 |
| GAP-005 | 2 (Low) | In progress | Dec 2026 |
| GAP-006 | 1 (Low) | Pending | Dec 2026 |
| GAP-007 | 1 (Low) | Completed | Completed Aug 2026 |
| GAP-008 | 2 (Low) | Completed | Completed Oct 2026 |
| GAP-009 | 1 (Low) | Completed | Completed Oct 2026 |
| GAP-010 | 4 (Medium) | In progress | Nov 2026 |
| GAP-011 | 2 (Low) | Completed | Completed Sep 2026 |
| GAP-012 | 1 (Low) | Pending | Dec 2026 |
| GAP-013 | 1 (Low) | Scheduled | Mar 2027 |
| GAP-014 | 6 (Medium) | In progress | Oct 2026 |
| GAP-015 | 1 (Low) | Completed | Completed Oct 2026 |

**Completed:** 8 gaps

**In progress:** 5 gaps

**Pending/Scheduled:** 2 gaps

See `remediation-tracker.csv` for tracking details.

## Recommendations

1. **Prioritize GAP-014** (legacy batch system not in quarterly access review): This is the highest-risk open gap (score 6). Complete by the Q4 2026 access review cycle.
2. **Complete TRAs before the next PCI ROC:** All TRA-related gaps (GAP-002, GAP-003, GAP-004, GAP-008) have been remediated. Maintain the TRA library (GOV-04) going forward.
3. **Formalize role-based access documentation (GAP-005):** Low risk, but completing this will strengthen the SOC 2 Type 2 control environment for the next audit.
4. **Review the remediation tracker monthly:** Add a standing agenda item to the Risk Committee meeting to review open gaps and confirm target dates are on track.
