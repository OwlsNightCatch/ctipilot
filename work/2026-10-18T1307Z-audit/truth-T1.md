**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:26:36Z · ended_at=2026-10-18T13:57:02Z · duration_seconds=1826

## Retrospective truth pass, batch T1 (run 2026-10-18T1307Z-audit)

### 2026-10-02/zammad-cve-2026-102489-102490-exploited-divd-breach — factual-error

- **Claim** (summary; actions[0]; cves[CVE-2026-102489].fixed; Defender takeaway; closing sentence of `## Update — 2026-10-10T03:43:01Z`): "Zammad says the code-execution flaw is exploitable only on 6.5 and older, which receive no security fixes" / "(6.5 and older receive no security fixes, and 7.2.0 is affected by the 27 advisories ...)" / "Nothing changes for the code-execution flaw: it stays exploitable only on 6.5 and older, which receive no security fixes."
- **Ground truth:** On 2026-10-15 Zammad shipped 6.5.5, an exceptional emergency release for the unsupported 6.5 series: "Zammad 6.5.5 provides an emergency security fix by hardening the WebSocket server code to address CVE-2026-102489"; "Zammad 6.5 users: Update to Zammad 6.5.5 immediately if upgrading to Zammad 7.2.2 is not yet possible." It is available only through a new package repository; 6.5 is still out of support. https://zammad.com/en/product/releases/6-5-5 (also listed on https://zammad.com/en/product/releases/ as "15 October 2026").
- **Fix:** append an update (record + section) naming 6.5.5 as the emergency fix for CVE-2026-102489 on the 6.5 series (new repository required, 6.4 and older and the upgrade-to-7.2.2 advice unchanged), and reword "receive no security fixes" in the five places above to "receive no regular security fixes; 6.5 has one emergency fix (6.5.5)".

### 2026-10-04/cve-2026-88779-citrix-netscaler-saml-overflow-exploited — imprecision

- **Claim** (Detection): "The Citrix pages list no signs of compromise to look for ([Citrix, 2026-10-03](https://community.citrix.com/techzone-blogs/110_security-updates/understanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway/))".
- **Ground truth:** the cited Citrix blog is unreadable from the container (403 on extract, raw, jina and WebFetch). Three secondary sources say Citrix supplies an indicator-of-compromise script through NetScaler Console as the compromise check: The Register 2026-10-05, quoting watchTowr: "Citrix provides an indicator-of-compromise script that teams can run to check exposed appliances for signs of compromise, though a clean result is not definitive proof"; watchTowr FAQ ("... the latest script version can report a false positive about suspicious nobody processes"); Help Net Security 2026-10-05. https://www.theregister.com/security/2026/10/05/citrix-netscaler-security-snafus-get-even-worse-amid-more-0-day-reports/5301232
- **Fix:** have a reader that can reach community.citrix.com confirm; then replace the sentence with the NetScaler Console IoC script (clean result not proof; nobody-process false positive) as the vendor's post-patch compromise check, and add it to Detection.

### 2026-10-02/cve-2026-104286-fortimail-path-traversal-zero-day-kev — imprecision (low confidence)

- **Claim** (`## Update — 2026-10-06T04:59:00Z`; sources[] CSAF record date): "The advisory's structured record is dated 2026-10-05 and lists 8.0.2, 7.6.7 and 7.4.9 as not affected".
- **Ground truth:** the CSAF record read today carries `"current_release_date": "2026-10-07T00:00:00"` with only the 2026-10-01 initial publication in `revision_history`; `known_not_affected` does list FortiMail-8.0.2, 7.6.7 and 7.4.9. The 2026-10-05 date was probably right when written and was overtaken by Fortinet's 2026-10-07 revision. https://filestore.fortinet.com/fortiguard/psirt/csaf_improper-limitation-of-a-pathname-to-a-restricted-directory_fg-ir-26-175.json
- **Fix:** say the structured record lists the three builds as not affected, without a record date (or date it 2026-10-07).

### 2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev — imprecision (low confidence)

- **Claim** (`## Update — 2026-10-03T04:55:00Z`; sources[] date): "Cisco's Live Protect page lists the feature from Catalyst SD-WAN Control Components release 20.18.3 ... ([Cisco, 2026-07-01](https://www.cisco.com/c/en/us/td/docs/routers/sdwan/26x-later/network-monitoring/network-monitoring-guide/live-protect-for-cisco-catalyst-sd-wan.html))".
- **Ground truth:** the page's visible dateline is "Updated: September 22, 2026" (page date meta Oct 6 2026); no 2026-07-01 date appears. The content claims (20.18.3, monitoring and enforce modes, shields for the current and two preceding releases) are all supported. https://www.cisco.com/c/en/us/td/docs/routers/sdwan/26x-later/network-monitoring/network-monitoring-guide/live-protect-for-cisco-catalyst-sd-wan.html
- **Fix:** change the citation and sources[] date to 2026-09-22.

### 2026-10-02/ftapi-ransomware-the-gentlemen-supplier-to-authorities — imprecision (low confidence)

- **Claim** (summary): "FTAPI Software of Munich, whose secure file-transfer service is used by authorities and companies".
- **Ground truth:** heise says "Munich-based provider FTAPI offers services for easy data transfer. Its customers include authorities and companies."; no cited source uses the name "FTAPI Software". https://www.heise.de/en/news/Cyber-attack-on-data-exchange-service-FTAPI-11469688.html
- **Fix:** "FTAPI of Munich".

## Named lead: 2026-10-02/anssi-reactiv-situation-report-99-state-data-breaches (decided: clause supported, no defect)

The pre-pass warning is a false positive caused by the PDF having no text layer. `pdftotext` on https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-006.pdf returns blank pages and `fetch_source.py pdf` returns binary, so the page check could not see the id. I rendered the 10 pages and read them. Page 3, "Vulnérabilités récurrentes": "Vulnérabilité Metabase (CVE-2026-72898) : une exploitation massive de la vulnérabilité est observée depuis début août 2026 ... Neuf instances au sein de ministères ont ainsi été compromises. Le correctif est disponible depuis le 6 août 2026. L'ANSSI a demandé à l'ensemble des ministères d'identifier leurs instances et de vérifier leur mise à jour." Page 4 repeats the id under "Travaux de l'ANSSI". The 99 / 67 / 32 counts (page 3), the Tchap, SNU (275,000) and TRACFIN (136 / 213) summaries (pages 5-6) and the six causes (page 3) all match the entry. CVE-2026-72898 resolves to the Metabase SQL injection in the CVE record and in KEV (dateAdded 2026-08-11), so the id names the right flaw. The clause "less often, missing authorization checks, SQL injection and exposed files" is the sixth bullet on pages 3-4.

## Claims that could not be read (14, verdict `unreadable`, none contradicted)

- Citrix community blogs (community.citrix.com returns 403 on every transport): 7 claims in the CVE-2026-88779 entry (the "upgrade your deployment again" quote, the Global Deny List build range, `show appfw signatures` / signature v24, the Citrix-ties-it-to-Gateway/AAA clause, the "no signs of compromise" sentence, the 2026-10-02 guidance-blog independence statement, and the 107406 blog's "not aware of any unmitigated exploits"). Where a secondary source relays the passage it is named in the claim row.
- Polizei Hamburg release (presseportal.de, captcha): 6 claims in the KillSwitch entry; the same facts are carried by Europol's release, fedpol's release, BleepingComputer and dpa/APA coverage that quote it.
- The entry-level evidence quotes attributed to those Citrix blogs and the Polizei Hamburg release are likewise not literally checkable by me.

Everything else in the 16 entries (401 claims: 379 ok, 14 unreadable, 8 flagged F3/F4/F5) was checked against pages fetched in this pass: every `cves[]` id and CVSS against the vendor bulletin plus the CNA record (every id resolves, scores match, and KEV state and dates match the current catalogue version 2026.10.16), every `techniques[]` id is active in the v20.0 pin, and no IOCs are present.
