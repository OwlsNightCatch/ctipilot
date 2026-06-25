**Model:** Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-25T04:28:17Z · ended_at=2026-06-25T04:32:07Z · duration_seconds=230
**Self-telemetry:** webfetch_calls=16 · websearch_calls=0 · bridge_fetches=2 · urls_checked=18

## Verification report — briefs/2026-06-25.md (iteration 1)

Cold read by a hostile Swiss/EU public-sector SOC reader. All inline Source/Additional-source URLs on every item were fetched or confirmed via the url-liveness ledger; named CVEs/actors/campaigns/versions/numbers cross-checked against the cited sources; ATT&CK technique IDs verified against attack.mitre.org. The Arista EOS item is the headline defect — it asserts "no CVE was published" and "exploitation not independently confirmed" for a flaw (CVE-2026-7473) that this repo already covered on 2026-06-10 as CISA-KEV-listed and exploited.

### Citation does not support the claim

**F3a — Arista EOS "no CVE published" is contradicted by both cited sources AND by prior coverage.** §1 frames the item as having no CVE, and §7 Verification Notes states verbatim: *"No CVE identifier was published with the disclosure."* Both cited sources name the CVE: the SecurityWeek page (`https://www.securityweek.com/no-patch-planned-for-exploited-arista-eos-vulnerability/`) states *"CVE-2026-7473 (CVSS 6.9)"* and *"CISA added CVE-2026-7473 to its Known Exploited Vulnerabilities (KEV) list."* The Eclypsium page (`https://eclypsium.com/blog/arista-eos-tunnel-decapsulation-no-patch/`) is titled around CVE-2026-7473 and links its NVD record. This repo's own `state/covered_items.json` carries `"key": "CVE-2026-7473"` and `briefs/2026-06-10.md` covered it as *"Arista EOS tunnel-decapsulation logic flaw bypasses segmentation, added to CISA KEV."* The "no CVE" claim is a hallucinated/contradicted fact. Remediation: name CVE-2026-7473 (CVSS 6.9), correct §7, and frame the item as an UPDATE to the 2026-06-10 coverage.

**F3b — Arista exploitation is independently confirmed (CISA KEV), not merely "the sources' assertion."** §7 states the in-the-wild claim *"is presented as the sources' assertion, not independently confirmed."* Both cited sources state CVE-2026-7473 is in CISA KEV (added 2026-06-09) — that IS independent confirmation, and the prior 06-10 coverage already recorded `Status: exploited, cisa-kev`. The reduced-confidence hedge in §7 is wrong and should be removed; exploitation is KEV-confirmed.

**F3c — Operation Endgame directory-traversal exploitation mis-attributed to Proofpoint/IBM.** §1 states *"Proofpoint and IBM X-Force exploited a directory-traversal flaw in StealC's C2 panel ... to map affiliate infrastructure."* The cited Proofpoint source (`https://www.proofpoint.com/us/blog/threat-insight/stealc-you-later-proofpoint-and-ibm-x-force-support-operation-endgame`) attributes the operational exploitation to law enforcement: *"An exploit was created, tested and later used in the disruptive and investigative actions by global law enforcement to search and seize StealC servers."* Proofpoint/IBM identified and documented the flaw; LE wielded it. Reword to "Proofpoint and IBM X-Force identified/documented a directory-traversal flaw ... which law enforcement used to seize StealC servers."

### Unsupported / hallucinated facts

**F4a — Cacti: three of four cited CVEs and the "40 vulnerabilities" / "ENISA EUVD 24 June" claims are absent from the only cited source.** §2 attributes CVE-2026-39893, CVE-2026-39948, CVE-2026-39955 (SQLi cluster, CVSS 9.8) and CVE-2026-39938 (unauthenticated LFI via `graph_theme`) plus *"fixes 40 vulnerabilities"* and *"indexed by ENISA EUVD on 24 June"* to GHSA-69gg-mjfm-jjpc. Fetching that advisory (`https://github.com/Cacti/cacti/security/advisories/GHSA-69gg-mjfm-jjpc`) shows it covers ONLY **CVE-2026-39893** — it does not mention CVE-2026-39948, -39955, -39938, the `graph_theme` LFI, "40 vulnerabilities," ENISA or EUVD. The item is flagged `[SINGLE-SOURCE]`, so no other primary covers the extra three CVEs/LFI. Remediation: either cite the per-CVE GHSAs / the Cacti 1.2.31 release notes that actually carry CVE-2026-39948/-39955/-39938 and the 40-count, or narrow the item to CVE-2026-39893 only. (CVSS 9.8 is verified only for CVE-2026-39893.)

**F4b — MISP: five of six per-CVE CVSS scores and the per-CVE technical descriptions are unsourced.** §2 lists CVSS 9.3/8.7/9.3/9.4/7.1 for CVE-2026-56447/-56446/-56425/-56424/-56423 and detailed descriptions (session_id-as-OAuth-state, contributor hard-delete, etc.). The MISP release notes (`https://www.misp-project.org/2026/06/22/misp.2.5.42.release.html/`) and the GitHub release tag (`https://github.com/MISP/MISP/releases/tag/v2.5.42`) carry NO CVSS scores and only generic one-liners ("RCE via arbitrary rdkafka config paths", "Azure AD authentication hardening"). The only cited source with detail, GHSA-834x-pvxg-xh58, covers ONLY CVE-2026-56447 (9.3, rdkafka RCE) — confirmed accurate. The other four CVSS scores and descriptions trace to no inline source. Remediation: add the per-CVE GHSAs (the CIRCL GCVE / vulnerability.circl.lu records the release notes link out to) as Additional sources, or drop the unsourced CVSS numbers.

**F4c — Mistic "headline capability is in-memory execution of Beacon Object Files" is in no readable cited source.** §1 calls BOF in-memory execution Mistic's *"headline capability."* Neither SecurityWeek (`https://www.securityweek.com/new-mistic-rat-opens-door-to-several-ransomware-families/`) nor the cited CSO Online article (`https://www.csoonline.com/article/4189132/...`) mentions Beacon Object Files. The Broadcom/Symantec bulletin is noted SPA-unreadable in §7, so no fetchable cited source corroborates the BOF claim. (The MpExtMs.exe → EndpointDlp.dll sideloading IS confirmed by CSO Online — CSO adds a `version.dll` intermediary the brief omits, a benign simplification.) Remediation: attribute the BOF claim to the Symantec bulletin explicitly with a confidence caveat, or drop the "headline capability" framing.

### Drop / reframe (dedup — recycled material presented as new)

**F7a — Arista EOS is recycled 06-10 coverage presented as a fresh in-window disclosure.** CVE-2026-7473, the Arista SA-0137 advisory (May 5), and the KEV listing (June 9) are all weeks old and covered on 2026-06-10. The only genuinely new hook is the Eclypsium blog (June 23) re-packaging the no-patch angle. The item carries no UPDATE framing and no acknowledgment of prior coverage; `state/covered_items.json` logged it as a new `vulnerability-trend:` entry rather than an UPDATE to the existing CVE-2026-7473 record (PD-8 dedup miss). The genuinely-new element — Eclypsium's emphasis that Arista will not patch the decap behaviour (06-10 brief said `patch-available`) — is worth carrying, but as an `UPDATE:` to CVE-2026-7473 that names the CVE, retains the KEV/exploited status, and surfaces the patch-status delta. Not a clean drop, but a mandatory reframe.

### Surface contradiction (already handled — confirmation)

**F9 (confirm, no action) — Operation Endgame figures.** §7 already surfaces the 326/142/27M/€41M vs 296/66/25.6M sub-agent disagreement and picks the BleepingComputer-corroborated figure. Verified: BleepingComputer (`.../amadey-stealc-malware-operations-disrupted-in-operation-endgame-action/`) states verbatim *"326 servers and 142 domains ... €41 million ($47 million) ... recovered approximately 27 million credentials stolen from over 385k compromised systems."* ESET cluster counts (53 Amadey / 73 StealC) confirmed verbatim on the ESET page. No action — the brief picked correctly. Minor nit: brief says ESET contributed "RC4 keys"; ESET's page says "encryption keys" generically — harmless.

### Editorial / less-is-more flags (advisory)

**F11a — Edgecution CloudFront C2 quote rests on an unreadable source.** The §5 Evidence quote *"All of the C2 servers observed by ThreatLabz have leveraged subdomains of cloudfront.net and hosted on Amazon AWS"* is attributed to Zscaler ThreatLabz, whose page is SPA-unreadable per §7; BleepingComputer (the readable corroborator) did NOT carry the CloudFront detail. The load-bearing Native Messaging mechanism IS fully corroborated by BleepingComputer, so this is advisory only — but the verbatim CloudFront quote could not be independently confirmed this run. Consider softening to "Zscaler reports" without the verbatim quote, or accept the residual.

### Items verified clean (no finding)

- NCSC-CH Week 25 voicemail-phishing (§1): title, date (23.06.2026), both Evidence quotes verbatim-accurate against the bridge-fetched page; ATT&CK T1114.003/T1098 plausible; national-CERT carve-out correctly applied in §7.
- Klue/Icarus UPDATE (§4): BeyondTrust + LastPass confirmed newly-named (SecurityWeek); "vaults not affected" confirmed (Help Net: "did not affect ... customer vaults"); "past 14" matches SecurityWeek "roughly 15"; Icarus attribution confirmed; both Evidence quotes verbatim.
- Edgecution deep dive (§5): Native Messaging bridge, Payouts Kings operator, Teams→fake-Outlook lure, embedded Python 3.13.3, headless Edge — all confirmed by BleepingComputer. ATT&CK T1204.002 (User Execution: Malicious File), T1564.003 (Hidden Window), T1071.001 (Web Protocols), T1559 (Inter-Process Communication), T1059.006 (Python) all map correctly.
- Cordyceps (§3): 30,000 repos / 654 flagged / 300+ exploitable and all named orgs (Microsoft Azure Sentinel, Google ADK, Apache Doris, Cloudflare Workers SDK, PSF Black) confirmed verbatim on Novee page; actions/checkout v7 confirmed via GitHub Changelog.
- Operation Endgame core figures + ESET clusters: confirmed (see F9).

### Verdict
NEEDS_FIXES (truth: 6, editorial: 1, advisory: 1)

Truth = F3a, F3b, F3c, F4a, F4b, F4c. Editorial = F7a. Advisory = F11a. F9 is a confirmation of an already-handled contradiction (no count). The Arista cluster (F3a/F3b/F7a) is the publication-blocking defect: a "no CVE published / exploitation unconfirmed" framing for a KEV-listed, already-covered CVE-2026-7473 actively misleads the SOC reader.

### Findings summary (machine-readable)
```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "Eclypsium reports an exploited, unpatched tunnel-decapsulation flaw in Arista EOS"
  url_or_quote: "\"No CVE identifier was published with the disclosure.\" (brief §7) vs SecurityWeek \"CVE-2026-7473 (CVSS 6.9)\" + \"CISA added CVE-2026-7473 to its KEV list\""
  summary: "Both cited sources name CVE-2026-7473; repo covered it 2026-06-10 as KEV-listed. The 'no CVE published' claim is false. Name the CVE and frame as UPDATE."
- code: F3
  category: claim-not-supported
  section: verification-notes
  item: "Arista EOS exploitation confidence"
  url_or_quote: "\"presented as the sources' assertion, not independently confirmed\" (brief §7)"
  summary: "Exploitation is independently confirmed by CISA KEV (added 2026-06-09) per both cited sources; remove the reduced-confidence hedge."
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "Operation Endgame — StealC C2 directory-traversal"
  url_or_quote: "\"Proofpoint and IBM X-Force exploited a directory-traversal flaw in StealC's C2 panel ... to map affiliate infrastructure\""
  summary: "Proofpoint source attributes operational exploitation to law enforcement, not Proofpoint/IBM ('An exploit was created, tested and later used ... by global law enforcement'). Reword to identified/documented."
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "[SINGLE-SOURCE] Cacti 1.2.31 — CVE-2026-39893/-39938/-39948/-39955"
  url_or_quote: "https://github.com/Cacti/cacti/security/advisories/GHSA-69gg-mjfm-jjpc"
  summary: "Cited GHSA covers ONLY CVE-2026-39893. CVE-2026-39948/-39955/-39938, the graph_theme LFI, '40 vulnerabilities' and 'ENISA EUVD 24 June' are not in the only cited source. Add per-CVE/release-notes sources or narrow to CVE-2026-39893."
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "MISP 2.5.42 — six CVEs"
  url_or_quote: "CVSS 8.7/9.3/9.4/7.1 for CVE-2026-56446/-56425/-56424/-56423"
  summary: "MISP release notes + GitHub release carry no CVSS scores; cited GHSA-834x covers only CVE-2026-56447 (9.3). The other four CVSS scores + per-CVE descriptions trace to no inline source. Add CIRCL GCVE / per-CVE GHSA sources or drop the numbers."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "Mistic backdoor"
  url_or_quote: "\"Its headline capability is in-memory execution of Beacon Object Files\""
  summary: "BOF in-memory execution is in neither readable cited source (SecurityWeek, CSO Online); Broadcom/Symantec bulletin is SPA-unreadable per §7. Attribute to Symantec with caveat or drop the 'headline capability' framing."
- code: F7
  category: drop
  section: active-threats
  item: "Arista EOS tunnel-decapsulation"
  url_or_quote: "state/covered_items.json key CVE-2026-7473; briefs/2026-06-10.md"
  summary: "Recycled 06-10 coverage (CVE-2026-7473, KEV 06-09, Arista SA-0137 May 5) presented as fresh. Reframe as UPDATE: naming CVE-2026-7473, retaining KEV/exploited status, surfacing the new 'no patch planned' delta (06-10 said patch-available)."
- code: F11
  category: editorial-advisory
  section: deep-dive
  item: "Edgecution — CloudFront C2"
  url_or_quote: "\"All of the C2 servers observed by ThreatLabz have leveraged subdomains of cloudfront.net ...\""
  summary: "Verbatim quote attributed to Zscaler whose page is SPA-unreadable; BleepingComputer (readable corroborator) lacks the CloudFront detail. Native Messaging mechanism is fully corroborated; advisory only — soften to 'Zscaler reports' or accept residual."
```
