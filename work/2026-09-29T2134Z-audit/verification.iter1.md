**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-09-29T23:10:40Z · ended_at=2026-09-29T23:31:42Z · duration_seconds=1262

## Verification report — 2026-09-29T2134Z-audit (iteration 1)

Scope read cold: the 15 updated entries (whole file + `git diff HEAD`), registry diff (`actor:dire-wolf`, `incident:metabase-sqli-zeroday-2026-08`), run record, audit report, `tools/fetch_source.py` diff and tests, `sources/sources.json` diff, `state/source_health.json`, `state/warning_acknowledgments.json`, `check_run.py 2026-09-29T2134Z-audit --pre-verify` (51 pass / 1 warn = the empty verification block, 0 fail), `check_run.py --all` (25 pass, 1 warn, 0 fail, 23 acknowledged), `test_fetch_source_pdf.py` (12/12). Cited pages were re-fetched this iteration (bridge `extract` / `url --direct` / `pdf` / `cisa-kev`, run cache under `work/2026-09-29T2134Z-audit/quote-bodies/`); cisa.gov alert text was corroborated through WebSearch snippets (WebFetch not used; the bridge 403s). MSRC per-CVE pages are JS shells and were not re-read (those entries' MSRC-cited text is unchanged by this run).

What held: every entry's changelog contract (one record with this run_id, matching section for non-internal records, `updated_at` moved only on the four `type: update` records, frontmatter `fields` cover every changed line), all new source URLs resolve and are specific, and the Check Point (sk1000117/118 `__NEXT_DATA__`), PaperCut, WatchGuard (per-CVE HTML incl. CWE list and CVSS vectors), CRA (ENISA FAQ, Commission page), Metabase/VenariX/Dodo/MediaNama, collusion.wiki, MovieReaper (Securelist), CNIL, ECA PDF, MAG, MikroTik KEV-typo and Unit 42 claims in the changed text match the fetched pages. Findings below are what did not hold.

### Unsupported / hallucinated facts

**#1 (F4) Audit report + run record + tool: "The WaterPlum advisory now reads cleanly, digits included" is false on disk.**
- Report line 56: "The reader now resolves each page's fonts and decodes each string with the font active at that point ... The WaterPlum advisory now reads cleanly, digits included." Run record `bridge_uses`: "pdf: the NPA/FBI WaterPlum joint advisory (ic3.gov CSA 260918), which exposed the merged-CMap decode defect fixed this run".
- Reproduced this iteration: `python3 tools/fetch_source.py pdf https://www.ic3.gov/CSA/2026/260918.pdf` prints `# pdf: 458084 chars from 13/27 streams — decode: byte-encoding` and starts `en-US1RUWK.RUHDQ:DWHU3OXPFRPPRQO\UHIHUUHGWRDV³&RQWDJLRXV`, the exact mojibake the report says was fixed (0 hits for "North Korean", 47 for "1RUWK"). The run's own cache `work/2026-09-29T2134Z-audit/quote-bodies/46fb61786f6ad34a.pdf.txt` (written 23:06:58, after `tools/fetch_source.py` was last edited at 23:02:10) is the same mojibake.
- Cause (checked by calling the functions): `_pdf_render_by_font` does decode the file (9 pages, "North Korean "WaterPlum," commonly referred to as “Contagious Interview,”…", 20,169 chars), but `pdf_text` keeps the per-font text only if `_pdf_prose_chars(by_font) >= 0.6 * _pdf_prose_chars(merged)`. The merged decode counts binary font streams that contain the bytes `BT`/`Tj` as text (458,923 chars, 164,715 "prose" chars) against 16,158 for the correct text, so the test fails and the fix never triggers on the file that motivated it. The 12 tests pass because none feeds `pdf_text` a real multi-stream file. For the ECA PDF the new and HEAD versions produce byte-identical output (equal, not better), so "equal or better on all ten" may hold but the headline claim does not.
- Fix: select per-font whenever the page tree resolved every page and the text is word-like (or compare against merged text restricted to streams reachable from page `/Contents`), add a regression test on a file with junk streams, re-run on the WaterPlum URL; otherwise strike the claim in the report and the run-record line.

**#2 (F4) 2026-07-31 Unit 42 — `sourcing_note` contradicts the corrected analysis and the source.**
- Entry: "Unit 42's own report contains an unresolved tension this entry does not resolve by inference: its narrative confines confirmed exploitation to the three NetScaler cases while its CVE table separately describes the Marimo activity as confirmed command execution. Both are reported as stated."
- Unit 42 (fetched): "Across all the exploitation attempts, both autonomous and manual, Unit 42 confirmed data exfiltration from three Citrix NetScaler targets (CVE-2026-3055) and command execution on 11 Marimo notebook endpoints (CVE-2026-39987)." The narrative confirms both; the "narrative confines … to three" reading came from the fabricated quote this run's correction removes, and the corrected title/summary/analysis now state both outcomes. Fix: rewrite the note (drop the "unresolved tension" sentence or restate it against what Unit 42 wrote, e.g. the "three successful exploitations" wording in the NetScaler subsection vs the 11 Marimo endpoints) and add `sourcing_note` to the record's `fields`.

**#3 (F4) 2026-08-09 Metabase — main analysis still says "a flaw with no CVE".**
- Body: "Detection is unusually well specified for a flaw with no CVE, because the vendor published the request sequence rather than indicators." The record summary says "The title, the summary and the main analysis no longer describe the flaw as having no CVE", and the same body's first paragraph now says CVE-2026-72898 was assigned. Fix: reword ("for a flaw disclosed before it had a CVE"); body is already in `fields`.

**#4 (F4) 2026-08-20 NetScaler AAA bypass (touched by this run) — summary contradicts the entry's own current state.**
- Summary ends "Rapid7 reports no observed exploitation as of 2026-08-19 and still recommends emergency patching." Frontmatter: `status: [exploited, cisa-kev, poc-public, patch-available]`, tag `actively-exploited`, body "sensor telemetry confirms exploitation attempts", KEV added 2026-09-09 (confirmed in the KEV feed fetched now). A reader of the summary alone concludes no exploitation. This is the top-of-entry drift the audit's own finding 3 names, missed on an entry the audit edited. Fix: `correction`/`improvement` moving the summary to PoC public, exploitation attempts observed, KEV 2026-09-09.

**#5 (F4) Audit report Recommendation 1 vs disk: WebFetch on cisa.gov is described as "not shipped, the operator's call", but it is shipped as agent guidance.**
- Report: "CLAUDE.md forbids `WebFetch` on CISA, so this is the operator's call". `sources/sources.json` (committed) notes for `cisa-news`, `cisa-advisories`, `cisa-directives` now say "use WebFetch (outbound-links template) first for the listing/feed and item pages" / "use WebFetch with the outbound-links template first" — a direct instruction against the CLAUDE.md hard rule ("NEVER WebFetch CISA / NCSC.ch directly"). The run record `fetch_failures[].mitigation_applied` says "none available in-container". Also `quote-triage.T1.yaml` records that T1 (a cti-verification agent) read the CISA alert "through WebFetch", which the run record does not disclose. Fix: reword the three notes to record the observation without instructing use (or take the operator decision first), and state the T1 WebFetch use in the report.

**#6 (F4, low confidence) Audit report / run record counts do not reconcile with disk.**
- "27 sources": the first content sweep in `state/source_health.json` has 162 relevant + 11 stale + 7 irrelevant + 5 shell + 5 unreadable = 190, i.e. 28 non-relevant (the 28th is the pre-existing demoted `threatpost`, never diagnosed); the report says "27 others" and lists 11+7+5+5 (=28).
- "Four of those page revisions carried news the entries had missed" but the coverage table lists five (PaperCut, Check Point, Metabase, WatchGuard, CRA); WatchGuard's re-rating is not among the four named.
- "Of the 14 PDFs the store cites": `grep` finds 15 distinct `.pdf` URLs in `entries/` (the ECA PDF this run added included).
- Run record `items_returned` T1=12, T2=10 vs 13 and 11 records in `quote-triage.T1.yaml` / `.T2.yaml`.
- Run record `completed: 23:06:24Z` precedes the Microsoft entry's changelog `at: 23:09:36Z` (restamp after the loop).

### Citation does not support the claim

**#7 (F3, low confidence) 2026-08-29 EU CRA — Commission citation date.** The new Improvement section cites "[European Commission, 2026-07-31]" for "ENISA has established the CRA Single Reporting Platform (SRP), operational as of 11 September 2026". The page's only dateline is "Last update 11 September 2026" (metadata date 2026-09-11); the sentence exists only in that revision. `sources[]` also still dates it 2026-07-31. Use 2026-09-11 for the newly cited text. Also `sourcing_note` still says ENISA's FAQ "states only that no API will be provided 'at this stage'" — that wording was replaced by the 09-17 revision this run cites ("at the initial release of the SRP"); the quote is no longer on the page.

**#8 (F3, low confidence) 2026-09-04 CNIL — clause cites a page that lacks the facts.** "France's CNIL imposed … against Hôpital privé de la Loire (HPL, Saint-Étienne, part of the Ramsay Santé group) … ([CNIL, 2026-09-03](https://www.cnil.fr/en/sanction-fine-hopital-prive-loire))". The CNIL page carries neither "Saint-Étienne" nor "Ramsay Santé" (0 hits); BleepingComputer (also cited on the entry) does. Pre-existing, not introduced by this run.

**#9 (F3, low confidence) 2026-08-29 PaperCut — Site Servers.** Update: "Site Servers and secondary/print servers need the same release as the primary Application Server ([PaperCut Software, 2026-09-10])". The bulletin FAQ says "Site Servers and secondary/print servers should be updated to a patched version, not just the primary Application Server." No "same release" statement.

### Quantifier without source

**#10 (F14) 2026-09-23 ECA NIS2 report — summary.** "NIS2 transposition is two years behind schedule in most member states." ECA text (PDF, fetched): "Member states had until October 2024 to transpose the NIS 2 Directive into national law, but only two met the deadline." Neither ECA nor heise says "two years behind" or that "most member states" remain behind. Fix: "only two member states met the October 2024 NIS2 transposition deadline". (Not touched by this run's correction but part of the entry it edited.)

### Claims missing inline citation

**#11 (F5, low confidence) `actor:dire-wolf` registry record.** "Double-extortion ransomware and data-extortion group active since May 2025, running a leak site … (Statista, Dodo Payments, August 2026)". The only source the run read (VenariX) says "a ransomware and data extortion threat actor" and gives no start date, leak site or incident dates for Statista. The background matches the public record (CSA Singapore alert AL-2025-082, fetched this iteration: "First identified in May 2025 … double extortion … data leak site") but nothing the run cited supports it, and that source does not say the VenariX actor is the same group. Add a source or trim to what VenariX states; drop "August 2026" for Statista.

**#12 (F5, low confidence) 2026-08-31 WatchGuard — detection sentence lost its support.** "Detection concepts: unexpected crashes or automatic respawns of the iked process are the observable symptom of a failed or exploratory attempt against either heap-overflow or type-confusion path". The earlier PSIRT text that said crash-and-respawn was replaced by this run's evidence edit; the current per-CVE pages say only "execute arbitrary code by sending specially crafted network traffic". No cited page now states the crash/respawn behaviour. Mark it as the pipeline's inference or drop it.

**#13 (F5, low confidence) 2026-08-28 MAG (pre-existing).** Paragraph 2: MAG "says only that it has 'informed and are working with the relevant authorities'" carries no citation (the phrase is on the media-centre statement, cited in the corrected 08-30 section), and "The group has suspended its Manage My Booking self-service portal" is uncited (Infosecurity Magazine carries it; the help page now links Manage Booking normally).

### Missed angles

**#14 (F10) `cves[].status` omits CISA KEV listings that the run's own sources carry — four touched entries.** KEV feed fetched now (`cisa-kev`, catalog 2026.09.29):
- `2026-08-29/papercut-ng-mf-tapestry-request-confusion-preauth-rce` (critical, `cves` in the record's `fields`): CVE-2026-81578 and CVE-2026-82078 both `dateAdded 2026-08-31`, dueDate 2026-09-14; status `[exploited, patch-available]`, no `cisa-kev` in status or tags, KEV never mentioned in the body.
- `2026-09-06/mikrotik-routeros-mikrotrick-ssh-auth-bypass-privesc-chain`: CVE-2026-67279 (the configuration-independent chain entry point) `dateAdded 2026-09-25`, KEV text "This vulnerability can be chained to achieve unauthenticated exploitation of CVE-2026-86060"; status `[exploited]`; no other entry carries it (`grep` finds it only here). The run edited this entry's KEV quote (typo) but not this newer KEV fact.
- `2026-07-14/microsoft-july-2026-patch-tuesday-two-exploited-zero-days`: CVE-2026-50522 `dateAdded 2026-07-22`; the run's own updated CISA quote says so and the internal record says the six CVEs are "already covered by this entry's later records", yet status is `[exploited, poc-public, patch-available]`.
- `2026-09-10/bluemoon-exploit-kit-…`: CVE-2026-85046 `dateAdded 2026-09-04`, status without `cisa-kev` (covered in the referenced 2026-09-04 entry; low).
Fix: changelog records (an `update` for MikroTik and PaperCut with the KEV date; `correction`/`improvement` for the status flags).

**#15 (F10) Wider page-check backfill left 44 warnings on 33 published entries, undisclosed.** `work/2026-09-29T2134Z-audit/page-checks-final.txt` (522 entries active since 2026-07-01, written 23:10:19) ends `4 pass · 44 warn · 0 fail`: 31 `quote-literal` WARNs on 27 entries (e.g. 2026-07-03 WatchGuard iked WGSA-2026-00023, whose page is now a multi-CVE roll-up; GhostLock, ShareFile, ESET UEFI, nginx, Kaltura, Cisco ASA/FTD, …) and 13 `citation-cve` WARNs on 7 entries (Joomla RSFiles, PraisonAI, WordPress wp2shell, GeoServer, SPIP, PTC Windchill, TrueConf). T1/T2 triaged only the 155-entry since-09-01 set. The report says the backfill "ran wider" and quotes the 633-quote figure (the 09-01 window; the wider run covered 1,825) but neither the report nor the run record dispositions these leads. Triage them or list them as residual, dated, in the report and run-record notes.

**#16 (F10, low confidence) Apple CVE-2026-86950 in KEV (added 2026-09-29, CoreGraphics out-of-bounds write, iOS/macOS/iPadOS, arbitrary code execution) has no entry.** Inside the audit window (KEV release 13:51Z); possibly left to the next intel fire. Query: "CVE-2026-86950 Apple CoreGraphics out-of-bounds write exploited iOS macOS update".

### Editorial / less-is-more flags (advisory)

- **#17 (F11) Truncated `sources.json` notes.** `cisa-news` ends "Latest items as of 2 (2026-09-29T2134Z-audit)"; `ibm-xforce` ends "Newest seen 2026-09-02 (Shodan/OT loca (…)"; `swarmcha-se` ends "Health-check suggestion: do not fire  (…)". The SR YAML has the full text (e.g. cisa-news "as of 2026-09-29: 23 Sep whitepaper …"). Restore.
- **#18 (F11) Record-keeping narration in reader-facing sections.** Unit 42 ("The title, the summary and the opening of the analysis above still described … They now name both"), MAG ("The analysis above no longer says …"), ECA ("the citations above now link directly"), MovieReaper and PaperCut ("the cited evidence above follow the revised report" names the frontmatter evidence field). Say what changed for the reader, not which field moved.
- **#19 (F11) Headline / action title not moved with the record.** PaperCut `headline` still "ships an emergency patch … and a second emergency release" (emergency patches replaced 10 Sept); Check Point `immediate_action.title` names Spark Firewall and Security Gateway only although the same record widens scope to every Management Server; Unit 42 `headline` names only the NetScaler outcome. PaperCut `immediate_action` says upgrade "every" v24/25/26 server now while the vendor says a Release 3 server "can schedule this upgrade normally" (the action does put Release 1/2 first).
- **#20 (F11, low confidence) Un-re-verifiable figures left in bodies after the same class was removed from evidence.** NetScaler body cites Previdian for "18 exploitation attempts total from 9 unique attacker IPs across 5 countries" (the page now shows a live counter, 62 attempts); Microsoft July body (07-17 section) quotes CISA's four-CVE sentence that the cited alert no longer carries (it lists six).
- **#21 (F11, low confidence) CNIL body rests on the French original.** "private-practice physicians" matches CNIL's French "médecins libéraux" (verified on cnil.fr/fr via search) but the cited English page now says "doctors not affiliated with the hospital"; say which reading is used or cite the French notice.

### Classification / action / triage

No F16, F17 or F18 findings (no `org_triage`, all 15 carry valid Admiralty blocks consistent with source nature, 19 actions across 15 entries within the do-now bar; `check_run` action-items PASS). No F1/F2 (all new URLs resolve; sources are specific). No F7 (all updates are the same finding as the entry they extend; no new entries). No F9 (the CRA NCSC-FI vs ENISA AR-cap contradiction is surfaced by the entry).

### Verdict

NEEDS_FIXES (truth: 10, editorial: 6, advisory: 5)

- Truth = #1 F4, #2 F4, #3 F4, #4 F4, #5 F4, #6 F4 (low), #7 F3 (low), #8 F3 (low), #9 F3 (low), #10 F14.
- Editorial = #11 F5 (low), #12 F5 (low), #13 F5 (low), #14 F10, #15 F10, #16 F10 (low).
- Advisory = #17–#21 F11.

### Findings summary (machine-readable)

See `work/2026-09-29T2134Z-audit/verification.iter1.findings.yaml`.
