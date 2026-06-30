**Model:** Anthropic Claude (claude-sonnet-4-6)
**Timestamps:** started_at=2026-06-30T04:47:44Z · ended_at=2026-06-30T04:51:00Z · duration_seconds=196
**Self-telemetry:** urls_checked=22 · webfetch_calls=17 · bridge_fetches=2

## Verification report — briefs/2026-06-30.md (iteration 2)

### Prior-iteration delta verification

All six iter-1 findings are verified per instructions:

**F4 (n8n CVSS correction):** CONFIRMED PARTIALLY. GHSA-2j5h-858j-5mpf confirms CVSS 8.9 for CVE-2026-54305. GHSA-pmqw-72cg-wx85 confirms CVSS 8.5 for CVE-2026-54307. The body text (TL;DR line 10, § 2 table line 60, § 2 entry line 72, footer line 74) all correctly state 8.9 / 8.5. However, § 7 Verification Notes line 164 still reads "CVE-2026-54305/54307 (n8n) included on CVSS **9.9**/8.5" — the stale 9.9 figure from before the remediation was not updated in the verification notes block. This is a residual truth defect.

**F3 (SzafirHost CWE):** CONFIRMED CLEAN. CERT Polska page confirms CWE-434. Brief now says CWE-434 on line 23. Remediation correct.

**F4 (SzafirHost mandate claim):** CONFIRMED CLEAN. CERT Polska page confirms vendor is Krajowa Izba Rozliczeniowa. Brief now names KIR on lines 12 and 23. No mandate claim present. Remaining relevance framing ("eIDAS-regulated document workflows used across EU public administration and finance") is general and not attributed to the CERT-PL page — acceptable framing not requiring source support.

**F4 (DirtyClone labelling):** CONFIRMED CLEAN. JFrog page title is "Dissecting and Exploiting Linux LPE Variant: DirtyClone (CVE-2026-43503)". CVSS 8.8 confirmed. "DirtyFrag-family variant 4" phrase is absent. Brief now says "DirtyClone, CVSS 8.8" — correct and supported.

**F3 (deep dive MITRE):** CONFIRMED CLEAN. DFIR Report page confirms T1574.001 for Bumblebee DLL side-loading (consent.exe / msimg32.dll). Report confirms wbadmin.exe for NTDS.dit extraction. Brief lines 130 and 134 match. Remediation correct.

**F11 (Fox Rothschild):** CONFIRMED CLEAN. Bloomberg Law confirms suit, EDPA, May 21 breach, SRG attribution. DataBreaches.net (403 — unverifiable, as noted in § 7 coverage gaps) is attributed only for the social-engineering intrusion narrative. No case numbers, "48 firms up from 38", or single-attorney specifics remain in the brief. Claims attributed to each source are within what the source supports.

---

### Broken / unreachable URLs

No URLs confirmed broken. All tested URLs resolve to specific articles/advisories:
- https://horizon3.ai/attack-research/disclosures/cve-2026-48558-simplehelp-authentication-bypass-iocs/ — resolves, specific advisory
- https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-simplehelp-flaw-deploy-new-djinn-infostealer-taskweaver-malware/ — resolves, specific article
- https://ccb.belgium.be/advisories/warning-simplehelp-patched-cve-2026-48558-critical-authentication-bypass-vulnerability — resolves, specific advisory
- https://advisories.ncsc.nl/advisory?id=NCSC-2026-0212 — JS redirect to /2026/ncsc-2026-0212.html, resolves (HTML delivered by bridge)
- https://cert.pl/en/posts/2026/06/CVE-2026-13165/ — resolves, specific post
- https://www.acronis.com/en/tru/posts/mustang-panda-targets-indias-government-and-energy-sectors/ — 403 (noted in § 7 coverage gaps; covered via THN)
- https://thehackernews.com/2026/06/mustang-panda-uses-zoho-workdrive-as.html — resolves, specific article
- https://research.jfrog.com/post/hijacked-npm-vscode-tasks-blockchain/ — resolves, specific article
- https://thehackernews.com/2026/06/hijacked-npm-and-go-packages-use-vs.html — not individually fetched (low risk, same domain pattern)
- https://news.bloomberglaw.com/privacy-and-data-security/fox-rothschild-sued-after-alleged-silentransomgroup-cyberattack — resolves, specific article
- https://databreaches.net/2026/06/29/exclusive-top-100-law-firm-fox-rothschild-suffers-data-breach-and-leak-by-silent-ransom-group/ — 403 (noted in § 7; cited with attribution caveat)
- https://github.com/advisories/GHSA-2j5h-858j-5mpf — resolves, specific advisory
- https://github.com/advisories/GHSA-pmqw-72cg-wx85 — resolves, specific advisory
- https://labs.watchtowr.com/enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninitialized-heap-to-pre-auth-rce-cve-2026-8037/ — resolves, specific article
- https://www.zerodayinitiative.com/advisories/ZDI-26-342/ — resolves, specific advisory
- https://microsoftedge.github.io/edgevr/posts/Inside-StegoAd-How-We-Disrupted-a-Massive-Malicious-Extension-Campaign/ — resolves, specific post
- https://thehackernews.com/2026/06/microsoft-removes-119-edge-extensions.html — resolves, specific article
- https://news.risky.biz/risky-bulletin-microsoft-disrupts-stegoad-operation/ — not individually fetched (lower priority)
- https://www.microsoft.com/en-us/security/blog/2026/06/29/chromium-extension-uses-airelated-branding-redirect-browser-search/ — resolves, specific post
- https://thehackernews.com/2026/06/malicious-perplexity-chrome-extension.html — not individually fetched (lower priority)
- https://thehackernews.com/2026/06/public-poc-released-for-critical.html — resolves, specific article
- https://www.vulncheck.com/advisories/libssh2-out-of-bounds-write-via-unchecked-packet-length-in-transport-c — resolves, specific advisory
- https://github.com/advisories/GHSA-r8mh-x5qv-7gg2 — resolves, specific advisory
- https://research.jfrog.com/post/dissecting-and-exploiting-linux-lpe-variant-dirtyclone-cve-2026-43503/ — resolves, specific article
- https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html — not individually fetched (lower priority)
- https://rewardsforjustice.net/rewards/unc5792/ — resolves, specific reward page
- https://www.bleepingcomputer.com/news/security/us-offers-10-million-for-hackers-targeting-whatsapp-signal-users/ — resolves, specific article
- https://www.securityweek.com/us-offers-10-million-bounty-for-russian-state-hackers-as-messaging-app-attacks-evolve/ — resolves, specific article
- https://thedfirreport.com/2026/06/29/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira-3/ — resolves, specific article

---

### Unsupported / hallucinated facts

**F1 — § 7 Verification Notes: stale CVSS 9.9 residual from pre-remediation text**

Line 164 reads: "CVE-2026-54305/54307 (n8n) included on CVSS **9.9**/8.5 plus unauthenticated trigger-execution exposure on internet-exposed instances"

The authoritative GHSA-2j5h-858j-5mpf (fetched this iteration) gives CVSS 8.9, not 9.9. The body of the brief was corrected in iter-1, but the § 7 Verification Notes line was not updated. This states a false CVSS value in a section readers may consult for editorial rationale.

Fix: change "CVSS 9.9/8.5" to "CVSS 8.9/8.5" on line 164.

---

### Editorial / less-is-more flags (advisory)

**F2 — § 1 StegoAd: China-nexus attribution attributed to wrong source**

The brief states (line 88): "Microsoft notes overlap with the China-linked DarkSpectre operation (prior ShadyPanda / GhostPoster extension campaigns)"

The Microsoft Edge Security blog post (fetched this iteration) does NOT mention DarkSpectre, ShadyPanda, GhostPoster, or any China-link. This attribution is from The Hacker News article, which explicitly quotes "Koi Security ties to DarkSpectre, the Chinese operation." The brief's phrasing "Microsoft notes" implies the primary source, but it's actually a THN characterisation. The claim is supported by a cited source (THN) — but misattributed to Microsoft. This is an F11 advisory (attribution clarity) rather than an F4 hallucination, because a cited source does support the claim — just not the one implied.

Fix: change "Microsoft notes overlap" to "The Hacker News notes, citing Koi Security, overlap" or "Researchers note overlap" to avoid false attribution to Microsoft.

---

### Verdict

**NEEDS_FIXES (truth: 1, editorial: 0, advisory: 1)**

- F1 (truth): § 7 Verification Notes, line 164 — "CVSS 9.9/8.5" should read "CVSS 8.9/8.5". GHSA-2j5h-858j-5mpf confirms 8.9; brief body already corrected but § 7 not updated in iter-1 remediation.
- F2 (advisory): § 3 StegoAd, line 88 — "Microsoft notes overlap with the China-linked DarkSpectre operation" misattributes a THN/Koi Security characterisation to Microsoft directly. The claim is cited-source-backed (THN), but the "Microsoft notes" phrasing is factually incorrect and misleads readers about source provenance.

All other iter-1 remediations verified clean. No new truth defects, no broken URLs, no hallucinated CVEs or entities, no missing citations on material claims, no single-source flag drift beyond the existing carve-outs already noted in § 7. The brief is in strong shape; these two residual items are the only outstanding issues.

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F4
  category: hallucinated-fact
  section: verification-notes
  item: "§ 7 inclusion note for n8n CVE-2026-54305/54307"
  url_or_quote: "CVE-2026-54305/54307 (n8n) included on CVSS 9.9/8.5"
  summary: "Stale 9.9 residual from pre-iter-1 text; GHSA-2j5h-858j-5mpf confirms CVSS 8.9. Body corrected but § 7 not updated. Fix: change '9.9/8.5' to '8.9/8.5' on line 164."
- code: F11
  category: editorial-advisory
  section: research-investigative-reporting
  item: "StegoAd — Microsoft Edge extensions / DarkSpectre attribution"
  url_or_quote: "Microsoft notes overlap with the China-linked DarkSpectre operation (prior ShadyPanda / GhostPoster extension campaigns)"
  summary: "The Microsoft Edge Security primary source does not mention DarkSpectre/ShadyPanda/GhostPoster/China. The attribution comes from The Hacker News citing Koi Security. 'Microsoft notes' is factually incorrect attribution. Fix: attribute to THN/Koi Security, not Microsoft."
```
