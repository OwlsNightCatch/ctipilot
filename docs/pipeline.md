# The intelligence pipeline — data model (v3, normative)

This document is the single normative specification of the v3 content model:
per-finding **entries**, the **entity registry**, and per-run **run records**.
Every producer (the run prompts, the migration tool) and every consumer
(`site/build.py`, `tools/check_run.py`, the verifier agents) implements
exactly this contract. If code and this document disagree, this document
wins and the code is the bug.

## Why this model exists

v2 produced one monolithic Markdown brief per day. That capped intelligence
latency at the routine cadence: something disclosed at 09:00 waited for the
next morning's fire. v3 turns the product into a **pipeline**: the run
prompt (`prompts/cti-run.md`) can fire any number of times per day, each
fire publishes only the *new* verified signal since the previous fire as
individual entry files, and the "brief" is a **rendering** over a reader-
chosen time window (default: last 24 h). Because every finding is a
standalone file with complete structured metadata, downstream automation
(notification hooks on `priority: critical`, sector feeds, entity timelines,
trend analytics) consumes the pipeline directly — no Markdown scraping.

Two properties are non-negotiable and carried over from v2 unchanged:

1. **More runs must not mean more content.** Entry volume is governed by a
   strict relevance/actionability gate (see § Relevance discipline), not by a
   numeric target or ceiling: the rolling-24-hour window carries exactly the
   entries that clear that gate, however few or many that is. Firing more
   often changes latency, never volume — dedup guarantees a re-scan of the
   same window republishes only the new delta. A run that finds nothing new
   publishes nothing but its run record — that is a healthy outcome.
2. **Everything published passed the same gates** — two-source
   verification, fake-news guard, URL truth, taxonomy validation, the
   mechanical self-check, and the adversarial verifier loop.

## Repository layout (v3)

```
entries/YYYY-MM-DD/<slug>.md   # one finding per file; folder = UTC date of discovered_at
entries/README.md              # short contract pointer (this file is normative)
entities/registry.yaml         # global entity registry: actors, campaigns, malware, tools, incidents, reports
entities/README.md             # registry contract pointer
runs/YYYY-MM-DD/<run-id>.md    # one run record per fire: frontmatter = telemetry, body = verification notes
runs/README.md                 # run-record contract pointer
state/cves_seen.json           # flat fast-lookup CVE index (kept from v2)
state/source_health.json       # source accessibility snapshots (kept from v2)
sources/sources.json           # curated source list (kept from v2)
work/<run-id>/                 # per-run forensic artefacts (kept from v2)
site/content_model.py          # THE shared parser/loader/validator for entries, registry, runs
```

Retired from v2 (no backwards compatibility): `briefs/` (migrated into
`entries/` by `tools/migrate_briefs.py`, then deleted),
`state/covered_items.json` (coverage is now derived by scanning `entries/`),
`state/deep_dive_history.json` (derived from entries with `deep_dive: true`),
`state/run_log.json` (replaced by `runs/`).

## Run identity — multiple runs per day

```
run_id = <YYYY-MM-DD>T<HHMM>Z-<kind>      kind ∈ { intel, weekly }
e.g.     2026-07-03T0412Z-intel           runs/2026-07-03/2026-07-03T0412Z-intel.md
```

- UTC, minute precision. Lexically sortable. Deterministic: a same-minute
  retry computes the same `run_id` and updates the same record in place
  (idempotent retry, same rationale as v2's sha8 scheme).
- `work/<run-id>/` uses the identical string.
- Migrated v2 runs keep their historical ids (`2026-07-03-04ba8283`,
  `2026-W26-b78503e7`) as filenames under `runs/<date>/`; only new runs use
  the timestamped form. Consumers treat `run_id` as an opaque sortable string
  and read timing from the frontmatter, never by parsing the id.

## Entry files — the atomic intelligence unit

Path: `entries/<YYYY-MM-DD>/<slug>.md` where the folder date is the UTC date
of `discovered_at` and `<slug>` is kebab-case, `[a-z0-9-]`, ≤ 60 chars,
unique within the day. The **entry id** is path-derived:
`<YYYY-MM-DD>/<slug>` (e.g. `2026-07-03/coolify-cve-2026-34038-rce`).
There is no `id` frontmatter field — the path is the identity.

**Entries are immutable once committed.** A later run never edits a
published entry. New information on a covered story becomes a **new entry**
with `update_of: <original entry id>` — the v2 "UPDATE (originally covered
YYYY-MM-DD)" rule generalised to any granularity, including two runs on the
same day. Corrections likewise ship as update entries, never as rewrites.

### Frontmatter — strict YAML subset

The frontmatter block is parsed by `site/content_model.py` (stdlib-only —
no PyYAML). It accepts a strict subset of YAML: 2-space indentation, no
tabs, no flow style except `[]` / inline `[a, b]` lists of plain scalars,
`- ` list items (scalar or single-level mapping), one level of nested
mapping for block fields, `>`/`|` block scalars, `null`/`true`/`false`
literals, full-line comments only. Producers MUST stay inside this subset;
`tools/check_run.py` fails the commit on anything the parser rejects.

```yaml
---
schema: 1
kind: vulnerability            # see § Kinds
horizon: operational           # operational | strategic
title: "CVE-2026-34038 — Coolify: authenticated command injection to RCE (CVSS 9.9)"
headline: "Coolify ships an emergency fix for a CVSS 9.9 authenticated command-injection RCE"
summary: >
  Self-contained 1–3 sentence summary naming products, regions and CVEs.
  This is the TL;DR bullet body, the RSS description, and the notification
  text — a reader who sees ONLY this must know what is affected and why it
  matters.
discovered_at: "2026-07-03T04:21:09Z"   # UTC moment this run verified the finding
event_date: "2026-07-02"                # date of the underlying event / primary publication
run_id: 2026-07-03T0412Z-intel
priority: high                 # critical | high | notable | routine — see § Priority
immediate_action: null         # or the block below — presence ⇔ priority: critical
# immediate_action:
#   title: "Patch Coolify to ≥ v4.0.0-beta.469 now"
#   action: >
#     One-to-three sentences: the specific time-critical defender action
#     (emergency patch, isolation, credential rotation, emergency rule).
tags: [vulnerabilities, rce, patch-available]   # taxonomy themes ∪ nexus
regions: [global]              # taxonomy regions
sectors: [technology]          # taxonomy sectors (may be empty)
entities: []                   # registry keys, e.g. [actor:shinyhunters, campaign:fortibleed]
cves:                          # [] when the entry carries no CVE
  - id: CVE-2026-34038
    cvss: "9.9"                # string; "n/a" when unassigned
    epss: null
    type: rce                  # taxonomy cve_types
    vector: zero-click         # taxonomy cve_vectors
    auth: post-auth            # taxonomy cve_auth
    status: [patch-available]  # taxonomy cve_status
    affected: "≤ 4.0.0-beta.462"
    fixed: "4.0.0-beta.469"
sources:
  - url: "https://github.com/coollabsio/coolify/security/advisories/GHSA-qqrq-r9h4-x6wp"
    publisher: "coollabsio GHSA"
    date: "2026-07-02"
    role: primary              # primary | corroborating — first source is the most primary
closed_sources: []             # [{title, provider, date, tlp, ref}] — intel/ drop citations, never URLs
evidence:                      # verbatim quotes binding claims to fetched sources
  - quote: "An authenticated remote command injection vulnerability (CWE-78) in Coolify…"
    publisher: "coollabsio GHSA"
verification: multi-source     # multi-source | single-source | single-source-national-cert |
                               # single-source-victim | contradicted
sourcing_note: null            # human clause, e.g. "victim-own SEC 8-K disclosure carve-out"
confidence: high               # high | medium | low
update_of: null                # entry id when this is an update note on prior coverage
references: []                 # entry ids this entry synthesises / builds on (weekly synthesis)
weekly_section: null           # strategic entries only: explicit weekly render section
                               # (weekly-top-stories | weekly-multi-day | weekly-vuln-rollup |
                               #  weekly-sector-patterns | weekly-incidents-recap | weekly-research |
                               #  weekly-annual-reports | weekly-long-running | weekly-policy |
                               #  weekly-looking-ahead); unset -> kind-based default placement
deep_dive: false               # true ⇒ this entry IS the deep-dive treatment
deep_dive_category: null       # taxonomy-free rotation slug when deep_dive: true (see prompt)
org_triage: null               # or {category: P1, rationale: "…"} when the org profile defines a scheme
watchlist_hit: false           # true only when inclusion was driven by an org-profile watchlist match
actions: []                    # imperative, entry-specific defender actions (strings) — feed § Action Items
migrated_from: null            # v2 provenance (briefs/YYYY-MM-DD.md) — migration tool only
---

Body: the full analysis in Markdown. Inline source links at the point of
claim (`([Publisher, YYYY-MM-DD](URL))`), defender takeaway, detection and
hardening concepts, MITRE ATT&CK IDs — the same technical register and
depth as a v2 brief item. Deep-dive entries carry the complete deep-dive
narrative (Background paragraph, kill chain, hunt concepts, mitigation).
No IOCs, no rule code, no vanity metrics, English only.
```

### Field semantics and hard rules

- **`headline`** — bold-lead TL;DR headline, ≤ 120 chars, no trailing period.
- **`summary`** — the load-bearing standalone digest. Never empty.
- **`discovered_at`** — the moment *this pipeline* verified the finding, set
  once, never backdated. The folder date MUST equal its UTC date.
- **`event_date`** — recency anchor of the underlying event (primary-source
  publication date). Drives staleness checks; `discovered_at` drives windows.
- **`entities`** — every value MUST resolve to a key in
  `entities/registry.yaml`. New entities are added to the registry in the
  same commit. Never invent a second key for a known entity — check aliases.
- **`cves[]`** — one record per CVE, always with `type`/`vector`/`auth`/
  `status` from the taxonomy. Multi-CVE items carry one record per CVE
  (the v2 "per-CVE breakdown" is now structural).
- **`sources[]`** — ≥ 1 unless `closed_sources` is non-empty. First entry is
  the most primary (vendor PSIRT > vendor research blog > research-lab post >
  regulator filing > victim disclosure > national CERT/CSIRT > MITRE/NVD >
  ENISA EUVD > news). Homepage / listing / category / per-CVE-database URLs
  are FAIL-blocked (same pattern list as v2, in `tools/check_run.py`).
- **`evidence[]`** — required when any CVE `status` includes `exploited` and
  on every `immediate_action` entry. Each quote must be a verbatim substring
  of a page fetched this run, attributed to a listed source's publisher.
- **`verification`/`sourcing_note`** — `single-source*` values replace the v2
  `[SINGLE-SOURCE]` heading flag; renderers surface them as badges.
- **`update_of`** — must resolve to an existing earlier entry. An update
  entry re-states only the delta, never recaps. Long-running campaigns get
  ≤ 1 consolidated update per week unless something critical changes.
- **`actions[]`** — only actions derived from this entry's own content.
  The rendered brief's § Action Items is the union over the window.
- **`priority` + `immediate_action`** — see next section.

### Priority — the notification surface

| value | meaning | rendering |
|---|---|---|
| `critical` | "stop reading and act now" — the v2 Immediate-Action bar, unchanged and still intentionally extremely high | callout above TL;DR; `immediate_action` block REQUIRED; notification hooks fire |
| `high` | leads the window — a reader who reads only the TL;DR must see it | TL;DR bullet (headline + summary) |
| `notable` | standard item | section body |
| `routine` | marginal but worth the record (e.g. hygiene CVE kept for awareness) | section body, after notable |

`priority: critical` ⇔ `immediate_action` present (both directions —
enforced by `tools/check_run.py`). The bar for `critical` is ALL of: newly
disclosed or newly weaponised; actively exploited right now or mass
exploitation imminent / campaign underway with confirmed impact; defender
action time-critical to the hour or day. Criticals are rare *by
construction* — that bar is extreme, not because a count caps them. Two
`critical` entries in a rolling 24 h is legitimate only when each
independently clears every element of the bar.

### Kinds — what renders where

| `kind` | daily-brief section (operational horizon) | weekly section (strategic horizon) |
|---|---|---|
| `threat` | § 1 Active Threats, Trending Actors, Notable Incidents & Disclosures | § Highest-impact / § Long-running via synthesis |
| `incident` | § 1 (same section, incident/disclosure flavour) | § Incidents & disclosures recap |
| `vulnerability` | § 2 Trending Vulnerabilities | § Vulnerability roll-up |
| `research` | § 3 Research & Investigative Reporting | § Research & threat-actor developments |
| `annual-report` | § 3 (one-time treatment per PD-9) | § Annual / periodic threat reports |
| `policy` | — (strategic only) | § Policy & regulatory horizon |
| `synthesis` | — (strategic only) | § Multi-day campaigns / § Sector patterns / § Long-running campaigns |
| `outlook` | — (strategic only) | § Looking ahead |

Orthogonal flags relocate an entry at render time: `update_of` ⇒ § Updates
to Prior Coverage; `deep_dive: true` ⇒ § Deep Dive (and not its kind
section). `horizon: operational` entries come from intel runs;
`horizon: strategic` from weekly runs. The daily/window view renders
operational entries only; the weekly view renders the week's strategic
entries plus the operational entries its `synthesis` entries `reference`.

## Relevance discipline — volume follows relevance, not cadence or a count

Entry volume is **not fixed** — there is no per-run, per-day, or
rolling-24-hour target or ceiling. The rolling 24-hour window across all
runs carries exactly the entries that clear the intel run's strict
relevance/actionability gate (`prompts/cti-run.md` PD-11), however few or
many the window's genuine signal turns out to be. A quiet day is a handful
of entries or none; a day with several unrelated actively-exploited edge
RCEs plus a home-region incident is legitimately larger. The reader is
protected from overflooding by the **gate**, not by a quota: every entry
must earn its place, and a marginal item is dropped no matter how much room
a numeric budget would have allowed.

The gate is applied for two properties of **equal weight**:

- **Sound** — everything published is relevant, accurate, and actionable;
  very low false positives; no marginal, off-scope, or unverified item.
- **Complete** — everything genuinely relevant to the reader's job is
  published; very low false negatives; a reader relying on ctipilot.ch alone
  has no blind spot on anything that matters to their work. The gate removes
  noise, never signal — a relevant item is never dropped to keep the count
  down (there is no count to keep down).

A missed relevant item is as serious a failure as an included marginal one —
and a silent one, since the reader never sees what they were not told — so
completeness is verified deliberately (the intel run's Phase 2 completeness
sweep; the verifier's coverage + missed-angle checks), not assumed.

- Each `vulnerability` entry must demand action **beyond the regular patch
  cycle** — actively exploited, imminent mass exploitation, pre-auth RCE on
  an exposed edge with public PoC, or another out-of-band response. A CVE
  the normal patch cadence already handles, with no exploitation or
  exposure-driven urgency, is out of scope even at high CVSS.
- **Deep-dive treatment** is reserved for an item that earns the long form
  (see the intel prompt's Phase 3 criteria); it is rare by construction, not
  by quota. Category rotation is derived from the last 30 days of
  `deep_dive: true` entries. Most UTC days carry one deep dive, some none;
  a second on one day is legitimate only when it independently earns the
  treatment, with the reason in the run record.
- **`priority: critical`** is governed by its own extreme bar (§ Priority),
  not by a count — criticals stay rare because the bar is high.
- Every run reads the window's already-published entries first (including
  earlier runs the same day) and publishes only the delta — so more runs
  mean lower latency, never more content. An empty run publishes only its
  run record.
- `tools/check_run.py` reports the rolling-24-hour composition (operational
  count, deep dives today, criticals) for the operator's awareness; it does
  **not** flag a count as an exceedance.

## Entity registry — `entities/registry.yaml`

The global controlled list of *named things* the pipeline tracks, so every
entry links the same real-world entity to the same key and duplicates
cannot creep in. Research and verification agents read it; the main agent
extends it (same commit as the entries that need the new key).

```yaml
schema: 1
entities:
  - key: actor:shinyhunters
    type: actor                # actor | campaign | malware | tool | incident | report
    name: "ShinyHunters"
    aliases: ["UNC6240"]       # every public alias; dedup checks match against these too
    nexus: null                # taxonomy nexus value when publicly attributed, else null
    summary: >
      One-to-three sentence definition: who/what this is, first public
      reporting, why the pipeline tracks it.
    first_seen: "2026-05-12"   # first pipeline coverage (entry date)
```

Entity types: `actor | campaign | malware | tool | incident | report |
trend | policy` (`trend` tracks named vulnerability/technique waves,
`policy` tracks named regulatory items — both inherited from v2 coverage
tracking).

Rules: `key` is `<type>:<kebab-slug>`, globally unique, never renamed once
published (entries reference it). Aliases must not collide with another
entity's key, name, or aliases (`check_run.py` FAILs). CVEs are NOT
registry entities — `state/cves_seen.json` and per-entry `cves[]` carry the
CVE model. Regions, sectors and theme tags stay in `site/taxonomy.yaml`.
Definitions follow sourcing rules: the `summary` states only what cited
public reporting supports (attribution stays claim-attributed).

## Run records — `runs/YYYY-MM-DD/<run-id>.md`

One file per fire, written in the run's final phase. Frontmatter is the
complete machine-readable telemetry record (the v2 `run_log.json` entry,
relocated); the body is the human-readable **verification & coverage
notes** — the v2 brief § 7, relocated to a dedicated, per-run home.

```yaml
---
schema: 1
run_id: 2026-07-03T0412Z-intel
kind: intel                    # intel | weekly
date: "2026-07-03"
started: "2026-07-03T04:12:03Z"
completed: "2026-07-03T04:31:40Z"
duration_seconds: 1177
model: "…"                     # main-agent friendly name (env-var self-identification)
model_id: "…"
prompt_version: "v3.1"
window_hours: 24               # gap-derived recency window this run covered (24 h floor)
gap_hours: 7                   # hours since the previous run record
entries_published: 3           # new entry files this run (incl. updates)
entries_updated: 1             # of which update_of entries
deep_dive: null                # entry id of a deep-dive entry published this run, or null
sub_agents:                    # S1–S4 (+S5) / W1–W2 (+W3): identical shape to v2
  S1:
    model: "…"
    model_id: "…"
    started_at: "…"
    ended_at: "…"
    duration_seconds: 279
    sources_attempted: [cisa-kev, bsi-de]
    sources_used: [cisa-kev]
    items_returned: 2
    returned: true
    telemetry: {webfetch_calls: 8, websearch_calls: 0, bridge_fetches: 14}
fetch_failures: []             # rich v2 shape: {id, url_tried, fetch_method, status_code,
                               #  error_class, error_message, attempted_methods, mitigation_applied, covered_anyway}
bridge_uses: []                # {id, method, outcome}
sources_changed: []            # {id, change, from, to, reason}
entities_added: []             # registry keys added this run
entries_dropped_by_verification: 0
verification_iterations: 1
verification_residual_count: 0 # never 0 when the final iteration was NEEDS_FIXES
verification:
  iterations:
    - n: 1
      model: "…"
      model_id: "…"
      started_at: "…"
      ended_at: "…"
      duration_seconds: 240
      verdict: CLEAN           # CLEAN | NEEDS_FIXES
      truth: 0                 # F1–F4 + F13–F15
      editorial: 0             # F5–F10 + F12 + F16
      advisory: 0              # F11
      findings: []             # rich per-finding records, v2 shape
---

## Verification & coverage notes

The v2 § 7 content, per run: borderline drops with reasons, single-source
items and their carve-outs, reduced-confidence inclusions, contradictions,
out-of-window drops, stalled sub-agents, and the parseable lines —
`Coverage gaps: …`, `Watchlist: …`, `Closed-source intake: …`,
`Essential-coverage: …`, budget-exceeded justifications.
```

The rendered window brief concatenates the run-record bodies of every run
in the window as its § Verification Notes, newest first. The Ops dashboard
is built entirely from `runs/**` frontmatter.

## Dedup across runs — how overlap is prevented

1. **Preflight scan.** Every run builds
   `work/<run-id>/prior_coverage.json` by scanning `entries/` for the last
   14 days **plus everything already published today** (multiple-runs-a-day
   is just more records in the same scan). Records carry: entry id, title,
   headline, `summary`, kind, CVE ids, entity keys, primary URL,
   `discovered_at`. The `summary` makes the file a load of every in-window
   brief, not just a key list.
2. **Compose-time dedup (in-context, 14 days).** The main agent `Read`s the
   full `prior_coverage.json` — every in-window brief loaded into context —
   and drops any candidate whose CVE ids or entity keys match an in-window
   entry from **any** run in those 14 days, unless it ships as `update_of`
   with a genuine delta.
3. **Metadata check (store-wide, older than 14 days).** Coverage older than
   the 14-day in-context window is caught by the store-wide CVE index
   (`state/cves_seen.json`, surfaced as `cves.ids` in the state summary),
   not an in-context read — an old CVE re-surfacing is still recognised.
4. **Fetch-time dedup.** Research sub-agents read `prior_coverage.json`
   before fetching and skip already-covered items unless they hold a
   material delta.
5. **Mechanical gate.** `tools/check_run.py` FAILs a new non-update entry
   whose CVE set intersects a prior entry from the last 14 days, and WARNs
   on entity-key overlap, forcing the update_of decision to be explicit.

## Rendering — the brief is a query

- **`/brief/`** — the dynamic brief. Reader picks *last N hours* (6 / 12 /
  24 / 48 / 72) or *since a date*; default **24 h**. The page ships with the
  default window server-rendered (full content, no-JS readable); JS
  re-assembles the same section structure client-side from
  `data/briefbook.json` (last ~35 days of entries with server-pre-rendered
  HTML bodies + full metadata + run-record notes). Section order matches
  a v2 daily brief exactly: TL;DR (+ Immediate-Action
  callout) → Active Threats → Trending Vulnerabilities → Research →
  Updates → Deep Dive → Action Items → Verification Notes.
- **`/briefs/YYYY-MM-DD/`** — static per-day archive page (that UTC day's
  operational entries in the same structure). The browsable historical
  record; daily RSS keys on these.
- **`/weekly/YYYY-Www/`** — static weekly page: the week's strategic
  entries in the 12-section weekly structure, with referenced operational
  entries linked in place.
- **`/entries/YYYY-MM-DD/<slug>/`** — per-entry permalink.
- **Feeds** — `feed-items.xml` (one item per entry, `<pubDate>` =
  `discovered_at` — true discovery latency, not commit time) + the eight
  sector slices + daily/weekly digest feeds.
- **`data/alerts.json`** — last 7 days of `critical`/`high` entries with
  headline, summary, immediate_action, entities, CVEs: the notification-
  hook surface.
- **Entity pages, trends, ops, search** — all derived from entries +
  registry + runs, same URLs as v2.

## The mechanical gate — `tools/check_run.py`

Replaces `tools/check_brief.py`. Read-only, stdlib-only, exit 0 required
before the verifier spawns and before every commit. Validates: frontmatter
parses and every field is schema- and taxonomy-valid; folder-date/
discovered_at/slug consistency; source-URL block-list + liveness (honouring
`work/<run-id>/url-liveness.tsv`); evidence shape/presence; priority ⇔
immediate_action consistency; entity refs resolve; registry integrity;
update_of resolution; cross-run dedup; rolling-24 h composition (reported,
not gated on a count); CVE sync with `cves_seen.json`; IOC scan; run-record completeness (incl. verification
counters and prompt-version cross-check against `prompts/CHANGELOG.md`);
`sources/sources.json` shape; TLP ceiling on closed-source citations; and
the site smoke tests (`site/test_build.py`).


