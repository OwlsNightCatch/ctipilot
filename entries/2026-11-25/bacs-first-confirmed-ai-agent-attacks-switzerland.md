---
schema: 1
kind: threat
title: "BACS: first confirmed cyberattacks carried out with AI agents against Swiss companies and critical-infrastructure operators, five confirmed cases according to its director, three on critical-infrastructure operators; internet-reachable agents such as ARTEX and CyberStrikeAI have almost doubled since October"
headline: "BACS: five confirmed AI-agent attacks in Switzerland, three on critical infrastructure; critical updates within 24 hours"
summary: >
  Switzerland's Federal Office for Cyber Security (BACS) said on 2026-11-24 that it had for the first time received reports of attacks on Swiss companies and critical-infrastructure operators in at least two sectors that were carried out with the support of an AI agent; on 2026-11-26 its director told SRF that BACS has five confirmed cases, three on critical-infrastructure operators, and SRF reports that systems were compromised in four of the five (RTS reads two successes among three critical-infrastructure attacks, and BACS's page says every case known on 2026-11-24). No framework, sector, victim or entry point is named for the Swiss cases and the actor is unknown; BACS says the number of internet-reachable agents such as ARTEX and CyberStrikeAI has almost doubled since October 2026 and recommends critical updates on internet-reachable systems within 24 hours.
discovered_at: "2026-11-25T04:39:00Z"
updated_at: "2026-11-28T04:41:50Z"
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
  - url: "https://www.srf.ch/news/schweiz/fuenf-bestaetigte-faelle-erstmals-cyberangriffe-mit-ki-agenten-in-der-schweiz"
    publisher: "SRF"
    date: "2026-11-26"
    role: corroborating
  - url: "https://www.rts.ch/info/suisse/2026/article/cybersecurite-5-cyberattaques-menees-par-l-ia-en-suisse-29428554.html"
    publisher: "RTS"
    date: "2026-11-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "In all cyberattacks known to the NCSC, the use of AI agents led to the successful compromise of the victim’s IT systems."
    publisher: "BACS (NCSC.ch)"
    source_url: "https://www.bacs.admin.ch/en/26-ki-agenten-1-en"
  - quote: "Critical security updates for systems accessible via the internet should be installed as soon as possible, but no later than 24 hours after release."
    publisher: "BACS (NCSC.ch)"
    source_url: "https://www.bacs.admin.ch/en/26-ki-agenten-1-en"
  - quote: "We currently have five confirmed cases of attacks with AI agents."
    original: "Wir haben aktuell fünf bestätigte Fälle von Angriffen mit KI-Agenten."
    publisher: "SRF (quoting the BACS director)"
    source_url: "https://www.srf.ch/news/schweiz/fuenf-bestaetigte-faelle-erstmals-cyberangriffe-mit-ki-agenten-in-der-schweiz"
  - quote: "In four of five cases, systems had been successfully hacked."
    original: "In vier von fünf Fällen seien Systeme erfolgreich gehackt worden."
    publisher: "SRF"
    source_url: "https://www.srf.ch/news/schweiz/fuenf-bestaetigte-faelle-erstmals-cyberangriffe-mit-ki-agenten-in-der-schweiz"
verification: single-source-national-cert
sourcing_note: "BACS is the disclosing national authority for its own jurisdiction; SRF and RTS relay an interview of its director on 2026-11-26, the same authority speaking again and not an independent observation. The page gives no case count, sectors, victims, framework or entry point for the Swiss cases; the director gave five cases, and the three readings of how many succeeded differ (the page: every case known on 2026-11-24; SRF, in indirect speech with no named speaker for that sentence: four of five; RTS: two successes among three critical-infrastructure attacks, without saying whether the count covers all five). The page's description of what such agents exploit is a general statement about the tool class, not the access path of those cases."
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
updates:
  - at: "2026-11-28T04:41:50Z"
    run_id: 2026-11-28T0355Z-intel
    type: update
    summary: >
      BACS director Florian Schütz told SRF on 2026-11-26 that BACS has five confirmed cases of attacks
      with AI agents, three on critical-infrastructure operators, and SRF reports compromises in four of
      the five, while RTS reads two successes among three critical-infrastructure attacks and BACS's own
      page says every case known on 2026-11-24. No framework, victim sector or entry point is named and
      the actor is unknown.
    fields: [body, evidence, headline, sources, sourcing_note, summary, title]
migrated_from: null
---

BACS reported on 2026-11-24 that in recent days it had received its first reports of cyberattacks against organisations in Switzerland carried out with the support of an AI agent, that the victims are various companies and operators of critical infrastructure in at least two sectors, and that in every case known to it then the use of AI agents led to a successful compromise of the victim's IT systems ([BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)). Its director told SRF on 2026-11-26 that BACS has five confirmed cases, three on critical-infrastructure operators, with SMEs that reported voluntarily also hacked, and SRF reports that systems were compromised in four of the five (translated from German) ([SRF, 2026-11-26](https://www.srf.ch/news/schweiz/fuenf-bestaetigte-faelle-erstmals-cyberangriffe-mit-ki-agenten-in-der-schweiz)); RTS reads three critical-infrastructure attacks of which two succeeded, without saying whether the count covers all five (translated from French) ([RTS, 2026-11-26](https://www.rts.ch/info/suisse/2026/article/cybersecurite-5-cyberattaques-menees-par-l-ia-en-suisse-29428554.html)). BACS calls these the first confirmed Swiss cases and says the attackers used so-called "Agentic Offensive Frameworks", agents that independently search for weaknesses, choose attack tools, evaluate the results and plan the next steps ([BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)). Neither the page nor the two outlets name a framework used in these cases, a victim sector or an entry point; SRF reports no larger outages and an unknown actor, and BACS shares technical indicators for detecting such AI tools with critical-infrastructure operators ([SRF, 2026-11-26](https://www.srf.ch/news/schweiz/fuenf-bestaetigte-faelle-erstmals-cyberangriffe-mit-ki-agenten-in-der-schweiz); [BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)). Netzwoche reported on 2026-11-02 that BACS's GovCERT co-head had said at the Gohack26 symposium that no case in which autonomous AI agents hacked someone had been reported to the office so far (translated from German) ([Netzwoche, 2026-11-02](https://www.netzwoche.ch/news/2026-11-02/wie-it-lieferketten-und-insider-zur-gefahr-werden-koennen)).

Describing the tool class in general, BACS says such agents exploit, for example, standard or easily guessed passwords and known vulnerabilities in software or internet-connected systems, often need only a fraction of the time a human would to find and exploit vulnerable systems, and switch to other known attack methods when they meet a defence ([BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)). It adds that the number of internet-reachable AI agents such as ARTEX or CyberStrikeAI has almost doubled since October 2026, with no baseline or counting method given, names the two tools only as examples and does not say they were used in the Swiss cases, and expects an accumulation of fast, successful attacks ([BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)).

**Exposure:** internet-reachable systems with standard or easily guessed passwords or with known, unpatched vulnerabilities, which is what BACS says such agents exploit; BACS addresses its recommendations to companies in Switzerland and does not name administrations or sectors.

**Detection:** BACS recommends detecting when identities, applications, workloads and infrastructure deviate from their established behaviour patterns ([BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)); BACS says it shares technical indicators with critical-infrastructure operators and publishes none in the text.

**Defender takeaway:** BACS asks that critical security updates for internet-reachable systems be installed as soon as possible and at the latest after 24 hours (the BACS German text gives no start point; the official English page and SRF's report say after release) ([BACS, 2026-11-24](https://www.bacs.admin.ch/en/26-ki-agenten-1-en); [SRF, 2026-11-26](https://www.srf.ch/news/schweiz/fuenf-bestaetigte-faelle-erstmals-cyberangriffe-mit-ki-agenten-in-der-schweiz)), that access to exposed systems be limited by allow-list or geo-blocking, and that MFA or passkeys cover every internet-reachable internal resource without exception ([BACS, 2026-11-24](https://www.bacs.admin.ch/de/26-ki-agenten-1-de)). Check the internet-facing estate for default and guessable passwords and for patch lag against that 24-hour ceiling first.

## Update — 2026-11-28T04:41:50Z

BACS director Florian Schütz told SRF on 2026-11-26 that BACS currently has five confirmed cases of attacks with AI agents, all reported in recent days (translated from German) ([SRF, 2026-11-26](https://www.srf.ch/news/schweiz/fuenf-bestaetigte-faelle-erstmals-cyberangriffe-mit-ki-agenten-in-der-schweiz)). SRF reports that three victims are operators of critical infrastructure and that SMEs that reported voluntarily were also hacked with the help of AI agents, that systems were successfully hacked in four of the five cases (indirect speech, with no named speaker for that sentence), that there had been no larger outages, that it is still unclear who is behind the attacks and that BACS will not name the victims, who have the right to communicate themselves, in Schütz's words ([SRF, 2026-11-26](https://www.srf.ch/news/schweiz/fuenf-bestaetigte-faelle-erstmals-cyberangriffe-mit-ki-agenten-in-der-schweiz)). RTS, relaying the interview, reads three attacks on critical infrastructure of which two succeeded, without saying whether that count covers all five cases (translated from French) ([RTS, 2026-11-26](https://www.rts.ch/info/suisse/2026/article/cybersecurite-5-cyberattaques-menees-par-l-ia-en-suisse-29428554.html)), while BACS's own page of 2026-11-24, unchanged on 2026-11-28, still says that every case known to it ended in a compromise ([BACS, 2026-11-24](https://www.bacs.admin.ch/en/26-ki-agenten-1-en)). The three readings differ, so no single success ratio is a BACS finding. Neither SRF nor RTS says which sectors the three critical-infrastructure victims belong to, and neither outlet names a framework or a public administration. SRF also reports that BACS recommends installing critical updates at the latest 24 hours after their release ([SRF, 2026-11-26](https://www.srf.ch/news/schweiz/fuenf-bestaetigte-faelle-erstmals-cyberangriffe-mit-ki-agenten-in-der-schweiz)).
