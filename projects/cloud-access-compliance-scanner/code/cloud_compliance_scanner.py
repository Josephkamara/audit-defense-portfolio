"""
Cloud Access Compliance Scanner
Joseph Kamara, CPA, CISSP, CISA

Automates four logical-access and data-protection control tests against an
AWS account, mapped to SOC 2 Trust Services Criteria (CC6 series) and the
equivalent SOX IT General Control objectives an auditor would test manually:

  1. Stale IAM access keys (SOC 2 CC6.1 / ITGC: periodic credential review)
  2. IAM users without MFA enabled (SOC 2 CC6.1 / ITGC: authentication control)
  3. S3 buckets with public access enabled (SOC 2 CC6.6-CC6.7 / ITGC: data
     protection, segregation of environments)
  4. IAM policies granting wildcard ("*:*") permissions (SOC 2 CC6.1 / ITGC:
     least-privilege provisioning)

Each check returns structured findings (resource, condition, severity,
control reference) rather than a pass/fail count, so the output reads like
audit workpaper evidence rather than a generic scan result.
"""

from __future__ import annotations

import datetime
import json
from dataclasses import asdict, dataclass, field


@dataclass
class Finding:
    check: str
    resource: str
    condition: str
    severity: str  # "High", "Medium", "Low"
    control_reference: str
    detail: str


@dataclass
class ComplianceReport:
    generated_at: str
    account_id: str
    findings: list = field(default_factory=list)

    def add(self, finding: Finding) -> None:
        self.findings.append(finding)

    def summary_counts(self) -> dict:
        counts = {"High": 0, "Medium": 0, "Low": 0}
        for f in self.findings:
            counts[f.severity] = counts.get(f.severity, 0) + 1
        return counts

    def to_dict(self) -> dict:
        return {
            "generated_at": self.generated_at,
            "account_id": self.account_id,
            "summary": self.summary_counts(),
            "findings": [asdict(f) for f in self.findings],
        }

    def to_markdown(self) -> str:
        counts = self.summary_counts()
        lines = [
            f"# Cloud Access Compliance Report",
            f"",
            f"Account: `{self.account_id}`  ",
            f"Generated: {self.generated_at}  ",
            f"Findings: {len(self.findings)} total "
            f"({counts['High']} High, {counts['Medium']} Medium, {counts['Low']} Low)",
            f"",
            f"| Severity | Check | Resource | Control | Detail |",
            f"|---|---|---|---|---|",
        ]
        order = {"High": 0, "Medium": 1, "Low": 2}
        for f in sorted(self.findings, key=lambda x: order.get(x.severity, 9)):
            lines.append(
                f"| {f.severity} | {f.check} | `{f.resource}` | {f.control_reference} | {f.detail} |"
            )
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Individual control tests
# ---------------------------------------------------------------------------

def key_age_days(create_date: datetime.datetime, now: datetime.datetime | None = None) -> int:
    """Pure helper, isolated so the age-threshold logic can be unit tested
    without needing a mocked AWS account or a real 90-day-old key."""
    now = now or datetime.datetime.now(datetime.timezone.utc)
    return (now - create_date).days


def check_stale_access_keys(iam_client, report: ComplianceReport, max_age_days: int = 90) -> None:
    """SOC 2 CC6.1 / ITGC periodic credential review.

    Flags any active IAM access key older than `max_age_days`. This is the
    automated equivalent of the manual quarterly credential-review step an
    auditor tests by pulling an IAM credential report and eyeballing dates.
    """
    now = datetime.datetime.now(datetime.timezone.utc)
    users = iam_client.list_users()["Users"]
    for user in users:
        username = user["UserName"]
        keys = iam_client.list_access_keys(UserName=username)["AccessKeyMetadata"]
        for key in keys:
            if key["Status"] != "Active":
                continue
            age_days = key_age_days(key["CreateDate"], now=now)
            if age_days > max_age_days:
                report.add(
                    Finding(
                        check="Stale access key",
                        resource=f"{username}/{key['AccessKeyId']}",
                        condition=f"Active key is {age_days} days old (threshold {max_age_days})",
                        severity="High" if age_days > max_age_days * 2 else "Medium",
                        control_reference="SOC 2 CC6.1 / ITGC credential rotation",
                        detail=f"{age_days}d old, created {key['CreateDate'].date()}",
                    )
                )


def check_mfa_enabled(iam_client, report: ComplianceReport) -> None:
    """SOC 2 CC6.1 authentication control: every IAM user should have an MFA device."""
    users = iam_client.list_users()["Users"]
    for user in users:
        username = user["UserName"]
        mfa_devices = iam_client.list_mfa_devices(UserName=username)["MFADevices"]
        if not mfa_devices:
            report.add(
                Finding(
                    check="MFA not enabled",
                    resource=username,
                    condition="No MFA device registered for an IAM user with console/API access",
                    severity="High",
                    control_reference="SOC 2 CC6.1 / ITGC authentication control",
                    detail="Zero MFA devices attached",
                )
            )


def check_public_s3_buckets(s3_client, report: ComplianceReport) -> None:
    """SOC 2 CC6.6/CC6.7 data protection: buckets should not be publicly readable/writable."""
    buckets = s3_client.list_buckets()["Buckets"]
    for bucket in buckets:
        name = bucket["Name"]
        try:
            acl = s3_client.get_bucket_acl(Bucket=name)
        except Exception:
            continue
        for grant in acl.get("Grants", []):
            grantee = grant.get("Grantee", {})
            uri = grantee.get("URI", "")
            if "AllUsers" in uri or "AuthenticatedUsers" in uri:
                permission = grant.get("Permission", "UNKNOWN")
                report.add(
                    Finding(
                        check="Public S3 bucket ACL",
                        resource=name,
                        condition=f"Bucket ACL grants {permission} to {uri.rsplit('/', 1)[-1]}",
                        severity="High",
                        control_reference="SOC 2 CC6.6/CC6.7 data protection",
                        detail=f"Grantee URI: {uri}, permission: {permission}",
                    )
                )


def check_wildcard_iam_policies(iam_client, report: ComplianceReport) -> None:
    """SOC 2 CC6.1 least privilege: flag customer-managed policies granting Action='*' on Resource='*'."""
    policies = iam_client.list_policies(Scope="Local")["Policies"]
    for policy in policies:
        arn = policy["Arn"]
        version_id = policy["DefaultVersionId"]
        version = iam_client.get_policy_version(PolicyArn=arn, VersionId=version_id)
        document = version["PolicyVersion"]["Document"]
        statements = document.get("Statement", [])
        if isinstance(statements, dict):
            statements = [statements]
        for statement in statements:
            if statement.get("Effect") != "Allow":
                continue
            actions = statement.get("Action", [])
            resources = statement.get("Resource", [])
            if isinstance(actions, str):
                actions = [actions]
            if isinstance(resources, str):
                resources = [resources]
            if "*" in actions and "*" in resources:
                report.add(
                    Finding(
                        check="Wildcard IAM policy",
                        resource=policy["PolicyName"],
                        condition="Policy statement allows Action:* on Resource:*",
                        severity="High",
                        control_reference="SOC 2 CC6.1 / ITGC least-privilege provisioning",
                        detail=f"Policy ARN {arn}",
                    )
                )


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def run_all_checks(iam_client, s3_client, account_id: str) -> ComplianceReport:
    report = ComplianceReport(
        generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        account_id=account_id,
    )
    check_stale_access_keys(iam_client, report)
    check_mfa_enabled(iam_client, report)
    check_public_s3_buckets(s3_client, report)
    check_wildcard_iam_policies(iam_client, report)
    return report


if __name__ == "__main__":
    import boto3

    iam = boto3.client("iam", region_name="us-east-1")
    s3 = boto3.client("s3", region_name="us-east-1")
    sts = boto3.client("sts", region_name="us-east-1")
    account_id = sts.get_caller_identity()["Account"]

    report = run_all_checks(iam, s3, account_id)
    print(report.to_markdown())
    with open("compliance_report.json", "w") as f:
        json.dump(report.to_dict(), f, indent=2)
