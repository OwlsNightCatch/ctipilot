---
schema: 1
kind: vulnerability
title: "Three misp-stix flaws put the CTI pipeline itself in scope: a crafted STIX document can set its own MISP distribution and sharing fields, kill a long-running importer, or bleed data into the next event"
headline: "The library that converts STIX into MISP decided a document was trustworthy using markers the sender controls — and the fix exists only as commits"
summary: >
  Three CVEs disclosed on 2026-08-21 against misp-stix, the Python library MISP and other platforms use to convert between MISP and STIX 1 / STIX 2, put the intelligence-ingestion path itself in scope. CVE-2026-77710 (CVSS 4.0 6.9) is the load-bearing one: the importer decided whether an incoming document was a trusted internal MISP export using markers inside the document — STIX2 tool labels, the STIX1 title — that the producer fully controls, and treated the resulting attributes as trusted enough to copy a whole metadata dictionary onto them, letting a crafted bundle set distribution, sharing_group_id and tags on imported attributes. CVE-2026-77755 (8.7) lets one malformed document terminate a long-running importer outright because the failure path raised SystemExit, which callers' exception handlers do not catch. CVE-2026-77761 (6.3) leaks state between documents when a parser instance is reused. No tagged release carries the fixes — the last affected version is 2026.7.8 and remediation is individual commits.
discovered_at: "2026-08-23T04:44:00Z"
event_date: "2026-08-21"
run_id: 2026-08-23T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, supply-chain, dos, info-disclosure, no-patch]
regions: [global, europe]
sectors: [public-sector]
entities: []
techniques: [T1565.001, T1499]
affected_products: ["MISP misp-stix"]
cves:
  - id: CVE-2026-77710
    cvss: "6.9"
    epss: "0.29"
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "≤ 2026.7.8"
    fixed: "no tagged release; commits 3e5e7bda and 66c654b9"
  - id: CVE-2026-77755
    cvss: "8.7"
    epss: "0.30"
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "≤ 2026.7.8"
    fixed: "no tagged release; commits 66119552 and e8e732ad"
  - id: CVE-2026-77761
    cvss: "6.3"
    epss: "0.37"
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "≤ 2026.7.8"
    fixed: "no tagged release; commits ad4f0a65, f08373dd and f6593931"
sources:
  - url: "https://osv.dev/vulnerability/CVE-2026-77710"
    publisher: "MISP Project advisory (via OSV.dev)"
    date: "2026-08-21"
    role: primary
  - url: "https://osv.dev/vulnerability/CVE-2026-77755"
    publisher: "MISP Project advisory (via OSV.dev)"
    date: "2026-08-21"
    role: primary
  - url: "https://osv.dev/vulnerability/CVE-2026-77761"
    publisher: "MISP Project advisory (via OSV.dev)"
    date: "2026-08-21"
    role: primary
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-63850"
    publisher: "ENISA EU Vulnerability Database"
    date: "2026-08-21"
    role: corroborating
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-63881"
    publisher: "ENISA EU Vulnerability Database"
    date: "2026-08-21"
    role: corroborating
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-63883"
    publisher: "ENISA EU Vulnerability Database"
    date: "2026-08-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "These classification indicators are fully controlled by the STIX producer and therefore cannot constitute a trusted indication of the document's origin."
    publisher: "MISP Project advisory (via OSV.dev)"
  - quote: "a malformed STIX document could terminate a long-running importer process instead of returning a recoverable parsing error"
    publisher: "MISP Project advisory (via OSV.dev)"
  - quote: "An attacker able to influence documents processed by such a long-lived parser could potentially cause information from one conversion to contaminate a subsequent MISP event."
    publisher: "MISP Project advisory (via OSV.dev)"
verification: single-source
sourcing_note: >
  All three advisories are authored by the MISP project as the maintainer of the affected library, so
  they are one assessor with several publishers rather than independent corroboration — ENISA's EU
  Vulnerability Database and OSV.dev both republish the same records, and the base scores and EPSS
  values cited here are read from the ENISA records. The advisory text was read through OSV.dev
  because github.com is not reachable from this pipeline's egress path; the content is the same
  advisory the project published. Each flaw's base score and EPSS are cited to that flaw's own vulnerability-database record rather than to one record standing in for all three.
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
  - "Audit any misp-stix automation that reuses one parser instance across several documents — batch import scripts are the affected pattern — and switch it to a fresh parser per document; per-file CLI invocations are unaffected."
migrated_from: null
---

Three CVEs published on 2026-08-21 against `misp-stix` — the Python library MISP and other threat-intelligence platforms use to convert between MISP's own format and STIX 1 / STIX 2 — sit in the ingestion path of the intelligence pipeline rather than in an internet-facing service, which is what makes them relevant to a constituency whose national CERTs, ISACs and sector sharing communities run MISP.

The one that changes a trust assumption is **CVE-2026-77710** (CVSS 4.0 base 6.9). The import logic chose between the internal-MISP parser and the external-STIX parser using metadata carried in the document itself: MISP-specific tool labels for STIX2, the document title for STIX1. The advisory states plainly that *"These classification indicators are fully controlled by the STIX producer and therefore cannot constitute a trusted indication of the document's origin"* ([MISP Project advisory, 2026-08-21](https://osv.dev/vulnerability/CVE-2026-77710)). When a document was accepted as an internal export, attributes inside an `x-misp-object` were converted by copying the entire `x_misp_attributes` dictionary straight into `add_attribute()`, so a crafted bundle could supply fields outside the expected round-trip format — the advisory names `distribution`, `sharing_group_id` and `tags` specifically. The consequence it draws is the one that matters operationally: imported intelligence could be given sharing restrictions or classification the importing organisation never chose, *"potentially causing information to be shared contrary to the importing organization's policy"*, or could carry attacker-chosen tags that downstream automation keys on. The fix introduces an explicit classification parameter so the caller decides, and restricts assignment to an allow-list.

**CVE-2026-77755** (8.7) is the availability half. The importer used `sys.exit()` on several parse and load failures; because `SystemExit` inherits from `BaseException` rather than `Exception`, those failures walked straight past the `except Exception` handlers a calling application would normally wrap an import in, so *"a malformed STIX document could terminate a long-running importer process instead of returning a recoverable parsing error"* ([MISP Project advisory, 2026-08-21](https://osv.dev/vulnerability/CVE-2026-77755)). Separately, no size limit was applied before parsing, and the advisory puts memory use during conversion at roughly two to seven times the input size — so a large crafted document degrades or kills the service during deserialisation. The fixes replace the exits with catchable exceptions and add a size ceiling, defaulting to 100 MB, that callers can adjust or disable.

**CVE-2026-77761** (6.3) is narrower and depends on how the library is called. Several STIX1 and STIX2 parser components kept per-document state across a reset — galaxy and galaxy-cluster data, references, passive DNS bookkeeping, package titles, dates and timestamps — so reusing one parser instance across independent documents could produce an event carrying information that was only present in an earlier one. The advisory notes an attacker who can influence what such a long-lived parser processes *"could potentially cause information from one conversion to contaminate a subsequent MISP event"*, and flags that where consecutive documents carry different distribution scopes the retained state can disclose a little of the earlier one ([MISP Project advisory, 2026-08-21](https://osv.dev/vulnerability/CVE-2026-77761)). Entry points that instantiate a fresh parser per file are not affected.

None of the three is reported as exploited, and each carries an EPSS below 0.4% on its own record — 0.29 for the trust-boundary flaw ([ENISA EU Vulnerability Database, 2026-08-21](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-63850)), 0.30 for the denial of service ([ENISA EU Vulnerability Database, 2026-08-21](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-63881)) and 0.37 for the state-contamination flaw ([ENISA EU Vulnerability Database, 2026-08-21](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-63883)). The reason they still warrant attention is the remediation state: the last affected version is 2026.7.8 and no tagged release yet carries any of the fixes — remediation today means applying individual commits.

**Defender takeaway:** the realistic delivery path is not a network attack on the MISP instance but a document arriving through a sharing relationship that already works as designed — from a partner whose own instance was compromised, or from a feed that accepts third-party submissions. That inverts the usual review order: an ingested bundle's `distribution`, `sharing_group_id` and tag fields deserve the same scrutiny as the indicators inside it, because until these fixes are applied those fields are attacker-settable rather than pipeline-derived. **Triage:** a genuine internal MISP export and a spoofed one are indistinguishable on the markers the parser used, so the discriminator is not the document — it is provenance the transport establishes independently, such as which authenticated feed or sync user delivered it, checked against whether that partner is one whose exports should be carrying MISP-internal metadata at all.
