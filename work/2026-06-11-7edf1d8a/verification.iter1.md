**Model:** Anthropic Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-06-11T04:34:57Z · ended_at=2026-06-11T04:38:38Z · duration_seconds=221
**Self-telemetry:** urls_checked=15 · webfetch_calls=15 · bridge_fetches=3 · websearch_calls=1

## Verification report — briefs/2026-06-11.md (iteration 1)

Cold read, all inline source URLs fetched (15 WebFetch + 3 bridge fetches of NCSC-CH SPA hash routes + 1 WebSearch to disambiguate "GreatXML"). Mechanical gate passed pre-spawn. Two truth-class findings; no broken/generic URLs; no editorial-drop findings.

### Citation does not support the claim

- **F3 — § 1, RoguePlanet item.** Claim quoted: "NCSC-CH GovCERT consolidated this and a follow-on BitLocker-bypass disclosure (\"GreatXML\") alongside the researcher's prior 2026 Defender drops" (line 27). The cited NCSC-CH GovCERT post 12622 was fully retrieved via `tools/fetch_source.py ncsc-csh post 12622`; its content names YellowKey (CVE-2026-45585), GreenPlasma (CVE-2026-50507), RoguePlanet (CVE TBD), and references prior BlueHammer/RedSun/UnDefend (April) and YellowKey/greenplasma (May). It does **not** mention "GreatXML" anywhere. Neither BleepingComputer nor SecurityWeek (the item's other cited sources) names GreatXML either (SecurityWeek lists MiniPlasma, not GreatXML). A targeted WebSearch confirms GreatXML is a *real* Nightmare-Eclipse-adjacent BitLocker-bypass codename (OffSeq Threat Radar lists it), so the entity is not hallucinated — but the specific attribution "NCSC-CH GovCERT consolidated ... GreatXML" is unsupported by any source cited on this item. Fix: either drop the GreatXML clause, or cite a source that actually consolidates it, or reword so the claim about what NCSC consolidated matches post 12622 (which consolidates YellowKey/GreenPlasma/RoguePlanet, not GreatXML).

### Quantifier without source

- **F14 — § 1, ServiceNow item.** Claim quoted: "Anomalous activity was observed from 2–3 June — **roughly five API requests per tenant from a single source IP** — and ServiceNow applied a server-side fix to hosted instances on 5 June" ([The Hacker News, 2026-06-10], line 19). The "roughly five API requests per tenant" quantifier is in none of the four cited sources, all fetched this iteration:
  - The Hacker News (cited for this sentence): does not contain a per-tenant request count; gives the window as "June 2-4".
  - BleepingComputer: "does not specify a number of API requests per tenant or instance." It *does* support the "single source IP" element (IP 51.159.98.241 shared by admins as an IOC).
  - TechCrunch / NCSC-CH GovCERT 12621: no such number.
  The "single source IP" half is supported; the numeric "roughly five API requests per tenant" is invented specificity. Secondary note: the brief's "2–3 June" window is narrower than THN's "June 2-4" — recommend aligning to the sourced window. Fix: drop "roughly five API requests per tenant" (or attribute it to a source that states it), and reconcile the date window to "2–4 June".

### Items checked and cleared (no finding — recorded for audit)

- **CVE mappings YellowKey/CVE-2026-45585 + GreenPlasma/CVE-2026-50507 (§ 1 RoguePlanet):** SecurityWeek garbles these (associates 45586 w/ GreenPlasma, 50507 w/ YellowKey) but NCSC-CH GovCERT post 12622 — a HIGH-reliability national-CERT primary cited on the item — states YellowKey=CVE-2026-45585 and GreenPlasma=CVE-2026-50507 verbatim. Brief follows the authoritative source. CORRECT. (Minor source contradiction already implicitly handled; not worth a § 7 line.)
- **CrowdStrike axios npm claim (§ 3):** CrowdStrike source confirms "STARDUST CHOLLIMA compromised the Axios npm package, downloaded 100 million times per week" — DPRK-nexus, consistent with brief's "DPRK-linked". Correctly flagged [SINGLE-SOURCE] + § 7 single-source line. National-CERT carve-out N/A. CLEARED.
- **ServiceNow Actively-Exploited vs bug-bounty framings (§ 1):** NCSC 12621 records "Actively Exploited"; TechCrunch + BleepingComputer carry ServiceNow's "likely security researchers / bug bounty" read. Brief presents both without overstating either. CORRECT per § 7 attribution caveat.
- **Langflow patch contradiction (§ 2 / § 7):** BleepingComputer + Tenable confirm patch available (1.9.0 / langflow-base 0.8.3 / 1.10.0 on 10 June). CVSS 8.8 + CWE-22 absent from BleepingComputer but confirmed verbatim in cited Tenable TRA-2026-26 (CVSS:3 AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H). § 7 contradiction line is accurate. CLEARED.
- **Netlogon CVE-2026-41089 (§ 4):** CERT-EU 2026-007 confirms CVSS 9.8, all patched build numbers verbatim, CCB Belgium ITW attribution, May 2026 Patch Tuesday. BleepingComputer corroborates. CLEARED. (BleepingComputer page may carry a June-1 original date vs brief's 2026-06-10 cite — summariser-derived, content fully supports; not flagged.)
- **JDY botnet (§ 3):** Lumen + THN confirm 1,500+ bots, ~650 Jan-2024 baseline, Volt-Typhoon/China-nexus, KV-botnet survival, device brands (THN explicitly lists Cisco/Araknis/Mimosa/Ubiquiti/Draytek/Hikvision/Linksys — matches brief), Platypus, Tor C2, CVE-2026-35616 Fortinet-scan-spike. CLEARED.
- **PeopleSoft deep dive (§ 5):** BleepingComputer confirms ~300 instances / 100+ orgs / higher-ed skew / psoft·oracle·linuxadm SSH accounts / ransom notes; Nottingham confirms student+alumni data accessed (does not name PeopleSoft/ShinyHunters, and brief does not claim it does); TechCrunch corroborates scale. No IOCs leaked despite sources carrying IPs/TLS-cert/ransom-note filename — policy honoured. CLEARED.
- **EDPB item (§ 1):** EDPB news + template pages + CNIL all resolve to specific articles dated 10 June 2026; 5 Aug 2026 consultation deadline confirmed verbatim. CLEARED.
- **NCSC-CH SPA hash routes (#/posts/12621, /12622):** confirmed legitimate GovCERT primaries via bridge; content retrieved. Not generic-URL findings.
- **Drops (§ 7):** FortiSandbox CVE-2026-25089 (no inclusion gate cleared; PSIRT page unavailable) — defensible. EVERTEC/Banco Popular 8-K (no CH/EU/public-sector nexus) — defensible. BACS G7-Évian (already covered campaign:g7-evian-2026, outside window) — defensible.

### Soft observation (not a finding)

- § 3 CrowdStrike: brief says report "frames AI/ML development pipelines and model weights as espionage targets". The CrowdStrike summariser confirmed AI as a "high-value target" but hedged on "model weights/ML pipelines" specifically. The brief's adjacent specifics (training data, ML infrastructure, semiconductor IP) are within the report's scope and the core claim is sound; below the threshold for a finding given the summariser's own uncertainty.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 0)

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "RoguePlanet Microsoft Defender zero-day"
  url_or_quote: "NCSC-CH GovCERT consolidated this and a follow-on BitLocker-bypass disclosure (\"GreatXML\")"
  summary: "Cited NCSC-CH GovCERT post 12622 (fully retrieved via bridge) names YellowKey/GreenPlasma/RoguePlanet + prior BlueHammer/RedSun/UnDefend but does NOT mention GreatXML; neither BleepingComputer nor SecurityWeek (item's other cited sources) names it. GreatXML is a real Nightmare-Eclipse codename (per WebSearch) but the attribution to NCSC is unsupported. Drop the GreatXML clause or cite a source that consolidates it."
- code: F14
  category: quantifier-without-source
  section: active-threats
  item: "ServiceNow unauthenticated REST endpoint"
  url_or_quote: "roughly five API requests per tenant from a single source IP"
  summary: "Quantifier 'roughly five API requests per tenant' is in none of the four cited sources (THN, BleepingComputer, TechCrunch, NCSC 12621); THN summariser explicitly lacks it and BleepingComputer 'does not specify a number'. Single-source-IP half IS supported (BleepingComputer IOC). Secondary: brief's '2-3 June' window narrower than THN's 'June 2-4'. Drop the per-tenant request count and align the window to 2-4 June."
```
