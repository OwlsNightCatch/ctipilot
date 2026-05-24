**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-05-24T22:54:36Z · ended_at=2026-05-24T22:59:21Z · duration_seconds=285
**Self-telemetry:** urls_checked=22 · webfetch_calls=16 · bridge_fetches=0

## Verification report — briefs/weekly/2026-W21.md (iteration 2)

Cold read, weekly run (ISO week 2026-W21, 18–24 May 2026). W-PD-1 applied. This is the alt-verifier (even-iteration rotation). Prior-iteration deltas block processed: all 9 iter-1 findings reviewed against the remediations described in the spawn message. 22 distinct inline source URLs verified this pass (all § 1 item primaries, both synthesis sources CSA and SafeDep, § 5 incident primaries Grafana THN + SecurityWeek, Unimed heise, CERT-PL Sparx, LiteSpeed vendor blog, Drupal SA-CORE-2026-004, GitHub Security Blog, THN GitHub breach, Unit 42 ROADtools, ESET Webworm, Verizon DBIR SW, SecurityWeek DBIR, Rapid7 Q1 blog, Greenberg Traurig EU sanctions, Squire Patton Boggs EU sanctions, Swiss EAER, npm staged publishing, Cisco PSIRT, Fox Tempest Microsoft blog). MSRC SPA pages not re-fetched (confirmed JS-rendered / empty-body by iter-1; claims corroborated by THN and other cited sources).

Prior-iteration deltas review — findings and remediation status:

| Iter-1 finding | Remediation applied | Status after remediation |
|---|---|---|
| F13 EU sanctions Article 5n | Removed "Article 5n" designation; kept Regulation (EU) 2026/506 | FIXED — § 8 now reads "introduces a prohibition" with no specific article number. Greenberg Traurig (fetched) confirms regulation number and MSS prohibition without naming an article; Squire Patton Boggs (fetched) confirms Art 2f(1a) as operative — brief's agnostic wording is now accurate. |
| F3 SonicWall mis-attached Calypso URL | Removed the BleepingComputer Calypso URL; now single primary (Cybersecurity Dive) | FIXED — Cybersecurity Dive (fetched) fully supports all SonicWall claims (CVE-2024-12802, CVSS 9.1, UPN/SAM split, Akira-consistent TTPs, Feb-Mar 2026). |
| F3 Grafana pull_request_target + canary token | Added The Hacker News (https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html) as first source | NOT FIXED — THN fetched this iteration; article says only "An unauthorized actor obtained a GitHub token granting access to Grafana's environment." No mention of pull_request_target, GitHub Actions misconfiguration, or canary token. SecurityWeek (also fetched) similarly says "a compromised token" only — no attack vector and no detection mechanism. Both load-bearing specifics remain unsupported by any cited source. |
| F4 Megalodon date "2026-05-23" | Reworded to "2026-05-23 (disclosure; event 2026-05-18)" | FIXED — SafeDep (fetched) confirms event date 18 May 2026. Brief wording now distinguishes disclosure date from event date accurately. |
| F4 Sparx EUVD identifiers | Replaced EUVD ids with CVE ids the CERT-PL source carries | FIXED — CERT-PL (fetched) confirms CVE-2026-42096 through -42100, no EUVD ids; brief now shows only CVE ids. |
| F14 Unimed ~97,600+ synthesized aggregate | Softened to "~96,600 across four named hospitals (The Record)" | SUBSTANTIALLY FIXED — The Record URL returned a certificate error this iteration (unverifiable). Heise (fetched) gives ~95,000+ across 8+ named hospitals — different breakdown from The Record's alleged 96,600 across 4. Brief's attribution is correctly source-attributed ("The Record"), which is the right editorial fix, though The Record URL could not be verified. No new defect raised; attribution is correct. |
| F9 LiteSpeed patched version 2.4.5 | Corrected to vendor-recommended 2.4.7 | FIXED — LiteSpeed vendor blog (fetched) explicitly recommends "LiteSpeed WHM Plugin v5.3.1.0 (bundled with cPanel plugin v2.4.7)"; brief table and prose now say 2.4.7. |
| F8 Rapid7 KEV disclosure window | Advisory — main agent noted it as advisory | ADVISORY carried forward — Rapid7 Q1 blog (fetched) does NOT mention a disclosure-to-KEV-listing window metric; only says exploitation activity follows public discussion spikes. Phrase "KEV-to-listing window collapsing" in brief (line 248 "KEV-to-listing window collapsing") is still unsupported by the cited Rapid7 blog. Advisory-level. |
| F10 GovCERT.ch supply-chain guidance | Logged in § 10 as missed angle | CARRIED FORWARD in § 10 coverage notes — acceptable. |

### Citation does not support the claim

**F3 — Grafana § 5: `pull_request_target` misconfiguration and canary-token detection not in any cited source.**

The § 5 Grafana item (line 214) asserts: "Grafana Labs confirmed [...] that the CoinbaseCartel data-extortion group exfiltrated private source code only [...] via a `pull_request_target` GitHub Actions misconfiguration, and that it rejected the ransom. The instructive detail for detection engineers: Grafana caught the exfiltration through a **canary token embedded in the private code**."

The item now cites two sources:
- [The Hacker News — CoinbaseCartel / Grafana breach](https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html): fetched this iteration — article says "An unauthorized actor obtained a GitHub token granting access to Grafana's environment, enabling codebase download." Zero mention of pull_request_target, GitHub Actions misconfiguration, or canary token.
- [SecurityWeek — Grafana confirms breach](https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/): fetched this iteration — article says "a compromised token that granted access to the Grafana Labs GitHub environment." Zero mention of pull_request_target, GitHub Actions misconfiguration, or canary token.

Both load-bearing specifics that constitute the entire defender takeaway ("Audit your own GitHub org for `pull_request_target` workflow runs", "seed canary tokens in private repositories") remain unsupported by any cited source in the weekly item. Adding THN as first source did not resolve this finding — THN provides the same unsupported claims as SecurityWeek.

**Required fix:** Either (a) cite the underlying Grafana primary source (a Grafana blog post or GitHub issue from the 2026-05-19 daily) that contains these specifics; or (b) remove the `pull_request_target` and canary-token specifics from the weekly item and reframe around the confirmed facts (token theft, source-code-only exfiltration, ransom rejected).

### Needs more research

**F8 (carried advisory) — Rapid7 "KEV-to-listing window collapsing" not in cited blog.**

Line 248 states Rapid7's Q1 report finds "KEV-to-listing window collapsing." The cited Rapid7 Q1 2026 blog (fetched) says exploitation activity follows public-discussion spikes but provides no specific disclosure-to-KEV-listing metric. The load-bearing 38% top-IAV figure IS confirmed. The "KEV-to-listing window collapsing" phrase is advisory-level unsupported. If taken from the downloadable full-report PDF (linked on the Rapid7 page as a separate URL), that source should be cited directly. Advisory — does not block CLEAN verdict if the Grafana F3 is resolved.

### Notes — checks that PASSED (no finding)

- **EU sanctions § 8**: Regulation (EU) 2026/506 confirmed by Squire Patton Boggs (fetched); MSS prohibition and 25 May effective date confirmed; "Article 5n" correctly removed; Swiss EAER (fetched) correctly confirmed to not mention MSS prohibition, brief hedge ("requires SECO confirmation") is accurate.
- **Verizon DBIR statistics** (31% vuln-exploit top IAV, 13% credential abuse, 43-day median patch vs 32-day prior, 26% vs 38% KEV remediation, 48% third-party, shadow AI): ALL CONFIRMED by SecurityWeek DBIR article (fetched).
- **SLSA BL3 "invalidated as an integrity gate"**: CSA note and Unit 42 (both fetched) say "no longer a reliable integrity gate" / "necessary but no longer sufficient." Brief's phrasing "SLSA Build Level 3 provenance attestation is invalidated as an integrity gate" is supported (functional equivalence in meaning).
- **Megalodon date (fixed)**: "2026-05-23 (disclosure; event 2026-05-18)" now correctly distinguishes — SafeDep (fetched) confirms 18 May 2026 burst.
- **SonicWall (fixed)**: Cybersecurity Dive (fetched) supports all claims. Single-primary status noted in § 10.
- **LiteSpeed 2.4.7 (fixed)**: Vendor blog (fetched) confirms 2.4.7 / WHM v5.3.1.0.
- **Sparx CVE ids (fixed)**: CERT-PL (fetched) confirms CVE-2026-42096…-42100 only, no EUVD ids.
- **Drupal CVE-2026-9082**: Drupal SA-CORE-2026-004 (fetched) confirms pre-auth SQLi, PostgreSQL-only, exploit attempts in the wild confirmed 22 May 2026.
- **GitHub Security Blog internal repos**: Confirmed ~3,800 repos exfiltrated, no customer-data impact per 20 May 2026 post (fetched).
- **Cisco CVE-2026-20223**: CVSS 10.0, no workaround, both confirmed by Cisco PSIRT advisory (fetched).
- **Webworm ESET**: EchoCreep, GraphWorm, Belgian/Italian/Serbian/Polish/Spanish government targets confirmed (fetched). Brief lists five countries; ESET source also names Hungary and Czechia — selective not wrong.
- **Fox Tempest**: Microsoft blog (fetched) confirms Rhysida/INC/Qilin/Akira ransomware families supplied by Fox Tempest's signing service.
- **ROADtools Unit 42**: Midnight Blizzard, Curious Serpens, UTA0355 all confirmed (fetched).
- **npm staged publishing GA**: GitHub Changelog (fetched) confirms GA, 2FA requirement, npm CLI 11.15.0+.
- **[SINGLE-SOURCE] discipline (F12)**: Check Point AI (§ 6), Huawei/POST Luxembourg (§ 4), Rhysida Stuttgart (§ 5), The Gentlemen RaaS (§ 7) all carry markers, § 10 records them. SonicWall is noted in § 10 as single-primary but NOT marked [SINGLE-SOURCE] in heading — however, § 10 line 340 explicitly discloses this ("now rests on a single primary") which is the correct transparency mechanism for weekly; no F12 raised.
- **W-PD-1**: Every section item answers inaction=incident / cross-day-pattern / strategic-horizon. § 10 correctly documents dropped items that cleared daily bar but not weekly bar.
- **Style and IOCs**: Zero IOCs in published prose; no workflow-internal language; English throughout.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 1)

The single truth defect is F3 Grafana (persisted from iter-1 despite the THN addition, because THN also doesn't support the specific claims). The advisory is the Rapid7 KEV-window phrase carried from iter-1 (F8). No new defects were introduced by the iter-1 remediations.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: incidents-disclosures
  item: "Grafana Labs / CoinbaseCartel — source-code-only theft confirmed"
  url_or_quote: "via a `pull_request_target` GitHub Actions misconfiguration ... Grafana caught the exfiltration through a canary token embedded in the private code"
  summary: "Both cited sources (THN fetched: 'GitHub token granting access'; SecurityWeek fetched: 'compromised token') say only a token was used — neither mentions pull_request_target, GitHub Actions misconfiguration, or canary token. Remediation (adding THN) did not resolve the finding because THN also lacks these specifics. Add the underlying Grafana primary (e.g. Grafana blog post from 2026-05-19 daily) that contains these details, or remove the unsupported specifics and reframe around confirmed facts."
- code: F8
  category: needs-more-research
  section: annual-periodic-reports
  item: "Rapid7 Q1 2026 Threat Landscape Report"
  url_or_quote: "KEV-to-listing window collapsing"
  summary: "Rapid7 Q1 blog (fetched) does not mention a disclosure-to-KEV-listing metric; notes only that exploitation follows public-discussion spikes. Advisory — the 38% top-IAV figure IS confirmed. Soften or cite the downloadable full-report PDF directly."
```
