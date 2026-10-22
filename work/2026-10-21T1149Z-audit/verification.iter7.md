**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-22T09:04:28Z · ended_at=2026-10-22T09:30:29Z · duration_seconds=1561

## Verification report — 2026-10-21T1149Z-audit (iteration 7)

Role: confirmation pass after iteration 6's CLEAN, read cold. Scope: all 278 claims of `claims.iter7.yaml` (every claim, no sampling), the 23 updated entries read whole with `git diff HEAD`, the fold twin at `git show HEAD:`, the run record, the wave report, `work/cleanup/plan.json`, `docs/cleanup/STATUS.md`, `state/cves_seen.json`, `state/legacy_review.json` and `entities/registry.yaml`. Claim verdicts: 274 ok, 2 unreadable (CCB Belgium), 1 F3, 1 F14; rows in `verification.iter7.claims.yaml`. Fetches: 66 cited URLs via `extract`/bridge (plus MSRC SUG and CVRF API, NVD API, EUVD API, CISA KEV, Adobe raw pages, Proofpoint, n8n advisories, June Exchange blog); one `WebFetch` (CCB, 403). Check_run on the run id: 58 pass, 0 warn, 1 fail (the expected `verification-confirmation`).

Disk checks that hold: 23 records (2 update, 6 correction, 15 improvement; internal: n8n correction, Adobe improvement); `updated_at` equals `at` on YellowKey (2026-10-21T15:38:35Z) and Nightmare Eclipse (15:40:42Z) and moved on no other entry; W1-D = 33 entries, 21 with a record (14 improvements, 5 corrections, 2 updates), 12 without, 366 listed defects, 30 of 33 carried a 2026-10-11 record; plus Adobe and the Pwn2Own roundup (W4-05, W4-04) = 23; cves_seen: `last_seen` moved on exactly CVE-2026-35616, 42321, 43284, 43500, 45585, 45586, 48558 and four titles (35616, 45586, 46817, 48558); legacy_review: four entries `reviewed`, 402 pending; registry: two summaries changed, five product records added (chroma, lm-studio, nvidia-container-toolkit, nvidia-megatron-bridge, red-hat-enterprise-linux-for-workstations), eight `first_seen` moved (Cursor, LiteLLM, Defender Antivirus, Edge, SharePoint, Windows Server, OpenAI Codex, ESXi), no relation with a missing source entry, no remaining reference to the folded twin id except the survivor's `merged_from` and the legacy queue; plan.json/STATUS.md rows (29 done / 2 declined / 7 in a wave / 20 open of 58), new rows W4-10 and W4-11, W7-16 (581 entries without `updates:` at HEAD), W7-17, the W2-04 lead (CVE-2026-50507 is a BitLocker bypass in MSRC); the twin scan (104 + 16 candidates, 2 overlapping = 118); run-record sub-agent and iteration durations all equal their stamps; claim commit 7e741582 landed after wave 05's c2366f87.

Source facts re-read this iteration and found right (selection): MSRC SUG/CVRF for CVE-2026-45585 (revisions 1.2 to 2.1, 6.8, AV:P, fixed builds, exploited No), CVE-2026-45586 (7.8, builds, link following), CVE-2026-62911 (affectedProduct fixed builds, credit), CVE-2020-17103 (re-release v2); CISA KEV rows for CVE-2026-20262 (CWE-22, 2026-06-15), 46817 (forensicTriage Yes), 20245, 31431, 35616, 42208, 42897; EUVD-2026-30010 (dateUpdated 2026-09-10); FIRST EPSS for 2026-09-04 and 2026-10-20; Oracle CSPU revision table (2026-May-28); Fortinet PSIRT (CVSSv3 9.8, temporal 9.1); NVD record for CVE-2026-48558 (CVSS 3.1 10.0); Adobe APSB26-120 (affected 9398 and earlier) and APSB26-114 (fixed 9398); ZDI day pages and announcement (JSON-LD dates 2026-05-14, 05-15, 05-16, 03-12); all five n8n advisories (authenticated workflow editor, no JavaScript execution); ATT&CK pin v20 ids for every changed `techniques[]`.

### Claim not supported (F3)

**#1 (low confidence).** `2026-05-17/pwn2own-berlin-2026-master-of-pwn-outcomes-the-new-ai-agents`, Defender takeaway: "no source reports these bugs used in the wild, and fixes arrive through vendor advisories within the 90-day window ([BleepingComputer, 2026-05-15])". The page says only "Vendors have 90 days to patch their software and hardware after the zero-days are disclosed at Pwn2Own." It does not say fixes will arrive in the window or through vendor advisories, and the 2026-10-21 section of the same entry says the pages "carry no patch forecast". Reword to the policy or drop the clause.

### Quantifier without source (F14)

**#2 (low confidence).** Same entry, first paragraph: "For 2026 ZDI split its AI category into AI Databases, Coding Agents (new), Local Inferences and NVIDIA ([Zero Day Initiative, 2026-03-12])". The announcement says "Last year, we added Artificial Intelligence as a category with great results. This year, we're expanding this and splitting it into multiple different categories: AI Databases, Coding Agents, Local Inferences, and a separate category for NVIDIA products." Nothing in the page calls Coding Agents new. Drop "(new)".

### Unsupported / hallucinated facts (F4)

**#3 (low confidence).** `docs/audits/2026-10-21-cleanup-wave-03.md`, Adobe row: "links APSB26-114 (W4-05), and one pipeline phrase in the sourcing note is reworded". `git diff HEAD` on the Adobe entry shows three workflow phrases changed in `sourcing_note` ("what this entry follows" to "what the analysis follows"; "and in the run record" removed; "surfaced the bulletin into this window" to "relayed the bulletin"); the iteration 2 remediation names two. "One" understates the edit.

**#4 (low confidence).** `entities/registry.yaml`, `campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac` summary: "After Microsoft's MSRC called uncoordinated disclosure never justifiable on 2026-05-27, the persona threatened a further release for 14 July 2026." The Record (https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more) says "The researcher threatened a further release on July 14" without dating the threat; the MSRC blog and heise do not carry it. The "After" sequence is in no source (the legacy summary had the same order). Write "The persona has threatened a further release for 14 July 2026."

### Editorial / less-is-more flags (advisory)

**#5 (low confidence).** LiteLLM: title, headline and summary say "first exploitation attempt 36 hours after the advisory"; Sysdig anchors the 36 h 7 min to the advisory's listing in the global advisory database on 2026-04-24 and notes the maintainer advisory was published on 2026-04-20, the entry's primary source and `event_date`. The body says "reached the global database"; the front matter does not. Optional.

**#6 (pre-existing, low confidence).** FortiClient Detection: "a request rejected with "Certificate not found in request header"". Arctic Wolf lists that log line as an exploitation signal and says the crafted requests were processed as legitimate; "rejected" is in no source.

**#7 (low confidence).** nginx: citation label "[ENISA EUVD, 2026-09-10]" is the record's dateUpdated; datePublished is 2026-05-13. The text says "updated on 2026-09-10", so the label is disclosed (declined in iteration 2).

**#8 (low confidence).** SimpleHelp, claims b3d0654cb8 and 1b7635154c cite only CCB Belgium, which is unreadable live (extract, url and jina: 503 maintenance page; WebFetch: 403). The repair worker's saved copy of 2026-10-21 reads "CVE-2026-48558 CVSS 10 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)" and the NVD record (VulnCheck CNA) carries CVSS 3.1 10.0. Rows are `unreadable`; no error suspected.

**#9 (low confidence).** Pwn2Own roundup (raised in iteration 1, declined): no CVE, no exploitation, no action, a takeaway that says nothing changes, and a dollar payout for most results (vanity-metric class, check 7).

**#10 (pre-existing).** Adobe APSB26-120: seven em dashes in reader-facing title, headline, summary and body (declined in iteration 2).

**#11 (low confidence).** Exchange OWA record 2026-10-21T12:07:16Z lists `headline` in `fields` (157 to 116 characters per the wave report) but its summary does not mention the recut.

Carried, already acknowledged in the report: SimpleHelp `critical` and Dirty Frag `high` calibration (pre-existing).

Coverage: no missed angle named; the wave is an operator-directed partial audit and ran no coverage re-sweep.

### Verdict

NEEDS_FIXES (truth: 4, editorial: 0, advisory: 7)

### Findings summary (machine-readable)

Written unfenced to `work/2026-10-21T1149Z-audit/verification.iter7.findings.yaml` (11 records: F14, F3, F4, F4, then seven F11).
