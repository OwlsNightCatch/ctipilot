**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-21T10:50:46Z · ended_at=2026-10-21T11:26:41Z · duration_seconds=2155

## Verification report — 2026-10-21T0800Z-audit (iteration 4)

Scope walked: all 223 claims of `claims.iter4.scope.yaml` (the 13 changed since iteration 3, every claim of the 7 remediated entries, the seeded quarter of the rest), each decided against its cited page fetched in this pass (cached bodies, raw HTML where the extract was truncated, EUVD API, ncsc-csh, cisa-kev, one WebFetch for the Pixel bulletin, the 2026-08-18 MSRC capture kept under `work/2026-08-18T0410Z-intel/raw/` for the ShieldBreak "working to provide" statement). 223 rows written to `verification.iter4.claims.yaml`, all `ok`. Plus the run record, `docs/audits/2026-10-21-cleanup-wave-02.md` and `docs/cleanup/STATUS.md` against disk.

### Prior-iteration deltas (iteration 3, eight findings)

1. ShinyHunters/PeopleSoft F3 (account names): confirmed fixed. BleepingComputer carries "common PeopleSoft and Oracle administrative accounts such as 'psoft', 'oracle', and 'linuxadm'"; GTIG stays on the script behaviour (`/etc/hosts` spraying, marker file into the WebLogic and Process Scheduler directories).
2. Kemp F3 (THN beside the 9.6 clause): confirmed fixed. The 9.6 clause now cites ENISA EUVD and eSentire only (EUVD: baseScore 9.6, assigner ProgressSoftware; eSentire: "CVSS: 9.6"); ZDI's raw HTML carries 9.8.
3. OpenAI/Medicare F9: **partly fixed, finding F9 below.** The new section no longer asserts the unsupported negative, but the 2026-09-26 section still says Albanese cited the "internal file names" while CNN and ABC attribute that description to OpenAI.
4. ShieldBreak F9 (ranking): confirmed fixed. The 2026-08-21 takeaway points to the 2026-08-24 update where LevelBlue puts the creation of phoneinfo.dll first (LevelBlue Signal 1, "strongest unconditional detection point"); the record summary says so.
5. Sophos F11 ("by inference from Malwarebytes' sandbox and dropper-script analysis"): confirmed. Sandbox section: WScript.exe dropping NOVUpdate.exe and avk.dll; static analysis of the dropper script: three files, hidden window (window style 0).
6. SAP August F11 (Secure Transformer): confirmed fixed to Onapsis's wording ("Only XSL files from these hosts can be consumed by the vulnerable servlet"); "the patch does not remove the vulnerable servlet" is a fair reading of Onapsis's contrast with Note 3758900 ("The patch removes the vulnerable servlet component"), left as is.
7. Conference phishing F11 (Jon Semon): confirmed. The recap names Huntress SOC Analysts Ryan Dowd and Jon Semon, "While they weren't the ones to receive the DMs"; Jon "deemed the second payload the most interesting" and named wallets and antivirus update signals; record summary matches the summary field.
8. Run record durations: confirmed. Iteration 2 09:21:17 to 10:05:16 = 2639 s, iteration 3 10:08:28 to 10:47:06 = 2318 s, iteration 1 2180 s; `budget.tsv` and the `verify.iter<N>.started_at` files agree (verify-4 spawned 10:50:47, stamp 10:50:46).

### Claims missing / unsupported (truth)

#### F4 — report and tracker point at an input file that is not on disk
`docs/audits/2026-10-21-cleanup-wave-02.md` line 157, `docs/cleanup/STATUS.md` (W1-I row and the Waves table "inputs in work/cleanup/wave-03/") and `work/cleanup/plan.json` (W1-I `item`) name `work/cleanup/wave-03/findings-W1-I.md`. `work/cleanup/wave-03/` holds only `findings-W1-D-and-groups.yaml`. The file (45 bullets, matching the "45 residuals") is at `work/cleanup/wave-06/findings-W1-I.md`, in an untracked directory; both directories carry mtime 11:08:46, i.e. the file was moved or relocated during the loop, after iteration 3 read the tracker. Fix: move it back, or repoint the three references and re-render the tracker.

### Surface contradiction

#### F9 — Medicare entry: who said "internal file names"
The Record (https://therecord.media/openai-australia-breach-cyber): "The 'internal file names' he mentioned were potentially published in full by the same JavaScript file" (he = Albanese). CNN: "OpenAI said they found no evidence patient records were accessed in the Medicare breach and that the information included 'aggregate health statistics and internal file names.'"; ABC carries the same OpenAI statement. The entry's 2026-09-26 section: "the 'internal file names' Prime Minister Albanese cited as evidence of unauthorized access were potentially exposed by the same JavaScript file"; the main analysis quotes OpenAI's review (ABC); the 2026-10-21 section: "CNN attributes the description of the accessed information as aggregate health statistics and internal file names to OpenAI". Both attributions stand with no Contradiction line. Add one clause ("The Record attributes the phrase to Albanese, CNN and ABC to OpenAI") or reword the 09-26 clause to follow ABC and CNN.

### Editorial / less-is-more flags (advisory)

#### F11 — Kemp entry, three adjacency gaps (pre-existing, low confidence)
(a) "reaching code execution as root" ends under the watchTowr citation; the watchTowr page has no "root" (ZDI: "execute code in the context of root"; THN: "The command runs as root"). (b) 2026-07-02 section "(CVSS 9.6–9.8)" under eSentire, whose page gives only "CVSS: 9.6". (c) 2026-09-30 section "the 9.8 score is ZDI's" ends under the EUVD cite, which names no ZDI; and the main text's "GA ... / LTSF ..." labels under EUVD are not in the record (bare ranges V7.2.60.0 <V7.2.63.2 and V7.2.54.12 <V7.2.54.18). All true and supported elsewhere in the entry.

#### F11 — ShieldBreak entry: compressed quotation, file-name indicators (pre-existing, low confidence)
(a) 2026-08-24 section: `"not expected on supported versions" is what it will bear`; LevelBlue reads "The file is not expected to exist natively on supported Windows versions", so the quoted string is not a substring (meaning preserved). (b) phoneinfo.dll in System32 (named in the 2026-08-21 takeaway this fire added, the 2026-08-24 section and the 2026-10-21 correction quote) and `WD_SCAN` with the full symlink target are file-name indicators the style rule excludes; "a DLL not shipped with Windows appearing in System32" carries the same detection.

#### F11 — NCSC-CH RoguePlanet entry: citation date (pre-existing, low confidence)
"NCSC-CH later recorded that a proof of concept dubbed ShieldBreak allegedly bypasses this fix ... (NCSC-CH, 2026-07-09)". Post 12622's history: created 2026-06-10, CVE-2026-50656 edit 2026-07-09, "Added CVE-2026-62832 and 'ShieldBreak', alleged bypass of CVE-2026-50656 fix" 2026-08-12, "Added ref to CVE-2026-69414" 2026-08-17. The 07-09 label fits the CVE assignment, not the ShieldBreak clause.

#### F16 — Check Point IKEv1 priority (pre-existing, carried, already W1-I)
`priority: critical` on a flaw exploited since 2026-05-07 and disclosed 2026-06-08, 4.5 months old with a hotfix; carried from iteration 1 to wave 03, listed so it is not lost.

### Run record, report, tracker against disk (all hold except F4)

- Record: 72 entries with one record from this run id; 61 improvements (18 internal), 11 corrections (1 internal), no update (counted from the entry files); `updated_entry_ids` equals that set. Per-worker results match the batch files (batch 1: 10 records, 3 corrections, 7 improvements, 4 internal; batch 2: 10, 4/6/0; batch 3: 14 improvements, 5 internal; batch 4: 14, 2/12, 4; batch 5: 10 improvements, 2 internal; batch 6: 14, 2/12, 4); 13 entries without a record. Budget 2,232,689 repair tokens (record: about 2.23 M); duration 10178 s = completed minus started.
- `state/legacy_review.json`: pending 406 to 388, 18 entries moved under this run id. `state/cves_seen.json`: CVE-2026-92438 added, 33 `last_seen` moves, four title changes (CVE-2026-33691, CVE-2026-44772, CVE-2026-58704, CVE-2026-73570). `entities/registry.yaml`: four product records added, BerriAI LiteLLM `first_seen` moved to 2026-06-09, FTAPI incident summary reworded.
- Report: the 72-row Records table matches the disk record type, internal flag, fields and batch on every row; W1-B 50 with a record plus 7 without = 57; W1-C 5; W1-F 8; W1-E 19 of 26 with a record, 7 without; commits `731706f`, `1f8d69e`, `ea6e509` exist in the branch history; the Nx CVE-2026-8398 9.3 (CVSS 4.0) matches EUVD-2026-30514.
- Tracker: entries 1002 (`ls entries/*/*.md | wc -l`), legacy pending 388, never-verified 71, rows 29 done / 2 declined / 18 open of 49 (parsed from the table), out-of-week verdicts 61 / 6 / 37, `check_run.py --all` "26 pass · 0 warn · 0 fail · 26 acknowledged" (run in this pass, exit 0).
- Verification line, Budget/Verification notes and the wave-02 status cell are in-progress text, expected.

I ran `python3 work/cleanup/inventory.py` to compare the tracker totals; it rewrites `work/cleanup/inventory.json` deterministically from the working tree (diffstat unchanged at 350 lines, no content change).

### Coverage

No missed angle for an audit of this scope (no coverage re-sweep ran, no new entries). The one run-scoped gate WARN (Pixel CVE-2026-58704) is a transport gap: WebFetch of the bulletin returns "**Note**: There are indications that CVE-2026-58704 may be under limited, targeted exploitation." verbatim, Modem, EoP, High, patch level 2026-09-05, "Last updated 2026-09-30".

### Verdict

NEEDS_FIXES (truth: 1, editorial: 1, advisory: 4)

### Findings summary (machine-readable)

See `work/2026-10-21T0800Z-audit/verification.iter4.findings.yaml`.
