**Model:** Anthropic Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-21T23:52:42Z · ended_at=2026-06-21T23:57:06Z · duration_seconds=264

## Verification report — briefs/weekly/2026-W25.md (iteration 3)

Read cold. WebFetched 14 cited primaries this pass (FortiBleed SecurityWeek, Splunk PSIRT, Heise PTC, Check Point Q1, EBA DORA, ReliaQuest Klue, Huntress Klue, SecurityWeek Council of Europe, Proofpoint SocGholish, Microsoft Mastra, Help Net RoguePlanet, ESET Gentlemen, Krebs Gentlemen, GTIG ShinyHunters, THN INC, EC NIS-transposition, Viktoria Compliance, Emsisoft, HCRG HIPAA Pulse). Bridge-fetched Acronis INC (JS-rendered, body not extractable). 403 (UA-blocked, not flagged as defects): Politie, EDPB, SEC iRhythm, Acronis body — these are mechanical-gate-validated URLs blocked to the automated UA; their claims rely on the daily backing / carve-out disclosure already in § 11.

Most numeric/named claims trace cleanly to cited primaries: FortiBleed (86,644 / 194 countries / Russian-speaking / 45-GPU Hashtopolis / AD pivot), Splunk CVE-2026-20253 (9.8/CWE-306/limited exploitation/affected+fixed versions), PTC CVE-2026-12569 (CVSS 10.0/9.3, 02:30 BSI call, backdoors), Check Point (71.1% / Gentlemen +315% / LockBit +106% / Switzerland Akira 31%), DORA (3,383 / one-third cross-border / ~10% cyber / "borderless and interconnected"), GTIG ShinyHunters (UNC6240 / 27 May–9 June zero-day / 100+ orgs 68% higher-ed / all TTPs), RoguePlanet (unpatched / TOCTOU CWE-59 / June PT build / "wait for a patch"), G7 Haute-Savoie DDoS (NoName057(16) / 15 June / named municipalities / EVA'D / Telegram), Krebs Gentlemen (36-yo Izhevsk / AI tooling), Mastra attribution (Sapphire Sleet/UNC1069/140+ packages/easy-day-js/persistence), Emsisoft Germany #2, Klue/Huntress (Icarus active since Apr 28 / victim list / python-urllib indicators). These are NOT defects.

### Citation does not support the claim

**F3 — INC ransomware geography/sectors contradict the cited THN primary.** Brief § 6 (line 228): "The group historically concentrates on **non-US targets** and counts healthcare, **education** and legal services among its primary sectors — a profile directly relevant to CH cantonal hospitals and universities." The cited The Hacker News primary (https://thehackernews.com/2026/06/inc-ransomware-claims-830-victims-since.html, fetched this pass) states the opposite: "Over 65% of victims are U.S. organizations" and lists primary sectors as "legal services, manufacturing, construction, technology, healthcare" — education is NOT named. The "non-US" framing is contradicted by the cited source and the CH-relevance hook ("CH cantonal hospitals and universities") leans on the incorrect non-US/education claim. The second cited source (Acronis TRU) is JS-rendered/403 to automated fetch and could not corroborate. Remediation: correct to "predominantly US-focused (65%+ of victims), with healthcare and legal services among its sectors" and re-anchor the CH-relevance line on the sector overlap (healthcare) rather than a non-US claim, OR cite a source that supports the non-US framing if one exists.

### Unsupported / hallucinated facts

**F4 — NIS2/CER referral: neither cited source supports the "CER Directive, seven Member States" headline.** Brief § 9 (line 282): "the Commission's 29 April CJEU referral of France and Spain was for failure to transpose the companion **CER Directive (EU 2022/2557)**, not NIS2 itself, and it named seven Member States in total (Bulgaria, France, Luxembourg, the Netherlands, Poland, Spain, Sweden)." Both cited sources fetched this pass fail to support it: the EC NIS-transposition tracker (https://digital-strategy.ec.europa.eu/en/policies/nis-transposition) describes a 7 May 2025 *reasoned opinion* to 19 Member States for NIS2 — no 29 April CER referral, no seven-state CER list. Viktoria Compliance (https://viktoria-compliance.eu/en/blog/nis2-transposition-status-eu-2026) "does not contain any reference to a 29 April 2026 CJEU referral concerning the CER Directive" and names no seven-state CER set. Additionally Viktoria says France's "final adoption now expected during the extraordinary session in July 2026," which contradicts the brief's claim that France's NIS2 vehicle is "absent from the 1 July extraordinary-session agenda." Remediation: either cite the specific EC press release / CJEU filing that states the 29 April CER referral + seven-state list, or downgrade to what the cited sources actually support (NIS2 transposition still incomplete across a large laggard set incl. France/Spain; France delayed). Reconcile the "absent from 1 July agenda" claim against the Viktoria "July extraordinary session" statement.

**F14 — Mastra "around 13 June" date contradicts the cited Microsoft primary and the brief's own text.** Brief § 6 (line 216): "rotate credentials on any host that pulled `@mastra` packages **around 13 June**." The same paragraph states the event was "first covered as an unattributed supply-chain event on **2026-06-18**" and cites Microsoft Security dated 2026-06-17. The Microsoft primary (fetched this pass) states the 140+ packages were published "within approximately 20 minutes (01:20 UTC June 17)" — i.e. 16–17 June, "not June 13." The "around 13 June" timing is unsupported and internally inconsistent. Remediation: change "around 13 June" to "around 16–17 June." (Context notes "Mastra timing" was remediated in a prior iteration; this is a residual instance of the same error.)

### Surface contradiction

**F9 — SocGholish cluster count: "five" (heading + § 6) contradicts "seven" (§ 8 body) and the cited Proofpoint primary.** § 8 heading (line 260): "Operation Endgame seized 106 servers, but **five** delivery clusters remain operational." § 8 body (line 262): "**seven** FakeUpdates-style clusters remain operational — TA2726, TA2727, ZPHP, ErrTraffic, LandUpdate808/KongTuke, GeoTDS and tdsshop" (seven names). § 6 (line 210): "ErrTraffic also surfaced as one of the **five** SocGholish-adjacent clusters still operating." The cited Proofpoint primary (https://www.proofpoint.com/us/blog/threat-insight/sayonara-socgholish-operation-endgame-disrupts-major-cybercrime-operation, fetched this pass) names "seven additional clusters beyond TA569" (the same seven listed in the body). "Five" is wrong in two places. Remediation: change "five" → "seven" in the § 8 heading (line 260) and in § 6 (line 210) to match the body and the Proofpoint source.

### Editorial / less-is-more flags (advisory)

**F11 — "The Gentlemen (Storm-2697)" designation not in either cited source.** § 2 heading (line 60) and § 7 reference label the group "Storm-2697." Neither the cited ESET nor Krebs primary (both fetched this pass) uses "Storm-2697" (ESET uses "Gentlemen"; Krebs uses "The Gentlemen"). "Storm-2697" is a Microsoft tracking name and plausibly carried from the 06-19 daily, but it is not supported by any source cited on this weekly item. Advisory only: either add a source that uses the Storm-2697 alias, or drop the parenthetical. Low severity — the alias is internally consistent and not contradicted, just uncited.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 1)

Truth findings F3 (citation-not-supported), F4 (unsupported fact), F14 (quantifier/date-without-source) — wait, recount below. Note: F9 is a surface-contradiction finding that also reflects a source mismatch ("five" not in Proofpoint). Per the return contract, F3+F4+F14 are truth-class; F9 is editorial (surface-contradiction, F9 category). F11 is advisory.

Recount for verdict line: truth = F3, F4, F14 = 3; editorial = F9 = 1; advisory = F11 = 1.

NEEDS_FIXES (truth: 3, editorial: 1, advisory: 1)

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: research-threat-actor
  item: "INC ransomware Rust rewrite and BYOVD evolution"
  url_or_quote: "\"concentrates on non-US targets and counts healthcare, education and legal services among its primary sectors\" — THN primary says 65%+ US, sectors are legal/manufacturing/construction/technology/healthcare (no education)"
  summary: "Cited The Hacker News primary contradicts the non-US framing (65%+ US) and does not list education; CH-relevance hook depends on the wrong claim. Correct to US-predominant and re-anchor CH relevance on healthcare sector overlap."
- code: F4
  category: hallucinated-fact
  section: policy-regulatory
  item: "NIS2 / CER enforcement — France/Spain referral"
  url_or_quote: "\"the Commission's 29 April CJEU referral of France and Spain was for failure to transpose the CER Directive... named seven Member States (Bulgaria, France, Luxembourg, the Netherlands, Poland, Spain, Sweden)\""
  summary: "Neither cited source (EC NIS-transposition tracker; Viktoria Compliance) supports the 29 April CER referral or the seven-state list. EC page describes a 7 May 2025 reasoned opinion to 19 states for NIS2. Viktoria also says France adoption expected July extraordinary session, contradicting the brief's 'absent from 1 July agenda'. Cite the actual CER-referral source or downgrade to supported claims and reconcile the July-session contradiction."
- code: F14
  category: quantifier-without-source
  section: research-threat-actor
  item: "DPRK Sapphire Sleet Mastra npm compromise"
  url_or_quote: "\"rotate credentials on any host that pulled @mastra packages around 13 June\""
  summary: "Microsoft primary dates package publication to 01:20 UTC June 17 (16-17 June); brief's own text says first covered 2026-06-18. 'Around 13 June' is unsupported and internally inconsistent. Change to 'around 16-17 June'. Residual of a previously-remediated Mastra timing error."
- code: F9
  category: surface-contradiction
  section: long-running-campaigns
  item: "SocGholish / TA569 — Operation Endgame status update"
  url_or_quote: "heading+§6 say 'five delivery clusters remain operational'; §8 body and Proofpoint primary say SEVEN (TA2726, TA2727, ZPHP, ErrTraffic, LandUpdate808/KongTuke, GeoTDS, tdsshop)"
  summary: "Cluster count 'five' in §8 heading (line 260) and §6 (line 210) contradicts the §8 body 'seven' and the cited Proofpoint primary (seven clusters beyond TA569). Change 'five' to 'seven' in both places."
- code: F11
  category: editorial-advisory
  section: multi-day-campaigns
  item: "The Gentlemen (Storm-2697)"
  url_or_quote: "\"The Gentlemen (Storm-2697)\" — neither cited ESET nor Krebs source uses the Storm-2697 alias"
  summary: "Storm-2697 (Microsoft tracking name) not present in either cited primary on this item; plausibly carried from the 06-19 daily. Advisory: add a source using the alias or drop the parenthetical. Not contradicted, just uncited."
```
