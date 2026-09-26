# First 90 Days: IT Auditor Onboarding Plan

**Fictional company, sample data, for portfolio demonstration only.**

## Purpose

This 30/60/90-day plan is designed for an IT auditor joining Keystone Civic Payments as a Senior IT Auditor or IT Audit Manager. The plan focuses on learning the environment, building relationships with control owners, owning a testing cycle, reducing duplicate evidence requests, and improving one process.

---

## First 30 Days: Learn the Environment and Prior Reports

### Week 1: Orientation and Access Setup

**Objectives:**

- Complete HR onboarding and system access provisioning.
- Understand Keystone's business model, customers, and compliance obligations.
- Review the organizational structure and identify key stakeholders.

**Activities:**

- [ ] **Day 1-2:** HR onboarding, benefits enrollment, security awareness training, policy acknowledgment.
- [ ] **Day 2-3:** Request and obtain access to:
  - Okta (SSO for all applications)
  - AWS IAM Identity Center (read-only access to production accounts for audit purposes)
  - ServiceNow (IT auditor role for access to change records, incidents, access requests)
  - GRC platform (read-only access to issue register, remediation tracker, risk register)
  - Shared Google Drive (audit evidence repository)
  - SIEM (Splunk, read-only access for log review)
- [ ] **Day 3-5:** Read the following documents:
  - Company overview deck (business model, customers, revenue)
  - Organizational chart (report to the CISO or CFO? Understand the reporting structure)
  - PCI DSS scope confirmation memo (most recent)
  - SOC 1 and SOC 2 reports (most recent)
  - GovRAMP system security plan (SSP) executive summary
  - Unified control matrix (02-control-matrix/unified-control-matrix.csv)
  - Compliance calendar (07-continuous-compliance/compliance-calendar-and-kpis.md)
- [ ] **Day 5:** Meet with the Director of GRC:
  - Understand the Director's expectations for the IT auditor role.
  - Confirm the scope of responsibilities (internal testing, audit coordination, evidence management, process improvement).
  - Identify immediate priorities (upcoming audit fieldwork, open findings, overdue remediation items).

### Week 2: Review Prior Audit Reports and Findings

**Objectives:**

- Understand what prior auditors tested, what findings were issued, and what remediation was completed.
- Identify any open or repeat findings.

**Activities:**

- [ ] **Read the most recent PCI ROC** (full report, not just the AOC):
  - What testing did the QSA perform? (Look at the testing procedures section for each requirement.)
  - Were there any compensating controls or findings?
  - What was the QSA's assessment of the segmentation controls?
  - What evidence did the QSA request that was difficult to provide?
- [ ] **Read the most recent SOC 1 and SOC 2 reports** (user entity auditor perspective):
  - What exceptions were noted in the Type 2 report?
  - What were the complementary user entity controls (CUECs) for the subservice orgs (AWS, GatewayCo)?
  - Which deviations were reported in the tests of controls, and how did management respond?
  - Was the opinion unmodified? If it was modified, which control objectives or criteria were not achieved?
- [ ] **Review the GovRAMP POA&M** (current version):
  - What open findings exist?
  - What are their due dates and risk levels?
  - Are any findings approaching 90 days old (escalation threshold)?
- [ ] **Read the gap analysis and remediation tracker** (05-gap-analysis/):
  - What gaps were identified in the readiness assessment?
  - What gaps have been remediated, and what gaps are still open?
- [ ] **Meet with the Director of GRC (second meeting):**
  - Discuss the findings from prior reports.
  - Ask: "What finding surprised you the most?" and "What finding do you worry might recur?"
  - Understand the Director's priorities for the next audit cycle.

### Week 3: Shadow a Control Owner

**Objectives:**

- Observe how controls operate in practice, not just on paper.
- Build a relationship with one control owner before you start testing their controls.

**Activities:**

- [ ] **Shadow the IAM Manager for one day:**
  - Watch how access requests are approved and provisioned (ACC-01).
  - Watch how a termination flows through the system (ACC-02).
  - See the quarterly access review process (ACC-04) if a review is occurring this week.
  - Ask: "What part of this process is the most manual?" and "What breaks most often?"
- [ ] **Shadow the Security Operations Manager for one afternoon:**
  - Watch how the SOC triages SIEM alerts (LOG-03).
  - See how a critical control failure alert is investigated (LOG-04).
  - Ask: "What alert do you see the most false positives from?" and "What alert worries you the most when it fires?"
- [ ] **Shadow the Cloud Platform Engineering Manager for one afternoon:**
  - Watch how a production deployment flows through the CI/CD pipeline (CHG-01, CHG-02, CHG-05).
  - See how AWS Config compliance checks work (CHG-09).
  - Ask: "What change has the highest risk of causing an outage?" and "How do you test changes before production?"

### Week 4: Map the Unified Control Matrix to Systems and Evidence

**Objectives:**

- Understand how the "map once, evidence once" principle works in practice, and where each assessor still tests independently.
- Identify where evidence for each control comes from.

**Activities:**

- [ ] **Pick 5 controls from the unified control matrix** (one from each domain: Governance, Access, Change, Operations, Logging):
  - For each control, trace the evidence source:
    - What system generates the evidence? (Okta, AWS, ServiceNow, SIEM)
    - Who owns the evidence? (IAM Manager, Security Operations Manager, etc.)
    - How is the evidence exported? (CSV, API, screenshot, log file)
    - Where is the evidence stored? (Google Drive folder, GRC platform attachment)
- [ ] **Create a personal reference guide:**
  - For each of the 5 controls, document:
    - Control ID and statement
    - Framework mappings (PCI, SOC 2, NIST, SOX)
    - Evidence source and export instructions
    - Sample evidence file name
  - This guide will become your cheat sheet when auditors request evidence.
- [ ] **Meet with the Vendor Risk Manager:**
  - Understand how Keystone tracks vendor SOC reports and AOCs.
  - See the vendor inventory and risk tiering.
  - Ask: "Which vendor's SOC report is the hardest to review?" and "Have you ever found a CUEC that Keystone wasn't covering?"

---

## Next 30 Days (Days 31-60): Build Relationships and Own a Testing Cycle

### Week 5: Meet All Control Owners

**Objectives:**

- Introduce yourself to every control owner listed in the unified control matrix.
- Build trust before you start asking them for evidence.

**Activities:**

- [ ] **Schedule 30-minute intro meetings** with each control owner role:
  - CISO
  - Director of GRC (you've met them, but schedule a deeper dive)
  - Director of Engineering
  - Cloud Platform Engineering Manager
  - AppSec Lead
  - Security Operations Manager
  - IAM Manager
  - DBA Lead
  - IT Operations Manager
  - Payment Operations Manager
  - Network Security Lead
  - Vendor Risk Manager
  - Privacy and Data Governance Lead
  - HR Director
- [ ] **In each meeting, ask:**
  - "What controls do you own?" (refer to the matrix)
  - "What evidence do you provide to auditors?"
  - "What evidence request from a past audit was the most painful to fulfill?"
  - "What control do you worry might fail if tested?"
  - "What process improvement would make your life easier?"
- [ ] **Document each control owner's pain points** in a personal notes file. You will use this later when you propose process improvements.

### Week 6-7: Own a Full ITGC Testing Cycle

**Objectives:**

- Test one ITGC area end to end, from population definition to workpaper completion.
- Experience what an auditor will ask for, so you can prepare better evidence next time.

**Activities:**

- [ ] **Pick one ITGC area to test** (choose one that is due soon based on the compliance calendar):
  - Quarterly privileged access review (ACC-04) if Q4 2026 review just completed
  - Monthly internal vulnerability scan (VUL-01) for the most recent month
  - Change management (CHG-01) for a sample of changes from the past month
- [ ] **Follow the test procedure** in the 03-itgc-test-procedures/ folder:
  - Obtain the population (access review results, vulnerability scan reports, change records).
  - Perform IPE (information produced by the entity) testing: verify completeness and accuracy of the population.
  - Select a sample per the sample size guidance.
  - Test each attribute (approvals, removal tickets, remediation evidence, etc.).
  - Document results in a workpaper (create your own using the sample workpaper format from 03-periodic-and-privileged-access-review.md as a template).
  - If you find an exception, document the deviation, perform inquiry to determine root cause, identify mitigating factors, and assess whether it is isolated or systemic.
- [ ] **Review your workpaper with the Director of GRC:**
  - Ask for feedback: "Did I test the right attributes?" and "Would this workpaper satisfy an auditor?"
  - Discuss any exceptions you found: "Is this exception already tracked in the remediation tracker or POA&M?"

### Week 8: Prepare for the Next Audit Fieldwork

**Objectives:**

- Understand what evidence the next audit (PCI ROC, SOC audit, or GovRAMP assessment) will request.
- Start gathering evidence early to avoid last-minute scrambling.

**Activities:**

- [ ] **Identify the next audit on the calendar:**
  - Is it PCI DSS ROC fieldwork (December 2026)?
  - Is it SOC 1/SOC 2 fieldwork (March 2027)?
  - Is it the GovRAMP annual 3PAO assessment (December 2026)?
- [ ] **Review the PBC (provided by client) request list** from the prior year's audit:
  - What evidence did the auditor request last year?
  - What evidence was re-requested or flagged as incomplete?
- [ ] **Create a draft PBC request list for the upcoming audit:**
  - Use the pbc-request-list.csv from 04-evidence/ as a starting template.
  - For each request, identify:
    - Control reference (from the unified control matrix)
    - Description of evidence
    - Owner (who will provide it)
    - Due date (work backward from the audit fieldwork start date)
    - Format (CSV, PDF, screenshot, etc.)
- [ ] **Send the draft PBC list to control owners for review:**
  - Ask: "Can you provide this evidence by [due date]?" and "Is the format I'm requesting the easiest format for you to export?"
  - Update the list based on their feedback.

---

## Final 30 Days (Days 61-90): Reduce Duplicate Requests and Improve One Process

### Week 9: Map Duplicate Evidence Requests Across Audits

**Objectives:**

- Identify evidence that is requested by multiple auditors (PCI QSA, SOC auditor, GovRAMP assessor) and reduce duplication.
- Create a cross-reference document so auditors know that one piece of evidence answers multiple requests.

**Activities:**

- [ ] **Review past PCI, SOC, and GovRAMP evidence requests:**
  - For each piece of evidence provided (example: Okta System Log showing MFA challenges), list which audits requested it:
    - PCI QSA requested it for 8.4.1 to 8.4.3.
    - SOC auditor requested it for CC6.1.
    - GovRAMP assessor requested it for IA-2(1) and IA-2(2).
- [ ] **Create a cross-reference table:**
  - Use the format from the unified control matrix README: Control ID → PCI Req → SOC 2 TSC → NIST 800-53 → Evidence Location.
  - For the top 20 most frequently requested pieces of evidence, document which audits they satisfy.
- [ ] **Propose a shared evidence repository folder structure:**
  - Organize evidence by control ID (not by auditor or framework).
  - Share folder links with all auditors instead of providing separate copies.
  - Example folder structure:
    ```
    Audit Evidence 2026-2027/
      ACC-01 User Provisioning/
        ServiceNow-Access-Request-Export.csv
      ACC-04 Access Review/
        Q1-2026-Review.csv
        Q2-2026-Review.csv
        Q3-2026-Review.csv
        Q4-2026-Review.csv
      ACC-06 MFA/
        Okta-MFA-Config.pdf
        Okta-MFA-Log-Sample.csv
    ```
- [ ] **Present the cross-reference table and folder structure to the Director of GRC:**
  - Explain how this will reduce duplicate evidence requests.
  - Get approval to pilot the new structure for the next audit.

### Week 10-11: Improve One Process

**Objectives:**

- Pick one process pain point (identified during Weeks 5-6 when you met control owners) and fix it.
- Show value by making a control owner's job easier.

**Activities:**

- [ ] **Pick one improvement project** (examples based on common pain points):
  - **Automate a manual evidence export:** If the IAM Manager manually exports Okta access review results every quarter, write a script (or work with the IAM Manager) to automate the export and save it to the shared evidence repository.
  - **Improve a workpaper template:** If the Security Operations Manager's log review workpaper is a blank Word doc every month, create a reusable template with pre-filled sections (Population, Sample Selection, Test Steps, Results, Exceptions).
  - **Fix a recurring evidence quality issue:** If the auditor re-requests evidence every year because the query parameters are not visible, update the export procedure to require parameters and timestamps in every export.
  - **Reduce a false positive alert:** If the SOC triages the same false positive alert every week, work with the Security Operations Manager to tune the SIEM rule or add an exclusion.
- [ ] **Implement the improvement:**
  - Get buy-in from the control owner.
  - Test the improvement (example: run the automated export script; verify it produces the same output as the manual export).
  - Document the new process (update the control description, test procedure, or evidence export instructions).
- [ ] **Measure the impact:**
  - How much time did the improvement save? (example: reduced quarterly access review evidence preparation from 2 hours to 15 minutes)
  - Did the improvement reduce errors or re-requests?
- [ ] **Present the improvement to the Director of GRC and the Risk Committee:**
  - Use the 90-day check-in meeting to showcase what you fixed.
  - Propose rolling the improvement out to other similar processes.

### Week 12: 90-Day Check-In and Set Goals for the Next Quarter

**Objectives:**

- Reflect on what you learned in the first 90 days.
- Set goals for the next quarter (continuous compliance, audit preparation, process improvement).

**Activities:**

- [ ] **Schedule a 90-day check-in meeting with the Director of GRC:**
  - Discuss what you accomplished:
    - "I learned the environment and reviewed all prior audit reports."
    - "I built relationships with all control owners."
    - "I owned a full testing cycle for [ITGC area]."
    - "I reduced duplicate evidence requests by creating a cross-reference table and shared evidence repository."
    - "I improved [specific process] and saved [X hours per quarter]."
  - Ask for feedback: "What should I focus on in the next 90 days?"
- [ ] **Set goals for Days 91-180:**
  - **Goal 1:** Own the next audit fieldwork cycle (PCI ROC or SOC audit) end to end, from PBC list creation to evidence coordination to auditor question responses.
  - **Goal 2:** Test all 7 ITGC areas (not just the one you tested in Week 6-7) over the next two quarters, so you have firsthand experience with every control domain.
  - **Goal 3:** Propose and implement a second process improvement (pick from the pain points you documented in Week 5).
  - **Goal 4:** Build deeper technical expertise in one compliance framework (example: become the go-to person for GovRAMP continuous monitoring, or for PCI DSS v4.0.1 future-dated requirements).
- [ ] **Share your 90-day reflection with the team:**
  - At the next Risk Committee meeting or GRC team meeting, present a 5-minute summary of your first 90 days.
  - Highlight one thing you learned that surprised you (example: "I didn't realize how much manual work goes into quarterly access reviews; we should explore automation").
  - Thank the control owners who helped you onboard.

---

## Success Metrics for the First 90 Days

By the end of the first 90 days, the new IT auditor should have:

- [ ] Reviewed all prior audit reports (PCI ROC, SOC 1/SOC 2, GovRAMP assessment) and identified open findings.
- [ ] Met every control owner listed in the unified control matrix.
- [ ] Completed one full ITGC testing cycle with a documented workpaper.
- [ ] Created a cross-reference table or evidence repository structure that reduces duplicate evidence requests.
- [ ] Implemented one process improvement that saves time or reduces errors.
- [ ] Set clear goals for the next 90 days.

---

## Tips for Success

1. **Ask questions early.** The first 30 days are when you have the most permission to ask "basic" questions. After 90 days, control owners will expect you to already know the answers.
2. **Build trust before you test.** If your first interaction with a control owner is "I need evidence for an audit," they will see you as a burden. If your first interaction is "I want to understand how your control works," they will see you as a partner.
3. **Shadow before you test.** Watching a control operate in real time (access provisioning, log review, change deployment) gives you context that reading a policy never will.
4. **Document everything.** Your personal reference guide (control ID, evidence source, export instructions) will save you hours when auditors start requesting evidence.
5. **Propose improvements, not criticisms.** When you find a gap or a manual process, frame it as "I can help automate this" or "I have an idea to make this easier," not "this is broken."
6. **Own something end to end.** Testing one ITGC area from population to workpaper gives you credibility. It shows you are not just coordinating audits; you are doing the work.

By following this plan, the new IT auditor will be productive, trusted, and ready to own the next audit cycle by Day 91.
