**Model:** Anthropic Claude Opus 4.8 (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-05-31T22:51:47Z · ended_at=2026-05-31T22:53:33Z · duration_seconds=106
**Self-telemetry:** webfetch_calls=8 · websearch_calls=0 · bridge_fetches=0 · urls_checked=8

## Verification report — briefs/weekly/2026-W22.md (iteration 3)

Cold read. Iteration 3 of a weekly summary that returned NEEDS_FIXES on iterations 1 and 2. Phase 4.5 mechanical gate (`check_brief.py`) already exits 0; standing transient WARNs (scworld 403 / sysdig 503 fetched 200 OK at run time, product-name name-collisions, quantifier-evidence) adjudicated acceptable in prior iterations and re-confirmed not regressed. Budget spent confirming the five iter-1/iter-2 remediations are accurate against re-fetched primaries, plus spot-checks of previously-unverified high-traffic claims.

### Remediation confirmation — all five landed correctly

1. **§8 German hackback (was iter-2 F3-A).** Brief now uses the government's general "their servers, their software and their strategy" framing and explicitly states "the announcement does not break the new powers down per agency in technical detail." Fetched https://www.bundesregierung.de/breg-en/news/strengthening-cyber-security-2433588 — page uses exactly that general framing ("target the attacker, their servers, their software and their strategy"), names BSI/BKA/Bundespolizei as gaining expanded authority without per-agency technical enumeration. The per-agency capability breakdown iter-2 flagged is gone. CONFIRMED. (Minor note: the EN page phrases the bill as "passed" cabinet; the brief correctly adds the Bundestag-passage-still-ahead qualifier from the DE source / daily — accurate, not a defect.)

2. **§6 ESET Sandworm (was iter-2 F3-B).** Brief now reads "a rare out-of-Ukraine Sandworm destructive incident (a medium-confidence December 2025 attack on a single Polish energy company)" and frames the Polish target as "notable precisely because the operator rarely acts destructively outside Ukraine." Fetched https://www.welivesecurity.com/en/eset-research/eset-apt-activity-report-q4-2025-q1-2026/ — report says "December 2025 data destruction incident affecting a Polish energy company, which we attribute to Sandworm with medium confidence" and "destructive attacks by Russia-aligned actors outside Ukraine remain rare." Single company, medium confidence, rarity — brief matches exactly. The earlier "Sandworm striking NATO energy targets" overstatement is removed. CONFIRMED. (Lazarus/DreamJob → European drone manufacturers and UNC5221/SPAWN/Ivanti also re-confirmed supported.)

3. **§3 table + §7 + §9 YellowKey/MiniPlasma relabel (was iter-2 F3-C / F11-A).** §3 row now reads "CVE-2026-45585 | Windows LPE (YellowKey, Chaotic Eclipse cluster)". §9 watch item separates "**YellowKey** (CVE-2026-45585), **GreenPlasma**, and **MiniPlasma** (CVE-2020-17103, the `cldflt.sys` Cloud Filter driver...)" — three distinct exploits no longer conflated under one CVE. §7 MiniPlasma H3 uses CVE-2020-17103 throughout (footer Region/CVE line `CVE-2020-17103`). Fetched https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more — confirms CVE-2026-45585 = YellowKey (no patch, no confirmed exploitation); BlueHammer/UnDefend/RedSun exploited; GreenPlasma/MiniPlasma have no CVE listed there. Fetched https://www.threatlocker.com/blog/miniplasma-windows-privilege-escalation-zero-day-affects-fully-patched-systems — confirms MiniPlasma = CVE-2020-17103 in cldflt.sys, SYSTEM on fully-patched Windows 11 May-2026 updates, researcher claims 2020 patch never applied or silently rolled back. Brief §7 H3 matches verbatim. CONFIRMED.

4. **§1 Samba dual-path config-dependence (was iter-2 F3-D, plus iter-1 4408 prereq).** Brief states CVE-2026-4408 reachable only where `check password script` (`%u`) configured and `samba-dcerpcd` runs as a service; CVE-2026-4480 reachable only where `%J` in print command, CUPS/IPP unaffected; both 10.0; both config-dependent (the "broader default-exposure" overstatement is gone). Fetched https://www.samba.org/samba/security/CVE-2026-4480.html — "Print servers configured with 'printing = cups' or 'printing = iprint', and print servers that do not have the %J substitution character in the 'print command' setting are not affected." Fetched https://www.samba.org/samba/security/CVE-2026-4408.html — "Unauthenticated Remote Code Execution in Samba DCE/RPC SAMR server", requires `check password script` with `%u` AND samba-dcerpcd as system service, CVSS 10.0. §3 table label "Samba (SAMR / printing)" is accurate. CONFIRMED.

5. **§7 Gentlemen APAC/LATAM concentration (was iter-2 F10).** Brief now reads "its victims concentrate in Thailand, Brazil and India (US ~13%), so the European and Swiss listings carried over from W21 run *against* its centre of gravity, which is precisely what makes a CH/EU hit worth surfacing." Fetched https://research.checkpoint.com/2026/the-state-of-ransomware-q1-2026/ — "Only 13.3% of its victims are based in the United States, compared to the ecosystem average of 49.6%"; Thailand 10.8%, Brazil 6.0%, India 4.2%; top-10 = 71.1%; Qilin #1 third quarter (338); Gentlemen #3 (166); LockBit comeback with Europe/LatAm shift. Brief §6 and §7 figures all match. CONFIRMED.

### Supplementary spot-checks (claims not deep-checked in iters 1–2)

- **§8 EU CRA milestone dates [SINGLE-SOURCE].** Fetched https://digital-strategy.ec.europa.eu/en/factpages/cyber-resilience-act-implementation — "11 June 2026 - Entry into application of the provisions on the notification of Conformity Assessment Bodies. Member States to designate notifying authorities" and "11 September 2026 - Entry into application of reporting obligations." Brief §8 dates and the SINGLE-SOURCE flag both correct. CONFIRMED.
- **§3 row 106 MSRC URL for CVE-2026-45585 (YellowKey).** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585 is a JS SPA that returns no static content to the fetcher (same class as the ec-presscorner / MSRC SPA limitation the brief already notes under coverage gaps). The URL resolves, is the correct canonical MSRC per-CVE page, and The Record's outbound-links list independently confirms it maps to YellowKey/CVE-2026-45585. NOT a broken-URL or citation defect — SPA render limitation only.

### Verdict

**CLEAN**

All five remediations from iterations 1–2 landed and are accurate against re-fetched primary sources. The iter-2 advisory F11-A (§9 three-exploit conflation) is resolved. Supplementary spot-checks of previously-unverified primaries (Samba 4408 SAMR prereqs, Check Point Gentlemen geography, MiniPlasma/CVE-2020-17103, CRA dates) all hold. No new truth or editorial defects surfaced. W-PD-1 satisfied across sections (§1 inaction-=-incident, §2 cross-day chains, §6/§8 strategic horizon). No IOCs, no vanity metrics in prose, English throughout, no workflow-internal leakage. The brief is ready to publish.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
[]
```
