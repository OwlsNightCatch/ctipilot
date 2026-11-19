---
title: "NGINX2Root: New Remote Code Execution Vulnerabilities in nginx Require Urgent Patching - Xint Blog | Insights from Offensive Security Researchers"
author: Xint
url: https://xint.io/blog/nginx2root-remote-code-execution
hostname: xint.io
description: nginx2root is a collection of 5 critical CVEs, the most impactful of which allows an unauthenticated attacker to execute commands on an affected nginx server w…
sitename: Xint Blog | Insights from Offensive Security Researchers
date: "2026-11-18"
categories: ['Vulnerability Research']
tags: ['Vulnerability Research, News, Open Source Projects', 'Vulnerability Research', 'News', 'Open Source Projects']
fingerprint: be9ab249de2186cf
---
# NGINX2Root: New Remote Code Execution Vulnerabilities in nginx Require Urgent Patching

## **Introduction**

nginx is one of the most widely deployed web servers in the world. Finding an unauthenticated remote code execution bug in it has long been a holy grail for security researchers. The Xint research team recently found five. Each one leads to remote code execution on its own, but they affect different configurations.

Xint also found a separate vulnerability in the Linux kernel which can be chained with any of the nginx vulnerabilities to gain root privileges on the host. Together, we call these six vulnerabilities **nginx2root**.

**If you run nginx, update to** [**1.31.9**](https://github.com/nginx/nginx/releases#release-release-1.31.9) as soon as the fixed release becomes available. This article explains the root cause of each nginx2root vulnerability and summarizes our exploitability assessments. For exposure checks, see Section 2 and for patching and temporary mitigations, see Section 3.

## **1. Executive Summary**

### **What an attacker can do**

The most impactful of the five findings, CVE-2026-123007, allows an unauthenticated attacker to execute commands on an affected nginx server with HTTP/2 enabled. The commands run with the privileges of the nginx worker process that handles the request.

We chained this vulnerability with a separate flaw in the Linux kernel's SCTP subsystem to gain root privileges on the host. In our tests, the chain also escaped a Docker container running nginx and obtained root on the underlying host.

In the video below, we use CVE-2026-123007 to execute commands as the nginx worker inside a container, then use the kernel vulnerability to escalate to root on the host.

We ran this demo on AWS, attacking the server over its public IP address. Demos for AWS, GCP, Azure, and bare-metal servers are available at [<u>nginx2root.com</u>](http://nginx2root.com).

### **Affected versions**

Each one of the five nginx vulnerabilities are independent attack paths and do not need to be chained together. They differ in what configuration is affected.

| CVE | Affected configuration | First affected release for this path | Blocked by disabling HTTP/2? | 
|---|---|---|---|
| [CVE-2026-123007](https://www.cve.org/CVERecord?id=CVE-2026-123007) | HTTP/2 enabled | 1.9.5 | Yes | 
| [CVE-2026-123634](https://www.cve.org/CVERecord?id=CVE-2026-123634) | `resolver`, a request-derived `proxy_pass` destination, and `mirror` with `mirror_request_body off` | 1.13.4 | No | 
| [CVE-2026-123633](https://www.cve.org/CVERecord?id=CVE-2026-123633) | HTTP/2 with requests forwarded to an upstream (backend) server | 1.19.7 | Yes | 
| [CVE-2026-121810](https://www.cve.org/CVERecord?id=CVE-2026-121810) | HTTP/3 with requests forwarded to an upstream (backend) server | 1.25.0 | No | 
| [CVE-2026-113425](https://www.cve.org/CVERecord?id=CVE-2026-113425) | Mail proxy using `proxy on` and `auth_http` | 0.5.15 | No | 

For CVE-2026-123634, the table shows the setup we tested, which uses the `mirror` directive. Other nginx features that create subrequests, such as SSI, may reach the same bug, so turning off `mirror` alone does not make a server safe.

CVE-2026-123007 has been present since nginx introduced HTTP/2 in 2015, more than a decade ago. Every official release from 1.9.5 through 1.31.8 contains the vulnerable code, including the `master` branch on Nov 10, 2026. Even servers running recent releases therefore need the same checks for patch status and HTTP/2 exposure as older installations.

### **What to do**

Update to 1.31.9 when it is available. Until then, disabling HTTP/2 on affected listening ports blocks CVE-2026-123007 and CVE-2026-123633. It does not block the other three nginx vulnerabilities. Check your configuration against the table above and apply the matching mitigations in Section 3.3.

### **How we found them**

While preparing for ZeroDay Cloud 2026, a Xint researcher found CVE-2026-123007. A few days later, a fully automated Xint scan found the other four without human guidance.

### **nginx2root at a glance**

| Item | Details | 
|---|---|
| CVE | CVE-2026-123007 CVE-2026-123634 CVE-2026-123633 CVE-2026-121810 CVE-2026-113425 | 
| Severity | Critical | 
| Fixed version | 1.31.9 | 
| Impact | An unauthenticated remote attacker can execute arbitrary commands with nginx worker privileges | 
| Affected versions (CVE-2026-123007) | **All official releases from nginx 1.9.5 through 1.31.8. The vulnerable code was also present in** `master` **as of November 10, 2026** | 
| Code history (CVE-2026-123007) | Introduced with the first HTTP/2 release, nginx 1.9.5, and retained through the current affected releases | 
| Temporary mitigation (CVE-2026-123007) | Disable HTTP/2 on affected listening ports | 
| Complete fix | Update to 1.31.9 | 
| Reported by | Xint Researchers (@imssm99, @cdor1, @tjbecker, @yves) | 

## **2. Affected Versions and How to Check for Exposure**

Section 2 focuses on CVE-2026-123007, the vulnerability that affects the most servers. It only requires HTTP/2 to be enabled. For the other four nginx vulnerabilities, first check the configuration table in Section 1.

### **2.1. Affected Versions**

CVE-2026-123007 affects every official nginx release from 1.9.5 through 1.31.8. As of November 10, 2026, the vulnerable code was also still present in the development branch (`master`).

#### **2.1.1. Affected Linux Distributions**

**The version number alone may not show whether a server is patched.**

Three of the most common versions are the default package versions shipped by major Linux distributions. Ubuntu 24.04 comes with 1.24.0, Ubuntu 22.04 provides 1.18.0, and Debian 12 provides 1.22.1. These distributions may backport security fixes to the existing version instead of replacing it with a new nginx release.

A backport can fix a vulnerability without changing the version reported by `nginx -v`. Only the distribution's full package version changes. For example, Ubuntu 22.04 originally shipped `1.18.0-6ubuntu14`. By October 26, 2026, [<u>security updates</u>](https://ubuntu.com/security/notices/USN-8955-1) had brought the package to `1.18.0-6ubuntu14.22`, while the nginx version remained `1.18.0`.

To determine whether a specific fix is included, compare the full installed package version with the distribution's security advisory.

### **2.2. Internet Exposure**

As of November 10, 2026, Shodan returned 56.7 million hosts for `product:nginx`. Of these, 11.94 million (21.1%) reported an identifiable version. Among hosts with an identified version, 98.9% fell within the version range affected by CVE-2026-123007: 1.9.5 through 1.31.8.

These numbers are based on reported version strings and don’t confirm that a server is vulnerable. Exploiting CVE-2026-123007 also requires HTTP/2 to be enabled, and a reported version may already include a backported fix.

### **2.3. Commands to Check for Exposure**

A server is affected by CVE-2026-123007 if it runs an unpatched version, includes the HTTP/2 module, and has HTTP/2 enabled. The first three checks below test each of these conditions. The fourth tests whether HTTP/2 is reachable over the Internet. The table at the end of this section shows how to read the combined results.

#### **2.3.1. Check the Version**

First, print the nginx version.

`nginx -v 2>&1`
The command prints a version string such as `nginx version: nginx/1.31.8`.

- **1.9.5 through 1.31.8:** The official release contains the vulnerable code. Continue with the next checks.
- **1.9.4 or earlier:** Released before HTTP/2 support and thus not affected.
- **1.31.9 or later:** Likely patched, but confirm that the build includes the changes referenced in [github.com/nginx/nginx/releases#release-release-1.31.9](https://github.com/nginx/nginx/releases#release-release-1.31.9).
- **Distribution or appliance-specific version:** Do not rely on the version string alone. Confirm whether the fix was backported.

#### **2.3.2. Check for the HTTP/2 Module**

Check whether the binary was built with the HTTP/2 module.

```
nginx -V 2>&1 | grep -q -- '--with-http_v2_module' \
  && echo 'HTTP2_MODULE=present' \
  || echo 'HTTP2_MODULE=absent'
```
- `HTTP2_MODULE=present`: The binary contains the HTTP/2 code, which is vulnerable if not patched. Continue with the next check.
- `HTTP2_MODULE=absent`: The binary does not contain the HTTP/2 code and is not affected by this vulnerability.

#### **2.3.3. Check Whether HTTP/2 Is Enabled in the Configuration**

Search the configuration for directives that enable HTTP/2.

```
sudo nginx -T 2>&1 \
  | sed 's/#.*//' \
  | grep -nE 'listen[[:space:]].*http2|^[[:space:]]*http2[[:space:]]+on[[:space:]]*;'
```
Output, such as `listen 443 ssl http2;` or `http2 on;`, means HTTP/2 is enabled. No output means it is not. Note that `nginx -T` reads the configuration on disk. If you changed it without reloading nginx, the running configuration may differ.

#### **2.3.4. Check Whether HTTP/2 Is Reachable Over the Internet**

Run the command below from a machine outside your network. It asks the server for HTTP/2 during the TLS handshake. Replace both `{HOST}` placeholders with your domain, and change the port if you don’t use 443.

```
openssl s_client -connect {HOST}:443 -servername {HOST} -alpn h2 </dev/null 2>&1 \
  | grep -E 'ALPN protocol:|No ALPN negotiated|Connection refused|connect:errno|handshake failure'
```
If you see ALPN protocol: h2, the server accepts HTTP/2 from the Internet, while No ALPN negotiated means it doesn’t. Anything else means the connection failed, so check that the server is reachable and try again.

If a CDN or reverse proxy sits in front of nginx, the test only reaches the proxy, so also run it directly against the nginx server.

Interpret the combined results using the following table.

| Result | Assessment | 
|---|---|
| Unpatched 1.9.5 through 1.31.8 + `HTTP2_MODULE=present` + `ALPN protocol: h2` on the actual nginx port | **Vulnerable and externally exposed. Immediate action required** | 
| Unpatched 1.9.5 through 1.31.8 + `HTTP2_MODULE=present` + HTTP/2 disabled | **The vulnerable code is present, but the current attack path is disabled** | 
| 1.9.4 or earlier, or `HTTP2_MODULE=absent` | **Not affected by this vulnerability** | 
| 1.31.9 installed, or the fix confirmed in an older backported build | **Patched. No longer vulnerable** | 
| Connection failure, TLS handshake failure, or uncertain patch status | **Inconclusive. Further review required** | 

## **3. Response and Recommended Actions**

### **3.1. Immediate Action**

Update nginx to 1.31.9 when the fixed release is available, and confirm that the installed build includes fixes for all five vulnerabilities. If you cannot patch immediately, apply the mitigations for your configuration in Section 3.3. Note that disabling HTTP/2 addresses only two of the five nginx vulnerabilities.

After installing the update, restart nginx or complete a supported live binary upgrade. A configuration reload alone does not replace the running executable.

### **3.2. Investigating Possible Attacks**

An attack using CVE-2026-123007 may leave little evidence in nginx access logs. The `WINDOW_UPDATE` and `RST_STREAM` control frames used to trigger the vulnerability are not logged as requests, and TLS encrypts them in transit. The subsections below cover four other places to look: connection statistics (3.2.1), requests per connection (3.2.2), programs started by workers (3.2.3), and worker crashes (3.2.4). Section 3.2.5 explains how to weigh them together.

#### **3.2.1. Check Connection Statistics**

On the target server, inspect TCP statistics for port 443.

`sudo ss -tinp state established '( sport = :443 )'`
Run the command twice, a short interval apart, and compare the changes in `bytes_received` and `bytes_sent`. Prioritize connections that show several of these conditions together:

- A connection from the same external IP remains open for several minutes
- `bytes_received` continues to grow very quickly
- The server's `bytes_sent` is much smaller than the received volume
- The same external IP also creates many short-lived TLS connections

These patterns match the attack we tested. It sends a large number of `WINDOW_UPDATE` frames over one long-lived connection, so `bytes_received` keeps climbing while nginx sends little back. It also opens many short TLS connections from the same IP. If you see both for several minutes and there is no legitimate explanation, such as a large upload, block the source and investigate.

#### **3.2.2. Review Requests by Connection**

The default access log does not show which connection each request belongs to. The log format below adds the connection ID (`conn`), the number of requests on that connection, and the size of each request. Add it to the nginx `http` block. No debug build is needed.

```
log_format h2_hunt '$time_iso8601 src=$remote_addr conn=$connection '
                   'requests=$connection_requests proto=$server_protocol '
                   'status=$status request_length=$request_length '
                   'bytes_sent=$bytes_sent request_time=$request_time';
access_log /var/log/nginx/h2-hunt.log h2_hunt;
```
Validate and reload the configuration, then display only HTTP/2 requests.

```
sudo nginx -t && sudo nginx -s reload
sudo grep 'proto=HTTP/2.0' /var/log/nginx/h2-hunt.log | tail -n 200
```
Take a suspicious IP from Section 3.2.1 and add up the `request_length` of its log entries, per `conn`. Compare that total with the `bytes_received` that `ss` shows for the same IP. If `bytes_received` keeps growing quickly while the logged request lengths stay small, the client is sending a lot of data that never shows up as requests. That fits a flood of HTTP/2 control frames, as in the attack. Long `request_time` values in the same period are another sign.

#### **3.2.3. Monitor Command Execution by Workers**

Our exploit uses `execve()` to start a shell or another program. A normal nginx worker has no reason to run external programs, so any program it starts warrants immediate investigation. First, identify the worker account's UID.

`ps -eo uid,user,pid,ppid,args | grep '[n]ginx: worker process'`
On systems that use the Linux audit subsystem `auditd`, replace `NGINX_UID` with the numeric UID from the previous output and add the following rule.

```
sudo auditctl -a always,exit -F arch=b64 -S execve,execveat \
  -F euid=NGINX_UID -k nginx_worker_exec
```
The rule records executions only after it is installed. An empty result cannot rule out an earlier compromise. It also matches other processes using the same UID, so check the process and parent process IDs to establish whether an event came from nginx.

Review the records with:

`sudo ausearch -k nginx_worker_exec -ts recent -i`
Look for `/bin/sh`, `/bin/bash`, or any other program started by an nginx worker. If other applications run under the same account, check each event’s parent process against your service configuration to tell which ones came from nginx.

#### **3.2.4. Check for Abnormal Worker Exits**

A failed exploit attempt can crash an nginx worker, so look for abnormal exits and core dumps with the commands below.

```
sudo grep -Ei 'worker process.*exited|signal 11|segfault' /var/log/nginx/error.log
sudo coredumpctl list nginx
```
A worker can crash for reasons unrelated to an attack. Correlate these records with the other signals before drawing a conclusion.

#### **3.2.5. Assess the Evidence**

A program started by an nginx worker (Section 3.2.3) is the clearest sign of a successful attack. Investigate it immediately. The signs below are weaker, and each one can have a normal cause on its own. If several show up together and you cannot explain them, block the source and investigate:

- Sustained high inbound traffic (Section 3.2.1).
- Many connections from the same source (Section 3.2.1).
- A large gap between actual received bytes and logged request lengths (Section 3.2.2).
- Repeated abnormal worker exits (Section 3.2.4).

### **3.3. Emergency Mitigations Before Patching**

Before a patch is available, disabling the affected features can block the known attack paths. These measures are temporary. Install the fixed release when it becomes available.

#### **3.3.1. Disable HTTP/2 (CVE-2026-123007 and CVE-2026-123633)**

Both vulnerabilities arise while nginx handles HTTP/2 connections. Disable HTTP/2 on affected ports until the patch is installed. Clients that support HTTP/1.1 can continue using the service, but services that require HTTP/2, such as native gRPC, will be affected.

For nginx 1.25.1 and later, set `http2 off;` in each affected `server` block and remove any legacy `http2` parameter from its `listen` directives. Check all server blocks sharing the listening address and port.

```
listen 443 ssl;
http2 off;
```
For nginx 1.9.5 through 1.25.0, remove `http2` from `listen 443 ssl http2;`.

`listen 443 ssl;`
Validate and reload the configuration. Then repeat the HTTP/2 check from Section 2.3.4 to confirm the change worked.

```
sudo nginx -t
sudo nginx -s reload
openssl s_client -connect HOST:443 -servername HOST -alpn h2 </dev/null 2>&1 | grep -F 'ALPN protocol: h2'
```
The last command prints nothing once HTTP/2 is disabled. It also prints nothing if the connection fails, so make sure the site still loads normally over HTTPS.

#### **3.3.2. Remove Request-Time DNS Lookups (CVE-2026-123634)**

This mitigation is for servers that choose their upstream (backend) per request and also use `mirror`. This happens when `proxy_pass` contains a variable, such as `proxy_pass http://$host;`, and nginx uses its `resolver` to look up that name with DNS while handling the request.

The bug is triggered while the main request and its mirror wait for the same DNS answer. Until the patch is installed, point `proxy_pass` at a fixed upstream group instead. This removes the DNS lookup during the request and blocks the path we tested.

Setting `mirror_request_body on` also stopped our exploit, but it does not fix the resolver bug. Do not rely on this setting alone.

If you don’t need mirroring, turn it off in the affected `location` and point `proxy_pass` at a fixed upstream. Replace `{BACKEND_IP}` with your backend’s IP address and adjust the port if needed:

```
upstream backend_hotfix {
    server {BACKEND_IP}:8080;
}
location / {
    mirror off;
    proxy_pass http://backend_hotfix;
}
```
If you need mirroring, use fixed upstream groups for both the main request and the mirror. The example below sends the main request and the mirror to different backends; if both use the same backend, point them at a single fixed group instead:

```
upstream backend_main_hotfix {
    server [MAIN_SERVER_IP]:8080;
}
upstream backend_mirror_hotfix {
    server [MIRROR_SERVER_IP]:8080;
}
location / {
    mirror /mirror;
    proxy_pass http://backend_hotfix;
}
location = /mirror {
    internal;
    proxy_pass http://backend_mirror_hotfix;
}
```
Validate and reload the configuration:

```
sudo nginx -t
sudo nginx -s reload
```
#### **3.3.3. Disable HTTP/3 (QUIC) (CVE-2026-121810)**

The vulnerability is in how nginx handles HTTP/3 request streams on a QUIC connection, so remove the QUIC listeners from affected services until the patch is installed.

In every affected `server` block, remove the `listen` directives that contain `quic`, set `http3 off`, and replace any `Alt-Svc` header advertising HTTP/3 with `Alt-Svc 'clear'`. The regular TLS listener on TCP stays, so the result should look like this:

```
listen 443 ssl;
# listen 443 quic reuseport;
# listen [::]:443 quic reuseport;
http3 off;
add_header Alt-Svc 'clear' always;
```
Validate and reload the configuration. Then check whether anything still accepts UDP traffic on port 443 (adjust the port if needed):

```
sudo nginx -t && sudo nginx -s reload
sudo ss -lunp 'sport = :443'
```
If the output still shows `nginx`, a QUIC listener is still active. For extra defense, also block UDP on that port using a firewall.

#### **3.3.4. Restrict Access to the Mail Proxy (CVE-2026-113425)**

This mitigation only applies if you use nginx as a mail proxy in front of IMAP, POP3, or SMTP servers. You are affected if the `mail` block uses `proxy on` together with `auth_http`. With `auth_http`, nginx asks an HTTP service whether each login is valid. The bug is triggered during login, and the attacker does not need valid credentials. Until the patch is installed, keep untrusted clients away from the mail proxy.

If the proxy does not need external access, bind every IMAP, POP3, and SMTP listener to a loopback address. Only programs on the same machine can then connect. Remote clients, such as users' mail apps, will no longer be able to reach the proxy. For example:

`listen 127.0.0.1:143;`
Validate and reload the configuration, then confirm that the mail ports are no longer listening on external addresses:

```
sudo nginx -t && sudo nginx -s reload
sudo ss -ltnp | grep -E ':(25|110|143|465|587|993|995)([[:space:]]|$)'
```
The command checks the standard mail ports. Add yours if they differ. If outside clients do need to reach the proxy, use your firewall to allow only the IP addresses you trust.

#### **3.3.5. Close Existing Connections**

A reload applies the new configuration only to new connections. Connections that were already open, such as HTTP/2 or mail sessions, stay with the old workers and keep using the old configuration. In `ps` these workers show up as `nginx: worker process is shutting down`.

If such workers are still running after the reload, restart nginx through your service manager (for example, `systemctl restart nginx`). A restart forcibly disconnects every client and cuts off downloads, uploads, and mail sessions in progress, so expect a short service interruption.

## **4. Discovery and Disclosure Timeline**

Finding five remote code execution bugs at once is unusual for nginx. In more than twenty years of security research, nginx has had very few unauthenticated RCEs. One example is CVE-2013-2028, a stack buffer overflow triggered by a crafted HTTP request.

We aren’t the only ones finding more nginx bugs this year. In 2025, the [<u>nginx security advisory list</u>](https://nginx.org/en/security_advisories.html) recorded two new vulnerabilities. By November 17 this year, it had recorded 26, not counting nginx2root, and several were memory corruption bugs such as buffer overflows and use-after-frees. AI-assisted research is finding bugs faster than ever, even in code as heavily studied as nginx. With nginx2root, Xint adds five more at once.

The timeline below covers discovery, disclosure, and the scheduled patch release. All dates are provided in Coordinated Universal Time (UTC+0).

| Date | Event | 
|---|---|
| Oct 11, 2026 | Xint research team discovered the vulnerabilities | 
| Oct 16, 2026 | Vulnerabilities reported to F5 through HackerOne | 
| Oct 20, 2026 | HackerOne completed validation | 
| Oct 27, 2026 | Reports delivered to F5's nginx development team | 
| Nov 09, 2026 | nginx team requested patch validation | 
| Nov 10, 2026 | Xint research team completed patch validation | 
| Nov 18, 2026 | Patch release scheduled | 

## **5. Technical Analysis of the nginx Vulnerabilities**

This section examines the five nginx vulnerabilities. CVE-2026-123007 begins with an error in window arithmetic that leads to an out-of-bounds write. The other four are use-after-free vulnerabilities. For each, we explain the relevant nginx features and behavior, trace the code behind the bug, and summarize how it leads to remote code execution. We explain how to achieve address disclosure and controlled memory corruption, but we intentionally omit the final steps needed to reproduce the full exploits.

### **5.1. CVE-2026-123007**

CVE-2026-123007 is an integer overflow vulnerability in HTTP/2 flow control. A send window exceeds its permitted maximum, eventually producing an invalid memory-copy length which leads to out-of-bounds reads and writes on the heap.

#### **5.1.1. How nginx Manages HTTP/2 Send Windows**

HTTP/2 handles multiple requests and responses over a single connection. Each request and response pair uses a stream. Streams created by the client receive distinct identifiers called Stream IDs, such as 1, 3, and 5. Within each stream, HEADERS frames carry the headers and DATA frames carry the body.

HTTP/2 uses flow control to keep the server from sending more data than the client is ready to receive. The server tracks this with send windows, one per stream plus one for the whole connection, which we call the h2c window. Each window holds the amount of DATA the server may still send. The server can only send DATA on a stream if both that stream's window and the h2c window have enough credit left. When the client is ready for more, it sends a `WINDOW_UPDATE` frame, and the server increases the matching window by that amount.

The Stream ID in `WINDOW_UPDATE` determines which window is increased. Stream ID 0 updates the h2c window, while a nonzero Stream ID updates only that stream's window.

nginx uses a default window of 65,535 (`0xffff`) and a maximum of `0x7fffffff` (`(1U << 31) - 1`).

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2.h#L50-L51
#define NGX_HTTP_V2_MAX_WINDOW      ((1U << 31) - 1)
#define NGX_HTTP_V2_DEFAULT_WINDOW  65535
```
nginx holds outgoing frames in an in-memory output queue before sending them through the socket. When it queues response DATA, `ngx_http_v2_send_chain()` deducts the DATA length from both the connection-level send window, `h2c->send_window`, and the stream's send window, `stream->send_window`.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2_filter_module.c#L1232-L1244
ngx_http_v2_queue_frame(h2c, frame);
h2c->send_window -= frame_size;
stream->send_window -= frame_size;
stream->queued++;
```
If the stream is canceled before the DATA is sent, `ngx_http_v2_filter_cleanup()` removes that stream's remaining DATA frames from the queue and returns the deducted length to the connection-level send window.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2_filter_module.c#L1719-L1767
h2c->send_window += window;
```
nginx deducts credit when it queues DATA, and returns that credit if the stream is canceled before the DATA is sent. Both steps are valid. The problem is what can happen in between. While the DATA is still queued, the client can send a `WINDOW_UPDATE` that raises the window again. If the stream is then canceled, cleanup adds the returned credit on top of the raised window. Cleanup never checks the result against the HTTP/2 maximum, so `h2c->send_window` can end up above its permitted upper bound.

#### **5.1.2. Vulnerability Details**

The sequence from the window-accounting error to command execution is summarized below. Subsection (1) covers steps 1–2, subsection (2) covers step 3, and subsection (3) covers steps 4–6 at a high level.

| Step | Description | 
|---|---|
| Hold DATA in the queue | Queue response bodies and deduct their length from the send windows, while preventing the DATA from reaching the client. | 
| Increase the window, return queued credit | Increase the send window via `WINDOW_UPDATE`, then cancel the streams so cleanup adds the credit deducted for queued DATA. | 
| Bypass the upper-bound check | Once the shared connection window exceeds its maximum, the remaining-capacity calculation fails and later `WINDOW_UPDATE` frames remain accepted. | 
| Create an abnormal copy length | The code interprets the same bits as signed and unsigned values, converting a small negative distance into a very large copy length. | 
| Disclose addresses and corrupt memory | Position both ends of the copy to return memory pointers in a response, corrupting TLS allocation metadata. | 
| Control a cleanup callback | Use the disclosed addresses and corrupted memory to overwrite a cleanup function pointer, then execute an arbitrary command when cleanup calls it. | 

#### **(1) Exceeding the 31-bit Limit When Queued Credit Is Returned**

The first goal is to build up DATA in nginx's output queue that has consumed window credit but has not been sent.

The client first raises the connection send window to its maximum (`Wmax`) with a `WINDOW_UPDATE` on Stream ID 0. The client sets the initial send window for new streams through `SETTINGS_INITIAL_WINDOW_SIZE` in a SETTINGS frame. Setting it to 0 allows nginx to create response HEADERS, but prevents it from sending DATA. This keeps response bodies pending until the client chooses to release them.

Next, the client stops reading and sends a burst of PING frames. nginx places control-frame responses (including PING acknowledgments) ahead of pending DATA, so these acknowledgments fill the TLS and TCP send buffers. The client then sends each stream enough `WINDOW_UPDATE` credit for its entire response body, causing nginx to queue the DATA and deduct its length from the connection send window. Because the TLS and TCP buffers are already full, this DATA remains queued indefinitely.

Let `Q` be the total amount of this queued DATA. The client now adds `Q` back to the h2c window twice. First, it sends a `WINDOW_UPDATE` on Stream ID 0 that grants `Q` of credit. Second, it sends `RST_STREAM` to cancel the streams. Cancellation triggers cleanup, which discards the unsent DATA and returns its credit, adding `Q` to the h2c window again.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2_filter_module.c#L1723-L1767
if (frame->stream == stream && !frame->blocked) {
    *fn = frame->next;
    window += frame->length;
}
h2c->send_window += window;
```
This second addition, shown on the last line above, has no upper-bound check. As a result, the h2c window moves through four values:

- `Wmax`: the client raises the window to its maximum.
- `Wmax - Q`: queuing the DATA deducts `Q`.
- `Wmax`: the `WINDOW_UPDATE` on Stream ID 0 grants `Q` back.
- `Wmax + Q`: cleanup returns `Q` a second time, pushing the window past the 31-bit limit.

The exact response sizes and stream count do not matter. What matters is that the same known quantity `Q` is added back twice, once by the `WINDOW_UPDATE` and once by cleanup.

#### **(2) Unsigned Underflow in the Window Check**

`ngx_http_v2_state_window_update()` calculates the remaining capacity before applying an increment.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2.c#L2564-L2575
if (window > NGX_HTTP_V2_MAX_WINDOW - h2c->send_window) {
    return ngx_http_v2_connection_error(h2c, NGX_HTTP_V2_FLOW_CTRL_ERROR);
}
h2c->send_window += window;
```
This check works only while the shared connection window is at or below `Wmax`. `h2c->send_window` has the unsigned type `size_t`, and the previous step has already changed it to `Wmax + Q`. The remaining-capacity expression is therefore `Wmax - (Wmax + Q)`, which would be negative as a signed value, but unsigned arithmetic wraps it into a very large positive value.

nginx treats this value as available capacity and continues accepting connection-level `WINDOW_UPDATE` frames for h2c. Each increment still complies with the HTTP/2 specification, but the check fails to detect that the current window is already outside its valid range. Repeating this process can increase the send window to any arbitrary 64-bit value.

#### **(3) From the Oversized Window to an Out-of-Bounds Copy**

`h2c->send_window` has the unsigned type `size_t`. On 64-bit targets, increasing it to, say, `2^64 - d` makes it appear very large as an unsigned value, but casting it to the signed type `off_t` yields a small negative value `-d`.

`ngx_http_v2_send_chain()` moves this value into the DATA frame size. It first compares the send window with `limit`, i.e. the maximum amount that the current call may send.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2_filter_module.c#L1144-L1146
if (limit == 0 || limit > (off_t) h2c->send_window) {
    limit = h2c->send_window;
}
```
A positive `limit` is greater than `-d`, so the condition is true and `limit` also becomes `-d`.

The next comparison uses `frame_size`, the current DATA frame size, and `limit`.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2_filter_module.c#L1163-L1166
if ((off_t) frame_size > limit) {
    frame_size = (size_t) limit;
}
```
A positive `frame_size` is greater than `-d`, so this condition is also true. Converting `-d` back to `size_t` produces `2^64 - d`, replacing a normal DATA size with a very large value.

nginx stores the value in `rest`, which tracks the length not yet attached to a buffer. It then passes this value to `ngx_http_v2_filter_get_shadow()` to set the buffer's start and end pointers.

```
// Call site: https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2_filter_module.c#L1169-L1207
// Implementation: https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2_filter_module.c#L1287-L1308
rest = frame_size;
cl = ngx_http_v2_filter_get_shadow(stream, in->buf, offset, rest);
static ngx_chain_t *
ngx_http_v2_filter_get_shadow(ngx_http_v2_stream_t *stream, ngx_buf_t *buf,
    off_t offset, off_t size)
{
    chunk->last = chunk->pos + size;
}
```
As an `off_t`, `size` holds `-d`, so `chunk->last` points `d` bytes before `chunk->pos`. The TLS output path later uses the difference between these pointers as the copy length.

```
// Declaration: https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/event/ngx_event_openssl.c#L3054-L3057
// Copy path: https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/event/ngx_event_openssl.c#L3137-L3150
ssize_t size;
size = in->buf->last - in->buf->pos;
ngx_memcpy(buf->last, in->buf->pos, size);
```
`last - pos` is `-d`, but the length argument to `memcpy()` is a `size_t`. The final conversion turns it back into `2^64 - d`, passing in a very large copy length.

A copy of almost `2^64` bytes would normally run past the end of the heap and crash the worker. It does not here, because of how glibc handles large copies. The x86-64 glibc `memcpy()` path used in our experiment does not copy front to back. It first loads the start and the end of the source, then copies the middle in a loop that walks backward from the end of the destination toward `dest`.

The end of the destination is `dest + size`. With `size = 2^64 - d`, this sum overflows the 64-bit address space and wraps around to `dest - d`, which is `d` bytes below `dest`. Since the end now lies below the start, the backward loop stops after one pass, and the large middle region is never touched. This backward-copy structure, which moves four 32-byte vectors per iteration, has been present in glibc's x86-64 implementation since version 2.24, released in 2016.

A simplified version of the glibc 2.41 AVX2 path is shown below.

```
# Introduced in: https://github.com/bminor/glibc/blob/glibc-2.24/sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S#L413-L462
# https://github.com/bminor/glibc/blob/glibc-2.41/sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S#L513-L554
head = load128(src)
tail = load32(src + size - 32)
end = (dest + size) mod 2^64
cursor = align_down(end - 129, 32)
do {
    copy128(dst=cursor, src=src + (cursor - dest))
    cursor -= 128
} while (cursor > dest)
store128(dst=dest, data=head)
store32(dst=end - 32, data=tail)
```
`align_down(x, 32)` rounds `x` down to a 32-byte boundary. When `end` is 32-byte aligned, as in the example below, `cursor = align_down(end - 129, 32)` becomes `end - 160`. glibc copies 128 bytes from this position and separately copies the final 32 bytes.

```
end - 160                         end - 32             end
    |---------- 128 bytes ----------|------ 32 bytes -----|
              loop copy                    fixed copy
```
Since `cursor` is already below `dest`, the loop runs only once. The long middle region is skipped, leaving only the first 128 bytes and the final 160 bytes to be copied.

```
src ~ src + 127                    -> dest ~ dest + 127
src - d - 160 ~ src - d - 1       -> dest - d - 160 ~ dest - d - 1
```
`dest` is the next write position in the TLS plaintext buffer, so it falls right after whatever nginx has already written there. Before the response body, nginx writes the acknowledgments for the client's control frames, and the client controls how many of those it sends. In the nginx source, an HTTP/2 frame header is 9 bytes, PING data is 8 bytes, and SETTINGS ACK data is 0 bytes.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2.h#L27
#define NGX_HTTP_V2_FRAME_HEADER_SIZE    9
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2.c#L30-L34
#define NGX_HTTP_V2_SETTINGS_ACK_SIZE    0
#define NGX_HTTP_V2_PING_SIZE            8
```
A PING without the ACK flag therefore produces a 17-byte PING ACK, while SETTINGS produces a 9-byte SETTINGS ACK. If the client sends `p` PING frames and `s` SETTINGS frames, nginx first generates `17p + 9s` bytes of responses. Including the 9-byte DATA frame header that follows them gives the start position of the next response body.

```
P = 17p + 9s + 9
dest = TLS + P
```
The client adjusts the send window with `WINDOW_UPDATE` so that `d = P - 64`. The copy end, `dest - d`, then becomes `TLS + 64`. The 160-byte region then spans the 96 bytes immediately before the TLS buffer and the first 64 bytes inside it.

The second move copies the 160 bytes just below `src - d` onto the edge of the TLS buffer. The attacker wants two things in those bytes: a chosen value to overwrite the heap metadata before the TLS buffer, and pointers that land inside the buffer and are sent back in the response. The request pool has both. It holds the request's headers, along with nginx's structures that describe them and point into the nginx image and heap. To move `src` there, the attacker sends a Range header that asks for several byte ranges. nginx then builds a multipart response that starts with a boundary string allocated in the request pool, so `src` points there.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/modules/ngx_http_range_filter_module.c#L484-L505
ctx->boundary_header.data = ngx_pnalloc(r->pool, size);
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/modules/ngx_http_range_filter_module.c#L867-L882
b->pos = ctx->boundary_header.data;
```
This `b->pos` becomes `in->buf->pos` as it passes through the output path, so it is the `src` used by the final `memcpy()`.

With `src` in the request pool, the attacker fills the 160 bytes below `src - d` using `Cookie` fields. When the same request contains multiple `Cookie` fields, nginx adds two bytes per separator to calculate the total length, then joins the values with `"; "`. It stores the length and combined buffer address in the request header structure.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2.c#L3725-L3769
len += vals[i].len + 2;
len -= 2;
h->key.data = cookie.data;
h->value.len = len;
h->value.data = buf;
```
`h->key.data` points to a static string in the nginx image, while `h->value.data` points to the Cookie buffer on the heap. This structure therefore contains an attacker-controlled length together with pointers into the nginx image and heap.

If the current request-pool block has enough space, nginx places a new small allocation immediately after the previous one.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/core/ngx_palloc.c#L157-L166
m = p->d.last;
if ((size_t) (p->d.end - m) >= size) {
    p->d.last = m + size;
    return m;
}
```
The Cookie count and lengths control the data and its placement, while the Range and URI lengths position the multipart buffer used as `src`. This allows the 160 bytes immediately before `src - d` to be arranged as follows.

```
Source:      [96 bytes containing the value for the size field][64 bytes of code and heap pointers]
Destination: [96 bytes before the TLS buffer, containing heap metadata][first 64 bytes of the TLS plaintext buffer]
```
The first 96 bytes overwrite the size field in the heap area preceding the TLS plaintext buffer. The remaining 64 bytes are sent in the TLS response, disclosing nginx image and heap addresses. A single malformed copy therefore provides both an out-of-bounds write and address disclosure. These can be used to overwrite a cleanup function pointer and execute commands with nginx worker privileges. We omit the detailed function-pointer overwrite procedure.

#### **5.1.3. Exploitability Validation**

Using only an externally reachable TLS/HTTP/2 port, we demonstrated unauthenticated remote code execution. The exploit corrupted the send window, disclosed nginx image and heap addresses, and took control of a cleanup function to execute commands with nginx worker privileges.

#### **Validation Results**

The Xint research team confirmed that our exploit works under concurrent normal traffic and across servers with different hardware specifications. On AWS, GCP, and Azure, we verified it from inside the target server, across a private network with separate sender and target hosts, and over a public HTTPS endpoint.

| Cloud | Inside target server | Private network, VPC or VNet | Public IP | 
|---|---|---|---|
| AWS | Success | Success | Success | 
| GCP | Success | Success | Success | 
| Azure | Success | Success | Success | 

### **5.2. CVE-2026-123634**

CVE-2026-123634 is a use-after-free in the nginx DNS resolver logic. A request's handler can free another resolver context that the waiting-list loop has not yet processed, which then continues to use the freed memory.

#### **5.2.1. How nginx Resolves Upstream Names at Request Time**

nginx can act as a reverse proxy, forwarding client requests to a backend server (called an *upstream*) to handle them. The `proxy_pass` config directive specifies the location of the upstream.

An upstream can be fixed in the configuration or chosen from the request. For example, `proxy_pass http://$host;` uses the request’s hostname in `$host` as the destination. This value usually comes from the client's `Host` header. If nginx needs a DNS lookup to obtain the server's IP address, it queries the DNS servers specified by the `resolver` directive.

Because DNS resolution takes time, nginx continues handling other requests while it waits for a DNS answer. Each lookup has a resolver context (`ngx_resolver_ctx_t`) holding its state, result, and a `handler` to call when the lookup finishes.

The resolver tracks each domain name in a node. If a lookup for the same name is already in flight, nginx does not send a second query, preferring instead to push the new context onto the head of that node's waiting list.

When the answer finally arrives, the resolver detaches the waiting list from the node by setting `rn->waiting` to `NULL`. It then walks the list and calls each context's `handler`, saving the next context in `next` before each call.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/core/ngx_resolver.c#L2131-L2147
next = rn->waiting;
rn->waiting = NULL;
...
while (next) {
    ctx = next;
    ctx->state = code;
    ctx->valid = ngx_time() + (r->valid ? r->valid : 10);
    next = ctx->next;
    ctx->handler(ctx);
}
```
A handler that frees a later context in the list therefore leaves `next` dangling. However, separate requests cannot cause this, because terminating a request frees only its own contexts. Hence, this is only a bug if the two contexts come from the same request.

In our testing, we found only one configuration option which creates two contexts attached to the same request. The `mirror` config directive copies a request to a second location as a background subrequest. It is commonly used to send a copy of live traffic to a test system. If the main request and its mirror use the same upstream name, their contexts can wait for the DNS answer on the same node.

#### **5.2.2. Vulnerability Details**

**(1) Terminating the Main Request Frees the Mirror's Context**

If the DNS lookup fails, the main request's `ngx_http_upstream_resolve_handler()` tries to send a 502 response. If the client has reset the TCP connection, that write can fail, causing `ngx_http_terminate_request()` to terminate the main request.

The main request’s `cleanup` list includes the mirror's upstream cleanup, so the cleanup code below also runs for the mirror, even though its DNS result has not yet been processed.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/ngx_http_upstream.c#L4802-L4805
if (u->resolved && u->resolved->ctx) {
    ngx_resolve_name_done(u->resolved->ctx);
    u->resolved->ctx = NULL;
}
```
`ngx_resolve_name_done()` then frees the mirror's context while the resolver loop still holds it in `next`.

**(2) The Resolver Uses the Freed Context**

Before the resolver loop reaches it, the mirror's context is still in state `NGX_AGAIN`. Before freeing a context in this state, `ngx_resolve_name_done()` tries to unlink it from the node's waiting list. But the loop has already detached that list and set `rn->waiting` to `NULL`. The search finds nothing, and the context is freed anyway.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/core/ngx_resolver.c#L554-L595
if (ctx->state == NGX_AGAIN || ctx->state == NGX_RESOLVE_TIMEDOUT) {
    rn = ctx->node;
    if (rn) {
        p = &rn->waiting;
        w = rn->waiting;
        while (w) {
            ...
        }
        ngx_log_error(NGX_LOG_ALERT, r->log, 0,
                      "could not cancel %V resolving", &ctx->name);
    }
}
done:
    ...
    ngx_resolver_free_locked(r, ctx);
```
Control then returns to the resolver loop, which advances to the context saved in `next`, i.e. the mirror's freed context. The loop now triggers the use-after-free by writing `ctx->state` and `ctx->valid`, reading `ctx->next`, and calling `ctx->handler(ctx)`. If another allocation reclaims the freed context’s memory, both `next` and `handler` are attacker controlled. As a result, the attacker can redirect the list traversal and the final indirect call, gaining control over the program execution.

To execute arbitrary code, we first need an address disclosure. Interestingly, this vulnerability can itself be leveraged for the disclosure. glibc's free-list pointer overwrites the context's next field, so the loop's `next` "context" is a freed array of DNS records whose contents we choose. We then employ a trick: we point the controlled handler at the `vsyscall` `gettimeofday()` address (which is fixed on amd64 systems), forging a heap chunk size and placing glibc and heap pointers inside a DNS query that nginx sends to our controlled server.

After the information disclosure, we can chain the loop through that array to a fake `context` in a pending request body, with its handler set to `system()` to get arbitrary command execution on the host.

#### **5.2.3. Exploitability Validation**

| Item | Result | 
|---|---|
| Target | Official `nginx:1.31.8` image, with a server block using request-time DNS resolution and `mirror` added to the stock configuration | 
| Entry point | HTTP on port 8080 and DNS answers for the attacker's zone | 
| Authentication | None | 
| Network requirement | nginx's recursive resolver must reach the attacker's authoritative DNS server | 
| Host kernel | Ubuntu Linux 6.8 (x86-64), with `vsyscall=xonly` | 
| Result | Remote code execution with nginx worker privileges | 

### **5.3. CVE-2026-123633**

CVE-2026-123633 is a use-after-free caused by an active HTTP/2 connection remaining eligible for draining. When a request opens an upstream connection, nginx can close the request's own HTTP/2 connection and free its memory while the upstream code continues to access it. This vulnerability requires nginx to open an upstream connection, which is common for <u>production</u> uses of nginx.

#### **5.3.1. How nginx Reuses Connections Under Pressure**

Each nginx worker has a fixed number of connection slots, set by `worker_connections`. Client and upstream connections share these slots. When slots run low, nginx closes idle connections to reclaim them for other purposes. To track which connections can be reclaimed, nginx marks connections as `reusable` if they meet some protocol-specific conditions, such as idle HTTP/1.1 keep-alive connections or HTTP/2 connections with no active streams. These `reusable` connections are tracked in a dedicated queue.

Before allocating a slot, `ngx_get_connection()` calls `ngx_drain_connections()`. If at most 1/16 of the slots are free and the reusable queue is not empty, it closes connections starting from the oldest entries, a process referred to as “draining”.

The drain sets `c->close` and calls each selected connection's read handler directly. These calls are synchronous, and slot allocation resumes only after the handler returns.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/core/ngx_connection.c#L1411-L1442
if (cycle->free_connection_n > cycle->connection_n / 16
    || cycle->reusable_connections_n == 0)
{
    return;
}
...
n = ngx_max(ngx_min(32, cycle->reusable_connections_n / 8), 1);
for (i = 0; i < n; i++) {
    ...
    q = ngx_queue_last(&cycle->reusable_connections_queue);
    c = ngx_queue_data(q, ngx_connection_t, queue);
    ...
    c->close = 1;
    c->read->handler(c->read);
}
```
#### **5.3.2. Vulnerability Details**

**(1) An Active HTTP/2 Connection Stays in the Reusable Queue**

`ngx_http_v2_handle_connection()` queues an HTTP/2 connection as reusable when it has no active streams or pending output frames. If the last read stopped in the middle of a frame, `h2c->state.incomplete` is set, but the flag is only checked after placing the connection in the queue:

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2.c#L628-L674
if (h2c->last_out || h2c->processing) {
    return;
}
...
ngx_reusable_connection(c, 1);
if (h2c->state.incomplete) {
    return;
}
```
Normally, an idle connection has its read handler updated to `ngx_http_v2_idle_handler()`, which takes it off the queue when data arrives. However, when `ngx_http_v2_handle_connection` returns early because of an incomplete frame, the connection keeps the normal `ngx_http_v2_read_handler()`, which never removes it from the reusable queue.

The flaw is therefore triggered as follows:

1. A client sends the first part of a HEADERS frame, which puts the connection in the reusable queue.
2. The client then sends the rest, which opens a stream.
3. If that request opens an upstream connection and triggers a drain, the drain may reclaim the connection the newly opened stream runs on.

#### **(2) The Upstream Connect Frees Its Own Request**

To reach the upstream, the request needs another connection slot. `ngx_event_connect_peer()` calls `ngx_get_connection()`, which runs the drain if slots are low. The HTTP/2 connection left in the reusable queue can now be selected for closure.

The HTTP/2 read handler sees `c->close` and tries to send `GOAWAY`, but if the client has already reset the TCP connection, the write fails and `ngx_http_v2_finalize_connection()` closes the connection and its streams.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2.c#L356-L382
if (c->close) {
    c->close = 0;
    ...
    if (!h2c->goaway) {
        h2c->goaway = 1;
        if (ngx_http_v2_send_goaway(h2c, NGX_HTTP_V2_NO_ERROR)
            == NGX_ERROR)
        {
            ngx_http_v2_finalize_connection(h2c, 0);
            return;
        }
        if (ngx_http_v2_send_output_queue(h2c) == NGX_ERROR) {
            ngx_http_v2_finalize_connection(h2c, 0);
            return;
        }
    }
```
Closing the stream calls `ngx_http_free_request()`, which destroys the request pool containing both the request `r` and its upstream structure `u`.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/ngx_http_request.c#L4062-L4071
/*
 * Setting r->pool to NULL will increase probability to catch double close
 * of request since the request object is allocated from its own pool.
 */
pool = r->pool;
r->pool = NULL;
ngx_destroy_pool(pool);
```
When the drain returns, nginx continues running the freed request's upstream code. It connects to the upstream, sends the proxied request, and handles events on that connection, all through the freed `r` and `u`.

With some heap grooming techniques, we arrange for a glibc largebin header to land on top of `u` and the header's `bk_nextsize` field to land on `u->peer.sockaddr`. It then points at bytes we controlled (a `sockaddr_in` for our own server), causing the upstream connection to actually connect to our own server.

To bypass ASLR, we simply accept the connection and nginx sends the freed request buffer, which now contains a variety of pointer values. The worker then crashes, but its replacement has the same address layout.

To execute commands, we use a different grooming technique to reclaim the freed request with a fake one whose upstream read handler is `execv()`. When we refuse the connection, epoll reports an error, and nginx calls that handler.

#### **5.3.3. Exploitability Validation**

| Item | Result | 
|---|---|
| Target | Official `nginx:1.31.8` image, with one TLS/HTTP/2 server using `proxy_pass` added to the stock `nginx.conf` | 
| Entry point | A TLS port with ALPN `h2`, plus an HTTP/1 port used to occupy connection slots | 
| Authentication | None | 
| Network requirement | nginx can open a TCP connection to the attacker | 
| Result | Remote code execution with nginx worker privileges | 

### **5.4. CVE-2026-121810**

CVE-2026-121810 is a use-after-free caused by closing a QUIC connection while one of its HTTP/3 requests is still running. During stream creation, the parent QUIC connection is incorrectly made eligible for draining. The request's subsequent upstream connect can then free its own request memory.

The bug is similar to CVE-2026-123633, but it is triggered by a slightly different mechanism, so our writeup will omit some definitions and background we already covered. As a result, we recommend reading Section 5.3 before reading this section.

#### **5.4.1. How nginx Handles HTTP/3 Streams as Connections**

HTTP/3 carries multiple request streams over one QUIC connection, but nginx internally allocates one `ngx_connection_t` for the QUIC connection and an additional one for each stream. All come from the same worker's connection slots, so creating a request stream also requires a free slot. We refer to the QUIC connection containing these streams as the parent connection. Both QUIC connections and HTTP/3 request streams waiting for headers may be eligible for draining.

When an individual stream closes, nginx checks whether the parent connection can also be drained. `ngx_quic_can_shutdown()` walks the parent's stream tree, and if every remaining stream is cancelable, nginx puts the parent connection in the reusable queue.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/event/quic/ngx_event_quic_streams.c#L1168-L1170
if (!pc->reusable && ngx_quic_can_shutdown(pc) == NGX_OK) {
    ngx_reusable_connection(pc, 1);
}
```
#### **5.4.2. Vulnerability Details**

**(1) Re-Queuing the QUIC Connection During Stream Creation**

Before allocating a connection slot for a new stream, `ngx_quic_create_stream()` takes the parent connection off the reusable queue, which is meant to prevent `ngx_get_connection()` from draining the parent during slot allocation.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/event/quic/ngx_event_quic_streams.c#L734-L743
reusable = c->reusable;
ngx_reusable_connection(c, 0);
sc = ngx_get_connection(c->fd, log);
if (sc == NULL) {
    ngx_destroy_pool(pool);
    ngx_queue_insert_tail(&qc->streams.free, &qs->queue);
    ngx_reusable_connection(c, reusable);
    return NULL;
}
```
However, the new stream only enters the parent's stream tree after the connection slot is allocated.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/event/quic/ngx_event_quic_streams.c#L814
ngx_rbtree_insert(&qc->streams.tree, &qs->node);
```
Suppose the drain closes an existing idle stream on the same parent connection. If both directions of that stream have finished, it can trigger the check that decides whether the parent can be drained, but this check cannot see a stream that is still being created. With no other non-cancelable streams in the tree, nginx puts the parent back in the reusable queue, where it stays even after the new stream has been created.

**(2) The Upstream Connect Frees the Request**

When the new stream's request connects upstream, it needs another slot, which can run the drain again and select the parent QUIC connection that was just queued. `ngx_quic_close_connection()` calls `ngx_quic_close_streams()` to close the parent's streams, which terminates the request whose upstream connect is still in progress.

`ngx_http_free_request()` destroys the request pool, including the upstream structure `u`. Control then returns to `ngx_event_connect_peer()`, which continues using the freed `u->peer` and causes a use-after-free.

From here, the ASLR bypass and control-flow hijack paths mirror those in Section 5.3.2, so they are omitted here for brevity.

#### **5.4.3. Exploitability Validation**

| Item | Result | 
|---|---|
| Target | Official `nginx:1.31.8` amd64 image, with an HTTP/3 proxy server added to the stock `nginx.conf` | 
| Entry point | UDP 443 (HTTP/3), TCP 443 (HTTP/2) and TCP 80 | 
| Authentication | None | 
| Network requirement | nginx can open a TCP connection to the attacker's listener | 
| Result | Remote code execution with nginx worker privileges | 

### **5.5. CVE-2026-113425**

CVE-2026-113425 is a use-after-free in the mail proxy's `auth_http` authentication path. Closing the client connection frees its session, but the connection to the authentication service remains open. A later event on that connection uses the freed session.

#### **5.5.1. How the Mail Proxy Authenticates Clients**

nginx can proxy IMAP, POP3, and SMTP between clients and mail servers. When a client logs in, nginx asks an HTTP service, configured with `auth_http`, whether the credentials are valid and which backend mail server to use.

During this lookup, nginx maintains two connections: one to the client and one to the HTTP authentication service; the latter is referred to as the auth connection.

`ngx_mail_auth_http_init()` creates a lookup context with its own memory pool. However, the auth connection's `data` and `pool` fields point to the client's session `s` and the client connection's pool. That pool must remain allocated while the auth connection uses the session.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/mail/ngx_mail_auth_http_module.c#L216-L221
ctx->peer.connection->data = s;
ctx->peer.connection->pool = s->connection->pool;
s->connection->read->handler = ngx_mail_auth_http_block_read;
ctx->peer.connection->read->handler = ngx_mail_auth_http_read_handler;
ctx->peer.connection->write->handler = ngx_mail_auth_http_write_handler;
```
#### **5.5.2. Vulnerability Details**

At the start of the lookup, the client's read handler is replaced with `ngx_mail_auth_http_block_read()`. If re-arming the read event fails, this handler function closes the auth connection, freeing the lookup pool. However, the client's write handler remains `ngx_mail_send()`, whose error path does not clean up the auth connection. The flaw is that this write handler *can* close the client connection while the auth connection still points to it.

#### **(1) Freeing the Client Session During the Lookup**

This path requires the client's write event to be registered beforehand. For example, if the client stops reading replies and fills the socket's send buffer, a send returns `EAGAIN`. `ngx_mail_send()` then registers the write event so it can retry.

If the login command and a TCP reset are processed in the same event-loop iteration, nginx handles the socket error reported by epoll by running the active read handler followed by the write handler. The read handler parses the login command, and then starts the auth lookup with a reply still queued in `s->out`.

`ngx_mail_send()` then tries to send the queued reply. The write fails on the reset socket, so it closes the client connection and destroys its pool.

```
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/mail/ngx_mail_handler.c#L812-L815
if (n == NGX_ERROR) {
    ngx_mail_close_connection(c);
    return;
}
// https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/mail/ngx_mail_handler.c#L966-L972
c->destroyed = 1;
pool = c->pool;
ngx_close_connection(c);
ngx_destroy_pool(pool);
```
The session `s` and its module context array were allocated from the now-freed pool. Importantly, the auth connection stays open, with its `data` field still pointing to `s`.

#### **(2) The Auth Connection Uses the Freed Session**

The next event (e.g. a connection-completion, response, or timeout) runs a handler on the auth connection. The read and write handlers both take the session pointer from the connection's `data` field and use it to obtain the lookup context, accessing `s->ctx` in the freed session. If attacker-controlled data reclaims that memory, `s->ctx` can point to a fake context. The authentication response path later calls `ctx->handler`, giving the attacker a control flow hijack.

To bypass ASLR, we leverage the stale auth connection's timeout. With some heap grooming, the timeout frees memory that now holds a partially received IMAP command from another connection. A later allocation reclaims that memory with heap pointers, and nginx echoes them back to us when it replies to the IMAP command.

To execute commands, we run the trigger again on a fresh worker. Just after the session is freed, an IMAP `LOGIN` with a controlled password reclaims it with a fake session. Its `s->ctx` points to a fake lookup context whose `handler` is `system()`. When the auth service replies, `ngx_mail_auth_http_read_handler()` follows the stale session and calls `system(s)`.

#### **5.5.3. Exploitability Validation**

| Item | Result | 
|---|---|
| Target | Official `nginx:1.31.8` image, stock configuration plus a `mail` block with IMAP, POP3 and SMTP | 
| Entry point | IMAP 143, POP3 110, and HTTP 80 served by the same workers | 
| Authentication | None. The auth service rejected every login. | 
| Result | Remote code execution with nginx worker privileges | 

## **6. Analysis of the Linux Kernel LPE Vulnerability**

The nginx vulnerabilities give an attacker code execution with worker privileges. Workers normally run with restricted permissions, so gaining full control of the host additonally requires a privilege escalation bug. We investigated the Linux kernel and found a zero-day vulnerability in its SCTP subsystem. Chaining it with one of the nginx vulnerabilities gave us root privileges on the host. This also worked when nginx ran inside a Docker container.

This section describes the cause of the SCTP vulnerability and our validation results. Until a kernel patch is available, we are withholding most of the details needed to reproduce or exploit it.

### **6.1. How SCTP Associations Work**

SCTP (Stream Control Transmission Protocol) is a transport-layer protocol, like TCP and UDP.

Like TCP, SCTP is connection-oriented. It calls a connection an *association*. An association can use multiple IP addresses at each endpoint, allowing it to continue over another path if one path fails.

### **6.2. Vulnerability Details**

The bug is in the SCTP send path. While a send operation is waiting, its association can be transferred to another socket. The waiting operation can then free the transferred association. Depending on what the other socket does, this leads to a use-after-free or a double free.

On a kernel built with KASAN, the kernel's memory error detector, the double free shows up like this:

```
BUG: KASAN: double-free in sctp_[...]
Free of addr ffff8880021b0880 by task t306/838
Call Trace:
 kfree+0x170/0x490
 sctp_[...]
 sctp_[...]
 sctp_[...]
Freed by task 836:
 kfree+0x23c/0x490
 sctp_[...]
 sctp_[...]
 sctp_[...]
 sctp_[...]
```
The bug was introduced in Linux v4.15 in 2018 and has remained in the kernel for more than eight years.

### **6.3. Exploitability Validation**

The use-after-free provides two primitives: a kernel memory disclosure that defeats kernel address space layout randomization (KASLR), and an arbitrary function call in the kernel. Together, they let us control kernel execution and escalate privileges. In our tests, an attacker already running code as an nginx worker could reliably gain root.

We also obtained a root shell on the host in a setup where nginx was running in a Docker container. On many Linux distributions, the SCTP module is installed by default and the kernel loads it automatically the first time a program opens an SCTP socket. Whether SCTP is reachable on a given host still depends on the kernel, the available modules, and the container's restrictions. Where it is reachable, the attacker can take over the host kernel. Since all containers on the host share that kernel, this gives the attacker control of the host and every container on it.

Until a kernel patch is available, hosts that do not use SCTP can block module loading by placing `install sctp /bin/false` in a `.conf` file under `/etc/modprobe.d/`. This only prevents loading through `modprobe`. It does not unload a module that is already loaded, and it does not disable SCTP compiled into the kernel.

## **Closing Remarks**

Thanks for reading this far. To recap, if you run nginx, update to 1.31.9 as soon as it’s out. If you can’t update right away, apply the mitigations described in Section 3.3. They block the attack paths we know about, but they aren’t a substitute for a patch. Until a kernel fix is available, also block the SCTP module on hosts that don’t need it, as described in Section 6.3.

Be careful when checking whether a server is patched. Linux distributions often backport fixes without changing the version that nginx -v shows. Check the full package version against your distribution’s security advisory instead.

We thank F5 and the nginx team for their cooperation during disclosure and patch validation. We’ll post updates and answers to common questions about nginx2root at [<u>nginx2root.com</u>](https://nginx2root.com).

CVE-2026-123007 went unnoticed in nginx for more than ten years, and the SCTP bug has been in the Linux kernel since 2018. Both projects run almost everywhere and have had years of security review, yet these bugs survived until a fully automated Xint scan found them. If you’d like to see what Xint finds in your own code, get in touch.

## About Xint

Xint ([xint.io](http://xint.io)) is the award-winning autonomous pentesting platform built by the most decorated team of white hat offensive security researchers in the world. Xint offers both black-box as well as white-box pentesting with results, on average, in 24 hours or less, including: full trigger conditions and step-by-step reproduction pathing, exploit impacts, and suggested remediations so teams can quickly triage and patch the most critical vulnerabilities. Xint is working with organizations with the highest defensive security needs, including The US Government’s Defense Advanced Research Projects Agency (DARPA), Microsoft, Google, Okta, Samsung, and Kia. Xint is a member of Anthropic’s Cyber Verification Program, OpenAI’s Daybreak cybersecurity program, and is a founding member of Project Canopy, a public interest initiative disseminating AI-powered preemptive defense capabilities to organizations ranging from major companies across Asia and Europe to civilian infrastructure and open-source software. Learn more at <u>xint.io</u>
