# Security Newsletter — Daily & Weekly CTI Briefs

> **AI-generated content notice.** Every brief in this repository is produced autonomously by an LLM (Claude Opus 4.7, model ID `claude-opus-4-7`) running scheduled Claude Code routines. The agent fetches public sources, applies the verification rules in [`docs/verification.md`](docs/verification.md), and writes the Markdown briefs you see in `briefs/`. Every claim in a brief is linked inline to its source. The repository contains the prompts, source list, state files, and policy documents that govern this generation. Verify any operationally critical claim against the linked primary source before acting on it. The briefs are not professional advice and may contain errors.

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

The agent walks through:

1. **Phase 0 — Preflight**: load source list, last 7 days of briefs, state files.
2. **Phase 1 — Parallel research**: spawn **seven** sub-agents in parallel — Active & Breaking, CH/EU, Government & Public Sector, Trending Vulnerabilities, Vendor & Independent Research, Quality News, **Major Breaches**. No token cap on sub-agents. Sub-agents return flexible Markdown with required fields.
3. **Phase 2 — Verification**: re-fetch primaries, enforce two-source / national-CERT rule, drop already-covered items, surface contradictions.
4. **Phase 3 — Deep-dive selection**: at most 1–2 items.
5. **Phase 4 — Compose**: write `briefs/YYYY-MM-DD.md` with sections 0–9.
6. **Phase 5 — State update**: append to `covered_items.json` and `cves_seen.json`; bump `last_successful_fetch` on used sources; propose new sources as `candidate`.
7. **Phase 6 — Commit**.

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

## Maintaining the source list

`sources/sources.json` is intentionally append-mostly. The agent may:
- Increment `last_successful_fetch` for sources used today.
- Demote a source's `reliability` after three consecutive failed/empty fetches (`status: "demoted"`).
- Propose new sources discovered during research as `status: "candidate"`.

The agent **must not** remove sources or auto-promote candidates. Humans review demotions and candidate additions periodically (`git log -- sources/sources.json`).

The current list (~75 sources) covers: Swiss/EU national CERTs (NCSC-CH, GovCERT.ch, CERT-EU, ENISA, BSI, ANSSI, NCSC-UK, NCSC-NL, CERT.at, GovCERT.at, CERT-PL, AGID, CCN-CERT); Swiss security firms (Compass Security, scip AG, OneConsult, InfoGuard, Kudelski Security, PRODAFT); top-tier vendor TI (Mandiant/GTIG, Microsoft, CrowdStrike, Unit 42, Cisco Talos, Volexity, ESET, Kaspersky Securelist, Trend Micro, Check Point, Sophos X-Ops, Secureworks, Recorded Future Insikt, Sekoia, Group-IB, Elastic Security Labs, Huntress, Red Canary, The DFIR Report, Sygnia, Truesec, NCC Group, WithSecure Labs, IBM X-Force, Akamai, Cloudflare Cloudforce One, Trustwave SpiderLabs, Tenable, Rapid7); vulnerability research (CISA KEV, watchTowr Labs, Project Zero, ZDI, VulnCheck, GreyNoise, Shadowserver); OT/ICS (Dragos, SANS ICS); journalism (Krebs, Schneier, Heise Security, Inside IT, Le Monde Informatique, Malwarebytes, The Record, CyberScoop, BleepingComputer, SecurityWeek, Security Affairs, Help Net Security, SANS ISC, Dark Reading); breach trackers (SEC EDGAR 8-K, UK ICO, CNIL FR, EDPB); civil-society research (Citizen Lab); discovery (r/netsec).

## Verification policy

Briefs explicitly defend against fake-news patterns common in CTI feeds: ransomware leak-site theatrics, hallucinated CVE numbers, AI-generated security blogspam, vendor PR dressed as research, re-runs of months-old news, sweeping unbacked attribution, and Telegram/X-only sourcing.

See [`docs/verification.md`](docs/verification.md) for the full checklist.

## License / classification

Briefs default to **TLP:CLEAR** unless otherwise stated. The repository contains no IOCs and no operationally sensitive material — only public-source synthesis with links.
