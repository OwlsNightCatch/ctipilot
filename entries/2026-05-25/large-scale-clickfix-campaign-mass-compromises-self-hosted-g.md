---
schema: 1
kind: threat
horizon: operational
title: Large-scale ClickFix campaign mass-compromises self-hosted Ghost CMS sites via CVE-2026-26980
headline: Large-scale ClickFix campaign mass-compromises self-hosted Ghost CMS sites via CVE-2026-26980
summary: "XLab researchers at Qianxin documented an active, large-scale campaign weaponising the unauthenticated SQL-injection flaw CVE-2026-26980 against self-hosted Ghost CMS instances, with more than 700 compromised domains observed — among them university portals (Harvard, Oxford and Auburn are named), AI/SaaS companies …"
discovered_at: "2026-05-25T05:00:00Z"
event_date: 2026-05-24
run_id: 2026-05-25-d675ef38
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - actively-exploited
  - pre-auth
  - info-disclosure
  - phishing
regions:
  - global
  - europe
sectors:
  - education
  - media
  - technology
  - public-sector
entities: []
cves: []
sources:
  - url: "https://github.com/advisories/GHSA-w52v-v783-gw97"
    publisher: GitHub Security Advisory GHSA-w52v-v783-gw97
    role: primary
  - url: "https://blog.xlab.qianxin.com/ghost-cms-mass-compromised-via-cve-2026-26980-now-fueling-clickfix-attacks/"
    publisher: "XLab Qianxin, 2026-05-21"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/"
    publisher: "BleepingComputer, 2026-05-24"
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
migrated_from: briefs/2026-05-25.md
---

XLab researchers at Qianxin documented an active, large-scale campaign weaponising the unauthenticated SQL-injection flaw CVE-2026-26980 against self-hosted Ghost CMS instances, with more than 700 compromised domains observed — among them university portals (Harvard, Oxford and Auburn are named), AI/SaaS companies, media outlets, fintech firms, security sites and personal blogs, plus DuckDuckGo ([BleepingComputer, 2026-05-24](https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/); [XLab Qianxin, 2026-05-21](https://blog.xlab.qianxin.com/ghost-cms-mass-compromised-via-cve-2026-26980-now-fueling-clickfix-attacks/)). The intrusion is a two-stage operation: the attacker first exploits the pre-auth SQLi in Ghost's Content API to read the **admin API key** out of the database, then uses that key — which carries full content-management scope — to inject a lightweight JavaScript loader into published articles. The loader pulls a second-stage cloaking script that fingerprints each visitor; those who qualify are served a fake Cloudflare "verify you are human" prompt in an iframe overlaid on the article (the ClickFix / FakeCaptcha pattern) instructing them to paste a supplied command into the Windows Run dialog, which drops DLL loaders, JavaScript droppers, or an Electron-based sample (`UtilifySetup.exe`) ([BleepingComputer, 2026-05-24](https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/)).

**Why it matters to us:** self-hosted Ghost is used across EU/CH universities, NGOs and independent media — exactly the named victim profile — and the campaign weaponises a flaw patched back in February (6.19.1) against the still-unpatched long tail. The threat is two-sided: site operators face server-side compromise and admin-key theft (rotate the key and audit posts/themes for injected `<script>` even after patching, per § 2 and § 5), while *every visitor* to a compromised site is a ClickFix target. The client-side execution chain is the higher-value, product-agnostic hunt — `cmd.exe` / `powershell.exe` spawned from a browser process tree following a Run-dialog paste — and is worth hunting regardless of whether you run Ghost (.
