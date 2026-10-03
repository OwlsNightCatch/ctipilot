---
schema: 1
kind: research
title: "BSI and NCSC-NL withdraw SQLite advisories built on LLM-fabricated CVEs — and GitHub's advisory database was still serving one of them"
headline: "Two national CERTs retract SQLite advisories because the CVEs describe bugs that do not exist, while the same records stay live downstream"
summary: >
  On 2026-08-03 NCSC-NL revised advisory NCSC-2026-0268 to state that its SQLite CVE was hallucinated by an LLM, and BSI
  CERT-Bund retitled two SQLite advisories (WID-SEC-2026-2581, WID-SEC-2026-2604) to "MELDUNG ZURÜCKGEZOGEN". The
  originating research is JFrog's reproduction audit of a batch published through one new GitHub repository: 54 of 55
  advisories were fabricated, and six SQLite entries (CVE-2026-51296, -51297, -51300, -51302, -51303, -51304) named
  functions absent from the claimed version, cited line numbers past end-of-file, and shipped proofs-of-concept that
  produce no crash. Retraction is propagating unevenly — GHSA still carried CVE-2026-51294 as an unreviewed record when
  this run checked on 2026-08-04, so scanner and SBOM pipelines are still being served records the CERTs have withdrawn.
discovered_at: "2026-08-04T04:46:00Z"
event_date: "2026-08-03"
run_id: 2026-08-04T0411Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, ai-abuse, supply-chain]
regions: [europe, global]
sectors: [public-sector, technology]
entities: [trend:llm-fabricated-cve-advisory-wave-2026-07]
techniques: []
affected_products: ["SQLite", "GitHub Advisory Database", "NIST National Vulnerability Database"]
cves: []
sources:
  - url: "https://advisories.ncsc.nl/2026/ncsc-2026-0268-1.txt"
    publisher: "NCSC-NL"
    date: "2026-08-03"
    role: primary
  - url: "https://research.jfrog.com/post/sqlite-critical-cves-or-llm-slops/"
    publisher: "JFrog Security Research"
    date: "2026-07-30"
    role: primary
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2604"
    publisher: "BSI CERT-Bund"
    date: "2026-08-03"
    role: corroborating
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2581"
    publisher: "BSI CERT-Bund"
    date: "2026-08-03"
    role: corroborating
  - url: "https://sqlite.org/forum/forumpost/34bdf3b9bd759d4d"
    publisher: "SQLite User Forum (Richard Hipp)"
    date: "2026-07-29"
    role: corroborating
  - url: "https://github.com/advisories/GHSA-4r76-5xh9-qj36"
    publisher: "GitHub Advisory Database"
    date: "2026-07-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "CVE is door een LLM gehallucineerd"
    publisher: "NCSC-NL"
  - quote: "A broader audit of 55 advisories published by the same GitHub account revealed that 54 were completely fabricated, while one contained a real bug wrapped in unverified CVE metadata."
    publisher: "JFrog Security Research"
  - quote: "Because no step in today's system actually requires a proof-of-concept or bug reproduction, a plausible-sounding fake advisory can slide right through the pipeline and end up in GHSA, downstream databases, and enterprise scanners."
    publisher: "JFrog Security Research"
verification: multi-source
sourcing_note: >
  The seven CVE identifiers named in this entry are recorded deliberately in the body and summary rather than in
  frontmatter `cves[]`, because they do not describe real vulnerabilities: populating a CVE record's type, vector and
  auth fields would assert a flaw class that does not exist. BSI scrubbed the CVE references from both withdrawn
  advisories, so their exact identifiers are not recoverable from the CSAF documents themselves.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Search your vulnerability-management, ticketing and dependency-scanning systems for CVE-2026-51294, CVE-2026-51296, CVE-2026-51297, CVE-2026-51300, CVE-2026-51302, CVE-2026-51303 and CVE-2026-51304 and close any SQLite finding raised from them — the advisories behind them have been withdrawn, but at least one was still live in GHSA on 2026-08-04, so an unattended pipeline may re-raise it."
migrated_from: null
---

Two European national CERTs pulled published SQLite advisories on 2026-08-03 for the same reason: the vulnerabilities are not real. NCSC-NL revised NCSC-2026-0268 to version 1.01, struck through its own description, and gave the reason in one line — "CVE is door een LLM gehallucineerd" ("the CVE was hallucinated by an LLM") — noting the retracted advisory had covered CVE-2026-51302 as affecting Red Hat's SQLite ([NCSC-NL, 2026-08-03](https://advisories.ncsc.nl/2026/ncsc-2026-0268-1.txt)). BSI CERT-Bund retitled WID-SEC-2026-2604 and WID-SEC-2026-2581 to "MELDUNG ZURÜCKGEZOGEN" ("advisory withdrawn") and removed their CVE references ([BSI CERT-Bund, 2026-08-03](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2604); [BSI CERT-Bund, 2026-08-03](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2581)).

The underlying work is a reproduction audit rather than an opinion. JFrog cloned `sqlite/sqlite` at the claimed tags, compiled the official releases in isolated containers, and fed each advisory's proof-of-concept SQL verbatim into the binaries under AddressSanitizer. Nothing reproduced, and the code references dissolve on inspection: CVE-2026-51302's claimed use-after-free runs through `exprComputeOperands()`, a function that did not exist in SQLite 3.41 and was added mid-2025, while the function it says does the freeing, `sqlite3ReleaseTempReg()`, only recycles register indices into an array and performs no heap deallocation at all. CVE-2026-51303 claims a fix in 3.51.3, but "a diff between 3.51.2 and 3.51.3 shows absolutely no changes to src/expr.c". CVE-2026-51296 cites lines 3555 and 3575 of `src/json.c` when, JFrog notes, "In version 3.41.0, src/json.c is only 2706 lines long". CVE-2026-51297 references `jsonBlobEdit()`, absent from the claimed release; CVE-2026-51304 gives a single-argument signature for a function that requires a database handle; CVE-2026-51300 cites a comment and a memory allocation as the vulnerable lines ([JFrog Security Research, 2026-07-30](https://research.jfrog.com/post/sqlite-critical-cves-or-llm-slops/)). SQLite's maintainer reported the same wave independently on 2026-07-29 ([SQLite User Forum, 2026-07-29](https://sqlite.org/forum/forumpost/34bdf3b9bd759d4d)).

The propagation path is the part that matters operationally, because every hop in it is one a defender's own tooling trusts. A newly created GitHub repository published the advisories; MITRE's public submission form performs no identity verification; NVD flagged them critical and CISA's Authorized Data Publisher enrichment agreed; Red Hat initially scored CVE-2026-51302 at 10.0 before downgrading it to 7.6; from there the records reached GHSA and the two national-CERT advisory streams that European public-sector vulnerability management actually reads. JFrog's diagnosis is structural: "Because no step in today's system actually requires a proof-of-concept or bug reproduction, a plausible-sounding fake advisory can slide right through the pipeline and end up in GHSA, downstream databases, and enterprise scanners." Retraction does not travel the same path in reverse — this run fetched GHSA-4r76-5xh9-qj36 — a use-after-free claim against SQLite 3.41 carrying CVE-2026-51294, from the same batch but not among the six JFrog reproduction-tested — and found it still live and marked "Unreviewed" on 2026-08-04, after both CERTs had withdrawn ([GitHub Advisory Database, 2026-07-30](https://github.com/advisories/GHSA-4r76-5xh9-qj36)).

**Defender takeaway:** a CVE's existence and its score are no longer sufficient triage evidence on their own, and JFrog's four red flags are cheap to apply before a critical-severity record consumes an emergency change window: no mention of the issue on the maintainer's own security page (SQLite publishes real ones at sqlite.org/cves.html), no commit hash or pull request in the reference fields, metadata contradictions such as empty CPE product definitions or version ranges that conflict with the narrative, and code references that do not resolve — functions absent from the claimed version, or line numbers past end-of-file. **Triage:** the discriminator against a real high-severity library disclosure is corroboration by the party that owns the code plus a resolvable fix commit; a genuine critical flaw in a widely embedded library arrives with a maintainer advisory and a diff, whereas this pattern arrives with a narrative, a pinned single-version CPE and a proof-of-concept nobody ran. JFrog names one further consequence for teams that have automated this layer: "An AI agent that encounters a fabricated CVE may attempt to locate the vulnerable function, generate a patch, or recommend changes based on code that does not even exist" — an automated remediation pipeline pointed at a fabricated record does not fail closed, it produces confident changes to code that was never broken.
