**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-11T04:11:20Z · ended_at=2026-11-11T04:40:46Z · duration_seconds=1766

## Verification report — 2026-11-11T0256Z-intel (iteration 1)

Scope: 12 new entries, 8 updated entries (whole entry read, `git diff HEAD` read for each), run record. Claim ledger `claims.iter1.yaml`: 438 of 438 claims walked, every claim has a row in `verification.iter1.claims.yaml` (413 ok, 11 F3, 10 F4, 3 F14, 1 F5, 0 unreadable). Sources fetched this iteration: every cited URL (MSRC records read through the update-guide API and the November CVRF; CISA pages through WebFetch; Ivanti advisory pages are a JS shell that no transport reads, so the Ivanti entry was checked against the two ENISA EUVD records only). Findings marked (low confidence) rest on evidence I read but whose reach I could not fully confirm.

### Citation does not support the claim

1. **#1 [F3]** `2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates` — eMudhra: macOS command-line tools "keep trusting them until a future update" / "check again after every macOS update" / heise "macOS 27.3 ... not expected before December"
   - Source/quote: https://support.apple.com/de-de/149555
   - The Apple page the entry cites three times (publication date now 10. November 2026) says: "Ab macOS 27.2.1 akzeptieren diese Befehlszeilenwerkzeuge diese Zertifikate nicht mehr" and that macOS 26.7.3 and 15.8.3 carry the protection too, and "Nachdem du auf macOS 27.2.1, macOS 26.7.3 oder macOS 15.8.3 aktualisiert hast, musst du diese Schritte nicht wiederholen." The tracker the entry also cites (emudhra.we-have-a-problem.com) says "Fixed in macOS 27.2.1, 26.7.3, and 15.8.3." Claims 88f3538fc1, e7160c47b1, 436c748caa and actions[0] (61b4eec292, "repeat it after each macOS update until the one that carries Apple's own change") are stale; the update that was written this run on SonicWall did not pick this up. Cite Apple as of 2026-11-10, name the fixed macOS builds, drop the heise 27.3 claim.

2. **#2 [F3]** `2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates` — (low confidence) "Apple devices on 2026-10-19, with the G3 root following there on 2026-10-23"
   - Source/quote: https://emudhra.we-have-a-problem.com/
   - Claim 6e80875731 is cited to the tracker, BleepingComputer and the Apple page. Tracker: "blocked in Firefox and Chrome since the 17th of October, on Microsoft platforms since the 20th and on Apple products since the 22nd"; BleepingComputer: "Apple added protections on October 22". The Apple page as fetched carries no 19 or 23 October dates. Low confidence only because an earlier revision of the Apple page may have carried the dates.

3. **#3 [F3]** `2026-10-31/cve-2026-98432-linux-kernel-tcp-uaf-mptcp-remote-root` — Kernel UAF: "Ubuntu's tracker, last updated 2026-11-07, ... 16.04 to 26.04 are still in progress" / takeaway "Ubuntu's LTS kernels were not out on 2026-11-07"
   - Source/quote: https://ubuntu.com/security/CVE-2026-98432
   - The cited Ubuntu tracker now reads "Last updated 10 November 2026" and lists 26.04 LTS "Fixed in 7.0.0-43.43", 24.04 LTS "Fixed in 6.8.0-149.149", 22.04 LTS "Fixed in 5.15.0-203.213"; only 20.04, 18.04 and 16.04 remain "work in progress". The entry was edited this run (Veeam) but still tells readers the Ubuntu LTS kernels are not out; headline ("Ubuntu 26.10 kernel out"), title and action[0] share the staleness. Claims 967f8237c1, 876946fbbf. Refresh as a correction/update on the entry and date the citation to the page (2026-11-10).

4. **#4 [F3]** `2026-11-11/turla-cereal-exchange-server-c2-and-mail-collector-gov` — Turla Cereal: "could not determine the initial access method, so there is no CVE to patch against" / "With no external C2 and nothing to patch"
   - Source/quote: https://web-assets.esetstatic.com/wls/en/papers/white-papers/turla-cereal-tricks.pdf
   - The clause (claim 08a969c360) is cited to the ESET blog post, which carries no initial-access statement. The white paper says: "We were unable to determine the initial access method. However, given that the Exchange servers are accessible from the internet, it is possible that they were breached by exploiting a vulnerability." The entry drops ESET's hedge and converts "unknown" into "no CVE to patch against" / "nothing to patch" (claim 43e8cc112c), which no source states. Cite the white paper for the initial-access statement and keep ESET's own wording.

5. **#5 [F3]** `2026-11-11/qubole-vendor-aws-identity-assumes-integration-roles` — (low confidence) "Wiz found no tie to other reported activity ...; it does not know how the Qubole IAM users were compromised"
   - Source/quote: https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild
   - Claim 03c6457492 (and the sourcing_note "Wiz does not know how the Qubole IAM users were compromised") is cited to Wiz. The Wiz post says only "Wiz has not identified any ties between this campaign and other publicly reported activity" and that it has no insight into motivation; it does not state what it knows about the compromise of the IAM users. BleepingComputer writes "The report does not specify the exact method used to compromise the Qubole accounts". Reword to "does not say" and cite BleepingComputer.

6. **#6 [F3]** `2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates` — (low confidence) actions[2]: "Cisco's remediation ... its eMudhra advisory (version 1.8)"
   - Source/quote: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-emudhra-info-ScS22A1r
   - The Cisco advisory page now lists "1.9 Updated products under investigation, impacted, and not impacted ... 2026-NOV-10". The action cites version 1.8 and the update written this run did not read the revision. Re-read 1.9 and update the version and any changed product rows (claim 818a7fb237).

### Unsupported / hallucinated facts

7. **#7 [F4]** `2026-11-11/cve-2026-124194-outlook-forced-authentication-exploited-kev` — CVE-2026-124194 Outlook zero-day: "no source names ... the kind of credential taken" / NTLM "no cited source states it"
   - Source/quote: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-124194
   - Summary ("no source names the actor, the victims or the kind of credential taken"), body ("No source names ... the kind of credential obtained"), Detection ("no cited source states it") and sourcing_note ("the NTLM hypothesis ... not from a source") are contradicted by the cited Microsoft record (MSRC API FAQ: "This vulnerability discloses a user's NTLMv2 hash to the attacker who could use this to authenticate as the user.") and by the cited BleepingComputer article ("exploited in attacks to steal NTLM account hashes"). State that Microsoft says NTLMv2 hash disclosure, drop the "hypothesis" hedging, and sharpen Detection/action (NTLMv2 relay or crack).

8. **#8 [F4]** `2026-11-11/qubole-vendor-aws-identity-assumes-integration-roles` — summary: "the counts range from \"over a dozen\" to \"dozens\""
   - Source/quote: https://sentra.io/blog/breaches/inside-the-qubole-supply-chain-attack
   - The summary puts "over a dozen" in quotation marks, but no cited page uses it: Sentra says "More than a dozen organizations" and "Dozens of Qubole customers"; BleepingComputer says "tens of companies". Use the source wording or drop the quote marks (claim a5815ddc82).

9. **#9 [F4]** `2026-11-11/copperdragon-silentdelivery-fake-certificate-watering-holes` — (low confidence) "DLL sideloading of uncommon signed executables" / Detection "rarely abused signed executables"
   - Source/quote: https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/
   - Check Point says DarkWire "heavily relies on DLL sideloading as a primary execution technique, often abusing executables that are not widely observed among other threat actors in the wild"; "signed" appears nowhere in that section (claims 288fee62d6, 8d0436b428). Drop "signed".

10. **#10 [F4]** `2026-11-11/ghostframe-esxi-post-exploitation-framework-tag-218` — (low confidence) "edits the ESXi boot script /etc/rc.local.d/local.sh and /sbin/auto-backup.sh to survive reboots"
   - Source/quote: https://www.recordedfuture.com/blog/ghostframe-esxi-implant-settra-ransomware
   - Insikt: the implant persists by "modifying the ESXi boot script /etc/rc.local.d/local.sh ... The implant also executes /sbin/auto-backup.sh to preserve the modified configuration across reboots"; Insikt's mitigation names changes to local.sh only. The entry (claim d2cdd1fc83, Detection, actions[0]) says it edits auto-backup.sh as well and tells hunters to look for changes to it. State that the implant executes auto-backup.sh.

11. **#11 [F4]** `2026-11-11/confluence-dc-cve-2026-90436-apache-axis-remote-api-rce` — (low confidence) Exposure "a Data Center instance on 9.2.27 or earlier"; sourcing_note "Atlassian states no exploitation"
   - Source/quote: https://confluence.atlassian.com/security/cve-2026-90436-remote-code-execution-in-confluence-data-center-and-server-1874560038.html
   - Atlassian lists Confluence Data Center 1.x.x to 9.x.x as affected and 9.2.28 as the only fixed version ("patch ... to the latest version or one of the listed fixed versions"), so "9.2.27 or earlier" narrows the affected range (claim 986f9a06cc). The advisory also makes no statement about exploitation at all (neither "none" nor "some"); the sourcing_note says "Atlassian states no exploitation". Reword both.

12. **#12 [F4]** `2026-11-10/n-able-n-central-33-unpatched-flaws-public-pocs-offline` — (low confidence) sourcing_note: "the CNA records do not state whether authentication is needed"
   - Source/quote: https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122942
   - N-able's CNA records carry CVSS 4.0 vectors that state the privilege requirement: CVE-2026-125883 and CVE-2026-125881 PR:N, CVE-2026-125878 and CVE-2026-91000 PR:L, CVE-2026-125882, -125879 and -125880 PR:H (EUVD-2026-122942, -122961, -122958, -122956, -122963, -122959, -122964). The scores in cves[] are CVSS 4.0, which the entry never says.

13. **#13 [F4]** `2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack` — (low confidence) Update section: "What is new is the patch statement and the wider population: BACS says security updates fixing the known flaws are available for the AK-SM 800A and 8xxA family"
   - Source/quote: https://security-hub.ncsc.admin.ch/#/posts/13054
   - NCSC Switzerland's Cyber Security Hub advisory of 2026-10-13, which the entry cites, already says "Vendor firmware updates are available for the AK-SM 800A and fix the disclosed CVEs" and "Newer AK-SM 800A firmware enables Strict Session Control and mandatory HTTPS by default"; the entry has also carried Censys's 4.3.1 fixed-firmware statement since 2026-10-14. The patch statement is not new; the genuine delta is BACS's public SME-facing warning and user list. Same framing in the record summary and the new Defender-takeaway sentence (claim 8927156011).

14. **#14 [F4]** `2026-11-11/vates-xen-orchestra-vsa-2026-062-auth-bypass-exploited` — (low confidence) "needs network reach to the interface and one unexpired token in the Xen Orchestra database"
   - Source/quote: https://docs.vates.tech/security-advisories/advisories/2026/vates-sa-2026-062/
   - Vates: the token collection "returns its first token; the provider authenticates as that token's owner if it is unexpired", i.e. the first stored token must be unexpired, not any one (claim 77c784cb9f). Precision fix.

### Claims missing inline citation

15. **#15 [F5]** `2026-11-11/adobe-connect-apsb26-191-five-unauthenticated-cvss-10-rows` — Defender takeaway: "rather than within Adobe's 30-day priority window"
   - Source/quote: https://www.adobe.com/trust/security/products/connect/apsb26-191
   - Neither the bulletin (it only says "priority 2") nor Adobe's severity-ratings page as fetched states a 30-day window; the sentence has no citation (claim 85aed99957). Cite Adobe's priority definition or drop the number.

### Drop (low relevance / off-audience / duplicate)

16. **#16 [F7]** `2026-11-11/confluence-dc-cve-2026-90436-apache-axis-remote-api-rce` — (low confidence) Confluence DC Remote API RCE, Adobe Connect APSB26-191 and the Microsoft Patch Tuesday roll-up as routine patch-cycle items
   - Source/quote: https://confluence.atlassian.com/security/cve-2026-90436-remote-code-execution-in-confluence-data-center-and-server-1874560038.html
   - All three are unexploited with no public proof of concept; Confluence is reachable only with an opt-in, off-by-default setting (a listed `high` disqualifier), Adobe Connect on-premises has no stated constituency footprint, and the Microsoft rows are Microsoft-scored exploit-code-unproven (E:U) fixes inside the regular cycle with no mechanism for five of the seven. The entries argue for prioritisation inside the cycle, not for action beyond it. Consider dropping, or cut to two sentences.

### Needs more research

17. **#17 [F8]** `2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates` — Update missed Microsoft's 2026-11-10 revision: remaining eMudhra roots removed from Windows, Edge and the Trusted Root Program from 2026-11-16
   - Source/quote: https://www.microsoft.com/en-us/msrc/blog/2026/10/microsoft-response-to-compromised-emudhra-certificate-authority-keys
   - The Microsoft post the entry cites carries "Update (November 10, 2026)": "Microsoft is removing the remaining eMudhra root certificates across its products and services, starting November 16, 2026" (10 roots from the Trusted Root Program and Windows; Edge and WebView2 remove default trust for emSign Root CA - G1, C1, ECC and Root TLS CA - G1; Azure Linux, .NET images and OpenJDK follow). The entry mentions only the October removals of seven certificates and Chrome's 2026-11-16 SCT cutoff, and actions[1] covers only G3 and the seven October certificates. Windows/Edge fleets lose trust in G1-chained certificates five days from now, so this is the decision-relevant delta of the day; add it (with the Apple 27.2.1 fix and Cisco v1.9) to this update.

18. **#18 [F8]** `2026-10-23/fortinet-hardening-release-fortios-fortimanager-fortimail` — FG-IR-26-265 (FortiAuthenticator, CVSS 9.1) not listed although sourcing_note says "only the unauthenticated rows scored 9.0 or higher are listed here"
   - Source/quote: https://fortiguard.fortinet.com/psirt/FG-IR-26-265
   - FG-IR-26-265 "An Incorrect Authorization vulnerability [CWE-863] in FortiAuthenticator may allow an attacker to bypass authentication and gain unauthorized access", CVSSv3 9.1 with vector AV:N/AC:L/PR:N/UI:N/.../E:F (functional exploit code), same fixed builds 8.0.4 and 6.6.11, published 2026-11-10 in the same feed. It meets the entry's own selection rule and is on the identity provider the entry already covers; the sourcing_note claim is therefore wrong as written. Add the row (or say the advisory does not state authentication) and correct the note.

19. **#19 [F8]** `2026-10-23/fortinet-hardening-release-fortios-fortimanager-fortimail` — (low confidence) CVE-2026-126253 FortiOS OSPF "unauthenticated attacker" without the adjacent attack vector
   - Source/quote: https://fortiguard.fortinet.com/psirt/FG-IR-26-267
   - FG-IR-26-267 scores 9.3 with CVSS vector AV:A (adjacent network), summary "unauthenticated attacker to broadcast LSA via specially crafted request". The entry, its Exposure line and the "internet-facing units first" action do not say that this row needs adjacency, which changes triage for internet exposure.

### Surface contradiction

20. **#20 [F9]** `2026-11-10/n-able-n-central-33-unpatched-flaws-public-pocs-offline` — (low confidence) cves[] types/vectors follow Huntress, N-able's CNA records say otherwise
   - Source/quote: https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122958
   - CVE-2026-125878 is typed rce/"multiple OGNL injection flaws per Huntress", but N-able's CNA record (EUVD-2026-122958, 8.7, PR:L) describes "cross-site scripting ... Resource Injection"; CVE-2026-125879 is typed local privilege escalation while its CNA record (EUVD-2026-122959, 8.6) carries AV:N/PR:H and "Incorrect privilege assignment". The entry cites the CNA records only for -125883 and -125881 and does not surface the disagreement.

21. **#21 [F9]** `2026-11-11/ivanti-epm-cve-2026-121653-unauthenticated-sqli-rce` — (low confidence) Cloud Services Application "the second record does not say which build fixes it"
   - Source/quote: https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-121155
   - EUVD-2026-121155 describes "version 5.0.8" as affected in prose but lists the structured product as "Cloud Services Application, patch: 5.0.8" (the first record uses the same "patch: 2024 SU8" field for the fixed build). The entry says the fixed build is unknown without surfacing that the record's own fields disagree. Also CVE-2026-121683 is in title, summary and body but absent from cves[].

22. **#22 [F9]** `2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow` — (low confidence) supplier "received a demand \"not made concrete with an amount or deadline\"" next to PK Softech "no concrete ransom demand"
   - Source/quote: https://www.watson.ch/schweiz/datenschutz/664513749-nach-daten-klau-keine-loesegeldforderung-von-hackern-an-publica-softwarelieferan
   - watson.ch's lead and headline say no ransom demand reached the supplier or the Confederation ("gingen weder an diesen, noch an den Bund Lösegeldforderungen ein"); the Sepos spokeswoman's sentence ("Dies im Gegensatz zum Softwarelieferanten ..., dort allerdings nicht mit einem Betrag oder einer Frist konkretisiert") is read by the entry as "the supplier did receive a demand". PK Softech says "keine konkreten Lösegeldforderungen". The entry states the supplier received a demand as fact without a Contradiction line.

23. **#23 [F9]** `2026-10-31/cve-2026-98432-linux-kernel-tcp-uaf-mptcp-remote-root` — (low confidence) body no longer mentions the severity dispute while cves[].cvss still does
   - Source/quote: https://kb.ciq.com/article/security-advisories/cve-2026-98432-mitigation
   - This run's body edit deleted "Severity is disputed: the CNA scores it 9.8, upstream 8.1 with high attack complexity" (CIQ: "The kernel.org CNA scores the CVE 9.8 ... Upstream rates it 8.1 (important) with attack complexity high"; Sophos: Red Hat rated 5.9) and the Go team's "not specific to MPTCP" sentence, while cves[].cvss still reads "upstream rates it 8.1 per CIQ". The record summary mentions only Veeam.

### Missed angles

24. **#24 [F10]** `run-record` — (low confidence) Cisco critical advisories (Catalyst SD-WAN Controller, Secure Email Gateway, Meraki) named in the Patch Tuesday roundup, no disposition
   - Source/quote: https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2026-patch-tuesday-fixes-1-235-flaws-outlook-zero-day/
   - BleepingComputer's 2026-11-10 roundup lists "Cisco released security updates for numerous products, including critical vulnerabilities Catalyst SD-WAN Controller, Secure Email Gateway, and Meraki"; the run record names Cisco BroadWorks, ISE and Brotli rows but no disposition for these, and no Cisco PSIRT source is among the attempted sources. Suggested search: "Cisco Catalyst SD-WAN Controller Meraki Secure Email Gateway critical advisory November 2026".

### Single-source items missing [SINGLE-SOURCE] flag

25. **#25 [F12]** `2026-11-11/synology-dsm-sa-26-19-preauth-sqli-auth-api-rsync-bypass` — (low confidence) verification: multi-source on Synology SA-26:19 and Confluence CVE-2026-90436 (second source self-described as a restatement)
   - Source/quote: https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1493/
   - The sourcing_notes say CERT-FR (Synology) and BSI CERT-Bund (Confluence) are "a restatement, not an independent assessment"; the vendor advisory is the only source. Use verification single-source (vendor primary) rather than multi-source, or name the carve-out.

### Quantifier without source

26. **#26 [F14]** `2026-11-11/microsoft-november-2026-patch-tuesday-preauth-9-8-rows` — "seven unauthenticated network flaws rated CVSS 9.8" (title, headline, summary, first body sentence)
   - Source/quote: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-95882
   - The November 2026 MSRC CVRF lists further CVSS 3.1 9.8 AV:N/PR:N/UI:N rows with the same "in-network attacker calling arbitrary endpoints" FAQ as the DNS, DHCP and iSCSI rows the entry covers: DirectMusic CVE-2026-95882 and CVE-2026-95901, Media Foundation CVE-2026-96157, Windows Xbox Live Networking Service CVE-2026-112967 (plus Color Management CVE-2026-96067/96078 and Azure OpenAI CVE-2026-119990 at 9.8). The sourcing_note excludes "file-format parsers that need a user to open a file", which Microsoft's records for DirectMusic, Media Foundation and Xbox do not say. "Seven" is the entry's selection, not the release count: scope the title/summary ("seven ... in domain infrastructure and server roles") or cover the others. Claims 8d7f969c98, 0a6c5683c1, 1b194dd86f.

27. **#27 [F14]** `2026-11-10/sap-november-2026-cna-records-four-unauth-cvss-10-rows` — Title: "Onapsis, which found two of them" (four CVSS 10.0 flaws)
   - Source/quote: https://onapsis.com/blog/proxygate-cve-2026-89103-sap-netweaver-gateway-threat-advisory/
   - Onapsis says ICM2SHELL (CVE-2026-76964 and CVE-2026-89126) and PROXYGATE (CVE-2026-89103) were each "discovered and reported by the Onapsis Research Labs": three of the four CVEs. The title says two; the body ("Onapsis, which found and reported the Web Dispatcher, ICM and Gateway flaws") and the record summary say three flaws. Fix the title.

### Org-triage line missing / inconsistent

28. **#28 [F16]** `2026-11-11/vates-xen-orchestra-vsa-2026-062-auth-bypass-exploited` — (low confidence) priority notable on Vates (exploited, vendor-Critical pre-auth Admin and root on XCP-ng hosts) and on SAP (four unauthenticated CVSS 10.0, working exploit with the researcher, patch Web Dispatchers first)
   - Source/quote: https://docs.vates.tech/security-advisories/advisories/2026/vates-sa-2026-062/
   - Vates states active exploitation of an unauthenticated management-plane bypass leading to code execution and root on hypervisors; by the `high` bar (plausible exposure plus a decision within 7 days) it looks under-called next to the exploited Chrome and Outlook entries rated `high`. The SAP entry (2026-11-10/sap-november-2026-cna-records-four-unauth-cvss-10-rows) has Onapsis stating a working unauthenticated RCE exploit exists and telling internet-facing Web Dispatchers to be patched first.

### Action-item discipline

29. **#29 [F18]** `2026-11-11/vates-xen-orchestra-vsa-2026-062-auth-bypass-exploited` — (low confidence) Vates actions[1] restates Detection; eMudhra actions[0] is a five-tool task list
   - Source/quote: actions[1]: "On every Xen Orchestra instance that was reachable from an untrusted network, search the XCP-ng hosts for the attacker's artefacts Vates lists ..."
   - Vates actions[1] repeats the Detection paragraph (hvm_serial file, pivot2, cron.d files, ld.so.preload) plus reinstall/rotate from the Defender takeaway; GhostFrame actions[0] likewise repeats its Detection line. 2026-10-21/emudhra actions[0] chains Java, Python, Go, GitLab, SonicWall and macOS steps in one item and is not startable as one task. Split or trim.

### Editorial / less-is-more flags (advisory)

30. **#30 [F11]** `2026-11-11/vates-xen-orchestra-vsa-2026-062-auth-bypass-exploited` — attacker-chosen names as indicators: pivot2 VM, zz-ustar cron files (Vates); vmhostd-core path (GhostFrame); WindowsUpdateAssist Run key value (CopperDragon); ncobjapi.dll/wbemcomn.dll (Turla)
   - Source/quote: Detection lines of the Vates, GhostFrame, CopperDragon and Turla entries
   - Style rule: no mutex or file-name indicators. These are vendor-published IOC names reproduced as detection content; keep the behavior (VM serial console bound to a file, cron entry created by an unauthenticated session, boot-script edit plus self-restoring execInstalledOnly, sideloaded wbem DLL) and let the vendor pages carry the names.

31. **#31 [F11]** `2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates` — updated entries trimmed earlier analysis that the record summary does not mention
   - Source/quote: git diff HEAD on the eMudhra, kernel, Danfoss and Barracuda entries
   - eMudhra lost "If no update is available, OpenJDK gives two alternatives: delete the aliases ... or enable revocation checking" (OpenJDK page still says it); kernel lost the Go team sentence and "Citrix rates ... Critical"; Danfoss lost Coolworld's "third-party component outside its control" and the BSI/CSIRT Italia lines; Barracuda's patch sentence changed from "apply any patch that was not applied automatically and turn automatic patching on" to "confirm automatic patching is on" while Barracuda's page still says to apply the patch manually. `fields` names body, so the gate passes, but the removals are unrelated to each record's stated delta.

32. **#32 [F11]** `2026-11-11/ghostframe-esxi-post-exploitation-framework-tag-218` — GhostFrame entry quotes CVE-2026-0257 without linking the existing entry
   - Source/quote: https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/
   - entries/2026-05-30/cve-2026-0257-palo-alto-pan-os-globalprotect-pre-auth-authen carries the CVE; references[] lists only the Kaspersky and Qilin entries.

### Verdict

NEEDS_FIXES (truth: 16, editorial: 13, advisory: 3)

Whole-run notes: coverage otherwise looks complete against the window (KEV sweep dispositions hold: Barracuda updated, Outlook and Chromium new, Openwave and BroadWorks borderline-dropped; SonicWall MFA bypass, OpenSSH musl, Zyxel and Ivanti Connect Secure were already covered by in-window entries). Dedup is sound: no new entry shares a CVE with an existing entry, the Synology entry declares its predecessor in references[]. The three updated entries that missed same-day source revisions (eMudhra: Apple, Microsoft, Cisco; kernel: Ubuntu; Fortinet: FG-IR-26-265) are the highest-value fixes. The run record notes were spot-checked for truth and hold (KEV counts, Xen Orchestra version contradiction, sub-agent and run durations, sources_changed ids); the record claims no deep dive and no critical, consistent with the entries.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F4
  category: hallucinated-fact
  section: 2026-11-11/cve-2026-124194-outlook-forced-authentication-exploited-kev
  item: 'CVE-2026-124194 Outlook zero-day: "no source names ... the kind of credential taken" / NTLM "no cited source states it"'
  url_or_quote: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-124194
  summary: 'Summary ("no source names the actor, the victims or the kind of credential taken"), body ("No source names ... the kind of credential obtained"), Detection ("no cited source states it") and sourcing_note ("the NTLM hypothesis ... not from a source") are contradicted by the cited Microsoft record (MSRC API FAQ: "This vulnerability discloses a user''s NTLMv2 hash to the attacker who could use this to authenticate as the user.") and by the cited BleepingComputer article ("exploited in attacks to steal NTLM account hashes"). State that Microsoft says NTLMv2 hash disclosure, drop the "hypothesis" hedging, and sharpen Detection/action (NTLMv2 relay or crack).'
- code: F3
  category: claim-not-supported
  section: 2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates
  item: 'eMudhra: macOS command-line tools "keep trusting them until a future update" / "check again after every macOS update" / heise "macOS 27.3 ... not expected before December"'
  url_or_quote: https://support.apple.com/de-de/149555
  summary: 'The Apple page the entry cites three times (publication date now 10. November 2026) says: "Ab macOS 27.2.1 akzeptieren diese Befehlszeilenwerkzeuge diese Zertifikate nicht mehr" and that macOS 26.7.3 and 15.8.3 carry the protection too, and "Nachdem du auf macOS 27.2.1, macOS 26.7.3 oder macOS 15.8.3 aktualisiert hast, musst du diese Schritte nicht wiederholen." The tracker the entry also cites (emudhra.we-have-a-problem.com) says "Fixed in macOS 27.2.1, 26.7.3, and 15.8.3." Claims 88f3538fc1, e7160c47b1, 436c748caa and actions[0] (61b4eec292, "repeat it after each macOS update until the one that carries Apple''s own change") are stale; the update that was written this run on SonicWall did not pick this up. Cite Apple as of 2026-11-10, name the fixed macOS builds, drop the heise 27.3 claim.'
- code: F3
  category: claim-not-supported
  section: 2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates
  item: (low confidence) "Apple devices on 2026-10-19, with the G3 root following there on 2026-10-23"
  url_or_quote: https://emudhra.we-have-a-problem.com/
  summary: 'Claim 6e80875731 is cited to the tracker, BleepingComputer and the Apple page. Tracker: "blocked in Firefox and Chrome since the 17th of October, on Microsoft platforms since the 20th and on Apple products since the 22nd"; BleepingComputer: "Apple added protections on October 22". The Apple page as fetched carries no 19 or 23 October dates. Low confidence only because an earlier revision of the Apple page may have carried the dates.'
- code: F3
  category: claim-not-supported
  section: 2026-10-31/cve-2026-98432-linux-kernel-tcp-uaf-mptcp-remote-root
  item: 'Kernel UAF: "Ubuntu''s tracker, last updated 2026-11-07, ... 16.04 to 26.04 are still in progress" / takeaway "Ubuntu''s LTS kernels were not out on 2026-11-07"'
  url_or_quote: https://ubuntu.com/security/CVE-2026-98432
  summary: The cited Ubuntu tracker now reads "Last updated 10 November 2026" and lists 26.04 LTS "Fixed in 7.0.0-43.43", 24.04 LTS "Fixed in 6.8.0-149.149", 22.04 LTS "Fixed in 5.15.0-203.213"; only 20.04, 18.04 and 16.04 remain "work in progress". The entry was edited this run (Veeam) but still tells readers the Ubuntu LTS kernels are not out; headline ("Ubuntu 26.10 kernel out"), title and action[0] share the staleness. Claims 967f8237c1, 876946fbbf. Refresh as a correction/update on the entry and date the citation to the page (2026-11-10).
- code: F3
  category: claim-not-supported
  section: 2026-11-11/turla-cereal-exchange-server-c2-and-mail-collector-gov
  item: 'Turla Cereal: "could not determine the initial access method, so there is no CVE to patch against" / "With no external C2 and nothing to patch"'
  url_or_quote: https://web-assets.esetstatic.com/wls/en/papers/white-papers/turla-cereal-tricks.pdf
  summary: 'The clause (claim 08a969c360) is cited to the ESET blog post, which carries no initial-access statement. The white paper says: "We were unable to determine the initial access method. However, given that the Exchange servers are accessible from the internet, it is possible that they were breached by exploiting a vulnerability." The entry drops ESET''s hedge and converts "unknown" into "no CVE to patch against" / "nothing to patch" (claim 43e8cc112c), which no source states. Cite the white paper for the initial-access statement and keep ESET''s own wording.'
- code: F14
  category: quantifier-without-source
  section: 2026-11-11/microsoft-november-2026-patch-tuesday-preauth-9-8-rows
  item: '"seven unauthenticated network flaws rated CVSS 9.8" (title, headline, summary, first body sentence)'
  url_or_quote: https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-95882
  summary: 'The November 2026 MSRC CVRF lists further CVSS 3.1 9.8 AV:N/PR:N/UI:N rows with the same "in-network attacker calling arbitrary endpoints" FAQ as the DNS, DHCP and iSCSI rows the entry covers: DirectMusic CVE-2026-95882 and CVE-2026-95901, Media Foundation CVE-2026-96157, Windows Xbox Live Networking Service CVE-2026-112967 (plus Color Management CVE-2026-96067/96078 and Azure OpenAI CVE-2026-119990 at 9.8). The sourcing_note excludes "file-format parsers that need a user to open a file", which Microsoft''s records for DirectMusic, Media Foundation and Xbox do not say. "Seven" is the entry''s selection, not the release count: scope the title/summary ("seven ... in domain infrastructure and server roles") or cover the others. Claims 8d7f969c98, 0a6c5683c1, 1b194dd86f.'
- code: F14
  category: quantifier-without-source
  section: 2026-11-10/sap-november-2026-cna-records-four-unauth-cvss-10-rows
  item: 'Title: "Onapsis, which found two of them" (four CVSS 10.0 flaws)'
  url_or_quote: https://onapsis.com/blog/proxygate-cve-2026-89103-sap-netweaver-gateway-threat-advisory/
  summary: 'Onapsis says ICM2SHELL (CVE-2026-76964 and CVE-2026-89126) and PROXYGATE (CVE-2026-89103) were each "discovered and reported by the Onapsis Research Labs": three of the four CVEs. The title says two; the body ("Onapsis, which found and reported the Web Dispatcher, ICM and Gateway flaws") and the record summary say three flaws. Fix the title.'
- code: F3
  category: claim-not-supported
  section: 2026-11-11/qubole-vendor-aws-identity-assumes-integration-roles
  item: (low confidence) "Wiz found no tie to other reported activity ...; it does not know how the Qubole IAM users were compromised"
  url_or_quote: https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild
  summary: Claim 03c6457492 (and the sourcing_note "Wiz does not know how the Qubole IAM users were compromised") is cited to Wiz. The Wiz post says only "Wiz has not identified any ties between this campaign and other publicly reported activity" and that it has no insight into motivation; it does not state what it knows about the compromise of the IAM users. BleepingComputer writes "The report does not specify the exact method used to compromise the Qubole accounts". Reword to "does not say" and cite BleepingComputer.
- code: F4
  category: hallucinated-fact
  section: 2026-11-11/qubole-vendor-aws-identity-assumes-integration-roles
  item: 'summary: "the counts range from \"over a dozen\" to \"dozens\""'
  url_or_quote: https://sentra.io/blog/breaches/inside-the-qubole-supply-chain-attack
  summary: 'The summary puts "over a dozen" in quotation marks, but no cited page uses it: Sentra says "More than a dozen organizations" and "Dozens of Qubole customers"; BleepingComputer says "tens of companies". Use the source wording or drop the quote marks (claim a5815ddc82).'
- code: F4
  category: hallucinated-fact
  section: 2026-11-11/copperdragon-silentdelivery-fake-certificate-watering-holes
  item: (low confidence) "DLL sideloading of uncommon signed executables" / Detection "rarely abused signed executables"
  url_or_quote: https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/
  summary: Check Point says DarkWire "heavily relies on DLL sideloading as a primary execution technique, often abusing executables that are not widely observed among other threat actors in the wild"; "signed" appears nowhere in that section (claims 288fee62d6, 8d0436b428). Drop "signed".
- code: F4
  category: hallucinated-fact
  section: 2026-11-11/ghostframe-esxi-post-exploitation-framework-tag-218
  item: (low confidence) "edits the ESXi boot script /etc/rc.local.d/local.sh and /sbin/auto-backup.sh to survive reboots"
  url_or_quote: https://www.recordedfuture.com/blog/ghostframe-esxi-implant-settra-ransomware
  summary: 'Insikt: the implant persists by "modifying the ESXi boot script /etc/rc.local.d/local.sh ... The implant also executes /sbin/auto-backup.sh to preserve the modified configuration across reboots"; Insikt''s mitigation names changes to local.sh only. The entry (claim d2cdd1fc83, Detection, actions[0]) says it edits auto-backup.sh as well and tells hunters to look for changes to it. State that the implant executes auto-backup.sh.'
- code: F4
  category: hallucinated-fact
  section: 2026-11-11/confluence-dc-cve-2026-90436-apache-axis-remote-api-rce
  item: (low confidence) Exposure "a Data Center instance on 9.2.27 or earlier"; sourcing_note "Atlassian states no exploitation"
  url_or_quote: https://confluence.atlassian.com/security/cve-2026-90436-remote-code-execution-in-confluence-data-center-and-server-1874560038.html
  summary: Atlassian lists Confluence Data Center 1.x.x to 9.x.x as affected and 9.2.28 as the only fixed version ("patch ... to the latest version or one of the listed fixed versions"), so "9.2.27 or earlier" narrows the affected range (claim 986f9a06cc). The advisory also makes no statement about exploitation at all (neither "none" nor "some"); the sourcing_note says "Atlassian states no exploitation". Reword both.
- code: F4
  category: hallucinated-fact
  section: 2026-11-10/n-able-n-central-33-unpatched-flaws-public-pocs-offline
  item: '(low confidence) sourcing_note: "the CNA records do not state whether authentication is needed"'
  url_or_quote: https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122942
  summary: 'N-able''s CNA records carry CVSS 4.0 vectors that state the privilege requirement: CVE-2026-125883 and CVE-2026-125881 PR:N, CVE-2026-125878 and CVE-2026-91000 PR:L, CVE-2026-125882, -125879 and -125880 PR:H (EUVD-2026-122942, -122961, -122958, -122956, -122963, -122959, -122964). The scores in cves[] are CVSS 4.0, which the entry never says.'
- code: F4
  category: hallucinated-fact
  section: 2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack
  item: '(low confidence) Update section: "What is new is the patch statement and the wider population: BACS says security updates fixing the known flaws are available for the AK-SM 800A and 8xxA family"'
  url_or_quote: https://security-hub.ncsc.admin.ch/#/posts/13054
  summary: NCSC Switzerland's Cyber Security Hub advisory of 2026-10-13, which the entry cites, already says "Vendor firmware updates are available for the AK-SM 800A and fix the disclosed CVEs" and "Newer AK-SM 800A firmware enables Strict Session Control and mandatory HTTPS by default"; the entry has also carried Censys's 4.3.1 fixed-firmware statement since 2026-10-14. The patch statement is not new; the genuine delta is BACS's public SME-facing warning and user list. Same framing in the record summary and the new Defender-takeaway sentence (claim 8927156011).
- code: F3
  category: claim-not-supported
  section: 2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates
  item: '(low confidence) actions[2]: "Cisco''s remediation ... its eMudhra advisory (version 1.8)"'
  url_or_quote: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-emudhra-info-ScS22A1r
  summary: The Cisco advisory page now lists "1.9 Updated products under investigation, impacted, and not impacted ... 2026-NOV-10". The action cites version 1.8 and the update written this run did not read the revision. Re-read 1.9 and update the version and any changed product rows (claim 818a7fb237).
- code: F4
  category: hallucinated-fact
  section: 2026-11-11/vates-xen-orchestra-vsa-2026-062-auth-bypass-exploited
  item: (low confidence) "needs network reach to the interface and one unexpired token in the Xen Orchestra database"
  url_or_quote: https://docs.vates.tech/security-advisories/advisories/2026/vates-sa-2026-062/
  summary: 'Vates: the token collection "returns its first token; the provider authenticates as that token''s owner if it is unexpired", i.e. the first stored token must be unexpired, not any one (claim 77c784cb9f). Precision fix.'
- code: F5
  category: missing-citation
  section: 2026-11-11/adobe-connect-apsb26-191-five-unauthenticated-cvss-10-rows
  item: 'Defender takeaway: "rather than within Adobe''s 30-day priority window"'
  url_or_quote: https://www.adobe.com/trust/security/products/connect/apsb26-191
  summary: Neither the bulletin (it only says "priority 2") nor Adobe's severity-ratings page as fetched states a 30-day window; the sentence has no citation (claim 85aed99957). Cite Adobe's priority definition or drop the number.
- code: F8
  category: needs-more-research
  section: 2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates
  item: 'Update missed Microsoft''s 2026-11-10 revision: remaining eMudhra roots removed from Windows, Edge and the Trusted Root Program from 2026-11-16'
  url_or_quote: https://www.microsoft.com/en-us/msrc/blog/2026/10/microsoft-response-to-compromised-emudhra-certificate-authority-keys
  summary: 'The Microsoft post the entry cites carries "Update (November 10, 2026)": "Microsoft is removing the remaining eMudhra root certificates across its products and services, starting November 16, 2026" (10 roots from the Trusted Root Program and Windows; Edge and WebView2 remove default trust for emSign Root CA - G1, C1, ECC and Root TLS CA - G1; Azure Linux, .NET images and OpenJDK follow). The entry mentions only the October removals of seven certificates and Chrome''s 2026-11-16 SCT cutoff, and actions[1] covers only G3 and the seven October certificates. Windows/Edge fleets lose trust in G1-chained certificates five days from now, so this is the decision-relevant delta of the day; add it (with the Apple 27.2.1 fix and Cisco v1.9) to this update.'
- code: F8
  category: needs-more-research
  section: 2026-10-23/fortinet-hardening-release-fortios-fortimanager-fortimail
  item: FG-IR-26-265 (FortiAuthenticator, CVSS 9.1) not listed although sourcing_note says "only the unauthenticated rows scored 9.0 or higher are listed here"
  url_or_quote: https://fortiguard.fortinet.com/psirt/FG-IR-26-265
  summary: FG-IR-26-265 "An Incorrect Authorization vulnerability [CWE-863] in FortiAuthenticator may allow an attacker to bypass authentication and gain unauthorized access", CVSSv3 9.1 with vector AV:N/AC:L/PR:N/UI:N/.../E:F (functional exploit code), same fixed builds 8.0.4 and 6.6.11, published 2026-11-10 in the same feed. It meets the entry's own selection rule and is on the identity provider the entry already covers; the sourcing_note claim is therefore wrong as written. Add the row (or say the advisory does not state authentication) and correct the note.
- code: F8
  category: needs-more-research
  section: 2026-10-23/fortinet-hardening-release-fortios-fortimanager-fortimail
  item: (low confidence) CVE-2026-126253 FortiOS OSPF "unauthenticated attacker" without the adjacent attack vector
  url_or_quote: https://fortiguard.fortinet.com/psirt/FG-IR-26-267
  summary: FG-IR-26-267 scores 9.3 with CVSS vector AV:A (adjacent network), summary "unauthenticated attacker to broadcast LSA via specially crafted request". The entry, its Exposure line and the "internet-facing units first" action do not say that this row needs adjacency, which changes triage for internet exposure.
- code: F9
  category: surface-contradiction
  section: 2026-11-10/n-able-n-central-33-unpatched-flaws-public-pocs-offline
  item: (low confidence) cves[] types/vectors follow Huntress, N-able's CNA records say otherwise
  url_or_quote: https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-122958
  summary: CVE-2026-125878 is typed rce/"multiple OGNL injection flaws per Huntress", but N-able's CNA record (EUVD-2026-122958, 8.7, PR:L) describes "cross-site scripting ... Resource Injection"; CVE-2026-125879 is typed local privilege escalation while its CNA record (EUVD-2026-122959, 8.6) carries AV:N/PR:H and "Incorrect privilege assignment". The entry cites the CNA records only for -125883 and -125881 and does not surface the disagreement.
- code: F9
  category: surface-contradiction
  section: 2026-11-11/ivanti-epm-cve-2026-121653-unauthenticated-sqli-rce
  item: (low confidence) Cloud Services Application "the second record does not say which build fixes it"
  url_or_quote: https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-121155
  summary: 'EUVD-2026-121155 describes "version 5.0.8" as affected in prose but lists the structured product as "Cloud Services Application, patch: 5.0.8" (the first record uses the same "patch: 2024 SU8" field for the fixed build). The entry says the fixed build is unknown without surfacing that the record''s own fields disagree. Also CVE-2026-121683 is in title, summary and body but absent from cves[].'
- code: F9
  category: surface-contradiction
  section: 2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow
  item: (low confidence) supplier "received a demand \"not made concrete with an amount or deadline\"" next to PK Softech "no concrete ransom demand"
  url_or_quote: https://www.watson.ch/schweiz/datenschutz/664513749-nach-daten-klau-keine-loesegeldforderung-von-hackern-an-publica-softwarelieferan
  summary: watson.ch's lead and headline say no ransom demand reached the supplier or the Confederation ("gingen weder an diesen, noch an den Bund Lösegeldforderungen ein"); the Sepos spokeswoman's sentence ("Dies im Gegensatz zum Softwarelieferanten ..., dort allerdings nicht mit einem Betrag oder einer Frist konkretisiert") is read by the entry as "the supplier did receive a demand". PK Softech says "keine konkreten Lösegeldforderungen". The entry states the supplier received a demand as fact without a Contradiction line.
- code: F9
  category: surface-contradiction
  section: 2026-10-31/cve-2026-98432-linux-kernel-tcp-uaf-mptcp-remote-root
  item: (low confidence) body no longer mentions the severity dispute while cves[].cvss still does
  url_or_quote: https://kb.ciq.com/article/security-advisories/cve-2026-98432-mitigation
  summary: 'This run''s body edit deleted "Severity is disputed: the CNA scores it 9.8, upstream 8.1 with high attack complexity" (CIQ: "The kernel.org CNA scores the CVE 9.8 ... Upstream rates it 8.1 (important) with attack complexity high"; Sophos: Red Hat rated 5.9) and the Go team''s "not specific to MPTCP" sentence, while cves[].cvss still reads "upstream rates it 8.1 per CIQ". The record summary mentions only Veeam.'
- code: F7
  category: drop
  section: 2026-11-11/confluence-dc-cve-2026-90436-apache-axis-remote-api-rce
  item: (low confidence) Confluence DC Remote API RCE, Adobe Connect APSB26-191 and the Microsoft Patch Tuesday roll-up as routine patch-cycle items
  url_or_quote: https://confluence.atlassian.com/security/cve-2026-90436-remote-code-execution-in-confluence-data-center-and-server-1874560038.html
  summary: All three are unexploited with no public proof of concept; Confluence is reachable only with an opt-in, off-by-default setting (a listed `high` disqualifier), Adobe Connect on-premises has no stated constituency footprint, and the Microsoft rows are Microsoft-scored exploit-code-unproven (E:U) fixes inside the regular cycle with no mechanism for five of the seven. The entries argue for prioritisation inside the cycle, not for action beyond it. Consider dropping, or cut to two sentences.
- code: F16
  category: org-triage
  section: 2026-11-11/vates-xen-orchestra-vsa-2026-062-auth-bypass-exploited
  item: (low confidence) priority notable on Vates (exploited, vendor-Critical pre-auth Admin and root on XCP-ng hosts) and on SAP (four unauthenticated CVSS 10.0, working exploit with the researcher, patch Web Dispatchers first)
  url_or_quote: https://docs.vates.tech/security-advisories/advisories/2026/vates-sa-2026-062/
  summary: Vates states active exploitation of an unauthenticated management-plane bypass leading to code execution and root on hypervisors; by the `high` bar (plausible exposure plus a decision within 7 days) it looks under-called next to the exploited Chrome and Outlook entries rated `high`. The SAP entry (2026-11-10/sap-november-2026-cna-records-four-unauth-cvss-10-rows) has Onapsis stating a working unauthenticated RCE exploit exists and telling internet-facing Web Dispatchers to be patched first.
- code: F10
  category: missed-angle
  section: run-record
  item: (low confidence) Cisco critical advisories (Catalyst SD-WAN Controller, Secure Email Gateway, Meraki) named in the Patch Tuesday roundup, no disposition
  url_or_quote: https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2026-patch-tuesday-fixes-1-235-flaws-outlook-zero-day/
  summary: 'BleepingComputer''s 2026-11-10 roundup lists "Cisco released security updates for numerous products, including critical vulnerabilities Catalyst SD-WAN Controller, Secure Email Gateway, and Meraki"; the run record names Cisco BroadWorks, ISE and Brotli rows but no disposition for these, and no Cisco PSIRT source is among the attempted sources. Suggested search: "Cisco Catalyst SD-WAN Controller Meraki Secure Email Gateway critical advisory November 2026".'
- code: F12
  category: single-source-flag-missing
  section: 2026-11-11/synology-dsm-sa-26-19-preauth-sqli-auth-api-rsync-bypass
  item: '(low confidence) verification: multi-source on Synology SA-26:19 and Confluence CVE-2026-90436 (second source self-described as a restatement)'
  url_or_quote: https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1493/
  summary: The sourcing_notes say CERT-FR (Synology) and BSI CERT-Bund (Confluence) are "a restatement, not an independent assessment"; the vendor advisory is the only source. Use verification single-source (vendor primary) rather than multi-source, or name the carve-out.
- code: F18
  category: action-item-discipline
  section: 2026-11-11/vates-xen-orchestra-vsa-2026-062-auth-bypass-exploited
  item: (low confidence) Vates actions[1] restates Detection; eMudhra actions[0] is a five-tool task list
  url_or_quote: 'actions[1]: "On every Xen Orchestra instance that was reachable from an untrusted network, search the XCP-ng hosts for the attacker''s artefacts Vates lists ..."'
  summary: Vates actions[1] repeats the Detection paragraph (hvm_serial file, pivot2, cron.d files, ld.so.preload) plus reinstall/rotate from the Defender takeaway; GhostFrame actions[0] likewise repeats its Detection line. 2026-10-21/emudhra actions[0] chains Java, Python, Go, GitLab, SonicWall and macOS steps in one item and is not startable as one task. Split or trim.
- code: F11
  category: editorial-advisory
  section: 2026-11-11/vates-xen-orchestra-vsa-2026-062-auth-bypass-exploited
  item: 'attacker-chosen names as indicators: pivot2 VM, zz-ustar cron files (Vates); vmhostd-core path (GhostFrame); WindowsUpdateAssist Run key value (CopperDragon); ncobjapi.dll/wbemcomn.dll (Turla)'
  url_or_quote: Detection lines of the Vates, GhostFrame, CopperDragon and Turla entries
  summary: 'Style rule: no mutex or file-name indicators. These are vendor-published IOC names reproduced as detection content; keep the behavior (VM serial console bound to a file, cron entry created by an unauthenticated session, boot-script edit plus self-restoring execInstalledOnly, sideloaded wbem DLL) and let the vendor pages carry the names.'
- code: F11
  category: editorial-advisory
  section: 2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates
  item: updated entries trimmed earlier analysis that the record summary does not mention
  url_or_quote: git diff HEAD on the eMudhra, kernel, Danfoss and Barracuda entries
  summary: 'eMudhra lost "If no update is available, OpenJDK gives two alternatives: delete the aliases ... or enable revocation checking" (OpenJDK page still says it); kernel lost the Go team sentence and "Citrix rates ... Critical"; Danfoss lost Coolworld''s "third-party component outside its control" and the BSI/CSIRT Italia lines; Barracuda''s patch sentence changed from "apply any patch that was not applied automatically and turn automatic patching on" to "confirm automatic patching is on" while Barracuda''s page still says to apply the patch manually. `fields` names body, so the gate passes, but the removals are unrelated to each record''s stated delta.'
- code: F11
  category: editorial-advisory
  section: 2026-11-11/ghostframe-esxi-post-exploitation-framework-tag-218
  item: GhostFrame entry quotes CVE-2026-0257 without linking the existing entry
  url_or_quote: https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/
  summary: entries/2026-05-30/cve-2026-0257-palo-alto-pan-os-globalprotect-pre-auth-authen carries the CVE; references[] lists only the Kaspersky and Qilin entries.
```
