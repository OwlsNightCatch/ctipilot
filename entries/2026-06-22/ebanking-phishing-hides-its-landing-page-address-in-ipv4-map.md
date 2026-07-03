---
schema: 1
kind: research
horizon: operational
title: eBanking phishing hides its landing-page address in IPv4-mapped IPv6 notation to slip past URL scanners
headline: eBanking phishing hides its landing-page address in IPv4-mapped IPv6 notation to slip past URL scanners
summary: "A live eBanking phishing campaign against a Belgian bank hides its landing-page address in IPv4-mapped IPv6 notation ([::ffff:…]), which browsers resolve normally but regex-based URL scanners and DNS-reputation lookups miss entirely (SANS ISC, 2026-06-19). Email-gateway and proxy teams should test whether their URL extractors handle the [::ffff:…] form."
discovered_at: "2026-06-22T04:52:28Z"
event_date: 2026-06-19
run_id: 2026-06-22-dece656d
priority: high
immediate_action: null
tags:
  - phishing
regions:
  - europe
sectors:
  - finance
  - public-sector
entities: []
cves: []
sources:
  - url: "https://isc.sans.edu/diary/33090"
    publisher: SANS ISC
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
migrated_from: briefs/2026-06-22.md
---

SANS ISC handler Xavier Mertens documented an active phishing campaign against customers of a major Belgian bank that encodes the destination address as an IPv4-mapped IPv6 literal — the `[::ffff:…]` bracketed form, where the dotted-decimal IPv4 address is rewritten as its hexadecimal IPv6 representation inside square brackets ([SANS ISC, 2026-06-19](https://isc.sans.edu/diary/33090)). Modern browsers resolve the form correctly per RFC 4291 and render the phishing page normally, but two defensive layers fail on it: regex-based URL extractors in email gateways and proxies typically match the dotted-decimal IPv4 pattern (`\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`) and never see the hexadecimal IPv6 form as an address at all, and because no DNS record is involved, domain-reputation lookups return nothing to score. The technique is delivery-agnostic — any link-based vector (spearphishing link, HTML attachment, QR redirect) inherits the same inspection blind spot. The RFC-level notation is old; the operational novelty is its appearance as a live evasion in commodity banking phishing (`T1598.003` Spearphishing Link; `T1027` Obfuscated Files or Information). `[SINGLE-SOURCE]` — SANS ISC is the disclosing party (PD-5 national-CERT-equivalent carve-out);

**Why it matters to us:** Swiss cantonal banks, PostFinance, and any organisation running URL-rewriting or reputation-based mail/web inspection should test their stack against a controlled `[::ffff:<ipv4>]`-style URL and confirm the extractor normalises IPv4-mapped IPv6 to its IPv4 form *before* the reputation lookup, not after. Hunting: update SIEM/proxy URL-extraction patterns to capture the `\[::ffff:[0-9a-fA-F:]+\]` shape, and treat bracketed-IPv6 URLs in inbound mail as high-suspicion regardless of reputation verdict.
