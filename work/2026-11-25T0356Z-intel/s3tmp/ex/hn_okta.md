---
title: Okta Links ShinyHunters-Associated Vishing Group to New INCEPTION Data Leak Site
author: The Hacker News
url: https://thehackernews.com/2026/11/okta-links-shinyhunters-associated.html
hostname: thehackernews.com
description: Okta links an active vishing cluster previously associated with ShinyHunters to the INCEPTION leak site, but its operators remain unconfirmed.
sitename: The Hacker News
date: "2026-11-24"
categories: ['Article']
tags: ['Cybercrime', 'Data Extortion', 'Identity Security', 'Phishing', 'ShinyHunters', 'Social Engineering']
fingerprint: c90820530830e7ed
language: en
image: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjete6dy8Fmd7sbjqKI5GKSySXkcnz4NF__irfVMBHzgRIDUnpGHtvRIbCywZYYsoKsnMdPhvanoXcnXbYvZpMjL2lL6d_F9a4ErEaI5rH_boPedH_ru2Ush9wonb8tYhGNVM6M_01DTue1THY7uGMbuKBJKNgMbrACkxHCGJiJylHWoxkkpCXNr2Z_CIdf/s1700-nu-rw-lo-l85-e365/leaks.jpg
pagetype: article
filedate: "2026-11-25"
---
A threat cluster previously assessed to be affiliated with the [ShinyHunters](https://thehackernews.com/2026/09/shinyhunters-claims-fbi-breach-says-it.html) extortion crew may have rebranded and continued operations under a new name called [INCEPTION](https://ransomware.live/group/Inception), according to Okta's Threat Intelligence team.

The cluster, dubbed **O-UNC-053**, is characterized by the use of [voice phishing](https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html) (aka vishing) attacks to trick targets into entering credentials in phishing pages and approving multi-factor authentication (MFA). Okta said it's been tracking the group since March 2026.

The identity and access management provider said targets of this cluster previously had stolen data published to the ShinyHunters data leak site (DLS). However, as of November 16, 2026, a new data leak site operating under the name INCEPTION has listed the data siphoned from O-UNC-053 targets.

"While this threat cluster has changed their brand affiliation, the operators remain active in targeting organizations with voice phishing attacks and account takeovers resulting in data theft and extortion," Okta researchers Moussa Diallo and Katie Nickels [said](https://www.okta.com/blog/threat-intelligence/former_shinyhunters_cluster_moves_to_new_inception_site/) in a report shared with The Hacker News.

Social engineering and credential harvesting attacks mounted by O-UNC-053 have targeted a broad range of sectors, including technology, healthcare, biotechnology, financial services, insurance, entertainment, gaming, retail, transportation, hospitality, and legal.

Similar to [O-UNC-066](https://thehackernews.com/2026/07/hackers-use-fake-microsoft-entra.html) and [UNC6671](https://thehackernews.com/2026/08/unc6671-vishing-attacks-target-personal.html), the newly identified cluster also relies on a phishing kit to intercept authentication flows and capture a user's credentials and MFA codes. However, the kit is not designed to bypass phishing-resistant methods like passkeys and Okta FastPass.


"While interacting with targeted users on the phone, the operators socially engineer them into sharing factors like one-time passcodes and approving push notifications," Okta said. "If successful, the operators gain access to SaaS applications and exfiltrate sensitive data, which is often used to extort targets under the threat of releasing it on a data leak site."

Domains created by the group are registered through NiceNIC, Spaceship, Tucows, and NameSilo, with the domain names using the following patterns -

- legal-\<target>\[.\]com
- legaldept-\<target>\[.\]com
- \<target>\[.\]legal
- \<target>-legal\[.\]com

The use of "legal" themes in these attacks is said to have started in October 2026, and is often registered on or within a day of a campaign starting. Prior campaign waves have employed help desk-, support-, and claims-related themes for the registered domains.

These findings also dovetail with an [alert](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-11-23-Legal-themed-vishing-activity.txt) from Palo Alto Networks Unit 42, which has warned of widespread vishing activity using legal-themed domains that either begin with "legal-" or end with "-legal" using the ".com" top-level domain.

More than 70 such domains have been observed since October 2026, it said, adding each domain is specifically created for an intended target operating in different industries, like cryptocurrency, financial services, healthcare, high technology, and hospitality, among others.

"Registered in rapid evening batches and shielded behind Cloudflare, these web-only domains deploy a filtered kit that delivers tailored content to intended victims while routing visitors it is not configured to attack to the targeted organization's legitimate Okta or NetIQ sign-in flow," ReversingLabs researcher Robert Simmons [said](https://www.reversinglabs.com/blog/threat-researchers-notebook-sso-vishing-campaign-associated-with-emerging-inception-extortion-group#iocs).

Some of the confirmed domains linked to the activity are listed below -

- legal-pepsico\[.\]com
- legal-paychex\[.\]com
- legal-duolingo\[.\]com
- activisionblizzard-legal\[.\]com
- legal-westernunion\[.\]com
- legal-dropbox\[.\]com
- legal-indeed\[.\]com
- legal-creditkarma\[.\]com
- legal-amd\[.\]com
- legal-grubhub\[.\]com
- legal-twitch\[.\]tv

The crux of the campaign is to tailor the landing page to the specific identity provider of the target, while filtering unwanted visitors and forwarding them to the organization's authentication infrastructure, such as Okta.

"Throughout our tracking of O-UNC-053 between March and September 2026, we observed the names of targeted entities appear on the ShinyHunters DLS between 1 and 28 days after the phishing infrastructure was registered," Okta noted.

However, it's unclear at this stage if the published data on the INCEPTION site is authentic and whether they are running the site themselves or are collaborating with another extortion gang. The exact nature of the relationship between ShinyHunters and O-UNC-053 is also unknown.

It's worth noting that the [ShinyHunters data leak site went offline](https://www.reuters.com/legal/government/shinyhunters-website-goes-offline-after-fbi-deadline-expires-2026-09-30/) in late September 2026 following the [arrest of three alleged members](https://thehackernews.com/2026/10/weekly-recap-helpdesk-0-days-rogue.html) of the group, including a Canadian co-conspirator responsible for the breach of the FBIjobs.gov portal.

There is no evidence of data from O-UNC-053 targets being published on any data leak site from early September 2026 through October and early November 2026, until [listings](https://ransomware.live/group/Inception#victims) for multiple targets [appeared](https://x.com/AlvieriD/status/2123334961822417407) on the INCEPTION site last week.

"This gap in publishing on any leak site followed by publishing on a new data leak site with a new brand is consistent with prior shifts from [Com](https://thehackernews.com/2025/11/a-cybercrime-merger-like-no-other.html)-affiliated actors," Okta said. "Regardless of the nature of the relationship with the INCEPTION DLS, O-UNC-053 remains active in conducting vishing attacks against targets in an effort to take over accounts, steal data, and extort targets."

### INCEPTION Denies ShinyHunters Link

In a post on their dark web site, INCEPTION has denied any affiliation with ShinyHunters, insisting that it operates independently with its own members and objectives.

"We are not ShinyHunters. We were never ShinyHunters. We are INCEPTION," the group said, adding "certain parties in the threat intelligence industry have been eager to give us a history we never asked for."

"We are also not copying anyone. If our methodology resembles what came before, it is because we took inspiration from operators who, whatever else may be said of them, understood that the weakest component of any secure system is a human being holding a phone. That is not theft of tradecraft. It is acknowledgment of a good idea -- the same way every group after LockBit used a leak site, and nobody called them LockBit."

*(The story was updated after publication to include a statement posted by INCEPTION on its dark web site.)*

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
