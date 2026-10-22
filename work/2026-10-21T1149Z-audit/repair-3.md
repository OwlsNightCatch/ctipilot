# Repair worker 3, cleanup wave 03 (2026-10-21T1149Z-audit)

Batch: `work/2026-10-21T1149Z-audit/batch-3.yaml`, 5 entries. Fetched bodies: `work/2026-10-21T1149Z-audit/repair-3/src/` (all 15 pages read cleanly with `extract`, except The Register, which returned only site navigation, and the CERT-Bund WID portal, an Angular shell read instead through `bsi-csaf WID-SEC-2026-1989`). KEV catalogue 2026.10.20 read with `cisa-kev`. Every new evidence quote and every new clause was checked with `grep -F` against the saved body. The gate's page checks skip migrated entries, and all five are migrated.

Records written: 3 improvement, 0 correction, 0 update. Entries without a record: 2.

## 2026-05-15/cve-2026-20182-cisco-catalyst-sd-wan-controller-manager-pre: no record

Every defect is already fixed by 2026-10-11T1307Z-audit, re-derived on the current text. The fixes were checked against Cisco rpa2, Rapid7 and Talos (sd-wan-ongoing-exploitation).
- Folded block (12 defects): the UAT-8616 kill chain with Clusters 1-10 tooling, device-type values, XenShell, CVE-2026-20127 as an RCE, the "sixth" count, "five advisories", "10+ clusters", the VHUB hunt, the revoked T1562.001 and T1070.002, the hardening rationale, the "Background." evidence, and the missing classification and techniques: all gone or corrected. The body now says vHub type 2, ten clusters, Cisco's `show control connections detail` check, `techniques: [T1190, T1098.004, T1021.004]` and Admiralty A1.
- Own block (6 defects): the ED 26-03 date, NETCONF on the Controller, segmentation, Validator, evidence and classification are all fixed.
- `facts_only_in_duplicates` rows with verified: true were not carried:
  - Talos "high confidence", the ORB overlap and the hardening-guide URL are not material enough to justify a record on their own.
  - The Snort SIDs are vendor detection content in an entry kept vendor-agnostic.
  - The CVE-2026-20127 and version-downgrade detail is the February activity, not this CVE.
- Item 4: already linked both ways with the CVE-2026-20245 entry.

## 2026-06-06/cve-2026-20245-cisco-catalyst-sd-wan-manager-actively-exploi: improvement

- `at`: 2026-10-21T12:10:28Z.
- Fields: headline, techniques, actions, body.
- Applied (ground truth: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx and https://cloud.google.com/blog/topics/threat-intelligence/zero-day-exploitation-cisco-catalyst-sd-wan-manager):
  - Folded-block defect "tenant-list CSV detail is Mandiant's; Cisco's IOC examples show other upload handlers":
    - Detection now lists all three `scripts.log` upload scripts Cisco gives (tenant list, vSmart serial numbers, chassis numbers).
    - The headline says "crafted upload file" instead of "crafted tenant file". It was also 139 characters and is now 113.
    - The citations are rebound so that Cisco carries the scripts.log clause and Mandiant the auth.log, rollback and `show history` clause.
  - Live Protect shield: "temporary coverage" is now "only temporary partial protection" (Cisco's words). This is swept in the main text and in the 2026-10-11 correction section.
  - From the verified group `current_state`: Cisco saw exploitation push configuration changes to edge devices and tells customers to verify edge-device configurations. This is added to the narrative, the Defender takeaway and the action.
  - From the verified `facts_only_in_duplicates` rows (su from admin, admin password changed then reverted), plus Mandiant's own Detections section: Detection now names `vmanage-admin` logins from unexpected sources, admin password set-and-revert, `su` from admin to an unauthorized account, `/var/confd/rollback/` password delta commits and `show history`.
  - Defender takeaway: Mandiant's actor restored what it modified and checked that its root account was gone, so a missing account does not clear a system. The takeaway also carries Cisco's TAC-remediation statement.
  - The action replaces the weak UID-0 check with the edge-device and auth.log `su` checks.
  - techniques: added T1021.004, T1078.001 and T1098. These are the SSH logins as default accounts and the password manipulation that the Mandiant sections already describe.
- Declined, already fixed by 2026-10-11T1307Z-audit:
  - "no patch"; the cves[] type, vector, auth and score for 20245; cvss and cisa-kev for 20127 and 20182; "second".
  - The Update 2026-06-26 dates and "communications"; the chain hedge; the history and syslog deletion.
  - "first complete": the section is fixed, and the record summary is append-only.
  - classification, techniques and evidence; the vManage dashboards claim; T1078.004; the KEV status.
- Not carried: the verified: false rows.

## 2026-06-16/cisco-catalyst-sd-wan-manager-cve-2026-20262-authenticated-a: improvement

- `at`: 2026-10-21T12:09:15Z.
- Fields: sources, references, body.
- Applied (ground truth: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-arbfw-c2rZvQ and the KEV row for CVE-2026-20262):
  - Vulnerability-description defect, open remainder: Cisco's page carries neither "traversal" nor a CWE, yet "is a path traversal" was bound to it. The text now uses Cisco's wording ("does not properly validate user-supplied input during a file upload"). The path-traversal (CWE-22) classification is bound to the KEV row, which carries "Directory or Path Traversal Vulnerability" and CWE-22.
  - Tomcat-to-WildFly defect, precision remainder: Detection now names `SdraAnyConnectFileUploadHandler` in `/var/log/nms/vmanage-server.log`, the `../` path into `/var/lib/wildfly/standalone/deployments/` with a `.war` archive, `WFLYSRV0010` in `vmanage-appserver.log` and `/var/log/nms/containers/service-proxy/serviceproxy-access.log`. It follows Cisco's split between the initial vector and follow-on entries that are not always seen, and keeps the standard-operations caveat.
  - Folded MFA-action defect ("keep the exposure advice"): Exposure now carries Cisco's statement that internet-exposed Managers are at risk.
  - Item 4: `references: [2026-06-06/cve-2026-20245-...]` is added. BleepingComputer frames 20262 as the next SD-WAN Manager zero-day after 20245, and the first fixed releases are identical (20.9.9.2 through 26.1.1.2). The body states the identical releases, cited to the privesc advisory, which is appended to `sources[]`.
- Declined, already fixed by 2026-10-11T1307Z-audit:
  - Tomcat; the KEV citation; the cves affected and fixed values; the self-authored evidence; the conjectured chain and T1078.004.
  - The privilege wording: Cisco's "at least write access" is used. The Register's "single-task" contradiction belongs in a run-record note, not the entry.
  - The UAT-8616 link; the summary stub; the dangling § 5; the MFA action.
- Not carried: the verified: false row (UAT-8616 / Tomcat hunt text).

## 2026-06-19/cisco-ise-cve-2026-20181-cve-2026-20190-an-unauthenticated-c: no record

- Declined, already fixed by 2026-10-11T1307Z-audit, re-checked line by line against https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-G5WP8vv:
  - The chain; "hashed administrator credentials"; the cves auth and type values; the 3.5 hot patch and the 3.1 and 3.2 fixes; the directory escape; "most"; the 36 h patch cycle with pgAdmin, NGINX and Drupal; classification and techniques.
- Declined, CERT-Bund WID-SEC-2026-1989 (low confidence, "not verifiable"): the record is readable through the sources.json-documented recipe, `python3 tools/fetch_source.py bsi-csaf WID-SEC-2026-1989` (saved as `src/certbund-wid-csaf.json`). It is CSAF WID-SEC-W-2026-1989, "Cisco ISE and Cisco ISE-PIC: Mehrere Schwachstellen" (translated from German: "multiple vulnerabilities"). Initial release is 2026-06-17, it names CVE-2026-20181 and CVE-2026-20190, and it references cisco-sa-ise-multi-G5WP8vv. "CERT-Bund relayed the advisory" holds. Per sources.json, the portal URL is the citation to keep.
- Not carried: the verified: false rows.

## 2026-06-24/cve-2026-20230-cisco-unified-cm-webdialer-ssrf-to-arbitrary: improvement

- `at`: 2026-10-21T12:08:21Z.
- Fields: sources, evidence, body.
- Applied (ground truth: https://ssd-disclosure.com/cisco-unified-communications-manager-arbitrary-file-write-to-rce/ and https://www.bleepingcomputer.com/news/security/cisco-unified-cm-sme-flaw-cve-2026-20230-now-exploited-in-attacks/):
  - "The hunt omits the SSD-documented precursor": the narrative now carries SSD's chain. It reads the true hostname from an unauthenticated WebDialer page, uses the unauthenticated cluster-install status endpoint as the SSRF with a full path in place of a node hostname, registers a new web service and writes a JSP web shell. BleepingComputer is cited for SSD publishing its write-up and PoC after the exploitation disclosure, which supports the existing poc-public status.
  - Detection now names `/webdialer/Version.jws?wsdl`, then `/cmplatform/installClusterStatusExecute` with `action=clusterNodeInstallStatus` and a percent-encoded path in the hostname parameter, then a new service under `/webdialer/services/` and new JSP files under `/platform-services/axis2-web/`. The `file://` clause is kept.
  - SSD is appended to `sources[]` and given one verbatim `evidence[]` quote. Lab IPs and PoC file and service names were left out.
- Declined, already fixed by 2026-10-11T1307Z-audit:
  - The MISP clause; the attacker-URL and cron mechanism; "publicly available"; the KEV state and active exploitation.
  - Classification, techniques and affected/fixed; the Service Parameters path; the weekend date and "historically".
- Left unchanged on purpose: "Cisco updated its advisory on 2026-07-01 to say ... and that proof-of-concept code is available". Revision 1.1 says only "Added information about active exploitation", in the section that holds the PoC sentence, so whether v1.0 already carried that sentence is not verifiable.

## Legacy duties and em dashes

No entry in the batch has `legacy_duty: true` or listed em dashes. My edits, sections and summaries contain no em dash. The only em dash in a touched entry is inside the 2026-06-26 record summary on the CVE-2026-20245 entry, which is append-only.

## State changes for the main agent

- `entities/registry.yaml`: none (no entity, product or relation changed).
- `state/cves_seen.json`: none (no `cves[]` record changed on any entry).

## Checks run

- `python3 tools/check_run.py --all`: exit 0. On my entries only the three expected WARNs that run id 2026-10-21T1149Z-audit has no run record yet; no FAIL. Output: `repair-3/checkall-after.txt`.
- `python3 tools/check_run.py 2026-10-21T1149Z-audit --page-checks-since 2026-10-21`: quote-literal and citation-cve PASS, nothing flagged. Output: `repair-3/page-checks.txt`.
- Main-analysis word counts: 323, 329 and 410. Headlines: 113, 100 and 106 characters.

## Residuals noticed outside the findings (nothing fixed)

- ISE entry: `evidence: []` is empty, there is no Detection line, and T1552 (Unsecured Credentials) maps CVE-2026-20190 less well than T1212 (Exploitation for Credential Access). Cisco's footnote that ISE-PIC's last supported release is 3.4 is not carried.
- ISE, 20182, 20262 and 20230 entries still carry a retired `update_of: null` key (the gate does not flag the null value).
- 20262 entry: `sectors: [telco, public-sector]` rests on no cited statement I could find. The Register URL in `sources[]` extracts to site navigation only; nothing in the body cites it.
- 20262 entry does not reference the 20182 entry. BleepingComputer mentions 20182 only as the prior month's flaw, with no build-on relation, so I left it.
- 20230 entry: SSD's PoC writes a JSP web shell (T1505.003). This is not mapped, because the exploitation seen in the wild (Defused) only wrote test files.
- 20245 entry: the 2026-06-27 update section's "hunting for new UID-0 accounts" is weakened by Mandiant's finding that the actor removed its account. It is not wrong, so it was left.
