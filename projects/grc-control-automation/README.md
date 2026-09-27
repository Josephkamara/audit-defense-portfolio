# GRC Control Automation: Why a Shared MFA Control Fails PCI DSS

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how automated evidence can pass two audits and fail a third when the automated check proves the wrong thing, and how a shared control crosswalk breaks down when frameworks test different attributes of the same control.

## The Fictional Company

**Keystone Civic Payments, LLC** (fictional). About 250 employees. Processes card and ACH payments for state government agencies. Level 1 PCI DSS service provider, annual SOC 2 Type 2, ISO/IEC 27001:2022 certified. GRC platform (a Vanta, Drata, or OneTrust class tool) pulls automated evidence for a shared MFA control mapped to SOC 2 CC6.1, ISO 27001 Annex A.8.5, and PCI DSS 8.4.1 through 8.4.3. The evidence check passes SOC 2 and ISO 27001 audits. It fails the PCI DSS QSA review.

## Read This in 3 Minutes

If you have three minutes:

1. **The control crosswalk:** One MFA control, ACC-06 in the unified control matrix, maps to SOC 2 CC6.1, ISO 27001 Annex A.8.5, and PCI DSS 8.4.1 through 8.4.3. The GRC engineering team designed one automated check to satisfy all three frameworks: query Okta for MFA factors enrolled for each user, pass if every user has at least one MFA factor, fail if any user has zero. The check runs daily and feeds a dashboard showing MFA compliance across the organization.
2. **What the check actually proved:** It proved enrollment. It did not prove per-session challenge. Okta's trusted-device feature, enabled to reduce MFA fatigue, allows a user to mark a device as trusted for 30 days after one successful MFA challenge. During that 30-day window, logins from the trusted device require only a password. The automated check sees MFA enrolled and reports a pass. The user's actual login session into the cardholder data environment runs on a password alone.
3. **Why two audits passed and one failed:** SOC 2 CC6.1 and ISO 27001 Annex A.8.5 require MFA for privileged or remote access, and both auditors tested the control by confirming MFA factors were configured and enrollment was enforced. PCI DSS 8.4.1 requires MFA "for all access" to the CDE, not just enrollment, and 8.5.1 further specifies that MFA must authenticate "each time" the user accesses the CDE. The QSA tested a real login session and found it completed with only a password. The automated check passed. The real control failed.

## Frameworks Covered

SOC 2 Trust Services Criteria (CC6.1 logical and physical access controls), ISO/IEC 27001:2022 (Annex A.8.5 secure authentication), PCI DSS v4.0.1 (Requirements 8.4.1, 8.4.2, 8.4.3, 8.5.1)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full control automation review with control mapping, automated evidence design, why the check passed two audits, why it failed PCI DSS, and the corrected evidence specification |
| `README.md` | This file |

## Key Finding

The shared control crosswalk was correct. The automated evidence was not. It checked enrollment instead of per-session challenge. The fix was not to unmap the control or to abandon automation. The fix was to change what the automated check measured: instead of checking Okta for enrolled MFA factors, check Okta authentication logs for the authentication methods used in real login sessions during the audit period. If any login to a CDE application completed with only a password (authentication method = password, no MFA factor present), the check fails. That evidence satisfies all three frameworks because it proves the control operates, not just that it is configured.
