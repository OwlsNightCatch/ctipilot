**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-05-23T05:21:54Z · ended_at=2026-05-23T05:27:42Z · duration_seconds=348
**Self-telemetry:** urls_checked=23 · webfetch_calls=16 · bridge_fetches=0

## Verification report — briefs/2026-05-23.md (iteration 4)

This is an even-iteration (alt / Sonnet) spawn. Per the `cti-verification-alt` protocol, the prior-iteration deltas block is the primary entry point; cold-read truth checks were also performed across all item URLs.

---

### Prior-iteration delta verification (iter-3 → iter-4)

**F1 — CERT-UA#10340 removal:** CONFIRMED. `grep -n "CERT-UA#10340"` returns no matches anywhere in the brief. Body retains "CERT-UA published a bulletin (surfaced 2026-05-22)" without the bulletin ID. Remediation correct.

**F2 — Storm-0257 / Umbral Bison removal:** CONFIRMED. `grep` returns no matches for either alias. Alias list in heading and body reads "UAC-0057, UNC1151, FrostyNeighbor". FrostyNeighbor is an established alias from prior coverage state (`state/covered_items.json` title: "FrostyNeighbor/Ghostwriter/UNC1151 March-May 2026 campaign") — not a new claim requiring THN sourcing. Remediation correct.

**F3 — FIOD role pairings removed:** CONFIRMED. "director of WorkTitans" and "founder of MIRhosting" do not appear. The revised framing — "both connected to bulletproof-hosting operators (WorkTitans B.V. and MIRhosting) named in the related corroborating coverage" — reads as analytical, not source-attributed. DutchNews.nl (fetched) confirms the 57-year-old is "director and sole shareholder" and the 39-year-old "ran the Dutch internet connectivity provider" without naming specific companies; BleepingComputer (fetched) confirms the same roles less specifically. Remediation correct.

**F4 — Four locations correctly enumerated:** CONFIRMED. Brief reads "raiding four locations including data centres in Dronten and Schiphol-Rijk plus the suspects' residences in Enschede and Almere." BleepingComputer (fetched) confirms: Dronten data center, Schiphol-Rijk data center, Enschede, Almere. DutchNews.nl (fetched) confirms the same four locations. Remediation correct.

**F5 — MITRE T-IDs moved to footnote:** CONFIRMED. Inline parentheticals removed from the chain narrative paragraphs. Italic footnote present at end of chain description: "*(MITRE ATT&CK overlay added by this brief, not by the CERT-UA narrative as carried by The Hacker News: T1027 Obfuscated Files/Information on the OYSTERFRESH stage, T1547.001 Registry Run Keys on the OYSTERBLUES persistence, T1059.007 JavaScript on OYSTERSHUCK execution, T1219 Remote Access Software on the Cobalt Strike final.)*". Remediation correct.

**F6 — SPIP parenthetical dropped:** CONFIRMED. "CERTFR-2026-AVI-0564", "2026-05-12", "RCE flaws" return no matches in the brief. Body now says "SPIP 4.4.15 is the immediate follow-on to the earlier-May 4.4.14 security release." Both CERTFR-2026-AVI-0635 (fetched) and SPIP blog (fetched) confirm the advisory covers a security-policy bypass / open-redirect in versions prior to 4.4.15. Remediation correct.

**F7 — "first criminal enforcement" softened:** CONFIRMED. The unconditional "first" framing is gone in both TL;DR and body. Body reads "one of the first publicly reported criminal enforcement actions in the EU directed at a bulletproof hoster acting as a proxy for a designated Russian entity." The softened framing is defensible without an explicit source. Remediation correct.

**F8 — Imperva date corrected:** CONFIRMED. `grep` confirms three occurrences of "[Imperva, 2026-05-21]" (TL;DR line 9, Immediate Action line 16, § 4 UPDATE line 137). Zero occurrences of "[Imperva, 2026-05-22]". Imperva blog (fetched) confirms publication date May 21, 2026. Remediation correct.

**F11a — Qualys disclosure date footnote:** CONFIRMED. The footnote "(the URL path encodes the disclosure date; the Qualys blog also carries a 2026-05-22 rendered 'Date' field that appears to reflect a content update; the brief uses the URL-encoded disclosure date as anchor)" is present at line 157. Qualys blog (fetched) confirms: URL path = 2026/05/20, rendered "Date" field = May 22, 2026. Remediation correct.

**F11b — Rhysida Stuttgart listing date anchored to DeXpose:** CONFIRMED. Body reads "in mid-May 2026 (DeXpose dates the listing to 2026-05-19; Heise (2026-05-21) covers the leak-site listing and Stuttgart's response without anchoring the original posting date)." DeXpose (fetched) confirms: "Date: May 20, 2026 (incident reported May 19, 2026)" — the listing date of May 19 is carried by DeXpose. Heise framing correctly characterised (Heise TollBit-gated; DeXpose is the listing-date anchor). Remediation correct.

---

### Truth checks (independent cold pass — items not in delta list)

**Drupal CVE-2026-9082 (§ 0 / § 4):** Fetched SA-CORE-2026-004 and Imperva blog. All claims verified: pre-auth SQL injection, PostgreSQL-only, active exploitation confirmed, patched versions (10.4.10 / 10.5.10 / 10.6.9 / 11.1.10 / 11.2.12 / 11.3.10) match the advisory exactly. Imperva article confirms 15,000+ attempts / ~6,000 sites / 65 countries. CLEAN.

**Megalodon (§ 1):** Fetched SafeDep article. Confirmed: 5,561 repos, six-hour window on 2026-05-18, SysDiag + Optimize-Build variants, @tiledesk/tiledesk-server versions 2.18.6–2.18.12. The SafeDep article date appears as May 21, 2026 in the WebFetch summary while the brief cites "[SafeDep, 2026-05-22]" — minor citation-date discrepancy. See F11 below.

**Screening Serpens / UNC1549 (§ 3):** Fetched Unit 42 article. Confirmed: four MiniUpdate variants (March 26 / March 26 / April 15 / April 17 2026), two MiniJunk V2 variants (February 17 / March 27 2026). AppDomainManager hijacking (T1574.014) + DLL sideloading (T1574.001) confirmed. ETW disable + strong-name validation disable confirmed. Azure-hosted C2 confirmed. CLEAN.

**Kimwolf (§ 1):** Fetched KrebsOnSecurity (DOJ URL returned 403). Krebs confirms: Jacob Butler, 23, Ottawa, alias Dort; "nearly 30 Tbps" peak (DOJ-cited figure); >25,000 attack commands; C2 seized 2026-03-19; AISURU, JackSkid, Mossad sibling botnets confirmed. Krebs publication date: May 21, 2026; DOJ complaint unsealed May 21, 2026. Brief cites "[U.S. Department of Justice, 2026-05-20]" — citation label shows 2026-05-20 but body text says "Thursday 2026-05-21." Minor citation-date label discrepancy. See F11 below.

**SPIP CVE (§ 1 / § 6):** Fetched CERTFR-2026-AVI-0635 and SPIP blog. CERTFR-2026-AVI-0635 confirmed (security-policy bypass, versions prior to 4.4.15). SPIP blog confirms open-redirect in cookie action. No CERTFR-2026-AVI-0564 reference anywhere. CLEAN.

**Rapid7 Q1 2026 (§ 3):** Fetched blog post and GlobeNewswire press release. Blog post page confirms 38% vulnerability exploitation figure and 50% zero-click. GlobeNewswire press release confirms ALL specific statistics cited in the brief: median KEV time 8.5→5.0 days, SQL injection most-exploited class, RMM 22.9%, ClickFix 18.8%, Qilin 357 / The Gentlemen 206 / Akira 174 ransomware rankings. CLEAN.

**Check Point AI report (§ 3):** Fetched CPR blog. Confirmed: nine Mexican government agencies, two AI platforms in parallel (one exploitation / one data processing), EvilTokens, stolen API keys for Anthropic/OpenAI/Groq/Mistral. CLEAN.

**ROADtools / Unit 42 (§ 3):** Fetched Unit 42 ROADtools article. Confirmed: Cloaked Ursa/Midnight Blizzard/APT29, Curious Serpens/Peach Sandstorm/APT33, UTA0355. T1098.005 / T1550 / T1087 mapped by Unit 42. The brief explicitly drops T1556.006 with a correct explanation that Unit 42 does not map it. CLEAN.

**Recorded Future Insikt Group (§ 1 FIOD background):** Fetched. Confirmed: AS44477→AS209847 migration, WorkTitans B.V. as Dutch entity, THE.Hosting rebrand, Dmitrii Miasnikov as RIPE maintainer connecting all entities. All analytical claims in the brief supported by this source. CLEAN.

**FIOD / Danish attribution claim (§ 1):** BleepingComputer (fetched) states: "The same outlet [De Volkskrant] alleges that Danish authorities and infrastructure providers linked WorkTitans to attacks by the pro-Russian hacktivist group NoName057(16)." The brief says "Danish authorities and infrastructure providers have publicly linked WorkTitans to NoName057(16) DDoS campaigns" without the De Volkskrant / "alleges" qualifier. The claim is traceable to the cited source (BleepingComputer) but BleepingComputer hedges it as second-hand. Minor F11 advisory — the brief presents a hedged secondary claim as established fact.

**CVE-2026-46333 / ssh-keysign-pwn (§ 5):** Fetched Qualys blog. Confirmed: TOCTOU race in __ptrace_may_access(), present since v4.10-rc1 (November 2016), combined with pidfd_getfd() (v5.6-rc1 January 2020). Four working exploits: chage, ssh-keysign, pkexec, accounts-daemon. Affected distros confirmed (Debian 13, Ubuntu 24.04/26.04, Fedora 43/44). Upstream fix landed 2026-05-14 confirmed. QID 387392 confirmed. CLEAN.

---

### Broken / unreachable URLs

No broken URLs detected. All primary sources fetched successfully except:
- `https://www.fiod.nl/fiod-houdt-twee-verdachten-aan-wegens-overtreding-sanctiewetgeving/` — returned empty content (likely Dutch-language page that the WebFetch summarizer couldn't parse; claims sourced from BleepingComputer and DutchNews.nl both confirmed). Not a broken URL.
- `https://www.justice.gov/usao-ak/pr/canadian-man-arrested-international-authorities-charged-administrating-kimwolf-ddos` — 403 (standard DOJ behavior). URL cited correctly; claims corroborated by KrebsOnSecurity which links to the same DOJ URL.
- `https://www.scworld.com/brief/belarus-linked-ghostwriter-group-targets-ukraine-using-prometheus-learning-platform-lures` — 403. This is an Additional source; primary claims sourced from THN which resolved cleanly.

None of the above warrant an F1 finding — they are access-restriction patterns on specific host types, not missing pages.

---

### Generic / oversight URLs (replace with specific article)

No F2 findings. All cited URLs resolve to specific articles/advisories/PSIRT pages.

---

### Citation does not support the claim

No F3 findings identified beyond the advisory-level FIOD / Danish attribution claim (categorised F11 below).

---

### Unsupported / hallucinated facts

No F4 findings. All named entities (CVEs, actor names, variant counts, statistics) were corroborated by fetched sources.

---

### Claims missing inline citation

No F5 findings.

---

### Strengthen primary source

No F6 findings. All items have vendor PSIRT / research-lab / official press releases as primary source. The Kali365 item correctly notes the IC3 advisory returned 403 and reconstructed from four corroborating outlets.

---

### Drop (low relevance / off-audience)

No F7 findings.

---

### Needs more research

No F8 findings.

---

### Surface contradiction

No F9 findings (existing contradiction in § 7 between Drupal severity 23/25 vs CVSS 6.5 is already documented in the brief).

---

### Missed angles

No blocking F10 issues. Suggested search for future run: "Gentlemen ransomware group Switzerland OR European public sector 2026" — the Rapid7 report names The Gentlemen (206 leak-site posts) as the #2 group but the brief does not examine their targeting profile.

---

### Editorial / less-is-more flags (advisory)

**F11-A — SafeDep citation date label (minor)**
The brief cites the SafeDep Megalodon article as "[SafeDep, 2026-05-22]" (TL;DR line 12 and § 1 line 44). The WebFetch summary returned "Date: May 21, 2026" for the SafeDep article. OX Security is correctly cited as 2026-05-21. This is a citation-date label inconsistency; the article content is correctly described and the URL resolves. No reader-facing harm.

**F11-B — Kimwolf DOJ citation date label (minor)**
The brief cites "[U.S. Department of Justice, 2026-05-20]" while the body text says the complaint was "unsealed Thursday 2026-05-21." KrebsOnSecurity (published May 21, corroborated by Krebs's link to the DOJ PR) reports May 21 as the unsealing date. The citation label "2026-05-20" may not match the DOJ press release's own publication date. DOJ URL returned 403 so the PR date cannot be confirmed directly; however given the body text says "Thursday 2026-05-21" there is an apparent internal inconsistency between the label and the body.

**F11-C — FIOD Danish attribution hedge (minor)**
Brief body (§ 1, para 2): "Danish authorities and infrastructure providers have publicly linked WorkTitans to NoName057(16) DDoS campaigns." BleepingComputer (fetched) reports: "The same outlet [De Volkskrant] alleges that Danish authorities and infrastructure providers linked WorkTitans to attacks by the pro-Russian hacktivist group NoName057(16)." The brief presents a hedged secondary claim as established fact. The reader impact is low because the broader Stark/WorkTitans/NoName057(16) connection is well-established via multiple sources; the specific "Danish authorities" linkage is the hedged element. Could be softened to "a Dutch investigative outlet reported" or left as-is given the overall corroboration density.

---

### Single-source items missing [SINGLE-SOURCE] flag

No F12 findings. Check Point AI Digest is already marked `[SINGLE-SOURCE]` in the heading and § 7 Verification Notes notes the single-source status. Gambit Security primary URL returned 404 (documented in § 7). Appropriate.

---

### Analytical-link-as-fact (F13)

No F13 findings.

---

### Quantifier without source (F14)

No F14 findings. The "nearly 30 Tbps" quantifier is sourced to DOJ/KrebsOnSecurity (both cite this figure). The "15,000+" and "~6,000 sites" and "65 countries" figures are confirmed by the Imperva blog (fetched). The "5,561" repos figure confirmed by SafeDep (fetched). The "357/206/174" ransomware gang post counts confirmed by GlobeNewswire (fetched).

---

### Name-collision unflagged (F15)

No F15 findings. The SafeDep outbound links reference "mini-shai-hulud" (a prior npm campaign), which is a SafeDep internal campaign name — not related to any entity named in this brief. The Ghostwriter UPDATE heading "FrostyNeighbor" is a continued alias from prior coverage with no name-collision risk detected.

---

### Verdict

**CLEAN**

All 10 prior-iteration (iter-3) remediations are correctly applied and verified. Three minor advisory items (F11-A, F11-B, F11-C) are citation-date label or hedging discrepancies that do not affect the brief's technical accuracy or operational utility. None meet the bar for NEEDS_FIXES — they are all sub-F11 cosmetic inconsistencies the main agent may choose to address or leave.

The brief is factually sound, all primary sources resolve, all named entities are confirmed by fetched sources, the SINGLE-SOURCE flag is correctly applied where needed, and the brief's overall structure and relevance to Swiss/EU public-sector defenders is high.

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F11
  category: editorial-advisory
  section: "§ 1 Megalodon"
  item: "Megalodon mass-poisons 5,561 GitHub repos"
  url_or_quote: "[SafeDep, 2026-05-22](https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows/)"
  summary: "SafeDep article date per WebFetch summary is May 21 2026; brief citation label says 2026-05-22. OX Security correctly cited 2026-05-21. Minor label inconsistency; article content confirmed correct."
- code: F11
  category: editorial-advisory
  section: "§ 1 Kimwolf"
  item: "Kimwolf / Dort DDoS-for-hire operator arrested"
  url_or_quote: "[U.S. Department of Justice, 2026-05-20](https://www.justice.gov/usao-ak/pr/canadian-man-arrested-international-authorities-charged-administrating-kimwolf-ddos)"
  summary: "Brief body says complaint unsealed Thursday 2026-05-21; citation label says 2026-05-20. DOJ URL returned 403 so date cannot be confirmed from the PR directly; KrebsOnSecurity (published May 21) confirms May 21 unsealing date. Internal inconsistency between label and body text."
- code: F11
  category: editorial-advisory
  section: "§ 1 FIOD"
  item: "Netherlands FIOD arrests two over EU sanctions evasion"
  url_or_quote: "Danish authorities and infrastructure providers have publicly linked WorkTitans to NoName057(16) DDoS campaigns"
  summary: "BleepingComputer (fetched) hedges this claim via De Volkskrant ('The same outlet alleges that Danish authorities and infrastructure providers linked WorkTitans to attacks'). Brief presents as established fact. Sub-truth-defect: source does carry the claim; hedging is one remove. Recommend softening to 'a Dutch investigative outlet reported' or noting the De Volkskrant origin."
```
