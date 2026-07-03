---
schema: 1
kind: research
horizon: operational
title: "FortiGuard documents C0XMO, a cross-platform Gafgyt variant propagating through a five-year-old DD-WRT UPnP flaw"
headline: "FortiGuard documents C0XMO, a cross-platform Gafgyt variant propagating through a five-year-old DD-WRT UPnP flaw"
summary: "FortiGuard Labs analysed C0XMO, a new Gafgyt-derived DDoS botnet that propagates by exploiting an old stack buffer overflow in the UPnP/SSDP parser of DD-WRT router firmware — sending an oversized ST value in a crafted M-SEARCH packet to UDP 1900 to drop its payload (FortiGuard Labs, 2026-06-03 …"
discovered_at: "2026-06-08T05:00:04Z"
event_date: 2026-06-07
run_id: 2026-06-08-1a0ce644
priority: notable
immediate_action: null
tags:
  - botnet
  - ddos
regions:
  - global
  - europe
sectors:
  - telco
entities:
  - "campaign:c0xmo-gafgyt"
cves: []
sources:
  - url: "https://www.fortinet.com/blog/threat-research/inside-cross-platform-propagation-of-new-gafgyt-variant-c0xmo"
    publisher: FortiGuard Labs
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/c0xmo-botnet-spreads-via-dd-wrt-router-flaw-kills-rival-malware/"
    publisher: BleepingComputer
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
actions:
  - "**Reduce edge UPnP exposure and hunt SOHO/branch gateways** (. Restrict inbound SSDP / outbound UDP 1900 and disable UPnP where unused; on Linux gateways hunt cron entries spawning processes from hidden dot-directories."
migrated_from: briefs/2026-06-08.md
---

FortiGuard Labs analysed **C0XMO**, a new Gafgyt-derived DDoS botnet that propagates by exploiting an old stack buffer overflow in the UPnP/SSDP parser of DD-WRT router firmware — sending an oversized `ST` value in a crafted M-SEARCH packet to UDP 1900 to drop its payload ([FortiGuard Labs, 2026-06-03](https://www.fortinet.com/blog/threat-research/inside-cross-platform-propagation-of-new-gafgyt-variant-c0xmo); [BleepingComputer, 2026-06-07](https://www.bleepingcomputer.com/news/security/c0xmo-botnet-spreads-via-dd-wrt-router-flaw-kills-rival-malware/)). FortiGuard attributes the DD-WRT flaw to *CVE-2021-27137*, an identifier that does not currently resolve on NVD or MITRE (flagged in § 7). The operationally interesting part is the engineering: C0XMO ships builds for seven architectures (ARM, MIPS, m68k, PowerPC, SuperH, x86, AMD64), splits its scanning/exploitation logic into a standalone Python propagator so it can be updated independently of the core bot, terminates rival malware on the host, and supports 19 DDoS methods including Cloudflare-bypass HTTP floods and game-server-specific floods. Persistence is via cron (15-minute interval) and shell-profile modification; payloads stage to hidden `.sys` files under `/tmp`, `/var/tmp` and `/dev/shm`.

**Why it matters to us:** the direct exposure is low for hardened public-sector cores, but self-managed SOHO/branch gateways and any DD-WRT devices below changeset 45723 are recruitable — and a compromised edge device becomes both a DDoS source and a foothold. Defender concepts: block or restrict outbound UDP 1900 / inbound SSDP at the perimeter and disable UPnP where it is not required; on Linux gateways, hunt for cron entries spawning processes from hidden dot-directories and for shell-profile modifications (Sysmon-for-Linux / `auditd` execve on `/tmp/.sys`-class paths). No IOCs are reproduced here.
