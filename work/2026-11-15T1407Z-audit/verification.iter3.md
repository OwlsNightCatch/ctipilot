**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-15T16:27:08Z · ended_at=2026-11-15T16:50:50Z · duration_seconds=1422

## Verification report — 2026-11-15T1407Z-audit (iteration 3)

Scope: 106 claim rows (the changed claims, every other claim of Publica, AhsayCBS, Fortinet, Linux TCP, Brotli, Chrome and Apache httpd, and a random quarter of the rest), all 106 answered in `verification.iter3.claims.yaml` (103 ok; 3 non-ok rows, all low confidence: two F3 on the AhsayCBS reboot wording, one F14 on the Brotli version binding). Beyond the ledger I read the whole new Artex entry, the diff of every one of the 27 updated entries against base, the registry diff, the run record and the audit report, and re-ran `check_run.py` (57 pass, 0 warn, 0 fail).

### Prior-iteration deltas (all 11 applied fixes verified on disk and against the source)

| Iteration-2 finding | Result |
|---|---|
| Apache: forky and sid fixed | Debian tracker now lists "forky, sid | 2.4.71-1 | fixed"; action, `cves[].fixed`, 2026-11-15 section and record summary say so. Correct. (A stale present-tense sentence remains in the main analysis: advisory F11 below.) |
| Chrome: Exposure citations, Brave/Vivaldi | Google pages cited for Chrome builds; browser list is Opera, which CISA's KEV text names ("Google Chrome, Microsoft Edge, and Opera"). Correct. |
| Brotli: Nexus rows not tied to one CVE | Affected, fixed and the section say so; Cisco's table has no per-CVE column and four Node.js CVEs. Correct. |
| Publica: BPK page after the notice clause | BPK notice page carries the 9 October notice (Strafanzeige, Bundesanwaltschaft, "keine Hinweise"). Correct. The old PDF returns HTTP 404. |
| Apache: SUSE added to the 9.8 citation | SUSE CVE page shows SUSE 9.8 (AC:L) and CNA (CISA-ADP) 8.1 (AC:H); Red Hat page shows 9.8 and 8.1. Correct. |
| Audit report sizes | AhsayCBS analysis 589 words (gate function), headline 100 characters, eMudhra 878, Publica 1,100. Correct. |
| Ahsay: latest hotfixes | Ahsay announcements listing dates the advisory 27 October (v9.15.2.78, v10.3.4.55), v10.3.6.1 on 3 November, v9.17.0 on 12 November; v9.17.0 and v10.3.6 release notes list the CVE patchset and the two defaults. Correct. |
| Fortinet Exposure | FG-IR-26-244 table (7.6 to 7.6.7, 7.4 to 7.4.11, 7.2 to 7.2.12, 7.0 all, 8.0.0 to 8.0.1) and FG-IR-26-219 (8.0.0 to 8.0.2) match. Correct. |
| Linux TCP: duplicate interim mitigation | actions[0] no longer carries it; actions[2] holds it (CIQ and AWS pages describe the IP-options drop and the legitimate-traffic warning). Correct. |
| Chrome headline | "update Chrome to 157.0.8103.50 and Edge to 157.0.4341.46 or later": Google and Microsoft's Edge notes agree. Correct. |
| Brotli summary date range | Ends 2026-11-13. Correct. |

The declined SSHole/eMudhra record-type advisory, the Check Point KEV-feed removal and the rolling-page date labels were not re-raised.

### Citation does not support the claim

F3 #1 (low confidence) — `2026-10-10/ahsaycbs-cve-2026-105133-105134-exploited-webshells-xmrig`, actions[0] and Defender takeaway: "install v9.17.0 or v10.3.6 ... or the latest partner hotfix ... and reboot it". The only reboot statement in the cited Ahsay pages is the 2026-10-12 hotfix advisory ("After applying the hotfix, please reboot your server."); the v9.17.0 and v10.3.6 release notes and the 2026-10-27 advisory say nothing about a reboot, so the reboot is not carried for the standard releases the clause leads with. Fix: scope the reboot to the hotfixes or drop it for the standard releases.

### Quantifier without source

F14 #2 (low confidence) — `2026-11-07/cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo`, summary: "... RoomOS and, since version 1.13, Nexus 3000 and 9000 switches running Guest Shell". Cisco's revision table says 1.13 "Updated products under investigation, vulnerable products, and products confirmed not vulnerable"; no page text says which revision added the Nexus rows (the base entry read 1.12 and never named Nexus). Fix: drop the version binding unless an earlier revision is shown not to carry the rows.

### Unsupported / hallucinated facts

F4 #3 — `docs/audits/2026-11-15-quality-audit.md`, systemic finding 7: "`actions[]` on new entries: 12 empty, 24 with one action, 2 with two." On disk the 38 new window entries carry 11 empty, 25 with one action, 2 with two: the Dixell entry gained its action in this fire (base `actions: []`). Fix: state 11, 25, 2.

### Editorial / less-is-more flags (advisory)

F11 #4 — `2026-11-12/cve-2026-119618-apache-httpd-mod-http2-assign-headers-rce`, main analysis: "... as fixed while forky is still vulnerable ([Debian Security Tracker, 2026-11-13])". Superseded by the 2026-11-15 section and the tracker (forky, sid fixed in 2.4.71-1); dated reading, so not false, but the main paragraph is the first thing a reader meets. (low confidence)

F11 #5 — `2026-10-10/ahsaycbs-...`, `sourcing_note`: "The patch position comes from Ahsay's own announcement, dated 2026-10-12 ..." now omits the release notes and the 2026-10-27 advisory that carry the standard-release and latest-hotfix statements.

F11 #6 — `2026-11-11/ghostframe-...` (Correction: "/opt/vmhostd-core ... the indicator it lists") and `2026-11-11/copperdragon-...` (Triage and Correction: "vmtoolsd.exe", "csrss.exe"): file-name indicators under the style rule; they are behavioural discriminators the sources give and the GhostFrame path pre-dates this fire, so this may stay. (low confidence)

### Checked and clean (no finding)

- New entry `2026-11-15/artex-aws-cloudwatch-log-secret-hunting-cognito-self-signup`: every sentence matches the Datadog post (anonymous S3 reads, FilterLogEvents with limit 1000, 2026-10-20 widened search, Cognito PreSignUp, CognitoIdentityCredentials session, failed discovery calls, hundreds of consoles, .gov blocklist, "playbook left to downstream AI inference") and the Wiz post (the `zzz-nonexistent` baseline request, dated 2026-10-22); the four `references[]` entries exist; `tool:artex` is a registered key; single-source flag and `sourcing_note` present; classification B/2 and `notable` are consistent; no em dash, no IOC, zero actions.
- Dixell (priority to `high`, exploitation, 14 CVEs, `fixed` ranges): the VulnCheck blog and CNA advisory confirm the 22:00 UTC and 03:41 UTC observations, four `id` probes, opportunistic scanners, the 2021-rewrite statement, 4.3.0 through 5.8.8, CVSS 8.8, and the blog-versus-CNA disagreement the section surfaces; the Dixell France guide points to Copeland's System Software Update page.
- Chrome/Edge: Edge release notes rows (157.0.4341.46 on November 9, Android 157.0.4341.53 on November 11, newer 157.0.4341.57 on November 13 without CVEs); MSRC record revision 1.1 and CISA ADP 8.8; Google Stable and Extended Stable builds and the Extended Stable second-bug note.
- Fortinet: FG-IR-26-244, -267, -273, -268 (virtual patch 26.118, updated 2026-11-13, Impact Denial of service), -219, -202, -194, -271 and the blog's availability column; NCSC.ch post 13092 "UNKNOWN".
- Linux TCP: Sophos v5, Ubuntu tracker (updated 14 November; HWE, Azure, NVIDIA, Raspberry Pi and the in-progress variants), Veeam KB4966 (last modified 2026-11-13), Debian 6.12.117-1, RHSA kernel builds, FMWP 26.113.
- Brotli: Cisco v1.13 Nexus rows and build list, Apple tvOS 27.2.1 (released November 13).
- SSHole (NCSC.ch update 10.11.2026 09:59 "Actively Exploited, PoC Available"; QNAP QSA-26-21; Previdian "First observed Nov 06"), Publica (BPK page, AWP, Inside IT, Publica, NZZ), Certighost (Microsoft Defender blog, CybersecurityNews, Kaspersky), SAP Patch Day table, Adobe APSB26-191 (12.12 and earlier, 12.12.a), N-able release notes, MC1506733, GhostFrame, Qubole, eMudhra (Microsoft 2026-11-12 table, Mozilla bug), LLMjacking (Obsidian), CopperDragon, Cursor, Check Point (sk1000302, Check Point Research), Danfoss and ANSSI removals (removed URLs cited nowhere).
- Run record: 27 updated ids, record counts (6 update, 10 correction, 11 improvement, 12 internal), 56-entry verdict arithmetic (27, 24, 5), 1,646 ledger claims, six registry product records plus two `ambiguous_labels`, `sources.json` changes, SonicWall entry reverted (no diff vs base). Audit report: Fortinet, SSHole, Chrome, Apache, Dixell, Publica, AhsayCBS rows, KEV window (12 additions, 4 not covered), `cves_seen` (16 bumps plus CVE-2026-124014), fire dates and gate logs (7 of 7), technique density (11.6, 2.8), Unit 42 caption, word counts.

Coverage: no relevant omission found in the entries read; the re-sweep dispositions in the audit report are consistent with the KEV window file.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 3)

All three truth findings are small and two are low confidence; they are quick fixes (an audit-report count, a version binding, a reboot scope). Every other claim in scope and every iteration-2 remediation held.
