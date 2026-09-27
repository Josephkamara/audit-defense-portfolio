# Building a Risk-Tiered Vendor Program

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to build a risk-tiered vendor program with assessment depth, contract terms, and monitoring cadence scaled to the risk each vendor actually carries.

## The Fictional Company

A fictional benefits administrator (Orrindale Benefits Administration in the case study) managing COBRA administration, FSA and HSA claims, and dependent eligibility verification. Current vendor program treats every vendor the same: one security questionnaire, filed once, never revisited. This program redesigns vendor risk management with supply chain risk categories.

## Read This in 3 Minutes

If you have three minutes:

1. **The problem:** Treating every vendor the same means the payroll provider (high-risk, handles sensitive data) gets the same questionnaire as a vendor with no data access. The payroll provider renews without reassessment. The claims processor (critical, handles all protected health information) has no attestation requirement in its contract. When an incident occurs, the contract has no breach notification SLA, no indemnification, and no audit rights.
2. **The tiering model:** Three tiers based on data exposure and system access. Tier 1 (critical): handles protected health information, PII, or financial data at scale, or provides a service whose failure disrupts operations. Tier 2 (moderate): limited data access, or operational but not critical. Tier 3 (low-risk): no data access, no integration, administrative services only. Tier 1 gets annual attestation review, audit rights, and quarterly business reviews. Tier 3 gets the basic questionnaire at onboarding, no reassessment unless the relationship changes.
3. **The contract changes:** Tier 1 contracts now require: attestation within 90 days of contract signature, breach notification SLA, indemnification for breaches caused by vendor negligence, audit rights, and right to terminate if the vendor loses certification or fails an audit. New vendors sign the updated terms before go-live.

## Frameworks Covered

NIST Cybersecurity Framework 2.0 supply chain risk management categories, NIST guidance documents

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full program design with risk tiering model, due diligence requirements by tier, contract terms, monitoring cadence, and sample vendor classification for eight fictional vendors |
| `README.md` | This file |

## Key Results

The program classifies eight sample vendors into three tiers: Tier 1 (claims processor, payroll provider, cloud infrastructure), Tier 2 (COBRA administrator, identity provider), Tier 3 (office supplies, training platform, expense management). Tier 1 vendors now require annual attestation review, breach notification, and audit rights. Tier 3 vendors get the basic questionnaire with no reassessment unless the relationship changes. The tiering model scales effort to risk, and the contract terms provide the legal foundation to act when a vendor fails an audit or loses certification.
