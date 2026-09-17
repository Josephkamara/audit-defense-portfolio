# Cloud Access Compliance Scanner

**Author:** Joseph Kamara, CPA, CISSP, CISA
**Status:** Working, tested code. Not a design sample.

## Portfolio note

This is a real Python tool, not a mockup. It runs against a mocked AWS account (via the `moto` library) with no real AWS credentials, no real cloud account, and no cost. Every check in this project executes and passes an automated test. The account, users, keys, policies, and buckets in the demo are fictional and created only to exercise the code.

## What it does

The scanner automates four access and data-protection control tests against an AWS account. Each test maps to a control an auditor already tests manually, either under SOC 2 (Trust Services Criteria, CC6 series) or as a SOX IT General Control (ITGC):

| Check | Control mapping | What it catches |
|---|---|---|
| Stale IAM access keys | SOC 2 CC6.1 / ITGC credential rotation | Active access keys older than 90 days |
| Missing MFA | SOC 2 CC6.1 / ITGC authentication control | IAM users with no MFA device registered |
| Public S3 buckets | SOC 2 CC6.6-CC6.7 / data protection | Bucket ACLs that grant access to AllUsers or AuthenticatedUsers |
| Wildcard IAM policies | SOC 2 CC6.1 / least-privilege provisioning | Customer-managed policies that allow Action:* on Resource:* |

The output is a structured finding, not a pass/fail count: resource, condition, severity, control reference, and detail. That is the same shape as audit workpaper evidence, because that is what it is meant to replace or support.

## Why it exists

Manual credential reviews, MFA checks, bucket permission reviews, and policy reviews are recurring audit steps. They are also the kind of control testing that scripting and API-based evidence pulls can do faster and more consistently than a manual walkthrough. This project demonstrates that translation directly: turning a manual control test into a repeatable script an auditor or a security team can run on a schedule.

## How it was built and tested

The scanner is written against the real `boto3` AWS SDK, so the same code runs against a real AWS account without modification. It was developed and verified using:

- **`moto`** (`@mock_aws`): mocks the AWS IAM, S3, and STS APIs in memory. No AWS account, credentials, or charges are involved in development or testing.
- **`freezegun`** (`freeze_time`): used to genuinely create one demo access key with a `CreateDate` 120 days in the past, so the stale-key check is proven against a real time difference rather than a hardcoded result.
- **`pytest`**: 10 unit tests, each isolating one control check in both its positive case (the condition is present and gets flagged) and its negative case (a compliant resource is confirmed clean). All 10 pass.

Test coverage:

1. `test_key_age_days_pure_math`: the date-math helper is correct in isolation
2. `test_stale_access_key_is_flagged`: a 95-day-old key is caught
3. `test_fresh_access_key_is_not_flagged`: a brand-new key is not a false positive
4. `test_very_old_key_is_high_severity_not_just_medium`: severity escalates past 2x the threshold
5. `test_user_without_mfa_is_flagged`
6. `test_user_with_enabled_mfa_is_not_flagged`
7. `test_public_bucket_acl_is_flagged`
8. `test_private_bucket_is_not_flagged`
9. `test_wildcard_policy_is_flagged`
10. `test_scoped_policy_is_not_flagged`: a least-privilege policy is not a false positive

## Files

- `cloud_compliance_scanner.py`: the scanner itself. Import and run `run_all_checks(iam_client, s3_client, account_id)` against any `boto3` IAM and S3 client.
- `test_cloud_compliance_scanner.py`: the pytest suite. Run with `pytest -v test_cloud_compliance_scanner.py`.
- `demo_seed_and_run.py`: seeds a mocked account with a mix of compliant and non-compliant users, keys, policies, and buckets, then runs the scanner and prints the report. This is the fastest way to see the tool work end to end.
- `demo_compliance_report.json` and `demo_compliance_report.md`: the actual output from running `demo_seed_and_run.py`. 5 findings (4 High, 1 Medium), with the compliant user, the private bucket, and the scoped policy confirmed absent from the findings.

## How to run it

```bash
pip install boto3 moto freezegun pytest

# See the tool work end to end against a seeded mock account
python3 demo_seed_and_run.py

# Run the full test suite
pytest -v test_cloud_compliance_scanner.py

# Run against a real AWS account (reads live IAM and S3 data, makes no changes)
python3 cloud_compliance_scanner.py
```

Running against a real account requires standard AWS credentials configured in the environment (`aws configure` or equivalent) and read-only IAM and S3 permissions. The script only calls list and get operations. It makes no changes to any resource.
