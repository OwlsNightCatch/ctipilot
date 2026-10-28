p='entries/2026-10-26/cve-2026-111497-microsoft-net-oob-update-brotli-sockets-fix.md'
t=open(p,encoding='utf-8').read()
def rep(old,new,count=1):
    global t
    assert t.count(old)==count,(t.count(old),old[:90])
    t=t.replace(old,new)
rep('''  CVE-2026-111497 (CVSS 3.1 8.1, publicly disclosed, not exploited, rated Exploitation More Likely) and to deliver the corrected fixes for''',
'''  CVE-2026-111497 (CVSS 3.1 8.1, publicly disclosed, rated Exploitation More Likely) and to deliver the corrected fixes for''')
rep('''  not fully address. Brotli exposure needs an application that decompresses attacker-controlled Brotli data, which ASP.NET Core and
  HttpClient do not do by default.''','''  not fully address. Brotli exposure needs an application that decompresses attacker-controlled Brotli data, which ASP.NET Core and
  HttpClient do not do by default; CISA lists CVE-2026-111497 as exploited since 2026-10-27, although Microsoft's record still said not
  exploited on 2026-10-25 and no source reports an attack on .NET.''')
rep('tags: [vulnerabilities, rce, pre-auth, patch-available]','tags: [vulnerabilities, rce, pre-auth, actively-exploited, cisa-kev, patch-available]')
rep('''    status: [patch-available]
    affected: ".NET 8 before 8.0.33, .NET 9 before 9.0.22, .NET 10 before 10.0.14 and .NET 11 before Release Candidate 3 (runtime and NativeAOT packages); .NET Framework is not affected"''',
'''    status: [exploited, cisa-kev, patch-available]
    affected: ".NET 8 before 8.0.33, .NET 9 before 9.0.22, .NET 10 before 10.0.14 and .NET 11 before Release Candidate 3 (runtime and NativeAOT packages); .NET Framework is not affected"''')
rep('''  - url: "https://nodejs.org/en/blog/vulnerability/october-2026-security-releases"
    publisher: "Node.js project"
    date: "2026-10-21"
    role: corroborating
closed_sources: []''','''  - url: "https://nodejs.org/en/blog/vulnerability/october-2026-security-releases"
    publisher: "Node.js project"
    date: "2026-10-21"
    role: corroborating
  - url: "https://www.cisa.gov/news-events/alerts/2026/10/27/cisa-adds-two-known-exploited-vulnerabilities-catalog"
    publisher: "CISA (alert, KEV additions)"
    date: "2026-10-27"
    role: corroborating
  - url: "https://ellio.tech/en/blog/node2shell-cve-2026-111497-rce-on-stock-nodejs-builds/"
    publisher: "ELLIO Threat Research Lab"
    date: "2026-10-26"
    role: corroborating
closed_sources: []''')
rep('''    source_url: "https://github.com/dotnet/announcements/issues/494"
verification: single-source''','''    source_url: "https://github.com/dotnet/announcements/issues/494"
  - quote: "based on evidence of active exploitation"
    publisher: "CISA (alert, KEV additions)"
    source_url: "https://www.cisa.gov/news-events/alerts/2026/10/27/cisa-adds-two-known-exploited-vulnerabilities-catalog"
verification: single-source''')
rep('''  pages are the basis for every .NET statement here.''','''  pages are the basis for every .NET statement here. The exploitation listing is CISA's, which describes no evidence; the one first-hand
  attack report found, ELLIO's, concerns Node.js 24.22.0.''')
rep('''Microsoft scores it CVSS 3.1 8.1 with high attack complexity, marks it publicly disclosed and not exploited, and rates it Exploitation More Likely ([MSRC, 2026-10-25]''',
    '''Microsoft scores it CVSS 3.1 8.1 with high attack complexity, marked it publicly disclosed and not exploited on 2026-10-25, and rates it Exploitation More Likely ([MSRC, 2026-10-25]''')
rep('''No source reports exploitation of any of the four.''','''No source reports an attack on .NET through any of the four, but CISA lists CVE-2026-111497, the Brotli decoder flaw, as exploited since 2026-10-27, and ELLIO recorded exploit traffic against Node.js 24.22.0 that carried the public exploit ([CISA, 2026-10-27](https://www.cisa.gov/news-events/alerts/2026/10/27/cisa-adds-two-known-exploited-vulnerabilities-catalog); [ELLIO, 2026-10-26](https://ellio.tech/en/blog/node2shell-cve-2026-111497-rce-on-stock-nodejs-builds/)).''')
rep('''**Defender takeaway:** install the updated runtime on every .NET host now, including Windows hosts patched on 2026-10-13, which still carry CVE-2026-70197 ([.NET Blog, 2026-10-25]''','''**Defender takeaway:** install the updated runtime on every .NET host now, including Windows hosts patched on 2026-10-13, which still carry CVE-2026-70197, and treat the Brotli flaw as exploited ([.NET Blog, 2026-10-25]''')
open(p,'w',encoding='utf-8').write(t)
