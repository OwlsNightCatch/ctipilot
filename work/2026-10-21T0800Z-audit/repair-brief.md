# Repair worker brief, cleanup wave 02 (2026-10-21T0800Z-audit)

You are a § C4 repair worker of the ctipilot store cleanup program (`prompts/cleanup-coordinator.md`). You compose fixes from findings that truth passes already produced. You do not research new stories and you do not run verification passes: the main agent runs the gate and the verifier loop after you return.

## Inputs

- `RUN_ID=2026-10-21T0800Z-audit`. Base commit: `work/2026-10-21T0800Z-audit/base.sha`.
- Your findings file: `work/2026-10-21T0800Z-audit/batch-<N>.yaml` (N is in your spawn message). One block per entry: `rows` (tracker rows), `findings` (W1-B truth-pass defects with claim, defect, ground_truth, ground_truth_url and a proposed fix; W1-C clean verdicts; W1-E carried residuals and advisories with their earlier disposition; W1-F pointers to unverified draft hunks), `legacy_duty`, `legacy_queue_now`, `em_dashes_in_reader_text`.
- W1-F drafts: `work/cleanup/wave-02/W1-F-reference-hunks.md`, one section per entry. They are unverified drafts from the reference branch: re-derive each change on the current text, re-verify it against its source, and fold it into your one record. Never copy a draft's record or its `at`.
- Your scratch directory: `work/2026-10-21T0800Z-audit/repair-<N>/` (helpers, fetched bodies under `src/`, notes). Write nowhere else except your entries and your report.

## Read first

`CLAUDE.md` (it is loaded), then in `prompts/cti-run.md`: Phase 4 § Updating an existing entry, § The actionability contract, § `actions[]`, § Triage-ready behavioral description, § Style rules and § Output discipline. `docs/pipeline.md` § Entry lifecycle when a type or `internal` decision is unclear. `prompts/entry-template.md` for the labelled-line shape.

## Per entry

1. **Read the entry in full and check the current text first.** The 2026-10-18 verdicts were read before the 2026-10-11 audit's records landed; in wave 01 that audit had already fixed part of the defects on most entries. A defect already fixed is declined as "already fixed by <run-id>".
2. **Re-read the ground-truth or cited source for every sentence you write.** Fetch with `python3 tools/fetch_source.py extract <URL>` and save the body under your `src/`. For cisa.gov pages and other walled hosts use `WebFetch` with the outbound-links template from `.claude/agents/cti-research.md`, asking for verbatim quotes. Quote only verbatim: `grep -F` every new evidence quote against the saved body. Never construct a URL. Cite the specific page, never a homepage, listing, NVD, MITRE, cve.org or CVE Services API page (`check_run.py` FAILs those). A score or workaround that only the CVE record carries cannot be cited; ENISA EUVD per-vulnerability pages (`euvd.enisa.europa.eu/vulnerability/EUVD-…`) are citable and carry the numbering authority's score.
3. **Fix a wrong or imprecise statement where it stands, and sweep it everywhere.** A corrected claim often stands in two or three places: title, headline, summary, main analysis, labelled lines, an earlier `## <Type> — <at>` section, `actions[]`, `immediate_action`, `cves[]`, `sources[]` dates, `evidence[]`. Fix every occurrence. Earlier `updates[]` records (their summaries included) are append-only: never edit them.
4. **Carried W1-E items.** An item declined earlier as "left for the next record on the entry" is applied now when the source supports the fix. An item declined on principle stays declined unless you find a reader-facing error: earlier records are append-only, removing an entry is outside the lifecycle, sector and relevance framing is the profile's call. Record your decision with its reason either way.
5. **Legacy duties** (`legacy_duty: true`): the entry must carry the Admiralty `classification`, a `techniques[]` mapping of active ids from `attack/enterprise-attack.json` (never empty on threat, incident or vulnerability), and the labelled lines its kind requires where the sources support them: `**Exposure:**`, `**Detection:**` (telemetry class first, plus the post-patch compromise check for an exploited vulnerability), `**Triage:**` only with an honest source-backed benign-lookalike discriminator, `**Defender takeaway:**`. A W1-C entry with a clean verdict still gets these if it lacks them. Do not run `legacy_review.py`: the main agent marks the batch.
6. **Em dashes.** On every entry that receives a record from you, remove the em dashes listed in `em_dashes_in_reader_text` (title, headline, summary, sourcing_note, actions, cves text, body; never the `## <Type> — <at>` headings, never verbatim evidence quotes, never earlier record summaries). Use a comma, colon, semicolon or parentheses. Never write a record only to fix em dashes. No em dash in anything you write.
7. **English.** A non-English quotation in reader text is given in English translation marked "(translated from <language>)"; an `evidence[]` row keeps the verbatim original in `original:` beside an English `quote:`.
8. **One record per entry for this run**, written with the record tool, after your edits:
   - `python3 tools/entry_record.py diff <entry-id> --run-id 2026-10-21T0800Z-audit` lists the fields you changed; `fields` must name every one, `body` included.
   - `python3 tools/entry_record.py add <entry-id> <update|correction|improvement> --run-id 2026-10-21T0800Z-audit --fields a,b --summary-file F (--section-file F | --internal)`; `amend` to change your own record afterwards.
   - Type by what happened (Phase 4 step 4b): `correction` when the entry was wrong, `improvement` when it was imprecise or incomplete, `update` only for a real development in the world after the entry's last record (it re-floats the entry).
   - A reader-facing delta gets its `## <Type> — <at>` section with only the inline-cited delta, no recap and no pipeline internals (no field names, no "this entry said", no record-keeping narration). A metadata-only fix with nothing to tell the reader is `--internal` with no section.
   - An entry where nothing applies gets no record.
9. **No IOCs** (hashes, IPs, attacker domains, rule code). No generic actions: `actions[]` follows the do-now bar, and empty is normal.

## Checks before you return

- `python3 tools/check_run.py --all 2>&1 | grep -F -e '<entry-id>' …` for your entries: no FAIL on them. Warnings that only say the run id has no run record yet are expected.
- `python3 tools/check_run.py 2026-10-21T0800Z-audit --page-checks-since 2026-10-21 > work/2026-10-21T0800Z-audit/repair-<N>/page-checks.txt 2>&1`, then read the `quote-literal` and `citation-cve` lines for your entries and fix each real one. Other workers' entries show up there too: ignore them.
- Do not run `site/build.py`, do not commit or push, and do not edit `entities/registry.yaml`, `state/*.json` or `sources/sources.json`. List the registry and `state/cves_seen.json` changes you need (a changed CVE record needs a `last_seen` bump) in your report.
- Touch only the entries in your batch file.

## Report

Write `work/2026-10-21T0800Z-audit/repair-<N>.md`: per entry the record type, its `at`, the fields, what was applied (with the ground-truth URL), each finding declined and why, the legacy duties done; then the registry and `cves_seen` changes the main agent must apply; then residuals you noticed outside the findings (one line each, nothing fixed). Return a compact summary of at most 20 lines: records written by type, entries without a record, declines, state changes needed, anything unreadable.
