---
schema: 1
kind: vulnerability
title: "Cacti Core 1.2.31 (4HTTP2ROOT): an anonymous guest session reaches a stored SQL injection and command execution as the web or poller account in four requests, public proof of concept, no CVE id and no release; the chain needs the guest account enabled, which Cacti's documentation says is off by default"
headline: "Cacti 1.2.31 zero-day 4HTTP2ROOT: guest-session RCE, public PoC, no release; disable the guest user, restrict the UI"
summary: >
  A researcher published a proof of concept on 2026-11-26 that takes Cacti Core 1.2.31 from an anonymous guest session to command execution as the web or poller account in four requests; no CVE id and no release exist, and the chain needs the guest account enabled, which Cacti's documentation says is off by default. Previdian's honeypots recorded SQL-injection attempts from 2026-11-27 with no confirmed success, and Cacti merged unreleased hardening commits on 2026-11-28 that cover each stage without referring to the disclosure. Cacti stores SNMP strings and device logins, so a compromised server is a pivot into the monitored network.
discovered_at: "2026-11-28T04:55:00Z"
updated_at: null
event_date: "2026-11-26"
run_id: 2026-11-28T0355Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, sqli, pre-auth, zero-day, poc-public, no-patch]
regions: [global]
sectors: [technology]
entities: ["product:cacti", "tool:4http2root"]
techniques: [T1190, T1059]
affected_products: ["Cacti"]
cves: []
sources:
  - url: "https://github.com/ekomsSavior/Sad-Girls-0day-Club/tree/main/4http2shell"
    publisher: "ek0ms savi0r (Church of Malware)"
    date: "2026-11-26"
    role: primary
  - url: "https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/"
    publisher: "watchTowr"
    date: "2026-11-26"
    role: corroborating
  - url: "https://ravenai.sh/blog/four-requests-to-shell-cacti"
    publisher: "RavenAI"
    date: "2026-11-26"
    role: corroborating
  - url: "https://thehackernews.com/2026/11/unpatched-cacti-zero-day-enables-rce-in.html"
    publisher: "The Hacker News"
    date: "2026-11-27"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/unpatched-cacti-zero-day-with-public-poc-gives-remote-code-execution/"
    publisher: "BleepingComputer"
    date: "2026-11-27"
    role: corroborating
  - url: "https://blog.previdian.com/cacti-zero-day-what-we-know-so-far/"
    publisher: "Previdian Research"
    date: "2026-11-26"
    role: corroborating
  - url: "https://previdian.com/VULN-2026-0010"
    publisher: "Previdian (VULN-2026-0010)"
    date: "2026-11-26"
    role: corroborating
  - url: "https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-4845.json"
    publisher: "BSI CERT-Bund (WID-SEC-2026-4845)"
    date: "2026-11-26"
    role: corroborating
  - url: "https://github.com/Cacti/documentation/blob/develop/User-Management.md"
    publisher: "Cacti documentation (User Management, as read)"
    date: "2026-11-28"
    role: corroborating
  - url: "https://github.com/Cacti/cacti/pull/9014"
    publisher: "Cacti pull request 9014"
    date: "2026-11-28"
    role: corroborating
  - url: "https://github.com/Cacti/cacti/releases"
    publisher: "Cacti releases (as read)"
    date: "2026-11-28"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Cacti has not published a fixed version for this vulnerability"
    publisher: "watchTowr"
    source_url: "https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/"
  - quote: "The guest account must be enabled, since the entire chain runs through the unauthenticated guest session."
    publisher: "watchTowr"
    source_url: "https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/"
  - quote: "As of November 27, 2026, no exploitation in the wild has been reported."
    publisher: "watchTowr"
    source_url: "https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/"
  - quote: "By default, Guest or Anonymous access is disabled in Cacti."
    publisher: "Cacti documentation (User Management, as read)"
    source_url: "https://github.com/Cacti/documentation/blob/develop/User-Management.md"
  - quote: "The researcher tested the exploit against Cacti Core 1.2.31, but it is unclear whether earlier versions are also vulnerable."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/unpatched-cacti-zero-day-with-public-poc-gives-remote-code-execution/"
  - quote: "The requests contained time-based SQL injection payloads designed to test whether the newly disclosed vulnerability was exploitable. Successful remote command execution has not been confirmed."
    publisher: "Previdian Research"
    source_url: "https://blog.previdian.com/cacti-zero-day-what-we-know-so-far/"
verification: multi-source
sourcing_note: >
  The technical claims rest on one researcher's lab test of 1.2.31, restated by watchTowr, RavenAI, The Hacker News and BleepingComputer; Cacti has made no statement and issued no advisory or CVE id, and none of the sources read names a CVE id. The researcher's statement that the flaw was not reported to Cacti first is known only through BleepingComputer. Previdian's two pages disagree on its honeypot counts (22 attempts from one address in its blog, 216 attempts from 21 addresses on its tracker page read on 2026-11-28 at about 04:35 UTC), and its counts keep changing. Previdian's tracker states a CVSS of 9.8 that it labels AI-generated, while its blog says no official score is available; BSI rates the issue critical.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

A researcher using the handle ek0ms savi0r published a write-up and proof of concept on 2026-11-26 for unauthenticated command execution on Cacti Core 1.2.31 in four HTTP requests that start from an anonymous guest session, a chain its repository calls 4HTTP2SHELL ([ek0ms savi0r, 2026-11-26](https://github.com/ekomsSavior/Sad-Girls-0day-Club/tree/main/4http2shell)) and watchTowr named 4HTTP2ROOT ([watchTowr, 2026-11-26](https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/)). BleepingComputer relays the researcher's statement that the flaw was not reported to Cacti before release, and no fixed version exists: watchTowr says Cacti has not published one, and the project's releases page lists 1.2.31 as its newest release on 2026-11-28 ([BleepingComputer, 2026-11-27](https://www.bleepingcomputer.com/news/security/unpatched-cacti-zero-day-with-public-poc-gives-remote-code-execution/); [watchTowr, 2026-11-26](https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/); [Cacti releases, 2026-11-28](https://github.com/Cacti/cacti/releases)).

As RavenAI and The Hacker News describe the chain, the guest profile page stores a non-numeric graph page size; a graph-preview request concatenates it into a query that accepts a second statement, which rewrites a poller entry's command; and a realtime-graph request runs that command inside the web request as the web server and poller account, often a low-privileged web user according to watchTowr ([RavenAI, 2026-11-26](https://ravenai.sh/blog/four-requests-to-shell-cacti); [The Hacker News, 2026-11-27](https://thehackernews.com/2026/11/unpatched-cacti-zero-day-enables-rce-in.html); [watchTowr, 2026-11-26](https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/)). The guest account must be enabled for the chain to work, and Cacti's documentation says guest or anonymous access is disabled by default and works only when the Guest user is enabled and set as the guest user ([watchTowr, 2026-11-26](https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/); [Cacti documentation, 2026-11-28](https://github.com/Cacti/documentation/blob/develop/User-Management.md)). Only 1.2.31 was tested, and it is unclear whether earlier versions are affected ([BleepingComputer, 2026-11-27](https://www.bleepingcomputer.com/news/security/unpatched-cacti-zero-day-with-public-poc-gives-remote-code-execution/)). Cacti stores SNMP strings and device logins, so a compromised server is a foothold into the monitored network ([watchTowr, 2026-11-26](https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/)).

watchTowr reports no exploitation as of 2026-11-27, while Previdian's honeypots recorded SQL-injection attempts from 2026-11-27 that it says do not show the target was vulnerable or that an attempt succeeded ([watchTowr, 2026-11-26](https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/); [Previdian, 2026-11-26](https://blog.previdian.com/cacti-zero-day-what-we-know-so-far/); [Previdian tracker, 2026-11-26](https://previdian.com/VULN-2026-0010)). BSI classifies the issue as critical ([BSI, 2026-11-26](https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-4845.json)). On 2026-11-28 the project merged unreleased 1.2.x hardening commits that reject guest profile writes, validate the page size and require graph access before a realtime command, without referring to the disclosure and with no release or advisory yet ([Cacti pull request 9014, 2026-11-28](https://github.com/Cacti/cacti/pull/9014)).

**Exposure:** Cacti Core 1.2.31 with the Guest user enabled and set as the anonymous user, reachable from wherever an attacker can load the web interface.

**Detection:** in web access logs, one client requesting the guest profile page, a profile update, a graph preview and a realtime graph in sequence; in the application log, a PHP warning about a non-numeric value in a graph display setting; in the Cacti database, a poller entry whose command is anything other than a normal poller command; on the host, new files written by the poller or web account, a shell or marker file among them ([RavenAI, 2026-11-26](https://ravenai.sh/blog/four-requests-to-shell-cacti); [watchTowr, 2026-11-26](https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/)). No release exists, so check guest-reachable servers for these artifacts and treat stored SNMP strings and device logins as exposed on a hit.

**Triage:** each request alone is ordinary guest behavior, so the stronger pivots are the non-numeric display-setting warning and a changed poller entry followed by a realtime-graph request ([RavenAI, 2026-11-26](https://ravenai.sh/blog/four-requests-to-shell-cacti)).

**Defender takeaway:** where the guest account is on, disable it and restrict the web interface to trusted internal networks now and review poller entries for unexpected commands; where it is off, the sources say the chain has no entry point, but watch for the first release with the hardening commits ([watchTowr, 2026-11-26](https://watchtowr.com/intelligence/4http2root-cacti-zero-day-faq/)).
