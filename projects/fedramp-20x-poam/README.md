# FedRAMP 20x Transition: Plan of Action & Milestones

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to build a POA&M for the FedRAMP 20x transition, with findings sequenced against real published deadlines, cited by specific RFC or Notice number, and rated by likelihood and impact.

## The Fictional Company

**CloudOps Federal Services, Inc.** (fictional). About 120 employees. Cloud service provider offering infrastructure management, monitoring, and DevOps automation to federal agencies. Existing FedRAMP Moderate authorization under Rev5 baseline (NIST SP 800-53 Rev 5). Must transition to FedRAMP 20x Consolidated Rules (effective January 1, 2027) and implement machine-readable evidence capabilities under RFC-0024 and CR26. Five gaps identified: machine-readable OSCAL artifacts not yet implemented, continuous monitoring submission format needs conversion from Rev5 to 20x schema, POA&M tracking system does not auto-close findings tied to resolved ConMon submissions, assessment boundary documentation needs update to 20x scoping guidance, and no automated evidence pipeline for Rev5 controls newly required as continuous in 20x.

## Read This in 3 Minutes

If you have three minutes:

1. **The regulatory timeline:** FedRAMP 20x Consolidated Rules take mandatory effect on January 1, 2027. Existing authorizations under Rev5 remain valid but must transition by that date. RFC-0024 (machine-readable compliance) was proposed in March 2024 and finalized as CR26 in July 2025. The change requires POA&Ms, System Security Plans (SSPs), and Security Assessment Reports (SARs) to be submitted in OSCAL JSON or XML format, not Word or PDF, starting with the first ConMon submission after January 1, 2027.
2. **The five gaps:** (1) No OSCAL tooling: the current SSP and POA&M are Word documents, need conversion to OSCAL. (2) ConMon format: monthly continuous monitoring submissions are Rev5 format, need 20x schema. (3) POA&M auto-close logic: when a vulnerability is remediated and confirmed in a ConMon scan, the POA&M should auto-close, but the current system requires manual updates. (4) Boundary documentation: scoping guidance changed in 20x, existing boundary document needs update. (5) Evidence pipeline: Rev5 controls that are now continuous under 20x (CM-2, CM-6, IA-5) need automated evidence collection, not quarterly exports.
3. **Sequencing against deadlines:** The gaps are sequenced by their published deadline, not by internal priority. OSCAL tooling (gap 1) must complete by October 1, 2026 to allow testing before the January 1, 2027 mandatory date. ConMon format conversion (gap 2) must complete by November 15, 2026 to meet the December ConMon submission. POA&M auto-close (gap 3) is medium priority, targeted for December 2026. Boundary documentation (gap 4) is required for the annual assessment in March 2027. Evidence pipeline (gap 5) phases in by control: CM-2 (configuration baseline) by January 2027, IA-5 (authenticator management) by February 2027, CM-6 (configuration settings) by March 2027.

## Frameworks Covered

FedRAMP 20x Consolidated Rules, NIST SP 800-53 Rev 5, FedRAMP RFC-0024 (machine-readable compliance, finalized as CR26), OSCAL (Open Security Controls Assessment Language)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full POA&M with five findings, each with control citation, vulnerability description, likelihood and impact rating, remediation plan, owner, target date, and status |
| `README.md` | This file |

## Key Findings

Five findings, all cited by specific RFC or Notice number. Gap 1 (OSCAL tooling) is the highest priority: without it, the January 1, 2027 ConMon submission cannot be machine-readable. Gap 2 (ConMon format) is sequenced to complete before the December 2026 submission. Gap 3 (POA&M auto-close) is a process improvement, medium priority. Gap 4 (boundary documentation) aligns to the March 2027 annual assessment. Gap 5 (evidence pipeline) phases in by control over three months. All findings are sequenced against real published deadlines, not internal guesses.
