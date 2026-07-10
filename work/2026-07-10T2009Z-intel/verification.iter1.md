**Model:** Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-10T20:47:34Z · ended_at=2026-07-10T20:53:50Z · duration_seconds=376
**Self-telemetry:** webfetch_calls=8 · websearch_calls=0 · bridge_fetches=4 · urls_checked=13

## Verification report — 2026-07-10T2009Z-intel (iteration 1)

Cold read of 6 new entries + run record. Every inline source URL fetched (WebFetch, or bridge/jina for CISA/NCSC.ch/Siemens/ZeroBEC). All CVE ids, versions, CVSS scores, dates and named entities cross-checked against the fetched sources. Dedup checked against prior_coverage.json (iCagenda distinct new CVE sharing trend tag = correctly new; Forg365 references the morning Railway/LSHIY entry = correctly new).

Facts that verified clean: iCagenda CVE-2026-48939 (CVSS 10.0, versions 3.2.1–3.9.14 / 4.0.0–4.0.7, fixed 3.9.15/4.0.8, Joomla-6-only RCE nuance, exactly-two KEV additions 2026-07-10 with Balbooa) — all confirmed against mySites.guru + CISA KEV. Siemens SSA-229470 (four CVEs, all four v3.1 base scores 6.5/6.7/4.8/7.2, aggregate 7.2/8.6, both evidence quotes verbatim, no exploitation, local/auth prerequisites correctly framed) — confirmed against Siemens ProductCERT + CERT-FR AVI-0860. Zimbra (no CVE, exploitation UNKNOWN, Classic-Web-Client-only, stored XSS per heise, NCSC-CH post 12757) — confirmed. Forg365 (pricing $400/mo / $3,800/yr / 5-day trial, ForgCookie SSO-cookie refresh, both evidence quotes verbatim, "no common ownership" caveat honoured, MFA quote a contiguous substring of CSA Labs sentence) — confirmed. WP-SHELLSTORM (27 CVEs 14c/9h, 1.4M domains, 5,700+ shells, 22 days, Breeze/ThemeREX/JCE figures, Nacos CVE-2021-29441, VShell/SNOWLIGHT) — confirmed; IOC-clean (no IPs/domains/hashes leaked; the `[kworker/X:Y]` discriminator reads as behavior, not an indicator). Open WebUI (six BAC CVEs, CVE-2025-64496 chain, CVE-2025-63681 unpatched, two GHSA map to CVE-2026-44556 and CVE-2026-54015 with matching versions/severities) — confirmed.

### Unsupported / hallucinated facts

- **F4** — `wp-shellstorm-webshell-brokerage-exposed-toolkit`, evidence[] quote (The Hacker News): "Ctrl-Alt-Intel's deduplicated count found 25,195 sites with confirmed or validated compromise evidence, while SOCRadar ... put the live figure at 5,700-plus". The cited THN page reads "…while SOCRadar, **counting active webshells**, put the live figure at 5,700-plus." The evidence[] quote inserts an ellipsis in place of ", counting active webshells," so it is not a contiguous verbatim substring (and the elided clause is precisely what reconciles the two counts). Fix: trim to a contiguous span or restore the elided words.
- **F4** — `open-webui-recurring-broken-access-control-cve-cluster`, evidence[] quote (CSA Labs): "CVE-2025-63681 ... remains unpatched as of this writing; upgrading to the latest version does not close this cluster's exposure completely". Inserted ellipsis after "CVE-2025-63681" plus a semicolon join of two source fragments — not a contiguous verbatim substring of the CSA Labs note. The body's short quote "remains unpatched as of this writing" is fine; the frontmatter evidence[] quote should be trimmed to a single contiguous span.
- **F4** — `wp-shellstorm-webshell-brokerage-exposed-toolkit`, body: "…both agreeing the crew is financially-motivated cybercrime rather than a nation-state actor". The cited THN article makes this assessment for SOCRadar only ("SOCRadar goes a step further, reading the crew as financially motivated rather than state-directed"); it does not state Ctrl-Alt-Intel's attribution stance. Asserting both research teams agree overstates the source. The frontmatter sourcing_note already correctly attributes the assessment to SOCRadar alone — align the body.

### Classification missing / inconsistent

- **F17** — `cve-2026-48939-icagenda-joomla-unauth-file-upload-rce-kev`, `classification: {reliability: A, credibility: 1}`. Reliability A rests on mySites.guru as `role: primary`, a third-party security-researcher vendor blog that is not in `sources.json` (the run record itself records it as an unpromoted candidate added this run). The run's own calibration assigns B to every comparable research-blog primary this run (CSA Labs, SOCRadar, ZeroBEC); A on a non-A-tier blog is inconsistent and matches the F17 trigger "A on a source not in the A tier of sources.json". Fix: downgrade reliability to B, or justify A explicitly on the CISA-KEV (A-tier) corroboration. Credibility 1 is defensible — CISA KEV independently confirms exploitation.

### Coverage assessment

Coverage looks complete. No missed in-window angle I can name with a plausible source: the four borderline drops (MODBEACON aggregator-only/no-nexus, Wiz Red Agent vendor case study, CISA GovCloud governance/weekly, DigitalMint US-only) are reasonably justified, and the one unmitigated 403 (industrialcyber-co) was a vendor-report roll-up the run correctly assessed as low-value. Priority calibration is sound (iCagenda `high` not `critical` — patch 3.5 weeks old, KEV formalises rather than newly weaponises; all others `notable`; zero `critical` appropriate). Update-vs-new decisions correct (iCagenda distinct CVE sharing the trend tag; Forg365 distinct kit/operator with a valid `references[]` cross-link to the morning entry). No IOCs, no vanity metrics, no workflow-internal language. All attacker-behavior entries carry non-empty `techniques[]`.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 1, advisory: 0)

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: wp-shellstorm-webshell-brokerage-exposed-toolkit
  item: "WP-SHELLSTORM exposed webshell-brokerage toolkit"
  url_or_quote: "evidence[] (THN): '...while SOCRadar ... put the live figure at 5,700-plus'"
  summary: "Inserted ellipsis; source reads '...while SOCRadar, counting active webshells, put the live figure at 5,700-plus.' Not a contiguous verbatim substring."
- code: F4
  category: hallucinated-fact
  section: open-webui-recurring-broken-access-control-cve-cluster
  item: "Open WebUI six broken-access-control CVEs"
  url_or_quote: "evidence[] (CSA Labs): 'CVE-2025-63681 ... remains unpatched as of this writing; upgrading...'"
  summary: "Inserted ellipsis + semicolon splice of two fragments; not a contiguous verbatim substring."
- code: F4
  category: hallucinated-fact
  section: wp-shellstorm-webshell-brokerage-exposed-toolkit
  item: "WP-SHELLSTORM exposed webshell-brokerage toolkit"
  url_or_quote: "body: '...both agreeing the crew is financially-motivated cybercrime rather than a nation-state actor'"
  summary: "THN attributes financially-motivated/non-state assessment to SOCRadar only; Ctrl-Alt-Intel's stance not stated. 'Both agreeing' overstates the source."
- code: F17
  category: classification
  section: cve-2026-48939-icagenda-joomla-unauth-file-upload-rce-kev
  item: "CVE-2026-48939 iCagenda Joomla unauth file-upload RCE"
  url_or_quote: "classification {reliability: A, credibility: 1}; primary mysites.guru"
  summary: "Reliability A on a non-sources.json research-blog primary; run's own calibration gives B to comparable primaries. Downgrade to B or justify A on the CISA-KEV corroboration."
```
