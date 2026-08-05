---
schema: 1
kind: vulnerability
horizon: operational
title: "CVE-2026-17583 — Thermo Fisher Applied Biosystems genetic analyzers write DNA result files with no integrity checking, so results can be altered after the run and no vendor fix is offered"
headline: "CISA flags an evidence-integrity flaw in the DNA analyzers forensic and clinical labs run — no patch"
summary: >
  CISA published ICSMA-26-216-01 on 2026-08-04 covering CVE-2026-17583 in Thermo Fisher Applied
  Biosystems genetic analyzers: the .fsa and .hid instrument output files carry no integrity check and
  can be edited after the fact, so anyone with access to the data-collection workstation or its file
  store can alter DNA data and produce inaccurate results. CVSS 3.1 8.4 with a local attack vector and
  no privileges required. The advisory names no vendor patch — the recommendations are exposure
  minimisation and defence in depth. The exposure that matters for this constituency is forensic-science
  institutes and clinical genomics laboratories, where the impact is a falsified result rather than a
  data breach.
discovered_at: "2026-08-05T04:12:23Z"
event_date: "2026-08-04"
run_id: 2026-08-05T0412Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, no-patch, ot-ics]
regions: [global, europe]
sectors: [healthcare, public-sector]
entities: []
techniques: [T1565.001]
affected_products: ["Thermo Fisher Applied Biosystems Genetic Analyzers", "Applied Biosystems GeneMapper ID-X", "Applied Biosystems SeqStudio Genetic Analyzer"]
cves:
  - id: CVE-2026-17583
    cvss: "8.4"
    epss: null
    type: logic-flaw
    vector: local
    auth: pre-auth
    status: [no-patch]
    affected: "Applied Biosystems 3500/3500xL Data Collection Software 4.0.2 and earlier, 3730/3730xL 5.0.2 and earlier, SeqStudio Genetic Analyzer 1.2.5 and earlier, SeqStudio Flex 1.2.0 and earlier, GeneMapper ID-X v1.7.3 and earlier, 3130 Series 4.1 and earlier, ABI PRISM 3100/3100-Avant 2.0 and earlier, ABI PRISM 310 3.1 and earlier."
    fixed: "None stated in the advisory — CISA's recommendations are exposure minimisation and defence in depth rather than an update."
sources:
  - url: "https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-216-01"
    publisher: "CISA"
    date: "2026-08-04"
    role: primary
closed_sources: []
evidence:
  - quote: "Successful exploitation of this vulnerability could allow an attacker to modify .fsa/.hid output files, tampering with DNA data and resulting in inaccurate test results."
    publisher: "CISA"
verification: single-source-national-cert
sourcing_note: "Single-source under the national-authority carve-out: CISA is the coordinating disclosing party for this ICS medical advisory. No vendor advisory or independent analysis had been published at the time of writing."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Where genetic-analyzer output feeds forensic or clinical reporting, move completed .fsa/.hid files into an append-only or cryptographically signed archive at the end of each run, because no vendor fix exists and the instrument software cannot detect a post-hoc edit."
migrated_from: null
---

CISA published ICS medical advisory ICSMA-26-216-01 on 2026-08-04, covering CVE-2026-17583 in Thermo Fisher Applied Biosystems genetic analyzers. The defect is a missing integrity check: the .fsa and .hid files these instruments produce can be edited after they are written, and CISA states that successful exploitation could allow an attacker to modify those output files, tampering with DNA data and resulting in inaccurate test results ([CISA, 2026-08-04](https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-216-01)). The advisory carries a CVSS 3.1 base score of 8.4 with a local attack vector, requiring no privileges and no user interaction once the attacker is on the data-collection workstation. The affected list is long and spans generations of hardware, from the current SeqStudio and 3500 series back to the ABI PRISM 310, and CISA names no vendor patch — its recommendations are minimising exposure and defence in depth.

**The reason this belongs in a European public-sector brief despite a local-only vector is who runs these instruments.** These are the capillary-electrophoresis platforms used by forensic-science institutes serving police and judicial processes, and by clinical and public-health genomics laboratories. The impact class is unusual for this brief: not confidentiality, not availability, but integrity of a result that a court or a clinician will rely on. A tampered .fsa file does not announce itself as an incident — it produces a wrong answer that everything downstream treats as correct, and the instrument software offers no way to detect that the file changed after the run that produced it.

The attack precondition is access to the data-collection workstation or its file store, which places this firmly in the post-compromise and insider space rather than the remote-exploitation space. That is also why the usual triage instinct — low CVSS vector, no exploitation reported, wait for the patch — reaches the wrong answer here. There is no patch to wait for, and the control that closes the gap is architectural rather than a software update.

Detection concepts, telemetry class first. File-integrity monitoring on the .fsa and .hid output directories is the direct signal, and the specific event worth alerting on is a write or rename to a result file after the run that generated it has completed — a legitimate instrument run creates its outputs once. Correlate that with interactive logon events and removable-media events on the data-collection workstation, since the vector requires someone or something operating on that host.

**Triage:** laboratory information systems, backup agents and analysis software legitimately read these files constantly, and reanalysis workflows may write new derived files. The discriminator is modification in place of an existing result file versus creation of a new one, and whether the writing process is the instrument's own data-collection software during an active run.

**Defender takeaway:** treat this as a records-integrity control problem rather than a vulnerability-management one. Isolating analyser workstations on a dedicated laboratory network with no internet path and restricting interactive logon to named operators reduces who can reach the files; but the control that actually makes tampering detectable is holding completed result files in an append-only or cryptographically signed archive, so that a later edit is visible even though the instrument software will never notice it. For laboratories whose output supports judicial or clinical decisions, that detectability is the property worth engineering for.
