**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-09-30T07:36:44Z · ended_at=2026-09-30T08:09:37Z · duration_seconds=1973

## Verification report — 2026-09-30T0639Z-audit (iteration 1, slice s4 of 4)

Scope: 16 existing entries (scope.iter1.s4.txt), all 227 ledger claims of claims.iter1.s4.yaml (176 ok, 30 F4, 8 F3, 5 F5, 5 F13, 1 F14, 2 unreadable), the run record and the audit report. First pass, so every claim was walked (no sampling). Unreadable this pass: the phpBB.com announcement (Cloudflare-style 403 anti-bot page, jina pool exhausted) and the BSI WID portal page (JS shell). Also unreadable and not relied on: advisories.ncsc.nl ?id= URLs (JS shell; the /2026/ncsc-2026-NNNN.html twin was read instead), the CISA alert pages (403), SecurityWeek Gitea article (403), Progress community bulletin (JS shell), Ivanti hub advisory (JS shell). Findings numbered in the order of the machine-readable file (#1 to #50).

### Broken / unreachable URLs

**#1 (F1)** `2026-05-08/cve-2026-5787-cve-2026-6973-ivanti-epmm-pre-auth-certificate`, sources[] BSI advisory
- Claim / URL: https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-211476-1032.html
- Gap: 404 (curl and fetch_source direct HTTP 404, also with ?nn=). The BSI warning for this disclosure is https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-255045-1032.html (fetched this pass, 200, 'Version 1.0: Ivanti EPMM: Systeme über neue Schwachstelle angegriffen', 07.05.2026). The rewrite kept the dead URL and the sourcing_note still says 'CERT-FR, BSI and NCSC-CH relay the same disclosure'. Replace the URL.

### Citation does not support the claim

**#2 (F3)** `2026-05-08/cve-2026-5787-cve-2026-6973-ivanti-epmm-pre-auth-certificate`, Update 2026-05-09 section (rewritten this run)
- Claim / URL: "CERT-FR (CERTFR-2026-AVI-0552), Germany's BSI and NCSC-CH published advisories on the May 2026 EPMM update" ([CERT-FR, 2026-05-07])
- Gap: The only citation is the CERT-FR page, which says nothing about BSI or NCSC-CH (checked this pass: CERT-FR AVI-0552 carries only its own advisory text). BSI (2026-255045-1032) and NCSC-CH post 12548 do exist and would carry the clause; cite them or drop the two names. (low severity)

**#3 (F3)** `2026-05-08/eurail-breach-308-777-travellers-notified-three-months-after`, body, Commission sentence (claim 31ddbb6713)
- Claim / URL: "the European Commission warned DiscoverEU participants that passport or ID copies, IBANs and health data may be involved and said the attackers had published a sample and were trying to sell the data" ([BleepingComputer]; [European Commission, 2026-01-13])
- Gap: The subject of 'said' is the Commission, but BleepingComputer attributes the sample and sale claim to Eurail: "Eurail also warned at the time that the threat actors had published a sample of the stolen data on Telegram and were attempting to sell it on the dark web." The Commission page (updated 2026-01-13) says the opposite: "there is currently no evidence that the data has been misused or publicly disclosed." Attribute the claim to Eurail, and surface the disagreement with the Commission notice (see F9 note in this finding) rather than pinning it on the Commission.

**#4 (F3)** `2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv`, body sentence 1 (claim 127cd589f9)
- Claim / URL: "unsealing a U.S. District Court (SDNY) civil action and seizing the service's web domain" ([The Record, 2026-05-19])
- Gap: The Record says only 'unsealed a legal case in U.S. District Court' and 'seized Fox Tempest's website'. 'SDNY' appears on Microsoft's On the Issues post (blogs.microsoft.com/on-the-issues/2026/05/19/...), which is in sources[] but not cited for this clause; 'civil' is on neither page ('legal case', 'lawsuit'). Cite the On the Issues post. (low)

**#5 (F3)** `2026-05-29/cve-2026-9170-ibm-http-server-websphere-application-server-p`, body, mitigation sentence (claim 3d81c3b677)
- Claim / URL: "IBM recommends applying interim fix APAR PH71265 or the corresponding fix pack and disabling unused optional modules (`mod_ibm_upload`, `mod_mem_cache`)."
- Gap: Attributed to IBM and uncited. IBM's bulletin (fetched: ibm.com security-bulletin-ibm-http-server-affected-multiple-vulnerabilities-1) says 'Workarounds and Mitigations: None'. The module advice is NCSC-CH post 12601: "Temporary: For certain DoS vectors, disable unnecessary optional modules such as mod_ibm_upload or mod_mem_cache to reduce attack surface", i.e. for DoS vectors, not for CVE-2026-9170. Re-attribute to NCSC-CH and scope it to the DoS flaws.

**#6 (F3)** `2026-05-29/cve-2026-9170-ibm-http-server-websphere-application-server-p`, body, Affected sentence (claim 7da249fbbe)
- Claim / URL: "Affected: IBM HTTP Server 9.0 and 8.5 branches; WebSphere Application Server Traditional 9.0 and 8.5 before the listed fix packs."
- Gap: IBM lists the IBM HTTP Server component (8.5, 9.0) 'in all editions of IBM WebSphere Application Server and bundling products', not WAS Traditional only, and lists no fix pack to be 'listed': fix packs 9.0.5.29 / 8.5.5.30 are 'targeted availability 3Q2026'. The entry never states the affected ranges (9.0.0.0-9.0.5.28, 8.5.0.0-8.5.5.29) or the interim-fix-only state. (low)

**#7 (F3)** `2026-06-12/cve-2026-25089-fortinet-fortisandbox-unauthenticated-os-comm`, body, verdict-dependency sentence (claim a97c365514)
- Claim / URL: "FortiSandbox returns the verdicts that FortiGate, FortiMail, FortiProxy and FortiClient use for blocking, so a compromised sandbox can pass malicious files as clean across the dependent stack" ([Help Net Security, 2026-06-16])
- Gap: The Help Net Security page says only that FortiSandbox is 'a platform that other Fortinet security products depend on for threat verdicts to enforce blocking decisions and trigger automated responses'. It names none of FortiGate, FortiMail, FortiProxy, FortiClient and says nothing about a compromised sandbox passing files as clean. (low)

**#8 (F3)** `2026-06-16/cve-2026-48611-cve-2026-48612-phpbb-unauthenticated-authenti`, body lede (claim 41db8fc8bb)
- Claim / URL: "the open-source forum software common across European universities, municipalities and community portals" ([Pentest-Tools.com, 2026-06-08])
- Gap: The Pentest-Tools page (fetched in full) does not mention universities, municipalities, community portals or Europe. This clause is the entry's home-region relevance argument; Aikido's disclosure names Joomla and Debian forums and '6 million' showcase members instead. Source it or drop it.

**#9 (F3)** `2026-06-16/cve-2026-48611-cve-2026-48612-phpbb-unauthenticated-authenti`, leftover CVE table, LiteSpeed row (claim 2753dd30a4)
- Claim / URL: "| CVE-2026-54420 | LiteSpeed cPanel/WHM plugin | 8.5 | n/a | Yes | Yes (ITW, May 2026) | WHM PlugIn version 5.3.2.1 / plugin 2.4.8 |" ([LiteSpeed])
- Gap: The LiteSpeed blog (fetched) gives no CVSS score; fixed builds and 'actively exploited' are on the page and KEV lists it (2026-06-15). The whole table is unrelated to phpBB (see F11); delete it. (low)

**#10 (F3)** `2026-09-18/cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev`, body first sentence (claim c5978b6473)
- Claim / URL: "incorrect default file permissions (CWE-276) in the Acronis Backup plugin ... ([Help Net Security, 2026-09-16])"
- Gap: Help Net Security says 'insecure file permissions' and gives no CWE. CWE-276 appears only in the CISA KEV record (kev.json cwes: CWE-276), which is a different source. Cite the KEV feed for the CWE. (low)

**#11 (F3)** `2026-09-04/cve-2026-85046-chrome-v8-type-confusion-exploited`, body first sentence (no ledger row)
- Claim / URL: "a type-confusion flaw in the V8 JavaScript engine (CWE-843) that a remote attacker triggers via a crafted HTML page, reaching arbitrary code execution inside the Chrome renderer sandbox" ([Google Chrome Releases, 2026-09-03])
- Gap: The Chrome release note says only 'High CVE-2026-85046: Type confusion in V8'. 'crafted HTML page' and 'arbitrary code inside the sandbox' were the MITRE description (source removed this run); CWE-843 and the same wording are in the CISA KEV record (shortDescription: 'execute arbitrary code inside the sandbox via a crafted HTML page'; cwes CWE-843), which is a different source. Re-point the citation to the KEV feed.

### Unsupported / hallucinated facts

**#12 (F4)** `2026-05-08/eurail-breach-308-777-travellers-notified-three-months-after`, body takeaway (claim 73922b3764) and techniques[]
- Claim / URL: "should expect targeted phishing that uses their real passport and booking details"; techniques: [T1530]
- Gap: Neither BleepingComputer nor the Commission lists booking details among the exposed data (name, passport number/ID, date of birth, contact details, IBAN, health data). T1530 is 'Data from Cloud Storage'; no source mentions cloud storage (sources say 'transferred files from our network').

**#13 (F4)** `2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv`, body sentence 2 and paragraph 2 (claims b769ef6bea, 8118a6c3ed)
- Claim / URL: "code-signing certificates tied to stolen US and Canadian identities"; "short-lived signing certificates sold to ransomware affiliates per signing run"
- Gap: Microsoft: 'which suggests the threat actor very likely used stolen identities based in the United States and Canada' (an assessment, hedge dropped). Pricing is plans of $5000 / $7500 / $9000 with queue priority; no 'per signing run' pricing is stated.

**#14 (F4)** `2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv`, 'Why it matters to us' paragraph (claims e599a89267, 574853989e)
- Claim / URL: "European public-sector and healthcare organisations are explicit downstream victims of the affiliates Fox Tempest serviced (Rhysida, Qilin, Akira have all hit EU targets)"; "Where Teams.exe / AnyDesk.exe / PuTTY / Webex installers spawn `cmd.exe` / `powershell.exe` / `rundll32` / `regsvr32` ... treat as Oyster/Broomstick suspect"
- Gap: Microsoft names sectors (healthcare, education, government, financial services) and countries (US, France, India, China) globally; nothing calls European public-sector or healthcare bodies 'explicit downstream victims', and the EU-targets claim for the three ransomware families is uncited. No cited source describes installers spawning cmd/powershell/rundll32/regsvr32; Microsoft describes only a trojanized MSTeamsSetup.exe deploying the Oyster backdoor.

**#15 (F4)** `2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv`, 'Why it matters to us' paragraph (claim df4a0be9c1)
- Claim / URL: "alert in Defender for Cloud Apps on rapid certificate creation from newly enrolled tenants (`Add-AzKeyVaultCertificate`)"
- Gap: Add-AzKeyVaultCertificate is a Key Vault certificate cmdlet; the sources say Fox Tempest abused Artifact Signing in tenants it controlled ('established hundreds of Azure tenants and subscriptions'), which a customer tenant cannot see. No source recommends this control; the sentence is invented detection guidance in a 'Why it matters to us' paragraph.

**#16 (F4)** `2026-05-29/cve-2026-9170-ibm-http-server-websphere-application-server-p`, body (claim 5ae73b7c1c)
- Claim / URL: "No public exploitation observed."
- Gap: Uncited. NCSC-CH post 12601 (the entry's own corroborating source): '**Current exploitation status**: UNKNOWN'. CVE-2026-9170 is not in kev.json. 'Unknown' and 'none observed' are different claims; state 'no exploitation reported' with a source or say status unknown.

**#17 (F4)** `2026-05-29/cve-2026-9170-ibm-http-server-websphere-application-server-p`, frontmatter summary and evidence[1]
- Claim / URL: summary: "Prevalent in Swiss banking, insurance and federal middleware estates; APAR PH71265 / Fix Pack updates are out."; evidence[1]: "IBM HTTP Server and WebSphere Application Server are vulnerable to remote code execution due to improper input validation" (publisher: IBM Security Bulletin)
- Gap: (a) No fetched source says anything about Swiss banking, insurance or federal middleware; this unsupported claim is the entry's relevance basis and its 'high' priority. (b) IBM: fix packs 9.0.5.29 and 8.5.5.30 are 'targeted availability 3Q2026'; only the interim fix for APAR PH71265 exists (heise 2026-05-28: 'Sicherheitsupdates sind für das dritte Quartal angekündigt'), so 'Fix Pack updates are out' is false. (c) evidence[1] is not on the IBM bulletin (0 matches for 'are vulnerable to remote code execution'); IBM's text is 'IBM HTTP Server is vulnerable to denial of service and a potential remote code execution due to improper input validation'. The title still says 'pre-auth RCE' while the correction says 'potential remote code execution'.

**#18 (F4)** `2026-06-16/cve-2026-48611-cve-2026-48612-phpbb-unauthenticated-authenti`, cves[CVE-2026-48612] and body (claims 2b450ecb7d, 9ca9d606ad, 0d1f046ad3)
- Claim / URL: cvss "8.0", vector: zero-click; "CVE-2026-48612 (CVSS 8.0) chains improper OAuth state verification with CSRF to hijack a logged-in session"
- Gap: The discoverer's report (which the correction says the entry now follows) scores CVE-2026-48612 'CVSS v3.1: 8.3 High AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:L'. UI:R means the victim must open a link, so vector 'zero-click' (no victim interaction) contradicts it. The attack binds the attacker's OAuth identity to the victim account for permanent login; it is not a session hijack. heise/NVD give 8.0, so the entry mixes authorities: 9.4 from Pentest-Tools for one CVE, 8.0 for the other.

**#19 (F4)** `2026-06-16/cve-2026-48611-cve-2026-48612-phpbb-unauthenticated-authenti`, stale 9.8 and correction record (claims 6a6827436c, 7123cf7055, fe6c41050a)
- Claim / URL: table row "| CVE-2026-48611 | phpBB 3.1.0–3.3.16, 4.0.0-alpha | 9.8 |"; summary: "CVE-2026-48611 (NVD CVSS 9.8) is an improper-authentication flaw in the OAuth implementation that allows …"; Correction: "The main text above scored CVE-2026-48611 at 9.8 via NVD."
- Gap: The correction record says the text and score 'now follow the discoverer's write-up', but the body's CVE table still says 9.8, and the frontmatter summary (not in the record's fields) still says 'NVD CVSS 9.8 ... OAuth implementation' and is truncated mid-sentence ('allows …'). The discoverer describes an auth_provider=apache path in ucp_login_link, not OAuth. The record and section also say 'The discoverer, Pentest-Tools.com': heise (2026-06-15) reports 'independently discovered and reported by the two discoverers' (Aikido reported on 2026-06-02; aikido.dev/blog/phpbb-authentication-bypass-rce).

**#20 (F4)** `2026-06-16/cve-2026-48611-cve-2026-48612-phpbb-unauthenticated-authenti`, body (claims caebc6c094, 03bf2bbdef)
- Claim / URL: "The disclosing source does not publish exploit code, and no in-the-wild exploitation is reported yet."; actions[0]: "if upgrade is delayed, disable the OAuth integration even when unused"
- Gap: The Pentest-Tools page carries full PoC requests, a curl one-liner and a JS payload and states 'July 4, 2026: Proof of concept details disclosed'; cves[] lacks poc-public. The same page says 'There is no configuration workaround that fully closes this attack path on versions prior to 3.3.17' and the CVE-2026-48611 path is auth_provider=apache, not OAuth, so the stop-gap advice (in body and actions[0]) is unsupported. 'No in-the-wild exploitation' has no source. Also cves[].affected/fixed are null though the page gives '<= 3.3.16 and 4.0.0-a2' / '3.3.17'.

**#21 (F4)** `2026-06-23/cve-2026-20896-gitea-docker-trust-all-reverse-proxy-default`, headline, summary, body (claims 26754bf205, 1d8d2047c2, f98ac62bc3)
- Claim / URL: "letting anyone on the port sign in as admin"; "anyone who can reach the container's HTTP port can forge an X-WEBAUTH-USER header and authenticate as any account, admin included, with no credentials"
- Gap: The exploit requires the opt-in setting ENABLE_REVERSE_PROXY_AUTHENTICATION = true. GHSA-f75j: 'When an admin enables ENABLE_REVERSE_PROXY_AUTHENTICATION = true ... The Docker image instead trusts X-WEBAUTH-USER from any source IP'; NCSC-CH: 'Prerequisites: ... reverse-proxy authentication enabled (ENABLE_REVERSE_PROXY_AUTHENTICATION = true)'; THN: 'With reverse-proxy login enabled ...'. The entry states the compromise unconditionally, tags it default-config, and never names the precondition an Exposure line needs. Rewrite headline/summary/body with the precondition and a known or guessable username.

**#22 (F4)** `2026-06-23/cve-2026-20896-gitea-docker-trust-all-reverse-proxy-default`, body (claims bd1eb990d9, 9320efce90, 204fbd948b) and actions[1] (claim df6107fe86)
- Claim / URL: "fix a cluster of four flaws"; "CVE-2026-27775 (protected-branch enforcement race in single-push batch operations)"; "Hunt for admin logins sourced from the reverse-proxy IP with no corresponding password-auth audit entry"
- Gap: The Gitea release post lists 8 CVE-numbered fixes plus at least 5 unnumbered ones in 1.26.3 and a further security fix in 1.26.4. For CVE-2026-27775 it says 'the pre-receive hook cached the first ref's result, letting a per-branch maintainer-edit grant escalate to full repository write' (no protected-branch race); the CVSS 7.1 for CVE-2026-20779 is on no fetched page. The body hunt idea ('sourced from the reverse-proxy IP') is the inverse of actions[1] ('source IP is not the configured trusted proxy'); no source says Gitea records the source IP of header-auth sessions.

**#23 (F4)** `2026-07-29/cve-2026-0769-langflow-preauth-eval-rce-exploited-not-in-kev`, body and cves[] (claims f55476b86d, b69a9567f6, 35d26aeeea)
- Claim / URL: "The current catalog carries five Langflow entries"; "one KEV-listed with a patch path and one neither listed nor patched"; fixed: "a direct OSV lookup for the same advisory identifier returns not-found"
- Gap: kev.json (catalogVersion 2026.09.29, cached this run) lists SIX Langflow entries: CVE-2026-9198 (dateAdded 2026-08-04), CVE-2026-0770, CVE-2026-55255, CVE-2025-34291, CVE-2026-33017, CVE-2025-3248; the sourcing_note lists five. The store's own CVE-2026-0770 entry records 'fixed: no version patch, mitigated by disabling AUTO_LOGIN / rotating default credentials', contradicting 'with a patch path'. https://api.osv.dev/v1/vulns/CVE-2026-0769 returns a record (published 2026-01-23, last_affected 1.3.2), and no GitHub/OSV source is cited for the not-found claim.

**#24 (F4)** `2026-08-08/cve-2026-65400-macos-screen-sharing-auth-state-bypass`, body first analysis paragraphs (claims defff90040, 350577326d, 23dea4f3f2)
- Claim / URL: "Taken alone this is a straightforward patch item on a client operating system."; "There is no known persistent artifact specific to CVE-2026-65400 ... a successful attack looks like a legitimate Screen Sharing session"; "discoverable over mDNS"
- Gap: The newest sections disprove the main analysis and the correction did not touch it: Calif ('the first public macOS remote root exploit in a long time'), NCSC-NL (root obtained, Monero miner planted on multiple systems) and Huntress (sessions via this bug report authentication_type 'SRP' vs 'RSA-SRP', session_username root or null) give an artifact and a discriminator. No fetched source mentions mDNS/Bonjour. The headline still leads with the fG! interval story, not exploitation.

**#25 (F4)** `2026-09-04/cve-2026-85046-chrome-v8-type-confusion-exploited`, body vs correction record (claim 92d8fcc247)
- Claim / URL: body: "CISA's ADP Vulnrichment program scores it CVSS 3.1 8.8 (AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H) ... neither Google nor MITRE ... publishes its own numeric score"; record: "The score is removed"
- Gap: cves[].cvss is now null and the two MITRE/NVD API sources were removed, but the body paragraph keeps the 8.8 score with no remaining source, contradicting the record ('The score is removed') and the sourcing_note ('publishes no numeric CVSS score, so none is recorded'). The record is internal, so no section explains it to the reader. Remove the sentence (fields: body).

**#26 (F4)** `2026-09-04/cve-2026-85046-chrome-v8-type-confusion-exploited`, body sentence 'sandbox-escape primitive'; cves[CVE-2026-85043]
- Claim / URL: "The type confusion is a sandbox-escape primitive, not a full chain by itself: code that runs from it stays confined to the renderer sandbox"; CVE-2026-85043 type: info-disclosure
- Gap: Self-contradictory: code confined to the renderer sandbox is not a sandbox escape (the sentence needs 'not'). Google lists CVE-2026-85043 as 'Incomplete cleanup in Network'; typing it info-disclosure is unsupported. Also the later BlueMoon entry (2026-09-10) documents this CVE chained into a click-to-SYSTEM chain, contradicting 'no source describes such chaining' (see F9). (low)

**#27 (F4)** `2026-09-17/cve-2026-76460-cisco-ise-auth-bypass-root-rce`, cves[CVE-2026-20192] and Update 2026-09-18 (no ledger row)
- Claim / URL: "no other CVE in the release is named exploited by any source"; cves[CVE-2026-20192] status: [patch-available]
- Gap: Cisco's hardening advisory (cisco-sa-hardening-ise-XU5EwX5T) lists CVE-2026-20192 (CWE-284 Improper access control, CVSS 10.0) with footnote 1: 'One vulnerability that belongs to this vulnerability class is known to be actively exploited. For more information, see [Cisco Identity Services Engine Authentication Bypass Vulnerability]' (the ISE-ABP advisory of CVE-2026-76460). So a Cisco source does tie exploitation to the CVE-2026-20192 class; the structured status and the sentence should say so.

**#28 (F4)** `2026-09-28/storm-3168-jadepuffer-azure-destructive-service-principal`, record (claim 8105c6e635), frontmatter summary, body takeaway
- Claim / URL: record: "The ATT&CK mapping carried Exploit Public-Facing Application although the sources ... The unsupported technique is removed."; summary: "likely initial access traces to a service-principal secret an employee posted"; takeaway: "Azure resource locks and storage-account deletion protection, were the only thing that stopped part of this campaign's deletions"
- Gap: Microsoft's own 'MITRE ATT&CK Techniques observed' list includes 'T1190 Exploit Public-Facing Application | Storm-3168 linked infrastructure repeatedly probed sensitive application paths on applications hosted in Azure App Service for potential exploitation', and the body describes that probing, so the technique is source-supported and its removal leaves described behavior unmapped. Microsoft labels the secret exposure 'Possible initial access' and says 'it is unclear how the service principal was initially compromised'; 'likely' upgrades that. SQL deletions failed because 'it used an unsupported API version', not because of locks, so 'the only thing that stopped part' is wrong.

**#29 (F4)** `docs/audits/2026-09-30-quality-audit.md`, 'Findings: systemic' item 1 and verdict paragraph
- Claim / URL: "478 entries carry `migrated_from: briefs/...`, and only 17 had ever received an audit record."; "cut from 22 open rows to 11"
- Gap: Not reproducible on disk. At HEAD 478 entries carry migrated_from (correct) but only 3 of them carry any updates[] record whose run_id contains 'audit' (2 from 2026-08-30T1312Z, 1 each from 2026-09-06T1308Z and 2026-09-13T1307Z); a search of all prior audit run records' updated_entry_ids and of prior audit reports also gives 3, not 17. The same '17' is repeated in tools/legacy_review.py and prompts/CHANGELOG.md 4.18. state/coverage_backlog.md has 26 table rows under ## Open at HEAD and 15 now (22 to 11 only if the 4 rows added by the 0404Z fire are excluded); say which. (low confidence on the backlog part)

### Claims missing inline citation

**#30 (F5)** `2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv`, body paragraph 2 (claims f498b31636, a5860ca7b3, cd5f7cd7c9)
- Claim / URL: "Confirmed downstream customers: **Vanilla Tempest** ... Microsoft revoked 1,000+ fraudulent code-signing certificates, disabled hundreds of Cloudzy-hosted VMs ... Microsoft's blog notes confirmed affected sectors include healthcare, education, government, and financial services across the US, **France**, India, and China."
- Gap: A full paragraph of attributed facts with no inline link (the paragraph names 'Microsoft's blog' but does not link it). Each fact is on Microsoft's two posts (verified this pass), except that INC, Qilin and Akira are 'clear links' from cryptocurrency analysis to affiliates, not 'confirmed downstream customers'. Add citations.

**#31 (F5)** `2026-06-30/cve-2026-8037-progress-kemp-loadmaster-pre-auth-rce-via-unin`, body (claims 7d2044ba87, b8ddfed4cb)
- Claim / URL: "A second bulletin CVE, CVE-2026-33691, bypasses file-upload extension checks via OWASP CRS whitespace padding."; "Progress reported no known active exploitation at disclosure."
- Gap: Neither sentence has a citation; none of the fetched pages (watchTowr, ZDI, eSentire, THN) describes CVE-2026-33691 or a Progress no-exploitation statement. The Progress bulletin (community.progress.com) is a JS shell and could not be read, so (low confidence) it may carry both; cite it or drop them.

### Drop (low relevance / off-audience / duplicate)

**#32 (F7)** `2026-05-08/eurail-breach-308-777-travellers-notified-three-months-after`, whole entry length (low confidence)
- Claim / URL: routine incident: 4 sentences in two paragraphs plus a Correction section
- Gap: The actionability rule says an incident with no access vector, no actor and no behavior beyond its impact is routine and 'two sentences at most, or dropped'. The entry says itself 'No source names the access vector or the actor'. It also lacks the labelled '**Defender takeaway:**' line (the last paragraph is one, unlabelled). Trim to two sentences and label the takeaway, or drop.

### Needs more research

**#33 (F8)** `2026-05-29/cve-2026-9170-ibm-http-server-websphere-application-server-p`, missing decision-relevant fields
- Claim / URL: cves[CVE-2026-9170] has no affected/fixed; no Exposure / Detection / Defender takeaway lines
- Gap: IBM's bulletin gives affected ranges (IHS 9.0.0.0-9.0.5.28, 8.5.0.0-8.5.5.29), the interim fix (APAR PH71265) and that fix packs 9.0.5.29 / 8.5.5.30 are targeted for 3Q2026. That interim-fix-only state is the decision-relevant fact and it is absent (the summary claims the opposite). A 'high' vulnerability entry ships without the labelled lines.

**#34 (F8)** `2026-05-08/cve-2026-5787-cve-2026-6973-ivanti-epmm-pre-auth-certificate`, Exposure omits a source-stated precondition; Detection/Response
- Claim / URL: Exposure: "on-premises EPMM below 12.6.1.1, 12.7.0.1 or 12.8.0.1"
- Gap: BleepingComputer: CVE-2026-7821 'affects only users who use and have configured Apple Device Enrollment' and Ivanti/BC advise reviewing admin accounts; neither is in the Exposure line. (low)

**#35 (F8)** `2026-09-17/cve-2026-76460-cisco-ise-auth-bypass-root-rce`, Defender takeaway / actions[] omit Cisco's compromise-response instruction
- Claim / URL: actions[1] ends at cross-checking network logs
- Gap: Cisco's advisory: 'If malicious activity is suspected, it is strongly recommended to re-image the affected nodes and restore from configuration backup if needed.' The entry tells readers to distrust on-box logs but never says what to do on a hit. (low)

**#36 (F8)** `2026-07-29/cve-2026-0769-langflow-preauth-eval-rce-exploited-not-in-kev`, labelled lines
- Claim / URL: body uses plain 'Detection:' and 'Hardening:' with no '**Exposure:**' or '**Defender takeaway:**'
- Gap: The actionability contract requires the labelled Defender takeaway on every entry; the two actions[] carry the decision but the body does not label it. (low)

**#37 (F8)** `2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv`, labelled lines
- Claim / URL: 'Why it matters to us' paragraph in place of Exposure / Detection / Defender takeaway
- Gap: The contract labels are missing and the paragraph that replaces them carries the unsupported claims listed under F4. (low)

### Surface contradiction

**#38 (F9)** `2026-06-12/cve-2026-25089-fortinet-fortisandbox-unauthenticated-os-comm`, cves[CVE-2026-25089].status includes poc-public; tags poc-public
- Claim / URL: CCB Belgium: "The publicly availability of a proof-of-concept (PoC) exploit increases the likelihood that this vulnerability could be exploited"
- Gap: Security Affairs (cited on the entry, 2026-06-16): "A working exploit for the vulnerability has not been publicly disclosed." The entry adopts CCB's PoC claim (tag, status, body) and never mentions the disagreement; add a 'Contradiction:' line. Similar: Eurail (Commission 'no evidence ... publicly disclosed' vs Eurail's sample-on-Telegram warning, see F3) and Chrome (see F4: BlueMoon entry documents the chain the body says no source describes).

### Missed angles

**#39 (F10)** `2026-05-08/cve-2026-5787-cve-2026-6973-ivanti-epmm-pre-auth-certificate`, later Ivanti EPMM advisory not in the store
- Claim / URL: https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Endpoint-Manager-Mobile-EPMM-CVE-2026-6973-CVE-2026-10727 (CCCS AV26-567, 2026-06-09)
- Gap: Search: 'Ivanti EPMM CVE-2026-10727 12.9.0.1 12.8.0.3 12.7.0.2'. CCCS AV26-567 lists EPMM 12.9.0, 12.8.0.2, 12.7.0.1 'and prior' as affected by a June 9 advisory (authenticated OS command injection as root, CVE-2026-10727, per search results); the store has the Sentry pair CVE-2026-10520/10523 but not CVE-2026-10727 (not in entries or state/cves_seen.json). The Ivanti entry's 'fixed' builds (12.7.0.1, 12.8.0.1) are therefore no longer the end of the patch path. Below the critical/high bar; a changelog line on the Ivanti entry would do. (low confidence; the Ivanti advisory itself is a JS shell)

### Editorial / less-is-more flags (advisory)

**#40 (F11)** `2026-05-08/cve-2026-5787-cve-2026-6973-ivanti-epmm-pre-auth-certificate`, title (run-written)
- Claim / URL: "CVE-2026-6973 — Ivanti EPMM: admin-authenticated RCE exploited in limited attacks, ..."
- Gap: Em dash in text this run wrote (the title was rewritten). The IBM main-text rewrite also keeps '`CVE-2026-9170` — CWE-94'. Also legacy updates[] summaries at 2026-05-09 and 2026-05-10 still carry 'KEV deadline tomorrow' and the four named victim organisations; they are append-only, so the Correction record is the only fix.

**#41 (F11)** `all non-internal records this run wrote`, record summaries (rendered on /changes/ and entry pages)
- Claim / URL: "The entry also gains the source rating and ATT&CK mapping every entry of its kind now carries." (IBM, phpBB); "The entry also gains its source rating." (Gitea, FortiSandbox); "An evidence item that quoted an earlier summary rather than a source is removed" (Kemp); "The sourcing note is rewritten as plain provenance without pipeline narration." (macOS); "The three duplicate entries ... are folded into it." (Ivanti); "CVE Services API" (Langflow)
- Gap: build.py renders updates[].summary to readers (entry-update__summary, /changes/, feeds). These sentences narrate field names and pipeline mechanics (source rating, ATT&CK mapping, evidence item, sourcing note, folded). Also the Correction sections for Eurail and Gitea end with record-keeping narration ('The text now says so.', 'Both passages now say so.').

**#42 (F11)** `2026-06-30/cve-2026-8037-progress-kemp-loadmaster-pre-auth-rce-via-unin`, Update 2026-08-08 section (legacy text)
- Claim / URL: "This pipeline's 2026-07-02 entry recorded exploitation *attempts* ..."
- Gap: Workflow-internal reference in reader text. Same class: Langflow sourcing_note ('verified directly against the current catalog', 'not carried in the CVE metadata here', and after this run's edit a broken sentence 'no independent corroboration;  The KEV absence was verified'); Fox Tempest 'Why it matters to us'.

**#43 (F11)** `2026-06-12/cve-2026-25089-fortinet-fortisandbox-unauthenticated-os-comm`, frontmatter hygiene
- Claim / URL: entities: []; sources[0] role primary = NCSC-NL (advisories.ncsc.nl, JS shell, unreadable); Security Affairs marked role: primary
- Gap: The registry gained product:fortinet-fortisandbox, -cloud and -paas (first_seen 2026-06-12) but the entry links none; the vendor PSIRT is the fifth source while a national-CERT page and a news outlet are marked primary. Reorder roles.

**#44 (F11)** `runs/2026-09-30/2026-09-30T0639Z-audit.md`, run record telemetry (exempt from vocabulary, not from truth)
- Claim / URL: gap_hours: 65; fetch_failures: []; sub_agents: R1 only
- Gap: gap_hours 65 is measured from the 2026-09-27T1308Z audit start; the 2026-09-29T2134Z audit completed 2026-09-30T05:11Z (about 1.5 h before this start). fetch_failures is empty while bridge_uses says die-linke.de returned 403 and a Wayback snapshot failed. The audit report (Method) and prompts/CHANGELOG.md credit a site sub-agent with the 4.17 site work, but the record lists only R1. The '43 s build' figure in the report was not re-run.

### Analytical-link-as-fact

**#45 (F13)** `2026-05-08/pro-russian-hacktivists-modify-ot-pump-settings-at-five-poli`, title, headline, takeaway, Update 2026-05-09, Correction, record (claims decdc49f68, 8d8da318ca, eef997455f, 68619ac9e2)
- Claim / URL: title: "hacktivists altered industrial-control parameters at five municipal water treatment plants through weak passwords and internet-exposed management panels"; headline: "Weak passwords on internet-facing management panels let attackers change equipment settings at five Polish water plants"; Update: "It attributes the water-plant intrusions to hacktivist activity"
- Gap: The ABW report (fetched, English PDF pp. 36-37) makes two separate statements: hacktivist groups 'exploited glaring vulnerabilities in the form of poor password policies and unsecured device management panels' against municipal infrastructure generally (p.36), and 'In 2025, security breaches were reported at water treatment plants in the following towns: ... the attackers were able to alter the technical parameters of the equipment' (p.37, in the APT-groups spread, with no actor and no access vector). No sentence ties the five plant breaches to hacktivists or to weak passwords. The body sentences quote ABW faithfully; the title, headline, defender-takeaway ('the whole access path ABW describes'), Update section, Correction section and record summary assert the link. State the two ABW statements separately, as the summary does.

**#46 (F13)** `2026-09-18/cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev`, headline, summary, takeaway (claim 913c8c67c0)
- Claim / URL: headline: "CISA lists it as exploited on a single customer's report"; takeaway: "CISA's KEV listing reflects its own independent judgment that active exploitation occurred"
- Gap: No cited source states the basis of CISA's listing (kev.json notes cite only Acronis advisory SEC-10986). The headline/summary say the listing rests on Acronis's single-customer report; the takeaway says the opposite (CISA's own independent judgment). Both are unsourced and contradict each other; remove the causal claim from both.

**#47 (F13)** `2026-09-28/storm-3168-jadepuffer-azure-destructive-service-principal`, title
- Claim / URL: "a sub-eight-minute, automated Azure resource-destruction campaign via a service-principal secret that stayed valid in a GitHub issue's edit history after the visible text was redacted"
- Gap: Microsoft: 'We could not confirm whether this secret was used for the activity described here' and 'it is unclear how the service principal was initially compromised'; it says the secret 'remained accessible', not 'stayed valid'. The title presents the exposed secret as the campaign's route.

### Quantifier without source

**#48 (F14)** `2026-06-23/cve-2026-20896-gitea-docker-trust-all-reverse-proxy-default`, body (claim 0354dc6c4b)
- Claim / URL: "Gitea is the dominant self-hosted GitHub alternative across DACH/EU public-sector DevOps and sovereign-cloud environments"
- Gap: No cited source states Gitea's market share or public-sector prevalence; the superlative is the entry's home-region relevance claim (the same wording sat in the pre-run summary). Remove or source.

### Org-triage line missing / inconsistent

**#49 (F16)** `2026-05-29/cve-2026-9170-ibm-http-server-websphere-application-server-p`, priority: high (low confidence)
- Claim / URL: priority: high; no exploitation, no PoC, 'potential' RCE, interim fix only
- Gap: Under the 4.17 high bar the reason to act rests on the unsupported 'Prevalent in Swiss banking, insurance and federal middleware estates' claim; nothing else in the entry (no exploitation, no public PoC, fix packs unreleased) is a decision within 7 days beyond the regular cycle. Consider notable. Same doubt, lower confidence: Fox Tempest (a service takedown with no time-critical defender decision, no actions) and Storm-3168 (unnamed victim, no constituency nexus stated, transferable-TTP ground not declared) are both still high.

### Action-item discipline

**#50 (F18)** `2026-06-23/cve-2026-20896-gitea-docker-trust-all-reverse-proxy-default`, actions[1]
- Claim / URL: "Hunt Gitea sign-in/audit logs for X-WEBAUTH-USER-authenticated admin sessions whose source IP is not the configured trusted proxy. By construction any such hit is a spoofed header, and it separates exploitation from legitimate proxy auth."
- Gap: Restates the body's hunting idea (with inverted logic, see F4) instead of naming a task, and rests on a log field no source says exists. Drop it or make it a concrete task from a cited artifact. Kemp: actions[0] 'Patch Kemp LoadMaster or disable its API' and actions[1] 'Re-verify every Kemp LoadMaster is on GA 7.2.63.2 ...' both start with the same patch/verify step; merge the version check into one action and keep the compromise assessment as the second.

### Checked statements: run record (runs/2026-09-30/2026-09-30T0639Z-audit.md)

- HOLDS: entries_updated 75 = len(updated_entry_ids) 75; every listed entry exists, is modified in the working tree and carries exactly one updates[] record with this run_id (56 correction, 18 improvement, 1 update; 38 internal); no modified entry is unlisted.
- HOLDS: entries_published 0; three Ivanti duplicate files deleted; survivor record lists them in merged_from; site/_site has redirect stubs for the three ids; no other entry or registry record still points at them.
- HOLDS: duration_seconds 3308 = completed 07:34:51 minus started 06:39:43. R1 started/ended files (06:41:19Z / 07:07:50Z) give 1591 s; findings.R1.yaml has 36 items (15 new + 11 existing replacement citations = sources_used 26, 10 none).
- HOLDS: "24 banned citations repaired": of the 36 in banned-citations.json, 24 are gone from their entries, 4 belong to the three deleted Ivanti files, 8 remain on 7 twin-group entries (PAN-OS 0300, Copy Fail, Exchange 42897, two FortiClient EMS 35616, two Cisco SD-WAN 20262).
- HOLDS: "30 priorities recalibrated": git diff vs HEAD gives 16 high to notable, 11 notable to routine, 3 high to routine (30).
- HOLDS: seven legacy entries re-verified (state/legacy_review.json: exactly the seven named, status reviewed, run id of this fire); 468 pending (legacy_review.py --stats: pending 468, reviewed 7).
- HOLDS: Apple CVE-2026-86950 is in kev.json (dateAdded 2026-09-29) and entries/2026-09-30/cve-2026-86950-apple-coregraphics-zero-day-kev.md exists; kev_window_diff over the cached KEV file reports 0 uncovered additions since 2026-09-16.
- HOLDS: "24 unfolded legacy UPDATE entries remain": 24 migrated entries whose title or opening carries "UPDATE (originally covered". NOT REPRODUCED: "about 19 same-finding twin groups" (a crude CVE-overlap count gives 51 pairs, 43 without a references[] link; approximation, not flagged).
- HOLDS: sources_changed (cisa-kev, anssi-fr, helpnetsecurity, fortinet-psirt last_successful_fetch 2026-09-30 in sources/sources.json); ATT&CK pin v19.2 unchanged (attack_version 19.2, file not in the diff); jina pool exhausted (every key HTTP 402 observed again in this pass); check_run.py: 1 fail (verification block empty, expected) and 1 warn (aggregator-only, Die Linke), as stated.
- QUESTIONABLE (F11 advisory): gap_hours 65 (measured from the 2026-09-27T1308Z audit start; the 2026-09-29T2134Z audit completed 05:11Z the same morning); fetch_failures [] while bridge_uses reports die-linke.de 403 and a failed Wayback snapshot; sub_agents lists only R1 while the report and CHANGELOG credit a site sub-agent.

### Checked statements: audit report (docs/audits/2026-09-30-quality-audit.md)

- HOLDS: verdict counts 75 records / 7 legacy / 3 folded; priority move counts 16 + 3 + 11 = 30; 36 banned citations in 30 entries, 24 fixed / 4 removed with the folded duplicates / 8 on seven twin entries; seven entries with attacker domains or mutex values removed (node-ipc, GTIG UNC6671, Fox Tempest, actions-cool, Sophos Beagle, TraderTraitor hostname, Chosen Brick mutexes), all records internal.
- HOLDS: table rows for ABW (defect text matches HEAD; ground truth partly, see #30), Ivanti EPMM (HEAD framing and victims verified; Ivanti/CERT-FR/KEV ground truth verified), Eurail (letters 2026-03-27, Commission says only EDPS notified), CVE-2026-50751 twin (kev.json lists 50751, not 50752), FortiSandbox (KEV 2026-07-16 for 25089 and 39808), the five exploitation-denied corrections (Gitea, TeamCity, ServiceNow, Kemp, macOS Screen Sharing all carry a correction or update record), TeamCity ransomware flag (kev.json Known; update record exists). Die Linke, CVE-2026-32202 and Dragos rows belong to other slices and were not re-derived.
- HOLDS: KEV RANSOMWARE rows: after the run kev_window_diff reports one row, CVE-2026-0257 (two PAN-OS twins); TeamCity, Cisco Secure FMC and Nx/TanStack each carry a record from this run adding the ransomware flag.
- HOLDS: tools/fold_entries.py (256 lines: mechanical fold, adds merged_from list, re-points references and registry relations, deletes duplicates, refuses without a record, redirect stubs in build), tools/legacy_review.py (init / next / done / stats, statuses pending|reviewed|folded), state/legacy_review.json (475 entries), quality-audit Phase 0 step 6b and Phase 3 item 13, v4.18 banner in both prompts and a 4.18 CHANGELOG entry, list-valued merged_from in content_model.py and build.py, ALERTS_WINDOW_DAYS = 7 with the landing alarm following the reading window, memory notes legacy-corpus.md (new) and site-landing-live-brief.md, eight Cisco ISE CVEs (20247, 20282, 20300, 76424 to 76428) added to state/cves_seen.json.
- DOES NOT HOLD as written (see #29): "only 17 had ever received an audit record" (3 reproducible; the number is also in tools/legacy_review.py and CHANGELOG 4.18); "cut from 22 open rows to 11" (26 to 15 in the file; 22 to 11 only if the four rows added by the 0404Z fire are excluded). "478 of 962 entries": 478 migrated entries and 966 entries at HEAD (962 before the 0404Z merge, 963 after the folds), acceptable as a start-of-run figure.
- NOT VERIFIED: "43 s build" and the check_run refinements (folded-deletion exception, internal-record allowance); check_run.py itself passes 53 checks. "35 CVE-sharing entry pairs carried no link" not reproduced (pre-fold store not available).
- Style: no US federal deadline used as a reason to act in any slice-s4 entry text after this run (one legacy sentence in Kemp says the due date "carries no weight here"); no IOC found; the em dash in the Ivanti title and record-summary vocabulary are in the F11 finding.

### Verdict

NEEDS_FIXES (truth: 33, editorial: 12, advisory: 5)

Coverage looks complete for this correction run (no uncovered KEV addition; the one missed angle is a low-severity June Ivanti EPMM advisory, #43). Highest-consequence items: ABW title/headline link (#30), Gitea precondition omitted (headline, summary, body), IBM summary and evidence (#5,6,16,17), phpBB scores/PoC/OAuth advice and stale 9.8, Chrome body still carrying the removed 8.8, Storm-3168 technique removal contradicted by Microsoft, Langflow KEV count and macOS stale analysis.

### Findings summary (machine-readable)

See work/2026-09-30T0639Z-audit/verification.iter1.s4.findings.yaml (50 records).
