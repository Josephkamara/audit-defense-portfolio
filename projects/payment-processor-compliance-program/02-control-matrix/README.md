# Unified Control Matrix

**Fictional company, sample data, for portfolio demonstration only.**

## Overview

The unified control matrix is the foundation of Keystone Civic Payments' multi-framework compliance program. It maps 76 controls across PCI DSS v4.0.1, SOC 2 (2017 Trust Services Criteria with 2022 Points of Focus), NIST SP 800-53 Revision 5 (GovRAMP Moderate baseline), and SOX IT General Controls (SOC 1 relevance).

**The principle:** Map once, evidence once. A single control, with one owner and one evidence set, supports multiple assessments. Each assessor still performs its own testing.

## File

`unified-control-matrix.csv` (76 controls, 14 columns)

Download or view the CSV directly in GitHub for the full matrix.

## Column Definitions

| Column | Description |
|--------|-------------|
| Control ID | Unique identifier (domain prefix + number) |
| Domain | Control category (Governance, Access, Change, Operations, Logging, Vulnerability, Network, Encryption, Incident Response, Vendor, Physical, HR, Data Retention, Business Continuity) |
| Control Statement | What the control does, with enough detail to test |
| Control Owner (role) | Role responsible for operating the control (not a person's name) |
| Frequency | How often the control operates (Continuous, Daily, Weekly, Monthly, Quarterly, Semiannual, Annual, Recurring event-driven, As needed) |
| Nature | Manual, Automated, or IT-dependent manual |
| Type | Preventive, Detective, or Corrective |
| Key Control (Y/N) | Whether the control is a key control (higher evidence standard, management review, direct testing) |
| PCI DSS v4.0.1 Req | Requirement numbers this control satisfies, or N/A |
| SOC 2 TSC | Trust Services Criteria and Points of Focus this control maps to, or N/A |
| NIST SP 800-53 Rev 5 | Control families this control maps to (GovRAMP Moderate baseline), or N/A |
| SOX ITGC Area | ITGC area this control supports for SOC 1 Type 2 relevance (Access to Programs and Data, Program Change, Computer Operations), or N/A |
| Evidence | What evidence demonstrates the control is designed and operating |
| Test Procedure Ref | Reference to the detailed test procedure (TP-01 through TP-07 in `03-itgc-test-procedures/`, or TP-STD for standard inspection-based testing) |

## How the Mapping Works

### Example 1: Quarterly Privileged Access Review (ACC-04)

| Framework | Requirement | What It Asks For |
|-----------|-------------|------------------|
| PCI DSS | 7.2.4 | Review all user accounts and access privileges, including vendor accounts, at least once every six months; address inappropriate access; management acknowledges the results |
| SOC 2 | CC6.2, CC6.3 | Logical access is reviewed periodically and inappropriate access is removed |
| NIST 800-53 | AC-2, AC-6(7) | Review accounts and privileges at organization-defined frequency |
| SOX ITGC | Access to Programs and Data | Periodic access reviews are performed and inappropriate access is remediated |

**One control (ACC-04) satisfies all four.** Keystone performs privileged and CDE access reviews quarterly and all other access reviews semiannually. That exceeds PCI's six-month minimum, satisfies SOC 2's "periodically," meets NIST's organization-defined frequency (Keystone defined it as quarterly for privileged), and provides SOX ITGC evidence. The same ServiceNow access review campaign export, with the same test procedure, goes to the PCI QSA, the SOC auditor, the GovRAMP assessor, and the financial statement auditor.

### Example 2: MFA for CDE Access (ACC-06)

| Framework | Requirement | What It Asks For |
|-----------|-------------|------------------|
| PCI DSS | 8.4.1, 8.4.2, 8.4.3 | 8.4.1: MFA for administrative non-console access into the CDE. 8.4.2: MFA for all non-console access into the CDE (future-dated, required from March 31, 2025). 8.4.3: MFA for all remote access from outside the network that could access or impact the CDE |
| SOC 2 | CC6.1, CC6.6 | Multi-factor authentication is required; remote access is appropriately restricted |
| NIST 800-53 | IA-2(1), IA-2(2), IA-2(8) | Multi-factor authentication for network and privileged access; phishing-resistant preferred |
| SOX ITGC | Access to Programs and Data | Strong authentication is enforced for access to systems affecting financial reporting |

**One control (ACC-06), one evidence set, four assessments.** Keystone enforces phishing-resistant MFA (FIDO2) for all workforce sign-ins through Okta, including all non-console access into the CDE and all remote access. The same design and evidence support PCI DSS 8.4.1 to 8.4.3 and 8.5.1, SOC 2 CC6.1 and CC6.6, NIST IA-2(1), IA-2(2), and IA-2(8), and the SOC 1 access control objective for the payment database. Each assessor still tests the control independently against its own criteria. Phishing-resistant MFA is Keystone's own standard. PCI DSS accepts any MFA that meets 8.5.1.

## Why This Matters

Before this matrix:

- The PCI QSA requested an MFA report showing "all non-console CDE access requires MFA"
- The SOC auditor requested "evidence that remote access requires multi-factor authentication"
- The GovRAMP assessor requested "evidence of IA-2(1) and IA-2(2) implementation"
- The SOC 1 service auditor requested "evidence supporting the access control objective for systems relevant to user entities' financial reporting"

Each request was answered separately, often with overlapping evidence re-exported in different formats, because no one had mapped the underlying control once.

After this matrix:

- One control ID: ACC-06
- One control owner: IAM Manager
- One source of evidence: Okta authentication policy configuration, Okta System Log showing per-session MFA challenge, exception register
- One test procedure: TP-STD (inspection of policy design, sample of access events to verify per-session MFA was challenged)
- One evidence set provided to four assessments, each tested independently

## Key Control Designation

19 of the 76 controls are marked as key controls (Y in the Key Control column). These are controls that:

1. Directly prevent or detect a significant risk (example: ACC-06 MFA for CDE access prevents unauthorized access to cardholder data)
2. Have a higher evidence standard (design and operating effectiveness must be tested directly, not through inquiry alone)
3. Are reviewed by management (example: GOV-06 quarterly operational review confirms log review, NSC reviews, and change management are operating)
4. Feed other controls (example: GOV-07 issue tracking ensures gaps found in testing are closed)

Key controls are always tested with a larger sample size (where frequency-based sampling applies) and are never rotated out of testing. Non-key controls may be rotated on a multi-year cycle at the auditor's discretion.

## Sample Sizes by Frequency

When a control operates multiple times per year, test sample sizes follow common audit practice (firms vary, but these are typical):

| Frequency | Population per Year | Typical Sample Size |
|-----------|---------------------|---------------------|
| Annual | 1 | 1 (test the one instance) |
| Quarterly | 4 | 2 |
| Monthly | 12 | 2 |
| Weekly | 52 | 5 |
| Daily | 365 | 20 to 40 |
| Recurring many-times-daily (example: access provisioning) | Hundreds to thousands | 25 to 60, stratified by month or system |

Sample selection is random or judgmental (higher-risk months, new systems, systems with prior exceptions). The sample is drawn from the full population period (12 months for SOC 2 Type 2, the PCI assessment period for PCI DSS).

## Evidence Quality Standards

The matrix specifies evidence sources, but evidence must also meet quality standards:

1. **System-generated preferred over screenshots.** A CSV export from ServiceNow with visible query parameters and export timestamp is stronger than a screenshot of the same data.
2. **Parameters visible.** If the evidence is a report, the query parameters, filters, and date range must be visible so the auditor can verify completeness.
3. **Population reconciles.** If the test says "all terminated users," the population must reconcile to the HR termination list with a documented tie-out.
4. **No editable spreadsheets as sole evidence.** If a control owner exports data to Excel and adds manual columns, the original system export must also be provided.
5. **Ties to the period under audit.** Evidence for a 12-month SOC 2 period must cover all 12 months, not 10 months with "the last two months were the same."
6. **Reviewer sign-off where required.** If the control statement says "reviewed by management," the evidence must show who reviewed, when, and whether they approved.

[See `04-evidence/evidence-quality-checklist.md` for the full checklist.](../04-evidence/)

## Controls That Map to SOX ITGC

12 controls in the matrix map to SOX ITGC areas, meaning they support SOC 1 Type 2 control objectives relevant to user entities' financial statement assertions:

- **Access to Programs and Data** (9 controls): ACC-01 through ACC-06, ACC-09, ACC-11, PHY-01
- **Program Change** (5 controls): CHG-01, CHG-02, CHG-05 (overlap)
- **Computer Operations** (4 controls): OPS-01, OPS-02, OPS-03, VEN-03, IR-04, BCP-01, BCP-02 (overlap)

These controls are tested with the same rigor as SOC 2 controls, but the evidence is explicitly tied to systems affecting financial reporting (the payment database, transaction processing API, settlement batch processor). State agency customers and their auditors (user auditors) rely on Keystone's SOC 1 report. They read its test results and deviations and confirm that they operate the complementary user entity controls. Keystone itself is a private LLC with no SOX audit; the "SOX ITGC Area" column uses the familiar ITGC categories to show SOC 1 relevance.

## PCI DSS v4.0.1 Future-Dated Requirements

Several controls in the matrix address PCI DSS requirements that became mandatory on March 31, 2025 (the "future-dated" requirements introduced in v4.0 and carried into v4.0.1):

- **5.4.1:** Automated anti-phishing (HR-03)
- **6.4.3:** Payment page script inventory and justification (CHG-07)
- **8.4.2:** MFA for all non-console access into the CDE, not just administrators (ACC-06)
- **10.4.1.1:** Automated log review mechanisms (LOG-03, SIEM correlation rules)
- **11.6.1:** Payment page change and tamper detection (CHG-08, if frequency is not at least once every seven days, requires a TRA per 11.6.1; Keystone runs it every few hours)
- **12.3.1:** Targeted risk analysis (TRA) for requirements allowing frequency flexibility (GOV-04)

These are marked in the gap analysis as items that were optional before March 2025 but are now mandatory. Keystone implemented most of them in 2024 as part of PCI v4.0.1 readiness.

## Notes on NIST 800-53 Mappings

NIST SP 800-53 Rev 5 has over 1,000 controls and enhancements. The matrix maps to the GovRAMP Moderate baseline, which is a subset of approximately 325 controls. Some NIST controls in the matrix are listed with enhancements in brackets (example: IA-2(1), AC-6(7)) when Keystone's control goes beyond the base requirement.

Two NIST controls listed in the matrix, CA-8 and CA-8(1) (penetration testing), are not formally part of the NIST SP 800-53B Moderate baseline but are included in GovRAMP's operational requirements. This is noted in the matrix where it appears (VUL-04, VUL-05).

## Cross-References to Other Project Materials

- **Test procedures:** See `03-itgc-test-procedures/` for detailed test steps for the seven most frequently tested control areas. TP-STD in the Test Procedure Ref column means standard inspection-based testing (examine the control design, inspect evidence for one or more instances, confirm operating effectiveness).
- **Evidence guide:** See `04-evidence/` for the PBC request list, evidence quality checklist, and how to avoid re-requesting the same evidence across audits.
- **Gap analysis:** See `05-gap-analysis/` for how gaps against this matrix are identified, rated, and tracked. The remediation tracker CSV links back to control IDs from this matrix.
- **Scoping:** See `01-scoping/` for how CDE boundaries, SOC 2 system boundaries, and GovRAMP boundaries relate to the controls in this matrix.

## How to Read the Matrix with an Auditor

When walking an auditor through the matrix:

1. **Start with one control that maps across all frameworks.** ACC-04 (quarterly privileged access review) or ACC-06 (MFA) are good examples.
2. **Show the control statement, evidence, and test procedure reference.** Point to the actual test procedure in `03-itgc-test-procedures/` if it exists.
3. **Explain the "test once, satisfy many" principle.** One control owner and one source of evidence per period, provided to every assessor that relies on the control.
4. **Walk through a key control end to end.** Pick GOV-07 (issue tracking) or CHG-01 (change management). Show how the control operates, where the evidence comes from, and how exceptions are handled.
5. **Acknowledge where you rely on subservice orgs.** Point to VEN-03 (SOC report review) and explain the CSOC/CUEC mapping in `01-scoping/system-description.md`.

The matrix is not just a mapping table. It is the documented control environment an auditor is testing.
