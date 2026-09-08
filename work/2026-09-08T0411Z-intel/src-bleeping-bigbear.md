# extract: served via trafilatura-direct
---
title: BigBear Microsoft 365 phishing service bypassed MFA at 258 organizations
author: Bill Toulas
url: https://www.bleepingcomputer.com/news/security/bigbear-microsoft-365-phishing-service-bypassed-mfa-at-258-organizations/
hostname: bleepingcomputer.com
description: A phishing-as-a-service framework called BigBear 2.0 has been used to bypass multi-factor authentication at 258 organizations and steal more than 5,000 Microsoft 365 credentials.
sitename: BleepingComputer
date: "2026-09-07"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Account Takeover, MFA, MFA Bypass, Microsoft 365, Phishing, Phishing Kit, Phishing-as-a-Service, Proxy,virus removal, malware removal, computer help, technical support']
---
A phishing-as-a-service framework called BigBear 2.0 has been used to bypass multi-factor authentication at 258 organizations and steal more than 5,000 Microsoft 365 credentials.

Researchers at cybersecurity company CloudSEK gained administrator access to the control panel and found that the service managed 42 VPS nodes, all configured to target Microsoft 365 as part of the observed operation.

According to the researchers, the campaign uses an Evilginx2-based adversary-in-the-middle framework to intercept passwords and authenticated session cookies, allowing attackers to hijack accounts after victims complete the multi-factor authentication (MFA) process.

BigBear uses a configuration called “offy” that sets up a man-in-the-middle (AiTM) proxy between the victim and Microsoft’s legitimate authentication infrastructure.

This allows the attacker to capture credentials, including MFA, and session cookies and replay them through an API to hijack the victim’s authentication session.

Microsoft 365 is Microsoft's cloud productivity and identity ecosystem, incorporating services such as Exchange Online, Teams, SharePoint, OneDrive, and Entra ID authentication.

Compromising an authenticated Microsoft 365 session can expose email and files while potentially providing access to other applications connected through single sign-on.

According to CloudSEK, BigBear proved to be sufficiently successful to compromise hundreds of entities and capture thousands of cookies.

“The panel has exfiltrated 5,137 credential records - including 474 complete MFA-bypassed authentications, 1,032 plaintext passwords, and 4,148 session cookies - affecting 3,331 unique victim IPs across 40+ countries with the operation still active at the time of writing,” [CloudSEK says](https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign) in a report shared with BleepingComputer.

“The multi-user PhaaS panel is leased to at least five affiliate operators identified through live Telegram exfiltration bots, each receiving stolen credentials in real time.”

While 461 organizations appeared in the broader targeting dataset, CloudSEK clarified that 258 distinct organizations had at least one completed MFA-bypass compromise.

CloudSEK has also found that BigBear uses custom JavaScript that interferes with FIDO2/WebAuthn authentication, disabling the browser functionality that accommodates it to force targets toward weaker authentication methods.

To increase its effectiveness, the platform uses geo-matched residential proxies for 69 countries, matching the victim’s location with a residential IP address so that Microsoft’s authentication servers don’t flag the activity as suspicious.

CloudSEK said it notified law enforcement and several affected organizations and included credentials in responsible-disclosure reports.

At the time of writing, the administration panel remains online, while the phishing infrastructure has been offline for nearly three weeks.

Organizations that were potentially affected by BigBear activity should reset exposed passwords, revoke active sessions, refresh tokens, and force re-authentication for high-privileged accounts.

It is also advisable to enforce phishing-resistant FIDO2/WebAuthn and use Conditional Access policies that require managed devices rather than relying on geo-location signals.

## 
            [Once attackers have valid credentials, only 37% of their actions are blocked](https://hubs.li/Q04sB3fb0)
        

        Overall prevention scores can hide what happens after initial access. Once attackers are using valid credentials, prevention drops sharply.

The Blue Report 2026 measures defenses technique by technique across 338 million simulations run in customer production environments.

[Get the report](https://hubs.li/Q04sB3fb0)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
