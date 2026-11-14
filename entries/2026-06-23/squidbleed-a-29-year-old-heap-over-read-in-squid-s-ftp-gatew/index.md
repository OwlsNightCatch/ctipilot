---
schema: 1
kind: research
title: "\"Squidbleed\" — a 29-year-old heap over-read in Squid's FTP gateway leaks other users' cleartext HTTP credentials (CVE-2026-47729)"
headline: "\"Squidbleed\" — a 29-year-old heap over-read in Squid's FTP gateway leaks other users' cleartext HTTP credentials (CVE-2026-47729)"
summary: "A 29-year-old heap over-read in Squid's FTP gateway (\"Squidbleed\", CVE-2026-47729) lets an attacker-controlled FTP server leak other proxy users' cleartext HTTP credentials and cookies; the upstream fix version is disputed (the maintainer cited 7.6 then 7.7, while SecurityWeek and Debian indicate the commit is already in 7.6, released 8 June). Shared school/university/government proxies are the exposure class (Calif.io, 2026-06-18)."
discovered_at: "2026-06-23T04:52:48Z"
event_date: 2026-06-22
run_id: 2026-06-23-165387f6
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - info-disclosure
  - no-patch
  - ai-abuse
regions:
  - global
  - europe
sectors:
  - public-sector
  - education
  - telco
entities: []
cves:
  - id: CVE-2026-47729
    cvss: "6.5"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status:
      - no-patch
sources:
  - url: "https://blog.calif.io/p/squidbleed-cve-2026-47729"
    publisher: Calif.io
    role: primary
  - url: "https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://www.securityweek.com/decades-old-squid-proxy-flaw-squidbleed-can-expose-user-data/"
    publisher: SecurityWeek
    role: corroborating
closed_sources: []
evidence:
  - quote: "A heap over-read in the Squid web proxy can leak another user's cleartext HTTP request, including any credentials or session tokens it carries, to anyone already allowed to send traffic through the same proxy"
    publisher: The Hacker News
  - quote: "while (strchr(w_space, *copyFrom)) — without checking for string termination first, causing the pointer to advance beyond the buffer boundary"
    publisher: Calif.io
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-23.md
---

Researchers at Calif.io disclosed CVE-2026-47729, nicknamed Squidbleed: a heap buffer over-read in the Squid proxy's FTP-over-HTTP gateway (`src/FtpGateway.cc`) introduced by a 1997 code commit ([Calif.io, 2026-06-18](https://blog.calif.io/p/squidbleed-cve-2026-47729); [The Hacker News, 2026-06-22](https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html)). The root cause is a whitespace-skipping loop that calls `strchr(w_space, *copyFrom)` without first checking for the string terminator: `strchr` returns a non-NULL pointer when the search character is the embedded `\0`, so the parser walks past the end of the FTP directory-listing buffer into adjacent heap memory containing other users' cached HTTP requests. An attacker who controls an FTP server and can induce the proxy to fetch from it (FTP support and TCP/21 are in Squid's default `Safe_ports` ACL) can leak `Authorization` headers, session cookies, API keys and other cleartext request content from concurrent users sharing the same proxy worker ([SecurityWeek, 2026-06-22](https://www.securityweek.com/decades-old-squid-proxy-flaw-squidbleed-can-expose-user-data/)). HTTPS relayed via `CONNECT` tunnels is not exposed; only cleartext HTTP and TLS-terminating proxy setups are. SUSE rates it moderate (CVSS 6.5) and there is no confirmed in-the-wild exploitation. The **fixed-version picture is disputed upstream**: the patch was merged in spring 2026, but the Squid maintainer first attributed the fix to 7.6 (released 8 June 2026) then corrected that to 7.7, while Debian's assessment is that the referenced commit is already present in 7.6, and SecurityWeek reports the fix shipped in 7.6 ([The Hacker News, 2026-06-22](https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html); [SecurityWeek, 2026-06-22](https://www.securityweek.com/decades-old-squid-proxy-flaw-squidbleed-can-expose-user-data/)). The safe reading for defenders is to treat the fixed version as uncertain and verify against your own build rather than assuming a single release line is clean Calif.io credits an AI model (Anthropic's "Claude Mythos") with surfacing the `strchr` edge case during AI-assisted fuzzing — another data point in the AI-assisted-vulnerability-discovery pattern the W25 weekly tracked.

**Why it matters to us:** Squid is widely deployed as a forward / caching / web-filtering proxy across EU public-sector networks, university perimeters and ISP infrastructure — exactly the multi-user environments where the cross-user leak has impact. Interim mitigation that does not depend on resolving the fixed-version dispute: disable FTP proxying (`acl ftp proto FTP` + `http_access deny ftp`, or drop FTP from `Safe_ports`) where it is not needed, and restrict who can reach the proxy from untrusted/multi-tenant segments. Confirm the fix is present in your actual build (RHEL/Debian/Ubuntu ship 4.x–6.x — check for a backport) rather than trusting a version number. Detection: monitor Squid `access.log` for `ftp://`-scheme requests from unusual clients and for worker heap-corruption / crash signals (`T1190` Exploit Public-Facing Application; effective outcome resembles `T1040` Network Sniffing).
