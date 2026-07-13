---
schema: 1
kind: incident
horizon: operational
title: "AIVD/MIVD: Russia-linked actors hijack default-credential IP cameras along NATO military-supply routes to monitor Ukraine-bound shipments"
headline: "Dutch intelligence: Russia hijacked default-credential internet cameras along military-supply routes; four EU states summon Russian ambassadors"
summary: >
  AIVD and MIVD disclosed that Russia-linked actors compromised internet-connected cameras — reachable because
  they still used default passwords or outdated firmware, including cameras operated by businesses along the
  routes — carrying military supplies to Ukraine through the Netherlands, to watch the shipments and equipment
  being moved. The 2026-07-13 diplomatic
  escalation (NL/France/Germany/Finland ambassador summons, NATO condemnation) followed. Transferable lesson:
  internet-exposed cameras/IoT are treated as a state-actor surveillance grid.
discovered_at: "2026-07-13T20:36:00Z"
event_date: "2026-07-11"
run_id: 2026-07-13T2009Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, russia-nexus]
regions: [europe, dach, nordics]
sectors: [public-sector, defense, transport]
entities: [campaign:russia-ip-camera-hijacking-nato-supply-routes-2026]
techniques: [T1078.001, T1190]
affected_products: []
cves: []
sources:
  - url: "https://nltimes.nl/2026/07/11/dutch-spy-agencies-russia-hacked-cameras-spy-military-routes"
    publisher: "NL Times (ANP)"
    date: "2026-07-11"
    role: primary
  - url: "https://nltimes.nl/2026/07/13/netherlands-summons-russian-ambassador-russias-hacking-military-supply-routes"
    publisher: "NL Times (ANP)"
    date: "2026-07-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Dutch intelligence services disclosed Friday that Russian actors had compromised “a small number of cameras” on routes for military shipments to Ukraine. The breaches allowed the hackers remote viewing access, according to statements from the General Intelligence and Security Service (AIVD) and the Military Intelligence and Security Service (MIVD)."
    publisher: "NL Times (ANP)"
  - quote: "We strongly condemn the persistent malicious cyber activities of Russia. The country uses its cyber ecosystem to attack allies and NATO partners."
    publisher: "NL Times (ANP)"
verification: single-source
sourcing_note: "The substance is a first-party disclosure by the Dutch national intelligence authorities AIVD/MIVD for their own jurisdiction, reported via the ANP wire (NL Times); marked single-source because the agencies' own bulletin was not directly reachable this run and the two cited URLs are both ANP-sourced (not independent). The disclosure was independently carried by multiple outlets (Ukrainska Pravda, UNITED24, APA per search) but those could not be fetched cleanly, which is why credibility is held at 2. No named Russian APT cluster was stated in this disclosure — an earlier allied attribution of similar camera-targeting to APT28/GRU Unit 26165 is background only and is not carried here as attribution."
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Dutch intelligence services AIVD (General Intelligence and Security Service) and MIVD (Military Intelligence and Security Service) disclosed on 2026-07-11 that Russia-linked actors compromised "a small number" of internet-connected cameras positioned along routes used to move military supplies to Ukraine through the Netherlands — including cameras operated by businesses located on those routes — giving the operators remote viewing access to the shipments and equipment being moved ([NL Times/ANP, 2026-07-11](https://nltimes.nl/2026/07/11/dutch-spy-agencies-russia-hacked-cameras-spy-military-routes)). The agencies state the cameras were reachable chiefly because they "still us[e] default passwords or outdated firmware" — weak/default-credential abuse and unpatched embedded firmware on internet-exposed devices, not a bespoke exploit chain. On 2026-07-13, after EU ministerial consultations in Brussels, the Netherlands summoned the Russian ambassador; France, Germany and Finland took the same step over related espionage and sabotage concerns, and NATO issued a joint statement condemning "the persistent malicious cyber activities of Russia" ([NL Times/ANP, 2026-07-13](https://nltimes.nl/2026/07/13/netherlands-summons-russian-ambassador-russias-hacking-military-supply-routes)). AIVD/MIVD separately warned businesses located along military-logistics routes to harden their camera and IoT security. This is a distinct technical story from the same-day FSB Centre 16 router-hijacking advisory and the Turla espionage attribution covered separately today — here the compromised asset class is consumer/commercial IP cameras used for physical-logistics surveillance.

**Defender takeaway:** the transferable lesson reaches any critical-infrastructure operator, not only those on a logistics route — a state actor is treating internet-exposed cameras, DVRs/NVRs and smart-building IoT with default credentials or unpatched firmware as a physical-surveillance sensor grid. Inventory internet-reachable camera and IoT devices across your estate, and in egress/flow telemetry watch for outbound video/RTSP or streaming sessions from those devices to destinations outside the expected vendor-cloud or monitoring endpoints. **Triage:** many IP cameras legitimately stream to a vendor cloud or an on-prem NVR — the discriminator is a camera establishing an interactive or streaming session to an unfamiliar external destination that is neither its vendor cloud nor the site's own recorder, particularly a device still answering on a factory-default credential from the public internet.
