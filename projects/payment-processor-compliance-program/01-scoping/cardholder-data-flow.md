# Cardholder Data Flow Diagram

**Fictional company, sample data, for portfolio demonstration only.**

This diagram shows how cardholder data flows through Keystone Civic Payments' systems from initial capture to storage and settlement.

## Diagram Legend

- **Red boxes:** Cardholder Data Environment (CDE) components that store, process, or transmit PAN
- **Orange boxes:** Connected-to systems that can affect CDE security but do not handle PAN
- **Green boxes:** Out-of-scope systems with tested segmentation
- **Solid lines:** Data flows containing or potentially containing PAN
- **Dashed lines:** Data flows with tokens only, no PAN

## Flow 1: Card Not Present (CNP) Transaction via Hosted Payment Page

```mermaid
graph TB
    subgraph "Citizen / Payer"
        A["Browser: State Agency Portal"]
    end
    
    subgraph "Out of Scope: Agency Systems"
        B["Agency Web Server"]
    end
    
    subgraph "CDE: Keystone Systems"
        C["Hosted Payment Page<br/>CloudFront + S3<br/>SAQ A-EP"]
        D["Payment Gateway<br/>GatewayCo (fictional)<br/>Subservice Org"]
        E["Payment API<br/>ECS Fargate"]
        F["Tokenization Service<br/>ECS Fargate"]
        G["Payment Database<br/>RDS PostgreSQL<br/>Encrypted PAN"]
        H["Settlement Processor<br/>Lambda + Step Functions"]
    end
    
    subgraph "Out of Scope: Financial Institution"
        I["Acquiring Bank"]
    end
    
    A -->|"1. Citizen enters card"| C
    C -->|"2. JavaScript posts PAN<br/>directly to gateway<br/>TLS 1.3"| D
    D -->|"3. Authorization request"| I
    I -->|"4. Authorization response"| D
    D -->|"5. Token + auth result"| E
    E -->|"6. Store token<br/>+ transaction record"| F
    F -->|"7. Token and truncated PAN written<br/>(pre-2025 rows: encrypted PAN)"| G
    E -->|"8. Return success + token"| B
    B -->|"9. Confirmation page"| A
    
    H -->|"Nightly: settlement file<br/>tokens only, no PAN"| I
    
    style C fill:#e74c3c,stroke:#c0392b,color:#fff
    style D fill:#e74c3c,stroke:#c0392b,color:#fff
    style E fill:#e74c3c,stroke:#c0392b,color:#fff
    style F fill:#e74c3c,stroke:#c0392b,color:#fff
    style G fill:#e74c3c,stroke:#c0392b,color:#fff
    style H fill:#e74c3c,stroke:#c0392b,color:#fff
    style B fill:#2ecc71,stroke:#27ae60,color:#fff
    style I fill:#2ecc71,stroke:#27ae60,color:#fff
```

**Key scoping notes for Flow 1:**

- The hosted payment page is CDE because it captures PAN, even though it immediately posts to the gateway. Keystone is responsible for PCI DSS 6.4.3 (script inventory and justification) and 11.6.1 (change and tamper detection). [See CHG-07 and CHG-08 in the control matrix.](../02-control-matrix/)
- The agency's web server never receives PAN, so it remains out of Keystone's CDE scope. The agency operates under SAQ A-EP or its own validation as a merchant.
- The gateway (GatewayCo) is a subservice organization. Keystone relies on GatewayCo's PCI DSS validation and reviews its AOC annually.
- Encrypted PAN from before Q1 2025 remains in the database for legacy reporting until the DAT-01 purge. New transactions store gateway tokens and truncated PAN only.

## Flow 2: Settlement and Reconciliation

```mermaid
graph LR
    subgraph "CDE: Keystone Systems"
        A["Payment Database<br/>Tokens + Transaction Log"]
        B["Settlement Processor<br/>Lambda + Step Functions<br/>Nightly 2 AM UTC"]
        C["SFTP Service<br/>Outbound Only"]
    end
    
    subgraph "Out of Scope: Financial Institution"
        D["Acquiring Bank SFTP<br/>TLS 1.2, key auth"]
    end
    
    subgraph "Out of Scope: State Agency"
        E["Agency Reconciliation<br/>Portal"]
    end
    
    A -->|"1. Query transaction totals<br/>by merchant + day"| B
    B -->|"2. Generate settlement file<br/>tokens, amounts, no PAN"| C
    C -->|"3. Encrypted transfer"| D
    B -->|"4. Post summary<br/>tokens only"| E
    
    style A fill:#e74c3c,stroke:#c0392b,color:#fff
    style B fill:#e74c3c,stroke:#c0392b,color:#fff
    style C fill:#e74c3c,stroke:#c0392b,color:#fff
    style D fill:#2ecc71,stroke:#27ae60,color:#fff
    style E fill:#2ecc71,stroke:#27ae60,color:#fff
```

**Key scoping notes for Flow 2:**

- Settlement files contain tokens and transaction amounts, not PAN. The acquiring bank receives its settlement data from the gateway separately.
- Agency reconciliation portal is out of scope because it receives tokens only, not PAN. Agencies can view transaction summaries but not decrypt stored PAN.

## Flow 3: Legacy ACH Batch System (Colocation)

```mermaid
graph TB
    subgraph "Out of Scope: State Agency"
        A["Agency Treasury System"]
    end
    
    subgraph "CDE: Colocation Legacy System"
        B["Legacy Batch Server<br/>Physical Server<br/>Cage Access: Badge + Bio"]
        C["Legacy Database<br/>PostgreSQL<br/>Column Encryption"]
        D["Hardware Firewall<br/>Default Deny"]
    end
    
    subgraph "Out of Scope: Financial Institution"
        E["ACH Network<br/>NACHA File Format"]
    end
    
    A -->|"1. ACH payment request<br/>bank account + amount"| D
    D -->|"2. Firewall allows<br/>specific IP only"| B
    B -->|"3. Store encrypted<br/>account number"| C
    B -->|"4. Generate NACHA file<br/>nightly batch"| E
    
    style B fill:#e74c3c,stroke:#c0392b,color:#fff
    style C fill:#e74c3c,stroke:#c0392b,color:#fff
    style D fill:#e74c3c,stroke:#c0392b,color:#fff
    style A fill:#2ecc71,stroke:#27ae60,color:#fff
    style E fill:#2ecc71,stroke:#27ae60,color:#fff
```

**Key scoping notes for Flow 3:**

- This system is in the CDE because it still processes legacy card batch settlements for two state agencies (see system-description.md), in addition to ACH files. ACH bank account numbers are not PCI account data, but they are confidential agency data protected under DAT-03 and SOC 2 Confidentiality. Shared management alone would not put a system in PCI scope; storing, processing, or transmitting account data, or connectivity to the CDE, would.
- Physical security is tested as part of PCI DSS Requirement 9. The colocation facility provides badge and biometric access, video surveillance, and visitor logs. [See PHY-01 in the control matrix.](../02-control-matrix/)
- This system is out of GovRAMP scope because the two state agencies using it are not GovRAMP participants.

## Data Retention and Destruction

- **PAN retention:** Encrypted PAN is retained for 18 months per business justification (dispute resolution and agency audit requirements), then securely deleted per DAT-01. A quarterly automated purge job removes PAN past its retention period.
- **Token retention:** Tokens are retained for 7 years per state record-keeping requirements. Tokens cannot be used to reconstruct PAN without access to the gateway's detokenization API, which requires separate authentication and logging.
- **Log retention:** Audit logs are retained for 12 months with 3 months immediately searchable in the SIEM, per PCI DSS 10.5.1 and GovRAMP ConMon requirements.

## Segmentation Controls Summary

The CDE is segmented from corporate and out-of-scope systems using:

1. **AWS account boundaries:** Production payment systems run in a dedicated AWS account with no cross-account access from corporate or sandbox accounts. SCPs prevent privilege escalation.
2. **VPC and security groups:** Default-deny security groups restrict traffic to necessary ports and protocols only. VPC Flow Logs monitor all network traffic.
3. **Transit Gateway route tables:** On-premises connectivity (colocation to AWS) flows through Transit Gateway with explicit route tables. No default route to the internet from CDE databases.
4. **Colocation hardware firewall:** Legacy system protected by a stateful firewall with explicit allow rules for the two state agencies only. All other traffic denied by default.

**Segmentation testing cadence:** At least every six months per PCI DSS 11.4.6 (service provider requirement), covering all segmentation methods in use. The September 2025 segmentation retest in the PCI DSS Network Segmentation project shaped the current design (CDE-dedicated Splunk index, Session Manager in place of the bastion, semiannual cadence). [See VUL-05 in the control matrix and the existing PCI DSS Network Segmentation project for detailed testing approach.](../02-control-matrix/)

## Change Impact on Data Flows

Any change to these flows triggers a scope impact review (PCI DSS 6.5.2 and 12.5.2.1):

- New payment channel (example: mobile app, recurring billing API)
- New subservice organization or gateway
- Migration of legacy batch system to AWS (planned for Q3 2027)
- New data export or integration with state agency back-office systems

Each change is documented in ServiceNow with a "significant change" flag, reviewed by the Director of GRC, and confirmed before production deployment. [See GOV-05 and CHG-06 in the control matrix.](../02-control-matrix/)
