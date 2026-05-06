# Security Newsletter — Daily & Weekly CTI Briefs

> **AI-generated content notice.** Every brief in this repository is produced autonomously by an LLM running as a [Claude Code routine](https://docs.claude.com/en/docs/claude-code/routines) on Anthropic-managed cloud infrastructure. The exact model varies based on the routine's runtime configuration; the model identifies itself in each brief's header. The agent fetches public sources, applies the verification rules in [`docs/verification.md`](docs/verification.md), and writes the Markdown briefs you see in `briefs/`. Every claim in a brief is linked inline to its source. The repository contains the prompts, source list, state files, and policy documents that govern this generation. Verify any operationally critical claim against the linked primary source before acting on it. The briefs are not professional advice and may contain errors.

A daily Cyber Threat Intelligence brief covering cyber threats targeting Switzerland and Europe with a public-sector focus (national/cantonal/federal administration, regulators, critical infrastructure, healthcare, education, public-sector technology suppliers), plus a once-a-week consolidating summary. Audience: Tier 2/3 incident responders, threat hunters, detection engineers. Output: one Markdown file per day under `briefs/` and one per ISO week under `briefs/weekly/`. Output is **always in English**.

The repository is the single source of truth for the workflow: prompts, source list, rolling coverage state, and every brief are version-controlled.

## What this repo contains

```
.
├── prompts/
│   ├── daily-cti-brief.md     # The canonical daily prompt (v2.0)
│   ├── weekly-summary.md      # The weekly summary prompt (v1.0)
│   └── CHANGELOG.md
├── sources/
│   └── sources.json           # Curated, dynamic CTI source list (~75 sources)
├── state/
│   ├── covered_items.json     # Rolling log of items reported and when (full records)
│   └── cves_seen.json         # Flat fast-lookup CVE index (sub-agent dedup)
├── briefs/
│   ├── README.md              # Brief format and conventions
│   ├── YYYY-MM-DD.md          # Daily briefs
│   └── weekly/
│       └── YYYY-Www.md        # Weekly summaries (ISO week)
├── docs/
│   ├── workflow.md            # End-to-end daily & weekly process
│   ├── routine-setup.md       # One-time Claude Code routine setup (GitHub App, branch permissions)
│   └── verification.md        # Fake-news verification policy
└── .gitignore
```

## Operating principles (non-negotiable)

These principles are encoded in the prompts and enforced by quality gates on each run.

1. **Zero LLM knowledge.** Every fact in any brief comes from a source fetched in that run. Nothing from training data.
2. **Inline source links at the point of claim.** No bibliography. The reader can click through from the exact sentence.
3. **No IOCs.** No hashes, IP addresses, attacker-controlled domains/URLs, or rule code. Briefs cover *knowledge* — TTPs, campaigns, actors, vulnerabilities, targeting, sectors, detection concepts. IOC distribution belongs elsewhere (e.g., MISP).
4. **No vanity metrics.** Skip "median dwell time", "breakout time", "X% YoY", "Y new adversaries tracked", and similar vendor-marketing numbers. Operational scoring (CVSS, EPSS, KEV status) is fine.
5. **Always English** (output). Sources may be in German / French / Italian / Polish; the brief translates findings and cites originals by their native title with a brief English gloss.
6. **Two-source verification by default**, with a national-CERT carve-out for HIGH-reliability authorities (NCSC-CH, GovCERT.ch, CERT-EU, BSI, ANSSI, NCSC-UK, NCSC-NL, CISA, CCN-CERT, AGID, CERT.at, CERT-PL) when they are the primary disclosing party for their own jurisdiction. Other single-source items are flagged `[SINGLE-SOURCE]`.
7. **No repetition across runs.** The agent reads the **last 7 days of briefs** plus `state/cves_seen.json` and `state/covered_items.json` before writing. Repeats appear only under "Updates to Prior Coverage" with a material new-information delta.
8. **Yearly / periodic threat reports get one dedicated treatment**, then are not re-summarised. Specific findings can be cross-referenced as context.
9. **Historical-context rule.** For *highly relevant* deep-dive items with prior public reporting older than ~6 months, the brief includes a 3–5-sentence Background paragraph linking 2–3 of the most relevant prior reports — to refresh defenders' memory without bloating routine items.
10. **Long-running campaigns** get ≤1 consolidated UPDATE per week unless something critical changes. The weekly summary is the canonical place for "what happened with X this week".
11. **Recency.** Daily window: 24 h default, 72 h for actively developing items.
12. **No suppression, no padding.** Empty sections state so explicitly.

## Daily routine

A scheduled Claude Code routine fires once per day. It is given exactly one instruction: read [`prompts/daily-cti-brief.md`](prompts/daily-cti-brief.md) and execute it.

> **One-time setup** required for the routine to publish back to this repo: install the Claude GitHub App on the repo, and (optionally) enable **Allow unrestricted branch pushes** in the routine's permissions for direct-to-`main` publishing. Full instructions: [`docs/routine-setup.md`](docs/routine-setup.md).

The agent walks through:

1. **Phase 0 — Preflight**: load source list, last 7 days of briefs, state files.
2. **Phase 1 — Parallel research**: spawn **four** sub-agents in parallel with cleanly partitioned source categories — (1) Active Threats & Trending Vulnerabilities, (2) Switzerland, Europe & Public Sector, (3) Research & Investigative Reporting, (4) Incidents & Disclosures. No token cap. Sub-agents return flexible Markdown with required fields. Each spawn prompt opens with a defensive-intent statement.
3. **Phase 2 — Verification**: re-fetch primaries, enforce two-source / national-CERT rule, drop already-covered items, surface contradictions.
4. **Phase 3 — Deep-dive selection**: at most 1–2 items.
5. **Phase 4 — Compose**: write `briefs/YYYY-MM-DD.md` with sections 0–9.
6. **Phase 5 — State update**: append to `covered_items.json` and `cves_seen.json`; bump `last_successful_fetch` on used sources; propose new sources as `candidate`.
7. **Phase 6 — Commit & push to `origin/main`** — every brief is published the moment it is generated. No review branch, no staging gate. Briefs are already AI-content-noticed and source-linked.

Full walkthrough: [`docs/workflow.md`](docs/workflow.md).

## Weekly routine

A separate scheduled routine fires once a week (Sunday recommended). Reads [`prompts/weekly-summary.md`](prompts/weekly-summary.md). Output: `briefs/weekly/YYYY-Www.md`.

The weekly summary:

1. Reads every daily brief from the past 7 days.
2. Builds a top-stories list, multi-day campaign roll-ups, full CVE roll-up table, sector/victim patterns, and major-breaches recap.
3. Spawns three horizon sub-agents (long-horizon campaigns, yearly/periodic reports, policy/regulatory) for material the daily briefs did not cover.
4. Distils any yearly threat report newly published.
5. Produces a "looking ahead" list of items in motion likely to develop next week.

Unlike the daily brief, the weekly summary **may repeat material** from the dailies — that is its consolidating purpose. Repetition is allowed; padding is not.

## Maintaining the source list and the CVE index — autonomous

The repository is the agent's working memory. Both `sources/sources.json` and `state/cves_seen.json` are maintained by the routine on each run with **no human review gate**. Every change appears in the run's git diff and commit message; that's the audit trail. The git log on these files is the curation history.

### Source lifecycle (all transitions autonomous)

- **Discovery → candidate.** When a sub-agent encounters a new high-quality publisher (primary source, editorial track record, in-scope) during research, it's added to `sources.json` with `status: "candidate"` and a `notes: "discovered YYYY-MM-DD via {source-id}"` line.
- **Candidate → active.** A candidate is auto-promoted to `active` after **3 distinct runs** in which the source was successfully fetched *and* contributed content to a brief (i.e., its `last_covered_in_brief` was bumped on three different days). On promotion, append a dated note recording the auto-promotion.
- **Active → demoted.** After **3 consecutive failed fetches** with no working canonical-URL probe (which is attempted before demotion — many publishers move their feed and a better URL exists at the same domain), the source's `reliability` drops one tier, `status` becomes `demoted`, and a dated `notes` line records the failure mode. Demoted sources are excluded from regular sub-agent rotation but kept in the file.
- **Demoted → active (recovery).** A demoted source returns to `active` only when the agent finds a working canonical URL during research and the recovered URL contributes content to a brief. Update `url`, set `status: active`, reset `consecutive_failures` to 0, add a dated note explaining the recovery.
- **URL updates in place.** Any time a better canonical URL is found for an active source (publisher CMS migration, restructured advisories index, more specific feed), update `url` and append a dated note. The source `id` stays stable so historical references in `state/covered_items.json` remain valid.
- **Reliability tier-down without full demotion.** Sources that return navigation-only pages (no dated content) for **3+ consecutive attempted runs** despite drill-down attempts get a one-tier reliability drop and a dated `notes` flag, while staying `active`. They keep getting fetched but the brief weighs their output less when corroboration matters.

**No source deletion.** Demoted and tier-downgraded sources stay in the file as historical record — the cost is a single extra entry, the benefit is a durable audit trail of why each source left or rejoined rotation. If the file ever grows unwieldy, that's a job for a separate cleanup commit, not a routine run.

### CVE index — autonomous

The agent appends new CVE IDs, bumps `last_seen` on subsequent appearances, updates `title` or `primary_source_url` when better information emerges, and **removes** entries that turn out to be invalid (e.g., a CVE ID that does not resolve on NVD/MITRE — a hallucinated identifier slipped past verification on a previous run). Removals are documented in the run's commit body so the audit trail is preserved in git history.

The current list (~75 sources) covers: Swiss/EU national CERTs (NCSC-CH, GovCERT.ch, CERT-EU, ENISA, BSI, ANSSI, NCSC-UK, NCSC-NL, CERT.at, GovCERT.at, CERT-PL, AGID, CCN-CERT); Swiss security firms (Compass Security, scip AG, OneConsult, InfoGuard, Kudelski Security, PRODAFT); top-tier vendor TI (Mandiant/GTIG, Microsoft, CrowdStrike, Unit 42, Cisco Talos, Volexity, ESET, Kaspersky Securelist, Trend Micro, Check Point, Sophos X-Ops, Secureworks, Recorded Future Insikt, Sekoia, Group-IB, Elastic Security Labs, Huntress, Red Canary, The DFIR Report, Sygnia, Truesec, NCC Group, WithSecure Labs, IBM X-Force, Akamai, Cloudflare Cloudforce One, Trustwave SpiderLabs, Tenable, Rapid7); vulnerability research (CISA KEV, watchTowr Labs, Project Zero, ZDI, VulnCheck, GreyNoise, Shadowserver); OT/ICS (Dragos, SANS ICS); journalism (Krebs, Schneier, Heise Security, Inside IT, Le Monde Informatique, Malwarebytes, The Record, CyberScoop, BleepingComputer, SecurityWeek, Security Affairs, Help Net Security, SANS ISC, Dark Reading); breach trackers (SEC EDGAR 8-K, UK ICO, CNIL FR, EDPB); civil-society research (Citizen Lab); discovery (r/netsec).

## Verification policy

Briefs explicitly defend against fake-news patterns common in CTI feeds: ransomware leak-site theatrics, hallucinated CVE numbers, AI-generated security blogspam, vendor PR dressed as research, re-runs of months-old news, sweeping unbacked attribution, and Telegram/X-only sourcing.

See [`docs/verification.md`](docs/verification.md) for the full checklist.

## License / classification

Briefs default to **TLP:CLEAR** unless otherwise stated. The repository contains no IOCs and no operationally sensitive material — only public-source synthesis with links.
