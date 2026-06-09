**Model:** Anthropic Claude Opus 4.8 (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-09T05:13:49Z · ended_at=2026-06-09T05:17:21Z · duration_seconds=212
**Self-telemetry:** webfetch_calls=14 · websearch_calls=0 · bridge_fetches=0 · urls_checked=14

## Verification report — briefs/2026-06-09.md (iteration 5, final/cap)

Cold read, both axes. Mechanical gate exited 0 pre-spawn; structural/URL-allowlist/footer-taxonomy/CVE-sync out of scope. I fetched every inline source URL carrying a load-bearing claim (14 distinct URLs — Check Point advisory, GitHub Advisory GHSA-v4p8-mg3p-g94g, Exodus Intelligence, Unit 42, Mandiant UNC6692, Horizon3.ai, BleepingComputer Oxford, SANS ISC 33060, Meta WhatsApp, Microsoft AI-brands, Help Net Security, Wiz Miasma, BleepingComputer Qilin, Ubuntu tracker, Rapid7, The Register, The Hacker News, CyberScoop, BleepingComputer WhatsApp, Microsoft Fox Tempest). NCSC-CH security-hub hash route and Check Point sk185033 SPA are corroborators (not sole support) per the established disposition — not fetched/re-flagged.

### Truth pass — all claims confirmed against fetched sources
- CVE-2026-50751: CVSS 9.3, IKEv1 cert-validation auth bypass, Qilin affiliate, exploitation since 7 May 2026 ("earliest observed exploitation date of May 7, 2026"), early-June surge, CISA KEV 2026-06-08, sk185033, affected trains R80.20.X→R82.10 + Spark, concurrent scanning of Palo Alto/Fortinet/F5 — all confirmed by Check Point + Help Net + BleepingComputer + Rapid7. Companion CVE-2026-50752 CVSS 7.4 site-to-site MitM, no ITW — confirmed.
- CVE-2026-42271 (LiteLLM): CVSS 8.7, range 1.74.2→<1.83.7, fixed 1.83.7, /mcp-rest/test/connection + /tools/list endpoints, API-key-gated no role check — confirmed by GitHub Advisory. Chaining with CVE-2026-48710 (Starlette Host-header bypass) → unauthenticated — confirmed by Horizon3.ai (2026-06-01). CISA KEV 2026-06-08 — consistent. (CVE-2026-48710 not in GitHub Advisory, but brief attributes the chain claim to Horizon3.ai, which states it verbatim.)
- CVE-2026-23111 (Linux nf_tables UAF): single inverted "!" in nft_map_catchall_activate(), >99% reliability on idle Debian Bookworm/Trixie + Ubuntu 22.04/24.04 LTS, root + container escape, upstream patch 5 Feb 2026, CVSS 7.8 — confirmed by Exodus + Ubuntu tracker + The Hacker News (T1068/T1611).
- Unit 42 Teams: 42% of phishing alerts (up from 30%), Cloaked Ursa/APT29/Midnight Blizzard, UNC6692 — confirmed. SNOW suite (SNOWBELT/SNOWGLAZE/SNOWBASIN), LSASS T1003.001, Pass-the-Hash T1550.002 — NOT in Unit 42 but brief attributes these to Mandiant UNC6692 source, which confirms all of them (dated 2026-04-23, matches brief).
- Microsoft AI-brands: Storm-3075, Fox Tempest, ChatGPT/Claude/DeepSeek/Copilot impersonation, SEO/malvertising/Rebrandly→CAPTCHA, code-signing T1553.002, Lumma/Vidar/Hijack Loader/Oyster, fraudulent GitHub repos — confirmed. Fox Tempest MSaaS post (2026-05-19) — confirmed.
- Oxford breach: GTI compromise 28 May, names/emails/encrypted-passwords-for-non-SSO, KCL + Manchester, credential-harvest oriented — confirmed by BleepingComputer; The Register corroborates unnamed further institutions.
- Meta/NSO: contempt complaint, 2025 injunction, one-click links to external sites, no protocol zero-day / no E2EE bypass, test accounts removed — confirmed by Meta + CyberScoop + BleepingComputer (T1566.002 reasonable mapping).
- TeamPCP UPDATE: Mini Shai-Hulud open-sourced on GitHub, Phantom Gyp abusing node-gyp/binding.gyp, SLSA-provenance-does-not-survive-subverted-build point, Miasma/@redhat-cloud-services — confirmed by SANS ISC 33060 + Wiz (2026-06-01).

### Editorial pass
- Relevance: every item carries CH/EU public-sector nexus or widely-deployed-tech CVE (Check Point VPN + NCSC-CH advisory; LiteLLM AI gateway; Linux kernel; Teams config; Oxford/Swiss Hochschulen; commercial spyware on public-sector mobile fleets; npm/Red Hat CI/CD). No drops warranted.
- Primary-source kind: every footer leads with vendor PSIRT / research-lab / vendor blog / victim statement. No NVD/MITRE-only or national-CERT-only Source. NVD/cve.org appear only as outbound links in fetched advisories, not as brief Sources.
- Single-source: §7 correctly flags SoFi (single-source) and documents 5 dropped items with reasons. Microsoft AI-brands item is two Microsoft posts (same vendor) but both are HIGH-reliability primary research, no ITW-incident claim — acceptable for a research-section item, not an F12.
- Name-collision (Shai-Hulud): consistently attacker-side tooling, same entity as prior 06-06/W23 coverage, framed as explicit UPDATE. No attacker/defender inversion. Benign.
- Quantifiers: "a month before disclosure" (7 May→8 Jun), ">99% reliability", "42% / up from 30%" — all source-backed verbatim.
- Analytical-links: all asserted connections (Qilin↔CVE, Storm-3075↔Fox Tempest, UNC6692↔SNOW, 42271+48710 chain, Phantom Gyp/Miasma↔TeamPCP) stated by cited sources.
- Style: zero IOCs (BleepingComputer/Meta/Microsoft surfaced domains + a cert thumbprint in sources; brief correctly excludes all). English throughout. No workflow-internal language. Immediate Action callout meets the "act now" bar (KEV-listed, ITW since 7 May, NCSC-CH Action-Required).
- Coverage shape: §1 leads UK-education + EU-relevant spyware (CH/EU nexus present); §2 inclusion gates honoured (both CVEs KEV-listed/ITW); deep dive (Check Point) earns its length; §4 is a genuine UPDATE with new delta (open-sourcing + Phantom Gyp).
- Dedup: CVE-2026-50751 / -42271 / -23111 all new vs prior_coverage_keys.json. TeamPCP/Miasma correctly an UPDATE to 2026-06-06 coverage.

### Verdict
CLEAN

No truth defects, no editorial defects, no advisory flags requiring action. Every inline URL fetched, resolved to a specific article/advisory, and supported its attached claim. The four prior-iteration remediation areas (citation re-points, infection-count removal, confidence-language removal, CVSS/scope corrections, SPA-URL removal) hold in the read I performed.

### Findings summary (machine-readable)
```yaml
# Findings summary (machine-readable) — v2.48
[]
```
