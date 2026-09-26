# Test Procedure 01: User Provisioning

**Control Reference:** ACC-01

**Control Statement:** Access to in-scope systems is requested in ServiceNow and approved by the user's manager and the system owner before provisioning. Access is granted through role-based Okta groups mapped to job function and least privilege.

**Control Owner:** IAM Manager

**Frequency:** Recurring (event-driven, many times per day)

**Nature:** IT-dependent manual

**Type:** Preventive

**Key Control:** Yes

## Control Objective

To ensure that user access is granted only after appropriate approval and is limited to what is necessary for the user's job function (least privilege principle).

## Applicable Framework Requirements

- **PCI DSS v4.0.1:** 7.2.1, 7.2.2, 7.2.3, 8.2.1, 8.2.4
- **SOC 2:** CC6.2, CC6.3
- **NIST SP 800-53 Rev 5:** AC-2, AC-6, IA-4
- **SOX ITGC:** Access to Programs and Data

## Population and Sample Size

**Population:** All access requests submitted and approved during the review period (typically 1,500-2,500 requests per year).

**Sample size:** 25 to 60 requests, stratified by system (Okta/AWS/ServiceNow/GitHub), month, and type (new hire, role change, temporary access).

## Test Steps

1. **Inquiry:** Ask the IAM Manager how access requests are submitted, approved, and provisioned.
2. **Observation:** Review the ServiceNow access request workflow and approval routing rules.
3. **Inspection:** Review the access provisioning policy and role matrix (job title → Okta groups → application access).
4. **Test of Operating Effectiveness:**
   - Obtain ServiceNow access request export for the selected period with request ID, requester, user, system, manager approval, system owner approval, provisioned date, Okta group assigned.
   - Select sample per above.
   - For each sampled request:
     - Confirm manager approved (approval in ServiceNow with timestamp before provisioning).
     - Confirm system owner approved (if required per policy; AWS admin roles and CDE access require system owner approval).
     - Confirm access was provisioned (trace request to Okta System Log showing group membership add event or AWS Identity Center assignment).
     - Confirm access matches the requested role (requested group = provisioned group, no excessive access granted).
     - Confirm provisioning occurred after approvals, not before.

## Sample Attributes

| Attribute | Expected | How to Test |
|-----------|----------|-------------|
| Manager approval | Present, timestamped before provisioning | Inspect ServiceNow approval history |
| System owner approval (if required) | Present for high-risk systems | Inspect ServiceNow approval history |
| Provisioned access matches request | Requested group = provisioned group | Trace to Okta System Log or AWS CLI output |
| Provisioning after approval | Provisioned timestamp > approval timestamp | Compare timestamps |
| No unapproved access | All provisioned access has an approved request | For a sample of current users, trace back to a request |

## Exception Example

**Exception:** One access request (REQ-12345) for AWS admin access approved only by the user's manager, not by the Cloud Platform Engineering Manager (system owner approval missing per policy).

**Root Cause:** The ServiceNow workflow was misconfigured and did not route the request to the system owner approval step for AWS admin roles. The misconfiguration was corrected the same week after the IAM Manager noticed the gap during a manual review.

**Remediation:** Workflow corrected, tested with a dummy request, and deployed. No further instances found in the remaining sample.

**Impact:** Isolated operational failure, not systemic. Recommend testing workflow changes before production deployment.
