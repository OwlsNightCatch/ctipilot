**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-01T04:40:22Z · ended_at=2026-10-01T05:12:10Z · duration_seconds=1908

## Verification report — 2026-09-30T0639Z-audit (iteration 4, slice s1)

Scope: 18 entries, 438 ledger claims, every claim has a verdict row in `verification.iter4.s1.claims.yaml` (429 ok, 8 F3, 1 F4). Every cited page was fetched this pass (extract / pdf / raw HTML / ncsc-csh; cisa.gov alerts through WebFetch; the Computing UK page through the jina rung after a 403; Cybersecurity News is behind a CAPTCHA and is cited by no body claim). The cyber.gov.au ACSC alert returned a block page on the first try and the full alert on the retry.

### Citation does not support the claim
- #1 `2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware`, this run's Correction: "The Run-key check in the triage line rests on NCSC's description of the malware's persistence, not on its detection guidance." and "its detection guidance is connections to the listed legitimate services ...". NCSC's investigation guidance has a "Check for persistence" section: "The registry path HKCU \ Software \ Microsoft \ Windows \ CurrentVersion \ Run contains programs configured to run automatically ... run the powershell command: reg query ...". The Run-key check is NCSC detection guidance. Remediation introduced a statement the source contradicts (claims 1521f0340a, 5b65665161). Drop both sentences.
- #2 same entry, summary "disables Defender via exclusions": NCSC "adds exclusions to Microsoft Defender antivirus in an attempt to evade detection" (low confidence; claim 8f0f34a24e).
- #3 `2026-05-18/thorchain-...` body and Correction: TSSHOCK shows "missing or malformed zero-knowledge proofs" let a participant extract key shards. Verichains lists an ambiguous Fiat-Shamir encoding, reduced dlnproof iterations and a 256-bit challenge over a composite-order group: weak or insecurely optimised proofs, not missing ones (low confidence; claim 9633711afa).
- #4 `2026-07-13/servicenow-...` Update paragraph: the Searchlight eval/new Function quote is why eval is forbidden in the sandbox; the chain gets Function through Class.create.constructor during gs.include() (low confidence).
- #5 `2026-05-08/qilin-...-die-linke`: "told Heise that it had not yet definitively clarified ..." is Heise's own-voice sentence, not attributed to Ehling (low confidence; claim 6bd148a223).
- #6 `2026-09-18/brevo-...`: "Brevo's post-mortem does not mention a separate SSO-hijacking incident" is cited to BleepingComputer, which does not say that; the Brevo write-up (uncited for this clause) confirms it (low confidence; claim 1f9fc13586).
- #7 `2026-09-23/austria-nisg-...` Correction: "not a criminal offence" is not in heise, which says only "strafbar" and separately that the district authority imposes penalties (low confidence; claim d425b5802b).
- #8 `2026-09-23/gambit-...`: "Compromise ranged from partial to full" at the four named companies; Gambit says "some level of access" (low confidence; claim 545e82205e).

### Unsupported / hallucinated facts
- #9 `2026-05-10/sophos-beagle-...` Detection line: MSI "or, in the earlier wave, by a VBScript". Sophos and Malwarebytes describe the same archive and Sophos writes "As reported by MalwareBytes in their coverage of this attack"; no source describes two waves or two delivery methods (low confidence).
- #10 `2026-09-29/kaspersky-payload-...` Triage: a GPO disabling the local Administrator account or Windows Firewall "has essentially no benign justification". Not in Kaspersky; "Accounts: Administrator account status" is an ordinary Security Options policy, so the discriminator misleads triage (low confidence; claim 0e0da45a7b).

### Analytical-link-as-fact
- #11 `2026-09-19/waterplum-...`: entities still lists `actor:purpledelta` while this run's Correction says the advisory never uses a vendor alias for the IT-worker scheme and the body sentence was removed. None of the advisory PDF, BfV, The Record or heise contains PurpleDelta, Jasper Sleet, UNC5267, Wagemole or Famous Chollima. Remove the key.

### Claims missing inline citation
- #12 `2026-09-17/cve-2026-58704-...` Defender takeaway: "TechCrunch notes this class of modem bug is not uncommonly abused by commercial surveillance vendors ..." has no link (low confidence; claim d7adc1a36e).

### Drop (low relevance / off-audience / duplicate)
- #13 `2026-06-09/cve-2026-50751-...`: a second live entry exists for the same CVE, same day and run (`check-point-ikev1-vpn-authentication-bypass-cve-2026-50751`, notable deep dive), and this run's text now sends the reader to it. Fold candidate under one-entry-per-finding (low confidence; pre-existing structure).

### Needs more research
- #14 `2026-09-19/waterplum-...`: the 30,000-device and USD 10.7M figures are shown without the advisory's period "From around December 2025 through July 2026" (also in The Record) (low confidence).
- #15 `2026-05-28/nx-console-...`: no Exposure line although the postmortem gives "18.95.0 exactly", the 2026-05-18 12:30-13:09 UTC window, 28 Marketplace installs, 41 Open VSX downloads and about 6,000 activations; the 2.2 million figure is the extension's install base (low confidence).
- #16 `2026-09-29/kaspersky-payload-...`: takeaway omits the detection telemetry Kaspersky specifies (DS Access auditing, events 5137/5136/5141, gPLink on the domain root, SYSVOL integrity monitoring, "missing 5136 events") (low confidence).

### Surface contradiction
- #17 `2026-05-18/thorchain-...`: (a) takeaway repeats CryptoTimes' "CGGMP21 ... stronger guarantees" while the cited Verichains page lists CGGMP21 implementations among the vulnerable ones; (b) the cited CryptoTimes article says THORChain's Incident Update #1 "confirmed the malicious-node vector", yet the Correction frames the node only as CryptoTimes' working theory (low confidence).
- #18 `2026-09-24/shinyhunters-...` Update 2026-09-29: "coercive rather than financial" omits that the cited Nextgov/FCW piece has the group calling it "a marketing campaign" and "not a threat" (low confidence).

### Editorial / less-is-more flags (advisory)
- #19 Rendered record summaries narrate the rating and mapping ("the entry gains its source rating and ATT&CK mapping": Sophos, THORChain, Nx Console, Check Point, LiteSpeed), the field work (Die Linke: "The summary and correction now give ...") and the pipeline ("narrated the pipeline's own tracking of the actors": WaterPlum).
- #20 `2026-09-18/gyazo-...` Correction: "The leaked image IDs protect captures ..." reads backwards; THN: the link is the only protection and the IDs make it unguessable.
- #21 `2026-05-28/nx-console-...` Correction: KEV's `knownRansomwareCampaignUse: Known` does not establish that exposed credentials "are in ransomware operators' hands" (low confidence).
- #22 `affected_products` empty or absent on Check Point, LiteSpeed and Nx Console although the sources name the products (legacy-format gap).

### Prior-iteration deltas walked (all 32 items)
Confirmed against the fetched sources: Die Linke party statement (27 March, German; facts as cited, Heise/BleepingComputer/The Record cited only for what they add; sourcing note corrected); OpenAI-Australia (cyber.gov.au alert primary, quotes verbatim, Cyber Daily only for "High Alert/Act Quickly" and its own first-person wording); CHOSEN BRICK wipe sentence, delivery paragraph (every sentence matches "Delivery and exploitation", cited) and Correction coverage of geography, screen capture and wiping; Pixel (title, headline, summary attribute the exploitation wording to TechCrunch, KEV the only unhedged signal; Google bulletin has no exploitation note); Check Point (each clause cited to the source that carries it; one confirmed Qilin case and the medium-confidence actor assessment both stated with their confidence; Exposure/Detection/takeaway lines match Check Point and NCSC-CH 12615); Austria KAIO (undated in body, Correction and sources[]); Flink (10,000 given as heise's customers-in-the-Netherlands figure; shortened text accurate and cited); WaterPlum (BeaverTail wording and the Restricted Mode / tasks.json / command-string controls match section 4(3)); Gyazo (X token and Google SSO email as Helpfeel lists them; shortened text accurate); THORChain (title and headline carry the hedge; takeaway drawn from CryptoTimes); Sophos (T1547.001 supported and active; Detection and takeaway lines on Sophos and Malwarebytes, no file names); Nx Console (three entity keys exist and are supported; takeaway from the postmortem); LiteSpeed (Exposure and takeaway match the advisory); ServiceNow (Contradiction line states both sides cited, no "at disclosure" dating; Guarded Script sentences match KB3137947); Brevo (Exposure line matches the write-up); ShinyHunters (no rating digit; the arrested suspect is no longer named); Kaspersky (name collision stated with Kaspersky and Ransomware.live both cited, no identity implied, `actor:payload-ransomware` left unlinked; handled, no finding). The new defect from a remediation is #1.

### Verdict
NEEDS_FIXES (truth: 11, editorial: 7, advisory: 4)

### Findings summary (machine-readable)
```yaml
- code: F3
  category: claim-not-supported
  section: 2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware
  item: 'Correction (this run): "The Run-key check in the triage line rests on NCSC''s description of the malware''s persistence, not on its detection guidance." and "its detection guidance is connections to the listed legitimate services where they are not expected as part of normal business" (claims 1521f0340a, 5b65665161)'
  url_or_quote: https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists
  summary: 'The NCSC advisory has a "Check for persistence" section under its investigation guidance: "The registry path HKCU \ Software \ Microsoft \ Windows \ CurrentVersion \ Run contains programs configured to run automatically when the current user logs in ... run the powershell command: reg query HKCU \ Software \ Microsoft \ Windows \ CurrentVersion \ Run", plus "searching available logging for the IOCs provided". The Run-key check IS NCSC detection guidance, so the Correction asserts the opposite of the source. Drop both sentences, or say NCSC lists the Run-key check and the network-connection check as separate steps and does not pair them as one discriminator.'
- code: F3
  category: claim-not-supported
  section: 2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware
  item: 'summary: "the malware persists via a registry Run key, disables Defender via exclusions" (claim 8f0f34a24e)'
  url_or_quote: https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists
  summary: '(low confidence) NCSC: "CHOSEN BRICK adds exclusions to Microsoft Defender antivirus in an attempt to evade detection (T1685)". Exclusions do not disable Defender; the body says "adds Microsoft Defender exclusions to evade detection". Align the summary with the body (phrase unchanged from the published version, but the summary was edited this run).'
- code: F3
  category: claim-not-supported
  section: 2026-05-18/thorchain-gg20-threshold-signature-scheme-vault-drain-11m-ac
  item: 'body and Correction: Fireblocks'' CVE-2023-33241 and Verichains'' TSSHOCK "showed that missing or malformed zero-knowledge proofs in GG18/GG20 threshold signing let a malicious participant extract other parties'' key shards" / "both show how a malicious participant can extract key shards when zero-knowledge proofs are missing or malformed" (claims 9633711afa, 0cdb86b21c)'
  url_or_quote: https://www.verichains.io/tsshock/
  summary: '(low confidence) Fits Fireblocks (Paillier modulus not proven biprime, "using a suitable ZK proof"). Verichains describes three different weaknesses: an ambiguous encoding in the Fiat-Shamir transcript ("-shuffle"), a reduced number of dlnproof iterations ("c-guess"), and a 256-bit challenge over a composite-order group ("c-split"); the proofs exist but are weak or insecurely optimised, not "missing or malformed". Say "weak or insecurely implemented zero-knowledge proofs" for TSSHOCK.'
- code: F3
  category: claim-not-supported
  section: 2026-07-13/servicenow-ai-platform-sandbox-escape-cve-2026-6875
  item: 'Update 2026-07-21 paragraph rewritten this run: "a chain Searchlight Cyber demonstrated where ''running any code via eval or new Function will run free from the constraints of the additional sandbox''"'
  url_or_quote: https://slcyber.io/research-center/smashing-the-servicenow-sandbox-pre-authentication-rce/
  summary: '(low confidence) Searchlight says that line to explain why eval and new Function are forbidden inside the script sandbox ("eval would be a trivial sandbox bypass, which is why it''s forbidden"). Its chain does not call eval: it obtains the Function constructor through Class.create.constructor and runs it during a gs.include() evaluation. The paraphrase makes eval/new Function the demonstrated route. The body takeaway describes the gs.include() route correctly; reword the Update sentence to match.'
- code: F3
  category: claim-not-supported
  section: 2026-05-08/qilin-ransomware-hits-die-linke-germany-1-5-tb-claimed-dpa-n
  item: 'body: "The party''s federal managing director told Heise that it had not yet definitively clarified which internal data had been compromised" (claim 6bd148a223)'
  url_or_quote: https://www.heise.de/en/news/Qilin-Left-Party-reports-Russian-ransomware-attack-11227232.html
  summary: '(low confidence) The Heise page states this in its own voice ("The party has filed a criminal complaint due to the incident; it has not yet been definitively clarified which internal data has been compromised") and attributes only the Qilin quote and the Qilin/offline remarks to Ehling. The party''s own statement says the aim is to publish data and "lässt sich nicht beurteilen". Attribute the sentence to Heise''s reporting, not to the managing director telling Heise.'
- code: F3
  category: claim-not-supported
  section: 2026-09-18/brevo-cloudflare-worker-clickfix-supply-chain
  item: 'body: "Brevo''s post-mortem does not mention a separate SSO-hijacking incident it disclosed on 2026-09-10 ... and BleepingComputer states Brevo did not respond" cited to BleepingComputer (claim 1f9fc13586)'
  url_or_quote: https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/
  summary: '(low confidence) BleepingComputer carries the 10 September SSO incident, Trezor and the unanswered question, but never says the post-mortem omits it. The omission is true of the Brevo write-up (I read it: no mention), which is cited elsewhere in the paragraph, not for this clause. Cite the Brevo write-up for the first half.'
- code: F3
  category: claim-not-supported
  section: 2026-09-23/austria-nisg-2026-bcs-transposition
  item: 'Correction (this run): "heise''s ''strafbar'' for obstructing the BCS scans means punishable, with penalties imposed by the district administrative authority, not a criminal offence" (claim d425b5802b)'
  url_or_quote: https://www.heise.de/news/Ab-1-10-Meldepflicht-fuer-IT-Vorfaelle-in-Oesterreich-11462442.html
  summary: '(low confidence) heise says only "Blockade oder Abwehr solcher staatlichen Scans ist ab 1. Oktober strafbar" and, in a separate paragraph on fines for registration, reporting and training breaches ("unter anderem"), "Strafen verhängt nicht das BCS selbst, sondern die jeweils zuständige Bezirksverwaltungsbehörde". It never says the scan-obstruction offence is "not a criminal offence". Keep "punishable" and drop the legal characterisation, or cite the statute.'
- code: F3
  category: claim-not-supported
  section: 2026-09-23/gambit-ai-agent-retail-skimmer-campaign-strix-cairn-hermes
  item: 'body: "Compromise ranged from partial to full at a Fortune 500 hospitality company, a major US airline, a large US industrial-supplies distributor and a US online fashion retailer" (claim 545e82205e)'
  url_or_quote: https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company
  summary: '(low confidence) Gambit: "some level of access to the assets of companies including a Fortune 500 hospitality company, a major US airline, a large private US industrial supplies distributor and a US online fashion retailer"; "at least 27 companies were compromised to varying degrees" is a separate, campaign-wide statement. "Partial to full" for these four is not in the source. Use Gambit''s "some level of access".'
- code: F4
  category: hallucinated-fact
  section: 2026-05-10/sophos-beagle-backdoor-distributed-via-fake-claude-ai-site-u
  item: 'Detection line (this run): "by an MSI installer (Sophos) or, in the earlier wave, by a VBScript run through WScript.exe"'
  url_or_quote: https://www.malwarebytes.com/blog/scams/2026/04/fake-claude-site-installs-malware-that-gives-attackers-access-to-your-computer
  summary: '(low confidence) Sophos and Malwarebytes describe the same archive (Claude-Pro-windows-x64.zip) and Sophos writes "As reported by MalwareBytes in their coverage of this attack". Malwarebytes gives the finer detail (the MSI installs a VBScript dropper that copies the three files into Startup); no source says the delivery differed between two waves. Present the VBScript step as Malwarebytes'' additional detail on the same chain, not as an earlier wave.'
- code: F4
  category: hallucinated-fact
  section: 2026-09-29/kaspersky-payload-gpo-encryptionless-ransomware
  item: 'Triage: "a GPO disabling the local Administrator account or Windows Firewall domain-wide has essentially no benign justification" (claim 0e0da45a7b)'
  url_or_quote: https://securelist.com/tr/payload-ransomware-via-group-policy/121335/
  summary: '(low confidence) Kaspersky makes no such claim; its Security Settings row is "Accounts: Administrator account status | Disabled", an ordinary Security Options policy (Microsoft documents it as a configurable setting and notes the maintenance trade-off). Disabling the built-in Administrator by GPO is a common hardening choice, so the discriminator as written would mislead triage. Narrow it to the combination Kaspersky documents (new domain-root GPO plus ransom-note, banner and wallpaper changes) or drop the clause.'
- code: F13
  category: analytical-link-as-fact
  section: 2026-09-19/waterplum-contagious-interview-joint-advisory-scale
  item: 'entities: ["campaign:contagious-interview", "actor:purpledelta", ...] while this run''s Correction says "The advisory does not name the IT-worker scheme by any vendor alias"'
  url_or_quote: https://www.ic3.gov/CSA/2026/260918.pdf
  summary: 'The run removed the body sentence equating the advisory''s North Korean IT workers with "PurpleDelta / Jasper Sleet / UNC5267 / Wagemole / Famous Chollima", but the frontmatter still links actor:purpledelta (registry summary: Recorded Future''s designation for the IT-worker cluster). None of the four cited pages (advisory PDF, BfV, The Record, heise) contains any of those aliases (grepped). Same unsupported connection, now only in the structured data that feeds the actor page. Remove actor:purpledelta from entities (record fields would need entities).'
- code: F5
  category: missing-citation
  section: 2026-09-17/cve-2026-58704-google-pixel-modem-zero-click-eop
  item: 'Defender takeaway: "TechCrunch notes this class of modem bug is not uncommonly abused by commercial surveillance vendors selling access to governments and law-enforcement agencies" (claim d7adc1a36e)'
  url_or_quote: https://techcrunch.com/2026/09/16/google-says-some-pixel-phone-owners-were-hacked-in-zero-day-attacks/
  summary: '(low confidence) Attributed to TechCrunch with no inline link; TechCrunch says "It''s not uncommon for bugs like this one to be abused by surveillance vendors ... who sell access to their data-stealing software to governments and law enforcement agencies". Add the citation.'
- code: F7
  category: drop
  section: 2026-06-09/cve-2026-50751-check-point-security-gateway-ikev1-vpn-authen
  item: 'Two live entries for one finding: this critical entry and entries/2026-06-09/check-point-ikev1-vpn-authentication-bypass-cve-2026-50751.md (notable deep dive, same CVE, same day, same run); this run''s text now points the reader to the companion for the kill chain, affected trains and hunt concepts'
  url_or_quote: https://blog.checkpoint.com/security/check-point-releases-important-hotfix-for-vulnerabilities-in-deprecated-ikev1-vpn-protocol/
  summary: '(low confidence) Pre-existing structure, declared through references[]; raised earlier by the audit and left to the main agent. Under the one-entry-per-finding rule the companion is a fold candidate (tools/fold_entries.py); at minimum the two should not both stay in the live brief for one CVE.'
- code: F8
  category: needs-more-research
  section: 2026-09-19/waterplum-contagious-interview-joint-advisory-scale
  item: 'headline, summary, title and body present "30,000+ infected devices ... $10.7M" as campaign-wide figures with no period'
  url_or_quote: https://www.ic3.gov/CSA/2026/260918.pdf
  summary: '(low confidence) Advisory section 4(1): "From around December 2025 through July 2026, WaterPlum exploited at least 30,000 PCs in over 100 countries ... exfiltrating at least 1.7 billion JPY"; The Record (cited source) repeats "between December 2025 and July 2026". The executive summary drops the window, the entry copies the executive summary. State the roughly eight-month window.'
- code: F8
  category: needs-more-research
  section: 2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands
  item: 'no **Exposure:** line although the sources give exact version, window and scale'
  url_or_quote: https://nx.dev/blog/nx-console-v18-95-0-postmortem
  summary: '(low confidence) Postmortem: affected version "18.95.0 exactly", exposure window 2026-05-18 12:30-13:09 UTC, VS Code and forks (Cursor), "28 installs" (Microsoft), 41 Open VSX downloads and about 6,000 activations by Nx''s own analytics. The entry gives 2.2 million installs of the extension (not of the bad version) and never states the malicious version''s reach. Add an Exposure line.'
- code: F8
  category: needs-more-research
  section: 2026-09-29/kaspersky-payload-gpo-encryptionless-ransomware
  item: 'Defender takeaway says "enable auditing on GPO creation and linking events (Group Policy Management Console / SYSVOL change auditing)" without the telemetry Kaspersky specifies'
  url_or_quote: https://securelist.com/tr/payload-ransomware-via-group-policy/121335/
  summary: '(low confidence) Kaspersky''s detection section names DS Access "Audit Directory Service Changes" on domain controllers with events 5137 (groupPolicyContainer created), 5136 (gPLink on the domain root or sensitive OUs; gPCMachineExtensionNames/gPCFileSysPath/versionNumber changes) and 5141, SYSVOL file-integrity monitoring, the Group Policy Operational log, and "missing 5136 events" as a sign of direct SYSVOL editing. The entry drops all of it; these are platform artifacts, not IOCs.'
- code: F9
  category: surface-contradiction
  section: 2026-05-18/thorchain-gg20-threshold-signature-scheme-vault-drain-11m-ac
  item: 'Defender takeaway cites CryptoTimes that "newer protocols such as CGGMP21 offer stronger guarantees against malformed-proof attacks"; Correction states the malicious node is only "CryptoTimes'' reported working theory"'
  url_or_quote: https://www.verichains.io/tsshock/
  summary: '(low confidence) (a) Verichains, cited on the same entry, lists CGGMP21 among the schemes whose implementations were vulnerable ("most implementations of GG18, GG20, and CGGMP21, found to be vulnerable"; Taurus multi-party-sig, a CGGMP-21 implementation, fell to -shuffle); the entry repeats CryptoTimes'' reassurance without that contrast. (b) The cited CryptoTimes article says "Incident Update #1 ... confirmed the malicious-node vector", and the related CryptoTimes piece reports THORChain contributors themselves naming a newly churned node and a GG20 TSS leak as the leading theory; the entry presents the node as CryptoTimes'' theory with no mention that the project said it.'
- code: F9
  category: surface-contradiction
  section: 2026-09-24/shinyhunters-fbi-peoplesoft-breach-claim
  item: 'Update 2026-09-29: ShinyHunters "states the intrusion''s motive is coercive rather than financial: it is demanding the FBI retract or amend a May 2026 public advisory"'
  url_or_quote: https://www.nextgov.com/cybersecurity/2026/09/shinyhunters-says-it-wont-publish-fbi-data/416280/
  summary: '(low confidence) The Nextgov/FCW article cited in the same paragraph reports the group''s newer statement: it "never expected compliance", "This was not a threat. It may have been worded like a threat", and called the episode "a marketing campaign". The section reports the earlier demand and the non-publication quote but not this recharacterisation, which contradicts "coercive".'
- code: F11
  category: editorial-advisory
  section: 2026-05-10/sophos-beagle-backdoor-distributed-via-fake-claude-ai-site-u; 2026-05-18/thorchain-gg20-threshold-signature-scheme-vault-drain-11m-ac; 2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands; 2026-06-09/cve-2026-50751-check-point-security-gateway-ikev1-vpn-authen; 2026-06-16/cve-2026-54420-litespeed-cpanel-whm-plugin-symlink-following; 2026-05-08/qilin-ransomware-hits-die-linke-germany-1-5-tb-claimed-dpa-n; 2026-09-19/waterplum-contagious-interview-joint-advisory-scale
  item: 'rendered record summaries carry field and pipeline narration: "the entry gains its source rating and ATT&CK mapping" (five records), "The summary and correction now give the party''s own uncertainty" (Die Linke), "Two phrases narrated the pipeline''s own tracking of the actors" (WaterPlum)'
  url_or_quote: updates[].summary of this run's records
  summary: '(low confidence) Not rating letters or digits, but record-keeping narration in text the changelog shows. State the change a reader can see (what the section says, the sources now cited) and leave the rating and mapping out.'
- code: F11
  category: editorial-advisory
  section: 2026-09-18/gyazo-helpfeel-data-breach-image-upload-rce
  item: 'Correction: "The leaked image IDs protect captures at Gyazo''s default link-only setting."'
  url_or_quote: https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html
  summary: 'Reads as if the leaked IDs protect the captures. THN: "For a capture at the default setting, the link is the only thing protecting it, and the leaked image IDs are the part of the link that makes it unguessable." Reword: the image IDs are the only protection for default-setting captures, which is why the leak matters; "Only me" captures are not reachable by link.'
- code: F11
  category: editorial-advisory
  section: 2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands
  item: 'Correction: "...as used in known ransomware campaigns (CISA KEV catalog), so credentials exposed through either compromise should be treated as in ransomware operators'' hands."'
  url_or_quote: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  summary: '(low confidence) KEV carries knownRansomwareCampaignUse: Known for CVE-2026-48027 and CVE-2026-45321 (verified in the cached feed). That flag does not say exposed credentials reached ransomware operators; the inference is stated as a fact-like instruction. Phrase it as the advisable assumption, or cite Grafana''s extortion by the attackers, which is in the cited Help Net Security page.'
- code: F11
  category: editorial-advisory
  section: 2026-06-09/cve-2026-50751-check-point-security-gateway-ikev1-vpn-authen; 2026-06-16/cve-2026-54420-litespeed-cpanel-whm-plugin-symlink-following; 2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands
  item: 'affected_products is empty (Check Point) or absent (LiteSpeed, Nx Console) on vulnerability entries whose sources name the products'
  url_or_quote: https://blog.checkpoint.com/security/check-point-releases-important-hotfix-for-vulnerabilities-in-deprecated-ikev1-vpn-protocol/
  summary: '(low confidence) Check Point names Remote Access VPN, Mobile Access / SSL VPN and Spark Firewall; LiteSpeed names the LiteSpeed user-end cPanel plugin / WHM plugin; Nx names Nx Console and DAEMON Tools Lite. The product pages are fed from this field. Legacy-format gap; add only if the record is touched again.'
```
