# Workflow — Daily and Weekly

End-to-end process for both the daily routine and the weekly summary routine.

## Two routines

| Routine | Cadence | Prompt | Output |
|---|---|---|---|
| Daily CTI brief | Operator-chosen (typically working days only — Mon–Fri) | `prompts/daily-cti-brief.md` | `briefs/YYYY-MM-DD.md` |
| Weekly summary | Operator-chosen (typically once per week) | `prompts/weekly-summary.md` | `briefs/weekly/YYYY-Www.md` |

**Recency window is gap-derived, not schedule-derived.** Each run reads its own brief directory (`briefs/` for the daily, `briefs/weekly/` for the weekly), finds the most recent published brief, and computes the recency window as `max(default, gap_since_previous + safety_overlap)`. This is **self-healing** for missed runs (a failed Tuesday is automatically caught up by Wednesday) and **schedule-agnostic** (the operator can change cron times or skip days without touching the prompt). The Monday daily naturally covers Friday-late + the weekend on a Mon–Fri schedule because the gap on disk is ~72–84 h. See Prime Directive 7 in [`../prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md).

Both share the same source list (`sources/sources.json`), state files (`state/covered_items.json`, `state/cves_seen.json`), verification policy (`docs/verification.md`), and quality gates. The weekly routine reads the daily briefs from the past week and adds horizon view; the daily routine reads the past 7 days of briefs (including the latest weekly summary if recent) for deduplication.

---

## Daily routine — phases

---

## 1. Routine fires

A scheduled Claude Code routine fires on whatever cadence the operator chose; the prompt does not assume a specific time or day. The recommended pattern is weekday mornings before the SOC's morning shift handover, with weekends covered by the gap-derivation rule on the next run.

The routine's prompt is exactly:

> Read `prompts/daily-cti-brief.md` and execute it.

The agent is given the repository root as its working directory and write access to the repo.

---

## 2. Phase 0 — Preflight

The agent loads:
- `sources/sources.json` — only `status: "active"` sources feed sub-agents.
- The briefs from the **last 7 calendar days** under `briefs/`, plus the **most recent weekly summary** at `briefs/weekly/YYYY-Www.md` for the current ISO week and the prior ISO week (named explicitly, regardless of mtime) — extracts a dedup index of CVEs, actors, campaigns, victims, annual-reports.
- `state/covered_items.json` — structured rolling log (full records).
- `state/cves_seen.json` — flat fast-lookup CVE index.
- `state/deep_dive_history.json` (if present) — last 30 days of deep-dive picks. Used by Phase 3's category-rotation rule.

If any read fails, the agent surfaces the error and stops; it does not silently proceed without prior context.

---

## 3. Phase 1 — Parallel research (four sub-agents)

In a single message, the agent spawns four `Agent` tool calls in parallel. The four-agent design (down from seven in earlier versions) trims per-run LLM load to avoid stream-timeout / rate-limit pressure while keeping the same coverage. Source categories are partitioned cleanly so no two sub-agents touch the same source for the same purpose.

| Sub-agent | Scope | Source categories |
|---|---|---|
| 1. Active Threats & Trending Vulnerabilities | ITW exploitation, emergency advisories, KEV/PoC/CVE table | `active-breaking`, `vulns` |
| 2. Switzerland, Europe & Public Sector | CH/EU nexus + global public-sector targeting | `ch-eu`, `gov` |
| 3. Research & Investigative Reporting | Vendor research, journalism, annual reports | `research`, `news`, `discovery` |
| 4. Incidents & Disclosures | Publicly-disclosed incidents, regulator notices | `breaches` (+ `news` for corroboration) |

Each receives:
- Its category-filtered subset of `sources.json`.
- The deduplication context from Phase 0.
- Today's date and the recency window.
- Constraints: **no IOCs, no vanity metrics, English output**.
- A *flexible* return format — Markdown with required fields (sources, summary, CH/EU nexus, public-sector nexus, sector, CVEs, actors, verification status, confidence, novelty). Sub-agents may add extended context. **No token cap.**
- A spawn-prompt opening that leads with defensive intent.

Sub-agents that find nothing return an empty list with a one-line note.

---

## 4. Phase 2 — Verification (main context)

For every candidate item:

1. **Re-fetch primary source** if there is any doubt the URL still resolves with the claimed content.
2. **Apply the two-source / national-CERT rule** (see `docs/verification.md`).
3. **Apply the fake-news guard** (see `docs/verification.md`).
4. **Verify CVE identifiers** resolve on NVD/MITRE.
5. **Apply deduplication.** Drop items in the last-5 briefs index unless there is a material delta. Apply the long-running-campaign rule (≤1 update per week unless critical).
6. **Sanity-check dates.** Drop items mis-dated as today's news.
7. **Rank** by exploitation > CH/EU nexus > gov nexus > novelty.

Items that fail verification are *not* silently dropped. They appear in § 8 (Verification Notes) so reviewers can audit decisions.

---

## 5. Phase 3 — Deep-dive selection

The agent picks at most 1 (exceptionally 2) items for technical deep dive. Selection criteria, in priority order:

1. Active in-the-wild exploitation **and** non-trivial exposure for Swiss / European public-sector environments.
2. Active exploitation with strong CH/EU or government nexus.
3. Substantive new technical analysis with sufficient public detail to be actionable.

**Category-rotation rule.** The agent reads `state/deep_dive_history.json`. If a candidate's category was already covered in the prior 7 days, the candidate is demoted one rank — unless criterion 1 (active exploitation + non-trivial CH/EU public-sector exposure) makes it irreducibly urgent. The intent: avoid covering Linux LPE five days running while network-stack RCE, identity infrastructure, and OT go untouched.

If no item clears the bar, the deep-dive section says so explicitly. The agent does not invent depth.

Deep-dive content includes the incident narrative (defender's perspective), ATT&CK technique mapping, and detection *concepts* — never IOCs and never rule code.

---

## 6. Phase 4 — Compose brief

The agent writes `briefs/YYYY-MM-DD.md` with sections 0–8 per the canonical structure: 0 TL;DR · 1 Immediate Actions (often absent) · 2 Active Threats / Trending Actors / Notable Incidents & Disclosures · 3 Trending Vulnerabilities · 4 Research & Investigative Reporting · 5 Updates to Prior Coverage · 6 Deep Dive · 7 Action Items · 8 Verification Notes. Each H3 item carries a v2 metadata footer (see `briefs/README.md` for the full schema).

Style enforced by quality gates:
- Always English.
- Inline link after every claim.
- No bibliography.
- No IOCs.
- No vanity metrics.
- No emojis.
- Hedge only when the source hedges.

---

## 6.5 Phase 4.5 — Final verification sub-agent (URL truth + editorial quality)

After the brief is composed, an independent verification sub-agent reads it end-to-end. The verifier covers two concerns in the same pass:

- **Truth gate** — every URL fetched, every claim cross-checked against its linked source, every named entity (CVE / actor / campaign / version / number) traced back to a source the verifier could read.
- **Editorial-quality gate** — relevance to a Swiss / EU public-sector SOC, primary-source strength (NVD/MITRE and national CERTs/NCSCs are second-tier primaries — the disclosing vendor's PSIRT advisory or research-lab post is preferred), vendor-marketing tells, fake-news patterns, contradictions, clarity. Items the audience does not need are flagged for drop.

The verifier returns structured findings and a verdict (`CLEAN` / `NEEDS_FIXES`). The main agent applies remediation per finding type:

- Broken / generic URLs → re-pivot via `WebFetch` / `WebSearch` / `tools/fetch_source.py` to a specific article URL, or drop.
- Unsupported facts → drop.
- Strengthen primary source → promote vendor advisory, demote NVD/CERT to `Additional source:`.
- Drop (low relevance) → remove the item, log in § 8, drop the today-appearance from `covered_items.json`.
- Needs more research → spawn ≤3 follow-up research sub-agents in parallel; re-Edit or drop.
- Surface contradiction → explicit § 8 contradiction line; do not silently pick a side.
- Missed angles → spawn one targeted research sub-agent if it would clear the inclusion gate; else log as a coverage gap.

A fresh verification sub-agent then runs against the updated brief. The loop runs until verdict `CLEAN` or until the iteration cap (3) is reached. Verification iterations and residual count are written to `state/run_log.json` (`verification_iterations`, `verification_residual_count`) — the Ops dashboard reads them.

Full details and the verbatim spawn template live in [`../prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) Phase 4.5; quality bar definitions live in [`verification.md`](verification.md).

---

## 7. Phase 5 — State update

The agent updates two files:

### `state/cves_seen.json`
Flat fast-lookup CVE index. For each CVE referenced in today's brief, append (or update) `{"id", "first_seen", "last_seen", "title", "primary_source_url"}`. Sub-agents read this file in Phase 0 for fast dedup.

### `state/covered_items.json`
For each item written into today's brief, append a record:

```json
{
  "key": "CVE-YYYY-NNNNN | actor:name | campaign:name | incident:slug",
  "type": "cve | actor | campaign | incident | tool | vulnerability-trend",
  "title": "Short title",
  "first_covered": "YYYY-MM-DD",
  "last_covered": "YYYY-MM-DD",
  "primary_source_url": "URL",
  "appearances": [
    {
      "date": "YYYY-MM-DD",
      "section": "active_breaking | ch_eu | gov_public | trending_vulns | research | deep_dive | updates",
      "brief_path": "briefs/YYYY-MM-DD.md",
      "delta_summary": "One-line description of what was new this run"
    }
  ]
}
```

If the `key` already exists, the agent appends to its `appearances` and bumps `last_covered`. It does not duplicate the record.

### `sources/sources.json`
- For each source the agent fetched and used today, set `last_successful_fetch` to today's ISO date and reset `consecutive_fetch_failures` and `consecutive_quiet_periods` to 0.
- For each source that returned 200 with no in-window items, increment `consecutive_quiet_periods` (a content signal — does not demote on its own).
- For each source that returned a transport error (HTTP 403 / 429 / 503 / 5xx / connection failure), increment `consecutive_fetch_failures`. **Sustained 403/429/5xx never demotes** — that pattern means the publisher is blocking the agent, not that the source is dead. Record an alternate-URL strategy in `notes`.
- For each source that returned 404 / dead host, increment `consecutive_fetch_failures` and try one canonical-URL probe. Demotion fires only after 5 consecutive 404 fails (with no working probe) or 3 consecutive quiet periods with a failed probe.
- If a *new* high-quality source was discovered, append it with `status: "candidate"`. **At most one new candidate per run.** A candidate auto-promotes to `active` after 3 distinct runs in which it was successfully fetched and contributed content.
- **Never delete a source.** Demotion is the soft-removal mechanism; demoted sources stay in the file as audit trail.

### `state/deep_dive_history.json`

If a deep dive was selected this run, append `{date, topic, category}` and trim to the most-recent 30 entries. Phase 3 reads this on the next run.

### `state/run_log.json` — feeds the Ops dashboard

Append a per-run record (model, prompt version, sub-agent allocation, verification-loop counters, fetch failures, items published, deep-dive slug, duration) and trim to 90 days. **Every key in the schema must be populated every run** — a sparse record produces an empty Ops dashboard at `/ops/`. The agent fills in:

- `model`, `prompt_version` — runtime context + `prompts/CHANGELOG.md`.
- `sub_agents.{S1..S4}` — `sources_attempted` (every id named in the spawn message), `sources_used` (subset that contributed at least one citation), `items_returned`, `returned: false` only when the sub-agent stalled past its 10-min budget.
- `verification_iterations`, `verification_residual_count` — Phase 4.5 loop counters.
- `fetch_failures` — every transport error encountered with its HTTP code; `[]` when none.
- `items_published`, `items_dropped_by_verification`, `deep_dive` — final counts.

The Ops dashboard renders sub-agent cells as `items (used/attempted src)`, surfaces a `stalled` badge when `returned: false`, and a yellow badge when `fetch_failures` is non-empty. If any cell on the dashboard reads `—` for today's run, Phase 5 bookkeeping was skipped — Phase 5.5's self-check script catches this.

---

## 8. Phase 5.5 — Self-check gate (institutionalised script)

Phase 5.5 is **a single command**: `python3 tools/check_brief.py`. The script is version-controlled at [`../tools/check_brief.py`](../tools/check_brief.py); the agent runs it after Phase 5 and treats a non-zero exit as a hard stop on the publishing chain.

The script bundles every consistency check the prompt previously listed inline, **plus** the build-side smoke tests in `site/test_build.py`. It verifies:

1. State JSON files (`covered_items.json`, `cves_seen.json`, `deep_dive_history.json`, `run_log.json`, `sources/sources.json`) parse cleanly.
2. `site/taxonomy.yaml` loads with every required key.
3. Core sections (`active-threats`, `trending-vulnerabilities`, `research`) carry ≥1 H3 item or an explicit `intentionally left empty` stub.
4. AI-content notice present at the top of the brief.
5. **IOC heuristic scan** — SHA-256 / SHA-1 / MD5 patterns and routable IPv4 (with version-string false-positive suppression) → FAIL.
6. Every CVE referenced in the brief appears in `state/cves_seen.json`.
7. Every UPDATE block carries at least one inline `[label](url)` citation.
8. Every H3 in `immediate-actions / active-threats / trending-vulnerabilities / research / updates / deep-dive / action-items` ends with a v2 metadata footer.
9. Every footer carries Source (≥1 link), Tags, Region; CVE-typed entries additionally carry CVE / Vector / Auth / Status.
10. Every footer's tags / regions / sectors / vectors / auth / statuses are values from `site/taxonomy.yaml`.
11. Multi-CVE items use either a single shared CVSS or per-CVE breakdown (`9.1 / 7.2` or `9.1 (CVE-…), 7.2 (CVE-…)`).
12. **Primary-source quality** (WARN) — items whose only source is NVD/MITRE or a national CERT/NCSC.
13. **`tools/fetch_source.py` for known-403 hosts** — when the brief cites CISA / NCSC.ch URLs and the run log records an unmitigated 403/429 on those source ids → FAIL.
14. H3 count in core sections matches `appearances[].date == today` count within tolerance 1 (heuristic; warns).
15. `run_log.json` for today is fully populated (every Ops-dashboard field).
16. At least one source has `last_successful_fetch == today` in `sources/sources.json`.
17. `site/test_build.py` exits 0.

Output is line-by-line `PASS / FAIL / WARN  <check>: <detail>` with a final summary. WARNs are tolerated; FAILs block the commit. The script is read-only — the agent fixes drift, the script reports it. New checks added to the script require a prompt-version bump.

If any check fails, Phase 6 is aborted and the operator output prints `state: drift — <reason>`. The brief file remains on disk; the next run rebuilds the state delta from the brief itself (the brief is the canonical artefact).

---

## 9. Phase 6 — Commit and push

The agent stages, commits, and **pushes to `origin/main`** in one go. Each brief is published the moment it is generated.

```bash
git add briefs/YYYY-MM-DD.md \
        state/covered_items.json state/cves_seen.json \
        state/deep_dive_history.json state/run_log.json \
        sources/sources.json
git commit -m "brief: YYYY-MM-DD

- ch-eu+pub: N · vulns: N · incidents: N · research: N · deep-dive: <topic or 'none'>
- sources: <URL updates / demotions / candidates>
- cves: <new: N · updated: N · removed: N>
"
git push origin main
```

The push goes to whatever remote is configured for the repo (Path A in setup is the typical: `git@github.com:OwlsNightCatch/ctipilot.git`). The routine never `--force`-pushes. If a push fails (transient auth or network), the commit stays local and the next run — or a manual `git push` — publishes it. There is no review branch and no human gate; the briefs are AI-content-noticed and source-linked already.

---

## 10. Phase 7 — Output

The agent prints exactly four lines to the terminal:

```
brief: briefs/YYYY-MM-DD.md
items: N · ch-eu+pub: N · vulns: N · incidents: N · research: N · deep-dive: <topic or 'none'>
commit: <short SHA or 'no-changes'>
push: ok | failed (<reason>)
```

Everything else is in the file.

---

## Failure modes and what to do

| Failure | What the agent does | What the operator does |
|---|---|---|
| Sub-agent returns no items | Section says "No qualifying items in window" | Verify source list freshness if multiple days in a row |
| Source URL repeatedly fails | Bumps `consecutive_failures`; demotes after 3 | Review demoted source; either fix URL/feed or accept |
| Verification kills most items | § 8 lists what was dropped | If pattern repeats, review verification rules |
| All sub-agents return empty | Brief is a thin "Quiet day" file | Cross-check against any social-media chatter; quiet days are real |
| Routine itself fails (env, auth) | No file is written | Check Claude Code logs; rerun manually |

---

## Weekly routine — phases

Once per week (Sunday recommended) the weekly routine fires with a single instruction:

> Read `prompts/weekly-summary.md` and execute it.

The agent then:

1. **Phase 0 — Preflight.** Compute current ISO week. Read every daily brief in the 7-day window plus the previous weekly summary (for continuity). Read state files and source list.
2. **Phase 1 — Structured review.** Build five working lists from the daily briefs: top items, multi-day campaigns, CVE roll-up, sector/victim patterns, yearly reports.
3. **Phase 2 — Horizon research.** Spawn two sub-agents in parallel:
    - **W1** Long-horizon ongoing developments — combines a status check on long-running publicly-tracked campaigns with the periodic / annual threat reports published in the last 30 days that the daily briefs did not yet cover.
    - **W2** Strategic & policy horizon — cybersecurity-policy and regulatory developments relevant to Swiss and European public-sector entities.
4. **Phase 3 — Compose.** Write `briefs/weekly/YYYY-Www.md` with sections 0–10 (Week at a glance, Top stories, Multi-day chains, Vulnerability roll-up table, Sector & victim patterns, Incidents & disclosures recap, Annual/periodic reports, Long-running campaigns status, Policy & regulatory horizon, Looking ahead, Verification & coverage notes).
5. **Phase 4 — State update.** Append `weekly_summary` appearance records to `covered_items.json`; update `cves_seen.json` `last_seen` for any CVE referenced; maintain `sources.json`.
6. **Phase 5 — Commit.**

The weekly summary is allowed to repeat content from the daily briefs — that is its purpose. The dedup mechanic on the daily routine treats appearance in a weekly summary the same as appearance in a daily brief: subsequent daily briefs do not re-report unless there is a material new development.

---

## Manual run

To run the routine outside the schedule, in a Claude Code session at the repo root:

```
> Read prompts/daily-cti-brief.md and execute it.
```

For a weekly summary:

```
> Read prompts/weekly-summary.md and execute it.
```

The agent will follow the same phases and produce the corresponding brief.
