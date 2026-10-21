**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-21T04:39:34Z · ended_at=2026-10-21T05:00:32Z · duration_seconds=1258

## Verification report — 2026-10-21T0256Z-intel (iteration 3)

Scope: post-fix cold pass, all 230 ledger claims decided (rows in `work/2026-10-21T0256Z-intel/verification.iter3.claims.yaml`: 228 ok, 2 F3), the 6 new entries, the 4 updated entries read whole with `git diff HEAD`, the run record, and the 7-item deltas block. Pages were read live this iteration with `extract`/`url`/`pdf` (CISA AA26-293A also through `WebFetch`, the KEV catalogue through `cisa-kev`, CVE.org through its API, EUVD through its search API). Reading limits: the live ConnectWise advisory is 403 on every transport (extract, WebFetch), so ConnectWise claims were checked against the saved read `work/2026-10-19T0256Z-intel/bodies/cw-advisory.md` (updates of 2026-10-18 01:00, 18:45 and 2026-10-19 01:15 UTC), which the entry itself bounds ("as of ... 2026-10-19 01:15 UTC"); the Tages-Anzeiger article is paywalled (standfirst and key points read); the CISA advisory body was checked from the saved read plus the live `WebFetch` summary. Oracle's tallies were recomputed from the 1295 risk-matrix rows (112 at 9.0 or higher, 90 unauthenticated network, 73 distinct ids, six at 10.0: all hold).

Deltas block (iteration-2 findings): 0 confirmed (PHP title, headline and summary now say a screenshot of an exploit tool is "reported leaked" and give remote code execution as CERT-EU's reading; both match Sansec and CERT-EU), 1 confirmed (the 2026-10-10 Publica closer reads "as of that date"), 2 confirmed (all ten sourcing notes are two or three sentences; no loader or key file name remains in any entry; the older ConnectWise, Metabase and Publica notes are cut), 3 confirmed with a residual (the third Publica record is gone; two records for the page remain, dated 2026-10-08 and 2026-10-20, as in HEAD), 4 confirmed (eMudhra: "some legitimate certificates ... will stop working", Google's hedge), 5 confirmed (T1569.002 and T1059.003 in techniques[]; the advisory's Table 7 maps both), 6 declined, acceptable (recorded again as an advisory residual below). No defect introduced by the remediations beyond those listed. Changelog contract 4c holds on all four updated entries: every record's `fields` covers the diff, `updated_at` equals the `update` record's `at` on PAN-OS, Publica and Metabase and is untouched on the ConnectWise `improvement`, each section matches its record summary, no silent edit, no superseded statement left standing (PAN-OS's older sections date Unit 42's "no lateral movement" line to 9 June).

### Generic / oversight URLs (replace with specific article)

- #1 (F2, low confidence) `2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619`: primary source `https://www.php.net/archive/2026.php` is the 2026 news archive (title "PHP: News Archive - 2026"), a listing of every 2026 item; CERT-EU, Sansec and Wordfence link the item as `https://www.php.net/archive/2026.php#2026-10-20-1`. Use the anchored permalink in `sources[0]`, the three php.net evidence `source_url` values and the body links.

### Citation does not support the claim

- #2 (F3) `2026-10-21/oracle-october-2026-cpu-six-unauthenticated-cvss-10-rows`, summary and last body sentence: "Patch availability documents are behind My Oracle Support login ([Oracle, 2026-10-20](...cpuoct2026.html))". The page says only "refer to ... Patch Availability Document for Oracle Products, My Oracle Support Note CPU391" and "Please click on the links in the Patch Availability Document column"; it never says login is needed. Reword to "point to My Oracle Support notes" or drop the clause.
- #3 (F3) `2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619`, sourcing_note: "CERT-EU, Sansec and Wordfence all derive from the PHP announcement, so they corroborate the release and not the flaws". CERT-EU: "according to other leaks [1,2,3]" and a social-media post for "PHP 5 onwards"; Sansec: "Information about the embargoed bugs leaked on October 20. Security firm watchTowr confirmed that they are remote code execution vulnerabilities in PHP" plus a leaked tool screenshot. Only Wordfence repeats the announcement alone, and the note's own first sentence says the ids, tool and ranges come from CERT-EU and Sansec. Say CERT-EU and Sansec add leak-based claims the PHP project has not confirmed.
- #4 (F3) `2026-10-21/apt28-hookedge-backdoor-nato-police-shipbuilder-ssh-tunnel`, sourcing_note (same wording in `entities/registry.yaml` actor:apt28 summary): "assessing with moderate confidence that it overlaps APT28". Recorded Future: "Insikt Group assesses with moderate confidence that this activity was conducted by BlueDelta (which overlaps with APT28, Fancy Bear, and Forest Blizzard)"; the overlap is unqualified in its Background. The entry body states it correctly; fix the note and the registry summary.

### Unsupported / hallucinated facts

- #5 (F4, low confidence) `2026-10-21/oracle-october-2026-cpu-six-unauthenticated-cvss-10-rows`, tags: `[vulnerabilities, pre-auth, rce, patch-available]`. The advisory gives only a CVSS vector (network, no privileges, High C/I/A) and no vulnerability class, the body never says remote code execution, and every `cves[].type` is null. Drop `rce` or support it.

### Strengthen primary source

- #6 (F6, low confidence) `2026-10-21/aa26-293a-safepay-ransomware-edge-flaws-backup-nas-reset`, `cves[].status` and `fixed`: `patch-available` on all five records rests on neither cited source (the advisory names no fix; KEV says "apply mitigations per vendor instructions"). The vendor advisories linked in the KEV notes, read this iteration, state fixes: Cisco `cisco-sa-asaftd-info-disclose-9eJtycMB` ("Cisco has released software updates"), Cisco `cisco-sa-asaftd-ravpn-auth-8LyfCkeC`, Veeam KB4424 ("resolved starting in the following ... build numbers") and KB4649, SonicWall SNWLID-2024-0015 ("Fixed Software"). Cite them as corroborating sources or drop the status.

### Editorial / less-is-more flags (advisory)

- #7 (F11) Residual em dashes: this run edited Metabase body paragraph 1 (added the GHSA citation) and left "access to the instance — from which"; the older Metabase sections and the append-only PAN-OS 2026-06-17 record summary carry more. The iteration-2 decline stands as an audit-sweep item.
- #8 (F11) `emudhra-...` Exposure: "shows Node.js, Bun and FreeBSD as pending when read" narrates the research step; give the tracker's date instead.
- #9 (F11, low) Publica still lists its page under two source records (2026-10-08 and 2026-10-20; the body cites each date); ConnectWise's source is the Trust Center advisories index (the 19 October advisory is its top item). Both pre-date this run's delta.

No missed angle found: the KEV sweep matches the catalogue (six additions, Siemens covered, Plex and SiteGuard dispositioned), CVE-2026-76519 (Cisco AsyncOS, KEV 2026-10-14) and wp2shell are already in the store, and searches for further in-window exploited flaws, Cisco 2026-10-21 publications and Swiss public-sector incidents found nothing the run's sources missed.

### Verdict

NEEDS_FIXES (truth: 5, editorial: 1, advisory: 3)

All six truth/editorial findings are small and low-risk wording or citation fixes; none touches an exploitation, version, count or attribution fact that a defender acts on. #1, #5 and #6 are low confidence.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F2
  category: generic-url
  section: 2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619 (sources[0], evidence source_url, body links)
  item: "PHP: critical security release pre-announced for 14:00 UTC, CVE-2026-109618 / CVE-2026-109619"
  url_or_quote: "https://www.php.net/archive/2026.php"
  summary: "(low confidence) The primary source is the php.net year news archive (title 'PHP: News Archive - 2026'), a listing index of every 2026 news item, not the single announcement. CERT-EU, Sansec and Wordfence (all fetched this iteration) link the item as https://www.php.net/archive/2026.php#2026-10-20-1; use that anchored permalink in sources[0], the three php.net evidence source_url values and the body links."
- code: F3
  category: claim-not-supported
  section: 2026-10-21/oracle-october-2026-cpu-six-unauthenticated-cvss-10-rows (summary and body final sentence)
  item: "Oracle's October CPU: six unauthenticated CVSS 10.0 rows"
  url_or_quote: "Patch availability documents are behind My Oracle Support login ([Oracle, 2026-10-20](https://www.oracle.com/security-alerts/cpuoct2026.html)); summary: 'its patch availability documents sit behind My Oracle Support login'"
  summary: "The cited advisory page (fetched this iteration, 1295 risk-matrix rows parsed) says only 'refer to ... Patch Availability Document for Oracle Products, My Oracle Support Note CPU391' and 'Please click on the links in the Patch Availability Document column'; it never says the documents need a login. Reword to 'point to My Oracle Support notes' or drop the clause."
- code: F3
  category: claim-not-supported
  section: 2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619 (sourcing_note)
  item: "PHP: critical security release pre-announced"
  url_or_quote: "CERT-EU, Sansec and Wordfence all derive from the PHP announcement, so they corroborate the release and not the flaws"
  summary: "Not what the sources say: CERT-EU writes 'according to other leaks [1,2,3]' and cites a social-media post for PHP 5 onwards; Sansec reports that 'Information about the embargoed bugs leaked on October 20. Security firm watchTowr confirmed that they are remote code execution vulnerabilities' and a leaked tool screenshot. Only Wordfence derives from the announcement alone. The same note's first sentence already says the CVE ids, the leaked tool and the version ranges come from CERT-EU and Sansec. Say that Wordfence repeats the announcement and that CERT-EU and Sansec add leak-based claims the PHP project has not confirmed."
- code: F3
  category: claim-not-supported
  section: 2026-10-21/apt28-hookedge-backdoor-nato-police-shipbuilder-ssh-tunnel (sourcing_note; same wording in entities/registry.yaml actor:apt28 summary)
  item: "APT28 (Swallowtail) used the HOOKEDGE backdoor against a law-enforcement agency, a naval shipbuilder and an aircraft-engine maker"
  url_or_quote: "Recorded Future ... tracks the group as BlueDelta, assessing with moderate confidence that it overlaps APT28"
  summary: "Recorded Future (https://www.recordedfuture.com/research/bluedelta-targets-with-hookedge) puts the hedge on the attribution of the activity: 'Insikt Group assesses with moderate confidence that this activity was conducted by BlueDelta (which overlaps with APT28, Fancy Bear, and Forest Blizzard)'; the BlueDelta/APT28 overlap is stated unqualified in its Background. The entry body has it right ('assesses with moderate confidence that BlueDelta, which overlaps APT28, is behind it'); fix the sourcing_note and the registry summary 'which it assesses with moderate confidence overlaps APT28'."
- code: F4
  category: hallucinated-fact
  section: 2026-10-21/oracle-october-2026-cpu-six-unauthenticated-cvss-10-rows (tags)
  item: "Oracle's October CPU: six unauthenticated CVSS 10.0 rows"
  url_or_quote: "tags: [vulnerabilities, pre-auth, rce, patch-available]"
  summary: "(low confidence) The `rce` tag is stronger than the entry: the advisory gives only a CVSS vector (network, no privileges, High confidentiality, integrity and availability) and no vulnerability class, the body never says remote code execution, and every cves[].type is null. Drop `rce` or support it."
- code: F6
  category: strengthen-primary-source
  section: 2026-10-21/aa26-293a-safepay-ransomware-edge-flaws-backup-nas-reset (cves[].status and fixed)
  item: "AA26-293A: SafePay ransomware, five edge and backup flaws"
  url_or_quote: "status: [exploited, cisa-kev, patch-available]; fixed: \"not stated by the advisory; see Cisco's advisory\""
  summary: "(low confidence) `patch-available` on all five records rests on neither cited source (the advisory names no fix; KEV requiredAction says 'apply mitigations per vendor instructions'). The vendor advisories linked in the KEV notes, fetched this iteration, do state fixes: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-info-disclose-9eJtycMB ('Cisco has released software updates'), https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ravpn-auth-8LyfCkeC, https://www.veeam.com/kb4424 ('resolved starting in the following ... build numbers'), https://www.veeam.com/kb4649, https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2024-0015 ('Fixed Software'). Cite them as corroborating sources or drop the status."
- code: F11
  category: editorial-advisory
  section: "2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally (body paragraph 1) and 2026-05-30/cve-2026-0257-... (updates[] 2026-06-17 summary)"
  item: "residual em dashes"
  url_or_quote: "\"that yields administrator access to the instance — from which the attacker can change\""
  summary: "Advisory, residual: this run edited the Metabase paragraph (added the GHSA citation) and left its em dash; the other em dashes in older Metabase sections and the append-only PAN-OS 2026-06-17 record summary are the audit-sweep items the iteration-2 decline already recorded."
- code: F11
  category: editorial-advisory
  section: "2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates (Exposure)"
  item: "eMudhra"
  url_or_quote: "shows Node.js, Bun and FreeBSD as pending when read"
  summary: "Advisory: 'when read' narrates the research step; state the tracker's date instead ('as of the 2026-10-20 tracker')."
- code: F11
  category: editorial-advisory
  section: "2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow (sources[]) and 2026-10-18/connectwise-cloud-backup-... (sources[0])"
  item: "living-page source records"
  url_or_quote: "https://www.publica.ch/de/cyberangriff-auf-softwarelieferanten (records dated 2026-10-08 and 2026-10-20); https://www.connectwise.com/company/trust/advisories"
  summary: "Advisory, low: the Publica page is still listed under two records (dated 2026-10-08 and 2026-10-20; the body cites each date), and ConnectWise's source is the Trust Center advisories index page (the 19 October advisory is its top item). Both pre-date this run's delta; leave or merge at the audit."
```
