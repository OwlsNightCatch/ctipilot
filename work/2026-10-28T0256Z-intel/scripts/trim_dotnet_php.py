import re,sys
sys.path.insert(0,'tools')
import check_run as c
def load(p): return open(p,encoding='utf-8').read()
def save(p,t): open(p,'w',encoding='utf-8').write(t)
def words(p):
    fm,body=c._frontmatter_and_body(load(p)); return c._main_words(body)
def rep(t,old,new,count=1):
    assert t.count(old)==count,(t.count(old),old[:80]); return t.replace(old,new)
# ---- .NET
p='entries/2026-10-26/cve-2026-111497-microsoft-net-oob-update-brotli-sockets-fix.md'
t=load(p)
t=rep(t,"No source reports an attack on .NET through any of the four, but CISA lists CVE-2026-111497, the Brotli decoder flaw, as exploited since 2026-10-27, and ELLIO recorded exploit traffic against Node.js 24.22.0 that carried the public exploit ([CISA, 2026-10-27](https://www.cisa.gov/news-events/alerts/2026/10/27/cisa-adds-two-known-exploited-vulnerabilities-catalog); [ELLIO, 2026-10-26](https://ellio.tech/en/blog/node2shell-cve-2026-111497-rce-on-stock-nodejs-builds/)).",
 "No source reports an attack on .NET, but CISA lists CVE-2026-111497 as exploited since 2026-10-27 ([CISA, 2026-10-27](https://www.cisa.gov/news-events/alerts/2026/10/27/cisa-adds-two-known-exploited-vulnerabilities-catalog)).")
t=rep(t,"CVE-2026-114148 is incorrect file ownership in Linux ASP.NET Core runtime and targeting-pack tarballs of .NET 8 and 9 and in source-built tarballs, a local privilege escalation (CVSS 3.1 7.8) ([dotnet/announcements #495, 2026-10-25](https://github.com/dotnet/announcements/issues/495)).",
 "CVE-2026-114148 is a local privilege escalation through incorrect file ownership in Linux ASP.NET Core tarballs of .NET 8 and 9 (CVSS 3.1 7.8) ([dotnet/announcements #495, 2026-10-25](https://github.com/dotnet/announcements/issues/495)).")
t=rep(t,"; Microsoft scores it CVSS 3.1 8.1 with high attack complexity, marked it publicly disclosed and not exploited on 2026-10-25, and rates it Exploitation More Likely (","; Microsoft scores it CVSS 3.1 8.1, marked it publicly disclosed and not exploited on 2026-10-25, and rates it Exploitation More Likely (")
save(p,t); print('dotnet',words(p))
# ---- PHP vendor paragraph
p='entries/2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619.md'
t=load(p)
i=t.index('Vendors of products that embed PHP report as follows:')
j=t.index('\n\n**Exposure:**',i)
old=t[i:j]
print('old vendor para words',len(old.split()))
new=("Vendors of products that embed PHP report as follows: Citrix lists the NetScaler management GUI on every supported version ([NetScaler Product Security, 2026-10-22](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)); "
 "Cisco lists Expressway, Ultra-Reliable Wireless Backhaul, Duo Access Gateway and ISE Portal Builder, with fixes at 15.5.21, 27.1.1 (March 2027) and 3.2.0 ([Cisco PSIRT, 2026-10-27](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq)); "
 "Fortinet keeps only FortiDDoS, FortiSOAR and FortiSOAR PaaS under investigation ([Fortinet PSIRT, 2026-10-26](https://fortiguard.fortinet.com/psirt/FG-IR-26-186)); "
 "Splunk lists its products as unaffected or remedied ([Splunk, 2026-10-26](https://advisory.splunk.com/advisories/SVD-2026-1013)); "
 "Tenable's patch SC-202610.2 updates the bundled PHP in Security Center and Enclave Security to 8.2.35 ([Tenable, 2026-10-23](https://www.tenable.com/security/tns-2026-30); [Tenable, 2026-10-23](https://www.tenable.com/security/tns-2026-31)); "
 "Siemens lists RUGGEDCOM APE1808 devices running PAN-OS as affected ([Siemens ProductCERT, 2026-10-23](https://cert-portal.siemens.com/productcert/html/ssa-566512.html)); "
 "and WatchGuard says none of its products are affected ([WatchGuard PSIRT, 2026-10-21](https://psirt.watchguard.com/WGSA-2026-0032/)).")
t=t[:i]+new+t[j:]
save(p,t); print('php',words(p))
