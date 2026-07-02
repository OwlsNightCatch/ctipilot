# CLAUDE.md — ctipilot.ch repo conventions

Loaded into every Claude Code session here (interactive or routine). The master prompts under `prompts/` are the source of truth for the daily / weekly brief routines — this file only carries cross-cutting rules every session needs.

## What this repo is

Autonomous CTI newsletter for a Swiss federal SOC (by default — the deployment is organization-parameterizable via `config/org-profile.yaml`, v2.65). A scheduled Claude Code routine reads `prompts/daily-cti-brief.md` (or `prompts/weekly-summary.md`) on each fire, researches that day's threat landscape via parallel sub-agents, writes `briefs/YYYY-MM-DD.md`, updates state under `state/`, and publishes via the feature-branch + auto-merge chain. The static site at [https://ctipilot.ch/](https://ctipilot.ch/) rebuilds on every push to `main` that touches the brief feed.

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
| Validate the org profile / re-render it into the prompts | `python3 tools/compose_prompts.py --check` / `--write` (also `--dump`, `--selftest`) |

`tools/check_brief.py` MUST exit 0 before any commit on a brief. The script is read-only; drift is what *you* fix.

## Hard rules — ALWAYS / NEVER

- **ALWAYS commit `.claude/memory/` changes on every session that touches it.** IMPORTANT — auto-memory is **enabled** and persisted under `.claude/memory/` (committed to git). Every routine fire spawns a fresh container that clones the repo from `main`; any memory written but not committed is silently lost on the next fire. If a session calls `/memory`, accepts a "remember that…" prompt, or writes any topic file under `.claude/memory/`, the session's commit MUST `git add .claude/memory/` alongside whatever other state it changed. The publishing chain (feature branch → auto-merge → `main`) handles the push automatically once it's committed. **Memory that doesn't reach `main` did not happen.**
- **NEVER push directly to `main`.** Repo policy. The feature-branch + auto-merge chain below is the only supported path.
- **NEVER let closed-source content above TLP:CLEAR into a brief on a public deployment.** Closed-source intel (`intel/<date>/` drop files) is cited by reference (`Closed-source: "Title" (Provider, date, TLP:X, ref: ID)`) — never via a fabricated URL. On `deployment.visibility: public` (see `config/org-profile.yaml`), above-CLEAR documents are leads to public sources only; `check_brief.py` `closed-source-tlp` FAILs the commit. Drop contract: [intel/README.md](intel/README.md). Private hosting: [docs/private-deployment.md](docs/private-deployment.md).
- **NEVER hand-edit an `ORG-PROFILE` managed block.** Organization-specific values (org description, sector/region lens, product + supplier watchlists, vulnerability-triage scheme) live in `config/org-profile.yaml`; `python3 tools/compose_prompts.py --write` regenerates the generated blocks inside both master prompts and all three agent definitions. **Any session that edits `config/org-profile.yaml` MUST run the compose script and commit the composed files in the same commit** — the `compose-profile` workflow fail-louds (does not auto-commit) on `claude/**` and `main`, so an uncomposed config change becomes red CI, not silent drift. Pure config-value changes need no prompt-version bump; changes to the compose *renderer* or to the static watchlist/triage policy text in the prompts follow the normal versioning rule.
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

Three named sub-agents — all isolated context, model bound by their YAML frontmatter (operator-rebindable):

- **`cti-research`** — Phase 1 (daily) / Phase 2 (weekly) parallel research workers. One per domain (S1–S4 daily, W1–W2 weekly; plus the conditional S5/W3 closed-source intake spawned only when `intel/<date>/` has in-window files). Pivots from news to primary sources, returns verified items with full discovery traces. Opens its return with a mandatory `**Model:**` self-identification line. Definition: [.claude/agents/cti-research.md](.claude/agents/cti-research.md).
- **`cti-verification`** — Phase 5.7 (daily) / Phase 4.7 (weekly) cold-reader verifier. **Opus default.** Read-only — main agent owns all edits. Looped iteratively, fresh spawn each iteration (no shared memory) until verdict CLEAN or 5-iteration cap. Same self-identification contract. Definition: [.claude/agents/cti-verification.md](.claude/agents/cti-verification.md).
- **`cti-verification-alt`** — model-rotation variant of `cti-verification`. **Sonnet default.** Identical operational system prompt (gatekeeper framing, F1–F16 finding categories, return contract, 30-min cap). Only the YAML frontmatter and the alt header note differ. The Phase 5.7 / Phase 4.7 main-agent loop spawns this on **even iterations** (iter 2, iter 4) so model-specific blind spots are caught when the next iteration runs on a different model. Definition: [.claude/agents/cti-verification-alt.md](.claude/agents/cti-verification-alt.md). **When you edit one verifier definition, you MUST regenerate the other in the same commit** — edit `cti-verification.md`, then copy its post-H1 body verbatim below the alt file's header note (the documented byte-equivalence boundary; the alt header explains the mechanics).

The main agent does composition, state update, commit, sync, push, publish-verification. Main agent and sub-agents may run on different models — the runtime decides per role and every agent self-identifies in its output. **Self-identification primary source: harness env vars `CLAUDE_FRIENDLY_NAME` and `CLAUDE_MODEL_ID`** (v2.47). The operator sets these in the routine container; sub-agents read them via Bash (`echo $CLAUDE_FRIENDLY_NAME`) and emit them verbatim in the `**Model:**` line. Falling back to "reason about your identity" is the v2.46 behaviour and is preserved when the env vars are unset, but it has demonstrably drifted (sub-agents pattern-matched stale training-data names). Set the env vars in the routine config to make the AI-content notice on every brief precisely correct. **NEVER spawn `general-purpose` for research or verification** — use the named sub-agents so the operator gets the right tool set + model binding.

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
- **Persist intermediate state often** under `work/<run-id>/<step>.json`. After every meaningful unit of work — every fetched source summarised, every CVE enriched, every section drafted — write the partial result so a later step can resume. **v2.59: `work/<run-id>/` is version-controlled** — Phase 6 (daily) / Phase 5 (weekly) commits the directory alongside the brief so sub-agent findings YAMLs, verification iteration reports, the URL-liveness ledger, and per-agent timestamp checkpoints are auditable in git history. The directory is the operator's primary forensic surface when a published brief later surfaces a defect.
- **One new candidate source per run, maximum.** Sub-agents surface candidates; the main agent writes them as `status: "candidate"` in `sources/sources.json` during Phase 5.
- **Verification loop is non-negotiable but never blocks publish.** Phase 5.7 (daily) / Phase 4.7 (weekly) spawns the verifier. Iteration 1 always runs. NEEDS_FIXES → apply remediations and re-spawn fresh. **Cap 5 iterations** (v2.46), with **model rotation across iterations** (v2.47): odd iterations spawn `cti-verification` (Opus), even iterations spawn `cti-verification-alt` (Sonnet). Iteration 5 still NEEDS_FIXES → publish anyway with residuals logged in § Verification Notes; `verification_residual_count` records `(truth + editorial)` of the final iteration so the cap-breach surfaces on the Ops dashboard (v2.47 — **never 0 on a NEEDS_FIXES final iteration**).

## Where things live

```
prompts/daily-cti-brief.md         # daily routine master prompt
prompts/weekly-summary.md          # weekly routine master prompt
prompts/CHANGELOG.md               # editorial-policy audit trail (bump on every prompt edit)
prompts/verification.md            # fake-news / two-source verification policy
prompts/brief-template.md          # canonical Markdown skeleton for the rendered brief / weekly
prompts/check-brief-fixes.md       # how to fix common check_brief.py FAILs
config/org-profile.yaml            # v2.65 — org profile: description, sector/region, product+supplier watchlists, triage scheme; v2.66 adds deployment (visibility, site_url)
intel/README.md                    # v2.66 — closed-source drop-folder contract (intel/<YYYY-MM-DD>/ + front-matter + TLP)
docs/private-deployment.md         # v2.66 — org-internal hosting: private repo + scheduled pull/build/serve of site/_site
tools/compose_prompts.py           # v2.65 — renders the profile into the ORG-PROFILE managed blocks (never hand-edit those)
.github/workflows/compose-profile.yml # v2.65 — composes on push to operator branches; check-only fail-loud on main + claude/**
.claude/agents/cti-research.md     # research sub-agent definition
.claude/agents/cti-verification.md  # verification sub-agent (Opus default)
.claude/agents/cti-verification-alt.md # rotation variant (Sonnet default; identical body)
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
tools/source_candidates.py         # v2.47 § 3.6 — surface "sources we should add" (cited-but-not-in-sources.json)
tools/source_health.py             # v2.47 § 3.7 — independent weekly source-health snapshot (run by GH Actions)
.github/workflows/source-health.yml # v2.47 § 3.7 — weekly cron firing source_health.py
state/source_health.json            # v2.47 § 3.7 — bounded health-snapshot history (Ops dashboard reads this)
site/build.py                      # static-site generator (stdlib-only)
site/taxonomy.yaml                 # controlled vocabulary for footers (build refuses unknown values)
site/_site/trends/                 # v2.47 § 4.1 — cross-brief threat-class trend dashboard (built from briefs)
site/_site/feed-{public-sector,healthcare,finance,energy,ot-ics,defense,telco,education}.xml  # v2.47 § 4.3 — sector-specific RSS slices
docs/architecture.md               # end-to-end map of what reads/writes what
docs/operating.md                  # operator runbook
work/<run-id>/                     # v2.59: version-controlled per-run artefact dir — committed in Phase 6 with the brief
work/<run-id>/url-liveness.tsv     # v2.47 § 3.4 — sub-agents append `<url>\t<status>\t<fetched_at>` per fetch; check_brief.py reads this
work/<run-id>/prior_coverage.json  # v2.47 § 2.2 — Phase 0 builds this; sub-agents read it for fetch-time dedup
work/<run-id>/findings.<S1|S2|S3|S4>.yaml  # v2.58 § Tier 4.3 — structured sub-agent findings; main agent reads from disk
work/<run-id>/verification.iter<N>.md  # v2.50 § verifier compact-summary — full disk report per iteration
work/<run-id>/verification.iter<N>.findings.yaml  # v2.48 § findings-summary — machine-readable per-iteration finding records
```

## Editing the master prompts — versioning rule (ALWAYS)

Any edit to `prompts/daily-cti-brief.md`, `prompts/weekly-summary.md`, `prompts/verification.md`, `prompts/brief-template.md`, `prompts/check-brief-fixes.md`, `.claude/agents/cti-research.md`, `.claude/agents/cti-verification.md`, or `.claude/agents/cti-verification-alt.md` MUST ship all three of these in the same commit (banner bump + CHANGELOG entry + the file edit itself). Skipping any of them produces silent drift between what the routine actually loaded, what the brief footer claims, and what the changelog records. **Both verifier definitions move in lockstep** — edit `cti-verification.md`, then regenerate the alt file's body from it (byte-identical below the alt header note; only the frontmatter and that note differ). **Exemption (v2.65):** regeneration of `ORG-PROFILE` managed blocks by `tools/compose_prompts.py` after a `config/org-profile.yaml` value change is NOT a prompt edit — no banner bump, no CHANGELOG entry; the compose commit records it. Edits to the compose renderer or to the static policy text around the blocks are prompt edits and follow the full rule.

### Daily ↔ weekly parity — shared machinery moves in lockstep; the lens stays divergent (ALWAYS)

`prompts/daily-cti-brief.md` and `prompts/weekly-summary.md` deliberately **share their procedure and machinery** but deliberately **differ in their intelligence lens and output structure**. **The daily is the gold standard for shared machinery.** When you change a shared element in one prompt you MUST mirror the equivalent change into the other **in the same commit** (same discipline as the two verifier definitions above), adapting only the phase numbers / cadence units, and update `prompts/brief-template.md` when the change touches the rendered shape. The CHANGELOG entry's `### What changed` must name which prompt(s) moved; `### What stays` must note what was intentionally left divergent. The two drifted once (the weekly lacked the daily's verification/triage pass, compose-after-return gate, `Evidence:` field, F13–F15 + prior-iteration deltas, and historical-context rule — see CHANGELOG v2.61); this rule exists so that cannot recur silently.

**Shared machinery — change one ⇒ mirror into the other (adapt phase numbers / cadence only):**

- CRITICAL "always produce a brief/summary" header + the anti-crash guards.
- Prime directives **except** the lens ones listed below — zero-LLM-knowledge, inline-links-must-be-real, no IOCs, no vanity metrics, two-source + national-CERT carve-out, fake-news guard, recency mechanics, trace-to-primary, CISA-KEV-deadline rule, historical-context/Background, less-is-more.
- Per-item metadata footer spec (taxonomy fields, multi-CVE breakdown, blocked-URL allowlist, the `Evidence:` source-quote field).
- Skeleton-then-Edit + the compose-after-return anti-fabrication gate.
- Self-identification (model + timestamps), the AI-content notice, the `Generated by:` line.
- Verification & triage pass (daily Phase 2 / weekly Phase 2.5).
- Self-check gate (daily Phase 5.5 / weekly Phase 4.5) **and** verification sub-agent loop (daily Phase 5.7 / weekly Phase 4.7): model rotation, prior-iteration deltas on even iterations, the F1–F15 finding set, rich per-iteration `findings[]`, early-exit, 5-iteration cap.
- `state/run_log.json` schema (`sub_agents`, `fetch_failures`, `bridge_uses`, `verification.iterations[]`) and the state-update lifecycle (`covered_items`, `cves_seen`, `sources`, `deep_dive_history`).
- Publishing chain + `work/<run-id>/` commit + publish verification.
- Main-agent-does-no-source-fetching anti-classifier-trip invariant; the META self-evolution authority + hard-invariants list.

**Intentionally divergent — do NOT force-sync (this is the *point* of having two prompts):**

- The intelligence lens / editorial framing: daily = operational today's-signal, 1–7-day patch / hunt / block / detect decisions, **no** long-horizon; weekly = broader threat picture, multi-day chains, research & threat-actor developments, annual reports, long-horizon, looking-ahead.
- Section structure: daily 8 sections (incl. Deep Dive + the Immediate-Action callout); weekly 12 sections (incl. on-fire / multi-day / research+actor / annual / long-running / policy / looking-ahead).
- Cadence + recency unit: daily `window_hours`; weekly `window_days` + most-recent-Sunday ISO-week anchor.
- Sub-agent fan-out: daily S1–S4; weekly Phase 1 structured review + W1–W2.
- Phase numbering offset (no deep-dive phase in the weekly; the weekly adds Phase 2.5 triage).
- Dedup polarity: the daily (PD-8) never repeats a recent weekly and carries no long-horizon synthesis; the weekly **may** repeat a daily item with a new lens. The asymmetry runs one way.

Edits to `CLAUDE.md`, `docs/`, `tools/`, or `site/` only require a prompt bump when they materially change runtime behaviour. Pure clarifications, reformatting, and ops-doc updates do not.

1. **Bump the version banner** in the prompt itself (`> **Prompt version:** vN.M`). Daily and weekly versions move in lockstep — even if only one was edited substantively — so `state/run_log.json.prompt_version` is unambiguous across runs.
2. **Add a top entry to [`prompts/CHANGELOG.md`](prompts/CHANGELOG.md)** with `### Why`, `### What changed`, `### What stays` headings. The CHANGELOG is the editorial-policy audit trail and the only place that explains *why* a behaviour shifted between two committed briefs. **No silent bumps.**
3. **Carry the new version through the brief footer and run log.** Both read from the prompt's banner — no extra step if step 1 is correct. `tools/check_brief.py` cross-checks the footer banner against `prompts/CHANGELOG.md`'s most-recent heading and FAILs the commit on a mismatch (the safety net for skipped step-1 / step-2 edits).

## Self-evolution

The routine has full authority to modify `prompts/`, `docs/`, `sources/sources.json`, `state/*.json`, `.claude/agents/`, `.claude/memory/`, `site/taxonomy.yaml`, and `tools/`. Every change appears in the commit diff for after-the-fact review.

**Hard invariants that must NOT be removed or weakened** (surface concerns in § Verification Notes instead): AI-content notice, no IOCs, two-source verification with national-CERT carve-out, English output, feature-branch-only publishing chain, self-check gate (Phase 5.5 daily / 4.5 weekly), verification sub-agent loop (Phase 5.7 daily / 4.7 weekly), per-item metadata footer using taxonomy values, memory commits.
