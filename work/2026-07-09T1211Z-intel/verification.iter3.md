**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-09T13:20:47Z · ended_at=2026-07-09T13:26:52Z · duration_seconds=365

## Verification report — 2026-07-09T1211Z-intel (iteration 3, cold)

Read cold, no prior-iteration deltas (odd iteration). 7 new entries + run record reviewed end-to-end. Every inline source URL fetched (WebFetch, escalated to bridge/jina on 403/503/empty). All named CVEs, actors, versions, dates, numbers, and verbatim evidence quotes cross-checked against fetched sources. Frontmatter↔body agreement, priority calibration, update-vs-new decisions, single-source carve-outs, and Admiralty classification codes all checked.

### URL / source liveness ledger
- Balbooa mysites.guru primary — WebFetch OK; confirms CVE-2026-56291, zero-day exploited in wild, no allow-list, com_baforms, File::makeSafe, Hetzner, 2.4.0/2.4.1, CVSS 4.0 10.0, CWE-434, reporter Phil Taylor. Both evidence quotes supported.
- Balbooa changelog — WebFetch empty; jina recovered: 2.4.1 dated 09.07.2026, four "Fixed" bullets (server-side extension allow-list, MIME option "to improve upload security", server-generated filenames, CSRF). No CVE/RCE/exploitation flag. Confirms iter-1 F3 remediation ("mentions upload security but nowhere flags RCE/CVE") holds.
- Group-IB RedHook — WebFetch 503; jina recovered. Verbatim quote "This, however, is the first time we have seen it used by a malware to abuse privileges on a victim's device." confirmed. Cyble July 2025, Vietnam→Indonesia, Shizuku, uid 2000, 53 commands, AWS S3/GitHub, ADB Wireless Debugging all confirmed.
- Groupe 3R (swisscybersecurity + ictjournal) — both fetched OK. Akira attribution via victim's own forensics, darknet publication, ransom refused, 20 sites/7 cantons rebuilt, medical-data exfil uncertain, prior April-2025 attack by different attackers, ISO-27001 partners, physician portal in testing — all confirmed by both.
- PDAG (swisscybersecurity) — fetched OK. @pdag.ch phishing→spam relay, account lockout + all-staff reset, authorities notified, no patient data, no root cause disclosed — confirmed.
- Nozomi Apex2/c2c — fetched OK. Both verbatim quotes confirmed present. All botnet technical detail (Telnet/SSH, Golang builds, cf Cloudflare-bypass, cpufreqd fake systemd, sudo -n true, flood modules) confirmed.
- Deutsche Bank (Computing UK primary jina; Cybernews jina; Cybersecurity Insiders WebFetch) — all fetched. Both verbatim quotes confirmed. Unsafe RaaS/double-extortion, 2024-25 quiet then 2026 re-emergence, DE/US/CH/FR targets, third-party German marketing/incentive vendor, employee records — confirmed. Secondary TTP profiling correctly flagged unverified in the entry.
- KDDI (BleepingComputer primary + corroborator) — both fetched. Verbatim quote confirmed. 12,233,087 emails / 7,616,173 passwords, 16 May compromise, zero-day unrecognised by vendor as of 17 June, EDR deployed, 23 June audit, PPC/MIC notified, five ISPs — confirmed. Corroborator title "up to 14.2 million" confirms the down-revision.
- industrialcyber.co (Nozomi corroborator) — documented transport-403 across all rungs per run record; Nozomi is the primary and single-source basis, so not load-bearing.

### Cross-checks that could have been defects but hold
- Balbooa "all three [July Joomla file-upload RCE zero-days] surfaced by the same research outfit": verified TRUE via the pipeline's own 2026-07-08 entry, which cites mySites.guru as primary discloser for both CVE-2026-48908 (sp-page-builder blog) and CVE-2026-56290 (pagebuilderck blog); Balbooa (56291) is also mySites.guru. Not an analytical-link-as-fact defect.
- Update targets exist and carry genuine deltas: Groupe 3R (2026-05-10 target; delta = victim forensic Akira confirmation + darknet publication) and KDDI (2026-06-29 target; delta = root-cause zero-day + final counts). Both correct as update_of, not new.
- Single-source carve-outs: Groupe 3R and PDAG single-source-victim — both outlets in each carry the victim's own disclosure (confirmed by fetch); carve-out fits, credibility 2 correct. RedHook/Nozomi single-source (lab research, credibility 2) and KDDI single-source (aggregator, credibility 2) correctly flagged with sourcing_note.
- Admiralty classification codes match source reliability in sources.json: Group-IB=B, Nozomi=B, BleepingComputer=B, swisscybersecurity=C — entries carry B/B/B and C/C respectively. Deutsche Bank B (Computing/Cybernews untracked in sources.json; B defensible given Cybernews original sample analysis + multi-source victim statement — within tolerance, not a plain contradiction). Balbooa (triage kind vulnerability) correctly carries classification:null + org_triage:null (no scheme configured).
- Priority calibration: Balbooa high (actively-exploited pre-auth RCE but narrow extension-level exposure, no public PoC — not critical) sound; no false critical; no under-alerted notable. KDDI routine appropriate for out-of-nexus update.
- Breach-gate: Deutsche Bank clears on home-region actor (Unsafe targets DE/CH/FR) + finance sector + transferable third-party-exposure lesson, framed around the lesson not the victim. KDDI clears as update on tracked incident + transferable vendor-unknown-zero-day lesson.
- Style: no IOCs (paths/endpoints/loopback are detection knowledge, not attacker IOCs); no vanity metrics; English; no workflow-internal jargon on the banned list.
- Recency: Groupe 3R (2026-07-07) and Nozomi (2026-07-06) both within the 72h developing window; documented in run record.

### Coverage completeness
Run record documents dedup drops (Januscape, BeyondTrust, Sygnia, Swiss Post stat, UNC1151) and borderline drops (OneConsult, INTERPOL, ChocoPoC-stale) with defensible reasoning. cisa-advisories JS-listing gap acknowledged with KEV/CSAF exploitation ground-truth covered. No relevant in-window story identifiable as a silent omission. Coverage looks complete.

### Verdict
CLEAN — no truth or editorial defects. All source URLs resolve and support their claims; all verbatim quotes confirmed; frontmatter agrees with bodies; classifications, priorities, update decisions, and single-source carve-outs are all correct. The two prior-iteration remediations (iter-1 F3 changelog wording, iter-1 F13 Akira misattribution, iter-2 F12 single-source-victim relabels) all hold. The run publishes.

### Findings summary (machine-readable)
```yaml
[]
```
