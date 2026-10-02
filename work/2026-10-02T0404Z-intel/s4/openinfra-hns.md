---
title: OpenInfra Europe's JFrog Artifactory instance breached, packages potentially compromised - Help Net Security
author: Zeljka Zorz
url: https://www.helpnetsecurity.com/2026/09/30/openinfra-jfrog-artifactory-instance-compromised/
hostname: helpnetsecurity.com
description: Attackers have compromised a self-hosted JFrog Artifactory instance (https://artifactory.nordix.org/) operated by OpenInfra Europe.
sitename: Help Net Security
date: "2026-09-30"
categories: ["Don't miss", 'Hot stuff', 'News']
tags: ['breach', 'JFrog', 'open source', 'OpenInfra', 'vulnerability', 'breach', 'JFrog', 'open source', 'OpenInfra', 'vulnerability']
---
# OpenInfra Europe’s JFrog Artifactory instance breached, packages potentially compromised

Attackers have compromised a self-hosted JFrog Artifactory instance operated by OpenInfra Europe, the regional hub of the OpenInfra Foundation warned in a security notice prominently displayed on its homepage.

OpenInfra Europe’s security incident notice

“Anyone who downloaded or installed artifacts from **https://artifactory.nordix.org/** from August 28 and September 15, 2026 should immediately stop using them, remove them from their pipelines, and treat these packages as potentially compromised,” the message says.

### Compromise through CVE-2026-82329

The OpenInfra Foundation is part of the non-profit Linux Foundation. It hosts and supports open source projects for running cloud and datacenter infrastructure. (Its best-known project is OpenStack, the open source platform for building private and public clouds.)

JFrog Artifactory is a binary repository manager that’s used for storing and serving the build outputs and dependencies that software development teams use. Organizations can self-host it or choose to go the Software-as-a-Service route.

According to the security notice, the compromised instance was running a vulnerable JFrog Artifactory version, which allowed unauthenticated attackers to exploit CVE-2026-82329, an authentication bypass vulnerability, to gain access to the instance and obtain admin privileges (and thus the capability to tamper with the deployment and the artifacts, credentials and integrations it manages.)

CVE-2026-82329 was [publicly disclosed](https://docs.jfrog.com/releases/docs/jfrog-security-advisories#cve-2026-82329---potential-authentication-bypass-leading-to-administrative-access-in-artifactory) on August 28, 2026, and was added to CISA’s Known Exploited Vulnerabilities catalog on September 2.

According to [various](https://www.fastly.com/blog/cve-2026-82329-jfrog-artifactory-authentication-bypass-exploitation-activity) [sources](https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201), in-the-wild exploitation began on August 31. 

OpenInfra Europe says that the compromise of their Artifactory instance happened on that day, but that the breach was discovered on September 15, “after a legitimate user was denied access.”

The affected system was immediately isolated and investigation began, it added, but the full scope and impact of the incident is still undetermined.

**Subscribe to our breaking news e-mail alert to never miss out on the latest breaches, vulnerabilities and cybersecurity threats. [Subscribe here!](https://www.helpnetsecurity.com/newsletter/)**
