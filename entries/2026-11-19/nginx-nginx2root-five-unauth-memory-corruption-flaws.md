---
schema: 1
kind: vulnerability
title: "NGINX nginx2root: five unauthenticated memory-corruption flaws (CVE-2026-123007 and CVE-2026-123633 in HTTP/2, CVE-2026-121810 in HTTP/3, CVE-2026-123634 in the resolver, CVE-2026-113425 in the mail proxy) can lead to code execution as the worker process; fixed in nginx 1.31.9 and 1.30.7 and NGINX Plus 37.3.0.1 and 37.0.8.1, Rapid7 proof of concept public, no exploitation reported (CVSS 4.0 9.2)"
headline: "NGINX nginx2root: five unauthenticated flaws reach worker RCE, Rapid7 PoC public; update 1.31.9, 1.30.7 or Plus 37.3.0.1"
summary: >
  F5 and the nginx project fixed five memory-corruption flaws in the nginx data plane on 2026-11-18, two in HTTP/2 and one each in HTTP/3, the resolver and the mail proxy, which CERT-EU says can lead to unauthenticated code execution with the privileges of the worker process; NCSC-NL scores all five CVSS 4.0 9.2, NCSC.ch and Wiz the two HTTP/2 flaws and Rapid7 CVE-2026-123007. The fixes are in nginx 1.31.9 and 1.30.7 and NGINX Plus 37.3.0.1 and 37.0.8.1, while NGINX Plus R33 to R36 have no update. Rapid7 published a proof of concept for CVE-2026-123007, CERT-EU reports no exploitation, and NCSC.ch, CERT-EU, CERT.at and NCSC-NL issued warnings.
discovered_at: "2026-11-19T05:12:00Z"
updated_at: null
event_date: "2026-11-18"
run_id: 2026-11-19T0355Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, poc-public, patch-available]
regions: [global]
sectors: [technology]
entities: ["product:f5-nginx-open-source", "product:f5-nginx-plus"]
techniques: [T1190, T1059.004, T1499.004, T1068, T1611]
affected_products: ["NGINX Open Source", "NGINX Plus"]
cves:
  - id: CVE-2026-123007
    cvss: "9.2 (CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [poc-public, patch-available]
    affected: "NGINX Open Source 1.9.5 to 1.31.8 with HTTP/2 enabled; NGINX Plus 37.1.0 to before 37.3.0.1 and 37.0.0 to before 37.0.8.1; NGINX Plus R34 to R36"
    fixed: "nginx 1.31.9 and 1.30.7; NGINX Plus 37.3.0.1 and 37.0.8.1; none for NGINX Plus R34 to R36"
  - id: CVE-2026-123633
    cvss: "9.2 (CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "NGINX Open Source 1.19.7 to 1.31.8 with HTTP/2 enabled; NGINX Plus before 37.2.0.1 and 37.0.7.1 and R34 to R36"
    fixed: "nginx 1.31.9 and 1.30.7; NGINX Plus 37.2.0.1 and 37.0.7.1 or later (per CERT.at, 37.3.0.1 and 37.0.8.1 carry the fixes for four of the five); none for NGINX Plus R34 to R36"
  - id: CVE-2026-123634
    cvss: "9.2 (CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "NGINX Open Source 0.6.18 to 1.31.8 using the resolver; NGINX Plus not itemised by any cited source"
    fixed: "nginx 1.31.9 and 1.30.7; NGINX Plus builds not itemised by any cited source, presumed 37.3.0.1 and 37.0.8.1"
  - id: CVE-2026-121810
    cvss: "9.2 (CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "NGINX Open Source 1.25.0 to 1.31.8 with HTTP/3; NGINX Plus before 37.3.0.1 and 37.0.8.1 and R34 to R36"
    fixed: "nginx 1.31.9 and 1.30.7; NGINX Plus 37.3.0.1 and 37.0.8.1; none for NGINX Plus R34 to R36"
  - id: CVE-2026-113425
    cvss: "9.2 (CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "NGINX Open Source 0.5.33 to 1.31.8 with the mail proxy; NGINX Plus 37.1.0 to 37.2.0, 37.0.0 to 37.0.7 and R33 to R36 per CERT.at"
    fixed: "nginx 1.31.9 and 1.30.7; NGINX Plus 37.3.0.1 and 37.0.8.1; none for NGINX Plus R33 to R36"
sources:
  - url: "https://nginx.org/en/security_advisories.html"
    publisher: "nginx.org security advisories"
    date: "2026-11-18"
    role: primary
  - url: "https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed"
    publisher: "Rapid7"
    date: "2026-11-18"
    role: corroborating
  - url: "https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities"
    publisher: "Wiz Research"
    date: "2026-11-18"
    role: corroborating
  - url: "https://xint.io/blog/nginx2root-remote-code-execution"
    publisher: "Xint"
    date: "2026-11-18"
    role: corroborating
  - url: "https://github.com/sfewer-r7/CVE-2026-123007"
    publisher: "Rapid7 proof-of-concept repository"
    date: "2026-11-18"
    role: corroborating
  - url: "https://cert.europa.eu/publications/security-advisories/2026-022/"
    publisher: "CERT-EU"
    date: "2026-11-18"
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/13203"
    publisher: "NCSC.ch Cyber Security Hub"
    date: "2026-11-18"
    role: corroborating
  - url: "https://advisories.ncsc.nl/2026/ncsc-2026-0506.html"
    publisher: "NCSC-NL"
    date: "2026-11-18"
    role: corroborating
  - url: "https://www.cert.at/de/warnungen/2026/11/kritische-sicherheitslucken-in-nginx-plus-und-nginx-open-source-updates-verfugbar"
    publisher: "CERT.at"
    date: "2026-11-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "All five vulnerabilities can lead to unauthenticated code execution with the privileges of the NGINX worker process"
    publisher: "CERT-EU"
    source_url: "https://cert.europa.eu/publications/security-advisories/2026-022/"
  - quote: "no exploitation in the wild has been reported yet"
    publisher: "CERT-EU"
    source_url: "https://cert.europa.eu/publications/security-advisories/2026-022/"
  - quote: "Leveraging CVE-2026-123007 for RCE requires a significant amount of network traffic to be transmitted, approximately 128 GB of HTTP/2 data."
    publisher: "Rapid7"
    source_url: "https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed"
  - quote: "Our testing of CVE-2026-123007 demonstrated code execution on NGINX serving ordinary static files, without a backend application or third-party modules."
    publisher: "Wiz Research"
    source_url: "https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities"
  - quote: "Until then, disabling HTTP/2 on affected listening ports blocks CVE-2026-123007 and CVE-2026-123633. It does not block the other three nginx vulnerabilities."
    publisher: "Xint"
    source_url: "https://xint.io/blog/nginx2root-remote-code-execution"
  - quote: "After installing the update, restart nginx or complete a supported live binary upgrade. A configuration reload alone does not replace the running executable."
    publisher: "Xint"
    source_url: "https://xint.io/blog/nginx2root-remote-code-execution"
verification: multi-source
sourcing_note: >
  nginx.org carries the per-flaw vulnerable ranges and the fixed releases, but its advisories page is a living listing with no dateline, so the 2026-11-18 date comes from the other sources; F5's K-articles are not publicly readable, so the NGINX Plus fixed builds and the unfixed R-releases come from Rapid7, Wiz and CERT.at, which differ on the R-release range: Wiz gives R33 for CVE-2026-123633 and CVE-2026-123007, CERT-EU and CERT.at give R34 to R36 for them (Rapid7 does so for CVE-2026-123007), and CERT.at gives R33 only for CVE-2026-113425; the entry follows the majority, and no cited source itemises NGINX Plus ranges for CVE-2026-123634, whose Plus fix is presumed to be the same builds. CERT-EU quotes a score of 8.1 for the flaws and NCSC.ch, NCSC-NL and Rapid7 CVSS 4.0 9.2, the score recorded here. Xint's first-affected releases for the resolver and mail-proxy flaws differ from nginx.org's, whose values are used. Rapid7's exploit is for CVE-2026-123007 only; Wiz did not publish its exploits, and Xint reports code execution for the flaws it found.
confidence: high
references: ["2026-10-20/nginx-three-unauth-heap-corruption-flaws-fixed-1-30-6", "2026-06-19/cve-2026-42530-cve-2026-42055-nginx-http-3-quic-use-after-fr"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Update every internet-facing nginx to 1.31.9 or 1.30.7 (NGINX Plus to 37.3.0.1 or 37.0.8.1) and restart the process, because a reload does not replace the running executable; where the update waits, disable HTTP/2 on exposed listeners, which blocks only CVE-2026-123007 and CVE-2026-123633, since five unauthenticated flaws reach code execution as the worker and Rapid7's proof of concept for one of them is public."
updates: []
migrated_from: null
---

F5 and the nginx project published the nginx2root fixes ([nginx.org, 2026-11-18](https://nginx.org/en/security_advisories.html)); CERT-EU counts five vulnerabilities, all able to lead to unauthenticated code execution with the privileges of the NGINX worker process ([CERT-EU, 2026-11-18](https://cert.europa.eu/publications/security-advisories/2026-022/)). CVE-2026-123007 is an HTTP/2 flow-control overflow: cancelling queued response data makes nginx use an invalid length when copying a later response ([Rapid7, 2026-11-18](https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed)), and Wiz demonstrated code execution on nginx serving ordinary static files ([Wiz Research, 2026-11-18](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)).

Rapid7 published a working proof of concept for CVE-2026-123007 against nginx 1.31.8; the exploit needs about 128 GB of HTTP/2 traffic and likely fails with concurrent clients ([Rapid7, 2026-11-18](https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed); [Rapid7 repository, 2026-11-18](https://github.com/sfewer-r7/CVE-2026-123007)). Rapid7 says execution has the worker's permissions and root is not established; F5, as CERT.at relays it, frames the base effect as worker crashes, with code execution possible where ASLR is disabled or can be bypassed, which Wiz says attackers can do by reading memory first (translated from German) ([Rapid7, 2026-11-18](https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed); [CERT.at, 2026-11-18](https://www.cert.at/de/warnungen/2026/11/kritische-sicherheitslucken-in-nginx-plus-und-nginx-open-source-updates-verfugbar); [Wiz Research, 2026-11-18](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)). CERT-EU reports no exploitation in the wild, NCSC.ch rates exploitation unknown with a proof of concept available, and NCSC-NL expects large-scale exploitation once proof-of-concept code is public (translated from Dutch) ([CERT-EU, 2026-11-18](https://cert.europa.eu/publications/security-advisories/2026-022/); [NCSC.ch, 2026-11-18](https://security-hub.ncsc.admin.ch/#/posts/13203); [NCSC-NL, 2026-11-18](https://advisories.ncsc.nl/2026/ncsc-2026-0506.html)).

The fixes are in nginx 1.31.9 and 1.30.7 ([nginx.org, 2026-11-18](https://nginx.org/en/security_advisories.html)). CERT.at lists NGINX Plus 37.3.0.1 and 37.0.8.1 as fixing four of the five (CVE-2026-123007, CVE-2026-121810, CVE-2026-123633 and CVE-2026-113425); it also says 37.2.0.1 and 37.0.7.1 already carry the fix for CVE-2026-123633 but stay affected by CVE-2026-123007 and CVE-2026-121810, and NGINX Plus R33 to R36 have no update (translated from German) ([CERT.at, 2026-11-18](https://www.cert.at/de/warnungen/2026/11/kritische-sicherheitslucken-in-nginx-plus-und-nginx-open-source-updates-verfugbar)).

**Exposure:** an nginx build from the first affected release of each flaw (1.9.5, 1.19.7, 0.6.18, 1.25.0 and 0.5.33) up to 1.31.8 whose configuration uses the feature: an HTTP/2 or HTTP/3 listener, the resolver with variable proxy_pass destinations plus mirror or SSI, or the mail proxy with auth_http ([nginx.org, 2026-11-18](https://nginx.org/en/security_advisories.html); [Xint, 2026-11-18](https://xint.io/blog/nginx2root-remote-code-execution)). A distribution backport can fix a flaw without changing the version nginx -v reports ([Xint, 2026-11-18](https://xint.io/blog/nginx2root-remote-code-execution)).

**Detection:** process-creation or audit telemetry for any program started by the worker's user, since a normal nginx worker runs no external programs and that is the clearest sign of success; worker exits and core dumps in the error log mark attempts, not successes ([Xint, 2026-11-18](https://xint.io/blog/nginx2root-remote-code-execution); [CERT-EU, 2026-11-18](https://cert.europa.eu/publications/security-advisories/2026-022/)). Network flow data showing a long-lived TLS connection with fast-growing received volume and little sent data, and many short connections from the same address, hints at CVE-2026-123007 ([Xint, 2026-11-18](https://xint.io/blog/nginx2root-remote-code-execution)).

**Triage:** a large upload is a legitimate cause of an inbound-heavy connection and workers crash for unrelated reasons, so a program started by the worker is the discriminator, not the traffic shape alone ([Xint, 2026-11-18](https://xint.io/blog/nginx2root-remote-code-execution)).

**Defender takeaway:** update and restart nginx, because a configuration reload does not replace the running executable; disabling HTTP/2 on exposed listeners blocks only the two HTTP/2 flaws, and Xint gives interim measures for the others: a fixed upstream group in place of request-time DNS lookups for CVE-2026-123634, no QUIC listeners for CVE-2026-121810 and bound or firewalled mail listeners for CVE-2026-113425 ([Xint, 2026-11-18](https://xint.io/blog/nginx2root-remote-code-execution)). An empty execution-audit result after the update cannot rule out an earlier compromise, and Xint chained CVE-2026-123007 with a separate Linux kernel SCTP flaw, unpatched when it published, to reach root on the host and escape a Docker container; hosts that do not use SCTP can block the module from loading ([Xint, 2026-11-18](https://xint.io/blog/nginx2root-remote-code-execution)).
