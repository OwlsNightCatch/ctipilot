---
schema: 1
kind: incident
title: "Foxconn confirms Nitrogen ransomware crippled North-American manufacturing sites; 8 TB / 11M files claimed"
headline: "Foxconn confirms Nitrogen ransomware crippled North-American manufacturing sites; 8 TB / 11M files claimed"
summary: "Foxconn confirms Nitrogen ransomware crippled North-American factories. Foxconn's statement on 2026-05-12 acknowledges the network collapse that began at the Mount Pleasant, Wisconsin plant on May 1 and the operational disruption since; Nitrogen claims 8 TB / 11M files exfiltrated, alleged to include design documentation for Apple, Nvidia, Intel, Google and Dell projects. Coveware previously published a programming bug in Nitrogen's ESXi encryptor that makes decryption mathematically impossible even after payment — relevant to anyone evaluating the recovery path (The Register, 2026-05-12; The Record, 2026-05-12)."
discovered_at: "2026-05-13T05:00:00Z"
event_date: 2026-05-12
run_id: 2026-05-13-c148b9a5
priority: high
immediate_action: null
tags:
  - ransomware
  - data-breach
  - supply-chain
regions:
  - us
sectors:
  - manufacturing
entities:
  - "incident:foxconn-nitrogen-2026"
cves: []
sources:
  - url: "https://www.theregister.com/cyber-crime/2026/05/12/foxconn-confirms-cyberattack-after-nitrogen-claims-apple-nvidia-data-theft/5239144"
    publisher: "The Register, 2026-05-12"
    role: primary
  - url: "https://therecord.media/foxconn-confirms-cyberattack-north-american-factories"
    publisher: "The Record, 2026-05-12"
    role: corroborating
  - url: "https://9to5mac.com/2026/05/12/apple-supplier-foxconn-confirms-ransomware-attack-affected-north-american-factories/"
    publisher: "9to5Mac, 2026-05-12"
    role: corroborating
  - url: "https://www.coveware.com/blog/2026/2/2/nitrogen-ransomware-esxi-malware-has-a-bug"
    publisher: "Coveware, 2026-02-02"
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
migrated_from: briefs/2026-05-13.md
---

Foxconn Technology Group confirmed on 2026-05-12 that several North-American factories — including Mount Pleasant (Wisconsin), Houston (Texas), and additional sites in Ohio, Virginia, Indiana and Mexico — suffered a cyberattack starting at approximately 07:00 ET on 2026-05-01, when the Mount Pleasant Wi-Fi failed and core infrastructure was disrupted by 11:00 ET; production halted for roughly a week before "affected factories are currently resuming normal production" ([The Register, 2026-05-12](https://www.theregister.com/cyber-crime/2026/05/12/foxconn-confirms-cyberattack-after-nitrogen-claims-apple-nvidia-data-theft/5239144); [The Record, 2026-05-12](https://therecord.media/foxconn-confirms-cyberattack-north-american-factories)). The Nitrogen ransomware crew — a Conti 2 leaked-builder derivative active since 2023 — listed Foxconn on its leak site on 2026-05-11 and claims 8 TB / 11 million files, alleging "confidential technical drawings and project documentation" for Apple, Nvidia, Intel, Google and Dell engagements ([9to5Mac, 2026-05-12](https://9to5mac.com/2026/05/12/apple-supplier-foxconn-confirms-ransomware-attack-affected-north-american-factories/)). None of the named third-party vendors has confirmed any compromise of their own systems; the 8 TB number is the attacker's claim, not a Foxconn-confirmed exfiltration volume.

**Why it matters to us:** Foxconn is the dominant EMS supplier for endpoints widely procured by Swiss / EU government and critical-infrastructure operators (Apple, Dell, Nvidia, Intel hardware). The operationally critical defender-side data point on Nitrogen is independent of the headline: a [Coveware analysis (2026-02-02)](https://www.coveware.com/blog/2026/2/2/nitrogen-ransomware-esxi-malware-has-a-bug) documents a programming error in Nitrogen's ESXi encryptor — a QWORD variable overwrites four bytes of the Curve25519 public key during ChaCha8 key-exchange, producing a corrupted key that is mathematically irrecoverable even with the operator's private key. If Nitrogen encrypts an ESXi host in your estate, paying does not restore your VMs. Backup integrity at the hypervisor layer (not just guest-level) is the only recovery path. Generic hypervisor-recovery detection concepts apply: alert on `vmkfstools` / `esxcli` invocations from non-administrator sessions on ESXi `/var/log/shell.log`, and on unexpected `vmx` process terminations preceding mass-rename events. The cited sources do not document the specific initial-access TTP chain Nitrogen has used at Foxconn — defenders should rely on standard hunting for the broader Conti-derivative cluster (Cobalt Strike beaconing, Rclone exfiltration) and let attribution-specific IOCs follow the in-flight forensics.
