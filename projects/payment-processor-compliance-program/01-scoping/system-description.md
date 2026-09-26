# System Description and Scoping

**Fictional company, sample data, for portfolio demonstration only.**

## Company Overview

Keystone Civic Payments, LLC processes card and ACH payments for approximately 50 state government agency web portals across 12 states. These portals handle license renewals, permit applications, court fines, and various government fees. Keystone processes about 6 million card transactions a year, well above the 300,000-transaction threshold for a Level 1 PCI DSS service provider, and validates annually with a ROC by a QSA.

## Framework Scope Summary

| Framework | Authorization / Report Type | Scope |
|-----------|---------------------------|-------|
| PCI DSS v4.0.1 | Level 1 Service Provider, Annual ROC and AOC | Cardholder data environment (CDE) as defined below |
| SOC 1 Type 2 | SSAE 18 | Payment processing controls relevant to user entities' financial statement assertions |
| SOC 2 Type 2 | Security, Availability, Confidentiality | Payment platform and customer portal |
| GovRAMP Moderate | NIST SP 800-53 Rev 5 based authorization, modeled on FedRAMP, for state and local government | Cloud-hosted components serving state customers |

## In-Scope System Components (Cardholder Data Environment)

The CDE includes system components that store, process, or transmit cardholder data, and components with unrestricted connectivity to them. Systems that can affect CDE security are in PCI scope as connected-to or security-impacting systems (next section):

### AWS VPC: Payment Processing Environment

**Account:** keystone-prod-payments (isolated AWS account)

- **Payment API tier** (ECS Fargate): RESTful API accepting card transactions from agency portals, validates and routes to payment gateway
- **Tokenization service** (ECS Fargate): Receives PAN from gateway response, stores encrypted PAN with column-level encryption in RDS, returns token to merchant
- **Hosted payment page** (CloudFront + S3): JavaScript-based secure payment form embedded in agency portals (PCI SAQ A-EP compliance path for merchants)
- **Database tier** (RDS PostgreSQL Multi-AZ): Stores encrypted PAN (legacy transactions only, pre-tokenization migration), tokens, transaction records
- **Settlement processor** (Lambda + Step Functions): Nightly batch reconciliation with acquiring banks

### Supporting CDE Infrastructure

- **Key Management:** AWS KMS with customer-managed keys for database encryption, Secrets Manager for application credentials
- **Logging and Monitoring:** CloudTrail (all regions, log file validation), VPC Flow Logs, application logs forwarded to SIEM (Splunk Cloud, CDE-dedicated index with role-based access)
- **Security Controls:** WAF (AWS WAF with OWASP rules, blocking mode), GuardDuty (all accounts), Security Hub, Systems Manager for patch management
- **Network Security:** Transit Gateway with segmentation route tables, security groups (default deny), NACLs

### Colocation Site: Legacy Batch System

**Facility:** ColoCo (fictional), facility location withheld

- **Legacy batch server** (physical server): Processes ACH files and legacy card batch settlements for two state agencies not yet migrated to the API platform
- **Database:** Local PostgreSQL instance with column-level encryption
- **Firewall:** Dedicated hardware firewall with default-deny rules, managed segmentation

## Connected-to Systems (Not in CDE, But Must Be Scoped)

These systems connect to the CDE but do not store, process, or transmit cardholder data:

- **Admin bastion hosts** (AWS Systems Manager Session Manager): Engineers access CDE systems through SSO with per-session MFA, sessions logged
- **CI/CD pipeline** (GitHub Actions with OIDC): Deploys code to CDE environments, read-only access to production, deployment logs retained
- **Monitoring and alerting** (PagerDuty, integrated with SIEM): Alert routing, on-call schedule
- **Backup service** (AWS Backup): Daily RDS and EBS snapshots, encrypted at rest, cross-region replication, vault lock enabled

## Out-of-Scope Systems (Confirmed Segmentation)

These systems are segmented from the CDE with documented and tested network security controls:

- **Corporate network:** HR systems (Workday), email (Google Workspace), internal collaboration (Slack), marketing website
- **Engineering sandbox:** Development and QA environments in separate AWS accounts with no live cardholder data, SCPs prevent cross-account access
- **Customer support portal:** ServiceNow instance used by agency customers to submit support tickets, no payment functionality, separate authentication
- **Analytics environment:** Redshift cluster receiving tokenized transaction summaries via one-way scheduled export, no raw PAN, no live CDE connectivity

**Segmentation testing:** Per PCI DSS 11.4.6, segmentation controls are penetration tested at least every six months and after any segmentation change. [See the existing PCI DSS Network Segmentation project for testing methodology.](../../pci-dss-network-segmentation/)

## Cardholder Data Flows

See `cardholder-data-flow.md` for the Mermaid diagram showing:

1. Card present transaction flow: Agency terminal → payment gateway → Keystone API → tokenization → storage
2. Card not present flow: Citizen browser → hosted payment page → gateway → Keystone API
3. Settlement flow: Keystone settlement processor → acquiring bank SFTP
4. ACH flow: Legacy batch system → NACHA file to state treasury

## Subservice Organizations (Carve-Out Method)

Keystone uses the carve-out method for two subservice organizations in its SOC 1 and SOC 2 reports:

### 1. Payment Gateway / Tokenization Provider: GatewayCo (fictional)

**Services provided:** Card authorization, gateway tokenization (primary tokens used for card-on-file), PCI DSS compliance for gateway infrastructure

**SOC reports obtained:** SOC 1 Type 2 and SOC 2 Type 2, periods ending within three months of Keystone's report date, bridge letters obtained when needed

**Complementary Subservice Organization Controls (CSOCs) Keystone relies on:**
- GatewayCo maintains PCI DSS Level 1 service provider validation (annual ROC and AOC)
- GatewayCo encrypts data in transit (TLS 1.2+) and at rest
- GatewayCo performs vulnerability scanning and penetration testing of gateway infrastructure
- GatewayCo provides transaction logs to Keystone for reconciliation

**Keystone's responsibility:** Validate TLS configuration on our API endpoints calling GatewayCo, review GatewayCo's AOC and SOC reports annually, map CSOCs to Keystone controls. [See VEN-03 in the control matrix.](../02-control-matrix/)

### 2. Cloud Infrastructure Provider: Amazon Web Services (AWS)

**Services provided:** Infrastructure as a service (compute, storage, networking, key management, logging)

**SOC reports obtained:** AWS SOC 1, SOC 2, and SOC 3 available in AWS Artifact, reviewed annually

**Complementary Subservice Organization Controls (CSOCs) Keystone relies on:**
- AWS provides physical security for data centers
- AWS maintains environmental controls (power, cooling, fire suppression)
- AWS provides hypervisor-level isolation between customer instances
- AWS encrypts EBS volumes and S3 objects when requested by the customer

**Complementary User Entity Controls (CUECs) Keystone must operate:**
- Keystone configures AWS services securely (security groups, IAM policies, encryption settings)
- Keystone enables and monitors CloudTrail, GuardDuty, and Config
- Keystone manages logical access to the AWS console and API through IAM Identity Center with MFA
- Keystone tests backup restores quarterly
- Keystone applies OS and application patches per policy

CUECs are explicitly mapped back to Keystone controls in the unified control matrix. AWS's responsibility for physical security means Keystone does not need to test data center badge readers, but Keystone is fully responsible for every configuration choice within AWS.

## SOC 2 System Boundary

The SOC 2 system description in Keystone's Type 2 report describes:

- **System:** Payment processing platform and customer portal for state agencies
- **Trust Services Categories:** Security (common criteria CC1 to CC9), Availability (A1.1 to A1.3), Confidentiality (cardholder data and citizen PII)
- **Period:** 12 months (April 1 to March 31); the report is issued after the period ends
- **Boundaries:** Same as the PCI CDE plus the customer-facing agency portal (authentication, user management, transaction reporting), which does not handle raw card data but is in scope for SOC 2 Availability
- **Carve-out subservice orgs:** GatewayCo (fictional) (gateway) and AWS (infrastructure) as described above

## GovRAMP Moderate Boundary

GovRAMP (Government Risk and Authorization Management Program) (formerly StateRAMP) is a nonprofit program, modeled on FedRAMP and based on NIST SP 800-53 Rev 5, that verifies the security of cloud providers serving state and local government. Keystone's GovRAMP authorization covers:

- **Cloud service offering:** Payment processing API and hosted payment page for state agencies
- **Impact level:** Moderate (handles citizen PII and payment information, no classified or high-impact data)
- **Baseline:** NIST SP 800-53 Revision 5 Moderate baseline controls
- **FedRAMP equivalency:** Accepted by 8 of the 12 states Keystone serves in lieu of a separate state security review

The GovRAMP boundary is narrower than the full PCI CDE:

- **In GovRAMP scope:** AWS-hosted payment API, hosted payment page, databases, supporting AWS services
- **Out of GovRAMP scope:** Legacy colocation batch system (state agencies using it are not GovRAMP participants), internal corporate systems

**GovRAMP continuous monitoring deliverables** (monthly): POA&M with open findings and due dates, updated system inventory, OS vulnerability scans, database vulnerability scans, web application vulnerability scans, compliance scans (CIS benchmarks), risk adjustments, operational requirements, false positive justifications, executive summary. [See GOV-08 in the control matrix for the control.](../02-control-matrix/)

## How the Three Boundaries Relate

```
Largest scope: PCI DSS scope (CDE plus connected-to systems)
  ├─ Includes: AWS payment platform + colocation legacy system + all connected-to systems
  │
  └─ SOC 2 system boundary (overlaps PCI scope; adds the portal, excludes the colocation system)
      ├─ Includes: AWS payment platform + agency customer portal
      ├─ Overlaps: Payment API, databases, some supporting infrastructure
      ├─ Adds: Customer portal (not in PCI CDE, no card data)
      │
      └─ GovRAMP Moderate boundary (smallest)
          ├─ Includes: AWS payment platform only
          └─ Excludes: Colocation legacy system, customer portal back-office features
```

One control often supports all three frameworks. Example: ACC-04 (quarterly privileged access review) maps to PCI DSS 7.2.4, SOC 2 CC6.2 and CC6.3, and NIST AC-2 and AC-6(7). That review covers privileged access to the payment database. The same evidence goes to the PCI QSA, the SOC auditor, and the GovRAMP 3PAO, and each one tests it.

## Scoping Changes and Review Cadence

- **PCI scope confirmation:** At least every six months per 12.5.2.1 (service provider requirement), signed by Director of GRC, includes updated data flows and inventory. [See GOV-05 in the control matrix.](../02-control-matrix/)
- **Significant change review:** Any new system, network change, or organizational change that could affect scope triggers a documented scope impact review before implementation (PCI DSS 6.5.2 and 12.5.2.1); changes to organizational structure also trigger the executive review required by 12.5.3
- **SOC report period:** 12 months, updated annually, system description changes disclosed in the report
- **GovRAMP inventory:** Updated monthly as part of continuous monitoring package

## References

- PCI DSS Requirements and Testing Procedures v4.0.1 (June 2024; future-dated requirements introduced in v4.0, March 2022, mandatory since March 31, 2025)
- AICPA Trust Services Criteria (2017 criteria with 2022 points of focus)
- NIST SP 800-53 Revision 5 (September 2020)
- NIST SP 800-53B, Control Baselines for Information Systems and Organizations (October 2020)
