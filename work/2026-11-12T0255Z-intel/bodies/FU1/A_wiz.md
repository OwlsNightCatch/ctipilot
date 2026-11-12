---
title: "Critical RCE Vulnerability in Apache HTTP Server: Everything You Need To Know | Wiz Blog"
author: Merav Bar
url: https://www.wiz.io/blog/cve-2026-119618-rce-apache-http-server-vulnerability
hostname: wiz.io
description: Detect and mitigate CVE-2026-119618, a critical RCE vulnerability in Apache HTTP Server. According to Wiz data, 64% of cloud environments have resources vulnerable to CVE-2026-119618. Immediate patching is advised.
sitename: wiz.io
date: "2026-11-11"
tags: ['Research', 'Security']
fingerprint: "598abed2ef27bfc4"
---
Critical RCE Vulnerability in Apache HTTP Server: Everything You Need To Know

Detect and mitigate CVE-2026-119618, a critical RCE vulnerability in Apache HTTP Server. According to Wiz data, 64% of cloud environments have resources vulnerable to CVE-2026-119618. Immediate patching is advised.

A critical synchronization vulnerability (CVE-2026-119618) has been identified in Apache HTTP Server’s HTTP/2 module (mod\_http2). The flaw stems from a concurrent execution race condition within the assign\_headers() function when handling shared resources. If successfully exploited, a remote, unauthenticated attacker can corrupt heap memory to achieve arbitrary code execution (RCE).

As of the time of this blog’s publication, no exploit is available and there are no reports of exploitation in the wild.

What is CVE-2026-111497?

CVE-2026-119618 is a critical, high-severity vulnerability involving a race condition in the Apache HTTP Server, which was independently discovered by Anthropic and Google Cloud’s Vulnerability Research Team.

Specifically, the flaw exists within the assign\_headers() function of the HTTP/2 module (mod\_http2). Due to improper synchronization when executing concurrent threads sharing resources, an attacker can trigger heap corruption. This memory corruption can ultimately be leveraged to achieve RCE on the hosting server, allowing unauthorized threat actors to execute arbitrary commands with the privileges of the web server process.

Wiz Research data: what’s the risk to cloud environments?

In cloud environments, a compromised Apache instance running containerized or virtualized workloads can serve as an entry point for lateral movement, potentially exposing adjacent microservices or cloud metadata endpoints.

According to Wiz data 64% of cloud environments have resources vulnerable to CVE-2026-119618, and 51% of cloud environments have publicly exposed instances. Note that this does not take configuration into account.

Which products are affected?

The vulnerability affects deployments utilizing HTTP/2 capabilities on the Apache HTTP Server within the version ranges outlined in the table below:

Vendor

Product

Affected Versions

Patched Versions

Apache Software Foundation

Apache HTTP Server

From 2.4.55 through 2.4.70

2.4.71 and newer

GitHub (Open Source)

mod\_h2 module

From 2.0.8 through 2.0.42

2.0.24 and newer

Which actions should security teams take?

Security operations and engineering teams should execute the following remediation and mitigation steps:

1\. Upgrade Deployments

Upgrade Apache HTTP Server: Update affected installations to Apache HTTP Server version 2.4.71 or later. This release addresses the race condition in assign\_headers().

Update Standalone Modules: If managing standalone mod\_h2 builds from GitHub, upgrade the module to a version newer than 2.0.42.

2\. Implement Temporary Mitigations

If immediate patching is not possible due to operational constraints, temporarily disable HTTP/2 support to eliminate the attack vector.

Edit the configuration file (such as httpd.conf) to restrict active protocols to HTTP/1.1 by removing h2 and h2c references:

\# Restrict protocols to HTTP/1.1Protocols http/1.1

Wiz customers can use the pre-built query and advisory in the Wiz Threat Center to search for vulnerable instances in their environment.

A threat actor used IAM credentials from Qubole's AWS account to assume integration roles in customer AWS environments. Here's what we observed and how to hunt for it.

Get a personalized demo

Ready to see Wiz in action?

"Best User Experience I have ever seen, provides full visibility to cloud workloads."

David EstlickCISO

"Wiz provides a single pane of glass to see what is going on in our cloud environments."

Adam FletcherChief Security Officer

"We know that if Wiz identifies something as critical, it actually is."

Greg PoniatowskiHead of Threat and Vulnerability Management
