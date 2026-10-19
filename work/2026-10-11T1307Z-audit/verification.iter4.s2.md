**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-19T16:27:21Z - ended_at=2026-10-19T16:50:19Z
## Verification report - 2026-10-11T1307Z-audit (iteration 4, slice s2)

Scope: 27 entries (verify-scope.iter4.s2.txt), 286 ledger claims. Every claim has a verdict row in verification.iter4.s2.claims.yaml (279 ok, 6 F3, 1 F4; 286 answered, 0 unreadable). Every page cited by a ledger claim was fetched this iteration (extract, raw url, WebFetch for the three cisa.gov pages, cisa-kev bridge, ncsc-csh post, pdf for the IC3 advisory); no claim rests on memory. Sources cited only in text outside the ledger (Hunt.io, Tenable and Unit 42 in the Gambit entry; NCSC-CH and BSI in the Kiteworks 2026-09-29 update) were not re-fetched. Coverage: all claims of the entries (this slice is the full ledger, including the 33 claims changed since iteration 3).

### Prior-iteration deltas (all 22 re-checked against the fetched sources)

- TeamCity F5 (generalisation): fixed. The sentence now reads "in analyst judgement, tends to close quickly".
- TeamCity F4 (sourcing_note withholding): fixed. sourcing_note says JetBrains "publishes no technical detail beyond the agent polling protocol"; the JetBrains advisory has no further detail.
- TeamCity F11 (record-keeping narration): fixed. The 2026-10-11 Correction no longer says "The main analysis now closes with...".
- The Gentlemen F4 (AdaptixC2): fixed. Body now carries Talos's hedge ("may be using it in real-world attacks"); Talos page confirms.
- Microsoft May F3 (2026-06-01 date): fixed. Body says BleepingComputer added Microsoft's statement on 2026-06-02 (page: "Update June 02, 08:51 EDT: Added Microsoft and CCB statements") and cites MSRC for the advisory clause (MSRC: Exploited No, revision 1.0 only).
- Microsoft May F3 (Server 2012): fixed. CERT-EU co-cited (lists Windows Server 2012 / 2012 R2).
- Microsoft May F4 (MDASH/dnsapi.dll): fixed. Correction cites the Microsoft Security Blog (16 CVEs found with MDASH; dnsapi.dll row for CVE-2026-41096) and keeps only NetworkService as unsupported.
- Inditex F3 (EU-only): fixed. Clause now cites BleepingComputer ("customers in different markets") and HIBP.
- Oracle EBS F3 (CSPU): fixed. Oracle's CSPU page lists CVE-2026-46817 (Oracle Payments, File Transmission, 9.8, 12.2.3-12.2.15).
- Microsoft May F11 (frontmatter exploited vs Microsoft denial): decline rationale holds. CCB (national CERT) states exploitation, CERT-EU relays it, and the body carries a Contradiction line with Microsoft's denial.
- Oracle EBS F11 (sourcing_note): fixed. Two sentences of provenance; nested parentheses gone.
- SAP August (five items): the unauthenticated-reach attribution to SAP, the analyst-judgement marking of the internal-versus-internet weighting, the NCSC-NL-relays-Defused body wording, and the import/ETL removal from the 2026-08-16 detection paragraph all landed. Two residuals remain and are new findings below (a second "working exploit" sentence; the Correction restating what NCSC-NL relays).
- WaterPlum F3 (family-level collection list): fixed. The Triage line now says the advisory lists what the actors' infostealers target (page: "Other sensitive data targeted for exfiltration includes ..."). A different adjacency in the same line is a new low-confidence finding.
- LiteLLM F5 ("widely deployed"): fixed. LiteLLM F11 (sourcing_note): fixed; the Check Point row stays by design (the KEV and Check Point blog support it); em dashes remain (advisory).
- Spring Cloud Config F4 (record summary vs empty actions): fixed. F5 (deployment premise): fixed, now "in analyst judgement".
- Plugin4Shell F11 (sectors): fixed. sectors is [].

### Citation does not support the claim

1. `F3` 2026-07-16/cve-2026-46817-oracle-ebs-payments-preauth-rce-kev-listed
   - Where: body paragraph 1: 'The bug sits in the File Transmission component of Oracle Payments — the payment-processing engine built into Oracle E-Business Suite — and an unauthenticated attacker with HTTP network access can use it to compromise and take over Oracle Payments (CVSS 9.8) ([Oracle CSPU, 2026-05-21](https://www.oracle.com/security-alerts/cspumay2026.html))' (claim efbd576749)
   - Finding: (low confidence) The cited risk-matrix page carries the component, HTTP protocol, 'Remote Exploit without Auth: Yes' and 9.8, but not the words 'take over' (they are in Oracle's English-text version, cspumay2026verbose.html, and in the KEV description) and not 'the payment-processing engine built into Oracle E-Business Suite' (that is Help Net Security's description).
   - Evidence: cspumay2026.html row: 'CVE-2026-46817 | Oracle Payments | File Transmission | HTTP | Yes | 9.8 | Network | Low | None | None | Un- changed | High | High | High | 12.2.3-12.2.15'; verbose page: 'Easily exploitable vulnerability allows unauthenticated attacker with network access via HTTP to compromise Oracle Payments. Successful attacks of this vulnerability can result in takeover of Oracle Payments.'; HNS: 'Oracle Payments is the payment-processing engine built into Oracle's E-Business Suite' (https://www.oracle.com/security-alerts/cspumay2026verbose.html)
   - Fix: Cite the verbose text page for the takeover wording and move the payment-engine description to the Help Net Security citation.

2. `F3` 2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce
   - Where: body: 'SAP Security Note 3773203 is SAP's fix for CVE-2026-42945 (CVSS 8.1), the upstream NGINX buffer overflow, in Commerce Cloud public-cloud deployments fronted by NGINX ([SAP SE, 2026-08-11])' and Correction 2026-10-11: 'SAP Security Note 3773203 is SAP's downstream fix for the NGINX flaw CVE-2026-42945 ... ([SAP SE])' (claims b03a8c8bcc, 5e94359c31)
   - Finding: (low confidence) The cited SAP page row carries the note number, CVE id, CVSS 8.1 and the title 'Potential buffer overflow vulnerability affects SAP Commerce Cloud in public-cloud deployments with NGINX'; it does not call the CVE the upstream or an NGINX flaw or the note a downstream fix. That identification rests on the entry's own references[] link to the NGINX entry, not on the cited page.
   - Evidence: SAP page: '[CVE-2026-42945] Potential buffer overflow vulnerability affects SAP Commerce Cloud in public-cloud deployments with NGINX ... High | 8.1' (https://support.sap.com/en/my-support/knowledge-base/security-notes-news/august-2026.html)
   - Fix: Cite the NGINX/F5 advisory (or drop 'upstream'/'downstream' framing) for the identification as the NGINX flaw.

3. `F3` 2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce
   - Where: Correction 2026-10-11: 'what is reported is exploitation attempts against Defused's honeypots, which NCSC-NL relays, and no party reports a compromised production instance ([BleepingComputer, 2026-08-14])' (claim 9b0102bc47)
   - Finding: (low confidence) NCSC-NL relays Defused's report that attackers are actively scanning and seeking vulnerable Data Hub Adapter systems; it does not mention honeypots or exploitation attempts, and the clause cites BleepingComputer only. The body paragraph (1bb9d263c7) words it correctly ('actively scanning for vulnerable systems'); the correction restates it as the honeypot attempts.
   - Evidence: NCSC-NL: 'Beveiligingsbedrijf Defused meldt dat kwaadwillenden actief scannen en op zoek zijn naar kwetsbare Data Hub Adapter-systemen.' (https://advisories.ncsc.nl/2026/ncsc-2026-0302.html)
   - Fix: Say 'Defused's honeypot attempts (BleepingComputer) and its report of active scanning, which NCSC-NL relays (NCSC-NL)'.

4. `F3` 2026-09-19/waterplum-contagious-interview-joint-advisory-scale
   - Where: Triage: 'the StoatWaffle delivery through a `.vscode/tasks.json` entry that runs when a cloned repository's folder is trusted ([FBI/IC3, 2026-09-18])' (claim 21163ff5d4)
   - Finding: (low confidence) The advisory says StoatWaffle uses 'a malicious VS Code configuration file that triggers auto-run code execution when the folder is opened and trusted'. It names '.vscode/tasks.json' only in a separate mitigation bullet ('Restricted Mode, which prevents execution of .vscode/tasks.json on launch') and never says the repository is 'cloned'. Tying StoatWaffle to a tasks.json entry in a cloned repository is the entry's inference, cited as the advisory's statement.
   - Evidence: Advisory fn. 6: 'embedding a malicious VS Code configuration file that triggers auto-run code execution when the folder is opened and trusted by the victim'; mitigation: 'only open in Restricted Mode, which prevents execution of .vscode/tasks.json on launch'. (https://www.ic3.gov/CSA/2026/260918.pdf)
   - Fix: Say 'a malicious VS Code configuration file that runs when the folder is trusted' (the advisory's words), and keep tasks.json to the Restricted Mode mitigation sentence.

5. `F3` 2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft
   - Where: body paragraph 1: 'the actor tried to exploit CVE-2025-24799 with a PoC and sqlmap to pull user information from the database, an unauthenticated SQL injection in GLPI's inventory endpoint fixed in GLPI 10.0.18 ([GLPI, 2025-03-18](https://github.com/glpi-project/glpi/security/advisories/GHSA-jv89-g7f7-jwfg))' (claim de137e3120)
   - Finding: (low confidence) The sentence chains a Talos-only fact (the actor's PoC and sqlmap attempt to retrieve user information) with GLPI-advisory facts (unauthenticated SQLi in the inventory endpoint, fixed in 10.0.18) and ends on the GLPI citation alone. The GLPI advisory says nothing about the actor, a PoC or sqlmap.
   - Evidence: GLPI advisory: 'An unauthenticated user can perfom a SQL injection through the inventory endpoint. ... Upgrade to 10.0.18.' Talos: 'the actor attempted to exploit CVE-2025-24799, an unauthenticated SQL injection vulnerability in GLPI, using both a PoC and sqlmap to retrieve user information from the database.' (https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/)
   - Fix: Add the Talos citation after the attempt clause (or split the sentence).

### Unsupported / hallucinated facts

1. `F4` 2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce
   - Where: Update 2026-08-16, 'Calibrate the status honestly' paragraph: 'the interval between a public fix and a working exploit has collapsed to days on this component'
   - Finding: (low confidence) No cited source says a working exploit exists: BleepingComputer reports Defused's first exploitation attempts at honeypots, 'no public PoC' and 'no party reports a compromised production instance' (the same paragraph says so), and NCSC-NL reports scanning. 'Working exploit' stated as fact is unsupported and sits in tension with the paragraph's own calibration; the iteration-3 remediation changed the other 'working exploit' sentence but left this one. Not marked as analyst judgement.
   - Evidence: BC: 'First exploitation attempts against CVE-2026-58231 ... is now hitting our honeypots - 3 days after patch day ... This vulnerability has no public PoC and is not known to be exploited.' (https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)
   - Fix: Reword to 'exploitation attempts appeared within days' or mark 'working exploit' as analyst judgement.

2. `F4` 2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft
   - Where: body: 'The VHDX backup files themselves ... were compressed with `zstd`, split into 256MiB chunks and uploaded concurrently (up to 16 files at a time) to Wasabi cloud storage via `rclone`'; summary: 'exfiltrates the VHDX backup images themselves in 256MiB chunks to Wasabi cloud storage' (claim 0c4a192607)
   - Finding: (low confidence) Talos hedges this phase: 'We also identified traces indicating that the VHDX files were compressed with zstd and transferred to cloud storage services such as Wasabi using rclone ... This suggests that the attackers were deliberately focused on exfiltrating large volumes of data and intended to maintain and monitor the transfer process.' The entry states the upload as completed fact with no hedge, the same hedge-dropping pattern iteration 3 fixed for AdaptixC2 in this entry.
   - Evidence: Talos: 'traces indicating that the VHDX files were compressed with zstd and transferred to cloud storage services such as Wasabi using rclone.' (https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/)
   - Fix: Say 'traces indicate' / 'Talos found command-history traces of' for the chunked rclone upload, in the summary and the body.

3. `F4` 2026-09-22/plugin4shell-ai-coding-agent-sha-pinning-bypass
   - Where: body paragraph 1: 'Gemini CLI has a distinct but equally exploitable variant ... ([AIR Security, 2026-09-17])' (claim cba5c9a957)
   - Finding: (low confidence) 'Equally exploitable' is the entry's comparison, not AIR's. AIR says only that 'git gives an attacker two ways to exploit it' and calls the result zero-click across all four. The Hacker News, which this fire's correction relies on to drop 'identically' from the title, says GitHub's rule 'does not clearly block' the Gemini name, i.e. the two variants' reach is not established as equal. The body sentence still carries the comparative the title correction removed.
   - Evidence: AIR: 'git gives an attacker two ways to exploit it.' THN: 'GitHub's rule against hash-shaped names does not clearly block that name. So it is not established that installing a Gemini CLI plugin from GitHub avoids the flaw.' (https://www.air.security/blog-posts/plugin4shell)
   - Fix: Say 'a distinct variant' and drop 'equally exploitable'.

### Claims missing inline citation

1. `F5` 2026-09-29/microsoft-storm-2570-cross-raas-toolkit
   - Where: body paragraph 1, sentences after the first citation ('Post-compromise, the affiliate routinely conducts internal network discovery ... Regardless of the final ransomware brand, Microsoft describes a recurring commodity toolchain ...') and paragraph 2 ('Microsoft's own post closes with a Defender XDR detection and mitigation mapping') (claims 469a0bbdd9, 2108167784)
   - Finding: (low confidence) About twenty named tools and behaviours (NetScan/SoftPerfect/Nmap, MeshAgent renaming, Atera/Splashtop/ScreenConnect/NinjaRMM, Cloudflared service, ngrok, ntdsutil IFM, Mimikatz/LaZagne/pypykatz, PerfLogs exclusions, PsExec @ip.txt, rdp.bat, Impacket/NetExec, s5cmd/Rclone) sit in two uncited sentences, attributed in prose to Microsoft but with no inline link; the same applies to the Defender XDR sentence. All are on the Microsoft post (verified), so this is a missing-link defect, not a truth defect. One gloss is not Microsoft's: 'ngrok exposing RDP for redundant remote access' (Microsoft: ngrok exposes TCP 3389 and Cloudflared creates 'resilient outbound access paths').
   - Evidence: Microsoft: 'the threat actor uses ngrok to expose TCP 3389 (default port for RDP), after which PsExec-related activity and security tampering appears.' (https://www.microsoft.com/en-us/security/blog/2026/09/24/beyond-ransomware-tracking-storm-2570-consistent-tradecraft-across-deployments/)
   - Fix: Append the Microsoft citation to the discovery and toolchain sentences and the Defender XDR sentence; drop 'redundant'.

### Needs more research

1. `F8` 2026-05-13/cve-2026-41089-cve-2026-41096-cve-2026-41103-cve-2026-42898
   - Where: body: no **Defender takeaway:** line (Exposure, Detection, Contradiction only)
   - Finding: (low confidence) The actionability contract requires a Defender takeaway on every entry; this high-priority exploited-CVE entry has Exposure, Detection and Contradiction lines but no takeaway (the decision: patch DCs first, treat disputed exploitation as a reason to prioritise, check for compromise because patching does not evict). The decision lives only in actions[0].
   - Evidence: CCB: while patching ... may provide safety from future exploitation, it does not remediate historic compromise; MSRC/CERT-EU: patch DCs (https://ccb.belgium.be/advisories/warning-microsoft-patch-tuesday-may-2026-patches-118-vulnerabilities-16-critical-102)
   - Fix: Add one **Defender takeaway:** line, cited.

2. `F8` 2026-06-09/cve-2026-42271-berriai-litellm-low-privilege-command-injecti
   - Where: body (no **Exposure:**, **Detection:**, **Defender takeaway:** lines); actions[0] trimmed to the upgrade task this fire
   - Finding: A KEV-listed, priority-high LiteLLM RCE entry carries none of the labelled lines and no interim mitigation. Both cited sources clearly support them and the trimmed action no longer carries them: GHSA states a workaround ('block POST /mcp-rest/test/connection and POST /mcp-rest/test/tools/list at their reverse proxy or API gateway'), and Horizon3 lists the Starlette 1.0.1 upgrade, rotating credentials the proxy stores, and the behaviours to hunt (unexpected subprocess execution spawned through the MCP test endpoints, requests to /mcp-rest/test/*, unusual Host header values). Iteration 3 asked to drop the interim clause from the action on the premise that the body carries it; the body does not.
   - Evidence: GHSA 'Workarounds: If upgrading is not immediately possible, developers should block POST /mcp-rest/test/connection and POST /mcp-rest/test/tools/list at their reverse proxy or API gateway.'; Horizon3 'If immediate patching is not possible: Block access to the affected MCP test endpoints; Rotate credentials stored by the proxy; Review logs for unusual Host header activity and subprocess execution events' (https://horizon3.ai/attack-research/vulnerabilities/cve-2026-42271-chained-with-cve-2026-48710/)
   - Fix: Add cited Exposure (versions 1.74.2 to 1.83.6, Starlette <= 1.0.0 for the unauthenticated chain), Detection (telemetry class: subprocess spawn from the proxy, requests to the two endpoints, anomalous Host headers) and Defender takeaway (upgrade plus Starlette 1.0.1, block the two endpoints meanwhile, rotate stored provider keys).

3. `F8` 2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce
   - Where: cves[CVE-2026-58231 / 44772 / 44758 / 58243].affected: 'see SAP Security Note ... for the release levels'; body has no **Exposure:**, **Detection:** or **Defender takeaway:** label
   - Finding: (low confidence) The cited SAP patch-day page states the affected release identifiers (CVE-2026-58231: COM_CLOUD 2211, 2211-JDK21; CVE-2026-44772: XMII 15.4, 15.5, MII_ADMIN 15.4, 15.5; CVE-2026-44758: XMII 15.4, 15.5; CVE-2026-58243: SAP_BASIS 750 to 758, 816, 918, 920), yet four of the six cves[] records point to the note instead, while CVE-2026-34265 carries its kernel list. A responder cannot match the version without opening the note. The body also carries none of the three labelled lines (the detection concepts and the rebuild-and-redeploy decision sit in prose and in actions[]), on a priority-high CVSS 10.0 entry.
   - Evidence: SAP page row: 'SAP Commerce Cloud (Data Hub Adapter) Version(s) - COM_CLOUD 2211, 2211-JDK21' (https://support.sap.com/en/my-support/knowledge-base/security-notes-news/august-2026.html)
   - Fix: Copy the version identifiers into affected; lift the exposure, detection and takeaway sentences into labelled lines.

### Editorial / less-is-more flags (advisory)

1. `F11` 2026-06-09/cve-2026-42271-berriai-litellm-low-privilege-command-injecti
   - Where: title, headline, summary and body paragraph 1 contain em dashes ('CVE-2026-42271 — BerriAI LiteLLM', 'Two preview endpoints — `POST ...`')
   - Finding: (low confidence) Style rule: no em dash in reader-facing entry text. Declined in earlier iterations as stripped at render; body was rewritten this fire so the text is in scope. Advisory only.
   - Fix: Optional: replace with colons/commas.

2. `F11` 2026-06-30/cve-2026-8037-progress-kemp-loadmaster-pre-auth-rce-via-unin
   - Where: frontmatter sectors: [technology, telco, public-sector]
   - Finding: (low confidence) No cited page (watchTowr, ZDI, eSentire, The Hacker News, CISA alert, KEV record) names the telco or public sector or any sector; the tag is unsourced, the same class as the plugin4shell sectors finding of iteration 3 that was fixed by emptying the field. THN says only 'used by enterprises'.
   - Evidence: THN: 'LoadMaster is an application delivery controller and load balancer used by enterprises to manage traffic across servers.' (https://thehackernews.com/2026/06/progress-kemp-loadmaster-flaw-could-let.html)
   - Fix: Empty sectors or cite a source that names them.

3. `F11` 2026-07-16/cve-2026-46817-oracle-ebs-payments-preauth-rce-kev-listed
   - Where: headline and body use em dashes ('KEV-listed — patch or pull exposed instances', 'Oracle Payments — the payment-processing engine ... —', '27 June 2026 — roughly six weeks')
   - Finding: (low confidence) Style rule: no em dash in reader-facing entry text; the body was re-written this fire. Advisory only.
   - Fix: Optional: replace with colons or commas.

4. `F11` 2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce
   - Where: frontmatter sectors: [public-sector, finance, telco, technology]
   - Finding: (low confidence) No cited page (JetBrains advisory, follow-up, Cadence post, CISA alert, KEV record) names any sector; the four sector tags are unsourced, the same class as the plugin4shell, n8n and Storm-3168 sector findings of earlier iterations. Advisory only.
   - Evidence: JetBrains advisory names no sector; only 'TeamCity On-Premises ... All versions'. (https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/)
   - Fix: Empty sectors or cite a source that names them.

5. `F11` 2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce
   - Where: Correction 2026-10-11 sentence: 'The main analysis now records that, three days after patch day, Defused saw exploitation attempts against the Data Hub Adapter flaw and NCSC-NL reported active scanning (see the 2026-08-16 update).'
   - Finding: (low confidence) Reader-facing section narrates the edit ('The main analysis now records...') rather than stating a delta; same class as the TeamCity record-keeping sentence of iteration 3, which was removed. Also carries '(see the 2026-08-16 update)'. Advisory.
   - Fix: Drop the sentence; the record summary already carries it.

6. `F11` 2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce
   - Where: frontmatter sectors: [public-sector, finance, manufacturing, retail]
   - Finding: (low confidence) Only retail (BleepingComputer: 'online stores owned by ... large retailers') and arguably manufacturing (MII) have a source; public-sector and finance are named by none of the cited pages. Same class as earlier sector findings. Advisory.
   - Evidence: BC: 'Commerce Cloud ... is a cloud-based e-commerce platform used by online stores owned by high-profile global brands and large retailers.' (https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)
   - Fix: Drop public-sector and finance or cite a source.

7. `F11` 2026-09-10/sap-september-2026-overpass-s4get-preauth-rce
   - Where: frontmatter sectors: [public-sector]; title and body use em dashes
   - Finding: (low confidence) No cited page (Onapsis x3, CERT-EU, BleepingComputer, Senthorus) names the public sector or any sector; the tag is unsourced. Title ('... (CVE-2026-58240, CVSS 9.8) — two unauthenticated ...') and the Defender takeaway still carry em dashes. Advisory.
   - Evidence: Onapsis: 'Exposure is globally distributed, concentrating in the United States, Germany, India and China across both on-premises networks and the managed cloud'; no sector named. (https://onapsis.com/blog/sap-overpass-remediation/)
   - Fix: Empty sectors; optionally replace em dashes.

8. `F11` 2026-09-19/waterplum-contagious-interview-joint-advisory-scale
   - Where: frontmatter sectors: [public-sector, technology, finance]
   - Finding: (low confidence) The advisory names individual IT professionals, web freelancers, crypto/Web3 specialists, a Japanese crypto exchange and 'businesses that outsource or commission work via crowdsourcing'; none names public-sector bodies. The body's cantonal/federal sentence is the entry's own extension. Advisory.
   - Evidence: Advisory: 'WaterPlum is victimizing individual IT professionals in Japan, the United States, Europe, and other countries.' (https://www.ic3.gov/CSA/2026/260918.pdf)
   - Fix: Drop public-sector from sectors or cite a source.

9. `F11` 2026-09-24/solarwinds-observability-cve-2026-28324-28325-unauth-rce
   - Where: frontmatter sectors: [public-sector]
   - Finding: (low confidence) None of the six cited pages (SolarWinds release notes and two trust-center advisories, NCSC-NL, CERT-FR, GBHackers) names the public sector or any sector; the tag is unsourced, the same class as earlier sector findings. Advisory.
   - Evidence: Release notes name no sector; GBHackers: 'If an affected SolarWinds instance is internet-facing or reachable from a compromised internal network segment...' (https://gbhackers.com/solarwinds-observability-flaws/)
   - Fix: Empty sectors or cite a source.

10. `F11` 2026-06-30/cve-2026-8037-progress-kemp-loadmaster-pre-auth-rce-via-unin
   - Where: title ('CVE-2026-8037 — Progress Kemp LoadMaster ...') and a body line in the 2026-07-02 section
   - Finding: (low confidence) Em dash in reader-facing title and body. Advisory only.
   - Fix: Optional.

11. `F11` 2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce
   - Where: cves[].affected, actions[1] and the 2026-08-28 Correction body use em dashes
   - Finding: (low confidence) Em dash in reader-facing text (actions[1]: '... XSL files — the patch alone does not remove the vulnerable servlet'). Advisory only.
   - Fix: Optional.

### Whole-run checks

- Relevance and priority calibration: no entry falls below the gate; priorities (critical Cisco SD-WAN; high for the exploited or pre-auth edge CVEs; notable or routine for the rest) are defensible. Flink's length is a carried-over advisory from an earlier iteration and is not repeated.
- Classification present on all 27 entries with in-vocabulary codes; no org_triage or watchlist use; no IOCs; no workflow-internal vocabulary found in reader-facing fields; actions[] lists are within the do-now bar.
- Citation dates: Onapsis posts show datePublished 2026-09-08 against the cited 2026-09-09 (one-day drift, not flagged); Rapid7's CVE-2026-20182 post carries JSON-LD 2026-05-04 but its visible timeline dates the disclosure 2026-05-14, matching the citation.
- Missed angles: none flagged for this slice.

### Verdict

NEEDS_FIXES (truth: 8, editorial: 4, advisory: 11)

Every truth finding is low-confidence and evidenced; none changes a headline conclusion. The substantive one is the LiteLLM entry, where the GHSA workaround and Horizon3 hunting guidance are now absent from the entry after the action was trimmed on the premise that the body carried them.
