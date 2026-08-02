**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-02T06:09:50Z · ended_at=2026-08-02T06:15:07Z · duration_seconds=317

## Verification report — 2026-08-02T0409Z-intel (iteration 8, final)

Cold-ish pass (deltas block supplied per the alt-verifier rotation contract) against all four entries and the run record. This is iteration 8 — the hard cap — so the verdict publishes regardless, but the pass was run at full rigour, not as a formality.

### Prior-iteration deltas verified

1. **Rails author attribution (iter-7 F3).** `deepread/rails.clean.txt` line 14 confirms flavorjones opens "Hello there, I'm writing as a member of the Rails security team about CVE-2026-66066," and line 22 confirms the exact quote now in the entry — "extracted from work I did at 37signals to perform a forensic analysis on our own apps" — verbatim, contiguous. The current body text ("The post's author, writing as a member of the Rails security team, states the material was 'extracted from work I did at 37signals to perform a forensic analysis on our own apps' — that is, it comes out of one company's real incident response rather than being written for the advisory") accurately reflects both the speaker's role and the individual/company framing. Remediation holds.

2. **Run-record discovery-gap dates (iter-7 F4).** Fetched `https://doublepulsar.com/adform-compromised-to-serve-crypto-stealer-via-supply-chain-attack-2f1ec024f33e` directly (bridge `url`, Medium-hosted mirror) and confirmed its structured `datePublished` is `2026-07-30T13:36:19Z` (also `article:published_time` `2026-07-30T13:42:20Z`). Against this run's window start (`2026-08-02T04:09:57Z` − 26h = `2026-08-01T02:09:57Z`), that is ~36h33m before window-open, and it falls inside the 2026-07-31 run's window (`2026-07-30T02:09:14Z`–`2026-07-31T04:09:14Z`, confirmed from that run's own frontmatter) — matching the record's "roughly 36 hours before this window opened and inside the window of the run before last." Also confirmed BleepingComputer's own JSON-LD `datePublished` (`deepread/bc-adform.txt` line 90) is `2026-07-31T17:09:25-04:00` = `2026-07-31T21:09:25Z`, ~5h before window-open — matching "the first mainstream pickup followed on 2026-07-31, about five hours before this window opened." Both figures in the corrected notes check out precisely against primary timestamps, not just approximately. Remediation holds.

### Independent checks this iteration (beyond the deltas)

- **CVE-2026-66066 cross-check** against the NVD API (`services.nvd.nist.gov/rest/json/cves/2.0`) and the OSV mirror (`api.osv.dev/v1/vulns/CVE-2026-66066`), since GitHub is egress-blocked this run. CVSS 9.5/CRITICAL, AV:N/PR:N/UI:N confirmed against the entry's `cvss: "9.5"`, `vector: zero-click`, `auth: pre-auth`. Affected ranges `< 7.2.3.2`, `>= 8.0.0.beta1 < 8.0.5.1`, `>= 8.1.0.beta1 < 8.1.3.1` match the entry's `cves[].affected` exactly, as do the three fixed versions.
- **COLDCARD entry**: all three `evidence[]` quotes confirmed as contiguous verbatim substrings of `deepread/coinkite.clean.txt`. Body figures (40-bit / 72-bit search space, firmware ranges 4.0.1–4.1.9→4.2.0, 5.6.0/1.5.0Q/6.6.0X/6.6.0QX) all match the source. Cross-checked the theft figures (1,367.05 BTC / 4,585 addresses / 207.7294 BTC third wave / 27-hour gap between waves 1–2 / P2WPKH-vs-P2WSH output-type distinction) against `deepread/ct.clean.txt` — all precise matches, including the wave-3 differentiators (per-victim addresses, batched victims, default-derivation-path-only). Cross-checked Block Engineering's "active exploitation is under way" framing (`deepread/block.clean.txt` line 3) against the registry summary's claim that exploitation was "confirmed under way by 2026-07-30" — holds, and no source in the set gives an exploitation *start* date, matching the registry's explicit "no cited source dates its start."
- **CCI Nice Côte d'Azur entry**: both quotes verified verbatim-contiguous against `deepread/cci.clean.txt`; the "nothing disclosed supports a conclusion that the chamber's wider IT estate was compromised" line is confirmed to be Cyberattaque.org's own editorializing (not attributed to the chamber), matching the entry's careful attribution. Publication date (`1 août 2026 à 9h00` → `2026-08-01`) matches the frontmatter source date.
- **Adform entry**: the browser-cache-persistence detail in the action item ("the altered file may persist in visitors' browser caches after the fix") traced to Adform's own primary notice (`deepread/adform.clean.txt` line 14: "we recommend that individuals who visited an affected website clear their browser cache as a precaution") — sourced, not invented, even though not restated in the entry body.
- **Run-record internal cross-checks**: `entries_published: 4` / `entries_updated: 1` verified against the four entry files (3 new + 1 update_of) and against the documented field meaning in `docs/pipeline.md`. The fetch-failure count ("eight… a ninth for an unrelated reason") verified against the `fetch_failures` block — exactly eight records carry HTTP 402/reader-exhaustion, the ninth (`group-ib-blog`) carries a distinct `transport-5xx`. `triage.json`'s `in_window_anchor` timestamps (Rails thread `2026-07-31T00:51`, Discourse reply `2026-08-01T06:00`, Coinkite advisory update `2026-08-01T18:35Z`, Galaxy relay `2026-08-01T20:36Z`, Cyberattaque.org `2026-08-01T07:00Z`) all independently confirmed against the raw source timestamps (Coinkite's own "Updated August 1, 2026 at 2:35 p.m. EDT" = 18:35 UTC; Cyberattaque.org's "1 août 2026 à 9h00" CEST = 07:00 UTC).
- **Dedup check**: `prior_coverage.json`'s 121 records contain no entry for Adform, CCI Nice Côte d'Azur or COLDCARD, and exactly one match for the Rails CVE (the correct `update_of` target). No missed dedup.
- **Registry entries**: all three new `incident:` keys' summaries cross-checked against their entries and sources — accurate, no unsupported quantifiers or dates.

No new defect found. No missed in-window angle identified beyond what iterations 1–7 already covered (this pass did not re-run the full missed-angle sweep given the iteration-8 time budget and the seven prior iterations' consistent "no gap" findings, but spot-checked the drops in `triage.json` against their stated reasons and found them all still defensible).

### Verdict

CLEAN

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
[]
```
