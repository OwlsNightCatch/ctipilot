---
schema: 1
kind: incident
title: "WordPress supply-chain compromise via Awesome Motive's CDN backdoors ~1.2M sites"
headline: "WordPress supply-chain compromise via Awesome Motive's CDN backdoors ~1.2M sites"
summary: "WordPress supply-chain compromise via Awesome Motive's shared CDN tampered OptinMonster / TrustPulse / PushEngage scripts on ~1.2M sites to auto-create rogue admins and a self-hiding backdoor plugin — \"update your plugins\" did not protect the exposure window. (Sansec, 2026-06-13)"
discovered_at: "2026-06-16T05:08:54Z"
event_date: 2026-06-15
run_id: 2026-06-16-38d638e1
priority: high
immediate_action: null
tags:
  - supply-chain
  - data-breach
  - identity
regions:
  - global
sectors:
  - public-sector
  - technology
entities: []
cves: []
sources:
  - url: "https://sansec.io/research/optinmonster-supply-chain-attack"
    publisher: Sansec
    role: primary
  - url: "https://optinmonster.com/security-incident-tampered-script-served-via-optinmonster-and-trustpulse/"
    publisher: OptinMonster
    role: corroborating
  - url: "https://patchstack.com/articles/supply-chain-attack-on-optinmonster-trustpulse-and-pushengage-tampered-cdn-scripts-auto-creating-rogue-admins/"
    publisher: Patchstack
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
migrated_from: briefs/2026-06-16.md
---

Sansec Forensics found malicious JavaScript appended to the CDN-served `api.min.js` files shared by three Awesome Motive WordPress plugins — **OptinMonster (1.2M+ installs), TrustPulse and PushEngage** — injected on 12 June and served from CDN edges into 13 June ([Sansec, 2026-06-13](https://sansec.io/research/optinmonster-supply-chain-attack)). The vendor confirmed the entry point was exploitation of an **UpdraftPlus vulnerability** on its own marketing server, which leaked the BunnyNet CDN API key used to tamper the scripts ([OptinMonster, 2026-06-14](https://optinmonster.com/security-incident-tampered-script-served-via-optinmonster-and-trustpulse/)). Because the tampering was at the CDN layer and not in the WordPress.org repository, "update your plugins" gave false assurance for the exposure window. The payload waited for a logged-in administrator, then created a hidden admin account and installed a self-hiding backdoor plugin masquerading as "Content Delivery Helper" or "Database Optimizer", concealed from the plugin list, update checks and API responses, beaconing harvested credentials to a `tidio.cc` lookalike domain ([Patchstack, 2026-06-15](https://patchstack.com/articles/supply-chain-attack-on-optinmonster-trustpulse-and-pushengage-tampered-cdn-scripts-auto-creating-rogue-admins/)). Mapped to `T1195.002`, `T1136.001` (create account) and `T1027.005` (indicator removal).

**Defender takeaway:** any site running these three plugins with an admin logged in during 12–13 June UTC should be treated as potentially backdoored. Audit for unexpected admin accounts, compare the active-plugin list in the database against the filesystem to surface hidden plugins, and pin externally-loaded CDN scripts to Subresource Integrity hashes.
