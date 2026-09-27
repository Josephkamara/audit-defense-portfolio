# Risk Acceptance Memorandum: Legacy EDI Gateway TLS Encryption Gap

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to document a risk acceptance decision for a technical vulnerability when migration is pending, including compensating controls, residual risk rating, and a forced expiration.

## The Fictional Company

A fictional claims processor (Fenwray Claims Services in the case study) handling claims data exchange through a legacy EDI gateway. The gateway supports only TLS 1.0, a protocol version that no longer meets current encryption standards. The clearinghouse vendor cannot support TLS 1.2 or higher until its platform migration completes, expected in Q1 2027.

## Read This in 3 Minutes

If you have three minutes:

1. **The vulnerability:** The legacy EDI gateway's TLS configuration is limited to TLS 1.0 and 1.1. Both versions have known cryptographic weaknesses (including BEAST and POODLE-class attacks) and are excluded from PCI DSS and most current security baselines. The clearinghouse vendor cannot support TLS 1.2 or higher until its platform migration completes.
2. **The compensating controls:** The connection runs over a dedicated point-to-point circuit, not the open internet. Network access to the circuit endpoint is restricted to a named list of systems and reviewed monthly. All traffic is logged and forwarded to the SIEM, with alerts configured for any new source or destination address. The vendor contract has been amended to add liability for breaches during the transition period.
3. **The residual risk and expiration:** Likelihood: Low (dedicated circuit, not public internet). Impact: High (PHI exposure would trigger HIPAA breach notification obligations). Overall risk: Medium. Accepted for 180 days under compensating controls, with a mandatory re-review at 90 days. If the vendor timeline slips past Q1 2027, the acceptance expires and the business must revisit immediate cutover.

## Frameworks Covered

HIPAA Security Rule (45 CFR 164.312(e)(1) transmission security), SOC 2 Trust Services Criteria (CC6.7 encryption in transit)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full risk acceptance memorandum with vulnerability description, threat assessment, compensating controls, residual risk rating, recommendation, and forced expiration date |
| `README.md` | This file |

## Key Decision

The memorandum documents a formal risk acceptance with compensating controls and a forced expiration. It is not a permanent waiver. When the migration target date arrives, the gateway must be decommissioned or the risk reassessed with updated likelihood and impact. Risk acceptances without expiration dates become technical debt that outlives the original decision maker.
