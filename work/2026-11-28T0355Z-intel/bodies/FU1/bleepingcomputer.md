---
title: Unpatched Cacti zero-day with public PoC gives remote code execution
author: Lawrence Abrams
url: https://www.bleepingcomputer.com/news/security/unpatched-cacti-zero-day-with-public-poc-gives-remote-code-execution/
hostname: bleepingcomputer.com
description: A zero-day vulnerability in the Cacti network monitoring platform has been publicly disclosed, along with a proof-of-concept exploit that lets unauthenticated attackers execute commands on vulnerable servers.
sitename: BleepingComputer
date: "2026-11-27"
tags: ['computers', 'windows', 'linux', 'mac', 'support', 'tech support', 'spyware', 'malware', 'virus', 'security', 'Cacti', 'Public PoC', 'Stored SQL Injection', 'Vulnerability', 'Zero-Day', 'virus removal', 'malware removal', 'computer help', 'technical support']
fingerprint: "91dbb45be91a7205"
language: en
image: https://www.bleepstatic.com/content/hl-images/2026/11/27/cacti.jpg
pagetype: article
filedate: "2026-11-28"
---
A zero-day vulnerability in the Cacti network monitoring platform has been publicly disclosed, along with a proof-of-concept exploit that lets unauthenticated attackers execute commands on vulnerable servers.

The exploit, dubbed "[4HTTP2SHELL](https://github.com/ekomsSavior/Sad-Girls-0day-Club/tree/main/4http2shell)" (previously 4HTTP2ROOT), was published on Thanksgiving Day by a cybersecurity researcher known as ek0ms savi0r from the Church of Malware, who demonstrated how the vulnerability can be exploited using just four HTTP requests.

Cacti is an open-source network monitoring and graphing tool used to monitor the performance of servers, routers, switches, firewalls, and other network infrastructure.

Because the software can store credentials and SNMP passphrases used to access or read data from monitored devices, compromising a Cacti server could potentially give attackers access to other systems on a corporate network.

The researcher published a technical write-up, a proof-of-concept (PoC) exploit, and a video demonstrating the attack in a GitHub repository named "Sad Girls 0day Club."

"I found a path from a fresh, unauthenticated HTTP session to command execution as the Cacti server user in four requests. No login. No valid API key. No phishing. Just four HTTP requests against the default guest surface," explains the researcher.

The vulnerability stems from weak input validation that allows an unauthenticated attacker to inject SQL statements into the application's database and modify commands executed by Cacti's real-time poller.

The attack requires the Cacti guest account to be enabled but does not require attackers to possess valid credentials.

While the researcher demonstrated the exploit providing root access to a vulnerable server, cybersecurity firm [watchTowr explains](https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/) that the privileges gained through exploitation depend on the account running the Cacti web server and poller processes.

In many deployments, this could be a low-privileged web server account rather than root.

Cybersecurity firm [RavenAI explains](https://ravenai.sh/blog/four-requests-to-shell-cacti) that the attack abuses weak validation of guest users' graph display settings, resulting in a stored SQL injection vulnerability.

The attack involves an attacker saving malicious SQL statements in a guest user's graph display preferences, which are stored in Cacti's database.

When Cacti processes these saved preferences, it executes the SQL statements, allowing the attacker to modify the poller's configuration and cause it to run malicious operating system commands.

The researcher tested the exploit against Cacti Core 1.2.31, but it is unclear whether earlier versions are also vulnerable.

In a separate post on [the GitHub repository](https://github.com/ekomsSavior/Sad-Girls-0day-Club/blob/main/sad_girls_0day_article.md), ek0ms savi0r expressed frustration with how companies handle vulnerability disclosures, describing years of security reports being dismissed or closed as duplicates, expected behavior, or issues that could not be reproduced.

"Security researchers are not the bad guys. We're the ones trying to help. We're the ones who read the docs, wrote the repro, and sent the packet capture," wrote the researcher.

"We get cracked because we get gaslit for years by billion dollar companies that treat disclosure like a PR problem."

In an [Instagram post](https://www.instagram.com/p/DgNqejbozp7/?img_index=1) announcing the Cacti exploit, the researcher shared a video demonstration of the PoC and said that the vulnerability was not reported to Cacti before being released.

Until a patch is released, administrators are advised to deactivate the Cacti guest account and restrict access to the application's web interface to trusted networks.

Administrators should also review poller configurations for unexpected commands and examine application logs for warnings involving non-numeric values in graph display settings, which could indicate attempted exploitation.

As of November 27, there have been no reports of the vulnerability being exploited in attacks.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
