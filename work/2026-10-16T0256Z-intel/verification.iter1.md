**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-16T04:33:18Z · ended_at=2026-10-16T05:01:39Z · duration_seconds=1701

## Verification report — 2026-10-16T0256Z-intel (iteration 1)

Scope: 5 new entries, 8 updated entries (whole entry read, `git diff HEAD` read for each, every `fields` name checked against the diff), run record. Claim ledger: 257/257 claims answered (`tools/claim_ledger.py --coverage 1` reports 0 missing); verdict rows in `verification.iter1.claims.yaml` (237 ok, 5 F3, 8 F4, 4 F14 rows, 3 F5 rows). No prior-iteration deltas block (first pass). Sources were read from the run's saved bodies where they were complete and re-fetched where the saved body lacked the passage (GTIG raw HTML for the date, PAN-OS advisory raw HTML, CERT-FR raw HTML for the version history, Previdian live, Register raw HTML, MSRC SUG API, Adobe bulletin tables, Fortinet raw HTML, BPK and BLVK PDFs, drupal.org SA-CORE-2026-014 and SA-CONTRIB-2026-218 via WebFetch).

### Citation does not support the claim
- #1 F3 `2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day`, Exposure line ("the /appliance interface shows whether it is installed or automatic updates are on, and a build older than 24.3.1 must be upgraded first, which closes the hole but does not undo earlier exposure ([BeyondTrust ... bt26-05 blog])"). The cited blog contains none of "/appliance", "24.3.1", "26.2.3" or automatic updates (zero matches). The advisory has them ("in their /appliance interface. Customers on a Remote Support version older than 24.3.1 will need to upgrade") and GTIG has "Upgrading closes the vulnerability but does not remediate prior exposure." Re-cite advisory and GTIG.
- #2 F3 same entry, Defender takeaway: "its own detection platform's automated triage closed the privilege-escalation alerts". Blog: "the built-in triage tool in our third-party detection platform closed those alerts as false positives." "Its own" misattributes ownership. Also "treat each one ... as compromised" is stronger than GTIG's "potentially compromised until it has been reviewed".
- #3 F3 (low confidence) `2026-10-16/adfection-candiru-spyware-zero-click-ad-delivery`: "the Windows implant Citizen Lab recovered". Citizen Lab: "Al Jazeera isolated a Windows DLL file from one of the compromised devices".
- #4 F3 `2026-10-16/peerstitch-fortigate-implant-cve-2025-61624-fortimanager`, Exposure: "a FortiManager reachable on TCP 541 from untrusted networks" is cited to FG-IR-26-122, which covers only the CLI path traversal and never mentions FortiManager or TCP 541 (that is Unit 42: "FMG-Access (TCP port 541) management channel").
- #5 F3 (low confidence) `2026-10-14/cve-2026-104935-ivanti-connect-secure-zero-day-chain-kev`, Update: "names the 22.8R2.x builds before 22.8R2.5". CERT-FR: "version 22.8Rx antérieures 22.8R2.5".

### Unsupported / hallucinated facts
- #6 F4 BeyondTrust `immediate_action`: "BeyondTrust and Google's Threat Intelligence Group confirm that ... was exploited as a zero-day from late August 2026 by a China-nexus espionage actor". GTIG: "ARMORY CASTLE, a suspected PRC-nexus espionage threat actor"; BeyondTrust: "A suspected China-nexus espionage actor", attribution "moderate to high confidence". "Confirm" upgrades a suspected attribution. Summary and body also drop "suspected" (low confidence for those two).
- #7 F4 AdFection Triage: "the immediate hand-off to uncategorized hosts" is in neither Citizen Lab nor Confiant (zero matches for "uncateg"). Remove or source.
- #8 F4 (low confidence) AdFection Defender takeaway: "the delivery path bypasses mail and web-filter controls". Citizen Lab says zero-click and "no consistently safe way to expose your users and networks to targeted ads"; nothing about bypassing mail or web-filter controls.
- #9 F4 PEERSTITCH Detection: "The implant leaves nothing on disk, so confirming it takes live forensics of miglogd and iked." Unit 42: "no persistent binary on disk", five files downloaded into /data2/template/ before lldprx unlinks itself, and its hunting table also lists a configuration-revision audit (auto-script objects with ../) and `diagnose debug crashlog read`.
- #10 F4 `2026-10-06/cve-2026-21589-atlassian-data-center-arbitrary-file-access`, Update 2026-10-16T04:11:30Z: "the earlier honeypot reports of attempts stand as the only public detail ... Previdian's page, which on 2026-10-08 listed the flaw as not in the catalog, predates the listing". The same Previdian URL, saved by the run and re-fetched now, reads "Updated 16 Oct 2026", "607 Attempts observed", "65 Unique attacker IPs", "20 Attacker countries", "5 Sensors", "In CISA KEV", with a Shadowserver attestation at 2026-10-14. The summary keeps the 2026-10-08 figures (129 attempts, 22 addresses). The exploitation delta (roughly 5x attempts, 3x addresses, a second attester) was missed and the "only public detail" statement is contradicted by the page it cites. Refresh with the current figures and date.
- #11 F4 (low confidence) Drupal Exposure: "any contributed module or custom code that renders Field UI tables from user-influenced input" is the entry's own inference (THN: contributed modules open paths, "custom code may also expose it"); "or on any end-of-life branch" is broader than the advisory range (>= 8.9.0).

### Claims missing inline citation
- #12 F5 `2026-10-10/ahsaycbs-...` title, headline, summary and body ("Ahsay admits its August AhsayCBS patches were incomplete", "The August patches did not close the flaws"). Ahsay's page says "our previous patches v9.15.2.59 and v10.3.4.0" with no month; SecurityWeek, Huntress and the 10.3.4 release notes (dated 05-Aug-2026, no security fix) do not call them August patches. Only The Hacker News (https://thehackernews.com/2026/10/ahsaycbs-flaws-exploited-to-deploy-web.html, "released in August 2026") does, and it is not cited. Cite it or drop "August".
- #13 F5 `2026-10-16/cl-unk-1211-...` Detection: "Unit 42's own endpoint rule for the history tampering is named ..." has no inline citation (true on the Unit 42 page).

### Drop (low relevance / off-audience / duplicate)
- #14 F7 `2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups`: `priority: routine`, APAC, no vector, no actor, no family, no Swiss nexus. Check 5b allows two sentences at most or drop; the entry has four body paragraphs and this run added a two-paragraph update (48-customer portal data classes, hashed password, fee totals, zone names). Cut to two sentences keeping the supplier-concentration lesson, or drop.

### Needs more research
- #15 F8 PEERSTITCH Detection omits Unit 42's own hunting guidance (Table 2): anonymous 16,384-byte rwxp regions in /proc/<pid>/maps of miglogd and iked, NOP patches at three fixed offsets, cross-PID open()/write() on /proc/<pid>/mem, crashlog Signal 11 queries, the ../../tmp/apache2/conf/md-acme.conf auto-script and MDChallengeDns01 mapped to /bin/node.
- #16 F8 CL-UNK-1211 drops source-stated behaviour: the custom Go scanner for CVE-2025-55182 (React2Shell), SSH authorized_keys injection, sshpass lateral movement, MSSQL xp_cmdshell double-hop, GSocket gs-netcat in /dev/shm as [kcached], reverse SOCKS tunnelers, exfiltration to public file-hosting services. The React2Shell scanner is the only vulnerability lead toward an entry route.
- #17 F8 AhsayCBS Update omits Bitdefender's second-incident persistence: "obfuscated PowerShell commands ... install and configure OpenSSH ... a way back in that does not depend on the vulnerable web service, which is why patching alone does not end the incident", and the static-site-hosting staging.
- #18 F8 AdFection Detection presents DNS logs as a sound signature without Confiant's caveat (cited page): the operator-chosen domain is "resolved over encrypted DoH and then reached by raw IP, so it never appears as a plaintext DNS query or as a connection hostname, keeping it invisible to DNS-based monitoring and blocklists".
- #19 F8 (low confidence) Drupal `cves[].affected` omits the advisory's ">= 12.0.0-alpha1 < 12.0.0-beta2" range.

### Missed angles
- #20 F10 (low confidence) Beyond Gravity. The run record says SRF (2026-10-15) reports the company and the Confederation assume China is the attacker and that the oversight committees were told of a data outflow, that S2 and S4 both recommended a short entry, and that it was held because no evidence-bound `techniques[]` exists (a gate reason, not an editorial one). I could not fetch the SRF item. Check before the 2026-10-20 expiry: WebSearch "Beyond Gravity SRF China Datenabfluss GPK". Otherwise coverage looks complete: my own sweeps (Patch Tuesday zero-day CVE-2026-96951 is covered by 2026-10-14; SonicWall, Cisco, Ivanti, Fortinet, Citrix items are covered or dated outside the window; no Swiss communal incident dated 2026-10-15 surfaced).

### Editorial / less-is-more flags (advisory)
- #21 F11 CL-UNK-1211 `techniques[]` has no ids for authorized_keys injection (T1098.004), sshpass SSH lateral movement (T1021.004), xp_cmdshell, SOCKS tunnelers (T1090) or file-hosting exfiltration (T1567); all are source-stated.
- #22 F11 Drupal `sourcing_note` narrates the pipeline's own lookup ("the CVE record did not resolve at the CVE services when checked"); the advisory page carries CVE-2026-108097 itself.
- #23 F11 CL-UNK-1211: "(Unit 42 says its product stopped this)" and the detector name are vendor product-efficacy material.
- #24 F11 AhsayCBS `cves[].cvss` "medium (Huntress)" / "critical (Huntress)" while the cited Bitdefender page gives VulDB scores 7.3 High / 5.5 Medium and 10.0 Critical / 9.3 Critical.
- #25 F11 Publica Update lead-in "The scope for other funds shifted." carries no fact.

### Quantifier without source
- #28 F14 PEERSTITCH headline, summary, body: "a FortiGate implant with no file on disk", "leaves no binary on disk". Source: "leaves no persistent binary on disk"; the setup script downloaded pM.js, index.js, index.wasm, ipssem.js and the lldprx injector into /data2/template/ and lldprx then unlinked itself.
- #29 F14 Publica Update: "Police have warned of the first concrete misuse scenario." No source says "first"; SwissCybersecurity.net says the police word it in the conditional and "scheinen also noch keinen Fall registriert zu haben".

### Org-triage line missing / inconsistent
- #27 F16 (low confidence) Drupal `priority: high`: no exploitation, "E:Theoretical", "not directly exploitable with core alone", the one named unauthenticated path is a contrib module with 90 reporting sites (THN), exposure depends on unknown contrib or custom code. Near the "unexploited flaw reachable only in a non-default configuration" disqualifier. The pre-announcement warning and the public-sector Drupal footprint argue for keeping it; main agent to confirm.

### Action-item discipline
- #26 F18 (low confidence) AhsayCBS actions[1]: the artifact list in parentheses restates the Detection paragraph; the task is "compromise-check every server reachable since 2026-10-04 and re-image confirmed hosts".

### Verified clean (no finding)
PAN-OS update (timeline line "11.2.16 has been published." dated 2026-10-15 on the live and saved advisory; solution table reads "Upgrade to 11.2.16 or later." for 11.2.14 and 11.2.15; fields and `updated_at` match the record). Exchange update (blog banner of 2026-10-15 quoted correctly; MSRC SUG API confirms CVSS 8.1, AC:H, Exploitation More Likely, exploited No, fixed builds 15.02.2562.056 / 15.02.1748.055 / 15.02.1544.050 / 15.01.2507.077). Ivanti update (CERT-FR order of response, secret list, ICT caveat, French `original` matches the page and the translation is faithful; first-version date 14 octobre 2026 matches the citation). IDCF update (fifth report: 194 of 495, 48 portal registrations, no-outflow judgement, data classes, translations faithful). Adobe update (Sansec quotes, affected list, priority-2 criticism all present; bulletin CVSS values for the ColdFusion, AEM and Commerce items match). Publica update (cybercrimepolice, SwissCybersecurity.net update of 15.10.2026, NZZ BVK statements, Inside IT Ticino item all match). Atlassian KEV record (CISA alert and KEV catalog date 2026-10-15). BeyondTrust and Drupal CVE ids, scores, affected and fixed versions match the advisories (drupal.org SA-CORE-2026-014 risk 19/25, CVE-2026-108097; SA-CONTRIB-2026-218 CVE-2026-108099, "<3.0.10"). Fortinet FG-IR-26-122 raw HTML: CVE-2025-61624, CVSSv3 6.0, Known Exploited Yes, published 2026-04-14. Source dates on the new entries match each page's own date (GTIG datePublished 2026-10-15 although the extractor printed 10-16; CERT-FR first version 14 octobre). No em dashes, workflow vocabulary or IOCs in reader-facing text. No name collisions (SAWFLY, BARECLAW, SysGoRAT, PEERSTITCH, AdFection, CL-UNK-1211 are new to the store). Classification blocks present and consistent with the rubric. `updates[]` records: each non-internal `update` has its section, `updated_at` equals `at`, `fields` match the diff, no silent edits found.

### Verdict
NEEDS_FIXES (truth: 13, editorial: 11, advisory: 5)

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: 2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day (Exposure)
  item: "Exposure line: the /appliance interface shows whether the patch is installed, a build older than 24.3.1 must be upgraded first, which closes the hole but does not undo earlier exposure"
  url_or_quote: "https://www.beyondtrust.com/blog/entry/bt26-05"
  summary: "The cited BeyondTrust blog contains none of '/appliance', '24.3.1', '26.2.3' or automatic updates (zero matches). Those facts are in the advisory (https://www.beyondtrust.com/trust-center/security-advisories/bt26-05: 'in their /appliance interface. Customers on a Remote Support version older than 24.3.1 will need to upgrade') and GTIG ('Upgrading closes the vulnerability but does not remediate prior exposure'). Re-cite the advisory and GTIG."
- code: F3
  category: claim-not-supported
  section: 2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day (Defender takeaway)
  item: "BeyondTrust adds that its own detection platform's automated triage closed the privilege-escalation alerts as false positives"
  url_or_quote: "https://www.beyondtrust.com/blog/entry/bt26-05"
  summary: "Blog says 'the built-in triage tool in our third-party detection platform closed those alerts as false positives'; 'its own detection platform' misattributes ownership. Also 'treat each one ... as compromised' is stronger than GTIG's 'potentially compromised until it has been reviewed'."
- code: F3
  category: claim-not-supported
  section: 2026-10-16/adfection-candiru-spyware-zero-click-ad-delivery (body)
  item: "the Windows implant Citizen Lab recovered persists through COM hijacking"
  url_or_quote: "https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/"
  summary: "(low confidence) Citizen Lab: 'Al Jazeera isolated a Windows DLL file from one of the compromised devices'; Citizen Lab analysed the sample, it did not recover it."
- code: F3
  category: claim-not-supported
  section: 2026-10-16/peerstitch-fortigate-implant-cve-2025-61624-fortimanager (Exposure)
  item: "FortiGate and FortiManager estates, a FortiManager reachable on TCP 541 from untrusted networks, and FortiOS on 7.2, 7.0 or 6.4 ..."
  url_or_quote: "https://fortiguard.fortinet.com/psirt/FG-IR-26-122"
  summary: "FG-IR-26-122 covers only the CLI path traversal in FortiOS/FortiPAM/FortiProxy/FortiSwitchManager; it never mentions FortiManager or TCP 541 (that is Unit 42's CVE-2024-47575 'FMG-Access (TCP port 541)'). Split the clause or cite Unit 42 for the FortiManager part."
- code: F3
  category: claim-not-supported
  section: 2026-10-14/cve-2026-104935-ivanti-connect-secure-zero-day-chain-kev (Update 2026-10-16T04:10:00Z)
  item: "Its affected-systems list names the 22.8R2.x builds before 22.8R2.5"
  url_or_quote: "https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-013/"
  summary: "(low confidence) CERT-FR lists 'Connect Secure (ICS) version 22.8Rx antérieures 22.8R2.5' (any 22.8Rx before 22.8R2.5), not only 22.8R2.x."
- code: F4
  category: hallucinated-fact
  section: 2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day (immediate_action; summary; body)
  item: "BeyondTrust and Google's Threat Intelligence Group confirm that an unauthenticated flaw ... was exploited as a zero-day from late August 2026 by a China-nexus espionage actor"
  url_or_quote: "https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust/"
  summary: "GTIG: 'ARMORY CASTLE, a suspected PRC-nexus espionage threat actor'; BeyondTrust: 'A suspected China-nexus espionage actor' and 'moderate to high confidence'. 'Confirm ... by a China-nexus espionage actor' upgrades a suspected attribution to a confirmed one; summary and body also drop 'suspected' (low confidence for those two)."
- code: F4
  category: hallucinated-fact
  section: 2026-10-16/adfection-candiru-spyware-zero-click-ad-delivery (Triage)
  item: "the reported discriminators are the eligibility gating ..., the immediate hand-off to uncategorized hosts, and the validator-then-command-and-control sequence"
  url_or_quote: "https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/"
  summary: "Neither Citizen Lab nor Confiant says anything about 'uncategorized' hosts (zero matches for 'uncateg' in both texts). Confiant describes a hand-off to a CloudFront-hosted script. Remove or source the discriminator."
- code: F4
  category: hallucinated-fact
  section: 2026-10-16/adfection-candiru-spyware-zero-click-ad-delivery (Defender takeaway)
  item: "the delivery path bypasses mail and web-filter controls and needs no user action"
  url_or_quote: "https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/"
  summary: "(low confidence) Citizen Lab says 'zero-click' and 'no consistently safe way to expose your users and networks to targeted ads'; it does not say the path bypasses mail or web-filter controls."
- code: F4
  category: hallucinated-fact
  section: 2026-10-16/peerstitch-fortigate-implant-cve-2025-61624-fortimanager (Detection)
  item: "The implant leaves nothing on disk, so confirming it takes live forensics of miglogd and iked."
  url_or_quote: "https://unit42.paloaltonetworks.com/fortimanager-cve-2024-47575-peerstitch-malware/"
  summary: "Unit 42 says 'no persistent binary on disk' and shows the setup script downloading five files into /data2/template/ before lldprx unlinks itself; its own hunting table also lists config-revision audit (system.auto-script objects with ../) and 'diagnose debug crashlog read' queries, which are not live memory forensics."
- code: F4
  category: hallucinated-fact
  section: 2026-10-06/cve-2026-21589-atlassian-data-center-arbitrary-file-access (Update 2026-10-16T04:11:30Z; summary)
  item: "the earlier honeypot reports of attempts stand as the only public detail ...; Previdian's page, which on 2026-10-08 listed the flaw as not in the catalog, predates the listing"
  url_or_quote: "https://previdian.com/CVE-2026-21589"
  summary: "The same Previdian page, read this iteration and by the run, now reads 'Updated 16 Oct 2026', '607 Attempts observed', '65 Unique attacker IPs', '20 Attacker countries', '5 Sensors', 'Listed in CISA KEV', Shadowserver attestation 2026-10-14 00:00 UTC. The summary still carries the 2026-10-08 figures (129 attempts, 22 addresses) and the update calls them the only public detail; the exploitation delta (about 5x attempts, 3x addresses, second attester) was missed. Refresh figures with the current page and date."
- code: F4
  category: hallucinated-fact
  section: 2026-10-16/drupal-sa-core-2026-014-cve-2026-108097-field-ui-rce (Exposure)
  item: "any contributed module or custom code that renders Field UI tables from user-influenced input"
  url_or_quote: "https://thehackernews.com/2026/10/drupal-patches-critical-core-rce-flaw.html"
  summary: "(low confidence) THN says contributed modules open paths and 'custom code may also expose it'; 'renders Field UI tables from user-influenced input' is the entry's own inference stated as exposure fact. 'or on any end-of-life branch' is also broader than the advisory range (>= 8.9.0)."
- code: F5
  category: missing-citation
  section: 2026-10-10/ahsaycbs-cve-2026-105133-105134-exploited-webshells-xmrig (title, headline, summary, body)
  item: "Ahsay admits its August AhsayCBS patches were incomplete / The August patches did not close the flaws"
  url_or_quote: "https://www.ahsay.com/en/company/announcements/patch-cve-105133-105134-update"
  summary: "Ahsay's announcement says 'our previous patches v9.15.2.59 and v10.3.4.0' with no month; the cited SecurityWeek/Huntress/release-notes pages never call them August patches (10.3.4 release notes are dated 05-Aug-2026 and list no security fix). Only The Hacker News (https://thehackernews.com/2026/10/ahsaycbs-flaws-exploited-to-deploy-web.html: 'released in August 2026') dates them, and it is not cited. Cite THN or drop 'August'."
- code: F5
  category: missing-citation
  section: 2026-10-16/cl-unk-1211-ai-assisted-intrusions-government-linux-hosts (Detection)
  item: "Unit 42's own endpoint rule for the history tampering is named \"Uncommon attempt to clear shell history\"."
  url_or_quote: "https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/"
  summary: "True on the Unit 42 page but the sentence has no inline citation (the whole Detection paragraph is uncited)."
- code: F7
  category: drop
  section: 2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups
  item: "routine APAC incident with four body paragraphs plus a two-paragraph update"
  url_or_quote: "priority: routine; sources: no vector, no actor, no ransomware family; no Swiss nexus"
  summary: "check 5b: an incident with no access vector, no actor and no behaviour beyond its impact is routine and two sentences at most, or dropped. The entry is far longer and this run added 48-customer portal data classes (hashed password, fee totals) and zone names. Cut to two sentences keeping the supplier-concentration lesson, or drop."
- code: F8
  category: needs-more-research
  section: 2026-10-16/peerstitch-fortigate-implant-cve-2025-61624-fortimanager (Detection)
  item: "Detection omits Unit 42's own hunting guidance"
  url_or_quote: "https://unit42.paloaltonetworks.com/fortimanager-cve-2024-47575-peerstitch-malware/"
  summary: "Source table (Table 2) gives: anonymous 16,384-byte rwxp regions in /proc/<pid>/maps of miglogd and iked; NOP patches at three fixed offsets; cross-PID open()/write() on /proc/<pid>/mem; 'diagnose debug crashlog read' for Signal 11 in miglogd/iked/syslogd; auto-script objects with ../; also MDChallengeDns01 mapped to /bin/node and a ../../tmp/apache2/conf/md-acme.conf auto-script. The entry reduces this to 'live forensics'."
- code: F8
  category: needs-more-research
  section: 2026-10-16/cl-unk-1211-ai-assisted-intrusions-government-linux-hosts (body, Detection, Defender takeaway)
  item: "source-stated behaviours dropped"
  url_or_quote: "https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/"
  summary: "Unit 42 lists a custom Go scanner for CVE-2025-55182 (React2Shell), SSH authorized_keys key injection and sshpass lateral movement, MSSQL xp_cmdshell double-hop pivoting, GSocket gs-netcat in /dev/shm under a [kcached] name, reverse SOCKS tunnelers, and exfiltration to public file-hosting services. None appear in the body, Detection or takeaway; the React2Shell scanner is the only vulnerability lead to a likely entry route."
- code: F8
  category: needs-more-research
  section: 2026-10-10/ahsaycbs-cve-2026-105133-105134-exploited-webshells-xmrig (Update 2026-10-16T04:09:30Z; Detection; actions)
  item: "Bitdefender's second incident persistence"
  url_or_quote: "https://www.bitdefender.com/en-us/blog/businessinsights/technical-advisory-ahsaycbs-exploitation-chain-cve-2026-105133-cve-2026-105134"
  summary: "Bitdefender: in the second incident 'obfuscated PowerShell commands ... install and configure OpenSSH ... A working SSH service would give an attacker a way back in that does not depend on the vulnerable web service, which is why patching alone does not end the incident.' The update lists webshells, command files and SYSTEM elevation but drops the OpenSSH install, the one persistence artifact that survives the hotfix, and the staging on a static-site hosting subdomain."
- code: F8
  category: needs-more-research
  section: 2026-10-16/adfection-candiru-spyware-zero-click-ad-delivery (Detection)
  item: "in per-device web-proxy, DNS and egress logs the reported signature is contact with Discover-Tech infrastructure ..."
  url_or_quote: "https://blog.confiant.com/p/adint-weaponized-ad-tech-for-zero-click-spyware-and-mass-identity-vacuuming"
  summary: "Confiant (cited): the SDK resolves an operator-chosen domain over DoH and reaches it by raw IP, 'so it never appears as a plaintext DNS query or as a connection hostname, keeping it invisible to DNS-based monitoring and blocklists'. The entry cites only the WebSocket/WebRTC caveat and presents DNS logs as a sound signature without this limit."
- code: F8
  category: needs-more-research
  section: 2026-10-16/drupal-sa-core-2026-014-cve-2026-108097-field-ui-rce (cves[].affected)
  item: "Drupal core from 8.9.0 before 10.6.19, from 11.0.0 before 11.3.19 and from 11.4.0 before 11.4.10"
  url_or_quote: "https://www.drupal.org/sa-core-2026-014"
  summary: "(low confidence) Advisory 'Affected versions' also reads '>= 12.0.0-alpha1 < 12.0.0-beta2' and THN names 12.0.0-beta2 (not for production) as the fix; the entry omits the 12.0.0 pre-release line."
- code: F10
  category: missed-angle
  section: whole run
  item: "Beyond Gravity (Confederation-owned space supplier)"
  url_or_quote: "work/2026-10-16T0256Z-intel run record: 'SRF reports ... the company and the Confederation assume China is the attacker ... the Council of States' oversight committee chair said the committees were told of a data outflow'"
  summary: "(low confidence; I could not fetch the SRF item) The run record itself says S2 and S4 both recommended a short notable entry and that the item has the strongest federal nexus of the window; it was held for a gate reason (no evidence-bound techniques[]) rather than an editorial one. Suggested check before the 2026-10-20 expiry: WebSearch 'Beyond Gravity SRF China Datenabfluss GPK' and decide on a two-sentence routine entry if an honest techniques[] exists."
- code: F16
  category: org-triage
  section: 2026-10-16/drupal-sa-core-2026-014-cve-2026-108097-field-ui-rce (priority)
  item: "priority: high"
  url_or_quote: "Drupal: 'The vulnerability is not directly exploitable with core alone'; THN: 'In the week starting October 4, 90 sites reported using' Entity List"
  summary: "(low confidence) Unexploited flaw, no public exploit (E:Theoretical), core alone not reachable, the single named unauthenticated path runs through a contrib module used by 90 reporting sites, and the exposure depends on unknown contrib/custom code: close to the 'unexploited flaw reachable only in a non-default configuration' disqualifier for high. The pre-announcement warning and Swiss public-sector Drupal footprint argue for keeping it; main agent to confirm the call."
- code: F18
  category: action-item-discipline
  section: 2026-10-10/ahsaycbs-cve-2026-105133-105134-exploited-webshells-xmrig (actions[1])
  item: "check for the artifacts Huntress and Bitdefender describe (children of the service downloading into Temp folders, new .jsp files ..., command files in C:\\Users\\Public, a service that mimics the Edge updater)"
  url_or_quote: "actions[1]"
  summary: "(low confidence) The artifact list restates the Detection paragraph (check 10b b); the task is 'compromise-check every server reachable since 2026-10-04 and re-image confirmed hosts'."
- code: F14
  category: quantifier-without-source
  section: 2026-10-16/peerstitch-fortigate-implant-cve-2025-61624-fortimanager (headline, summary, body)
  item: "a FortiGate implant with no file on disk / leaves no binary on disk"
  url_or_quote: "https://unit42.paloaltonetworks.com/fortimanager-cve-2024-47575-peerstitch-malware/"
  summary: "Source: 'PEERSTITCH leaves no persistent binary on disk, opens no listening ports and initiates no outbound network connections.' The setup script downloaded pM.js, index.js, index.wasm, ipssem.js and the lldprx injector into /data2/template/ and lldprx then unlinked itself. 'no file on disk' and 'no binary on disk' drop 'persistent'."
- code: F14
  category: quantifier-without-source
  section: 2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow (Update 2026-10-16T04:11:00Z)
  item: "Police have warned of the first concrete misuse scenario."
  url_or_quote: "https://www.swisscybersecurity.net/news/2026-10-08/bundespensionskasse-publica-meldet-datenabfluss"
  summary: "No source says 'first'; SwissCybersecurity.net says the police 'formulieren ihre Warnung im Konjunktiv, scheinen also noch keinen Fall registriert zu haben', i.e. a hypothetical scenario, not a concrete one."
- code: F11
  category: editorial-advisory
  section: 2026-10-16/cl-unk-1211-ai-assisted-intrusions-government-linux-hosts (techniques[])
  item: "techniques[] omits clearly described behaviours"
  url_or_quote: "https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/"
  summary: "No ids for SSH authorized_keys injection (T1098.004), SSH lateral movement via sshpass (T1021.004), MSSQL xp_cmdshell pivot, reverse SOCKS tunnelers (T1090) or exfiltration to file-hosting services (T1567); all are stated in the source."
- code: F11
  category: editorial-advisory
  section: 2026-10-16/drupal-sa-core-2026-014-cve-2026-108097-field-ui-rce (sourcing_note)
  item: "the CVE record did not resolve at the CVE services when checked, and the identifier is taken from the advisory"
  url_or_quote: "sourcing_note"
  summary: "Narrates the pipeline's own lookup; the advisory page itself carries the CVE id (CVE-2026-108097), so provenance is one sentence: Drupal's advisory names the CVE and carries the affected and fixed versions, risk score and mitigation."
- code: F11
  category: editorial-advisory
  section: 2026-10-16/cl-unk-1211-ai-assisted-intrusions-government-linux-hosts (body)
  item: "(Unit 42 says its product stopped this) ... Unit 42's own endpoint rule ... named \"Uncommon attempt to clear shell history\""
  url_or_quote: "body"
  summary: "Vendor product-efficacy and detector-name material from a vendor blog; keep behaviour, drop the product claims."
- code: F11
  category: editorial-advisory
  section: 2026-10-10/ahsaycbs-cve-2026-105133-105134-exploited-webshells-xmrig (cves[].cvss)
  item: "cvss: \"medium (Huntress)\" / \"critical (Huntress)\""
  url_or_quote: "https://www.bitdefender.com/en-us/blog/businessinsights/technical-advisory-ahsaycbs-exploitation-chain-cve-2026-105133-cve-2026-105134"
  summary: "The cited Bitdefender page gives the CNA (VulDB) scores: CVE-2026-105133 7.3 High (CVSS 3.1) / 5.5 Medium (4.0); CVE-2026-105134 10.0 Critical (3.1) / 9.3 Critical (4.0). Record the numeric scores with their CNA."
- code: F11
  category: editorial-advisory
  section: 2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow (Update 2026-10-16T04:11:00Z)
  item: "The scope for other funds shifted."
  url_or_quote: "body"
  summary: "Vague narration sentence with no fact in it (BVK 'not directly affected'; Ticino fund no statement); state the fact instead."
```
