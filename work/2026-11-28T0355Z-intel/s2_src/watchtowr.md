---
title: "4HTTP2ROOT FAQ: Cacti Zero-Day Exposure and Fix"
url: https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/
hostname: watchtowr.com
description: "4HTTP2ROOT Zero-day in Cacti: Remote Code Execution, affected versions, the fixed version, and checking for compromise, updated as details emerge."
sitename: watchTowr
date: "2026-11-26"
categories: ['Vulnerability FAQ']
tags: ['4HTTP2ROOT', 'Cacti', 'Remote Code Execution']
fingerprint: f0d0b05bcd4bb209
language: en
image: https://watchtowr.com/wp-content/uploads/4http2root-cacti-zero-day-faq.png
pagetype: article
filedate: "2026-11-28"
---
## What is the Remote Code Execution in Cacti?

4HTTP2ROOT is a Remote Code Execution vulnerability in Cacti, an open source network monitoring tool, that lets an attacker with no account and no valid session run operating system commands on the Cacti server. The attacker starts as an anonymous guest, writes an unvalidated value into a per user display setting, and that value is later inserted into a database query that the server treats as more than one command. One of those extra commands changes a poller setting to a shell command, which a separate guest reachable page then executes.

Because Cacti often stores credentials and connection details for routers, switches, servers, and other devices across a network, an attacker who reaches this level of command execution can gain a foothold reaching far beyond the monitoring server itself.

## Is 4HTTP2ROOT being exploited in the wild?

As of November 27, 2026, no exploitation in the wild has been reported.

## How did 4HTTP2ROOT come to light?

A researcher using the handle ek0ms savi0r, published the chain on GitHub on November 26, 2026, describing four unauthenticated HTTP requests that reach command execution on a lab instance of Cacti Core 1.2.31.

## How is watchTowr helping Cacti customers?

- [Adversary Sight engine](https://watchtowr.com/platform/#adversary-sight) identified Cacti instances across client environments and assessed exposure.
- [Rapid Reaction](https://watchtowr.com/use-cases/rapid-reaction/) identified exposure to this vulnerability across the watchTowr client base, giving teams the time they need to act.

## What is Cacti?

Cacti is an open source network monitoring and graphing tool that enterprises use to track performance data from routers, switches, servers, and other devices across a network. It stores credentials such as SNMP strings and device logins used to reach those systems, making it a central point of trust inside many enterprise networks.

## Which Cacti versions are affected?

| Product | Affected Versions | Fixed Version | 
|---|---|---|
| Cacti Core | 1.2.31 | Not yet available | 

- The guest account must be enabled, since the entire chain runs through the unauthenticated guest session.
- The researcher tested the chain against Cacti Core version 1.2.31 in an isolated lab.
- The privilege gained matches whichever account runs the Cacti web server and poller process, often a low privileged web user rather than root.

Deployments that run Cacti Core 1.2.31 with the guest account enabled face the most direct risk, especially when the Cacti web interface is reachable from untrusted networks.

## How do I fix 4HTTP2ROOT?

Cacti has not published a fixed version for this vulnerability, so security teams should disable the guest account to break the chain and restrict the Cacti web interface to trusted networks until an official patch appears.

1. Disable the guest account within Cacti's user administration settings to remove the chain's entry point.
2. Restrict network access to the Cacti web interface to trusted internal networks only.
3. Review poller configuration entries for unexpected command values that do not match normal polling setup.
4. Watch application logs for warnings about non-numeric values in display settings, which the chain produces.
5. Apply the vendor's fixed version for Cacti Core as soon as one becomes available.

## How do I check Cacti for compromise?

Administrators can watch for warning messages in Cacti's logs about a non-numeric value in a graph display setting, which the research describes as appearing even though the request still succeeds. Unexpected commands configured in poller settings, or new files created by the poller process, are further signs that the chain has run.

## What types of threat actors typically exploit this vulnerability?

No attribution has been made public.
