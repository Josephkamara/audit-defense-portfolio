# Third-Party Risk Management Under NIST CSF 2.0

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to build a risk-tiered vendor program under NIST CSF 2.0's supply chain risk category, with assessment depth, contract terms, and monitoring cadence scaled to the risk each vendor actually carries.

## The Fictional Company

**CoreBenefits Group, LLC** (fictional). About 180 employees. Third-party benefits administrator for mid-sized employers (500 to 5,000 employees each). Health, dental, vision, FSA, HSA, COBRA, and leave administration. Annual SOC 2 Type 2 attestation. HIPAA Business Associate for all clients. Current vendor program treats every vendor the same: one security questionnaire, filed once, never revisited. No risk tiering, no contract review cadence, no monitoring between renewals. This program redesigns vendor risk management under NIST CSF 2.0.

## Read This in 3 Minutes

If you have three minutes:

1. **The problem:** Treating every vendor the same means the payroll provider (high-risk, handles SSNs and bank accounts) gets the same 30-question security questionnaire as the office supply vendor (low-risk, no data access). The payroll provider renews every year without reassessment. The claims processor (critical, handles all ePHI) has no SOC 2 requirement in its contract. When an incident occurs, the contract has no breach notification SLA, no indemnification, and no audit rights.
2. **The tiering model:** Tier 1 (critical): handles ePHI, PII, or financial data at scale, or provides a service whose failure disrupts operations. Tier 2 (moderate): limited data access, or operational but not critical. Tier 3 (low-risk): no data access, no integration, administrative services only. Tier 1 gets annual SOC 2 or ISO 27001 review, on-site or virtual audit rights, breach notification within 24 hours, and quarterly business reviews. Tier 3 gets the basic questionnaire at onboarding, no reassessment unless the relationship changes.
3. **The contract changes:** Tier 1 contracts now require: SOC 2 Type 2 or ISO 27001 within 90 days of contract signature, breach notification SLA (24 hours for critical, 72 hours for moderate), indemnification for breaches caused by vendor negligence, audit rights on 30 days' notice, and right to terminate if the vendor loses certification or fails an audit. Existing Tier 1 vendors get an addendum at renewal. New vendors sign the updated terms before go-live.

## Frameworks Covered

NIST CSF 2.0, Govern Function, GV.SC (Cybersecurity Supply Chain Risk Management), NIST SP 1305 (Quick-Start Guide for Cybersecurity Supply Chain Risk Management), NIST IR 8179 (Criticality Analysis Process Model)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full program design with risk tiering model, due diligence requirements by tier, contract terms, monitoring cadence, and sample vendor classification for eight fictional vendors |
| `README.md` | This file |

## Key Results

The program classifies eight sample vendors into three tiers: Tier 1 (claims processor, payroll provider, cloud infrastructure), Tier 2 (COBRA administrator, identity provider), Tier 3 (office supplies, training platform, expense management). Tier 1 vendors now require annual SOC 2 review, breach notification within 24 hours, and audit rights. Tier 3 vendors get the basic questionnaire with no reassessment unless the relationship changes. The tiering model scales effort to risk, and the contract terms give CoreBenefits the legal foundation to act when a vendor fails an audit or loses certification.
