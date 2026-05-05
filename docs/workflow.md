# Workflow — Daily and Weekly

End-to-end process for both the daily routine and the weekly summary routine.

## Two routines

| Routine | Cadence | Prompt | Output |
|---|---|---|---|
| Daily CTI brief | Once per day (e.g. 06:30 Europe/Zurich, Mon–Sat) | `prompts/daily-cti-brief.md` | `briefs/YYYY-MM-DD.md` |
| Weekly summary | Once per week (Sunday recommended) | `prompts/weekly-summary.md` | `briefs/weekly/YYYY-Www.md` |

Both share the same source list (`sources/sources.json`), state files (`state/covered_items.json`, `state/cves_seen.json`), verification policy (`docs/verification.md`), and quality gates. The weekly routine reads the daily briefs from the past week and adds horizon view; the daily routine reads the past 7 days of briefs (including the latest weekly summary if recent) for deduplication.

---

## Daily routine — phases

---

## 1. Routine fires

A scheduled Claude Code task fires once per day on Opus 4.7. Recommended schedule: weekday mornings local time, e.g. 06:30 Europe/Zurich, so the brief is available before the SOC's morning shift handover. Weekends optional.

The routine's prompt is exactly:

> Read `prompts/daily-cti-brief.md` and execute it.

The agent is given the repository root as its working directory and write access to the repo.

---

## 2. Phase 0 — Preflight

The agent loads:
- `sources/sources.json` — only `status: "active"` sources feed sub-agents.
- The briefs from the **last 7 calendar days** under `briefs/` (and the most recent weekly summary in `briefs/weekly/` if dated within the window) — extracts a dedup index of CVEs, actors, campaigns, victims, annual-reports.
- `state/covered_items.json` — structured rolling log (full records).
- `state/cves_seen.json` — flat fast-lookup CVE index.

If any read fails, the agent surfaces the error and stops; it does not silently proceed without prior context.

---

## 3. Phase 1 — Parallel research (seven sub-agents)

In a single message, the agent spawns seven `Agent` tool calls in parallel:

| Sub-agent | Scope | Source filter |
|---|---|---|
| A. Active & Breaking | Last 24–72 h ITW exploitation, emergency advisories | `active-breaking` |
| B. Switzerland & Europe | CH/EU nexus only | `ch-eu` |
| C. Government & Public Sector | Gov-targeting / state-linked, transferable TTPs | `gov` + `research` |
| D. Trending Vulnerabilities | KEV / PoC / new vendor advisories | `vulns` |
| E. Vendor & Independent Research | Last 7 days substantive technical reports + new yearly reports | `research` |
| F. Quality News & Commentary | Editorial signal | `news` + `discovery` |
| G. Major Breaches | Newly disclosed breaches; regulator notices | `breaches` + `news` |

Each receives:
- Its category-filtered subset of `sources.json`.
- The deduplication context from Phase 0.
- Today's date and the recency window.
- Constraints: **no IOCs, no vanity metrics, English output**.
- A *flexible* return format — Markdown with required fields (sources, summary, CH/EU nexus, gov nexus, CVEs, actors, verification status, novelty). Sub-agents may add extended context. **No token cap.**

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

If no item clears the bar, the deep-dive section says so explicitly. The agent does not invent depth.

Deep-dive content includes kill chain, ATT&CK mapping, and detection *concepts* — never IOCs and never rule code.

---

## 6. Phase 4 — Compose brief

The agent writes `briefs/YYYY-MM-DD.md` with sections 0–9 per the canonical structure (see `briefs/README.md`).

Style enforced by quality gates:
- Always English.
- Inline link after every claim.
- No bibliography.
- No IOCs.
- No vanity metrics.
- No emojis.
- Hedge only when the source hedges.

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
- For each source the agent fetched and used today, set `last_successful_fetch` to today's ISO date and reset `consecutive_failures` to 0.
- For each source that returned 404 / dead host / empty content, increment `consecutive_failures`. If `>= 3`, drop the reliability tier by one (HIGH → MEDIUM, MEDIUM → LOW), set status to `demoted`, and add a `notes` line with today's date and the failure mode.
- If a *new* high-quality source was discovered (linked from existing trusted sources, with editorial track record), append it with `status: "candidate"`, `notes: "discovered YYYY-MM-DD via {source-id}"`. **Never auto-promote.** Humans review candidates.
- **Never delete a source.** Demotions are reversible by humans editing the file.

---

## 8. Phase 6 — Commit

The agent stages and commits only the touched files:

```bash
git add briefs/YYYY-MM-DD.md state/covered_items.json state/cves_seen.json sources/sources.json
git commit -m "brief: YYYY-MM-DD

- ch-eu: N · vulns: N · breaches: N · research: N · deep dive: <topic or 'none'>
"
```

The agent does **not** push. Push policy is set by the human operator (e.g. weekly review-and-push, or auto-push to a private mirror with branch protection).

---

## 9. Phase 7 — Output

The agent prints exactly three lines to the terminal:

```
brief: briefs/YYYY-MM-DD.md
items: N · ch-eu: N · vulns: N · deep-dive: <topic or 'none'>
commit: <short SHA or 'no-changes'>
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
3. **Phase 2 — Horizon research.** Spawn three sub-agents in parallel:
    - **W1** Long-horizon campaign status check (Salt Typhoon, Volt Typhoon, BRICKSTORM, Forest Blizzard, Akira/SonicWall, Ivanti waves, etc.).
    - **W2** Yearly / quarterly threat reports published in the last 30 days that the daily briefs did not yet cover.
    - **W3** Cybersecurity policy and regulatory developments relevant to Swiss and European public-sector entities.
4. **Phase 3 — Compose.** Write `briefs/weekly/YYYY-Www.md` with sections 0–10 (Week at a glance, Top stories, Multi-day chains, Vulnerability roll-up table, Sector & victim patterns, Major breaches recap, Annual/periodic reports, Long-running campaigns status, Policy & regulatory horizon, Looking ahead, Verification & coverage notes).
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
