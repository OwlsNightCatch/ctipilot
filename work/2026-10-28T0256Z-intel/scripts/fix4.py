import re
def edit(p, pairs):
    s = open(p).read()
    for o, n in pairs:
        if isinstance(o, re.Pattern):
            assert len(o.findall(s)) == 1, (p, o.pattern[:70]); s = o.sub(n, s)
        else:
            assert s.count(o) == 1, (p, s.count(o), o[:80]); s = s.replace(o, n)
    open(p, "w").write(s)

A = "entries/2026-10-28/cve-2026-48356-adobe-commerce-magento-upload-flaw-cisa-kev.md"
ADOBE = "https://www.adobe.com/trust/security/products/commerce/apsb26-73.html"
SANSEC = "https://sansec.io/research/magento-polyshell"
CNA = "https://cveawg.mitre.org/api/cve/CVE-2026-48356"
edit(A, [
 (re.compile(r"Adobe's fix reached\n  2\.4\.9 on 2026-05-12 and the supported lines through bulletin APSB26-73 on 2026-07-14, a bulletin that still says Adobe knows of no exploits;\n"),
  "Adobe's bulletin\n  APSB26-73 of 2026-07-14 names the 2026-jul builds as the fix and still says Adobe knows of no exploits, while Sansec says Magento 2.4.9 carried a fix on 2026-05-12;\n"),
 ('fixed: "2.4.9 (Sansec, 2026-05-12); the 2026-jul builds of the supported lines per bulletin APSB26-73, for example 2.4.9-2026-jul and 2.4.8-2026-jul (2026-07-14)"',
  'fixed: "the 2026-jul builds of every line per bulletin APSB26-73 (2026-07-14), 2.4.9-2026-jul included; Sansec says plain 2.4.9 of 2026-05-12 carries a fix, which Adobe\'s bulletin does not reflect"'),
 ("\nclosed_sources: []\n",
  '\n  - url: "%s"\n    publisher: "Adobe (CVE record, CNA container)"\n    date: "2026-10-28"\n    role: corroborating\nclosed_sources: []\n' % CNA),
 ("Sansec's account contradicts, and it scores the flaw 9.6 where Adobe's CVE record says 9.3 and rates it as needing user interaction, while\n  Sansec describes an anonymous upload.",
  "Sansec's account contradicts, and it lists 2.4.9 as affected where Sansec says 2.4.9 carries a fix. It scores the flaw 9.6 where Adobe's CVE\n  record says 9.3 and rates it as needing user interaction, while Sansec describes an anonymous upload."),
 ("Update every Magento Open Source and Adobe Commerce store to 2.4.9 or the 2026-jul fix in bulletin APSB26-73, then check",
  "Update every Magento Open Source and Adobe Commerce store, those on 2.4.9 included, to the 2026-jul fix in bulletin APSB26-73, then check"),
 ("Sansec dates Adobe's fix to Magento 2.4.9 on 2026-05-12, without a backport to the supported 2.4.8 and 2.4.7 lines, and the backport to those lines to 2026-07-14, in bulletin APSB26-73 ([Sansec, 2026-03-17](%s)). That bulletin rates the flaw Critical at CVSS 3.1 9.6, names the 2026-jul builds of Adobe Commerce, Magento Open Source and Adobe Commerce B2B as the fix, and still says Adobe is not aware of any exploits in the wild ([Adobe, 2026-07-14](%s))." % (SANSEC, ADOBE),
  "Sansec dates a fix in Magento 2.4.9 to 2026-05-12, without a backport to the supported 2.4.8 and 2.4.7 lines, and the backport to those lines to 2026-07-14, in bulletin APSB26-73 ([Sansec, 2026-03-17](%s)). That bulletin rates the flaw Critical at CVSS 3.1 9.6, lists 2.4.9 among the affected versions, names the 2026-jul builds, 2.4.9-2026-jul included, as the fix for Adobe Commerce and Magento Open Source, and still says Adobe is not aware of any exploits in the wild ([Adobe, 2026-07-14](%s)). Adobe's CVE record scores the flaw 9.3 with user interaction required and lists Adobe Commerce B2B among the affected products ([Adobe CVE record, 2026-10-28](%s))." % (SANSEC, ADOBE, CNA)),
 ("every Magento Open Source and Adobe Commerce store without the 2.4.9 or 2026-jul fix;", "every Magento Open Source and Adobe Commerce store without the 2026-jul fix, 2.4.9 included;"),
])

edit("entries/2026-10-26/cve-2026-111497-microsoft-net-oob-update-brotli-sockets-fix.md", [
 ("affecting source-build tarballs of .NET 10 and 11 and ASP.NET Core tarballs of .NET 8 and 9", "affecting ASP.NET Core tarballs of .NET 8 and 9 and source-built tarballs of .NET 8 to 11"),
])

NS = "https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/"
edit("entries/2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27.md", [
 ("because the NetScaler Management Portal uses PHP, that Citrix is working to upgrade the PHP package, and that all supported software versions are affected ([NetScaler Product Security, 2026-10-21](%s))." % NS,
  "because the NetScaler Management Portal uses PHP and that all supported software versions are affected; the post, last updated on 2026-10-27, now says Citrix has released fixes for all supported versions ([NetScaler Product Security, 2026-10-21](%s))." % NS),
])

PH = "https://security.paloaltonetworks.com/CVE-2026-109618"
edit("entries/2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619.md", [
 ("and Palo Alto's hotfixes for PAN-OS are due by 2026-10-30.", "and Palo Alto's remaining PAN-OS hotfixes are due by 2026-10-30 ([Palo Alto Networks, 2026-10-28](%s))." % PH),
])

IN = "https://www.inside-it.ch/tessiner-gemeinde-wird-opfer-von-cyberkriminellen-20260929"
edit("entries/2026-09-30/manno-ti-commune-ransomware-safepay-claim.md", [
 ('publisher: "Inside IT (teaser and lead paragraph from its feed; article body not readable)"', 'publisher: "Inside IT (article of 2026-09-29)"'),
 ("Inside IT's earlier article body is not readable, so only its teaser is\n  cited. The restoration sentence of the PDF notice is stored with a shifted font encoding, and its plain reading is that data and operations\n  were restored from existing backups during the afternoon.",
  "The notice's restoration sentence says that data and operations were restored from existing backups during the afternoon."),
 ("The leak-site listing of 2026-09-28 had described no dataset.", "The claim as Inside IT reported it on 2026-09-29 named no dataset ([Inside IT, 2026-09-29](%s))." % IN),
])

edit("entries/2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups.md", [
 ("verification: multi-source\n", "verification: single-source-victim\n"),
 ("classification:\n  reliability: A\n  credibility: 1\n", "classification:\n  reliability: A\n  credibility: 2\n"),
 ("the\n  outage itself is corroborated by BleepingComputer. The conclusion", "the\n  outage itself, but not the cause or the later counts, is corroborated by BleepingComputer. The conclusion"),
])

HPE = "https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05171.json"
edit("entries/2026-10-28/hpe-clearpass-php2shell-hotfixes-hpesbnw05171.md", [
 ("the bulletin itself reports no exploitation of ClearPass ([HPE Networking, 2026-10-23](%s))" % HPE, "the bulletin itself says nothing about exploitation of ClearPass ([HPE Networking, 2026-10-23](%s))" % HPE),
])

PHTML = "https://security.paloaltonetworks.com/CVE-2026-111497"
edit("entries/2026-10-24/cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi.md", [
 ("Cisco and Palo Alto report no malicious use against their own products ([Cisco PSIRT, 2026-10-27](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-oct2026-node-js-Jj3SQ19u); [Palo Alto Networks, 2026-10-28](%s))." % PHTML,
  "Cisco and Palo Alto report no malicious use against their own products ([Cisco PSIRT, 2026-10-27](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-oct2026-node-js-Jj3SQ19u); [Palo Alto Networks, 2026-10-28](%s)). Palo Alto's advisory, as read on 2026-10-28, shows six of the nine PAN-OS hotfixes released and the other three, 12.1.4-h13, 12.1.10-h3 and 11.2.4-h23, due on 2026-10-29 and 2026-10-30 ([Palo Alto Networks, 2026-10-28](%s))." % (PHTML, PHTML)),
])
print("ok")
