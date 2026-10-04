**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-09-30T12:43:55Z · ended_at=2026-09-30T13:19:09Z · duration_seconds=2114

## Verification report — 2026-09-30T0639Z-audit (iteration 3, slice s3)

### Citation does not support the claim

**#1 F3** `2026-09-29/bitget-hot-wallet-theft-north-korea-nexus`: Bitget: $351.6M presented as TRM Labs' initial on-chain estimate
- Quote: up from TRM Labs' initial on-chain estimate of about $351.6M (TRM Labs, 2026-09-25); record summary: TRM Labs' attribution reasoning and loss figures are stated as TRM reports them
- Evidence / fix: TRM page: 'Bitget reported a loss of USD 351.6 million' and 'This post uses Bitget's figure'; TRM's own early on-chain estimates were 'USD 170-190 million' (EVM chains), with XRP/TRX outflows bringing observed outflows only 'close to' Bitget's figure. So 351.6M is Bitget's reported loss relayed by TRM, not TRM's initial on-chain estimate. Low-severity companion: 'a fund TRM puts at USD 464 million' - TRM writes 'Bitget ... says its USD 464 million User Protection Fund covers the loss' (Bitget's figure, relayed). Fix: 'up from the roughly $351.6M Bitget first reported (as relayed by TRM Labs)'; 'a fund of USD 464 million according to TRM Labs'. Claims a0e120632a, bbdd6e8903, 9578fa2aa1.

**#2 F3** `2026-09-22/plugin4shell-ai-coding-agent-sha-pinning-bypass`: (low confidence) Plugin4Shell: takeaway says the Copilot fix rests on GitHub support's statement 'to heise online'
- Quote: keeping in mind that the Claude Code fix rests on AIR's account and the Copilot fix on GitHub support's statement to heise online
- Evidence / fix: heise says only 'Nach Angaben des GitHub-Supports steckt der Fix in ...' and earlier 'heise developer hat GitHub um eine Stellungnahme gebeten'; it never says the support statement was made to heise. Drop 'to heise online' or say 'as reported by heise online'. Claim 2425d3d2f5.

**#3 F3** `2026-09-29/openai-dns-tunnel-sandbox-escape-self-replicating-injection`: (low confidence) OpenAI: GitHub-token incident dated 'in May'
- Quote: a model that in May smuggled a private GitHub token to view another team's work
- Evidence / fix: TechCrunch says 'Another incident, discovered in May'; the event date is not given. Say 'discovered in May'. Claim 89c65be7d1.

**#4 F3** `2026-09-27/qbusoft-medyc-poland-healthcare-breach-fingerprint-actor`: (low confidence) Qbusoft: 'five million patients and 8 million photos, which ZTS could not confirm'
- Quote: The attackers claim data on five million patients and 8 million photos, which ZTS could not confirm
- Evidence / fix: ZTS 2026-09-25: 'we assessed the scale at least a million; according to the perpetrators five million' and 'another source of ours confirmed our assessment of the scale ... complete database going back up to 7 years'; only the photo count is stated as unconfirmed ('nie udalo nam sie potwierdzic'). Say 'ZTS could not confirm the photo count and gives its own estimate of at least a million patients'. Claim b9e3456aca.

**#5 F3** `2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev`: Citrix Correction: 'Mandiant's interim network controls apply to CVE-2026-88772 only'
- Quote: Correction (this run): 'Citrix has published no workaround (watchTowr), and Mandiant's interim network controls apply to CVE-2026-88772 only (GTIG/Mandiant)'
- Evidence / fix: GTIG: 'The DTLS and UDP/443 controls below are specific to CVE-2026-88772 and should not be relied on to mitigate CVE-2026-88771.' Its third interim control, 'Implement upstream IP allow-listing where feasible', is not scoped to one CVE, and the entry's own 09-30 'Interim controls' paragraph says so ('while upstream IP allow-listing ... is not scoped to one CVE'). Fix: 'Mandiant's DTLS and UDP/443 controls apply to CVE-2026-88772 only'. Same overgeneralisation in the main-text 'Detection and hunting' paragraph ('Mandiant's interim network controls for CVE-2026-88772 alone'), older text. Claim ce0c422b07.

**#6 F3** `2026-07-30/cisco-secure-fmc-cve-2026-20316-static-credential-exploited`: (low confidence) Cisco FMC Correction: content of later advisory revisions cited with the 2026-07-29 date
- Quote: Correction: "Cisco's fixed-release table lists 7.0 and earlier as affected, with 7.0.10 as the fix ... ([Cisco PSIRT, 2026-07-29])" and "it sends any device with indicators to TAC because its hot fix files may not address an existing compromise ([Cisco PSIRT, 2026-07-29])"
- Evidence / fix: Advisory revision history: 'Version 1.6 Added Fixed Releases table and removed Hot Fixes table ... 2026-SEP-16'; '1.2 Updated to make it clear to contact TAC ... 2026-JUL-31'; '1.4 Updated information about customer action with hot fixes ... 2026-AUG-05'. The initial 2026-07-29 text had neither the table nor the hot-fix/TAC wording, and the entry's own body dates the same table 'revised 2026-09-16'. Use 'revised 2026-09-16' in both citations. Claims a48bc6d52d, 6863e3865b.

**#7 F3** `2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal`: (low confidence) Check Point Correction: 'against a handful of customers' cited to the CPR blog
- Quote: Correction: 'Check Point reports attacks observed on 2026-07-23 against a handful of customers, not exploitation running continuously since then ([Check Point Research, 2026-09-22])'
- Evidence / fix: The CPR blog says 'we observed a handful of pinpointed attacks on July 23, 2026' and 'a handful of pinpointed exploitation'; 'a handful of customers who have been attacked' is sk1000171's wording (and sk1000171 is not the cited page for this clause). 'not exploitation running continuously since then' is the entry's inference; neither page says exploitation stopped. Fix: cite sk1000171 for the customers clause and drop or hedge the inference. Claim c9d11f2f96.

### Unsupported / hallucinated facts

**#8 F4** `2026-09-17/ddrop-dram-interposer-defeats-confidential-computing`: (low confidence) DDRop: title still asserts 'no CVE' for both vendors after the Correction says that went beyond what they published
- Quote: title: '... - no CVE, no vendor fix'; Correction: 'Only AMD says it does not plan to assign a CVE ... Intel's announcement does not mention a CVE ... The earlier statement that ... neither is assigning a CVE went beyond what they published.'
- Evidence / fix: AMD-SB-3048 says 'does not plan to assign a CVE'; the Intel announcement (2026-09-14-001) is silent on CVEs. The title (not in the record's fields) still states 'no CVE' unqualified, which is the overreach the Correction withdraws. Fix: 'AMD assigns no CVE' or drop 'no CVE' from the title. Claim 8367c8b908 / title.

**#9 F4** `2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning`: (low confidence) Kiteworks: title states the vendor's own claim as fact
- Quote: title: '... then lifted the advice and fixed a critical flaw it found meanwhile'
- Evidence / fix: Kiteworks' 2026-09-28 release is the only source for the discovery and the fix (the entry's own sourcing note and 09-30 section say 'The vendor's own statements are the only source for the discovery, the fix and the absence of exploitation'); the headline hedges ('says it fixed') but the title asserts it. Fix: 'and says it fixed a critical flaw it found meanwhile'.

**#10 F4** `2026-09-29/openai-dns-tunnel-sandbox-escape-self-replicating-injection`: OpenAI Correction: withdraws 'a pause triggered by this incident' although OpenAI ties the pause to the incident
- Quote: Correction: 'OpenAI states that training, evaluation and tool-use inference of its most capable models remain paused, which the summary had presented as a pause triggered by this incident'; published summary: 'triggering a training pause'
- Evidence / fix: OpenAI's DNS report (Investigation and response): 'The incident exposed a gap in our controls over network restrictions. We therefore stopped the affected training run and have subsequently decided to pause all other training, evaluation, and inference with tool-use (defined broadly) for our most capable models until we have both validated that the gap is resolved and performed additional red-teaming of the system.' The published wording was supported; the Correction withdraws a true statement on the false premise that OpenAI does not say so. Fix: drop the second Correction sentence (or restore 'the pause OpenAI decided on after this incident'). Claim 3030314cf7.

**#11 F4** `2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft`: Gentlemen: summary still says the chain 'exploits a public-facing GLPI SQL injection' after the Correction reduced it to an attempt
- Quote: summary: 'exploits a public-facing GLPI SQL injection and attempts Zerologon/MS17-010 for lateral movement'; Correction: 'Talos describes the actor's use of the GLPI SQL injection CVE-2025-24799 as an attempt ... and reports no outcome ... so the flaw is not recorded as exploited'
- Evidence / fix: Talos Phase 3: 'the actor attempted to exploit CVE-2025-24799 ... using both a PoC and sqlmap to retrieve user information from the database' (no outcome). The frontmatter summary (not in the record's fields) still asserts exploitation, which the newest section disproves (supersession). Fix: 'attempts a public-facing GLPI SQL injection'. Also 'enumerates AD via RustHound/BloodHound' in the same summary is Talos's hedged 'may also have used'.

**#12 F4** `2026-09-25/switzerland-sovereign-digital-infrastructure-motion-24-3209`: Swiss motion: Netzwoche is cited five times but no longer appears in sources[]
- Quote: frontmatter sources: only the Curia Vista OData record and Laux Lawyers; body: 'Netzwoche, 2026-09-25' cited for the 31:11 vote, the 126:66 vote, the 13:12 committee vote, the minority view and the Federal Council's reasoning; record summary: 'Netzwoche citations carry the date of its 2026-09-25 update'
- Evidence / fix: git diff HEAD shows the Netzwoche source record (netzwoche.ch/news/2026-03-23/staenderat-sagt-ja-zu-souveraener-ki-infrastruktur) was deleted by this run while every Netzwoche-derived fact remains, so the source list no longer carries the source of most of the body. The iteration-2 remediation log says the record was kept and re-dated 2026-09-25 with a publisher note; the file does not show that. Restore the record (date 2026-09-25 or 2026-03-23 consistently with the citations, publisher note 'report of 2026-03-23, updated 2026-09-25'). Netzwoche page dateline is 2026-03-23 with an 'Update vom 25.9.2026' block; the March 31:11 vote is from the 23 March original. Claims 7dec40c04f, b65bf97f7b.

### Claims missing inline citation

**#13 F5** `2026-09-27/qbusoft-medyc-poland-healthcare-breach-fingerprint-actor`: (low confidence) Qbusoft: summary says ZTS is 'the outlet that broke August's MyDr breach'
- Quote: summary: 'Zaufana Trzecia Strona, the outlet that broke August's MyDr breach, attributes both intrusions ...'
- Evidence / fix: None of the four cited pages (ZTS x2, TVP World, DataBreaches.net) says ZTS broke the MyDr story. The store's MyDr entry says attackers 'approached' ZTS, but that is not a cited source here. Drop the clause or cite ZTS's own MyDr post. Claim e917f1d912.

**#14 F5** `2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle`: (low confidence) HPE: product descriptions cited to bulletins that do not carry them
- Quote: HPE published two Aruba Networking security bulletins on 2026-09-01: HPESBNW05133 for HPE Networking Fabric Composer (AFC), the controller that manages Aruba CX switch fabrics, and HPESBNW05134 for AOS-CX, the network OS on Aruba's CX-series campus and data-center switches ([HPE, HPESBNW05133]) ([HPE, HPESBNW05134])
- Evidence / fix: Both bulletins only name 'HPE Networking Fabric Composer' and 'HPE Networking AOS-CX' (read in full); the role descriptions are background from no cited page. The pre-run text carried the same descriptions. Drop them or cite a page that states them. Claim ec0f5c4fd6.

### Editorial / less-is-more flags (advisory)

**#15 F11** `2026-09-18/ntc-swiss-solar-inverter-cybersecurity-assessment`: (low confidence) NTC: record summary states more than the Correction section
- Quote: record summary: 'The Federal Office of Energy's confirmation, the CVE statement and the takeaway now follow the cited pages'; section: only the Bern tender attribution
- Evidence / fix: The published body said the Federal Office of Energy 'independently confirms NTC's assessment, per SRF' and 'No CVEs were assigned to any of the findings'; both were unsupported and are now changed, yet the reader-facing Correction section mentions only the Bern tender. Either add one sentence to the section naming these two withdrawn statements or trim the record summary to what the section states. Claim 4c932a6235.

**#16 F11** `several (Kiteworks, NTC, Unbound, OpenAI)`: Record summaries narrate metadata (verification badge, rating, stacked takeaways)
- Quote: Kiteworks: 'the stacked takeaways are merged into one, and the verification badge reflects that all reporting traces to Kiteworks'; NTC: 'the verification badge reflects the single underlying assessment'; Unbound: 'The rating and verification badge reflect a single assessor'; OpenAI: 'the verification badge reflects that the findings are OpenAI's own disclosures about its own systems'
- Evidence / fix: Changelog summaries render for readers; 'verification badge', 'rating' and 'stacked takeaways are merged' describe the entry's frontmatter/composition rather than what the sources say. Advisory: drop those clauses or say 'now rated as one underlying assessor'.

**#17 F11** `2026-09-29/openai-dns-tunnel-sandbox-escape-self-replicating-injection`: (low confidence) OpenAI: entities[] still carries three incident keys the shortened body no longer mentions
- Quote: entities: incident:openai-australia-medicare-agent-breach-2026-06, incident:openai-dsewiki-agent-collusion-2026-05, incident:openai-unctad-agent-scan-2026-04
- Evidence / fix: The rewrite removed the UNCTAD and Medicare sentences, and DSEWiki was never described; the entities[] links (which feed the entity graph) now assert a connection the text does not make. Keep only incident:openai-misalignment-disclosures-2026-09 unless a cited sentence names the others; references[] can carry the two entries.

**#18 F11** `2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle`: HPE Correction/record summary narrate source policy and miscount ('correct four points' lists five)
- Quote: Correction: 'HPE's own bulletins are published as plain-text advisories and correct four points.'; record summary: 'rested on relays and on MITRE CVE Services records that are not citable sources'
- Evidence / fix: The section then enumerates five corrections (52 vs 45 and the 7.3.3 bound, 34 CVEs, the 10.18 range, the 10.10 branch, the exploitation statement), and the record summary explains the change by the repo's citation policy rather than by what the sources say. Advisory: drop 'four', and say 'rested on relays and on CVE-record mirrors' or state the substantive change only.

**#19 F11** `2026-09-17/kairos-libercourt-commune-ransomware-confirmed`: (low confidence) Kairos: takeaway opens with a composition-rationale sentence
- Quote: **Defender takeaway:** the ground for carrying this is the victim class, small local administrations like the constituency's communes, claimed repeatedly by one actor.
- Evidence / fix: States why the entry exists rather than the decision it supports (check 12: composition-rationale sentences in reader text). Advisory: lead with the decision ('treat a leak-site listing that names your organization as an incident trigger').

### Quantifier without source

**#20 F14** `2026-09-18/ntc-swiss-solar-inverter-cybersecurity-assessment`: (low confidence) NTC: 'across every connected installation' after the em dash (older text)
- Quote: compromising one manufacturer's cloud could let an attacker trigger the same unauthenticated shutdown across every connected installation simultaneously
- Evidence / fix: NTC: 'if an attacker gains control of a manufacturer's cloud, the same manipulation could be triggered simultaneously across thousands of connected installations' (change in feed-in, not framed as an unauthenticated shutdown; the unauthenticated part is the local interface). 'every' and 'unauthenticated shutdown' go beyond the page; the clause is also uncited and still carries an em dash. Not touched by this run, so low priority.

**#21 F14** `2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning`: (low confidence) Kiteworks: summary states 'no CVE is known' unattributed
- Quote: summary: 'BSI names Kiteworks Advanced Forms below 9.5.1 as affected; no CVE is known.'
- Evidence / fix: Support for the absence of a CVE is watchTowr's 2026-09-25 remark ('There is no known CVE') and the BSI record and Kiteworks releases simply not naming one; The Record adds Kiteworks did not answer whether one existed. The 2026-09-29 section was reworded to 'Neither the BSI record nor Kiteworks' releases name a CVE' but the summary still states the negative flatly. Fix: 'neither BSI nor Kiteworks names a CVE'. Claim 403915b31a.
### Verdict

NEEDS_FIXES (truth: 14, editorial: 2, advisory: 5)

The five findings that carry weight (the rest are marked low confidence): OpenAI #F4 (the Correction withdraws a pause-trigger statement that OpenAI's report supports), Swiss motion #F4 (the Netzwoche source record was deleted while five inline Netzwoche citations remain, contrary to the iteration-2 remediation log), Gentlemen #F4 (summary still says "exploits" GLPI SQLi after the Correction reduced it to an attempt), Bitget #F3 ($351.6M is Bitget's figure relayed by TRM, not TRM's on-chain estimate), Citrix #F3 (Correction says all Mandiant interim controls are CVE-2026-88772-only; the IP allow-list control is not).

### Prior-iteration deltas (walked against sources fetched this pass)

Confirmed correct as remediated: DDRop install time and three access vectors restored with citation, vendor positions and TDX-only attestation forgery; Plugin4Shell (Copilot fix per heise/GitHub support, GitLab not exploitable, Google confirmation given to the researchers, rev-parse HEAD check attributed to AIR); actions-cool (Harden-Runner block list, event_date 2026-05-18); Bitget SlowMist "attempting" kept, TraderTraitor/alias claims corrected, Bitget/TRM figure split (but see #1); NTC (FOE "confirms the analysis", takeaway split, CVE statement limited to the two pages, single-source consistent with sourcing note); Unbound (severities and nine-CVE count from the oss-security announcement, credibility 2, single-source, Correction heading); Kiteworks opening facts re-cited per page, CVE statement limited to BSI/Kiteworks, law enforcement vs federal intelligence surfaced with four citations, single-source; Citrix "independently" wording, GTIG sector sentence; Check Point "first" removed, em dashes removed from the two rewritten paragraphs; Cisco FMC no hot-fix file names, existing-compromise warning attributed to the hot fix files, device-credential claim removed; HPE SSH quote verbatim in HPESBNW05133, 10.18 sentence citing HPE and CERT-FR each for its own half; Gentlemen Talos hedges kept; OpenAI Triage matches the DNS report, UNCTAD/Medicare sentences gone, body two paragraphs; Qbusoft title/headline/summary attribute the link to ZTS; Kairos "data-theft-only" gone; SolarWinds record wording; TeamCity KEV-history claim gone and Exposure line matches JetBrains; Linux KEV Contradiction line quotes THN and Red Hat.

Not confirmed: Swiss motion sources[] dating (record deleted, see F4); Bitget registry summary (entities/registry.yaml, incident:bitget-hot-wallet-theft-2026-09) is correct against TRM, Mandiant and SlowMist (no attribution of Bybit/AFX Bridge to TraderTraitor in its own voice, Mandiant appliance A/B and SlowMist Product A zero-day stated separately, no CVE/alias claims).

Coverage: all 430 claims in claims.iter3.s3.yaml have a verdict row (417 ok, 13 non-ok). Sources not readable by any transport this pass: SolarWinds trust-center advisory (403 on every transport; the gate's cached body from this run supports the two claims, so they are marked ok on that cached body); cybersecuritynews.com (CAPTCHA; not cited inline in actions-cool). Whole-run coverage (F10) not assessed at slice level.
