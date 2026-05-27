**Model:** Anthropic Claude (specific model not determined; CLAUDE_FRIENDLY_NAME / CLAUDE_MODEL_ID unset in env — runtime context indicates Opus 4.7, model id `claude-opus-4-7[1m]`)
**Timestamps:** started_at=2026-05-27T04:39:34Z · ended_at=2026-05-27T04:43:24Z · duration_seconds=230

## Verification report — briefs/2026-05-27.md (iteration 1)

Cold read, iteration 1. Every inline source URL in the brief was fetched this iteration (WebFetch + the EUVD/CERT-FR bridge + one corroborating WebSearch). Mechanical gate (check_brief.py) already passed per spawn message; this pass is URL-truth + editorial. Two truth-class defects found, both repairable without dropping an item. Verdict NEEDS_FIXES.

### Citation does not support the claim

**F3 — § 4 Mini Shai-Hulud (TeamPCP) UPDATE: "CERT-FR confirms French victims" is not supported by the cited CERT-FR bulletin.**
Brief asserts (TL;DR): "CERT-FR confirms French victims in the Mini Shai-Hulud worm. ANSSI's CERTFR-2026-ACT-023 is the first national-CERT jurisdiction confirmation of the TeamPCP npm/PyPI supply-chain worm." § 4 H3: "the first national-CERT confirmation of victims within its own jurisdiction ... CERT-FR documents French organisations affected."
Fetched CERTFR-2026-ACT-023 via `tools/fetch_source.py url` this iteration. It is the routine weekly "Bulletin d'actualité" digest (Vulnérabilités significatives de la semaine 21). Its TeamPCP / Mini Shai-Hulud "Incidents" section describes the campaign generically ("TeamPCP est un groupe cybercriminel actif depuis au moins septembre 2025..."), lists the compromised packages (mbt@1.2.48, @cap-js/sqlite/postgres/db-service, @tanstack/*, @squawk/*, @mistralai/mistralai, mistralai/guardrails-ai/lightning on PyPI, 300+ @antv packages via account "atool"), describes the worm's secret-harvesting and `rm -rf ~/` persistence/destruction behaviour, and issues SEARCH/REMEDIATION RECOMMENDATIONS ("Le CERT-FR recommande donc de rechercher la présence de : paquets compromis..."). Nowhere does it confirm a French organisation as a victim, and it does not frame itself as a jurisdiction victim-confirmation. The "CERT-FR confirms French victims" / "first national-CERT jurisdiction confirmation" framing is unsupported.
Supported by the same source and should be retained: the expanded package scope (@antv, @mistralai/mistralai, guardrails-ai, lightning — all verbatim in the bulletin) and the 2026-05-13 source-code leak ("Le 13 mai 2026, le code source de Shai-Hulud a été publié par TeamPCP sur le forum cybercriminel Breach[Forums]").
Remediation: reframe the TL;DR + H3 to "CERT-FR issues a TeamPCP / Mini Shai-Hulud advisory with expanded affected-package scope and detection/remediation guidance" (what the source supports), and remove the French-victim-confirmation assertion. The PD-5 national-CERT carve-out in § 7 should be re-checked against the reframed claim (it currently rests on a victim-confirmation that the source doesn't make).

### Broken / unreachable URLs

**F1 — § 4 Nimbus Manticore UPDATE: the Security Affairs URL serves an unrelated article (Laravel-Lang Composer), not the Nimbus Manticore piece it is cited for.**
URL: `https://securityaffairs.com/192697/apt/nimbus-manticore-expanded-attacks-with-ai-assisted-malware-and-fake-zoom-installers.html`. Cited inline for the SSL.com cert claim ("abused two SSL.com-issued code-signing certificates ([Security Affairs, 2026-05-26])") and as an Additional source.
Fetched twice this iteration. The URL resolves but renders an article titled "Malware Found in Laravel-Lang Composer Packages After Git Tag Poisoning Attack" — no mention of Nimbus Manticore. The slug implies a Nimbus Manticore article; the served content is unrelated (likely wrong path / stale ID).
The underlying SSL.com cert claim is true — the Check Point primary (fetched this iteration) confirms two SSL.com certs issued to "Gray Matter Software S.R.L." and "Kirubel Kerie Negeya." So this is a citation repair, not an item drop.
Remediation: repoint to the correct Security Affairs Nimbus Manticore article, or drop the Security Affairs additional source entirely — the Check Point primary plus The Hacker News (2026-05-26, verified this iteration: "Iranian Hackers Deploy MiniFast and MiniJunk V2 via Phishing and SEO Poisoning") already establish the item and the in-window amplification.

### Editorial / less-is-more flags (advisory)

**F11a — Lithuania item, LRT additional-source date label.** `https://www.lrt.lt/.../lithuania-probes-theft-of-600-000-records-from-state-registry` resolves and supports the ~600k / investigation core claim, but its actual date is 2026-05-22 (brief labels "2026-05-26") and it does not mention the resignation. Resignation is independently sourced (The Record names Adrijus Jusas; Euronews corroborates). Advisory: correct the LRT date label. Low priority.

**F11b — Tycoon deep-dive detection-rule count.** Elastic Security Labs post verified this iteration — every load-bearing specific confirmed: Microsoft Authentication Broker client ID 29d9ed98-a469-4536-ade2-f981bc1d605e, Chrome OAuth client 77185425430.apps.googleusercontent.com, token progression none->refreshToken->primaryRefreshToken, aiConfirmedSafe/anomalousToken false-negative, Graph endpoints transitiveRoleAssignments / tenantRelationships/getResourceTenants / subscribedSkus, the March 2026 Microsoft/Europol/Cloudflare/SpyCloud/eSentire takedown of 300+ domains. Advisory: the precise count "six Entra ID and four Google Workspace detections" could not be exactly reconciled from the fetched body (it enumerated ~4-5 Entra + 4 Google rules); the fetch may simply not have surfaced every rule. Verify the "six Entra ID" figure or soften to "multiple." Also: Elastic tracks the actor as Storm-1747 (brief doesn't name it — fine).

### Items checked and CLEAN (no finding)

- **§ 2 CVE-2026-9312 GitHub Enterprise Server.** EUVD is a JS SPA (unrenderable by WebFetch or the bridge — both return only the React shell), so the cited primary itself could not be read. However the underlying facts were fully corroborated this iteration via the GHSA advisory (`github.com/advisories/GHSA-fwfp-h68w-2hcr`) and WebSearch (SecurityWeek): CVE id, SSRF via path-traversal in upload endpoint, CVSS 4.0 = 9.2, affected < 3.22, the exact six patched versions (3.16.20/3.17.17/3.18.11/3.19.8/3.20.4/3.21.1), Bug Bounty credit — all accurate. Name-collision WARN ("GitHub" shared with prior GitHub Actions supply-chain items) is BENIGN: GHES on-prem product, genuinely distinct from actions-cool/Megalodon/Nx; no attacker/defender inversion. No F15. (Editorial note for the main agent, not a finding: EUVD-as-sole-renderable-primary is a recurring blind spot — the GHES release-notes additional source also failed to render. Facts hold; consider whether EUVD should ever be the *only* primary given it can't be machine-verified.)
- **§ 2 CVE-2026-9642 Delta DIAView [SINGLE-SOURCE].** Tenable TRA-2026-44 verified: CVE id, CVSS 3.1 = 9.8, CVE-2025-62582 bypass / incomplete fix, unauthenticated remote database access — all supported. [SINGLE-SOURCE] flag correctly applied; § 7 single-source disposition honest (Tenable HIGH-reliability researcher).
- **§ 1 Lithuania Centre of Registers.** The Record + Euronews verified: ~600k, registers named, credential abuse (not a CVE), foreign infrastructure, exact exfiltrated/not-exfiltrated fields, early-April timeline, Adrijus Jusas resignation, Slovakia/Ukraine cross-reference, and the Russian-intelligence allegation (Euronews: Laurynas Kasčiūnas, "Russian intelligence operation"). Solid.
- **§ 4 ShinyHunters Charter + 7-Eleven UPDATE.** Charter (BleepingComputer) + CyberInsider verified; 7-Eleven SSN/driver's-licence claim traces to the cited CyberInsider additional source ("Some notifications reportedly included Social Security numbers, driver's license information..."). The 42M figure traces to the cited CyberInsider Charter source; BleepingComputer's "40M" variance is reconciled (both cited; actor-claimed figure). Charter's dispute vs actor claim handled even-handedly per § 7.
- **§ 4 Nimbus Manticore technical detail.** Check Point primary verified every specific (MiniFast 64-bit DLL, single CheckForUpdates export, /agent/init //agent/poll //upload/, 14-opcode set incl. DLL injection/UAC/scheduled-task, ZoomUpdateTaskUser-<SID> hijack, getsqldeveloper[.]com SEO poisoning, .config AppDomain hijack, parent=svchost.exe check, two SSL.com certs). UPDATE framing (out-of-window CP 2026-05-22 + in-window THN 2026-05-26 amplification) correct. Only defect is the mis-cited SecurityAffairs URL (F1).
- **§ 5 Tycoon 2FA deep dive.** All technical specifics verified against the Elastic primary (see F11b). Earns its length.
- **§ 7 drops.** MuddyWater out-of-window, database-ransom census single-source/vanity-metric, Oncology Institute SEC-403/single-verifiable-source — all three dispositions consistent with what the run_log fetch_failures (sec-disclosures-edgar 403, databreaches-net 403) and PD rules imply. Honest.

### Missed angles

None material. Coverage shape is sound: § 1 leads CH/EU/public-sector (Lithuania register, with explicit Zefix/cantonal-land-registry transfer), § 2 gates honoured (GHES = EUVD-CVSS-9+/pre-auth; Delta = EUVD-CVSS-9+/single-source-flagged), deep dive is genuine primary research. No Immediate Actions callout present (correct — nothing meets the "act to the hour" bar this run; the GHES SSRF is EPSS 0.0 / no ITW). § 3 intentionally empty with justification — acceptable.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 2)

Truth: F3 (CERT-FR French-victim claim unsupported), F1 (SecurityAffairs URL serves wrong article). Advisory: F11a (LRT date label), F11b (Tycoon rule count). Both truth defects are repairable in place — reframe the CERT-FR claim to what the source supports; repoint or drop the SecurityAffairs link. No item needs to be dropped.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: updates
  item: "UPDATE: Mini Shai-Hulud (TeamPCP) — CERT-FR confirms French victims, widens affected-package scope"
  url_or_quote: "ANSSI / CERT-FR published CERTFR-2026-ACT-023, the first national-CERT confirmation of victims within its own jurisdiction"
  summary: "CERTFR-2026-ACT-023 is the weekly bulletin d'actualite digest; it describes the campaign + lists packages + gives detection/remediation recommendations but confirms NO French victim and makes no jurisdiction victim-confirmation. Expanded package scope and 2026-05-13 source-code leak ARE supported; reframe the French-victim-confirmation claim."
- code: F1
  category: broken-url
  section: updates
  item: "UPDATE: Nimbus Manticore (UNC1549 / Screening Serpens)"
  url_or_quote: "https://securityaffairs.com/192697/apt/nimbus-manticore-expanded-attacks-with-ai-assisted-malware-and-fake-zoom-installers.html"
  summary: "URL serves 'Malware Found in Laravel-Lang Composer Packages After Git Tag Poisoning Attack' (no Nimbus Manticore). Cited inline for the SSL.com cert claim (which is true per Check Point). Repoint to correct SecurityAffairs article or drop it (Check Point + THN cover the item)."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "Lithuania Centre of Registers — LRT additional source"
  url_or_quote: "https://www.lrt.lt/en/news-in-english/19/2936340/lithuania-probes-theft-of-600-000-records-from-state-registry"
  summary: "LRT resolves + supports 600k/investigation but actual date is 2026-05-22 (brief says 2026-05-26) and no resignation mention. Resignation independently sourced. Advisory: fix date label."
- code: F11
  category: editorial-advisory
  section: deep-dive
  item: "Tycoon 2FA deep dive — detection-rule count"
  url_or_quote: "Elastic shipped six Entra ID and four Google Workspace detections"
  summary: "All load-bearing technical specifics verified against Elastic primary. Advisory: 'six Entra ID' count not exactly reconcilable from fetched body (~4-5 Entra + 4 Google enumerated); verify or soften to 'multiple'."
```
