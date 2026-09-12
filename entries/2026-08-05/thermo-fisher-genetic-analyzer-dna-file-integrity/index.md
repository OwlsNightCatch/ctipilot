---
schema: 1
kind: vulnerability
title: >
  CVE-2026-17583 — Thermo Fisher Applied Biosystems genetic analyzers write DNA result files with
  no integrity checking, so results can be altered after the run and no vendor fix is offered
headline: >
  CISA flags an evidence-integrity flaw in the DNA analyzers forensic and clinical labs run — no
  patch
summary: >
  CISA published ICSMA-26-216-01 on 2026-08-04 covering CVE-2026-17583 in Thermo Fisher Applied
  Biosystems genetic analyzers: the .fsa and .hid instrument output files carry no integrity check
  and can be edited after the fact, so anyone with access to the data-collection workstation or
  its file store can alter DNA data and produce inaccurate results. CVSS 3.1 8.4 with a local
  attack vector and no privileges required. The advisory names no vendor patch — the
  recommendations are exposure minimisation and defence in depth. The exposure that matters for
  this constituency is forensic-science institutes and clinical genomics laboratories, where the
  impact is a falsified result rather than a data breach.
discovered_at: "2026-08-05T04:12:23Z"
updated_at: null
event_date: 2026-08-04
run_id: 2026-08-05T0412Z-intel
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - no-patch
  - ot-ics
  - patch-available
regions:
  - global
  - europe
sectors:
  - healthcare
  - public-sector
  - legal-services
entities: []
techniques:
  - T1565.001
affected_products:
  - Thermo Fisher Applied Biosystems Genetic Analyzers
  - Applied Biosystems GeneMapper ID-X
  - Applied Biosystems SeqStudio Genetic Analyzer
  - Thermo Fisher Applied Biosystems 3500 Series Data Collection Software
  - Thermo Fisher Applied Biosystems 3730 Series Data Collection Software
  - Thermo Fisher Applied Biosystems SeqStudio Genetic Analyzer Data Collection Software
  - Thermo Fisher Applied Biosystems SeqStudio Flex Series Instrument Software
  - Thermo Fisher Applied Biosystems GeneMapper ID-X Software
cves:
  - id: CVE-2026-17583
    cvss: "8.4"
    epss: null
    type: logic-flaw
    vector: local
    auth: pre-auth
    status:
      - patch-available
    affected: >
      Applied Biosystems 3500/3500xL Data Collection Software 4.0.2 and earlier, 3730/3730xL 5.0.2 and
      earlier, SeqStudio Genetic Analyzer 1.2.5 and earlier, SeqStudio Flex 1.2.0 and earlier,
      GeneMapper ID-X 1.7.3 and earlier, 3130 Series 4.1 and earlier, ABI PRISM 3100/3100-Avant 2.0
      and earlier, ABI PRISM 310 3.1 and earlier.
    fixed: >
      3500/3500xL Data Collection Software 4.0.3; 3730/3730xL Data Collection Software 5.0.3;
      SeqStudio Genetic Analyzer Data Collection Software 1.2.6; SeqStudio Flex Series Instrument
      Software 1.2.1; GeneMapper ID-X Software 1.7.4. The 3130 Series, ABI PRISM 3100/3100-Avant and
      ABI PRISM 310 Data Collection Software are end of life and receive no update.
    status_note: >
      The original entry recorded status [no-patch] and fixed: none stated. Both were wrong; this
      record supersedes them.
sources:
  - url: "https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-216-01"
    publisher: CISA
    date: 2026-08-04
    role: primary
  - url: "https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2026/icsma-26-216-01.json"
    publisher: CISA
    date: 2026-08-04
    role: corroborating
closed_sources: []
evidence:
  - quote: "Successful exploitation of this vulnerability could allow an attacker to modify .fsa/.hid output files, tampering with DNA data and resulting in inaccurate test results."
    publisher: CISA
  - quote: "Thermo Fisher has developed security updates to address the vulnerability. The security updates implement the use of digital signatures on the instrument software that adds an extralayer of protection. Moving forward, this will help users verify that data files have not been modified."
    publisher: CISA
  - quote: "Applied Biosystems 3500/3500xL Series Data Collection Software: Update to version 4.0.3"
    publisher: CISA
  - quote: "Applied Biosystems 3130 Series Data Collection Software: Product is End of Life (EoL), no update provided"
    publisher: CISA
verification: single-source-national-cert
sourcing_note: >
  Single-source under the national-authority carve-out: CISA is the coordinating disclosing party
  for this ICS medical advisory. No vendor advisory or independent analysis had been published at
  the time of writing.
confidence: high
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
  - "Update the genetic-analyzer software this entry names to 4.0.3, 5.0.3, 1.2.6, 1.2.1 or 1.7.4 as applicable, rather than treating the flaw as unpatchable — and for the three end-of-life ABI PRISM and 3130 Series lines, where no update exists, keep the archival control the earlier entry described, because for those products it remains the only option."
updates:
  - at: "2026-08-09T14:15:00Z"
    run_id: 2026-08-09T1315Z-audit
    type: correction
    summary: >
      The 2026-08-05 entry here on CVE-2026-17583 stated throughout — in its title, its
      summary, its cves[] status and its action item — that Thermo Fisher offered no fix for the
      missing integrity checking on Applied Biosystems genetic-analyzer result files, and told readers
      the control that closes the gap is architectural because there is no patch to wait for. That is
      wrong against the entry's own cited advisory. CISA ICSMA-26-216-01 carries vendor-fix
      remediations naming patched versions for five product lines — 3500/3500xL Data Collection
      Software 4.0.3, 3730/3730xL 5.0.3, SeqStudio 1.2.6, SeqStudio Flex 1.2.1 and GeneMapper ID-X
      1.7.4 — and only the three end-of-life ABI PRISM and 3130 Series products have no update. The
      updates implement digital signatures on the instrument software so users can verify that data
      files have not been modified, which is the control the original entry argued was unavailable.
      The advisory is at revision 1 and has never been revised, so the fixes were present when the
      original entry was composed.
    fields:
      - actions
      - affected_products
      - cves
      - evidence
      - priority
      - sectors
      - sources
      - tags
      - body
    merged_from: 2026-08-09/thermo-fisher-genetic-analyzer-correction-patch-exists
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      v4.2 migration: pipeline-internal phrasing removed from the correction section; 
      updated_at recomputed under the new float rule where applicable.
    fields: [updated_at, body]
migrated_from: null
---

CISA published ICS medical advisory ICSMA-26-216-01 on 2026-08-04, covering CVE-2026-17583 in Thermo Fisher Applied Biosystems genetic analyzers. The defect is a missing integrity check: the .fsa and .hid files these instruments produce can be edited after they are written, and CISA states that successful exploitation could allow an attacker to modify those output files, tampering with DNA data and resulting in inaccurate test results ([CISA, 2026-08-04](https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-216-01)). The advisory carries a CVSS 3.1 base score of 8.4 with a local attack vector, requiring no privileges and no user interaction once the attacker is on the data-collection workstation. The affected list is long and spans generations of hardware, from the current SeqStudio and 3500 series back to the ABI PRISM 310, and CISA names no vendor patch — its recommendations are minimising exposure and defence in depth.

**The reason this belongs in a European public-sector brief despite a local-only vector is who runs these instruments.** These are the capillary-electrophoresis platforms used by forensic-science institutes serving police and judicial processes, and by clinical and public-health genomics laboratories. The impact class is unusual for this brief: not confidentiality, not availability, but integrity of a result that a court or a clinician will rely on. A tampered .fsa file does not announce itself as an incident — it produces a wrong answer that everything downstream treats as correct, and the instrument software offers no way to detect that the file changed after the run that produced it.

The attack precondition is access to the data-collection workstation or its file store, which places this firmly in the post-compromise and insider space rather than the remote-exploitation space. That is also why the usual triage instinct — low CVSS vector, no exploitation reported, wait for the patch — reaches the wrong answer here. There is no patch to wait for, and the control that closes the gap is architectural rather than a software update.

Detection concepts, telemetry class first. File-integrity monitoring on the .fsa and .hid output directories is the direct signal, and the specific event worth alerting on is a write or rename to a result file after the run that generated it has completed — a legitimate instrument run creates its outputs once. Correlate that with interactive logon events and removable-media events on the data-collection workstation, since the vector requires someone or something operating on that host.

**Triage:** laboratory information systems, backup agents and analysis software legitimately read these files constantly, and reanalysis workflows may write new derived files. The discriminator is modification in place of an existing result file versus creation of a new one, and whether the writing process is the instrument's own data-collection software during an active run.

**Defender takeaway:** treat this as a records-integrity control problem rather than a vulnerability-management one. Isolating analyser workstations on a dedicated laboratory network with no internet path and restricting interactive logon to named operators reduces who can reach the files; but the control that actually makes tampering detectable is holding completed result files in an append-only or cryptographically signed archive, so that a later edit is visible even though the instrument software will never notice it. For laboratories whose output supports judicial or clinical decisions, that detectability is the property worth engineering for.

## Correction — 2026-08-09T14:15:00Z

The earlier entry's central claim was false, and the correction runs the wrong way round from the usual — a flaw previously described here as unfixable has a fix, and readers were told not to look for one.

CISA's advisory ICSMA-26-216-01 carries eight per-product vendor-fix records for this flaw, alongside seven mitigation records. Five of the eight name a patched version for a specific product line: "Applied Biosystems 3500/3500xL Series Data Collection Software: Update to version 4.0.3", and correspondingly 3730/3730xL Data Collection Software to 5.0.3, SeqStudio Genetic Analyzer Data Collection Software to 1.2.6, SeqStudio Flex Series Instrument Software to 1.2.1, and GeneMapper ID-X Software to 1.7.4 ([CISA ICSMA-26-216-01 (CSAF), 2026-08-04](https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2026/icsma-26-216-01.json)). Three products are genuinely unfixed, and the advisory says why rather than staying silent: the 3130 Series, ABI PRISM 3100/3100-Avant and ABI PRISM 310 Data Collection Software each carry "Product is End of Life (EoL), no update provided" ([CISA ICSMA-26-216-01 (CSAF), 2026-08-04](https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2026/icsma-26-216-01.json)). The original entry generalised the end-of-life products' position to the whole product set.

The substance of the fix matters as much as its existence, because the earlier entry argued that no software update could address the problem and that only an architectural control — moving completed `.fsa`/`.hid` files into append-only or signed storage — would do. The advisory says the updates do precisely that job in the instrument software: "Thermo Fisher has developed security updates to address the vulnerability. The security updates implement the use of digital signatures on the instrument software that adds an extralayer of protection. Moving forward, this will help users verify that data files have not been modified" ([CISA ICSMA-26-216-01 (CSAF), 2026-08-04](https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2026/icsma-26-216-01.json)). The interim measures the original entry treated as the whole answer — encrypted storage media, access restriction to authorised personnel, least privilege on the instrument hosts, and firewall rules and network ACLs limiting internet connectivity to trusted sources — are in the advisory as what to do *until* the applicable updates are installed, not instead of them.

Nothing about the flaw itself changes: the CVSS 3.1 base score of 8.4, the local attack vector, the affected version list and the mechanism — result files written with no integrity checking, so a file altered after the run reads as authentic — were all correct in the original entry and were re-verified in this audit. What changes is the disposition. For five of the eight product lines this is a patching task on a normal change window, and this entry's vulnerability record now carries the patched versions — the earlier no-patch status would otherwise leave anyone asking "is my version patched?" with a wrong no.

**Defender takeaway:** where genetic-analyzer output feeds forensic or clinical reporting, install the applicable update and get the signature check the vendor built, then keep the archival control for the three end-of-life lines that will never receive one. The original entry's advice was right only for those three.

**Triage:** an instrument host still reporting a Data Collection Software version at or below the affected boundary after the update window is the discriminator between "unpatchable end-of-life product" and "patchable product nobody updated" — the two look identical in an asset inventory that records only the product family, and only the version string separates them.
