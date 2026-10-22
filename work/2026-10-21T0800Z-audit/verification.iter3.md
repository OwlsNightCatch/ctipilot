**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-21T10:08:28Z · ended_at=2026-10-21T10:47:06Z · duration_seconds=2318

(My own first command printed 10:08:28Z. `work/2026-10-21T0800Z-audit/verify.iter3.started_at` now reads 10:14:00Z, rewritten after I wrote it; `verify.iter3.ended_at` is mine, 10:47:06Z. Use one pair in the run record.)

## Verification report — 2026-10-21T0800Z-audit (iteration 3)

Scope walked: all 187 claims of `claims.iter3.scope.yaml` (the 8 changed since iteration 2, every claim of the 5 remediated entries, and the seeded quarter of the rest), each against a page fetched this pass (89 distinct pages; ENISA EUVD through its API, CISA KEV through the bridge, Pixel bulletin through WebFetch), plus the run record, `docs/audits/2026-10-21-cleanup-wave-02.md` and `docs/cleanup/STATUS.md` against disk. The gate (`check_run.py 2026-10-21T0800Z-audit`) re-run this pass: 60 pass · 1 warn · 0 fail, exit 0; the one WARN is the Pixel quote-literal transport gap (see below). Claim rows: 185 ok, 2 F3 (`verification.iter3.claims.yaml`).

### Prior-iteration deltas (iteration 2, eight findings) — all remediations checked against the cited page

| Iteration 2 finding | Remediation read this pass | Result |
|---|---|---|
| Conference phishing: body, 2026-10-21 section and record still attribute the ranking to "a Huntress researcher" (F3) | Huntress recap (2026-09-15): "Jon deemed the second payload the most interesting", byline "Huntress SOC Analysts Ryan Dowd and Jon Semon"; the "second payload" is `Localcertificate.zip`, the TLS-intercepting proxy. Body, section and record now name Huntress SOC analyst Jon Semon. | Correct. Residual ambiguity elsewhere in the same entry (F11 #7). |
| Report Records table lacked `sources` on two rows (F4) | Table regenerated: all 72 rows compared with the 72 on-disk `updates[]` records of this run (type, internal flag, fields): 0 mismatches; 61 improvements (18 internal) and 11 corrections (1 internal) match the Verdict line; batch column and W1-B/W1-C/W1-E/W1-F tags reconcile (50 / 5 / 19 / 8). | Correct. |
| STATUS "Now" cell said 996 (F4) | STATUS.md and plan.json read 1002; `check_run.py --all` store-parse count and inventory agree (iteration 2); tracker rows done/declined/open 29 / 2 / 18 of 49 recounted from the table; out-of-week verdicts 61 / 6 / 37 follow from 77 / 63 / 42 minus 16, 57 and 5. | Correct. |
| ShieldBreak record summary rested on an unreadable Wayback copy (F11) | Record now says only that the 2026-08-21 and 2026-09-13 updates "no longer read MSRC's temporal CVSS metrics as recording the fix". The run's own 2026-08-18 raw capture (`work/2026-08-18T0410Z-intel/raw/msrc-69414.json`) already carries `E:P/RL:O/RC:C` and the "We are working to provide a high quality security update" sentence, so the removed sentences were wrong and the removal is right. | Correct. |
| Exchange 2026-10-16 section cites a post that did not exist at its timestamp (F11) | Release post changelog: "October 16 ... Updated the banner to link to a post ..." and "October 15 ... Added a banner mentioning that October 2026 Windows Server updates might create issues ... (no installation of October 2026 Exchange SU updates is required)". The dedicated post (postTime 2026-10-16T18:00:38-07:00) carries the KB list, MapiExceptionMdbOffline, event ID 1006, queues and the `EpmapSavedContextCap` workaround. 2026-10-16 section now cites only what the release post carries; the 2026-10-21 section carries the dedicated post. | Correct. |
| SAP actions[1] over-stated "remains exploitable regardless of patch status" (F11) | Reworded to "Onapsis requires the property after the patch so that only XSL files from the listed hosts can be consumed", which is Onapsis's sentence. | Correct for actions[1]; same inference still stands in `cves[CVE-2026-44772].fixed` and the 2026-08-28 section (F11 #6). |
| Sophos Triage discriminator unlabelled (F11) | Now "by inference from Malwarebytes' sandbox observation". | Label added; label itself slightly inexact (F11 #5). |
| SAP "in this entry" (F11) | "in this advisory round". | Correct. |

### Citation does not support the claim (F3)

1. **2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access, body (Detection), claim 9113eebf7e, text added this fire.** "Watch for SSH authentication attempts with the `psoft`/`oracle`/`linuxadm` account names or other administrative accounts that originate from a PeopleSoft server toward other internal PeopleSoft hosts: the recovered script sprays SSH credentials at the internal hosts named in the compromised server's `/etc/hosts` ... ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/))". The GTIG page prints the script's list as `USERS="[redacted_usernames]"` and says only "a hardcoded list of common administrative and application-specific usernames"; neither GTIG article (06-12 and 09-26) contains `psoft`, `oracle` or `linuxadm`. The three names are BleepingComputer's: "common PeopleSoft and Oracle administrative accounts such as 'psoft', 'oracle', and 'linuxadm'" (https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/, 2026-06-10, already a source of the entry). The old sentence carried no citation; this fire's rewrite attached GTIG to a clause that includes the names. Cite BleepingComputer for the account names (or drop them).
2. **(low confidence) 2026-06-30/cve-2026-8037-progress-kemp-loadmaster-pre-auth-rce-via-unin, section 2026-09-30T06:43:48Z, claim 7cb1674236.** "the 9.8 score is ZDI's, while Progress's CVE record gives 9.6 ([ENISA EUVD]), the score eSentire reports ([The Hacker News] · [eSentire TRU])". THN carries "a CVSS score of 9.8 according to ZDI" and nothing on eSentire; eSentire's own page carries "(CVSS: 9.6)". Let THN terminate the ZDI clause and eSentire alone the 9.6 clause.

### Surface contradiction (F9)

3. **(low confidence) 2026-09-24/openai-agent-australia-medicare-portal-breach, section 2026-10-21T08:20:00Z vs the main analysis, claim 9644f27d61.** New section: "That the accessed information included aggregate health statistics and internal file names is OpenAI's statement, not part of Albanese's account ([CNN Business, 2026-09-23])". CNN, ABC and The Record's first article attribute "aggregate health statistics and internal file names" to OpenAI, but The Record's 2026-09-25 article, cited in the same section and in the body, writes "The "internal file names" he mentioned" (he = Albanese), and the main analysis still says: 'the "internal file names" Prime Minister Albanese cited as evidence of unauthorized access were potentially exposed by the same JavaScript file'. The negative "not part of Albanese's account" is carried by none of the cited pages. Add a Contradiction line or reconcile body and section.
4. **(low confidence, pre-existing) 2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix, sections 2026-08-21T06:20:00Z and 2026-08-24T09:11:00Z.** 08-21: "The highest-value single signal is a module load: Defender's management library being loaded by a process outside the small, stable set of Defender's own binaries" and takeaway "not on the exploit's filenames"; 08-24: "LevelBlue identifies `C:\Windows\System32\phoneinfo.dll` as the strongest single indicator in the chain". LevelBlue's page lists "Signal 1: phoneinfo.dll Created in System32 ... the strongest unconditional detection point" and Signal 2 (MpClient.dll load) second, and its IOC note calls phoneinfo.dll creation variant-independent. Two rankings sit unreconciled; not touched this fire.

### Editorial / less-is-more flags (advisory, F11)

5. **(low confidence) 2026-05-10/sophos-beagle..., body (Triage), claim 2c8bd25d2f.** "by inference from Malwarebytes' sandbox observation, the discriminator is the sequence, in which WScript.exe writes the updater, the DLL ... and an encrypted data file ... and starts the updater with a hidden window while the freshly installed Claude application opens in the foreground". Malwarebytes' sandbox section observed only "WScript.exe was observed dropping NOVUpdate.exe and avk.dll into the Startup folder"; the third file, the hidden window (window style 0) and the real app in the foreground come from its "Static analysis of the dropper script". Say "sandbox and static analysis".
6. **(low confidence, pre-existing) 2026-08-12/sap-august..., `cves[CVE-2026-44772].fixed` and section 2026-08-28T05:00:00Z.** "... or the servlet remains reachable" and "has left the vulnerable servlet reachable: the patch alone does not close the flaw for this note". Onapsis says only "After implementing the patch, customers need to maintain the new system property 'Secure Transformer' ... Only XSL files from these hosts can be consumed by the vulnerable servlet"; what an unconfigured property allows is the entry's inference. Iteration 2 asked for this softening; only actions[1] was changed.
7. **(low confidence) 2026-09-21/conference-phishing..., body and record 2026-10-21T08:11:55Z.** "A Huntress researcher named crypto-wallet domains and antivirus update signals as targets the operator could intercept" (also the 2026-09-30 correction): the recap gives that remark to Jon, a SOC analyst, while the entry opens with "A Huntress researcher was targeted", the ambiguity iterations 1 and 2 removed elsewhere. Also the record summary says "The summary and analysis ... attribute the judgement to Huntress SOC analyst Jon Semon" while the summary field says "Huntress's recap calls the most interesting" and does not name him.
8. **Run record `runs/2026-10-21/2026-10-21T0800Z-audit.md`.** verification.iterations[1]: started_at 09:21:17Z, ended_at 10:05:16Z, duration_seconds 2536; the interval is 2639 s (the verifier's own timestamp file says 09:23:00Z, which gives 2536). The Verification paragraph of the notes ("The Phase 5.7 loop is in progress: iteration 1 runs as two slices over the 541 claims of the ledger.") is stale at iteration 3; it and the report's and tracker's placeholders get the loop summary when the loop ends. `budget.tsv` lists verify-3 spawned at 10:14:00Z.

### Checked and holding (run record, report, tracker, state, tools)

- Run record: 72 `updated_entry_ids` equal the 72 on-disk records of this run; sub-agent start/end/duration arithmetic holds for repair-1 to repair-6 and iteration 1; token total 2,232,689 matches "about 2.23 M" and `budget.tsv`; iteration-1 and -2 finding lists and counts equal the verifier files; commit ids `731706f`, `1f8d69e`, `ea6e509` exist with the stated content; 72 of 85 entries with a record, 13 without, equal the report's "Entries without a record" table (6 + 7 entries).
- `state/cves_seen.json` diff: CVE-2026-92438 added, 33 `last_seen` moves (34 lines at 2026-10-21 include the new record), four titles (CVE-2026-44772, CVE-2026-73570, CVE-2026-58704, CVE-2026-33691) as the report says. `entities/registry.yaml`: four product records, LiteLLM `first_seen` 2026-06-09 and the FTAPI summary as stated. `state/legacy_review.json`: 18 entries under this run id (13 W1-B + 5 W1-C, 406 to 388). `work/cleanup/wave-03/findings-W1-I.md` holds 45 residual items; the Pixel WebFetch file exists.
- Pixel CVE-2026-58704: WebFetch of the live bulletin (published 2026-09-15, last updated 2026-09-30) returns "There are indications that CVE-2026-58704 may be under limited, targeted exploitation." in the Announcements section; the WARN is a transport gap, not a quote defect. Patch level 2026-09-05, KEV 2026-09-16, EUVD "remote (proximal/adjacent) escalation of privilege ... User interaction is not needed" support the summary.
- Liechtenstein: the six German originals added this fire are verbatim on presseportal pages 100941487, 100941500 and 100941523 and the translations are faithful.
- Unreadable from my transports and verified on the workers' saved copies (stated in the claim rows): cyber.gov.au ACSC alert (403/503; `repair-5/src/e14-acsc.md`, date 2026-09-25), The Register Citrix article (nav-only extract; `repair-6/src/citrix-register.txt`), Citrix techzone blog (403; `repair-6/src/citrix-blog.md`), Cisco Live Protect "Updated: September 22, 2026" (raw HTML plus worker copy).
- Not verified: the report's statement that W7-14 lists 14 sentences on wave 01's record (running the ledger on wave 01 would overwrite that run's artifacts).

### Observations, not findings

- Exchange 2026-10-14: the dedicated Microsoft post was updated on 2026-10-20 with an FAQ ("install already released Windows updates as soon as possible", "no imminent follow-up release from either Windows or Exchange", raising the limit above 65536 not seen as required). Nothing in the entry contradicts it; a next intel pass may carry it as an update. No audit defect.
- Coverage: the audit ran no re-sweep and no new entries; no missed-angle finding raised.
- Pentagon DMDC (routine, short body, transferable encryption lesson) and Arista VeloCloud (critical, exploited, KEV, two trains unfixed, July flaw's four trains match THN's table) hold their priorities on the sources read.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 2, advisory: 4)

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: body (Detection)
  item: "2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access (claim 9113eebf7e, added this fire)"
  url_or_quote: "Watch for SSH authentication attempts with the `psoft`/`oracle`/`linuxadm` account names or other administrative accounts that originate from a PeopleSoft server toward other internal PeopleSoft hosts: the recovered script sprays SSH credentials ... ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/))"
  summary: "The GTIG page shows the fan-out script's list as USERS=\"[redacted_usernames]\" and says only 'a hardcoded list of common administrative and application-specific usernames'; neither GTIG article (06-12, 09-26) contains psoft, oracle or linuxadm. The three names are BleepingComputer's (https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/, 2026-06-10: 'common PeopleSoft and Oracle administrative accounts such as psoft, oracle, and linuxadm'). This fire added the GTIG citation to the clause (the old sentence carried none). Cite BleepingComputer for the account names or drop the names."
- code: F3
  category: claim-not-supported
  section: section 2026-09-30T06:43:48Z
  item: "2026-06-30/cve-2026-8037-progress-kemp-loadmaster-pre-auth-rce-via-unin (claim 7cb1674236)"
  url_or_quote: "the 9.8 score is ZDI's, while Progress's CVE record gives 9.6 ([ENISA EUVD]), the score eSentire reports ([The Hacker News, 2026-06-30](https://thehackernews.com/2026/06/progress-kemp-loadmaster-flaw-could-let.html) · [eSentire TRU, 2026-06-30](...))"
  summary: "(low confidence) THN sits beside 'the score eSentire reports' but carries only 'a CVSS score of 9.8 according to ZDI'; the eSentire figure (CVSS 9.6) is on the co-cited eSentire page. Split the pair so THN terminates the ZDI 9.8 clause and eSentire alone terminates the 9.6 clause."
- code: F9
  category: surface-contradiction
  section: body vs section 2026-10-21T08:20:00Z
  item: "2026-09-24/openai-agent-australia-medicare-portal-breach (claim 9644f27d61)"
  url_or_quote: "section: 'That the accessed information included aggregate health statistics and internal file names is OpenAI's statement, not part of Albanese's account ([CNN Business])' vs body line: 'the \"internal file names\" Prime Minister Albanese cited as evidence of unauthorized access were potentially exposed by the same JavaScript file'"
  summary: "(low confidence) CNN, ABC and The Record's first article attribute 'aggregate health statistics and internal file names' to OpenAI, but The Record's 2026-09-25 article (cited in the same section and body) writes 'The \"internal file names\" he mentioned' of Albanese, and the entry's main analysis still says Albanese cited them. The new section's negative ('not part of Albanese's account') is carried by none of the cited pages and contradicts the body. Add a Contradiction line or reconcile body and section."
- code: F9
  category: surface-contradiction
  section: sections 2026-08-21T06:20:00Z and 2026-08-24T09:11:00Z
  item: "2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix (pre-existing)"
  url_or_quote: "08-21: 'The highest-value single signal is a module load: Defender's management library being loaded by a process outside the small, stable set ...' and takeaway 'not on the exploit's filenames' vs 08-24: 'LevelBlue identifies phoneinfo.dll as the strongest single indicator in the chain'"
  summary: "(low confidence, pre-existing, not changed this fire) LevelBlue ranks Signal 1 'phoneinfo.dll Created in System32' as 'the strongest unconditional detection point' and Signal 2 (MpClient.dll load) as a strong signal; its IOC note calls phoneinfo.dll creation and MpClient.dll loading variant-independent. The 08-21 section's own ranking and 'not on filenames' advice stand beside the 08-24 section without reconciliation."
- code: F11
  category: editorial-advisory
  section: body (Triage)
  item: "2026-05-10/sophos-beagle-backdoor-distributed-via-fake-claude-ai-site-u (claim 2c8bd25d2f)"
  url_or_quote: "by inference from Malwarebytes' sandbox observation, the discriminator is the sequence, in which WScript.exe writes the updater, the DLL it loads from its own directory and an encrypted data file into a user's Startup folder and starts the updater with a hidden window while the freshly installed Claude application opens in the foreground"
  summary: "(low confidence) Malwarebytes' sandbox section observed only 'WScript.exe was observed dropping NOVUpdate.exe and avk.dll into the Startup folder'; the third file, the hidden window (window style 0) and the real app in the foreground come from its 'Static analysis of the dropper script'. Say 'Malwarebytes' sandbox and static analysis' or 'dropper analysis'."
- code: F11
  category: editorial-advisory
  section: cves[CVE-2026-44772].fixed, section 2026-08-28T05:00:00Z
  item: "2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce (pre-existing, claims 7b1e4af421 and 37786fe8ed)"
  url_or_quote: "'... customers must additionally configure and maintain the new \"Secure Transformer\" system property ..., or the servlet remains reachable'; 'has left the vulnerable servlet reachable: the patch alone does not close the flaw for this note'"
  summary: "(low confidence, pre-existing) Onapsis says only 'After implementing the patch, customers need to maintain the new system property ... Only XSL files from these hosts can be consumed by the vulnerable servlet'; it does not say what an unconfigured property allows. Iteration 2 asked for this inference to be softened; only actions[1] was. Soften both to 'Onapsis requires the property after the patch'."
- code: F11
  category: editorial-advisory
  section: body and record 2026-10-21T08:11:55Z
  item: "2026-09-21/conference-phishing-rogue-root-ca-mitm-persistence (pre-existing wording, claim ba7220b3cb)"
  url_or_quote: "'A Huntress researcher named crypto-wallet domains and antivirus update signals as targets the operator could intercept the same way' (also the 2026-09-30 correction); record: 'The summary and analysis ... attribute the judgement to Huntress SOC analyst Jon Semon'"
  summary: "(low confidence) The recap attributes the wallet and antivirus-update remark to Jon, a Huntress SOC analyst, but the entry opens with 'A Huntress researcher was targeted', the same two-person ambiguity iterations 1 and 2 removed elsewhere; name him. The record summary also says the summary attributes the ranking to Jon Semon, while the summary field says only 'Huntress's recap calls the most interesting'."
- code: F11
  category: editorial-advisory
  section: run record verification.iterations[1] and verification notes
  item: "runs/2026-10-21/2026-10-21T0800Z-audit.md"
  url_or_quote: "iteration 2: started_at 2026-10-21T09:21:17Z, ended_at 2026-10-21T10:05:16Z, duration_seconds: 2536; notes: 'The Phase 5.7 loop is in progress: iteration 1 runs as two slices over the 541 claims of the ledger.'"
  summary: "09:21:17 to 10:05:16 is 2639 s, not 2536 (the verifier's own timestamp file, work/.../verify.iter2.started_at, says 09:23:00, which gives 2536; use one pair). The Verification note is stale at iteration 3 and should be rewritten with the loop summary when the loop ends (expected placeholder). budget.tsv lists verify-3 spawned at 10:14:00Z while its started_at stamp is 10:08:28Z; use the stamps."
```
