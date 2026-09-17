# Cloud Access Compliance Report

Account: `123456789012`  
Generated: 2026-09-17T14:37:03+00:00  
Findings: 5 total (4 High, 1 Medium, 0 Low)

| Severity | Check | Resource | Control | Detail |
|---|---|---|---|---|
| High | MFA not enabled | `bob.stale-key` | SOC 2 CC6.1 / ITGC authentication control | Zero MFA devices attached |
| High | MFA not enabled | `carol.no-mfa` | SOC 2 CC6.1 / ITGC authentication control | Zero MFA devices attached |
| High | Public S3 bucket ACL | `public-marketing-assets` | SOC 2 CC6.6/CC6.7 data protection | Grantee URI: http://acs.amazonaws.com/groups/global/AllUsers, permission: READ |
| High | Wildcard IAM policy | `LegacyFullAccessPolicy` | SOC 2 CC6.1 / ITGC least-privilege provisioning | Policy ARN arn:aws:iam::123456789012:policy/LegacyFullAccessPolicy |
| Medium | Stale access key | `bob.stale-key/AKIARZPUZDIKA2F7AFL5` | SOC 2 CC6.1 / ITGC credential rotation | 120d old, created 2026-05-20 |