---
schema: 1
kind: vulnerability
horizon: operational
title: "Correction — Thermo Fisher shipped patched software for CVE-2026-17583 on five genetic-analyzer product lines, and the update implements exactly the file-integrity control this pipeline said did not exist"
headline: "This pipeline told readers there was no patch to wait for; the advisory it cited names five patched versions with download links"
summary: >
  This pipeline's 2026-08-05 entry on CVE-2026-17583 stated throughout — in its title, its summary, its
  cves[] status and its action item — that Thermo Fisher offered no fix for the missing integrity
  checking on Applied Biosystems genetic-analyzer result files, and told readers the control that
  closes the gap is architectural because there is no patch to wait for. That is wrong against the
  entry's own cited advisory. CISA ICSMA-26-216-01 carries vendor-fix remediations naming patched
  versions for five product lines — 3500/3500xL Data Collection Software 4.0.3, 3730/3730xL 5.0.3,
  SeqStudio 1.2.6, SeqStudio Flex 1.2.1 and GeneMapper ID-X 1.7.4 — and only the three end-of-life ABI
  PRISM and 3130 Series products have no update. The updates implement digital signatures on the
  instrument software so users can verify that data files have not been modified, which is the control
  the original entry argued was unavailable. The advisory is at revision 1 and has never been revised,
  so the fixes were present when the original entry was composed.
discovered_at: "2026-08-09T14:15:00Z"
event_date: "2026-08-04"
run_id: 2026-08-09T1315Z-audit
priority: high
immediate_action: null
tags: [vulnerabilities, patch-available, ot-ics]
regions: [global, europe]
sectors: [healthcare, public-sector, legal-services]
entities: []
techniques: [T1565.001]
affected_products: ["Thermo Fisher Applied Biosystems 3500 Series Data Collection Software", "Thermo Fisher Applied Biosystems 3730 Series Data Collection Software", "Thermo Fisher Applied Biosystems SeqStudio Genetic Analyzer Data Collection Software", "Thermo Fisher Applied Biosystems SeqStudio Flex Series Instrument Software", "Thermo Fisher Applied Biosystems GeneMapper ID-X Software"]
cves:
  - id: CVE-2026-17583
    cvss: "8.4"
    epss: null
    type: logic-flaw
    vector: local
    auth: pre-auth
    status: [patch-available]
    affected: "Applied Biosystems 3500/3500xL Data Collection Software 4.0.2 and earlier, 3730/3730xL 5.0.2 and earlier, SeqStudio Genetic Analyzer 1.2.5 and earlier, SeqStudio Flex 1.2.0 and earlier, GeneMapper ID-X 1.7.3 and earlier, 3130 Series 4.1 and earlier, ABI PRISM 3100/3100-Avant 2.0 and earlier, ABI PRISM 310 3.1 and earlier."
    fixed: "3500/3500xL Data Collection Software 4.0.3; 3730/3730xL Data Collection Software 5.0.3; SeqStudio Genetic Analyzer Data Collection Software 1.2.6; SeqStudio Flex Series Instrument Software 1.2.1; GeneMapper ID-X Software 1.7.4. The 3130 Series, ABI PRISM 3100/3100-Avant and ABI PRISM 310 Data Collection Software are end of life and receive no update."
    status_note: "The original entry recorded status [no-patch] and fixed: none stated. Both were wrong; this record supersedes them."
sources:
  - url: "https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-216-01"
    publisher: "CISA"
    date: "2026-08-04"
    role: primary
  - url: "https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2026/icsma-26-216-01.json"
    publisher: "CISA"
    date: "2026-08-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Thermo Fisher has developed security updates to address the vulnerability. The security updates implement the use of digital signatures on the instrument software that adds an extralayer of protection. Moving forward, this will help users verify that data files have not been modified."
    publisher: "CISA"
  - quote: "Applied Biosystems 3500/3500xL Series Data Collection Software: Update to version 4.0.3"
    publisher: "CISA"
  - quote: "Applied Biosystems 3130 Series Data Collection Software: Product is End of Life (EoL), no update provided"
    publisher: "CISA"
verification: single-source-national-cert
sourcing_note: >
  Single source under the national-authority carve-out: CISA is the coordinating publisher of
  ICSMA-26-216-01 and the CSAF record is the authoritative machine-readable form of the same advisory
  the original entry cited. The correction was found by this audit's retrospective truth pass, which
  established that the HTML rendering of the advisory dropped the mitigations block on two of three
  transports while the CSAF JSON carried all fifteen remediation records, the eight per-product fixes among them — the reason the original entry
  read the advisory as offering no fix. Credibility is 2 rather than 1 because one authority states
  it; nothing here needs corroboration beyond the record that carries the remediations.
confidence: high
update_of: 2026-08-05/thermo-fisher-genetic-analyzer-dna-file-integrity
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
classification:
  reliability: A
  credibility: 2
actions:
  - "Update the genetic-analyzer software this entry names to 4.0.3, 5.0.3, 1.2.6, 1.2.1 or 1.7.4 as applicable, rather than treating the flaw as unpatchable — and for the three end-of-life ABI PRISM and 3130 Series lines, where no update exists, keep the archival control the earlier entry described, because for those products it remains the only option."
---

**UPDATE (originally covered 2026-08-05):** the earlier entry's central claim was false, and the correction runs the wrong way round from the usual — a flaw this pipeline described as unfixable has a fix, and readers were told not to look for one.

CISA's advisory ICSMA-26-216-01 carries eight per-product vendor-fix records for this flaw, alongside seven mitigation records. Five of the eight name a patched version for a specific product line: "Applied Biosystems 3500/3500xL Series Data Collection Software: Update to version 4.0.3", and correspondingly 3730/3730xL Data Collection Software to 5.0.3, SeqStudio Genetic Analyzer Data Collection Software to 1.2.6, SeqStudio Flex Series Instrument Software to 1.2.1, and GeneMapper ID-X Software to 1.7.4 ([CISA ICSMA-26-216-01 (CSAF), 2026-08-04](https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2026/icsma-26-216-01.json)). Three products are genuinely unfixed, and the advisory says why rather than staying silent: the 3130 Series, ABI PRISM 3100/3100-Avant and ABI PRISM 310 Data Collection Software each carry "Product is End of Life (EoL), no update provided" ([CISA ICSMA-26-216-01 (CSAF), 2026-08-04](https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2026/icsma-26-216-01.json)). The original entry generalised the end-of-life products' position to the whole product set.

The substance of the fix matters as much as its existence, because the earlier entry argued that no software update could address the problem and that only an architectural control — moving completed `.fsa`/`.hid` files into append-only or signed storage — would do. The advisory says the updates do precisely that job in the instrument software: "Thermo Fisher has developed security updates to address the vulnerability. The security updates implement the use of digital signatures on the instrument software that adds an extralayer of protection. Moving forward, this will help users verify that data files have not been modified" ([CISA ICSMA-26-216-01 (CSAF), 2026-08-04](https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2026/icsma-26-216-01.json)). The interim measures the original entry treated as the whole answer — encrypted storage media, access restriction to authorised personnel, least privilege on the instrument hosts, and firewall rules and network ACLs limiting internet connectivity to trusted sources — are in the advisory as what to do *until* the applicable updates are installed, not instead of them.

Nothing about the flaw itself changes: the CVSS 3.1 base score of 8.4, the local attack vector, the affected version list and the mechanism — result files written with no integrity checking, so a file altered after the run reads as authentic — were all correct in the original entry and were re-verified in this audit. What changes is the disposition. For five of the eight product lines this is a patching task on a normal change window, and the frontmatter here supersedes the earlier `status: [no-patch]` and its empty `fixed` field, both of which would otherwise leave an automated triage consumer answering "is my version patched?" with a wrong no.

**Defender takeaway:** where genetic-analyzer output feeds forensic or clinical reporting, install the applicable update and get the signature check the vendor built, then keep the archival control for the three end-of-life lines that will never receive one. The original entry's advice was right only for those three.

**Triage:** an instrument host still reporting a Data Collection Software version at or below the affected boundary after the update window is the discriminator between "unpatchable end-of-life product" and "patchable product nobody updated" — the two look identical in an asset inventory that records only the product family, and only the version string separates them.
