---
schema: 1
kind: threat
horizon: operational
title: "GodDamn ransomware (Beast/Monster rebrand) blinds EDR with 'PoisonX', a malicious kernel driver Microsoft signed"
headline: "Symantec: a driver built malicious from the outset — yet WHCP-signed — defeats code-signing allowlisting to kill EDR before GodDamn encrypts"
summary: >
  Symantec attributes GodDamn ransomware (first seen 2026-05-21) to the Hyadina developer behind
  the Monster→Beast lineage, and documents a June 2026 intrusion where the operators loaded
  PoisonX (g11.sys) — a kernel driver they got signed under Microsoft's Windows Hardware
  Compatibility Publisher program despite it being malicious by design — to terminate security
  processes and strip user-mode API hooks before encrypting. The signed-malicious-driver twist
  means code-signing allowlisting will not stop it; detection must be behavioural.
discovered_at: "2026-07-11T04:30:43Z"
event_date: "2026-07-09"
run_id: 2026-07-11T0409Z-intel
priority: notable
immediate_action: null
tags: [ransomware, organized-crime, identity]
regions: [global]
sectors: [technology, public-sector, healthcare, finance, energy]
entities: [actor:hyadina, tool:poisonx-driver]
techniques: [T1219.002, T1021.002, T1543.003, T1547.006, T1685, T1553.002, T1003.001, T1555.003, T1486]
affected_products: []
cves: []
sources:
  - url: "https://www.security.com/threat-intelligence/goddamn-ransomware-beast-rebrand"
    publisher: "Symantec Threat Hunter Team (Broadcom)"
    date: "2026-07-09"
    role: primary
  - url: "https://thehackernews.com/2026/07/goddamn-ransomware-uses-poisonx-driver.html"
    publisher: "The Hacker News"
    date: "2026-07-09"
    role: corroborating
  - url: "https://www.infosecurity-magazine.com/news/ransomware-removes-cybersecurity/"
    publisher: "Infosecurity Magazine"
    date: "2026-07-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "the PoisonX driver seems to be slightly more unusual, in that it appears to be a malicious driver that its developers succeeded in getting signed by Microsoft, and it is now being used by ransomware attackers."
    publisher: "Symantec Threat Hunter Team (Broadcom)"
  - quote: "Placing AnyDesk under the user Music folder rather than a standard installation directory is consistent with manual delivery by an attacker who had already obtained access to the host by an earlier means."
    publisher: "Symantec Threat Hunter Team (Broadcom)"
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Hunt for a kernel driver-load event immediately followed (same host, short window) by security-product service-stop events or the disappearance of user-mode API hooks — the behavioural signal that survives PoisonX's valid Microsoft signature; do not rely on code-signing allowlisting to catch it."
  - "Alert on remote-access software (AnyDesk) executing from a user profile folder such as Music rather than Program Files, on AnyDesk registered as an auto-start Windows service, and on `ad.security.interactive_access=2` in an AnyDesk config (suppresses the interactive consent prompt)."
  - "Flag `Set-MpPreference -DisableRealtimeMonitoring $true` and PsExec lateral movement (psexesvc.exe → services.exe → wininit.exe lineage) with credential-tool staging under a user profile directory."
migrated_from: null
---

Symantec's Threat Hunter Team assesses that GodDamn — surfaced as a "new" ransomware, first observed 2026-05-21 — is the latest rebrand in a lineage it tracks to a developer called Hyadina: Monster (2022) → Beast → GodDamn, the last sharing significant code overlap with Beast ([Symantec/Broadcom, 2026-07-09](https://www.security.com/threat-intelligence/goddamn-ransomware-beast-rebrand)). The investigated early-June intrusion is a conventional human-operated ransomware kill chain with one standout component. AnyDesk appeared on the first host staged under the user's Music folder — a placement Symantec reads as manual attacker delivery, not a normal install — and began beaconing to relay infrastructure. The operators then dropped a defence-evasion binary masquerading as a Symantec product, which installed the PoisonX kernel driver (`g11.sys`) into the system driver store, staged a 14-tool credential-harvesting kit (13 NirSoft utilities plus Mimikatz) under the profile, moved laterally across 10-plus hosts via PsExec while re-installing AnyDesk on each for unattended access (writing `ad.security.interactive_access=2` to suppress the consent prompt and registering it as auto-start services), disabled Windows Defender real-time monitoring, and finally deployed the encrypter ([Symantec/Broadcom, 2026-07-09](https://www.security.com/threat-intelligence/goddamn-ransomware-beast-rebrand); [The Hacker News, 2026-07-09](https://thehackernews.com/2026/07/goddamn-ransomware-uses-poisonx-driver.html)).

PoisonX is what distinguishes this case from routine bring-your-own-vulnerable-driver tradecraft. Rather than abusing a flaw in a legitimate signed driver, PoisonX is a driver built to be malicious that its developers nonetheless got signed under Microsoft's "Windows Hardware Compatibility Publisher" program; once loaded it terminates security-product processes and strips user-mode API hooks, so it disables EDR visibility rather than merely evading it. It was first documented earlier in 2026 killing the CrowdStrike Falcon service via a crafted IOCTL to an undocumented driver interface ([Symantec/Broadcom, 2026-07-09](https://www.security.com/threat-intelligence/goddamn-ransomware-beast-rebrand)). **Defender takeaway:** because the driver carries a valid Microsoft signature, code-signing allowlists and reputation checks pass it — detection has to be behavioural. **Triage:** legitimate driver installs do not co-occur with mass termination of security services, so the load of a rarely-seen driver immediately followed by security-product process/service stops and the loss of user-mode hooks on the same host is the discriminator; AnyDesk running from a personal media folder (versus IT-managed Program Files) and configured for unattended access is a second, independent pivot.
