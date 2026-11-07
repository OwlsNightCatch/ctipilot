---
schema: 1
kind: incident
title: "The hijacked Polyfill CDN domain came back online answering HTTP 401, so leftover script tags raised browser sign-in prompts on Toshiba, Muji and other sites"
headline: "Leftover Polyfill script tags raised browser sign-in prompts on Toshiba and Muji sites once the hijacked domain answered HTTP 401"
summary: >
  From late May 2026 the Polyfill CDN domain hijacked in 2024 answered requests with HTTP 401 authentication
  challenges, so browsers on pages that still loaded its script showed a native sign-in dialog. Toshiba, Muji,
  Samsung and several Japanese companies saw the prompts on their sites. Toshiba told users to cancel and to
  change any password they had typed in; there is no indication sites were hacked or credentials stolen.
discovered_at: "2026-06-07T05:00:00Z"
event_date: 2026-06-05
run_id: 2026-06-07-0885f123
priority: notable
immediate_action: null
tags: [supply-chain, phishing]
regions: [apac, global]
sectors: [technology, retail, manufacturing]
entities: ["incident:polyfill-io-domain-reactivates-http-401-credential-prompts"]
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/"
    publisher: "BleepingComputer"
    date: "2026-06-05"
    role: primary
  - url: "https://www.global.toshiba/jp/top/info-20260602.html"
    publisher: "Toshiba"
    date: "2026-06-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "At the moment, there is no indication that impacted websites were hacked or that credentials entered on these rogue login screens were stolen."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/"
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
techniques: [T1195.001, T1056.002]
affected_products: []
classification:
  reliability: B
  credibility: 2
migrated_from: briefs/2026-06-07.md
updates:
  - at: "2026-10-11T15:08:32Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      Re-verified against BleepingComputer and Toshiba's notice. The defanged domain is removed from the title, headline, summary and body. The replacement advice named two domains that BleepingComputer ties to the service's 2024 relaunch, not to a vetted mirror, and called Subresource Integrity a fix, which does not stop an HTTP 401 prompt; the takeaway now follows the creator's recommendation to remove the reference. Added the further affected companies, Toshiba's 2026-06-04 resolution, the rating, the ATT&CK mapping and the registry link; priority high to notable.
    fields: [title, headline, summary, priority, tags, entities, techniques, affected_products, sources, evidence, classification, update_of, body]
---

Starting in late May 2026, the Polyfill CDN domain that was bought and used to serve malicious scripts in 2024 became active again and answered requests with HTTP 401 authentication challenges, which a browser shows as its own username and password dialog ([BleepingComputer, 2026-06-05](https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/)). Pages that still loaded the Polyfill script two years after the service was abandoned therefore raised a sign-in prompt that looked as if it came from the site itself. Toshiba warned on 2026-06-02 that parts of its website showed such a screen, asked users to choose Cancel without typing anything, told anyone who had entered a username and password to change it at every service that uses it, and added on 2026-06-04 that the screen no longer appears ([Toshiba, 2026-06-02](https://www.global.toshiba/jp/top/info-20260602.html)). Muji published a similar warning, and Japanese media reported Zojirushi, FiNC Technologies, Ishiyaku Publishers and Hobonichi affected, while a researcher saw the prompt on Samsung Smart TVs and websites on 2026-06-01; there is no indication the sites were hacked or that typed credentials were stolen ([BleepingComputer, 2026-06-05](https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/)).

**Exposure:** any web page, CMS template or embedded web view that still references the original Polyfill CDN domain; the site has to load nothing new for its visitors to be prompted ([BleepingComputer, 2026-06-05](https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/)).

**Detection:** in web proxy or secure web gateway logs, browser requests to the original Polyfill CDN domain answered with HTTP 401 identify the pages that still embed it, through their referrer; a source-code or rendered-HTML search across the organization's web properties finds the same references before a visitor does.

**Defender takeaway:** remove the Polyfill reference outright rather than switching it to another host, as the project's creator recommended in 2024, and treat any credentials users report typing into the prompt as exposed ([BleepingComputer, 2026-06-05](https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/)).

## Correction — 2026-10-11T15:08:32Z

The earlier text advised moving the script to two other domains. BleepingComputer describes those domains as the service's relaunch after the 2024 incident, not as vetted mirrors, and the project's creator recommended removing the service ([BleepingComputer, 2026-06-05](https://www.bleepingcomputer.com/news/security/suspicious-polyfill-login-prompts-pop-up-on-toshiba-muji-websites/)). The earlier text also recommended Subresource Integrity, which does not stop a browser from showing the sign-in prompt for an HTTP 401 answer. Toshiba reported on 2026-06-04 that the prompt no longer appears on its site ([Toshiba, 2026-06-02](https://www.global.toshiba/jp/top/info-20260602.html)). The priority moves from high to notable: the prompts collected nothing that is known to have been stolen, and the fix is a cleanup.
