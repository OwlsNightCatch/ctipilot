# CLAUDE.md — ctipilot.ch repo conventions

Loaded into every Claude Code session here (interactive or routine). The master prompts under `prompts/` are the source of truth for the daily / weekly brief routines — this file only carries cross-cutting rules every session needs.

## What this repo is

Autonomous CTI newsletter for a Swiss federal SOC. A scheduled Claude Code routine reads `prompts/daily-cti-brief.md` (or `prompts/weekly-summary.md`) on each fire, researches that day's threat landscape via parallel sub-agents, writes `briefs/YYYY-MM-DD.md`, updates state under `state/`, and publishes via the feature-branch + auto-merge chain. The static site at [https://ctipilot.ch/](https://ctipilot.ch/) rebuilds on every push to `main` that touches the brief feed.

Audience is Tier 2/3 IR / threat hunters / detection engineers — assume MITRE ATT&CK fluency, no executive hedging, no IOCs, no vanity metrics.

For an end-to-end map of what reads / writes what, see [docs/architecture.md](docs/architecture.md). For the operator runbook see [docs/operating.md](docs/operating.md).

## Key commands (verify before claiming a task is done)

| Goal | Command |
|---|---|
| Phase 5.5 self-check on today's brief | `python3 tools/check_brief.py` |
| Run check on a specific brief | `python3 tools/check_brief.py briefs/YYYY-MM-DD.md` |
| Build the static site (smoke test for any `site/` change) | `python3 site/build.py` |
| Stdlib-only smoke tests for build helpers | `python3 site/test_build.py` |
| Bridge fetcher for known-403 hosts | `python3 tools/fetch_source.py {cisa-kev \| ncsc-csh recent N \| url <URL>}` |

`tools/check_brief.py` MUST exit 0 before any commit on a brief. The script is read-only; drift is what *you* fix.

## Hard rules — ALWAYS / NEVER

- **ALWAYS commit `.claude/memory/` changes on every session that touches it.** IMPORTANT — auto-memory is **enabled** and persisted under `.claude/memory/` (committed to git). Every routine fire spawns a fresh container that clones the repo from `main`; any memory written but not committed is silently lost on the next fire. If a session calls `/memory`, accepts a "remember that…" prompt, or writes any topic file under `.claude/memory/`, the session's commit MUST `git add .claude/memory/` alongside whatever other state it changed. The publishing chain (feature branch → auto-merge → `main`) handles the push automatically once it's committed. **Memory that doesn't reach `main` did not happen.**
- **NEVER push directly to `main`.** Repo policy. The feature-branch + auto-merge chain below is the only supported path.
- **NEVER put IOCs in a brief.** No SHA hashes, no IPs, no attacker domains, no YARA / Sigma / Suricata. The brief is *knowledge* — TTPs, campaigns, vulnerabilities, detection concepts.
- **NEVER `WebFetch` CISA / NCSC.ch directly** — both reliably 403 the routine UA. Same for CSIRT Italia, UK ICO, Inside IT, PRODAFT, NCC Group, occasionally Cisco Talos. Use `python3 tools/fetch_source.py` (host allow-list + desktop-Chrome UA).
- **NEVER call `WebFetch` without the outbound-links template.** The default summariser drops every URL; without an explicit "Outbound links" ask the news → primary pivot collapses. Template lives verbatim in `.claude/agents/cti-research.md` and `.claude/agents/cti-verification.md`.
- **NEVER cite a homepage, listing index, news category, or NVD/MITRE per-CVE page as a Source.** `tools/check_brief.py` FAILs the commit on these patterns. Use the specific article / advisory / vendor PSIRT URL.
- **NEVER skip `tools/check_brief.py` before commit.** Phase 5.5 (daily) / Phase 4.5 (weekly). Exit 0 required.
- **NEVER block the brief on a sub-agent.** Stalled (>10 min) sub-agents are abandoned, not waited on. Late + short + partial is fine. **Failing to write a brief is the worst outcome** — operator can't tell if the run failed or nothing happened.

## Auto-memory mechanics (only what's non-obvious)

- **Storage:** `.claude/memory/MEMORY.md` is the index (auto-loaded into every session, first 200 lines / 25 KB). Topic files in the same dir load on demand. The `/memory` command, "remember that…" prompts, and Claude's automatic note-taking all work as documented — only difference is the files live in the repo.
- **Redirect mechanism:** [`.claude/hooks/setup-memory.sh`](.claude/hooks/setup-memory.sh) symlinks `~/.claude/projects/<project-hash>/memory` → `<repo>/.claude/memory/` on `SessionStart`. Idempotent. The hook self-documents.
- **Fallback:** if the symlink isn't created (hook approval declined, container restriction), Claude can still `Read` / `Write` / `Edit` `.claude/memory/` directly. Persistence still works; only the `/memory` command and the auto-loading behaviour are lost.
- **First local run** prompts to approve the hook once per machine. Pre-existing local-only memory is migrated into `.claude/memory/` and the original dir moved aside as `*.local-backup-<timestamp>`.

## Custom sub-agents (`.claude/agents/`)

Two named sub-agents — both isolated context, model bound by their YAML frontmatter (operator-rebindable):

- **`cti-research`** — Phase 1 (daily) / Phase 2 (weekly) parallel research workers. One per domain (S1–S4 daily, W1–W2 weekly). Pivots from news to primary sources, returns verified items with full discovery traces. Opens its return with a mandatory `**Model:**` self-identification line. Definition: [.claude/agents/cti-research.md](.claude/agents/cti-research.md).
- **`cti-verification`** — Phase 4.5 (daily) / Phase 3.5 (weekly) cold-reader verifier. Read-only — main agent owns all edits. Looped iteratively, fresh spawn each iteration (no shared memory) until verdict CLEAN or 3-iteration cap. Same self-identification contract. Definition: [.claude/agents/cti-verification.md](.claude/agents/cti-verification.md).

The main agent does composition, state update, commit, sync, push, publish-verification. Main agent and sub-agents may run on different models — the runtime decides per role and every agent self-identifies in its output. The prompts deliberately give no example model name so the agents reason about their own identity instead of pattern-matching a placeholder. **NEVER spawn `general-purpose` for research or verification** — use the named sub-agents so the operator gets the right tool set + model binding.

## Branching and publishing — feature branch only

Every session here (interactive or routine) operates on a `claude/<adjective>-<name>-<id>` feature branch. **`main` is owned by [`.github/workflows/auto-merge-claude.yml`](.github/workflows/auto-merge-claude.yml)** — that workflow is the only thing that promotes commits onto `main`.

**1. Session start — pull the freshest `main` before doing any work.** The routine container's clone may be stale (the local git proxy mirrors github.com on a schedule, not per-pull) and another routine or operator commit may have landed since the worktree was created. Run:

```bash
git fetch origin main
git merge --no-edit -m "sync: pull origin/main at session start" origin/main
```

Conflicts on `state/cves_seen.json`, `state/covered_items.json`, `state/run_log.json`, `state/deep_dive_history.json`, or `sources/sources.json` resolve via the same auto-rules the workflow uses (state/* → `--ours`, `sources/sources.json` → `--theirs`); anything else surfaces to the operator.

**2. Throughout the session — feature branch only.** Never check out `main`, never push to `main`, never `git push origin HEAD:main`. Repo policy on `main-protect` blocks force-push and non-fast-forward; the routine's GitHub App is also rejected by branch protection on direct push.

**3. Session end — stage specifics (never `git add -A`), commit, sync again, push the feature branch with retry.** **Always include `.claude/memory/` in the stage list when memory was touched.**

```bash
current_branch=$(git rev-parse --abbrev-ref HEAD)
git add <specific files — including .claude/memory/ when modified>
git commit -m "<descriptive message>"
git fetch origin main && git merge --no-edit origin/main   # second sync — main may have advanced

PUSH_OK=false
for attempt in 1 2 3; do
    if git push origin "$current_branch"; then
        PUSH_OK=true
        echo "push: ok (feature branch)"
        break
    fi
    echo "push attempt ${attempt} failed; retrying in $((attempt * 5))s"
    sleep $((attempt * 5))
done
if [ "$PUSH_OK" = "true" ]; then
    :
else
    echo "push: feature-branch push failed after 3 attempts"
    exit 1
fi
```

The explicit `if/else` matters: the tail shape `[ "$PUSH_OK" != "true" ] && echo "..."` exits 1 in the **success** case (test "true != true" is false → exit 1, `&&` propagates), which makes the harness flag a successful push as a failed background task. Use the shape above.

**4. Auto-merge takes it from there.** Every push to a `claude/**` branch fires the workflow on a github-hosted runner, which fast-forwards `main` if the feature branch is a strict descendant, applies the same auto-resolution rules on a true divergence, and deletes the feature branch on success. Conflicts outside the auto-resolved paths fail loud with `::error::` annotations.

**5. Publish verification (Phase 7 daily / Phase 6 weekly).** Poll `git fetch origin main && git cat-file -e origin/main:<brief-path>` until the brief lands (10-min budget), then poll `https://ctipilot.ch/` until the deploy-site workflow rebuilt gh-pages. Report `publish: ok` / `main-only` / `pending (<reason>)` from the actual poll, not a guess. **A pushed feature branch is not a published brief** — verification is what confirms both the auto-merge action and the deploy-site action succeeded.

**`gh` is for local interactive sessions only.** The Anthropic-managed cloud routine container and Claude Code on the Web do **not** ship `gh` and have no GitHub credentials configured. **The cloud routine and Claude Code on the Web MUST use the polling path above and MUST NOT attempt `gh`** — `gh` will exit 127. In a local session where `gh auth status` exits 0, use `gh run list / watch / view --log-failed` against `auto-merge-claude.yml` and `deploy-site.yml` filtered by your push's head SHA — that surfaces the *why* (auto-merge conflict, deploy build failure, workflow didn't fire) when polling alone can't distinguish those. Match runs by head SHA, not branch tip, since concurrent pushes race.

## Operational guardrails

- **Skeleton-then-Edit (applies to docs / prompts / build code, not just briefs).** A single `Write` of any large file — or a long sequence of large `Edit`s in one assistant turn — trips `Stream idle timeout — partial response received` and silently drops the rest of the turn. Empirical limit: past ~6–8 substantial `Edit` calls in a single response is risky; a single `Write` of >300 lines is risky. Two shapes that work: (1) for new files, `Write` a placeholder skeleton (`_(no content yet)_`) → `Read` it back → `Edit` each section in turn; (2) for refactors that touch many files, batch ~5 small `Edit`s per turn, then yield with a one-sentence progress update before the next batch. A stream-idle timeout cannot be recovered from — the user can interrupt; that hang cannot.
- **Persist intermediate state often** under `work/<run-id>/<step>.json` (gitignored). After every meaningful unit of work — every fetched source summarised, every CVE enriched, every section drafted — write the partial result so a later step can resume.
- **One new candidate source per run, maximum.** Sub-agents surface candidates; the main agent writes them as `status: "candidate"` in `sources/sources.json` during Phase 5.
- **Verification loop is non-negotiable but never blocks publish.** Phase 4.5 (daily) / Phase 3.5 (weekly) spawns `cti-verification`. Iteration 1 always runs. NEEDS_FIXES → apply remediations and re-spawn fresh. Cap 3 iterations. Iteration 3 still NEEDS_FIXES → publish anyway with residuals logged in § Verification Notes.

## Where things live

```
prompts/daily-cti-brief.md         # daily routine master prompt
prompts/weekly-summary.md          # weekly routine master prompt
prompts/CHANGELOG.md               # editorial-policy audit trail (bump on every prompt edit)
prompts/verification.md            # fake-news / two-source verification policy
prompts/brief-template.md          # canonical Markdown skeleton for the rendered brief / weekly
prompts/check-brief-fixes.md       # how to fix common check_brief.py FAILs
.claude/agents/cti-research.md     # research sub-agent definition
.claude/agents/cti-verification.md # verification sub-agent definition
.claude/memory/                    # version-controlled auto-memory — MUST be committed when touched
.claude/hooks/setup-memory.sh      # SessionStart hook — symlinks system auto-memory dir
.claude/settings.json              # autoMemoryEnabled, SessionStart hook
sources/sources.json               # ~80 curated CTI sources (autonomous lifecycle)
state/covered_items.json           # rolling coverage log
state/cves_seen.json               # flat CVE index
state/deep_dive_history.json       # 30-day deep-dive picks (rotation memory)
state/run_log.json                 # per-run telemetry — feeds the Ops dashboard at /ops/
briefs/YYYY-MM-DD.md               # daily output
briefs/weekly/YYYY-Www.md          # weekly output
tools/fetch_source.py              # bridge fetcher for known-403 hosts
tools/check_brief.py               # institutionalised self-check (single command, must exit 0)
site/build.py                      # static-site generator (stdlib-only)
site/taxonomy.yaml                 # controlled vocabulary for footers (build refuses unknown values)
docs/architecture.md               # end-to-end map of what reads/writes what
docs/operating.md                  # operator runbook
work/<run-id>/                     # gitignored intermediate state
```

## Editing the master prompts — versioning rule (ALWAYS)

Any edit to `prompts/daily-cti-brief.md`, `prompts/weekly-summary.md`, `prompts/verification.md`, `prompts/brief-template.md`, `prompts/check-brief-fixes.md`, `.claude/agents/cti-research.md`, or `.claude/agents/cti-verification.md` MUST ship all three of these in the same commit (banner bump + CHANGELOG entry + the file edit itself). Skipping any of them produces silent drift between what the routine actually loaded, what the brief footer claims, and what the changelog records.

Edits to `CLAUDE.md`, `docs/`, `tools/`, or `site/` only require a prompt bump when they materially change runtime behaviour. Pure clarifications, reformatting, and ops-doc updates do not.

1. **Bump the version banner** in the prompt itself (`> **Prompt version:** vN.M`). Daily and weekly versions move in lockstep — even if only one was edited substantively — so `state/run_log.json.prompt_version` is unambiguous across runs.
2. **Add a top entry to [`prompts/CHANGELOG.md`](prompts/CHANGELOG.md)** with `### Why`, `### What changed`, `### What stays` headings. The CHANGELOG is the editorial-policy audit trail and the only place that explains *why* a behaviour shifted between two committed briefs. **No silent bumps.**
3. **Carry the new version through the brief footer and run log.** Both read from the prompt's banner — no extra step if step 1 is correct. `tools/check_brief.py` cross-checks the footer banner against `prompts/CHANGELOG.md`'s most-recent heading and FAILs the commit on a mismatch (the safety net for skipped step-1 / step-2 edits).

## Self-evolution

The routine has full authority to modify `prompts/`, `docs/`, `sources/sources.json`, `state/*.json`, `.claude/agents/`, `.claude/memory/`, `site/taxonomy.yaml`, and `tools/`. Every change appears in the commit diff for after-the-fact review.

**Hard invariants that must NOT be removed or weakened** (surface concerns in § Verification Notes instead): AI-content notice, no IOCs, two-source verification with national-CERT carve-out, English output, feature-branch-only publishing chain, Phase 4.5 verification loop, Phase 5.5 self-check gate, per-item metadata footer using taxonomy values, memory commits.
