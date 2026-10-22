**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-21T15:58:44Z · ended_at=2026-10-21T20:36:09Z · duration_seconds=16645

## Verification report — 2026-10-21T1149Z-audit (iteration 1)

Scope: first pass, full ledger (266 claims, every one with a verdict row in `verification.iter1.claims.yaml`: 259 ok, 3 F3, 1 F5, 3 unreadable), all 23 updated entries read whole with `git diff HEAD`, the folded twin read from `HEAD`, the run record and the wave report checked against disk. Every one of the 65 cited URLs was fetched this pass (CISA KEV through the bridge, MSRC through `msrc cve`/CVRF, NCSC-CH through `ncsc-csh`), plus the evidence-quote sources not in the ledger; all 53 `evidence[]` quotes that carry a source_url were substring-checked against fetched pages (50 exact; the other 3 are the MSRC acknowledgment, present in the CVRF, and two Japanese-original quotes whose `original:` text is verbatim on digital.go.jp). `entry_record.py diff` field sets equal each record's `fields` on all 23 entries; `updated_at` follows the record rule. Unreadable: CCB Belgium (403 on every rung); see F11 note. The ledger's claim id `8697872289` is an unquoted number and parses as an integer; the verdict file writes it as a string.

### Broken / unreachable URLs

- **F1 #1** — japan-digital-agency-gss-vpn-breach-maintenance-account, `https://www.nippon.com/en/news/yjj2026091100453/` (sources[0], role primary): 404 (curl 404; extract: "Error 404 - Not Found"). The 2026-10-21T12:08:54Z record says the article "is no longer online" and lists `sources` in its fields, but the dead URL stays as the first primary source, and `sourcing_note` still says the notice "is cited beside three outlets that relay it" and describes Jiji Press although the body cites only Piyolog and Rocket Boys. Drop the source, reword the note.

### Citation does not support the claim

- **F3 #2** (low confidence) — nginx entry, claim e78155117b, "Reliable impact is a crash of the NGINX worker process, which the master process restarts" cited to the depthfirst research post. That post says only that a failed exploit crashes a worker and "the master process simply spawns a new one"; "crash/restart" as the reliable impact is F5's wording (EUVD: "leading to a restart") and NCSC-CH's, neither cited on that sentence; depthfirst's landing page says "The outcome is remote code execution".
- **F3 #3** (low confidence) — YellowKey entry, claim 83e1ebf26e, Detection: "GreenPlasma shows in process telemetry as a shell running as SYSTEM that descends from a standard user's process tree, and the public partial PoC raises a UAC consent prompt" cited to The Register. The Register has only the UAC clause; the telemetry shape is inference, and BleepingComputer says the leaked PoC lacks the component for a full SYSTEM shell.
- **F3 #4** (low confidence) — YellowKey entry, claim 7a90e4cc2b, "the June 2026 Windows update closes both flaws; ... interim WinRE script need not be reverted" cited to MSRC CVE-2026-45585 only; that page covers YellowKey, the GreenPlasma fix is on CVE-2026-45586.

### Unsupported / hallucinated facts

- **F4 #5** — wave report, row "2026-05-15 YellowKey and GreenPlasma (legacy)": "priority high to routine". The entry's frontmatter is `priority: notable` and the run's record summary says "high to notable".
- **F4 #6** — wave report, Scope: "base `17506d0` (`work/2026-10-21T1149Z-audit/base.sha`)". The file holds `29364cd70b726de933d4ba030ba283eca05f4fe0`; `claims.iter1.yaml` repeats it. 17506d0 is an older commit.
- **F4 #7** (low confidence) — run record, `sub_agents.repair-4.duration_seconds: 830`; its own stamps (11:56:07Z to 12:09:56Z) give 829. All other durations match.

### Claims missing inline citation

- **F5 #8** (low confidence) — YellowKey entry, claim fc92c5fab7, section "Update — 2026-05-20": the sentence with the new direct quotation "consider implementing" has no inline citation (the MSRC link is on the next sentence); the content matches the MSRC FAQ, but "TPM-only" is the author's framing.

### Needs more research

- **F8 #9** — Dirty Frag entry: `git diff HEAD` shows the sentence "Copy Fail is a separate, earlier flaw, CVE-2026-31431 (Microsoft Security Blog ...)" deleted. The headline, summary, sourcing_note, body and 2026-10-11 section still name "Copy Fail" with no CVE id and `references: []`; the Copy Fail entry exists (2026-05-09/cve-2026-31431-...). Restore the identification or add the reference. The record summary does not declare the deletion.

### Surface contradiction

- **F9 #10** (low confidence) — YellowKey summary "TPM+PIN also blocks YellowKey" states Microsoft's side flat; the body's Contradiction line records the researcher's counterclaim.
- **F9 #11** (low confidence) — nginx: NCSC-CH #12575, cited three times, says "Achieving RCE additionally requires ... ASLR disabled"; the entry now says code execution is not limited to ASLR-disabled hosts (EUVD, depthfirst) and its Contradiction line covers severity only.
- **F9 #12** (low confidence) — DEVCORE entry: MSRC "allows an authorized attacker" (PR:L) versus Franky's Web (cited) "The attacker does not need valid credentials" and MB VRED's title "Pre-Auth RCE"; only Microsoft's wording is carried.
- **F9 #13** (low confidence) — DENIC headline "about three hours" (DENIC's final-report figure) against the entry's own timeline (19:57 or 19:30 to 23:15 UTC, 3 h 18 to 3 h 45) and the 2026-10-11 record's "about three and a half hours".

### Editorial / less-is-more flags (advisory)

- **F11 #14 (pre-existing)** — Adobe sourcing_note: "the run record", "into this window".
- **F11 #15 (pre-existing)** — Japan 2026-09-13 section and sourcing_note: "Admiralty rating", "credibility number is 2".
- **F11 #16** — records omit deletions: Dirty Frag (Copy Fail identification, headline recut), Cisco 20245 ("adds" checks; also removed the /etc/passwd UID-0 check, defensible per Mandiant but undeclared).
- **F11 #17** — Pwn2Own roundup is now a per-researcher payout ledger with takeaway "no change on the results alone" (vanity-metric class).
- **F11 #18** — FortiClient: file-name indicators `FortiEndpoint_Patch.exe` (pre-existing) and `C:\ProgramData\log.txt` (added this fire).
- **F11 #19** — CERT-FR and Exchange OWA improvement sections duplicate a sentence the same fire added to the main analysis.
- **F11 #20** — Nightmare Eclipse `cves[]` lists only CVE-2026-45585 while the body states fixes for CVE-2026-45586 and CVE-2020-17103.
- **F11 #21** (low confidence) — ZDI announcement cited as 2026-03-11; its dateline and JSON-LD say 2026-03-12.
- **F11 #22** (low confidence) — GLPI cves[CVE-2026-5385] keeps the release-notes range; the advisory disagreement is in prose only.
- **F11 #23** — verification gap, no defect asserted: CCB Belgium unreadable (claims b3d0654cb8, 1b7635154c, 67a2cb0628); the repair worker's saved copy and NVD (cross-check only) both show CVSS 3.1 10.0.

### Org-triage / priority

- **F16 #24 (pre-existing, low confidence)** — SimpleHelp `priority: critical` + `immediate_action`; this fire's section records the non-default setting and that servers without such a Group cannot be exploited; recalibrate.
- **F16 #25 (pre-existing, low confidence)** — Dirty Frag `priority: high` although the entry says exploitation is unconfirmed and the CVE-2026-43500 EPSS now reads 0.0262.

### Action-item discipline

- **F18 #26 (low confidence)** — Cisco 20245 actions[0]: the clause added this fire (verify edge-device configurations, check auth.log for su) restates Detection and the takeaway.
- **F18 #27 (pre-existing)** — nginx actions[0]: ~90 words restating the body, hedged "either ... or", now duplicating the new Defender takeaway.

### Checks with no finding

Update-vs-new decisions are right (the one fold, Ghost, is the same finding; the Adobe, YellowKey, Nightmare Eclipse and DEVCORE links are correctly `references[]`). Wave-report claims that hold on disk: 366 defects on the 33 W1-D entries, 30 of 33 with a 2026-10-11 record, 12 with no record, 21 records on W1-D entries, the 2/6/15 record split, 118 unique twin candidates (104 + 16 - 2 overlap), 581 entries without `updates:` at HEAD, the four legacy entries marked reviewed, the cves_seen `last_seen` and title changes, the registry summaries and five product records, 157 to 116 headline characters, the fold leaving no dangling reference. Tracker rows still read `in-wave` and STATUS.md lacks W4-10 because C5 step 5 runs after this loop; no finding. Missed angles: none; this wave published no new entries and its sources were the entries' own.

### Verdict

NEEDS_FIXES (truth: 7, editorial: 7, advisory: 13)

### Findings summary (machine-readable)

See `work/2026-10-21T1149Z-audit/verification.iter1.findings.yaml` (27 records).
