**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-12T03:25:48Z · ended_at=2026-10-12T03:32:23Z · duration_seconds=395

## Verification report — 2026-10-12T0256Z-intel (iteration 1)

Scope: 1 new entry (`2026-10-12/cve-2026-85097-bricksforge-pro-forms-upload-php-exploited`), 0 updates, the run record. All 31 ledger claims have a verdict row in `verification.iter1.claims.yaml` (26 ok, 3 F3, 2 F5). Pages fetched fresh this iteration: Patchstack article, Bricksforge changelog, Dr. Web article, CVE Program record (cveawg), FIRST EPSS, Patchstack DB page, CISA KEV catalogue (2026.10.08), MSRC 2026-Oct CVRF, Patchstack RSS feed, GitHub search/contents API (read only), Previdian, TheHackerWire, TechJack.

Checked and clean: all three source dates (Patchstack 2026-10-08T11:28:37, Dr. Web 2026-10-09, changelog 4.0.1 section "8. October 2026"); all four evidence quotes verbatim (incl. the two German originals and faithful translations); CVSS 9.8 and CNA Wordfence on the CVE record; EPSS 0.0031 (FIRST 0.00312, 2026-10-11); not in KEV; techniques T1190 / T1505.003 / T1036.008 valid in the pinned ATT&CK 19.2; Patchstack reliability B matches sources.json; no store overlap (CVE or Bricksforge) in prior coverage or cves_seen; no em dash, no IOCs (the login_admin_* file-name pattern and source IPs were correctly left out); run-record counts (7 items, 81 rotation records, window 26 h, duration) and the MSRC early-October claim (0 Exploited/Publicly Disclosed flags in 312 CVRF records) hold.

### Citation does not support the claim
- #1 F3 (low confidence), claims fd64e94e9d / 100d6ea5cb: "Wordfence, the CVE's assigner, scores it 9.8 and Patchstack 10.0 ([Dr. Web])". Dr. Web: "CVSS 3.1: 9,8, vergeben von Wordfence; Patchstack vergibt 10,0" - no statement that Wordfence is the CVE's assigner. True per the CVE record (assignerShortName Wordfence) but that page is not citable. Rephrase to "Dr. Web credits Wordfence with the 9.8 score" (also in `sourcing_note`).
- #2 F3 (low severity), claim dcda687793: Exposure clause "versions up to and including 3.1.8.9 ... ([Bricksforge, 2026-10-08])". The changelog says only "It affects every site with Pro Forms active, including sites whose forms use no upload fields"; the 3.1.8.9 bound is on Patchstack/Dr. Web. Cite Patchstack for the bound.

### Unsupported / hallucinated facts
- #4 F4 (low severity, run-record note): "The CISA enrichment on the CVE record lists exploitation as none, which pre-dates the Patchstack report by hours." CVE record CISA ADP SSVC timestamp is 2026-10-08T14:24:30Z; Patchstack datePublished 2026-10-08T11:28:37 (feed pubDate 11:28:37 GMT). The enrichment post-dates the article by about three hours. Fix the direction or drop the sentence.

### Claims missing inline citation
- #5 F5, claim 258f0526a2: "Versions up to and including 3.1.8.9 are affected." Add Patchstack (or Dr. Web).
- #6 F5, claim 24a502efff: "Patchstack's telemetry first recorded exploitation attempts on 2026-10-07 at 21:47 UTC, from 63 distinct source addresses; it calls the activity automated and does not attribute it." Add the Patchstack citation (all facts are on that page).

### Surface contradiction
- #7 F9: Exposure and `affected` bound the flaw at <= 3.1.8.9 (Patchstack, CVE record, Dr. Web) while the vendor ships the upload fix only in 4.0.1 ("affects every site with Pro Forms active"); the 4.0.0 changelog (2026-09-17) says only "Includes all hardening and fixes from the 3.x line", and 3.1.8.10 post-dates it. No source states whether 4.0.0 is affected, and a reader on the current major cannot tell. Add an uncertainty/Contradiction line. (A GitHub PoC docstring says "Fixed in 4.0.0", a third and unreliable reading.)

### Needs more research
- #8 F8: public exploit availability is absent from the entry. GitHub repository search for CVE-2026-85097 returns one repository (created 2026-10-10T04:51:32Z; description "Bricksforge <= 3.1.8.9 Unauthenticated Arbitrary File Upload") whose contents API lists README.md and poc.py (33,478 bytes). The script header documents the nonce, form_file_upload and form_submit chain and a "-i targets.txt -t 20" mass mode. S1's findings saw the repository and left it uninspected. Previdian (https://previdian.com/CVE-2026-85097) and TheHackerWire tag the CVE "PoC available". Add one sentence (cite Previdian rather than the repository) and consider `poc-public` in `cves[].status`. Read only, not run.
- #9 F8 (low confidence): TechJack Solutions (https://techjacksolutions.com/?p=94413, 2026-10-08) states "exploitation activity tracked by VulnCheck KEV". The VulnCheck page sits behind a login in this container and the run never queried the VulnCheck KEV index. If VulnCheck lists it independently, "telemetry alone" and `single-source` change; if it relays Patchstack, say so.
- #10 F8 (low confidence): Detection names `temporaryFileUploads` and the nonce action but not the route and action Patchstack gives (POST /wp-json/bricksforge/v1/form_submit; admin-ajax action bricksforge_form_submit); these are the plugin's own endpoints, not attacker indicators. Name them.

### Quantifier without source
- #3 F14 (low confidence): "none of the cited sources reports a confirmed compromise". Patchstack says "active exploitation attempts"; Dr. Web's lead says "Seit Mittwochnacht schleusen Angreifer ... eigenen PHP-Code auf fremde Server", readable as successful injection. Attribute the narrower statement to Patchstack or drop it.

### Action-item discipline
- #11 F18: actions[1] ("... search the access logs for the exploit request pattern and the uploads tree for PHP files, and restore from a backup older than 2026-10-07 and change all passwords if code turns up") restates the Detection line and the Defender takeaway (10b b). Keep actions[0] (inventory plus update), drop its fallback clause (deactivate / deny PHP execution, which restates the takeaway), and drop or fold actions[1].

### Editorial / less-is-more flags (advisory)
- #12 F11: the `**Triage:**` line is a detection signature already in Detection, not a benign-lookalike discriminator. Drop it.
- #13 F11: `sourcing_note` is three sentences and the last is a score discussion (already in the body). Cut to two sentences of provenance.
- #14 F11 (low confidence): run record `completed: '2026-10-12T03:50:00Z'` is later than the container clock (03:28Z) during verification; stamp the real time.

### Missed angles
None found. Spot searches for an exploited in-window flaw and a Swiss public-sector incident returned nothing new beyond the run's own dispositions; KEV has no addition since 2026-10-08. Coverage looks complete for what could be checked. The relevance of the entry (exploited pre-auth RCE with a vendor fix; no Swiss deployment shown; priority notable) is defensible under the run's gate and is not flagged.

### Verdict
NEEDS_FIXES (truth: 4, editorial: 7, advisory: 3)

### Findings summary (machine-readable)
See `work/2026-10-12T0256Z-intel/verification.iter1.findings.yaml` (14 records).
