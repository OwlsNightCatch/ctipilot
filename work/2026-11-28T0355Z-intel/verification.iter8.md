**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-28T07:34:23Z · ended_at=2026-11-28T08:00:00Z · duration_seconds=1537

## Verification report — 2026-11-28T0355Z-intel (iteration 8)

Scope: six new entries, five updated entries (including the new Drupal `improvement` record), the run record, the claim ledger (208 claims, every claim covered; rows in `verification.iter8.claims.yaml`). Every cited URL was fetched live this pass (`extract` for 82 pages, `ncsc-csh post` for NCSC.ch hub posts 13196/13203/13242, raw `url --direct` for Kudelski tables, GitHub advisory sidebars, Hunt.io publication element, EFK dateline, Inside IT embedded JSON, BSI CSAF, GitHub PR API; `WebFetch` with the outbound-links template for cisa.gov alerts of 2026-11-24 and 2026-11-27 and for drupal.org SA-CORE-2026-017, -018 and PSA-2026-11-16, which answer the container with a client challenge). CISA KEV catalogue 2026.11.27 read through the bridge: CVE-2026-132165 (2026-11-24), CVE-2026-120705, CVE-2026-129243 and CVE-2026-136716 (2026-11-27) are listed; CVE-2026-129245, -129244 and -129242 are not.

Quote check: all 70 `evidence[]` quotes of the eleven entries were searched literally against the live bodies. Every non-English `original:` field (BACS/SRF German, SAP German x4, CERT-FR French) is a literal substring of its page; the English translations are faithful. English quotes that did not match literally were only the translated ones and the CISA sentence (markdown link syntax in the extract; confirmed verbatim by the WebFetch read) and the three drupal.org pages the container cannot read (SA-CORE-2026-017/-018 sentences confirmed by WebFetch; the two long PSA sentences were truncated by the WebFetch summariser and are unchanged by this run). Kudelski table-derived claims (weakness table, detection table, attack-in-numbers table) were read from the raw HTML and match the entry; the 'each forged account could read only its own customer's data' sentence matches section 7 of the post.

Update records: each of the five records carries this run's run_id; `updated_at` equals `at` for the three non-internal `update` records (BACS 04:41:50Z, GeoServer 04:50:22Z, nginx 04:51:23Z) and is untouched for the two `improvement` records (Mitel, Drupal); every record has its matching `## <Type> — <at>` section; the frontmatter diff of each entry is covered by the record's `fields`. Drupal improvement (new this iteration): the CISA alert of 2026-11-27 lists CVE-2026-136716 ("Drupal Core Improper Check for Unusual or Exceptional Conditions Vulnerability"), the added source/evidence quote are verbatim, `cisa-kev` on that CVE is right, the section states what the record summary states, and `updated_at` correctly does not move. Three drift items on the other four records are listed below as low-confidence findings.

Missed angles: none evidenced. Two further searches (late-November exploited-vulnerability items; Swiss cantonal/communal incidents of 2026-11-27) surfaced nothing newer or not already covered or dropped with reasons in the notes (Planzer, FIFA, US Air Force Cloud One, pCloud, BSI agentic-AI warning, Basel-Stadt, OTRS, Tomcat). Coverage looks complete for a post-Thanksgiving window.

Other observation, not a finding: `state/cves_seen.json` still carries `last_seen: 2026-11-26` for CVE-2026-136716 although the Drupal improvement record is dated 2026-11-28 (bookkeeping the audit sweeps).

### Citation does not support the claim
- #1 F3 (low confidence) — cacti-1-2-31-4http2root-guest-session-rce-zero-day, body sentence 1: "a chain its repository now calls 4HTTP2SHELL and watchTowr 4HTTP2ROOT ([ek0ms savi0r, 2026-11-26](https://github.com/ekomsSavior/Sad-Girls-0day-Club/tree/main/4http2shell))". The cited page says only "This is 4HTTP2SHELL." / "That is 4HTTP2SHELL."; 4HTTP2ROOT does not occur on it. watchTowr's name and the rename (BleepingComputer: 'previously 4HTTP2ROOT') are cited only in the next sentence. Add the two citations to the clause or drop "now".
- #2 F3 (low confidence) — same entry, body paragraph 3 and sources[]: "[Previdian tracker, 2026-11-28](https://previdian.com/VULN-2026-0010)" / `date: "2026-11-28"`. The page states "Published 26 Nov 2026" (counters "Updated 28 Nov 2026"; the live counters now read 248 attempts from 23 addresses, while the entry's as-read figures 216/21 are time-stamped in the sourcing_note). Two-day drift on a page with its own publication date; use 2026-11-26 or label "as read".

### Unsupported / hallucinated facts
- #3 F4 (low confidence) — mitel-openscape-4000-misa-2026-0013-unauth-cvss-10, summary and the 2026-11-28 record summary: "The CVE Program assigned CVE-2026-137724, CVE-2026-137721 and CVE-2026-137723 on 2026-11-27". No source gives an assignment date; the three ENISA records show only publication (EUVD-2026-137039 datePublished "Nov 27, 2026, 5:33:03 AM", assigner mitre), and the body and section say "published". Align to "published".

### Claims missing inline citation
- #4 F5 — sap-github-environment-intrusion-project-granite: "Project Granite" is in the title ("(Project Granite)"), the headline and the entity key, but the body never mentions it or cites it. Sources: BleepingComputer (via SPIEGEL) "a cyberattack it tracks under the code name 'Project Granite'"; Handelsblatt "Unter dem internen Namen 'Project Granite'"; heise "Intern führt SAP den Vorfall laut dem Nachrichtenmagazin unter dem Codenamen 'Project Granite'". SAP has not confirmed the name. One attributed, cited body sentence fixes it.
- #5 F5 (low confidence) — kudelski-offensive-ai-identity-lifecycle-insurer, Defender takeaway: "move a ZITADEL deployment on 4.0.0 through 4.20.4 to 4.20.5" has no citation in its paragraph (the ZITADEL advisory is cited in the preceding paragraph).

### Editorial / less-is-more flags (advisory)
- #6 F11 (low confidence) — GeoServer 2026-11-28 section: the descriptors of the two KEV CVEs ("unauthenticated ... WFS GetFeatureById stored query", "service-level ... prefixed service name") are cited to the CISA alert, which names only "XML Injection Vulnerability" and "Incorrect Authorization Vulnerability"; they come from the project advisories.
- #7 F11 (low confidence) — FreeRADIUS: "The page states no exploitation and no proof of concept for this flaw" (body and summary) reads as an assertion; the page is silent. Say "mentions no".
- #8 F11 (low confidence) — Kudelski Detection: "The sequence to alert on is ..." is the entry's own ordering while the sourcing_note says the post gives no ordered chain. May be left.
- #9 F11 (low confidence) — SAP: the Inside IT S/4HANA wording is only in the paywalled page's embedded JSON. May be left.
- #10 F11 (low confidence) — Drupal: the 2026-11-26 section keeps the present-tense "and the newer flaw is not on the list" that the new section says no longer holds; sourcing_note and main paragraph name only the 2026-11-24 listing.
- #11 F11 (low confidence) — Hunt.io: "Their presence establishes availability, not successful operation against any named target" follows the 'rest of the kit' list on the page, not the edge-exploit list; the entry's reading is supported elsewhere on the page.

### Verdict
NEEDS_FIXES (truth: 3, editorial: 2, advisory: 6)

### Findings summary (machine-readable)
See `work/2026-11-28T0355Z-intel/verification.iter8.findings.yaml` (11 records).
