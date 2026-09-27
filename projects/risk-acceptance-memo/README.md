# Risk Acceptance Memorandum: Legacy EDI Gateway TLS Encryption Gap

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to document a risk acceptance decision for a technical vulnerability when migration is pending, including compensating controls, residual risk rating, and a forced expiration.

## The Fictional Company

**ClearPath Benefits Administration** (fictional). About 450 employees. Administers health and benefits plans for mid-sized employers (3,000 to 15,000 employees each). Claims processing, enrollment, and premium billing. Annual SOC 2 Type 2 attestation. HIPAA Business Associate for all clients. Legacy EDI gateway (ClaimStream, vendor end-of-life announced) processes about 40,000 claims per month, supports only TLS 1.0, vendor migration in progress with a target completion date.

## Read This in 3 Minutes

If you have three minutes:

1. **The vulnerability:** The legacy EDI gateway (ClaimStream) supports only TLS 1.0. Modern browsers dropped TLS 1.0 in 2020. Known vulnerabilities (BEAST, downgrade attacks) exist. HIPAA Security Rule 164.312(e)(1) requires transmission security. SOC 2 CC6.7 requires encrypted data in transit. The vendor announced end-of-life, and no patch will bring TLS 1.2 or 1.3.
2. **The compensating controls:** The gateway sits in a private VLAN with no internet routing, accessed only through a dedicated VPN tunnel from three trusted payer systems (Aetna, BCBS regional affiliate, UnitedHealthcare). No public internet exposure. Network-level access controls (firewall rules, VPN authentication) limit connections. The gateway logs all sessions, and the SIEM alerts on unexpected source IPs.
3. **The residual risk and expiration:** Likelihood rated Low (no public exposure, private network, three known endpoints), Impact rated Moderate (ePHI exposure if an attacker gains VPN access). Overall risk: Medium. Accepted until March 31, 2027 (vendor migration target completion). After that date, the gateway must be decommissioned or the risk re-evaluated. The memo includes a recommendation that leadership approve with the forced expiration.

## Frameworks Covered

HIPAA Security Rule (45 CFR 164.312(e)(1) transmission security), SOC 2 Trust Services Criteria (CC6.7 encryption in transit)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full risk acceptance memorandum with vulnerability description, threat assessment, compensating controls, residual risk rating, recommendation, and forced expiration date |
| `README.md` | This file |

## Key Decision

The memorandum documents a formal risk acceptance with compensating controls and a forced expiration. It is not a permanent waiver. When the migration target date arrives, the gateway must be decommissioned or the risk reassessed with updated likelihood and impact. Risk acceptances without expiration dates become technical debt that outlives the original decision maker.
