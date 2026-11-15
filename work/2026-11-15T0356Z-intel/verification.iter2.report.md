**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-15T04:44:55Z · ended_at=2026-11-15T04:51:57Z · duration_seconds=422

## Verification report — 2026-11-15T0356Z-intel (iteration 2)

Scope: all 72 claims of work/2026-11-15T0356Z-intel/claims.iter2.yaml (the 16 changed claims, every other claim of the four entries and the run-record notes; the pass walked the whole ledger, not a quarter). Every cited URL was fetched this iteration (Cursor x2, Fireworks, Microsoft, heise, Phorion, Sophos, NCSC hub post 13121 via ncsc-csh, Apiiro, Sonatype, JFrog, StepSecurity, Huntress, Ransom-ISAC). Apiiro was served by the reader rung of `extract`; the text was complete (all sections, tables and code blocks present).

### Prior-iteration deltas (all 17 walked)
1. Gentlemen title/headline/summary hedge: confirmed, "most likely" present in all three; Ransom-ISAC: "One line in the actor's deployment script most likely lost a race against replication" and "The most likely explanation ... probably extracted those Domain Admin credentials from the legacy server".
2. sectors [] : source names no sector ("a small company", "The victim's infrastructure is confidential"). OK.
3. discovered_at: equals each file's birth time (04:26:40, 04:27:47, 04:28:58) and precedes the clock. The run-record half of the same finding (completed 04:50:00Z, duration 3230) was not addressed: see F4 #3.
4. Run-record entry ids: both exist in entries/2026-11-15/. OK.
5. PolinRider "none relies on an npm install script": Sonatype "The manifests show no consumer install or postinstall hooks"; JFrog "Nothing about it runs at `npm install`" and the camera-check route is curl, dropper, payload.js; Apiiro "Cloning runs nothing", build or folder-open trigger. Supported.
6. ScreenConnect "a guest client needs only the relay address": source says "needs a ScreenConnect server's relay address"; "only" is not in the source: F14 #1.
7. Cursor "Cursor says the attacker could not log in": Cursor notice "the attacker could not have logged in through the tunnel". OK.
8. Cursor "a stolen credential from the exposed data": verbatim from Cursor's report. OK.
9. PolinRider 1,949: Apiiro "1,949 repos were infected again after they were publicly listed" and, separately, "Where owners cleaned up, the stolen access often still worked." OK.
10. "latest outbound transaction" (Apiiro: "It reads the latest outbound transaction of a wallet") and "plain HTTP on TCP port 443" (Sonatype). OK.
11. ScreenConnect 151 s scoped to 29 servers: Huntress "Across 29 servers with complete connection histories". OK.
12. Takeaway opens with 26.6.5 upgrade: Huntress "MSPs should upgrade ScreenConnect host clients to 26.6.5 or later". OK.
13. Cursor record summary and sourcing_note: record summary is clean; sourcing_note is provenance only (five sentences, advisory at most).
14. Gentlemen techniques: T1059.001, T1059.007, T1102.001, T1568 all in Ransom-ISAC's ATT&CK table; T1685/T1685.005 exist in the pinned v20.1 dataset (Disable or Modify Tools; Clear Windows Event Logs). OK. T1490 still unmapped (F11 #1).
15. Declined (inclusion ground): accepted; the entry is a `threat` with transferable behaviour and detection content and claims no victim nexus.
16. ScreenConnect version string: marked "context, not unique on its own" (Huntress IOC table: "context indicator, not unique on its own"); action no longer carries it. OK.
17. Declined (contagious-interview key): accepted.

### Claims
72 rows written to work/2026-11-15T0356Z-intel/verification.iter2.claims.yaml: 70 ok, 1 F14, 1 F4. Cursor update section, record summary, summary, body and both actions verified against Cursor's incident report, Cursor's notice, Fireworks' bulletin, Microsoft, heise, Phorion, NCSC post 13121 (places the extension on Open VSX, as the entry states), Sophos. Evidence quotes: all 10 spot-checked as contiguous substrings of the live pages. Dates: Apiiro 2026-11-09, JFrog 2026-11-09, Sonatype 2026-11-04, StepSecurity 2026-11-13, Huntress 2026-11-14, Ransom-ISAC 2026-11-13, Cursor 2026-11-13, Fireworks 2026-11-09 all equal the cited source datelines.

### Claim not supported / quantifier without source
- F14 #1 (low confidence) ScreenConnect body: "a guest client needs only the relay address embedded in the server's guest installer to register". Huntress: "To register, a guest client needs a ScreenConnect server's relay address, which is embedded in that server's guest installer." No "only". Fix: drop "only".

### Unsupported / hallucinated facts
- F4 #2 (low confidence) ScreenConnect body: "It rejects the public suggestion that the sessions are a malware sandbox detonating installers." Huntress: "after further investigation, this doesn't seem likely." Fix: "judges it unlikely".
- F4 #3 (low confidence) Run record: `completed: '2026-11-15T04:50:00Z'` was written at 04:44:50Z (file birth); the verifier clock read 04:48:42Z and 04:49:53Z; `duration_seconds: 3230` derives from it. Unaddressed half of iteration-1 finding 3. Fix: set the real completed time at finalisation and recompute the duration.

### Claims missing inline citation
- F5 #4 (low confidence) Gentlemen Defender takeaway, last clause ("a GPO of this shape found in a domain is unlinked and deleted, with its Preferences task file, before hosts are cleaned or credentials rotated") is Ransom-ISAC's response order but carries no citation.

### Needs more research
- F8 #5 (low confidence) Cursor `**Exposure:**` still names only extension hosts; the update's second exposure class (non-Privacy-Mode agent traces with credentials, credentials sent to support, Cursor's "If you did not receive a notification, your data was not in these traces") appears only in actions[1].

### Editorial / less-is-more flags (advisory)
- F11 #6 (low confidence) Gentlemen techniques[] omits T1490 although Ransom-ISAC's table lists it ("The locker deletes the shadow copies and the change journal as part of its cleanup").

### Missed angles
None evidenced. KEV catalogue 2026.11.13 has no addition dated after 2026-11-13 (the run note holds); NCSC hub newest post 13178 of 2026-11-13 (Red Hat Quay, already carried by entries/2026-11-14/red-hat-quay-signing-key-takeover-cve-2026-123710.md); the CVEs surfaced by a news search (CVE-2026-20245, -102764, -104935, -111357, -118527, -124194) are all already in state/cves_seen.json. Coverage looks complete for the window; no Swiss communal or cantonal incident surfaced for 2026-11-14/15.

### Other checks passed
Dedup: no prior entry covers the Apiiro, Huntress or Ransom-ISAC posts; PolinRider declares the GhostAction entry in references[]; the ScreenConnect entry declares the CVE-2026-84869 and SCKit entries; Gentlemen and EtherRAT keys exist in the registry (no alias miss). Classification present and coherent on all four (B/2, B/2, C/2 matches ransom-isac tier C, B/1). Priorities (all notable) fit. No em dash in reader-facing text, no IOC hashes, IPs or wallet addresses, no workflow-internal vocabulary in reader fields. Cursor changelog contract (4c): record `at`/`updated_at` match, section present, diff shows no uncovered change, `discovered_at`/`run_id` untouched, main analysis consistent with the newest section.

### Verdict
NEEDS_FIXES (truth: 3, editorial: 2, advisory: 1). All six findings are low confidence and low severity; none changes a fact a reader acts on except the F14/F4 wording on ScreenConnect.

### Findings summary (machine-readable)
See work/2026-11-15T0356Z-intel/verification.iter2.findings.yaml (6 records).
