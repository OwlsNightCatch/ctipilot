**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-05-19T05:09:48Z · ended_at=2026-05-19T05:12:49Z · duration_seconds=181
**Self-telemetry:** urls_checked=14 · webfetch_calls=10 · bridge_fetches=0

## Verification report — briefs/2026-05-19.md (iteration 4)

### Prior-iteration delta verification

This is an even iteration (iter 4), so I received the prior-iteration deltas block and walked each remediation before my cold truth pass.

**F1 (iter3) — n8n patch versions for CVEs -44789/-44790/-44791:** Fetched GHSA-c8xv-5998-g76h, GHSA-57g9-58c2-xjg3, GHSA-wrwr-h859-xh2r directly. All three advisories confirm patches at 1.123.43 / 2.20.7 / 2.22.1. The brief's CVE Summary Table and §5 deep dive now correctly split: `-42231`/`-42232` → 1.123.32/2.17.4/2.18.1; `-44789`/`-44790`/`-44791` → 1.123.43/2.20.7/2.22.1. **F1 remediation: confirmed correct.**

**F2 (iter3) — GHSA-to-CVE mapping and per-CVE descriptions:** Fetched all three GHSA pages. Confirmed mappings: CVE-2026-44789=GHSA-c8xv-5998-g76h ("HTTP Request Node Pagination Prototype Pollution to RCE"); CVE-2026-44790=GHSA-57g9-58c2-xjg3 ("Arbitrary File Read via Git Node" — CWE-88, argument injection, not SSH RCE chain); CVE-2026-44791=GHSA-wrwr-h859-xh2r ("XML Node Prototype Pollution Patch Bypass"). The brief's §5 deep dive and §2 body now correctly reflect these descriptions. **F2 remediation: confirmed correct.**

**F3 (iter3) — Datadog analysis date:** The TL;DR bullet (line 14) now correctly reads "Datadog Security Labs analysed on 2026-05-13." HOWEVER, the §4 UPDATE body (line 90) still reads "Datadog Security Labs' **2026-05-15** analysis of the leaked Shai-Hulud worm source code." The 2026-05-15 brief confirms the Datadog date is 2026-05-13 (the UPDATE heading on that brief reads "UPDATE: Datadog Security Labs analyzes ... 2026-05-13"). **F3 remediation: INCOMPLETE — TL;DR fixed but §4 body still carries the wrong date.**

**F4 (iter3) — chalk-tempalte key descriptor (public/private):** The brief now says "new attacker private key" (§4 body, line 90). I fetched both cited primary sources:
- OX Security (primary discoverer, 2026-05-17): states "a public key embedded inside the code"
- The Hacker News (2026-05-18): states "its own C2 server and private key"

These two sources directly contradict each other. The iter3 finding said "Both cited sources say 'private key'" — but this is incorrect: OX Security says "public key." The iter3 remediation chose to apply "private key" (per THN). Since the two sources conflict, the brief must either (a) attribute the "private key" claim specifically to THN, noting OX Security says "public key," or (b) surface this as a `Contradiction:` in § 7. **F4 remediation: partially applied but source contradiction not surfaced — new F9 finding.**

**F13 (iter3) — INTERPOL "first-of-its-kind":** Fetched the INTERPOL press release and THN article. Both confirm "first-of-its-kind" refers to the operation as a whole ("the first cyber operation of its scale coordinated by INTERPOL in the MENA region"), not to the Algerian PhaaS takedown specifically. The brief now says "described as the first cyber operation of its scale coordinated by INTERPOL specifically targeting the MENA region" — this is accurate. The TL;DR heading and §1 body no longer apply the "first" label to the Algerian PhaaS component. **F13 remediation: confirmed correct.**

**F14 (iter3) — ARWINI 11M GKV quantifier:** Fetched Ärzteblatt and Borns IT Blog. Neither mentions 11 million patients. The brief now says "statutory-health-insurance (GKV) patients in Lower Saxony" (TL;DR) and "≥70,000 patients" (body). Ärzteblatt cites "70,000 datasets"; Borns IT Blog cites "up to 80,000"; Heise says "up to 75,000." The "≥70,000" figure is the conservative floor from the Ärzteblatt source — accurate and within the range confirmed by all three sources. **F14 remediation: confirmed correct.**

**F11 (iter3) — Grafana technical-mechanism framing:** The §4 UPDATE now explicitly marks the technical-mechanism block as "previously reported in the 2026-W21 weekly summary citing THN's earlier coverage." The SecurityWeek 2026-05-18 article confirms it only states "compromised token" — no mechanism detail. The THN prior coverage link is cited. **F11 remediation: confirmed correct.**

---

### Hallucinated / incorrect facts

**F3-RESIDUAL — §4 TeamPCP/Shai-Hulud UPDATE: Datadog date still wrong in body text**

The §4 UPDATE body (line 90) reads: "Datadog Security Labs' **2026-05-15** analysis of the leaked Shai-Hulud worm source code."

The correct date is 2026-05-13, confirmed by:
- The 2026-05-15 brief (UPDATE heading: "UPDATE: Datadog Security Labs analyzes ... 2026-05-13"; source footer: "Datadog Security Labs, 2026-05-13")
- The TL;DR bullet in the current brief (line 14) was already corrected to 2026-05-13

The TL;DR fix and the §4 body diverge. The body still carries the original incorrect date. This is a hallucinated-fact residual from iter3 F3.

---

### Surface contradiction

**F9 — OX Security vs The Hacker News: "public key" vs "private key" in chalk-tempalte**

The brief states (§4 body, line 90): "`chalk-tempalte` is a near-unmodified clone of the leaked Shai-Hulud worm with a modified C2 server and a new attacker **private key**"

Two sources are cited for this item:
- **OX Security** (primary discoverer, 2026-05-17): "a **public key embedded inside the code**" — this is the cryptographic public key of the attacker's keypair
- **The Hacker News** (2026-05-18): "its own C2 server and **private key**"

These directly contradict each other on which half of the keypair is embedded in the malware. The brief currently adopts the THN wording without flagging the discrepancy. A § 7 `Contradiction:` line is needed, and the claim should be attributed specifically to THN rather than stated as fact.

---

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 0)

- F3-RESIDUAL (hallucinated-fact): §4 body still says "2026-05-15" for Datadog analysis date; TL;DR correctly says "2026-05-13"
- F9 (surface-contradiction): OX Security says "public key", THN says "private key"; brief adopts one without surfacing the disagreement

---

### Findings summary (machine-readable)

```yaml
- code: F3
  category: hallucinated-fact
  section: updates-to-prior-coverage
  item: "§ 4 TeamPCP/Shai-Hulud UPDATE — Datadog analysis date in body text"
  url_or_quote: "Datadog Security Labs' 2026-05-15 analysis of the leaked Shai-Hulud worm source code"
  summary: "§4 body (line 90) still reads '2026-05-15'; TL;DR (line 14) was correctly changed to '2026-05-13'. Correct date per 2026-05-15.md UPDATE heading and source footer is 2026-05-13. F3 fix from iter3 only applied to TL;DR, not the §4 body."

- code: F9
  category: surface-contradiction
  section: updates-to-prior-coverage
  item: "§ 4 TeamPCP/Shai-Hulud UPDATE — chalk-tempalte key type (public vs private)"
  url_or_quote: "a new attacker private key"
  summary: "OX Security (primary discoverer, https://www.ox.security/blog/new-actors-deploy-shai-hulud-clones-teampcp-copycats-are-here/) states 'a public key embedded inside the code'; The Hacker News (https://thehackernews.com/2026/05/four-malicious-npm-packages-deliver.html) states 'private key'. Brief adopts THN wording without surfacing the contradiction. Add Contradiction: line to § 7, or attribute specifically to THN."
```
