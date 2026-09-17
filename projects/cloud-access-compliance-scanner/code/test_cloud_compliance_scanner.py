"""
Unit and integration tests for cloud_compliance_scanner.py

Run: pytest -v test_cloud_compliance_scanner.py

Covers each control test in isolation (positive and negative cases) plus the
pure age-threshold helper, so the logic is verified independent of any live
AWS account.
"""

import datetime
import json

import boto3
import pytest
from freezegun import freeze_time
from moto import mock_aws

from cloud_compliance_scanner import (
    ComplianceReport,
    check_mfa_enabled,
    check_public_s3_buckets,
    check_stale_access_keys,
    check_wildcard_iam_policies,
    key_age_days,
)


def new_report() -> ComplianceReport:
    return ComplianceReport(generated_at="2026-09-17T00:00:00+00:00", account_id="000000000000")


# ---------------------------------------------------------------------------
# Pure helper
# ---------------------------------------------------------------------------

def test_key_age_days_pure_math():
    created = datetime.datetime(2026, 1, 1, tzinfo=datetime.timezone.utc)
    now = datetime.datetime(2026, 4, 11, tzinfo=datetime.timezone.utc)  # 100 days later
    assert key_age_days(created, now=now) == 100


# ---------------------------------------------------------------------------
# Stale access keys
# ---------------------------------------------------------------------------

@mock_aws
def test_stale_access_key_is_flagged():
    iam = boto3.client("iam", region_name="us-east-1")
    iam.create_user(UserName="old-key-user")
    with freeze_time(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=95)):
        iam.create_access_key(UserName="old-key-user")

    report = new_report()
    check_stale_access_keys(iam, report, max_age_days=90)

    assert len(report.findings) == 1
    assert report.findings[0].check == "Stale access key"
    assert "old-key-user" in report.findings[0].resource


@mock_aws
def test_fresh_access_key_is_not_flagged():
    iam = boto3.client("iam", region_name="us-east-1")
    iam.create_user(UserName="fresh-key-user")
    iam.create_access_key(UserName="fresh-key-user")

    report = new_report()
    check_stale_access_keys(iam, report, max_age_days=90)

    assert len(report.findings) == 0


@mock_aws
def test_very_old_key_is_high_severity_not_just_medium():
    iam = boto3.client("iam", region_name="us-east-1")
    iam.create_user(UserName="ancient-key-user")
    with freeze_time(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=200)):
        iam.create_access_key(UserName="ancient-key-user")

    report = new_report()
    check_stale_access_keys(iam, report, max_age_days=90)

    assert report.findings[0].severity == "High"  # >2x threshold


# ---------------------------------------------------------------------------
# MFA
# ---------------------------------------------------------------------------

@mock_aws
def test_user_without_mfa_is_flagged():
    iam = boto3.client("iam", region_name="us-east-1")
    iam.create_user(UserName="no-mfa-user")

    report = new_report()
    check_mfa_enabled(iam, report)

    assert len(report.findings) == 1
    assert report.findings[0].check == "MFA not enabled"


@mock_aws
def test_user_with_enabled_mfa_is_not_flagged():
    iam = boto3.client("iam", region_name="us-east-1")
    iam.create_user(UserName="mfa-user")
    device = iam.create_virtual_mfa_device(VirtualMFADeviceName="mfa-user-device")["VirtualMFADevice"]
    iam.enable_mfa_device(
        UserName="mfa-user",
        SerialNumber=device["SerialNumber"],
        AuthenticationCode1="123456",
        AuthenticationCode2="789012",
    )

    report = new_report()
    check_mfa_enabled(iam, report)

    assert len(report.findings) == 0


# ---------------------------------------------------------------------------
# Public S3 buckets
# ---------------------------------------------------------------------------

@mock_aws
def test_public_bucket_acl_is_flagged():
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="public-bucket")
    s3.put_bucket_acl(
        Bucket="public-bucket",
        AccessControlPolicy={
            "Grants": [
                {
                    "Grantee": {"Type": "Group", "URI": "http://acs.amazonaws.com/groups/global/AllUsers"},
                    "Permission": "READ",
                }
            ],
            "Owner": {"ID": "owner", "DisplayName": "owner"},
        },
    )

    report = new_report()
    check_public_s3_buckets(s3, report)

    assert len(report.findings) == 1
    assert report.findings[0].resource == "public-bucket"


@mock_aws
def test_private_bucket_is_not_flagged():
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="private-bucket")

    report = new_report()
    check_public_s3_buckets(s3, report)

    assert len(report.findings) == 0


# ---------------------------------------------------------------------------
# Wildcard IAM policies
# ---------------------------------------------------------------------------

@mock_aws
def test_wildcard_policy_is_flagged():
    iam = boto3.client("iam", region_name="us-east-1")
    iam.create_policy(
        PolicyName="TooPermissive",
        PolicyDocument=json.dumps(
            {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": "*", "Resource": "*"}]}
        ),
    )

    report = new_report()
    check_wildcard_iam_policies(iam, report)

    assert len(report.findings) == 1
    assert report.findings[0].resource == "TooPermissive"


@mock_aws
def test_scoped_policy_is_not_flagged():
    iam = boto3.client("iam", region_name="us-east-1")
    iam.create_policy(
        PolicyName="ScopedPolicy",
        PolicyDocument=json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {"Effect": "Allow", "Action": ["s3:GetObject"], "Resource": "arn:aws:s3:::reports/*"}
                ],
            }
        ),
    )

    report = new_report()
    check_wildcard_iam_policies(iam, report)

    assert len(report.findings) == 0


if __name__ == "__main__":
    import sys

    sys.exit(pytest.main([__file__, "-v"]))
