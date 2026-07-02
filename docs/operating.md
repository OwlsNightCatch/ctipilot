# Operating

Operator's reference for the autonomous CTI brief generator: one-time setup, the publishing chain, the operations dashboard, the sub-agent capability ceiling, and what to do when something goes wrong.

The full daily / weekly process narrative lives in the prompts themselves — [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md) and [`prompts/weekly-summary.md`](../prompts/weekly-summary.md). This file is the operator-facing wrapper around them.

---

## Publishing chain — feature branch only

`main` is protected: only [`.github/workflows/auto-merge-claude.yml`](../.github/workflows/auto-merge-claude.yml) promotes commits onto it. Every Claude Code session in this repo (interactive or routine) operates on a `claude/<adjective>-<name>-<id>` feature branch.

```
routine fires (cloud, scheduled)
   │
   ▼
feature branch  ─── git push ───▶  auto-merge-claude.yml
   (claude/<…>)                      │
                                     ▼ ff-merge to main (or regular merge with auto-resolution
                                     │  for state/*.json → --ours, sources/sources.json → --theirs)
                                     ▼
                                   main  ─── workflow_run ───▶  deploy-site.yml
                                                                   │
                                                                   ▼ runs site/build.py,
                                                                     force-pushes to gh-pages
                                                                   ▼
                                                                 https://ctipilot.ch/
```

The redundancy: the routine's local clone may be staleness-biased (network proxy mirrors github.com on a schedule, not per-pull), so the auto-merge workflow runs the same merge logic against the live `main` tip on a github-hosted runner. Two passes catch races the local routine missed.

**Direct push to `main` is forbidden** by the `main-protect` ruleset. Don't try it from a routine, a worktree, or a CI job.

---

## One-time setup

### 1. Install the Claude GitHub App

The routine container pushes through an internal git proxy that uses a scoped GitHub credential. The most reliable credential source is the **Claude GitHub App**.

1. Go to <https://github.com/apps/claude>.
2. **Configure** (or **Install** if it's not yet on your account).
3. Under **Repository access**, either:
   - **All repositories**, or
   - **Only select repositories** → add this repo.
4. Save.

If you'd rather use `gh`-token sync, the alternative is:

```sh
gh auth refresh -h github.com -s repo
# then in a Claude Code CLI session:
/web-setup
```

This widens your `gh` token to include `repo` write scope and syncs it to your claude.ai account. The Claude GitHub App route is more durable.

Either way, the credential the routine uses must have write access to this repo, otherwise the push step fails with HTTP 403 *(Permission to … denied)*.

### 2. Workflow permissions for `auto-merge-claude.yml`

[`auto-merge-claude.yml`](../.github/workflows/auto-merge-claude.yml) runs against pushes to `claude/**` branches. It needs `contents: write` on the default `GITHUB_TOKEN` so it can fast-forward `main`.

- The workflow declares this in its `permissions:` block, so for most repos it works without further configuration.
- If your repo or organization has set the default `GITHUB_TOKEN` permissions to **read-only**, the workflow's `git push origin main` is rejected and the brief stays on the feature branch.
- To check / fix: GitHub repo → **Settings** → **Actions** → **General** → under **Workflow permissions**, choose **Read and write permissions**, save.

The workflow also exposes a manual `workflow_dispatch` trigger with a `branch` input, so you can merge a `claude/...` branch that was pushed before the workflow existed (or re-run after fixing an issue). GitHub repo → **Actions** → **Auto-merge claude/\* branches to main** → **Run workflow** → enter the branch name.

### 3. Enable GitHub Pages

The site at <https://ctipilot.ch/> is the published reader. Enable Pages once:

1. GitHub repo → **Settings** → **Pages**.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**, **Branch** to **`gh-pages`**, **Folder** to **`/` (root)**.
3. Save.

The first push to `main` that touches the brief feed (`briefs/`, `state/`, `sources/`, `docs/`, `README.md`, `site/`, or the workflow itself) triggers [`.github/workflows/deploy-site.yml`](../.github/workflows/deploy-site.yml), which runs `site/build.py` and force-pushes the rendered site to `gh-pages`. The custom domain comes from the `CNAME` file at the repo root (`ctipilot.ch`).

### 4. Set up the routine itself

In <https://claude.ai/code/routines>:

1. **New routine** → point it at this repository.
2. **Schedule** — pick a cadence. For daily: weekday mornings before SOC handover is the recommended pattern; the prompts are gap-derivation aware so missed runs are caught up automatically.
3. **Prompt** — exactly one line: `Read prompts/daily-cti-brief.md and execute it.` (Or `prompts/weekly-summary.md` for the weekly routine.)
4. **Permissions** — leave **Allow unrestricted branch pushes** *off*. The routine pushes to `claude/**` only; the auto-merge workflow promotes.
5. **Sub-agent capability ceiling** — see § [Sub-agent capability ceiling](#sub-agent-capability-ceiling) below; restrict to read-only tools.
6. **Environment variables for self-identification** — set both env vars in the routine container so every agent (main + sub-agents + verifier) emits a precise `**Model:**` line in its return:
   - `CLAUDE_FRIENDLY_NAME` — the human-facing name (e.g. `Claude Opus 4.7`, `Claude Sonnet 4.6`). Should match the friendly name a release blog post would use.
   - `CLAUDE_MODEL_ID` — the canonical model id the harness identifies the agent by (e.g. `claude-opus-4-7`, `claude-sonnet-4-6`).
   When unset, the agents fall back to "reason about your identity from runtime context" — workable but demonstrably drift-prone (sub-agents have pattern-matched stale training-data names like `Claude Sonnet 4.5` with model id `claude-sonnet-4-6`). Setting these env vars is the single highest-confidence way to make every brief's AI-content notice precisely correct.
7. **Allow the `cti-verification-alt` sub-agent type** — Phase 5.7 / Phase 4.7 rotates verifier per iteration: odd iterations spawn `cti-verification` (Opus default), even iterations spawn `cti-verification-alt` (Sonnet default). Both definitions live under `.claude/agents/`; if the routine needs an explicit allow-list, include both names.

---

## Customizing the organization profile

Everything organization-specific is parameterized in [`config/org-profile.yaml`](../config/org-profile.yaml): who the briefs are for (name, sector, region, description, audience), the **product watchlist** (estate technologies swept for advisories / exploitation every run — e.g. Windows Server, Windows clients, a firewall line), the **supplier watchlist** (companies swept for breach / incident / compromise reporting), standing free-text interests, and the **vulnerability-triage scheme** (your own categories with criteria + response targets; when configured, every CVE-typed brief item carries a `**Org triage (<short_name>):** P1 — …` line derived from the item's cited facts).

To change it:

1. Edit `config/org-profile.yaml` (the file documents its own strict-YAML syntax; sectors/regions must be `site/taxonomy.yaml` values).
2. Run `python3 tools/compose_prompts.py --check` to validate, then `--write` to render the values into the `ORG-PROFILE` managed blocks inside the two master prompts and the three agent definitions. **Never edit those blocks by hand.**
3. Commit the config **and** the composed files together, on a feature branch as usual.

If you edit the config on an operator branch (e.g. via the GitHub web UI) and forget step 2, the [`compose-profile`](../.github/workflows/compose-profile.yml) workflow composes and commits for you; on `claude/**` branches and `main` it is check-only and fails loud instead (auto-committing there would race the auto-merge workflow). `tools/check_brief.py` additionally WARNs (`profile-sync`) when a routine runs against a stale composition.

Guardrails you get for free: watchlist matches only *lower the relevance bar* (they never bypass recency / verification / sourcing gates); watchlist-driven items are tagged `watchlist` in their footers and capped by the ≤ ⅓ anti-overshoot guideline so general threat-landscape coverage always stays primary; a zero-hit sweep is reported as one `Watchlist:` line in the Verification Notes, never padded items. Empty watchlists + no triage scheme (the shipped default) make every profile-driven behaviour a no-op.

**Closed-source feeds:** point your provider-export / ISAC-download script at the `intel/<YYYY-MM-DD>/` drop-folder contract ([`intel/README.md`](../intel/README.md)) — the next routine fire ingests the documents via a dedicated intake sub-agent, cites them by reference (never linked), and enforces the TLP ceiling implied by `deployment.visibility`. **Private hosting:** to run the whole stack org-internally (private repo, internal web server on a scheduled pull → build → serve loop, above-CLEAR intel allowed), follow [`docs/private-deployment.md`](private-deployment.md).

## Source-health snapshot

[`tools/source_health.py`](../tools/source_health.py) is an independent weekly health-check of every `status: active` source. HEAD-only against each source URL, records `(id, status_code, latency_ms, fetched_at, class)` per source into `state/source_health.json` (bounded history, 12 runs ≈ 3 months at weekly cadence). Runs as the [`weekly-source-health`](../.github/workflows/source-health.yml) GitHub Action on Sundays at 04:30 UTC, and on manual `workflow_dispatch`.

The Ops dashboard surfaces this once `state/source_health.json` exists. The signal you're looking for is the **stable** failing pattern (a source that's been unreachable for the last 3+ snapshots) versus the day-of-week luck of the routine's daily fire (a one-off 503 on the day the routine ran). Use it to decide which sources to demote in `sources/sources.json` versus which to leave alone because they recovered.

To run manually: `python3 tools/source_health.py --dry-run --timeout 12`.

## Source candidates

[`tools/source_candidates.py`](../tools/source_candidates.py) walks the last 30 days of briefs, counts every outbound link host, subtracts hosts already in `sources/sources.json` and the news-aggregator allowlist, and outputs the top-N missing-but-cited domains. Operator runs manually (or as a weekly cron) to spot publishers worth promoting to `status: candidate`. Pure post-hoc analytics; no runtime cost on the brief routine.

```sh
python3 tools/source_candidates.py                # last 30 days, top 20
python3 tools/source_candidates.py --window-days 14 --top 30
python3 tools/source_candidates.py --json         # machine-readable
```

## Operations dashboard

Live at [`/ops/`](https://ctipilot.ch/ops/). Read directly from `state/run_log.json`, rendered server-side at build time. Surfaces:

- **Recent runs** — sub-agent allocation per S1–S4, fetch failures, items published, deep-dive picks, verification iterations + residuals, prompt version executed.
- **Stale active sources** — sources marked `active` in `sources/sources.json` whose `last_successful_fetch` is more than 7 days old. Useful for spotting a quietly broken source or a rotation bias.

Operator-side signals to watch:

| Signal | What it usually means |
|---|---|
| Same source on the stale list for >14 days | The source is dead, blocked, or its canonical URL changed. Open it manually; if the publisher restructured, update `url` in `sources/sources.json` and let the agent recover; if the publisher is gone, demote it. |
| `verification_residual_count` non-zero on consecutive runs | Verifier is finding the same residual issue repeatedly. Check § Verification Notes in the brief; if a check needs adjusting, edit the relevant agent definition (`.claude/agents/cti-verification.md` AND `cti-verification-alt.md` together — both verifier definitions move in lockstep) and bump the prompt version. |
| `cap-breach` warning on `tools/check_brief.py` | Verifier's final iteration returned `NEEDS_FIXES` — the brief published at the safety-valve cap, not on a CLEAN verdict. Three or more cap-breaches in a 7-day window is the threshold to investigate prompt drift; the verifier is either finding real defects (signal: research sub-agent quality regression) or chasing fabricated ones (signal: verifier prompt regression). |
| `fetch_failures` spike on one sub-agent | Either a publisher block (frequent on CISA / NCSC.ch — already routed via [`tools/fetch_source.py`](../tools/fetch_source.py)) or a transient network event. If it persists across runs for the same host, add the host to the bridge fetcher. |
| Prompt version not bumped after a prompt edit | `tools/check_brief.py` cross-checks; this should never happen in production. If it does, the prompt-versioning rule (CLAUDE.md) was skipped — restore the bump. |

---

## Sub-agent capability ceiling

The four research sub-agents the daily routine spawns (and the cold-reader verification sub-agent) are the single most dangerous configuration surface: a sub-agent that follows an injection-laced page could perform writes the parent never intended. When configuring the routine in claude.ai, restrict the sub-agent toolset to **read-only** operations:

| Allowed for sub-agents | `Read`, `Grep`, `Glob`, `WebFetch`, `WebSearch` |
| Forbidden for sub-agents | `Write`, `Edit`, `Bash`, `Task`, `NotebookEdit` |

The main agent retains the full toolset (it has to write the brief and push the commit). Sub-agents return Markdown to the main context and never touch the filesystem or git directly.

Verify the live routine config matches this list as a periodic operator-checklist task. The custom sub-agent definitions in [`.claude/agents/`](../.claude/agents/) name their allowed tools, but the runtime is what enforces them.

---

## Rotation cadence (credentials)

The routine credential (Claude GitHub App installation token, or the synced `gh` token) inherits its lifetime from the underlying credential. Rotate at least every 90 days, or whenever a routine operator leaves:

- **Claude GitHub App** — re-install the App on the repo to roll the installation token. No prompt or routine change needed.
- **`gh`-token sync** — re-run `gh auth refresh -h github.com -s repo` and `/web-setup` from a Claude Code CLI session.

A leaked credential lets the holder push commits as the routine. Because every routine commit appears in the git diff and every prompt edit triggers the in-prompt CHANGELOG-bump rule, a maliciously crafted run is detectable but not preventable in real time. The defensive frame is "detect and correct".

---

## Limits to be aware of

- **Routine wall-clock budget.** Each sub-agent runs against a ~10-minute soft budget (the prompt instructs the main agent to abandon a stalled sub-agent rather than block the brief). A sustained slowdown on a national-CERT host shows up as `fetch_failures` for that source on the Ops dashboard, not as a missed brief.
- **Stream timeout.** A single `Write` of the whole brief sometimes trips a stream-idle timeout. The prompts use the skeleton-then-Edit pattern (write a placeholder skeleton, then `Edit` each section in turn) to dodge this.
- **Network proxy staleness.** The routine container's git proxy mirrors github.com on a schedule, not per-pull, so the routine's local view of `origin/main` may be a few minutes stale. The auto-merge workflow runs the same merge logic against the live tip; this is the safety net.

---

## When something goes wrong

| Symptom | First thing to check |
|---|---|
| Routine fired but no commit on the feature branch | Routine container died mid-run. Check the routine's run log in claude.ai. If a partial brief is on disk in `briefs/`, the next run will rebuild state from it. |
| Push succeeded but auto-merge workflow didn't run | GitHub Actions outage or `workflow_run` concurrency conflict. Check **Actions** → **Auto-merge claude/\* branches to main**; manually trigger via `workflow_dispatch` with the branch name. |
| Auto-merge ran but failed loud (`::error::`) | A merge conflict outside the auto-resolved paths (`state/*.json`, `sources/sources.json`). Workflow logs name the conflicting file; resolve manually and re-trigger. |
| Auto-merge succeeded but `https://ctipilot.ch/` is stale | `deploy-site.yml` failure. Check **Actions** → **Deploy GitHub Pages site**. Common causes: vendored-library SHA mismatch, taxonomy validation failure, smoke-test failure. |
| `tools/check_brief.py` FAILs blocking a commit | See [`prompts/check-brief-fixes.md`](../prompts/check-brief-fixes.md) — every common FAIL has a fix recipe. |
| Custom domain stops resolving (`ctipilot.ch` fails) | The `CNAME` file at the repo root may have been removed. Restore it (single line: `ctipilot.ch`) and re-deploy. GitHub Pages → repo Settings → Pages should show the custom domain populated. |
