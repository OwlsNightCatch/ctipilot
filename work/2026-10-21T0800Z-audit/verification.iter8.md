**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-21T20:31:39Z · ended_at=2026-10-21T21:05:49Z · duration_seconds=2050

## Verification report — 2026-10-21T0800Z-audit (iteration 8)

Scope walked: all 151 claims of `claims.iter8.scope.yaml` (the 1 changed since iteration 7, all 16 claims of the Chaindrop entry and the 2 of Fox Tempest, the seeded quarter), each against its cited page fetched this pass (`extract`, raw HTML for Register, Aikido, Onapsis, Fortinet CSAF, Check Point embedded page data, ENISA EUVD API, MSRC API, Red Hat security-data API, CISA KEV feed via the bridge, `WebFetch` for the Pixel bulletin, a Wayback copy of the two OX Security posts that every direct reader refuses). Every row of `verification.iter8.claims.yaml` is `ok`. Also read against disk: the run record, the report, the tracker (`STATUS.md`, `plan.json`), `work/cleanup/wave-06/findings-W1-I.md` and the wave-06 kickoff.

### Prior-iteration deltas (iteration 7, nine findings), each re-verified
- F4 report "Uncitable values" (Ninja Forms): fixed. The bullet now says the alias keeps no score and that EUVD-2026-84282 carries WPScan's 8.8; the EUVD API returns CVE-2026-92438, assigner WPScan, 8.8, CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H, ninja-forms 3.15.3 <3.15.4. The Virtualizor records (EUVD-2026-84620/84622/84624, CVSS 4.0 only: 9.3, 9.2, 8.7) and EUVD-2026-30514 (9.3, CVSS 4.0) hold. The W1-I file carries the Ninja Forms item.
- F11 Kemp W1-I bullet direction: fixed. It now reads that the GA and LTSF labels sit under an EUVD citation whose record carries neither; EUVD-2026-34260 lists bare ranges. Correct.
- F11 ShieldBreak "not expected on supported versions": carried, still in the 2026-08-24 section (LevelBlue: "The file is not expected to exist natively on supported Windows versions"). Listed again below.
- F11 Fragnesia Aikido date: carried. Nuance found this pass, see F4 #2.
- F11 Chaindrop 08:24:07Z record summary: fixed. It now ends at "latent capability rather than observed behaviour", which the section and Unit 42 ("In this sample, the installer was decrypted but never invoked. The routine that pipes it to bash has no call site, so treat OS-level persistence as latent capability, not observed behavior") carry.
- F11 Oracle September CSPU label: carried to W1-I. The carried bullet is false, see F4 #2.
- F11 Fox Tempest em dashes: fixed. Both `sources[].publisher` labels use commas; the record's `fields` now name `sources`; no reader-facing em dash is left in the entry outside headings.
- F11 report "Folds": fixed. "The W4 rows run in waves 03, 06, 08 and 12" equals `plan.json` (W4-01/03/04/05 wave 03, W4-02 wave 06, W4-06 wave 08, W4-07/08/09 wave 12).
- F11 next-wave line: fixed. Gates match `plan.json`: 09 and 10 have empty `after`, 12 after 04 and 05, 11 after 03 to 10 and 12.

### Tracker and report against disk and origin/main
- `git fetch`: origin/main is still `5a2e81bf` (the branch base). `plan.json` differs from origin/main in exactly this wave's delta (wave 02 rows done with counts, W1-I entries and note, totals, next_wave, wave 02 `done` with the expected summary placeholder, waves 06 to 08 `ready`, the log line). `render_status.py --check-lanes` passes (waves 03 to 08 pairwise disjoint). A render written to a scratch path is byte-identical to `docs/cleanup/STATUS.md`. Disk totals: 1002 entries, 388 pending, 18 legacy entries under this run id; rows 29 done / 2 declined / 7 in a wave / 18 open; W1-B 50 of 57 and W1-E 19 of 26 carry a record, W1-C 5, W1-F 8, W1-H 0 (declined with reason), W1-I 73 entries.
- Records table: 72 rows, regenerated from the records on disk by my own script: type, internal flag and field sets equal on every row (61 improvements of which 18 internal, 11 corrections of which 1 internal; 19 internal records). The 13 "without a record" rows match the 13 entries of the plan rows with no record.
- State diffs: `state/cves_seen.json` (1 added, CVE-2026-92438; 33 `last_seen` moves, all 2026-10-21; 4 titles: CVE-2026-33691, -44772, -58704, -73570), `entities/registry.yaml` (FTAPI summary, LiteLLM `first_seen`, 4 product records), run-record durations and token sums equal their stamps. Commit hashes cited (731706f, 1f8d69e, ea6e509, b511bbe, 17506d0) exist; the first two are on main. Spot-checked report statements hold: PHP SOAP CVE-2026-7262 2.9 beside 6.3 (EUVD-2026-28971), the eight Liechtenstein evidence rows with originals, IBM IFDT503301.
- The gate (`check_run.py 2026-10-21T0800Z-audit`) exits 0: 59 pass, 2 warn, 0 fail. The Pixel WARN is a transport gap: `WebFetch` of the bulletin reads "There are indications that CVE-2026-58704 may be under limited, targeted exploitation.", Published September 15, 2026, High, EoP, Modem, A-484011314, patch level 2026-09-05 (footer "Last updated 2026-09-30"). The prompt-version WARN is the expected v4.22/v4.23 trail.
- Scan of the 72 new records and sections for workflow-internal language (this entry, frontmatter, registry key, sub-agent, wave, changelog, field names): clean. Em-dash scan of the 72 entries outside headings and append-only records: only the verbatim quotations in the coding-agent and Entra entries.

### Unsupported / hallucinated facts
- F4 #1: report line "which also carries the six verifier advisories this wave did not fix (Kemp twice, ShieldBreak twice, the RoguePlanet citation label and the Check Point IKEv1 priority)". `work/cleanup/wave-06/findings-W1-I.md`, section "wave 02 verifier, pre-existing advisories carried forward", holds eight bullets (the six plus the Ninja Forms alias score and the Oracle CSPU date, added by iteration-7 remediation); 53 bullets in the file, 45 worker residuals and 8 verifier advisories. The wave-06 kickoff says "W1-I (45 residuals the wave 02 repair workers and verifier left unfixed, on 73 entries)", which counts only the workers' residuals. Fix both counts.
- F4 #2: the last W1-I bullet, "Oracle September 2026 CSPU: no fetched page states the 2026-09-15 citation label, and the page metadata says 2026-09-10", is false. The Oracle page body carries "| 2026-September-15 | Rev 1. Initial Release. |"; 2026-09-10 is only the Updated Date metadata. Drop or reword so wave 06 does not change a correct date. Low-confidence companion: the Aikido bullet says the page's metadata dates it 2026-04-07 against the entry's 2026-09-04; the page's raw HTML carries `datePublished: 2026-09-04` in an embedded Article JSON-LD block beside the header's "Apr 7, 2026" and "Sep 7, 2026".

### Editorial / less-is-more flags (advisory)
- F11 #3 Flink record 08:08:02Z (low confidence): the record summary says the takeaway treats the email wave as evidence an actor holds breach data "not as a measure of its scope"; the takeaway says "not as unrelated spam". Amend the record or the clause.
- F11 #4 Kemp (carried, low confidence): GA and LTSF labels sit under the EUVD citation in the Exposure line and the 2026-07-02 section; EUVD carries bare ranges. Tracked in W1-I.
- F11 #5 ShieldBreak (pre-existing, carried): the quoted "not expected on supported versions" is not a substring of LevelBlue's sentence.

Notes with no finding: cyber.gov.au returned 503 to every reader this pass, so the ACSC alert's own 25 September date rests on repair-5's saved copy (page metadata 2026-09-25) and Cyber Daily's 24 September; the Citrix support bulletin CTX697174 is an Angular shell, so "The Citrix pages for this flaw list no signs of compromise" is confirmed on the TechZone post only; ox.security posts were read on Wayback copies (the tensorlake post says "kill the gh-token-monitor persistence first ... Otherwise, revocation triggers rm -rf ~/"; the keyv post says "dead man's switch trigger, to delete the current machine if the stolen GitHub token is revoked" and "extortion string"). The Chaindrop 2026-10-11 clause "removing the npm dependency alone does not remove that persistence" is carried by Socket alone, which terminates the cite with OX; acceptable as written.

Coverage looks complete for this audit's scope (no research spawn, no re-sweep).

### Verdict
NEEDS_FIXES (truth: 2, editorial: 0, advisory: 3)

### Findings summary (machine-readable)
See `work/2026-10-21T0800Z-audit/verification.iter8.findings.yaml` (5 records: 2 F4, 3 F11).
