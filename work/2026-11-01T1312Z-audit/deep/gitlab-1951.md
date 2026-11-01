# extract: served via trafilatura-direct
---
title: "GitLab Critical Patch Release: 19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10, 18.11.13"
author: Félix Veillette-Potvin
url: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/
hostname: gitlab.com
description: "Learn more about GitLab Critical Patch Release: 19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10, 18.11.13 for GitLab Community Edition (CE) and Enterprise Edition (EE)."
sitename: GitLab Docs
date: "2013-11-18"
fingerprint: f666eddecb094c8a
license: CC BY-SA 4.0
---
# GitLab Critical Patch Release: 19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10, 18.11.13

On October 21, 2026, we released versions 19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10, 18.11.13 for GitLab Community Edition (CE) and Enterprise Edition (EE).

These versions contain important bug and security fixes, and we strongly recommend that all self-managed GitLab installations be upgraded to one of these versions immediately. GitLab.com is already running the patched version. GitLab Dedicated tenants running 19.3.5-internal0 and 19.4.2-internal0 or later already include these fixes and do not need to take action.

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

### [CVE-2026-110264](https://www.cve.org/CVERecord?id=CVE-2026-110264) - Integer Overflow issue in Regular Expression Compiler impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, could have allowed an unauthenticated user to execute arbitrary code on the GitLab server due to integer overflow when compiling a specially crafted regular expression.

In addition to our standard patch releases, we have backported this fix to GitLab CE/EE versions 18.11.13, 19.0.10, 19.1.9, and 19.2.9.

**Impacted Versions:** GitLab CE/EE: all versions from 7.0 before 18.11.13, 19.0 before 19.0.10, 19.1 before 19.1.9, 19.2 before 19.2.9, 19.3 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1

**CVSS** 10.0 ([`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H))

Thanks [joaxcar](https://hackerone.com/joaxcar) for reporting this vulnerability through our HackerOne bug bounty program

### Detecting [CVE-2026-110264](https://www.cve.org/CVERecord?id=CVE-2026-110264) Exploitation Attempts

GitLab security has released two threat detections to support customers with self-managed instances, listed below. GitLab-managed infrastructure, including GitLab.com and GitLab Dedicated, remains patched.

### [CVE-2026-15723](https://www.cve.org/CVERecord?id=CVE-2026-15723) - Improper Authentication issue in OmniAuth-to-LDAP auto-linking email lookup impacts GitLab CE/EE

GitLab has remediated an issue that, when OmniAuth SAML and LDAP auto-linking were both enabled, an authenticated user could have taken over an existing LDAP-backed account without any interaction from the targeted user, due to improper input sanitization in the LDAP email lookup path used during OmniAuth identity linking.

**Impacted Versions:** GitLab CE/EE: all versions from 10.1 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1

**CVSS** 8.2 ([`CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:N))

Thanks [stealthy](https://hackerone.com/stealthy) for reporting this vulnerability through our HackerOne bug bounty program

### [CVE-2026-112212](https://www.cve.org/CVERecord?id=CVE-2026-112212) - Cache Poisoning issue in OAuth/OIDC discovery endpoints impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, an unauthenticated user could have poisoned a shared cache’s OAuth/OIDC discovery document to redirect certain flows to an externally controlled server, due to improper trust of user-supplied values when constructing endpoint URLs in cached discovery responses.

**Impacted Versions:** GitLab CE/EE: all versions from 18.3 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1

**CVSS** 7.5 ([`CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:L/A:L`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:L/A:L))

This vulnerability has been discovered internally by GitLab team member Peter Arts

### [CVE-2026-12664](https://www.cve.org/CVERecord?id=CVE-2026-12664) - Improper Access Control issue in GraphQL work item email address field impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, could have allowed an authenticated user with a read\_api-scoped token to retrieve a project’s incoming email address and create work items, bypassing the token’s restrictions, due to insufficient scope enforcement on a GraphQL field.

**Impacted Versions:** GitLab CE/EE: all versions from 18.2 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1

**CVSS** 6.8 ([`CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:N))

Thanks [go7f0](https://hackerone.com/go7f0) for reporting this vulnerability through our HackerOne bug bounty program

### [CVE-2026-16255](https://www.cve.org/CVERecord?id=CVE-2026-16255) - Incomplete enforcement of instance-wide SAML/LDAP membership lock allows unauthorized member additions in GitLab EE

GitLab has remediated an issue that, when the instance-wide SAML or LDAP membership lock was enabled, an authenticated user could have granted or accepted project and group membership outside the identity provider’s control, due to incomplete enforcement of the membership lock on requests created before the lock was enabled.

**Impacted Versions:** GitLab EE: all versions from 12.0 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1

**CVSS** 5.9 ([`CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:L/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:L/A:N))

Thanks [3nvz](https://hackerone.com/3nvz) for reporting this vulnerability through our HackerOne bug bounty program

### [CVE-2026-105777](https://www.cve.org/CVERecord?id=CVE-2026-105777) - Internal Credential Exposure issue in internal response headers impacts GitLab CE/EE

GitLab has remediated an issue that, under certain conditions, an unauthenticated user could have retrieved sensitive internal server credentials due to improper filtering of internal response headers.

**Impacted Versions:** GitLab CE/EE: all versions from 17.6.5 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1

**CVSS** 4.3 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N))

Thanks [altair00](https://hackerone.com/altair00) for reporting this vulnerability through our HackerOne bug bounty program

### [CVE-2026-13319](https://www.cve.org/CVERecord?id=CVE-2026-13319) - Authorization Bypass Through User-Controlled Key issue in group milestones API impacts GitLab CE/EE

GitLab has remediated an issue that could have allowed an authenticated user to read milestone metadata, including titles, descriptions, and full project paths, from arbitrary private projects across the instance without any project membership, due to missing authorization checks on a user-supplied project filter parameter in the group milestones API.

**Impacted Versions:** GitLab CE/EE: all versions from 15.10 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1

**CVSS** 4.3 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N))

Thanks [a0xnirudh](https://hackerone.com/a0xnirudh) for reporting this vulnerability through our HackerOne bug bounty program

### [CVE-2026-112378](https://www.cve.org/CVERecord?id=CVE-2026-112378) - Use of Less Trusted Source issue in AI Gateway feature enablement header impacts GitLab EE

GitLab has remediated an issue that under certain conditions could have allowed an authenticated user to access paid AI features without a valid subscription due to insufficient server-side validation in billing eligibility checks.

**Impacted Versions:** GitLab EE: all versions from 17.8 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1

**CVSS** 4.3 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N))

This vulnerability has been discovered internally by GitLab team member Halil Coban

### [CVE-2026-105711](https://www.cve.org/CVERecord?id=CVE-2026-105711) - Use of Cache Containing Sensitive Information issue in merge request title rendering impacts GitLab CE/EE

GitLab has remediated an issue that, when a merge request in a public project referenced a confidential issue from a private project, an authenticated user with no project membership could have read the confidential issue’s title, due to a viewer-independent fragment cache key that incorrectly shared per-user-redacted rendered content across all users.

**Impacted Versions:** GitLab CE/EE: all versions from 15.0 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1

**CVSS** 3.5 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:N/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:N/A:N))

Thanks [20kilograma](https://hackerone.com/20kilograma) for reporting this vulnerability through our HackerOne bug bounty program

### [CVE-2026-14288](https://www.cve.org/CVERecord?id=CVE-2026-14288) - Improper Access Control issue in merge request approval policy enforcement impacts GitLab EE

GitLab has remediated an issue that under certain conditions could have allowed an authenticated user to bypass a required merge request approval policy on a protected branch due to improper access control during approval rule synchronization.

**Impacted Versions:** GitLab EE: all versions from 17.4 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1

**CVSS** 3.1 ([`CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:N))

Thanks [3nvz](https://hackerone.com/3nvz) for reporting this vulnerability through our HackerOne bug bounty program

### [CVE-2026-112326](https://www.cve.org/CVERecord?id=CVE-2026-112326) - Improper Cleanup on Thrown Exception issue in security findings impacts GitLab EE

GitLab has remediated an issue that, under certain conditions, could have allowed an authenticated user with read-only permissions to permanently delete existing vulnerability records due to improper cleanup logic that failed to distinguish between pre-existing records from newly created ones during error handling.

**Impacted Versions:** GitLab EE: all versions from 17.8 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1

**CVSS** 3.1 ([`CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:N))

This vulnerability has been discovered internally by GitLab team member Gregory Havenga

### [CVE-2026-103515](https://www.cve.org/CVERecord?id=CVE-2026-103515) - Improper Access Control issue in group Duo admin-lock enforcement for Amazon Q settings impacts GitLab EE

GitLab has remediated an issue that, when an instance administrator locked a group’s Duo availability, an authenticated user with group Owner permissions could have re-enabled AI-backed data egress to a third-party service for that group and its descendant projects, due to insufficient granularity of the admin-lock enforcement controls.

**Impacted Versions:** GitLab EE: all versions from 19.2 before 19.3.6, 19.4 before 19.4.3, and 19.5 before 19.5.1

**CVSS** 2.7 ([`CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:L/A:N))

Thanks [3nvz](https://hackerone.com/3nvz) for reporting this vulnerability through our HackerOne bug bounty program

## Bug fixes

### 19.5.1

### 19.4.3

### 19.3.6

### 19.2.9

### 19.1.9

### 19.0.10

- [Increase staging and production upload timeout from 35m to 60m](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/9816)
- [\[19.0\] Add Ruby regexp repeat-range double-free patch for 3.3 and 3.4](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3169)
- [\[19.0\] Add Ruby regexp repeat-range double-free patch for 3.3 and 3.4](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/9926)
- [\[19.0\] Update gitlab-markup to 2.2.0 and rdoc to 8.1.0](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/262719)

### 18.11.13

- [Increase staging and production upload timeout from 35m to 60m](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/9815)
- [Mattermost Security Updates August 13, 2026](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/9799)
- [\[18.11\] Add Ruby regexp repeat-range double-free patch for 3.3 and 3.4](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/9940)
- [\[18.11\] Add Ruby regexp repeat-range double-free patch for 3.3 and 3.4](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3181)

## Important notes on upgrading

This patch includes database migrations that may impact your upgrade process.

### Impact on your installation:

- **Single-node instances**: This patch will cause downtime during the upgrade as migrations must complete before GitLab can start.
- **Multi-node instances**: With proper [zero-downtime upgrade procedures](https://docs.gitlab.com/update/zero_downtime/), this patch can be applied without downtime.

### Regular migrations

The following versions include regular migrations that run during the upgrade process:

- 19.4.3
- 19.3.6

### Post-deploy migrations

The following versions include post-deploy migrations that can run after the upgrade:

- 19.4.3

To learn more about the impact of upgrades on your installation, see:

- [Zero-downtime upgrades](https://docs.gitlab.com/update/zero_downtime/) for multi-node deployments
- [Standard upgrades](https://docs.gitlab.com/update/with_downtime/) for single-node installations

## Updating

To update GitLab, see the [Update page](https://about.gitlab.com/update).
To update GitLab Runner, see the [Updating the Runner page](https://docs.gitlab.com/runner/install/linux-repository.html#updating-the-runner).

## Receive Patch Notifications

To receive patch blog notifications delivered to your inbox, visit our [contact us](https://about.gitlab.com/company/contact/) page.
To receive release notifications via RSS, subscribe to our [patch release RSS feed](https://docs.gitlab.com/releases/patch-releases.xml) or our [RSS feed for all releases](https://about.gitlab.com/all-releases.xml).
