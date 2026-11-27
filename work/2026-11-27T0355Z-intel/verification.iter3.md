**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-27T06:07:46Z · ended_at=2026-11-27T06:32:52Z · duration_seconds=1506

## Verification report — 2026-11-27T0355Z-intel (iteration 3)

Scope: post-fix pass after NEEDS_FIXES iteration 2. All 325 claims of `claims.iter3.yaml` walked (39 changed claims, every claim of the 11 entries, nothing sampled). Verdicts: 319 ok, 2 F3, 2 F4, 2 unreadable (rows in `verification.iter3.claims.yaml`). Every one of the 97 cited URLs was fetched this iteration (extract / pdf / ncsc-csh / direct url; CISA alert pages via WebFetch; KEV via `cisa-kev`).

### Prior-iteration deltas (all 14 re-read against the sources)

| # | Remediation | Result |
|---|---|---|
| 1 Juniper F3 | summary and sourcing_note attribute the SIRT wording to SecurityWeek | True to SecurityWeek ("At least one instance of malicious exploitation ... reported to the Juniper SIRT"; "On Tuesday, Juniper updated its advisory"). One residue: the NCSC.ch post's own summary field says "Juniper has confirmed malicious exploitation", so "SecurityWeek's quotation alone" overstates (finding F4 #4, low confidence). |
| 2 ARTEX F3 | "these two posts do not mention Storm-0940" | Confirmed: neither Wiz post (2026-11-23, 2026-11-25) names Storm-0940. |
| 3 PAN-OS F4 | "until then rested on Dream's account alone" removed | Confirmed: KEV record of 2026-10-28 and PAN-SA-2026-0015 both read; new text says only that the vendor now states exploitation and CISA has listed it since 2026-10-28. |
| 4 SoftwareOK F4 | "a Python runtime and a remote-access tool" | Confirmed against ASEC ("Package containing a Python runtime environment and a RAT"). |
| 5, 6 run record | nine `update` records; Contradiction paragraph in the 2026-11-27 update section | Confirmed on disk: all nine `updates[]` tails are `type: update`; the Zammad section carries the paragraph. |
| 7 SoftwareOK F13 | earliest-exposure reading marked as the entry's own | Present in the third body paragraph ("the entry's reading, since ASEC gives no window"); Exposure line and action still carry "since 2026-10-28" bare, acceptable beside the hedge. |
| 8 Mitel F5 | sourcing_note no longer mentions SecurityWeek's date | Confirmed. |
| 9 PAN-OS F5 | Exposure line cites PAN-SA-2026-0015 | Confirmed (dataplane interface with management profile is in the FAQ). |
| 10 Zammad F5 | report cited on its own clause | Confirmed; the quote is verbatim in the report. |
| 11 Fragnesia F10 | update record for PAN-SA-2026-0015 | Genuine delta (vendor statement of exploitation, later fixed builds), fields match the diff (`sources, evidence, sourcing_note, body, updated_at`), new evidence quote is verbatim on the bulletin. One consistency issue with the PAN-OS entry (F9 #8). |
| 12 F18 | nginx/Juniper actions | nginx: three single-product tasks, PAN-OS action gone, Veeam split out; Juniper: upgrade plus interim restriction. Acceptable. |
| 13 nginx headline | names 1.31.10, 1.30.8, Plus 37.3.1.1 | Confirmed against CHANGES, CHANGES-1.30 and the Plus release notes; `headline` is in the record's fields. |
| 14 Juniper "transport" | now "the bulletin page could not be read" | Confirmed. |

The iteration-2 remediation for the ARTEX Triage line introduced a new misattribution (F3 #1).

### Citation does not support the claim (F3)
- #1 **ARTEX** Triage: "on the two ConnectWise applications Expel reviewed, which call Graph with a .NET SDK, a Python user agent is the anomaly". Expel: "Huntress found the ConnectWise Cloud Management and Partner Center apps it reviewed call Graph with kiota-dotnet, so a Python user agent on one of those apps is the anomaly." Huntress reviewed them, not Expel.
- #5 (low confidence) **Zammad** Contradiction paragraph cites "[DIVD, 2026-11-18]" for the case page; the page reads "Last modified 25 Nov 2026 14:10 CET" (published 29 Sep, updated 18 Nov and 25 Nov). The 11-18 label cannot be confirmed for the quoted sentence.
- #6 (low confidence) **nginx** Veeam KB4976 is cited as 2026-11-25; the page reads "Published: 2026-11-20, Last Modified: 2026-11-25".
- #7 (low confidence, pre-existing) **Puppet** release notes cited as 2026-11-12; the page says only "Released November 2026" (HTTP Last-Modified 2026-11-26).

### Unsupported / hallucinated facts (F4)
- #2 (low confidence) **nginx** `cves[CVE-2026-123634]`: "NGINX Plus builds not itemised by any cited source, presumed 37.3.0.1 and 37.0.8.1" and sourcing_note "no cited source itemises NGINX Plus ranges for CVE-2026-123634". The F5 NGINX Plus release notes, cited and in `sources[]` since this run, list the resolver use-after-free (CVE-2026-123634) under PLS.37.3.0.1 and PLS.37.0.8.1.
- #3 (low confidence) **Puppet** update section: "and nothing of the server-side effect was seen" is attributed to Huntback; Huntback says "Our decoy signed the certificate, accepted the report with a 200, and returned no marker".
- #4 (low confidence) **Juniper** sourcing_note: "reaches the record through SecurityWeek's quotation alone ... NCSC Switzerland's post ... without carrying that wording". NCSC.ch's summary: "Juniper has confirmed malicious exploitation, and CISA has added the flaw to its Known Exploited Vulnerabilities catalog."

### Surface contradiction (F9)
- #8 (low confidence) **Fragnesia** update: "A PAN-OS device that took only the first PHP2Shell hotfix therefore still needs the later one." PAN-SA-2026-0015 FAQ: "If you are running a fixed PAN-OS listed in the CVE-2026-109618 advisory, you are protected ... We still recommend upgrading to a fixed release at your next maintenance interval." The PAN-OS entry carries this framing; the Fragnesia entry omits it.

### Editorial / less-is-more flags (advisory, F11)
- #9 Fragnesia update: "(the builds are in the PAN-OS PHP2Shell entry)" is a cross-entry pointer in reader-facing prose.
- #10 Summary fields far beyond the 1-3 sentence contract: ARTEX 329 words (9 sentences), nginx 211, Zammad 185, PAN-OS 178, Mitel 156.

### Not raised on purpose
- Zammad main analysis at 1,030 words and Fragnesia at 550 (declared in the run record; counts reproduced: 1,030 and 550).
- Two cited pages, the kernel CVE announcement and the linux-nfs patch thread on lore.kernel.org, answer every transport with an Anubis bot challenge (extract, raw, WebFetch 403). The two claims that rest on them (`6c2d56f937`, `cb45aff710`) are marked `unreadable`; their content is confirmed on the CVE.org record (via cveawg.mitre.org), the ENISA EUVD record, OpenSec's timeline (17 Aug 2026 fix posted) and watchTowr. This is a reader convenience limit, disclosed in the entry's sourcing_note, not a defect.
- The run record's coverage-gap list (Znuny ZSA-2026-17 to -43 HTTP 500) is disclosed; the advisories index I could fetch is a 2026-10-21 snapshot ending at ZSA-2026-16 and the individual pages still return HTTP 500, so I cannot evidence an omission.

### Whole-run checks
- Gate-adjacent: evidence quotes added this iteration (PAN-SA-2026-0015 on two entries, the four Zammad report quotes, Mitel, Puppet, ARTEX, Veeam, Ruby, NFS2ROOT, SoftwareOK) are verbatim on their pages; NCSC.ch 13244 "Audit the fleet list for router names your team did not create." is verbatim in the post JSON.
- Update contract (4c): all nine records are `type: update` with a genuine delta, sections end with the matching `## Update` heading, `updated_at` equals each record's `at`, `fields` match the diffs, no silent edits found, no main-analysis statement disproved by a newest section apart from F9 #8.
- Dedup: CVE-2026-99362 and the SoftwareOK/ASEC story have no prior coverage in `prior_coverage.json` or `state/cves_seen.json`; registry keys for both new entries exist; no alias miss found.
- Priority / classification: no miscalibration found (nginx `high` stands on the public Rapid7 PoC for pre-auth RCE in a ubiquitous edge component; NFS2ROOT, SoftwareOK `notable`; classification present on all entries, SoftwareOK single-source B2 consistent).
- Style: no em dash outside headings, no IOCs, no IPs or hashes, no pipeline vocabulary in reader-facing fields; ATT&CK ids checked against the pin (T1685.006 is the active id for the log-clearing behaviour APEX maps to revoked T1070.002).
- Missed angles: two standard-mode searches for in-window (2026-11-26/27) exploited-flaw and Swiss public-sector incidents returned nothing new beyond covered items (Basel-Landschaft, Xen Orchestra and the 2026-11-25 KEV rows are already in the store). Coverage looks complete for critical/high signal.

### Verdict
NEEDS_FIXES (truth: 7, editorial: 1, advisory: 2)

One truth finding is firm (F3 #1, a misattribution the iteration-2 remediation introduced). Six truth findings and the F9 are low confidence and cheap to fix (each is one clause); the advisory items may be left.

### Findings summary (machine-readable)
See `work/2026-11-27T0355Z-intel/verification.iter3.findings.yaml` (10 records).
