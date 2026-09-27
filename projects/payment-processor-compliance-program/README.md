# Payment Processor Compliance Program

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to scope, map, test, and manage a multi-framework compliance program for a payment processor serving state government agencies under PCI DSS v4.0.1 (service provider), SOC 1 Type 2, SOC 2 Type 2, and GovRAMP Moderate.

## The Fictional Company

**Keystone Civic Payments, LLC** (fictional). About 250 employees. Processes card and ACH payments for state agency web portals (license renewals, permits, fees, fines). Level 1 PCI DSS service provider. Annual SOC 1 Type 2 and SOC 2 Type 2 (Security, Availability, Confidentiality). GovRAMP Moderate authorization for state customers.

Hosted mostly in AWS (VPC, EC2, RDS, S3, KMS, CloudTrail, GuardDuty), code in GitHub with CI/CD, identity in Okta, ticketing in ServiceNow, logs in a SIEM, one small colocation site for a legacy batch system. Uses a payment gateway / tokenization subservice organization and a cloud host (carve-out method in SOC reports).

## Read This in 3 Minutes

If you have three minutes:

1. **Start with scoping:** `01-scoping/system-description.md` shows how the CDE boundary is defined, what is connected, and what stays out. The data-flow diagram is in the same folder.
2. **See the unified control matrix:** `02-control-matrix/unified-control-matrix.csv` maps 79 controls across PCI DSS v4.0.1, SOC 2, NIST SP 800-53 Rev 5 (GovRAMP Moderate baseline), and SOX ITGC areas. One control and one evidence set support multiple assessments; each assessor still tests independently.
3. **Pick one test procedure:** `03-itgc-test-procedures/03-periodic-and-privileged-access-review.md` walks through testing a quarterly access review with a sample workpaper and one realistic exception with root cause and how it would be reported.
4. **Check the gap analysis:** `05-gap-analysis/readiness-assessment.md` shows how gaps are identified, rated, and tracked, with examples from SOC 2 readiness and PCI DSS v4.0.1 future-dated requirements that became mandatory March 31, 2025.

## Folder Map

- **01-scoping:** System description, cardholder data flow diagram, CDE and connected-to systems, segmentation, SOC 2 boundary with carve-out subservice orgs and CUECs/CSOCs, GovRAMP boundary.
- **02-control-matrix:** Unified control matrix CSV and explanation of the "map once, evidence once" approach.
- **03-itgc-test-procedures:** One file per ITGC area with control objective, population, sample size, test steps, attributes, and sample workpapers with one realistic exception.
- **04-evidence:** PBC request list, evidence quality checklist, guide on avoiding duplicate requests across audits.
- **05-gap-analysis:** Readiness assessment with risk rating method, at least 12 gaps, and remediation tracker CSV.
- **06-third-party-and-pentest:** Vendor risk tiering, SOC report review checklist, pen test oversight checklist, ASV scan tracking.
- **07-continuous-compliance:** 12-month compliance calendar and KPI set.
- **08-first-90-days:** A 30/60/90 plan for an IT auditor joining this company.

## Program Operations (Add-on)

Day-to-day program operations: [program-operations.html](program-operations.html) ([live](https://josephkamara.github.io/audit-defense-portfolio/projects/payment-processor-compliance-program/program-operations.html)). DR and backup testing audited under BCP-01, BCP-02, OPS-01 and OPS-02 with one exception (reporting schema RPO, remediated and retested), unified audit calendar (October 2026 to September 2027) showing how PCI, SOC and GovRAMP share evidence, GovRAMP roadmap from Security Snapshot to Authorized status, contract obligations tracker for five sample agency customers (fictional names), one-page leadership dashboard showing control health and audit readiness by framework, and a 30/60/90 plan for integrating an acquired company.

## Framework Versions Used

- **PCI DSS:** v4.0.1 (requirements that became mandatory March 31, 2025 are marked in the gap analysis)
- **SOC 2:** 2017 Trust Services Criteria with 2022 Points of Focus
- **NIST SP 800-53:** Revision 5 (GovRAMP Moderate baseline)
- **SOX ITGC:** Standard areas (access, change, operations)

## Disclaimer

Everything in this project is about a fictional company. The company, systems, findings, and data are built to demonstrate judgment and technical depth in a compliance program design. No real employer, client, or assessment is named or depicted.
