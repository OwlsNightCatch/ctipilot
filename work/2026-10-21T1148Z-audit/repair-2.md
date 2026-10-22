# Repair batch 2 report (run 2026-10-21T1148Z-audit, cleanup wave 04)

**Model:** Opus 5.5 (`claude-opus-5-5`). One session-limit pause between entry 4 and entry 5 (records before 16:09Z, after 20:19Z).

16 entries, 16 records: 15 `correction`, 1 `improvement`, 0 internal, 0 `update`. Every record's `fields` equals `tools/entry_record.py diff` (checked mechanically after the last edit). Every new `evidence[]` quote was checked against the saved bodies, literally or in the gate's letters-and-digits form (non-breaking spaces and markdown links in the extracts); translations carry their Dutch `original:`. No em dash is left in reader text outside the `## <Type> — <at>` headings. Every entry got `classification`, `techniques`, `affected_products`, `updated_at` and `updates` keys where it had none. The legacy "UPDATE (originally covered ...)" labels (Checkmarx, Gentlemen, Datadog) are gone. `actions[]` is empty on all 16 (May findings, no do-now task remains); the Ivanti, Nextcloud and AMD entries had actions, which are removed and declared in `fields`.

Gate: `check_run.py --all` shows no FAIL or WARN on these entries except (a) the expected "run_id does not resolve to a run record" WARN and (b) the store-wide `cve-sync` FAIL for the six CVEs listed under § cves_seen below, which the main agent must add.

Fresh fetches saved under `work/2026-10-21T1148Z-audit/repair-2/src/`: Computable 2026-05-13 (readable now; the truth pass got HTTP 503), the TanStack GHSA raw page (carries CVE-2026-45321 and 9.6), GovInfoSecurity and THN raw pages (dates), and the CISA KEV feed of 2026-10-21.

## Per entry

### 2026-05-12/teampcp-unc6780-pcpjack-ecosystem-backdoors-the-checkmarx-je
- correction, at 2026-10-21T15:57:54Z; fields: affected_products, body, classification, cves, entities, event_date, evidence, headline, kind, regions, sources, sourcing_note, summary, tags, techniques, title.
- Applied: CVE-2026-33634 record and sentence removed (it is the Trivy CVE, https://github.com/advisories/GHSA-69fq-xp46-6x23); SANDCLOCK kept only as GTIG's name for the March stealer (https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access); target list, chronology, auto-update premise, defacement scope and attribution wording per Checkmarx (https://checkmarx.com/blog/ongoing-security-updates/), BleepingComputer, THN and SOCRadar; PCPJack unkeyed and described per SentinelLABS; self-quoting evidence replaced. kind vulnerability → threat; event_date 2026-05-11 → 2026-05-09; regions europe dropped; tags vulnerabilities and ai-abuse → infostealer. Keyed `incident:checkmarx-jenkins-ast-plugin-2026` (existed, was unkeyed). THN kept as first `sources[]` record.
- Declined: none.
- Legacy: A/2; T1195.002, T1078, T1552.001; Exposure, Detection, Defender takeaway (no honest Triage).

### 2026-05-13/microsoft-mdash-multi-model-agentic-vulnerability-discovery
- correction, at 2026-10-21T16:01:41Z; fields: affected_products, body, classification, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title.
- Applied: figures re-cited to Microsoft's blog with sample sizes (tcpip.sys 7 cases, clfs.sys 28); prove stage per Microsoft (no "practically exploitable"); per-CVE MSRC scores, release months and exploitability ratings; "first production run", June preview, Swiss/EU deployment claim and "§ 2" removed; IKEv2 responder exposure condition; T1133 dropped. Surfaced a discrepancy: the MDASH blog describes the CVE-2026-33827 trigger as IPv4 SSRR packets, the MSRC FAQ as an IPv6 packet to an IPsec-enabled node. Ground truth: https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-finds-16-new-vulnerabilities/ and the four msrc.microsoft.com update-guide pages.
- Declined (partly): finding 7 offered "cves[] or the body"; the four Critical CVEs are named in the body only, so the entry does not duplicate the structured CVE coverage of its possible twin (see § Twins).
- Legacy: B/2; T1190; Exposure, Detection, Defender takeaway.

### 2026-05-13/mini-shai-hulud-s-github-actions-pwn-request-oidc-token-thef
- correction, at 2026-10-21T16:08:09Z; fields: affected_products, body, classification, cves, event_date, evidence, headline, sectors, sources, sourcing_note, summary, tags, techniques, title.
- Applied: deep dive rewritten from TanStack's post-mortem (https://tanstack.com/blog/npm-supply-chain-compromise-postmortem), its GHSA, StepSecurity, Wiz and NCSC-CH hub 12558: SAP first wave 2026-04-29 (The Register); reconnaissance step and T1593 dropped; PR content, skipped publish step, OIDC handling, genuine (not forged) provenance, `prepare` not `postinstall`, sudo-run memory scraper; invented `save: false` and `npm provenance verify` replaced by the restore action and `npm audit signatures`; SHA-pinning overclaim removed; inline T-ids removed; every chain step cited. Added CVE-2026-45321 (9.6 from the GHSA page, KEV 2026-05-27 with known ransomware use from the KEV feed). Attacker account names, the spoofed commit e-mail, file names and the npm-token ransom string left out as indicators. event_date 2026-05-12 → 2026-05-11; sectors public-sector dropped; tags ai-abuse dropped, wiper and cisa-kev added.
- Declined: none (finding 7, low confidence, applied).
- Legacy: A/1 (TanStack plus independent StepSecurity, Wiz, NCSC-CH); 18 ids: T1190, T1195.001, T1195.002, T1059.007, T1105, T1027, T1003.007, T1528, T1550.001, T1552.001, T1552.005, T1567, T1567.001, T1546, T1543.001, T1543.002, T1036, T1485; Exposure, Detection, Defender takeaway.

### 2026-05-13/ncsc-uk-10-questions-to-ask-when-using-ai-models-to-find-vul
- correction, at 2026-10-21T16:09:00Z; fields: affected_products, body, classification, evidence, headline, sources, summary, techniques, title.
- Applied: invented (f) false-positive item and the (b)/(d) glosses removed; NCSC's hedged wording quoted; NCSC-CH comparison and `[SINGLE-SOURCE]` marker removed. Ground truth: https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities.
- `techniques: []` deliberately: the page describes no attacker behavior (it is defensive guidance). The gate WARNs on an empty mapping for research entries on v3.18+ runs; it did not fire under `--all`.
- Legacy: A/2; Defender takeaway only (the page gives no exposure condition, telemetry or discriminator).

### 2026-05-13/trickmo-trickmo-c-android-banking-trojan-migrates-c2-to-the
- improvement, at 2026-10-21T20:19:00Z; fields: affected_products, body, classification, evidence, headline, sources, sourcing_note, summary, techniques, title.
- Applied: TON detection point, Pine/NFC reading, "Facebook campaigns" not ads, per ThreatFabric (https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app) and THN; Mobile ATT&CK ids removed from prose; MDM/public-sector paragraph replaced by sourced guidance.
- Declined: none.
- Legacy: B/2; T1036.005, T1105, T1056.001, T1056.002, T1113, T1111, T1071.001, T1090, T1572, T1016, T1046 (Enterprise only; no Mobile ids in the pin); Exposure, Detection, Defender takeaway.

### 2026-05-14/cve-2026-8043-ivanti-xtraction-external-file-control-cvss-9
- correction, at 2026-10-21T20:20:51Z; fields: actions, affected_products, body, classification, cves, event_date, evidence, headline, priority, sources, sourcing_note, summary, tags, techniques, title.
- Applied: CVE-2026-8043 type rce → info-disclosure with `< 2026.2` / `2026.2`; added CVE-2026-8111 (8.8) and CVE-2026-8051 (7.2) from ENISA EUVD (EUVD-2026-29487, -29491, -29488); EPM "before 2024 SU6"; no-exploitation statement cited to Ivanti's blog (https://www.ivanti.com/blog/may-2026-security-update); web-shell chain, egress premise, 2026-04-01 window, IAB claim, "Inclusion gate cleared" and "See § 2" removed; Secure Access Client (22.8R6, CERT-FR) named; headline completed; priority high → notable; action removed. event_date 2026-05-13 → 2026-05-12.
- Declined: none.
- Legacy: A/2; T1190, T1059; Exposure, Detection, Defender takeaway.

### 2026-05-14/dutch-igj-rules-clinical-diagnostics-nmdl-failed-nen-7510-in
- correction, at 2026-10-21T20:23:07Z (summary amended); fields: affected_products, body, classification, entities, evidence, headline, priority, sources, sourcing_note, summary, tags, techniques, title.
- Applied: IGJ's ask (demonstrate compliance), the company's positive audit, enforcement position and "could have reduced the likelihood" wording per IGJ (https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging), Dutch quoted in translation with originals in `evidence`; Swiss/EPDG comparison, ISO claim and "proximate consequence" removed; Nova and the 941,000 figure cited to GovInfoSecurity (dated 2025-09-03 from its byline) with the extent caveat. Computable, readable this session, adds the access vector (compromised account without MFA, legacy environments outside SOC monitoring) and IGJ's call on providers; keyed `incident:clinical-diagnostics-nmdl-igj-2026` (existed, unkeyed); priority high → notable.
- Declined (partly): finding 1 asked to delete the sector-wide call unless a source carries it. Computable carries it ("geeft de IGJ aanleiding om zorgaanbieders op te roepen om aantoonbaar te werken volgens NEN 7510"), so it stays, re-cited to Computable.
- Legacy: A/2; T1078, T1657; Exposure, Detection, Defender takeaway.

### 2026-05-14/famoussparrow-three-wave-intrusion-of-an-azerbaijani-energy
- correction, at 2026-10-21T20:26:12Z; fields: affected_products, body, classification, cves, entities, evidence, headline, regions, sources, sourcing_note, summary, tags, techniques, title.
- Applied: deep dive rebuilt from Bitdefender (https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry): "does not establish motive", moderate-to-high attribution, evolved (not novel) sideload matching Trend Micro's Earth Estries loader, TernDoor attempt blocked, re-entry through the unpatched server (no surviving persistence), Hamachi-path persistence, Bitdefender's own detection actions and triage discriminators; rollback claim, generic IIS/ASR/legacy-auth bullets, victimology and "first in some time" removed; added CVE-2022-41040/41082 records (MSRC 8.8/8.0, KEV 2022-09-30, fixes 2022-11-08) and surfaced the authentication contradiction (MSRC "Yes, the attacker must be authenticated" vs Bitdefender "unauthenticated"); T1574.002 → T1574.001; headline completed; regions europe/apac → russia-cis; keyed `actor:famoussparrow` and `campaign:famoussparrow-azerbaijan-2026`. Hashes, C2 domains, web-shell and driver file names omitted.
- Declined: the upgrade block's T1685 is not mapped. Bitdefender maps the StartServiceCtrlDispatcherW patch to T1562, whose pin successor is T1685 "Disable or Modify Tools"; the patch hijacks the service start-up path rather than disabling tools, so T1685 would misdescribe it.
- Legacy: B/2; 17 ids: T1190, T1505.003, T1574.001, T1543.003, T1569.002, T1036.005, T1140, T1027, T1055, T1112, T1071.001, T1078.002, T1021.001, T1059.001, T1105, T1021.002, T1014; Exposure, Detection, Triage, Defender takeaway.

### 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha
- correction, at 2026-10-21T20:28:35Z; fields: body, classification, entities, evidence, headline, sources, sourcing_note, summary, tags, techniques, title. `updated_at` stays 2026-09-19T04:45:00Z; the 2026-09-19 record is untouched.
- Applied: title/headline state the attribution as the researchers', with RubyGems unable to confirm and OpenAI disputing (https://blog.rubygems.org/2026/09/11/update-may-spam-publishing-campaign.html); Socket named as documenting without attribution; RubyDoc.info as a separate site; "had not filed as of 2026-09-18"; main analysis rebuilt from Socket (https://socket.dev/blog/gemstuffer) with its recon step, its two detection signals and the CI egress rule (Triage line from Socket's "abnormal operation" statement); 155 artifacts / more than 100 gems. In the 2026-09-19 section (fixed in place, no later events added): attacker contact e-mail replaced by "a contact address impersonating OpenAI", "on the DSEWiki entry" replaced by Euractiv's description, the "same trust boundary" lesson rewritten from Nightingale's findings, OpenAI's two sentences quoted without an ellipsis splice, em dashes replaced. Techniques T1195.002, T1552.001 → T1528, T1585 (+T1567); credibility 1 → 2; tag organized-crime dropped; `incident:hugging-face-autonomous-ai-agent-breach-2026-07` unkeyed (comparison only). `source_url` added to the pre-existing evidence rows.
- Declined: none. Note: the pre-existing September `.yardopts` evidence quote does not match the saved extract because the extract renders "RubyDoc.info" as a markdown link; the live HTML should match.
- Legacy: B/2; T1190, T1528, T1585, T1567, T1567.004; Exposure, Detection, Triage, Defender takeaway.

### 2026-05-14/the-gentlemen-raas-backend-rocket-database-leaked-16-22-gb-c
- correction, at 2026-10-21T20:30:42Z; fields: affected_products, body, classification, entities, evidence, headline, sources, sourcing_note, summary, techniques, title.
- Applied: decryptor advice replaced by the memory-capture requirement from the Bedrock Safeguard README (https://github.com/Bedrock-Safeguard/gentlemen-decryptor) and the same-day patch (BankInfoSecurity); 1,570 re-scoped to one affiliate's SystemBC C&C from Check Point's earlier DFIR report, under-reporting claim dropped; initial access, CVE tracking, CWMP/TR-069, ETW/NTDLL attribution, CertiHound via NetExec per Check Point (https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/); tool process names removed from detection in favour of behaviors; 8,200 lines attributed to DynaRisk; "UPDATE (originally covered ... quarterly synthesis)" removed. Entities: tombstone `actor:gentlemen-raas-gentlekiller` and the deleted synthesis `report:q1-2026-ransomware-quarterly` removed, `actor:thegentlemen` kept. Operator handles and TOX IDs not carried.
- Declined: none.
- Legacy: B/2; 15 ids: T1190, T1110, T1078, T1557.001, T1649, T1685 (EDR start-up blocking fits "Disable or Modify Tools"), T1003.001, T1539, T1135, T1484.001, T1572, T1219, T1490, T1486, T1657; Exposure, Detection, Defender takeaway.

### 2026-05-15/cve-2026-45691-nextcloud-server-enterprise-server-2fa-bypass
- correction, at 2026-10-21T20:32:25Z; fields: actions, affected_products, body, classification, cves, evidence, headline, kind, priority, sources, sourcing_note, summary, techniques, title.
- Applied: "pre-auth" corrected to password-dependent (PR:L) per GHSA-mp6x-g55j-w9jw (https://github.com/nextcloud/security-advisories/security/advisories/GHSA-mp6x-g55j-w9jw, page dated 2026-05-13); version ranges; batch ids and severities corrected from the four GHSAs; CVE records for 45691 and 45690 added; EU-deployment claim and uncited PoC/ITW sentence removed (KEV absence as of 2026-10-21 stated instead); T1550.001 → T1550.004; kind threat → vulnerability; priority high → notable; action removed. Four-part versions written "version 31.0.14.5" etc.
- Declined: none.
- Legacy: A/2; T1078, T1550.004, T1213; Exposure, Detection, Defender takeaway.

### 2026-05-15/cve-2026-45793-php-composer-github-actions-ci-token-disclosu
- correction, at 2026-10-21T20:33:27Z; fields: affected_products, body, classification, cves, entities, evidence, headline, kind, sources, sourcing_note, summary, tags, techniques, title, verification.
- Applied: mechanism per Packagist (https://blog.packagist.com/composer-2-9-8-and-2-2-28-fix-github-actions-token-disclosure-in-error-messages/): token-format validation on the default path, GITHUB_TOKEN and App tokens (not PATs), setup-php auto-registration; lifetimes, rollback and 18 May re-rollout; App-token permission statement replaces the unsupported write-access claim; Mini Shai-Hulud sentence and `campaign:mini-shai-hulud` removed; CVE record added from GHSA-f9f8-rm49-7jv2 (7.5); kind threat → vulnerability; verification single-source → multi-source (Packagist post plus the GHSA, same assessor).
- Declined: none.
- Legacy: A/2; T1552.001, T1528; Exposure, Detection, Defender takeaway.

### 2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off
- correction, at 2026-10-21T20:34:33Z; fields: affected_products, body, classification, entities, event_date, evidence, headline, sources, sourcing_note, summary, tags, techniques, title.
- Applied: deliberate open-source release, not a leak; GitHub removed the repository after forks; pwn-request, `pull_request_target` and `head.sha` injection claims and the advice built on them removed; OIDC path hardcoded to one workflow and package; Russian-locale exit, wipe-on-revocation daemon and Datadog's compromise checks added (https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/); truncated summary and "UPDATE (...)" preamble replaced; keyed `tool:datadog-shai-hulud-framework-2026-05` and `campaign:mini-shai-hulud`; event_date 2026-05-13 → 2026-05-12. Commit e-mail, commit message, repository description string, hashes and C2 domains left out.
- Declined: none.
- Legacy: B/2; 18 ids: T1195.002, T1059.004, T1059.007, T1003.007, T1552.001, T1552.005, T1552.007, T1528, T1550.001, T1546, T1543.001, T1543.002, T1027, T1614.001, T1041, T1102.001, T1567.001, T1485; Exposure, Detection, Defender takeaway.

### 2026-05-15/frostyneighbor-ghostwriter-unc1151-belarus-state-aligned-ese
- correction, at 2026-10-21T20:36:01Z; fields: affected_products, body, classification, evidence, headline, sectors, sources, sourcing_note, summary, tags, techniques, title.
- Applied: scope corrected to Ukrainian governmental organisations since March 2026; the Poland/Lithuania sector list stated as ESET's historical victimology (https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/); scheduled-task, Run-key LNK and renamed-rundll32 behaviors added to the body, Detection and Triage lines; inline ATT&CK links removed; sectors healthcare/manufacturing dropped; tag russia-nexus dropped (ESET says Belarus-aligned), phishing added. Attacker file names (lure, RAR, renamed binary) and C2 URLs left out.
- Declined: none.
- Legacy: B/2; 13 ids: T1566.001, T1204.002, T1059.007, T1027, T1140, T1053.005, T1082, T1057, T1071.001, T1105, T1036.003, T1218.011, T1547.001; Exposure, Detection, Triage, Defender takeaway.

### 2026-05-15/sophos-2026-state-of-identity-security-switzerland-records-h
- correction, at 2026-10-21T20:37:00Z; fields: affected_products, body, classification, confidence, entities, event_date, evidence, headline, regions, sources, sourcing_note, summary, tags, techniques, title, verification.
- Applied: Sophos's own blog added as primary, dated 2026-05-12 (https://www.sophos.com/blog/sophos-state-of-identity-security-2026); ransomware sentence restated as Sophos words it, the three-way breakdown dropped; NCSC-CH, Lumma, FamousSparrow and TeamPCP cross-links, `actor:teampcp` and the nation-state tag removed; kept to a short survey item; keyed `report:sophos-identity-security-2026` (existed); confidence high → medium; verification single-source → multi-source. HNS stays first record.
- `techniques: []` deliberately: the survey describes no attacker behavior.
- Rating: B/3, not the truth pass's C/3. Its C rested on Help Net Security as the reporting source; the primary is now Sophos's own blog, B in `sources/sources.json` (sophos-xops); credibility 3 because the figures are self-reported survey answers with no independent assessment.
- Declined: none.
- Legacy: Defender takeaway only (no exposure condition, telemetry or discriminator in a survey).

### 2026-05-16/amd-sb-7052-cve-2025-54518-amd-zen-2-op-cache-corruption-soc
- correction, at 2026-10-21T20:38:27Z; fields: actions, affected_products, body, classification, cves, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title.
- Applied: mitigation split per AMD (https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7052.html): OS update for EPYC 7002 / Embedded 7002, OEM BIOS with PI versions for Ryzen, Threadripper PRO and Ryzen Embedded; Microsoft's "enable the mitigation" wording and Exploitation Unlikely; Xen XSA-490 impact (guest to host), no mitigation besides patches; CVE table of Exchange and OpenClaw findings removed; `wmic` check, Patch Tuesday cross-reference and unverified Fedora/Lenovo detail removed; action removed; event_date 2026-05-15 → 2026-05-12; `affected_products` with AMD's exact product names.
- Declined: none.
- Legacy: A/2; T1068, T1611; Exposure, Defender takeaway (no telemetry in any source, so no Detection line).

## Folds and links

None. The truth pass found no duplicate group; I found no pair inside the batch that needed a `references[]` link.

## Possible twins outside the batch (nothing changed)

- 2026-05-13/microsoft-mdash-multi-model-agentic-vulnerability-discovery and entries/2026-05-13/cve-2026-41089-cve-2026-41096-cve-2026-41103-cve-2026-42898.md (May Patch Tuesday entry carrying CVE-2026-41089 and CVE-2026-41096, which MDASH found).
- 2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off and entries/2026-06-09/teampcp-open-sources-its-mini-shai-hulud-framework-spawning.md (same open-sourcing event, reported via SANS ISC on 2026-06-08).

## Registry changes for the main agent

- `actor:teampcp`: summary names "the SANDCLOCK Checkmarx Jenkins-plugin backdoor", which no source supports; suggested: "Cybercrime actor targeting software supply chains (GTIG tracks it as UNC6780): the March 2026 Trivy, Checkmarx, LiteLLM and BerriAI compromises, the Mini Shai-Hulud npm worm, and a claimed compromise of the Checkmarx Jenkins AST plugin in May 2026." Add alias "UNC6780" (GTIG; source 2026-05-12/teampcp-unc6780-pcpjack-ecosystem-backdoors-the-checkmarx-je).
- `incident:checkmarx-jenkins-ast-plugin-2026`: summary "SANDCLOCK exfiltrates CI/CD secrets" is unsupported; suggested: "Rogue Checkmarx Jenkins AST plugin build 2026.5.09, live 2026-05-09 01:25 to 2026-05-10 08:47 UTC, swept OS-specific credential file paths; Checkmarx traces the access to the March 2026 Trivy compromise; claimed by TeamPCP." Its `attributed-to actor:teampcp` relation stays (the entry still states the claim).
- `tool:microsoft-mdash-2026`: summary should read "16 CVEs across the Windows networking and authentication stack (10 kernel-mode, 6 user-mode), four of them Critical RCEs" instead of "in network-stack kernel components"; alias "Microsoft Security multi-model agentic scanning harness".
- `campaign:mini-shai-hulud`: add relation `{to: actor:teampcp, type: attributed-to, source: 2026-05-13/mini-shai-hulud-s-github-actions-pwn-request-oidc-token-thef, note: StepSecurity and Wiz attribute the TanStack wave to TeamPCP}`.
- `tool:datadog-shai-hulud-framework-2026-05`: name and summary describe a Datadog scanner, which is wrong. Suggested name "Shai-Hulud offensive framework (open-source release)", alias "Shai-Hulud Open Source", summary: "TeamPCP's TypeScript/Bun framework for credential harvesting, supply-chain poisoning and encrypted exfiltration, released on GitHub on 2026-05-12 and statically analysed by Datadog Security Labs on 2026-05-13." Relation on `actor:teampcp`: `{to: tool:datadog-shai-hulud-framework-2026-05, type: uses, source: 2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off}`.
- `incident:openai-rubygems-agent-attack-2026-05`: summary states the OpenAI attribution as fact, says Socket documented it "anonymously" and calls RubyDoc.info RubyGems' companion service; rephrase to the researchers' attribution, which RubyGems cannot confirm and OpenAI disputes (source 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha).
- `campaign:famoussparrow-azerbaijan-2026`: summary "novel two-stage export-gated" → "evolved two-export DLL sideloading"; move alias "UAT-9244" to `actor:famoussparrow` (THN: "FamousSparrow (aka UAT-9244)"); add relation `{to: actor:famoussparrow, type: attributed-to, source: 2026-05-14/famoussparrow-three-wave-intrusion-of-an-azerbaijani-energy, note: Bitdefender, moderate-to-high confidence}`. New entities, then key them on that entry: `malware:deed-rat` ("Deed RAT", modular backdoor loaded through a two-export DLL sideload; Bitdefender 2026-05-13), `malware:terndoor` ("TernDoor", backdoor whose execution chain loads a Windows driver; assessed in wave 2; Bitdefender, Cisco Talos UAT-9244), `malware:mofu-loader` ("Mofu Loader", shellcode loader documented by JPCERT; Bitdefender); relations on the campaign `uses` each, source the same entry.
- `campaign:frostyneighbor-2026-05-campaign`: summary should say "since March 2026 against governmental organisations in Ukraine" (not Poland, Lithuania and Ukraine); its aliases Ghostwriter and UNC1151 are actor names. New `actor:frostyneighbor`: name "FrostyNeighbor", aliases Ghostwriter, UNC1151, UAC-0057, TA445, PUSHCHA, Storm-0257, nexus null, summary "Long-running cyberespionage group apparently aligned with Belarus (ESET), active since at least 2016 per Mandiant, using PicassoLoader downloaders to deliver Cobalt Strike against Ukraine, Poland and Lithuania", first_seen 2026-10-21; relation on the campaign `{to: actor:frostyneighbor, type: attributed-to, source: 2026-05-15/frostyneighbor-ghostwriter-unc1151-belarus-state-aligned-ese}`; then key the actor on that entry.
- New actor for the Clinical Diagnostics breach: `actor:nova-raas`, name "Nova", ambiguous_labels ["Nova"], summary "Ransomware-as-a-service operation using the RaLord ransomware, which threatened in July 2025 to leak data stolen from the Dutch lab Clinical Diagnostics (GovInfoSecurity, 2025-09-03)"; relation on `incident:clinical-diagnostics-nmdl-igj-2026` `{to: actor:nova-raas, type: attributed-to, source: 2026-05-14/dutch-igj-rules-clinical-diagnostics-nmdl-failed-nen-7510-in}`; then key it on that entry.
- `trend:amd-sb-7052`: summary implies a Windows update mitigates every part; suggested: "Zen 2 op-cache corruption (CVE-2025-54518): OS updates for EPYC 7002, OEM BIOS updates with AMD's PI versions for Ryzen-class parts, Xen XSA-490."

## cves_seen changes for the main agent

Add (missing; the `cve-sync` FAIL names them):
- CVE-2026-33827: Windows TCP/IP race-condition use-after-free RCE (tcpip.sys, CVSS 8.1, April 2026), found by Microsoft MDASH; primary https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33827.
- CVE-2026-8111: Ivanti Endpoint Manager web-console SQL injection to RCE before 2024 SU6 (CVSS 8.8); https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-29491.
- CVE-2026-8051: Ivanti Virtual Traffic Manager admin OS command injection before 22.9r4 (CVSS 7.2); https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-29488.
- CVE-2026-45545: Nextcloud Tables SQL injection in the column-type parameter (High 8.2); https://github.com/nextcloud/security-advisories/security/advisories/GHSA-x43f-gmgh-vvjj.
- CVE-2026-45156: Nextcloud User OIDC missing JWT signature verification in ID4me handling (High 8.1); https://github.com/nextcloud/security-advisories/security/advisories/GHSA-qqgv-fqwp-mjpp.
- CVE-2026-45286: Nextcloud Calendar attendee-suggestion endpoint leaked user identifiers (Moderate 4.3); https://github.com/nextcloud/security-advisories/security/advisories/GHSA-r697-74m9-gvf2.

Bump `last_seen` to 2026-10-21 (records added or changed by these records): CVE-2026-45321, CVE-2026-8043, CVE-2026-45691, CVE-2026-45690, CVE-2026-45793, CVE-2022-41040, CVE-2022-41082, CVE-2025-54518, CVE-2026-33824, CVE-2026-41089, CVE-2026-41096, CVE-2024-55591, CVE-2025-32433, CVE-2025-33073, CVE-2026-33634.

Title corrections suggested: CVE-2026-33634 is "Aqua Security Trivy embedded malicious code (malicious v0.69.4 release and trivy-action tags, 2026-03-19)", not the Checkmarx Jenkins plugin (primary https://github.com/advisories/GHSA-69fq-xp46-6x23); CVE-2025-32433 is a CVE The Gentlemen evaluated a proof of concept for, not one "confirmed as initial-access"; CVE-2026-45690 is a Nextcloud second 2FA bypass by pending session token replay (Moderate 5.9), not an SQL injection; CVE-2026-45691 is not pre-authenticated (password required); CVE-2026-8043 is file read and HTML write, information disclosure.

## Residuals noticed (not fixed)

- `campaign:teampcp-shai-hulud-copycat-wave-ox-security-checkmarx-pcpja` summary repeats "third in three months" for the Checkmarx plugin and groups PCPJack with TeamPCP tooling.
- `actor:thegentlemen` summary calls FortiGate CVE-2024-55591 "the initial-access funnel"; Check Point's leak analysis shows the CVE tracked, not exploited.
- `incident:openai-dsewiki-agent-collusion-2026-05` and `tool:gemstuffer-rubygems-2026` summaries contain em dashes.
- The GemStuffer September `.yardopts` evidence quote may need a re-check against the live page (the saved extract breaks it with a markdown link).
- The vm2 (2026-05-20) and PinTheft (2026-05-21) entries also fail `cve-sync` (other workers' batches).
