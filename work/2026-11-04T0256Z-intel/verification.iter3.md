**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-04T04:48:10Z · ended_at=2026-11-04T05:08:31Z · duration_seconds=1221

## Verification report — 2026-11-04T0256Z-intel (iteration 3)

Role: post-fix pass after the iteration-2 NEEDS_FIXES. Scope walked: all 14 changed claims in `claims.changed.iter3.yaml`; every claim of the five entries the remediation touched (Cisco 30, Ivanti 31, Barracuda 20, cPGuard 15, 3AM 11); a seeded random quarter of the rest (30 of 122 claims of the Binance, Publica, Danfoss, WordPress and Vaud entries, seed 20261104); and, because the pages were already fetched, further claims of those entries. 211 claim rows are in `verification.iter3.claims.yaml`. Not walked: 18 pre-existing Publica and Danfoss claims outside the sample whose pages (BPK, BLVK and Pensionskasse Post pages and PDFs, Tages-Anzeiger paywall, Le Monde, Forescout, the Dixell PDF) were not read.

Iteration-2 deltas, each re-fetched:

1. Barracuda sourcing_note date: confirmed. Both Mandiant files carry `## Disclosure Timeline ... 2026-11-02: CVE published and Mandiant advisory released` (raw .md and rendered blob).
2. Cisco CVE-2026-76443 wording: the "states ... separate finding" and "explicitly distinct" text is gone; "listed separately from" and "in the same weakness class as" match footnote 2 of the hardening advisory (rev 1.1). Correct. (The lead phrase "a separate finding from the same ... review" survives and is acceptable as "one of the five listed CVEs".)
3. Cisco section: the "had said none" clause is gone; the section states only revision 1.1 of 2026-10-14. Correct.
4. Ivanti `fixed` and sourcing_note: CERT-FR AVI-1442 and ALE-013 both read "25.1.2.x antérieures à 25.1.3.1"; EUVD-2026-98816 reads "before version 25.1.3.0"; Rapid7 resolves 25.1.3.0 and 25.1.3.1. The rewritten text matches. See F9 #3 for earlier sections that still describe the pre-2-November text.
5. Registry: the 3AM summary now says an EDR removal attempt that anti-tampering blocked (matches Bitdefender). The cPGuard summary matches the disclosure on entry point, 2,950 servers, 02:08 to 03:20 UTC and 5.88.26, but see F4 #1.
6. Run-record notes: Barracuda mechanism text, cPGuard figures (2,950 and 7,900 in the entry; 32 files and 2,946 only in the sourcing note), `_main_words` 737 to 735 (Danfoss) and 1,158 to 1,148 (Publica) all recomputed with `check_run._main_words` and hold; source-health counts (291 probed, 287 relevant, 1 stale, 3 unreadable) match `source_health.out`; the KEV disposition matches `kev-window.txt`.
7. cPGuard takeaway co-citation: advisory says "Reset passwords for root and all other password-enabled local Linux accounts from a trusted recovery environment". Correct.
8. 3AM takeaway: each clause is Bitdefender's ("Alert on the creation of any new domain trust", "Put domain trusts and domain-admin accounts behind change control, and alert on every one", "credential-reading access to backup-software databases and on reg save of the SECURITY, SYSTEM, or SAM hives", "Put an endpoint agent on every machine", "Limit them to known management hosts"). Correct.
9. Barracuda ranges and patch ids: Mandiant MNDT-2026-0041 raw lists "ESG <= 9.4.0.27, ADC <= 6.4.0, WAF <= 11.0.1, WSG <= 16.1.100.100, BMA <= 5.5.4.0, WCC <= 2.2.1"; the Trust Center table (read from raw HTML) gives BNSF-40425 (9.4.017+), BNSF-40430 (<9.4.017), BNADC-16586 (ADC and WAF), BNMA-32468, BNWF-60060, BNYF-24789. Correct. Firmware 9.4.0.030 exists (Campus ESG release notes list "Version 9.4.0.030").
10. cPGuard Exposure paragraph: the advisory/disclosure pairing is now stated; see F5 #4 for the uncited trailing clause.
11. cPGuard summary caveat: present ("the vendor's logs do not record the exact request that gave access"); disclosure: "Our logs do not record the exact request that gave them access".

Other cold-pass checks: evidence quotes of the four new entries are literal on their pages (Barracuda Trust Center, Campus, Mandiant, OPSSHIELD disclosure and advisory, Binance, FBI, Bitdefender); CVSS 9.3 and 8.6 match the Trust Center and Mandiant; CVE-2026-111357 CVSS 7.0 and affected 22.8R2.4 match the CVE record (cveawg); CVE-2026-118527 CVSS 4.3 matches the EUVD vector; KEV dates (2026-09-14, 2026-10-13, 2026-10-30, 2026-11-03) match the catalogue and the CISA pages; `check_run.py --pre-verify --no-link-check` exits 0 with only the expected counter and run-clock FAILs; no em dash, IOC, KEV deadline or workflow vocabulary in reader-facing text; classification, org_triage and watchlist fields conform; actions lists are short and concrete. Coverage: searches for in-window items beyond the run's (zero-day patches of 3 November, Swiss communal incidents of 3 November) surfaced nothing new; coverage looks complete. One omitted detail, not flagged: heise (cited on the Danfoss entry) says the BSI issued a warning and WDR reports the EU Commission calling two crisis meetings; the entry is already over its word bound.

### Unsupported / hallucinated facts

- F4 #1 (low confidence) `cpguard-update-channel-hijacked-backdoor-root-secrets` summary and `entities/registry.yaml` `incident:opsshield-cpguard-update-channel-compromise-2026-11`. Summary: "but copied credentials stay usable until rotated"; registry: "credentials copied before cleanup stay usable until rotated (OPSSHIELD, 2026-11-03)". Source (https://opsshield.com/notice/cpguard-update-channel-compromise.html): "A successful update removes the known files, but credentials copied before cleanup may still be usable." The body keeps the hedge; frontmatter and registry drop it, and the registry cites the 2026-11-03 disclosure, which does not carry the sentence. Restore "may still be usable" and attribute to the advisory.

### Claims missing inline citation

- F5 #4 (low confidence) `cpguard-update-channel-hijacked-backdoor-root-secrets`, Exposure: "and the later disclosure narrows the fake update to 02:08 to 03:20 UTC without repeating a version range or withdrawing that check." The paragraph cites only the earlier advisory; the disclosure (`.../security-incident-disclosure-servermanage.html`, "2 Nov, 02:08-03:20 | cPGuard agents install the fake update", no version range) is not cited there. Add it.

### Surface contradiction

- F9 #2 (low confidence) `cve-2026-76461-cisco-secure-email-gateway-sqli-root-rce`. Body: "Cisco states the vulnerability 'was found during the resolution of a Cisco TAC support case' (meaning it surfaced from a real customer's compromise investigation, not internal fuzzing)" against the new "Cisco's advisory, revised on 2026-10-14, says two vulnerabilities found in the review are known to be actively exploited: this SQL injection and the separately advised arbitrary file write" and the summary's "two vulnerabilities from its internal review ... this one". cisco-sa-esa-inj-2bLVGmhX: "This vulnerability was found during the resolution of a Cisco TAC support case." cisco-sa-hardening-esa-dfCrfXkm: "These vulnerabilities were found during internal testing. Two of them are known to be actively exploited. For more information, see [SQL Injection] and [Arbitrary File Write]." Cisco's two pages disagree on how the SQL injection was found; the entry carries both without a Contradiction line.
- F9 #3 (low confidence) `cve-2026-104935-ivanti-connect-secure-zero-day-chain-kev`, 2026-10-21 section "CERT-FR still lists 25.1.3.x builds before 25.1.3.1 as affected ([CERT-FR, 2026-10-14](.../CERTFR-2026-ALE-013/))" and 2026-10-16 section "does not list a 25.1.2.x line", against the same alert page now (updated 2 Nov): "Connect Secure (ICS) version 25.1.2.x antérieures à 25.1.3.1 ... Ivanti précise que les versions 25.1.3.x ne sont pas affectées par ... CVE-2026-111357 et CVE-2026-118527", which the 2026-11-04 section states. The earlier present-tense statements stay unqualified. Also the 2026-10-31 section's "CVE-2026-118527 has no public CVE record, affected range or fixed build yet" is superseded by the 2026-11-03 record. Qualify them as the text of their date.

### Editorial / less-is-more flags (advisory)

- F11 #5 `cve-2026-116606-barracuda-esg-auth-bypass-root-rce`, Exposure: "which should read 9.4.0.029 or later after the update" while the action and takeaway say 9.4.0.030 or later (the Mandiant record lists builds before 9.4.0.030 as affected). Say 9.4.0.030 there.
- F11 #6 `threeam-uk-school-veeam-rogue-domain-admins-new-ad-trusts`, `techniques[]`: Bitdefender's table also maps T1490 (wbadmin deletion of system-state backups), T1555.003, T1059.006, T1021.006, T1078.002, T1105; none is present. T1490 is the most useful to add.
- F11 #7 (low confidence) `cpguard-update-channel-hijacked-backdoor-root-secrets`: the advisory is labelled 2026-11-02 in `sources[]` and three inline citations; its dateline is `<time datetime="2026-11-03">3 November 2026</time>` (last updated 3:19 AM IST) and BleepingComputer (2026-11-03) says OpsShield "published an alert earlier today". One-day drift, possibly timezone; advisory only.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 3, advisory: 3)

All four blocking findings are low-confidence, one-sentence edits; every remediation from iteration 2 was confirmed correct against the live sources. On every other claim in scope the run is clean.

### Findings summary (machine-readable)

See `work/2026-11-04T0256Z-intel/verification.iter3.findings.yaml` (7 records: F4, F9, F9, F5, F11, F11, F11).
