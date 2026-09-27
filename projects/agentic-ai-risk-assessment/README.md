# Agentic AI Risk Assessment

**Fictional company, sample data, for portfolio demonstration only.**

This project demonstrates how to assess an autonomous AI agent that has authority to act on its own, using the OWASP Top 10 for Agentic Applications, MITRE ATLAS attack paths, and NIST AI Risk Management Framework.

## The Fictional Company

A fictional wholesale distributor handling accounts payable for thousands of transactions per month. The company deployed an AI agent with authority to read vendor bills, match them against purchase orders, and approve payment on its own for transactions below a threshold, no human review. Transactions above the threshold route to a human approver. The agent uses a large language model to extract data, a retrieval system to pull purchase order details, and a decision engine to compare and approve or reject.

## Read This in 3 Minutes

If you have three minutes:

1. **What the agent does:** The agent reads vendor bills (PDF, email, or scanned image), extracts vendor name, transaction number, line items, quantities, unit prices, and total amount. It retrieves the matching purchase order from the ERP system. It compares data to PO data: vendor match, line items match, quantities within tolerance, unit prices match, total within PO approval limit. If all checks pass and the total is below the threshold, it approves payment and updates the ERP. If any check fails, it rejects and routes to human review. If the total meets or exceeds the threshold, it routes to human review regardless of match quality.
2. **The risks:** Prompt injection: an attacker embeds a hidden instruction in a document and the agent follows it. Excessive autonomy: the agent approves a payment without verifying the vendor's bank account changed since the last payment (a business email compromise indicator). Lack of grounding: the agent hallucinates a purchase order that does not exist and approves a transaction with no PO. Authorization failure: the agent has write access to the ERP with no rate limit, so a compromised agent or a malicious batch can approve many fraudulent payments before anyone notices.
3. **The controls:** Input validation: strip all instructions and prompt-like text from documents before the model sees them. Human-in-the-loop: require human approval for any transaction where the vendor's bank details changed since the last payment, or where the document was received from a new email address not on file. Verification: log the PO lookup and require the PO to exist in the ERP with a status of open or partially received. Authorization boundary: limit the agent to a small number of approvals per hour, and require dual approval (agent plus human) for any vendor flagged as high-risk in the vendor master file. Audit trail: log every decision with the document, the PO, the comparison results, and the approval or rejection reason.

## Frameworks Covered

OWASP Top 10 for Agentic Applications (v1.0, December 2025), MITRE ATLAS (adversarial threat landscape for AI systems), NIST AI Risk Management Framework (AI RMF 1.0), generative AI profile

## What Is in the Folder

| File | Description |
|------|-------------|
| `index.html` | Full risk assessment with agent description, OWASP Top 10 threat analysis, one MITRE ATLAS attack path (invoice injection to fraudulent payment), NIST AI RMF controls mapped to the AI lifecycle (design, data, deployment, operation), and residual risk statement |
| `README.md` | This file |

## Key Finding

The agent as originally designed had excessive autonomy (OWASP-A3): it approved payments without checking for bank account changes, a known business email compromise indicator. The control set adds human-in-the-loop for bank account changes, limits the agent to 10 approvals per hour, and requires dual approval for high-risk vendors. The residual risk is that a sophisticated prompt injection attack could still bypass input validation and cause the agent to approve a fraudulent invoice, but the rate limit and the high-risk vendor flag reduce the blast radius. The assessment structures the controls using NIST AI RMF: Govern (risk appetite, acceptable use), Map (threat model, OWASP and ATLAS), Measure (logging and audit trail), and Manage (human oversight, authorization limits).
