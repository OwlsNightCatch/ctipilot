# CLAUDE.md — ctipilot.ch repo conventions

This file is loaded into every Claude Code session in this repo (interactive or routine). Keep it short — the master prompts in `prompts/` are the source of truth for the daily / weekly brief routines.

## What this repo is

Autonomous CTI newsletter for a Swiss federal SOC. A scheduled Claude Code routine reads `prompts/daily-cti-brief.md` (or `prompts/weekly-summary.md`) on each fire, researches that day's threat landscape via parallel sub-agents, writes `briefs/YYYY-MM-DD.md`, updates state under `state/`, and publishes via the feature-branch + auto-merge chain. The static site at `https://ctipilot.ch/` is rebuilt by `.github/workflows/deploy-site.yml` on every push to `main` that touches the brief feed.

Audience is Tier 2/3 IR, threat hunters, detection engineers — assume MITRE ATT&CK fluency, no executive hedging, no IOCs, no vanity metrics.

## Custom sub-agents (`.claude/agents/`)

The routine delegates to two custom sub-agents — both Sonnet, isolated context, clear remits:

- **`cti-research`** — Phase 1 (daily) / Phase 2 (weekly) parallel research workers. Spawn one per domain (S1–S4 daily, W1–W2 weekly). Pivots from news to primary sources, returns verified items with full discovery traces. **Definition: [.claude/agents/cti-research.md](.claude/agents/cti-research.md).**
- **`cti-verification`** — Phase 4.5 (daily) / Phase 3.5 (weekly) cold-reader verifier. Read-only — main agent owns all edits. Looped iteratively: spawn fresh on every iteration (no shared memory) until verdict CLEAN or 3-iteration cap. **Definition: [.claude/agents/cti-verification.md](.claude/agents/cti-verification.md).**

The main agent (Opus by default) does composition, state update, commit, sync, push, publish-verification. Sub-agents are Sonnet so they can run with their own large context windows in parallel without burning the main agent's budget. Never spawn `general-purpose` for research or verification — use the named sub-agents so the operator gets the right model + tool set.

## Branching and publishing — feature branch only, auto-merge promotes to main

Every Claude Code session in this repo (interactive or routine) operates on a `claude/<adjective>-<name>-<id>` feature branch. **`main` is owned by `.github/workflows/auto-merge-claude.yml`** — only that workflow promotes commits onto `main`. The full lifecycle:

1. **At session start — always pull the freshest `main` before doing any work.** The routine container's clone may be stale (the local git proxy mirrors github.com on a schedule, not per-pull) and another routine or operator commit may have landed on `main` since the worktree was created. Run:

   ```bash
   git fetch origin main
   git merge --no-edit -m "sync: pull origin/main at session start" origin/main
   ```

   If the merge conflicts on `state/cves_seen.json`, `state/covered_items.json`, `state/run_log.json`, `state/deep_dive_history.json`, or `sources/sources.json`, apply the same auto-resolution rules the workflow uses (see daily prompt § Phase 6 step 2): state/* → `--ours`, `sources/sources.json` → `--theirs`, anything else → surface to the operator.

2. **Throughout the session — work on the feature branch only.** Never check out `main`, never push to `main`, never `git push origin HEAD:main`. Repo policy on the `main-protect` ruleset blocks force-push and non-fast-forward; direct push by the routine's GitHub App may also be rejected by branch protection.

3. **At session end — commit and push the feature branch.** After Phase 5 / Phase 5.5 (or, in interactive sessions, after the work is reviewed):

   ```bash
   current_branch=$(git rev-parse --abbrev-ref HEAD)        # claude/<adjective>-<name>-<id>
   git add <specific files — never `git add -A`>
   git commit -m "<descriptive message>"
   git fetch origin main && git merge --no-edit origin/main # second sync — main may have advanced
   for attempt in 1 2 3; do
       git push origin "$current_branch" && break
       sleep $((attempt * 5))
   done
   ```

   Push the **feature branch only**. Retry up to 3× with backoff for transient transport failures.

4. **Auto-merge takes it from there.** Every push to a `claude/**` branch fires [`.github/workflows/auto-merge-claude.yml`](.github/workflows/auto-merge-claude.yml) on a github-hosted runner, which:
   - Fast-forwards `main` if the feature branch is a strict descendant (common case when step 1's sync was clean).
   - Detects "already merged" if the feature branch is an ancestor of `main`, and just deletes the branch.
   - On a true divergence, attempts a regular merge and applies the **same auto-resolution rules** as the routine (state/* → `--ours`, `sources/sources.json` → `--theirs`) before pushing `main`. The workflow runs against the live github.com tip, so it catches any race the routine's local clone missed.
   - Deletes the feature branch on success. Any remaining conflict outside the auto-resolved paths fails loud with an `::error::` annotation in the workflow logs so the operator notices.

5. **Phase 7 (daily) / Phase 6 (weekly) — verify the brief actually landed.** Poll `git fetch origin main && git cat-file -e origin/main:<brief-path>` until the brief lands (10-min budget). Then poll `https://ctipilot.ch/` until the deploy-site workflow has rebuilt gh-pages. Report `publish: ok` / `main-only` / `pending (<reason>)` from the actual poll result, not from a guess. **A pushed feature branch is not a published brief** — the verification step is what confirms the auto-merge action and the deploy-site action both succeeded.

## Hard "do nots"

- **Never push directly to `main`.** Repo policy. The feature-branch + auto-merge chain above is the only supported path. Direct `git push origin HEAD:main` is forbidden — see daily prompt § Phase 6.
- **Never put IOCs in a brief.** No SHA hashes, no IPs, no attacker domains, no YARA/Sigma/Suricata. The brief is *knowledge* — TTPs, campaigns, vulnerabilities, detection concepts.
- **Never `WebFetch` CISA / NCSC.ch directly.** Both reliably 403 the routine UA. Use `python3 tools/fetch_source.py` (`cisa-kev`, `ncsc-csh recent N`, `url <URL>`). Also applies to CSIRT Italia, UK ICO, Inside IT, PRODAFT, NCC Group, occasionally Cisco Talos. The bridge enforces a host allow-list and forwards a desktop-Chrome UA.
- **Never call `WebFetch` without the outbound-links template.** The default summariser drops every URL — without an explicit "Outbound links" ask, you get prose with no citation chain and the news → primary pivot collapses. Template lives in `.claude/agents/cti-research.md` and `.claude/agents/cti-verification.md` — copy verbatim.
- **Never cite a homepage, listing index, news category, or NVD/MITRE per-CVE page as a Source.** `tools/check_brief.py` FAILs the commit on these patterns. Use the specific article / advisory / vendor PSIRT URL.
- **Never skip `tools/check_brief.py` before commit.** Phase 5.5 (daily) / Phase 4.5 (weekly). Exit 0 required. Drift is what *you* fix — the script is read-only.
- **Never block the brief on a sub-agent.** Stalled (>10 min) sub-agents are abandoned, not waited on. Late + short + partial is fine. **Failing to write a brief is the worst outcome** — operator can't tell if the run failed or nothing happened.

## Operational guardrails

- **Skeleton-then-Edit.** A single `Write` of the whole brief trips `Stream idle timeout — partial response received`. `Write` skeleton with `_(no content yet)_` placeholders → `Read` it back → `Edit` each section in turn (one Edit per section). Split long sections into halves.
- **Persist intermediate state often** under `work/<run-id>/<step>.json` (gitignored). After every meaningful unit of work — every fetched source summarised, every CVE enriched, every section drafted — write the partial result so a later step can resume.
- **One new candidate source per run, maximum.** Sub-agents surface candidates; the main agent writes them as `status: "candidate"` in `sources/sources.json` during Phase 5.
- **Verification loop is non-negotiable but never blocks publish.** Phase 4.5 (daily) / Phase 3.5 (weekly) spawns `cti-verification`. Iteration 1 always runs. If verdict NEEDS_FIXES, apply remediations and re-spawn fresh (no shared memory). Hard cap 3 iterations. Iteration 3 still NEEDS_FIXES → publish anyway with residuals logged in § Verification Notes.

## Where things live

```
prompts/daily-cti-brief.md       # daily routine master prompt
prompts/weekly-summary.md        # weekly routine master prompt
prompts/CHANGELOG.md             # editorial-policy audit trail (bump version on every edit)
.claude/agents/cti-research.md   # research sub-agent definition (Sonnet)
.claude/agents/cti-verification.md  # verification sub-agent definition (Sonnet)
sources/sources.json             # ~80 curated CTI sources (autonomous lifecycle)
state/covered_items.json         # rolling coverage log
state/cves_seen.json             # flat CVE index
state/deep_dive_history.json     # 30-day deep-dive picks (rotation memory)
state/run_log.json               # per-run telemetry (Ops dashboard at /ops/)
briefs/YYYY-MM-DD.md             # daily output
briefs/weekly/YYYY-Www.md        # weekly output
tools/fetch_source.py            # bridge fetcher for known-403 hosts
tools/check_brief.py             # institutionalised self-check (single command, must exit 0)
site/                            # static-site generator + assets (stdlib-only)
site/taxonomy.yaml               # controlled vocabulary for footers (build refuses unknown values)
docs/architecture.md             # end-to-end map of what reads/writes what
docs/workflow.md                 # daily + weekly agent process
docs/verification.md             # fake-news verification policy
docs/brief-template.md           # canonical Markdown skeleton for the rendered brief
docs/check-brief-fixes.md        # how to fix common check_brief.py FAILs
work/<run-id>/                   # gitignored intermediate state
```

## Self-evolution

The routine has full authority to modify `prompts/`, `docs/`, `sources/sources.json`, `state/*.json`, `.claude/agents/`, `site/taxonomy.yaml`, and `tools/`. Every change appears in the commit diff for after-the-fact review. Hard invariants (AI-content notice, no IOCs, two-source verification with national-CERT carve-out, English output, feature-branch-only publishing chain, Phase 4.5 verification loop, Phase 5.5 self-check gate, per-item metadata footer using taxonomy values) **must not** be removed or weakened — surface concerns in § Verification Notes instead.

When editing the master prompts, bump `prompts/CHANGELOG.md` in the same commit and carry the new version through the brief footer (`**Prompt:** vN.M`) and `state/run_log.json.prompt_version`.
