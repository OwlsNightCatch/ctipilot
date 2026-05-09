# CLAUDE.md — ctipilot.ch repo conventions

This file is loaded into every Claude Code session in this repo (interactive or routine). Keep it short — the master prompts in `prompts/` are the source of truth for the daily / weekly brief routines.

## What this repo is

Autonomous CTI newsletter for a Swiss federal SOC. A scheduled Claude Code routine reads `prompts/daily-cti-brief.md` (or `prompts/weekly-summary.md`) on each fire, researches that day's threat landscape via parallel sub-agents, writes `briefs/YYYY-MM-DD.md`, updates state under `state/`, and publishes via the feature-branch + auto-merge chain. The static site at `https://ctipilot.ch/` is rebuilt by `.github/workflows/deploy-site.yml` on every push to `main` that touches the brief feed.

Audience is Tier 2/3 IR, threat hunters, detection engineers — assume MITRE ATT&CK fluency, no executive hedging, no IOCs, no vanity metrics.

## Project memory — version-controlled auto-memory

Auto-memory is **enabled** (`autoMemoryEnabled: true` in [`.claude/settings.json`](.claude/settings.json)) and **redirected to a repo-local directory** so memory persists across cloud routine fires (fresh container each run), across local Claude Code sessions on different machines, and across worktrees.

How it works:

- **Storage:** `.claude/memory/` in the repo (committed to git). [`.claude/memory/MEMORY.md`](.claude/memory/MEMORY.md) is the index — auto-loaded into every session by Claude Code's auto-memory feature (first 200 lines / 25 KB). Topic files in the same directory load on demand.
- **Redirect mechanism:** [`.claude/hooks/setup-memory.sh`](.claude/hooks/setup-memory.sh) runs on `SessionStart`. It computes the project hash the same way Claude Code does (replace `/`, `_`, `.` in `$PWD` with `-`) and symlinks `~/.claude/projects/<project-hash>/memory` → `<repo>/.claude/memory`. Idempotent; logs to stderr only on the first run.
- **First local run:** Claude Code prompts to approve the hook. Approve once — the approval persists for that machine. Existing local-only memory files (from before the symlink) are migrated into `.claude/memory/` automatically and the original directory is moved aside as `*.local-backup-<timestamp>`.
- **Cloud routine:** the hook runs in the routine container the same way. Memory writes land in the cloned repo. Phase 5 (daily) / Phase 4 (weekly) commits `.claude/memory/` alongside `state/` files. The next routine fire — fresh container, fresh symlink, repo cloned fresh from `main` — sees the accumulated memory.
- **Use it normally:** the `/memory` command, "remember that..." prompts, and Claude's automatic note-taking all work as documented. The only difference is *where* the files live.
- **Fallback if the hook fails:** if the symlink doesn't get created (Claude Code version mismatch, hook approval declined, container restriction), Claude can still read and write `.claude/memory/` directly using `Read` / `Write` / `Edit`. Memory persistence still works; only the `/memory` command and the auto-loading behaviour are lost.

Commit the memory dir alongside other state. The daily prompt's Phase 5 git-add and the weekly prompt's Phase 4 git-add both include `.claude/memory/`.

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
       :  # success path — script exits 0 from the no-op
   else
       echo "push: feature-branch push failed after 3 attempts"
       exit 1
   fi
   ```

   Push the **feature branch only**. Retry up to 3× with backoff for transient transport failures. The `if/else` ending matters: a tail like `[ "$PUSH_OK" != "true" ] && echo "..."` exits 1 in the success case (the test "true != true" is false → exit 1, and `&&` propagates that), which makes the harness flag a successful push as a failed background task. Use the explicit `if/else` shape above.

4. **Auto-merge takes it from there.** Every push to a `claude/**` branch fires [`.github/workflows/auto-merge-claude.yml`](.github/workflows/auto-merge-claude.yml) on a github-hosted runner, which:
   - Fast-forwards `main` if the feature branch is a strict descendant (common case when step 1's sync was clean).
   - Detects "already merged" if the feature branch is an ancestor of `main`, and just deletes the branch.
   - On a true divergence, attempts a regular merge and applies the **same auto-resolution rules** as the routine (state/* → `--ours`, `sources/sources.json` → `--theirs`) before pushing `main`. The workflow runs against the live github.com tip, so it catches any race the routine's local clone missed.
   - Deletes the feature branch on success. Any remaining conflict outside the auto-resolved paths fails loud with an `::error::` annotation in the workflow logs so the operator notices.

5. **Phase 7 (daily) / Phase 6 (weekly) — verify the brief actually landed.** Poll `git fetch origin main && git cat-file -e origin/main:<brief-path>` until the brief lands (10-min budget). Then poll `https://ctipilot.ch/` until the deploy-site workflow has rebuilt gh-pages. Report `publish: ok` / `main-only` / `pending (<reason>)` from the actual poll result, not from a guess. **A pushed feature branch is not a published brief** — the verification step is what confirms the auto-merge action and the deploy-site action both succeeded. The polling path is the **only** verification path the routine and Claude Code on the Web have available — see the next paragraph.

   **`gh` is for local interactive sessions only.** The Anthropic-managed cloud routine container and Claude Code on the Web do **not** ship `gh` and have no GitHub credentials configured. **The cloud routine and Claude Code on the Web MUST use the polling path above and MUST NOT attempt `gh`** — there is no fallback path that magically works there; `gh` will fail or exit 127 (command not found). The routine relies on `git cat-file` for "did the brief land on main" and `curl https://ctipilot.ch/` for "did the site rebuild". That's the contract.

   In a **local interactive session** where `gh` is on PATH **and** authenticated (`gh auth status` exits 0), it gives you the *why* when polling can't. Use it as a diagnostic supplement, not a replacement, after the polling path has signalled `main-only` or `pending (<reason>)`:

   ```bash
   # ONLY run this in a local interactive session that you know has gh authenticated.
   # The cloud routine and Claude Code on the Web must skip this entire block.
   if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
       current_branch=$(git rev-parse --abbrev-ref HEAD)
       head_sha=$(git rev-parse HEAD)

       # Wait for the auto-merge run that was triggered by THIS push (matched by head SHA),
       # not whichever run is most recent on the branch — concurrent pushes race.
       run_id=""
       for _ in $(seq 1 30); do                # ~10 min budget at 20 s interval
           run_id=$(gh run list \
               --workflow auto-merge-claude.yml \
               --branch "$current_branch" \
               --limit 5 \
               --json databaseId,headSha,status,conclusion \
               --jq ".[] | select(.headSha == \"$head_sha\") | .databaseId" | head -1)
           [ -n "$run_id" ] && break
           sleep 20
       done

       if [ -n "$run_id" ]; then
           if gh run watch "$run_id" --exit-status; then
               echo "auto-merge: ok (run $run_id)"
           else
               echo "auto-merge: failed — fetching logs"
               gh run view "$run_id" --log-failed | tail -100
           fi
       else
           echo "auto-merge: no run found for $head_sha within budget"
       fi

       # Recent deploy-site runs on main, for diagnosing site staleness.
       gh run list --workflow deploy-site.yml --branch main --limit 3 \
           --json databaseId,headSha,status,conclusion,createdAt | head -50
   fi
   ```

   The `gh` path surfaces three failure modes the polling path can't distinguish:
   - Auto-merge ran but failed loud with `::error::` (conflict outside the auto-resolved paths) → `git fetch` keeps returning "brief not on main" without any signal *why*.
   - Auto-merge succeeded but deploy-site failed (vendored-library hash mismatch, taxonomy validation, smoke test) → `curl https://ctipilot.ch/` polling will time out without telling you it was the build, not the merge.
   - The workflow didn't fire at all (concurrency conflict, GitHub Actions outage) → both polls return nothing useful.

   `gh run view --log-failed` gives the actual error in seconds. Use it whenever you have it locally.

## Hard "do nots"

- **Never push directly to `main`.** Repo policy. The feature-branch + auto-merge chain above is the only supported path. Direct `git push origin HEAD:main` is forbidden — see daily prompt § Phase 6.
- **Never put IOCs in a brief.** No SHA hashes, no IPs, no attacker domains, no YARA/Sigma/Suricata. The brief is *knowledge* — TTPs, campaigns, vulnerabilities, detection concepts.
- **Never `WebFetch` CISA / NCSC.ch directly.** Both reliably 403 the routine UA. Use `python3 tools/fetch_source.py` (`cisa-kev`, `ncsc-csh recent N`, `url <URL>`). Also applies to CSIRT Italia, UK ICO, Inside IT, PRODAFT, NCC Group, occasionally Cisco Talos. The bridge enforces a host allow-list and forwards a desktop-Chrome UA.
- **Never call `WebFetch` without the outbound-links template.** The default summariser drops every URL — without an explicit "Outbound links" ask, you get prose with no citation chain and the news → primary pivot collapses. Template lives in `.claude/agents/cti-research.md` and `.claude/agents/cti-verification.md` — copy verbatim.
- **Never cite a homepage, listing index, news category, or NVD/MITRE per-CVE page as a Source.** `tools/check_brief.py` FAILs the commit on these patterns. Use the specific article / advisory / vendor PSIRT URL.
- **Never skip `tools/check_brief.py` before commit.** Phase 5.5 (daily) / Phase 4.5 (weekly). Exit 0 required. Drift is what *you* fix — the script is read-only.
- **Never block the brief on a sub-agent.** Stalled (>10 min) sub-agents are abandoned, not waited on. Late + short + partial is fine. **Failing to write a brief is the worst outcome** — operator can't tell if the run failed or nothing happened.

## Operational guardrails

- **Skeleton-then-Edit (also applies to docs / prompts / build code, not just briefs).** A single `Write` of any large file — or a long sequence of large `Edit`s in one assistant turn — trips `Stream idle timeout — partial response received` and silently drops the rest of the turn. **Empirical limit: anywhere past ~6–8 substantial `Edit` calls in a single response is risky; a single `Write` of >300 lines is risky.** Two shapes that work: (1) for new files, `Write` a placeholder skeleton (`_(no content yet)_`) → `Read` it back → `Edit` each section in turn (one Edit per section, split long sections in half); (2) for refactors that touch many files, batch ~5 small `Edit`s per turn, then yield with a one-sentence progress update before the next batch. The user can interrupt; a stream-idle timeout cannot be recovered from.
- **Persist intermediate state often** under `work/<run-id>/<step>.json` (gitignored). After every meaningful unit of work — every fetched source summarised, every CVE enriched, every section drafted — write the partial result so a later step can resume.
- **One new candidate source per run, maximum.** Sub-agents surface candidates; the main agent writes them as `status: "candidate"` in `sources/sources.json` during Phase 5.
- **Verification loop is non-negotiable but never blocks publish.** Phase 4.5 (daily) / Phase 3.5 (weekly) spawns `cti-verification`. Iteration 1 always runs. If verdict NEEDS_FIXES, apply remediations and re-spawn fresh (no shared memory). Hard cap 3 iterations. Iteration 3 still NEEDS_FIXES → publish anyway with residuals logged in § Verification Notes.

## Where things live

```
prompts/daily-cti-brief.md       # daily routine master prompt
prompts/weekly-summary.md        # weekly routine master prompt
prompts/CHANGELOG.md             # editorial-policy audit trail (bump version on every edit)
prompts/verification.md          # fake-news / two-source verification policy (the prompt enforces it)
prompts/brief-template.md        # canonical Markdown skeleton for the rendered brief / weekly
prompts/check-brief-fixes.md     # how to fix common check_brief.py FAILs
.claude/agents/cti-research.md   # research sub-agent definition (Sonnet)
.claude/agents/cti-verification.md  # verification sub-agent definition (Sonnet)
.claude/memory/                  # version-controlled auto-memory (MEMORY.md + topic files)
.claude/hooks/setup-memory.sh    # SessionStart hook — symlinks system auto-memory dir to .claude/memory/
.claude/settings.json            # project settings: autoMemoryEnabled, SessionStart hook
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
docs/operating.md                # operator runbook (setup, ops dashboard, troubleshooting)
docs/analytics.md                # public-facing privacy disclosure
docs/improvements.md             # open backlog
work/<run-id>/                   # gitignored intermediate state
```

## Editing the master prompts — versioning rule (ALWAYS)

Any edit to `prompts/daily-cti-brief.md`, `prompts/weekly-summary.md`, `prompts/verification.md`, `prompts/brief-template.md`, `prompts/check-brief-fixes.md`, `.claude/agents/cti-research.md`, or `.claude/agents/cti-verification.md` **must** ship with all three of these in the same commit (banner bump + CHANGELOG entry + the file edit itself). Skipping any of them produces silent drift between what the routine actually loaded, what the brief footer claims, and what the changelog records.

Edits to `CLAUDE.md`, `docs/`, `tools/`, or `site/` only require a prompt bump when they materially change runtime behaviour (a new tool the prompt should mention, a new convention the prompt should enforce, a new file the prompt should commit). Pure clarifications, reformatting, and ops-doc updates do not.

1. **Bump the version banner in the prompt file itself.** Both master prompts open with `> **Prompt version:** vN.M …`. Edit that string to the next version. The daily and weekly are versioned in lockstep — when one bumps, bump the other to match (even when only one was edited substantively) so the operator's `state/run_log.json.prompt_version` is unambiguous across runs.

2. **Add a new top entry to [`prompts/CHANGELOG.md`](prompts/CHANGELOG.md).** Format:

   ```markdown
   ## N.M — YYYY-MM-DD (one-line headline of what changed)

   ### Why
   <1–3 sentences: what problem this edit solves, what concrete pain or incident
   prompted it. Avoid restating what changed; that's the next section.>

   ### What changed
   <per-file bullets — name the file, name the section, name the diff in
   plain English. Include any operator-visible behaviour changes
   (cost shifts, new prompts, breaking config requirements).>

   ### What stays
   <one short paragraph naming the hard invariants and prior-version features
   the edit preserves, so the diff isn't read as "everything was rewritten".>
   ```

   The CHANGELOG is the editorial-policy audit trail — every entry is the only place that explains *why* a behaviour shifted between two committed briefs. **No silent bumps.**

3. **Carry the new version through the brief footer and the run log.** The next brief's `**Prompt:** vN.M` line and `state/run_log.json.prompt_version` field both read from the prompt's banner — no extra step required if step 1 is done correctly. Phase 5.5's `tools/check_brief.py` cross-checks the footer banner against `prompts/CHANGELOG.md`'s most recent heading; a mismatch FAILs the commit, which is the safety net catching skipped step-1 or step-2 edits.


## Self-evolution

The routine has full authority to modify `prompts/`, `docs/`, `sources/sources.json`, `state/*.json`, `.claude/agents/`, `.claude/memory/`, `site/taxonomy.yaml`, and `tools/`. Every change appears in the commit diff for after-the-fact review. Hard invariants (AI-content notice, no IOCs, two-source verification with national-CERT carve-out, English output, feature-branch-only publishing chain, Phase 4.5 verification loop, Phase 5.5 self-check gate, per-item metadata footer using taxonomy values) **must not** be removed or weakened — surface concerns in § Verification Notes instead.
