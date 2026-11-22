---
title: "GitLab Critical Patch Release: 19.6.1, 19.5.8, 19.4.10"
author: Katherine Wu
url: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-1-released/
hostname: gitlab.com
description: "Learn more about GitLab Critical Patch Release: 19.6.1, 19.5.8, 19.4.10 for GitLab Community Edition (CE) and Enterprise Edition (EE)."
sitename: GitLab Docs
date: "2010-04-19"
fingerprint: f2744df28c15c60e
license: CC BY-SA 4.0
---
# GitLab Critical Patch Release: 19.6.1, 19.5.8, 19.4.10

On November 20, 2026, we released versions 19.6.1, 19.5.8, 19.4.10 for GitLab Community Edition and Enterprise Edition.

These versions contain important bug and security fixes, and we strongly recommend that all self-managed GitLab installations be upgraded to one of these versions immediately. GitLab.com and GitLab Dedicated are already running a patched version. GitLab.com and GitLab Dedicated customers do not need to take action. GitLab Dedicated was previously protected through internal-only releases 19.5.7 and 19.4.9, which contained interim mitigations for these vulnerabilities; all fixes from those releases are also included in 19.5.8 and 19.4.10.

GitLab releases fixes for vulnerabilities in patch releases. There are two types of patch releases:
scheduled releases and ad-hoc critical patches for high-severity vulnerabilities. Scheduled releases are released twice a month on the second and fourth Wednesdays.
For more information, please visit our [releases handbook](https://handbook.gitlab.com/handbook/engineering/releases/) and [security FAQ](https://about.gitlab.com/security/faq/).
You can see all of GitLab release blog posts [here](https://docs.gitlab.com/releases/).

We are committed to ensuring that all aspects of GitLab that are exposed to customers or that host customer data are held to
the highest security standards. To maintain good security hygiene, it is highly recommended that all customers
upgrade to the latest patch release for their supported version. You can read more
[best practices in securing your GitLab instance](https://about.gitlab.com/blog/gitlab-instance-security-best-practices/) in our blog post.

### Recommended Action

We **strongly recommend** that all installations running a version affected by the issues described below are **upgraded to the latest version as soon as possible**.

When no specific deployment type (omnibus, source code, helm chart, etc.) of a product is mentioned, it means all types are affected.

**Important guidance for self-compiled GitLab installations:** The fix for CVE-2026-132825 is a patch to Ruby. Official GitLab Linux packages and container images already include the patched Ruby. For self-compiled installations, you must rebuild the Ruby installation used to run GitLab with Ruby 3.3.14 or 3.4.13 (or a later release in the same minor series), which include the fixes for CVE-2026-132825 and the other vulnerabilities disclosed in the [Ruby security advisory](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/), as described in [Ruby](https://docs.gitlab.com/install/self_compiled/#2-ruby).

## Security fixes

### Table of security fixes

| Title | Severity | 
|---|---|
| [CVE-2026-132825 (vulnerability in `ruby`)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-1-released/#cve-2026-132825-vulnerability-in-ruby) | Critical | 

The severity shown reflects the Critical rating assigned by the Ruby security team in [GHSA-34m4-m9fh-gqp5](https://github.com/ruby/ruby/security/advisories/GHSA-34m4-m9fh-gqp5). MITRE rates [CVE-2026-132825](https://nvd.nist.gov/vuln/detail/CVE-2026-132825) as High (CVSS 7.4). As this is a vulnerability in Ruby rather than in GitLab’s own code, the severity is taken from the upstream advisory.

### CVE-2026-132825 (vulnerability in `ruby`)

This release addresses the security issue [CVE-2026-132825](https://www.cve.org/CVERecord?id=CVE-2026-132825) ([GHSA-34m4-m9fh-gqp5](https://github.com/ruby/ruby/security/advisories/GHSA-34m4-m9fh-gqp5)), a heap-based buffer overflow in the case conversion of strings in `ruby`, by updating the version of Ruby bundled with GitLab. This issue has been remediated on GitLab.com, and in GitLab CE/EE versions 19.4.10, 19.5.8, and 19.6.1.

In GitLab, under certain conditions, changing the case of a crafted string can result in an out-of-bounds heap write. The Ruby security team has stated that this flaw may allow remote code execution in some scenarios.

These versions also include fixes for all of the other vulnerabilities disclosed in the Ruby security advisory [Multiple vulnerabilities in Regexp and String](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/).

**Impacted Versions:** GitLab CE/EE: all versions before 19.4.10, 19.5 before 19.5.8, and 19.6 before 19.6.1

## Bug fixes

### 19.6.1

### 19.5.8

### 19.4.10

## Important notes on upgrading

These versions do not include any new migrations, and for multi-node deployments, [should not require any downtime](https://docs.gitlab.com/update/downtime_options/#zero-downtime-upgrades).

Please be aware that by default the Omnibus packages will stop, run migrations,
and start again, no matter how “big” or “small” the upgrade is. This behavior
can be changed by adding a [`/etc/gitlab/skip-auto-reconfigure`](https://docs.gitlab.com/update/zero_downtime/) file,
which is only used for [upgrades](https://docs.gitlab.com/update/).

## Updating

To update, check out our [update page](https://about.gitlab.com/update/).

## GitLab subscriptions

Access to GitLab Premium and Ultimate features is granted by a paid [subscription](https://about.gitlab.com/pricing/).

Alternatively, [sign up for GitLab.com](https://gitlab.com/users/sign_in)
to use GitLab’s own infrastructure.
