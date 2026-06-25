**Model:** Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-25T04:53:08Z · ended_at=2026-06-25T04:57:43Z · duration_seconds=275

## Verification report — briefs/2026-06-25.md (iteration 3)

Cold read by a fresh Opus instance. Mechanical gate (check_brief.py) passed pre-spawn (51 pass / 4 warn); this pass is URL-truth + editorial only. Every cited primary and load-bearing secondary URL was `WebFetch`ed in this iteration. The url-liveness ledger (work/2026-06-25-da7fbd23/url-liveness.tsv) shows all cited URLs returned HTTP 200 during the run; I independently confirmed each resolves to a specific article/advisory (no homepages/listings) and supports its attached claim.

### Sources fetched and confirmed this pass
- BleepingComputer Operation Endgame — 326 servers / 142 domains / ~27M credentials / 385,000+ systems / EUR 41M all confirmed verbatim; page does NOT carry the StealC directory-traversal detail (brief correctly attributes that elsewhere). ✓
- MISP 2.5.42 release notes — six CVE IDs, both RCE paths (rdkafka + ndjson), Azure-AD + mass-assignment hardening, no per-CVE CVSS published. ✓
- GHSA-834x-pvxg-xh58 — CVE-2026-56447, CVSS 9.3, rdkafka plugin.library.paths RCE. ✓ (brief Evidence quote is a faithful paraphrase of the advisory wording)
- GitHub release v2.5.42 — specific release page, all six CVEs listed. ✓
- NCSC-CH Wochenrückblick Week 25 — both Evidence quotes exact matches; "Play voicemail as guest", BEC, credential-resale-resurfaces-weeks-later all confirmed verbatim. ✓
- Proofpoint/IBM X-Force — StealC C2 directory-traversal (forward-slash sanitiser failure) confirmed; researchers discovered / law enforcement built+used the exploit — matches brief attribution exactly. ✓ (this page carries the lower 296/66/25.6M StealC-specific figures, which the brief's § 7 Contradiction note correctly documents)
- SecurityWeek Mistic — Woodgnat/KongTuke, six ransomware families, MLTBackdoor alias, April 2026, ClickFix/FileFix/CrashFix. ✓
- CSO Online Mistic — MpExtMs.exe (signed MS Defender) → EndpointDlp.dll sideloading confirmed, cited to Symantec — the load-bearing detail; brief attributes it to CSO citing Symantec. ✓
- Novee Security Cordyceps — 30,000 scanned / 654 flagged / 300+ exploitable verbatim; all five named orgs (Microsoft/Azure Sentinel, Google/ADK, Apache/Doris, Cloudflare/Workers SDK, PSF/Black) confirmed. ✓
- SecurityWeek Cordyceps — corroborates 654/300+ and named orgs (does not carry 30,000 — that is from Novee primary). ✓
- GitHub Changelog — actions/checkout v7 GA 18 June, refuses fork-PR fetch in pull_request_target; specific entry, not a redirect. ✓
- SecurityWeek Klue/BeyondTrust-LastPass — BeyondTrust verbatim quote matches; LastPass new; "roughly 15" victims; Icarus crew + Klue compromised integration. ✓ (BeyondTrust + LastPass confirmed as genuinely NEW named victims vs dedup context — prior briefs tracked Huntress/Recorded Future/Tanium/Jamf/Sprout/HackerOne/OneTrust/Snyk/Insurity/8x8)
- Help Net Security Klue/LastPass — "did not affect... customer vaults" and OAuth-token quote both verbatim. ✓
- BleepingComputer Edgecution — Payouts Kings, Edge extension + Native Messaging + Python backdoor, Python 3.13.3, "Edge Monitoring Agent", headless Edge, Teams→fake Outlook portal. ✓ (does NOT mention CloudFront — consistent with brief attributing cloudfront detail to Zscaler, not BC)
- Zscaler ThreatLabz Edgecution — readable this pass: cloudfront.net/AWS C2 confirmed verbatim; BOTH Evidence quotes appear VERBATIM in the Key Takeaways section. ✓
- ESET WeLiveSecurity — 53 Amadey / 73 StealC clusters verbatim; RC4 keys + clustering contribution. ✓
- Europol newsroom — SPA loading-shell only (summariser couldn't render body) but title matches, slug-specific article (not a listing), corroborated by BC+Microsoft which link to it. Acceptable.
- The Hacker News Klue-disable — specific article, confirms Salesforce disabled the Klue app. ✓

### Dedup verdict
No recycled material. Operation Endgame (Amadey/StealC, 24 June) is explicitly disambiguated from the 06-19 SocGholish/TA569 phase. Klue/Icarus UPDATE adds BeyondTrust + LastPass as genuinely new victims. § 7 drops (DifyTap, OXLoader, Shai-Hulud/Miasma/Hades, Huione, GhostSender, Cacti, Arista) are all soundly reasoned (out-of-window or unreconciled-mechanism). F15 name-collision (Operation Endgame) is benign — same campaign umbrella, explicitly disambiguated.

### Editorial / less-is-more flags (advisory)
- F11a — Edgecution Evidence field attributes two quotes to "BleepingComputer citing Zscaler ThreatLabz". Both quotes are in fact verbatim from the Zscaler primary (the item's FIRST Source), which I confirmed carries them word-for-word in its Key Takeaways. BleepingComputer paraphrases rather than quotes them. The claims are fully supported by a cited source on the item; only the in-Evidence attribution label is imprecise. Optional fix: re-label the two quotes to "(Zscaler ThreatLabz)" or "(BleepingComputer/Zscaler)". Not a truth defect — substance correct and traceable.
- F11b — § 4 states Salesforce disabled the Klue connection "on 17 June". The cited The Hacker News page (the source attached to that sentence) does not state the 17 June date specifically (it gives publication 19 June, incident 11 June). The date is consistent with prior in-house coverage and is not contradicted by any source; low materiality. Optional: soften to "by 17 June" or cite the source that carries that exact date.

Low-confidence note (not a finding): the "C++" language descriptor for Amadey/StealC (§ 1 Endgame body) did not surface in my ESET fetch; "modular loader", "29+ commands" (Microsoft) and "RC4-encrypted HTTP" (ESET) are all sourced. The Microsoft technical blog is the cited primary and plausibly carries the C++ implementation detail. Not flagged.

### Verdict
CLEAN — no truth or editorial defects. Two F11 advisory items (attribution-label precision; one under-confirmed date) the main agent MAY leave; both are traceable to cited sources and do not block publish.

### Findings summary (machine-readable)
```yaml
# Findings summary (machine-readable) — v2.48
- code: F11
  category: editorial-advisory
  section: deep-dive
  item: "Edgecution — Native Messaging bridge (§ 5)"
  url_or_quote: "Evidence: \"Edgecution has two components...\" / \"the attackers gain direct host access...\" attributed to BleepingComputer citing Zscaler ThreatLabz"
  summary: "Both quotes are verbatim from the Zscaler primary (item's first Source, confirmed this pass), not BleepingComputer which paraphrases. Claims fully supported; only the Evidence attribution label is imprecise. Optional re-label to Zscaler ThreatLabz."
- code: F11
  category: editorial-advisory
  section: updates-to-prior-coverage
  item: "Klue/Icarus UPDATE (§ 4)"
  url_or_quote: "Salesforce had already disabled the Klue Battlecards connection on 17 June (cited to The Hacker News)"
  summary: "Cited THN page does not state the 17 June date specifically (pub 19 June, incident 11 June). Consistent with prior coverage, not contradicted. Low materiality; optional soften to 'by 17 June'."
```
