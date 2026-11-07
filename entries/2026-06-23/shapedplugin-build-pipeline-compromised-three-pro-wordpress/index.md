---
schema: 1
kind: incident
title: "ShapedPlugin build pipeline compromised — three Pro WordPress plugins backdoored to steal credentials, 2FA secrets and drop a web shell"
headline: "ShapedPlugin build pipeline compromised — three Pro WordPress plugins backdoored to steal credentials, 2FA secrets and drop a web shell"
summary: "Attackers compromised ShapedPlugin's Easy Digital Downloads update pipeline and backdoored three paid WordPress plugins (Product Slider Pro, Real Testimonials Pro, Smart Post Show Pro), harvesting admin credentials and 2FA secrets and dropping a self-deleting web-shell loader (CVE-2026-10735). Any site that took a Pro update between ~21 May and mid-June should be treated as fully compromised, not merely patched (Wordfence, 2026-06-22)."
discovered_at: "2026-06-23T04:52:44Z"
event_date: 2026-06-22
run_id: 2026-06-23-165387f6
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
  - retail
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
  - url: "https://thehackernews.com/2026/06/shapedplugin-wordpress-pro-plugins.html"
    publisher: The Hacker News
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
migrated_from: briefs/2026-06-23.md
---

Wordfence disclosed on 2026-06-22 that an attacker breached the build and Easy Digital Downloads (EDD) distribution pipeline of plugin vendor ShapedPlugin and injected backdoor code into the **Pro (paid)** releases of three products — Product Slider Pro for WooCommerce (before 3.5.4), Real Testimonials Pro (fixed in 3.2.5) and Smart Post Show Pro (before 4.0.2) — tracked as CVE-2026-10735 ([Wordfence, 2026-06-22](https://www.wordfence.com/blog/2026/06/psa-supply-chain-compromise-targets-shapedplugin-backdoored-pro-plugins-distributed-via-official-channels/); [BleepingComputer, 2026-06-22](https://www.bleepingcomputer.com/news/security/shapedplugin-update-flow-hacked-to-infect-wordpress-sites/)). The free versions hosted on the WordPress.org repository were not affected — only the licensed Pro updates pushed through EDD between roughly 21 May and 12–16 June carried the injection. The malicious code planted a `LicenseLoader.php` stub that executes when an administrator loads any wp-admin page; it calls out to a C2, downloads a second-stage payload, installs it as a hidden fake plugin (masquerading as `woocommerce-subscription` / `woocommerce-notification`), reports the victim domain, then deletes itself to frustrate forensics ([The Hacker News, 2026-06-22](https://thehackernews.com/2026/06/shapedplugin-wordpress-pro-plugins.html)). The second stage steals WordPress admin credentials, 2FA TOTP secrets, `wp-config.php` salts and database credentials, and maintains persistence through hidden REST API endpoints. Timestamp analysis pointed to an automated injection touching only four files inside a two-hour window — consistent with a pipeline-level compromise rather than manual tampering.

**Why it matters to us:** This is the "trusted update channel" supply-chain pattern again (cf. the W25 OptinMonster strand), and the operational consequence is that *patching is not remediation* — Wordfence's guidance is to treat any site that installed an affected Pro update as fully compromised. Detection concepts (no IOCs): hunt for a `LicenseLoader.php` in plugin directories; for installed plugins named `woocommerce-subscription` / `woocommerce-notification` that do not appear in the admin plugin list; for `php-fpm`/`apache2`/`nginx` child processes making outbound connections (Sysmon EID 1 with a web-server parent image, or `auditd` execve on PHP workers); and for `wp_users` rows with administrator role created after ~21 May. Mapped to `T1195.002` Compromise Software Supply Chain, `T1505.003` Server Software Component: Web Shell, `T1552.001` Unsecured Credentials: Credentials In Files. Remediation: update to the fixed Pro versions, then rotate **all** WordPress secrets — admin passwords, 2FA, DB credentials and `wp-config.php` salts — and review the WooCommerce order/SMTP-credential exposure.
