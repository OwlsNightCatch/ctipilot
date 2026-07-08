**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-08T20:57:45Z · ended_at=2026-07-08T21:10:02Z · duration_seconds=737
**Self-telemetry:** urls_checked=27 · webfetch_calls=17 · bridge_fetches=11 · websearch_calls=0

## Verification report — 2026-07-08T2009Z-intel (iteration 1)

Cold read of all 11 new entries + run record. Every primary source fetched (WebFetch, jina reader, or bridge for CISA/NCSC-CH/NCSC-NL); load-bearing corroborators fetched; lower-priority corroborators (teiss, coldfusion "patch-by-Friday" BC #2, Hydro-Québec CSAF GitHub mirror) sampled against already-verified authorities. CISA KEV confirmed all four CVEs (CVE-2026-48282/-55255/-48908/-56290) added 2026-07-07 and CVE-2026-33017 on 2026-03-25. NCSC-NL CSAF confirmed 25 vulnerabilities and all six Ubiquiti CVSS scores exactly. Dedup validated against prior_coverage.json (prior BeyondTrust = Klue/Icarus Salesforce victim, no CVE overlap; prior Langflow = JADEPUFFER CVE-2025-3248, different CVE — both correctly new entries; ColdFusion correctly update_of the 07-02 cluster; Ubiquiti SAB-066 correctly distinct from the 06-24 UniFi OS chain).

Verified clean (no finding): ColdFusion (both BC quotes verbatim, ~800 Shadowserver, sub-2h weaponisation, KEV), Langflow (Sysdig quotes verbatim, 9.9/8.4 reconciliation correct, CVE-2026-33017 chain confirmed), GhostLock deep-dive (nebusec + THN, commit 3bfdc63936dd, 97%/5s/kernelCTF $92,337, CONFIG_FUTEX_PI all confirmed), Talos UAT-7810 (both quotes verbatim, all router CVEs + malware suite confirmed), Unit42 Factory-v3 (both quotes verbatim, all evasion mechanics confirmed; IOCs correctly excluded), Hydro-Québec OCPP (CISA advisory quotes verbatim, no-exploitation status confirmed), Ubiquiti (all CVEs/CVSS confirmed), Accenture core incident (Accenture statement verbatim, scope framed as unverified '888' claim throughout, 32,826/three scope-inflation history confirmed verbatim in Help Net Security). Classification codes (B2 on the three single-source labs, B3 on Accenture), single-source flags (F12) and org-triage/watchlist absence (F16 — org has no scheme; none present) all correct.

### Unsupported / hallucinated facts
- **F4 — Joomla (evidence quote not verbatim).** evidence[1] attributed to The Hacker News reads "CVE-2026-48908 was exploited as a zero-day to upload a PHP file via HTTP POST request to the 'index.php?option=com_sppagebuilder&task=asset.uploadCustomIcon' endpoint." The article's actual text: "CVE-2026-48908, on the other hand, is said to have been exploited as a zero-day to upload a PHP file by means of an HTTP POST request to the ... endpoint." The entry removes the hedge "is said to have been" → "was" (a mild but real overstatement of certainty) and rewrites "by means of an" → "via". Substance is accurate; the evidence[] quote is not a verbatim substring. Fix: restore the verbatim source string.
- **F4 — Accenture (evidence quote not verbatim).** evidence[1] attributed to SOCRadar reads "Several important details remain unclear: Whether the full advertised dataset is authentic, whether the 35GB figure is accurate, whether any keys are still valid." Source text: "Several important details remain unclear: Whether the full advertised dataset is authentic, Whether the 35GB figure is accurate, Whether the alleged data is current, Whether any keys, tokens, or credentials are still valid." The entry silently drops the clause "Whether the alleged data is current," and compresses "any keys, tokens, or credentials" → "any keys", presented as one continuous quote. Fix: restore verbatim text or mark the omission with an ellipsis.
- **F4 — CrySome ("subscription ... sold via a public web portal" uncited).** The entry states "CrySome, a subscription .NET RAT" (summary) and "a subscription-based .NET remote-access trojan sold via a public web portal" (body). This is a single-source entry; the sole cited source (LevelBlue SpiderLabs, fetched via jina) describes CrySome as a RAT "documented extensively in previous public reporting" but nowhere states a subscription model or portal sale — no "subscription"/"sold"/sales-"portal" text (the only "portal" is the phishing rate-confirmation portal). Provenance descriptor is uncited by the only source. Fix: soften to what the source supports, or add a corroborating source. (Likely true from other CrySome reporting, but not from the cited article.)

### Editorial / less-is-more flags (advisory)
- **F11 — vendor PSIRT as primary (BeyondTrust / Ubiquiti).** Both entries are multi-source and valid (national-CERT primary + news/vendor corroboration). Optional strengthening: add the first-party vendor advisory (BeyondTrust BT26-03 at https://www.beyondtrust.com/trust-center/security-advisories/bt26-03 ; Ubiquiti SAB-066) as a source. Non-blocking.
- **F11 — Langflow references cross-link.** Prior coverage carries a related Langflow-exploitation entry (2026-07-04 JADEPUFFER, Sysdig, CVE-2025-3248). Distinct CVEs, so correctly a new entry — but a `references` link to JADEPUFFER (same product + same lab, days apart) would help the reader connect the thread. Optional.

### Analytical-link-as-fact
- **F13 — BeyondTrust China-nexus / US-Treasury attribution.** The body asserts: "BeyondTrust RS/PRA zero-days (CVE-2024-12356/-12686) were previously weaponised by a China-nexus actor to breach the US Treasury in December 2024 ([The Hacker News, 2026-07-07])." I fetched that THN article (jina, 4.3 KB): it contains no "Treasury", "China", "Silk", "nexus", "nation-state" or "espionage"; it only says the prior RS/PRA flaws "have come under repeated exploitation in the past to deploy web shells and backdoors", and it pairs CVE-2024-12356 with CVE-2026-1731 — not -12686. The other cited source (BleepingComputer) likewise does not mention Treasury or China. So the specific China-nexus + US-Treasury + December-2024 attribution is presented as cited but is unsupported by any source on this item. The claim is factually true in the real world (Silk Typhoon / US Treasury, Dec 2024), so this is a sourcing/attribution defect, not a fabrication — and it partly underpins the entry's "nation-state exploitation history" justification for the `high` rating. Fix: add a source that actually documents the attribution (the original Jan-2025 reporting), or reword to what THN/BC support.

### Verdict
NEEDS_FIXES (truth: 4, editorial: 0, advisory: 2)

Truth findings are one material attribution defect (F13, load-bearing for the BeyondTrust priority justification) and three quote/provenance-fidelity defects (two non-verbatim evidence quotes on Joomla and Accenture, one uncited single-source provenance claim on CrySome). None is a fabricated fact — all four describe true statements that are either mis-attributed to a source that does not state them (F13, CrySome) or reworded from the verbatim source text (Joomla, Accenture). All are cheap to remediate. No broken/generic URLs, no dedup errors, no priority miscalibration (ColdFusion/Langflow/BeyondTrust `high` and the four `notable`s are all defensible; no under/over-alerting), no missed in-window angle I can name a source for — the three documented borderline drops (Compass CRA, Krebs IRIS, Swiss Post e-voting) correctly fail the actionability gate and the out-of-window Linux-LPE near-miss (Bad Epoll) is already thematically covered by GhostLock. Coverage looks complete and sound.

### Findings summary (machine-readable)
```yaml
# Findings summary (machine-readable)
- code: F13
  category: analytical-link-as-fact
  section: trending-vulnerabilities
  item: "CVE-2026-40138/-40139 — BeyondTrust RS/PRA pre-auth bypass (NCSC-CH)"
  url_or_quote: "\"BeyondTrust RS/PRA zero-days (CVE-2024-12356/-12686) were previously weaponised by a China-nexus actor to breach the US Treasury in December 2024 ([The Hacker News, 2026-07-07])\""
  summary: "The China-nexus + US-Treasury + Dec-2024 attribution is asserted as cited to the THN 2026-07-07 article, but that article (fetched via jina, 4.3 KB) contains no mention of Treasury, China, Silk or nexus — it only says the prior flaws 'have come under repeated exploitation ... to deploy web shells and backdoors' and pairs CVE-2024-12356 with CVE-2026-1731 (not -12686). The other cited source (BleepingComputer) also does not mention Treasury/China. Claim is true in reality (Silk Typhoon/Treasury) but unsupported by any source cited on this item. Remediation: add a source that documents the attribution, or reword to what THN/BC actually support."
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "CVE-2026-48908 / CVE-2026-56290 — Joomla page-builder KEV zero-days"
  url_or_quote: "evidence[1] attributed to The Hacker News: \"CVE-2026-48908 was exploited as a zero-day to upload a PHP file via HTTP POST request to the 'index.php?option=com_sppagebuilder&task=asset.uploadCustomIcon' endpoint.\""
  summary: "Not a verbatim substring of the cited THN article. Actual text: 'CVE-2026-48908, on the other hand, is said to have been exploited as a zero-day to upload a PHP file by means of an HTTP POST request to the ... endpoint.' The entry silently removes the hedge 'is said to have been' -> 'was' (mild overstatement) and rewrites 'by means of an' -> 'via'. Remediation: replace evidence quote with the verbatim source string (or re-attribute)."
- code: F4
  category: hallucinated-fact
  section: incidents
  item: "Accenture confirms data-theft incident; '888' claims 35 GB"
  url_or_quote: "evidence[1] attributed to SOCRadar: \"Several important details remain unclear: Whether the full advertised dataset is authentic, whether the 35GB figure is accurate, whether any keys are still valid.\""
  summary: "Not a verbatim substring. Source text: 'Several important details remain unclear: Whether the full advertised dataset is authentic, Whether the 35GB figure is accurate, Whether the alleged data is current, Whether any keys, tokens, or credentials are still valid.' The entry elides the clause 'Whether the alleged data is current,' and compresses 'any keys, tokens, or credentials' to 'any keys' with no ellipsis, presenting it as continuous. Substance faithful; quote not verbatim. Remediation: restore verbatim text or mark elision with ellipsis."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "CrySome RAT freight-phishing chain (LevelBlue SpiderLabs)"
  url_or_quote: "\"CrySome, a subscription .NET RAT\" / \"CrySome RAT — a subscription-based .NET remote-access trojan sold via a public web portal\""
  summary: "Single-source entry (verification: single-source). The sole cited source (LevelBlue SpiderLabs, fetched via jina) describes CrySome as a RAT 'documented extensively in previous public reporting' but does NOT state it is subscription-based or sold via a public portal — no 'subscription'/'sold'/sales-'portal' language in the article text (the only 'portal' is the phishing rate-confirmation portal). The provenance/business-model descriptor is uncited. Remediation: soften to what the source supports, or add a corroborating source for the subscription-sales-model claim."
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "BeyondTrust (BT26-03) and Ubiquiti (SAB-066) entries"
  url_or_quote: "primary = national CERT (NCSC-CH post 12751 / NCSC-NL NCSC-2026-0221)"
  summary: "Both entries are multi-source and valid, but the vendor PSIRT is the true first-party disclosure (BeyondTrust https://www.beyondtrust.com/trust-center/security-advisories/bt26-03 ; Ubiquiti SAB-066). Optional: add the vendor advisory as a primary/corroborating record to anchor first-party sourcing. Non-blocking."
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CVE-2026-55255 — Langflow IDOR chained with CVE-2026-33017"
  url_or_quote: "references: []"
  summary: "Prior coverage carries a related Langflow-exploitation entry (2026-07-04 JADEPUFFER, Sysdig, CVE-2025-3248). Distinct CVEs so correctly a NEW entry, but a references cross-link to the JADEPUFFER entry (same product + same research lab, days apart) would help the reader connect the Langflow-exploitation thread. Optional. Non-blocking."
```
