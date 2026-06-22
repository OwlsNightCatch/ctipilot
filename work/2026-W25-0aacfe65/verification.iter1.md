**Model:** Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-21T23:32:07Z · ended_at=2026-06-21T23:39:04Z · duration_seconds=417
**Self-telemetry:** webfetch_calls=15 websearch_calls=0 bridge_fetches=0 urls_checked=15

## Verification report — briefs/weekly/2026-W25.md (iteration 1)

Cold read, weekly run. 41 H3 items across 12 sections. I WebFetched 15 cited Source URLs covering every § 1 Evidence-bearing item, every § 0 headline, all § 2 multi-day campaigns, the load-bearing § 6 research/actor items, both § 7 annual reports, both § 8 long-running items, and the § 9 G7/NoName item. Lower-priority § 3 vuln-roll-up entries and several § 4/§ 5 sector items were spot-checked via the prior-coverage trace rather than re-fetched (noted as sampling per the 30-min cap). All URLs fetched resolved to specific articles/advisories/research posts — no broken links, no homepage/listing/NVD-only Sources found (consistent with the pre-spawn mechanical gate). The defects below are truth-class misreadings of cited sources plus one quantifier-without-source and one advisory date discrepancy.

### Citation does not support the claim

**F3 — DORA § 7: "one-third third-party-driven" misreads the ESA "one-third cross-border" statistic.**
Brief (§ 7): "roughly **one-third traced back to third-party ICT providers** — empirical confirmation of the concentration-risk lens DORA was built around and a direct echo of this week's third-party-breach theme (§ 5)". Also § 0 bullet: "3,383 major incidents, a third third-party-driven".
Both cited primaries contradict this. EBA (https://www.eba.europa.eu/publications-and-media/press-releases/esas-publish-first-report-dora-major-ict-related-incidents) and EIOPA (https://www.eiopa.europa.eu/esas-publish-first-report-dora-major-ict-related-incidents-2026-06-03_en) both state the one-third figure is CROSS-BORDER IMPACT: "around one third of the 3,383 major incidents reported by financial entities in the EU ... had a cross-border impact". The reports mention third-party risk management as important but do NOT attribute one-third of incidents to third-party providers. This is the load-bearing analytical claim of the item (the entire "direct echo of this week's third-party theme" synthesis rests on it) and it also drives the § 0 headline. Truth defect — correct to "cross-border impact" and re-examine the third-party-theme tie-in.

### Unsupported / hallucinated facts

**F4 — Check Point § 7: "EU countries collectively account for ~20.7% of global victims" is not in the cited source.**
Brief (§ 7): "EU countries collectively account for ~20.7% of global victims". Check Point page (https://research.checkpoint.com/2026/the-state-of-ransomware-q1-2026/): the 20.7% figure refers ONLY to healthcare-sector targeting by the Genesis group, not EU-wide victim share. Not corroborated by the cited Emsisoft page either. The other Check Point figures on this item verify cleanly (71.1% top-10 concentration; Gentlemen +315%; LockBit 5.0 +106%; Switzerland — Akira 31%; 11 May publication date). Remove or correct the 20.7% claim.

**F4 — INC § 6: NHS Dumfries & Galloway and Alder Hey Children's Hospital "confirmed victims" not in any fetchable cited source.**
Brief (§ 6): "The European exposure is direct: NHS Dumfries & Galloway and Alder Hey Children's Hospital are confirmed victims". Cited THN page (https://thehackernews.com/2026/06/inc-ransomware-claims-830-victims-since.html) does NOT name either hospital. The cited Acronis page (https://www.acronis.com/.../the-evolution-of-inc-ransomware/) returns HTTP 403, and § 11 of the brief itself states Acronis content was "recovered via The Hacker News" — but THN carries neither victim. The "European exposure is direct" hook is therefore unsupported by any source I could fetch. Verify against a reachable primary or qualify/drop. (The 830+ victims, fourth-in-Q1, Rust rewrite, BYOVD drivers filwfp/filnk/fildds, Veeam dumper, Lynx/Sinobi variants all verify in THN.)

**F4 — SocGholish § 8: "1.4M compromised WordPress sites" not on the cited Proofpoint page.**
Brief (§ 8): "while law enforcement seized 106 servers and credentials for 1.4M compromised WordPress sites" (sourced to Proofpoint). The cited Proofpoint page (https://www.proofpoint.com/us/blog/threat-insight/sayonara-socgholish-operation-endgame-disrupts-major-cybercrime-operation) surfaces "over 100 servers" and "14,971 websites remediated" but not "1.4M compromised WordPress sites". The § 5 sibling attributes the 106-servers / 14,971-sites figures to Politie. The 1.4M figure has no support on the cited page — confirm against Politie/Proofpoint or qualify. (The five named persisting clusters — TA2726, TA2727, ZPHP, ErrTraffic, LandUpdate808/KongTuke — and the credential-reinfection point all verify on Proofpoint.)

### Claims missing inline citation

**F5 — INC § 6: "Germany ranks #2 globally for ransomware victims in Q1 2026" — true, but no citation on this item supports it.**
Brief (§ 6): "Germany ranks #2 globally for ransomware victims in Q1 2026". Cited THN page does not state it; cited Acronis page is 403/unverifiable. The claim is actually TRUE per the Emsisoft source (https://www.emsisoft.com/en/blog/47562/the-state-of-ransomware-in-q1-2026/ — "Germany moved into the #2 position" at 5.9%) — but Emsisoft is cited on the § 7 Check Point item, NOT on this § 6 INC item. Add the Emsisoft citation here or drop the figure. (Note: the same "Germany is the #2 country globally" sentence appears in § 7 where Emsisoft IS cited — that instance is supported; this § 6 instance is the orphaned one.)

### Quantifier without source

**F14 — Council of Europe "first European institution" (§ 0, § 2, § 4).**
Brief (§ 2): "the first European-institution victim named in the campaign"; echoed in § 0 and § 4. Neither cited source states this. SecurityWeek (https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/) does not state it is the first European institution; GTIG (https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit) does not either. The quantifier is an analytical claim carried from daily 06-16 ("the first European intergovernmental victim named in the 100+-organisation PeopleSoft campaign"). Either source the "first" quantifier or soften (e.g. "the first European institution publicly named in this repository's coverage of the campaign"). Lower severity — defensible as house analysis, but currently reads as a sourced fact.

### Editorial / less-is-more flags (advisory)

**F11 — GTIG ShinyHunters citation date (§ 2).**
Brief cites "[Google GTIG, 2026-06-17]" and refers to "GTIG's 17 June analysis". The fetched page reports publication 2026-06-11. WebFetch date extraction is not fully reliable, so confidence is low, but reconcile the date and the "17 June" framing against the page. All substantive claims (UNC6240 attribution, 27 May-9 June window, 100+ orgs notified, 68% higher education, JSP shell, MeshCentral-as-Azure, [victim]_fanout.sh, zstd exfil) fully verify. Advisory only — no action required if the date is confirmed correct.

### Notes on what verified cleanly (no action)

- **§ 1 all three Evidence-bearing items verify**: FortiBleed (86,644 creds / 194 countries, 45-GPU Hashtopolis cluster, SSL-VPN-intercept-to-AD pivot, Russian-speaking operator, both Evidence quotes verbatim in SecurityWeek); Splunk CVE-2026-20253 (CVSS 9.8 / CWE-306, limited exploitation June 2026, PostgreSQL-sidecar primitive, version ranges and fixes, both Evidence quotes verbatim in Splunk PSIRT); PTC Windchill CVE-2026-12569 (CVSS 3.1 10.0 / 4.0 9.3, pre-auth deserialization, backdoor-deployment + 2:30 AM BSI-call Evidence quotes verbatim in Heise).
- **§ 2 Klue/Icarus**: "Icarus" actor name and the python-urllib / /services/data/v59.0/query/ TTP verify in the cited Huntress page; "dormant/prototype-integration credential" is a fair paraphrase of Huntress "abandoned OAuth credential" / Klue "legacy credential". Note the ReliaQuest page (also cited) does NOT name Icarus — but Huntress carries it, so the attribution is sourced.
- **§ 6 AutoJack, Mastra/Sapphire Sleet, ErrTraffic, FishMonger** all verify in full against their cited primaries (Microsoft, Microsoft, Sekoia, ESET respectively), including the three-flaw AutoGen chain, Sapphire Sleet attribution + 140 packages/88 min + easy-day-js typosquat + tri-platform persistence, ErrTraffic Polygon-blockchain C2, and FishMonger RawWNPF.sys + BlackLotus/CVE-2023-24932 UEFI note + Honduras/Taiwan/Thailand/Pakistan victims.
- **§ 8 RoguePlanet CVE-2026-50656** verifies (TOCTOU/CWE-59, SYSTEM, fully-patched Win10/11 incl. June Patch Tuesday, RTP-irrelevant, fix-in-development-no-timeline). Help Net Security notes no in-the-wild exploitation, consistent with the brief's no-patch/post-access framing.
- **§ 9 G7/NoName Haute-Savoie** verifies (15 June, Évian/Thonon/Saint-Gingolph + EVA'D, temporary outages no data compromise, Telegram self-claim attribution — correctly flagged MEDIUM in § 11).
- **§ 7 Check Point** core figures verify (71.1%, +315%, +106%, Switzerland-Akira 31%, 11 May) — only the EU-20.7% claim (F4) fails.
- **HCRG (§ 4)** verifies (Feb 2025 Medusa attack, mid-2026 notification, >12-month gap) and is correctly [SINGLE-SOURCE]-flagged in § 11. **Kodak, Cisco SD-WAN CVE-2026-20262 (CVSS 6.5), DORA 3,383/10%-cyber** all verify.
- **Contradiction handling**: the PAN-OS CVE-2026-0257 Impacket-vs-Unit-42 nuance is correctly surfaced in § 11 and the § 3 item uses Unit 42's wording — no silent resolution. Good.

### W-PD-1 weekly-lens check

Every item I reviewed answers one of W-PD-1's three questions: § 1 (inaction = incident), § 2/§ 4/§ 5/§ 8 (cross-day patterns no single daily surfaced), § 6/§ 7/§ 9 (research / strategic-horizon). No pure one-to-one daily summaries detected; § 11 documents the dropped single-day items (Rokarolla, clipboard-hijacker, USB-LNK worm, Prinz Eugen) with W-PD-1 rationale. Coverage shape is sound. No F7 drops.

### Verdict

NEEDS_FIXES (truth: 4, editorial: 1, advisory: 1)

Truth = F3, F4(×3 counted as the three F4 records: Check Point EU-20.7%, INC NHS/Alder Hey, SocGholish 1.4M) + F14 → in the machine-readable block there are F3 (1), F4 (3), F14 (1) = 5 truth-class records; F5 (1) editorial; F11 (1) advisory. Counts line below reflects the YAML records.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: annual-periodic-reports
  item: "DORA Year 1 — the ESAs' first annual ICT-incident report (§ 7)"
  url_or_quote: "https://www.eba.europa.eu/publications-and-media/press-releases/esas-publish-first-report-dora-major-ict-related-incidents"
  summary: "Brief: 'roughly one-third traced back to third-party ICT providers'. EBA+EIOPA primaries say the one-third figure is CROSS-BORDER IMPACT, not third-party-provider-driven. Propagates to § 0 'a third third-party-driven' and the § 7 third-party-theme synthesis."
- code: F4
  category: hallucinated-fact
  section: annual-periodic-reports
  item: "Check Point State of Ransomware Q1 2026 (§ 7)"
  url_or_quote: "https://research.checkpoint.com/2026/the-state-of-ransomware-q1-2026/"
  summary: "Brief: 'EU countries collectively account for ~20.7% of global victims'. Check Point: 20.7% is healthcare-sector Genesis targeting, not EU-wide. Not in Emsisoft either. Remove/correct."
- code: F4
  category: hallucinated-fact
  section: research-threat-actor
  item: "INC ransomware confirmed European healthcare victims (§ 6)"
  url_or_quote: "Brief: 'NHS Dumfries & Galloway and Alder Hey Children's Hospital are confirmed victims'"
  summary: "Cited THN does not name them; cited Acronis is 403 and brief says recovered-via-THN which lacks them. Unsupported European-exposure hook. Verify or drop."
- code: F4
  category: hallucinated-fact
  section: long-running-campaigns
  item: "SocGholish / TA569 Operation Endgame status (§ 8)"
  url_or_quote: "Brief: 'seized 106 servers and credentials for 1.4M compromised WordPress sites' (cited Proofpoint)"
  summary: "Cited Proofpoint page has 'over 100 servers' and '14,971 websites remediated', not '1.4M compromised WordPress sites'. Confirm against Politie/Proofpoint or qualify."
- code: F5
  category: missing-citation
  section: research-threat-actor
  item: "INC ransomware Germany #2 (§ 6)"
  url_or_quote: "Brief: 'Germany ranks #2 globally for ransomware victims in Q1 2026'"
  summary: "True per Emsisoft (Germany #2, 5.9%) but Emsisoft is not cited on this item; cited THN/Acronis do not support it. Add Emsisoft citation or drop."
- code: F14
  category: quantifier-without-source
  section: multi-day-campaigns
  item: "ShinyHunters — Council of Europe (§ 0, § 2, § 4)"
  url_or_quote: "Brief: 'the first European-institution victim named in the campaign'"
  summary: "Cited SecurityWeek and GTIG do not state 'first'. Daily-originated analytical claim. Source the quantifier or soften. Low severity."
- code: F11
  category: editorial-advisory
  section: multi-day-campaigns
  item: "GTIG ShinyHunters citation date (§ 2)"
  url_or_quote: "Brief: '[Google GTIG, 2026-06-17]' / 'GTIG's 17 June analysis'"
  summary: "Fetched GTIG page reports 2026-06-11 publication. WebFetch date extraction unreliable; reconcile. Substance fully verifies. Advisory only."
```
