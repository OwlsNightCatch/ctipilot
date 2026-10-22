BLOCKER: 2026-05-16/bka-arrests-dream-market-lead-administrator-speedstepper-in (kind: threat) has no `techniques` key and none was added. Its sources (DEA/DOJ release = IRS-CI release, The Record) describe a law-enforcement action: an indictment and German charges for laundering Dream Market commission proceeds (2022 transfers of dormant marketplace wallets into new consolidated wallets, 2023 gold purchases through an Atlanta crypto service provider, searches locating gold, cash and identified accounts). Marketplace users reached the site over Tor, but no source describes an intrusion, an access vector or attacker behavior against a victim estate. The gate did not FAIL it (legacy run id); the main agent decides whether to keep the entry as is, re-kind it, or drop it.

# Repair worker 3, cleanup wave 04 (2026-10-21T1148Z-audit)

**Model:** Opus 5.5 (`claude-opus-5-5`)

Inputs: truth-3.yaml / truth-3.md / truth-3.claims.yaml and truth-3/bodies/. Fresh fetches are under repair-3/src/: certpl-44088.txt and .html (the full CERT Polska sentence; the saved extract was cut off), ghsa-x3h8.html (confirms OpenClaw rates CVE-2026-44115 "moderate"), jb-teamcity-2023-09.txt (JetBrains CVE-2023-42793 advisory), kev.json (CISA KEV catalogue 2026.10.21), the EUVD records euvd-EUVD-2026-29986 (F5), -30936 (FunnelKit), -25528 (CVE-2026-31635), -44996/-44997/-44998 (BigBlueButton) and euvd-search-*.json.

All 20 entries carry exactly one `correction` record from this run, each with a `## Correction — <at>` section. In every entry `entry_record.py diff` agrees with the record's `fields`. `check_run.py --all` raises no FAIL or WARN on these entries beyond the expected "run id has no run record" WARN (entry-updates, 20×). The one store-wide FAIL that touches the batch is `cve-sync`, because CVE-2026-47100 is missing from state/cves_seen.json (see State changes). No `update` records were written, and `updated_at` is unchanged everywhere: 7-Eleven keeps 2026-05-25T05:00:03Z from its earlier update record.

Common legacy duties on all 20: Admiralty `classification` set, `techniques[]` validated mechanically against the pin (all ids active; the revoked T1574.002 was replaced), labelled lines written from the sources, `affected_products[]` added where product-specific, citations dated to each page's own date, `sources[].date` added, evidence quotes replaced by contiguous verbatim sentences (`grep -F` checked against saved or fresh bodies), em dashes removed from reader text, self-reference removed ("Why it matters to us", "Reference: §", "[SINGLE-SOURCE]", "covered 2026-05-15", "UPDATE (originally covered ...)" per the coordinator), and stale `actions[]` emptied. Not one of these May actions is still a do-now task.

## Per entry

### 1. 2026-05-16/bka-arrests-dream-market-lead-administrator-speedstepper-in
- correction at 2026-10-21T16:04:38Z; fields: body, classification, entities, event_date, evidence, headline, sources, sourcing_note, summary, title
- Applied (https://www.dea.gov/press-releases/2026/05/13/german-citizen-charged-laundering-funds-linked-prominent-darknet, https://therecord.media/dream-market-admin-arrested-in-germany):
  - Coordinated German and US arrest on German charges (not "BKA arrests"). The case is investigated by IRS-CI and DEA Miami with the BKA and ZKI Oldenburg assisting; FBI, USPIS and HSI were the 2016-2022 task force.
  - Transfers went to new consolidated wallets, and the searches located funds rather than seizing $1.2M in crypto.
  - Only the US indictment ties Andresen to the administrator role; the "definitive link" claim and the "increasingly" generalisation were dropped, and every clause is now cited.
  - The truncated summary was completed; The Record and event_date set to 2026-05-13.
- Declined: none. Techniques: BLOCKER above.
- Legacy: A/2; techniques none (BLOCKER); labelled lines: Defender takeaway only (sources give no exposure or detection); entities + incident:dream-market-admin-arrest-2026-05.

### 2. 2026-05-16/cve-2026-44112-cve-2026-44113-cve-2026-44115-cve-2026-44118 (OpenClaw)
- correction at 2026-10-21T16:07:24Z; fields: actions, affected_products, body, classification, cves, evidence, headline, priority, sources, sourcing_note, summary, techniques, title
- Applied (Cyera blog, OpenClaw GHSA-wppj/-5h3g/-x3h8/-r6xh, VulnCheck advisories):
  - CVE-2026-44115 is a heredoc shell-expansion bypass.
  - The 245K sum was removed: Cyera's 65K (Shodan) and 180K (Zoomeye) are separate counts.
  - Chain order follows Cyera; the "human-attacker" phrase was dropped.
  - Every cves[] record now carries affected (≤ 2026.4.21) and fixed (2026.4.22), with types per flaw (path-traversal, info-disclosure, logic-flaw, priv-esc).
  - CVSS is attributed per scorer (Cyera 3.1, VulnCheck 4.0, OpenClaw moderate for 44115, checked on the raw advisory page).
  - "Originally launched as Clawdbot"; the headline is complete; the no-exploitation line is stated as "neither Cyera nor the vendor advisories report exploitation".
  - priority high→notable; the stale action was dropped.
- Declined:
  - The vector stays `local` on all four. Every step of Cyera's chain presupposes code execution inside the OpenShell sandbox; the CNA's AV:N reflects agent-mediated input. The vocabulary has no "network" value, and zero-click would overstate.
  - Vendor "High" severity for 44112 was not stated: the GHSA sidebar is not in the saved body, and only 44115 was verified raw.
- Legacy: A/2; T1195.002, T1068, T1005, T1552.001, T1059.004; Exposure, Detection (with the post-patch secret-rotation step), Defender takeaway; affected_products "OpenClaw".

### 3. 2026-05-16/sentinelone-living-off-the-pipeline-ci-cd-subversion-taxonom
- correction at 2026-10-21T16:09:54Z; fields: affected_products, body, classification, confidence, cves, evidence, headline, sectors, sources, sourcing_note, summary, techniques, title
- Applied (https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/; JetBrains 2023-09 and 2023-10-18 advisories):
  - The monitoring list is now SentinelOne's own; the invented event name, IP-range criterion and binaries are gone.
  - T1547/T1555 were replaced by the supported set.
  - Rewritten as examples, not a "taxonomy of three cases". Rogue runners and comment triggers are attributed to Sha1-Hulud, and install-time reconnaissance scripts are described as such.
  - Contagious Interview's run-this-command mechanism was added and the over-privilege gloss dropped.
  - CVE-2023-42793 added to cves[] (unauthenticated RCE, fixed 2023.05.4 or patch plugin; status exploited and cisa-kev, from the KEV catalogue pull, dateAdded 2023-10-04).
  - The JetBrains post-patch backdoor warning now drives the takeaway. public-sector sector removed; confidence medium.
- Declined: none.
- Legacy: B/2; T1190, T1078, T1072, T1195.001, T1195.002, T1566, T1204.004, T1552; Exposure, Detection, Triage (SentinelOne's role-deviation discriminator), Defender takeaway; affected_products "JetBrains TeamCity On-Premises". Contagious Interview and Sha1-Hulud are left unkeyed (examples in a multi-case post).

### 4. 2026-05-16/unit-42-gremlin-stealer-evolved-with-net-resource-xor-obfusc
- correction at 2026-10-21T20:19:32Z; fields: affected_products, body, classification, evidence, headline, sources, sourcing_note, summary, techniques, title
- Applied (https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/):
  - Exfiltration is a ZIP named with the victim's public IP, uploaded to an attacker-controlled panel, with Telegram as the alternative channel.
  - The clipper swaps any matching wallet address; "saved passwords" removed.
  - The session-hijack module is described as Unit 42 does (it requests session data from the running browser process).
  - The commercial packer with instruction virtualization was added; the three "tiers" were replaced by the named capabilities; detection and hardening were rebuilt from the mechanism.
- Declined: none.
- Legacy: B/2; T1027.013, T1027.002, T1140, T1115, T1565.002, T1185, T1539, T1555.003, T1528, T1005, T1560, T1041, T1567; Exposure, Detection, Defender takeaway.

### 5. 2026-05-17/cert-pl-cve-2026-44088-szafirhost-jar-zip-polyglot-bypass-in
- correction at 2026-10-21T20:21:19Z; fields: actions, affected_products, body, classification, cves, evidence, headline, priority, sectors, sources, sourcing_note, summary, techniques, title, verification
- Applied (https://cert.pl/en/posts/2026/05/CVE-2026-44088/, EUVD-2026-30512, wFirma help page, https://www.bakom.admin.ch/en/electronic-signature):
  - The Swiss eIDAS-recognition clause was deleted. BAKOM: no CH-EU mutual recognition, so foreign qualified signatures are not equivalent. This is stated in the takeaway as the scope condition.
  - The download-path, MitM, silent-signing and sector-list claims were removed; the RCE is stated as CERT Polska gives it.
  - T1574.002 (revoked) replaced by T1203 and T1553.
  - The CVE record now reads type rce, affected "all versions before 1.2.1", fixed 1.2.1, and "8.6 (CVSS 4.0, CERT-PL via ENISA EUVD)".
  - The SzafirHost description is taken from wFirma (quote translated from Polish, original kept). Brief references removed.
  - priority high→routine (no Swiss nexus, no exploitation); action dropped; verification set to single-source-national-cert (cert.pl is on the carve-out list).
  - The healthcare and legal-services sectors were dropped.
- Declined: none.
- Legacy: A/2; Exposure, Defender takeaway (CERT Polska gives no detection basis); affected_products "KIR SzafirHost".

### 6. 2026-05-17/cve-2026-41225-f5-big-ip-big-iq-icontrol-rest-manager-role-a
- correction at 2026-10-21T20:23:39Z; fields: actions, affected_products, body, classification, cves, event_date, evidence, headline, priority, sectors, sources, sourcing_note, summary, techniques, title
- Applied (SecurityWeek https://www.securityweek.com/f5-patches-over-50-vulnerabilities/, NCSC-NL CSAF, new source EUVD-2026-29986 https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-29986, which carries F5's description, versions and CVSS 4.0):
  - BIG-IP only (BIG-IQ dropped).
  - Fixed versions 21.0.0.2, 17.5.1.6 and 17.1.3.2; 16.1 is past end of technical support with no fix listed.
  - Dated 2026-05-13; CVSS shown as F5 8.6 (4.0) and NCSC-NL 9.1 (3.1, scope changed), with NVD no longer cited.
  - The misattributed secondary-cluster id list was removed (verified against the CSAF descriptions).
  - The public-sector deployment claim, the credential-theft chain and the uncited monitoring list were removed; detection is derived from the mechanism.
  - Self-references removed; priority high→notable; sectors reduced to technology.
- Declined: none. K000160932 stays as the original primary record but is unreadable (myF5 shell), so no specifics are cited to it.
- Legacy: A/2; T1078, T1059, T1068; Exposure, Detection, Defender takeaway; affected_products "F5 BIG-IP".

### 7. 2026-05-17/cve-2026-41553-dhtmlx-pdf-export-module-unauthenticated-serv
- correction at 2026-10-21T20:25:10Z; fields: actions, affected_products, body, classification, cves, evidence, headline, priority, regions, sectors, sources, sourcing_note, summary, tags, techniques, title
- Applied (https://cert.pl/en/posts/2026/05/CVE-2026-7182/, EUVD-2026-30537/30538/30539, DHTMLX changelog):
  - The EU e-government, healthcare and municipal deployment claims were removed (they were the only nexus).
  - Product scope corrected to the PDF Export Module (Gantt and Scheduler) and Diagram's export module.
  - CVE-2026-41552 and CVE-2026-7182 retyped as path-traversal (file read); affected and fixed set on all three (0.3.3 to before 0.7.6; Diagram 1.0.0 to before 1.1.1).
  - The migrated CVE Summary Table was deleted (it held F5 and SzafirHost rows); scanning and 48-hour claims removed.
  - priority high→notable; eu-nexus tag, extra sectors and the europe region removed.
- Declined: the EPSS figure was dropped rather than corrected to 0.0039. The FIRST API is not a citable page, and the score is time-varying.
- Legacy: A/2; T1190, T1059.007, T1005; Exposure, Detection (with post-upgrade compromise check), Defender takeaway; affected_products "DHTMLX PDF Export Module", "DHTMLX Diagram".

### 8. 2026-05-17/funnelkit-funnel-builder-for-woocommerce-actively-exploited
- correction at 2026-10-21T20:26:56Z; fields: actions, affected_products, body, classification, cves, event_date, evidence, headline, priority, sectors, sources, sourcing_note, summary, tags, techniques, title
- Applied (https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited, BleepingComputer, THN https://thehackernews.com/2026/05/funnel-builder-flaw-under-active.html, EUVD-2026-30936):
  - CVE-2026-47100 added (CVSS 4.0 8.7 VulnCheck, affected before version 3.15.0.3, exploited and patch-available); "no CVE assigned" removed.
  - 40,000+ is stated as the install base. FunnelKit's statement (added to THN on 2026-05-31) gives 3 of 1,300+ monitored sites compromised, the exploitation path closed and backports pushed via WordPress.org.
  - Evidence replaced with contiguous quotes; the "three independent sources" sentence deleted.
  - The polymorphic, PHP-process WebSocket, wp_options and Swiss/EU exposure claims were removed, and T1505.003 replaced.
  - Detection rebuilt on the plugin's External Scripts setting and browser-side checkout telemetry; Triage added from Sansec's GTM-disguise discriminator.
  - priority high→notable; actively-exploited and rce tags plus extra sectors removed.
- Declined: the truth pass asked for an update record with the vendor statement. That statement is folded into this correction, because the brief forbids `update` (see Tension 1).
- Legacy: B/2; T1190, T1059.007, T1140, T1036.005, T1071.001, T1056; Exposure, Detection, Triage, Defender takeaway; affected_products "FunnelKit Funnel Builder for WooCommerce Checkout".

### 9. 2026-05-17/kaspersky-great-documents-kimsuky-s-rust-based-hellodoor-and
- correction at 2026-10-21T20:28:53Z; fields: actions, affected_products, body, classification, entities, evidence, headline, regions, sources, sourcing_note, summary, techniques, title
- Applied (https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/):
  - The spliced quote was replaced by whole sentences; httpMalice, MemLoad and httpTroy are described as Kaspersky does.
  - Detection is derived from Kaspersky's observations; Kaspersky published no guidance.
  - Sample window set to August 2025 to February 2026. HelloDoor is described as early-stage, with TryCloudflare making its infrastructure hard to trace.
  - Targeting corrected (South Korea, with PebbleDash also hitting Brazilian defense organizations and a German defense firm); the "closest to Swiss government" claim and self-references removed.
  - Task names generalised; the mapping was moved into techniques[]; the campaign key added; regions now apac, dach and latam.
- Declined: none.
- Legacy: B/2; 26 ids (T1566.001, T1204.002, T1036.007, T1059.007, T1059.001, T1564.003, T1140, T1218.010, T1218.011, T1547.001, T1053.005, T1543.003, T1497.001, T1620, T1105, T1082, T1071.001, T1102.002, T1573.001, T1572, T1219, T1113, T1560, T1041, T1056.001, T1553.002); Exposure, Detection, Triage (legitimate VSCode tunnel/DWAgent vs dropper-launched from Public/ProgramData), Defender takeaway.

### 10. 2026-05-18/tycoon2fa-after-the-march-2026-takedown-oauth-device-authori (deep dive)
- correction at 2026-10-21T20:30:49Z; fields: affected_products, body, classification, entities, event_date, evidence, headline, regions, sectors, sources, sourcing_note, summary, tags, techniques, title, verification
- Applied (https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing, BleepingComputer, Microsoft Learn CA page):
  - The device-code variant now runs alongside the relay kit, and AS45102 is an addition to the known hosting set, not a replacement.
  - The fabricated device-code prompt quote was removed.
  - Hunts replaced with eSentire's signals: successful deviceCode sign-ins (ResultType 0) from new sources, the Broker AppId, node/undici user agents (axios marks the relay variant) and ResultType 50173 after revocation.
  - The CryptoJS key is no longer printed; both FIDO2 claims were removed.
  - Hardening rebuilt from eSentire and Microsoft (Conditional Access device-code block, admin consent, CAE, device compliance); the CAPTCHA and Check Domain steps are separated.
  - Every attack-chain clause is cited; verification set to single-source (one assessor); campaign key added; sectors emptied; ai-abuse tag removed.
- Declined: none.
- Legacy: B/2; T1566.002, T1204.001, T1583.007, T1027, T1622, T1497, T1528, T1550.001, T1078.004; Exposure, Detection (with the revocation and post-compromise review), Triage, Defender takeaway; affected_products "Microsoft Entra ID", "Microsoft 365".

### 11. 2026-05-19/7-eleven-confirms-shinyhunters-breach-of-600-000-salesforce
- correction at 2026-10-21T20:33:26Z; fields: body, classification, entities, evidence, headline, priority, regions, sectors, sources, sourcing_note, summary, techniques, title
- Applied (SecurityWeek, Security Affairs, Cybersecurity Dive https://www.cybersecuritydive.com/news/7-eleven-cyberattack-franchisee-data/820698/, CyberInsider):
  - The title states the confirmed breach of franchisee documents, not 600K records; the 600K figure stays an unverified actor claim.
  - The co-victims are SecurityWeek's list of recent claims, not "the same campaign".
  - Letters dated 2026-05-01 with access on 2026-04-08; filings count 47/2/1 people in MA/ME/VT; up to 24 months of IDX protection.
  - The 2026-05-25 section was revised in place: CyberInsider gives no vector for Charter; the "following our security protocols" quote is full; the "first telco" claim, "tracked here" and the non-CPNI speculation were dropped; Troy Hunt is described as relaying a post, not corroborating.
  - Medtronic incident key replaced by the 7-Eleven and Charter incident keys; uncited recommendations and T-ids removed; techniques mapped to the stated behavior only; priority high→notable.
  - Cybersecurity Dive added as a source; the unreadable Maine AG page is kept as the original record but not cited.
- Declined:
  - The Charter dataset leak (CyberInsider UPDATE, HIBP 4.9M emails) is a later development. It cannot go into the 2026-05-25 section (that section must not report later events), and the brief forbids `update`. It belongs on whichever entry carries Charter (see twins).
  - "Decide with the twin which one carries Charter" was not done (twin rule).
- Legacy: B/2; T1213.004, T1657 (no access vector stated for 7-Eleven or Charter, so no T1566/T1199); Exposure, Defender takeaway.

### 12. 2026-05-19/arwini-lower-saxony-statutory-prescription-audit-body-invest
- correction at 2026-10-21T20:34:28Z; fields: affected_products, body, classification, evidence, headline, priority, regions, sources, sourcing_note, summary, techniques, title
- Applied (Heise https://www.heise.de/news/Niedersachsen-Datenabfluss-bei-Wirtschaftsprueferverein-im-Gesundheitswesen-11297772.html, Deutsches Ärzteblatt, Borns IT Blog):
  - ARWINI's figure is up to 75,000 records in the worst case, while HAZ/NDR estimate more than 70,000. The KVN's statement that the patient data it supplies are anonymised is added as the contradiction.
  - Authorities corrected: the Hannover police directorate and the Lower Saxony DPA (timeliness under review). The BSI, KRITIS and NIS2 claims and the NMDL/IGJ link were removed.
  - Evidence now has English quotes with German originals; the police-confirmed Kairos attribution is in.
  - "Double-extortion ransomware" replaced by data theft with a leak-site listing (2.87 TB since 05-11, unpublished); the headline was completed; priority high→notable.
- Declined: none.
- Legacy: B/2; T1657; Exposure, Defender takeaway (no vector, no detection basis).

### 13. 2026-05-19/bigbluebutton-bbb-web-3-0-21-3-0-23-three-flaws-in-eu-educat
- correction at 2026-10-21T20:35:59Z; fields: actions, affected_products, body, classification, cves, event_date, evidence, headline, priority, regions, sectors, sources, sourcing_note, summary, techniques, title
- Applied (GHSA-7959/-43hc/-xqm3, BSI WID-SEC-2026-1568, EUVD-2026-44996/44998/44997, the CVE records GitHub issued on 2026-07-16):
  - Advisories dated 2026-05-13 and BSI 2026-05-18; the DFN, SWITCH, GÉANT, cantonal and Länder operator claims were removed.
  - Impacts are now the vendor's own statements; the evidence quote is the advisory's impact sentence; the BSI quote is translated with the original kept.
  - Every CVE record now has affected and fixed versions; CVE-2026-46404 retyped ssrf; vector zero-click.
  - Detection derived from the mechanisms ("link-local addresses"); headline complete; priority high→notable; regions global and dach; sectors education.
- Declined: none.
- Legacy: A/2; T1190, T1212; Exposure, Detection, Defender takeaway; affected_products "BigBlueButton".

### 14. 2026-05-19/chaotic-eclipse-windows-zero-days-miniplasma-is-third-poc-in
- correction at 2026-10-21T20:37:19Z; fields: affected_products, body, classification, cves, event_date, evidence, headline, sectors, sources, sourcing_note, summary, tags, techniques, title
- Applied (BleepingComputer, THN, MSRC https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103):
  - CVSS 7.0 (Microsoft). Microsoft re-released the CVE on 2026-06-09 and the June 2026 updates fix MiniPlasma, so the status is now patch-available and the no-patch tag is removed.
  - Evidence is verbatim BleepingComputer; Dormann's confirmation is kept separate from BleepingComputer's own test; the race-condition note was added.
  - Series order corrected (BlueHammer, RedSun, UnDefend, YellowKey, GreenPlasma); the "UPDATE (originally covered ...)" label and the migration sourcing_note were removed.
  - Detection is limited to ThreatLocker's two registry paths; EID 6 and the OneDrive claim dropped; public-sector sector removed.
- Declined:
  - Linking the 2026-05-15 YellowKey/GreenPlasma entry in references[] was declined: the coordinator routes that pair to a new tracker row, and twins get no reference.
  - The June fix arrives via a correction, not an `update` (Tension 1).
- Legacy: A/1 (vendor plus two independent reproductions); T1068, T1112; Exposure, Detection, Defender takeaway; affected_products "Microsoft Windows".

### 15. 2026-05-19/cisa-contractor-nightwing-exposed-aws-govcloud-admin-keys-an
- correction at 2026-10-21T20:38:37Z; fields: affected_products, body, classification, entities, event_date, evidence, headline, regions, sectors, sources, sourcing_note, summary, techniques, title
- Applied (https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/, Gizmodo):
  - LZ-DSO (one of the internal systems) is separated from the Artifactory credentials.
  - The "CISA acknowledged" staffing inference was replaced by CISA's own statement; staffing is Krebs's context.
  - The sync explanation is Caturegli's suspicion; the exposure runs from 2025-11-13 to mid-May, up to about six months; the backdoor point is quoted as a risk.
  - The file name was generalised; event_date 2026-05-18; every clause cited; uncited recommendations removed; the incident key added; defense sector and global region dropped.
- Declined: none.
- Legacy: B/2; T1593.003, T1552.001, T1078.004; Exposure, Detection, Defender takeaway.

### 16. 2026-05-19/grafana-labs-coinbasecartel-breach-victim-confirms-source-co
- correction at 2026-10-21T20:40:06Z; fields: affected_products, body, classification, entities, event_date, evidence, headline, regions, sectors, sources, sourcing_note, summary, techniques, title
- Applied (SecurityWeek, BleepingComputer, THN 2026-05-17, new THN 2026-05-20 https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html):
  - The Pwn-Request mechanism was replaced by Grafana's own account: a workflow token missed after the TanStack npm compromise (TeamPCP), detected 2026-05-11.
  - The scope widened to internal repositories with business contact names and emails; production systems and Grafana Cloud were not affected.
  - Confirmation dated 2026-05-17; the UPDATE/W21 framing removed. The ShinyHunters link is contested (BleepingComputer), victim counts are 105 (SW) vs 170 (THN), and actor:shinyhunters was removed.
  - The EU/CH Grafana claim and the uncited plugin-monitoring advice removed; mapping moved to T1195.001, T1528, T1213.003, T1657.
  - The Register source was dropped (the saved page is an unrelated listing).
- Declined: the "update record (2026-05-19 scope widening)" is folded into this correction (Tension 1).
- Legacy: B/2; Exposure, Detection, Defender takeaway.

### 17. 2026-05-19/interpol-operation-ramz-13-country-mena-cybercrime-sweep-201
- correction at 2026-10-21T20:41:04Z; fields: affected_products, body, classification, evidence, headline, regions, sectors, sources, sourcing_note, summary, tags, techniques, title
- Applied (https://www.interpol.int/en/News-and-Events/News/2026/201-arrests-in-first-of-its-kind-cybercrime-operation-in-MENA-region):
  - The EU-targeting, advisory-prediction and Europol claims were removed.
  - The Jordan case is stated as INTERPOL gives it: a fake trading platform run by 15 trafficking victims, with two organizers arrested.
  - The Oman server is described correctly; the Algeria arrest and the Qatar finding were added; the summary was completed and every outcome cited.
  - eu-nexus tag, the europe region and public-sector sector removed; headline shortened to 120 characters.
- Declined: none.
- Legacy: A/2; T1566, T1584, T1657; Defender takeaway (no exposure or detection basis).

### 18. 2026-05-19/symantec-carbon-black-document-fast16-hook-engine-targeting
- correction at 2026-10-21T20:42:29Z; fields: affected_products, body, classification, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title
- Applied (https://www.security.com/blog-post/fast16-nuclear-sabotage, Zetter, THN):
  - SentinelOne's April 2026 analysis is now described without the LABScon and centrifuge claims.
  - The framing contradiction is explicit: Zetter calls fast16 contemporaneous with Stuxnet, Broadcom still says pre-Stuxnet.
  - Broadcom dated 2026-05-16; the evidence is one verbatim bullet; LS-DYNA/AUTODYN described per Broadcom; "first publicly documented" dropped; the headline completed.
  - Detection is built on the documented install artifacts, described generically with no file names; Broadcom's driver-inventory defense drives the takeaway.
  - T1021.002 and T1570 added (admin-share copy and remote service, stated by Broadcom).
- Declined: none.
- Legacy: B/1 (two labs agree on the core); T1059, T1014, T1565.003, T1543.003, T1546.012, T1070.006, T1518.001, T1135, T1021.002, T1570, T1569.002; Exposure, Detection, Defender takeaway.

### 19. 2026-05-20/cisco-talos-demo-pdb-badiis-variant-now-a-commodity-maas-iis
- correction at 2026-10-21T20:44:17Z; fields: affected_products, body, classification, entities, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title
- Applied (https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/):
  - BadIIS is a native IIS module in globalModules/modules (not ISAPI), with a hidden backup copy that survives IIS restarts.
  - DragonRank and UAT-8099 are stated as a contrast, not an overlap; the MaaS assessment is Talos's; the "first" claim removed.
  - The lwxat evidence is listed; the access vector is stated as not described; detection derived from the module list, backup copy and impersonating services.
  - event_date 2026-05-19; the campaign key added.
- Declined: none.
- Legacy: B/2; T1505.004, T1565.002, T1543.003, T1036.004, T1027, T1059.003, T1105, T1071.001; Exposure, Detection, Defender takeaway; affected_products "Microsoft IIS".

### 20. 2026-05-20/cve-2026-31635-dirtydecrypt-linux-kernel-rxgk-page-cache-wri
- correction at 2026-10-21T20:45:41Z; fields: actions, affected_products, body, classification, confidence, cves, event_date, evidence, headline, sectors, sources, sourcing_note, summary, techniques, title
- Applied (BleepingComputer, THN, new EUVD-2026-25528 https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-25528):
  - The DirtyDecrypt-to-CVE-2026-31635 mapping is attributed to Will Dormann and the NVD PoC link. The contradiction is stated: the kernel CNA describes an inverted RESPONSE length check hitting BUG_ON, CVSS 7.5 network DoS.
  - File path corrected; the dead Moselwal source and its 7.8-8.1 range dropped (THN quotes Moselwal on the mechanism).
  - The Debian/RHEL/Ubuntu claim was replaced by the CONFIG_RXGK and version scope: 6.16 up to before 6.18.23 or 6.19.13, fixed 6.18.23, 6.19.13 and 7.0.
  - V12 and Delphos Labs are credited; the mitigation is BleepingComputer's (blocking esp4, esp6 and rxrpc breaks IPsec and AFS); EID 8 dropped.
  - event_date 2026-05-18; confidence medium; the action removed.
- Declined: the PoC date is stated as "public by 2026-05-18" (BleepingComputer), not 2026-05-17. The commit date comes from the GitHub API, which is not a citable page.
- Legacy: B/2; T1068, T1611; Exposure, Detection, Defender takeaway; affected_products "Linux kernel".

## Tensions for the main agent
1. Three corrections carry post-discovery developments: FunnelKit (CVE-2026-47100 published 2026-05-19, the vendor statement in the 2026-05-31 THN update), MiniPlasma (Microsoft's 2026-06-09 re-release and June fix) and Grafana (the 2026-05-19 scope update). BigBlueButton additionally cites the July EUVD/CVE records. Each is written as today's truth inside a `correction`, because the brief forbids `update` (re-floating). Change the type if the policy view differs.
2. 7-Eleven / Charter: the later Charter leak (HIBP, 4.9M emails) is not recorded anywhere in my batch. See the twin 2026-05-27/shinyhunters-salesforce-campaign-charter-and-7-eleven-both-c.

## Folds and links
- Folds: none (no duplicate group in the batch).
- references[]: none added.
- possible_twin_outside_batch, all unchanged:
  - SzafirHost ↔ 2026-06-30/cert-polska-discloses-a-jar-parser-confusion-rce-in-the-szaf (same product, different flaw CVE-2026-13165; cross-reference candidate)
  - F5 CVE-2026-41225 ↔ 2026-05-15/cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea (same F5 quarterly)
  - Tycoon2FA ↔ 2026-05-27/tycoon-2fa-after-the-march-2026-takedown-two-tier-aitm-opera
  - 7-Eleven ↔ 2026-05-27/shinyhunters-salesforce-campaign-charter-and-7-eleven-both-c (also carries Charter, with a ~185,000 7-Eleven count)
  - Chaotic Eclipse MiniPlasma ↔ 2026-05-15/windows-bitlocker-yellowkey-and-ctfmon-greenplasma-zero-days (fold candidate, routed to a new tracker row per the coordinator); see also 2026-05-30/nightmare-eclipse-chaotic-eclipse-microsoft-s-digital-crimes
  - Grafana ↔ 2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands
  - DirtyDecrypt: not a twin, but 2026-05-20/vm2-node-js-sandbox-12-critical-cves-cve-2026-43997-43999-44 carries a CVE-2026-31635 table row citing the dead Moselwal URL

## Registry changes needed (entities/registry.yaml)
- New actor (proposed): `actor:coinbasecartel`, name "CoinbaseCartel", aliases ["Coinbase Cartel"].
  - Summary: "Data-theft extortion group active since September 2025 that lists victims on its leak site without encrypting files; security firms link it to ShinyHunters, Scattered Spider and Lapsus$, which ShinyHunters denies."
  - Sources: SecurityWeek and BleepingComputer, 2026-05-18, via entry 2026-05-19/grafana-labs-coinbasecartel-breach-victim-confirms-source-co; first_seen 2026-10-21.
  - Possible relation on incident:grafana-labs-coinbasecartel-pwn-request-github-actions-breac → actor:coinbasecartel, type `related-to`, note "claimed on its leak site". Not `attributed-to`: the claim is unverified and Grafana names an unnamed extorter. Source: the Grafana entry. Then key the actor on that entry.
- Summary fixes:
  - incident:dream-market-admin-arrest-2026-05: "Suspected Dream Market main administrator Owe Martin Andresen arrested in Germany on 2026-05-07 on German money-laundering charges in a coordinated German and US operation; the US indictment alleges he laundered the marketplace's dormant commission wallets." (not "BKA with US multi-agency support")
  - campaign:sentinelone-living-off-the-pipeline-2026: "SentinelOne post (2026-05-15) on CI/CD subversion seen in 2025: a TeamCity intrusion, a GitLab service-account token used to run Ansible playbooks, Contagious Interview and Sha1-Hulud rogue runners." (no "taxonomy" or "three case studies"; the type `campaign` is questionable for a vendor post)
  - campaign:funnelkit-funnel-builder-for-woocommerce-actively-exploited-magecart-skimmer: "Unauthenticated settings write in FunnelKit Funnel Builder for WooCommerce Checkout before 3.15.0.3 (CVE-2026-47100) exploited to plant fake Google Tag Manager card skimmers; FunnelKit saw 3 of 1,300+ monitored sites compromised." (the CVE exists; 40,000+ is the install base)
  - campaign:kimsuky-pebbledash-hellodoor-trycloudflare-tunnel-c2-evolution and actor:kimsuky: remove "HTTPSpy RAT" (not in the Securelist report; the tools are HelloDoor, httpMalice, MemLoad, httpTroy, AppleSeed, HappyDoor). "Germany spillover" → "PebbleDash victims include a German defense firm"; actor "European targets" is unsupported by this source.
  - incident:7-eleven-confirms-shinyhunters-salesforce-breach-600k-recor: "7-Eleven confirms unauthorized access on 2026-04-08 to systems storing franchisee documents (about 50 people in three US state filings) after ShinyHunters claimed 600,000+ Salesforce records." (no "same campaign")
  - incident:arwini-lower-saxony-statutory-prescription-audit-body-data: "confirmed by the Hannover police directorate", not "the LKA"; police name Kairos.
  - trend:bigbluebutton-bbb-web-three-cves-46351-46353-46404-eu-edu: drop "EU education/government ... platform" (no source for the deployment base); "open-source virtual classroom".
  - incident:grafana-labs-coinbasecartel-pwn-request-github-actions-breac: "Grafana Labs GitHub breach via a workflow token missed after the TanStack npm compromise; code and internal repositories with business contacts downloaded; CoinbaseCartel claimed it; ransom refused." (no pwn-request, not source-code-only; the key name stays as is, keys are permanent)
  - campaign:cisco-talos-badiis-demo-pdb-maas-isapi-backdoor-lwxat-dragon: "native IIS module (globalModules/modules), commodity MaaS likely shared among Chinese-speaking crime groups; contrasted with, not linked to, DragonRank/UAT-8099". Drop "1,800+ IIS servers" (not in the Talos post) and "ISAPI".
  - campaign:fast16-symantec-carbon-black-contemporaneous-stuxnet-nuclea: "Kim Zetter argues contemporaneous with Stuxnet; Broadcom still calls it pre-Stuxnet" (not "corrected").
  - campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac: MiniPlasma is not "the third PoC", and CVE-2020-17103 was re-released and fixed with the June 2026 updates.
  - campaign:interpol-operation-ramz-mena-cybercrime-13-country-201-arre: "first ... sweep" → "first cyber operation of its scale coordinated by INTERPOL in MENA"; "first Algerian PhaaS takedown" is unsupported (INTERPOL says a PhaaS website was dismantled in Algeria).

## state/cves_seen.json changes needed
- Add CVE-2026-47100: first_seen 2026-10-21, last_seen 2026-10-21, primary_source_url https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited, title "FunnelKit Funnel Builder for WooCommerce Checkout before 3.15.0.3: unauthenticated settings write exploited to plant checkout card skimmers (CVSS 4.0 8.7)". This clears the cve-sync FAIL for my batch.
- Bump last_seen to 2026-10-21 (records changed or added this run): CVE-2023-42793 (now a cves[] record on the SentinelOne entry), CVE-2026-44112, CVE-2026-44113, CVE-2026-44115, CVE-2026-44118, CVE-2026-44088, CVE-2026-41225, CVE-2026-41553, CVE-2026-41552, CVE-2026-7182, CVE-2026-46351, CVE-2026-46353, CVE-2026-46404, CVE-2020-17103, CVE-2026-31635.
- Titles still carrying the corrected errors:
  - CVE-2026-44115: "command-parser allowlist bypass" → "exec allowlist bypass via shell expansion in unquoted heredocs"
  - CVE-2026-41225: "CVSS 9.1" → "CVSS 4.0 8.6 (F5); 9.1 CVSS 3.1 (NCSC-NL)"
  - CVE-2026-41552: "path traversal via src attribute" belongs to CVE-2026-7182 → "PDF Export Module path traversal, local files in generated PDF"
  - CVE-2020-17103: add "re-released 2026-06-09, fixed by the June 2026 updates"
  - CVE-2026-31635: note the kernel CNA describes a RESPONSE length-check BUG_ON
  - CVE-2026-44112..44118: "OpenClaw / Clawdbot" → "OpenClaw (originally Clawdbot)", fixed in 2026.4.22

## Product names introduced (for tools/sync_products.py)
OpenClaw; JetBrains TeamCity On-Premises; KIR SzafirHost; F5 BIG-IP (existing); DHTMLX PDF Export Module; DHTMLX Diagram; FunnelKit Funnel Builder for WooCommerce Checkout; Microsoft Entra ID; Microsoft 365; BigBlueButton; Microsoft Windows (existing); Microsoft IIS; Linux kernel (existing).

## Residuals outside the findings (nothing fixed)
- 2026-05-19/cisa-contractor-nightwing-exposed-aws-govcloud-admin-keys-an stays priority high (no finding); under the high bar (constituency exposure, a decision within 7 days) it reads as notable.
- 2026-05-19/7-eleven-confirms-shinyhunters-breach-of-600-000-salesforce updates[0].summary (append-only) still contains "tracked here", "by our own tracking" and an em dash.
- 2026-05-16/bka-arrests-dream-market-lead-administrator-speedstepper-in keeps sector legal-services, which no source supports.
- 2026-05-17/cert-pl-cve-2026-44088-szafirhost-jar-zip-polyglot-bypass-in and 2026-05-19/bigbluebutton-bbb-web-3-0-21-3-0-23-three-flaws-in-eu-educat keep kind threat although they are vulnerability disclosures.
- 2026-05-19/symantec-carbon-black-document-fast16-hook-engine-targeting keeps tags espionage and iran-nexus (sabotage; Iran is the presumed target, not the actor's nexus).
- 2026-05-16 OpenClaw: OpenClaw's severity label for CVE-2026-44112 (High per the truth pass) is not verified from a saved body; only CVE-2026-44115 (moderate) was checked raw.
- CVE-2023-42793 `cisa-kev` status rests on the KEV catalogue pull (repair-3/src/kev.json, dateAdded 2023-10-04); the body does not cite KEV.
- None of the batch's other CVEs is in the CISA KEV catalogue of 2026.10.21.
