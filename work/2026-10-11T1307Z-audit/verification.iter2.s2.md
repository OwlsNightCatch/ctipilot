**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-11T16:12:54Z · ended_at=2026-10-11T16:33:45Z · duration_seconds=1251

## Verification report — 2026-10-11T1307Z-audit (iteration 2, slice s2, post-fix pass)

Scope: 19 entries, 252 ledger claims, every claim answered (`verification.iter2.s2.claims.yaml`: 243 ok, 4 F4, 1 F3, 1 F13, 2 F5 rows). Every cited page was read this iteration (cached bodies first; `extract`, `url`, `ncsc-csh post`, `cisa-kev`, `WebFetch` for the two cisa.gov pages, the MSRC CVRF and the CVE record API where a rung needed it). No `unreadable` claim. The whole entry was read for each of the 19, including sections outside the ledger quarter.

### Prior-iteration deltas (all 27 walked against disk and source)

Applied fixes that hold: Kaspersky (no WinRAR; old Securelist URL answers 404, new report carries the veteran-flaw and Protected View chain text); German court ("her" in headline, summary, body; heise names a female claimant); Microsoft (Help Net Security "120+", Krebs "less likely", no KEV clause, priority high, immediate_action null, 2012 wording changed); Cisco SD-WAN (Metasploit module named, poc-public); Ghost (deep_dive cleared); Splunk (advisory dated 2026-06-10, compromise window anchored at the advisory; SecurityWeek: exploited "days after disclosure"); Liechtenstein (500,000 reframed as the 2025 proposal count, human-versus-telemetry sentence gone, shutdown quote); Nexus (summary now "crash a process that can reload the device"); GitLab (readable-file sentence, Triage line, backport action); Unbound (82717 8.4 restored, CNA record `baseScore 8.4` for the quoted vector; NCSC cited for 81642 only); conference phishing (T1546.015 gone, contradiction line added); Austria (scans limited to essential entities); Telerik (KB citation undated, "default" gone).

Residuals from applied fixes, filed below: GitLab body foothold clause (F3) and actions[0] key list (F4); Unbound action (F4); Liechtenstein shutdown lesson (F13).

Declined rationales judged: Microsoft status "exploited" (CCB, a national CERT, reports it and the body carries the Contradiction line; accepted, headline hedged); German court F11 (routine, transferable enrolment lesson; accepted); Liechtenstein F11 (three takeaways remain; stands as advisory only); Austria F7 and F11 (routine; section is the dated delta notice; accepted); Medicare date (page shows Published 25 Sep 2026 against 24 Sep in the reporting, one day, within tolerance; accepted); Telerik F11 (same reason as Austria; accepted).

Process note: my first two result batches were appended to `work/2026-10-11T1307Z-audit/s3tmp/rows.jsonl` because another verifier overwrote my helper in the shared scratchpad. I removed exactly my 34 rows (33 claim ids in this slice plus one TEST row) from that file in a single rewrite and kept the other 23 rows untouched; slice s3's owner should re-check that file is intact.

### Unsupported / hallucinated facts

1. **F4 (low confidence)** `entries/2026-05-25/ghost-cms-cve-2026-26980-clickfix-the-cms-compromise-to-endp.md`, record 2026-10-11T14:46:35Z summary: "the injection is described by the sources as a read primitive in slug-filter ordering rather than a boolean-blind injection with time-delay artefacts". GHSA: "allowed unauthenticated attackers to read arbitrary data from the database"; CVE record: "perform arbitrary reads from the database"; no cited page or the CVE record says "ordering". Fix: drop the phrase.
2. **F4 (low confidence)** `entries/2026-09-12/cve-2026-85706-gitlab-unauth-path-traversal-file-read.md`, actions[0]: "(CI/CD credentials, SSH keys, database connection strings, application secrets)". watchTowr names "configuration files, secrets, or other sensitive server-side data" and "source code, credentials, and CI/CD configuration data" only; the same specifics iteration 1 flagged survive in the action.
3. **F4 (low confidence)** `entries/2026-09-19/cve-2026-81642-cve-2026-82717-unbound-dnssec-rce.md`, actions[0]: "normal recursive resolution against an attacker-controlled zone is enough to reach a vulnerable resolver, whether or not it is exposed to the open internet". For CVE-2026-82717 NLnet Labs says only "CNAME synthesis during an upstream response"; the only stated reachability condition is NCSC-CH's, for CVE-2026-81642. Keep "patch every Unbound", drop the assertion.
4. **F4 (low confidence)** `entries/2026-08-04/liechtenstein-vwbp-beneficial-ownership-register-breach.md`, headline "...owners behind Swiss- and EU-administered structures" and takeaway "the constituency that administers those structures is largely Swiss and European". NZZ: "von liechtensteinischen Treuhändern verwaltet"; The Record: "wealth management hub for clients around the world". No source supports the Swiss/EU administrator claim that carries the entry's Swiss nexus.

### Citation does not support the claim

5. **F3 (low confidence)** GitLab main text ¶1: "...credentials and CI/CD configuration data, which turns a file-read primitive into a foothold on the CI/CD and source-control plane GitLab manages ([watchTowr])". watchTowr stops at "carries significant risk to enterprise environments"; the foothold conclusion is the entry's own.

### Analytical-link-as-fact

6. **F13 (low confidence)** Liechtenstein takeaway: "The second lesson is architectural and shows in the government's own actions: it took further systems offline as a precaution, ... Per-register segmentation and retained ... logs ... make 'was this one reached too?' a query rather than a shutdown decision." The government's reason is "zur sorgfältigen Prüfung allfälliger Sicherheitslücken" and it says there was no indication of unlawful access on those systems; no source links the shutdowns to a segmentation or log gap.

### Claims missing inline citation

7. **F5 (low confidence)** Microsoft entry, 2026-10-11 correction and record summary: "five months after CCB's statement, Microsoft still reports no evidence of exploitation". The only Microsoft statement in the cited pages is BleepingComputer's of 2026-06-01; MSRC shows "Exploited No" at original publication and a single revision (2026-05-12).

### Needs more research

8. **F8 (low confidence)** Microsoft **Exposure:** "Windows Server 2012 and 2012 R2 are also affected, and CERT-EU names no fixed build for them". Krebs and CCB (both in sources): "Patches are available for all versions of Windows Server from 2012 onwards."; MSRC CVRF 2026-May lists Monthly Rollups 6.2.9200.26079 (2012) and 6.3.9600.23181 (2012 R2). Add the rollups to the Exposure line and cves[].fixed.
9. **F8 (low confidence)** GitLab Triage/actions omit GitLab's own "three threat detections" (LFI attempts reading gitlab.yml, via metadata.path, path enumeration) from the 19.3.2 and 19.0.9 release notes.

### Surface contradiction

10. **F9 (low confidence)** GitLab CVE-2026-87719 status "exploited" rests on NCSC-CH post 12935's edit-history reason ("CVE-2026-87719 is known as actively exploited", 2026-09-14); the same post's 14.09 update text says "CISA added CVE-2026-85706 to its catalog" and carries nothing on 87719. Record the conflict or soften the status.
11. **F9 (low confidence)** German court entry: Borncity has "Ein QR-Code führte auf eine manipulierte Webseite"; heise has the customer logging in via her browser favorites bar and being asked to set up 2FA. The entry follows Borncity silently.

### Editorial / less-is-more flags (advisory)

12. F11 Ghost `sourcing_note` is "migration: evidence backfilled from v2 brief body ..." (workflow-internal and stale; evidence is now verbatim XLab).
13. F11 (low confidence) Nexus record 2026-10-11T14:02:26Z is `internal: true` but corrects reader-facing body and summary wording.
14. F11 Unbound Detection and Triage name `named`, BIND's daemon; the flaw is Unbound-only.
15. F11 (low confidence) Flink routine entry carries about 700 words of narrative.
16. F11 Liechtenstein still has three Defender takeaways (main, 09-01, 09-02 "(updated)"); main one is accurate, so leaving it is acceptable.
17. F11 Pre-existing em dashes in reader-facing text of Liechtenstein, GitLab, Kemp, Nexus.

### Whole-slice checks with no finding

Relevance, priority and classification looked right for all 19 (Cisco SD-WAN critical on KEV and CVSS 10; GitLab, Kemp, Splunk, Unbound, MS high with a decision inside seven days; the rest notable or routine). No IOCs, no TLP findings, no `org_triage` block, no watchlist tag, actions lists short. Update-vs-new decisions: the four entries that absorbed folded duplicates (Microsoft, Cisco SD-WAN, Ghost, Splunk) are the same finding as their folded duplicates. No missed-angle assessment is made in this slice (slice s6 owns run-level coverage).

### Verdict

NEEDS_FIXES (truth: 6, editorial: 5, advisory: 6)

### Findings summary (machine-readable)

See `work/2026-10-11T1307Z-audit/verification.iter2.s2.findings.yaml` (17 records, identical to the list above).
