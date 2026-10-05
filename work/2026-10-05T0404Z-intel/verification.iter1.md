**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-05T04:37:11Z · ended_at=2026-10-05T04:46:39Z · duration_seconds=568

## Verification report — 2026-10-05T0404Z-intel (iteration 1)

Scope: three changelog records (no new entries), the run record, registry additions (`campaign:stac4924`, aliases on `actor:rhysida` and `malware:loremipsumloader`). All 71 ledger claims have a verdict row in `verification.iter1.claims.yaml` (63 ok, 5 F3, 2 F14, 1 F5). Every cited page was fetched live this iteration (Sophos, Microsoft, DIVD cases 00014/00015 plus overview page and both CVE records and the log-check script, NCSC-NL, Zammad statement, Citrix bulletin and both Citrix blogs, Cyber Press, heise, ASD ACSC, CISA KEV via the bridge, CISA alert via WebFetch). `git diff HEAD` confirms every changed line in the three entries is declared in the run's record (fields lists are complete; no silent edit; `updated_at` mirrors correct; Citrix `improvement` correctly leaves `updated_at` null).

Registry check: `campaign:stac4924` summary and the three relations match Sophos (`uses` Lorem Ipsum Loader; `overlaps-with` the TerminalFix campaign, worded as tooling and tradecraft alignment; `attributed-to` actor:rhysida carries Sophos's "support BlueVoyant's attribution" and the no-encryption caveat in its note, so the overlap is not silently upgraded). Aliases "Rapid Brigantine" and "GOLD VICTOR" rest on Sophos's own equivalence statement ("Rapid Brigantine ... which Sophos CTU researchers track as GOLD VICTOR (also known as Vanilla Tempest, DEV-0832, VICE SPIDER, and Vice Society)"); "Lorem Ipsum Loader" is Sophos's spelling. No finding.

Run record: counts, `updated_entry_ids`, `entities_added`, sources_changed, backlog strikes (TCS, Securitas) and the KEV disposition all agree with the working tree and `git diff` (KEV catalogue released 2026-10-04T18:52:56Z with CVE-2026-88779 `dateAdded` 2026-10-04). One note statement rests on a wrong date (finding #5 below): "The page carries a 2026-10-02 08:30 GMT header, so the item rests on the 72 h developing window".

### Citation does not support the claim

- #3 (F3) `2026-08-31/microsoft-terminalfix-clickfix-reverse-tunnel-campaign`, Defender takeaway paragraph: "The other pairings Sophos lists follow the same shape: a legitimate Windows or updater-named executable running from a user-writable or application directory with a DLL beside it that it loads from there" ([Sophos](https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling)). Sophos Table 1 has only "Legitimate application" / "Malicious DLL" columns; the page gives no run location for any pairing, and `bin.exe` / `net runtime optimization service.exe` are not "Windows or updater-named". Same gap in the preceding clause "so the same finding for any other executable running from a user-writable or application directory beside a planted DLL carries the same weight" (claim cc19f93ca2): an inference attributed to the Sophos link. Drop the location claims or present them as inference.
- #4 (F3) same entry, update section 2026-10-05T04:34:00Z: "and executables renamed to look like Microsoft Edge or Teams helper components". Table 1 lists "Microsoft Edge Updates Helper.exe" and "Microsoft Teams Revo Helper. Exe" under "Legitimate application"; Sophos does not say they were renamed (only `ResilientStorageCoordinator.exe` is marked "originally WerFaultSecure.exe"; the masquerading Sophos describes is of persistence entries). Rewrite as "named like".
- #5 (F3) `2026-10-02/zammad-cve-2026-102489-102490-exploited-divd-breach`, Update 2026-10-05 and the new Defender-takeaway sentence, `sources[].date`: citations read "DIVD CSIRT, 2026-10-02". The canonical page https://csirt.divd.nl/cases/DIVD-2026-00014/overview_data_investigation/ carries JSON-LD `"dateModified":"2026-10-01T14:19:22+02:00"` and DIVD's case timeline says "01 Oct 2026 | Publication of overview of which data is compromised and which data is not". The 2026-10-02 08:30:33 GMT "Published Time" the jina rung returned is the site build time (case DIVD-2026-00015 shows the identical header while stating "Last modified 01 Oct 2026 13:27 CEST"). One-day drift, not a timezone artifact (12:19Z on 10-01). It also breaks the run record's window justification: 2026-10-01T12:19Z precedes the 72 h window start (2026-10-02T04:04Z).

### Quantifier without source

- #1 (F14) `2026-08-31/microsoft-terminalfix-clickfix-reverse-tunnel-campaign`, frontmatter `summary`: "19 different legitimate executables sideloading a malicious DLL". Table 1 has 19 rows (pairings) but 15 distinct executables (changepk.exe x3, embeddedapplauncher.exe x2, sessionmsg.exe x2; `ResilientStorageCoordinator.exe` is "originally WerFaultSecure.exe"). Body and record correctly say "19 pairings"; the summary should too.
- #6 (F14, low confidence) Zammad entry, Update 2026-10-05: "DIVD marks its investigation of each data category as ongoing". The page marks "Our accounting systems" and "Our bank account" "Not under investigation". In context only the scan-data, reported-vulnerability and credential-dump categories are meant (all "Ongoing"); narrow the wording.

### Unsupported / hallucinated facts

- #2 (F4, low confidence) TerminalFix frontmatter `summary`: "Sophos reports the same chain running since March". Sophos: campaign STAC4924 "active since at least March"; phase 1 (March-April) was SEO-poisoned sites with trojanized Teams MSI installers and a PowerShell loader; "Beginning in late May, the campaign transitioned from signed MSI installers to TerminalFix lures". The TerminalFix chain is the second phase.

### Claims missing inline citation

- #7 (F5, low confidence, pre-existing text) TerminalFix body paragraph 2: "Persistence lands through both an `HKCU\...\Run` registry key and a scheduled task re-executing every 60 minutes ..." has no inline link. Content is supported by Microsoft's section 4 (Run key, scheduled task every 60 minutes, `LockScreenContentServer_MuODG5yBM` masquerading name, hidden folder), so it is a citation gap only.

### Editorial / less-is-more flags (advisory)

- #8 (F11) TerminalFix `sourcing_note` (edited this run): still carries "the same independent national-CERT confirmation that moved the sibling Berlin Landesnetz entry's credibility from 2 to 1" (credibility digits and a "sibling entry" reference) and the new sentence is ungrammatical ("as one its own observations support"). Two sentences of provenance suffice. Pre-existing em dashes remain in the body and `sourcing_note`.
- #9 (F11, low confidence) Citrix entry: record typed `improvement`, section opens "The earlier text said the flaw was not in CISA's KEV catalog as of 2026-10-04." The earlier statement was true when written (entry 2026-10-04T04:38Z, KEV released 18:52Z that day), so the KEV listing is a new development, not a correction. The run record's reasoning ("bookkeeping, no float") is an editorial call the main agent may keep; the section would read better leading with the fact than with the entry's own history. All Citrix claims, the KEV description quote, the CISA alert, the version tables and the frontmatter changes verified clean.
- #10 (F11, low confidence) Zammad entry: the cited overview URL `https://csirt.divd.nl/DIVD-2026-00014/overview_data_investigation/` is a client-side redirect stub (200 "Redirecting..." with meta refresh); only the jina rung read it. The canonical `https://csirt.divd.nl/cases/DIVD-2026-00014/overview_data_investigation/` reads cleanly via `extract` (fetched this iteration); `https://csirt.divd.nl/DIVD-2026-00015` has the same shape. Also, the page dates to 2026-10-01 (before the entry's own creation and linked from the case page it already cites), so the `update` re-floats four-day-old material; defensible as a missed delta.

### Missed angles

None nameable. S1 to S4 and the KEV window diff (one in-window addition, CVE-2026-88779, covered) leave no gap I can evidence; two web searches for in-window exploited zero-days and Swiss communal incidents surfaced nothing dated in the window. The run's own "not worked" leads (ENISA Threat Landscape 2026, dated 2026-09-22) are outside the window. Coverage looks complete for a quiet Sunday.

### Verdict

NEEDS_FIXES (truth: 6, editorial: 1, advisory: 3)

### Findings summary (machine-readable)

See `work/2026-10-05T0404Z-intel/verification.iter1.findings.yaml` (10 records, identical to the findings above).
