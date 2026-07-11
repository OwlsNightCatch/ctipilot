---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "\"The Gentlemen\" RaaS — operations continue post-leak, decryptor published, FortiOS / Erlang SSH initial access CVEs confirmed"
headline: "\"The Gentlemen\" RaaS — operations continue post-leak, decryptor published, FortiOS / Erlang SSH initial access CVEs confirmed"
summary: "Following the 2026-05-04 Rocket backend DB leak (attributed to a breach of hosting provider 4VPS), administrator zeta88 / hastalamuerte announced a full communications-infrastructure overhaul — new NAS deployment and new locker upgrades — signalling no intent to cease operations."
discovered_at: "2026-05-11T05:00:38Z"
event_date: 2026-05-14
run_id: 2026-W20-71c96b25
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
regions:
  - global
sectors:
  - public-sector
entities:
  - "actor:thegentlemen"
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/"
    publisher: Check Point Research
    role: primary
  - url: "https://blog.checkpoint.com/research/when-the-ransomware-gang-gets-hacked-what-the-gentlemen-leak-reveals-about-modern-ransomware-risk"
    publisher: Check Point blog
    role: corroborating
  - url: "https://github.com/Bedrock-Safeguard/gentlemen-decryptor"
    publisher: Bedrock Safeguard decryptor
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
migrated_from: briefs/weekly/2026-W20.md
---

Following the 2026-05-04 Rocket backend DB leak (attributed to a breach of hosting provider 4VPS), administrator `zeta88` / `hastalamuerte` announced **a full communications-infrastructure overhaul — new NAS deployment and new locker upgrades — signalling no intent to cease operations**. The operation maintained ~332 victims in H1 2026, ranking second in global RaaS activity per Check Point Research. Check Point documented **initial access via CVE-2024-55591** (FortiOS management interface auth bypass, ITW since November 2024) **and CVE-2025-32433** (Erlang SSH in Cisco context); post-access chain includes RelayKing-based NTLM relay (CVE-2025-33073), AD enumeration, EDR disablement, and GPO-deployed locker ([Check Point Research](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/); [Check Point blog](https://blog.checkpoint.com/research/when-the-ransomware-gang-gets-hacked-what-the-gentlemen-leak-reveals-about-modern-ransomware-risk); [daily 2026-05-14 UPDATE](/briefs/2026-05-14/)).

Bedrock Safeguard (Canadian security firm) published a **working decryptor on 2026-05-14** exploiting Go's failure to zero XChaCha20 / X25519 ephemeral private-key material from goroutine stacks post-use; 35/35 files decrypted in testing. The operator claims to have patched the binary, so the decryptor capability is best-case retrospective; affiliates show no evidence of forking, and the core nine-person structure remains intact per leaked chats ([Bedrock Safeguard decryptor](https://github.com/Bedrock-Safeguard/gentlemen-decryptor)). Defender takeaway: for any Gentlemen-impacted Go-binary host, attempt process-memory dump capture for ephemeral key recovery before reimaging; verify FortiOS patch state on CVE-2024-55591 across every Swiss / EU public-sector Fortinet deployment (the FortiOS bug is the documented initial-access primary, and the W19 long-running record already lists this CVE).
