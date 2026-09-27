# EU AI Act High-Risk Classification

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to build a high-risk classification under the EU AI Act when the narrow-task exemption claim fails, with reasoning a regulator would actually apply.

## The Fictional Company

A fictional HR technology vendor (Veskaro Technologies in the case study), SaaS talent platform serving corporate HR departments. Two AI features: candidate screening (resume parsing, keyword matching, ranked shortlist) and employee monitoring (workforce behavioral risk scoring for attrition and performance). The company classified the screening tool as high-risk under EU AI Act Annex III without argument. It classified the monitoring feature as exempt under the narrow task exemption because the feature only scores existing employees, not candidates. That exemption claim fails.

## Read This in 3 Minutes

If you have three minutes:

1. **What the monitoring feature does:** The feature monitors employee activity (email volume, calendar density, messaging response time, commit frequency for engineers, ticket close rate for support). It builds a behavioral risk score for attrition risk and performance risk. The score is attached to the employee's profile and visible to managers and HR. Managers use the score to prioritize one-on-one check-ins, adjust workload, or flag employees for a performance improvement plan. The score does not trigger automated actions, but it influences manager decisions.
2. **Why the exemption claim fails:** Article 6(3) allows a narrow-task exemption when the AI system performs a narrow procedural task (detect duplicates, classify documents, route a request), does not replace human assessment, and does not profile individuals. Profiling is explicitly excluded from the exemption. The monitoring feature builds a profile: it takes multiple behavioral signals, aggregates them into a risk score, and attaches that score to a named individual. That is profiling. The fact that a human makes the final decision does not save the exemption, because the exemption closes as soon as profiling occurs, not when an automated decision occurs.
3. **What high-risk classification requires:** The vendor must implement Article 9 through Article 15 obligations: risk management system (identify and mitigate risks of discrimination and privacy harm), data governance (training data representative, tested for bias), technical documentation (system design, datasets, test results), record-keeping (logs retained for oversight), transparency (users informed the system is AI, how it works, how to challenge outputs), human oversight (users can override or ignore the score), accuracy and robustness (tested for false positives and bias across protected groups). Compliance date: 2 December 2027 (deferred by the Digital Omnibus from the original 2 August 2026 date).

## Frameworks Covered

EU AI Act (Regulation (EU) 2024/1689), Annex III (high-risk AI systems, point 4(a) employment), Article 6(3) (narrow-task exemption), Articles 9-15 (high-risk AI system obligations), Regulation (EU) 2026/1744 (Digital Omnibus, compliance date deferral)

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full classification assessment with feature description, initial exemption claim, why the exemption fails (profiling analysis), high-risk determination, compliance obligations under Articles 9-15, and the deferred compliance date |
| `README.md` | This file |

## Key Decision

The exemption claim fails because Workforce Signals profiles workers. Profiling closes the exemption regardless of how narrow the task looks, and regardless of whether a human makes the final decision. The classification is not about whether the feature is helpful or whether managers use it responsibly. It is about whether the feature meets the legal definition of profiling under Annex III, point 4(a). It does. Veskaro must implement high-risk obligations or disable the feature in the EU. The compliance date is 2 December 2027, deferred from the original 2 August 2026 date by the Digital Omnibus (Regulation (EU) 2026/1744, published 24 July 2026, entered into force 27 July 2026).
