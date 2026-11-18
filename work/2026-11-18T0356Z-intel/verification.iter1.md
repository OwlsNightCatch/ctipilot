**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-18T05:22:20Z · ended_at=2026-11-18T05:46:22Z

## Verification report — 2026-11-18T0356Z-intel (iteration 1)

Scope: first pass, all 296 ledger claims answered (`verification.iter1.claims.yaml`: 281 ok, 8 F3, 5 F4, 2 F14, 0 unreadable; `claim_ledger.py --coverage 1` reports 296/296). All 10 new entries, the 3 updated entries (full read plus `git diff HEAD`), the run record, `prior_coverage.json`, `cves_seen.json` and the registry were read. Pages were read from the gate's saved bodies and re-fetched where a claim needed it (CVE.org API for the 10 TYPO3 and 24 N-central ids, ENISA EUVD, FIRST EPSS, GitHub advisories API, NCSC.ch hub posts 13196 and 13198, BSI CSAF, CERT-FR, Drupal PSA RSS and WebFetch, PyPI JSON, Axis PDF, CISA KEV JSON). Sources the gate could not read directly: drupal.org PSA (client challenge; confirmed through the PSA RSS feed and WebFetch).

Dedup: none of the new entries' CVEs appears in `prior_coverage.json` or earlier in `cves_seen.json`; all `references[]` targets exist; registry keys used by the entries exist. Missed angles: the NCSC.ch hub shows only posts 13196 and 13198 inside the window (both covered), the single in-window KEV addition is covered, and the CVEs surfaced by my searches (Cisco ISE and SEG, BeyondTrust, Outlook, Craft CMS) are already in the store. Coverage looks complete.

### Citation does not support the claim
- #1 (F3, low confidence) Puppet: "Puppet's release notes list the flaw as fixed in Puppet Enterprise 2026.0.1, 2025.12.1 and 2023.8.13" — the PE 2026.0.1 notes list CVE-2026-115731 under "The following CVEs were fixed in PE" with no per-CVE versions; 2025.12.1 and 2023.8.13 come from the EUVD record. The source date 2026-11-03 for that page has no dateline ("Released November 2026").
- #2 (F3, low confidence) Puppet: "The upgrade changes `auth.conf` wildcard matching" — listed as an Enhancement of PE 2026.0.1 only, not for 2025.12.1 or 2023.8.13.
- #3 (F3) Drupal Exposure: "the PSA names no module or configuration condition, so the version decides" — the PSA vector reads `AC:Complex/.../E:Proof/TD:Uncommon` with "Only uncommon module configurations are exploitable".
- #4 (F3, low) COLD RELIC Triage: "GTIG's discriminators are an unfamiliar device, a non-corporate or residential-proxy network, or an enrolment right after an MFA-fatigue pattern" — GTIG states no such discriminators.
- #5 (F3, low) Barracuda Detection: "new branches in many repositories" — blog says "a handful of repositories".
- #6 (F3, low) Barracuda: "expire vendor credentials when an engagement ends" cited to the blog; it is on the Trust Center page.
- #7 (F3, low) TYPO3 Detection: "HTML or SVG files in the form upload folder and web-server logs" cited to SA-029, which gives no detection guidance.
- #8 (F3, low) N-able: "ask each IT provider ... whether it runs a server on premises and has upgraded it" cited to Field Effect, which does not say it.

### Unsupported / hallucinated facts
- #9 (F4) agent-framework Exposure: "the lockfile or `pip list` shows the installed version" — SafeDep: "look for either startup file without starting the environment's Python. Starting it would run the stealer again." `pip list` starts Python in the affected environment and re-runs the stealer. The entry also omits that caution.
- #10 (F4) COLD RELIC summary: "In both cases ... kept access with enrolled passkeys, MFA backup codes and rogue MFA devices that survived password and session resets, then exported whole tenants" — Case 2 was one new MFA device and a bulk download of one user's drive; the rest is Case 1.
- #11 (F4) N-able `cves[CVE-2026-129271].affected` "(CNA wording: before 2026.4.1 HF3)" — the CNA record scopes it to "N-central Patch Management Component" before 2.14.4.5829.
- #12 (F4, low) N-able CVE-2026-129286 and -129287 `auth: post-auth` — CNA vectors are PR:N.
- #13 (F4, low) RIKEN `techniques[]` T1021.004 — no cited source says SSH carried the attempted connections.

### Quantifier without source
- #14 (F14, low) Oracle: "only interim control/relief is blocking the network protocols" — Oracle's page names a second measure (removing privileges) for privilege-requiring attacks.
- #15 (F14, low) OptimJack headline: "poisoned scripts on 178 sites" — Report URI: "188 snippets belonging to 178 organisations"; the count is Report URI's, not Optimizely's.

### Needs more research
- #16 (F8) Java4Shell omits the Tenable-reported Immersive claim of a working exploit ("Tomcat's Basic authentication and the java-jwt library provide ways to exploit the flaw before a user logs in"; unreleased); the sourcing_note's "no independent reproduction ... was found" and the headline's "no attacks yet" need that qualifier.
- #17 (F8) Java4Shell Exposure/Detection: no CPU families or `/proc/cpuinfo` flag check (avx512f, avx512bw, avx512vbmi, bmi2) although Calif, Tenable and Upwind give them; Exposure omits the Java 8 Enterprise Performance Pack the actions name; Detection omits Upwind's request-shape signal and `IllegalArgumentException` bursts and Talos's Snort coverage.
- #18 (F8) Drupal: the PSA vector (E:Proof, AC:Complex, TD:Uncommon) is dropped; only "18 of 25" is carried.
- #19 (F8) TYPO3 SA-028: ImageMagick/MVG precondition and the advisory's post-update image-format configuration are omitted while the SA-032 and SA-034 actions are carried.

### Surface contradiction
- #20 (F9, low) OptimJack: Ohey dates the Optimizely loader from 13 November, Report URI first sees it on 16 November 04:21; the body now attributes only Kissmetrics/StorifyMe/minute-ly to Ohey and silently adopts Report URI's date.

### Drop (low relevance / off-audience / duplicate)
- #21 (F7, low) RIKEN: out-of-nexus single-victim incident, method unknown, no stated relevance ground; hold to routine or drop.

### Org-triage line missing / inconsistent
- #22 (F16, low) Puppet `notable` on a CISA KEV exploited management-plane RCE (Red Hat Satellite uses it by default).
- #23 (F16, low) Drupal `notable` for a critical pre-announcement with an in-day release window and an NCSC.ch advisory.
- #24 (F16, low) Apache/Axis `notable` after the update adds a vendor-confirmed unauthenticated 9.8 on every current AXIS OS with no fix.

### Action-item discipline
- #25 (F18, low) COLD RELIC actions[0]: the remediation clause restates the Detection paragraph; keep the hunt.

### Editorial / less-is-more flags (advisory)
- #26 (F11) sourcing_note fetch vocabulary and length: Puppet ("no reader returned"), Drupal ("WebFetch reading", "direct readers"), COLD RELIC and agent-framework ("could not be read"), N-able (very long).
- #27 (F11) OptimJack update: "the entry first relied on", "the entry's statement ... stands", "settles the access question" (Optimizely names no flaw class); section repeats body sentences.
- #28 (F11) `updates[].summary` narration: N-able ("the entry's statements ... are replaced"), Apache ("the entry's list ... now includes it").
- #29 (F11) Barracuda and RIKEN carry no one-clause relevance ground (prompts/cti-run.md "The incident floor").
- #30 (F11) Apache headline "Linux distros fixed" (SUSE overall state "Pending").
- #31 (F11) `entities/registry.yaml` campaign:optimjack summary still dates the Optimizely files from 2026-11-13.
- #32 (F11) Run-record calibration note omits N-able (`high`) among the entries the run touched.

### Checked and clean
Puppet CVSS (CNA 4.0 9.4, Red Hat 3.1 9.9), EPSS 0.00366, affected/fixed ranges, KEV addition; Java4Shell versions, Oracle row, Calif/Tenable/Upwind/Talos/NCSC/BACS statements; all ten TYPO3 CVE ids and CVSS against CVE.org; Oracle tally from the 655 matrix rows (62 rows at 9.0+, 56 unauthenticated, 57 CVEs, six 10.0 changed-scope rows, CVE-2025-61882 ransomware flag in KEV); Mitel scores, patch KB, MISA-2026-0006 range and BSI/CERT-FR; agent-framework timeline (33 minutes), PyPI listing, Socket and SafeDep behaviour; Barracuda, RIKEN and COLD RELIC narrative facts; the 17 new N-central CVE ids and all 17 scores and descriptions against CVE.org plus HF3 notes and Huntress; Axis advisory text and workaround; all evidence quotes the gate checked; changelog records (types, `updated_at`, `fields` versus `git diff`, no silent edits); no IOCs, em dashes or KEV deadlines in entry text; classification blocks present and within vocabulary; no org_triage or watchlist use.

### Verdict
NEEDS_FIXES (truth: 15, editorial: 10, advisory: 7)

Highest-weight items to fix first: #9 (agent-framework `pip list`, operationally harmful), #10 (COLD RELIC summary), #11 (N-able CVE-2026-129271 scope), #3 and #18 (Drupal vector), #16 and #17 (Java4Shell exploit-readiness and how-to-tell). Findings in machine-readable form: `work/2026-11-18T0356Z-intel/verification.iter1.findings.yaml`.
