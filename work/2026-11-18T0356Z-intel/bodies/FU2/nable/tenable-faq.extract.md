---
title: "Able2Shell FAQ: N-able N-central Zero-Days and Hotfix 2"
author: Research Special Operations
url: https://www.tenable.com/blog/able2shell-frequently-asked-questions-for-reported-n-able-n-central-zero-day-vulnerabilities
hostname: tenable.com
description: Answers to key questions on Able2Shell, 33 alleged N-able N-central zero-days with public PoCs. N-able's Hotfix 2 fixes seven CVEs, including CVE-2026-125883.
sitename: Tenable®
date: "2026-11-11"
fingerprint: "75b0c19bf566948b"
---
**N-able released a hotfix for N-central that fixes seven CVEs after a researcher published proof-of-concept code for 33 alleged zero-day vulnerabilities. The researcher says one attack chain needs no credentials.**

### Change log

**Update November 16:** Added a note that N-able published network indicators of compromise relevant only to customers who have not disabled the Legacy API.

## **Click here to review the change log history**

**Update November 16:** Added a note that N-able published network indicators of compromise relevant only to customers who have not disabled the Legacy API.

**Update November 12:** Added the researcher’s new exploit claims against Hotfix 2, N-able’s November 12 statements and huntback’s report of cryptocurrency miners on live N-central servers. Updated the Key Takeaways, the exploitation, threat actor, patches, indicators and KEV answers, and the links to the researcher’s write-up after a GitHub account rename.

**November 11:** Original publication.

## Key Takeaways

1. Able2Shell is a set of 33 alleged vulnerabilities in N-able N-central, published with proof-of-concept code. The researcher says one chain lets an unauthenticated attacker run commands on the server. On November 12 (UTC), the researcher published new exploits claimed to work against Hotfix 2, including an unauthenticated chain to root that the researcher says requires the Legacy API to be enabled.
2. Security firms reported exploitation attempts against N-central honeypots after the original disclosure. On November 12, the security firm huntback reported that a newer exploit chain, 4EverAble2Shell, was used to install cryptocurrency miners on 21 live N-central servers it identified, 19 of which reported running Hotfix 2. Separately, N-able’s November 12 update says it has seen no signs of compromise.
3. N-able released N-central 2026.4 Hotfix 2 on November 10. It fixes seven CVEs.

## Background

Tenable's Research Special Operations (RSO) team has compiled this blog to answer Frequently Asked Questions (FAQ) regarding Able2Shell, a set of reported zero-day vulnerabilities in N-able N-central.

## FAQ

**When was Able2Shell first disclosed?**

A researcher operating under the [<u>GitHub</u>](https://github.com/MSPNightmare/CVEs/blob/main/0-Days/N-Central%20N-Able/Able2Shell/README.md) account “Oracle-Security,” since renamed “MSPNightmare,” published a write-up titled “Able2Shell” in the account’s CVEs repository. It describes 33 alleged N-central vulnerabilities with proof-of-concept code. The earliest README commit is dated November 9, 2026 at 04:14 UTC. N-able described the [<u>release</u>](https://uptime.n-able.com/) as a public disclosure by an independent security researcher. N-able does not state whether it was notified in advance and does not name the researcher.

**What are the vulnerabilities associated with Able2Shell?**

On November 10, N-able published seven CVE records for vulnerabilities fixed in N-central 2026.4 Hotfix 2. On its status page, N-able says the release addresses “the most critical November 9 vulnerabilities” and that a follow-up hotfix will provide further security updates. The page lists all seven as related CVEs. One, [<u>CVE-2026-91000</u>](https://www.tenable.com/cve/CVE-2026-91000), had been reserved on September 14, before the public Able2Shell disclosure.

| **CVE** | **Description (per N-able)** | **CVSSv4** | 
|---|---|---|
| [<u>CVE-2026-125883</u>](https://www.tenable.com/cve/CVE-2026-125883) | Multiple XML external entity (XXE) vulnerabilities | 9.3 | 
| [<u>CVE-2026-125881</u>](https://www.tenable.com/cve/CVE-2026-125881) | Schema-hint server-side request forgery (SSRF) via service import schema validation | 9.3 | 
| [<u>CVE-2026-125878</u>](https://www.tenable.com/cve/CVE-2026-125878) | Multiple OGNL injection vulnerabilities | 8.7 | 
| [<u>CVE-2026-125879</u>](https://www.tenable.com/cve/CVE-2026-125879) | Local privilege escalation to root via nable-writable syslog-ng config | 8.6 | 
| [<u>CVE-2026-125882</u>](https://www.tenable.com/cve/CVE-2026-125882) | Remote code execution via file repository upload path traversal | 8.6 | 
| [<u>CVE-2026-91000</u>](https://www.tenable.com/cve/CVE-2026-91000) | Insecure IPC channels lead to local privilege escalation | 8.4 | 
| [<u>CVE-2026-125880</u>](https://www.tenable.com/cve/CVE-2026-125880) | Stored cross-site scripting (XSS) via MMS3 patch metadata (admin context) | 8.3 | 

N-able’s CVE titles match several finding types in the researcher’s README, but N-able has not said which of the 33 findings each CVE addresses. N-able credits CVE-2026-125882 to Nate Fair of Sprocket Security, and a file repository path traversal also appears in the README.

**Is Able2Shell one vulnerability or several?**

Several. The README lists 33 findings, and some of them are steps in longer exploit chains built from other entries on the same list. The researcher lists four exploit chains. The rest are standalone findings.

| **Chain** | **Login needed** | **Reaches** | 
|---|---|---|
| Service import XXE | None | Commands as the nable account | 
| MMS3 stored XSS to OGNL execution | None to plant, but an administrator has to view it | Commands as the nable account | 
| MMS3 stored XSS to Audit Export | None to plant, but an administrator has to view it | Commands as root | 
| SIS file path traversal to syslog installer | Yes | Commands as root | 

The researcher describes the XXE chain as credential-free, and N-able's record for CVE-2026-125883 lists no privileges and no user interaction as required. The researcher’s proof-of-concept takes several identifiers as inputs, and other findings in the README describe anonymous ways to obtain some of them. The XXE step has the appliance fetch a file from an attacker-hosted server. For the MMS3 chains, the researcher says an unauthenticated attacker can plant the script, which runs when a logged-in administrator views the poisoned patch details. N-able’s record for CVE-2026-125880 lists high privileges and active user interaction.

**How severe is Able2Shell?**

Two of the four chains reach root: MMS3 stored XSS to Audit Export, and SIS path traversal to syslog. The XXE chain runs commands as the nable account (uid 992), and the researcher’s proof-of-concept can also create an administrator account. N-able’s CVSSv4 scores for the seven CVEs range from 8.3 to 9.3, and N-able calls Hotfix 2 a critical security update.

**Has N-able confirmed the findings?**

N-able has published seven CVEs and a hotfix, but it has not mapped its CVEs to the researcher’s 33 findings or commented on them individually. Before the hotfix, N-able said it was responding to the public disclosure of critical vulnerabilities in N-central by an independent security researcher.

On November 12, N-able said it is investigating the new claims. In that first notice, N-able said: “Based on our initial review, the server issue described depends on a non-default configuration in which the Legacy API is turned on and exposed to the public internet.” In a [<u>later November 12 update</u>](https://uptime.n-able.com/event/202613/), N-able said it is “restricting certain N-central features and integrations” as a precaution while it develops additional remediation. N-able has not yet published findings on the new claims.

**Which versions are affected?**

N-able's CVE records list N-central versions before 26.4.1 as affected (the record for CVE-2026-91000 writes this as 2026.4.1), and the fixed build is 2026.4.1.26. The researcher says all testing was done on N-central Appliance 2026.4.0.31, which the researcher describes as a pre-release build, and that "most if not all vulnerabilities should work on previous versions."

**Is the hosted N-central service affected?**

N-able took its hosted N-central environments offline as a precaution after the disclosure, and its status page lists hosted N-central in the Americas, APAC and Europe among the affected services. On November 10, N-able said all hosted N-central servers across all global regions had been upgraded to the new release. Hosted customers still upgrade their own Agents and Probes.

**Has Able2Shell been exploited in the wild?**

N-able's status page says it is observing “scanning activity associated with the published proof-of-concept code.” Huntress reported N-able’s statement that it had no evidence that any customer environment had been successfully exploited, and said on November 10 that it had not observed evidence of Able2Shell exploitation in its partners’ environments.

[<u>Beazley Security Labs</u>](https://labs.beazley.security/advisories/BSL-A1242) updated its November 9 advisory on November 10 with watchTowr’s report of exploitation attempts against its N-central honeypots. In that November 10 update, Beazley Security Labs said a confirmed compromise of a customer server “has not been reported.”

[<u>Previdian</u>](https://blog.previdian.com/n-able-n-central-critical-vulnerabilities-what-we-know-so-far/) reports exploitation attempts against its N-central decoy environment, not confirmed compromise. Its decoys recorded 68 events from one source IP address starting on November 9, including XXE and sensitive-file access attempts. Previdian says these do not show a completed account takeover or command execution, or a full replay of the published chain.

On November 12, [<u>huntback</u>](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers) reported that one operator used the 4EverAble2Shell chain against live N-central servers to install an XMRig Monero miner. Huntback says the operator’s source IP address first probed its N-central decoys at 08:30 UTC and sent the full chain at 09:16 UTC. At 12:50 UTC, huntback says, the operator’s public mining pool account listed 21 active miners labeled “nc\_” plus an IP address.

Huntback says all 21 addresses serve N-central’s web interface and 19 report build 2026.4.1.26 (Hotfix 2). Huntback has not published the affected addresses and does not say whether the Legacy API was enabled on those servers. Previdian told [<u>BleepingComputer</u>](https://www.bleepingcomputer.com/news/security/new-n-able-4everable2shell-zero-day-exploited-hours-after-poc-released/) that attackers attempted the full chain against its N-central honeypot, and BleepingComputer reports that the attacking IP address matched the one huntback observed.

Huntress said in a November 12 update, posted before huntback’s report, that it had not observed exploitation of the new issues in its partners’ environments. Separately, N-able’s November 12 update says it has seen no signs of compromise.

**Which threat actors are exploiting Able2Shell?**

No named threat actor has been linked to Able2Shell or 4EverAble2Shell activity as of November 12. Huntback attributes the November 12 miner installations to one operator and says the same mining wallet lists miners named for several other products, which it says shows what else the operator exploits.

**Is there a proof-of-concept (PoC) available?**

Yes. The researcher’s README includes Python proof-of-concept code for the alleged vulnerabilities, tested against N-central Appliance 2026.4.0.31.

On November 12 (UTC), the researcher published two more sets of exploits claimed to work against Hotfix 2 (2026.4.1.26). The researcher describes [<u>4EverAble2Shell</u>](https://github.com/MSPNightmare/CVEs/blob/main/0-Days/N-Central%20N-Able/4EverAble2Shell/README.md) as an unauthenticated chain to root on the N-central server, and later added that it requires the Legacy API to be enabled. [<u>Agent2Shell</u>](https://github.com/MSPNightmare/CVEs/blob/main/0-Days/N-Central%20N-Able/Agent2Shell/README.md) contains chains that the researcher says target Windows Agents and Probes, and the researcher says an attacker may have to obtain appliance IDs first. Huntress says it has not yet confirmed whether the Agent2Shell chains also depend on the Legacy API.

**How does this relate to earlier N-central vulnerabilities?**

Able2Shell is a newly disclosed set of vulnerabilities, and it is not known whether any relate to earlier N-central flaws. None of the seven CVEs fixed in Hotfix 2 is in CISA’s Known Exploited Vulnerabilities (KEV) catalog as of November 12. Five earlier N-central CVEs are in the KEV catalog:

| **CVE** | **Description** | **Date Added to KEV** | 
|---|---|---|
| [<u>CVE-2026-86218</u>](https://www.tenable.com/cve/CVE-2026-86218) | Static code injection | September 8, 2026 | 
| [<u>CVE-2026-18556</u>](https://www.tenable.com/cve/CVE-2026-18556) | Authentication bypass | August 4, 2026 | 
| [<u>CVE-2026-18577</u>](https://www.tenable.com/cve/CVE-2026-18577) | Authentication bypass | August 3, 2026 | 
| [<u>CVE-2025-8876</u>](https://www.tenable.com/cve/CVE-2025-8876) | Command injection | August 13, 2025 | 
| [<u>CVE-2025-8875</u>](https://www.tenable.com/cve/CVE-2025-8875) | Insecure deserialization | August 13, 2025 | 

**Are patches or mitigations available?**

Yes. On November 10, N-able released N-central 2026.4 Hotfix 2 (build 2026.4.1.26), which fixes the seven CVEs above. According to N-able, on-premises customers upgrade their own servers, while N-able upgrades hosted servers. All customers also upgrade their Agents and Probes, Agents first, because an upgraded Probe cannot communicate with Agents that have not been upgraded. Until an on-premises server is upgraded, N-able recommends keeping it offline. A follow-up hotfix with further security updates is also planned. N-able has not yet released a fix for the November 12 claims and says it is developing additional remediation. In its [<u>November 12 update</u>](https://uptime.n-able.com/event/202613/), N-able says it has turned off the Intune integration in hosted environments and has temporarily deactivated it for on-premises customers running it, and that its support team will contact any on-premises customer where it could not do so. It tells on-premises customers to make sure the Legacy API is turned off in their environment, which N-able says is the default setting.

Hotfix 2 removes legacy mobile device management (MDM). The release notes list N-central’s built-in remote control as temporarily disabled, while Take Control continues to work.

**Are there indicators of compromise?**

Yes. On November 13, N-able [published network indicators of compromise](https://uptime.n-able.com/event/202613/) relevant only to customers who have not disabled the Legacy API. While there are no host-level indicators, they cover download URLs and outbound connections. Huntback separately published host artifacts, including file paths and persistence mechanisms, for the November 12 miner activity. For the original Able2Shell chains, Beazley Security Labs lists reported source IP addresses and the targeted SOAP endpoint, and Huntress recommends reviewing login and authentication activity from November 8 onward, including remote access sessions, new scripts and unauthorized administrator accounts.

**Has Tenable released product coverage?**

A list of Tenable plugins for these vulnerabilities can be found on the individual CVE pages:

This list may contain plugins released after this blog’s publication.

**Has Tenable classified any of these vulnerabilities under Vulnerability Watch?**

Yes. Tenable has classified CVE-2026-125883 as a Vulnerability of Interest (VOI) under [Vulnerability Watch](https://www.tenable.com/blog/reducing-remediation-time-remains-a-challenge-how-tenable-vulnerability-watch-can-help). CVE-2026-125878, CVE-2026-125881 and CVE-2026-125882 are each classified as a Vulnerability Being Monitored (VBM).

### Get more information

## Learn more

- Exposure Management
- Vulnerability Management

Tenable One

## Request a demo

The world’s leading AI-powered exposure management platform.

## Thank You

Thank you for your interest in Tenable One.

A representative will be in touch soon.

Debug:
Form ID: 7469
Form Name: one-eval

Form Class: c-form form-panel\_\_global-form c-form--mkto js-mkto-no-css js-form-hanging-label c-form--hide-comments

Form Wrapper ID: one-eval-form-wrapper

Confirmation Class: one-eval-confirmform-modal

Simulate Success
