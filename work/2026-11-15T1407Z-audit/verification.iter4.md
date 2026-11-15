**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-15T16:53:11Z · ended_at=2026-11-15T17:14:23Z · duration_seconds=1272

## Verification report — 2026-11-15T1407Z-audit (iteration 4)

Role: post-fix pass. Scope: 63 claims (`verify.iter4.scope.txt`: the 5 changed since iteration 3, every other claim of AhsayCBS and Brotli, and a random quarter of the rest). All 63 have a verdict row in `verification.iter4.claims.yaml` (62 ok, 1 F3). Beyond the ledger I read the new ARTEX entry whole, the diff of every updated entry, the run record and the audit report against disk, and re-ran `check_run.py` (57 pass, 0 warn, 0 fail).

### Prior-iteration deltas (iteration 3)

- **F3 AhsayCBS reboot binding: fix confirmed.** The action, takeaway and both `fixed` fields now tie the reboot to the partner hotfix. Ahsay's 2026-10-12 advisory says "After applying the hotfix, please reboot your server." (hotfixes 10.3.4.45 and 9.15.2.70); the v9.17.0 and v10.3.6 release notes carry no reboot instruction. The 2026-10-27 advisory (v9.15.2.78, v10.3.4.55) states no reboot either, so 'followed by a reboot' for those builds is an extension of the 10-12 instruction, cited in the same takeaway; acceptable.
- **F14 Brotli 'since version 1.13': fix confirmed.** The summary now reads 'at version 1.13 of 2026-11-13'. Cisco's revision table lists 1.13 as 2026-NOV-13 ("Updated products under investigation, vulnerable products, and products confirmed not vulnerable"); the Nexus rows and the Guestshell 4.9 / NX-OS builds match the table.
- **F4 audit report systemic finding 7: fix confirmed.** Recounted from disk over the 38 entries filed in the window: 11 empty, 25 one action, 2 two actions (Dixell has one). Companion figures also hold: 6 of 38 new `high`, 14 of 56 in-scope `high`. Run-record counts hold too: 27 records from this fire (6 update, 10 correction, 11 improvement; 12 internal), SonicWall entry diff vs base is empty, BPK PDF returns 404.
- **F11 AhsayCBS sourcing_note: fix confirmed** (names Ahsay's announcements and release notes; `sourcing_note` is in the record's `fields`).
- **Declined items (Apache dated section, GhostFrame/CopperDragon file names): not re-raised on the declined text.** One piece of new evidence on the Apache item is raised below (the main analysis, not the dated section).

### Citation does not support the claim

**#1 (F3, low confidence)** 2026-10-23/fortinet-hardening-release-fortios-fortimanager-fortimail, claim d366ad3ae1: "The advisories withheld until Patch Tuesday, published on 2026-11-10, state no exploitation, and NCSC.ch listed the status as unknown ([NCSC.ch, 2026-10-22](https://security-hub.ncsc.admin.ch/#/posts/13092))". NCSC post 13092 (created 2026-10-22T12:10Z) says only "Current exploitation status: UNKNOWN" for the October release. The first clause is not on that page; the PSIRT pages carry it ("Known Exploited No" on FG-IR-26-268 and FG-IR-26-244). Cite a PSIRT page for that clause.

### Unsupported / hallucinated facts

**#2 (F4)** 2026-11-12/cve-2026-119618-apache-httpd-mod-http2-assign-headers-rce, main analysis: "...as fixed while forky is still vulnerable ([Debian Security Tracker, 2026-11-13](...))". The Debian tracker read now: "| forky, sid | 2.4.71-1 | fixed |". This fire's section, `cves[].fixed` and `actions[1]` say forky and sid are fixed. The paragraph is the undated main analysis (edited by this fire for SUSE), so it asserts a falsehood the newest section disproves (4c-h). The declined item was the dated 2026-11-13 section; this is a different location and is not covered by that rebuttal.

### Needs more research

**#3 (F8, low confidence)** 2026-11-07/cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo: Exposure and Defender takeaway omit the Cisco Nexus 3000/9000 Guest Shell rows (Guestshell 4.9 is a listed fix) and Apple tvOS 27.2.1 that the new section and `cves[]` carry (HomeView Software 27.2 is also absent from the takeaway).

**#4 (F8, low confidence)** 2026-10-10/ahsaycbs-cve-2026-105133-105134-exploited-webshells-xmrig: Ahsay's announcement listing shows "13 November: New Ahsay v10.3.6.14 Released"; its release notes (13-Nov-2026) list Security fixes including "Redirector logged CBS password in the access log in readable form". The entry names v10.3.6 and v10.3.6.1 only.

### Editorial / less-is-more flags (advisory)

**#5 (F11, low confidence)** AhsayCBS headline "...standard releases v9.17.0 and v10.3.6 now patch both flaws": the release notes list a "Security Patchset for CVE-2026-105133 and CVE-2026-105134"; no third party verified them. Body and summary hedge; the headline does not.

### Whole-run checks

- Coverage: the re-sweeps (G1 46/46, G2 44/44, G3 42/42 sources) plus the KEV window (12 additions since 2026-11-08, 8 in `cves_seen`, the 4 absent ones carry run-record borderline-drop lines) show no uncovered critical or high item. Coverage looks complete; no missed angle named.
- New entry (ARTEX in AWS): all 13 ledger claims and every prose sentence checked against the Datadog post and the Wiz post; no defect. Single-source flag, sourcing note, B2 rating, `notable`, empty actions and the four references are right.
- Record/section agreement: every non-internal record of the fire has its section; each record summary matches its section; no silent edits; `updated_at` matches only on the six `update` records.
- Style: no em dash outside section headings, no IOCs, no pipeline vocabulary in reader-facing text in any changed entry.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 2, advisory: 1)

### Findings summary (machine-readable)

See `work/2026-11-15T1407Z-audit/verification.iter4.findings.yaml`.
