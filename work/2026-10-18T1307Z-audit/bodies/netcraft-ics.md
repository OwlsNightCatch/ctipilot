---
title: How Attackers Get Into Your Calendar the Easy Way
url: https://www.netcraft.com/blog/how-attackers-get-into-your-calendar-the-easy-way
hostname: netcraft.com
description: Threat actors are abusing ICS calendar invites to evade email security and reach users through calendars. Learn the risks and defenses.
sitename: Netcraft
date: "2026-10-16"
fingerprint: "3d688d686b46d6c9"
---
# You’re Invited: How Attackers Get into Your Calendar the Easy Way

## Executive summary

Threat actors are using ICS calendar invite files to bypass email security filters and often achieve persistence in targets’ calendars even after the original email is deleted. This technique came to be used in sophisticated and widespread attacks in 2025 and is now seeing more adoption in low-effort attacks. Defenders may wish to review ICS settings in their email clients and adjust phishing guidance to reflect that invites may be a vector for attackers.

## [From research to reality](https://www.netcraft.com#from-research-to-reality) 

Minor use of ICS files — files that contain information on events or meeting invites that synch with apps like Microsoft Outlook and Apple iCal — for attacks was first observed between 2020 and 2022, with findings primarily niche, isolated, or research based. It was not until 2025 that ICS files became significant delivery mechanisms for phishing campaigns.

The first significant example was the use of malicious ICS files to exploit a stored XSS vulnerability in the Zimbra Collaboration Suite’s Classic Web Client ([CVE-2025-27915](https://nvd.nist.gov/vuln/detail/cve-2025-27915)). Since then, threat actors have continued to adapt, integrating ICS files into phishing campaigns to bypass email security filters and avoid suspicion. Other researchers, such as those at email security firm Sublime Security has noted [“exponential growth”](https://www.theguardian.com/money/2026/oct/11/calendar-phishing-scam-meeting-renewal-google-microsoft-paypal#:~:text=Luke%20Wescott%2C%20a%20threat%20detection%20engineer%20at%20Sublime%20Security%2C%20says%20calendar%20phishing%20is%20still%20relatively%20new%20but%20the%20company%20has%20seen%20%E2%80%9Cexponential%20growth%E2%80%9D) in their observations of calendar phishing and The Guardian has [recently reported](https://www.theguardian.com/money/2026/oct/11/calendar-phishing-scam-meeting-renewal-google-microsoft-paypal#:~:text=Luke%20Wescott%2C%20a%20threat%20detection%20engineer%20at%20Sublime%20Security%2C%20says%20calendar%20phishing%20is%20still%20relatively%20new%20but%20the%20company%20has%20seen%20%E2%80%9Cexponential%20growth%E2%80%9D) on campaigns leveraging this TTP to lead victims to fake Microsoft, Google, or PayPal pages.

*Example of an ICS event captured by Netcraft that uses this technique.*

More recently observed exploitation has been focused on exploiting the behavior of the recipient’s email client to bring phishing lures directly into their calendar. This has been accompanied by an increase in observed volume as this TTP has moved beyond academic contexts and entered use by relatively unsophisticated threat actors.

## [Why it works](https://www.netcraft.com#why-it-works) 

ICS files are the “text/calendar” MIME type, which is treated as low risk by major email clients. This is because the files are non-executing, structured text. On their own, they may seem no more harmful than a generic TXT file.

*Contents of an ICS file containing an Amazon Prime renewal lure.*

What makes this dangerous is the exploitation of email-calendar client workflows that are expected and relied on by many users.

When an invite is sent to a user, having the item penciled into their calendar helps identify conflicts when scheduling. In this case, however, it allows attackers to go from the target’s inbox to their calendar without user interaction. Ultimately, the lure’s injection into the target’s calendar is a normal and intended behavior of their email client. In many email clients, this allows the invite to persist in the target’s calendar even after the original phishing email is deleted.

Email-attached calendar invites are now so ubiquitous that the average user may barely scrutinize them. In fast-paced, tech-reliant workplaces, new events appearing in the calendar without manual entry have become normalized. This combination of automatic behavior by email clients, users’ normalized expectations that events simply appear, and persistence even after the original email is deleted gives threat actors an easy route to the user’s attention.

## EvilTokens and beyond: How attackers are weaponizing calendar invites at scale

Calendar invite abuse has been adopted as a delivery mechanism by widespread campaigns such as those using EvilTokens, a token-stealing phishing toolkit targeting Microsoft 365 accounts that was [previously reported](https://www.netcraft.com/eviltokens-and-oauth-abuse) by Netcraft. This campaign often used ICS files as low-friction lures, attempting to bypass scrutiny, appearing directly in a user’s calendar, and remaining even if the original phishing email was deleted. Invites associated with this campaign are often disguised as meetings, alerts, or voicemail notifications. When users follow them, they are taken to an attacker-controlled page that gives them a device code and instructions to enter it into Microsoft’s device authorization page. These instructions, presented by the service allegedly notifying the victim, purport to be for the user’s identity verification to access files.

In reality, the user will have allowed another device access to their account through OAuth. user will have allowed another device access to their account through OAuth. user will have allowed another device access to their account through OAuth. user will have allowed another device access to their account through OAuth.

*Example from the EvilTokens Voicemail Cluster captured by Netcraft.*

Campaigns like this take advantage of the automatic processing built into most modern inboxes. Users may also trust their calendar as this attack’s appearance does not align with many users’ expectations of what phishing looks like, and their calendar is a place that they may see as generally under their own control.

While this shows use of this technique in a sophisticated and widespread campaign, Netcraft has also observed its use in smaller scam efforts. These often include the same lure content as traditional phishing, just inside of an ICS file. The fake Microsoft, Google, and PayPal campaigns mentioned in [The Guardian’s report](https://www.theguardian.com/money/2026/oct/11/calendar-phishing-scam-meeting-renewal-google-microsoft-paypal) are not confirmed to be an EvilTokens campaign – though they employed similar lures, claiming documents or voicemails were available for review. This is becoming a normalized TTP in the wild. Defenders’ expectations of phishing tactics will need to catch up, or the behavior of email clients will need to change.

## [What defenders should do now](https://www.netcraft.com#what-defenders-should-do-now) 

Going forward, it is imperative that email-attached calendar invites are not trusted by default. They are part of the phishing attack surface and are a vector to reach users beyond typical phishing emails. Security teams may wish to review their default email client settings to ensure that employees who should not expect invites from outside of the organization would not have those automatically added to their calendars. For employees who expect meetings from outside of the organization, it is recommended to update phishing guidance to reflect this risk.

Netcraft’s scanning includes analysis of ICS files, and we are continuing to monitor this tactic’s evolution and increasing use.

### Affected email clients

| **Email Client/Calendar** | **Does the event automatically show up in the calendar** | **Is the event noted as tentative or pending by default?** | **Do events remain after the email is deleted?** | 
| **Microsoft Outlook + Exchange Online**  | Yes | Yes | Yes | 
| **Outlook on the Web + Exchange Online** | Yes | Yes | Yes | 
| **Outlook Mobile (iOS/Android)** | Yes, through Exchange synchronization | Yes | Yes | 
| **Gmail with Google Calendar** | Yes | Yes | Yes | 
| **Google Calendar App (iOS/Android)** | Yes, following the Google account’s settings | Yes | Yes | 
| **Apple Mail + Apple Calendar  (iCloud)** | No | N/A | Yes | 
| **Apple Calendar + Exchange Online** | Yes (often inherits Exchange server settings) | Usually, if processed by Exchange | Yes |
