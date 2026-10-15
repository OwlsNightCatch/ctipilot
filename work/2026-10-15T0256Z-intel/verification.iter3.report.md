**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-15T04:12:41Z · ended_at=2026-10-15T04:25:48Z · duration_seconds=787

## Verification report — 2026-10-15T0256Z-intel (iteration 3)

Scope: whole ledger (99 claims, every one has a row in `verification.iter3.claims.yaml`; `tools/claim_ledger.py --coverage 3` reports 99/99 answered, 0 missing). All six entries read whole, the run record read whole, `git diff HEAD` read for both updated entries. Every cited page was fetched live this iteration (extract, raw `url`, `ncsc-csh post`, WebFetch for the CISA alert and the Born City page); the CVE record for CVE-2026-110447 was read from the CVE Services endpoint (read only, not cited).

### Prior-iteration deltas (Collabora entry), each remediation checked against the fetched source

- F4 (disabling is not a mitigation): CONFIRMED FIXED. Collabora advisory GHSA-g3vx-3m76-fghh (fetched, dated 2026-10-14): "It is not sufficient to disable the app to avoid the problem, it must be upgraded to >= 26.4.303 or removed." actions[0], `cves[].fixed`, Exposure, the Defender takeaway, the headline and the summary all now say update to 26.4.303 or remove it and that disabling does not help.
- F14 (10 September as start of exploitation): CONFIRMED FIXED. Title, headline, summary and hunt window no longer present 10 September as the start; the sourcing note and body say the earliest date is the hoster's report of 2026-09-11 (issue 354: "Since yesterday we're experiencing succesful hacks", first log line 10/Sep/2026) and the hunt runs back to at least early September. No stray "since 10 September" remains in any field.
- F6 (primary source): CONFIRMED FIXED. `sources[0]` is Collabora's own advisory (role primary, dated 2026-10-14, matches the page); the GitHub Advisory Database record (GHSA-f97p-r72q-64h2, "exploited in the wild in September and October 2026", Unreviewed, 2026-10-14) is corroborating. Reliability A is consistent with a vendor advisory.
- F8 (vendor-advisory facts): CONFIRMED FIXED. Not-running-server condition ("The attack only works while the built-in CODE server is not running. So on a container restart, an upgrade, or after a crash"), EOL Nextcloud <= 29 guidance, standalone Collabora not affected, and "This is not the same path as CVE-2025-66208, and the fix for that issue does not prevent it" are all carried and match the page. CVE-2025-66208 is in the CVE index.
- F16 (priority): ACCEPTED. `high` clears the bar: exploited, unauthenticated, CVSS 4.0 9.2 (CVE record: baseScore 9.2, PR:N, CWE-78; both GitHub pages show 9.2), persistent web shells that survive the update, update-or-remove decision inside seven days, Nextcloud is plausibly run by the constituency. Not an unexploited or non-default-only flaw.
- Trimmed narrative: every cited clause is still attached to its source. I found no clause that lost its citation and no fact that migrated to a source that does not carry it. The one residue is the issue-354 paraphrase in F4 #1 below.

### Unsupported / hallucinated facts

F4 #1 (low confidence) `2026-10-15/cve-2026-110447-collabora-code-server-nextcloud-rce`, body: "Other administrators report the same compromise, one noticing it because Nextcloud's integrity check failed on an unexpected PHP file, and one reports that the request still reached proxy.php after the app was deactivated". Issue 354 (raw page data) attributes both facts to one commenter, UlliDieckmann: 2026-09-11 "Exactly the same happened to me. Fortunatly I updeted nextcloud so the integrity check failed as a php file called shx13a86.php was created", and 2026-09-14 "The http request from above still uses proxy.php from the deactivated app" (the same 14 Sep comment begins "I upgraded to 26.4.303 and the app is still activated", so the "deactivated" remark is itself inconsistent). "one ... and one" reads as two administrators. Fix: one administrator, or drop the deactivated-app clause since Collabora's own advisory now carries the point.

F4 #2 (low confidence) same entry, `sourcing_note`: "whose author handles and the maintainers' replies are not individually attributed on the page". The live page attributes every comment to a named account (UlliDieckmann, timar "Andras Timar" MEMBER, mmeeks "Michael Meeks" authorAssociation NONE, HeikoBw, ahlund, nembo81, zaicurity, symptog, caolanm CONTRIBUTOR); the unattributed look was an extraction artifact. The body ("The maintainers answered ...") and `evidence[3]` ("(project maintainers)") credit mmeeks' replies to "the maintainers", which the page does not mark (mmeeks is authorAssociation NONE; the member, timar, only wrote "I believe it's fixed there"). Fix: delete the sentence; say "a reply on the issue" unless a maintainer role can be shown.

F4 #3 (low confidence) `2026-10-15/fake-watchguard-vpn-client-site-credential-capture`, title "leaving endpoint tools nothing to flag" and Detection "the endpoint sees nothing malicious". Huntress (https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing) says "there's no trojanized installer or malicious DLL for security defenses to flag" but also "Huntress Managed Defender flagged the incident 21 seconds after the malicious domain loaded", which the entry's own body repeats. An endpoint product did flag the activity, so "nothing to flag" and "sees nothing malicious" contradict the entry's body and the source. Fix: "no malicious file for endpoint tools to flag"; Detection: "no malicious file or process, so the signal is in web proxy and DNS telemetry".

### Editorial / less-is-more flags (advisory)

F11 #4 `2026-10-15/cve-2026-110447-collabora-code-server-nextcloud-rce` `sourcing_note`: four sentences, the first about 70 words, one of them about how the page renders (see F4 #2). The note should be two sentences of provenance.

### Checked and clean (no finding)

- Cisco CVE-2026-76519 (critical): every clause checked on the Cisco advisory (raw HTML shows CVE-2026-76519 and CWE-23 relative path traversal, CVSS 3.1 base 9.8, fixed releases 15.5.5-014 / 16.5.0-780, 16.0 migrate, Content Scanner Tools 25.3.0.5525, no restart, "In October 2026, the Cisco PSIRT became aware of active exploitation", system_logs messages, cluster SSH-key paragraph), BleepingComputer (CVE-2026-76461 "last month") and the CISA alert (WebFetch, four KEV additions incl. CVE-2026-76519). The "four weeks" is arithmetic from the store's own 2026-09-14 disclosure of CVE-2026-76461; not a defect. Priority critical clears the bar (exploited, unauthenticated root on the mail path, no workaround, Cisco contacted compromised Cloud tenants).
- PAN-OS CVE-2026-0322 (high): Palo Alto advisory read in full (ATTACKED tag, "Very limited exploitation", CVSS-B 8.6 / 8.5 with jump box, CWE-94, all fixed builds, 11.2.16 "ETA: 10/15", Threat IDs 510046/510047, three FAQ IPs correctly not reproduced), BleepingComputer (asked when exploitation began, who is behind, whether firewalls were compromised) and CISA. Iteration 1's F3 remediation holds.
- Fake WatchGuard VPN site (notable, single-source): all clauses match the Huntress post (7 Oct incident, Bing redirect, popup.js ~150 lines, forced rejection, genuine signed installer, 21 seconds, WHOIS 2026-08-22 / 2026-09-14, offline 2026-10-13, January Secplicity and March Storm-2561 context). `single-source` with a two-sentence sourcing note, B2, is right; no IOCs.
- PK Softech / Publica update: PKZH notice (dated 2026-10-13) and Publica status of 2026-10-14 match the section, the three new `evidence[]` quotes and the translations are faithful; record `summary` equals the section; `updated_at` mirrors the record `at`; actions[] replaced, not accumulated. Main analysis, summary and takeaway do not contradict the new state.
- Danfoss improvement: every Censys figure and firmware boundary matches the Censys post (1,825 to 537, -71 percent, 4.2.4 / 4.3.1, 1,166 to 966, Poland 81 / Romania 80); the improvement type is defensible (depth added, no claim reversed); `updated_at` unchanged. The pre-existing AFP, BFMTV, Infosecurity, BleepingComputer, Cooling Post, Blick, CERT-FR (revision dated 13 octobre 2026) and NCSC.ch hub 13054 claims all re-verified.
- Run record notes: counts, KEV sweep, backlog row (unchanged, expires 2026-10-20), gap 24.0 h (previous start 2026-10-14T02:55:54Z), previous publish_status ok, iteration counters (iteration 1: 8+2+2 = 12 findings; iteration 2: 2+3+0 = 5) all hold on disk.
- No em dashes, workflow vocabulary, IOCs, KEV deadlines, TLP or org-triage artefacts in any reader-facing field; classification block present and plausible on all six.

### Missed angles

None I can name with a plausible in-window source. Checked CERT.at's end-of-day report for 2026-10-14 (Chrome 155, Patch Tuesday, curl, Adobe, Fortinet FG-IR-26-178/184/185 already dropped, DNSSEC connectors) and general searches for Swiss public-sector incidents; nothing new in the window. Considered and not flagged: Ghostscript CVE-2026-39919 (Born City, 2026-10-14, hedged "wohl angegriffen" with no named reporter; two earlier fires dropped it on identical facts, searches show no confirmed exploitation or KEV listing), Ahold Delhaize (2026-10-12, before the window), CISA's SSVC "Exploitation: none" on the CVE record of CVE-2026-110447 (not cited; first-hand issue reports outweigh it). Coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 1)

### Findings summary (machine-readable)

See `verification.iter3.findings.yaml` (4 records: F4 x3, F11 x1).
