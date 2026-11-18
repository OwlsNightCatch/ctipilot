---
title: N-able Disables Cloud Services Following Disclosure of "Able2Shell" Exploit Chains | Huntress
author: Lindsey O'Donnell-Welch; Susannah Matt; Sharon Martin
url: https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains
hostname: huntress.com
description: "UPDATE: N-able took N-central offline after 33 critical flaws were disclosed, including chains enabling remote code execution and privilege escalation."
sitename: Huntress
date: "2026-11-09"
fingerprint: bc32c093f906f68f
---
### **UPDATE: 11/17 @ 8:30 AM ET**

N-able has now published CVSS 4.0 scores and official descriptions for all 17 CVEs fixed in N-central 2026.4 Hotfix 3 (build 2026.4.1.39). Three are rated critical severity, eight high severity, and six medium severity. All scores were assigned by N-able as the CVE Numbering Authority. NVD has not yet published its own scoring.

Public proof-of-concept code for all 17 CVEs was released on the evening of November 16, shortly after the hotfix. Any unpatched server should be treated as exposed.

Critical:

- CVE-2026-129272 (9.3): A predictable appliance passcode lets a remote, unauthenticated attacker who knows or guesses an appliance ID impersonate that Agent or Probe. This is the impersonation issue behind N-able's instruction to upgrade every Agent and Probe.
- CVE-2026-129280 (9.3): Multiple ServerUI SOAP operations don't check the caller's session, permissions, or customer scope. In some cases without logging in, an attacker can read device and patch data, test user passwords, send messages to managed agents, and change settings belonging to other customers on the same server.
- CVE-2026-129286 (9.2): Path traversal in software update metadata leads to code execution as the N-central service account.

High:

- CVE-2026-129274 (8.7): Unauthenticated forged results for any customer's remote execution tasks
- CVE-2026-129282 (8.7): Test email argument injection with no permission check or CSRF protection
- CVE-2026-129273 (8.6): Audit Export syslog injection leading to root command execution (requires product administrator)
- CVE-2026-129271 (8.5): Patch Management Engine local privilege escalation, fixed in Patch Management Component 2.14.4.5829
- CVE-2026-129281 (8.5): View-only users can set execution configuration that the Windows agent acts on
- CVE-2026-129287 (8.3): XXE in the software repository parser
- CVE-2026-129275 (8.2): Unauthenticated download of any customer's Automation Manager policies, including embedded scripts and parameter values
- CVE-2026-129283 (7.1): XXE in custom service import

Medium:

- CVE-2026-129276, CVE-2026-129277 (6.9): Unauthenticated asset data overwrite, and reading or cancelling pending maintenance actions
- CVE-2026-129278 (6.9): Unauthenticated tampering with Take Control session records and audit log entries
- CVE-2026-129279 (6.9): Account email enumeration via password reset
- CVE-2026-129284, CVE-2026-129285 (5.3): SSRF in Report Manager and Data Export settings, and forged XMPP action responses (requires another appliance's credentials)

Beyond patching, we recommend:

- Confirm the full stack is updated: the server to 2026.4.1.39, every Agent and Probe to 2026.4.1 HF3, and the Patch Management Engine to 2.14.4.5829 or later. A patched server alone does not close the impersonation issues.
- Rotate secrets in Automation Manager policies. Any credentials or API keys embedded in policies on a server that was exposed before patching should be treated as potentially disclosed (CVE-2026-129275).
- Don't rely on Take Control audit records from an unpatched server during an investigation. They could have been altered (CVE-2026-129278).
- Expect targeted password attacks. Valid account emails may have been enumerated (CVE-2026-129279), so make sure MFA is enforced on all N-central accounts.

As of this writing, Huntress has not observed exploitation of these issues in our partners' environments.

### **UPDATE: 11/16 @ 7 PM ET**

N-able has released [<u>N-central 2026.4 Hotfix 3</u>](https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/?shem=aimgspe), a critical security update that supersedes the earlier hotfix released on November 10. According to their release notes, the update implements server and user account hardening measures, improves Agents and Probes communications, and adds additional validation to file publishing, file path, and XML import handling.

The hotfix also removes the configuration option for legacy APIs, a feature that was leveraged in several of the proofs of concept (POCs) that emerged for the recent CVEs. N-able states that legacy APIs are now permanently blocked.

N-able began applying the hotfix to hosted N-central environments in a phased rollout on the morning of November 16 before releasing to the general public in the evening. **All customers running on-premise N-central deployments are urged to upgrade their servers as soon as possible.** 

**Both hosted and on-premise customers** must upgrade all of their Agents and Probes to the latest version to be fully protected, as N-able states that "agents and probes that are not upgraded are subject to impersonation."

Here's a quick breakdown of the 17 CVEs this hotfix includes.

Several appear to require no login:

- **CVE-2026-129272:** Predictable MMS3 appliance passcode
- **CVE-2026-129274, CVE-2026-129276, CVE-2026-129277:** Missing authentication on ServerMMS2 calls
- **CVE-2026-129278:** Take Control audit log tampering
- **CVE-2026-129279:** User enumeration via password reset
- **CVE-2026-129280:** Missing authorization on ServerUI SOAP calls

Several appear to lead to `root` or `nable` user code execution:

- **CVE-2026-129271:** Patch-package local privilege escalation
- **CVE-2026-129273:** Audit Export syslog injection
- **CVE-2026-129286:** SIS GenericFiles path traversal

The rest appear to be XXE, SSRF, and permission gaps:

- CVE-2026-129275
- CVE-2026-129281
- CVE-2026-129282
- CVE-2026-129283
- CVE-2026-129284
- CVE-2026-129285
- CVE-2026-129287

While these vulnerabilities have yet to be assigned CVSS scores, Huntress recommends patching both on-prem servers, Agents, and Probes as soon as possible. We have not seen evidence of exploitation in the wild.

### **UPDATE: 11/13 @ 10:25 AM ET**

In an [<u>update to its security advisory</u>](https://uptime.n-able.com/) on November 13 at 13:40:25 UTC, N-able said that it has identified Indicators of Compromise (IoCs) for customers that haven't disabled the Legacy API. Here are the IoCs they have released:

**URLs**

`hxxp://157.20.241[.]16:8080/jup.sh`

`hxxp://157.20.241[.]16:8080/xvgz`

`hxxp://157.20.241[.]16:8080/xmrig.tgz`

`hxxp://157.20.241[.]16:8080/ob/cronhit?h=jup_start_<rig>&persist=<method>`

`hxxp://157.20.241[.]16:8080/ob/fcheck`

**Outbound Traffic**

`157.20.241[.]16` (ports `8080, 19202` to `19418`**)**

`139.99.69[.]109:10128`

`79.76.51[.]56:39100` 

Additionally, N-able confirmed that Agent2Shell exploitation (like 4EverAble2Shell) requires the non-default Legacy API to be enabled.

As of this writing, Huntress has not observed exploitation of these issues in our partners' environments. We are continuing to track this incident and will continue updating this blog as new information emerges.

### **UPDATE: 11/12 @ 6:30 AM ET**

New information from N-able changes our guidance from earlier this morning.

N-able has released an [<u>active advisory</u>](https://uptime.n-able.com/event/202609/) addressing this latest set of exploits. In its advisory, N-able said that the N-central server issue described depends on a non-default configuration, where the Legacy API is turned on and exposed to the public internet.

N-able released a knowledge base article on how to disable Legacy API settings [<u>on on-premises N-central servers</u>](https://me.n-able.com/s/article/How-to-Disable-Legacy-API-settings-on-On-premise-N-central-servers). N-able is not advising customers to take N-central offline.

The author of the exploit code has since updated their repository to confirm the exploit only works with Legacy API turned on. Servers running 2026.4 HF2 with Legacy API disabled are not exposed to this exploit chain.

### What should you do right now?

- **On-premises N-central: confirm that Legacy API is disabled.** If it is enabled, follow N-able's article to disable it.
- If **you need Legacy API enabled, do not expose it to the internet**. Restrict access to the server until N-able provides a fix.
- **If you took your server offline based on our earlier update,** confirm Legacy API is disabled before bringing it back online.
- **Hosted N-central:** N-able states that hosted environments are not vulnerable to this issue.
- **If Legacy API was enabled and reachable from the internet,** review server and endpoint activity from November 11 onward using the indicators in our earlier update below.

We have not yet confirmed whether the Agent2Shell chains affecting Windows Agents and Probes also depend on Legacy API. We are working with N-able to clarify this and will update this post when we know more.

As of this writing, Huntress has not observed exploitation of these issues in our partners' environments. Huntress is continuing to track this incident and will continue updating this blog as new information emerges.

### UPDATE: 11/12 @ 1:10 AM ET

Late on November 11, the researcher behind Able2Shell published two more sets of exploit code for N-able N-central, named “4EverAble2Shell” and “Agent2Shell”. Both are stated to work against N-central 2026.4 HF2 (build 2026.4.1.26), the version N-able released on November 10 to address the original disclosure. A fully patched N-central server should be treated as vulnerable. There is no fix available at the time of writing.

Based on our initial review of the published code:

- 4EverAble2Shell is an unauthenticated remote code execution chain that results in root access on the N-central server. It requires no credentials.
- Agent2Shell is a set of more than ten issues in how the N-central server communicates with Windows Agents and Probes. Two of the chains allow an unauthenticated attacker who can reach the server to run commands on managed Windows endpoints, including as SYSTEM.

Used together, these could let an attacker move from an internet-facing N-central server to the endpoints it manages. Huntress is actively investigating, and we will update this post as our analysis continues.

If the POC code is used in an unmodified fashion, the following indicators may appear. Please note that all of these potential indicators were extracted from a static code analysis and none have been observed in the wild:

- **In logs to the N-Central Server:**
  - POSTs to `/dms/services/ServerUI` containing `jline.internal`.TerminalLineSettings (the PoC gets an HTTP 500 back).
  - POSTs to `/dms/services/ServerUI` containing `GenericAgentXMPPMessageExchange` with SessionID of -1.
  - POSTs to `/dms2/services2/ServerMMS2` containing `RemoteExecutionTaskSubmit` with sessionID of -1.
- **Files on system on the N-Central Server**
  - `/var/opt/n-central/flag/flag_default.json` existing as a symlink to `/opt/nable/var/ncsai/scripts/ServerChild.sh`.
  - `/var/opt/n-central/tmp/serverchild-<12 hex>.bak`, `.sh` or `.out`.
  - ZIPs under `/download/scheduled_tasks/output_files/` containing `CodeDropMeta.xml`.
- **On Windows Endpoints:**
  - `powershell.exe -NoProfile -NonInteractive -EncodedCommand` as SYSTEM, spawned from the N-able Agent.
    - Note: PowerShell is very commonly seen as a child process of N-able, it's the command that is running that is of interest in this case.
  - `wsp.exe` or `service.cfg` written to `Windows Software Probe\bin`, with a backup at `CodeDrop\ServiceBackup\wsp.exe` and files in `Temp\CodeDropTmp`.
    - Note: The Windows Software Probe is very commonly seen as a child process of N-able, so that process tree alone is expected, and not a sole indicator of compromise.
  - `taskkill /f /im wsp.exe` and a stop/start of "Windows Software Probe Service" run from a .cmd in `%TEMP%`.

### **What should you do right now?**

- **On-premises N-central:** Take the server offline again, or remove all internet access to it, even if you have applied 2026.4 HF2. Keep it offline until N-able issues guidance for these new issues.
- **Do not rely on IP allowlisting alone:** The affected endpoints are the same ones Agents and Probes use to check in, so any device on an allowed network can still reach them.
- **Hosted N-central:** Monitor [<u>N-able's status page</u>](https://uptime.n-able.com/event/202561/) for guidance. Hosted servers run the same build.
- **Review activity from November 11 onward:** On the server, look for unexpected administrator accounts, scripts, scheduled tasks, and remote sessions. On Windows endpoints, look for unexpected PowerShell or cmd.exe activity launched by the N-able Agent or Probe, and unexpected restarts of the Windows Software Probe service.
- **If you find suspicious activity:** Treat it as a potential compromise of your managed environments and engage your incident response team.

### UPDATE: 11/10 @ 5:30 PM ET

On November 10, N-able released [**<u>N-central 2026.4 HF2</u>**](https://status.n-able.com/2026/11/10/n-central-2026-4-hf2-release-notes/), (build 2026.4.1.26) to address the Able2Shell vulnerabilities disclosed the day before. According to their release, the critical security update strengthens authentication and permission checks on the server, removes legacy mobile device management (MDM), adds additional validation to file and log handling, and hardens server components and web and sign-in protections.

The hotfix addresses the following vulnerabilities, which now have designated CVEs:

- [<u>CVE-2026-125883</u>](https://www.cve.org/CVERecord?id=CVE-2026-125883): Multiple XXE vulnerabilities
- [<u>CVE-2026-125878</u>](https://www.cve.org/CVERecord?id=CVE-2026-125878): Multiple OGNL injection vulnerabilities
- [<u>CVE-2026-125879</u>](https://www.cve.org/CVERecord?id=CVE-2026-125879): Local privilege escalation to root via `nable-writable syslog-ng config`
- [<u>CVE-2026-125880</u>](https://www.cve.org/CVERecord?id=CVE-2026-125880): Stored XSS via MMS3 patch metadata (admin context)
- [<u>CVE-2026-125881</u>](https://www.cve.org/CVERecord?id=CVE-2026-125881): Schema-hint SSRF via service import schema validation
- [<u>CVE-2026-125882</u>](https://www.cve.org/CVERecord?id=CVE-2026-125882): RCE via file repository upload path traversal (credit to Nate Fair from Sprocket Security)
- [<u>CVE-2026-91000</u>](https://www.cve.org/CVERecord?id=CVE-2026-91000): Insecure IPC Channels lead to local privilege escalation

N-able has updated all hosted N-central servers, and all customers running on-premises N-central deployments are advised to upgrade their servers as soon as possible, keeping them offline until the upgrade is complete. Note that all customers, both hosted and on-premises, must also upgrade their Agents and Probes, as the hotfix updates legacy components of the Agent and Probe to change how the two communicate.

N-able shared on their [<u>status page</u>](https://uptime.n-able.com/) that they had observed "scanning activity associated with the published proof-of-concept code" but no evidence that any customer environment had been successfully exploited.

As of this writing, Huntress has not observed evidence of Able2Shell exploitation in our partners' environments.

### Original post

*Acknowledgments: Special thanks to John Hammond, Ben Bernstein, and Andrew Brandt for their contributions to this investigation and writeup.*

Huntress is tracking N-able's response to the public disclosure of critical vulnerabilities in its N-central platform, a remote monitoring and management (RMM) platform built for managed service providers and IT teams. On November 9, N-able [<u>took its hosted N-central environment</u>](https://uptime.n-able.com/) offline while it worked to secure the environment and apply remediation.

That move came after an independent researcher published the details of 33 critical vulnerabilities to GitHub that can be chained to lead to four different exploits (dubbed "Able2Shell"). Three of those chained exploits lead to remote code execution and one leads to privilege escalation to root. The vulnerabilities impact servers running N-central Appliance 2026.4.0.31 (and likely earlier versions as well).

N-able said it has not seen active exploitation of the vulnerabilities as of November 9 at 15:15:00 UTC. The company is working on a hotfix that it said will be available soon; customers should keep their N-central servers offline until N-able confirms they can be brought back online safely.

Huntress has tracked and responded to other, separate flaws in N-able's N-central this year, including [<u>five critical CVEs</u>](https://www.huntress.com/blog/n-able-vulnerability-exploitation):

- **August 2026:** N-able released a hotfix for [<u>CVE-2026-18556</u>](https://nvd.nist.gov/vuln/detail/cve-2026-18556), a critical vulnerability impacting all current versions of N-central across both hosted and on‑prem deployments, giving attackers unauthenticated, "god-mode" access to the RMM console. [<u>CVE-2026-18577</u>](https://nvd.nist.gov/vuln/detail/CVE-2026-18577) was disclosed soon after as an incomplete patch to the former CVE.
- **September 2026:** N-able issued a hotfix to address a third vulnerability, [<u>CVE-2026-86218</u>](https://nvd.nist.gov/vuln/detail/CVE-2026-86218), an actively exploited pre-auth RCE zero day with a 10.0 CVSS score. The next day Huntress produced a proof of concept (PoC) exploit of a separate, net new vulnerability chain ([<u>CVE-2026-86206</u>](https://nvd.nist.gov/vuln/detail/CVE-2026-86206) and [<u>CVE-2026-86207</u>](https://nvd.nist.gov/vuln/detail/CVE-2026-86207)) in N-central that allowed attackers to bypass access controls to create unauthorized administrative accounts.

## What Should Potentially Impacted Organizations Do?

Potentially impacted organizations should do the following:

- If you run N-central on premises, take the server offline now and keep it offline until N-able confirms it is safe to restore.
- If you use N-able's hosted service, expect an outage. N-able has taken its cloud infrastructure offline; follow its status page for updates.
- Review login and authentication activity from November 8 onward for unexpected or unauthorized access. If you find suspicious activity, involve your incident-response team and assess whether systems or client networks managed through N-central may also be affected. The document warns that exploitation could enable remote code execution or privilege escalation on the server.
- Carefully examine your audit logs for secondary indicators of compromise. During previous N-central vulnerability exploitations (such as the CVE-2026-86218 zero-day), threat actors were observed "spraying" downstream environments with unauthorized scripts and tools. Specifically, you should monitor for anomalous remote access sessions, new scripts being deployed, or the unauthorized creation of new administrator accounts.
- Apply N-able's hotfix and restore service only when N-able says it is safe. The document said a hotfix was in development, with no exact ETA, so check current vendor guidance rather than relying on this dated update. 
  - N-able does not always iterate version numbers when it pushes down live hotfixes that don't require a reboot, so it remains to be seen whether the patched version will be numbered 2026.4.0.31 or something different.

## Next Steps

Huntress is actively investigating this incident and we are communicating with our potentially vulnerable customers to share updates as they become available. Please check this blog for further updates as we learn more information.

You can also get further updates from N-able at: <u>https://uptime.n-able.com/event/202561/</u>

## Indicators of Compromise (IOCs)

| **Item** | **Description** | 
|---|---|
| `hxxp://157.20.241[.]16:8080/jup.sh` `hxxp://157.20.241[.]16:8080/xvgz` `hxxp://157.20.241[.]16:8080/xmrig.tgz` `hxxp://157.20.241[.]16:8080/ob/cronhit?h=jup_start_<rig>&persist=<method>` `hxxp://157.20.241[.]16:8080/ob/fcheck` | N-able recommends that customers who have not disabled the Legacy API monitor for these URLs | 
| `157.20.241[.]16` (on ports `8080, 19202` to `19418`) `139.99.69[.]109:10128` `79.76.51[.]56:39100`  | N-able recommends that customers who have not disabled the Legacy API monitor for these outbound traffic IP addresses |
