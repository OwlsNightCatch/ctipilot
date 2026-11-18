**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-18T06:17:24Z · ended_at=2026-11-18T06:37:45Z · duration_seconds=1221

## Verification report — 2026-11-18T0356Z-intel (iteration 3)

Post-fix pass. Scope walked: all 14 claims in claims.changed.iter3.yaml, every claim of the five entries remediated in iteration 2 (Java4Shell, agent-framework, Drupal, N-able, Apache), and a random quarter (43 of 172, seed 20261118) of the rest; in practice every new and updated entry was read end to end against pages fetched this iteration and all 303 ledger rows are answered (`python3 tools/claim_ledger.py 2026-11-18T0356Z-intel --coverage 3`: 303/303). Rows: `verification.iter3.claims.yaml` (300 ok, 3 F3 low confidence).

### Prior-iteration deltas (iteration 2 findings and their remediation)

- Java4Shell decoder wording: LANDED. Exposure now says "the basic or URL decoder of java.util.Base64"; Upwind: "Untrusted Base64 reaching Base64.getDecoder() or getUrlDecoder()"; Equixly: "only the basic and URL decoders of java.util.Base64 reach it".
- Java4Shell "no release stated": LANDED in body, summary and sourcing_note; Tenable: "The post does not say that the exploit has been released."
- Java4Shell version clause: LANDED. Oracle's risk matrix row (8u511b33-perf, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3) is now the cited source; the BACS-terminated remainder still carries two uncited sub-facts (finding #1, low confidence).
- Java4Shell Detection split: LANDED. Equixly keeps the hs_err_pid statement ("Do not expect the log to name Base64: the crash comes later"); restart bursts and request-shape signals are Upwind's; the process and administrative-activity hunts are marked as following from Calif's chains.
- agent-framework "image build logs": dropped from Exposure (SafeDep: "Look for the versions in lockfiles and requirement files"). The same shape survives in Detection and actions[0] ("CI job logs", "build caches") and a sign-in-log clause is cited to Socket, which does not carry it (finding #2, low confidence).
- Drupal: LANDED. Exposure names "Drupal before 10.6 and Drupal 11 before 11.3" (PSA: "All versions of Drupal prior to 10.6.x as well as all versions of Drupal 11 prior to 11.3.x are end-of-life"); the absence sentence and the drupal.org/security source are gone; no transport wording left in sourcing_note.
- N-able: LANDED. CVE-2026-125879 and CVE-2026-125882 are admin-required; the CNA records (EUVD-2026-122959, -122963) carry PR:H, as do -125880 and -129273. sourcing_note is shorter but still 168 words (finding #6).
- Apache: LANDED. The Defender takeaway now cites Wiz ("temporarily disable HTTP/2 support to eliminate the attack vector"). sourcing_note is 121 words.
- The three declined F16 challenges (Puppet, Drupal, Apache) were not re-raised; the run record's calibration note gives reasons and I found nothing in the pages that overturns them.

### Citation does not support the claim

- #1 (F3, low confidence) Java4Shell, Exposure: "...at or below the affected builds ([Oracle, 2026-11-17]) on an x86-64 host, covering standalone runtimes, runtimes bundled in applications and appliances, and containers; the running build, not the installed package, decides ([BACS, 2026-11-18])". BACS (fetched, German) says "Die Schwachstelle betrifft bestimmte Java-Versionen auf bestimmten, weit verbreiteten Prozessortypen", "Die Prüfung muss auch Java-Komponenten innerhalb von Anwendungen, Geräten und Containern umfassen" and "Prüfen Sie, ob die laufenden Anwendungen tatsächlich die korrigierte Java-Version verwenden"; it names no x86-64 and no standalone runtimes. The NCSC.ch Hub post 13198 (already a source) states "Check standalone runtimes, application-bundled Java, containers, appliances" and "Verify that the running applications actually use the patched runtime". Fix: cite the Hub post for the scope list, move "on an x86-64 host" before the Oracle citation (or cite Calif). Claim 0c8d60f89a.
- #2 (F3, low confidence) agent-framework, Detection: "installed-package inventories and CI job logs for the two versions, a .pth file ... ([SafeDep])" and "because the stealer requests identity tokens, Azure and GitHub sign-in logs for those identities from unfamiliar addresses show later use ([Socket])". SafeDep names lockfiles, requirements files and the two startup files, no inventories or CI job logs; Socket (grep of the full extract) has no sign-in-log statement and neither page says "unfamiliar addresses"; SafeDep says "Review sign-in and activity logs for the managed identities and federated credentials that environment could use, from the install time onward". Fix: cite SafeDep for the sign-in-log review, mark "unfamiliar addresses" as the entry's own hunt idea or drop it, say lockfiles and requirements files for the version check (also in actions[0], "build caches and CI job logs"). Claims c2e4646eed, 482df7ef21.

### Claims missing inline citation

- #3 (F5, low confidence) Java4Shell, sourcing_note: "Early source-reading analyses (Equixly, and Upwind before its update) expected a JVM crash". Upwind's current page, the one cited, says "It's just a crash. Wrong." and keeps no record of its earlier reading; the page that carries it is The Hacker News (https://thehackernews.com/2026/11/oracle-to-patch-11-java-flaws-today-as.html: "Separate analyses of the OpenJDK source code by security companies Upwind and Equixly point to a flaw in Java's Base64 decoder whose likely result is a crash of the Java virtual machine rather than code execution"), which is not in sources[]. Add it as corroborating or drop the Upwind half.

### Needs more research

- #4 (F8, low confidence) N-able, 2026-11-18 update: Field Effect (cited in the body, in sources[]) says under "Update 3: November 16, 2026": "Shortly after the HF3 release, technical details on 24 further N-central vulnerabilities were published. These are reported to be addressed by HF3 and not exploitable on deployments running the latest update." The update section carries Huntress's 17 and never mentions or reconciles the 24. Add one attributed clause or note the difference.

### Editorial / less-is-more flags (advisory)

- #5 (F11) agent-framework, Detection (line 65): "(look for it on disk without starting the environment's Python, because starting it runs the stealer again ([SafeDep, 2026-11-18](...))" opens a parenthesis that is never closed (5 opening, 4 closing on the line).
- #6 (F11) sourcing_note length: N-able 168 words in four sentences, Apache 121 words in three. The contradictions (CNA wording versus Huntress, BleepingComputer versus Censys on the date, Wiz versus Red Hat on the exploit) are worth keeping; the rest belongs in the body or can go.
- #7 (F11, low confidence) Drupal body: "with attack complexity Complex"; the PSA's metric reads "AC - Access complexity: Complex or highly specific" (WebFetch of https://www.drupal.org/psa-2026-11-16).

### Checks that came back clean

Fetched this iteration and matched: Calif (raw HTML; the extract drops the write-up), Tenable, Oracle CSPU risk matrices (tallied: 62 rows at CVSS 9.0 or above, 56 with remote exploit without authentication, six at 10.0), OpenJDK advisory, BACS, NCSC.ch Hub posts 13196 and 13198, CISA Java alert and KEV feed (CVE-2026-115731 added 2026-11-17, ransomware flag Unknown; CVE-2025-61882 Known), Talos, Upwind, Equixly, SafeDep, Socket, Drupal PSA (WebFetch), N-able HF3 notes, Huntress, Huntback, Field Effect, The Hacker News, Axis PDF, Apache project page, Red Hat CVE page, Wiz, RIKEN, Barracuda blog and Trust Center, GTIG COLD RELIC, Report URI, Optimizely status, Hudson Rock, Mitel MISA-2026-0012, BSI CSAF, TYPO3 SA-025 to SA-034 and release announcement, Puppet release notes and ENISA EUVD (N-able, TYPO3 and Puppet CVE scores and vectors, via the EUVD search API). Saved bodies were used for Ohey, Wordfence, Debian, Alpine, SUSE, Ubuntu, Red Hat errata, the researcher repository and CERT-FR. No IOCs, no em dash outside changelog headings, no workflow-internal vocabulary, `org_triage` null and no watchlist use on every entry, classification present and plausible on every entry, main analyses at or below about 530 words, updated_at mirrors the last non-internal `update` record, every record summary matches its section.

### Missed angles

None evidenced. The run record's telemetry shows no stalled sub-agent and no unmitigated 403/429 on a source that carried the window's items; the one KEV addition is an entry; I looked for a recent actively exploited or Swiss-nexus item and found only older material (Cisco SD-WAN CVE-2026-20245 is dated 2026-06-09). Coverage looks complete for the critical/high signal.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 2, advisory: 3). All four non-advisory findings are small and marked low confidence; none changes a priority, a CVE field or an action.

### Findings summary (machine-readable)

See `work/2026-11-18T0356Z-intel/verification.iter3.findings.yaml` (7 records).
