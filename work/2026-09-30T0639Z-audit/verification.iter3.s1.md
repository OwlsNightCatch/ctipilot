**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-09-30T12:43:37Z · ended_at=2026-09-30T13:17:32Z · duration_seconds=2035

## Verification report — 2026-09-30T0639Z-audit (iteration 3, slice s1)

Scope: 18 existing entries (scope.iter1.s1.txt), 376 ledger claims in claims.iter3.s1.yaml, every claim has a verdict row in verification.iter3.s1.claims.yaml (361 ok, 8 F3, 7 F5, 0 unreadable). Post-fix pass: full ledger of the slice read, not a sample. Cached bodies reused where the gate had saved them; all other cited pages fetched this iteration with `fetch_source.py extract` (pdf for the WaterPlum advisory, `ncsc-csh post` for 12615 and 12778, raw HTML for the Gambit embedded table and the Brevo write-up). `check_run.py --pre-verify`: 56 pass, 2 warn (verification block, Die Linke aggregator-only), 0 fail.

### Prior-iteration deltas (iteration 2, slice s1) walked

Confirmed correct after fetching the source: Sophos hedge ("is likely part of an active malvertising campaign") is carried in summary, body and Correction, T1055 gone; THORChain summary sentences each cite the page that carries them (The Record and TRM for the drain, CryptoTimes for the GG20 theory), Verichains dated 2023-08-10 matches the page ("Aug 10, 2023 TSSHOCK has been released"); Nx Console payload sentence split correctly (activation and credential list to the postmortem, "fetched an obfuscated payload" and the exfiltration channels to the GHSA, GitHub reach to Help Net Security), Detection line now rests on the postmortem and GHSA, exposure sentence scoped to Nx Console 18.95.0, no inline T-ids; Check Point evidence[1] is the contiguous NCSC-CH "Observed exploitation linked to Qilin ransomware affiliate.", companion link resolves; ServiceNow no longer calls KB3137947 a hotfix, hosted fix dated April and 2026-07-13 the self-hosted release (BleepingComputer), NCSC-CH cited as resting on news coverage, takeaway leads with `/assessment_thanks.do`; CHOSEN BRICK geography and screen-capture wording match NCSC, no em dashes in the body; Brevo figure stated as Sansec ("more than 100 thousand", public source-code search link) and BleepingComputer ("up to 100,000") each, root cause hedged as Sansec hedges it, action leads with the general plugin check, title 27 words; WaterPlum laptop-farm definition matches the advisory and the transfers are attributed to the actor group; registry `campaign:contagious-interview` summary now reads "reports its scale" (verified in entities/registry.yaml); Austria sector list cited to OTS, "punishable" replaces "criminal offence", ICSG/IDSV sentence matches the KAIO page, main text ~200 words; Gambit: 100-plus sites, admin-pod route, hand-picked victims and the Unit 42 model-choice clause match Gambit and Unit 42; ShinyHunters: the FBI release read directly (dated September 23, 2026, "point of breach is still undetermined--whether a third-party or the FBI's enterprise"), Krebs ("brief statement confirming the hack") vs BleepingComputer/CyberScoop stated as a Contradiction line, one Defender takeaway; Pixel Correction states the TechCrunch dek/lede inconsistency and no longer calls one wording an error; Flink Contradiction line states heise ("insgesamt 100 ETH aufbringen") vs NL Times (company pays 100 ETH) without picking one.

Declines that hold: WaterPlum `actor:purpledelta` (F13): the registry holds a sourced `overlaps-with` edge from `campaign:contagious-interview` to `actor:purpledelta` whose note quotes the advisory's shared-parent assessment, and the alias set includes Famous Chollima; acceptable, no finding. ShinyHunters/ServiceNow append-only record summaries: not raised.

Declines that no longer hold: OpenAI-Australia F6 (ACSC alert now readable, see #12); Flink F7 (record now declares body and is public, see #14); Kaspersky F15 (Ransomware.live ties the Payload group to a Windows/ESXi ransomware family, see #28). Gyazo F7 is re-raised low confidence (#15).

No IOCs, KEV deadlines or Admiralty letters found in reader text of the 18 entries; no em dash in text this run added (the one hit is THORChain's verbatim CryptoTimes quote).

### Citation does not support the claim (F3)
- #1 `2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware`: body: "in at least one sample, this downloaded payload carried the data-wiping functionality already described above" (claim 9de3c5dbc3). (low confidence) NCSC lists wiping (T1485) among Telegram-bot tasking functions and separately says only "In at least one sample, there was functionality for data wiping (T1485)." It does not say the downloaded payload carried it. Narrow to NCSC's wording or drop the 'downloaded payload' link. Source: https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists
- #2 `2026-09-17/cve-2026-58704-google-pixel-modem-zero-click-eop`: headline "...a Pixel modem zero-day it says may be under limited, targeted exploitation" and summary "Google says there are indications it may be under limited, targeted exploitation" (claims cf683593fd, 44cbf83994). (low confidence) The Google bulletin as read carries no exploitation statement and Google's spokesperson did not respond to TechCrunch; the only source is TechCrunch's dek ("The Pixel phone maker said there are indications ..."). The body attributes it correctly to TechCrunch; the headline and summary state it as Google's own words. Attribute to TechCrunch's reporting there too. Source: https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
- #3 `2026-06-09/cve-2026-50751-check-point-security-gateway-ikev1-vpn-authen`: summary: "NCSC-CH flagged it as actively exploited and CISA added it to KEV (Check Point, 2026-06-08)." (claim f6ff2ecbc1). (low confidence) The trailing citation terminates the NCSC-CH and KEV clause, but the Check Point blog mentions neither. NCSC-CH is post 12615, KEV is the CISA feed (both already in sources[]). Source: https://blog.checkpoint.com/security/check-point-releases-important-hotfix-for-vulnerabilities-in-deprecated-ikev1-vpn-protocol/
- #4 `2026-09-23/austria-nisg-2026-bcs-transposition`: sources[] date 2026-09-30 and labels "[Kanton Bern KAIO, 2026-09-30]" in the closing sentence and the Correction (claims 3713ea1366, 360af5dd74). (low confidence) 2026-09-30 is the retrieval date: the page has no dateline (the extract metadata date equals the fetch date). Content is correct (ICSG and IDSV in force 1 November 2026, reporting platform with the IDSV). Drop the date from the label and leave sources[].date empty, or say 'accessed'. Source: https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html
- #5 `2026-09-27/flink-lpg-group-crowdfund-extortion-order-hub-breach`: body "At least 10,000 customers and employees in the Netherlands received ransom notes" and summary "mass-emailed at least 10,000 individual customers and employees" (claims d36e28a6a7, 3dd10f2a21). (low confidence) heise: "gingen dort bei mindestens 10.000 Kunden Erpressermails ein" (customers). NL Times says only that individuals were contacted and that Flink is contacting 'customers and employees'. The 10,000 figure is customers only. Source: https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html
- #6 `2026-09-19/waterplum-contagious-interview-joint-advisory-scale`: body: "BeaverTail (a JavaScript loader hidden in NPM packages hosted on GitHub or Bitbucket)" (claim ce8f500d67). (low confidence) Advisory footnote 2: "BeaverTail is JavaScript-based malware hidden inside Node Package Manager (NPM) packages, and can be downloaded from GitHub or Bitbucket." It does not call BeaverTail a loader. Source: https://www.ic3.gov/CSA/2026/260918.pdf
- #7 `2026-09-18/gyazo-helpfeel-data-breach-image-upload-rce`: body: "...device ID, login-session ID, X/Google SSO tokens, profile data..." (not in the ledger; text unchanged this run). (low confidence) THN and Helpfeel list an "X (formerly Twitter) integration token, if the account was connected" and the "Email address used for Google single sign-on (SSO), if connected". The Google item is an email address, not a token. Source: https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html

### Unsupported / hallucinated facts (F4)
- #8 `2026-05-18/thorchain-gg20-threshold-signature-scheme-vault-drain-11m-ac`: title/headline: "THORChain GG20 Threshold Signature Scheme vault drain — ~$11M across nine chains". (low confidence) The run narrowed the body and summary so the GG20 TSS flaw is only CryptoTimes' 'working theory' (The Record reports a compromised vault; TRM attributes nothing). The unchanged title and headline still name the GG20 Threshold Signature Scheme as the drain mechanism. Suggest 'THORChain vault drain, ~$11M across nine chains; GG20 TSS flaw suspected'. Source: https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/

### Claims missing inline citation (F5)
- #9 `2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware`: second body paragraph, sentences 'Access begins with extensive social-engineering rapport-building...', 'The victim is then persuaded to download...', 'A decoy screen matching the lure's theme...', 'Operators target the victim's work device first...', 'In every observed instance the malware has targeted Windows only.' (claims c63eb00424, cb574a6172, c3ddb6fdb0, dd81aa79ee, 5a923b89dd). The whole paragraph, rewritten by this run, has no inline citation. Every fact is in NCSC's 'Delivery and exploitation' section ('Regardless of the file thematic, the approach has been to display a legitimate appearing screen ...', 'In all observed instances, the malware has been exclusively targeted at the Windows operating system'). Add ([NCSC UK, 2026-09-15](...)) at the paragraph end. Source: https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists
- #10 `2026-06-16/cve-2026-54420-litespeed-cpanel-whm-plugin-symlink-following`: body: "The exposure is most acute for hosting providers and any public-sector tenant on shared CloudLinux infrastructure." (claim 9eab6b0e6c). (low confidence) No cited source says exposure is most acute for hosting providers or public-sector tenants; LiteSpeed says only 'shared hosting servers running CloudLinux/CageFS'. Replace with the sourced exposure statement (user-end plugin before 2.4.8 on CloudLinux/CageFS shared hosting). Source: https://blog.litespeedtech.com/2026/06/01/security-update-for-litespeed-cpanel-plugin-2/
- #11 `2026-07-13/servicenow-ai-platform-sandbox-escape-cve-2026-6875`: body: "a population that still includes public-sector and critical-infrastructure operators running ServiceNow ITSM, HR-service-delivery and case-management on-prem or through partners" (claim eb43054cc8). (low confidence) No cited source names such operators or workloads. The KB and BleepingComputer say only that self-hosted instances needed the updates. Drop the clause or cite it. Source: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3137947

### Strengthen primary source (F6)
- #12 `2026-09-24/openai-agent-australia-medicare-portal-breach`: ACSC alert cited only via Cyber Daily (sources[] role primary, evidence[8..10], 2026-09-27 section, takeaway). The iteration-2 decline ('cyber.gov.au unreadable') no longer holds: `fetch_source.py extract` on this URL returned the full alert ('served via trafilatura-direct', dated 2026-09-24; it is intermittently blocked, a retry succeeds). The primary reads 'ASD's ACSC is aware of instances of artificial intelligence (AI) misalignment, in which AI agents have undertaken unexpected actions...', so the evidence quote 'We are aware of instances of AI misalignment...' is Cyber Daily's wording, not ACSC's. Re-cite the mitigation list and 'notable difference' passage to cyber.gov.au and add it to sources[] as primary. Source: https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/risks-of-ai-misalignment-to-australian-organisations
- #13 `2026-05-08/qilin-ransomware-hits-die-linke-germany-1-5-tb-claimed-dpa-n`: sourcing_note: "the party's own statement, which could not be retrieved from die-linke.de"; sources[] are three news outlets. (low confidence) `fetch_source.py extract` returned the party's statement (dated 27 March 2026, served via jina; direct transports fail). It carries the party-side facts the entry cites to Heise/BleepingComputer/The Record (Thursday 26 March detection, offline as a precaution, Qilin indication, criminal complaint, member database not affected, aim to publish internal and staff data, 'lässt sich nicht beurteilen'), though not the 2026-04-01 leak-site listing. Cite it as the victim-statement primary (German, translated) and correct the sourcing note; this also clears the aggregator-only WARN. Source: https://www.die-linke.de/start/presse/detail/news/cyberangriff-auf-die-partei-die-linke/

### Drop (low relevance / off-audience / duplicate) (F7)
- #14 `2026-09-27/flink-lpg-group-crowdfund-extortion-order-hub-breach`: priority: routine with a ~700-word body (three long paragraphs plus takeaway). (low confidence) The iteration-2 decline rested on the record not declaring `body`. This run's record now declares body and is public (make_public), so the trim is available. A routine awareness incident with no access vector should be held to a few sentences: actor, per-person pivot, the Contradiction line, the takeaway. Source: prompts/cti-run.md Phase 4 incident floor
- #15 `2026-09-18/gyazo-helpfeel-data-breach-image-upload-rce`: priority: routine with a ~360-word body listing every exposed field, vendor status-page criticism and a generic communications takeaway. (low confidence) Recalibrated to routine but not shortened; the record-count and field-list prose is the loss-figure-as-reason pattern the routine tier should not carry. The decline was procedural (internal record). A public improvement/correction record declaring body would allow a short version. Source: prompts/cti-run.md Phase 4 incident floor

### Needs more research (F8)
- #16 `2026-09-19/waterplum-contagious-interview-joint-advisory-scale`: Defender takeaway and Triage omit the advisory's own endpoint controls. (low confidence) Advisory section 4(3): open unknown VS Code projects only in Restricted Mode (answer 'No' to the trust prompt), verify '.vscode/tasks.json' for download/execute code, never open unknown projects from a previously trusted path, and be wary of command lines containing curl, base64, -enc, mshta, Invoke-WebRequest or hidden. The entry describes the StoatWaffle auto-run mechanism but drops the lever that defeats it. Source: https://www.ic3.gov/CSA/2026/260918.pdf
- #17 `2026-09-18/brevo-cloudflare-worker-clickfix-supply-chain`: actions[0] and Triage cover only WordPress sites that embed the widgets. (low confidence) Brevo: 'If you or a visitor ran the pasted command, treat that computer as compromised: disconnect it, run a full antivirus scan, and change passwords used on it.' Staff who browsed a Brevo-embedding site between 15:01 and 20:30 UTC on 2026-09-14 and followed the Win+R prompt are the constituency's likelier exposure; no endpoint check is stated. Source: https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up
- #18 `2026-07-13/servicenow-ai-platform-sandbox-escape-cve-2026-6875`: Defender takeaway tells self-hosted admins to apply the fixed release without the patch side effect. (low confidence) KB3137947: the patches include Guarded Script; 'Complex scripts ... will need to be moved into a script include'; guest (unauthenticated) traffic is enforced immediately on upgraded instances, authenticated traffic phases in over about four weeks (on-premises admins advance each phase manually). Relevant to the admins acting now. Source: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3137947
- #19 `multiple legacy entries (Sophos Beagle, Nx Console cascade, Check Point CVE-2026-50751, LiteSpeed, THORChain)`: no `**Defender takeaway:**` (and no `**Exposure:**` / `**Detection:**` where the sources support them) on entries whose bodies this run rewrote. (low confidence) Check Point (critical) has no labelled line at all although NCSC-CH gives the prerequisites (IKEv1, legacy Remote Access clients accepted, no mandatory machine certificate); Nx Console has Detection prose but no takeaway; Sophos has an unlabelled takeaway and no Detection line although Sophos and Malwarebytes describe the startup-folder MSI drop and the signed-updater sideload; LiteSpeed has Detection but no takeaway. These are legacy-format entries; add only the lines the cited sources already support. Source: docs/pipeline.md actionability contract

### Surface contradiction (F9)
- #20 `2026-07-13/servicenow-ai-platform-sandbox-escape-cve-2026-6875`: evidence[1] and body: ServiceNow "at disclosure was 'not currently aware of exploitation'" vs summary/headline exploitation. BleepingComputer (2026-07-20): 'ServiceNow has yet to flag this security as actively abused and, in the official advisory, still states that it is "not currently aware of exploitation against ServiceNow instances."', and the spokesperson: 'Based on our investigation to date, we have not observed evidence that this activity is related to instances that ServiceNow hosts.' The entry limits the vendor line to 'at disclosure' and never states that the vendor disputes or has not confirmed the exploitation NCSC-CH and Defused report. Add a Contradiction line. Source: https://www.bleepingcomputer.com/news/security/critical-servicenow-code-execution-flaw-now-exploited-in-attacks/
- #21 `2026-06-09/cve-2026-50751-check-point-security-gateway-ikev1-vpn-authen`: headline/summary/Correction: 'one case linked to a Qilin affiliate'; Correction says the earlier framing 'tied the whole exploitation period to a Qilin affiliate' (claims 0fc3241274, 9a4d8c4d72). (low confidence) Check Point states both: 'One case involved confirmed post-compromise activity associated with Qilin ransomware affiliate' and, under 'Actor profile', 'we assess with medium confidence that the actor behind the exploitation of CVE-2026-50751 is financially motivated, uses Qilin ransomware'. HNS, NCSC-NL and NCSC-CH repeat only the one-case wording. The narrowing drops the vendor's medium-confidence actor-level assessment; state both with their confidence. Source: https://blog.checkpoint.com/security/check-point-releases-important-hotfix-for-vulnerabilities-in-deprecated-ikev1-vpn-protocol/

### Editorial / less-is-more flags (advisory) (F11)
- #22 `2026-05-18/thorchain-gg20-threshold-signature-scheme-vault-drain-11m-ac`: body: "**Why it matters to us:** the relevance to a Swiss / EU public-sector SOC is the *technique class*, not the cryptocurrency context.". Composition-rationale sentence in reader text ('to us'), followed by uncited guidance naming FINMA-supervised custodians and MiCA platforms. State the defender lesson directly (node-admission and newly churned validator controls) as a Defender takeaway. Source: entries/2026-05-18/thorchain-gg20-threshold-signature-scheme-vault-drain-11m-ac.md
- #23 `2026-05-10/sophos-beagle-backdoor-distributed-via-fake-claude-ai-site-u`: techniques[] omits T1547.001. Sophos: the MSI 'drops three files into the user's startup folder'; Malwarebytes: the VBScript 'copies three files ... into the Windows Startup folder'. T1547.001 (Registry Run Keys / Startup Folder, active in the pin) is a clearly described behavior with no id. Source: https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor
- #24 `2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware`: record summary lists geography, screen-capture and drop-directory corrections that the Correction section does not state. (low confidence) The non-internal record says 'The victim geography and the screen-capture frequency follow NCSC's wording' and that the drop directory is 'described rather than given as a literal path', but the section only covers the espionage framing and the triage line. A reader cannot see that 'with confirmed victims in the UK, US and Netherlands' and 'the most commonly observed data-theft feature' were corrected. Add one cited sentence to the section or trim the record summary. Source: entries/2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware.md
- #25 `2026-09-24/shinyhunters-fbi-peoplesoft-breach-claim`: record summary: "...and credibility returns from 2 to 3.". (low confidence) Admiralty credibility digit and field narration in a rendered record summary; state the change (sources differ on whether the FBI statement confirms the compromise) without the rating digit. Source: entries/2026-09-24/shinyhunters-fbi-peoplesoft-breach-claim.md
- #26 `2026-09-24/shinyhunters-fbi-peoplesoft-breach-claim`: 2026-09-29 section names an arrested private individual and his employer history (Pepijn van der Stap). (low confidence) Krebs reports it from three sources, but the suspect is arrested and not charged, and the name and past employers add no detection or decision value for the readers. Consider 'a 24-year-old Dutch suspect' and dropping the biography. Source: https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/
- #27 `2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands`: entities: only actor:teampcp although the body covers Mini Shai-Hulud, Nx Console and DAEMON Tools. (low confidence) The registry has campaign:mini-shai-hulud, incident:nx-console-vs-code-extension-18-95-0-compromised-stolen-publ and incident:daemon-tools-supply-chain-2026; the body cites Help Net Security for the Mini Shai-Hulud attribution. Entity-linking miss (needs `entities` in the record's fields). Source: entities/registry.yaml

### Name-collision unflagged (F15)
- #28 `2026-09-29/kaspersky-payload-gpo-encryptionless-ransomware`: entities: [] and references: [] with a sourcing_note that no longer mentions the collision; body names the 'PAYLOAD' ransomware family. The registry holds actor:payload-ransomware (ambiguous_labels: ['Payload']; the leak-site group behind the 2026-08-20 Zurich-area listing, entry 2026-08-23/payload-zurich-it-provider-hwz-student-data). Kaspersky calls PAYLOAD an existing public family ('PAYLOAD cryptomalware for Windows does exist', 'an ESXi PAYLOAD variant', banner 'Welcome to Payload!') and speaks of 'PAYLOAD operators'; Ransomware.live describes the Payload group as 'using Babuk-derived source code targeting both Windows and ESXi', with Switzerland its most-hit country (7 victims). Removing the unsourced 'unrelated' claim was right, but the entry now neither links nor disambiguates. Add references[] to the 2026-08-23 entry and a sentence that Kaspersky does not name the operators and that the shared name is not established as the same group (or link actor:payload-ransomware if the main agent accepts Ransomware.live's group-to-family description). The record's 'no constituency nexus' rationale should be rechecked against the Swiss victim count if the link is made. Source: https://www.ransomware.live/group/payload

### Missed angles (F10)
None raised. Coverage of this slice's findings looks complete. Optional: the Helpfeel notice for Gyazo was updated on 2026-09-24 and 2026-09-27 (service suspended, then resumed), which the 2026-09-18 entry does not carry; below the entry's routine bar, so not raised as a finding.

### Verdict
NEEDS_FIXES (truth: 9, editorial: 13, advisory: 6)

Truth = F3 x7, F4 x1, F15 x1. Editorial = F5 x3, F6 x2, F7 x2, F8 x4, F9 x2. Advisory = F11 x6. Most truth items are low confidence and narrow; the load-bearing ones are #28 (F15, Kaspersky PAYLOAD link), #9 (uncited CHOSEN BRICK paragraph), #12 (ACSC primary now readable) and #20 (ServiceNow vendor position).

### Findings summary (machine-readable)
```yaml
- code: F3
  category: claim-not-supported
  section: 2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware
  item: 'body: "in at least one sample, this downloaded payload carried the data-wiping functionality already described above" (claim 9de3c5dbc3)'
  url_or_quote: https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists
  summary: (low confidence) NCSC lists wiping (T1485) among Telegram-bot tasking functions and separately says only "In at least one sample, there was functionality for data wiping (T1485)." It does not
    say the downloaded payload carried it. Narrow to NCSC's wording or drop the 'downloaded payload' link.
- code: F3
  category: claim-not-supported
  section: 2026-09-17/cve-2026-58704-google-pixel-modem-zero-click-eop
  item: headline "...a Pixel modem zero-day it says may be under limited, targeted exploitation" and summary "Google says there are indications it may be under limited, targeted exploitation" (claims cf683593fd,
    44cbf83994)
  url_or_quote: https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
  summary: (low confidence) The Google bulletin as read carries no exploitation statement and Google's spokesperson did not respond to TechCrunch; the only source is TechCrunch's dek ("The Pixel phone maker
    said there are indications ..."). The body attributes it correctly to TechCrunch; the headline and summary state it as Google's own words. Attribute to TechCrunch's reporting there too.
- code: F3
  category: claim-not-supported
  section: 2026-06-09/cve-2026-50751-check-point-security-gateway-ikev1-vpn-authen
  item: 'summary: "NCSC-CH flagged it as actively exploited and CISA added it to KEV (Check Point, 2026-06-08)." (claim f6ff2ecbc1)'
  url_or_quote: https://blog.checkpoint.com/security/check-point-releases-important-hotfix-for-vulnerabilities-in-deprecated-ikev1-vpn-protocol/
  summary: (low confidence) The trailing citation terminates the NCSC-CH and KEV clause, but the Check Point blog mentions neither. NCSC-CH is post 12615, KEV is the CISA feed (both already in sources[]).
- code: F3
  category: claim-not-supported
  section: 2026-09-23/austria-nisg-2026-bcs-transposition
  item: sources[] date 2026-09-30 and labels "[Kanton Bern KAIO, 2026-09-30]" in the closing sentence and the Correction (claims 3713ea1366, 360af5dd74)
  url_or_quote: https://www.kaio.fin.be.ch/de/start/themen/rechtliche-grundlagen/ICSG.html
  summary: '(low confidence) 2026-09-30 is the retrieval date: the page has no dateline (the extract metadata date equals the fetch date). Content is correct (ICSG and IDSV in force 1 November 2026, reporting
    platform with the IDSV). Drop the date from the label and leave sources[].date empty, or say ''accessed''.'
- code: F3
  category: claim-not-supported
  section: 2026-09-27/flink-lpg-group-crowdfund-extortion-order-hub-breach
  item: body "At least 10,000 customers and employees in the Netherlands received ransom notes" and summary "mass-emailed at least 10,000 individual customers and employees" (claims d36e28a6a7, 3dd10f2a21)
  url_or_quote: https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html
  summary: '(low confidence) heise: "gingen dort bei mindestens 10.000 Kunden Erpressermails ein" (customers). NL Times says only that individuals were contacted and that Flink is contacting ''customers
    and employees''. The 10,000 figure is customers only.'
- code: F3
  category: claim-not-supported
  section: 2026-09-19/waterplum-contagious-interview-joint-advisory-scale
  item: 'body: "BeaverTail (a JavaScript loader hidden in NPM packages hosted on GitHub or Bitbucket)" (claim ce8f500d67)'
  url_or_quote: https://www.ic3.gov/CSA/2026/260918.pdf
  summary: '(low confidence) Advisory footnote 2: "BeaverTail is JavaScript-based malware hidden inside Node Package Manager (NPM) packages, and can be downloaded from GitHub or Bitbucket." It does not
    call BeaverTail a loader.'
- code: F3
  category: claim-not-supported
  section: 2026-09-18/gyazo-helpfeel-data-breach-image-upload-rce
  item: 'body: "...device ID, login-session ID, X/Google SSO tokens, profile data..." (not in the ledger; text unchanged this run)'
  url_or_quote: https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html
  summary: (low confidence) THN and Helpfeel list an "X (formerly Twitter) integration token, if the account was connected" and the "Email address used for Google single sign-on (SSO), if connected". The
    Google item is an email address, not a token.
- code: F4
  category: hallucinated-fact
  section: 2026-05-18/thorchain-gg20-threshold-signature-scheme-vault-drain-11m-ac
  item: 'title/headline: "THORChain GG20 Threshold Signature Scheme vault drain — ~$11M across nine chains"'
  url_or_quote: https://www.cryptotimes.io/2026/05/17/10-8-million-drained-inside-the-thorchain-exploit-that-froze-cross-chain-defi-for-13-hours/
  summary: (low confidence) The run narrowed the body and summary so the GG20 TSS flaw is only CryptoTimes' 'working theory' (The Record reports a compromised vault; TRM attributes nothing). The unchanged
    title and headline still name the GG20 Threshold Signature Scheme as the drain mechanism. Suggest 'THORChain vault drain, ~$11M across nine chains; GG20 TSS flaw suspected'.
- code: F5
  category: missing-citation
  section: 2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware
  item: second body paragraph, sentences 'Access begins with extensive social-engineering rapport-building...', 'The victim is then persuaded to download...', 'A decoy screen matching the lure's theme...',
    'Operators target the victim's work device first...', 'In every observed instance the malware has targeted Windows only.' (claims c63eb00424, cb574a6172, c3ddb6fdb0, dd81aa79ee, 5a923b89dd)
  url_or_quote: https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists
  summary: The whole paragraph, rewritten by this run, has no inline citation. Every fact is in NCSC's 'Delivery and exploitation' section ('Regardless of the file thematic, the approach has been to display
    a legitimate appearing screen ...', 'In all observed instances, the malware has been exclusively targeted at the Windows operating system'). Add ([NCSC UK, 2026-09-15](...)) at the paragraph end.
- code: F5
  category: missing-citation
  section: 2026-06-16/cve-2026-54420-litespeed-cpanel-whm-plugin-symlink-following
  item: 'body: "The exposure is most acute for hosting providers and any public-sector tenant on shared CloudLinux infrastructure." (claim 9eab6b0e6c)'
  url_or_quote: https://blog.litespeedtech.com/2026/06/01/security-update-for-litespeed-cpanel-plugin-2/
  summary: (low confidence) No cited source says exposure is most acute for hosting providers or public-sector tenants; LiteSpeed says only 'shared hosting servers running CloudLinux/CageFS'. Replace with
    the sourced exposure statement (user-end plugin before 2.4.8 on CloudLinux/CageFS shared hosting).
- code: F5
  category: missing-citation
  section: 2026-07-13/servicenow-ai-platform-sandbox-escape-cve-2026-6875
  item: 'body: "a population that still includes public-sector and critical-infrastructure operators running ServiceNow ITSM, HR-service-delivery and case-management on-prem or through partners" (claim
    eb43054cc8)'
  url_or_quote: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3137947
  summary: (low confidence) No cited source names such operators or workloads. The KB and BleepingComputer say only that self-hosted instances needed the updates. Drop the clause or cite it.
- code: F6
  category: strengthen-primary-source
  section: 2026-09-24/openai-agent-australia-medicare-portal-breach
  item: ACSC alert cited only via Cyber Daily (sources[] role primary, evidence[8..10], 2026-09-27 section, takeaway)
  url_or_quote: https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/risks-of-ai-misalignment-to-australian-organisations
  summary: 'The iteration-2 decline (''cyber.gov.au unreadable'') no longer holds: `fetch_source.py extract` on this URL returned the full alert (''served via trafilatura-direct'', dated 2026-09-24; it
    is intermittently blocked, a retry succeeds). The primary reads ''ASD''s ACSC is aware of instances of artificial intelligence (AI) misalignment, in which AI agents have undertaken unexpected actions...'',
    so the evidence quote ''We are aware of instances of AI misalignment...'' is Cyber Daily''s wording, not ACSC''s. Re-cite the mitigation list and ''notable difference'' passage to cyber.gov.au and add
    it to sources[] as primary.'
- code: F6
  category: strengthen-primary-source
  section: 2026-05-08/qilin-ransomware-hits-die-linke-germany-1-5-tb-claimed-dpa-n
  item: 'sourcing_note: "the party''s own statement, which could not be retrieved from die-linke.de"; sources[] are three news outlets'
  url_or_quote: https://www.die-linke.de/start/presse/detail/news/cyberangriff-auf-die-partei-die-linke/
  summary: (low confidence) `fetch_source.py extract` returned the party's statement (dated 27 March 2026, served via jina; direct transports fail). It carries the party-side facts the entry cites to Heise/BleepingComputer/The
    Record (Thursday 26 March detection, offline as a precaution, Qilin indication, criminal complaint, member database not affected, aim to publish internal and staff data, 'lässt sich nicht beurteilen'),
    though not the 2026-04-01 leak-site listing. Cite it as the victim-statement primary (German, translated) and correct the sourcing note; this also clears the aggregator-only WARN.
- code: F7
  category: drop
  section: 2026-09-27/flink-lpg-group-crowdfund-extortion-order-hub-breach
  item: 'priority: routine with a ~700-word body (three long paragraphs plus takeaway)'
  url_or_quote: prompts/cti-run.md Phase 4 incident floor
  summary: '(low confidence) The iteration-2 decline rested on the record not declaring `body`. This run''s record now declares body and is public (make_public), so the trim is available. A routine awareness
    incident with no access vector should be held to a few sentences: actor, per-person pivot, the Contradiction line, the takeaway.'
- code: F7
  category: drop
  section: 2026-09-18/gyazo-helpfeel-data-breach-image-upload-rce
  item: 'priority: routine with a ~360-word body listing every exposed field, vendor status-page criticism and a generic communications takeaway'
  url_or_quote: prompts/cti-run.md Phase 4 incident floor
  summary: (low confidence) Recalibrated to routine but not shortened; the record-count and field-list prose is the loss-figure-as-reason pattern the routine tier should not carry. The decline was procedural
    (internal record). A public improvement/correction record declaring body would allow a short version.
- code: F8
  category: needs-more-research
  section: 2026-09-19/waterplum-contagious-interview-joint-advisory-scale
  item: Defender takeaway and Triage omit the advisory's own endpoint controls
  url_or_quote: https://www.ic3.gov/CSA/2026/260918.pdf
  summary: '(low confidence) Advisory section 4(3): open unknown VS Code projects only in Restricted Mode (answer ''No'' to the trust prompt), verify ''.vscode/tasks.json'' for download/execute code, never
    open unknown projects from a previously trusted path, and be wary of command lines containing curl, base64, -enc, mshta, Invoke-WebRequest or hidden. The entry describes the StoatWaffle auto-run mechanism
    but drops the lever that defeats it.'
- code: F8
  category: needs-more-research
  section: 2026-09-18/brevo-cloudflare-worker-clickfix-supply-chain
  item: actions[0] and Triage cover only WordPress sites that embed the widgets
  url_or_quote: https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up
  summary: '(low confidence) Brevo: ''If you or a visitor ran the pasted command, treat that computer as compromised: disconnect it, run a full antivirus scan, and change passwords used on it.'' Staff who
    browsed a Brevo-embedding site between 15:01 and 20:30 UTC on 2026-09-14 and followed the Win+R prompt are the constituency''s likelier exposure; no endpoint check is stated.'
- code: F8
  category: needs-more-research
  section: 2026-07-13/servicenow-ai-platform-sandbox-escape-cve-2026-6875
  item: Defender takeaway tells self-hosted admins to apply the fixed release without the patch side effect
  url_or_quote: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3137947
  summary: '(low confidence) KB3137947: the patches include Guarded Script; ''Complex scripts ... will need to be moved into a script include''; guest (unauthenticated) traffic is enforced immediately on
    upgraded instances, authenticated traffic phases in over about four weeks (on-premises admins advance each phase manually). Relevant to the admins acting now.'
- code: F8
  category: needs-more-research
  section: multiple legacy entries (Sophos Beagle, Nx Console cascade, Check Point CVE-2026-50751, LiteSpeed, THORChain)
  item: no `**Defender takeaway:**` (and no `**Exposure:**` / `**Detection:**` where the sources support them) on entries whose bodies this run rewrote
  url_or_quote: docs/pipeline.md actionability contract
  summary: (low confidence) Check Point (critical) has no labelled line at all although NCSC-CH gives the prerequisites (IKEv1, legacy Remote Access clients accepted, no mandatory machine certificate);
    Nx Console has Detection prose but no takeaway; Sophos has an unlabelled takeaway and no Detection line although Sophos and Malwarebytes describe the startup-folder MSI drop and the signed-updater sideload;
    LiteSpeed has Detection but no takeaway. These are legacy-format entries; add only the lines the cited sources already support.
- code: F9
  category: surface-contradiction
  section: 2026-07-13/servicenow-ai-platform-sandbox-escape-cve-2026-6875
  item: 'evidence[1] and body: ServiceNow "at disclosure was ''not currently aware of exploitation''" vs summary/headline exploitation'
  url_or_quote: https://www.bleepingcomputer.com/news/security/critical-servicenow-code-execution-flaw-now-exploited-in-attacks/
  summary: 'BleepingComputer (2026-07-20): ''ServiceNow has yet to flag this security as actively abused and, in the official advisory, still states that it is "not currently aware of exploitation against
    ServiceNow instances."'', and the spokesperson: ''Based on our investigation to date, we have not observed evidence that this activity is related to instances that ServiceNow hosts.'' The entry limits
    the vendor line to ''at disclosure'' and never states that the vendor disputes or has not confirmed the exploitation NCSC-CH and Defused report. Add a Contradiction line.'
- code: F9
  category: surface-contradiction
  section: 2026-06-09/cve-2026-50751-check-point-security-gateway-ikev1-vpn-authen
  item: 'headline/summary/Correction: ''one case linked to a Qilin affiliate''; Correction says the earlier framing ''tied the whole exploitation period to a Qilin affiliate'' (claims 0fc3241274, 9a4d8c4d72)'
  url_or_quote: https://blog.checkpoint.com/security/check-point-releases-important-hotfix-for-vulnerabilities-in-deprecated-ikev1-vpn-protocol/
  summary: '(low confidence) Check Point states both: ''One case involved confirmed post-compromise activity associated with Qilin ransomware affiliate'' and, under ''Actor profile'', ''we assess with medium
    confidence that the actor behind the exploitation of CVE-2026-50751 is financially motivated, uses Qilin ransomware''. HNS, NCSC-NL and NCSC-CH repeat only the one-case wording. The narrowing drops
    the vendor''s medium-confidence actor-level assessment; state both with their confidence.'
- code: F11
  category: editorial-advisory
  section: 2026-05-18/thorchain-gg20-threshold-signature-scheme-vault-drain-11m-ac
  item: 'body: "**Why it matters to us:** the relevance to a Swiss / EU public-sector SOC is the *technique class*, not the cryptocurrency context."'
  url_or_quote: entries/2026-05-18/thorchain-gg20-threshold-signature-scheme-vault-drain-11m-ac.md
  summary: Composition-rationale sentence in reader text ('to us'), followed by uncited guidance naming FINMA-supervised custodians and MiCA platforms. State the defender lesson directly (node-admission
    and newly churned validator controls) as a Defender takeaway.
- code: F11
  category: editorial-advisory
  section: 2026-05-10/sophos-beagle-backdoor-distributed-via-fake-claude-ai-site-u
  item: techniques[] omits T1547.001
  url_or_quote: https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor
  summary: 'Sophos: the MSI ''drops three files into the user''s startup folder''; Malwarebytes: the VBScript ''copies three files ... into the Windows Startup folder''. T1547.001 (Registry Run Keys / Startup
    Folder, active in the pin) is a clearly described behavior with no id.'
- code: F11
  category: editorial-advisory
  section: 2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware
  item: record summary lists geography, screen-capture and drop-directory corrections that the Correction section does not state
  url_or_quote: entries/2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware.md
  summary: (low confidence) The non-internal record says 'The victim geography and the screen-capture frequency follow NCSC's wording' and that the drop directory is 'described rather than given as a literal
    path', but the section only covers the espionage framing and the triage line. A reader cannot see that 'with confirmed victims in the UK, US and Netherlands' and 'the most commonly observed data-theft
    feature' were corrected. Add one cited sentence to the section or trim the record summary.
- code: F11
  category: editorial-advisory
  section: 2026-09-24/shinyhunters-fbi-peoplesoft-breach-claim
  item: 'record summary: "...and credibility returns from 2 to 3."'
  url_or_quote: entries/2026-09-24/shinyhunters-fbi-peoplesoft-breach-claim.md
  summary: (low confidence) Admiralty credibility digit and field narration in a rendered record summary; state the change (sources differ on whether the FBI statement confirms the compromise) without the
    rating digit.
- code: F11
  category: editorial-advisory
  section: 2026-09-24/shinyhunters-fbi-peoplesoft-breach-claim
  item: 2026-09-29 section names an arrested private individual and his employer history (Pepijn van der Stap)
  url_or_quote: https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/
  summary: (low confidence) Krebs reports it from three sources, but the suspect is arrested and not charged, and the name and past employers add no detection or decision value for the readers. Consider
    'a 24-year-old Dutch suspect' and dropping the biography.
- code: F11
  category: editorial-advisory
  section: 2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands
  item: 'entities: only actor:teampcp although the body covers Mini Shai-Hulud, Nx Console and DAEMON Tools'
  url_or_quote: entities/registry.yaml
  summary: (low confidence) The registry has campaign:mini-shai-hulud, incident:nx-console-vs-code-extension-18-95-0-compromised-stolen-publ and incident:daemon-tools-supply-chain-2026; the body cites Help
    Net Security for the Mini Shai-Hulud attribution. Entity-linking miss (needs `entities` in the record's fields).
- code: F15
  category: name-collision-unflagged
  section: 2026-09-29/kaspersky-payload-gpo-encryptionless-ransomware
  item: 'entities: [] and references: [] with a sourcing_note that no longer mentions the collision; body names the ''PAYLOAD'' ransomware family'
  url_or_quote: https://www.ransomware.live/group/payload
  summary: 'The registry holds actor:payload-ransomware (ambiguous_labels: [''Payload'']; the leak-site group behind the 2026-08-20 Zurich-area listing, entry 2026-08-23/payload-zurich-it-provider-hwz-student-data).
    Kaspersky calls PAYLOAD an existing public family (''PAYLOAD cryptomalware for Windows does exist'', ''an ESXi PAYLOAD variant'', banner ''Welcome to Payload!'') and speaks of ''PAYLOAD operators'';
    Ransomware.live describes the Payload group as ''using Babuk-derived source code targeting both Windows and ESXi'', with Switzerland its most-hit country (7 victims). Removing the unsourced ''unrelated''
    claim was right, but the entry now neither links nor disambiguates. Add references[] to the 2026-08-23 entry and a sentence that Kaspersky does not name the operators and that the shared name is not
    established as the same group (or link actor:payload-ransomware if the main agent accepts Ransomware.live''s group-to-family description). The record''s ''no constituency nexus'' rationale should be
    rechecked against the Swiss victim count if the link is made.'
```
