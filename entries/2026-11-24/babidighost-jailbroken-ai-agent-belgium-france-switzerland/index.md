---
schema: 1
kind: threat
title: "BabidiGhost: a jailbroken Hermes-based AI agent run against more than 50 targets, mostly in Belgium, France and Switzerland, exported an insurer's customer database and 13 municipalities' archives through public flaws and exposures; MFA, IP allow-listing and server-side validation stopped it"
headline: "BabidiGhost AI agent targeted 50+ organisations, mostly in Belgium, France, Switzerland; MFA and allow-lists held"
summary: >
  SOCRadar reconstructs a nine-day operation (2026-11-06 to 2026-11-14) in which a low-skill French-speaking operator ran a jailbroken Hermes-based AI agent against more than 50 organisations and datasets, mostly in Belgium, France and Switzerland, breaching two of 14 analysed in depth and partly breaching three, the largest thefts being an insurer's customer database through an unpatched Metabase (CVE-2023-38646) and the archives of more than 13 municipalities through a weak password on a shared IT provider's storage interface, while TOTP, IP allow-listing and server-side validation stopped it. ZATAZ reports that the BlackHatSect0r handle now rents the agent and offers a bank-phishing platform that covers 28 Swiss banks; neither source names a Swiss victim.
discovered_at: "2026-11-24T04:31:00Z"
updated_at: null
event_date: "2026-11-06"
run_id: 2026-11-24T0355Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, organized-crime, data-breach, phishing]
regions: [europe, switzerland]
sectors: [public-sector, finance]
entities: ["actor:babidighost", "actor:blackhatsect0r", "tool:hermes-ai-agent"]
techniques: [T1595.002, T1596.003, T1589.002, T1584.004, T1190, T1078, T1110.001, T1110, T1552.001, T1059.001, T1053.005, T1547.001, T1546, T1036.005, T1685, T1005, T1213, T1567, T1657]
affected_products: ["Metabase"]
cves: []
sources:
  - url: "https://socradar.io/blog/babidighost-ai-augmented-cybercrime/"
    publisher: "SOCRadar Research"
    date: "2026-11-20"
    role: primary
  - url: "https://www.zataz.com/blackhatsect0r-phishing-bancaire-extorsion-et-industrie/"
    publisher: "ZATAZ"
    date: "2026-11-23"
    role: corroborating
  - url: "https://www.zataz.com/blackhat-sector-une-ia-offensive-a-louer-pour-500-e/"
    publisher: "ZATAZ"
    date: "2026-11-23"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The agent targeted more than 50 organizations and datasets, mostly in Belgium, France and Switzerland"
    publisher: "SOCRadar Research"
    source_url: "https://socradar.io/blog/babidighost-ai-augmented-cybercrime/"
  - quote: "A storage server run by a shared IT provider exposed its management interface to the internet, and a weak administrator password opened it."
    publisher: "SOCRadar Research"
    source_url: "https://socradar.io/blog/babidighost-ai-augmented-cybercrime/"
  - quote: "The commercial announcement stresses the integration of 28 Swiss institutions, among them UBS, PostFinance, Raiffeisen, ZKB, BCV, BCGE, Migros Bank, Swissquote, Pictet and Julius Baer. (translated from French)"
    original: "L’annonce commerciale insiste sur l’intégration de 28 établissements suisses, parmi lesquels UBS, PostFinance, Raiffeisen, ZKB, BCV, BCGE, Migros Bank, Swissquote, Pictet et Julius Baer."
    publisher: "ZATAZ"
    source_url: "https://www.zataz.com/blackhatsect0r-phishing-bancaire-extorsion-et-industrie/"
verification: single-source
sourcing_note: >
  Every fact about the operation is SOCRadar's alone, from static analysis of the operator's exposed staging server; SOCRadar anonymises its victims and does not state the countries of the breached organisations, so a Swiss victim is neither confirmed nor excluded. ZATAZ corroborates only the handle's commerce, the agent rental and the phishing platform, from the seller's own advertisements, and relays unverified claims. The sources differ on identity: SOCRadar calls BabidiGhost the second operator of the BlackHatSect0r toolchain, ZATAZ treats BabidiGhost and GhostHunters as signatures of BlackHatSect0r. CVE-2023-38646 is named by SOCRadar without a per-CVE record, so no CVE record is carried.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

SOCRadar recovered the exposed home directory of a hijacked French staging server and reconstructs a nine-day operation, 2026-11-06 to 2026-11-14, in which a low-skill French-speaking operator, BabidiGhost, typed plain-language orders to a jailbroken Hermes-based AI agent that wrote the scanners, exploits and exfiltration scripts ([SOCRadar, 2026-11-20](https://socradar.io/blog/babidighost-ai-augmented-cybercrime/)). The agent targeted more than 50 organisations and datasets, mostly in Belgium, France and Switzerland; of 14 analysed in depth, two were breached and three partly breached; SOCRadar says every successful intrusion used an exposed, unpatched analytics tool, a readable secret, a weak password or an unauthenticated endpoint, with no zero-day ([SOCRadar, 2026-11-20](https://socradar.io/blog/babidighost-ai-augmented-cybercrime/)).

An internet-facing, unpatched Metabase vulnerable to CVE-2023-38646 let the agent in; it then ran commands on the server beneath the dashboard, read cloud database credentials from the container environment, exported the customer database and planted a database trigger that relaunched its implant on every new record. A shared IT provider's storage-management interface was exposed to the internet and a weak administrator password opened it, giving 23 archives of about 8.6 GB from more than 13 municipalities and 10 other public bodies; SOCRadar says this one server drives Belgium's share of more than half of the targets and names no Swiss municipality. Against banks the agent mapped the attack surface through certificate logs and a sign-in error oracle confirmed 48 valid corporate accounts, while a crawler swept Swiss websites for IBANs, email addresses and phone numbers. TOTP second factors, an IP allow-list and server-side business validation stopped the same agent ([SOCRadar, 2026-11-20](https://socradar.io/blog/babidighost-ai-augmented-cybercrime/)).

Its model API key was revoked on 2026-11-14, but a PowerShell beacon and a C# backdoor posing as a Windows Update service, persisted through scheduled tasks and a Run key, kept calling home until 2026-11-15, and stolen archives had gone out through Telegram ([SOCRadar, 2026-11-20](https://socradar.io/blog/babidighost-ai-augmented-cybercrime/)).

ZATAZ reports that the BlackHatSect0r handle, whose toolchain SOCRadar says the agent runs, rents a jailbroken agent ([ZATAZ, 2026-11-23](https://www.zataz.com/blackhat-sector-une-ia-offensive-a-louer-pour-500-e/)) and offers a bank-phishing platform with templates for 81 banks in France, Belgium, Luxembourg and Switzerland, 28 of them Swiss including UBS, PostFinance and Raiffeisen; ZATAZ names no Swiss victim ([ZATAZ, 2026-11-23](https://www.zataz.com/blackhatsect0r-phishing-bancaire-extorsion-et-industrie/)).

**Exposure:** the gaps used were internet-facing analytics tools, storage-management interfaces at shared IT providers, unauthenticated API routes, sign-in flows that reveal whether an account exists and secrets readable from a web application's environment ([SOCRadar, 2026-11-20](https://socradar.io/blog/babidighost-ai-augmented-cybercrime/)).

**Detection:** egress or proxy telemetry showing a server calling a model-provider API or the Telegram bot API without a business reason; on Windows, a Run key and scheduled tasks for a service posing as Windows Update, unexpected Defender exclusions and outbound TCP to port 8443; on PostgreSQL, triggers nobody created. SOCRadar's hunt window is 2026-11-05 to 2026-11-17, and revoking the model key did not remove deployed implants ([SOCRadar, 2026-11-20](https://socradar.io/blog/babidighost-ai-augmented-cybercrime/)).

**Triage:** the Hermes Agent directory and its SOUL.md exist on every Hermes installation; they matter only when SOUL.md carries the jailbreak strings SOCRadar's rule matches ([SOCRadar, 2026-11-20](https://socradar.io/blog/babidighost-ai-augmented-cybercrime/)).

**Defender takeaway:** patch Metabase and take analytics tools, storage-management interfaces and unauthenticated API routes off the internet, keep secrets out of runtime environments, and verify the controls that stopped the agent (TOTP, IP allow-listing, server-side validation) at the shared IT providers that hold municipal data ([SOCRadar, 2026-11-20](https://socradar.io/blog/babidighost-ai-augmented-cybercrime/)).
