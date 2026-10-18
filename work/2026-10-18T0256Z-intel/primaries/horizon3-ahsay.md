---
title: "AhsayCBS Auth Bypass & RCE: CVE Analysis"
author: Zach Hanley
url: https://horizon3.ai/attack-research/attack-blogs/ahsaycbs-cve-2026-105133-cve-2026-105134-technical-analysis/
hostname: horizon3.ai
description: Technical analysis of CVE-2026-105133 and CVE-2026-105134 in AhsayCBS, revealing how authentication bypass and path traversal enable remote code execution.
sitename: Horizon3
date: "2026-10-14"
fingerprint: b509c8df8fa20687
---
## **Introduction**

On 8 October 2026, Huntress released a [report](https://www.huntress.com/blog/ahsaycbs-flaws-exploit) detailing the in-the-wild exploitation of [AhsayCBS](https://www.ahsay.com/), an on-premises backup server application. The report described two vulnerabilities:

1. CVE-2026-105133 – An authentication bypass in the API components
2. CVE-2026-105134 – A file write path traversal leading to remote code execution

By chaining the vulnerabilities together, attackers were observed writing webshells into the application filesystem, allowing them to execute commands as SYSTEM and root. On 12 October 2026, Ahsay released hotfixes for the [issues](https://www.ahsay.com/en/company/announcements/patch-cve-105133-105134-update).

Even though we had not heard of this specific backup solution before, given the in-the-wild exploitation reports, we dug in.

## **Unpacking the Installer**

AhsayCBS is available to install on both Linux and Windows servers. This analysis focuses on the Linux installer which is released as a tarball, cbs-nix-tar.gz. Inside the tarball, you’ll find that it’s a Java application, shipped with its own JRE, and built upon the tomcat framework.

The interesting surface lives in the web applications under `webapps/.` Alongside the main console (`cbs`) and the client-facing backup service (`obs`) sits `rps`, the Replication Receiver. Taking a look at its `struts-config.xml`, a familiar pattern emerges – a set of `.do` actions under `/rps/api/json/`, each mapped to a Java class:

**Figure 1.** API routes exposed in `webapps/rps/WEB-INF/struts-config.xml`.

Every one of these JSON actions extends a common base class, `com.ahsay.obs.api.json.JSONApi.` That base class is where authentication is supposed to happen, and it is where we first look.

## **CVE-2026-105133: The Path to Unauthenticated API Access**

The first vulnerability can be found in the `JSONApi` base class. `JSONApi.execute()` runs before any action-specific logic. Reading the source, the authentication decision comes down to three booleans:

**Figure 2.** The only credential gate in `JSONApi.execute()`

`b` is true only when the caller already holds an authenticated session. `equals2` is the `FromObc` flag, honored only for actions that opt in. And `equals` is the `FromServlet` flag, read straight out of the attacker-controlled JSON request body. `checkSysPwd()` is the one function that validates the system administrator’s username and password, and it is called only when all three booleans are false.

Which means a request that simply includes `"FromServlet":"Y"` sets `equals` to true, and the credential check is never reached. The resolved administrator object is computed a few lines later but its value is never checked, and the downstream actions never reference it.

Confirming the bypass takes two requests. Without the flag, the server demands credentials:

**Figure 3.** Demonstrating auth bypass with `FromServlet` flag

## **The Path to Admin**

With the entire API now unauthenticated, one of the most impactful actions an attacker may take is to add a new administrative user. Among the `obs` actions is `com.ahsay.obs.api.json.system.systemUser.AddSysUser`, the endpoint the console uses to create system administrators.

Reading its `doAction`, the handler pulls `LoginName`, `Password`, and `Role` out of the request, validates the role against the `Admin.Type` enum, and builds a new administrator:

**Figure 4.** `AddSysUser` creating an administrator from attacker-supplied JSON

Notably, `AddSysUser` never consults the authenticated caller. Combined with the bypass, that is all an unauthenticated attacker needs to mint themselves an administrator:

**Figure 5.** Creating a new administrator account

## **CVE-2026-105134: The Path to Code Execution**

The second vulnerability targets the Replication Receiver directly, and it is the one that lands a webshell. Replication in AhsayCBS mirrors a primary server’s data to a secondary “receiver.” The receiver is configured through `UpdateReceivers`, and it ingests replicated files through a service, `com.ahsay.ars.obs7.FileService`, exposed at `/rps/obs7/rpsfile.`

Starting from the configuration side, an auth-bypassed call to `UpdateReceivers.do` with `Id=0` creates a new V7 receiver. The attacker controls its login, its password, and its `SystemHome. SystemHome` is run through a system-folder denylist (`com.ahsay.c`) that blocks the obvious targets like `webapps`, `conf`, `tomcat`, and the rest, so we point it somewhere benign like `/opt/AhsayCBS/rpsrecv_x` and move on.

The write happens later, when we feed the receiver a file. `FileService` authenticates the upload by matching the receiver’s login and password – both of which we just set – carried in a set of base64-encoded `X-RSW-Request-*` headers. It then builds the destination directory from two more attacker-controlled headers, `UserHome` and `TopDir:`

**Figure 6.** `getReplicatedPath` concatenating an attacker string onto the write root

`FileList.a()` escapes exactly two characters, `%` and `:`. It leaves `../` untouched. And unlike `SystemHome` at creation time, this computed path is never run back through the `com.ahsay.c` denylist. The call chain that matters is `doUpload -> FileService.a() -> getReplicatedPath(),` and the denylist appears in none of it.

Which means a `UserHome` of `../../webapps/rps` walks the write directory straight out of the receiver’s home and into a live, web-served Tomcat application:

`C:\AhsayCBS\rpsrecv_x\files\..\..\webapps\rps   ->   C:\AhsayCBS\webapps\rps`

**Figure 7.** The traversal resolving into the web root

From there it is a single `PUT` of a `.jsp` file. The upload is a plain octet-stream body with the path and the receiver’s credentials in headers:

**Figure 8.** Writing the webshell into `webapps/rps`

Requesting `/rps/status.jsp` runs it. On a Windows receiver, the AhsayCBS service runs as `LocalSystem`, so the webshell executes as SYSTEM. On Linux it runs as root. The same `cbs.jar` drives both platforms; the only thing the exploit changes between them is the install root, because the receiver’s path validator happily accepts a `C:\...` absolute path and the server rewrites our forward slashes to backslashes on the way to disk.

Putting it all together in a proof of concept, we bypass authentication, upload a webshell, execute a command, and clean up the webshell:

**Figure 9.** Proof of concept exploit

Our proof of concept can be found on our [GitHub](https://github.com/horizon3ai/AhsayCBS-Auth-Bypass-RCE).

## **Indicators of Compromise**

- Suspicious child processes spawning from \*\*`cbssvcX64.exe`\*\* (Windows) or the CBS JVM (Linux) – command interpreters, `curl`/`certutil`, miners, or persistence tooling.
- New `.jsp` files under `webapps/rps`, `webapps/cbs`, or any served application directory, especially files that answer with a `404` unless a specific parameter is supplied.
- New replication \*\*receivers\*\* whose `SystemHome` sits under the install directory, created outside a change window (`System Logs` → “Created new receiver”).
- Unexpected \*\*system administrator\*\* accounts (`ListSystemUsers`), and API logon entries recording “Logon to API from IP address …” for accounts you did not provision.
- Requests to `/*/api/json/*.do` and `/rps/obs7/rpsfile/upload` carrying a `FromServlet` field or `X-RSW-Request-*` headers from untrusted sources.

For more specific indicators of compromise from observed attacks we recommend referencing Huntress’s [report](https://www.huntress.com/blog/ahsaycbs-flaws-exploit).
