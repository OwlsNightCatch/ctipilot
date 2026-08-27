# Verification Policy

Defends the pipeline's published entries against hallucination, vendor hype, fake-news patterns common in CTI feeds, and silent drift over time.

---

## Two-source rule, with carve-outs

**Default:** every claim must be corroborated by ≥2 independent reputable sources before an entry publishes (`verification: multi-source`). Reputable means a publisher present in `sources/sources.json` with `status: "active"` and a NATO Admiralty `reliability` of at least **C** (A/B/C — i.e. not D/E/F), or a previously unseen publisher with a clearly verifiable editorial track record (in which case the agent also proposes them as a `candidate` source). Independence is about first-hand observation, not count — six rewrites of one wire story are one source.

**National-CERT carve-out** (`verification: single-source-national-cert`): when a high-reliability (Admiralty A / B) national CERT or government cybersecurity authority is the **primary disclosing party for its own jurisdiction or for an advisory it owns**, single-source is acceptable.

<!-- ORG-PROFILE:BEGIN org-certs -->
<!-- GENERATED from config/org-profile.yaml — do not edit by hand; edit the config and run: python3 tools/compose_prompts.py --write -->
**National-CERT single-source carve-out list** — a high-reliability (Admiralty A / B) national CERT / government cybersecurity authority acting as the primary disclosing party for its own jurisdiction or an advisory it owns is acceptable as a single source: NCSC-CH, GovCERT.ch, CERT-EU, ENISA, BSI, ANSSI/CERT-FR, NCSC-UK, NCSC-NL, CISA, CCN-CERT, AGID-CSIRT-IT, CERT.at, CERT-PL. The list is deployment-configurable (`national_certs` in config/org-profile.yaml); treat it as the trust bar, illustrative rather than exhaustive for same-tier authorities.
<!-- ORG-PROFILE:END org-certs -->

The reasoning: these organisations *are* the authoritative source for advisories they issue. Their *commentary on someone else's disclosure* still requires the standard two-source rule.

**Victim-own-disclosure carve-out** (`verification: single-source-victim`): a victim's own regulatory filing (SEC 8-K, regulator notice) or public statement about its own incident is authoritative for what it discloses, even before independent press coverage exists.

**Everything else single-source** is `verification: single-source` with a `sourcing_note` naming the situation — the renderer surfaces the badge so the reader sees the reduced confidence.

**Contradictions** (`verification: contradicted`) are surfaced in the run record's verification notes AND on the entry, never silently resolved by picking a side.

---

## Fake-news patterns to defend against

### Ransomware leak-site claims
Frequently inflated; sometimes wholly fabricated. Some groups list victims they breached only superficially, list re-extorted victims twice, or list organisations they never touched as "marketing".

**Rule:** never publish a leak-site claim as fact unless the named victim has confirmed (or pointedly declined to confirm), or a high-reliability (Admiralty A / B) journalist with original sourcing has corroborated. Mirror-data-only (ransomware.live / ransomlook.io) is an *observation that the group claimed X*, not that X is true. Phrase accordingly or drop.

### Hallucinated CVE numbers
Sub-agents (and humans) sometimes invent CVE identifiers that look plausible but do not exist, or transpose digits.

**Rule:** verify any CVE entering an entry's `cves[]` or body resolves on `https://nvd.nist.gov/vuln/detail/CVE-YYYY-NNNNN` or MITRE. If it does not resolve and no official equivalent exists, the CVE is dropped and the underlying claim re-checked or removed.

### AI-generated security blogspam
Sites with anonymous "authors", AI-generated stock images, and confidently stated wrong details. They aggregate other people's reporting, sometimes invert facts, and do not respond to corrections.

**Rule:** no named author byline, no editorial-standards page, no corrections track record, LLM-pattern prose → discovery only; trace to primary. Never cite as primary or corroborating.

### Vendor press releases dressed as research
**Rule:** separate the technical claim from the product pitch. The campaign claim is includable if it stands on its own; the product-efficacy claim is not.

### Months-old news as "new"
**Rule:** check the **original** event date, not the article date — that is what the entry's `event_date` field records. First English coverage of a weeks-old foreign-press story is still timely; the third re-statement of three-week-old news is not.

### Sweeping attribution claims
**Rule:** only accept attribution from organisations with a track record and a stake in being right (frontline IR vendors, national authorities, peer-reviewed research). From anyone else, attribute the *claim*, not the actor: "ESET reports the campaign matches the TTPs of X" — never "X is behind it". Entity links (`entities:`) follow the same rule — link the actor the source *names*, with the claim attributed in the body.

### Telegram / X-only sourcing
**Rule:** never publish a claim sourced only from a Telegram channel, X/Twitter post, Mastodon toot, or LinkedIn update. Discovery only; trace to a publication.

---

## Recency sanity check

Every entry reflects events inside the run's gap-derived recency window (`window_hours` — see `prompts/cti-run.md` PD-7; developing stories up to `developing_window_hours`). Older material qualifies only as: a *material new development* on covered ground (→ an `update` changelog record on the existing entry, delta only); a vendor advisory freshly relevant (e.g. quietly KEV-listed today); or a national-CERT publication today referencing prior activity. In every case `event_date` states the original date so the reader is never misled.

---

## Quality-gate checklist (agent self-check before the mechanical gate)

- [ ] Every claim has an inline link to a source fetched this run; every URL in `sources[]` was actually fetched and matches its claim.
- [ ] Zero IOCs anywhere (hashes, IPs, attacker domains/URLs, rule code).
- [ ] Zero vanity metrics.
- [ ] No duplication of covered ground (incl. earlier runs today, and the store-wide CVE index): repeats are changelog records on the existing entry with a material delta, or dropped; every record has its `## <Type> — <at>` section and no entry was edited without one.
- [ ] Every entry's `verification` value is correct: `multi-source` needs ≥2 independent sources; carve-outs named in `sourcing_note`.
- [ ] Classification set on EVERY entry — never zero ratings: every non-triage-kind entry carries a valid Admiralty `classification` (reliability A–F tracking the cited source's own letter; credibility 1–6 tracking corroboration, assessed independently); triage-kind entries carry `org_triage` + `classification: null` when a triage scheme is configured, and the Admiralty block like every other kind when none is (`check_run.py` FAILs a missing rating from v3.18).
- [ ] CVE identifiers verified against NVD/MITRE; `cves[]` records complete (type/vector/auth/status).
- [ ] `evidence[]` present and verbatim on every critical-priority and exploited-status entry — each quote a **contiguous** substring of a fetched page (no ellipsis splices, no re-hedging; two passages = two records).
- [ ] `techniques[]` carries every ATT&CK id the body maps and nothing the body doesn't describe — and is **never empty on a `threat`/`incident`/`vulnerability` entry** (the access/exploitation vector is always mappable; `check_run.py` FAILs it from v3.18); ids woven into prose at the behavior they name (no bare ID lists); `affected_products[]` names only products the cited sources name; any `**Triage:**` discriminator follows from the cited mechanism (omitted, never invented, when the sources give no basis).
- [ ] All entity references resolve in `entities/registry.yaml` (aliases checked); new entities registered with sourced definitions.
- [ ] `priority` calibrated (critical ⇔ immediate_action bar; high ⇔ TL;DR-worthy); every entry clears the strict relevance/actionability gate (no count target or ceiling).
- [ ] `actions[]` clears the do-now bar (`prompts/cti-run.md` Phase 4 § `actions[]`): only concrete, finding-derived, start-now tasks; no generic advice, no body restatement, no in-window duplicates; empty where nothing qualifies.
- [ ] Deep-dive treatment reserved for an item that earns it; category rotation applied.
- [ ] Run record complete: telemetry, verification counters, notes with drops / single-source / contradictions / parseable lines.
- [ ] **`python3 tools/check_run.py "$RUN_ID"` exits 0 BEFORE the verification sub-agent is spawned** — the verifier reads output whose schema / URLs / taxonomy / dedup are already mechanically clean.
- [ ] **Phase 5.7 verification sub-agent ran ≥1 iteration (≥2 for a CLEAN publish)** covering both URL truth and editorial quality; confirmed CLEAN (two consecutive CLEAN verdicts on two different models) within ≤8 iterations, or residuals / a `confirmation_waived` reason logged in the run record.
- [ ] No `sources[]` URL on the hard-blocked pattern list (NVD/MITRE/cve.org per-CVE pages, homepages, category landings, advisory indexes — enforced by `tools/check_run.py`).
- [ ] Every `sources[]` URL returns HTTP 200 on a live HEAD/GET at commit time (ledger-cached fetches trusted).

---

## Phase 5.7 — Final verification sub-agent (URL truth + editorial quality)

After entries and the run record are written, state is updated, and `tools/check_run.py` exits 0 (the cheap mechanical gate runs first), an independent verification sub-agent reads the run's output end to end — every new entry (frontmatter AND body), every entry the run appended a changelog record to (read whole; the new section and every changed field checked against the cited sources), plus the run record — as a hostile, technically-fluent SOC reader with no memory of how the run was assembled. **The gate to publish is a confirmed CLEAN — two consecutive iterations, on two different models, both returning verdict CLEAN** (v3.23; the 8-iteration cap — raised from 5 in v3.27 — and the low-residual early exit are the fail-open safety valves). A single model's CLEAN never publishes alone: the rotation puts the confirmation pass on the other model, so one model's blind spot is never the last word.

**Truth gate.** Every URL fetched; every claim cross-checked against its linked source; every named entity traced to a fetched source; every `evidence[]` quote confirmed verbatim; frontmatter ⇔ body agreement (a `summary` claiming more than the body's sources support is a hallucination with a notification blast radius).

**Editorial-quality gate.** Relevance to the profiled organization; primary-source strength (vendor PSIRT / research lab / regulator / victim first — NVD/CERT second-tier); priority calibration; action-item discipline (`actions[]` do-now bar); correct update-vs-new decisions; vendor-marketing tells; fake-news patterns; contradictions; clarity for a Tier 2 responder; missed angles.

The verifier's finding categories (F1–F18), report format, and compact-summary contract live in [`.claude/agents/cti-verification.md`](../.claude/agents/cti-verification.md). **Verifier-model rotation:** odd iterations spawn `cti-verification` (Opus default), even iterations `cti-verification-alt` (Sonnet default) — byte-identical operational prompts, different model pins — so model-specific blind spots are caught across iterations; even iterations receive the prior iteration's findings + applied remediations so the alternate model verifies fixes instead of flip-flopping. The rotation also carries the double-CLEAN gate: the confirming iteration is by construction a different model, so every CLEAN publish rests on two independent models agreeing.

### Iterative refinement loop (double-CLEAN to publish; cap 8 — fail-open safety valve, not goal)

Remediation per finding type, re-run `tools/check_run.py`, fresh re-spawn — the full loop, decision rules (incl. the CLEAN-confirmation pass) and remediation table live in `prompts/cti-run.md` Phase 5.7. Up to 3 follow-up `cti-research` sub-agents per iteration for `Needs more research` / `Missed angles`. Iteration counters and per-iteration findings land in the run record's `verification` block — the Ops dashboard at `/ops/` and the per-run pages at `/runs/<run-id>/` surface cap-breaches and unconfirmed-CLEAN waivers.

---

## Operator review pattern

Periodically, a human operator reviews:

- `git log -- sources/sources.json` for demotions and candidates; promote or revert as warranted.
- Recent run records' verification-notes bodies for recurring single-source patterns or repeated drops (a missing source, or a quality issue with an existing one).
- `entities/registry.yaml` growth for duplicate or drifting entity definitions.
- The Ops dashboard's verification panel for cap-breach and residual trends.
