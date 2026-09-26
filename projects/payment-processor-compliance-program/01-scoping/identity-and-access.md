# Identity and Access (Scenario Assumptions)

This document describes Keystone Civic Payments' (fictional) identity and access management architecture, showing how workforce identity, joiner/mover/leaver processes, AWS access, privileged access management, authentication, and access reviews operate.

## Workforce Identity

**Okta is the single identity provider.** Every in-scope application federates with SAML 2.0 or OIDC. Apps that cannot do SSO are listed as exceptions with a local-account review (ACC-12).

## Joiner, Mover, Leaver

The HRIS is the source of truth.

**Joiner:**
- Birthright groups are provisioned through Okta with SCIM to downstream apps (ServiceNow, GitHub, the GRC platform, Splunk).
- Non-birthright access is requested and approved in ServiceNow (ACC-01).

**Mover:**
- An HRIS job change creates a ServiceNow task, and SCIM removes the old birthright groups (ACC-11).

**Leaver:**
- The HRIS termination deactivates Okta, and SCIM deprovisions downstream accounts (ACC-02).

## AWS Access

Humans use Okta SSO into IAM Identity Center permission sets. There are no human IAM users. Two vaulted break-glass users are the documented exception (ACC-05, GAP-001).

## Privileged Access (PAM, Just-in-Time)

Production write and legacy root/sudo access are not standing. Engineers request time-bound elevation tied to a ServiceNow ticket. Elevation expires automatically: default 4 hours, maximum 8.

Sessions run through AWS Systems Manager Session Manager or the PAM tool, with session logging (ACC-13).

## Authentication

**Phishing-resistant MFA (FIDO2 security keys or platform authenticators)** for all workforce sign-ins and required for all administrators (ACC-06). Break-glass is the GAP-001 exception.

## Unused and External Access

**IAM Access Analyzer,** organization-level unused access analyzer with a 90-day window, reports unused roles, unused access keys and passwords, and unused permissions. External access findings are also reviewed.

- Findings are reviewed monthly.
- Removals go through Terraform and CHG-01 (ACC-14).

## Access Review Evidence

Quarterly privileged and CDE reviews and semiannual general reviews run as ServiceNow review campaigns (ACC-04, TP-03). The source listings include Okta group exports, Identity Center assignments, and legacy account listings.

The Q2 2026 access review found one contractor access removal 9 business days after termination, 4 days past the 5-business-day standard. This is the realistic exception example in TP-03. A daily automated HRIS-to-Okta-to-legacy reconciliation is being added as a detective layer (see [../soc2-access-review-automation/](../../soc2-access-review-automation/)).

Legacy batch and database accounts are not yet included in quarterly reviews (GAP-014).

---

**Fictional company, sample data.** Keystone Civic Payments is built for this walkthrough. The company, scenario, and all data are invented to demonstrate modern identity and access management.
