**Model:** Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-25T04:57:47Z · ended_at=2026-07-25T05:06:32Z · duration_seconds=525
**Self-telemetry:** urls_checked=13 · webfetch_calls=8 · bridge_fetches=4 · websearch_calls=0

## Verification report — 2026-07-25T0409Z-intel (iteration 1)

Read cold. All 7 entries + run record reviewed end-to-end; every inline source URL fetched
(MSRC + CISA via bridge; CybersecurityNews escalated bridge→jina after WebFetch returned a JS
shell; victim PDF text-extracted from the saved binary). Every named CVE / actor / version /
date / evidence quote cross-checked against a source fetched this iteration.

### Unsupported / hallucinated facts

**F4 — Certighost entry: `certpdef.dll` / `_LoadPrincipalObject` / `certsrv.exe` not in cited sources.**
Body claim: "the vulnerable logic sits in the Enterprise CA's enrollment \"chase\" fallback
(`certpdef.dll`, the `_LoadPrincipalObject` path in `certsrv.exe`)" — attributed to CybersecurityNews.
MSRC (bridge) carries only the AD CS EoP description / CWE-285 / CVSS 8.8 — no binary names. The
CybersecurityNews article (read in full via jina) confirms the chase/cdc/rmd mechanics, the DCSync
of krbtgt, the SERVER_TRUST_ACCOUNT (8192) + SID-comparison fix, and names the patch function as
`_ValidateChaseTargetIsDC` (behind Feature_3185813818) — but never mentions certpdef.dll,
_LoadPrincipalObject, or certsrv.exe. These names are not in either cited source (likely from the
dropped H0j3n gist). Remediation: drop the parenthetical, or source it to the researcher gist.
Everything else in this entry verified clean: CVE/CVSS/dates/exploitation-status (MSRC), cdc/rmd,
rogue SMB/LDAP/LSA, ms-DS-MachineAccountQuota, PKINIT, DCSync/krbtgt, the 8192+SID patch, and both
researchers (H0j3n gist + aniqfakhrul PoC repo) all confirmed.

### Claims missing inline citation

**F5 — Stiftung Autismuslink: uncited INC Ransom<->Lynx / FortiGate attribution (low severity).**
"its assessed operational overlap with the Lynx rebrand and FortiGate credential-theft
infrastructure mean any organisation with unpatched or credential-exposed FortiGate edge should
treat this cluster as a live access vector" — an assessed attribution driving a concrete
recommendation, with no inline citation; neither cited source (victim PDF, ransomware.live) makes
the claim. NOT hallucinated: it is registry-documented (actor:inc-ransom summary + incident:
fortibleed-fortigate-credential-exposure, sourced to SOCRadar 2026-07-01 / weekly-w27) and correct.
Optional strengthening: add the SOCRadar/weekly citation inline, or soften to a prior-coverage
reference. Reader-verifiability gap, not a truth defect.

### Verified clean (no findings)

- **Check Point siblings** — sk185152 evidence quote verbatim ("An unauthenticated attacker can run
  any command on the Management including run-script and exec-command on Security Gateway"); sk185153
  evidence quote verbatim ("A vulnerability in Gaia Portal allows an authenticated attacker with
  read-only access to run commands as root"); NCSC-NL CVSS v4 10.0/9.4 confirmed; CERT-FR confirms all
  three CVEs + CVE-2026-16232 active exploitation; version ranges and Jumbo Hotfix takes match;
  update_of target exists; Admiralty A/2 justified (vendor PSIRT primary).
- **TA458 / RoundPress** — Proofpoint confirms CVE-2026-8496 (SOGo, patched 5.12.8), SpyPress, GRU
  assessment, half-click, all five platforms + n-day CVEs, target countries, TA422 distinction,
  Roundcube CVE-2025-49113 persistence chain; SOGo 5.12.8 GitHub release confirms a security release
  fixing XSS-in-mail (the WebFetch "May 12 2026" is a misread of the version string; CVE mapping is
  Proofpoint's). Registry entities (ta458-roundpress, spypress) correctly created. Deep-dive
  justification sound.
- **LAUNDRY BEAR / ZimReaper** — Proofpoint confirms CSS-@import sanitizer bypass reconstructing
  <svg onload=eval(atob())>, DNS-tunnel exfil, the "ZimbraWeb" CreateAppSpecificPasswordRequest
  persistence surviving reset+patch, TA458 not observed using CVE-2025-66376, "upstream Russian
  intelligence taskmasters", no TA488 activity since Feb 2026. CISA AA26-204A corroborates campaign +
  "Newly-created Application Passcode [T1098]". ZimReaper correctly registered as alias of
  tool:ulej-flowerbed. Genuine update delta.
- **Microsoft email Q2 2026** — every statistic verbatim-confirmed against source (10x vishing
  baseline, 94-96% credential phishing, 4-6% malware, PDF->DOC/DOCX drift, QR near-zero, Tycoon2FA,
  Amazon SES Python-MIME BEC to role mailboxes, EML/Teams-voicemail multi-tenant-Entra OAuth BAT
  dropper, 14:00-20:00 UTC vishing window). Single-source correctly flagged; volume totals correctly
  omitted; actions:[] correct for a landscape report.
- **Stiftung Autismuslink** (aside from F5) — both German evidence quotes verbatim in the victim PDF;
  29.06.2026 detection, Infoguard forensics, criminal complaint, backups-unaffected, and the affected
  data classes (IV/BKD service agreements, teacher contracts, doctors' certificates, 2016-2023 client
  dossier archive) all present. ransomware.live confirms the INC Ransom claim (2026-07-24). Strong
  Swiss home-region nexus. (Minor: entry says "NCSC was notified"; PDF says "official federal offices"
  — defensible gloss, not flagged.)
- **Thailand MoF / Hermes** — Hunt.io confirms 585 files/~470MB, Hermes YOLO mode, LinPEAS,
  HiveServer2 SASL-PLAIN Java-UDF, Ambari REST, GlassFish default-cred WAR webshell, Hades Go implant
  (Registry Run/scheduled-task/cron, HTTPS, AES-256-GCM), Bob Diachenko, Chinese-speaking low-to-med
  attribution, ThaiCERT/NCSA notified 2026-07-15. BleepingComputer evidence quote verbatim. Single-
  source correctly flagged; compromise-unconfirmed framing honest; transferable-TTP breach
  justification clears the stricter out-of-nexus bar. No IOCs leaked into the entry.

### Whole-run checks
- **Relevance/soundness:** all 7 clear the gate. Both out-of-region incidents (Thailand) and the
  landscape report earn their place on transferable-TTP / M365-nexus grounds; the Swiss breach has a
  direct home-region nexus. No F7 drops.
- **Priority calibration:** 3 high / 4 notable, 0 critical — correct; no entry clears the critical
  bar (all patched or not actively exploited), none is under-alerted.
- **Update-vs-new:** both update_of decisions correct with genuine deltas; new CVEs (54121, 62144,
  8496) absent from prior_coverage; exploited siblings (16232, 66376) correctly framed as updates.
  Thailand/RoundPress correctly keep already-in-store LinPEAS/Roundcube CVEs out of cves[] (verified
  in state/cves_seen.json).
- **Classification (F17):** all Admiralty codes calibrated to sourcing (single-source items credibility
  2, corroborated campaigns credibility 1, victim first-party A). No drift.
- **Org-triage/watchlist (F16):** no scheme/watchlist configured; all entries carry org_triage:null,
  watchlist_hit:false. Clean.
- **Action items (F18):** disciplined — concrete do-now tasks where present, correct empty lists on
  the landscape/incident/awareness entries. No padding.
- **Style:** no IOCs, no vanity metrics, English, no workflow-internal language. Clean.
- **Coverage/missed angles (F10):** none identified. Borderline drops (Flare, GTIG) and out-of-window
  items are well-justified in the run record; jina-402 and cisa-listing-403 gaps were mitigated
  (cisa-kev/detail pages, cert-pl recovered) with no nameable in-window story lost. Coverage looks
  complete.

### Verdict
NEEDS_FIXES (truth: 1, editorial: 1, advisory: 0)

F4 is a genuine truth defect (unsupported implementation names). F5 is a low-severity, optional
sourcing strengthening — the underlying claim is registry-backed and correct. The run is otherwise
exceptionally clean: every evidence quote that could be checked is verbatim, every CVE/actor/version/
date traces to a fetched source, and the editorial calibration (priority, classification, updates,
actions, relevance) is sound.

### Findings summary (machine-readable)
```yaml
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "CVE-2026-54121 — AD CS 'Certighost'"
  url_or_quote: "(`certpdef.dll`, the `_LoadPrincipalObject` path in `certsrv.exe`)"
  summary: "Binary/function names not in either cited source (MSRC or CybersecurityNews); CSN names the patch fn as _ValidateChaseTargetIsDC only. Drop the parenthetical or source to the H0j3n gist."
- code: F5
  category: missing-citation
  section: active-threats
  item: "Stiftung Autismuslink / INC Ransom"
  url_or_quote: "its assessed operational overlap with the Lynx rebrand and FortiGate credential-theft infrastructure"
  summary: "Uncited assessed attribution driving a FortiGate-edge recommendation; registry-backed and correct but not in either cited source. Low severity — add SOCRadar/weekly-w27 citation or soften."
```
