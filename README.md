# Audit Defense Portfolio

**GRC, cybersecurity, and IT audit case studies by Joseph Kamara, CPA, CISSP, CISA.**

[![Live Site](https://img.shields.io/badge/live_site-josephkamara.github.io-002147?style=flat-square)](https://josephkamara.github.io/audit-defense-portfolio/)
![AI Governance](https://img.shields.io/badge/-AI_Governance-C5A55A?style=flat-square)
![Cloud Security](https://img.shields.io/badge/-Cloud_Security-C5A55A?style=flat-square)
![Cybersecurity](https://img.shields.io/badge/-Cybersecurity-C5A55A?style=flat-square)
![GRC Engineering](https://img.shields.io/badge/-GRC_Engineering-C5A55A?style=flat-square)
![HIPAA](https://img.shields.io/badge/-HIPAA-C5A55A?style=flat-square)
![SOC 2](https://img.shields.io/badge/-SOC_2-C5A55A?style=flat-square)

This is a working portfolio of GRC, cybersecurity, and IT audit projects. Each one is a realistic scenario, built to show the reasoning behind a decision, not just a completed checklist. Frameworks are listed where they apply, but the point of each project is the judgment call underneath the framework.

**[View the live site →](https://josephkamara.github.io/audit-defense-portfolio/)**

## Case Studies

**[Agentic AI Risk Assessment: Where an Autonomous Invoice-Approval Agent Needs a Human in the Loop](https://josephkamara.github.io/audit-defense-portfolio/projects/agentic-ai-risk-assessment/)**

A distributor gives an AI agent the authority to read invoices, match them against purchase orders, and pay vendors on its own, below a set dollar threshold. The assessment tests that design against the OWASP Top 10 for Agentic Applications, walks one attack path through MITRE ATLAS, and structures the controls using NIST's AI Risk Management Framework.

`AI Governance` `GRC Engineering` `Agentic AI`

**[GRC Control Automation: Why a Shared MFA Control Passes SOC 2 and ISO 27001 but Fails PCI DSS](https://josephkamara.github.io/audit-defense-portfolio/projects/grc-control-automation/)**

A GRC engineering team built one control crosswalk to satisfy three audits at once. The mapping was correct. The automated evidence was not: it checked MFA enrollment, not per-session challenge, and a trusted-device feature meant real login sessions into the cardholder data environment ran on a password alone. Two audits missed it. A PCI QSA didn't.

`GRC Engineering` `SOC 2` `PCI DSS`

**[EU AI Act High-Risk Classification: Why a Workforce Monitoring Feature Can't Claim the Narrow-Task Exemption](https://josephkamara.github.io/audit-defense-portfolio/projects/eu-ai-act-high-risk-classification/)**

A talent platform vendor classified its recruitment screening tool high-risk without argument, then waved its employee monitoring feature through as exempt. The exemption claim fails because the feature profiles workers, and profiling closes the exemption regardless of how narrow the task looks. Builds the classification a regulator would actually run.

`EU AI Act` `AI Governance` `GRC Engineering`

**[PCI DSS Network Segmentation: Defending the CDE Boundary Under QSA Scrutiny](https://josephkamara.github.io/audit-defense-portfolio/projects/pci-dss-network-segmentation/)**

A payment platform has renewed the same segmentation attestation every year without testing the parts that don't show up on the architecture diagram. This report builds the testing scope a QSA will actually run and names the boundary that fails before an auditor finds it first.

`PCI DSS` `Cybersecurity` `GRC Engineering`

**[ISO/IEC 27001 Statement of Applicability: Justifying Control Exclusions for a Remote-First SaaS Company](https://josephkamara.github.io/audit-defense-portfolio/projects/iso27001-statement-of-applicability/)**

A consultant-built Statement of Applicability marks all 93 Annex A controls applicable. This document rebuilds it from the actual infrastructure up: which controls apply in full, which apply with the scope narrowed to what the company really operates, and which do not apply at all, with reasoning an auditor can test.

`ISO 27001` `GRC Engineering` `Cybersecurity`

**[Third-Party Risk Management: Building a Risk-Tiered Vendor Program Under NIST CSF 2.0](https://josephkamara.github.io/audit-defense-portfolio/projects/third-party-risk-management/)**

A benefits administrator treats every vendor the same: one questionnaire, filed once, never revisited. This program redesigns vendor risk management under NIST CSF 2.0's supply chain risk category, with assessment depth, contract terms, and monitoring cadence scaled to how much risk each vendor actually carries.

`NIST CSF` `GRC Engineering` `Third-Party Risk`

**[SOC 2 Evidence Automation: Quarterly Access Review as a Continuous Control](https://josephkamara.github.io/audit-defense-portfolio/projects/soc2-access-review-automation/)**

A manual quarterly access review gets redesigned as a continuous, automated check under SOC 2 CC6. The automation replaces the reconciliation. It does not replace the analyst: the document draws a hard line between what a script can safely decide and what still needs judgment.

`SOC 2` `GRC Engineering` `Cybersecurity`

**[Risk Acceptance Memorandum: Legacy EDI Gateway TLS Encryption Gap](https://josephkamara.github.io/audit-defense-portfolio/projects/risk-acceptance-memo/)**

A healthcare claims gateway is stuck on TLS 1.0 while a vendor migration is pending. Walks the full decision: vulnerability, risk, likelihood/impact rating, compensating controls, residual risk, and a recommendation with a forced expiration date.

`HIPAA` `SOC 2` `Risk Acceptance`

**[FedRAMP 20x Transition: Plan of Action & Milestones for the Machine-Readable Evidence Gap](https://josephkamara.github.io/audit-defense-portfolio/projects/fedramp-20x-poam/)**

A cloud service provider holding an existing FedRAMP Rev5 Moderate authorization has to close five gaps before FedRAMP 20x's Consolidated Rules take mandatory effect on January 1, 2027. Every finding cites a specific RFC or Notice number, rated by likelihood and impact, and sequenced against real published deadlines rather than internal guesses.

`Cloud Security` `GRC Engineering` `POA&M`

More case studies are in progress: real lab environments, original evidence, the same judgment-first approach.

## About

I audit technology risk and AI governance programs and build hands-on projects that show the reasoning behind the work, not just the finished checklist. CPA, CISSP, CISA. I write on these topics at [josefkamara.com](https://josefkamara.com) and publish [The Authority Brief](https://www.linkedin.com/newsletters/7419428063517728768/) on LinkedIn.

## Connect

Available for GRC, audit, and AI governance engagements. [Book a call](https://calendar.app.google/8xRWG2Yz3n9vKDLx5)

[LinkedIn](https://www.linkedin.com/in/joseph-kamara) · [X](https://x.com/Josefkamara) · [GitHub profile](https://github.com/Josephkamara)
