# ISO/IEC 27001:2022 Statement of Applicability

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to build a Statement of Applicability from the actual infrastructure up, justifying which Annex A controls apply, which apply with narrowed scope, and which do not apply, with reasoning an auditor can test.

## The Fictional Company

**Streamline Workflow, Inc.** (fictional). About 75 employees. Remote-first SaaS company providing project management and collaboration software to small businesses (10 to 100 users per customer). Annual revenue about $8 million. Infrastructure entirely in AWS (ECS, RDS, S3, CloudFront, VPC). No physical office, no on-premises equipment. Customer data is project metadata, tasks, files, and user profiles (names, email addresses). ISO/IEC 27001:2022 certification pursuit underway, with an external consultant having delivered a draft Statement of Applicability marking all 93 Annex A controls applicable. This document rebuilds that SoA from the infrastructure up.

## Read This in 3 Minutes

If you have three minutes:

1. **The problem:** A consultant delivered a Statement of Applicability marking all 93 Annex A controls as applicable without checking what the company actually operates. The company has no physical office, no on-premises servers, no paper records, no datacenter to secure, and no utility services to protect. Twenty controls do not apply, and marking them applicable creates audit scope the company cannot satisfy.
2. **The method:** Rebuild the SoA from what the company really runs. Group controls by theme (Organizational, People, Physical, Technological). For each control, check whether the company operates the asset or process that control protects. If it does not, justify the exclusion with a statement an auditor can verify. If it does, mark it applicable and state how it is implemented.
3. **The exclusions:** Physical security controls (7.4 physical monitoring, 7.5 asset security in areas, 7.7 clear desk, 7.8 unattended equipment, 7.10 storage media, 7.11 utilities, 7.13 equipment maintenance) do not apply because the company has no physical office or datacenter. Paper-based controls (8.30 physical media transfer) do not apply because the company uses no removable media or paper records. Supplier-facility controls (5.21 physical supplier security) do not apply because AWS is responsible for its own datacenter security under the shared responsibility model.

## Frameworks Covered

ISO/IEC 27001:2022, Clause 6.1.3 (Information Security Risk Treatment), Annex A (93 controls across Organizational, People, Physical, and Technological themes)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full Statement of Applicability with applicability determination, implementation summary, and exclusion justification for all 93 Annex A controls |
| `README.md` | This file |

## Key Decision

The Statement of Applicability must reflect what the company actually operates. A control that protects a physical datacenter does not apply when the company has no datacenter. A control that protects removable media does not apply when the company uses no removable media. Marking non-applicable controls as applicable creates audit findings the company cannot fix, because it cannot implement a control for an asset it does not have. The exclusions are justified with verifiable statements: no physical office (lease records confirm it), no on-premises servers (AWS is the only infrastructure), no paper records (document retention policy confirms electronic-only).
