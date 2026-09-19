---
schema: 1
kind: vulnerability
title: "Kaltura mwEmbed/html5lib video player: unauthenticated RCE and arbitrary file read via an undocumented ServiceUrl parameter; patched for legacy Player V2 after months of no vendor response, 630+ exposed instances found by the discoverer"
headline: "A single undocumented request parameter lets an unauthenticated visitor control what a shared, multi-tenant media platform fetches and deserializes"
summary: >
  Two unauthenticated vulnerabilities in Kaltura's mwEmbed/html5lib video-player library are
  reachable with no session, token or user interaction. CVE-2026-19913 (CVSS 9.1) yields
  arbitrary local file read; CVE-2026-19912 (CVSS 10.0) chains an unchecked path-traversal cache
  write with unauthenticated PHP object injection to reach remote code execution. The
  vulnerable code is confirmed unchanged in the current release. Disclosure attempts spanning five
  months across email, LinkedIn and CERT/CC involvement produced no vendor response; patches for the
  affected legacy Player V2 line appeared on 2026-08-28 (see the update below).
discovered_at: "2026-08-28T06:00:00Z"
updated_at: "2026-08-30T13:12:06Z"
event_date: "2026-08-26"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, info-disclosure, pre-auth]
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
    status: [patch-available]
    affected: "Kaltura legacy Player V2 / mwEmbed (html5lib v2.x), self-hosted deployments included; not the supported Player V7"
    fixed: "Patched legacy Player V2 release (Kaltura, per CERT/CC VU#308749, 2026-08-28)"
  - id: CVE-2026-19913
    cvss: "9.1"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Kaltura legacy Player V2 / mwEmbed (html5lib v2.x), self-hosted deployments included; not the supported Player V7"
    fixed: "Patched legacy Player V2 release (Kaltura, per CERT/CC VU#308749, 2026-08-28)"
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
  - quote: "Kaltura has released new patches to remediate these vulnerabilities in all affected legacy Player V2 versions."
    publisher: "CERT/CC"
verification: single-source
sourcing_note: >
  AndDone (Gerjan Wemekamp) is the discoverer and sole publisher; the technical write-up is
  demonstrated end-to-end (file-read path against a live bug-bounty target and the current
  codebase, full RCE chain against a 2019-era Docker image). CERT/CC's own vulnerability-note page
  (kb.cert.org/vuls/id/308749) is a living advisory and has been revised since this was written.
  The 2026-08-26 revision recorded that CERT/CC could not reach Kaltura to coordinate; the
  2026-08-28 revision replaced that with the patch announcement quoted in the update below, so the
  earlier coordination-failure statement is no longer retrievable from the page and is not quoted
  here. The disclosure timeline above rests on the discoverer's own write-up, which is
  first-party for it. Every CERT/CC quotation here is verbatim from the current revision,
  retrieved in full through the reader proxy on 2026-08-30.
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
  - at: "2026-08-30T13:12:06Z"
    run_id: 2026-08-30T1312Z-audit
    type: update
    summary: >
      Kaltura has patched. CERT/CC updated VU#308749 on 2026-08-28 at 19:59 UTC, after this entry
      was written, to state that patches now exist for every affected legacy Player V2 version,
      and to scope the flaws to that legacy line only: the currently supported Player V7 is not
      affected. Both CVE records move from no-patch to patched with the fixed release named, and
      the title, tags, summary and body no longer present this as an unpatched exposure.
    fields: [title, summary, tags, cves, sourcing_note, evidence, body, updated_at]
migrated_from: null
---

Two unauthenticated vulnerabilities exist in Kaltura's mwEmbed/html5lib video-player library, reachable at the `mwEmbedLoader.php` endpoint with no session, token or user interaction. The root cause is an undocumented `ServiceUrl` request parameter that lets the caller control the URL the server fetches data from: `KalturaClientBase.php`'s `doQueue()` function concatenates it unchecked into a request URL with no origin or scheme validation, then feeds the fetched response through PHP's `unserialize()` with no signature check, origin check, or class allow-list.

CVE-2026-19913 (CVSS 9.1): supplying a `file://` scheme in `ServiceUrl` makes the application fetch and attempt to deserialize an internal file's contents; failed-deserialization error messages reflect the raw file bytes back to the client, yielding arbitrary local file read. CVE-2026-19912 (CVSS 10.0): the `uiconf_id` request parameter is concatenated unsanitized into the on-disk cache-file destination path — "`getFilePath()` builds the on-disk destination by concatenating the cache base directory with a path derived from the `uiconf_id` request parameter, with no sanitisation" ([AndDone (Gerjan Wemekamp), 2026-08-26](https://anddone-git.github.io/2026/one-parameter-two-bugs/)) — so path-traversal sequences in `uiconf_id` escape the cache directory; combined with the unchecked `unserialize()` above (PHP object injection), this reaches unauthenticated remote code execution when the default file-based cache backend is in use and PHP execution is not blocked in the cache directory.

The discoverer fully demonstrated the file-read path against a production bug-bounty target and the current codebase, and validated the full RCE chain end-to-end against a 2019-era Kaltura Server Docker image (14.12.0) — the vulnerable code is confirmed unchanged in the current West-23.5.0 release, though no current-release container was available to re-run the full RCE demonstration against. The discoverer found 630+ indexed, internet-facing Kaltura instances via a search query. Disclosure attempts spanned personal email (23 March 2026), corporate email (13 April), LinkedIn escalation (23 May) and national CERT involvement (2 July); CERT/CC's advisory recorded at that point that it had been unable to reach the vendor to coordinate, a statement its 2026-08-28 revision replaced with the patch announcement ([CERT/CC, VU#308749](https://kb.cert.org/vuls/id/308749)), and no vendor response or patch existed when this was first reported. Because Kaltura is frequently deployed as shared, multi-tenant CDN/hosting infrastructure, a single exposed `mwEmbedLoader.php` can put every tenant served by that shared host at risk. Kaltura's video platform is widely used by universities and research institutions for lecture capture and media hosting, a use case common across Swiss and EU academic institutions.

**Triage:** any inbound request to `mwEmbedLoader.php` carrying a `ServiceUrl` parameter with a non-`http(s)` scheme (`file://` in particular), or a `uiconf_id` value containing path-traversal sequences (`../`, encoded variants), has no legitimate explanation — normal player-loading traffic never sets `ServiceUrl` to a local-file scheme or supplies a traversal-shaped `uiconf_id`. With no vendor fix available, WAF-level pattern blocking on those two parameter shapes is the only mitigation short of taking the endpoint offline entirely.

## Update — 2026-08-30T13:12:06Z

Kaltura has released patches. CERT/CC updated VU#308749 on 2026-08-28 at 19:59 UTC, hours after this entry was published, and now states: "Kaltura has released new patches to remediate these vulnerabilities in all affected legacy Player V2 versions. Customers using legacy players, including self-hosted legacy player deployments (html5lib v2.x), should update to the patched version or, preferably, migrate to the newer and currently supported Kaltura Player V7 platform" ([CERT/CC, VU#308749, updated 2026-08-28](https://kb.cert.org/vuls/id/308749)).

The same update narrows the affected estate, which this entry had left open: "only versions of the legacy player (Player V2) are vulnerable; these issues do not affect any versions of the currently supported Kaltura Player V7" (same advisory). So the scoping question for an institution running Kaltura is which player line its deployment sits on, not whether it is on a current server release, and self-hosted html5lib v2.x deployments are explicitly in scope. The 630+ internet-facing instances the discoverer found do not become safe by the patch existing; each still has to be updated or migrated.
