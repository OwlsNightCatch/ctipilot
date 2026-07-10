# Architecture

A single, end-to-end map of every component in the repository: what it is,
what it reads, what it writes, and how it talks to the others. If you are
debugging an unexpected commit or onboarding a new operator, start here.

The **data model** (entry files, entity registry, run records) is specified
normatively in [`docs/pipeline.md`](pipeline.md) — this file maps the moving
parts and defers to that spec for every field-level question.

## One picture

```
                      ┌────────────────────────────────────┐
                      │  Claude Code routines (cloud)      │
                      │                                    │
                      │  intel run — fired N× per day:     │
                      │   "Read prompts/cti-run.md and     │
                      │    execute it."                    │
                      │  weekly — fired once per week:     │
                      │   "Read prompts/weekly-summary.md  │
                      │    and execute it."                │
                      └─────────────────┬──────────────────┘
                                        │ git push
                                        ▼
   reads ┌──────────────────────────────────────────────────────────┐
 ──────► │                       repository                         │
         │                                                          │
         │  prompts/                  entries/YYYY-MM-DD/<slug>.md  │
         │   ├ cti-run.md             entities/registry.yaml        │
         │   ├ weekly-summary.md      runs/YYYY-MM-DD/<run-id>.md   │
         │   ├ CHANGELOG.md                                         │
         │   ├ verification.md        state/                        │
         │   ├ entry-template.md       ├ cves_seen.json             │
         │   └ check-run-fixes.md      └ source_health.json         │
         │                            sources/sources.json          │
         │  docs/pipeline.md          work/<run-id>/                │
         │   (NORMATIVE data model)                                 │
         │  site/content_model.py     tools/                        │
         │   (shared parser)           ├ check_run.py (Phase 5.5)   │
         │                             ├ build_prior_coverage.py    │
         │  .claude/agents/            ├ run_summary.py             │
         │   ├ cti-research.md         └ fetch_source.py            │
         │   ├ cti-verification.md                                  │
         │   └ cti-verification-alt.md                              │
         └──────────────────────────────┬───────────────────────────┘
                                        │
                                        │ git push (claude/** branches only)
                                        ▼
                           ┌────────────────────────────┐
                           │ auto-merge-claude.yml      │
                           │  ff-merges (or merges with │
                           │  state/*.json + entities/  │
                           │  registry.yaml → ours,     │
                           │  sources.json → theirs)    │
                           └────────────┬───────────────┘
                                        ▼
                                      main
                                        │
                                        ▼ workflow_run (success only)
                           ┌────────────────────────────┐
                           │ deploy-site.yml            │
                           │  runs site/build.py        │
                           │  force-pushes to gh-pages  │
                           └────────────┬───────────────┘
                                        ▼
                              GitHub Pages reader
                              /live/ renders the entry store
                              over a reader-chosen time window
                              (real HTML pages — no SPA)
```

## Components

### `docs/pipeline.md` — the normative data model

The single normative specification of the v3 content model: entry-file
frontmatter (kinds, priority, verification enum, `update_of`, `cves[]`,
`evidence[]`, `org_triage`, …), run-id shape, the entity-registry contract,
run-record telemetry, relevance discipline, cross-run dedup, and what
`tools/check_run.py` validates. **If any code or doc disagrees with it, the
spec wins and the code is the bug.** Nothing in this file restates its field
tables — read it once before touching any producer or consumer.

### `prompts/` — everything the routines load at runtime

The two master prompts plus the runtime-policy / template / debug docs they reference. Each master prompt is the *entire* runtime contract for a routine; the routine is invoked with a one-line wrapper ("Read this prompt and execute it"). The supporting files live under `prompts/` because the master prompts `Read` them at runtime — they are part of the prompt machinery, not operator-facing documentation.

- [`prompts/cti-run.md`](../prompts/cti-run.md) — the intel run, **fired
  multiple times per day** (the operator picks the cadence; the prompt is
  cadence-agnostic — the recency window derives from the gap since the
  previous run record). Phases 0–7: preflight (run id, dedup index, state
  digest, registry read) → parallel research (S1–S4, conditional S5 intake)
  → verification & triage → deep-dive selection → compose entries + run
  record → state update → 5.5 mechanical gate → 5.7 verifier loop →
  commit/sync/push → publish verification. Output: zero or more entry
  files plus exactly one run record per fire.
- [`prompts/weekly-summary.md`](../prompts/weekly-summary.md) — the weekly
  *strategic* run, fired once per week. **Builds on `cti-run.md`** — it
  instructs a runtime `Read` of the intel-run prompt and defines only the
  weekly divergences (W-PD-1 inclusion gate, ISO-week recency, weekly dedup
  polarity, `weekly_section` placement, relevance-driven section volume), so
  shared machinery lives in exactly one file and cannot copy-drift. Output:
  `horizon: strategic` entries + one run record; the `/weekly/YYYY-Www/`
  page is rendered from them. The weekly may re-frame operational entries
  via `references`; intel runs never duplicate strategic entries — the
  asymmetry runs one way.
- [`prompts/CHANGELOG.md`](../prompts/CHANGELOG.md) — the version history of
  the prompts. Treat as the audit trail for editorial-policy changes.
- [`prompts/verification.md`](../prompts/verification.md) — the editorial /
  fake-news verification policy; the two-source rule and its carve-outs
  (now the structured `verification` frontmatter enum).
- [`prompts/entry-template.md`](../prompts/entry-template.md) — canonical
  entry + run-record skeletons per kind plus a worked-good depth fragment.
  Phase 4 `Read`s it before composing.
- [`prompts/check-run-fixes.md`](../prompts/check-run-fixes.md) — fix
  recipes for common `tools/check_run.py` FAILs, keyed to the checker's
  output labels.

### `entries/` — the content store

One Markdown file per verified finding at `entries/<YYYY-MM-DD>/<slug>.md`
(folder = UTC date of `discovered_at`; entry id = `<YYYY-MM-DD>/<slug>` —
the path is the identity, there is no `id` field). Frontmatter carries the
complete metadata contract (headline, summary, priority + optional
`immediate_action`, taxonomy tags/regions/sectors, entity keys, per-CVE
records, sources, evidence quotes, verification flags, `actions[]`); the
body is the analysis in the same technical register as a v2 brief item.

**Entries are immutable once committed.** New information — including a
same-day development between two runs — is a new entry with
`update_of: <original entry id>`; corrections ship the same way, never as
edits. Volume follows a strict relevance/actionability gate rather than a
count — no per-run, per-day, or rolling-24 h target or ceiling; the window
carries exactly the entries that earn their place, and more runs mean lower
latency, never more content (dedup). Everything the site renders —
the dynamic brief, day archives, weeklies, feeds, entity pages, trends,
`data/alerts.json` — is derived from these files. Contract pointer:
[`entries/README.md`](../entries/README.md); spec: [`docs/pipeline.md`](pipeline.md).

### `entities/registry.yaml` — the global entity registry

The single controlled list of named things the pipeline tracks — actors,
campaigns, malware families, tools, incidents, reports (plus `trend` and
`policy`). Every entry references entities by registry key
(`actor:shinyhunters`); research agents read keys + aliases before naming
anything; the dedup gate matches candidates against keys *and* aliases, so
"UNC6240" and "ShinyHunters" can never become two separately-tracked
things. The main agent appends new entities in the same commit as the
entries that first reference them; keys are permanent (extend aliases,
never rename). Alias collisions and unresolved keys FAIL
`tools/check_run.py`. The site renders `/entities/<key>/` pages from it.
Contract pointer: [`entities/README.md`](../entities/README.md).

### `attack/enterprise-attack.json` — the pinned MITRE ATT&CK dataset

The one ATT&CK Enterprise release every consumer renders and validates
against — a compact, committed extraction (technique id → name, tactics,
definition, sub-technique parentage, lifecycle flags with `revoked_by`
forwarding) from the official `mitre-attack/attack-stix-data` STIX
releases. `tools/attack_data.py` is the only writer (`--check` compares the
pin against the upstream latest, `--update` rewrites it, `--selftest`
verifies invariants — also enforced by `check_run.py`). Entry
`techniques[]` frontmatter is validated against it; `site/build.py`
derives evidence-bound entity/CVE → technique profiles from entries
(frontmatter ∪ legacy in-prose T-ids via
`content_model.entry_technique_ids`), renders the entity-page ATT&CK
sections and the `/attack/` overlap matrix, and exports per-entity ATT&CK
Navigator layers. Revoked techniques are kept and forwarded — the ATT&CK
analogue of registry tombstones, because immutable entries keep citing old
ids. Normative: [`docs/pipeline.md`](pipeline.md) § The ATT&CK layer;
contract: [`attack/README.md`](../attack/README.md).

### `runs/` — per-run records

One file per fire at `runs/<YYYY-MM-DD>/<run-id>.md`, with
`run_id = <YYYY-MM-DD>T<HHMM>Z-<intel|weekly>` (UTC, minute precision,
lexically sortable; a same-minute retry updates the same record —
idempotent). **The run record is the mandatory artifact of every fire** —
zero entries is a healthy quiet window; a missing record is an operational
failure. Frontmatter is the machine-readable telemetry (models per role,
gap/window hours, per-sub-agent allocation, fetch failures, entry counters,
the full verification-loop breakdown — the v2 `run_log.json` entry,
relocated); the body is the human-readable verification & coverage notes
(the v2 brief § 7, relocated), including the parseable `Coverage gaps:` /
`Watchlist:` / `Closed-source intake:` / `Essential-coverage:` lines the
next run's preflight reads. The Ops dashboard at `/ops/` is built entirely
from `runs/**` frontmatter; the rendered brief concatenates the in-window
record bodies as its § Verification Notes. Records migrated from v2 keep
their historical run ids as filenames. Contract pointer:
[`runs/README.md`](../runs/README.md).

### `site/content_model.py` — the shared parser

The single reference implementation for parsing, serialising and
schema-validating all three content types (entries, registry, runs).
Stdlib-only — no PyYAML; it accepts the strict YAML subset defined in
`docs/pipeline.md` § "Frontmatter — strict YAML subset" and refuses
anything outside it. Consumed by `site/build.py`, `tools/check_run.py`
and `tools/migrate_briefs.py`, so the producer (the run prompts) and every
consumer literally share one parser and cannot drift on parsing rules —
the v3 equivalent of v2's "check_brief imports the footer parser from
build.py" discipline, promoted to a first-class module.

### `config/org-profile.yaml` + `tools/compose_prompts.py` — organization parameterization

The deployment's organization-specific values live in one config file:
organization (name, short name, sector, additional sectors, region focus,
home region, description, audience), watchlists (products with
vendor/exposure/criticality, suppliers with relationship/criticality,
standing free-text interests), the vulnerability-triage scheme
(categories with id/name/criteria/response + a default), the
national-CERT single-source carve-out list (`national_certs` — absent key
= upstream default list, `[]` = carve-out disabled), the weekly's
standing policy/regulatory watch (`policy_watch`), the `classification:`
scheme (the NATO Admiralty code + the `triage_kinds` split), and the
`deployment:` section (`site_url` only — there is no visibility/TLP flag).
The defaults reproduce the historical Swiss-federal-SOC deployment;
watchlists and triage ship empty/disabled, which makes those profile-driven
behaviours no-ops.

`tools/compose_prompts.py` (stdlib-only; `--check` / `--write` / `--dump` /
`--selftest`; `--get dotted.key` for single values) renders the profile
into `ORG-PROFILE:BEGIN/END` managed marker blocks inside six files:
[`prompts/cti-run.md`](../prompts/cti-run.md) (mission + audience, the
§ Organization profile & watchlists data block),
[`prompts/weekly-summary.md`](../prompts/weekly-summary.md) (same, plus
the `org-policy-watch` block under W2), `prompts/verification.md` (the
`org-certs` carve-out list), the `cti-research` definition (mission,
audience, watchlist values, `org-certs`), and both verifier definitions
(§ Organization context). The static policy text around the blocks
(anti-overshoot rules, sweep ownership, the `org_triage` frontmatter
spec) lives in the prompts, is deliberately org-neutral, and follows the
normal versioning rule; the generated blocks carry values only and are
exempt from version bumps. In entry output the profile surfaces as
structured frontmatter: `org_triage: {category, rationale}` when a triage
scheme is configured, `classification: {reliability, credibility}` (the NATO
Admiralty code) on every non-triage entry, `watchlist_hit: true` + the
`watchlist` tag when a watchlist match drove inclusion. `site/build.py`
reads the profile's `classification:` block directly at build time (NATO
doctrine fallback when absent) so the rating badge on every finding card,
its tooltip, the `/sources/` legend and the entry-detail assessment panel
render the configured scheme's own name and definitions — the published
badges can never drift from what the agents were instructed to assess.

The same decoupling exists on the site side: `config/branding.yaml`
(loaded by `site/branding_config.py` into `site/build.py`) owns the
published site's identity, theme overrides, logos, chart palettes, feed
slices, trend cohorts, and analytics; `site/branding/` holds downstream
asset files. The shipped config equals the loader's defaults and builds a
byte-identical site. Fork contract: [docs/customization.md](customization.md).

Enforcement is three-layered: the `compose-profile` workflow (below)
composes or fail-louds on push; `tools/check_run.py` carries a
`profile-sync` WARN so a routine run surfaces stale composition; and
CLAUDE.md forbids hand-editing the generated blocks.

The `deployment:` section drives only the Phase 7 site poll
(`compose_prompts.py --get deployment.site_url`); there is no TLP / visibility
gate. For org-internal operation see
[`docs/private-deployment.md`](private-deployment.md).

### `intel/` — closed-source drop folder

Operator-owned feed scripts commit dated folders (`intel/<YYYY-MM-DD>/`)
of front-mattered text documents; the runs detect in-window content in
Phase 0 and spawn a conditional intake sub-agent (S5 on intel runs / W3
weekly) that extracts items with mandatory verbatim evidence quotes and
public-corroboration pivots. Entries cite the documents via
`closed_sources` frontmatter records (`{title, provider, date, ref}`
— referenced, never a fabricated URL). There is no TLP gate — everything
under `intel/` is fair game to process; `check_run.py` only traces citations
back to drop files (`closed-source` WARN), and the verifier `Read`s the drop
files as ground truth for every closed-source claim. Contract:
[`intel/README.md`](../intel/README.md). Empty/absent `intel/` — the
normal state — costs nothing.

### `.claude/agents/` — custom sub-agent definitions

- [`cti-research.md`](../.claude/agents/cti-research.md) — isolated context,
  per-role model bound by the agent definition's YAML frontmatter (operator
  rebindable). Phase 1 (intel run) / Phase 2 (weekly) parallel research
  workers — S1–S4 + conditional S5 intake per intel run, W1–W2 + W3 weekly;
  also reused for verification follow-ups (max 3 per iteration). Embeds the
  `WebFetch` outbound-links template, the `tools/fetch_source.py` contract
  for known-403 hosts, the intelligence-methodology tradecraft, the
  findings-YAML return contract, and the mandatory `**Model:**`
  self-identification line (primary source: the harness-injected model line
  in the agent's own system prompt, which sees the definition's `model:`
  pin; env vars `CLAUDE_FRIENDLY_NAME` / `CLAUDE_MODEL_ID` as marked
  container-default fallback). Before fetching, each
  worker reads `work/<run-id>/prior_coverage.json` (which includes entries
  earlier runs published *today* — an afternoon fire never re-researches
  the morning's entries) and `entities/registry.yaml` (canonical names +
  aliases; genuinely new entities return as `new_entity` suggestions,
  covered stories as `novelty: update-of:<entry-id>`). Appends one TSV line
  per successful fetch to `work/<run-id>/url-liveness.tsv` so
  `tools/check_run.py` can skip redundant HEAD/GETs.
- [`cti-verification.md`](../.claude/agents/cti-verification.md) — read-only,
  isolated context (Opus by default — gatekeeper of the publish gate).
  The Phase 5.7 cold-reader verifier; its scope is **this run's new entries
  plus the run record**. Runs AFTER `tools/check_run.py` exits 0 (cheap
  mechanical gate first), looped iteratively (cap 5, fresh spawn each time,
  no shared memory; each iteration re-runs `check_run.py` between fix and
  re-spawn). Finding categories F1–F16 include frontmatter ⇔ body
  agreement and priority calibration (a false `critical` fires notification
  hooks). Same self-identification contract.
- [`cti-verification-alt.md`](../.claude/agents/cti-verification-alt.md) —
  Sonnet-pinned variant of `cti-verification`. Byte-identical operational
  system prompt below its header note; only the YAML `model:` frontmatter
  differs. The Phase 5.7 loop spawns this on **even iterations** (iter 2,
  iter 4) so model-specific blind spots are caught when the next iteration
  runs on a different model. The two verifier definitions move in lockstep
  — when you edit one, regenerate the other.

### `state/` — the surviving flat state files

v3 retired most of `state/`: coverage is now derived by scanning
`entries/` (was `covered_items.json`), deep-dive rotation from entries
with `deep_dive: true` (was `deep_dive_history.json`), and run telemetry
lives in `runs/**` (was `run_log.json`). `tools/migrate_briefs.py`
performed the one-shot conversion and is kept for provenance. Two files
remain:

- [`state/cves_seen.json`](../state/cves_seen.json) — flat fast-lookup CVE
  index (`{id, title, primary_source_url, first_seen, last_seen}`) for
  sub-agent dedup and the CVE-sync check. Kept flat because a CVE-id
  lookup must not require scanning the entry store.
- `state/source_health.json` — written by
  [`tools/source_health.py`](../tools/source_health.py): bounded history
  (12 runs) of per-source accessibility probes via each source's *actual
  recipe*. Fired by the weekly [`source-health.yml`](../.github/workflows/source-health.yml)
  Action and at the end of every routine run; rendered on `/ops/`. Lets
  demotion logic key off a stable failing pattern instead of one fire's
  luck.

### `sources/` — the curated source list

[`sources/sources.json`](../sources/sources.json) — ~150 entries spanning
national CERTs, vendor TI, vulnerability research, journalism, breach
trackers. Schema:

```jsonc
{
  "id": "stable-id-never-changes",        // referenced from run records
  "publisher": "Display name",
  "url": "https://...",
  "category": ["ch-eu", "vulns", ...],
  "tier": "essential | standard",         // essential = attempted every intel run
  "reliability": "A | B | C | D | E | F",  // NATO Admiralty source-reliability letter
  "language": ["en", "de", ...],
  "status": "active | candidate | demoted",
  "fetch_method": "rss | webfetch | api | bridge",
  "last_successful_fetch": "YYYY-MM-DD | null",
  "consecutive_failures": 0,
  "notes": "history of changes, dated — the record is the recipe"
}
```

`tier: essential` records (national CERTs, CISA, ENISA, …) go into every
intel run's sub-agent slices — a miss is disclosed in the run record and
WARNed by `check_run.py`; `standard` records rotate on a staleness
ranking. The agent maintains the file autonomously per the lifecycle in
the top-level [README](../README.md#source-lifecycle-all-transitions-autonomous);
every edit is recorded in the run record's `sources_changed[]`.

### `tools/` — pipeline and operator helpers

- [`tools/check_run.py`](../tools/check_run.py) — the institutionalised
  Phase 5.5 mechanical gate. Stdlib-only, read-only; **exit 0 is required
  before the verifier spawns and before every commit** that adds entries or
  a run record. `python3 tools/check_run.py <run-id>` validates that run's
  scope (no arg = latest run; `--all` validates the whole content store;
  `--no-link-check` for offline use). Checks (full list in
  [`docs/pipeline.md`](pipeline.md#the-mechanical-gate--toolscheck_runpy)):
  entry schema + taxonomy + registry linkage via `content_model.py`,
  folder-date/`discovered_at`/slug consistency, blocked-URL patterns +
  liveness (honouring `work/<run-id>/url-liveness.tsv`), evidence
  presence/binding, `priority` ⇔ `immediate_action`, cross-run CVE dedup
  (FAIL) + entity-key dedup (WARN), `update_of` resolution + cycle check,
  rolling-24 h composition report (informational), CVE sync with
  `cves_seen.json`, IOC scan, closed-source traceability to `intel/` (no TLP
  gate), org-triage + Admiralty-classification vocabulary/placement,
  run-record completeness + prompt-version cross-check
  against `prompts/CHANGELOG.md`, `sources.json` shape (incl. Admiralty A–F
  `reliability_codes`), essential-coverage, the ATT&CK layer (pinned
  dataset present + invariant-clean is a FAIL; unknown/revoked
  `techniques[]` ids and prose-mapped ids missing from the frontmatter are
  WARNs), and the `site/test_build.py`
  smoke tests. Fix
  recipes: [`prompts/check-run-fixes.md`](../prompts/check-run-fixes.md).
- [`tools/build_prior_coverage.py`](../tools/build_prior_coverage.py) —
  Phase 0 helper: scans `entries/` for the last N days (14 on the intel run
  and the weekly) **including entries earlier runs published today** and
  writes `work/<run-id>/prior_coverage.json` (full records incl. each
  entry's `summary` — the main agent AND the sub-agents read this to load
  every in-window brief for compose-time / fetch-time dedup) +
  `prior_coverage_keys.json` (lean keys-only metadata index). Coverage
  older than the window is caught by the store-wide `state/cves_seen.json`
  metadata check. This machinery is the mechanical heart of the
  no-repetition discipline.
- [`tools/run_summary.py`](../tools/run_summary.py) — Phase 0 helper:
  compact state digest (known CVE ids, active sources, last run + gap
  anchor, fetch-gap rotation candidates, and the rolling-24 h budget
  snapshot — what earlier runs already consumed).
- [`tools/attack_data.py`](../tools/attack_data.py) — builds and updates
  the pinned MITRE ATT&CK dataset `attack/enterprise-attack.json` from the
  official `mitre-attack/attack-stix-data` releases: `--check` (pin vs
  upstream latest — a weekly-run duty), `--update [--version X.Y]`
  (rewrite + printed change summary for the commit body), `--selftest`
  (offline invariants), `--info`. See § `attack/enterprise-attack.json`.
- [`tools/fetch_source.py`](../tools/fetch_source.py) — stdlib-only HTTP
  bridge that re-issues requests with a current desktop-Chrome UA +
  matching client-hint headers. Solves the recurring 403 / 302-to-login on
  high-signal publishers (CISA, the Swiss NCSC Cyber Security Hub) that
  filter the routine's default UA. **Mandatory every run for CISA +
  NCSC.ch** — don't even attempt `WebFetch` there. Structured subcommands
  (`cisa-kev`, `ncsc-csh`, `enisa-euvd`, `bsi-rss/csaf`, `ncsc-nl`,
  `cert-eu`, `cert-fr`, `ico-uk`, `sec-edgar`, `feed`, `msrc`) wrap
  JS-rendered listing pages. Read-only by design: https-only, resolved-IP
  deny list, redirect re-validation, body-size cap.
- [`tools/migrate_briefs.py`](../tools/migrate_briefs.py) — the one-shot
  v2 → v3 migration: decomposed the monolithic briefs into entries
  (discovery timestamps from git history), seeded the registry from
  `covered_items.json`, converted `run_log.json` into run records. Kept in
  the repo for provenance; never runs again.
- [`tools/source_candidates.py`](../tools/source_candidates.py) — walks the
  last 30 days of entries, counts outbound-link hosts, subtracts hosts
  already in `sources.json` + the aggregator allowlist, outputs the top-N
  cited-but-untracked domains. Operator-run, post-hoc, read-only.
- [`tools/source_health.py`](../tools/source_health.py) — the accessibility
  probe behind `state/source_health.json` (see § `state/`). Probes every
  source via its actual recipe — `feed` discovery for RSS, the documented
  bridge subcommand for `api`/`bridge`, browser-UA HEAD→GET for
  `webfetch` — and derives an `action` (`none | needs-bridge |
  needs-demote`) the Ops Health panel floats.
- [`tools/compose_prompts.py`](../tools/compose_prompts.py) — see
  § `config/org-profile.yaml` above.

### `docs/` — operator-facing documentation

System reference for operators, contributors, and curious readers. With one exception nothing here is loaded by the prompts at runtime (that material lives under `prompts/`); the exception is [`docs/pipeline.md`](pipeline.md), which the run prompts reference as the normative data model.

- [`docs/pipeline.md`](pipeline.md) — the normative v3 data model (see the top of this file).
- [`docs/architecture.md`](architecture.md) — this file. End-to-end map of every component.
- [`docs/operating.md`](operating.md) — operator runbook: routine setup, GitHub App, Pages, ops dashboard, troubleshooting.
- [`docs/customization.md`](customization.md) — downstream fork / rebrand guide (two-config model, upstream-merge workflow).
- [`docs/private-deployment.md`](private-deployment.md) — org-internal hosting: private repo + scheduled pull/build/serve.
- [`docs/analytics.md`](analytics.md) — public-facing privacy disclosure (what we measure, what we don't).

### `.github/workflows/` — CI

- [`auto-merge-claude.yml`](../.github/workflows/auto-merge-claude.yml) —
  triggers on push to `claude/**`. The **only** path commits land on `main`;
  fast-forwards when the feature branch is a strict descendant, falls back
  to a regular merge on a true divergence with auto-resolution for
  `state/cves_seen.json`, `state/source_health.json` and
  `entities/registry.yaml` (`--ours` — the routine's fresh state) and
  `sources/sources.json` (`--theirs` — main's curated list). Entry and
  run-record files are per-run unique paths and cannot conflict. Deletes
  the feature branch on success; conflicts outside the auto-resolved paths
  fail loud with `::error::`. **Belongs to the publishing chain; do not
  edit unless you understand the resolution rules in
  [`docs/operating.md`](operating.md#publishing-chain--feature-branch-only).**
- [`deploy-site.yml`](../.github/workflows/deploy-site.yml) — rebuilds the
  site when the build's inputs change: direct pushes to `main` touching
  `entries/**`, `runs/**`, `entities/**`, `state/**`, `sources/**`,
  `docs/**`, `prompts/**`, `README.md`, `site/**`, or the workflow itself
  — plus a `workflow_run` chain from every successful auto-merge (pushes
  by `GITHUB_TOKEN` don't retrigger workflows, so the chain is explicit).
  Runs `site/build.py`, force-pushes `site/_site/` to `gh-pages`.
- [`source-health.yml`](../.github/workflows/source-health.yml) — weekly
  cron (Sundays 04:30 UTC) + `workflow_dispatch`. Runs
  [`tools/source_health.py`](../tools/source_health.py) and commits
  `state/source_health.json` directly to `main` (that path sits in the
  auto-merge auto-resolution allowlist, so a concurrent claude/* push
  won't race). Independent of the routines.
- [`compose-profile.yml`](../.github/workflows/compose-profile.yml) —
  triggers on push touching `config/org-profile.yaml`, the compose script,
  or any composed target. Selftests the compose script, then: on operator
  branches with drift, runs `--write` and commits the composed prompts
  back to the branch; on `main` and `claude/**`, is check-only and fails
  loud (`::error::`) — auto-committing on `claude/**` would race
  `auto-merge-claude.yml`, so the Claude session that edits the config is
  required to compose in the same commit instead.

The four workflows are independent. The site is a *consumer* of the
pipeline's output and never writes back.

### `site/` — the public reader

A stdlib-only Python static-site generator (`site/build.py`, on top of
`site/content_model.py`) emits a real HTML page for every URL. **The brief
is a query**: `/live/` is the live rolling brief — a run-grouped,
reverse-chronological timeline of the last 24 h in which **every run
appears, including quiet (0-finding) ones**. The default window ships
server-rendered and fully no-JS-readable; `assets/js/brief.js` re-renders
the timeline client-side from `data/briefbook.json` (the last ~35 days of
entries) when the reader changes the window selector (6 / 12 / 24 / 48 /
72 h) or loads older findings. Page inventory:

- `/` home (Live / Daily / Weekly brief cards) · `/live/` the live rolling
  brief · `/daily/YYYY-MM-DD/` one settled page per **completed** UTC day
  in the classic editorial section order (the still-rolling day lives only
  in `/live/`) · `/daily/` the newest-first completed-day archive ·
  `/weekly/YYYY-Www/` weekly pages rendered from the week's strategic
  entries (+ `/weekly/` archive).
- `/entries/YYYY-MM-DD/<slug>/` per-entry permalinks (metadata badges,
  update chain, producing-run link).
- `/entities/<key>/` unified entity pages from the registry + CVE
  universe — including the derived ATT&CK-technique section and a
  per-entity Navigator layer (`attack-layer.json`); `/cves/` and
  `/topics/` type-filtered list views (legacy per-id URLs are
  meta-refresh redirect stubs to the canonical).
- `/attack/` the ATT&CK coverage matrix (pinned release, store-wide heat,
  per-technique definitions + evidence directory, client-side
  multi-entity TTP overlap over `data/attack.json`).
- `/sources/` + `/sources/<id>/`, `/tags/<t>/`, `/regions/<r>/`,
  `/trends/` (entries-per-ISO-week cohort dashboard), `/ops/` (run
  telemetry from `runs/**`), `/feeds/`, `/about/**` (README, docs,
  prompts rendered as pages).
- Eleven RSS feeds: `feed.xml` (one item per day page), `feed-weekly.xml`,
  `feed-items.xml` (one item per entry — `<pubDate>` is the entry's
  `discovered_at`, true discovery latency, not commit time) + eight sector
  slices (`feed-public-sector.xml`, `feed-healthcare.xml`,
  `feed-finance.xml`, `feed-energy.xml`, `feed-ot-ics.xml`,
  `feed-defense.xml`, `feed-telco.xml`, `feed-education.xml`).
- Data islands: `data/briefbook.json` (the `/live/` client payload —
  Phase 7 polls it for the run id), `data/alerts.json` (last 7 days of
  `critical`/`high` entries with headline, summary, `immediate_action`,
  entities, CVEs — the notification-hook surface), `data/search.json`,
  `data/site.json`.

The site is read-only with respect to the rest of the repo: it reads
`entries/`, `entities/`, `runs/`, `state/`, `sources/`, `README.md`,
`docs/*.md`, `prompts/*.md` and `site/taxonomy.yaml`, and writes only
under `site/_site/` (gitignored locally; force-pushed to `gh-pages` by
CI). JavaScript only enhances — with JS disabled every page, including
the default `/live/` window, is fully readable. Internals:
[`site/README.md`](../site/README.md).

[`site/taxonomy.yaml`](../site/taxonomy.yaml) is the controlled vocabulary
for every entry-frontmatter value (themes / sectors / regions / nexus /
cve_types / cve_vectors / cve_auth / cve_status). The build and
`check_run.py` refuse any entry using a value not in this file.

## Data flow per intel run

The weekly run shares this machinery verbatim (it `Read`s `cti-run.md` at
runtime); it differs in Phase 1 (a local week-in-review pass over the
window's operational entries) and its research fan-out (W1–W2 + W3).

```
 ┌──────────────┐  Phase 0     ┌───────────────────────────────────────┐
 │  intel run   │─────────────▶│ compute RUN_ID (YYYY-MM-DDTHHMMZ-intel)│
 │  fires       │  preflight   │ build_prior_coverage.py → work/<id>/  │
 │  (N×/day,    │              │   prior_coverage{,_keys}.json          │
 │  operator-   │              │   (last 14 days INCL. earlier runs     │
 │  scheduled)  │              │    today — main agent loads all)       │
 └──────────────┘              │ run_summary.py → state digest +        │
                               │   rolling-24 h budget snapshot         │
                               │ Read entities/registry.yaml + taxonomy │
                               │ gap → window_hours (self-healing)      │
                               │ detect intel/<date>/ drops (⇒ S5)      │
                               └──────────┬────────────────────────────┘
                                          │ spawn in parallel (isolated
                                          ▼ contexts; xhigh effort, 45-min cap)
 ┌────────────────────────────────────────────────────┐
 │ S1 active threats & trending vulns  (+product sweep)│
 │ S2 home region & sector                             │
 │ S3 research & investigative reporting               │
 │ S4 incidents & disclosures        (+supplier sweep) │
 │ S5 closed-source intake             (conditional)   │
 │  each: reads prior_coverage + registry BEFORE       │
 │  fetching; writes work/<id>/findings.<Sn>.yaml +    │
 │  url-liveness.tsv appends + .ended_at checkpoint    │
 └──────────┬─────────────────────────────────────────┘
            ▼ all returned or capped (compose-after-return gate)
 ┌────────────────────────────────────────────────────┐
 │ Phase 2 — verification & triage (main context)      │
 │  URL spot-checks · two-source/carve-outs ·          │
 │  fake-news guard · CVE verify · dedup ⇒ new entry   │
 │  vs update_of vs drop · recency re-check ·          │
 │  relevance/actionability gate · rank ⇒ priority     │
 │ Phase 3 — deep-dive selection (reserved for items   │
 │  that earn it; category rotation from prior entries)│
 └──────────┬─────────────────────────────────────────┘
            ▼
 ┌────────────────────────────────────────────────────┐
 │ Phase 4 — compose (strictly from findings files)    │
 │  Write entries/<date>/<slug>.md   (one per finding, │
 │    immutable; updates as update_of entries)         │
 │  Write runs/<date>/<run-id>.md    (telemetry front- │
 │    matter + verification-notes body)                │
 └──────────┬─────────────────────────────────────────┘
            ▼
 ┌────────────────────────────────────────────────────┐
 │ Phase 5 — state update                              │
 │  entities/registry.yaml   (new entities + aliases)  │
 │  state/cves_seen.json     (CVE index sync)          │
 │  sources/sources.json     (lifecycle bookkeeping)   │
 │  state/source_health.json (recipe-level probe)      │
 └──────────┬─────────────────────────────────────────┘
            ▼
 ┌────────────────────────────────────────────────────┐
 │ Phase 5.5 — mechanical gate                         │
 │  python3 tools/check_run.py "$RUN_ID"               │
 │  (schema/taxonomy/registry/dedup/budgets/evidence/  │
 │   priority⇔immediate_action/IOC/classification/     │
 │   liveness/run-record completeness + site smoke)    │
 │  exit != 0 → fix and re-run; no verifier, no commit │
 └──────────┬─────────────────────────────────────────┘
            ▼
 ┌────────────────────────────────────────────────────┐
 │ Phase 5.7 — verifier loop (≤5 iterations)           │
 │  odd iters: cti-verification (Opus)                 │
 │  even iters: cti-verification-alt (Sonnet) + the    │
 │    prior-iteration deltas block                     │
 │  scope: this run's entries + run record             │
 │  NEEDS_FIXES → remediate (incl. dropping entries)   │
 │    → re-run check_run.py → fresh re-spawn           │
 │  CLEAN → publish · iter 5 NEEDS_FIXES → fail-open,  │
 │    residuals recorded in the run record             │
 └──────────┬─────────────────────────────────────────┘
            ▼
 ┌────────────────────────────────────────────────────┐
 │ Phase 6 — commit entries/ runs/ registry state      │
 │  sources work/<run-id>/ (+ .claude/memory/) on the  │
 │  claude/<name> branch · sync origin/main (state/* + │
 │  registry → ours, sources → theirs) · push w/ retry │
 │ Phase 7 — publish verification (10-min budget):     │
 │  poll run record on origin/main, then                │
 │  <site>/data/briefbook.json for the RUN_ID           │
 └────────────────────────────────────────────────────┘
```

The agent never bypasses any of these phases — Phase 0 is a hard
prerequisite for Phase 1, Phase 5 (state update) for Phase 5.5 (the
mechanical gate), which gates Phase 5.7 (the verifier), which gates
Phase 6 (commit). The run record is written even when everything else
fails — a fire that produced neither entries nor a record is the worst
outcome the prompts are engineered against.

## Adding a new component

A safe pattern for extending the system without affecting the runs:

1. **Site-only feature** (new view, new search facet). Edit `site/`. The
   pipeline's runs are untouched.
2. **New entry-frontmatter field.** Specify it in `docs/pipeline.md`
   first, add it to `site/content_model.py` (parser + validator) and
   `tools/check_run.py`, then teach the prompts' Phase 4 to populate it
   and `site/build.py` to render it. Existing entries stay valid because
   new fields are optional with a documented default — entries are
   immutable, so a migration rewrite is not an option.
3. **New source category.** Add the records to `sources/sources.json` and
   extend the category filter in `prompts/cti-run.md` Phase 1 so a
   sub-agent slice picks them up. The site's source catalogue follows on
   the next build automatically.
4. **New routine** (e.g. a monthly horizon scan). Add a prompt under
   `prompts/` (follow the weekly's pattern: build on `cti-run.md`, define
   only the divergences), create a routine pointing at it, and extend the
   run-id `kind` vocabulary in `docs/pipeline.md` + `content_model.py`.

Anything more invasive (new content type, new repo layout) — update
`docs/pipeline.md` first (it is normative; code follows it), write down
the reasoning in the commit message, and bump the prompt version with a
CHANGELOG entry explaining the *why*. The prompts and the data-model spec
are the load-bearing parts of the system; small contract changes are easy
to ship by accident and hard to roll back — not least because published
entries are immutable.
