**Model:** Anthropic Claude (specific model not determined) (`unknown`)
**Timestamps:** started_at=2026-06-27T05:01:07Z · ended_at=2026-06-27T05:05:10Z · duration_seconds=243

## Verification report — briefs/2026-06-27.md (iteration 3)

Cold two-axis read (URL truth + editorial quality). Every primary Source URL and the load-bearing Additional sources were WebFetched this iteration (IC3 PSA via tools/fetch_source.py bridge). The three prior-iteration fix spots were re-verified against their sources and confirmed correct with no regression (details under "Re-verified, no regression" below).

### Citation does not support the claim

**F3 — § 3 Citizen Lab / Cellebrite: forensic report attributed to the wrong Russian agency.**
Brief (§ 3, para 1): "an official **Russian Investigative Committee** forensic report explicitly names the UFED tooling and lists extracted WhatsApp/Telegram/Viber data."
Citizen Lab (fetched this iteration) states the forensic expert report (ЗАКЛЮЧЕНИЕ ЭКСПЕРТА Nº 1269-17) was authored by **Russia's Forensic Expert Center of the Ministry of the Interior (MVD)**, and was *commissioned by* the Investigative Committee. The document is an MVD report, not an Investigative-Committee report. The brief attributes authorship to the commissioning body. Operationally minor (the report is genuine Russian-state forensic documentation that does name UFED and list WhatsApp/Telegram/Viber data, and the UFED-host evidence stream is unaffected), but a hostile reader checking the source catches the agency error.
Fix: attribute the report to the MVD Forensic Expert Center (commissioned by the Investigative Committee), or generalise to "an official Russian state forensic report."

### Editorial / less-is-more flags (advisory)

**F11a — Socket source date inconsistency.** TL;DR bullet 4 cites "[Socket, 2026-06-26]"; the § 4 Miasma body and footer correctly cite "Socket Security, 2026-06-25". The Socket page is dated 2026-06-25 (verified). Align the TL;DR date to 2026-06-25. Non-blocking.

**F11b — Klue victim list, Autodesk.** § 4 Klue UPDATE lists "Blackbaud, Autodesk, Deel, Camunda and Tines" among victims. SecurityWeek (verified) flags Autodesk as potentially unaffected (uses a non-Salesforce integration). Either drop Autodesk or carry the hedge. Non-blocking.

**F11c — ENISA EUVD additional source renders blank.** The EUVD URL (EUVD-2026-37831) is a client-rendered SPA that returns "The European Vulnerability Database application could not be loaded" to non-browser fetchers; a reader clicking it sees a blank app. It is a specific per-entry deep link (not an index, so check_brief.py-clean) and only an Additional source — the primary (The Hacker News) fully supports the Windchill deserialization-RCE claim. Advisory only; no action strictly required.

### Re-verified, no regression (the iteration-2 fix spots)

- **§ 3 Amazon Q (CVE-2026-12957):** Wiz confirms fix in Language Server for AWS **1.65.0** (consent prompt added). Brief's "< 1.65.0; fixed in 1.65.0" and the ≥1.65.0 action are correct. CVSS 8.5, dates (discovered 2026-04-17, patched 2026-05-12, public 2026-06-26) all match.
- **§ 3 SANS ISC prctl:** isc.sans.edu/diary/33102 supports exactly what the brief claims — comm-vs-cmdline divergence, kworker masquerade, eBPF/Kunai, Operation Highland/Velvet Ant (Sygnia), T1036. The diary does **not** mention auditd and neither does the brief. Clean.
- **§ 4 The Gentlemen:** in-window hook correctly = inside-it.ch 2026-06-26 (Switzerland second-most-targeted). The 478-victims / `--spread` / GentleKiller profile is correctly attributed to The Hacker News 2026-06-11 (THN confirms all three; does NOT mention Switzerland). Swiss-targeting claim is logged single-source in § 7. Clean.
- **§ 4 Miasma:** Socket explicitly mentions `RevokeAndItGoesKaboom` and links it to `codfish/semantic-release-action` with StepSecurity documentation. The connection is supported by the Socket primary and correctly attributed. Clean.
- **§ 1 Canvas:** Computer Weekly confirms "paid an undisclosed sum to destroy the stolen data"; Instructure's incident page confirms the "agreement / deletion (shred) logs" framing without confirming a monetary payment. Brief's "reportedly paid" hedge + § 7 contradiction note are accurate. Clean.
- **§ 1 Signal:** FBI IC3 PSA (I-062626-PSA, 2026-06-26, fetched via bridge) precisely supports the re-registration-persistence claim ("that same key remains valid even if they create a new account ... using the same phone number"), UNC5792/UNC4221, backup-recovery-key elicitation, target population. CyberScoop gone; footer is IC3 (primary) + THN. Clean.
- **§ 5 STOCKSTAY:** GTIG primary dated 2026-06-25; STOCKTRADER confirmed at **13 commands**; all four components, WM_COPYDATA, 4096-bit RSA, K1MORPHER/Squirrel3, websocket-sharp, Render/Glitch C2, MicrosoftUpdateOneDrive persistence, 09:00–18:00 working hours, CVE-2025-8088, WILDDAY/DIAMONDBACK, Italian-foreign-policy targeting, Tornado controller in public GitHub repo all confirmed. § 7 contradiction note (GTIG 06-25 vs corroboration 06-26) consistent. Clean.

### Other items verified clean
- § 0/§2 DirtyClone (JFrog): CVE-2026-43503, __pskb_copy_fclone(), SKBFL_SHARED_FRAG, XFRM/IPsec, CVSS 8.8, commit 48f6a5356a33 / v7.1-rc5 / merged 2026-05-21, related DirtyFrag CVEs, "no kernel logs or audit traces" — all confirmed verbatim.
- § 2 pedit COW: Red Hat RHSB-2026-008 + THN confirm CVE-2026-46331, tcf_pedit_act()/act_pedit, out-of-bounds/partial-COW page-cache write, PoC packet_edit_meme, CVE assigned 2026-06-16, /bin/su target, RHEL 8/9/10/OpenShift/RHOSP, blacklist act_pedit mitigation.
- § 1 Microsoft TonRAT: TonRAT, Photo ZIP, Calendly/SendGrid laundering, share.google, Node.js v24.13.0, dual HKCU\Run + HKCU\RunOnce, csc.exe/cvtres.exe, Add-MpPreference exclusions, Dutch/Danish/Japanese lures, hospitality Europe/Asia since April 2026 — all confirmed.
- § 4 Windchill: CVE-2026-12569, KEV 2026-06-25, CVSS 9.3, JSP /Windchill/login/<16-hex>.jsp, flst.txt — confirmed (brief correctly omits the IOCs the source carries).
- § 4 Cisco SD-WAN (Mandiant): CVE-2026-20127/20182/20245, evil_tenant.csv via `request tenant-upload`, troot in /etc/passwd+/etc/shadow, service-provider victim, anti-forensic revert/delete — confirmed.
- § 4 Klue (SecurityWeek): ~two dozen / ~195 orgs, Lucanet, Link11, Camunda, Deel, Tines, Icarus compromised + second unnamed actor + leak site offline — confirmed.
- § 3 StrikeShark (Securelist): SharkLoader, StrikeShark cluster, LOW-confidence Chinese-speaking, Perfect DLL Hijacking (LdrpLoaderLock/LdrpWorkInProgress), DscCoreR.mui/SyncRes.dat, Detours 50+ APIs, EtwEventWrite nulling, the five named initial-access CVEs, North Macedonia/Serbia, government targets — confirmed.

### Coverage shape / style
- § 1 leads with CH/EU/public-sector-relevant items (Signal phishing of CH gov staff; Canvas affecting CH/DE/AT universities) before global. § 2 inclusion gate caveat for the two local LPEs is honestly logged in § 7. Deep dive (Turla STOCKSTAY) earns its length and has a clear CH foreign-affairs nexus. No § 0 Immediate-Actions callout over-claim. No IOCs in prose. English throughout. No workflow-internal language. Vanity-metric-free.
- F13/F14/F15 sweep: no analytical-link-as-fact (the one cross-actor link — Miasma↔codfish — is source-supported); the "478 victims" / "~24 firms" / "second-most-targeted" / "13 commands" / "160 universities" quantifiers are each carried verbatim from a fetched source; no unflagged name-collision (Miasma/Shai-Hulud reuse is the same campaign lineage, correctly framed as an UPDATE).

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 3)

The brief is in strong shape and the iteration-2 fixes all held. One truth finding (F3, agency misattribution in the Citizen Lab item) and three non-blocking advisory items (F11a–c). F3 is low operational impact but is a quotable source-vs-brief discrepancy a hostile reader would catch.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: research
  item: "Citizen Lab: Cellebrite UFED used by Russian authorities"
  url_or_quote: "an official Russian Investigative Committee forensic report explicitly names the UFED tooling"
  summary: "Citizen Lab states the forensic expert report (ZAKLYUCHENIE EKSPERTA No 1269-17) was authored by the MVD's Forensic Expert Center, only commissioned by the Investigative Committee. Brief attributes authorship to the Investigative Committee. Fix: attribute to the MVD Forensic Expert Center (commissioned by the Investigative Committee)."
- code: F11
  category: editorial-advisory
  section: tldr / updates
  item: "Socket source date inconsistency"
  url_or_quote: "Socket, 2026-06-26 (TL;DR) vs Socket Security, 2026-06-25 (s4 body/footer)"
  summary: "Socket page is dated 2026-06-25. TL;DR cites 2026-06-26; body/footer correct. Align TL;DR to 2026-06-25."
- code: F11
  category: editorial-advisory
  section: updates
  item: "Klue victim list — Autodesk"
  url_or_quote: "newly named EU-domiciled victims including ... alongside Blackbaud, Autodesk, Deel, Camunda and Tines"
  summary: "SecurityWeek flags Autodesk as potentially unaffected (non-Salesforce integration). Drop Autodesk or add the hedge."
- code: F11
  category: editorial-advisory
  section: updates
  item: "ENISA EUVD additional source renders blank"
  url_or_quote: "https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-37831"
  summary: "EUVD SPA returns an error screen to non-browser fetchers. Specific-entry URL, Additional source only, primary THN supports the claim. Advisory only."
```
