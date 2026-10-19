**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-19T18:09:14Z · ended_at=2026-10-19T18:36:28Z · duration_seconds=1634

## Verification report — 2026-10-11T1307Z-audit (iteration 7, slice s3)

Scope: 27 entries (26 audited existing entries and the new NeedyMantis entry), 233 ledger claims, 233 verdict rows written (228 ok, 3 F3, 1 F4, 1 F5; no unreadable). Post-fix pass: every claim of every entry was walked, including the entries remediated after iteration 6. Fetched this iteration: all 116 URLs cited in the 27 entries (cached bodies first, `extract` otherwise; raw `url` for Register, ZDI-26-342, Cisco advisories, Google blogs and GitHub advisories whose extracts dropped the facts checked; `ncsc-csh post 12622` for the NCSC-CH hub; `WebFetch` with the outbound-links template for the three cisa.gov alert pages; KEV JSON for every KEV claim). The ledger rows are in `verification.iter7.s3.claims.yaml`.

### Prior-iteration deltas (11 findings from iteration 6)

- SES F3 (PDFs held only payment details and supporting documentation): fix holds, body and Detection match Securelist.
- SES F4 ('in most cases' IAM keys, SES API credential contrast dropped): fix holds.
- NeedyMantis F4 (cookie 'oversized'): fix holds; Detection now says Base64-encoded compressed system information, no size.
- Cisco ISE F3 (triage and immediate action wording): fix holds against Cisco's advisory ('uploads that were initiated from the affected device to external IP addresses or downloads from malicious IP addresses').
- ShinyHunters F3 (exfiltration clause now cites Mandiant): fix holds. F4 (blanket assume-compromise action): fixed in the action but the same rule survives in the 2026-06-16 section (finding #5 below). F4 (/etc/hosts, authorized_keys): fix holds. F5 (Swiss membership): clause dropped, but 'Strasbourg' remains uncited (finding #10).
- ShieldBreak F11 (file-name indicator): decline rationale accepted for the 08-24 record summary (append-only record names the file); the same class is raised separately on the SimpleHelp entry where that argument does not apply (finding #18).
- RoguePlanet F3 (disclosure and PoC date 2026-06-09): fix holds against NCSC-CH post 12622 ('June 9th 2026 As part of Patch Tuesday'); the changelog does not declare the date move (finding #15).
- Sekoia F4 (action now names a hidden HTA file): fix holds, Sekoia and Infosecurity both describe the hidden HTA in the Startup directory.
- Instructure F5 (first sentence cites The Register): fix does NOT hold. The Register carries the 2026-04-29 detection date but not the 2026-05-01 disclosure date (finding #1).

### Citation does not support the claim

**#1 (F3)** `entries/2026-05-08/instructure-canvas-extortion-330-institutions-across-six-cou.md`
- Where: body, first sentence: 'Instructure detected unauthorized activity on 2026-04-29 and disclosed a security incident on 2026-05-01 ([The Register, 2026-05-12])'
- Finding: (low confidence) The Register page carries the 2026-04-29 detection date but not the 2026-05-01 disclosure date; the delta claims 'The Register, which carries both dates'. The only cited page that bears on the disclosure is BleepingComputer ('On Friday, Instructure disclosed', page dated 2026-05-03), which does not give the date either.
- Ground truth: Register: 'On April 29, the online education firm detected unauthorized activity in Canvas ... according to Instructure's notice'; no 'May 1', 'Friday' or disclosure date anywhere in the article. BC (2026-05-03): 'On Friday, Instructure disclosed that it suffered a cybersecurity incident'. (https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361)
- Fix: Cite BleepingComputer for the disclosure ('on Friday', 2026-05-01 by its dateline) or drop the 2026-05-01 date from the Register-cited clause.

**#2 (F3)** `entries/2026-05-13/cve-2026-41089-cve-2026-41096-cve-2026-41103-cve-2026-42898.md`
- Where: Detection: 'the indicators Automox lists ... are unexpected Netlogon service crashes or restarts, Netlogon traffic from source addresses that are not domain controllers, and authentication failures ...' ([Help Net Security, 2026-06-01])
- Finding: (low confidence) Help Net Security lists 'Anomalous Netlogon traffic patterns from non-DC source addresses'. The entry drops 'anomalous ... patterns', so as written the indicator matches ordinary member-to-DC Netlogon traffic (every domain-joined host talks Netlogon to a DC) and gives a hunter no usable discriminator.
- Ground truth: HNS 2026-06-01: 'Jason Kikta ... outlined events that might point to active exploitation: The Netlogon service unexpectedly crashing or restarting; Anomalous Netlogon traffic patterns from non-DC source addresses; Authentication failures or domain trust errors immediately after suspicious network activity hits a domain controller'. (https://www.helpnetsecurity.com/2026/06/01/windows-netlogon-rce-exploited-cve-2026-41089/)
- Fix: Write 'anomalous Netlogon traffic patterns from non-DC source addresses', as Automox does.

**#3 (F3)** `entries/2026-10-11/needymantis-modular-post-compromise-framework-storm-3069.md`
- Where: body paragraph 1 and summary: 'it has seen further NeedyMantis activity beyond Storm-3069 and assesses the activity originates from China without attributing it to a Chinese nation-state actor'; summary: 'Storm-3069 ... is one operator; Microsoft assesses the activity originates from China without attributing it to a nation-state actor.'
- Finding: (low confidence) Microsoft's non-attribution statement is about Storm-3069 only ('it has not attributed Storm-3069 to a Chinese nation-state actor'). For the additional NeedyMantis activity Microsoft says only that it 'has thus far aligned with activity Microsoft associates with threat actors operating from China'. The entry's sentence puts the China-origin assessment and the no-nation-state statement on 'the activity' as a whole, so the scope of both is wider than the source.
- Ground truth: Microsoft blog: 'While Microsoft assesses the activity originates from China, it has not attributed Storm-3069 to a Chinese nation-state actor.' / 'Observed activity involving NeedyMantis has thus far aligned with activity Microsoft associates with threat actors operating from China ... Microsoft has not determined whether all observed activity is attributable to the same threat actor'. (https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/)
- Fix: Say: Microsoft assesses Storm-3069's activity originates from China without attributing it to a nation-state actor, and the further NeedyMantis activity it has seen aligns with activity it associates with China-based actors; it has not determined whether one operator is behind all of it.

**#4 (F3)** `entries/2026-05-09/daemon-tools-lite-supply-chain-quic-rat-deployed-via-signed.md`
- Where: frontmatter summary, last sentence: 'Version 12.6.0.2445 is clean.'
- Finding: (low confidence) Kaspersky says the vendor 'published a new software version intended to address it' and that release 12.6.0.2445 'no longer includes the malicious behavior described in this article'. 'Is clean' is a stronger, unqualified statement than the source makes; the body correctly says the version 'no longer contains the malicious behaviour'.
- Ground truth: Securelist update 5/6/26: 'Following a disclosure, the vendor acknowledged the issue and published a new software version intended to address it. The updated release 12.6.0.2445 no longer includes the malicious behavior described in this article.' (https://securelist.com/tr/daemon-tools-backdoor/119654/)
- Fix: Write 'Version 12.6.0.2445 no longer contains the malicious behaviour Kaspersky describes.'

### Unsupported / hallucinated facts

**#5 (F4)** `entries/2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md`
- Where: body, '## Update — 2026-06-16T05:09:02Z', second paragraph: 'treat any externally-reachable PeopleSoft Environment Management Hub as compromised pending forensic review and block perimeter access to /PSEMHUB/*'
- Finding: (low confidence) Same blanket assume-compromise rule that iteration 6 found unsupported in the action (remediated there: 'treat hosts with a web shell as compromised, as Mandiant does'), still present in this section. No cited source says an exposed hub is to be treated as compromised: Mandiant's June guidance is block/disable plus log review; its September guidance makes 'treat the host as compromised' conditional on finding a web shell; Rapid7 says investigate for signs of compromise.
- Ground truth: Mandiant 2026-09-25: 'Organizations that identify a web shell should treat the host as compromised, preserve evidence, and rotate all credentials accessible from the PeopleSoft tier'. Mandiant 2026-06-11: 'If you cannot disable the EMHub Service, immediately block external network access to /PSEMHUB/*' ... 'Audit the PIA WebLogic access logs'. (https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/)
- Fix: Reword to 'investigate any externally-reachable hub for compromise and block perimeter access', matching the action.

**#6 (F4)** `entries/2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md`
- Where: body, Post-access lateral movement paragraph, first sentence after the bold lead: 'The better-evidenced, and more directly defender-actionable, phase is what follows initial access.'
- Finding: (low confidence) Legacy framing from when the initial-access flaw was attacker-asserted. This fire's correction rewrote the Access paragraph to state Oracle's confirmation of CVE-2026-35273 (CVSS 9.8) and Mandiant's zero-day dating, but kept the comparative; the initial-access step is now the best-evidenced one (vendor alert, CVE, Mandiant attribution). The sentence is uncited and the newest sections disprove it.
- Ground truth: Oracle alert 2026-06-10 (CVE-2026-35273, 9.8, remotely exploitable without authentication); Mandiant 2026-06-11: 'consistent with the exploitation of CVE-2026-35273 ... exploited as a zero-day'. (https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)
- Fix: Delete the comparative or reword to 'The phase with the most defender-actionable telemetry is what follows initial access.'

**#7 (F4)** `entries/2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix.md`
- Where: body, '## Update — 2026-08-18T04:45:00Z', **Detection, telemetry class first.** paragraph: 'The durable anchor remains process-creation telemetry with parent lineage: the Malware Protection Engine has no legitimate reason to be the parent of an interactive shell or an unexpected child process, so any such process tree rooted at the engine is the signal irrespective of which variant produced it. **Triage:** ... a shell parented to it does not have a benign counterpart'
- Finding: (low confidence) This fire rewrote the paragraph's lead-in but kept its guidance. No cited source supports it (the paragraph has no citation), and the entry's own later sections show it is wrong for ShieldBreak: LevelBlue's mechanism has Defender's engine write the DLL into System32 and a Windows Error Reporting scheduled task make wermgr.exe load it as SYSTEM, so no interactive shell is parented to the engine, and the 2026-08-21 Triage line says MsMpEng.exe writing into System32 is normal and the discriminator is the sequence. A hunter following the 08-18 anchor would look for the wrong parent-child shape (4c(h) supersession; the section was not marked superseded).
- Ground truth: LevelBlue 2026-08-19: 'ShieldBreak then triggers the QueueReporting task, causing wermgr.exe to execute phoneinfo.dll as SYSTEM'; 'telemetry can show MsMpEng.exe as the process responsible for the file write. That is expected from the exploit's design'; 'ShieldBreak is best detected through behavioral correlation rather than any single static indicator.'
- Fix: Delete the 08-18 Detection/Triage sentences, or mark them as the disclosure-day hypothesis superseded by the 08-21 and 08-24 sections (and by the main analysis Detection line).

**#8 (F4)** `entries/2026-09-25/switzerland-sovereign-digital-infrastructure-motion-24-3209.md`
- Where: frontmatter summary: 'The motion instructs the Federal Council to submit a legal revision enabling a federally co-financed sovereign cloud service and an independent data-exchange platform to host administration, industry and critical-infrastructure data inside Switzerland'
- Finding: (low confidence) The summary drops the source's hedge. Laux Lawyers (the cited source for the motion text) says the infrastructure is meant to host the data 'möglichst in der Schweiz' (where possible); this fire's own Correction and body stress 'where possible' because the earlier text over-read the motion as a hosting requirement, but the summary, which readers and agents see first, still states the hosting inside Switzerland flatly.
- Ground truth: Laux Lawyers: 'Vorgesehen sind insbesondere ein eigenständiger Cloud-Dienst sowie eine unabhängige Austauschplattform, um Daten von Unternehmen, Verwaltung und kritischen Infrastrukturen möglichst in der Schweiz zu hosten.' (https://www.lauxlawyers.ch/it-recht-in-der-herbstsession-2026/)
- Fix: Write '... to host administration, industry and critical-infrastructure data in Switzerland where possible' in the summary.

### Claims missing inline citation

**#9 (F5)** `entries/2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md`
- Where: body, Detection and hunting concepts, second sentence: 'On the application tier, alert on anomalous bulk-query volumes or out-of-hours mass record retrieval in PeopleTools security-audit logs, and on egress anomalies consistent with bulk data transfer to non-standard destinations.'
- Finding: (low confidence) Uncited and not marked analyst judgement, unlike the adjacent authorized_keys and hardening sentences this fire marked. The nearest source support is Mandiant's September 'Hunt for Evidence of Data Theft' ('Review database audit logs for bulk queries or exports against HR, payroll, and student records tables, and network logs for large or sustained outbound transfers'), which names database audit logs, not 'PeopleTools security-audit logs'. The first sentence also says SSH attempts from 'external' sources although the recovered script runs from the compromised PeopleSoft host against internal hosts.
- Ground truth: Mandiant 2026-09-25 Hunt for Evidence of Data Theft: 'Review database audit logs for bulk queries or exports against HR, payroll, and student records tables, and network logs for large or sustained outbound transfers from the PeopleSoft tier'. Mandiant 2026-06-11: the fanout script is written to /tmp on the compromised host and sprays SSH against internal hosts parsed from /etc/hosts. (https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/)
- Fix: Cite Mandiant's data-theft hunting paragraph (and say database audit logs) or mark the sentence 'in analyst judgement'; drop 'external' from the SSH-source clause.

**#10 (F5)** `entries/2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md`
- Where: body, '## Update — 2026-06-16T05:09:02Z': 'the 46-member Strasbourg human-rights body'
- Finding: (low confidence) 'Strasbourg' is in none of the three cited pages (SecurityWeek, The Register, BleepingComputer); they give 46 member states and 'Europe's leading human rights organization'. Minor, true in the world but uncited; the iteration-6 remediation dropped only the Swiss clause.
- Ground truth: SecurityWeek 2026-06-15: 'Europe's leading human rights organization ... includes 46 member states, including 27 European Union countries.' No 'Strasbourg'. (https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/)
- Fix: Drop 'Strasbourg' or say 'the 46-member-state human-rights organization'.

### Needs more research

**#11 (F8)** `entries/2026-09-04/cve-2026-20212-cisco-nexus-9000-s1hal-unauth-root-rce.md`
- Where: body paragraph 1 ('inventory should key on the ten Silicon One product IDs rather than on the Nexus 9000 family name') and actions[0] ('Run show module on every Nexus 9000 switch ... upgrade those')
- Finding: (low confidence) Cisco's 'Products Confirmed Not Vulnerable' list includes 'Nexus 9000 Series Fabric Switches in ACI mode'. The entry reproduces the Nexus 3000 and other-model exclusions but drops the ACI-mode exclusion, so a responder following the PID-only inventory rule and the action would count ACI-mode fabric units (the chassis PIDs N9K-C9804/9808 also run ACI) as exposed. The exposure test that follows from the cited advisory is: listed PID and standalone NX-OS mode.
- Ground truth: Cisco advisory, Products Confirmed Not Vulnerable: '... Nexus 9000 Series Switches other than the models listed in the Vulnerable Products section; Nexus 9000 Series Fabric Switches in ACI mode; ...'. (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9k-s1-rce-EH8dEtr)
- Fix: Add to the exposure sentence: Cisco lists Nexus 9000 fabric switches in ACI mode as not vulnerable, so the affected set is the ten PIDs running NX-OS; adjust the action's first clause accordingly (or add an Exposure line).

### Surface contradiction

**#12 (F9)** `entries/2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix.md`
- Where: frontmatter cves[CVE-2026-50656].fixed: 'Engine build 1.1.26060.3008, shipped 2026-07-09' and body 'was fixed in engine build 1.1.26060.3008 on 2026-07-09' (cited sentence follows to Cyber Kendra)
- Finding: (low confidence) Cyber Kendra says 'shipped engine build 1.1.26060.3008 on July 9'; Microsoft's own record for CVE-2026-50656 shows its revision announcing the shipped engine update dated Jul 8, 2026, and the sibling RoguePlanet entry in this store says 'a revision dated 2026-07-08 confirms Microsoft has now shipped'. The per-CVE authority is a day earlier than the date this entry states without a Contradiction line; cves[] was in this fire's changed fields.
- Ground truth: MSRC CVE-2026-50656: 'Last updated: Jul 8, 2026' ... Revisions: 'Jul 8, 2026 Microsoft has released an update to the Microsoft Malware Protection Engine that addresses the vulnerability identified by CVE-2026-50656'. (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656)
- Fix: Write 'shipped 2026-07-08 per Microsoft's revision (Cyber Kendra reports 9 July)' or drop the day from cves[].fixed and the sentence.

### Editorial / less-is-more flags (advisory)

**#13 (F11)** `entries/2026-06-02/sekoia-consolidates-gamaredon-tooling-under-gammaphish-gamma.md`
- Where: updates[] record 2026-10-11T14:56:35Z (internal: true): summary 'Adds references to the WinRAR and Turla entries...' with fields [references, actions]
- Finding: (advisory, low confidence) The record's fields name actions and git diff shows actions[0] reworded ('.exe/.vbs' to 'a hidden HTA file'), but the summary mentions only the references. An internal record that also changes reader-facing action text should say so (or be a correction).
- Ground truth: git diff HEAD: actions[0] '... alert on archive utilities writing `.exe`/`.vbs` into `Programs\Startup`' -> '... writing a hidden HTA file into `Programs\Startup`'. Sekoia: 'extract a hidden HTA file directly into the user's Windows Startup directory'. (https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/)
- Fix: Add a clause to the record summary: 'the Startup-folder alert now names the hidden HTA file the sources describe'.

**#14 (F11)** `entries/2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md`
- Where: body, Post-access lateral movement paragraph: 'stolen directories are compressed with zstd before they leave' and, three sentences later, 'Mandiant records the stolen directories compressed with zstd and an outbound SSH connection'
- Finding: (advisory) The zstd exfiltration fact is stated twice in one paragraph (this fire inserted the first sentence and rewrote the second), and em dashes remain in the title-adjacent legacy text of earlier sections.
- Ground truth: Mandiant 2026-06-11: 'Compressed exfiltrated directories containing stolen data using zstd ... establishing an outbound SSH connection ... to 176.120.22.24'. (https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)
- Fix: Delete the standalone 'Mandiant documents the exfiltration step separately' sentence.

**#15 (F11)** `entries/2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md`
- Where: Correction 2026-10-11T14:55:23Z and its record summary: the PoC/disclosure date changed from 2026-06-10 to 2026-06-09 in the summary and main analysis (git diff) but neither the section nor the record summary says so
- Finding: (advisory, low confidence) A reader-facing date moved by one day in the summary and body. The record fields name summary and body, but the record summary and the Correction section list the other changes and omit the date fix, so the changelog does not declare everything that moved.
- Ground truth: git diff HEAD: '- A public PoC existed from 2026-06-10' -> '+ A public PoC existed from 2026-06-09'; body 'first disclosed RoguePlanet as an unpatched zero-day on 2026-06-10' -> '2026-06-09, Patch Tuesday'. NCSC-CH post 12622 files RoguePlanet under 'June 9th 2026 As part of Patch Tuesday'. (https://security-hub.ncsc.admin.ch/#/posts/12622)
- Fix: Add one sentence to the Correction and the record summary: the disclosure and public-PoC date is 2026-06-09, Patch Tuesday, not 2026-06-10.

**#16 (F11)** `entries/2026-06-02/sekoia-consolidates-gamaredon-tooling-under-gammaphish-gamma.md`
- Where: frontmatter summary: '...introducing unified naming for two capability clusters: GammaPhish (the funnel from …'
- Finding: (advisory, low confidence) The summary field is cut off mid-sentence with an ellipsis ('introducing unified naming for two capability clusters: GammaPhish (the funnel from …'), so the card text shown to readers and agents is a truncated fragment. Legacy text that this fire left in place while it edited the same entry's references and actions.
- Ground truth: Entry frontmatter summary: '...two capability clusters: GammaPhish (the funnel from …'
- Fix: Rewrite the summary as a complete two-sentence statement from the Sekoia report (GammaPhish and GammaWorm naming, CVE-2025-8088 delivery into the Startup folder) via a changelog record.

**#17 (F11)** `entries/2026-09-17/mandiant-ai-risk-resilience-report-2026.md`
- Where: em dashes in reader-facing text this fire rewrote or re-wrapped: Mandiant AI entry body (about 10 lines, e.g. 'its most operationally useful content for defenders — each pairs an attack pattern ...', 'Case study 1 — ...' bold leads, '(T1027.010) — never writing ...'); also ShieldBreak body (7 re-wrapped lines and title/headline), WinRAR first paragraph ('CVE-2025-8088 — a path traversal ... — nearly a year'), ShinyHunters 06-16 section ('Council of Europe — the 46-member ...'), RoguePlanet first paragraph ('closes it — last vulnerable ...'), Oracle EBS second paragraph (two), Cisco ISE Triage line ('signal — and because ...')
- Finding: (advisory) Definition check 12: no em dash in reader-facing entry text (only the '## <Type> — <at>' heading is exempt). The listed text sits in paragraphs this fire edited, so it was open to a clean-up in the same pass. Advisory only; the main agent may leave it.
- Ground truth: git diff HEAD '+' lines containing U+2014 outside '## ' headings: Mandiant AI 10, ShieldBreak 7, ShinyHunters 1, WinRAR 1, RoguePlanet 1, Oracle EBS 1, Cisco ISE 1.
- Fix: Replace the dashes with commas, colons or full stops in the paragraphs this fire already touched.

**#18 (F11)** `entries/2026-06-30/cve-2026-48558-simplehelp-rmm-oidc-sso-authentication-bypass.md`
- Where: body paragraph 2: 'an obfuscated `jquery.js` fetched from a temporary Cloudflare domain delivered the TaskWeaver loader'
- Finding: (advisory, low confidence) The loader's masquerade file name is a file-name indicator of the kind the style rule bars ('no hashes, IPs, attacker domains, mutex or file-name indicators'); the entry elsewhere describes behaviour in prose. Sits in this fire's rewrite. Same class as the ShieldBreak phoneinfo.dll decision (declined there on an append-only-record argument that does not apply here).
- Ground truth: Blackpoint: 'jquery.js, retrieved from a temporary Cloudflare hosted URL and executed through node.exe'; BC: 'an obfuscated JavaScript file named jquery.js'. (https://blackpointcyber.com/blog/a-djinn-in-the-machine-taskweavers-node-js-intrusion-chain/)
- Fix: Say 'an obfuscated JavaScript loader named to resemble a jQuery library, fetched from a temporary Cloudflare domain and run through Node.js'.

### Action-item discipline

**#19 (F18)** `entries/2026-09-17/cve-2026-76460-cisco-ise-auth-bypass-root-rce.md`
- Where: actions[1]: 'Review access.log on every ISE node (or pull a support bundle with debug logs for apigateway/access.log.*.gz) for suspicious usernames on the API endpoint, and cross-check firewall and network logs outside the ISE appliance ... Re-image any node where malicious activity is suspected'
- Finding: (low confidence) check 10b(b): the action restates the body's Defender takeaway paragraph and the immediate_action text almost word for word (access.log review, off-box log cross-check, re-image), so the aggregated Action Items list carries the same task three times (immediate_action, actions[0] ACL/patch, actions[1] log review). Keep actions[0]; the log-review task is already the immediate_action's second half.
- Ground truth: Body Defender takeaway: 'review each node's access.log (or a decrypted debug-log bundle at ./ise/logs/apigateway/access.log.*.gz) for suspicious usernames ... If malicious activity is suspected, Cisco strongly recommends re-imaging'; immediate_action carries the same two steps. (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5)
- Fix: Drop actions[1], or reduce the list to one action and let immediate_action carry the log-review and re-image steps.

### Verdict

NEEDS_FIXES (truth: 8, editorial: 5, advisory: 6)

Truth = F3 x4 (Instructure, Netlogon, NeedyMantis, DAEMON Tools) + F4 x4 (ShinyHunters x2, ShieldBreak, Swiss motion). Editorial = F5 x2 + F8 x1 + F9 x1 + F18 x1. Advisory = F11 x6. Every truth and editorial finding but the Instructure F3 is marked low confidence; each rests on a quoted passage from a page fetched this iteration. No broken URLs, no hallucinated CVE ids or CVSS values, every KEV claim matches the KEV catalogue, every checked evidence quote is a verbatim substring of its page (the Curia Vista quote differs from the raw JSON only by a JSON unicode escape). Coverage of the audited slice looks complete; no missed-angle finding.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  entry: entries/2026-05-08/instructure-canvas-extortion-330-institutions-across-six-cou.md
  where: 'body, first sentence: ''Instructure detected unauthorized activity on 2026-04-29 and disclosed a security incident on 2026-05-01 ([The Register, 2026-05-12])'''
  summary: (low confidence) The Register page carries the 2026-04-29 detection date but not the 2026-05-01 disclosure date; the delta claims 'The Register, which carries both dates'.
    The only cited page that bears on the disclosure is BleepingComputer ('On Friday, Instructure disclosed', page dated 2026-05-03), which does not give the date either.
  ground_truth: 'Register: ''On April 29, the online education firm detected unauthorized activity in Canvas ... according to Instructure''s notice''; no ''May 1'', ''Friday'' or disclosure
    date anywhere in the article. BC (2026-05-03): ''On Friday, Instructure disclosed that it suffered a cybersecurity incident''.'
  ground_truth_url: https://www.theregister.com/security/2026/05/12/double-canvas-intrusion-confirmed-as-shinyhunters-resets-leak-deadline/5238361
  fix: Cite BleepingComputer for the disclosure ('on Friday', 2026-05-01 by its dateline) or drop the 2026-05-01 date from the Register-cited clause.
- code: F3
  category: claim-not-supported
  entry: entries/2026-05-13/cve-2026-41089-cve-2026-41096-cve-2026-41103-cve-2026-42898.md
  where: 'Detection: ''the indicators Automox lists ... are unexpected Netlogon service crashes or restarts, Netlogon traffic from source addresses that are not domain controllers, and
    authentication failures ...'' ([Help Net Security, 2026-06-01])'
  summary: (low confidence) Help Net Security lists 'Anomalous Netlogon traffic patterns from non-DC source addresses'. The entry drops 'anomalous ... patterns', so as written the indicator
    matches ordinary member-to-DC Netlogon traffic (every domain-joined host talks Netlogon to a DC) and gives a hunter no usable discriminator.
  ground_truth: 'HNS 2026-06-01: ''Jason Kikta ... outlined events that might point to active exploitation: The Netlogon service unexpectedly crashing or restarting; Anomalous Netlogon
    traffic patterns from non-DC source addresses; Authentication failures or domain trust errors immediately after suspicious network activity hits a domain controller''.'
  ground_truth_url: https://www.helpnetsecurity.com/2026/06/01/windows-netlogon-rce-exploited-cve-2026-41089/
  fix: Write 'anomalous Netlogon traffic patterns from non-DC source addresses', as Automox does.
- code: F11
  category: editorial-advisory
  entry: entries/2026-06-02/sekoia-consolidates-gamaredon-tooling-under-gammaphish-gamma.md
  where: 'updates[] record 2026-10-11T14:56:35Z (internal: true): summary ''Adds references to the WinRAR and Turla entries...'' with fields [references, actions]'
  summary: (advisory, low confidence) The record's fields name actions and git diff shows actions[0] reworded ('.exe/.vbs' to 'a hidden HTA file'), but the summary mentions only the
    references. An internal record that also changes reader-facing action text should say so (or be a correction).
  ground_truth: 'git diff HEAD: actions[0] ''... alert on archive utilities writing `.exe`/`.vbs` into `Programs\Startup`'' -> ''... writing a hidden HTA file into `Programs\Startup`''.
    Sekoia: ''extract a hidden HTA file directly into the user''s Windows Startup directory''.'
  ground_truth_url: https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/
  fix: 'Add a clause to the record summary: ''the Startup-folder alert now names the hidden HTA file the sources describe''.'
- code: F4
  category: hallucinated-fact
  entry: entries/2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md
  where: 'body, ''## Update — 2026-06-16T05:09:02Z'', second paragraph: ''treat any externally-reachable PeopleSoft Environment Management Hub as compromised pending forensic review
    and block perimeter access to /PSEMHUB/*'''
  summary: '(low confidence) Same blanket assume-compromise rule that iteration 6 found unsupported in the action (remediated there: ''treat hosts with a web shell as compromised, as
    Mandiant does''), still present in this section. No cited source says an exposed hub is to be treated as compromised: Mandiant''s June guidance is block/disable plus log review;
    its September guidance makes ''treat the host as compromised'' conditional on finding a web shell; Rapid7 says investigate for signs of compromise.'
  ground_truth: 'Mandiant 2026-09-25: ''Organizations that identify a web shell should treat the host as compromised, preserve evidence, and rotate all credentials accessible from the
    PeopleSoft tier''. Mandiant 2026-06-11: ''If you cannot disable the EMHub Service, immediately block external network access to /PSEMHUB/*'' ... ''Audit the PIA WebLogic access logs''.'
  ground_truth_url: https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/
  fix: Reword to 'investigate any externally-reachable hub for compromise and block perimeter access', matching the action.
- code: F4
  category: hallucinated-fact
  entry: entries/2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md
  where: 'body, Post-access lateral movement paragraph, first sentence after the bold lead: ''The better-evidenced, and more directly defender-actionable, phase is what follows initial
    access.'''
  summary: (low confidence) Legacy framing from when the initial-access flaw was attacker-asserted. This fire's correction rewrote the Access paragraph to state Oracle's confirmation
    of CVE-2026-35273 (CVSS 9.8) and Mandiant's zero-day dating, but kept the comparative; the initial-access step is now the best-evidenced one (vendor alert, CVE, Mandiant attribution).
    The sentence is uncited and the newest sections disprove it.
  ground_truth: 'Oracle alert 2026-06-10 (CVE-2026-35273, 9.8, remotely exploitable without authentication); Mandiant 2026-06-11: ''consistent with the exploitation of CVE-2026-35273
    ... exploited as a zero-day''.'
  ground_truth_url: https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/
  fix: Delete the comparative or reword to 'The phase with the most defender-actionable telemetry is what follows initial access.'
- code: F5
  category: missing-citation
  entry: entries/2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md
  where: 'body, Detection and hunting concepts, second sentence: ''On the application tier, alert on anomalous bulk-query volumes or out-of-hours mass record retrieval in PeopleTools
    security-audit logs, and on egress anomalies consistent with bulk data transfer to non-standard destinations.'''
  summary: (low confidence) Uncited and not marked analyst judgement, unlike the adjacent authorized_keys and hardening sentences this fire marked. The nearest source support is Mandiant's
    September 'Hunt for Evidence of Data Theft' ('Review database audit logs for bulk queries or exports against HR, payroll, and student records tables, and network logs for large or
    sustained outbound transfers'), which names database audit logs, not 'PeopleTools security-audit logs'. The first sentence also says SSH attempts from 'external' sources although
    the recovered script runs from the compromised PeopleSoft host against internal hosts.
  ground_truth: 'Mandiant 2026-09-25 Hunt for Evidence of Data Theft: ''Review database audit logs for bulk queries or exports against HR, payroll, and student records tables, and network
    logs for large or sustained outbound transfers from the PeopleSoft tier''. Mandiant 2026-06-11: the fanout script is written to /tmp on the compromised host and sprays SSH against
    internal hosts parsed from /etc/hosts.'
  ground_truth_url: https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/
  fix: Cite Mandiant's data-theft hunting paragraph (and say database audit logs) or mark the sentence 'in analyst judgement'; drop 'external' from the SSH-source clause.
- code: F5
  category: missing-citation
  entry: entries/2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md
  where: 'body, ''## Update — 2026-06-16T05:09:02Z'': ''the 46-member Strasbourg human-rights body'''
  summary: (low confidence) 'Strasbourg' is in none of the three cited pages (SecurityWeek, The Register, BleepingComputer); they give 46 member states and 'Europe's leading human rights
    organization'. Minor, true in the world but uncited; the iteration-6 remediation dropped only the Swiss clause.
  ground_truth: 'SecurityWeek 2026-06-15: ''Europe''s leading human rights organization ... includes 46 member states, including 27 European Union countries.'' No ''Strasbourg''.'
  ground_truth_url: https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/
  fix: Drop 'Strasbourg' or say 'the 46-member-state human-rights organization'.
- code: F11
  category: editorial-advisory
  entry: entries/2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md
  where: 'body, Post-access lateral movement paragraph: ''stolen directories are compressed with zstd before they leave'' and, three sentences later, ''Mandiant records the stolen directories
    compressed with zstd and an outbound SSH connection'''
  summary: (advisory) The zstd exfiltration fact is stated twice in one paragraph (this fire inserted the first sentence and rewrote the second), and em dashes remain in the title-adjacent
    legacy text of earlier sections.
  ground_truth: 'Mandiant 2026-06-11: ''Compressed exfiltrated directories containing stolen data using zstd ... establishing an outbound SSH connection ... to 176.120.22.24''.'
  ground_truth_url: https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/
  fix: Delete the standalone 'Mandiant documents the exfiltration step separately' sentence.
- code: F11
  category: editorial-advisory
  entry: entries/2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md
  where: 'Correction 2026-10-11T14:55:23Z and its record summary: the PoC/disclosure date changed from 2026-06-10 to 2026-06-09 in the summary and main analysis (git diff) but neither
    the section nor the record summary says so'
  summary: (advisory, low confidence) A reader-facing date moved by one day in the summary and body. The record fields name summary and body, but the record summary and the Correction
    section list the other changes and omit the date fix, so the changelog does not declare everything that moved.
  ground_truth: 'git diff HEAD: ''- A public PoC existed from 2026-06-10'' -> ''+ A public PoC existed from 2026-06-09''; body ''first disclosed RoguePlanet as an unpatched zero-day
    on 2026-06-10'' -> ''2026-06-09, Patch Tuesday''. NCSC-CH post 12622 files RoguePlanet under ''June 9th 2026 As part of Patch Tuesday''.'
  ground_truth_url: https://security-hub.ncsc.admin.ch/#/posts/12622
  fix: 'Add one sentence to the Correction and the record summary: the disclosure and public-PoC date is 2026-06-09, Patch Tuesday, not 2026-06-10.'
- code: F4
  category: hallucinated-fact
  entry: entries/2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix.md
  where: 'body, ''## Update — 2026-08-18T04:45:00Z'', **Detection, telemetry class first.** paragraph: ''The durable anchor remains process-creation telemetry with parent lineage: the
    Malware Protection Engine has no legitimate reason to be the parent of an interactive shell or an unexpected child process, so any such process tree rooted at the engine is the signal
    irrespective of which variant produced it. **Triage:** ... a shell parented to it does not have a benign counterpart'''
  summary: '(low confidence) This fire rewrote the paragraph''s lead-in but kept its guidance. No cited source supports it (the paragraph has no citation), and the entry''s own later
    sections show it is wrong for ShieldBreak: LevelBlue''s mechanism has Defender''s engine write the DLL into System32 and a Windows Error Reporting scheduled task make wermgr.exe
    load it as SYSTEM, so no interactive shell is parented to the engine, and the 2026-08-21 Triage line says MsMpEng.exe writing into System32 is normal and the discriminator is the
    sequence. A hunter following the 08-18 anchor would look for the wrong parent-child shape (4c(h) supersession; the section was not marked superseded).'
  ground_truth: 'LevelBlue 2026-08-19: ''ShieldBreak then triggers the QueueReporting task, causing wermgr.exe to execute phoneinfo.dll as SYSTEM''; ''telemetry can show MsMpEng.exe
    as the process responsible for the file write. That is expected from the exploit''s design''; ''ShieldBreak is best detected through behavioral correlation rather than any single
    static indicator.'''
  ground_truth_url: null
  fix: Delete the 08-18 Detection/Triage sentences, or mark them as the disclosure-day hypothesis superseded by the 08-21 and 08-24 sections (and by the main analysis Detection line).
- code: F9
  category: surface-contradiction
  entry: entries/2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix.md
  where: 'frontmatter cves[CVE-2026-50656].fixed: ''Engine build 1.1.26060.3008, shipped 2026-07-09'' and body ''was fixed in engine build 1.1.26060.3008 on 2026-07-09'' (cited sentence
    follows to Cyber Kendra)'
  summary: (low confidence) Cyber Kendra says 'shipped engine build 1.1.26060.3008 on July 9'; Microsoft's own record for CVE-2026-50656 shows its revision announcing the shipped engine
    update dated Jul 8, 2026, and the sibling RoguePlanet entry in this store says 'a revision dated 2026-07-08 confirms Microsoft has now shipped'. The per-CVE authority is a day earlier
    than the date this entry states without a Contradiction line; cves[] was in this fire's changed fields.
  ground_truth: 'MSRC CVE-2026-50656: ''Last updated: Jul 8, 2026'' ... Revisions: ''Jul 8, 2026 Microsoft has released an update to the Microsoft Malware Protection Engine that addresses
    the vulnerability identified by CVE-2026-50656''.'
  ground_truth_url: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656
  fix: Write 'shipped 2026-07-08 per Microsoft's revision (Cyber Kendra reports 9 July)' or drop the day from cves[].fixed and the sentence.
- code: F8
  category: needs-more-research
  entry: entries/2026-09-04/cve-2026-20212-cisco-nexus-9000-s1hal-unauth-root-rce.md
  where: body paragraph 1 ('inventory should key on the ten Silicon One product IDs rather than on the Nexus 9000 family name') and actions[0] ('Run show module on every Nexus 9000 switch
    ... upgrade those')
  summary: '(low confidence) Cisco''s ''Products Confirmed Not Vulnerable'' list includes ''Nexus 9000 Series Fabric Switches in ACI mode''. The entry reproduces the Nexus 3000 and other-model
    exclusions but drops the ACI-mode exclusion, so a responder following the PID-only inventory rule and the action would count ACI-mode fabric units (the chassis PIDs N9K-C9804/9808
    also run ACI) as exposed. The exposure test that follows from the cited advisory is: listed PID and standalone NX-OS mode.'
  ground_truth: 'Cisco advisory, Products Confirmed Not Vulnerable: ''... Nexus 9000 Series Switches other than the models listed in the Vulnerable Products section; Nexus 9000 Series
    Fabric Switches in ACI mode; ...''.'
  ground_truth_url: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9k-s1-rce-EH8dEtr
  fix: 'Add to the exposure sentence: Cisco lists Nexus 9000 fabric switches in ACI mode as not vulnerable, so the affected set is the ten PIDs running NX-OS; adjust the action''s first
    clause accordingly (or add an Exposure line).'
- code: F4
  category: hallucinated-fact
  entry: entries/2026-09-25/switzerland-sovereign-digital-infrastructure-motion-24-3209.md
  where: 'frontmatter summary: ''The motion instructs the Federal Council to submit a legal revision enabling a federally co-financed sovereign cloud service and an independent data-exchange
    platform to host administration, industry and critical-infrastructure data inside Switzerland'''
  summary: (low confidence) The summary drops the source's hedge. Laux Lawyers (the cited source for the motion text) says the infrastructure is meant to host the data 'möglichst in
    der Schweiz' (where possible); this fire's own Correction and body stress 'where possible' because the earlier text over-read the motion as a hosting requirement, but the summary,
    which readers and agents see first, still states the hosting inside Switzerland flatly.
  ground_truth: 'Laux Lawyers: ''Vorgesehen sind insbesondere ein eigenständiger Cloud-Dienst sowie eine unabhängige Austauschplattform, um Daten von Unternehmen, Verwaltung und kritischen
    Infrastrukturen möglichst in der Schweiz zu hosten.'''
  ground_truth_url: https://www.lauxlawyers.ch/it-recht-in-der-herbstsession-2026/
  fix: Write '... to host administration, industry and critical-infrastructure data in Switzerland where possible' in the summary.
- code: F3
  category: claim-not-supported
  entry: entries/2026-10-11/needymantis-modular-post-compromise-framework-storm-3069.md
  where: 'body paragraph 1 and summary: ''it has seen further NeedyMantis activity beyond Storm-3069 and assesses the activity originates from China without attributing it to a Chinese
    nation-state actor''; summary: ''Storm-3069 ... is one operator; Microsoft assesses the activity originates from China without attributing it to a nation-state actor.'''
  summary: (low confidence) Microsoft's non-attribution statement is about Storm-3069 only ('it has not attributed Storm-3069 to a Chinese nation-state actor'). For the additional NeedyMantis
    activity Microsoft says only that it 'has thus far aligned with activity Microsoft associates with threat actors operating from China'. The entry's sentence puts the China-origin
    assessment and the no-nation-state statement on 'the activity' as a whole, so the scope of both is wider than the source.
  ground_truth: 'Microsoft blog: ''While Microsoft assesses the activity originates from China, it has not attributed Storm-3069 to a Chinese nation-state actor.'' / ''Observed activity
    involving NeedyMantis has thus far aligned with activity Microsoft associates with threat actors operating from China ... Microsoft has not determined whether all observed activity
    is attributable to the same threat actor''.'
  ground_truth_url: https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/
  fix: 'Say: Microsoft assesses Storm-3069''s activity originates from China without attributing it to a nation-state actor, and the further NeedyMantis activity it has seen aligns with
    activity it associates with China-based actors; it has not determined whether one operator is behind all of it.'
- code: F3
  category: claim-not-supported
  entry: entries/2026-05-09/daemon-tools-lite-supply-chain-quic-rat-deployed-via-signed.md
  where: 'frontmatter summary, last sentence: ''Version 12.6.0.2445 is clean.'''
  summary: (low confidence) Kaspersky says the vendor 'published a new software version intended to address it' and that release 12.6.0.2445 'no longer includes the malicious behavior
    described in this article'. 'Is clean' is a stronger, unqualified statement than the source makes; the body correctly says the version 'no longer contains the malicious behaviour'.
  ground_truth: 'Securelist update 5/6/26: ''Following a disclosure, the vendor acknowledged the issue and published a new software version intended to address it. The updated release
    12.6.0.2445 no longer includes the malicious behavior described in this article.'''
  ground_truth_url: https://securelist.com/tr/daemon-tools-backdoor/119654/
  fix: Write 'Version 12.6.0.2445 no longer contains the malicious behaviour Kaspersky describes.'
- code: F11
  category: editorial-advisory
  entry: entries/2026-06-02/sekoia-consolidates-gamaredon-tooling-under-gammaphish-gamma.md
  where: 'frontmatter summary: ''...introducing unified naming for two capability clusters: GammaPhish (the funnel from …'''
  summary: '(advisory, low confidence) The summary field is cut off mid-sentence with an ellipsis (''introducing unified naming for two capability clusters: GammaPhish (the funnel from
    …''), so the card text shown to readers and agents is a truncated fragment. Legacy text that this fire left in place while it edited the same entry''s references and actions.'
  ground_truth: 'Entry frontmatter summary: ''...two capability clusters: GammaPhish (the funnel from …'''
  ground_truth_url: null
  fix: Rewrite the summary as a complete two-sentence statement from the Sekoia report (GammaPhish and GammaWorm naming, CVE-2025-8088 delivery into the Startup folder) via a changelog
    record.
- code: F11
  category: editorial-advisory
  entry: entries/2026-09-17/mandiant-ai-risk-resilience-report-2026.md
  where: 'em dashes in reader-facing text this fire rewrote or re-wrapped: Mandiant AI entry body (about 10 lines, e.g. ''its most operationally useful content for defenders — each pairs
    an attack pattern ...'', ''Case study 1 — ...'' bold leads, ''(T1027.010) — never writing ...''); also ShieldBreak body (7 re-wrapped lines and title/headline), WinRAR first paragraph
    (''CVE-2025-8088 — a path traversal ... — nearly a year''), ShinyHunters 06-16 section (''Council of Europe — the 46-member ...''), RoguePlanet first paragraph (''closes it — last
    vulnerable ...''), Oracle EBS second paragraph (two), Cisco ISE Triage line (''signal — and because ...'')'
  summary: '(advisory) Definition check 12: no em dash in reader-facing entry text (only the ''## <Type> — <at>'' heading is exempt). The listed text sits in paragraphs this fire edited,
    so it was open to a clean-up in the same pass. Advisory only; the main agent may leave it.'
  ground_truth: 'git diff HEAD ''+'' lines containing U+2014 outside ''## '' headings: Mandiant AI 10, ShieldBreak 7, ShinyHunters 1, WinRAR 1, RoguePlanet 1, Oracle EBS 1, Cisco ISE
    1.'
  ground_truth_url: null
  fix: Replace the dashes with commas, colons or full stops in the paragraphs this fire already touched.
- code: F11
  category: editorial-advisory
  entry: entries/2026-06-30/cve-2026-48558-simplehelp-rmm-oidc-sso-authentication-bypass.md
  where: 'body paragraph 2: ''an obfuscated `jquery.js` fetched from a temporary Cloudflare domain delivered the TaskWeaver loader'''
  summary: (advisory, low confidence) The loader's masquerade file name is a file-name indicator of the kind the style rule bars ('no hashes, IPs, attacker domains, mutex or file-name
    indicators'); the entry elsewhere describes behaviour in prose. Sits in this fire's rewrite. Same class as the ShieldBreak phoneinfo.dll decision (declined there on an append-only-record
    argument that does not apply here).
  ground_truth: 'Blackpoint: ''jquery.js, retrieved from a temporary Cloudflare hosted URL and executed through node.exe''; BC: ''an obfuscated JavaScript file named jquery.js''.'
  ground_truth_url: https://blackpointcyber.com/blog/a-djinn-in-the-machine-taskweavers-node-js-intrusion-chain/
  fix: Say 'an obfuscated JavaScript loader named to resemble a jQuery library, fetched from a temporary Cloudflare domain and run through Node.js'.
- code: F18
  category: action-item-discipline
  entry: entries/2026-09-17/cve-2026-76460-cisco-ise-auth-bypass-root-rce.md
  where: 'actions[1]: ''Review access.log on every ISE node (or pull a support bundle with debug logs for apigateway/access.log.*.gz) for suspicious usernames on the API endpoint, and
    cross-check firewall and network logs outside the ISE appliance ... Re-image any node where malicious activity is suspected'''
  summary: '(low confidence) check 10b(b): the action restates the body''s Defender takeaway paragraph and the immediate_action text almost word for word (access.log review, off-box
    log cross-check, re-image), so the aggregated Action Items list carries the same task three times (immediate_action, actions[0] ACL/patch, actions[1] log review). Keep actions[0];
    the log-review task is already the immediate_action''s second half.'
  ground_truth: 'Body Defender takeaway: ''review each node''s access.log (or a decrypted debug-log bundle at ./ise/logs/apigateway/access.log.*.gz) for suspicious usernames ... If malicious
    activity is suspected, Cisco strongly recommends re-imaging''; immediate_action carries the same two steps.'
  ground_truth_url: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
  fix: Drop actions[1], or reduce the list to one action and let immediate_action carry the log-review and re-image steps.
```
