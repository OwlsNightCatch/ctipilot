---
schema: 1
kind: vulnerability
horizon: operational
title: "CVE-2026-77710 — a crafted STIX document can tell MISP's own import library that it is MISP-native, and then set the distribution and sharing-group fields on the intelligence it creates"
headline: "Three CVEs in the library MISP uses to ingest external threat intel, and none of the fixes is in a release you can install"
summary: >
  CIRCL, Luxembourg's national CERT and the numbering authority for MISP vulnerabilities, published three
  flaws in misp-stix, the library MISP instances use to import and export STIX threat-intelligence
  documents. The structurally serious one is CVE-2026-77710: the import logic decided whether an incoming
  document was MISP-native from producer-controlled markers, and on that basis copied an entire
  attacker-supplied attribute dictionary in without an allow-list — so a crafted bundle can set
  security-relevant properties including distribution, sharing-group and tags on the intelligence it
  creates. CVE-2026-77755 lets one malformed document terminate a long-running import process through an
  exception callers cannot catch, and adds an unbounded memory path. CVE-2026-77761 leaks state between
  documents parsed by a reused parser. All three fixes exist only as commits: the newest released version
  remains 2026.7.8, so there is nothing to install.
discovered_at: "2026-08-22T05:12:30Z"
event_date: "2026-08-21"
run_id: 2026-08-22T0410Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, no-patch, supply-chain, info-disclosure, dos]
regions: [europe, global]
sectors: [public-sector]
entities: []
techniques: [T1565.001, T1499]
affected_products: ["MISP misp-stix"]
cves:
  - id: CVE-2026-77710
    cvss: "6.9"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "misp-stix up to and including 2026.7.8"
    fixed: "fix commits merged upstream; no tagged release and no installable package version as of 2026-08-22"
  - id: CVE-2026-77755
    cvss: "8.7"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "misp-stix up to and including 2026.7.8"
    fixed: "fix commits merged upstream; no tagged release and no installable package version as of 2026-08-22"
  - id: CVE-2026-77761
    cvss: "6.3"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "misp-stix up to and including 2026.7.8"
    fixed: "fix commits merged upstream; no tagged release and no installable package version as of 2026-08-22"
sources:
  - url: "https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-63883"
    publisher: "ENISA EU Vulnerability Database (CIRCL as numbering authority)"
    date: "2026-08-21"
    role: primary
  - url: "https://github.com/advisories/GHSA-pqpx-w6cx-7q9c"
    publisher: "GitHub Security Advisory (CIRCL)"
    date: "2026-08-21"
    role: primary
  - url: "https://github.com/advisories/GHSA-65gx-wjvj-88j8"
    publisher: "GitHub Security Advisory (CIRCL)"
    date: "2026-08-21"
    role: primary
  - url: "https://pypi.org/project/misp-stix/#history"
    publisher: "PyPI"
    date: "2026-08-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A parser state isolation vulnerability in misp-stix could cause data from a previously processed STIX document to be retained and incorporated into the MISP event generated from a subsequent document when the same parser instance is reused."
    publisher: "ENISA EU Vulnerability Database (CIRCL as numbering authority)"
  - quote: "The issue primarily affects applications using the misp-stix API directly and reusing parser instances across independent STIX documents. Normal conversion entry points that instantiate a new parser for each file are not affected by this particular reuse scenario."
    publisher: "ENISA EU Vulnerability Database (CIRCL as numbering authority)"
verification: multi-source
sourcing_note: >
  CIRCL is both the maintaining organisation and the numbering authority here, so every record traces to
  one first-party assessor: reliability A, credibility 2. The mechanism descriptions for CVE-2026-77710 and
  CVE-2026-77755 come from their advisory records, which could only be read through a transport that
  summarises rather than returning raw page text this run — the advisory host refused the direct transport
  and the reader fallback was credit-exhausted — so those two descriptions are paraphrased in the body and
  are deliberately not carried as verbatim quotes in `evidence`, where only the record this run could
  literal-check appears. No advisory record for CVE-2026-77761 could be located at all; its CVE record with
  CIRCL as the numbering authority is the primary for that flaw instead, which is a first-party source
  rather than a downgrade. The release state is confirmed twice over, from the project's own release list
  and from the package index independently, both agreeing the newest version is 2026.7.8 from 8 July 2026 —
  so the absence of an installable fix is established rather than inferred from the advisories' silence. No
  source reports exploitation of any of the three.
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
  - "On any MISP instance that ingests STIX from outside the organisation, stop reusing a single long-lived parser instance across documents from different feeds or trust levels — CIRCL states the state-leak flaw affects applications driving the library's API directly and reusing parsers, and does not affect conversion paths that instantiate a fresh parser per file. Until a release ships, pin to a post-fix commit or apply the referenced commits, and enforce an input-size cap ahead of any import workflow."
  - "Review recently imported STIX-derived events for distribution and sharing-group values that do not match the ingesting feed's configured policy, and correct any that are wider than intended. The trust-decision flaw lets an incoming document set those fields directly, so the consequence is intelligence shared further than the operator chose — which is not something the import log will flag as an error."
migrated_from: null
---

CIRCL — Luxembourg's national CERT, the organisation that maintains MISP, and the numbering authority for MISP-project vulnerabilities — published three flaws on 2026-08-21 in misp-stix, the Python library MISP instances use to import and export STIX threat-intelligence documents. For any SOC, CERT or sector ISAC that ingests external STIX feeds into MISP, this is a flaw in the doorway rather than in a peripheral component.

CVE-2026-77710 is the one worth reading twice. The import path decided whether an incoming document should be treated as MISP-native — that is, as a document produced by another MISP instance and therefore round-tripping MISP's own field structure — from markers the producing party controls: tool labels in the STIX 2 case and the document title in the STIX 1 case. An untrusted value was driving a security-relevant trust decision. Where a document was classified as native, the code copied an entire attacker-supplied attribute dictionary straight into the object-construction call with no allow-list, so a crafted bundle can supply fields outside the expected round-trip format including security-sensitive properties such as distribution, sharing-group identifier and tags. Those three fields are the ones that decide who inside and outside the organisation gets to see an event ([GitHub Security Advisory, 2026-08-21](https://github.com/advisories/GHSA-pqpx-w6cx-7q9c)). The consequence is not a compromise of the MISP host: it is intelligence entering the platform pre-labelled with a visibility the operator did not choose, through a mechanism the import log has no reason to record as anomalous. CIRCL rates it 6.9 ([GitHub Security Advisory, 2026-08-21](https://github.com/advisories/GHSA-pqpx-w6cx-7q9c)), which is a fair reflection of the technical severity and understates the operational one for a national or governmental instance whose sharing groups are the control that keeps sensitive material inside a community.

The other two are more conventional. CVE-2026-77755, rated 8.7, is a denial of service with two independent halves: the import code called a process-exit function on several parse-failure paths, and because the resulting exception derives from the base exception class rather than the ordinary one, a caller's normal error handling does not catch it — a single malformed document can therefore end a long-running import process. Separately, no input-size limit was enforced before parsing, and the advisory records that processing could consume roughly two to seven times the input size in memory. The fix replaces the process-terminating calls with catchable exceptions and introduces a size limit defaulting to 100 MB that callers can adjust or explicitly disable ([GitHub Security Advisory, 2026-08-21](https://github.com/advisories/GHSA-65gx-wjvj-88j8)). CVE-2026-77761, rated 6.3, is a state-isolation failure: CIRCL states that data from a previously processed STIX document can be retained and incorporated into the MISP event generated from a subsequent document when the same parser instance is reused ([ENISA EU Vulnerability Database, 2026-08-21](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-63883)). It is precisely scoped, and the scoping is the actionable part — CIRCL states the issue primarily affects applications using the library's API directly and reusing parser instances across independent documents, and that normal conversion entry points instantiating a new parser per file are not affected by that reuse scenario ([ENISA EU Vulnerability Database, 2026-08-21](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-63883)).

**Defender takeaway:** the operational fact that outranks all three severities is that there is nothing to install. The fixes exist as merged commits; the newest released version of the library remains 2026.7.8 from 8 July 2026, confirmed independently against both the project's own release list and the package index, and every affected range runs up to and including that version. A team that patches by upgrading has no upgrade available, so the choices are pinning to a post-fix commit, applying the referenced commits, or living with the flaws under compensating controls — which is a decision someone has to make deliberately rather than a ticket that clears itself next cycle. The compensating controls follow directly from the mechanisms: cap input size ahead of the import workflow, stop reusing a parser instance across documents from different feeds or trust levels, and review the distribution and sharing-group values on recently imported STIX-derived events against what the ingesting feed's policy should have produced. There is no exploitation reported by anyone and no detection signature to write; the honest posture is a configuration review plus a data-integrity check on what has already been ingested. The wider point is one this pipeline keeps arriving at from different directions: the tooling the defensive community uses to exchange intelligence is itself software with an attack surface, and a document format designed for machine consumption between trusted parties inherits every weakness of the trust decision that admits it.
