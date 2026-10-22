# Repair worker repair-4: batch 4 report (2026-10-21T0800Z-audit)

16 entries. 14 records written (2 correction, 12 improvement: 8 with a section, 4 internal). 0 `update` records. 2 entries without a record (MikroTik, Acronis). No entry in this batch carried `legacy_duty: true`, so no legacy duties were owed. No W1-F drafts covered these entries. Fetched bodies, helper scripts and record texts are under `work/2026-10-21T0800Z-audit/repair-4/` (`src/`, `rec/`).

## Per entry

### 1. 2026-08-10/coding-agent-ci-harness-trust-boundary-shared-checkout
- Record: improvement, at 2026-10-21T08:08:35Z, fields actions, body, evidence, summary, title.
- Applied (W1-B, CVE binding): the body and summary now say what Google's advisory (OSV alias CVE-2026-12537) covers: headless mode auto-trusting the workspace folder (RCE through environment variables in the local `.gemini/` directory) and the tool allowlist ignored under `--yolo`. A sentence states that the advisory does not describe Novee's parent-process environment read, which Novee chains with a shell allowlist never enforced at runtime. Ground truth: https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g and https://api.osv.dev/v1/vulns/GHSA-wpqr-6v78-jr5g. Novee: https://novee.security/blog/critical-flaws-in-anthropic-google-and-openais-coding-agents/. Three new evidence rows, all `grep -F` literal.
- Em dashes removed from the title, summary (2), actions[0] and body (4). Kept: the two inside Anthropic's verbatim GHSA quote.
- Not cited: the CNA record's title and CVSS 4.0 vector (CVE record only).

### 2. 2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce
- Record: improvement, at 2026-10-21T08:10:17Z, fields actions, body, cves.
- Applied (carried W1-E item 2, labelled lines that had been left for the next record): added **Exposure:**, **Detection:** and **Defender takeaway:** lines. Paragraph 4's detection prose moved into the Detection line instead of being repeated. The Detection line adds a post-redeploy compromise check: review access logs from 2026-08-14 (first honeypot attempts) up to the redeploy. Triage was omitted because the only discriminator (the integration-source baseline) is analyst judgement, not sourced. Sources: https://support.sap.com/en/my-support/knowledge-base/security-notes-news/august-2026.html, https://onapsis.com/blog/sap-security-patch-day-august-2026/ and https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/.
- Em dashes removed from actions[1], cves[CVE-2026-44772].fixed and body (2, in the 08-16 and 08-28 sections).

### 3. 2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix
- Record: correction, at 2026-10-21T08:11:58Z, fields body, cves, evidence, headline, title.
- Applied (carried W1-E item 10): the item had been declined as "dated context", but the text is a reader-facing error. The 2026-08-18 section called a process tree rooted at the engine "the durable anchor", and its **Triage:** claim was uncited. LevelBlue shows the SYSTEM stage runs under wermgr.exe via the QueueReporting task. The paragraph now says this, cites LevelBlue and points to the 2026-08-24 detection sequence; the uncited Triage claim is gone. The disclosure-day paragraph's matching premise ("SYSTEM process spawned by an engine") is replaced by a pointer to the same update. Ground truth: https://www.levelblue.com/blogs/spiderlabs-blog/cloud-sync-root-registrationshieldbreak-hunting-windows-defender-remediation-abuse-and-cloud-files-hijacking (quote literal, added to evidence).
- Em dashes removed from the title, headline, cves[CVE-2026-50656].fixed and body (46). Kept: the publisher names and the earlier record summaries.

### 4. 2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited
- Record: improvement, internal, at 2026-10-21T08:12:17Z, fields cves, sourcing_note.
- Applied (W1-B): EPSS changed from 0.11736 to 0.71663, FIRST's score for 2026-10-20 (it rose on 2026-10-06). The sourcing note's date now reads 2026-10-20. The body never states EPSS, so the record is internal. Ground truth: https://api.first.org/data/v1/epss?cve=CVE-2026-73570 (time series saved).

### 5. 2026-08-29/exchange-mrsproxy-auth-bypass-cve-2026-62911-poc
- Record: improvement, at 2026-10-21T08:14:17Z, fields actions, body, cves, sourcing_note, title.
- Applied (carried W1-E item 8, earlier declined as style): beyond its length, the note contained composition-rationale narration ("The pre-auth rating follows the weight of…", "see body"), a reader-facing defect the style rules fix by deletion. It is now two provenance sentences, re-verified against the MSRC record (`msrc cve`: PR:L/UI:R, "authorized attacker"), Franky's Web ("does not need valid credentials"), the CERT-Bund post, the NCSC-NL CSAF and MB VRED ("most plausible hypothesis").
- The section gives a dated delta: as of 2026-10-21, MSRC has no revision after 2026-08-11, exploitation is "No" and the rating is "Exploitation Less Likely". The body's "as of this writing" now reads "as of 2026-08-29". CVE-2026-62911 is not in KEV (catalogue of 2026-10-20).
- Em dashes removed from the title, actions[0], cves fixed and body (15). A sectioned record was needed because the punctuation edits exceed the 12-word internal limit.

### 6. 2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection
- Record: improvement, internal, at 2026-10-21T08:14:57Z, fields summary.
- Applied (carried W1-E item 13): deleted the summary clause "no fix exists short of upgrading". It is tautological, and it implies there is no workaround, which no cited outlet says for SNWLID-2026-0016. The Hacker News's "No workaround is listed" refers to the October advisory, SNWLID-2026-0017. Checked: https://www.securityweek.com/sonicwall-warns-of-two-sma1000-zero-days-exploited-in-attacks/, both BleepingComputer articles and https://thehackernews.com/2026/10/sonicwall-patches-cvss-100-pre.html. The SonicWall PSIRT page was unreadable (JS shell, also via WebFetch), so the record summary claims only what the outlets show.

### 7. 2026-09-06/mikrotik-routeros-mikrotrick-ssh-auth-bypass-privesc-chain: no record
- Declined W1-E item 0: "frontmatter" appears only in the 2026-09-11 `updates[]` record summary, which is append-only. No other finding applies, and em dashes alone never justify a record.

### 8. 2026-09-10/sap-september-2026-overpass-s4get-preauth-rce
- Record: improvement, internal, at 2026-10-21T08:16:00Z, fields body, cves, sources, title.
- Applied (W1-B, dates): both Onapsis posts are now dated 2026-09-08 in sources[0..1] and in the 7 inline citations. JSON-LD datePublished is 2026-09-08T08:57:42Z / 08:57:01Z, and the visible date is "September 8, 2026". Ground truth: https://onapsis.com/blog/sap-overpass-remediation/ and https://onapsis.com/blog/s4get-cve-2026-58240-sap-message-server-threat-advisory/. Simulated internal word delta: 2.
- Declined, already fixed by 2026-10-11T1307Z-audit: the headline ("maximum-severity") and the Exposure-line scope (OVERPASS 7.22 to 9.20 and WEBDISP; the 9.16 to 9.20 patch levels are labelled as S4GET's).
- Em dashes removed from the title, cves[CVE-2026-58240].fixed and body (1).

### 9. 2026-09-12/jfrog-artifactory-cve-2026-42016-42018-token-chain-takeover
- Record: improvement, at 2026-10-21T08:18:09Z, fields actions, body, cves, evidence, headline, immediate_action, sources, sourcing_note, summary, title.
- Applied (all 5 W1-B findings):
  - (a) Restored cvss: 8.1 for CVE-2026-42016 (EUVD-2026-49566) and 7.5 for CVE-2026-42018 (EUVD-2026-57388), both with assigner JFROG. Cited to the ENISA EUVD pages (two new sources[] records), not the CVE record. JFrog's advisory page still shows only "High" (re-read: https://docs.jfrog.com/releases/docs/jfrog-security-advisories).
  - (b) In the 2026-09-30 Correction section, the sentence about the "8.1 and 7.5 figures… no longer shown" now attributes the scores to JFrog's CNA records.
  - (c) Sourcing note: BSI's WID-SEC-2026-2808 lists CVE-2026-42018 (not 42016), and its revision of 2026-09-10 recorded an exploit for both CVEs and CVE-2026-82329. It says nothing about KEV. Ground truth: `bsi-csaf WID-SEC-2026-2808`.
  - (d) Headline: dropped "dormant".
  - (e) immediate_action and actions[1]: "within minutes" now reads "shortly afterwards (in some cases an admin account within five minutes of the first request)". Wiz's sentence was added as evidence (literal): https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201.
- Also: EPSS refreshed to FIRST's 2026-10-20 scores (0.0864 and 0.0981; were 0.0027 and 0.0035). Em dashes removed from the title, summary (2) and immediate_action.title.

### 10. 2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware
- Record: correction, at 2026-10-21T08:18:41Z, fields body, evidence, title.
- Applied (W1-B): the 2026-09-30 Correction now says NCSC lists wiping the computer system among the bot-taskable functions and separately notes data-wiping in at least one sample. The body's "full disk wipe" now reads "wiping the computer system". Ground truth: https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists ("Wipe the computer system (T1485)", added to evidence, literal). Em dash removed from the title.

### 11. 2026-09-17/cve-2026-58704-google-pixel-modem-zero-click-eop
- Record: improvement, at 2026-10-21T08:21:17Z, fields body, cves, evidence, headline, sources, sourcing_note, summary.
- Applied (W1-B 1): Google's bulletin is cited directly for "There are indications that CVE-2026-58704 may be under limited, targeted exploitation". TechCrunch's "was exploited" opening is noted as stronger than Google's wording. The "Google did not confirm" / "only unhedged signal" framing is dropped from the body, the 2026-09-30 Correction section, the headline and the summary. Read via WebFetch only (the extract/jina text drops the Note, and the direct GET returns 302); the verbatim text is saved at `repair-4/src/e11-pixel-webfetch.txt`. Source: https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01.
- Applied (W1-B 2): cvss 8.8 (CVSS3.1, AV:A) and the "remote (proximal/adjacent)" description are cited to https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-79004 (new sources[] record). The scorer is not attributed beyond EUVD; the CVE record is not citable. The summary now says "proximal or adjacent attacker". EPSS is 0.0059 (FIRST, 2026-10-20). `vector` stays zero-click, since the taxonomy has no adjacent value.
- Declined: editing the 2026-09-30 `updates[]` record summary (append-only).

### 12. 2026-09-17/cve-2026-76460-cisco-ise-auth-bypass-root-rce
- Record: improvement, at 2026-10-21T08:22:06Z, fields body, cves, immediate_action, summary.
- Applied (W1-B 1): "every release" now reads "ISE and ISE-PIC releases before the fixed patch levels, regardless of device configuration", in the summary and body paragraphs 1 and 2. Ground truth: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5 and cisco-sa-ise-multi-hrP9jQSQ.
- Applied (W1-B 2): the takeaway keeps the command shape (`show logging application ise-kong/access.log`) and Cisco's "suspicious usernames" wording, without the literal example username.
- Declined (W1-B 3): the 2026-09-18 `updates[]` summary is append-only. The 2026-09-30 Correction section already supersedes it.
- Em dashes removed from cves[76423].fixed, cves[20130/20192].affected, body (2) and immediate_action.action.

### 13. 2026-09-17/ddrop-dram-interposer-defeats-confidential-computing
- Record: improvement, internal, at 2026-10-21T08:22:25Z, fields body, sources.
- Applied (W1-B): AMD-SB-3048 is now dated 2026-09-14 (revision table "2026-09-14 | Initial version"; 2026-09-15 is only og:updated_time) in sources[] and the 2 inline citations. Ground truth: https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3048.html.

### 14. 2026-09-18/brevo-cloudflare-worker-clickfix-supply-chain
- Record: improvement, at 2026-10-21T08:23:25Z, fields actions, body, summary.
- Applied (W1-B 1): the ClickFix window is 16:07 to 20:30 UTC per Brevo ("The ClickFix was active on following URLs from 16:07 UTC until 20:30"). Sansec observed 16:05 to 20:13, and BleepingComputer gives 16:07 to 20:30. The Worker's impact window (15:01 to 20:30) is now stated separately in the Exposure line, paragraph 1 and the summary, which also conflated the two. Ground truth: https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up, https://sansec.io/research/brevo-supply-chain-attack, and the BleepingComputer article.
- Applied (W1-B 2): the plugin display name is removed from actions[0], paragraph 1, the Triage line and the 2026-09-30 Correction. The behavioural description stays (it hides from the plugin list and copies itself into mu-plugins, per BleepingComputer).

### 15. 2026-09-18/cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev: no record
- Declined W1-E item 22 (JSON API source): the human-readable page both outlets link (https://security-advisory.acronis.com/advisories/SEC-10986) is a JS shell with none of the cited text, while the JSON record carries all of it (products, builds, the exploitation sentence). Swapping would cite an unreadable page.
- Declined W1-E item 23 (em dashes): already fixed. No em dash remains in the title (rewritten by 2026-10-11T1307Z-audit / 2026-10-20T0835Z-audit).

### 16. 2026-09-18/cve-2026-91843-check-point-security-mgmt-stack-overflow
- Record: improvement, at 2026-10-21T08:25:29Z, fields actions, body, cves, sourcing_note, title.
- Applied (W1-B): added the R82.20 Jumbo Hotfix route (Take 10) to cves.fixed, body paragraph 2, the 2026-09-30 Correction and actions[0]. actions[0] also names the R82.20 Security Hotfix as the separate CVE-2026-93616 fix. Ground truth: the sk1000155 and sk1000171 `__NEXT_DATA__` solution text ("Jumbo Hotfix Accumulator for R82.20 starting from Take 10"; "These Jumbo Hotfix Accumulators also include the fix for CVE-2026-91843"). Pages: https://support.checkpoint.com/results/sk/sk1000155 and https://support.checkpoint.com/results/sk/sk1000171/; WebFetch returned an empty body.
- Em dashes removed from the title and sourcing_note (2).

## Checks run
- `check_run.py --all`: no FAIL on any batch-4 entry. Only the expected "run_id does not resolve to a run record" WARNs. The one store FAIL (cve-sync CVE-2026-92438, Ninja Forms entry) belongs to another batch.
- Page checks (`repair-4/page-checks.txt`): one quote-literal WARN on my entries, the Pixel evidence row "There are indications that CVE-2026-58704 may be under limited, targeted exploitation." This is a transport gap, not a non-verbatim quote: the cached extract keeps only the Announcements bullet and drops Google's Note, and the direct GET returns 302. WebFetch returned the sentence verbatim. Kept for the verifier to confirm by hand. citation-cve: no lines for my entries.
- Simulated the run-scope `changelog-fields` internal-word limit (max 2 words on internal records) and the inline-citation in-sources/date rules: all pass. The run-scoped gate itself needs the run record.

## State changes for the main agent
- `entities/registry.yaml`: none.
- `state/cves_seen.json`: set last_seen 2026-10-21 on the CVE records this run changed: CVE-2026-73570 (epss), CVE-2026-42016 and CVE-2026-42018 (cvss, epss), CVE-2026-58704 (cvss, epss), CVE-2026-91843 (fixed: R82.20 Take 10), CVE-2026-44772, CVE-2026-50656, CVE-2026-62911, CVE-2026-58240, CVE-2026-76423, CVE-2026-20130 and CVE-2026-20192 (em-dash punctuation in fixed/affected only).
- Suggested `cves_seen` title fixes, since the titles contradict the entries:
  - CVE-2026-44772 still says "the patch removes the vulnerable servlet component" (wrong since the 2026-08-28 correction).
  - CVE-2026-73570 says "fixed in 10.1.20 (21 July 2026)" (the entry says 20 July).
  - CVE-2026-58704 says "exploited in limited targeted attacks" (Google: "may be under limited, targeted exploitation").

## Residuals noticed outside the findings (nothing fixed)
- Coding-agent entry (research): no Exposure/Detection lines, and its sourcing note runs about eight sentences.
- Exchange entry: Detection and Defender takeaway are inline in paragraph 2, not separate labelled lines, and there is no Exposure line.
- SonicWall entry: Defender takeaway inline in paragraph 3; no Exposure/Detection lines.
- Pixel entry: no Exposure/Detection lines.
- Check Point: both SKs were last modified 2026-10-13. If the R82.20 Take 10 line was added after 2026-09-30, it was a new fix in the world, not an omission (not determinable; the HFA index is a WebHelp shell).
- JFrog entry: still `priority: critical` with an immediate_action five weeks after exploitation began; a calibration question for the audit.
- SAP August: Onapsis also lists Note 3747367 (CVE-2026-44747, HotNews 9.9 update), not in the entry. SAP's page shows a later "Update to Security Note" for 3771065, whose content was not read.
- MikroTik: em dashes remain in title, summary, sourcing_note, actions[1] and body (18) for its next record.
- Cisco ISE and Pixel: earlier `updates[]` summaries still carry statements later corrections retracted (append-only, audit trail only).
