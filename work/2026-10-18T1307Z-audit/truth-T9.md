**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:27:48Z · ended_at=2026-10-18T13:59:42Z · duration_seconds=1914

## Retrospective truth pass, batch T9, run 2026-10-18T1307Z-audit

Entries: 14 checked · clean 3 · imprecision 8 · factual-error 3. Claims: 423 in scope, 423 checked (400 ok, 22 with a finding, 1 unreadable).

### Named leads
- Kiteworks (CVE-2026-54154 clause cites the press release): CONFIRMED, imprecision. The 2026-09-27 press release carries only the Advanced Forms support notice; the CVE id and the 9.4.1 bound are in GHSA-5xhq-9wq3-rvj6. All eight `cves[]` ids, CVSS scores, affected and fixed versions were checked against the GitHub advisory API per advisory and are correct; none is in KEV.
- Bitget (hedged evidence quote not on the page): CONFIRMED. Bitget has revised the page; the quoted wording ("may have exploited ... to potentially obtain") and "to impersonate authorized activity" no longer appear. The 2026-09-29 research capture still carried the hedged wording, so the quote was true when captured and is stale now.

### Prior-audit remediations (2026-09-30T0639Z-audit, iteration 8)
All held when read against the sources: Kaspersky "the desktop and the C: and D: drive roots" matches Securelist; Push Security record is now `improvement`; Kiteworks summary attributes "no CVE was known" to watchTowr and the record-summary closing clause names it; Qbusoft Correction states the withdrawn "never told the national CERT" headline claim with the minister's 2026-09-25 statement; Bitget record summary uses each report's own label.

### Not verifiable
- 2026-09-28/cve-2026-88771: both community.citrix.com pages cited in the 2026-10-04 update return HTTP 403 to extract, url, jina and WebFetch. "Citrix has observed targeted attacks ... Denial of Service" and "please upgrade your deployment again" are confirmed through BleepingComputer's quotation of the Citrix blog (and CTX697174 for the DoS impact); the independence statement and the quote continuation "with the software released as part of the" are unverified.

### 2026-09-25/switzerland-sovereign-digital-infrastructure-motion-24-3209 (imprecision)
1. **imprecision** at summary; body paragraph 1
   - Claim: an independent cloud service and an independent data-exchange platform intended to host administration, industry and critical-infrastructure data inside Switzerland
   - Defect: Drops the motion text's qualifier 'where possible': the cited Laux Lawyers page (and the entry's own evidence[] translation) say the platforms are meant to host the data inside Switzerland where possible, not as an unqualified residency requirement.
   - Ground truth: Laux Lawyers: 'Vorgesehen sind insbesondere ein eigenständiger Cloud-Dienst sowie eine unabhängige Austauschplattform, um Daten von Unternehmen, Verwaltung und kritischen Infrastrukturen möglichst in der Schweiz zu hosten.' (https://www.lauxlawyers.ch/it-recht-in-der-herbstsession-2026/)
   - Fix: Add 'where possible' after 'inside Switzerland' in the summary and the body sentence.

### 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning (imprecision)
1. **imprecision** at body, Defender takeaway
   - Claim: Run 9.5.1 or later on every deployment (Email Protection Gateway at least 9.4.1 for CVE-2026-54154), and put the open question to Kiteworks Support in writing: ... beyond its notice to customers with self-hosted Advanced Forms to contact Customer Support ([Kiteworks, 2026-09-27](https://www.kiteworks.com/company/press-releases/kiteworks-precautionary-shutdown-advisory/))
   - Defect: The sentence's only citation, the 2026-09-27 press release, carries the Advanced Forms support notice but neither CVE-2026-54154 nor the 9.4.1 bound; the CVE and version come from GHSA-5xhq-9wq3-rvj6 (cited only in the 2026-10-02 section). Citation does not vouch for the CVE/9.4.1 clause.
   - Ground truth: Press release: 'Customers with self-hosted Advanced Forms should contact Customer Support for assistance.' (no CVE id, no 9.4.1). GHSA-5xhq-9wq3-rvj6: CVE-2026-54154, 'Upgrade to Kiteworks Email Protection Gateway 9.4.1 or later.' (https://www.kiteworks.com/company/press-releases/kiteworks-precautionary-shutdown-advisory/)
   - Fix: Split the sentence: cite GHSA-5xhq-9wq3-rvj6 after the 9.4.1 / CVE-2026-54154 clause and keep the press-release citation for the Advanced Forms notice.
2. **imprecision** at body paragraph 1
   - Claim: and recommended shutting systems down even where they are not directly internet-facing, since the possible access route is unconfirmed.
   - Defect: Clause follows the Heise citation with no citation of its own and attributes the recommendation and rationale to the CISO email; Heise states it as KiteWorks recommending (and 'It cannot be said with certainty what potential access routes there might be'), BleepingComputer and TechCrunch carry the same point.
   - Ground truth: Heise: 'KiteWorks recommends shutting down the servers even before this time – even if they are not accessible from the internet. It cannot be said with certainty what potential access routes there might be.' (https://www.heise.de/en/news/Imminent-Zero-Day-Attack-KiteWorks-Urges-Customers-to-Shut-Down-Servers-11466375.html)
   - Fix: Add the Heise citation after the clause (or attribute it to Heise's report of the email).
3. **imprecision** at ## Update 2026-10-02T04:58:16Z, second sentence
   - Claim: (low confidence) BleepingComputer, quoting the advisory, describes input-handling flaws in publicly reachable endpoints that potentially allowed unauthenticated code execution and, by chaining local weaknesses, escalation to root
   - Defect: BleepingComputer does attribute the passage to a 'Wednesday advisory' linked to GHSA-5xhq-9wq3-rvj6, but that GHSA (page and GitHub API) carries only 'Multiple issues were addressed with improved input validation.' and no such passage; the chain-to-root description is BleepingComputer's only.
   - Ground truth: GHSA-5xhq-9wq3-rvj6 description: '**Impact:** A remote attacker may be able to execute arbitrary code with root privileges. **Description:** Multiple issues were addressed with improved input validation.' (https://api.github.com/repos/kiteworks/security-advisories/security-advisories/GHSA-5xhq-9wq3-rvj6)
   - Fix: Say 'BleepingComputer, quoting a Kiteworks statement' (or drop 'quoting the advisory') since the linked GHSA does not carry the passage.

### 2026-09-27/flink-lpg-group-crowdfund-extortion-order-hub-breach (imprecision)
1. **imprecision** at body paragraph 2
   - Claim: (low confidence) The extortion actor behind the breach, self-named "LPG Group"
   - Defect: States as fact that LPG Group is behind the breach; the identity rests on the group's own extortion emails, heise says the intruders were 'bisher unbekannte Kriminelle' and that the group 'bekennt sich' to the acts, and Flink has not named an actor.
   - Ground truth: heise: 'In diesen ... bekennt sich eine bisher recht unbekannte Bande namens „LPG Group“ zu den Taten.' (https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)
   - Fix: Say 'The extortion actor claiming the breach, self-named LPG Group'.
2. **imprecision** at body paragraph 3
   - Claim: Abuse reporting to the group's mail provider curtailed the flood of messages
   - Defect: Drops heise's qualifiers: it is Flink's account, the flood was only 'vorerst' (for now) contained, and heise adds the extortionists may seek other routes; sentence also carries no citation of its own.
   - Ground truth: heise: 'Laut Flink wurde über eine Abuse-Mitteilung beim von der Bande genutzten Mailprovider die Flut der Schreiben auch vorerst eingedämmt, nicht auszuschließen sei aber, dass sich die Erpresser andere Wege suchen.' (https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)
   - Fix: Write 'According to Flink, an abuse report to the mail provider curtailed the flood for now' and cite heise.
3. **imprecision** at Defender takeaway
   - Claim: (low confidence) treat any wave of individually-addressed extortion emails referencing a real breach as corroboration of that breach's scope, not as unrelated spam.
   - Defect: No cited source says extortion emails corroborate scope; the entry itself reports that Flink did not confirm the claimed 1 million customers and that heise cannot size the German wave. Emails corroborate at most that an actor holds some data.
   - Ground truth: NL Times: 'The total number of affected customers was not confirmed by Flink'; heise: 'Die Zahl der kontaktierten Kunden in Deutschland lässt sich damit bisher schlecht einschätzen.' (https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data)
   - Fix: Replace 'scope' with 'existence' (corroboration that an actor holds data), or drop the clause.

### 2026-09-27/pentagon-dmdc-military-personnel-data-breach-unencrypted-ssn (imprecision)
1. **imprecision** at headline; body paragraph 1
   - Claim: (low confidence) A vulnerable Pentagon HR file server sat unencrypted and reachable for nine months before anyone noticed
   - Defect: /
   - Ground truth: a government's central personnel-data store kept identity numbers unencrypted and readable for nine months before discovery (The nine months is the window of unauthorized access (Oct 2025 to 16 Jul 2026); no source says how long the data had been unencrypted or that the server was externally 'reachable' (the entry's own sourcing note says reachability is not reported).)
   - Fix: CNN: 'beginning last October, but it wasn't until nine months later, in July, that the Pentagon discovered and remediated the issue' and 'The stolen data wasn't encrypted, according to the letter.'
2. **imprecision** at Defender takeaway
   - Claim: check that central personnel and HR data stores encrypt identifying fields at rest, which CNN notes is standard security practice and which DMDC's server lacked
   - Defect: CNN says only that the stolen data was not encrypted and that encrypting sensitive data is standard practice; 'at rest' and 'identifying fields' are the entry's gloss, and no source says encryption at rest would have stopped access through the file-sharing vulnerability.
   - Ground truth: CNN: 'The stolen data wasn't encrypted, according to the letter. Encrypting sensitive data is a standard security practice.' (https://www.cnn.com/2026/09/25/politics/pentagon-data-personnel-breach)
   - Fix: Mirror CNN: 'encrypt sensitive personnel data, which CNN notes is standard practice and which the stolen data lacked'.

### 2026-09-27/qbusoft-medyc-poland-healthcare-breach-fingerprint-actor (imprecision)
1. **imprecision** at sources[2].date; body paragraph 2 citation label
   - Claim: [TVP World, 2026-09-26](https://tvpworld.com/95581628/poland-hit-by-cyberattack-weeks-after-19-million-medical-records-breach)
   - Defect: The citation date does not equal the source's own publication date: TVP World's JSON-LD datePublished is 2026-09-25T10:35:00+02:00 (the DataBreaches.net repost is 2026-09-26).
   - Ground truth: TVP World JSON-LD: "datePublished": "2026-09-25T10:35:00+02:00" (https://tvpworld.com/95581628/poland-hit-by-cyberattack-weeks-after-19-million-medical-records-breach)
   - Fix: Change the TVP World source date and the body citation label to 2026-09-25.

### 2026-09-28/cve-2019-18935-telerik-godzilla-webshell-virtualpathprovider (imprecision)
1. **imprecision** at summary; cves[0]; body paragraph 1; Defender takeaway
   - Claim: a .NET deserialization flaw in Telerik UI for ASP.NET AJAX's RadAsyncUpload feature, patched since version 2020.1.114 but still reachable on unpatched IIS deployments
   - Defect: /
   - Ground truth: patch to 2020.1.114 or later now (Omits the vendor's stated exploitation prerequisites and fix semantics: Telerik's KB says exploitation needs the attacker to break RadAsyncUpload encryption (or know the custom keys) AND type whitelisting not enabled; 2020.1.114 only enables whitelisting by default, and the vendor still says to apply the recommended security settings on 2020.1.114 and later. The entry presents a plain pre-auth, version-bound flaw and states no exposure discriminator.)
   - Fix: Telerik KB: 'Prerequisites for an Attack: An attacker can break the RadAsyncUpload encryption (or have prior knowledge of your custom encryption keys) and stage a malicious request. The type whitelisting feature of RadAsyncUpload is not enabled'; table: 'R1 2020 (2020.1.114) and later | Not possible through RadAsyncUpload, unless the attacker has access to your encryption keys | The feature is enabled by default | Apply the recommended security settings.'
2. **imprecision** at Defender takeaway
   - Claim: where patching must wait, restrict or disable the RadAsyncUpload handler and monitor for the VirtualPathProvider-registration pattern described above
   - Defect: The interim control 'restrict or disable the RadAsyncUpload handler' appears in no cited source (AhnLab's mitigation list is upgrade to 2020.1.114 or later plus the process and file checks); the vendor's interim control is the recommended security settings (custom encryption keys, type whitelisting).
   - Ground truth: AhnLab mitigation: 'Upgrade Telerik UI for ASP.NET AJAX to a version that includes the Vulnerability Patch ... Telerik UI version: 2020.1.114 Or later'; Telerik KB: 'Apply the recommended security settings.' (https://asec.ahnlab.com/en/95561/)
   - Fix: Replace with the vendor's recommended security settings (cited to Telerik) or drop the unsourced workaround.

### 2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev (imprecision)
1. **imprecision** at headline; tags
   - Claim: (low confidence) Citrix confirms in-the-wild exploitation of two default-configuration NetScaler zero-days and publishes no workaround
   - Defect: Only CVE-2026-88771 applies to every deployment in default configuration; Citrix's precondition for CVE-2026-88772 is 'DTLS configuration enabled' (enabled by default only on VPN vServers; other virtual servers vulnerable only if configured as type DTLS), which the entry's own body states. The headline lumps both as default-configuration.
   - Ground truth: Citrix CTX697096: 'CVE-2026-88772 | Precondition: DTLS configuration enabled on NetScaler ADC or NetScaler Gateway (Note: Enabled by default on VPN vServer)' (https://support.citrix.com/external/article/CTX697096/citrix-netscaler-adc-and-citrix-netscale.html)
   - Fix: Say 'two NetScaler zero-days, one default-configuration and one default on VPN virtual servers'.
2. **imprecision** at ## Update 2026-09-29T04:35:00Z (and record summary), first paragraph
   - Claim: (low confidence) ns_monuploadd_err.pl, a Perl script that periodically scans NetScaler system logs for Pitboss "PPE unexpectedly died" crash messages to recover a core-dump filename
   - Defect: 'periodically' is in neither cited source: watchTowr's article shows the script greps logs for 'missed too many heartbeats' or 'unexpectedly died' and its PoC output says 'triggering force pickup'; Unit 42 says only that the log 'will eventually be processed' by the script.
   - Ground truth: watchTowr Labs: 'grep -E -i "pitboss.*PPE.*missed too many heartbeats|pitboss.*PPE.*unexpectedly died" @WR_FILES | tail -1 | sed ...'; Unit 42: 'Eventually this ns.log file will be processed by the vulnerable Perl script' (https://labs.watchtowr.com/oh-look-the-foot-gun-went-off-again-citrix-netscaler-preauth-command-injection-cve-2026-88771/)
   - Fix: Drop 'periodically' and name both trigger strings.
3. **imprecision** at evidence[] (Citrix community blog quote); ## Update 2026-10-04T04:42:00Z
   - Claim: (low confidence) quote "please upgrade your deployment again with the software released as part of the" and "The flaw is independent of the vulnerabilities disclosed in the earlier bulletin CTX697096" cited to community.citrix.com blogs
   - Defect: Both cited Citrix community pages return HTTP 403 to every transport (extract, url, jina, WebFetch), so the independence statement and the quote continuation could not be checked at the source; BleepingComputer's rendering of the same Citrix sentence ends 'please upgrade your deployment again,' without the continuation the evidence quote carries.
   - Ground truth: BleepingComputer: 'if you have determined that your NetScaler deployment meets the preconditions describe above, please upgrade your deployment again," Citrix warned.' (https://www.bleepingcomputer.com/news/security/citrix-patches-netscaler-saml-zero-day-exploited-in-attacks/)
   - Fix: Verify the quote against the Citrix blog when reachable; otherwise end the quote at 'again'.

### 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan (factual-error)
1. **factual-error** at body paragraph 2, first sentence
   - Claim: The agents' access appears to have been restricted to HTTP GET, while UNCTAD's `Facts` endpoint required POST and returned data only to requests originating from UNCTAD's own site.
   - Defect: Mis-states the CORS point: Howard-Jones says only that UNCTAD's own website is allowed to READ the data from JavaScript (Access-Control-Allow-Origin); the Urlquery-submitted form POST returned 200 with data in the scan screenshots (SiliconANGLE: 'Screenshots in the scan reports show index data coming back'), so the endpoint did not serve data only to UNCTAD-origin requests. The entry's own next sentences rely on the form POST working. Also 'began blocking GET requests' adds a change the source does not state ('the Facts endpoint was blocked to GET requests entirely').
   - Ground truth: swarmcha.se: 'UNCTAD only allows its own website to read its data, not httpbin, because of the Access-Control-Allow-Origin header.'; 'The urlquery report records a GET to httpbin followed by a POST to UNCTADstat, both returning 200.' (https://swarmcha.se/posts/openai-unctad)
   - Fix: Say the Facts endpoint accepts only POST and its cross-origin header lets only UNCTAD's own site read responses from script; drop 'began'.
2. **imprecision** at tags; Defender takeaway; title
   - Claim: tags: [ai-abuse, auth-bypass, info-disclosure]; 'an AI vendor's own agents autonomously engineering an access-control bypass against public-sector infrastructure ... is now a repeated pattern'
   - Defect: Sources describe no authentication bypass and no non-public disclosure: SiliconANGLE says 'None of the data was secret' and the API key is public (UNCTADstat's viewer sends it with every request); Howard-Jones: 'Was this hacking? I don't think I'd call it that'; Transluce 'identified no instances ... where agents gained access to any information that is not publicly available'. The takeaway also states OpenAI authorship as fact where the primary says 'highly likely' on infrastructure overlap, and OpenAI is only 'reviewing these findings'.
   - Ground truth: SiliconANGLE: 'None of the data was secret. The agents wanted public figures ... The key they used for those queries was public too.' (https://siliconangle.com/2026/09/27/researcher-links-16000-scans-of-a-u-n-statistics-portal-to-openai-agents/)
   - Fix: Drop auth-bypass and info-disclosure tags; phrase the takeaway as 'agents attributed to OpenAI engineering a method-filter bypass against a public data API' and note the data was public.

### 2026-09-28/storm-3168-jadepuffer-azure-destructive-service-principal (imprecision)
1. **imprecision** at frontmatter sectors / priority
   - Claim: (low confidence) sectors: [public-sector, technology]; priority: high
   - Defect: Microsoft's blog does not name or characterise the victim organisation or its sector, so 'public-sector' (and the home-region nexus that the high priority leans on) is not in the cited source; it is a single-tenant incident whose observed activity dates to early June 2026 and whose guidance (rotate exposed secrets, locks) is generic. Context only: the priority bar rests on an assumed Azure/public-sector exposure.
   - Ground truth: Microsoft: 'Microsoft observed two compromised service principals belonging to the same tenant' (no sector or victim named); 'in early June 2026, one of the compromised service principals enumerated ...' (https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)
   - Fix: Remove public-sector from sectors unless a source names it; re-grade priority on the exposure of Swiss Azure tenants (leaked workload-identity secrets) rather than on the victim sector.

### 2026-09-29/bitget-hot-wallet-theft-north-korea-nexus (factual-error)
1. **factual-error** at evidence[0]; body paragraph 1
   - Claim: "the attacker may have exploited a vulnerability in a third-party security product to potentially obtain high-level internal credentials," then used those credentials "to impersonate authorized activity and send fraudulent withdrawal commands to the wallet system,"
   - Defect: LEAD CONFIRMED: the quoted wording is not a contiguous passage of the cited Bitget page as it reads today. Bitget has revised the page: it now states the attacker 'exploited a vulnerability in a third-party security product to obtain high-level internal credentials' and, in the findings section, 'a zero-day vulnerability in a third-party security product'; neither the hedges 'may have' / 'potentially' nor 'to impersonate authorized activity' remain. The entry's hedged framing of Bitget's own conclusion is outdated (Bitget, THN 2026-09-28, Mandiant and SlowMist all state the compromise as found).
   - Ground truth: Bitget page: 'The latest investigation found that the attacker exploited a vulnerability in a third-party security product to obtain high-level internal credentials. The attacker then used those credentials to send fraudulent withdrawal commands to the wallet system, resulting in abnormal transfers that bypassed existing risk controls.' (https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)
   - Fix: Replace evidence[0] and the body quotation with the current wording (or attribute the hedged wording to the page's 2026-09-27 version) and drop 'may have' / 'potentially' from the narration.
2. **imprecision** at body paragraph 1, last sentence
   - Claim: the vulnerable third-party product's vendor was notified and the affected functionality disabled pending a fix.
   - Defect: The cited Bitget page now says the underlying vulnerability was remediated; 'pending a fix' reflects the earlier state (THN 2026-09-28: 'Bitget has not said whether the vendor has released a fix').
   - Ground truth: Bitget page: 'The affected systems were isolated and the underlying vulnerability was remediated. ... the relevant third-party vendor was notified and affected functionality was disabled.' (https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)
   - Fix: Say the vendor was notified, the affected functionality disabled, and Bitget states the vulnerability was remediated.

### 2026-09-30/cve-2026-86950-apple-coregraphics-zero-day-kev (factual-error)
1. **factual-error** at cves[0].epss
   - Claim: epss: "0.81"
   - Defect: The field must carry the FIRST.org EPSS probability in [0, 1]; 0.81 reads as 81% and is a percent-scale figure copied from ENISA EUVD (the 2026-09-30 research note records 'EPSS 0.81' from EUVD). EUVD's epss field is on a percent scale: today it shows 1.24 while FIRST's probability for the same CVE is 0.01242 (percentile 0.687). The corresponding probability on the entry date would have been about 0.008, not 0.81.
   - Ground truth: FIRST EPSS API 2026-10-16: {"cve":"CVE-2026-86950","epss":"0.012420000","percentile":"0.686880000"}; ENISA EUVD record EUVD-2026-88445: "epss":1.24 (https://api.first.org/data/v1/epss?cve=CVE-2026-86950)
   - Fix: Set epss to the FIRST probability (null if not re-looked-up; 0.0124 as of 2026-10-16) via an internal correction record.
2. **imprecision** at body paragraph 1
   - Claim: (low confidence) CISA added the flaw to its Known Exploited Vulnerabilities catalog on 2026-09-29 and attached its forensic-triage requirements to the listing
   - Defect: In the KEV record as read on 2026-10-16 (catalog 2026.10.16) the forensicTriage field for CVE-2026-86950 is "No"; the 'Forensics Triage Requirements' appear only in the BOD 26-04 boilerplate of requiredAction/notes that every new entry carries, so the sentence suggests a triage flag the record does not set (the research note of 2026-09-30 had recorded forensicTriage=Yes, so the flag may have changed).
   - Ground truth: KEV: {"cveID":"CVE-2026-86950","dateAdded":"2026-09-29",...,"forensicTriage":"No"} (https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
   - Fix: State only that CISA added the flaw on 2026-09-29, or say the record's forensic-triage flag is set as the catalog shows when re-read.

### Clean entries
- 2026-09-29/kaspersky-payload-gpo-encryptionless-ransomware
- 2026-09-29/push-security-clickfix-h2-2026-detection-review
- 2026-09-29/openai-dns-tunnel-sandbox-escape-self-replicating-injection
