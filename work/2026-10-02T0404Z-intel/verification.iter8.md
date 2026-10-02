**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-02T08:50:19Z · ended_at=2026-10-02T09:09:53Z · duration_seconds=1174

## Verification report — 2026-10-02T0404Z-intel (iteration 8)

Scope: post-fix pass, fresh cold read. All 295 claims in claims.iter8.yaml have a verdict row in verification.iter8.claims.yaml (`claim_ledger.py --coverage 8`: 295/295, 0 missing): the 8 changed claims, every claim of the six remediated entries (Citrix, UNCTAD, Belnet, Kiteworks, SDIS, KillSwitch) and every claim of the other nine entries as well (no sampling). Derived and uncited analysis rows carry a paraphrased supporting passage, labelled as such; cited rows carry the source text.

### Iteration-7 deltas (all eight re-checked against the source)
- Citrix Triage (claim 187baa5776): fixed correctly. watchTowr Labs shows the injected text shaped as 'pitboss PPE unexpectedly died NSPPE;...' and Unit 42 shows 'pitboss PPE missed too many heartbeatsNSPPE;<additional text>'; 'imitates the packet engine's crash message and carries command text after it' matches both.
- UNCTAD dates (bbd74b3b5d): fixed correctly. Transluce page dated 2026-09-30, Asymmetric Security page dated 2026-10-01; the summary now names each separately.
- Belnet summary (ee69e2093b): fixed ('generated and sent directly'). The title still says 'FileSender download links' (finding #4 below, residual).
- Kiteworks 'No CVE was known' (f957ebb904, 19abaf8cbf): supported. The Record quotes watchTowr's Knott 'There is no known CVE, patch, or additional technical details available'; BleepingComputer (2026-10-01) later says no CVE ID was assigned for the vulnerability fixed during the shutdown.
- Censys links: fixed. Canonical page fetched, same body as the old slug; no leftover cve-2026-10747 link in any entry. The Objectif Gard links in SDIS now point to objectifsud.fr, whose body carries the evidence quotes verbatim.
- Citrix record summary (18cc653770): states the Triage rewrite, the agency wording, the BleepingComputer clause and the link fix; matches git diff HEAD. (The inline CERT.at link added to the takeaway is not named; immaterial.)
- UNCTAD composition language (4eb9f4d0e2): removed; the replacement sentence is hunt-relevant. One part of it is looser than the sources (finding #2).
- KillSwitch '500 of the 1,000' (bb68e9c2df): fixed and matches Polizei Hamburg ('rund 1.000 ... Rund 500 der mutmaßlichen Angriffe ... erfolgreich identifiziert').

### Editorial: missed angles
**#1 (F10)** Apple CoreGraphics CVE-2026-86950, existing entry 2026-09-30/cve-2026-86950-apple-coregraphics-zero-day-kev (priority high, KEV-listed). The Hacker News, 2026-10-01, 'Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path' (https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html): Calif published a public PoC on 2026-09-30 (crafted TrueType font in a PDF, out-of-bounds write via float-to-fixed conversion; triggers a crash, not code execution; github.com/califio/publications; https://calif.io/research/the-great-glyph-grift). Within the 50 h window. The store entry has no PoC mention (grep for poc/proof returns nothing), no `poc-public` status and says 'No source states how the file is delivered'. findings.S1 and S3 marked the item 'no delta' after reading only Apple's pages and aggregators. A public exploit for an exploited iOS/macOS zero-day is a changelog update on that entry. Search query: 'CVE-2026-86950 Calif great glyph grift proof of concept'. Coverage otherwise looks complete: the KEV window (CVE-2026-76504, CVE-2026-104286) is covered, TeamViewer (not exploited, no PoC), MikroTik (held backlog row), Bitget, MetaMask and the THN/BleepingComputer items of 2026-09-30 to 2026-10-02 are either covered or correctly dropped.

### Unsupported / overstated
**#2 (F4, low confidence)** OpenAI agents UNCTAD, update closing sentence (claim 4eb9f4d0e2): 'The cases name no Swiss target and no confirmed intrusion'. Asymmetric opens with 'We found successful access to staging environments' and says AIHW's pre-production system 'returned data ... As far as we know, this data was all publicly available'. The sources support 'no confirmed access to non-public data' (Transluce, Cyber Centre), not 'no confirmed intrusion'.

### Quantifier without source
**#3 (F14, low confidence)** Zimbra, analysis paragraph (claim 94466b080a): 'had nothing to match against for four weeks'. Release 2026-07-20 (Zimbra page), CVE published 2026-08-13 (ENISA): 24 days. The cited sentence hedges ('nearly four weeks'); the analysis does not.
**#4 (F14, low confidence)** Belnet title: 'copy all incoming mail to Belnet-owned domains and FileSender download links for 65 days'. Belnet: 'All download links generated and sent directly by our FileSender and FedSender services'. The iteration-7 finding named the title; only the summary was fixed.

### Editorial / less-is-more flags (advisory)
**#5 (F11, low confidence)** Kiteworks sourcing_note (pre-existing): 'Credibility reflects that the advisory's issuance is well documented...' is workflow-internal vocabulary (Admiralty credibility digit) in a reader-facing field, in a three-sentence note where two sentences of provenance suffice.
**#6 (F11, low confidence)** UNCTAD body paragraph 2: 'appear in the proxy's own logged request list' reads as codetabs' log; the source says Urlquery's report of fetched URLs.
**#7 (F11, low confidence)** Citrix: Censys cited as 2026-09-29 (sources[] and two 2026-09-30 section citations); the canonical page carries datePublished 2026-09-30T16:54:05Z and the title 'Sept 28 Advisory'.

### What was checked and held
Citrix: CTX697096 table and fixed builds, watchTowr FAQ and Labs, CERT-EU, CERT.at, NCSC-NL (v1.0.0 2026-09-27 16:55), NCSC-CH 13005, NCSC UK, CERT-FR, KEV rows (2026-09-27 and the forensic-triage requiredAction), BleepingComputer, GTIG artefacts and interim controls, Tenable, Censys counts, and every Unit 42 claim of the new section (dates, paths, three-stage chain, 50,277, the Oct. 1 footnote does not affect the 2026-09-30 content). UNCTAD: swarmcha.se, SiliconANGLE, Transluce (200,000 requests, 899 requests with 13 payloads, 'oai' tag, Navy, API-key reuse), Asymmetric, Cyber Centre. Belnet: 22 July to 25 September = 65 days, 'sent directly', Risky Bulletin. Kiteworks: eight GHSA pages (CVE ids, CVSS 3.1 vectors recomputed to 10.0/9.8/9.8/9.8/9.4/9.3/7.2/7.2, CWE classes, 2026-09-30 dates, EPSS 0.00332 from FIRST), BleepingComputer 2026-10-01, The Record, Heise, TechCrunch, Kiteworks pages. SDIS 66: ICI body, Mercredi = 2026-09-30, quotes verbatim with originals. KillSwitch: Polizei Hamburg, fedpol, Europol (datePublished 2026-10-01). Zimbra: Microsoft blog, Zimbra 10.1.20/10.1.21 pages and advisory table, ENISA (EU KEV 2026-08-18, CISA KEV 2026-08-21, CVSS vector computes to 8.9), CERT-FR (19 août), NCSC-CH 13022, FIRST EPSS 0.11736. FortiMail, Cisco, Zammad, FTAPI, Stadt Wien, UAT-11587, ANSSI and Adobe: primaries read, all claims held; KEV 2026.10.01 contains none of the Adobe, Kiteworks or Zammad CVEs and lists CVE-2026-104286 (2026-10-01), CVE-2026-76504 (2026-09-30), CVE-2026-88771/88772 (2026-09-27), CVE-2026-73570 (2026-08-21). Style: no em dash outside `## Update` headings, no IOCs, no KEV deadline used as a reason to act. Registry keys all resolve. Classification blocks present and consistent. Priorities: Cisco and FortiMail critical (exploited, no workaround or no fixed build) hold; Kiteworks high and Adobe notable are earlier declines and unchanged.

### Verdict
NEEDS_FIXES (truth: 3, editorial: 1, advisory: 3). Truth items are all low confidence; the one editorial item is the Apple CoreGraphics proof of concept.

### Findings summary (machine-readable)
See verification.iter8.findings.yaml.
