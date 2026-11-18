import json, re
from fu2_lib import *

OR = 'oracle/cspunov2026.extract.md'
VB = 'oracle/cspunov2026verbose.extract.md'
TN = 'oracle/tenable.extract.md'
U_ADV = 'https://www.oracle.com/security-alerts/cspunov2026.html'
U_VB = 'https://www.oracle.com/security-alerts/cspunov2026verbose.html'
U_TN = 'https://www.tenable.com/blog/oracle-november-2026-critical-security-patch-update-addresses-640-cves-cve-2026-114938'
U_KEV = 'https://www.cisa.gov/known-exploited-vulnerabilities-catalog (via `fetch_source.py cisa-kev`, catalogVersion 2026.11.17)'

rows = json.load(open(ROOT + 'oracle/cspunov2026.rows.json'))
hi = json.load(open(ROOT + 'oracle/cspunov2026.hi-rows.json'))

# compact KEV records (single-line so quotes can be grep -F checked)
kev = {x['cveID']: x for x in json.load(open(ROOT + 'oracle/cisa-kev.json'))['vulnerabilities']}
with open(ROOT + 'oracle/kev-records.txt', 'w') as f:
    f.write('CISA KEV catalogVersion 2026.11.17 dateReleased 2026-11-17T17:53:15.5664Z; records fetched by tools/fetch_source.py cisa-kev on 2026-11-18\n')
    for c in ('CVE-2026-111497', 'CVE-2025-61882', 'CVE-2023-44487'):
        k = kev[c]
        f.write('KEV %s | vendorProject: %s | product: %s | vulnerabilityName: %s | dateAdded: %s | knownRansomwareCampaignUse: %s\n' % (c, k['vendorProject'], k['product'], k['vulnerabilityName'], k['dateAdded'], k['knownRansomwareCampaignUse']))
KV = 'oracle/kev-records.txt'

out = []
A = out.append

A('## 1. ORACLE CSPU 2026-11-17 (Critical Security Patch Update, Rev 1)\n')
A('Primary: ' + U_ADV + ' (read with `extract`, served `trafilatura-direct`; raw HTML also saved as `oracle/cspunov2026.raw.html` and parsed into `oracle/cspunov2026.rows.json`: 655 matrix rows). Oracle\'s own English text version of the same matrices: ' + U_VB + ' (saved `oracle/cspunov2026verbose.extract.md`). Fetched 2026-11-18 ~04:40-04:55Z.\n')

A('### 1.1 Totals and what Oracle itself states vs what is derived\n')
t = [
 ('Oracle states the patch total (655) and that the matrices cover "the product families listed below"; Oracle states NO count of product families and NO CVE count', U_ADV, OR, 'This Critical Security Patch Update contains 655 new security patches across the product families listed below.'),
 ('Advisory is Rev 1, initial release 2026-11-17 (no later revision at fetch time)', U_ADV, OR, '2026-November-17 | Rev 1. Initial Release.'),
 ('Oracle says risk matrices list only newly addressed vulnerabilities', U_ADV, OR, 'Risk matrices list only security vulnerabilities that are newly addressed by the patches associated with this advisory.'),
 ('Oracle groups Database Server, APEX, Autonomous Health Framework, Global Lifecycle Management and REST Data Services under "Oracle Database Products" in its lead-in (20 patches)', U_ADV, OR, 'This Critical Security Patch Update contains 20 new security patches for Oracle Database Products divided as follows:'),
 ('Oracle: scoring is CVSS 3.1', U_ADV, OR, 'Security vulnerabilities are scored using CVSS version 3.1'),
 ('Oracle: patches only for Premier/Extended Support versions; unsupported releases are not tested', U_ADV, OR, 'Patches released through the Critical Security Patch Update program are provided only for product versions that are covered under the Premier Support or Extended Support phases'),
 ('Oracle: unsupported releases likely also affected', U_ADV, OR, 'it is likely that earlier versions of affected releases are also affected by these vulnerabilities'),
 ('Oracle: interim relief is blocking the network protocols an attack requires (no vendor-specific workaround per CVE)', U_ADV, OR, 'it may be possible to reduce the risk of successful attack by blocking network protocols required by an attack'),
 ('Next release dates', U_ADV, OR, '15 December 2026 (CSPU)'),
 ('Next release dates (quarterly CPU)', U_ADV, OR, '19 January 2027 (CPU)'),
 ('Tenable (independent, derived from the matrices): 640 unique CVEs in 655 updates across 21 product families', U_TN, TN, 'This CSPU contains fixes for 640 unique CVEs in 655 security updates across 21 Oracle product families.'),
 ('Tenable: 62 critical patches across 57 CVEs (critical = CVSS 9.0+; includes rows that need privileges)', U_TN, TN, "This month's update includes 62 critical patches across 57 CVEs."),
 ('Tenable severity table row', U_TN, TN, '| Critical | 62 | 57 |'),
 ('Tenable states Oracle introduced CSPUs in May 2026', U_TN, TN, 'Beginning in May 2026, Oracle introduced CSPUs as a monthly release cycle'),
]
A(table(t))
A('')
A('Derived by this read from the 655 parsed matrix rows (not stated by Oracle; reproducible from `oracle/cspunov2026.rows.json`): 655 rows = 640 distinct CVE ids (matches Tenable); 62 rows at CVSS 3.1 >= 9.0 = 57 distinct CVEs (matches Tenable); of those 62, 56 rows (51 distinct CVEs) have "Remote Exploit without Auth.? = Yes" and 6 rows need privileges (listed in 1.4). Rows at 10.0: 6 (all unauthenticated). The matrices form 21 risk-matrix sections (Database Products DB, APEX, Autonomous Health Framework, REST Data Services, Application Testing Suite, Commerce, Communications, Construction and Engineering, E-Business Suite, Enterprise Manager, Financial Services, Fusion Middleware, Analytics, Hyperion, Java SE, JD Edwards, MySQL, PeopleSoft, Siebel CRM, Supply Chain, Virtualization) plus Global Lifecycle Management (no matrix, third-party VEX only). The "affected products" table lists 62 product/version lines under 26 Patch Availability Document family labels (my count). Oracle\'s own lead-in groups DB, APEX, AHF, GLM and ORDS as "20 new security patches for Oracle Database Products".\n')

A('### 1.2 Oracle\'s own per-family patch and unauthenticated-row statements (sum of "remotely exploitable without authentication" = 303 rows; Oracle states no grand total)\n')
txt = body(OR)
fam_rows = []
for m in re.finditer(r'(This Critical Security Patch Update contains (?:\d+|no) new security patch(?:es)?(?:, plus additional third party patches noted below,)? for ([^.\n]*?)\.)[\xa0 ]+((?:\d+ of these vulnerabilities|Both of these vulnerabilities|All of these vulnerabilities|This vulnerability) (?:may be remotely exploitable without authentication|is not remotely exploitable without authentication))', txt):
    s1, fam, s2 = m.group(1), m.group(2), m.group(3)
    if '\n' in s1 or '\n' in s2:
        continue
    fam_rows.append((fam, s1, s2))
A('| family (Oracle section) | patches: Oracle sentence (verbatim) | unauthenticated: Oracle sentence (verbatim) |')
A('|---|---|---|')
tot_unauth = 0
for fam, s1, s2 in fam_rows:
    ok = chk(OR, s1) and chk(OR, s2)
    A('| %s | "%s" | "%s"%s |' % (esc(fam), esc(s1), esc(s2), '' if ok else ' **[NOT FOUND]**'))
A('')
A('(All sentences from ' + U_ADV + ', saved `oracle/cspunov2026.extract.md`. The page puts a non-breaking space between the two sentences, so quote them separately.)')
A('')

A('### 1.3 Rows reachable over the network WITHOUT authentication at CVSS 3.1 >= 9.0 (56 rows, 51 CVEs), grouped by product family\n')
A('Reading key. "Oracle wording" is the verbatim sentence from Oracle\'s English text version of the matrices (' + U_VB + '); the matrix cells (Protocol, "Remote Exploit without Auth.? = Yes", Privs Req\'d = None, UI) are from ' + U_ADV + ' and were verified row by row against the saved extract. Oracle publishes no exploit prerequisites beyond the matrix: no default-config statement, no "feature must be enabled" note and no Notes-column entry exists on any of these 56 rows (the Notes column is non-empty only on the 11 Java SE rows). UI = "Required" rows are marked; they remain unauthenticated and network-reachable but need a person other than the attacker to act.\n')

order = [('Fusion Middleware', 'Oracle Fusion Middleware (WebLogic Server, Access Manager, Platform Security for Java, SDP, ADF, Managed File Transfer)'),
         ('Analytics', 'Oracle Analytics'),
         ('E-Business Suite', 'Oracle E-Business Suite'),
         ('PeopleSoft', 'Oracle PeopleSoft'),
         ('Database (APEX)', 'Oracle Database Products: APEX'),
         ('Database (ORDS)', 'Oracle Database Products: REST Data Services'),
         ('Database (AHF)', 'Oracle Database Products: Autonomous Health Framework'),
         ('Hyperion', 'Oracle Hyperion'),
         ('Supply Chain', 'Oracle Supply Chain'),
         ('Communications', 'Oracle Communications'),
         ('Enterprise Manager', 'Oracle Enterprise Manager'),
         ('MySQL', 'Oracle MySQL')]
tsv = ['family\tcve\tproduct\tcomponent\tprotocol\tscore\tvector\tunauth\tprivileges\tsupported_versions\toracle_wording']
vrf = 0
for key, label in order:
    rs = sorted([r for r in hi if r['family'] == key and r['unauth'] == 'Yes'], key=lambda r: (-r['score'], r['cve']))
    if not rs:
        continue
    A('**%s** (%d rows)\n' % (label, len(rs)))
    A('| CVE | product / component | protocol | CVSS | vector | supported versions affected | Oracle wording (verbatim) |')
    A('|---|---|---|---|---|---|---|')
    for r in rs:
        pref = '| %s | %s | %s | %s | %s | %s |' % (r['cve'], r['product'], r['component'], r['protocol'], r['unauth'], ('%.1f' % r['score']))
        ok1 = chk(OR, pref)
        ok2 = chk(VB, r['verbose'])
        flag = '' if (ok1 and ok2) else ' **[CHECK FAILED]**'
        ui = ' (UI Required)' if r['ui'] == 'Required' else ''
        sc = ' (scope change)' if r['scope'] == 'Changed' else ''
        A('| %s | %s / %s | %s | %.1f%s%s | %s | %s | "%s"%s |' % (r['cve'], esc(r['product']), esc(r['component']), esc(r['protocol']), r['score'], ui, sc, r['vector'].replace('CVSS:3.1/', ''), esc(r['versions']), esc(r['verbose']), flag))
        tsv.append('\t'.join([key, r['cve'], r['product'], r['component'], r['protocol'], '%.1f' % r['score'], r['vector'], r['unauth'], r['pr'], r['versions'], r['verbose']]))
    A('')
open(ROOT + 'oracle/oracle-unauth-ge9.tsv', 'w').write('\n'.join(tsv) + '\n')
A('Machine-readable copy of the 56 rows: `work/2026-11-18T0356Z-intel/bodies/FU2/oracle/oracle-unauth-ge9.tsv`.\n')
A('Note on scope: "unauthenticated" here is Oracle\'s "Remote Exploit without Auth.? = Yes" column; every one of the 56 rows also has Attack Vector Network, Attack Complexity Low and Privs Req\'d None (checked), and 52 of 56 also have User Interaction None. The four UI-Required rows are CVE-2026-114856 (ORDS General, 9.6), CVE-2026-114785 (Hyperion Planning Security, 9.6), CVE-2026-115139 and CVE-2026-114956 (Hyperion, 9.3).\n')

A('### 1.4 Rows at >= 9.0 that are NOT unauthenticated (6 rows) - do not count these as pre-auth\n')
A('| CVE | product / component | CVSS | Oracle\'s privilege wording (verbatim) |')
A('|---|---|---|---|')
for r in sorted([r for r in hi if r['unauth'] != 'Yes'], key=lambda r: (-r['score'], r['cve'])):
    ok = chk(VB, r['verbose'])
    A('| %s | %s / %s (%s) | %.1f | "%s"%s |' % (r['cve'], esc(r['product']), esc(r['component']), r['family'], r['score'], esc(r['verbose']), '' if ok else ' **[CHECK FAILED]**'))
A('')
A('Database 9.9 rows confirmed: Oracle\'s matrix has a "Package and/or Privilege Required" column for the Database table and lists "Create Session" for all three, with "Remote Exploit without Auth.? = No":\n')
A(table([
 ('CVE-2026-114819 Oracle Text 9.9: needs Create Session, not unauthenticated', U_ADV, OR, '| CVE-2026-114819 | Oracle Text | Create Session | Oracle Net | No | 9.9 |'),
 ('CVE-2026-114848 Oracle Text 9.9: needs Create Session, not unauthenticated', U_ADV, OR, '| CVE-2026-114848 | Oracle Text | Create Session | Oracle Net | No | 9.9 |'),
 ('CVE-2026-114822 RDBMS 9.9: needs Create Session, not unauthenticated', U_ADV, OR, '| CVE-2026-114822 | RDBMS | Create Session | Oracle Net | No | 9.9 |'),
 ('Oracle: only 3 Database Products-table rows are unauthenticated (these are the third-party OpenSSL 7.5, Python 7.4, Apache HttpClient 4.3 rows)', U_ADV, OR, '3 of these vulnerabilities may be remotely exploitable without authentication'),
 ('Oracle wording for the 9.9 Oracle Text row', U_VB, VB, 'Easily exploitable vulnerability allows low privileged attacker having Create Session privilege with network access via Oracle Net to compromise Oracle Text.'),
 ('Unauthenticated Database-table rows are third-party components, max 7.5', U_ADV, OR, '| CVE-2026-72897 | RDBMS (OpenSSL) | None | TLS | Yes | 7.5 |'),
]))
A('')
A('Pre-release headline check (the "22 unauthenticated EBS rows" and "unauthenticated Database/APEX rows up to 9.9" came from the 2026-11-12 pre-release page as recorded in `state/coverage_backlog.md` row B of run 2026-11-17T0355Z; that page was replaced by the published advisory, so the pre-release text itself could not be re-read and only the published numbers are confirmed here):\n')
A(table([
 ('E-Business Suite: published page says 71 patches, 19 unauthenticated (NOT 22)', U_ADV, OR, '19 of these vulnerabilities may be remotely exploitable without authentication'),
 ('Tenable independently counts 19 unauthenticated EBS rows', U_TN, TN, '| Oracle E-Business Suite | 71 | 19 |'),
 ('APEX: both rows unauthenticated at 9.8 (not 9.9)', U_ADV, OR, 'Both of these vulnerabilities may be remotely exploitable without authentication'),
 ('APEX row CVE-2026-114849: 9.8, HTTPS, supported 24.1.22, 24.2.21, 26.1.5, 26.2.0', U_ADV, OR, '| CVE-2026-114849 | Oracle APEX | General | HTTPS | Yes | 9.8 |'),
]))
A('')

A('### 1.5 Brotli CVE-2026-111497 (CISA KEV) - three rows\n')
A(table([
 ('Row 1: Communications Diameter Signaling Router, component labelled PMAC (Node.js), 9.8, HTTP, unauthenticated; supported 9.0.0.0.0-9.3.0.0.0', U_ADV, OR, '| CVE-2026-111497 | Oracle Communications Diameter Signaling Router | PMAC (Node.js) | HTTP | Yes | 9.8 |'),
 ('Row 2: Communications Unified Assurance, component labelled Core (Brotli), 9.8, HTTP, unauthenticated; supported 6.1.1-7.0.0 (the only row that says "Brotli")', U_ADV, OR, '| CVE-2026-111497 | Oracle Communications Unified Assurance | Core (Brotli) | HTTP | Yes | 9.8 |'),
 ('Row 3: PeopleSoft PeopleTools, component labelled OpenSearch Dashboards (Node.js), 9.8, HTTP, unauthenticated; supported 8.61-8.63', U_ADV, OR, '| CVE-2026-111497 | PeopleSoft Enterprise PeopleTools | OpenSearch Dashboards (Node.js) | HTTP | Yes | 9.8 |'),
 ('Oracle states the same CVE id appears in every matrix it affects', U_ADV, OR, 'A vulnerability that affects multiple products will appear with the same CVE ID in all risk matrices.'),
 ('Footnote under the Communications table', U_ADV, OR, 'The patch for CVE-2026-111497 also addresses CVE-2026-105482, CVE-2026-105483, and CVE-2026-106069.'),
 ('Footnote under the PeopleSoft table', U_ADV, OR, 'The patch for CVE-2026-111497 also addresses CVE-2026-105481, CVE-2026-105482, CVE-2026-105483, CVE-2026-106069, CVE-2026-106070, CVE-2026-106071, CVE-2026-106072, CVE-2026-106073, and CVE-2026-106074.'),
 ('CISA KEV: CVE-2026-111497 = Google Brotli, added 2026-10-27, ransomware use Unknown', U_KEV, KV, 'KEV CVE-2026-111497 | vendorProject: Google | product: Brotli | vulnerabilityName: Google Brotli Unchecked Return Value Vulnerability | dateAdded: 2026-10-27 | knownRansomwareCampaignUse: Unknown'),
]))
A('')
A('Caveat: only the Unified Assurance row names Brotli; Oracle labels the other two rows "Node.js". Tying all three rows to the Brotli flaw rests on the shared CVE id plus CISA KEV naming CVE-2026-111497 as Google Brotli, not on any Oracle sentence about Node.js bundling Brotli. Oracle does not say the KEV-listed flaw is exploited in Oracle products. It is the only one of the 640 matrix CVEs on KEV (checked by set intersection against the 1782-entry catalogue fetched 2026-11-18); `oracle/cisa-kev.json`.\n')

A('### 1.6 Java SE and CVE-2026-114938 (Java4Shell)\n')
A(table([
 ('Java SE section: 11 patches, all flagged remotely exploitable without authentication', U_ADV, OR, 'All of these vulnerabilities may be remotely exploitable without authentication'),
 ('The matrix INCLUDES CVE-2026-114938: component Compiler, protocol Multiple, unauthenticated, CVSS 8.1 (so it is not in the >= 9.0 set)', U_ADV, OR, '| CVE-2026-114938 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Compiler | Multiple | Yes | 8.1 |'),
 ('Oracle wording for the row ("Difficult to exploit"; Attack Complexity High)', U_VB, VB, 'Difficult to exploit vulnerability allows unauthenticated attacker with network access via multiple protocols to compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.'),
 ('Oracle wording: takeover', U_VB, VB, 'Successful attacks of this vulnerability can result in takeover of Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.'),
 ('Supported versions Oracle lists for the row (note: plain 8u511b33 and 11.0.33.0.3 are NOT in this row; 8u511b33-perf, 17, 21, 25 and 27 are)', U_VB, VB, 'Supported versions that are affected are Oracle Java SE: 8u511b33-perf, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3; Oracle GraalVM for JDK: 17.0.21.0.3 and 21.0.13.0.3; Oracle GraalVM Enterprise Edition: 21.3.20.0.3.'),
 ('Oracle note 1 attached to the row (server-side web-service exposure, not only applets)', U_ADV, OR, '1. This vulnerability can only be exploited by supplying data to APIs in the specified Component without using Untrusted Java Web Start applications or Untrusted Java applets, such as through a web service.'),
 ('Oracle: Java scores assume applet/Web Start user has administrator privileges', U_ADV, OR, 'The CVSS scores below assume that a user running a Java applet or Java Web Start application has administrator privileges'),
 ('Highest Java SE row in this CSPU is 8.1; there is no Java SE row at >= 9.0', U_ADV, OR, '| CVE-2026-114938 | Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition | Compiler | Multiple | Yes | 8.1 |'),
 ('Tenable: CVSS 8.1, details expected, FAQ planned', U_TN, TN, 'technical details about this vulnerability are expected to be released soon'),
 ('Oracle credits the finders of CVE-2026-114938', U_ADV, OR, 'Albert Yang: CVE-2026-114938'),
 ('Oracle credits the finders of CVE-2026-114938 (second credit)', U_ADV, OR, 'Quang Luong of Calif.io: CVE-2026-114938'),
]))
A('')

A('### 1.7 Exploitation, disclosure and write-up status of the >= 9.0 rows\n')
A(table([
 ('Oracle flags no row as exploited or publicly disclosed; its only exploitation language is generic (about already-patched flaws and unpatched customers)', U_ADV, OR, 'Oracle continues to periodically receive reports of attempts to maliciously exploit vulnerabilities for which Oracle has already released security patches.'),
 ('Oracle generic sentence, second half', U_ADV, OR, 'it has been reported that attackers have been successful because targeted customers had failed to apply available Oracle patches'),
 ('Oracle reminds customers of four earlier Security Alerts (Oct 21: CVE-2026-91403; Oct 24: CVE-2026-114820; Oct 25: CVE-2026-109618 and CVE-2026-109619); these are NOT new rows except CVE-2026-114820', U_ADV, OR, 'Oracle released Security Alerts on October 21, 2026 for'),
 ('CVE-2026-114820 appears in three Communications rows at 9.1 (Element Manager, Unified Assurance, Unified Inventory Management)', U_ADV, OR, '| CVE-2026-114820 | Oracle Communications Element Manager | Core (Java) | HTTPS | Yes | 9.1 |'),
 ('Oracle Security Alert for CVE-2026-114820 describes it as removal of root CA certificates (eMudhra), not an exploited code flaw', 'https://www.oracle.com/security-alerts/alert-cve-2026-114820.html', 'oracle/alert-cve-2026-114820.extract.md', 'This Security Alert addresses CVE-2026-114820 by providing Java updates that remove the set of impacted root CA certificates related to eMudhra.'),
 ('CISA KEV: PHP CVE-2026-109618 and CVE-2026-109619 (Oracle Security Alert of Oct 25) are on KEV since 2026-10-26; they are not rows of this CSPU (set intersection)', U_KEV, 'oracle/cisa-kev.json', '"vulnerabilityName": "PHP Memory Corruption Vulnerability"'),
 ('Footnote: the patch for the EBS row CVE-2026-114918 ALSO ADDRESSES CVE-2025-61882 (KEV, Cl0p-era EBS flaw)', U_ADV, OR, 'The patch for CVE-2026-114918 also addresses CVE-2025-61882.'),
 ('That EBS row: Oracle Concurrent Processing / BI Publisher Integration, 8.7, high privileges required (not unauthenticated)', U_ADV, OR, '| CVE-2026-114918 | Oracle Concurrent Processing | BI Publisher Integration | HTTP | No | 8.7 |'),
 ('Oracle wording for it: "high privileged attacker"', U_VB, VB, 'Easily exploitable vulnerability allows high privileged attacker with network access via HTTP to compromise Oracle Concurrent Processing.'),
 ('CISA KEV: CVE-2025-61882 = Oracle E-Business Suite, added 2025-10-06, ransomware use Known', U_KEV, KV, 'KEV CVE-2025-61882 | vendorProject: Oracle | product: E-Business Suite | vulnerabilityName: Oracle E-Business Suite Unspecified Vulnerability | dateAdded: 2025-10-06 | knownRansomwareCampaignUse: Known'),
 ('Oracle credits ZDI-affiliated researchers for CVE-2026-114849 (APEX/ORDS, 9.8): an anonymous researcher', U_ADV, OR, "An Anonymous researcher working with Trend Micro's Zero Day Initiative: CVE-2026-114849"),
 ('Oracle credits ZDI-affiliated researchers for CVE-2026-114850 (APEX 9.8) and CVE-2026-114822 (RDBMS 9.9)', U_ADV, OR, "Ikotas Labs working with Trend Micro's Zero Day Initiative: CVE-2026-114822, CVE-2026-114850"),
 ('Oracle credit for CVE-2026-114835 (Access Manager Admin Console 10.0)', U_ADV, OR, 'Phuoc Pham & Son Tran from starfishsec.com: CVE-2026-114835'),
 ('Oracle credit for CVE-2026-114819 (Oracle Text 9.9, needs Create Session)', U_ADV, OR, 'Zheng Yu of depthfirst: CVE-2026-114819'),
 ('Oracle credit for CVE-2026-114925 (EBS Applications Framework REST Services 9.8)', U_ADV, OR, 'Tomais Williamson: CVE-2026-114925'),
 ('NCSC-NL covers only the Java row so far (advisory NCSC-2026-0495, published 2026-11-17 21:55Z)', 'https://advisories.ncsc.nl/advisory?id=NCSC-2026-0495', 'oracle/ncsc-nl-recent.txt', 'In dit beveiligingsadvies gaan we uitsluitend in op CVE-2026-114938, de rest van de kwetsbaarheden zal hierin later worden aangevuld.'),
 ('NCSC-NL: Java compiler flaw not easy to exploit because of multiple requirements', 'https://advisories.ncsc.nl/advisory?id=NCSC-2026-0495', 'oracle/ncsc-nl-recent.txt', 'niet eenvoudig te misbruiken'),
 ('NCSC-CH Security Hub post 13198 is the Java4Shell advisory (edited into it from the pre-release CSPU text)', 'https://security-hub.ncsc.admin.ch/#/posts/13198', 'oracle/ncsc-csh-recent.txt', '[Advisory] Java4Shell (CVE-2026-114938): Critical Remote Code Execution, Patch Now'),
]))
A('')
A('Absence checks (all fetched 2026-11-18 between 04:40Z and 04:56Z; an absence is "not found", never "does not exist"):\n')
A('- BSI CERT-Bund RSS (`bsi-rss`, saved `oracle/bsi-rss.txt`): the only Oracle items are [UPDATE] entries on older WID-SEC ids (Java SE x4, MySQL x3, all pubDate 2026-11-17 07:27-11:07Z); no new Oracle CSPU advisory yet.')
A('- CERT-EU (`cert-eu recent 20` returned its 10 most recent advisories, newest dated 2026-11-12, `oracle/cert-eu-recent.txt`) and CERT-FR (`cert-fr avis-recent 30`, 30 avis dated 2026-11-13..17, `oracle/cert-fr-recent.txt`): no Oracle CSPU item.')
A('- ENISA EUVD: `api/search?text=oracle&fromDate=2026-11-16&toDate=2026-11-18` returns 583 Oracle records (all 6 pages read, `oracle/euvd-oracle-search*.json`); none carries `exploitedSince`; the EUVD "exploited" feed (`oracle/euvd-exploited.json`) lists none of the 640 CSPU CVEs.')
A('- CISA KEV: only CVE-2026-111497 of the 640 (above). Neither CVE-2025-61882 nor CVE-2023-44487 is a CSPU row; they appear only in "also addresses" footnotes (CVE-2026-27135 Communications BRM nghttp2 row 7.5 also addresses CVE-2023-44487).')
A('- Public write-ups: WebSearch queries for CVE-2026-114835 / CVE-2026-91470 / CVE-2026-114849 / CVE-2026-114850 / CVE-2026-114819 / "starfishsec" / "depthfirst" / ZDI / Rapid7 / Qualys returned no page naming these ids (search engine index of the last 36 h is thin; this is weak evidence of absence). Tenable lists its plugins as "will appear" (not yet). No Rapid7, ZDI, Qualys or SANS write-up found for the CSPU.\n')

A('### 1.8 Strongest rows for a Swiss public-sector defender (analyst ranking on stated facts; the ranking is an assessment of this read, not an Oracle or third-party claim)\n')
A('Ranking facts used: (a) Oracle marks the row unauthenticated, network, low complexity, no privileges; (b) Oracle\'s CVSS 3.1 score and whether "scope change" is flagged; (c) the component is a gateway, identity or web-facing tier that is commonly published (assessment); (d) supported versions are current branches, i.e. patches exist for what is deployed; (e) no row has a public write-up or exploitation report at fetch time, so none can be ranked up on exploitation.\n')
A('1. **WebLogic Server** (12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0, 15.1.1.0.0): CVE-2026-91569 TopLink Integration HTTP 10.0 scope change; CVE-2026-91470 Core T3, IIOP 9.8; CVE-2026-91456 Core SOAP 9.8; CVE-2026-91570 and CVE-2026-91583 TopLink HTTP 9.8; CVE-2026-91585 TopLink TCP 9.8; CVE-2026-91469 Core HTTP 9.4. Oracle wording for each: "unauthenticated attacker with network access" ending in "takeover of Oracle WebLogic Server" (CVE-2026-91470 row verbatim: "Easily exploitable vulnerability allows unauthenticated attacker with network access via T3, IIOP to compromise Oracle WebLogic Server."). Seven unauthenticated rows on one product; T3/IIOP is the one with a protocol-level interim control (block the protocol), which Oracle\'s generic text endorses.')
A('2. **Oracle Access Manager** (12.2.1.4.0, 14.1.2.1.0): CVE-2026-114835 Admin Console 10.0, CVE-2026-91500 and CVE-2026-91510 Authentication Engine 10.0, CVE-2026-91507 Authentication Engine 9.3, all HTTP, all "scope change". Identity/SSO tier (assessment: large blast radius; Oracle itself flags that "attacks may significantly impact additional products"). Oracle\'s credit line names starfishsec.com for CVE-2026-114835.')
A('3. **Oracle Platform Security for Java** (12.2.1.4.0, 14.1.2.0.0): CVE-2026-114824 "Centralized Thirdparty Jars", HTTP, 10.0 scope change. It is a library component present under WebLogic/Fusion Middleware domains (assessment); Oracle states no prerequisites.')
A('4. **Oracle Business Intelligence Enterprise Edition**: CVE-2026-114784 Platform Security, HTTP, 10.0 scope change; the matrix row lists 8.2.0.0.0 and 26.01.0.0.0 only (the affected-products table also lists 12.2.1.4.0 for BI EE, so 12.2.1.4.0 is NOT in this CVE row: check before asserting).')
A('5. **E-Business Suite 12.2.3-12.2.15** (6 rows): CVE-2026-114880 and CVE-2026-114881 Document Management and Collaboration/Attachments (9.8, 9.1), CVE-2026-114924 Application Object Library/Core (9.8), CVE-2026-114925 Applications Framework/REST Services (9.8), CVE-2026-114863 Universal Work Queue/Media Integration issues (9.8), CVE-2026-101691 Mobile Field Service/Admin UI (9.3), all HTTP. ERP in cantonal and communal finance and HR (assessment). Context facts: CISA KEV lists EBS CVE-2025-61882 with ransomware use "Known", and this CSPU\'s footnote says the patch for the EBS row CVE-2026-114918 (needs high privileges) also addresses CVE-2025-61882.')
A('6. **APEX and ORDS**: CVE-2026-114849 (9.8; one id in the APEX row and the ORDS Core row), CVE-2026-114850 (APEX 9.8), CVE-2026-114856 (ORDS General 9.6, user interaction), all HTTPS; APEX supported 24.1.22, 24.2.21, 26.1.5, 26.2.0; ORDS 24.2.0-26.3.0. Oracle credits several researchers "working with Trend Micro\'s Zero Day Initiative" for -114849 and -114850 (whether ZDI will publish a technical advisory is an assessment from general practice, not from a source fetched here; no ZDI advisory found yet).')
A('7. **PeopleSoft PeopleTools 8.61-8.63**: CVE-2026-111497 (Node.js/OpenSearch Dashboards, 9.8, KEV via Brotli), CVE-2026-114934 Integration Broker 9.3 scope change, CVE-2026-114862 Weblogic 9.1.')
A('8. Lower on the list: Hyperion (11 unauthenticated rows, all 11.2.26.0.000, mostly HTTP/RMI; typically internal finance, assessment); Supply Chain/AutoVue (4 rows at 9.8, version 21.1.0, niche) and Agile PLM Tomcat HTTP/2 9.1; MySQL Shell (Python) 9.8 and MySQL Server/Cluster "Client programs" 9.1 over the MySQL protocol; Enterprise Manager Agent Next Gen (Eclipse Jetty) 9.1; Autonomous Health Framework 9.1; Communications (telecom estates: DSR, Unified Assurance, Element Manager, UIM); Service Delivery Platform SOAP 9.8; Managed File Transfer (Bouncy Castle) 9.1; ADF Security Framework 9.1.')
A('9. Not in the >= 9.0 set although often asked about: Oracle HTTP Server (only CVE-2026-9545, WebLogic Server Proxy Plug-in (curl), 7.5); Java SE (max 8.1); Database Server unauthenticated rows (max 7.5).\n')

A('### 1.9 Contradictions with, and unsupported statements in, the first pass (item 6)\n')
A('- CONFIRMED: 655 patches; 62 rows >= 9.0 / 57 CVEs; 56 unauthenticated rows / 51 CVEs; family counts (Hyperion 107, Fusion Middleware 53, Supply Chain 36, Communications 21, EBS 19, Analytics 9, Siebel 9, PeopleSoft 6, ORDS 5, MySQL 3, Database 3, Enterprise Manager 3, Virtualization 3, Java SE 11, APEX 2); EBS 19 (not 22); Database 9.9 rows need Create Session; the three Brotli rows; Java SE matrix includes CVE-2026-114938 at 8.1.')
A('- NOT SUPPORTED AS WORDED: "655 new security patches across 21 product families" attributes "21" to the advisory. Oracle writes "across the product families listed below" and never counts them; 21 is Tenable\'s count (and equals the number of risk-matrix sections). "640 CVEs" is likewise Tenable\'s figure (reproduced here from the rows), not an Oracle statement.')
A('- NOT SUPPORTED AS WORDED: the headline lumps "WebLogic T3/IIOP and TopLink ... at 10.0". Only the TopLink Integration row CVE-2026-91569 is 10.0; the T3/IIOP row CVE-2026-91470 is 9.8. The six 10.0 rows are CVE-2026-114835, -91500, -91510 (Access Manager), -114824 (Platform Security for Java), -91569 (WebLogic TopLink), -114784 (BI EE).')
A('- "none flagged exploited or publicly disclosed by Oracle": supported only in the sense that the page contains no such flag at all (Oracle\'s matrices have no exploited/disclosed column). The page does not say "not exploited"; it carries the generic warning quoted in 1.7.')
A('- The first pass lists the unauthenticated >= 9.0 rows by family but omits Commerce (6 unauthenticated rows, none >= 9.0), Construction and Engineering (2, none >= 9.0), Application Testing Suite (1) and Financial Services (1); none of these has a row >= 9.0, so nothing material is lost.')
A('- Not in the first pass: the "also addresses CVE-2025-61882" footnote (1.7) and the EUVD/NCSC/BSI absence checks.\n')
A('### 1.10 Open gaps (Oracle)\n')
A('- Pre-release page text (652 patches; EBS 22; DB/APEX 9.9 unauthenticated) not re-readable; only `state/coverage_backlog.md` records it.')
A('- Oracle publishes no per-CVE exploit prerequisites, default-configuration statements or patch-number mapping on the page itself (patch numbers sit in My Oracle Support notes CPU433, CPU454, KA923, KA1182, which need a login).')
A('- No third-party exploit or write-up found for any >= 9.0 row except the Java row; check again at the next fire, especially ZDI advisories for CVE-2026-114849/-114850/-114822/-114848 and any Calif/depthfirst/starfishsec posts.\n')

SECTION = '\n'.join(out)
