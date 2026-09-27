# GRC Control Automation: Why a Shared MFA Control Fails PCI DSS

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how automated evidence can pass two audits and fail a third when the automated check proves the wrong thing, and how a shared control crosswalk breaks down when frameworks test different attributes of the same control.

## The Fictional Company

A fictional multi-tenant SaaS payment platform (Pellworth Commerce in the case study) that processes card payments for merchant customers. Audited under SOC 2 Type II, ISO 27001, and PCI DSS Level 1. The GRC engineering team built a control crosswalk so that one automated evidence pull would satisfy all three audits. The mapping was correct. The automated evidence was not.

## Read This in 3 Minutes

If you have three minutes:

1. **The control crosswalk:** A shared MFA control mapped to SOC 2, ISO 27001, and PCI DSS. The GRC engineering team designed one automated check to satisfy all three frameworks: query the identity provider for MFA factors enrolled for each user, pass if every user has at least one MFA factor, fail if any user has zero. The check runs daily and feeds a dashboard showing MFA compliance.
2. **What the check actually proved:** It proved enrollment. It did not prove per-session challenge. The identity provider's trusted-device feature allows a user to mark a device as trusted after one successful MFA challenge. During that window, logins from the trusted device require only a password. The automated check sees MFA enrolled and reports a pass. The user's actual login session into the cardholder data environment runs on a password alone.
3. **Why two audits passed and one failed:** SOC 2 and ISO 27001 auditors tested the control by confirming MFA factors were configured and enrollment was enforced. PCI DSS requires MFA for all access to the CDE, not just enrollment, and specifies that MFA must authenticate each time the user accesses the CDE. The QSA tested a real login session and found it completed with only a password. The automated check passed. The real control failed.

## Frameworks Covered

SOC 2 Trust Services Criteria (logical and physical access controls), ISO/IEC 27001:2022 (secure authentication), PCI DSS v4.0.1 (MFA requirements)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full control automation review with control mapping, automated evidence design, why the check passed two audits, why it failed PCI DSS, and the corrected evidence specification |
| `README.md` | This file |

## Key Finding

The shared control crosswalk was correct. The automated evidence was not. It checked enrollment instead of per-session challenge. The fix was not to unmap the control or to abandon automation. The fix was to change what the automated check measured: instead of checking Okta for enrolled MFA factors, check Okta authentication logs for the authentication methods used in real login sessions during the audit period. If any login to a CDE application completed with only a password (authentication method = password, no MFA factor present), the check fails. That evidence satisfies all three frameworks because it proves the control operates, not just that it is configured.
