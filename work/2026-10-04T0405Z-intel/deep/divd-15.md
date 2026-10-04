Title: DIVD-2026-00015 - Vulnerabilities in Zammad during investigation of case DIVD-2026-00014

URL Source: https://csirt.divd.nl/DIVD-2026-00015/

Published Time: Fri, 02 Oct 2026 08:30:33 GMT

Markdown Content:
Our reference[DIVD-2026-00015](https://csirt.divd.nl/cases/DIVD-2026-00015)
Case lead[Victor Pasman](https://www.divd.nl/who-we-are/team/people/victor-pasman/)
Researcher(s)*    Earth Grob (Merlon Security) 
*    Luke Paris (Merlon Security) 
*    Tijmen van der Spijk (Merlon Security) 
*    Zohar Cochavi (Merlon Security) 
*    Alje Woltjer (Merlon Security) 
*    Mischa Rick van Geelen (DIVD) 
*    Ralph Horn (DIVD) 
*    Max van der Horst (DIVD) 
*    Frank Breedijk (DIVD) 
*    Davy Aarts (DIVD)
CVE(s)*   [CVE-2026-102489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-102489)
*   [CVE-2026-102490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-102490)
Products*   Zammad
Versions*   Zammad versions 6.3.0 to 6.5.4 for the RCE in Zammad.
*   Zammad version 7.0.0 to version 7.1.3 for the RCE in Zammad, not exploitable due to environments conditions.
*   Zammad version v1.5.0 to v7.1.0-alpha for the LPE vulnerability.
Recommendation Upgrade to Zammad version 7.
Patch status Available
Workaround N/A
Status Open
Last modified 01 Oct 2026 13:27 CEST

## Summary

During the investigation of case DIVD-2026-00014, two new CVEs were identified.

*   CVE-2026-102489 - Zammad versions 6.3.0 to 6.5.4 are vulnerable a session hijack vulnerability that leads to remote code execution as the zammad user. The vulnerability is also present in version 7.0.0 to version 7.1.3, but not exploitable due to environment conditions.
*   CVE-2026-102490 - In all versions of Zammad including the latest alpha has an vulnerability which enables the local zammad user to escalate privileges to root.

## What you can do

We advise all users of Zammad to upgrade to version 7 of Zammad or to take it offline. If you want to investigate whether you have been compromised based on our IoCs, you can download our [log check script](https://csirt.divd.nl/downloads/DIVD-2026-00015/cve-2026-102489_ioc_check_script_v2.sh) to check your Zammad logfiles for Indicators of Compromise.

## What we are doing

DIVD is actively scanning and alerting owners of vulnerable Zammad instances. We have reported the vulnerability to Zammad who are working on a fix.

## Timeline

| Date | Description |
| --- | --- |
| 21 Sep 2026 | Vulnerability abused to breach DIVD |
| 22 Sep 2026- 23 Sep 2026 | Vulnerability analysed and reproduced by DIVD team |
| 24 Sep 2026 | Vulnerability reported to Zammad. |
| 26 Sep 2026 | DIVD scanned for publicly available and vulnerable Zammad instances. |
| 26 Sep 2026 | DIVD created a limited disclosure for CVE-2026-102489 & CVE-2026-102490. |
| 26 Sep 2026 | DIVD started notifying owners of vulnerable instances. |

gantt title DIVD-2026-00015 - Vulnerabilities in Zammad during investigation of case DIVD-2026-00014 dateFormat YYYY-MM-DD axisFormat %e %b %Y section Case DIVD-2026-00015 - Vulnerabilities in Zammad during investigation of case DIVD-2026-00014 (still open) :2026-09-24, 2026-10-09 section Events Vulnerability abused to breach DIVD : milestone, 2026-09-21, 0d Vulnerability analysed and reproduced by DIVD team (1 days) : 2026-09-22, 2026-09-23 Vulnerability reported to Zammad. : milestone, 2026-09-24, 0d DIVD scanned for publicly available and vulnerable Zammad instances. : milestone, 2026-09-26, 0d DIVD created a limited disclosure for CVE-2026-102489 & CVE-2026-102490. : milestone, 2026-09-26, 0d DIVD started notifying owners of vulnerable instances. : milestone, 2026-09-26, 0d

## More information

*   [CVE-2026-102489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-102489)
*   [CVE-2026-102490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-102490)

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
- [DIVD-2026-00015](https://csirt.divd.nl/cases/DIVD-2026-00015)
- [Victor Pasman](https://www.divd.nl/who-we-are/team/people/victor-pasman/)
- [CVE-2026-102489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-102489)
- [CVE-2026-102490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-102490)
- [log check script](https://csirt.divd.nl/downloads/DIVD-2026-00015/cve-2026-102489_ioc_check_script_v2.sh)
- [Twitter](https://twitter.com/DIVDnl)
- [LinkedIn](https://www.linkedin.com/company/divd-nl)
