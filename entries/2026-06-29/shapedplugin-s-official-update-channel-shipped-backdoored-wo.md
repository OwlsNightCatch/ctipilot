---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-top-stories
title: "ShapedPlugin's official update channel shipped backdoored WordPress Pro plugins — credential, 2FA-secret and web-shell theft"
headline: "ShapedPlugin's official update channel shipped backdoored WordPress Pro plugins — credential, 2FA-secret and web-shell theft"
summary: "ShapedPlugin's official WordPress update channel shipped backdoored Pro plugins — credential, 2FA-secret and web-shell theft straight from the trusted pipeline. (daily 06-23, Wordfence)"
discovered_at: "2026-06-29T00:20:54Z"
event_date: 2026-06-22
run_id: 2026-W26-b78503e7
priority: high
immediate_action: null
tags:
  - supply-chain
  - data-breach
  - actively-exploited
  - patch-available
regions:
  - global
  - europe
sectors:
  - technology
  - public-sector
entities: []
cves:
  - id: CVE-2026-10735
    cvss: "9.8"
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - exploited
      - patch-available
sources:
  - url: "https://www.wordfence.com/blog/2026/06/psa-supply-chain-compromise-targets-shapedplugin-backdoored-pro-plugins-distributed-via-official-channels/"
    publisher: Wordfence
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/shapedplugin-update-flow-hacked-to-infect-wordpress-sites/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence:
  - quote: "Attackers compromised the vendor's build and distribution pipeline, injecting backdoor code into Pro plugin releases distributed through official licensed update channels"
    publisher: Wordfence
  - quote: "The malicious packages contained a file named LicenseLoader.php, which was loaded automatically within the WordPress admin panel ... downloaded a second-stage payload, installed it as a fake plugin ... and then deleted itself to hinder forensic analysis"
    publisher: BleepingComputer
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
migrated_from: briefs/weekly/2026-W26.md
---

**If you did nothing this week:** any site running the ShapedPlugin Pro plugins that auto-updated through the licensed channel pulled backdoor code straight from the vendor — patch level was no defence, because the trusted distribution pipeline itself was the attacker. The malicious `LicenseLoader.php` loads inside the WordPress admin panel, fetches a second stage, installs it as a fake plugin and self-deletes to frustrate forensics.

Wordfence [disclosed on 2026-06-22](https://www.wordfence.com/blog/2026/06/psa-supply-chain-compromise-targets-shapedplugin-backdoored-pro-plugins-distributed-via-official-channels/) that an attacker breached ShapedPlugin's build and Easy Digital Downloads distribution pipeline and injected backdoor code into the Pro (paid) releases of three plugins, served through official update channels. The implant harvests credentials and 2FA secrets and drops a web shell ([BleepingComputer](https://www.bleepingcomputer.com/news/security/shapedplugin-update-flow-hacked-to-infect-wordpress-sites/)). For a public-sector or education estate that runs WordPress behind a CMS team, the hunt is for the fake-plugin artefact and unexpected `LicenseLoader.php` execution in the admin context, plus credential/2FA rotation for any admin who logged in during the exposure window — not merely "update the plugin." ([daily 06-23](/briefs/2026-06-23/))
