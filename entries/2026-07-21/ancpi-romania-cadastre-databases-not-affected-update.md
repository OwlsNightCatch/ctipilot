---
schema: 1
kind: incident
horizon: operational
title: "ANCPI (Romania cadastre): agency says core databases were NOT compromised, contradicting ByteToBreach's destruction claim; Gov Cloud migration to complete 22 July"
headline: "Romania's cadastre authority disputes the attacker's database-wipe claim as it moves e-Terra to Government Cloud"
summary: >
  Update on the ANCPI (Romanian National Agency for Cadastre) cyberattack: on 2026-07-20 the agency
  stated, after security verification, that its technical and legal databases "have not been affected" —
  directly contradicting data-leak operator ByteToBreach's claim of deleting backups after a failed
  extortion. ANCPI is migrating its applications to the Romanian Government Cloud, expected to finish
  22 July, before any phased service restoration. KELA separately profiled the ByteToBreach operator;
  the contradiction between the wipe claim and the "databases intact" statement is itself the notable
  fact — both are held, neither is resolved.
discovered_at: "2026-07-21T04:45:00Z"
event_date: "2026-07-20"
run_id: 2026-07-21T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, hacktivism, ransomware]
regions: [europe]
sectors: [public-sector]
entities: [actor:bytetobreach, incident:ancpi-romania-cyberattack-2026-07]
techniques: [T1078, T1485, T1490]
affected_products: []
cves: []
sources:
  - url: "https://www.digi24.ro/stiri/actualitate/agentia-nationala-de-cadastru-spune-ca-bazele-de-date-nu-au-fost-afectate-cand-se-reiau-serviciile-3870161"
    publisher: "Digi24 (Romania)"
    date: "2026-07-20"
    role: primary
  - url: "https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/"
    publisher: "Risky Business News"
    date: "2026-07-20"
    role: corroborating
  - url: "https://www.kelacyber.com/blog/bytetobreach-a-deep-dive-into-a-persistent-data-leak-operator/"
    publisher: "KELA Cyber Intelligence Center"
    date: "2026-07-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The hacker entered using valid credentials, mapped internal systems, and wiped systems and backups after failing to extort the agency."
    publisher: "Risky Business News"
  - quote: "KELA assesses the actor behind the campaign, ByteToBreach, is likely operated by Zakaria Mahdjoub, an individual based in Oran, Algeria."
    publisher: "KELA Cyber Intelligence Center"
verification: contradicted
sourcing_note: "Genuine contradiction on impact: ANCPI (via Digi24) states databases were not affected; ByteToBreach claims (screenshots alongside a data-sale listing) it deleted backups after failed extortion, relayed by Risky Business News. Both are reported; neither is independently confirmed. The KELA operator attribution is a separate, corroborating analytical profile."
confidence: medium
update_of: 2026-07-19/ancpi-romania-cadastre-cyberattack-bytetobreach
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-07-19):** The still-open ANCPI (Romanian National Agency for Cadastre and Real Estate Publicity) incident developed on two fronts. First, an impact contradiction: on 2026-07-20 ANCPI stated publicly, following completed security verification, that its technical and legal databases had not been affected ([Digi24, 2026-07-20](https://www.digi24.ro/stiri/actualitate/agentia-nationala-de-cadastru-spune-ca-bazele-de-date-nu-au-fost-afectate-cand-se-reiau-serviciile-3870161)) — squarely against extortion operator ByteToBreach's earlier claim, reported by Risky Business News, that the "hacker entered using valid credentials, mapped internal systems, and wiped systems and backups after failing to extort the agency" ([Risky Business News, 2026-07-20](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/)). The agency frames the multi-day e-Terra/RENNS outage (down since 14 July) as deliberate protective isolation and says it is migrating applications to the Romanian Government Cloud, coordinated by the Special Telecommunications Service, expected to complete 22 July before any phased service restoration.

Second, actor context: KELA's updated profile assesses ByteToBreach is likely a single operator based in Oran, Algeria, active since June 2025 across forums, Dread, Telegram and a storefront, with a victim set spanning government, banking, airline and university targets across several countries, and access methods documented as cloud/corporate-infrastructure exploitation, reuse of infostealer/phishing-harvested credentials, and brute force ([KELA, 2026-07-17](https://www.kelacyber.com/blog/bytetobreach-a-deep-dive-into-a-persistent-data-leak-operator/)). **Defender takeaway:** the contradiction is unresolved and should be held both ways rather than settled — an agency "databases intact" statement and an attacker "backups wiped" claim can both be partially true (e.g. production preserved, some systems/backups damaged). For CH/EU cantonal and national registries the transferable pattern is concrete: valid-credential entry followed by destructive follow-through after a failed extortion is a documented combined objective against national e-government/cadastre platforms, independent of any software CVE, so identity-plane monitoring and offline, integrity-verified registry backups are the controls that matter for this class of target.
