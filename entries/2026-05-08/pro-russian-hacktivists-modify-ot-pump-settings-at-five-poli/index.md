---
schema: 1
kind: threat
title: "Poland's ABW: attackers breached five municipal water treatment plants in 2025 and in some cases altered equipment parameters, and hacktivists exploited weak passwords on exposed management panels at municipal sites"
headline: "ABW reports breaches at five Polish water plants in 2025, with equipment settings altered in some cases, naming no actor or access route"
summary: >
  Poland's Internal Security Agency (ABW) reports that in 2025 attackers breached water treatment
  plants in Jabłonna Lacka, Szczytno, Małdyty, Tolkmicko and Sierakowo and, where they reached the
  industrial control systems, altered equipment parameters, putting operation and water supply at
  risk. It names no actor or access vector for these breaches. In a separate passage on municipal
  infrastructure, ABW describes hacktivist groups exploiting poor password policies and device
  management panels exposed directly to the internet.
discovered_at: "2026-05-08T05:00:02Z"
updated_at: "2026-05-09T05:00:14Z"
event_date: 2026-05-06
run_id: 2026-05-08-migrated
priority: notable
immediate_action: null
tags:
  - hacktivism
  - ot-ics
  - actively-exploited
regions:
  - europe
sectors:
  - water
  - public-sector
entities: []
techniques: [T1078]
affected_products: []
cves: []
sources:
  - url: "https://www.abw.gov.pl/download/24/4877/InternalSecurityAgencyABW2024-2025Selectedactvities.pdf"
    publisher: "ABW (Internal Security Agency), Internal Security Agency ABW 2024-2025: Selected activities"
    date: "2026-05-25"
    role: primary
  - url: "https://cyberdefence24.pl/cyberbezpieczenstwo/ataki-na-wodociagi-abw-o-widocznosci-obiektow-z-internetu"
    publisher: "CyberDefence24"
    date: "2025-10-08"
    role: corroborating
  - url: "https://www.abw.gov.pl/pl/aktualnosci/2815,Agencja-Bezpieczenstwa-Wewnetrznego-2024-2025-Wybrane-aktywnosci.html"
    publisher: "ABW (Internal Security Agency), news release: Agencja Bezpieczeństwa Wewnętrznego 2024-2025. Wybrane aktywności"
    date: "2026-05-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "By gaining access, in some cases, to industrial control systems, the attackers were able to alter the technical parameters of the equipment"
    publisher: "ABW (Internal Security Agency), Internal Security Agency ABW 2024-2025: Selected activities"
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-05-09T05:00:14Z"
    run_id: 2026-05-09-migrated
    type: update
    summary: "UPDATE (originally covered 2026-05-08):"
    fields:
      - entities
      - sectors
      - sources
      - body
    merged_from: 2026-05-09/polish-water-ot-intrusions-abw-annual-report-names-five-faci
  - at: "2026-09-30T07:12:19Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      The earlier text said pro-Russian hacktivists modified pump settings at all five facilities,
      with manual overrides preventing disruption, that ABW attributed the intrusions to APT28,
      APT29 and UNC1151 and to hacktivists exploiting flat IT/OT networks, and it described Poland's
      NIS2 transposition. ABW's 2024-2025 activity review names the five plants and says that in
      some cases the attackers reached industrial control systems and altered equipment parameters,
      but it names no actor or access vector. ABW's press office has said the potentially
      compromised operators had internet-reachable IT resources, including HMI panels. ABW released
      the review in Polish on 2026-05-06 and in English on 2026-05-25, not on 2026-05-07. The
      priority moves from high to notable.
    fields: [title, headline, summary, event_date, priority, tags, entities, techniques, sources, evidence, classification, body, verification]
migrated_from: briefs/2026-05-08.md
---

Poland's Internal Security Agency (ABW) reports in its 2024-2025 activity review that in 2025 "security breaches were reported at water treatment plants in the following towns: Jabłonna Lacka, Szczytno, Małdyty, Tolkmicko and Sierakowo", and that "by gaining access, in some cases, to industrial control systems, the attackers were able to alter the technical parameters of the equipment", a direct risk to the plants' continued operation and to water supply ([ABW, 2026-05-25](https://www.abw.gov.pl/download/24/4877/InternalSecurityAgencyABW2024-2025Selectedactvities.pdf)). ABW describes hacktivist groups as particularly active against municipal infrastructure and says they "exploited glaring vulnerabilities in the form of poor password policies and unsecured device management panels, accessible directly via the public internet" ([ABW, 2026-05-25](https://www.abw.gov.pl/download/24/4877/InternalSecurityAgencyABW2024-2025Selectedactvities.pdf)). The report names no actor and no access vector for the water-plant breaches and does not tie them to the hacktivist activity. The state-sponsored groups it names, APT28, APT29 and UNC1151, are described as carrying out "sophisticated, long-term espionage and sabotage operations" ([ABW, 2026-05-25](https://www.abw.gov.pl/download/24/4877/InternalSecurityAgencyABW2024-2025Selectedactvities.pdf)). ABW's press office told CyberDefence24 that the potentially compromised water and sewage operators had IT resources reachable from the public internet, including HMI panels controlling their processes ([CyberDefence24, 2025-10-08](https://cyberdefence24.pl/cyberbezpieczenstwo/ataki-na-wodociagi-abw-o-widocznosci-obiektow-z-internetu)). CyberDefence24, which lists the five plants among the sites hit, describes the attacks on the Polish water sector as the work of pro-Russian hacktivists ([CyberDefence24, 2025-10-08](https://cyberdefence24.pl/cyberbezpieczenstwo/ataki-na-wodociagi-abw-o-widocznosci-obiektow-z-internetu)).

**Exposure:** municipal infrastructure operators, which ABW says include sewage and water treatment plants and waste incinerators, whose device management panels answer from the internet and accept weak passwords, the weaknesses ABW says hacktivist groups exploited ([ABW, 2026-05-25](https://www.abw.gov.pl/download/24/4877/InternalSecurityAgencyABW2024-2025Selectedactvities.pdf)).

**Detection:** successful logins to HMI, PLC or device management interfaces from internet addresses, and changes to setpoints or equipment parameters that match no operator log.

**Defender takeaway:** ABW's report does not say how the five plants were breached, but its press office points to internet-reachable IT resources and HMI panels at the potentially compromised operators ([CyberDefence24, 2025-10-08](https://cyberdefence24.pl/cyberbezpieczenstwo/ataki-na-wodociagi-abw-o-widocznosci-obiektow-z-internetu)). The route ABW describes for hacktivists against municipal infrastructure, an internet-reachable management panel with a weak password ([ABW, 2026-05-25](https://www.abw.gov.pl/download/24/4877/InternalSecurityAgencyABW2024-2025Selectedactvities.pdf)), is closed by removing direct internet exposure of OT interfaces and enforcing unique strong credentials on them.

## Update — 2026-05-09T05:00:14Z

ABW's 2024-2025 activity review, published in Polish on 2026-05-06 with an English edition dated 2026-05-25 ([ABW, 2026-05-06](https://www.abw.gov.pl/pl/aktualnosci/2815,Agencja-Bezpieczenstwa-Wewnetrznego-2024-2025-Wybrane-aktywnosci.html)), names the five affected facilities: Jabłonna Lacka, Szczytno, Małdyty, Tolkmicko and Sierakowo ([ABW, 2026-05-25](https://www.abw.gov.pl/download/24/4877/InternalSecurityAgencyABW2024-2025Selectedactvities.pdf)). It names no actor and no access vector for the water-plant intrusions ([ABW, 2026-05-25](https://www.abw.gov.pl/download/24/4877/InternalSecurityAgencyABW2024-2025Selectedactvities.pdf)).

## Correction — 2026-09-30T07:12:19Z

The earlier text said pro-Russian hacktivists modified pump settings at all five facilities and that manual overrides prevented disruption. It also said ABW attributed these intrusions to APT28, APT29 and UNC1151, and that ABW attributed the five plant breaches to pro-Russian hacktivists exploiting flat IT/OT networks, in a pattern like NoName057(16) and Cyber Army of Russia Reborn campaigns, and it detailed Poland's NIS2 transposition. It dated ABW's report 2026-05-07. ABW released the review in Polish on 2026-05-06 and in English on 2026-05-25 ([ABW, 2026-05-06](https://www.abw.gov.pl/pl/aktualnosci/2815,Agencja-Bezpieczenstwa-Wewnetrznego-2024-2025-Wybrane-aktywnosci.html)). ABW's report names no actor and no access vector for the water-plant breaches. It says breaches were reported at the five plants and that, "in some cases", the attackers reached industrial control systems and altered the technical parameters of the equipment ([ABW, 2026-05-25](https://www.abw.gov.pl/download/24/4877/InternalSecurityAgencyABW2024-2025Selectedactvities.pdf)).
