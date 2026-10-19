**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-11T16:59:05Z · ended_at=2026-10-11T17:16:48Z · duration_seconds=1063

## Verification report — 2026-10-11T1307Z-audit (iteration 3, slice s3)

Scope: 9 entries, 193 ledger claims (61 changed since iteration 2). All 193 have a verdict row in `verification.iter3.s3.claims.yaml` (181 ok, 8 F3, 4 F4). Every cited page was fetched this iteration (extract, raw HTML for dates, `ncsc-csh post`, `cisa-kev`); 14 findings sit outside the ledger (legacy sections and evidence[] that this fire edited or left in place).

### Prior-iteration deltas (all 35 checked against disk and source)

Landed and holding: MRSProxy relay clause now states only what Franky's Web says; Emergency Mitigation absence cited to Franky's Web and BSI access advice to heise; RoguePlanet product list and CWE cited to MSRC, estate reading marked "in the entry's reading", monitoring action dropped, inline T1068 removed; nginx score attributions per page; DENIC time-zone conversion marked as reading; MuddyWater T1041 restored, certificate sentence and "within the session" corrected, file names removed; ShinyHunters Nottingham count attributed to Have I Been Pwned, Oracle/Mandiant roles, BleepingComputer script description, Mandiant entry surface, hardening split, Council of Europe wording, "first" dropped, citations added, actions[1] dropped; Cisco record summary no longer carries pipeline vocabulary; SAP title/action/detection name the Data Hub Adapter endpoint, exploited status declined (rationale accepted as a judgement call, see note below); GitLab sentence on readable files, action list, three vendor detections, CVE-2026-87719 edit-history attribution.

Did not fully land (raised again, low confidence): GitLab foothold clause (still present after the citation), SAP 08-16 section ("import-job", ETL, still there), nginx Exposure clause (cites a depthfirst page that lacks "unnamed" and "if"), SAP DIAG weighting (unmarked clause remains), DENIC 10 May section wording (unchanged).

Declined rationales: DENIC F7 (length) accepted, the entry carries the vendor root cause and a resolver-operator lesson at routine priority; SAP `exploited` status accepted as a judgement call (Defused honeypot attempts plus BleepingComputer "targeted in the wild"), noting that NCSC-NL only relays Defused (finding on claim 97b8af6ea2) and that the nginx entry applies a stricter standard to the same evidence class (VulnCheck honeypots, THN headline "Exploited in the Wild"); the main agent may want one consistent rule.

### Citation does not support the claim

**F3 #1** `shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.` — body first paragraph: "TechCrunch independently corroborated the scale of the campaign and the education-sector skew" (claim ff8a9a155f)
- (low confidence) TechCrunch relays the same actor claim: "a ShinyHunters member told TechCrunch on Wednesday". It verified nothing independently, so "independently corroborated" is not what the page says.
- Source: TechCrunch: "The notorious cybercrime group ShinyHunters claimed to have hacked Oracle PeopleSoft servers at more than 100 organizations, many of them universities, a ShinyHunters member told TechCrunch on Wednesday." (https://techcrunch.com/2026/06/10/cybercriminals-claim-breach-of-oracle-peoplesoft-servers-at-100-plus-organizations/)
- Fix: Say TechCrunch was told the same by a ShinyHunters member, not that it corroborated.

**F3 #2** `shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.` — ## Update 2026-06-12: "published an out-of-band Security Alert with fixes ([Oracle, 2026-06-10]; [SecurityWeek, 2026-06-11])"
- (low confidence) The co-cited SecurityWeek page says the opposite on fixes: Oracle appears to have released mitigations only. Rapid7 and BleepingComputer (not cited here) say a patch shipped, so the sources conflict and the entry picks one silently; the summary also says "Oracle fixed it out of band".
- Source: SecurityWeek: "It appears that only mitigations have been released by Oracle rather than a full patch." Rapid7: "Oracle released an out-of-band patch the same day as the advisory." (https://www.securityweek.com/oracle-addresses-peoplesoft-vulnerability-amid-reports-of-zero-day-attacks/)
- Fix: Cite Rapid7 for the patch, drop SecurityWeek from that clause or add a Contradiction line.

**F3 #3** `shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.` — ## Update 2026-06-16: "claiming 297 GB across ~429,000 files taken via the Oracle PeopleSoft Environment Management Hub zero-day CVE-2026-35273 ... ([SecurityWeek, 2026-06-15])"
- (low confidence, earlier-fire sentence) The cited SecurityWeek page reports the leak-site listing and sizes but does not tie the Council of Europe claim to PeopleSoft, the Environment Management Hub or the CVE; its only PeopleSoft mention is a context line. The Register (cited later in the next paragraph) makes the PeopleSoft link.
- Source: SecurityWeek: "Last week, Google confirmed that a new ShinyHunters campaign exploited a zero-day vulnerability in Oracle PeopleSoft, likely impacting 100 organizations." The Register: "another victim of the Oracle PeopleSoft heist ... tracked as CVE-2026-35273". (https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/)
- Fix: Cite The Register for the PeopleSoft/CVE link and drop "Environment Management Hub" unless a source ties it to this victim.

**F3 #4** `cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea` — frontmatter summary: "affects NGINX 0.6.27–1.30.0, Plus R32–R36, Kubernetes Ingress Controller, and multiple F5 products (NCSC-CH Security Hub #12575, 2026-05-15)" (claim 568b9dcc15)
- (low confidence) The terminating NCSC-CH citation carries product names only, no version ranges.
- Source: NCSC-CH post 12575: "AFFECTED PRODUCTS: NGINX Open Source, NGINX Plus, ... For specific versions, please check the references." (https://security-hub.ncsc.admin.ch/#/posts/12575)
- Fix: Cite nginx.org (0.6.27-1.30.0) and depthfirst / Security Affairs (Plus R32-R36) for the ranges, or drop the parenthetical.

**F3 #5** `cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea` — body **Exposure:** "an unnamed capture and a `?` in the replacement, followed by another `rewrite`, `if` or `set` in the same scope ([depthfirst, 2026-05-13])" (claim f54587938d); prior-iteration remediation only partly lands
- (low confidence) The cited depthfirst research writeup describes a rewrite with "?" in the replacement followed by a `set` directive that references a capture group. It has no "unnamed" capture and no "rewrite/if" follow-on. The exact sentence is on depthfirst.com/nginx-rift and in Security Affairs.
- Source: depthfirst.com/nginx-rift: "a `rewrite` directive with an unnamed regex capture (`$1`, `$2`) and a replacement string that contains a question mark, followed by another `rewrite`, `if`, or `set` directive". The cited /research/ page: "This is where ... a subsequent `set` directive references a regex capture group". (https://depthfirst.com/nginx-rift)
- Fix: Cite https://depthfirst.com/nginx-rift or Security Affairs for the Exposure clause.

**F3 #6** `denic-de-dnssec-outage-faulty-key-rollover-3-5-h-disruption.` — body paragraph 1: "heise dates the first disruption to 21:43 local time, 19:43 UTC" (claim c28965c3cc)
- (low confidence) heise states no time zone. "local time" and the UTC conversion are the entry's reading, stated flat, while the same sentence marks the DENIC conversion as "giving no time zone; read as CEST".
- Source: heise: "Am 5. Mai um 21:43 knirschte es im deutschen Teil des Internets". (https://www.heise.de/news/DNS-Probleme-mit-de-Domains-DENIC-liefert-erste-Erklaerung-11288197.html)
- Fix: Write "heise gives 21:43, which read as CEST is 19:43 UTC".

**F3 #7** `ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md` — body paragraph 2: "the Malware Protection Engine (`mpengine.dll`) auto-updates multiple times a day by default" (claim 1ac4431122)
- (low confidence) The MSRC FAQ gives the engine release cadence as monthly or as needed; the multiple-times-daily figure is for definitions and, as an upper bound ("up to"), for update checks.
- Source: MSRC FAQ: "Microsoft typically releases an update for the Microsoft Malware Protection Engine once a month or as needed ... Microsoft also typically updates the malware definitions three times daily"; "the software may search for engine and definition updates every day ... up to multiple times daily". (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656)
- Fix: Reword to MSRC's statement: engine and definition updates are applied automatically by default, no manual action normally required.

**F3 #8** `sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce.m` — frontmatter summary: "an improper-authorization flaw ... that Onapsis describes as insufficient authorization checks and input validation reachable without authentication" (claim 7cec3f6937)
- (low confidence) Onapsis does not say "without authentication" for this note; that comes from SAP's text quoted by BleepingComputer.
- Source: Onapsis: "caused by insufficient authorization checks and input validation. Successful exploitation could enable arbitrary code execution and compromise internal components". BleepingComputer (SAP): "allows an unauthenticated attacker to abuse a default authentication client". (https://onapsis.com/blog/sap-security-patch-day-august-2026/)
- Fix: Move "reachable without authentication" outside the Onapsis attribution.

**F3 #9** `sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce.m` — body paragraph 3: "CVE-2026-34265 (CVSS 9.8, Note 3714806) is the one to weigh against internal network exposure rather than internet exposure: 'Logical errors ...' ... ([Onapsis])" (claim 11f533031e); prior-iteration remediation only marked the later DIAG sentence
- (low confidence) Onapsis carries the quoted sentence and the outcome, not the internal-versus-internet weighting, which is the entry's own judgement left unmarked inside the cited sentence.
- Source: Onapsis: "Logical errors in DIAG protocol parsing allow an unauthenticated attacker to generate memory corruptions. The vulnerability could potentially disclose sensitive system information or crash the system". (https://onapsis.com/blog/sap-security-patch-day-august-2026/)
- Fix: Move the weighting outside the citation and mark it "in analyst judgement".

**F3 #10** `sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce.m` — body paragraph 4: "on 2026-08-15 NCSC-NL reported attackers actively scanning for vulnerable systems ([NCSC-NL, 2026-08-15])" (claim 97b8af6ea2)
- (low confidence) NCSC-NL relays Defused ("Defused meldt"); the scanning is Defused's report, not an NCSC-NL observation. The sentence credits NCSC-NL as the reporter without the Defused attribution, which also weakens the declined-F4 rationale that NCSC-NL is separate evidence of exploitation.
- Source: NCSC-NL: "Beveiligingsbedrijf Defused meldt dat kwaadwillenden actief scannen en op zoek zijn naar kwetsbare Data Hub Adapter-systemen." (https://advisories.ncsc.nl/2026/ncsc-2026-0302.html)
- Fix: Write "NCSC-NL relayed Defused's report of attackers actively scanning".

**F3 #11** `cve-2026-85706-gitlab-unauth-path-traversal-file-read.md` — body paragraph 1: "...CI/CD configuration data ([watchTowr]); that is what turns a file-read primitive into a foothold on the CI/CD and source-control plane GitLab manages."; prior-iteration remediation said the foothold conclusion was cut
- (low confidence) The remediation did not land as described: the foothold conclusion is still in the text, now after the closing parenthesis, unmarked as the entry's own inference. watchTowr says only that unauthorized file access "carries significant risk to enterprise environments".
- Source: watchTowr: "Because GitLab instances often hold sensitive source code, credentials, and CI/CD configuration data, any vulnerability that allows unauthorized file access carries significant risk to enterprise environments." (https://watchtowr.com/resources/rapid-reaction-gitlab-critical-path-traversal-vulnerability-cve-2026-85706/)
- Fix: Cut the clause or mark it "in analyst judgement".

### Unsupported / hallucinated facts

**F4 #1** `shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.` — frontmatter evidence[2] (publisher Rapid7)
- Evidence quote attributed to Rapid7 is not a substring of the Rapid7 page (the only Rapid7 source on the entry). The gate could not read this page, so it was not machine-checked. Quote: "CVE-2026-35273 is a critical remote code execution vulnerability (CVSS 9.8) in Oracle PeopleTools versions 8.61 and 8.62 that exploits a server-side request forgery flaw in the Environment Management component". The evidence list was edited this fire (the Hacker News record was removed), so the whole list is in scope.
- Source: Rapid7 page (fetched twice, extract and raw HTML): "a critical vulnerability in the Updates Environment Management component of PeopleSoft Enterprise PeopleTools" and "TrendAI has classified the underlying flaw as a server-side request forgery (CWE-918)"; grep for "that exploits a server-side request forgery" returns 0 hits. (https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273/)
- Fix: Replace with a contiguous sentence from the page (e.g. "Oracle released an out-of-band patch the same day as the advisory, underscoring the urgency of remediation.") or drop the record.

**F4 #2** `shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.` — body "Post-access lateral movement": "culminating in `T1567` Exfiltration Over Web Service"; techniques[] T1567 (claim e0aca45dca)
- (low confidence, legacy sentence) No cited source describes exfiltration over a web service. Mandiant describes zstd-compressed archives and an outbound SSH connection to the leak-site mirror, and its own ATT&CK table lists T1048 (Exfiltration Over Alternative Protocol), not T1567.
- Source: Mandiant (renewed-campaign post) ATT&CK table: "Exfiltration T1048 Exfiltration Over Alternative Protocol"; June post: "Compressed exfiltrated directories ... using zstd" and "outbound SSH connection from the staging host to ... the public mirror of the ShinyHunters Data Leak Site". (https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/)
- Fix: Map to T1048 (or drop the exfiltration id) and reword the sentence; keep T1567 only if a cited source states a web-service channel.

**F4 #3** `cve-2026-42945-nginx-open-source-plus-f5-waf-products-18-yea` — body paragraph 1: NCSC-CH rated the exploitation status "UNKNOWN, PoC Available" on 2026-05-15 (claim 44189baeab)
- (low confidence) The string in quotation marks is not verbatim, and the sentence has no inline citation.
- Source: NCSC-CH post 12575: "Current exploitation status: UNKNOWN, Proof of Concept Available". (https://security-hub.ncsc.admin.ch/#/posts/12575)
- Fix: Quote the post verbatim ("UNKNOWN, Proof of Concept Available") and add the NCSC-CH citation.

**F4 #4** `cve-2026-20230-cisco-unified-cm-webdialer-ssrf-to-arbitrary.` — record summary 2026-10-11T14:48:28Z: "rewritten with the facts of Cisco's 2026-06-04 disclosure" (claim d721036a50)
- (low confidence) Cisco's initial public release is 2026-06-03, not 06-04 (06-04 is the date of the folded brief entry).
- Source: Cisco advisory revision table: "1.0 Initial public release - Final 2026-JUN-03". BleepingComputer: "Cisco released security updates for the CVE-2026-20230 flaw on June 3". (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW)
- Fix: Say "Cisco's 2026-06-03 disclosure".

**F4 #5** `sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce.m` — ## Update 2026-08-16, Detection paragraph: "import-job invocations that do not line up with a scheduled integration run — an import that no ETL schedule accounts for is the anomaly, since this component's legitimate traffic is machine-generated and predictable"; "a host that normally talks only to its own data-integration peers"; prior-iteration remediation said this section "drops 'import'"
- (low confidence) The remediation did not fully land: "import-job" and "import" remain in this section while this fire's own correction says "No cited source calls the vulnerable endpoint an import endpoint". The ETL, machine-generated-traffic and "talks only to its own data-integration peers" statements are unsourced and stated as fact, not marked as analyst judgement.
- Source: BleepingComputer (SAP): "submit specially crafted input to certain functions lacking sufficient validation"; Onapsis: "restrict access to the vulnerable endpoint" (function not named). No cited page mentions imports, ETL schedules or the host's normal peers. (https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)
- Fix: Drop "import-job"/"import"/"ETL" or mark the whole detection paragraph as analyst judgement; remove the unsourced normal-traffic claims.

**F4 #6** `sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce.m` — ## Update 2026-08-16: "whoever is sending these requests built a working exploit without published research to copy, on a three-day clock"; "the interval between a public fix and a working exploit has collapsed to days"
- (low confidence, earlier-fire sentence) Defused reports exploitation attempts at honeypots; no source says the exploit works or that it was built from scratch rather than patch-diffed.
- Source: BleepingComputer (Defused): "First exploitation attempts against CVE-2026-58231 ... is now hitting our honeypots - 3 days after patch day ... no public PoC and is not known to be exploited." (https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)
- Fix: Say attackers developed exploitation attempts within three days, in analyst judgement, without "working".

**F4 #7** `exchange-mrsproxy-auth-bypass-cve-2026-62911-poc.md` — frontmatter summary: "lets a relayed Negotiate/NTLM authentication exchange be treated as the relayed account, giving an attacker who can capture or coerce that exchange full mailbox access" (claim 7b4bcc7cec)
- (low confidence) None of the five cited pages names NTLM (grep 0). Sources say "Negotiate authentication", "capture-replay" and a "captured hash". The body relay clause was cut back to Franky's wording this fire; the summary was not.
- Source: Franky's Web: "accepts Negotiate authentication but does not check the so-called channel bindings ... relay the authentication of the server account to the endpoint". (https://www.frankysweb.de/en/exchange-public-exploit-for-critical-vulnerability-cve-2026-62911/)
- Fix: Drop "/NTLM" and "capture or coerce" or cite MB VRED for the coercion/hash detail.

### Needs more research

**F8 #1** `ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md` — frontmatter actions[0]: "verify the installed Malware Protection Engine build is ≥ 1.1.26060.3008"; body ShieldBreak sentence
- The action floor is the RoguePlanet fix build. The entry records the ShieldBreak bypass (CVE-2026-69414) but not that Microsoft fixed it in a later engine, so a pinned estate that reaches 1.1.26060.3008 as instructed stays in the bypass range. Evidence is outside the entry's cited sources; the store's own ShieldBreak entry (in references[]) carries it.
- Source: MSRC CVE-2026-69414 (last updated Sep 3, 2026): "Last version of the Microsoft Malware Protection Engine affected by this vulnerability 1.26070.7; First version ... addressed 1.1.26080.3"; 2.0 revision: "Microsoft has released an update ... that addresses the vulnerability identified by CVE-2026-69414." (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414)
- Fix: Add the MSRC CVE-2026-69414 source, state the fix build 1.1.26080.3, and raise the action floor or name both builds.

### Action-item discipline

**F18 #1** `cve-2026-85706-gitlab-unauth-path-traversal-file-read.md` — frontmatter actions[1]: "For any instance with a Duo Chat-enabled account, hunt for anomalous GraphQL subscription requests targeting Advanced Search configuration retrieval ..."
- (low confidence) Restates the hunting guidance of the 2026-09-13 section (audit logs for GraphQL subscription requests with abnormal argument shapes targeting Advanced Search) and rests on the thin edit-history exploited status; the patch action already covers CVE-2026-87719.
- Source: Entry body, ## Update 2026-09-13: "Audit logs for GraphQL subscription requests with abnormal argument shapes targeting Advanced Search ... are the discriminators". (https://security-hub.ncsc.admin.ch/#/posts/12935)
- Fix: Drop actions[1] (body keeps the guidance) or fold "rotate Advanced Search credentials if access is found" into actions[0].

### Editorial / less-is-more flags (advisory)

**F11 #1** `denic-de-dnssec-outage-faulty-key-rollover-3-5-h-disruption.` — ## Update 2026-05-10 first paragraph; frontmatter kind, event_date
- Advisory, low confidence. (1) The prior-iteration fix for the dated-before-the-event wording did not change the text: the 10 May section still reads "DENIC's addendum of 11 May 2026 states ..." with no "later". (2) kind: policy is defined as a regulatory action, deadline or authority guidance; a non-adversarial outage post-mortem is not that (incident would need techniques, so this reads as a rule workaround). (3) event_date 2026-05-08 matches neither the outage (05-05) nor the first primary (05-06).
- Source: DENIC analysis: "Nachtrag vom 11. Mai 2026: Eine Keytag-Kollision lag nicht vor." site/taxonomy.yaml: "kind: policy - a regulatory action, deadline or authority guidance". (https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/)
- Fix: Optional: "DENIC's later addendum of 11 May"; consider kind research; event_date 2026-05-05 or 05-06.

**F11 #2** `cve-2026-20230-cisco-unified-cm-webdialer-ssrf-to-arbitrary.` — frontmatter sources[0].date; record summary
- Advisory, low confidence. sources[0] dates the Cisco advisory 2026-07-01 (the revision) although it was first released 2026-06-03 (iteration 2 raised it; only the record summary was touched). The record summary also narrates folding ("absorbing the separate disclosure-day entry") rather than the reader-facing delta.
- Source: Cisco revision table: "1.1 Added information about active exploitation 2026-JUL-01; 1.0 Initial public release 2026-JUN-03". (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW)
- Fix: Date the source 2026-06-03 (or note the 07-01 revision) and trim the record summary.

**F11 #3** `ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md` — frontmatter summary: sat in "no fix" for over three weeks; record summary
- Advisory, low confidence. (1) "no fix" is in quotation marks but is not a source phrase (NCSC-CH: "no patch available"). (2) The record summary narrates references, source rating, evidence and action changes that the section does not state (4c(d)); the iteration-2 decline called it append-only, but this fire's own record is editable.
- Source: NCSC-CH: "Current exploitation status: Proof of Concept Available, no patch available". (https://security-hub.ncsc.admin.ch/#/posts/12622)
- Fix: Drop the quote marks; trim the record summary to the section.

**F11 #4** `cve-2026-85706-gitlab-unauth-path-traversal-file-read.md` — frontmatter sources[] (duplicate NCSC-CH record); em dashes across entries
- Advisory, low confidence. sources[] carries https://security-hub.ncsc.admin.ch/#/posts/12935 twice (two dates). Em dashes remain in reader-facing text of several entries (nginx 4, shinyhunters 10, rogueplanet 4, sap 12, exchange 21, gitlab 7); the site strips them at render and the gate checks only new text, so this stands as advisory.
- Source: site/build.py section "EM-DASH NORMALISATION" (operator directive 2026-08-29). (https://security-hub.ncsc.admin.ch/#/posts/12935)
- Fix: Optional: merge the duplicate source record.

### Verdict

NEEDS_FIXES (truth: 18, editorial: 2, advisory: 4)

No missed-angle or coverage finding for this slice (it holds existing entries only). Entity links checked against the registry (actor:chaos-ransomware is registered as distinct from the MuddyWater false-flag operation; the body disambiguates). check_run.py (full) currently reports one run-clock FAIL for the run record (completed precedes the iteration-2 verifier end); that is a Phase 6 re-stamp item, not an entry defect.

### Findings summary (machine-readable)

See `work/2026-10-11T1307Z-audit/verification.iter3.s3.findings.yaml` (24 records).
