---
title: Barracuda links cloud breach to ARTEX AI-powered cyberattack
author: Bill Toulas
url: https://www.bleepingcomputer.com/news/security/barracuda-links-cloud-breach-to-artex-ai-powered-cyberattack/
hostname: bleepingcomputer.com
description: Hackers who breached the cloud environment of network and email security company Barracuda earlier this month used a stolen cloud access key and the ARTEX AI penetration testing framework.
sitename: BleepingComputer
date: "2026-11-16"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, AI, ARTEX, Artificial Intelligence, Barracuda, Cloud, Security Breach,virus removal, malware removal, computer help, technical support']
fingerprint: "1d4f9b02dd37a504"
---
Hackers who breached the cloud environment of network and email security company Barracuda earlier this month used a stolen cloud access key and the ARTEX AI penetration testing framework.

The company says the attacker accessed approximately 10 of its cloud accounts over a 44-hour period between November 1 and 2.

The attacker's presence was discovered on November 4, and Barracuda's investigation determined that the open-source [AI pentesting framework ARTEX](https://www.bleepingcomputer.com/news/security/fbi-warns-artex-ai-hacking-tool-is-powering-global-cyberattacks/) was used for this "machine-speed intrusion."

The company explains that the attacker leveraged a cloud access key provided to a third-party vendor for the duration of a previous project.

"We did not retire the key when the vendor — a company working in AI — finished that work. That is on us," Barracuda says.

The security company believes the attacker stole the key from the unnamed third-party AI vendor in October. It [confirmed](https://trust.barracuda.com/security/barracuda-xdr-integration-credentials) that the key was stored in a configuration file in the vendor's GitHub repository.

The attacker used credentials they found in one system to move through Barracuda’s data analytics environment, source-code repositories, and Kubernetes clusters.

Based on the attacker's commands targeting cryptocurrency-related secrets, including private keys, Ethereum keystore files, and seed phrases, [Barracuda believes](https://blog.barracuda.com/2026/11/11/anatomy-of-a-machine-speed-intrusion) the attack was financially motivated.

However, the company does not rule out that this activity might have been a diversion from the attacker’s true motive.

The threat actor attempted to establish persistence by deploying a container that mounted the host’s file system, including credentials stored on it.

A separate attempt to create a new cloud administrator identity was blocked.

Barracuda says the attack used machine-style labels, certain probing methods, and built-in hunting routines that matched what is found in ARTEX.

The firm noted that the attack was very similar to a [recent incident](https://www.bleepingcomputer.com/news/security/railway-warns-devs-to-rotate-secrets-after-potential-breach/) at cloud hosting provider Railway, which also involved credential chaining and the [apparent use of ARTEX](https://www.bleepingcomputer.com/news/apple/railway-breach-leads-to-740-000-in-fraudulent-ai-charges/).

According to the cybersecurity company, the attacker reached a system that stores customer integration credentials for Barracuda XDR; however, it found no evidence that those were accessed or stolen.

Because of the uncertainty surrounding this scenario, Barracuda asked potentially affected Managed XDR Cloud or Monitored Endpoint customers to revoke and recreate their integration credentials.

Barracuda assures customers who did not receive direct communications about this incident that they need to take no action.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
