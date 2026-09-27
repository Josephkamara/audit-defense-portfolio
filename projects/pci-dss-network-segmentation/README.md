# PCI DSS Network Segmentation

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to test segmentation controls under PCI DSS 11.4.5, 11.4.6, and 11.4.7 when a multi-year attestation has been renewed without testing the infrastructure that does not appear on the architecture diagram.

## The Fictional Company

A fictional payment processor (Keystone Civic Payments in the case study) processing card and ACH payments for state government agencies. Hosted in cloud infrastructure with a small colocation site for a legacy batch system. Segmentation boundaries between the cardholder data environment and corporate networks, analytics systems, logging infrastructure, and jump hosts have been attested annually. This is the segmentation retest one year before the readiness assessment.

## Read This in 3 Minutes

If you have three minutes:

1. **The claimed boundaries:** The architecture diagram shows four segmentation boundaries: corporate network (isolated via routing with no routes to CDE), analytics export (read-only replica, no card data, daily batch job), shared log pipeline (logs forwarded to SIEM), and a bastion host (SSH jump for engineers, session logging via session manager).
2. **The testing method:** Walk each boundary from both sides. Attempt to initiate a connection from the non-CDE side to a CDE resource (database, application server, encryption key). Attempt to initiate a connection from the CDE side to a non-CDE resource. Check network flow logs, security group rules, network access control lists, routing tables, and access policies. If traffic crosses the boundary in either direction without hitting a deny rule, the boundary fails.
3. **What failed:** The SIEM ingestion path. Application logs written to the log service are forwarded to a data stream that lands raw logs in a storage bucket shared with non-CDE analytics systems. The bucket is encrypted and access-controlled, but PCI DSS requires card data to be unreadable or removed before crossing a segmentation boundary. The log masking function runs after the data lands in the shared bucket, not before it crosses. That boundary failed the retest. Remediation: move the masking function upstream so card data is masked before logs reach the shared bucket. Retested and passed.

## Frameworks Covered

PCI DSS v4.0.1 (network segmentation and CDE scoping, segmentation penetration testing for service providers and multi-tenant providers)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full segmentation testing report with boundary descriptions, testing methodology, pass/fail results for each boundary, remediation for the failed SIEM boundary, and retest confirmation |
| `README.md` | This file |

## Key Findings

Three boundaries passed: corporate network (no routes), analytics replica (no card data, read-only), and bastion host (session manager with session recording, no standing SSH keys). One boundary failed: the SIEM ingestion path allowed raw application logs containing card data to reach a shared storage bucket before masking. Remediation moved the masking function upstream. The boundary was retested and passed. All findings were closed before the readiness assessment.
