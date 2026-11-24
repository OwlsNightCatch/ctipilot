**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-24T05:53:04Z · ended_at=2026-11-24T06:07:13Z · duration_seconds=849

## Verification report — 2026-11-24T0355Z-intel (iteration 5)

Scope: post-fix pass. All 155 claims of `claims.iter5.yaml` have a verdict row in `verification.iter5.claims.yaml` (150 ok, 5 F3 rows that fold into 2 findings); this covers the 7 changed claims, every claim of the Project Zero and APIM entries, and, with no time limit, every other claim of the other seven entries (no sampling). `python3 tools/claim_ledger.py 2026-11-24T0355Z-intel --coverage 5`: 155/155 answered, 0 missing. Every cited page was fetched this iteration (`extract` for articles, `pdf` for the Optimizely report, `url --direct` for the EUVD record, the Equinor HTML (JSON-LD dates) and the Kristiansen HTML, `msrc cve` plus the SUG affectedProduct API, `bsi-csaf`, `ncsc-nl csaf`, CNA records from cveawg, `cisa-kev` plus WebFetch for the CISA alert). `git diff HEAD` read for both updated entries.

### Prior-iteration deltas (3), each re-fetched

- #1 Project Zero title: fixed. Title now says "is expected to remain a protected-process bypass"; the post says "this wouldn't change the behavior in PPL therefore that should still be bypassable".
- #2 Project Zero "hooks and audits": fixed. `grep -i "audit\|hook"` on the entry returns nothing; summary, main analysis and Detection line use "protection code that checks/expects to check the loaded image section", the post's wording ("Any protection code which is expecting to check the loaded image section will not see the load").
- #3 Equinor date note: fixed and correct. JSON-LD `datePublished` 2026-11-17T17:55Z, `dateModified` 2026-11-20T08:12Z; the page's Update 20 November 2026 08:55 CET matches the citation date.

### Citation does not support the claim

- #1 [F3] `2026-11-24/azure-api-management-classic-secrets-exposed-nsm-advisory`: Kristiansen citation date (claims bb5a7fcca6, 11d3330233, and `sources[]`).
  - Entry: "[Anders Kristiansen, 2026-11-23]"; `sources[].date: "2026-11-23"`; sourcing_note: "Anders Kristiansen's page carries a metadata date of 2026-11-05 that precedes the events it describes, so its citation date is the date SecurityWeek linked it."
  - Page (raw HTML header, `url --direct`): `Created <relative-time datetime="Sat, 21 Nov 2026 09:00:00 +0100">` and `Modified <relative-time datetime="Sat, 21 Nov 2026 09:00:00 +0100">`. The string 2026-11-05 appears nowhere in the HTML (it is a trafilatura artefact), so the sourcing_note's premise is wrong and the page does carry a usable dateline, two days before the cited date. Check 2(e): two or more days is F3. Content of both clauses is supported (hunting map, log sources, Management API, developer portal).
  - Fix: cite 2026-11-21 in `sources[]` and both inline citations; replace the sourcing_note sentence (or delete it).
- #2 [F3, low confidence] same entry: exposure boundary (claims c0adee5805, d485a8ad7c, dadb26034d).
  - Entry body: "an unauthorized party could have used it to reach secrets stored in Azure API Management Classic instances before Microsoft acted"; action: "Microsoft's notice says Classic instances were exposed before its 2026-11-19 mitigation"; summary: "closed the access path on 2026-11-19, and says Classic instances were exposed before then".
  - SecurityWeek: "the tech giant discovered the issue on November 18 and closed the access path the next day" and the quoted notice "an unauthorized party could have used the issue to access secrets stored in Azure API Management Classic instances before Microsoft identified the security issue". The notice anchors the exposure to identification (2026-11-18), not to the closure or to "acted".
  - Fix: "before Microsoft identified the issue"; keep 2026-11-18 and 2026-11-19 distinct in the summary and action.

### Editorial / less-is-more flags (advisory)

- #3 [F11, low confidence] `2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router`: the Optimizely PDF is titled "Nov 17 2026" with a revision log (17 Nov corrected, 18 Nov corrections, 20 Nov "shortened report"); the entry cites it as 2026-11-20 (the version read) and the body says "shortened on 2026-11-20", but sourcing_note does not state the first-issue date as it now does for Equinor. One clause would settle it; may be left.
- #4 [F11, low confidence] `2026-11-24/babidighost-jailbroken-ai-agent-belgium-france-switzerland`: SOCRadar's ATT&CK table also lists T1585.002, T1587.001 and T1059.006; none is in `techniques[]` and the body does not describe the behaviours. May be left.

### Checks that came back clean (no finding)

- Project Zero entry, all 22 claims: the post (author James Forshaw, 2026-11-23) supports the flat-mapping fallback, the one-bit COFF flag change with no checksum fix-up, regasm `/unregister` without administrator rights, the WLDP inequality check that Windows 11 S Mode satisfies, 44Con, late-September report, October fix, WerSecureFault.exe PPL result, "should still be bypassable", Dynamic Code Security off by default. MSRC SUG record: Important, 8.8, publiclyDisclosed Yes, exploited No, release 2026-10-13, 24 affectedProduct rows, fixed builds 4.8.9363.0 / 4.8.10008.0 (26H2 only) / 4.8.4811.0 / 4.7.4150.0, KB5126868, KB5127666 to KB5127668, KB5127683 to KB5127694. Oracle CSPU: CVE-2026-87268 7.8, 7.2.16, Note 1 Windows host only, "earlier versions ... likely affected", Rev 1 2026-September-15, credit James Forshaw; CNA record datePublished 2026-09-15. The three evidence quotes are contiguous. All changed claims (61204fad09, 8911d0e39a, 2551c403d0, 9fa1ede07f, 039b280805, 74d8db5dfb, 62396b0341) are `ok`.
- APIM entry, remaining claims: NSM page (Norwegian originals of all three evidence quotes contiguous; RuntimeVersion thresholds 31936 / 31938; "Artikkelen er oppdatert 23. november"), SecurityWeek, Equinor, Skagerak and Kristiansen content all match.
- Changelog contract (4c), both updated entries: `git diff HEAD` changes exactly the fields each record names (Vates: title, summary, entities, cves, sources, evidence, sourcing_note, tags, body; OptimJack: sources, evidence, sourcing_note, actions, body); `updated_at` unmoved in both; section headings equal `at`; no silent edit; no supersession (the Vates "no CVE assigned" statements are gone; the OptimJack 04:21 versus 07:51 disagreement is stated, not resolved). Vates: EUVD record (assigner GitHub_M, published Nov 23, 9.8, "actively exploited in the wild", fixed 6.9.2 and 6.10.1), GHSA (2026-11-20, "The attacker does not choose which token", one-request PoC) and the Vates advisory (Critical, 2026-11-10, xo-server 5.213.1 / 5.211.2, detection items) support every sentence; BleepingComputer does name 6.9.1 and 6.10.0. OptimJack: the Optimizely PDF supports 07:51 / 13:34 / 16:10 / 22:24 UTC, the exposure window, the hosted-iframe carve-out, the withdrawn guidance and the eight customer actions; both new evidence quotes are contiguous; Krebs (dateline 2026-11-17) supports 68 / 50 / 24 (15 percent); Report URI supports 04:21 first injection, 188 snippets / 178 organisations and own-domain snippets; Zscaler, Hudson Rock, Ohey, Optimizely status and Amirul match the older claims I re-read.
- BabidiGhost (SOCRadar, ZATAZ x2), Entra (BleepingComputer, Netzwoche), N-able (N-able blog, THN, SecurityWeek, GHSA, CISA alert plus KEV bridge `dateAdded 2026-11-23`, BOD deadline not used as a reason to act), F5 (THN; BSI CSAF lists only CVE-2026-123637 and the five fixed-build ranges; NCSC-NL CSAF 12 CVEs, Kans medium / Schade high; all six F5 CNA records: 9.8 and 9.3, Kheirkhah credited on four, F5 on two, the BIGIP-...-ENG and BNK-...-EHF1 names) and Symantec: every cited sentence, number, date and evidence quote traces to the page.
- Dedup: no new entry shares a CVE with an existing one (CVE-2023-38646 only in BabidiGhost as background); all `entities[]` keys exist in the registry and the 12 registry additions in `git diff HEAD` equal the run record's `entities_added`; the other "API Management" entries in the store concern different products.
- Style: no IOC, no em dash outside changelog headings, no pipeline vocabulary in reader-facing prose; classification letters and numbers consistent with source tiers and corroboration; priorities (APIM `high`, rest `notable`) defensible.
- Run record: counts by kind, KEV disposition, source promotions, registry additions, contradiction notes and single-source ratings hold against the entries and `git diff HEAD`.
- Missed angles: none found. A search of the public THN front page for 2026-11-21 to 2026-11-23 items (ScreenConnect CVE-2026-84869 exploitation, Idunno.AntiCsrf, Java4Shell, NGINX2Root, Ruby2Shell, GL.iNet, Webworm, SAP NetWeaver, Cisco Expressway, VMware vCenter, Roller, MONAI, Ghostscript) found each already in the store (several as changelog records), and the standing sweeps for Chrome, Outlook, Plone and Barracuda hit existing entries. Coverage looks complete on the critical/high signal. (Considered and not raised: the F5 entry's primary sources are BSI and NCSC-NL because F5's K-article is a JavaScript shell on every transport; THN and F5's CNA records carry the vendor facts.)

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 2)

Both truth findings sit in the APIM entry and are small edits: finding #1 is the Kristiansen dateline (2026-11-21, with the sourcing_note premise corrected), finding #2 (low confidence) is "before Microsoft identified the issue". All three iteration-4 remediations verified correct.

### Findings summary (machine-readable)

See `work/2026-11-24T0355Z-intel/verification.iter5.findings.yaml` (4 records: F3, F3 low confidence, F11 low confidence, F11 low confidence).
