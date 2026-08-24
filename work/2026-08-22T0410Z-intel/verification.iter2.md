**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-22T06:14:12Z · ended_at=2026-08-22T06:25:01Z · duration_seconds=649

## Verification report — 2026-08-22T0410Z-intel (iteration 2)

Scope: all sixteen entries under `entries/2026-08-22/` plus `runs/2026-08-22/2026-08-22T0410Z-intel.md`. Per the spawn tasking, this iteration (a) read the never-before-verified `crates-io-build-script-dropper-yank-lure-arrayref` entry cold and hard, (b) re-verified all 25 iteration-1 remediations against primary sources / saved artefacts for soundness and regression, and (c) re-audited the run record's own internal consistency per the "least trustworthy artefact" warning.

### Priority 1 — the never-reviewed entry (`crates-io-build-script-dropper-yank-lure-arrayref`)

All ten `evidence[]` quotes verified as genuine contiguous verbatim substrings of the saved source bodies (`rust-blog.txt`, `rustsec-0260.txt`, `wiz.html`/`wiz.clean`, `step.html`/`step.clean`). The two flagged "deliberate mid-sentence fragments" are real artefacts of inline-markup tag-flattening, not splices: `rust-blog.txt.clean` line 44 begins exactly at `"to be acting maliciously..."` (the preceding `<code>arrayref</code>` tag caused a line break in the flattened text), and `rustsec-0260.clean` line 42 ends exactly at `"...constituted less than"` with `"10% of"` starting a new line after the `<code>` tag around `arrayref`. Both quotes stop precisely where the extracted text stops being contiguous — correct handling, not a defect.

- **Lockfile claim** ("Lockfile-pinned builds were not exposed") is directly supported by StepSecurity's own sentence, verified verbatim in `step.clean`: "Builds with pre-existing lockfiles pinning clean versions kept compiling the clean, yanked-but-downloadable code, since yanking alone never breaks a locked build."
- **Download/dependent figures**: the entry does not print any "403 dependents" or "406 dependent crate versions" figure anywhere — it cites only RustSec's verified "downloaded 2,285 times... less than 10%" figure. The disputed referral figure the research pass warned about was correctly never carried into the published entry. No defect.
- **North Korea overlap**: confined to attributive hedge language everywhere it appears — body text ("infrastructure substantially overlaps with operations attributed to recent North Korean actors" — Wiz's own words, verified verbatim), `sourcing_note` ("Wiz's own overlap assessment... not an attribution by anyone"), and the registry edge (`entities/registry.yaml` line 5281: `type: overlaps-with`, not `attributed-to`). Consistent throughout.
- **Technique mapping** follows Wiz's published self-correction: `wiz.clean` line 77 reads "Edit: A prior version of this piece mistakenly stated that browser credentials were stolen. The queries only enumerate saved logins, they do not retrieve the encrypted credential material" — verified verbatim. `techniques[]` carries `T1217` (Browser Information Discovery, active/non-deprecated in the pinned ATT&CK dataset) and does NOT carry `T1555.003` (Credentials from Web Browsers). Correct.
- **Action items**: all three are concrete and finding-derived — a specific time window (07:11–09:25 UTC) and specific poisoned-version/typosquat-crate names to search build logs for; a specific instruction to treat build identity (not just the project) as compromised and rotate SSH/cloud/CI/signing credentials on hosts that resolved a poisoned version; a specific instruction to re-run dependency auditing because the malicious versions were deleted (not yanked) and RustSec records were still pending on the day, so a same-day scan could have reported clean. None is generic supply-chain boilerplate; none restates the body's detection guidance. No F18.

**Verdict on this entry: clean.**

### Priority 2 — remediation verification (all 25 items)

All 25 remediations were independently re-verified against primary sources, saved run artefacts, or the entity registry, with no regressions found:

1. TP-Link ER706W-4G v1 build — vendor table (`tplink-vendor.html`) confirms `1.2.6 Build 20260723 Rel.41321` for ER706W-4G v1 (distinct from ER706W v1's `1.2.11 Build 20260723 Rel.41567`); matches in `cves[]`, action, and body. Correct.
2. TP-Link "nineteen rows / eighteen names" — counted the vendor table directly: 19 rows, 18 unique model names, ER706W-4G repeated for two hardware revisions. Matches `affected_products[]` (18 entries). Correct.
3. PTC CVE-2026-77645/77646 product bindings — confirmed against the GHSA pages themselves (fetched via `WebFetch` directly, bypassing the blocked bridge): GHSA-qxmv-9q88-wwmw (CVE-2026-77645) names only "PTC Windchill and PTC FlexPLM"; GHSA-2698-qwmx-3r6f (CVE-2026-77646) names "PTC Windchill PDMLink and PTC FlexPLM." Entry now matches both exactly (BSI's CSAF product tree is looser/broader, but the per-CVE authority — PTC via GHSA — is what the entry correctly follows). Correct.
4. PTC "three unauthenticated" — all three GHSA vectors carry `PR:N`; verified via WebFetch on all three advisories. No stray "two" found in the entry. Correct.
5. PTC single-source flag — `verification: single-source` with reasoning present, and the run record's sourcing paragraph (line 388) covers it. Correct.
6. BTR non-breaking-space quotes — all three evidence quotes contain literal U+00A0 and are exact substrings of `btr_text2.txt` (the correctly-flattened text; `btr_full.html`/`btr_flat.txt`/`btr_text.txt` do NOT contain them due to different flattening). Correct.
7. UAT-10147 systemd curly-quote quote — verified verbatim against `talos_spectre.html`/`talos_spectre_text.txt` including the curly `"Before=sysinit.target"` quotation marks. Correct.
8. SPIP affected-systems quote — "Systèmes affectés SPIP versions antérieures à 4.4.21" verified as an exact substring of `spip_certfr.txt` (the actual SPIP CERT-FR advisory; note `certfr-1074.html` in the run directory is a differently-named, unrelated file — it is the Entra ID advisory, not SPIP's). Correct, no splice.
9. GTIG residential-proxy scoping — WebFetched the primary directly; it states "All clusters heavily rely on commercial residential proxies" for the ICE RELIC-linked UNC6293/UNC7005 pairing and separately "UNC5976 uses dedicated infrastructure... rather than residential proxies." Entry's body wording matches this scoping exactly. Correct.
10. UAT-10147 AI-authorship hedge + actor-handle overlap — summary and body both carry "medium confidence" and "a combination of AI-assisted development and human expertise," verified verbatim against `talos_spectre_text.txt`. The "x神"/xshen actor-handle overlap (medium confidence) is also verified verbatim in the same source and is now in the body. Correct.
11. TrueConf range discrepancy — vendor table (`trueconf_vendor_text.txt`) confirms CVE-2026-72530 range is `<5.3.9; 5.4.x<5.4.9; 5.5.x<5.5.5` (no explicit sub-5.3 floor stated separately, i.e., no lower bound) while CVE-2026-72529 explicitly lists `<5.3` as well — exactly matching the corrected `cves[]` and sourcing_note. Correct.
12. TrueConf PHP/JS file — Kaspersky's report (`kl_report_text.txt`) names the overwritten file as `.../httpconf/site/public/js/locale.php` — a PHP file inside the `js` directory. Body and hunt guidance now state this correctly. Correct.
13. TrueConf technique mapping — `techniques[]` carries `T1070` (parent, Indicator Removal — confirmed active/non-revoked in the ATT&CK pin) rather than a Windows-log-clearing sub-technique. Correct.
14. Kairos/Valdemoro citation — the EscudoDigital 2026-05-12 article is now in `sources[]` and its claims (1.8 TB, police reports/DNIs/administrative files, 5 May detection date) verified verbatim against `escudo_valdemoro.txt`. Correct.
15. Kairos contradiction — body now states the Valdemoro article's internal inconsistency (URL slug says "ransomware," background text says "se centra en el robo de datos sin encriptación") — verified against `escudo_valdemoro.txt`. Correct.
16. Entra ID EUVD record — now a cited primary; `euvd-63693.json` confirms `exploitedSince` and `dateUpdated` fields as the entry describes. Correct.
17. misp-stix missing citations — the three added citations were checked against the GHSA pages directly via WebFetch: GHSA-pqpx-w6cx-7q9c (CVE-2026-77710, CVSS 6.9) and GHSA-65gx-wjvj-88j8 (CVE-2026-77755, CVSS 8.7) both support the entry's mechanism descriptions closely. Correct.
18. UAT-10147 victimology citation — "Brazil, Bolivia, China, Canada and Vietnam" / "government, universities, media, technology and gaming" verified verbatim against `talos_ai_text.txt` line 64. Correct.
19. FTP-banner reliability — `sources/sources.json` rates `socradar` reliability `C`; entry now matches (`classification.reliability: C`). Correct.
20. Cisco CVSS count — counted all nine `cvss:` fields directly: five `10.0`, two `9.9` (plus one `7.5` and one `9.6`). Matches "five of them scored 10.0 and two more 9.9." Correct.
21. GTIG missing entity — `actor:midnight-blizzard`'s registered alias "ICE RELIC" now appears multiple times in the body (with attribution language at the correct moderate-confidence hedge). HEADRUSH and ENGINELIGHT are also both explicitly named. Correct.
22. Kairos registry edge — `entities/registry.yaml` line 5262-5265 confirms `type: related-to` (not `attributed-to`) with a note explaining only the actor's own claim connects the incident to it. Correct.
23. Run record discovered_at values — all 15 originally-composed entries carry `discovered_at` between 04:45:00Z and 05:12:30Z, all before the run record's `completed: "2026-08-22T05:14:02Z"`. (The 16th entry, crates-io, was composed later via the R1 recovery pass after the verification loop found the gap, so its `discovered_at: "2026-08-22T06:09:00Z"` — one second after R1 ended at 06:08:59Z — is correctly later; this matches the pipeline's established pattern of `completed` marking composition-phase finish rather than the full run including the verification loop, confirmed against three other recent run records where `verification.iterations[].started_at` also postdates `completed`.) No stale or future timestamps remain. Correct, no regression.
24. Run record action arithmetic — recounted directly from the 16 entry files: 19 actions total across 12 entries (0+1+3+1+1+1+1+2+0+0+2+2+2+2+0+1 = 19), with 4 entries shipping none (btr, kairos, martigny, uat-10147). Matches "Nineteen actions across twelve entries; four of the sixteen ship none." Correct.
25. Run record single-source list — both entry ids named in the "Sourcing and single-source items" bullets (`btr-defender-remediation-driver-ring0-primitive-absence-tell`, `uat-10147-spectre-callback-unlinking-linux-rootkit`, plus `gtig-...` and `ftp-banner-...`) all resolve to real files in `entries/2026-08-22/`. Correct.

### Priority 3 — run-record self-consistency audit

### Unsupported / hallucinated facts

- **F4 (run record).** The `runs/2026-08-22/2026-08-22T0410Z-intel.md` body's "**Priority calibration**" paragraph states: *"Seven entries are `high`: three under confirmed exploitation (the TrueConf chain, SPIP's two flaws, and GitLab's move from disclosed to exploited inside two days), the active Russian espionage campaign against European government and defence identity, an unauthenticated code-execution flaw on a product line already under mass extortion with no obtainable fixed version for two of its three CVEs, a pre-authentication command injection on an internet-facing edge VPN service, and an unpatched trust-decision flaw in the intelligence-sharing library this constituency's own tooling depends on. The remaining eight are `notable`. That is seven `high` across a 48 h window..."* This enumerates exactly seven high-priority items (TrueConf, SPIP, GitLab, GTIG, PTC, TP-Link, misp-stix) and states "the remaining eight are notable" — 7 + 8 = 15, but `entries_published: 16`. Directly counting `priority:` fields across all sixteen entry files gives **eight** `high` entries (the seven named, plus `crates-io-build-script-dropper-yank-lure-arrayref`, priority `high`) and **eight** `notable` entries (0 critical) — 8 + 8 = 16, which reconciles correctly. The paragraph was evidently written before the crates-io entry was recovered by the verification-driven R1 pass and never updated afterward, even though the adjacent "**Action items**" paragraph in the same record *was* correctly updated to "sixteen" and "nineteen actions across twelve entries" (which includes crates-io's three actions). This is an internal arithmetic contradiction within the same document (7+8≠16 against its own `entries_published: 16`) and an undercount of the `high`-priority entries a reader relies on this record to summarise correctly.
  - Suggested fix: revise the paragraph to state eight `high` entries, naming the crates-io supply-chain compromise alongside the other seven, and correct "seven `high` across a 48 h window" to eight.

No other defects found. All 25 remediation items and the newly-recovered entry check out against primary sources fetched fresh in this iteration; the mechanical gate is green (40 pass, 0 warn, 0 fail, re-confirmed at the start of this iteration).

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: run-record
  item: "runs/2026-08-22/2026-08-22T0410Z-intel.md"
  url_or_quote: "Seven entries are `high`: ... The remaining eight are `notable`. That is seven `high` across a 48 h window"
  summary: "7 high + 8 notable = 15, but entries_published is 16. Direct count of priority: fields across all 16 entry files gives 8 high (missing crates-io-build-script-dropper-yank-lure-arrayref, priority: high, recovered later via the R1 pass) and 8 notable, which correctly sums to 16. The paragraph was not updated after crates-io was added, unlike the adjacent Action items paragraph in the same record which was correctly updated to reflect sixteen entries."
```
