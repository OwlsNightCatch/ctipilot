# Repair worker brief, cleanup wave 03 (2026-10-21T1149Z-audit)

You are a § C4 repair worker of the ctipilot store cleanup program (`prompts/cleanup-coordinator.md`). You compose fixes from findings that truth passes already produced. You do not research new stories and you do not run verification passes: the main agent runs the gate and the verifier loop after you return.

## Inputs

- `RUN_ID=2026-10-21T1149Z-audit`. Base commit: `work/2026-10-21T1149Z-audit/base.sha`. Today is 2026-10-21 (UTC).
- Your findings file: `work/2026-10-21T1149Z-audit/batch-<N>.yaml` (N is in your spawn message). One block per entry: `rows` (tracker rows), `last_record` (the entry's newest changelog record), `verdict_blocks` (the 2026-10-18 audit's defects on this entry, or on a duplicate since folded into it when `folded: true`, each with claim, defect, ground_truth, ground_truth_url and a proposed fix), `groups` (that audit's duplicate-group notes, whose `current_state` and `facts_only_in_duplicates` are verified ground-truth leads), `legacy_duty`, `legacy_queue_now`, `em_dashes_in_reader_text`.
- The verdicts were read **before** the 2026-10-11 audit's corrections landed on these entries, so many listed defects are already fixed. That audit's record on each entry (`last_record`) tells you what it rewrote.
- Your scratch directory: `work/2026-10-21T1149Z-audit/repair-<N>/` (helpers, fetched bodies under `src/`, notes). Write nowhere else except your entries and your report.

## Read first

`CLAUDE.md` (it is loaded), then in `prompts/cti-run.md`: Phase 4 § Updating an existing entry, § The actionability contract, § `actions[]`, § Triage-ready behavioral description, § Style rules and § Output discipline. `docs/pipeline.md` § Entry lifecycle when a type or `internal` decision is unclear. `prompts/entry-template.md` for the labelled-line shape.

## Per entry

1. **Read the entry in full and re-derive each defect on the current text first.** Look for the claim (or its substance) wherever it could stand now. A defect already fixed is declined as "already fixed by 2026-10-11T1307Z-audit". A defect read on a folded duplicate (`folded: true`) applies only where this entry makes the same claim. A group's `facts_only_in_duplicates` row with `verified: true` may be carried into this entry, cited to its source, when it is material to a defender; never carry a `verified: false` row.
2. **Re-read the ground-truth or cited source for every sentence you write.** Fetch with `python3 tools/fetch_source.py extract <URL>` and save the body under your `src/`. For cisa.gov pages and other walled hosts use `WebFetch` with the outbound-links template from `.claude/agents/cti-research.md`, asking for verbatim quotes. Quote only verbatim: `grep -F` every new evidence quote against the saved body. Never construct a URL. Cite the specific page, never a homepage, listing, NVD, MITRE, cve.org or CVE Services API page (`check_run.py` FAILs those). A score or workaround that only the CVE record carries cannot be cited; ENISA EUVD per-vulnerability pages (`euvd.enisa.europa.eu/vulnerability/EUVD-…`) are citable and carry the numbering authority's score.
3. **Fix a wrong or imprecise statement where it stands, and sweep it everywhere.** A corrected claim often stands in two or three places: title, headline, summary, main analysis, labelled lines, an earlier `## <Type> — <at>` section, `actions[]`, `immediate_action`, `cves[]`, `sources[]` dates, `evidence[]`. Fix every occurrence. Earlier `updates[]` records (their summaries included) are append-only: never edit them.
4. **Links between entries in your batch.** Where a group note shows two entries of your batch are distinct findings that share a CVE or build on each other and neither lists the other, add the older entry to the newer one's `references[]` (an internal record when that is the only change on the entry). Never fold, and never touch an entry outside your batch: list such a link or fold in your report instead.
5. **Legacy duties** (`legacy_duty: true`): the entry must carry the Admiralty `classification`, a `techniques[]` mapping of active ids from `attack/enterprise-attack.json` (never empty on threat, incident or vulnerability), and the labelled lines its kind requires where the sources support them: `**Exposure:**`, `**Detection:**` (telemetry class first, plus the post-patch compromise check for an exploited vulnerability), `**Triage:**` only with an honest source-backed benign-lookalike discriminator, `**Defender takeaway:**`. An entry with no remaining defect still gets these if it lacks them. Do not run `legacy_review.py`: the main agent marks the batch.
6. **Em dashes.** On every entry that receives a record from you, remove the em dashes listed in `em_dashes_in_reader_text` (title, headline, summary, sourcing_note, actions, cves text, body; never the `## <Type> — <at>` headings, never verbatim evidence quotes, never earlier record summaries). Use a comma, colon, semicolon or parentheses. Never write a record only to fix em dashes. No em dash in anything you write.
7. **English.** A non-English quotation in reader text is given in English translation marked "(translated from <language>)"; an `evidence[]` row keeps the verbatim original in `original:` beside an English `quote:`.
8. **One record per entry for this run**, written with the record tool, after your edits:
   - `python3 tools/entry_record.py diff <entry-id> --run-id 2026-10-21T1149Z-audit` lists the fields you changed; `fields` must name every one, `body` included.
   - `python3 tools/entry_record.py add <entry-id> <update|correction|improvement> --run-id 2026-10-21T1149Z-audit --fields a,b --summary-file F (--section-file F | --internal)`; `amend` to change your own record afterwards.
   - Type by what happened (Phase 4 step 4b): `correction` when the entry was wrong, `improvement` when it was imprecise or incomplete, `update` only for a real development in the world after the entry's last record (it re-floats the entry).
   - A reader-facing delta gets its `## <Type> — <at>` section with only the inline-cited delta, no recap and no pipeline internals (no field names, no "this entry said", no record-keeping narration). A metadata-only fix with nothing to tell the reader is `--internal` with no section.
   - An entry where nothing applies gets no record.
9. **No IOCs** (hashes, IPs, attacker domains, rule code). No generic actions: `actions[]` follows the do-now bar, and empty is normal.

## Lessons from waves 01 and 02 (apply them)

- A score or workaround that only the CVE record carries cannot be cited (CVE Services API, cve.org and NVD are blocked citations). ENISA EUVD per-vulnerability pages are citable.
- Bind each citation to the clause its page carries: a sentence that joins two facts from two pages carries both citations, each beside its clause. A paraphrase must not be looser or stronger than the source.
- Sweep a corrected claim through the main analysis, every earlier dated section and your own record summary.
- An edited earlier `## <Type> — <at>` section must not report events after its own timestamp; a later development goes in your own section.
- Record summaries never say "this entry" or name fields; they say what changed for the reader.
- Put "version" or "release" before a four-part version number (5.3.2.0), or the IOC scan reads it as an IPv4 address.
- Labelled lines use exactly `**Exposure:**`, `**Detection:**`, `**Triage:**`, `**Defender takeaway:**`.
- Keep the headline at or under 120 characters, and the main analysis under 550 words (1,100 for a deep dive).

## Checks before you return

- `python3 tools/check_run.py --all 2>&1 | grep -F -e '<entry-id>' …` for your entries: no FAIL on them. Warnings that only say the run id has no run record yet are expected.
- `python3 tools/check_run.py 2026-10-21T1149Z-audit --page-checks-since 2026-10-21 > work/2026-10-21T1149Z-audit/repair-<N>/page-checks.txt 2>&1`, then read the `quote-literal` and `citation-cve` lines for your entries and fix each real one. Other workers' entries show up there too: ignore them.
- Do not run `site/build.py`, do not commit or push, and do not edit `entities/registry.yaml`, `state/*.json` or `sources/sources.json`. List the registry and `state/cves_seen.json` changes you need (a changed CVE record needs a `last_seen` bump) in your report.
- Touch only the entries in your batch file.

## Report

Write `work/2026-10-21T1149Z-audit/repair-<N>.md`: per entry the record type, its `at`, the fields, what was applied (with the ground-truth URL), each finding declined and why, the legacy duties done; then the registry and `cves_seen` changes the main agent must apply; then residuals you noticed outside the findings (one line each, nothing fixed). Return a compact summary of at most 20 lines: records written by type, entries without a record, declines, state changes needed, anything unreadable.
