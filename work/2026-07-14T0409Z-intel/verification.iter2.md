**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-14T04:52:14Z · ended_at=2026-07-14T04:59:30Z · duration_seconds=436
**Self-telemetry:** urls_checked=7 · webfetch_calls=5 · bridge_fetches=2 · websearch_calls=1

## Verification report — 2026-07-14T0409Z-intel (iteration 2)

Cold read of all 3 new entries + run record. Verified the iteration-1 remediations
first, then independently re-verified every cited URL and every `techniques[]` id
against fetched source text and body prose.

### Prior-iteration deltas verified

- **F4 remediation (CrashStealer "since-revoked Developer ID") — CONFIRMED FIXED.**
  Re-fetched the Jamf blog with a targeted prompt: the article states *"After
  confirming that the Developer Team ID was used to distribute malicious payloads,
  Jamf Threat Labs reported it to Apple"* and separately *"it is a universal (arm64
  and x86_64) binary signed with the Developer ID `Emil Grigorov (WWB7JA7AQV)`, has
  hardened runtime enabled, and carries a stapled notarization ticket"* — no mention
  anywhere of revocation. The entry's current phrasing — "a valid Developer ID —
  which Jamf reported to Apple after confirming it was used to distribute malicious
  payloads — with hardened runtime enabled" — is a precise paraphrase of exactly
  that Jamf sentence, with no revocation claim remaining. Clean.
- **F11 remediation (`mobile` tag → `identity`) — CONFIRMED FIXED.** `tags:
  [infostealer, identity]`. Both terms are in `site/taxonomy.yaml`'s theme list;
  "identity" correctly reflects the credential/keychain-theft core behaviour.
  No `mobile` tag remains.

### Unsupported / hallucinated facts

- **F4 — CrashStealer: three `techniques[]` ids have zero matching body prose.**
  `techniques: [... T1622, T1027, ... T1560.001 ...]` are mapped in frontmatter, and
  all three ARE genuinely supported by the Jamf source (confirmed by a targeted
  re-fetch this iteration: *"A constructor that runs before `main` ... uses `sysctl`
  with a `KERN_PROC` / `P_TRACED` query"* and *"a second check later in application
  initialization exits the same way"* for T1622; *"Control-flow flattening and
  encrypted strings complement the anti-debugging measures"* for T1027; and *"The
  malware packages collected data into ZIP archives before exfiltration ... 'shells
  out to the `zip` utility' to create hidden archives with a `.zx_` prefix ...
  written to `~/.cache/com.apple.crashreporter/`"* for T1560.001 — Archive via
  Utility) — but the entry BODY never once mentions debugging/anti-debug, control-flow
  flattening/string encryption, or any archiving/zip step (`grep -in
  "debug|zip|archive|packing|obfuscat"` on the entry returns zero hits). The body
  goes straight from "collects browser data ... password-manager material" to
  "AES-GCM-encrypting the staged files and exfiltrating them over `libcurl`", skipping
  the archiving step entirely, and the anti-debugging/obfuscation tradecraft — genuinely
  interesting defensive material (exit code 45 on debugger detection is a concrete,
  reproducible indicator) — never appears in prose at all, only as a disconnected
  frontmatter `evidence[]` quote that the body text never echoes. Per the hard rule
  ("the body describes each mapped behavior in plain language and must read complete
  without a single T-number") and check 4b ("an id with no matching body behavior ...
  is F4"), this is a genuine frontmatter⇔body mismatch on 3 of 14 mapped techniques.
  Fix: add 1-2 sentences describing the zip-archival step (a `zip` process spawned by
  the crashreporter-impersonating app writing to a hidden `.zx_*.zip` path under
  `~/.cache` is itself a strong, addable detection hook) and the anti-debug/obfuscation
  behaviour (constructor-time `sysctl KERN_PROC/P_TRACED` check + a second later check,
  both exiting with code 45; control-flow flattening + encrypted strings) — all
  Jamf-sourced, not fabricated, just currently undescribed.

- **F4 — OFAC/1VPNS entry: `T1090.003` (Multi-hop Proxy) is not supported by any
  cited source or the body prose.** `techniques: [T1090.003, T1027.002]`. I re-fetched
  all three cited sources this iteration: the Treasury press release (sb0559)
  describes 1VPNS only as "a virtual private network (VPN) provider selling services
  to ransomware groups" that let actors "hide the origins of their attacks, deploy
  malware, and manage exfiltrated data"; the FBI Boston release states the service
  "allowed users to route internet traffic through servers in approximately 27
  different countries"; neither describes proxy **chaining** (two-or-more hops in
  sequence) — MITRE's Multi-hop Proxy subtechnique specifically covers an adversary
  chaining multiple proxies/relays (the canonical example is Tor), which is distinct
  from a commercial VPN offering exit-node choice across many countries. The entry
  body itself never describes any proxy mechanism at all (it only calls 1VPNS "the
  Russian-language, no-log criminal anonymisation service" and discusses the sanctions
  administratively) — so there is neither a source basis nor a body-prose basis for
  the specific "multi-hop" claim. `T1090` (Proxy) or `T1090.002` (External Proxy —
  the standard mapping for a commercial/third-party anonymization service an
  adversary rents rather than builds) both fit the cited facts better. Fix: retarget
  to `T1090` or `T1090.002`, or add a sourced sentence establishing actual multi-hop
  chaining if a source supports it. `T1027.002` (Software Packing) is correctly
  supported — Treasury's own quoted language ("built specifically to make malware
  stealthier ... by disguising it as harmless files") is in the evidence[] and maps
  cleanly.

### Editorial / less-is-more flags (advisory)

- **F11 — Run record body: workflow-internal language leaked into the published
  verification notes.** Per `docs/pipeline.md` § Run records, the run record's body
  ("the human-readable verification & coverage notes") is exactly what "the rendered
  window brief concatenates ... as its § Verification Notes" — i.e., this text is
  reader-facing, not internal telemetry. The opening sentence of the body reads:
  *"All four Phase 1 research sub-agents (S1–S4) returned within cap; no S5 (no
  in-window `intel/` drops)."* This is precisely the workflow-internal vocabulary
  ("Phase N", "sub-agents") that check 12 / CLAUDE.md's hard rule prohibits from
  leaking into any entry or the run-record notes ("no workflow-internal language...
  leaking into any entry or the run-record notes"). Iteration 1's report explicitly
  claimed "Style clean: ... no workflow-internal language" — that claim was
  incorrect; the sentence is present verbatim in the body I read. Fix: rephrase to
  reader-facing language, e.g. "All four research workstreams returned within budget;
  no fifth workstream needed (no in-window closed-source intake)." Advisory-severity
  because it is a single sentence in run-record framing prose, not an entry, and
  doesn't misstate any fact — but it is a real, quotable instance of the prohibited
  pattern and should be cleaned up.

### Items checked and CLEARED (no finding)

- **CrashStealer** — all cited URLs (Jamf blog, BleepingComputer) live and specific;
  re-confirmed via targeted re-fetch that the Developer-ID phrasing, the "right-click
  → Open" social-engineering framing, the GitHub→base64→bash delivery chain, the
  `dscl -authonly` password-validation loop, the EDR-tooling reconnaissance sweep, and
  the hidden `/private/tmp`/`~/.cache` staging paths are all Jamf/BleepingComputer-
  supported. Remaining 11 of 14 `techniques[]` ids (T1204.002, T1553.001, T1140,
  T1105, T1543.001, T1518.001, T1555.001, T1555.003, T1564.001, T1041, T1070.006) all
  have clear matching body prose and source support. No IOCs leaked (C2 IP, domains
  present in source, none in entry). `event_date` matches the Jamf byline (2026-07-13).
  `verification: multi-source` / credibility-held-at-2 handling and `sourcing_note`
  are accurate and disclosed.
- **Check Point AI Security Report 2026** — re-fetched with targeted prompts; both
  `evidence[]` quotes verbatim ("AI has crossed from assistant to operator." /
  "the durable bypass is now a planted configuration file an agent loads and trusts
  across sessions."); VoidLink 88k-line C2 in "under a week," China-nexus campaign +
  Mexican-government breach, PhaaS with jailbroken LLMs, voice-agent vishing, the
  March–May "fivefold" payload-length rise (entry correctly omits the vanity number
  and keeps "climbing sharply"), and "most actors favor jailbroken mainstream models
  over self-hosted ones" all independently confirmed present and accurately
  paraphrased. `techniques[]` (T1587.001, T1566) both have matching body prose and
  source support. Percentages correctly flagged in the Defender-takeaway paragraph as
  CPR's own product telemetry. `single-source` + `sourcing_note` correct; B2
  classification matches `sources.json`'s `checkpoint-research: B` reliability code.
  Distinct registry entity from CPR's earlier March–April AI Threat Landscape Digest
  (`report:checkpoint-research-ai-threat-landscape-march-april-2026-...`) — the
  Mexican-government-breach example the new report cites overlaps that earlier
  digest's finding, but the new entry is about the new annual report's own
  publication and framing, not a re-report of the Mexican breach itself; not flagged.
- **OFAC/UK 1VPNS sanctions (UPDATE)** — re-fetched all three cited sources (Treasury
  press release sb0559, OFAC SDN listing 20260713, FBI Boston release). All three
  `evidence[]` quotes verbatim-confirmed, including the FBI's "assistance from
  Ukraine, the United Kingdom, Switzerland, and Luxembourg" line. Rashevskyi aliases
  ("Maksim Sorin"/"Roman Chabanenko") and Silayev's Belarusian nationality confirmed
  on the SDN listing (spelled "Yevgeniy" on the SDN entry vs "Yegeniy" in the Treasury
  press release's own prose — the entry follows the primary press release's spelling,
  not an entry error). `update_of` the 2026-05-22 Operation Saffron entry file exists
  and is the correct target; registry aliases extended (not duplicated) with "First
  VPN Service"/"1VPNS"; no orphan `tool:first-vpn-service-1vpns` entity was created
  despite that draft key appearing in `triage.json` — correctly resolved to the
  existing incident entity at compose time. Delta-only body, no recap padding.
  Classification A1 justified (two independent first-party government sources
  corroborating each other). `actions: []` correct — no do-now action, entry says so.
  No IOCs.

### Coverage / whole-run

Reviewed `triage.json` drops against the run record narrative — same conclusions as
disclosed (SAP Patch Day, DIRAC, Swiss M365/OpenDesk deferred to weekly, Compass CRA,
Lidl, D1R, Qilin/CCCM). A brief independent web search for Swiss-nexus incidents in
the 2026-07-13/14 window surfaced only already-covered, older (June 2026) Swiss
ransomware items (AiLock/Schneebeli, Icarus/Gms-net, Akira/Groupe 3R) — nothing new
or in-window found. No additional missed angle identified beyond what's logged.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 1)

Both truth findings are technique-mapping/body-prose gaps (not hallucinations — the
underlying facts ARE source-supported) and are straightforward to remediate: add
~2 sentences to CrashStealer's body for the anti-debug/obfuscation/archiving
tradecraft, and retarget the OFAC entry's T1090.003 to T1090/T1090.002 (or add a
sourced multi-hop claim). The advisory finding is a one-sentence run-record wording
fix. The two remediations verified from iteration 1 (Developer-ID phrasing, mobile
tag) both landed correctly and cleanly.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "CrashStealer — native-C++ macOS infostealer"
  url_or_quote: "techniques: [T1622, T1027, T1560.001]"
  summary: "Three of 14 mapped techniques (Debugger Evasion, Obfuscated Files or Information, Archive via Utility) are genuinely Jamf-sourced but have zero matching body prose — the body never mentions anti-debugging, control-flow flattening/string encryption, or the zip-archival step before AES-GCM encryption. Add 1-2 sourced sentences describing these behaviors; do not remove the technique ids (they are source-supported)."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "OFAC and the UK sanction First VPN Service (1VPNS)"
  url_or_quote: "techniques: [T1090.003, T1027.002]"
  summary: "T1090.003 (Multi-hop Proxy) is unsupported by any cited source (Treasury press release, OFAC SDN listing, FBI Boston release all describe 1VPNS as a VPN/anonymization service routing through servers in ~27 countries, not proxy chaining) and has no matching body prose either. Retarget to T1090 (Proxy) or T1090.002 (External Proxy), or add a sourced multi-hop claim. T1027.002 is correctly supported."
- code: F11
  category: editorial-advisory
  section: run-record
  item: "runs/2026-07-14/2026-07-14T0409Z-intel.md body"
  url_or_quote: "All four Phase 1 research sub-agents (S1–S4) returned within cap; no S5 (no in-window `intel/` drops)."
  summary: "Workflow-internal language ('Phase 1', 'sub-agents') leaked into the published run-record verification-notes body, which docs/pipeline.md confirms is reader-facing (concatenated into the rendered brief's § Verification Notes). Violates check 12 / CLAUDE.md's hard rule. Rephrase in reader-facing language; iteration 1 incorrectly reported this section as clean."
```
