Title: Overview of data investigation

URL Source: https://csirt.divd.nl/DIVD-2026-00014/overview_data_investigation/

Published Time: Fri, 02 Oct 2026 08:30:33 GMT

Markdown Content:
On Monday 21 September 2026, the servers in our data center got compromised. We are now in incident response mode. True to DIVD fashion this incident got its own DIVD case number: [DIVD-2026-00014](https://csirt.divd.nl/cases/DIVD-2026-00014) with the title: When not if… Because let’s be honest, in security it was never a question of if.

## TL;DR

We’ll update this page often, so to save you from reading this wall of text every time, here’s the TL;DR.

We got hacked, and data was compromised and possibly exfiltrated. We don’t have the full picture yet, because we’re still in full investigation mode. We chose full transparency, which means that we also communicate about the things we don’t know. Questions regarding data can be sent to [dpo@divd.nl](mailto:dpo@divd.nl?subject=Data%20status%20inquiry%20DIVD%20hack). All other questions can go to [communications@divd.nl](mailto:communications@divd.nl?subject=Quewstion%20about%20DIVD%20breach).

## No salami tactics here

We believe open and honest communication about hacks is vital for a resilient digital society. The GDPR (the AVG, for the Dutch among us) backs this up by requiring that people whose personal data has leaked are notified “without undue delay”. It doesn’t say “when the PR team feels ready”. Too often we see this kind of news come out through the [salami tactic](https://en.wikipedia.org/wiki/Salami_slicing_tactics). Serving the whole sausage at once could raise a lot of worries and stomach aches, so organisations cut it into thin slices, hoping each one feels less painful, does less damage to their reputation and can easily be eaten up without stomach ache.

This is not the way.

Below you’ll find every type of data we hold, personal (PII) and non-personal, with an update on the investigation status. That includes the things we don’t know yet. This page will be updated as soon as we know more.

## What data is listed here

It was quite a puzzle to figure out what data we should and shouldn’t list here. We want this overview to honest, but not overly long or complicated. The data listed below is data that we feel needs to be investigated to determine if it was compromised by our attacker. This means that this is data if valuable to them, or poses a risk to others if compromised.

Beware that: a) This is not a definite list of all data we have b) The fact that this data is listed alone here does NOT mean it is compromised

Per catagory of data we have listed a Investigation status, Preliminary Analysis and Final Assessment. There three columns indicate the status of the investigation and the status of the data.

A dash (-) means no input yet.

## Data about volunteers

Our volunteers are our favorite humans, that’s why we start here. Without volunteers, DIVD would not be possible. We try to keep as little data about them as possible, but lots of little things still add up.

## Status

| Data | Description | Investigation status | Preliminary Analysis | Final assessment |
| --- | --- | --- | --- | --- |
| Our office environment in GSuite | - | Ongoing | - | - |
| Our HR environment | - | Ongoing | - | - |
| Our IT support systems including our helpdesk | - | Ongoing | - | - |
| Our project support environment, including Jira and Confluence | Project support, including Jira and Confluence. | Ongoing | Signs of compromise of the system | - |
| System data on IT systems that support our operations | - | Ongoing | Signs of compromise of the system | - |
| Source code in (hidden) repos in public GitHub and internal GitLab | Source code in GitHub and internal GitLab. | Ongoing | - | - |
| Internal communication via Slack | - | Ongoing | - | - |

## Current picture

We know for sure that user data (DIVD email addresses) and possibly contact details of volunteers were exfiltrated, and we’re still investigating exactly which data of which volunteers is affected. For DIVD volunteers (and others) this means a higher risk of social engineering, because this makes it easier for someone to pose as a DIVD’er.

## Core business data

Volunteers may be our favorite humans. But the DIVD is there to help everybody. “Everybody deserves a responsible disclosure”, but that means we do have a lot of data about a lot of entities, that is unfortunately sensitive in nature and that is not limited to PII.

## Status

| Data | Description | Investigation status | Preliminary Analysis | Final assessment |
| --- | --- | --- | --- | --- |
| CSIRT tickets system with all conversations with csirt@divd.nl and *@csirt.divd.nl | - | Ongoing | Signs of compromise of the system | - |
| Lists of vulnerable systems | We are investigating which part of this information is in the CSIRT ticket system. | Ongoing | - | - |
| Fingerprints to identify vulnerable systems | - | Ongoing | - | - |
| “De-weaponised” PoCs | - | Ongoing | - | - |
| Zero day vulnerabilities | We are investigating which part of this information is in the CSIRT ticket system. | Ongoing | - | - |
| Proof of concept attacks | - | Ongoing | - | - |
| Leaked credential dumps | - | Ongoing | - | - |
| Masked leaked credential dumps | We are investigating which part of this information is in the CSIRT ticket system. | Ongoing | - | - |
| Private communication between DIVD researchers and third parties via e.g. mail | - | Ongoing | - | - |

## Current picture

We know for sure that the attackers got in through the ticketing system our CSIRT team uses. That system holds every email sent to the CSIRT mailbox and every reply, but not our initial notifications. We know that the attackers had difficulties extracting information from this system and our environment, that makes that only a part of the information was extracted. If an organisation or individual has been emailing back and forth with our CSIRT team, assume the attackers may have that information. This could be follow-up requests on scan data (including IP addresses of vulnerable systems), vulnerabilities reported to us through the CSIRT mailbox and extracts of credential dumps with masked passwords.

We say ‘assume’ because our setup and security measures meant the attacker had to work for every bit of data they got out. We’re still working out how far the exfiltration went, and that takes time.

## TCB: Taking care of business

Like any organisation we have to pay the rent, answer the telephone and pay an occasional bill and organise ourselves. This covers the administration, accounting and bank account we need to run DIVD.

## Status

| Data | Description | Investigation status | Preliminary Analysis | Final assessment |
| --- | --- | --- | --- | --- |
| Our administration in our GSuite | - | Ongoing | - | - |
| Our accounting systems | Handled via an external party. | Not under investigation | No signs found so far | - |
| Our bank account | Handled via an external party. | Not under investigation | No signs found so far | - |

## Current picture

Our accounting systems and bank account are handled via an external party, and we have no indications of compromise there. Our administration in GSuite is still under investigation.

Links/Buttons:
- [Skip to the content.](https://csirt.divd.nl/#content)
- [Home](https://csirt.divd.nl/)
- [Cases](https://csirt.divd.nl/cases/)
- [DIVD](https://www.divd.nl/)
- [DIVD-2026-00015 - Vulnerabilities in Zammad during investigation of case DI Multiple vulnerabilities found in Zammad including a Undisclosed RCE in Zam...](https://csirt.divd.nl/cases/DIVD-2026-00015/)
- [DIVD-2026-00014 - When, not if... DIVD got hacked through AI agents....](https://csirt.divd.nl/cases/DIVD-2026-00014/)
- [DIVD-2026-00012 - MikroTik RouterOS MikroTrick vulnerabilities Multiple vulnerabilities in MikroTik RouterOS can be combined to obtain una...](https://csirt.divd.nl/cases/DIVD-2026-00012/)
- [DIVD-2026-00010 - Improper Access Control in Hashtopolis Server An improper access control vulnerability in the Hashtopolis server chunk ac...](https://csirt.divd.nl/cases/DIVD-2026-00010/)
- [DIVD-2026-00007 - Victim Notification Operation Endgame - S03E03 & S03E04 The DIVD is notifying victims of the SocGholish malware and the StealC and ...](https://csirt.divd.nl/cases/DIVD-2026-00007/)
- [DIVD-2026-00006 - Vulnerability found in DIVD App VerySecureApp The VerySecureApp made by DIVD using Mendix Studio Pro 11.8.0 Beta allows u...](https://csirt.divd.nl/cases/DIVD-2026-00006/)
- [DIVD-2026-00005 - Salesforce Experience Cloud – Data Exposure via Misconfig DIVD is researching Salesforce Experience Cloud applications exposing sensi...](https://csirt.divd.nl/cases/DIVD-2026-00005/)
- [DIVD-2026-00003 - Mendix Applications – Data Exposure due to Authorization DIVD is researching Mendix applications exposing sensitive data due to auth...](https://csirt.divd.nl/cases/DIVD-2026-00003/)
- [DIVD-2026-00002 - DIVD-2026-00002 – Ivanti Endpoint Manager Mobile Vulnerab Two critical vulnerabilities in Ivanti Endpoint Manager Mobile allow unauth...](https://csirt.divd.nl/cases/DIVD-2026-00002/)
- [DIVD-2026-00001 - DIVD-2026-00001 – EVbee Service App and DC Quick Charging Multiple vulnerabilities in EVbee Service App and DC Quick Charging Station...](https://csirt.divd.nl/cases/DIVD-2026-00001/)
- [DIVD-2025-00042 - React2shell vulnerability A vulnerability in React Server components allow unauthorized access via Re...](https://csirt.divd.nl/cases/DIVD-2025-00042/)
- [DIVD-2025-00041 - Victim Notification Operation Endgame S03E01 DIVD is notifying victims of the various infostealer malware strains from i...](https://csirt.divd.nl/cases/DIVD-2025-00041/)
- [DIVD-2025-00040 - Oracle E-Business Suite Vulnerabilities Vulnerability in the Oracle Concurrent Processing product of Oracle E-Busin...](https://csirt.divd.nl/cases/DIVD-2025-00040/)
- [DIVD-2025-00039 - Cisco ASA WebVPN Vulnerabilities Multiple vulnerabilities in Cisco ASA WebVPN could allow attackers to bypas...](https://csirt.divd.nl/cases/DIVD-2025-00039/)
- [DIVD-2025-00038 - Found webshells in FreePBX due to RCE vulnerability FreePBX has assigned CVE-2025-57819 to vulnerabilities in its administrator...](https://csirt.divd.nl/cases/DIVD-2025-00038/)
- [DIVD-2025-00037 - Critical vulnerabilities in Citrix ADC and Gateway system Citrix has released security updates for vulnerabilities in NetScaler ADC a...](https://csirt.divd.nl/cases/DIVD-2025-00037/)
- [DIVD-2025-00035 - Sharepoint Mass-Exploitation (ToolShell) through CVE-2025 Threat actors are targeting Sharepoint installations with CVE-2025-53770. I...](https://csirt.divd.nl/cases/DIVD-2025-00035/)
- [DIVD-2025-00034 - Remote Code Execution in IBM WebSphere version 8.5 and 9. A critical vulnerability in IBM WebSphere was discovered in versions 8.5 an...](https://csirt.divd.nl/cases/DIVD-2025-00034/)
- [DIVD-2025-00033 - Remote Code Execution in GeoServer versions below 2.27.0, A critical vulnerability in GeoServer was discovered in versions below 2.27...](https://csirt.divd.nl/cases/DIVD-2025-00033/)
- [DIVD-2025-00032 - Unauthenticated Arbitrary Remote Code Execution in Pterod A critical vulnerability in Pterodactyl was discovered in versions below 1....](https://csirt.divd.nl/cases/DIVD-2025-00032/)
- [CVEs](https://csirt.divd.nl/cves/)
- [CVE-2026-22104 - Improper access control in Hashtopolis server chunk activity...](https://csirt.divd.nl/cves/CVE-2026-22104/)
- [CVE-2026-22103 - Command injection in NPC start web endpoint...](https://csirt.divd.nl/cves/CVE-2026-22103/)
- [CVE-2026-22102 - Arbitrary file overwrite through certificate update function...](https://csirt.divd.nl/cves/CVE-2026-22102/)
- [CVE-2026-22101 - Sensitive information leak through hidden menu...](https://csirt.divd.nl/cves/CVE-2026-22101/)
- [CVE-2026-22100 - Comnand injection in OCPP ReserveLogin message...](https://csirt.divd.nl/cves/CVE-2026-22100/)
- [CVE-2026-22099 - Missing authentication for Bluetooth communication...](https://csirt.divd.nl/cves/CVE-2026-22099/)
- [CVE-2026-22098 - Sensitive information is written to logs...](https://csirt.divd.nl/cves/CVE-2026-22098/)
- [CVE-2026-22097 - Missing firmware validation allows remote code execution...](https://csirt.divd.nl/cves/CVE-2026-22097/)
- [CVE-2026-22096 - Missing authentication for webserver endpoints...](https://csirt.divd.nl/cves/CVE-2026-22096/)
- [CVE-2026-22095 - Command injection in diagnosis web endpoint...](https://csirt.divd.nl/cves/CVE-2026-22095/)
- [CNA](https://csirt.divd.nl/cna/)
- [Stolen credentials](https://csirt.divd.nl/credentials/)
- [Blog](https://csirt.divd.nl/blog/)
- [2026-09-24 : It was a matter of when, not if......](https://csirt.divd.nl/2026/09/24/when-not-if/)
- [2026-08-19 : Sungrow web portal full disclosure...](https://csirt.divd.nl/2026/08/19/Sungrow-web-portal/)
- [2026-07-31 : CyberAuditWeb and videx-legacy-ssl full disclosure...](https://csirt.divd.nl/2026/07/31/full-disclosure-cyberauditweb/)
- [2026-07-30 : Visioweb.js...](https://csirt.divd.nl/2026/07/30/visioweb-full-disclosure/)
- [2026-07-30 : Cloudflow...](https://csirt.divd.nl/2026/07/30/cloudflow-full-disclosure/)
- [2026-07-27 : Six vulnerabilities in Enphase IQ Gateway devices...](https://csirt.divd.nl/2026/07/27/enphase-iq-gateway-full-disclosure/)
- [2026-07-17 : White Rabbit Switch full disclosure...](https://csirt.divd.nl/2026/07/17/DIVD-2022-00068-full-disclosure/)
- [2026-07-17 : Axiell Iguana CMS full disclosure...](https://csirt.divd.nl/2026/07/17/DIVD-2022-00064-full-disclosure/)
- [2026-07-16 : Mennekes Smart - charging stations full disclosure...](https://csirt.divd.nl/2026/07/16/mennekes-smart-full-disclosure/)
- [2026-07-16 : SOPlanning Online Planning tool full disclosure...](https://csirt.divd.nl/2026/07/16/DIVD-2024-00024-full-disclosure-v1/)
- [More...](https://csirt.divd.nl/blog)
- [Donate](https://www.divd.nl/donate/)
- [Search...](https://csirt.divd.nl/search/)
- [RSS](https://csirt.divd.nl/feed.xml)
- [Contact](https://csirt.divd.nl/contact/)
- [DIVD-2026-00014](https://csirt.divd.nl/cases/DIVD-2026-00014)
- [dpo@divd.nl](mailto:dpo@divd.nl?subject=Data%20status%20inquiry%20DIVD%20hack)
- [communications@divd.nl](mailto:communications@divd.nl?subject=Quewstion%20about%20DIVD%20breach)
- [salami tactic](https://en.wikipedia.org/wiki/Salami_slicing_tactics)
- [Twitter](https://twitter.com/DIVDnl)
- [LinkedIn](https://www.linkedin.com/company/divd-nl)
