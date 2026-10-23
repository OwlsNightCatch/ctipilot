**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-23T04:29:16Z · ended_at=2026-10-23T04:51:04Z · duration_seconds=1308

## Verification report — 2026-10-23T0256Z-intel (iteration 2)

Scope walked: all 282 ledger claims (the 80 changed claims, every other claim of the eleven remediated or new entries, and all 15 Arista claims, which exceeds the required random quarter). Verdict rows: `verification.iter2.claims.yaml` (282/282 answered by `tools/claim_ledger.py --coverage 2`; 275 ok, 5 F3 rows (three findings), 1 F14, 1 F4). Every cited page was fetched this iteration (cached bodies not relied on); the HPE bulletin is a JS shell and was read once through the metered reader, byte-identical to the run's saved body.

### Citation does not support the claim
**F3 #1** `2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow`, body paragraph 1: "the supplier, PK Softech AG of Reinach (BL), says unknown persons used malware to reach part of its IT infrastructure" is cited to https://pksoftech.ch/de/newsreader/Cyberangriff-auf-die-PKSoftechAG. That page says only "Ende September 2026 wurde die PK Softech AG Opfer eines Cyberangriffs"; it names no town or canton. "Reinach BL" is on watson.ch ("PK Softech AG in Reinach BL") and in the NZZ. Cite one of those for the location or drop it. (low confidence on severity; the fact itself is true.)

**F3 #2** `2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release`, body paragraph 2 and Detection (claims 9b083a871e, 59279b1b66): "Threat Prevention coverage (Threat IDs 543004, 97622, ...) that protects only management traffic routed through a dataplane interface, sent to a replaced inbound-management certificate, decrypted so the firewall can inspect it, and covered by threat prevention" and "where the signatures are active and the four conditions hold". The advisory lists three bullets: "Route incoming traffic for the MGT port through a DP port", "Replace the Certificate for Inbound Traffic Management", "Enable threat prevention on the inbound traffic to management services". Neither the advisory nor the Unit 42 brief contains "decrypt" or "inspect". The fourth condition is the entry's inference presented as Palo Alto's. (low confidence)

**F3 #3** `2026-10-23/fortinet-fortisandbox-fortisiem-pre-auth-critical-fixes`, Defender takeaway and actions[0] (claims 327482c0e0, d71008be93): "until then keep the FortiSandbox GUI on an administrator network and allow tcp 27918 only from the deployment's own nodes", cited to FG-IR-26-185 and FG-IR-26-180. FG-IR-26-185 has no workaround; FG-IR-26-180 says only "Restricting access on tcp port 27918 prevents the issue." Neither page mentions an administrator network for the GUI or "the deployment's own nodes". Attribute only Fortinet's workaround to Fortinet and mark the rest as the entry's recommendation. (low confidence)

### Unsupported / hallucinated facts
**F4 #4** `2026-10-23/blackx-uefi-bootkit-baton-drop-revocation-default-off`, `cves[CVE-2023-24932].status: [exploited, patch-available]` (claim e47b726190). The body itself says "Kaspersky ties the exploitation to Baton Drop alone; CVE-2023-24932 ... appears in its post only as the one a UEFI component in ESET's FishMonger report might exploit"; Securelist: "the possible use of an unspecified UEFI bootkit component, which might exploit CVE-2023-24932". Microsoft's KB ties the CVE to BlackLotus, not BlackX. The frontmatter overstates the body. (low confidence)

**F4 #5** run record: `entries_dropped_by_verification: 0` while the notes say the YOOtheme entry was "written, then cut at verification iteration 1"; `completed: 2026-10-23T03:49:54Z` precedes the FortiSandbox/FortiSIEM entry's `discovered_at` 2026-10-23T04:25:40Z (added in remediation). (low confidence)

### Quantifier without source
**F14 #6** `2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow`, `## Update 2026-10-23` paragraph 2 (claim 23f7fc011b): "This is the first reported statement by an authority on the actor, but it reaches the reader second-hand ..." terminates on Publica's page, whose 2026-10-20 status says only "Dazu dauern die Abklaerungen noch an". No cited source says "first", and the entry's own `## Update 2026-10-21` reports "the involved federal bodies assume Akira is responsible" (Inside IT 2026-10-20: "gehen die involvierten Bundesstellen davon aus, dass die Ransomware-Bande Akira fuer den Angriff verantwortlich ist"). Replace with "a reported confirmation by the Federal Prosecutor's Office" or drop "first".

### Surface contradiction
**F9 #7** `2026-10-09/publica-...` main analysis paragraph 1 still says in the present tense "neither the Confederation nor Publica has confirmed the perpetrator or the demand" while the newest section reports (second-hand) that "the Federal Prosecutor's Office confirmed that data was extracted by the Akira ransomware group". The summary was reworded and dated; this sentence was not. Date it ("as of 2026-10-20") or add the relayed statement. (low confidence)

**F9 #8** `2026-10-23/cve-2026-114625-arista-...`: the advisory page says CWE-89 SQL injection with operator privileges and access to internal-only functionality; the CSAF the entry cites carries "CVE Description : VeloCloud Orchestrator Remote Code Execution (VCO RCE)". The entry uses the CSAF only for the score and interim measures, types the flaw `sqli`, and does not note Arista's own RCE label. Add a `Contradiction:` line. (low confidence)

### Needs more research
**F8 #9** `2026-10-21/emudhra-...`, `cves[CVE-2026-91403].fixed` says only "the Java updates of Oracle's Security Alert and the OpenJDK advisory of 2026-10-21". The cited tracker lists the fixed builds ("Java | 27.0.1.0.2, 25.0.5.0.2, 21.0.13.0.2, 17.0.21.0.2, 11.0.33.0.2, 8u511") while Oracle's alert lists 27.0.1, 25.0.5, 21.0.13, 17.0.21, 11.0.33, 8u511 as affected; without the build identifiers a responder cannot tell a fixed 21.0.13.0.2 from an affected 21.0.13, and the tracker's 8u511 (fixed) against Oracle's 8u511 (affected) is not reconciled. (low confidence)

### Editorial / less-is-more flags (advisory)
**F11 #10** Store-internal wording in reader-facing prose: hardening entry "that the store covers in the earlier entry linked from this one"; FortiSandbox entry "the earlier FortiSandbox entry records 5.0.6 and 4.4.9 as the builds that fix them".
**F11 #11** eMudhra: the `## Update 2026-10-23` section repeats the main-analysis Java paragraph nearly fact for fact (Oracle CVSS and exploitability, OpenJDK alternatives, distribution packages, NCSC.ch status).
**F11 #12** Publica: "is available to cite" (summary, sourcing_note, section) is verification-process wording; headline "PK Softech kept Publica data it had promised in writing to delete" drops the "apparently" the Tamedia lede ("offenbar") and Publica ("mutmasslich") carry (Inside IT's lede is unhedged, so low).
**F11 #13** PAN-OS headline "PHP2Shell hits PAN-OS, Panorama and WF-500" reads as exploitation while Palo Alto knows of none; use "affects".

### Delta verification (iteration-1 findings, each checked against the live source)
1 php VulnCheck wording: page "As of 7 PM ET on October 22, ... at least one PoC that successfully bypassed ASLR on x86-64 systems for a single version of PHP (8.4.26) with default heap configurations ... did not work outside of this specific setup", "supports PHP 8.4.10-8.4.26 with no modifications": correct.
2 eMudhra Apple date: tracker "on Apple products since the 22nd": correct.
3 eMudhra Exposure: tracker lists Node.js, Bun, FreeBSD fixed and Composer ca-bundle, Erlang certifi, Bottlerocket, Godot pending: correct.
4 hardening "scheduled for 2026-10-22": blog "On October 22, 2026, Fortinet will release ... following recent releases from FortiMail and FortiAuthenticator": correct.
5 Publica Tagi/Inside IT split: Tagi lede ("Das ist offenbar nicht geschehen", "Doch dies war falsch") and Inside IT ("im Januar 2026 ... Migration von 2019"): correct.
6/7 PAN-OS and PHP hotfix ETAs: all 21 ETAs, Panorama and WF-500 "ETA: TBD", XCORE 10/21 and WildFire Cloud 10/22 footnotes match the live advisory: correct.
8 PHP evidence quotes: watchTowr "since October 21, 2026" and VulnCheck "was successful on x86-64 platforms with ASLR enabled" are on the live pages: correct.
9 hardening FortiMail overlap: FG-IR-26-175 table identical, "Known Exploited Yes", CVE-2026-104286: correct.
10 Publica Frontaliere to TicinoNews: "Secondo nostre informazioni, nel server della ditta c'era una cartella IPCT": correct.
11 YOOtheme dropped: file absent from `entries/`. 12 Cisco Expressway update reverted: `git status` shows no change to `entries/2026-10-22/cve-2026-76466-...`; NetScaler references carry no Cisco entry: correct.
13 Publica F9: summary reworded and dated, but main-analysis paragraph 1 not (see F9 #7).
14 HPE ranges: bulletin text ranges and CSAF `known_affected` ranges (>=10.6.0.0|<=10.7.2.6, >=10.3.0.0|<=10.4.1.13, >=8.12.0.0|<=8.13.3.0) match the entry for all 19 CVEs; CVSS and mechanisms match: correct.
15 FortiSandbox/FortiSIEM entry (new, read cold): ids, CVSS 9.6/9.4, "Known Exploited No", versions, port 27918 workaround, E:F/E:H vectors, Defused/June flaws and 5.0.6/4.4.9 overlap verified; findings F3 #3 and F11 #10 only.
16 PHP actions[1] removed: one action remains. 17-20 wording changes present (m365 "12 minutes ... four minutes", "is affected by", "change windows ... that Fortinet suggested", Mythic "updater-style name", BlackX Kaspersky caveat).

### Coverage
No missed angle found. In-window NCSC.ch advisories 13090 to 13093 (GitLab, Oracle Java, Fortinet, Cisco Expressway) are all covered; KEV 2026.10.21 carries no addition; the SharePoint "zero-day" headline in The Register's sidebar is a July 2025 article. FortiSandbox/FortiSIEM is borderline on the sound-throughout bar (Fortinet's regular monthly release, no exploitation) but the "June-patched units are still affected" hook keeps it defensible.

### Verdict
NEEDS_FIXES (truth: 6, editorial: 3, advisory: 4)

### Findings summary (machine-readable)
See `work/2026-10-23T0256Z-intel/verification.iter2.findings.yaml` (13 records).
