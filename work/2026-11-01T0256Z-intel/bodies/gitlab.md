---
title: "GitLab Patch Release and Security Update: 19.5.3, 19.4.5, 19.3.7, 19.2.10, 19.1.10, 19.0.11, 18.11.14"
author: Akinyele Cafe-Febrissy
url: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-3-released/
hostname: gitlab.com
description: GitLab releases 19.5.3, 19.4.5, 19.3.7, 19.2.10, 19.1.10, 19.0.11, 18.11.14
sitename: GitLab Docs
date: "2010-01-19"
fingerprint: "76544dbe4819444e"
license: CC BY-SA 4.0
---
# GitLab Patch Release and Security Update: 19.5.3, 19.4.5, 19.3.7, 19.2.10, 19.1.10, 19.0.11, 18.11.14

We have released versions 19.5.3, 19.4.5, 19.3.7, 19.2.10, 19.1.10, 19.0.11, 18.11.14 for GitLab Community Edition (CE) and Enterprise Edition (EE). We [also released version 19.5.1](https://gitlab.com/gitlab-org/gitlab-runner/-/releases/v19.5.1) for GitLab Runner and released versions 18.11.8, 19.0.13, 19.1.9, 19.2.5, 19.3.3, 19.4.3, 19.5.3 for GitLab AI Gateway. GitLab.com is already running the patched version. GitLab Dedicated tenants running 19.4.3-internal0 or later already include these fixes and do not need to take action.

These versions address [CVE-2026-111943](https://www.cve.org/CVERecord?id=CVE-2026-111943), along with additional unrelated bug fixes. We strongly recommend that all self-managed GitLab installations be upgraded to one of these versions. If you use the self-hosted version of Runners or AI Gateway, you must also upgrade those components to the latest versions; guidance is included below. GitLab-hosted infrastructure has already been upgraded.

## **Security update**

### [CVE-2026-111943](https://www.cve.org/CVERecord?id=CVE-2026-111943) - GitLab has removed trust for compromised eMudhra Intermediate CA Certificates for GitLab CE/EE

For GitLab CE/EE, GitLab has removed trust for eight eMudhra intermediate CA certificates whose private keys have been compromised. This release removes trust for those certificates from the certificate stores GitLab ships. For background, see eMudhra’s [public incident write-up](https://emudhra.we-have-a-problem.com/).

**Impacted Versions:** GitLab CE/EE: all versions before 18.11.14, 19.0 before 19.0.11, 19.1 before 19.1.10, 19.2 before 19.2.10, 19.3 before 19.3.7, 19.4 before 19.4.5, and 19.5 before 19.5.3.

**Action required: update Self-Hosted GitLab Runner to version 19.5.1**

Upgrading GitLab does not update GitLab Runner. Runner verifies certificates on its own, so **you must also update GitLab Runner** to [version 19.5.1](https://gitlab.com/gitlab-org/gitlab-runner/-/releases/v19.5.1), and rebuild any CI/CD job images that include their own `ca-certificates` package. To update, see the [Updating the Runner page](https://docs.gitlab.com/runner/install/linux-repository/#upgrade-gitlab-runner).

**Action required: update Self-Hosted GitLab AI Gateway to versions 18.11.8, 19.0.13, 19.1.9, 19.2.5, 19.3.3, 19.4.3, 19.5.3**

Upgrading GitLab does not update the GitLab AI Gateway. AI Gateway verifies certificates on its own, so **you must also update AI Gateway** to versions 18.11.8, 19.0.13, 19.1.9, 19.2.5, 19.3.3, 19.4.3, 19.5.3 or above. To update, see the [AI gateway installation page](https://docs.gitlab.com/install/install_ai_gateway/).

## GitLab Community Edition and Enterprise Edition

### 19.5.3

### 19.4.5

### 19.3.7

### 19.2.10

### 19.1.10

### 19.0.11

### 18.11.14

## Important notes on upgrading

This patch includes database migrations that may impact your upgrade process.

### Impact on your installation

- **Single-node instances**: This patch will cause downtime during the upgrade as migrations must complete before GitLab can start.
- **Multi-node instances**: With proper [zero-downtime upgrade procedures](https://docs.gitlab.com/update/zero_downtime/), this patch can be applied without downtime.

### Regular migrations

The following versions include regular migrations that run during the upgrade process:

- 19.5.3
- 19.4.5

To learn more about the impact of upgrades on your installation, see:

- [Zero-downtime upgrades](https://docs.gitlab.com/update/zero_downtime/) for multi-node deployments
- [Standard upgrades](https://docs.gitlab.com/update/with_downtime/) for single-node installations

## Updating

To update, check out our [update page](https://about.gitlab.com/update/).

GitLab releases have skipped 19.5.2 and 19.4.4. There are no patches with these version numbers.

## GitLab subscriptions

Access to GitLab Premium and Ultimate features is granted by a paid [subscription](https://about.gitlab.com/pricing/).

Alternatively, [sign up for GitLab.com](https://gitlab.com/users/sign_in)
to use GitLab’s own infrastructure.
