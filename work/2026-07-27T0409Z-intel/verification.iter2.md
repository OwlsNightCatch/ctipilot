**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-27T05:00:54Z · ended_at=2026-07-27T05:08:09Z · duration_seconds=435

## Verification report — 2026-07-27T0409Z-intel (iteration 2)

Cold read of all three new entries + run record. Prior-iteration deltas (F4, F3, F9, F11 from iteration 1) were walked first against the raw source bodies (ptc-advisory.txt, zataz.txt, cyberattaque.txt, ransomisac.txt, fastjson-advisory.txt) plus a fresh, independent fetch of the NVD REST API for both CVEs, the Imperva blog, and the BleepingComputer article. All four iteration-1 remediations verify correctly against source, with one exception found in the process: the F4 remediation on the Windchill entry replaced one inaccurate version-floor claim with a second, differently-sourced but still inaccurate one. Full detail below.

### Unsupported / hallucinated facts

**F4-1.** Entry: `2026-07-27/clop-windchill-flexplm-mass-extortion-wave-cve-2026-12569`.

Claim (frontmatter `cves[].affected`): *"Windchill (PDMLink) and FlexPLM from 11.0 M030 up to and including the 13.1.3 line per NVD, all CPS versions"*.

Claim (body, paragraph 3): *"NVD records the vulnerable range as running from 11.0 M030 up to and including the 13.1.3 line."*

I fetched the NVD 2.0 REST API directly in this iteration (`https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-12569`, timestamp 2026-07-27T05:01:32Z). NVD's own CVE description states: *"This advisory also applies to all CPS versions … The identified vulnerability also impacts Windchill and FlexPLM releases prior to 11.0 M030."* The `affected` version data for both PTC products lists version `"0"` with `lessThanOrEqual: "11.0 M030"` as `affected` — i.e. everything from the beginning of the product's version history through 11.0 M030 is in scope, not starting at 11.0 M030 — followed by individually enumerated affected versions (11.1 M020 through 13.1.3.0).

So NVD's own record explicitly contradicts "from 11.0 M030" as a floor: 11.0 M030 is the *upper* bound of an unbounded-below range, and NVD says in plain language that pre-11.0-M030 releases are affected too. This is the same defect class iteration 1 caught and fixed (a version floor that doesn't exist) — the correction moved the false floor from PTC's patch list onto NVD's record, but the floor itself is still false, and it's the one fact newly introduced with the correction that had not yet been through a verifier pass, per this iteration's brief.

Suggested fix: drop the "from 11.0 M030" framing. State instead something like: "NVD records every Windchill/FlexPLM release through the 13.1.3 line as vulnerable, including releases prior to 11.0 M030; PTC's eSupport article CS473270 carries the authoritative per-version patch list" — this keeps the true, useful fact (nothing is safe below 13.1.3-and-patched) without asserting a lower boundary that doesn't exist.

### Quantifier without source

**F14-1.** Entry: `2026-07-27/clop-windchill-flexplm-mass-extortion-wave-cve-2026-12569`.

Claim (body, "Defender takeaway" lead-in / correction paragraph): *"an organisation running a current 13.1.3.x release had no patch available for the first four weeks of confirmed exploitation."*

No cited source states "four weeks." The store's own June entry (`entries/2026-06-27/ptc-windchill-cve-2026-12569-now-confirmed-exploited-in-the.md`) dates "confirmed exploited in the wild" to CISA's KEV addition on **2026-06-25** ("CISA added … to its Known Exploited Vulnerabilities catalog on 2026-06-25, confirming active in-the-wild exploitation"). The 13.1.3 / 13.1.2 SUPs became available on **2026-07-14** per PTC's own changelog (verified directly from `ptc-advisory.txt`, entry timestamped "7/14/2026 at 9:20 AM ET": *"AVAILABLE NOW: Windchill and FlexPLM Security Patches … The patches are available for the following versions: SUPs: 13.1.3, 13.1.2 …"*). 2026-06-25 to 2026-07-14 is 19 days — under three weeks, not four. Even using the more generous anchor of PTC's first webshell-IOC disclosure (6/18/2026 2:00 PM ET) the gap is 26 days (3.7 weeks), still short of a clean "four weeks."

Suggested fix: state the exact dates ("no patch available between the 2026-06-25 KEV confirmation and the 2026-07-14 SUP release — roughly three weeks") rather than a rounded week-count that overstates the gap.

### Editorial / less-is-more flags (advisory)

**F11-1.** Entry: `2026-07-27/clop-windchill-flexplm-mass-extortion-wave-cve-2026-12569`. Minor: the `cves[].affected` frontmatter field attributes a claim to NVD ("per NVD") without NVD appearing in `sources[]` — a bare inline attribution to an unlinked authority. Once F4-1 above is fixed this is moot (the corrected text need not lean on an NVD attribution at all), so no separate action needed beyond fixing F4-1.

### What I independently re-verified and found clean

- **Fastjson entry** — every inline citation checked against the raw Alibaba advisory (fetched via bridge, on disk) and a fresh direct fetch of the Imperva blog (`imperva.com/blog/...`, `datePublished: 2026-07-24T18:16:29+00:00`, articleBody extracted from the page's own JSON-LD). Both quotes in `evidence[]` are verbatim substrings of their respective pages. The "US-based … Singapore and Canada … expects the targeting to expand globally" and "roughly 30 per cent … Ruby- and Go-based tooling" claims are both verbatim/near-verbatim paraphrases of Imperva's own "What We're Seeing" section ("Attacks are currently almost entirely targeting US-based organizations, with a few attacks in Singapore and Canada, although this will likely continue to expand globally" / "tools written in Ruby and Go account for about 30% of all attacks collectively"). CVSS 9.0, CVSS v3.1, AC:H, and the CISA SSVC 2026-07-23 "exploitation: none" record were all independently confirmed against a fresh NVD API fetch for CVE-2026-16723. No mention of "ThreatBook" anywhere in the Imperva page, consistent with the run record's note that the claim was dropped pre-composition. Reporter credit (Kirill Firsov / FearsOff) matches the advisory verbatim. Clean.

- **Windchill entry, prior-iteration deltas F3/F9/F11 (Chat Control) and F11 (Windchill sectors)** — all four verified correct: ZATAZ's raw HTML confirms the 24-figure count, the six named officials, the "Chat Control 1.0 … malgré les règles ePrivacy" characterization, the actor-history description ("une dizaine de fuites … entreprises françaises"), and the named risks (hameçonnage ciblé, usurpation d'identité, fraude bancaire, harcèlement) all verbatim/accurately paraphrased. Cyberattaque.org's raw HTML confirms the Cybernox handle, the 25 July claim date, the second-group listing, the "no total specified" quote (verbatim), the heterogeneity/aggregation reasoning (verbatim), and the "origine exacte … n'est pas établie" quote (verbatim). Ransom-ISAC's raw HTML confirms Manufacturing/Automotive/Aerospace/Retail-Apparel as the named sectors (supporting the entry's manufacturing/aviation/retail taxonomy mapping — "aviation" is the closest available taxonomy term to "Aerospace"; "automotive" has no taxonomy slot). The evidence[] quote attributed to BleepingComputer-quoting-ReliaQuest ("The actor behind these attacks remains unconfirmed. however, the observed tradecraft...") is a verbatim match against a fresh direct fetch of the BleepingComputer article (confirmed only after stripping HTML tags — the raw markup splits the sentence across `<p>` boundaries, which produced a false negative on my first grep pass; flagging this for the record so a future iteration doesn't waste budget on the same false lead). CVSS 9.8/9.3 split, dates, and the Oracle EBS comparison all check out verbatim against the raw advisory bodies.

- **Registry additions** (`actor:clop`, `campaign:clop-windchill-flexplm-extortion-2026`, `actor:cybernox`) — summaries and the one typed relation (`attributed-to`, sourced to this run's entry, with the attribution-dispute caveat carried in the `note`) all trace cleanly to the entries and their sources. No untyped `related` list, no invented connections.

- **`update_of` target** (`2026-06-27/ptc-windchill-cve-2026-12569-now-confirmed-exploited-in-the`) exists on disk and the update entry carries only the delta (extortion phase + the version-floor correction), not a recap.

- **Action-item discipline** — fastjson's single action and Windchill's two actions are concrete, self-contained, do-now tasks derived from each entry's own mechanics, not generic advice or body restatement; Chat Control's empty `actions: []` is correct (no IT/SOC action clears the do-now bar for a personnel-protection story). No F18.

- **Single-source / classification** — all three entries carry 2–3 sources (no F12); Admiralty codes (A/2 fastjson, B/2 Windchill, B/2 Chat Control) are defensible given each entry's actual sourcing mix and the contested/uncorroborated points each entry flags in its own `sourcing_note`. No F17.

- **Priority calibration** — `high` on fastjson and Windchill, `notable` on Chat Control all sit on the right side of the critical/high/notable bar as described in § Organization context; nothing here clears the "stop-reading-and-act-now" critical bar or is under-alerted as notable when it should be high. No F16 (N/A — no triage scheme configured, and no org_triage / watchlist fields present on any entry, correctly).

### Verdict

`NEEDS_FIXES (truth: 2, editorial: 0, advisory: 0)`

Both findings are on the Windchill entry's own correction paragraph and CVE-affected-range language — the two fresh, not-yet-verified facts the spawn message flagged as needing scrutiny this iteration. The fastjson and Chat Control entries, and three of the four iteration-1 remediations, are clean on independent re-verification.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "2026-07-27/clop-windchill-flexplm-mass-extortion-wave-cve-2026-12569"
  url_or_quote: "cves[].affected / body para 3: \"NVD records the vulnerable range as running from 11.0 M030 up to and including the 13.1.3 line.\""
  summary: "NVD's own CVE-2026-12569 record (fetched directly this iteration) states the vulnerability 'also impacts Windchill and FlexPLM releases prior to 11.0 M030' and its affected-versions data lists 11.0 M030 as the ceiling of an unbounded-below range, not a floor. The entry re-introduces the same version-floor error iteration 1 fixed, now attributed to NVD instead of PTC."
- code: F14
  category: quantifier-without-source
  section: active-threats
  item: "2026-07-27/clop-windchill-flexplm-mass-extortion-wave-cve-2026-12569"
  url_or_quote: "\"an organisation running a current 13.1.x release had no patch available for the first four weeks of confirmed exploitation\""
  summary: "No cited source says 'four weeks.' Store's own June entry dates confirmed exploitation to the 2026-06-25 CISA KEV addition; PTC's changelog dates the 13.1.3/13.1.2 SUP release to 2026-07-14. That gap is 19 days (~2.7 weeks), not four weeks."
```

**Self-telemetry:** webfetch_calls=0 · websearch_calls=0 · bridge_fetches=6 (NVD CVE-2026-12569, NVD CVE-2026-16723, PTC advisory re-grep via existing disk copy, BleepingComputer article, Imperva blog) · urls_checked=7
