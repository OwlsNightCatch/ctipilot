# ctipilot.ch — Continuous CTI Intelligence Pipeline

> **AI-generated content notice.** Every intelligence entry in this repository is produced autonomously by an LLM running as a [Claude Code routine](https://docs.claude.com/en/docs/claude-code/routines) on Anthropic-managed cloud infrastructure. The exact models vary based on the routine's runtime configuration; every producing run identifies its main-agent, research and verifier models in its run record under `runs/`. The agent fetches public sources, applies the verification rules in [`prompts/verification.md`](prompts/verification.md), and writes the entry files you see in `entries/`. Every claim in an entry is linked inline to its source. No human reviews entries before publication. Verify any operationally critical claim against the linked primary source before acting on it. The entries are not professional advice and may contain errors.

A **continuous Cyber Threat Intelligence pipeline** covering cyber threats targeting Switzerland and Europe with a public-sector focus (national/cantonal/federal administration, regulators, critical infrastructure, healthcare, education, public-sector technology suppliers). Audience: Tier 2/3 incident responders, threat hunters, detection engineers. Output is **always in English**.

The intel run fires **multiple times per day**; each fire publishes only the *new* verified signal since the previous fire, as individual entry files under `entries/YYYY-MM-DD/`. A weekly strategic run adds the longer arc. **There is no brief file — the brief is a query**: [`/brief/`](https://ctipilot.ch/brief/) renders the entry store over a reader-chosen time window (default: the last 24 hours), and the rolling 24 h is calibrated to read exactly like one classic daily brief regardless of how many runs produced it. More runs mean lower latency, never more content.

The repository is the single source of truth for the workflow: prompts, source list, the entry store, the entity registry, per-run records, and every policy document are version-controlled. The normative data model is [`docs/pipeline.md`](docs/pipeline.md).

## Where to read

- **The brief:** [https://ctipilot.ch/brief/](https://ctipilot.ch/brief/) — the current intelligence window, assembled from the per-finding entries. Pick a wider window (6 / 12 / 24 / 48 / 72 h chips) or a start date; the default 24 h window is server-rendered and fully readable without JavaScript. Section structure and volume match a classic daily brief: TL;DR (+ Immediate-Action callout when one exists) → Active Threats → Trending Vulnerabilities → Research → Updates → Deep Dive → Action Items → Verification Notes.
- **Day archives:** `https://ctipilot.ch/briefs/YYYY-MM-DD/` — one static page per UTC day, the browsable historical record.
- **Weekly:** `https://ctipilot.ch/weekly/YYYY-Www/` — the week's strategic entries in the 12-section weekly structure, with the operational entries they synthesise linked in place.
- **Everything else:** per-entry permalinks (`/entries/<date>/<slug>/`), entity pages (`/entities/<key>/` — actors, campaigns, malware, tools, incidents, reports, plus every CVE), source catalogue (`/sources/`), tag/region indexes, the `/trends/` dashboard and the `/ops/` run-telemetry dashboard.
- **GitHub:** the entries are Markdown files under [`entries/`](entries/) — frontmatter metadata + analysis body, each readable natively on GitHub. Run records live under [`runs/`](runs/).

The site deploys automatically on every push to `main` that touches the content store. See [`site/README.md`](site/README.md) for internals and [`docs/operating.md`](docs/operating.md#3-enable-github-pages) for one-time enablement.

## RSS — eleven feeds

[`/feeds/`](https://ctipilot.ch/feeds/) is the single discovery page; every page advertises the three main feeds via `<link rel="alternate" type="application/rss+xml">` autodiscovery.

| URL | Contents | Truncation |
|-----|----------|------------|
| [`/feed.xml`](https://ctipilot.ch/feed.xml) | One item per day page | last 30 |
| [`/feed-weekly.xml`](https://ctipilot.ch/feed-weekly.xml) | One item per weekly page | last 30 |
| [`/feed-items.xml`](https://ctipilot.ch/feed-items.xml) | One item per published entry | last 50 |
| [`/feed-public-sector.xml`](https://ctipilot.ch/feed-public-sector.xml) | Per-entry slice — sector: public-sector | last 50 |
| [`/feed-healthcare.xml`](https://ctipilot.ch/feed-healthcare.xml) | Per-entry slice — sector: healthcare | last 50 |
| [`/feed-finance.xml`](https://ctipilot.ch/feed-finance.xml) | Per-entry slice — sector: finance | last 50 |
| [`/feed-energy.xml`](https://ctipilot.ch/feed-energy.xml) | Per-entry slice — sector: energy | last 50 |
| [`/feed-ot-ics.xml`](https://ctipilot.ch/feed-ot-ics.xml) | Per-entry slice — energy / water / manufacturing / transport / `ot-ics` tag | last 50 |
| [`/feed-defense.xml`](https://ctipilot.ch/feed-defense.xml) | Per-entry slice — sector: defense | last 50 |
| [`/feed-telco.xml`](https://ctipilot.ch/feed-telco.xml) | Per-entry slice — sector: telco | last 50 |
| [`/feed-education.xml`](https://ctipilot.ch/feed-education.xml) | Per-entry slice — sector: education | last 50 |

`<pubDate>` derives from each entry's `discovered_at` — the moment the pipeline verified the finding, not a publish schedule or commit time. Subscribing to `feed-items.xml` therefore delivers findings at true discovery latency. `<content:encoded>` carries full HTML. No UTM parameters, no per-source variants — every link is plain canonical.

## Reader features

- **The dynamic brief.** `/brief/` is a rendering over the entry store: default last-24 h window server-rendered (view source and you can read it), client-side re-windowing from `data/briefbook.json` (the last ~35 days of entries) when you pick a different window or a since-date.
- **Per-entry permalinks.** Every finding is a first-class page at `/entries/<date>/<slug>/` with its full metadata badges, update chain, and a link to the run record that produced it.
- **Notification surface.** `data/alerts.json` carries the last 7 days of `critical`/`high` entries with headline, summary, immediate-action block, entities and CVEs — machine-readable input for paging hooks and chat integrations. A `priority: critical` entry always carries a structured `immediate_action` block; the bar for `critical` is deliberately extreme (≤ 1 per rolling 24 h under normal conditions).
- **Entity registry pages.** Every actor, campaign, malware family, tool, incident and report the pipeline tracks is canonical in [`entities/registry.yaml`](entities/registry.yaml) and rendered at `/entities/<key>/` with coverage timeline, KPI tiles and co-occurrence links; aliases resolve to one page ("UNC6240" and "ShinyHunters" are the same entity, mechanically).
- **Update chains.** Entries are immutable; developments arrive as new entries with `update_of` links, so every story's evolution is browsable — the permalink of the original always leads forward.
- **Static HTML.** Every page contains its full content on first paint. JavaScript only enhances: window re-rendering on `/brief/`, search autocomplete, filter chips, theme cycle, copy-link.
- **Topbar search** across day pages, weeklies, entries, entities (every type) and sources — press `/` anywhere. CVE ids match as a single token.
- **Verification badges.** Single-source entries carry their `verification` value (`single-source`, `single-source-national-cert`, `single-source-victim`, `contradicted`) as reader-visible badges, auditable across the site.
- **Operations dashboard** at `/ops/` — recent runs from `runs/**` frontmatter: per-run gap/window, entries published, sub-agent allocation, fetch failures, verification iterations + residuals, prompt version.
- **Trends dashboard** at [`/trends/`](https://ctipilot.ch/trends/) — weekly-bucketed cohort sparklines (ransomware, actively-exploited vulnerabilities, public-sector, OT/ICS, supply-chain, AI-abuse, Switzerland+Europe, nation-state) computed from entry metadata.
- **Print stylesheet** — `Cmd/Ctrl+P` produces a clean, link-annotated PDF for handover.
- **Light / dark / system theme toggle**, persisted per device.
- **Privacy-by-design analytics** — Umami Cloud (no cookies, no fingerprinting), aggregate counts only; `analytics.provider: "none"` in `config/branding.yaml` turns it off entirely. See [`docs/analytics.md`](docs/analytics.md).
- **SEO** — per-page `<title>` / description / OpenGraph + canonical URLs, sitemap.xml, robots.txt.

## What this repo contains

```
.
├── entries/                   # THE content store — one file per verified finding
│   ├── README.md              # Contract pointer (docs/pipeline.md is normative)
│   └── YYYY-MM-DD/<slug>.md   # Frontmatter = full metadata; body = analysis; immutable
├── entities/
│   ├── README.md              # Registry contract pointer
│   └── registry.yaml          # Global entity registry (actors, campaigns, malware, …)
├── runs/
│   ├── README.md              # Run-record contract pointer
│   └── YYYY-MM-DD/<run-id>.md # One per fire: telemetry frontmatter + verification notes
├── prompts/                   # Everything the routines load at runtime
│   ├── cti-run.md             # The intel-run master prompt (fired N× per day)
│   ├── weekly-summary.md      # The weekly strategic run (builds on cti-run.md)
│   ├── CHANGELOG.md           # Editorial-policy audit trail
│   ├── verification.md        # Fake-news / two-source verification policy
│   ├── entry-template.md      # Canonical entry + run-record skeletons
│   └── check-run-fixes.md     # How to fix common check_run.py FAILs
├── config/
│   ├── org-profile.yaml       # Organization profile: org/sector/region, watchlists, triage scheme, deployment
│   └── branding.yaml          # Site branding: identity, theme, logos, feeds, analytics
├── intel/
│   └── README.md              # Closed-source drop folder (intel/<date>/, TLP-gated, cited by reference)
├── sources/
│   └── sources.json           # Curated, dynamic CTI source list (~150 sources, tiered)
├── state/
│   ├── cves_seen.json         # Flat fast-lookup CVE index (dedup)
│   └── source_health.json     # Bounded source-accessibility history
├── tools/
│   ├── check_run.py           # Phase 5.5 mechanical gate (must exit 0 before commit)
│   ├── build_prior_coverage.py# Per-run dedup index from the entry store
│   ├── run_summary.py         # Compact state digest + rolling-24 h budget snapshot
│   ├── compose_prompts.py     # Renders org-profile.yaml into the ORG-PROFILE managed blocks
│   ├── fetch_source.py        # Bridge fetcher for hosts that 403 the routine UA
│   ├── migrate_briefs.py      # One-shot v2→v3 migration (kept for provenance)
│   ├── source_candidates.py   # Cited-but-untracked publisher surfacing
│   └── source_health.py       # Recipe-level source accessibility probe
├── site/                      # GitHub Pages reader (static-site generator, stdlib-only)
│   ├── build.py               # SSG entrypoint — dynamic /brief/, day/weekly pages, feeds, ops
│   ├── content_model.py       # THE shared parser/validator for entries, registry, runs
│   ├── taxonomy.yaml          # Controlled vocabulary for entry frontmatter
│   ├── test_build.py          # Stdlib-only smoke tests
│   └── assets/                # CSS, JS (brief.js window renderer), vendored libs
├── docs/
│   ├── pipeline.md            # NORMATIVE v3 data model (entries, registry, runs)
│   ├── architecture.md        # End-to-end map: what reads/writes what
│   ├── operating.md           # Operator runbook: setup, ops dashboard, troubleshooting
│   ├── customization.md       # Downstream fork / rebrand guide
│   ├── private-deployment.md  # Host the whole stack org-internally
│   └── analytics.md           # What we measure, what we don't
├── .github/workflows/
│   ├── auto-merge-claude.yml  # Promotes pushes to claude/** branches onto main
│   ├── deploy-site.yml        # Build + deploy site/ to GitHub Pages
│   ├── source-health.yml      # Weekly cron firing tools/source_health.py
│   └── compose-profile.yml    # Composes config/org-profile.yaml into the prompts on push
├── .claude/agents/
│   ├── cti-research.md        # Parallel research worker (S1–S5 / W1–W3)
│   ├── cti-verification.md    # Cold-reader verifier (Opus default; F1–F16)
│   └── cti-verification-alt.md# Sonnet rotation variant (byte-identical body)
├── work/<run-id>/             # Per-run forensic artefacts, committed with each run
└── CNAME                      # Custom-domain marker for GitHub Pages → ctipilot.ch
```

For an end-to-end map of how every piece reads and writes data, see [`docs/architecture.md`](docs/architecture.md). For operator setup and the runbook, see [`docs/operating.md`](docs/operating.md).

## Customizing for your organization

The deployment is organization-parameterizable via [`config/org-profile.yaml`](config/org-profile.yaml): describe your organisation / sector / region (the shipped default is the Swiss public-sector deployment), list **products** and **suppliers** the research agents specifically sweep every run, define your own **vulnerability-triage categories** (every CVE-carrying entry then carries a structured `org_triage` rating in your scheme), set the **national-CERT single-source carve-out list** your deployment trusts, and the **policy/regulatory watch** the weekly tracks. `python3 tools/compose_prompts.py --write` renders the profile into the prompts and agent definitions (the `compose-profile` workflow does it on push). Watchlist matches only *sharpen* relevance — general threat-landscape coverage always stays primary (hard anti-overshoot rules; watchlist-driven entries carry `watchlist_hit: true` and the ≤ ⅓ guideline applies). See [`docs/operating.md`](docs/operating.md#customizing-the-organization-profile).

The **published site is equally parameterizable** via [`config/branding.yaml`](config/branding.yaml) + [`site/branding/`](site/branding/README.md): site name and wordmark, taglines, theme colors and fonts, logos and favicon, chart palettes, sector RSS slices, trend cohorts, and analytics (`analytics.provider: "none"` is a one-line tracking off switch that also strips the third-party origins from the CSP). The shipped config *is* the ctipilot.ch default and builds a byte-identical site. **Downstream forks customize only `config/*.yaml` + `site/branding/` + `CNAME` + this README and merge upstream conflict-free** — the full guide is [`docs/customization.md`](docs/customization.md).

## Operating principles (non-negotiable)

These principles are encoded in the prompts and enforced by quality gates on each run.

1. **Zero LLM knowledge.** Every fact in any entry comes from a source fetched in that run. Nothing from training data.
2. **Inline source links at the point of claim.** No bibliography. The reader can click through from the exact sentence; the frontmatter `sources[]` list and the body's inline links must agree.
3. **No IOCs.** No hashes, IP addresses, attacker-controlled domains/URLs, or rule code. Entries cover *knowledge* — TTPs, campaigns, actors, vulnerabilities, targeting, sectors, detection concepts. IOC distribution belongs elsewhere (e.g., MISP).
4. **No vanity metrics.** Skip "median dwell time", "X% YoY", and similar vendor-marketing numbers. Operational scoring (CVSS, EPSS, KEV status) is fine.
5. **Always English** (output). Sources may be in German / French / Italian / Polish; entries translate findings and cite originals by their native title with a brief English gloss.
6. **Two-source verification by default**, with carve-outs for a national CERT / government authority disclosing for its own jurisdiction and a victim's own filing about its own incident. Single-source entries carry a structured `verification` value (`single-source`, `single-source-national-cert`, `single-source-victim`) rendered as a reader-visible badge; contradictions are flagged, never silently resolved.
7. **No repetition across runs.** Every run builds a prior-coverage index over the last 7 days of entries — **including entries earlier runs published the same day** — and publishes only the delta. A covered story returns solely as a new entry with `update_of: <original entry id>` carrying a material delta; the mechanical gate FAILs CVE-level duplicates.
8. **Volume discipline.** The rolling 24 h across all runs stays in the one-daily-brief band: soft ceiling 14 operational entries, ≤ 1 deep-dive entry per UTC day, ≤ 1 `priority: critical` per 24 h. More runs mean lower latency, never more content. A run that finds nothing publishes only its run record — a healthy outcome.
9. **Priority is the alert-fatigue control surface.** `critical` ⇔ a structured `immediate_action` block (mechanically enforced) and means "stop reading and act now"; `high` leads the window's TL;DR; `notable` is the standard item; `routine` is kept-for-awareness. A false `critical` trains readers to ignore the channel.
10. **One entity namespace.** Every named actor / campaign / malware / tool / incident / report resolves to a key in `entities/registry.yaml`; aliases are checked before anything new is registered; keys are permanent.
11. **Yearly / periodic threat reports get one dedicated entry**, then are never re-summarised — later coverage references the report's registry entity.
12. **Historical-context rule.** Deep-dive entries on topics with prior public reporting older than ~6 months open with a 3–5-sentence Background paragraph citing 2–3 prior reports.
13. **Recency is gap-derived and self-healing.** Each run's window is computed from the previous run record (`window_hours = max(6, gap_hours + 2)`); a missed fire simply widens the next window. The underlying event's date is recorded as `event_date` so freshness is never misrepresented.
14. **One new candidate source per run, maximum.** A flood of new candidates is anomalous; overflow waits for the next run.

## The intel run

A scheduled Claude Code routine fires on whatever cadence the operator configured — **several times per working day is the intended pattern** (e.g. every 4–6 hours). The routine is given exactly one instruction: `Read prompts/cti-run.md and execute it.`

The recency window is **derived from the previous run record, not from a hardcoded schedule**: every fire computes `gap_hours` since the last record under `runs/` and covers the gap plus a 2-hour safety overlap (`window_hours = max(6, gap_hours + 2)`). This makes the system **self-healing** for missed fires — the next window simply widens — and **cadence-agnostic** — the operator can fire it 1× or 6× a day without touching the prompt. Entry-level dedup makes the overlap harmless.

> **One-time setup** required for the routine to publish back to this repo: install the Claude GitHub App on the repo, leave **Allow unrestricted branch pushes** *off* (the routine pushes to `claude/**` only — the auto-merge workflow promotes), and enable Pages. Full instructions: [`docs/operating.md`](docs/operating.md).

Each fire walks through:

1. **Phase 0 — Preflight.** Compute the run id (`YYYY-MM-DDTHHMMZ-intel` — minute-precision, so multiple runs per day are first-class and a same-minute retry is idempotent). Build the prior-coverage index over the last 7 days of entries *including earlier runs today* (`tools/build_prior_coverage.py`) and the compact state digest with the rolling-24 h budget snapshot (`tools/run_summary.py`); read `entities/registry.yaml` + `site/taxonomy.yaml`; detect closed-source drops under `intel/`.
2. **Phase 1 — Parallel research.** Spawn four `cti-research` sub-agents with tiered source slices — (S1) Active Threats & Trending Vulnerabilities, (S2) Home Region & Sector, (S3) Research & Investigative Reporting, (S4) Incidents & Disclosures — plus a conditional S5 intake when intel drops exist. Every worker reads the prior-coverage index and the registry *before* fetching. Essential-tier sources (national CERTs, CISA, ENISA, …) are attempted every run; standard-tier sources rotate by staleness.
3. **Phase 2 — Verification & triage.** URL spot-checks, two-source / carve-out rule, fake-news guard, CVE verification on NVD/MITRE, the dedup decision (new entry vs `update_of` vs drop), recency re-check, 24 h budget check, priority assignment.
4. **Phase 3 — Deep-dive selection.** ≤ 1 deep-dive entry per UTC day across all runs, with category rotation derived from the last 30 days of `deep_dive: true` entries.
5. **Phase 4 — Compose.** One `Write` per finding — `entries/YYYY-MM-DD/<slug>.md`, strictly from the sub-agents' findings files (anti-embellishment rules; no enrichment from memory) — plus the run record `runs/YYYY-MM-DD/<run-id>.md`: telemetry frontmatter + verification & coverage notes body.
6. **Phase 5 — State update.** Register new entities (same commit as the entries that need them), sync `state/cves_seen.json`, run the source lifecycle on `sources/sources.json`, refresh `state/source_health.json`.
7. **Phase 5.5 — Mechanical gate.** `python3 tools/check_run.py <run-id>` must exit 0: schema/taxonomy/registry validation, cross-run CVE dedup, volume budgets, `priority` ⇔ `immediate_action`, evidence binding, URL block-list + liveness, IOC scan, run-record completeness, site smoke tests. Fix recipes: [`prompts/check-run-fixes.md`](prompts/check-run-fixes.md).
8. **Phase 5.7 — Verifier loop (gatekeeper).** [`cti-verification`](.claude/agents/cti-verification.md) reads the run's entries + record cold; CLEAN gates publish. NEEDS_FIXES → remediate, re-run the gate, re-spawn fresh. **5-iteration cap with model rotation** — odd iterations Opus, even iterations the Sonnet-pinned [`cti-verification-alt`](.claude/agents/cti-verification-alt.md) — and a documented fail-open at the cap. Verification can drop entries; it never blocks the run record.
9. **Phase 6 — Commit & push the feature branch**; `auto-merge-claude.yml` promotes to `main` (auto-resolution: `state/*.json` + `entities/registry.yaml` → ours, `sources/sources.json` → theirs), then `deploy-site.yml` rebuilds the site. **Phase 7** polls the run record on `origin/main` and then `data/briefbook.json` for the run id — a pushed feature branch is not a published run.

Full walkthrough lives in the prompt itself ([`prompts/cti-run.md`](prompts/cti-run.md)). Architecture map: [`docs/architecture.md`](docs/architecture.md). Operator runbook: [`docs/operating.md`](docs/operating.md).

## The weekly run

A separate routine fires once per week (operator-chosen day and time): `Read prompts/weekly-summary.md and execute it.` The weekly prompt **builds on the intel-run prompt** — it `Read`s `cti-run.md` at runtime and defines only the divergent lens, so shared machinery can never copy-drift.

The weekly reads the week's operational entries, builds its working lists (what's on fire if no one acted, multi-day chains, CVE roll-up, sector patterns, incidents recap), spawns horizon sub-agents (W1 threat-actor / campaign / research / report horizon; W2 policy & regulatory; conditional W3 intake), and composes `horizon: strategic` entries placed by `weekly_section` — each listing the operational entries it synthesises via `references`. Run id: `YYYY-MM-DDTHHMMZ-weekly`; the `/weekly/YYYY-Www/` page is rendered from these entries. Unlike intel runs, the weekly **may re-frame operational coverage** with a new lens — the asymmetry runs one way; intel runs never duplicate the weekly.

## Source list and CVE index — autonomous

The repository is the agent's working memory. Both `sources/sources.json` and `state/cves_seen.json` are maintained by the runs with **no human review gate**. Every change appears in the run's git diff, the commit message, and the run record's `sources_changed[]` telemetry; that's the audit trail.

### Source lifecycle (all transitions autonomous)

- **Discovery → candidate.** When a sub-agent encounters a new high-quality publisher (primary source, editorial track record, in-scope) during research, it's added to `sources.json` with `status: "candidate"`. **At most one new candidate per run** — overflow waits for the next run.
- **Candidate → active.** A candidate is auto-promoted to `active` after **3 distinct runs** in which the source was successfully fetched *and* contributed content to a published entry.
- **Active → demoted (content axis only).** Demotion fires only on the **content axis**, never on the transport axis. After 3 consecutive `consecutive_quiet_periods` increments accompanied by a failed canonical-URL probe, OR after 5 consecutive `consecutive_fetch_failures` of code 404 (sustained 4xx-not-403/429), the source's `reliability` drops one tier and `status` becomes `demoted`. Sustained 403 / 429 / 503 / 5xx **never** demotes — that pattern means the publisher is blocking the agent's request shape, not that the source is dead. For those, the agent records an alternate-URL strategy in `notes` and keeps the source in rotation.
- **Demoted → active (recovery).** A demoted source returns to `active` only when the agent finds a working canonical URL during research and the recovered URL contributes content to an entry.
- **URL updates in place.** Any time a better canonical URL is found for an active source (publisher CMS migration, restructured advisories index), update `url` and append a dated note. The source `id` stays stable so historical references remain valid.

**No source deletion.** Demoted and tier-downgraded sources stay in the file as historical record.

On top of the lifecycle, every source carries a `tier`: the ~14 `essential` records (national CERTs, NCSC-CH, CERT-EU, ENISA, BSI, ANSSI, NCSC-UK, NCSC-NL, CERT-PL, CERT-AT, CISA) are attempted on **every** intel run — a miss is disclosed in the run record — while `standard` records rotate on a staleness ranking so nothing silently starves and nothing floods.

### CVE index — autonomous

The agent appends new CVE IDs, bumps `last_seen` on subsequent appearances, updates `title` or `primary_source_url` when better information emerges, and **removes** entries that turn out to be invalid (e.g., a CVE ID that does not resolve on NVD/MITRE). Removals are documented in the run's commit body.

The current list (~150 sources) covers: Swiss/EU national CERTs (NCSC-CH, GovCERT.ch, CERT-EU, ENISA, BSI, ANSSI, NCSC-UK, NCSC-NL, CERT.at, GovCERT.at, CERT-PL, AGID, CCN-CERT); Swiss security firms (Compass Security, scip AG, OneConsult, InfoGuard, Kudelski Security, PRODAFT); top-tier vendor TI (Mandiant/GTIG, Microsoft, CrowdStrike, Unit 42, Cisco Talos, Volexity, ESET, Kaspersky Securelist, Trend Micro, Check Point, Sophos X-Ops, Secureworks, Recorded Future Insikt, Sekoia, Group-IB, Elastic Security Labs, Huntress, Red Canary, The DFIR Report, Sygnia, Truesec, NCC Group, WithSecure Labs, IBM X-Force, Akamai, Cloudflare Cloudforce One, Trustwave SpiderLabs, Tenable, Rapid7); vulnerability research (CISA KEV, watchTowr Labs, Project Zero, ZDI, VulnCheck, GreyNoise, Shadowserver); OT/ICS (Dragos, SANS ICS); journalism (Krebs, Schneier, Inside IT, Le Monde Informatique, Malwarebytes, The Record, CyberScoop, BleepingComputer, SecurityWeek, Security Affairs, Help Net Security, SANS ISC, Dark Reading); breach trackers (SEC EDGAR 8-K, UK ICO, CNIL FR, EDPB); civil-society research (Citizen Lab); discovery (r/netsec).

## Reader engagement (privacy-by-design)

The site uses **Umami Cloud** for aggregate visitor counts so the operator can see whether the pipeline's output is being read. Umami is a privacy-by-design alternative to mainstream analytics:

- No cookies. No fingerprinting. No personal data persisted.
- Aggregates only: page URL, referrer host, country (IP discarded after lookup), and a daily-rotated hash for unique-visitor counting.
- Search-string parameters are excluded from collection.
- Block at the network layer if you don't want to be counted: `cloud.umami.is` in your browser, ad-blocker, or DNS resolver. The site keeps working without it.

The site's strict CSP allows only `'self'`, `https://cloud.umami.is` (the script), and `https://gateway.umami.is` (the beacon endpoint) for `script-src` / `connect-src` — no other third-party origin can run code or receive data from this page. Full disclosure at [`/about/docs/analytics/`](https://ctipilot.ch/about/docs/analytics/).

The pipeline's Phase 0 does **not** consume any engagement signal. Editorial weighting is purely verification + home-region/coverage-focus nexus + novelty per [`prompts/verification.md`](prompts/verification.md); what is read is not reflected in what is written.

## Security posture

This is a fully autonomous, self-evolving system: the agent edits its own prompts, mutates its own state, and publishes via the feature-branch + auto-merge chain. The defensive frame is "detect and correct", not "prevent at all costs". Highlights:

- **Phase 5.5 mechanical gate.** Before the verifier and before every commit, `tools/check_run.py` must exit 0: every entry's frontmatter parses and is schema- and taxonomy-valid, entity keys resolve in the registry, `update_of` chains resolve, no cross-run CVE duplicates, `priority` ⇔ `immediate_action` holds, evidence quotes are bound, no blocked/dead source URLs, no IOCs, the run record is complete, and the site smoke tests pass.
- **Adversarial verification loop.** An independent cold-reader sub-agent (model-rotated across iterations) re-fetches every URL and traces every claim before publish; its CLEAN verdict gates the commit.
- **Entry immutability.** Published entries are never edited — corrections are new `update_of` entries, so the published record cannot be silently rewritten.
- **Feature-branch-only publishing.** Nothing writes to `main` except the auto-merge workflow; every routine commit is a reviewable diff.
- **Vendored library integrity.** `site/build.py` aborts on SHA-256 mismatch against [`site/assets/vendor/HASHES`](site/assets/vendor/HASHES).
- **Strict CSP** delivered via meta tag — no inline scripts; `script-src` / `connect-src` restricted to `'self'` plus the two Umami origins; no inline frames or forms.
- **Build-side Markdown sanitisation** with a pinned tag/URI-scheme allowlist. The build refuses any rendered output that would carry an event handler, a `javascript:` / `data:` URI, or a forbidden tag.
- **Site privacy guarantees:** no cookies, no fingerprinting, no third-party scripts other than Umami's privacy-by-design tracker.

## Verification policy

Entries explicitly defend against fake-news patterns common in CTI feeds: ransomware leak-site theatrics, hallucinated CVE numbers, AI-generated security blogspam, vendor PR dressed as research, re-runs of months-old news (the `event_date` field pins the real timeline), sweeping unbacked attribution, and Telegram/X-only sourcing.

See [`prompts/verification.md`](prompts/verification.md) for the full checklist and the `verification` frontmatter enum that surfaces the sourcing status of every entry.

## License / classification

Entries default to **TLP:CLEAR** unless otherwise stated. The repository contains no IOCs and no operationally sensitive material — only public-source synthesis with links. Closed-source intelligence above TLP:CLEAR never appears in entries on the public deployment (mechanically gated; see [`intel/README.md`](intel/README.md)).
