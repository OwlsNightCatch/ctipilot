# CTI Weekly Quality Audit — Master Prompt

> **Prompt version:** v3.34 — bump in `prompts/CHANGELOG.md` whenever you edit this file. Carry the version through to the run record (`prompt_version` in `runs/<date>/<run-id>.md`). Print this banner at run start.
>
> **Runtime:** Claude Code routine on Anthropic-managed cloud infrastructure, fired **once per week** (operator-chosen slot — recommended Sunday, after the weekly strategic run; the prompt is schedule-agnostic and self-healing). Same delegation model as the intel run: the main agent owns diffing, root-causing, fixing and publishing; bulk source fetching runs in sub-agents.
>
> **Output:** one audit report `docs/audits/<YYYY-MM-DD>-weekly-quality-audit.md`, exactly one run record `runs/<YYYY-MM-DD>/<run-id>.md` (`run_id = <date>T<HHMM>Z-audit`, `kind: audit` — first-class in `RUN_KINDS` since v3.24; precedent `runs/2026-07-11/2026-07-11T1435Z-audit.md`), zero or more audit-recovered entries, and shipped fixes. **A clean audit is a healthy outcome** — the report then records what was verified clean, not manufactured findings.

**This prompt builds on [`prompts/cti-run.md`](cti-run.md) — `Read` that file in full before Phase 0.** The intel-run prompt defines the shared machinery once (anti-crash guards, prime directives PD-1…PD-13, entry composition discipline, state lifecycle, mechanical gate, verification loop, publishing chain); this file defines only what the audit does differently. Where the two disagree, this file wins for the audit lens and `cti-run.md` wins for machinery.

**Mission — institutionalized continuous improvement.** The scheduled pipeline optimizes for latency inside each window; this run audits the pipeline itself over the trailing week, the way the operator-directed full-store audit of 2026-07-11 did ([`docs/audits/2026-07-11-intelligence-quality-audit.md`](../docs/audits/2026-07-11-intelligence-quality-audit.md) — the method template). Two questions, weighted equally per the sound-AND-complete doctrine:

1. **Soundness** — is everything published in the window true, precisely sourced, correctly classified/prioritized/mapped, and relevant? Re-verify against primary sources, not against the entries' own citations alone.
2. **Completeness** — did the window miss anything a reader relying on ctipilot.ch alone needed? Re-research the window independently and diff against the store.

Plus the meta-question neither scheduled run asks: **is the machinery drifting** — runaway runs, dark-but-green sources, discipline decay (`actions[]`, priority, classification), fixes from the previous audit that didn't take? Every confirmed failure is root-caused to a specific mechanism and the fix ships in this run (or becomes an explicit operator recommendation when it exceeds § META authority). Be very critical — question everything, fetch ground truth, trust no claim because it is in the store. But never performative: a defect-free component is reported clean.

**The audit is also the pipeline's weekly cleanup (v3.28).** It leaves the whole repo at **zero warnings**: every `check_run.py --all` WARN and every `site/build.py` self-check warning is either fixed at its root cause this fire or — settled, immutable history only — acknowledged with a reason in `state/warning_acknowledgments.json` (Phase 3 item 8 / Phase 4 fix class). Beyond warnings, the audit fixes everything fixable it touches along the way: renderer defects, stale tool output, drifted docs, dead recipes — small repairs ship in the audit commit rather than being deferred, provided they stay inside § META authority and never weaken a hard invariant. The operator expectation is a repo that is *perfectly clean* after every audit, not merely audited.

---

## CRITICAL: this run must produce a committed run record AND the audit report

Identical invariant to the intel run: **every fire ends with a written, committed, pushed run record.** The audit report is the second mandatory artifact — an audit whose findings die in context improved nothing. All ten anti-crash guards from `prompts/cti-run.md` § CRITICAL apply verbatim, with these audit readings:

- **Time-boxing:** the retrospective truth passes and coverage re-sweeps are research-class workloads (dozens of primary fetches each) — they carry the **45-min research hard cap**; the Phase 5.7 verification loop over this run's own output keeps its 30-min cap. Abandoned sub-agents are logged as audit coverage gaps, never waited on.
- **Wall-clock watchdog (guard #10), audit priority order:** past ~3 h stop widening and land the run — truth passes > coverage re-sweeps > systemic review > calibration. The report and record ship from whatever completed, with the cut explicitly recorded. A partial audit that publishes beats a complete one that doesn't.
- **No main-agent fetching while Phase 1/2 sub-agents run** (guard #9). Main-agent exceptions after they return: bounded single-URL spot-checks in Phase 3/4 and the Phase 5.7/7 exceptions from `cti-run.md`.

---

## Phase 0 — Preflight (sequential, ~2 min)

```bash
STARTED=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
RUN_DATE=$(date -u +%F)
RUN_ID="${RUN_DATE}T$(date -u +%H%M)Z-audit"
mkdir -p "work/${RUN_ID}" "runs/${RUN_DATE}"
echo "$STARTED" | tee "work/${RUN_ID}/main.started_at"
echo "$RUN_ID"  | tee "work/${RUN_ID}/run_id"
: > "work/${RUN_ID}/url-liveness.tsv"

git fetch origin main
# Most recent prior audit record — the window anchor.
LAST_AUDIT=$(git ls-tree -r --name-only origin/main -- runs/ | grep -- '-audit\.md$' | sort | tail -1)

# Dedup context for any audit-recovered entries.
python3 tools/build_prior_coverage.py "$RUN_ID" 14
python3 tools/run_summary.py --out "work/${RUN_ID}/state-summary.json"
python3 tools/check_run.py --all > "work/${RUN_ID}/check-all.txt" 2>&1 || true
python3 tools/attack_data.py --check >> "work/${RUN_ID}/check-all.txt" 2>&1 || true
```

Then, in order:

1. **Window.** `AUDIT_START` = the `started` timestamp of `LAST_AUDIT` (`git show origin/main:$LAST_AUDIT`); no prior audit → 7 days back. Cap the window at 21 days — beyond it, audit the most recent 21 and record the truncation as an operator item. The window covers entries **and** run records with `started`/`discovered_at` in `[AUDIT_START, now]`.
2. **Duplicate-audit guard.** Gap since `LAST_AUDIT` < 72 h → stop and report `duplicate-audit` (mirror of the weekly's `duplicate-week` guard), unless this fire is an explicit interactive operator directive.
3. **Carry-forward.** `Read` the most recent audit report(s) under `docs/audits/` and extract (a) **open watch items** — each gets a re-check duty this fire; (b) **fixes shipped last audit** — each gets an effectiveness check in Phase 3 (a fix that didn't change behavior is a finding). **Operator closures are final (v3.27):** a watch item the operator has explicitly closed — an operator-response addendum in an audit report, or a dated operator note in `.claude/memory/` — is CLOSED, gets no re-check duty, and is never re-opened by an audit; if genuinely new information on the underlying story surfaces later, it flows through the normal intel runs (as an `update_of` where an entry exists), not through audit tracking.
4. **Monthly calibration duty (recommendation 3 of the 2026-07-11 audit).** Search `docs/audits/` on `origin/main` for a report dated in the **current calendar month** containing a `## Priority calibration` heading. None found → this fire owns Phase 3b. This puts the review at monthly cadence on a weekly schedule, self-healing across missed fires.
5. **Inventory.** Enumerate the window's entry files and run records; partition entries into truth-pass batches of **≤20 entries each** (batch = one Phase 1 sub-agent). Read `entities/registry.yaml` + `site/taxonomy.yaml`. Persist the plan to `work/<run-id>/audit-plan.json`; initialise `TodoWrite`.

---

## Phase 1 — Retrospective truth verification (sub-agents, parallel; 45-min cap each)

One cold-reader pass per batch, spawned in a single message — `subagent_type: cti-verification` on odd-numbered batches, `cti-verification-alt` on even (model diversity across the audit, same rationale as the Phase 5.7 rotation). These are **retrospective audit passes, not Phase 5.7 iterations** — record them under the run record's `sub_agents:` telemetry with the usual `**Model:**` / `**Timestamps:**` capture; Phase 5.7 still runs separately on this run's own output.

Spawn envelope: run id; the explicit entry-file list for the batch; the audit mandate ("assume nothing; fetch ground truth"); ledger path. Per entry, the pass fetches the primary sources and checks:

- every `cves[]` id and CVSS against the **per-CVE authority** (vendor PSIRT / per-CVE advisory / discloser's per-vulnerability page — a roundup, even the same publisher's, is never sufficient; the v3.21 provenance rule, applied retroactively);
- KEV/exploitation claims, version boundaries, affected/patched products, victim statements, attribution claims, and every `evidence[]` quote verbatim against its cited URL;
- every `techniques[]` id **active in the pinned `attack/enterprise-attack.json`** — mechanical ground truth, never memory (the 07-11 audit had a verifier mis-assert a revoked id was active);
- `classification` consistency with the sourcing actually present; `closed_sources` tracing to a readable drop file; no IOCs; frontmatter⇔body agreement.

Return: a findings YAML to `work/<run-id>/truth-<batch>.yaml` — per entry `{entry, verdict: clean|imprecision|factual-error, defect, ground_truth, ground_truth_url}`. Clean entries are listed as clean (the audit's headline number is `clean/total`).

## Phase 2 — Independent coverage re-sweeps (sub-agents, parallel with Phase 1; 45-min cap each)

Spawn `subagent_type: cti-research`, same spawn-envelope contract as the intel run's Phase 1 (window = the audit window as `window_hours`, source slice, dedup paths incl. `entities/registry.yaml`, ISO date), one per gap domain:

| Sub-agent | Domain |
|---|---|
| **G1 — Vulnerabilities & exploitation** | KEV additions, national-CERT advisories, vendor PSIRTs, exploitation reporting across the window. |
| **G2 — Incidents & ransomware** | Home-region / coverage-focus priority (the composed org profile in `cti-run.md` governs); victim disclosures, regulator filings, leak-site claims needing corroboration. |
| **G3 — Threat research & APT** | Vendor **research-blog listing sweeps** per publisher across the window dates — the discovery path that does not route through CVE/KEV channels and caused both misses found on 2026-07-11. |

Their job is to re-research the window **as if for the first time** and return everything that would clear PD-11, with discovery traces — the main agent diffs returns against the store (an item already covered, incl. as `update_of`, is a match, not a gap). G2 additionally re-checks every **open watch item** carried forward from Phase 0 step 3 (e.g. corroboration hunts on single-source leak-site claims).

## Phase 3 — Systemic & operational review (main context, local files, ~15 min)

Over the window's run records, `work/` artifacts and state — no fetching except bounded single-URL recipe spot-checks after Phase 1/2 return:

1. **Telemetry:** wall-clock durations (>3 h runaway), `gap_hours` anomalies and overtaken-run races, verification iteration counts / residuals / dropped-entry rates, stalled-sub-agent abandonments. Zero-entry runs: read their notes — defensible quiet window or filter failure? **Scheduler cadence is operator-owned and intentionally variable (operator decision 2026-07-18):** the operator tunes the fire schedule at will — more fires, fewer fires, different slots — and the pipeline is built to work off the gap to the last run (PD-7). A changed cadence is therefore NOT a finding and NOT an operator recommendation; what the audit checks is the *mechanism* — that every fire's gap-derived window self-healed across the change with no coverage hole between runs. Only a self-heal failure or an actual coverage hole is a finding; the latency profile of a lower cadence may be stated as context in a miss's root cause, never flagged as a defect. (A gap with *no run record at all* on a previously firing schedule is still worth surfacing as possible scheduler outage — that is an availability signal, not a cadence judgment.)
2. **Publish follow-through:** any v3.14+ record with missing/stale `publish_status` (the Phase 7 amendment that never landed).
3. **Source health — reachability ≠ readability:** essential/tier-1 sources green in `state/source_health.json` but contributing zero items across the whole window are suspects for the dark-but-green class (ncsc-uk, 07-11); spot-check the fetch recipe of each suspect and record a working recipe in `sources/sources.json` notes when found.
4. **Reader-pool health (last-resort transport — a dead pool is normal, not an incident; v3.33):** run `python3 tools/fetch_source.py jina-usage`. The jina reader is the fetch ladder's LAST rung, behind the trafilatura capture layer (`extract <URL>`), and the operator refills its keys sparsely and deliberately — so a dead or low pool is an expected steady state the pipeline must work through, never by itself an operator recommendation and NEVER a notification. What the audit checks instead: (a) that fires kept reading primaries through a dead pool via the direct rungs (a run record claiming a source was unreachable when `extract` would have read it is a finding); (b) that reader spend outside `fetch_method: jina`-pinned hosts stayed near zero (rising spend means the trafilatura-first discipline is eroding). Note the pool state in the report's telemetry section as context only.
5. **Discipline drift:** `actions[]` distribution against the v3.19 do-now bar (empty-is-normal shape restored?); priority mix of the window; classification codes present and plausible; behavior-kind `techniques[]` density; `update_of` discipline on same-topic entries.
6. **Gate & pin:** the Phase 0 `check_run.py --all` and `attack_data.py --check` results — store-wide FAILs and unmentioned pin drift are audit findings.
7. **Fix effectiveness:** for each fix the previous audit shipped, confirm the behavior actually changed in this window's output; a fix that didn't take is a finding with its own root cause.
8. **Warning sweep to zero (v3.28):** collect every WARN from the Phase 0 `check-all.txt` and every `SELF-CHECK WARNING` from a fresh `python3 site/build.py`. Each one is a mandatory Phase 4 work item — fix the root cause (tool, prompt, renderer, source record, state) whenever a fix exists; only a warning whose subject is settled immutable history (a published run record's telemetry fact, an era-correct recorded waiver) may instead be acknowledged in `state/warning_acknowledgments.json`. The audit does not publish until `check_run.py --all` ends **0 warn · 0 fail** (acknowledged entries report separately) and `site/build.py` emits no self-check warnings. Review existing ledger entries while there: an acknowledgment whose match no longer silences anything (the underlying check changed, or the warning no longer fires) is deleted — the ledger never accumulates dead rows.

## Phase 3b — Monthly priority-calibration review (only when Phase 0 step 4 assigned it)

Institutionalizes recommendation 3 of the 2026-07-11 audit: *"the `high` share (37 %) is stable but on the generous side; one pass a month over the priority distribution against F-category drift keeps the notification channel honest."*

1. Compute the `priority` distribution store-wide and over the trailing calendar month (grep `entries/**` frontmatter; the 2026-07 store baseline: 15 critical / 335 high / 564 notable / 1 routine — `high` ≈ 37 %).
2. Collect the priority-calibration findings (**F16**) from the month's run records' `verification.iterations[].findings` — the drift signal the verifier loop already produces.
3. Judge against the bars, which are fixed references the review never tunes: `critical` clears stop-reading-and-act-now (rare because the bar is extreme, never because a number caps it — a long critical-free streak under real exploitation pressure is itself a signal to check); `high` genuinely TL;DR-worthy (every `high` headline tops the rendered 24 h window — the generous direction burns the notification channel); `notable` not absorbing items that plainly clear a higher bar (under-alerting is the same defect in reverse).
4. Ship the outcome as a `## Priority calibration` section in the audit report — distribution table, month-over-month movement, F16 summary, verdict. Only when drift is confirmed against **concrete mis-prioritized entries** does a calibration edit to `prompts/cti-run.md` priority guidance ship (versioning rule applies); a judgment call the audit shouldn't own alone becomes an operator recommendation.

---

## Phase 4 — Root-cause & fix (main context)

Every confirmed defect is root-caused to the specific mechanism that let it through (which phase, rule, tool, or missing duty), then fixed by class:

- **Factual metadata errors that poison machine surfaces** — wrong/unresolvable CVE id, wrong CVSS in `cves[]`, dead ATT&CK id, wrong registry key: repair **in place** under the immutability-exception discipline, and ONLY this class. Log each repair in `.claude/memory/entry-immutability-exceptions.md` (entry, field, old→new, ground-truth source), re-sync affected state (`state/cves_seen.json`), and disclose in the report and run record. Precedent and scope: the 2026-07-11 audit's three repairs.
- **Content-level errors, corrections, new information:** a NEW entry with `update_of: <original id>` — never an in-place rewrite. Entry immutability stays a hard invariant; the exception class above is its only carve-out.
- **Missed coverage that still clears PD-11 today:** compose and publish the recovered entry through the **full normal gates** (Phase 4 composition rules, dedup, `check_run.py`, verifier loop), with a provenance line naming this audit. Borderline items that correctly fail PD-11 are documented as correctly-droppable — that documentation is what makes the completeness judgment auditable.
- **Systemic causes:** fix prompts / tools / sources / agent definitions / memory under § META authority — the versioning rule applies in full (banner bump + CHANGELOG entry in the same commit; verifier definitions regenerate in lockstep). What exceeds authority (scheduler config, org-profile values, hosting) becomes a numbered operator recommendation.
- **Single-source claims touching the constituency** that fail corroboration: not published, recorded as **watch items** with what would resolve them — the next audit re-checks.
- **Warnings on settled immutable history (v3.28):** a WARN whose subject cannot change without falsifying the record — a published run record's runaway `duration_seconds`, an era-correct recorded confirmation waiver — is acknowledged in `state/warning_acknowledgments.json`: `check` label, `match` pinned to the specific run id/subject, `reason`, `acknowledged_at`. This is a reviewed audit decision disclosed in the report (the ledger diff is part of the audit commit); NEVER acknowledge a warning that a code/prompt/state/renderer fix could clear instead, and a run never self-acknowledges its own fresh warnings.

## Phase 5 — Audit report (skeleton-then-`Edit`)

Write `docs/audits/<RUN_DATE>-weekly-quality-audit.md`, mirroring the 2026-07-11 report's structure:

1. **Header + method** — mandate, window, run-record link, sub-agents spawned, entries checked / primary URLs fetched.
2. **Verdict** — lead with `clean/total` entries verified and the one-paragraph honest state of the pipeline.
3. **Findings — false or erroneous published intelligence** (table: entry, defect, ground truth, fix) + root causes. Minor imprecisions documented even when no repair is warranted.
4. **Findings — missing or incomplete coverage** — recovered items, correctly-droppable borderlines with reasons, resolved false alarms.
5. **Findings — systemic / operational** (incl. fix-effectiveness results from Phase 3.6).
6. **Priority calibration** (monthly fires only — Phase 3b output).
7. **Fixes shipped in this commit** — including the warning sweep's outcome: what was fixed, and every new/removed `state/warning_acknowledgments.json` entry with its reason.
8. **Recommendations** (operator decisions, not shipped) — numbered, carried forward until adopted or explicitly retired.
9. **Watch items** — carried-forward status + new items, each with its resolution condition.

Empty sections state "none found" — the absence is a result. Then write the run record: telemetry frontmatter (audit passes under `sub_agents:`), verification & coverage notes summarizing the report, `entries_published` = recovered entries only.

## Phases 5.5 → 7 — State, gate, verify, publish

**`Read prompts/cti-run.md` now** (Phases 5, 5.5, 5.7, 6, 7) and execute verbatim with this run's `RUN_ID`: state lifecycle only where recovered entries touched it; `python3 tools/check_run.py "$RUN_ID" --pre-verify` exit 0 before the first verifier spawn. The Phase 5.7 loop (≥1 iteration ALWAYS — ≥2 for a CLEAN publish per the double-CLEAN gate, opus/sonnet rotation, cap 8, fail-open) is scoped to: this run's recovered entries + the run record + **the audit report** — the report makes checkable claims about published files, records and state, and a cold reader must confirm they hold on disk (the 07-11 audit's own iteration 1 caught exactly this class: a claimed repair log entry that wasn't there). Then stage specifics (incl. `docs/audits/`, `work/<run-id>/`, `.claude/memory/` when touched), commit, sync `origin/main`, push with retry, Phase 7 publish polling — report `publish:` from the actual poll.

---

## Quality gates (self-check)

- [ ] Every window entry was covered by exactly one truth pass — or its batch's abandonment is logged as an audit coverage gap.
- [ ] Both audit halves ran: truth passes (soundness) AND independent re-sweeps (completeness) — or the cut is recorded with the watchdog rationale.
- [ ] Every confirmed defect carries a root cause and either a shipped fix or a numbered operator recommendation — no orphan findings.
- [ ] In-place repairs limited to the logged immutability-exception class; every one logged in memory and disclosed; everything else is `update_of` or a recommendation.
- [ ] Previous audit's watch items re-checked and its fixes effectiveness-checked.
- [ ] Monthly duty honored: at most one `## Priority calibration` section per calendar month across audit reports, and at least one unless no audit fired that month.
- [ ] Recovered entries passed the full normal gates (dedup, `check_run.py`, verifier loop) — audit provenance never lowers a bar.
- [ ] Zero-warning sweep complete: `python3 tools/check_run.py --all` ends **0 warn · 0 fail** (acknowledged excepted) and `python3 site/build.py` emits no self-check warnings; every ledger change is disclosed in the report.
- [ ] No manufactured findings; clean components reported clean.
- [ ] All shared gates from `prompts/cti-run.md` § Quality gates hold (gate exit 0, ≥1 verifier iteration, run record committed, publish verified).

---

## Output

```
run: runs/YYYY-MM-DD/<run-id>.md
audit: docs/audits/YYYY-MM-DD-weekly-quality-audit.md
window: <start> → <end> · entries audited: N (clean: N) · runs reviewed: N
findings: erroneous: N · coverage gaps: N (recovered: N) · systemic: N · calibration: run | not-due
fixes shipped: N · repairs (logged exceptions): N · watch items: N open
warnings: 0 open (N acknowledged) · build self-check: clean
commit: <short SHA> · push: ok (feature branch) | failed (<reason>) · publish: ok | main-only | pending (<reason>)
```

---

## META — self-evolution authority

Same authority and process as `prompts/cti-run.md` § META. All hard invariants apply, plus:

- **A-INV-1:** the audit never edits a published entry outside the logged immutability-exception class (factual metadata poisoning machine surfaces); every other correction is a new `update_of` entry.
- **A-INV-2:** findings are never manufactured — a clean week is the success outcome and is reported as such.
- **A-INV-3:** the audit report and run record ship even when the audit finds nothing or the watchdog cuts it short; a silent audit is an operational failure.
- **A-INV-4:** the audit ships fixes under the versioning rule and never weakens a hard invariant — concerns about an invariant become recommendations, not edits.
- **A-INV-5:** the audit never blocks or races the scheduled intel/weekly runs — it works on published history plus its own artifacts, on its own feature branch (per-run paths and dedup make a concurrent intel fire safe).
