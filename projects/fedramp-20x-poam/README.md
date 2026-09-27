# FedRAMP 20x Transition: Plan of Action & Milestones

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to build a POA&M for the FedRAMP 20x transition, with findings sequenced against real published deadlines, cited by specific RFC or Notice number, and rated by likelihood and impact.

## The Fictional Company

A fictional cloud service provider holding an existing FedRAMP Moderate authorization under Rev5 baseline. Must transition to FedRAMP 20x Consolidated Rules (effective January 1, 2027) and implement machine-readable evidence capabilities. Five gaps identified related to machine-readable OSCAL artifacts, continuous monitoring submission format, POA&M tracking system auto-close logic, assessment boundary documentation, and automated evidence pipeline for certain controls.

## Read This in 3 Minutes

If you have three minutes:

1. **The regulatory timeline:** FedRAMP 20x Consolidated Rules take mandatory effect on January 1, 2027. Existing authorizations under Rev5 remain valid but must transition by that date. Machine-readable compliance (OSCAL format) requires POA&Ms, System Security Plans, and Security Assessment Reports to be submitted in OSCAL format, not document format, starting with the first continuous monitoring submission after January 1, 2027.
2. **The five gaps:** No OSCAL tooling (current documents need conversion to OSCAL). Continuous monitoring format (monthly submissions are Rev5 format, need 20x schema). POA&M auto-close logic (when a vulnerability is remediated and confirmed in a scan, the POA&M should auto-close, but the current system requires manual updates). Boundary documentation (scoping guidance changed in 20x, existing boundary document needs update). Evidence pipeline (Rev5 controls that are now continuous under 20x need automated evidence collection, not quarterly exports).
3. **Sequencing against deadlines:** The gaps are sequenced by their published deadline, not by internal priority. OSCAL tooling must complete to allow testing before the January 1, 2027 mandatory date. Continuous monitoring format conversion must complete before the December submission. POA&M auto-close is medium priority. Boundary documentation is required for the annual assessment. Evidence pipeline phases in by control over several months.

## Frameworks Covered

FedRAMP 20x Consolidated Rules, NIST SP 800-53 Rev 5, FedRAMP RFC-0024 (machine-readable compliance, finalized as CR26), OSCAL (Open Security Controls Assessment Language)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full POA&M with five findings, each with control citation, vulnerability description, likelihood and impact rating, remediation plan, owner, target date, and status |
| `README.md` | This file |

## Key Findings

Five findings, all cited by specific RFC or Notice number. Gap 1 (OSCAL tooling) is the highest priority: without it, the January 1, 2027 ConMon submission cannot be machine-readable. Gap 2 (ConMon format) is sequenced to complete before the December 2026 submission. Gap 3 (POA&M auto-close) is a process improvement, medium priority. Gap 4 (boundary documentation) aligns to the March 2027 annual assessment. Gap 5 (evidence pipeline) phases in by control over three months. All findings are sequenced against real published deadlines, not internal guesses.
