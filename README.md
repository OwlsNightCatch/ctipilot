# Security Newsletter — Daily & Weekly CTI Briefs

> **AI-generated content notice.** Every brief in this repository is produced autonomously by an LLM running as a [Claude Code routine](https://docs.claude.com/en/docs/claude-code/routines) on Anthropic-managed cloud infrastructure. The exact model varies based on the routine's runtime configuration; the model identifies itself in each brief's header. The agent fetches public sources, applies the verification rules in [`docs/verification.md`](docs/verification.md), and writes the Markdown briefs you see in `briefs/`. Every claim in a brief is linked inline to its source. The repository contains the prompts, source list, state files, and policy documents that govern this generation. Verify any operationally critical claim against the linked primary source before acting on it. The briefs are not professional advice and may contain errors.

A daily Cyber Threat Intelligence brief covering cyber threats targeting Switzerland and Europe with a public-sector focus (national/cantonal/federal administration, regulators, critical infrastructure, healthcare, education, public-sector technology suppliers), plus a once-a-week consolidating summary. Audience: Tier 2/3 incident responders, threat hunters, detection engineers. Output: one Markdown file per day under `briefs/` and one per ISO week under `briefs/weekly/`. Output is **always in English**.

The repository is the single source of truth for the workflow: prompts, source list, rolling coverage state, and every brief are version-controlled.

## Where to read

- **Public reader:** [https://owlsnightcatch.github.io/security-newsletter/](https://owlsnightcatch.github.io/security-newsletter/) — the static GitHub Pages site. Home shows a preview of the latest daily brief; click through for the full text. Cross-links span briefs, CVEs, topics, and sources, with full-text and section-level search. The site has an **About** page that renders this same README directly from the repository — if you found this file via the site, you are already reading it. The site also exposes an [RSS feed](https://owlsnightcatch.github.io/security-newsletter/feed.xml).
- **GitHub:** the briefs are markdown files under [`briefs/`](briefs/). Each brief is a self-contained operational report that reads natively on GitHub.

The site deploys automatically on every push to `main` that touches the brief feed. See [`site/README.md`](site/README.md) for internals and [`docs/routine-setup.md`](docs/routine-setup.md#enable-github-pages) for one-time enablement.

## Reader features

- **Home preview** — the landing view shows the TL;DR of the latest daily brief; clicking *Read the full brief* opens the full text.
- **Cross-linked entities** — every CVE, source, and topic page lists the briefs that mention it; every brief lists the CVEs, topics and sources it cites.
- **Section-level search** — typing in the top bar matches brief sections (H3 headings) as separate results, jumping straight to the relevant paragraph inside a brief.
- **Verification filters** — the Topics page can filter by `[SINGLE-SOURCE]`, `[SINGLE-SOURCE-NATIONAL-CERT]`, or `[SINGLE-SOURCE-OTHER]` so a SOC reviewer can audit single-source items across all briefs at once.
- **Operations dashboard** at `/#/ops` — recent runs (sub-agent allocation, fetch failures, deep-dive picks) and stale active sources (no successful fetch for >7 days). Useful for spotting rotation bias or a quietly broken source.
- **RSS feed** at `/feed.xml`.
- **Print stylesheet** — `Cmd/Ctrl+P` produces a clean, link-annotated PDF for handover.
- **Light / dark / system theme toggle** — top-bar button cycles `system → light → dark → system`; persisted per device.
- **Per-brief metadata badge** — each brief header shows the prompt version that produced it, linking to the changelog entry.
- **Permalink** — each brief has a *Copy link* button that puts the canonical SPA URL on your clipboard.
- **Privacy-by-design analytics** — Umami Cloud (no cookies, no fingerprinting), aggregate counts only. See About → *Analytics & privacy* for the full disclosure.
- **SEO** — per-route `<title>` / `description` / OpenGraph rewrites in the SPA, plus a static `sitemap.xml` and JSON-LD `WebSite` block.

## What this repo contains

```
.
├── prompts/
│   ├── daily-cti-brief.md     # The canonical daily prompt
│   ├── weekly-summary.md      # The weekly summary prompt
│   └── CHANGELOG.md           # Editorial-policy audit trail (rendered on the About page)
├── sources/
│   └── sources.json           # Curated, dynamic CTI source list (~80 sources)
├── state/
│   ├── covered_items.json     # Rolling log of items reported and when (full records)
│   ├── cves_seen.json         # Flat fast-lookup CVE index (sub-agent dedup)
│   ├── deep_dive_history.json # Last 30 days of deep-dive picks (rotation memory)
│   └── run_log.json           # Per-run sub-agent allocation, fetch failures (Ops view)
├── briefs/
│   ├── README.md              # Brief format and conventions
│   ├── YYYY-MM-DD.md          # Daily briefs
│   └── weekly/
│       └── YYYY-Www.md        # Weekly summaries (ISO week)
├── tools/
│   └── fetch_source.py        # Bridge fetcher for CISA / NCSC CSH (browser UA, host-allowlisted)
├── site/                      # GitHub Pages reader (static SPA)
│   ├── index.html             # SPA shell — vanilla JS, no framework
│   ├── build.py               # Stdlib-only Python build of the data bundle
│   ├── README.md              # Site internals
│   └── assets/                # CSS, JS, vendored marked/DOMPurify
├── docs/
│   ├── architecture.md        # End-to-end map: what reads/writes what
│   ├── workflow.md            # End-to-end daily & weekly agent process
│   ├── routine-setup.md       # One-time Claude Code routine + Pages setup
│   ├── verification.md        # Fake-news verification policy
│   ├── security-review.md     # Threat model for the autonomous-agent setup
│   └── improvements.md        # Recommended improvements (with rationale)
├── .github/workflows/
│   ├── auto-merge-claude.yml  # Routine fallback: ff-merge claude/* → main
│   └── deploy-site.yml        # Build + deploy site/ to GitHub Pages
└── .gitignore
```

For an end-to-end map of how every piece reads and writes data, see [`docs/architecture.md`](docs/architecture.md). For improvements identified but not yet implemented, see [`docs/improvements.md`](docs/improvements.md).

## Operating principles (non-negotiable)

These principles are encoded in the prompts and enforced by quality gates on each run.

1. **Zero LLM knowledge.** Every fact in any brief comes from a source fetched in that run. Nothing from training data.
2. **Inline source links at the point of claim.** No bibliography. The reader can click through from the exact sentence.
3. **No IOCs.** No hashes, IP addresses, attacker-controlled domains/URLs, or rule code. Briefs cover *knowledge* — TTPs, campaigns, actors, vulnerabilities, targeting, sectors, detection concepts. IOC distribution belongs elsewhere (e.g., MISP).
4. **No vanity metrics.** Skip "median dwell time", "breakout time", "X% YoY", "Y new adversaries tracked", and similar vendor-marketing numbers. Operational scoring (CVSS, EPSS, KEV status) is fine.
5. **Always English** (output). Sources may be in German / French / Italian / Polish; the brief translates findings and cites originals by their native title with a brief English gloss.
6. **Two-source verification by default**, with a national-CERT carve-out for HIGH-reliability authorities (NCSC-CH, GovCERT.ch, CERT-EU, BSI, ANSSI, NCSC-UK, NCSC-NL, CISA, CCN-CERT, AGID, CERT.at, CERT-PL) when they are the primary disclosing party for their own jurisdiction. Other single-source items are flagged `[SINGLE-SOURCE]`.
7. **No repetition across runs.** The agent reads the **last 7 days of briefs** plus the most recent weekly summary plus `state/cves_seen.json` and `state/covered_items.json` before writing. Repeats appear only under "Updates to Prior Coverage" with a material new-information delta.
8. **Yearly / periodic threat reports get one dedicated treatment**, then are not re-summarised. Specific findings can be cross-referenced as context.
9. **Historical-context rule.** For *highly relevant* deep-dive items with prior public reporting older than ~6 months, the brief includes a 3–5-sentence Background paragraph linking 2–3 of the most relevant prior reports.
10. **Long-running campaigns** get ≤1 consolidated UPDATE per week unless something critical changes. The weekly summary is the canonical place for "what happened with X this week".
11. **Recency.** Daily window: 24 h default, 72 h for actively developing items.
12. **No suppression, no padding.** Empty sections state so explicitly.
13. **Deep-dive category rotation.** The agent keeps a 30-day rolling history of deep-dive picks and demotes a candidate one rank if its category was already covered in the prior 7 days, unless active exploitation makes it irreducibly urgent.
14. **One new candidate source per run, maximum.** A flood of new candidates is anomalous; overflow goes into the next run via § 7.

## Daily routine

A scheduled Claude Code routine fires on whatever cadence the operator configured. The recommended pattern is **working days only**, so the prompt assumes Saturday and Sunday are not covered by the daily routine. The routine is given exactly one instruction: read [`prompts/daily-cti-brief.md`](prompts/daily-cti-brief.md) and execute it.

The recency window is **derived from `briefs/`, not from a hardcoded schedule** (Prime Directive 7). Every run computes the gap since the last brief on disk and covers the entire gap plus a 12-hour safety overlap. This makes the system **self-healing** for missed runs — if Tuesday's run fails, Wednesday's run sees a ~48 h gap and naturally extends its window — and **schedule-agnostic** — the operator can change cron times, days, or even routines without touching the prompt. The brief that lands always covers everything since the previous published brief.

> **One-time setup** required for the routine to publish back to this repo: install the Claude GitHub App on the repo, and (optionally) enable **Allow unrestricted branch pushes** in the routine's permissions for direct-to-`main` publishing. Full instructions: [`docs/routine-setup.md`](docs/routine-setup.md).

The agent walks through:

1. **Phase 0 — Preflight.** Load source list, last 7 days of briefs (and the most recent weekly summary for the current and prior ISO weeks), state files, deep-dive history.
2. **Phase 1 — Parallel research.** Spawn **four** sub-agents in parallel with cleanly partitioned source categories — (1) Active Threats & Trending Vulnerabilities, (2) Switzerland, Europe & Public Sector, (3) Research & Investigative Reporting, (4) Incidents & Disclosures.
3. **Phase 2 — Verification.** Re-fetch primaries, enforce two-source / national-CERT rule, drop already-covered items, surface contradictions.
4. **Phase 3 — Deep-dive selection.** At most 1–2 items, with the category-rotation rule applied.
5. **Phase 4 — Compose.** Write `briefs/YYYY-MM-DD.md` with sections 0–7, including the prompt-version metadata field.
6. **Phase 5 — State update.** Append to `covered_items.json` and `cves_seen.json`; bump `last_successful_fetch` on used sources; propose at most one new source as `candidate`; append to `deep_dive_history.json` if a deep dive was selected; append a record to `run_log.json`.
7. **Phase 5.5 — Self-check gate.** Verify state JSON parses, every CVE in the brief is in `cves_seen.json`, every § 1–4 item has a matching `covered_items.json` appearance for today. If any check fails, abort the commit; the brief stays on disk and the next run rebuilds state from it.
8. **Phase 6 — Commit & push to `origin/main`** — every brief is published the moment it is generated. No review branch, no staging gate.

Full walkthrough: [`docs/workflow.md`](docs/workflow.md).

## Weekly routine

A separate scheduled routine fires once per week (operator-chosen day and time — no schedule is hardcoded). Reads [`prompts/weekly-summary.md`](prompts/weekly-summary.md). Output: `briefs/weekly/YYYY-Www.md`. The same gap-derivation rule applies: each run reads `briefs/weekly/` to find the previous summary and covers the entire gap. A missed week is automatically caught up by the next run.

The weekly summary reads every daily brief from the past 7 days, builds a top-stories list, multi-day campaign roll-ups, full CVE roll-up table, sector/victim patterns, and major-breaches recap. It then spawns horizon sub-agents (long-horizon campaigns, yearly/periodic reports, policy/regulatory) for material the dailies did not cover, distils any newly published yearly threat report, and produces a "looking ahead" list. Unlike the daily brief, the weekly summary **may repeat material** from the dailies — that is its consolidating purpose.

## Source list and CVE index — autonomous

The repository is the agent's working memory. Both `sources/sources.json` and `state/cves_seen.json` are maintained by the routine on each run with **no human review gate**. Every change appears in the run's git diff and commit message; that's the audit trail.

### Source lifecycle (all transitions autonomous)

- **Discovery → candidate.** When a sub-agent encounters a new high-quality publisher (primary source, editorial track record, in-scope) during research, it's added to `sources.json` with `status: "candidate"`. **At most one new candidate per run** — overflow waits for the next run.
- **Candidate → active.** A candidate is auto-promoted to `active` after **3 distinct runs** in which the source was successfully fetched *and* contributed content to a brief.
- **Active → demoted (content axis only).** Demotion fires only on the **content axis**, never on the transport axis. After 3 consecutive `consecutive_quiet_periods` increments accompanied by a failed canonical-URL probe, OR after 5 consecutive `consecutive_fetch_failures` of code 404 (sustained 4xx-not-403/429), the source's `reliability` drops one tier and `status` becomes `demoted`. Sustained 403 / 429 / 503 / 5xx **never** demotes — that pattern means the publisher is blocking the agent's request shape, not that the source is dead. For those, the agent records an alternate-URL strategy in `notes` and keeps the source in rotation.
- **Demoted → active (recovery).** A demoted source returns to `active` only when the agent finds a working canonical URL during research and the recovered URL contributes content to a brief.
- **URL updates in place.** Any time a better canonical URL is found for an active source (publisher CMS migration, restructured advisories index), update `url` and append a dated note. The source `id` stays stable so historical references in `state/covered_items.json` remain valid.

**No source deletion.** Demoted and tier-downgraded sources stay in the file as historical record.

### CVE index — autonomous

The agent appends new CVE IDs, bumps `last_seen` on subsequent appearances, updates `title` or `primary_source_url` when better information emerges, and **removes** entries that turn out to be invalid (e.g., a CVE ID that does not resolve on NVD/MITRE). Removals are documented in the run's commit body.

The current list (~80 sources) covers: Swiss/EU national CERTs (NCSC-CH, GovCERT.ch, CERT-EU, ENISA, BSI, ANSSI, NCSC-UK, NCSC-NL, CERT.at, GovCERT.at, CERT-PL, AGID, CCN-CERT); Swiss security firms (Compass Security, scip AG, OneConsult, InfoGuard, Kudelski Security, PRODAFT); top-tier vendor TI (Mandiant/GTIG, Microsoft, CrowdStrike, Unit 42, Cisco Talos, Volexity, ESET, Kaspersky Securelist, Trend Micro, Check Point, Sophos X-Ops, Secureworks, Recorded Future Insikt, Sekoia, Group-IB, Elastic Security Labs, Huntress, Red Canary, The DFIR Report, Sygnia, Truesec, NCC Group, WithSecure Labs, IBM X-Force, Akamai, Cloudflare Cloudforce One, Trustwave SpiderLabs, Tenable, Rapid7); vulnerability research (CISA KEV, watchTowr Labs, Project Zero, ZDI, VulnCheck, GreyNoise, Shadowserver); OT/ICS (Dragos, SANS ICS); journalism (Krebs, Schneier, Heise Security, Inside IT, Le Monde Informatique, Malwarebytes, The Record, CyberScoop, BleepingComputer, SecurityWeek, Security Affairs, Help Net Security, SANS ISC, Dark Reading); breach trackers (SEC EDGAR 8-K, UK ICO, CNIL FR, EDPB); civil-society research (Citizen Lab); discovery (r/netsec).

## Reader engagement (privacy-by-design)

The site uses **Umami Cloud** for aggregate visitor counts so the operator can see whether the newsletter is being read. Umami is a privacy-by-design alternative to mainstream analytics:

- No cookies. No fingerprinting. No personal data persisted.
- Aggregates only: page URL, referrer host, country (IP discarded after lookup), and a daily-rotated hash for unique-visitor counting.
- Search-string parameters are excluded from collection.
- Block at the network layer if you don't want to be counted: `cloud.umami.is` in your browser, ad-blocker, or DNS resolver. The site keeps working without it.

The site's strict CSP allows only `'self'` and `https://cloud.umami.is` for both `script-src` and `connect-src` — no other third-party origin can run code or receive data from this page. Full disclosure on the [About page](https://owlsnightcatch.github.io/security-newsletter/#/about?at=analytics).

The agent's Phase 0 does **not** consume any engagement signal. Editorial weighting is purely verification + CH/EU nexus + novelty per [`docs/verification.md`](docs/verification.md). Full posture in [`docs/security-review.md`](docs/security-review.md) § 4.

## Security posture

This is a fully autonomous, self-evolving system: the agent edits its own prompts, mutates its own state, and pushes directly to `main`. The defensive frame is "detect and correct", not "prevent at all costs". Threat model and current controls are documented in [`docs/security-review.md`](docs/security-review.md). Highlights:

- **Phase 5.5 self-check.** Before commit, the agent verifies that every CVE in the brief is in `cves_seen.json`, every § 1–4 item has a `covered_items.json` appearance for today, and all state JSON parses cleanly. Drift aborts the commit; the brief stays on disk and the next run rebuilds state from it.
- **Vendored library integrity.** `site/build.py` aborts on SHA-256 mismatch against [`site/assets/vendor/HASHES`](site/assets/vendor/HASHES).
- **Strict CSP** delivered via meta tag — no inline scripts; `script-src` and `connect-src` are restricted to `'self'` and `https://cloud.umami.is` (the analytics tracker, see About → Analytics & privacy); no inline frames or forms.
- **DOMPurify on every brief render** with a pinned, restrictive config (forbidden tags + URI scheme allowlist).
- **Site privacy guarantees:** no cookies set, no fingerprinting, no third-party scripts other than Umami's privacy-by-design tracker (aggregate counts only, no PII).

## Verification policy

Briefs explicitly defend against fake-news patterns common in CTI feeds: ransomware leak-site theatrics, hallucinated CVE numbers, AI-generated security blogspam, vendor PR dressed as research, re-runs of months-old news, sweeping unbacked attribution, and Telegram/X-only sourcing.

See [`docs/verification.md`](docs/verification.md) for the full checklist.

## License / classification

Briefs default to **TLP:CLEAR** unless otherwise stated. The repository contains no IOCs and no operationally sensitive material — only public-source synthesis with links.
