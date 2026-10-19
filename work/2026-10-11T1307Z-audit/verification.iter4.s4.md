# Verification report: 2026-10-11T1307Z-audit, slice s4, iteration 4 (post-fix)

**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-19T16:27:20Z (ended_at in `verification.iter4.s4.ended_at`)

## Verification report — 2026-10-11T1307Z-audit (iteration 4, slice s4 plus the fire's own documents)

Scope: 27 entries, 236 ledger claims (236 answered in `verification.iter4.s4.claims.yaml`: 233 ok, 2 F3, 1 F4), the iteration-3 deltas block (25 findings), `docs/audits/2026-10-11-quality-audit.md` and `runs/2026-10-11/2026-10-11T1307Z-audit.md` against disk. Every cited page was fetched this pass (cached bodies reused only where the cache's first line named the URL). The run-clock FAIL and the `entry-run-binding` WARN on this fire's own Citrix record (dated 2026-10-19) are the expected post-loop re-stamp items and are not findings.

### Citation does not support the claim (F3)
- **#1 SEPPmail** (low confidence): "while the CVE record lists versions before 15.0.4 as affected" closes on an InfoGuard citation (and again in the 05-20 Contradiction line); InfoGuard carries only the table row `15.0.3 | CVE-2026-44126`. True per the CNA record (`cveawg.mitre.org/api/cve/CVE-2026-44126`: lessThan 15.0.4), but no cited page carries it.
- **#2 Ghost** (low confidence): record summary says "BleepingComputer and XLab date the fix's release to 19 February"; XLab says "publicly disclosed as early as February 19" (disclosure, not fix release).

### Unsupported / hallucinated facts (F4)
- **#3 Unbound** (low confidence): the iteration-3 inference ("not exposure to attacker-initiated connections", "most validating recursive resolvers meet by design") was removed from the action only; it remains in the takeaway and the main analysis. NLnet: "controlling a malicious zone and querying a vulnerable Unbound".
- **#4 Linux KEV** (low confidence): the report row says CVE-2025-39682's missing lower bound (first affected 6.0 per the kernel CNA record) was corrected; the entry's `affected` still has none.
- **#5 Audit report / CHANGELOG / run-record notes**: "118 existing entries carry a record from this fire" (report lines 46 and 421, CHANGELOG 4.20 with 14 improvements and 28 internal, run-record notes). Disk: 117 existing (102 corrections, 13 improvements, 2 updates, 27 internal); the run record's own `entries_updated` is 117. The Publica entry (2026-10-09) carried a record at iteration 2 and no longer does.
- **#6 Audit report line 432**: "`state/source_health.json`: this fire's sweep" is listed as shipped, but the file is not in the diff and its history holds no 238-source run from this fire (newest 12 runs start 2026-10-12). The sweep lives only in `work/.../source-health.txt` (238 probed, 237 relevant).
- **#7 Audit report / run record** (low confidence): "eight feed recipes and five notes"; the eset record's `fetch_method` and `rss_url` are unchanged (note appended only), so seven recipes and six notes.

### Editorial / less-is-more flags (advisory, F11)
- **#8 Exchange Pwn2Own**: record summary ends "the rating follows the B-rated contest reporting" (Admiralty letter in a reader-facing field); title still "three undisclosed"; `cves[]` empty although the takeaway acts on CVE-2026-62911.
- **#9 WinRAR**: em dashes in title, summary and first paragraph; "registry campaign" in the record summary.
- **#10 ShinyHunters PeopleSoft**: "the entry's own advice", "see the FBI PeopleSoft entry", "see the § 0 callout"; evidence[1] duplicates evidence[0].
- **#11 Unbound**: "a third high-rated flaw" (oss-security: one critical, two high).

### Iteration-3 deltas, one by one
| Delta | Result |
|---|---|
| xrdp F4 backport | Holds: Securelist "backported the patch to versions 0.9.27 and 0.10.4.1"; Exposure cites it. |
| PAN-OS 0300 F11 (12.1.7 ETA) | Holds: main analysis notes the table still marks 12.1.7 "(ETA: 05/28)"; PSIRT shows it. |
| ShinyHunters F4 Rapid7 quote | Holds: sentence is verbatim on the Rapid7 page; all six evidence quotes re-checked (Mandiant 09-25, BleepingComputer 09-26 verbatim). |
| ShinyHunters F4 exfiltration / T1048 | Holds: Mandiant records zstd archives and an outbound SSH connection to the leak-site mirror; techniques carry T1048, not T1567. |
| ShinyHunters F3 TechCrunch, SecurityWeek, Council of Europe | Hold: TechCrunch described as a member's account; patch cited to Rapid7 and Oracle's alert; The Register carries the PeopleSoft link ("ShinyHunters claims"). SecurityWeek's "mitigations only" is no longer cited. |
| Canvas / DAEMON / WaterPlum / SEPPmail / Cisco 20262 uncited sources F11 declined | Rationale holds. |
| Ghost F9 | Applied, but the new wording over-attributes to XLab (finding #2). Ghost advisory 2026-02-16 confirmed (GHSA datetime 2026-02-16T18:04:35Z). |
| Ghost F11 T1491.002 | Holds: dropped. |
| Exchange F4 (CVE-2026-62911) | Holds: Franky's Web ties it to the chain and dates exploit code 2026-08-27; ZDI-26-534/535/538 (2026-08-11) all link MSRC CVE-2026-62911; "tracked in a separate entry" is gone. F17 B2 applied. |
| Unbound F4 | Partially applied (finding #3). F10 PoC declined: holds (the only GitHub repo for the CVE id is a distribution patch tracker; searches for CVE-2026-82717 and "poc" return nothing). F8 Exposure line present. |
| Storm-3168 F4 | Holds: `sectors: []`. F11 T1190 declined: holds. |
| SEPPmail F3 / F4 / F11 | Detection now puts the traversal in the JSON body (matches InfoGuard's request); both fixed-version readings are stated (finding #1 on the uncited clause); 10.0 attributed to The Hacker News (page carries it). |
| Audit report 923/234 | Holds: page-checks.txt "fetching 923 ... literal-quote", "fetching 234 ... CVE-citation". As-published means (threat 10.6, incident 2.8, vulnerability 4.5, research 2.7) recomputed at 430fbdf; post-record threat 10.9 and incident 3.0 follow from this fire's four techniques records. |
| WinRAR F11 | Rating code and field name dropped from the record summary; em dashes remain (#9). |

### Audit report and run record against disk (verified true)
Window 2026-09-30T06:39:43Z to 2026-10-11T13:07:20Z, 270.5 h; 17 sub-agents all Sonnet 5.5; 196 = 133 + 20 + 43; 27 `merged_from` ids into 21 survivors with the fold table (4 PAN-OS 0300, 2 Exchange, 2 Cisco 20182, four singles, 13 in 12 groups, 0257, 50751) and all 27 files deleted; one new entry (NeedyMantis: notable, B2, single-source; registry `malware:needymantis` and `actor:storm-3069` sourced to it, DAEMON incident `attributed-to` Storm-3069); registry +20 product records, 11 `first_seen` moves, four summaries; `cves_seen` CVE-2026-55008 plus five titles; the 23 priority moves match the report's lists exactly; calibration table recomputed at 430fbdf (997: 30/408/540/19; Aug 196; Sep 128; trailing 30 days 113; Oct 34); October discipline figures; legacy queue 468 to 408 pending, 69 reviewed; warning acknowledgment (24 now, duration 363056 s = 100.8 h); KEV 10 additions all COVERED; page checks 1,024 quotes / 923 pages, 384 CVEs / 234 pages, re-run 314 entries with 421 and 68 and one Bitget WARN; prompt banners v4.20 and `LAST_AUDIT` loop; `check_run.py` description-meta change; `fetch_source.py` image-stream skip and `test_uncompressed_image_stream_is_not_content` (14/14 pass); GitLab 19.0.9 / 18.11.12 and Citrix CVE-2026-88773 `poc-public` update records; Sonnet 5 vs 5.5 baseline arithmetic (7.25 vs 5.6 iterations, median 2.50 h vs 2.79 h); the 14 error rows exist as records of the stated types (Linux and OpenAI internal). ATT&CK pin: v19.2 was current at fire time (v20.0 was published 2026-10-13, after the fire).

### Considered, no finding
`sectors[]` tags without a source naming the sector on PAN-OS 0257 (public-sector), Cisco 20262 (telco, public-sector) and SimpleHelp (public-sector): the report declines this class (line 106). Missed angles: none evidenced; the KEV diff, re-sweep ledgers and NeedyMantis recovery are consistent with disk.

### Verdict
NEEDS_FIXES (truth: 7, editorial: 0, advisory: 4)

Findings: `verification.iter4.s4.findings.yaml`; claim verdicts: `verification.iter4.s4.claims.yaml`.
