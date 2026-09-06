# extract: served via trafilatura-direct
---
title: Critical Security Issue Affecting TeamCity On-Premises (CVE-2026-63077) – Update to 2025.11.7 or 2026.1.3 Now - The JetBrains Blog
author: Dmitrii Korovin
url: https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/
hostname: jetbrains.com
description: "August 7, 2026 update: Please also see this follow-up blog post for additional guidance. Summary A critical security vulnerability has been identified in TeamCity On-Premises and assigned the C"
sitename: The JetBrains Blog
date: "2026-08-07"
categories: ['News']
tags: ['News', 'security']
---

## TeamCity

Powerful CI/CD for DevOps-centric teams

[News](https://blog.jetbrains.com/teamcity/category/news/)

[Security](https://blog.jetbrains.com/teamcity/category/security/)

# Critical Security Issue Affecting TeamCity On-Premises (CVE-2026-63077) – Update to 2025.11.7 or 2026.1.3 Now

**August 7, 2026 update:** Please also see [this follow-up blog post](https://blog.jetbrains.com/teamcity/2026/08/cve-2026-63077-update/) for additional guidance.

## Summary

- A critical security vulnerability has been identified in TeamCity On-Premises and assigned the Common Vulnerabilities and Exposures (CVE) identifier CVE-2026-63077.
- If exploited, this vulnerability may allow an unauthenticated attacker with HTTP(S) access to a TeamCity server to bypass authentication checks and execute arbitrary operating system commands.
- This vulnerability affects all TeamCity On-Premises versions.
- The issue has been fixed in versions 2025.11.7 and 2026.1.3.
- We strongly recommend that all users update their servers to one of the above versions.
- For those who are unable to do so, we have released a security patch plugin.
- TeamCity Cloud customers are not required to take any action.

## Details

A critical security vulnerability has been identified in TeamCity On-Premises. If exploited, this flaw may enable an unauthenticated attacker with HTTP(S) access to a TeamCity server to bypass authentication checks and execute arbitrary operating system commands with the privileges of the TeamCity server process.

All versions of TeamCity On-Premises are affected. TeamCity Cloud customers are not required to take any action, as the necessary measures have already been applied. We have verified that there is no evidence of TeamCity Cloud environments being exploited through this vulnerability.

This unauthenticated remote code execution vulnerability was reported to us privately on July 10, 2026, by Antoni Tremblay in accordance with our coordinated disclosure policy.

This vulnerability has been assigned the Common Vulnerabilities and Exposures (CVE) identifier CVE-2026-63077.

A fix for this vulnerability has been introduced in versions 2025.11.7 and 2026.1.3. We have also released a security patch plugin for 2017.1+ so that customers who are unable to upgrade can still patch their environments.

### Mitigation option 1: Update your server to 2025.11.7 or 2026.1.3

To update your TeamCity server, [download and install](https://www.jetbrains.com/teamcity/download/other.html) the latest patched version (2025.11.7 or 2026.1.3) or use the [automatic update](https://www.jetbrains.com/help/teamcity/upgrading-teamcity-server-and-agents.html#Automatic+Update) option within TeamCity. These versions include a fix for CVE-2026-63077.

### Mitigation option 2: Apply the security patch plugin

If you are unable to update your server to version 2025.11.7 or 2026.1.3, we have also released a security patch plugin that can be installed on TeamCity 2017.1+ and will patch the specific vulnerability described above.

To get the security patch plugin:

- [Download and install](https://download.jetbrains.com/teamcity/plugins/internal/fix_CVE_2026_63077.zip) it manually.
- For TeamCity 2024.03 and newer, TeamCity automatically downloads available security patch plugins and notifies administrators (if notifications are configured). You can review and apply pending security patches from *Administration* |*Updates* , under*Available security updates* .

For TeamCity 2017.1 to 2018.1, a server restart is required after installing the security patch plugin. Starting from TeamCity 2018.2, you can enable the plugin without restarting the TeamCity server.

See the [TeamCity plugin installation instructions](https://www.jetbrains.com/help/teamcity/installing-additional-plugins.html#Installing+Plugin+via+Web+UI) for more information.

**Important:** The security patch plugin will address only the vulnerability described above (CVE-2026-63077). We always recommend upgrading your server to the latest version to benefit from many other security updates.

## Best practices

As a longer-term security best practice for internet-facing TeamCity servers (those accessible to external users who can reach the TeamCity login screen), consider requiring VPN connections or implementing an additional security layer to help prevent unauthorized access. Even exposing the TeamCity login screen or REST API can provide attackers with potential entry points to exploit newly disclosed vulnerabilities.

## Technical details

This vulnerability affects TeamCity servers that are reachable over HTTP(S).

Exploitation of this vulnerability does not require authentication. An unauthenticated attacker could exploit the vulnerability via the TeamCity agent polling protocol to bypass authentication checks and execute arbitrary operating system commands with the privileges of the TeamCity server process.

Depending on the privileges granted to the TeamCity server process, a successful attack could expose TeamCity data, configurations, and stored credentials, modify server state, and potentially compromise the integrity of build artifacts and downstream CI/CD pipelines.

At the time of publishing this advisory, we are not aware of any active exploitation of this vulnerability.

As a general best practice, we strongly recommend limiting network access to TeamCity servers to trusted networks wherever possible. We also recommend running the TeamCity server with the minimum operating system privileges required for normal operation.

TeamCity servers should also run on dedicated hosts separate from build agents, as described in [our documentation](https://www.jetbrains.com/help/teamcity/install-and-start-teamcity-agents.html).

## Support

If you have any questions about this issue or encounter problems updating your server or installing the security patch plugin, please contact the TeamCity Support team by [submitting a ticket](https://teamcity-support.jetbrains.com/hc/en-us/requests/new?ticket_form_id=66621).


*Prev post*What’s Next for TeamCity – CI/CD by JetBrains
[TeamCity 2026.1.3 and 2025.11.7 Are Now Available](https://blog.jetbrains.com/teamcity/2026/07/teamcity-2026-1-3-2025-11-7-bugfix/)

*Next post*
#### Subscribe to TeamCity Blog updates
