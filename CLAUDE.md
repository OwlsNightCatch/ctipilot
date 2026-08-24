# CLAUDE.md — ctipilot.ch repo conventions

Loaded into every Claude Code session here (interactive or routine). The master prompts under `prompts/` are the source of truth for the pipeline routines — this file only carries cross-cutting rules every session needs.

## What this repo is

Autonomous CTI pipeline for a Swiss federal SOC (by default — the deployment is organization-parameterizable via `config/org-profile.yaml`). A scheduled Claude Code routine reads `prompts/cti-run.md` on each fire — **the cadence is operator-tuned at will (multiple fires per day and a single daily fire are equally first-class; the window is always derived from the gap to the last run)** — researches the window's threat landscape via parallel sub-agents, and publishes each verified finding as its own entry file `entries/YYYY-MM-DD/<slug>.md` plus one run record `runs/YYYY-MM-DD/<run-id>.md`. A weekly routine (`prompts/weekly-summary.md`) adds `horizon: strategic` entries; a second weekly routine (`prompts/quality-audit.md`) audits the trailing window — truth re-verification, coverage re-sweeps, systemic drift, monthly priority calibration — and ships fixes (reports under `docs/audits/`). **There is no brief file** — the brief is *rendered* from entries over a reader-chosen time window (default: last 24 h) at [https://ctipilot.ch/live/](https://ctipilot.ch/live/); the site rebuilds on every push to `main` that touches the content store. The normative data model is [docs/pipeline.md](docs/pipeline.md).

Audience is Tier 2/3 IR / threat hunters / detection engineers — assume MITRE ATT&CK fluency, no executive hedging, no IOCs, no vanity metrics.

For an end-to-end map of what reads / writes what, see [docs/architecture.md](docs/architecture.md). For the operator runbook see [docs/operating.md](docs/operating.md).

## Key commands (verify before claiming a task is done)

| Goal | Command |
|---|---|
| Phase 5.5 self-check on a run's output | `python3 tools/check_run.py <run-id>` (no arg = latest run) |
| Validate the whole content store | `python3 tools/check_run.py --all` |
| Build the static site (smoke test for any `site/` change) | `python3 site/build.py` |
| Stdlib-only smoke tests for build helpers | `python3 site/test_build.py` |
| Build the per-run dedup index | `python3 tools/build_prior_coverage.py <run-id> 7` |
| Compact state digest | `python3 tools/run_summary.py --out work/<run-id>/state-summary.json` |
| Bridge fetcher for known-403 hosts | `python3 tools/fetch_source.py {cisa-kev \| ncsc-csh recent N \| url <URL>}` |
| Read a PDF-only advisory (joint advisories, authority reports) | `python3 tools/fetch_source.py pdf <URL>` (stdlib, no OCR — an image-only PDF reports "no text objects", which means *not extractable*, never *says nothing*); tests: `python3 tools/test_fetch_source_pdf.py` |
| Validate the org profile / re-render it into the prompts | `python3 tools/compose_prompts.py --check` / `--write` (also `--dump`, `--selftest`) |
| ATT&CK pin: freshness / update / invariants | `python3 tools/attack_data.py {--check \| --update [--version X.Y] \| --selftest \| --info}` (contract: [attack/README.md](attack/README.md)) |

`tools/check_run.py` MUST exit 0 before any commit that adds entries or a run record. The script is read-only; drift is what *you* fix.

**Zero-warning discipline (v3.28): warnings are defects with a deadline, not decoration.** A run fixes every warning it caused or can fix before commit (`check_run.py` WARNs and `site/build.py` self-check warnings alike); what legitimately survives — a run's own telemetry facts, settled history on immutable records — is swept to zero by the weekly quality audit, which fixes root causes or (unfixable history only) acknowledges the warning with a reason in `state/warning_acknowledgments.json`. Acknowledged warnings report separately and count as zero; a run NEVER self-acknowledges its own fresh warnings. The audit is the pipeline's weekly cleanup — after every audit, `check_run.py --all` ends 0 warn · 0 fail and the build is warning-free.

## Hard rules — ALWAYS / NEVER

- **ALWAYS commit `.claude/memory/` changes on every session that touches it.** Auto-memory is enabled and persisted under `.claude/memory/` (committed to git). Every routine fire spawns a fresh container that clones from `main`; memory not committed is silently lost. **Memory that doesn't reach `main` did not happen.**
- **NEVER push directly to `main`.** Repo policy. The feature-branch + auto-merge chain below is the only supported path.
- **NEVER edit a published entry.** Entries are immutable once committed. New information, corrections, and same-day developments are NEW entries with `update_of: <original entry id>`. The run record is the only per-run file the same fire may update in place (same-minute retry; Phase 7 publish-status amendment — `publish_status`/`publish_checked_at`/`publish_note` only).
- **NEVER let a run finish without a run record.** `runs/<date>/<run-id>.md` is the mandatory artifact of every fire — zero entries is a healthy quiet window; a missing record is an operational failure.
- **NEVER duplicate in-window coverage.** Every run's Phase 0 builds the prior-coverage index (last 14 days INCLUDING earlier runs today) and the main agent loads it in full — every in-window brief — into context; a candidate matching covered CVEs/entities anywhere in that 14-day window (or the store-wide CVE index for older coverage) ships as an `update_of` delta or not at all. `check_run.py` FAILs CVE-level duplicates.
- **NEVER inflate volume, NEVER hardcode an entry count, and NEVER leave a relevant item out.** Entry volume follows the strict relevance/actionability gate (PD-11) — there is no per-run, per-day, or rolling-24 h target or ceiling. The brief must be **sound AND complete**: sound (everything in it is relevant, accurate, and actionable — very low false positives; no marginal item survives) *and* complete (every genuinely-relevant in-window item the run surfaced is published — very low false negatives; a reader relying on ctipilot.ch alone has no blind spot on anything that matters to their job). A dropped relevant item is as serious a failure as an included marginal one — and a silent one. The window carries exactly the entries that clear the gate, however few or many; every entry must earn its place, none that earns it is thinned to save space. More runs mean lower latency, never more content (dedup guarantees it). `priority: critical` and deep-dive treatment stay rare because their qualitative bars are extreme, not because a number caps them.
- **ALWAYS hold `actions[]` to the do-now bar — empty is the normal case (v3.19).** `actions[]` feeds the rendered brief's aggregated § Action Items — the task list an on-shift team actually works, whose value drops with every marginal line. An action ships only when it is a concrete, self-contained task the team starts now, derived from this finding's own mechanics; generic advice ("enable MFA", "patch regularly") NEVER appears, body detection/hardening guidance is never restated as an action, and a relevant entry with `actions: []` is healthy. Master rules: `prompts/cti-run.md` Phase 4 § `actions[]`; the verifier flags drift (F18) and `check_run.py` WARNs (`action-items`).
- **NEVER invent a second entity key.** Every actor/campaign/malware/tool/incident/report is linked via its `entities/registry.yaml` key; check aliases before registering anything new; registry keys are permanent (extend aliases, never rename); a discovered duplicate is tombstoned with `merged_into: <canonical-key>` (its `relations[]` move to the canonical record) and new entries reference only canonical keys (docs/pipeline.md § Entity registry).
- **ALWAYS type and source entity relationships (v3.20).** Entity connections are typed, directed `relations[]` edges on the registry record — `{to, type, source, note}` with `type` from the controlled vocabulary (`attributed-to`, `uses`, `exploits`, `part-of`, `variant-of`, `successor-of`, `collaborates-with`, `overlaps-with`, `documented-in`, `related-to`) and `source` the entry id whose cited reporting states the connection. Only relate what a source states — an overlap claim is `overlaps-with`, never upgraded to attribution; a suspected same-entity is an alias or a tombstone, not a relation; co-occurrence is derived at render time, never stored. The untyped `related` list is retired; `check_run.py` FAILs it and every malformed edge. Normative: docs/pipeline.md § Relationships; analyst surface: the `/graph/` interactive threat graph.
- **NEVER filter on TLP or a public/private flag.** This pipeline has no TLP gate and no `deployment.visibility` switch: everything the agents can read — including every file under `intel/<date>/` — is fair game to process into entries and reports; nothing is withheld or downgraded on the basis of a TLP marking (a legacy `tlp` key is ignored). Closed-source intel is still cited via `closed_sources` frontmatter (referenced, never a fabricated URL) and must trace to a drop file the verifier can `Read` (`check_run.py` `closed-source` WARN). The control is what the operator drops into the repo, not a downstream filter. Drop contract: [intel/README.md](intel/README.md).
- **ALWAYS classify every entry — exactly one rating, never zero (v3.18).** Non-triage entries carry a NATO Admiralty `classification: {reliability A–F, credibility 1–6}`. Triage kinds (`classification.triage_kinds`, default `vulnerability`) carry `org_triage` INSTEAD only while the profile configures a triage scheme; with none configured (this deployment) they carry the Admiralty block like every other kind. `check_run.py` FAILs a v3.18+ entry with neither rating, and `--all` re-enforces it store-wide forever (`store-ratings`). Schemes, code vocabularies, and the kind split live in `config/org-profile.yaml` `classification:` and are rendered into the prompts by `compose_prompts.py`; source reliability in `sources/sources.json` uses the same Admiralty A–F letters (`reliability_codes`).
- **NEVER hand-edit an `ORG-PROFILE` managed block.** Organization values live in `config/org-profile.yaml`; `python3 tools/compose_prompts.py --write` regenerates the blocks in both master prompts, `prompts/verification.md`, and all three agent definitions. Any session that edits the config MUST compose and commit the composed files in the same commit.
- **NEVER reintroduce a site-identity literal into `site/build.py`.** Every site name / tagline / color / analytics value comes from `config/branding.yaml` via `site/branding_config.py`. Fork contract: [docs/customization.md](docs/customization.md).
- **NEVER put IOCs in an entry.** No hashes, no IPs, no attacker domains, no YARA/Sigma/Suricata. Entries are *knowledge* — TTPs, campaigns, vulnerabilities, detection concepts.
- **ALWAYS compose entries triage-ready and vendor-agnostic.** The entry store is a threat-knowledge base for two readers of equal rank: human Tier 2/3 responders AND automated SOC/triage agents matching live alerts against it. Attacker activity is described as *observable behavior* — telemetry classes in vendor-neutral terms (platform artifacts as examples, never rule code), official product names in `affected_products[]`, and a `**Triage:**` benign-lookalike discriminator where the cited mechanism supports one — omitted, never invented, where it doesn't. Master rules: `prompts/cti-run.md` Phase 4 § Triage-ready behavioral description.
- **ALWAYS map ATT&CK in `techniques[]` metadata — keep T-ids out of prose unless essential.** `techniques[]` is the canonical, complete mapping surface (every technique the sources support, **active ids** per the pinned `attack/enterprise-attack.json`); entity/CVE TTP profiles, the `/attack/` overlap matrix and the Navigator-layer exports are all derived from it, evidence-bound. The body describes each mapped behavior in plain language and must read complete without a single T-number — inline ids only where they genuinely earn their place (deep-dive kill chains, a mapping that is itself the finding); bare ID lists are a defect. The pin is versioned: NEVER hand-edit the dataset, NEVER hardcode tactic/technique tables (releases rename tactics — v19 replaced Defense Evasion); update via `tools/attack_data.py --update` (weekly runs `--check` and surface drift). **A `threat`/`incident`/`vulnerability` entry never ships with an empty `techniques[]`** — the access/exploitation vector is always mappable; `check_run.py` FAILs it on v3.18+ runs (and `research`/`annual-report` empty → WARN), FAILs a missing/broken pin, and WARNs on unknown/revoked ids and unmirrored prose ids.
- **NEVER `WebFetch` CISA / NCSC.ch directly** — both reliably 403 the routine UA. Use `python3 tools/fetch_source.py`.
- **ALWAYS treat the jina reader as the LAST-RESORT transport (v3.25).** It spends metered API-key credit per fetch and its anonymous free tier is best-effort only (observed HTTP 401, 2026-07-18). The ladder is: RSS feed → `WebFetch` → direct bridge (`url <URL>` / structured recipe) → `jina <URL>` last. Force the reader directly only for hosts proven to need it (`fetch_method: jina` in `sources/sources.json` — e.g. heise article bodies, cisa.gov dynamic paths) or after every direct rung failed. Monitor the pool with `python3 tools/fetch_source.py jina-usage`; keys live ONLY in the environment, never in the repo.
- **NEVER call `WebFetch` without the outbound-links template** (verbatim in `.claude/agents/cti-research.md` and `.claude/agents/cti-verification.md`) — the default summariser drops every URL.
- **NEVER cite a homepage, listing index, news category, or NVD/MITRE per-CVE page as a source.** `check_run.py` FAILs these patterns. Use the specific article / advisory / vendor PSIRT URL.
- **NEVER skip `tools/check_run.py` before commit.** Phase 5.5. Exit 0 required.
- **NEVER block the run on a sub-agent.** Sub-agents stalled past their per-role hard cap (45 min research / 30 min verification) are abandoned, not waited on. **Failing to write the run record is the worst outcome.**

## Auto-memory mechanics (only what's non-obvious)

- **Storage:** `.claude/memory/MEMORY.md` is the index (auto-loaded, first 200 lines / 25 KB); topic files load on demand. Only difference from stock behaviour: the files live in the repo.
- **Redirect mechanism:** [`.claude/hooks/setup-memory.sh`](.claude/hooks/setup-memory.sh) symlinks the system auto-memory dir into `<repo>/.claude/memory/` on `SessionStart`. Idempotent; self-documenting.
- **Fallback:** if the symlink isn't created, `Read`/`Write`/`Edit` `.claude/memory/` directly — persistence still works.

## Custom sub-agents (`.claude/agents/`)

Three named sub-agents — isolated context, model bound by YAML frontmatter (operator-rebindable):

- **`cti-research`** — Phase 1 (intel run) / Phase 2 (weekly) parallel research workers, one per domain (S1–S4 + conditional S5 intake; W1–W2 + conditional W3). Reads the prior-coverage index AND `entities/registry.yaml` before fetching; returns findings YAMLs with `entity_keys` / `new_entities` / `novelty: update-of:<entry-id>`. Opens every return with the mandatory `**Model:**` line.
- **`cti-verification`** — Phase 5.7 cold-reader verifier (**Opus default**). Scope: the run's new entries + run record. Read-only; looped fresh-spawn until a **confirmed CLEAN — two consecutive iterations, on two different models, both CLEAN (v3.23)** — or the 8-iteration cap (v3.27). Finding categories F1–F18 incl. frontmatter⇔body agreement, priority calibration, Admiralty-classification drift, and action-item discipline.
- **`cti-verification-alt`** — Sonnet rotation variant, byte-identical body below its header note. Spawned on even iterations. **When you edit one verifier definition, you MUST regenerate the other in the same commit.**

**Self-identification primary source: the model line the harness injects into each agent's OWN system prompt** (`You are powered by the model named … The exact model ID is …`) — generated per-agent at spawn time, it sees the definition's `model:` pin (verified empirically 2026-07-09: pinned sub-agents reported Sonnet from their prompt line while the container env vars said Opus). Fallback 1: env vars `CLAUDE_FRIENDLY_NAME` / `CLAUDE_MODEL_ID` — **container-scoped**: they carry the main-agent default and cannot see a sub-agent's pin; env-fallback values carry an explicit `— container default, env fallback` marker on the `**Model:**` line, and uniformity among such reports is a measurement limitation, never proof that pinning/rotation failed. Fallback 2: `Anthropic Claude (specific model not determined)` — never a training-data guess. **NEVER spawn `general-purpose` for research or verification** — use the named sub-agents.

## Branching and publishing — feature branch only

Every session here operates on a `claude/<adjective>-<name>-<id>` feature branch. **`main` is owned by [`.github/workflows/auto-merge-claude.yml`](.github/workflows/auto-merge-claude.yml)** — the only thing that promotes commits onto `main`.

**1. Session start — pull the freshest `main` before doing any work:**

```bash
git fetch origin main
git merge --no-edit -m "sync: pull origin/main at session start" origin/main
```

Conflicts on `state/*.json` or `entities/registry.yaml` resolve `--ours`, `sources/sources.json` resolves `--theirs` (same rules as the workflow); anything else surfaces to the operator. Entry and run-record files are per-run unique paths and cannot conflict.

**2. Throughout the session — feature branch only.** Never check out `main`, never push to `main`.

**3. Session end — stage specifics (never `git add -A`), commit, sync again, push with retry.** Always include `.claude/memory/` when memory was touched. Use the retry shape from `prompts/cti-run.md` Phase 6 (the explicit `if/else` on `PUSH_OK` matters — the `[ ... ] && echo` tail shape exits 1 on success and makes the harness flag a successful push as failed).

**4. Auto-merge takes it from there.** Every push to `claude/**` fires the workflow: fast-forward when possible, auto-resolution on known paths, feature branch deleted on success, loud `::error::` otherwise.

**5. Publish verification (Phase 7).** Poll `git fetch origin main && git cat-file -e origin/main:runs/<date>/<run-id>.md` until the record lands (10-min budget), then poll `<site>/data/briefbook.json` for the run id. Report `publish: ok` / `main-only` / `pending (<reason>)` from the actual poll. **A pushed feature branch is not a published run.**

**`gh` is for local interactive sessions only.** The cloud routine container and Claude Code on the Web do **not** ship `gh` — use the polling path.

## Operational guardrails

- **Entry files are small — one `Write` per entry is safe.** Never batch more than ~5 file writes per assistant turn; long files (run record with many findings, docs) use skeleton-then-`Edit`. A single `Write` >300 lines risks a stream-idle timeout.
- **Persist intermediate state often** under `work/<run-id>/` (version-controlled — committed with the run). Findings YAMLs, verification reports, url-liveness ledger, timestamp checkpoints are the operator's forensic surface.
- **One new candidate source per run, maximum.**
- **Verification loop is non-negotiable but never blocks publish.** Iteration 1 always runs; model rotation (odd = Opus `cti-verification`, even = Sonnet `cti-verification-alt`); **a CLEAN publish requires two consecutive CLEAN verdicts from two different models (v3.23)** — a first CLEAN triggers a confirmation pass on the other model, so a CLEAN publish is ≥2 iterations, and an unconfirmed CLEAN publishes only at the cap or with `verification.confirmation_waived` recorded; cap 8 with fail-open (v3.27 — raised from 5); `verification_residual_count` never 0 on a NEEDS_FIXES final iteration.

## Where things live

```
prompts/cti-run.md                 # intel-run master prompt (fires N×/day)
prompts/weekly-summary.md          # weekly strategic run (builds on cti-run.md)
prompts/quality-audit.md           # weekly quality-audit run (builds on cti-run.md; reports → docs/audits/)
prompts/CHANGELOG.md               # editorial-policy audit trail (bump on every prompt edit)
prompts/verification.md            # two-source / fake-news verification policy
prompts/entry-template.md          # canonical entry + run-record skeletons
prompts/check-run-fixes.md         # fix recipes for common check_run.py FAILs
docs/routines.md                   # catalog of every routine invocation prompt + in-repo prompt (incl. weekly backup)
docs/pipeline.md                   # NORMATIVE v3 data model (entries, registry, runs)
config/org-profile.yaml            # org profile (compose_prompts.py renders it into the prompts)
config/branding.yaml               # site branding profile
entries/YYYY-MM-DD/<slug>.md       # per-finding intelligence entries (immutable)
entities/registry.yaml             # global entity registry (actors, campaigns, malware, …)
attack/enterprise-attack.json      # pinned MITRE ATT&CK release (generated — tools/attack_data.py)
runs/YYYY-MM-DD/<run-id>.md        # per-run records: telemetry frontmatter + verification notes
sources/sources.json               # ~150 curated CTI sources (autonomous lifecycle; tier field)
state/cves_seen.json               # flat CVE dedup index
state/source_health.json           # bounded source-health history
state/warning_acknowledgments.json # audit-reviewed ledger of settled-history WARNs (zero-warning discipline)
site/content_model.py              # reference parser/validator (entries, registry, runs)
site/build.py                      # static-site generator (dynamic /live/, day pages, weekly, ops, feeds)
site/taxonomy.yaml                 # controlled vocabulary for entry frontmatter
tools/check_run.py                 # Phase 5.5 gate (must exit 0)
tools/attack_data.py               # ATT&CK dataset builder/updater (--check/--update/--selftest)
tools/build_prior_coverage.py      # entry-store dedup index builder
tools/run_summary.py               # compact state digest (+ 24 h budget snapshot)
tools/migrate_briefs.py            # one-shot v2→v3 migration (kept for provenance)
tools/fetch_source.py              # bridge fetcher for known-403 hosts
tools/source_candidates.py         # cited-but-untracked host surfacing
tools/source_health.py             # source accessibility probe
work/<run-id>/                     # per-run artefacts (committed with the run)
```

## Editing the master prompts — versioning rule (ALWAYS)

Any edit to `prompts/cti-run.md`, `prompts/weekly-summary.md`, `prompts/quality-audit.md`, `prompts/verification.md`, `prompts/entry-template.md`, `prompts/check-run-fixes.md`, or any `.claude/agents/*.md` MUST ship all three of: banner bump + `prompts/CHANGELOG.md` entry (`### Why` / `### What changed` / `### What stays`) + the edit itself, in the same commit. All three banner-versioned master prompts (`cti-run.md`, `weekly-summary.md`, `quality-audit.md`) move in lockstep; both verifier definitions move in lockstep (edit `cti-verification.md`, regenerate the alt body byte-identically). **Exemption:** ORG-PROFILE block regeneration after a config-value change is not a prompt edit. `check_run.py` cross-checks the run record's `prompt_version` against the CHANGELOG head and FAILs on mismatch.

### Intel-run ↔ weekly — shared machinery lives in one place; the lens stays divergent (ALWAYS)

v3 ended the v2 copy-drift problem structurally: `prompts/weekly-summary.md` **builds on** `prompts/cti-run.md` (it instructs a runtime `Read` of the intel-run prompt and defines only the weekly divergences). Shared machinery (anti-crash guards, PD-1…13, composition discipline, state lifecycle, gate, verifier loop, publishing chain) is edited ONLY in `cti-run.md`; the weekly file carries the deliberately divergent lens — W-PD-1 inclusion gate, ISO-week recency, weekly dedup polarity (weekly may re-frame operational entries via `references`; intel runs never duplicate the weekly), `weekly_section` placement, relevance-driven section volume (no count target). When an edit to `cti-run.md` changes a phase contract the weekly references, re-read the weekly in the same commit to confirm the reference still holds. The same build-on pattern and re-check duty apply to `prompts/quality-audit.md` (the weekly quality-audit lens).

## Self-evolution

The routine has full authority to modify `prompts/`, `docs/`, `sources/sources.json`, `state/*.json`, `entities/registry.yaml`, `.claude/agents/`, `.claude/memory/`, `site/taxonomy.yaml`, and `tools/`. Every change appears in the commit diff for after-the-fact review.

**Hard invariants that must NOT be removed or weakened** (surface concerns in the run record instead): AI-content transparency via run records, no IOCs, two-source verification with carve-outs, English output, feature-branch-only publishing, the mechanical gate (`check_run.py` exit 0), the verification sub-agent loop, entry immutability + update_of discipline, the entity registry as the single entity namespace, relevance discipline (strict inclusion gate, no hardcoded entry count; sound AND complete — no marginal items and no blind spots; more runs never mean more content), run-record-per-fire, memory commits.
