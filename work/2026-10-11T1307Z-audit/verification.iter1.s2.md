**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** see verify.iter1.s2.started_at / ended_at

## Verification report — 2026-10-11T1307Z-audit (iteration 1, slice s2)

Scope: 22 entries, 322 ledger claims, all answered (`verification.iter1.s2.claims.yaml`). Every cited page was fetched or read from the gate cache this iteration (cached bodies first; `extract`, `url`, `pdf`, `ncsc-csh post`, `cisa-kev` and the CVE record API where a rung needed it). No `unreadable` claims.

### Citation does not support the claim

1. **F3 #1 — `entries/2026-06-12/cve-2026-25089-fortinet-fortisandbox-unauthenticated-os-comm.md`**
   - Where: body § Exposure ('NCSC-NL also lists FortiSandbox 4.2 as affected'), record summary of 2026-10-11T14:01:19Z, vs the section's own 'NCSC-NL says Fortinet fixed the flaw in ... 4.2 through 5.0.5'
   - Finding: (low confidence) NCSC-NL's advisory says Fortinet fixed a vulnerability 'in FortiSandbox versies 4.2 tot en met 5.0.5'; it carries no 'affected versions' list and does not use the word affected. The Exposure line and the record summary turn that into 'lists 4.2 as affected', while the correction section words it as 'fixed the flaw in'. Wording should match what the page says.
   - Ground truth: NCSC-2026-0189: 'Fortinet heeft een kwetsbaarheid verholpen in FortiSandbox versies 4.2 tot en met 5.0.5, inclusief FortiSandbox Cloud en FortiSandbox PaaS.' (https://advisories.ncsc.nl/advisory?id=NCSC-2026-0189)
   - Fix: Say NCSC-NL's advisory covers 'versions 4.2 through 5.0.5' (which implies 4.2 is in scope but is not stated as such), in the Exposure line and the record summary alike.

2. **F3 #2 — `entries/2026-07-16/cve-2026-46817-oracle-ebs-payments-preauth-rce-kev-listed.md`**
   - Where: sources[0].date '2026-05-28' and body '[Oracle CSPU, 2026-05-28]', 'the 28 May patch date', summary/actions 'after 2026-05-28'
   - Finding: Oracle's CSPU page carries Updated Date 2026-05-21, seven days before the cited 2026-05-28; the 28 May figure comes from Help Net Security ('left unpatched past May 28 as potentially compromised'), which calls the patch 'late May 2026', not a patch date. The body presents 28 May as 'the patch date'.
   - Ground truth: Oracle page meta: Updated Date 2026-05-21T20:07:01Z; Help Net Security: 'The vulnerability was patched by Oracle in late May 2026.' ... 'unpatched past May 28 as potentially compromised' (https://www.oracle.com/security-alerts/cspumay2026.html)
   - Fix: Date the Oracle citation 2026-05-21 (or the advisory's stated release date) and word the hunt window as Help Net Security's 28 May threshold rather than 'the 28 May patch date'.

3. **F3 #3 — `entries/2026-06-30/cve-2026-48558-simplehelp-rmm-oidc-sso-authentication-bypass.md`**
   - Where: body § Detection: 'on managed endpoints, the RMM agent launching Node.js, PowerShell or Python to fetch scripts from temporary tunnel domains ([BleepingComputer, 2026-06-29])'
   - Finding: The cited BleepingComputer article does not name Node.js, PowerShell or Python or an RMM agent launching them; it says only that TaskWeaver 'was downloaded in the form of an obfuscated JavaScript file named jquery.js from a temporary Cloudflare domain'. The runtime-launch detection comes from Blackpoint's own post, which is not cited.
   - Ground truth: Blackpoint: 'Detect suspicious runtime execution. Alert when RMM software launches Node.js, PowerShell, Python, Deno, or Bun, particularly from temporary, download, remote-support, or user-writable directories.' and 'executed it through Node.js: node.exe <path>\jquery.js' from a trycloudflare.com address (https://blackpointcyber.com/blog/a-djinn-in-the-machine-taskweavers-node-js-intrusion-chain/)
   - Fix: Cite the Blackpoint post for the detection sentence (add it to sources[]) or reduce the claim to what BC states.

4. **F3 #4 — `entries/2026-09-28/storm-3168-jadepuffer-azure-destructive-service-principal.md`**
   - Where: body **Triage:** '... then a credential-harvesting ListKeys sweep, from principals with no prior operational history of this pattern ([Microsoft Security Blog, 2026-09-25])'
   - Finding: The citation terminates a clause that includes 'from principals with no prior operational history of this pattern'. The Microsoft post says nothing about the principals' prior history or baseline; it describes the enumeration, destruction and ListKeys phases only. The clause is the entry's own inference attached to a citation that does not carry it. (Minor: the post says 'five unique tokens', not 'OAuth tokens', in the body's automation paragraph.)
   - Ground truth: Microsoft: 'Microsoft observed two compromised service principals belonging to the same tenant. One performed reconnaissance and resource discovery. The other performed discovery, destructive operations, and credential collection.' (no statement on prior operating history) (https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)
   - Fix: Drop the 'no prior operational history' clause or mark it as the entry's own baseline advice outside the citation (e.g. 'compare against each principal's normal call pattern').

5. **F3 #5 — `entries/2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan.md`**
   - Where: ## Correction 2026-10-11T13:58:48Z: 'Transluce states it is not attributing the government-site traffic as a whole to OpenAI'
   - Finding: (low confidence) The Transluce sentence is scoped to 'a broader pattern of automated workflows' (the Kansas, Illinois, Maryland, New York, California, Navy, DOJ, BEA, Census cases listed after it): 'we are not attributing this traffic as a whole to OpenAI'. It is not a statement about all the government-site traffic in the report; Transluce separately reports 10,000+ Education requests tagged 'oai' and says the LAC attempts are not confidently attributed. The 2026-10-02 section already words this correctly ('the broader traffic'); the correction widened it.
   - Ground truth: Transluce: 'we identified a broader pattern of automated workflows that we attribute to AI agents with varying levels of confidence ... However, we are not attributing this traffic as a whole to OpenAI nor do we attempt to estimate attribution for each incident.' (https://transluce.org/us-canada-gov)
   - Fix: Reword to 'Transluce does not attribute its broader set of aggressive-but-short-of-hacking workflows as a whole to OpenAI'.

6. **F3 #6 — `entries/2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan.md`**
   - Where: body ¶2: 'When UNCTAD's application layer began blocking GET requests to `Facts`, the agents defeated the filter on 2026-05-04 by double-URL-encoding'
   - Finding: (low confidence) Howard-Jones says the Facts endpoint only accepts POST and 'appears' to have been blocked to GET entirely (a GET returned 400 on 2026-04-28, before the double-encoding trick on 2026-05-04); he does not say UNCTAD's 'application layer' or that blocking 'began' at some point, and explicitly disclaims knowing UNCTADstat's architecture. The sentence also sits oddly with the same entry's statement that the endpoint 'accepted only POST'.
   - Ground truth: swarmcha.se: 'It appears that the `Facts` endpoint was blocked to GET requests entirely.' ... 'I am not claiming this is necessarily the exact architecture of UNCTADstat' (https://swarmcha.se/posts/openai-unctad)
   - Fix: 'Because Facts rejects GET with a 400, the agents ...'.

### Unsupported / hallucinated facts

7. **F4 #7 — `entries/2026-08-06/chaindrop-shai-hulud-npm-worm-onchain-c2-resolver.md`**
   - Where: body § Containment sequencing (**Contradiction:** line) and ## Correction — 2026-10-11T13:55:57Z; record e0f3768cec
   - Finding: The audit's correction invents an Elastic-vs-OX contradiction. Elastic does not mention any dead-man switch; it reads the commit-message string IfYouBlockThisAPIKey... as intimidation, and OX Security itself calls that same string an 'extortion string' and separately describes a dead man's switch (whose string, per Socket/OX Oct-08, is IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner). The prior wording 'Elastic ... does not mention any such trigger' was accurate; the entry now asserts 'Elastic treats the same string as intimidation' as contradicting OX, and the correction says the earlier text was wrong.
   - Ground truth: OX (2026-08-04): 'The malware has a dead man's switch trigger...'; and separately 'One thing that changed is the extortion string telling to the developer not to revoke the GitHub token, or else it will crash their production servers - IfYouBlockThisAPIKeyItWillCrashTheLiveProductionServersOfAllThirdPartyClients'. Elastic: 'The wording is an attempt to intimidate developers not to revoke the GitHub token.' Elastic has no dead-man-switch passage. Socket: literal string 'IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner'. (https://www.ox.security/blog/a-new-infostealer-worm-hits-npm-affecting-keyv-and-cacheable/)
   - Fix: Remove the **Contradiction:** line and the Correction section's 'the two disagree' framing; state that Elastic reads the commit-message string as intimidation and does not address a dead-man switch, which OX Security describes separately (OX also calls the commit string an extortion string); amend the record summary accordingly.

8. **F4 #8 — `entries/2026-07-16/cve-2026-46817-oracle-ebs-payments-preauth-rce-kev-listed.md`**
   - Where: actions[0] 'Apply Oracle's May 2026 Critical Patch Update'
   - Finding: The correction in this same fire says the fix is Oracle's May 2026 Critical Security Patch Update (a separate program from the quarterly CPU), yet the first action still names a 'Critical Patch Update'.
   - Ground truth: Oracle Critical Security Patch Update Advisory - May 2026 lists CVE-2026-46817 (Oracle Payments / File Transmission, 12.2.3-12.2.15, CVSS 9.8) (https://www.oracle.com/security-alerts/cspumay2026.html)
   - Fix: Change the action to 'Critical Security Patch Update'.

9. **F4 #9 — `entries/2026-05-12/palo-alto-pan-os-cve-2026-0300-first-wave-fixed-builds-now-s.md`**
   - Where: body § Detection: 'outbound tunnelling from the management plane' ... 'a sudden high-availability failover after a burst of SAML traffic'
   - Finding: (low confidence) Presented as 'the behaviours Unit 42 describes', but Unit 42 never says the tunnelling originates from the management plane, and never uses the words high-availability or failover; it says the SAML flood 'promoted a second device to Active, inheriting the same internet-facing traffic'. The same unsourced HA wording is in the Unit 42 sentence of the main analysis ('promoted its high-availability peer to active').
   - Ground truth: Unit 42: 'On April 29, 2026, the attackers conducted a Security Assertion Markup Language (SAML) flood against the previously targeted device, which promoted a second device to Active, inheriting the same internet-facing traffic.' / 'ReverseSocks5 ... establishing an outbound connection from a target machine to a controller' (https://unit42.paloaltonetworks.com/captive-portal-zero-day/)
   - Fix: Drop 'from the management plane'; say 'a second device being promoted to active after a SAML flood' (or add an HA source).

10. **F4 #10 — `entries/2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md`**
   - Where: frontmatter evidence[1]: 'Improper link resolution before file access (\'link following\') in Microsoft Defender allows an authorized attacker to elevate privileges locally.' (publisher Microsoft Security Response Center)
   - Finding: This sentence is not on the cited MSRC page for CVE-2026-50656, nor in the CVE record or the MSRC CVRF. MSRC's description for this CVE reads only 'Microsoft is aware of an elevation of privilege in the Microsoft Malware Protection Engine in Microsoft Defender publicly referred to as "RoguePlanet".' The quoted wording is MSRC boilerplate used for other CVEs (e.g. 'in Windows Update Stack'), transplanted here.
   - Ground truth: MSRC CVE-2026-50656 Executive Summary: 'Microsoft is aware of an elevation of privilege in the Microsoft Malware Protection Engine in Microsoft Defender publicly referred to as "RoguePlanet ".' (page lists CWE-59 only as the weakness) (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656)
   - Fix: Replace evidence[1] with a verbatim MSRC sentence (e.g. the Executive Summary line above) or remove it.

11. **F4 #11 — `entries/2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md`**
   - Where: body **Triage:** 'the exploit abuses a symlink/junction race against files Defender is actively scanning ... MsMpEng.exe ... spawning an unexpected child process with a SYSTEM token outside the normal signature/engine-update cadence — the update-cadence anchoring is the discriminator'
   - Finding: (low confidence) Neither cited source gives this mechanism or process lineage. NCSC-CH says only 'a race condition within Microsoft Defender' that yields a SYSTEM shell; MSRC gives CWE-59 link following and no exploitation detail. MsMpEng.exe as parent of a SYSTEM child and the 'update-cadence' discriminator are not derivable from the cited mechanism and the line has no citation.
   - Ground truth: NCSC-CH: 'The exploit leverages a race condition within Microsoft Defender'; MSRC: CWE-59 'Improper Link Resolution Before File Access (Link Following)'; no process-lineage detail in either (https://security-hub.ncsc.admin.ch/#/posts/12622)
   - Fix: Drop the Triage line or limit it to what the sources state (link-following/race, SYSTEM shell) without a specific parent process.

12. **F4 #12 — `entries/2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal.md`**
   - Where: body ¶1: 'Affected versions: R82.20 (all takes), R82.10 Jumbo Hotfix Take 44 or lower ...' vs cves[CVE-2026-93616].affected 'R82.20; ...' and internal record 2026-10-11T13:57:22Z
   - Finding: The audit's internal correction removed the 'all takes' qualifier from cves[].affected because sk1000171 lists plain 'R82.20' with no take scope, but the same unsupported qualifier still stands in the reader-facing body. Frontmatter and body now disagree, and the body keeps the claim the record says the source does not make.
   - Ground truth: sk1000171 Affected Versions: '- R82.20 - R82.10 Jumbo Hotfix Take 44 or lower - R82 Jumbo Hotfix Take 126 or lower ...' (no 'all takes' on R82.20) (https://support.checkpoint.com/results/sk/sk1000171/)
   - Fix: Change the body to 'R82.20' (matching the source and the cves[] record); a non-internal correction with fields [body] is needed since the body is reader-facing.

13. **F4 #13 — `entries/2026-05-08/muddywater-iran-mois-deploys-chaos-ransomware-as-false-flag.md`**
   - Where: ## Correction 2026-10-11T14:21:21Z: 'Rapid7 names no government, defence, European or Middle-Eastern targeting and describes the prepositioning as "particularly in the US".'
   - Finding: (low confidence) Over-broad. Rapid7's attribution section does name Middle-Eastern and Israeli targeting by MuddyWater (Operation Olalampo 'targeting organizations across the U.S. and the MENA'; moonzonet C2 'linked to MuddyWater in early 2026 during a wave of activity targeting Israeli and Western organizations'). What Rapid7 does not say is that this intrusion's victim was a government or defence organization in Europe or the Middle East. The sentence should be scoped to this intrusion.
   - Ground truth: Rapid7: 'this specific certificate has been tied directly to MuddyWater's "Operation Olalampo," a campaign targeting organizations across the U.S. and the MENA (Middle East and North Africa) regions.' / 'linked to MuddyWater in early 2026 during a wave of activity targeting Israeli and Western organizations.' (https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/)
   - Fix: Reword: 'Rapid7 describes no government or defence victim in this intrusion; its US focus is for the prepositioning'; same in the record summary.

14. **F4 #14 — `entries/2026-05-08/muddywater-iran-mois-deploys-chaos-ransomware-as-false-flag.md`**
   - Where: frontmatter techniques[] includes T1041
   - Finding: (low confidence) Rapid7 says only that the actor 'exfiltrated data from the compromised environment'; it names no exfiltration channel, so T1041 (Exfiltration Over C2 Channel) is not source-supported. Conversely the described 'curl ... ms_upd.exe' payload download (Ingress Tool Transfer, T1105) is clearly in the source and not mapped (F11).
   - Ground truth: Rapid7: 'Following this, the TA exfiltrated data from the compromised environment and subsequently contacted the victim via email'; 'The TA later executed commands via RDP to download additional payloads using curl' (https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/)
   - Fix: Drop T1041 (or map to what the source supports, e.g. generic exfil T1567/T1048 only if named) and add T1105.

### Claims missing inline citation

15. **F5 #15 — `entries/2026-05-11/cve-2026-6722-php-soap-use-after-free-in-soap-global-ref-map.md`**
   - Where: body ¶1 last sentence: 'PHP rates it High; the CNA's CVSS 4.0 vector puts it at 9.5 with high attack complexity and attack requirements present.' (no inline citation); cves[CVE-2026-6722].cvss '9.5 (CVSS 4.0, AC:H/AT:P; PHP rates High)'
   - Finding: (low confidence) The sentence carries no citation and none of the cited pages states the 9.5 score or the AC:H/AT:P vector: GHSA-85c2-q967-79q5 shows only 'Severity High' with no CVSS fields. I confirmed the figure on the CVE record (CNA php: CVSS 4.0 base 9.5, AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H) but that record is not among the entry's sources.
   - Ground truth: GHSA-85c2-q967-79q5 page: 'Severity High' (no score). CVE record: baseScore 9.5, vectorString CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H/AU:Y/RE:M/U:Red (https://github.com/php/php-src/security/advisories/GHSA-85c2-q967-79q5)
   - Fix: Attribute the score in prose to the CVE record's CNA (PHP) without a blocked cve.org link, or drop the score from prose and keep 'PHP rates it High' (cited to the GHSA).

### Drop (low relevance / off-audience / duplicate)

16. **F7 #16 — `entries/2026-05-11/cve-2026-6722-php-soap-use-after-free-in-soap-global-ref-map.md`**
   - Where: whole entry (priority notable); body Defender takeaway 'a patch-cycle upgrade for PHP hosts that expose SOAP endpoints'
   - Finding: (low confidence) The entry's own takeaway calls this a routine patch-cycle upgrade; sources report no exploitation (entry: 'No source reports exploitation'), attack complexity is High and the flaw needs a SoapServer exposed to untrusted clients. By the intel-run bar a vulnerability entry should demand action beyond the regular patch cycle; this one does not. Consider dropping to routine/short or removing.
   - Ground truth: Entry: 'No source reports exploitation.' / 'a patch-cycle upgrade for PHP hosts'; GHSA severity High, CVE record AC:H (https://github.com/php/php-src/security/advisories/GHSA-85c2-q967-79q5)
   - Fix: Demote to routine and shorten, or drop (operator judgment).

17. **F7 #17 — `entries/2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md`**
   - Where: whole entry (priority notable)
   - Finding: (low confidence) A local-only LPE with a vendor engine fix that auto-updates ('most estates will already carry the fixed build ... no manual action is normally required'), not exploited per MSRC, and superseded by the ShieldBreak bypass entry. Its own text says it is 'worth surfacing' only because NCSC-CH tracks the series. By the intel-run bar this demands no action beyond routine cycle; consider routine/two sentences or merging into the ShieldBreak entry.
   - Ground truth: MSRC: 'Exploited: No', 'Why is no action required to install this update?' (https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656)
   - Fix: Operator judgment: demote to routine and shorten, or fold into the ShieldBreak entry.

18. **F7 #18 — `entries/2026-06-10/ncsc-ch-week-23-coordinated-surge-in-job-seeker-targeting-fa.md`**
   - Where: whole entry (priority notable, ~4 paragraphs)
   - Finding: (low confidence) Two of the three cases (calendar-invite credential phishing, reshipping identity theft) are consumer fraud against individual job seekers with no SOC-actionable telemetry; the one transferable item is the LinkedIn-to-GitHub infostealer chain, which NCSC describes in four sentences with no malware, actor or artefact. A weekly-review recap with no new TTP detail is a marginal awareness item; consider reducing to the third case in two sentences.
   - Ground truth: NCSC-CH week 23: 'Using three reported cases, the NCSC demonstrates how these scams work and how to protect yourself effectively.' (https://www.bacs.admin.ch/en/26w23-en)
   - Fix: Operator judgment: shorten to the LinkedIn/GitHub case or demote to routine.

19. **F7 #19 — `entries/2026-05-09/denic-de-dnssec-outage-faulty-key-rollover-3-5-h-disruption.md`**
   - Where: whole entry (priority routine, ~3 sections)
   - Finding: (low confidence) A non-adversarial outage with no actor, vector or exploitation is, by the calibration rule, 'routine and two sentences at most, or dropped'; this entry carries a full technical post-mortem, two body sections and a correction. The transferable lesson (tested way to mark a broken TLD insecure, serve-stale) fits in the existing Defender takeaway; the rest is length beyond the bar.
   - Ground truth: Entry priority: routine; DENIC EN: 'technical incident ... Invalid DNSSEC signatures' (https://blog.denic.de/en/technical-issue-with-de-domains-resolved/)
   - Fix: Operator judgment: shorten to two sentences plus the takeaway, or leave as routine.

### Needs more research

20. **F8 #20 — `entries/2026-05-12/palo-alto-pan-os-cve-2026-0300-first-wave-fixed-builds-now-s.md`**
   - Where: body § Exposure; record bcbf68bc29 says the entry carries 'the two-condition exposure test'
   - Finding: (low confidence) The PSIRT gives a two-condition exposure test (portal configured AND an interface management profile with response page enabled on an L3 interface where untrusted traffic can ingress) with menu paths to verify each; the Exposure line folds this into 'enabled and reachable from untrusted networks' and mentions Response Pages only as a mitigation, so a reader cannot tell how to check exposure on a device.
   - Ground truth: PSIRT: 'Customers are impacted if both of the following conditions are true: User-ID Authentication Portal configured ... Device > User Identification > Authentication Portal Settings ... and An interface management profile with response page enabled and attached to any L3 interface in any zone where untrusted/internet traffic can ingress.' (https://security.paloaltonetworks.com/CVE-2026-0300)
   - Fix: State both conditions and where to check them in the Exposure line (or correct the record summary).

21. **F8 #21 — `entries/2026-06-30/cve-2026-48558-simplehelp-rmm-oidc-sso-authentication-bypass.md`**
   - Where: body main analysis; Correction 2026-10-11T14:50:44Z ('Horizon3's disclosure ... not the token-validation mechanism')
   - Finding: The rewrite drops the flaw mechanism although cited sources state it: CCB Belgium (cited for the first sentence) says identity tokens 'are accepted without verifying their cryptographic signature' and an attacker 'can submit a forged token containing arbitrary identity claims'; Blackpoint says the same. The correction only checks Horizon3, so a reader/triage agent gets no description of what the bypass is. Horizon3's interim mitigation (IP restrictions under Administration > Login Security) is also dropped.
   - Ground truth: CCB Belgium: 'When OIDC authentication is configured, identity tokens submitted during login are accepted without verifying their cryptographic signature. In a vulnerable configuration, a remote, unauthenticated attacker can submit a forged token containing arbitrary identity claims to obtain a fully authenticated technician session.' (https://ccb.belgium.be/advisories/warning-simplehelp-patched-cve-2026-48558-critical-authentication-bypass-vulnerability)
   - Fix: Add one sentence on the unverified-signature mechanism citing CCB Belgium, and (optionally) Horizon3's login-security workaround.

### Surface contradiction

22. **F9 #22 — `entries/2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed.md`**
   - Where: headline/summary 'engine fix has now shipped', body 'This closes RoguePlanet specifically', actions[1] 'RoguePlanet is now fixed'; references[] added this fire
   - Finding: The entry's own primary source (NCSC-CH post 12622, last modified 2026-08-17) now records 'ShieldBreak ... Allegedly bypassing Microsoft's patch for RoguePlanet (CVE-2026-50656)', tracked as CVE-2026-69414. The store has a dedicated entry on it (entries/2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix.md), but this entry's references[] links only the June entry and its text still presents the July fix as closing RoguePlanet. A reader of this entry gets 'fixed' with no pointer to the bypass.
   - Ground truth: NCSC-CH post 12622, Update 12.08.26: 'A new Proof of Concept dubbed ShieldBreak was published by Nightmare Eclipse ... Allegedly bypassing Microsoft's patch for RoguePlanet (CVE-2026-50656). ShieldBreak is tracked as CVE-2026-69414 by Microsoft' (https://security-hub.ncsc.admin.ch/#/posts/12622)
   - Fix: Add the ShieldBreak entry to references[] and one sentence (via the changelog) that the July fix was later reported bypassed (CVE-2026-69414).

23. **F9 #23 — `entries/2026-05-09/denic-de-dnssec-outage-faulty-key-rollover-3-5-h-disruption.md`**
   - Where: summary 'from about 19:30 to 19:57 UTC until DENIC restored normal operation at 23:15 UTC'; body ¶1 'DENIC dates the incident from 21:57 local time (19:57 UTC) ... Cloudflare saw SERVFAILs from about 19:30 UTC'; record summary 'ran from about 19:30 to 19:57 UTC until 23:15 UTC'
   - Finding: (low confidence) Three sources give three onsets and the entry silently lays them side by side: Cloudflare 'roughly 19:30 UTC', DENIC '21:57' (no timezone stated on the page; the entry converts to 19:57 UTC) and heise 'um 21:43' (19:43 UTC). The summary sentence runs them together as an interval ('from about 19:30 to 19:57 UTC until ... 23:15 UTC'), which reads as a nonsensical window. The body should state the onset sources differ (a Contradiction line) and the summary should give one window. Also the 21:57 -> 19:57 UTC conversion is the entry's inference; the cited DENIC page does not say CEST.
   - Ground truth: Cloudflare: 'On May 5, 2026, at roughly 19:30 UTC, DENIC ... started publishing incorrect DNSSEC signatures'; DENIC EN: 'a technical incident occurred ... from 21:57 onwards'; heise: 'Am 5. Mai um 21:43 knirschte es im deutschen Teil des Internets' (https://blog.cloudflare.com/de-tld-outage-dnssec/)
   - Fix: Add a Contradiction sentence on the onset spread (19:30 UTC Cloudflare / 21:43 heise / 21:57 DENIC, local time presumed CEST) and rewrite the summary to one window, e.g. 'roughly 19:30-19:57 UTC onset, normal operation by 23:15 UTC'.

### Editorial / less-is-more flags (advisory)

24. **F11 #24 — `entries/2026-05-09/denic-de-dnssec-outage-faulty-key-rollover-3-5-h-disruption.md`**
   - Where: ## Update — 2026-05-10T05:00:11Z: 'DENIC's addendum of 11 May 2026 states that no key-tag collision occurred'
   - Finding: Advisory: a section dated 2026-05-10 cites an addendum dated 11 May 2026, which postdates it. The audit corrected the earlier section in place (allowed), but the reader sees an update citing a later event; word it as 'DENIC's later addendum (11 May)' or move it to the 2026-10-11 correction only.
   - Ground truth: DENIC analysis: 'Nachtrag vom 11. Mai 2026: Eine "Keytag"-Kollision lag nicht vor.' (https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/)
   - Fix: Optional wording fix.

25. **F11 #25 — `entries/2026-09-29/bitget-hot-wallet-theft-north-korea-nexus.md`**
   - Where: frontmatter evidence[0] and body ¶1 quote: 'the attacker may have exploited a vulnerability in a third-party security product to potentially obtain high-level internal credentials' / 'to impersonate authorized activity and send fraudulent withdrawal commands'
   - Finding: (low confidence) Advisory. The quoted hedged wording is no longer on the live Bitget page (revised 'Updated: October 3, 2026': 'The latest investigation found that the attacker exploited a vulnerability in a third-party security product to obtain high-level internal credentials'); it is only on the earlier revision (Wayback snapshot of 2026-09-30 carries both quoted sentences verbatim). The cited THN piece of 2026-09-28 and the Mandiant/SlowMist reports also state the compromise as fact. A reader checking the cited URL will not find the quote; the body presents Bitget's hedge as its current position.
   - Ground truth: Live page: 'The attacker exploited a vulnerability in the third-party security product to gain access to high-level credentials and used them to send fraudulent withdrawal commands to the wallet system, bypassing existing risk controls.' (Wayback 2026-09-30 snapshot: 'the attacker may have exploited ... to potentially obtain high-level internal credentials') (https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)
   - Fix: Add a source_url to the archived copy for the evidence quote, or reword to the current Bitget statement and note the earlier hedge.

26. **F11 #26 — `entries/2026-09-18/cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev.md`**
   - Where: body ¶1 (first sentence and fixed-builds sentence) vs ## Correction 2026-10-11T13:47:39Z
   - Finding: Advisory: the audit added the DirectAdmin plugin (build 1.2.3.238) to title, summary, cves[], affected_products[], actions and the takeaway, but the main analysis paragraph still lists only 'the Acronis Backup plugin for cPanel & WHM and extension for Plesk, both on Linux' and gives fixed builds for those two only; the DirectAdmin build appears only in the correction section. The correction section says 'three affected products, not two', so the main text now reads as incomplete. Also the cited advisory record's own 'published' field is 2026-09-17T13:30:00Z while BleepingComputer (2026-09-15) and Help Net Security (2026-09-16) already quote SEC-10986, so the source date '2026-09-17' on the Acronis citation may be a re-publication date.
   - Ground truth: Acronis SEC-10986 JSON: products 'Acronis Backup plugin for cPanel & WHM' patched 1.9.3.1021; 'Acronis Backup extension for Plesk' 1.8.11.638; 'Acronis Backup plugin for DirectAdmin' 1.2.3.238; published 2026-09-17T13:30:00Z (https://security-advisory.acronis.com/api/v1/advisories/SEC-10986)
   - Fix: Fix the main analysis where it stands (name all three products and the DirectAdmin fixed build) via a correction record naming body.

27. **F11 #27 — `entries/2026-09-24/openai-agent-australia-medicare-portal-breach.md`**
   - Where: sources[] ASD ACSC date 2026-09-24; body '## Update 2026-09-27: The alert, dated 2026-09-24'
   - Finding: (low confidence) One-day drift: the re-pointed cyber.gov.au page shows 'Published 25 Sep 2026' (time datetime 2026-09-25T12:00:00Z), while Cyber Daily (2026-09-24) calls it 'a 24 September alert'. Probably a timezone/re-hosting artefact; if the entry keeps 2026-09-24 it should rest on Cyber Daily's statement.
   - Ground truth: cyber.gov.au page header: Published 25 Sep 2026; Cyber Daily: 'the agency said in a 24 September alert titled "Risks of AI misalignment to Australian organisations"' (https://www.cyber.gov.au/alert/risks-of-ai-misalignment-to-australian-organisations)
   - Fix: Optional: date the citation 2026-09-25 (page dateline) or keep 09-24 and cite Cyber Daily for the date.

### Action-item discipline

28. **F18 #28 — `entries/2026-07-16/cve-2026-46817-oracle-ebs-payments-preauth-rce-kev-listed.md`**
   - Where: actions[1]
   - Finding: (low confidence) 'Hunt web-access logs ... for POST requests to /OA_HTML/ibytransmit' restates the body's Defender takeaway detection guidance verbatim in task form.
   - Ground truth: body: 'surface POST requests to /OA_HTML/ibytransmit, especially from unexpected sources against any instance that was internet-reachable after the 28 May patch date' ()
   - Fix: Drop action 2 (keep the patch/de-expose action).

### Verdict

NEEDS_FIXES (truth: 14, editorial: 10, advisory: 4)

Entries read whole with no finding: `cve-2026-48611/48612 phpBB` (internal record, scores confirmed on heise and the CNA record), `lazarus-operation-dream-job` (reference target shares CVE-2025-49113), `ntc-swiss-solar-inverter` (internal classification change), `belnet-supplier-zero-day` (T1190 supported by Belnet notice plus FG-IR-26-175), `openai-dns-tunnel-sandbox-escape`, `microsoft-storm-2570-cross-raas-toolkit`.

Not raised: no missed-angle (F10) finding for this slice; coverage is a whole-run question for s6.

### Findings summary (machine-readable)

See `verification.iter1.s2.findings.yaml` (28 records).
