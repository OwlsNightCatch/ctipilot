# Repair worker 4, cleanup wave 04 (2026-10-21T1148Z-audit)

**Model:** Opus 5.5 (`claude-opus-5-5`). Inputs: truth-4.yaml / truth-4.md / truth-4.claims.yaml, saved bodies under truth-4/bodies/, fresh reads under repair-4/src/ (Keycloak GitHub issues, Red Hat CVE pages and errata linked from RHSA-2026:19596, EUVD-2026-31267, CISA KEV alert of 2026-05-20 via WebFetch). Section and summary files: repair-4/rec/. The session stopped once on an API limit after the Nx Console record and resumed at Sparx.

**Totals:** 18 records (16 correction, 2 improvement), 1 entry without a record (the fold duplicate, untouched). Every record's `fields` equals `entry_record.py diff`; every new evidence quote was checked verbatim against its saved body (repair-4/qcheck.py). `check_run.py --all`: no FAIL or WARN on my entries except the expected missing-run-record warning and `cve-sync` for the 14 CVE ids listed under State changes. Em-dash and self-reference sweep over reader text: clean. Labelled lines present on every repaired entry (Exposure, Detection, Triage where an honest discriminator exists, Defender takeaway). `actions[]` is empty on all 18: none of the May tasks is still a do-now task.

## Per entry

### 2026-05-20/cve-2026-41091-microsoft-defender-engine-link-following-eop
correction, 2026-10-21T16:01:33Z. fields: actions, affected_products, body, classification, cves, evidence, headline, sources, sourcing_note, summary, tags, techniques, title, verification.
Applied (MSRC CVE-2026-41091/45498, Microsoft Learn remediation page, Vectra, Help Net, THN, BleepingComputer, CISA alert https://www.cisa.gov/news-events/alerts/2026/05/20/cisa-adds-seven-known-exploited-vulnerabilities-catalog): "Turn off routine remediation" GPO claim removed (it controls remediation, not updates); engine and platform fixes stated as separate updates, "combined out-of-band" removed; CVE-2026-45498 typed dos/pre-auth with Platform builds; affected/fixed filled; unsourced Sysmon hunts replaced by Huntress/Vectra behavior; RedSun/UnDefend mapping per researcher; self-quoting evidence replaced; KEV listing cited to CISA. The 2026-05-22 update section was rewritten in place to its own timestamp (no MsMpEng.exe, standard-user or Sysmon claims).
Declined: adding CVE-2026-45584 to cves[] or linking the two entries (coordinator: distinct flaws, no link); the action that named it is dropped instead.
Legacy: A/1 (MSRC + CISA KEV + Huntress); T1068, T1687, T1033, T1036; products Defender Antivirus, Malware Protection Engine, SCEP, Security Essentials; Triage present.

### 2026-05-20/cve-2026-45584-microsoft-defender-engine-heap-buffer-overflo
correction, 2026-10-21T16:03:10Z. fields: affected_products, body, classification, cves, evidence, headline, sources, sourcing_note, summary, techniques, title.
Applied (https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45584): not zero-click (user-interaction: local user must act, AC:H); "Defender process context" dropped; not exploited / not publicly disclosed cited to MSRC; affected/fixed Engine builds.
Declined: vector "network" (not in the taxonomy; `user-interaction` encodes the stated user step). Legacy: A/2; T1203; Detection omitted (no source gives one).

### 2026-05-20/drupal-core-highly-critical-pre-patch-warning-unauthenticate (fold survivor)
correction, 2026-10-21T16:06:42Z. fields: actions, affected_products, body, classification, cves, evidence, headline, immediate_action, kind, regions, sectors, sources, sourcing_note, summary, tags, techniques, title.
Applied (SA-CORE-2026-004, PSA-2026-05-18 WebFetch body, risk-levels page, EUVD-2026-31153, Imperva, Searchlight, CSO, Register, BleepingComputer, bk.admin.ch): retitled around CVE-2026-9082, kind threat to vulnerability; CVSS 9.8 (CNA via EUVD; 6.5 is NIST); type sqli; affected/fixed per SA; 20/25 is the top tier, raised to 23/25 on 2026-05-22; Drupal Steward protection pre-patch; only 9.x/8.9 manual patches (11.1.10/10.4.10 are releases); exploitation quote binding (PSA, not SecurityWeek); Imperva counts are attempts, mostly probing, Gaming/Finance targets; Swiss/EU/SWITCH prevalence and targeting claims removed (SS Web is Livingdocs); "swap the backend" control removed; KEV cited to the KEV catalog feed; both earlier update sections rewritten to their timestamps without brief self-references or the unsourced "Defender takeaway" block. Priority kept critical on the 2026-05-20/22 facts; immediate_action rewritten to the verified fixed versions and Steward caveat.
Declined: EPSS from EUVD (15.7 is not stated as a probability). Legacy: A/1; T1190, T1595.002; product Drupal Core; Triage present.

### 2026-05-20/huawei-vrp-enterprise-router-zero-day-caused-post-luxembourg
correction, 2026-10-21T16:08:00Z. fields: body, classification, entities, evidence, headline, sources, sourcing_note, summary, tags, techniques, title.
Applied (https://therecord.media/huawei-zero-day-behind-last-year-luxembourg-telecom-outage, Paperjam, Security Affairs): "VRP" dropped as the vulnerable software; no-target finding attributed to the High Commission for National Protection; zero-day label hedged to anonymous sources; nation-state and no-patch tags dropped; summary finished; entity keyed.
Legacy: B/2; T1499.004; no Triage (no honest discriminator).

### 2026-05-20/nx-console-vs-code-extension-2-2-m-installs-compromised-via
correction, 2026-10-21T16:09:47Z. fields: affected_products, body, classification, entities, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title.
Applied (GHSA-c9j4-9m59-847w, https://nx.dev/blog/nx-console-v18-95-0-postmortem, StepSecurity, THN): windows 12:30-12:48 (Marketplace) / 12:33-13:09 (Open VSX); contributor GitHub CLI token stolen via TanStack; 2.2M is the extension total, 28 installs / ~6,000 activations; RSA/persistent clause cited to StepSecurity; upload passed Microsoft's checks; event_date 2026-05-18; GHSA and postmortem added as primaries.
Declined: StepSecurity's "stolen VSCE_PAT at 12:36" (conflicts with Nx's own account). Legacy: A/1; T1195.002, T1528, T1059.007, T1552.001, T1552.005, T1555.005, T1102.001, T1543.001, T1548.003, T1041.

### 2026-05-20/prepare-emergency-drupal-patch-window-for-today-17-00-21-00 (fold duplicate)
No record, not edited (diff empty). Verified one finding with the survivor: same PSA-2026-05-18, same two primaries, no sourced fact the survivor lacks (its change-control advice is unsourced; its NCSC quote was already in the survivor's history).

### 2026-05-20/sparx-enterprise-architect-pro-cloud-server-five-cve-chain-p
correction, 2026-10-21T20:20:24Z. fields: actions, affected_products, body, classification, cves, evidence, headline, priority, regions, sectors, sources, sourcing_note, summary, tags, techniques, title, verification.
Applied (https://cert.pl/en/posts/2026/05/CVE-2026-42096/, sploit.tech, CCB, GitHub br0xpl/sparx_hack, Sparx PCS 6.5 history): per-CVE CNA CVSS 4.0 scores (via CCB), types and auth; CWE-228 for 42100; "SQL injection" recast as unauthorized SQL execution; bypass endpoint `/SparxCloudLink.sseap` without `model`; chained 10.0 attributed to the researcher; PoC caveat (no working key); prevalence claim dropped; no-patch recast as "no fix at disclosure" plus unmapped PCS 6.5 fixes (status no-patch removed, fixed "not stated by the vendor"). Priority high to notable (no sourced constituency exposure, unexploited).
Declined: wrong EUVD range text was simply dropped (EUVD-2026-30931 kept as a source). Legacy: A/2; T1190, T1499.004; Triage present.

### 2026-05-20/storm-2949-sspr-to-key-vault-azure-kill-chain (deep dive)
correction, 2026-10-21T20:22:14Z. fields: body, classification, event_date, evidence, headline, regions, sectors, sources, sourcing_note, summary, tags, techniques, title, verification.
Applied (https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/, BleepingComputer, Microsoft Learn SSPR reporting): not "financially motivated"; ScreenConnect / Defender tampering / log clearing restore the endpoint phase; four accounts; hedged SSPR phishing; Key Vault and publishing-profile wording per Microsoft; production web app takeover added; Self-Service Password Management audit category; unsourced operation names, Hardening assertions, prevalence sentence and organized-crime tag dropped; all prose T-ids removed (T1562.007 was revoked); sectors [] and regions [global]; event_date 2026-05-18.
Legacy: B/2; 24 ids (T1621, T1078.004, T1556.006, T1098.005, T1087.004, T1098.001, T1530, T1213.002, T1555.006, T1686.001, T1651, T1136.001, T1552.005, T1685, T1219, T1036.004, T1685.005, T1070.003, T1070.004, T1082, T1087.002, T1069.002, T1552.001, T1552.004).

### 2026-05-20/thegentlemen-raas-lists-czech-university-and-swiss-engineeri
correction, 2026-10-21T20:23:38Z. fields: body, classification, confidence, entities, event_date, evidence, headline, priority, references, sources, sourcing_note, summary, tags, techniques, title, verification.
Applied (DeXpose x2, ransomware.live, https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/): both listed 2026-05-18; CPR dated 2026-05-13, "TTPs unchanged" claim dropped; edge-device entry per CPR (FortiGate/Cisco), not SD-WAN; Ziefen cited to ransomware.live; "UPDATE (originally covered ...)" and "as of this brief" removed; `references` to 2026-05-14/the-gentlemen-raas-backend-rocket-database-leaked-16-22-gb-c (coordinator instruction; the 05-14 entry was not touched); actor:thegentlemen keyed; priority notable to routine (unconfirmed leak-site claim).
`possible_twin_outside_batch`: 2026-05-14/the-gentlemen-raas-backend-rocket-database-leaked-16-22-gb-c, nothing changed for the note beyond the instructed reference. Legacy: C/3; T1657.

### 2026-05-20/vm2-node-js-sandbox-12-critical-cves-cve-2026-43997-43999-44
correction, 2026-10-21T20:26:55Z. fields: affected_products, body, classification, cves, event_date, evidence, headline, sectors, sources, sourcing_note, summary, techniques, title, verification.
Applied (THN 2026-05-07, BSI WID-SEC-2026-1583 CSAF, GHSA-47x8/947f/qcp4/v6mx, wave-2 GHSA bodies, Kodem 2026-05-14): two waves separated (12 CVEs fixed by 3.11.2; BSI's set of 2026-05-18 fixed in 3.11.4); 21 CVE records with GHSA versions and scores (status poc-public only where the saved GHSA shows a PoC section); bullets rewritten per GHSA titles; Kodem quote replaced by attribution; uncited prevalence/n8n/no-workaround claims dropped; unrelated CVE table removed; event_date 2026-05-18.
Declined: CVE-2026-92956 / 92962 (added to BSI in September, outside the finding); CVE-2026-47141 cvss left "n/a" (GHSA gives only Moderate). Legacy: A/2; T1190, T1059.007; Triage present.

### 2026-05-21/b1ack-s-stash-carding-marketplace-publicly-releases-4-6m-car
improvement, 2026-10-21T20:28:19Z. fields: body, classification, entities, event_date, evidence, headline, sources, sourcing_note, summary, tags, techniques, title, verification.
Applied (https://socradar.io/blog/b1acks-stash-4-6-million-stolen-credit-cards-free/, Security Affairs): storefront and cross-wave root-cause claims dropped; 4.3M cited to Security Affairs; 8M suspended; headline/summary finished; cryptocrime tag dropped; event_date 2026-05-18; campaign entity keyed. Legacy: B/2; T1657.

### 2026-05-21/cve-2026-42822-microsoft-azure-local-disconnected-operations
correction, 2026-10-21T20:29:01Z. fields: actions, affected_products, body, classification, cves, evidence, headline, priority, sources, sourcing_note, summary, tags, techniques, title.
Applied (https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-42822): insider-realistic attacker; "cloud-managed Azure already protected" removed; full system update via Azure portal; fixed ALDO 2604; Bundesverwaltung claim dropped; priority high to notable.
Declined: vector "network (internal)" (taxonomy; kept zero-click/pre-auth per CVSS PR:N UI:N). Legacy: A/2; T1068, T1078.

### 2026-05-21/cve-2026-45829-chromadb-python-fastapi-server-pre-auth-rce-v
correction, 2026-10-21T20:30:26Z. fields: actions, affected_products, body, classification, cves, evidence, headline, sectors, sources, sourcing_note, summary, techniques, title.
Applied (https://hadrian.io/blog/cve-2026-45829----chromadb-python-server-hands-you-rce-before-it-asks-who-you-are, BleepingComputer): server-wide trust_remote_code setting removed; 500 vs 403 stated; HiddenLayer discoverer/scorer vs Hadrian analysis; report-date conflict stated; headline finished; education sector dropped; affected/fixed.
Deviation: classification B/1, not the truth pass's B/2: Hadrian ran its own proof of concept, an independent assessment beside HiddenLayer's. PyPI still lists 1.5.9 as latest (read 2026-10-21) but no citable page states it, so reader text keeps "no fix as of 2026-05-19". Legacy: T1190, T1059.006; Triage present.

### 2026-05-21/keycloak-26-6-2-16-cves-including-oidc-session-fixation-cve
correction, 2026-10-21T20:33:44Z. fields: actions, affected_products, body, classification, cves, entities, event_date, evidence, headline, regions, sectors, sources, sourcing_note, summary, tags, techniques, title, verification.
Applied (Keycloak release notes, BSI WID-SEC-2026-1612 CSAF, Red Hat CVE pages for 7507/37982/37979/4630/37978, GitHub issue #48388, RHSA-2026:19594 and :19596): 4630 is a same-realm cross-resource-server IDOR; 7507 mechanism via /login-actions/restart; Red Hat CVSS per CVE with vectors/auth; 16 issues / 18 ids; BSI nine CVEs rated high (released 2026-05-19 22:00 UTC); RHBK fixed in 26.2.16 / 26.4.12; actor:akira removed; unrelated CVE table removed; prevalence and /auth path claims dropped.
Declined: records for the other 12 ids (third-party and lower-impact items stay unrecorded). Legacy: A/2; T1185, T1098.005, T1212.

### 2026-05-21/pintheft-linux-kernel-local-privilege-escalation-primitive-r
improvement, 2026-10-21T20:35:19Z. fields: affected_products, body, classification, cves, event_date, evidence, headline, kind, sources, sourcing_note, summary, techniques, title, verification.
Applied (https://www.openwall.com/lists/oss-security/2026/05/19/6, BleepingComputer, EUVD-2026-31267): Arch-only finding narrowed to "among the distributions V12 tested", CONFIG_RDS + CONFIG_RDS_TCP; discoverer/relay roles; CVE-2026-43494 record added (kernel CNA fix for the same rds_message_zcopy_from_user() op_nents double drop, cited to EUVD; no source names PinTheft and the CVE together, so the body states the shared fix, not a vendor mapping); unsourced auditd/Sysmon hunts replaced by the exploit's sequence; module-blocking mitigation; kind research to vulnerability. Legacy: B/2; T1068.

### 2026-05-21/sonicwall-gen6-ssl-vpn-incomplete-patching-cve-2024-12802-ak
correction, 2026-10-21T20:37:36Z. fields: affected_products, body, classification, cves, entities, event_date, evidence, headline, regions, sectors, sources, sourcing_note, summary, tags, techniques, title.
Applied (https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0001, https://reliaquest.com/blog/threat-spotlight-vpn-exploitation-when-patched-doesnt-mean-protected/, Cybersecurity Dive, BleepingComputer): CVSS 6.5 vendor / 9.1 CISA-ADP, post-auth; affected/fixed builds; unattributed, likely IAB, Akira only as comparison, actor:akira removed; six steps cited to BleepingComputer's listing of the advisory (KB id dropped); sess="CLI", Event IDs 238/1080, CLI-to-GMS as detection; ReliaQuest added as primary; event_date 2026-05-19; self-quoting evidence replaced. Legacy: B/2; T1110, T1133, T1556.006, T1078, T1021.001, T1685; Triage present.

### 2026-05-21/verizon-2026-dbir-vulnerability-exploitation-overtakes-crede
correction, 2026-10-21T20:39:13Z. fields: body, classification, deep_dive, deep_dive_category, entities, event_date, evidence, headline, kind, priority, sectors, sources, sourcing_note, summary, techniques, title, verification.
Applied (DBIR PDF https://www.verizon.com/business/resources/T1f0/reports/2026-dbir-data-breach-investigations-report.pdf, Help Net, press release): dataset counts and Nov 2024 to Oct 2025 window; TeamPCP / Mini Shai-Hulud sentence and entities removed; 26% KEV remediation recast; 13%/31% cited to the PDF with the pretexting methodology caveat (16% without it); three-cycle and pivot-point claims dropped; landing page replaced by the PDF; self-references removed; kind annual-report, priority high to notable, deep dive off. Legacy: B/2; T1190, T1078; Exposure/Detection omitted (statistics report, nothing specific).

### 2026-05-21/webworm-china-aligned-shifts-to-eu-government-targets-echocr
correction, 2026-10-21T20:41:34Z. fields: body, classification, cves, evidence, headline, sources, sourcing_note, summary, techniques, title, verification.
Applied (https://www.welivesecurity.com/en/eset-research/webworm-new-burrowing-techniques/, THN): related groups not aliases (Space Pirates tenuous); pre-created Discord channels; S3 bucket as compromised third-party, taken down, hostname removed; SharpSecretsdump only uploaded; CVE-2017-7692 record added; mapping taken from ESET's own ATT&CK table (all ids active in v20) plus T1105 (curl downloads).
Declined: T1003.001/.002/.004 (tool only uploaded) and T1078 (ESET's hedged assumption about the Serbian credentials). Legacy: B/2; 30 ids.

### 2026-05-22/calypso-red-lamassu-bronze-medley-deploys-showboat-linux-and
correction, 2026-10-21T20:43:20Z. fields: body, classification, event_date, evidence, headline, regions, sources, sourcing_note, summary, techniques, title.
Applied (Lumen https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms dated 2026-05-20, PwC 2026-05-21): victims per Lumen (Afghanistan ISP, Azerbaijan; US potential; Donbas a separate cluster), europe region dropped; kworker is PwC's name, masquerade and kthreadd hunt dropped; campaign since mid-2022 vs actor since 2019; JFMBackdoor capabilities (TCP proxying, screenshots); certificate clusters C2 nodes; T1574.002 (revoked) replaced by T1574.001; prose ids removed; headline finished; Lumen dated 2026-05-20. Repaired on its own facts; no reference to the twin 2026-05-22/red-lamassu-calypso-bronze-medley-showboat-jfmbackdoor-telco (W4-07), which was not touched. Priority kept high. Legacy: B/1; T1059.004, T1090.001, T1105, T1543.002, T1564, T1132.001, T1574.001, T1140, T1620, T1113, T1070.006.

## Folds and links

- fold: 2026-05-20/drupal-core-highly-critical-pre-patch-warning-unauthenticate <- 2026-05-20/prepare-emergency-drupal-patch-window-for-today-17-00-21-00
- link: 2026-05-20/thegentlemen-raas-lists-czech-university-and-swiss-engineeri `references` 2026-05-14/the-gentlemen-raas-backend-rocket-database-leaked-16-22-gb-c (distinct events: new leak-site listings vs the backend database leak; coordinator instruction).
- No link between the two Defender entries (distinct flaws). No link from the Showboat entry to its twin in another wave.

## Registry changes for the main agent (entities/registry.yaml)

1. `incident:huawei-vrp-enterprise-router-zero-day-post-luxembourg-2025-o` (now keyed by the Huawei entry): name "POST Luxembourg outage (Huawei router zero-day)"; summary "An attack exploiting a previously unknown vulnerability in Huawei enterprise router software caused POST Luxembourg's nationwide telecom outage on 23 July 2025; no CVE or public advisory had been issued ten months later (The Record, 2026-05-19)."
2. `incident:nx-console-vs-code-extension-18-95-0-compromised-stolen-publ` (now keyed): summary "Malicious Nx Console 18.95.0, published on 2026-05-18 with a core contributor's GitHub CLI token stolen in the TanStack npm compromise, was live 12:30 to 12:48 UTC on the Visual Studio Marketplace and 12:33 to 13:09 UTC on Open VSX, shipping a multi-channel credential stealer and a Python backdoor (Nx, 2026-05-21)."
3. `trend:sparx-enterprise-architect-pro-cloud-server-five-cve-chain-c`: summary "Five CVEs in Sparx Systems Pro Cloud Server (through 6.1) and Enterprise Architect (through 17.1), CVE-2026-42096 to -42100: unauthenticated SQL execution by omitting the model parameter, unrestricted SQL for low-privileged users, a WebEA race to code execution, client-side authentication and a DoS; researcher-chained CVSS 4.0 10.0, public PoC, no vendor fix at disclosure (CERT Polska, 2026-05-19)."
4. `actor:storm-2949`: summary "Microsoft's temporary designation for an actor that took over privileged Entra ID accounts through SSPR abuse and pursued mass data exfiltration across Microsoft 365 and Azure; no extortion observed and no link to ShinyHunters (Microsoft, 2026-05-18; BleepingComputer, 2026-05-19)." (drop "financially motivated", "voice-phishing").
5. `campaign:storm-2949-sspr-to-key-vault-azure-cloud-wide-kill-chain`: summary "Storm-2949's SSPR-abuse intrusion: four privileged Entra ID accounts taken over, then App Service publishing profiles, Key Vault secrets, SQL and Storage data, VM Run Command and VMAccess, and ScreenConnect on VMs (Microsoft, 2026-05-18)." (drop "malware-less", "voice-phishing").
6. `trend:pintheft-linux-kernel-rds-zerocopy-iouring-lpe-no-cve-arch-d`: summary "Linux kernel LPE turning an RDS zerocopy double-free into a page-cache overwrite of a SUID-root binary through io_uring fixed buffers; public PoC by V12 Security (2026-05-19), kernel fix published as CVE-2026-43494 on 2026-05-21; RDS is default only on Arch Linux among the distributions V12 tested." (key stays.)
7. `campaign:b1ack-stash-46m-card-dump-may-2026-third-free-release-wave` (now keyed): replace "SOCRadar attributes the collection to" with "SOCRadar assesses the data likely comes from".
8. `report:verizon-2026-dbir-exploitation-overtakes-credentials`: replace "supply-chain breaches +60% YoY" with "breaches involving a third party +60%", and add "2025 data (November 2024 to October 2025)".
9. `actor:webworm-fishmonger-aquatic-panda-eset-echocreep-graphworm-eu`: aliases FishMonger, Aquatic Panda, SixLittleMonkeys and Space Pirates are not Webworm's names (ESET links Webworm to SixLittleMonkeys and FishMonger as related groups; THN: FishMonger aka Aquatic Panda; ESET calls the Space Pirates link tenuous). Main agent's call on removing them; if FishMonger and SixLittleMonkeys get actor records, add `overlaps-with` relations from Webworm, source 2026-05-21/webworm-china-aligned-shifts-to-eu-government-targets-echocr. Summary: "China-aligned APT active since at least 2022 that moved to European governmental targets in 2025 (Belgium, Italy, Serbia, Poland) with the EchoCreep (Discord) and GraphWorm (Microsoft Graph and OneDrive) backdoors (ESET, 2026-05-20)."
10. New actor entity proposed: key e.g. `actor:red-lamassu`, type actor, name "Red Lamassu", aliases ["Calypso", "Bronze Medley"] (Calypso per PwC, Bronze Medley per THN), nexus china-nexus, summary "China-based threat actor likely operating from Sichuan Province that PwC has tracked since 2019 against telecommunications organisations in Asia, chiefly Kazakhstan, Afghanistan and India; PwC attributes the JFMBackdoor operation and its Showboat (kworker) sample to it (PwC, 2026-05-21)." Relation on `campaign:calypso-red-lamassu-showboat-jfmbackdoor-linux-windows-telco`: {to: actor:red-lamassu, type: attributed-to, source: 2026-05-22/calypso-red-lamassu-bronze-medley-deploys-showboat-linux-and, note: "PwC attribution; Lumen says only PRC-aligned clusters"}; the campaign's aliases "Red Lamassu"/"Bronze Medley" are actor names. Coordinate with the twin's worker (W4-07). I did not key it (no such key yet).
11. Products new to the registry (product sync): "Microsoft Azure Local Disconnected Operations", "Sparx Systems Pro Cloud Server", "Sparx Systems Enterprise Architect", "vm2", "ChromaDB".

## state/cves_seen.json changes for the main agent

Add (first_seen and last_seen 2026-10-21):
- CVE-2026-24118, -24120, -24781, -26332, -44007 (vm2 first wave): primary_source_url https://thehackernews.com/2026/05/vm2-nodejs-library-vulnerabilities.html; titles e.g. "vm2 sandbox escape via __lookupGetter__ (CVSS 9.8, fixed 3.11.0)", "vm2 Promise species patch bypass of CVE-2023-37466 (9.8, fixed 3.10.5)", "vm2 sandbox escape via inspect (9.8, fixed 3.11.0)", "vm2 sandbox escape via SuppressedError (9.8, fixed 3.11.0)", "vm2 improper access control sandbox escape (9.1, fixed 3.11.1)".
- CVE-2026-47131, -47135, -47137, -47139, -47140, -47141, -47208, -47209 (vm2 second wave): primary_source_url https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1583; title "vm2 sandbox escape, affects 3.11.3 and earlier, fixed 3.11.4 (WID-SEC-2026-1583)" with the GHSA title per id (repair-4 vm2 cves[] has the scores).
- CVE-2026-43494: primary_source_url https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-31267; title "Linux kernel net/rds zerocopy op_nents double drop (PinTheft), CVSS 7.8".
Bump last_seen to 2026-10-21 (records changed by these repairs): CVE-2026-41091, -45498, -45584, -9082, -42096, -42097, -42098, -42099, -42100, -26956, -43997, -43999, -44005, -44006, -44008, -44009, -47210, -42822, -45829, -7507, -37982, -37979, -4630, -37978, -6856, CVE-2024-12802, CVE-2017-7692. Stale titles worth replacing: CVE-2026-43997 ("host Object obtained despite earlier protections; fixed 3.11.0"; the getPrototypeOf wording belongs to CVE-2026-44006), CVE-2026-9082 (drop "highly-critical pre-auth" framing if desired; add CVSS 9.8, 23/25).

## Residuals noticed (not fixed)

- `campaign:fishmonger-isoon-sprysocks-windows-kernel-rootkit` carries `attributed-to actor:webworm-...` because FishMonger was registered as a Webworm alias; ESET treats them as distinct, so that edge (source 2026-06-17/fishmonger-i-soon-ports-its-sprysocks-backdoor-to-windows-wi) is likely wrong.
- `incident:drupal-core-highly-critical-pre-patch-warning-psa-2026-05-18` is keyed by no entry and its summary is stale ("no CVE at announcement").
- The Drupal duplicate keeps its own errors until folded (second-highest tier, 10.4/11.1 manual patches, no mitigation).
- `actor:thegentlemen` summary's "FortiGate CVE-2024-55591 as the initial-access funnel" was not checked against this batch's sources.
- A later entry, 2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands, keys the same Nx incident; not reviewed.
- Several new source records (Drupal risk-level page, three vm2 GHSA pages, four Red Hat CVE pages, Keycloak issue #48388, Sparx PCS history) carry `date: null` because the saved pages show no date.
