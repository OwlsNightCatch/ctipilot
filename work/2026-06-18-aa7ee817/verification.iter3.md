**Model:** Anthropic Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-18T04:53:26Z · ended_at=2026-06-18T04:57:09Z · duration_seconds=223

## Verification report — briefs/2026-06-18.md (iteration 3)

Cold read by a hostile, technically-fluent Swiss/EU public-sector SOC reviewer. Env vars `CLAUDE_FRIENDLY_NAME` / `CLAUDE_MODEL_ID` were unset; identity reported from runtime.

Every cited Source/Additional-source URL in the brief was `WebFetch`ed (or fetched via `tools/fetch_source.py` for Oracle/CISA/NCSC-CH/cert-bund) this iteration, except the BSI cert-bund advisory (known-403 national-CERT host; see § note below). Named CVEs, CVSS scores, actors, products, versions, dates and counts were cross-checked against the fetched sources.

### Unsupported / hallucinated facts

**F4 — § 3 JetBrains plugin item asserts "Aikido reported its findings to JetBrains"; neither cited source supports it.**
- Quoted claim: *"Aikido reported its findings to JetBrains; defenders should **not** assume the plugins have been removed from the Marketplace…"*
- Cited sources on the item: Aikido Security (`https://www.aikido.dev/blog/multiple-jetbrains-ide-plugins-caught-stealing-ai-keys`) and Infosecurity Magazine (`https://www.infosecurity-magazine.com/news/fifteen-jetbrains-marketplace/`).
- I fetched both this iteration. The Aikido page documents the 15 plugins, 7 vendor accounts, ~70,000 installs, key-exfil-on-Apply mechanism, resale-as-discounted-access, and names CodeGPT AI Assistant / DeepSeek AI Assist as the two largest — all of which the brief states correctly. But the Aikido page does **not** state that Aikido notified JetBrains; it says only that Aikido "shared the relevant IoCs in its blog post." The Infosecurity Magazine article likewise "does not explicitly state whether Aikido reported findings to JetBrains."
- The downstream caution ("do not assume the plugins have been removed") is fine as the brief's own analyst caveat — neither source addresses removal status, and the brief frames it as a defender caution, not a sourced fact. The defect is the affirmative antecedent "Aikido reported its findings to JetBrains," which is presented as fact with no source support.
- Remediation: drop the "Aikido reported its findings to JetBrains" clause, or replace with a sourced statement (Aikido published IoCs in its blog post). The surrounding caution can stand.

### Editorial / less-is-more flags (advisory)

**F11 — minor source-date drift (advisory, no action required).** A few item datelines are one day ahead of the underlying page's publish date but the articles fully support every claim and the dates do not affect any operational conclusion: Genians item cited "2026-06-16" (page header reads 2026-06-15); THN NarwhalLRAT cited "2026-06-17" (page reads 2026-06-16); Zammad item says the release shipped "2026-06-16" (the release page reads 2026-06-17, and the BSI advisory is 2026-06-17). These are within tolerance; flagged only for the record, not as a fix.

**F11 — "~1.1 million combined weekly downloads" for Mastra (§ 5, advisory).** JFrog did not state a download figure; Socket states `@mastra/core` alone is 918K weekly. "Roughly 1.1 million combined" across the 140+-package scope is a reasonable aggregation and is qualified with "roughly," so it stands; noted only because no single cited line gives the 1.1M figure verbatim.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 2)

Single truth defect: F4 (unsupported "reported to JetBrains" clause). Everything else in the brief verified cleanly against fetched primaries:

- **FortiBleed (§0/§1/§6):** Russian-speaking actor + Active-Directory lateral movement correctly attributed to BleepingComputer; 194-country reach to Arctic Wolf; 73,932 URLs / 21,632 domains / ~75,000 devices / "not a new vulnerability" (Fortinet statement) all supported. § 7 sourcing-precision note (Arctic Wolf carries the SHA-256→PBKDF2 hash weakness, which the brief does NOT rely on) is accurate.
- **Oracle (§0/§2/table):** 245 fixes + ~100 unauth → SecurityWeek; CVE-2026-46978 (Solaris Remote Administration Daemon, HTTPS, unauth, CVSS 10.0, 11.4) and CVE-2026-35278 (PeopleSoft PT PeopleTools Performance Monitor, HTTP, unauth, CVSS 9.8, 8.61/8.62) both confirmed against the Oracle CSPU advisory table.
- **Rockwell (§0/§2/table):** CVE-2026-0647 (9.4, 1794-AENTR/AENTRXT, ≤V2.012, fixed 2.013/SD1775, crafted HTTP GET) and CVE-2026-0646 (7.5 CIP DoS) → CISA ICSA-26-167-05; CVE-2026-11317 (7.5, CompactLogix/ControlLogix 5370/5570) → CISA ICSA-26-167-03; CVE-2025-13036 (7.7, FactoryTalk Historian Site Edition auth bypass) → NCSC-CH post 12639. All confirmed.
- **ScarCruft/NarwhalRAT (§0/§1):** APT37 attribution, NarwhalRAT name, fake-Microsoft-OTP lure, LNK→PowerShell -ExecutionPolicy Bypass, one-minute scheduled task, compiled-Python (keylog/screenshot/audio/USB), pCloud dead-drop resolver → Genians + THN.
- **China / Silver Fox (§1):** 67 arrests, 5 provinces, aliases (Void Arachne / UTG-Q-1000 / TA4922), full-supply-chain roles, Winos/ValleyRAT, CNCERT/CC 2026-05-22 alert → Risky Biz News + CNCERT/CC (both fetched; CNCERT URL resolves to the Silver Fox advisory).
- **Crypto clipboard hijacker (§3):** Rust Win+macOS payloads, GitHub/SourceForge/YouTube/Telegram ghost network, WordPress phishing hub, VirusTotal community-vote manipulation, Solana/Pump.fun/Aviator lures → Check Point Research + THN.
- **Mastra deep dive (§5):** postinstall `node setup.cjs`, `NODE_TLS_REJECT_UNAUTHORIZED=0`, stage-2 cross-platform backdoor, wallet-extension enumeration, LaunchAgent/systemd-user/HKCU-Run persistence masquerading as NVM/Node, 140+ packages, ~88-minute sweep, clean-then-malicious easy-day-js@1.11.22, undisclosed publish-account vector (correctly stated as undisclosed) → JFrog + Socket.

**Sourcing-strength note:** primary sources are vendor research labs / PSIRT-equivalent / national-CERT throughout; no NVD/MITRE-only footers; no homepages/listing indexes. No IOCs in prose, no vanity metrics, no contradictions, English throughout, no workflow-internal language. § 1 leads CH/EU-relevant; § 2 inclusion gates (CVSS 9+, pre-auth, OT with NCSC-CH flag) honoured. Deep dive earns its length. Deliberate-exclusion notes (RoguePlanet, DragonForce Teams-TURN, ShinyHunters/CVE-2026-35273) are sound and consistent with the dedup context.

**National-CERT single-source note (not a finding):** the Zammad § 2 item's first Source is the BSI CERT-Bund advisory WID-SEC-2026-1981, a known-403 host I could not fetch this iteration. It is corroborated by the Zammad 7.1 release page (fetched — confirms 13 GitHub Security Advisories and the security nature of the release). BSI is a HIGH-reliability national CERT acting as a regional public-sector disclosing party; the severity-language claim ("hoch"/admin-priv chain) is consistent with BSI advisory conventions and is appropriately backed by a second source for the 13-advisory count. No `[SINGLE-SOURCE]` flag required.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F4
  category: hallucinated-fact
  section: research
  item: "15 malicious JetBrains Marketplace plugins exfiltrate AI provider API keys on Apply"
  url_or_quote: "Aikido reported its findings to JetBrains; defenders should not assume the plugins have been removed from the Marketplace"
  summary: "Affirmative claim 'Aikido reported its findings to JetBrains' is unsupported — fetched Aikido blog says only it 'shared the relevant IoCs in its blog post'; Infosecurity Magazine does not state any JetBrains notification. Drop the clause or replace with the sourced 'published IoCs' statement; the 'do not assume removed' caution can stand as analyst caveat."
- code: F11
  category: editorial-advisory
  section: multiple
  item: "Source-date drift (Genians, THN NarwhalRAT, Zammad release) and Mastra ~1.1M combined-downloads figure"
  url_or_quote: "various datelines off by one day; '~1.1 million combined weekly downloads'"
  summary: "Advisory only. Datelines one day ahead of underlying pages but claims fully supported and operationally unaffected; '~1.1M combined' is a reasonable qualified aggregation (Socket gives 918K for @mastra/core alone). No fix required."
```
