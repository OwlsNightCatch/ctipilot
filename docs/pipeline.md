# The intelligence pipeline — data model (v4, normative)

This document is the single normative specification of the content model:
per-finding **entries** (one living record per finding, with a dated
changelog), the **entity registry**, and per-run **run records**. Every
producer (the run prompts, the migration tools) and every consumer
(`site/build.py`, `tools/check_run.py`, the verifier agents) implements
exactly this contract. If code and this document disagree, this document
wins and the code is the bug.

**v4.0 (2026-08-27) in one paragraph.** Two routines remain — the intel run
(`prompts/cti-run.md`, any cadence) and the quality audit
(`prompts/quality-audit.md`); the weekly strategic routine is retired and
its `/weekly/` pages are gone (its `horizon: strategic` entries stay in the
store as archived permalinks). A finding has exactly **one** entry for its
whole life: developments, corrections and improvements are appended to that
entry as timestamped `updates[]` changelog records with matching body
sections, `updated_at` floats the entry back to the top of the live brief,
and the old `update_of` second-entry mechanism is retired (the historical
update entries were folded into their roots by `tools/migrate_updates.py`).
See § Entry lifecycle.

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

## Repository layout

```
entries/YYYY-MM-DD/<slug>.md   # one finding per file; folder = UTC date of discovered_at
entries/README.md              # short contract pointer (this file is normative)
entities/registry.yaml         # global entity registry: actors, campaigns, malware, tools, incidents, reports
entities/README.md             # registry contract pointer
attack/enterprise-attack.json  # pinned MITRE ATT&CK release (see § The ATT&CK layer)
attack/README.md               # ATT&CK dataset contract + update procedure
runs/YYYY-MM-DD/<run-id>.md    # one run record per fire: frontmatter = telemetry, body = verification notes
runs/README.md                 # run-record contract pointer
state/cves_seen.json           # flat fast-lookup CVE index (kept from v2)
state/source_health.json       # source accessibility snapshots (kept from v2)
state/warning_acknowledgments.json  # audit-reviewed ledger of settled-history check_run.py WARNs (v3.28)
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
run_id = <YYYY-MM-DD>T<HHMM>Z-<fire>      fire ∈ { intel, audit }   (weekly: legacy records only)
e.g.     2026-07-03T0412Z-intel           runs/2026-07-03/2026-07-03T0412Z-intel.md
```

- UTC, minute precision. Lexically sortable. Deterministic: a same-minute
  retry computes the same `run_id` and updates the same record in place
  (idempotent retry, same rationale as v2's sha8 scheme).
- The suffix names the **fire type** and the frontmatter `kind` carries the
  same value. A v4+ fire is `intel` or `audit` (`content_model.ACTIVE_RUN_KINDS`);
  `weekly` remains in the validated vocabulary only so the historical weekly
  run records keep validating — the weekly routine was retired in v4.0 and
  `check_run.py` FAILs a new record carrying it. (v3.24 made audit fires
  `kind: audit`; before that they carried `kind: intel` with the `-audit`
  suffix as the only discriminator.) Consumers distinguish run types by
  `kind`; the run-id suffix stays as the human-readable mirror.
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

**One entry per finding, for the finding's whole life.** The entry is the
single living record of the finding: a later run (an intel fire or the
quality audit) that learns something new about it, finds an error in it, or
can make it more precise **edits this same file** — appending a dated
`updates[]` changelog record and a matching `## <Type> — <at>` body section,
bringing the frontmatter to the current truth, and bumping `updated_at`.
There is never a second entry for the same finding, and there is never a
silent edit: every change is a record the reader and the gate can see.
Three things never change once published — the entry id/path,
`discovered_at` (first publication) and `run_id` (the originating fire).
Full contract: § Entry lifecycle.

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
horizon: operational           # always `operational` on v4+ entries (`strategic` = legacy weekly entries)
title: "CVE-2026-34038 — Coolify: authenticated command injection to RCE (CVSS 9.9)"
headline: "Coolify ships an emergency fix for a CVSS 9.9 authenticated command-injection RCE"
summary: >
  Self-contained 1–3 sentence summary naming products, regions and CVEs.
  This is the TL;DR bullet body, the RSS description, and the notification
  text — a reader who sees ONLY this must know what is affected and why it
  matters.
discovered_at: "2026-07-03T04:21:09Z"   # UTC moment the finding was FIRST published — never changes
updated_at: null               # UTC moment of the latest changelog record (== updates[-1].at); null until
                               # the first update. max(discovered_at, updated_at) is the entry's activity
                               # moment — the live brief's sort key
event_date: "2026-07-02"                # date of the underlying event / primary publication
run_id: 2026-07-03T0412Z-intel          # the ORIGINATING fire — never changes; updating runs appear in updates[]
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
techniques: []                 # MITRE ATT&CK ids the sources support (T####[.###]) — the
                               # CANONICAL mapping surface (active ids per the pinned
                               # attack/enterprise-attack.json); every id must name a behavior
                               # the body describes in prose (inline T-ids only where
                               # essential); [] when the entry maps none
affected_products: []          # official product names ("Vendor Product" strings — what an
                               # alert or asset inventory would name); [] when not
                               # product-specific
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
closed_sources: []             # [{title, provider, date, ref}] — intel/ drop citations, never URLs (no TLP gate)
evidence:                      # verbatim quotes binding claims to fetched sources
  - quote: "An authenticated remote command injection vulnerability (CWE-78) in Coolify…"
    publisher: "coollabsio GHSA"
verification: multi-source     # multi-source | single-source | single-source-national-cert |
                               # single-source-victim | contradicted
sourcing_note: null            # human clause, e.g. "victim-own SEC 8-K disclosure carve-out"
confidence: high               # high | medium | low
references: []                 # entry ids this entry builds on (a distinct finding that shares a CVE
                               # with an older entry MUST list it here — the explicit, gate-checked
                               # statement that it is not a duplicate; see § Dedup)
weekly_section: null           # LEGACY (pre-v4 strategic entries only) — a v4+ entry never sets it
deep_dive: false               # true ⇒ this entry IS the deep-dive treatment
deep_dive_category: null       # taxonomy-free rotation slug when deep_dive: true (see prompt)
org_triage: null               # or {category: P1, rationale: "…"} on triage-kind entries when a scheme is defined
classification: null           # null here (vulnerability is a triage kind → uses org_triage). EVERY
                               # non-triage entry instead carries the NATO Admiralty code, e.g.:
                               #   classification: {reliability: B, credibility: 2}
                               # reliability A–F (of the sourcing) + credibility 1–6 (of the item),
                               # assessed independently — config/org-profile.yaml `classification:`.
watchlist_hit: false           # true only when inclusion was driven by an org-profile watchlist match
actions: []                    # imperative, entry-specific defender actions (strings) — feed § Action Items
updates: []                    # the changelog — append-only, oldest first (§ Entry lifecycle):
# updates:
#   - at: "2026-07-05T04:40:12Z"          # UTC; > discovered_at and > the previous record's at
#     run_id: 2026-07-05T0410Z-intel      # the fire that made the change
#     type: update                        # update | correction | improvement
#     summary: >                          # 1–3 self-contained sentences: what changed and why —
#       CISA added CVE-2026-34038 to KEV on 2026-07-04; status moved to exploited.   # the timeline row
#     fields: [cves, priority, summary]   # optional: frontmatter fields changed in place ("body" for
#                                         # an edit to the main analysis)
#     merged_from: null                   # migration provenance only (a v3 update_of entry folded here)
migrated_from: null            # v2 provenance (briefs/YYYY-MM-DD.md) — migration tool only
---

Body: the full analysis in Markdown, followed — when the entry has been
updated — by one `## <Type> — <at>` section per `updates[]` record, in the
same order (§ Entry lifecycle). Inline source links at the point of
claim (`([Publisher, YYYY-MM-DD](URL))`), defender takeaway, detection and
hardening concepts — ATT&CK mappings live in `techniques[]`, and an inline
T-id appears in prose only where essential (deep-dive kill chains, a
mapping that is itself the finding) — the same technical register and
depth as a v2 brief item, described as
observable behavior (telemetry classes in vendor-neutral terms; platform
artifacts as examples) so a human analyst or an automated triage agent
can match an alert against it. Threat/incident/research bodies close with
`**Defender takeaway:**` and, where the cited mechanism supports a
benign-lookalike discriminator, a `**Triage:**` line. Deep-dive entries
carry the complete deep-dive narrative (Background paragraph, kill chain,
hunt concepts, mitigation). No IOCs, no rule code, no vanity metrics,
English only.
```

### Field semantics and hard rules

- **`headline`** — bold-lead TL;DR headline, ≤ 120 chars, no trailing period.
- **`summary`** — the load-bearing standalone digest. Never empty.
- **`discovered_at`** — the moment *this pipeline* first published the
  finding, set once, never backdated, never changed by an update. The folder
  date MUST equal its UTC date.
- **`updated_at` / `updates[]`** — the entry's changelog (§ Entry
  lifecycle). `updates[]` is append-only, oldest first; `updated_at` MUST
  equal the last record's `at` (null while the list is empty). The entry's
  **activity moment** is `max(discovered_at, updated_at)`
  (`content_model.entry_activity_ts`): it orders the live brief, the
  briefbook and the feeds, so an update floats the entry back to the top.
- **`event_date`** — recency anchor of the underlying event (primary-source
  publication date). Drives staleness checks; `discovered_at` drives windows.
- **`entities`** — every value MUST resolve to a key in
  `entities/registry.yaml`. New entities are added to the registry in the
  same commit. Never invent a second key for a known entity — check aliases.
- **`cves[]`** — one record per CVE, always with `type`/`vector`/`auth`/
  `status` from the taxonomy. Multi-CVE items carry one record per CVE
  (the v2 "per-CVE breakdown" is now structural). Axis semantics: `vector`
  encodes the victim-interaction requirement (`zero-click` = attacker-
  initiated, no victim interaction — independent of auth state), `auth`
  encodes the authentication precondition; an authenticated, no-interaction
  bug is correctly `vector: zero-click` + `auth: post-auth`.
- **`techniques[]`** — the entry's MITRE ATT&CK technique ids, validated
  against `T####`/`T####.###` (format — FAIL) and against the pinned
  ATT&CK dataset `attack/enterprise-attack.json` (existence + lifecycle —
  WARN; see § The ATT&CK layer). This is the **canonical mapping
  surface**: the machine retrieval layer for alert-triage consumers
  (given an alert mapped to a technique, the matching entries are a field
  lookup), and the sole input to the derived entity/CVE TTP profiles, the
  `/attack/` matrix and the Navigator-layer exports — a technique missing
  here is invisible to all of them. Use active ids only (revoked ids
  resolve forward via `revoked_by`, but new entries reference survivors).
  Every id must correspond to a behavior the body describes **in plain
  prose**; inline T-ids in the body appear only where essential, and a
  bare ID list in prose is a defect. An id no cited source supports is a
  hallucination. Entries that predate this field (the migrated/early-v3
  tail) carry their mappings as in-prose T-ids only; consumers derive
  their effective set via `content_model.entry_technique_ids` (frontmatter
  ∪ dataset-known prose ids) — the tail is not bulk-rewritten, so that
  derivation path stays.
- **`affected_products[]`** — official vendor product names as plain
  strings (`"Citrix NetScaler ADC"`, `"Adobe ColdFusion"`), the names an
  alert, asset inventory, or CMDB would carry. Generalizes the CVE-only
  `affected`/`fixed` version fields to campaign/threat entries; empty when
  the entry is not product-specific.
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
- **`update_of`** — RETIRED in v4.0. The gate FAILs any non-null value:
  developments and corrections are `updates[]` records on the existing
  entry, never a second entry. (Long-running campaigns still get ≤ 1
  consolidated update record per week unless something critical changes.)
- **`references[]`** — entry ids this entry builds on. It is also the
  explicit dedup statement: a genuinely distinct finding whose `cves[]`
  intersect an existing entry's MUST list that entry here, or the gate
  FAILs the new entry as a duplicate (§ Dedup across runs).
- **`actions[]`** — only actions derived from this entry's own content,
  held to the do-now bar (`prompts/cti-run.md` Phase 4 § `actions[]`, v3.19):
  concrete, self-contained, start-now tasks — never generic advice, never a
  restatement of the body's detection/hardening guidance. **Empty is the
  normal case for many entries.** The rendered brief's § Action Items is the
  union over the window, so every marginal action dilutes it for the reader.
- **`migrated_from`** — non-null marks a v2-brief import. Migrated entries
  may carry placeholder `evidence[]`, empty `entities`/`actions`/
  `techniques`, and news-register bodies; **machine consumers (triage
  agents, exporters) should treat `migrated_from != null` as a
  lower-fidelity tier** and prefer native entries when both cover a topic.
  An audit may lift a migrated entry through an `improvement` record like
  any other entry; the provenance flag itself never changes.
- **`org_triage` / `classification`** — every entry carries exactly one
  classification scheme, selected by kind. Triage kinds
  (`classification.triage_kinds` in `config/org-profile.yaml`, default
  `vulnerability`) carry `org_triage: {category, rationale}` and
  `classification: null`; every other kind carries the NATO Admiralty
  `classification: {reliability, credibility}` (letter A–F for the sourcing,
  number 1–6 for the item, assessed independently) and `org_triage: null`.
  Both schemes and the kind split are config-driven; the gate FAILs an
  out-of-vocabulary code and the verifier flags mis-placement (F16 / F17).
  There is no TLP gate anywhere — everything under `intel/` is processable.
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

| `kind` | brief section (`content_model.KIND_DAILY_SECTION`) | writable by v4+ runs |
|---|---|---|
| `threat` | § Active Threats, Trending Actors, Notable Incidents & Disclosures | yes |
| `incident` | § Active Threats (incident / disclosure flavour) | yes |
| `vulnerability` | § Trending Vulnerabilities | yes |
| `research` | § Research, Reports & Policy | yes |
| `annual-report` | § Research, Reports & Policy (one-time treatment per PD-9) | yes |
| `policy` | § Research, Reports & Policy — a regulatory action or deadline with a transferable obligation for the constituency (PD-11 c) | yes |
| `synthesis` | — (legacy weekly kind; archived entries only) | **no** |
| `outlook` | — (legacy weekly kind; archived entries only) | **no** |

`content_model.ACTIVE_KINDS` is the writable set; `check_run.py` FAILs a
v4+ entry with a legacy kind, `horizon: strategic` or a `weekly_section`.
Orthogonal flags relocate an entry at render time: `deep_dive: true` ⇒
§ Deep Dive (and not its kind section); an entry with a changelog record
dated inside the rendered day/window additionally appears in § Updates to
Prior Coverage (rendered from that record — see § Rendering). The legacy
`horizon: strategic` entries are archived history: reachable by permalink,
entity page, CVE page, tag/region index and search, rendered in no brief.

## Entry lifecycle — one living entry per finding

A finding is published once and then **maintained in place**. The same
file carries the original analysis, every later development, every
correction and every improvement, each as a dated, attributed changelog
record. This replaces the v3 "immutable entry + `update_of` second entry"
model (retired 2026-08-27, operator decision): a reader — human or triage
agent — opens one URL and sees the current state of the finding *and* how
it got there, and an update surfaces on the live brief exactly like a new
finding would.

### The changelog record

```yaml
updates:
  - at: "2026-07-05T04:40:12Z"      # UTC; strictly later than discovered_at and than the previous record
    run_id: 2026-07-05T0410Z-intel  # the fire that made the change — resolves to a run record
    type: update                    # update | correction | improvement (vocabulary below)
    summary: >                      # 1–3 self-contained sentences: what changed and why. This is the
      …                             # text the live timeline row, the day page's § Updates and the feed
                                    # item show — a reader who sees ONLY this knows what moved
    fields: [cves, priority]        # optional: the frontmatter fields this record changed in place;
                                    # "body" when the main analysis itself was edited (corrections)
    merged_from: null               # optional, migration provenance only: the v3 update_of entry id
                                    # that was folded into this record (the build redirects its old URL)
updated_at: "2026-07-05T04:40:12Z"  # == updates[-1].at
```

Every record pairs **1:1, in order, by `at`** with a body section headed
exactly `## <Type> — <at>` (`Update`, `Correction` or `Improvement`, an em
dash, the record's `at` verbatim — `content_model.update_section_heading`).
The section carries the **delta only**, inline-cited like any other prose,
never a recap of the entry. The main analysis is everything above the first
such heading and must remain a complete, readable entry on its own.

| `type` | when | what changes |
|---|---|---|
| `update` | a **material new development** on the finding — new actor, victim, CVE in the chain, patch shipped, exploitation-status change (incl. a KEV listing of a not-yet-exploited CVE), confirmed law-enforcement action | the section states the development; the frontmatter moves to the **new current state**: `cves[].status`/`fixed`, `affected_products`, `entities`, `techniques`, `tags`, `actions[]` (replace, never accumulate — the list is the *current* do-now set), and `priority`/`immediate_action` when the bar changes in either direction; `headline`/`summary` are revised only when a reader who sees only the summary must now know something different (e.g. now exploited) |
| `correction` | the entry **stated something wrong** — a claim its source does not support, an inverted mechanism, a wrong version/date/score/id, a mis-attributed quote | the wrong statement is **fixed where it stands** (frontmatter and/or body — `fields` names them, `"body"` included) so the entry never asserts something known to be false, AND the section records what was wrong, what is right, and the ground-truth source. The reader can see both the corrected text and the correction note; git carries the exact diff |
| `improvement` | precision or depth added **without reversing a claim** — a second independent source, a technique mapped that the body already described, a `**Triage:**` line the mechanism supports, a fixed version stated to vendor precision, a Background paragraph | the section states what was added and on what basis; touched frontmatter listed in `fields` |

Rules, all enforced by `tools/check_run.py` (`entry-updates`, `silent-edit`) unless noted:

1. **Provenance never moves.** The entry id/path, `discovered_at`, `run_id`
   and `migrated_from` are never edited. Folder date == `discovered_at` date
   forever, whatever `updated_at` says.
2. **No silent edits.** Every change to a published entry's file — any field,
   any prose — ships with a changelog record whose `run_id` is the editing
   fire. At the gate, an entry modified in the working tree relative to
   `HEAD` that carries neither `run_id == <this run>` (new) nor an
   `updates[]` record with `run_id == <this run>` FAILs (`silent-edit`).
3. **One record per fire per entry.** A fire that changes an entry in
   several ways writes one record covering all of them; two fires write two
   records. Records are append-only and strictly increasing in `at`; a
   record is never edited or removed by a later fire (a wrong update is
   corrected by a further `correction` record).
4. **Sources travel with the change.** A section's inline citations are
   `sources[]` records like any other claim's — new sources are appended to
   `sources[]` (the first record stays the original primary), new verbatim
   quotes to `evidence[]`. The verifier reads the whole entry and checks the
   new section and every changed field against them.
5. **The main analysis stays current.** An `update` that supersedes a
   statement in the main analysis (a "no patch" claim after the patch
   shipped, "PoC only" after exploitation) edits that statement too — a
   minimal, `fields: [body]`-declared edit — so the entry never contradicts
   itself; the section explains the change. Developments are never
   *absorbed* into the analysis silently: the section is where the reader
   learns what happened when.
6. **Who may update.** Any intel run (its own dedup decision, PD-8) and the
   quality audit (soundness corrections, completeness improvements). The
   audit's former "immutability-exception ledger" is retired — the
   changelog *is* the ledger, and it lives with the entry.
7. **Cadence discipline.** Long-running campaigns receive ≤ 1 consolidated
   `update` record per week unless something critical changes; bookkeeping
   that changes nothing a reader would act on (a `cisa-kev` flag on a CVE
   the entry already calls exploited) is not a record.

### How the pipeline reacts to an update

- **Live brief** (`/live/`, `data/briefbook.json`, brief.js): the entry is
  in the window iff its **activity moment** is; it renders in the run group
  of the fire that made the latest record, flagged `UPD` with the record's
  type and `summary` shown under the headline; the pulse panel's "updates to
  prior coverage" counts it. An entry appears once, at its latest activity.
- **Day pages** (`/daily/<date>/`): § Updates to Prior Coverage lists every
  entry with a record dated that UTC day, rendered from the record (type,
  time, summary, the section body, link to the entry); the entry's kind
  section still shows it only on its `discovered_at` day.
- **Entry permalink**: "First published <discovered_at> · Updated
  <updated_at>" in the meta line; each `## <Type> — <at>` section renders
  as a timestamped, type-badged block; a *Revision history* panel lists the
  records (type · time · run link · summary · changed fields).
- **Feeds**: `feed-items.xml` and the sector feeds emit one item per entry
  (`pubDate` = `discovered_at`) **and one item per changelog record**
  (`guid` = `<entry url>#update-<at>`, `pubDate` = `at`, title prefixed by
  the type, description = the record's `summary`, content = the section).
- **`data/alerts.json`**: an entry enters the 7-day window by activity
  moment and carries `updated_at` + a compact `updates[]` (`at`, `type`,
  `summary`), so a hook can alert on a critical/high entry's update.
- **Redirects**: for every record with `merged_from`, the build emits a
  meta-refresh stub at the folded entry's old permalink pointing at the
  living entry (noindex, excluded from the sitemap).
- **Run records**: `entries_updated` counts the entries a fire appended a
  record to and `updated_entry_ids[]` names them (§ Run records); the run's
  detail page and the ops dashboard list them beside its new entries.

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
    relations:                 # optional: typed, directed, evidence-bound
                               # graph edges (§ Relationships below)
      - to: "tool:shinysp1d3r-ransomware"
        type: uses             # controlled vocabulary — direction matters
        source: "2026-06-14/some-entry-slug"   # entry that establishes the edge
        note: "one-clause basis (optional)"
    # merged_into: <key>       # optional: tombstone — this record was merged
                               # into the named canonical entity (see below)
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

**Naming convention (uniform across the registry):** `name` is the concise
canonical entity name only — the name of the actor/campaign/tool itself,
never the reporting vendor, never a headline sentence, never a list of
alternates. Every other public name goes in `aliases` (which feeds both
dedup matching and the site's phrase-based entry↔entity attachment).
`summary` is the 1–3-sentence English definition carrying the
who/what/so-what plus the attributing source and date.

**Merging duplicates — `merged_into` tombstones.** Because keys are
permanent and hundreds of published entries reference them by key, a
duplicate entity is never deleted while any entry references it. Instead the losing record becomes a
tombstone: it keeps its key and gains `merged_into: <canonical-key>`.
Semantics enforced by `content_model.validate_registry` (surfaced as FAILs
by `check_run.py`): the target must exist and must not itself be a
tombstone (no chains); tombstones are exempt from the name/alias collision
check (their labels legitimately move to the canonical record). Consumers
resolve through tombstones via `content_model.resolve_entity_key`: the site
attaches a tombstone's entries to the canonical entity's page (the
tombstone keeps a stub permalink pointing forward), and cross-run dedup
treats old and canonical keys as the same entity. New entries MUST
reference the canonical key, never a tombstone. When tombstoning, move the
losing record's `relations[]` onto the canonical record (dropping edges the
canonical record already carries, and retargeting registry-wide edges that
pointed at the loser); a tombstone carries no relations, and no relation
targets one. An entity referenced by zero entries (orphan) that turns out
to be a duplicate may simply be deleted — fold its names into the
canonical record's `aliases` and migrate its edges first.

## Relationships — the threat graph

Entity relationships are **typed, directed, evidence-bound edges** carried
in each registry record's optional `relations[]` list. They replaced the
untyped `related: []` key list (removed without backward compatibility);
`validate_registry` FAILs a record that still carries `related`. The graph
has exactly two edge classes, and every edge's derivation is explicit:

1. **Curated edges** (`relations[]` in the registry) — a connection a
   cited source *states*: "this actor operates this campaign", "this
   campaign deploys this malware". Each edge names its relationship type
   from the controlled vocabulary below and cites the entry whose sourced
   reporting establishes it.
2. **Derived edges** (computed by `site/build.py`, never stored) — a
   connection the entry store *implies*: two entities referenced by the
   same entry (co-occurrence, weight = shared-entry count), an entity and
   a CVE carried by the same entry, an entity and an ATT&CK technique via
   the derived TTP profiles (§ The ATT&CK layer). Derived edges are
   recomputed on every build and always carry their supporting entry ids —
   they can never drift from the store. **Evidence-quality gate**
   (`build.derived_edge_qualified`): only focused operational reporting
   creates a derived edge — `horizon: strategic` entries (weekly
   synthesis, outlooks, policy roundups) and `annual-report` treatments
   are excluded, because they mention many unrelated entities by
   construction: two names sharing a weekly recap or a quarterly
   ransomware ranking is summarization, not a connection. Curated edges
   are unaffected (each carries its own establishing entry).

Curated edges assert *what happened*; derived edges surface *what the
store connects*. Renderers keep the two visually distinct (curated edges
carry their type label; derived edges are labelled by their derivation),
and an analyst reading any edge can always answer "why does this edge
exist?" — either "entry X's cited source states it" or "these N entries
reference both".

### Curated edge shape

```yaml
relations:
  - to: "actor:shinyhunters"      # target registry key — MUST exist, MUST be
                                  # canonical (never a tombstone)
    type: attributed-to           # controlled vocabulary below
    source: "2026-06-14/<slug>"   # entry id whose cited reporting establishes
                                  # the connection — MUST resolve; the entry's
                                  # date doubles as the edge's first-seen date
    note: "GTIG attributes the wave to ShinyHunters"   # optional one-clause basis
```

### Relationship vocabulary (controlled — `content_model.RELATION_TYPES`)

Directed types read **subject → object**: the edge lives on the *subject's*
record and `to` names the object. Renderers show every edge from both ends
(the object's page shows the inverse reading). Symmetric types are stored
**once**, on either endpoint — declaring the mirror edge too is a FAIL
(duplicate), and renderers/exports surface it on both endpoints anyway.

| `type` | subject types → object types | reading (inverse reading) |
|---|---|---|
| `attributed-to` | campaign, incident, malware, tool → actor | subject is attributed to actor (actor's attributed activity) |
| `uses` | actor, campaign, incident → malware, tool | subject deploys/operates the malware or tool (used by) |
| `exploits` | actor, campaign, incident → trend | subject exploits the named vulnerability/technique wave (exploited by). CVE-level exploitation is a **derived** edge — the entry that carries both the entity and the `cves[]` record is the evidence; CVEs are not registry entities. |
| `part-of` | incident, campaign → campaign, trend | subject belongs to the larger campaign/wave (includes) |
| `variant-of` | malware, tool → malware, tool | subject is a variant/fork/derivative of the object (has variant) |
| `successor-of` | actor→actor, campaign→campaign, malware→malware, tool→tool, policy→policy | subject continues/rebrands/replaces the object (succeeded by) |
| `collaborates-with` | actor ↔ actor (symmetric) | the two actors cooperate (shared operations, hand-offs) |
| `overlaps-with` | actor, campaign, malware, tool ↔ same set (symmetric) | cited reporting states technical/infrastructure/TTP overlap **short of** attribution or identity |
| `documented-in` | any non-report type → report | the report profiles the subject (documents) |
| `related-to` | any ↔ any (symmetric) | fallback — a source-stated connection none of the typed relations fits; prefer a typed relation whenever one applies |

Semantics guardrails: `attributed-to` is for *responsibility claims* (keep
the claim attributed in the `note`/entry, per the sourcing rules);
`overlaps-with` is the honest middle ground when researchers report shared
infrastructure or tooling without asserting identity — never upgrade an
overlap claim to `attributed-to` or `successor-of` beyond what the cited
source states. A suspected *same entity* is not a relation at all — that is
an alias or a `merged_into` tombstone.

### Hard rules (enforced by `content_model.validate_registry`, surfaced as FAILs by `check_run.py`)

- `type` must be in the vocabulary; subject/object entity types must
  satisfy the type's endpoint constraints.
- `to` must exist, must be canonical (not a tombstone), and must not be
  the record itself. Tombstones must not carry `relations[]` — move edges
  to the canonical record when merging.
- `source` is REQUIRED and must be a valid entry id (`YYYY-MM-DD/<slug>`)
  that resolves to an existing entry — this is what makes every curated
  edge evidence-bound and dates it. `check_run.py` additionally WARNs when
  the source entry references neither endpoint in its `entities[]` (the
  edge is still legal — the establishing entry may predate one endpoint's
  registration — but the mismatch is worth an operator's glance).
- No duplicate edges: the same `(subject, type, object)` — for symmetric
  types the same unordered pair — appears once in the whole registry. New
  corroboration of an existing edge does not add a second edge; material
  evolution of the *relationship* (e.g. overlap upgraded to attribution by
  new reporting) **replaces** the edge's `type`/`source`/`note` in place —
  relations are registry state, not immutable entries.
- Relations are otherwise append-only in spirit: edges are added when a
  cited source establishes a connection, in the same commit as the entry
  that carries the evidence.

### The graph rendering — `/graph/` + `data/graph.json`

The full graph ships as `data/graph.json` (all canonical entities, covered
CVEs, mapped ATT&CK techniques, curated + derived edges) and renders at
`/graph/` as an interactive, self-contained (strict-CSP, no external
libraries) canvas exploration surface. Exploration is **seeded**: the
analyst names one or more starting nodes (search, an entity-page deep link
`?focus=<id>`, or the most-connected directory), and the view renders
exactly the subgraph the analyst has grown from those seeds — the direct
neighbourhood by default (`?hops=` widens to 2 hops or the full connected
component), extended node by node via expand — and nothing else: nodes
outside the grown view are not drawn at all, not even dimmed; with no
seed, nothing is drawn. Within the view:
type-filtering (entities / CVEs / techniques as a toggleable layer),
curated/derived edge toggles (both also bound reachability), hover
neighborhoods, a node detail panel (summary, typed relations, supporting
entries — including connections outside the current view), re-seeding from
any node, and shortest-path tracing between two nodes — "how is this actor
connected to this CVE?" answered visually, every hop backed by an edge
whose provenance is one click away. Entity pages render the same edges in
prose form: typed curated relations grouped by relationship reading, each
with its source entry link, followed by the derived co-occurrence list.

## The ATT&CK layer — pinned dataset + derived TTP mappings

CVEs, actors, campaigns and every other entity get their MITRE ATT&CK
technique profile **by derivation, never by assertion**: an entity maps a
technique exactly when a published entry ties them together. The layer has
three parts:

1. **The pinned dataset — `attack/enterprise-attack.json`** (contract:
   [attack/README.md](../attack/README.md); writer: `tools/attack_data.py`).
   A compact, committed extraction of one specific ATT&CK Enterprise
   release: technique id → name, tactics, first-paragraph definition,
   sub-technique parentage, platforms, and lifecycle flags. Pinning matters
   because releases drift — v19 renamed Defense Evasion into Stealth +
   Defense Impairment (new TA0112) and every release revokes ids.
   Revoked/deprecated techniques are **kept, flagged**, with `revoked_by`
   forwarding — the ATT&CK analogue of the registry's `merged_into`
   tombstones, and for the same reason: the store is not rewritten when the
   pin moves, so an id cited before MITRE revoked it must keep resolving
   (`content_model.resolve_technique_id`). Updating the pin is an explicit,
   diff-reviewed act: `tools/attack_data.py --check` (drift detection;
   quality-audit duty) / `--update` (rewrite + change summary for the commit
   body) / `--selftest` (offline invariants; also enforced by
   `check_run.py`).
2. **Per-entry effective techniques —
   `content_model.entry_technique_ids`.** The union of the entry's
   `techniques[]` frontmatter (canonical, v3.17+) and dataset-known T-ids
   in its body prose (the only mapping surface of the pre-v3.17 tail, which
   is not bulk-rewritten), revoked ids resolved forward. Exposed per entry in
   `data/briefbook.json` and `data/alerts.json` as `techniques[]`.
3. **Derived aggregations (`site/build.py`).** Per entity AND per CVE:
   `{technique id: [supporting entry ids]}` — evidence-bound, rendered as
   the entity page's ATT&CK section (grouped by tactic in official matrix
   order, definitions from the pin, entry links) and exported as a
   per-entity **ATT&CK Navigator layer** (`entities/<key>/attack-layer.json`,
   layer format 4.5, score = supporting-entry count). The `/attack/` page
   renders the full matrix heat-shaded by store-wide coverage, carries the
   per-technique definitions-and-evidence directory, and offers the
   client-side multi-entity overlap view (union / overlap≥2 /
   common-to-all) over `data/attack.json` — Navigator-layer semantics
   without leaving the site, plus layer export of any comparison.

## Run records — `runs/YYYY-MM-DD/<run-id>.md`

One file per fire, written in the run's final phase. Frontmatter is the
complete machine-readable telemetry record (the v2 `run_log.json` entry,
relocated); the body is the human-readable **verification & coverage
notes** — the v2 brief § 7, relocated to a dedicated, per-run home.

Run records are immutable once their fire completes (unlike entries, which
are living records — a run record is telemetry about one fire and has no
"current state" to maintain), with exactly two same-fire in-place updates
permitted: the same-minute retry (idempotent run_id) and the **Phase 7
publish-status amendment** — after the publish poll, the fire updates
`publish_status`/`publish_checked_at`/`publish_note` in place, commits
`run: <run-id> publish-status`, and re-pushes the feature branch
(fire-and-forget; auto-merge promotes it). No other field is ever edited
after commit, and no later fire edits an earlier fire's record.

An optional `stood_down: <reason>` field (non-empty string) marks a fire that
legitimately aborted **before Phase 1** spawned any research/verification
workers — e.g. the quality audit's duplicate-audit guard (gap since the last
audit < 72 h). Such a fire still writes a run record (run-record-per-fire is
never waived) but carries an empty `sub_agents` block, since no sub-agents
ran; the mechanical gate exempts the `sub_agents` requirement only when
`stood_down` is set. The mandatory verification iteration still runs (scoped
to the run record). Normal fires omit `stood_down`.

```yaml
---
schema: 1
run_id: 2026-07-03T0412Z-intel
kind: intel                    # intel | audit (matches the run-id suffix; `weekly` = legacy records)
date: "2026-07-03"
started: "2026-07-03T04:12:03Z"
completed: "2026-07-03T04:31:40Z"
duration_seconds: 1177
model: "…"                     # main-agent friendly name (self-ID: harness prompt line; env vars as marked fallback)
model_id: "…"
prompt_version: "v3.1"
window_hours: 24               # gap-derived recency window this run covered (24 h floor)
gap_hours: 7                   # hours since the previous run record
entries_published: 3           # NEW entry files this run (run_id == this run)
entries_updated: 1             # existing entries this run appended an updates[] record to
updated_entry_ids:             # v4.0: their ids — len == entries_updated; [] when none
  - 2026-07-01/some-earlier-entry
deep_dive: null                # entry id of a deep-dive entry published this run, or null
sub_agents:                    # S1–S4 (+S5); audit fires: truth-pass and re-sweep workers
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
publish_status: pending        # pending | ok | main-only — machine-auditable publish outcome.
                               # Written `pending` at the Phase 6 commit; the SAME fire amends
                               # it in place after Phase 7's poll (ok = run record on main AND
                               # site rebuilt, or site polling disabled; main-only = record on
                               # main but the site rebuild never confirmed) and pushes the
                               # amendment. A record still `pending` on main means the fire died
                               # before Phase 7 or the amendment push failed — an operator signal
                               # either way. Absent on records that predate v3.14.
publish_checked_at: null       # UTC timestamp of the Phase 7 poll that set publish_status
publish_note: null             # free-text reason detail (e.g. "site polling disabled",
                               # "auto-merge pending at deadline")
verification_iterations: 2
verification_residual_count: 0 # never 0 when the final iteration was NEEDS_FIXES
verification:
  confirmation_waived: null    # optional (v3.23+): non-null string ONLY when the run published
                               # on a CLEAN that no second model confirmed (single CLEAN at the
                               # iteration cap, watchdog-overrun single iteration, other-model
                               # spawn blocked) — the reason, verbatim. Normal confirmed-CLEAN
                               # publishes omit it. `check_run.py` FAILs an unconfirmed final
                               # CLEAN on v3.23+ records unless this (or the cap) explains it.
  iterations:                  # v3.23+: a CLEAN publish requires the final TWO iterations both
                               # CLEAN, on different models (the opus/sonnet rotation supplies
                               # the model diversity) — so a CLEAN publish has ≥2 iterations
    - n: 1
      model: "…"
      model_id: "…"
      subagent_type: cti-verification   # which rotation definition was spawned
      started_at: "…"
      ended_at: "…"
      duration_seconds: 240
      verdict: CLEAN           # CLEAN | NEEDS_FIXES
      truth: 0                 # F1–F4 + F13–F15
      editorial: 0             # F5–F10 + F12 + F16
      advisory: 0              # F11
      findings: []             # rich per-finding records, v2 shape
    - n: 2                     # the confirmation pass — the other model, also CLEAN
      model: "…"
      model_id: "…"
      subagent_type: cti-verification-alt
      started_at: "…"
      ended_at: "…"
      duration_seconds: 210
      verdict: CLEAN
      truth: 0
      editorial: 0
      advisory: 0
      findings: []
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
   full `prior_coverage.json` — every in-window brief loaded into context
   (each record also carries `updated_at`, its record count and the last
   record's summary) — and never writes a new entry for a candidate whose
   CVE ids or entity keys match an in-window entry from **any** run in those
   14 days: the candidate is either an `updates[]` record on that entry
   (material delta) or nothing.
3. **Metadata check (store-wide, older than 14 days).** Coverage older than
   the 14-day in-context window is caught by the store-wide CVE index
   (`state/cves_seen.json`, surfaced as `cves.ids` in the state summary),
   not an in-context read — an old CVE re-surfacing is still recognised and
   handled the same way (a record on the existing entry).
4. **Fetch-time dedup.** Research sub-agents read `prior_coverage.json`
   before fetching and skip already-covered items unless they hold a
   material delta (returned as `novelty: update-of:<entry-id>`).
5. **Mechanical gate.** `tools/check_run.py` FAILs a new entry whose CVE set
   intersects **any** existing entry (store-wide, any age) unless the new
   entry lists that entry in `references[]` — the explicit, reviewable
   statement that this is a distinct finding building on the older one, not
   a duplicate — and WARNs on entity-key overlap inside 14 days. Entries
   updated by the run are exempt (the record IS the dedup decision).

## Rendering — the brief is a query

- **`/live/`** — the live rolling brief, rendered as a run-grouped,
  reverse-chronological **timeline** keyed on each entry's **activity
  moment** (`max(discovered_at, updated_at)`): a new finding appears under
  the run that published it, an updated finding under the run that updated
  it (flag `UPD`, the record's type + summary shown), each entry once at
  its latest activity. Reader picks *last N hours* (6 / 12 / 24 / 48 / 72)
  via the window selector or loads older findings; default **24 h**.
  **Every run in the window appears, including quiet (0-finding) ones.**
  The default window ships server-rendered (full content, no-JS readable);
  JS re-renders the timeline client-side from `data/briefbook.json` (last
  ~35 days of entries by activity + run records). Each timeline row carries
  priority / CVE / exploited / updated badges, a linked headline,
  provenance, and a clickable source list.
- **`/daily/YYYY-MM-DD/`** — one settled page per **completed** UTC day
  (the still-rolling day lives only in `/live/`), in the classic editorial
  section order: TL;DR → Active Threats → Trending Vulnerabilities →
  Research, Reports & Policy → Updates to Prior Coverage (every entry with a
  changelog record dated that day, rendered from the record) → Deep Dive →
  Action Items, with a collapsible Verification block. `/daily/` is the
  newest-first archive; daily RSS keys on these.
- **`/entries/YYYY-MM-DD/<slug>/`** — per-entry permalink: current state
  first, the changelog sections as timestamped blocks, a Revision history
  panel; "First published … · Updated …" meta. Folded v3 update entries'
  old URLs redirect here (`merged_from`).
- **Feeds** — `feed-items.xml` (one item per entry, `<pubDate>` =
  `discovered_at` — true discovery latency, not commit time — **plus one
  item per changelog record**, `<pubDate>` = its `at`) + the eight sector
  slices + the daily digest feed. There is no weekly feed.
- **`data/alerts.json`** — last 7 days (by activity moment) of
  `critical`/`high` entries with headline, summary, immediate_action,
  entities, CVEs, techniques, `updated_at` and compact `updates[]`: the
  notification-hook surface.
- **`/attack/` + `data/attack.json` + `entities/<key>/attack-layer.json`**
  — the ATT&CK coverage matrix, its client-side overlap dataset, and the
  per-entity Navigator layer exports (§ The ATT&CK layer).
- **`/graph/` + `data/graph.json`** — the interactive threat graph over
  all canonical entities, covered CVEs and (toggleable) ATT&CK techniques:
  curated typed edges + derived co-occurrence/CVE/technique edges, each
  with its provenance (§ Relationships).
- **Entity pages, trends, ops, search** — all derived from entries +
  registry + runs, same URLs as v2. Entity/CVE pages carry the derived
  ATT&CK section; covered techniques are searchable.

## The mechanical gate — `tools/check_run.py`

Replaces `tools/check_brief.py`. Read-only, stdlib-only, exit 0 required
before the verifier spawns and before every commit. Validates: frontmatter
parses and every field is schema- and taxonomy-valid; folder-date/
discovered_at/slug consistency; source-URL block-list + liveness (honouring
`work/<run-id>/url-liveness.tsv`); evidence shape/presence; priority ⇔
immediate_action consistency; entity refs resolve; registry integrity
(incl. typed-relation vocabulary, endpoint constraints, canonical targets
and source-entry resolution — § Relationships);
the entry lifecycle (`updates[]` shape, `updated_at` mirror, strictly
increasing `at`, 1:1 body-section pairing, record `run_id` resolution, no
silent edit — an entry modified without a record for the modifying run
FAILs; `update_of` retired — any non-null value FAILs; v4+ entries carry no
legacy kind / horizon / weekly_section); `references[]` resolution;
cross-run dedup (store-wide CVE overlap FAILs unless declared in
`references[]`); run counters vs disk (`entries_published`,
`entries_updated` + `updated_entry_ids`, `deep_dive`); rolling-24 h
composition (reported, not gated on a count); CVE sync with
`cves_seen.json`; IOC scan; run-record completeness (incl. verification
counters and prompt-version cross-check against `prompts/CHANGELOG.md`);
`sources/sources.json` shape (incl. Admiralty A–F `reliability_codes`);
closed-source citation traceability to `intel/` (no TLP gate); org-triage and
Admiralty-classification vocabulary/placement; the ATT&CK layer (pinned
dataset present + invariant-clean — FAIL; `techniques[]` ids unknown /
revoked / deprecated in the pin, or prose-mapped ids missing from the
frontmatter — WARN); and the site smoke tests (`site/test_build.py`).


