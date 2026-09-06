# extract: served via trafilatura-direct
---
title: Security Incident Affecting JetBrains Cadence - The JetBrains Blog
author: Paul Everitt
url: https://blog.jetbrains.com/pycharm/2026/08/cadence-security-incident-august-2026/
hostname: jetbrains.com
description: We are investigating a security incident affecting JetBrains Cadence. Cadence is a JetBrains-hosted service that integrates with PyCharm through an optional plugin, and lets you run your projects on c
sitename: The JetBrains Blog
date: "2026-09-03"
categories: ['News']
tags: ['News', 'security']
---
[News](https://blog.jetbrains.com/pycharm/category/news/)

[Security](https://blog.jetbrains.com/pycharm/category/security/)

# Security Incident Affecting JetBrains Cadence

We are investigating a security incident affecting JetBrains Cadence. Cadence is a JetBrains-hosted service that integrates with PyCharm through an optional plugin, and lets you run your projects on cloud compute resources. Our investigation has confirmed unauthorized access to the service and the exposure of customer data associated with its use.

We have contacted affected users directly and have taken steps to contain the incident.

**This post provides the latest information about the incident, its potential impact, and the actions we recommend Cadence users take. We will update it as our investigation progresses and additional information becomes available.**

**Last updated:** September 3, 2026, 19:00 CEST

## September 3, 2026, 19:00 CEST

Our investigation has identified additional potential exposure involving storage used by the current Cadence environment.

We confirmed that the threat actor obtained access that could have allowed them to reach storage containing data associated with current Cadence users, including email addresses, project source code, and credentials. This affects the same group of users we previously contacted directly. These findings did not identify any additional affected users. As a precaution, we are treating the data stored there as potentially exposed.

Our investigation has now concluded. The recommended actions for affected users remain unchanged.

## September 1, 2026, 12:05 CEST

Our investigation is nearing completion, and most mitigation and response actions are now finalized. We have not identified any additional compromised resources or data since our last update, and we are wrapping up a small number of remaining verification activities. The recommended actions for affected users remain unchanged.

## August 31, 2026, 12:56 CEST

Our investigation remains ongoing. At this time, we have not identified any additional compromised resources or data.

We have confirmed that the threat actor accessed data contained in the Cadence server backup from 2024. At this time, there is no evidence to suggest that the threat actor extracted data, including secrets, from the current Cadence environment.

The recommended actions described below remain unchanged.

## August 28, 2026, 11:50 CEST

[Cadence](https://blog.jetbrains.com/pycharm/2025/06/training-your-ml-models-with-cadence/) is a JetBrains-hosted service integrated with PyCharm through an optional plugin, that lets you run your projects on cloud compute resources. Cadence uses JetBrains TeamCity to orchestrate this work. We recently disclosed [CVE-2026-63077](https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/), a critical vulnerability in TeamCity that can allow an unauthenticated attacker to execute arbitrary commands on a vulnerable server.

We have since confirmed the Cadence environment was vulnerable to CVE-2026-63077 and was exploited through this vulnerability.

Cadence users should immediately revoke or rotate all credentials and secrets that may have been used to run their Cadence executions. They should also treat all executions, including their inputs and outputs in your Cadence project, as potentially untrusted.

### **Actions required immediately**

We strongly recommend that Cadence users:

- Revoke and rotate all credentials and secrets that may have been used to run Cadence executions.
- Review connected systems for suspicious activity, particularly AWS accounts, S3 buckets, deployment environments, package/container registries, and other systems accessible using credentials mentioned above.
- Review source code repositories for unauthorized changes made during the affected period.
- Review any source code or project files synchronized to Cadence from PyCharm and rotate any credentials, tokens, or other sensitive information contained within them.
- Treat all executions, including their inputs and outputs in your Cadence project, as potentially untrusted.

Cadence users can contact us to request an inventory of the credentials and secrets associated with their Cadence usage. This may help users identify which credentials need to be revoked or rotated, but the inventory should not be considered exhaustive.

We have collated a list of Indicators of Compromise (IoCs) below. These indicators are not exhaustive, and the absence of these indicators does not confirm that an account or system was unaffected:

- Activity occurring from August 8, 2026, onwards, particularly authentication or activity using credentials previously stored in or accessible through Cadence.
- IP addresses associated with observed exploitation activity:
  - 150.109.230.104
  - 43.153.227.206
  - 62.210.127.48
  - 210.247.242.190
  - 15.235.225.205
  - 152.233.30.18
- Authentication or other activity from unexpected IP addresses or locations.
- Unexpected repository clones or downloads, and unexpected commits to repositories.
- Changes to repository secrets, webhooks, collaborators, or permissions.
- New or modified personal access tokens, API tokens, or SSH keys in external services.
- New service accounts created in external services.
- Unexpected changes to cloud IAM roles, policies, or permissions.
- Unexpected access to cloud storage, including S3 buckets and objects, in services such as AWS and Google Cloud.
- Unexpected publication or modification of packages or releases.

### **Affected server**

We have confirmed that the following Cadence server was successfully exploited: `api.cadence.jetbrains.com`.

### **Affected period**

August 8, 2026, to August 24, 2026.

### **What happened**

The Cadence server used TeamCity to orchestrate workloads and was vulnerable to CVE-2026-63077. Threat actors exploited the vulnerability and gained unauthorized access to the affected Cadence environments, with activity identified from August 8, 2026. We discovered the exploitation on August 23, 2026, and took the affected server offline on August 24, 2026, while we continued our investigation.

### **What we know**

Our investigation is ongoing, but we have confirmed that the threat actors:

- Accessed personal data and extracted it from the affected environment. Confirmed affected personal data includes usernames, real names, email addresses, last-login timestamps, and last accessed IP addresses.
- Compromised a full backup of the Cadence server dating from 2024. This means credentials, configuration, artifacts, logs, or other data present in that backup must also be treated as potentially exposed.
- Compromised multiple AWS IAM users and associated credentials/secrets used with Cadence, including IAM users belonging to JetBrains employees who used the service. These credentials were present in the compromised 2024 backup.
- Accessed files stored in S3 buckets within JetBrains AWS accounts used by Cadence. We are still determining the full scope of the data accessed. We do not currently know whether the threat actors accessed storage buckets in customer accounts. However, some users may have configured Cadence to access their own storage buckets, and the credentials used for those connections may have also been exposed.
- May have accessed source code synchronized from PyCharm projects to the affected server. If you used PyCharm to upload or synchronize project files for execution in Cadence, you should treat that code, and any credentials or configuration contained within it, as potentially compromised.

The likely consequences of the personal data exposure include an increased risk of targeted phishing, social engineering, impersonation, and other unsolicited or malicious communications using the affected names and email addresses.

As the threat actors gained access to the Cadence server, any credentials or secrets stored in Cadence, contained in the compromised backup, or made available to executions on the affected server should be considered compromised and must be revoked or rotated.

This includes but is not limited to:

- Cloud credentials, including AWS, Azure, and Google Cloud.
- Source control credentials and tokens, including GitHub, GitLab, and Bitbucket.
- Package repository credentials, including npm, Maven, NuGet, PyPI, and similar services.
- Container registry credentials, including Docker Hub, ECR, GCR, ACR, and other registries.
- Slack tokens, webhooks, API tokens, SSH/deployment keys, service account credentials, signing keys/certificates, and credentials for any other external systems used by your Cadence executions.

### **Actions JetBrains has taken**

We took the Cadence server offline on August 24, 2026, while we continue to investigate the incident. At present, we have confirmed that the incident is limited to data associated with the Cadence host mentioned above.

The server should have been patched as part of our response to the vulnerability, but it was not. We sincerely apologize for this failure and the impact it may have on you.

We have invalidated all access tokens used by the JetBrains Cadence plugin in PyCharm to connect to Cadence, and took the server offline on August 24, 2026.

We are also notifying the relevant authorities and taking the necessary steps to protect the data of Cadence users.

### **Further updates**

We will publish further findings and guidance here as our investigation progresses. We recommend checking this page frequently for the latest information. We will also contact affected users directly if we identify any important new information that may require action on their part.

For more information about the underlying vulnerability, please see our original [security advisory](https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/) to TeamCity customers and users.

If you previously used Cadence and need assistance identifying which credentials may have been exposed or have any questions regarding this incident, contact the JetBrains Security team at [security@jetbrains.com](<mailto:security@jetbrains.com?subject=Security incident affecting JetBrains Cadence>).

We recognize the seriousness of this incident and apologize again for the impact.


*Prev post*PyCharm for AI-assisted Django Workflows
[The State of Django 2026: Boring is so back](https://blog.jetbrains.com/pycharm/2026/08/the-state-of-django-2026-boring-is-so-back/)

*Next post*
#### Subscribe to PyCharm Blog updates
