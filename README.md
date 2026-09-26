# Audit Defense Portfolio

**GRC, cybersecurity, and IT audit case studies by Joseph Kamara, CPA, CISSP, CISA.**

[![Live Site](https://img.shields.io/badge/live_site-josephkamara.github.io-002147?style=flat-square)](https://josephkamara.github.io/audit-defense-portfolio/)

This is a working portfolio of GRC, cybersecurity, and IT audit projects. Each one is a realistic scenario, built to show the reasoning behind a decision, not just a completed checklist. Frameworks are listed where they apply, but the point of each project is the judgment call underneath the framework.

**[View the live site →](https://josephkamara.github.io/audit-defense-portfolio/)**

## About

I have about 15 years of experience in IT audit and information security compliance, with CPA, CISA, and CISSP certifications. I led a five-person IT audit team whose SOX ITGC work a Big 4 external auditor relied on, and led a ten-person SOC and HITRUST attestation team. I have HIPAA and PCI experience.

This portfolio demonstrates how to scope, test, and document controls under PCI DSS, SOC 2, ISO 27001, NIST frameworks, and AI governance standards. Every scenario is fictional and built to demonstrate reasoning and technical depth. No real employer or client is named.

I write at [josefkamara.com](https://josefkamara.com) and publish [The Authority Brief](https://www.linkedin.com/newsletters/7419428063517728768/) on LinkedIn.

## Start Here

### [Payment Processor Compliance Program](https://josephkamara.github.io/audit-defense-portfolio/projects/payment-processor-compliance-program/)

**Program Design**

A fictional payment processor serving state agencies under PCI DSS v4.0.1 (Level 1 service provider), SOC 1 Type 2, SOC 2 Type 2, and GovRAMP Moderate. Unified control matrix mapping 79 controls across all frameworks. Seven detailed ITGC test procedures with sample workpapers and one realistic exception with root cause analysis. Gap analysis, remediation tracker, 12-month compliance calendar, and 30/60/90-day plan for a new IT auditor.

`PCI DSS` `SOC 2` `GovRAMP` `SOX ITGC`

### [PCI DSS Network Segmentation](https://josephkamara.github.io/audit-defense-portfolio/projects/pci-dss-network-segmentation (Keystone's September 2025 segmentation retest)/)

**Assessment**

A payment platform's segmentation attestation was renewed every year without testing the parts that don't show up on the architecture diagram. This report builds the testing scope a QSA will actually run: a shared log pipeline, a jump box, and a batch export job. Three boundaries hold up. The SIEM ingestion path does not.

`PCI DSS` `Cybersecurity`

### [GRC Control Automation: Why a Shared MFA Control Fails PCI DSS](https://josephkamara.github.io/audit-defense-portfolio/projects/grc-control-automation/)

**Assessment**

A GRC engineering team built one control crosswalk to satisfy SOC 2, ISO 27001, and PCI DSS at once. The mapping was correct. The automated evidence was not: it checked MFA enrollment, not per-session challenge. A trusted-device feature meant real login sessions into the cardholder data environment ran on a password alone. Two audits missed it. A PCI QSA didn't.

`PCI DSS` `SOC 2` `ISO 27001`

## IT Audit and SOX ITGC

### [Multi-Cloud SOX ITGC Control Mapping](https://josephkamara.github.io/audit-defense-portfolio/projects/multicloud-sox-itgc-control-mapping/)

**Test Plan**

A company running production across both AWS and GCP tests the same six SOX IT general controls in two environments. This maps each control to its real native evidence source in both clouds, then separates what a script can pull from what a SOX tester still has to judge.

`Cloud Security` `SOX`

### [Cloud Access Compliance Scanner](https://josephkamara.github.io/audit-defense-portfolio/projects/cloud-access-compliance-scanner (tested against a mocked Keystone sandbox account)/)

**Working Code**

A Python scanner that pulls real evidence for four controls: stale IAM keys, missing MFA, public S3 buckets, and wildcard IAM policies. Built against the real boto3 SDK and verified with a 10-test pytest suite against a mocked AWS account.

`Cloud Security` `SOC 2` `Automation`

## SOC 2 and Attestation

### [SOC 2 Evidence Automation: Quarterly Access Review as a Continuous Control](https://josephkamara.github.io/audit-defense-portfolio/projects/soc2-access-review-automation (Keystone's quarterly ServiceNow review redesigned as a continuous control)/)

**Memo**

A manual quarterly access review gets redesigned as a continuous, automated check under SOC 2 CC6. The automation replaces the reconciliation. It does not replace the analyst: the document draws a hard line between what a script can safely decide and what still needs judgment.

`SOC 2` `Automation`

### [ISO/IEC 27001:2022 Statement of Applicability](https://josephkamara.github.io/audit-defense-portfolio/projects/iso27001-statement-of-applicability/)

**Assessment**

A consultant-built SoA marks all 93 Annex A controls applicable. This document rebuilds it from the actual infrastructure up: which controls apply in full, which apply with the scope narrowed to what the company really operates, and which do not apply at all, with reasoning an auditor can test.

`ISO 27001` `Cybersecurity`

## Risk and Third Parties

### [Third-Party Risk Management Under NIST CSF 2.0](https://josephkamara.github.io/audit-defense-portfolio/projects/third-party-risk-management/)

**Program Design**

A benefits administrator treats every vendor the same: one questionnaire, filed once, never revisited. This program redesigns vendor risk management under NIST CSF 2.0's supply chain risk category, with assessment depth, contract terms, and monitoring cadence scaled to how much risk each vendor actually carries.

`NIST CSF` `Third-Party Risk`

### [Risk Acceptance Memorandum: Legacy EDI Gateway TLS Encryption Gap](https://josephkamara.github.io/audit-defense-portfolio/projects/risk-acceptance-memo/)

**Memo**

A healthcare claims gateway is stuck on TLS 1.0 while a vendor migration is pending. Walks the full decision: vulnerability, risk, likelihood/impact rating, compensating controls, residual risk, and a recommendation with a forced expiration date.

`HIPAA` `SOC 2` `Risk Acceptance`

### [FedRAMP 20x Transition: Plan of Action & Milestones](https://josephkamara.github.io/audit-defense-portfolio/projects/fedramp-20x-poam/)

**POA&M**

A cloud service provider holding an existing FedRAMP Rev5 Moderate authorization has to close five gaps before FedRAMP 20x's Consolidated Rules take mandatory effect on January 1, 2027. Every finding cites a specific RFC or Notice number, rated by likelihood and impact, and sequenced against real published deadlines.

`Cloud Security` `FedRAMP`

## AI Governance

### [Agentic AI Risk Assessment](https://josephkamara.github.io/audit-defense-portfolio/projects/agentic-ai-risk-assessment/)

**Assessment**

A distributor gives an AI agent the authority to read invoices, match them against purchase orders, and pay vendors on its own, below a set dollar threshold. The assessment tests that design against the OWASP Top 10 for Agentic Applications, walks one attack path through MITRE ATLAS, and structures the controls using NIST's AI Risk Management Framework.

`AI Governance` `Agentic AI`

### [EU AI Act High-Risk Classification](https://josephkamara.github.io/audit-defense-portfolio/projects/eu-ai-act-high-risk-classification/)

**Assessment**

A talent platform vendor classified its recruitment screening tool high-risk without argument, then waved its employee monitoring feature through as exempt. The exemption claim fails because the feature profiles workers, and profiling closes the exemption regardless of how narrow the task looks.

`EU AI Act` `AI Governance`

## Connect

Available for GRC, audit, and AI governance engagements. [Book a call](https://calendar.app.google/8xRWG2Yz3n9vKDLx5)

[LinkedIn](https://www.linkedin.com/in/joseph-kamara) · [X](https://x.com/Josefkamara) · [josefkamara.com](https://josefkamara.com)
