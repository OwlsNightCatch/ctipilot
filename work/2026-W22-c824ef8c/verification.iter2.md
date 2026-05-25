**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`) — env vars CLAUDE_FRIENDLY_NAME / CLAUDE_MODEL_ID unset; identity from system context
**Timestamps:** started_at=2026-05-25T01:15:19Z · ended_at=2026-05-25T01:18:24Z · duration_seconds=185
**Self-telemetry:** webfetch_calls=10 · websearch_calls=0 · bridge_fetches=0 · urls_checked=10

## Verification report — briefs/weekly/2026-W22.md (iteration 2, Sonnet delta pass)

Cold read of the 2026-W22 weekly after iter-1 (Opus) applied 13 fixes. 10 cited URLs fetched via WebFetch. Iter-1 BLOCK fixes confirmed as applied; new truth defects found in the post-remediation text.

### Prior-iteration delta verification

All 13 iter-1 BLOCK fixes confirmed present:
- F4 hospital names: Cologne, Freiburg, Heidelberg, Tübingen, Ulm, Mannheim — CONFIRMED correct per The Record fetch.
- F3 Sparx exploitation reframe: § 0 bullet now reads "PoC-public; advisory body states no confirmed ITW" — CONFIRMED. § 1 heading now reads "CCB advisory title labels 'actively exploited'; advisory body states no confirmed exploitation" — CONFIRMED.
- F1 Cisco PSIRT URL: `cisco-sa-csw-pnbsa-g8WEnuy` — CONFIRMED resolves to CVE-2026-20223 CVSS 10.0 advisory.
- F1 n8n GHSA URL: `GHSA-q5f4-99jv-pgg5` — CONFIRMED resolves to CVE-2026-42231 prototype-pollution advisory.
- F2 vm2 GHSA: `GHSA-47x8-96vw-5wg6` — CONFIRMED resolves to CVE-2026-43997 sandbox-escape advisory.
- F3 Megalodon date reconciliation: § 1 now says "the CSA research note dates this wave to 2026-05-18" — CONFIRMED.
- F3 GitHub breach attribution: now attributed to GitHub Security Blog — CONFIRMED.
- F3 WebWorm Aquatic Panda removed — CONFIRMED; ESET page confirms Aquatic Panda not mentioned.
- F14 WebWorm reframed to "50+ reconnaissance targets" — CONFIRMED in § 0 and § 4.
- Europol "identified" — CONFIRMED in § 8.
- ChromaDB CVSS phrasing: now says "The reporting researcher published an initial CVSS of 4.0 (misjudging the scoring as 'network + auth required'); the actual attack surface is unauthenticated, network-accessible, giving an effective severity equivalent to CVSS 10.0" — CONFIRMED coherent.
- 13 [SINGLE-SOURCE] heading flags: verified present on all 13 items listed in iter-1 F12.
- German hospitals aggregator-only note: CONFIRMED in § 10.

New defects found below.

### Citation does not support the claim

**F1 — Researcher name "Chaotic Eclipse" is wrong; source says "Nightmare Eclipse".** § 1 CVE-2026-45585 deep-dive (line 44): "CVE-2026-45585 is a BitLocker security-feature bypass (CVSS 6.8; physical-access prerequisite) discovered by researcher **Chaotic Eclipse**." The cited Help Net Security source (`https://www.helpnetsecurity.com/2026/05/20/yellowkey-bitlocker-mitigation-cve-2026-45585/`) names the researcher as "**Nightmare Eclipse**" and links to GitHub repo `https://github.com/Nightmare-Eclipse/YellowKey`. "Chaotic Eclipse" does not appear in the source. Correct to "Nightmare Eclipse." Also: the § 7 long-running-campaigns item heading slug contains "chaotic-eclipse-zero-day" — a slug-level artefact of the wrong name.

**F2 — "Unit 42 and StepSecurity published a joint analysis" — StepSecurity not co-author.** § 1 Shai-Hulud deep-dive (line 24): "On 2026-05-22, **Unit 42 and StepSecurity** published a **joint analysis** confirming that SLSA Build Level 3 attestation does not constitute an integrity gate." The cited source (`https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/`) is sole-authored by Unit 42 (Palo Alto Networks). The article makes no mention of StepSecurity as co-author. The same false attribution appears in § 2 (line 94) and § 4 (line 204). Replace "Unit 42 and StepSecurity published a joint analysis" with "Unit 42 published an analysis" in all three locations.

**F3 — Drupal fixed version numbers are wrong.** § 1 CVE-2026-9082 hardening guidance (line 56): "upgrade to Drupal **≥ 10.3.14 / ≥ 11.1.6 / ≥ 11.2.3** immediately." The cited SA-CORE-2026-004 (`https://www.drupal.org/sa-core-2026-004`) lists fixed versions as: **10.4.10, 10.5.10, 10.6.9, 11.1.10, 11.2.12, 11.3.10**. The brief's version numbers (10.3.14, 11.1.6, 11.2.3) do not appear in the advisory and are incorrect. A defender applying the brief's version check would incorrectly conclude an unpatched system is patched. This is an operationally dangerous wrong-number defect.

**F4 — n8n fixed version "≥ 1.94.1" is wrong.** § 3 vulnerability roll-up table (line 152): "CVE-2026-42231 | n8n self-hosted automation < **1.94.1** | PoC-public | Patch-available (**≥ 1.94.1**) | No". The cited GHSA-q5f4-99jv-pgg5 (`https://github.com/n8n-io/n8n/security/advisories/GHSA-q5f4-99jv-pgg5`) states fixed in **>= 1.123.32, >= 2.18.1, and >= 2.17.4**. Version 1.94.1 is not mentioned in the advisory and is not the fix threshold. Replace with the actual fixed versions from GHSA.

**F5 — Cisco Secure Workload fixed version "prior to 3.11.1.12" is wrong.** § 3 deep-dive CVE-2026-20223 (line 162): "Affected versions include all Cisco Secure Workload releases **prior to 3.11.1.12**." The cited Cisco PSIRT advisory (`https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-csw-pnbsa-g8WEnuy`) lists the fixed releases as: **3.10.8.3** (for 3.10.x branch) and **4.0.3.17** (for 4.0.x branch); 3.9 and earlier must migrate to a fixed release. The advisory does not mention version 3.11.1.12 at all. The brief's version boundary is fabricated. Correct to reflect the advisory's actual fixed versions.

### Unsupported / hallucinated facts

**F6 — "Three public PoCs in circulation" for YellowKey not supported by source.** § 0 TL;DR bullet (line 11): "Three public PoCs in circulation" for CVE-2026-45585. § 1 "If you did nothing" callout (line 42): "Three public PoC implementations are available." The cited Help Net Security source names one PoC from Nightmare Eclipse and references other CVEs in the same disclosure blog post (BlueHammer, RedSun, UnDefend are listed as different CVEs, not YellowKey PoCs). No source confirms three distinct PoC implementations for CVE-2026-45585 specifically. Drop "Three" or reduce to "at least one public PoC" unless the daily brief provides the three-PoC source.

### Quantifier without source

**F7 — Megalodon open-source release attributed to 2026-05-23 but CSA source says 2026-05-12.** § 1 (line 24) and § 2 (line 96) say "By 2026-05-23, TeamPCP had released the full worm as **Megalodon** — an open-source toolkit." These passages attribute the open-source release date as 2026-05-23 to the daily brief. The CSA research note (the other cited source) states: "May 12, 2026 — open-source release" (not May 18 which is Wave 2 mass-poisoning). The current brief reconciles "CSA dates the wave to 2026-05-18" which is correct for the mass-poisoning, but does not address the CSA-stated open-source release date of May 12. The brief says TeamPCP "released the full worm as Megalodon — an open-source toolkit" on 2026-05-23, but the CSA source gives May 12 for the open-source release. This is a residual conflict the iter-1 fix did not fully resolve: the reconciliation note addresses the mass-poisoning date discrepancy but not the open-source release date discrepancy.

### Items confirmed clean (no finding)

- Iter-1 F4 fix (hospital names): Cologne, Freiburg, Heidelberg, Tübingen, Ulm, Mannheim confirmed per The Record fetch.
- CERT-EU TLR 2025 (174 actors, 7/9 incidents, agentic AI): all confirmed on cert.europa.eu.
- GitHub breach (~3,800 repos, initial access via Nx Console extension, published 2026-05-20): confirmed.
- WebWorm ESET: 50+ recon targets (56 dirsearch targets), 433+ messages (>400 Discord messages), FishMonger/SixLittleMonkeys confirmed; Aquatic Panda correctly absent.
- Cisco PSIRT URL: resolves and confirms CVE-2026-20223 CVSS 10.0, no workaround.
- n8n GHSA-q5f4-99jv-pgg5: resolves and confirms CVE-2026-42231.
- vm2 GHSA-47x8-96vw-5wg6: resolves and confirms CVE-2026-43997 (patched in 3.11.0; brief says "≥ 3.11.4" — minor version drift but 3.11.4 > 3.11.0 so the instruction is safe-but-wrong; flagged implicitly under F4 which the main agent should note; not a separate BLOCK finding as 3.11.4 is also ≥ 3.11.0).
- MSS prohibition 25 May 2026: confirmed by Greenberg Traurig. Swiss parallel date 22 May 2026 not mentioned in the GT source but the brief attributes the Swiss date separately.
- Drupal SA-CORE-2026-004: confirms CVE-2026-9082, pre-auth SQLi, PostgreSQL-only — technical claims correct; version numbers wrong (F3 above).
- CCB Belgium Sparx advisory: confirms body states "no proof of exploitation as of 2026-05-20"; title/body contradiction correctly preserved in brief.
- 13 [SINGLE-SOURCE] flags: all confirmed in headings.
- No IOCs (no hashes, IPs, attacker domains, rule code). English throughout. No workflow-internal language in published prose.

### Verdict

NEEDS_FIXES (truth: 6, editorial: 0, advisory: 0)

F1 (researcher name: Nightmare Eclipse, not Chaotic Eclipse), F2 (Unit 42 sole author, not joint with StepSecurity — appears 3×), F3 (Drupal fixed versions wrong — operationally dangerous), F4 (n8n fixed version wrong), F5 (Cisco CSW fixed version wrong), F6 (three YellowKey PoCs unsourced), F7 (Megalodon open-source release date conflict CSA May 12 vs brief May 23). All 7 items are truth-class; 0 editorial; 0 advisory.

Priority: F3 (Drupal version) is most operationally dangerous — wrong patch version will cause defenders to leave unpatched systems. F5 (Cisco CSW version) same issue. F1 (researcher name) and F2 (StepSecurity attribution) are credibility defects. F4 (n8n version) is a wrong patch check threshold. F6 and F7 are unsourced quantifier / date conflicts.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48 — iteration 2
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-45585 (YellowKey) — researcher name"
  url_or_quote: "CVE-2026-45585 is a BitLocker security-feature bypass ... discovered by researcher Chaotic Eclipse"
  summary: "Help Net Security source names researcher as 'Nightmare Eclipse' (github.com/Nightmare-Eclipse/YellowKey); 'Chaotic Eclipse' does not appear in the source. Same error in § 7 heading slug."

- code: F3
  category: claim-not-supported
  section: highest-impact-events
  item: "Shai-Hulud/Megalodon — Unit 42 and StepSecurity joint analysis"
  url_or_quote: "Unit 42 and StepSecurity published a joint analysis confirming that SLSA Build Level 3 attestation does not constitute an integrity gate"
  summary: "Unit 42 source (unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/) is sole-authored by Unit 42; no mention of StepSecurity as co-author. False attribution appears in § 1, § 2, and § 4."

- code: F3
  category: claim-not-supported
  section: highest-impact-events
  item: "Drupal SA-CORE-2026-004 / CVE-2026-9082 — fixed version numbers"
  url_or_quote: "upgrade to Drupal ≥ 10.3.14 / ≥ 11.1.6 / ≥ 11.2.3 immediately"
  summary: "SA-CORE-2026-004 (drupal.org/sa-core-2026-004) lists fixed versions as 10.4.10, 10.5.10, 10.6.9, 11.1.10, 11.2.12, 11.3.10. Version numbers in brief (10.3.14, 11.1.6, 11.2.3) are not in the advisory and are incorrect. Operationally dangerous wrong-version defect."

- code: F3
  category: claim-not-supported
  section: vulnerability-rollup
  item: "CVE-2026-42231 n8n — fixed version"
  url_or_quote: "n8n self-hosted automation < 1.94.1 | Patch-available (≥ 1.94.1)"
  summary: "GHSA-q5f4-99jv-pgg5 states fixed in >= 1.123.32, >= 2.18.1, >= 2.17.4. Version 1.94.1 not mentioned in advisory."

- code: F3
  category: claim-not-supported
  section: vulnerability-rollup
  item: "CVE-2026-20223 Cisco Secure Workload — affected version boundary"
  url_or_quote: "Affected versions include all Cisco Secure Workload releases prior to 3.11.1.12"
  summary: "Cisco PSIRT (cisco-sa-csw-pnbsa-g8WEnuy) states fixed releases are 3.10.8.3 (3.10.x) and 4.0.3.17 (4.0.x); 3.9 and earlier must migrate. Version 3.11.1.12 not mentioned. The version boundary in the brief is fabricated."

- code: F4
  category: hallucinated-fact
  section: week-at-a-glance
  item: "CVE-2026-45585 YellowKey — three public PoCs"
  url_or_quote: "Three public PoCs in circulation"
  summary: "Help Net Security source names one PoC from Nightmare Eclipse (github.com/Nightmare-Eclipse/YellowKey). References to BlueHammer/RedSun/UnDefend are different CVEs, not YellowKey PoCs. No source confirms three distinct CVE-2026-45585 PoC implementations."

- code: F14
  category: quantifier-without-source
  section: multi-day-campaigns
  item: "Megalodon open-source release date 2026-05-23"
  url_or_quote: "By 2026-05-23, TeamPCP had released the full worm as Megalodon — an open-source toolkit"
  summary: "CSA research note states 'May 12, 2026 — open-source release' (not May 18, which is Wave 2 mass-poisoning). Iter-1 fix reconciled the mass-poisoning date (May 18 CSA vs May 23 daily) but did not address the open-source release date conflict: CSA says May 12, brief says May 23. The brief should note CSA dates the open-source release to May 12."
```
