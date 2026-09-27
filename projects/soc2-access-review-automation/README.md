# SOC 2 Evidence Automation: Quarterly Access Review as a Continuous Control

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to redesign a manual quarterly access review as a continuous, automated check under SOC 2 CC6, drawing a clear line between what a script can safely decide and what still needs human judgment.

## The Fictional Company

A fictional payment processor (Keystone Civic Payments in the case study) running a quarterly ServiceNow access review campaign covering identity provider, cloud access, and in-scope applications. The review relies on manual exports for legacy batch and database accounts. Role changes depend on ServiceNow tasks tied to HRIS job changes. This design redesigns the quarterly review as a continuous, automated check.

## Read This in 3 Minutes

If you have three minutes:

1. **The current process:** Every quarter, IT pulls identity provider group exports, cloud access assignments, and legacy account listings into a ServiceNow access review campaign. Department managers review and certify their teams' access. IT validates terminations against HRIS records and removes exceptions. The review takes about three weeks end to end, and any access added or removed between quarters is not checked until the next campaign.
2. **The automation design:** Add a daily automated reconciliation between HRIS active status, identity provider user state, cloud access assignments, and legacy account listings. When the script finds a terminated user with active access, it creates a ServiceNow ticket for IT to investigate. The script does not remove access itself. It also checks for role changes: when HRIS shows a job change but identity provider groups have not updated, it creates a task referencing the original access request.
3. **What the automation replaces and what it does not:** The automation replaces the manual quarterly reconciliation of terminated users. It does not replace manager review of their teams' access, because a script cannot judge whether a developer needs admin access to a test environment. It does not replace the analyst investigating exceptions, because a delay in contractor offboarding has a reason, and the script cannot determine whether that reason is acceptable.

## Frameworks Covered

SOC 2 Trust Services Criteria, CC6.2 (access rights reviewed and approved), CC6.3 (access rights removed when no longer required)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full design document with current quarterly review process, proposed continuous automation, and the line between automated checks and human judgment |
| `README.md` | This file |

## Key Decision

The automation finds discrepancies and creates tickets. It does not remove access itself, because automated deprovisioning without human review carries a different risk: the false positive that locks a legitimate user out mid-shift. The quarterly manager review remains because a script cannot judge role appropriateness. The automation makes the control continuous without replacing the judgment that makes the control effective.
