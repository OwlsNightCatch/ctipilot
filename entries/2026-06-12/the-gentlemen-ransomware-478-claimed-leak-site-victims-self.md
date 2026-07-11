---
schema: 1
kind: threat
horizon: operational
title: "The Gentlemen ransomware: 478 claimed leak-site victims, self-propagating Go encryptor, operator publicly named"
headline: "The Gentlemen ransomware: 478 claimed leak-site victims, self-propagating Go encryptor, operator publicly named"
summary: "The Gentlemen RaaS claims 478 leak-site victims (concentrated in Thailand, the UK, Brazil, Germany and India per THN); Krebs publishes an operator deanonymisation, and Microsoft's dissection details the encryptor's --spread worm mode (KrebsOnSecurity, 2026-06-10)."
discovered_at: "2026-06-12T05:00:02Z"
event_date: 2026-06-11
run_id: 2026-06-12-5ab9a319
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
regions:
  - europe
  - global
sectors:
  - education
  - healthcare
  - transport
  - finance
entities:
  - "actor:thegentlemen"
cves: []
sources:
  - url: "https://krebsonsecurity.com/2026/06/who-runs-the-ransomware-group-the-gentlemen/"
    publisher: KrebsOnSecurity
    role: primary
  - url: "https://www.microsoft.com/en-us/security/blog/2026/05/28/the-gentlemen-ransomware-dissecting-a-self-propagating-go-encryptor/"
    publisher: Microsoft Threat Intelligence
    role: corroborating
  - url: "https://thehackernews.com/2026/06/the-gentlemen-ransomware-claims-478.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/"
    publisher: Check Point Research
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
migrated_from: briefs/2026-06-12.md
---

The Gentlemen — tracked by Microsoft as Storm-2697 and by PRODAFT as Phantom Mantis / LARVA-368 — has claimed 478 victims on its leak site, with victims concentrated in Thailand, the UK, Brazil, Germany and India ([The Hacker News, 2026-06-11](https://thehackernews.com/2026/06/the-gentlemen-ransomware-claims-478.html)). Microsoft's technical dissection details a Go encryptor obfuscated with Garble: per-file ephemeral Curve25519 key pairs with XChaCha20 (the ephemeral public key is appended to each encrypted file after an `--eph--` marker), a `--spread` argument that "turns the malware from a single-host encryptor into a self-propagating worm" — simultaneously abusing network shares, scheduled tasks and remote process execution ([T1021.002](https://attack.mitre.org/techniques/T1021/002/), [T1053.005](https://attack.mitre.org/techniques/T1053/005/)) — and a `--full` mode that spawns a SYSTEM-context child via a scheduled task named `gentlemen_system` ([Microsoft Threat Intelligence, 2026-05-28](https://www.microsoft.com/en-us/security/blog/2026/05/28/the-gentlemen-ransomware-dissecting-a-self-propagating-go-encryptor/)). Defence evasion includes disabling Defender real-time monitoring ([T1562.001](https://attack.mitre.org/techniques/T1562/001/)), re-enabling SMBv1 and registry changes for anonymous share access; persistence runs via `UpdateSystem`/`UpdateUser` scheduled tasks and Run keys. On 10 June, KrebsOnSecurity published a deanonymisation tracing the operator handle "Hastalamuerte"/"Zeta88" to a named Russian national in Izhevsk, corroborated by Intel 471, Constella and Flashpoint ([KrebsOnSecurity, 2026-06-10](https://krebsonsecurity.com/2026/06/who-runs-the-ransomware-group-the-gentlemen/)). Check Point Research documents the affiliate-favourable 90/10 revenue split and reports affiliates obtaining initial access via Fortinet SSL-VPN credentials ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)). Note: Krebs cites 332 published victims since mid-2025 versus the leak site's 478 claim

**Why it matters to us:** the initial-access pattern is concrete and huntable — review Fortinet SSL-VPN authentication logs for brute-force sequences followed by a first-time successful logon from a new ASN; alert on scheduled-task creation named `gentlemen_system`/`UpdateSystem`/`UpdateUser` (Windows Event ID 4698) and on shadow-copy deletion; treat SMBv1 re-enablement on any host as a high-confidence compromise signal.
