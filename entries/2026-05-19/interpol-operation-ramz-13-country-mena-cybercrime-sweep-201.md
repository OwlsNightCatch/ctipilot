---
schema: 1
kind: threat
title: "INTERPOL Operation Ramz: 13 MENA countries arrest 201 suspects, seize 53 servers and dismantle a phishing-as-a-service site in Algeria"
headline: "INTERPOL Operation Ramz: 201 arrests and 53 servers seized in 13 MENA countries, among them a phishing-as-a-service site"
summary: "INTERPOL announced on 2026-05-18 the results of Operation Ramz (October 2025 to 2026-02-28), in which 13 Middle East and North African countries went after phishing, malware and cyber scams: 201 arrests, 382 further suspects and 3,867 victims identified, and 53 servers seized. Highlights include a phishing-as-a-service website dismantled in Algeria with one arrest, phishing software and banking data seized in Morocco, compromised devices found spreading malicious threats in Qatar, and in Jordan a fake trading-platform scam run by 15 trafficking victims from Asia, whose two suspected organizers were arrested."
discovered_at: "2026-05-19T05:00:04Z"
event_date: 2026-05-18
run_id: 2026-05-19-2505c918
priority: routine
immediate_action: null
tags:
  - law-enforcement
  - organized-crime
  - phishing
regions:
  - middle-east
  - africa
sectors:
  - finance
entities:
  - "campaign:interpol-operation-ramz-mena-cybercrime-13-country-201-arre"
techniques: [T1566, T1584, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region"
    publisher: INTERPOL
    date: "2026-05-18"
    role: primary
  - url: "https://thehackernews.com/2026/05/interpol-operation-ramz-disrupts-mena.html"
    publisher: The Hacker News
    date: "2026-05-18"
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/05/18/interpol-mena-cybercrime-operation-ramz-201-arrests/"
    publisher: Help Net Security
    date: "2026-05-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A first-of-its-kind cybercrime operation in the MENA region has led to the arrest of 201 individuals, with a further 382 suspects identified."
    publisher: INTERPOL
    source_url: "https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region"
  - quote: "In Algeria, a website offering phishing as a service was identified and dismantled as part of Operation Ramz."
    publisher: INTERPOL
    source_url: "https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region"
  - quote: "A raid uncovered 15 individuals carrying out the scams, but investigators determined that they were victims of human trafficking who had been recruited under the false promise of employment from their home countries in Asia."
    publisher: INTERPOL
    source_url: "https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region"
verification: multi-source
sourcing_note: >
  INTERPOL reports on its own operation, and The Hacker News and Help Net Security restate its release; the release names no phishing kit, lure or
  technique beyond the outcomes listed.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-19.md
updates:
  - at: "2026-10-21T20:41:04Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      INTERPOL describes Operation Ramz as aimed at phishing, malware and cyber scams that cost the MENA
      region and names no targeting of EU banking customers or payment systems. In Jordan police raided a
      fake trading-platform fraud run by 15 trafficking victims from Asia and arrested two suspected
      organizers, and in Oman investigators disabled a vulnerable, malware-infected server in a private
      residence whose owner had legitimate access to its data; the Algeria takedown also led to one arrest
      and compromised devices in Qatar were found spreading malicious threats.
    fields: [affected_products, body, classification, evidence, headline, regions, sectors, sources, sourcing_note, summary, tags, techniques, title, priority]
---

INTERPOL's Operation Ramz ran from October 2025 to 2026-02-28 across Algeria, Bahrain, Egypt, Iraq, Jordan, Lebanon, Libya, Morocco, Oman, Palestine, Qatar, Tunisia and the UAE and focused on phishing and malware threats and on cyber scams; it led to 201 arrests, identified 382 further suspects and 3,867 victims, seized 53 servers and spread nearly 8,000 pieces of data and intelligence among the participants ([INTERPOL, 2026-05-18](https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region); [The Hacker News, 2026-05-18](https://thehackernews.com/2026/05/interpol-operation-ramz-disrupts-mena.html); [Help Net Security, 2026-05-18](https://www.helpnetsecurity.com/2026/05/18/interpol-mena-cybercrime-operation-ramz-201-arrests/)). In Algeria authorities dismantled a phishing-as-a-service website, seizing a server, a computer, a mobile phone and hard drives with phishing software and scripts and taking one suspect into custody, and Moroccan authorities seized devices holding banking data and phishing software, with three people now in judicial proceedings ([INTERPOL, 2026-05-18](https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region)). In Qatar the operation identified compromised devices whose owners did not know they were being used to spread malicious threats, and in Oman investigators disabled a server in a private residence that held sensitive information and suffered from critical vulnerabilities, including a malware infection ([INTERPOL, 2026-05-18](https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region)). Jordanian police raided a fraud operation whose fake trading platform shut down once victims had deposited money and found that the 15 people running it were trafficking victims recruited from Asia with false job offers whose passports had been confiscated; two suspected organizers were arrested ([INTERPOL, 2026-05-18](https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region)). Group-IB, Kaspersky, the Shadowserver Foundation, Team Cymru and TrendAI supported the operation, which the EU and the Council of Europe partly funded through the CyberSouth+ project ([INTERPOL, 2026-05-18](https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region)).

**Defender takeaway:** no change for defenders outside the region: the operation targeted infrastructure and suspects in the Middle East and North Africa, and the release names no lure, kit or technique to hunt for ([INTERPOL, 2026-05-18](https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region)). The Jordan case documents a scam operation staffed by trafficked workers held without their passports ([INTERPOL, 2026-05-18](https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region)).

## Correction — 2026-10-21T20:41:04Z

INTERPOL says the operation focused on phishing and malware threats and on cyber scams that inflict severe cost to the region; it names no targeting of EU banking customers or payment systems, and no source forecasts follow-on advisories or links the Jordan case to Europol work ([INTERPOL, 2026-05-18](https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region)). In Jordan police raided a computer used for a fake trading-platform fraud and found that the 15 people running it were trafficking victims recruited from Asia whose passports had been confiscated, and two suspected organizers were arrested ([INTERPOL, 2026-05-18](https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region)). The server in Oman sat in a private residence and held sensitive information its owner could legitimately access, but suffered from critical vulnerabilities including a malware infection and was disabled ([INTERPOL, 2026-05-18](https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region)). The Algerian takedown also put one suspect in custody, and in Qatar the operation found compromised devices being used, without their owners' knowledge, to spread malicious threats ([INTERPOL, 2026-05-18](https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region)).
