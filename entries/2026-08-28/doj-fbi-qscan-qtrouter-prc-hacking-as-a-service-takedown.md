---
schema: 1
kind: threat
horizon: operational
title: "DOJ/FBI seize domains behind QScan and QTRouter, the hacking-as-a-service platforms a PRC contractor sold to China's MSS and PLA — NASA, the Federal Reserve, DOJ, HHS, NIH and the US Senate named among the victims of activity DOJ dates to at least 2018, with European infrastructure among Lumen's own profiled targets"
headline: "A PRC state-enablement platform leasing commercial proxy subscriptions as anonymisation infrastructure has been seized — but blocklisting won't be durable"
summary: >
  DOJ and the FBI announced court-authorized domain seizures on 2026-08-26 against QScan and
  QTRouter, hacking-as-a-service platforms attributed to QTFY, a PRC state-sponsored contractor
  paid by China's Ministry of State Security. QScan is a reconnaissance pipeline; QTRouter turns
  compromised IoT devices, leased VPS and bulk-purchased Chinese commercial proxy subscriptions
  into an obfuscation network for downstream customers. Lumen's independent telemetry shows
  sustained targeting of research universities, defence-supplier perimeters and European
  infrastructure and judicial nodes.
discovered_at: "2026-08-28T06:05:00Z"
updated_at: null
event_date: "2026-08-26"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [nation-state, espionage, law-enforcement, botnet]
regions: [global, europe]
sectors: [public-sector, energy, education]
entities: [actor:qtfy, tool:qscan, tool:qtrouter]
techniques: [T1595, T1584.005, T1090.003, T1665]
affected_products: []
cves: []
sources:
  - url: "https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-platforms-operated-and-used-china-state-sponsored-hackers"
    publisher: "U.S. Department of Justice, Office of Public Affairs"
    date: "2026-08-26"
    role: primary
  - url: "https://www.lumen.com/blog/en-us/the-infrastructure-quartermaster-inside-a-china-nexus-state-enablement-model"
    publisher: "Lumen Technologies — Black Lotus Labs"
    date: "2026-08-26"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/fbi-disrupts-proxy-network-enabling-chinese-espionage-operations/"
    publisher: "BleepingComputer"
    date: "2026-08-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Among the victims of QTFY computer intrusion activity are the National Aeronautics and Space Administration, Federal Reserve, Department of Energy, Department of Justice, Department of Health and Human Services, National Institutes of Health, and the U.S. Senate."
    publisher: "U.S. Department of Justice"
  - quote: "Because the seized domains were hard-coded into both the QScan and QTRouter malware and used for essential tasks such as communication and authentication, the court-authorized seizures made QScan and QTRouter inoperable."
    publisher: "U.S. Department of Justice"
  - quote: "Systematic mapping of these remote-access boundaries is necessary to establish the required staging footprints that facilitate future lateral movement, maintain non-attributable backchannels, and conduct stealthy data-harvesting operations across multiple public sectors simultaneously."
    publisher: "Lumen Technologies — Black Lotus Labs"
  - quote: "Court documents reveal that the threat group includes former members of the Chinese People's Liberation Army military wing"
    publisher: "BleepingComputer"
verification: multi-source
sourcing_note: >
  DOJ's own press release and Lumen Black Lotus Labs' companion technical report (tracking the
  same infrastructure independently for over a year under the names "Fast Labyrinth"/"QTProxy")
  are both first-party primaries published the same day; BleepingComputer corroborates. Lumen's
  date-extraction tooling misread the blog page's own metadata as 2026-03-16 — an artefact, not
  the true publish date; DOJ's release states Lumen "also today" published the write-up, and every
  corroborating outlet dates it 2026-08-26.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [title, body]
migrated_from: null
---

DOJ and the FBI announced court-authorized domain seizures on 2026-08-26 against "QScan" and "QTRouter", two complementary hacking platforms unsealed court documents attribute to "QTFY" (aka QT/QTCYBER), a PRC state-sponsored contractor run by Nanjing Xinjiuwei Network Technology Company that received payments from China's Ministry of State Security. BleepingComputer's reporting of the unsealed court documents adds a staffing detail neither DOJ's nor Lumen's own material states directly: "Court documents reveal that the threat group includes former members of the Chinese People's Liberation Army military wing" ([BleepingComputer, 2026-08-26](https://www.bleepingcomputer.com/news/security/fbi-disrupts-proxy-network-enabling-chinese-espionage-operations/)). QScan is a three-stage reconnaissance pipeline — a Celery/RabbitMQ task broker, a distributed scanner fleet that rotates across /24 subnet blocks on a 30-day cycle to dodge threshold detection, and a Redis results backend — that fingerprints IoT devices, OS kernels and exposed management interfaces worldwide. QTRouter, which Lumen's Black Lotus Labs calls a "quartermaster" enablement layer after tracking the same infrastructure for over a year under the names "Fast Labyrinth" and "QTProxy", turns QScan-compromised IoT devices, leased VPS instances, and — most distinctively — bulk-purchased subscriptions to the Chinese "Airport" (机场) commercial GFW-circumvention proxy service into an obfuscation-as-a-service network: because the seized domains were hard-coded into both platforms for communication and authentication, "the court-authorized seizures made QScan and QTRouter inoperable" ([U.S. Department of Justice, 2026-08-26](https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-platforms-operated-and-used-china-state-sponsored-hackers)).

DOJ names NASA, the Federal Reserve, the Departments of Energy, Justice and Health and Human Services, NIH, and the U.S. Senate among the victims — "among the victims of QTFY computer intrusion activity are the National Aeronautics and Space Administration, Federal Reserve, Department of Energy, Department of Justice, Department of Health and Human Services, National Institutes of Health, and the U.S. Senate" — and, in a separate statement in the same release, dates the intrusion activity to at least 2018 ([U.S. Department of Justice, 2026-08-26](https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-platforms-operated-and-used-china-state-sponsored-hackers)). Lumen's independent telemetry additionally shows sustained QScan/Fast-Labyrinth targeting of research universities, defense-supplier perimeters, and — explicitly — European infrastructure and judicial nodes worldwide, describing the reconnaissance purpose plainly: "systematic mapping of these remote-access boundaries is necessary to establish the required staging footprints that facilitate future lateral movement, maintain non-attributable backchannels, and conduct stealthy data-harvesting operations across multiple public sectors simultaneously" ([Lumen Technologies — Black Lotus Labs, 2026-08-26](https://www.lumen.com/blog/en-us/the-infrastructure-quartermaster-inside-a-china-nexus-state-enablement-model)). Lumen found direct crossover between administrative check-in sessions from Nanjing (China Telecom/Unicom IP space) and the co-opted commercial proxy nodes — evidence the operators actively tested and calibrated the leased infrastructure before leasing it to downstream customers.

The takedown follows the same court-authorized disruption playbook DOJ/FBI used against Flax Typhoon (2024) and Volt Typhoon (2023) ORB networks. Lumen cautions that because the proxy layer rides on dynamically-rotating legitimate commercial subscriptions rather than a static botnet, blocklisting alone will not be durable, and recommends the CISA/NCSC ORB-mitigation guidance. For this constituency, the relevant read is not the US federal victim list but the infrastructure model itself: a hacking-as-a-service anonymisation layer leased to multiple PRC state customers, explicitly profiled by its own independent tracker as reaching European infrastructure and judicial systems, is the same class of ORB (operational relay box) infrastructure prior Volt Typhoon and Flax Typhoon disruptions have shown reaching European routers and critical-infrastructure networks.
