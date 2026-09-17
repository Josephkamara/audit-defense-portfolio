# Cloud Access Compliance Scanner: Working Code for Four SOC 2 and SOX Access Controls

A Python scanner that pulls real evidence for four access and data-protection controls instead of describing how they could be pulled: stale IAM access keys, missing MFA, public S3 buckets, and wildcard IAM policies. Built against the real boto3 SDK and verified with a 10-test pytest suite against a mocked AWS account (moto), including a genuinely time-shifted test key (freezegun) rather than a faked comparison.

This is real, working code, not a design sample. All 10 tests pass.

**Framework:** SOC 2 Trust Services Criteria (CC6 series) and the equivalent SOX IT General Controls
**Tags:** Cloud Security, SOC 2, Automation

[Read the full write-up](https://josephkamara.github.io/audit-defense-portfolio/projects/cloud-access-compliance-scanner/)

[View the code](code/)

[Back to the portfolio](../../)
