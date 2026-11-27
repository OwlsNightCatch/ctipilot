---
schema: 1
kind: vulnerability
title: "CVE-2026-103406, Juniper Session Smart Conductor before 7.0.5, 7.1.7 and 7.2.3: an unauthenticated OS command injection as root through a crafted salt minion ID in the AutomatedProvisioner (CVSS 3.1 9.8) is listed by CISA as exploited on 2026-11-25, after BSI reported exploitation"
headline: "Juniper Session Smart Conductor: unauthenticated root command injection exploited; upgrade to 7.0.5, 7.1.7 or 7.2.3"
summary: >
  CISA added CVE-2026-103406 to its Known Exploited Vulnerabilities catalogue on 2026-11-25, after BSI revised its advisory to say the flaw is being exploited. ENISA's record, which carries Juniper's own description, calls it an OS command injection in the AutomatedProvisioner of Session Smart Conductor that lets a remote attacker run commands as root through a crafted salt minion ID (CVSS 3.1 9.8, no privileges or user interaction), with the affected ranges ending at 7.0.5, 7.1.7 and 7.2.3. No source names an actor, victim, scale or technique, and Juniper's own bulletin JSA112183 could not be read.
discovered_at: "2026-11-26T05:04:10Z"
updated_at: null
event_date: "2026-11-25"
run_id: 2026-11-26T0356Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, actively-exploited, cisa-kev, patch-available]
regions: [global]
sectors: [technology]
entities: ["product:juniper-session-smart-conductor", "product:juniper-session-smart-router"]
techniques: [T1190, T1059.004]
affected_products: ["Juniper Session Smart Conductor", "Juniper Session Smart Router"]
cves:
  - id: CVE-2026-103406
    cvss: "9.8"
    epss: "0.0086"
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "Session Smart Conductor before 7.0.5, from 7.1.0 before 7.1.7 and from 7.2.0 before 7.2.3"
    fixed: "7.0.5, 7.1.7, 7.2.3"
  - id: CVE-2026-103409
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Session Smart Router, exploitable only before the device is onboarded to Mist or a Conductor"
    fixed: "7.0.5, 7.1.7, 7.2.3"
sources:
  - url: "https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog"
    publisher: "CISA"
    date: "2026-11-25"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV catalogue"
    date: "2026-11-25"
    role: primary
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-112215"
    publisher: "ENISA EUVD (EUVD-2026-112215)"
    date: "2026-10-28"
    role: corroborating
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-112212"
    publisher: "ENISA EUVD (EUVD-2026-112212)"
    date: "2026-10-28"
    role: corroborating
  - url: "https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-4234.json"
    publisher: "BSI CERT-Bund (WID-SEC-W-2026-4234)"
    date: "2026-11-24"
    role: corroborating
closed_sources: []
evidence:
  - quote: "contain an OS command injection vulnerability that could allow a remote attacker to execute arbitrary commands as root via a specially crafted salt minion ID."
    publisher: "CISA KEV catalogue"
    source_url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
  - quote: "CVE-2026-103406 is being exploited"
    original: "CVE-2026-103406 wird ausgenutzt"
    publisher: "BSI CERT-Bund (WID-SEC-W-2026-4234)"
    source_url: "https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-4234.json"
  - quote: "An Improper Neutralization of Special Elements used in an OS Command vulnerability in the AutomatedProvisioner in Juniper Networks Session Smart Conductor allows a remote attacker to execute arbitrary commands as root via a specially crafted salt minion ID."
    publisher: "ENISA EUVD (EUVD-2026-112215)"
    source_url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-112215"
verification: multi-source
sourcing_note: >
  CISA, BSI and ENISA each state the flaw or its exploitation, but all three rest on Juniper's own bulletin JSA112183, whose text was not available, so the affected ranges, scores and description are ENISA's relay of Juniper's text. BSI does not state its basis for the exploitation statement, and no source gives an actor, a victim or a count of compromised systems; the only first-exploitation date is ENISA's exploited-since field, which follows the catalogue listing. CISA's catalogue names Session Smart Router as well as Conductor, while ENISA's record, which carries Juniper's text, lists only Conductor for this CVE. The EPSS value is FIRST's probability of 2026-11-25.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every Juniper Session Smart Conductor to 7.0.5, 7.1.7 or 7.2.3 (by branch) and, on any Conductor that was reachable before the upgrade, look for shell processes started by its provisioning services and for routers, accounts or configuration changes nobody made, because CISA lists CVE-2026-103406 as exploited."
updates: []
migrated_from: null
---

CISA added CVE-2026-103406 to its Known Exploited Vulnerabilities catalogue on 2026-11-25 ([CISA, 2026-11-25](https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog)); the catalogue record says a remote attacker could execute arbitrary commands as root via a specially crafted salt minion ID and names both Session Smart Conductor and Session Smart Router ([CISA KEV catalogue, 2026-11-25](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). BSI had revised its advisory on 2026-11-24 (23:00 UTC) with the summary "CVE-2026-103406 is being exploited" (translated from German), without stating its basis ([BSI, 2026-11-24](https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-4234.json)). No source names an actor, a victim, the number of compromised systems or the attack technique, and the only first-exploitation date, ENISA's exploited-since field of 2026-11-25, follows the catalogue listing ([ENISA EUVD, 2026-10-28](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-112215)).

ENISA's record, which carries Juniper's description, narrows the flaw to the AutomatedProvisioner of Session Smart Conductor: an improper neutralization of special elements lets a remote attacker execute arbitrary commands as root via a specially crafted salt minion ID, scored CVSS 3.1 9.8 with network access, no privileges and no user interaction ([ENISA EUVD, 2026-10-28](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-112215)). The affected ranges are Conductor before 7.0.5, from 7.1.0 before 7.1.7 and from 7.2.0 before 7.2.3, so 7.0.5, 7.1.7 and 7.2.3 are the first fixed releases ([ENISA EUVD, 2026-10-28](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-112215)). The record references Juniper's bulletin JSA112183, which could not be read, and its CVE record was published on 2026-10-28. The same release fixes CVE-2026-103409 in the Session Smart Router, an unauthenticated flaw scored 9.8 that can be exploited only before the device is onboarded to Mist or a Conductor ([ENISA EUVD, 2026-10-28](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-112212)).

**Exposure:** a Session Smart Conductor on a release below 7.0.5, 7.1.7 or 7.2.3 that a network attacker can reach; the sources do not name the interface or port the AutomatedProvisioner path uses or say whether it is on by default. Read the running release on each Conductor and compare it with the three fixed releases.

**Detection:** process-creation events showing a shell or interpreter started as root by the Conductor's provisioning or salt services, minion or router registration events whose ID contains shell metacharacters or command-substitution syntax, and the Conductor's audit and configuration-change records; these follow from the mechanism ENISA relays, and no source publishes an indicator. Upgrading does not remove an attacker who is already in, so a Conductor that was reachable before the upgrade needs a check for accounts, router registrations and configuration pushed from it that nobody made.

**Defender takeaway:** upgrade every Conductor to a fixed release now rather than at the next cycle, since CISA and BSI both report exploitation of an unauthenticated root command injection; until then, limit which hosts can reach the Conductor, because the flaw needs only network access.
