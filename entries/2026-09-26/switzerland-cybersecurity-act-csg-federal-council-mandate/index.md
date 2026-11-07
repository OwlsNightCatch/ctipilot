---
schema: 1
kind: policy
title: "Switzerland's Federal Council orders drafting of a standalone Cybersecurity Act (CSG), relocating the critical-infrastructure incident-reporting duty out of the Information Security Act"
headline: "Bern moves the critical-infrastructure breach-reporting duty into a new, standalone Cybersecurity Act"
summary: >
  Switzerland's Federal Council decided on 2026-09-25 to task the Federal
  Department of Defence, Civil Protection and Sport (VBS) with drafting a
  consultation proposal for a new standalone federal Cybersecurity Act (CSG),
  consolidating CRA-aligned product cyber-resilience rules, protection duties
  for important digital data, and hosting/cloud-provider obligations. The
  existing mandatory cyber-incident reporting duty for critical-infrastructure
  operators — in force under the Information Security Act (ISG) since April
  2025 — will move into the new CSG; a consultation draft is due by June 2027.
discovered_at: "2026-09-26T04:04:42Z"
updated_at: null
event_date: "2026-09-25"
run_id: 2026-09-26T0404Z-intel
priority: notable
immediate_action: null
tags: [policy]
regions: [switzerland]
sectors: [public-sector]
entities: ["policy:switzerland-cybersecurity-act-csg-2026", "policy:eu-cyber-resilience-act"]
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.bacs.admin.ch/de/newnsb/zX9oNK8tuI-Z"
    publisher: "Bundesamt für Cybersicherheit (BACS)"
    date: "2026-09-25"
    role: primary
  - url: "https://www.netzwoche.ch/news/2026-09-25/bundesrat-erteilt-auftrag-fuer-neues-cybersicherheitsgesetz"
    publisher: "Netzwoche"
    date: "2026-09-25"
    role: corroborating
  - url: "https://www.swisscybersecurity.net/news/2026-09-25/bundesrat-erteilt-auftrag-fuer-neues-cybersicherheitsgesetz"
    publisher: "SwissCybersecurity.net"
    date: "2026-09-25"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The Federal Council, at its session of 25 September 2026, tasked the Federal Department of Defence, Civil Protection and Sport (VBS), for the purpose of strengthening national cybersecurity, with drafting, by June 2027, a consultation proposal for a new, standalone federal Cybersecurity Act." # (translated from German)
    original: "Der Bundesrat hat an seiner Sitzung vom 25. September 2026 zur Stärkung der nationalen Cybersicherheit das Eidgenössische Departement für Verteidigung, Bevölkerungsschutz und Sport (VBS) beauftragt, bis im Juni 2027 eine Vernehmlassungsvorlage für ein neues, eigenständiges Bundesgesetz über die Cybersicherheit auszuarbeiten."
    publisher: "Bundesamt für Cybersicherheit (BACS)"
    source_url: "https://www.bacs.admin.ch/de/newnsb/zX9oNK8tuI-Z"
  - quote: "a standalone federal Cybersecurity Act (Cybersicherheitsgesetz, CSG) is to be created, into which the cyber-incident reporting duty for critical infrastructure operators, in effect under the ISG since April 2025, will also be transferred. The ISG will continue to govern the information security of federal authorities." # (translated from German)
    original: "soll ein eigenständiges Bundesgesetz über die Cybersicherheit (Cybersicherheitsgesetz, CSG) geschaffen werden, in welches auch die seit April 2025 geltende Meldepflicht für Cyberangriffe auf kritische Infrastrukturen aus dem ISG überführt wird. Das ISG regelt weiterhin die Informationssicherheit der Bundesbehörden."
    publisher: "Bundesamt für Cybersicherheit (BACS)"
    source_url: "https://www.bacs.admin.ch/de/newnsb/zX9oNK8tuI-Z"
  - quote: "The Federal Council has tasked the VBS with drafting a consultation proposal by June 2027 and submitting it for decision." # (translated from German)
    original: "Der Bundesrat hat das VBS beauftragt bis im Juni 2027 eine Vernehmlassungsvorlage auszuarbeiten und ihm zum Beschluss vorzulegen."
    publisher: "Bundesamt für Cybersicherheit (BACS)"
    source_url: "https://www.bacs.admin.ch/de/newnsb/zX9oNK8tuI-Z"
verification: single-source-national-cert
sourcing_note: >
  The Federal Office for Cybersecurity (BACS) published its own press release
  on the Federal Council's decision; Netzwoche and SwissCybersecurity.net
  carry the same wire-style article (same byline, same body) on two URLs, one
  syndicated treatment rather than a second independent assessor, so this is
  one first-party governmental statement under the government-authority
  carve-out. That syndicated article paraphrases the consultation-draft
  deadline as "summer 2027," while BACS's own release states "bis im Juni
  2027" (by June 2027) twice; this entry follows the
  primary verbatim over the secondary paraphrase.
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
updates: []
migrated_from: null
---

Switzerland's Federal Council decided at its session of 2026-09-25 to task the Federal Department of Defence, Civil Protection and Sport (VBS) with drafting, by June 2027, a consultation proposal for a new, standalone federal Cybersecurity Act (Bundesgesetz über die Cybersicherheit, CSG) ([Bundesamt für Cybersicherheit, 2026-09-25](https://www.bacs.admin.ch/de/newnsb/zX9oNK8tuI-Z)). The CSG folds together three previously separate parliamentary mandates the Federal Office for Cybersecurity (BACS) had been developing as amendments to the existing Information Security Act (ISG): binding cyber-resilience requirements for manufacturers, importers and retailers of hardware and software products, explicitly modeled on the EU Cyber Resilience Act to ease compliance for internationally active firms already subject to it; strengthened protection duties for particularly important digital data; and participation and defense obligations for hosting and cloud providers ([Bundesamt für Cybersicherheit, 2026-09-25](https://www.bacs.admin.ch/de/newnsb/zX9oNK8tuI-Z)).

Most consequential for the constituency this brief serves: the existing mandatory cyber-incident reporting duty for critical-infrastructure operators, in effect under the ISG since April 2025, is being relocated out of the ISG and into the new CSG; the ISG itself will continue to govern only the information security of federal authorities ([Bundesamt für Cybersicherheit, 2026-09-25](https://www.bacs.admin.ch/de/newnsb/zX9oNK8tuI-Z)). Sector-specific rules under the Telecommunications Act, the Electricity Supply Ordinance and the Telecommunications Installations Ordinance are left untouched, with the CSG framed as supplementing them with cross-cutting duties. No operational obligation changes today: this is a drafting mandate with a June 2027 consultation-draft deadline, not yet a bill, but it settles the future statutory home of the incident-reporting duty that federal, cantonal and communal critical-infrastructure operators already comply with, and signals that product-cyber-resilience and hosting/cloud-provider obligations comparable to the EU CRA are coming to Switzerland as a dedicated instrument rather than an ISG amendment.
