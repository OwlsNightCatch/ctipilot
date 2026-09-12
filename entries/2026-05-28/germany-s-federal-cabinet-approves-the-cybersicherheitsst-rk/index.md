---
schema: 1
kind: threat
title: "Germany's federal cabinet approves the Cybersicherheitsstärkungsgesetz — BKA, BSI and Federal Police gain authority to redirect traffic and disable attacker infrastructure"
headline: "Germany's federal cabinet approves the Cybersicherheitsstärkungsgesetz — BKA, BSI and Federal Police gain authority to redirect traffic and disable attacker"
summary: "The German federal cabinet approved the Cybersicherheitsstärkungsgesetz (Law to Strengthen Cybersecurity) on 2026-05-27, granting three federal agencies — the Bundeskriminalamt (BKA), the Bundesamt für Sicherheit in der Informationstechnik (BSI) and the Bundespolizei — new authority to conduct what the government …"
discovered_at: "2026-05-28T05:00:01Z"
event_date: 2026-05-27
run_id: 2026-05-28-3e33200a
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - eu-nexus
regions:
  - dach
  - europe
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.heise.de/news/Hackback-Erlaubnis-Kabinett-macht-Weg-frei-11308323.html"
    publisher: Heise Security
    role: primary
  - url: "https://www.onvista.de/news/2026/05-27-kabinett-billigt-gesetz-fuer-offensive-cyberabwehr-0-20-26515861"
    publisher: onvista / dpa
    role: corroborating
  - url: "https://www.t-online.de/nachrichten/deutschland/id_101271406/kabinett-gibt-bsi-und-polizei-befugnisse-zur-cyberabwehr.html"
    publisher: t-online
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-28.md
---

The German federal cabinet approved the *Cybersicherheitsstärkungsgesetz* (Law to Strengthen Cybersecurity) on 2026-05-27, granting three federal agencies — the Bundeskriminalamt (BKA), the Bundesamt für Sicherheit in der Informationstechnik (BSI) and the Bundespolizei — new authority to conduct what the government frames as active cyber defence rather than offensive hackback ([Heise Security, 2026-05-27](https://www.heise.de/news/Hackback-Erlaubnis-Kabinett-macht-Weg-frei-11308323.html); [onvista / dpa, 2026-05-27](https://www.onvista.de/news/2026/05-27-kabinett-billigt-gesetz-fuer-offensive-cyberabwehr-0-20-26515861); [t-online, 2026-05-27](https://www.t-online.de/nachrichten/deutschland/id_101271406/kabinett-gibt-bsi-und-polizei-befugnisse-zur-cyberabwehr.html)). Under the law the agencies may redirect attacker-controlled traffic, selectively intervene in IT systems used to attack Germany, delete or modify data on attacker servers, and shut down dangerous C2 nodes — explicitly including foreign infrastructure. Interior Minister Alexander Dobrindt (CSU) positioned the measure as active cyber defence targeting attacker command-and-control infrastructure rather than retaliatory hackback. The bill funds the order of 350 new positions across the three agencies and approximately €50 million per year in personnel and material (per onvista/dpa; t-online reports a smaller initial figure. The Bundesverband der Deutschen Industrie (BDI) and civil-society voices warned of collateral-damage risk on shared hosting and VPN servers and flagged constitutional concerns. The bill next proceeds to the Bundestag; it does not yet have force of law.

**Why it matters to us:** German LE gaining the legal authority to sinkhole, redirect, or disable attack infrastructure will change the threat-intel attribution picture across Europe. SOC managers should expect that unexplained C2 outages on Germany-adjacent hosting may be LE action rather than malware infrastructure rotation. Threat-intel teams tracking takedown patterns should add `de.bka`, `de.bsi`, `de.bpol` as expected actors in the takedown attribution stack alongside CrowdStrike Counter Adversary Operations, Microsoft DCU and Europol.
