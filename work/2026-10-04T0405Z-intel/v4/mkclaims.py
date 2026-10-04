import yaml
SK="https://support.checkpoint.com/results/sk/sk1000171/"
CPB="https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-cve-2026-85102-and-a-management-pre-authentication-vulnerability-cve-2026-93616/"
HN="https://thehackernews.com/2026/09/check-point-warns-of-management-server.html"
BF="https://bishopfox.com/blog/weaponizing-check-point-management-cve-2026-93616"
GH="https://github.com/BishopFox/CVE-2026-93616-check"
KEV="https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
HEISEF="https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html"
NLT="https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data"
RN="https://retail-news.de/flink-datenschutzvorfall-kundendaten-phishing/"
C96="https://support.citrix.com/external/article/CTX697096/citrix-netscaler-adc-and-citrix-netscale.html"
C74="https://support.citrix.com/external/article/CTX697174/citrix-netscaler-adc-and-citrix-netscale.html"
CB="https://community.citrix.com/techzone-blogs/110_security-updates/understanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway/"
CG="https://community.citrix.com/techzone-blogs/110_security-updates/security-update-guidance-for-netscaler-saml-authentication-deployments/"
WT="https://watchtowr.com/intelligence/citrix-netscaler-zero-day-vulnerabilities-faq/"
U42="https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/"
CERTEU="https://cert.europa.eu/publications/security-advisories/2026-014/"
CERTAT="https://www.cert.at/de/warnungen/2026/9/kritische-sicherheitslucken-in-citrix-netscaler-adc-und-netscaler-gateway-aktiv-ausgenutzt-updates-verfugbar"
NCSCNL94="https://advisories.ncsc.nl/advisory?id=NCSC-2026-0394"
BC="https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/"
HUB="https://security-hub.ncsc.admin.ch/#/posts/13005"
ZNL="https://www.ncsc.nl/alerts/actief-misbruik-van-zeroday-kwetsbaarheden-in-zammad-update-nu"
D14="https://csirt.divd.nl/cases/DIVD-2026-00014/"
D15="https://csirt.divd.nl/DIVD-2026-00015"
C89="https://csirt.divd.nl/cves/CVE-2026-102489"
C90="https://csirt.divd.nl/cves/CVE-2026-102490"
ZAM="https://community.zammad.org/t/take-care-local-privilege-escalation-cve-2026-102490-is-reported-as-being-actively-exploited/21297"
CYB="https://cyberpress.org/new-citrix-netscaler-saml-flaw-triggers-crashes-and-suspected-exploitation-attempts/"
HNS="https://www.heise.de/en/news/Netscaler-admins-beware-Zero-day-causes-crashes-and-code-execution-11474996.html"
ACSC="https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/critical-vulnerabilities-in-citrix-netscaler-adc-and-citrix-netscaler-gateway-products"
HG="https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat"
HP="https://www.huntress.com/blog/parks-recreation-platform-webshell-attack"
ok="ok"
R={}
def a(i,v,u,p): R[i]=(v,u,p)
# Check Point
a("793e3cbd50",ok,BF,"Bishop Fox 2026-10-01: 'Every step runs over one port, TCP 19009'; indicators: 'the chain we validated does not touch the code path the vendor's indicators watch'; scanner tool linked")
a("b35b30b500",ok,CPB,"'we observed a handful of pinpointed attacks on July 23, 2026'; sk1000171 R82.20 Security Hotfix + Jumbo takes 45/127/170/192; BF: 'Restrict TCP 19009 ... Check Point's primary mitigation'")
a("7a5d1ff534",ok,SK,"'The fix is also included in: JHF R82.10 starting from Take 45 ... R82 Take 127 ... R81.20 Take 170 ... R81.10 Take 192'; 'a LivePatch is not be available for this issue'")
a("4e299eebea",ok,SK,"'Make sure that access to port TCP/19009 is only possible from Trusted IP addresses ... make sure your Trusted Clients are limited to trusted internal IP addresses'")
a("128a418027",ok,BF,"Hunting IoCs: '/etc/cron.d ...', 'authorized_keys and the usual startup paths', 'Anything new under $FWDIR/conf/SMC_Files'; second indicator 'leaves neither the ERROR line nor a ../'")
a("78daf46b12",ok,SK,"sk1000171: CVSS 9.8; affected R82.20, R82.10 Take 44 or lower, R82 126, R81.20 166, R81.10 190 (EoS), R80-R81 EoS; fixed R82.20 Security Hotfix + takes; KEV added 2026-09-22")
a("232f4ddbd2",ok,SK,"'allows an unauthenticated attacker to upload and execute arbitrary scripts on the Check Point Management Server'")
a("ba8c9bedc1",ok,CPB,"'allows an attacker to execute a script from an arbitrary path and load an arbitrary Java class'")
a("dcebb82077",ok,CPB,"'we observed a handful of pinpointed attacks on July 23, 2026'; 'newly discovered zero-day vulnerability in Security Management'")
a("1fbe34e55c",ok,SK,"'Because of the nature of the fix, a LivePatch is not be available for this issue.'")
a("83b9e22a45",ok,HN,"'Check Point says those LivePatch takes do not fix CVE-2026-93616'; LivePatch Take 28, or Take 29 on R82.20, fixed CVE-2026-91843")
a("11edb1c7e8",ok,KEV,"CVE-2026-93616 dateAdded 2026-09-22 (catalogVersion 2026.10.02 fetched this pass)")
a("66e8085052",ok,CPB,"CVE-2026-85102 'released fixes on September 9'; 'Starting September 12, 2026, we observed a wave of exploitation attempts against Spark customers'")
a("5c80850171",ok,SK,"'Check for these two indicators of compromise on every Security Management, Multi-Domain ... SmartEvent Server'")
a("e8578426a9",ok,BF,"'whose crash signature, an over-long username next to a core dump, is the advisory's first indicator, not evidence of this traversal' (CVE-2026-91843); sk: core dump at the same time")
a("071a0ff3c7",ok,BF,"Second indicator 'fires only when an upgrade-tools load fails, which makes it a weak net both ways'; 'The vendor's second indicator watches for traces of [the upgrade-service traversal]'")
a("5f076697df",ok,BF,"'Restrict TCP 19009 to trusted management hosts. Check Point's primary mitigation'; Trusted Clients list 'emits an implied rule'")
a("a3a64f86cc",ok,BF,"'Execution runs as root inside the process that holds your policy and internal CA. On any box that was exposed and unpatched, plan for credential and certificate rotation'")
a("f878cc9a1e",ok,SK,"'Affected Products: Security Management Server, Multi-Domain ..., Log Server, Multi-Domain Log Server, SmartEvent'; Not Affected: 'Smart-1 Cloud (fix is already applied)', Firewall Appliances, Spark Firewall")
a("dcd09d8b36",ok,SK,"Affected Versions: R82.20; R82.10 Take 44 or lower; R82 Take 126; R81.20 Take 166; R81.10 Take 190 (EoS); R80, R80.10, R80.20, R80.30, R80.40, R81 (all EoS)")
a("c47d488b88",ok,SK,"'Download the R82.20 Security Hotfix'; JHF R82.10 from Take 45, R82 Take 127, R81.20 Take 170, R81.10 Take 192")
a("ad6b5346e2",ok,CPB,"Derived from 'observed a handful of pinpointed attacks on July 23, 2026' and the 2026-09-22 fix date; Bishop Fox: 'treat it as though it's already compromised' if reachable")
a("e97e2f6ef2",ok,BF,"'We reproduced the attack end to end against unpatched R81.10 and R82.10 lab servers, confirming execution as root on both. Every step runs over one port, TCP 19009.'")
a("7fd49c3889",ok,BF,"authenticateRemoteApplication 'reads the CN= half ... without checking that a certificate was presented'; cron.d overwrite runs as root, 'No trigger request is needed'; downloadRawFile reads output")
a("6b960579cf",ok,BF,"'We confirmed additional attack vectors from the same write primitive'; two listed; 'Closing any single one would leave the others standing.'")
a("bdf67428aa",ok,BF,"'The hotfix closes three'; 'Either fix alone breaks the chain'; 'Check Point remediated more than it described.' (bytecode diff of Take 45)")
a("647afa3052",ok,GH,"'The tool does not execute code on the target and does not detect prior compromise.'; BF: 'reports patch state from outside with one benign request'")
a("4981327ddf",ok,BF,"'It fires only when an upgrade-tools load fails'; 'The route in this post never calls that service, so it leaves neither the ERROR line nor a ../'; 'A genuine upgrade can trip the grep'")
a("9851829d8e",ok,BF,"Hunting IoCs paths; 'A scheduled hash check can miss the change entirely ... restore the originals byte for byte. Pair file checks with execution telemetry, cron reload events, and an alert on the CPM Java process spawning a shell.'")
a("e1156cffb3",ok,BF,"'The second is a permissions setting, not a rule base entry, so a rule base audit alone can miss it.'")
a("b2011a4af1",ok,BF,"Only link to a tool is the GitHub detection tool; PoC script described ('Our proof-of-concept script returned uid=0') but not linked")
a("6914180c1a",ok,BF,"Follows from second indicator never reached and first being CVE-2026-91843's signature; BF: 'primitive is an arbitrary root write ... file-integrity monitoring rather than a log grep'")
a("052e98c83a",ok,BF,"Record summary matches the section (end-to-end chain over TCP 19009, scanner, second indicator not firing, first indicator = separate CVE, three defects, FIM hunting)")
# Flink
a("a083780bba",ok,NLT,"Summary consistent with body; NL Times 'contacting customers and employees directly'; heise 'mindestens 10.000 Kunden'; Oct. 2 deadline (note: sell-threat is heise's reading only, advisory F11)")
a("ed614997f9",ok,NLT,"'Flink is headquartered and operates in Germany ... started up and wound down operations in both Austria and France'; 'serves dozens of municipalities in the Netherlands'")
a("b9a3d580ad",ok,HEISEF,"'ein eigenes, eigentlich internes Bestellsystem ... in den Order Hubs ... kleine, dezentrale Lager in Städten ... Lieferung in unter einer halben Stunde' (paraphrase conflates system and warehouses, advisory)")
a("432c018c64",ok,RN,"'gelangte eine unbefugte Person mithilfe kompromittierter Zugangsdaten in eines der internen Systeme des Lieferdienstes'; customer e-mail 'der Redaktion vorliegenden'")
a("c61c56a02f",ok,HEISEF,"'ein einzelner dieser Order Hubs angegriffen, dieser wurde auch schon identifiziert und der unberechtigte Zugriff unterbunden'")
a("e6ebacc5e0",ok,HEISEF,"'Flink tritt grundsätzlich nicht mit Kriminellen in Kontakt ... Flink auch in diesem Fall tatsächlich gar nicht reagiert'")
a("8bb8cf5ba6","F3",NLT,"NL Times: 'The LPG Group is not particularly well-known' (carries NL Times half); the 'and heise' half ('bisher recht unbekannte Bande') is on the heise page, not linked at this clause (low confidence)")
a("35a067c10e",ok,NLT,"heise: 'Wenn nicht, würden die Daten ... im deep web verkauft'; NL Times: 'delete all user data if the company itself pays ... 100 ETH ... A deadline of Oct. 2 was mentioned'")
a("34e9d7379a",ok,HEISEF,"'Die Mails wenden sich namentlich und mit einem Flink-ähnlichen gefälschten Absender an die Kunden, sodass diese wohl leicht verunsichert werden könnten.'")
a("b0c4b9c07b",ok,HEISEF,"'Name, Lieferadresse, E-Mail-Adresse und Telefonnummer ... Im Einzelfall ... Lieferhinweise wie das Stockwerk'; 'Passwörter, Zahlungsdaten, Kreditkarteninformationen und Bankdaten sollen ... nicht ... in die Hände gefallen sein'")
a("cab7161efa",ok,NLT,"'\"But I haven't seen individual consumers being approached before,\" said Takkenberg in an interview with NOS'")
a("e44d6b79f9",ok,HEISEF,"'Datenschutzbeauftragte des Landes Berlin ... informiert. Externe IT-Forensiker'; 'Anders als ursprünglich gemeldet hat Flink ... bisher nicht das BSI eingeschaltet.'")
a("364b6895f3",ok,NLT,"'Flink has reported the matter to the German Data Protection Authority, and has filed reports with police there and in the Netherlands'")
a("75ef6c8c3f",ok,HEISEF,"'wandten sich die Angreifer zunächst an Flink direkt und forderten Geld in Form der Kryptowährung ETH. Wenn sie bezahlt würden ... würden die Daten gelöscht.'")
a("1637cb4923",ok,HEISEF,"'Daher wandten sich die Kriminellen nun direkt an die Kunden'")
a("5b1050238f",ok,NLT,"NL Times '0.005 ETH ... 11.80 euros', '100 ETH, which is just shy of 237,300 euros'; heise 'mindestens 10.000 Kunden' (NL), 'etwa 230.000 Euro'; Germany scale unclear; Flink: customers and employees")
a("31198ccea9",ok,NLT,"'Pim Takkenberg said the attempt ... as if it were a crowdfunding campaign is exceptional. Hacker group Shinyhunters did extort Dutch higher education institutions that were the clients of a hacked software system.'")
a("ffd7bc4291",ok,HEISEF,"'über eine Abuse-Mitteilung beim ... Mailprovider die Flut der Schreiben ... eingedämmt'; 'nur rund 150 Mitteilungen von Kunden'; Germany count hard to estimate")
a("9107100556",ok,None,"Editorial takeaway framing; no factual claim beyond cited body")
a("66d56675e0",ok,HEISEF,"Derived lesson: heise 'Kriminelle wandten sich nun direkt an die Kunden', spoofed Flink-like sender; Flink: do not respond, report to police")
a("e3ccc2e1ae",ok,HEISEF,"Derived from heise 'eine Art kriminelles Crowdfunding' and NL Times Takkenberg 'as if it were a crowdfunding campaign'")
a("41ab64aee9",ok,RN,"'Flink hat am Freitag Kunden per einer der Redaktion vorliegenden E-Mail ... informiert ... unbefugte Person mithilfe kompromittierter Zugangsdaten'; page dated 2026-09-25")
a("a55fdec48f",ok,HEISEF,"'gingen dort bei mindestens 10.000 Kunden Erpressermails ein'; RETAIL-NEWS gives no detail on which credentials or MFA")
a("b4ec912a1a",ok,NLT,"Flink: 'criminals are currently attempting to exploit this incident by contacting customers and employees directly and requesting payments'")
a("30f64b4568","F3",NLT,"NL Times carries its own reading ('delete all user data if the company itself pays'); the heise half ('sum customers are to raise') is not on the cited page, heise not linked at this clause (low confidence)")
a("e7dc519350",ok,RN,"Record summary matches section: RETAIL-NEWS compromised credentials, 10,000 figure now customers, two readings of 100 ETH")
# 88771
a("3613aefa62",ok,C74,"Summary consistent with CTX697096 and CTX697174 (CVE-2026-88779 fixed in 14.1-73.41/13.1-64.28); Mandiant/Unit 42 items verified in earlier sections")
a("1f570a7718",ok,C74,"'NetScaler ADC and NetScaler Gateway 14.1-73.41 and later releases ... 13.1-64.28 and later'; CB: 'upgrade your deployment again' for SAML SP/IdP; CTX697096 fixed builds .37/.23")
a("f078b476fb",ok,C74,"Fixed builds 14.1-73.37/13.1-64.23/13.1-37.279 (CTX697096) and the later .41/.28/.282 for SAML-configured; watchTowr: 'show ns variable' caveat, 13.1-64.24")
a("49aa0d8eff",ok,"https://cloud.google.com/blog/topics/threat-intelligence/defending-against-active-exploitation-of-citrix-netscaler-adc-and-gateway-appliances","GTIG: 'Halt HA synchronization ... Disable configuration synchronization until both nodes have been validated'; Unit 42 artifacts in entry body")
a("5e4c8a48ee",ok,"https://www.tenable.com/blog/frequently-asked-questions-about-reported-citrix-netscaler-zero-day-vulnerabilities","Tenable FAQ: 12.1 and 13.0 end of life, no security updates, Citrix has not said whether affected (cited in the 2026-09-30 section)")
a("48ab05cd03",ok,WT,"'exploited as zero-days, before any fix existed. Citrix confirmed both and released fixed builds on September 27, 2026 in security bulletin CTX697096'; bulletin lists eight CVEs")
a("69be7f2e4c",ok,C96,"'Exploits of CVE-2026-88771 and CVE-2026-88772 on unmitigated NetScaler deployments have been observed.'")
a("30bb01b9e8",ok,KEV,"CVE-2026-88771/88772 dateAdded 2026-09-27; requiredAction cites BOD 26-04 and 'Forensics Triage Requirements'; forensicTriage: Yes")
a("ff0f929be7",ok,CERTEU,"'Citrix has confirmed active exploitation of these 2 critical vulnerabilities in the wild'; 'CERT-EU strongly advise to run a compromise assessment on any internet-facing appliance'; 27/09/2026")
a("cb05e92189",ok,BC,"admins 'advising them to shut down their NetScaler appliances'; 'NCSC-NL reportedly sent a pre-notification'; 'declined to confirm the notification'; no CVE IDs or Citrix advisory yet")
a("f78239f07d",ok,NCSCNL94,"NCSC-2026-0394 revision 1.0.0 'Initiele versie' 27-09-2026 16:55")
a("375d1894db",ok,WT,"'No attribution has been made public. Historically, NetScaler vulnerabilities have been exploited by both state-sponsored groups and ransomware operators.'; table lists CVE-2023-4966, CVE-2025-5777")
a("8f9351d61d",ok,WT,"'Appliances patched for CVE-2026-19490 remain vulnerable to CVE-2026-88771 and CVE-2026-88772 unless they run one of the fixed builds above.'")
a("648420dd0b",ok,WT,"'Citrix has not published a workaround for either vulnerability, so upgrading is the only fix.'")
a("bd5077c6f6",ok,WT,"'Capture logs, a snapshot, a support bundle and a core dump from each exposed appliance'; Unit 42: 'A NetScaler VPX instance snapshot', support bundle, packet engine core dump")
a("dae7c16c7a",ok,KEV,"KEV requiredAction: 'ensuring compliance with ... Forensics Triage Requirements'; notes 'Customers must conduct forensic triage as directed by BOD 26-04'")
a("fca670b72b",ok,WT,"'Run the IOC scan on the NetScaler Console Security Advisory page (version 14.1-73.36 or later, with telemetry enabled), or ask Citrix Support ... Citrix warns that the IOCs do not cover every technique'")
a("05b2a64afd","F3",CERTAT,"CERT.at page (27. September 2026) covers only its own advisory; it has no 'perimeter VPN and remote-access layer' statement and does not mention CERT-EU or NCSC-NL (low confidence)")
a("d31e164167",ok,HUB,"NCSC-CH hub post 13005 'created': '2026-09-28T05:39:47Z'")
a("ffff8517f1",ok,C96,"'CWE-20: Improper Input Validation | CVSS v4.0 Base Score: 9.5'; 'All NetScaler ADC and NetScaler Gateway deployments (Default configuration / No additional feature required)'")
a("c243414a20",ok,C96,"'CWE-119 ... Base Score: 9.5'; 'DTLS configuration enabled ... (Note: Enabled by default on VPN vServer)'; 'vulnerable if DTLS is not explicitly disabled'")
a("ef28f1a35c",ok,None,"Framing sentence; no factual claim")
a("1828124b39",ok,C96,"CVE-2026-88773 9.3 smuggling; 88774 7.0; 88775/76/77 8.8 (Gateway/AAA, Oracle LB, non-HTTP L7); 88778 8.8 'apply the TCP configuration change' Enhanced ISN Generation")
a("c2261fa5ca",ok,WT,"'On 13.1, run show ns variable first: if it returns any variables, use 13.1-64.24 to avoid a known reboot loop'; CTX697096 builds 14.1-73.37, 13.1-64.23, 14.1-73.37 FIPS, 13.1.37.279")
a("4b4f4ff745",ok,C74,"CTX697174 (2026-10-03): CVE-2026-88779, SAML SP/IdP precondition; fixed 14.1-73.41/13.1-64.28 (builds above .37/.23 not fixed)")
a("187baa5776",ok,"https://labs.watchtowr.com/oh-look-the-foot-gun-went-off-again-citrix-netscaler-preauth-command-injection-cve-2026-88771/","watchTowr: 'pitboss PPE unexpectedly died NSPPE;...' in login username reaches the log-parsing script; 'not limited to a single endpoint'")
a("573116ad17",ok,"https://cloud.google.com/blog/topics/threat-intelligence/defending-against-active-exploitation-of-citrix-netscaler-adc-and-gateway-appliances","GTIG: DTLS handshake-failure 'Internal Error' syslog line, packet-engine termination and watchdog line as artifacts of CVE-2026-88772 exploitation")
a("4a1248e2c5",ok,C96,"'DTLS configuration enabled ... (Note: Enabled by default on VPN vServer)'; 'A NetScaler Gateway is vulnerable if DTLS is not explicitly disabled'")
a("55d99d951c",ok,CB,"'Citrix has observed targeted attacks on unmitigated NetScaler deployments which can lead to Denial of Service'; CTX697174: SAML SP/IdP precondition, 'Memory overflow vulnerability leading to Denial of Service'")
a("a2627c3438",ok,CG,"'This issue is independent of the vulnerabilities disclosed in CTX697096.' (published 2026-10-02T21:35+02:00)")
a("970de6ef4c",ok,CB,"'If you upgraded ... CVE 2026-88771 through CVE 2026-88778 ... and ... meet the preconditions ... please upgrade your deployment again'")
a("b153c841b0",ok,C74,"14.1-73.41; 13.1-64.28; 14.1-FIPS 14.1-73.41 FIPS; 13.1-FIPS and 13.1-NDcPP 13.1-37.282")
a("3b60bd91ae",ok,C74,"Follows: CTX697096 fixed .37/.23 vs CTX697174 affected 'BEFORE 14.1-73.41 / 13.1-64.28'")
a("25a93814d2",ok,C74,"Record summary matches the section (CTX697174, SAML-triggered overflow, targeted attacks, upgrade again to .41/.28/FIPS)")
# Zammad
a("f97c742eab",ok,ZNL,"NCSC-NL: 'Beide kwetsbaarheden worden actief misbruikt'; 'De tweede kwetsbaarheid (CVE-2026-102490) is nog niet opgelost'; DIVD: 'two zero-days in Zammad'")
a("22fc75a5db",ok,ZAM,"Zammad: 'only possible on Zammad 6.5 and older'; 'hardened ... included in Zammad 7.2.0'; 'cannot confirm the vulnerability'; KEV 2026-10-02 both CVEs; NCSC-NL exploited since 21 Sep")
a("5d7305f8c5",ok,ZAM,"'Update to Zammad 7.2.0, the current stable release.'; NCSC-NL: copy application and network logs first; DIVD log check script")
a("c787a2603b",ok,D14,"'Thanks to proper network segmentation ... we were able to stop the attackers from going deeper'; NCSC-NL: second flaw not yet fixed")
a("9e31060113",ok,C89,"CVE record: Base score 8.7 (UI:P), chained 9.4; affected '>= 6.3.0 to < 6.5.4'; KEV 2026-10-02; Zammad: only 6.5 and older, 7.0+ not affected")
a("9349fe34a8",ok,C90,"CVE record: Base score 8.5 (AV:L, PR:L), chained 9.4; 'All versions of Zammad including the latest alpha'; KEV 2026-10-02; Zammad cannot verify")
a("f2e531b28b",ok,D14,"Timeline '21 Sep 2026 First access'; Statement #4: 'two zero-days in Zammad that together allowed session hijacking, remote code execution and privilege escalation ... to root, in seconds'")
a("e08e502feb",ok,D14,"'From there they could access other services and exfiltrate data'; segmentation 'stop the attackers from going deeper'; 'volunteer data got out, such as DIVD email addresses and possibly contact details'")
a("b2d4026edc",ok,D14,"'attacker's scripts contain notes where the agent justifies its own actions'; 'We see no link to any known public threat actor'")
a("a03b8b036c",ok,D15,"'Zammad versions 6.3.0 to 6.5.4 ... session hijack ... remote code execution as the zammad user ... also present in version 7.0.0 to 7.1.3, but not exploitable due to environment conditions'")
a("5bf3603018",ok,ZNL,"'maakt het mogelijk dat een aanvaller zonder in te loggen op afstand schadelijke code kan uitvoeren'")
a("e86f7e914c",ok,C89,"'Base score 8.7 - HIGH' vector CVSS:4.0/.../UI:P/...")
a("b4ed953885",ok,C90,"Description: 'All versions of Zammad including the latest alpha enable the local zammad user to escalate privileges to root'; chained base score 9.4")
a("26e44287d0",ok,ZNL,"'kans op misbruik en de mogelijke schade zijn hoog'; 'sinds 21 september 2026 actief misbruikt'; update only for the first; 'nog niet opgelost'")
a("8d3bc89b4b",ok,D15,"Patch status Available; 'upgrade to version 7 of Zammad or to take it offline'; 'DIVD is actively scanning and alerting owners of vulnerable Zammad instances'")
a("38e5f00699","F3",ZAM,"Zammad page carries 'only possible on Zammad 6.5 and older' and '7.0 and later are not affected' but not the 'per DIVD and NCSC-NL' 6.3.0 to 6.5.4 range; DIVD/NCSC-NL not linked at this clause (low confidence)")
a("efd79180b7",ok,D15,"'download our log check script ... to check your Zammad logfiles for Indicators of Compromise'")
a("02771335ff",ok,ZNL,"'Maak voor het installeren van de update een kopie van de applicatie- en netwerklogs'")
a("ac6baa75e9",ok,D15,"Products: Zammad; Versions listed; self-hosted inferred from log paths /var/log/zammad and nginx in DIVD script")
a("d415ac24c9",ok,ZAM,"Negative claim: neither DIVD, NCSC-NL nor Zammad statement addresses hosted Zammad")
a("e2bbea9661",ok,D15,"DIVD page lists only the log-check script; script content (fetched) greps ERROR lines for session material and says 'investigate ... unfamiliar processes and files'; no process/network IoCs")
a("1f9a7a98ab",ok,ZNL,"NCSC-NL: 'aanvaller het systeem overnemen, gegevens bekijken, aanpassen of verwijderen en het systeem gebruiken voor verdere aanvallen'; DIVD segmentation; Zammad: 6.5 and older receive no security fixes")
a("28dc2313a7",ok,KEV,"Both CVEs dateAdded 2026-10-02; shortDescription 'This vulnerability can be chained with CVE-2026-102490/102489'")
a("662005ff4e",ok,ZAM,"'Exploitation is only possible on Zammad 6.5 and older, because of the runtime environment those versions use'; 'Zammad 7.0 and later are not affected'; 'included in Zammad 7.2.0'; 'current stable release'")
a("3ef1010d4e",ok,ZAM,"'DIVD has not given us any technical details about this vulnerability'; 'report to us on 24 September 2026, followed by public scanning and disclosure on 26 September 2026'")
a("195d515716",ok,ZAM,"'We first received a report about this issue in August 2026 and analysed it then.' (under the CVE-2026-102489 heading)")
a("33a2b4edb9",ok,ZAM,"Record summary matches the update section (KEV 2026-10-02; Zammad statement; August 2026 report)")
# 88779
a("e74d8bce49",ok,CB,"'Citrix has observed targeted attacks on unmitigated NetScaler deployments'; CG: 'independent of the vulnerabilities disclosed in CTX697096'")
a("db42895391",ok,C74,"CTX697174 table: memory overflow, SAML SP OR IdP precondition, CVSS 8.7 (AV:N/PR:N/VA:H); blog: attacks observed, DoS; KEV json (this pass) has no CVE-2026-88779")
a("26a647db4c",ok,CB,"'add authentication samlAction' / 'add authentication samlIdPProfile'; GDL: 'show appfw signatures ... needs to be at least v24'; ranges '>= 14.1-73.37 and < 14.1-73.41'")
a("06b37367c7",ok,CG,"'If you are currently experiencing the impact from this issue, please contact Citrix support.'; Cyber Press: 'preserve logs and crash artifacts before restarting affected devices'")
a("8163bd6e31",ok,C74,"CVSS v4.0 8.7; affected 14.1 BEFORE 14.1-73.41, 13.1 BEFORE 13.1-64.28, 14.1-FIPS BEFORE 14.1-73.41 FIPS, 13.1-FIPS/NDcPP BEFORE 13.1-37.282")
a("d7c87f0a1a",ok,C74,"'CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:H'; 'This bulletin only applies to customer-managed'; 'must be configured as a SAML SP OR SAML IdP'; dated 2026-10-03")
a("9f233963c9",ok,CB,"'Citrix has observed targeted attacks on unmitigated NetScaler deployments which can lead to Denial of Service ... we have not identified an impact on the integrity of customer data'")
a("58e6cfc748",ok,CG,"'This issue is independent of the vulnerabilities disclosed in CTX697096.'")
a("9186b4a224",ok,CB,"'If you upgraded ... with one of the updated software releases identified in [CTX697096] ... please upgrade your deployment again with the software released as part of [CVE-2026-88779 bulletin]'")
a("80a625e4a8",ok,C74,"14.1-73.41; 13.1-64.28; 14.1-FIPS 14.1-73.41 FIPS; 13.1-FIPS and 13.1-NDcPP 13.1-37.282")
a("4785385451",ok,CB,"'Global Deny List signatures can help to mitigate the vulnerability. Citrix recommends upgrading'; '>= 14.1-73.37 and < 14.1-73.41'; '>= 13.1-64.23 and < 13.1-64.28'")
a("cd31a1d344",ok,CYB,"'running patched releases, including version 14.1-73.37'; 'crash the nsaaad authentication service'; 'command intended to download a script ... did not succeed'; 'payload delivered through the username field'")
a("4c6cdfd5de",ok,HNS,"Beaumont: 'on one of the honeypots it's running a downloaded (malware) binary. Both [honeypots] were patched'; 'the watchTowr Labs team has now successfully reproduced this vulnerability.'")
a("d4a1afd069",ok,ACSC,"'A remote attacker exploiting the issue may induce system crashes, denial of service and potential exploitation. ASD's ACSC is aware of impacts to Australian organisations.'")
a("8f92b52871",ok,KEV,"KEV catalogVersion 2026.10.02 (dateReleased 2026-10-02T15:19Z): no CVE-2026-88779 entry; no cited page confirms code execution beyond the honeypot/reproduction claims")
a("58a78e2cc1",ok,C74,"'Secure Private Access Hybrid deployments using NetScaler instances are also affected'; 'must be configured as a SAML SP OR SAML IdP'; 'inspecting their NetScaler configuration for entries'")
a("20b8043e2c",ok,CB,"'SAML authentication in conjunction with Gateway or AAA functionality'; configuration entries 'add authentication samlAction' / 'add authentication samlIdPProfile'")
a("be9c65fc4d",ok,CYB,"Cyber Press and heise describe administrator reports of crashes/reboots; 'Citrix gives no detection guidance' is true of the Citrix pages read but is not on these two pages (advisory F11)")
a("5e0c2201a8",ok,CYB,"'Reports of reboots alone should not be treated as proof of compromise, but the combination of active scanning, malformed authentication traffic, and appliance crashes warrants incident-response handling'")
a("363e6d42d3",ok,None,"Framing sentence introducing third-party reporting")
a("fd97aa4056",ok,HNS,"heise: 'The exploit can likely be executed by sending a massive number of SAML requests'; Cyber Press: 'failovers or full appliance reboots', nsaaad crashes")
a("667acbee7d",ok,CB,"'Global Deny List signatures can help to mitigate ... Citrix recommends upgrading to the following software versions containing the fix'")
a("cf75da4c0d",ok,CYB,"Crashes reported 'running patched releases, including version 14.1-73.37'; Citrix scopes to DoS; code execution unconfirmed")
# ChatGPT
a("2c7b5ca0a6",ok,HG,"'attacker-created Custom GPT' -> Google Sites ClickFix -> MSI -> Canon-signed host sideloads malicious DLL -> RAT")
a("49d5362d99",ok,HG,"'In some of the incidents ... searched on Google for \"chatgpt.\" A sponsored result then led them to the Custom GPT'; 'at least 40 incidents ... two ... came through a Custom GPT instance'")
a("55b5986bf6",ok,HG,"'rules and URL filters that look for a dotted IP address never see one'; 'installs it silently with msiexec /qn /norestart in a hidden window, and then deletes itself'")
a("cf22ea502a",ok,HG,"'remote desktop sessions ... camera ... microphone and system audio ... advanced search'; 'DNS-over-HTTPS through Cloudflare, Google, and Quad9 ... so they never appear in local DNS logs'")
a("da1d39150d",ok,HG,"'taken down as of September 25'; 'on September 27 ... new Custom GPT'; Stardock host; NuGet package Build.dat; 'strips the Mark-of-the-Web'; 'freshly obfuscated on every request'; RAT 'exact same file'")
a("38fccbfb3f",ok,HG,"'Detections tied to Canon or Stardock names will miss the next swap. The behaviors (so far) carry over:'")
a("72d903865c",ok,HG,"Carry-over list: 'PowerShell launching msiexec on a GUID-named MSI in %TEMP%'; 'A signed app started by msiexec from a fake product folder'; 'A Run value and scheduled task that share one name and come back when deleted'")
a("ab01c27a52",ok,HG,"'Delete one while the implant is running and the script puts it back within a few minutes. Kill the process first, then remove both.'")
a("d395faf728",ok,HG,"'Starting late September'; 'In some of the incidents ... searched on Google for \"chatgpt.\" A sponsored result'; 'Attackers titled this Custom GPT \"Plus 5.6\"'; chatgpt.com domain")
a("bad5568119",ok,HG,"'\"Service Availability Notice\" ... \"backup domain\"'; Google Sites page 'presents as a CloudFlare CAPTCHA check and delivers a ClickFix attack'")
a("b311360bdd",ok,HG,"'Advanced Printer Configuration Reader'; Canon-signed COTFileReadApp.exe; ceiinfolog.dll 'modified and patched to load rdCore.dll'; .wav 'rolling single-byte XOR'")
a("88af8fb781",ok,HG,"Stage 5: AMSI bypass, 'ntdll unhooking', anti-VM checks, 'Hosting the .NET runtime (CLR v4.0.30319)'; monitor.raw 'custom archive' holding script and RAT")
a("d1e016c764",ok,HG,"'Every 150 seconds, the script checks for that Run key and re-creates it if it's gone, and every 875 seconds it does the same for a scheduled task.'")
a("6364f40a64",ok,HG,"'at least 40 incidents stemming from the specific Google Sites domain ... confirmed that two of these incidents came through a Custom GPT instance'")
a("9edad82487",ok,HG,"ClickFix 'copy-and-paste a command into their Terminal' executing PowerShell on Windows; no CVE named in the post")
a("dec37f9d8e",ok,HG,"'Most of this chain runs in memory ... so process activity is the most reliable place to catch it'")
a("676b9ff6f4",ok,HG,"Detection opportunities: powershell launching msiexec on GUID MSI; COTFileReadApp/DeElevate64 from %LOCALAPPDATA%\\Programs started by msiexec; unsigned ceiinfolog.dll; Run value and task with one name")
a("103d1e7093",ok,HG,"Decimal-integer host and DoH via Cloudflare/Google/Quad9 are in the post; 'from a non-browser process' is the entry's own concept (advisory F11)")
a("d6eede2fdf",ok,HG,"'Detections tied to Canon or Stardock names will miss the next swap' ; 'Kill the process first, then remove both.'")
# recreation
a("5864f42acc",ok,HP,"'register a member account, upload a malicious file, and turn it into a webshell'; webshells on three servers; card-data hunt on server 1, payment folders probed on server 3")
a("d1c88c267d",ok,HP,"'September 10, 2026, Huntress observed ... compromising multiple tenants'; /documents/MemberFiles/; 'put back into production prematurely ... Using the same account'; jQuery asset appended")
a("fd9b1d0914",ok,HP,"'On September 10, 2026, Huntress observed a threat actor compromising multiple tenants on a shared recreation management software platform using one repeatable trick: register a member account, upload a malicious file, and turn it into a webshell.'")
a("7a67b39a83",ok,HP,"'spending roughly 6 hours'; brute force, IIS 8.3 tilde, WebDAV, upload-handler bypasses, forced browsing; 'uploaded 14 files ... only the .aspx files were used to execute commands'")
a("63c84c2cb7",ok,HP,"Figure 1 'Sqlcmd is used to connect to the database with the obtained SQL credentials and search cardholder data'; Fortis webhook logs 'dumping specific log files to extract payment card details, including expiration dates, CVVs, and credit card numbers'")
a("a76a3b5e57",ok,HP,"'a total of five webshells uploaded'; copies as css_bundle.aspx / webresource.aspx; 'timestomping'; 'dir ... mxmerchant / fortis' payment modules probed")
a("1cf3634c2d",ok,HP,"'When the third server was put back into production prematurely ... Using the same account'; jQuery appended; 'intended to convert every visiting browser ... into an encrypted C2 client ... push dynamic eval() frames and harvest credentials in real time'")
a("ab1efd70dd",ok,HP,"'After registering a new account on the platform, the attacker was able to upload malicious files directly to the /documents/MemberFiles/ directory' (.aspx executed)")
a("aae3e9c834",ok,HP,"timestomping 'same last modified ... as legitimate components'; trojanized jQuery file; 'Base64-encoded files with .b64 extension ... decoded into actual .ps1 and .js files' in C:\\Windows\\Temp")
a("bdafc097e6",ok,HP,"'.jpg and .pdf files were uploaded as an extension execution test; only the .aspx files were used to execute commands'; IIS worker process spawns cmd.exe (Figure 2)")
a("2c6895a8d8",ok,HP,"'walked straight back in after a server was cleaned but not fully locked down'; 'Using the same account they previously registered'; SQL credentials extracted from web.config")
a("62af83a772",ok,HP,"Page description: 'breach 3 municipal servers and steal payment data'; no platform vendor or CVE named in the post")
a("573aa0675a",ok,HP,"'zh-CN ... we can deduce that the threat actor is most likely based in China'; scripts 'appear to be AI generated, with the extensive comments'")
a("6f05f1fc7f",ok,HP,"Post body describes attempts to extract card details; no count of cards and no statement that data left the servers")
a("5e09c8867e",ok,HP,"Registration then upload to /documents/MemberFiles/; .aspx webshells; 'IIS worker process spawns cmd.exe for enumeration commands' (Figure 2)")
a("6837e8b606",ok,HP,"Payment modules (mxmerchant, fortis) on the same server as general tenants; Fortis webhook logs read as plain .txt")
claims=yaml.safe_load(open('/home/user/ctipilot/work/2026-10-04T0405Z-intel/claims.iter4.yaml'))['claims']
ids=[str(c['claim_id']) for c in claims]
missing=[i for i in ids if i not in R]
extra=[i for i in R if i not in ids]
print("missing",missing,"extra",extra, len(R))
out=open('/home/user/ctipilot/work/2026-10-04T0405Z-intel/verification.iter4.claims.yaml','w')
out.write("claims:\n")
for i in ids:
    v,u,p=R[i]
    out.write("  - "+yaml.safe_dump({"claim_id":i,"verdict":v,"source_url":u,"passage":p[:200]},default_flow_style=True,width=10000).strip()+"\n")
out.close()
