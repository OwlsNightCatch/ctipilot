**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-17T03:46:23Z · ended_at=2026-10-17T04:05:45Z · duration_seconds=1162

## Verification report — 2026-10-17T0256Z-intel (iteration 1)

Scope: 1 new entry, 5 updated entries (whole entries read, `git diff HEAD` walked), the run record, registry additions. Ledger `claims.iter1.yaml`: 179 of 179 claims carry a verdict row in `verification.iter1.claims.yaml` (170 ok, 9 non-ok). Sources fetched this iteration: GTIG (extract plus raw HTML, whose six tables `extract` drops), METAL, AOMEI changelog, Atlassian advisory, CONFSERVER/CWD tickets, EUVD record API and CVE Services records (CVE-2026-21589, CVE-2026-111357), Volexity, Rapid7 (both), CERT-FR, CCCS, GHSA, Exchange Team posts (10-13 and 10-17, from page JSON-LD), MSRC per-CVE and CVRF 2026-Oct, PaperCut bulletins and docs, Hunt.io, Huntress, GreyNoise, watchTowr, PKZH / PK Post / Inside IT / admin.ch / PK Softech / Publica / BPK / BLVK / NZZ and the other cached bodies. Every evidence quote of the six entries was literal-searched against the cached bodies: one now fails (finding #7); the ENISA quote verified through the record API.

### Citation does not support the claim (F3)

1. aomei entry, body para 2: "METAL reproduced the chain on Backupper 8.3.0 ([METAL, 2026-10-16])". METAL: "That record became the starting point for reconstructing the chain on AOMEI Backupper 8.3.0" (from EDR telemetry) and, under "Why we could not reproduce it", "The same HTML file arrived ... No executable arrived." Reword to "METAL's EDR recorded the chain on Backupper 8.3.0".
2. aomei entry, Detection: "a signed Radmin binary loading an unexpected DLL, and dllhost.exe hosting a COM server registered beside it; scheduled tasks ...; outbound SMB ... ([GTIG, 2026-10-16])". dllhost.exe appears only in METAL ("dllhost.exe instances hosting COM components registered from non-standard paths"; "signed dllhost.exe surrogate"). GTIG's text and its six tables (read from raw HTML) never name dllhost.exe as the host (only the SecOps rule name "Suspicious Process Invoking Dllhost Clsid Invocation"). Add the METAL cite to that clause.
3. publica-pk-softech, Update 2026-10-17: "PKZH still runs another provider's system, which is not affected, and plans to move to PK Softech's system in early 2027 ([Inside IT, 2026-10-16])". Inside IT: "Die PKZH setzt aktuell noch auf einen anderen Softwareanbieter, will aber 2027 auf das System von PK Softech wechseln." "Not affected" and "Anfang 2027" come from the PKZH page.
4. publica-pk-softech, Defender takeaway: the sentence chains PKZH's theft statement, Pensionskasse Post's "data left" and the Bernese funds' status, and ends on one cite, Cybercrimepolice, which carries only the investment-fraud warning and names no fund. Add the PKZH and Pensionskasse Post cites to those clauses.
5. (low confidence) cve-2026-21589 summary and Update 2026-10-16: "607 attempts from 65 addresses in 20 countries by 2026-10-16". The cited Previdian page now reads 613 attempts, 66 unique IPs, 21 countries ("Updated 17 Oct 2026", "Last observed 16 Oct 2026"). Date-qualify the earlier figure ("through 2026-10-15") or refresh it.

### Unsupported / hallucinated facts (F4)

6. papercut-ng-mf (summary, actions[0], cves[CVE-2026-82077].affected/fixed, Update 2026-10-10): "the vendor lists as fixed only in 26.0.5 and 25.0.13", "does not list for 24.1.10", "the vendor's bulletin names no fixed 24.x release", "it names no 24.x release". The September bulletin, fetched fresh ("Last updated October 13, 2026"), reads: "CVE-2026-82077 ... Fixed in: PaperCut NG/MF 26.0.5; 25.0.13 for the 25.x branch; 24.1.10 for the 24.x branch." and "You are affected if you are running PaperCut NG/MF earlier than 26.0.5 (or 25.0.13 on the 25.x branch, 24.1.10 on the 24.x branch)." The page changed three days after the entry's 10-10 text; the current-state fields now contradict it.
7. papercut-ng-mf evidence[]: "If you have already upgraded to the latest release (26.0.5, 25.0.13) the issues are already addressed." The page now reads "(26.0.5, 25.0.13, 24.1.11)"; the quote is no longer verbatim.
8. (low confidence) publica-pk-softech, record 2026-10-17T03:35:30Z summary: Pensionskasse Post's notice "replac[es] its earlier anonymisation statement". Notice 263 does not retract it; notice 260 is still live ("Festzuhalten ist, dass die Daten der Pensionskasse Post bei PK Softech AG anonymisiert sind."). The section body ("does not repeat") is right; align the record summary.
9. Run record notes: "the second health sweep reports 246 of 246 relevant" vs `source_health.out2` "245x relevant, 1x stale" (no UNSOLVED row is correct); S2 telemetry websearch 27 / bridge 130 vs `findings.S2.yaml` self_telemetry 24 / 120.

### Claims missing inline citation (F5)

10. (low confidence) papercut-ng-mf body para 4: "PaperCut treats **all versions** of NG and MF as potentially affected." No cite in the sentence; the next cite is Huntress, which does not carry it. Rapid7: "PaperCut currently considers all versions of PaperCut NG and PaperCut MF potentially impacted."

### Needs more research (F8)

11. aomei entry: Detection names the scheduled task NitroRuntime with no explanation. GTIG describes the mid-July follow-on (ADAPTAGENT, the Adaptix C2 client, masquerading as Nitro PDF tools, sideloaded Eztwain4.dll, hidden PowerShell launch) and warns it "can mislead analysts into treating alerts as isolated, user-initiated software downloads". The Triage line omits this discriminator.
12. papercut-ng-mf: summary, actions and `fixed` name 24.1.10 as the v24 target "vendor's recommended build". The 2026-10-13 bulletin recommends "26.0.5 (or 25.0.13 on the 25.x branch, 24.1.11 on the 24.x branch) or later" and lists CVE-2026-14780 (Print and Device Scripting RCE, authenticated admin, optional feature) fixed in 24.1.11 (released 11 October 2026).
13. papercut-ng-mf: the second XML-RPC route has a hardening action but no detection line. Hunt.io supplies the telemetry (POSTs to /rpc/api/xmlrpc invoking api.setConfigValue or api.lookUpUserNameByCardNo from non-allowlisted sources, followed by user-lookup.* writes) and advises egress filtering on PaperCut servers.

### Surface contradiction (F9)

14. (low confidence) publica-pk-softech Update 2026-10-17: the PKZH page still carries "Die PKZH klärt derzeit ab, ob ... auch Daten der PKZH betroffen sind" beside "Nachdem sich diese Vermutung bestätigt hat". The run record names this contradiction; the entry carries no Contradiction line.

### Missed angles (F10)

15. (low confidence) (a) Republik (Zurich) Metabase intrusion, first Swiss confirmed victim of an exploited flaw the store already covers, ten-week patch lag (Inside IT 2026-10-16): a changelog record on `2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally` may earn a paragraph; query "Republik Metabase Datenleck". (b) DD-Automation / Safepay (S2.1): Swiss Army logistics supplier chain; the run-record reason "no vector, actor or behaviour beyond the impact" does not fit it, since S2 names Safepay and T1657; query "DD-Automation Safepay Armasuisse". (c) The S3 Norwegian armed-forces rental-car lead was left "for S2 or the operator" and never followed. Otherwise coverage looks complete for critical/high signal: the KEV sweep, the EUVD exploited list and the S1 to S4 drops hold against their findings files.

### Org-triage / priority (F16)

16. (low confidence) publica-pk-softech `notable`: PKZH now confirms theft of City of Zurich insured persons' and pensioners' data (AHV number, IBAN, salary) and Publica (federal administration, ETH domain) says data presumably left; the call-back decision is due within days. May clear the `high` bar (incident in the constituency's sector and supply chain).

### Editorial / less-is-more flags (advisory, F11)

17. (low confidence) aomei sources/event_date: GTIG dated 2026-10-16; its visible dateline and JSON-LD say 2026-10-15, page meta published_time says 2026-10-16T21:02:24Z.
18. papercut-ng-mf: 1 em dash in the title, 2 in the summary, 15 in the body (older text); style rule 12.
19. aomei techniques[]: GTIG's own mapping adds T1614, T1059.001, T1140, T1564.004, T1573.001, T1001.001, T1016, T1082, T1033; METAL maps T1574.002; none is in `techniques[]`.
20. (low confidence) cve-2026-104935 title/headline/summary: present-tense "root step has no fix" rests on Volexity's 2026-10-13 sentence; the newest section says "no source read says whether any build now fixes it". Qualify as of Volexity's report.
21. (low confidence) publica-pk-softech actions[0] (about 175 words, per-fund status clauses that will age) and papercut-ng-mf actions[0] (about 145 words, four tasks in one): consider splitting.
22. (low confidence) aomei Detection and actions[0]: task names and install-tree folder names read as indicator strings (rule 12); similar artifacts exist elsewhere in the store.

### Checked and clean

Atlassian update (EUVD record, CVE Services state REJECTED dateRejected 2026-10-16T20:39:09Z, assigner atlassian, exploitedSince 2026-10-15, advisory unchanged and without a rejection note), Ivanti improvement (GHSA text verbatim, published 2026-10-15, affected 22.8R2.4 only, no fixed build; record `fields` match the diff), Exchange update (all workaround facts and KB numbers verified in the post's JSON-LD; fixed builds and the 9.3/8.1 scores in MSRC CVRF), PK Softech 10-17 section (PKZH, Pensionskasse Post, dates), PaperCut 10-17 section (every Hunt.io figure, the PaperCut docs keys, T1053.003/T1572/T1090.001/T1003.004/T1552 all in Hunt.io's own mapping). Registry additions match the entry; no name collision; no overlap with prior coverage. `updated_at` mirrors are right (non-internal `update` records at the new `at`; Ivanti `improvement` leaves it). Frontmatter and body agree except as listed.

### Verdict

NEEDS_FIXES (truth: 9, editorial: 7, advisory: 6)

### Findings summary (machine-readable)

See `work/2026-10-17T0256Z-intel/verification.iter1.findings.yaml` (22 records, same order as above).
