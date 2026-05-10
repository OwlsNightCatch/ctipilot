# Verification Policy

Defends the brief against hallucination, vendor hype, fake-news patterns common in CTI feeds, and silent drift over time.

---

## Two-source rule, with a national-CERT carve-out

**Default:** every claim must be corroborated by ≥2 independent reputable sources before inclusion in the brief. Reputable means a publisher present in `sources/sources.json` with `status: "active"` and `reliability` of at least MEDIUM, or a previously unseen publisher with a clearly verifiable editorial track record (in which case the agent also proposes them as a `candidate` source).

**National-CERT carve-out:** when a HIGH-reliability national CERT or government cybersecurity authority is the **primary disclosing party for its own jurisdiction or for an advisory it owns**, single-source is acceptable.

Carve-out qualifiers (illustrative, not exhaustive):
- NCSC-CH, GovCERT.ch
- CERT-EU, ENISA
- BSI (Germany), ANSSI/CERT-FR (France)
- NCSC-UK, NCSC-NL
- CISA (USA)
- AGID/CSIRT-IT (Italy), CCN-CERT (Spain)

The reasoning: these organisations *are* the authoritative source for advisories they issue. Their *commentary on someone else's disclosure* still requires the standard two-source rule.

**Single-source items that do not qualify for the carve-out** must be marked `[SINGLE-SOURCE]` next to the item title, with the source named explicitly in the body.

**Contradictions** are surfaced in § 8 Verification Notes of the brief, not silently resolved by picking a side.

---

## Fake-news patterns to defend against

### Ransomware leak-site claims
Frequently inflated; sometimes wholly fabricated. Some groups list victims they breached only superficially, list re-extorted victims twice, or list organisations they never touched as "marketing".

**Rule:** never include a leak-site claim as fact unless the named victim has confirmed (or pointedly declined to confirm), or a HIGH-reliability journalist with original sourcing has corroborated. If the only source is `ransomware.live` / `ransomlook.io` mirror data, it is an *observation that the group claimed X*, not that X is true. Phrase accordingly or drop.

### Hallucinated CVE numbers
Sub-agents (and humans) sometimes invent CVE identifiers that look plausible but do not exist, or transpose digits.

**Rule:** verify any CVE cited in the brief resolves on `https://nvd.nist.gov/vuln/detail/CVE-YYYY-NNNNN` or `https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-YYYY-NNNNN`. If it does not resolve and no official equivalent exists, the CVE is dropped and the underlying claim is re-checked or removed.

### AI-generated security blogspam
A growing problem. Sites with anonymous "authors", AI-generated stock images, and confidently stated wrong details. They aggregate other people's reporting, sometimes invert facts in the process, and do not respond to corrections.

**Rule:** if a site has no named author byline, no editorial standard page, no track record of corrections, and the prose reads like LLM output (uniform paragraph length, suspiciously fluent without specifics, no original sourcing), treat it as discovery only and trace to primary source. Never cite as primary or corroborating.

### Vendor press releases dressed as research
Vendor blog posts that are 80 % product marketing and 20 % threat content. The threat content may be real but framed to drive demand for the vendor's product.

**Rule:** separate the technical claim from the product pitch. Cite the technical claim only if it stands on its own. If the report is "we observed X campaign and our product caught it", the campaign claim is includable; the product efficacy claim is not.

### Months-old news as "new"
Aggregators and AI-driven news bots regularly republish months-old incidents as fresh. The article date can be today; the underlying event can be months back.

**Rule:** check the **original** event date, not just the article date. If the article is the first English-language coverage of a foreign-press story from weeks ago, treat as still timely if no English coverage existed before. If it is the third re-statement of US news from three weeks ago, drop.

### Sweeping attribution claims
Attribution by aggregators, bloggers, or non-research outfits should be treated with extreme caution. Attribution requires technical evidence (overlapping infrastructure, code reuse, victimology, operational TTP fingerprints), not just "looks like X".

**Rule:** only accept attribution from organisations with a track record and a stake in being right (the major frontline IR vendors, national authorities, peer-reviewed research). When any other source attributes, attribute the *claim*, not the actor: "ESET reports the campaign matches the TTPs of X" — not "X is behind it".

### Telegram / X-only sourcing
Single-source social-media posts are not sources. Even if the post is by a researcher with a track record, it is a lead, not a claim.

**Rule:** never include a claim sourced only from a Telegram channel, X/Twitter post, Mastodon toot, or LinkedIn update. Use these as discovery only; trace to a publication.

---

## Recency sanity check

Every item in the brief must reflect events within the last 24 h (default) or 72 h (active campaign). When a sub-agent surfaces something older, the agent must confirm it qualifies under one of:

- A *material new development* on a longer-running campaign (in which case it goes under § 5 Updates to Prior Coverage with the original date).
- A vendor advisory that happened to land late but is freshly relevant (e.g., a CVE quietly added to KEV today for a 2024-disclosed flaw).
- A national-CERT publication today that references prior activity.

In every case the brief states the original date so the reader is not misled.

---

## Quality-gate checklist (agent self-check before write)

- [ ] Every claim has an inline link to a source fetched today.
- [ ] Zero IOCs anywhere (hashes, IPs, attacker domains/URLs, rule code).
- [ ] Zero vanity metrics (dwell time, breakout time, YoY counts).
- [ ] No item from the last 7 briefs appears unless under § 5 Updates with a delta + an inline citation.
- [ ] Every item passed two-source verification, OR is national-CERT primary disclosure, OR is marked `[SINGLE-SOURCE]`.
- [ ] CVE identifiers verified against NVD/MITRE.
- [ ] CH/EU/public-sector items in § 2 carry the appropriate `Region:` and `Sector:` tags in their metadata footer.
- [ ] Deep dive present, or explicit "no item met the bar".
- [ ] State files updated (`state/covered_items.json`, `sources/sources.json`).
- [ ] Verification Notes section lists drops, single-source items, and contradictions.
- [ ] No content from training data — only from today's fetches.
- [ ] **`python3 tools/check_brief.py` exits 0 BEFORE the verification sub-agent is spawned** — every mechanical consistency check passes first; the verifier reads a brief whose URL allowlist / footer taxonomy / CVE-sync / run-log shape is already clean.
- [ ] **Phase 5.7 (daily) / Phase 4.7 (weekly) verification subagent ran** (see below) covering both URL truth and editorial quality; verdict reached `CLEAN` within ≤5 iterations or residual findings logged in § 8.
- [ ] CVE entries do not lean on a national CERT/NCSC as the *only* primary source — the disclosing vendor's PSIRT advisory or research-lab post is preferred.
- [ ] **No `Source:` URL is on the hard-blocked allowlist** (NVD/MITRE/cve.org per-CVE pages, Heise homepage / `/news/` / `/security`, NOS homepage / `/artikel/`, CERT-FR `/avis/` or `/actualite/` indexes, CISA news-events root, Dragos year-in-review marketing landing, ABW cybersecurity category landing). The full list is enforced by `tools/check_brief.py` and lives at the top of the script.
- [ ] **Every `Source:` URL returns HTTP 200 on a live HEAD/GET** at commit time (`tools/check_brief.py` validates). 404s are typically fabricated URLs that look plausible — re-pivot to a real one or drop the item.
- [ ] Multi-CVE items carry per-CVE breakdown for fields whose value differs (`CVSS: 9.1 / 7.2`, `Auth: pre-auth (CVE-…), admin-required (CVE-…)`).

---

## Phase 5.7 (daily) / Phase 4.7 (weekly) — Final verification sub-agent (URL truth + editorial quality)

After Phase 4 has written the brief, Phase 5 has updated state, and Phase 5.5 has run `tools/check_brief.py` to exit 0 (the cheap mechanical gate runs first), an independent verification sub-agent reads the brief end to end. The verifier does not see the research transcript and reads the publication as a hostile, technically-fluent SOC reader would. **The verifier's CLEAN verdict is the gate to publish** — no commit until CLEAN, except via the iteration-cap fail-open at iteration 5. **Two distinct concerns are checked in the same pass:**

**Truth gate.** Every URL fetched, every claim cross-checked against its linked source, every named entity (CVE / actor / campaign / version / date / number) traced back to a source the verifier could read. Catches: hallucinated URLs, generic landing pages cited as sources, claims attached to the wrong source, named entities that drifted into prose without source backing, aggregate numbers not in any linked source.

**Editorial-quality gate.** Every item assessed against:

1. **Relevance** to a Swiss / EU public-sector SOC — items that are interesting in the abstract but operationally irrelevant are flagged for drop.
2. **Primary-source strength** — first source should be a vendor PSIRT advisory / research-lab post / vendor blog / regulator filing / victim statement. NVD/MITRE and national CERTs/NCSCs are second-tier primaries; they belong as `Additional source:` unless a vendor or research-lab post genuinely does not exist for this item. Items whose only source is `nvd.nist.gov` or `cert.ssi.gouv.fr` (or similar) get flagged.
3. **Vendor-marketing tells** — vanity metrics, product-efficacy claims, AI-blogspam patterns.
4. **Fake-news patterns** — leak-site claims as fact, sweeping attribution by non-research outfits, Telegram/X-only sourcing, months-old news as new.
5. **Contradictions** between sources cited for the same item.
6. **Clarity** — is anything under-explained to the point that a Tier 2 responder could not act on it without further research?

The verifier returns structured Markdown with sections `Broken / unreachable URLs`, `Generic / oversight URLs`, `Citation does not support the claim`, `Unsupported / hallucinated facts`, `Claims missing inline citation`, `Strengthen primary source`, `Drop`, `Needs more research`, `Surface contradiction`, `Missed angles`, `Editorial / less-is-more flags`, **`Single-source items missing [SINGLE-SOURCE] flag`** (F12 — promoted from "the gatekeeper sometimes catches" to a numbered finding in v2.47), and a `Verdict: CLEAN | NEEDS_FIXES`.

**Verifier-model rotation (v2.47):** the main agent rotates between two verifier sub-agent definitions across iterations — odd iterations spawn `cti-verification` (Opus default), even iterations spawn `cti-verification-alt` (Sonnet default). The two definitions carry the byte-identical operational system prompt; only the YAML model frontmatter differs. This rotation catches model-specific blind spots that would otherwise silently inherit when every iteration runs on the same model.

### Iterative refinement loop (cap: 5 iterations — fail-open safety valve, not goal)

The main agent reads the verification report and remediates per finding type:

| Finding | Main-agent response |
|---|---|
| Broken / generic URL | Replace with a specific article URL fetched fresh now (re-pivot via `WebFetch` / `WebSearch` / `tools/fetch_source.py`). |
| Citation does not support claim | Replace the claim with a narrower one the source supports, or replace the citation. |
| Unsupported / hallucinated fact | Drop the fact and the claim it props up. |
| Missing inline citation | Add the citation, or rewrite the sentence to drop the unsourced fact. |
| **Strengthen primary source** | Re-pivot via `WebSearch` / `WebFetch` to the vendor PSIRT advisory or vendor research blog. Promote that to first source; demote NVD/CERT to `Additional source:`. |
| **Drop** (low relevance) | Remove the item; log in § 8; remove the matching `appearances[]` entry for today from `covered_items.json`. |
| **Needs more research** | Spawn ≤3 follow-up research sub-agents in parallel; re-Edit the affected item with new findings, or drop. |
| **Surface contradiction** | Add an explicit § 8 contradiction line; do not silently pick a side. |
| **Missed angles** | Spawn one targeted research sub-agent if the angle would clear the inclusion gate; else log as a coverage gap. |
| Editorial / less-is-more (advisory) | Apply if cheap; otherwise leave. |

After remediation, the main agent **re-runs `python3 tools/check_brief.py`** to confirm the fixes did not introduce mechanical drift, then a **fresh** verification sub-agent is spawned (no shared memory) against the updated brief. The loop runs until verdict `CLEAN` or until the iteration cap (5) is reached. After the cap, the brief publishes regardless as a fail-open safety valve, with unresolved findings logged in § 8 — the prime directive (the brief must publish) wins. **The cap is a safety net, not the goal** — a brief that needs 5 iterations is a quality regression and gets reviewed after-the-fact.

**The main agent may spawn up to 3 follow-up research sub-agents per iteration**, each scoped to one specific question with a suggested source / search angle from the verifier. These sub-agents share the Phase 1 patience clause and 30-min wall-clock budget.

The verification sub-agent's iteration count and residual-finding count are written to `state/run_log.json` (`verification_iterations`, `verification_residual_count`) so the Operations dashboard at `/ops/` surfaces editorial signal across runs.

---

## Operator review pattern

Periodically (e.g. weekly), a human operator reviews:

- `git log -- sources/sources.json` to see what got demoted, what was proposed as `candidate`. Promote candidates the operator trusts; revert demotions if the source recovered.
- Section 8 (Verification Notes) of recent briefs to spot recurring single-source patterns or repeated drops, which may indicate a missing source or a quality issue with an existing one.
- Aggregate coverage in `state/covered_items.json` to spot blind spots — categories of threat consistently missing.
