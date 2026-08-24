# W34 operational entries (2026-08-17..2026-08-23) — 39 records

## 2026-08-17/akira-safe-mode-boot-edr-blinding-sonicwall-vpn
date=2026-08-17 kind=threat horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: Akira blinds EDR by rebooting a victim host into Safe Mode with Networking — the operator's first observed use of the technique, and the stripped-down boot starved its own encryptor
HEADLINE: Akira reboots a SonicWall-VPN victim into Safe Mode to strip EDR — and starves its own encryptor
SUMMARY: Huntress documents the first Akira intrusion it has observed using a Safe Mode with Networking reboot to take endpoint defences offline. After a credential spray resolved into a successful login on a SonicWall SSL VPN with no multi-factor authentication, the operator wrote its own AnyDesk service into the Safe Mode service allow-list, forced a reboot through msconfig, and worked from 06:29 UTC until 08:10 UTC on a host where neither the EDR agent nor Microsoft Defender real-time protection could start. The encryptor then failed — Safe Mode's constrained virtual memory starved the process tree — but Active Directory dumps and archived file shares had already left, so the intrusion stayed extortion-viable, and Huntress is explicit that the failure was the attacker's own memory-budget mistake rather than a defence to rely on.
CVES: -
ENTITIES: actor:akira
PRIMARY: https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr

## 2026-08-17/patchcord-sheetcord-google-sheets-c2-browser-shortcut-hijack
date=2026-08-17 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: PATCHCORD, SHEETCORD and HACKERAI — one espionage cluster runs three different command-and-control channels, two of them inside Google Sheets and GitHub, and persists by rewriting the victim's browser shortcuts
HEADLINE: Espionage implants run command-and-control through the Google Sheets API and persist by rewriting browser shortcuts
SUMMARY: Acronis Threat Research Unit documents three previously undocumented implants sharing one operator's infrastructure against Afghan telecom providers and South Asian critical infrastructure: PATCHCORD, a C/C++ backdoor delivered by fake Afghan Telecom VPN and ministry installers, SHEETCORD, a Go implant whose command-and-control runs entirely through the Google Sheets API v4 using a hardcoded cloud service account and a per-victim spreadsheet tab, and HACKERAI C2 Agent, which does the same job through GitHub Gists. All three persist by hijacking browser shortcuts so the implant launches first and then starts the real browser, and PATCHCORD executes operator-supplied shellcode entirely in memory. The targeting is South Asian, but the tradecraft is not: two of the three channels terminate on Google- and GitHub-owned endpoints that most egress policy treats as benign.
CVES: -
ENTITIES: actor:apt36, malware:patchcord, malware:sheetcord, malware:hackerai-c2-agent
PRIMARY: https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/

## 2026-08-18/arbeiterkammer-ooe-anti-forensic-wiping-blocks-scoping
date=2026-08-18 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Arbeiterkammer Oberösterreich cannot scope its own breach because the attackers wiped the traces — so every member is being notified under Article 34 as a precaution
HEADLINE: Deliberate trace removal turned a scoped breach notification into a blanket one at an Austrian public-law body
SUMMARY: The Upper Austrian Chamber of Labour disclosed on 2026-08-16 that unknown attackers reached parts of its IT systems on Monday 2026-08-10 and obtained access to data. It states it cannot establish the extent of that access — nor whether and which members' personal data were specifically affected — because the attackers deliberately wiped the traces. Having lost the ability to scope, it is treating all member data it holds as potentially affected and notifying every member individually by post under Article 34 GDPR, while warning them that any message claiming to come from the chamber about payments or prize winnings is fraudulent. Police and the Austrian data protection authority were notified and the entire data and IT infrastructure was moved into an isolated environment. No ransomware family, actor or initial-access vector has been disclosed.
CVES: -
ENTITIES: incident:ak-oberoesterreich-cyberattack-2026-08
PRIMARY: https://ooe.arbeiterkammer.at/service/presse/Cyberangriff-auf-die-AK-Oberoesterreich.html

## 2026-08-18/cve-2025-62593-ray-dashboard-dns-rebinding-browser-rce-kev
date=2026-08-18 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2025-62593 — Ray's dashboard is defended against browsers by a User-Agent string check, and CISA now records the DNS-rebinding bypass as exploited
HEADLINE: A developer's own browser is the attack path into a local Ray cluster — CISA catalogued the flaw as exploited on 17 August
SUMMARY: CISA added CVE-2025-62593 to its Known Exploited Vulnerabilities catalog on 2026-08-17, recording confirmed exploitation of a code-injection flaw in Ray, the distributed-computing framework widely used for machine-learning and data-engineering workloads. Ray's dashboard exposes unauthenticated job-submission endpoints by design, and the only guard against browser-borne requests is a check that the User-Agent header begins with "Mozilla" — which Firefox and Safari allow a page to overwrite through fetch(). Combined with DNS rebinding, a developer who visits a malicious page or is served a malicious advertisement has their own browser used as a proxy into a Ray instance that was never exposed to the internet, yielding code execution on the host. Fixed in Ray 2.52.0, which is also the first release to offer authentication at all — and it is disabled by default.
CVES: CVE-2025-62593
ENTITIES: -
PRIMARY: https://github.com/ray-project/ray/security/advisories/GHSA-q279-jhrf-cc6v

## 2026-08-18/cve-2026-69414-shieldbreak-defender-acknowledged-no-fix
date=2026-08-18 kind=vulnerability horizon=operational priority=notable deep_dive=False(None) update_of=2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix weekly_section=None
TITLE: UPDATE — Microsoft has acknowledged ShieldBreak and assigned CVE-2026-69414, rating the Defender privilege-escalation bypass 'Exploitation More Likely' with no update yet available
HEADLINE: The Defender patch-bypass proof-of-concept now has a vendor-confirmed identifier — and still no fix
SUMMARY: The ShieldBreak proof-of-concept covered here on 2026-08-12, which claims a fully reliable bypass of Microsoft's July fix for the RoguePlanet Defender privilege-escalation flaw and had drawn no vendor comment at the time, is now tracked as CVE-2026-69414. Microsoft's advisory names ShieldBreak explicitly, rates the flaw Important at CVSS 3.1 base 7.8, records it as publicly disclosed but not exploited, sets its exploitability assessment to "Exploitation More Likely", and states that a security update is still being worked on. Switzerland's NCSC and France's CERT-FR both relayed the identifier to their constituencies on 2026-08-17, which is what puts a tracking number on an unpatched weakness in a baseline endpoint control across this constituency's estate.
CVES: CVE-2026-69414
ENTITIES: actor:nightmare-eclipse, trend:shieldbreak-defender-rogueplanet-patch-bypass-2026-08
PRIMARY: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414

## 2026-08-18/geoserver-jsonarraycontains-patched-wfs10-stacked-copy
date=2026-08-18 kind=vulnerability horizon=operational priority=high deep_dive=True(web-app-rce) update_of=2026-08-15/geoserver-jsonarraycontains-unauth-sqli-zeroday-exploited weekly_section=None
TITLE: UPDATE — GeoServer's actively exploited jsonArrayContains SQL injection now has a fix, a published root cause and a service-dependent exploitation path: WFS 1.0 reaches top-level SQL, WFS 2.0 does not
HEADLINE: GeoServer's exploited SQL injection is patched — vendor and researcher disagree on whether any config change helps
SUMMARY: GeoServer shipped 3.0.1, 2.28.5 and 2.27.6 on 2026-08-14 for the unauthenticated SQL injection in the GeoTools jsonArrayContains filter function that this pipeline covered on 2026-08-15 as exploited with no vendor fix; Switzerland's NCSC appended the fixed versions to its own advisory on 2026-08-17. Independent reversing published with the patch supplies the mechanism: the CQL filter value is interpolated into a PostgreSQL jsonb_path_exists() expression through String.format() with no escaping, reachable pre-authentication through the public OGC WMS and WFS endpoints of any PostGIS-backed layer with a text or JSON column. Exploitability depends on which service answers — WFS 1.0 puts the injection at the top level of the statement where a stacked second statement runs, WFS 2.0's count wrapper traps it — and where the database role holds superuser or pg_execute_server_program the stacked statement reaches OS command execution on the database host. The vendor advisory and the reversing analysis disagree on whether any configuration change helps — GeoTools states the mitigation published for the 2023 flaw this one regresses is not effective, while the reversing analysis states that disabling the encode functions option on the PostGIS data store stops the vulnerable translation — so the upgrade is the only remediation both agree on, and restricting the database role removes the command execution but not the injection.
CVES: -
ENTITIES: -
PRIMARY: https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html

## 2026-08-18/zurich-trial-lockergoga-megacortex-nefilim-swiss-victims
date=2026-08-18 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Zurich District Court opens the LockerGoga / MegaCortex / Nefilim trial: four named Swiss victims, CHF 100m+ in damage, and an indictment that describes the intrusion pattern step by step
HEADLINE: Six years on, the charge sheet for the Stadler Rail ransomware attacks is public — disable monitoring, encrypt servers and workstations, encrypt the backups too
SUMMARY: A 52-year-old Ukrainian software developer resident in canton Basel-Landschaft went on trial at Zurich District Court on 2026-08-17, accused of a central development and organising role in an international ransomware operation that ran from December 2018 to May 2020 using LockerGoga, MegaCortex and Nefilim. The indictment names four Swiss victims — Stadler Rail, Meier Tobler, Crealogix and IHI Ionbond — among ten companies across seven countries, puts economic damage above CHF 100 million, and records that none of the Swiss companies paid while three non-Swiss victims paid CHF 4.5 million between them. Prosecutors allege the group's principal, based in Moscow, operated under a cover identity of Russia's FSB; that is a prosecution claim in a contested trial, not an established attribution. The prosecution seeks twelve years' imprisonment and a twelve-year entry ban.
CVES: -
ENTITIES: incident:zurich-lockergoga-megacortex-nefilim-trial-2026, malware:lockergoga, malware:megacortex, malware:nefilim
PRIMARY: https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362

## 2026-08-19/clop-windchill-custom-implant-reverse-engineered
date=2026-08-19 kind=threat horizon=operational priority=high deep_dive=True(ransomware-affiliate) update_of=2026-08-15/clop-windchill-philips-shell-first-victim-confirmations weekly_section=None
TITLE: UPDATE — Cl0p's Windchill implant, reverse-engineered: a custom request header carries the commands, one of them decrypts the whole keystore including the LDAP manager password, and a built-in class loader turns it into an unlimited backdoor
HEADLINE: The web shell is written against Windchill's own Java classes, so its database queries wear the application's identity
SUMMARY: ReliaQuest published a reverse-engineering analysis on 2026-08-18 of the custom web shell deployed after exploitation of CVE-2026-12569 in PTC Windchill, attributing it highly likely to Cl0p. The implant is purpose-built against the application: commands arrive in a custom X-windchill-req HTTP request header rather than a body, a single S command reads Windchill's configuration file and decrypts every value in the application keystore — the LDAP manager password and all site administrator keys included — and a built-in Java class loader executes attacker-supplied bytecode from a Base64 ZIP entirely in memory. Its database queries run through Windchill's own MethodContext and WTConnection classes, so database telemetry attributes them to the application's normal service identity. General Electric confirmed on 2026-08-17 that it is assessing Cl0p's claims, joining Philips and Shell.
CVES: CVE-2026-12569
ENTITIES: actor:clop, campaign:clop-windchill-flexplm-extortion-2026
PRIMARY: https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign

## 2026-08-19/cve-2026-15748-forminator-forms-unauth-file-upload-rce
date=2026-08-19 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-15748 — Forminator Forms (600,000+ WordPress sites): a forged Select-field value overrides the upload allow-list, and the root cause went public seventeen days after the patch (CVSS 9.8)
HEADLINE: The blocklist matches MIME keys exactly, so a pipe-alternative key walks a PHP file past it
SUMMARY: Wordfence published the root cause of CVE-2026-15748 on 2026-08-17, an unauthenticated arbitrary-file-upload flaw in the Forminator Forms plugin for WordPress affecting all versions up to and including 1.56.1 — 600,000+ active installs, CVSS 9.8, Wordfence acting as CVE Naming Authority. The plugin's handle_file_upload function screens uploads against a dangerous-extension blocklist that matches MIME-type keys exactly, so a pipe-alternative key is not matched, and a forged Select-field value lets an unauthenticated submitter override the upload field's own type configuration — together yielding a PHP file on disk and remote code execution. Exploitable only on forms carrying both a File Upload field and a Select field. Patched in 1.56.2 on 2026-07-31; neither Wordfence nor the Swiss advisory reports any observed exploitation, and the advisory records the exploitation status for its whole bundle as unknown. Switzerland's NCSC put the disclosure in front of its constituency on 2026-08-18.
CVES: CVE-2026-15748
ENTITIES: -
PRIMARY: https://security-hub.ncsc.admin.ch/#/posts/12860

## 2026-08-19/cve-2026-15826-user-profile-builder-type-confusion-admin
date=2026-08-19 kind=vulnerability horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-15826 — User Profile Builder: a 61-to-70-character username makes WordPress return an error object, absint() turns it into the integer 1, and the plugin logs the caller in as user ID 1 (CVSS 9.8)
HEADLINE: A type coercion in the wrong order hands an anonymous registrant the administrator account
SUMMARY: Wordfence disclosed CVE-2026-15826 on 2026-08-14, an unauthenticated authentication bypass in the User Profile Builder plugin for WordPress affecting all versions up to and including 3.16.4 — 40,000+ active installs, CVSS 9.8, Wordfence as CVE Naming Authority. The plugin's wppb_log_in_user() function calls absint() on the return value of wp_insert_user() before checking whether that value is an error: a registration with a 61-to-70-character username is rejected by WordPress core with a WP_Error object, which absint() coerces to the integer 1 before the error check can stop execution, so the plugin issues an autologin bound to user ID 1 — normally the site administrator. Exploitable only where the plugin's Automatically Log In setting is enabled. Patched in 3.16.5 on 2026-07-16, the same day the vendor acknowledged the report; no source reports observed exploitation.
CVES: CVE-2026-15826
ENTITIES: -
PRIMARY: https://security-hub.ncsc.admin.ch/#/posts/12860

## 2026-08-19/cve-2026-18963-keycloak-reset-credentials-account-takeover
date=2026-08-19 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-18963 — Keycloak's password-reset flow can be driven to completion without the verification email being clicked, handing an unauthenticated attacker any account including administrators (CVSS 9.1)
HEADLINE: An identity provider's account-recovery path is the account-takeover path, and one affected Red Hat product has no fix at all
SUMMARY: Red Hat disclosed CVE-2026-18963 on 2026-08-18: a flaw in the reset-credentials flow of Keycloak's keycloak-services component lets an unauthenticated attacker force the password-reset process for any user without clicking the required email-verification link, then set new credentials directly and take full control of the account. Red Hat rates it Critical at CVSS 9.1 with no privileges and no user interaction required, and states the root cause is improper state validation in the reset-credentials authentication flow. Fixes shipped on 2026-08-18 in Red Hat build of Keycloak 26.4.15 and 26.6.6 — but the same component is recorded Affected with no erratum in the JBoss Enterprise Application Platform Expansion Pack, so part of the affected estate has no patch to apply. The two fixed streams are also not equivalent: 26.4.15 closes this flaw alone while 26.6.6 closes five, two of them further account-takeover and credential-disclosure paths on the same identity surface. Because the reset flow is reachable by anyone who can reach the realm, an administrator account served by that realm is takeable on the same terms.
CVES: CVE-2026-18963
ENTITIES: -
PRIMARY: https://access.redhat.com/security/cve/CVE-2026-18963

## 2026-08-19/cve-2026-19478-gitlab-graphql-unauth-data-destruction
date=2026-08-19 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-19478 — GitLab ships an out-of-band critical patch for a GraphQL directive flaw that lets an unauthenticated caller modify or delete public projects and user data (CVSS 9.4)
HEADLINE: GitLab breaks its own release cadence for a pre-auth flaw whose impact is destruction, not disclosure
SUMMARY: GitLab released 19.2.4, 19.1.6, 19.0.8 and 18.11.11 for Community and Enterprise Edition on 2026-08-17 outside its scheduled patch cadence, fixing CVE-2026-19478 — a code-injection flaw reachable through a GraphQL directive that GitLab states can allow an unauthenticated user to remotely modify or delete public projects and user data, rated CVSS 9.4 with no authentication and no user interaction. Every release line from 18.2 onward is affected. GitLab.com and GitLab Dedicated were already patched at disclosure, so the exposure is entirely self-managed instances. A companion CSRF flaw in the GraphQL multiplex query handler, CVE-2026-19650 at CVSS 7.1, lets mutations be executed through GET requests. No exploitation is reported by any party and GitLab withholds the technical detail for 90 days.
CVES: CVE-2026-19478, CVE-2026-19650
ENTITIES: -
PRIMARY: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/

## 2026-08-19/cve-2026-33824-ikeext-kev-confirmed-exploited
date=2026-08-19 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=2026-08-10/cve-2026-33824-ikeext-double-free-root-cause-published weekly_section=None
TITLE: UPDATE — CVE-2026-33824 (Windows IKE Extension) is now on CISA's exploited catalogue, four months after the patch, while Microsoft's own record still reads 'Exploitation Less Likely'
HEADLINE: The pre-auth double free on UDP 500/4500 is now catalogued as exploited, and it carries an EPSS of 55.85
SUMMARY: CISA added CVE-2026-33824 to its Known Exploited Vulnerabilities catalog on 2026-08-18, changing what this pipeline recorded on 2026-08-10 when the flaw was covered as patched but not confirmed exploited. Nothing about the remediation changes — the fix shipped in Microsoft's April 2026 cumulative updates — but the exposure now carries a federal exploitation determination: an unauthenticated attacker reaching UDP 500 or 4500 on any Windows host acting as an IKEv2 responder can free the same heap block twice and execute code in the Local System context of the IKEEXT service. The determination rests on that one authority — ENISA's database carries the same date and an EPSS of 55.85 but mirrors CISA rather than assessing independently — and Microsoft's record has not been revised since 14 April, still recording exploitation as no with an assessment of "Exploitation Less Likely", so an estate that triaged this CVE on the vendor's exploitability signal alone ranked it too low.
CVES: CVE-2026-33824
ENTITIES: actor:knaithe-knyuan
PRIMARY: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json

## 2026-08-19/cve-2026-55040-sharepoint-kev-exploitation-confirmed
date=2026-08-19 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=2026-08-13/sharepoint-cve-2026-55040-jwt-forgery-exploited-root-cause weekly_section=None
TITLE: UPDATE — CVE-2026-55040 crosses into confirmed exploitation on CISA's catalogue while Microsoft still records it as not exploited, and it lands on an on-premises SharePoint estate this constituency has already had breached twice
HEADLINE: CVE-2026-55040 moves from honeypot proof-of-concept traffic to a federal exploitation listing
SUMMARY: CISA added CVE-2026-55040 to its Known Exploited Vulnerabilities catalog on 2026-08-18, and ENISA's EU Vulnerability Database mirrors that date. This pipeline covered the flaw on 2026-08-13 when the only exploitation evidence was Rapid7's proof-of-concept being replayed against honeypots, and carried it as proof-of-concept-public rather than exploited; that is what has changed. The flaw is a pre-authentication weak-authentication bypass in Microsoft SharePoint Server that allows impersonation, patched in July 2026 for Subscription Edition, 2019 and Enterprise Server 2016. Microsoft's record has not been revised since 14 July and still records exploitation as no. For this constituency the listing lands on ground that has already been breached twice — the federal IT provider BIT and canton Graubünden both disclosed on-premises SharePoint intrusions in early August.
CVES: CVE-2026-55040
ENTITIES: incident:foitt-bit-sharepoint-breach-2026-07, incident:graubuenden-canton-sharepoint-breach-2026-08
PRIMARY: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json

## 2026-08-19/medusa-raas-advisory-update-24-hour-weaponisation
date=2026-08-19 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Medusa's joint advisory update puts a number on the patch race: affiliates weaponise newly announced flaws within 24 hours, and the agencies find no sign the group develops any of them itself
HEADLINE: A ransomware crew that develops no zero-days still beats the patch window, on exploits it obtains from sources the agencies cannot identify
SUMMARY: CISA, the FBI and — newly — HHS updated the joint #StopRansomware advisory on Medusa on 2026-08-18 with FBI investigative data through April 2026, raising the recorded victim count from more than 300 to more than 500; the only sector list any cited outlet publishes covers medical, education, legal, insurance and manufacturing. The operationally useful part is the tempo claim: the agencies state Medusa actors exploit newly announced flaws within 24 hours and have been seen using exploits up to a week before public disclosure, while explicitly assessing that the group develops no zero-day or N-day vulnerabilities of its own, obtaining advanced access to exploits from sources the agencies could not identify or else moving fast on public disclosures. Separately from that, initial-access brokers who sell entry into victim networks are paid from $100 to $1 million, with a premium for exclusivity. The advisory also names the remote-management tooling affiliates use post-compromise. The group has added no new leak-site victims since April.
CVES: -
ENTITIES: malware:medusa
PRIMARY: https://therecord.media/more-than-200-medusa-ransomware-victims-in-last-year-cisa

## 2026-08-19/metabase-downstream-victims-nine-credential-rotation
date=2026-08-19 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=2026-08-12/cve-2026-72898-metabase-sqli-cve-assigned-kev weekly_section=None
TITLE: UPDATE — the Metabase SQL injection has produced nine publicly confirmed downstream breaches, and the reason the list keeps growing is that patching the BI tool does not invalidate the database credentials it already handed over
HEADLINE: A business-intelligence layer holds the keys to every warehouse behind it, and the patch does not take them back
SUMMARY: A tracker maintained by VenariX, updated 2026-08-17, now counts nine publicly confirmed organisations whose compromised Metabase environments were used to reach connected data warehouses — n8n, Framework, Tally and Kilo Code, joined on 2026-08-17 by Stocksy United Co-op, ShipMonk, Checkly, Cypress.io and Bits of Gold. This pipeline covered CVE-2026-72898 on 2026-08-09 and 2026-08-12 as an exploited CVSS 10.0 unauthenticated SQL injection in the password-reset endpoint; the delta is the downstream pattern. Because Metabase stores the credentials for every database it connects to, administrative access to the application yields those credentials, and Metabase's own guidance is that patching does not invalidate credentials already exposed. Metabase also published a two-request log pattern that indicates a given instance was compromised.
CVES: CVE-2026-72898
ENTITIES: incident:metabase-sqli-zeroday-2026-08
PRIMARY: https://venarix.com/blog/metabase-security-incident-downstream-impact-across-customer-environments

## 2026-08-19/purpledelta-dprk-it-worker-facilitator-rmm-detection
date=2026-08-19 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: PurpleDelta: Insikt Group gets inside a North Korean IT-worker operation and finds the detectable half is on the endpoint — a second remote-management tool on the company laptop, and a device whose location never matches the login
HEADLINE: The fraud is a hiring problem; the evidence sits in RMM inventory and laptop geolocation
SUMMARY: Recorded Future's Insikt Group published an analysis on 2026-08-18 of PurpleDelta, its designation for the North Korean IT-worker cluster that overlaps with the vendor names Jasper Sleet, UNC5267, Wagemole and Famous Chollima. Between late 2024 and early 2025 one cluster applied to over 1,100 companies, sometimes 60 positions a day, running at least 22 fabricated personas, some of them supported by AI-generated photos, illicit identity documents and purpose-configured chatbot assistants used to answer interview questions in real time; Insikt assesses the operators are highly likely to have been employed by at least ten organisations. Roughly 80% of the target companies were North American, but Insikt states operators applied in every region of the world. The transferable value for defenders is Insikt's own technical control set: the employer-issued laptop is held by a facilitator and reached over commercial remote-desktop tooling, which makes a second RMM agent and a location mismatch the observable evidence.
CVES: -
ENTITIES: actor:purpledelta
PRIMARY: https://www.recordedfuture.com/research/purpledelta-fraudulent-employment-operations

## 2026-08-19/stopandprotect-wordpress-hosted-extortion-mu-plugin
date=2026-08-19 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: StopAndProtect runs its whole operation off other people's WordPress sites — a must-use plugin that never appears in the plugin list, a hidden REST route that accepts PHP, and an installer that deletes itself
HEADLINE: Roughly 2,000 hijacked sites are the infrastructure, not the victims, and the persistence lives where nobody looks
SUMMARY: Check Point Research published an analysis on 2026-08-18 of StopAndProtect, a criminal toolkit it first saw in mid-May 2026 that hosts its payloads, command-and-control and stolen data on compromised WordPress sites rather than on dedicated infrastructure. Persistence on each hijacked site is a must-use plugin dropped at wp-content/mu-plugins/wp-sec.php — a directory WordPress auto-loads on every request and does not show in the standard plugin list — which registers a hidden REST route authenticated by hardcoded credentials that will write files, explicitly including PHP, almost anywhere under the site root; the installer then deactivates and deletes itself. Delivery is a fake-CAPTCHA paste-and-run lure leading through two .NET loader stages to a component set covering encryption, an SMB/USB worm, a credential and screenshot collector, a lock screen and an operator chat channel. Check Point states no initial-compromise vector and names no actor.
CVES: -
ENTITIES: campaign:stopandprotect, malware:silentencryptor
PRIMARY: https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/

## 2026-08-20/castilla-la-mancha-panzer-extortion-claim-confirmed-attack
date=2026-08-20 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Spain's Castilla-La Mancha regional government confirms a cyberattack after the Panzer extortion group lists it — the government confirms the intrusion, not the group's data claims
HEADLINE: A regional administration confirms it was attacked; everything about what was taken is still the attacker's own assertion
SUMMARY: The regional government of Castilla-La Mancha confirmed to Spanish outlet Escudo Digital that it suffered a cyberattack, that all response protocols were activated, and that competent authorities and potentially affected individuals have been informed — after the extortion group Panzer listed the administration and claimed roughly 3 GB of stolen data. What Panzer claims to hold is education-heavy and includes minors: student and family records, Google Workspace user files, documentation on pupils with specific educational-support needs, school-census and electoral-process material, internal email and administrative documents. None of that is confirmed by the government, and Escudo Digital states plainly that the group's publication must be treated as a claim pending verification. No access vector has been stated by anyone.
CVES: -
ENTITIES: actor:panzer, incident:castilla-la-mancha-panzer-breach-2026
PRIMARY: https://www.escudodigital.com/ciberseguridad/castilla-la-mancha-confirma-el-ciberataque-de-panzer-que-reivindica-el-robo-de-datos-de-alumnos-y-familias.html

## 2026-08-20/cve-2026-19490-netscaler-gateway-aaa-auth-bypass
date=2026-08-20 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-19490 — Citrix NetScaler: an authentication bypass on Gateway and AAA virtual servers (CVSS 9.3), and on older builds no SAML configuration is needed to be exposed
HEADLINE: The precondition is wider than the headline version numbers suggest — on older builds a Gateway or AAA vserver alone is enough
SUMMARY: Citrix published a bulletin on 2026-08-19 covering two NetScaler ADC and NetScaler Gateway flaws, relayed the same day by CERT-EU as advisory 2026-010. CVE-2026-19490 is an authentication bypass using an alternate path, scored 9.3, against appliances configured as a Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) or as an AAA virtual server; CVE-2026-19489 is a memory overflow reachable only where SIP ALG is enabled on a Large Scale NAT group. The exposure boundary is the operationally important part: on 14.1-43.56 and 13.1-61.28 and later the bypass applies only when a SAML action is configured, but on earlier builds and on 13.1 FIPS any Gateway or AAA virtual server configuration is enough. Fixed in 14.1-73.32, 13.1-63.21, 14.1-73.32 FIPS and 13.1-37.277. Rapid7 reports no observed exploitation as of 2026-08-19 and still recommends emergency patching.
CVES: CVE-2026-19490, CVE-2026-19489
ENTITIES: -
PRIMARY: https://cert.europa.eu/publications/security-advisories/2026-010/

## 2026-08-20/cve-2026-64849-mlflow-webhook-ssrf-redirect-bypass-kev
date=2026-08-20 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-64849 — MLflow: the SSRF guard resolves the webhook host and then throws the answer away, so one redirect turns an unauthenticated tracking server into a reader of its own cloud credentials
HEADLINE: CISA catalogued it as exploited on 19 August, and the default MLflow server needs no authentication to reach the webhook that does the fetching
SUMMARY: CISA added CVE-2026-64849 to its Known Exploited Vulnerabilities catalog on 2026-08-19 with a 2026-09-02 remediation date, recording confirmed exploitation of a server-side request forgery in MLflow. On a default MLflow tracking server the model-registry webhooks API is unauthenticated, including a test endpoint that returns the upstream response status and body to the caller. The URL guard resolves the webhook hostname and rejects non-public addresses at registration, but never pins the resolved address to the connection, and delivery follows HTTP redirects without re-validating where they lead — so a webhook pointed at an attacker-controlled public HTTPS host that answers with a redirect reaches internal and cloud instance-metadata services and reflects what it finds. Fixed in MLflow 3.15.0.
CVES: CVE-2026-64849
ENTITIES: -
PRIMARY: https://osv.dev/vulnerability/GHSA-7gwp-5pfp-969j

## 2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited
date=2026-08-20 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-73570 — Zimbra Collaboration: a pre-auth command injection patched without a CVE in July is now recorded as actively exploited, four weeks after the fix shipped
HEADLINE: The patch landed on 21 July, the identifier on 13 August, the exploitation on 18 August — a CVE-driven patch process could not see this one at all
SUMMARY: Zimbra shipped ZCS 10.1.20 on 2026-07-21 with a fix for a command injection in the SNMP monitoring component, described at the time only in general terms and with no vulnerability flagged as exploited. The identifier CVE-2026-73570 was published on 2026-08-13, and ENISA's EU Vulnerability Database now records the flaw as exploited since 2026-08-18 — a determination CERT-FR relayed to its constituency on 2026-08-19. The flaw needs no authentication: improper sanitisation of untrusted input during SNMP notification processing lets a crafted SMTP request reach arbitrary operating-system command execution as the Zimbra user. It applies only where the optional zimbra-snmp package is installed and SNMP notifications are enabled, which is the check that decides whether an estate is affected at all.
CVES: CVE-2026-73570
ENTITIES: -
PRIMARY: https://wiki.zimbra.com/wiki/Zimbra_Security_Advisories

## 2026-08-20/doj-mabna-institute-superseding-indictment-swiss-victims
date=2026-08-20 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: DOJ's superseding indictment against Iran's Mabna Institute names Switzerland twice — among the countries whose universities were compromised, and among those whose companies had employee mailboxes taken
HEADLINE: Eight more defendants, a password-spray campaign against government entities, and a victim list a Swiss reader is on
SUMMARY: The US Department of Justice unsealed a 14-count superseding indictment on 2026-08-18 charging 17 members of the Mabna Institute, an Iran-based company that has run intrusions on behalf of the Islamic Revolutionary Guard Corps since at least 2013; nine were charged in 2018 and eight are new. The indictment covers 144 US and 178 foreign universities, at least 42 US and 11 foreign companies, at least five US federal and state agencies and two NGOs. DOJ's own release names Switzerland in both foreign-victim lists. The tradecraft is unglamorous and still current: spearphishing against academic staff, reuse of stolen credentials to log into professor accounts and pull research, and — for the corporate and government intrusions the new defendants are charged with — password spraying, which DOJ says cost victims more than $20 million to investigate and remediate.
CVES: -
ENTITIES: actor:mabna-institute
PRIMARY: https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary

## 2026-08-20/grandoreiro-dll-sideload-inverted-sandbox-check
date=2026-08-20 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Grandoreiro's loader decides it is in a sandbox when it finds seven ordinary desktop shortcuts — an inverted environment check, behind a two-hop DLL sideload
HEADLINE: The evasion logic is backwards on purpose: a clean, well-stocked desktop is what makes this malware quit
SUMMARY: Acronis's Threat Research Unit analysed a Grandoreiro banking-trojan wave delivered as a renamed copy of the legitimate Duplicate Files Finder utility, which loads its genuine dependency and is in turn used to sideload a malicious library under the ordinary-looking name of a MinGW runtime component. Before any command-and-control attempt the loader runs a staged environment gate whose standout check is inverted: if desktop shortcuts for all seven of a named set of mainstream consumer applications are present at once, it concludes it is in an analysis image and terminates. Acronis's telemetry places the largest share of samples in Mexico, with Spain and several Latin American countries forming a secondary cluster and European presence described as limited but notable. The command-and-control server was offline during analysis, so the protocol detail is static analysis rather than observed traffic.
CVES: -
ENTITIES: malware:grandoreiro
PRIMARY: https://www.acronis.com/en/tru/posts/grandoreiro-goes-north-from-brazil-to-mexico-with-a-new-dll-sideloading-campaign/

## 2026-08-20/joint-advisory-active-threat-siemens-s7-plcs
date=2026-08-20 kind=threat horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: Five US agencies warn of an active threat to Siemens S7 PLCs — AI-written Python tooling built on the standard S7 libraries, dressed as legitimate OT monitoring software
HEADLINE: The agencies say the targeting is not limited to Siemens, and that what they see is reconnaissance rather than confirmed manipulation
SUMMARY: The NSA, CISA, the FBI, the Department of Energy and the Environmental Protection Agency issued a joint advisory on 2026-08-19 on an active threat to Siemens S7 Series programmable logic controllers, naming S7-200, S7-300, S7-400, S7-1200 and S7-1500 as actively targeted. Actors locate exposed controllers through internet-scanning services including Censys and ZoomEye and attack critical and high-severity vulnerabilities, outdated software and weak authentication. The tooling is the notable part: AI-developed Python scripts using the snap7.dll and python-snap7 libraries to speak S7comm, disguised as legitimate OT monitoring software, with read and write access to PLC memory, configuration data and ladder-logic programs. The agencies assess the activity as focused on persistent reconnaissance, potentially preparing for disruption, and state that ongoing PLC targeting is broader than Siemens.
CVES: -
ENTITIES: -
PRIMARY: https://www.ic3.gov/CSA/2026/260819.pdf

## 2026-08-20/latvia-csdd-breach-outsourced-monitoring-missed-it
date=2026-08-20 kind=incident horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: Latvia's vehicle-registration authority lost payment records on two-thirds of the country's population — and the provider contractually watching its infrastructure round the clock did not notice
HEADLINE: CSDD's own staff found the intrusion and stopped it in hours; the outsourced monitoring never raised it, and the supervisory board has resigned
SUMMARY: Latvia's Road Traffic Safety Directorate (CSDD), the national vehicle-registration and driver-licensing authority, states that between 8 and 10 August 2026 an attacker obtained payment-receipt data going back to 2008 on 1.2 million individuals and 200,000 legal entities — roughly two-thirds of Latvia's population. Names, personal identity codes, payment amounts and dates, licence plates and registered addresses were taken; phone numbers, email addresses, usernames and passwords were not. CSDD's own staff discovered and stopped the intrusion within hours, while its outsourced IT provider, contracted for round-the-clock monitoring, neither detected it nor alerted the agency. CERT.LV assesses the attack was targeted and preceded by preparation; a second targeted attempt the following weekend was blocked. The supervisory board has resigned and the agency's chief intends to.
CVES: -
ENTITIES: incident:latvia-csdd-breach-2026
PRIMARY: https://cert.lv/lv/2026/08/csdd-saskaries-ar-kiberdrosibas-incidentu

## 2026-08-20/oracle-august-2026-cpu-three-unauthenticated-cvss-10
date=2026-08-20 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: Oracle's August 2026 Critical Security Patch Update carries three unauthenticated CVSS 10.0 flaws — one of them in the LDAP server of Oracle Internet Directory
HEADLINE: 943 patches in a monthly release, and the ones that decide the sequencing are the three needing no credential and no user interaction at all
SUMMARY: Oracle published its August 2026 Critical Security Patch Update — its monthly release, distinct from the quarterly cumulative Critical Patch Update — on 2026-08-18 with 943 new security patches, and Switzerland's NCSC relayed it to its own constituency the following day. Three flaws in the release carry a CVSS 3.1 base score of 10.0 with Privileges Required and User Interaction both None in Oracle's own risk matrix: CVE-2026-61241 in the LDAP server of Oracle Internet Directory, and CVE-2026-70880 and CVE-2026-70921 in Hyperion Data Relationship Management and Hyperion Financial Management. Fusion Middleware alone accounts for 262 patches of which Oracle states 182 may be remotely exploitable without authentication, and E-Business Suite for 120 of which 27 may be. No flaw in this cycle is reported as exploited by any source.
CVES: CVE-2026-61241, CVE-2026-70880, CVE-2026-70921, CVE-2026-60782, CVE-2026-70926, CVE-2026-60672
ENTITIES: -
PRIMARY: https://www.oracle.com/security-alerts/cspuaug2026.html

## 2026-08-20/ransom-busters-rogue-affiliate-fake-recovery-firm
date=2026-08-20 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: "Ransom Busters" emails ransomware victims before their incident is public, offering to delete the stolen data for a fee — and the tooling says it is the same affiliate who took it
HEADLINE: The tell is the timing: a recovery offer that arrives while the intrusion is still private is foreknowledge, not marketing
SUMMARY: GuidePoint Security's research team documents an entity calling itself Ransom Busters that emails ransomware victims at their own domain, asking for the CEO or IT leadership, claiming years of unauthorised access to criminal infrastructure and offering to return stolen files and delete the attackers' copies for $20,000-$60,000. The anomaly that gives it away is timing: the outreach arrives before the intrusion is public knowledge. Across two responses GuidePoint found the same reconnaissance scanner, the same cloud-exfiltration utility, the same remote-management tool installed by script, a local backdoor account with an identical fixed password and an identical attacker workstation name — an operator-level match recurring across incidents attributed to DragonForce, Settra and Anubis. GuidePoint assesses with moderate confidence this is one affiliate working across those programmes and diverting payments from them; Coveware independently confirmed responding to at least one incident with contact from the same party.
CVES: -
ENTITIES: actor:ransom-busters, actor:dragonforce, actor:settra, actor:anubis-raas
PRIMARY: https://www.guidepointsecurity.com/blog/beware-ransom-busters/

## 2026-08-23/blockchain-dead-drop-c2-commodity-graphspy
date=2026-08-23 kind=research horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Dead-drop command-and-control went commodity: three of four new entrants on Red Canary's monthly list resolve their C2 from a dead drop, two of them from a public blockchain, and the fourth is a GUI for Entra ID device-code phishing
HEADLINE: Dead-drop C2 moved from novelty to routine, and the control is an egress baseline rather than a blocklist
SUMMARY: Red Canary's monthly threat round-up, published 2026-08-20 on July 2026 telemetry, records four new entrants to its most-prevalent list — GraphSpy, Phexia, CastleRAT and EtherRAT — of which three resolve their command-and-control address from a dead drop rather than from a hardcoded domain, and two of those three read it from a public blockchain smart contract. The technique defeats domain and IP blocking because the operator rewrites the contract value and every installation picks up the change. The fourth, GraphSpy, is an open-source Entra ID and Microsoft 365 attack tool with a browser GUI that centralises device-code phishing, primary refresh token theft, Windows Hello for Business key registration and MFA method manipulation — the third device-code phishing tool to reach that list in 2026.
CVES: -
ENTITIES: tool:graphspy, malware:phexia, malware:castlerat, malware:etherrat
PRIMARY: https://redcanary.com/blog/threat-intelligence/intelligence-insights-august-2026/

## 2026-08-23/btr-sys-defender-remediation-driver-kernel-primitive
date=2026-08-23 kind=research horizon=operational priority=high deep_dive=True(windows-lpe) update_of=None weekly_section=None
TITLE: Windows Defender ships its own kernel write primitive: BTR.sys, the signed boot-time remediation driver, takes an encrypted job list from an alternate data stream and will delete or create any file or registry value asked of it
HEADLINE: No exploit, no vulnerability, nothing to blocklist — the driver is a required Defender component, and its instructions live in a hidden stream on its own file
SUMMARY: Check Point Research published an analysis on 2026-08-20 showing that BTR.sys, the Microsoft-signed "Boot Time Removal Tool" driver Windows Defender extracts from MpEngine.dll to finish remediation actions that need a reboot, exposes a general-purpose kernel-mode file and registry primitive once its transaction format is understood. There is no memory corruption and no vulnerability: the driver reads an RC4-encrypted job list from an NTFS alternate data stream on its own file and executes six action types, two of which amount to arbitrary file write and arbitrary registry write. Because the driver is a functionally required Defender component carrying a genuine signature, it cannot be added to the vulnerable-driver blocklist or blocked by WDAC without breaking Defender's own remediation, and because the tool extracts it from the local MpEngine.dll there is no third-party binary for a blocklist to key on. The precondition is pre-existing administrative privilege, which is why MSRC declined to service it; Check Point reports no evidence of real-world abuse.
CVES: -
ENTITIES: tool:btr-sys-loldriver-primitive
PRIMARY: https://research.checkpoint.com/2026/btr-reforged-weaponizing-defenders-remediation-driver-as-a-kernel-operation-primitive/

## 2026-08-23/cve-2026-69836-entra-id-exploited-flag-corrected
date=2026-08-23 kind=vulnerability horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-69836 — Microsoft corrected its own Entra ID CVSS 10.0 record from exploited to not-exploited within a day, and ENISA's exploited feed still says otherwise two days later
HEADLINE: A maximum-severity identity-plane CVE with nothing to patch, and two authorities that disagree about whether it was ever exploited
SUMMARY: Microsoft published CVE-2026-69836 on 2026-08-20, a CWE-502 deserialization flaw in Entra ID rated CVSS 3.1 base 10.0 and described only as letting an unauthorized attacker execute code over a network. It is a cloud-service CVE issued under Microsoft's transparency programme: the fix was applied to Microsoft's own infrastructure before disclosure, so no tenant has anything to install. The operationally relevant part is the exploitation field — MSRC's revision 1.1 of 2026-08-21 corrected the record to state the flaw was not exploited in the wild, while ENISA's EU Vulnerability Database, re-synced on 2026-08-22, still carries it on the exploited feed with an exploited-since date of 2026-08-21. Any vulnerability process that ranks on the EUVD exploited feed will treat this CVE as exploited; the vendor that owns the record says it was not.
CVES: CVE-2026-69836
ENTITIES: -
PRIMARY: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69836

## 2026-08-23/gtig-russia-clusters-app-passwords-whatsapp-linking
date=2026-08-23 kind=threat horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: Three Russia-nexus espionage clusters compromise European diplomats and academics without malware — by talking targets through app passwords, device-code approvals and WhatsApp device-linking, all of which are legitimate features working as designed
HEADLINE: No exploit and no payload — the victim approves the attacker's session, or issues a credential the second factor never sees
SUMMARY: Google Threat Intelligence Group published research on 2026-08-20 on three distinct suspected Russia-nexus clusters whose primary access method is abuse of legitimate authentication workflows rather than malware. UNC6293 talks targets into creating an application-specific password and sharing it back, which grants access without ever triggering the second factor. UNC7005 — the cluster this store already tracks as Storm-2945 — runs device-code phishing through spoofed conference sites that fingerprint the browser to evade automated scanners before showing the code, and separately abuses WhatsApp device-linking by generating a genuine link request against a victim-supplied phone number, then instructing the victim to approve it; a fake voice call on the same page captures microphone and camera through the browser under cover of the call. UNC5976 stands up a cloud project per phishing domain and harvests OAuth tokens after a real consent flow. The target set is academia, aerospace and defence, governments and think tanks across Europe.
CVES: -
ENTITIES: actor:storm-2945, actor:midnight-blizzard, actor:unc6293, actor:unc5976, malware:headrush, campaign:captivecrunch-storm-2945-hospitality-wifi
PRIMARY: https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia

## 2026-08-23/martigny-combe-valais-communal-mailbox-compromise
date=2026-08-23 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: A Valais commune's secretariat mailbox was compromised on 10 August and sat quiet until the attacker used it on 18 August to mail roughly 450 of the commune's own contacts — the send is what triggered detection
HEADLINE: Eight days of undetected mailbox access at a Swiss communal administration, ended not by monitoring but by the attacker making noise
SUMMARY: The commune of Martigny-Combe in Valais disclosed on 2026-08-20 that its municipal secretariat's professional mailbox had been accessed without authorisation. Its external IT-security contractor traced the compromise to 10 August, when an employee opened a malicious email without realising it; nothing surfaced until 18 August, when the attacker used the trusted communal mailbox to send a fraudulent message to roughly 450 people, which is what caused the commune to notice. Around 300 emails and their attachments were taken, described by the commune president as confidential and in places containing sensitive data, and two recipients are known to have clicked the fraudulent link. The commune blocked the mailbox, notified the federal cybersecurity office and the Valais cantonal data protection commissioner, has a criminal complaint with the cantonal police in progress, and says it will keep a year-long watch for the stolen data.
CVES: -
ENTITIES: -
PRIMARY: https://www.lenouvelliste.ch/valais/bas-valais/martigny-district/martigny-combe-commune/cyberattaque-a-la-commune-de-martigny-combe-300-courriels-contenant-des-donnees-sensibles-ont-ete-voles-1511002

## 2026-08-23/misp-stix-import-trust-boundary-dos-parser-state
date=2026-08-23 kind=vulnerability horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Three misp-stix flaws put the CTI pipeline itself in scope: a crafted STIX document can set its own MISP distribution and sharing fields, kill a long-running importer, or bleed data into the next event
HEADLINE: The library that converts STIX into MISP decided a document was trustworthy using markers the sender controls — and the fix exists only as commits
SUMMARY: Three CVEs disclosed on 2026-08-21 against misp-stix, the Python library MISP and other platforms use to convert between MISP and STIX 1 / STIX 2, put the intelligence-ingestion path itself in scope. CVE-2026-77710 (CVSS 4.0 6.9) is the load-bearing one: the importer decided whether an incoming document was a trusted internal MISP export using markers inside the document — STIX2 tool labels, the STIX1 title — that the producer fully controls, and treated the resulting attributes as trusted enough to copy a whole metadata dictionary onto them, letting a crafted bundle set distribution, sharing_group_id and tags on imported attributes. CVE-2026-77755 (8.7) lets one malformed document terminate a long-running importer outright because the failure path raised SystemExit, which callers' exception handlers do not catch. CVE-2026-77761 (6.3) leaks state between documents when a parser instance is reused. No tagged release carries the fixes — the last affected version is 2026.7.8 and remediation is individual commits.
CVES: CVE-2026-77710, CVE-2026-77755, CVE-2026-77761
ENTITIES: -
PRIMARY: https://osv.dev/vulnerability/CVE-2026-77710

## 2026-08-23/payload-zurich-it-provider-hwz-student-data
date=2026-08-23 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: A Zurich business school tells students their bank details and sick-leave records were stolen — not from its own systems, but through the infrastructure of an IT service provider whose leak-site listing names seven other Swiss customers alongside it, and does not close the list
HEADLINE: HWZ confirms the theft and names no provider; the only source connecting a provider to it is the extortion group's own leak-site listing
SUMMARY: HWZ Hochschule für Wirtschaft Zürich told students and alumni in a letter, reported on 2026-08-22, that its analysis of stolen data confirmed personal information of current students and alumni was taken — names, addresses, phone numbers, student-administration records, bank details and sick-leave notifications — and that the attack came through an external IT service provider's infrastructure rather than the school's own local systems. Two days earlier the extortion group Payload had listed a Swiss data-centre operator on its leak site, claiming roughly 490 GB and naming eight affected customer domains including the school's. No source other than that listing connects the named provider to the school, and HWZ itself names no provider — so the shape of the incident, a single managed-IT compromise reaching several unrelated downstream Swiss organisations at once, is established while the provider's identity is not.
CVES: -
ENTITIES: actor:payload-ransomware, incident:hwz-service-provider-breach-2026-08
PRIMARY: https://insideparadeplatz.ch/2026/08/22/cyber-attacke-konto-daten-von-hwz-studenten-geschnappt/

## 2026-08-23/rust-crates-arrayref-build-script-backdoor-dprk
date=2026-08-23 kind=threat horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: A hijacked crates.io account added the first dependency arrayref has taken in ten years, and that dependency ran a backdoor at compile time — every machine that built an affected project during a ninety-minute window must be treated as compromised
HEADLINE: Build scripts execute before the crate's own code, so `cargo build` was the whole exploit; Wiz ties the infrastructure to two DPRK-linked npm campaigns
SUMMARY: On 2026-08-20 an attacker holding a compromised crates.io publisher account pushed malicious versions of three widely used Rust crates — arrayref, internment and append-only-vec — each declaring a new build-time dependency on a freshly published typosquat impersonating the standard proc-macro2 crate. That dependency's build script runs automatically during compilation, before any of the parent crate's own code, so building an affected project was sufficient to execute the payload: it reconstructs a command-and-control URL from encoded fragments, disables certificate validation for its own callback, and downloads a platform-specific implant for Linux, Windows and macOS that persists via a registry run key, a launch agent or a user systemd service and falls back to a domain generation algorithm if its primary channel is unreachable. The Rust Security Response Team removed everything within 86 to 107 minutes per crate and locked the account, and states it does not believe the maintainer acted maliciously. Wiz reports the infrastructure substantially overlaps operations attributed to North Korean actors.
CVES: -
ENTITIES: actor:sapphire-sleet, campaign:rust-crates-arrayref-dprk-overlap-2026-08, campaign:mastra-easy-day-js-supply-chain
PRIMARY: https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/

## 2026-08-23/spectre-uat-10147-byovd-edr-callback-unlink
date=2026-08-23 kind=threat horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: SPECTRE unlinks EDR's kernel callbacks one at a time using a two-driver BYOVD toolkit and an offset table for thirteen Windows builds — and its Linux half hides through ftrace rather than the syscall table
HEADLINE: A cross-platform implant that blinds named endpoint products to process, thread and image-load events for the rest of the session
SUMMARY: Cisco Talos published an analysis on 2026-08-20 of SPECTRE, a cross-platform C backdoor deployed by a Chinese-speaking intrusion actor it tracks as UAT-10147 against compromised IIS and Linux web servers. The Windows variant loads one of two long-known vulnerable drivers as a transient kernel service, locates the kernel image through a documented information call, and uses a hardcoded per-build offset table covering thirteen Windows versions to unlink registered process-creation, thread-creation and image-load notification callbacks from their linked lists — blinding callback-dependent endpoint products, which Talos names as CrowdStrike Falcon, SentinelOne and Microsoft Defender, for the remainder of the session. Credential access deliberately avoids LSASS entirely, and the C2 configuration is held in an alternate data stream on the hosts file so it can be rotated without recompiling. The Linux variant persists as a systemd unit ordered ahead of security tooling and hides through the kernel's ftrace debugging interface rather than by patching the syscall table.
CVES: CVE-2019-16098, CVE-2021-21551
ENTITIES: actor:uat-10147, malware:spectre-uat10147
PRIMARY: https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/

## 2026-08-23/trueconf-server-kev-head-mare-trojanized-installer
date=2026-08-23 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-72529 and CVE-2026-72530 — a pre-auth chain on TrueConf Server's port 4307 reaches SYSTEM, and the operators use it to replace the client installer the server hands to everyone who joins a meeting
HEADLINE: Both flaws are now catalogued as exploited; the reach extends to organisations that run no TrueConf server of their own
SUMMARY: CISA added CVE-2026-72529 and CVE-2026-72530 to its Known Exploited Vulnerabilities catalogue on 2026-08-20, and ENISA's EU Vulnerability Database independently records both as exploited since the same date. Chained, they take an unauthenticated attacker from network access on TrueConf Server's port 4307/TCP — open by default per the vendor's own documentation — to arbitrary command execution as SYSTEM: the first invokes an undocumented function to run a script inside a deliberately restricted sandbox, the second escapes that sandbox through a flaw in its code-generation logic. Kaspersky, which coordinated both CVEs and is the CNA, reports the group it calls Head Mare — a cluster it has now reclassified from hacktivist to APT — chaining them since at least July 2026 to plant a web shell, then overwrite the server's own distributed Windows client installer with an unsigned trojanised copy. That last step is why the exposure is not confined to TrueConf operators: staff who join a meeting hosted on a compromised contractor's server and accept its client-update prompt receive the backdoor. Fixed on 2026-06-18 in 5.3.9, 5.4.9 and 5.5.5, two months before the catalogue listing, and Kaspersky's own analysis puts the underlying flaw in every release since 2022.
CVES: CVE-2026-72529, CVE-2026-72530
ENTITIES: actor:head-mare, malware:phantomcore, malware:phantomgraph, malware:phantomhook, malware:phantomreact
PRIMARY: https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/

## 2026-08-23/uat-10147-agentic-ai-exploitation-oob-confirmation
date=2026-08-23 kind=research horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: An intrusion crew's AI-written playbook records why time-based blind testing fails against ViewState deserialization — and that a successful exploit returns HTTP 500, which is what most error-rate alerting is tuned to ignore
HEADLINE: Talos recovered the attacker's own generated tradecraft notes from an open directory, and the most useful page is the one explaining how they confirm execution
SUMMARY: Cisco Talos published a companion analysis on 2026-08-20 to its SPECTRE implant research, covering how the same Chinese-speaking actor, UAT-10147, uses agentic AI across the exploitation lifecycle rather than for scripting help. Talos recovered the actor's own operational artifacts from an open directory on a download server: a target list of roughly 170,000 URLs split into seventeen batches, an AI-generated nine-section playbook for ASP.NET ViewState deserialization attacks, and four companion Python scripts automating write-capability checks, implant deployment, web-shell staging and reconnaissance. Two findings in that playbook are directly useful to defenders regardless of this actor: time-based blind testing cannot confirm ViewState code execution because the launch call returns immediately, pushing the actor to out-of-band callbacks instead; and a successful exploit surfaces as an HTTP 500 with a cast exception, so alerting that treats 5xx responses as noise misses the successful attempts specifically.
CVES: -
ENTITIES: actor:uat-10147, tool:pentestgpt, tool:deepaudit
PRIMARY: https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations/

