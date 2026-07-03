---
schema: 1
kind: research
horizon: operational
title: "SANS ISC: SVG phishing wave abuses a non-standard MIME type to slip past WAF/email pattern-matching"
headline: "SANS ISC: SVG phishing wave abuses a non-standard MIME type to slip past WAF/email pattern-matching"
summary: "SANS ISC handler Xavier Mertens documented a fresh wave of phishing emails carrying SVG attachments whose embedded JavaScript is obfuscated with combined Base64 + XOR encoding and, on decode, redirects the victim via window.location.href to a credential-harvesting page (SANS ISC, 2026-06-02)."
discovered_at: "2026-06-03T05:00:06Z"
event_date: 2026-06-02
run_id: 2026-06-03-ee0eae61
priority: notable
immediate_action: null
tags:
  - phishing
  - infostealer
regions:
  - global
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://isc.sans.edu/diary/33040"
    publisher: SANS Internet Storm Center
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-03.md
---

SANS ISC handler Xavier Mertens documented a fresh wave of phishing emails carrying SVG attachments whose embedded JavaScript is obfuscated with combined Base64 + XOR encoding and, on decode, redirects the victim via `window.location.href` to a credential-harvesting page ([SANS ISC, 2026-06-02](https://isc.sans.edu/diary/33040)). The notable evasion is the use of `<script type="application/ecmascript">` instead of the standard `text/javascript` — browsers execute both identically, but email-security and WAF products that pattern-match specifically on `text/javascript` can miss the non-standard declaration. Because SVGs open natively in Windows browsers, the redirect fires on file open with no extra click. [SINGLE-SOURCE] (SANS Internet Storm Center). Detection: flag email attachments of `Content-Type: image/svg+xml` that contain embedded `<script>` elements; treat the `application/ecmascript`/`application/javascript` MIME variants as equivalent to `text/javascript` in inspection rules; sandbox SVG attachments before delivery and watch newly-registered low-cost TLDs (the campaign used a `.cfd` domain) at the proxy.
