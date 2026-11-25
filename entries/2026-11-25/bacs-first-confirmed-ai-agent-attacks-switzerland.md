---
schema: 1
kind: threat
title: "BACS: first confirmed cyberattacks carried out with AI agents against Swiss companies and critical-infrastructure operators, every known case ending in a compromise; internet-reachable agents such as ARTEX and CyberStrikeAI have almost doubled since October"
headline: "BACS confirms first AI-agent attacks in Switzerland, all successful; critical updates within 24 hours"
summary: >
  Switzerland's Federal Office for Cyber Security (BACS) said on 2026-11-24 that it has for the first time received reports of attacks on Swiss companies and critical-infrastructure operators in at least two sectors that were carried out with the support of an AI agent, and that in every case known to it the agent led to a successful compromise of the victim's IT systems. It names no framework, case count, sector or entry point for the Swiss cases, says the number of internet-reachable agents such as ARTEX and CyberStrikeAI has almost doubled since October 2026, and recommends critical updates on internet-reachable systems within 24 hours.
discovered_at: "2026-11-25T04:39:00Z"
updated_at: null
event_date: "2026-11-24"
run_id: 2026-11-25T0356Z-intel
priority: high
immediate_action: null
tags: [ai-abuse]
regions: [switzerland]
sectors: []
entities: []
techniques: [T1595.002, T1190, T1078.001, T1110.001]
affected_products: []
cves: []
sources:
  - url: "https://www.bacs.admin.ch/de/26-ki-agenten-1-de"
    publisher: "BACS (NCSC.ch)"
    date: "2026-11-24"
    role: primary
  - url: "https://www.bacs.admin.ch/en/26-ki-agenten-1-en"
    publisher: "BACS (NCSC.ch)"
    date: "2026-11-24"
    role: corroborating
  - url: "https://www.netzwoche.ch/news/2026-11-02/wie-it-lieferketten-und-insider-zur-gefahr-werden-koennen"
    publisher: "Netzwoche"
    date: "2026-11-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "In all cyberattacks known to the NCSC, the use of AI agents led to the successful compromise of the victim’s IT systems."
    publisher: "BACS (NCSC.ch)"
    source_url: "https://www.bacs.admin.ch/en/26-ki-agenten-1-en"
  - quote: "Critical security updates for systems accessible via the internet should be installed as soon as possible, but no later than 24 hours after release."
    publisher: "BACS (NCSC.ch)"
    source_url: "https://www.bacs.admin.ch/en/26-ki-agenten-1-en"
verification: single-source-national-cert
sourcing_note: "BACS is the disclosing national authority for its own jurisdiction and the only source; no second outlet had reported it when this was written. The page gives no case count, sectors, victims, framework or entry point for the Swiss cases, and its description of what such agents exploit is a general statement about the tool class, not the access path of those cases."
confidence: high
references:
  - 2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse
  - 2026-11-24/babidighost-jailbroken-ai-agent-belgium-france-switzerland
  - 2026-11-14/cyberstrikeai-aws-cloudtrail-intrusion-one-source-ip
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

BACS reports that in recent days it received its first reports of cyberattacks against organisations in Switzerland carried out with the support of an AI agent, that the victims are various companies and operators of critical infrastructure in at least two sectors, and that in every case known to it the use of AI agents led to a successful compromise of the victim's IT systems ([BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)). It calls these the first confirmed Swiss cases and says the attackers used so-called "Agentic Offensive Frameworks", agents that independently search for weaknesses, choose attack tools, evaluate the results and plan the next steps ([BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)). The page names no framework used in these cases, no case count, no sector and no entry point, and says BACS also shares technical indicators for detecting such AI tools with critical-infrastructure operators ([BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)). Netzwoche reported on 2026-11-02 that BACS's GovCERT co-head had said at the Gohack26 symposium that no case in which autonomous AI agents hacked someone had been reported to the office so far (translated from German) ([Netzwoche, 2026-11-02](https://www.netzwoche.ch/news/2026-11-02/wie-it-lieferketten-und-insider-zur-gefahr-werden-koennen)).

Describing the tool class in general, BACS says such agents exploit, for example, standard or easily guessed passwords and known vulnerabilities in software or internet-connected systems, often need only a fraction of the time a human would to find and exploit vulnerable systems, and switch to other known attack methods when they meet a defence ([BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)). It adds that the number of internet-reachable AI agents such as ARTEX or CyberStrikeAI has almost doubled since October 2026, with no baseline or counting method given, names the two tools only as examples and does not say they were used in the Swiss cases, and expects an accumulation of fast, successful attacks ([BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)).

**Exposure:** internet-reachable systems with standard or easily guessed passwords or with known, unpatched vulnerabilities, which is what BACS says such agents exploit; BACS addresses its recommendations to companies in Switzerland and does not name administrations or sectors.

**Detection:** BACS recommends detecting when identities, applications, workloads and infrastructure deviate from their established behaviour patterns ([BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)); BACS says it shares technical indicators with critical-infrastructure operators and publishes none in the text.

**Defender takeaway:** BACS asks that critical security updates for internet-reachable systems be installed as soon as possible and at the latest after 24 hours (the German text gives no start point; the official English page says after release) ([BACS, 2026-11-24](https://www.bacs.admin.ch/en/26-ki-agenten-1-en)), that access to exposed systems be limited by allow-list or geo-blocking, and that MFA or passkeys cover every internet-reachable internal resource without exception ([BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)). Check the internet-facing estate for default and guessable passwords and for patch lag against that 24-hour ceiling first.
