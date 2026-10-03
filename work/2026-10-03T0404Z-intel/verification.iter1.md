**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-03T04:46:17Z · ended_at=2026-10-03T04:58:52Z · duration_seconds=755

## Verification report — 2026-10-03T0404Z-intel (iteration 1)

Scope: 1 new entry, 3 updated entries, run record; all 85 ledger claims have a verdict row (`verification.iter1.claims.yaml`: 77 ok, 3 F3, 2 F4, 2 F5 at claim level). No prior-iteration deltas block (first pass). Pages read this iteration: Symantec, both BleepingComputer articles, Fortinet FG-IR-26-175 (extract, raw url, WebFetch), Belnet, NCSC-NL 0398, NCSC-CH hub posts 13027 and 13021 (via `ncsc-csh recent 40`, quote matched by hand), Cisco advisory (v1.1) and Live Protect page, VulnCheck, Risky Bulletin, CISA KEV (bridge) and both CISA alerts (WebFetch), Microsoft ToolShell guidance.

### Answer on the FortiMail file-table citation
- Fortinet's page today carries: affected/solution table, three workarounds, two IPs, three system-event log lines (cron `O=/migadmin`, admin logout, CLI "Added 'archive234' to 'archive account' ... destination[remote]"), IBE decrypter log lines, acknowledgement, "Virtual Patch: No", Timeline "2026-10-01: Initial publication". It carries NO file table.
- BleepingComputer (2026-10-01) carries the file table (liblog.so, smit, webconsole, mailservice, httpd.conf, ld.so.preload, migadmin.tar.gz with Added/Modified) and says Fortinet published it; NCSC-CH 13027 names ld.so.preload, webconsole, mailservice.
- The prior run's verifiers read that table on Fortinet's own page on 2026-10-02 (`work/2026-10-02T0404Z-intel/verification.iter3.claims.yaml:643`), and the same page then said "management interface" (iter8:645). Fortinet revised the advisory after publication without a Timeline entry: workaround now "webmail interface" plus a WAF rule, IBE GUI path added, file table gone.
- As written, the file clause is cited to Fortinet alone, which the page does not support (F3 #1); the log-event clauses in the same sentence are supported by it. The following BleepingComputer sentence is supportable.

### Broken / unreachable URLs
None. All cited URLs resolved.

### Generic / oversight URLs (replace with specific article)
- F2 #1 (low confidence): `2026-10-02/cve-2026-104286-...` cites the whole-catalog KEV JSON feed. Per-event page read this iteration (WebFetch): https://www.cisa.gov/news-events/alerts/2026/10/01/cisa-adds-one-known-exploited-vulnerability-catalog (CVE-2026-104286, posted October 1, 2026).

### Citation does not support the claim
- F3 #1: FortiMail, "Fortinet's compromise section shows ... a shared library added ... ld.so.preload entry ... modified admin-migration archive; a cron job ..." cited to Fortinet only. Page has no file table (WebFetch: "No table of added/modified files was present"). Attribute files to BleepingComputer/NCSC-CH, logs to Fortinet; same for the Detection line "Fortinet's advisory lists the exact artifacts and log patterns" and the file part of actions[1].
- F3 #2: Cisco, "[Cisco, 2026-10-03](...live-protect...)" and sources[].date 2026-10-03: page dateline "Updated: July 1, 2026", meta date 2026-08-04; 2026-10-03 is the fetch date.
- F3 #3 (low confidence): Warlock Defender takeaway cites Symantec for "replace the machine keys if a web shell is found"; Symantec does not say it (entry's own Exposure note). Microsoft's guidance (fetched) does.

### Unsupported / hallucinated facts
- F4 #1: FortiMail Update section "The workaround text and the exposure statement above are corrected to Fortinet's wording" (and record summary / body "not Fortinet's wording" / run-record note): frames Fortinet's later revision as an error in the earlier text and in BleepingComputer and NCSC-CH, which repeated Fortinet's then wording ("management interface"). Say Fortinet revised the advisory.
- F4 #2: FortiMail evidence[1] "Disable the IBE feature support using the following CLI command:" is not on the live page ("... via the GUI ( Encryption -> IBE -> IBE Service 'off' ) or with the following CLI command:").
- F4 #3 (low confidence): Warlock Triage "a service installed from a system folder on a host already showing SharePoint exploitation": Symantec installs the tunnel on Computer 4, a further host, not a SharePoint server (Computers 1 and 2).

### Claims missing inline citation
- F5 #1 (low confidence): two Warlock sentences without an inline link (2026-07-22 web shell; 2026-07-31 tool killer and K7RKScan CVE-2025-1055). Symantec supports both.

### Needs more research
- F8 #1 (low confidence): Cisco Update says "the advisory does not say which releases support the shield"; the cited Live Protect page states the rule (current release plus the two preceding in each supported train that includes Live Protect).

### Surface contradiction
- F9 #1 (low confidence): NCSC-NL (cited) says "Fortinet heeft beveiligingsupdates uitgebracht" against Fortinet's "upcoming" fixes; no Contradiction line.

### Editorial / less-is-more flags (advisory)
- F11 #1: FortiMail Update section names `webconsole` and `mailservice` (file-name indicators; main body avoids them) and narrates its own correction.
- F11 #2: Belnet, Cisco (and FortiMail's Belnet paragraph): Update sections repeat facts already integrated into the rewritten main analysis; keep the delta only.
- F11 #3: Warlock `techniques[]` omits T1036.010 for the setup-lookalike account Symantec calls masquerading.

### Checked and clean
- Warlock: every Symantec figure, date and behavior (4 organizations, 40 hosts/2 h, 33 hosts, 2026-07-22/28/31, SYSVOL/dfsrs.exe on 3 hosts, machine-key web shell, VS Code tunnel, NetExec, K7RKScan) matches; 3 evidence quotes verbatim; BleepingComputer relay and date correct; no IOCs; classification B/2 and single-source flag correct; all 15 technique ids active in pinned v19.2; actor key and `Longlegs`/`china-nexus` registry change match Symantec; four ToolShell CVE index records match the cited text; not a duplicate (no prior Warlock/Longlegs entry, two Swiss SharePoint entries correctly referenced). `high` is defensible on the two Swiss SharePoint breaches and the key-theft persistence.
- FortiMail: CVSS 9.8, versions, KEV date, upcoming fixes, workaround text, IoC log lines, Belnet window and remediation time, NCSC-CH quote (matched in post 13027), `updated_at` = record `at`, record `fields` cover every changed field, no silent edit.
- Belnet: all four evidence quotes verbatim, 65-day window, 2026-09-29 actions, CCB, Risky Bulletin claim; record summary matches section; priority move to `notable` follows from the now-known vector.
- Cisco: v1.1 text, shield limitation quotes, fixed-release table, log paths, TAC procedure, VulnCheck mechanism and counts, CISA alert, NCSC-CH 13021; record summary matches section.
- Run record: counts, KEV sweep (Zammad only, COVERED), 7 open backlog rows and the 2026-10-05 expiry hold on disk; one inaccuracy: the FortiMail note frames the workaround wording as the entry's error (see F4 #1).
- Missed angles: none found. Searches for in-window items (exploited zero-days, Swiss public-sector incidents, BleepingComputer 2026-10-02 headlines) returned only covered or out-of-window material (Citrix, Cisco, FortiMail, Warlock, Dell CSM dropped per record, SonicWall and Chrome older and already in the store). Coverage looks complete for critical/high signal.

### Verdict
NEEDS_FIXES (truth: 7, editorial: 3, advisory: 3)

### Findings summary (machine-readable)
See `work/2026-10-03T0404Z-intel/verification.iter1.findings.yaml`.
