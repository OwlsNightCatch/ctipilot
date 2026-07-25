**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-25T05:26:43Z · ended_at=2026-07-25T05:34:07Z · duration_seconds=444

## Verification report — 2026-07-25T0409Z-intel (iteration 3)

Cold read of all 7 new entries + run record. Verified every iter-2 remediation and re-read the run cold.
Every inline source URL fetched (WebFetch / bridge / jina last-resort); every evidence[] quote checked
verbatim; every CVE / CVSS / version / date / actor traced to a source fetched this iteration.

### Iter-2 fix verification (all confirmed good, no regressions)
- **F3 (MS report)** — the OAuth-chain phrase is now an unquoted paraphrase. The Microsoft blog explicitly
  states "Because the link routed through Microsoft authentication infrastructure, both recipients and URL
  scanners saw a login.microsoftonline[.]com link" — the paraphrase "obscured the true destination from
  scanners and recipients" is source-supported. No fabricated quote remains. Both evidence[] quotes are
  verbatim in the source.
- **F4 (ZimReaper)** — evidence quote "Proofpoint has not observed TA458 using CVE-2025-66376, despite the
  group's regular access to webmail XSS zero-days." confirmed a single contiguous verbatim substring of the
  Proofpoint TA488/Zimbra page. The svg-onload sanitizer-bypass quote is also verbatim. No spliced quotes.
- **F9 (RoundPress)** — attribution divergence now surfaced in sourcing_note and body and is accurate:
  ESET's 2025 Operation RoundPress report attributes to Sednit/APT28 (medium confidence, confirmed against
  welivesecurity), while Proofpoint tracks TA458 and reports no telemetry overlap with TA422/APT28
  (confirmed against Proofpoint). Framed as overlapping tracking, not a single confirmed actor.
- **F17 ×2 (RoundPress, ZimReaper)** — both now classification.credibility: 2 (reliability B retained).
  Correct for single-vendor Proofpoint sourcing.
- **F18 (RoundPress)** — the two actions are concrete do-now tasks (patch SOGo 5.12.8; inventory/prioritize
  internet-reachable webmail). No restatement of the body WAF/sanitizer hardening remains.
- **Iter-1 fixes** — Certighost binary/function names (certpdef.dll, _LoadPrincipalObject, certsrv.exe)
  absent from entry and confirmed absent from the CybersecurityNews source. Autismuslink Lynx/FortiGate
  specifics and the FortiGate recommendation are gone. No regressions.

### Cold-read source verification (all 7 entries)
- **Certighost (CVE-2026-54121)** — MSRC (bridge) confirms AD CS EoP, CVSS 8.8 (AV:N/AC:L/PR:L/UI:N),
  released 2026-07-14, publiclyDisclosed=No, exploited=No, "Exploitation Less Likely"; evidence quote
  verbatim. CybersecurityNews (jina, last-resort — bridge/WebFetch returned only JS-hydrated metadata)
  confirms the chase fallback, cdc/rmd attributes, host-trust flaw, ms-DS-MachineAccountQuota (default 10),
  DCSync of krbtgt, and SERVER_TRUST_ACCOUNT flag (8192) + SID-comparison patch gate. All body claims
  supported. priority high correctly below critical (no ITW exploitation).
- **Check Point (CVE-2026-62144/62145)** — both evidence quotes verbatim in sk185152/sk185153; CVE ids,
  affected versions, Jumbo Hotfix takes all match. NCSC-NL confirms CVSS v4 10.0 / 9.4 and that only
  CVE-2026-16232 is exploited (limited number of internet-exposed customers). update_of target genuine;
  delta (two sibling CVEs on the same surface) is real.
- **TA458/RoundPress (CVE-2026-8496)** — Proofpoint primary confirms every CVE (Zimbra CVE-2025-27915,
  mDaemon CVE-2025-3929, Roundcube CVE-2023-43770/CVE-2024-42009/CVE-2025-49113, SOGo CVE-2026-8496 patched
  in 5.12.8, Kerio no-CVE), GRU attribution, half-click phrase verbatim, five-platform set, targeting, and
  no-TA422-overlap. SOGo 5.12.8 release tag resolves. Deep-dive earns its length.
- **ZimReaper (LAUNDRY BEAR)** — Proofpoint primary confirms all mechanics/persistence claims and quotes;
  CISA aa26-204a corroborates the Zimbra/CVE-2025-66376/LAUNDRY BEAR/Void Blizzard joint advisory. update_of
  delta (app-specific-password persistence surviving reset + patch) is load-bearing and genuine.
- **Microsoft email report** — both evidence quotes verbatim; vishing ~10× / 14:00-20:00 UTC, 94-96%,
  4-6% malware, PDF→DOC/DOCX drift, QR near-zero, Tycoon2FA, SES/Python BEC, EML/OAuth/Entra BAT chain all
  supported. single-source flag correct.
- **Stiftung Autismuslink** — victim PDF (read directly) confirms both German quotes verbatim; "Am
  Montagmorgen, 29.06.2026" confirms detected Monday 2026-06-29 (2026-06-29 is genuinely a Monday — an
  interim WebFetch summariser's "Friday" was a hallucination, refuted against the primary). Data classes,
  Infoguard, federal/NCSC notification, criminal complaint, backups-unaffected all match. ransomware.live
  confirms incransom listing for autismuslink.ch dated 2026-07-24. Home-region + sector nexus clears the
  breach bar; framed around target-class lesson, not victim name.
- **Thailand MoF / Hermes** — Hunt.io primary confirms YOLO-mode quote verbatim, 585 files/~470 MB, Hermes,
  LinPEAS, Hades Go implant (persistence/HTTPS/AES-256-GCM), Hive SASL-PLAIN UDF, Ambari REST, GlassFish
  default-cred WAR webshell, Bob Diachenko, ThaiCERT/NCSA 2026-07-15, low-to-medium Chinese-speaker
  attribution. BleepingComputer confirms the "not confirmed breached" quote verbatim. Out-of-region breach
  clears F7 via transferable AI-unattended-post-exploitation TTP, explicitly framed as such. "Second
  AI-agent-driven autonomous-attack ... in roughly a week" is defensible (Hugging Face autonomous-agent
  breach, 2026-07-21/23, is the first).

### Whole-run checks
- Classification: every entry carries a valid Admiralty block; org_triage null throughout (no scheme
  configured — correct); no watchlist tags/hits. No F16/F17.
- Actions: 5 entries with concrete do-now actions, 2 correctly empty (report/incident). No duplication
  across in-window entries. No F18.
- Single-source flags (MS report, Thailand) present with sourcing_note. No F12.
- Style: no IOCs, no vanity metrics, English throughout, no workflow-internal tokens. Priorities calibrated
  (no critical; highs are TL;DR-worthy; notables correctly below the critical bar).
- Coverage: updates vs new decisions correct; deep-dive justified; borderline-drops and out-of-window drops
  documented with reasoning; jina-402 / cisa-listing-403 outages mitigated per the run record. No named
  in-window Swiss/EU story identifiable as a silent omission — coverage looks complete.

### Verdict
CLEAN — all iter-2 remediations verified correct with no regressions; every entry's sources fetched this
iteration support its claims; no truth or editorial defects found. This is a first CLEAN on the cold (Opus)
cycle; a confirmation pass on the other model is the double-CLEAN publish gate.

### Findings summary (machine-readable)
```yaml
[]
```
