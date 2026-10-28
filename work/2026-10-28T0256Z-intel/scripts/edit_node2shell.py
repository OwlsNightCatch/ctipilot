import re,yaml
p='entries/2026-10-24/cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi.md'
t=open(p,encoding='utf-8').read()
def rep(old,new,count=1):
    global t
    assert t.count(old)==count,(t.count(old),old[:90])
    t=t.replace(old,new)
rep('headline: "Node2Shell Brotli flaw: Node.js, PyPI, .NET, Envoy and PAN-OS with decryption need updates; exploitation unknown"',
    'headline: "Node2Shell Brotli flaw is now on CISA KEV, with exploit traffic seen against Node.js 24.22.0; update now"')
old=t[t.index('summary: >\n'):t.index('discovered_at:')]
new='''summary: >
  CISA added CVE-2026-111497, an out-of-bounds write in the Brotli decoder bundled with Node.js, to its Known Exploited Vulnerabilities
  catalog on 2026-10-27 on evidence of active exploitation, and ELLIO's sensors recorded exploit traffic against Node.js 24.22.0 on
  2026-10-26, though its own copy of the attacker's chain got no shell. Node.js 22.23.4, 24.22.1 and 26.12.1 fix it, and because the flaw is
  in Google's decoder the PyPI packages Brotli (1.2.1) and brotlicffi (1.2.1.0), Envoy, Microsoft .NET, PHP for Windows, Ubuntu and, with
  Brotli inspection and TLS decryption enabled, PAN-OS 12.2, 12.1 and 11.2 firewalls carry it too; Palo Alto and Cisco report no malicious
  use against their own products.
'''
t=t.replace(old,new)
rep('priority: notable','priority: high')
rep('tags: [vulnerabilities, rce, pre-auth, poc-public, patch-available]','tags: [vulnerabilities, rce, pre-auth, actively-exploited, cisa-kev, poc-public, patch-available]')
rep('status: [poc-public, patch-available]','status: [exploited, cisa-kev, poc-public, patch-available]')
rep('''closed_sources: []
evidence:''','''  - url: "https://www.cisa.gov/news-events/alerts/2026/10/27/cisa-adds-two-known-exploited-vulnerabilities-catalog"
    publisher: "CISA (alert, KEV additions)"
    date: "2026-10-27"
    role: corroborating
  - url: "https://ellio.tech/en/blog/node2shell-cve-2026-111497-rce-on-stock-nodejs-builds/"
    publisher: "ELLIO Threat Research Lab"
    date: "2026-10-26"
    role: corroborating
  - url: "https://www.tenable.com/blog/brotli2shell-frequently-asked-questions-for-google-brotli-decoder-cve-2026-111497"
    publisher: "Tenable Research"
    date: "2026-10-26"
    role: corroborating
  - url: "https://research.jfrog.com/post/brotli2shell-beyond-node2shell-and-http2shell/"
    publisher: "JFrog Security Research"
    date: "2026-10-25"
    role: corroborating
  - url: "https://www.akamai.com/blog/security-research/inside-node2shell-closer-look-cve-2026-111497"
    publisher: "Akamai Security Intelligence Group"
    date: "2026-10-26"
    role: corroborating
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-oct2026-node-js-Jj3SQ19u"
    publisher: "Cisco PSIRT (advisory, Vulnerabilities in node.js Affecting Cisco Products)"
    date: "2026-10-27"
    role: corroborating
closed_sources: []
evidence:''')
rep('''verification: multi-source
sourcing_note: "The Node.js advisory names the affected release lines but not the fixed versions; the three release pages of 2026-10-21 list the flaw in their notes, and Imperva names the fixed versions together. Node.js rates the flaw high; the Google CNA record, read through ENISA's EUVD, scores it CVSS 4.0 9.2."''',
'''  - quote: "based on evidence of active exploitation"
    publisher: "CISA (alert, KEV additions)"
    source_url: "https://www.cisa.gov/news-events/alerts/2026/10/27/cisa-adds-two-known-exploited-vulnerabilities-catalog"
  - quote: "ELLIO sensors have recorded CVE-2026-111497 exploit traffic in the wild"
    publisher: "ELLIO Threat Research Lab"
    source_url: "https://ellio.tech/en/blog/node2shell-cve-2026-111497-rce-on-stock-nodejs-builds/"
  - quote: "the attacker's chain scored zero hits in 50 attempts"
    publisher: "ELLIO Threat Research Lab"
    source_url: "https://ellio.tech/en/blog/node2shell-cve-2026-111497-rce-on-stock-nodejs-builds/"
  - quote: "Tenable has not independently confirmed this activity."
    publisher: "Tenable Research"
    source_url: "https://www.tenable.com/blog/brotli2shell-frequently-asked-questions-for-google-brotli-decoder-cve-2026-111497"
  - quote: "The Cisco PSIRT is not aware of any malicious use of these vulnerabilities against any Cisco product."
    publisher: "Cisco PSIRT (advisory, Vulnerabilities in node.js Affecting Cisco Products)"
    source_url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-oct2026-node-js-Jj3SQ19u"
  - quote: "A single HTTP request containing a crafted 23 MB body crashed the tested ClickHouse server."
    publisher: "JFrog Security Research"
    source_url: "https://research.jfrog.com/post/brotli2shell-beyond-node2shell-and-http2shell/"
verification: multi-source
sourcing_note: "The Node.js advisory names the affected release lines but not the fixed versions; the three release pages of 2026-10-21 list the flaw in their notes, and Imperva names the fixed versions together. Node.js rates the flaw high; the Google CNA record, read through ENISA's EUVD, scores it CVSS 4.0 9.2. CISA's alert gives no detail of the exploitation evidence; ELLIO's sensor telemetry is the only first-hand account of an attack found, and Tenable relays it without confirming it."''')
rep('''  - "Update every Node.js 22.x, 24.x and 26.x runtime to 22.23.4, 24.22.1 or 26.12.1, including the Node binary inside container images, which a package inventory misses, and upgrade the PyPI Brotli package to 1.2.1 and brotlicffi to 1.2.0.1 wherever either is installed; move any application on an end-of-life Node.js line to a supported release."''' if False else '''  - "Update every Node.js 22.x, 24.x and 26.x runtime to 22.23.4, 24.22.1 or 26.12.1, including the Node binary inside container images, which a package inventory misses, and upgrade the PyPI Brotli package to 1.2.1 and brotlicffi to 1.2.1.0 wherever either is installed; move any application on an end-of-life Node.js line to a supported release."''',
'''  - "Update every Node.js 22.x, 24.x and 26.x runtime to 22.23.4, 24.22.1 or 26.12.1, including the Node binary inside container images (a Dockerfile that pins 24.22.0 keeps the flaw until the pin changes), and upgrade the PyPI Brotli package to 1.2.1 and brotlicffi to 1.2.1.0 wherever either is installed; judge a Node.js build by its release version, because process.versions.brotli reads 1.2.0 on patched builds too, and move any application on an end-of-life Node.js line to a supported release."''')
head,rest=t.split('\n---\n\n',1)
idx=rest.index('## Update — 2026-10-26T03:40:22Z')
tail=rest[idx:]
IM='https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/'
NJ='https://nodejs.org/en/blog/vulnerability/october-2026-security-releases'
EL='https://ellio.tech/en/blog/node2shell-cve-2026-111497-rce-on-stock-nodejs-builds/'
body=f'''Node.js shipped security releases on 2026-10-21 for CVE-2026-111497, an out-of-bounds write in the Brotli decoder it bundles: an invalid block switch was reported as a need for more input instead of a format error, so the streaming decoder kept appending input to an eight-byte internal buffer ([Node.js project, 2026-10-21]({NJ})). An attacker who can supply Brotli data that an application decompresses with the node:zlib module can corrupt process memory, which can lead to a crash, disclosure of process memory or remote code execution ([Node.js project, 2026-10-21]({NJ})). The Google CNA record scores it CVSS 4.0 9.2 with no authentication and no user interaction ([ENISA EUVD, 2026-10-23](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-108169)).

CISA added the flaw to its Known Exploited Vulnerabilities catalog on 2026-10-27 "based on evidence of active exploitation", naming no actor, victim or product ([CISA, 2026-10-27](https://www.cisa.gov/news-events/alerts/2026/10/27/cisa-adds-two-known-exploited-vulnerabilities-catalog)). The only first-hand attack telemetry found is ELLIO's: its sensors recorded a public checker mapping which hosts decompress Brotli and then, on 2026-10-26, a single Brotli-coded request body of about 23 MB built against one binary, Node.js 24.22.0 on x86-64, which ELLIO reads as adoption of the exploit by an operator focused on mass exploitation, although the attacker's chain got no shell against ELLIO's own copy of that build in 50 attempts ([ELLIO, 2026-10-26]({EL})). Tenable relays the report without confirming it ([Tenable, 2026-10-26](https://www.tenable.com/blog/brotli2shell-frequently-asked-questions-for-google-brotli-decoder-cve-2026-111497)); Cisco's advisory, which lists its products as still under investigation, and Palo Alto's say they know of no malicious use against their own products ([Cisco PSIRT, 2026-10-27](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-oct2026-node-js-Jj3SQ19u); [Palo Alto Networks, 2026-10-26](https://security.paloaltonetworks.com/CVE-2026-111497)).

Imperva ran code carried in Brotli data against the official Node.js 24.22.0 Linux arm64 image, through the built-in fetch() consuming a compressed response and through Express 5.0.0 to 5.3.0 and body-parser 2.0.0 to 2.3.0 request-body parsers; a bare Node.js HTTP server does not decode an incoming Brotli body, and the fixed 24.22.1 rejected the same input ([Imperva, 2026-10-22]({IM})). Fixes are in Node.js 22.23.4, 24.22.1 and 26.12.1; end-of-life lines are always affected when a security release occurs ([Node.js project, 2026-10-21]({NJ})), and Node.js cherry-picked the fix without bumping the bundled version string, so process.versions.brotli reads 1.2.0 on patched and vulnerable builds ([ELLIO, 2026-10-26]({EL})).

The decoder is Google's, so the flaw reaches beyond Node.js: Google released Brotli 1.2.1 on 2026-10-21 ([Google Brotli, 2026-10-21](https://github.com/google/brotli/releases/tag/v1.2.1)), the PyPI packages Brotli (fixed in 1.2.1) and brotlicffi (1.2.1.0) compile the same decoder ([OpenSourceMalware, 2026-10-23](https://opensourcemalware.com/blog/node2shell-affects-python)), and Envoy and Microsoft .NET have shipped fixes ([Envoy, 2026-10-23](https://github.com/envoyproxy/envoy/security/advisories/GHSA-3wvj-j6qm-62mr); [.NET Blog, 2026-10-25](https://devblogs.microsoft.com/dotnet/dotnet-october-2026-oob-security-updates/)). JFrog also crashed a ClickHouse server with one request carrying a crafted 23 MB body, for which a fix was merged but not yet released when it wrote ([JFrog, 2026-10-25](https://research.jfrog.com/post/brotli2shell-beyond-node2shell-and-http2shell/)).

**Exposure:** a service on Node.js 22.x, 24.x or 26.x below the fixed releases that decodes Brotli from an untrusted party, either request bodies inflated by Express 5 or body-parser 2 or compressed responses that fetch() consumes from a server an attacker influences ([Imperva, 2026-10-22]({IM})); Python code that decompresses untrusted data with the PyPI Brotli or brotlicffi packages ([OpenSourceMalware, 2026-10-23](https://opensourcemalware.com/blog/node2shell-affects-python)); Envoy with the Brotli decompressor configured ([Envoy, 2026-10-23](https://github.com/envoyproxy/envoy/security/advisories/GHSA-3wvj-j6qm-62mr)); .NET applications that decompress attacker-controlled Brotli data ([dotnet/announcements #494, 2026-10-25](https://github.com/dotnet/announcements/issues/494)); and PAN-OS 12.2, 12.1 and 11.2 firewalls that inspect Brotli traffic with TLS decryption enabled ([Palo Alto Networks, 2026-10-26](https://security.paloaltonetworks.com/CVE-2026-111497)).

**Detection:** in web server, proxy and WAF logs, requests that carry a Brotli content encoding to endpoints that parse bodies, followed by worker crashes or restarts in the supervisor or container logs; in ELLIO's lab most of 400 attempts against Express crashed the worker instead of returning a shell, and a patched build answers at once with HTTP 400 and ERR__ERROR_FORMAT_BLOCK_SWITCH ([ELLIO, 2026-10-26]({EL})). Where systemd-coredump is enabled, each forced crash writes a core file under /var/lib/systemd/coredump that can hold other visitors' session cookies, tokens and key material, so restrict who can read those files ([ELLIO, 2026-10-26]({EL})).

**Triage:** Brotli-compressed responses are ordinary web traffic; a Brotli-coded request body sent to an endpoint that parses bodies, or a Brotli response from a server an attacker influences, followed by a worker crash, is the pattern the exploit needs ([Imperva, 2026-10-22]({IM})).

**Defender takeaway:** replace the runtime, the two Python packages and any Envoy with the decompressor configured now, because CISA lists the flaw as exploited, and judge a Node.js build by its release version; where an update has to wait, reject Content-Encoding: br as NCSC Switzerland advises ([NCSC Switzerland, 2026-10-26](https://security-hub.ncsc.admin.ch/#/posts/13105)) and, if the application accepts no compressed request bodies, set the body-parser inflate option to false so they are rejected ([Akamai, 2026-10-26](https://www.akamai.com/blog/security-research/inside-node2shell-closer-look-cve-2026-111497)), and test the change against normal traffic.

'''
t=head+'\n---\n\n'+body+tail
open(p,'w',encoding='utf-8').write(t)
fm=yaml.safe_load(head.split('---\n',1)[1])
print(len(fm['headline']),fm['priority'],fm['tags'])
main=body.split('**Exposure:**')[0]
print('main words',len(re.sub(r'\(\[[^\]]*\]\([^)]*\)\)','',re.sub(r'\[[^\]]*\]\([^)]*\)','',main)).split()))
