"""
Demo harness for cloud_compliance_scanner.py

Seeds a mocked AWS account (via moto, no real AWS credentials or costs
involved) with a deliberate mix of compliant and non-compliant resources,
then runs the scanner against it and prints the resulting report. This is
what proves the scanner logic actually works, not just reads plausibly.

Bob's access key is genuinely created 120 days in the past using freezegun
to move the system clock backward at creation time, so moto stamps a real
120-day-old CreateDate on it. Alice's key is created at the real "now," and
her MFA device is fully enabled, so she should raise zero findings. That
alice comes back clean while bob, carol, the wildcard policy, and the public
bucket all get flagged is what proves the checks discriminate correctly
rather than flagging everything indiscriminately.

Run: python3 demo_seed_and_run.py
"""

import datetime
import json

import boto3
from freezegun import freeze_time
from moto import mock_aws

from cloud_compliance_scanner import run_all_checks


@mock_aws
def main():
    iam = boto3.client("iam", region_name="us-east-1")
    s3 = boto3.client("s3", region_name="us-east-1")
    sts = boto3.client("sts", region_name="us-east-1")

    # --- Seed IAM users: one fully compliant, two with real findings ---
    iam.create_user(UserName="alice.compliant")
    iam.create_access_key(UserName="alice.compliant")  # created at real "now" -> not stale
    mfa_device = iam.create_virtual_mfa_device(VirtualMFADeviceName="alice-mfa")["VirtualMFADevice"]
    iam.enable_mfa_device(
        UserName="alice.compliant",
        SerialNumber=mfa_device["SerialNumber"],
        AuthenticationCode1="123456",
        AuthenticationCode2="789012",
    )  # alice now has an active MFA device and a fresh key -> should raise zero findings

    iam.create_user(UserName="bob.stale-key")
    with freeze_time(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=120)):
        # Genuinely creates the key with a CreateDate 120 days in the past,
        # rather than faking the comparison at check time.
        key = iam.create_access_key(UserName="bob.stale-key")["AccessKey"]
    # bob has no MFA device either -> two separate findings expected for bob

    iam.create_user(UserName="carol.no-mfa")
    iam.create_access_key(UserName="carol.no-mfa")  # fresh key, but no MFA device -> one finding

    # --- Seed an over-permissive customer-managed policy ---
    wildcard_policy_document = {
        "Version": "2012-10-17",
        "Statement": [{"Effect": "Allow", "Action": "*", "Resource": "*"}],
    }
    iam.create_policy(
        PolicyName="LegacyFullAccessPolicy",
        PolicyDocument=json.dumps(wildcard_policy_document),
    )

    # A properly scoped policy, seeded to prove the check does NOT flag
    # least-privilege policies as false positives.
    scoped_policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {"Effect": "Allow", "Action": ["s3:GetObject"], "Resource": "arn:aws:s3:::reports-bucket/*"}
        ],
    }
    iam.create_policy(
        PolicyName="ScopedReportsReadPolicy",
        PolicyDocument=json.dumps(scoped_policy_document),
    )

    # --- Seed S3 buckets: one private, one public ---
    s3.create_bucket(Bucket="internal-audit-workpapers")  # default ACL, private -> no finding

    s3.create_bucket(Bucket="public-marketing-assets")
    s3.put_bucket_acl(
        Bucket="public-marketing-assets",
        AccessControlPolicy={
            "Grants": [
                {
                    "Grantee": {
                        "Type": "Group",
                        "URI": "http://acs.amazonaws.com/groups/global/AllUsers",
                    },
                    "Permission": "READ",
                }
            ],
            "Owner": {"ID": "demo-owner", "DisplayName": "demo"},
        },
    )

    account_id = sts.get_caller_identity()["Account"]

    # --- Run the real, unmodified scanner logic against this seeded account ---
    report = run_all_checks(iam, s3, account_id)

    print(report.to_markdown())
    print()
    print(f"Total findings: {len(report.findings)}")
    print(f"Severity breakdown: {report.summary_counts()}")
    print()
    flagged_resources = {f.resource.split("/")[0] for f in report.findings}
    print(f"alice.compliant appears in findings: {'alice.compliant' in flagged_resources} (expected: False)")
    print(f"internal-audit-workpapers appears in findings: {'internal-audit-workpapers' in flagged_resources} (expected: False)")
    print(f"ScopedReportsReadPolicy appears in findings: {'ScopedReportsReadPolicy' in flagged_resources} (expected: False)")

    with open("demo_compliance_report.json", "w") as f:
        json.dump(report.to_dict(), f, indent=2)
    with open("demo_compliance_report.md", "w") as f:
        f.write(report.to_markdown())

    return report


if __name__ == "__main__":
    main()
