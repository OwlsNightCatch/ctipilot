---
schema: 1
kind: threat
horizon: operational
title: "Iran MOIS attributed to LACMTA destructive breach via \"Ababil of Minab\" hacktivist front — 700 GB exfiltrated, backups and VMs deliberately destroyed"
headline: "Iran MOIS attributed to LACMTA destructive breach via \"Ababil of Minab\" hacktivist front — 700 GB exfiltrated, backups and VMs deliberately destroyed"
summary: "Gambit Security (Israeli threat-intelligence firm) published a technical report on 2026-05-26 attributing the March 2026 breach of Los Angeles County Metropolitan Transportation Authority (LACMTA / LA Metro) to an Iran-MOIS-linked cluster operating under the hacktivist persona Ababil of Minab (Gambit Security …"
discovered_at: "2026-05-28T05:00:05Z"
event_date: 2026-05-27
run_id: 2026-05-28-3e33200a
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - wiper
  - iran-nexus
regions:
  - us
  - middle-east
sectors:
  - transport
  - public-sector
entities:
  - "actor:ababil-of-minab-mois-attribution-lacmta-march-2026-700gb-backups-destroyed"
cves: []
sources:
  - url: "https://gambit.security/blog-posts/babil-of-minab-iran-mois-destruction-campaign"
    publisher: Gambit Security
    role: primary
  - url: "https://techcrunch.com/2026/05/26/iranian-hackers-blamed-for-breach-of-los-angeles-transit-system-that-took-weeks-to-recover/"
    publisher: TechCrunch
    role: corroborating
  - url: "https://therecord.media/iranian-intelligence-behind-hack-of-la-transit-system"
    publisher: The Record
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
migrated_from: briefs/2026-05-28.md
---

Gambit Security (Israeli threat-intelligence firm) published a technical report on 2026-05-26 attributing the March 2026 breach of Los Angeles County Metropolitan Transportation Authority (LACMTA / LA Metro) to an Iran-MOIS-linked cluster operating under the hacktivist persona *Ababil of Minab* ([Gambit Security, 2026-05-26](https://gambit.security/blog-posts/babil-of-minab-iran-mois-destruction-campaign); [TechCrunch, 2026-05-26](https://techcrunch.com/2026/05/26/iranian-hackers-blamed-for-breach-of-los-angeles-transit-system-that-took-weeks-to-recover/); [The Record, 2026-05-27](https://therecord.media/iranian-intelligence-behind-hack-of-la-transit-system)). The persona surfaced in late March / early April 2026 claiming to be a standalone hacktivist crew; Gambit's forensic evidence ties the cluster's infrastructure and techniques to the MOIS-attributed *Black Shadow* group, a designation the Israel National Cyber Directorate (INCD) has previously applied. The campaign exfiltrated a large volume of emails, backups and other files from LACMTA, then deliberately targeted the recovery layer: virtual machines and storage volumes were deleted, backup infrastructure was destroyed, and multiple destructive techniques were applied in parallel to force concurrent remediation pathways and maximise downtime. LA Metro required weeks to recover. The campaign also touched named and unnamed organisations in Israel, Saudi Arabia and Turkey.

**Defender takeaway:** the destruction-of-recovery TTP is the signal here, not the persona. Operators are now explicitly designing kill chains in which the backup and hypervisor planes are first-class targets — `T1485` Data Destruction extended to VM-lifecycle and backup-job APIs rather than file-level deletion. Swiss public-transport operators (SBB, PostBus, cantonal networks) and EU equivalents running large hypervisor estates with shared admin trust into backup orchestration should treat the recovery plane as part of the protected estate, not an out-of-band restore mechanism: separate identity boundary, MFA on backup-job execution, and a tested air-gapped restore path that does not depend on the same identity provider as the production estate. Hunt: hypervisor-level mass VM lifecycle events (power-off-all, delete-all) outside change-window; backup-job cancellation or backup-system event-log purge by unexpected service accounts.
