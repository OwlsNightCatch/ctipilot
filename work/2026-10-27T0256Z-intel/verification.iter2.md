**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-27T04:27:09Z · ended_at=2026-10-27T04:46:55Z · duration_seconds=1186

## Verification report — 2026-10-27T0256Z-intel (iteration 2)

Scope walked: 3 new entries, 8 updated entries (whole text, `git diff HEAD`, `entry_record.py diff` against each record's `fields`), the run record, and all 232 ledger claims (rows in `verification.iter2.claims.yaml`: 215 ok, 5 F3, 6 F4, 1 F14, 5 unreadable; `claim_ledger.py --coverage 2` reports 232/232). Every claim of the changed file and of every remediated entry was decided against a page fetched this iteration (live `extract`, `pdf`, `cisa-kev`, `ncsc-csh post 13105`, WebFetch for the CISA alert); the older pages of the PHP, ARTEX and Brotli entries were re-read from `work/<run-id>/quote-bodies/` where unchanged.

### Generic / oversight URLs (replace with specific article)

- **#6 F2 (low confidence)** `php2shell-ot-products-...`, `https://www.wibu.com/support/product-alerts.html`: the decline reason ("no per-advisory permalink exists") does not hold. In the page HTML the PHP advisory is its own content element (`<div id="61269" ...><a id="c61269" class="u-anchor-link">`, followed by "Last updated on: 2026-10-23 7:00 pm CEST (CodeMeter License Central PHP Vulnerabilities)") and holds only this advisory; `https://www.wibu.com/support/product-alerts.html#c61269` would pin the citation when newer alerts land above it. Optional.

### Citation does not support the claim

- **#1 F3** `pan-os-panorama-php2shell-mgmt-interface-no-fixed-release` (2026-10-27 section) and `php-critical-release-pre-announced-cve-2026-109618-109619` (body): Palo Alto revised its advisory at 2026-10-27T04:03:00Z, after the entries were written (03:40Z and 03:48Z). Live JSON timeline: "2026-10-27T04:03:00.000Z Removed the ETAs for 12.1.7-h11 and 12.2.4-h1 as these versions are released." Live table: "| PAN-OS 12.2 | < 12.2.4-h1 | >= 12.2.4-h1 |" and "... >= 12.1.4-h13 (ETA: 10/29) >= 12.1.7-h11 >= 12.1.10-h3 (ETA: 10/30)" with no ETA on the two released builds, so eleven hotfixes are out. Entry text: PAN-OS section "No hotfix for PAN-OS 12.2 or 12.1 is out yet and only one for 11.2"; body "Install the hotfix released for your maintenance line (10.2.13, ... 11.2.10)"; PHP body "with nine hotfixes released and the rest due by 2026-10-30". Fix: re-fetch the advisory, amend this run's unpublished records on both entries (a later revision may follow before publish; the ETAs run to 2026-10-30).
- **#3 F3 (low confidence)** `qnap-synology-...` Exposure line: "or a QNAP device running QVR Surveillance below 3.0.3.1756, TVR OS below 1.0.5, Note Station 3 or QNE (ADRA)" cites QSA-26-18, which lists "QVR Surveillance 3.0.3 and earlier (ARM32 models)Resolved QVR Surveillance 3.0.3.1756". The ARM32 qualifier is dropped (also in the Defender takeaway); the action keeps it.
- **#4 F3 (low confidence)** `camping-care-...` Defender takeaway: "updated to 8.5.12, 8.4.27, 8.3.36 or 8.2.35 or to a vendor backport ([CISA, 2026-10-26])". The CISA alert (WebFetch, verbatim) says "Organizations should immediately update to PHP 8.5.12, 8.4.27, 8.3.36, or 8.2.35" and does not address vendor backports; php.net 2026-10-21 ("Some distributions and LTS vendors provide backported fixes") carries that clause. Add the PHP citation or drop the clause.

### Unsupported / hallucinated facts

- **#2 F4** `pan-os-panorama-...` frontmatter, same source revision as #1: headline "Palo Alto: nine PAN-OS hotfixes for PHP2Shell are out, 12.2 and 12.1 still wait"; summary "none yet for PAN-OS 12.2 or 12.1"; `cves[].fixed` "estimated dates: 12.2.4-h1 (10/28); ... 12.1.7-h11 (10/28)"; actions[0] (nine-build list and "due 2026-10-27 to 2026-10-30"); record summary "none yet for 12.2 and 12.1". Now 12.2 has its hotfix and only 12.1.4-h13 and 12.1.10-h3 of 12.1 are still estimated. The Brotli advisory (CVE-2026-111497) was last revised 2026-10-26T23:40Z and still shows 10/28 ETAs for the same builds, so the Brotli entry stays correct as cited.

### Quantifier without source

- **#5 F14 (low confidence)** `php-critical-release-...` summary: "the only production victim reported is a Swiss booking-system supplier whose theft SRF links to the PHP flaw". No source says "only"; Blick, cited in this entry and in the Camping entry, writes "Camping.Care ist nicht der einzige Softwareanbieter, dem die beiden kritischen PHP-Sicherheitslücken zum Verhängnis wurden", and the Camping entry itself reports that. Say "the one production victim the sources name" or drop the quantifier.

### Editorial / less-is-more flags (advisory)

- **#7 F11** `qnap-synology-...`: QSA-26-18 names the product "Notes Station 3" ("Notes Station 3 3.9.14 and earlier", "Updating Notes Station 3"). Iteration 1 asked for one spelling; the entry standardised on "Note Station 3" (title, headline, summary, body, `affected_products` "QNAP Note Station 3"), a form no source uses. Use the vendor's name (the registry key can stay).
- **#8 F11** `gheist-...`: advisory, may be left. The action's "ci-sync- plus six random characters ... sync-check.yml" and Detection's "user agent gheist" are Wiz's published indicators (file-name indicators fall under the no-IOC rule; kept so the action is executable). Also, Wiz states "Gheist is distinct from GhostAction", the store carries the 2026-10-10 GhostAction entry (stolen credentials pushing malicious workflows), and `references: []` carries nothing; one clause of disambiguation plus the reference would spare readers the conflation.
- **#9 F11** `php2shell-ot-products-...` sourcing_note: "the Security Expert fixed version are read through SecurityWeek's summary of the vendors' notices, and the Schneider Electric notice was read only in part". The `pdf` tool returns the bulletin's text (SESB-2026-295-01 v2.0.0), which carries "Version 1.48.4.0 of Security Expert includes a fix for this vulnerability"; the Defender takeaway can cite Schneider for 1.48.4.0, and the second sentence (fetch narration, now inaccurate) can go.
- **#10 F11 (low confidence)** run record notes: "connectwise-trust-center (403 on every transport, eighth consecutive failing run)" while `sources.json` and `sources_changed` carry `consecutive_fetch_failures` 5 (last successful fetch 2026-10-19). Iteration 1 raised the count; only the `fetch_failures` message was changed. For information: `check_run.py --pre-verify` now FAILs `run-record` (residual count 0 on a NEEDS_FIXES iteration) and `run-clock` (completed 03:58:00Z precedes the verifier iterations); both belong to the Phase 6 re-stamp and are not entry defects.
- **#11 F11** summaries against the 1 to 3 sentence contract: PHP 4 sentences (about 200 words), Apple 4 (113 words, +27 this run), QNAP 4 (131 words). PHP and QNAP were already 4 before this run; PAN-OS (5 to 3) and Brotli (3) comply.

### Prior-iteration deltas (all 23 records re-walked against live pages)

Confirmed correct: Splunk ("Smartlook | Remedied", changelog 2026-10-26), Fortinet FG-IR-26-186 (only FortiDDoS, FortiSOAR, FortiSOAR PaaS under investigation; FortiClient Cloud Services remediated; 2026-10-26 revision), Cisco v1.7 of 2026-OCT-26 (15.5.21 with no date qualifier; URWB 27.1.1 Feb 2027), WatchGuard ("completed our assessment", no "initial"), Gheist (variant undated; only the self-hosted job "On October 19 ... Hours later"), roundup versions (HMS "3.00.11", Wibu "5.2.2", Belden macmon 7.x patch; SecurityWeek has "Johnson Controls has released patches for several Illustra product lines", no "camera firmware"; "Bern-headquartered" in Belden's 2022 release), Camping (Dutch and Touring Club Schweiz from Blick; title "15'000 Gäste vorsorglich"; Defender takeaway now hedged), Brotli Exposure (each clause on its own page), QNAP (QuMagie absent from QSA-26-18 and from cves, affected_products and entities), Apple (lever now names 18.7.11), PHP F4 reword (consistent across summary, body, section and record summary), Talos entry gone (counters 3 and 8 match disk). Declined items reviewed: priority of the NetScaler and PAN-OS entries stays `notable` (KEV lists PHP, not the products; PAN scores availability only; doubt resolves to notable, no finding); the Citrix Tech Zone post is 403 on `extract`, `url`, `jina` and WebFetch, so the five NetScaler claims are `unreadable`, with CTX697263 and the KEV record supporting what is readable.

Missed angles: coverage looks complete. NCSC.ch hub list (13105 and the 22 and 23 October advisories all in the store), the Swiss-news searches and the PHP2Shell follow-up search found nothing relevant that is neither in the store nor in the run record's borderline-drops.

### Verdict

NEEDS_FIXES (truth: 6, editorial: 0, advisory: 5)

### Findings summary (machine-readable)

See `work/2026-10-27T0256Z-intel/verification.iter2.findings.yaml` (11 records: F2 1, F3 3, F4 1, F14 1, F11 5).
