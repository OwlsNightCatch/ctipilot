**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-08T05:00:36Z · ended_at=2026-08-08T05:18:07Z · duration_seconds=1051
**Self-telemetry:** urls_checked=27 · webfetch_calls=13 · bridge_fetches=16

## Verification report — 2026-08-08T0409Z-intel (iteration 1)

Read cold. All 14 entry files read end-to-end (frontmatter + body) plus the run record. Every inline source URL on every entry was fetched in this iteration (WebFetch, `fetch_source.py url`, or the jina rung where the first two failed); the CISA advisory, KEV catalog, CISA CSAF record, NCSC-NL CSAF records and the Flowise sunset page were read directly. All 40 `evidence[]` quotes were tested as contiguous substrings against fetched source text; two apparent misses (Unit 42 `/proc/<pid>/mem`, Check Point "As of now, Cloudflare has not assigned CVEs") were HTML-markup artifacts in the cached raw and are verbatim in the rendered text — not defects. Entity keys, ATT&CK ids against the pinned v19.1 dataset, CVE dedup against `prior_coverage.json`, and `update_of` targets were all checked.

No broken URLs (F1) and no generic/oversight URLs (F2) found. Coverage looks complete: the run-record telemetry's named gaps (google-tag recipe drift, prodaft stale cache, claroty-team82 undated listing, msrc-blog / siemens-productcert-csaf undrilled) do not correspond to any in-window story I can name a plausible source for — Microsoft and Siemens both publish on Patch Tuesday (2026-08-11), outside this window — and every documented drop in `triage.json` is defensibly reasoned. No F10.

### Citation does not support the claim

**F1 — CVE-2026-65400 — macOS Screen Sharing auth-state bypass**

Quoted: "do not treat System Integrity Protection as a compensating control for the network-reachable half of the problem — per fG!'s own analysis of the related daemon bug, SIP does not block that path ([fG!, 2026-07-29](https://reverse.put.as/2026/07/29/its-a-pre-auth-stupid/))"

Inverted. The cited post says the opposite in as many words: 'It would be perfect if it could bypass SIP. That one it doesn't do.' fG!'s SIP-irrelevant remark is about TCC ('this bug doesn't care about TCC either!'), not SIP. The entry appears to have swapped TCC for SIP and then inverted the polarity. Fix: either drop the clause or restate it as 'the bug does not bypass SIP, but it does not care about TCC'.

**F2 — CVE-2026-65400 — macOS Screen Sharing auth-state bypass**

Quoted: "stating he found a pre-authentication bug allowing arbitrary file read and write as root — demonstrated by retrieving /etc/sudoers with no credentials — that Apple's 26.6 release of 2026-07-27 patched but described in its bulletin as a denial-of-service fix"

Three elements are not on the cited page (fetched this iteration). (a) 'write': fG! describes only a 'Go based ARM64 PoC that allows you to download any file' — read/download only; no write primitive is claimed. (b) 'as root': fG! never says root of his own bug; 'root remote command execution' is his description of the OTHER team's blogpost. (c) '26.6 release of 2026-07-27': the string '26.6' does not appear on the page (0 matches) and no date is given — the post says only 'This Monday Apple's Security Bulletin'. Fix: reduce to 'arbitrary file read demonstrated by retrieving /etc/sudoers' and either source the 26.6/2026-07-27 release facts to Apple's own 26.6 bulletin or drop the version and date.

**F3 — Elastic — coding agent reverse tunnel + LaunchAgent persistence**

Quoted: "telemetry from a macOS developer laptop where Claude Code and Cursor, invoked with a permission-bypass flag, authenticated to free reverse-tunnel brokers, stood up a Cloudflare quick tunnel and installed launchd LaunchAgent persistence" / affected_products: ["Anthropic Claude Code", "Cursor"]

Elastic attributes the observed chain to Claude Code alone: 'Elastic Security endpoint telemetry showed shells under Claude Code that scripted a login to an ephemeral tunnel hostname, pulled application metrics, stood up a Cloudflare quick tunnel, and installed LaunchAgent persistence', and 'The activity sits on a macOS developer endpoint where Claude Code (and in related cases Cursor) was already installed'. Cursor appears only as (i) generic framing and (ii) 'Variant B: A Cursor agent session that tried a decrypted keychain dump ... endpoint controls blocked the dump' — a different host, a different behaviour, and blocked. Summary, headline, body and affected_products all bind Cursor to the tunnel/LaunchAgent chain the source does not attribute to it.

**F4 — CPDLC over ATN-B1 — ICSA-26-219-01**

Quoted: "reported to CISA by Martin Strohmeier of armasuisse, the science and technology arm of Switzerland's federal defence procurement office ([CISA, 2026-08-07](https://www.cisa.gov/news-events/ics-advisories/icsa-26-219-01))"

The cited advisory's Acknowledgments section says only 'Martin Strohmeier of Armasuisse reported these vulnerabilities to CISA' — it carries no organisational description. The gloss is also inaccurate: armasuisse IS the Swiss federal office for defence procurement; its research unit is armasuisse Science and Technology. For a Swiss federal readership this misdescribes a sister agency. Fix: 'Martin Strohmeier of armasuisse' or 'of armasuisse Science and Technology'.

### Unsupported / hallucinated facts

**F5 — DPRK Contagious Interview — Flemish Government confirmation**

Quoted: techniques: [T1566.004, T1204.002, T1199, T1078.004]

T1566.004 in the pinned ATT&CK v19.1 dataset is 'Spearphishing Voice'. Neither the entry body nor WIRED describes any voice/vishing vector — the described initial access is a fake job offer delivered as a message plus a downloaded 'coding test' program. No cited source supports a voice component. The behaviour the body does describe maps to T1566.003 (Spearphishing via Service). Replace or drop.

**F6 — Cisco IOS XE August 2026 hardening release**

Quoted: tags: [vulnerabilities, rce, priv-esc, patch-available, no-patch]

The `no-patch` tag contradicts the entry itself. All seven cves[] records carry status: [patch-available] and a `fixed:` value, and the body lists first fixed releases 17.9.10 / 17.12.8 / 17.15.6 / 17.18.4 or 17.18.4a / 26.1.2 (confirmed on the Cisco PSIRT advisory this iteration). What Cisco says is that there are no *workarounds* — a different thing. The tag will render and filter as 'no fix available'. Drop `no-patch`.

**F7 — Run record § Verification & coverage notes — single-source line**

Quoted: "Single-source: five entries ship single-source with the situation named in each sourcing note. Two are national-authority carve-outs ... Three are research labs reporting their own original work — the runtime memory-corruption research, the coding-agent telemetry, and the remote-support-tool distribution campaign"

Seven of this run's fourteen entries carry a single-source* verification value, not five. The enumeration omits chaindrop-oidc-runner-memory-theft-valid-slsa-provenance.md (verification: single-source, Unit 42 only) and wiz-cloud-threat-highlights-h1-2026-ai-toolchain-exposure.md (verification: single-source, Wiz only). Both do carry sourcing_note text, so the fix is the count and the enumeration, not the entries.

**F8 — Run record § Verification & coverage notes — deep-dive paragraph**

Quoted: "An earlier run published no deep dive today either."

Wrong on both halves. runs/2026-08-08/ contains only this run (2026-08-08T0409Z-intel), so there is no earlier run today; and the immediately preceding run, runs/2026-08-07/2026-08-07T0411Z-intel.md, records deep_dive: 2026-08-07/unc6671-blackfile-multi-brand-passkey-vishing-aitm — i.e. the previous fire DID publish a deep dive. Delete or restate the sentence.

### Claims missing inline citation

**F10 — Flowise — three CVEs into a vendor sunset**

Quoted: "CVE-2026-67622 (CWE-639, CVSS 4.0 8.5) ... CVE-2026-67621 (CWE-862, CVSS 4.0 7.2) ..." and "with the company winding down commercial operations"

Two of the three CVEs, and the entry's central framing, rest on pages that are not in sources[]. (a) The per-CVE scores, CWEs and descriptions for CVE-2026-67622 and CVE-2026-67621 (in the body AND in frontmatter cves[]) come from VulnCheck advisories the entry never cites — both fetched live this iteration: https://www.vulncheck.com/advisories/flowise-idor-in-openai-assistants-integration (CVE-2026-67622, CWE-639, CVSS 4.0 8.5) and https://www.vulncheck.com/advisories/flowise-missing-authorization-on-document-store-mutation-endpoints (CVE-2026-67621, CWE-862, CVSS 4.0 7.2); the one cited VulnCheck URL covers CVE-2026-70636 only, and BSI publishes a single advisory-level 7.7 with no per-CVE breakdown (confirmed on WID-SEC-2026-2703). (b) The wind-down claim in title, headline, summary and body traces to https://flowiseai.com/sunset ('we've decided to wind down our operations for Flowise'; announcement/code freeze 2026-07-29; archival 2026-08-10; EOL 2026-08-31), which is fetchable and not cited. Add the two per-CVE VulnCheck advisory URLs and the sunset page to sources[].

**F11 — CVE-2026-8037 — Kemp LoadMaster KEV addition**

Quoted: cves[].fixed: "GA 7.2.63.2 / LTSF 7.2.54.18" (also in actions[])

The LTSF fixed release 7.2.54.18 appears in neither cited source. The watchTowr post (fetched this iteration) gives GA 7.2.63.2 as fixed and mentions only 7.2.54.17 on the LTSF train (as affected); the CISA KEV alert and the KEV catalog record for CVE-2026-8037 carry no version numbers at all. The value is correct against third-party reporting, so this is a sourcing gap rather than an invention — the KEV record's own notes field links the Progress bulletin (https://community.progress.com/s/article/LoadMaster-Critical-Security-Bulletin-June-2026-CVE-2026-8037-CVE-2026-33691), which is the natural citation to add. (Note: that Progress URL returns a JS shell to the bridge and 403s the jina reader, so verify before citing.)

### Quantifier without source

**F9 — Flowise — three CVEs into a vendor sunset**

Quoted: "Langflow reached the exploited-vulnerabilities catalog three times in as many weeks"

No citation, and the CISA KEV catalog (re-read this iteration) does not support the timeframe: Langflow KEV additions are CVE-2026-55255 dateAdded 2026-07-07, CVE-2026-0770 dateAdded 2026-07-21 and CVE-2026-9198 dateAdded 2026-08-04 — three additions spanning four weeks at fortnightly intervals, not 'three times in as many weeks'. Either restate as 'three times in the last month' with a citation, or drop the aside.

### Action-item discipline

**F12 — Elastic — coding agent reverse tunnel + LaunchAgent persistence**

Quoted: "Alert on LaunchAgent creation or modification (launchctl bootstrap, PlistBuddy writes under ~/Library/LaunchAgents) where the parent lineage is a coding-agent process, and pair it with credentialed egress to reverse-tunnel broker domains from the same tree — Elastic's finding is that either signal alone is noise on a developer endpoint and the pair is not."

Fails 10b(b): a standing detection-engineering idea restating the body, not a start-now task. The body's Defender takeaway already names the same three keyed signals ('credentialed connections to reverse-tunnel broker infrastructure originating anywhere in a coding-agent process tree; LaunchAgent creation or modification under a coding-agent ancestor; and any agent-parented listener made durable across reboot'). Either drop to actions: [] (legitimate for a research/awareness entry) or replace with the one concrete task the entry does support — inventory which developer endpoints have coding agents configured with permission-bypass flags.

### Editorial / less-is-more flags (advisory)

**F13 — Check Point — workerd native-glue memory corruption**

Quoted: headline: "Five memory-corruption bugs in the C++ layer between JavaScript and native code..." / summary: "five memory-corruption vulnerabilities in workerd" vs body: "A separate SQL authorization-bypass path reaches arbitrary deserialization."

Advisory. The source's 'short version' does say 'We found five memory-corruption bugs', so the entry is not wrong to quote it — but the same article's §10 says 'The other four bugs are memory-corruption. This one is a classic that leads to arbitrary deserialization', and the entry's own body describes the fifth as a SQL authorization bypass. Headline and summary therefore contradict the body. Cheapest fix: 'five vulnerabilities ... four of them memory-corruption'. Main agent may leave this.

**F14 — CVE-2026-65400 — macOS Screen Sharing auth-state bypass**

Quoted: cves[].cvss: null / sourcing_note: "Apple publishes no CVSS score for CVE-2026-65400, so none is recorded."

Advisory. The statement about Apple is correct, but the entry's own corroborating source does publish a score: NCSC-2026-0280 records 'CVE-2026-65400 - CVSS (v3) 7.1' (read via the CSAF-backed advisory this iteration). Consider recording 7.1 with the CERT provenance noted, or say explicitly in the sourcing_note that NCSC-NL's 7.1 was not adopted.


### Verdict

NEEDS_FIXES (truth: 9, editorial: 3, advisory: 2)

Truth = F1–F4 (claim-not-supported), F5–F8 (hallucinated-fact), F9 (quantifier-without-source). Editorial = F10–F11 (missing-citation), F12 (action-item-discipline). Advisory = F13–F14.

The single most dangerous defect is **F1**: the macOS entry tells a defender that SIP does not block the screensharingd path when the cited researcher says in as many words that his bug cannot bypass SIP. That is an inverted safety claim on a hardening recommendation and must be fixed before publish. **F3** (Cursor bound to a chain Elastic attributes to Claude Code) and **F5** (Spearphishing *Voice* on a fake-job-offer campaign) are the next most consequential — both corrupt downstream consumers (`affected_products[]`, the ATT&CK overlap matrix).

Everything else in the run verified clean: the KEV addition and catalog text, the CCB/V4bel KVM pair including both preconditions and the assignment date, the NCSC-CH advisory including the RPC-provider recommendation, the entire Unit 42 CHAINDROP mechanic chain (opensearch-js gate, trusted-publishing exchange, Fulcio/Rekor, "not forged provenance", the "we did not observe this path execute" caveat), the WIRED figures and every quoted statement, all seven Cisco CVE/CWE/score pairings and the aggregate vector, all five CPDLC CVEs with per-CVE CWE and CVSS plus the CSAF `none_available` remediation and lab-setting assessment, the Beacon/Victim Support/Infosecurity chain, the LevelBlue campaign mechanics, and every Wiz quotation. Dedup, `update_of` targets and entity keys are all correct.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F1
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-65400 — macOS Screen Sharing auth-state bypass"
  url_or_quote: "\"do not treat System Integrity Protection as a compensating control for the network-reachable half of the problem — per fG!'s own analysis of the related daemon bug, SIP does not block that path ([fG!, 2026-07-29](https://reverse.put.as/2026/07/29/its-a-pre-auth-stupid/))\""
  summary: "Inverted. The cited post says the opposite in as many words: 'It would be perfect if it could bypass SIP. That one it doesn't do.' fG!'s SIP-irrelevant remark is about TCC ('this bug doesn't care about TCC either!'), not SIP. The entry appears to have swapped TCC for SIP and then inverted the polarity. Fix: either drop the clause or restate it as 'the bug does not bypass SIP, but it does not care about TCC'."
- code: F2
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-65400 — macOS Screen Sharing auth-state bypass"
  url_or_quote: "\"stating he found a pre-authentication bug allowing arbitrary file read and write as root — demonstrated by retrieving /etc/sudoers with no credentials — that Apple's 26.6 release of 2026-07-27 patched but described in its bulletin as a denial-of-service fix\""
  summary: "Three elements are not on the cited page (fetched this iteration). (a) 'write': fG! describes only a 'Go based ARM64 PoC that allows you to download any file' — read/download only; no write primitive is claimed. (b) 'as root': fG! never says root of his own bug; 'root remote command execution' is his description of the OTHER team's blogpost. (c) '26.6 release of 2026-07-27': the string '26.6' does not appear on the page (0 matches) and no date is given — the post says only 'This Monday Apple's Security Bulletin'. Fix: reduce to 'arbitrary file read demonstrated by retrieving /etc/sudoers' and either source the 26.6/2026-07-27 release facts to Apple's own 26.6 bulletin or drop the version and date."
- code: F3
  category: claim-not-supported
  section: research
  item: "Elastic — coding agent reverse tunnel + LaunchAgent persistence"
  url_or_quote: "\"telemetry from a macOS developer laptop where Claude Code and Cursor, invoked with a permission-bypass flag, authenticated to free reverse-tunnel brokers, stood up a Cloudflare quick tunnel and installed launchd LaunchAgent persistence\" / affected_products: [\"Anthropic Claude Code\", \"Cursor\"]"
  summary: "Elastic attributes the observed chain to Claude Code alone: 'Elastic Security endpoint telemetry showed shells under Claude Code that scripted a login to an ephemeral tunnel hostname, pulled application metrics, stood up a Cloudflare quick tunnel, and installed LaunchAgent persistence', and 'The activity sits on a macOS developer endpoint where Claude Code (and in related cases Cursor) was already installed'. Cursor appears only as (i) generic framing and (ii) 'Variant B: A Cursor agent session that tried a decrypted keychain dump ... endpoint controls blocked the dump' — a different host, a different behaviour, and blocked. Summary, headline, body and affected_products all bind Cursor to the tunnel/LaunchAgent chain the source does not attribute to it."
- code: F4
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CPDLC over ATN-B1 — ICSA-26-219-01"
  url_or_quote: "\"reported to CISA by Martin Strohmeier of armasuisse, the science and technology arm of Switzerland's federal defence procurement office ([CISA, 2026-08-07](https://www.cisa.gov/news-events/ics-advisories/icsa-26-219-01))\""
  summary: "The cited advisory's Acknowledgments section says only 'Martin Strohmeier of Armasuisse reported these vulnerabilities to CISA' — it carries no organisational description. The gloss is also inaccurate: armasuisse IS the Swiss federal office for defence procurement; its research unit is armasuisse Science and Technology. For a Swiss federal readership this misdescribes a sister agency. Fix: 'Martin Strohmeier of armasuisse' or 'of armasuisse Science and Technology'."
- code: F5
  category: hallucinated-fact
  section: incidents
  item: "DPRK Contagious Interview — Flemish Government confirmation"
  url_or_quote: "techniques: [T1566.004, T1204.002, T1199, T1078.004]"
  summary: "T1566.004 in the pinned ATT&CK v19.1 dataset is 'Spearphishing Voice'. Neither the entry body nor WIRED describes any voice/vishing vector — the described initial access is a fake job offer delivered as a message plus a downloaded 'coding test' program. No cited source supports a voice component. The behaviour the body does describe maps to T1566.003 (Spearphishing via Service). Replace or drop."
- code: F6
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "Cisco IOS XE August 2026 hardening release"
  url_or_quote: "tags: [vulnerabilities, rce, priv-esc, patch-available, no-patch]"
  summary: "The `no-patch` tag contradicts the entry itself. All seven cves[] records carry status: [patch-available] and a `fixed:` value, and the body lists first fixed releases 17.9.10 / 17.12.8 / 17.15.6 / 17.18.4 or 17.18.4a / 26.1.2 (confirmed on the Cisco PSIRT advisory this iteration). What Cisco says is that there are no *workarounds* — a different thing. The tag will render and filter as 'no fix available'. Drop `no-patch`."
- code: F7
  category: hallucinated-fact
  section: run-record
  item: "Run record § Verification & coverage notes — single-source line"
  url_or_quote: "\"Single-source: five entries ship single-source with the situation named in each sourcing note. Two are national-authority carve-outs ... Three are research labs reporting their own original work — the runtime memory-corruption research, the coding-agent telemetry, and the remote-support-tool distribution campaign\""
  summary: "Seven of this run's fourteen entries carry a single-source* verification value, not five. The enumeration omits chaindrop-oidc-runner-memory-theft-valid-slsa-provenance.md (verification: single-source, Unit 42 only) and wiz-cloud-threat-highlights-h1-2026-ai-toolchain-exposure.md (verification: single-source, Wiz only). Both do carry sourcing_note text, so the fix is the count and the enumeration, not the entries."
- code: F8
  category: hallucinated-fact
  section: run-record
  item: "Run record § Verification & coverage notes — deep-dive paragraph"
  url_or_quote: "\"An earlier run published no deep dive today either.\""
  summary: "Wrong on both halves. runs/2026-08-08/ contains only this run (2026-08-08T0409Z-intel), so there is no earlier run today; and the immediately preceding run, runs/2026-08-07/2026-08-07T0411Z-intel.md, records deep_dive: 2026-08-07/unc6671-blackfile-multi-brand-passkey-vishing-aitm — i.e. the previous fire DID publish a deep dive. Delete or restate the sentence."
- code: F9
  category: quantifier-without-source
  section: trending-vulnerabilities
  item: "Flowise — three CVEs into a vendor sunset"
  url_or_quote: "\"Langflow reached the exploited-vulnerabilities catalog three times in as many weeks\""
  summary: "No citation, and the CISA KEV catalog (re-read this iteration) does not support the timeframe: Langflow KEV additions are CVE-2026-55255 dateAdded 2026-07-07, CVE-2026-0770 dateAdded 2026-07-21 and CVE-2026-9198 dateAdded 2026-08-04 — three additions spanning four weeks at fortnightly intervals, not 'three times in as many weeks'. Either restate as 'three times in the last month' with a citation, or drop the aside."
- code: F10
  category: missing-citation
  section: trending-vulnerabilities
  item: "Flowise — three CVEs into a vendor sunset"
  url_or_quote: "\"CVE-2026-67622 (CWE-639, CVSS 4.0 8.5) ... CVE-2026-67621 (CWE-862, CVSS 4.0 7.2) ...\" and \"with the company winding down commercial operations\""
  summary: "Two of the three CVEs, and the entry's central framing, rest on pages that are not in sources[]. (a) The per-CVE scores, CWEs and descriptions for CVE-2026-67622 and CVE-2026-67621 (in the body AND in frontmatter cves[]) come from VulnCheck advisories the entry never cites — both fetched live this iteration: https://www.vulncheck.com/advisories/flowise-idor-in-openai-assistants-integration (CVE-2026-67622, CWE-639, CVSS 4.0 8.5) and https://www.vulncheck.com/advisories/flowise-missing-authorization-on-document-store-mutation-endpoints (CVE-2026-67621, CWE-862, CVSS 4.0 7.2); the one cited VulnCheck URL covers CVE-2026-70636 only, and BSI publishes a single advisory-level 7.7 with no per-CVE breakdown (confirmed on WID-SEC-2026-2703). (b) The wind-down claim in title, headline, summary and body traces to https://flowiseai.com/sunset ('we've decided to wind down our operations for Flowise'; announcement/code freeze 2026-07-29; archival 2026-08-10; EOL 2026-08-31), which is fetchable and not cited. Add the two per-CVE VulnCheck advisory URLs and the sunset page to sources[]."
- code: F11
  category: missing-citation
  section: trending-vulnerabilities
  item: "CVE-2026-8037 — Kemp LoadMaster KEV addition"
  url_or_quote: "cves[].fixed: \"GA 7.2.63.2 / LTSF 7.2.54.18\" (also in actions[])"
  summary: "The LTSF fixed release 7.2.54.18 appears in neither cited source. The watchTowr post (fetched this iteration) gives GA 7.2.63.2 as fixed and mentions only 7.2.54.17 on the LTSF train (as affected); the CISA KEV alert and the KEV catalog record for CVE-2026-8037 carry no version numbers at all. The value is correct against third-party reporting, so this is a sourcing gap rather than an invention — the KEV record's own notes field links the Progress bulletin (https://community.progress.com/s/article/LoadMaster-Critical-Security-Bulletin-June-2026-CVE-2026-8037-CVE-2026-33691), which is the natural citation to add. (Note: that Progress URL returns a JS shell to the bridge and 403s the jina reader, so verify before citing.)"
- code: F12
  category: action-item-discipline
  section: research
  item: "Elastic — coding agent reverse tunnel + LaunchAgent persistence"
  url_or_quote: "\"Alert on LaunchAgent creation or modification (launchctl bootstrap, PlistBuddy writes under ~/Library/LaunchAgents) where the parent lineage is a coding-agent process, and pair it with credentialed egress to reverse-tunnel broker domains from the same tree — Elastic's finding is that either signal alone is noise on a developer endpoint and the pair is not.\""
  summary: "Fails 10b(b): a standing detection-engineering idea restating the body, not a start-now task. The body's Defender takeaway already names the same three keyed signals ('credentialed connections to reverse-tunnel broker infrastructure originating anywhere in a coding-agent process tree; LaunchAgent creation or modification under a coding-agent ancestor; and any agent-parented listener made durable across reboot'). Either drop to actions: [] (legitimate for a research/awareness entry) or replace with the one concrete task the entry does support — inventory which developer endpoints have coding agents configured with permission-bypass flags."
- code: F13
  category: editorial-advisory
  section: research
  item: "Check Point — workerd native-glue memory corruption"
  url_or_quote: "headline: \"Five memory-corruption bugs in the C++ layer between JavaScript and native code...\" / summary: \"five memory-corruption vulnerabilities in workerd\" vs body: \"A separate SQL authorization-bypass path reaches arbitrary deserialization.\""
  summary: "Advisory. The source's 'short version' does say 'We found five memory-corruption bugs', so the entry is not wrong to quote it — but the same article's §10 says 'The other four bugs are memory-corruption. This one is a classic that leads to arbitrary deserialization', and the entry's own body describes the fifth as a SQL authorization bypass. Headline and summary therefore contradict the body. Cheapest fix: 'five vulnerabilities ... four of them memory-corruption'. Main agent may leave this."
- code: F14
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CVE-2026-65400 — macOS Screen Sharing auth-state bypass"
  url_or_quote: "cves[].cvss: null / sourcing_note: \"Apple publishes no CVSS score for CVE-2026-65400, so none is recorded.\""
  summary: "Advisory. The statement about Apple is correct, but the entry's own corroborating source does publish a score: NCSC-2026-0280 records 'CVE-2026-65400 - CVSS (v3) 7.1' (read via the CSAF-backed advisory this iteration). Consider recording 7.1 with the CERT provenance noted, or say explicitly in the sourcing_note that NCSC-NL's 7.1 was not adopted."
```
