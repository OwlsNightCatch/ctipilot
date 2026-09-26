---
schema: 1
kind: threat
title: "Kiteworks (formerly Accellion) tells customers worldwide to shut down every server for six hours after 'credible' law-enforcement intelligence of an imminent attack, no CVE assigned"
headline: "A secure-file-transfer vendor with government customers tells its entire customer base to unplug production systems this weekend"
summary: >
  Kiteworks, a secure managed-file-transfer and confidential-communications
  platform rebranded from Accellion and marketed to government agencies and
  financial institutions, emailed customers worldwide on 2026-09-25 urging a
  precautionary six-hour shutdown of every Kiteworks system over the weekend
  of 2026-09-26 after receiving "credible threat intelligence from law
  enforcement" of a possible imminent attack. No CVE has been assigned and
  Kiteworks says it is not aware of any actual compromise; the Central
  European shutdown window falls in the timezone Switzerland shares.
discovered_at: "2026-09-26T04:04:42Z"
updated_at: null
event_date: "2026-09-25"
run_id: 2026-09-26T0404Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, zero-day]
regions: [global, europe, switzerland]
sectors: [public-sector, finance]
entities: ["product:kiteworks"]
techniques: [T1190]
affected_products: ["Kiteworks"]
cves: []
sources:
  - url: "https://www.heise.de/en/news/Imminent-Zero-Day-Attack-KiteWorks-Urges-Customers-to-Shut-Down-Servers-11466375.html"
    publisher: "Heise Online"
    date: "2026-09-25"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/"
    publisher: "BleepingComputer"
    date: "2026-09-25"
    role: primary
  - url: "https://therecord.media/kiteworks-urges-customers-to-stop-using-systems-incident"
    publisher: "The Record (Recorded Future News)"
    date: "2026-09-25"
    role: corroborating
  - url: "https://techcrunch.com/2026/09/25/kiteworks-urges-customers-to-shut-down-their-servers-amid-imminent-threat-of-cyberattack/"
    publisher: "TechCrunch"
    date: "2026-09-25"
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12985"
    publisher: "NCSC Switzerland — Cyber Security Hub"
    date: "2026-09-25"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We have received credible threat intelligence from law enforcement indicating an attack on Kiteworks systems may be imminent this weekend. We strongly recommend you shut down your Kiteworks system for six hours"
    publisher: "Kiteworks CISO Frank Balonis, via Heise Online"
    source_url: "https://www.heise.de/en/news/Imminent-Zero-Day-Attack-KiteWorks-Urges-Customers-to-Shut-Down-Servers-11466375.html"
  - quote: "We are not aware of any compromise of Kiteworks systems, and this advisory is preventative rather than a response to a confirmed breach"
    publisher: "Kiteworks, statement to BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/"
  - quote: "All known vulnerabilities are addressed in our current release, 9.5.1, and we continue to recommend customers run the latest version."
    publisher: "Kiteworks, statement to BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/"
  - quote: "There is no known CVE, patch, or additional technical details available – but nobody requests that their entire customer base unplug production systems over the weekend because of a hunch."
    publisher: "Jake Knott, watchTowr, via The Record (Recorded Future News)"
    source_url: "https://therecord.media/kiteworks-urges-customers-to-stop-using-systems-incident"
verification: multi-source
sourcing_note: >
  Every outlet's reporting traces to Kiteworks' own customer notification and
  CISO statements; the underlying threat (whether an actual vulnerability or
  attack exists) remains the vendor's own unconfirmed, precautionary
  characterization, not independently corroborated by a second party who
  observed an attack or a flaw. Credibility reflects that the advisory's
  issuance is well documented, not that an attack is confirmed.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Any Swiss public-sector or supplier Kiteworks deployment should follow the vendor's shutdown-window guidance for the remainder of the advised window, confirm the instance is updated to release 9.5.1, and watch Kiteworks' own advisory channel for a CVE or technical follow-up over the coming days."
updates: []
migrated_from: null
---

Kiteworks — a secure managed-file-transfer and confidential-communications platform rebranded from Accellion in 2021, marketed to government agencies, financial institutions and enterprises — emailed customers worldwide on 2026-09-25 urging a precautionary six-hour shutdown of every Kiteworks system, staggered by timezone; the Central European window falls 04:00–10:00 CEST on Saturday 2026-09-26, a timezone Switzerland shares ([Heise Online, 2026-09-25](https://www.heise.de/en/news/Imminent-Zero-Day-Attack-KiteWorks-Urges-Customers-to-Shut-Down-Servers-11466375.html)). CISO Frank Balonis told Heise Online the company "received credible threat intelligence from law enforcement indicating an attack on Kiteworks systems may be imminent this weekend" ([Heise Online, 2026-09-25](https://www.heise.de/en/news/Imminent-Zero-Day-Attack-KiteWorks-Urges-Customers-to-Shut-Down-Servers-11466375.html)), and recommended shutting systems down even where they are not directly internet-facing, since the possible access route is unconfirmed. No CVE has been assigned, and Kiteworks states plainly it is "not aware of any compromise of Kiteworks systems" and that "all known vulnerabilities are addressed in our current release, 9.5.1" ([BleepingComputer, 2026-09-25](https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/)) — the advisory is preventative, not a confirmed-breach response. Researcher Kevin Beaumont's Shodan search found roughly a thousand internet-facing Kiteworks instances, though TechCrunch notes the count is likely an overcount of actually-affected customer systems ([TechCrunch, 2026-09-25](https://techcrunch.com/2026/09/25/kiteworks-urges-customers-to-shut-down-their-servers-amid-imminent-threat-of-cyberattack/)), and watchTowr's Jake Knott called the request itself unusual: "nobody requests that their entire customer base unplug production systems over the weekend because of a hunch" ([The Record, 2026-09-25](https://therecord.media/kiteworks-urges-customers-to-stop-using-systems-incident)).

The precedent class is exactly the one that matters for public-sector defenders: BleepingComputer notes that the Clop extortion gang "has a long history of targeting enterprise platforms in data-theft attacks," naming Accellion FTA, GoAnywhere MFT, SolarWinds Serv-U FTP, Cleo, and MOVEit Transfer as past victims of that pattern ([BleepingComputer, 2026-09-25](https://www.bleepingcomputer.com/news/security/kiteworks-urges-6-hour-server-shutdown-over-potential-zero-day-attacks/)); no actor has been named or confirmed for this specific warning by Kiteworks, the FBI, or CISA. Kiteworks itself was formerly Accellion, whose FTA product was the subject of exactly this kind of zero-day mass exploitation in December 2020, when a Clop-linked group stole data from dozens of high-profile organizations ([The Record, 2026-09-25](https://therecord.media/kiteworks-urges-customers-to-stop-using-systems-incident)).

**Defender takeaway:** treat the vendor's own shutdown-window guidance as the immediate action for the remainder of the advised window, confirm any Kiteworks deployment is current on release 9.5.1, and watch Kiteworks' advisory channel for a CVE or confirmed-exploitation disclosure over the coming days.
