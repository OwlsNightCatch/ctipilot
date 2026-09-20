**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-20T14:32:21Z · ended_at=2026-09-20T14:42:02Z · duration_seconds=581

## Verification report — 2026-09-20T1308Z-audit (iteration 3)

### Prior-iteration deltas walked first

All five iteration-2 remediations were re-checked against the sources this iteration fetched fresh:

1. **F10 (sixth CVE)** — confirmed correct on the entry's `cves[]`, title, headline, summary and `affected_products[]`: Oracle's own risk matrix (`work/2026-09-20T1308Z-audit/src_oracle_cspu.txt`) lists exactly six CVSS 10.0 rows with `Privs Req'd: None` / `User Interact: None` (CVE-2026-83021, -71133, -83099, -83059, -83020, -87230), matching the entry's six `cves[]` records exactly, no seventh missing. **But the fix was incomplete** — see F4 findings below: two frontmatter/body surfaces inside the same entry, and both the run record and the audit report, still say "five."
2. **F3 (NCSC-NL narrowing)** — confirmed correct. Fetched `https://advisories.ncsc.nl/2026/ncsc-2026-0372.html` (the resolved redirect target): the page carries a single `Prioriteit: Hoog` field and no dual likelihood/damage marker. The entry's narrowed sentence ("assigned it priority \"Hoog\", its high rating") matches exactly what the page shows.
3. **F4 (Gyazo duplicate clause)** — confirmed fixed. `entries/2026-09-18/gyazo-helpfeel-data-breach-image-upload-rce.md` sourcing_note now reads "under the victim-disclosure carve-out;" with no duplication.
4. **F4 (em-dash recount, low confidence)** — reproduced independently: `grep`-equivalent count over `entries/*/*.md` gives exactly **8,416 occurrences across 906 of 917 files**, matching the report's corrected figure exactly.
5. **F8 (CVE-database-API backlog recount, low confidence)** — partially reproduces. Entry count (12) and body-link count (15) reproduce exactly using the same patterns and logic as `check_run.py`'s `_BODY_LINK_RE` / `BLOCKED_SOURCE_PATTERNS`. The **`sources[]` figure does not reproduce**: precise counting of `sources[].url` matching `cveawg.mitre.org/api/cve/CVE-` or `services.nvd.nist.gov/rest/json/cves` across the 12 entries gives **16**, not 18 (see F4 below).

### Fresh cold pass

Read the new entry end to end, all ten updated entries plus their `git diff HEAD`, the run record (both verification-iteration blocks), and the full audit report. Fetched: Oracle's CSPU page, NCSC-NL's resolved advisory page, Cisco's FMC advisory (revision history), the Piyolog page (Japanese original-text substring check), Anthropic's September report (banned-accounts line), Sansec's write-up (100k figure), and all three Red Hat per-CVE pages plus The Hacker News's article for the Linux KEV correction. All ten changelog corrections/improvements check out against their cited sources — see detail in the deltas walk above and the findings below for the two residual gaps.

### Unsupported / hallucinated facts

**#1.** `entries/2026-09-20/oracle-september-2026-cspu-five-unauthenticated-cvss-10.md`, `actions[1]` (second action item): "Confirm that no Oracle Internet Directory LDAP listener, WebLogic web container or Access Manager authentication endpoint answers from outside its administrative network segment; **all five flaws** need no credential and no user interaction, so reachability is the whole of the exposure." The entry's own `cves[]` list carries **six** CVSS 10.0 records after the iteration-2 fix (title, headline, summary and the first action item all correctly say "six"). This action item was missed by that remediation and still says five, self-contradicting the frontmatter it sits in.

**#2.** `runs/2026-09-20/2026-09-20T1308Z-audit.md`, "## Verification and coverage notes" (published body): "One is published here: Oracle's September 2026 Critical Security Patch Update, **five unauthenticated CVSS 10.0 flaws** across WebLogic Server, Access Manager, Forms, Internet Directory and Platform Security for Java, released 2026-09-15 and relayed by NCSC-NL on 2026-09-16 **at its highest likelihood and damage rating**." Two separate defects in one sentence: (a) the flaw count omits CVE-2026-87230 (Hyperion Financial Management), which the entry itself now carries as the sixth CVSS 10.0 record; (b) "highest likelihood and damage rating" is the exact framing iteration 2's F3 established the cited NCSC-NL page does not support — I re-fetched `https://advisories.ncsc.nl/2026/ncsc-2026-0372.html` this iteration and it shows only a single field, "Prioriteit: Hoog", no likelihood/damage pairing. The entry's own body was corrected to match the page; this run-record sentence was not.

**#3.** `docs/audits/2026-09-20-quality-audit.md`, line 55 ("Findings — missing or incomplete coverage" → "Published: Oracle's September 2026 Critical Security Patch Update"): "`entries/2026-09-20/oracle-september-2026-cspu-five-unauthenticated-cvss-10` — **five flaws** at CVSS 3.1 10.0 ... CVE-2026-83021 ... CVE-2026-71133 ... CVE-2026-83099 ... CVE-2026-83059 ... CVE-2026-83020 (Platform Security for Java). Released 2026-09-15; NCSC-NL relayed the Fusion Middleware half as NCSC-2026-0372 on 2026-09-16, **rating it high for both likelihood and damage, the only one of its eleven Oracle advisories that day to do so**." This lists only five CVEs (omitting CVE-2026-87230/Hyperion) and repeats verbatim the "high for both likelihood and damage... only one of eleven" framing that iteration 2 established the cited page does not carry (confirmed again this iteration by re-fetching the page). The defect is internally inconsistent with the same report's own § 8 ("Iteration 2 found four more... The Oracle release carries a **sixth**... the entry now carries all six"), which states the corrected fact three sections later without the earlier passage being fixed to match.

**#4** (low confidence). `docs/audits/2026-09-20-quality-audit.md`, § 4 and recommendation 4: "**12 entries carrying 18 `sources[]` records and 15 body links**" (also repeated in the run record's iteration-2 finding remediation text). Reproducing this count with the same logic `check_run.py`'s `check_blocked_sources` uses (`sources[].url` matching `cveawg.mitre.org/api/cve/CVE-` or `services.nvd.nist.gov/rest/json/cves`, `_BODY_LINK_RE` for body links) over the current store gives: 12 entries (matches), 15 body links (matches exactly), but **16** `sources[]` records, not 18. Even a looser raw-text scan of the whole frontmatter block per entry (which would also catch `evidence[].source_url` fields) gives 17, still short of 18. Per-entry breakdown: cve-2026-46300(1), langflow-0769(1), teamcity-63077(1), zalktis-59109(1), cisco-nexus-20212(1), chrome-v8-85046(2), hpe-aruba(3), mikrotik(4), pixel-58704(1), unbound(1) = 16; jfrog and the 2026-08-10 coding-agent entry carry 0 `sources[]` hits (body-only). This is the same class of self-recount drift the report's own § 3 and § 8 already document twice this run (112/140/118 iteration-mismatch figure; the em-dash figure corrected across two iterations) — worth a third recount before publish.

### Needs more research

**#1** (low confidence). `entries/2026-09-20/oracle-september-2026-cspu-five-unauthenticated-cvss-10.md`, `cves[]` record for CVE-2026-87230: `affected: "Oracle Hyperion Financial Management, Security component, reachable over HTTP"` — omits the version string. Oracle's own risk matrix (`src_oracle_cspu.txt` line 620) gives the affected version as `11.2.26.0.000`, and every one of the other five `cves[]` records in this same entry includes its version string in the `affected` field (e.g. "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0..."). The first action item also punts on Hyperion specifically ("Hyperion Financial Management per the release matrix") while giving exact version numbers for all five other components. The version was available in the same document the rest of the sixth-CVE remediation used; this is a residual completeness gap in that same fix.

### Verdict

`NEEDS_FIXES (truth: 4, editorial: 1, advisory: 0)`

All ten changelog updates this run made to prior entries check out against their cited sources (Cisco advisory revision 2.6, Piyolog's verbatim Japanese sentence, Anthropic's actual "banned accounts associated with the actors" language, Sansec's "more than 100 thousand" floor, and all three Red Hat per-CVE pages plus The Hacker News's verbatim quote for the Linux KEV correction) — no residual defects found there. The residual is entirely in the incomplete propagation of iteration 2's own two Oracle-entry fixes (six CVEs; the narrowed NCSC-NL claim) into three other surfaces that describe the same finding: one frontmatter field inside the entry itself, the run record's published notes, and the audit report's own findings table — plus one recount that still doesn't reproduce, and one minor completeness gap on the newly-added sixth CVE record. No new coverage gaps identified; the audit's own completeness sweep (source-rotation fix, `oracle-cpu` cadence correction, seven backlog rows) reads sound and I found no additional in-window story it missed.

### Findings summary (machine-readable)
- code: F4
  category: hallucinated-fact
  section: entries/2026-09-20
  item: "Oracle September 2026 CSPU — six unauthenticated CVSS 10.0 flaws"
  url_or_quote: "actions[1]: \"...all five flaws need no credential and no user interaction, so reachability is the whole of the exposure.\""
  summary: "Entry's cves[] carries six CVSS 10.0 records after the iteration-2 fix (title/headline/summary/actions[0] all say six); this second action item was missed and still says five, self-contradicting the entry's own frontmatter."
- code: F4
  category: hallucinated-fact
  section: runs/2026-09-20
  item: "2026-09-20T1308Z-audit.md — Verification and coverage notes"
  url_or_quote: "\"...Oracle's September 2026 Critical Security Patch Update, five unauthenticated CVSS 10.0 flaws across WebLogic Server, Access Manager, Forms, Internet Directory and Platform Security for Java... relayed by NCSC-NL on 2026-09-16 at its highest likelihood and damage rating.\""
  summary: "Omits CVE-2026-87230 (Hyperion) that the entry itself now carries as a sixth CVSS 10.0 record, and repeats the 'highest likelihood and damage rating' framing iteration 2 already established https://advisories.ncsc.nl/2026/ncsc-2026-0372.html does not support (page shows a single 'Prioriteit: Hoog' field, re-confirmed this iteration)."
- code: F4
  category: hallucinated-fact
  section: docs/audits
  item: "2026-09-20-quality-audit.md line 55 — Published: Oracle's September 2026 Critical Security Patch Update"
  url_or_quote: "\"...five flaws at CVSS 3.1 10.0... [lists five CVEs, omits CVE-2026-87230]... rating it high for both likelihood and damage, the only one of its eleven Oracle advisories that day to do so.\""
  summary: "Lists only five CVEs and repeats the debunked dual likelihood/damage + 'one of eleven' claim; contradicts the entry (six CVEs, narrowed NCSC-NL claim) and contradicts the report's own section 8, which correctly says the entry now carries all six."
- code: F4
  category: hallucinated-fact
  section: docs/audits
  item: "2026-09-20-quality-audit.md systemic finding 4 / recommendation 4 — CVE-database-API backlog"
  url_or_quote: "\"12 entries carrying 18 sources[] records and 15 body links\""
  summary: "(low confidence) Reproducing with check_run.py's own BLOCKED_SOURCE_PATTERNS/_BODY_LINK_RE logic gives 12 entries and 15 body links (both match exactly) but 16 sources[] records, not 18; a looser raw-text scan of the whole frontmatter block (incl. evidence[].source_url) gives 17, still short of 18."
- code: F8
  category: needs-more-research
  section: entries/2026-09-20
  item: "Oracle September 2026 CSPU — CVE-2026-87230 (Hyperion Financial Management)"
  url_or_quote: "cves[]: affected: \"Oracle Hyperion Financial Management, Security component, reachable over HTTP\" (no version string)"
  summary: "(low confidence) Oracle's own risk matrix gives the affected version as 11.2.26.0.000 (src_oracle_cspu.txt line 620); every one of the entry's other five cves[] records includes its version string in `affected` and actions[0] gives exact versions for all components except Hyperion (\"per the release matrix\")."
