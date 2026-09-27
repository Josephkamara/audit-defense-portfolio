# SOC 2 Evidence Automation: Quarterly Access Review as a Continuous Control

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to redesign a manual quarterly access review as a continuous, automated check under SOC 2 CC6, drawing a clear line between what a script can safely decide and what still needs human judgment.

## The Fictional Company

**Keystone Civic Payments, LLC** (fictional). About 250 employees. Processes card and ACH payments for state government agencies. Level 1 PCI DSS service provider, annual SOC 2 Type 2. Quarterly access review campaign (ACC-04) covering privileged and CDE access, with ServiceNow as the review platform. Legacy batch system accounts and database service accounts require manual exports. Role changes depend on ServiceNow tasks tied to HRIS job changes (ACC-11). The Q2 2026 quarterly review surfaced GAP-014: contractor access removed 4 business days past the standard, remediated with tightened offboarding tracking.

## Read This in 3 Minutes

If you have three minutes:

1. **The current process:** Every quarter, IT pulls Okta group exports, Identity Center assignments, and legacy account listings into a ServiceNow access review campaign. Department managers review and certify their teams' access. IT validates terminations against HRIS records and removes exceptions. The review takes about 3 weeks end to end, and any access added or removed between quarters is not checked until the next campaign.
2. **The automation design:** Add a daily automated reconciliation between HRIS active status, Okta user state, Identity Center assignments, and legacy account listings. When the script finds a terminated user with active access, it creates a ServiceNow ticket for IT to investigate. The script does not remove access itself. It also checks for role changes: when HRIS shows a job change but Okta groups have not updated, it creates a task referencing the original ACC-11 request.
3. **What the automation replaces and what it does not:** The automation replaces the manual quarterly reconciliation of terminated users. It does not replace manager review of their teams' access, because a script cannot judge whether a developer needs admin access to a test environment. It does not replace the analyst investigating exceptions, because a 4-day delay in contractor offboarding (GAP-014) has a reason, and the script cannot determine whether that reason is acceptable.

## Frameworks Covered

SOC 2 Trust Services Criteria, CC6.2 (access rights reviewed and approved), CC6.3 (access rights removed when no longer required)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full design document with current quarterly review process, proposed continuous automation, and the line between automated checks and human judgment |
| `README.md` | This file |

## Key Decision

The automation finds discrepancies and creates tickets. It does not remove access itself, because automated deprovisioning without human review carries a different risk: the false positive that locks a legitimate user out mid-shift. The quarterly manager review remains because a script cannot judge role appropriateness. The automation makes the control continuous without replacing the judgment that makes the control effective.
