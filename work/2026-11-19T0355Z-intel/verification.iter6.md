**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-19T07:42:45Z · ended_at=2026-11-19T08:01:00Z · duration_seconds=1095

## Verification report — 2026-11-19T0355Z-intel (iteration 6)

Scope walked: all 7 claims in claims.changed.iter6.yaml; every claim of the three remediated entries (nginx 24, Obsidian 23, OptimJack 25 = 72); a random quarter of the other 240 claims (60, `random.seed(20261119)`, spread over all 11 other entries: HPE 11, Synology 8, Java4Shell 8, PHP2Shell 5, Drupal 5, CyberPower 5, REDCap 5, Confluence 4, Airlock 4, tcherber 3, Idunno 2); the run record notes, frontmatter counts and iteration ledger. 132 rows in verification.iter6.claims.yaml, all `ok`. Unreadable: none (the Drupal SA-CORE-2026-018 and PSA pages answered a client challenge to `extract`; both were read through WebFetch with the outbound-links template and the sentences quoted below matched).

### Prior-iteration deltas (iteration 5 findings, each re-read at its source)

1. F3 Obsidian takeaway (v1.83.14-stable / endpoint block). Obsidian (fetched): "Upgrade to v1.83.14-stable or later. This is the first release that contains the complete fix set for all three CVEs." The LiteLLM GHSA (fetched, raw page): "If upgrading is not immediately possible, block `POST /guardrails/test_custom_code` at your reverse proxy or API gateway"; text says "Fixed in 1.83.11", Patched-versions field ">= 1.83.10", affected ">= 1.81.8, < 1.83.10", Moderate CVSS:4.0 5.9. The remediated clause cites Obsidian for the release and the advisory for the block. Correct.
2. F14 nginx first sentence. CERT-EU 2026-022: "F5 published an advisory addressing five vulnerabilities in NGINX that allow an unauthenticated remote attacker to execute code with the privileges of the NGINX worker process" and "All five vulnerabilities can lead to unauthenticated code execution". nginx.org lists ten advisories fixed in 1.31.9/1.30.7; the body now attributes the count to CERT-EU and cites nginx.org only for the publication of the fixes. Correct.
3. F4 Obsidian CVE-2026-47101 cvss. The Hacker News gives only "VulnCheck ... scores it 8.7 under CVSS 4.0, 8.8 under 3.1" for CVE-2026-47102; Obsidian scores only the chain (9.9). `cvss: "n/a"` plus the sourcing-note sentence "no listed source scores CVE-2026-47101 on its own" is accurate. Correct.
4. F9 nginx CVE-2026-113425 Plus range. CERT.at: "CVE-2026-113425: 37.1.0 bis 37.2.0 sowie 37.0.0 bis 37.0.7", "R33 (nur CVE-2026-113425)", "Fuer NGINX Plus R33 bis R36 sind derzeit keine Updates verfuegbar". The record reads "37.1.0 to 37.2.0, 37.0.0 to 37.0.7 and R33 to R36 per CERT.at" and fixed 37.3.0.1 / 37.0.8.1. Correct against the listed source.
5. F11 OptimJack Detection/action overlap. Detection now ends with the Hudson Rock account-history review plus "Zscaler advises customers to review recent changes, user activity, account creation events and administrative access"; action[1] carries the audit of Project JavaScript fields and the rotation, which Zscaler lists ("Audit all Project JavaScript fields ...", "Rotate API tokens, session tokens, and integration keys"). The two no longer repeat each other. Correct.

### Truth results

No F1-F5, F13-F15 finding. Highlights of what was re-read this pass:
- nginx: nginx.org (per-CVE vulnerable ranges 0.6.18, 1.9.5, 1.25.0, 1.19.7, 0.5.33 to 1.31.8; "Not vulnerable: 1.31.9+, 1.30.7+"), CERT-EU, CERT.at (Plus builds, R-releases, ASLR condition), NCSC.ch hub 13203 ("UNKNOWN, Proof-of-Concept Available"; CVSS4.0 9.2 for the two HTTP/2 CVEs), NCSC-NL (all five 9.2; "verwacht ... exploitatie op grote schaal"), Wiz (two HTTP/2 CVEs 9.2, "we will not be releasing these exploits"), Rapid7 (128 GB, worker permissions only, remediation table) and its PoC repository ("likely fail against ... multiple concurrent clients"), Xint (interim measures, SCTP chain, restart-not-reload, backport caveat). All clauses terminate on pages that carry them.
- Obsidian: THN, GHSA, Obsidian and the CISA alert (WebFetch-equivalent cached body, "based on evidence of active exploitation"; row "BerriAI LiteLLM Unprotected Alternate Channel Vulnerability") carry every cited clause; CNA records read only to check scores (CVE-2026-47102 lessThan 1.83.10, 8.7/8.8; CVE-2026-47101 lessThan 1.83.14), not cited.
- OptimJack: Optimizely status page (Nov 18 14:49 UTC post and Nov 17 01:02 UTC post), Zscaler, Report URI, Ohey, Hudson Rock and Amirul Cyber carry every figure (178 orgs, 188 snippets, 04:21/13:43/20:40-21:10 UTC, 450+ domains and 3,000+ URLs, 21 properties, Basel capture 2026-11-14 03:27, <5%).
- Sample: HPE CSAF parsed in full (76 CVEs; 33 at 9.0 or higher = 8x10.0, 10x9.8, 10x9.6, 1x9.4, 4x9.3; the 19 at 10.0/9.8/9.4 are AV:N/PR:N, the other 14 AV:A; revision 2 text and FIPS note), Synology SA-26:13 / SA-24:20 / 360 / heise / NCSC.ch 12960, Trend KA-0024802 and Download Center rows, NetApp advisory data (revision 13.0 adds 9.15.1P21 and 9.18.1P9; exploitation field "Public"), CISA KEV JSON (CVE-2026-109618/-109619 dateAdded 2026-10-26; four 2026-11-18 additions), CISA Java alert (WebFetch), NCSC.ch 13198, Talos, Upwind, BACS, Calif (raw HTML carries both JVM options and the ARM caveat), Drupal SA-017/SA-018/PSA (Critical 18/25 and Moderately critical 14/25 risk lines), Atlassian, Apache Axis thread, ENISA EUVD (Airlock, Idunno), Symantec, Mandiant MNDT-2026-0048, Unit 42 note, Securifera post, Cyderes.
- Gate: `check_run.py` reproduces 59 pass / 0 warn / 3 fail (the two residual-arithmetic lines and the run-clock line, all expected); the one quote not machine-checkable (SA-CORE-2026-018 "This issue is not directly exploitable.") matched on the WebFetch read.
- Run record notes: counts (6 new, 8 updated, 14 items, four KEV additions and their dispositions), the Confluence record typed `update`, Drupal priority notable, the HPE id replacement, the held backlog rows (present in state/coverage_backlog.md with conditions and expiries), the new source candidates (present in sources.json), the registered entity keys (all present in the registry) and the iteration counts (41, 22, 17, 16, 5; per-iteration truth/editorial/advisory sums match) hold on disk.

### Editorial results

Priorities hold: nginx high (internet-facing, public PoC for one flaw, no exploitation), REDCap high (exploited, KEV, mining with persistence), OptimJack high (supply chain with Swiss university nexus), Synology high (ransomware on outdated DSM), Java4Shell high, others notable; no critical. Classification blocks present and within vocabulary on all 14 entries; no `org_triage` content, no watchlist use; no IOCs, em dashes or pipeline vocabulary in reader-facing text (scan run on all 14 entries). Dedup: no new entry shares a CVE or subject with prior coverage (cves_seen and a text scan of the store), REDCap and nginx declare their earlier related entries in `references[]`. Coverage: the national-CERT feeds the run read (CERT-EU 2026-021/-022, CERT.at 18 Nov items) are all covered; the Basel-Landschaft cantonal incident is a documented HELD backlog row (no vector, actor or behaviour; techniques[] cannot be evidence-bound), not a missed item; two WebSearch sweeps for other in-window exploited items surfaced nothing new (Gitea CVE-2026-116289 dates from 2026-11-01 with no exploitation; Cisco SD-WAN CVE-2026-20245 is covered by the 2026-06-06 entry). Coverage looks complete.

### Editorial / less-is-more flags (advisory)

All five are low-confidence F11 items the main agent may leave:
1. Obsidian record summary ends "and the earlier description of the flaw was corrected." (narration; the section carries no such clause).
2. Obsidian `cves[CVE-2026-47102]`: `cvss: "8.8"` unscaled (body says 3.1); "per the VulnCheck record" names a record not in sources[] where Obsidian's timeline ("v1.83.10-stable shipped with the role escalation fix") supports it.
3. Obsidian body/Exposure "any authenticated user" for CVE-2026-47102; Obsidian: reachable directly by org_admin, by default internal_user only after CVE-2026-47101.
4. nginx: "[nginx.org, 2026-11-18]" cites a living listing with no dateline; sourcing_note does not disclose that the date comes from other sources.
5. Drupal update record `fields` names `priority`, which did not change against HEAD.

### Verdict

CLEAN (truth: 0, editorial: 0, advisory: 5). This is a first CLEAN after a NEEDS_FIXES iteration: an independent cold confirmation pass is still required before publish. The residual-arithmetic and run-clock gate lines clear in Phase 6.

### Findings summary (machine-readable)

See verification.iter6.findings.yaml (five F11 advisory records).
