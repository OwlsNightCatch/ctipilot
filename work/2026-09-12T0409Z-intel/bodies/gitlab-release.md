---
title: "GitLab Critical Patch Release: 19.3.2, 19.2.6, 19.1.8"
author: Katherine Wu
url: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/
hostname: gitlab.com
description: "Learn more about GitLab Critical Patch Release: 19.3.2, 19.2.6, 19.1.8 for GitLab Community Edition (CE) and Enterprise Edition (EE)."
sitename: GitLab Docs
date: "2011-03-03"
license: CC BY-SA 4.0
---
[Take the survey](https://gitlab.fra1.qualtrics.com/jfe/form/SV_e5Ig7YiRmL0RSm2).

# GitLab Critical Patch Release: 19.3.2, 19.2.6, 19.1.8

On September 10, 2026, we released versions 19.3.2, 19.2.6, 19.1.8 for GitLab Community Edition (CE) and Enterprise Edition (EE).

These versions contain important bug and security fixes, and we strongly recommend that all self-managed GitLab installations be upgraded to one of these versions immediately. GitLab.com is already running the patched version. GitLab Dedicated customers do not need to take action.

GitLab releases fixes for vulnerabilities in patch releases. There are two types of patch releases:
scheduled releases and ad-hoc critical patches for high-severity vulnerabilities. Scheduled releases are released twice a month on the second and fourth Wednesdays.
For more information, please visit our [releases handbook](https://handbook.gitlab.com/handbook/engineering/releases/) and [security FAQ](https://about.gitlab.com/security/faq/).
You can see all of GitLab release blog posts [here](https://docs.gitlab.com/releases/).

For security fixes, the issues detailing each vulnerability are made public on our
[issue tracker](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_date&state=closed&label_name%5B%5D=bug%3A%3Avulnerability&confidential=no&first_page_size=100)
90 days after the release in which they were patched.

We are committed to ensuring that all aspects of GitLab that are exposed to customers or that host customer data are held to
the highest security standards. To maintain good security hygiene, it is highly recommended that all customers
upgrade to the latest patch release for their supported version. You can read more
[best practices in securing your GitLab instance](https://about.gitlab.com/blog/gitlab-instance-security-best-practices/) in our blog post.

### Recommended Action

We **strongly recommend** that all installations running a version affected by the issues described below are **upgraded to the latest version as soon as possible**.

When no specific deployment type (omnibus, source code, helm chart, etc.) of a product is mentioned, it means all types are affected.

## Security fixes

### Table of security fixes

### [CVE-2026-85706](https://www.cve.org/CVERecord?id=CVE-2026-85706) - Path Traversal issue in repository commits API impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, an unauthenticated user could have read arbitrary files from the GitLab server due to improper path confinement and missing authentication enforcement in the repository commits API.

**Impacted Versions:** GitLab CE/EE: all versions from 18.7 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 10.0 ([`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N))

Thanks [s3ntago](https://hackerone.com/s3ntago) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2026-87719](https://www.cve.org/CVERecord?id=CVE-2026-87719) - Insecure Deserialization issue in GraphQL subscription serializer impacts GitLab EE

GitLab has remediated an issue that, under certain conditions, could allow an authenticated user with Duo Chat access to obtain Advanced Search instance configurations and sensitive credentials using a specially crafted GraphQL subscription argument to bypass serialization and perform server object lookup.

**Impacted Versions:** GitLab EE: all versions from 18.3 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 9.9 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H))

Thanks [kyyblin](https://hackerone.com/kyyblin) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2026-88765](https://www.cve.org/CVERecord?id=CVE-2026-88765) - Buffer Overflow issue in Unicode conversion wrapper impacts GitLab EE

GitLab has remediated an issue that, under certain conditions, could allow an authenticated user to achieve remote code execution by importing a specially crafted Git project export to overflow the Unicode conversion buffer used in Advanced Search indexing.

**Impacted Versions:** GitLab EE: all versions from 12.3 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 8.5 ([`CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H))

Thanks [joaxcar](https://hackerone.com/joaxcar) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2026-79708](https://www.cve.org/CVERecord?id=CVE-2026-79708) - Scheduled Pipeline Execution Policy test allows Developers to access protected CI/CD variables

GitLab has remediated an issue that, under certain conditions, could have allowed an authenticated user with developer permissions to execute a policy test pipeline on projects within their group and access protected CI/CD variables restricted to higher-privileged roles due to insufficient scope validation.

**Impacted Versions:** GitLab EE: all versions from 19.0 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 8.5 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:H/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:H/A:N))

Thanks [yvvdwf](https://hackerone.com/yvvdwf) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2026-78252](https://www.cve.org/CVERecord?id=CVE-2026-78252) - Cross-site Scripting issue in Markdown JSON table renderer impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, an authenticated user could have induced a targeted user to perform unintended state-changing HTTP requests due to improper sanitization of user-controlled data in the Markdown JSON table renderer.

**Impacted Versions:** GitLab CE/EE: all versions from 15.3 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 8.2 ([`CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:L`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:L))

Thanks [a_m_a_m](https://hackerone.com/a_m_a_m) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2026-13210](https://www.cve.org/CVERecord?id=CVE-2026-13210) - Incorrect Authorization issue in CI/CD environment variable scope matcher impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, could have allowed an authenticated user to access CI/CD variables outside their intended environment scope due to improper input validation in the environment scope pattern matcher.

**Impacted Versions:** GitLab CE/EE: all versions from 15.7 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 7.7 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N))

Thanks [nwicks](https://hackerone.com/nwicks) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2025-14871](https://www.cve.org/CVERecord?id=CVE-2025-14871) - Denial of Service issue in GraphQL complexity limiter impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, could have allowed an unauthenticated user to cause denial of service due to improper resource allocation limits in the GraphQL complexity calculation logic.

**Impacted Versions:** GitLab CE/EE: all versions from 18.4.6 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 7.5 ([`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H))

Thanks [hunter0xp7](https://hackerone.com/hunter0xp7) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2026-1168](https://www.cve.org/CVERecord?id=CVE-2026-1168) - Denial of Service issue in GraphQL complexity limiter impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, could have allowed an unauthenticated user to cause denial of service due to improper resource allocation limits in the GraphQL complexity calculation logic.

**Impacted Versions:** GitLab CE/EE: all versions from 18.4.6 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 7.5 ([`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H))

Thanks [joaxcar](https://hackerone.com/joaxcar) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2024-11222](https://www.cve.org/CVERecord?id=CVE-2024-11222) - Race Condition issue in Merge Request Pipelines impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, could have allowed a developer user to perform actions in the context of another user’s merge request commit due to a race condition issue in pipeline creation.

**Impacted Versions:** GitLab CE/EE: all versions from 13.0 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 6.4 ([`CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N))

Thanks [xorz](https://hackerone.com/xorz) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2026-12910](https://www.cve.org/CVERecord?id=CVE-2026-12910) - Improper Authentication issue in SAML SSO sign-in restriction enforcement impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, could have allowed an authenticated user to bypass SAML SSO sign-in restrictions and authenticate without SSO due to missing authentication enforcement checks.

**Impacted Versions:** GitLab CE/EE: all versions from 18.6 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 5.4 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N))

Thanks [theluci](https://hackerone.com/theluci) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2026-82837](https://www.cve.org/CVERecord?id=CVE-2026-82837) - Insufficiently Protected Credentials issue in Workhorse senddata emitters impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, could have allowed an authenticated user to access sensitive credentials and tokens without transiting the expected proxy due to improper authorization checks on internal data emission endpoints.

**Impacted Versions:** GitLab CE/EE: all versions from 10.1.0 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 5.3 ([`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N))

Thanks [0xoroot](https://hackerone.com/0xoroot) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2026-19619](https://www.cve.org/CVERecord?id=CVE-2026-19619) - Cross-site Scripting issue in Content Editor impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, could have allowed an unauthenticated user to execute arbitrary JavaScript in the context of a targeted user’s session due to improper sanitization of pasted HTML content in the Content Editor.

**Impacted Versions:** GitLab CE/EE: all versions from 19.0 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 4.7 ([`CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:L/I:L/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:L/I:L/A:N))

Thanks [lucvs](https://hackerone.com/lucvs) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2026-86341](https://www.cve.org/CVERecord?id=CVE-2026-86341) - Access Control Implementation issue in protected environment approval rules impacts GitLab EE

GitLab has remediated an issue that, under certain conditions, an authenticated user with Owner or Maintainer permissions could have silently disabled protected environment deployment approval requirements, allowing unapproved deployments to reach production due to improper access control checks performed after the protected resource was modified.

**Impacted Versions:** GitLab EE: all versions from 17.1 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 4.4 ([`CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:N/I:H/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:N/I:H/A:N))

This vulnerability has been discovered internally by GitLab team member Peter Arts.

### [CVE-2026-86340](https://www.cve.org/CVERecord?id=CVE-2026-86340) - Authorization Bypass issue in protected environment approval rules impacts GitLab EE

GitLab has remediated an issue that, under certain conditions, could allow an authenticated user to bypass required deployment approvals for protected environments by deleting the sole approver group or user account.

**Impacted Versions:** GitLab EE: all versions from 17.1 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 4.4 ([`CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:N/I:H/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:N/I:H/A:N))

This vulnerability has been discovered internally by GitLab team member Peter Arts.

### [CVE-2026-7514](https://www.cve.org/CVERecord?id=CVE-2026-7514) - Missing Authorization issue in Generic Package Registry impacts GitLab CE/EE

GitLab has remediated an issue that an authenticated user with developer-role permissions could substitute package file content and hide packages from their owners due to improper authorization checks in the Generic Package Registry.

**Impacted Versions:** GitLab CE/EE: all versions from 13.9 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 4.3 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N))

Thanks [toofikz](https://hackerone.com/toofikz) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2026-8030](https://www.cve.org/CVERecord?id=CVE-2026-8030) - Improper Input Validation issue in Namespace Transfer impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, could have allowed an authenticated user to prevent another user from modifying their group settings due to improper validation of group URL slugs during namespace transfers.

**Impacted Versions:** GitLab CE/EE: all versions from 13.0 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 4.3 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L))

Thanks [mateuszek](https://hackerone.com/mateuszek) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2026-16794](https://www.cve.org/CVERecord?id=CVE-2026-16794) - Missing Authorization issue in Compliance Framework management impacts GitLab EE

GitLab has remediated an issue that, under certain conditions, could have allowed an authenticated user with the Security Manager role to execute arbitrary CI/CD jobs and access protected variables within group projects due to improper authorization controls on compliance framework management.

**Impacted Versions:** GitLab EE: all versions from 18.11 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 4.3 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N))

Thanks [manual_mint](https://hackerone.com/manual_mint) for reporting this vulnerability through our HackerOne bug bounty program.

### [CVE-2026-3855](https://www.cve.org/CVERecord?id=CVE-2026-3855) - Improper Input Validation issue in Terraform State API impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, could have allowed an authenticated user with project-level permissions to access restricted file contents on the server or cause denial of service due to improper validation of parameters in the Terraform state upload functionality.

**Impacted Versions:** GitLab CE/EE: all versions from 18.2.7 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2**CVSS** 3.1 ([`CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:N/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:N/A:N))

Thanks [ahacker1](https://hackerone.com/ahacker1) for reporting this vulnerability through our HackerOne bug bounty program.

## Bug fixes

### 19.3.2

### 19.2.6

### 19.1.8

## Important notes on upgrading

This patch includes database migrations that may impact your upgrade process.

### Impact on your installation:

- **Single-node instances** : This patch will cause downtime during the upgrade as migrations must complete before GitLab can start.
- **Multi-node instances** : With proper[zero-downtime upgrade procedures](https://docs.gitlab.com/update/zero_downtime/) , this patch can be applied without downtime.

### Post-deploy migrations

The following versions include post-deploy migrations that can run after the upgrade:

- 19.3.2

To learn more about the impact of upgrades on your installation, see:

- [Zero-downtime upgrades](https://docs.gitlab.com/update/zero_downtime/) for multi-node deployments
- [Standard upgrades](https://docs.gitlab.com/update/with_downtime/) for single-node installations

## Updating

To update GitLab, see the [Update page](https://about.gitlab.com/update).
To update GitLab Runner, see the [Updating the Runner page](https://docs.gitlab.com/runner/install/linux-repository.html#updating-the-runner).

## Receive Patch Notifications

To receive patch blog notifications delivered to your inbox, visit our [contact us](https://about.gitlab.com/company/contact/) page.
To receive release notifications via RSS, subscribe to our [patch release RSS feed](https://docs.gitlab.com/releases/patch-releases.xml) or our [RSS feed for all releases](https://about.gitlab.com/all-releases.xml).
