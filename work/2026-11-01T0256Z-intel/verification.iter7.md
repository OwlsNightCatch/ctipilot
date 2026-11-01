**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-01T05:50:42Z · ended_at=2026-11-01T06:06:15Z · duration_seconds=933

## Verification report — 2026-11-01T0256Z-intel (iteration 7)

Scope: post-fix pass after the iteration-6 NEEDS_FIXES. All 149 ledger claims of claims.iter7.yaml walked (the six changed claims, every claim of the six entries; no sampling needed because the ledger is the six entries); rows written to verification.iter7.claims.yaml, `tools/claim_ledger.py 2026-11-01T0256Z-intel --coverage 7` reports 149/149 answered, 0 missing. Whole entries read for all six, `git diff HEAD` on each, run record read end to end, registry diff read, `entry_record.py diff` field lists compared with each record's `fields` (all match).

Pages read this iteration (fetched fresh): Palo Alto PSIRT advisory (extract) and JSON record (timeline, workarounds, exploits), Wayback copy of 2026-10-27 17:10 UTC, Dream Research, Unit 42 brief, Hunt.io (extract and raw HTML dates), GreyNoise tracker (live: 1,177 confirmed, 5 IPs; definition sentence; 10-28, 10-29 and 10-31 command rows), CISA KEV catalogue 2026.10.30 (PHP and kernel rows; additions since 10-28), CISA PHP alert (WebFetch), php.net archive raw HTML (2026-10-21-5, 2026-10-23-1, 2026-10-26-1), both GHSA pages, Sansec, Cloudflare, Wordfence x2, watchTowr, VulnCheck, Karimi report, SecurityWeek, BleepingComputer x2, CrowdStrike, Sophos, SANS ISC, Red Hat, The Hacker News x3, PHP Foundation, CERT-EU, ENISA, BACS, ReliaQuest, Cisco PHP and eMudhra advisories, Fortinet, Splunk, Tenable x2, Siemens, WatchGuard, Citrix, nau.ch x2, Publica, Inside IT, SRF, Blick, OpenJDK emudhra page (extract and raw), both OpenJDK advisories, Oracle alerts 91403 and 114820 (rev 2), MSRC, Google, Mozilla, Go announcement, GitLab page and security-releases feed, Python Insider post and feed, Python security-announce thread, ENISA EUVD JSON, Python Discourse thread (JSON, post 3 author name), Dennis Jackson tracker (extract and raw, Java and pending rows), THN eMudhra, eMudhra press release, GTIG and Mandiant (extract and raw HTML including the lifecycle table), vd.ch, RTS, NCSC.ch Security Hub recent posts.

### Iteration-6 remediations (checked first)
- F3 eMudhra (per-runtime repeat): CORRECT. Raw openjdk.org/emudhra: "If you have more than one standalone OpenJDK Java runtime installed, repeat these steps for each installation." closes the keystore-removal item; the revocation item says only to add the two flags "to the application's java command line". The sentence now attaches "repeating for each installation" to the keystore alternative only.
- F4 PAN-OS (every release): summary and both cves[].affected are CORRECT against the advisory ("< 12.2.4-h1 | >= 12.2.4-h1", per-train "< hotfix" rows). The title still says "affect every release": see F4 below.
- F11 actions[2] 'backup, storage': removed; remaining list checked, 'wireless controllers' not literal in sources (F11 below).
- F11 Vaud Detection line: removed; the entry is now one paragraph plus the Defender takeaway, which matches the canton's recommendations.

### Unsupported / hallucinated facts
#1 (F4) PAN-OS entry, title: "the PHP2Shell flaws affect every release through the management web interface ... all twenty hotfixes are out". Advisory read today: "| PAN-OS 12.2 | \< 12.2.4-h1 | >= 12.2.4-h1 |" (Affected | Unaffected), per-train rows for 12.1, 11.2, 11.1, 10.2 likewise; "12.2.0 through 12.2.4-h* | Upgrade to 12.2.4-h1 or later"; CPE applicability "up to (excluding) 12.2.4-h1". The summary and affected fields were fixed in iteration 6 but the title carries the same overstatement and contradicts its own second half. Fix: "affect PAN-OS and Panorama releases below each train's hotfix".

### Citation does not support the claim
#2 (F3, low confidence) PHP2Shell main entry, Hunt.io record and body citations "[Hunt.io, 2026-10-30]". Raw HTML: data-framer-ssr-released-at="2026-10-28T17:59:09.324Z" (also the extract's date), data-framer-page-optimized-at="2026-10-30T14:38:57.896Z" and the comment "Published Oct 30, 2026, 2:38 PM UTC" (site publish); the visible "Published on" is empty. The article was revised after Dream's 29 Oct update, so 10-30 is the revision stamp, 10-28 the release stamp. Date the record 2026-10-28 or say "revised 2026-10-30".

### Needs more research
#3 (F8, low confidence) PAN-OS entry, body: "Threat ID 543004 helps only where inbound management traffic is decrypted on a dataplane interface with threat prevention enabled". The advisory lists 543004 as the Frontier Virtual Patching (ATP Plus, PAN-OS 12.2.4 and later) advance signature and, for Threat Prevention subscribers, "543004, 97622, 97623, ... 97678" under the four conditions. This run's rewrite kept one ID and dropped the range and the earlier threat-log pointer. Restore or say the advisory lists them.

### Editorial / less-is-more flags (advisory)
#4 (F11, low confidence) PHP2Shell main, actions[2]: "wireless controllers" is not in any cited vendor page (Cisco lists Ultra-Reliable Wireless Backhaul / Unified Industrial Wireless Software).
#5 (F11, low confidence) ARTEX, Update 2026-11-01: "wrote web shells under incrementing file names" against GTIG's "somewhat-incremental file names" and "likely intended to poison MySQL logs".
#6 (F11, low confidence) ARTEX techniques[]: the GTIG lifecycle table (in the raw HTML, dropped by extract) describes Kerberoasting, DCSync, Pass-the-Ticket/Hash attempts and Kudu API command execution; T1087.002 and T1580 were added from that table but not T1558.003 or T1003.006, and the section omits the AD behaviours.
#7 (F11, low confidence) ARTEX: Microsoft's "since at least September 2026" beside GTIG's "at least August 2026" for the overlapping UNC7228 campaign, unreconciled (also noted by iteration 5).
#8 (F11, low confidence) eMudhra headline "Windows now drops the roots": MSRC removed seven certificates (six G3 roots and an AAA cross-sign) and "is evaluating the remaining eMudhra roots separately".

### Not findings (checked)
- Updated-entry contract (4c): `updated_at` equals `at` for the four `update` records (PAN-OS 03:27:57Z, PHP2Shell 04:10:00Z, ARTEX 03:29:45Z, eMudhra 03:32:20Z); the Fragnesia `improvement` (03:28:54Z) leaves `updated_at` at 2026-10-29T04:52:00Z; each non-internal record has its section and vice versa; `entry_record.py diff` field lists equal each record's `fields`; the "one unnamed vendor" supersession is stated in the PHP2Shell and Fragnesia sections; no em dash or workflow vocabulary in reader text (the one em dash is inside a verbatim OpenJDK quote); no IOCs.
- Every PAN-OS, Dream, Unit 42, GreyNoise (10-28 first shell, 10-29 reverse shells, .ssh creation, metadata queries, linPEAS and gitleaks downloads; 10-31 gitleaks runs over /var/www/html, /srv, /root, /opt, /home), Hunt.io, GTIG (UNC7228 overlap, forks incl. a commercial one, 2 to 25 s bursts, MySQL general-log JSP shells), MSRC, Cisco v1.5, GitLab, Python, Oracle rev 2, tracker (Java 27.0.1.0.3 etc. fixed, OpenJDK pending; Bottlerocket, HarmonyOS, certbot, containerd, Godot, LibreOffice pending), OpenJDK, vd.ch and RTS claim is carried by the page cited; Vaud French originals match verbatim and RTS adds the pupil suspicion as the entry says. Quote-literal gate passes.
- Date nuances accepted: GTIG datePublished 2026-10-30 with og published_time 2026-10-31T02:18Z (one day, timezone artifact); the GreyNoise tracker now reads "Last updated 01 November 2026, 05:48 UTC" while the entry states the 03:48 UTC it read, count unchanged; GitLab and Python dates come from their feeds as the entries say (both feeds re-read: 2026-10-29 and 2026-10-26).
- Classification, priority, verification, sourcing_note values fit (Vaud A/2 single-source-victim; PAN-OS A/2 multi-source, high; PHP2Shell critical on KEV plus honeypot shells plus PAN-OS rooting; no org_triage, no watchlist). Actions lists: PHP2Shell 3, eMudhra 3, PAN-OS 2, Fragnesia 2, ARTEX 1; none generic.
- Run record: duration 4520 s equals started to completed; entries_published 1 and the five updated ids match git status; seven entities_added match seven registry additions; KEV window diff (six additions since 10-28, all COVERED) matches catalogue 2026.10.30 (no later catalogue); sub-agent telemetry present; verifier-1 finding count (23) matches findings file.
- Coverage looks complete: NCSC.ch Security Hub posts 13120 to 13124 are each covered (Linux kernel TCP flaw and Drupal Commerce have their own 2026-10-31 entries); searches for Swiss cantonal or communal incidents and KEV additions dated 2026-10-31 to 2026-11-01 returned nothing new.

### Operator note (not an entry defect)
Two untracked files sit in the repository root: gl_feed.xml and py_feed.xml (feed captures left by an earlier verifier pass). Do not stage them with the run.

### Verdict
NEEDS_FIXES (truth: 2, editorial: 1, advisory: 5)

### Findings summary (machine-readable)
See work/2026-11-01T0256Z-intel/verification.iter7.findings.yaml (8 records: F4, F3 low confidence, F8 low confidence, five F11 low confidence).
