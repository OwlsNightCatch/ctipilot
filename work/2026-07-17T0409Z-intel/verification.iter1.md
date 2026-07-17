**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-17T04:50:10Z · ended_at=2026-07-17T04:59:46Z · duration_seconds=576
**Self-telemetry:** urls_checked=16 · webfetch_calls=11 · bridge_fetches=8 · websearch_calls=0

## Verification report — 2026-07-17T0409Z-intel (iteration 1)

Cold read. 8 new entries + run record. Every inline source URL fetched (CISA/NCSC.ch via bridge; MSRC/NCSC-NL/Register/NCA/CPS/Kaspersky/Microsoft escalated to jina reader where WebFetch returned a JS shell). Every evidence[] quote checked for verbatim-contiguous substring against the fetched source. Frontmatter cves/CVSS cross-checked against per-CVE authorities (MSRC for CVE-2026-58644; Mozilla MFSA for the two Firefox CVEs). All techniques[] ids resolved against the pinned attack/enterprise-attack.json. Update targets confirmed on disk and in prior_coverage.json.

### Citation does not support the claim
- **F3 — TfL sentencing entry.** Body: "TfL later established that data on roughly 7 million users had been accessible — far beyond the ~5,000 initially believed ([NCA, 2026-07-16](…nationalcrimeagency…); [CPS, 2026-07-16](…cps.gov.uk…))." Fetched both cited pages: the NCA page contains no occurrence of "million" at all (only "148 systems … manual workarounds", which is correctly used as evidence[] elsewhere); the CPS page carries only "£29 million … rendered more than 140 systems inoperable". Neither the 7 million nor the ~5,000 figure is on either cited page. Both figures ARE on The Register (already listed on the entry as a corroborating source): line 62 "originally thought to be only around 5,000 people"; line 64 "Scattered Spider actually gained access to around 7 million users' data". The claim is TRUE but MIS-CITED — a reader verifying at the cited authority will not find it. Remediation: attach the 7M/5,000 clause to the Register source (move/add the citation). Truth-class.

### Unsupported / hallucinated facts
- **F4 (minor, adjacent-paragraph splice) — TfL sentencing entry.** The Register evidence[] quote joins two sentences that are separate consecutive paragraphs in the source (Register line 58 "Flowers and Jubair purchased partial TfL credentials … a process that took multiple attempts." and line 60 "Woolwich Crown Court heard that the pair impersonated an employee … resetting the password for their account.") with ". ", collapsing the paragraph break. Both sentences are verbatim and in source order, so meaning is fully preserved — but the string is not a contiguous copyable substring, which the evidence-quote rule treats as a splice (F4). Remediation: split into two evidence[] records, or represent the paragraph boundary. Lowest-severity truth finding.

### Items checked and CLEARED (no finding)
- **Abacus (vuln, high).** NCSC-CH post 12766 (bridge) + both Abacus PSIRT advisories fetched. All four evidence quotes verbatim; fixed builds (V2026 2026.201.17211 / V2025 2025.203.17044 / V2024 2024.204.16772) match the advisory; SilentHotfix→AbaClient≥4.2 dependency matches; "APIs exposed to extern … the case by default" matches NCSC-CH + PSIRT; no-CVE/no-IOC/no-ITW statements accurate. Strong Swiss home-region nexus; high (not critical, no exploitation) correct. Classification A/2 sound. Actions concrete and finding-specific.
- **SharePoint CVE-2026-58644 (vuln, high, update).** CISA alert (bridge) confirms both evidence quotes verbatim and the KEV-add 2026-07-16. MSRC (jina) confirms CVSS 9.8 base, vector AV:N/AC:L/PR:N/UI:N, AND "Exploitation Detected / Exploited: Yes" (rev 1.2, 2026-07-15). The frontmatter `auth: post-auth` is defensibly sourced: MSRC FAQ says "an attacker authenticated as at least a Site Owner" (the entry's sourcing_note names exactly this). Update target 2026-07-15 exists and prior_coverage shows CVE-2026-58644 in it; genuine exploitation-status delta; body carries only the delta. AMSI/MDAV signatures in body match CISA verbatim. Classification A/1 sound (confirmed by two authorities).
- **Firefox 152.0.6 (vuln, notable).** Mozilla MFSA2026-67 confirms both CVEs (CVE-2026-15718 Critical / JavaScript:WebAssembly / invalid pointer; CVE-2026-15719 Critical / DOM:Navigation / site isolation) and the exact "exploit code … public … not aware of any attacks in the wild" quote. NCSC-NL advisory is a client-side SPA that returned only a redirect shell to WebFetch, jina, and bridge — the Dutch corroborating quote could not be independently verified, but the substance is fully confirmed by Mozilla and NCSC-NL is a carve-out national CERT, so NOT flagged. notable (public PoC, no ITW) correct; entry explicitly rejects the aggregator "zero-day exploited" over-claim.
- **Talos UAT-11795 (threat, notable).** Blog fetched; both evidence quotes verbatim; every body claim (ClickFix→mshta, trojanized installers, in-memory Starland RAT, PythonLauncher-{3 chars} task, 40+ wallets, CastleStealer/Remcos, AMSI/ETW patch, Polygon dead-drop, WLDR, Germany/Romania) confirmed. Single-source correctly flagged; classification B/2 correct. techniques[] all resolve and map to described behavior (T1685=Disable or Modify Tools ↔ AMSI/ETW patch; T1102.001=Dead Drop Resolver ↔ Polygon; T1204.004=Malicious Copy and Paste ↔ ClickFix). No IOCs in body (Polygon contract address appears only inside the verbatim source quote, not an enumerated IOC class).
- **Kaspersky HelloNet (research, notable).** Securelist fetched (jina); all three evidence quotes verbatim-contiguous (socket-ops quote confirmed by grep). Body claims confirmed. Attribution correctly carried as Kaspersky's own low-confidence, no nexus asserted. Single-source flagged; B/2. techniques resolve.
- **Microsoft ACR Stealer (research, notable).** MS blog fetched (jina); all three evidence quotes verbatim-contiguous (EtherHiding and DPAPI quotes grep-confirmed). Amatera-rebrand link carried as Microsoft's hedged "reportedly … associated with". Single-source flagged; B/2. entities tool:acr-stealer / tool:amatera correct; no collision with the distinct campaign:acr-stealer-fake-claude.
- **Garante / Wind Tre (incident, notable).** Both Garante pages + ANSA fetched; both Italian evidence quotes verbatim; EUR 1,715,600 / 365,048 / 41,359 / ~2M enumeration / secondary-API / OWASP-rejection all confirmed. EU-telco nexus + transferable TTP clears the stricter breach bar; framed around the lesson, not the victim. A/1 sound.
- **TfL entry — everything except F3/F4.** NCA "148 systems … manual workarounds" evidence quote verbatim; sentencing 5y6m each, Woolwich Crown Court, Scattered Spider members, 2024 TfL, credential-purchase→helpdesk-vishing→MFA-reset chain all confirmed across NCA/CPS/Register. Update target 2026-06-23 exists; genuine court-record delta. A/1 sound.

### Whole-run checks
- **Coverage completeness (F10): none found — coverage looks complete.** The three drops (FortiSandbox KEV-only delta; Siemens SICAM 8 already covered 2026-07-10; Unit 42 AI-lens strategic revisit) are correctly justified and documented in the run record. Out-of-window items (Hoymiles 2026-07-15, Cursor IDE 2026-07-14, BSI Windows Hello, Zoom CVE-2026-53412 single trade-press) are reasonably excluded and logged. cisa-directives miss is disclosed. I cannot name an in-window, in-nexus story with a plausible source that the run missed.
- **Soundness:** every entry clears the relevance/actionability gate; the three vulnerability entries each demand out-of-band action (Swiss flagship pre-auth RCE / confirmed-exploited KEV / public-exploit-code browser chain). No marginal padding.
- **Priority calibration (F16): clean.** No entry is over- or under-alerting; no `critical` this run (correct — none clears the stop-and-act-now bar); the two `high` (Abacus, SharePoint) are TL;DR-worthy.
- **org_triage / watchlist:** all null / false as required for this deployment (no scheme, no watchlists). No F16.
- **Classification (F17): clean.** Every entry carries exactly one Admiralty rating, all within vocabulary, letters consistent with source nature (A only on national-CERT/vendor-PSIRT/regulator/law-enforcement primaries; B on single research-lab reports), credibility numbers consistent with corroboration (2 on the single-source lab reports; 1 only where two authorities confirm).
- **Action-item discipline (F18): clean.** The three vuln entries carry ≤2 concrete, finding-specific actions; the five awareness/research/incident entries correctly carry actions: [].
- **Style/IOC/English:** no hashes/IPs/attacker-domains/rule-code in any entry body; no workflow-internal language; English throughout with Italian source quotes glossed.

### Verdict
NEEDS_FIXES (truth: 2, editorial: 0, advisory: 0)

Both findings are on a single entry (scattered-spider-tfl-sentencing-helpdesk-vishing). F3 (mis-cited 7M/5,000 figure) is the material one — a reader verifying at the cited NCA/CPS pages will not find the figure, which is actually on the Register source already listed on the entry. F4 is a minor adjacent-paragraph evidence splice. All seven other entries and the run record are clean.

### Findings summary (machine-readable)
```yaml
- code: F3
  category: claim-not-supported
  section: active-incidents
  item: "Scattered Spider TfL sentencing (scattered-spider-tfl-sentencing-helpdesk-vishing)"
  url_or_quote: "7 million users / ~5,000 initially believed — inline-cited to NCA + CPS"
  summary: "Neither cited page (NCA/CPS) contains the 7M or 5,000 figure; both are on The Register (already a source on the entry). Re-attribute the clause to the Register."
- code: F4
  category: hallucinated-fact
  section: active-incidents
  item: "Scattered Spider TfL sentencing (scattered-spider-tfl-sentencing-helpdesk-vishing)"
  url_or_quote: "Register evidence[] quote joining lines 58 and 60 (two separate paragraphs) with '. '"
  summary: "Adjacent-paragraph splice — verbatim and in order but not a contiguous copyable substring; split into two evidence records or mark the paragraph boundary. Minor."
```
