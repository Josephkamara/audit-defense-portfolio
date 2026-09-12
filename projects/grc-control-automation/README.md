# GRC Control Automation: Why a Shared MFA Control Passes SOC 2 and ISO 27001 but Fails PCI DSS

A GRC engineering team built one control crosswalk to satisfy three audits at once. The mapping was correct. The automated evidence was not: it checked MFA enrollment, not per-session challenge, and a trusted-device feature meant real login sessions into the cardholder data environment ran on a password alone. Two audits missed it. A PCI QSA didn't.

The company is built for this case study. The SOC 2, ISO 27001, and PCI DSS citations are real and current.

**Framework:** SOC 2 Trust Services Criteria, CC6.1 (Logical and Physical Access Controls); ISO/IEC 27001:2022, Annex A.8.5 (Secure Authentication); PCI DSS v4.0.1, Requirements 8.4.3 and 8.5.1
**Tags:** GRC Engineering, SOC 2, PCI DSS

[Read the full control automation review](https://josephkamara.github.io/audit-defense-portfolio/projects/grc-control-automation/)

[Back to the portfolio](../../)
