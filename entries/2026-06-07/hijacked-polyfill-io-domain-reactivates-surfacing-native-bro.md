---
schema: 1
kind: incident
horizon: operational
title: "Hijacked polyfill[.]io domain reactivates, surfacing native browser credential prompts on sites that never removed legacy script tags"
headline: "Hijacked polyfill[.]io domain reactivates, surfacing native browser credential prompts on sites that never removed legacy script tags"
summary: "The hijacked polyfill[.]io CDN domain reactivated and is throwing HTTP 401 prompts, surfacing native browser credential dialogs on sites that never stripped legacy script tags. Toshiba and Muji issued public warnings; audit web properties for residual polyfill[.]io references (BleepingComputer, 2026-06-05)."
discovered_at: "2026-06-07T05:00:00Z"
event_date: 2026-06-05
run_id: 2026-06-07-0885f123
priority: high
immediate_action: null
tags:
  - supply-chain
  - phishing
  - data-breach
regions:
  - apac
  - global
sectors:
  - technology
  - retail
  - manufacturing
entities: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.global.toshiba/jp/top/info-20260602.html"
    publisher: Toshiba — customer notice
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
migrated_from: briefs/2026-06-07.md
---

The `polyfill[.]io` CDN domain — seized and weaponised in the June 2024 supply-chain attack that affected more than 100,000 sites — became active again in late May 2026 and began answering with HTTP 401 authentication challenges, which browsers render as native credential dialog boxes ([BleepingComputer, 2026-06-05](https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/)). Any site still loading a `<script src="…polyfill[.]io…">` tag — a failure documented across many organisations since 2024 — now prompts visitors for credentials in a dialog that appears to originate from the trusted site. Toshiba published a warning on 2026-06-02 telling users to click *Cancel* without entering anything ([Toshiba, 2026-06-02](https://www.global.toshiba/jp/top/info-20260602.html)); Muji issued a parallel notice stating it had not confirmed unauthorised access or data leakage ([BleepingComputer, 2026-06-05](https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/)). This is mechanically distinct from the 2024 redirect-to-malicious-JavaScript attack: the harm here is HTTP-401-induced credential phishing, not script injection, so neither party has confirmed exfiltration — but both advised affected users to change passwords. Maps to `T1195.002` (Compromise Software Supply Chain).
**Why it matters to us:** The exposure is entirely a function of stale third-party references, which most organisations underestimate. Grep all rendered HTML, CMS templates, and CDN-inclusion lists for `polyfill[.]io` with any subdomain or path; replace with the legitimate `polyfill.com` / `polyfill.top` mirrors or self-hosted polyfills, and enforce Subresource Integrity (SRI) on all third-party scripts. Web-proxy/SWG logs showing 401 responses from `polyfill[.]io` pinpoint pages that still load the script.
