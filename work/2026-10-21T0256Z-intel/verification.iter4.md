**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-21T05:01:48Z · ended_at=2026-10-21T05:24:50Z · duration_seconds=1382

## Verification report — 2026-10-21T0256Z-intel (iteration 4)

Scope: post-fix cold pass; all 230 ledger claims decided (`verification.iter4.claims.yaml`: 224 ok, 6 F4), the six new entries, the four updated entries read whole with `git diff HEAD`, the run record, the registry diff, and the nine-item deltas block. Pages read live this iteration with `extract` (php.net, CERT-EU, Sansec, Wordfence, Unit 42, PAN PSIRT, Rapid7, Arctic Wolf, Symantec, Recorded Future, Google, Mozilla, Go announce, BleepingComputer x4, the eMudhra tracker, TeamUpdraft, Patchstack, Nethemba, Sophos, Huntress, Todyl, SpecterOps, Inside IT, Publica, Tamedia standfirst, admin.ch, PKZH, Pensionskasse Post x2, cybercrimepolice, NZZ, watson, Netzwoche x2, swissinfo, Metabase blog, GHSA, Cisco and SonicWall PSIRTs, VenariX), raw `url` (Oracle CPU, CERT-EU dateline, CVE.org API), `pdf` (BPK, BLVK), `cisa-kev` (the catalogue, catalogVersion 2026.10.20), and `WebFetch` for cisa.gov (AA26-293A and the 2026-08-11 KEV alert). Reading limits: the ConnectWise advisory is 403 on every transport today (extract, WebFetch, jina), so ConnectWise advisory claims were checked against the saved read `work/2026-10-19T0256Z-intel/bodies/cw-advisory.md` (update of 2026-10-19 01:15 UTC, which the entry itself bounds); the Tages-Anzeiger article is paywalled (standfirst and key points read, as the entry says). Oracle tallies recomputed from the 1295 risk-matrix rows (112 at CVSS 3.1 9.0 or higher, 90 unauthenticated network, 73 distinct ids, six at 10.0, WebLogic 9.8/9.8/9.1; all hold). `check_run.py` re-run: 59 pass, 0 warn, 0 fail.

Deltas block (iteration-3 findings), each checked against the page:
- n0 F2 (php.net listing): fixed. The anchored permalink `https://www.php.net/archive/2026.php#2026-10-20-1` is in sources[0], the three php.net evidence records, the body link and the CVE index; the page heading links to that same anchor.
- n1 F3 (Oracle login clause): fixed. Summary and body now say Oracle points to My Oracle Support documents; the page says 'Patch Availability Document for Oracle Products, My Oracle Support Note CPU391'.
- n2 F3 (PHP sourcing note): fixed. 'Wordfence repeats it. CERT-EU and Sansec add leak-based claims the project has not confirmed' matches CERT-EU ('according to other leaks') and Sansec ('Information about the embargoed bugs leaked'). CVE.org API returns CVE_RECORD_DNE for both ids and EUVD search returns zero items, so the 'neither CVE id was yet in the CVE.org record service or EUVD' clause holds.
- n3 F3 (APT28 hedge): fixed in the sourcing note and the registry summary; both now put 'moderate confidence' on Recorded Future's attribution of the activity, as the Recorded Future text does.
- n4 F4 (Oracle `rce` tag): fixed. Tags are now `[vulnerabilities, pre-auth, patch-available]`.
- n5 F6 (AA26 `patch-available`): fixed. The tag is gone from all five records; no line asserts a fix exists. A residual on the same five records is F4 #2 below (auth/vector).
- n6 F11 (em dashes): the Metabase paragraph the run edited is clean; the declined residuals remain (advisory #7).
- n7 F11 (eMudhra 'when read'): fixed; 'as of 2026-10-20' matches the tracker's own dateline and its current content (FreeBSD, Node.js and Bun pending; Debian and Fedora have since gone green, which the entry does not claim).
- n8 F11 (living-page records): declined; still an advisory (#8).
Remediations introduced no new defect beyond the findings below.

Changelog contract 4c on the four updated entries: every record's `fields` covers the `git diff HEAD` (PAN-OS: headline, summary, entities, sources, evidence, sourcing_note, actions, body; Publica: headline, summary, tags, entities, techniques, sources, evidence, sourcing_note, body, priority; ConnectWise improvement: sources, evidence, sourcing_note, body; Metabase: regions, sectors, sources, evidence, sourcing_note, body), `updated_at` equals the `update` record's `at` on PAN-OS, Publica and Metabase and is untouched on the ConnectWise `improvement`, each section states what its record summary states, no silent edit, no superseded statement left standing in the main analysis (PAN-OS's 2026-10-11 correction dates Unit 42's 'no lateral movement' line to 9 June, and the new section does not repeat it). Each new section is the same finding as its entry and carries a genuine delta.

### Unsupported / hallucinated facts
- #1 F4 (low confidence) PHP entry, `cves[]` auth/vector. `auth: pre-auth`, `vector: zero-click` on both records. CERT-EU (the only source near it): 'CVSS scores of 9.2, which indicate the potential for unauthenticated remote code execution'; php.net gives no attack detail; Sansec confirms RCE (via watchTowr) but states neither authentication nor vector. Body and title hedge; the machine-consumed fields do not. Null the two fields or carry the hedge.
- #2 F4 (low confidence) AA26-293A entry, `cves[]` CVE-2020-3259 and CVE-2024-40766, auth/vector. KEV: 'An attacker could retrieve memory contents on an affected device' and 'improper access control vulnerability that could lead to unauthorized resource access'; the advisory lists only CWE ids. Cisco's PSIRT page ('unauthenticated, remote attacker') and SonicWall's (AV:N/PR:N) support it but are not cited. Cite them as corroborating sources or null the fields.
- #3 F4 (low confidence) eMudhra entry, `cves[]` CVE-2026-111943 `type: logic-flaw`, `auth: pre-auth`, `vector: zero-click`. Go: 'We're blocking trust in a small set of intermediate certificates due to specific security concerns around their operation. Verify will now filter out chains'; the CVE.org record carries CWE-299 and no vector or authentication. Entry inference, not source statement.
- #4 F4 (low confidence) APT28 entry title and headline. Title: '... used the HOOKEDGE backdoor against a law-enforcement agency, a naval shipbuilder and an aircraft-engine maker in two NATO states, then pushed an SSH key for a persistent tunnel, captured NTLM handshakes and loaded a reflective loader'; headline: '... then tunnelled in over SSH'. Symantec reports the tunnel, NTLM capture and loader only 'During one attack, against the naval shipbuilder'. Summary and body say 'at the shipbuilder'; title and headline do not.

### Citation does not support the claim
- #5 F3 (low confidence) `entities/registry.yaml` incident:emudhra-intermediate-ca-key-compromise-2026-10 summary: 'recoverable because their values were below 256 ... (Google, Mozilla and the incident tracker, 2026-10-20)'. None of the three carries '256'; BleepingComputer (citing Mozilla's bug report) does. The entry body attributes it correctly. Add BleepingComputer.
- #6 F3 (low confidence) `entities/registry.yaml` incident:teamupdraft-updraftcentral-key-theft-2026-10 summary: 'TeamUpdraft says unauthorised access ... exposed UpdraftCentral, UpdraftVault and UpdraftClone connection keys'. TeamUpdraft: 'We believe our customer database was accessed. It holds: ... connection keys for UpdraftCentral, UpdraftVault and UpdraftClone'. Hedge dropped (iteration 1 fixed the same hedge in the entry).

### Editorial / less-is-more flags (advisory)
- #7 F11 residual em dashes: Metabase title ('administrator access to BI instances — exploited since at least 3 August') and older Metabase sections; PAN-OS 2026-06-17 record summary ('European targets — Arctic Wolf'). Declined in iterations 1 to 3, recorded as audit residual.
- #8 F11 living-page records: Publica page is two source records (2026-10-08, 2026-10-20); ConnectWise's source is the Trust Center advisories listing and is unreadable today.
- #9 F11 Publica reading-limit narration: 'the article is paywalled and only its standfirst and key points were read'; source label 'standfirst and key points read'.
- #10 F11 Metabase title 'fifteen downstream victims confirmed' is VenariX's 2026-08-17 count; the 2026-09-29 section says the real total is higher and the 2026-10-21 section adds Republik outside it. Attribute or drop the number.
- #11 F11 PHP: 'today' in headline and action reads stale after the 21 October release; '(16:00 CEST)' is cited to php.net, which does not carry it (Sansec does).
- #12 F11 (low) APT28: 'calls an exported function named ExecuteLoader' is a malware-specific string in the indicator class the style rule bars; the behavior reads complete without it.

### Considered and not flagged
- Oracle CPU at `notable` (no exploitation, no PoC, six unauthenticated CVSS 10.0 rows, Oracle WebLogic/EBS widely deployed): borderline against the PD-11 'beyond the regular patch cycle' test but defensible as a constituency-wide scheduled-release duty; the run record states the reasoning.
- Missed angles: KEV sweep (6 additions, 5 not covered, all dispositioned; Siemens covered), Microsoft October Patch Tuesday (Windows Shell CVE-2026-96951 covered earlier), Ivanti Connect Secure, FortiMail CVE-2026-104286 (entries exist). A search for in-window Swiss public-sector incidents returned nothing dated 20 to 21 October beyond what the run holds. Coverage looks complete.
- Dedup: AA26 declares the SonicWall and Manno entries in `references[]`; TeamUpdraft declares the CVE-2026-10795 entry; no new entry re-covers a store CVE.
- PD-11 style: no IOCs, no em dash in the six new entries (headings excepted), no workflow vocabulary in any reader field, no KEV deadline used as a reason to act, English throughout with `original` kept in evidence.
- Run record notes: counts, dispositions and contradictions checked against `kev-window.txt`, the registry diff and the entries; all hold (duration 7489 s equals started to completed).

### Verdict
NEEDS_FIXES (truth: 6, editorial: 0, advisory: 6)

### Findings summary (machine-readable)
See `work/2026-10-21T0256Z-intel/verification.iter4.findings.yaml` (12 records: F4 x4, F3 x2, F11 x6).
