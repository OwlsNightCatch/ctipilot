import re,sys
sys.path.insert(0,'tools')
import check_run as c
def load(p): return open(p,encoding='utf-8').read()
def save(p,t): open(p,'w',encoding='utf-8').write(t)
def words(p):
    fm,body=c._frontmatter_and_body(load(p)); return c._main_words(body)
# ---- Node2Shell
p='entries/2026-10-24/cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi.md'
t=load(p)
head,rest=t.split('\n---\n\n',1)
i=rest.index('## Update — 2026-10-26T03:40:22Z'); tail=rest[i:]
NJ='https://nodejs.org/en/blog/vulnerability/october-2026-security-releases'
IM='https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/'
EL='https://ellio.tech/en/blog/node2shell-cve-2026-111497-rce-on-stock-nodejs-builds/'
OSM='https://opensourcemalware.com/blog/node2shell-affects-python'
EV='https://github.com/envoyproxy/envoy/security/advisories/GHSA-3wvj-j6qm-62mr'
body=f'''Node.js shipped security releases on 2026-10-21 for CVE-2026-111497, an out-of-bounds write in the Brotli decoder it bundles: an invalid block switch was reported as a need for more input instead of a format error, so the streaming decoder kept appending input to an eight-byte internal buffer ([Node.js project, 2026-10-21]({NJ})). An attacker who can supply Brotli data that an application decompresses with node:zlib can corrupt process memory, which can lead to a crash, disclosure of process memory or remote code execution ([Node.js project, 2026-10-21]({NJ})).

CISA added the flaw to its Known Exploited Vulnerabilities catalog on 2026-10-27 "based on evidence of active exploitation", naming no actor or victim ([CISA, 2026-10-27](https://www.cisa.gov/news-events/alerts/2026/10/27/cisa-adds-two-known-exploited-vulnerabilities-catalog)). The only first-hand attack telemetry found is ELLIO's: on 2026-10-26 its sensors recorded one Brotli-coded request body of about 23 MB built against Node.js 24.22.0 on x86-64, which it reads as adoption by an operator focused on mass exploitation, although the chain got no shell against ELLIO's own copy of that build in 50 attempts ([ELLIO, 2026-10-26]({EL})). Tenable relays the report without confirming it, and Cisco and Palo Alto say they know of no malicious use against their own products ([Tenable, 2026-10-26](https://www.tenable.com/blog/brotli2shell-frequently-asked-questions-for-google-brotli-decoder-cve-2026-111497); [Cisco PSIRT, 2026-10-27](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-oct2026-node-js-Jj3SQ19u); [Palo Alto Networks, 2026-10-26](https://security.paloaltonetworks.com/CVE-2026-111497)).

Fixes are in Node.js 22.23.4, 24.22.1 and 26.12.1; end-of-life lines are always affected, and because Node.js cherry-picked the fix without bumping the bundled version string, process.versions.brotli reads 1.2.0 on patched and vulnerable builds alike ([Node.js project, 2026-10-21]({NJ}); [ELLIO, 2026-10-26]({EL})). The decoder is Google's, so the PyPI packages Brotli (fixed in 1.2.1) and brotlicffi (1.2.1.0), Envoy and Microsoft .NET carry the flaw too ([OpenSourceMalware, 2026-10-23]({OSM}); [Envoy, 2026-10-23]({EV}); [.NET Blog, 2026-10-25](https://devblogs.microsoft.com/dotnet/dotnet-october-2026-oob-security-updates/)).

**Exposure:** a service on Node.js 22.x, 24.x or 26.x below the fixed releases that decodes Brotli from an untrusted party, either request bodies inflated by Express 5 or body-parser 2 or compressed responses that fetch() consumes from a server an attacker influences ([Imperva, 2026-10-22]({IM})); Python code that decompresses untrusted data with the PyPI packages ([OpenSourceMalware, 2026-10-23]({OSM})); Envoy with the Brotli decompressor configured ([Envoy, 2026-10-23]({EV})); .NET applications that decompress attacker-controlled Brotli data ([dotnet/announcements #494, 2026-10-25](https://github.com/dotnet/announcements/issues/494)); and PAN-OS 12.2, 12.1 and 11.2 firewalls that inspect Brotli traffic with TLS decryption enabled ([Palo Alto Networks, 2026-10-26](https://security.paloaltonetworks.com/CVE-2026-111497)).

**Detection:** in web server, proxy and WAF logs, requests that carry a Brotli content encoding to endpoints that parse bodies, followed by worker crashes or restarts; in ELLIO's lab most of 400 attempts against Express crashed the worker instead of returning a shell, and a patched build answers at once with HTTP 400 and ERR__ERROR_FORMAT_BLOCK_SWITCH ([ELLIO, 2026-10-26]({EL})). Where systemd-coredump is enabled, each forced crash writes a core file that can hold other visitors' session cookies, tokens and key material, so restrict who can read it ([ELLIO, 2026-10-26]({EL})).

**Defender takeaway:** replace the runtime, the two Python packages and any Envoy with the decompressor configured now, because CISA lists the flaw as exploited; where an update has to wait, reject Content-Encoding: br as NCSC Switzerland advises ([NCSC Switzerland, 2026-10-26](https://security-hub.ncsc.admin.ch/#/posts/13105)) and, if the application accepts no compressed request bodies, set the body-parser inflate option to false ([Akamai, 2026-10-26](https://www.akamai.com/blog/security-research/inside-node2shell-closer-look-cve-2026-111497)).

'''
save(p,head+'\n---\n\n'+body+tail)
print('node2shell',words(p))
