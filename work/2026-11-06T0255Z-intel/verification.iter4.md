**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-06T04:51:37Z · ended_at=2026-11-06T05:07:38Z · duration_seconds=961

## Verification report — 2026-11-06T0255Z-intel (iteration 4)

Scope: all 129 claims of claims.iter4.yaml walked in full (post-fix pass; nothing sampled). Rows in verification.iter4.claims.yaml: 129 rows, 129 ok, 0 non-ok. Sources re-read this iteration from the gate's saved bodies and live: Barracuda Trust Center (raw HTML for the patch table), Barracuda Campus, Mandiant MNDT-2026-0041 and -0042 (embedded rawLines), watchTowr post and README (repo createdAt 2026-11-03), NCSC posts 13144, 13155 and 13054, OpenSSH 10.6p2 notes, OX feed text, heise, GHSA page (raw HTML: Critical, CVSS:3.1 9.8, affected <= 1.11.2, patched >= 1.11.3, published Oct 28 2026), BSI CSAF, Securelist, Microsoft (two posts), Todyl, Seqrite, SRF, Keystone-SDA (two), CISA fact sheet (WebFetch, Publish Date November 05, 2026, no vendor or CVE named). CVE ids and scores checked against the MITRE CVE API: CVE-2026-116779 (9.8, < 1.11.3), CVE-2026-123158 (8.1, < 10.6p2), CVE-2026-116606 (9.3, < 9.4.0.030), CVE-2026-111560 (8.6). KEV 2026.11.04 carries none of the four.

Iteration-3 fixes checked against the live sources, all confirmed correct:
1. Entra summary: Todyl says "About 45 app registrations at roughly 18 organizations were targeted, and more than 33 of them authenticated successfully ... reached 27 organizations"; the summary now matches.
2. Run record, Audit leads: entries/2026-10-29/mdaemon-clamav-unrar-cve-2025-8088-exploited-in-ukraine.md lists the ESET report (welivesecurity post and PDF) as a source; "no dedicated entry (the 2026-10-29 MDaemon and ClamAV entry cites it for one finding)" is true.
3. Barracuda sourcing_note: the "no fetched page" phrase is gone; the replacement clause is slightly imprecise (advisory item #3 below).
4. Storm-2603 title and headline: Securelist Attribution section ends "this allows us to attribute this case to Storm-2603 with moderate confidence"; "attributed ... with moderate confidence" and "Storm-2603-linked" are faithful.

Updated-entry contract (4c): Barracuda record 2026-11-06T03:41:00Z (type update; fields title/headline/summary/priority/tags/cves/sources/evidence/sourcing_note/actions/body) covers every changed line of git diff HEAD, updated_at equals the record's at, discovered_at/run_id/path untouched, the section is the same finding with a genuine delta (watchTowr chain, README, Barracuda's own 2026-11-05 field change), the main analysis no longer contradicts it. Danfoss record 2026-11-06T03:44:30Z (fields title/headline/summary/sources/evidence/sourcing_note/body) covers the diff including the dropped Sabcobel/CyberInsider sentence of the main analysis and the "as of 2026-10-14" qualifier; the section is the same finding and every SRF, Keystone-SDA, BACS and CISA claim matches its page.

### Unsupported / hallucinated facts
- #1 (F4, low confidence) cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole, sourcing_note: "OX Security's analysis is the source of the mechanism, the preconditions, the CVSS score and the Alpine fixed-package table; the project's release notes and NCSC Switzerland's advisory do not carry them." NCSC post 13155 has "Prerequisites: All of the following must apply: Linux system using musl libc; sshd built and run with PAM support disabled; `PasswordAuthentication` enabled; Network access to the SSH service", and the OpenSSH notes say the bug affects Linux systems "when built and run with PAM support disabled" on musl. The entry's Exposure line cites NCSC for exactly these conditions, so the note contradicts the body. Name only what is OX-only (mechanism, the `*`-account condition, CVSS score, Alpine table).

### Editorial / less-is-more flags (advisory)
- #2 (F11, low confidence) cve-2026-116779-freeswitch-sip-message-api-command-execution, sourcing_note: "The vendor advisory is the only source for the exploitation claim, the score, the affected range and the fix; BSI CERT-Bund's advisory ... lists versions before 1.11.3 as affected". BSI's CSAF carries product_version_range "<1.11.3" and the fixed product version 1.11.3, so the first clause contradicts the second; say vendor-only for the exploitation claim and the score.
- #3 (F11, low confidence) cve-2026-116606-barracuda-esg-auth-bypass-root-rce, sourcing_note: "Barracuda's pages name 9.4.0.029 as the fixed build." Only Campus does ("Appliances should upgrade to 9.4.0.029 and above."); the Trust Center says "Remediation: Upgrade to the latest firmware version". Say "Barracuda Campus names 9.4.0.029".

### Missed angles
None found. KEV catalogue 2026.11.04 (newest addition 2026-11-04, none in the window), NCSC Switzerland feed (post 13155 newest, covered), four open searches (Barracuda exploitation, OpenSSH musl exploitation, in-window exploited edge flaws, Swiss municipal incidents, BACS weekly) surfaced nothing dated in the window that the run missed; the Swiss federal and Graubünden SharePoint breaches that came up are already in the store (2026-08-05, 2026-08-06). Coverage looks complete for the sources surveyed.

Other checks with no finding: every evidence quote verified verbatim or by hand (NCSC 13155 and the Danfoss German originals included); all `techniques[]` ids are active in the pinned ATT&CK v20 dataset (T1574.001 is "DLL", T1685 "Disable or Modify Tools", T1688 "Safe Mode Boot") and each maps to behavior a cited source describes; registry keys all exist, no tombstones; references[] all resolve; no IOCs, em dashes, workflow vocabulary or KEV deadlines in reader-facing entry text; classification blocks present with plausible letters; priorities defensible (FreeSWITCH notable: vendor-only exploitation claim, no constituency exposure shown); actions are concrete and not duplicates of the ConnectWise or ARTEX entries' actions; run-record notes checked for truth (ESET lead, KEV sweep, entities_added match the registry diff, iteration-3 remediation statements hold). Declined advisories (Danfoss long title and summary; Q3 email body points) not re-counted.

### Verdict
NEEDS_FIXES (truth: 1, editorial: 0, advisory: 2)

### Findings summary (machine-readable)
See work/2026-11-06T0255Z-intel/verification.iter4.findings.yaml (3 records: F4, F11, F11).
