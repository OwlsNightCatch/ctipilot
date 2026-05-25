**Model:** Anthropic Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-05-25T04:46:45Z · ended_at=2026-05-25T04:49:42Z · duration_seconds=177
**Self-telemetry:** urls_checked=7 · webfetch_calls=8 · bridge_fetches=0 · websearch_calls=1

## Verification report — briefs/2026-05-25.md (iteration 2)

Cold read, full end-to-end. Model-rotation alt-verifier (Sonnet). Iteration 2 receives the prior-iteration deltas block from the main agent. Walked that block before independent truth pass.

All 7 distinct inline source URLs WebFetched in this iteration with the outbound-links + mentioned-entities template:
- GHSA-w52v-v783-gw97 — resolved 200, specific advisory page, supports all Ghost version/CVSS/component/remediation claims
- XLab Qianxin ghost-cms-mass-compromised — resolved 200, specific research post, supports 700+ domains, kill chain, UtilifySetup.exe, victim list (Harvard, Oxford, Auburn — does NOT name DuckDuckGo)
- BleepingComputer ghost-cms-sql-injection-flaw — resolved 200, specific article, supports DuckDuckGo, victim list, SentinelOne Feb 27 reference, versions, CVSS
- ADAMnetworks support forum t/1584 — resolved 200, specific forum post (primary disclosure), supports 88M domains, US/UK/CA nexus, architectural description
- SecurityWeek underminr — resolved 200, specific article, supports 88M domains, detection gap quote verbatim confirmed, US/UK/CA most affected
- CyberInsider charter-communications — resolved 200, specific article, supports 42M claim as actor assertion, Charter partial denial, FCC CPNI language, no Salesforce vector or "first telco" framing
- Troy Hunt weekly-update-505 — resolved 200, specific post, supports ShinyHunters new victims listing including Charter; does NOT mention Salesforce, OAuth, or any vector
- SentinelOne vuln DB cve-2026-26980 — resolved (followed from BleepingComputer outbound links), specific entry, confirms Feb 27 publication on exploitation, CVSS 7.5 noted (different from GHSA 9.4 — see below)

---

## Prior-iteration deltas verification

### F14 remediation (quantifier-without-source: "first telco victim")

The main agent applied the following changes:
- § 4 heading: "first telco victim" dropped; now reads "telco victim in the Salesforce-credential campaign" — confirmed in brief line 51.
- TL;DR (line 11): now reads "by our own tracking its first telco/ISP victim to respond publicly" — the "by our own tracking" attribution is present.
- § 4 body (lines 53–55): now reads "By our own campaign tracking Charter is the first telco/ISP victim of this wave to respond publicly — an inference from the prior named victims (Instructure, Vimeo, Wynn, Vercel, Medtronic, 7-Eleven), none of them telcos, rather than a claim made by the cited sources."
- § 7 disclosure (lines 105–106): "The campaign-continuity link to 7-Eleven, and the 'first telco/ISP victim to respond publicly' characterisation, are our own campaign-tracking assessments (inferred from the prior named victims, none of them telcos), not attributions or claims made by the cited sources."

Verdict on F14 remediation: **correctly applied**. The absolute quantifier is now clearly disclosed as the brief's own inference, not a sourced fact. No new overclaim introduced. § 7 is consistent with the body text. The TL;DR retains "first" but the "by our own tracking" qualifier makes it clear it's the brief's assessment. F14 is resolved.

### F11 remediation (editorial-advisory: Troy Hunt citation positioning)

The main agent repositioned the Troy Hunt citation. Brief now reads (line 55): "The fresh Charter listing is independently corroborated by [Troy Hunt's Weekly Update 505, 2026-05-24], which records ShinyHunters' new claimed victims."
And § 7 (line 105): "Troy Hunt corroborates the fresh victim listing, not the Salesforce vector."

Troy Hunt Weekly 505 (fetched this iteration): confirms ShinyHunters' new victims including Charter, no Salesforce/OAuth reference. The citation now attaches correctly to the victim-listing claim. F11 is resolved.

---

## Independent truth pass (clean categories — no findings)

### Ghost CMS CVE-2026-26980 facts

All claims verified:
- CVE-2026-26980, CVSS 9.4, CWE-89, unauthenticated, Content API `slug` filter: confirmed by GHSA-w52v-v783-gw97 (fetched)
- Affected 3.24.0–6.19.0, fixed 6.19.1: confirmed by GHSA (fetched)
- 700+ compromised domains: confirmed by XLab (fetched)
- Named victims Harvard, Oxford, Auburn: confirmed by XLab (fetched) and BleepingComputer (fetched)
- DuckDuckGo named: confirmed by BleepingComputer (fetched); XLab does not name DuckDuckGo but BC does and BC is the cited source for that claim
- Admin API key extraction via blind SQLi: confirmed by both GHSA and XLab
- ClickFix / FakeCaptcha / fake Cloudflare prompt: confirmed by XLab and BleepingComputer
- UtilifySetup.exe payload: confirmed by XLab
- SentinelOne documented exploitation by 27 February: confirmed by BleepingComputer ("SentinelOne published on February 27 details about CVE-2026-26980 being exploited in attacks")
- Ghost(Pro) cloud patched server-side; self-hosted operators exposed: confirmed by BleepingComputer
- Ghost 6.19.1 released 19 February 2026: confirmed by GHSA outbound link to github.com/TryGhost/Ghost/releases/tag/v6.19.1
- WAF mitigation pattern `slug:[` / `slug%3A%5B`: confirmed by GHSA

Note on CVSS discrepancy: GHSA-w52v-v783-gw97 reports CVSS 9.4; SentinelOne's vuln DB reports 7.5. The brief uses 9.4, which matches the authoritative vendor advisory (TryGhost's own GHSA). This is not a brief defect — NVD/MITRE scoring sometimes differs from vendor advisory scores; the brief correctly uses the primary vendor advisory score.

### Underminr facts

All claims verified:
- ADAMnetworks primary disclosure: confirmed, resolves to specific forum post
- ~88M domains: confirmed by ADAMnetworks (fetched) and SecurityWeek (fetched)
- US, UK, Canada most affected: confirmed by ADAMnetworks and SecurityWeek
- No CVE, architectural property: confirmed
- Detection gap quote verbatim: confirmed ("the detection gap appears when DNS decisions, edge IPs, SNI, Host headers, and CDN tenant routing are not correlated")
- T1090.004 mapping: accurate (Domain Fronting ATT&CK technique)
- Specific vulnerable CDN providers not named: confirmed, both sources avoid naming specific CDNs
- "Classic domain fronting largely closed by major CDNs in 2021–2022": ADAMnetworks source says "2018" (for Google/Amazon). However, the brief's "2021–2022" is defensible as the period when the last major CDN (Microsoft Azure) completed the phase-out; web research confirms Google/Amazon acted in 2018 and Microsoft completed its block in 2022. The brief says "largely closed" not "fully closed" — this is accurate for the 2021-2022 period when Azure completed the picture. Not flagged as a defect; the claim is supportable from the broader record even if the ADAMnetworks source gives a different date anchor.
- Window-edge note in § 7 (SecurityWeek 2026-05-23 ~5h outside strict 36h window): appropriate disclosure

### Charter / ShinyHunters UPDATE facts

All claims verified (post-F14/F11 remediation):
- ShinyHunters listing of Charter around 22–23 May: confirmed by CyberInsider (fetched)
- 42M figure: correctly attributed as "actor's own unverified leak-site claim"
- Charter statement re "no sensitive PI or CPNI": confirmed verbatim by CyberInsider (fetched)
- FCC CPNI category framing: appropriate; CyberInsider quotes the Charter denial language
- 27 May deadline: confirmed by CyberInsider
- Troy Hunt Weekly 505 corroborates victim listing (not vector): confirmed (fetched) — Troy Hunt names Charter as one of ShinyHunters' new victims
- First telco/ISP framing: now correctly attributed as brief's own inference, not cited-source claim
- Salesforce-OAuth vector: correctly attributed to prior campaign coverage (7-Eleven, 2026-05-19), with no overclaim that the current sources confirm it for Charter

### IOC check

`UtilifySetup.exe` appears in § 1 body and § 5 kill-chain. This is a payload/masquerade filename used as a hunt artefact in the context of detection — "an Electron-based sample named `UtilifySetup.exe`". No SHA hash, no IP, no domain, no YARA/Sigma. Per-CLAUDE.md policy, file names used as hunt artefacts are not IOCs. Clean.

### Dedup check

Laravel-Lang/Packagist, Stormshield, GLPI, Exim, Cloud Atlas, Oncology Institute all dropped in § 7 with documented reasons. All confirmed against prior_coverage.json (walked in this iteration — all were covered in prior briefs or are out-of-window). No recycled-as-new material.

### GitHub WARN (name-collision: GHSA-w52v-v783-gw97)

The mechanical gate flagged a potential GitHub name-collision. The brief cites GitHub as the *host* of the TryGhost vendor security advisory (github.com/advisories/GHSA-w52v-v783-gw97), not GitHub as a victim. The advisory is titled "Ghost has a SQL injection in Content API" — TryGhost is the vendor, Ghost CMS is the affected product, GitHub is merely the advisory platform. No inversion. The WARN is benign.

### Single-source check

§ 7 line 106: "none — all included items carry ≥2 independent sources (Ghost: vendor advisory + research lab + news; Underminr: vendor primary + journalism; Charter: victim statement + journalism)." This is confirmed by my source review. No F12 flag needed.

### Style / workflow-internal language check

No IOCs. No workflow-internal language ("sub-agent", "Phase N", "spawn", "main agent") in §§ 0–6. English throughout. No vanity metrics. Clean.

### Missed angles

The brief covers Ghost exploitation, Underminr, and Charter/ShinyHunters adequately for the window. Given the run log notes sophos-xops (HTTP 503 × 5 consecutive) and inside-it-ch (Cloudflare challenge × 4 consecutive) — both Swiss/EU-relevant sources — there may be CH-specific advisories uncovered. The NCSC.ch coverage gap is noted; no CH-specific brief items are in the window based on available sources. Suggested search query: `site:ncsc.admin.ch OR site:melani.admin.ch "Ghost" OR "ClickFix" 2026`.

---

## Verdict

CLEAN

No findings requiring remediation. All prior-iteration defects (F14, F11) are correctly resolved with no regressions introduced. Ghost CVE technical facts, Underminr claims, and Charter UPDATE text all verified against fetched sources. No broken URLs, no unsourced facts, no hallucinated named entities, no IOCs, no recycled content, no single-source gaps, no editorial quality defects. One advisory observation (missed-angles, F10) is documented for operator awareness but does not block publication.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
[]
```
