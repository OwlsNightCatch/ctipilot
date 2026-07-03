---
schema: 1
kind: research
horizon: operational
title: "Bauman University \"Department No. 4\" — leaked GRU cyber-operator training pipeline reveals direct line to Sandworm and APT28 operations against European targets"
headline: "Bauman University \"Department No. 4\" — leaked GRU cyber-operator training pipeline reveals direct line to Sandworm and APT28 operations against European targets"
summary: "A six-publisher investigative consortium (The Insider, The Guardian, Le Monde, Der Spiegel, VSquare, Frontstory) published more than 2 000 leaked internal documents from Bauman Moscow State Technical University on 2026-05-07 detailing a structured GRU recruitment-and-training pipeline operating under the cover of …"
discovered_at: "2026-05-10T05:00:04Z"
event_date: 2026-05-07
run_id: 2026-05-10-001
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - russia-nexus
regions:
  - europe
  - global
sectors:
  - public-sector
  - defense
entities: []
cves: []
sources:
  - url: "https://meduza.io/amp/en/feature/2026/05/07/secret-gru-linked-department-at-top-russian-university-trains-hackers-and-saboteurs-investigation-finds"
    publisher: "Meduza (English), 2026-05-07"
    role: primary
  - url: "https://www.theguardian.com/world/2026/may/07/revealed-russia-top-secret-spy-school-hacking-western-electoral-interference"
    publisher: "The Guardian, 2026-05-07"
    role: corroborating
  - url: "https://www.lemonde.fr/en/m-le-mag/article/2026/05/07/moscow-s-bauman-university-the-clandestine-school-training-russian-hackers_6753208_117.html"
    publisher: "Le Monde, 2026-05-07"
    role: corroborating
  - url: "https://www.spiegel.de/ausland/hybrider-krieg-moskau-bildet-in-einem-geheimen-uni-programm-spione-und-hacker-aus-a-2de79023-aa56-4ed6-b5de-d7c222402e63"
    publisher: "Der Spiegel, 2026-05-07"
    role: corroborating
  - url: "https://www.heise.de/news/Cyberkrieg-Medien-zitieren-Interna-aus-Russlands-Geheimdienstausbildung-11285528.html"
    publisher: "heise online, 2026-05-07"
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
migrated_from: briefs/2026-05-10.md
---

A six-publisher investigative consortium (The Insider, The Guardian, Le Monde, Der Spiegel, VSquare, Frontstory) published more than 2 000 leaked internal documents from Bauman Moscow State Technical University on 2026-05-07 detailing a structured GRU recruitment-and-training pipeline operating under the cover of "Department No. 4 — Special Training" ([Meduza (English), 2026-05-07](https://meduza.io/amp/en/feature/2026/05/07/secret-gru-linked-department-at-top-russian-university-trains-hackers-and-saboteurs-investigation-finds) · [The Guardian, 2026-05-07](https://www.theguardian.com/world/2026/may/07/revealed-russia-top-secret-spy-school-hacking-western-electoral-interference) · [Le Monde, 2026-05-07](https://www.lemonde.fr/en/m-le-mag/article/2026/05/07/moscow-s-bauman-university-the-clandestine-school-training-russian-hackers_6753208_117.html) · [Der Spiegel, 2026-05-07](https://www.spiegel.de/ausland/hybrider-krieg-moskau-bildet-in-einem-geheimen-uni-programm-spione-und-hacker-aus-a-2de79023-aa56-4ed6-b5de-d7c222402e63) · [heise online, 2026-05-07](https://www.heise.de/news/Cyberkrieg-Medien-zitieren-Interna-aus-Russlands-Geheimdienstausbildung-11285528.html)). Each year 10–15 graduates are placed directly into Russian military intelligence units. The 144-hour core curriculum, labelled in the documents "Countering Technical Intelligence", covers password attacks, CVE-driven exploitation using Metasploit *against US DoD network architectures by name*, custom trojan development, DDoS methodologies, penetration testing against Western targets, computer-virus construction, and propaganda/manipulation training. Candidates are physically assessed at a mandatory training camp; each placement requires explicit GRU approval.

The leaked assignment records explicitly link graduates to **GRU Unit 74455** (Sandworm / VoodooBear — responsible for the 2015–2016 Ukraine power-grid attacks, 2017 NotPetya global wiper, and 2023 Kyivstar telecom outage) and to **APT28** (Fancy Bear — responsible for the 2016 Bundestag hack and the 2017 Macron campaign breach, with continuing 2025–2026 activity against EU government and election-adjacent targets). For European defenders the salient operational point is that the curriculum *trains specifically against Western and US-DoD topologies* — meaning the training pipeline is producing operators whose default mental model of a target network is a NATO-aligned environment, not a generic enterprise. The investigation does not change short-term defensive priorities but reframes the long-running attribution debate: GRU cyber units are not ad-hoc-recruited contractors, they are graduates of a structured technical-intelligence training stream with measurable annual throughput.
