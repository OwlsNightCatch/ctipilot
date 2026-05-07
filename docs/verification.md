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

---

## Operator review pattern

Periodically (e.g. weekly), a human operator reviews:

- `git log -- sources/sources.json` to see what got demoted, what was proposed as `candidate`. Promote candidates the operator trusts; revert demotions if the source recovered.
- Section 8 (Verification Notes) of recent briefs to spot recurring single-source patterns or repeated drops, which may indicate a missing source or a quality issue with an existing one.
- Aggregate coverage in `state/covered_items.json` to spot blind spots — categories of threat consistently missing.
