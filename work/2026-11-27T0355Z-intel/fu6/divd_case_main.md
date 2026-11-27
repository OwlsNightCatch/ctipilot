---
title: DIVD-2026-00014 - When, not if…
url: https://csirt.divd.nl/cases/DIVD-2026-00014/
hostname: divd.nl
description: DIVD was hacked in an attack involving AI agents.
sitename: DIVD CSIRT
date: "2026-11-25"
fingerprint: "98a98f99057736ba"
language: en
pagetype: website
filedate: "2026-11-27"
---
# DIVD-2026-00014 - When, not if...

| Our reference | [DIVD-2026-00014](https://csirt.divd.nl/cases/DIVD-2026-00014) | 
| Case lead | DIVD Crisis Management Team | 
| Author | Various | 
| CVE(s) |  | 
| Status | Open | 
| Last modified | 25 Nov 2026 14:10 CET | 

## Summary

DIVD was hacked in an attack involving AI agents. The forensic investigation of the breach has been completed.

## What we know so far

On 21 September 2026, a malicious actor breached the Zammad instance that serves as our ticketing system for communications with csirt@divd.nl and all other email addresses ending in @csirt.divd.nl. The attacker exploited two zero-day vulnerabilities ([CVE-2026-102489](https://csirt.divd.nl/cves/CVE-2026-102489) and [CVE-2026-102490](https://csirt.divd.nl/cves/CVE-2026-102490)), which we have since reported to Zammad through case [DIVD-2026-00015](https://csirt.divd.nl/cases/DIVD-2026-00015). Zammad has fixed both vulnerabilities: the first in release 7.2 and the second in release 7.2.2.

After obtaining root privileges on the system, the attacker used AI agents to continue the attack. Several indicators point to the use of AI agents, most notably:

- The sheer volume of attack activity and the number of artefacts generated in a relatively short period.
- The extensive comments and documentation in the attack scripts, including comments in which the attack agents appear to communicate with one another.

Within minutes of the attack, the first indicators appeared in our monitoring system, and an alert was sent to our SOC volunteers for investigation.

Although the alert arrived quickly, it took us 19 hours to initiate our first response on 22 September 2026. During that response, we formulated a plan to contain the attack.

Executing this plan took a further nine hours. This included travel time to bring the incident response team together at the [Hermit Hive](https://hermithive.nl/), our friendly hackerspace home away from home. It also required careful coordination to ensure that we could isolate our systems in the Amsterdam data centre without cutting off our own network access and preventing the further response actions we knew would be needed.

Since then, we have investigated the incident to determine which data was involved. We have also informed our key partners and reported the breach to the [Dutch Data Protection Authority](https://www.autoriteitpersoonsgegevens.nl/en/about-the-ap) and the [Dutch Cyber Security Center (NCSC-NL)](https://www.ncsc.nl), and, through them, to our regulator under the [Cyberweerbaarheidswet](https://www.rdi.nl/onderwerpen/digitale-weerbaarheid/cyberbeveiligingswet/meldplicht). We have also filed a police report.

To provide as much clarity as possible, we created an [overview page](https://csirt.divd.nl/DIVD-2026-00014/overview_data_investigation/) showing what data we hold, the status of the investigation and which data was affected by the breach.

We wouldn’t be DIVD if we hadn’t launched case [DIVD-2026-00015](https://csirt.divd.nl/cases/DIVD-2026-00015) to warn other Zammad users who could fall victim to the same zero-day vulnerabilities. And yes, since the Zammad 7.x branch was not vulnerable and we were not running it, we had special stickers made to remind ourselves to practise what we preach. Stop yapping, start patching.

## Metrics

We are nerds. Nerds love metrics. Here are metrics.

| Metric | Time (HH:MM:SS) | Explanation | 
|---|---|---|
| Mean Time to Detect (MTTD) | 00:15:11 | Time between first breach and first alert | 
| Mean Time to Acknowledge | 07:20:51 | Time between first alert and SOC pickup | 
| Mean Time to Respond (MTTR) | 19:16:51 | Time between first attack and formal response | 
| Mean Time to Contain (MTTC) | 27:40:51 | Time between first attack and containment of the attack | 

We said we love metrics, but being the perfectionists we are, we see plenty of room for improvement. Then again, looking at the bigger picture, these numbers are not too shabby compared with industry averages, especially for a volunteer-run organisation.

And to give you an impression of the attack, here are some metrics relating to the adversary:

| Metric | Time (HH:MM:SS) / Volume | 
|---|---|
| Time between first probe and first breach | 11:47:20 | 
| Time from first breach to root | 00:19:01 | 
| Probe to root | 12:06:21 | 
| Custom-written payloads recovered | 990 | 
| Output directories created | 228 (excluding subdirectories) | 
| Output files generated and recovered | 3,259 (excluding files in subdirectories) | 

## Public statements

We made a number of public statements about this hack on social media. So many, in fact, that we moved them to the [public statements](https://csirt.divd.nl/DIVD-2026-00014/public_statements_on_hack/) page.

## More information

- Case [DIVD-2026-00015](https://csirt.divd.nl/cases/DIVD-2026-00015) - The case file for the zero-day vulnerabilities in Zammad
- [Overview of the compromise status of our data](https://csirt.divd.nl/DIVD-2026-00014/overview_data_investigation/)
- Overview of [public statements](https://csirt.divd.nl/DIVD-2026-00014/public_statements_on_hack/)
- The [report of the forensic investigation of the hack](https://csirt.divd.nl/DIVD-2026-00014/full_disclosure/)

We will update this page when we have more information.

## Timeline

| Date | Description | 
|---|---|
| 21 Sep 2026 | First access to DIVD systems by a malicious actor | 
| 22 Sep 2026 | DIVD becomes aware of malicious activity. Access to all systems in the data centre is blocked | 
| 22 Sep 2026 | Incident response team is formed | 
| 23 Sep 2026 | Forensic investigation begins in collaboration with Merlon Security | 
| 24 Sep 2026 | Vulnerability reported to Zammad. | 
| 24 Sep 2026 | DIVD updated partners and affected parties. | 
| 24 Sep 2026 | [First public statement on LinkedIn about being hacked.](https://www.linkedin.com/feed/update/urn:li:activity:7508986131779088384) | 
| 26 Sep 2026 | DIVD launched case DIVD-2026-00015 to scan for publicly accessible, vulnerable Zammad instances. | 
| 26 Sep 2026 | DIVD issued a limited disclosure for CVE-2026-102489 and CVE-2026-102490. | 
| 26 Sep 2026 | [Public statement on LinkedIn about the AI modus operandi.](https://www.linkedin.com/feed/update/urn:li:activity:7509723920586153984) | 
| 28 Sep 2026 | [Public statement on LinkedIn about what we know so far.](https://www.linkedin.com/feed/update/urn:li:activity:7510363579972206592) | 
| 29 Sep 2026 | Publication of the [case file](https://csirt.divd.nl/DIVD-2026-00014) | 
| 30 Sep 2026 | [Public statement on LinkedIn about zero-days in Zammad.](https://www.linkedin.com/feed/update/urn:li:activity:7511092587848523778) | 
| 30 Sep 2026 | DIVD informed partners and affected parties about data that might have been compromised. | 
| 01 Oct 2026 | Publication of an [overview of which data was compromised](https://csirt.divd.nl/DIVD-2026-00014/overview_data_investigation/) and which data was not. | 
| 01 Oct 2026 | [Public statement on LinkedIn about the data breach.](https://www.linkedin.com/feed/update/urn:li:activity:7511448012582387714) | 
| 05 Oct 2026 | Police report filed at 13:37 | 
| 07 Oct 2026 | Presentation at the [One Conference](https://one-conference.nl/session/divd-secures-the-internet-gets-hacked-with-0-days-and-ai/) | 
| 09 Oct 2026 | Case file overview of the data investigation updated. | 
| 18 Nov 2026 | Updated the casefile and [overview of the compromise status of our data](https://csirt.divd.nl/DIVD-2026-00014/overview_data_investigation/) based on the technical investigation | 
| 24 Nov 2026 | Victim notificaitons sent to all personal email addresses leaked. | 
| 25 Nov 2026 | Full disclosure, publication of [the report of the forensic investigation of the hack](https://csirt.divd.nl/DIVD-2026-00014/full_disclosure/) based on the technical investigation | 

## Contact

For general questions about the breach, please contact [communications@divd.nl](mailto:communications@divd.nl?subject=Question%20about%20DIVD%20breach). If you have concerns about your personal data, please contact [dpo@divd.nl](mailto:dpo@divd.nl?subject=Data%20status%20inquiry%20DIVD%20hack).
