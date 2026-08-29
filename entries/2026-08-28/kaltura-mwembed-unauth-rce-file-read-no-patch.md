---
schema: 1
kind: vulnerability
title: "Kaltura mwEmbed/html5lib video player: unauthenticated RCE and arbitrary file read via an undocumented ServiceUrl parameter — no vendor response, no patch, 630+ exposed instances found by the discoverer"
headline: "A single undocumented request parameter lets an unauthenticated visitor control what a shared, multi-tenant media platform fetches and deserializes"
summary: >
  Two unauthenticated vulnerabilities in Kaltura's mwEmbed/html5lib video-player library are
  reachable with no session, token or user interaction. CVE-2026-19913 (CVSS 9.1) yields
  arbitrary local file read; CVE-2026-19912 (CVSS 10.0) chains an unchecked path-traversal cache
  write with unauthenticated PHP object injection to reach remote code execution. The
  vulnerable code is confirmed unchanged in the current release. Disclosure attempts spanning five
  months across email, LinkedIn and CERT/CC involvement produced no vendor response.
discovered_at: "2026-08-28T06:00:00Z"
updated_at: null
event_date: "2026-08-26"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, info-disclosure, pre-auth, no-patch]
regions: [global, europe]
sectors: [public-sector, technology, education]
entities: []
techniques: [T1190]
affected_products: ["Kaltura HTML5 Player Library (mwEmbed / html5lib)", "Kaltura Server"]
cves:
  - id: CVE-2026-19912
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "Kaltura Server / mwEmbed — confirmed unchanged through current West-23.5.0 release; validated end-to-end against a 2019-era 14.12.0 Docker image"
    fixed: "None available"
  - id: CVE-2026-19913
    cvss: "9.1"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "Kaltura Server / mwEmbed — confirmed unchanged through current West-23.5.0 release"
    fixed: "None available"
sources:
  - url: "https://anddone-git.github.io/2026/one-parameter-two-bugs/"
    publisher: "AndDone (Gerjan Wemekamp)"
    date: "2026-08-26"
    role: primary
  - url: "https://kb.cert.org/vuls/id/308749"
    publisher: "CERT/CC"
    date: "2026-08-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "getFilePath() builds the on-disk destination by concatenating the cache base directory with a path derived from the uiconf_id request parameter, with no sanitisation"
    publisher: "AndDone (Gerjan Wemekamp)"
  - quote: "was unable to reach Kaltura to coordinate these vulnerabilities"
    publisher: "CERT/CC"
verification: single-source
sourcing_note: >
  AndDone (Gerjan Wemekamp) is the discoverer and sole publisher; the technical write-up is
  demonstrated end-to-end (file-read path against a live bug-bounty target and the current
  codebase, full RCE chain against a 2019-era Docker image). CERT/CC's own vulnerability-note page
  (kb.cert.org/vuls/id/308749) returned a corrupted/binary body on every transport this run, so
  its "unable to reach Kaltura" statement is carried at reduced confidence via a prior WebFetch
  summarization rather than a verbatim re-read.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Block or heavily restrict access to mwEmbedLoader.php at a WAF/reverse-proxy/CDN layer on every internet-facing Kaltura deployment — no vendor fix exists, and this is the only available control. Reject non-http(s) ServiceUrl values and deny PHP execution rights in cache directories as a compensating measure."
  - "Where Kaltura is deployed as shared, multi-tenant CDN/hosting infrastructure (common in higher-education lecture-capture and media-hosting environments), treat a single exposed mwEmbedLoader.php as putting every tenant on that host at risk, and prioritise the WAF-level block across the whole shared platform rather than per-tenant."
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [body]
migrated_from: null
---

Two unauthenticated vulnerabilities exist in Kaltura's mwEmbed/html5lib video-player library, reachable at the `mwEmbedLoader.php` endpoint with no session, token or user interaction. The root cause is an undocumented `ServiceUrl` request parameter that lets the caller control the URL the server fetches data from: `KalturaClientBase.php`'s `doQueue()` function concatenates it unchecked into a request URL with no origin or scheme validation, then feeds the fetched response through PHP's `unserialize()` with no signature check, origin check, or class allow-list.

CVE-2026-19913 (CVSS 9.1): supplying a `file://` scheme in `ServiceUrl` makes the application fetch and attempt to deserialize an internal file's contents; failed-deserialization error messages reflect the raw file bytes back to the client, yielding arbitrary local file read. CVE-2026-19912 (CVSS 10.0): the `uiconf_id` request parameter is concatenated unsanitized into the on-disk cache-file destination path — "`getFilePath()` builds the on-disk destination by concatenating the cache base directory with a path derived from the `uiconf_id` request parameter, with no sanitisation" ([AndDone (Gerjan Wemekamp), 2026-08-26](https://anddone-git.github.io/2026/one-parameter-two-bugs/)) — so path-traversal sequences in `uiconf_id` escape the cache directory; combined with the unchecked `unserialize()` above (PHP object injection), this reaches unauthenticated remote code execution when the default file-based cache backend is in use and PHP execution is not blocked in the cache directory.

The discoverer fully demonstrated the file-read path against a production bug-bounty target and the current codebase, and validated the full RCE chain end-to-end against a 2019-era Kaltura Server Docker image (14.12.0) — the vulnerable code is confirmed unchanged in the current West-23.5.0 release, though no current-release container was available to re-run the full RCE demonstration against. The discoverer found 630+ indexed, internet-facing Kaltura instances via a search query. Disclosure attempts spanned personal email (23 March 2026), corporate email (13 April), LinkedIn escalation (23 May) and national CERT involvement (2 July); CERT/CC states it "was unable to reach Kaltura to coordinate these vulnerabilities" ([CERT/CC, 2026-08-26](https://kb.cert.org/vuls/id/308749)), and no vendor response or patch exists as of 2026-08-28. Because Kaltura is frequently deployed as shared, multi-tenant CDN/hosting infrastructure, a single exposed `mwEmbedLoader.php` can put every tenant served by that shared host at risk. Kaltura's video platform is widely used by universities and research institutions for lecture capture and media hosting, a use case common across Swiss and EU academic institutions.

**Triage:** any inbound request to `mwEmbedLoader.php` carrying a `ServiceUrl` parameter with a non-`http(s)` scheme (`file://` in particular), or a `uiconf_id` value containing path-traversal sequences (`../`, encoded variants), has no legitimate explanation — normal player-loading traffic never sets `ServiceUrl` to a local-file scheme or supplies a traversal-shaped `uiconf_id`. With no vendor fix available, WAF-level pattern blocking on those two parameter shapes is the only mitigation short of taking the endpoint offline entirely.
