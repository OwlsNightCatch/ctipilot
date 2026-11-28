---
title: "GitLab Patch Release: 19.6.2, 19.5.9, 19.4.11, 19.3.10, 19.2.11, 19.1.11, 19.0.12, 18.11.15"
author: Greg Myers
url: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-2-released/
hostname: gitlab.com
description: "Learn more about GitLab Patch Release: 19.6.2, 19.5.9, 19.4.11, 19.3.10, 19.2.11, 19.1.11, 19.0.12, 18.11.15 for GitLab Community Edition (CE) and Enterprise Edition (EE)."
sitename: GitLab Docs
date: "2011-04-19"
fingerprint: f606459adf290c98
license: CC BY-SA 4.0
language: en
pagetype: article
filedate: "2026-11-28"
---
# GitLab Patch Release: 19.6.2, 19.5.9, 19.4.11, 19.3.10, 19.2.11, 19.1.11, 19.0.12, 18.11.15

On November 25, 2026, we released versions 19.6.2, 19.5.9, 19.4.11 for GitLab Community Edition (CE) and Enterprise Edition (EE).

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

### Dependency updates

Recent patches to upstream dependencies bundled with GitLab have been backported or updated for multiple vulnerabilities:

- Git ([CVE-2026-105437](https://www.cve.org/CVERecord?id=CVE-2026-105437)): backported to GitLab versions 19.2.11, 19.1.11, 19.0.12, and 18.11.15 (previously included in [19.5.4, 19.4.6, and 19.3.8](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-4-released/)).
- Ruby ([Ruby security advisory](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/)): backported to GitLab versions 19.3.10, 19.2.11, 19.1.11, 19.0.12, and 18.11.15 (previously included in [19.6.1, 19.5.8, and 19.4.10](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-1-released/)).
- GitLab has also remediated [CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975), a double free in GPGME, through multiple fixes, all of which are included in GitLab versions 19.6.2, 19.5.9, 19.4.11, 19.3.10, 19.2.11, 19.1.11, 19.0.12, and 18.11.15:
  - The GPGME library bundled with GitLab Linux packages has been patched to fix the double free.
  - [Ruby-GPGME](https://rubygems.org/gems/gpgme) (the `gpgme` gem) has been updated to 2.0.27.
  - OpenPGP input is now validated before it is passed to GPGME as an additional mitigation.
- NGINX ([NGINX release notes](https://blog.nginx.org/blog/nginx-1-31-9-stricter-header-parsing-flood-detection-for-chunked-request-bodies-and-protocol-fixes-for-http-2-and-http-3)): updated to 1.31.9 in the Linux package (Omnibus) and GitLab Docker images built from the package in versions 19.6.2, 19.5.9, and 19.4.11.
**Please note**: GitLab Helm Chart and GitLab Operator installations using the deprecated NGINX Ingress controller are also affected. This controller is deprecated and has been disabled by default since 19.0. The upstream NGINX Ingress no longer receives security patches so we strongly recommend migrating to Envoy Gateway or an external Ingress controller. An updated NGINX controller will ship in an upcoming chart release.

Extended backports are an exception and do not reflect our standard [maintenance policy](https://docs.gitlab.com/policy/maintenance/).

### Table of security fixes

### [CVE-2026-119452](https://www.cve.org/CVERecord?id=CVE-2026-119452) - Exposure of Sensitive Information issue in dependency proxy authentication impacts GitLab CE/EE

GitLab has remediated an issue that under certain conditions could have allowed an authenticated user with Maintainer-role permissions to obtain another user’s authenticated session cookie and gain unauthorized access to that user’s account due to improper session storage handling in the dependency proxy authentication flow when a redirect-pending state was triggered.

**Impacted Versions:** GitLab CE/EE: all versions from 13.7.0 before 19.4.11, 19.5 before 19.5.9, and 19.6 before 19.6.2

**CVSS** 6.7 ([`CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:L`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:L))

Thanks [jc314159](https://hackerone.com/jc314159) for reporting this vulnerability through our HackerOne bug bounty program

### [CVE-2026-132156](https://www.cve.org/CVERecord?id=CVE-2026-132156) - Improper Validation of Specified Quantity in Input issue in on-call rotation length API impacts GitLab EE

GitLab has remediated an issue that under certain conditions could have allowed an authenticated user with Maintainer-role permissions to cause denial of service due to missing server-side input validation on on-call rotation values.

**Impacted Versions:** GitLab EE: all versions from 13.8 before 19.4.11, 19.5 before 19.5.9, and 19.6 before 19.6.2

**CVSS** 6.5 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H))

This vulnerability has been discovered internally by GitLab team member Daniele Rossetti

### [CVE-2026-132822](https://www.cve.org/CVERecord?id=CVE-2026-132822) - Allocation of Resources Without Limits or Throttling issue in Sentry error tracking client impacts GitLab CE/EE

GitLab has remediated an issue that under certain conditions could have allowed an authenticated user with Maintainer-role permissions to cause denial of service due to missing resource limits in the error tracking integration.

**Impacted Versions:** GitLab CE/EE: all versions from 11.7 before 19.4.11, 19.5 before 19.5.9, and 19.6 before 19.6.2

**CVSS** 6.5 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H))

This vulnerability has been discovered internally by GitLab team member Daniele Rossetti

### [CVE-2026-81336](https://www.cve.org/CVERecord?id=CVE-2026-81336) - Improper Neutralization of Special Elements issue in Service Desk quick action redaction impacts GitLab CE/EE

GitLab has remediated an issue that could have allowed an unauthenticated user to execute quick actions through Service Desk emails due to improper input sanitization.

**Impacted Versions:** GitLab CE/EE: all versions from 12.8 before 19.4.11, 19.5 before 19.5.9, and 19.6 before 19.6.2

**CVSS** 6.5 ([`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N))

Thanks [parthshah\_14](https://hackerone.com/parthshah_14) for reporting this vulnerability through our HackerOne bug bounty program

### [CVE-2026-131867](https://www.cve.org/CVERecord?id=CVE-2026-131867) - Exposure of Sensitive Information issue in Work Item REST API CI job token scope validation impacts GitLab CE/EE

GitLab has remediated an issue that on instances with incoming email enabled could have allowed an authenticated user with CI job access to obtain sensitive information belonging to another user due to improper scope validation.

**Impacted Versions:** GitLab CE/EE: all versions from 19.0 before 19.4.11, 19.5 before 19.5.9, and 19.6 before 19.6.2

**CVSS** 6.3 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:L/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:L/A:N))

This vulnerability has been discovered internally by GitLab team member Tetiana Chupryna

### [CVE-2026-135221](https://www.cve.org/CVERecord?id=CVE-2026-135221) - Server-Side Request Forgery issue in MCP server OAuth token endpoint handler impacts GitLab EE

GitLab has remediated an issue that under certain conditions could have allowed an authenticated user to perform server-side request forgery against internal network resources due to insufficient URL validation in MCP server OAuth handling.

**Impacted Versions:** GitLab EE: all versions from 18.10 before 19.4.11, 19.5 before 19.5.9, and 19.6 before 19.6.2

**CVSS** 6.3 ([`CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N))

This vulnerability has been discovered internally by GitLab team member Gunnar Andrews

### [CVE-2026-17194](https://www.cve.org/CVERecord?id=CVE-2026-17194) - Use of Weak Hash issue in merge request approval reset mechanism impacts GitLab CE/EE

GitLab has remediated an issue that under certain conditions could have allowed an authenticated user with developer-role permissions to merge code changes into protected branches without triggering approval resets due to the use of a weak hash function in the merge request approval change detection mechanism.

**Impacted Versions:** GitLab CE/EE: all versions from 16.7.0 before 19.4.11, 19.5 before 19.5.9, and 19.6 before 19.6.2

**CVSS** 5.7 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:H/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:H/A:N))

Thanks [secundumkid](https://hackerone.com/secundumkid) for reporting this vulnerability through our HackerOne bug bounty program

### [CVE-2026-132102](https://www.cve.org/CVERecord?id=CVE-2026-132102) - Inefficient Regular Expression Complexity issue in dependency proxy route matching middleware impacts GitLab CE/EE

GitLab has remediated an issue that under certain conditions could have allowed an unauthenticated user to cause denial of service due to unconstrained backtracking in regular expression evaluation.

**Impacted Versions:** GitLab CE/EE: all versions from 14.4 before 19.4.11, 19.5 before 19.5.9, and 19.6 before 19.6.2

**CVSS** 5.3 ([`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L))

This vulnerability has been discovered internally by GitLab team member David Fernandez

### [CVE-2026-16744](https://www.cve.org/CVERecord?id=CVE-2026-16744) - Server-Side Request Forgery issue in cluster agent URL configuration validator impacts GitLab EE

GitLab has remediated an issue that on instances with receptive cluster agents enabled could have allowed an authenticated user with Maintainer-role permissions to make requests to internal network services through the GitLab agent server due to insufficient validation of destination addresses.

**Impacted Versions:** GitLab EE: all versions from 17.4 before 19.4.11, 19.5 before 19.5.9, and 19.6 before 19.6.2

**CVSS** 5.0 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:N))

Thanks [lucasfutures](https://hackerone.com/lucasfutures) for reporting this vulnerability through our HackerOne bug bounty program

### [CVE-2026-107633](https://www.cve.org/CVERecord?id=CVE-2026-107633) - Incorrect Authorization issue in merge request approval policy enforcement impacts GitLab EE

GitLab has remediated an issue that under certain conditions could have allowed an authenticated user with developer-role permissions to self-approve their own merge request and merge code into protected branches due to incorrect authorization when a security policy prohibited author self-approval.

**Impacted Versions:** GitLab EE: all versions from 18.11 before 19.4.11, 19.5 before 19.5.9, and 19.6 before 19.6.2

**CVSS** 4.3 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N))

Thanks [rogerace](https://hackerone.com/rogerace) for reporting this vulnerability through our HackerOne bug bounty program

### [CVE-2026-132794](https://www.cve.org/CVERecord?id=CVE-2026-132794) - Incorrect Authorization issue in work items API impacts GitLab CE/EE

GitLab has remediated an issue that under certain conditions could have allowed an authenticated user with a fine-grained personal access token to read work items in projects or groups they have access to but that were not granted to the token due to incorrect authorization checks.

**Impacted Versions:** GitLab CE/EE: all versions from 18.10 before 19.4.11, 19.5 before 19.5.9, and 19.6 before 19.6.2

**CVSS** 4.3 ([`CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N))

This vulnerability has been discovered internally by GitLab team member Tetiana Chupryna

### [CVE-2026-129982](https://www.cve.org/CVERecord?id=CVE-2026-129982) - Incorrect Authorization issue in batch suggestion apply API impacts GitLab CE/EE

GitLab has remediated an issue that under certain conditions could have allowed an authenticated user with a fine-grained personal access token to read and apply merge request suggestions from projects outside the token’s scope due to incorrect authorization checks.

**Impacted Versions:** GitLab CE/EE: all versions from 19.2 before 19.4.11, 19.5 before 19.5.9, and 19.6 before 19.6.2

**CVSS** 4.2 ([`CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:N))

Thanks [jamstone](https://hackerone.com/jamstone) for reporting this vulnerability through our HackerOne bug bounty program

### [CVE-2026-135636](https://www.cve.org/CVERecord?id=CVE-2026-135636) - Server-Side Request Forgery (SSRF) issue in remote Git endpoint validation impacts GitLab CE/EE

GitLab has remediated an issue that under certain conditions could have allowed an authenticated user to send requests to internal network resources due to insufficient validation in repository import.

**Impacted Versions:** GitLab CE/EE: all versions from 18.0 before 19.4.11, 19.5 before 19.5.9, and 19.6 before 19.6.2

**CVSS** 3.5 ([`CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:L/I:N/A:N`](https://gitlab-com.gitlab.io/gl-security/product-security/appsec/cvss-calculator/explain#explain=CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:L/I:N/A:N))

Thanks [anhiu102](https://hackerone.com/anhiu102) for reporting this vulnerability through our HackerOne bug bounty program

## Bug fixes

### 19.6.2

- [Backport of ‘Add workflow rules to the generated gems child pipeline’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272811)
- [Backport of ‘Add 19.6 upgrade note for new rate limits and resource limits’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272741)
- [Backport of ‘Default `discussions_resolve_limit` to 0’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272101)
- [Backport of ‘Log nested counted\_by values as strings’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/273027)
- [Backport of ‘Drop detached ai\_events\_counts partitions before the table’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/273555)
- Bump NGINX to 1.31.9 in the Linux package and Docker images ([NGINX release notes](https://blog.nginx.org/blog/nginx-1-31-9-stricter-header-parsing-flood-detection-for-chunked-request-bodies-and-protocol-fixes-for-http-2-and-http-3)). For Helm chart installations, see [Dependency updates](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-2-released/#dependency-updates).
- Bump gpgme gem to 2.0.27 ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))

### 19.5.9

- [\[19.5\] Restore Ruby 3.3.12 regexp patches](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3325)
- [\[19.5\] Bump GITLAB\_CNG\_MIRROR\_REF to restore Ruby 3.3.12 patches](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272689)
- [Backport of ‘Add an optional runner tag for the buildx assets jobs’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272799)
- [Backport ActiveSupport safe\_constantize fix to 19.5](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272155)
- [Backport of ‘Fix group transfer failing and wedging on 2FA’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/271390)
- [Backport of ‘Count CI job token Git requests against the user’s rate limit’ to 19.5](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272433)
- [Backport of ‘Log nested counted\_by values as strings’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/273028)
- [Backport of ‘Show Ask GitLab Duo in Orbit Quickstart after a turn-on’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272984)
- [Backport 19.5 - Bump Postgres to 18.7, 17.12](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10107)
- [\[19.5\] Stop marking the smartcard NGINX server as default\_server](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10127)
- Bump NGINX to 1.31.9 in the Linux package and Docker images ([NGINX release notes](https://blog.nginx.org/blog/nginx-1-31-9-stricter-header-parsing-flood-detection-for-chunked-request-bodies-and-protocol-fixes-for-http-2-and-http-3)). For Helm chart installations, see [Dependency updates](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-2-released/#dependency-updates).
- Bump gpgme gem to 2.0.27 ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))

### 19.4.11

- [\[19.4\] Restore Ruby 3.3.12 regexp patches](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3326)
- [\[19.4\] Bump GITLAB\_CNG\_MIRROR\_REF to restore Ruby 3.3.12 patches](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272688)
- [Backport ActiveSupport safe\_constantize fix to 19.4](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272156)
- [Backport of ‘Count CI job token Git requests against the user’s rate limit’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272160)
- [Backport of ‘Add an optional runner tag for the buildx assets jobs’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272798)
- [Backport of ‘Fix group transfer failing and wedging on 2FA’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/271391)
- [Backport of ‘Log nested counted\_by values as strings’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/273029)
- [Backport of ‘Show Ask GitLab Duo in Orbit Quickstart after a turn-on’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272985)
- [Backport 19.4 - Bump Postgres to 18.7, 17.12](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10108)
- [\[19.4\] Stop marking the smartcard NGINX server as default\_server](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10128)
- Bump NGINX to 1.31.9 in the Linux package and Docker images ([NGINX release notes](https://blog.nginx.org/blog/nginx-1-31-9-stricter-header-parsing-flood-detection-for-chunked-request-bodies-and-protocol-fixes-for-http-2-and-http-3)). For Helm chart installations, see [Dependency updates](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-2-released/#dependency-updates).
- Bump gpgme gem to 2.0.27 ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))

### 19.3.10

- [\[19.3\] Restore Ruby 3.3.12 regexp patches](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3336)
- [\[19.3\] Bump Ruby to 3.3.14](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3313)
- [\[19.3\] Bump GITLAB\_CNG\_MIRROR\_REF to apply Ruby regexp patches](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272732)
- [Backport of ‘Add an optional runner tag for the buildx assets jobs’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272797)
- [Backport 19.3 - Bump Postgres to 18.7, 17.12](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10109)
- [Backport: Publish the Pulp repository if the uploaded RPM is not published (19-3)](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10116)
- [\[19.3\] Bump Ruby to 3.3.14 and 3.4.13](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10134) ([Ruby security advisory](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/))
- Validate OpenPGP input before passing it to GPGME ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))
- \[19.3\] Backport of ‘Patch gpgme to fix double free in the gpg engine’ ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))
- Bump gpgme gem to 2.0.27 ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))

### 19.2.11

- [\[19.2\] Update danger-review component to 2.2.0](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3243)
- [\[19.2\] Move Ruby regexp patches to the 3.3.11 directory](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3335)
- [\[19.2\] Bump Ruby to 3.3.14](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3314)
- [Makefile: Upgrade Git for 2.56.1 security release (v19.2)](https://gitlab.com/gitlab-org/gitaly/-/merge_requests/9588)
- [Backport of ‘Bump webauthn gem to 3.4.4’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/269847)
- [\[19.2\] Pin Valkey Helm chart to 0.12.1 in orchestrator](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/271037)
- [\[19.2\] Bump GITLAB\_CNG\_MIRROR\_REF to apply Ruby regexp patches](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272731)
- [Backport of ‘Add an optional runner tag for the buildx assets jobs’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272796)
- [Backport: Allow skipping the redundant Pulp CLI publish after RPM uploads](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10004)
- [\[19.2\] Build Docker images with Docker media types for Podman](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10028)
- [Backport: Publish the Pulp repository if the uploaded RPM is not published (19-2)](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10117)
- [\[19.2\] Bump Ruby to 3.3.14 and 3.4.13](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10135) ([Ruby security advisory](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/))
- Validate OpenPGP input before passing it to GPGME ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))
- \[19.2\] Backport of ‘Patch gpgme to fix double free in the gpg engine’ ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))
- Bump gpgme gem to 2.0.27 ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))

### 19.1.11

- [\[19.1\] Update danger-review component to 2.2.0](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3244)
- [\[19.1\] Move Ruby regexp patches to the 3.3.11 directory](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3334)
- [\[19.1\] Bump Ruby to 3.3.14](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3315)
- [Makefile: Upgrade Git for 2.56.1 security release (v19.1)](https://gitlab.com/gitlab-org/gitaly/-/merge_requests/9590)
- [\[19.1\] Pin Valkey Helm chart to 0.12.1 in orchestrator](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/271036)
- [Backport of ‘Bump webauthn gem to 3.4.4’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/269866)
- [\[19.1\] Bump GITLAB\_CNG\_MIRROR\_REF to apply Ruby regexp patches](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272730)
- [Backport of ‘Add an optional runner tag for the buildx assets jobs’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272795)
- [Backport: Allow skipping the redundant Pulp CLI publish after RPM uploads](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10005)
- [\[19.1\] Build Docker images with Docker media types for Podman](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10029)
- [Backport: Publish the Pulp repository if the uploaded RPM is not published (19-1)](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10118)
- [\[19.1\] Bump Ruby to 3.3.14 and 3.4.13](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10136) ([Ruby security advisory](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/))
- Validate OpenPGP input before passing it to GPGME ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))
- \[19.1\] Backport of ‘Patch gpgme to fix double free in the gpg engine’ ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))
- Bump gpgme gem to 2.0.27 ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))

### 19.0.12

- [\[19.0\] Update danger-review component to 2.2.0](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3245)
- [\[19.0\] Move Ruby regexp patches to the 3.3.11 directory](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3333)
- [\[19.0\] Bump Ruby to 3.3.14](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3316)
- [Makefile: Upgrade Git for 2.56.1 security release (v19.0)](https://gitlab.com/gitlab-org/gitaly/-/merge_requests/9587)
- [Backport of ‘Bump webauthn gem to 3.4.4’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/269868)
- [\[19.0\] Bump GITLAB\_CNG\_MIRROR\_REF to apply Ruby regexp patches](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272729)
- [Backport of ‘Add an optional runner tag for the buildx assets jobs’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272794)
- [Backport: Allow skipping the redundant Pulp CLI publish after RPM uploads](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10006)
- [\[19.0\] Build Docker images with Docker media types for Podman](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10030)
- [Backport: Publish the Pulp repository if the uploaded RPM is not published (19-0)](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10119)
- [\[19.0\] Bump Ruby to 3.3.14 and 3.4.13](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10137) ([Ruby security advisory](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/))
- Validate OpenPGP input before passing it to GPGME ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))
- \[19.0\] Backport of ‘Patch gpgme to fix double free in the gpg engine’ ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))
- Bump gpgme gem to 2.0.27 ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))

### 18.11.15

- [\[18.11\] Update danger-review component to 2.2.0](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3246)
- [\[18.11\] Move Ruby regexp patches to the 3.3.10 directory](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3332)
- [\[18.11\] Bump Ruby to 3.3.14](https://gitlab.com/gitlab-org/build/CNG/-/merge_requests/3317)
- [Makefile: Upgrade Git for 2.56.1 security release (v18.11)](https://gitlab.com/gitlab-org/gitaly/-/merge_requests/9586)
- [\[18.11\] Use the system CA bundle for gRPC default roots](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/265708)
- [Backport of ‘Bump webauthn gem to 3.4.4’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/269871)
- [\[18.11\] Bump GITLAB\_CNG\_MIRROR\_REF to apply Ruby regexp patches](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272728)
- [Backport of ‘Add an optional runner tag for the buildx assets jobs’](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/272793)
- [Backport: Allow skipping the redundant Pulp CLI publish after RPM uploads](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10007)
- [\[18.11\] Build Docker images with Docker media types for Podman](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10031)
- [Backport: Publish the Pulp repository if the uploaded RPM is not published (18-11)](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10120)
- [\[18.11\] Bump Ruby to 3.3.14 and 3.4.13](https://gitlab.com/gitlab-org/omnibus-gitlab/-/merge_requests/10138) ([Ruby security advisory](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/))
- Validate OpenPGP input before passing it to GPGME ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))
- \[18.11\] Backport of ‘Patch gpgme to fix double free in the gpg engine’ ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))
- Bump gpgme gem to 2.0.27 ([CVE-2026-129975](https://www.cve.org/CVERecord?id=CVE-2026-129975))

## Important notes on upgrading

This patch includes database migrations that may impact your upgrade process.

### Impact on your installation:

- **Single-node instances**: This patch will cause downtime during the upgrade as migrations must complete before GitLab can start.
- **Multi-node instances**: With proper [zero-downtime upgrade procedures](https://docs.gitlab.com/update/zero_downtime/), this patch can be applied without downtime.

### Post-deploy migrations

The following versions include post-deploy migrations that can run after the upgrade:

- 19.6.2

To learn more about the impact of upgrades on your installation, see:

- [Zero-downtime upgrades](https://docs.gitlab.com/update/zero_downtime/) for multi-node deployments
- [Standard upgrades](https://docs.gitlab.com/update/with_downtime/) for single-node installations

## Updating

To update GitLab, see the [Update page](https://about.gitlab.com/update).
To update GitLab Runner, see the [Updating the Runner page](https://docs.gitlab.com/runner/install/linux-repository.html#updating-the-runner).

## Receive Patch Notifications

To receive patch blog notifications delivered to your inbox, visit our [contact us](https://about.gitlab.com/company/contact/) page.
To receive release notifications via RSS, subscribe to our [patch release RSS feed](https://docs.gitlab.com/releases/patch-releases.xml) or our [RSS feed for all releases](https://about.gitlab.com/all-releases.xml).
