import re,sys
sys.path.insert(0,'tools')
def load(p): return open(p,encoding='utf-8').read()
def save(p,t): open(p,'w',encoding='utf-8').write(t)
def rep(t,old,new,count=1):
    assert t.count(old)==count,(t.count(old),old[:90]); return t.replace(old,new)
CS='https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq'
# ---------------- Cisco
p='entries/2026-10-28/cisco-php2shell-expressway-urwb-duo-access-gateway-fixes.md'
t=load(p)
old_aff='Expressway Series and Expressway Select Series, Ultra-Reliable Wireless Backhaul and Unified Industrial Wireless Software, Duo Access Gateway and, with an administrator login, Identity Services Engine Portal Builder; version ranges are in the Cisco bug records CSCwx37062 and CSCwx37073'
new_aff='Expressway Series and Expressway Select Series, Ultra-Reliable Wireless Backhaul and Unified Industrial Wireless Software, Duo Access Gateway and Identity Services Engine Portal Builder; the advisory gives no version ranges (its bug records CSCwx37062 and CSCwx37073 carry platform-specific information)'
t=rep(t,old_aff,new_aff,2)
t=rep(t,'''  statement that it knows of no malicious use. The flaws themselves are in the PHP runtime and are covered by the entries listed under
  references. The advisory carries no CVSS score except for ISE Portal Builder, and gives no affected-version ranges; those sit in the bug
  records, which were not read. The listing of both PHP flaws in CISA's Known Exploited Vulnerabilities catalog comes from the catalog itself.''',
'''  statement that it knows of no malicious use. The flaws themselves are in the PHP runtime. The advisory carries no CVSS score except the 6.6
  it gives for the Ultra-Reliable Wireless Backhaul row, and no affected-version ranges; its bug records, which were not read, carry
  platform-specific information, workarounds and fixed releases. The listing of both PHP flaws in CISA's Known Exploited Vulnerabilities
  catalog comes from the catalog itself.''')
t=rep(t,'''  - quote: "For this product, the attacker must be authenticated as an administrator to exploit this vulnerability."
    publisher: "Cisco PSIRT (cisco-sa-php-october26-Jj384Daq, version 1.8)"''','''  - quote: "For this product, the attacker must be authenticated as an administrator to exploit this vulnerability."
    publisher: "Cisco PSIRT (cisco-sa-php-october26-Jj384Daq, version 1.8, footnote to the Ultra-Reliable Wireless Backhaul row)"''')
t=rep(t,"lists four products as affected by CVE-2026-109618 and CVE-2026-109619, the PHP flaws behind PHP2Shell","lists Expressway, Ultra-Reliable Wireless Backhaul, Duo Access Gateway and ISE Portal Builder as affected by CVE-2026-109618 and CVE-2026-109619, the PHP flaws behind PHP2Shell")
t=rep(t,"have 27.1.1, listed for March 2027, and a workaround; Duo Access Gateway is fixed in 3.2.0; and ISE Portal Builder is offline for remediation, where the attacker must be authenticated as an administrator, which lowers its CVSS 3.1 score to 6.6 (",
 "have 27.1.1, listed for March 2027, and a workaround, and there the attacker must be authenticated as an administrator, which lowers the CVSS 3.1 score to 6.6; Duo Access Gateway is fixed in 3.2.0; and ISE Portal Builder is offline for remediation (")
t=rep(t,"The advisory gives no affected-version ranges and no workaround steps, which sit in the bug records, and says a product it does not list is not affected","The advisory gives no affected-version ranges and no workaround steps; its bug records carry platform-specific information, workarounds and fixed releases, and a product it does not list is, in Cisco's review, not affected")
t=rep(t,"the advisory names no version-check command and no component that runs the PHP, so the Cisco bug records CSCwx37062 and CSCwx37073 carry the affected-release detail (","the advisory names no version-check command, no component that runs the PHP and no affected-version ranges; its bug records CSCwx37062 and CSCwx37073 carry platform-specific information (")
t=rep(t,"**Detection:** Cisco publishes no indicator and reports no attack on its products, so the only telemetry is the generic PHP2Shell pattern in web access logs and process telemetry described in the PHP entry.",
 "**Detection:** Cisco publishes no indicator and reports no attack on its products, but lists Snort rules 67359 and 67360 as action links for the advisory ([Cisco PSIRT, 2026-10-27]("+CS+")); beyond that, the generic PHP2Shell pattern applies: multipart POST requests to PHP endpoints from unfamiliar sources, worker crashes and processes started by the web worker account.")
save(p,t)
# ---------------- HPE
p='entries/2026-10-28/hpe-clearpass-php2shell-hotfixes-hpesbnw05171.md'
t=load(p)
HP='https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json'
t=rep(t,'''  public access until the hotfixed versions run; the bulletin says nothing about exploitation of ClearPass, although CISA added both flaws
  to its Known Exploited Vulnerabilities catalog on 2026-10-26.''','''  public access until ClearPass runs a version providing some level of mitigation, which it names as 6.14.1 and 6.11.16; the bulletin says
  nothing about exploitation of ClearPass, although CISA added both flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26.''')
t=rep(t,'''  are covered by the entry listed under references. The listing of both flaws in CISA's catalog comes from the catalog itself.''','''  are covered by the entry listed under references. The bulletin is inconsistent: its workaround text names 6.14.1 and 6.11.16 as versions
  providing some level of mitigation, while its affected list covers 6.14.1 and 6.11.16 and below and its remediation names hotfix patches
  for both. The listing of both flaws in CISA's catalog comes from the catalog itself.''')
t=rep(t,'''  - quote: "customers are asked to consider removing guest portals and all management interfaces from public access"''','''  - quote: "a version providing some level of mitigation"
    publisher: "HPE Networking (CSAF advisory HPESBNW05171, revision 2)"
    source_url: "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
  - quote: "customers are asked to consider removing guest portals and all management interfaces from public access"''')
t=rep(t,"until the ClearPass instances run the hotfixed 6.14.1 or 6.11.16, which it describes as versions providing some level of mitigation (",
 "until ClearPass instances have been upgraded to \"a version providing some level of mitigation\", which it names as 6.14.1 and 6.11.16, although the same bulletin lists 6.14.1 and 6.11.16 and below as affected and names the hotfix patches as the remediation (")
t=rep(t,"**Detection:** HPE gives no indicator and no post-patch check, so the only telemetry is the generic PHP2Shell pattern described in the PHP entry, on the web access and process logs of the ClearPass nodes.",
 "**Detection:** HPE gives no indicator and no post-patch check, so the only telemetry is the generic PHP2Shell pattern on the ClearPass nodes: multipart POST requests to PHP endpoints from unfamiliar sources, worker crashes and processes started by the web worker account.")
t=rep(t,"the hotfix is described as a mitigation level, so check HPE's bulletin for a full fix before treating the exposure as closed (",
 "the guest portal is the first surface to take off public networks (")
t=rep(t,"**Defender takeaway:** install the hotfix on every node now and treat any guest portal or management interface that was reachable from untrusted networks as the first to restrict;","**Defender takeaway:** install the hotfix patch for 6.14.1 or 6.11.16 on every node now, the remediation HPE's bulletin names, and treat any guest portal or management interface that was reachable from untrusted networks as the first to restrict;")
save(p,t)
# ---------------- Gridbox
p='entries/2026-10-28/cve-2026-102788-102789-balbooa-gridbox-joomla-unauth-sqli.md'
t=load(p)
t=rep(t,"CVE-2026-102788 is in the sort-by URL parameter of store and category post lists: Balbooa added a strict allowlist validation in GridboxHelper::getBlogPosts(), which previously inserted the value into the query's ORDER BY clause. CVE-2026-102789",
 "CVE-2026-102788 is in the sort-by URL parameter of store and category post lists, for which Balbooa added a strict allowlist validation in GridboxHelper::getBlogPosts(); mySites.guru says the value previously went into the ORDER BY part of the database query ([mySites.guru, 2026-10-27](https://mysites.guru/blog/gridbox-2-20-4-2-sql-injection-fixes/)). CVE-2026-102789")
save(p,t)
# ---------------- DeadTag
p='entries/2026-10-28/deadtag-expired-tag-domains-coruna-darksword-iphone-kits.md'
t=load(p)
RU='https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/'
IV='https://www.iverify.com/blog/malvertising-coruna-darksword-iphone-exploits'
t=rep(t,"The script is about 2 KB, does nothing for bots, scanners or repeat visits from data-centre addresses, asks the operator's server what to do with each visitor and redirects the chosen ones;",
 "The script is about 2 KB, does nothing for search engines, scanners and other bots, asks the operator's server what to do with each visitor and redirects the chosen ones, and Report URI found that the operator stopped answering when it probed from data-centre addresses or returned too often from residential ones;")
t=rep(t,"regions: [global]","regions: [global, europe]")
t=rep(t,'entities: ["campaign:deadtag", "tool:coruna", "tool:darksword", "product:apple-ios"]','entities: ["campaign:deadtag", "tool:coruna", "tool:darksword"]')
t=rep(t,'affected_products: ["Apple iOS"]','affected_products: []')
t=rep(t,'references: ["2026-09-30/cve-2026-86950-apple-coregraphics-zero-day-kev"]','references: []')
t=rep(t,'''  - quote: "iVerify caught the P7 variant of DarkSword delivered through a malicious Instagram ad themed around the World Cup."''','''  - quote: "Based on current findings, DeadTag appears to be mostly focused on European domains versus .com"
    publisher: "iVerify Threat Intelligence Team"
    source_url: "https://www.iverify.com/blog/malvertising-coruna-darksword-iphone-exploits"
  - quote: "iVerify caught the P7 variant of DarkSword delivered through a malicious Instagram ad themed around the World Cup."''')
t=rep(t,"iVerify saw the P7 variant reach an employee's device","iVerify reads DeadTag as mostly focused on European domains rather than .com ([iVerify, 2026-10-21]("+IV+")), and saw the P7 variant reach an employee's device")
t=rep(t,'''  - "Audit the external script references on every public website your organisation, its agencies and its hosting suppliers run, and remove each whose provider has shut down, because DeadTag buys exactly those expired domains; enforce a Content Security Policy that lists the script domains each site may load."''',
'''  - "List every third-party script domain on the public websites your organisation, its agencies and its hosting suppliers run, and remove or re-verify each whose provider has shut down, because DeadTag buys exactly those expired domains."''')
save(p,t)
# ---------------- ARA headline hedge
p='entries/2026-10-28/ara-region-lyss-limpachtal-safepay-darknet-publication.md'
t=load(p)
t=rep(t,'headline: "SafePay published about 49 GB from a Bernese wastewater association; the association declines to comment"','headline: "Inside IT: SafePay published about 49 GB from a Bernese wastewater association; the association declines to comment"')
save(p,t)
# ---------------- Manno headline hedge
p='entries/2026-09-30/manno-ti-commune-ransomware-safepay-claim.md'
t=load(p)
t=rep(t,'headline: "SafePay published about 30 GB from Manno: social-assistance files with AHV numbers; the commune makes no statement"','headline: "Inside IT: SafePay published about 30 GB from Manno, social-assistance files with AHV numbers; no commune statement"')
save(p,t)
import yaml
for p in ['entries/2026-10-28/ara-region-lyss-limpachtal-safepay-darknet-publication.md','entries/2026-09-30/manno-ti-commune-ransomware-safepay-claim.md','entries/2026-10-28/hpe-clearpass-php2shell-hotfixes-hpesbnw05171.md']:
    fm=yaml.safe_load(load(p).split('\n---\n',1)[0].split('---\n',1)[1]); print(len(fm['headline']),p.split('/')[-1][:30])
