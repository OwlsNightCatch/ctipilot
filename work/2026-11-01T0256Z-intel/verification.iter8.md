**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-01T06:08:14Z · ended_at=2026-11-01T06:24:07Z · duration_seconds=953

## Verification report — 2026-11-01T0256Z-intel (iteration 8)

Scope: all 149 claims of claims.iter8.yaml (the 7 changed claims, every claim of the six entries, so the full ledger); frontmatter title, headline, sources[] record dates and evidence quotes of each entry; run-record notes. Verdict rows: verification.iter8.claims.yaml (147 ok, 1 F3, 1 F4). Cited pages were read from the gate's saved bodies where they exist and re-fetched this iteration for the drifting ones (PAN-OS advisory HTML and JSON, Dream Research, Unit 42, CISA KEV, GreyNoise raw HTML and extract, Hunt.io, incident tracker, GitLab page and Atom feed, Python feed, Le Temps, vd.ch, RTS, watchTowr).

### Iteration-7 remediations (all confirmed)
- PAN-OS title now says "every release below its train's hotfix": matches the advisory table (every build below a train's hotfix affected, hotfix and later unaffected; twenty hotfix builds listed).
- Hunt.io: record dated 2026-10-28 (page metadata date), publisher label says revised 2026-10-30, inline citations dated 2026-10-28, run-record Recency bullet agrees.
- PAN-OS Threat Prevention clause restored with the Threat IDs and the four conditions (decrypted dataplane interface, replaced certificate, threat prevention enabled): conditions match the advisory; the ID range notation introduces finding #1 below.
- PHP actions[2]: "wireless controllers" removed.
- ARTEX section and record summary carry "somewhat-incremental" and "likely intended".
- eMudhra headline now "Windows drops seven certificates": matches MSRC ("removes seven certificates ... six eMudhra G3 roots and an AAA Certificate Services cross-sign").

### Citation does not support the claim
- F3 #1 (low confidence): eMudhra, "A Java runtime already updated on 2026-10-21 needs the update of 2026-10-24 as well" cited to https://openjdk.org/emudhra, which is dated 2026-10-24 and says only "even if you have updated your runtime in the past few days". The 2026-10-21 date sits on Oracle's alert and OpenJDK advisory 2026/10/21. Cite those on this clause.

### Unsupported / hallucinated facts
- F4 #2: PAN-OS entry, "Threat IDs 543004, 97622 to 97625 and 97643 to 97678". The advisory (HTML and JSON, read this iteration) lists 543004, 97622 to 97625 (contiguous) and twenty non-contiguous IDs inside 97643 to 97678 (97643, 97647, 97649, 97652, 97653, 97656 to 97659, 97662 to 97664, 97670 to 97674, 97676 to 97678). The range asserts sixteen IDs the advisory does not list. The entry's 2026-10-24 section words it correctly ("twenty further Threat IDs, from 97643 to 97678").

### Surface contradiction
- F9 #3 (low confidence): PHP main entry says "The first documented code execution is a honeypot report by Adel Karimi ... dated 2026-10-24" while its new Update cites Hunt.io, which names watchTowr among the networks that confirmed shells and dates watchTowr's honeypot exploitation to 2026-10-21 ("the earliest of the three"). SecurityWeek supports "first" as of 2026-10-26; watchTowr's own page says "Exploitation has been observed" without saying code ran. Add a Contradiction clause or reword.

### Editorial / less-is-more flags (advisory)
- F11 #4 (low confidence): PAN-OS summary dates the exploitation statement to "advisory of 2026-10-21"; that wording appeared after 2026-10-27 17:10 UTC.
- F11 #5 (low confidence, carried and declined): ARTEX Kerberoasting and DCSync described by GTIG (raw HTML lifecycle table) with no technique id.
- F11 #6 (low confidence, carried and declined): ARTEX onset (Microsoft September, GTIG August for the overlapping campaign) not reconciled in a clause.

### Checks with no finding
- New Vaud entry: every fact matches vd.ch and RTS; both evidence quotes and their `original:` text are verbatim and the translations faithful; sourcing_note claim that SRF and Le Temps relay the release holds (Le Temps/ATS article read; SRF body saved); `single-source-victim`, classification A/2 (vd.ch is reliability A in sources.json, RTS and SRF relay), routine priority, no actions, no IOC, no em dash, registry key present, no prior coverage of the incident.
- Changelog contract: each updated entry's last record carries this run's id; `updated_at` equals `at` for the four non-internal updates and is untouched for the Fragnesia improvement; every changed frontmatter line in `git diff` is named in the record's `fields`; each section heading matches its record `at`; record summaries state what the sections state; main analyses carry no statement the newest sections disprove (the Fragnesia and PHP sections say the earlier "unnamed vendor" text is superseded).
- GreyNoise: the page now reads "Last updated 01 November 2026, 05:48 UTC" while the entry (and the saved copy) say 03:48 UTC; the stable statements (1,177 confirmed exploitations from 5 attacker IPs, definition, first shell 2026-10-28 05:14:01, 10-29 reverse shell, mkdir /var/www/.ssh, metadata queries, linPEAS and gitleaks downloads, 10-31 gitleaks runs over /var/www/html, /etc, /opt) still match.
- PAN-OS cves[]: every fixed build, CVSS-B 9.2 / 7.7, the unaffected WF-500 correction and KEV status match the advisory, the JSON timeline and the KEV catalog (version 2026.10.30 lists both PHP flaws added 2026-10-26 and CVE-2026-46300 added 2026-10-28 with the chaining note).
- Run record: counts (1 published, 5 updated), Hunt.io dates, the Contradiction line (Hunt.io "one uniform PHP 8.0.30 build" against Dream's PHP 7.4.33 for 11.1), the iteration-1 count (23 findings, matching verification.iter1.findings.yaml), KEV-sweep statement and the Cisco 2026-11-04 carry-forward are consistent with the files and sources read.
- Missed angles: none found. The window is a weekend; the open threads (Publica / PK Softech, Camping.Care, Drupal Commerce, ARX) were re-checked by the slices with no newer development.

### Verdict
NEEDS_FIXES (truth: 2, editorial: 1, advisory: 3)

### Findings summary (machine-readable)
See work/2026-11-01T0256Z-intel/verification.iter8.findings.yaml
