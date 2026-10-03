---
schema: 1
kind: threat
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
  - quote: "We assess that DPRK actors may have reused IP addresses from the gambling operation because the domains were purchased by the associates rather than by “Bismarck” or other North Korean operatives."
    publisher: "Kudelski Security"
verification: single-source
sourcing_note: >
  Kudelski Security is the sole source and original investigator; its article names specific IP
  addresses and hostnames as infrastructure evidence for the overlap claim, deliberately not
  reproduced here or in evidence quotes (indicators are left out) — the quotes above are chosen to carry the analytic claim without the indicators. The FakeCalls malware
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
  - at: "2026-08-30T13:12:06Z"
    run_id: 2026-08-30T1312Z-audit
    type: correction
    summary: >
      This entry said Kudelski's report treats Bismarck as distinct from the already-tracked
      PurpleDelta IT-worker cluster rather than as an alias. Kudelski's report never mentions
      PurpleDelta at all, so it makes no such judgement in either direction, and presenting a
      silence as a stated analytic position is a claim the source does not support. Replaced with
      what the report does and does not say.
    fields: [body]
  - at: "2026-09-29T23:44:54Z"
    run_id: 2026-09-29T2134Z-audit
    type: correction
    summary: >
      The analysis stated Kudelski's explanation for the infrastructure overlap more firmly and more
      narrowly than Kudelski does. Kudelski says DPRK actors "may have" reused the gambling
      operation's IP addresses because associates, rather than Bismarck or other North Korean
      operatives, bought the domains. The analysis and the evidence quotation now carry that wording,
      and the 2026-08-30 correction cites the report under its publication date of 2026-08-12. The
      sourcing note no longer describes the quotes as redacted, since they are now verbatim.
    fields: [evidence, sourcing_note, body]
migrated_from: null
---

Kudelski Security, a Swiss research lab headquartered in Cheseaux-sur-Lausanne, reconstructs connections between North Korean state-linked cybercrime and fake-IT-worker operations via a stealer-log leak. An actor the researchers designate "Bismarck," linked to DPRK-run gambling platforms, reused infrastructure that overlaps with the FakeCalls Android banking trojan (previously documented by Check Point targeting South Korean banking customers via voice-phishing app impersonation): "we recently observed a stealer log leak involving an actor linked to the DPRK, nicknamed 'Bismarck.' The actor used two IP addresses that overlap with indicators of compromise (IOCs) documented by Check Point Research in its analysis of FakeCalls, an Android banking trojan targeting South Korea" ([Kudelski Security, 2026-08-12](https://kudelskisecurity.com/research/inside-north-koreas-cybercrime-ecosystem-fake-it-workers-gambling-networks-and-malware)). Kudelski assesses that DPRK actors may have reused IP addresses from the gambling operation because the domains were purchased by associates rather than by Bismarck or other North Korean operatives.

Separately, a DPRK-affiliated manager's own WinSCP credential vault — stolen in a 2021 leak — held access to historical Emotet botnet loader infrastructure, and cross-referencing that infrastructure's later reuse ties it into a loader role for subsequent campaigns. The investigation names operational bases and identifies university-affiliated IT-worker pipelines at named North Korean technical universities, plus organisational entities supporting fake IT-worker placement across multiple countries — directly relevant tradecraft for this constituency's HR and identity-vetting teams screening remote-hire pipelines, where a DPRK IT worker's fabricated identity and credentials are the initial-access vector rather than a technical exploit.

Kudelski does not relate Bismarck to any previously named North Korean IT-worker cluster: its report names Bismarck, several DPRK universities and the "Base" system, and makes no comparison to other tracked clusters either way. This is a research/awareness finding for HR and identity-vetting process design rather than a technical exposure with a specific patch, hunt or block action.

## Correction — 2026-08-30T13:12:06Z

Kudelski's report does not distinguish Bismarck from the PurpleDelta IT-worker cluster, because it never mentions PurpleDelta. This entry previously presented that distinction as the source's own analytic position. The report names Bismarck, the DPRK universities behind it and the "Base" system, and draws no comparison to any other tracked cluster ([Kudelski Security, 2026-08-12](https://kudelskisecurity.com/research/inside-north-koreas-cybercrime-ecosystem-fake-it-workers-gambling-networks-and-malware)). Whether Bismarck overlaps an existing cluster is therefore an open question, not one this reporting answers.

## Correction — 2026-09-29T23:44:54Z

Kudelski's explanation for the infrastructure overlap is hedged, and this entry stated it more firmly and more narrowly than the report does. The report says: "We assess that DPRK actors may have reused IP addresses from the gambling operation because the domains were purchased by the associates rather than by “Bismarck” or other North Korean operatives" ([Kudelski Security, 2026-08-12](https://kudelskisecurity.com/research/inside-north-koreas-cybercrime-ecosystem-fake-it-workers-gambling-networks-and-malware)). The analysis above now carries that wording instead of "most plausibly" and "Bismarck directly". The overlap itself is unchanged.
