---
title: Fake OpenAI, SpaceX events used to steal Microsoft, Google accounts
author: Lawrence Abrams
url: https://www.bleepingcomputer.com/news/security/fake-openai-spacex-events-used-to-steal-microsoft-google-accounts/
hostname: bleepingcomputer.com
description: Hackers are using fake OpenAI, SpaceX, and Anthropic event invitations to lure employees into phishing attacks, using two different phishing-as-a-service platforms to steal Microsoft and Google account credentials and authentication sessions.
sitename: BleepingComputer
date: "2026-11-05"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Device Code, Google, Kali365, MFA, Microsoft, PhaaS, Phishing, VoidProxy,virus removal, malware removal, computer help, technical support']
fingerprint: "3c2088491982fdcd"
---
Hackers are using fake OpenAI, SpaceX, and Anthropic event invitations to lure employees into phishing attacks, using two different phishing-as-a-service platforms to steal Microsoft and Google account credentials and authentication sessions.

According to a new report from [Push Security](http://pushsecurity.com/blog/ai-themed-fake-event-campaign-analysis), the attackers use convincing event registration pages offering free access to premium AI services and other rewards to trick victims into signing in with their corporate accounts.

What makes the attacks interesting is that the same phishing pages integrate two separate phishing-as-a-service (PhaaS) platforms, Kali365 and VoidProxy, to target Microsoft and Google accounts using different authentication attacks.

Kali365 conducts Microsoft device code phishing attacks, while VoidProxy acts as an adversary-in-the-middle (AiTM) reverse proxy to intercept Google sign-ins and steal authentication session cookies.

The Microsoft attack also uses VoidProxy as a second stage, allowing attackers to capture credentials and session cookies after obtaining authentication tokens through Kali365.

Push Security says it detected and blocked visits to the malicious event registration pages in late October 2026.

The campaign comes after a similar campaign documented by [ANY.RUN](https://x.com/anyrun_app/status/2077370282193404060) in July, when attackers abused legitimate Zoom event pages to promote fake Meta, OpenAI, and Anthropic events that led to device code and AiTM phishing attacks.

Cofense also [recently reported](http://cofense.com/blog/would-your-employees-join-a-fake-anthropic-ai-preview) on phishing emails impersonating Anthropic event invitations that were distributed through GoTo Webinar's email infrastructure and redirected recipients through multiple websites to fake registration pages.

## Fake AI events lead to account phishing

While it is unclear how the attackers initially distribute the phishing links, Push Security found that they redirect victims to a malicious event registration page using links from trusted services, including Google and Zapier URL shorteners.

Invitations from earlier versions of the campaign were also distributed through GoTo Webinar's email systems or legitimate Zoom event pages.

Push Security says the attackers use two custom phishing kits, tracked as ZoomMock and MSDRoot, to create fake event pages that then direct victims to the Kali365 and VoidProxy phishing services.

The researchers believe the same threat actors operate both kits, as they use shared infrastructure and the same targeting.

The campaign impersonates events hosted by OpenAI, SpaceX, and Anthropic, with registration pages designed to resemble legitimate event websites.

One phishing page advertises an OpenAI event titled "ChatGPT for Social & Digital Marketing Teams" that promises three months of ChatGPT Pro to participants.

Another promotes a private SpaceX event on November 12, offering registrants either three months of Grok Heavy or a "SpaceX share."

The researchers also found a phishing page impersonating an Anthropic event at AWS re:Invent 2026 that was already taken down.

The fake registration pages tell visitors they must sign in with their work accounts to register and claim the advertised rewards.

Before displaying the fake registration pages, the websites show a Cloudflare CAPTCHA to "Confirm you're not a robot." This prevents automated security platforms from scanning the phishing site.

Once visitors reach the event registration page, they see two options: "Continue with Microsoft" and "Continue with Google."

When victims select the Microsoft option, the phishing page contacts the Kali365 platform to generate a Microsoft device authentication code.

A device code phishing attack occurs when an attacker abuses the legitimate OAuth 2.0 device authorization grant flow to obtain authentication tokens for the victim's Microsoft Entra account.

This can then be used to access the user's resources and connected SSO applications, such as Microsoft 365, Salesforce, Google Workspace, Dropbox, Adobe, SAP, Slack, Zendesk, Atlassian, and many others.

Device code phishing attacks have been used in the past for [data theft](https://www.bleepingcomputer.com/news/security/hackers-target-microsoft-entra-accounts-in-device-code-vishing-attacks/) and [cyberespionage attacks](https://www.bleepingcomputer.com/news/security/microsoft-365-accounts-targeted-in-wave-of-oauth-phishing-attacks/).

The visitor is instructed to copy the code and enter it on Microsoft's legitimate device login website, where they authenticate and approve the request.

This allows the Kali365 phishing platform to steal Microsoft authentication tokens without requiring the victim to disclose their password directly.

After the device code authentication succeeds, the page redirects the victim to a VoidProxy Microsoft login page, where attackers can also capture the victim's password and session cookie.

When victims select the Google authentication option, the phishing page instead opens a pop-up containing a Google login page from the VoidProxy PhaaS.

The platform operates as an adversary-in-the-middle (AiTM) platform that sits between the victim's browser and Google's login page, proxies the login forms, and steals credentials, MFA responses, and session cookies.

Both the Kali365 and VoidProxy platforms let attackers bypass multifactor authentication by capturing an already authenticated session or, in the case of device code authentication, bypassing MFA entirely.

To protect against these attacks, employees should avoid entering Microsoft device authentication codes provided by unfamiliar websites and be cautious of event invitations that require signing in with corporate accounts to claim rewards.

Organizations can also restrict device code authentication where it is not needed and use phishing-resistant MFA, such as FIDO2 security keys, to help prevent session hijacking.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
