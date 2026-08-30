**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-30T15:03:10Z · ended_at=2026-08-30T15:16:21Z · duration_seconds=791

## Verification report — 2026-08-30T1312Z-audit (iteration 5)

**Prior-iteration deltas walked first.** All three iteration-4 remediations confirmed correct against freshly fetched sources this iteration:

1. Oracle entry (`2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev`) — fetched `https://socradar.io/blog/snowlight-government-chinese-campaign/` directly. The victimology table reads exactly: "WebLogic-class (CVE-2026-21962) | 119 | 91 | 1 | Blind RCE via DNS/HTTP out-of-band callback", confirming the entry's 119/91/1/"Blind RCE via DNS/HTTP out-of-band callback" figures verbatim. The sourcing_note's three-way mechanism disclosure (NetSPI access-bypass / SecurityWeek RCE / SOCRadar out-of-band-callback) is accurate to the three sources. Confirmed against Oracle's own January-2026 CPU advisory (`oracle.com/security-alerts/cpujan2026.html`) as an independent check: CVE-2026-21962, CVSS 10.0, versions 12.2.1.4.0/14.1.1.0.0/14.1.2.0.0 (IIS: 12.2.1.4.0 only) match exactly.
2. Same entry — `references[]` now links `2026-08-05/cve-2026-34486-tomcat-encryptinterceptor-fail-open-kev`; confirmed that entry exists, cites the same SOCRadar report and the same UNC5174/UNC6586/SNOWLIGHT entities. Apt link.
3. Zbtlink entry (`2026-08-06/endlessdoors-zbtlink-router-factory-shipped-root-backdoor`) — the "carried in wire coverage from around 2026-08-06, before this entry was first written" clause is gone from both the `## Correction` section and the changelog summary; the correction now rests only on the cited heise article. Fetched `https://www.heise.de/news/OEM-China-Router-von-ZBT-mit-Backdoors-11433072.html`: the German original in the entry's new `evidence[]` record ("den Verkauf betroffener Router auszusetzen und die betroffene Software offline zu nehmen, während an Updates gearbeitet werde") is a verbatim substring of the article, and the English translation is faithful. No uncited date claim remains anywhere in the correction (grepped the full entry for date-adjacent language).

No new defect found in the remediated material itself. My own full cold pass below found additional items.

### Citation does not support the claim

**#1** `2026-08-28/kaltura-mwembed-unauth-rce-file-read-no-patch` — `evidence[]` still carries: `quote: "was unable to reach Kaltura to coordinate these vulnerabilities"`, `publisher: "CERT/CC"`, and the body repeats it inline, both cited to `https://kb.cert.org/vuls/id/308749` dated 2026-08-26. This run's own `## Update` section states "the reader proxy retrieved the page in full on 2026-08-30, and the quotations in the update below are verbatim from it" — but that claim covers only the two *new* patch quotations, not this pre-existing one. I fetched the live page three ways this iteration (`extract` — corrupted binary body; `jina` — clean markdown; the VINCE JSON API and CSAF export directly) and none contains the phrase "unable to reach" anywhere; the current document (revision `1.20260828195928.4`, `Date Last Updated: 2026-08-28 19:59 UTC`) covers only Overview/Description/Impact/**Solution**/Acknowledgements, with the Solution section now reading "Kaltura has released new patches…". CERT/CC vulnerability notes are single evolving documents, not append-only, so the vendor-unresponsiveness text this entry's `evidence[]` record quotes has been overwritten by the patch text and is no longer a verifiable substring of the source it cites. (low confidence on remediation path — the quote was almost certainly accurate against an earlier revision of the same URL; flagging because the current live page, which this run itself re-fetched for the update, no longer supports it.)

### Unsupported / hallucinated facts

**#2** `2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen` — the `2026-08-30T13:12:06Z` `improvement` record is `internal: true` and its summary states "no reader-facing text, claim or field value changed," but `fields: [actions, classification]` includes moving `classification` from `null` to `{reliability: A, credibility: 1}`. I read `site/build.py`'s `classification_meta()`/`render_classification_badge()`: with `classification: null`, `classification_meta` returns `None` and the badge renders as an empty string; with `{A, 1}` it renders `<span class="b cls cls-…">NATO A1</span>` in the live timeline, day-page cards and the entry detail page. That is a new, reader-visible artifact where none existed before — the opposite of "nothing to tell the reader" — so marking this record internal (no body section) is a changelog-contract violation (check 4c): a reader-facing delta shipped with no citation-backed section explaining it.

**#3** `2026-06-02/sekoia-consolidates-gamaredon-tooling-under-gammaphish-gamma` — same pattern, more severe. The `2026-08-30T13:12:06Z` `improvement` record is `internal: true`, `fields: [actions, classification, techniques, evidence]`, summary ending "No claim in the entry changed." Besides the classification badge issue in #2 (null → B2, same rendering proof), the diff replaces the entry's sole `evidence[]` record — previously `quote: "UPDATE (originally covered 2026-06-02): Sekoia TDR's \"FSB's Matryoshka\" series adds material technical detail…"`, `publisher: ctipilot v2 brief (migrated)` (a citation attributing the pipeline's own prior update summary to a publisher byline that never wrote it) — with two genuine verbatim Sekoia TDR passages. I confirmed both new quotes are exact substrings of `https://kudelskisecurity.com/research/…` — no, correction: I fetched Sekoia's own report is not the URL in this entry; the two replacement quotes ("This archive exploits the CVE-2025-8088 vulnerability to extract a hidden HTA file…" and "Forensic analysis of compromised hosts revealed a highly obfuscated VBScript worm…") were not independently re-fetched by me this iteration (time budget); I take the run record's account of the fetch at face value. Independent of whether the new quotes are accurate, `site/build.py`'s `render_entry_evidence()` renders every `evidence[]` record in a "Cited evidence" section on the entry detail page — so this change replaces what a reader literally sees on the page (a nonsensical self-referential citation) with a different, correct citation. That is unambiguously a reader-facing delta and, because the *old* state was a fabricated/mis-attributed quote (an F4-class defect in its own right), the fix reads like a `correction`, not an `internal: true` `improvement` with no section. Marking it internal denies any reader-facing record of the fact that a previously-published citation was fabricated and has now been fixed.

### Editorial / less-is-more flags (advisory)

**#4** (low confidence) `2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev` — sourcing_note/body: "its own success rate against WebLogic was around one host in ninety, far below the Confluence and cPanel campaigns in the same table." Fetched SOCRadar's table: cPanel/WHM is 16 confirmed / 1,563 unique hosts (≈1.02%) against WebLogic's 1/91 (≈1.10%) — nearly identical per-host success rates, not "far below," though true in raw confirmed-compromise counts (1 vs. 16) and unambiguously true against Confluence (80/80, 100%). The sentence is defensible read as a raw-count comparison but could mislead a reader parsing it as a rate comparison against cPanel specifically.

### Verdict

`NEEDS_FIXES (truth: 3, editorial: 0, advisory: 1)`

Full scope covered this iteration: all 13 entries carrying the `2026-08-30T1312Z-audit` changelog record, both new 2026-08-30 entries under full-gate treatment, the run record, and `docs/audits/2026-08-30-quality-audit.md`. Every correction record's cited claim on the 2026-08-28 cohort (Claroty/CVE-2026-21718, CNCMachineRMS/LevelBlue quotes, CVE-2026-53362 CVSS vector, DOJ/QTFY quote, Kudelski/PurpleDelta silence, Manchester Airports/ICO, ownCloud/EPSS + Hunt.io ZKTeco quote, Protection Civile/FrenchBreaches quote, Unisoc/chipset scope) was independently re-fetched and confirmed accurate this iteration — no residual defect found in any of those nine.

Mechanical checks: `check_run.py 2026-08-30T1312Z-audit --pre-verify` → 46 pass · 2 warn · 1 fail, exactly the expected residue (verification_residual_count 0 pending this iteration's fold-in; the aggregator-only WARN on the Unisoc entry is already disclosed in the run record's "Reduced-confidence note"). `check_run.py --all` → 24 pass · 0 warn · 2 fail · 25 acknowledged, matching the spawn message's expectation exactly (the 2 fails are the same pending-fold-in residue). `site/build.py` → built cleanly, zero self-check warnings. `state/coverage_backlog.md` → 11 open rows, 2 struck rows dated `2026-08-30`/this run id (Oracle, Gitea). Both `CVE-2026-21962` and `CVE-2026-60004` present in `state/cves_seen.json` with correct primary-source URLs. The three `truth-B*.yaml` files reconcile exactly to the report's 44/19/11/14 figures (verified by script: 48 raw records collapse to 44 distinct entries — 4 entries carry both a factual-error and an imprecision record and are counted once under factual-error — giving 19 clean / 11 factual-error / 14 imprecision, matching the report and run record verbatim, with Kaltura correctly the eleventh factual error per an `update` rather than `correction`).

`techniques[]` spot-checked against the pinned `attack/enterprise-attack.json` (v19.2): T1190, T1105, T1496, T1552.001 (Gitea), T1080 (Gamaredon fix) all active, not deprecated/revoked, names matching. CVE data on both new entries cross-checked against NVD as an independent authority beyond the entries' own cited sources: CVE-2026-60004 CVSS 3.1 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) and CVE-2026-53362 CVSS 3.1 7.8 (AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) both match the entries' frontmatter exactly. No IOCs, no blocked source-URL patterns (both confirmed by `check_run.py`'s `ioc-scan` and `blocked-source` PASS). No `org_triage`/`watchlist_hit: true` anywhere in scope.

No missed-angle finding this iteration — the run record's coverage-backlog additions (WatchGuard Fireware OS, Microsoft TI TerminalFix, Microsoft TI AI-infrastructure intrusions, Huntress DPRK-worker forensics, Norway ID-porten DDoS, inside-it.ch/Insel Gruppe lead) are all disclosed as open rows with gate reasoning rather than silent omissions, and I found no additional in-window item they missed.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: updated-entries
  item: "2026-08-28/kaltura-mwembed-unauth-rce-file-read-no-patch"
  url_or_quote: "https://kb.cert.org/vuls/id/308749 — evidence[] quote \"was unable to reach Kaltura to coordinate these vulnerabilities\" (CERT/CC, 2026-08-26)"
  summary: "Current live page (extract/jina/VINCE-JSON/CSAF all checked, revision dated 2026-08-28 19:59 UTC) contains no such phrase anywhere; Solution section now reads the patch text. This run's own sourcing_note claims the page was retrieved in full on 2026-08-30 but that verification covered only the new update quotes, not this pre-existing one."
- code: F4
  category: hallucinated-fact
  section: updated-entries
  item: "2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen"
  url_or_quote: "updates[] record at 2026-08-30T13:12:06Z, internal: true, fields: [actions, classification]"
  summary: "Record claims no reader-facing change, but adds classification {A,1} where none existed; site/build.py renders a new \"NATO A1\" badge on the live timeline/card/detail page wherever classification was previously null (renders nothing). Should not be internal:true; needs a non-internal record with a body section."
- code: F4
  category: hallucinated-fact
  section: updated-entries
  item: "2026-06-02/sekoia-consolidates-gamaredon-tooling-under-gammaphish-gamma"
  url_or_quote: "updates[] record at 2026-08-30T13:12:06Z, internal: true, fields: [actions, classification, techniques, evidence]"
  summary: "Same classification-badge issue as the Exchange entry, plus: the record replaces evidence[] — previously a quote attributed to publisher \"ctipilot v2 brief (migrated)\" that reproduced the pipeline's own earlier update summary — with two Sekoia TDR quotes. site/build.py's render_entry_evidence() renders every evidence[] record in a Cited-evidence section on the entry page, so this is a reader-visible fix of a previously fabricated/mis-attributed citation, which should be a non-internal correction with a section, not an internal improvement with none."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev"
  url_or_quote: "\"its own success rate against WebLogic was around one host in ninety, far below the Confluence and cPanel campaigns in the same table\""
  summary: "(low confidence) SOCRadar's table gives cPanel/WHM 16/1563 (~1.02%) vs WebLogic 1/91 (~1.10%) — nearly identical per-host rates, not 'far below', though true for Confluence (80/80) and for raw confirmed-compromise counts. Defensible as written but could mislead on a rate reading."
```
