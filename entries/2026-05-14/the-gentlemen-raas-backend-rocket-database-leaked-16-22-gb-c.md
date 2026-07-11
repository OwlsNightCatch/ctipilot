---
schema: 1
kind: threat
horizon: operational
title: "The Gentlemen RaaS — backend \"Rocket\" database leaked (16.22 GB), Check Point analysis exposes operator handles, ZeroPulse C2 internals, 1,570+ victims, decryptor published on GitHub"
headline: "The Gentlemen RaaS — backend \"Rocket\" database leaked (16.22 GB), Check Point analysis exposes operator handles, ZeroPulse C2 internals, 1,570+ victims"
summary: "The Gentlemen RaaS backend dumped — Check Point exposes operator handles and tooling; SystemBC C&C reveals 1,570+ victims vs. 332 on the public leak site; decryptor on GitHub. Check Point Research's 2026-05-13 analysis of a 44.4 MB extract from the group's leaked \"Rocket\" backend (16.22 GB total, posted to the cybercrime forum Breached on 4 May after the group's infrastructure was compromised) maps nine operator handles, the EDR-suppression toolchain (EDRStartupHinder, gfreeze, glinker), the ZeroPulse C2 framework, and a separately-exposed SystemBC C&C server holding 1,570+ victim entries against 332 publicly listed in the first five months of 2026 — large under-reporting of true scope. The decryptor is public on GitHub per BankInfoSecurity, making decryption the first action for any in-flight Gentlemen incident (Check Point Research, 2026-05-13; BankInfoSecurity, 2026-05-11)."
discovered_at: "2026-05-14T05:00:04Z"
event_date: 2026-05-13
run_id: 2026-05-14-e05c6e6e
priority: high
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - identity
regions:
  - europe
  - global
sectors:
  - technology
entities:
  - "report:q1-2026-ransomware-quarterly"
  - "actor:gentlemen-raas-gentlekiller"
  - "actor:thegentlemen"
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/"
    publisher: "Check Point Research, 2026-05-13"
    role: primary
  - url: "https://www.bankinfosecurity.com/tables-turned-gentlemen-ransomware-group-suffers-data-leak-a-31654"
    publisher: "BankInfoSecurity, 2026-05-11"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: update target unresolved (originally covered 2026-05-10)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-14.md
---

**UPDATE (originally covered 2026-05-10 in the Q1 2026 ransomware quarterly synthesis):** Check Point Research published "Thus Spoke…The Gentlemen" on 2026-05-13, a detailed analysis of a 44.4 MB extract from the group's leaked "Rocket" backend database (16.22 GB total) that was posted to the cybercrime forum Breached on 2026-05-04 after the group's infrastructure was compromised by an unidentified actor ([Check Point Research, 2026-05-13](https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/); [BankInfoSecurity, 2026-05-11](https://www.bankinfosecurity.com/tables-turned-gentlemen-ransomware-group-suffers-data-leak-a-31654)). The dataset contains 8,200 lines of internal chat-tool traffic across channels INFO / general / TOOLS / PODBOR, shadow files with password hashes, affiliate negotiation transcripts, and configuration artefacts for the ZeroPulse C2 framework.

Nine operator handles are identified — including administrator `zeta88` (also `hastalamuerte`), who both manages the RaaS panel and participates directly in encryption events. Reconstructed attack chain: initial access almost exclusively via unpatched edge devices — FortiGate CVE-2024-55591 (the group's documented mainstay), Cisco appliances, CWMP/TR-069 interfaces — or purchased infostealer credentials; post-access tooling includes NetExec, RelayKing (NTLM relay), CertiHound (AD Certificate Services abuse), TaskHound, PrivHound; EDR-suppression utilities `EDRStartupHinder`, `gfreeze` and `glinker` manipulate ETW callbacks and NTDLL syscall tables; persistence is maintained via Cloudflare Zero Trust tunnels and self-provisioned WireGuard/OpenVPN chains.

Two operationally critical facts: (1) Check Point Research attributes a count of **1,570+ victim entries** to a separately-exposed SystemBC C&C server, against **332 victims publicly listed on the group's data-leak site in the first five months of 2026** — significant under-reporting of true scope (Check Point's wider comparison cites 412 cumulative DLS listings); (2) the decryptor has been released as [GitHub `Bedrock-Safeguard/gentlemen-decryptor`](https://github.com/Bedrock-Safeguard/gentlemen-decryptor), enabling existing victims to recover without payment (decryptor disclosed in BankInfoSecurity's 2026-05-11 reporting). For Swiss / EU SOCs handling an active Gentlemen incident the workflow changes today: attempt decryption before any negotiation. Detection pivots from the leak: alert on `EDRStartupHinder`, `gfreeze`, `glinker` process names (custom binaries, not commodity); monitor for AD Certificate Services reconnaissance (`certutil` enumeration of CA servers and templates) consistent with CertiHound; correlate with FortiGate CVE-2024-55591 initial-access exploitation patterns that the group continues to weaponise.
