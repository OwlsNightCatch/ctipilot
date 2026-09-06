# extract: served via trafilatura-direct
---
title: Attackers Breached JetBrains Cadence via Unpatched TeamCity, Extracting AWS Credentials
author: The Hacker News
url: https://thehackernews.com/2026/09/attackers-breached-jetbrains-cadence.html
hostname: thehackernews.com
description: Attackers exploited CVE-2026-63077 to breach JetBrains Cadence, accessing a 2024 backup containing credentials and user data.
sitename: The Hacker News
date: "2026-09-05"
categories: ['Article']
---
JetBrains is urging Cadence users to revoke and rotate all credentials following a security incident last month in which unidentified threat actors exploited a recently disclosed critical vulnerability in TeamCity to breach its own environment.

"Cadence users should immediately revoke or rotate all credentials and secrets that may have been used to run their Cadence executions," JetBrains [said](https://blog.jetbrains.com/pycharm/2026/08/cadence-security-incident-august-2026/). "They should also treat all executions, including their inputs and outputs in your Cadence project, as potentially untrusted."

"As the threat actors gained access to the Cadence server, any credentials or secrets stored in Cadence, contained in the compromised backup, or made available to executions on the affected server should be considered compromised and must be revoked or rotated."

[Cadence](https://blog.jetbrains.com/pycharm/2025/06/training-your-ml-models-with-cadence/) is a JetBrains-hosted cloud computing service that integrates with PyCharm via an optional plugin to let developers run machine learning and heavy workloads on cloud GPUs directly from their IDE.

The attack, per the software development company, involved the exploitation of [CVE-2026-63077](https://thehackernews.com/2026/07/critical-teamcity-flaw-could-let.html) (CVSS score: 9.8) to breach the affected Cadence environments. The deserialization of untrusted data vulnerability can permit an unauthenticated attacker with access to a TeamCity server to bypass authentication checks and execute arbitrary operating system commands with the privileges of the TeamCity server process.


The security flaw has since [come under active exploitation](https://thehackernews.com/2026/08/cisa-flags-teamcity-cve-2026-63077-rce.html) in the wild, with the U.S. Cybersecurity and Infrastructure Security Agency (CISA) adding it to the Known Exploited Vulnerabilities (KEV) catalog on August 5, 2026. The exploitation was discovered by JetBrains on August 23, 2026.

In subsequent updates, JetBrains said the threat actor accessed data contained in the Cadence server backup from 2024 and that they obtained unauthorized access that could have allowed them to reach storage containing data associated with current Cadence users, including email addresses, project source code, and credentials.

"This affects the same group of users we previously contacted directly," Daniel Gallo, Solutions Engineering Lead at JetBrains, said. "These findings did not identify any additional affected users. As a precaution, we are treating the data stored there as potentially exposed."

Some of the information the threat actor has been "confirmed" to have accessed or compromised -

- Personal data, including usernames, real names, email addresses, last-login timestamps, and last accessed IP addresses
- A full backup of the Cadence server dating from 2024, which contains credentials, configuration, artifacts, logs, or other data
- Multiple AWS IAM users and associated credentials/secrets used with Cadence extracted from the 20224 backup, including IAM users belonging to JetBrains employees who used the service
- Files stored in S3 buckets within JetBrains AWS accounts used by Cadence

JetBrains also cautioned that the attackers may have accessed source code synchronized from PyCharm projects to the affected server. This covers scenarios where users have relied on PyCharm to upload or synchronize project files for execution in Cadence, meaning the actions could have inadvertently exposed code, credentials, or configurations.

It's not clear who is behind the activity. However, JetBrains said the intrusion took place between August 8 and 24, 2026. The exploited Cadence server ("api.cadence.jetbrains.com") has since been taken offline. The company conceded that the server in question should have been patched as part of its own vulnerability response efforts, but did not share any details as to why this did not happen.

JetBrains has also invalidated all access tokens used by the JetBrains Cadence plugin in PyCharm to connect to Cadence. It has shared the following indicators of compromise -

- Activity occurring from August 8, 2026, onwards, particularly authentication or activity using credentials previously stored in or accessible through Cadence
- 
    IP addresses associated with observed exploitation activity:
    
  - 150.109.230.104
  - 43.153.227.206
  - 62.210.127.48
  - 210.247.242.190
  - 15.235.225.205
  - 152.233.30.18
- Authentication or other activity from unexpected IP addresses or locations
- Unexpected repository clones or downloads, and unexpected commits to repositories
- Changes to repository secrets, webhooks, collaborators, or permissions
- New or modified personal access tokens, API tokens, or SSH keys in external services
- New service accounts created in external services
- Unexpected changes to cloud IAM roles, policies, or permissions
- Unexpected access to cloud storage, including S3 buckets and objects, in services such as AWS and Google Cloud
- Unexpected publication or modification of packages or releases

Besides rotating all credentials, users are being asked to review connected systems for suspicious activity, specifically AWS accounts, S3 buckets, deployment environments, package/container registries, and other systems that are accessible using the revoked credentials, audit source code repositories for any unauthorized changes during the time period, and treat all executions as potentially untrusted.

"The likely consequences of the personal data exposure include an increased risk of targeted phishing, social engineering, impersonation, and other unsolicited or malicious communications using the affected names and email addresses," JetBrains said.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
