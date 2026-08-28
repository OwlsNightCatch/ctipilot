---
schema: 1
kind: threat
horizon: operational
title: "Kudelski Security: North Korean IT-worker infrastructure overlaps a Bismarck-linked gambling-platform operation and the FakeCalls Android banking trojan"
headline: "A Swiss research lab traces a stealer-log leak into DPRK gambling infrastructure and the fake-IT-worker university pipelines behind it"
summary: >
  Kudelski Security, a Swiss research lab, reconstructs connections between North Korean
  state-linked cybercrime and fake-IT-worker operations via a stealer-log leak. An actor it
  designates "Bismarck," linked to DPRK-run gambling platforms, reused infrastructure overlapping
  the FakeCalls Android banking trojan. Separately, a DPRK-affiliated manager's own stolen 2021
  credential vault held access to historical Emotet loader infrastructure. The investigation
  names university-affiliated IT-worker pipelines directly relevant to HR/identity-vetting teams
  screening remote-hire candidates.
discovered_at: "2026-08-28T06:32:00Z"
updated_at: null
event_date: "2026-08-12"
run_id: 2026-08-28T0409Z-intel
priority: notable
immediate_action: null
tags: [nation-state, organized-crime, cryptocrime]
regions: [global]
sectors: [public-sector, finance]
entities: [actor:purpledelta, actor:bismarck-dprk-cybercrime]
techniques: [T1585.001, T1586]
affected_products: []
cves: []
sources:
  - url: "https://kudelskisecurity.com/research/inside-north-koreas-cybercrime-ecosystem-fake-it-workers-gambling-networks-and-malware"
    publisher: "Kudelski Security"
    date: "2026-08-12"
    role: primary
closed_sources: []
evidence:
  - quote: "We recently observed a stealer log leak involving an actor linked to the DPRK, nicknamed \"Bismarck.\" The actor used two IP addresses that overlap with indicators of compromise (IOCs) documented by Check Point Research in its analysis of FakeCalls, an Android banking trojan targeting South Korea."
    publisher: "Kudelski Security"
  - quote: "We assess that DPRK actors may have reused IP addresses from the gambling operation because the domains were purchased by the associates rather than by [Bismarck directly]."
    publisher: "Kudelski Security"
verification: single-source
sourcing_note: >
  Kudelski Security is the sole source and original investigator; its article names specific IP
  addresses and hostnames as infrastructure evidence for the overlap claim, deliberately not
  reproduced here or in evidence quotes (no IOCs per house policy) — the quotes above are lightly
  redacted to remove literal indicators while preserving the analytic claim. The FakeCalls malware
  family itself was previously documented by Check Point Research (2023); that is background, not
  independent corroboration of this specific infrastructure-overlap claim, which rests on Kudelski
  alone.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [body]
migrated_from: null
---

Kudelski Security, a Swiss research lab headquartered in Cheseaux-sur-Lausanne, reconstructs connections between North Korean state-linked cybercrime and fake-IT-worker operations via a stealer-log leak. An actor the researchers designate "Bismarck," linked to DPRK-run gambling platforms, reused infrastructure that overlaps with the FakeCalls Android banking trojan (previously documented by Check Point targeting South Korean banking customers via voice-phishing app impersonation): "we recently observed a stealer log leak involving an actor linked to the DPRK, nicknamed 'Bismarck.' The actor used two IP addresses that overlap with indicators of compromise (IOCs) documented by Check Point Research in its analysis of FakeCalls, an Android banking trojan targeting South Korea" ([Kudelski Security, 2026-08-12](https://kudelskisecurity.com/research/inside-north-koreas-cybercrime-ecosystem-fake-it-workers-gambling-networks-and-malware)). Kudelski assesses the infrastructure reuse most plausibly reflects that the gambling-operation domains were purchased by DPRK associates rather than by Bismarck directly.

Separately, a DPRK-affiliated manager's own WinSCP credential vault — stolen in a 2021 leak — held access to historical Emotet botnet loader infrastructure, and cross-referencing that infrastructure's later reuse ties it into a loader role for subsequent campaigns. The investigation names operational bases and identifies university-affiliated IT-worker pipelines at named North Korean technical universities, plus organisational entities supporting fake IT-worker placement across multiple countries — directly relevant tradecraft for this constituency's HR and identity-vetting teams screening remote-hire pipelines, where a DPRK IT worker's fabricated identity and credentials are the initial-access vector rather than a technical exploit.

Kudelski's own article treats Bismarck as distinct from the already-tracked PurpleDelta North Korean IT-worker cluster rather than as an alias. This is a research/awareness finding for HR and identity-vetting process design rather than a technical exposure with a specific patch, hunt or block action.
