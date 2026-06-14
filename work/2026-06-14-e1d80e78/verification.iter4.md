**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-14T04:56:22Z · ended_at=2026-06-14T04:58:59Z · duration_seconds=157
**Self-telemetry:** urls_checked=17 · webfetch_calls=14 · bridge_fetches=1

## Verification report — briefs/2026-06-14.md (iteration 4)

### Prior-iteration delta verification (iter 3 / Opus 4.8 remediations)

**Delta F3 — Sekoia Signal/MotW framing:** VERIFIED CORRECT. The Sekoia page (fetched this iteration) states verbatim: "APT28 sends weaponised Office documents through private Signal Desktop chats, probably taking advantage of the fact that the client does not apply Mark-of-the-Web protection." The brief currently reads: "treat Office documents delivered through Signal Desktop as a Mark-of-the-Web bypass risk — Sekoia notes APT28 uses the messenger to deliver Office lures that arrive without the Mark-of-the-Web protection." This accurately paraphrases the source. No process-spawning claim remains anywhere in the brief.

**Delta F4 — Conti "indicted in 2023":** VERIFIED CORRECT. The DOJ mirror (globalsecurity.org) states: "In September 2023, an indictment charging four other Conti conspirators was unsealed in the Middle District of Tennessee." The brief states "Four other alleged Conti members were indicted in 2023." The phrase "remain at large" does not appear in the brief. Remediation confirmed good; no regression.

**Delta F14 — Ivanti "~40 hours":** VERIFIED CORRECT. The phrase "~40 hours" or "roughly 40 hours" does not appear anywhere in the brief. All references now use "shortly after the public PoC." The Security Affairs source and watchTowr/Splunk sources do not state any specific time figure. Remediation confirmed; no regression introduced.

---

### Broken / unreachable URLs

No broken or unreachable URLs found. All 17 URLs checked resolved to specific articles/advisories.

---

### Generic / oversight URLs (replace with specific article)

No generic URLs found. All source citations land on specific article or advisory pages.

---

### Citation does not support the claim

**F1.** Section § 2, item CVE-2026-10795 UpdraftPlus. The brief states: "Wordfence reports actively blocking exploitation attempts against this flaw in the wild — it is being weaponised, not theoretical."

The cited source is `malware.news/t/critical-unauthenticated-authentication-bypass-vulnerability-patched-in-updraftplus-wordpress-plugin/107751` (mirroring the Wordfence writeup). Fetched this iteration. The source states that Wordfence firewall rules were deployed to Premium/Care/Response users on June 3 as *preventive* protection, with free users receiving protection on July 3. **The source does not state that exploitation attempts were actively observed in the wild.** There is no language about active blocking of real-world attacks.

This same claim appears in the TL;DR (§ 0): "Wordfence reports active exploitation attempts in the wild" and in § 2 body: "Wordfence reports actively blocking exploitation attempts against this flaw in the wild — it is being weaponised, not theoretical."

The WPScan source (also cited) states the vulnerability status but does not mention active exploitation. Neither cited source supports the "actively exploited in the wild" characterisation.

**F2.** Section § 2 / § 5, Splunk CVE-2026-20253. The brief states in § 2: "Splunk-on-AWS is vulnerable out of the box" and attributes this claim to `advisory.splunk.com/advisories/SVD-2026-0603`. Fetched this iteration: the Splunk advisory says only "the PostgreSQL sidecar service endpoint lacks authentication controls" and lists affected versions 10.0.0–10.0.6 and 10.2.0–10.2.3. **It makes no mention of AWS deployment being vulnerable by default.**

The watchTowr Labs post (also cited) discusses AWS but does not explicitly state the sidecar is "enabled by default" on AWS vs. on-premises. The brief's § 5 paragraph refines this with "Splunk states that Splunk Enterprise on AWS is vulnerable in its default configuration because the PostgreSQL sidecar is enabled out of the box; on-premises Windows installs are exposed only where the sidecar has been explicitly enabled" — citing the Splunk advisory. The advisory does not make this AWS/on-premises distinction. This is a claim attributed to the advisory that the advisory does not contain.

Note: The watchTowr post may contain this AWS framing — the fetch showed Splunk Enterprise on AWS is mentioned, but specific language about "enabled by default on AWS" vs on-premises was not returned in the summary. The claim should be attributed to watchTowr, not the advisory, if watchTowr is the source.

---

### Unsupported / hallucinated facts

No additional hallucinated facts beyond F1 and F2 above.

---

### Claims missing inline citation

No claims missing inline citations found.

---

### Strengthen primary source

No NVD/CERT-only sourcing found. All primary sources are vendor advisories, research lab posts, or government filings.

---

### Drop (low relevance / off-audience / not weekly content)

No items recommended for drop. All items have clear Swiss/EU public-sector relevance or transferable defensive lessons.

---

### Needs more research

No items flagged. Technical depth is adequate across all items.

---

### Surface contradiction

No contradictions between cited sources.

---

### Missed angles

No missed angles. The § 7 notes appropriately log the intentional drops. Coverage shape is sound.

---

### Editorial / less-is-more flags (advisory)

No editorial advisory flags.

---

### Single-source items missing [SINGLE-SOURCE] flag

§ 3 APT28 item already carries the `[SINGLE-SOURCE]` flag and § 7 documents this. No drift found.

---

### Analytical-link-as-fact

No analytical-link-as-fact issues. All connections are attributed to named sources.

---

### Quantifier without source

The brief (§ 2, UpdraftPlus) states "3 million-plus active installations." Neither the WPScan advisory nor the Wordfence/malware.news writeup mention this specific figure in the fetched summaries. However, the UpdraftPlus WordPress.org plugin page lists active installs publicly, and this is a widely cited figure in the WordPress community. This is borderline — the cited sources don't explicitly state the figure, but it is verifiable from the WordPress.org plugin page. Given this is a well-known public figure rather than a brief-invented quantifier, this is advisory rather than a hard F14 finding.

---

### Name-collision unflagged

No name collisions found.

---

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 0)

**F1** (truth): The claim "Wordfence reports actively blocking exploitation attempts against this flaw in the wild" appears in the TL;DR and in § 2 body, but neither the WPScan source nor the Wordfence/malware.news source (both fetched this iteration) contain any statement about active in-the-wild exploitation. This is a material factual error that overstates the severity of CVE-2026-10795 exploitation status.

**F2** (truth): The claim "Splunk-on-AWS is vulnerable out of the box because the PostgreSQL sidecar is enabled by default" is attributed (via § 5 language) to the Splunk advisory SVD-2026-0603, but the advisory contains no AWS-specific language. The claim should be reattributed to watchTowr Labs or confirmed as present in the watchTowr source.

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: tl-dr-and-section-2
  item: "CVE-2026-10795 — UpdraftPlus WordPress backup plugin"
  url_or_quote: "Wordfence reports actively blocking exploitation attempts against this flaw in the wild — it is being weaponised, not theoretical."
  summary: "Neither the WPScan source (fetched: reports exploitation status but no active ITW claim) nor the Wordfence/malware.news source (fetched: describes preventive firewall rule deployment, not active blocking of ITW attacks) supports the 'actively blocking exploitation attempts in the wild' claim. The exploitation status should be downgraded or removed unless a source explicitly confirming ITW exploitation can be cited."
- code: F3
  category: claim-not-supported
  section: section-2-and-section-5
  item: "CVE-2026-20253 — Splunk Enterprise PostgreSQL sidecar"
  url_or_quote: "Splunk-on-AWS is vulnerable out of the box because the PostgreSQL sidecar is enabled by default"
  summary: "Splunk advisory SVD-2026-0603 (fetched this iteration) makes no mention of AWS deployment or the sidecar being enabled by default on AWS vs. on-premises. The claim appears in § 2 and § 5 attributed implicitly to the Splunk advisory. Either confirm the watchTowr post contains this language and reattribute to watchTowr, or remove the AWS-default-enabled specificity."
```
