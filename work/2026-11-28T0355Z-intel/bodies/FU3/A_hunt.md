---
title: US hospital credentials taken, a US manufacturer’s cloud accessed, law firms and federal agencies next
url: https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms
hostname: hunt.io
description: Three recovered open directories tie an active crew to a US hospital's stolen credentials, a manufacturer's cloud listing taken with a live token, and US law firms and federal agencies under recon.
sitename: Hunt Intelligence
date: "2026-11-24"
fingerprint: b451ad91a6b26f89
language: en
image: https://framerusercontent.com/images/GddJZBdKk2mHyxgvDdOMiO3GcP0.png?width=540&height=540
pagetype: website
filedate: "2026-11-28"
---
US hospital credentials taken, a US manufacturer’s cloud accessed, law firms and federal agencies next

Published on

**Disclosure: We notified CISA and shared an advance copy before publishing, for coordination with the affected victims. Organizations with confirmed compromise or data access are generalized to sector. Organizations that were only targeted, scanned, or appeared in reused third-party credential lists are named as targets, not as breach victims.**

An exposed [open directory](https://hunt.io/glossary/open-directories) is one of the more useful mistakes an operator can make, showing the work in progress: the tooling, the target lists, the logs, and the loot.

The Hunt.io threat-research team surfaced three of them through [AttackCapture™](https://hunt.io/features/attackcapture) scanning and recovered their full contents. They belong to an active intrusion crew, and the operators' own files carry both the human stakes and the tooling: hospital account material and a recorded VPN session, a US manufacturer's cloud storage opened with a live token, reconnaissance across the US legal and government sectors, and a malware set running from a malicious Java database driver to an Apollo-derived Windows payload and a Poseidon Linux implant.

Everything below is drawn from the crew's own files, cited by IP, port, and path, with credentials, tokens, and personal data redacted and no recovered program executed. We separate what the code can do from what the logs actually record, because the extent of compromise differs sharply between environments.

The findings start with what matters most, the confirmed US impact, then work through the toolkit, the wider targeting, and the infrastructure.

## Key findings

Named is not breached. The law firms, federal agencies, and institutions named in this report were targeted, enumerated, or pulled from a reused credential list, not compromised by this operator. Confirmed access and data already taken are limited to the findings marked as such below, starting with University Hospitals and the US manufacturer.

- **A US hospital's data is in the operators' hands**: a large US hospital system’s staff credentials, an 8,460-address directory, a web-server phpinfo capture, and a separately recorded hospital VPN session. This is not a proven domain login or patient-data loss.
- **A US manufacturer's cloud storage was accessed**. The crew listed its Azure container with a live SAS token, capturing 155,568 object names including QuickBooks files, and ran its Windows hashes against a custom wordlist. Objects were listed, not downloaded.
- **US law firms and federal agencies are next**. Several hundred firms are enumerated at the remote-access edge, one is under active attack, and the same sweep reaches HRSA, SBA, NEA, NSF, and NCUA. This is targeting and attempts, not confirmed breach.
- **A malicious JDBC driver chains to an Apollo payload**. A TlsChannelFix class runs when a Java app loads it, and a launcher XOR-decodes a packed file into an Apollo-derived Windows executable. A separate Linux artifact is a Poseidon build.
- **Sensitive stores were retained**: 414 keystroke-log rows and 35,601 Kerberos key records across 11,867 principals. These are record counts, not victim totals.
- **The C2 mixes custom and commercial tooling**: a custom Java HTTPS beacon plus clients for Net Monitor for Employees Professional, a bought product, over authenticated SOCKS relays. Its agent port is not a standalone indicator.
- **Two foreign domains show deep access**: a Bangladeshi university's Kerberos material exported at scale, and a Swiss tax office's domain database and hives staged off an internal share. Neither is US.
- **The crew runs AI coding tools and collects victims' AI credentials**. Agentic AI clients run in its own environment, and scripts index Claude and OpenAI Codex credential files on victim hosts. No AI action is tied to a specific exploitation step.

## Three open directories and a shared toolkit

Hunt.io researchers discovered three open-directory endpoints. For source references, A denotes [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001), B denotes [45.83.180\[.\]113:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:8000), and C denotes [74.63.203\[.\]115:18111](https://portal.hunt.io/attackcapture/filemanager?host=http://74.63.203.115:18111).

A and B share an IP, giving two initial host profiles; C is a separate host whose relationship to the first two is kept open until independent evidence supports a stronger link. The three primary collections contain 2,115 files and 1,981 distinct hashes. Co-discovery does not establish common ownership.

Fig 01. Those totals come from three servers. The rest of the report walks them in order, beginning with the servers themselves.
A rules file left on host A, /README-RULES.txt at [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001), shows a shared box with multiple operators working separate branches:

```bash
VPS USAGE RULES (approved by operator 2026-10-25)
Point model: MAIN = operator Windows box (kit/loot/secrets live only there).
vps1 = 45.83.180.113 (Tallinn) workhorse; vps2 = 91.236.230.9 heavy tasks.
1\. File/process prefix = branch: vc_* = vCenter, nw_* = netway/vCloud, bd_*/nmep_* = BD.
6\. Traffic to victim nets only via proxychains4 -> Mythic socks :7002.
7\. Finishing a branch: remove own /root/<prefix>*, close tmux, drop own cron lines.
```
                Copy
The staged kit is a full enterprise-intrusion chain. The exploit CVEs actually present in the files, grouped by target:

- Citrix NetScaler: CVE-2025-5777, CVE-2019-19781
- FreePBX: CVE-2025-57819
- [php2shell](https://hunt.io/blog/php2shell-cve-2026-109618-109619-open-directories): CVE-2026-109618, CVE-2026-109619
- Active Directory and relay: CVE-2021-42278, CVE-2021-36942 (PetitPotam coercion), CVE-2017-8563, CVE-2020-1472 (Zerologon)

The [FortiGate](https://hunt.io/blog/thai-broadband-fortigate-sslvpn-meshcentral-intrusion) is hit two ways: a credential login check and a FortiOS auth-bypass probe. The login-check script fg.sh posts to /logincheck and, on success, queries the SSL VPN monitor API, while fg\_ldapbypass.sh probes the [CVE-2026-22153](https://nvd.nist.gov/vuln/detail/cve-2026-22153) LDAP empty-password bypass.

Three more exploit scripts sit alongside the list above: a Microsoft Exchange MRSProxy pre-auth RCE (CVE-2026-62911, cve62911\_poc.py), TightVNC (CVE-2024-42049, tvnc\_ctrl.py), and an LFI driver (CVE-2026-87902, lfi.py on host C).

The rest of the kit is standard: PetitPotam, krbrelayx, [Responder](https://hunt.io/malware-families/responder), PKINITtools, mitm6, Impacket, netexec, DonPAPI, and an LDAP relay-scan toolkit, with Microsoft 365 spraying (o365spray) and movement tooling (Chisel, proxychains). Their presence establishes availability, not successful operation against any named target.

The clearest impact sits not in this kit but in what the crew already took, starting with a US hospital.

## US healthcare: what is in the operators' hands

### University Hospitals

The primary healthcare victim is a large US hospital system. Collection A holds a loot file of 8,460 unique nonempty addresses, including 6,929 at the hospital’s primary domain and 513 at an affiliated academic medical domain, plus a separate 3,570-record authentication dump and a web-server phpinfo capture.

We are not reproducing any of that data. The per-domain address counts from /loot\_uh\_emails.txt at [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001), with no addresses shown, make the scale and the target plain:

```bash
  6929 primary hospital domain
  513 affiliated academic medical domain
  259 other domains
```
                Copy
A companion script separates the hospital’s two mail domains for targeted replay. A caution from the code itself: the credential-type checks submit usernames and discovery fields, not passwords, so neither the check nor its response proves a working login.

The format, acquisition origin, and current validity of these records are not established by the files. This is hospital credential material and a web-tier capture in the crew's possession, not a demonstrated interactive compromise.

Figure 1: Username discovery request to Microsoft's identity endpoint. The request contains a username and discovery flags. There is no password field in this request. It therefore cannot demonstrate that a password worked or that the account completed a sign-in.
### A recorded hospital VPN session

Separately, a US hospital-network VPN log records an ESP tunnel and a private address. Gateway logs of this kind support a session at a particular time: establishment, rekeying, dead-peer detection, fallback, and termination.

They do not establish continuous access through a configured expiry, and the accompanying failed-relay log cannot establish later internal access. We keep the VPN session, the credential lists, and the phpinfo capture as separate trails rather than merging them into one authenticated compromise.

### A pediatric-research credential set

A separate loot file holds 153 email-and-hash records for staff across roughly 54 children's hospitals and pediatric and oncology research centers, spanning 62 email domains. Most are US institutions.

The best-known names in the set include St. Jude, Children's Hospital of Philadelphia, Children's Hospital Los Angeles, Seattle Children's, Texas Children's, Cincinnati Children's, Johns Hopkins, Stanford, Duke, and Dana-Farber, with others alongside them. The records read as an account list reused from a third-party breach compilation, not a breach of any one of these institutions. These are credentials the crew collected, not evidence it got inside each hospital.

### The children's-hospital hunting list

Beyond what was already collected, A carried an active hunting list aimed at clinical-research infrastructure. These are REDCap servers, the data-capture platform hospitals use for research studies, from /hunt\_targets.txt at [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001):

```bash
redcap.shepherd.org          redcap.providence.org
redcap.atlantichealth.org    redcap-dev.research.bcm.edu
redcap.bmhcc.org             redcap-sctx.seattlechildrens.org
redcaphcm.stonybrookmedicine.edu  redcappoc.luriechildrens.org
researchredcap.luriechildrens.org  redcapwap.archildrens.org
```
                Copy
Same method as the law-firm list below: choose a sector, enumerate its exposed services, work the list.

### Medical-sector endpoint probing

The operators also sweep for exposed Spring Boot management endpoints, including across a university's medical and health subdomains. A university-related filter for /actuator/heapdump, /actuator/env, and /.env yields 9,195 records, of which 6,365 are status 403 and 96 are status 200.

Titles include ordinary pages, errors, and challenges, and a status 200 here does not establish disclosure. This is attempted probing of the medical-education sector, not confirmed access. The firmest US impact in the whole corpus is not a hospital at all, but a manufacturer.

## A US manufacturer: cloud storage listed, hashes attacked

The crew also worked a US manufacturer tracked by the codename MFLLC, through cloud-storage enumeration plus on-premises hash cracking.

A script, vslist.py, lists objects in a Microsoft Azure blob container (vsyd220.blob.core.windows.net/mfllc) with configured SAS parameters, follows the listing continuation marker across up to 300 pages, aggregates prefix sizes, and writes the object names to a local file. It also searches names for NTDS-related strings.

The implementation lists and sizes objects; in the recovered form it neither downloads their bodies nor deletes them, and its token was not tested. What it does establish is that the operator held working keys to the company's cloud storage and walked its contents.

Figure 2: Parsing Azure object metadata and following the listing continuation marker. The loop reads XML fields from a listing response. It stores names, counts files by prefix, and adds the listed sizes. The continuation marker requests another page of metadata. This fragment does not request the contents of those objects.Figure 3: Saving object names and calculating totals from listed sizes. The saved output is a name list and summary statistics. GiB is calculated from listed sizes. It is not a counter of bytes downloaded from the container. The SAS token and its signature are excluded from the excerpts.
A second script, ntcand.py at [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001), builds NTLM-hash candidates from the company's own terms:

```bash
base = ["Rochelle","Owen","Nate","Southern","Meridian","Fence","Jacob","Travis",
        "inventory","MFLLC","Weld","welding","Shop", ...]
cands += ["Rochelle!02","Meridian2026","Fence#1","Idaho2026","Welcome1","Winter2026", ...]
```
                Copy
The seed words alone are leads, not identification. The stronger identification is in the stolen listing itself: the object names include the company's QuickBooks company file and its domain, which point to a US manufacturer.

Hash-candidate generators do not establish successful cracking or access to an on-premises domain, so we hold the cloud-listing impact separate from the hash work. Outside the US, the same operators show what full interior access looks like when they get it.

## Outside the US: a Bangladeshi university and a Swiss tax office

Outside the US, the same corpus shows how far the crew gets once inside. We report these briefly; they are the capability proof, not the focus.

A Bangladeshi university had its Kerberos key material exported: 11,867 records in each of AES256, AES128, and DES formats, 35,601 records across 11,867 principals, including machine accounts. The crew worked it hands-on, with a pass-the-hash loot-mapping run across internal workstations and a DPAPI collection run. The export does not identify its own acquisition mechanism, and the reviewed domain-dump log lacks a successful DCSync, so we describe this as a recovered large-scale key export with hands-on lateral movement, not a one-click DC dump.

A Swiss tax office (internal domain TABT, 192.168.151.x) is covered by the IFM (install-from-media) workflow. A log reports ntdsutil install-from-media creation; a script copies the domain database and registry hives from a controller share to staging, XOR-decoding bytes with 0xA5, then requests IFM removal.

The recorded byte counts (a 33,554,432-byte database, 17,563,648-byte SYSTEM, 65,536-byte SECURITY) describe the staging step. Complete off-host transfer is not independently confirmed.

This environment is also where the operator's printer files and an NTLM-relay run (ntlmrelayx against ldap://192.168.151.1) belong. With those results behind them, the crew pointed the same toolkit at the US legal sector.

## US law firms and federal agencies: the sector in progress

With hospital and manufacturer data already in hand and two foreign domains dumped, the crew pointed the same toolkit at the US legal sector. Most of it is reconnaissance; one firm has moved into hands-on attack.

A legal-sector seed list holds 563 unique entries, and the HTTP sweep catalogues live remote-access front doors across more than 60 named firms, including Kirkland & Ellis, DLA Piper, Latham & Watkins, Dentons, Skadden, Jones Day, Sidley Austin, Gibson Dunn, White & Case, Morgan Lewis, Mayer Brown, Weil Gotshal, Cooley, Baker Botts, Troutman Pepper, Littler Mendelson, Jackson Lewis, K&L Gates, Holland & Knight, Greenberg Traurig, Crowell & Moring, Orrick, Wilson Sonsini, Quinn Emanuel, Morrison Foerster, and more.

Live remote-access endpoints from the httpx sweep, /comm\_web.txt at [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001):

```bash
https://a1-vpn.jonesday.com         [200]  [HSTS]
https://access.morganlewis.com      [200]  [Morgan Lewis Remote Access Portal] [Azure]
https://1-vpn-net-1.littler.com     [200]  [HSTS]
https://02fw1.honigman.com          [200]  [HSTS]
http://citrix.stblaw.com            [200]  [Apache]
http://citrixna.sidley.com          [307]  [Azure Front Door]
http://clientportal.mayerbrown.com  [301]  [Apache]
http://globalportal.dentons.com     [307]  [Azure Front Door]
```
                Copy
That is the remote-access edge, VPN, Citrix, and client portals, catalogued across the AmLaw list. It is the step right before the Citrix and Fortinet exploits staged on the same box.

Dedicated law directories and per-state scan folders show the crew working the sector down by state and specialty. These are enumeration counts, not organization or breach counts.

### Beyond law firms

The same recon run reaches past the legal sector. Associated web output contains 22,312 lines, with 22,250 parser-matched records and 1,051 .gov URLs across 536 hostnames.

Named in the sweep are federal agencies including HRSA (hrsa.gov, including the National Practitioner Data Bank and 340B systems), SBA (sba.gov), NEA (arts.gov), NSF (nsf.gov), and NCUA (ncua.gov), a university governance body (UNC School of Government), and large US enterprises (Hertz, Plaid, Oportun). Most responses are redirects or access-denied (often 403 behind Akamai or Cloudflare).

These are probes: targeting, not access. The .gov and legal counts are not organization or breach counts.

### One firm singled out

For at least one firm the crew went well past cataloguing. Simpson Thacher & Bartlett (stblaw.com) has a cluster of operator files that read like a worked attack plan: around 100 staff email and password pairs from a public breach-compilation service (pn\_stb\_lines.txt holds 99 lines), credential-stuffing against two Citrix NetScaler VPN gateways, the Citrix [CVE-2019-19781](https://www.citrix.com/blogs/2019-12/citrix-adc-citrix-gateway-cve-2019-19781-vulnerability) exploit (stb\_19781.sh), SQL injection against a firm web app, username enumeration, an SMTP open-relay test, and probing of its ServiceNow tenant and other services.

Every captured result shows failure. The VPN credential-stuffing returned invalid-credential errors (NetScaler 4009) and no session, and the leak tests logged no leak.

A caution on the success heuristics: two of the Citrix check scripts default an absent Location header to an empty string and then treat the absence of index.html as a positive, so a missing redirect can produce a false hit in either direction. SAML and Duo text in a response is not proof of accepted credentials or completed MFA.

So we have no evidence Simpson Thacher was breached. What we have is a named AmLaw firm under a sustained, multi-vector attack.

Figure 4: A Citrix response heuristic that can misclassify a missing redirect as success. When the response has no Location header, loc becomes an empty string. That string does not contain index.html, so this condition can return a hit without proving a successful login. A printed success label needs independent evidence.
To be precise about the wider claim: there is no law-firm loot on these servers and no firm in a verified-hit result. Most of the several hundred firms are at the enumeration stage, one is under active attack, and none shows a confirmed breach.

What makes the sector work serious is the company it keeps. The same operators, with the same toolkit, already hold a US hospital system's credentials and web-tier artifacts, have listed a US manufacturer's cloud storage with a live token, and have taken deep access in two foreign domains. How they get in is the weakest-evidenced part of the picture, and it is where we turn next.

## Initial access: more post-access than entry

The files show substantially more post-access activity than original entry. University material already contains monitoring access and credentials; the Swiss output begins after execution is available. Neither explains how access was first obtained.

The Citrix, FreePBX, and PHP-related sources include probes, attempted exploit logic, and external-tool references. The FreePBX evidence is broader than a wrapper reference: one script directly constructs an EXTRACTVALUE SQL-error probe, and another tests module-dispatch responses.

The referenced complete exploit is outside the preserved tree. A direct SQL-injection attempt is implemented in source; no successful database disclosure, command execution, or validated CVE assignment follows from that source alone. The same caution applies to a QuickBooks browser check whose branding-text heuristic can match a login-page footer, and to PHP session-file injection and REDCap import experiments whose response markers can be satisfied by reflection rather than execution.

A VPN cookie-forging script constructs an RSA-encrypted identity and time cookie, and a companion attempts tunnels and private-port checks. Source construction and recorded session events do not independently prove an authentication bypass or identify which credential mechanism produced each session.

Support-form delivery scripts prepare pretext messages under a persona with links to a listener; no matching submission, click, or resulting access was established. What the files show far more clearly is what runs after access, starting with a malicious database driver built for code execution.

## Execution through a malicious JDBC provider

Collection A contains generators for a class named com.microsoft.sqlserver.jdbc.TlsChannelFix. The class implements java.sql.Driver; its static initializer and constructor both invoke a boot routine. The generator also writes a service-provider descriptor naming the class:

```bash
META-INF/services/java.sql.Driver
    com.microsoft.sqlserver.jdbc.TlsChannelFix
```
                Copy
The descriptor was independently confirmed inside both inspected JARs (sqljdbc42beacon.jar and sqljdbc42v8.jar). In a compatible application environment, loading the provider starts the malicious routine.

This supplies a path to repeat execution when the application loads the JAR, subject to its classpath and runtime configuration. It does not require a separate scheduled task.

Figure 5: The JDBC provider calls its startup routine during initialization and construction. The class registers itself with DriverManager, but the malicious routine has already been invoked. The constructor therefore matters as an execution trigger, even though the driver methods do not provide a useful SQL connection.
The Python generator also creates the service-provider file, linking the Java class to the discovery mechanism:

```bash
os.makedirs('/root/jbeacon/META-INF/services', exist_ok=True)
open('/root/jbeacon/com/microsoft/sqlserver/jdbc/TlsChannelFix.java', 'w').write(src)
open('/root/jbeacon/META-INF/services/java.sql.Driver', 'w').write('com.microsoft.sqlserver.jdbc.TlsChannelFix\n')
```
                Copy
Writing the descriptor is not a deployment result; actual execution still depends on the application finding and loading that JAR.

The driver interface is largely a facade: connect() returns null, acceptsURL() returns false, and jdbcCompliant() returns false. The meaningful behavior occurs during initialization, before the object needs to provide a database connection.

An AtomicBoolean guard limits startup to the first successful compare-and-set in that loaded class, set before initialization completes, so an exception can leave startup incomplete without a retry. The guard is not a machine-wide lock and does not coordinate separate JVMs or classloader copies.

Figure 6: Stub JDBC methods provide the expected interface without a working database connection. Inside boot(), an atomic flag limits startup to the first successful compare-and-set in that loaded class. The daemon worker it starts cannot keep the JVM alive after application threads exit, and broad Throwable handlers suppress failures without resetting the guard.
### The file-decoding launcher and the Apollo payload

A separate generator reads a local dbmaint.fix file, XOR-decodes it, writes an executable under the Java temporary directory, and starts it with ProcessBuilder. Saved runtime output records the sequence on 14 October at 15:58:57 CEST: initialization, a 2,109,952-byte executable written under C:\Windows\TEMP, and process creation.

The same three-line event appears in several copied logs and must be counted once. This is direct evidence of the launcher event the logs report, not evidence that the HTTPS beacon variant also completed a polling cycle.

We independently confirmed that XOR-decoding dbmaint.fix with 0x5A produces the exact bytes of q4final.exe. Both hashes appear in the indicator appendix.

Figure 7: The launcher decodes bytes with XOR, writes an executable and starts a child process. The routine waits, logs a marker if its input is missing, otherwise reads and XOR-decodes it. The destination combines the Java temporary directory, an encoded prefix, a random hexadecimal suffix, and an extension. The log follows ProcessBuilder.start(), supporting recorded process creation rather than callback or task completion.
The managed q4final.exe has an obfuscated outer entry point, 101 type definitions, and 854 method definitions. Offline raw-DEFLATE extraction recovers 17 managed assemblies plus metadata.

ApolloInterop, Tasks, HttpProfile, and cryptographic components correspond to upstream Apollo architecture, supporting Apollo derivation with high confidence rather than relying on the assembly name. Task and transport names are an inventory, not proof that every handler ran. A verified runtime command-and-control configuration remains unresolved.

The HTTPS and launcher paths share a provider identity but do different work, and we keep their evidence separate:

```bash
JVM loads service provider
        |
        +--> HTTPS variant: poll queue -> cmd.exe -> post output
        |
        +--> Launcher variant: read packed file -> XOR decode
                              -> write temporary EXE -> start process
```
                Copy
A third diagnostic variant stages an encoded command file and launches cmd.exe, maps the callback domain lababalbaba.com to 45.83.182\[.\]68, and requests WinHTTP and .NET registry changes. Its transcripts record SYSTEM context and DNS diagnostics but do not establish a completed implant callback.

The Windows side is only half of the payload set. A second implant targets Linux.

## A Poseidon Linux implant

The Java launcher is only part of the recovered payload set. A 7,716,744-byte file named gkbd-cache.bin is a 64-bit Linux ELF.

Its Go build information names [github.com/MythicAgents/poseidon](http://github.com/MythicAgents/poseidon), identifies Go 1.25.1, and includes HTTP-profile build settings. This is strong artifact-level evidence of a Poseidon-derived build. It does not establish that the file ran on an external victim.

Offline decoding of the embedded HTTP configuration exposes the callback domain and timing:

```bash
callback_host      https://lababalbaba[.]com
callback_port      443
callback_interval  3600
callback_jitter    20
post_uri           data
killdate           2027-10-21
```
                Copy
AESPSK and proxy credentials: omitted

These values describe a build, not observed traffic or current infrastructure ownership. Encryption and proxy-secret fields are withheld.

The Apollo cryptographic provider and a DPAPI helper (UnprotectBlob.exe) were read statically as well; neither read exposes a validated key or a recovered plaintext credential. Alongside the implants sits the crew's privileged-execution and credential-access tooling.

## Credential access: NTDS, Kerberos, and DPAPI

SYSTEM selections and diagnostics establish a recorded execution context, not an exploited privilege-escalation vulnerability. A directly inspected console screenshot shows a command that creates a local account named svc\_audit, adds it to the administrators group, and writes a registry value named LocalAccountTokenFilterPolicy, with a console-reported zero exit status.

A caution on that last step: the screenshot writes the value under HKLM\SYSTEM\CurrentControlSet\Control\Lsa, while Microsoft documents the remote-UAC policy under a different path (HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System). So the command records account creation and a zero exit, but is not sufficient evidence that remote UAC restrictions were actually disabled. The credential in the original console command is excluded from publication.

For offline password testing, the collection includes NT-hash comparators and NTLMv2 checkers. Two variants contain a more fundamental defect: they calculate the identity component from the uppercased password candidate, leaving the parsed username unused, which differs from Microsoft's NTLMv2 construction. This is a static implementation finding, read from the code; no new password recovery is claimed.

Figure 8: A flawed NTLMv2 calculation uses the password candidate where the username is required. The response-key calculation uses the password candidate plus domain, rather than the required username and domain construction. We identified the error by reading the code; we did not run password recovery.
A recovered PowerShell recon script builds a local report using whoami /all, cmdkey /list, klist, quser, domain-controller queries, directory searches, and administrator-group queries. Listing saved-credential references is not the same as extracting plaintext passwords, and the script writes results and errors to a temporary file, so its presence alone cannot establish that each query succeeded.

Figure 9: Enumerating Active Directory computer objects through DirectorySearcher. The source writes results and errors to a temporary report; its LDAP block records a failure message when the search raises an exception. A result file or command transcript is needed to identify the computers actually enumerated.
Bundled PKINITtools, PetitPotam, and krbrelayx source shows capability availability. A successful coercion, relay, ticket acquisition, and subsequent remote execution would each require their respective outputs; these steps cannot be inferred by joining tool names. What ties the implants and the credential theft together is the channel the crew uses to run commands and move data back.

## Command and control: a Java beacon and a commercial monitoring agent

### The Java HTTPS beacon

The beacon generator implements a small command loop. After a 30-second initial delay it polls an HTTPS endpoint on TCP 8443, sleeps roughly 25 to 35 seconds between polls, passes a nonempty response to cmd.exe /c, and posts the collected output to a second endpoint. Bodies are XORed with 0x5A and base64-encoded; the transport is HTTPS with certificate and hostname checks disabled by the generated class.

Figure 10: Disabling TLS certificate and hostname validation for HTTPS connections. The TLS change affects the default HttpsURLConnection socket factory and hostname verifier in that JVM. It is not scoped to one connection object and is not a Windows-wide trust-store change. This describes a code-level consequence, not a measured effect on other traffic.Figure 11: The byte-wise XOR transformation used by the beacon. Each byte is XORed with the same value, 0x5A. Applying the operation again restores the original bytes. This is obfuscation, not keyed encryption; HTTPS is the transport protection.Figure 12: Polling for a command and submitting its output through separate HTTP paths. The loop acts only on a nonempty command, limits the returned string to 60,000 UTF-16 code units, and posts the result to the response path. This shows the implemented task-and-result flow; the saved launcher log belongs to a different variant.Figure 13: Setting HTTP timeouts and encoding the outgoing request body. The helper converts UTF-8 text to XOR-transformed bytes and then base64, and accepts only HTTP 200 before reading a response. The excerpt is from the recovered Java template; it does not prove this variant completed a live exchange.Figure 14: Running a command through cmd.exe and collecting its output. redirectErrorStream(true) merges stderr into stdout. The worker drains output, checks exitValue(), and appends an exit marker once the process exits. The outer loop checks elapsed time but does not call destroy() when it ends.
On the server side, the GET handler consumes a shared command file rather than selecting a per-client queue, and the handlers do not verify an application-level client credential:

Figure 15: The server retrieves a queued command and removes the queue file. The queue file is removed before the reply is delivered. If several clients poll, the request that consumes the file receives the command. Removing it before delivery also creates a possible command-loss case, though the saved material does not show such a loss.Figure 16: Decoding submitted results and appending them to the server's log. Results and decode errors share one file, recorded with a UTC time but without the client identifier. An HTTP acknowledgement alone does not prove a useful result was retained.
### The commercial monitoring protocol

Collection B contains custom clients associated with Net Monitor f or Employees Professional, a commercial monitoring product. The clients connect to agents on TCP 4495, in B through an authenticated SOCKS5 relay. This is a bought product with custom clients wrapped around it, not a framework the crew wrote, which is why the agent port alone is not an indicator.

Figure 17: Reading a four-byte length prefix before receiving the frame body. The receive loops handle data arriving across several socket reads. The prefix is an unsigned 32-bit big-endian byte count. This is framing logic, not evidence that a frame was authenticated, decrypted, or followed by command execution.
The client reads a four-byte big-endian frame length, reads the body, and processes JSON or encrypted content. Authentication derives a 32-byte key by applying SHA-256 to a configured passphrase, encrypts a challenge with AES-CBC and a random IV, and sends an authentication frame.

B's client supports both encrypted and plaintext command-frame modes; A's client authenticates with AES but sends its command frame as plaintext. The configured passphrase is withheld, and this analysis documents the recovered clients rather than establishing a product vulnerability.

Figure 18: Encrypting the challenge response with AES-CBC and a random initialization vector. The field carries the IV followed by encrypted challenge bytes, represented as hex. This fragment covers authentication; the later command mode must be checked in the client variant that sends it.
Five packet captures contain 51,049 records. Offline parsing identifies candidate monitoring-protocol frames through the configured SOCKS channel, supporting the framing analysis.

Incomplete sessions and capture boundaries prevent treating every frame as authenticated command execution, and no packet-derived victim total is assigned. The same stack also records what the crew collected through it.

## What the crew collected

The monitoring store contains 501 web-log, 842 application-log, 20 user-log, and 414 populated keylog rows. Keylogs share one host value; web logs contain five.

Browser counts are 178 Chrome cookies, 207 Firefox cookies, and 17 Edge saved-login rows, plus a separate Chrome token. Decryption and current usability were not established.

Cloud enumeration reports 542,861 objects and 418.24 GB of metadata-derived sizes, which is not downloaded volume or proof of container deletion. These are stored-record and listing counts, not people or organizations.

A separate media-collection script lists media paths and sizes, retrieves bodies over SMB, hashes them, runs a media classifier, and removes the temporary copies. Its results file records 126 qualifying records across eight addresses. Artwork and document paths appear in the set, and a model label is not a verified description of an image.

Figure 19: Retrieving an SMB file, hashing its contents and applying media-classification thresholds. The script retrieves file bytes, hashes them, and writes a temporary copy for the detector, logging only results that meet its score conditions. The 126 saved records are not a count of every image inspected, and a model label is not a verified content description.
### Exfiltration mechanisms

The recon transfer stage base64-encodes the local output, makes it URL-safe, and splits it into chunks sent inside GET request paths to the server's HTTP listener. A proxy or web server that retains request paths may preserve both the host label and the transferred data, which makes URL logs useful evidence and also sensitive records.

An expanded server access log contains 540 request records from 195 distinct client addresses. A successful HTTP status means the server handled a request, not that a known person received a complete, usable dataset.

The loop catches individual failures without retry or integrity verification, so hostname and chunk count alone cannot establish completeness. A third recovered host adds a different dimension: the crew's own environment and its AI tooling.

## The third collection: virtualization, guest-agent pulls, and AI artifacts

Collection C is a separate host, and we keep it separate until independent evidence supports a stronger link to A and B.

### Local virtualization administration

C's shell history records Proxmox inventory, Windows guests, storage changes, and RDP forwarding. The operators run a small farm of Windows VMs reached over RDP, and the history builds NAT rules that forward external ports to each VM's RDP service and persists them through an interface hook, recorded in /.bash\_history at [74.63.203\[.\]115:18111](https://portal.hunt.io/attackcapture/filemanager?host=http://74.63.203.115:18111):

```bash
dhcp-host=BC:24:11:DF:F5:BF,jkzy,192.168.100.113   # dnsmasq static lease
iptables -t nat -A PREROUTING -i vmbr0 -p tcp --dport 1012 -j DNAT --to-destination 192.168.100.113:3389
iptables -t nat -A PREROUTING -i vmbr0 -p tcp --dport 1099 -j DNAT --to-destination 192.168.100.113:3389
# persisted via /etc/network/if-up.d/sg-rdp-nat and /etc/network/if-up.d/codex-rdp-jkzy
```
                Copy
The VMs carry operator handles (sg12, sg13, sg14, jkzy, sg10v) on 192.168.100.0/24, exposed on external ports 1010 to 1099 and 13389. This is the crew's own hands-on environment, not a victim network. Timezone, language, and installation-media choices on this host do not establish the administrator's nationality or physical location.

### AI applications and configuration artifacts

C contains AI-application paths, configuration files, and a large application log (zz\_main.log) that records agentic AI-coding-client activity in the operators' environment, including a Claude Code client running under a local user, a browser-automation bridge connecting, and an agent-mode session with plugins and a scheduled-task wake claim. Scripts on the same host search for AI-tool authentication and configuration files on other systems, for example a disk-enumeration script whose search roots include a Claude data directory, and a produced file listing that indexes Claude desktop and OpenAI Codex credential and state files on a victim host.

Read carefully, this shows two things: AI tooling running in the operators' own environment, and collection intent against victims' AI-tool files. It does not connect an AI-generated instruction or agent action to a specific exploitation step in the hospital or manufacturer records.

Other scripts request changes to a Codex-named sandbox service and terminate WSL processes; their presence does not establish successful changes or an AI-product vulnerability. The ownership and origin of the copied authentication material remain unresolved, so we do not characterize it as a verified theft of a usable AI credential from an external victim. What the files do support is that AI-tool credential and state files are being swept up alongside the usual browser and DPAPI loot.

### Authentication stores and further experiments

C also contains a privacyIDEA copy (18 token records, 16 owners, 172 token-info records, 3,200 audit records), a cookie store, and archives of vault, DPAPI, and registry material, plus a Jenkins remoting agent and SQL-extraction experiments. These are retained sensitive artifacts and source-level capability.

We did not decrypt OTP secrets, use credentials, or establish external-victim ownership. Guest-agent file-pull helpers read content through a local VM's QEMU guest agent, but their counters can double-count partial saves, so a callback or saved filename requires independent length and hash validation before it is treated as a complete acquisition. Pulling back from the files, the platform record ties these hosts to a wider set of infrastructure.

## From the directories to a Mythic C2 host

Hunt.io lists [45.83.180\[.\]113](https://portal.hunt.io/ip/45.83.180.113) within AS62005, BlueVPS. Its profile shows open-directory warnings dated 6 October, 25 October, and 5 November 2026. Those dates guide the archived service records; warning counts and map locations do not establish who operated the server.

The second host, [74.63.203\[.\]115](https://portal.hunt.io/ip/74.63.203.115), is listed within AS46475, Limestone Networks, with an open-directory warning dated 4 November, and historical HTTP records show directory listings on port 18111 on 4 and 6 November. This confirms the exposure without joining its VM and application artifacts to the other host.

### From recovered configuration to a Mythic-labelled service

The next pivot came from source rather than a shared hosting provider. A hosts-mapping generator explicitly maps lababalbaba.com to [45.83.182\[.\]68](https://portal.hunt.io/ip/45.83.182.68), and the Linux payload's decoded configuration names the same domain. That gave a specific destination to investigate.

Searching its HTTP observations on port 7443 exposed a page titled Mythic:

```huntsql
SELECT ip, port, timestamp, html.head.title, http.headers.server
FROM http
WHERE ip = '45.83.182.68'
  AND port = 7443
  AND timestamp > '2025-11-03'
LIMIT 20
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT+ip%2C+port%2C+timestamp%2C+html.head.title%2C+http.headers.server%0AFROM+http%0AWHERE+ip+%3D+%2745.83.182.68%27%0A++AND+port+%3D+7443%0A++AND+timestamp+%3E+%272025-11-03%27%0ALIMIT+20&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
Output example:

Figure 23:
[Historical HTTP results](https://portal.hunt.io/sql?sql=SELECT%0A++ip%2C%0A++port%2C%0A++timestamp%2C%0A++html.head.title%2C%0A++http.headers.server%0AFROM%0A++http%0AWHERE%0A++ip+%3D+%2745.83.182.68%27%0A++AND+port+%3D+7443%0A++AND+timestamp+%3E+%272025-11-03%27%0ALIMIT%0A++20&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)showing a Mythic page title on 45.83.182.68:7443. The capture shows several Mythic observations, including 27 October 2026. Other rows show an HTTP 400 title indicating a plain HTTP request reached an HTTPS service. The screenshot corroborates the retained title; it does not show an authenticated Mythic session.

The [Pivot view](https://portal.hunt.io/ip/45.83.182.68/pivots) exposes the certificate SHA-256 and subject (lababalbaba.com). The exact hash is a more precise pivot than the title or subject name.

[JARM](https://hunt.io/glossary/jarm-fingerprinting)and

[JA4X fingerprints](https://hunt.io/glossary/ja4-fingerprinting). The broader fingerprints were not used to assign additional hosts to this activity.

A [HuntSQL](https://hunt.io/features/hunt-sql) query for that exact certificate hash returns every observation of it:

```huntsql
SELECT ip, port, certificate_hash, timestamp
FROM certificates
WHERE certificate_hash =
  '1ba2ec04908a4c4696f2f740f04588708c0c3afc7efbebc0aa69f39b78fc535b'
  AND timestamp > '2025-11-03'
LIMIT 100
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT+ip%2C+port%2C+certificate_hash%2C+timestamp%0AFROM+certificates%0AWHERE+certificate_hash+%3D%0A++%271ba2ec04908a4c4696f2f740f04588708c0c3afc7efbebc0aa69f39b78fc535b%27%0A++AND+timestamp+%3E+%272025-11-03%27%0ALIMIT+100&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
Output example:

Figure 25: Matching certificate observations on ports 443 and 7443. The exact-hash search returned 23 observations, all on the configured IP, across ports 443 and 7443. That supports certificate reuse between those services and adds no further host in the returned inventory.
### A second domain association

Hunt.io's [Domains view for 45.83.182\[.\]68](https://portal.hunt.io/ip/45.83.182.68/domain) shows sb-it-support.com and its mail and www subdomains. These are platform-listed associations, not proof of common ownership on their own.

A separate retained observation makes the lead more specific: on 8 November, port 8089 served a page titled User Portal with a certificate for sb-it-support.com. The exact-certificate search returned two observations on that IP only. Historical DNS and tenancy evidence are still needed before assigning the domain to the same operator.

### Additional staging and delivery services

Returning to [45.83.180\[.\]113, the retained port-8899](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:8899) response exposed another directory on 5 November. Its links included wsvc\_beacon.exe, wsvc\_prod.exe, gh0st\_push.py, and prod-miniupdate-v9.zip and prod-miniupdate-v10.zip, with version-directory entries retained through 10 November.

The host's port-8080 response contained a document-sharing pretext and a browser-mediated WordPress plugin-installation attempt referencing /athena.zip on the same server. These are acquisition leads; the filenames do not establish the files' behavior, and their contents were not retrieved during this hunt.

Figure 27: Archived executable, script and log filenames in the additional directory. The archived inventory sets the next collection step: compare the versioned archives, examine the transfer or deployment logs, and obtain executable hashes before assigning a payload family. The badges shown are platform annotations and do not replace analysis of the bytes.
To see how long that lure page stayed live, we pulled its history on port 8080.

```huntsql
SELECT
  ip,
  port,
  timestamp,
  html.head.title,
  html.body.hash.sha256
FROM
  http_history
WHERE
  ip = '45.83.180.113'
  AND port = 8080
  AND html.head.title = 'Secure Document — Action Required'
  AND timestamp >= '2026-10-21'
  AND timestamp < '2026-11-03'
ORDER BY
  timestamp ASC
LIMIT
  500
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT%0A++ip%2C%0A++port%2C%0A++timestamp%2C%0A++html.head.title%2C%0A++html.body.hash.sha256%0AFROM%0A++http_history%0AWHERE%0A++ip+%3D+%2745.83.180.113%27%0A++AND+port+%3D+8080%0A++AND+html.head.title+%3D+%27Secure+Document+%E2%80%94+Action+Required%27%0A++AND+timestamp+%3E%3D+%272026-10-21%27%0A++AND+timestamp+%3C+%272026-11-03%27%0AORDER+BY%0A++timestamp+ASC%0ALIMIT%0A++500&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
Output example:

Figure 28: Repeated observations of the document-themed page on port 8080. The capture shows the title Secure Document, Action Required on the original host's port 8080 at several dates from 21 October through 2 November. It supports repeated observations of the title, without showing that every response body was byte-identical.
Pivoting on the login page’s etag shows where else the same page appeared, including port 7443.

```huntsql
SELECT ip, port, timestamp, http.headers.etag, http.redirected.url
SELECT ip, port, timestamp, http.headers.etag, http.redirected.url
FROM http
WHERE http.headers.etag = '"6abf81c9-249"'
 AND http.redirected.url LIKE '%/new/login'
 AND timestamp > '2025-11-03'
LIMIT 100
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT+ip%2C+port%2C+timestamp%2C+http.headers.etag%2C+http.redirected.url%0ASELECT+ip%2C+port%2C+timestamp%2C+http.headers.etag%2C+http.redirected.url%0AFROM+http%0AWHERE+http.headers.etag+%3D+%27%226abf81c9-249%22%27%0A+AND+http.redirected.url+LIKE+%27%25%2Fnew%2Flogin%27%0A+AND+timestamp+%3E+%272025-11-03%27%0ALIMIT+100&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
Output example:

Figure 29: HTTP search rows showing the configured host on port 7443. The capture shows several rows for the host on port 7443. Together, source configuration, the certificate, page title, and HTTP metadata strengthen the service association. They do not establish a successful implant callback.
Taken together, the hosts and certificates map one operation. Who runs it is a separate question, and a more cautious one.

## Attribution: Chinese-speaking operators, a Russian toolkit

We are not tying this to a named group, and nothing here points to a state sponsor: this section is an assessment drawn from indicators in the files, not a validated attribution.

The independent technical validation of this corpus deliberately did not assign a nationality or location, and that caution is right. The indicators are present and point one way: a financially motivated, Chinese-speaking crew operating in the UTC+7 band, using a toolkit that is not its own.

Across the three collections, the operators' own scripts carry Chinese comments and Chinese resource names far more than Russian. The Russian sits inside the shared toolkit, the exploit and password-cracking utilities.

The hands-on work, the recon, the RDP-resilience checks, and the log triage are written and commented in Chinese. The simplest read is a Chinese-speaking crew running an exploit and C2 kit whose source was written by a Russian speaker, bought or borrowed rather than built. A host-health script on the third node sets its timezone to UTC+7 and buckets activity into Thailand and Vietnam office hours.

The core business reads as gambling and spam, with enterprise intrusion layered on top as opportunistic expansion: a betting-platform admin database, link-farm keywords, crypto-wallet scanners, and romanized-Chinese management panels. One caution worth keeping: language and timezone in code tell you who wrote and ran the code, not a nationality or a flag.

We read this as a Chinese-speaking, Southeast Asia-based cybercrime operation running a Russian-authored toolkit. For defenders, the practical question is less who they are than how to catch them.

## Detection and response

- Inventory and lock down the remote-access edge: Citrix NetScaler, FortiGate SSL VPN, Exchange and OWA, VPN portals, and SSO. Patch the CVEs listed below and get management interfaces off the internet.
- Treat credential-stuffing on VPN and Citrix gateways as expected. Enforce MFA, alert on NetScaler 4009 bursts and spray patterns, and watch for reuse of breach-compilation pairs.
- Audit cloud storage: rotate and scope Azure SAS tokens tightly, alert on long-lived tokens and bulk blob enumeration, and review container access policies.
- Watch for NTLM relay and coercion activity (PetitPotam, Responder, mitm6). Enforce SMB signing and LDAP channel binding.
- Review Java application servers for unexpected JDBC providers. A service-provider descriptor naming a com.microsoft.sqlserver.jdbc.TlsChannelFix class, or a sqljdbc42 JAR that does not match a known vendor build, is worth pulling and inspecting.
- Hunt for a created local admin account named svc\_audit, for the launcher's temporary-EXE pattern under the Windows temp directory, and for outbound connections to the callback domain and Mythic host below. Treat the Net Monitor for Employees Professional agent port as context, not a standalone indicator.
- Block and alert on the network indicators below, after confirming current ownership.

The mapping below places these behaviors against MITRE ATT&CK.

## MITRE ATT&CK mapping

This is a conservative subset tied to the reviewed artifacts: technique presence does not establish success; code capability is distinguished from observed outcome.

| Tactic | Technique | ID | Evidence and state | 
|---|---|---|---|
| Reconnaissance | Active Scanning: Vulnerability Scanning | T1595.002 | Mass scan hit-lists, php2shell and actuator sweeps (capability) | 
| Reconnaissance | Gather Victim Identity Info: Credentials | T1589.001 | Firm credential pairs from a breach-compilation service | 
| Resource Development | Acquire Infrastructure: VPS | T1583.003 | BlueVPS and Limestone staging hosts | 
| Resource Development | Develop Capabilities: Malware | T1587.001 | TlsChannelFix JDBC provider; Apollo-derived and Poseidon-derived payloads | 
| Initial Access | Exploit Public-Facing Application | T1190 | Citrix, FreePBX, php2shell, Exchange (CVE-2026-62911), FortiOS (CVE-2026-22153), TightVNC (CVE-2024-42049) and LFI exploit/probe logic (capability) | 
| Execution | Command and Scripting Interpreter: Windows Command Shell | T1059.003 | Java beacon command execution path (code capability) | 
| Execution | Command and Scripting Interpreter: PowerShell | T1059.001 | Recon and console-command content (capability / saved artifact) | 
| Persistence | Create Account: Local Account | T1136.001 | svc\_audit account-creation command, console-reported zero exit | 
| Credential Access | OS Credential Dumping: NTDS | T1003.003 | IFM creation output; separate large Kerberos-key export | 
| Credential Access | Credentials from Password Stores | T1555 | Browser stores and exports; AI-tool credential files indexed on victim hosts | 
| Credential Access | Brute Force: Password Cracking | T1110.002 | ntcand.py candidate generation against MFLLC hashes | 
| Credential Access | Adversary-in-the-Middle: SMB/LDAP relay | T1557.001 | Responder, krbrelayx, mitm6, ntlmrelayx (capability) | 
| Credential Access | Brute Force: Credential Stuffing | T1110.004 | Simpson Thacher NetScaler VPN stuffing (all failed) | 
| Discovery | Remote System Discovery | T1018 | Computer-object discovery in recon script | 
| Collection | Data from Cloud Storage | T1530 | vslist.py listing the MFLLC Azure container with a live SAS token | 
| Collection | Data from Network Shared Drive | T1039 | AD database and hives staged from an internal share | 
| Command and Control | Application Layer Protocol: Web Protocols | T1071.001 | Java HTTPS beacon and HTTP transfer path (code capability) | 
| Command and Control | Remote Access Software | T1219 | Net Monitor for Employees Professional clients, with command evidence | 
| Command and Control | Protocol Tunneling / Proxy | T1572 / T1090 | Chisel; authenticated SOCKS relays; Mythic SOCKS | 
| Exfiltration | Exfiltration Over C2 Channel | T1041 | Recon-file chunked transfer logic; full delivery not confirmed | 

The concrete indicators behind those techniques follow.

## Indicators of compromise

| Artifact | Bytes | SHA-256 | Interpretation | 
|---|---|---|---|
| gkbd-cache.bin | 7,716,744 | c1d26614cb1469e0651435a8e6301f6e38d4fa0add4fea138fe708e6669a2c33 | Linux ELF, Poseidon Go module and HTTP config; no execution verified | 
| dbmaint.fix | 2,109,952 | 5ec1fe899277b0f489fcc20783abb3385e7f15b23bcaf44832ad57379ee13371 | XOR-obfuscated payload; decoded bytes match the next row | 
| q4final.exe | 2,109,952 | 36c89cddd8e9edb4f7f2a88e86d828a33428247a75e55e4c2252f06a033e44ca | Apollo-derived; decoded from dbmaint.fix; not executed in this review | 
| sqljdbc42beacon.jar | 9,664 | e1d539437644e653a5b2dbf43bd1be03505b5997979c1f7229724e4ea9236228 | Java artifact with the malicious TlsChannelFix provider | 
| sqljdbc42v8.jar | 5,944 | 41f34eed79c86341006666612500ae60e95da761ee04332d3601e3a181083cdf | Java artifact, same provider identity; assess behavior per variant | 
| nmep\_cmd3.py | 3,213 | d4effaf9967404eaf833bdc97a9e2575fc91c686e2f048fd9c7fd07153709232 | Custom Net Monitor client; source hash as an artifact identifier | 

### Network artifacts and scope

| Indicator | Type | Context | Action | 
|---|---|---|---|
| 45.83.180\[.\]113 | IPv4 | Operator host A/B (BlueVPS, AS62005); open dirs :8000, :19001, :8899, :8080; beacon :8443 | Block after confirming current ownership | 
| 91.236.230\[.\]9 | IPv4 | Operator-named second VPS ("vps2, heavy tasks") in README-RULES.txt | Investigate | 
| 74.63.203\[.\]115 | IPv4 | Operator host C (Limestone, AS46475); open dir :18111 | Investigate; relationship to A/B unresolved | 
| 45.83.182\[.\]68 | IPv4 | Mythic-labelled service :7443; cert subject lababalbaba.com | Historical C2 hunt; confirm ownership before action | 
| lababalbaba\[.\]com | Domain | Poseidon callback and hosts-file mapping to 45.83.182\[.\]68 | Historical host-configuration and DNS hunt | 
| sb-it-support\[.\]com | Domain | Associated with 45.83.182\[.\]68; User Portal page on :8089 | Investigate; tenancy not confirmed | 
| 101.99.92\[.\]128 | IPv4 | Authenticated SOCKS relay (B client config); :35045 | Historical relay hunt | 
| 194.213.18\[.\]54 | IPv4 | Proxy configuration in A; :16252 | Historical relay hunt | 
| TCP/7002 | Port | Mythic SOCKS listener named in the rules file | Hunt | 
| TCP/56777 | Port | Operator SSH | Hunt | 

### Certificates and keys

| Indicator | Type | Context | 
|---|---|---|
| 1ba2ec04908a4c4696f2f740f04588708c0c3afc7efbebc0aa69f39b78fc535b | TLS cert SHA-256 | lababalbaba.com, observed on 45.83.182\[.\]68 ports 443 and 7443 | 
| 9b325e75e840b7c6d7505f57ec527d680b786cc948fa0eff3850412706f4db89 | TLS cert SHA-256 | sb-it-support.com, User Portal on :8089 | 

CVEs present in the recovered files, with the tooling that references each:

| CVE | Target / product | Referencing tooling or note | 
|---|---|---|
| CVE-2019-19781 | Citrix NetScaler | Citrix exploit scripts (incl. stb\_19781.sh) | 
| CVE-2025-5777 | Citrix NetScaler (CitrixBleed 2) | Citrix NetScaler tooling | 
| CVE-2025-57819 | FreePBX | FreePBX exploit logic | 
| CVE-2026-109618 | php2shell (PHP RCE) | php2shell scanner output vs external hosts | 
| CVE-2026-109619 | php2shell (PHP RCE) | php2shell scanner output vs external hosts | 
| CVE-2026-62911 | Microsoft Exchange, MRSProxy pre-auth RCE | cve62911\_poc.py | 
| CVE-2024-42049 | TightVNC | tvnc\_ctrl.py | 
| CVE-2026-87902 | LFI driver | lfi.py | 
| CVE-2026-22153 | FortiOS, LDAP auth bypass | fg\_ldapbypass.sh | 
| CVE-2021-42278 | Active Directory (sAMAccountName / noPac) | AD relay and Kerberos kit | 
| CVE-2021-36942 | PetitPotam (AD coercion) | AD relay and Kerberos kit | 
| CVE-2017-8563 | Active Directory / LDAP relay | AD relay and Kerberos kit | 
| CVE-2020-1472 | Zerologon (Netlogon) | AD relay and Kerberos kit | 

The separate fg.sh is a FortiGate credential login check. CVE-2025-6543, CVE-2023-27997 and CVE-2021-1675 were in an earlier draft but do not appear in the recovered files and were removed.

Scope note: these are historical observations from the recovered material, not claims that the addresses are currently malicious. Victim domains, internal addresses, third-party downloaders, the commercial monitoring vendor's services, and unverified panel domains are excluded from the block set.

TCP 4495 alone is not an indicator, and a normal AI-application path is not evidence of compromise. The table below places every organization in the corpus on one scale, from confirmed access to reconnaissance.

## Victim and target summary by evidence strength

We put every organization from the report into one picture, ranked by how strong the evidence is. The top tier is confirmed: data or access already in the operators' hands. Everything below it is weaker, active attempts, harvested credential lists, and targets that show up only in a scan. Keeping those apart is the difference between reporting a breach and reporting a target.

The graphic is the fast read, the table below gives the basis for each placement, the exact files, logs, or captures behind it, so every tier can be checked against the source rather than taken on trust.

| Organization | Region | Status | Basis | 
|---|---|---|---|
| Large US hospital system | US | Data and credentials in operator hands; recorded VPN session | 8,460-address directory, 3,570-record auth dump, phpinfo capture, separate hospital VPN log; acquisition and validity not established | 
| US manufacturer (internal identity held) BRAC University | US | Cloud storage listed with live token; hashes attacked | Azure container enumerated via live SAS token; own QuickBooks file and domain in the listing; NTLM candidates generated | 
| Bangladeshi university | Bangladesh | Breached | Large Kerberos-key export (35,601 records); hands-on PtH and DPAPI collection | 
| Swiss tax office (domain TABT) | Switzerland | Domain DB and hives staged | IFM creation and copy to staging; NTLM relay; printer and share loot | 
| Pediatric / academic-medical set (\~54 institutions) | US and intl | Harvested | 153-record credential list reused from a third-party breach compilation | 
| Simpson Thacher & Bartlett | US | Attacked, no success | Credential-stuffing, Citrix CVE-2019-19781, SQLi, SMTP relay test, service probing; all captured results failed | 
| \~563 US law firms (60+ named AmLaw) | US | Targeted | VPN, Citrix, client-portal edges enumerated | 
| US federal agencies: HRSA (incl NPDB, 340B), SBA, NEA, NSF, NCUA | US | Targeted | Probed in recon sweep; mostly 403, some live portals | 
| US enterprises: Hertz, Plaid, Oportun; UNC School of Government | US | Targeted | Live edges catalogued; credential-check script | 
| Children's-hospital REDCap servers | US | Targeted | Active hunting list | 
| University medical/health subdomains | US | Targeted | Actuator endpoints probed; status 200/403 mix, no disclosure established | 

## Conclusion

One set of exposed directories gave up a US hospital system's credential and web-tier material and a recorded gateway session, a US manufacturer's cloud object listing taken with a live token, a full enterprise-intrusion kit, a malicious JDBC-to-Apollo execution chain and a Poseidon implant, and a target project that runs from hundreds of law firms into federal agencies. The strongest findings connect inspected mechanisms with retained artifacts; the files support several operational workflows without proving one continuous intrusion across every environment.

The records do not establish AI-led exploitation or a planned sequence of future victims. The US healthcare and manufacturer impact needs disclosure now. The law-firm and agency work is still at the edge, which is exactly the VPN, Citrix, and portal surface defenders can watch.

[Find more Apollo, Poseidon, and Mythic infrastructure like thisThis crew chained a malicious JDBC driver into an Apollo payload, ran a Poseidon implant on Linux, and kept a Mythic C2 one certificate hash away. See how Hunt.io pivots across hosts, certs, and callback domains to catch the next build before it hits a blocklist.Book a Free Demo Now](https://hunt.io/get-started)

**Disclosure: We notified CISA and shared an advance copy before publishing, for coordination with the affected victims. Organizations with confirmed compromise or data access are generalized to sector. Organizations that were only targeted, scanned, or appeared in reused third-party credential lists are named as targets, not as breach victims.**

An exposed [open directory](https://hunt.io/glossary/open-directories) is one of the more useful mistakes an operator can make, showing the work in progress: the tooling, the target lists, the logs, and the loot.

The Hunt.io threat-research team surfaced three of them through [AttackCapture™](https://hunt.io/features/attackcapture) scanning and recovered their full contents. They belong to an active intrusion crew, and the operators' own files carry both the human stakes and the tooling: hospital account material and a recorded VPN session, a US manufacturer's cloud storage opened with a live token, reconnaissance across the US legal and government sectors, and a malware set running from a malicious Java database driver to an Apollo-derived Windows payload and a Poseidon Linux implant.

Everything below is drawn from the crew's own files, cited by IP, port, and path, with credentials, tokens, and personal data redacted and no recovered program executed. We separate what the code can do from what the logs actually record, because the extent of compromise differs sharply between environments.

The findings start with what matters most, the confirmed US impact, then work through the toolkit, the wider targeting, and the infrastructure.

## Key findings

Named is not breached. The law firms, federal agencies, and institutions named in this report were targeted, enumerated, or pulled from a reused credential list, not compromised by this operator. Confirmed access and data already taken are limited to the findings marked as such below, starting with University Hospitals and the US manufacturer.

- **A US hospital's data is in the operators' hands**: a large US hospital system’s staff credentials, an 8,460-address directory, a web-server phpinfo capture, and a separately recorded hospital VPN session. This is not a proven domain login or patient-data loss.
- **A US manufacturer's cloud storage was accessed**. The crew listed its Azure container with a live SAS token, capturing 155,568 object names including QuickBooks files, and ran its Windows hashes against a custom wordlist. Objects were listed, not downloaded.
- **US law firms and federal agencies are next**. Several hundred firms are enumerated at the remote-access edge, one is under active attack, and the same sweep reaches HRSA, SBA, NEA, NSF, and NCUA. This is targeting and attempts, not confirmed breach.
- **A malicious JDBC driver chains to an Apollo payload**. A TlsChannelFix class runs when a Java app loads it, and a launcher XOR-decodes a packed file into an Apollo-derived Windows executable. A separate Linux artifact is a Poseidon build.
- **Sensitive stores were retained**: 414 keystroke-log rows and 35,601 Kerberos key records across 11,867 principals. These are record counts, not victim totals.
- **The C2 mixes custom and commercial tooling**: a custom Java HTTPS beacon plus clients for Net Monitor for Employees Professional, a bought product, over authenticated SOCKS relays. Its agent port is not a standalone indicator.
- **Two foreign domains show deep access**: a Bangladeshi university's Kerberos material exported at scale, and a Swiss tax office's domain database and hives staged off an internal share. Neither is US.
- **The crew runs AI coding tools and collects victims' AI credentials**. Agentic AI clients run in its own environment, and scripts index Claude and OpenAI Codex credential files on victim hosts. No AI action is tied to a specific exploitation step.

## Three open directories and a shared toolkit

Hunt.io researchers discovered three open-directory endpoints. For source references, A denotes [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001), B denotes [45.83.180\[.\]113:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:8000), and C denotes [74.63.203\[.\]115:18111](https://portal.hunt.io/attackcapture/filemanager?host=http://74.63.203.115:18111).

A and B share an IP, giving two initial host profiles; C is a separate host whose relationship to the first two is kept open until independent evidence supports a stronger link. The three primary collections contain 2,115 files and 1,981 distinct hashes. Co-discovery does not establish common ownership.

Fig 01. Those totals come from three servers. The rest of the report walks them in order, beginning with the servers themselves.
A rules file left on host A, /README-RULES.txt at [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001), shows a shared box with multiple operators working separate branches:

```bash
VPS USAGE RULES (approved by operator 2026-10-25)
Point model: MAIN = operator Windows box (kit/loot/secrets live only there).
vps1 = 45.83.180.113 (Tallinn) workhorse; vps2 = 91.236.230.9 heavy tasks.
1\. File/process prefix = branch: vc_* = vCenter, nw_* = netway/vCloud, bd_*/nmep_* = BD.
6\. Traffic to victim nets only via proxychains4 -> Mythic socks :7002.
7\. Finishing a branch: remove own /root/<prefix>*, close tmux, drop own cron lines.
```
                Copy
The staged kit is a full enterprise-intrusion chain. The exploit CVEs actually present in the files, grouped by target:

- Citrix NetScaler: CVE-2025-5777, CVE-2019-19781
- FreePBX: CVE-2025-57819
- [php2shell](https://hunt.io/blog/php2shell-cve-2026-109618-109619-open-directories): CVE-2026-109618, CVE-2026-109619
- Active Directory and relay: CVE-2021-42278, CVE-2021-36942 (PetitPotam coercion), CVE-2017-8563, CVE-2020-1472 (Zerologon)

The [FortiGate](https://hunt.io/blog/thai-broadband-fortigate-sslvpn-meshcentral-intrusion) is hit two ways: a credential login check and a FortiOS auth-bypass probe. The login-check script fg.sh posts to /logincheck and, on success, queries the SSL VPN monitor API, while fg\_ldapbypass.sh probes the [CVE-2026-22153](https://nvd.nist.gov/vuln/detail/cve-2026-22153) LDAP empty-password bypass.

Three more exploit scripts sit alongside the list above: a Microsoft Exchange MRSProxy pre-auth RCE (CVE-2026-62911, cve62911\_poc.py), TightVNC (CVE-2024-42049, tvnc\_ctrl.py), and an LFI driver (CVE-2026-87902, lfi.py on host C).

The rest of the kit is standard: PetitPotam, krbrelayx, [Responder](https://hunt.io/malware-families/responder), PKINITtools, mitm6, Impacket, netexec, DonPAPI, and an LDAP relay-scan toolkit, with Microsoft 365 spraying (o365spray) and movement tooling (Chisel, proxychains). Their presence establishes availability, not successful operation against any named target.

The clearest impact sits not in this kit but in what the crew already took, starting with a US hospital.

## US healthcare: what is in the operators' hands

### University Hospitals

The primary healthcare victim is a large US hospital system. Collection A holds a loot file of 8,460 unique nonempty addresses, including 6,929 at the hospital’s primary domain and 513 at an affiliated academic medical domain, plus a separate 3,570-record authentication dump and a web-server phpinfo capture.

We are not reproducing any of that data. The per-domain address counts from /loot\_uh\_emails.txt at [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001), with no addresses shown, make the scale and the target plain:

```bash
  6929 primary hospital domain
  513 affiliated academic medical domain
  259 other domains
```
                Copy
A companion script separates the hospital’s two mail domains for targeted replay. A caution from the code itself: the credential-type checks submit usernames and discovery fields, not passwords, so neither the check nor its response proves a working login.

The format, acquisition origin, and current validity of these records are not established by the files. This is hospital credential material and a web-tier capture in the crew's possession, not a demonstrated interactive compromise.

Figure 1: Username discovery request to Microsoft's identity endpoint. The request contains a username and discovery flags. There is no password field in this request. It therefore cannot demonstrate that a password worked or that the account completed a sign-in.
### A recorded hospital VPN session

Separately, a US hospital-network VPN log records an ESP tunnel and a private address. Gateway logs of this kind support a session at a particular time: establishment, rekeying, dead-peer detection, fallback, and termination.

They do not establish continuous access through a configured expiry, and the accompanying failed-relay log cannot establish later internal access. We keep the VPN session, the credential lists, and the phpinfo capture as separate trails rather than merging them into one authenticated compromise.

### A pediatric-research credential set

A separate loot file holds 153 email-and-hash records for staff across roughly 54 children's hospitals and pediatric and oncology research centers, spanning 62 email domains. Most are US institutions.

The best-known names in the set include St. Jude, Children's Hospital of Philadelphia, Children's Hospital Los Angeles, Seattle Children's, Texas Children's, Cincinnati Children's, Johns Hopkins, Stanford, Duke, and Dana-Farber, with others alongside them. The records read as an account list reused from a third-party breach compilation, not a breach of any one of these institutions. These are credentials the crew collected, not evidence it got inside each hospital.

### The children's-hospital hunting list

Beyond what was already collected, A carried an active hunting list aimed at clinical-research infrastructure. These are REDCap servers, the data-capture platform hospitals use for research studies, from /hunt\_targets.txt at [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001):

```bash
redcap.shepherd.org          redcap.providence.org
redcap.atlantichealth.org    redcap-dev.research.bcm.edu
redcap.bmhcc.org             redcap-sctx.seattlechildrens.org
redcaphcm.stonybrookmedicine.edu  redcappoc.luriechildrens.org
researchredcap.luriechildrens.org  redcapwap.archildrens.org
```
                Copy
Same method as the law-firm list below: choose a sector, enumerate its exposed services, work the list.

### Medical-sector endpoint probing

The operators also sweep for exposed Spring Boot management endpoints, including across a university's medical and health subdomains. A university-related filter for /actuator/heapdump, /actuator/env, and /.env yields 9,195 records, of which 6,365 are status 403 and 96 are status 200.

Titles include ordinary pages, errors, and challenges, and a status 200 here does not establish disclosure. This is attempted probing of the medical-education sector, not confirmed access. The firmest US impact in the whole corpus is not a hospital at all, but a manufacturer.

## A US manufacturer: cloud storage listed, hashes attacked

The crew also worked a US manufacturer tracked by the codename MFLLC, through cloud-storage enumeration plus on-premises hash cracking.

A script, vslist.py, lists objects in a Microsoft Azure blob container (vsyd220.blob.core.windows.net/mfllc) with configured SAS parameters, follows the listing continuation marker across up to 300 pages, aggregates prefix sizes, and writes the object names to a local file. It also searches names for NTDS-related strings.

The implementation lists and sizes objects; in the recovered form it neither downloads their bodies nor deletes them, and its token was not tested. What it does establish is that the operator held working keys to the company's cloud storage and walked its contents.

Figure 2: Parsing Azure object metadata and following the listing continuation marker. The loop reads XML fields from a listing response. It stores names, counts files by prefix, and adds the listed sizes. The continuation marker requests another page of metadata. This fragment does not request the contents of those objects.Figure 3: Saving object names and calculating totals from listed sizes. The saved output is a name list and summary statistics. GiB is calculated from listed sizes. It is not a counter of bytes downloaded from the container. The SAS token and its signature are excluded from the excerpts.
A second script, ntcand.py at [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001), builds NTLM-hash candidates from the company's own terms:

```bash
base = ["Rochelle","Owen","Nate","Southern","Meridian","Fence","Jacob","Travis",
        "inventory","MFLLC","Weld","welding","Shop", ...]
cands += ["Rochelle!02","Meridian2026","Fence#1","Idaho2026","Welcome1","Winter2026", ...]
```
                Copy
The seed words alone are leads, not identification. The stronger identification is in the stolen listing itself: the object names include the company's QuickBooks company file and its domain, which point to a US manufacturer.

Hash-candidate generators do not establish successful cracking or access to an on-premises domain, so we hold the cloud-listing impact separate from the hash work. Outside the US, the same operators show what full interior access looks like when they get it.

## Outside the US: a Bangladeshi university and a Swiss tax office

Outside the US, the same corpus shows how far the crew gets once inside. We report these briefly; they are the capability proof, not the focus.

A Bangladeshi university had its Kerberos key material exported: 11,867 records in each of AES256, AES128, and DES formats, 35,601 records across 11,867 principals, including machine accounts. The crew worked it hands-on, with a pass-the-hash loot-mapping run across internal workstations and a DPAPI collection run. The export does not identify its own acquisition mechanism, and the reviewed domain-dump log lacks a successful DCSync, so we describe this as a recovered large-scale key export with hands-on lateral movement, not a one-click DC dump.

A Swiss tax office (internal domain TABT, 192.168.151.x) is covered by the IFM (install-from-media) workflow. A log reports ntdsutil install-from-media creation; a script copies the domain database and registry hives from a controller share to staging, XOR-decoding bytes with 0xA5, then requests IFM removal.

The recorded byte counts (a 33,554,432-byte database, 17,563,648-byte SYSTEM, 65,536-byte SECURITY) describe the staging step. Complete off-host transfer is not independently confirmed.

This environment is also where the operator's printer files and an NTLM-relay run (ntlmrelayx against ldap://192.168.151.1) belong. With those results behind them, the crew pointed the same toolkit at the US legal sector.

## US law firms and federal agencies: the sector in progress

With hospital and manufacturer data already in hand and two foreign domains dumped, the crew pointed the same toolkit at the US legal sector. Most of it is reconnaissance; one firm has moved into hands-on attack.

A legal-sector seed list holds 563 unique entries, and the HTTP sweep catalogues live remote-access front doors across more than 60 named firms, including Kirkland & Ellis, DLA Piper, Latham & Watkins, Dentons, Skadden, Jones Day, Sidley Austin, Gibson Dunn, White & Case, Morgan Lewis, Mayer Brown, Weil Gotshal, Cooley, Baker Botts, Troutman Pepper, Littler Mendelson, Jackson Lewis, K&L Gates, Holland & Knight, Greenberg Traurig, Crowell & Moring, Orrick, Wilson Sonsini, Quinn Emanuel, Morrison Foerster, and more.

Live remote-access endpoints from the httpx sweep, /comm\_web.txt at [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001):

```bash
https://a1-vpn.jonesday.com         [200]  [HSTS]
https://access.morganlewis.com      [200]  [Morgan Lewis Remote Access Portal] [Azure]
https://1-vpn-net-1.littler.com     [200]  [HSTS]
https://02fw1.honigman.com          [200]  [HSTS]
http://citrix.stblaw.com            [200]  [Apache]
http://citrixna.sidley.com          [307]  [Azure Front Door]
http://clientportal.mayerbrown.com  [301]  [Apache]
http://globalportal.dentons.com     [307]  [Azure Front Door]
```
                Copy
That is the remote-access edge, VPN, Citrix, and client portals, catalogued across the AmLaw list. It is the step right before the Citrix and Fortinet exploits staged on the same box.

Dedicated law directories and per-state scan folders show the crew working the sector down by state and specialty. These are enumeration counts, not organization or breach counts.

### Beyond law firms

The same recon run reaches past the legal sector. Associated web output contains 22,312 lines, with 22,250 parser-matched records and 1,051 .gov URLs across 536 hostnames.

Named in the sweep are federal agencies including HRSA (hrsa.gov, including the National Practitioner Data Bank and 340B systems), SBA (sba.gov), NEA (arts.gov), NSF (nsf.gov), and NCUA (ncua.gov), a university governance body (UNC School of Government), and large US enterprises (Hertz, Plaid, Oportun). Most responses are redirects or access-denied (often 403 behind Akamai or Cloudflare).

These are probes: targeting, not access. The .gov and legal counts are not organization or breach counts.

### One firm singled out

For at least one firm the crew went well past cataloguing. Simpson Thacher & Bartlett (stblaw.com) has a cluster of operator files that read like a worked attack plan: around 100 staff email and password pairs from a public breach-compilation service (pn\_stb\_lines.txt holds 99 lines), credential-stuffing against two Citrix NetScaler VPN gateways, the Citrix [CVE-2019-19781](https://www.citrix.com/blogs/2019-12/citrix-adc-citrix-gateway-cve-2019-19781-vulnerability) exploit (stb\_19781.sh), SQL injection against a firm web app, username enumeration, an SMTP open-relay test, and probing of its ServiceNow tenant and other services.

Every captured result shows failure. The VPN credential-stuffing returned invalid-credential errors (NetScaler 4009) and no session, and the leak tests logged no leak.

A caution on the success heuristics: two of the Citrix check scripts default an absent Location header to an empty string and then treat the absence of index.html as a positive, so a missing redirect can produce a false hit in either direction. SAML and Duo text in a response is not proof of accepted credentials or completed MFA.

So we have no evidence Simpson Thacher was breached. What we have is a named AmLaw firm under a sustained, multi-vector attack.

Figure 4: A Citrix response heuristic that can misclassify a missing redirect as success. When the response has no Location header, loc becomes an empty string. That string does not contain index.html, so this condition can return a hit without proving a successful login. A printed success label needs independent evidence.
To be precise about the wider claim: there is no law-firm loot on these servers and no firm in a verified-hit result. Most of the several hundred firms are at the enumeration stage, one is under active attack, and none shows a confirmed breach.

What makes the sector work serious is the company it keeps. The same operators, with the same toolkit, already hold a US hospital system's credentials and web-tier artifacts, have listed a US manufacturer's cloud storage with a live token, and have taken deep access in two foreign domains. How they get in is the weakest-evidenced part of the picture, and it is where we turn next.

## Initial access: more post-access than entry

The files show substantially more post-access activity than original entry. University material already contains monitoring access and credentials; the Swiss output begins after execution is available. Neither explains how access was first obtained.

The Citrix, FreePBX, and PHP-related sources include probes, attempted exploit logic, and external-tool references. The FreePBX evidence is broader than a wrapper reference: one script directly constructs an EXTRACTVALUE SQL-error probe, and another tests module-dispatch responses.

The referenced complete exploit is outside the preserved tree. A direct SQL-injection attempt is implemented in source; no successful database disclosure, command execution, or validated CVE assignment follows from that source alone. The same caution applies to a QuickBooks browser check whose branding-text heuristic can match a login-page footer, and to PHP session-file injection and REDCap import experiments whose response markers can be satisfied by reflection rather than execution.

A VPN cookie-forging script constructs an RSA-encrypted identity and time cookie, and a companion attempts tunnels and private-port checks. Source construction and recorded session events do not independently prove an authentication bypass or identify which credential mechanism produced each session.

Support-form delivery scripts prepare pretext messages under a persona with links to a listener; no matching submission, click, or resulting access was established. What the files show far more clearly is what runs after access, starting with a malicious database driver built for code execution.

## Execution through a malicious JDBC provider

Collection A contains generators for a class named com.microsoft.sqlserver.jdbc.TlsChannelFix. The class implements java.sql.Driver; its static initializer and constructor both invoke a boot routine. The generator also writes a service-provider descriptor naming the class:

```bash
META-INF/services/java.sql.Driver
    com.microsoft.sqlserver.jdbc.TlsChannelFix
```
                Copy
The descriptor was independently confirmed inside both inspected JARs (sqljdbc42beacon.jar and sqljdbc42v8.jar). In a compatible application environment, loading the provider starts the malicious routine.

This supplies a path to repeat execution when the application loads the JAR, subject to its classpath and runtime configuration. It does not require a separate scheduled task.

Figure 5: The JDBC provider calls its startup routine during initialization and construction. The class registers itself with DriverManager, but the malicious routine has already been invoked. The constructor therefore matters as an execution trigger, even though the driver methods do not provide a useful SQL connection.
The Python generator also creates the service-provider file, linking the Java class to the discovery mechanism:

```bash
os.makedirs('/root/jbeacon/META-INF/services', exist_ok=True)
open('/root/jbeacon/com/microsoft/sqlserver/jdbc/TlsChannelFix.java', 'w').write(src)
open('/root/jbeacon/META-INF/services/java.sql.Driver', 'w').write('com.microsoft.sqlserver.jdbc.TlsChannelFix\n')
```
                Copy
Writing the descriptor is not a deployment result; actual execution still depends on the application finding and loading that JAR.

The driver interface is largely a facade: connect() returns null, acceptsURL() returns false, and jdbcCompliant() returns false. The meaningful behavior occurs during initialization, before the object needs to provide a database connection.

An AtomicBoolean guard limits startup to the first successful compare-and-set in that loaded class, set before initialization completes, so an exception can leave startup incomplete without a retry. The guard is not a machine-wide lock and does not coordinate separate JVMs or classloader copies.

Figure 6: Stub JDBC methods provide the expected interface without a working database connection. Inside boot(), an atomic flag limits startup to the first successful compare-and-set in that loaded class. The daemon worker it starts cannot keep the JVM alive after application threads exit, and broad Throwable handlers suppress failures without resetting the guard.
### The file-decoding launcher and the Apollo payload

A separate generator reads a local dbmaint.fix file, XOR-decodes it, writes an executable under the Java temporary directory, and starts it with ProcessBuilder. Saved runtime output records the sequence on 14 October at 15:58:57 CEST: initialization, a 2,109,952-byte executable written under C:\Windows\TEMP, and process creation.

The same three-line event appears in several copied logs and must be counted once. This is direct evidence of the launcher event the logs report, not evidence that the HTTPS beacon variant also completed a polling cycle.

We independently confirmed that XOR-decoding dbmaint.fix with 0x5A produces the exact bytes of q4final.exe. Both hashes appear in the indicator appendix.

Figure 7: The launcher decodes bytes with XOR, writes an executable and starts a child process. The routine waits, logs a marker if its input is missing, otherwise reads and XOR-decodes it. The destination combines the Java temporary directory, an encoded prefix, a random hexadecimal suffix, and an extension. The log follows ProcessBuilder.start(), supporting recorded process creation rather than callback or task completion.
The managed q4final.exe has an obfuscated outer entry point, 101 type definitions, and 854 method definitions. Offline raw-DEFLATE extraction recovers 17 managed assemblies plus metadata.

ApolloInterop, Tasks, HttpProfile, and cryptographic components correspond to upstream Apollo architecture, supporting Apollo derivation with high confidence rather than relying on the assembly name. Task and transport names are an inventory, not proof that every handler ran. A verified runtime command-and-control configuration remains unresolved.

The HTTPS and launcher paths share a provider identity but do different work, and we keep their evidence separate:

```bash
JVM loads service provider
        |
        +--> HTTPS variant: poll queue -> cmd.exe -> post output
        |
        +--> Launcher variant: read packed file -> XOR decode
                              -> write temporary EXE -> start process
```
                Copy
A third diagnostic variant stages an encoded command file and launches cmd.exe, maps the callback domain lababalbaba.com to 45.83.182\[.\]68, and requests WinHTTP and .NET registry changes. Its transcripts record SYSTEM context and DNS diagnostics but do not establish a completed implant callback.

The Windows side is only half of the payload set. A second implant targets Linux.

## A Poseidon Linux implant

The Java launcher is only part of the recovered payload set. A 7,716,744-byte file named gkbd-cache.bin is a 64-bit Linux ELF.

Its Go build information names [github.com/MythicAgents/poseidon](http://github.com/MythicAgents/poseidon), identifies Go 1.25.1, and includes HTTP-profile build settings. This is strong artifact-level evidence of a Poseidon-derived build. It does not establish that the file ran on an external victim.

Offline decoding of the embedded HTTP configuration exposes the callback domain and timing:

```bash
callback_host      https://lababalbaba[.]com
callback_port      443
callback_interval  3600
callback_jitter    20
post_uri           data
killdate           2027-10-21
```
                Copy
AESPSK and proxy credentials: omitted

These values describe a build, not observed traffic or current infrastructure ownership. Encryption and proxy-secret fields are withheld.

The Apollo cryptographic provider and a DPAPI helper (UnprotectBlob.exe) were read statically as well; neither read exposes a validated key or a recovered plaintext credential. Alongside the implants sits the crew's privileged-execution and credential-access tooling.

## Credential access: NTDS, Kerberos, and DPAPI

SYSTEM selections and diagnostics establish a recorded execution context, not an exploited privilege-escalation vulnerability. A directly inspected console screenshot shows a command that creates a local account named svc\_audit, adds it to the administrators group, and writes a registry value named LocalAccountTokenFilterPolicy, with a console-reported zero exit status.

A caution on that last step: the screenshot writes the value under HKLM\SYSTEM\CurrentControlSet\Control\Lsa, while Microsoft documents the remote-UAC policy under a different path (HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System). So the command records account creation and a zero exit, but is not sufficient evidence that remote UAC restrictions were actually disabled. The credential in the original console command is excluded from publication.

For offline password testing, the collection includes NT-hash comparators and NTLMv2 checkers. Two variants contain a more fundamental defect: they calculate the identity component from the uppercased password candidate, leaving the parsed username unused, which differs from Microsoft's NTLMv2 construction. This is a static implementation finding, read from the code; no new password recovery is claimed.

Figure 8: A flawed NTLMv2 calculation uses the password candidate where the username is required. The response-key calculation uses the password candidate plus domain, rather than the required username and domain construction. We identified the error by reading the code; we did not run password recovery.
A recovered PowerShell recon script builds a local report using whoami /all, cmdkey /list, klist, quser, domain-controller queries, directory searches, and administrator-group queries. Listing saved-credential references is not the same as extracting plaintext passwords, and the script writes results and errors to a temporary file, so its presence alone cannot establish that each query succeeded.

Figure 9: Enumerating Active Directory computer objects through DirectorySearcher. The source writes results and errors to a temporary report; its LDAP block records a failure message when the search raises an exception. A result file or command transcript is needed to identify the computers actually enumerated.
Bundled PKINITtools, PetitPotam, and krbrelayx source shows capability availability. A successful coercion, relay, ticket acquisition, and subsequent remote execution would each require their respective outputs; these steps cannot be inferred by joining tool names. What ties the implants and the credential theft together is the channel the crew uses to run commands and move data back.

## Command and control: a Java beacon and a commercial monitoring agent

### The Java HTTPS beacon

The beacon generator implements a small command loop. After a 30-second initial delay it polls an HTTPS endpoint on TCP 8443, sleeps roughly 25 to 35 seconds between polls, passes a nonempty response to cmd.exe /c, and posts the collected output to a second endpoint. Bodies are XORed with 0x5A and base64-encoded; the transport is HTTPS with certificate and hostname checks disabled by the generated class.

Figure 10: Disabling TLS certificate and hostname validation for HTTPS connections. The TLS change affects the default HttpsURLConnection socket factory and hostname verifier in that JVM. It is not scoped to one connection object and is not a Windows-wide trust-store change. This describes a code-level consequence, not a measured effect on other traffic.Figure 11: The byte-wise XOR transformation used by the beacon. Each byte is XORed with the same value, 0x5A. Applying the operation again restores the original bytes. This is obfuscation, not keyed encryption; HTTPS is the transport protection.Figure 12: Polling for a command and submitting its output through separate HTTP paths. The loop acts only on a nonempty command, limits the returned string to 60,000 UTF-16 code units, and posts the result to the response path. This shows the implemented task-and-result flow; the saved launcher log belongs to a different variant.Figure 13: Setting HTTP timeouts and encoding the outgoing request body. The helper converts UTF-8 text to XOR-transformed bytes and then base64, and accepts only HTTP 200 before reading a response. The excerpt is from the recovered Java template; it does not prove this variant completed a live exchange.Figure 14: Running a command through cmd.exe and collecting its output. redirectErrorStream(true) merges stderr into stdout. The worker drains output, checks exitValue(), and appends an exit marker once the process exits. The outer loop checks elapsed time but does not call destroy() when it ends.
On the server side, the GET handler consumes a shared command file rather than selecting a per-client queue, and the handlers do not verify an application-level client credential:

Figure 15: The server retrieves a queued command and removes the queue file. The queue file is removed before the reply is delivered. If several clients poll, the request that consumes the file receives the command. Removing it before delivery also creates a possible command-loss case, though the saved material does not show such a loss.Figure 16: Decoding submitted results and appending them to the server's log. Results and decode errors share one file, recorded with a UTC time but without the client identifier. An HTTP acknowledgement alone does not prove a useful result was retained.
### The commercial monitoring protocol

Collection B contains custom clients associated with Net Monitor f or Employees Professional, a commercial monitoring product. The clients connect to agents on TCP 4495, in B through an authenticated SOCKS5 relay. This is a bought product with custom clients wrapped around it, not a framework the crew wrote, which is why the agent port alone is not an indicator.

Figure 17: Reading a four-byte length prefix before receiving the frame body. The receive loops handle data arriving across several socket reads. The prefix is an unsigned 32-bit big-endian byte count. This is framing logic, not evidence that a frame was authenticated, decrypted, or followed by command execution.
The client reads a four-byte big-endian frame length, reads the body, and processes JSON or encrypted content. Authentication derives a 32-byte key by applying SHA-256 to a configured passphrase, encrypts a challenge with AES-CBC and a random IV, and sends an authentication frame.

B's client supports both encrypted and plaintext command-frame modes; A's client authenticates with AES but sends its command frame as plaintext. The configured passphrase is withheld, and this analysis documents the recovered clients rather than establishing a product vulnerability.

Figure 18: Encrypting the challenge response with AES-CBC and a random initialization vector. The field carries the IV followed by encrypted challenge bytes, represented as hex. This fragment covers authentication; the later command mode must be checked in the client variant that sends it.
Five packet captures contain 51,049 records. Offline parsing identifies candidate monitoring-protocol frames through the configured SOCKS channel, supporting the framing analysis.

Incomplete sessions and capture boundaries prevent treating every frame as authenticated command execution, and no packet-derived victim total is assigned. The same stack also records what the crew collected through it.

## What the crew collected

The monitoring store contains 501 web-log, 842 application-log, 20 user-log, and 414 populated keylog rows. Keylogs share one host value; web logs contain five.

Browser counts are 178 Chrome cookies, 207 Firefox cookies, and 17 Edge saved-login rows, plus a separate Chrome token. Decryption and current usability were not established.

Cloud enumeration reports 542,861 objects and 418.24 GB of metadata-derived sizes, which is not downloaded volume or proof of container deletion. These are stored-record and listing counts, not people or organizations.

A separate media-collection script lists media paths and sizes, retrieves bodies over SMB, hashes them, runs a media classifier, and removes the temporary copies. Its results file records 126 qualifying records across eight addresses. Artwork and document paths appear in the set, and a model label is not a verified description of an image.

Figure 19: Retrieving an SMB file, hashing its contents and applying media-classification thresholds. The script retrieves file bytes, hashes them, and writes a temporary copy for the detector, logging only results that meet its score conditions. The 126 saved records are not a count of every image inspected, and a model label is not a verified content description.
### Exfiltration mechanisms

The recon transfer stage base64-encodes the local output, makes it URL-safe, and splits it into chunks sent inside GET request paths to the server's HTTP listener. A proxy or web server that retains request paths may preserve both the host label and the transferred data, which makes URL logs useful evidence and also sensitive records.

An expanded server access log contains 540 request records from 195 distinct client addresses. A successful HTTP status means the server handled a request, not that a known person received a complete, usable dataset.

The loop catches individual failures without retry or integrity verification, so hostname and chunk count alone cannot establish completeness. A third recovered host adds a different dimension: the crew's own environment and its AI tooling.

## The third collection: virtualization, guest-agent pulls, and AI artifacts

Collection C is a separate host, and we keep it separate until independent evidence supports a stronger link to A and B.

### Local virtualization administration

C's shell history records Proxmox inventory, Windows guests, storage changes, and RDP forwarding. The operators run a small farm of Windows VMs reached over RDP, and the history builds NAT rules that forward external ports to each VM's RDP service and persists them through an interface hook, recorded in /.bash\_history at [74.63.203\[.\]115:18111](https://portal.hunt.io/attackcapture/filemanager?host=http://74.63.203.115:18111):

```bash
dhcp-host=BC:24:11:DF:F5:BF,jkzy,192.168.100.113   # dnsmasq static lease
iptables -t nat -A PREROUTING -i vmbr0 -p tcp --dport 1012 -j DNAT --to-destination 192.168.100.113:3389
iptables -t nat -A PREROUTING -i vmbr0 -p tcp --dport 1099 -j DNAT --to-destination 192.168.100.113:3389
# persisted via /etc/network/if-up.d/sg-rdp-nat and /etc/network/if-up.d/codex-rdp-jkzy
```
                Copy
The VMs carry operator handles (sg12, sg13, sg14, jkzy, sg10v) on 192.168.100.0/24, exposed on external ports 1010 to 1099 and 13389. This is the crew's own hands-on environment, not a victim network. Timezone, language, and installation-media choices on this host do not establish the administrator's nationality or physical location.

### AI applications and configuration artifacts

C contains AI-application paths, configuration files, and a large application log (zz\_main.log) that records agentic AI-coding-client activity in the operators' environment, including a Claude Code client running under a local user, a browser-automation bridge connecting, and an agent-mode session with plugins and a scheduled-task wake claim. Scripts on the same host search for AI-tool authentication and configuration files on other systems, for example a disk-enumeration script whose search roots include a Claude data directory, and a produced file listing that indexes Claude desktop and OpenAI Codex credential and state files on a victim host.

Read carefully, this shows two things: AI tooling running in the operators' own environment, and collection intent against victims' AI-tool files. It does not connect an AI-generated instruction or agent action to a specific exploitation step in the hospital or manufacturer records.

Other scripts request changes to a Codex-named sandbox service and terminate WSL processes; their presence does not establish successful changes or an AI-product vulnerability. The ownership and origin of the copied authentication material remain unresolved, so we do not characterize it as a verified theft of a usable AI credential from an external victim. What the files do support is that AI-tool credential and state files are being swept up alongside the usual browser and DPAPI loot.

### Authentication stores and further experiments

C also contains a privacyIDEA copy (18 token records, 16 owners, 172 token-info records, 3,200 audit records), a cookie store, and archives of vault, DPAPI, and registry material, plus a Jenkins remoting agent and SQL-extraction experiments. These are retained sensitive artifacts and source-level capability.

We did not decrypt OTP secrets, use credentials, or establish external-victim ownership. Guest-agent file-pull helpers read content through a local VM's QEMU guest agent, but their counters can double-count partial saves, so a callback or saved filename requires independent length and hash validation before it is treated as a complete acquisition. Pulling back from the files, the platform record ties these hosts to a wider set of infrastructure.

## From the directories to a Mythic C2 host

Hunt.io lists [45.83.180\[.\]113](https://portal.hunt.io/ip/45.83.180.113) within AS62005, BlueVPS. Its profile shows open-directory warnings dated 6 October, 25 October, and 5 November 2026. Those dates guide the archived service records; warning counts and map locations do not establish who operated the server.

The second host, [74.63.203\[.\]115](https://portal.hunt.io/ip/74.63.203.115), is listed within AS46475, Limestone Networks, with an open-directory warning dated 4 November, and historical HTTP records show directory listings on port 18111 on 4 and 6 November. This confirms the exposure without joining its VM and application artifacts to the other host.

### From recovered configuration to a Mythic-labelled service

The next pivot came from source rather than a shared hosting provider. A hosts-mapping generator explicitly maps lababalbaba.com to [45.83.182\[.\]68](https://portal.hunt.io/ip/45.83.182.68), and the Linux payload's decoded configuration names the same domain. That gave a specific destination to investigate.

Searching its HTTP observations on port 7443 exposed a page titled Mythic:

```huntsql
SELECT ip, port, timestamp, html.head.title, http.headers.server
FROM http
WHERE ip = '45.83.182.68'
  AND port = 7443
  AND timestamp > '2025-11-03'
LIMIT 20
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT+ip%2C+port%2C+timestamp%2C+html.head.title%2C+http.headers.server%0AFROM+http%0AWHERE+ip+%3D+%2745.83.182.68%27%0A++AND+port+%3D+7443%0A++AND+timestamp+%3E+%272025-11-03%27%0ALIMIT+20&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
Output example:

Figure 23:
[Historical HTTP results](https://portal.hunt.io/sql?sql=SELECT%0A++ip%2C%0A++port%2C%0A++timestamp%2C%0A++html.head.title%2C%0A++http.headers.server%0AFROM%0A++http%0AWHERE%0A++ip+%3D+%2745.83.182.68%27%0A++AND+port+%3D+7443%0A++AND+timestamp+%3E+%272025-11-03%27%0ALIMIT%0A++20&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)showing a Mythic page title on 45.83.182.68:7443. The capture shows several Mythic observations, including 27 October 2026. Other rows show an HTTP 400 title indicating a plain HTTP request reached an HTTPS service. The screenshot corroborates the retained title; it does not show an authenticated Mythic session.

The [Pivot view](https://portal.hunt.io/ip/45.83.182.68/pivots) exposes the certificate SHA-256 and subject (lababalbaba.com). The exact hash is a more precise pivot than the title or subject name.

[JARM](https://hunt.io/glossary/jarm-fingerprinting)and

[JA4X fingerprints](https://hunt.io/glossary/ja4-fingerprinting). The broader fingerprints were not used to assign additional hosts to this activity.

A [HuntSQL](https://hunt.io/features/hunt-sql) query for that exact certificate hash returns every observation of it:

```huntsql
SELECT ip, port, certificate_hash, timestamp
FROM certificates
WHERE certificate_hash =
  '1ba2ec04908a4c4696f2f740f04588708c0c3afc7efbebc0aa69f39b78fc535b'
  AND timestamp > '2025-11-03'
LIMIT 100
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT+ip%2C+port%2C+certificate_hash%2C+timestamp%0AFROM+certificates%0AWHERE+certificate_hash+%3D%0A++%271ba2ec04908a4c4696f2f740f04588708c0c3afc7efbebc0aa69f39b78fc535b%27%0A++AND+timestamp+%3E+%272025-11-03%27%0ALIMIT+100&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
Output example:

Figure 25: Matching certificate observations on ports 443 and 7443. The exact-hash search returned 23 observations, all on the configured IP, across ports 443 and 7443. That supports certificate reuse between those services and adds no further host in the returned inventory.
### A second domain association

Hunt.io's [Domains view for 45.83.182\[.\]68](https://portal.hunt.io/ip/45.83.182.68/domain) shows sb-it-support.com and its mail and www subdomains. These are platform-listed associations, not proof of common ownership on their own.

A separate retained observation makes the lead more specific: on 8 November, port 8089 served a page titled User Portal with a certificate for sb-it-support.com. The exact-certificate search returned two observations on that IP only. Historical DNS and tenancy evidence are still needed before assigning the domain to the same operator.

### Additional staging and delivery services

Returning to [45.83.180\[.\]113, the retained port-8899](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:8899) response exposed another directory on 5 November. Its links included wsvc\_beacon.exe, wsvc\_prod.exe, gh0st\_push.py, and prod-miniupdate-v9.zip and prod-miniupdate-v10.zip, with version-directory entries retained through 10 November.

The host's port-8080 response contained a document-sharing pretext and a browser-mediated WordPress plugin-installation attempt referencing /athena.zip on the same server. These are acquisition leads; the filenames do not establish the files' behavior, and their contents were not retrieved during this hunt.

Figure 27: Archived executable, script and log filenames in the additional directory. The archived inventory sets the next collection step: compare the versioned archives, examine the transfer or deployment logs, and obtain executable hashes before assigning a payload family. The badges shown are platform annotations and do not replace analysis of the bytes.
To see how long that lure page stayed live, we pulled its history on port 8080.

```huntsql
SELECT
  ip,
  port,
  timestamp,
  html.head.title,
  html.body.hash.sha256
FROM
  http_history
WHERE
  ip = '45.83.180.113'
  AND port = 8080
  AND html.head.title = 'Secure Document — Action Required'
  AND timestamp >= '2026-10-21'
  AND timestamp < '2026-11-03'
ORDER BY
  timestamp ASC
LIMIT
  500
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT%0A++ip%2C%0A++port%2C%0A++timestamp%2C%0A++html.head.title%2C%0A++html.body.hash.sha256%0AFROM%0A++http_history%0AWHERE%0A++ip+%3D+%2745.83.180.113%27%0A++AND+port+%3D+8080%0A++AND+html.head.title+%3D+%27Secure+Document+%E2%80%94+Action+Required%27%0A++AND+timestamp+%3E%3D+%272026-10-21%27%0A++AND+timestamp+%3C+%272026-11-03%27%0AORDER+BY%0A++timestamp+ASC%0ALIMIT%0A++500&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
Output example:

Figure 28: Repeated observations of the document-themed page on port 8080. The capture shows the title Secure Document, Action Required on the original host's port 8080 at several dates from 21 October through 2 November. It supports repeated observations of the title, without showing that every response body was byte-identical.
Pivoting on the login page’s etag shows where else the same page appeared, including port 7443.

```huntsql
SELECT ip, port, timestamp, http.headers.etag, http.redirected.url
SELECT ip, port, timestamp, http.headers.etag, http.redirected.url
FROM http
WHERE http.headers.etag = '"6abf81c9-249"'
 AND http.redirected.url LIKE '%/new/login'
 AND timestamp > '2025-11-03'
LIMIT 100
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT+ip%2C+port%2C+timestamp%2C+http.headers.etag%2C+http.redirected.url%0ASELECT+ip%2C+port%2C+timestamp%2C+http.headers.etag%2C+http.redirected.url%0AFROM+http%0AWHERE+http.headers.etag+%3D+%27%226abf81c9-249%22%27%0A+AND+http.redirected.url+LIKE+%27%25%2Fnew%2Flogin%27%0A+AND+timestamp+%3E+%272025-11-03%27%0ALIMIT+100&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
Output example:

Figure 29: HTTP search rows showing the configured host on port 7443. The capture shows several rows for the host on port 7443. Together, source configuration, the certificate, page title, and HTTP metadata strengthen the service association. They do not establish a successful implant callback.
Taken together, the hosts and certificates map one operation. Who runs it is a separate question, and a more cautious one.

## Attribution: Chinese-speaking operators, a Russian toolkit

We are not tying this to a named group, and nothing here points to a state sponsor: this section is an assessment drawn from indicators in the files, not a validated attribution.

The independent technical validation of this corpus deliberately did not assign a nationality or location, and that caution is right. The indicators are present and point one way: a financially motivated, Chinese-speaking crew operating in the UTC+7 band, using a toolkit that is not its own.

Across the three collections, the operators' own scripts carry Chinese comments and Chinese resource names far more than Russian. The Russian sits inside the shared toolkit, the exploit and password-cracking utilities.

The hands-on work, the recon, the RDP-resilience checks, and the log triage are written and commented in Chinese. The simplest read is a Chinese-speaking crew running an exploit and C2 kit whose source was written by a Russian speaker, bought or borrowed rather than built. A host-health script on the third node sets its timezone to UTC+7 and buckets activity into Thailand and Vietnam office hours.

The core business reads as gambling and spam, with enterprise intrusion layered on top as opportunistic expansion: a betting-platform admin database, link-farm keywords, crypto-wallet scanners, and romanized-Chinese management panels. One caution worth keeping: language and timezone in code tell you who wrote and ran the code, not a nationality or a flag.

We read this as a Chinese-speaking, Southeast Asia-based cybercrime operation running a Russian-authored toolkit. For defenders, the practical question is less who they are than how to catch them.

## Detection and response

- Inventory and lock down the remote-access edge: Citrix NetScaler, FortiGate SSL VPN, Exchange and OWA, VPN portals, and SSO. Patch the CVEs listed below and get management interfaces off the internet.
- Treat credential-stuffing on VPN and Citrix gateways as expected. Enforce MFA, alert on NetScaler 4009 bursts and spray patterns, and watch for reuse of breach-compilation pairs.
- Audit cloud storage: rotate and scope Azure SAS tokens tightly, alert on long-lived tokens and bulk blob enumeration, and review container access policies.
- Watch for NTLM relay and coercion activity (PetitPotam, Responder, mitm6). Enforce SMB signing and LDAP channel binding.
- Review Java application servers for unexpected JDBC providers. A service-provider descriptor naming a com.microsoft.sqlserver.jdbc.TlsChannelFix class, or a sqljdbc42 JAR that does not match a known vendor build, is worth pulling and inspecting.
- Hunt for a created local admin account named svc\_audit, for the launcher's temporary-EXE pattern under the Windows temp directory, and for outbound connections to the callback domain and Mythic host below. Treat the Net Monitor for Employees Professional agent port as context, not a standalone indicator.
- Block and alert on the network indicators below, after confirming current ownership.

The mapping below places these behaviors against MITRE ATT&CK.

## MITRE ATT&CK mapping

This is a conservative subset tied to the reviewed artifacts: technique presence does not establish success; code capability is distinguished from observed outcome.

| Tactic | Technique | ID | Evidence and state | 
|---|---|---|---|
| Reconnaissance | Active Scanning: Vulnerability Scanning | T1595.002 | Mass scan hit-lists, php2shell and actuator sweeps (capability) | 
| Reconnaissance | Gather Victim Identity Info: Credentials | T1589.001 | Firm credential pairs from a breach-compilation service | 
| Resource Development | Acquire Infrastructure: VPS | T1583.003 | BlueVPS and Limestone staging hosts | 
| Resource Development | Develop Capabilities: Malware | T1587.001 | TlsChannelFix JDBC provider; Apollo-derived and Poseidon-derived payloads | 
| Initial Access | Exploit Public-Facing Application | T1190 | Citrix, FreePBX, php2shell, Exchange (CVE-2026-62911), FortiOS (CVE-2026-22153), TightVNC (CVE-2024-42049) and LFI exploit/probe logic (capability) | 
| Execution | Command and Scripting Interpreter: Windows Command Shell | T1059.003 | Java beacon command execution path (code capability) | 
| Execution | Command and Scripting Interpreter: PowerShell | T1059.001 | Recon and console-command content (capability / saved artifact) | 
| Persistence | Create Account: Local Account | T1136.001 | svc\_audit account-creation command, console-reported zero exit | 
| Credential Access | OS Credential Dumping: NTDS | T1003.003 | IFM creation output; separate large Kerberos-key export | 
| Credential Access | Credentials from Password Stores | T1555 | Browser stores and exports; AI-tool credential files indexed on victim hosts | 
| Credential Access | Brute Force: Password Cracking | T1110.002 | ntcand.py candidate generation against MFLLC hashes | 
| Credential Access | Adversary-in-the-Middle: SMB/LDAP relay | T1557.001 | Responder, krbrelayx, mitm6, ntlmrelayx (capability) | 
| Credential Access | Brute Force: Credential Stuffing | T1110.004 | Simpson Thacher NetScaler VPN stuffing (all failed) | 
| Discovery | Remote System Discovery | T1018 | Computer-object discovery in recon script | 
| Collection | Data from Cloud Storage | T1530 | vslist.py listing the MFLLC Azure container with a live SAS token | 
| Collection | Data from Network Shared Drive | T1039 | AD database and hives staged from an internal share | 
| Command and Control | Application Layer Protocol: Web Protocols | T1071.001 | Java HTTPS beacon and HTTP transfer path (code capability) | 
| Command and Control | Remote Access Software | T1219 | Net Monitor for Employees Professional clients, with command evidence | 
| Command and Control | Protocol Tunneling / Proxy | T1572 / T1090 | Chisel; authenticated SOCKS relays; Mythic SOCKS | 
| Exfiltration | Exfiltration Over C2 Channel | T1041 | Recon-file chunked transfer logic; full delivery not confirmed | 

The concrete indicators behind those techniques follow.

## Indicators of compromise

| Artifact | Bytes | SHA-256 | Interpretation | 
|---|---|---|---|
| gkbd-cache.bin | 7,716,744 | c1d26614cb1469e0651435a8e6301f6e38d4fa0add4fea138fe708e6669a2c33 | Linux ELF, Poseidon Go module and HTTP config; no execution verified | 
| dbmaint.fix | 2,109,952 | 5ec1fe899277b0f489fcc20783abb3385e7f15b23bcaf44832ad57379ee13371 | XOR-obfuscated payload; decoded bytes match the next row | 
| q4final.exe | 2,109,952 | 36c89cddd8e9edb4f7f2a88e86d828a33428247a75e55e4c2252f06a033e44ca | Apollo-derived; decoded from dbmaint.fix; not executed in this review | 
| sqljdbc42beacon.jar | 9,664 | e1d539437644e653a5b2dbf43bd1be03505b5997979c1f7229724e4ea9236228 | Java artifact with the malicious TlsChannelFix provider | 
| sqljdbc42v8.jar | 5,944 | 41f34eed79c86341006666612500ae60e95da761ee04332d3601e3a181083cdf | Java artifact, same provider identity; assess behavior per variant | 
| nmep\_cmd3.py | 3,213 | d4effaf9967404eaf833bdc97a9e2575fc91c686e2f048fd9c7fd07153709232 | Custom Net Monitor client; source hash as an artifact identifier | 

### Network artifacts and scope

| Indicator | Type | Context | Action | 
|---|---|---|---|
| 45.83.180\[.\]113 | IPv4 | Operator host A/B (BlueVPS, AS62005); open dirs :8000, :19001, :8899, :8080; beacon :8443 | Block after confirming current ownership | 
| 91.236.230\[.\]9 | IPv4 | Operator-named second VPS ("vps2, heavy tasks") in README-RULES.txt | Investigate | 
| 74.63.203\[.\]115 | IPv4 | Operator host C (Limestone, AS46475); open dir :18111 | Investigate; relationship to A/B unresolved | 
| 45.83.182\[.\]68 | IPv4 | Mythic-labelled service :7443; cert subject lababalbaba.com | Historical C2 hunt; confirm ownership before action | 
| lababalbaba\[.\]com | Domain | Poseidon callback and hosts-file mapping to 45.83.182\[.\]68 | Historical host-configuration and DNS hunt | 
| sb-it-support\[.\]com | Domain | Associated with 45.83.182\[.\]68; User Portal page on :8089 | Investigate; tenancy not confirmed | 
| 101.99.92\[.\]128 | IPv4 | Authenticated SOCKS relay (B client config); :35045 | Historical relay hunt | 
| 194.213.18\[.\]54 | IPv4 | Proxy configuration in A; :16252 | Historical relay hunt | 
| TCP/7002 | Port | Mythic SOCKS listener named in the rules file | Hunt | 
| TCP/56777 | Port | Operator SSH | Hunt | 

### Certificates and keys

| Indicator | Type | Context | 
|---|---|---|
| 1ba2ec04908a4c4696f2f740f04588708c0c3afc7efbebc0aa69f39b78fc535b | TLS cert SHA-256 | lababalbaba.com, observed on 45.83.182\[.\]68 ports 443 and 7443 | 
| 9b325e75e840b7c6d7505f57ec527d680b786cc948fa0eff3850412706f4db89 | TLS cert SHA-256 | sb-it-support.com, User Portal on :8089 | 

CVEs present in the recovered files, with the tooling that references each:

| CVE | Target / product | Referencing tooling or note | 
|---|---|---|
| CVE-2019-19781 | Citrix NetScaler | Citrix exploit scripts (incl. stb\_19781.sh) | 
| CVE-2025-5777 | Citrix NetScaler (CitrixBleed 2) | Citrix NetScaler tooling | 
| CVE-2025-57819 | FreePBX | FreePBX exploit logic | 
| CVE-2026-109618 | php2shell (PHP RCE) | php2shell scanner output vs external hosts | 
| CVE-2026-109619 | php2shell (PHP RCE) | php2shell scanner output vs external hosts | 
| CVE-2026-62911 | Microsoft Exchange, MRSProxy pre-auth RCE | cve62911\_poc.py | 
| CVE-2024-42049 | TightVNC | tvnc\_ctrl.py | 
| CVE-2026-87902 | LFI driver | lfi.py | 
| CVE-2026-22153 | FortiOS, LDAP auth bypass | fg\_ldapbypass.sh | 
| CVE-2021-42278 | Active Directory (sAMAccountName / noPac) | AD relay and Kerberos kit | 
| CVE-2021-36942 | PetitPotam (AD coercion) | AD relay and Kerberos kit | 
| CVE-2017-8563 | Active Directory / LDAP relay | AD relay and Kerberos kit | 
| CVE-2020-1472 | Zerologon (Netlogon) | AD relay and Kerberos kit | 

The separate fg.sh is a FortiGate credential login check. CVE-2025-6543, CVE-2023-27997 and CVE-2021-1675 were in an earlier draft but do not appear in the recovered files and were removed.

Scope note: these are historical observations from the recovered material, not claims that the addresses are currently malicious. Victim domains, internal addresses, third-party downloaders, the commercial monitoring vendor's services, and unverified panel domains are excluded from the block set.

TCP 4495 alone is not an indicator, and a normal AI-application path is not evidence of compromise. The table below places every organization in the corpus on one scale, from confirmed access to reconnaissance.

## Victim and target summary by evidence strength

We put every organization from the report into one picture, ranked by how strong the evidence is. The top tier is confirmed: data or access already in the operators' hands. Everything below it is weaker, active attempts, harvested credential lists, and targets that show up only in a scan. Keeping those apart is the difference between reporting a breach and reporting a target.

The graphic is the fast read, the table below gives the basis for each placement, the exact files, logs, or captures behind it, so every tier can be checked against the source rather than taken on trust.

| Organization | Region | Status | Basis | 
|---|---|---|---|
| Large US hospital system | US | Data and credentials in operator hands; recorded VPN session | 8,460-address directory, 3,570-record auth dump, phpinfo capture, separate hospital VPN log; acquisition and validity not established | 
| US manufacturer (internal identity held) BRAC University | US | Cloud storage listed with live token; hashes attacked | Azure container enumerated via live SAS token; own QuickBooks file and domain in the listing; NTLM candidates generated | 
| Bangladeshi university | Bangladesh | Breached | Large Kerberos-key export (35,601 records); hands-on PtH and DPAPI collection | 
| Swiss tax office (domain TABT) | Switzerland | Domain DB and hives staged | IFM creation and copy to staging; NTLM relay; printer and share loot | 
| Pediatric / academic-medical set (\~54 institutions) | US and intl | Harvested | 153-record credential list reused from a third-party breach compilation | 
| Simpson Thacher & Bartlett | US | Attacked, no success | Credential-stuffing, Citrix CVE-2019-19781, SQLi, SMTP relay test, service probing; all captured results failed | 
| \~563 US law firms (60+ named AmLaw) | US | Targeted | VPN, Citrix, client-portal edges enumerated | 
| US federal agencies: HRSA (incl NPDB, 340B), SBA, NEA, NSF, NCUA | US | Targeted | Probed in recon sweep; mostly 403, some live portals | 
| US enterprises: Hertz, Plaid, Oportun; UNC School of Government | US | Targeted | Live edges catalogued; credential-check script | 
| Children's-hospital REDCap servers | US | Targeted | Active hunting list | 
| University medical/health subdomains | US | Targeted | Actuator endpoints probed; status 200/403 mix, no disclosure established | 

## Conclusion

One set of exposed directories gave up a US hospital system's credential and web-tier material and a recorded gateway session, a US manufacturer's cloud object listing taken with a live token, a full enterprise-intrusion kit, a malicious JDBC-to-Apollo execution chain and a Poseidon implant, and a target project that runs from hundreds of law firms into federal agencies. The strongest findings connect inspected mechanisms with retained artifacts; the files support several operational workflows without proving one continuous intrusion across every environment.

The records do not establish AI-led exploitation or a planned sequence of future victims. The US healthcare and manufacturer impact needs disclosure now. The law-firm and agency work is still at the edge, which is exactly the VPN, Citrix, and portal surface defenders can watch.

[Find more Apollo, Poseidon, and Mythic infrastructure like thisThis crew chained a malicious JDBC driver into an Apollo payload, ran a Poseidon implant on Linux, and kept a Mythic C2 one certificate hash away. See how Hunt.io pivots across hosts, certs, and callback domains to catch the next build before it hits a blocklist.Book a Free Demo Now](https://hunt.io/get-started)

Related Posts

Related Posts

Related Posts

©2026 Hunt Intelligence, Inc.

©2026 Hunt Intelligence, Inc.

©2025 Hunt Intelligence, Inc.
