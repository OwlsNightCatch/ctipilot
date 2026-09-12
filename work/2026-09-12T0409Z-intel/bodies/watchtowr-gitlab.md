---
title: "Rapid Reaction: GitLab Path Traversal Vulnerability (CVE-2026-85706) | watchTowr"
author: Watchtowr Team
url: https://watchtowr.com/resources/rapid-reaction-gitlab-critical-path-traversal-vulnerability-cve-2026-85706/
hostname: watchtowr.com
description: watchTowr Intel is observing in-the-wild probes for the latest critical GitLab Path Traversal vulnerability, CVE-2026-85706, which allows attackers to read arbitrary files in a single HTTP request.
sitename: Watchtowr
date: "2026-09-11"
categories: ['Rapid Reaction']
tags: ['CVE-2026-85706', 'GitLab', 'Path traversal vulnerability']
---
On September 10, 2026, GitLab released versions 19.3.2, 19.2.6, and 19.1.8 for GitLab Community Edition and Enterprise Edition. The release addresses a critical path traversal vulnerability tracked as CVE-2026-85706, affecting the repository commits API. GitLab assigned this issue a CVSS score of 10.0, and watchTowr assesses with a high confidence that this vulnerability will rapidly transition to indiscriminate, in-the-wild exploitation given the low complexity of exploitation.

watchTowr reviewed the technical details published by GitLab, reproduced the vulnerability, and validated exposure across client environments running self-managed GitLab instances. [watchTowr Intel](https://watchtowr.com/platform/watchtowr-intel/) is already seeing behavioral probes for this vulnerability against Attacker Eye, our global honeypot network, meaning attackers have already successfully reverse engineered and reproduced the vulnerability and the countdown to indiscriminate, in-the-wild exploitation is on.

Organizations running self-hosted versions of GitLab should apply patches as a priority. If you need urgent help assessing exposure, contact us here.

## What Is GitLab?

GitLab is a widely deployed DevOps platform used for source code management, CI/CD pipelines, and application security workflows. It is used by enterprises of all sizes to store source code, manage releases, and run build and deployment pipelines. Because GitLab instances often hold sensitive source code, credentials, and CI/CD configuration data, any vulnerability that allows unauthorized file access carries significant risk to enterprise environments.

## What Is the GitLab Path Traversal Vulnerability?

The **GitLab Path Traversal Vulnerability (CVE-2026-85706)** is a path traversal issue in the repository commits API within GitLab CE and EE. According to GitLab, under certain conditions an unauthenticated user could read arbitrary files from the GitLab server. The root cause is improper path confinement combined with missing authentication enforcement in the affected API endpoint.

In practical terms, an attacker with no credentials could send a request to the commits API and have the application return the contents of files it should never have exposed, potentially including configuration files, secrets, or other sensitive server-side data. The lack of any authentication requirement, combined with the low attack complexity, is reflected in the CVSS 10.0 score assigned to this issue.

**What Is Affected**

| Product Name | Affected Versions | 
|---|---|
| GitLab CE/EE | All versions from 18.7 before 19.1.8, 19.2 before 19.2.6, and 19.3 before 19.3.2 | 

## What Should You Do

Organizations with public-facing self-hosted GitLab instances should patch as soon as possible or remove public access.

Defenders should also hunt through log files for HTTP POST requests to “/api/v4/projects/{id}/repository/commits/” URIs containing “file.path” parameters to identify potential exploitation attempts.

1. Identify every self-managed GitLab instance in your environment and confirm the exact version in use.
2. Prioritize patching any instance running an affected version, given the unauthenticated attack path and CVSS 10.0 rating.
3. Review recent access logs on the repository commits API for unusual or unauthenticated requests that may indicate probing or exploitation attempts.
4. Confirm that GitLab.com and GitLab Dedicated deployments require no further action, and document this for audit purposes.
5. Upgrade affected installations to the patched versions listed below as soon as possible.

| Product Name | Patched Version(s) | 
|---|---|
| GitLab CE/EE | 19.1.8, 19.2.6, 19.3.2 | 

## How watchTowr Helps Respond to the GitLab Path Traversal Vulnerability

The watchTowr Platform delivers Preemptive Exposure Management, identifying, validating, and mitigating external exposure across enterprise environments.

- **[watchTowr Instinct](https://watchtowr.com/platform/watchtowr-intel/):** assessed CVE-2026-85706 as high-likelihood for in-the-wild exploitation in real-time as the vulnerability was disclosed.
- [**Project Red:**](https://watchtowr.com/resources/introducing-project-red-autonomous-vulnerability-reproduction/) autonomously reproduced the threat, CVE-2026-85706.
- **[Adversary Sight engine](https://watchtowr.com/platform/attack-surface-visibility/):** identified GitLab instances across client environments and assessed exposure.
- **Attacker Eye:** our global honeypot network, is monitoring for in-the-wild exploitation activity as it emerges.
- **[Rapid Reaction](https://watchtowr.com/platform/rapid-reaction/):** was leveraged across the watchTowr client base to identify exposure to this vulnerability and give teams the time they need to act.
- **[Active Defense](https://watchtowr.com/platform/active-defense/)****:** released targeted network-level mitigations to clients, enabling immediate risk reduction while permanent fixes are applied.

[Request a demo](https://watchtowr.com/demo/)to see how Rapid Reaction protects your environment from emerging threats like this GitLab Critical Path Traversal Vulnerability (CVE-2026-85706).
