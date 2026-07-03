---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "The Gentlemen RaaS — Europe-skewed operation surged approximately 448% QoQ; 32% of Q1 2026 victims in Europe; FortiGate CVE-2024-55591 initial-access funnel"
headline: "The Gentlemen RaaS — Europe-skewed operation surged approximately 448% QoQ; 32% of Q1 2026 victims in Europe; FortiGate CVE-2024-55591 initial-access funnel"
summary: W1 horizon research identified an in-window operator gap the daily briefs missed.
discovered_at: "2026-05-04T05:00:40Z"
event_date: 2026-04-20
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - actively-exploited
  - data-breach
regions:
  - europe
  - dach
sectors:
  - energy
  - manufacturing
  - healthcare
  - public-sector
entities:
  - "actor:gentlemen-raas-gentlekiller"
  - "actor:thegentlemen"
  - "campaign:tds-security-tool-impersonation-checkpoint"
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/dfir-report-the-gentlemen/"
    publisher: Check Point Research — The Gentlemen DFIR Report
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/the-gentlemen-ransomware-now-uses-systembc-for-bot-powered-attacks/"
    publisher: BleepingComputer — The Gentlemen + SystemBC
    role: corroborating
  - url: "https://www.zerofox.com/intelligence/q1-2026-ransomware-wrap-up/"
    publisher: ZeroFox Q1 2026 Ransomware Wrap-Up
    role: corroborating
  - url: "https://www.comparitech.com/news/healthcare-ransomware-roundup-q1-2026-stats-on-attacks-ransoms-and-data-breaches/"
    publisher: Comparitech Q1 2026 Healthcare
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: CVE fields incomplete in v2 footer (CVE-2024-55591)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W19.md
---

W1 horizon research identified an in-window operator gap the daily briefs missed. "The Gentlemen" emerged in August 2025 and per ZeroFox surged to the second- or third-most-active ransomware operation globally in Q1 2026 — 192 attacks that quarter, a approximately 448% QoQ increase, **32% of Q1 2026 victims in Europe** (up from 2% in Q4 2025) ([ZeroFox Q1 2026 Wrap-Up, 2026-04-17](https://www.zerofox.com/intelligence/q1-2026-ransomware-wrap-up/)). Check Point Research's DFIR report on the operator confirms the post-compromise tradecraft observed during a single incident-response engagement: Cobalt Strike delivered via RPC from a Domain Controller; Mimikatz for credential harvesting; **GPO abuse** to inject a scheduled task into Group Policy that propagates the encryptor to all domain-joined systems near-simultaneously (compressing time-to-encryption to minimise IR response window); **SystemBC** SOCKS5 C2 tunnelling and covert payload staging; encryption using X25519 Diffie–Hellman key exchange per file combined with XChaCha20 stream cipher, per-file ephemeral key pair with a random 32-byte private key ([Check Point Research DFIR Report, 2026-04-20](https://research.checkpoint.com/2026/dfir-report-the-gentlemen/) · [BleepingComputer — The Gentlemen + SystemBC, 2026-04-20](https://www.bleepingcomputer.com/news/security/the-gentlemen-ransomware-now-uses-systembc-for-bot-powered-attacks/)). CPR explicitly states the precise initial-access vector could not be conclusively determined for the engagement it analysed; broader reporting attributes initial access to a FortiOS / FortiProxy attack surface that includes **CVE-2024-55591** (authentication bypass, CVSS 9.8 — patched January 2025), with secondary reporting describing an operator database of pre-exploited devices and brute-forced VPN credentials primed for deployment — defenders should treat patch-state-alone as insufficient if the device was unpatched against CVE-2024-55591 at any point during the exposure window.

European victims surfaced in BleepingComputer's SystemBC coverage and in quarterly leak-site aggregation include **Oltenia Energy Complex** (Romania — described as a significant portion of national electricity supply, December 2025) and **The Adaptavist Group**; Comparitech's Q1 2026 healthcare roundup attributes 10 healthcare-sector claims to the operator in the quarter; the operator's leak-site footprint and the absence of an "off-limits" sector convention make hospitals, water utilities, and similar critical-infrastructure targets in-scope. The cross-finding with this week's other concerns: GPO-injected scheduled-task propagation defeats backup-isolation defences if the AD environment is in the encryption path; if the operator's initial-access funnel includes unpatched FortiGate devices, that surface intersects directly with the Polish water-OT NIS2 coverage-gap framing (§ 4, § 6) since small municipal CI operators are over-represented in the unpatched-FortiGate population. Defender priorities for 2026-W20: hunt scheduled tasks in SYSVOL pointing to UNC paths or temp directories; profile SystemBC SOCKS5 beacons; add XChaCha20 file-header pattern detection at backup / DLP tier; re-verify FortiGate patch state against CVE-2024-55591 and any later FortiOS / FortiProxy auth-bypass advisories.
