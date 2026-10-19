**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-11T16:13:04Z · ended_at=2026-10-11T16:34:47Z · duration_seconds=1303

## Verification report — 2026-10-11T1307Z-audit (iteration 2, slice s4)

Scope: 20 entries, 252 ledger claims, every claim walked (249 ok, 2 F5, 1 F3; rows in `verification.iter2.s4.claims.yaml`). Every cited page was fetched this iteration (cached bodies first, `extract`, `pdf`, `ncsc-csh post`, `cisa-kev`, raw HTML for CVSS vectors); 64 URLs appended to `url-liveness.tsv`. Whole entries were read, not only ledger claims; evidence quotes of the entries with `evidence[]` were spot-checked literal against the fetched pages.

### Prior-iteration deltas (walked first)

Applied and confirmed on disk and against the source:
- Inditex F3 (about 197,000 in headline/summary/body; HIBP "197k"), Exchange F3 (June blog co-cited; June and July blogs both say the update does not remove the mitigation), Exchange F4 ("stored" gone from title/summary/body; MSRC says cross-site scripting), Exchange F4 supersession (07-31 takeaway now "June shipped the fix, July is the recommended update"), PAN-OS F4 (event_date 2026-05-13 = PSIRT date), CVE-2026-3300 F4 (event_date 2026-06-03 = Wordfence) and F11 (sourcing note rewritten), CVE-2026-42271 F3 (KEV catalog cited; KEV dateAdded 2026-06-08) and F18 (action trimmed), Check Point F3 (Rapid7's own wording), F4 (companion pointer removed) and F8 (Detection adds the ELF downloads Check Point observed), WinRAR F4 (Telegram move limited to SHADOW-EARTH-066 with THN's "likely aligns") and F12 (single-source, sourcing note names Trend Micro), chosen-brick F5 (The Record cited), TraderTraitor F14 ("none for Linux" gone; Zscaler says Windows and macOS ROOFDECK variants), SolarWinds F4 (reworded to narrowing who can reach it; vectors AV:N / AV:A confirmed in the trust-center HTML), UNCTAD F3 x2 (Transluce "not attributing this traffic as a whole to OpenAI"; swarmcha.se 400 on GET on 28 April, double-encoding on 4 May), Kaspersky F18 (action keeps the audit task), Publica F3 (Inside IT cited for BLVK) and F9 (PK Post anonymisation statement surfaced; identity-proof advice no longer extends to PK Post insured).

Partly landed (reported below): WinRAR F11 (only the sourcing note was addressed; ATT&CK ids in prose, `entities: []` against an existing registry key, the uncited hunting sentence and the missing labelled lines remain).

Declined, judged:
- LiteLLM-42208 F11 (Sysdig's 36 h runs from the global-database listing, 2026-04-24): rationale holds; the body says "reached the global database" and Sysdig's own title and wording use "advisory/disclosure". No new finding.
- ENISA F7: holds (routine, two sentences; entries are only removed by folding).
- Inditex F7: holds (routine; the token-scope lesson is stated in the takeaway).
- CVE-2026-42271 F11: holds (the Check Point row is accurate against the Check Point blog: 9.3, since 7 May, Qilin-affiliate case, sk185033, KEV 2026-06-08; em dashes are stripped at render per cti-run.md).
- AFPA F12: holds (the trackers add independent sample reviews; credibility was lowered to 2 accordingly). AFPA F11 and Publica F11: hold mechanically (a rewrite above about a dozen words needs a non-internal record); both remain advisory.
- Exchange F11 ("append-only"): partly wrong, see F11 #3.
- Publica F16: rationale mixes up the critical and high bars, see F16 #1.

### Citation does not support the claim
- **F3 #1** `inditex-zara-...` Correction 2026-10-11T13:56: "the records span international markets rather than EU customers only ([Have I Been Pwned])" (low confidence). HIBP says only "the market the support ticket originated in" and lists "Geographic locations"; "different markets" is BleepingComputer's wording (Inditex statement), not cited on the clause. Co-cite BleepingComputer or trim.
- **F3 #2** `cve-2026-42897-exchange-...` Update 2026-07-31: "a named Russian state-supported actor" and "the Russian state-supported email-espionage actor ... ([Proofpoint, 2026-07-29])" (low confidence, citation gap with a true fact). The cited Proofpoint page says "Russia-aligned threat actor TA488" and never "state-supported"; that wording is the NSA/FBI joint advisory's title ("Russian State-Supported Cyber Actors Conduct Phishing Campaign Targeting Users of Zimbra", read via the pdf recipe), which the entry does not cite. Cite the advisory or use "Russia-aligned".

### Unsupported / hallucinated facts
- **F4 #1** `cve-2026-42897-exchange-...` event_date 2026-05-17 (low confidence): primary Exchange blog 2026-05-14, MSRC "Released: May 14, 2026". Same defect class iteration 1 fixed on PAN-OS and CVE-2026-3300.
- **F4 #2** `cve-2026-42271-berriai-...` event_date 2026-06-01 (low confidence): GHSA primary published 2026-04-21, KEV listing 2026-06-08; 06-01 is only Horizon3's chain post.

### Claims missing inline citation
- **F5 #1** `cve-2026-42897-exchange-...` "Exchange Online is not affected." No inline link and none of the paragraph's citations carries it; the May Exchange blog does ("Exchange Online is not impacted by this vulnerability").
- **F5 #2** `year-old-winrar-...` "hunt `wscript.exe`/`mshta.exe` spawned from archive-extraction events, Startup-folder writes (Sysmon EID 11), and PowerShell script-block logging (EID 4104) for in-memory reflection": uncited and partly beyond the sources. Trend Micro's own list is cmd.exe launching PowerShell with bypass/hidden flags from ProgramData, PowerShell allocating executable memory, and mshta.exe from the Startup folder; wscript.exe, Sysmon EID 11, EID 4104 and the archive-extraction lineage are in neither Trend Micro nor THN (0 grep hits).

### Needs more research
- **F8 #1** `year-old-winrar-...` Trend Micro gives "CVSS 8.4, patched in WinRAR 7.13 in July 2025", says WinRAR is outside Group Policy and central update tooling, and advises inventorying apps outside standard update channels and quarantining RAR at the mail gateway. The entry says only "ensure deployed versions are current", `cves[].cvss: n/a`, and has no Exposure or Defender takeaway line (actionability contract).

### Editorial / less-is-more flags (advisory)
- **F11 #1** WinRAR: ATT&CK ids still in prose; `entities: []` although registry key `campaign:uac0226-giftedcrook-winrar-cve-2025-8088` exists for this finding (delta F11 partly landed).
- **F11 #2** CVE-2026-42271: internal record summary names only the added reference while `fields` also lists `actions` and `body`; em dashes remain in title/headline/body text this fire rewrote.
- **F11 #3** Exchange: the 2026-08-30 Improvement section carries Admiralty letter/digit and "This entry"; the "append-only" decline covers the record, not the section (CLAUDE.md allows revising earlier sections through the current record). May be left.

### Org-triage / priority
- **F16 #1** `publica-pk-softech-...` (low confidence) the declined rationale treats `high` as act-now. The high bar is exposure of the constituency (supply-chain incident reaching federal-administration and cantonal staff data) plus a 7-day decision beyond the cycle, which the entry's first action describes. Doubt resolves to notable, so a calibration question rather than a fact defect.

### Missed angles
None found for this slice; coverage of these items looks complete.

### Verdict
NEEDS_FIXES (truth: 4, editorial: 4, advisory: 3). All four truth findings are low confidence; the F3 and F4 items each rest on a fetched page quoted above.

### Findings summary (machine-readable)
See `work/2026-10-11T1307Z-audit/verification.iter2.s4.findings.yaml` (11 records).
