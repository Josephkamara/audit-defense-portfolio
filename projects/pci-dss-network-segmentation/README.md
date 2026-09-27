# PCI DSS Network Segmentation

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to test segmentation controls under PCI DSS 11.4.5, 11.4.6, and 11.4.7 when a multi-year attestation has been renewed without testing the infrastructure that does not appear on the architecture diagram.

## The Fictional Company

**Keystone Civic Payments, LLC** (fictional). About 250 employees. Processes card and ACH payments for state government agencies. Level 1 PCI DSS service provider (more than 300,000 card transactions per year). Annual ROC by a QSA. Hosted in AWS with a small colocation site for a legacy batch system. Segmentation boundaries between the cardholder data environment (CDE) and corporate networks, analytics systems, logging infrastructure, and jump hosts have been attested annually since 2022. September 2025 segmentation retest, one year before the November 2026 readiness assessment.

## Read This in 3 Minutes

If you have three minutes:

1. **The claimed boundaries:** The architecture diagram shows four segmentation boundaries: corporate network (isolated via Transit Gateway with no routes to CDE VPCs), analytics export (read-only replica, no PAN, daily batch job), shared log pipeline (CloudTrail and application logs forwarded to Splunk), and a bastion host (SSH and RDP jump for engineers, session logging via Systems Manager).
2. **The testing method:** Walk each boundary from both sides. Attempt to initiate a connection from the non-CDE side to a CDE resource (database, application server, KMS key). Attempt to initiate a connection from the CDE side to a non-CDE resource. Check network flow logs, security group rules, NACLs, Transit Gateway route tables, and IAM policies. If traffic crosses the boundary in either direction without hitting a deny rule, the boundary fails.
3. **What failed:** The SIEM ingestion path. Application logs written to CloudWatch Logs are forwarded to a Kinesis Data Firehose that lands raw logs in an S3 bucket shared with non-CDE analytics systems. The bucket is encrypted and access-controlled, but PCI DSS 3.4.1 requires PAN to be unreadable or removed before crossing a segmentation boundary. The log masking function runs after the data lands in the shared bucket, not before it crosses. That boundary failed the September 2025 retest. Remediation: move the masking function upstream so PAN is masked before logs reach the shared S3 bucket. Retested and passed in October 2025.

## Frameworks Covered

PCI DSS v4.0.1, Requirement 1.2.5 through 1.2.8 (network segmentation), Requirement 11.4.5 (annual segmentation penetration test), Requirement 11.4.6 (semiannual segmentation test for service providers), Requirement 11.4.7 (additional segmentation testing for multi-tenant providers)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full segmentation testing report with boundary descriptions, testing methodology, pass/fail results for each boundary, remediation for the failed SIEM boundary, and retest confirmation |
| `README.md` | This file |

## Key Findings

Three boundaries passed: corporate network (no routes), analytics replica (no PAN, read-only), and bastion host (Systems Manager Session Manager with session recording, no standing SSH keys). One boundary failed: the SIEM ingestion path allowed raw application logs containing PAN to reach a shared S3 bucket before masking. Remediation moved the masking function upstream. The boundary was retested in October 2025 and passed. All findings were closed before the November 2026 readiness assessment.
