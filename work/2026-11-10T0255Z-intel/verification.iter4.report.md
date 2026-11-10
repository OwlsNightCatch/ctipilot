**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-10T05:14:57Z · ended_at=2026-11-10T05:38:28Z · duration_seconds=1411

## Verification report — 2026-11-10T0255Z-intel (iteration 4)

Scope walked: all four new entries and all seven updated entries read, `git diff HEAD` read for every updated entry (declared `fields` versus changed frontmatter keys compared programmatically: no undeclared change, no declared-unchanged field; last record, `## Update` section and `updated_at` agree on all seven), run record read, `check_run.py` run with the live link check (60 pass, 0 warn, 0 fail). Claim ledger: all 7 claims of `claims.changed.iter4.yaml`, every claim of the four entries remediated this round (OpenSSH 29, N-able 23, SonicWall 24, FreeSWITCH 19) and a seeded random quarter of each of the other seven entries (PK Softech 11 of 44, Ahsay 7 of 27, Danfoss 10 of 39, Barracuda 6 of 26, SAP 5 of 21, IBM 3 of 13, BluePhishing 3 of 11). 140 verdict rows in `verification.iter4.claims.yaml` (139 ok, 1 F3). `claim_ledger.py --coverage 4` reports 140/276 answered, the remainder being the unsampled three quarters of the non-remediated entries.

### Prior-iteration deltas (each remediation checked against the cited page)

- OpenSSH rebuild advice cited to OX: OX carries it verbatim ("Rebuild them from a fixed base and redeploy."). Correct.
- OpenSSH CVSS 3.1 8.1 attributed to OX: the OX affected-versions table has a "CVSS v3.1" column with "8.1 High"; GreyNoise's timeline reads "Published to NVD CVE-2026-123158, CVSS 8.1.", so the sourcing_note sentence is right. Correct.
- OpenSSH "GreyNoise's confirmed successes are on its own gridpoints, and no source reports a compromised production host": the GreyNoise page says "we have confirmed vulnerable gridpoints deployed", "An attacker exploited a vulnerable GreyNoise gridpoint", victims #1 to #4 are gridpoints. BleepingComputer, SecurityWeek, The Hacker News, Previdian, SANS ISC and Defused report attempts, botnet and miner activity or a honeypot, and none reports a compromised production host. Correct (BleepingComputer's phrase "networks protected by GreyNoise" does not contradict GreyNoise's own "gridpoint").
- OpenSSH sourcing_note no longer narrates a fetch failure. Correct.
- N-able "No source has validated the individual claims" cited to Censys: Censys says "no source has validated the proof-of-concept code" and "None of it has been validated". Correct. Exposure sentence "can give attackers a path to the systems it manages": Field Effect "a compromised N-central server can give attackers a path to downstream systems". Correct.
- SonicWall CVE record without NSv model numbers: accurate but incomplete, see advisory #3 (the numbers were right and are now readable).
- FreeSWITCH BSI date: the BSI portal shows "04.11.2026" next to "SignalWire FreeSWITCH <1.11.3", CSAF aggregate severity "kritisch", initial release 2026-11-04T23:00Z, revision 2026-11-05T23:00Z. Rating, version range and 2026-11-04 are supported. Correct. GHSA sidebar: CVSS:3.1 9.8, `<= 1.11.2`, `>= 1.11.3`, published 2026-10-28. CISA alert and KEV catalogue list CVE-2026-116779 (dateAdded 2026-11-09). Correct.

### Citation does not support the claim

#1 (F3, low confidence) 2026-10-10/ahsaycbs, Update 2026-11-10T03:45:06Z: "it cannot say how many credentials were retrieved, has not identified the implant family and has not seen what was downloaded ([Huntress, 2026-11-09](https://www.huntress.com/blog/ahsaycbs-webshells))". Huntress has no such statement. The credentials and implant-family clauses match ("We cannot say how many of those credentials were retrieved", "We have not identified the malware family"); the third clause has only a distant relative about the nsmind.jsp webshell: "We did not see logs showing `download` in use, so we cannot say what, if anything, was taken." The entry's wording presupposes that something was downloaded and, after the Veeam sentence, reads as exfiltration having occurred; the sourcing_note already says "what was taken". Fix: "and cannot say what, if anything, was taken through the webshell's download action".

### Editorial / less-is-more flags (advisory)

#2 (F11) 2026-11-10/n-able Exposure: "Field Effect says several of the published proofs of concept describe unauthenticated attack paths, so network reachability is the prerequisite to remove". Field Effect: "Several of the published PoCs describe unauthenticated attack paths, so if they work as described, network reachability is a prerequisite for exploitation." The conditional is dropped from the prose (it survives in evidence[]). Add "if they work as described".

#3 (F11) 2026-11-07/sonicwall sourcing_note: "that capture did not include the affected and fixed build table, so the fixed builds are those read on 2026-11-06 and the NSv model numbers are not listed". Fetch-limit narration ("capture") in a reader-facing field, and stale: the PSIRT page loads its content from `https://psirtapi.global.sonicwall.com/api/v1/vulndetail/?advisory_id=SNWLID-2026-0014`, which returns the full table: Gen7 hardware TZ, NSa and NSsp plus "Gen7 NSv - NSv 270, NSv 470, NSv 870 (ESX, KVM, HYPER-V, AWS, Azure)", 7.3.3-7015 and older, fixed 7.3.4-7013 and higher; Gen8 hardware TZ and NSa plus "Gen8 NSv - NSv XS, NSv S, NSv M, NSv L (ESX, KVM, HYPER-V, AWS, Azure)", 8.2.2-8015 and older, fixed 8.2.3-8015 and higher. Revision history there: "Version 1.1 Date 09-Nov-2026 ... The Workaround section has been updated for CVE-2026-19868". The NSv model numbers dropped last round were correct; the record may restore them and the note reduce to provenance.

#4 (F11) update-record summaries (rendered on the site) carry frontmatter field names, a registry-style tag and record-keeping narration: OpenSSH "the CVE record, tags, techniques, headline, summary and actions move to exploited"; Barracuda "the CVE record, tags, headline and title move to exploited"; FreeSWITCH "the CVE record, tags, sources, evidence, summary and action move to cisa-kev"; Danfoss "Title, headline, summary and analysis no longer say ... and the summary is condensed"; Ahsay "the follow-on paragraph is shortened to make room"; SonicWall "The entry's statements that there is no workaround are corrected". About ten earlier records in the store use the same style, so this is a standing pattern, advisory only.

#5 (F11) FreeSWITCH title and headline still read "vendor says exploited" after the KEV update; OpenSSH, IBM and SonicWall lead with CISA's listing. Not false; optional.

#6 (F11) PK Softech summary is 331 words and Danfoss 233 words; the Zug clause was appended to an already very long summary. Optional condensation.

### Checks that came back clean

- Updated-entry contract (4c): each last record carries run_id 2026-11-10T0255Z-intel and type `update`; every non-internal record has its `## Update` section; `updated_at` equals `at`; no changed frontmatter key outside `fields`; no superseded statement survived (Barracuda "no source reports attacks", SonicWall "no workaround", FreeSWITCH "the vendor's alone" were replaced).
- New entries: IBM bulletin 2026-11-07 (CVSS 9.8, vector PR:N, "authorized" versus CISA's "authenticated" disclosed, 5.0.19 PL1 on Linux, Workarounds None, KEV 2026-11-09); SAP, four EUVD records (descriptions, 10.0 vectors with S:C, notes 3849308, 3778556, 3778530, 3798345, version lists, EPSS 0.0, published 2026-11-10); BluePhishing (Proofpoint page: AgentIdentity.CreateAsManager cannot be revoked, 250 identities, User.Read.All and Group.Read.All, "Add application"/"Add service principal", MC1506733, no in-the-wild activity; dateline "November 09, 2026" and JSON-LD datePublished 2026-11-09, while `article:published_time` says 2026-11-07, which the run record already discloses); N-able (Huntress, BleepingComputer, Field Effect and Censys agree with every statement; the two earlier N-central entries exist).
- Barracuda: Barracuda's Nov 9 9:00pm EST update, the full patch table (BNSF-40425 9.4.017+, BNSF-40430 <9.4.017, BNADC-16586 for the Load Balancer ADC and WAF, BNMA-32468, BNWF-60060, BNYF-24789), Campus "All versions of the Email Security Gateway (ESG)" and 9.4.0.029, Mandiant 0042, Canadian Cyber Centre Update 1, NCSC post 13144 (created 2026-11-03, still UNKNOWN).
- Danfoss new section: foreign ministry text (night of 11 to 12 October, Shahid Kaveh, "première campagne cyberoffensive opérée purement à des fins de sabotage"), CERT-FR report (faisceau d'indices, FOFA, CyberbanNews from 13 October, Farsi traces, Schneider hydro installations, Modbus port 502), Sekoia (26 addresses, xml.cgi, account-rename attempt on 1 November, similarities, NoName057(16) assessed with doubts), Reuters via NBC (arrest warrants, could not establish how the French made their determination), Ransom-ISAC (588 + 155 = 743 writes, two Administrator sessions).
- PK Softech Zug section: Inside IT 2026-11-09 carries every statement; Tages-Anzeiger "rund hundert Gigabyte"; IPCT letter figures; Pensionskasse Post, BPK, NZZ (Libera) and the Publica newsletter PDF ("Die Hackergruppe Akira wird mit dem Angriff in Verbindung gebracht") all match.
- Ahsay follow-up: five webshell families, "simply tried every likely location", kvm task, Python implant gated on a MachineGuid hash marker, tooling list, Veeam command, re-image and credential rotation advice, and the first post's "full host re-image ... secondary backdoors for extended persistence" all match.
- Style (check 12): no em dash outside headings, no IOCs (IP, hash, domain scan clean), no workflow vocabulary in entry text, English throughout. Classification blocks present and within vocabulary; no org_triage, no watchlist.
- Run record notes: counts (four new, seven records, ledger sizes 19/26/14/10), KEV dispositions and the Proofpoint date note hold against the entries, `kev-window.txt` and the pages.

### Missed angles

None evidenced in the window. The Zyxel GS1900 zero-day (CVE-2026-107441, Binarly and Zyxel advisory of 2026-11-03, SecurityWeek 2026-11-05) predates the 26 h window and no earlier fire covered it either; named only as an observation for the operator, not a finding: query "Zyxel GS1900 CVE-2026-107441 Binarly exploited".

### Considered and not raised

- SAP Exposure: "the SAML2 flaw applies only where the SAML 2.0 service provider is configured ("under certain configurations")" is a gloss on SAP's wording that the record's product name supports; left as is.
- FreeSWITCH, IBM Aspera Faspex and OpenSSH priorities (`notable`): no constituency-exposure evidence either way, so no F16.
- The CISA KEV JSON feed as a corroborating source on the IBM entry: established in 103 entries.
- SAP raw EUVD API links, SAP patch-day relevance and GPUStack: standing declines.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 5). The one truth finding is a low-confidence wording fidelity gap in the Ahsay Update section; everything else I walked held, including every changed claim and every remediation from iteration 3.

### Findings summary (machine-readable)

See `verification.iter4.findings.yaml`.
