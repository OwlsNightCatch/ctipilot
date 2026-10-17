**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-17T04:11:09Z · ended_at=2026-10-17T04:30:17Z · duration_seconds=1148

## Verification report — 2026-10-17T0256Z-intel (iteration 2)

Scope: 1 new entry, 5 updated entries (each read whole, `git diff HEAD` walked, record `fields` checked against the diff), the run record, the registry additions. Ledger `claims.iter2.yaml`: 190 of 190 claims carry a verdict row in `verification.iter2.claims.yaml` (184 ok, 6 non-ok, all six also appear below). Pages fetched fresh this iteration: GTIG (extract plus raw HTML for its six tables and date meta), METAL (extract plus raw HTML date), AOMEI changelog, Atlassian advisory, EUVD record API, CVE Services record (CVE-2026-21589, CVE-2026-111357), NVD record, Previdian, The Register (raw HTML), GHSA, Volexity, CERT-FR (raw version table), CCCS, Rapid7, CISA, Ivanti blog, NCSC-CH post 13032, MSRC SUG per-CVE records, Exchange Team posts 4563014 and 4565382 (page JSON-LD), PKZH (both pages), Pensionskasse Post 260 and 263, Inside IT 2026-10-16, BPK and BLVK PDFs, PaperCut bulletins (27 Aug and Sept) and web-services documentation, Hunt.io (extract and raw date), GreyNoise (extract and raw HTML), watchTowr (both posts). Cached quote-bodies were used for the stable pages (Netzwoche, watson, admin.ch, Publica, PK Softech, NZZ, Cybercrimepolice, SwissCybersecurity.net, SANS, Huntress, tickets).

### Iteration-1 deltas: each fix checked against its source

1. AOMEI "METAL's EDR recorded the chain on Backupper 8.3.0": correct (METAL: "That record became the starting point for reconstructing the chain on AOMEI Backupper 8.3.0").
2. AOMEI dllhost.exe clause: now cited to METAL, which carries it ("dllhost.exe instances hosting COM components registered from non-standard paths"). Correct.
3. PK Softech "not affected" / "early 2027": now cited to the PKZH 2026-10-15 page, which carries both. The added "Inside IT reports the same" over-binds (finding #5 below).
4. PK Softech Defender takeaway: each clause now carries its own cite; PKZH FAQ, Pensionskasse Post 263, BPK ("keine Hinweise ... nicht restlos ausgeschlossen"), BLVK and Cybercrimepolice (Löhne und Vorsorgeguthaben) all support their clauses. Correct.
5. Atlassian 607/65/20: date-qualified, but the page now reads 613 / 66 / 21 (finding #4, low confidence).
6. PaperCut 24.1.10 / 24.1.11: correct against the bulletin fetched fresh (Last updated October 13, 2026: CVE-2026-82077 "Fixed in ... 24.1.10 for the 24.x branch"; recommendation "24.1.11 on the 24.x branch"). Summary, `cves[CVE-2026-82077]` and the 10-17 section are consistent with it.
7. PaperCut evidence quote: now verbatim ("(26.0.5, 25.0.13, 24.1.11)").
8. PK Softech record summary: now says Pensionskasse Post "no longer repeats" its anonymisation statement; correct (notice 263 omits it, notice 260 carries it).
9. Run record counts: "245 relevant, 1 stale" matches `source_health.out2`; the S2 header versus findings telemetry is noted. Correct.
10. PaperCut "all versions" sentence: now cites Rapid7, which carries it.
11. AOMEI Triage / NitroRuntime: the Triage line and the body now carry the Nitro PDF camouflage and the second scheduled task (GTIG "Camouflaged Follow-on Activity"). Correct. The same edit left a stray token (finding #1).
12. PaperCut v24 target 24.1.11: correct.
13. PaperCut XML-RPC detection: now present and supported by Hunt.io (`api.setConfigValue`, `api.lookUpUserNameByCardNo`, disable the endpoint, `user-lookup.*`, `custom/web/`).
14. PKZH earlier checking line: now surfaced in the 10-17 section; the section states the contradiction in plain words.
15, 16, 17, 22: declined with rebuttals. Checked against the files: the DD-Automation reason now matches `findings.S2.yaml` (Army: no interfaces; only Inside IT; one technique id on a leak-site claim); the Republik drop matches S2's own borderline reason ("Drop if the composer judges it adds nothing") and the Metabase entry does carry credential rotation; the Norwegian lead matches S3 ("primary (DN) not reached"); the GTIG date follows the page meta (`published_time` 2026-10-16T21:02Z, first-published 2026-10-16 21:10) against JSON-LD/dateline 2026-10-15, one day apart, not a defect. Not re-raised.
18. PaperCut em dashes: none left in title, summary, frontmatter or body outside the section headings.
19. AOMEI T1614 and T1059.001 added and supported by GTIG; the rest of the mapping gap is finding #6.
20. Ivanti title, headline, summary and immediate action re-dated to "at disclosure"; the Defender takeaway was not (finding #2).
21. PK Softech actions[0] now 135 words; PaperCut actions[0] unchanged (146 words).

### Missing inline citation (F5)

1. aomei entry, Triage: "Radmin is legitimate software, so provenance discriminates: METAL's EDR recorded the backup program itself installing it {m}." The sentence ends on a literal unresolved `{m}` token and carries no citation. METAL says "ManageEngine EDR recorded AOMEI Backupper installing Radmin" and its process table shows `upgrade-now.exe` (unsigned) dropping the components and `rsetup64.exe /intsetup` installing Radmin Server. Replace the token with the METAL link; consider "an AOMEI updater child process launching a Radmin installer", since the installer was started by the dropper.

### Unsupported / hallucinated facts (F4)

2. (low confidence) cve-2026-104935 Defender takeaway: "the root-escalation step stays unfixed and the Integrity Checker cannot clear it." Only Volexity (2026-10-13) says a fix was coming "in the coming weeks"; the entry's newest section says "no source read says whether any build now fixes it". Title, headline, summary and immediate action were re-dated, this line was not.
3. (low confidence) papercut actions[0]: "because the route Hunt.io recovered needs neither the Tapestry bypass nor an unpatched build when the allowlist is too permissive or no token is set." Hunt.io: "A PaperCut instance that has already been hardened against the Tapestry bypass is not necessarily protected against this one if its XML-RPC API is exposed with weak access controls." No fetched source says a patched build is exploitable through that route.

### Citation does not support the claim (F3)

4. (low confidence) cve-2026-21589 summary: "607 attempts from 65 addresses in 20 countries as of its 2026-10-16 update". The cited Previdian page ("Updated 17 Oct 2026") now reads 613 attempts, 66 unique IPs, 21 countries, last observed 16 Oct. The figure cannot be confirmed from the page.
5. (low confidence) publica-pk-softech Update 2026-10-17: "plans to move to PK Softech's system in early 2027 ([PKZH]); Inside IT reports the same". Inside IT: "Die PKZH setzt aktuell noch auf einen anderen Softwareanbieter, will aber 2027 auf das System von PK Softech wechseln"; no "not affected", no "early". Reword to what Inside IT carries.

### Editorial / less-is-more flags (advisory, F11)

6. aomei techniques[]: GTIG's Table 6 still maps T1140, T1564.004, T1573.001, T1001.001, T1016, T1082, T1033, T1583.001, T1583.006, T1608.001, T1027.013, T1219.002; METAL maps T1574.002. The "word limit" reason does not apply to metadata.
7. sourcing_note fields: Atlassian (7 sentences; "readable in the record's data, not on the rendered page"), Ivanti ("not readable without a browser"), PK Softech (5+ sentences): fetch-transport remarks and per-source narration; rule 12 wants two sentences of provenance.
8. publica-pk-softech: title 50 words, summary 248, body about 1,965 words for an incident with no vector, actor or ransom detail; the defender content is the identity-proofing rule and the test-data-at-supplier lesson.
9. cve-2026-104935 Improvement: CCCS AV26-1035 Update 1 (already a cited source) states "Open-source reporting indicates that CVE-2026-111357 is being exploited in the wild"; the section relies on the GitHub mirror alone.
10. (low confidence) exchange summary and Defender takeaway: "Windows Server cumulative updates"; both Exchange Team posts say "Windows Server updates".
11. (low confidence) carry-overs: actor-chosen task names in the AOMEI Detection and action; PaperCut actions[0] names 24.1.11 and 24.1.10 in one sentence and chains four tasks; "more than 35,000 dummy sections" (GTIG: "over 35,000 lines of repetitive configuration sections").

### Missed angles

None found. Coverage looks complete for the critical/high signal: the KEV sweep (two additions, both covered), the EUVD exploited list (ten records, covered), Patch Tuesday's exploited Windows Shell flaw (covered on 2026-10-14), and a Swiss-incident web search turned up nothing new in window. The Republik, DD-Automation, Arkadia and Norwegian leads are dispositioned in the run record with reasons that match the findings files.

### Checked and clean

Atlassian rejection (EUVD record: assigner atlassian, dateUpdated Oct 16 2026 8:39:09 PM, exploitedSince Oct 15; CVE Services state REJECTED, dateRejected 2026-10-16T20:39:09Z; advisory fetched today unchanged, same fixed versions incl. Crowd 7.1.7, no rejection note; NCSC-CH post 13032 edit of 2026-10-12 verified); Ivanti improvement (GHSA text verbatim, published Oct 15, affected 22.8R2.4 only, no fixed build; record `fields` match the diff); Exchange update (post JSON-LD datePublished 10/17/2026 1:00:38 AM; every symptom, KB, registry value and caveat matches; MSRC per-CVE records: Critical 8.1 AC:H, 9.3, Exploitation More Likely, exploited No); PK Softech 10-17 section (PKZH, Pensionskasse Post 263, dates); PaperCut 10-17 section (every Hunt.io figure: 1,005 hosts / 45 countries / 800+205 / 2,165 attempts / 46 domains / 45 live pivots / Switzerland listed / CERT sharing; Hunt.io displayed date Oct 15 2026; PaperCut docs keys; T1053.003, T1572, T1090.001, T1003.004, T1552 in Hunt.io's mapping). Registry additions match the AOMEI entry, no name collision. `updated_at` mirrors correct; Ivanti `improvement` leaves it. Classification and `verification` values consistent with sources. Run-record counts (25 notes, KEV, health sweep, EUVD list) hold.

### Verdict

NEEDS_FIXES (truth: 4, editorial: 1, advisory: 6)

### Findings summary (machine-readable)

See `work/2026-10-17T0256Z-intel/verification.iter2.findings.yaml` (11 records).
