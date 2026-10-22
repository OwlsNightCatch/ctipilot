**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-22T09:32:38Z · ended_at=2026-10-22T10:07:40Z · duration_seconds=2102

## Verification report — 2026-10-21T1149Z-audit (iteration 8)

**Scope covered.** Iteration 8 is the cap, a post-fix pass at full scope: all 278 claims of `claims.iter8.yaml` have a verdict row in `verification.iter8.claims.yaml` (274 ok, 1 F3, 1 F4, 2 unreadable); the 3 changed claims (2e3d97554b, 793dbc3f19, 726e8d7205) were re-read first. Every one of the 23 updated entries was read whole with `git diff HEAD`, and its record fields and `updated_at` rule checked. Also read: the run record, the wave report, `work/cleanup/plan.json`, `docs/cleanup/STATUS.md` (not re-rendered), `state/cves_seen.json` (7 `last_seen` and 4 titles match the record), `state/legacy_review.json` (4 entries reviewed, 402 pending), `entities/registry.yaml` (two summaries, five new product keys, eight moved `first_seen` dates all match the earliest naming entry). `check_run.py 2026-10-21T1149Z-audit` re-run: 59 pass, 0 warn, 0 fail. The CISA KEV catalogue, MSRC CVRF (May, June, August) and the MSRC per-CVE API, FIRST's EPSS API, ENISA's EUVD API and NCSC-CH's hub were read for the structured claims; the page-check gate skips migrated entries, so every evidence quote on YellowKey, Nightmare Eclipse, the Pwn2Own roundup, the DEVCORE entry, nginx, LiteLLM, Ghost, Copy Fail, FortiClient and Oracle was matched against its page.

### Prior-iteration deltas (all six confirmed)

- **F14, Pwn2Own roundup, "(new)":** removed. ZDI's announcement says "Last year, we added Artificial Intelligence as a category with great results. This year, we're expanding this and splitting it into multiple different categories: AI Databases, Coding Agents, Local Inferences, and a separate category for NVIDIA products." The entry now says "split its AI category", and the string "(new)" occurs nowhere in the file.
- **F3, takeaway "90 days":** now "vendors have 90 days to patch them", against BleepingComputer 2026-05-15: "Vendors have 90 days to patch their software and hardware after the zero-days are disclosed at Pwn2Own." Correct.
- **F4, wave report Adobe row:** "three pipeline phrases in the sourcing note are reworded". The diff shows exactly three: "what this entry follows" to "what the analysis follows", "and in the run record" removed, "surfaced the bulletin into this window" to "relayed the bulletin". Correct.
- **F4, registry campaign summary:** now "Microsoft's MSRC called uncoordinated disclosure never justifiable on 2026-05-27, and the persona threatened a further release for 14 July 2026". The Record dates the threat to neither side of the statement; the MSRC blog is dated 2026-05-27. Correct.
- **F11, Exchange OWA record summary:** ends "The headline is shortened to the length limit without a change of meaning." Old headline 157 characters, new 116 (the report's figures hold); the recut keeps the exploited-by-a-Russia-aligned-actor, fixed-since-June and foothold-needs-removal content.
- **F11, wave report LiteLLM row:** now "Sysdig observed the first exploitation attempt 36 hours after the advisory reached the global database". Sysdig: "The advisory was indexed in the GitHub Advisory Database on April 24, 2026 ... The timeline is anchored to the global-database publication." Correct.

Declined items re-read, no new evidence, not re-raised: LiteLLM title anchor, FortiClient "rejected" gloss (pre-existing), CCB Belgium (listed below as advisory, same disposition as iterations 4 to 7), roundup kept as routine research, Adobe em dashes (pre-existing, internal record). The nginx EUVD update-date label is not re-raised as a label point; finding #3 below rests on something new (the EUVD API record carries only record-level dates, so "updated CVE description" implies a change nobody read).

### Citation does not support the claim

**F3 #1.** `2026-05-09/cve-2026-40982-spring-cloud-config-server-pre-authentication`, Improvement 2026-10-21T12:08:56Z, claim bfe2478ad2. Quote: "The same post also says an attacker can read or write arbitrary files, and the CVSS vector it gives scores integrity High; Spring's advisory describes only a directory traversal ([Spring, 2026-05-06](https://spring.io/security/cve-2026-40982))". The only citation is Spring's advisory, which reads "A malicious user, or attacker, can send a request using a specially crafted URL that can lead to a directory traversal attack" and carries no read-or-write statement and no vector. Both statements about "the same post" are HeroDevs's ("read or write arbitrary files accessible to the server process"; vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N). The facts are true and the HeroDevs page is already cited in the sentence before and in the main analysis; the citation that ends the sentence just does not carry them. Fix: cite HeroDevs after the first clause.

### Unsupported / hallucinated facts

**F4 #2 (pre-existing, low confidence).** `2026-05-15/cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea`, root-cause sentence (claim c74fdcf820): "expanding `+`, `%` and `&` by two bytes each". depthfirst says the function "expands every escapable character, like a plus sign or ampersand, from one byte to three bytes"; no cited page names "%" (Security Affairs, NCSC-CH, EUVD, the GitHub advisory fetched). The same three characters are in the Detection line. Not changed by this fire beyond the dashes.

**F4 #3 (low confidence).** `docs/audits/2026-10-21-cleanup-wave-03.md`, "State from the records": "(no criminal action was threatened, and the three drops are fixed)". Stated as fact where the sources disagree: The Record "stopped short of directly threatening legal action"; heise "is threatening lawsuits and the police"; BleepingComputer (2026-06-10) "initially reacted to these zero-day leaks with threats of legal action, but backtracked". The corrected summary only stops claiming a threat; reword the parenthetical to "the summary no longer says criminal action was threatened".

### Surface contradiction

**F9 #4 (low confidence).** nginx, Correction 2026-10-21T12:06:51Z opens "Code execution is not limited to hosts with ASLR disabled." The support is conditional: depthfirst "Theoretically, we could leverage this design to leak ASLR", F5 via EUVD "or when the attacker can bypass ASLR". Three pages the entry cites say the opposite: NCSC-CH ("Achieving RCE additionally requires the host system to have Address Space Layout Randomization (ASLR) disabled"), The Hacker News ("code execution is possible only on devices where Address Space Layout Randomization (ASLR) ... is turned off") and Security Affairs ("On systems with ASLR disabled ... remote code execution ... is achievable ... Even where ASLR is enabled, repeated requests can be used to drive workers into a crash loop"). The Contradiction line names only NCSC-CH against F5, and calls F5's text "updated": the EUVD API shows datePublished "May 13, 2026" and dateUpdated "Sep 10, 2026" for the record, not a changed ASLR clause. The record summary words it attributively; the section should too. The upgrade advice stands either way.

### Editorial / less-is-more flags (advisory)

- **F11 #5 (low confidence).** Record summaries that omit a change their `fields` name: CERT-FR (headline also drops "production"), Spring (headline), Dirty Frag (headline), Oracle (headline), Ghost (headline), DEVCORE (title now "one reported to be CVE-2026-62911", was "one later fixed as"), Cisco CVE-2026-20245 (three ATT&CK ids added, headline). Iteration 7 set the standard on the Exchange OWA record; one clause each, or leave as meaning-preserving.
- **F11 #6 (low confidence).** Cisco CVE-2026-20245 Detection lists three script names; they are Cisco's own legitimate CLI scripts published as the log entries to audit, not attacker artefacts. Defensible; listed under style rule 12 so the main agent can leave it.
- **F11 #7 (low confidence).** SimpleHelp claims b3d0654cb8 and 1b7635154c cite only CCB Belgium: extract and url return the 503 maintenance page, jina 503, WebFetch 403; both rows are `unreadable`. No defect asserted: the repair worker's saved copy reads "CVE-2026-48558 CVSS 10 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)" and the NVD record (VulnCheck CNA) gives CVSS 3.1 10.0 for the same vector. The `cves[]` row (67a2cb0628) is ok against NVD and SimpleHelp's guide.

### Checked and clean (no finding)

Every new Improvement, Correction and Update section, every record summary, the frontmatter fields each record names and the two internal records (n8n: all five advisories require "an authenticated user with permission to create or modify workflows" and none describes JavaScript execution, so T1078 in and T1059.007 out is source-supported; Adobe: APSB26-120 lists "ACC v7: 7.4.3 build 9398 and earlier" and APSB26-114's fixed build is 9398, no reader-facing section, `updated_at` untouched). Oracle's advisory revision table reads "2026-May-28 Rev 1. Initial Release", so the 2026-05-28 date and the 30-day gap hold. YellowKey: MSRC revisions 1.2 (script, manual steps removed, 2026-05-21) and 2.0 (June update links, 2026-06-09), CVRF fixed builds and "Exploited: No" for CVE-2026-45585 and CVE-2026-45586 all match; Windows Server 2022 is absent from CVE-2026-45585's table as the entry says. Dirty Frag EPSS values match the FIRST API on both dates. Record, report, tracker and state numbers hold (23 records = 2 updates, 6 corrections, 15 improvements; 366 W1-D defects, 30 of 33 with a 2026-10-11 record, 21 with a record here; 118 unique twin candidates; 581 entries without `updates:` at HEAD; 29/2/7/20 of 58 tracker rows). Two housekeeping items for the main agent, not findings: the run record's `completed` stamp (09:32:13Z) predates this pass and `verification_iterations` stands at 7, so both need the iteration 8 update; the record's CCB note and the report's carried-forward list already name the SimpleHelp and Dirty Frag priority items for the next monthly calibration.

No missed angle found: CVE-2026-50507 (a second BitLocker bypass, publicly disclosed, fixed 2026-06-09) is already covered by two entries and named as a lead in the tracker.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 1, advisory: 3)

The three truth items are one citation placement (add HeroDevs), one dropped character (nginx "%") and one wave-report parenthetical; the editorial item is a sentence of attribution. This is the cap iteration, so the run publishes with whatever the main agent remediates; the remaining items belong in the run record as residuals.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable), iteration 8
- code: F3
  category: claim-not-supported
  section: updated-entry
  item: "2026-05-09/cve-2026-40982-spring-cloud-config-server-pre-authentication, Improvement 2026-10-21T12:08:56Z, second sentence (claim bfe2478ad2)"
  url_or_quote: "The same post also says an attacker can read or write arbitrary files, and the CVSS vector it gives scores integrity High; Spring's advisory describes only a directory traversal ([Spring, 2026-05-06](https://spring.io/security/cve-2026-40982))"
  summary: "The sentence's only citation is Spring's advisory, which says only 'A malicious user, or attacker, can send a request using a specially crafted URL that can lead to a directory traversal attack' and carries no read-or-write statement and no CVSS vector. The two clauses about 'the same post' are HeroDevs's ('read or write arbitrary files accessible to the server process'; vector AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N). The facts are true and sit on the HeroDevs page the entry already cites; add that citation to the first clause."
- code: F4
  category: hallucinated-fact
  section: updated-entry
  item: "(pre-existing, low confidence) 2026-05-15/cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea, main analysis root-cause sentence (claim c74fdcf820)"
  url_or_quote: "expanding `+`, `%` and `&` by two bytes each"
  summary: "(low confidence) depthfirst, the only page that describes the escaping, says the function 'expands every escapable character, like a plus sign or ampersand, from one byte to three bytes'; no cited source names '%' as an expanded character (Security Affairs, NCSC-CH, EUVD and the GitHub advisory do not either). The same three characters recur in the Detection line. Text this fire did not change (only the dashes were removed); drop '%' or cite a source."
- code: F9
  category: surface-contradiction
  section: updated-entry
  item: "2026-05-15/cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea, Correction 2026-10-21T12:06:51Z opening sentence and the Contradiction line"
  url_or_quote: "Code execution is not limited to hosts with ASLR disabled."
  summary: "(low confidence) The section opens with this flat sentence; the sources it rests on are conditional (depthfirst: 'Theoretically, we could leverage this design to leak ASLR'; F5 via EUVD: code execution 'when the attacker can bypass ASLR'), while NCSC-CH ('Achieving RCE additionally requires the host system to have ASLR disabled'), The Hacker News (code execution 'is possible only on devices where ASLR ... is turned off') and Security Affairs, all cited by the entry, say RCE needs ASLR off. The Contradiction line names only NCSC-CH against F5 and calls F5's text 'updated'; the EUVD record shows only datePublished 2026-05-13 and dateUpdated 2026-09-10 at record level, so a change to the ASLR clause is not shown. Attribute the sentence to F5 and add THN and Security Affairs to the Contradiction line; the record summary already words it this way."
- code: F4
  category: hallucinated-fact
  section: wave-report
  item: "(low confidence) docs/audits/2026-10-21-cleanup-wave-03.md, 'State from the records' paragraph"
  url_or_quote: "the summaries of `campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac` (no criminal action was threatened, and the three drops are fixed)"
  summary: "(low confidence) Stated as fact, but the sources disagree and the entry itself shows it: The Record says Microsoft 'stopped short of directly threatening legal action', heise writes the company 'is threatening lawsuits and the police', BleepingComputer says Microsoft 'initially reacted ... with threats of legal action' before backtracking. The corrected registry summary only stops saying a threat was made. Reword to 'the summary no longer says criminal action was threatened'."
- code: F11
  category: editorial-advisory
  section: records
  item: "(low confidence) record summaries of cert-fr, spring, dirty-frag, oracle-ebs, ghost-cms, exchange-devcore and cve-2026-20245 omit changes their `fields` name"
  url_or_quote: "fields: [summary, body, headline] (cert-fr); fields: [body, headline] (spring); fields: [headline, sources, body] (oracle); fields: [headline, techniques, actions, body] (cve-2026-20245)"
  summary: "(low confidence) Iteration 7's standard was that a record summary says when the headline is recut. CERT-FR's recut also drops the word 'production' (old: 'off production workstations'), the DEVCORE title moves from 'one later fixed as CVE-2026-62911' to 'one reported to be CVE-2026-62911', and the Cisco CVE-2026-20245 record names `techniques` (three ATT&CK ids added) without saying so. Add one clause to each, or leave as meaning-preserving."
- code: F11
  category: editorial-advisory
  section: updated-entry
  item: "(low confidence) 2026-06-06/cve-2026-20245-cisco-catalyst-sd-wan-manager-actively-exploi, Detection"
  url_or_quote: "`vconfd_script_upload_tenant_list.sh`, `vconfd_script_upload_vsmart_serial_numbers.sh` and `vconfd_script_upload_chassis_number_file.sh`"
  summary: "(low confidence) Style rule 12 bars file-name indicators. These are Cisco's own legitimate CLI scripts, published in Cisco's advisory as the log entries to audit ('These are legitimate commands, and the logs will not distinguish between legitimate and malicious use'), not attacker-created artefacts, so this is defensible; listed so the main agent can leave it."
- code: F11
  category: editorial-advisory
  section: updated-entry
  item: "(low confidence) 2026-06-30/cve-2026-48558-simplehelp-rmm-oidc-sso-authentication-bypass, claims b3d0654cb8 and 1b7635154c"
  url_or_quote: "CVE-2026-48558, scored CVSS 3.1 10.0 ([CCB Belgium, 2026-06-19](https://ccb.belgium.be/advisories/warning-simplehelp-patched-cve-2026-48558-critical-authentication-bypass-vulnerability))"
  summary: "(low confidence) Two claims cite only CCB Belgium, unreadable live this iteration (extract and url: 503 maintenance page; jina: 503; WebFetch: 403). No defect asserted: the repair worker's saved copy of 2026-10-21 reads 'CVE-2026-48558 CVSS 10 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)', and the NVD record (VulnCheck CNA) gives CVSS 3.1 10.0 for the same vector."
```
