**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-15T15:19:15Z · ended_at=2026-11-15T15:46:50Z · duration_seconds=1655

## Verification report — 2026-11-15T1407Z-audit (iteration 1)

Scope: first pass, cold. All 166 ledger claims have a verdict row (`verification.iter1.claims.yaml`: 147 ok, 11 F3, 6 F4, 2 F5). New entry read whole and every cited page fetched. For each of the 28 updated entries the `git diff b010c9a5` was read, every changed claim was checked against its cited page, and the record `summary` was compared with the section. Unchanged text was read only where a new section or field supersedes or depends on it. Run-record and audit-report claims about disk, state and counts were checked (record counts 7/10/11 with 12 internal, truth-pass tallies 27/24/5 and 1,646 claims, 14 of 56 `high` at base and now, KEV 12/8/4, 16 `last_seen` bumps, CVE-2026-124014 added, six product records and two `ambiguous_labels`, sources.json changes, v4.25 banner/CHANGELOG, `test_check_run.py` 9/9, 25 non-product registry records, Publica 1,100 / eMudhra 878 / AhsayCBS 576 words): all hold except the SonicWall statements below. New entry `2026-11-15/artex-aws-cloudwatch-log-secret-hunting-cognito-self-signup`: every claim matches the Datadog and Wiz pages, references exist, classification and `single-source` are consistent, no defects found.

### Citation does not support the claim

- **#1 SSHole summary (2026-11-06).** "Previdian's and SANS ISC's sensors record attempts from 2026-11-05". Previdian (`https://previdian.com/CVE-2026-123158`): "First observed Nov 06, 2026"; only SANS ISC dates 2026-11-05. The body itself says Previdian first on 2026-11-06. Fix: split the dates.
- **#2 Dixell/Copeland section 2026-11-15T14:53:24Z.** "the unfixed exposure is the pre-2021 fleet plus the predictable-password flaws and CVE-2026-124014, which reach the last firmware" cited to the VulnCheck blog. The blog lists CVE-2026-124014 among the pre-2021 `.lua`-era flaws ("fixed on the current branch") and never says it reaches 5.8.8; only the CNA advisory does ("XWEB EVO 4.3.0 through 5.8.8", cveawg agrees). The blog/CNA disagreement shows only in `sourcing_note`; the section and `cves[]` (`no-patch`) state one side as fact. Fix: cite the CNA advisory for the range and state the disagreement in the section.
- **#3 Chrome (2026-11-11) Exposure line.** "Edge below 157.0.4341.46, Edge for Android below 157.0.4341.53 ... ([Google, 2026-11-09](chromereleases...stable-channel-update-for-desktop_018223192))". The Google post carries no Edge builds; they are Microsoft's (Edge security release notes). Fix: add the Microsoft citation.
- **#4 Publica main analysis (low confidence).** "The Bernische Pensionskasse says its supplier is the same company ([BPK, 2026-10-30](https://bpk.ch/hauptnavigation/cybervorfall))". The page names PK Softech AG as its supplier but never says it also serves Publica; the same fire's Correction section says exactly that this is AWP's report. Fix: re-cite to cash.ch or reword.
- **#5 AhsayCBS Detection (low confidence).** "(the CBS JVM on Linux)" under a Huntress citation; Huntress names only `cbssvcX64.exe`/`cbssvcX86.exe`. "or the CBS JVM (Linux)" is Horizon3's wording.
- **#6 AhsayCBS Defender takeaway (low confidence).** "or on v10 ... the v10.3.6.1 release" cited to the v9.17.0 notes and the 2026-10-12 hotfix announcement; neither names v10.3.6.1 (release-1036 is cited only in the update section), and "or later" for the hotfix is not stated.
- **#7 eMudhra section 2026-11-15T15:05:50Z (low confidence).** "Azure CLI 2.93.0 ... to remove the remaining roots from its bundled trust store"; Microsoft: "removing two eMudhra roots: emSign Root CA - C1 and emSign ECC Root CA - C3". The 2026-11-12 update is also labelled [Microsoft, 2026-11-10].
- **#8 Brotli section 2026-11-15T15:04:45Z (low confidence).** "marks NX-OS Software as impacted in its priority-product table"; the table row reads "NX-OS Software: See the Impacted Products with Software Fixes and Products Confirmed Not Vulnerable tables". Nexus rows, CSCwx56979 and the fix list verified.
- **#9 BluePhishing headline (low confidence).** "default users can now create blueprints"; MC1506733 (dated 2026-10-13) is a schedule ("Starting November 4 ... expected to complete by late November 2026"); no source confirms it is live. The section's "will be able to" is right.
- **#10 LLMjacking section (low confidence).** "Obsidian Security, which disclosed CVE-2026-40217": Obsidian credits X41 D-Sec with the playground path and says its own variant is "tracked under CVE-2026-40217". Page JSON-LD `datePublished` is 2026-09-08 against the 2026-06-15 label.
- **#11 Dixell takeaway (low confidence).** "two flaws are exploited ... ([Dixell France, 2026-10-14])": the exploitation fact is VulnCheck's; the guide predates it.

### Unsupported / hallucinated facts

- **#12 SonicWall (2026-11-07), update 2026-11-15T15:08:15Z: headline, actions[0], Defender takeaway, section, record summary.** The section says "SonicWall's bulletin page returned no readable content, so it is not established that it concerns the SAML bypass; for Gen7 firewalls 7.3.4-7015 or later covers both bulletins"; the headline moves to "upgrade Gen7 to 7.3.4-7015"; the action says "7.3.4-7015 also a second SonicOS bulletin of 2026-11-10". SNWLID-2026-0021 is readable: `https://psirtapi.global.sonicwall.com/api/v1/vulndetail/?advisory_id=SNWLID-2026-0021` (and the PSIRT page via `extract`) returns "Informational Advisory: SonicOS Client DPI-SSL Trust of Compromised eMudhra Certificate Chain", CVE null, remediation by removing eMudhra roots. It is the same advisory the eMudhra entry already cites and whose 7.3.4-7015 / 8.2.3-8015 targets it already carries. SNWLID-2026-0014 (API) lists 7.3.4-7013 and 8.2.3-8015 as the fix for CVE-2026-19868. G1 flagged this as a LOW-confidence unverified lead; it was promoted to a published update without reading the vendor page. Fix: drop the update and restore 7013, or reduce it to a cross-reference to the eMudhra entry.
- **#13 Run record and audit report (same cause).** Run record Coverage gaps: "the SonicWall PSIRT page for SNWLID-2026-0021 (empty to every reader, WebFetch included)". Report Watch items: "SonicWall SNWLID-2026-0021 (new): CERT-FR relays it without a CVE, and SonicWall's page returns no content to any reader"; table row "a second bulletin, SNWLID-2026-0021, fixed in 7.3.4-7015"; "Recovered as records ...: CERT-FR's SNWLID-2026-0021 on SonicWall". The advisory is readable and unrelated (see #12).
- **#14 AhsayCBS actions[0] (low confidence).** "install v9.17.0 (v7 to v9)": the v9.17.0 notes do not say v7/v8 servers take it, and Ahsay's announcement routes "v7, v8, and v9" to hotfix v9.15.2.70.

### Claims missing inline citation

- **#15 GhostFrame body, first paragraph, last sentence.** "Its command channel opens simultaneous TCP connections ... mainly an in-memory shellcode loader." carries no citation (facts are on the Recorded Future post; the sentence was trimmed by this fire).
- **#16 Chrome `cves[].cvss` 8.8 and `sourcing_note`.** The MSRC record (`https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-125350`: CISA ADP CVSS:3.1 8.8, released Nov 13, revision 1.1 "Added Microsoft Edge software") is verified but is neither in `sources[]` nor cited inline, and the new section never states the score or revision the record summary names.

### Drop (low relevance / off-audience / duplicate)

- **#17 SonicWall non-internal `update` record.** No genuine delta for this finding (an unrelated eMudhra advisory the store already carries), yet it moves `updated_at` and re-floats the entry (4c(a), 4c(i)). See #12.

### Needs more research

- **#18 AhsayCBS v10 fix (low confidence).** Ahsay's v10.3.6 release notes (02-Nov-2026) list "Ahsay Security Patchset for CVE-2026-105133 and CVE-2026-105134", remote API off by default and the JSP engine disabled; the entry says only "security hardening" for v10.3.6.1, leaving v10 owners without the statement that the standard release patches both flaws. v10.3.6.14 (13-Nov) exists.

### Editorial / less-is-more flags (advisory)

- **#19 Workflow phrasing in reader-facing sections.** Fortinet Correction: "The entry said FortiAnalyzer and FortiManager 7.2 must migrate ..."; SonicWall: "Neither CERT-FR nor any other read source ... returned no readable content".
- **#20 Brotli `cves[].affected` garble.** Starts "Siemens Desigo CC V8 and V9, all versions, and since version 1.13 Nexus 3000 and 9000 switches running Guest Shell, fixed by Guestshell 4.9 or NX-OS releases due from December 2026 to February 2027; Siemens SIMATIC ..." The Nexus fragment is spliced into the Siemens clause (and repeated correctly at the end of the field).
- **#21 Record summaries versus sections.** AhsayCBS names "the CNA" (true, CWE-78 per cveawg, but the section cites CISA only); Chrome names the Security Update Guide score (not in the section); GhostFrame omits the trim of "with a reverse-shell fallback"; Fortinet omits the heise removal.
- **#22 Check Point.** Removing the uncited KEV-feed source leaves `cisa-kev` in `cves[].status` and the sourcing-note KEV statement with no listed source.
- **#23 Citation date labels on new sections** carry the first-publication date of rolling pages (Canonical 2026-11-10 for a 2026-11-14 tracker, Veeam 2026-11-10 for 2026-11-13, Sophos 2026-11-06 for version 5, Microsoft 2026-11-10 for 2026-11-12, Cisco 2026-10-27 for version 1.13; eMudhra's Cisco record says "version 1.11" but is dated 2026-11-10, revision 2026-11-13).
- **#24 Publica correction.** "says only that an external software supplier ... detected a cyber incident": the 9 October notice also states the criminal complaint and the Federal Prosecutor's investigation.
- (pre-existing) AhsayCBS Exposure still reads "below the hotfixes v10.3.4.45 or v9.15.2.70" although v9.17.0 and v10.3.6.1 now ship.

### Missed angles

None to report. The three re-sweeps' dropped items hold on their stated grounds, all twelve KEV additions have dispositions, and Oracle's 2026-11-17 CPU is a watch item for the next fires. Coverage looks complete for critical/high signal.

### Verdict

NEEDS_FIXES (truth: 14, editorial: 4, advisory: 6)

The decisive defect is #12/#13: a lead the research agent marked unverified was published as an update on the SonicWall entry, changing its headline and action, and the "unreadable page" premise is false. Everything else is local wording or citation binding. No prior-iteration deltas block was supplied.

### Findings summary (machine-readable)

See `work/2026-11-15T1407Z-audit/verification.iter1.findings.yaml` (24 records: F3 x11, F4 x3, F5 x2, F7 x1, F8 x1, F11 x6).
