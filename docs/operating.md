# Operating

Operator's reference for the autonomous CTI pipeline: one-time setup, the publishing chain, the operations dashboard, the sub-agent capability ceiling, and what to do when something goes wrong.

The full run narrative lives in the prompts themselves — [`prompts/cti-run.md`](../prompts/cti-run.md) (the intel run, fired several times per day) and [`prompts/weekly-summary.md`](../prompts/weekly-summary.md) (the weekly strategic run). The data model (entries, entity registry, run records) is [`docs/pipeline.md`](pipeline.md). This file is the operator-facing wrapper around them.

---

## Publishing chain — feature branch only

`main` is protected: only [`.github/workflows/auto-merge-claude.yml`](../.github/workflows/auto-merge-claude.yml) promotes commits onto it. Every Claude Code session in this repo (interactive or routine) operates on a `claude/<adjective>-<name>-<id>` feature branch.

```
routine fires (cloud, scheduled — intel run N×/day, weekly 1×/week)
   │
   ▼
feature branch  ─── git push ───▶  auto-merge-claude.yml
   (claude/<…>)                      │
                                     ▼ ff-merge to main (or regular merge with auto-resolution:
                                     │  state/*.json + entities/registry.yaml → --ours,
                                     │  sources/sources.json → --theirs; entry + run-record
                                     ▼  files are per-run unique paths and cannot conflict)
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
- If your repo or organization has set the default `GITHUB_TOKEN` permissions to **read-only**, the workflow's `git push origin main` is rejected and the run's output stays on the feature branch (the run's Phase 7 then reports `publish: pending`).
- To check / fix: GitHub repo → **Settings** → **Actions** → **General** → under **Workflow permissions**, choose **Read and write permissions**, save.

The workflow also exposes a manual `workflow_dispatch` trigger with a `branch` input, so you can merge a `claude/...` branch that was pushed before the workflow existed (or re-run after fixing an issue). GitHub repo → **Actions** → **Auto-merge claude/\* branches to main** → **Run workflow** → enter the branch name.

### 3. Enable GitHub Pages

The site at <https://ctipilot.ch/> is the published reader. Enable Pages once:

1. GitHub repo → **Settings** → **Pages**.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**, **Branch** to **`gh-pages`**, **Folder** to **`/` (root)**.
3. Save.

The first push to `main` that touches the content store (`entries/`, `runs/`, `entities/`, `state/`, `sources/`, `docs/`, `prompts/`, `README.md`, `site/`, or the workflow itself) triggers [`.github/workflows/deploy-site.yml`](../.github/workflows/deploy-site.yml), which runs `site/build.py` and force-pushes the rendered site to `gh-pages`. The custom domain comes from the `CNAME` file at the repo root (`ctipilot.ch`).

### 4. Set up the routines

In <https://claude.ai/code/routines>, create these routines against this repository. The full, version-controlled text of every routine invocation prompt — plus a catalog of the in-repo prompts they load — lives in [`docs/routines.md`](routines.md); keep the live routine config in sync with it.

1. **Intel run** — **several times per working day is the intended pattern** (e.g. every 4–6 h). The prompt is cadence-agnostic and self-healing: each fire derives its window from the gap since the previous run record, so missed fires are caught up automatically and the operator can change the cron freely without touching the prompt. More fires mean lower latency, never more content — dedup ensures a re-scan republishes only the new delta, and entry volume follows a strict relevance/actionability gate, not a count. Prompt, exactly one line: `Read prompts/cti-run.md and execute it.`
2. **Weekly run** — once per week, operator-chosen day/time. Prompt: `Read prompts/weekly-summary.md and execute it.` It refuses to fire twice for the same ISO week.
   - **Weekly backup run** *(optional resilience net)* — a second routine scheduled *after* the primary weekly slot that produces the weekly only if the primary did not. It checks whether a `-weekly` run record for the most-recently-completed ISO week reached `main` and exits if so, else runs the weekly. The pipeline has **no** `briefs/weekly/<week>.md` file, and the weekly targets the completed week (the week ending on the most recent Sunday), not the current calendar week — so the check keys on the run record's `week:` frontmatter, never a guessed file path or `date +%V` of today. Copy the exact prompt from [`docs/routines.md` § 1c](routines.md#1c-weekly-backup-run--resilience-net-for-the-weekly). Running the weekly is safe even in a race: `weekly-summary.md`'s Phase 0 `duplicate-week` guard is the authoritative backstop.
3. **Permissions** — leave **Allow unrestricted branch pushes** *off*. The routines push to `claude/**` only; the auto-merge workflow promotes.
4. **Sub-agent capability ceiling** — see § [Sub-agent capability ceiling](#sub-agent-capability-ceiling) below.
5. **Environment variables for self-identification** — set both env vars in the routine container so every agent (main + sub-agents + verifiers) emits a precise `**Model:**` line:
   - `CLAUDE_FRIENDLY_NAME` — the human-facing name (e.g. `Claude Opus 4.7`, `Claude Sonnet 4.6`). Should match the friendly name a release blog post would use.
   - `CLAUDE_MODEL_ID` — the canonical model id the harness identifies the agent by (e.g. `claude-opus-4-7`, `claude-sonnet-4-6`).
   When unset, the agents fall back to "reason about your identity from runtime context" — workable but demonstrably drift-prone (sub-agents have pattern-matched stale training-data names). Setting these env vars is the single highest-confidence way to make every run record's model telemetry — and therefore the site's AI-content notice — precisely correct.
6. **Allow the `cti-verification-alt` sub-agent type** — Phase 5.7 rotates the verifier per iteration: odd iterations spawn `cti-verification` (Opus default), even iterations spawn `cti-verification-alt` (Sonnet default). Both definitions live under `.claude/agents/`; if the routine needs an explicit allow-list, include both names (plus `cti-research`).

---

## Customizing the organization profile

Everything organization-specific is parameterized in [`config/org-profile.yaml`](../config/org-profile.yaml): who the entries are for (name, sector, region, description, audience), the **product watchlist** (estate technologies swept for advisories / exploitation every run — e.g. Windows Server, Windows clients, a firewall line), the **supplier watchlist** (companies swept for breach / incident / compromise reporting), standing free-text interests, and the **vulnerability-triage scheme** (your own categories with criteria + response targets; when configured, every vulnerability entry carries a structured `org_triage: {category, rationale}` frontmatter block derived from the entry's cited facts).

To change it:

1. Edit `config/org-profile.yaml` (the file documents its own strict-YAML syntax; sectors/regions must be `site/taxonomy.yaml` values).
2. Run `python3 tools/compose_prompts.py --check` to validate, then `--write` to render the values into the `ORG-PROFILE` managed blocks inside the two master prompts, `prompts/verification.md`, and the three agent definitions. **Never edit those blocks by hand.**
3. Commit the config **and** the composed files together, on a feature branch as usual.

If you edit the config on an operator branch (e.g. via the GitHub web UI) and forget step 2, the [`compose-profile`](../.github/workflows/compose-profile.yml) workflow composes and commits for you; on `claude/**` branches and `main` it is check-only and fails loud instead (auto-committing there would race the auto-merge workflow). `tools/check_run.py` additionally WARNs (`profile-sync`) when a routine runs against a stale composition.

Guardrails you get for free: watchlist matches only *lower the relevance bar* (they never bypass recency / verification / sourcing gates); watchlist-driven entries carry `watchlist_hit: true` + the `watchlist` tag and are capped by the ≤ ⅓ anti-overshoot guideline so general threat-landscape coverage always stays primary; a zero-hit sweep is reported as one `Watchlist:` line in the run record, never padded entries. Empty watchlists + no triage scheme (the shipped default) make every profile-driven behaviour a no-op.

**Closed-source feeds:** point your provider-export / ISAC-download script at the `intel/<YYYY-MM-DD>/` drop-folder contract ([`intel/README.md`](../intel/README.md)) — the next fire ingests the documents via a dedicated intake sub-agent and cites them via `closed_sources` frontmatter records (referenced, never linked). There is no TLP gate: everything you drop is fair game to process, so the control is what you place in the repo. **Private hosting:** to run the whole stack org-internally (private repo, internal web server on a scheduled pull → build → serve loop) so nothing is world-readable, follow [`docs/private-deployment.md`](private-deployment.md).

## Source-health snapshot

[`tools/source_health.py`](../tools/source_health.py) is an independent health-check of every source, probed via its *actual recipe* (feed discovery for RSS sources, the documented `tools/fetch_source.py` subcommand for bridge/API sources, browser-UA HEAD→GET for the rest). Records per-source status into `state/source_health.json` (bounded history, 12 runs). Runs as the [`source-health`](../.github/workflows/source-health.yml) GitHub Action on Sundays at 04:30 UTC, on manual `workflow_dispatch`, and at the end of every routine fire.

The Ops dashboard surfaces this once `state/source_health.json` exists. The signal you're looking for is the **stable** failing pattern (a source that's been unreachable for the last 3+ snapshots) versus one-fire luck (a one-off 503 on the day a run happened to probe). Use it to decide which sources to demote in `sources/sources.json` versus which to leave alone because they recovered.

To run manually: `python3 tools/source_health.py --dry-run --timeout 12`.

## Source candidates

[`tools/source_candidates.py`](../tools/source_candidates.py) walks the last 30 days of entries, counts every outbound link host, subtracts hosts already in `sources/sources.json` and the news-aggregator allowlist, and outputs the top-N missing-but-cited domains. Operator runs manually (or as a weekly cron) to spot publishers worth promoting to `status: candidate`. Pure post-hoc analytics; no runtime cost on the pipeline.

```sh
python3 tools/source_candidates.py                # last 30 days, top 20
python3 tools/source_candidates.py --window-days 14 --top 30
python3 tools/source_candidates.py --json         # machine-readable
```

## Operations dashboard

Live at [`/ops/`](https://ctipilot.ch/ops/). Built entirely from the frontmatter of the run records under `runs/**`, rendered server-side at build time. Surfaces:

- **Recent runs** — one row per fire: kind (intel/weekly), gap/window hours, `entries_published` / `entries_updated`, deep-dive picks, sub-agent allocation per S1–S4 (+S5 / W1–W3), fetch failures, verification iterations + residuals, entries dropped by verification, prompt version executed.
- **Stale active sources** — sources marked `active` in `sources/sources.json` whose `last_successful_fetch` is more than 7 days old. Useful for spotting a quietly broken source or a rotation bias.
- **Source health** — the recipe-level probe snapshot from `state/source_health.json`, floating only the unsolved problems (`needs-bridge` / `needs-demote`).

Operator-side signals to watch:

| Signal | What it usually means |
|---|---|
| A scheduled fire with no run record | The container died before Phase 4 — the one outcome the prompts are engineered against. Check the routine's run log in claude.ai; the next fire self-heals the coverage window, but investigate anything recurring. |
| `entries_published` at zero across many consecutive intel runs | Legitimate on quiet intraday windows; suspicious over multiple days. Read the run-record bodies (verification notes) — they must say *why* windows were quiet (out-of-window drops, dedup, borderline drops). |
| `verification_residual_count` non-zero on consecutive runs | Verifier is finding the same residual issue repeatedly. Check the run records' verification notes; if a check needs adjusting, edit the relevant agent definition (`.claude/agents/cti-verification.md` AND `cti-verification-alt.md` together — both verifier definitions move in lockstep) and bump the prompt version. |
| `cap-breach` warning on `tools/check_run.py` | Verifier's final iteration returned `NEEDS_FIXES` — the run published at the safety-valve cap, not on a CLEAN verdict. Three or more cap-breaches in a 7-day window is the threshold to investigate prompt drift; the verifier is either finding real defects (signal: research sub-agent quality regression) or chasing fabricated ones (signal: verifier prompt regression). |
| Same source on the stale list for >14 days | The source is dead, blocked, or its canonical URL changed. Open it manually; if the publisher restructured, update `url` in `sources/sources.json` and let the agent recover; if the publisher is gone, demote it. |
| `fetch_failures` spike on one sub-agent | Either a publisher block (frequent on CISA / NCSC.ch — already routed via [`tools/fetch_source.py`](../tools/fetch_source.py)) or a transient network event. If it persists across runs for the same host, add the host to the bridge fetcher. |
| Prompt version not bumped after a prompt edit | `tools/check_run.py` cross-checks the run record's `prompt_version` against `prompts/CHANGELOG.md`; this should never happen in production. If it does, the prompt-versioning rule (CLAUDE.md) was skipped — restore the bump. |

---

## Sub-agent capability ceiling

The research sub-agents the runs spawn (S1–S4 + conditional S5 on intel runs, W1–W3 weekly) and the cold-reader verifiers are the single most dangerous configuration surface: a sub-agent that follows an injection-laced page could perform writes the parent never intended. The agent definitions in [`.claude/agents/`](../.claude/agents/) pin each role's ceiling — keep the live routine config matched to them:

| Role | Toolset |
|---|---|
| `cti-verification` / `cti-verification-alt` | **Read-only**: `Read`, `Grep`, `Glob`, `WebFetch`, `WebSearch`, plus `Bash` for env-var self-identification and the read-only `tools/fetch_source.py` bridge. Never `Write`/`Edit` — the verifier reports; the main agent owns all edits. |
| `cti-research` | Read-only **plus** `Write`/`Edit`/`Bash` scoped by contract to `work/<run-id>/` artefacts (findings YAMLs, url-liveness ledger appends, timestamp checkpoints). Never entries, state, or git. |

The main agent retains the full toolset (it has to write the entries and the run record and push the commit). Sub-agents never compose published content and never touch git directly.

Verify the live routine config matches the definitions as a periodic operator-checklist task — the YAML frontmatter names the allowed tools, but the runtime is what enforces them.

---

## Rotation cadence (credentials)

The routine credential (Claude GitHub App installation token, or the synced `gh` token) inherits its lifetime from the underlying credential. Rotate at least every 90 days, or whenever a routine operator leaves:

- **Claude GitHub App** — re-install the App on the repo to roll the installation token. No prompt or routine change needed.
- **`gh`-token sync** — re-run `gh auth refresh -h github.com -s repo` and `/web-setup` from a Claude Code CLI session.

A leaked credential lets the holder push commits as the routine. Because every routine commit appears in the git diff and every prompt edit triggers the in-prompt CHANGELOG-bump rule, a maliciously crafted run is detectable but not preventable in real time. The defensive frame is "detect and correct".

---

## Limits to be aware of

- **Routine wall-clock budget.** Each sub-agent runs against a hard 30-minute cap (the prompt instructs the main agent to abandon a stalled sub-agent rather than block the run — failing to write the run record is the worst outcome). A sustained slowdown on a national-CERT host shows up as `fetch_failures` for that source on the Ops dashboard, not as a missed run.
- **Stream timeout.** Entry files are small — one `Write` per entry is safe. Long files (a run record with many findings) use the skeleton-then-`Edit` pattern, and the prompts cap file writes per assistant turn, to dodge stream-idle timeouts.
- **Network proxy staleness.** The routine container's git proxy mirrors github.com on a schedule, not per-pull, so the routine's local view of `origin/main` may be a few minutes stale. The auto-merge workflow runs the same merge logic against the live tip; this is the safety net.

---

## When something goes wrong

| Symptom | First thing to check |
|---|---|
| Routine fired but no commit on the feature branch | Routine container died mid-run. Check the routine's run log in claude.ai. The next fire self-heals: its gap-derived window covers everything the dead run missed. |
| A fire happened but there is no run record under `runs/` | The worst outcome — the prompts write the run record even on zero-entry runs and sub-agent failures. Check the claude.ai run log for a crash before Phase 4; if the branch pushed partially, the auto-merge may still have landed entries without a record — `python3 tools/check_run.py --all` will flag the orphans. |
| `tools/check_run.py` FAILs blocking a commit | See [`prompts/check-run-fixes.md`](../prompts/check-run-fixes.md) — every common FAIL has a fix recipe keyed to the checker's output labels. |
| `dedup` FAIL — a new entry shares CVE ids with prior coverage | The run tried to publish a repeat as a fresh entry. Correct outcome: re-ship as `update_of: <original entry id>` with only the delta, or drop it. The prior-coverage index (`work/<run-id>/prior_coverage.json`) names the conflicting entry. |
| Push succeeded but auto-merge workflow didn't run | GitHub Actions outage or `workflow_run` concurrency conflict. Check **Actions** → **Auto-merge claude/\* branches to main**; manually trigger via `workflow_dispatch` with the branch name. |
| Auto-merge ran but failed loud (`::error::`) | A merge conflict outside the auto-resolved paths (`state/*.json`, `entities/registry.yaml`, `sources/sources.json`). Workflow logs name the conflicting file; resolve manually and re-trigger. Entry/run-record paths are per-run unique and never conflict. |
| Auto-merge succeeded but `https://ctipilot.ch/` is stale | `deploy-site.yml` failure. Check **Actions** → **Deploy GitHub Pages site**. Common causes: vendored-library SHA mismatch, taxonomy validation failure, smoke-test failure. The run's Phase 7 reports this as `publish: main-only`. |
| Custom domain stops resolving (`ctipilot.ch` fails) | The `CNAME` file at the repo root may have been removed. Restore it (single line: `ctipilot.ch`) and re-deploy. GitHub Pages → repo Settings → Pages should show the custom domain populated. |
