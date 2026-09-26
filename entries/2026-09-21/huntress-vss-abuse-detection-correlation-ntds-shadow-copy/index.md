---
schema: 1
kind: research
title: "Huntress: distinguishing malicious Volume Shadow Copy abuse — NTDS.dit theft via shadow copy, anti-recovery deletion — from routine RMM/backup housekeeping requires event correlation, not single-event alerting"
headline: "Huntress lays out why no single VSS event, on its own, ever justifies an alert"
summary: >
  Huntress documents three classes of Volume Shadow Copy Service abuse it detects — pre-ransomware
  shadow-copy deletion, quiet NTDS.dit theft via a purpose-created shadow copy, and shadow-copy
  size/configuration manipulation — and the event-correlation logic needed to separate each from
  routine RMM and backup-agent VSS housekeeping, which performs the identical raw API calls
  constantly. A worked incident shows PsExec, `vssadmin create shadow` and an attempted cover-up
  correlating into a single escalation no individual step would justify alone.
discovered_at: "2026-09-21T04:44:00Z"
updated_at: null
event_date: "2026-09-14"
run_id: 2026-09-21T0410Z-intel
priority: notable
immediate_action: null
tags:
  - ransomware
  - identity
regions:
  - global
sectors: []
entities: []
techniques:
  - T1490
  - T1003.003
  - T1569.002
  - T1021.002
  - T1033
affected_products: []
cves: []
sources:
  - url: "https://www.huntress.com/blog/vss-abuse-explained"
    publisher: "Huntress Labs"
    date: "2026-09-14"
    role: primary
closed_sources: []
evidence:
  - quote: "Rather than running credential-dumping tools directly against a live, monitored system, an attacker can spin up a shadow copy and quietly pull the NTDS.dit file (the Active Directory database) out of it."
    publisher: "Huntress Labs"
    source_url: "https://www.huntress.com/blog/vss-abuse-explained"
  - quote: "PsExec was used to spawn SYSTEM-level command shell processes on a domain controller. From there, the attacker enumerated active Remote Desktop sessions, then ran vssadmin create shadow, a technique commonly used to pull credentials out of the NTDS.dit database without touching it directly. A few minutes later, the attacker tried to cover their tracks by deleting the shadow copies they'd just created; that attempt was blocked and flagged by endpoint antivirus."
    publisher: "Huntress Labs"
    source_url: "https://www.huntress.com/blog/vss-abuse-explained"
verification: single-source
sourcing_note: "Huntress Labs is the sole publisher of this detection-engineering write-up; no independent lab corroboration was sought or is expected for a vendor's own methodology piece."
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Huntress lays out three distinct classes of Volume Shadow Copy Service (VSS) abuse it detects, and the correlation logic each requires to separate it from benign RMM- and backup-agent housekeeping that performs the identical raw create/delete API calls constantly ([Huntress Labs, 2026-09-14](https://www.huntress.com/blog/vss-abuse-explained)). The first and most familiar class, MITRE ATT&CK's Inhibit System Recovery, is pre-ransomware shadow-copy deletion — most commonly via `vssadmin.exe` but achievable through several other services and binaries, so a detection that anchors only on the `vssadmin.exe` process image misses variants. The second, less commonly discussed class is credential access by proxy: rather than running credential-dumping tools live against a monitored host, an attacker creates a shadow copy specifically in order to pull the `NTDS.dit` Active Directory database out of the static snapshot, a materially quieter path than direct extraction. The third class is shadow-copy size or configuration manipulation as ancillary tradecraft.

Huntress's own detection logic fires on the raw VSS event plus its surrounding context rather than the event in isolation: for deletions, it inspects how the deletion occurred, accounting for the non-`vssadmin` paths; for creations, it looks for pairing with lateral-movement indicators and credential-harvesting commands appearing before or after the VSS event within a correlation window, rather than judging the creation alone. A worked incident illustrates the method: PsExec spawned a SYSTEM-level shell on a domain controller, the operator enumerated active RDP sessions, ran `vssadmin create shadow` — the NTDS.dit-theft pattern — then, a few minutes later, attempted to delete the shadow copies to cover their tracks, an attempt endpoint antivirus blocked and flagged, while DNS enumeration against at least one additional host appeared in the same window. Huntress states no single step in that sequence would have justified escalating alone; the lateral-movement-then-VSS-creation-then-credential-harvesting-attempt correlation is what does.

**Defender takeaway:** build (or verify an existing) correlation rule that pairs any `vssadmin create shadow` (or equivalent) event on a domain controller or credential-bearing host with lateral-movement indicators — PsExec-style SYSTEM shell spawns, RDP session enumeration, or authentication sweeps — occurring in the same narrow time window, rather than alerting on the VSS event alone; a shadow-copy deletion attempt following a shadow-copy creation on the same host within a narrow window — minutes, not hours — is close to definitionally malicious and warrants a high-severity rule of its own regardless of which tool performed the deletion.

**Triage:** a shadow copy being created or deleted is one of the most common legitimate Windows operations — routine RMM tooling and backup agents do it constantly — so the raw event carries almost no signal by itself. The discriminator is context: lateral-movement activity and credential-harvesting-adjacent commands appearing in the same time window as the VSS event is what separates an attacker's shadow-copy abuse from a backup agent's routine housekeeping.
