**Model:** Opus 5.5 (`claude-opus-5-5`)

# Repair batch 1, cleanup wave 04 (run 2026-10-21T1148Z-audit)

BLOCKER: 2026-05-12/bka-and-zit-dismantle-relaunched-crimenetwork-darknet-market (incident) has no `techniques[]`, so the run-scope gate FAILs it (`attack-mapping`). Its sources (Help Net Security relaying the BKA release; bka.de itself served a maintenance page to both `extract` and WebFetch on 2026-10-21) describe only a law-enforcement takedown: the Mallorca arrest, the relaunch of the marketplace after the December 2024 takedown, user and vendor counts, revenue and seized assets. No intrusion behaviour by anyone is described. Options for the main agent: re-kind it (it reports a law-enforcement action, not an intrusion), or drop it.

BLOCKER: 2026-05-13/bwh-hotels-best-western-worldhotels-sure-hotels-181-day-unau (incident) has no `techniques[]`, so the run-scope gate FAILs it (`attack-mapping`). The Register and SecurityWeek, relaying BWH's guest notification and CTO statement, describe unauthorised access from 2025-10-14 (or data going back to that date) to a guest-reservation web application, discovered on 2026-04-22: names, email addresses, phone numbers, home addresses and reservation details. They give no access vector, no actor and no collection mechanism. A reservation web application is not a repository or cloud store the T1213 or T1530 families describe, so mapping one would be invented.

Research entry with an empty mapping (allowed by the brief, WARN only in run scope): 2026-05-10/bauman-university-department-no-4-leaked-gru-cyber-operator. The leaked documents describe a training curriculum and staffing, not observed attacker behaviour.

## Records written: 20 (17 correction, 3 improvement); none skipped

Checks run: `entry_record.py diff` matches every record's `fields` (20/20). All 97 `evidence[]` quotes match a saved or freshly fetched body (`grep -F`, whitespace-normalised). The em-dash, T-id-in-prose and self-reference scan is clean on all 20. `_scan_iocs` is clean. `check_reader_text_internals` (run scope, v4.17 enforcement) passes. The run-scope `check_attack_mapping` (strict ids) leaves only the two BLOCKER FAILs and the Bauman WARN. `check_run.py --all` exits 0; the only lines naming my entries are the expected "updates[0].run_id does not resolve to a run record" WARNs. The twin entry `2026-05-22/west-pharmaceutical-services-8-k-a-confirms-full-operational` is unchanged.

Common legacy duties on every entry: `classification` set, `updates: []` added where missing before the record, `sources[]` publisher/date split, em dashes removed from reader text, evidence rows added (non-English originals in `original:`), uncited guidance removed, labelled lines added where the sources support them.

### 2026-05-10/bauman-university-department-no-4-leaked-gru-cyber-operator
- correction at 2026-10-21T20:21:31Z; fields: affected_products, body, classification, confidence, entities, evidence, headline, sources, sourcing_note, summary, techniques, title.
- Applied all 8 findings. The documents were reviewed, not published (Meduza). The 2025 to 2026 APT28 clause is dropped; Le Monde's most recent item is the Paris 2024 Olympics. The Macron contradiction is stated (Guardian/Meduza: Sandworm; Le Monde: Fancy Bear). Attributions are worded as accusations; NotPetya is attributed to heise citing Spiegel. The Bundestag hack is dropped. Metasploit and the DoD networks are cited to VSquare (added as a source). The one-month camp is "all students attend" (heise, translated). "Penetration testing against Western targets", "CVE-driven" and the mental-model analysis are dropped; Mirea is added as context. The truncated summary is rewritten.
- Rating B2. Techniques: none (see above). Labelled lines: Defender takeaway only; no source supports Exposure or Detection.
- Entities keyed: `report:bauman-gru-pipeline-investigation-2026`, `actor:sandworm`, `actor:apt28`.

### 2026-05-10/braintrust-ai-evaluation-platform-aws-account-breach-multi-t
- correction at 2026-10-21T20:23:33Z; fields: affected_products, body, classification, confidence, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title, verification.
- Applied all 8 findings (https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/, TechCrunch). Discovered 05-04, disclosed 05-05; the one-day email discrepancy is noted; no access date exists. Rotation was requested, not mandated. The Box/Cloudflare list is the Nudge CTO's estimate. The provider names are dropped. "At least one affected, three usage spikes" is now cited. The LiteLLM sentence is replaced by attributed "credential warehouse" wording. The invented 05-04 to 05-06 log window is replaced by a provider-usage check. event_date is now 2026-05-05 and the self-reference is removed.
- Rating B2; verification single-source-victim. Techniques: T1496.004 (usage spikes the sources tie to the incident; no access vector stated). Labelled lines: Exposure, Detection, Defender takeaway.

### 2026-05-10/clickfix-campaign-expands-to-macos-macsync-shub-stealer-and
- correction at 2026-10-21T20:25:53Z; fields: affected_products, body, classification, entities, evidence, headline, sources, sourcing_note, summary, techniques, title, verification.
- Applied all 6 findings (https://www.microsoft.com/en-us/security/blog/2026/05/06/clickfix-campaign-uses-fake-macos-utilities-lures-deliver-infostealers/). Framed as a shift from DMG to Terminal commands. Three execution paths are described. Wallet apps (Ledger Wallet, Trezor Suite, Exodus) are replaced with trojanized archives. Microsoft's detection guidance replaces the Endpoint Security hook claim. T1204.002 becomes T1204.004. "AMOS" is used as Microsoft writes it.
- Partly declined: the truth pass's statement that Apple's `es_event_type_t` has no OpenSSH constant. Its saved snapshot predates macOS 13, so neither the section nor the summary claims the event does not exist; they drop the hook and cite Microsoft's guidance.
- Rating A2; verification single-source (Malwarebytes corroborates only the SHub behaviour). Techniques: T1204.004, T1059.004, T1059.002, T1140, T1105, T1082, T1614.001, T1497.001, T1056.002, T1555.001, T1555.003, T1539, T1005, T1074.001, T1560, T1041, T1071.001, T1070.004, T1543.001, T1543.004, T1036.005, T1553.001, T1102.001, T1554. Labelled lines: Exposure, Detection, Defender takeaway. Entities: `campaign:clickfix-macos-2026`, `malware:macsync`.

### 2026-05-10/cpanel-whm-second-emergency-tsr-in-10-days-embargo-lifted-on
- correction at 2026-10-21T20:29:26Z; fields: affected_products, body, classification, cves, event_date, evidence, headline, priority, sources, sourcing_note, summary, techniques, title.
- Applied all 10 findings:
  - Scores are cPanel's as CNA via EUVD (29202 and 29203: 5.3 CVSS 4.0; 29201: 8.6 CVSS 3.1); THN's 8.8/8.8/4.3 are reported as THN's figures, since the CISA-ADP attribution exists only in the CVE record.
  - Types: 29203 priv-esc, 29201 info-disclosure with auth pre-auth per the CNA vector. `vector: zero-click` is kept because the vocabulary has no "network" value; `auth` carries the precondition.
  - The 44,000 figure is restated as Shadowserver's IPs on 2026-04-30, with exploitation since 2026-02-23 per KnownHost.
  - The pivot claim, the UPDATE lead and the migration note are removed; event_date is 2026-05-08.
  - The full fixed-version table is in `cves[]` and the body (with "version" before four-part numbers).
  - CVE-2026-41940 appears as one cited sentence citing its vendor advisory; it is not added to `cves[]`.
  - Priority is now notable.
- Sources: the three vendor advisories, three EUVD pages, the 41940 advisory, SecurityWeek and THN 05-04 were added; the uncited Panelica blog was dropped.
- Rating A2. Techniques: T1059, T1068, T1005. Labelled lines: Exposure, Detection (file-permission telemetry derived from the vendor mechanism), Defender takeaway.

### 2026-05-10/groupe-3r-r-seau-radiologique-romand-akira-ransomware-claims
- correction at 2026-10-21T20:31:42Z; fields: actions, body, classification, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title. `updated_at` is unchanged (still mirrors the 2026-07-09 update record, which is preserved byte for byte).
- Applied all 10 findings:
  - The attack date is 04-30 and the disclosure date is not given as 04-30.
  - "Second outage" becomes "second attack; the 2025 attack stole data without disruption".
  - The Akira claim is cited to ransomware.live and DeXpose.
  - The seventh canton is Zurich (victim site navigation).
  - Theft of administrative data is now victim-confirmed, and medical-data exfiltration is unprovable (current victim page).
  - The Akira playbook is replaced by CISA AA24-109A, with the access vector stated as not public.
  - "Rebuilt infrastructure" is corrected.
  - "Second attack" is attributed to the press.
  - The earlier `## Update — 2026-07-09` section is fixed in place: attribution "based on methods its partners observed", T1567 and the MTTR benchmark removed, translated quote wording, nothing dated after 07-09.
  - Both generic actions are removed.
- Rating A2. Techniques: T1486 (no vector stated). Labelled lines: Exposure, Defender takeaway (operator's invoice-fraud warning). Priority left high (not flagged; see residuals).

### 2026-05-10/jdownloader-official-site-compromised-windows-and-linux-inst
- correction at 2026-10-21T20:33:12Z; fields: affected_products, body, classification, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title.
- Applied all 7 findings (https://jdownloader.org/incident_8.5.2026.html, BleepingComputer):
  - The window is ~00:01 UTC 05-06 to shutdown on 05-07, and only the "Download Alternative Installer" and Linux shell links were affected.
  - The Python RAT is Klemenc's analysis; the Linux SUID-root binary and /etc/profile.d persistence are described.
  - The vendor published hashes of the substitutes (none reproduced here) and the AppWork GmbH signature check.
  - Publisher names are user reports; "unsigned" comes from the developer.
  - The product description is sourced; CyberKendra is dated 05-08.
  - Detection now uses the sourced telemetry.
- Vendor notice, BleepingComputer and Security Affairs added as sources.
- Rating A1. Techniques: T1190, T1195.002, T1204.002, T1036.005, T1059.006, T1105, T1036.008, T1548.001, T1546.004, T1027. Labelled lines: Exposure, Detection, Triage (signature discriminator from BleepingComputer), Defender takeaway.

### 2026-05-11/bsi-flags-netgate-pfsense-community-edition-as-critical-unpa
- correction at 2026-10-21T20:35:05Z; fields: affected_products, body, classification, confidence, cves, evidence, headline, priority, sources, sourcing_note, summary, techniques, title.
- Applied all 11 findings:
  - CVE-2025-69690 CVSS is 9.1 (EUVD), with the researcher's 8.8 noted.
  - BSI claims are reduced to what the CSAF carries (fetched fresh: https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-1435.json, released 2026-05-07T22:00Z); "UNGEPATCHT" and the mitigation claim are dropped.
  - Netgate's position comes via the researcher, plus the supplier dispute note.
  - The admin-auth precondition is stated; the vector is network (vocabulary `zero-click`) with `admin-required`.
  - The pfSense+ sentence is dropped; the system.xml indicator and brute-force framing are dropped.
  - Priority is now notable; the DACH claim is dropped.
  - cve.news is removed.
- Partly declined: the "disputed" status value is not in the `cve_status` vocabulary, so the dispute is carried in `fixed` ("none (the supplier disputes the vulnerability)") and in the body; status is no-patch and poc-public.
- Rating B2. Techniques: T1078.001, T1059, T1059.004. Labelled lines: Exposure, Detection (derived from the endpoint mechanism), Defender takeaway.

### 2026-05-11/sms-blaster-smishing-establishing-itself-in-switzerland-port
- correction at 2026-10-21T20:36:37Z; fields: affected_products, body, classification, evidence, headline, priority, sources, sourcing_note, summary, techniques, title, verification.
- Applied all 7 findings:
  - BACS 2025-09-09 (https://www.bacs.admin.ch/en/25w36-en) is added as primary, with SRF 2025-11-13 for the arrest; verification is multi-source.
  - The Android advice is now DISALLOW_CELLULAR_2G (API 34, device owner).
  - The detection claim is the BACS 4G-to-2G observation; the MDM product claims are dropped.
  - Device description from BACS; "mutual authentication" and "SMSC" are dropped.
  - The "us" framing is removed; priority is now notable.
  - Technique is T1566.002, plus T1598.003 for the credential and card harvesting.
- Rating A1. Labelled lines: Exposure, Detection, Defender takeaway.

### 2026-05-12/bka-and-zit-dismantle-relaunched-crimenetwork-darknet-market
- improvement at 2026-10-21T20:39:01Z; fields: body, classification, confidence, entities, event_date, evidence, headline, priority, sources, sourcing_note, summary, title.
- Applied all 5 findings (https://www.helpnetsecurity.com/2026/05/11/germany-crimenetwork-marketplace-shut-down/): seizure and data statement, arrest by the Spanish special unit, market framing, takeaway reduced to the sourced statement, priority routine, event_date 2026-05-08, and no techniques invented.
- The BKA source URL is now the press-release page Help Net Security links (`.../260508_PM_Crimenetwork.html`) instead of the unverifiable PDF path. Both served a maintenance page on 2026-10-21, so the arrest date could not be re-checked against the BKA.
- Rating A2. Techniques: unchanged (absent) — BLOCKER above. Labelled lines: Defender takeaway (no decision). Entity keyed: `incident:bka-crimenetwork-takedown-2026`.

### 2026-05-12/gtig-ai-threat-tracker-may-2026-first-confirmed-ai-generated
- correction at 2026-10-21T20:41:20Z; fields: affected_products, body, classification, entities, evidence, headline, priority, sources, sourcing_note, summary, techniques, title.
- Applied all 9 findings (https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access):
  - The zero-day is "believed AI-developed, planned mass exploitation, may have been prevented", with a Contradiction line against THN's "in the wild".
  - The malware section is rewritten (CANFAIL and LONGSTREAM decoy code, PROMPTSPY as runtime-LLM malware, PROMPTFLUX and HONESTCUE as prior-report context).
  - The stolen-key market and the SANDCLOCK claims are dropped; TeamPCP's vector is PyPI and malicious PRs.
  - The valid-credentials precondition and the artefact list are verbatim.
  - T1553 is dropped and T1027.016 used.
  - UNC5673 "overlaps with TEMP.Hex"; OFTP is spelled out.
  - The banner, PD-9, section references and BACS mention are removed.
  - The uncited hardening list is removed.
- Priority is now notable (the high basis was the "in the wild" claim).
- Rating B2. Techniques: T1190, T1078, T1588.007, T1587.004, T1027.016, T1090.003, T1591, T1592.001, T1195.002, T1552. Labelled lines: Exposure, Detection, Defender takeaway. Entity added: `actor:dark-castle` (registry alias UNC2814).

### 2026-05-12/ico-fines-south-staffordshire-water-963-900-water-sector-oes
- correction at 2026-10-21T20:43:46Z; fields: affected_products, body, classification, cves, entities, evidence, headline, priority, sources, sourcing_note, summary, techniques, title.
- Applied all 7 findings (penalty notice https://ico.org.uk/media2/xdrfahsw/south-staffordshire-plc-and-south-staffordshire-water-plc-monetary-penalty-notice.pdf, press release):
  - ZeroLogon is cited to the penalty notice.
  - CVE-2020-1472 is added to `cves[]` with Microsoft as authority (MSRC recipe: CVSS 5.5, release 2020-08-11; KEV status confirmed via the `cisa-kev` recipe: dateAdded 2021-11-03, ransomware use Known).
  - The kill chain is re-sequenced; the regulatory framing is UK GDPR Articles 5(1)(f) and 32(1); "5% monitored"; data figures are cited to the ICO.
  - DC event IDs are dropped; priority notable; headline completed; migration note replaced.
- Rating A2. Techniques: T1566.001, T1204.002, T1068, T1078.002. Labelled lines: Exposure, Detection, Defender takeaway. Entity added: `actor:clop` (press attribution, ICO names no actor).

### 2026-05-12/koda-auto-deutschland-online-shop-breach-exposes-customer-pi
- correction at 2026-10-21T20:44:49Z; fields: affected_products, body, classification, confidence, entities, evidence, headline, sources, sourcing_note, summary, techniques, title, verification.
- Applied all 5 findings (https://www.skoda-auto.de/unternehmen/sicherheitsvorfall-skoda-shop):
  - No 72-hour claim.
  - The invented quotation is replaced by the translated vendor sentence (original in evidence).
  - Scope: accessories shop only; Connect and the manufacturer are unaffected; full card data is not stored.
  - The takeaway is sourced.
  - T1190 is added.
- Rating A2; verification single-source-victim. Labelled lines: Exposure, Defender takeaway. Entity keyed: `incident:skoda-shop-breach-2026`.

### 2026-05-12/west-pharmaceutical-services-files-sec-form-8-k-item-1-05-da
- improvement at 2026-10-21T20:45:48Z; fields: affected_products, body, classification, confidence, entities, evidence, headline, priority, sources, sourcing_note, summary, techniques, title, verification.
- Applied all 4 findings (8-K https://www.sec.gov/Archives/edgar/data/105770/000010577026000068/wst-20260507.htm, BleepingComputer): T1486 only, with the exfiltration method stated as undisclosed; no claim as of 2026-05-13; the product description cited; the takeaway reduced to supply continuity; BleepingComputer added; single-source-victim.
- Priority is now routine (incident floor: impact only, no vector, no actor).
- Twin outside batch, untouched: `2026-05-22/west-pharmaceutical-services-8-k-a-confirms-full-operational` (the 8-K/A follow-up; tracker row). No reference added.
- Rating A2. Techniques: T1486. Labelled lines: Defender takeaway. Entity keyed: `incident:west-pharma-8k-2026`.

### 2026-05-13/bwh-hotels-best-western-worldhotels-sure-hotels-181-day-unau
- correction at 2026-10-21T20:46:47Z; fields: body, classification, confidence, entities, evidence, headline, priority, sources, sourcing_note, summary, title, verification.
- Applied all 5 findings: "six EU brands" and passport data are dropped; dwell is "about six months", with the SecurityWeek/Register difference in the sourcing note; the vector is not disclosed (IAB theory and mappings dropped); "regulators notified, number and location of guests undisclosed".
- Priority is now routine (incident floor).
- Rating B2; single-source-victim. Techniques: unchanged (absent) — BLOCKER above. Labelled lines: Defender takeaway. Entity keyed: `incident:bwh-hotels-breach-2026`.

### 2026-05-13/certfr-2026-avi-0564-spip-4-4-14-multiple-rces-public-and-pr
- correction at 2026-10-21T20:47:49Z; fields: affected_products, body, classification, entities, evidence, headline, sources, sourcing_note, summary, techniques, title.
- Applied all 4 findings (https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-14.html): invented detection patterns dropped; deployment claim dropped; French quotes translated and marked; T1190; "two RCE flaws".
- The tombstone key `campaign:certfr-2026-avi-0564` (merged into `trend:spip-2026-rce-wave`) is removed from `entities`.
- Rating A2. Labelled lines: Exposure, Defender takeaway.

### 2026-05-13/certfr-2026-avi-0572-centreon-infra-monitoring-rce-sqli-xss
- correction at 2026-10-21T20:48:52Z; fields: affected_products, body, classification, entities, evidence, headline, sources, sourcing_note, summary, techniques, title.
- Applied all 4 findings: the CVE summary table and its closing paragraph are deleted; "no CVE identifiers"; the deployment claim and the credential-store and detection claims are dropped; per-component flaws and CVSS come from the Centreon bulletin, and first fixed releases per branch from CERT-FR.
- The tombstone key `campaign:certfr-2026-avi-0572` is removed.
- Rating A2. Techniques: T1190. Labelled lines: Exposure, Defender takeaway.

### 2026-05-13/cve-2026-34263-cve-2026-34260-sap-commerce-cloud-pre-auth-rc
- correction at 2026-10-21T20:50:35Z; fields: actions, affected_products, body, classification, cves, evidence, headline, priority, sources, sourcing_note, summary, techniques, title.
- Applied all 5 findings:
  - CVE-2026-34260 is sqli, post-auth, read and availability only (Onapsis).
  - CVE-2026-34263 is user-interaction per SAP's vector (https://support.sap.com/en/my-support/knowledge-base/security-notes-news/may-2026.html); the Spring Security root cause is cited to EUVD.
  - #3747787 is dated 2026-04-30.
  - The federal-programme sentence and T1213 are dropped.
  - The defective action (exposure claim, section reference) is removed; actions are empty.
- Priority is now notable (regular Patch Day, no exploitation). SAP page and two EUVD pages added.
- Rating A2. Techniques: T1190. Labelled lines: Exposure, Defender takeaway. `campaign:mini-shai-hulud` kept (sourced HotNews statement).

### 2026-05-13/cve-2026-44277-cve-2026-26083-fortinet-fortiauthenticator-an
- improvement at 2026-10-21T20:53:18Z; fields: affected_products, body, classification, cves, evidence, headline, sources, sourcing_note, summary, techniques, title.
- Applied all 4 findings:
  - CVSSv3 is 9.8 base and 9.1 temporal (PSIRT pages fetched fresh into `repair-1/src/forti-128.txt` and `forti-136.txt`); `cves[].cvss` is 9.8.
  - The 6.4 and 4.2 branches are cited to EUVD, with "no fixed release listed by Fortinet".
  - "Cloud 23 and 24: migrate"; `affected` and `fixed` filled.
  - The Swiss relevance claim and the FortiOS command are dropped; the vendor workaround is stated.
- Rating A2. Techniques: T1190. Labelled lines: Exposure, Detection, Defender takeaway.

### 2026-05-13/cve-2026-45185-exim-dead-letter-use-after-free-in-bdat-chunk
- correction at 2026-10-21T20:55:03Z; fields: affected_products, body, classification, cves, evidence, headline, sources, sourcing_note, summary, techniques, title.
- Applied all 5 findings (https://exim.org/static/doc/security/EXIM-Security-2026-05-01.1/EXIM-Security-2026-05-01.1.txt added as primary):
  - The LLM-guided chains covered non-PIE builds only; the PIE exploit was human (stack leak).
  - The CHUNKING workaround is dropped (vendor: no mitigation other than upgrading).
  - CVSS and versions come from the Exim advisory; the prevalence claim is dropped; the Debian/Ubuntu default is cited to XBOW.
  - The STARTTLS and CHUNKING precondition is in Exposure.
  - T1499.004 and the panic.log advice are dropped.
  - `affected` and `fixed` are filled.
- Rating A1. Techniques: T1190, T1059.004 (bash via `${run}` in XBOW's ASLR chain). Labelled lines: Exposure, Detection (derived from XBOW's chain), Defender takeaway.

### 2026-05-13/foxconn-confirms-nitrogen-ransomware-crippled-north-american
- correction at 2026-10-21T20:56:23Z; fields: affected_products, body, classification, confidence, evidence, headline, priority, sources, sourcing_note, summary, techniques, title.
- Applied all 5 findings:
  - Foxconn confirms only "some factories".
  - The state list is where Foxconn has factories; Mount Pleasant comes via worker accounts and Houston via AppleInsider; "ET" and "a week" are dropped.
  - The Nitrogen claim is quoted from The Register.
  - The Coveware finding is stated precisely.
  - The EMS relevance, ESXi shell-log and Cobalt Strike advice are dropped.
- Priority is now notable (out-of-nexus incident).
- Rating B2. Techniques: T1486. Labelled lines: Exposure, Defender takeaway.

## Folds and links

- No duplicate group in the batch; no fold proposed; no `references[]` added.
- possible_twin_outside_batch: 2026-05-12/west-pharmaceutical-services-files-sec-form-8-k-item-1-05-da and 2026-05-22/west-pharmaceutical-services-8-k-a-confirms-full-operational (unchanged; goes to the tracker).

## Registry changes for the main agent (`entities/registry.yaml`)

Aliases:
- `actor:teampcp`: add alias "UNC6780" (source 2026-05-12/gtig-ai-threat-tracker-may-2026-first-confirmed-ai-generated: "TeamPCP (aka UNC6780)").

Summary corrections (each restates a defect corrected in the entry):
- `report:gtig-ai-threat-tracker-may-2026`: drop "first AI-generated zero-day exploit ITW". Suggested: "Google Threat Intelligence Group AI Threat Tracker of 2026-05-11: a criminal zero-day 2FA-bypass exploit GTIG believes was AI-developed, prepared for planned mass exploitation that disclosure may have prevented; LLM-generated decoy code in CANFAIL and LONGSTREAM; the Gemini-driven Android backdoor PROMPTSPY; PRC and DPRK actors using Gemini for vulnerability research; LLM account pooling; TeamPCP supply-chain attacks on AI components."
- `actor:dark-castle`: its last sentence says GTIG's May 2026 tracker names UNC2814 for ORB-fleet management and CVE/PoC validation. Per GTIG, UNC2814 used expert-persona prompting for vulnerability research into TP-Link firmware and OFTP implementations; the ORB tool was APT27's and the CVE/PoC validation APT45's.
- `campaign:clickfix-macos-2026`: replace "expands to macOS ... bypass Gatekeeper" with "macOS infostealer campaign (MacSync, SHub Stealer, AMOS) that shifted from disk-image delivery to ClickFix Terminal commands (Microsoft, 2026-05-06)".
- `actor:akira`: "edge-device CVE chains and intermittent-encryption EDR evasion" is unsourced. CISA AA24-109A: initial access mostly through VPN services using known CVEs; encryption full or partial by file type and size; mainly targets small and medium businesses.
- `incident:foxconn-nitrogen-2026`: drop "crippled" and "the ESXi decryptor proved mathematically broken". Suggested: "Cyberattack on some Foxconn North American factories (confirmed 2026-05-12), claimed by Nitrogen with 8 TB of alleged customer project data."
- `incident:jdownloader-supply-chain-2026`: drop "(~48 h window)" and "Windows/Linux ... Python RAT". Suggested: "jdownloader.org CMS compromise that pointed the Windows alternative-installer and Linux shell-installer links to malware on 6 and 7 May 2026."
- `incident:bwh-hotels-breach-2026`: drop "181-day dwell" and "EEA guests in scope". Suggested: "access to a BWH Hotels guest-reservation web application from 2025-10-14 until discovery on 2026-04-22."
- `incident:south-staffordshire-water-ico-2026`: drop "a UK NIS2/CER precedent" and "SOC coverage"; it is a UK GDPR penalty (Art. 5(1)(f), 32(1)); 5% of the IT environment monitored.
- `incident:braintrust-aws-breach-2026`: "LLM provider keys" becomes "org-level AI provider keys"; optional.
- `incident:groupe-3r-akira-2026`: optionally add "administrative data stolen and published (victim-confirmed)".
- `trend:spip-2026-rce-wave`: drop the unsourced "dominant French public-administration CMS with wide EU/CH Francophone government deployment".
- `trend:centreon-april-2026-vuln-cluster`: drop the unsourced "widely deployed in European public-sector infrastructure monitoring".
- `campaign:sms-blaster-ch-2026`: optional, add "reported by BACS since September 2025".

Relations (subject record, source entry id):
- `incident:groupe-3r-akira-2026` -> `actor:akira`, type attributed-to, source 2026-05-10/groupe-3r-r-seau-radiologique-romand-akira-ransomware-claims, note "victim attributes the attack to Akira on methods its partners observed".
- `incident:south-staffordshire-water-ico-2026` -> `actor:clop`, source 2026-05-12/ico-fines-south-staffordshire-water-963-900-water-sector-oes, note "attribution by The Record and The Register; the ICO names no actor". Use attributed-to or related-to as the main agent judges.

New entities (optional, the main agent decides):
- `actor:nitrogen`: ransomware group believed to use a builder based on the Conti ransomware, first observed in 2023 (Barracuda via The Record); Coveware documented a bug in its ESXi encryptor that leaves files unrecoverable (2026-02-02). Source 2026-05-13/foxconn-confirms-nitrogen-ransomware-crippled-north-american. Relation from `incident:foxconn-nitrogen-2026`, claimed responsibility (related-to unless the main agent treats a claim as attribution).
- GTIG entry candidates (not keyed): `malware:promptspy`, `malware:canfail`, `malware:longstream`, `actor:apt45`, `actor:apt27`, `actor:unc5673` (PRC-nexus, overlaps with TEMP.Hex, targets government sectors in South and Southeast Asia). Each has sourced text in the GTIG entry.

Products named for the first time in `affected_products` (product entities to create): "AppWork JDownloader", "Netgate pfSense CE", "Centreon Infra Monitoring", "Exim", "Fortinet FortiAuthenticator".

## `state/cves_seen.json` changes (set `last_seen` to 2026-10-21 on each)

- CVE-2026-29201: title "cPanel & WHM arbitrary file read via feature::LOADFEATUREFILE"; primary_source_url https://support.cpanel.net/hc/en-us/articles/40311033698327-Security-CVE-2026-29201-cPanel-WHM-WP2-Security-Update-May-08-2026 (current value is the watchTowr homepage, and the title still says "dropped ... embargoed").
- CVE-2026-29202: title "cPanel & WHM Perl code injection in create_user API (authenticated)"; primary_source_url https://support.cpanel.net/hc/en-us/articles/40311426610327-Security-CVE-2026-29202-cPanel-WHM-WP2-Security-Update-May-08-2026 (current: watchTowr homepage).
- CVE-2026-29203: last_seen bump (record changed); title fine.
- CVE-2025-69690 and CVE-2025-69691: last_seen bump; drop "vendor refuses" from the titles in favour of "supplier disputes".
- CVE-2020-1472: last_seen bump (added to the ICO entry's `cves[]`); title "chained by Cl0p" becomes "exploited during the South Staffordshire Water intrusion".
- CVE-2026-34263 and CVE-2026-34260: last_seen bump.
- CVE-2026-44277: last_seen bump.
- CVE-2026-26083: last_seen bump; title "CVSS 9.1" becomes "CVSSv3 9.8 base, 9.1 temporal".
- CVE-2026-45185: last_seen bump.

## Residuals noticed (not fixed)

- No entry in the store covers CVE-2026-41940 (cPanel & WHM authentication bypass; CISA KEV 2026-04-30, known ransomware use); it appears only as context in the cPanel entry.
- Groupe 3R keeps `priority: high` (not flagged). The access vector is unknown and the incident is single-victim outside the government constituency, so the audit may want it at notable.
- The SPIP and Centreon entries kept their regions and sectors (`public-sector`); no cited source carries public-sector deployment, so the sector tag rests only on CERT-FR's audience.
- bka.de served a maintenance page to `extract`, the jina reader and WebFetch on 2026-10-21, and two jina keys reported exhausted balances; the CrimeNetwork arrest date remains verified only through Help Net Security.
- The ClickFix truth finding relied on an Apple `es_event_type_t` snapshot that predates macOS 13; a future truth pass should not cite it for the absence of OpenSSH events.
- The Fortinet PSIRT saved body in `truth-1/bodies/` is truncated before the temporal score; the fresh raw copies are in `work/2026-10-21T1148Z-audit/repair-1/src/`.
- 2026-08-07/macos-clickfix-server-side-fingerprinting-gate-amos describes a later evolution of the same Microsoft-tracked campaign and shares `campaign:clickfix-macos-2026`; distinct finding, no link needed from the older entry.
