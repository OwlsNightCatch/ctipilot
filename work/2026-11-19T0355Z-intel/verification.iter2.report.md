**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-19T06:03:37Z · ended_at=2026-11-19T06:27:28Z · duration_seconds=1431

## Verification report — 2026-11-19T0355Z-intel (iteration 2)

Role: post-fix pass after iteration 1's NEEDS_FIXES. Scope: all 308 ledger claims (the 49 changed, every claim of the entries iteration 1 remediated, and the rest, because every entry except the PHP2Shell record was touched). Every cited page was read this pass (gate-saved bodies, `extract`, `url`, `ncsc-csh`, CSAF/CVE-record JSON, CISA alert via WebFetch with the outbound-links template). Claim rows: `work/2026-11-19T0355Z-intel/verification.iter2.claims.yaml` (289 ok, 19 non-ok). 22 findings: 14 truth, 4 editorial, 4 advisory.

### Iteration-1 remediations walked

- Fixed and confirmed against the source: Obsidian date 2026-06-11 and the VulnCheck 8.8 clause on The Hacker News; CERT-Bund critical plus revision-2 "Exploit aufgenommen" (read from the CSAF twin); REDCap Detection split between Unit 42 and Securifera; nginx CVSS attribution; Java4Shell exploitation attempts and VulnCheck exploit (Tenable: "As of November 18, GreyNoise has reported exploitation attempts ... has not confirmed any successful exploitation"); Idunno rotation condition; tcherber 30-second loop and VMRay wording; Drupal "neither advisory reports exploitation"; Obsidian CVE-2026-47102 range (VulnCheck record: lessThan 1.83.10); HPE CSAF scoping and FIPS note; Synology December-versus-November note; Confluence retype to `update` with a moved `updated_at`.
- Declined, rebuttal accepted: `T1574.001` for the DLL side-load (pinned ATT&CK v20.1 has `T1574.002` revoked, `revoked_by` `T1574.001`); `8u513-perf` as a fixed build (the cited Tenable page's patch table lists "8u511b33-perf | 8u513-perf"); Xint's SCTP chain (now stated in the nginx entry with its module-block mitigation); no `T1110` for tcherber (both statements are attributed readings, not observed behaviour); the Basel-Landschaft incident held on the backlog (a confirmed cantonal incident, but no source gives a vector, actor, data or behaviour, so it is `routine` under the actionability rules and has no evidence-bound technique; named hold condition and expiry; same ground as the Beyond Gravity precedent).
- Fixed in part, residual found: Airlock "heap" (title and summary fixed, headline still says it, finding F4 #1); CyberPower krbtgt trigger (F4 #3); nginx ASLR prerequisite (the remediation's "cannot be cited" is wrong, CERT.at states it, F8 #2); CyberPower file-name indicators (script names remain, F11).

### Citation does not support the claim

F3 #1. Confluence update section and record summary: "naming no product and no actor" / "(no product named)". The CISA alert row reads "CVE-2026-90436 Apache Axis Unsafe Reflection Vulnerability". Say it names neither Confluence nor N-able N-central.
F3 #2. Obsidian Defender takeaway: "rotate the master key, the salt key and every provider API key ... as Obsidian advises". Obsidian: "Rotate provider API keys, database credentials, and any MCP tokens stored in the proxy if exposure is suspected." No master or salt key, and the entry drops database credentials and MCP tokens. THN repeats the Obsidian list.
F3 #3 (low confidence). nginx: "37.2.0.1 and 37.0.7.1 fix only CVE-2026-123633" cited to CERT.at, which says they already fix CVE-2026-123633 and remain affected by CVE-2026-123007 and CVE-2026-121810; "only" is not stated, and CERT.at's CVE-2026-113425 range excludes those builds.
F3 #4 (low confidence). nginx summary: "NCSC.ch, NCSC-NL and Rapid7 score them CVSS 4.0 9.2". NCSC.ch's post scores two CVEs, Rapid7 one; only NCSC-NL lists all five.
F3 #5 (low confidence). Java4Shell: "the other products it names as under investigation". Fortinet lists 22 further products as "confirmed NOT Impacted" and 51 under investigation.
F3 #6 (low confidence). Java4Shell: "the running build, not the installed package, decides" cited to NCSC.ch, which only says "Record the Java distribution, exact running build ...".
F3 #7 (low confidence). Airlock: documentation citations dated 2026-11-18 while the note says they carry the retrieval date (2026-11-19).

### Unsupported / hallucinated facts

F4 #1. Airlock headline "Smart Form Protection heap overflow": the ENISA record says "buffer overflow" only; "heap" is in no cited page.
F4 #2. nginx `cves[]`: NGINX Plus "R33 to R36" on CVE-2026-123007 and CVE-2026-123633. Rapid7 "R34 - R36 | None", CERT-EU "R34, R35 and R36", CERT.at "R34 bis R36 (alle vier)" and "R33 (nur CVE-2026-113425)". R33 missing on CVE-2026-113425; no cited per-CVE Plus range for CVE-2026-123634.
F4 #3. CyberPower action and Defender takeaway: a script that "differs from the product defaults" triggers a krbtgt reset. Symantec ties the reset to finding the techniques and indicators; unknown scripts are "treat as hostile and review". A legitimate user-programmed event-action script also differs from defaults.
F4 #4 (low confidence). CyberPower: "a signed-looking binary". Symantec: "an old, trusted executable"; nothing about signing.
F4 #5 (low confidence). Synology action: the SA-24:20 builds "close only CVE-2024-10441"; SA-24:20 fixes three CVEs.
F4 #6 (low confidence). Obsidian sourcing_note: "the CNA record held by VulnCheck" for CVE-2026-40217; the record's `assignerShortName` is `mitre`.

### Claims missing inline citation

F5 #1 (low confidence). REDCap: "Securifera ... is its CNA" is on no cited page (the CVE record says so; it is not cited).
F5 #2 (low confidence). Idunno action: "because request bodies are rarely logged" has no source.

### Needs more research

F8 #1. PHP2Shell (updated 2026-11-19): NetApp's advisory data is at revision 13.0 of 2026-11-18, "ONTAP 9.15.1P21 and ONTAP 9.18.1P9 added to Software Versions and Fixes". The entry stops at revision 12.0 ("final"), so `cves[].fixed` and the body lack two fixed builds.
F8 #2. nginx: vendor framing missing although citable. CERT.at: crash of worker processes, and code execution "when ASLR is deactivated or can be bypassed, according to F5"; nginx.org change log for CVE-2026-123007: "might allow an attacker to cause a segmentation fault in a worker process, or might have potential other impact". The headline states only the demonstrated ceiling.

### Editorial / less-is-more flags (advisory)

F11 #1. Java4Shell update section and record summary omit the GreyNoise and VulnCheck delta that drove the new title and headline.
F11 #2. CyberPower: attacker script names (`pp?????.cmd` pattern, `ifm.cmd` to `ifm4.cmd`) remain as file-name indicators.
F11 #3. Registered product keys not linked (CyberPower product, three Cisco products, Deep Discovery Analyzer).
F11 #4. Obsidian `event_date` 2026-06-15 against the primary's 2026-06-11.

### Analytical-link-as-fact

F13 #1 (low confidence). tcherber headline "tunnels into FortiGate and SonicWall VPNs with default logins": Cyderes gives a credential file with a mix of default and organisation-specific passwords and logs of tunnels (FortiGate only); no source ties the tunnels to default logins.

### Whole-run checks

- Relevance and priority: nginx, REDCap, Java4Shell and Drupal at `high` clear the bar (constituency-wide products, public PoC or KEV, patch inside seven days); Airlock `notable` is right (Smart Form Protection is not default, attack complexity high); Idunno, CyberPower and tcherber `notable` are defensible. No `critical`. Classification present and in vocabulary on all 14 entries; reliability letters match `sources.json` tiers (ENISA EUVD, nginx.org, HPE, Drupal, Synology A; Unit 42, Symantec, Cyderes, Mandiant B).
- Style: no em dash outside the changelog heading, no IOC, no workflow vocabulary in reader-facing fields (the two `spawn`/`product:` regex hits are ordinary words).
- Coverage: the four CISA additions of 2026-11-18 are all on an entry or record; the three NCSC.ch hub posts inside the window (13196, 13198, 13203) are all covered; the Roundcube 1.6.21/1.7.6 drop is outside the window (2026-11-09). I found no relevant in-window gap beyond the Basel-Landschaft hold judged above. Coverage looks complete.
- Run record: the verification notes match the files on disk (six new entries, eight updated, the backlog rows and the borderline-drop list). The gate's only FAILs are the residual arithmetic that iteration 1 causes.

### Verdict

NEEDS_FIXES (truth: 14, editorial: 4, advisory: 4)

### Findings summary (machine-readable)

See `work/2026-11-19T0355Z-intel/verification.iter2.findings.yaml` (22 records, same content).
