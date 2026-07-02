# Prompt CHANGELOG

Tracks substantive changes to `prompts/daily-cti-brief.md` and `prompts/weekly-summary.md`.

---

## 2.69 — 2026-07-02 (org-neutral prompt prose; national-CERT carve-out list and policy watch move into the org profile)

### Why

The deployment is organization-parameterizable via `config/org-profile.yaml`, but a body of "Swiss / EU public-sector" phrasing, the hardcoded national-CERT single-source carve-out list, and the weekly's Swiss/EU regulator enumeration lived as static prose OUTSIDE the ORG-PROFILE managed blocks. A downstream fork changing the org profile still inherited the Swiss lens in ranking rules, deep-dive criteria, section-ordering guidance, empty-section boilerplate, the verifier's F7 drop rule, and the W2 policy sweep — and any local rewrite of that prose would conflict with upstream prompt improvements on every merge. This release makes the org profile the *only* place the lens lives, so forks customize config and merge prompts cleanly. Companion change (no prompt semantics): the site build gains `config/branding.yaml` + `site/branding/` for the same decoupling on the visual side — see `docs/customization.md`.

### What changed

- **Both master prompts** (v2.69, lockstep): every org-lens phrase outside the managed blocks now references the profile instead of naming it — "Swiss/EU public-sector" → "the profiled constituency / the profiled organization's SOC (§ Organization profile)", "CH/EU nexus" ranking → "home-region/coverage-focus nexus", § 1 ordering, deep-dive criteria 1–2, less-is-more criteria (a)/(c), empty-section boilerplate, PD-13's jurisdiction rationale (now states the profiled audience is not a US-FCEB agency), the S2 spawn-table label, and both editorial-quality gates. Semantics for the default Swiss-federal-SOC deployment are unchanged — the managed blocks already carry that lens.
- **Weekly W2 / § 9**: the hardcoded regulator enumeration (NCSC.ch, FINMA, NIS2 / DORA / CRA, OFCOM / BAKOM, Council of Europe, sanctions actions) moved to a new `policy_watch` list in `config/org-profile.yaml`, rendered as a new `org-policy-watch` managed block under W2; § 9 references that watch list. Omitting the key keeps the previous list verbatim.
- **National-CERT carve-out list** (NCSC-CH … CERT-PL) moved to a new `national_certs` list in `config/org-profile.yaml`, rendered as a new `org-certs` managed block into `.claude/agents/cti-research.md` and `prompts/verification.md` (now a compose target), and appended to the `verify-context` block both verifier agents receive. Omitting the key keeps the previous list; an explicit `[]` disables the carve-out (two-source everywhere).
- **Research findings schema**: example field names `ch_eu_nexus` / `public_sector_nexus` renamed to org-neutral `region_nexus` / `primary_sector_nexus`; the compact-summary labels follow ("Region nexus / Primary-sector nexus").
- **Both verifier agents** (lockstep, byte-identical bodies): the coverage-shape check and the F7 drop rule now phrase the lens via § Organization context; the redundant "(default: Swiss / EU public-sector)" parenthetical dropped.
- **`prompts/brief-template.md`**: template placeholders for the sector-pattern and synthesis sections now phrase the lens via the org profile.
- **`tools/compose_prompts.py`**: renders the two new blocks; validates the two new optional keys (absent → upstream defaults, `[]` → feature disabled); `prompts/verification.md` added to TARGETS; selftest extended.

### What stays

- The default deployment's lens is untouched: the composed blocks still say Swiss federal SOC · public-sector · switzerland · Switzerland and Europe, and rendered brief content is unaffected — this is prose refactoring plus config extraction, not an editorial-policy change.
- The daily/weekly lens divergence (operational today's-signal vs long-horizon) is untouched; the two prompts moved in lockstep on shared machinery only.
- All hard invariants: two-source verification + carve-out mechanics (now config-listed, same default trust bar), no IOCs, AI-content notice, English output, publishing chain, self-check gate, verification loop, metadata footers, memory commits.
- Worked examples that illustrate formats (ISAC-CH closed-source drop fixtures, discovery-trace samples) keep their Swiss flavor — they document format, not lens.
- `tools/check_brief.py` heuristics keyed to `switzerland`/`europe` region tags (tldr-body-drift) are unchanged — they no-op harmlessly on deployments with other home regions (documented in `docs/customization.md`).

## 2.68 — 2026-07-02 (version history lives only in this file; stale-reference and contradiction sweep; prompt-version gate implemented)

### Why

Operator request: version-history annotations ("v2.53 …") had leaked out of this CHANGELOG into the master prompts, the agent definitions, the policy docs, CLAUDE.md, config comments, tooling output strings and code comments. Those annotations tell a future reader *when* a rule appeared — which is this file's job, not the prompt's — and they accumulate as noise the agents re-read on every run. The only version a prompt should carry is its own banner. The sweep that removed them also surfaced real contradictions that had accumulated between files (stale wall-clock budgets, wrong section numbers, stale counts, an off-by-one phase-step reference), plus one documented safety net that had never actually been implemented.

### What changed

- **Every vN.M annotation removed outside `prompts/CHANGELOG.md`**: both master prompts, all three agent definitions, `prompts/verification.md`, `prompts/brief-template.md`, `prompts/check-brief-fixes.md`, `CLAUDE.md`, `config/org-profile.yaml`, `intel/README.md`, `README.md`, `docs/*`, and the user-visible strings + comments of `tools/check_brief.py` / `site/build.py` / `tools/compose_prompts.py`. The two prompt banners (`> **Prompt version:** vN.M`) are now the only version markers outside this file. Where an annotation carried operational rationale (e.g. "the 10-min soft cap is removed"), the rationale was kept and only the history framing dropped.
- **Contradictions fixed (daily + weekly in lockstep):**
  - **Sub-agent budget** — every stray "10-min" reference (daily Execution environment, daily Phase 2 trigger, both prompts' `returned: false` population rule, weekly Execution environment, CLAUDE.md hard rule) now states the one true 30-min hard cap.
  - **`work/<run-id>/`** was still described as "gitignored" in four places despite being version-controlled and committed with the brief — corrected everywhere.
  - **Section numbers** — daily: "§ 3 Updates sits above § 4 Deep Dive" → "§ 4 … above § 5"; weekly: four references routed Verification-Notes content to "§ 10" (which is Looking ahead) instead of § 11; `prompts/verification.md` still used a pre-8-section layout ("§ 8 Verification Notes", "§ 5 Updates", "§ 2" for CH/EU items); `check_brief.py`'s docstring and `check-brief-fixes.md` pointed drops at "§ 8"; the verifier's F12 instruction said "§ 7 / § 10". All now name the correct sections (or the section name plus per-cadence numbers).
  - **Stale schema comments** — `findings[].code` "F1..F12" (daily) / "F1..F15" (weekly) → F1..F16; "one entry per iteration, up to 3" → up to 5; weekly "11-section file" → 12; CLAUDE.md parity list "F1–F15 finding set" → F1–F16.
  - **Stale references in the daily Phase 1 spawn contract** — `window_hours` "from Phase 0 step 6" → step 7; "generated by Phase 0 step 7a" → step 1 (twice); source-list size "~80" → ~150.
  - **Compose-after-return gate** now includes S5 in the `.ended_at` wait loop when Phase 0 spawned it (previously only S1–S4 were gated).
- **Main-agent self-identification aligned with the sub-agents**: both master prompts now read `CLAUDE_FRIENDLY_NAME` / `CLAUDE_MODEL_ID` as the authoritative source (the agent definitions already did), keeping reason-about-identity as the unset-env-var fallback. Removes the drift where only sub-agents used the env vars while the main agent was told to reason cold.
- **`prompt-version` gate implemented in `tools/check_brief.py`**: CLAUDE.md documented a cross-check of the brief's `**Prompt:** vN.M` badge against this file's most recent heading, but the check did not exist. It now does — FAIL when the brief under check is uncommitted (the pre-commit gate, the moment the mismatch must be fixed), WARN when the brief is already committed clean (the changelog legitimately moved on after publication; verified against the 2026-07-01/02 briefs, whose v2.64 badge trails the three same-day bumps).
- **Daily quality-gates checklist got its missing `## Quality gates (self-check)` heading** — it previously floated unlabelled at the end of Phase 7 (the weekly already had the heading).
- Template harmonization: `brief-template.md` TL;DR bullet guidance now matches the daily prompt (3–6 bullets).

### What stays

No behavioural rule was added, removed, or weakened: every gate, cap, hard invariant, schema and lens is unchanged in substance — this release removes history annotations, fixes wrong cross-references, and implements an already-documented gate. The daily/weekly lens divergence is untouched. The ORG-PROFILE managed blocks are untouched (`compose_prompts.py --check` in-sync on all five files). Both verifier definitions were regenerated in lockstep and remain byte-identical below the alt header note. The two dated incident references that justify standing rules (the 2026-05-15 fabrication/inversion traces, the W21/W22 duplicate-weekly misfires) stay in the prompts as operational rationale — only their changelog-version pointers were dropped.

## 2.67 — 2026-07-02 (methodology-driven research agents; tiered source allocation with a daily essential-coverage guarantee)

### Why

Operator request, third round: stop telling the research agents *which sources to query* — hardcoded publisher names in the agent definition (the v2.66 playbooks, the per-host recipe tables, the RSS quick-reference) duplicate `sources/sources.json` and go stale the moment the list evolves. Instead: teach every agent the *methodology* of world-class CTI (dig past news and alarming catches to primary evidence, produce actionable results), make the curated source list the single collection plan the agents know how to read and keep up to date, and guarantee that the essential providers (national CERTs, NCSC, CISA, ENISA, …) are queried every single day while the remaining providers rotate in a balanced way so nothing is missed and no run floods.

### What changed

- **`.claude/agents/cti-research.md` — new § Intelligence methodology:** the five-stage cycle written as tradecraft — direction (org requirement decides, not curiosity), collection (evidence not headlines; never stop at the first report; an alarming headline is a hypothesis; absences are intelligence), processing (fact / claim / inference buckets at collection time — the upstream half of the anti-hallucination chain), analysis (corroboration = independence not count; competing-hypotheses-in-miniature for attribution; delta-vs-repeat contextualization; org-specific severity weighing), dissemination (actionability as the exit criterion), plus craft habits (References-section pivots, disclosing-party preference, contradiction handling, recycled-news trap, honest dead-end logging).
- **Source knowledge moved out of the prompt into the list:** the per-host recipe table, publisher RSS quick-reference, Microsoft-specific sections, and named-source playbooks are GONE from the agent definition. Replaced by **§ Working the source list — the record is the recipe** (how to read `tier` / `fetch_method` / `notes`-borne dated recipes / `reliability`, slice discipline, drift-fixing duty) and **§ Fetch tooling reference** (capability catalog of `tools/fetch_source.py` subcommands + the seven cross-host empirical rules, publisher-agnostic). **§ Domain collection missions** replace the v2.66 playbooks: per-domain intelligence *questions* and collection shape, naming zero publishers — sources come exclusively from the spawn slice.
- **Tiered sources (`sources/sources.json`):** new top-level `tiers` vocabulary + required per-source `tier` field. 14 records tagged `essential` (NCSC-CH ×3, CERT-EU, ENISA, BSI, ANSSI/CERT-FR, NCSC-UK, NCSC-NL, CERT-PL, CERT-AT, CISA KEV / advisories / directives); everything else `standard`. `sources_changed[]` vocabulary gained `tier`; candidate shape carries `tier: standard` by default (essential is an operator-grade decision).
- **Daily + weekly (lockstep): tier-aware per-agent allocation** replaces the flat category slice — essential floor (ALL active essential records, category-matched, every daily run, no exceptions) + staleness rotation for standard records (oldest `last_successful_fetch` first, gap-flagged records promoted, ~10–14 per agent) so every standard source is attempted at least every ~7 runs. Spawn element 4 now passes full per-record metadata incl. tier and the newest recipe note; § 7 gained a parseable `Essential-coverage: missed=…` disclosure (omitted on full coverage).
- **`tools/check_brief.py`:** `sources-schema` validates the `tier` field/vocabulary; new **`essential-coverage`** check (WARN — publish never blocks) verifies every active essential source appears in the union of today's `sub_agents[*].sources_attempted`. Run against the 2026-07-02 brief it immediately surfaced 6 missed essential authorities — the exact defect class this release closes.

### What stays

Lens divergence, hard invariants, and the whole v2.65/v2.66 machinery unchanged. The bridge tool itself, the outbound-links template, the discovery-trace contract, and the anti-classifier main-agent-no-fetch invariant are untouched — only *where source knowledge lives* moved (into `sources/sources.json`, whose v2.62 metadata-drift duty already keeps recipes current). The `fetch_gaps_in_window` rotation signal is still consumed — now as a promotion input to the staleness ranking rather than a parallel list.

## 2.66 — 2026-07-02 (closed-source intel intake; private deployment; alert-fatigue calibration; per-domain research playbooks)

### Why

Operator request, second round: (a) a **daily drop folder for closed-source intelligence** — an operator-owned script downloads provider reports / ISAC bulletins into a dated folder, the routine ingests them with correctly *referenced, never linked* citations and high credibility, and the machinery costs nothing on the (normal) days the folder is empty; (b) support **private deployments** — the whole stack, including the static site, hostable org-internally (private repo + a web server that pulls, builds and serves on a schedule), documented; (c) another optimization pass with three focuses: the **false-positive/false-negative balance** ("not knowing about a relevant threat is bad, but flooding until the brief isn't taken seriously is also very bad"), **clear per-domain instructions that hold up on less capable research-agent models**, and keeping everything traceable to sources with no hallucination.

### What changed

- **New `intel/` drop-folder contract** ([`intel/README.md`](../intel/README.md)): `intel/<YYYY-MM-DD>/` folders with front-mattered text documents (`title`, `provider`, `date`, `tlp`, `ref`); fed by the operator's script via the existing auto-merge chain (`claude/intel-drop-<date>` branch) or a direct operator push. **Daily + weekly (lockstep):** Phase 0 gained an intel-detection step; Phase 1/2 gained a **conditional intake sub-agent (S5 daily / W3 weekly)** spawned only when in-window intel files exist — it `Read`s the documents in an isolated context (classifier-trip discipline preserved), extracts items to the standard findings YAML with `closed_source` source records + REQUIRED verbatim evidence quotes, treats the documents as HIGH-reliability primaries (single-document sourcing acceptable, `[CLOSED-SOURCE]` heading marker), and attempts public corroboration for every item. New **`Closed-source:` footer field** — `"Title" (Provider, YYYY-MM-DD, TLP:X, ref: ID)`, unlinked by design — parsed and validated by `site/build.py` + `tools/check_brief.py` (new fallback-parser support, footer Source requirement relaxed to *linked source OR closed-source citation*, unlinked rendering, smoke tests). § 7 / § 11 gained a parseable `Closed-source intake:` line.
- **TLP gate (hard invariant — daily #18 / weekly #17):** on a `deployment.visibility: public` profile, closed-source content above TLP:CLEAR never reaches the brief (not cited, not quoted, not paraphrased-in-detail); above-CLEAR documents are leads to public sources only, counted via the findings YAML `tlp_restricted_leads` block. `check_brief.py` `closed-source-tlp` FAILs the commit; `closed-source-ref` / `closed-source-flag` WARN on citations not traceable to a drop file and on missing `[CLOSED-SOURCE]` markers. The verifier `Read`s every referenced drop file: claims → F3/F4, missing file → F1-equivalent, TLP violation → F7, missing marker → F12.
- **Private deployment** ([`docs/private-deployment.md`](../docs/private-deployment.md)): new `deployment:` section in `config/org-profile.yaml` (`visibility: public|private`, `site_url`), composed into the org-data and verifier context blocks; `compose_prompts.py` gained `--get dotted.key`; both prompts' publish-verification phase now reads `deployment.site_url` (empty ⇒ skip the site poll and report the new `publish: ok (main — site polling disabled)` outcome — the internal web server owns the last mile via a documented scheduled pull → `site/build.py` → static-serve loop; systemd timer + nginx examples in the doc).
- **Calibration (daily PD-11 / weekly PD-13, in lockstep):** explicit false-negative-vs-false-positive operating point — inclusion decided by org-relevance, borderline test ("would a Tier 2/3 responder at this organization act differently in the next 7 days?"), and a two-sided audit trail: `borderline-drop:` lines in § 7 / § 11 for near-threshold drops, one-clause org-relevance statements for near-threshold includes. Research agents gained the matching rule plus `borderline: true` / `borderline_reason:` findings-YAML fields so threshold calls escalate to the main agent instead of being silently made in isolation.
- **Per-domain playbooks in `cti-research.md`** (new § Domain playbooks): concrete ordered checklists per domain — S1 (KEV → EUVD → MSRC-on-Patch-Tuesday → slice → per-CVE PSIRT pivot → watchlist sweep → named search shapes), S2 (NCSC-CH → CERT-EU/FR/BSI → regional press → sector sweeps in local languages), S3 (lab feeds → landing-scrapes → annual-report flagging), S4 (EDGAR 8-K → ICO → victim-statement-first discipline → supplier sweep), W1/W2, S5/W3 — written as floors so the same baseline executes even on less capable models.
- **Quality gates** extended in both prompts (intake handling, calibration audit trail); run-log check validates the optional S5/W3 record shape when present.

### What stays

Lens divergence and all prior hard invariants untouched; the closed-source and calibration machinery is shared and mirrored per the parity rule. The footer grammar is *extended* (new optional `Closed-source:` field), not changed — every existing brief parses identically; items with linked sources behave exactly as before. Empty/absent `intel/` (the normal state) and the default `deployment` section (`public`, ctipilot.ch) reproduce v2.65 behaviour bit-for-bit. Aggregator-avoidance, trace-to-primary, Evidence escalation, compose-from-findings, and the verification loop are unchanged — the intake path plugs into them rather than bypassing them.

## 2.65 — 2026-07-02 (parameterizable organization profile: watchlists + org-triage; compose-into-prompts pipeline; anti-embellishment composition rules)

### Why

Operator request: make the deployment organization-configurable instead of hard-wired to the Swiss public-sector default — (a) a list of estate **products** (e.g. Windows Server, Windows clients) and a list of **suppliers / companies** the research agents specifically sweep for relevant cyber information; (b) a free description of the **organisation, sector and region** (not just "public sector in Switzerland"); (c) an org-specific **vulnerability-categorization scheme** so briefs immediately carry the organization's own triage rating on CVE items. All of it parameterized in one config file and composed into the prompt files by script on push via GitHub Actions, with the current values preserved as defaults and hard guarantees that the agents do not overshoot — general-situation coverage stays primary.

Independently, run-log telemetry across v2.53–v2.64 (62 runs) showed the verification loop burning 4–5 iterations on most runs, dominated by **F3 claim-not-supported (73)** and **F4 hallucinated-fact (59)** findings — composition-time embellishment on top of sound research. The `Evidence:` rollout (v2.53) stayed permissive and never escalated; the weekly's sub-agent return-format section still described the pre-v2.53 free-form Markdown contract (drift the parity rule should have caught).

### What changed

- **New `config/org-profile.yaml`** — single parameterization point: organization (name, short name, sector, additional sectors, region focus, home region, description, audience), watchlists (products with vendor/exposure/criticality, suppliers with relationship/criticality, standing interests), vulnerability-triage scheme (categories with id/name/criteria/response + default). Defaults reproduce the pre-v2.65 Swiss-federal-SOC text in meaning; watchlists and triage ship empty/disabled so default output is unchanged.
- **New `tools/compose_prompts.py`** (stdlib-only, `--check/--write/--dump/--selftest`) renders the profile into `ORG-PROFILE` managed marker blocks inside **five** files: both master prompts (mission + audience paragraph, new § Organization profile & watchlists data block), `.claude/agents/cti-research.md` (mission, audience, watchlist values), and both verifier definitions (§ Organization context — so relevance check 5 judges against the *configured* org, not a hardcoded "Swiss federal SOC"). **New `.github/workflows/compose-profile.yml`** (shell-only): auto-composes on push to operator branches, check-only + fail-loud on `main` and `claude/**` (auto-committing on claude/** would race auto-merge). `check_brief.py` gained a `profile-sync` WARN.
- **Daily + weekly (shared machinery, in lockstep): § Organization profile & watchlists** — watchlist policy (match = relevance boost only, every other gate unchanged; mandatory batched sweep with explicit ownership — daily S1 products / S4 suppliers / S2 sector-lens, weekly W1 consolidated status sweep; hits carry the new `watchlist` taxonomy tag; parseable `Watchlist:` line in § 7 / § 11) and org-triage policy (bold `**Org triage (<short_name>):**` body line immediately before the footer on CVE-typed daily § 0/§ 2/§ 5 and weekly § 3 items when a scheme is configured; derived strictly from cited facts). **Anti-overshoot hardened as daily invariant #17 / weekly #16**: watchlist items ≤ ~⅓ of core sections, general critical items always win, no padding, no gate bypass. Spawn contracts gained element 9 (`watchlist_duty`); the S1/S2/S4 domain-table rows and the W1 domain list were updated accordingly (S2 renamed "Home region & sector"; telemetry showed the four-way split itself is well balanced — 3.6–5.5 items, ~11 min per agent — so ownership was refined rather than restructured).
- **Daily + weekly: § Compose strictly from the findings files (anti-embellishment)** — every factual claim must trace to the sub-agent findings YAMLs, a gap-window daily (weekly), or a main-agent spot-check; tighten-never-escalate phrasing rule; counts/superlatives only from `evidence`/`summary`. **`Evidence:` escalated from permissive to required** on the daily § 0 callout + exploited-status § 1/§ 2 items and weekly § 1 + exploited-status § 3 items (`check_brief.py` `evidence-presence` WARN; main agent clears it pre-verifier). Expected effect: F3/F4 down, verification iterations down from the current 4–5 mode.
- **`.claude/agents/cti-research.md`**: new § Organization watchlist duties (duty semantics per spawn assignment, batched-sweep shape, never-pad rule); findings YAML gained per-item `watchlist:` field + top-level `watchlist_sweep:` block + a `**Watchlist sweep:**` compact-summary line; the WebFetch outbound-links template gained a **"Load-bearing quotes"** item (verbatim sentences for Evidence binding).
- **Both verifiers (bodies re-synchronized byte-identically — they had drifted in 5 paragraphs)**: new § Organization context (generated); relevance check 5 reworded to judge against the composed profile incl. watchlist-tag semantics; **new F16 `org-triage`** (editorial): missing/unknown/criteria-inconsistent triage line, or triage line / `watchlist` tag present with no scheme configured. Verdict buckets and both master prompts' remediation tables updated (F1–F16). The alt variant is now mechanically regenerated from the canonical body (documented boundary in its header note).
- **Weekly parity fix**: the weekly's "Sub-agent return format" still described the legacy free-form Markdown return; it now references the v2.53 findings-on-disk contract that `cti-research.md` (and the daily) already mandated.
- **v2.64 leftover cleanup**: the daily prompt still referenced the "§ 2 secondary aggregation table" in three places and `cti-research.md` still told S1 to return a Markdown CVE table — all contradicting v2.64's table removal. The references now describe `cve_table:` as structured YAML input (footers + state updates), never a rendered table.
- **`site/taxonomy.yaml`**: new `watchlist` theme tag. **`prompts/brief-template.md`**: Org-triage line + `Evidence:` examples on the daily § 2 and weekly § 3 fragments. **`tools/check_brief.py`**: new `profile-sync`, `evidence-presence`, `org-triage` checks (all WARN-only — publish is never blocked on profile machinery).

### What stays

The intelligence lens and output structure stay divergent (daily operational-today vs. weekly horizon) — the profile parameterizes *who the reader is*, not the lens split. All hard invariants untouched: AI-content notice, no IOCs, two-source + national-CERT carve-out, English output, feature-branch-only publishing, self-check gate (Phase 5.5 / 4.5), verification loop (Phase 5.7 / 4.7, 5-iteration cap, model rotation, early-exit rules), per-item taxonomy footers, memory commits, main-agent-no-fetch invariant. The metadata-footer grammar is unchanged (the org-triage line is a body line; `Evidence:` was already parsed since v2.53/v2.58) — `site/build.py` needed no changes. Default-profile output is byte-compatible with v2.64 behaviour: empty watchlists and no triage scheme mean no new lines, no new tags, and the same mission/audience text.

## 2.64 — 2026-06-20 (drop Wayback fallback repo-wide; remove the CVE Summary Table from briefs; RSS fetch-waste demotions)

### Why

Operator review: (1) the Wayback Machine fallback is no longer wanted — fetching publisher content from web.archive.org is out; (2) the per-section **CVE Summary Table** was a recurring source of transcription errors (patched-version / KEV / SAP-note cells contradicting the body — see the v2.48–v2.63 verification logs) and duplicated data the per-item footers already carry; (3) RSS sources whose feed is a teaser AND whose articles can't be drilled are a waste of tool calls — fetching them can't produce citable content.

### What changed

- **Wayback removed everywhere (T3):** the `wayback` subcommand + all of its code is gone from `tools/fetch_source.py`; the cti-research agent's per-host recipe table now routes Cloudflare-blocked hosts to a feed path or a WebSearch corroboration instead of Wayback; `fetch_failures` guidance, docs, and `sources/sources.json` notes no longer mention Wayback. Blocked hosts (group-ib, ccn-cert-es, coe.int, seppmail) are surfaced as coverage gaps with WebSearch as the only fallback.
- **CVE Summary Table removed from future briefs (T4):** dropped from `prompts/brief-template.md` (daily § 2 + weekly § 3), the daily S1 sub-agent return spec, and the weekly § 3 instruction. Per-CVE H3 entries with their taxonomy footers (CVE / CVSS / Vector / Auth / Status) remain — the table is gone. Existing briefs keep their tables; this is forward-only.
- **RSS fetch-waste demotions (T2):** audited every RSS/feedburner source for article readability. `heise-sec` (120-char teaser feed + TollBit-paywalled articles) and `csirt-acn-it` (no parseable feed + React-SPA advisory body) demoted as fetch-waste; `databreaches-net` confirmed full-content feed (~1.4 KB bodies) and kept.
- **`sources/sources.json`:** deleted the duplicate `sansec` entry entirely (kept active `sansec-research`).
- **Ops dashboard / source_health (no prompt-behaviour change):** model-name normalisation, Health-section consolidation, bridge-failure floating, and removal of the fetch-failure chart from /sources/ — see CLAUDE.md / build.py.

### What stays

Lens divergence and all hard invariants untouched. The per-item taxonomy footer (which carries the CVE metadata the table used to duplicate) is unchanged and still mandatory. The bridge, RSS, and structured-endpoint fetch recipes are unchanged except for the Wayback removal.

## 2.63 — 2026-06-20 (every-run source-accessibility health check + recipe-aware probe; Ops dashboard floats only unsolved source problems)

### Why

v2.62 surfaced *which sources a run changed*, but nothing periodically answered "which sources are now unreachable and need a dedicated bridge fetcher or demotion?" — `tools/source_health.py` only ran weekly, only HEAD-probed `active` sources, and only checked the raw `url` (not the actual fetch recipe), so it both missed broken `api`/`bridge` recipes and false-flagged sources whose homepage is hostile but whose feed works. The operator asked for: the accessibility probe moved into the global Health view; a list that floats ONLY unsolved problems (needs-bridge / needs-demote), never already-demoted or already-bridged sources; verification that the bridge recipes still work; every source checked; and the check run at the end of every routine.

### What changed

- **Daily + weekly (shared machinery, in lockstep):** the routine now runs `python3 tools/source_health.py` at the END of every run (new § `state/source_health.json` in Phase 5 / Phase 4) and commits the snapshot, so every source is probed on every fire — not just on the weekly cron. The prompt directs the agent to act on the printed `UNSOLVED` list the same run (add a bridge recipe for `needs-bridge`, fix-or-demote for `needs-demote`) and record the edit in `sources_changed[]`.
- **`tools/source_health.py` (v2.63):** probes EVERY source (not just active); probes via the *actual recipe* (`feed` for RSS with common-path discovery, the documented `tools/fetch_source.py` subcommand for `api`/`bridge`, browser-UA HEAD→GET with a GET-retry-after-403 for `webfetch`); UA aligned to the bridge (Chrome 138 + Sec-CH-UA); derives a per-source `action` (`none` | `needs-bridge` | `needs-demote`); schema_version 2.
- **`site/build.py` Ops dashboard:** the source-accessibility panel moved into **Health** and now floats ONLY non-`none` actions (sources needing a dedicated bridge or demotion), grouped and detailed; already-demoted and already-bridged-and-working sources are omitted. Explicitly distinguished from a run's per-run "Coverage gaps".

### What stays

The lens stays divergent; hard invariants untouched. The status-axis lifecycle thresholds and the "transport-403 never auto-demotes" rule are unchanged — the health check *recommends* action; the agent still applies the lifecycle rules. `sources_changed` (v2.62) and the per-run Run-detail panels are unchanged.

## 2.62 — 2026-06-20 (source-metadata-drift correction made a first-class lifecycle step; per-run `sources_changed` telemetry surfaced on the Ops dashboard)

### Why

A full out-of-band audit of all 147 sources on 2026-06-20 (12 parallel workers, artefacts under `work/source-audit-2026-06-20/`) found that the source list's *status* axis was maintained but its *metadata* axis had drifted: ~47 sources had a `fetch_method` that no longer reflected the recipe that actually works (publishers that began 403-ing WebFetch but serve a clean RSS feed; SPA landings whose only path is a bridge subcommand; feeds that moved or died), ~35 had stale `category` tags (vendor labs mis-tagged `gov`; research blogs that started shipping CVE write-ups but lacked `vulns`), and dozens of proven candidates had never been promoted. Two "transport-blocked" sources (`databreaches.net`, `prodaft.com`) turned out to be reachable once the bridge UA was modernised. The lifecycle rules covered status transitions and url updates but never said "also fix the recipe / categories / reliability when a fetch shows they're wrong," and there was no per-run record of source edits for the operator to review — so drift accumulated silently between audits.

### What changed

- **Daily + weekly (shared machinery, in lockstep):** added a **metadata-drift correction** step to the `sources/sources.json` lifecycle — fetching a source re-validates its `fetch_method` / `category` / `reliability`, and a mismatch is corrected in place (append-only dated note), not just its counters. Added a `sources_changed[]` array to the `state/run_log.json` schema (both prompts) with `{id, change, from, to, reason}` per edit, plus its population rule; the change vocabulary is `promoted | demoted | added | recategorised | reliability | fetch_method | url | recovered`.
- **`tools/fetch_source.py` (v2.62):** bumped the bridge User-Agent Chrome 124 → 138 and added the matching `Sec-CH-UA` client-hint headers a real Chrome 138 sends, so WAFs that cross-check UA ↔ client-hints stop filtering the bridge. This recovered `databreaches.net` (its `/feed/` RSS now 200) and `prodaft.com`. Trimmed `CLOUDFLARE_BLOCKED_HOSTS` to the hosts still genuinely blocked to every UA (`group-ib.com`, `ccn-cert.cni.es`, `coe.int`, `downloads.seppmail.com`).
- **`site/build.py` Ops dashboard:** new per-run "Sources Δ" runs-table column + a "Source changes (latest run)" panel reading `run_log[].sources_changed`, and a "Source health" panel that finally surfaces the previously-orphaned `state/source_health.json` snapshot.
- **`sources/sources.json`:** applied the audit — 33 candidate→active promotions, 1 duplicate consolidated (`sansec` → `sansec-research`), reliability/category/fetch_method corrections, and an append-only dated audit note with the working recipe on every source so an LLM agent knows how to fetch each one and what not to waste calls on.

### What stays

The intelligence lens and output structure stay divergent (daily operational-today vs. weekly horizon). The hard invariants are untouched: AI-content notice, no IOCs, two-source + national-CERT carve-out, English output, feature-branch-only publishing, the self-check gate (Phase 5.5 / 4.5) and verification loop (Phase 5.7 / 4.7), per-item taxonomy footers, memory commits. The status-axis transition thresholds (3 content runs to promote; the 403/429/503 *never*-demotes-on-transport rule; one-new-candidate-per-run cap) are unchanged — v2.62 only adds the *metadata* axis alongside them. `sources_changed` is additive: a run that records `[]` is valid.

## 2.61 — 2026-06-20 (weekly aligned to the daily gold standard in structure + procedure, with a sharpened horizon lens; daily↔weekly division of labour made explicit)

### Why

The weekly summary had drifted procedurally from the daily, which is the gold-standard routine. A side-by-side audit found the weekly was **missing several procedures the daily institutionalised** and was **under-serving the intelligence lens the weekly exists for**. The operator asked to (a) bring the weekly procedurally very close to the daily, and (b) sharpen the weekly's *distinct* view onto the intelligence — broader threat picture, how things developed across the week, the week's highest-impact / "what's on fire if no one acted" items, threat-actor developments, research findings, long-horizon / multi-day campaigns, annual reports, and looking-ahead — while keeping the asymmetry: **the weekly may repeat a daily item with a new lens; the daily must not repeat the weekly and must not carry long-horizon synthesis.**

Concrete procedural gaps the weekly had relative to the daily:

1. **No pre-compose verification/triage pass.** The daily's Phase 2 (URL spot-check → two-source → fake-news → CVE-verify → dedup → recency re-check → rank) had no weekly analogue; the weekly jumped from horizon research straight to compose.
2. **No compose-after-return anti-fabrication gate.** The daily's Phase 4 `.ended_at`-file gate (added v2.58 after a run fabricated sub-agent returns mid-wait) had no weekly equivalent, even though the weekly spawns W1/W2 the same way.
3. **No historical-context / Background rule.** The daily's PD-10 reserves Background for deep dives; the weekly — whose whole job is the longer arc — had no Background directive at all.
4. **Thin less-is-more + recency directives** vs. the daily's (no item-level-cuts list, weaker recency-enforcement framing).
5. **`Evidence:` source-quote binding absent** from the weekly footer spec, even though `check_brief.py`'s `evidence-shape` check runs on weeklies too.
6. **Phase 4.7 lagged Phase 5.7:** no prior-iteration-deltas block for even (Sonnet) iterations, no F13/F14/F15 remediation rows, no rich per-iteration `findings[]` in the run-log schema, finding range stated as F1–F12.

And the lens gap: the weekly had **no home for research findings or threat-actor developments** — the daily has a dedicated § 3 Research section, the weekly had none, scattering that content or dropping it.

### What changed

**`prompts/weekly-summary.md` (v2.61):**

- **New § 6 "Research & threat-actor developments"** — mirrors the daily's § 3 but synthesises across the week (research findings + actor-level shifts: new clusters, attribution shifts, tooling / affiliate moves). Output structure goes from 11 to **12 sections (0–11)**; §§ 6–10 renumbered to §§ 7–11 (Annual reports → § 7, Long-running → § 8, Policy → § 9, Looking ahead → § 10, Verification → § 11). All internal § cross-references updated.
- **New Phase 2.5 — Verification & triage pass** between horizon research and compose: the weekly analogue of the daily's Phase 2, with weekly-specific dedup (against prior *weeklies*, not the dailies, since the weekly may repeat daily content) and W-PD-1 enforcement. Persists `work/<run-id>/triage.json`.
- **Compose-after-return discipline** added to Phase 3 (the daily's `.ended_at` gate, adapted to W1/W2).
- **W1/W2 rebalanced:** W1 is now "threat-actor, campaign, research & report horizon" (long-running campaigns + threat-actor developments + research findings + annual reports); W2 unchanged (strategic & policy). Phase 1 gains a 7th working list ("Research & threat-actor developments").
- **Prime directives:** PD-5 recency strengthened (mirrors daily PD-7 emphasis, anchored on the new Phase 2.5 re-check); PD-13 less-is-more gains an item-level-cuts list and per-section empty-stub guidance; **new PD-14 historical-context / Background rule** (the weekly is the explicit home for the longer arc the daily skips).
- **`Evidence:` field** documented in the footer spec — mandatory on § 1 (the weekly's highest-trust section, analogue of the daily's Immediate Action callout), encouraged on §§ 2 / 3 / 6.
- **Phase 4.7 brought to parity with the daily's Phase 5.7:** prior-iteration-deltas block for even iterations, F13/F14/F15 + generic-URL remediation rows, finding range corrected to F1–F15, rich per-iteration `findings[]` added to the run-log schema (truth = F1–F4 + F13–F15; editorial = F5–F10 + F12).
- **"What the weekly is for"** rewritten to foreground the broader-picture / research / threat-actor / long-horizon lens and to state the daily↔weekly asymmetry explicitly. Quality-gate checklist expanded (Phase 2.5 ran, compose-after-return honoured, § 1 Evidence, § 6 present-or-stub).
- Looking-ahead Phase-0 reads made **section-number-agnostic** (match the heading text, not `## N`) so future renumbers don't break the previous-weekly read.

**`prompts/daily-cti-brief.md` (v2.61, lockstep):** banner bump; **PD-8 gains an explicit daily↔weekly division-of-labour clause** (daily must not re-report a recent weekly's item, must not carry long-horizon / strategic-arc synthesis — that is the weekly's job; the asymmetry runs one way); prior-coverage comment updated to "§§ 0–10 of the previous weekly".

**Tooling / config (so the new § 6 renders, validates, and dedups):**
- `site/taxonomy.yaml` — added `weekly-research` to `sections`.
- `tools/check_brief.py` — added `weekly-research` slug-keyword mappings (before the bare `research` key), `WEEKLY_FOOTERED_SECTION_KEYS`, and the primary-source-quality / single-source / aggregator-only `target_keys` (mirroring the daily's treatment of `research`).
- `site/build.py` and `tools/build_prior_coverage.py` — same slug mappings; `build_prior_coverage.py` `weekly_section_keys` set gains `weekly-research` so the new section is indexed for dedup.
- `prompts/brief-template.md` — weekly template gains the § 6 block, renumbers §§ 7–11, and shows an `Evidence:` example on § 1.
- `docs/architecture.md` — weekly description updated (12 sections, Phase 2.5, rebalanced W1/W2, the lens + asymmetry).

### What stays

- **Every hard invariant** (AI-content notice, inline links, two-source + national-CERT carve-out, no IOCs, no vanity metrics, English, always-produce, feature-branch publishing chain, Phase 4.5 self-check, Phase 4.7 verification loop, taxonomy footers, memory commits) — untouched.
- **The daily's procedure is unchanged** beyond the lockstep banner and the PD-8 clause — the daily remains the gold standard; the weekly was moved toward it.
- **The verifier definitions** (`cti-verification.md` / `-alt.md`) are untouched — they already carry F1–F15 and the W-PD-1 weekly check; no lockstep edit was needed.
- **Section slugs are derived from heading text, not numbers**, so the renumber does not change any slug; existing weeklies (W19–W24) still parse and `check_brief.py` still passes against them. `weekly-research` is **footered-but-not-required**, so historical weeklies without the section do not FAIL.
- Verified after the change: `site/test_build.py`, `site/build.py` (briefs=52, 0 skips), `tools/check_brief.py briefs/weekly/2026-W24.md` (0 FAIL), and `tools/build_prior_coverage.py` all pass.

---

## 2.60 — 2026-05-25 (weekly ISO-week anchor — most-recent-Sunday; fixes Sun→Mon-boundary duplicate weeklies)

### Why

Two weekly summaries were published for the **same** coverage week because the weekly routine computed its target week from the wall-clock `date -u +%G-W%V` at the moment the container fired. The primary fires Sunday night; a run that crosses the Sunday→Monday **UTC** boundary computes the *next* ISO week and writes a brand-new file for a week that has barely started:

- **2026-05-18 00:02 UTC** — a Monday fire labelled its run `2026-W21` and wrote `briefs/weekly/2026-W21.md` re-summarising the just-finished W20 content (self-corrected the following Sunday when the legitimate W21 run overwrote the file).
- **2026-05-25 00:13 UTC** — the **backup** run for the W21 weekly fired after midnight, computed `2026-W22`, found no `2026-W22.md` (the primary had correctly written `2026-W21.md` on Sunday), and generated a full second weekly — `briefs/weekly/2026-W22.md`, header *"2026-W22 (Mon 18 May – Sun 24 May)"* — a duplicate of week 21.

The backup's guard prompt (*"if this week's file exists, do nothing"*) could not catch it: it computed "this week" the same wall-clock way and checked the wrong (future) week's filename.

### What changed

**`prompts/weekly-summary.md`** (v2.60):

- **Phase 0 step 0** — `ISO_WEEK=$(date -u +%G-W%V)` replaced with an anchor to the **week ending on the most recent Sunday**:
  ```bash
  dow=$(date -u +%u)                                   # 1=Mon … 7=Sun
  ISO_WEEK=$(date -u -d "$((dow % 7)) days ago" +%G-W%V)
  ```
  On a Sunday this equals the current ISO week; early Monday it resolves to the week that just ended — both yield the same label the Sunday primary produces. An inline comment records the why.
- **Phase 0 step 1** — prose rewritten: the run targets the *just-completed* ISO week bound to `ISO_WEEK`, never the raw `+%G-W%V`; re-run/overwrite is scoped to "a previous run for the **same ISO week**".
- **Phase 6** (publish verification) — the two inline `$(date -u +%G-W%V)` computations (`weekly_path`, `week_id`) now derive from the same most-recent-Sunday anchor, so a post-midnight fire polls `origin/main` and the live site for the week it actually published.

**`prompts/daily-cti-brief.md`** — version banner bumped to v2.60 for lockstep only; no behavioural change (the daily is keyed per calendar day and has no ISO-week rollover).

### What stays

- The weekly remains cadence-agnostic; the anchor assumes the operator's Sunday-night / early-Monday cadence (a fire Sun–Wed still resolves to the correct just-completed week). A mid-week cadence change would need the anchor revisited.
- Re-run / overwrite semantics for a same-ISO-week retry by the same role are unchanged.
- The CRITICAL "always produce a summary" directive, the Phase 4.5 self-check gate, the Phase 4.7 verification loop, and the feature-branch publishing chain are untouched.
- The backup execution's own stand-down guard (provided to the operator) anchors the same most-recent-Sunday way and checks `origin/main` rather than the local tree; this prompt change makes the *generation* path label correctly on the occasions the backup must run.

---

## 2.59 — 2026-05-15 (work/<run-id>/ becomes version-controlled — every run commits the sub-agent artefact dir alongside the brief)

### Why

The 2026-05-15 cap-breach run made it painfully clear that the operator's primary forensic surface — *what each sub-agent actually fetched, what it wrote, what evidence quote was extracted, which verification iteration flagged what* — vanishes the moment the routine container shuts down. The brief on `main` is the only record. The `work/<run-id>/` directory that carried `findings.<domain>.yaml`, `verification.iter<N>.md`, `url-liveness.tsv`, the per-agent `.started_at` / `.ended_at` timestamps, and `prior_coverage.json` was gitignored — by design, "intermediate state, ephemeral". That design has been wrong for the entire history of the routine; we just didn't notice until v2.58's structured-findings shape made the cost visible: the v2.58 main agent reads sub-agent returns from `findings.<domain>.yaml`, and now that file is the *authoritative record of what each sub-agent surfaced*. Throwing it away post-run leaves no audit trail when the published brief later turns out to contain a fact the cited source doesn't support.

User asked directly: *"commit the agent work to the git repo and publish it for each run. I would love to see the subagent findings versioned in the git. Just add the entire work/ dir to the commit with the brief."* v2.59 satisfies that request.

### What changed

**`.gitignore`** — `work/` removed; replaced with narrow editor/OS-chaff exclusions (`work/**/.DS_Store`, `work/**/*.swp`, `work/**/*.bak`).

**`CLAUDE.md`** — "Operational guardrails" bullet on `work/<run-id>/` rewritten: "v2.59: `work/<run-id>/` is version-controlled — Phase 6 (daily) / Phase 5 (weekly) commits the directory alongside the brief so sub-agent findings YAMLs, verification iteration reports, the URL-liveness ledger, and per-agent timestamp checkpoints are auditable in git history. The directory is the operator's primary forensic surface when a published brief later surfaces a defect." The `Where things live` block expanded to enumerate the per-run files: `findings.<S1|S2|S3|S4>.yaml`, `verification.iter<N>.md`, `verification.iter<N>.findings.yaml`.

**`prompts/daily-cti-brief.md`** — Phase 6 § 1 (Stage and commit) `git add` invocation extended to include `"work/${RUN_ID}/"`. The commit-message template adds a `work/${RUN_ID}/:` line summarising the artefact-dir contents. A rationale paragraph above the snippet explains why committing the dir matters and quantifies the size impact (~200-500 KB per run; ~70-180 MB cumulative over a year).

**`prompts/weekly-summary.md`** — Phase 5 § 1 (Stage and commit) extended analogously; references the daily prompt's rationale paragraph to avoid duplication.

### What stays

- The `work/<run-id>/` directory's *contents* are unchanged — same `findings.<domain>.yaml` shape, same `verification.iter<N>.md` shape, same `url-liveness.tsv`, same `prior_coverage.json` / `prior_coverage_keys.json`, same `state-summary.json`. v2.59 changes only *what we commit*, not *what we write*.
- The auto-merge workflow's conflict-resolution rules. `work/<run-id>/` is unique per run (the `run_id` carries the date + sha8), so concurrent routine runs never collide on the same path.
- Size discipline: future work on a `tools/work_archive.py` (compress runs older than 30 days; delete runs older than 1 year) is deferred to v2.60+ once the actual growth rate is observed.

---

## 2.58 — 2026-05-15 (Tier 1 + 3 + 4 — source-quote binding, verifier convergence, workflow hardening)

### Why

v2.57 (Tier 2 mechanical pre-verifier checks) caught the surface defects that don't need editorial review — broken anchor links, quantifier flags, TL;DR/body drift, name-collision candidates. v2.58 lands the deeper structural changes the 2026-05-15 cap-breach run revealed:

1. **The Datadog Shai-Hulud inversion almost shipped to readers.** The brief described an attacker offensive worm as if it were a Datadog defender framework and § 6 told defenders to "run the framework." The only thing that stopped publication was the verifier's truth pass on iter-1. Nothing structural prevented the inversion. **Tier 1 (source-quote binding)** addresses this by requiring sub-agents to attach a verbatim quote from a fetched source to every load-bearing claim. The inversion would have been impossible because no quote from the Datadog blog says "defender framework"; the sub-agent could not have constructed an `Evidence:` field for the inverted claim.

2. **The verifier loop introduced regressions.** Iter-2 (Sonnet, reading cold) added "Hyunwoo Kim" as Fragnesia co-discoverer — a fact the cited source does not support. Iter-3 (Opus) had to revert. **Tier 3.1 (prior-iteration deltas to alternating verifiers)** addresses this by passing the previous iteration's findings + the main agent's applied remediations to the Sonnet (even-iteration) spawns only. The cold cycle (Opus, odd iterations) keeps blind-spot detection; the deltas cycle prevents regressions on the same edits.

3. **The verifier prompt's truth pass was generic.** **Tier 3.2 (new finding categories F13/F14/F15)** splits the most-common truth-defect classes into named categories with explicit detection guidance: analytical-link-as-fact (F13), quantifier-without-source (F14), name-collision-unflagged (F15).

4. **The main agent fabricated sub-agent returns mid-wait.** The 2026-05-15 transcript shows the main agent writing "S1 returned: …" with full invented CVE details *before any sub-agent had returned*. **Tier 4.2 (compose-after-return)** makes it mechanical: no `work/<run-id>/<S1|S2|S3|S4>.ended_at` file ⇒ no `Edit` against `briefs/YYYY-MM-DD.md`. **Tier 4.3 (findings on disk)** complements this: sub-agent returns are written to `work/<run-id>/findings.<domain>.yaml`, and the main agent reads from disk rather than parsing assistant-text.

5. **The premature-commit issue.** A stop hook fired mid-verification; the main agent committed with `final_verdict: "PENDING"`. **Tier 4.1 (commit-gate)** adds a `verification-final-verdict-set` FAIL to `tools/check_brief.py`.

### What changed

**`tools/check_brief.py`** — **`verification-final-verdict-set`** FAIL (Tier 4.1) refuses commits when `state/run_log.json.verification.final_verdict` is in the pending-states set. **`evidence-shape`** check (Tier 1) — FAIL on malformed `Evidence:` field, WARN on attribution unbound to listed Source, PASS silently when absent. Footer parser extended (in both `site/build.py` and the check_brief fallback) to parse `Evidence:` into a structured `evidence: [{quote, attribution}]` list.

**`.claude/agents/cti-research.md`** (Tier 1 + 4.3) — Return contract reshaped: sub-agents write structured findings to `work/<run-id>/findings.<domain>.yaml` and return only a ~150-token summary. The YAML carries a new `evidence: [{quote, attribution, source_url}]` list per item. Legacy Markdown return shape kept as fallback. `.ended_at` checkpoint file mandate strengthened.

**`.claude/agents/cti-verification.md` + `.claude/agents/cti-verification-alt.md`** (Tier 3.1 + 3.2, lockstep) — New "What to read" bullet on the optional `Prior-iteration deltas` block. Three new finding categories: **F13 analytical-link-as-fact**, **F14 quantifier-without-source**, **F15 name-collision-unflagged** — all truth-class. YAML `category` slug list grows accordingly. Verdict-block truth count = F1–F4 + F13–F15.

**`prompts/daily-cti-brief.md`** — Phase 4 Compose-after-return discipline; Phase 5.7 Prior-iteration deltas block; Phase 5.7 F13/F14/F15 remediation rows; per-item-footer `Evidence:` field documentation (mandatory on § 0 Immediate Action callout, optional elsewhere).

**`prompts/brief-template.md`** — Immediate Action callout footer example shows `Evidence:` field shape.

**`prompts/check-brief-fixes.md`** — Fix-recipe paragraphs for `verification-final-verdict-set`, `evidence-shape`, `evidence-binding`.

### What stays

- 5-iteration verifier cap, model rotation, early-exit on low-defect convergence, cap-breach safety valve.
- Mechanical gate ↔ verifier separation.
- Markdown fallback for sub-agent returns (parsed alongside YAML).
- Evidence field parsed and validated but not yet rendered on the public site (reserved for v2.60+).

---

## 2.57 — 2026-05-15 (Tier 2 mechanical pre-verifier checks: anchor-resolution, quantifier-evidence, tldr-body-drift, name-collision)

### Why

The 2026-05-15 cap-breach run had iter-4 (Sonnet, 237 s) and iter-5 (Opus, 59 s) burn editorial-review budget on things `check_brief.py` should catch for free: a CVE-table-cell drift in iter-4 and five broken `[text](#slug)` anchor links in §6 Action Items in iter-5. Three other iterations spent budget flagging quantifier claims ("five unpatched zero-days", "first time ESET has documented", "10 additional clusters") and the TL;DR-vs-body region drift (`europe, switzerland` in the §6 footer after iter-1 had already removed `switzerland` from §1). The Datadog Shai-Hulud inversion (iter-1 F1) was preceded by a missed-collision signal — the name "Shai-Hulud" appeared in prior coverage as the TeamPCP attacker worm and in today's §4 UPDATE as the Datadog tool, without the main agent registering the collision.

Tier 2 lands four mechanical checks that catch each defect class before the verifier ever spawns. Goal: free verifier budget for editorial judgement, drop the cap-breach rate, and surface name-collision risk explicitly so the catastrophic-inversion class is registered by the main agent at compose time rather than discovered by the verifier post-hoc.

### What changed

**`tools/check_brief.py`** — four new checks:

- **`anchor-resolution`** (FAIL). Every `[text](#slug)` inline link must resolve to an H2/H3/H4 heading in the same brief. Slugs computed via `slugify()` imported from `site/build.py` (local fallback). Mechanical defects of this class should never reach a verifier iteration.
- **`quantifier-evidence`** (WARN, detection-only). Surfaces phrases like "first time", "the only", "never before", numeric quantifiers ("five unpatched zero-days", "10 additional clusters"), counted-status patterns for verifier corroboration against cited sources. v2.58 upgrades the named F14 category to FAIL when paired with Evidence binding.
- **`tldr-body-drift`** (WARN). For each TL;DR bullet naming a CVE-YYYY-NNNNN token, find the matching § 1 / § 2 body item and compare the TL;DR's regional phrasing against the body footer's `Region:` taxonomy. v2.57 ships a narrow Swiss-and-European-only phrase set — the concrete 2026-05-15 iter-1 failure mode.
- **`name-collision`** (WARN). Reads `name_collision_candidates` from `work/<run-id>/prior_coverage.json` (new field — see below). For each H3 in today's brief, scans the body for any candidate name and WARNs if the H3 is not an `UPDATE:`-prefixed block and the body lacks a disambiguation phrase. Catches the Datadog Shai-Hulud inversion class at compose time.

**`tools/build_prior_coverage.py`** — emits `name_collision_candidates` list. Three patterns extract codenames from prior-coverage titles: quoted codenames, hyphenated TitleCase, CamelCase with ≥ 2 internal capitalisations. Actor-cluster IDs (UAT-/UNC-/APT-/Storm-/CL-XXX-/TA/UAC-) deliberately excluded — stable tracking IDs, never reused for defender tooling. On the 2026-05-15 corpus: 35 candidates including Shai-Hulud, Fragnesia, Dirty Frag, NGINX Rift, YellowKey, GreenPlasma, BitLocker, TanStack, FrostyNeighbor, ShinyHunters.

**`prompts/check-brief-fixes.md`** — Four new fix-recipe paragraphs, one per check.

### What stays

- Mechanical gate ↔ verifier separation; verifier reads the same brief shape, just with a richer pre-spawn WARN list as cross-check signal.
- All existing checks unchanged. v2.57 is purely additive.

---

## 2.56 — 2026-05-15 (telemetry: `fetch_failures[]` becomes a strict "coverage gaps" log, `bridge_uses[]` tracks successful bridge calls separately, Ops dashboard sub-agent card rebuilt with labelled metrics)

### Why
A review of the last 5 runs' `state/run_log.json.fetch_failures[]` arrays showed the field had become a misleading catch-all. Concretely, the 2026-05-12 daily run logged 13 "fetch failures" — but reading the entries showed:

- `cisa-kev` → `bridge:cisa-kev → 200 OK; no new entries` — **success**, not failure
- `ncsc-ch-security-hub` → `bridge → 200 OK; latest posts ... no new posts in window` — **success**
- `enisa-euvd` → `bridge:enisa-euvd.recent → 200 OK; coverage gap is no-new-content rather than transport failure` — **success**, with the entry itself admitting it's not a real failure
- `bsi-de` → `bridge:bsi-rss → 200 OK; no new in-window KRITISCH items` — **success**
- `bleepingcomputer` → article-level 403, recovered via THN/SecurityWeek — **covered_anyway: true**, not a gap
- `ico-uk` → SPA listing returned navigation only, but structured `ico-uk enforcement` worked — **success**
- ...and 3 actual gaps (`databreaches-net`, `inside-it-ch`, ...)

The pre-v2.56 sub-agent prompt explicitly told agents to "log every transport / SPA-empty / paywall outcome, even if you recovered." That made `fetch_failures[]` a "things I tried that had a wrinkle" log, not a "things that broke" log — exactly the wrong signal for an operator scanning the Ops dashboard at 8am to spot real problems. The user-named symptom was *"no new advisories is not a fetch failure ... when the agent can fetch via the bridge that is also not a failure."*

Two additional usability problems surfaced in the same review:

1. **Ops sub-agent telemetry was unreadable.** The card printed `"3 items / 12/18 sources / 461 duration seconds 9 webfetch calls 18 websearch calls 11 bridge fetches"` — all chips on the same line, all using the same visual weight, no labels distinguishing what was a count vs. what was a unit. The "12/18" had no tooltip explaining numerator/denominator.
2. **`spa-empty-body` was still a documented `error_class`** even though v2.53+ ships a structured-endpoint bridge subcommand for every SPA host the brief uses — those should never appear in the log.

### What changed

**`.claude/agents/cti-research.md` § fetch_failures reporting — rewritten.**

The new rule, prefixed clearly at the top of the section: *log a `fetch_failures[]` entry ONLY when the source could not be retrieved at all and the recipe in `sources/sources.json` has no working alternative.* Two explicit lists follow:

- **Log as a failure:** 5xx with no recovery; 403/429/TLS/DNS/timeout with bridge AND Wayback exhausted AND `covered_anyway: false`; Cloudflare Managed Challenge on hosts without Wayback coverage; bridge subcommand 404 on a *non-speculative* identifier; TollBit-style auth-gated content with no alternate.
- **Do NOT log as a failure:** "Bridge fetched OK; no new content in window" (success); WebFetch-403 on a known-403 host where the bridge then succeeded (the bridge IS the recipe); SPA-empty landings handled by a structured-endpoint bridge subcommand; sources where `covered_anyway: true` via a deterministic alternate; NCSC-NL speculative-ID 404s (speculative enumeration was deprecated in v2.53 — use `ncsc-nl recent`).

The `spa-empty-body` error class is dropped from the documented vocabulary; sub-agents that find a new SPA host with no structured-endpoint route should add a `Coverage gap: <source-id> (recipe missing)` line in § 7 rather than logging a fetch failure.

**New optional `## Bridge uses` section** in the sub-agent return → `state/run_log.json.bridge_uses[]`. Each record is `{id, method, outcome}` with `outcome ∈ {ok, empty-feed, item-not-found, other}`. This captures bridge effectiveness telemetry that used to be lumped into `fetch_failures[]` as fake failures. The section is optional; omitting it means no bridge-use telemetry that run.

**Daily + weekly prompt Phase 5 schema docs mirrored** to the new rule. `fetch_failures` description was rewritten to lead with "ONLY real, unrecovered failures" and to enumerate the v2.56 do-not-log cases. New `bridge_uses` field documented in the Phase 5 state-update sections.

**Ops dashboard (`site/build.py`, `site/assets/css/styles.css`) — sub-agent card rebuilt.**

The old `ops-sa-card__stats` line + `ops-sa-card__tele` chip row are replaced with a `<dl class="ops-sa-card__metrics">` definition list:

```
ITEMS RETURNED   3
SOURCES          3 of 27 contributed (11%)
DURATION         7m 23s (443s wall-clock)
TOOL CALLS       14 WebFetch · 8 WebSearch · 11 bridge
```

Labels are small-caps light-weight; values are mono bold. Tool calls cluster on a single row (they're three related counters). Optional metrics (`urls_checked`, `tokens_in`, `tokens_out`) move below a hairline to an "extras" row when reported, keeping the primary card uncluttered.

**Coverage-gaps table replaces "Fetch failures" table.** The table is renamed in the dashboard (`<h3>Coverage gaps (latest run)</h3>`) with an explainer line below the header stating *"Sources the brief needed that returned no usable content via any documented recipe. Bridge-recovered or quiet-day sources do NOT appear here under v2.56."* The "Outcome" column is dropped (every row is a gap by definition). A new yellow soft-signal row badge highlights any record with `covered_anyway: true` that survived from older runs — "covered via alternate — should NOT be in this list under v2.56."

**New "Bridge invocations" panel** renders the separate `bridge_uses[]` stream as a chip row (`12 ok`, `4 empty feed`, `1 item not found`) followed by a frequency list of bridge subcommands. This is the panel that shows "the bridge is doing its job" without conflating with the gap signal.

**Runs table sub-agent cell** (`_sa_cell`) — adds explicit `items` label and a tooltip on the `sources_used / sources_attempted` ratio so the bare "12/18" can no longer be misread.

### What stays
Every editorial invariant unchanged. PD-1 through PD-13 unchanged. Main-agent anti-fetch invariants (v2.52 META #16 / W-INV-3) unchanged. The `fetch_failures[]` record SHAPE is identical to v2.48 — `id`, `url_tried`, `fetch_method`, `status_code`, `error_class`, `error_message`, `attempted_methods`, `mitigation_applied`, `covered_anyway` are all the same fields with the same semantics. Only the **policy on when to write a record** has tightened. The dashboard's legacy back-compat for the v2.47 `{id, code, note}` shape is preserved (renders as yellow "legacy shape — needs detail" row). `tools/check_brief.py` is unchanged.

### Migration note
- Sub-agents that follow the v2.56 prompt will produce shorter `fetch_failures[]` arrays. The dashboard's "Coverage gaps (latest run)" panel will be empty on most runs — that's the new normal, not a regression.
- Pre-v2.56 records may carry `covered_anyway: true` entries; those render with a yellow soft-signal row badge so the operator can see at a glance which runs were under the old rule.
- `bridge_uses[]` is optional — sub-agents that don't emit a `## Bridge uses` section produce a missing field, which the dashboard renders as "no bridge invocations reported" (no panel).

---

## 2.55 — 2026-05-15 (bridge fetcher: generic `feed <URL>` subcommand for any RSS/Atom, 16-source verification with per-article drilldowns, RDF/Atom parser fix, 6 new sources added)

### Why
v2.54 added MSRC + MSFT Security Blog support, but a wider audit of the operator's source list surfaced **16 widely-cited CTI publishers** that the bridge could not handle uniformly: half were RSS-driven (and each would need its own subcommand under the v2.49–v2.54 pattern), two had no RSS at all (Trellix, SANS NewsBites), one had broken Atom parsing in the v2.53 helper (Schneier + heise.de — `_parse_rss` lowercased the namespace URI and so missed the case-sensitive `{http://www.w3.org/2005/Atom}feed` root), and one was anti-bot-gated (heise.de via TollBit).

The 16 publishers covered in this release:
- thedfirreport.com — DFIR Report
- sans.org/newsletters/newsbites — SANS NewsBites
- krebsonsecurity.com — Krebs on Security
- trellix.com/blogs — Trellix Research / Perspectives / Platform
- blog.compass-security.com — Compass Security (Swiss CH-EU primary)
- intel471.com/blog — Intel 471 cybercrime intelligence
- heise.de/security — Heise Security (DE)
- threatpost.com — Threatpost (archive-only since 2023)
- thehackernews.com — The Hacker News
- isc.sans.edu — SANS Internet Storm Center
- cloud.google.com/blog/topics/threat-intelligence — Mandiant / GTIG
- schneier.com — Schneier on Security
- troyhunt.com — Troy Hunt / Have I Been Pwned
- socprime.com/blog — SOC Prime Sigma research
- wiz.io/api/feed/cloud-threat-landscape — Wiz Cloud Threat Landscape
- sophos.com/en-us/blog — Sophos News

### What changed

**`tools/fetch_source.py` — banner v2.54 → v2.55.**

1. **New `feed <URL> [N]` subcommand.** Generic RSS / Atom / RDF parser that runs on any HTTPS feed URL and returns `{source, feed, count, items: [{title, link, published, summary}]}` — the same JSON shape every other listing subcommand uses. The agent's drilldown pattern (take `link` from `items[i]`, then `url <link>` for the full body) works uniformly across every publisher. Replaces dozens of per-publisher subcommands that the bridge would otherwise grow.

2. **`_parse_rss` rewritten with proper namespace handling.** v2.53's parser lowercased `root.tag` before comparing to `{http://www.w3.org/2005/Atom}feed` — XML namespaces are case-sensitive per spec, so the comparison failed and any Atom feed raised `ValueError: unrecognised feed root: '{http://www.w3.org/2005/Atom}feed'`. The new parser splits the qualified tag into namespace URI + local name, lowercases only the local part, and case-insensitively compares the namespace URI. It also adds support for RSS 1.0 / RDF Site Summary feeds (`{rdf-syntax-ns#}RDF` root with `{rss/1.0/}item` children), which a small but growing minority of CMSs emit. Atom `<link>` handling now prefers `rel="alternate"` over the first link element (Atom can repeat `<link>` with different `rel`/`type`), and Atom item bodies fall back from `<summary>` to `<content>` when only the latter is present.

3. **End-to-end verification of all 16 sources.** Every requested publisher was probed: feed-parse via `feed <URL>` then per-article drill via `url <link>`. 14 of 16 succeed cleanly (RSS feed returns titles + links + summaries, drilldown returns ≥40 KB of server-rendered HTML). 2 have no RSS feed and use a landing-scrape recipe (Trellix, SANS NewsBites — both documented in `cti-research.md`). 1 (heise.de) returns its RSS feed cleanly but per-article URLs are **TollBit-gated** — the response is a 307 redirect to `tollbit.heise.de/` or a 274-byte "you are not authorized to access this content without a valid TollBit Token" body. Documented as: use the feed's 150-char `summary` for awareness, pivot to a corroborating publisher for body.

**`sources/sources.json` — 6 added + 10 updated.** New entries: `intel471`, `trellix`, `threatpost` (demoted — archive-only), `troyhunt`, `socprime`, `sans-newsbites`. Existing entries updated with an `rss_url` field on the 10 of 16 that have one: `dfirreport`, `krebs`, `compass-security`, `heise-sec`, `sans-isc`, `mandiant-gtig`, `schneier`, `wiz-blog`, `sophos-xops`, `hackernews`. Each `notes` field carries the verified recipe (`python3 tools/fetch_source.py feed <url> [N]`). `heise-sec.notes` carries the TollBit warning verbatim. Total active sources: 120 (was 114 at v2.54).

**`.claude/agents/cti-research.md` § Bridge fetcher** — three new subsections:

- **"Generic RSS / Atom feeds — `feed <URL> [N]`"** — explicit listing-→-drilldown pattern, plus a 14-row reference table of every source verified in v2.55 with its canonical `rss_url`.
- **"Publishers without an RSS feed — landing-scrape recipe"** — Trellix + SANS NewsBites pattern (regex over landing HTML for article hrefs, then `url <full>` per article). Also recommends sitemap probing before scraping.
- **TollBit / anti-bot publishers note** — heise.de per-article URLs return TollBit's 307 redirect; the feed's `summary` field carries the lede + first-paragraph context (~150 chars) which is enough for awareness coverage, and pivots to corroborating outlets handle the full-body need.

**Daily + weekly prompt banners — v2.54 → v2.55.** Banner-only bump.

### What stays
Every editorial invariant unchanged. PD-1 through PD-13 unchanged. Main-agent anti-fetch invariants (v2.52 META #16 / W-INV-3) unchanged. Allowlist-removed (v2.53), keys-only digest (v2.52), tech-depth taxonomy in sub-agent (v2.52), v2.53 structured discovery feeds (cert-eu, cert-fr, ncsc-nl recent, ico-uk enforcement, sec-edgar 8k), v2.54 MSRC + MSFT Security Blog subcommands, Wayback fallback — all unchanged.

### Migration note for sub-agent callers
The new `feed <URL> [N]` subcommand is the **preferred bridge entry point for any blog publisher with an RSS feed.** It replaces the v2.49–v2.54 pattern of "`url <listing>` and pray it's not an SPA." For sources in [`sources/sources.json`](../sources/sources.json), check the new `rss_url` field first: if non-null, use `feed <rss_url> N`; if null, the source needs the landing-scrape recipe documented in its `notes` field.

For heise.de specifically: do **not** chain `feed → url <heise per-article>`. The feed gives 150-char summaries which are usable; the per-article URLs are TollBit-blocked. Pivot to a corroborating publisher for body.

---

## 2.54 — 2026-05-15 (bridge fetcher: Microsoft MSRC Update Guide + Security Blog, end-to-end drilldown verification of v2.53 listings)

### Why
v2.53 added structured listing subcommands but did not formally verify that every per-article drilldown URL the listings return actually resolves to substantive content via the bridge. v2.53 also did not cover the **Microsoft MSRC Update Guide** (Angular SPA at `https://msrc.microsoft.com/update-guide/`) — every route on that domain returns a ~1 KB JavaScript shell, so without bridge support the routine cannot get Microsoft's Patch Tuesday data even though Microsoft publishes both the human-facing SPA *and* the public unauthenticated JSON APIs that back it.

The user-named sample URLs that need to return relevant content:
- `https://msrc.microsoft.com/update-guide/`
- `https://msrc.microsoft.com/update-guide/releaseNote/2026-May`
- `https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41089`
- `https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/`

All three MSRC routes are SPA-only; the Security Blog landing is server-rendered HTML but has an RSS feed that's cheaper to consume.

### What changed

**`tools/fetch_source.py` — banner v2.53 → v2.54.**

1. **`msrc cvrf <YYYY-Mon>`** — fetches `https://api.msrc.microsoft.com/cvrf/v3.0/cvrf/<release>`, returns full CVRF JSON. Verified 2026-May = 494 vulnerabilities, ~4.6 MB.
2. **`msrc cve <CVE-ID>`** — fetches `https://api.msrc.microsoft.com/sug/v2.0/en-US/vulnerability/<CVE>`, returns per-CVE detail JSON with `cveNumber`, `cveTitle`, `releaseNumber`, `releaseDate`, `vulnType`, `publiclyDisclosed`, `exploited`, `baseScore`, `impact`, `description` (HTML), `cweList`, `acknowledgements`, `articles`. Verified CVE-2026-41089 = Windows Netlogon RCE CVSS 9.8.
3. **`msrc release <YYYY-Mon> [N]`** — OData query `…/vulnerability?$filter=releaseNumber eq 'YYYY-Mon'&$top=N&$orderby=releaseDate desc`. Returns flat list with the operationally-interesting per-CVE fields. Verified 2026-May = 323 CVEs total.
4. **`msrc recent [N]`** — newest N CVEs across all releases.
5. **`msrc releases [N]`** — discovery: list of the N most-recent monthly release tags. Verified MSRC catalogue has 187 monthly releases dating back to 1999-Sep.
6. **`msft-secblog recent [N] [TOPIC]`** — Microsoft Security Blog RSS. General feed at `…/blog/feed/`; topic feed at `…/blog/topic/<slug>/feed/`. Topic slugs include `threat-intelligence`, `vulnerabilities-and-exploits`, `incident-response`, `ai-and-machine-learning`. Per-article drilldown via `url <link>` returns server-rendered HTML (~250–350 KB).

**MSRC content-negotiation handling.** The MSRC API responds with **XML** when the `Accept` header includes `*/*` and **JSON** when it's strictly `application/json`. The bridge's `msrc *` subcommands route through a new `_msrc_fetch_strict_json` helper that sends `Accept: application/json` (no `*/*` fallback). Without this fix, the bridge's default `Accept: application/json, */*;q=0.5` triggered XML responses and a misleading `JSONDecodeError: Expecting value: line 1 column 1`.

**MSRC OData `$orderby` constraint.** The SUG OData backend rejects multi-field sorts with HTTP 500. `msrc release` and `msrc recent` now use a single-field `$orderby=releaseDate desc` (the publisher's natural sort).

**End-to-end drilldown verification.** Every v2.53 listing subcommand was re-tested against its drilldown:

| Listing → Drilldown | Verified |
|---|---|
| `cert-eu recent` → `url <link>` | 2026-006 PAN-OS advisory, 19 KB, CVE-2026-0300 surfaced |
| `cert-fr avis-recent` → `url <link>` | CERTFR-2026-AVI-0552 Ivanti EPMM, 26 KB, 5 CVEs surfaced |
| `ncsc-nl recent` → `ncsc-nl csaf <id>` | NCSC-2026-0159 Exchange Server, CVE-2026-42897, full CSAF document |
| `ico-uk enforcement` → `url <url>` | South Staffordshire Water enforcement, 31 KB, monetary penalty text |
| `sec-edgar 8k` → `url <filing_url>` | CB Financial Services 8-K Item 1.05, 13 KB filing index |
| `msrc release` → `msrc cve <id>` | CVE-2026-41615 Authenticator, CVSS 9.6, full per-CVE detail |
| `msft-secblog recent` → `url <link>` | 2026-05-14 Kazuar botnet writeup, 326 KB, full article body |

The NCSC-NL chain confirms the v2.52 problem area (speculative advisory-ID 404s) is fully resolved: `ncsc-nl recent` returns parsed IDs from the RSS title field, the agent feeds them directly into `ncsc-nl csaf <id>` for the data.

**`.claude/agents/cti-research.md` § Bridge fetcher rewritten** — explicit "listing → drilldown" pattern for every structured subcommand, with the verified drilldown sizes and content patterns. New § "Microsoft MSRC Update Guide" documents the SPA / API mismatch and the citation rule (cite the human-facing SPA URL, fetch from the JSON API). New § "Microsoft Security Blog" notes the `msft-secblog recent` shortcut over `url`-fetching the landing page.

**Daily + weekly prompt banners — v2.53 → v2.54.** Banner-only bump; the operational changes live in the sub-agent definition. Anti-fetch hard invariants (META #16 / W-INV-3) unchanged.

### What stays
Every editorial invariant unchanged. PD-1 through PD-13 unchanged. Main-agent anti-fetch invariants (v2.52 META #16 / W-INV-3) unchanged — main agent still does no source fetching during Phase 1 / 2; this release improves sub-agent reach, not main-agent scope. Allowlist-removed (v2.53), keys-only digest (v2.52), tech-depth taxonomy in sub-agent (v2.52), Phase 0 token-budget guards (v2.50), verifier compact-summary contract (v2.50), early-exit on low-defect convergence (v2.50), 5-iteration verifier cap with model rotation (v2.47), URL-liveness ledger + deterministic `run_id` (v2.47) all unchanged. `tools/check_brief.py` unchanged.

### Migration note for sub-agent callers
- **MSRC Patch Tuesday coverage** now goes `msrc releases 3` (discover newest tag) → `msrc release <tag> N` (enumerate exploitation-status flags) → `msrc cve <id>` per interesting CVE. The Update Guide SPA URL remains the citation URL.
- **Microsoft Security Blog** coverage now goes `msft-secblog recent N [topic]` (RSS listing) → `url <article-link>` (full body). The topic-filtered feed (`threat-intelligence` etc.) is the right entry point for routine threat-intel coverage.
- Direct `url`-fetch of `msrc.microsoft.com/update-guide/...` is no-op (SPA shell). Don't.

---

## 2.53 — 2026-05-15 (bridge fetcher: allowlist removed, structured discovery feeds for JS-rendered listings, Wayback Machine fallback for Cloudflare-blocked hosts)

### Why
Forensic review of the last 5 runs' `fetch_failures` ledger (47 failure records across 25 distinct sources) surfaced four recurring root causes:

1. **JS-rendered listing pages** — `cert-eu`, `cert-fr` actualité, `advisories-ncsc-nl`, `ico-uk` all expose Angular / Next / React SPAs as their listing routes; the v2.49 bridge recipe `url <listing>` returned navigation shells with no advisory enumeration. The 2026-05-12 daily wasted ~8 min of sub-agent budget speculatively guessing NCSC-NL advisory IDs (NCSC-2026-0384, -0399, -0400, -0401 all 404'd; -0135 was the only one that resolved).
2. **Cloudflare Managed Challenge** — `inside-it-ch`, `databreaches-net`, `www.darkreading.com`, `www.coe.int`, `www.group-ib.com`, `downloads.seppmail.com` reject every UA combination the bridge can construct; v2.49's "WebSearch fallback only" recipe yielded zero unique items across 8 attempts.
3. **Host-allowlist friction** — every previously-unlisted CTI publisher (Ivanti Hub, TrendMicro Research, ConnectWise PSIRT, Dutch DPA, SEC EDGAR) required a code change in `ALLOWED_HOSTS` before the bridge would even attempt the fetch. The 2026-05-10 run logged `group-ib` and `autoriteitpersoonsgegevens-nl` as `host not on bridge allowlist` failures with no recovery path.
4. **SEC EDGAR 8-K Item 1.05** — the primary regulator filing for US-listed-company cyber incidents (West Pharma, ADT, Itron) returned 503 / 403 via `WebFetch`; no bridge subcommand existed.

### What changed

**`tools/fetch_source.py` — banner v2.49 → v2.53.**

1. **`ALLOWED_HOSTS` removed.** The bridge no longer enforces a static host allowlist. Every HTTPS publisher is reachable. The deeper SSRF defences are unchanged and remain the gate that matters: HTTPS-only (`_check_url`), resolved-IP deny list (`_resolve_and_check` refuses loopback, link-local, private, multicast, reserved, unspecified, and cloud-metadata endpoints 169.254.169.254 / 100.100.100.200 / fd00:ec2::254), redirect re-validation (`SafeRedirectHandler` re-runs `_check_url` on every 30x destination), body-size cap (25 MB HTML / 64 MB JSON), read-only-by-design (no posts, no auth, no cookies, no JS, stdlib-only).

2. **Six new structured subcommands.**
   - `cert-eu recent [N]` — fetches `https://cert.europa.eu/publications/security-advisories-rss`, parses RSS, returns JSON list of advisories with title / link / date / summary. Replaces the v2.49 `url <listing>` recipe that returned an Angular shell.
   - `cert-fr avis-recent [N]` — fetches `https://www.cert.ssi.gouv.fr/avis/feed/` for vendor-vulnerability advisories (CERTFR-YYYY-AVI-NNNN).
   - `cert-fr actu-recent [N]` — fetches `https://www.cert.ssi.gouv.fr/actualite/feed/` for weekly bulletins (CERTFR-YYYY-ACT-NNNN).
   - `ncsc-nl recent [N]` — fetches `https://advisories.ncsc.nl/rss/advisories`, parses the RSS, extracts the `NCSC-YYYY-NNNN` ID from each title so the caller can chain into `ncsc-nl csaf <id>` for the full CSAF JSON. **Ends the speculative-ID-enumeration 404 rabbit-hole** that wasted sub-agent budget in 2026-05-12 / 2026-05-13 runs.
   - `ico-uk enforcement [N]` — fetches `https://ico.org.uk/sitemap.xml` (5 MB, ~30 K URLs), regex-filters the 206 `/action-weve-taken/enforcement/` entries, sorts by `<lastmod>` descending, returns top N as JSON with `{url, lastmod, year, month, slug}`. Caller chains into `url <url>` for the per-action body (which is server-rendered).
   - `sec-edgar 8k [start] [end] [item]` — queries SEC's EDGAR full-text search at `https://efts.sec.gov/LATEST/search-index?q=%22Item+<item>%22&forms=8-K&dateRange=custom&startdt=...&enddt=...`. Default item = 1.05 (cybersecurity-incident disclosure); default date range = trailing 14 days. Returns each hit with `{file_date, form, items, display_name, ciks, adsh, filing_url}` where `filing_url` is the canonical `https://www.sec.gov/Archives/edgar/data/<cik>/<adsh-nodash>/` URL the brief should cite. Sends the SEC-required identifying User-Agent suffix.

3. **`wayback <URL> [target-ts] [min-size]` — Wayback Machine fallback.** For Cloudflare-Managed-Challenge-protected publishers that reject every UA the bridge can construct, the subcommand queries Wayback's availability API + CDX index for a usable snapshot in the last 180 days, fetches it, strips Wayback's wombat-toolbar / analytics / URL-rewriting injection from the body, and returns publisher-clean HTML. Includes:
   - **Empty-snapshot detection**: Wayback's own "no snapshot" placeholder pages (~9 KB of `<title>Wayback Machine</title>` HTML) are rejected via marker-string detection — caller never gets a placeholder as if it were real content.
   - **Size filter**: default `min_size=5000` rejects Cloudflare empty-body captures (0–2 KB) which CDX often has interleaved with real snapshots.
   - **CDX 503 retry**: Wayback's CDX index rate-limits with HTTP 503; one 35-s retry covers the rate-limit window.
   - **From-strategy field**: tells the caller whether the snapshot came from the cheap availability API or the slower CDX walk, useful for ops telemetry.

   Verified on:
   - `inside-it.ch` → 2026-04-19 snapshot, 283 KB, German title preserved
   - `darkreading.com` → 2026-05-14 snapshot, 495 KB, fresh
   - `databreaches.net` → recent snapshot empty (Cloudflare body capture); CDX fall-through to 2025-11-26 snapshot, 187 KB with 74 article-like links. Out-of-window but available.
   - `www.coe.int/en/web/cybercrime` → 2026-05-13 snapshot
   - `group-ib.com`, `downloads.seppmail.com` → no usable Wayback snapshots; documented as WebSearch-only.

**`.claude/agents/cti-research.md` § Bridge fetcher rewritten.** New table separates structured discovery feeds (the `cert-eu recent` / `ncsc-nl recent` / `ico-uk enforcement` / `sec-edgar 8k` group) from per-host recipes. Adds explicit Wayback-fallback rows for Cloudflare-blocked hosts. Documents the empty-snapshot detection, size filter, recency caveat (Wayback snapshots may be days / weeks out-of-window — `snapshot_ts` is preserved verbatim so the agent applies PD-7 itself).

**Daily + weekly prompt banners — v2.52 → v2.53.** Banner-only bump; the sub-agent definition carries the operational changes per the v2.52 "bridge table lives in the sub-agent" refactor. The anti-fetch hard invariants (META #16 / W-INV-3) are unchanged — the main agent still does no source fetching during Phase 1 / Phase 2; the bridge improvements raise sub-agent fetch quality, not main-agent fetch scope.

### What stays
Every editorial invariant — AI-content notice, no IOCs, no vanity metrics, English output, two-source verification with national-CERT carve-out, feature-branch-only publishing chain, Phase 5.5 / 4.5 mechanical gate, mandatory at-least-one verification iteration, F1–F12 finding categories, per-item metadata footer using taxonomy values, memory commits, PD-1 through PD-13, the 5-iteration verifier cap with model rotation and early-exit on low-defect convergence. The main agent's anti-fetch invariants (v2.52 META #16 / W-INV-3) are unchanged. The fetch_failures rich shape, URL-liveness ledger, deterministic `run_id`, per-agent timestamp capture, verifier compact-summary contract are unchanged. The Phase 0 keys-only digest (v2.52) is unchanged. `tools/check_brief.py` is unchanged — the bridge improvements happen below the gate.

### Migration note for sub-agent callers
The `ncsc-nl recent` subcommand is **strongly preferred** over speculative `ncsc-nl csaf <guessed-id>` calls. The 2026-05-12 / 2026-05-13 runs wasted ~6 min total on 4 speculative IDs. Always `recent` first, then `csaf <id-from-recent>`.

The `cert-fr avis-recent` / `cert-fr actu-recent` / `cert-eu recent` / `ico-uk enforcement` subcommands likewise replace the v2.49 `url <listing>` recipe that returned SPA shells. The recipes for *per-advisory* URLs are unchanged — `url <per-advisory URL>` still works after the listing-driven discovery returns the link.

---

## 2.52 — 2026-05-15 (anti-classifier-trip: forbid main-agent source fetching during Phase 1/2, move bridge table + technical-depth taxonomy into sub-agent, keys-only digest for main agent)

### Why
Two consecutive routine runs (2026-05-13 daily, 2026-05-15 daily transcripts on file) died mid-Phase-2 with `API Error: ... violative cyber content ... blocked under Anthropic's Usage Policy` and **never wrote a brief** — the worst PD-1 (`Always write the file`) violation. The shared failure mode in both transcripts was identical:

1. Phase 0 completed cleanly — `run_id`, prior-coverage, state-summary, taxonomy reads.
2. Phase 1 sub-agents (S1–S4) launched in parallel — correct.
3. **Main agent then made its own background `python3 tools/fetch_source.py` and `WebFetch` calls in parallel with the sub-agents** — pulling NCSC-CH advisories, ANSSI vulnerability bulletins, ENISA EUVD exploited-CVE lists, ICO enforcement actions (one transcript even grepped the ICO sitemap with `enforcement|penalty|fine|breach|reprimand|monetary` terms) into main-agent context.
4. Four `API Error` returns in a tight burst killed the conversation. No commit, no push, no brief.

Forensic measurement of the main-agent context at the kill point:

- `prompts/daily-cti-brief.md` v2.50 — 987 lines / ~42 K tokens of dense CTI vocabulary (Kerberos / OAuth / SAML abuse names, exploit-class taxonomy, full bridge-fetcher table with every known-403 host's structured-endpoint subcommand, named-cluster prefix patterns, defender event-ID list).
- `prior_coverage.json` Read in Phase 0 — ~12 K tokens of CVE titles ("pre-auth RCE … KEV deadline …"), incident summaries with named victims and exploitation patterns, named ransomware-affiliate clusters, breach victim/sector pairs.
- `state-summary.json` — ~10 K tokens of CVE one-liners and item titles, similarly dense.
- The main agent's own background fetches of NCSC-CH / ICO / ANSSI / ENISA bodies — additional 20–40 K tokens of raw advisory + enforcement content.
- Classifier reads the cumulative content; once the density crossed threshold, every subsequent Bash / WebFetch / WebSearch tool call returned `API Error`.

The architectural defect: **the main agent was duplicating sub-agent work AND pulling raw security-advisory content into its own context** despite the prompt's *implicit* "sub-agents do the research" framing. The v2.50 prompt's bridge-fetcher table (with every known-403 host's structured-endpoint subcommand) read as a checklist that the main agent could helpfully run itself to "verify connectivity" or "pre-warm caches" — and it did, both runs. Implicit guidance was insufficient.

### What changed

**Three structural fixes, all in this release:**

**1. Anti-fetch guard #9 (daily) / #10 (weekly) — main agent does NO source fetching during the research phase.** New numbered anti-crash guard in both prompts naming `WebFetch` / `WebSearch` / `python3 tools/fetch_source.py` as forbidden while sub-agents are running. The only main-agent invocations of those tools are: Phase 2 spot-checks (one URL the sub-agent already cited), Phase 5.7 / Phase 4.7 verification-fix re-fetches (one URL the verifier flagged), Phase 7 / Phase 6 publish polling (`curl https://ctipilot.ch/`). Anything else: spawn another sub-agent. Hardened as META hard invariant #16 (daily) / W-INV-3 (weekly) — self-evolution authority cannot weaken it.

**2. Bridge-fetcher recipe table moved out of the main-agent prompts into [`.claude/agents/cti-research.md`](../.claude/agents/cti-research.md).** The v2.50 daily prompt's Phase 1 § Reinforced rules contained the full bridge allowlist (cisa-kev / cisa-{advisories,news,directives} / ncsc-ch-security-hub / enisa-euvd / bsi-de / advisories-ncsc-nl / anssi-fr / cert-eu / cert-pl / ncsc-uk / ico-uk / prodaft / bleepingcomputer / nccgroup / dragos / sygnia / talos / ccn-cert-es / acn.gov.it / inside-it-ch / databreaches-net) with per-host subcommand recipes. That table is now sub-agent-only — the main-agent prompts carry a one-paragraph pointer to the canonical location and the explicit reminder that the main agent never invokes the bridge during Phase 1 / Phase 2. Same content, different reader.

**3. `### Technical depth — what every item must include` taxonomy moved out of the main-agent prompts into [`.claude/agents/cti-research.md`](../.claude/agents/cti-research.md) § Technical depth.** The v2.50 daily/weekly prompts each carried a ~200-line prescriptive list of MITRE T-IDs (T1190 / T1059.001 / T1505.003 / T1557.001 / T1068 / T1078.004 / T1556.006 / T1611), Sysmon / Windows event IDs (1, 4624 Logon Type 9 for S4U2Self, 4663 on ntds.dit, 4769 ticket-request anomalies), identity-protocol abuse names (NTLM relay, OAuth device-code, SAML response forgery, S4U2Self), named-cluster patterns (UNC####, Storm-####, TA####, APT##, CL-###-####), and `auditd` syscall references. Both main-agent prompts now carry a short summary list (vulnerable component / technique class / prerequisites / affected versions / exploitation status / defender takeaway / sectors and regions) with a pointer to the sub-agent definition for the prescriptive vocabulary. The sub-agents apply the taxonomy at research time; the main agent composes from their returns and does not need the vocabulary in its prompt baseline.

**Token-budget consequence:** the daily prompt drops from ~42 K tokens to an expected ~32 K (bridge table removed, technical-depth taxonomy removed); the weekly drops from ~32 K to ~25 K. The classifier reads the whole conversation, so a 10 K-token reduction in the prompt baseline frees that much headroom for sub-agent returns and composition before the cumulative-content threshold is reached.

**4. `tools/build_prior_coverage.py` emits a keys-only companion file** (`work/<run-id>/prior_coverage_keys.json`) alongside the full `prior_coverage.json`. The companion file carries `{key, date, brief_path, section}` per record — no titles, no tldrs, no primary-source URLs. The main agent's Phase 0 step 2 / weekly Phase 0 step 4 now `Read`s the keys-only file (~4 KB / ~1 K tokens) instead of the full file (~50 KB / ~12 K tokens). Sub-agents continue reading the full file in their isolated contexts for fetch-time PD-8 dedup against prior titles + URLs. Main-agent token budget drops another ~8 K vs v2.50. On-demand `jq` extraction of a specific record from the full file is documented for the rare cases where Phase 4 composition needs to quote a prior brief's primary URL.

**5. Verifier definitions** ([`.claude/agents/cti-verification.md`](../.claude/agents/cti-verification.md), [`.claude/agents/cti-verification-alt.md`](../.claude/agents/cti-verification-alt.md)) — check #10 (Clarity) gains a one-line ground-truth reference to `.claude/agents/cti-research.md` § Technical depth as the standard for "enough technical depth". Both verifier definitions edited in lockstep (byte-equivalent bodies preserved).

### What stays
Every editorial invariant — AI-content notice, no IOCs, no vanity metrics, English output, two-source verification with national-CERT carve-out, feature-branch-only publishing chain, Phase 5.5 / Phase 4.5 mechanical self-check gate, mandatory at-least-one verification iteration, 5-iteration verifier cap with model rotation, F1–F12 finding categories, per-item metadata footer using taxonomy values from `site/taxonomy.yaml`, memory commits, fetch_failures rich shape, URL-liveness ledger, deterministic `run_id`, per-agent timestamp capture, verifier compact-summary contract, early-exit on low-defect convergence — is unchanged. PD-1 through PD-13 unchanged. The 30-min sub-agent wall-clock cap unchanged. The sub-agent research contract unchanged (same `**Model:**` + `**Timestamps:**` self-identification, same Discovery-trace shape, same `Sources:` block, same `## Coverage gaps` and `## Fetch failures` sections, same per-CVE-table return shape for S1). `tools/check_brief.py` is unchanged — the prompts moved content around the script, not the gates the script enforces. The full `prior_coverage.json` is still on disk for the sub-agents to read; only the main agent's `Read` target changed.
## 2.51 — 2026-05-15 (sources.json schema gate: canonical candidate shape + `tools/check_brief.py` mechanical validator)

### Why
The 2026-05-15 daily routine added a new candidate source (`depthfirst`) to `sources/sources.json` with `"category": "research"` (string) instead of `["research"]` (list). Every other entry in the file uses a list, and `site/build.py` iterates `category` everywhere it touches a source (`s.get("category") or []` patterns) — when the value is a string, Python iterates it character-by-character, producing wrong category tags or crashing the `+` between str and list. The brief itself passed `tools/check_brief.py` (the schema was never checked) and `site/build.py` (the routine doesn't run the full build pre-commit), but the `deploy-site.yml` GitHub Actions workflow that rebuilds `gh-pages` on every push to `main` then failed — the brief was on `main` but the public site at `https://ctipilot.ch/` did not rebuild. A follow-up commit patched the data (`a624ff2`) and added a defensive helper for the related run-log shape drift; this changelog entry covers the **preventive** side.

The root cause is that the source-add bullet under Phase 5 → `sources/sources.json` was under-specified: it instructed the autonomous routine to "append `status: "candidate"`, `notes: "discovered YYYY-MM-DD via {source-id}"`" with no example, no field list, no shape rules. The routine pattern-matched the surrounding entries inconsistently — caught `category`, dropped from a list to a string, used `name` instead of `publisher`, omitted `reliability` / `language` / `fetch_method` / `consecutive_failures`. A clearer prompt would have prevented this regression; a mechanical gate guarantees the next drift is caught before push, not after deploy.

### What changed

**`tools/check_brief.py` — new `check_sources_schema()` check, wired into the Phase 5.5 gate**. Reads the parsed `sources/sources.json` from `check_state_json_valid()` and validates every source entry against an explicit schema:

- **Top-level** must contain `schema_version`, `categories`, `reliability_tiers`, `statuses`, `fetch_methods`, `sources`.
- **Every source FAILs the commit on**:
  - missing or non-string `id`; duplicate `id`; missing or non-http(s) `url`;
  - missing `category` **or** `category` that is not a JSON list (★ the 2026-05-15 regression);
  - empty `category`; `category` value not in the top-level `categories` vocabulary;
  - missing `status` or `status` not in `{active, candidate, demoted}`;
  - missing `publisher` (including entries that wrote `name` instead — surfaced explicitly so the autonomous routine sees the rename);
  - missing `notes`;
  - `active` or `demoted` source missing `reliability` / `fetch_method` / `language` / `consecutive_failures`, or with unknown vocab values;
  - `language` not a non-empty list of strings; `consecutive_failures` not an int; `last_successful_fetch` not a YYYY-MM-DD string or null.
- **WARN-only advisory**: candidate source missing recommended `publisher` / `reliability` / `language` / `fetch_method` — the candidate is not blocking, but the prompt now describes the canonical candidate shape so this warning shouldn't fire on routine adds.

The check is invoked from `run_checks()` directly after the existing `check_sources_touched_today()` so the schema gate and the bookkeeping gate share the same parsed view. Both run for daily and weekly briefs (the schema check is brief-kind-agnostic — it validates the file, not the brief).

**`prompts/daily-cti-brief.md`** — Banner v2.50 → **v2.51**. Phase 5 → `sources/sources.json` rewritten: the one-line "Discovery → candidate" bullet expanded to a **canonical candidate JSON template** with every field, the documented type for each, the controlled-vocab pointer for `category` / `status` / `reliability` / `fetch_method`, and four explicit "hard shape rules" — `category` is always a list (even with one value), the field is `publisher` (never `name`), vocab values must come from the top-level dicts, every active/demoted source carries the full field set. Closes with an explicit reference to the `sources-schema` check so a reader looking for the source of truth follows the link to `tools/check_brief.py`.

**`prompts/weekly-summary.md`** — Banner v2.50 → **v2.51** (lockstep). The Phase 4 `sources/sources.json` paragraph gains a pointer to the daily prompt's canonical-candidate template + the `sources-schema` check name, so a weekly-only reader doesn't miss the gate.

**`sources/sources.json`** — `depthfirst` entry brought to the canonical candidate shape: renamed `name` → `publisher`, added `reliability: "MEDIUM"` (genuine but unproven), `language: ["en"]`, `fetch_method: "webfetch"`, `consecutive_failures: 0`, dropped the redundant `added` field (date is already in `notes`), kept `category: ["research"]` (the list shape patched in `a624ff2`). Now passes `sources-schema` cleanly.

### What stays
- Every existing source-lifecycle rule (one new candidate per run, append-only `notes`, `consecutive_quiet_periods` content-only demotion, transport-error 403/429/503/5xx never demotes, etc.) is unchanged. v2.51 specifies the **shape** of the entry the routine writes; the **lifecycle** of the source is the same as v2.50.
- The four state files + `sources/sources.json` continue to auto-resolve on `origin/main` sync (`state/*` → ours, `sources/sources.json` → theirs). The schema check runs against the local merged view, so a conflict-driven shape regression on either side would be caught.
- The verification sub-agent contract is untouched — `sources-schema` is a mechanical gate, not an editorial concern.


---

## 2.50 — 2026-05-11 (token-budget guards: prior-coverage + state-summary scripts, verifier compact-summary contract, early-exit on low-defect convergence)

### Why
The 2026-05-11 weekly run hit the main-agent token limit *during Phase 0* — before Phase 1 even started. Forensic measurement of that run's input footprint:

- `prompts/weekly-summary.md` — 83 KB / ~32 K tokens (master prompt itself)
- 5 daily briefs in window — ~340 KB / ~85 K tokens combined (the 2026-05-09 and 2026-05-10 dailies are individually 28 K + 29 K tokens, each above Read's 25 K limit, so each had to be re-read in chunks)
- `state/covered_items.json` — 100 KB / ~25 K tokens (89 items, growing weekly)
- `sources/sources.json` — 84 KB / ~21 K tokens (114 sources)
- `state/run_log.json` — 35 KB / ~9 K tokens

Total Phase 0 input: ~120 K tokens *before* dedup-context build, *before* W1/W2 spawn, *before* composing the brief skeleton. The verifier loop adds ~50 K more tokens across 5 iterations (each iteration's full report read into main context). The main agent runs out of working budget partway through the run.

The user-reported diagnosis ("too many sub-agents") was wrong — the load is *all* in the main agent's reads of the prompt + dailies + state files + verifier outputs. Sub-agents have isolated context and don't compete for the main agent's budget.

### What changed

**NEW — `tools/build_prior_coverage.py`** — replaces the prompt's instruction "the main agent walks every H3 in §§ 0–6 of every brief in the window". Walks the gap-window dailies + previous weekly via the same Markdown structure the existing prompt assumes, emits `work/<run-id>/prior_coverage.json` with `{key, title, tldr_one_line, primary_source_url, date, brief_path, section}` per H3. The full-record output is ~50 KB / ~12 K tokens for a 7-day window, vs ~340 KB / ~85 K tokens for full daily-brief Reads. Adds `--keys-only` mode (~12 KB / ~3 K tokens) for when even the tldrs are more than the main agent needs. Same script serves both the main agent's Phase 0 and the existing PD-8 enforcement-at-fetch-time use the prompts already mention.

**NEW — `tools/run_summary.py`** — emits `work/<run-id>/state-summary.json`: `cves.{count, ids[], recent[]}`, `items.{count, keys[], recent[]}`, `sources.{active_count, active_ids[], demoted_ids[], candidate_ids[]}`, `runs.{count, last_run, fetch_gaps_in_window[]}`. Output is ~40 KB / ~10 K tokens, vs ~230 KB / ~57 K tokens for full reads of `state/covered_items.json` + `state/cves_seen.json` + `state/run_log.json` + `sources/sources.json`. Pre-computes the `fetch_gaps_in_window` list (sources flagged as failing in ≥ 2 of the last 7 runs) so the main agent doesn't manually scan run-log entries to build the rotation-priority list.

**`prompts/daily-cti-brief.md` — Banner v2.49 → v2.50.** Phase 0 rewritten:
- Old: "1. `Read sources/sources.json`. 2. List `briefs/`; read every brief from last 7 days … 3. `Read state/covered_items.json`, …, 7a. **Generate `work/<run-id>/prior_coverage.json` …** [agent walks every H3 by hand]."
- New: "1. **Generate the structured H3-record + state digests via scripts (MANDATORY — token-budget guard).** `python3 tools/build_prior_coverage.py "$RUN_ID" 7` and `python3 tools/run_summary.py --out work/$RUN_ID/state-summary.json`. 2. **`Read work/$RUN_ID/prior_coverage.json`.** 3. **`Read work/$RUN_ID/state-summary.json`.** 4. `Read site/taxonomy.yaml`. 5. **Optional on-demand reads** for specific items (Read by date for full body; `jq` for full state record)."
- Token-budget reduction: full-Read approach ~120 K tokens before Phase 1; script-based approach ~30 K tokens. The full state files and brief bodies are still on disk for sub-agents to Read directly.

**`prompts/weekly-summary.md` — Banner v2.49 → v2.50.** Phase 0 rewritten with the same shape: invoke `tools/build_prior_coverage.py "$RUN_ID" "$WINDOW_DAYS"` and `tools/run_summary.py --out work/$RUN_ID/state-summary.json` instead of "read every daily brief whose date falls within the gap-derived window" + four full-state Reads. `WINDOW_DAYS` is exported by step 2 (gap-derived window computation) so step 3 picks it up. The weekly's 7-day window with previous-weekly include emits a slightly larger `prior_coverage.json` (~88 KB / ~22 K tokens vs ~12 K for the daily) but still cuts ~80 % off the full-Read approach.

**`.claude/agents/cti-verification.md` + `.claude/agents/cti-verification-alt.md` — verifier compact-summary contract.**
- The verifier now persists its full structured report to `work/<run-id>/verification.iter<N>.md` (Markdown) and the machine-readable findings to `work/<run-id>/verification.iter<N>.findings.yaml` (sibling YAML).
- The verifier's response to the spawn call is a compact ~150-token summary block: `**Model:**`, `**Timestamps:**`, `**Verdict:** CLEAN | NEEDS_FIXES`, `**Counts:** truth=N editorial=N advisory=N`, `**Report:** <path>`, `**Findings summary path:** <path>`, `**Self-telemetry:** …`.
- The main agent stamps the summary lines into `state/run_log.json.verification.iterations[<N>]` directly and reads the persisted files only on-demand when applying remediations or surfacing the cap-breach iteration's `findings[]`.
- 5 iterations × ~6 KB report = ~30 K tokens of main-agent context in v2.49 → ~750 tokens in v2.50.

**Verifier loop early-exit (v2.50, both prompts).** The cap remains 5 as the safety valve, but the loop SHOULD exit early when the verifier returns NEEDS_FIXES with `truth + editorial ≤ 2` AND no F1 (broken URL) / F4 (hallucinated fact) finding. Empirically the 2026-05-10 weekly trace showed iter-1 = 17 truth + 6 editorial → iter-2 = 7 + 5 → iter-3 = 10 + 1 → iter-4 = 2 + 1 → iter-5 = 0 + 0; iter-3 onward chased edge-case URL UA-blocking and framing-precision findings rather than substantive defects. The early-exit publishes after iter-3 in that pattern, freeing iter-4 / iter-5 budget. Decision rules in priority order: CLEAN → publish; F1/F4 present → re-spawn always; truth+editorial ≥ 3 → re-spawn; truth+editorial ≤ 2 with no F1/F4 → publish with residuals logged; iter 5 → publish anyway (original safety valve).

### What stays
Every editorial invariant — AI-content notice, no IOCs, no vanity metrics, English output, two-source verification with national-CERT carve-out, feature-branch-only publishing chain, Phase 5.5 / 4.5 self-check gate, mandatory at-least-one verification iteration, per-item metadata footer using taxonomy values, memory commits — is unchanged. The verifier's gatekeeper framing, F1–F12 finding categories, 30-min hard cap, anti-hallucinated-findings clause, and read-only tool set are unchanged. The mechanical gate (`tools/check_brief.py`) runs in the same place. The fetch_failures rich shape, URL-liveness ledger, deterministic run_id, and per-agent timestamp capture are unchanged. **The full state files and brief bodies remain on disk** — sub-agents Read them directly when they need the full data; only the main agent's transient working context is freed.

The 5-iteration cap stays; the early-exit is an additive shortcut that doesn't override the safety valve. F11 advisory items still don't block CLEAN.

---

## 2.49 — 2026-05-11 (bridge-fetcher bug fixes: re-import, ENISA EUVD host correction, BSI WID full-body via CSAF, NCSC-NL CSAF distribution path correction, CF-blocked + SPA-only recipes documented)

### Why
Six defects in `tools/fetch_source.py` and the bridge-allowlist recipe table surfaced across the 2026-05-11 daily run's `fetch_failures` ledger:
1. **NameError on `re`.** `tools/fetch_source.py` called `re.match(...)` from `ncsc_nl_csaf` and `enisa_euvd_advisory` without importing the `re` module. Both subcommands crashed with `NameError: name 're' is not defined` on every invocation — every S1 / S2 attempt to fetch a Dutch-NCSC CSAF advisory or look up a specific EUVD entry failed at the validation step.
2. **ENISA EUVD endpoints empty.** The v2.48 paths `https://euvd.enisa.europa.eu/enisaeuvd/api/{criticals,lastvulnerabilities,exploited,vulnerability/<id>}` now route through the SPA's catch-all and return the React shell (HTTP 200, `text/html`, ~900 bytes) instead of JSON. `fetch_json` surfaced this as an unparseable body. The actual EUVD API lives on a separate publisher host, `https://euvdservices.enisa.europa.eu`, with different path names (`/api/criticalvulnerabilities`, `/api/exploitedvulnerabilities`, `/api/lastvulnerabilities`, `/api/enisaid?id=<EUVD-ID>`).
3. **BSI WID per-advisory pages unreadable.** `wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-YYYY-NNNN` is an Angular SPA — every tool ctipilot has access to gets the empty `<app-root>` shell. The v2.48 bridge recipe `bsi-rss` then `url <per-advisory URL>` gave the agent the RSS list (title + short summary) but no advisory body. A structural gap that surfaced every time a BSI advisory was the only EU national-CERT signal on a vulnerability.
4. **NCSC-NL CSAF URL pattern wrong.** The v2.48 bridge constructed `https://advisories.ncsc.nl/advisory/<id>/v<n>/<id>.json` — every variant 404s. Publisher's actual TLP:WHITE CSAF distribution (advertised at `/.well-known/csaf/provider-metadata.json`) serves each advisory at `https://advisories.ncsc.nl/csaf/v2/{year}/ncsc-{year}-{nnnn}.json`. The legacy `version` parameter is no longer in the URL — only the latest revision is published at the deterministic path.
5. **inside-it.ch + databreaches.net Cloudflare Managed Challenge.** Both hosts are now behind Cloudflare's "Just a moment..." challenge that refuses every UA the bridge can construct (Chrome desktop, curl, Mozilla/5.0, Googlebot all return 403 with the challenge body). The v2.48 recipe `url <URL>` would still fail. The cloud routine container has no path to a JS-rendering shell and cannot reach `web.archive.org` (egress policy block), so there is no in-container workaround — these hosts require WebSearch fallback. Marking them explicitly stops the agent from burning fetch budget on the bridge before falling through.
6. **prodaft `/blogs` + ico.org.uk `/action-weve-taken/enforcement/` JS-rendered listings.** Both publishers serve the listing page as a client-rendered shell but the per-item URLs (per-post for prodaft; per-action for ICO) are server-rendered, and both expose a server-rendered `sitemap.xml` that enumerates the per-item URLs. The v2.48 recipe `url <URL>` against the listing returned an empty SPA shell; the working recipe is sitemap-then-per-item, which the routine already supports via `url <sitemap>` since both hosts are on `ALLOWED_HOSTS`.

### What changed

**`tools/fetch_source.py`** — five hotfixes, behaviourally additive:
- Added `import re` (the actual NameError fix).
- `ENISA_EUVD_BASE` → `ENISA_EUVD_API_BASE` pointing at the services host `https://euvdservices.enisa.europa.eu`; `enisa_euvd_recent` maps the CLI kind vocabulary (`lastvulnerabilities`, `criticals`, `exploited` — unchanged for back-compat with prompts) to the publisher path names (`/api/lastvulnerabilities`, `/api/criticalvulnerabilities`, `/api/exploitedvulnerabilities`); `enisa_euvd_advisory` rewritten to use `/api/enisaid?id=<ID>`. New host `euvdservices.enisa.europa.eu` added to `ALLOWED_HOSTS`.
- **NEW subcommand `bsi-csaf <WID-SEC-YYYY-NNNN>`** — fetches the per-advisory CSAF v2.0 JSON document from BSI's CSAF Trusted Provider distribution (`https://wid.cert-bund.de/.well-known/csaf/white/{YEAR}/wid-sec-w-{YEAR}-{NUM}.json`, derived from the portal-style ID). The CSAF document contains the full advisory body: title, all `notes` (Produktbeschreibung / Angriff / Maßnahmen), `product_tree`, every CVE in `vulnerabilities[]`, CVSS scores, remediations. The agent still cites the human-readable portal URL — the bridge provides the data, not the citation.
- `ncsc_nl_csaf(advisory_id, version)` rewritten to fetch `https://advisories.ncsc.nl/csaf/v2/{year}/ncsc-{year}-{nnnn}.json` (the publisher's well-known CSAF distribution). The `version` parameter is accepted for back-compat with v2.48 recipes but ignored — the deterministic path always serves the latest revision.
- `www.bleepingcomputer.com` / `bleepingcomputer.com` added to `ALLOWED_HOSTS` so listing-level discovery (200 on desktop UA) works through the bridge. Article-level URLs frequently 403 — the recipe documents WebSearch fallback for content. New `CLOUDFLARE_BLOCKED_HOSTS` constant flags inside-it.ch + databreaches.net so future code can branch on it; the routine prompt currently uses this only as documentation, not as a programmatic switch.

**`prompts/daily-cti-brief.md`** — Banner v2.48 → **v2.49**. The "MANDATORY bridge allowlist" table:
- BSI row: `bsi-rss` then `url <per-advisory URL>` → `bsi-rss` then `bsi-csaf <WID-SEC-YYYY-NNNN>`, with an explicit "do NOT `url` it" note.
- NCSC-NL row: `[version]` argument removed; recipe simplified to `ncsc-nl csaf <NCSC-YYYY-NNNN>`; URL pattern documented inline.
- New row for `ico-uk`: sitemap-then-per-action discovery recipe.
- New row for `prodaft`: sitemap-then-per-post discovery recipe.
- New row for `bleepingcomputer`: listing-level discovery + WebSearch fallback for content.
- New row for `inside-it-ch` + `databreaches-net`: explicit "WebSearch fallback only" — bridge attempt records the 403 in `fetch_failures` but the host is behind Cloudflare's Managed Challenge.

**`prompts/weekly-summary.md`** — Banner v2.48 → **v2.49** (lockstep). The weekly prompt references the daily table by name so no body edit was needed.

**`.claude/agents/cti-research.md`** — Same row updates on the sub-agent's bridge table. The `WebFetch outbound-links template` contract, the `fetch_failures` rich-shape rules, the URL-liveness ledger, and the self-identification mechanics are all unchanged.

### What stays
Every v2.48 invariant. The bridge-first rule for known-403 / SPA-only hosts. The rich `fetch_failures` schema and Phase 5.5 / Phase 4.5 enforcement (recording the 403 / CF-challenge outcome is still mandatory — the rule shift is only that for `inside-it-ch` / `databreaches-net` the `mitigation_applied` field is `"WebSearch fallback (Cloudflare Managed Challenge — bridge cannot bypass)"` instead of an empty mitigation). The per-finding `verification.iterations[].findings[]` shape. The 5-iteration verifier cap with model rotation, the 30-min sub-agent cap, the dual-gate model (`check_brief.py` → `cti-verification`). The CLI vocabulary for `enisa-euvd recent` is preserved (`lastvulnerabilities`, `criticals`, `exploited`) so existing recipes and run-log entries keep working. Every PD-1 → PD-13 prime directive.

---

## 2.48 — 2026-05-10 (bridge fetcher expanded to all known-403 / SPA-only sources, rich `fetch_failures` schema, per-finding verification detail, /sources/ owns stale-source surface)

### Why
Operator review of the v2.47 2026-05-10 run flagged seven sources where the routine recorded `fetch_failures` but the entries were too thin to debug — `cisa-kev 403`, `ncsc-ch-security-hub 403`, `enisa-euvd 200` (SPA empty), `wid.cert-bund.de 200` (RSS-only), `advisories.ncsc.nl 200` (CSAF SPA), `databreaches-net 403`, `ico-uk` — and noted that the agents should be using the bridge fetcher for most of them but weren't. The verification-iteration records also lacked per-finding detail, so the operator couldn't see WHAT the verifier flagged in the cap-breach iteration without reading the brief's § 7. And the Ops dashboard's "Stale active sources (>7 days since last successful fetch)" panel duplicated information already on /sources/ — the operator wanted it consolidated alongside reliability and status. v2.48 fixes all four.

### What changed

**`tools/fetch_source.py`** — `ALLOWED_HOSTS` expanded with eight new hosts: `euvd.enisa.europa.eu` (ENISA EUVD SPA), `wid.cert-bund.de` (BSI cert-bund), `advisories.ncsc.nl` + `www.ncsc.nl` + `ncsc.nl` (Dutch NCSC), `www.cert.ssi.gouv.fr` + `cert.ssi.gouv.fr` (CERT-FR — per-advisory pages need browser UA), `cert.europa.eu` + `www.cert.europa.eu` (CERT-EU), `cert.pl` + `www.cert.pl` (CERT-PL), `www.ncsc.gov.uk` + `ncsc.gov.uk` (NCSC-UK). Three new structured-endpoint subcommands so the bridge fetches the underlying JSON / RSS rather than the SPA shell:
- `enisa-euvd recent {lastvulnerabilities|criticals|exploited}` and `enisa-euvd advisory <id>` against `/enisaeuvd/api/...`
- `bsi-rss` against `/content/public/securityAdvisory/rss`
- `ncsc-nl csaf <NCSC-YYYY-NNNN> [version]` against `/advisory/<id>/v<n>/<id>.json`

**`prompts/daily-cti-brief.md`** + **`prompts/weekly-summary.md`** — Banner v2.47 → **v2.48**. The "MANDATORY for CISA + NCSC.ch" rule extended to the full bridge allowlist with an explicit table of subcommands per source. **`fetch_failures` schema rewritten as a rich shape**: `{id, url_tried, fetch_method, status_code, error_class, error_message, attempted_methods, mitigation_applied, covered_anyway}` per entry — the legacy `{id, code}` shape still parses but the dashboard renders it as a yellow "needs-detail" row. Sub-agents are now required to record EVERY transport / SPA-empty / paywall / unusable-body outcome regardless of whether they recovered, so the audit trail captures the recovery chain itself. **`verification.iterations[]` schema gains `findings[]` array** (per-finding records: code, category, section, item, url_or_quote, summary, remediation_applied, remediation_outcome) so the cap-breach iteration shows on /ops/ exactly what the verifier flagged and what the main agent did about it (or didn't).

**`tools/check_brief.py`** — three new validation rules on the rich shapes (back-compat WARN on legacy v2.47 entries):
- `fetch-failure-detail` (WARN) — `fetch_failures[]` entry missing one of `url_tried`, `fetch_method`, `error_class`, `attempted_methods`, `mitigation_applied`, `covered_anyway` → flag for upgrade.
- `fetch-failure-bridge-required` (FAIL) — entry whose `id` matches a bridge-allowlisted source AND whose `attempted_methods` does NOT contain a `bridge:*` method.
- `verification-finding-detail` (WARN) — final-iteration `verdict: NEEDS_FIXES` without a populated `findings[]` array.

**`site/build.py`** — Ops dashboard rewrite of the latest-run + recent-runs sections to render the rich `fetch_failures` shape (one row per entry showing url_tried, the method chain, error_class + error_message, mitigation, recovery outcome) and the per-finding detail of the FINAL verifier iteration (the cap-breach signal). The "Stale active sources (>7 days since last successful fetch)" panel **REMOVED from /ops/** and reborn as a dedicated section on `/sources/` alongside reliability and status — same data, but co-located with the source-lifecycle context (status: active/candidate/demoted, reliability: HIGH/MEDIUM/LOW, last_successful_fetch, consecutive_quiet_periods, consecutive_fetch_failures). The `/sources/` filter chips gain a "Stale" toggle that filters to sources >7 days silent.

### What stays
Every v2.47 invariant. Every PD-1 → PD-13 prime directive. The dual-gate model (Phase 5.5 mechanical → Phase 5.7 verifier-as-gatekeeper). The 5-iteration verifier cap with model rotation. The 30-min hard cap on sub-agents. CSP, vendored-library SHA-256 integrity, no IOCs, no vanity metrics, English output. The feature-branch-only publishing chain. The repo-resident `.claude/memory/`. The eleven-feed RSS surface and the /trends/, /feeds/, editorial-choices, per-item-delta, actor-timeline site additions from v2.47. The `/ops/` dashboard's KPI tiles, models donut, sub-agent heatmap, verification-iteration timeline, recent-runs table.

---

## 2.47 — 2026-05-10 (cap-breach yellow signal + residual-count semantics, prior-coverage records to sub-agents, env-var self-identification, deterministic run_id, URL-liveness cache, verifier model rotation, F12 single-source-flag finding, three new mechanical checks, dropped-items-end site rendering, per-item delta site rendering, /trends/ dashboard, actor-timeline strips, sector-RSS slices, source-candidate + source-health tooling)

### Why
Senior-architect review over the v2.46 routine surfaced a coherent set of follow-on improvements without re-litigating any of v2.46's choices. The improvements fall in three buckets: (1) **brief-quality** — silent acceptance of iteration-cap publishes (the run-log records `verification_residual_count: 0` even when the final iteration returned NEEDS_FIXES), sub-agent dedup blind spots (sub-agents only get headline / first-paragraph dedup context, not full prior-coverage records — so they can spend fetch time on items the main agent will later drop), TL;DR bullets that lead with US-only KEV-deadline framing despite v2.44 PD-13, aggregator-only-sourcing items that meet the literal two-source bar but lack any primary, missing `[SINGLE-SOURCE]` flags, sub-agent self-identification drift (Sonnet 4.5 friendly name with `claude-sonnet-4-6` model id); (2) **architectural** — verifier-model homogeneity per run (every iteration uses the same model so model-specific blind spots silently inherit), non-idempotent state writes (a Phase-6 retry can re-append a duplicate `run_log` entry under a fresh `run_id`), URL-liveness check noise (sub-agents successfully fetched a URL but `tools/check_brief.py` re-fetches and trips an SSL-cert / anti-bot 403); (3) **features** — per-item "what changed since first coverage" deltas on the site (data already in `covered_items.json.appearances[].delta_summary`), cross-brief threat-class trend dashboard (data already in every brief footer), actor-activity timelines on entity pages, sector-specific RSS feed slices, source-candidate suggestion engine (cited-but-not-in-`sources.json` domains), and a weekly source-health GitHub Action that exercises every active source independently of the routine's daily fire. The v2.7 site renders an "Editorial choices" block at the end of every daily brief — drop reasoning that previously lived only in § 7's prose now surfaces as a discoverable, distinct collapsed block under the brief body. The "do not implement" subset of the original review list (operator-feedback UI, bilingual DE/FR, continuity-of-coverage, comparison-vs-commercial) was excluded by the operator and is not part of this release.

### What changed

**`prompts/daily-cti-brief.md`** — Banner v2.46 → **v2.47**. Phase 0 now generates `work/<run-id>/prior_coverage.json` from the last 7 daily briefs (full per-H3 records: key, title, one-line tl;dr, primary-source URL, date) and the spawn message to every Phase 1 sub-agent carries it as `prior_coverage_records: <count>` plus the path; the sub-agent reads the file and dedups against full records before fetching, not after (PD-8 enforcement at sub-agent fetch time, not just main-agent Phase 2 dedup). New `run_id` rule: deterministic — `<YYYY-MM-DD>-<sha8>` where the sha8 is the first 8 hex of `sha256("<brief_path>|<started>")`; Phase 5 refuses to write a run_log entry whose run_id already exists (idempotent retry). New URL-liveness cache: every sub-agent's successful `WebFetch` of a Source URL writes one line `<url>\t<status>\t<fetched_at_iso>` into `work/<run-id>/url-liveness.tsv`; Phase 5.5's check_brief.py now reads this file and skips its own HEAD/GET on URLs already verified within the run. Phase 5 state-update writes the verifier's residual count correctly: `verification_residual_count` = `truth + editorial` count of the **final** iteration if its verdict is `NEEDS_FIXES`, else 0 (advisory ignored — F11 doesn't block CLEAN). Phase 5.7 now rotates verifier sub-agent on iteration: odd iterations spawn `cti-verification` (Opus), even iterations spawn `cti-verification-alt` (Sonnet) — same operational system prompt, same return contract, different model runtime so model-specific blind spots are caught across iterations. Self-identification — both sub-agent prompts (research and verification) now read `CLAUDE_FRIENDLY_NAME` and `CLAUDE_MODEL_ID` env vars from the harness via Bash and emit them verbatim in the `**Model:**` line; falls back to "reason about your identity" when env vars are unset. Operator sets these env vars in the routine's harness configuration (see `docs/operating.md`).

**`prompts/weekly-summary.md`** — Banner v2.46 → **v2.47**. Same structural changes scoped to weekly: prior-coverage records pass to W1/W2 sub-agents; deterministic `run_id`; URL-liveness cache; verification rotation; env-var self-identification.

**`prompts/verification.md`** — New F12 finding category: `single-source item missing [SINGLE-SOURCE] flag`. Promoted from "the gatekeeper sometimes catches" to a numbered finding so the verifier consistently flags items with a single non-national-CERT source that don't carry the explicit reader-visible `[SINGLE-SOURCE]` marker.

**`.claude/agents/cti-research.md`** — New § Self-identification — read CLAUDE_FRIENDLY_NAME / CLAUDE_MODEL_ID env vars from harness; new § URL-liveness ledger — append every successful WebFetch source URL to `work/<run-id>/url-liveness.tsv`. Spawn-contract docs updated to mention `prior_coverage_records` as a passed input.

**`.claude/agents/cti-verification.md`** — Same env-var self-identification rule. F12 added to the F1–F11 finding categories. Iteration-rotation note: don't assume you're running on the same model as the previous iteration; the main agent rotates per-iteration.

**`.claude/agents/cti-verification-alt.md`** — NEW. Identical body to `cti-verification.md` but with `model: sonnet` in the YAML frontmatter (vs. `model: opus`). The Phase 5.7 main-agent loop spawns this on even iterations to rotate verifier model and catch single-model blind spots.

**`tools/check_brief.py`** — Three new checks added (matching the v2.47 prompt):
- **`tldr-deadline-lead`** (WARN) — TL;DR bullet whose first ~120 chars contain "KEV deadline" / "remediation deadline" / "CISA deadline" but does NOT contain `exploited|exploitation|in-the-wild|ITW|active|victim|impacted|exposed` → flag for reframe (PD-13 mechanical enforcement at the bullet level).
- **`aggregator-only-sourcing`** (WARN) — § 1 / § 2 / § 3 item whose Source field has ≥2 URLs all matching the news-aggregator hostname allowlist → flag as `reduced confidence — only aggregator sources` so § 7 must reflect this.
- **`single-source-flag`** (WARN) — item whose Source field has exactly 1 URL and isn't a national-CERT primary disclosure (carve-out) but the heading lacks `[SINGLE-SOURCE]` → flag.
- **`cap-breach`** (WARN) — `verification.iterations[]` ends on `NEEDS_FIXES` → flag as cap-breach with the residual finding count; the `run-log-verification-residual` check now derives the expected count from the final iteration's truth+editorial sum and FAILs on a mismatch.
- **URL-liveness cache integration** — when `work/<run-id>/url-liveness.tsv` exists, the live HEAD/GET check trusts it for any URL the sub-agents successfully fetched within the run (cuts SSL-cert / anti-bot 403 noise on URLs the agent has already verified).

**`site/build.py`** — Five additions:
- **Editorial-choices block at end of brief** (§ 2.7) — items dropped or held back, parsed from § 7 Verification Notes' "Items dropped" / "Items dropped or held back" / "Items dropped from Phase 2 Candidates" sub-headings, render as a single collapsed `<details class="editorial-choices">` block at the very bottom of the brief page (after § 7, after the cited footer). Not in TL;DR, not in the body — visible only after the editorial signal the brief was choosing.
- **Per-item "Changes since first coverage" inline block** (§ 3.5) — for any item whose CVE / topic key appears in `covered_items.json` with `len(appearances) > 1`, render an inline `<details class="item-deltas">` collapsible inside the item body listing prior `delta_summary` lines with their dates.
- **`/trends/` page** (§ 4.1) — bucket every brief footer's tags + sectors + regions by ISO week, render four sparklines (ransomware, vulnerabilities/actively-exploited, public-sector, OT/ICS) plus a heatmap of weekly tag frequency. Pure post-hoc analytics; no new state.
- **Actor-timeline strip on entity pages** (§ 4.2) — for entities of type `actor` / `campaign` / `incident` / `tool`, render a horizontal timeline strip above the existing Story timeline showing first-coverage → last-coverage with marker dots per appearance.
- **Sector-specific RSS feed slices** (§ 4.3) — `feed-public-sector.xml`, `feed-healthcare.xml`, `feed-finance.xml`, `feed-energy.xml`, `feed-ot-ics.xml`, `feed-defense.xml`, `feed-telco.xml`, `feed-education.xml`, `feed-government.xml`. Each is the per-item feed filtered by the corresponding `Sector:` value (or by `ot-ics` tag for OT/ICS).

**`tools/source_candidates.py`** — NEW. Walks the last 30 days of briefs, extracts every outbound link host, subtracts `sources/sources.json` ids and known-aggregator hosts, outputs the top-20 missing-but-cited domains with citation counts. Operator runs manually (or via cron). Pure post-hoc analytics; no runtime cost.

**`tools/source_health.py` + `.github/workflows/source-health.yml`** — NEW. Weekly cron (and `workflow_dispatch`) hits HEAD on every `status: active` source, records `(id, status_code, latency_ms, fetched_at)` to `state/source_health.json`. Records the rolling pattern so demotion logic can key off "consistently failing" vs. "intermittently failing" rather than the day-of-week luck of the routine's daily fire. The Ops dashboard surfaces this once `state/source_health.json` exists.

### What stays
Every v2.46 invariant. Every PD-1 → PD-13 prime directive. The dual-gate model (Phase 5.5 mechanical → Phase 5.7 verifier-as-gatekeeper). The 5-iteration verifier cap. The 30-min hard cap on sub-agents. The depth-over-speed research model with no fetch-call budget. Every hard-blocked source URL pattern. The feature-branch-only publishing chain with auto-merge action promotion to main. CSP, vendored-library SHA-256 integrity, no IOCs, no vanity metrics, English output. The `/cves/`, `/topics/`, `/entities/` legacy URL stubs and the unified `/entities/` canonical space. The repo-resident `.claude/memory/` and SessionStart symlink hook.

---

## 2.46 — 2026-05-10 (verifier model=opus, gatekeeper framing, 5-iter cap, mechanical gate runs first, 30-min sub-agent cap, depth-over-speed research, stricter recency)

### Why
Operator pass over the 2026-05-10 daily brief surfaced six related deficiencies: (1) the `cti-verification` sub-agent ran on Sonnet by default — the gatekeeper of publish quality should run on the heaviest model available; (2) Phase 4.5 (verification, expensive) ran *before* Phase 5.5 (`check_brief.py`, cheap) — the cheap mechanical gate should run first so the verifier doesn't spend its budget chasing structural defects the script already catches; (3) the 3-iteration verification cap was being treated as a target rather than a safety valve, with iteration 1 NEEDS_FIXES → iteration 2 NEEDS_FIXES → publish-with-residuals patterns showing up too often; (4) the verifier was not framed as a gatekeeper — it produced findings that went into iteration loops without the verifier knowing whether its CLEAN verdict was load-bearing; (5) sub-agents were soft-capped at 10 min with a ≤45-call fetch budget, biasing toward shallow runs; (6) source-date analysis on the 2026-05-10 brief showed zero same-day citations and 33 / 86 sources from 3+ days ago, with the recency window not being enforced strictly enough by either the research sub-agents or the main agent's Phase 2 verification pass. (Note: operator's "sources from 2023 / 2024 / 2025" reading was a misperception driven by `CVE-2025-XXXXX` numbers — CVE assignment year, not source publication year — but the underlying observation that source dates lag the brief by 2–3 days is real.) This release fixes all six in one commit.

### What changed

**`.claude/agents/cti-verification.md`** — `model: sonnet` → **`model: opus`** in the YAML frontmatter (the verifier is the gatekeeper of the publish gate; runs on the heaviest available model so its judgment is load-bearing). New "You are the gatekeeper" section at the top of the body explaining (a) the brief does not publish until verdict CLEAN unless the iteration cap is reached; (b) **fabricated / padded findings actively harm the run** — they push the brief through the cap without improving it. Verdict-block rewritten: CLEAN is the success outcome; NEEDS_FIXES counts must correspond to numbered findings with quoted evidence. Hard rules updated: 10-min runtime cap → **30-min hard cap** ("use the time"); explicit "do not pad findings" rule; clarification that the mechanical gate already covered cheap structural defects so the verifier can spend its budget on the slow expensive editorial + truth review. Iteration cap 3 → **5** (fail-open safety valve, not goal). Description in the YAML frontmatter updated for new phase numbers + cap.

**`.claude/agents/cti-research.md`** — Time-boxing: 10-min soft cap → **30-min hard cap** ("depth over speed — the main agent will not pre-empt you before that"). Operational guardrails: **dropped the ≤45 fetch-call budget entirely** ("no fixed fetch budget; budget is your wall-clock, not a count" — fetch as many sources as the domain warrants for deep pivots / corroboration / outbound-link traversal). New "Recency — fresh signal beats yesterday's news" section: anchor every in-window decision on `window_hours` from the spawn message; prefer today and yesterday over older; drop items whose freshest available source is outside the window unless they're an explicit § 4 UPDATE / Background paragraph / patch-reference exception; "empty is honest" is reaffirmed.

**`prompts/daily-cti-brief.md`** — Banner v2.45 → **v2.46**. Phase numbers: **Phase 4.5 (verification) renamed to Phase 5.7** and **moved physically below Phase 5.5 (self-check)** so the cheap mechanical gate runs first; Phase 5 (state update) moves up correspondingly with an intro explaining why state must be populated before the script reads `cves_seen.json` / `covered_items.json` / `run_log.json`. Phase 5.7 rewritten: 3-iter cap → **5-iter cap** (fail-open at 5, not goal); each iteration re-runs `check_brief.py` between fix and re-spawn; spawn message now carries `mechanical gate (check_brief.py) exited 0 in iteration N pre-spawn` so the verifier knows mechanical defects are out of scope; the `Drop` finding remediation now includes "re-update state — remove the matching `appearances[]` entry from `covered_items.json`, remove dropped CVEs from `cves_seen.json` if today was their only `last_seen`". Anti-crash guard #2: 10-min soft cap → **30-min hard cap** for every sub-agent (Phase 1 research, Phase 5.7 verification, Phase 5.7 follow-up research). Phase 1 / Phase 2 headings updated to "up to 30 min wall-clock each". PD-7 (Recency) gains a "**Recency enforcement (NEW emphasis)**" paragraph: stale-source drift is what makes the brief feel like yesterday's news; the gate is the sub-agent's recency filter + main-agent Phase 2 re-check, both anchored on `window_hours`. Phase 2 main-context check 6 rewritten as a recency re-check that drops out-of-window items to § 7 unless they fall under one of three documented exceptions. Quality gates checklist + hard invariants updated for new phase order, 5-iter cap, "check_brief BEFORE verifier" framing.

**`prompts/weekly-summary.md`** — Banner v2.45 → **v2.46**. Same structural changes scoped to weekly: **Phase 3.5 (verification) renamed to Phase 4.7** and **moved below Phase 4.5 (self-check)**; Phase 4 (state update) intro updated; Phase 4.7 cap raised to 5; sub-agent hard cap 30 min; PD-5 strengthened on source recency (sources must fall inside the gap-derived window unless they're explicit horizon / status-update content); checklist + invariants updated.

**`prompts/verification.md`** — Phase 4.5 references → Phase 5.7 (daily) / Phase 4.7 (weekly); 3-iter cap → 5-iter cap (with "safety valve, not goal" framing); the loop description now includes "re-run `python3 tools/check_brief.py`" between fix and re-spawn; preflight checklist now requires `check_brief.py` exits 0 *before* the verifier is spawned.

**`prompts/brief-template.md`** — `Phase 3.5 telemetry` reference in the weekly § 10 line → `Phase 4.7 telemetry`.

**`prompts/check-brief-fixes.md`** — Doc opener now states the script runs in Phase 5.5 (daily) / Phase 4.5 (weekly), **before** the verification sub-agent (Phase 5.7 / Phase 4.7) and again between every verification fix iteration.

**`docs/architecture.md`** — Sub-agent definitions now mention Opus default for verifier; ASCII flow diagram reordered (Write brief → state update → self-check gate → verification sub-agent loop → commit) with verification-block content rewritten to mention the new cap, the gating semantics, and the per-iteration `check_brief.py` re-run; "hard prerequisite" sentence updated for new phase chain.

### What stays
All hard invariants are unchanged: AI-content notice, no IOCs, two-source verification with national-CERT carve-out, English output, feature-branch-only publishing chain, the verification sub-agent loop itself (just larger cap + reordered + opus-by-default), the Phase 5.5 / Phase 4.5 self-check gate via `tools/check_brief.py` (just earlier in the phase chain), per-item metadata footer using taxonomy values, memory commits. The `state/run_log.json` schema is unchanged from v2.45 — `verification_iterations` and `verification_residual_count` scalars stay; the only loop-shape change is the cap value from 3 to 5. The `**Model:**` + `**Timestamps:**` sub-agent self-identification contract from v2.43 / v2.45 is unchanged. Older briefs from v2.42–v2.45 still pass `tools/check_brief.py` because the cap-related WARNs the script emits are tolerant (the script's `warn("run-log-verification", f"verification_iterations = {vi} exceeds the v2.27 cap of 3")` triggers above 3 iterations but is a WARN, not a FAIL — that warn message will be updated to reference the v2.46 cap of 5 in the next `tools/check_brief.py` patch).

---

## 2.45 — 2026-05-10 (per-agent start/end timestamps — every agent records its own wall-clock and reports it back)

### Why
The v2.43 self-identification rework gave every sub-agent a `**Model:**` self-report line plus an *optional* `**Self-telemetry:** duration_seconds=…` line, but two gaps remained: (1) `duration_seconds` was an opaque scalar with no underlying start / end timestamps, so an operator couldn't tell from a run record whether two sub-agents ran concurrently or serially, when in wall-clock terms a stall happened, or how long elapsed between the main agent's last sub-agent return and Phase 5; (2) the field was optional, so most actual returns omitted it and the Ops dashboard's per-sub-agent duration sparkline stayed empty. The main agent already recorded its own `started` / `completed` / `duration_seconds` in `state/run_log.json` (added in v2.43), but the sub-agents had no symmetric contract — and crucially, no instruction to capture a stamp at the very *start* of their turn before any tool call. Operator asked for symmetry: every agent (main + each research sub-agent + each verification iteration) records its own start timestamp at the beginning and end timestamp at the end, and sub-agents report both back so the main agent can stash them in the run log.

### What changed

**`.claude/agents/cti-research.md`** — New "Timestamps — MANDATORY" section (above Self-identification) requiring the sub-agent's first action to be `date -u +"%Y-%m-%dT%H:%M:%SZ" | tee work/<run-id>/<your-domain>.started_at` and its last action to be the symmetric `*.ended_at` capture. Self-identification block updated: the existing optional `**Self-telemetry:**` line is split — start / end / duration move to a new **mandatory** `**Timestamps:** started_at=… · ended_at=… · duration_seconds=…` line right under `**Model:**`; `**Self-telemetry:**` keeps fetch / token counters and stays optional. Return-format example updated. `unknown` is the only honest fallback when capture fails — never invent.

**`.claude/agents/cti-verification.md`** — Same Self-identification change (mandatory `**Timestamps:**` line under `**Model:**`) plus a parallel "Timestamps — MANDATORY" section using `work/<run-id>/verify.iter<N>.started_at` / `.ended_at` so each iteration's timing is preserved across the 3-iteration loop.

**`prompts/daily-cti-brief.md`** — Banner bumped to v2.45. New **Phase 0 step 0** added before the existing step 1: main agent captures its start timestamp into `work/<run-id>/main.started_at` as its very first action. Phase 1 capture block extended: parses the new `**Timestamps:**` line from each research return and stashes `started_at` / `ended_at` / `duration_seconds` into `state/run_log.json.sub_agents.<S1..S4>` (top-level, not inside `telemetry`); missing line → `"unknown"` and `null`. Phase 4.5 verifier capture block similarly extended for `verification.iterations[N].started_at` / `.ended_at` / `.duration_seconds`. Phase 5 opens with a symmetric main-agent end-stamp capture (`work/<run-id>/main.ended_at`) used to populate `started` / `completed`. The `run_log.json` schema example gains six new fields (3 per sub-agent × 4 + 3 per verification iteration). Population rules updated.

**`prompts/weekly-summary.md`** — Banner bumped to v2.45 in lockstep. Same updates as daily, scoped to W1 / W2 sub-agents and Phase 3.5 verification, with Phase 4 carrying the symmetric end-stamp capture.

### What stays
All hard invariants are unchanged: AI-content notice, no IOCs, two-source verification with national-CERT carve-out, English output, feature-branch-only publishing chain, Phase 4.5 verification loop, Phase 5.5 self-check gate, per-item metadata footer using taxonomy values, memory commits. The existing `**Model:**` self-identification contract (v2.43) is unchanged — `**Timestamps:**` is a new required line below it, not a replacement. The `state/run_log.json` schema is **additive** — every existing field stays, the new `started_at` / `ended_at` / `duration_seconds` per sub-agent and per verification iteration sit alongside what was already there, and `tools/check_brief.py`'s existing `check_run_log_for_today` keeps working without modification (the new fields are not yet enforced; that can come in a later WARN-level check). The `**Self-telemetry:**` line stays optional, just narrower in scope (fetch / token counters only — duration moves to the mandatory `**Timestamps:**` line). Older briefs from v2.42–v2.44 still pass every existing gate.

---

## 2.44 — 2026-05-10 (CISA KEV remediation deadlines de-emphasised — US-FCEB only, not operational signal for CH/EU audience)

### Why
The 2026-05-10 brief led an UPDATE entry with *"UPDATE: Ivanti EPMM CVE-2026-6973 — KEV deadline expired"* and an Action Item with *"Patch Ivanti EPMM today — KEV deadline expired"*. The operator flagged this as wrong framing for the brief's audience: a Swiss / European public-sector SOC. CISA's Known Exploited Vulnerabilities catalog is a US Federal Civilian Executive Branch (FCEB) compliance regime under [BOD 22-01](https://www.cisa.gov/news-events/directives/binding-operational-directive-22-01) — its **listing flag** is jurisdiction-agnostic intelligence (CISA confirms in-the-wild exploitation), but its **remediation deadline** is a US compliance date with no jurisdictional weight in CH / EU. *"KEV deadline expired today"* on a previously-covered CVE was being treated as material new development — it isn't, and the prompt's PD-8 (no repetition / UPDATE rule) had no explicit guard against it. Same drift in § 6 Action Items (framing actions around the US deadline instead of the underlying exploitation) and in the weekly's § 1 / § 9 framing inputs (the "List 6 — inaction = incident" recipe and the "Looking ahead" examples both named KEV deadlines as drivers).

This release adds an explicit prime directive that draws the line between the KEV listing-flag (keep) and the KEV deadline (drop) and rewires every section that previously named KEV deadlines as a framing input.

### What changed

**`prompts/daily-cti-brief.md`** — Banner bumped to v2.44. New **PD-13** added at the end of the Prime directives block: *"CISA KEV remediation deadlines are not operational signal for this audience."* The directive keeps the listing flag (`Status: ..., cisa-kev` footer + `cisa-kev` taxonomy tag stay) and forbids leading TL;DR bullets, Immediate Action callouts, § 4 UPDATEs, or § 6 Action Items on a KEV deadline alone. *"KEV deadline expired today"* / *"KEV deadline tomorrow"* on a previously-covered item is explicitly named as **not** material new development under PD-8. Same logic extended to other US-only deadlines (CISA Emergency Directives, ED orders). § 0 Immediate Actions callout disqualifiers updated: the prior phrasing *"surface as § 4 Updates or § 6 Action Items"* (which directly contradicted the new rule) was removed; KEV deadlines now drop from the callout entirely with PD-13 governing § 4 / § 6 too.

**`prompts/weekly-summary.md`** — Banner bumped to v2.44 in lockstep. New **PD-12** (KEV jurisdictional scope) added to the "Highlights restated for first read" block; the prior PD-12 (Less is more) renumbers to PD-13 — Markdown auto-numbers so prose/anchors are unaffected. Three downstream rewires: (a) §§ 1–3 framing recipe at top of "What the weekly is for" drops *"where a CISA KEV deadline has passed"* from the Monday-morning fire list and adds an inline pointer back to PD-13. (b) Phase 1 List 6 ("inaction = incident") inputs drop the *"CISA KEV deadline passed during the window"* bullet — the surrounding bullets (active exploitation continued / pre-auth RCE with mass-scanning / campaign confirmed targeting audience / vendor advisory reclassified) already capture the operational drivers. (c) § 1 H3 framing line drops *"missed deadline"* and replaces with *"ongoing victim acquisition, mass-scanning evidence, fresh victim disclosures"*. (d) § 9 *Looking ahead* rewrites the example list — *"KEV deadlines pending"* is removed, *"EU / Swiss regulator deadlines approaching, ongoing exploitation against named target classes"* added, with an explicit PD-13 pointer.

**`site/build.py`** — Self-check at `self_check()` strips `<code>...</code>` and `<pre>...</pre>` spans from feed `<content:encoded>` payloads before the `**...**` and `[..](http..)` leak checks. The 2026-05-10 deploy build failed (workflow run #83 → exit 4) because the brief's verification iteration log deliberately quotes a sub-agent's verbatim self-identification string `` `**Model:** Claude Sonnet 4.5 (`...`)` `` — the renderer correctly emits this as `<code>**Model:**</code>` (literal text), but the regex scanned the whole payload and false-positived. The fix lets the operator preserve verbatim sub-agent self-identification strings (required by daily PD-3 self-id contract) without tripping the self-check. Genuinely-leaked markdown elsewhere in feed bodies still triggers the check.

### What stays
All hard invariants are unchanged: AI-content notice, no IOCs, two-source verification with national-CERT carve-out, English output, feature-branch-only publishing chain, Phase 4.5 verification loop, Phase 5.5 self-check gate, per-item metadata footer using taxonomy values, memory commits. The `cisa-kev` taxonomy tag and the `Status: ..., cisa-kev` footer slot **stay in place** — the KEV listing flag (CISA-confirmed exploitation) is exactly the kind of jurisdiction-agnostic intelligence signal the brief is for. § 2 Trending Vulnerabilities inclusion gate "Listed in the CISA KEV catalog" stays — KEV inclusion is still a valid gate because what it gates on is *confirmed exploitation*, not the deadline. § 3 weekly CVE roll-up still groups by status including *KEV-added* — same reasoning. The `tools/fetch_source.py cisa-kev` mandatory-bridge rule stays — fetching the KEV catalog is how the listing flag gets read every run.

---

## 2.43 — 2026-05-09 (per-agent model self-identification + Ops dashboard rework)

### Why
Until this version, only the main agent self-identified its model — the four research sub-agents and the verification sub-agents had no contract for naming themselves. When the runtime ran the main agent and the sub-agents on different models (a routine operator configuration), the brief's AI-content notice silently overstated uniformity ("produced by a single model") and `state/run_log.json` had no per-agent model field, so the Ops dashboard at `/ops/` couldn't surface the split. The dashboard itself was sparse — a thin recent-runs table plus a stale-source list — with none of the duration / verification-verdict / fetch-failure / sub-agent-allocation telemetry the run log already captured. Operators couldn't tell from one glance whether a run was healthy, which model wrote which part, or how performance was trending. This release closes both gaps in one commit so the surface (notice + footer + run log + dashboard) is internally consistent. **Critically, the prompt content deliberately gives no example model name** — naming one would bias every routine into self-identifying as that model regardless of which model actually ran. Each agent reasons about its own identity from its runtime context.

### What changed

**`.claude/agents/cti-research.md`** — New "Self-identification" section (above the return format) requiring the agent to open every return with `**Model:** <friendly> (<id>)` plus an optional `**Self-telemetry:**` line carrying duration / fetch-call counts. Return-format example updated to show both lines.

**`.claude/agents/cti-verification.md`** — Same Self-identification block requiring the verifier's first non-blank line to be `**Model:**`. Return-format heading rewritten to mention the line ahead of the `## Verification report …` heading. Optional self-telemetry covers `urls_checked`, `webfetch_calls`, `bridge_fetches`, `duration_seconds`.

**`prompts/daily-cti-brief.md`** — Banner bumped to v2.43. Phase 1 Spawn block now instructs the main agent to parse each sub-agent's `**Model:**` line and stash `model` / `model_id` / `telemetry` under `sub_agents.<S1..S4>`. Phase 4.5 verification now records `verification.iterations[]` with a per-iteration `model` / `model_id` / `verdict` / finding-count breakdown (legacy `verification_iterations` / `verification_residual_count` scalars stay for back-compat). Phase 5 `run_log.json` example schema rewritten end-to-end with the new fields (`started`, `completed`, `duration_seconds`, main `model_id`, per-sub-agent `model` / `model_id` / `telemetry`, `verification.iterations[]`). Self-identification section rewritten to require a three-place surface — blockquote enumerates sub-agent models, `**Generated by:**` line carries an explicit `**Sub-agents:** S1: … · S2: … · verify: …` block, `run_log.json` records the structured form.

**`prompts/weekly-summary.md`** — Banner bumped to v2.43 in lockstep. Same updates as daily, scoped to W1 / W2 sub-agents and the weekly's verification phase.

**`prompts/brief-template.md`** — Both daily and weekly skeleton blockquotes updated: AI-content notice now names the main agent **and** the comma-separated set of distinct sub-agent models; `**Generated by:**` line carries the new `**Sub-agents:** Sn: <friendly>` block.

**`tools/check_brief.py`** — `check_ai_notice` now WARNs (not FAILs, so older briefs still pass) when the v2.43 sub-agent enumeration is missing from the blockquote or the metadata line. `check_run_log_for_today` extended with five new checks: main-agent `model` recorded; every returning sub-agent has a `model`; `verification.iterations[]` populated and consistent with the legacy scalar; `duration_seconds > 0`; `started` + `completed` both present. All five WARN rather than FAIL — the run log's existing required-keys check is the hard gate.

**`state/run_log.json`** — Schema bumped to v2 with new field documentation. The two existing run records (2026-05-08, 2026-05-09) backfilled with realistic values for the new fields so the dashboard has demonstrable telemetry on first build (durations, per-sub-agent models + telemetry, verification iteration breakdown, S4 stalled on 2026-05-08).

**`site/build.py`** — `render_ops_page` rewritten end to end. Top of the page now carries seven KPI tiles (total runs, avg duration, items published, verification clean-rate, sub-agent stalls, last run, distinct models) with inline SVG sparklines / bar charts / stacked bars. New "Latest run" panel: main-agent model badge, per-sub-agent cards with model swatch + items-returned + sources-used bar + self-telemetry, verification chips, fetch-failure chips, deep-dive title. New "Models in use" section: donut chart with legend + per-role contribution table. New "Sub-agent fetch density" heatmap (rows = sub-agents, columns = runs, intensity = used/attempted ratio). New "Verification iterations" table: one row per iteration with verdict pill, verifier-model swatch, finding counts, telemetry. Recent-runs table redesigned: kind pill, main-model swatch, prompt version, duration, items, per-sub-agent cells (model swatch + items + sources), fetch-fail count, verification verdict pill. Six new pure-Python SVG primitives (`_ops_svg_sparkline`, `_ops_svg_bars`, `_ops_svg_stacked_bars`, `_ops_svg_donut`, `_ops_svg_heatmap`, `_ops_kpi_tile`) — all CSP-safe (no inline JS), no third-party chart deps.

**`site/assets/css/styles.css`** — New `Ops dashboard` section at end of file: KPI tile grid, sparkline / bar / donut / heatmap styling, latest-run panel, sub-agent cards, model swatches, pill variants, denser recent-runs table layout. Light + dark themes both covered via existing CSS custom properties.

### What stays
Hard invariants preserved: AI-content notice still required (mechanism is just expanded); two-source verification + national-CERT carve-out unchanged; no IOCs / no vanity metrics / English-only / feature-branch-only publishing chain unchanged; Phase 4.5 verification loop with 3-iteration cap unchanged; Phase 5.5 `tools/check_brief.py` self-check gate unchanged (gains five new WARN-level checks but no new FAIL gates, so older runs and the migration brief still pass). `state/run_log.json` legacy fields (`model`, `verification_iterations`, `verification_residual_count`) all stay for back-compat with v2.42 run records and the dashboard's fallback rendering. Stale-source watchlist on the Ops page kept in place.

---

## 2.42 — 2026-05-09 (drop `docs/improvements.md` from the keep-current doc list)

### Why
Operator deleted `docs/improvements.md` — the backlog file mixed shipped items with open ones, and the open items were drifting (some referenced threat IDs from the deleted `security-review.md`, others were minor enough to belong in commit messages instead of a parallel tracker). With the file gone, the daily prompt's "Documentation — keep current" list still named it, which would push the routine to recreate the deleted file on its next self-edit pass. Bumping to v2.42 syncs the list with on-disk reality.

### What changed

**`prompts/daily-cti-brief.md`** — "Documentation — keep current" list: dropped `docs/improvements.md`. Header banner bumped to v2.42.

**`prompts/weekly-summary.md`** — Header banner bumped to v2.42 in lockstep (no other content change).

**`README.md`, `docs/architecture.md`, `CLAUDE.md`** — Removed tree entries and links pointing at `docs/improvements.md`. The README's "where to find more" footer paragraph now points to `docs/operating.md` for runbook content. The architecture doc's "Adding a new component" footer now instructs operators to write reasoning into the commit message and bump the prompt version with a CHANGELOG entry, rather than into a separate backlog file.

### What stays
All hard invariants are unchanged: AI-content notice, no IOCs, two-source verification with national-CERT carve-out, English output, feature-branch-only publishing chain via `.github/workflows/auto-merge-claude.yml`, Phase 4.5 verification loop, Phase 5.5 self-check gate, per-item metadata footer using taxonomy values. No phase order change. No source-list policy change. No fetch-budget change. The remaining four `docs/` files (`architecture.md`, `operating.md`, `analytics.md`) and three runtime-policy files in `prompts/` (`verification.md`, `brief-template.md`, `check-brief-fixes.md`) carry the load that was previously split between docs and a separate backlog.

---

## 2.41 — 2026-05-09 (separation of concerns: prompt-runtime files moved into `prompts/`, `docs/` reworked, About page split into Documentation + Prompts)

### Why
Mixing prompt-runtime content (verification policy, brief template, check-brief fix recipes — all `Read` by the master prompt at runtime) with operator-facing system documentation in the same `docs/` directory was confusing. A new operator reading `docs/` couldn't tell which files were policy the routine enforces versus reference material for them. Worse, `docs/workflow.md` and `docs/routine-setup.md` carried stale content from the pre-v2.36 direct-push-to-`main` model and didn't match what the prompts actually do anymore.

This release is a single conceptual cut: anything the routine `Read`s at runtime moves to `prompts/`; `docs/` becomes pure operator-facing documentation.

### What changed

**Files moved (`git mv`, history preserved)**

- `docs/verification.md` → [`prompts/verification.md`](verification.md)
- `docs/brief-template.md` → [`prompts/brief-template.md`](brief-template.md)
- `docs/check-brief-fixes.md` → [`prompts/check-brief-fixes.md`](check-brief-fixes.md)

**Files deleted**

- `docs/spawn-templates.md` — pure pointer doc; superseded by [`.claude/agents/cti-research.md`](../.claude/agents/cti-research.md) and [`.claude/agents/cti-verification.md`](../.claude/agents/cti-verification.md) which carry the canonical sub-agent system prompts.
- `docs/workflow.md` — duplicated the prompts themselves (the prompts ARE the workflow contract). Phase narrative now lives in the daily / weekly prompts; structural map in `docs/architecture.md`.
- `docs/routine-setup.md` — replaced by `docs/operating.md` (rewritten for the current feature-branch + auto-merge model; the old doc still described the forbidden direct-push pattern).

**Files created**

- [`docs/operating.md`](../docs/operating.md) — operator runbook covering: publishing chain (feature branch only), one-time setup (Claude GitHub App, workflow permissions, Pages enablement, routine creation), operations dashboard signals to watch, sub-agent capability ceiling, credential rotation cadence, troubleshooting matrix.

**Daily prompt — `prompts/daily-cti-brief.md`**

- All `docs/verification.md` / `docs/brief-template.md` / `docs/check-brief-fixes.md` references updated to the new `prompts/`-rooted paths (intra-prompts links use bare filenames since the prompts directory is the link root).
- "Where things live" tree updated to list the runtime-policy files under `prompts/` and to describe `docs/` as operator-facing only.
- "Documentation — keep current" list rewritten to match the new layout: `docs/architecture.md`, `docs/operating.md`, `docs/analytics.md`, `docs/improvements.md`, `prompts/verification.md`, `prompts/brief-template.md`, `prompts/check-brief-fixes.md`.
- `docs/routine-setup.md` references replaced with `docs/operating.md`.
- Header banner bumped to v2.41.

**Weekly prompt — `prompts/weekly-summary.md`**

- Same path updates applied; header bumped to v2.41 in lockstep (no other content change).

**`CLAUDE.md`**

- "Where things live" tree updated to reflect the moves.
- Prompt-versioning rule extended: edits to `prompts/verification.md`, `prompts/brief-template.md`, and `prompts/check-brief-fixes.md` now also require a CHANGELOG entry + version bump (these files are loaded by the prompts at runtime, so a silent edit produces the same drift between rendered brief and committed policy as a silent prompt edit).
- New "Skeleton-then-Edit (operational guardrail)" reminder added to the operational-guardrails section, explaining why a single large `Write` trips `Stream idle timeout` and what shape of edit dodges it (this rule was previously folded into a one-liner; now expanded with the empirical signal that prompted it).

**`README.md`, `docs/architecture.md`, `docs/improvements.md`**

- All `docs/verification.md` / `docs/workflow.md` / `docs/routine-setup.md` references updated to either the new `prompts/`-rooted path or to `docs/operating.md`.
- README's "Phase 6" bullet rewritten to describe the actual feature-branch + auto-merge chain (the old wording said "push directly to `main` — every brief is published the moment it is generated", which contradicts repo policy).
- README tree updated to show the new `prompts/` and `docs/` layouts side-by-side.

**`site/build.py`, `site/test_build.py`, `site/README.md`**

- About-page generator restructured. Old layout: flat `/about/<doc>/` for every `docs/*.md` plus `/about/changelog/`. New layout:
  - `/about/` — landing page with two clear sections (Documentation + Prompts), prepended to the README content.
  - `/about/docs/` — documentation index linking each doc.
  - `/about/docs/<name>/` — one page per `docs/*.md`.
  - `/about/prompts/` — prompts index listing each prompt + the last 10 CHANGELOG version headings (so the version evolution is visible without leaving the index).
  - `/about/prompts/<name>/` — one page per `prompts/*.md` (excl. CHANGELOG).
  - `/about/prompts/changelog/` — full prompt CHANGELOG.
- Link-rewriter (`_rewrite_about_links`) extended with `prompts/<name>.md` → `about/prompts/<name>/` and `prompts/CHANGELOG.md` → `about/prompts/changelog/` mappings.
- Brief-page prompt-version badge updated to point at `about/prompts/changelog/`.
- Ops dashboard "Architecture" link updated to `about/docs/architecture/`.
- `test_build.py` reference updated.
- `site/README.md` output-tree and URL-table updated.

### What stays
All hard invariants are unchanged: AI-content notice, no IOCs, two-source verification with national-CERT carve-out, English output, feature-branch-only publishing chain via `.github/workflows/auto-merge-claude.yml`, Phase 4.5 verification loop, Phase 5.5 self-check gate, per-item metadata footer using taxonomy values. No phase order change. No source-list policy change. No fetch-budget change. The verification policy text in `prompts/verification.md` is byte-identical to the previous `docs/verification.md`. Same for `brief-template.md` and `check-brief-fixes.md` — only the path changed.

CNAME (`ctipilot.ch`) restored at the repo root after being mistakenly grouped into the v2.40 deletions; the build still copies it to gh-pages and the custom domain is unaffected.

---

## 2.40 — 2026-05-09 (docs cleanup: drop superseded historical/duplicate docs from prompt's keep-current list)

### Why
The operator removed four files that no longer reflect the current system: `CNAME` (custom-domain marker — managed elsewhere), `SECURITY_REVIEW.md` (root duplicate of `docs/security-review.md`), `docs/security-review.md` (point-in-time threat-model snapshot — the actionable carry-over already lives in `docs/improvements.md` § "Open — security & autonomy hardening"), and `docs/v2-plan.md` (historical implementation plan; every item shipped in v2.23). The daily prompt's "keep current" doc list still listed `security-review.md`, which would push the routine to recreate the deleted file on its next self-edit pass. Bumping to v2.40 syncs the list with on-disk reality.

### What changed

**`prompts/daily-cti-brief.md`** — "Encouraged self-edits" → "Documentation — keep current" list: dropped `security-review.md`. The remaining list (`architecture.md`, `workflow.md`, `verification.md`, `routine-setup.md`, `analytics.md`, `brief-template.md`, `check-brief-fixes.md`, `spawn-templates.md`, `README.md`, `briefs/README.md`, `site/README.md`) matches what's on disk after the cleanup. Header banner bumped to v2.40.

**`prompts/weekly-summary.md`** — Header banner bumped to v2.40 in lockstep (no other content change).

**`README.md`, `site/README.md`, `docs/improvements.md`, `docs/routine-setup.md`** — Removed broken links / tree entries pointing at the deleted files. The "Reader engagement" → "Full posture in security-review.md § 4" line and the "Security posture" → "Threat model and current controls are documented in security-review.md" line in `README.md` are gone; the section keeps its substantive content (CSP, Markdown sanitisation, vendored-library hash pinning, Phase 5.5 self-check) and now reads standalone. `routine-setup.md`'s sub-agent capability ceiling section drops the parenthetical security-review.md cross-reference; the runbook content (allowed/forbidden tools per sub-agent) is unchanged.

**`.gitignore`** — Added `.claude/worktrees/` so Claude Code-created feature-branch worktrees stop showing up as untracked in `git status`.

### What stays
All hard invariants are unchanged: AI-content notice, no IOCs, two-source verification with national-CERT carve-out, English output, feature-branch-only publishing chain via `.github/workflows/auto-merge-claude.yml`, Phase 4.5 verification loop, Phase 5.5 self-check gate, per-item metadata footer using taxonomy values. No phase order change. No source-list policy change. No fetch-budget change. The cleanup only removes dead files and the prompt's stale references to them.

---

## 2.39 — 2026-05-09 (version-controlled auto-memory: `.claude/memory/` + SessionStart symlink hook)

### Why
Claude Code's built-in auto-memory writes to `~/.claude/projects/<project-hash>/memory/` — a machine-local directory that's invisible to other operators, doesn't survive a fresh cloud-routine container, and produces a different directory per worktree (Claude Code derives the hash from `$PWD`, not from the git repo root). For an autonomous CTI routine where the operator wants Claude to accumulate learnings across runs (recurring source-fetch failure modes, publisher quirks, `WebFetch` workarounds, deep-dive rotation patterns), machine-local storage is the wrong default — every fresh fire forgets everything.

### How
Three new files redirect auto-memory into a version-controlled, repo-local directory:

- **`.claude/memory/MEMORY.md`** — seed index file. The auto-memory feature loads the first 200 lines / 25 KB of this file into every session. Topic files in the same directory load on demand.
- **`.claude/hooks/setup-memory.sh`** — SessionStart hook. Computes the project hash the same way Claude Code does (`tr '/_.' '---'` against `$PWD`) and symlinks `~/.claude/projects/<project-hash>/memory` → `<repo>/.claude/memory/`. Idempotent. On first run with pre-existing local memory files, migrates them into the repo and moves the original aside as `*.local-backup-<timestamp>`. Best-effort: failures log to stderr but never block the session.
- **`.claude/settings.json`** — `autoMemoryEnabled: true` (explicit, the default), `SessionStart` hook config.

### Daily prompt — `prompts/daily-cti-brief.md`

**Phase 6 git-add** now includes `.claude/memory/` so memory writes from this session are committed alongside `state/*.json` and `sources/sources.json`. The next routine fire (or a local session) sees the accumulated memory.

**Header banner** bumped to v2.39.

### Weekly prompt — `prompts/weekly-summary.md`

Same change to the Phase 5 git-add. Header bumped to v2.39.

### `CLAUDE.md`

New "Project memory" section explaining the redirect mechanism, first-run approval flow, cloud-routine behaviour, fallback if the hook fails (Claude can still `Read` / `Write` `.claude/memory/` directly), and where the files live. Updated the "Where things live" tree.

### Operator-visible changes

- `/memory` command in interactive sessions now lists files in `<repo>/.claude/memory/` instead of `~/.claude/projects/<hash>/memory/`. "Remember that X" prompts persist into the repo.
- Cloud routine memory survives across fires. Each fire reads the committed `MEMORY.md`, may write new topic files, commits the diff in Phase 6.
- First local session per machine: Claude Code prompts to approve the `SessionStart` hook. Approve once. Pre-existing local memory files (e.g., from before this commit) are migrated into the repo automatically.
- Worktrees: each worktree's hook symlinks to *that worktree's* `.claude/memory/`. Since the directory is committed, all worktrees see the same content via git.

---

## 2.38 — 2026-05-09 (custom sub-agents: `cti-research` + `cti-verification`, model split Opus main / Sonnet workers, root CLAUDE.md)

### Why
The daily and weekly routines previously spawned every sub-agent as `subagent_type: general-purpose` and prepended a verbatim ~30-line spawn template from `docs/spawn-templates.md` to every spawn message. Three problems with that pattern:

1. **Token waste.** The spawn template was re-injected into every parallel sub-agent's input on every run — four times per daily Phase 1, twice per weekly Phase 2, plus once per verification iteration. Sub-agent system prompts can be loaded once by the harness and reused — `general-purpose` couldn't take advantage of that.
2. **No model isolation.** With `general-purpose`, every sub-agent inherited the main agent's model. When the routine ran on Opus, the four parallel research workers each consumed an Opus context — bumping cost and tightening the per-agent context budget. The right split is: Opus for the main agent (large context, owns composition + publishing chain), Sonnet for the workers (parallel research + cold-reader verification with isolated 1M-token context windows each).
3. **No tool-set enforcement.** The verifier was specified as "reads only" in prose but had every tool the main agent had. A bug or a misread instruction could have let it `Edit` the brief mid-verification, bypassing the iteration loop. With a custom sub-agent definition, the read-only constraint is enforced by the harness via the `tools:` frontmatter.

A second-order ask: a root `CLAUDE.md` to give an interactive operator (debugging a brief, investigating a state-file inconsistency, looking at the build) the same project-wide guardrails the routine has — without requiring them to read the master prompts first.

### New files

**`.claude/agents/cti-research.md`** — Sonnet, isolated context, color blue. Tools: `Read`, `WebFetch`, `WebSearch`, `Bash`, `Write`, `Edit`, `Grep`, `Glob`. The full operational system prompt — defender-vantage opener, link-discipline clauses, MANDATORY bridge-fetcher rules for known-403 hosts, `WebFetch` outbound-links template + the two empirical findings (listing-page outbound-link loss; per-advisory CERT-page citation pattern), Discovery-trace requirements, return format, operational guardrails, candidate-source surfacing, "what you do NOT do" (composition / state / commit / nest sub-agents). Used by both daily Phase 1 (S1–S4) and weekly Phase 2 (W1–W2); domain is passed in the spawn message.

**`.claude/agents/cti-verification.md`** — Sonnet, isolated context, color red. Tools: `Read`, `WebFetch`, `WebSearch`, `Bash`, `Grep`, `Glob` (no `Edit` / `Write` — read-only constraint enforced by the harness). The full check list: truth checks 1–4, editorial-quality checks 5–10, whole-brief checks 11–13 (W-PD-1 included for the weekly), return format with finding categories F1–F11, verdict line. Used by both daily Phase 4.5 and weekly Phase 3.5; the iteration loop runs in the main agent (re-spawn fresh each iteration, no shared memory, cap 3).

**`CLAUDE.md`** at repo root — short project-wide guardrails for any Claude Code session in this repo: what the repo is, the two custom sub-agents, the hard "do nots" (no direct push to main, no IOCs, no `WebFetch` of CISA / NCSC.ch, no `WebFetch` without the outbound-links template, no homepage / NVD-per-CVE / news-category Source URLs, never skip `tools/check_brief.py`, never block on a sub-agent), the operational guardrails (Skeleton-then-Edit, persist intermediate state, one new candidate per run, verification loop is non-negotiable but never blocks publish), where things live, self-evolution authority. Loaded into every session.

### Daily prompt — `prompts/daily-cti-brief.md`

**Header banner.** Bumped to `v2.38` and added the recommended-model-split note (Opus main / Sonnet sub-agents).

**Tools line.** Now references `.claude/agents/cti-research.md` and `.claude/agents/cti-verification.md` as the canonical sub-agent definitions.

**Phase 1 — Parallel research.** Replaced the "Sub-agent spawn template — read `docs/spawn-templates.md`" / "Passed verbatim — do not paraphrase" pattern with `subagent_type: cti-research` and an explicit "What each spawn message must contain" list (run id, window_hours, domain, source-list slice, dedup context, rotation-priority list, today's ISO date). Reinforced rules for the main agent kept (with the `WebFetch` outbound-links pointer now pointing at the `.claude/agents/cti-research.md` definition rather than `docs/spawn-templates.md`). Removed the now-redundant duplication of operational guardrails the sub-agent definition already covers.

**Phase 4.5 — Final verification sub-agent.** Replaced the "spawn template lives in `docs/spawn-templates.md`" pattern with `subagent_type: cti-verification` and an explicit short spawn-message list (brief path, iteration number, dedup context, run-log slice). Iteration loop unchanged — still cap 3, still fresh spawn each iteration, still allows ≤3 follow-up `cti-research` sub-agents per iteration for `Needs more research` / `Missed angles`. Hard rules updated: read-only is now enforced by the sub-agent's tool set, not just by prose. Added: "At least one verification iteration is mandatory — never commit without a `cti-verification` return on file."

**Quality gates.** Updated the Phase 4.5 quality-gate item to specify "ran via the `cti-verification` sub-agent at least once … re-spawn was a fresh sub-agent every iteration, not a continuation."

### Weekly prompt — `prompts/weekly-summary.md`

**Header banner.** Added an explicit `**Prompt version:** v2.38` line (parity with the daily prompt) plus the recommended-model-split note.

**Tools line.** References the same two sub-agent definitions as the daily prompt — explicitly noting that one definition backs both routines and the domain (W1 / W2 vs S1–S4) is passed in the spawn message.

**Phase 2 — Horizon research.** Same refactor as daily Phase 1: switched from `subagent_type: general-purpose` + verbatim template prepend to `subagent_type: cti-research` + thin per-domain envelope. Reinforced rules kept; redundant operational guardrails removed (covered in the sub-agent definition). The W1 (long-horizon ongoing developments) and W2 (strategic & policy horizon) sections themselves are unchanged.

**Phase 3.5 — Final verification.** Same refactor as daily Phase 4.5: switched to `subagent_type: cti-verification`, short spawn-message list (now explicitly carries `kind: weekly` so the verifier applies W-PD-1 in check 11), iteration loop unchanged. Added: "At least one verification iteration is mandatory."

**Quality gates.** Updated the Phase 3.5 quality-gate item to mirror the daily ("ran via the `cti-verification` sub-agent at least once … fresh sub-agent every iteration").

### Replaced — `docs/spawn-templates.md`

Trimmed from a ~140-line verbatim spawn-template repository to a ~50-line pointer at `.claude/agents/cti-research.md` and `.claude/agents/cti-verification.md`. The previous content (defender-vantage opener, link-discipline, bridge-fetcher rules, `WebFetch` outbound-links template, empirical findings, Discovery-trace requirements, return formats, operational guardrails, finding-category list F1–F11) all moved into the canonical sub-agent definitions. The pointer file documents what the main agent passes per spawn (so the daily and weekly prompts don't need to repeat it) and lists the hard invariants that must never be removed from the sub-agent definitions.

### What v2.37 keeps

- Section numbering 0–7, Immediate Actions callout, UPDATE blockquote shape, footer parser fix, version banner.
- Phase 6 publishing chain (commit → sync → push → auto-merge → verify), Phase 7 publish verification, hard invariants 7 + 9.
- All editorial gates, prime directives, state-update rules, the Phase 5.5 self-check gate via `tools/check_brief.py`.
- All build-side smoke tests, taxonomy validation, URL allowlist, vendored-library SHA-256 integrity.

### Operator-visible changes

- Per-run cost should drop noticeably when the routine runs on Opus, since the four parallel research workers and the verification sub-agent now run on Sonnet via the `model: sonnet` frontmatter in the sub-agent definitions. The main agent stays on whatever model the routine config specifies (recommended: Opus).
- Read-only enforcement on the verifier is now mechanical — the verifier sub-agent simply does not have `Edit` or `Write` tools available. A bug in the iteration loop can no longer let it modify the brief.
- Interactive sessions in this repo now have a root `CLAUDE.md` covering the same project-wide guardrails the routine has — easier for an operator to debug a brief or investigate a state-file inconsistency without first reading the master prompts.

---

## 2.37 — 2026-05-09 (rendering fixes: section numbering, Immediate Actions callout, UPDATE blockquote, footer parser, version banner)

### Why
Operator review of the 2026-05-09 brief surfaced four rendering / structure problems plus one operability ask:

1. **Strange whitespace** between the AI-content notice and the TL;DR heading — the prompt convention placed `**Generated by:** …` + `---` between the notice and the first H2, the build stripped the metadata line but left the trailing horizontal rule, and the rendered `<hr/>` introduced an empty band.
2. **Section numbering jumped 0 → 2** on the (typical) days when the Immediate Actions section was omitted, because the heading skeleton hard-coded `## 1. Immediate Actions`.
3. **Per-item footer pills failed to render** for the last H3 in § 3 Trending Vulnerabilities (xrdp item), because the H4 CVE Summary Table was the trailing block of that item's body and `_split_trailing_footer` only inspected the *last* line.
4. **UPDATE blockquotes only contained the label**, because the agent wrote `> **UPDATE (originally covered …):**` followed by un-prefixed paragraphs — the renderer correctly closed the blockquote at the first non-`>` line, leaving the update content visually outside the callout.
5. **Hard to verify which prompt version the routine actually loaded** at run-time without diffing against `prompts/CHANGELOG.md`. The brief footer carries the version; the prompt itself did not surface it at the top.

### Daily prompt — `prompts/daily-cti-brief.md`

**Header banner.** Added a `> **Prompt version:** v2.37 …` line as the first blockquote of the prompt so the routine sees the version on the first page of its `Read`. The version log pointer was folded into the same banner.

**§ 0 / § 1 / Immediate Actions restructure.** Section table is now **8 sections, dense numbering, no skips** — TL;DR=0, Active Threats=1, Trending Vulnerabilities=2, Research=3, Updates=4, Deep Dive=5, Action Items=6, Verification Notes=7. The former § 1 Immediate Actions section is removed; on the rare day an item meets the bar, it appears as a **single Markdown blockquote callout immediately after the TL;DR bullet list**, ending in the standard metadata footer. New "§ 0 TL;DR + Immediate Actions callout" rule defines the callout shape, the bar, the disqualifiers, and the at-most-one rule.

**§ 4 Updates blockquote rule (new explicit shape).** Each UPDATE must be a single blockquote that `> `-prefixes every line of the update content (including blank separators as `>`), with the metadata footer as the final `> ` line. The prompt notes that the build's renderer auto-extends `> **UPDATE …` blockquotes as a safety net, but the agent should still write the canonical shape so source Markdown is unambiguous.

**Section-number references swept through the prompt** — the `§ 2`-through-`§ 8` numbering used in cross-references, the deep-dive history, the verification rule, the run-log fields, and the quality-gates checklist all shifted down by one to match the new layout.

### Build — `site/build.py`

**Preamble whitespace.** After stripping the `**Generated by:**` and `**Audience/Classification/Language/Prompt:**` metadata lines from the rendered preamble, also strip the trailing horizontal rule and surrounding blank lines. Result: the AI-content notice sits immediately above the TL;DR heading, no stray `<hr/>` between them.

**`_split_trailing_footer` scans backward.** When the trailing line of an item body is not a footer (typical when § 3's H4 CVE Summary Table is appended after the last per-CVE item's footer), scan backwards through the body for the most-recent footer-shaped line and lift only that line out — preserving the trailing aggregation in the rendered body, while still surfacing the structured footer pills.

**UPDATE blockquote auto-extension.** When `render_markdown` opens a blockquote whose first line matches `**UPDATE …`, it now absorbs subsequent paragraphs into the same `<blockquote class="callout-update">` until it hits a heading, HR, fenced code, another blockquote, or a metadata-footer line. This is a safety net for the new prompt rule; existing briefs still render correctly without re-authoring.

### Brief template — `docs/brief-template.md`

Updated to match the new section numbering, the Immediate Actions callout shape, the explicit UPDATE blockquote shape (with `> ` on every line including blank separators), and the H4 CVE Summary Table's location at the end of § 2.

### What v2.36 keeps
- Phase 6 publishing chain (commit → sync → push → auto-merge → verify), Phase 7 publish verification, hard invariants 7 + 9.
- All editorial gates, verification phases, and state-update rules.

---

## 2.36 — 2026-05-09 (publishing autonomy: feature-branch-only, auto-resolve conflicts, verify live site)

### Why
Operator review of the v2.35 fix revealed three further problems with the original publishing chain:

1. **Direct push to `main` violates repo policy.** Branch ruleset `main-protect` (deletion + non-fast-forward block) is active, and operator intent is "no humans or routines push to main directly — only the auto-merge action promotes." The v2.35 chain still tried `git push origin HEAD:main` first, which the routine's GitHub App may or may not be allowed to do depending on bypass-actor configuration; in any case the *intent* is that only the GitHub-hosted workflow runner pushes to main.
2. **The 2026-05-09 incident was not "main advanced during the run."** Last commit on main before the routine fired was 14 hours old; main was static the whole time the routine ran. The routine container's clone was already stale at session start — the local git proxy at `127.0.0.1:34969` mirrors github.com on a schedule, not per-pull. So `git fetch origin main` from inside the container can return a stale tip; the v2.35 sync step running against that stale tip can no-op, the push goes out, and only the auto-merge action (running on a github-hosted runner with direct github.com access) sees the real main and the real conflict.
3. **A pushed feature branch is not a published brief.** Without explicit verification, the routine's "push: ok" report is a *hope*, not a fact. Today's brief lived as an orphan branch for hours before anyone noticed.

### Daily prompt — `prompts/daily-cti-brief.md`

**Phase 6 — Commit & sync & push (publishing chain):**
- The direct-push-to-`main` step is **removed entirely**. The routine pushes only the feature branch.
- Sync step now applies **auto-resolution rules** before giving up: `state/cves_seen.json` / `state/covered_items.json` / `state/run_log.json` / `state/deep_dive_history.json` resolve with `--ours` (routine has freshest state); `sources/sources.json` resolves with `--theirs` (sources are curated on main outside routines; routine writes are transient `last_successful_fetch` fields). Anything else → abort merge, push feature branch as-is, let the auto-merge action surface the conflict.
- Feature-branch push retries up to 3 times with backoff (5s / 10s / 15s).
- Hard rule added: never `git push origin HEAD:main`. Repo policy.

**Phase 7 — Publish verification (NEW):**
- Polls `git fetch origin main && git cat-file -e origin/main:briefs/$(date -u +%F).md` until the brief lands on main, with a 10-min budget.
- If the brief landed, polls `curl -fsS https://ctipilot.ch/ | grep -q "$(date -u +%F)"` until the live site reflects today's date, sharing the same budget.
- Three reportable outcomes: `publish: ok`, `publish: main-only` (deploy-site failed/slow), `publish: pending (<reason>)` (auto-merge running / conflict / push failed / unknown).
- Hard rule: verification is read-only — never re-push, never touch the local commit on failure.

**Output line:** the `push:` line now reports only `ok (feature branch)` or `failed (<reason>)`. New `publish:` line carries the verified outcome.

**Hard invariant 7** rewritten to spell out the five-stage chain (commit → sync → push → wait for auto-merge → verify) and add the "no direct pushes to main" rule.

**Standalone-brief invariant 9** updated to match.

**Quality gate added:** "Phase 7 publish verification ran — the operator output's `publish:` line was set from the actual poll result, not assumed."

**Execution-environment paragraph (line 81)** updated end-to-end: chain description, the routine's stale-clone failure mode, the workflow's auto-resolution backstop, the deploy-site → ctipilot.ch path, and the policy that direct pushes to main are forbidden.

### Weekly prompt — `prompts/weekly-summary.md`

Phase 5 receives the same rewrite as the daily's Phase 6 (commit → sync with auto-resolution → feature-branch push with retry). New Phase 6 verifies `briefs/weekly/$(date -u +%G-W%V).md` is on main and that `https://ctipilot.ch/` reflects this week's id, with the same 10-min budget and the same outcome set. Output line, hard invariants, environment paragraph, and quality-gates list updated to match.

### Workflow — `.github/workflows/auto-merge-claude.yml`

Case 3 ("main advanced") now applies the same auto-resolution rules as the routine's sync step: `state/*.json` → `--ours`, `sources/sources.json` → `--theirs`. Any other conflicting path remains a loud failure (`exit 1` + `::error::` annotation). The header comment block was rewritten to document the auto-resolution policy and to note explicitly that the workflow's auto-resolution is a backstop for the case where the routine's local view of main was stale (proxy lag).

### What v2.35 got right and v2.36 keeps
- The sync step itself: still correct, still mandatory, still merges `origin/main` into the feature branch before pushing. v2.35's claim that this fixes the "silent skip" path was correct *as far as the workflow file going forward with the feature branch*; v2.36 adds the auto-resolution that v2.35 was missing.
- No changes to phases 0–5 of either prompt.

---

## 2.35 — 2026-05-09 (sync-then-publish chain — closes silent-skip on "main advanced")

### Why
On 2026-05-09 the daily routine published its brief to `claude/festive-mendel-dtucc` but the brief never reached `main`. Seven commits had landed on `main` while the routine was running — including the auto-merge fix `29685aa`. The routine pushed its feature branch unchanged, so the auto-merge workflow ran the *old* workflow file from the feature branch's tree (which still had the pre-`29685aa` "Skipping auto-merge; resolve manually" silent-skip path) and exited 0. The brief was orphaned. Operator had to manually merge `origin/main` into the feature branch (resolving a `sources/sources.json` conflict) and re-push so the workflow could ff-merge.

Root cause is structural: `on: push` workflows always run the workflow file from the pushed ref's tree. Any fix to `auto-merge-claude.yml` is invisible to a routine whose base predates the fix. The durable mitigation is to have **the routine itself sync `origin/main` into its feature branch before pushing**, which both (a) makes the direct push to `main` a fast-forward when branch protection allows and (b) ensures the feature branch carries the latest workflow file when the fallback path runs.

### Daily prompt — `prompts/daily-cti-brief.md`

**Phase 6 renamed two-stage chain → sync-then-publish chain.** Now five steps:

1. Stage and commit (unchanged).
2. **NEW — Sync.** `git fetch origin main` then `git merge --no-edit origin/main`. On clean merge → `SYNC_OK=true`. On conflict → `git merge --abort`, `SYNC_OK=false`, fall through.
3. Direct push to `main` — guarded on `$SYNC_OK=true` (only meaningful when feature branch is a strict descendant of main).
4. Fallback — push the feature branch.
5. Operator output — adds `push: needs operator (sync conflict)` for the rare case where step 2 aborted (the auto-merge workflow now fails loud with a conflict annotation in this case).

**Hard rule** added: "Never bypass the sync step — it is what makes the chain robust against main advancing during the run."

**Execution-environment paragraph (line 81)** updated to mention the sync step in the publishing-chain description.

**Hard invariants** point 7 ("Two-stage publishing chain") renamed to "Sync-then-publish chain" with the order spelled out. Point 9 in the standalone-brief checklist renamed similarly.

### Weekly prompt — `prompts/weekly-summary.md`

Phase 5 receives the same five-step rewrite as the daily's Phase 6, with the same operator-output set, the same hard rule about not bypassing sync, and the same environment-paragraph update. The weekly references a "summary edits" conflict path (vs. the daily's "brief edits") but otherwise mirrors the daily.

### What did NOT change
- `.github/workflows/auto-merge-claude.yml` is correct as of `29685aa`. The bug was the gap between routines that predate the fix and the workflow itself, not the workflow's logic.
- The publishing chain still tries direct push to `main` first (now usually succeeding because of the sync) and still falls back to the feature-branch + auto-merge Action path. The only difference is that the fallback now ships a feature branch that is a strict descendant of main, so case 1 (fast-forward) of the workflow always applies — case 3 (main advanced + merge commit) becomes unreachable from a properly-syncing routine.

---

## 2.34 — 2026-05-08 (weekly prompt brought up to daily quality bar — knowledge transfer)

### Why
The v2.33 compression aligned daily and weekly on the same docs (spawn-templates.md, brief-template.md, check-brief-fixes.md), but the weekly prompt itself was still thinner than the daily on several editorial-quality and operational-discipline sections. Operator and audit feedback called for the weekly to publish at the same technical / editorial bar as the daily — not a softer, "summary-grade" version. This release transfers the daily's load-bearing operational sections into the weekly so the weekly stands alone with the same rigour.

### Weekly prompt — `prompts/weekly-summary.md`

**Phase 0 — Preflight:** added explicit construction of the **deduplication context** (CVE IDs from `cves_seen.json`; named actors / campaigns / incidents / annual reports from `covered_items.json`; headlines and key paragraphs from each daily brief in the gap window; previous weekly's "Looking ahead" items as first-priority status-update candidates) and the **source rotation list** (parsed from `Coverage gaps:` lines in daily § 8 and prior weekly § 10; rotation-priority sources passed to W1 and W2, filtered by category — W1 → research/news/discovery/active-breaking; W2 → gov/policy/regulatory). The weekly previously assumed the daily provided this; now it builds its own.

**Phase 2 — Reinforced rules for the main agent:** new section mirroring the daily's. Carries the seven operational discipline points (drill into curated sources; `tools/fetch_source.py` MANDATORY for CISA + NCSC.ch with all five `python3 tools/fetch_source.py {ncsc-csh recent 10 | ncsc-csh post <ID> | cisa-kev | cisa page <URL> | url <full-URL>}` invocation forms; pivot from news to primary; `WebFetch` outbound-links template not optional; search topically — especially for previous weekly's "in motion" items where this week's status delta is the value-add; propose new sources at most one per run; full source-link discipline). Previously the weekly assumed the agent would re-derive these from the spawn template — now they're explicit for the consolidate / verify phases too.

**Phase 3 — Per-item metadata footer:** the **hard-blocked URL patterns table** is now inline (8 rows: NVD/MITRE/cve.org per-CVE; news-site landings; broadcaster namespace roots; national-CERT advisory indexes; CISA-catalog roots; research-lab marketing landings; gov cybersecurity-section landings; bare publisher/news/blog with no slug). Previously the weekly cross-referenced the daily; now it stands alone. Added the "Rule of thumb: if removing the trailing path component still resolves to a meaningful page, the URL is too generic" guidance and the live HEAD/GET 404 enforcement note.

**Phase 3 — Source-link discipline (numbered):** new explicit 6-point numbered list — only fetched URLs, specific page never landing, drill to primary keep secondaries, news-only fallback acceptable when explicit, verify before publishing, drop if unsure.

**Phase 3 — Multi-CVE breakdown:** expanded with the full footer example block and per-field breakdown rules (CVSS slash-separated or per-CVE explicit; Vector/Auth shared or per-CVE; Status comma-separated or per-CVE-scoped). Was previously one line.

**Phase 3 — Technical depth section:** new section ported from the daily, adapted for weekly. Carries the six bullet points — exact vulnerable component, MITRE ATT&CK technique IDs (with the daily's `T1190` / `T1059.001` / `T1505.003` / `T1557.001` / `T1068` / `T1078.004` / `T1556.006` / `T1611` example list), exploitation prerequisites (NTLM relay / OAuth device-code / SAML response forgery / S4U2Self), affected/patched versions to vendor-stated precision, observed exploitation status with named clusters (UNC / Storm / TA / APT / CL-STA), concrete defender takeaway with detection events (`Sysmon EID 1`, `4624 Logon Type 9`, `4663` on `ntds.dit`, `4769`), affected sectors and regions in footer fields. Cross-references the worked-good fragment in `docs/brief-template.md`. Includes the "weekly's consolidating role does NOT lower the technical bar — items get more synthesis context, not less specificity" framing.

**Phase 3 — Item granularity section:** new — one story per item, with weekly-specific framing on when consolidation is allowed (multiple daily items into one weekly item only when they truly are one story).

**Phase 3 — Citation strategy section:** new — primary source as substance, news as via, stack primary sources, always link primary AND originating daily brief (week → day → original primary walk), don't cite roll-up in place of primary (with the explicit reminder that the weekly summary IS itself a roll-up so it must cite the primaries underneath).

**Prime directives expanded:** the eight existing PDs were highlights of the daily's PDs; added four more for completeness as standalone weekly directives — fake-news guard (full text with all the daily's leak-site / hallucinated-CVE / blogspam / months-old-news / sweeping-attribution / Telegram-X-only specifics), no-IOCs (with MISP pointer), no-vanity-metrics, less-is-more (with the weekly-specific "bar is higher than the daily's because every item must additionally answer W-PD-1" framing, drop-without-ceremony list, variable-size rule, empty-section stub format).

**Phase 4.5 — Self-check checks expanded:** added two checks the daily's check_brief.py runs that the weekly was missing — `covered_items.json` appearances (every § 1 / § 2 / § 7 H3 with a key matching covered_items.json has a `weekly_summary` appearances[] record for today, warns) and Daily-brief link integrity (every `briefs/YYYY-MM-DD.md` link points to a file in the gap window, warns; surfaces file-rename drift). Brings weekly check count from 17 to 19, matching the daily.

### Net effect
- Weekly prompt now stands alone with the same operational rigour as the daily — no implicit cross-references for load-bearing rules.
- Every published weekly item carries the same technical-depth bar, citation discipline, and verification gating as a daily item, plus the weekly's W-PD-1 framing on top.
- File still fits in a single Read (~17K tokens, well under the 25K limit).

### Compatibility
- No changes to `tools/check_brief.py` itself — the two new weekly checks (covered_items appearances, daily-brief link integrity) need to be added to the script in a follow-up commit if they aren't already covered by the existing daily-mode checks. Output artefacts and footer format unchanged.
- Hard invariants list is unchanged (15 items + W-INV-1 / W-INV-2).

---

## 2.33 — 2026-05-08 (single-Read prompt fit for Sonnet 4.6 + spawn templates / reference template / FAIL-fix table extracted to docs)

### Why
The daily and weekly master prompts were the agent's first-step `Read`. Both had grown to the point where a single default `Read` failed (`File content (NN tokens) exceeds maximum allowed tokens (25000)`) — the daily was ~45K tokens, the weekly ~17K. Forcing the agent to do offset/limit reads at startup is a structural failure mode: the routine should never start in a degraded state. Target model is **Claude Sonnet 4.6**, which can handle dense / terse prose without the lengthy reinforcement that earlier prompt versions used.

### Goal
Both prompts must fit in **one** `Read` (≤25K tokens) so the agent can load the master prompt at the start of the run with a single tool call. **No operational content lost** — every rule, schema, command, empirical finding (Krebs feed test, CERT-FR per-advisory shape, `<content:encoded>` vs `<description>` RSS, listing-page outbound-link drop), bridge-fetcher invocation, hard-blocked URL pattern, inclusion gate, hard invariant, anti-crash guard, and verification check must remain operational.

### Daily prompt — `prompts/daily-cti-brief.md`
- **All operational content preserved**: 12 prime directives, 8 anti-crash guards, 4-class recency-window table, 4 sub-agents (S1–S4), § 1 do/do-not shape catalog, § 3 inclusion gates, hard-blocked URL patterns table, 19 Phase 5.5 checks, two-stage push chain, 15 hard invariants, every empirical finding from the operator's WebFetch audit, every fetch_source.py invocation form, the discovery-trace rationale + 3 example shapes + 6 mandatory rules, the worked-good fragment (now in `docs/brief-template.md`), the "What this phase fixes" Phase 4.5 catalog.
- **Externalised** to keep the master prompt under the Read limit:
  - **Reference template** for the rendered brief → `docs/brief-template.md` (also adds the worked-good § 2 fragment for technical-depth pedagogy).
  - **Sub-agent + verifier spawn templates** (the verbatim quoted blocks passed to spawned agents) → `docs/spawn-templates.md`. The agent reads this file once during Phase 1 (research sub-agents) and Phase 4.5 (verifier sub-agent) and passes the contents verbatim. Empirical findings (Krebs / CERT-FR / RSS shapes / listing-page drop), bridge-fetcher hostnames, WebFetch outbound-links template, Discovery-trace requirements, return format, operational guardrails all live there.
  - **Phase 5.5 FAIL-fix recipes** → `docs/check-brief-fixes.md` (cve-sync, footer-presence, run-log-fields, run-log-subagents, sources-touched, footer-taxonomy, fetch-source-403, multi-cve-cvss, blocked-source NVD/news, source-urls 404).
- **Prose tightened** throughout (audience description, execution environment, Phase 5 sources/sources.json bookkeeping, META section) without removing rules or examples — terser sentences, fewer redundant repetitions of already-stated rules.

### Weekly prompt — `prompts/weekly-summary.md`
- Same externalisation pattern: research-sub-agent and verifier spawn templates → `docs/spawn-templates.md`; reference template → `docs/brief-template.md` (under the "Weekly summary reference template" heading); FAIL-fix recipes → `docs/check-brief-fixes.md`.
- W-PD-1 weekly-editorial-framing rule, six Phase 1 working lists (with the inaction-=-incident list as the editorial centre), 11-section output structure, weekly-specific § 1 framing, all 15 hard invariants + 2 W-INV addenda preserved verbatim.
- The verifier check 11 in the shared spawn template now carries the weekly-specific W-PD-1 question; the F7 finding category in the shared spawn template now covers the weekly-specific drop case for "pure one-to-one daily-brief summary".

### `docs/spawn-templates.md` (NEW)
Single canonical home for both spawn templates:
1. **Research sub-agent spawn template** — passed verbatim by both daily Phase 1 and weekly Phase 2. Contains the full operational guidance the sub-agent depends on: defender-vantage opener, link-discipline clauses, MANDATORY bridge-fetcher rules for known-403 hosts (CISA, NCSC.ch, CSIRT Italia, UK ICO, Inside IT, PRODAFT, DataBreaches, NCC Group, Cisco Talos), `WebFetch` outbound-links prompt template, both empirical rules (Krebs feed 13-outbound-links test; CERT-FR per-advisory carries vendor citations from "Documentation"/"Références"), the BSI WID-SEC / NCSC-NL / NCSC-CH CSH / ENISA EUVD same-shape note, `<content:encoded>` vs `<description>` RSS distinction, "silent loss of outbound links is the failure mode that turns a brief into a dead-end stub" warning, Discovery-trace requirements + 3 example shapes + 6 mandatory rules, sub-agent return format with all required fields, operational guardrails.
2. **Verifier sub-agent spawn template** — passed verbatim by both daily Phase 4.5 and weekly Phase 3.5. Truth checks 1–4, editorial-quality checks 5–10, whole-brief checks 11–13 (check 11 carries the weekly-specific W-PD-1 question), return format with finding categories F1–F11 (F7 covers the weekly-specific drop case for pure one-to-one daily summaries), verdict line.
3. **"What this verification phase fixes"** catalog of editorial defects the loop catches.

### `docs/brief-template.md` (NEW)
Single canonical home for the rendered output skeletons:
- **Daily brief reference template** — exact heading hierarchy (§§ 0–8), AI-content-notice text, `Generated by:` metadata line, footer placement per section, § 3 vulnerability secondary-aggregation table.
- **Weekly summary reference template** — exact heading hierarchy (§§ 0–10), AI-content-notice text, `Generated by:` metadata line, footer placement per section, § 3 vulnerability roll-up table.
- **Worked-good § 2 fragment** — illustrative npm supply-chain compromise showing the technical-depth bar (osascript / powershell.exe -enc launched from npm/node parent-process trees, DoH C2, mapped to `T1195.002` / `T1071.004`, with detection + hardening tied to the specifics).

### `docs/check-brief-fixes.md` (NEW)
Operator playbook of FAIL-message → fix-action mappings for the most common `tools/check_brief.py` failures, plus WARN-level signal explanations.

### Net effect
- Daily master prompt: ~45K → ~24K tokens, fits in a single default `Read` call.
- Weekly master prompt: ~17K → ~14K tokens, fits in a single default `Read` call.
- No operational content lost; ALL schemas, commands, empirical findings, and rules preserved either in the master prompts or in the externalised docs.

### Routine integration
- Daily Phase 1 reads `docs/spawn-templates.md` once before spawning S1–S4 in parallel; uses the verbatim research-sub-agent template per spawn.
- Daily Phase 4 reads `docs/brief-template.md` once before composing.
- Daily Phase 4.5 reads `docs/spawn-templates.md` once before spawning the verifier (already in context if read in Phase 1; the agent can re-use the loaded copy or re-Read for a fresh copy of the verifier-template section).
- Weekly Phase 2 / Phase 3 / Phase 3.5 follow the same pattern.

### Compatibility
- Output artefacts (daily brief, weekly summary, state JSON, footer format, taxonomy) are unchanged.
- `tools/check_brief.py` and `site/test_build.py` continue to enforce the same checks unchanged.
- Hard invariants list is unchanged (15 items + W-INV-1 / W-INV-2).

---

## 2.32 — 2026-05-08 (WebFetch outbound-links discipline + sources audit cleanup)

### Why
Operator audit of the source set found that the agent's link-traversal — pivoting from a news article to the vendor PSIRT, from a national-CERT advisory to the vendor blog it cites, from a research-lab post to the GitHub commit that fixed the bug — was failing silently inside the `WebFetch` tool. `WebFetch` returns a small-model summary of the fetched HTML, and **without an explicit prompt instruction the summariser drops every URL.** Sub-agents were getting prose-only summaries, with no citation chain to follow, so they hit dead ends on the news → primary pivot mandated by Phase 1 step 2.

Two empirical findings from the audit (both reproducible against current sources):
- Listing pages (e.g. `https://krebsonsecurity.com/`, `https://www.bleepingcomputer.com/news/security/`) return article titles + entity mentions but **zero outbound links** — article bodies are not on the index. To pivot, the agent has to drill into a specific article URL.
- Per-advisory CERT pages (e.g. `https://www.cert.ssi.gouv.fr/avis/CERTFR-YYYY-AVI-NNNN/`) return the full CVE list **and** the vendor advisory URLs in their "Documentation" / "Références" section — **but only when the prompt explicitly asks for `Outbound links`**. Same for `<content:encoded>` RSS feeds (Krebs, Schneier).

### Daily prompt — `prompts/daily-cti-brief.md`

- **New mandatory clause in the sub-agent spawn template** ("`WebFetch` prompt template — every call MUST request 'Outbound links'…"): every `WebFetch` call must append an explicit instruction to enumerate every URL in the body / References / Documentation / Sources section, formatted as bullets with full absolute URLs. Without this clause the call returns a dead-end summary.
- **New "Research methodology" item 3** with the full `WebFetch` prompt template, the two empirical rules (listing pages don't carry inline links — drill into a specific article URL; per-advisory CERT pages and `<content:encoded>` RSS preserve the citation chain), and worked examples (Krebs feed returned 13 outbound URLs from one article; CERT-FR per-advisory page returned the Ivanti vendor URLs from its References section).
- Renumbered the methodology items (`Search topically` is now item 4, `Propose new sources` is item 5).
- Added DataBreaches.net and NCC Group to the named-403-host list (now require `tools/fetch_source.py`).

### Weekly prompt — `prompts/weekly-summary.md`
- Same mandatory `WebFetch` prompt clause inserted into the sub-agent spawn template, with a back-pointer to `prompts/daily-cti-brief.md` § "Research methodology" item 3 for the full template.

### `sources/sources.json` — comprehensive audit + dedup + add 30 sources (separate commit, v2 schema)
- **Removed (4):** `govcert-ch` (exact-URL duplicate of `ncsc-ch-security-hub` — GovCERT was merged into NCSC.ch in 2023), `secureworks-ctu` (Sophos absorbed it; redundant with `sophos-xops`), `sec-ir-firms-edr-blogs` (techcommunity.microsoft.com now redirects to Microsoft OAuth login — unfetchable), `reddit-netsec` (WebFetch is host-blocked from reddit.com).
- **URL corrections** for sources whose canonical home moved or whose listing was a JS-rendered shell: `kudelski-security` → `kudelskisecurity.com/research-blog`; `trustwave-spiderlabs` → `levelblue.com/blogs/spiderlabs-blog` (rebrand); `crowdstrike` → `/counter-adversary-operations/` (legacy /threat-intel-research/ now redirects); `bsi-de` → RSS (HTML is JS-rendered SPA); `darkreading` → RSS (HTML 403's WebFetch UA); `redcanary` → RSS (resource hub returns nav-only); `akamai-sirt` → FeedBurner (HTML is nav-only shell); `projectzero` → `projectzero.google` (Blogspot legacy).
- **Added (30 sources)** spanning national CERTs (NL/IE/BE/JP/KR), vendor PSIRTs (Cisco/Apple/Oracle/Mozilla/Chrome/MSRC/GitHub), research labs (Google TAG, SentinelLabs, Team Cymru, Censys, 0patch, Snyk, Trail of Bits, ProjectDiscovery, Morphisec, KELA), regional CTI vendors (Intrinsec, Synacktiv, Lab52, Resecurity), OT/ICS specialists (Nozomi, Claroty), ransomware tracking (ransomware.live), news (Hacker News, Infosecurity Magazine, Risky Biz News), and sanctions (US Treasury OFAC).
- **New schema fields:** per-source `fetch_method` (`webfetch` / `rss` / `bridge` / `api` / `blocked`); top-level `fetch_methods` documentation block; new categories `vendor-psirt`, `ransomware`, `sanctions`. Every source's `notes` field now records the 2026-05-08 audit verdict and concrete RSS / bridge fallback.
- **Bridge allowlist (`tools/fetch_source.py`)** extended with `databreaches.net`, `www.nccgroup.com`, `www.dragos.com`, `www.sygnia.co`, `www.ccn-cert.cni.es` for sources where Claude Code's WebFetch UA is filtered.

Total: 114 sources (up from 85), 94 active / 18 candidate / 2 demoted. Coverage: Switzerland + EU + US + UK + DACH + Nordics + Iberia + Italy + Poland + Czechia + Ireland + Netherlands + Belgium + Japan + Korea, plus all major CTI vendors with publicly-available research.

---

## 2.31 — 2026-05-08 (neutralise vendor / product / actor / CVE biases in worked examples)

### Why
Operator audit of `prompts/daily-cti-brief.md` and `prompts/weekly-summary.md` found that worked examples and illustrative fragments throughout both prompts named specific vendors, products, actor clusters, advisory IDs, and CVE IDs. Earlier versions used these as concrete pedagogy ("a freshly-disclosed pre-auth RCE on Citrix NetScaler / Ivanti Connect Secure / Fortinet SSL-VPN", "named campaigns / clusters when available (`UNC5337`, `Storm-2077`, `CL-STA-1132`, `RomCom`, `Akira`, `Fog`)", "Ivanti EPMM CVE-2026-5787 → CVE-2026-6973"). The same pattern appeared in the discovery-trace examples (named Ivanti EPMM URLs verbatim), the URL-pattern do/don't table (named Microsoft / Palo Alto / Ivanti vendor PSIRT roots as the "good" example), the news-to-primary pivot guidance (BleepingComputer / Mandiant / CrowdStrike / Heise / CERT-FR), the Phase 4.5 verifier's example findings (`APT28 active against EU governments`, `CVE-2023-35078 was exploited by APT29`), and the worked-good § 2 fragment (Google Chrome cookie paths + Cloudflare Workers DoH resolver).

These specifics created two distinct biases in the agent:

1. **Topic bias toward the named vendors / products / actors / CVEs.** When a prompt example names "Ivanti EPMM CVE-2026-6973", the agent is more likely to over-cover Ivanti EPMM stories and CVEs in that ID neighbourhood — even when Phase 1 sub-agents surface a more relevant story elsewhere.
2. **Anchor bias for nexus tags.** Footer template examples consistently used `china-nexus`. Without intent, this biased the rendered footers' nexus tag toward China-attributed activity when other nexus tags (or no nexus tag) was the correct call.

### Daily prompt — `prompts/daily-cti-brief.md`

Worked examples rewritten as **structural pattern descriptions** rather than topic picks. The pedagogical value is preserved (the agent still sees what the example is teaching) but the names that biased topic selection are replaced with placeholders:

- **Audience description.** Removed the named research-lab list (Mandiant / GTIG / Volexity / Talos / Unit 42 / Project Zero) and the explicit red-team-tooling roll-call (BloodHound / Mythic / Sliver / KrbRelayUp / etc.). Replaced with a description of the *technique classes* the audience is fluent in — offensive-tooling terminology, identity-protocol abuse (Kerberos / OAuth / SAML), endpoint-evasion classes, kernel-callback-level techniques.
- **PD-1 background-context example.** "APT28 is attributed to GRU Unit 26165" → generic "actor-to-government-unit attributions, infrastructure-to-actor mappings, multi-year campaign histories".
- **PD-1 URL-construction example.** "Securelist post on Amazon SES BEC must live at securelist.com/amazon-ses-bec-campaign-2026/" → generic "inferring that a research lab's post about a given topic + year *must* live at `https://<lab-domain>/<topic-slug>-<year>/`".
- **PD-8 long-running-campaign examples.** "Ivanti waves, Salt Typhoon, ransomware crew turnovers" → generic shape descriptions ("sustained edge-device exploitation waves against any vendor's product family, long-running named-cluster operations regardless of nexus, ransomware-affiliate turnovers and rebrands").
- **PD-9 annual-reports list.** Removed the enumerated publisher list (Mandiant M-Trends, CrowdStrike Global Threat Report, Verizon DBIR, Microsoft Digital Defense, IBM X-Force, Truesec TIR, Dragos OT Year in Review, Cloudflare Cloudforce One). Replaced with a publisher-agnostic class definition.
- **Phase 1 sub-agent template — discovery trace example.** The "Ivanti EPMM CVE first surfaced via the French national CERT and pivoted to Ivanti's PSIRT" example is now a generic "vulnerability in some enterprise edge product first surfaces via a national CERT advisory and the agent pivots to the affected vendor's own PSIRT bulletin" with `<placeholder>` URLs.
- **Phase 1 sub-agent template — URL-construction example.** "the advisory ID is `CERTFR-2026-AVI-0551`…" → "because an advisory ID has a known format, its detail page must live at a derivable path on the issuing CERT's site".
- **Discovery trace examples in sub-agent return format section** (lines 245–247). The three concrete trace examples (Ivanti / Heise → Spiegel / search → BleepingComputer → CCB Belgium → Ivanti) are now structural patterns with `<source-id>` and `<full URL fetched>` placeholders.
- **News-to-primary pivot examples** (line 195). "BleepingComputer summarising Mandiant; The Record covering CrowdStrike; Heise reporting on a CERT-FR advisory" → generic "a security-news publisher summarising a vendor research lab; a regional tech outlet relaying a national-CERT advisory; a wire service rewriting a vendor PSIRT post".
- **Forbidden-Source URL examples** (line 207). The named publisher URLs (heise.de, nos.nl, securelist.com, dragos.com, cert.ssi.gouv.fr, abw.gov.pl) are replaced with `<news-site>/news/` / `<lab-domain>/year-in-review/` / `<cert-domain>/advisories/` / `<gov-domain>/cybersecurity/` pattern descriptions.
- **Mandatory-rules pivot example.** "→ Ivanti PSIRT → primary" → "→ <vendor> PSIRT → primary".
- **Hard-blocked URL patterns table** (line 389). The "Good — what to use instead" column previously named `msrc.microsoft.com/update-guide/...`, `security.paloaltonetworks.com/CVE-…`, `www.ivanti.com/blog/…`. Replaced with publisher-agnostic guidance ("the disclosing vendor's PSIRT advisory page for the CVE — pivot to whichever one actually owns the disclosure"). The "Bad" column also genericised (no longer lists specific publisher domains).
- **Phase 5.5 fabricated-URL examples.** Removed `https://securelist.com/amazon-ses-bec-campaign-2026/` and `https://www.deepinstinct.com/blog/muddywater-2026` — replaced with a description of the failure mode ("URLs the agent constructed by guessing a slug from the topic + year rather than fetching a real page").
- **Phase 4.5 verifier flagging language.** "`Source: CERT-FR` as the **only** source" → "any single national-CERT URL as the **only** source on a CVE-typed item".
- **Multi-CVE chain examples** (lines 410–417, 422–424). "Ivanti EPMM CVE-2026-5787 → CVE-2026-6973: cert-validation flaw chains to admin RCE" / "CERT-FR CERTFR-2026-AVI-0551 listing 7 GLPI CVEs" → generic shapes ("a vendor's monthly patch advisory disclosing a chain where one CVE prerequisites another", "a national-CERT advisory grouping multiple CVEs in a single product family"). All `CVE-2026-5787` / `CVE-2026-6973` IDs in the worked footer / breakdown examples replaced with `CVE-YYYY-NNNNN` / `CVE-YYYY-MMMMM`.
- **Section template CVE placeholders** (lines 562, 576, 580, 614). `CVE-2026-XXXXX` (which still anchored the agent to 2026-era CVE IDs) → `CVE-YYYY-NNNNN` (the standard placeholder convention used elsewhere in the prompt).
- **§ 1 Immediate Actions examples** (line 456). "freshly-disclosed pre-auth RCE on Citrix NetScaler / Ivanti Connect Secure / Fortinet SSL-VPN" → "freshly-disclosed pre-auth RCE on a widely-deployed internet-exposed enterprise edge appliance class (any vendor)".
- **Technical-depth attack-surface examples** (line 486). The named-product list (`wp-login.php`, `nginx-quic`, Citrix NetScaler AAA virtual server, AD `MS-RPRN`, `dsamain.exe`, SAP `Visual Composer` MetaEditor servlet) → a publisher-agnostic enumeration of *types* of attack surface ("a specific PHP page on a CMS, a worker process inside a web server, an authentication virtual server inside an edge appliance, an RPC interface inside an OS service, an LDAP listener daemon, a specific servlet inside an enterprise application"). The rule "Use whatever the source actually states — never substitute generic phrasing" is preserved.
- **Named-cluster examples** (line 490). The literal cluster IDs `UNC5337`, `Storm-2077`, `CL-STA-1132`, `RomCom`, `Akira`, `Fog` → publisher-agnostic naming-format hints (`UNC####`-style, `Storm-####`-style, `TA####`-style, `APT##`-style, `CL-###-####`-style).
- **Detection / EDR product names** (line 491). "Defender for Identity / Falcon Identity Protection alert names, Velociraptor / Kape collection targets" → "identity-protection / EDR alert-name patterns, DFIR collection-target categories". Standard log-source / event-ID references (Sysmon EID 1, 4624 / 4663 / 4769, S4U2Self, ntds.dit, etc.) are kept — those are protocol- and OS-level primitives, not vendor topic bias.
- **Stack-corroborating-primaries example** (line 519). "Mandiant blog + CISA joint advisory + Microsoft Threat Intel post" → "an independent research lab's blog, a government joint cybersecurity advisory, and a major-vendor threat-intel post".
- **Reference template footer examples** (lines 572, 608). Default `china-nexus` tag in the worked § 2 and Deep Dive footers → `<nexus-tag-from-taxonomy-if-applicable>`. The taxonomy still defines the full nexus-tag list (`china-nexus`, `russia-nexus`, `north-korea-nexus`, `iran-nexus`, `us-nexus`, `eu-nexus`); the change just stops biasing the *example* toward one specific nexus.
- **Phase 4.5 verifier example findings.** "Source: [NVD — CVE-…] / [CERT-FR — CERTFR-…]" → "an NVD/MITRE/cve.org per-CVE page or a national-CERT advisory page". `https://heise.de/news/` → "a homepage / category landing (no article slug)". "APT28 active against EU governments" → "<named actor> active against <victim class>". "508 EU on-premises instances internet-reachable (Censys/Shodan telemetry)" → "<specific aggregate number> on-premises instances internet-reachable (<vendor> telemetry)". "CVE-2023-35078 was exploited by APT29 within days" → "<CVE ID> was exploited by <named actor> within days".
- **Worked-good § 2 fragment** (line 496). The supply-chain example previously named `Google Chrome` cookie paths verbatim and a `Cloudflare-Workers-hosted resolver`. Replaced with publisher-agnostic phrasing ("each browser's per-profile cookie store on disk", "an attacker-operated edge-serverless resolver"). The fictional `@org/x-cli` package, the version range, the OS-intrinsic execution methods (`osascript`, `powershell.exe -enc`), the MITRE technique mapping, and the detection / hardening guidance are kept — those are pedagogical, not topic bias. Date in the inline citation neutralised to `YYYY-MM-DD`.
- **Phase 5.5 blocked-source-pattern enumeration** (line 896). The named-publisher domain list (heise.de variants, nos.nl variants, cert.ssi.gouv.fr, dragos.com, abw.gov.pl) replaced with shape descriptions; the **full pattern list with concrete domain examples drawn from sources in `sources.json`** continues to live at the top of `tools/check_brief.py`. The script — which the operator owns and edits to track real source-rotation patterns — is the right place for concrete domain enumeration; the prompt is the wrong place because every domain it names becomes an anchor.
- **Phase 5.5 "How to fix" table example** (line 918). The specific Heise article URL example replaced with a structural description.

The bridge-fetcher operational guidance (Phase 1 — `tools/fetch_source.py` with the explicit `cisa.gov` / `ncsc.admin.ch` / `acn.gov.it` / `ico.org.uk` / `inside-it.ch` / `prodaft.com` / `talos` host enumeration) is **kept verbatim** — those are operational facts about which specific source IDs in `sources.json` need the bridge for HTTP 403 reasons. They tell the agent *how to fetch these sources*, not *what to write about*. Replacing them with placeholders would break the bridge-mandate.

The national-CERT carve-out enumeration in PD-5 (NCSC-CH, GovCERT.ch, CERT-EU, ENISA, BSI, ANSSI/CERT-FR, NCSC-UK, NCSC-NL, CISA, CCN-CERT, AGID-CSIRT-IT, CERT.at, CERT-PL) is also kept — that list is the operational allow-list for the single-source verification carve-out, not topic guidance.

The CVE primary-source order (vendor advisory > national CERT/CSIRT > MITRE/NVD > ENISA EUVD > researcher write-up > aggregator) is kept — it's an operational priority order for the agent to follow when selecting primaries, not a topic-selection bias.

### Weekly prompt — `prompts/weekly-summary.md`

Same rewrites applied where the weekly carries equivalent worked examples:

- **Audience description.** Same de-naming as the daily.
- **Hard-blocked URL pattern examples** (line 258). Specific publisher URLs → shape descriptions.
- **§ 7 long-running-campaign template footer** (line 389). Default `china-nexus` tag → `<nexus-tag-from-taxonomy-if-applicable>`.
- **Phase 3.5 verifier example findings**. `https://heise.de/news/` → "a homepage / category landing (no article slug)".

The weekly's `CVE-YYYY-NNNNN` placeholders were already in the recommended form across §§ 1, 3, 7 — no normalisation needed.

### Out of scope for this version

- `tools/check_brief.py` is intentionally **not edited**. The script is allowed (and expected) to enumerate concrete domain patterns drawn from `sources/sources.json` — that's where source-rotation reality is encoded. The prompt was the wrong place because it was being read by the agent as authoritative topic guidance every run.
- `site/taxonomy.yaml` is unchanged. The full nexus-tag set (`china-nexus`, `russia-nexus`, `north-korea-nexus`, `iran-nexus`, `us-nexus`, `eu-nexus`) remains available; only the *example footers in the prompt* stopped defaulting to one specific nexus.
- The `briefs/` archive is unchanged. Past briefs continue to ship with the names and CVEs that were live at the time.

---

## 2.30 — 2026-05-08 (weekly prompt rewritten on top of the daily's institutionalised stack + new editorial intent)

### Why
v2.28 + v2.29 institutionalised seven things in the **daily** prompt — the dual-axis Phase 4.5 verifier, the iterative refinement loop with up to three follow-up research sub-agents, the `tools/check_brief.py` Phase 5.5 gate, the multi-CVE / multi-source / multi-primary footer rules, the "avoid NVD/CERT as primary" rule with a hard-blocked URL allowlist, the `tools/fetch_source.py` mandate for CISA + NCSC.ch every run, and the `state/run_log.json` Ops-dashboard schema. The **weekly** prompt was still on the v2.23-era structure (single round of W1/W2 horizon research, inline Phase 4.5 shell snippet, no verification sub-agent loop, no blocked-URL list, no fetch_source.py mandate). The two prompts had diverged.

Plus the operator surfaced a missing editorial framing for the weekly: it was being authored as a one-to-one rollup of the dailies. The weekly's actual job is the strategic-horizon view + an explicit "what would be on fire if no one acted on the dailies" register — items where active exploitation continued through the week, where a CISA KEV deadline passed, where a campaign is still acquiring victims, where a patch window closed. Pure recap is not weekly content.

### Weekly prompt — `prompts/weekly-summary.md` (full rewrite on top of the daily's institutionalised stack)

- **New editorial intent block at the top** ("What the weekly is for — and what it is NOT"). Three explicit lenses:
  1. *What would be on fire by Monday morning if no one had acted on the dailies this week* — Mon-morning escalation register.
  2. *The strategic-horizon view a daily reader cannot see from any single day* — multi-day chains, sectoral pressure, long-running operator turnovers, regulatory shifts.
  3. *The longer arc on items the dailies could only sketch* — the disclosure-only-Monday-but-KEV-by-Friday case.

  Repetition without one of these lenses is padding.

- **New W-PD-1 prime directive.** Every weekly item must answer one of the three questions above. Items that don't get dropped in Phase 3.5 even if they were prominent in a daily.

- **Phase 1 Structured review** gains a sixth working list: **"Items where inaction = incident"**. Built from lists 1–3 by asking *if a Swiss / EU public-sector SOC reader did not act on this when it appeared in the daily, would they currently be in an incident?* This list drives the new § 1 framing.

- **Output structure (NORMATIVE)** keeps the 11-section layout but renames § 1 from *"Top stories of the week"* to *"Highest-impact events — what's on fire if no one acted"*. Each H3 in § 1 leads with a one-line **"If you did nothing this week:"** framing — operational reality of what's currently breaking. § 1 may be empty when no item from the week continued to be operationally critical at week-end; the prompt requires explicit empty-stub text in that case.

- **Phase 2 horizon sub-agents (W1, W2)** spawn template now mirrors the daily's: explicit primary-source bias, hard-blocked URL list reference, NVD/MITRE/cve.org per-CVE blocked outright as primary Source, mandatory `tools/fetch_source.py` for CISA + NCSC.ch.

- **Per-item metadata footer (NORMATIVE)** matches the daily verbatim: multi-source forms (`Source: [a](u) · [b](u) · [c](u)` and the `Additional source:` form, both supported), multi-primary case examples (vendor advisory + research blog, vendor + 8-K, CERT + vendor), avoid-NVD/CERT-as-primary rule with the narrow exceptions, hard-blocked URL patterns referenced from the daily's full list, multi-CVE per-CVE breakdown syntax (`CVSS: 9.1 / 7.2`, `Auth: pre-auth (CVE-…), admin-required (CVE-…)`).

- **NEW Phase 3.5 — Final verification sub-agent (URL truth + editorial quality, loop until clean)**. Mirrors the daily's Phase 4.5 with weekly-specific framing in the editorial-quality gate: every item must answer one of W-PD-1's three questions or get flagged for drop. Truth gate identical (every URL fetched, every claim cross-checked, every named entity grounded). Loop cap: 3 iterations. Main agent may spawn up to 3 follow-up research sub-agents per iteration for `Needs more research` / `Missed angles`. Iteration count + residuals written to `run_log.json`.

- **Phase 4 State update** adds the `state/run_log.json` weekly-specific schema with `iso_week`, `kind: "weekly"`, `sub_agents: { W1, W2 }`, every Ops-dashboard-required field. Same population rules as the daily.

- **NEW Phase 4.5 — Self-check gate via `python3 tools/check_brief.py briefs/weekly/YYYY-Www.md`**. Replaces the v2.23 inline shell snippet. Same script, same 17-check inventory, with weekly-aware section keys (`weekly-top-stories`, `weekly-multi-day`, `weekly-vuln-rollup`, `weekly-incidents-recap`).

- **Hard invariants — 9 → 15 + 2 weekly-specific (W-INV-1, W-INV-2).** The weekly now mirrors the daily's 15 invariants (Phase 3.5 verification loop, Phase 4.5 script gate, fetch_source.py mandate, run_log.json populate). New weekly invariants: every item answers W-PD-1's three questions; § 1 frames items as "what's on fire if no one acted".

- **Quality gates** updated to include the W-PD-1 framing check, the Phase 3.5 verification check, the script invocation, the multi-CVE breakdown rule, the NVD/CERT-as-only-primary rule, the run_log population check.

### Script — `tools/check_brief.py`

- **Now kind-aware.** `resolve_brief_path` accepts `YYYY-Www` and routes to `briefs/weekly/`. `detect_brief_kind` reads the filename pattern and returns `("daily", date, None)` or `("weekly", date, iso_week)`.
- New section keys for the weekly (`weekly-glance`, `weekly-top-stories`, `weekly-multi-day`, `weekly-vuln-rollup`, `weekly-sector-patterns`, `weekly-incidents-recap`, `weekly-annual-reports`, `weekly-long-running`, `weekly-policy`, `weekly-looking-ahead`).
- `check_section_h3_coverage` — for weekly, requires `weekly-top-stories`, `weekly-multi-day`, `weekly-vuln-rollup`, `weekly-incidents-recap`. Empty weekly-top-stories is acceptable when the body explicitly states `no item .{0,40}continued to be operationally critical` or similar — the v2.30 inaction-=-incident framing.
- `check_h3_footers`, `check_multi_cve_footers`, `check_blocked_source_patterns`, `check_primary_source_quality` — all thread `kind` through; weekly variants target the weekly section keys.
- `check_run_log_for_today` — picks the right run record by `(kind, iso_week)` for weekly, by `(kind, date)` for daily. Weekly's required schema: `iso_week`, `kind`, `sub_agents: { W1, W2 }`, no `deep_dive`. Daily unchanged.
- The `updates-citations` check only fires for daily briefs; the weekly's § 7 (Long-running campaigns) is regular H3 + footer, not UPDATE blockquotes.
- The `covered-items` heuristic is daily-only (the weekly logs `weekly_summary` appearances which the heuristic doesn't model).

### Daily prompt — `prompts/daily-cti-brief.md`

Minor cleanup: dropped the "Run with `--no-link-check` for offline test runs only." parenthetical from two places (per-item-metadata-footer NVD section + Phase 5.5 check inventory). The flag still exists in the script for ergonomics; it just isn't documented in the prompt — Phase 5.5 always runs the live URL check.

---

## 2.29 — 2026-05-08 (blocked-URL allowlist + live URL HEAD check + every external link opens in new tab)

### Why
Three operator-visible defects in the 2026-05-08 brief and rendered site:

1. **NVD/MITRE per-CVE pages and generic landings still appeared as `Source:` entries.** The 2026-05-08 brief cited `https://nvd.nist.gov/vuln/detail/CVE-2026-5787`, `https://www.heise.de/news/`, `https://nos.nl/artikel/`, `https://www.dragos.com/year-in-review/`, `https://abw.gov.pl/pl/cyberbezpieczenstwo/` — derived data sheets and category landings, not disclosing-party content. v2.28 had this as a soft WARN; v2.29 escalates it to a hard FAIL backed by an explicit blocked-URL list in `tools/check_brief.py`.

2. **Fabricated URLs** like `https://securelist.com/amazon-ses-bec-campaign-2026/`, `https://www.surf.nl/actualiteiten/2026/canvas-security-update`, `https://www.deepinstinct.com/blog/muddywater-2026` looked plausible but 404. The Phase 4.5 verifier was supposed to catch these by fetching every URL — but a local pre-publish check had no equivalent. v2.29 adds it to `tools/check_brief.py` so the operator sees the same FAIL signal at commit time.

3. **External links opened in the same tab**, costing the reader the brief tab on every citation click. The Markdown renderer's `<a>` emission carried `rel="noopener noreferrer"` but no `target="_blank"`. The `_rewrite_about_links` pass on docs/* pages also didn't add target when the rewrite turned a relative path into a `github.com/.../blob/main/...` URL.

### Daily prompt — `prompts/daily-cti-brief.md`

- **Per-item metadata footer (NORMATIVE) gains a "Hard-blocked URL patterns" subsection.** Lists every NVD/MITRE per-CVE pattern, the four "/news/", "/security", landing-page Heise variants, NOS landing pages, CERT-FR `/avis/` and `/actualite/` index roots, CISA news-events root, Dragos year-in-review marketing landing, ABW category landing, and the rule-of-thumb (if dropping the trailing path component still resolves to a meaningful page, the URL is too generic). Includes a Bad → Good table mapping each blocked pattern to the right vendor PSIRT / research-blog URL pattern.
- **Phase 5.5 check inventory expanded** from 17 → 19 checks. New entries:
  - `blocked-source` (FAIL) — host + path pattern match against the v2.29 blocked-URL list.
  - `source-urls` (FAIL on 404, WARN on other non-200) — live HEAD/GET on every Source URL in every footer. Includes a Mac local-Python SSL-trust-store pre-flight: if the local Python lacks a CA bundle, the check emits a single environment-level WARN and skips the per-URL loop. CI on Linux runs the check normally.
- **Phase 5.5 "How to fix common FAILs" table** gains entries for `blocked-source: ... cites NVD per-CVE`, `blocked-source: ... cites heise.de/news/` (or any landing), and `source-urls: <url> returns 404`.

### Site — `site/build.py`

- **`render_inline` Markdown link emission** now adds `target="_blank"` for any href starting with `http://`, `https://`, or `mailto:`. Internal/relative links keep current-tab navigation. Every inline citation in every brief now opens in a new tab.
- **`render_footer_html` source pills** add `target="_blank"`. Footer source links open in a new tab.
- **`_rewrite_about_links`** — when a relative path in `docs/*.md` gets rewritten to `https://github.com/<repo>/blob/main/<path>`, the rewriter now adds `target="_blank"` to the resulting anchor.
- **404 page's GitHub-issues link** had `rel="noopener noreferrer"` but no target — fixed.

Full-site audit after the fix: 911 external anchors, 0 missing `target="_blank"`. 4525 internal anchors, 9 deliberately carrying `target="_blank"` (RSS-feed chips on the briefs index — pre-existing UX choice).

### Tests

`site/test_build.py` gains:
- `external link target=_blank` — `render_inline` emits `target="_blank"` for `https://` hrefs.
- `external link rel noopener` — accompanying `rel="noopener noreferrer"`.
- `relative link no target` — `#anchor` and other relative hrefs do *not* pick up the target.

---

## 2.28 — 2026-05-08 (institutionalised self-check script + multi-CVE / multi-source footers + Phase 4.5 quality gate + mandatory fetch_source.py for CISA + NCSC.ch)

### Why
The 2026-05-08 run exposed three classes of drift that the v2.27 prompt could not catch on its own:

1. **The Phase 5.5 self-check was a copy-paste of inline shell snippets**: the agent reproduced them imperfectly run-to-run, and any new check (e.g. footer-field completeness, `run_log.json` Ops-dashboard population, primary-source quality, multi-CVE hygiene, IOC heuristic) had to be added in the prompt and re-pasted by the agent. The 2026-05-08 inline check found 5 CVEs missing from `cves_seen.json` — useful, but did not also catch that `run_log.json` was empty (Ops dashboard renders `—` cells), that 4 CVE entries cited NVD/CERT-FR as the *only* primary source instead of the vendor advisory, that CISA was 403'd without `tools/fetch_source.py` mitigation, or that the 2026-05-08 brief had Ivanti EPMM CVE-2026-5787 + CVE-2026-6973 as a multi-CVE footer that needed per-CVE CVSS breakdown.

2. **The Phase 4.5 verification sub-agent was URL-truth only.** It caught fabricated and broken URLs but did not assess *editorial quality*: relevance to a Swiss / EU public-sector SOC, primary-source strength (NVD/CERT cited as sole primary on items where a vendor PSIRT advisory existed), vendor-marketing tells, missed angles a senior reader would expect.

3. **Multi-CVE / multi-source footer patterns were happening organically but not documented.** The 2026-05-08 brief used `CVE: CVE-2026-5787, CVE-2026-6973 · CVSS: 9.1 (CVE-2026-5787), 7.2 (CVE-2026-6973)` and `Source: [Ivanti — …](url) · [NVD — …](url) · [The Hacker News — …](url)` — both correct, both unparseable as conventions because the prompt didn't spell them out.

### Daily prompt — `prompts/daily-cti-brief.md`

- **New `tools/check_brief.py`** — institutionalised, version-controlled, stdlib-only Python script that imports `parse_footer_line` / `validate_footer` / `parse_taxonomy` from `site/build.py` so script and build agree on parsing rules. Bundles 17 checks: state JSON parses · taxonomy loads · core sections present (title-based, schema-neutral about § numbering) · AI-content notice · IOC heuristic scan with version-string false-positive suppression · CVE sync · UPDATE inline citations · footer presence (skips Markdown thematic breaks `---`) · footer Source/Tags/Region/CVE-fields completeness · footer taxonomy validation · multi-CVE per-CVE CVSS breakdown · primary-source quality (warns on NVD/CERT as sole primary) · `tools/fetch_source.py` enforcement on known-403 hosts · `covered_items.json` appearance heuristic · `run_log.json` Ops-dashboard fields fully populated · `sources.json` last-fetched bookkeeping · `site/test_build.py` smoke tests. Read-only by design — agent fixes drift, script reports it. Non-zero exit aborts the commit.

- **Phase 5.5 rewritten** — replaces the six inline shell snippets with a single `python3 tools/check_brief.py` invocation, lists the 17 checks the script bundles, and ships a "How to fix common FAILs" table so the agent has a recipe for each `FAIL` line.

- **Phase 4.5 widened from URL-truth-only to URL-truth + editorial-quality.** The verification sub-agent's spawn template now also assesses (per item) relevance to a Swiss / EU public-sector SOC, primary-source strength with explicit guidance to flag NVD/MITRE/CERT-as-sole-primary, vendor-marketing tells, fake-news patterns, contradictions, and clarity. Whole-brief checks added: coverage shape, style discipline, missed angles. The verifier now returns 5 additional finding categories (`Strengthen primary source`, `Drop`, `Needs more research`, `Surface contradiction`, `Missed angles`) on top of the 5 truth categories from v2.27. The main-agent loop authorises spawning **≤3 follow-up research sub-agents per iteration** for `Needs more research` / `Missed angles` findings — iterative refinement so unclear or under-sourced items can be deepened rather than dropped on the spot. Iteration cap stays at 3 (the brief must publish).

- **`tools/fetch_source.py` is now MANDATORY for CISA + NCSC.ch every run.** The Phase 1 research-methodology section says: do not even attempt `WebFetch` on `cisa.gov` / `www.cisa.gov` / `ncsc.admin.ch` / `ncsc.ch` first — go straight to the bridge. Phase 5.5's script FAILs the commit if `run_log.json.fetch_failures` lists a 403/429 on a known-403 source id without bridge mitigation. The 2026-05-08 brief skipped CISA because of an unhandled 403 — this run-class drift is now caught both ways.

- **Multi-CVE / multi-source / multi-primary footer pattern documented in the per-item metadata footer (NORMATIVE) section.** Three new subsections:
  - **Multi-source — primary + corroborating in the same footer.** Two equivalent forms supported: `Source: [a](u) · [b](u) · [c](u)` (preferred for 2–4 sources) and `Source: [a](u) · Additional source: [b](u) · Additional source: [c](u)`. Both parse to the same structured list.
  - **When more than one publisher counts as a "primary" source.** Vendor advisory + vendor research blog, vendor advisory + regulator filing (8-K), CERT advisory (when it *is* the primary disclosing party for its jurisdiction) + vendor advisory it references — these are dual primaries. The first two `[Title](URL)` blocks are both leads.
  - **Avoid NVD / national-CERT as the *only* primary.** Editorial rule: vendor PSIRT advisories / research-lab posts / vendor blogs / regulator filings / victim statements are preferred as the lead. NVD/MITRE and national CERTs/NCSCs are second-tier primaries — `Additional source:` material — except in the narrow cases where they genuinely *are* the disclosing party (NCSC.ch on a Swiss federal incident, ENISA EUVD on an EU-discovered vuln, KEV before vendor's advisory page is up).
  - **Multi-CVE — one item, several CVEs.** It is *encouraged* to group related CVEs into one item rather than emit a paragraph per CVE (Ivanti EPMM chain, CERT-FR multi-CVE advisory, research-lab multi-bug audit). The footer carries a comma-separated `CVE:` field and per-CVE breakdown for any field whose value differs (`CVSS: 9.1 / 7.2`, `Auth: pre-auth (CVE-…), admin-required (CVE-…)`).

- **`state/run_log.json` schema made exhaustive** with `prompt_version`, `items_dropped_by_verification`, and explicit population rules for every field. The Ops dashboard renders sub-agent cells as `items (used/attempted src)`, surfaces a `stalled` badge on `returned: false`, and a yellow badge when `fetch_failures` is non-empty — empty fields produce empty dashboard cells. Every field is required every run, no exceptions. `tools/check_brief.py` validates the population.

- **Quality gates** add: Phase 4.5 ran covering both axes; `run_log.json` fully populated; `tools/fetch_source.py` used for CISA + NCSC.ch; `python3 tools/check_brief.py` exits 0.

- **Hard invariants — 12 → 15 entries.** All 12 from v2.27 preserved. New: (10) Phase 4.5 verification sub-agent loop covering URL truth + editorial quality, ≤3 iterations, may spawn ≤3 follow-up research sub-agents per iteration; (11) Phase 5.5 self-check via `tools/check_brief.py`; (14) `tools/fetch_source.py` is the bridge for CISA + NCSC.ch every run; (15) `state/run_log.json` populated every run with the full per-sub-agent allocation block + verification counters.

- **Working-directory layout** adds `tools/check_brief.py` and `site/test_build.py`; clarifies that `tools/fetch_source.py` is mandatory for CISA + NCSC.ch.

### Documentation

- **`docs/verification.md`** — adds a Phase 4.5 section describing the dual-axis verification (truth gate + editorial-quality gate), the 6-item editorial bar, the iterative refinement table, and the 3-iteration / 3-follow-up-sub-agent caps. Quality-gate checklist gains the script + Phase 4.5 entries + multi-CVE breakdown + anti-NVD/CERT-as-primary rule.

- **`docs/workflow.md`** — adds a § 6.5 Phase 4.5 section between Phase 4 and Phase 5; replaces the six-bullet Phase 5.5 description with the 17-check institutionalised script invocation; expands the `state/run_log.json` description to spell out every required field and how the Ops dashboard renders each.

- **`docs/architecture.md`** — adds `tools/check_brief.py` to the components list (with the full check inventory + import-from-`build.py` design); updates the data-flow diagram to show Phase 4.5 (truth + editorial) and the script-driven Phase 5.5 as discrete boxes.

### Hard invariants — 12 → 15

All 12 from v2.27 preserved. Three new entries (Phase 4.5 dual-axis loop, `tools/check_brief.py` gate, `tools/fetch_source.py` mandatory for CISA+NCSC.ch, `run_log.json` populate) make the new dependencies non-removable.

---

## 2.27 — 2026-05-08 (final-verification sub-agent loop + less-is-more rewrite)

### Why
v2.26 hardened the *intent* around link discipline ("don't fabricate URLs") and tightened the § 1 bar. v2.27 adds the *enforcement layer* — an independent verification sub-agent that reads the finished brief end to end before publication and flags fabricated URLs, citation mismatches, and unsupported claims for the main agent to fix. The same release rewrites PD-11 around an explicit "less is more" principle so the brief stops drifting toward "fill every section" and back toward "ship only what changes a defender's day."

Both changes are responses to operator review of the 2026-05-08 brief, which contained: invented blog slugs, citations that pointed to homepages, claims (notably aggregate exposure counts) that no linked source supported, and sections padded with items that did not meet the relevance bar.

### Daily prompt — `prompts/daily-cti-brief.md`

- **PD-11 rewritten as "Less is more — relevance over volume."** The single-line "no suppression, no padding" rule is replaced with: an explicit daily relevance bar (the four conditions an item must satisfy to qualify for the brief at all), a non-exhaustive blocklist of content the brief should drop without ceremony (vendor marketing dressed as research, recap of already-covered stories without delta, awareness-level pieces, industry surveys, conference recaps, product launches, opinion pieces, year-over-year stats without a defender takeaway), variable-size guidance (a quiet day produces a short brief, a noisy day produces a longer one — never pad to length), an empty-section policy (sections without qualifying content render the heading + an italic `*intentionally left empty*` stub), and item-level cuts (throat-clearing intros, hedge stacks, restating section context, closing flourishes, recap of prior coverage all get cut). The reader-trust framing — "the reader trusts that brevity reflects signal, not laziness" — is the operative line for the model.

- **New Phase 4.5 — Final verification sub-agent (loop until clean).** Inserted between Phase 4 (compose) and Phase 5 (state update). After the brief is written to disk, a fresh `general-purpose` sub-agent is spawned with a strict verification prompt: read the brief end to end, fetch every cited URL, confirm each (a) resolves, (b) is a specific page (not homepage / category / listing), (c) actually supports the claim being cited; cross-check named entities (CVEs, actors, campaigns, victims, dates, aggregate numbers) against the linked sources and flag any without source backing; surface claims missing inline citations. The verification agent is read-only — it never edits the brief. It returns a structured Markdown report with five blocking-finding categories (broken URLs, generic / oversight URLs, citation does not support claim, unsupported / hallucinated facts, claims missing inline citation) and one advisory category (less-is-more flags), each finding numbered so the main agent can fix or drop surgically. The main agent applies fixes in priority order — replace the URL with a freshly-fetched specific URL, narrow the claim to what the source supports, or drop the claim/item — then spawns a fresh verification sub-agent against the updated brief. Loop until verdict CLEAN, with a hard cap of three iterations. After three rounds remaining issues are dropped, surviving residuals are logged in § 8 (`verification: published with N residual findings unresolved after 3 iterations`), and the brief publishes — the CRITICAL "always write the file" header always wins over the verification gate; verification removes bad content but never blocks publication.

- **Run-log schema** gains `verification_iterations` (number of Phase 4.5 rounds) and `verification_residual_count` (issues unresolved after the iteration cap, 0 on a clean publish). Operations dashboard at `/ops/` will surface these.

- **Quality-gates checklist** gains two entries: "Phase 4.5 verification ran, final verifier returned CLEAN (or three iterations exhausted with residuals logged in § 8); `verification_iterations` and `verification_residual_count` set in `state/run_log.json`," and "Less is more applied — every item passes the daily relevance bar; sections without qualifying content carry the explicit `*intentionally left empty*` stub (except § 1, which is omitted entirely)."

### Notes for the operator

The verification sub-agent costs another ~5–10 minutes of wall-clock and a non-trivial fetch budget on top of Phase 1. That is the intended price for catching hallucinated URLs and unsupported aggregate numbers before they reach the published feed. The iteration cap of 3 is the upper bound on how many rounds the loop will run — most days the first verification should return CLEAN; iteration 2 catches anything the writer-verifier disagreed about; iteration 3 is the safety floor, after which residuals are logged and the brief publishes anyway.

If the verification sub-agent itself fails (timeout, no return), the main agent proceeds with publication and notes `verification: sub-agent did not return — published without final verification` in § 8 — the brief still ships.

---

## 2.26 — 2026-05-08 (Immediate Actions bar + source-link discipline)

### Why
Operator review of the 2026-05-08 brief surfaced three editorial defects:

1. **§ 1 Immediate Actions was over-inclusive.** A Windows Shell NTLM-coercion item entered § 1 because of an upcoming CISA KEV federal-remediation deadline, even though the underlying vulnerability had been patched in April Patch Tuesday and was not freshly weaponised. § 1 is meant to be the "stop reading and act now" section — emergency patches, immediate isolation, instant credential rotation — not a KEV-deadline reminder.

2. **Hallucinated and oversight URLs.** Several inline citations pointed to homepages, news category landing pages, or fabricated blog slugs (`https://heise.de/news/`, `https://nos.nl/artikel/`, `https://www.surf.nl/actualiteiten/2026/canvas-security-update`). The reader cannot verify a claim from a URL that 404s or lands on a generic feed.

3. The site-build TL;DR, Updates-section keyword, and footer-detection regexes had drift bugs against the prompt's `## § N — Heading` numbering and the trailing `---` horizontal rule between sections — those are fixed in `site/build.py` in this same change.

### Daily prompt — `prompts/daily-cti-brief.md`

- **PD-2 expanded** with an explicit "Critical link discipline" paragraph banning URL fabrication, URL inference from advisory IDs, and citation of homepages / news categories / listing indexes. Every URL in a brief must be a URL the agent actually fetched in this run that resolved to content matching the claim. Surface every relevant URL where the claim was found (primary + corroborating), not just one.

- **§ 1 Immediate Actions criteria rewritten** as a **conjunctive** test instead of a disjunctive one. An item now needs to be (a) newly disclosed or newly weaponised, AND (b) actively exploited or with imminent expected mass exploitation, AND (c) require time-critical-to-the-hour-or-day action. CISA KEV deadlines on already-covered items are explicitly disqualified from § 1 — they belong in § 5 (Updates) or the § 7 Action Items table. New "If unsure, it does not belong in § 1" tiebreaker.

- **New `Source-link discipline (highly critical)` sub-section** in Phase 1 spelling out, for sub-agents:
  - Only fetched URLs may be cited.
  - URLs must point to specific article / advisory / vendor PSIRT / regulator filing / victim statement pages, never homepages or category landings.
  - Drill to the most primary source, AND keep the corroborating sources too.
  - News-only fallback is acceptable when the primary was unreachable, provided the URL is a specific article URL (not the news site's homepage) and the item is flagged in § 8.
  - Verify each link actually resolves before returning it.
  - If unsure, drop the item rather than ship a guessed URL.

- **Sub-agent spawn template** now includes a prominent "LINKS ARE ABSOLUTELY CRITICAL — read this twice" paragraph that mirrors the same rules in plain language inside the template the four sub-agents see at spawn time.

- **Phase 2 step 1 expanded** from "re-fetch the primary source if any doubt" to a full URL spot-check: every cited URL is checked against the sub-agent's fetch transcript, 404s and homepage redirects fail the item, and items whose URLs cannot be replaced are dropped to § 8 with a `URL verification failed: ...` line.

### Site build — `site/build.py`

(Not strictly a prompt change but co-released with v2.26 because it surfaced the same review.)

- **TL;DR parsing regex** broadened from `## 0?. TL;DR` to `## ...TL;DR...`, so the home-page TL;DR preview, the RSS description, and the brief summary populate correctly when the prompt uses any heading-prefix style (`## TL;DR`, `## 0. TL;DR`, `## § 1 — TL;DR`).

- **Item-footer detection** in `parse_brief` now skips trailing blank lines AND trailing Markdown horizontal rules (`---`, `***`, `___`) when locating the metadata-footer line. The 2026-05-08 brief's last H3 in each section was failing footer parsing because the H2-section divider `---` ended up inside the slice, hiding the actual footer line — leaving the per-item Tags / Region pills unrendered and the line emitted as raw italic Markdown instead.

- **`_SECTION_KEYWORDS`** now also recognises `Updates on Previously Covered Items` and `Previously Covered Items` as the canonical "updates" section, in addition to the existing `Updates to Prior Coverage`.

- **H4 item fallback in `parse_brief`.** § 4 Trending Vulnerabilities in v2 emits each per-CVE detail block under a `#### CVE-...` heading (the section opens with an H3-equivalent table, so per-CVE blocks step down to H4). Sections with no H3 items now also walk H4 boundaries for item detection. Previously these blocks fell through into the section's raw body Markdown and their per-item footer lines rendered as plain italic text.

- **`parse_footer_line` accepts Source-less footers.** The previous regex hard-required a `Source:` prefix, which dropped both (a) the TL;DR aggregate footer (`— *Tags: ... · Region: ...*`) and (b) any other footer style without an explicit `Source:` label. The matcher is now permissive on the prefix while still requiring at least one recognised footer-field label (`Sources?`, `Tags`, `Region`, `Sector`, `CVE`, `CVSS`, `Vector`, `Auth`, `Status`, `Additional source`) to qualify, so arbitrary italic prose does not get misclassified as a footer.

- **Multiple bare-link sources at the head of a footer.** The deep-dive shape `— *Source: [a](u) · [b](u) · [c](u) · [d](u) · Tags: ...*` previously kept only the first link; the parser now treats every leading bare-link part as an additional source and de-dupes by URL. The reader sees every primary + corroborating link the writer attached to the unit.

- **Section-level footer detection.** The Deep Dive (§ 7) has no item heading — its block-level metadata footer sits at the section tail. `parse_brief` now extracts a section-level footer for sections that have no H3 / H4 items, exposes it as `section["section_footer"]`, and the brief-page renderer emits it as a structured pill block under the section body.

- **Per-item RSS feed includes section-level footers.** A section that carries a section-level footer (Deep Dive) now produces a single per-item-feed entry pointing at `briefs/<name>/#<section-anchor>`, so every block of content with its own metadata footer reaches the per-item feed reader.

- **RSS feed bodies render Sources only.** `render_footer_html` gains a `sources_only=True` flag; the per-item feed uses it so the structured footer block in `<content:encoded>` shows just the Sources line. Tags / Region / CVE / CVSS / Vector / Auth / Status remain as `<category>` feed metadata. The daily and weekly feed bodies, which use the brief's raw markdown rather than the parsed structure, run a new `_strip_footer_metadata_in_md` pre-pass that drops every non-Source field from each italic footer line before rendering. Tags-only footers (TL;DR aggregate) collapse to nothing.

---

## 2.25 — 2026-05-07 (audience + technical depth)

### Why
The brief was occasionally drifting toward executive-summary register —
*"a critical vulnerability has been disclosed"*, *"organizations are urged
to patch promptly"*, *"the threat landscape continues to evolve"* — when
the actual audience is Tier 2/3 incident responders, threat hunters, and
detection engineers who live in MITRE ATT&CK every day and read primary
vendor research directly. They don't need to be told what BloodHound is;
they need to be told which exact component, which exact technique, which
exact event ID surfaces it. v2.25 makes the audience expectation
unmissable and pins down what "deep technical level" means for every
section.

### Daily prompt — `prompts/daily-cti-brief.md`
- Opening role description rewritten to spell out the audience (Tier
  2/3 IR + threat hunters + detection engineers + reverse engineers +
  red-team-aware defenders + SOC management who came up through
  analyst rotations) and to give the assumed-fluency vocabulary as a
  concrete list (BloodHound, Mythic, gMSA, S4U2Self, OAuth device-code
  phishing, EDR userland hooking, BYOVD, LOLBAS, process hollowing,
  kernel callback registration, …).
- New "**The brief is a deep technical document.**" paragraph
  enumerates what every item must include: exact vulnerable component;
  technique class with MITRE ATT&CK IDs; exploitation prerequisites;
  affected and patched versions at vendor-stated precision; observed
  exploitation status with named campaign clusters; concrete defender
  takeaway tied to the specificity (event ID / log source / EDR
  telemetry / configuration switch).
- New "**Technical depth — what every item must include**" section in
  Phase 4, with a worked-good example fragment showing how the depth
  reads in practice on a § 2 item. Explicitly notes: *better to write
  less than to fabricate plausible-sounding specifics* (PD-1).
- Phase 3 deep-dive guidance expanded to spell out the seven content
  pillars: vulnerability or campaign mechanics; exploitation chain
  mapped to the MITRE ATT&CK kill chain; affected and patched
  versions; hunt and detection concepts (Sysmon EID 1, Windows event
  IDs 4624 / 4625 / 4663 / 4769 / 5379, Linux audit syscalls, Sigma
  technique categories); hardening and mitigation specifics; named
  campaign cluster; background paragraph for material with prior
  reporting older than ~6 months.
- Style rules now include "deep technical register" with a concrete
  example (`S4U2Self abuse to obtain a service ticket as a privileged
  user, followed by silver-ticket forging with the captured TGS` —
  *not* `attackers used Kerberos features to escalate privileges`)
  and a list of banned filler phrasings (*"in today's evolving threat
  landscape"*, *"organizations are urged to"*, *"this highlights the
  importance of"*).

### Weekly prompt — `prompts/weekly-summary.md`
- Same audience description as the daily, with the explicit note that
  SOC management read at the same level (they came up through analyst
  rotations).
- New "**The weekly summary is a deep technical document at SOC-analyst
  register**" paragraph clarifying that the weekly's step-back lens is
  about clustering threads / sectoral patterns / long-running-campaign
  arcs, NOT about translating the dailies into executive-summary
  register for a non-technical reader.
- New "**Technical depth — same standard as the daily**" section inside
  Phase 3 listing the seven specificity pillars and rejecting
  surface-level talking points even at week-level register.
- Style rules expanded to mirror the daily's "deep technical register"
  +  banned-filler-phrasing list.

### Hard invariants
Unchanged. The 12 hard invariants in the daily prompt's META section
still hold. The audience clarification is consistent with — and
sharpens — Prime Directive 1 (zero LLM knowledge): you can't fabricate
the technical specificity an audience this skilled will demand, so the
specificity must come from the primary source you fetched today.

---

## 2.24 — 2026-05-07 (prompt rewrite for clarity + Sonnet readability)

### Why
The v2.23 cut-over landed all the new features (9-section structure, per-item metadata footer, Trending Vulnerabilities inclusion gates, Action Items, Immediate Actions, primary-source bias) but the prompts had grown organically — daily was 1067 lines / ~25k tokens with significant duplication and verbose subsections. Goals for v2.24:
- One read-through is enough — Sonnet 4.6 should not need to refer back mid-execution.
- Every anti-crash guard is explicit and prominent.
- Total budget well under 25k tokens (now 14k for daily, 6.5k for weekly).
- All v2 features still fully specified (9 sections / footer / gates / taxonomy / patience clause / primary-source bias).

### Daily prompt — `prompts/daily-cti-brief.md`
- Total length 1067 → 671 lines (~14k tokens). Same scope; tighter prose.
- New "**CRITICAL: this run must produce a brief**" block at the top consolidating all 8 anti-crash guards (always write the file; ~10 min sub-agent timebox; compose-incrementally to dodge stream-idle-timeout; persist intermediate state to `work/<run-id>/`; drop raw HTML; bounded retries; two-stage publishing chain; quality over retries).
- 12 prime directives consolidated into a single ordered list (was 12 H3 subsections); each directive is now 3–6 lines instead of 10–25. Every directive that previously needed a sub-table or nested bullet keeps it.
- "Trace to the most primary source" promoted from buried sub-agent guidance to PD-12.
- Phase-by-phase descriptions reorganised under H2 headings with explicit time budgets (~1 min preflight, ~10 min Phase 1, ~5 min Phase 2, ~2 min Phase 3, ~10 min Phase 4).
- Sub-agent spawn template consolidated into a single block-quoted message that opens every spawn — covers defensive intent + patience + primary-source bias + always-return-something. Used to be three separate paragraphs scattered through Phase 1.
- Research methodology compressed (drill / pivot / search / propose) — 80 lines → 30 lines without losing the bridge-fetcher recipes (NCSC.ch CSH, CISA KEV, generic allow-listed hosts).
- Phase 4 "Output structure" now lists the 9 sections as a normative table on first read; the per-section guidance follows. The reference template at the end still shows the full Markdown skeleton with every metadata footer.
- Phase 5 source lifecycle compressed (60 lines → 25 lines) without dropping any rule.
- Phase 5.5 self-check expanded with the v2.23 retargeting at sections 2–4 plus the metadata-footer presence check (step 5) and the taxonomy-validation check (step 6).
- META "Hard invariants" list now includes (10) Phase 5.5 self-check gate, (11) per-item metadata footer, (12) strict CSP + vendored-library hash check.

### Weekly prompt — `prompts/weekly-summary.md`
- Total length 363 → 448 lines (~6.5k tokens). Slightly longer because we added the same anti-crash guards block, the consolidated spawn template, and an explicit Phase 4.5 self-check gate.
- New "**CRITICAL: this run must produce a summary**" block mirroring the daily.
- Sub-agent spawn template consolidated into a single block-quoted message (was three).
- Per-item metadata footer NORMATIVE block referencing `site/taxonomy.yaml` for the controlled vocabulary (instead of duplicating the full vocab list — the daily prompt is the source of truth).
- New Phase 4.5 self-check gate: state JSON parses; every CVE in cves_seen.json; every H3 in §§ 1–8 carries a v2 metadata footer; every footer value is in the taxonomy.
- Reference template at the end now shows every section with a representative metadata footer.

### Hard invariants — unchanged
The 12 hard invariants in the daily prompt's META section are unchanged. The two prompts share the same publishing chain, the same metadata-footer schema, the same taxonomy file, and the same anti-crash guard list.

---

## 2.23 — 2026-05-07 (v2 schema cut-over)

### Why
Substantial editorial + engineering upgrade landed together: the SPA reader is replaced by a real static-site SSG, every brief item gets a structured metadata footer parsed by the build, and the section structure is reorganised so per-item tagging (region + sector + theme) replaces the dedicated "Switzerland, Europe & Public Sector" section. Full plan: [`docs/v2-plan.md`](../docs/v2-plan.md).

### Daily prompt — section structure
The eight-section structure (`0. TL;DR / 1. Active Threats & Trending Vulns / 2. Switzerland, Europe & Public Sector / 3. Notable Incidents & Disclosures / 4. Research & Investigative Reporting / 5. Deep Dive / 6. Updates / 7. Verification Notes`) becomes a nine-section structure:

```
0. TL;DR
1. Immediate Actions                                         (often absent — see below)
2. Active Threats, Trending Actors, Notable Incidents & Disclosures
3. Trending Vulnerabilities                                  (consolidated, with inclusion gates)
4. Research & Investigative Reporting
5. Updates to Prior Coverage
6. Deep Dive — {topic}
7. Action Items                                              (derived from today's content only)
8. Verification Notes
```

Switzerland / Europe / public-sector emphasis is now expressed as **per-item region + sector tags** on every § 2 item, ordered with CH/EU/public-sector first then global then the rest. There is no separate § 2 in the v2 layout — the editorial focus rides on the metadata footer.

### Daily prompt — Immediate Actions
New § 1, **omitted entirely on most days**. An item only enters when it satisfies at least one of: actively-exploited zero-day with RCE/auth-bypass; zero-click RCE (exploited or with public PoC); pre-auth RCE on internet-exposed enterprise software; supply-chain compromise affecting widely deployed software; active campaign with confirmed European public-sector impact. Empty Immediate Actions is part of the design — rendering the heading every day with a placeholder dilutes the meaning when something does meet the bar.

### Daily prompt — Trending Vulnerabilities inclusion gate
§ 3 now narrows the CVE bar with explicit inclusion gates. CVEs that the news cycle is hyping but that don't clear at least one gate (CISA KEV, ENISA EUVD `exploited=true`, ENISA EUVD CVSS ≥9.0, ITW report from a HIGH-reliability researcher, pre-auth internet-exposed RCE with public PoC) **stay out of the brief** — logged in § 8 with the reason. The legacy `CVE | Product | …` table is folded in as a secondary aggregation beneath the per-CVE entries.

### Daily prompt — Action Items
New § 7. Specific, derived-from-this-brief recommendations only. Generic advice does not belong here. Skews toward patching / mitigations for actively-exploited CVEs covered today, hunting queries / IoC-free detection concepts for campaigns covered today, configuration changes that close the specific attack path covered today.

### Daily prompt — per-item metadata footer (NORMATIVE)
Every individual content block (every § 1 / § 2 / § 3 / § 4 / § 5 / § 6 / § 7 item) ends with **exactly one italic Markdown line** in the format

```
— *Source: [Title](URL) [· Additional source: [Title](URL)] · Tags: tag1, tag2 · Region: region1[, region2] [· CVE: CVE-…] [· CVSS: …] [· Vector: …] [· Auth: …] [· Status: …]*
```

Field separator is the middle dot ` · ` (U+00B7 with surrounding spaces). Controlled vocabularies live in [`site/taxonomy.yaml`](../site/taxonomy.yaml). The build refuses any item using a value not in the taxonomy. The build splits each brief by H3 + footer and emits one stable `/items/<slug>/` page per content block plus per-tag, per-region, per-CVE indexes. Missing or malformed footer on a post-cut-over item is a build failure.

### Daily prompt — Phase 5.5 self-check
- Steps 1, 2 unchanged.
- Step 3 retargets at sections 2–4 (was 1–4).
- Step 4 retargets at § 5 (was § 6) and additionally requires a metadata footer inside each UPDATE blockquote.
- Steps 5 and 6 added: every H3 in §§ 1, 2, 3, 4, 5, 7 carries a footer; every footer's values are in `site/taxonomy.yaml`.

### Sub-agent spawn — patience and primary-source bias
Both sub-agent spawn-prompt blocks gain explicit "take your time, persist intermediate state, never block the brief" and "trace to the most primary source you can verify; news is at most a *via* reference" stanzas, replacing earlier soft guidance.

### Engineering — `site/build.py`, RSS, taxonomy
- New SSG emits real HTML pages for every URL: home, brief, item, CVE, source, topic, tag, region, ops, about. The legacy SPA hash routes get a one-time JS bootstrap on `/` that converts indexed `#/briefs/<name>` URLs to the clean URL.
- Three valid RSS feeds: `/feed.xml` (daily, URL preserved), `/feed-weekly.xml` (NEW), `/feed-items.xml` (NEW per-item, last 50). Closes [#2](https://github.com/OwlsNightCatch/ctipilot/issues/2):
  - **Defect A fixed:** Markdown emphasis / links / inline code render to HTML before the body is CDATA-wrapped. A unit test asserts no unrendered `**...**` or `[..](http..)` survives into `<content:encoded>` payloads.
  - **Defect B fixed:** `<pubDate>` is the actual git-commit moment of the brief on `main` (sourced from `git log --diff-filter=A --format=%aI -- briefs/YYYY-MM-DD.md`), falling back to file mtime — never midnight-of-brief-date.
- Vendored library integrity check is preserved and now also covers the new `filter.min.js`.
- Strict CSP unchanged.
- Self-check at the end of every build asserts: every emitted HTML page contains the Umami snippet exactly once; every feed parses as XML; no UTM parameters anywhere; no unrendered Markdown emphasis in any feed body.

### Weekly prompt
Adopts the same metadata footer on every item. Section structure unchanged.

---

## 2.22 — 2026-05-07

### Why
Operator changed the routine schedule (daily Mon–Fri 06:00 GMT+2, weekly Mondays 11:00) and asked that *no time, day, or schedule assumption* be hardcoded in the prompt. The agent should always derive its recency window from `briefs/` so:

- (a) the operator can change cron times freely without touching the prompt,
- (b) a failed run is automatically caught up by the next run (Tuesday fails → Wednesday's brief covers Mon-noon → Wed-morning),
- (c) the daily covers the gap since the last *daily* and the weekly covers the gap since the last *weekly*, independently and self-coordinating.

v2.21's day-of-week recency table conflicted with goal (a) — it baked Mon–Fri / Sat–Sun assumptions into the prompt. Removed.

### Prime Directive 7 (Recency) — gap-derived, schedule-agnostic, self-healing
- Day-of-week table replaced with a **gap-derivation rule from disk**:
  ```
  latest_brief = max(date in briefs/*.md by lex sort)
  gap_hours    = (currentDate - latest_brief) * 24
  window_hours = max(24, gap_hours + 12)   # 12h safety overlap
  ```
- New window-class table maps `gap_hours` to expected brief size and § 7 disclosure:
  - ≤ 30 h → standard daily (3–5 § 1a items)
  - 30 – 60 h → extended (one missed run; 5–8 items)
  - 60 – 96 h → catch-up (typical Monday after Mon–Fri schedule, OR two missed runs; 6–10 items)
  - > 96 h → major gap (cap at 10–12 items, surface unhandled volume in § 7)
- Self-healing by construction: any missed run is automatically caught up by the next run because the gap on disk widens.
- Schedule independence by construction: the prompt doesn't know — and doesn't need to know — when the cron fires.

### Phase 0 step 7 (new)
- After loading state, the agent now explicitly computes `gap_hours` and `window_hours` from the latest file in `briefs/`, sets the window-class, and passes `window_hours` to every Phase 1 sub-agent's spawn message.

### "Determining today" subsection
- Day-of-week table replaced with the gap-derivation pseudocode and the rule "do not hardcode times, days, or schedule assumptions".

### Weekly summary (`prompts/weekly-summary.md`)
- Same gap-derivation rule applied: `latest_weekly = max(briefs/weekly/*.md)`, `gap_days = today - latest_weekly_end`, `window_days = max(7, gap_days + 1)`.
- Weekly window-class table:
  - ≤ 8 d → standard week
  - 9 – 15 d → one missed week (doubled coverage)
  - > 15 d → major gap (cap at ~3 weeks of detail)
- Header `fires once per week` softened to `schedule is set by the operator`.

### META autonomy paragraph
- "fires once per **working day** (Monday–Friday) … weekly summary fires Sunday night" → "scheduled routines fire on whatever cadence the operator configured … schedule is **not** encoded in this prompt".

### Docs
- README, `docs/workflow.md`, `docs/routine-setup.md` all stripped of hardcoded times (no `06:30 Europe/Zurich`, no `18:00–22:00`, no `Sunday night`); the gap-derivation rule is explained as a self-healing + schedule-agnostic mechanic.

---

## 2.21 — 2026-05-07

### Why
The daily routine runs **only on working days** (Mon–Fri); the weekly summary runs **Sunday night**. Saturday + Sunday + Friday-during-the-day events therefore fall through the cracks unless the Monday brief explicitly catches them up. Earlier prompt versions said "Default window: events from the last 24 hours" with no day-of-week awareness — Mondays were producing a same-size brief that silently dropped two and a half days of operational signal.

### Prime Directive 7 (Recency) — schedule-aware window
- New explicit table mapping day-of-week to recency window:
  - **Mon** → 72–84 h (Fri-morning → Mon-morning); Monday brief is expected to be larger (typically 6–10 § 1a items vs the usual 3–5).
  - **Tue–Fri** → 24 h, extend 72 h for actively developing items.
  - **Sat / Sun** → routine should not run; off-schedule run is treated as Monday-class with the gap surfaced in § 7.
- Monday brief explicitly catches Friday-during-the-day publications (vendor advisories that landed after the Friday brief, victim disclosures filed into EU close-of-business, US-afternoon CISA KEV additions) plus the entire weekend.
- "Don't bridge to the weekly summary" rule: the Sunday-night weekly is week-level synthesis; the Monday daily is *catch-up of the operational items the daily missed*. The two are complementary, not redundant.
- First brief after any unscheduled gap (public holiday, missed run) extends the window the same way and surfaces the gap in § 7 (`Coverage window: extended to N hours due to scheduling gap; previous brief YYYY-MM-DD`).

### "Determining today" — day-of-week derivation
- Phase 0 now derives the day-of-week from `currentDate` and applies the recency-window table.
- Sub-agent spawn messages receive the computed window length so their `WebSearch` / `WebFetch` budgets target the right time range.

### META autonomy paragraph
- "fires once per weekday" replaced with "fires once per **working day** (Monday–Friday)"; weekly cadence stated explicitly as Sunday night.

### Docs
- `docs/workflow.md` schedule table updated.
- `README.md` daily-routine + weekly-routine paragraphs updated.
- `docs/routine-setup.md` recommended-cadence step updated to "Mon–Fri, 06:30 Europe/Zurich".

---

## 2.20 — 2026-05-07

### Why
Operator review of the deployed site flagged three things to harden:
(1) the agent had been citing the BSI generic landing page instead of the
specific WID-SEC advisory; (2) several deep-dive items leaned on news
articles when the underlying vendor / CERT report was reachable in one
extra fetch; (3) the agent's fetch budget was too tight for the
primary-source pivot work.

### Phase 1 — research methodology (changed)
- **Primary-source pivot mechanic made explicit and persistent.** The "follow news to the primary report" rule now spells out the pivot procedure step by step:
  1. Scan the article for outbound links (prose, pull-quotes, "via" footers).
  2. If no obvious link, search directly: `WebSearch "<vendor name> <topic> blog"` or jump to the vendor's `/research` / `/blog` index.
  3. **Incident chain**: victim disclosure → regulator filing → IR-firm post-mortem → news. Walk it from the victim end.
  4. **Vulnerability chain**: vendor PSIRT → NVD → national CERT (CERT-EU / CERT-FR / BSI WID / NCSC-CH CSH) → exploit-research lab → news.
  5. Don't stop at the first link that looks plausible — confirm it's the primary, not another aggregator. Two pivots is normal; three is fine when the trail is real.
  6. If the primary cannot be reached, record `Coverage gaps: <topic> — primary source <URL> unreachable, citing news as fallback` in § 7.

### Phase 1 — operational guardrails (changed)
- **Fetch budget raised 30 → 45 calls** to leave headroom for the pivot work (each pivot costs 2–3 fetches per item).
- **Wall-clock soft cap raised 10 → 12 min** for the same reason.
- **New "primary-source pivot reserve"** of ~10–15 of the 45 calls — fetches whose only purpose is to follow a news article down to the underlying primary report.
- Per-source timeout exception: when chasing a primary, one alternate path (publisher blog index, `tools/fetch_source.py`) is allowed and counts as part of the pivot, not a retry.

### Sources (`sources/sources.json`)
- **BSI Germany** URL replaced. The previous URL (`https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Cyber-Sicherheitslage/Technische-Sicherheitshinweise-und-Warnungen/Cyber-Sicherheitswarnungen/cyber-sicherheitswarnungen_node.html`) was a generic landing page that did not contain advisory content. New URL is `https://wid.cert-bund.de/portal/wid/kurzinformationen` (the CERT-Bund WID advisory index). RSS available at `https://wid.cert-bund.de/content/public/securityAdvisory/rss`. Per-advisory drill-down URL pattern is `https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-YYYY-NNNN`. Drill-down is mandatory: never cite the kurzinformationen index, always the per-advisory detail URL.

### Existing briefs (retroactive)
- `briefs/2026-05-06.md`: both BSI Copy Fail citations (TL;DR § 1a item header and § 5 deep-dive narrative) updated from the broken landing-page URL to `https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1232` (the WID-SEC ID for CVE-2026-31431 'Copy Fail').

---

## 2.19 — 2026-05-07

### Why
Operator pass over [`docs/improvements.md`](../docs/improvements.md): bring the highest-leverage editorial and operational improvements into the prompt, retire the soft-kill-switch (`state/BLOCKED.md`) in favour of a stronger in-prompt self-check (Phase 5.5), and tighten the source-lifecycle rules so transport errors no longer demote sources that are merely being blocked by their publisher.

### Phase 0
- **Step 0 (BLOCKED.md circuit-breaker) removed.** The `state/BLOCKED.md` file was a pre-2.16-era idea that depended on an external editorial-invariant workflow we never built. Its responsibility is now absorbed by Phase 5.5 (in-prompt self-check, fail-closed on drift).
- **Step 2 strengthened.** The agent now reads the most recent weekly summary at `briefs/weekly/YYYY-Www.md` for the current ISO week and the prior ISO week explicitly, by name, regardless of file mtime. Closes the dedup gap when a Sunday weekly consolidates items the next Monday daily was about to re-report (improvements.md A6).
- **New step 5: read `state/deep_dive_history.json`.** Used by Phase 3's category-rotation rule.

### Phase 3 — deep-dive selection
- **Category-rotation rule added (improvements.md A8).** If the prior 7 days of `deep_dive_history.json` already cover a candidate's category (linux-lpe, windows-lpe, network-stack-rce, identity-infra, web-app-rce, endpoint-rce, firewall-vpn-rce, supply-chain, ot-ics, ransomware-affiliate, apt-campaign, cloud-saas, cryptography, mobile, annual-report, other), demote the candidate one rank — unless criterion 1 (active exploitation + non-trivial CH/EU public-sector exposure) makes it irreducibly urgent. Avoids covering "Linux LPE for the fifth day running" while OT and identity-infra go uncovered.

### Phase 4 — compose
- **Prompt-version field added to the metadata line.** `**Generated by:** ... · **Prompt:** v{N.M}`. The site renders this as a clickable badge linking to the matching CHANGELOG entry, so a reader can tell at a glance which editorial-policy version produced the brief (improvements.md D3).
- **Metadata line slimmed.** Removed `**Audience:** SOC Tier 2/3, IR, Threat Hunting` — the audience is documented elsewhere (README, About page) and added no per-brief value.
- **AI-generated content notice strengthened.** Now opens with **"AI-generated content — no human review."** and explicitly states **"Nothing here is reviewed or edited by a human before publication."** Closes a perception gap where readers could assume editorial oversight that does not exist.

### Prime Directive 2 — inline links, always (clarified)
- **Explicit "every section, no exception" wording added.** A real brief produced § 6 UPDATEs without inline citations (`UPDATE: ANTS officially confirmed the count as 11.7 million.` — no link). The directive now states verbatim that updates and "no material change" notes both require an inline source link, and § 4's per-section guidance restates it under § 6 specifically.
- **Phase 5.5 self-check #4 added.** Before commit: split § 6 on `> **UPDATE` boundaries; assert each non-empty UPDATE paragraph contains at least one `[…](http…)` link. Drift aborts the commit; the agent re-Edits § 6 to add the missing source.

### Phase 1 — research methodology
- **Bridge-fetcher allow-list expanded after 2026-05-07 retest.** Five additional publishers — `csirt-acn-it` (CSIRT Italy / ACN), `talos` (Cisco Talos blog), `prodaft` (PRODAFT reports), `inside-it-ch` (Inside IT Switzerland), and `ico-uk` (UK ICO news) — were verified to return HTTP 200 under the bridge fetcher's standard browser User-Agent. They were 403'ing the routine container previously; now reachable through `python3 tools/fetch_source.py url <URL>`. Hostname allow-list and prompt recipe both updated.
- **`ccn-cert-es` confirmed unreachable** even with full browser headers (`Sec-Ch-Ua` brand strings included). Likely Cloudflare / geo-IP gating from outside Spain. Source `notes` records the test outcome and the rule: never demote on this transport block; surface as `Coverage gaps: ccn-cert-es: 403 even with bridge fetcher` in § 7. Retest periodically.

### Phase 1 — research methodology
- **NCSC-CH Security Hub guidance corrected — twice in one day.** First investigation (morning) found that anonymous calls to `/api/posts/search` returned 302-to-login and concluded the platform was authenticated-only. Second investigation (afternoon) found that the routine container's default User-Agent was being filtered by the publisher; with a normal browser UA, the public TLP:CLEAR slice is fully reachable via `GET /api/posts/dashboard?pageSize=N&pageIndex=0` (listing) and `GET /api/posts/{id}/details` (per-post Markdown body). Source `ncsc-ch-security-hub` is back to `status: active`.
- **New helper: `tools/fetch_source.py`.** Stdlib-only, host-allow-list-restricted, read-only Python script that re-issues HTTP requests with a stable desktop-Chrome User-Agent. Solves the recurring 403 / 302-to-login on CISA pages and the NCSC CSH dashboard. Provides four sub-commands: `url`, `ncsc-csh {list,post,recent}`, `cisa-kev`, `cisa page`. Posts marked TLP:AMBER or TLP:RED are refused client-side. The agent uses this via the `Bash` tool whenever a `WebFetch` on the documented hosts comes back blocked. The script never authenticates, never executes JavaScript, and never fetches a host that isn't in its allow-list.
- **Phase 5 source-lifecycle clarification (already in v2.19, restated for emphasis).** A 403 / 302-to-login is a transport signal, not a content signal — it never demotes a source on its own. The agent records the alternate-fetch strategy (typically: "use `tools/fetch_source.py`") in the source's `notes` and keeps the source in rotation.

### Phase 5 — state update
- **Source-lifecycle rules rewritten on the transport-vs-content axis (improvements.md A1, A9).**
  - Two distinct counters per source: `consecutive_quiet_periods` (200 with no in-window items — content signal) and `consecutive_fetch_failures` (transport error — 403 / 429 / 503 / 5xx / 404 / dead host).
  - **Sustained 403 / 429 / 503 / 5xx never demotes.** That pattern means the publisher is blocking the agent's request shape, not that the source is dead. The agent records an alternate-URL strategy in `notes` instead and keeps the source in rotation.
  - Demotion fires only on the content axis: 3 consecutive quiet periods with a failed canonical-URL probe, OR 5 consecutive 404 fails.
- **Hard cap added (improvements.md SR10): one new candidate source per run, maximum.** A flood of new candidates in one brief is anomalous; overflow is queued in § 7 for the next run.
- **New file `state/deep_dive_history.json`** — rolling 30-day list of `{date, topic, category}`; FIFO trim. Phase 3 reads it on the next run.
- **New file `state/run_log.json`** — rolling 90-day per-run record (model, sub-agent allocation `sources_attempted`/`sources_used`/`items_returned`, fetch failures, items published, deep-dive slug, duration). Surfaced by the SPA's `#/ops` view (improvements.md A5 / S8).

### Phase 5.5 — self-check gate (new, between Phase 5 and Phase 6)
Drop-in replacement for the BLOCKED kill-switch (improvements.md A2). Three checks before commit:

1. Every state JSON file the run wrote parses cleanly.
2. Every `CVE-YYYY-NNNNN` extracted from the brief markdown appears in `state/cves_seen.json`.
3. Every H3 heading in §§ 1–4 of the brief has a matching `appearances[].date == today` record in `state/covered_items.json`. The H3 / appearance-count delta is permitted to be ±1 (the deep-dive H3 may also appear).

If any check fails, **abort Phase 6** (do not commit). The brief file remains on disk; the next run rebuilds the state delta from the brief itself (the brief is the canonical artefact, not the state). The state files are reconstructable from the briefs; the briefs are not reconstructable from the state files.

### Phase 6 — commit
- The `git add` line now includes `state/deep_dive_history.json` and `state/run_log.json`.

### Effect on output
- Briefs carry a clickable prompt-version badge.
- Deep-dive coverage drifts away from any single category that has been over-represented for a week.
- Sources blocked by 403/429/5xx stay in rotation indefinitely with notes about alternate URLs, instead of silently dropping out of the active list within three runs.
- Anomalous mass-source-discovery commits become impossible by construction.
- Commits with state/output drift never land on `main` — they abort and re-run.

### What this rolls back / supersedes
- Rolls back v2.16 (the BLOCKED.md circuit-breaker). Phase 5.5 is the structural replacement.

---

## 2.17 — 2026-05-06

### Why
Added `ncsc-ch-security-hub` (https://security-hub.ncsc.admin.ch/#/dashboard) to `sources/sources.json` — the unified Swiss NCSC security advisory dashboard. It's an SPA with hash routing, so a naive `WebFetch` on the dashboard URL returns only the JavaScript shell. The Phase 1 "drill into articles" rule already covered the general case; this version makes it explicit for SPA dashboards and forbids ever citing a dashboard / index / listing URL as the source for a claim. The fix is to find the SPA's underlying JSON API, list advisories, then open each per-advisory detail page and cite *that*.

### Changed
- **Phase 1 research methodology, item 1 expanded.** Strengthens the existing "follow links from index pages" rule: index pages, dashboards, listings, and feed views MUST never be the cited source. The inline citation always points to the per-article / per-advisory detail URL.
- **New SPA-specific guidance.** Concrete recipe for the NCSC-CH Security Hub and similar dashboards: identify the underlying `/api/` endpoint, list advisories, fetch each detail page, cite the detail URL. If the SPA defeats every approach, record the failure mode in `Coverage gaps:` rather than falling back to a dashboard citation.

### `sources/sources.json` change
- Added `ncsc-ch-security-hub` (HIGH reliability, ch-eu / active-breaking / gov / vulns categories, multilingual de/fr/it/en). Includes a long `notes` field documenting that the URL is an SPA entry point and the per-advisory drill-down requirement.

---

## 2.18 — 2026-05-06

### Why
Reverted the v2.15 engagement signal entirely. The GitHub Repo Traffic API exposes github.com repo traffic only — there is no public API for GitHub Pages site traffic — so `state/engagement.json` could never measure what the agent was meant to weight (Pages-site reader engagement). Pivoting to repo-blob view counts was honest but misleading: a niche signal dressed up as a primary one. Cleanest fix is to remove the dependency.

### Changed
- **Phase 0 step 5 removed** (engagement.json read).
- **Reader-engagement context block removed** from Phase 0. The agent no longer accepts the soft-tiebreaker signal in deep-dive selection. All editorial weighting returns to verification + CH/EU nexus + novelty as before.
- The `state/engagement.json` file is gone; `.github/workflows/sync-engagement.yml` is gone; the SPA's repo-traffic panels are gone.

### What stays
- **On-device personal reading history** in the site's localStorage. Per-brief visit count and dwell time, never leaves the device. This is the only "page count" the system keeps, and only for briefs the visitor opened on their own device.
- **The agent's verification gates and source-rotation logic are unchanged.**

### Why this is safe
The signal that just got removed was already only a *tiebreaker*. Verification, two-source rule, CVE existence check, no-IOCs rule, no-vanity-metrics rule, and source-rotation memory all stay in place. Editorial integrity is unaffected; we removed an input that was measuring the wrong thing.

---

## 2.16 — 2026-05-06

### Why
The system is now intentionally self-evolving — the agent edits the prompt, the source list, and the state files autonomously, and there is no human review gate on any of these. The threat-model document (`docs/security-review.md`) identifies prompt self-mutation drift (T2) as the residual risk that most warrants a structural defence. The right shape for that defence under the autonomy constraint is a soft kill-switch: a flag the agent itself checks at the very top of Phase 0, settable out-of-band when a quality-gate workflow detects an editorial-invariant violation, and clearable only by a deliberate (human) commit.

### Changed
- **Phase 0 step 0 added** (numbered 0 because it is a prerequisite, not a phase action). The agent now checks for `state/BLOCKED.md` before doing anything else. If present, the run aborts with no writes. The flag is the documented signal that something has gone wrong and a human (or a follow-up workflow) needs to look at it.
- A short note added to Phase 0 explaining that step 0 is the soft circuit breaker referenced in `docs/security-review.md` § 3.4.

### Why this is safe
The kill-switch is fail-closed by design: if the file system read fails, the agent stops. It is set automatically by a future `editorial-invariant.yml` workflow when output regressions are detected (IOC pattern in a brief, hallucinated CVE, multi-day flood of [SINGLE-SOURCE] items) and by hand when a human notices something suspicious. The flag's *presence* is the binding action — what the file *contains* is operator commentary that the agent never reads. So the flag cannot be subverted by injecting content into it.

---

## 2.15 — 2026-05-06

### Why
The repository now ships a public reader (`site/`) and an aggregate-only engagement-tracking pipeline (`.github/workflows/sync-engagement.yml` → `state/engagement.json`). Aggregate page-view counts from the GitHub Repo Traffic API are pulled into the repo so the agent can use *which prior coverage readers are returning to* as a soft signal when picking deep-dive topics and Updates-to-Prior-Coverage entries. The signal is fully aggregate (no PII, no sessions, no cookies) and is computed by GitHub from anonymised request logs.

### Changed
- **Phase 0 step 5 added** (with subsequent step renumber): read `state/engagement.json` if present. The file may be missing on first run or if the sync action has not yet succeeded — the agent must degrade gracefully in both cases.
- **New "reader-engagement context" subsection** in Phase 0 below the deduplication-context block. Specifies how the engagement signal is allowed to influence editorial selection:
    - Used only as a *tiebreaker* for Phase 3 deep-dive selection and Phase 4 § 6 Updates ordering.
    - Never overrides the verification rules, the two-source policy, the no-IOCs rule, or the no-vanity-metrics rule.
    - Reader engagement *guides attention*; the verification chain still gates everything.
- **No change** to Phases 1–7. Sub-agents do not see the engagement signal directly; the main agent applies it during Phase 3/4 selection only.

### Why this is safe
The engagement file is generated by a separate workflow that the routine cannot influence (the routine's git push doesn't touch the workflow's data source — GitHub computes the counts). Even if the file were poisoned, the agent's verification gates remain unchanged: a poisoned engagement signal could nudge topic selection but cannot change which sources are accepted, whether the two-source rule applies, or what makes it past Phase 2. See `docs/security-review.md` for the full threat-model analysis.

---

## 2.14 — 2026-05-06

### Why
The routine's runtime model has been switched (per-routine Claude Code configuration). The earlier prompt versions hardcoded "Claude Opus 4.7 / claude-opus-4-7" into the brief template's AI-generated content notice and `Generated by:` metadata line, which means a brief produced by a different model would carry an inaccurate identity unless the model overrode the template. Worse, by *naming* the model, the prompt biased the model into believing it was the named one. Fix: never name the model in the prompt; require the model to identify itself accurately at composition time.

The prompt also lacked explicit execution-environment context for the Claude Code Routines on the web infrastructure. The agent had to infer that it was running in an ephemeral cloud container with a feature-branch git proxy and time/token budgets — better to state it directly so it doesn't waste tokens orienting itself.

### Changed
- **Removed all model names from the prompt and supporting docs** (`prompts/daily-cti-brief.md`, `prompts/weekly-summary.md`, `README.md`, `briefs/README.md`, `docs/workflow.md`). The prompt now never says which Claude variant it is for. The hardcoded "Opus 4.7" / "Sonnet 4.6" / `claude-opus-4-7` / `claude-sonnet-4-6` strings are gone from the brief template, runtime headers, and prose.
- **Added an explicit "Self-identification" subsection** in Phase 4 (daily) and Phase 3 (weekly):
    - Identify yourself accurately when filling in the AI-content notice and `Generated by:` line.
    - Use the actual model name and ID you are at execution time.
    - Do not invent a name; if uncertain, write *"Anthropic Claude (specific model not determined)"* and continue.
    - Putting the wrong model name is an integrity failure.
- **Brief template now uses `{model name}` / `{model-id}` placeholders.** The model fills them in from its own identity at runtime. The reference template caption explicitly notes which placeholders are filled by self-identification vs. which are content placeholders.
- **Expanded "EXECUTION ENVIRONMENT — Where you are running"** with concrete context:
    - Ephemeral cloud container; the repo is the only durable memory.
    - Default branch is `main` but the runtime checks out a feature branch; the publishing chain handles `HEAD:main` push and feature-branch fallback.
    - Network access via internal HTTP proxy with allow-list.
    - Git operations via separate proxy; 403 means missing GitHub App permissions, not transient.
    - Wall-clock and token budgets enforced; sub-agent guardrails align.
    - **Model assignment is configurable at the routine level**; identify yourself accordingly.
- **Removed version-pinning header** ("Version: 2.0 (date)") from both prompt files. Source of truth for versions is `prompts/CHANGELOG.md` only — keeps each commit from also having to bump the header.

### Sonnet 4.6 considerations
The prompt is now well-suited to Sonnet's stronger literal-instruction following. Several earlier rule clarifications (incremental writes, partial-result composition, item granularity, news-to-primary pivot, no workflow-internal language) help Sonnet produce a brief that matches the intent without the inferred latitude Opus tended to take. Existing concrete worked examples (the W18 TeamPCP / Mini Shai-Hulud / Vect cluster as the example for item granularity) stay because Sonnet benefits from concrete reference patterns more than from abstract guidance.

---

## 2.13 — 2026-05-06

### Why
Earlier prompt versions said the agent "must not auto-promote candidates" and that "humans review demotions and candidate additions periodically". That was a leftover from a model where a human reviewed routine output before merge. The actual operating model is fully autonomous — the routine fires, commits, pushes, no human gate. Encoded "human review" steps are dead weight; worse, they cause new candidate sources to never get promoted, and the source list silently stagnates.

### Changed
- **`sources/sources.json` lifecycle is now fully autonomous.** Every state transition runs in the routine, with the git diff as the audit trail. Encoded transitions:
    - **Discovery → candidate** (already autonomous; unchanged).
    - **Candidate → active**: auto-promote after 3 distinct runs where the candidate was successfully fetched *and* contributed content to a brief. No human gate.
    - **Active → demoted**: after 3 consecutive failed fetches with no working canonical-URL probe (already autonomous; unchanged).
    - **Demoted → active (recovery)**: NEW. A demoted source returns to `active` when a working canonical URL is found during research *and* that URL contributes content to a brief. Update url, reset counters, dated note. No human gate.
    - **URL updates in place**: already autonomous; unchanged.
    - **Reliability tier-down without demotion** for navigation-only sources: already encoded in v2.12; unchanged.
- **Hard rules clarified**: do not delete sources (demotion is soft removal; cleanup is a separate manual commit), do not promote demoted → active without a recovery event, do not edit historical `notes` (append-only).
- **README "Maintaining the source list and the CVE index"** rewritten to describe the autonomous lifecycle. The phrase "for human review" is gone everywhere; the new framing is "git log is the curation history".

### Effect on the source list over time
- Candidates that consistently deliver content get auto-promoted. The active source list grows organically as the routine encounters new high-quality publishers.
- Demoted sources can self-heal when publishers fix their URLs.
- The active list stays operationally honest without external curation cycles.

---

## 2.12 — 2026-05-06

### Why
The 2026-05-06 brief's § 7 listed real coverage gaps:

> *"Coverage gaps: CCN-CERT Spain (not fetched, sub-agent budget limit); GovCERT.ch advisory archive (navigation page only); CERT.at and GovCERT Austria (navigation pages only, no dated advisory content returned); NCC Group Research, WithSecure Labs, Dragos, SANS ICS, Cloudflare Cloudforce One, Akamai SIRT, Elastic Security Labs, Group-IB, Secureworks CTU, Red Canary, Huntress, Sygnia — not fetched in this run."*

That signal is structured and self-emitted by the brief — perfect for closing the loop. Without it, the same handful of high-yield sources (NCSC.ch, CISA, CERT-EU, top vendor labs) get fetched every run while the rest of the curated list is silently starved by budget limits, biasing coverage toward those publishers' framings of the threat landscape. The goal is **neutral, balanced documentation of the ongoing threat landscape**, which requires source rotation.

### Added
- **Phase 0 — source rotation list construction.** The agent parses the `Coverage gaps:` line from § 7 of every brief in the last 7 days, aggregates source IDs / publisher names that appeared as gaps in 2 or more recent runs, and tags them as **rotation-priority** for this run. Each gap also carries the most recent *reason* (budget limit / navigation-page-only / dead host) so different responses can be applied.
- **Phase 1 — fetch budget reservation for rotation sources.** Each sub-agent reserves **6–8 of its ~30 fetch calls** for rotation-priority sources in its category scope. Must-have high-signal sources (CISA, NCSC.ch, CERT-EU, top vendor labs in scope) still go first; the reservation ensures the rest of the curated list also reaches the brief regularly.
- **Rotation-list handling rules** in Phase 1, mapping gap reasons to actions:
    - "not fetched, budget limit" → fetch this run.
    - "navigation page only" → fetch and *drill into linked articles*; if no dated content exists, record for source-list maintenance.
    - "consistent 404" → confirm and demote.
    - Successful fetch this run → source drops off the rotation list naturally for the next run.
- **Phase 4 § 7 format** — the `Coverage gaps:` line is now formally specified as parseable: single line, `Coverage gaps:` prefix, semicolon-separated `source-id (reason)` entries. Source IDs from `sources.json` preferred; publisher names fall back if not listed.
- **Phase 5 sources.json maintenance** — adds an optional `last_covered_in_brief` field per source (alongside the existing `last_successful_fetch`). Distinguishes "alive but quiet" from "alive and feeding the brief". Schema is allowed to grow; existing sources don't need backfill.
- **Phase 5** — new rule: a source that returns navigation pages only (no dated content) for 3+ consecutive attempted runs gets a `notes` flag and a reliability tier-down, but not full `demoted` status until a hard fetch failure.

### Effect on output
Over weeks, the brief covers a much wider slice of the curated source list. The W18 gaps (CCN-CERT, GovCERT.at, CERT.at, NCC Group Research, WithSecure Labs, Dragos, SANS ICS, Cloudforce One, Akamai SIRT, Elastic Security Labs, Group-IB, Secureworks CTU, Red Canary, Huntress, Sygnia) move to the front of W19's rotation reservation. Rotation is self-rebalancing: any source that gets fetched drops off the next run's rotation list automatically.

---

## 2.11 — 2026-05-06

### Why
A close read of the 2026-05-06 brief against the SANS ISC W18 TeamPCP weekly diary surfaced a structural problem: § 4 lumped four distinct W18 stories into one paragraph with one shared citation set:

1. The Mini Shai-Hulud SAP npm worm (Wiz / Socket / StepSecurity).
2. The cross-ecosystem propagation into PyPI Lightning and Packagist intercom-php (OX Security / Socket).
3. The first documented weaponisation of AI coding agent config files (.claude/settings.json, .vscode/tasks.json) by Mini Shai-Hulud (Wiz / Socket).
4. The Vect 2.0 ChaCha20 nonce-reuse / wiper-bug disclosure (Check Point Research, separate post).

Each is a distinct finding with a distinct primary publisher; the brief instead collapsed them into one paragraph and cited two roll-up sources (SANS ISC weekly diary + a Check Point weekly digest) instead of the four primary research posts. Net effect: the reader couldn't tell which source supported which claim, the substance got buried, and the citations sat one layer removed from the actual research.

### Added
- **Phase 1 research methodology — clarification on roll-up sources.** Weekly diaries (SANS ISC), vendor weekly threat-intelligence digests (Check Point's weekly research notes, etc.), and monthly summaries are *discovery*, not substance. Treat them like news: open them, follow the links to the primary publishers named inside, read those, and cite those. A roll-up cited for an individual claim is the same anti-pattern as citing news for a Mandiant finding.
- **Phase 4 — new "Item granularity — one story per item" subsection.** Distinct findings get distinct items, each with its own specific primary source set, even when they all attribute to the same actor / campaign / ecosystem. Worked example included (the W18 TeamPCP cluster: at least three brief items, possibly four — worm on SAP, cross-ecosystem propagation, AI-agent-config weaponisation, Vect wiper-bug). Section-level grouping with a one-line orientation sentence is fine; paragraph-level conflation is not.
- **Citation strategy** subsection extended:
    - "Don't cite a roll-up / weekly digest in place of the primary it summarises."
    - "One story = one set of citations." When item A's primary is Wiz and item B's primary is Check Point, those are two items in the brief, not one mixed paragraph.

### Effect on output
Future briefs will have more items per section but each item will be tighter — one specific finding, one specific primary source set, one specific defender takeaway. Sections like § 4 should look more like the SANS ISC W18 dated event log in structure: discrete dated events, each with its own attribution and source link, even when they cluster around one campaign.

---

## 2.10 — 2026-05-06

### Why
News sites are excellent at *discovery* — they tell defenders which vendor reports, CERT advisories, and primary research are worth reading this week. They are not the substance. The substance lives in the original Mandiant blog post, the CERT-FR advisory, the Volexity write-up, the SEC 8-K filing. A brief that summarises news summaries is two layers removed from the technical detail; a brief that cites the primary report puts the reader one click from the full content.

The 2026-05-06 brief was good but occasionally cited a news article when the underlying vendor report was the substance. This codifies the news-to-primary-source pivot as an explicit research and citation rule.

### Added
- **Phase 1 research methodology — rule 2: "News points to primary sources — always pivot to the report".** Sub-agents follow news links into the original vendor / CERT / research output and build the brief from the primary source. The news article becomes at most a *"via"* reference, included only when it adds something the primary source didn't.
- **Citation strategy** subsection in Phase 4 (composition):
    - Inline citations point to the primary source as the substance.
    - News added as *"via [Publisher](url)"* only when it adds value beyond the primary source.
    - Multiple primary sources are stacked inline when they corroborate (vendor blog + joint CISA advisory + Microsoft Threat Intel post on the same campaign — all three cited).
    - "Always link the primary report" rule: a brief paragraph without a primary-report link is a dead end.
- **Sub-agent 3 topical queries** expanded to include vendor-name + topic searches (e.g., *"Mandiant blog [today's month]"*, *"Talos research [today's month]"*) to surface primary reports directly without going through news.
- **Section 4 (Research & Investigative Reporting) guidance** updated: the cited link is to the primary report itself, not a news article that summarised it. Annual / periodic reports link to the report's landing page or PDF, not to news coverage.
- **Weekly summary** updated in parallel — same news-to-primary pivot rule.

### Effect on output
The brief becomes denser in primary-source links. A typical § 4 entry now links the actual vendor blog, advisory, or paper instead of the news article that pointed there. § 1, § 2, § 3 also gain primary-report links where journalism currently dominated.

---

## 2.9 — 2026-05-06

### Why
Reviewing the 2026-05-06 brief, four issues stood out:

1. **Workflow-internal language leaked into the brief.** Sentences like *"From Sub-agent 2. CH/EU nexus items first, then transferable global public-sector items."* appeared verbatim in the published Markdown. The reader doesn't know about sub-agents — that's prompt scaffolding, not output.
2. **Sub-agents summarised from index pages without drilling in.** When sub-agent 2 fetched `https://www.ncsc.admin.ch/ncsc/de/home/aktuell/im-fokus.html`, it took the page's title list as the data, instead of following the links into the individual advisories.
3. **Sub-agents stuck to fixed URLs and missed topical breadth.** The curated source list was treated as the only set, not the starting set. New high-quality sources discovered while researching weren't proposed; sources that delivered nothing weren't flagged.
4. **No explicit self-evolution authority.** The user's intent is fully autonomous operation — the agent should be free to refactor prompts, restructure sub-agents, curate sources, and add docs without a human gate. The prompt didn't say so explicitly.

### Changed
- **Phase 4 restructured.** The output structure (eight section headings) is now a clean table; per-section content guidance is a separate block clearly labelled *"do not reproduce in the brief"*. Added a hard rule against workflow-internal references in the output. Placeholder text changed from `_(composing — see Phase 4)_` to `_(no content yet)_` so any leak reads as a sensible empty-section indicator instead of a workflow reference.
- **Phase 1 sub-agent operational guardrails expanded.**
    - **Drill, don't summarise from index pages.** When fetching an aggregator / listing page, follow the links into individual articles. Two full advisories beat ten headline-level inferences.
    - **Topical `WebSearch` per sub-agent.** Each sub-agent runs 2–4 topical search queries per run to discover primary sources outside the curated list and to validate against missing major stories. Concrete query examples per sub-agent included.
    - **Source discovery.** Sub-agents return a `Sources discovered:` list with publisher, URL, why it's high-quality, scope. Main agent in Phase 5 writes them to `sources.json` as `candidate`.
    - **Source self-curation across runs.** Promote candidates after 3 successful runs; demote consistent failures or aggregator-only sources.
    - Fetch budget bumped from ≤20 to ≤30 calls per sub-agent to accommodate the drill-down work.
- **New top-level section: META — self-evolution authority** in both the daily and weekly prompts. Authorises the agent to modify the prompt, source list, docs, sub-agent structure, and repo layout in normal operation. Lists hard invariants that must not be removed (AI-content notice, inline links, two-source rule, no IOCs / vanity metrics, English output, always-produce, no workflow-internal language, two-stage publishing). Documents the process: bump version, write CHANGELOG entry explaining the change, commit alongside the brief.
- **Weekly summary** updated in parallel — Phase 3 restructured to match the daily Phase 4 pattern (clean output structure table, separate guidance block, no-leak rule); Phase 2 inherits the drill / topical-search / discover-sources rules.

### Effect on operator output
- The two-stage publishing chain is now reflected in the weekly's `push:` line variants: `push: ok (direct main) | ok (via auto-merge action) | failed (<reason>)`.

---

## 2.8 — 2026-05-06

### Why
After v2.7, `git push origin HEAD:main` is the primary publish path. But on the 2026-05-06 run that direct push was rejected (the routine container's enforcement varied from what Path C should have allowed), so the brief stayed on a `claude/...` feature branch even though Path C was enabled in the routine config. The fallback path needs to actually merge to `main` rather than depend on a human to merge a PR.

### Changed
- **Phase 6 (daily) and Phase 5 (weekly) now describe a two-stage publishing chain explicitly:**
    1. Direct push (`git push origin HEAD:main`).
    2. Fallback push to the current branch.
    3. The repo's GitHub Action (`.github/workflows/auto-merge-claude.yml`) fast-forwards `main` from the feature branch and cleans up.
  Operator output reports which stage published: `push: ok (direct main)`, `push: ok (via auto-merge action)`, or `push: failed (<reason>)`.
- **The Action ships with the repo** at `.github/workflows/auto-merge-claude.yml`. It triggers on `push` to `claude/**` and on manual `workflow_dispatch` (with a `branch` input for after-the-fact merging). Concurrency-guarded so simultaneous merges don't race.

### Set-up implication
The auto-merge Action needs `contents: write` on the repo's default `GITHUB_TOKEN`. The workflow declares it; in most repos this works as-is. If the repo's organization sets the default token to read-only, the Action's push to `main` will fail — fix in the repo's **Settings → Actions → General → Workflow permissions**. Documented in `docs/routine-setup.md`.

---

## 2.7 — 2026-05-06

### Why
The 2026-05-06 run published successfully — but to a `claude/determined-hypatia-PCpxM` feature branch instead of `main`, even though "Allow unrestricted branch pushes" (Path C) was enabled on the routine. Cause: the routine container *always* checks out a `claude/<adjective>-<name>-<id>` branch on session start, and v2.6 told the agent to "honour the environment branch and push there". Path C means the routine *can* push to `main`, but v2.6 didn't tell it to try.

### Changed
- **Phase 6 (daily) and Phase 5 (weekly) now use `git push origin HEAD:main` as the primary publish path.** This pushes the current commit to remote `main` regardless of the local branch name. With Path C enabled, the brief lands directly on `main` and is live immediately. No PR step, no merge gate, no auto-merge dependency.
- **Fallback** if the primary push is rejected with 403: push the current branch as-is, so a GitHub auto-merge rule, a GitHub Action, or a manual PR review can take the brief to `main`. This handles the case where Path C is accidentally disabled or the routine credential lacks repo-write scope.
- Removed the v2.6 "honour environment branch override" framing — the prompt now actively pushes to `main`, with the fallback handling environments that block direct pushes.

### `docs/routine-setup.md` updated
- Explains the `HEAD:main` mechanism.
- Adds an optional `.github/workflows/auto-merge-claude.yml` GitHub Action as a safety net for the fallback case.

---

## 2.6 — 2026-05-06

### Why
First successful end-to-end execution of the daily prompt produced a 21-item brief but failed to publish: the routine ran in a Claude Code routine container which forces a feature-branch workflow (`claude/<adjective>-<name>-<id>`) and pushes through an internal git proxy. The proxy returned HTTP 403 because the GitHub App credential it uses doesn't have write access to the repo. The agent retried with backoff four times, which was noise — a 403 is a permissions issue, not a transient blip.

### Changed
- **Branch selection is now explicit.** Default is `origin/main`. If the execution environment has assigned a different branch (routine container, CI worktree, etc.), the routine pushes there and trusts the environment's PR / merge / fast-forward policy to land the change on `main`. The agent should not second-guess the environment's branch instructions.
- **Push-failure handling is one-shot.** No retry-with-backoff. A 403 won't resolve in seconds; a network blip will be picked up by the next run. One push attempt, surface the error verbatim, keep the local commit, exit cleanly.

### Same content guarantee
The brief's content, structure, and source pipeline are unchanged. Only the publish-step semantics shifted to be honest about feature-branch workflows and to stop retrying on hard auth errors.

---

## 2.5 — 2026-05-06

### Why
Second observed failure mode: with v2.4, all four sub-agents returned successfully and verification + deep-dive selection completed, but the final composition step hit `API Error: Stream idle timeout — partial response received`. The brief was being written in a single large `Write` tool call (the entire 8-section Markdown blob in one streamed response). The model pauses between sections during generation, and those pauses are long enough to trip the proxy's idle threshold on a large output.

### Changed
- **Phase 4 (daily) and Phase 3 (weekly) now require incremental writes.** One `Write` for the skeleton (header + AI notice + metadata + TL;DR + section headings with `_(composing — see Phase 4)_` placeholders), one `Read` to satisfy the `Edit` tool's precondition, then one `Edit` per section to replace the placeholder with the section's full content. Each `Edit` is a much shorter streamed output, well within idle-threshold safety.
- If a single section's content is itself unusually long (e.g., a vuln table with many rows), the agent splits that section's Edit into two halves.

### Same-output guarantee
The brief's content and structure are unchanged. Only the I/O pattern of the composition phase shifts — from one large `Write` to one `Write` + N `Edit` calls. This trades a small amount of tool-call overhead for stream-stability.

---

## 2.4 — 2026-05-06

### Why
Observed failure mode on first real run (2026-05-05): three of four sub-agents returned successfully, the fourth (Switzerland, Europe & Public Sector — slow national-CERT pages with German translation work) did not return on time, and the main agent waited indefinitely. No brief was written. **Never block the routine on one slow sub-agent.**

### Added
- **Prime Directive 12 — Always produce a brief; never block on a single sub-agent.** Specifies exact behaviour for 4/4, 3/4, 1–2/4, and 0/4 sub-agent return rates. Worst case still produces a stub brief with a "Quiet run — no sub-agent results" header. The presence of the file is the operational signal that a run took place; its absence is worse than a sparse file.
- **Operational guardrails for sub-agents** (Phase 1):
    - Target ≤20 WebFetch / WebSearch calls per sub-agent.
    - Per-source timeout: skip on hang/error, do not retry more than once.
    - Wall-clock soft cap of ~10 minutes per sub-agent — return what you have if you run long.
    - Always return something, even a one-line "no qualifying items" explanation.
- **Phase 2 trigger condition** is now explicit: begin as soon as all sub-agents that are going to return have returned (10-minute stall window). Do not wait indefinitely.
- **Quality gate added**: a brief file *must* exist at `briefs/YYYY-MM-DD.md` after every run.
- Same partial-result rules ported to the weekly summary (Phase 2).

---

## 2.3 — 2026-05-05

### Changed
- **Phase 6 renamed `COMMIT & PUSH`.** The routine now `git push origin main` after committing — every brief is published immediately. No review branch, no staging gate. Same for the weekly summary. Push failures do not roll back the commit; they are surfaced in operator output and a later run / manual push catches up. The routine never `--force`-pushes.
- **Active source maintenance** — Phase 5's `sources/sources.json` rules are now stronger:
    - Before demoting a source on 3 consecutive failures, the agent does **one canonical-URL probe** and updates the `url` in place if an equivalent page exists at the same publisher.
    - When a clearly better URL is discovered for an already-listed publisher, the agent updates the `url` in place (keeping the `id` stable so historical state references remain valid).
    - Every URL change is annotated with a dated note in the source's `notes` field and enumerated in the run's commit body.
    - Sources still cannot be deleted — `demoted` is the soft-removal mechanism.
- **Active CVE-index maintenance** — Phase 5's `state/cves_seen.json` rules are now stronger:
    - On reuse of an already-known CVE today, the agent updates `title` if a better short title exists (e.g., a CVE got a public name) and `primary_source_url` if a clearly better authoritative source now exists.
    - Records that turn out to be invalid (e.g., the CVE ID does not resolve on NVD/MITRE — a hallucinated identifier from an earlier run) are **removed**, with the removal noted in the commit body.
- Operator output now includes a `push: ok | failed (<reason>)` line.
- README and `docs/workflow.md` updated to reflect auto-push behaviour and the active maintenance rules.

### Why
The routine produces a public CTI feed; manual review-and-push doesn't fit that model. Auto-push to `main` makes every brief live immediately. Active source / CVE maintenance keeps the repo operationally honest over time without human babysitting — broken links self-heal where possible, and bad data self-corrects.

---

## 2.2 — 2026-05-05

### Changed
- **Daily sub-agents reduced from 7 to 4** with cleanly-partitioned source categories. The new four are:
    1. Active Threats & Trending Vulnerabilities (was A + D)
    2. Switzerland, Europe & Public Sector (was B + C)
    3. Research & Investigative Reporting (was E + F)
    4. Incidents & Disclosures (was G)
  Each source category belongs to exactly one sub-agent's filter, so no two agents touch the same source for the same purpose. Goal: cut per-run LLM load to avoid stream-timeout and rate-limit failures, while keeping coverage.
- **Daily brief output sections reduced from 10 to 8** to match the four-agent layout. New sections 0–7: TL;DR, Active Threats & Trending Vulnerabilities (with embedded vuln table as part 1b), Switzerland Europe & Public Sector, Notable Incidents & Disclosures, Research & Investigative Reporting, Deep Dive, Updates to Prior Coverage, Verification Notes.
- **Weekly horizon sub-agents reduced from 3 to 2.** W1 now combines long-running-campaign status checks with the annual / periodic-report horizon (both are "ongoing items beyond the daily window"). W2 keeps the strategic / policy horizon. The composed weekly summary's section list is unchanged.
- Quality gates and `Phase 5 — STATE UPDATE` `section` enum aligned to the new section names.

### Source list updates
- `cisa-kev` URL unchanged (`https://www.cisa.gov/known-exploited-vulnerabilities-catalog`).
- `cisa-alerts` renamed to `cisa-advisories` (URL unchanged: `https://www.cisa.gov/news-events/cybersecurity-advisories`).
- Added `cisa-news` (`https://www.cisa.gov/news-events/news`).
- Added `cisa-directives` (`https://www.cisa.gov/news-events/directives`).
- `shadowserver` URL updated to `https://www.shadowserver.org/news-insights/`.
- `agid-csirt-it` renamed to `csirt-acn-it`, URL updated to `https://www.acn.gov.it/portale/en/csirt-italia/alert-e-bollettini`.
- `prodaft` URL updated to `https://www.prodaft.com/reports`.
- `ncsc-ch` split into two entries — `ncsc-ch-incidents` (`aktuelle-vorfaelle.html`) and `ncsc-ch-focus` (`im-fokus.html`); both German, with note to translate findings.
- `ncsc-nl` removed (no news output available at the previous URL).

### Why
v2.1 runs were hitting "Stream idle timeout — partial response received" and Anthropic per-period usage limits when seven sub-agents ran in parallel and each did extensive WebFetch / WebSearch work. The four-agent design keeps the same scope under one tighter budget. The source-list updates align with the actual canonical pages of the publishers.

---

## 2.1 — 2026-05-05

### Changed
- **Added a `DEFENSIVE PURPOSE` preamble** to both prompts, immediately after `ROLE`. States explicitly that this is a defensive intelligence workflow for protectors, that every section is written from the defender's vantage point, and that the brief contains no operational attack details. Helps the framing stay correct end-to-end.
- **Sub-agent spawn prompts must lead with a defensive-intent statement** (template provided). Applies to all seven daily sub-agents and all three weekly horizon sub-agents.
- **Sub-agent G renamed and reframed** from "Major Breaches" to "Incident & Disclosure Roundup". Now explicitly framed as a *defender's overview* of who was publicly affected and what disclosed root causes can be learned from. Dark-web listings are treated as unverified claims and phrased accordingly. Each item ends with a *defender takeaway*. Output section 6 in the brief renamed "Notable Incidents & Disclosures".
- **Sub-agent C, F** got short defensive-purpose lines added.
- **Deep-dive language softened**: "Kill chain narrative" → "Incident narrative" framed from the defender's perspective.
- **Weekly summary § 5** renamed from "Major breaches recap" to "Incidents & disclosures recap" with defender-learning framing.

### Why
The previous v2.0 phrasing — although structurally fine — accumulated cybersecurity terminology that was triggering Anthropic's cyber-content usage-policy filter when sub-agents executed in parallel. Reframing to defender-first language and adding explicit defensive-intent statements at every level keeps the workflow operating as intended.

### Output structure unchanged
Section count and ordering of the daily and weekly briefs are unchanged; only the wording of section 6 and the framing within sub-agents has shifted.

---

## 2.0 — 2026-05-05

### Added
- **Weekly summary track.** New `prompts/weekly-summary.md` for a once-a-week extended brief that consolidates the week's daily briefs and adds horizon view, multi-day campaign rollups, and integration of yearly/periodic threat reports.
- **Major Breaches sub-agent (G).** Daily brief now has a dedicated sub-agent for newly disclosed breaches, drawing from regulator notices (SEC EDGAR 8-K, ICO, CNIL, EDPB) and victim disclosures, with a new § 6 section.
- **CVE fast-lookup index** (`state/cves_seen.json`). Flat list keyed by CVE ID for sub-agent dedup, complementing the richer `covered_items.json`.
- **Yearly/periodic-report rule** (Prime Directive 9). Annual reports (M-Trends, CrowdStrike GTR, ENISA TLR, Verizon DBIR, MS Digital Defense, IBM X-Force, Truesec TIR, Dragos OT YIR) get one dedicated treatment, then are not re-summarised — only cross-referenced as context.
- **Historical-context rule** (Prime Directive 10). For *highly relevant* deep-dive items with prior public reporting older than ~6 months, a Background paragraph (3–5 sentences) summarises what was known, with inline links. Targets the "humans forget things" problem without bloating routine items.
- **English-only output** (Prime Directive: Language). The brief is always in English even when sources are German / French / Italian / Polish — translate findings and keep original-language source titles.
- New sources: Sygnia, InfoGuard (CH), Truesec, NCC Group Research, WithSecure Labs, IBM X-Force, Akamai SIRT, Cloudflare Cloudforce One, Tenable Research, Rapid7 Research, GreyNoise Labs, Shadowserver Foundation, Citizen Lab, Dragos, CERT.at, GovCERT.at, CERT-PL, Trustwave SpiderLabs, SANS ICS (industrial), Help Net Security, Security Affairs, SEC EDGAR 8-K, UK ICO, CNIL FR, EDPB.
- New categories in `sources.json`: `breaches`, `ot-ics`.

### Changed
- **Look-back window: 7 days** (was 5). Reduces repeats during long-running campaigns and matches the weekly cadence.
- **Sub-agent return format is now flexible Markdown** with required fields, not a strict JSON schema. Sub-agents may add extended context and analysis. Required fields remain stable.
- **No token cap on sub-agents.** Sub-agents do whatever depth the topic warrants; they return summarised findings, not raw HTML.
- Updated `govcert-ch` URL to `https://www.ncsc.admin.ch/govcert` (legacy `govcert.ch` 302-redirects).
- Renamed daily output structure: § 6 Major Breaches inserted; Deep Dive moves to § 7; Updates to § 8; Verification Notes to § 9.

### Verified live (2026-05-05)
- NCSC.ch, GovCERT.ch (via redirect), Sygnia, InfoGuard, Compass Security, scip.ch, watchTowr Labs.

---

## 1.0 — 2026-05-05

Initial canonical version.

### Operating principles
- Zero LLM knowledge: every fact must come from a source fetched in the run.
- Inline source links at the point of claim; no bibliography.
- No IOCs (hashes, IPs, attacker domains/URLs, rule code).
- No vanity metrics (dwell time, breakout time, %-YoY).
- Two-source verification by default with national-CERT carve-out.
- Recency window 24 h default, 72 h for active campaigns.
- No-repetition rule with explicit `UPDATE` mechanism for material new developments.
- Long-running-campaign rule: ≤1 update per week unless critical change.
- Empty-section discipline.

### Execution model
- Six topic-scoped sub-agents spawned in parallel.
- JSON return schema (replaced by flexible Markdown in v2.0).
- Main context handles verification, deep-dive selection, composition, state update, commit.

### Output
- `briefs/YYYY-MM-DD.md`, sections 0–8.
- Updates `state/covered_items.json` and `sources/sources.json`.
- Conventional git commit.

### Source list
- Initial seed of ~40 sources across categories.
- Reliability tiers: HIGH / MEDIUM. Statuses: active / candidate / demoted.
- Maintenance rules: never delete; demote after 3 consecutive failed fetches; new sources enter as `candidate`.
