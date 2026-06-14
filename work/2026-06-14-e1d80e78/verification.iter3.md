**Model:** Anthropic Claude Opus 4.8 (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-14T04:49:07Z · ended_at=2026-06-14T04:51:48Z · duration_seconds=161
**Self-telemetry:** webfetch_calls=15 · websearch_calls=0 · bridge_fetches=2 · urls_checked=17

## Verification report — briefs/2026-06-14.md (iteration 3)

Cold read. Mechanical gate passed pre-spawn (52 pass / 3 warn / 0 fail). Every inline Source URL fetched (Security Affairs x2, watchTowr Splunk, watchTowr Ivanti, WPScan, Malware.news/Wordfence, Sekoia TDR, BleepingComputer x2, CyberScoop, DOJ mirror, TechTimes, ENISA, Brussels Morning, Splunk SVD-2026-0603 advisory, THN, CERT-EU 2026-008 via bridge, MITRE T1190 + T1059). All resolve to specific articles/advisories — no broken or generic-landing URLs, no NVD/MITRE-only primary sourcing. Splunk/UpdraftPlus/Ivanti/Kyushu/ENISA/Conti core facts (CVEs, CVSS, versions, dates, install counts, record counts, scenario, $150M / 1000+ orgs / 31 countries) all trace cleanly to fetched sources. Switzerland-as-partner-country is supported by Brussels Morning verbatim. The findings below are three truth-class gaps where the brief asserts detail the cited sources do not carry.

### Citation does not support the claim

**F3 — APT28 `Signal.exe` spawning script interpreters detection tell (§ 3 and § 6).** Brief writes (§ 3 "Why it matters"): "watch for `Signal.exe` spawning script interpreters as an initial-access tell" and repeats it in § 6 Action Items ("`Signal.exe` spawning script interpreters"). The cited Sekoia TDR report does not describe Signal.exe spawning script interpreters. Per the fetched page, the report's only Signal reference is Signal Desktop being abused as a Mark-of-the-Web bypass for delivery of malicious Office documents — a different behaviour (MotW bypass on document delivery, not a process-ancestry tell on Signal.exe). The detection guidance as written attributes a process-spawning behaviour to the source that the source does not state. Either reword to the MotW-bypass behaviour the report actually documents, or drop the Signal.exe child-process tell.

### Unsupported / hallucinated facts

**F4 — "Four co-conspirators indicted in 2023 remain at large" (§ 1 Conti item, final sentence).** Brief: "Four co-conspirators indicted in 2023 remain at large." The DOJ mirror (globalsecurity.org) supports "an indictment charging four other Conti conspirators was unsealed in the Middle District of Tennessee" in September 2023 — so "four co-conspirators indicted in 2023" is sourced. But none of the three cited sources (DOJ mirror, CyberScoop, BleepingComputer) state that those four "remain at large" / are fugitives. CyberScoop names four (Galochkin, Rudenskiy, Tsarev, Zhuykov) but the fetched summary explicitly notes their at-large status is "not explicitly stated"; the DOJ mirror does not say it; BleepingComputer does not mention the four at all. The "remain at large" clause is an unsourced inference. Reword to what the DOJ states ("four other Conti conspirators were charged in a September 2023 indictment unsealed in the same district") or drop the at-large assertion.

### Quantifier without source

**F14 — "within roughly 40 hours" PoC-to-backdoor timeline (§ 0 TL;DR, § 0 Immediate Action callout, § 4 UPDATE).** Brief asserts in three places that the Shadowserver-confirmed backdooring occurred "within ~40 h of the public PoC" / "within roughly 40 hours of watchTowr's public proof-of-concept." The watchTowr Ivanti PoC is dated 10 June (confirmed by fetching the watchTowr page CERT-EU references) and the Shadowserver backdooring is reported by Security Affairs dated 11 June. Neither Security Affairs, BleepingComputer, CERT-EU, nor the watchTowr page states a "~40 hour" figure — it is the brief's own arithmetic across two source dates. The figure is plausible but no cited source carries it. Either attribute the derivation transparently ("within roughly two days of the 10 June PoC, per the 11 June Shadowserver report") or drop the specific "~40 hours" number, which reads as a sourced metric but is not.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 0)

All three are truth-class: F3 (citation does not support claim), F4 (unsupported fact), F14 (quantifier without source). Each is backed by a source I fetched in this iteration. No editorial drops — relevance is strong throughout (Ivanti/Splunk/UpdraftPlus are widely-deployed CH/EU public-sector tech; APT28 names NATO European ministries; ENISA/Cyber Europe has explicit Swiss nexus; Conti extradition is an EU-channel data point; Kyushu is a NIS2-transferable physical-media lesson). § 2 inclusion gates honoured. Deep dive earns its length. SINGLE-SOURCE flag correctly present on the Sekoia APT28 item with a matching § 7 line. No IOCs, no vanity metrics, no workflow-internal language. Coverage shape leads CH/EU. No missed angles given the logged drops.

### Findings summary (machine-readable)
```yaml
- code: F3
  category: claim-not-supported
  section: research-investigative
  item: "Sekoia APT28 tradecraft evolution — detection tells"
  url_or_quote: "watch for `Signal.exe` spawning script interpreters as an initial-access tell"
  summary: "Sekoia report describes Signal Desktop as a Mark-of-the-Web bypass for malicious Office-document delivery, not Signal.exe spawning script interpreters. Reword to MotW-bypass behaviour or drop. Appears in §3 and §6."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "Conti loader developer Oleksii Lytvynenko pleads guilty"
  url_or_quote: "Four co-conspirators indicted in 2023 remain at large."
  summary: "DOJ mirror supports 'four other Conti conspirators indicted Sept 2023 (unsealed MD-Tennessee)' but no cited source (DOJ/CyberScoop/BleepingComputer) states they 'remain at large'. Reword to the DOJ wording or drop at-large clause."
- code: F14
  category: quantifier-without-source
  section: tldr
  item: "Ivanti Sentry CVE-2026-10520 PoC-to-backdoor timeline"
  url_or_quote: "within roughly 40 hours of watchTowr's public proof-of-concept"
  summary: "watchTowr PoC dated 10 June; Shadowserver backdooring reported by Security Affairs 11 June. No cited source states a ~40h figure; it is the brief's arithmetic. Attribute the derivation or drop the specific number. Appears in §0 TL;DR, §0 callout, §4 UPDATE."
```
