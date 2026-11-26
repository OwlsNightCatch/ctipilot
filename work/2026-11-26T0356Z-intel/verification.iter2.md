**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-26T05:43:01Z · ended_at=2026-11-26T06:05:20Z · duration_seconds=1339

## Verification report — 2026-11-26T0356Z-intel (iteration 2)

Scope: post-fix pass. All 207 ledger claims have a verdict row in `verification.iter2.claims.yaml` (the 32 changed claims, every claim of the entries remediated in the deltas, and the remaining claims of Mitel, nginx2root, PolinRider and ARTEX; 197 ok, 6 F3, 3 F4, 1 F14). Passages in the claims file were machine-checked as substrings of the pages fetched this iteration; CISA alert pages were read with WebFetch (listing lines quoted), the three Drupal advisories with WebFetch (paraphrase flagged in the rows). Fetched this iteration: Okta blog and acquisition release, 1Password post and BleepingComputer, SEPPmail revision history and ENISA EUVD (no record for CVE-2026-130637), CISA KEV json, EUVD-2026-112215/112212/130382, BSI CSAF WID-SEC-W-2026-4234, FIRST EPSS, Danfoss DSA-2023-08-01/2025-03-01/2025-08-01, EUVD CNA records for CVE-2025-41450/41451/41452, Claroty Team82, ICSA-26-328-03 CSAF, Synacktiv PDF, watchTowr FAQ, The Hacker News, NCSC.ch 13242, Eye Security, GHSA-wc3v/39mw, Drupal SA-CORE-2026-017/018/019, StepSecurity x2, Searchlight, Fortinet FG-IR-26-278, Cisco Java4Shell and nginx advisories, HPE HPESBNW05193, Mitel MISA-2026-0012, Microsoft ARTEX guide and NK report, The Record, Nextgov, Macau Business, GTIG, SafeDep, Unit 42, PAN CVE-2026-123633, CERT.at, Wiz-linked nginx pages (Xint, NCSC-NL). Run record and registry diff read; two WebSearches for in-window gaps found nothing new.

### Prior-iteration deltas

Walked all 27 items against the pages above. Confirmed correct: Danfoss ICSA-26-328-03 wording (single CVE-2026-129713, CVSS 3.1 9.8, boilerplate quoted accurately) in section and record summary (#1); Claroty vector now user-interaction with the CNA UI:R/AC:H explained (#2), Danfoss 8.7 and 6.8 with both scores cited (#3); GeoServer 129245 now exploited (#4, see finding on the remaining subset); SEPPmail sourcing note (#5); Juniper BSI 23:00 UTC stamp and title/summary wording (#6), EUVD-2026-112212 date (#7); Okta wording and the Permiso acquisition source (#8, #9, #14); 1Password takeaway citation (#10, see finding on 'limited to'), four-item advice list (#11), reliability B (#20); Drupal neither-observed wording (#12, #16); Java4Shell Fortinet wording (#13) and update typing (#26); Juniper action (#15) and priority high (#19); ARTEX Nextgov paragraph stays within the pages (#17); Claroty action (#21); GeoServer and Drupal actions (#22); Okta sourcing note (#23); em dashes in Claroty (#24); Danfoss 2023 wording (#27). Item #25 (alias note in the run record) does not hold on disk: see the F11 finding.

### Citation does not support the claim

1. (#1, F3) **2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce** — `body`
   - Claim: CVE-2025-41450 ... bypasses normal login and discloses a web report with internal IPs, usernames and store names, as Claroty puts it: "the application accepts a specially crafted authentication request containing a generated 'code of the day'" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers))
   - Evidence / fix: The cited Claroty page never mentions a web report, internal IPs, usernames or store names (grep for "report", "internal IP", "usernames", "store names" finds only "privately reported"); that clause is Danfoss DSA-2025-03-01 / the CISA KEV description, not Claroty. Claroty says instead: "Successful authentication through this hidden mechanism results in a fully authenticated administrative session, granting privileged access to the device's web management interface." Fix: cite DSA-2025-03-01 or the KEV record for the report clause and state Claroty's own description of the impact.

2. (#2, F3) **2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce** — `body-update-section`
   - Claim: Cisco's advisory is at version 1.4 of 2026-11-23: ... ([Cisco, 2026-11-20](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nov2026-java-rce-eCa6ss9z)); also main analysis "Cisco's advisory (version 1.4) ... ([Cisco, 2026-11-20]"
   - Evidence / fix: (low confidence) The cited page is first published 2026-11-18 and last updated 2026-11-23 (revision table: 1.4 2026-NOV-23, 1.3 2026-NOV-20, 1.0 2026-NOV-18). The citation label 2026-11-20 is the version 1.3 date, two days off the first publication and three off the version-1.4 text it terminates, and contradicts "version 1.4 of 2026-11-23" in the same sentence. sources[] carries the same 2026-11-20.

3. (#3, F3) **2026-11-19/nginx-nginx2root-five-unauth-memory-corruption-flaws** — `update-section`
   - Claim: Palo Alto Networks released 12.1.7-h15, 11.2.10-h19 and 11.2.13-h6 on 2026-11-24
   - Evidence / fix: (low confidence) The PAN timeline says only "2026-11-24 Removed ETA for 12.1.7-h15, 11.2.10-h19, 11.2.13-h6 as these versions are released"; the earlier ETA was 2026-11-23, so the release date is not stated and may precede 2026-11-24. Say the ETA was removed on 2026-11-24 or drop the date.

4. (#4, F3) **2026-11-26/juniper-session-smart-cve-2026-103406-unauth-root-rce** — `body-and-sources`
   - Claim: ([ENISA EUVD, 2026-11-25](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-112215)) and sources[] date 2026-11-25 for EUVD-2026-112215
   - Evidence / fix: (low confidence) The record carries "datePublished":"Oct 28, 2026" and "dateUpdated":"Nov 25, 2026"; the clauses it terminates (description, CVSS 3.1 9.8, affected ranges) date from 2026-10-28. The sibling record EUVD-2026-112212 was re-dated to its datePublished in the fix pass, so the two citations in one entry now follow different conventions.

### Unsupported / hallucinated facts

5. (#5, F4) **2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce** — `frontmatter`
   - Claim: cves[CVE-2025-41451].vector and cves[CVE-2025-41452].vector: zero-click
   - Evidence / fix: (low confidence) The run set CVE-2025-41450 to user-interaction because its CNA record carries UI:R, but left the two sibling CVEs at zero-click although their CNA records (EUVD-2025-25499, EUVD-2025-25498) carry CVSS:4.0/.../PR:H/UI:A. The sourcing_note explains only the 41450 choice. Apply one rule to all three or explain.

6. (#6, F4) **2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce** — `body`
   - Claim: **Triage:** monitor authentication attempts ... for requests carrying a non-standard authentication parameter shape (a "code" field distinct from the normal username/password flow): legitimate operator logins never use the code-of-the-day mechanism, so its presence in a request is itself the discriminator.
   - Evidence / fix: (low confidence) Claroty describes "two request attributes (redacted)" set to 1 plus "a precomputed password" in the normal getauth request, not a separate "code" field, and calls the mechanism "likely intended for vendor support or maintenance", so a vendor-support login is a possible benign lookalike. The discriminator as worded does not follow from the cited mechanism.

7. (#7, F4) **2026-11-25/geoserver-five-step-unauthenticated-rce-chain-public-poc** — `frontmatter`
   - Claim: cves[]: exploited on CVE-2026-129243, CVE-2026-120705, CVE-2026-129245; CVE-2026-129244 and CVE-2026-129242 without it
   - Evidence / fix: (low confidence) The fix rationale says every CVE any source names as exploited carries the status, but the update section itself states "watchTowr's prose names all five chain CVEs" and the watchTowr FAQ prose reads "CVE-2026-129245, CVE-2026-129242, CVE-2026-129243, CVE-2026-129244, and CVE-2026-120705 is being exploited in the wild". The status set follows THN for 129243 and the table for 129245 but not the prose for 129244 and 129242. Mark all five (body already shows the disagreement) or state the rule in the sourcing note.

8. (#8, F4) **runs/2026-11-26/2026-11-26T0356Z-intel.md** — `run-record-notes`
   - Claim: "One `improvement`: Java4Shell (HPE bulletin, Cisco version 1.4)."; "Recorded for the audit: the Claroty entry carries CVSS 7.6 and 5.4 ... and CVE-2025-41450's vector shows UI:R and AC:H in the CNA record against the entry's zero-click"; "Danfoss 2023 flaws (Danfoss states no authentication requirement ...)"; "Drupal CVSS (The Hacker News 9.8 without a source, none exists)" listed under contradictions carried in entries
   - Evidence / fix: Stale after the fix pass. The Java4Shell record is now type update; the Claroty frontmatter now carries 8.7 and 6.8 and vector user-interaction; the Danfoss section now says the advisory "does not state whether authentication is needed"; the Drupal sourcing_note no longer carries the Hacker News CVSS sentence. Update the notes to the shipped state.

### Claims missing inline citation

9. (#9, F5) **2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce** — `body`
   - Claim: "; patched in firmware build 4.2." and "Danfoss shipped firmware R4.3.1 fixing CVE-2025-41451/41452 (build 4.2 for CVE-2025-41450)."
   - Evidence / fix: (low confidence) No inline citation; the Claroty page says only "released firmware version R4.3.1, which addresses the vulnerabilities described in this research" and does not mention build 4.2. Build 4.2 is in Danfoss DSA-2025-03-01, cited only in the update section.

### Surface contradiction

10. (#10, F9) **2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce** — `body`
   - Claim: The RCE and Nginx-injection primitives require prior authentication; Claroty's article does not explicitly confirm the code-of-the-day mechanism as a pre-auth path into the two post-auth primitives, so the chain is treated as auth-gated unless a combined path is independently confirmed.
   - Evidence / fix: Claroty (primary): "Successful authentication through this hidden mechanism results in a fully authenticated administrative session", "we gained access to the device's full administrative interface and every management function it exposed", and the findings "combine to create powerful attack chains against internet-accessible cyber-physical systems". Danfoss DSA-2025-03-01 and CISA KEV (cited) describe the same flaw as a web-report disclosure. The entry takes the Danfoss/CISA impact in summary and body and the auth-gated reading without a Contradiction line naming Claroty's different impact statement. Add the contradiction and revisit the chain wording.

11. (#11, F9) **2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse** — `update-section`
   - Claim: the commercial edition is therefore the vendor's own product, not a community fork (and the 2026-11-01 section no longer says "among them a commercial one")
   - Evidence / fix: (low confidence) GTIG, cited in that section, writes "the framework continues to proliferate globally via community forks, including localized variations such as ScopeWeaver and a commercial version dubbed ARTEX PRO". The run removed GTIG's clause and states the opposite from ThreatBook's release and Microsoft without attributing the disagreement to GTIG. The run record lists only Microsoft vs ThreatBook as the contradiction.

### Editorial / less-is-more flags (advisory)

12. (#12, F11) **2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack; 2026-11-26/seppmail-15-1-2-gina-template-injection-account-takeover** — `body`
   - Claim: "the report-generating authentication bypass that the Claroty entry from August covers"; "The earlier 15.1.1 fixes are covered separately."
   - Evidence / fix: Store cross-references without a link in reader-facing text, raised in iteration 1 and not changed (the fix pass handled only the Okta sentence). Drop them or link the entry; both entries already carry the other in references[] where applicable.

13. (#13, F11) **2026-11-26/okta-ai-agents-mail-tm-disposable-signups-blocklist-decay** — `frontmatter`
   - Claim: title: "... whose single rotating mailbox domain makes blocklists stop matching within weeks"; headline: "one rotating domain defeats blocklists within weeks"; summary: "so a blocklist stops matching within weeks"
   - Evidence / fix: Okta writes "a blocklist built from previously observed domains will very likely stop matching within weeks of being compiled"; the body keeps "very likely", the title, headline and summary state it as fact.

14. (#14, F11) **runs/2026-11-26/2026-11-26T0356Z-intel.md** — `run-record-notes`
   - Claim: iteration-2 deltas item 25: "registered as separate keys ... noted in the run record for the audit" (Onyx Sleet/Andariel, Salt Typhoon/FamousSparrow)
   - Evidence / fix: The run record contains no mention of Andariel, FamousSparrow or GhostEmperor (grep finds none); registry actor:andariel and actor:famoussparrow remain unlinked to actor:onyx-sleet and actor:salt-typhoon. Add the note the fix pass says exists.

### Quantifier without source

15. (#15, F14) **2026-11-26/1password-employee-github-account-backend-compromise** — `body`
   - Claim: **Defender takeaway:** 1Password's own advice is limited to phishing caution and reporting suspicious messages
   - Evidence / fix: (low confidence) The post's "What you can do" has four items: phishing caution; "1Password will never contact you to ask for your account password or Secret Key"; "Keep your Secret Key and account password safe."; "If you see something suspicious, tell us at support@1password.com." "Limited to" two of them is the same restrictive quantifier iteration 1 flagged as "only"; the body paragraph lists all four correctly.

### Org-triage line missing / inconsistent

16. (#16, F16) **2026-11-26/seppmail-15-1-2-gina-template-injection-account-takeover** — `frontmatter`
   - Claim: priority: notable ... "treat the template injection and the unauthenticated reset as the reason to move this update ahead of the regular cycle"
   - Evidence / fix: (low confidence) A Swiss vendor's gateway (regions: switzerland, europe) with a vendor-scored 9.3 unauthenticated account takeover and an unauthenticated reset; the entry's own takeaway urges an out-of-cycle update where GINA is internet-facing, which is the high bar's decision. Notable implies the regular cycle. No exploitation or PoC is stated, so notable is defensible; align the takeaway or the priority.

17. (#17, F16) **2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce** — `frontmatter`
   - Claim: priority: notable (update typed: CISA KEV lists CVE-2025-41450 as exploited; actions[0] "because CISA lists CVE-2025-41450 as exploited")
   - Evidence / fix: (low confidence) KEV-listed unauthenticated authentication bypass on a product family under active attack in Europe and Switzerland (the sibling 2026-10-13 incident entry is high), thousands of exposed devices, and the entry's own action asks for an out-of-cycle upgrade or de-exposure. Compare the Mitel and Juniper entries moved to high on the same evidence class. KEV does not tie the listing to the refrigeration campaign, so notable may be intended; justify or align.

### Missed angles

None found. Two searches (exploited vulnerabilities of 2026-11-25; Swiss public-sector incidents of November 2026) surfaced nothing in-window beyond what the store carries; all ten 2026-11-25 KEV additions have a disposition (Juniper new; Mitel and Danfoss updated; Xen Orchestra already covered). Coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 9, editorial: 5, advisory: 3)

The firm defect is the Claroty entry's F3: a pre-existing clause cited to Claroty that the Claroty page does not carry, found on re-reading the page this pass (it sat in a paragraph the fix pass re-touched). The other truth items are low-confidence or low-severity and are marked so. Everything else in the nine updated entries and four new entries checks out against the fetched pages: Juniper (CISA, BSI, ENISA, EPSS), SEPPmail (eleven rows, vendor page), Okta and Permiso, 1Password, Drupal (SA-017/018/019, CISA, StepSecurity, Searchlight), GeoServer, Java4Shell (HPE, Cisco 1.4, Fortinet), nginx2root (Unit 42, PAN, Cisco 1.5), Mitel, PolinRider, ARTEX (Microsoft guide, Nextgov, The Record, Macau Business). No IOCs, no TLP, no watchlist or org_triage use, no em dashes outside changelog headings.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: body
  item: 2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce
  url_or_quote: 'CVE-2025-41450 ... bypasses normal login and discloses a web report with internal IPs, usernames and store names, as Claroty puts it: "the application accepts a specially crafted authentication request containing a generated ''code of the day''" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers))'
  summary: 'The cited Claroty page never mentions a web report, internal IPs, usernames or store names (grep for "report", "internal IP", "usernames", "store names" finds only "privately reported"); that clause is Danfoss DSA-2025-03-01 / the CISA KEV description, not Claroty. Claroty says instead: "Successful authentication through this hidden mechanism results in a fully authenticated administrative session, granting privileged access to the device''s web management interface." Fix: cite DSA-2025-03-01 or the KEV record for the report clause and state Claroty''s own description of the impact.'
- code: F4
  category: hallucinated-fact
  section: frontmatter
  item: 2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce
  url_or_quote: 'cves[CVE-2025-41451].vector and cves[CVE-2025-41452].vector: zero-click'
  summary: '(low confidence) The run set CVE-2025-41450 to user-interaction because its CNA record carries UI:R, but left the two sibling CVEs at zero-click although their CNA records (EUVD-2025-25499, EUVD-2025-25498) carry CVSS:4.0/.../PR:H/UI:A. The sourcing_note explains only the 41450 choice. Apply one rule to all three or explain.'
- code: F4
  category: hallucinated-fact
  section: body
  item: 2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce
  url_or_quote: '**Triage:** monitor authentication attempts ... for requests carrying a non-standard authentication parameter shape (a "code" field distinct from the normal username/password flow): legitimate operator logins never use the code-of-the-day mechanism, so its presence in a request is itself the discriminator.'
  summary: '(low confidence) Claroty describes "two request attributes (redacted)" set to 1 plus "a precomputed password" in the normal getauth request, not a separate "code" field, and calls the mechanism "likely intended for vendor support or maintenance", so a vendor-support login is a possible benign lookalike. The discriminator as worded does not follow from the cited mechanism.'
- code: F3
  category: claim-not-supported
  section: body-update-section
  item: 2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce
  url_or_quote: 'Cisco''s advisory is at version 1.4 of 2026-11-23: ... ([Cisco, 2026-11-20](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nov2026-java-rce-eCa6ss9z)); also main analysis "Cisco''s advisory (version 1.4) ... ([Cisco, 2026-11-20]"'
  summary: '(low confidence) The cited page is first published 2026-11-18 and last updated 2026-11-23 (revision table: 1.4 2026-NOV-23, 1.3 2026-NOV-20, 1.0 2026-NOV-18). The citation label 2026-11-20 is the version 1.3 date, two days off the first publication and three off the version-1.4 text it terminates, and contradicts "version 1.4 of 2026-11-23" in the same sentence. sources[] carries the same 2026-11-20.'
- code: F3
  category: claim-not-supported
  section: update-section
  item: 2026-11-19/nginx-nginx2root-five-unauth-memory-corruption-flaws
  url_or_quote: 'Palo Alto Networks released 12.1.7-h15, 11.2.10-h19 and 11.2.13-h6 on 2026-11-24'
  summary: '(low confidence) The PAN timeline says only "2026-11-24 Removed ETA for 12.1.7-h15, 11.2.10-h19, 11.2.13-h6 as these versions are released"; the earlier ETA was 2026-11-23, so the release date is not stated and may precede 2026-11-24. Say the ETA was removed on 2026-11-24 or drop the date.'
- code: F3
  category: claim-not-supported
  section: body-and-sources
  item: 2026-11-26/juniper-session-smart-cve-2026-103406-unauth-root-rce
  url_or_quote: '([ENISA EUVD, 2026-11-25](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-112215)) and sources[] date 2026-11-25 for EUVD-2026-112215'
  summary: '(low confidence) The record carries "datePublished":"Oct 28, 2026" and "dateUpdated":"Nov 25, 2026"; the clauses it terminates (description, CVSS 3.1 9.8, affected ranges) date from 2026-10-28. The sibling record EUVD-2026-112212 was re-dated to its datePublished in the fix pass, so the two citations in one entry now follow different conventions.'
- code: F14
  category: quantifier-without-source
  section: body
  item: 2026-11-26/1password-employee-github-account-backend-compromise
  url_or_quote: '**Defender takeaway:** 1Password''s own advice is limited to phishing caution and reporting suspicious messages'
  summary: '(low confidence) The post''s "What you can do" has four items: phishing caution; "1Password will never contact you to ask for your account password or Secret Key"; "Keep your Secret Key and account password safe."; "If you see something suspicious, tell us at support@1password.com." "Limited to" two of them is the same restrictive quantifier iteration 1 flagged as "only"; the body paragraph lists all four correctly.'
- code: F4
  category: hallucinated-fact
  section: frontmatter
  item: 2026-11-25/geoserver-five-step-unauthenticated-rce-chain-public-poc
  url_or_quote: 'cves[]: exploited on CVE-2026-129243, CVE-2026-120705, CVE-2026-129245; CVE-2026-129244 and CVE-2026-129242 without it'
  summary: '(low confidence) The fix rationale says every CVE any source names as exploited carries the status, but the update section itself states "watchTowr''s prose names all five chain CVEs" and the watchTowr FAQ prose reads "CVE-2026-129245, CVE-2026-129242, CVE-2026-129243, CVE-2026-129244, and CVE-2026-120705 is being exploited in the wild". The status set follows THN for 129243 and the table for 129245 but not the prose for 129244 and 129242. Mark all five (body already shows the disagreement) or state the rule in the sourcing note.'
- code: F4
  category: hallucinated-fact
  section: run-record-notes
  item: runs/2026-11-26/2026-11-26T0356Z-intel.md
  url_or_quote: '"One `improvement`: Java4Shell (HPE bulletin, Cisco version 1.4)."; "Recorded for the audit: the Claroty entry carries CVSS 7.6 and 5.4 ... and CVE-2025-41450''s vector shows UI:R and AC:H in the CNA record against the entry''s zero-click"; "Danfoss 2023 flaws (Danfoss states no authentication requirement ...)"; "Drupal CVSS (The Hacker News 9.8 without a source, none exists)" listed under contradictions carried in entries'
  summary: 'Stale after the fix pass. The Java4Shell record is now type update; the Claroty frontmatter now carries 8.7 and 6.8 and vector user-interaction; the Danfoss section now says the advisory "does not state whether authentication is needed"; the Drupal sourcing_note no longer carries the Hacker News CVSS sentence. Update the notes to the shipped state.'
- code: F9
  category: surface-contradiction
  section: body
  item: 2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce
  url_or_quote: 'The RCE and Nginx-injection primitives require prior authentication; Claroty''s article does not explicitly confirm the code-of-the-day mechanism as a pre-auth path into the two post-auth primitives, so the chain is treated as auth-gated unless a combined path is independently confirmed.'
  summary: 'Claroty (primary): "Successful authentication through this hidden mechanism results in a fully authenticated administrative session", "we gained access to the device''s full administrative interface and every management function it exposed", and the findings "combine to create powerful attack chains against internet-accessible cyber-physical systems". Danfoss DSA-2025-03-01 and CISA KEV (cited) describe the same flaw as a web-report disclosure. The entry takes the Danfoss/CISA impact in summary and body and the auth-gated reading without a Contradiction line naming Claroty''s different impact statement. Add the contradiction and revisit the chain wording.'
- code: F9
  category: surface-contradiction
  section: update-section
  item: 2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse
  url_or_quote: 'the commercial edition is therefore the vendor''s own product, not a community fork (and the 2026-11-01 section no longer says "among them a commercial one")'
  summary: '(low confidence) GTIG, cited in that section, writes "the framework continues to proliferate globally via community forks, including localized variations such as ScopeWeaver and a commercial version dubbed ARTEX PRO". The run removed GTIG''s clause and states the opposite from ThreatBook''s release and Microsoft without attributing the disagreement to GTIG. The run record lists only Microsoft vs ThreatBook as the contradiction.'
- code: F16
  category: org-triage
  section: frontmatter
  item: 2026-11-26/seppmail-15-1-2-gina-template-injection-account-takeover
  url_or_quote: 'priority: notable ... "treat the template injection and the unauthenticated reset as the reason to move this update ahead of the regular cycle"'
  summary: '(low confidence) A Swiss vendor''s gateway (regions: switzerland, europe) with a vendor-scored 9.3 unauthenticated account takeover and an unauthenticated reset; the entry''s own takeaway urges an out-of-cycle update where GINA is internet-facing, which is the high bar''s decision. Notable implies the regular cycle. No exploitation or PoC is stated, so notable is defensible; align the takeaway or the priority.'
- code: F16
  category: org-triage
  section: frontmatter
  item: 2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce
  url_or_quote: 'priority: notable (update typed: CISA KEV lists CVE-2025-41450 as exploited; actions[0] "because CISA lists CVE-2025-41450 as exploited")'
  summary: '(low confidence) KEV-listed unauthenticated authentication bypass on a product family under active attack in Europe and Switzerland (the sibling 2026-10-13 incident entry is high), thousands of exposed devices, and the entry''s own action asks for an out-of-cycle upgrade or de-exposure. Compare the Mitel and Juniper entries moved to high on the same evidence class. KEV does not tie the listing to the refrigeration campaign, so notable may be intended; justify or align.'
- code: F5
  category: missing-citation
  section: body
  item: 2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce
  url_or_quote: '"; patched in firmware build 4.2." and "Danfoss shipped firmware R4.3.1 fixing CVE-2025-41451/41452 (build 4.2 for CVE-2025-41450)."'
  summary: '(low confidence) No inline citation; the Claroty page says only "released firmware version R4.3.1, which addresses the vulnerabilities described in this research" and does not mention build 4.2. Build 4.2 is in Danfoss DSA-2025-03-01, cited only in the update section.'
- code: F11
  category: editorial-advisory
  section: body
  item: 2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack; 2026-11-26/seppmail-15-1-2-gina-template-injection-account-takeover
  url_or_quote: '"the report-generating authentication bypass that the Claroty entry from August covers"; "The earlier 15.1.1 fixes are covered separately."'
  summary: 'Store cross-references without a link in reader-facing text, raised in iteration 1 and not changed (the fix pass handled only the Okta sentence). Drop them or link the entry; both entries already carry the other in references[] where applicable.'
- code: F11
  category: editorial-advisory
  section: frontmatter
  item: 2026-11-26/okta-ai-agents-mail-tm-disposable-signups-blocklist-decay
  url_or_quote: 'title: "... whose single rotating mailbox domain makes blocklists stop matching within weeks"; headline: "one rotating domain defeats blocklists within weeks"; summary: "so a blocklist stops matching within weeks"'
  summary: 'Okta writes "a blocklist built from previously observed domains will very likely stop matching within weeks of being compiled"; the body keeps "very likely", the title, headline and summary state it as fact.'
- code: F11
  category: editorial-advisory
  section: run-record-notes
  item: runs/2026-11-26/2026-11-26T0356Z-intel.md
  url_or_quote: 'iteration-2 deltas item 25: "registered as separate keys ... noted in the run record for the audit" (Onyx Sleet/Andariel, Salt Typhoon/FamousSparrow)'
  summary: 'The run record contains no mention of Andariel, FamousSparrow or GhostEmperor (grep finds none); registry actor:andariel and actor:famoussparrow remain unlinked to actor:onyx-sleet and actor:salt-typhoon. Add the note the fix pass says exists.'
```
