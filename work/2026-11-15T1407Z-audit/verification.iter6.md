**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-15T17:44:12Z · ended_at=2026-11-15T18:10:36Z · duration_seconds=1584

## Verification report — 2026-11-15T1407Z-audit (iteration 6)

Role: post-fix pass. Scope: the 101 claim ids in `verify.iter6.scope.txt` (the 8 changed claims, every claim of the six entries remediated after iteration 5 (AhsayCBS 21, Fortinet 14, Check Point 3, LLMjacking 4, Apache httpd 11, Dixell 20), the ARTEX new entry whole, and a random quarter of the rest, 28 claims across 13 other entries). Every in-scope claim has a verdict row in `verification.iter6.claims.yaml` (101 ok, 0 non-ok). The ARTEX entry, the six remediated entries and the run record were read whole; SonicWall shows no diff vs base.

### Deltas block (iteration 5, nine findings), each checked on disk and at the source

1. Check Point F4 (R82.20 take pending): fixed. sk1000302 (raw HTML, `__NEXT_DATA__`): "Jumbo Hotfix Accumulator for R82.20 starting from Take 14" and "Check Point Firewalls R82.20 protect themselves through the Check Point IPS signatures "PHP Remote Code Execution" even when IPS is not enabled and HTTPS Inspection is not active". Check Point Research: "the portal's Apache/PHP workers experienced hundreds of segmentation faults".
2. AhsayCBS F3 (Exposure citations): fixed; the Exposure clause cites the v9.17.0 and v10.3.6 release notes, the 2026-10-12 advisory and Huntress. v9.17.0 notes (12-Nov-2026) and v10.3.6 notes (02-Nov-2026) both list "Ahsay Security Patchset for CVE-2026-105133 and CVE-2026-105134" plus remote API off and JSP engine off; announcements listing dates v10.3.6.1 to 03 November, hotfix advisory to 27 October, v10.3.6.14 to 13 November.
3. LLMjacking F14 ('first shown by X41'): fixed. Obsidian: "Separately, X41 showed that `/guardrails/test_custom_code`'s regex deny-list can be bypassed" and "full set of fixes included in LiteLLM v1.83.14-stable (released 2026-04-25)"; the CVE record (MITRE) describes "bytecode rewriting at the /guardrails/test_custom_code URI". The record summary carries no narration.
4. Audit report F4 (registry count): fixed. Registry keys added between the 2026-11-08 audit commit (7dd3e4e1) and base b010c9a: 55, of which 22 non-product (malware 7, actor 6, campaign 3, tool 3, incident 3); this audit's working tree adds exactly six product records (Amazon CloudWatch Logs, Amazon Cognito, Apple tvOS, Cisco Nexus 3000, Sophos UTM, Veeam Recovery Orchestrator). The audit's systemic finding 7 line is right.
5. Fortinet F8 (8.0.0 to 8.0.1 to 8.0.2): fixed; actions[0] names "every FortiManager and FortiAnalyzer on 8.0.0 or 8.0.1, 7.6, 7.4 or 7.2 to 8.0.2, 7.6.8, 7.4.12 or 7.2.13". FG-IR-26-244: 8.0.0 through 8.0.1 upgrade to 8.0.2.
6. AhsayCBS F11 (title 'carry the fix'): title and headline fixed ("now list a patchset"). The record summary still says "now carry the fix": advisory #1 below.
7. Apache F11 (headline 'SUSE fixed'): fixed; "Debian, Ubuntu, Alpine fixed, SUSE partly". SUSE CVE page: "Overall state of this security issue: Pending"; SLE 15 SP7 (SUSE-SU-2026:5231-1), SP4 to SP6 LTSS, 12 SP5 LTSS and Tumbleweed Released, SLE 16.0 In progress, 16.1 and Leap 16 Affected. Debian tracker: bookworm, trixie, forky and sid fixed.
8. Fortinet F11 (FortiClient Windows qualifier): fixed. FG-IR-26-194: FortiClientWindows and WindowsPAM 7.2.0 through 7.2.14, FortiClientMac 7.2 "Not affected", Mac 7.4.0 through 7.4.7.
9. Dixell F11 (record summary priority narration): the sentence is removed. One residual inconsistency: advisory #2 below.

### Audit report and run record against disk

- AhsayCBS row and recommendation 3 sizes: main analysis 705 to 599 words (check_run `_main_words`), headline 127 to 110 characters; Publica 1,100 (base 1,100), eMudhra 878 (base 895). Match.
- "27 entries carry one record each: 6 updates, 10 corrections and 11 improvements, 12 of them internal": counted on disk, matches; plus one new entry. SonicWall: no diff vs base.
- `ambiguous_labels` on `malware:cereal` ("Cereal") and `actor:silent-ransom-group` ("SRG"): present in the registry diff.
- KEV table (12 additions, 8 covered, 4 not covered) matches `kev-window.txt`. `tools/test_check_run.py`: 9/9 pass.
- Run record: `entries_published: 1`, `entries_updated: 27`, `updated_entry_ids` list matches the 27 entries; truth-pass claim sum 309+308+312+265+256+196 = 1,646 matches the "1,646 ledger claims" statement.

### Sampled rest (28 claims, 13 entries) — all ok

Certighost record (Kaspersky: "both groups are Russian-speaking and attack Russian companies only"; Microsoft: "has not observed confirmed threat-actor exploitation"), ANSSI record (CTI-010 page duplicates the cited PDF report), Publica (NZZ, AWP/cash.ch, BPK notice page, Inside IT), eMudhra (Cisco v1.11 product rows; Mozilla bug 2083449: "Subscriber migration arising from the RSA G2C revocations is complete"), Linux TCP (Debian trixie security 6.12.117-1 after 6.12.113-1), Brotli (Cisco v1.13, Nexus Guest Shell rows, tvOS 27.2.1 of 2026-11-13; Siemens SSA-242944 lists 15 products), N-able (hotfix page via WebFetch only, direct fetch returns 403), SAP (Patch Day table reproduced exactly; CVSS 10.0; Onapsis patch levels), BluePhishing (MC1506733), Chrome (Edge 157.0.4341.46 of 2026-11-09, Edge for Android 157.0.4341.53, CISA ADP CVSS 8.8), GhostFrame (Insikt wording), SCKit record (EUVD record added by the 2026-11-13 fire, cited nowhere).

### ARTEX in AWS (new entry), read whole

Datadog Security Labs page read in full: the S3 opening, FilterLogEvents limit of 1000, 2026-10-20 widened search, Cognito PreSignUp iteration, InitiateAuth / RespondToAuthChallenge / GetUser / GetTokensFromRefreshToken, CognitoIdentityCredentials role session name, discovery calls that failed, hundreds of consoles, .gov and .edu blocklist, "playbook is therefore left to downstream AI inference" all match. Wiz corroboration (the "zzz-nonexistent" baseline request) confirmed. All four evidence quotes verbatim. No IOC, no em dash, no pipeline vocabulary. References exist; no duplicate coverage of the Datadog post. Priority `notable`, single-source with sourcing_note, classification B/2: consistent.

### Missed angles

Checked NCSC.ch security-hub advisories 13174 to 13178 (PTC Windchill, SignDrop CLFS zero-day, Red Hat Quay): all three have entries. KEV window dispositions hold. Coverage looks complete.

### Editorial / less-is-more flags (advisory)

1. AhsayCBS record 2026-11-15T14:59:12Z: summary opens "Ahsay's standard releases now carry the fix" after the title and headline were deliberately reworded to "list a patchset"; align the record summary.
2. Dixell record 2026-11-15T14:53:24Z: "so only the password flaws and CVE-2026-124014 stay unfixed" differs from the section (unfixed exposure = pre-2021 fleet plus password flaws; CVE-2026-124014 is a blog/CNA disagreement). Suggested: restate what the section says.
3. Reader-facing record summaries that narrate the edit ("the entry also gives" on Apache; "The Triage line now names" on GhostFrame and CopperDragon; "the section notes", "now cited" on Publica; "the title and summary now say" on eMudhra; "the summary" on SSHole; "the headline gives" on BluePhishing).
4. Dixell: "any pre-2021 unit" in the takeaway with no way to recognise one in Exposure (CNA records: below 5.6.2 or 5.7.0).
5. Check Point: Exposure and takeaway do not carry the R82.20 built-in IPS protection the new section reports.

### Verdict

CLEAN (advisory: 5; truth 0, editorial 0). Every advisory item may be left; nothing evidenced in this pass is false, unsupported or mis-cited.

### Findings summary (machine-readable)

See `verification.iter6.findings.yaml` (five F11 records).
