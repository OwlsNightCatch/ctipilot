# Repair worker 2, cleanup wave 03 (2026-10-21T1149Z-audit)

Batch: `work/2026-10-21T1149Z-audit/batch-2.yaml`, 5 entries, 13 verdict blocks, 85 listed defects. Every defect was re-derived on the current text (after the 2026-10-11T1307Z-audit corrections) and every sentence written was checked against a freshly fetched source saved under `repair-2/src/` (`grep -F` on every new quote: 11 of 11 verbatim). Result: 3 records written (1 correction, 2 improvements), 2 entries without a record, 6 defects applied (some partly, where the 2026-10-11 audit had already fixed the rest), 79 declined. No entry in this batch had a legacy duty (`legacy_duty: false` on all five).

Gate: `python3 tools/check_run.py --all` exits 0; the only lines on these entries are the expected `entry-updates` WARNs that run id 2026-10-21T1149Z-audit has no run record yet. Page checks (`repair-2/page-checks.txt`): no `quote-literal` or `citation-cve` line on any of the five entries.

## 2026-05-10/microsoft-semantic-kernel-cve-2026-26030-cve-2026-25592-prom

No record. All 18 defects (block on folded duplicate `2026-05-10/cve-2026-26030-cve-2026-25592-microsoft-semantic-kernel-prom`: 8; block on this entry: 10) are declined as already fixed by 2026-10-11T1307Z-audit. Re-checked against the Microsoft blog (https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/) and both advisories (api.github.com GHSA-xjw9-4gw8-4rqx, GHSA-2ww3-72rp-wpp4):
- Foundry / Copilot Studio / EU-pilot claims, "§ 5" pointers, uncited generalisations, the invented "without explicit validation" quote and AutoGen: gone.
- Only `DownloadFileAsync` is described as mis-exposed, as the host-side write to the Startup folder; `upload_file` is the read path (blog lines on Startup and upload_file match).
- CVE-2026-26030 is described as eval() of a lambda with an AST blocklist bypassed via BuiltinImporter; the fix's allowlists match the blog.
- `auth: post-auth` (both GHSA vectors PR:L), affected/fixed filled (pip 1.39.4; Plugins.Core 1.71.0 and pip 1.39.3), GHSA dates 2026-02-19 / 2026-02-06, priority notable, T1565.001 replaced (T1547.001 present).
- Function Invocation Filter attributed to GHSA-2ww3; the Python workaround (avoid InMemoryVectorStore in production) cited to GHSA-xjw9.
- All verified `facts_only_in_duplicates` rows are already carried.

## 2026-05-12/palo-alto-pan-os-cve-2026-0300-first-wave-fixed-builds-now-s

No record. All 29 defects (one block on this entry; folded duplicates 2026-05-14, 2026-05-18, 2026-05-08, 2026-05-09) are declined as already fixed by 2026-10-11T1307Z-audit. Re-checked against PSIRT (https://security.paloaltonetworks.com/CVE-2026-0300) and Unit 42 (https://unit42.paloaltonetworks.com/captive-portal-zero-day/):
- The action lists only 05/13-wave builds; 12.1.7 carries its ETA 05/28 in the body and the 05-13 section.
- The 05-13 section no longer says "last updated 2026-05-07" (that text survives only in the append-only 2026-05-13 record summary).
- Threat ID 510019 carries "content 9097-10022", "Threat Prevention subscribers" and "PAN-OS 11.1 or later".
- April 9 is described as the first unsuccessful attempts, with RCE a week later; one cluster, "likely state-sponsored", limited exploitation; no China-nexus or "primary actor" claim.
- No "delayed", "now scheduled", "continues", heap-overflow, GlobalProtect, inverted 10.2 guidance, invented signatures or behaviours, 10.1/11.0 versions, dwell time or compliance-gap text.
- Two-condition exposure test and advisory menu path present; status includes patch-available; classification A1, techniques, affected_products, full fixed table, KEV JSON source, Unit 42 source, sectors [] all present.

Facts not carried: the 2026-05-14/05-16/05-28 PSIRT timeline rows (verified) are history with no defender effect today, since every listed build is now released except the still-labelled 12.1.7 ETA the entry already states. The KEV 5/13 "variety of patches" note adds nothing beyond the stated first wave.

## 2026-05-15/cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea

Record: `correction` at 2026-10-21T12:06:51Z, fields `body, evidence, headline, sources, title`.

Applied:
- Block 1 defect 3 (ASLR part; the exploitation-attempts part was already fixed): "RCE requires ASLR to be disabled" rewritten. depthfirst's PoC runs with ASLR off and depthfirst notes forked workers share one heap layout that could in theory leak ASLR (https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability). F5's CVE description, updated 2026-09-10, covers "ASLR disabled or when the attacker can bypass ASLR", cited to ENISA EUVD-2026-30010 (https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-30010; read through the euvdservices API, saved as `src/nginx-euvd-search.json`), since cveawg is a blocked citation. The Contradiction line's ASLR clause was swept the same way. Correction section added; EUVD appended to sources.
- Block 1 defect 4 and block 2 defect 4 (evidence part; classification, techniques and affected/fixed were already fixed): six verbatim evidence quotes added (the GHSA trigger sentence, depthfirst x3 for PoC/ASLR/disclosure date, EUVD for the ASLR wording, THN for the VulnCheck honeypot attempts).
- Em dashes removed from the title, the headline and the body (2). The headline (137 characters and a copy of the title) was rewritten to 117 characters, naming the public PoC and the honeypot attempts.

Declined as already fixed by 2026-10-11T1307Z-audit:
- Block 1 defect 1 (dates and NDA) and defect 2 (8.1 / CWE-122 no longer stated).
- Block 2 defect 1 (three-part trigger stated), defect 2 (detection anchor now escapable URI characters plus worker crashes; Security Affairs supports it), defect 3 (says "exploitation attempts"), defect 5 (K000161019 no longer cited).

`cves[].status` was left as is: the taxonomy has no "attempted" value, and the body states the honeypot attempts precisely.

## 2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen

Record: `improvement` at 2026-10-21T12:07:16Z, fields `body, evidence, techniques`.

Applied:
- Block 1 (folded 2026-05-16 stored) defect 3, remaining part, using the verified lead: the EM service cannot check for new mitigations on a build older than March 2023. Added to the main analysis with an evidence quote and an Improvement section (https://techcommunity.microsoft.com/blog/exchange/addressing-exchange-server-may-2026-vulnerability-cve-2026-42897/4518498). The September 2021 CU and officeclient.microsoft.com parts were already fixed.
- Block 3 defect 8: T1552 replaced with T1555.003 (browser autofill harvesting) and T1528 (GetClientAccessToken OAuth token theft), both active in the ATT&CK 20.0 pin, per Proofpoint (https://www.proofpoint.com/us/blog/threat-insight/cleaning-out-inboxes-ta488-comes-outlook-another-half-click-exploit).

Declined:
- Block 3 defect 7, Proofpoint date: not a defect. The page's visible byline reads "July 29, 2026" and its JSON-LD datePublished is 2026-07-29T15:00Z; only `article:published_time` says 2026-07-28 (US Pacific). The MSRC re-attribution half was already fixed by 2026-10-11T1307Z-audit.
- Block 3 defect 9, part: the 2026-08-30 metadata-only record cannot be made internal, because records are append-only. Its section wording was already made plain by 2026-10-11T1307Z-audit.
- Every other defect (blocks 1 to 3, 23 more) is already fixed by 2026-10-11T1307Z-audit:
  - "no permanent patch" in every field; stored XSS; Get-ExchangeDiagnosticInfo / Set-Server / Get-Server; the 2026-05-09 lookback; IIS / EID 4 / w3wp detections.
  - The tier count; the Patch Tuesday framing; unverifiable "permanent fix" quotes; "§ 5"; the M2 request-rewrite and no-restart claims; the THN-attributed-to-Microsoft line and missing TA488 attribution.
  - T1566.001 / cookie-theft chain; quantifiers and Hafnium; CU numbers now cited to the July blog; PD-13 / "Background." evidence.
  - The officemitigations host; affected/fixed now June SU; the no-patch tag; priority now high.

## 2026-09-12/japan-digital-agency-gss-vpn-breach-maintenance-account

Record: `improvement` at 2026-10-21T12:08:54Z, fields `body, evidence, headline, sources, sourcing_note, summary`.

Applied, for the one defect (nippon.com Jiji URL 404, confirmed this run):
- The Wayback copy is unreachable from the container and from WebFetch. The Digital Agency's own notice (https://www.digital.go.jp/news/2026-0911-01, 2026-09-11) was appended as a primary source instead, and the two body clauses cited to Jiji were rebound to it: the ~246,000 records, the 25 June detection and the 9 July VPN-intrusion finding. Two Japanese evidence quotes were added, each with an `original:` and its English translation.
- The two Jiji evidence quotes were removed. Their cited page is gone (the page check flagged both), the body no longer cites Jiji, and the Kihara quote backed no sentence. The nippon.com record stays as sources[0].
- The GSS description was rebound to Rocket Boys' wording (shared base of work PCs, networks, office software, communication tools and security measures). "Authentication environment" is on no readable page.
- From the notice, the section adds the 189,000 / 57,000 split and the commitment to improve how connections from outside are made; the main analysis's measures sentence was swept (Rocket Boys carries both measures and the no-specifics note). The sourcing note no longer says "all three cited outlets".
- Em dashes removed from the headline (also brought from 133 to 116 characters), the summary, the sourcing note, the body (5) and the 2026-09-13 section (1).

## State changes the main agent must apply

- `entities/registry.yaml`: none.
- `state/cves_seen.json`: none required, since no `cves[]` record changed. Optional: bump `last_seen` to 2026-10-21 for CVE-2026-42945 and CVE-2026-42897, whose entries gained records.
- Links and folds: none needed. The SAP entry `2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce` already references the nginx entry, and `2026-05-17/exchange-cve-2026-42897-pwn2own-devcore-three-bug-system-rce` already references the Exchange entry.

## Residuals noticed outside the findings (nothing fixed)

- PAN-OS 2026-05-12: no `**Defender takeaway:**` line; the PSIRT source record has no date.
- nginx 2026-05-15: no `**Defender takeaway:**` line; Security Affairs is dated "2026-05" (page metadata 2026-05-14); the `state/cves_seen.json` title for CVE-2026-42945 still reads "§ 7 drop (primary 2026-05-18 out-of-window)".
- Exchange 2026-05-18: the headline is 157 characters; the Detection label in the 2026-07-31 section is `**Detection.**`, not `**Detection:**`; the main analysis carries only `**Exposure:**`, with Detection, Triage and Defender takeaway inside the 2026-07-31 section.
- Japan 2026-09-12: the 2026-09-13 Correction section says whether the flaw "was known and patched before the intrusion" remains undisclosed, which contradicts the main analysis (the minister said on 2026-09-11 that it was known); the sourcing note says the CVE guess "is not carried in this entry's frontmatter" (pipeline self-reference); the Piyolog publisher strings carry em dashes; there are no `**Exposure:**` or `**Detection:**` lines.
- Unreadable this run: web.archive.org, through both the container and WebFetch.
