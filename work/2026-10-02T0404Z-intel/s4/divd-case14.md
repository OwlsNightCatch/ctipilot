---
title: DIVD-2026-00014 - When, not if…
url: https://csirt.divd.nl/cases/DIVD-2026-00014/
hostname: divd.nl
description: DIVD got hacked through AI agents.
sitename: DIVD CSIRT
date: "2026-10-01"
---
# DIVD-2026-00014 - When, not if...

| Our reference | [DIVD-2026-00014](https://csirt.divd.nl/cases/DIVD-2026-00014) | 
| Case lead | DIVD Crisis Management Team | 
| Author | Various | 
| CVE(s) |  | 
| Status | Open | 
| Last modified | 01 Oct 2026 22:30 CEST | 

## Summary

DIVD got hacked through AI agents and is currently investigating the breach. Incident investigation is ongoing.

### Statement #1 — Thursday 24 September 2026

We got hacked. We noticed suspicious activity, investigated, and came to the inevitable conclusion that we got hacked. We went into full incident response mode, blocked access to our infrastructure and started a forensics investigation with a third party incident response team. The modus operandi indicates an agentic AI powered attack, something we had not seen before. We informed the directly involved parties, reported the incident to the Autoriteit Persoonsgegevens and NCSC-NL and discussed our options with the police. Until proven otherwise, we handle this as a worst case scenario and assume breach.

### Statement #2 — Saturday 26 September 2026

On our birthday, we share two redacted screenshots from the logs. They show the attacker’s scripts contain notes where the agent justifies its own actions, explaining why what it’s doing is okay and really not phishing, something a human attacker wouldn’t bother with. It supports our assessment that this is an agentic AI powered attack. We can’t share more for now without getting in the way of the investigation.

### Statement #3 — Monday 29 September 2026

We separate what we know from what we think and what we don’t know yet. The attackers got in by exploiting a technical vulnerability, and it was not Citrix Netscaler. We see no link to any known public threat actor, and no facts so far point to our worst case scenario, in which an actor targeted us directly to get at our crown jewels, though we can’t rule it out. The attack was loud and very messy, with the agent working automated and deciding each next step itself at speed on sloppy logic and its overexplaining comments have made our reverse engineering a lot easier.

### Statement #4 — Tuesday 30 September 2026

We explain the attackers got in through two zero-days in Zammad that together allowed session hijacking, remote code execution and privilege escalation from the Zammad user to root, in seconds due to the agentic part of this hack. From there they could access other services and exfiltrate data. Thanks to proper network segmentation and the actions of our IT and Incident Response Team after detection, we were able to stop the attackers from going deeper into our systems and network. Unfortunately some of the damage was already done. We’ve found signs of compromise that we’re still looking into, and until we can prove otherwise we assume breach. Still, stopping the attackers is a win and in a situation like this you take every win you can get. 
**We have assigned the CVE IDs [CVE-2026-102489](https://csirt.divd.nl/cves/CVE-2026-102489) and [CVE-2026-102490](https://csirt.divd.nl/cves/CVE-2026-102490) to these vulnerabilities and started case [DIVD-2026-00015](https://csirt.divd.nl/cases/DIVD-2026-00015) to do target and victim notification for these two known exploited vulnerabilities.**

### Statement #5 — Thursday 1 October 2026

We share the most painful and awkward part of being hacked, which data got out. We don’t wait until we have every answer, because that doesn’t make digital society any safer. What we know for sure is that volunteer data got out, such as DIVD email addresses and possibly contact details. Whose data and exactly which data is still being investigated, but it does mean it’s now easier for someone to pose as a DIVD volunteer. If a message from someone at DIVD feels off, check with us first at communications@divd.nl.

We have identified that the hackers got in via two 0-day vulnerabilities in Zammad. We have assigned the CVE IDs [CVE-2026-102489](https://csirt.divd.nl/cves/CVE-2026-102489) and [CVE-2026-102490](https://csirt.divd.nl/cves/CVE-2026-102490) to these vulnerabilities and started case [DIVD-2026-00015](https://csirt.divd.nl/cases/DIVD-2026-00015) to do target and victim notification for these two known exploited vulnerabilities.

## More information

- Case [DIVD-2026-00015](https://csirt.divd.nl/cases/DIVD-2026-00015) - The casefile for the 0-day vulnerabilities in Zammad
- [Overview of the investigation into the status of our data](https://csirt.divd.nl/DIVD-2026-00014/overview_data_investigation/)

We will update this page shortly with more information on the incident.

## Timeline

| Date | Description | 
|---|---|
| 21 Sep 2026 | First access by malicious actor on DIVD systems | 
| 22 Sep 2026 | DIVD becomes aware of malicious activity. Access to all systems in the datacenter is blocked | 
| 22 Sep 2026 | Incident response team formed and forensic investigation started together with Merlon Security | 
| 24 Sep 2026 | Vulnerability reported to Zammad. | 
| 24 Sep 2026 | DIVD updated partners and affected parties. | 
| 24 Sep 2026 | First public statement on LinkedIn about being hacked. | 
| 26 Sep 2026 | DIVD started case DIVD-2026-00015, to scan for publicly available and vulnerable Zammad instances. | 
| 26 Sep 2026 | DIVD created a limited disclosure for CVE-2026-102489 & CVE-2026-102490. | 
| 26 Sep 2026 | Public statement on LinkedIn about the AI modus operandi. | 
| 28 Sep 2026 | Public statement on LinkedIn about what we know so far. | 
| 29 Sep 2026 | Publication of casefile | 
| 30 Sep 2026 | Public statement on LinkedIn about zero-days in Zammad. | 
| 30 Sep 2026 | DIVD informed partners and affected parties about data that might have been breached. | 
| 01 Oct 2026 | Publication of overview of which data is compromised and which data is not. | 
| 01 Oct 2026 | Public statement on LinkedIn about the data breach. |
