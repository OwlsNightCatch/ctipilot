**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-19T06:30:07Z · ended_at=2026-11-19T06:55:25Z · duration_seconds=1518

## Verification report — 2026-11-19T0355Z-intel (iteration 3)

Scope walked: all 310 claims of `claims.iter3.yaml` (every claim of the 14 entries, which includes the 31 changed claims, every claim of the 11 entries remediated in iteration 2, and, rather than a random quarter, all claims of Drupal, OptimJack and HPE as well). Verdict rows: `verification.iter3.claims.yaml` (295 ok, 9 F3, 3 F4, 2 F5, 1 F13). Cited pages were read this pass from the gate's saved bodies plus fresh fetches (CVE JSON records, EPSS API, Tenable, Cisco, Fortinet, BACS, Calif raw HTML, Oracle, OpenJDK, Obsidian raw HTML, GHSA, NCSC.ch hub posts 12960/13196/13198/13203, NCSC-NL 0506/0507, CERT-Bund CSAF, HPE text advisory, nginx.org news, Drupal SA-CORE-2026-018 and PSA via WebFetch, CISA Java alert via WebFetch).

### Iteration 2 remediations (22 findings)

Fixed and verified correct: Confluence section and record summary ("naming neither Confluence nor N-able N-central" matches the alert row); Obsidian rotation list (provider keys, database credentials, MCP tokens as Obsidian words them; master and salt keys labelled as the entry's addition); nginx patched-versions sentence, summary score attribution (NCSC-NL all five, NCSC.ch and Rapid7 the HTTP/2 pair), per-CVE R-release ranges (R34 to R36; R33 for CVE-2026-113425) and ASLR/base-effect statement (CERT.at); Java4Shell Fortinet clause, BACS running-version point, update-section exploitation facts; Airlock citation dates and headline ("buffer overflow"); CyberPower "signed-looking" and script/implant names; Synology "only the SA-24:20 flaws"; Obsidian CNA wording and event_date; REDCap "and CNA" dropped; Idunno broader rotation labelled; PHP2Shell NetApp revision 13.0 (ONTAP 9.15.1P21 and 9.18.1P9 confirmed in the advisory data); product keys linked.

Fixed in part, residual found: the CyberPower krbtgt trigger (only `actions[0]` changed; the body takeaway and the Triage line keep the old trigger, finding F4 #1); the Confluence "no product named" wording (still in the `sourcing_note`, F3 #1); the tcherber headline (still names only "default logins", and the run record's remediation note says it names the mix, F13 #1).

### Claim does not support the claim (F3)

- #1 Confluence `sourcing_note`: "CISA added the CVE to its Known Exploited Vulnerabilities catalog on 2026-11-18 without naming a product or an actor." The CISA alert row reads "CVE-2026-90436 Apache Axis Unsafe Reflection Vulnerability". Residual of iteration 2 F3 #1.
- #2 (low confidence) CyberPower summary and body: "Symantec could not establish how the attacker reached the console". Symantec: "Any of these, or stolen administrator credentials, could give an attacker the necessary console access"; it never says it could not establish the route.
- #3 (low confidence) Java4Shell title, summary, body, section, record summary: "none confirmed successful". Tenable: "GreyNoise has not confirmed any successful exploitation against its sensors"; the scope is dropped.
- #4 (low confidence) Obsidian takeaway and action: rotation "on any instance that an untrusted user could reach on an older build ... as Obsidian advises". Obsidian: "Rotate provider API keys, database credentials, and any MCP tokens stored in the proxy if exposure is suspected."
- #5 (low confidence) nginx body: "NGINX Plus 37.3.0.1 and 37.0.8.1 fix the flaws" cited to CERT.at, which says the builds fix "alle vier Schwachstellen" and does not list CVE-2026-123634; no cited page names the Plus fixed builds for that flaw.

### Unsupported / hallucinated facts (F4)

- #1 CyberPower body Defender takeaway: "where the audit finds a deviation, assume Active Directory credentials are exposed and plan a krbtgt reset and wider credential rotation". Symantec: "Review the techniques and indicators in this document. If you find them, assume Active Directory credentials are exposed and plan a krbtgt reset"; its audit advice is "Treat any unknown scripts as hostile". Same entry, Triage line: "scripts that differ from the product defaults ... separate it from benign use", while the cited vendor page lists "External Command Scripts ... user-programmable command executions" as a normal feature; actions[0] calls "children of ppbed.exe that are not shutdown or notification routines with no preceding power event" a technique "Symantec lists" (it is the entry's own filter). Residual of iteration 2 F4 #3.

### Claims missing inline citation (F5)

- #1 (low confidence) Airlock first body sentence: "the Ergon web application firewall and API gateway vendor"; the headline's "WAF" rests on it. No cited page carries either term.
- #2 (low confidence) Idunno `sourcing_note`: the CVE record's CISA assessment ("Exploitation none", 2026-11-19T01:39:42Z) is true when fetched (CVE API) but is not a listed source.
- #3 (low confidence) Obsidian Detection line: no citation, no inference label.

### Needs more research (F8)

- #1 nginx `cves[CVE-2026-121810]`: CERT.at lists R34 to R36 for all four flaws it covers (CVE-2026-121810 among them) and no update for R33 to R36; the record omits R34 to R36 while the HTTP/2 records now carry it.
- #2 (low confidence) PHP2Shell `cves[].affected` omits Deep Discovery Analyzer although `fixed`, `affected_products` and Exposure carry it; the advisory also says "Engine: Fixed via Active Update on Nov.6" for the Analyzer, which the entry never states.

### Surface contradiction (F9)

- #1 nginx `sourcing_note`: the R33 variance is attributed to CERT.at, but CERT.at lists R33 only for CVE-2026-113425. Wiz's table gives "CVE-2026-123633: R33; 37.0.0" and "CVE-2026-123007: R33; 37.0.0"; the entry records R34 to R36 for both and never names Wiz's R33.

### Analytical-link-as-fact (F13)

- #1 (low confidence) tcherber headline "Cyderes: 'tcherber' broker toolkit for FortiGate and SonicWall VPNs, default logins, then an LDAP sweep". Cyderes: "Contains a mix of default credentials (guest:guest, admin:admin, test:test) and organization-specific passwords, indicating both brute-force harvesting and credential dump sourcing"; nothing ties the toolkit's logins or the tunnels to the default accounts. The run record's remediation note for this finding ("the headline names the credential file's mix") does not match the headline.

### Org-triage / priority (F16)

- #1 (low confidence) Drupal `priority: high`. The entry says Drupal rates the one critical flaw exploitable only in uncommon module configurations (TD:Uncommon, installer not secured or removed), no source reports exploitation and the second advisory is not directly exploitable: the high-bar disqualifier for an unexploited flaw reachable only in a non-default configuration. Counterweights: the Security Team's "exploits might be developed within hours or days" and Drupal's footprint in Swiss public-sector hosting; say which carries it.

### Action-item discipline (F18)

- #1 (low confidence) Idunno `actions[0]`: four tasks in one line, restates the Detection IIS-log hunt, and ends in the hedged "treating an internet-reachable server that ran the module as a candidate for the same rotation as a precaution".

### Editorial / less-is-more flags (advisory, F11)

- #1 Java4Shell update section and record summary: "which replaces the entry's earlier statement that no source reports attacks" and "so the entry no longer says no source reports attacks" are record-keeping narration in reader-facing text.
- #2 (low confidence) REDCap summary "Unit 42 saw it exploited from 2026-10-07" (the note is dated 2026-10-07 and gives no start date) and `event_date` 2026-11-18 versus the primary source's 2026-09-27.

### Checked and clean (for the record)

Changelog contract on all eight updated entries: `entry_record.py diff` field lists match the declared `fields`; `updated_at` mirrors the non-internal `update` record `at`; every section has its record; no silent edit found. cves[] cross-check: HPE (all 19 ids and scores against the revision 2 CSAF, 76 vulnerabilities, 33 at 3.1 9.0 or above), EPSS values (CVE-2026-90436 0.01128, CVE-2024-10441 0.01251, CVE-2026-40217 0.1702), LiteLLM CVE records (VulnCheck 8.8/8.7, MITRE 8.8 for CVE-2026-40217), Drupal SA-CORE-2026-017/018 fields. Evidence quotes spot-read against pages (nginx CERT-EU/Xint/Rapid7/Wiz, Mandiant, Symantec, Cyderes, BACS original/translation, Drupal SA-018). Style scan over all 14 entries: no em dash in reader-facing fields, no hash/IP/domain indicator, no workflow vocabulary beyond the F11 narration above. ATT&CK pin: T1574.002 revoked by T1574.001 (mapping stands). Dedup: no new entry duplicates a 14-day record; REDCap, nginx link their earlier entries in `references[]`.

### Missed angles (F10)

None named. The KEV window (four additions) is fully dispositioned; a search for a 2026-11-18 exploited edge disclosure surfaced nothing dated in the window beyond what the store carries (SonicWall SonicOS 2026-11-06 predates it). Coverage looks complete for the window; the Basel-Landschaft incident stays a held backlog row with a named condition.

### Verdict

NEEDS_FIXES (truth: 7, editorial: 8, advisory: 2)

The two findings with firm evidence are the CyberPower krbtgt/Triage residual (F4 #1) and the Confluence sourcing_note residual (F3 #1). The rest carry `(low confidence)` and are cheap to settle by rewording.

### Findings summary (machine-readable)

See `work/2026-11-19T0355Z-intel/verification.iter3.findings.yaml` (17 records).
