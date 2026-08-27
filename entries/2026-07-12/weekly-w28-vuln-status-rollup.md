---
schema: 1
kind: vulnerability
horizon: strategic
weekly_section: weekly-vuln-rollup
title: 'Vulnerability status roll-up — 2026-W28: what moved into exploitation, what reached KEV, and what to patch out-of-band'
headline: '2026-W28 vuln roll-up — exploited: ColdFusion, CitrixBleed 2, Gitea, Langflow, Joomla wave; notable: HTTP.sys mechanics, KVM escape, Siemens SICAM 8, MOVEit'
summary: 'Consolidated status view of the week''s vulnerabilities that demand action beyond the routine patch cycle. Confirmed exploited / KEV this week: Adobe ColdFusion CVE-2026-48282, Citrix NetScaler CitrixBleed 2 CVE-2025-5777, Gitea CVE-2026-20896, Langflow CVE-2026-55255, and the Joomla extension file-upload wave (CVE-2026-48908/56290/56291/48939). Public-exploit or full-mechanics disclosures raising urgency without confirmed ITW use: GhostLock Linux kernel LPE CVE-2026-43499 (public reliable exploit), Windows HTTP.sys CVE-2026-47291 (ZDI published exploitation mechanics), Linux KVM ''Januscape'' CVE-2026-53359 (guest-to-host escape), BeyondTrust RS/PRA CVE-2026-40138 cluster. OT/CI note: Siemens SICAM 8 grid RTU firmware-signing bypass (CVE-2026-54798-801). See the linked operational entries for per-CVE detail.'
discovered_at: '2026-07-12T23:26:00Z'
event_date: 2026-07-11
run_id: 2026-07-12T2309Z-weekly
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - actively-exploited
  - cisa-kev
  - rce
  - priv-esc
  - ot-ics
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
  - energy
techniques:
  - T1190
  - T1068
  - T1505.003
  - T1611
  - T1499
affected_products:
  - Adobe ColdFusion
  - Citrix NetScaler ADC
  - Citrix NetScaler Gateway
  - Gitea
  - Progress MOVEit Transfer
  - Siemens SICAM 8
cves: []
sources:
  - url: https://www.bleepingcomputer.com/news/security/max-severity-adobe-coldfusion-flaw-now-exploited-in-attacks/
    publisher: BleepingComputer
    role: primary
  - url: https://security-hub.ncsc.admin.ch/#/posts/12755
    publisher: NCSC-CH Cyber Security Hub
    role: primary
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: A roll-up that carries no CVEs in its own frontmatter by design — every CVE named here is fully sourced in its linked operational entry (see references); this entry states the current status trajectory, not new per-CVE claims. Reliability B, credibility 1 (the aggregated statuses are each corroborated in-store).
confidence: high
classification:
  reliability: B
  credibility: 1
update_of: null
references:
  - 2026-07-02/cve-2026-48276-48277-48281-48282-48283-48316-adobe-coldfusio
  - 2026-07-10/citrixbleed-2-dragonforce-iab-kill-chain-stac3725
  - 2026-06-23/cve-2026-20896-gitea-docker-trust-all-reverse-proxy-default
  - 2026-07-08/cve-2026-55255-langflow-idor-kev-chained-with-rce
  - 2026-07-08/ghostlock-cve-2026-43499-linux-kernel-rtmutex-uaf-lpe
  - 2026-06-10/cve-2026-47291-microsoft-june-patch-tuesday-http-sys-pre-aut
  - 2026-07-09/cve-2026-53359-januscape-kvm-x86-guest-to-host-vm-escape
  - 2026-07-08/beyondtrust-rs-pra-preauth-bypass-cve-2026-40138-cluster
  - 2026-07-10/siemens-sicam-8-ssa-229470-firmware-signing-bypass
  - 2026-07-11/moveit-transfer-certfr-cve-2026-10699-10698-11903
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
---

This roll-up consolidates the 2026-W28 vulnerabilities that cross the out-of-band-action bar — actively exploited, at imminent mass exploitation, or otherwise demanding a response the routine monthly cycle does not give. Per-CVE facts, CVSS, and affected/fixed versions live in the linked operational entries; this entry is the status trajectory a reader uses to sequence the week's patching.

**Confirmed exploited / on CISA KEV this week.** *Adobe ColdFusion* CVE-2026-48282 (one of the 1 July CVSS 10.0 unauthenticated RCEs) — exploited within two hours of public detail, KEV-listed 7 July ([BleepingComputer, 2026-07-08](https://www.bleepingcomputer.com/news/security/max-severity-adobe-coldfusion-flaw-now-exploited-in-attacks/)). *Citrix NetScaler* CitrixBleed 2 CVE-2025-5777 — weaponised into a repeatable initial-access-broker kill chain ending in DragonForce ransomware; patch plus session termination required. *Gitea* CVE-2026-20896 — NCSC-CH escalated to "Actively Exploited, Proof of Concept Available" ([NCSC-CH, 2026-07-10](https://security-hub.ncsc.admin.ch/#/posts/12755)). *Langflow* CVE-2026-55255 — cross-tenant IDOR chained with pre-auth RCE, first exploited 25 June, now KEV. *Joomla extension file-upload wave* — CVE-2026-48908 / 56290 / 56291 / 48939 exploited as zero-days (see the dedicated top-story), CVE-2026-57827/57828 patched without confirmed exploitation yet.

**Urgency raised by public exploit or full mechanics, no confirmed ITW use.** *GhostLock* CVE-2026-43499 — Linux kernel rtmutex use-after-free with a public ~97%-reliable local-privilege-escalation exploit. *Windows HTTP.sys* CVE-2026-47291 (pre-auth RCE, CVSS 9.8) — ZDI published full exploitation mechanics for the June Patch Tuesday flaw, collapsing the reverse-engineering barrier. *Linux KVM/x86 'Januscape'* CVE-2026-53359 — shadow-MMU use-after-free enabling guest-to-host VM escape, relevant to multi-tenant virtualisation. *BeyondTrust Remote Support / Privileged Remote Access* — the CVE-2026-40138 pre-auth bypass cluster on a remote-access product class that is itself a high-value target.

**OT / critical-infrastructure note.** *Siemens SICAM 8* grid RTUs (A8000/EGS/S8000) — a firmware-signature-validation bypass (CVE-2026-54798-801) on devices deployed in European energy grids; slow patch cycles make network isolation and OT-segment monitoring the near-term control. *Progress MOVEit Transfer* — pre-auth SFTP DoS (CVE-2026-10699) plus admin scope-bypass fixes, notable given MOVEit's history as a mass-exfiltration target.

**Defender takeaway:** sequence by exploitation evidence, then exposure — the KEV/exploited set above is this week's out-of-band queue; the public-exploit set is next in line before it is weaponised; the OT items are isolate-and-monitor where an immediate patch is impractical.
