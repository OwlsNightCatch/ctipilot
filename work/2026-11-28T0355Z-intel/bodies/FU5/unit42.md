---
title: "NGINX HTTP/2 Use-After-Free: CVE-2026-123633"
author: Bon Berry
url: https://unit42.paloaltonetworks.com/cve-2026-123633-nginx-http2-vulnerability/
hostname: paloaltonetworks.com
description: Technical analysis of CVE-2026-123633, an NGINX HTTP/2 use-after-free flaw, with details on affected versions, sanitizer tests, and patch guidance.
sitename: Unit 42
date: "2026-11-24"
fingerprint: a53689497ea0c583
language: en
image: https://unit42.paloaltonetworks.com/wp-content/uploads/2026/11/06_Security-Technology_Category_1920x900.jpg
pagetype: article
filedate: "2026-11-28"
---
## Executive Summary

[CVE-2026-123633](https://www.cve.org/CVERecord?id=CVE-2026-123633) is a [use-after-free](https://cwe.mitre.org/data/definitions/416.html) vulnerability in NGINX HTTP/2 that may let an unauthenticated attacker cause a denial of service. In the CVE record, F5 says code execution may be possible when address space layout randomization (ASLR) is disabled or bypassed.

CVE-2026-123633 affects NGINX servers that accept HTTP/2 client connections and proxy requests to a backend when free worker connections run low. A fragmented request can leave an active connection marked reusable. Under connection pressure, NGINX can close that connection and free memory the active request still uses.

F5's CVE record scores the issue 9.2 Critical under CVSS 4.0. The [NGINX security advisories page](https://nginx.org/en/security_advisories.html) labels the issue medium and lists versions 1.19.7 through 1.30.6 and 1.31.0 through 1.31.8 as affected. F5 credits [memN0ps](https://github.com/memn0ps) (Palo Alto Networks Unit 42) among the reporters.

NGINX 1.30.7 on the stable branch and 1.31.9 on the mainline branch contain the fix. F5 [also lists affected NGINX Plus releases](https://my.f5.com/manage/s/article/K000163928).

Administrators should review HTTP/2 reverse-proxy exposure and upgrade to a fixed NGINX release or a vendor package containing the CVE-2026-123633 fix.

Palo Alto Networks customers are better protected from the threats discussed above through the following products and services:

Organizations can access tailored adversary intelligence, direct analyst consultations, and specialized exposure tracking through [Unit 42 Threat Intel Services](https://www.paloaltonetworks.com/unit42/threat-intelligence) and its [Deep and Dark Web Service](https://www.paloaltonetworks.com/resources/datasheets/unit-42-deep-and-dark-web-service).

If you think you might have been compromised or have an urgent matter, contact the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html).

| **Related Unit 42 Topics** | **[HTTP](https://unit42.paloaltonetworks.com/tag/http/), [DNS](https://unit42.paloaltonetworks.com/tag/dns/), [Threat Detection](https://unit42.paloaltonetworks.com/tag/threat-detection/)** | 

## Background

While researching NGINX, I independently found the HTTP/2 connection-state defect now tracked as CVE-2026-123633.

An unauthenticated client can send a fragmented HTTP/2 request that leaves an active connection marked as reusable. When the server resolves a hostname during the request and free connection slots run low, NGINX can reclaim that connection mid-request and free memory its DNS resolver is still using.

I reproduced the use-after-free with [AddressSanitizer (ASan)](https://clang.llvm.org/docs/AddressSanitizer.html) on builds of unmodified NGINX 1.31.7 and 1.31.8 source. The NGINX [security advisories page](https://nginx.org/en/security_advisories.html) lists 1.19.7 through 1.30.6 and 1.31.0 through 1.31.8 as affected and 1.30.7 and 1.31.9 as fixed releases.

I reported the HTTP/2 use-after-free privately to F5. F5's CVE record scores it 9.2 Critical under CVSS 4.0 and 8.1 High under CVSS 3.1. The NGINX security advisories page labels it Medium.

In my ASan test on a Debian guest, ASan stopped NGINX at the first read from freed DNS lookup memory.

The resolver path in my test stems from the HTTP/2 connection bug tracked as CVE-2026-123633. [CVE-2026-123634](https://nvd.nist.gov/vuln/detail/cve-2026-123634) is a separate DNS resolver vulnerability fixed in the same release.

I also found a memory disclosure vulnerability that leaked a libc pointer. I used the address to calculate the libc base and work around ASLR when chaining the disclosure with CVE-2026-123633. I reported this additional bug to F5 as a separate issue. From an attacker VM, I achieved pre-authentication remote code execution on a target VM as the non-root NGINX worker. The chain required a non-default NGINX configuration, and some attempts did not open a shell.

F5 assessed the memory disclosure as a behavior limited to a non-typical configuration and has not assigned it a CVE at the time of writing, so I am leaving out its details and the exploit steps.

## How the Connection State Defect Works

NGINX marks a connection reusable when it can close that connection under pressure. Stream creation should clear the reusable mark once a request starts, but [ngx\_http\_v2\_create\_stream()](https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2.c#L3063-L3200) leaves it set in affected releases.

When a client sends only part of an HTTP/2 HEADERS frame header, [ngx\_http\_v2\_handle\_connection()](https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2.c#L621-L697) marks the connection reusable and returns early. The code below shows that decision:

| 1 2 3 4 5 | ngx\_reusable\_connection(c, 1); if (h2c->state.incomplete) { return; } | 

The reusable mark lets NGINX reclaim connections stalled on partial frames before they exhaust the worker's slots.

The client then sends the remaining header bytes. ngx\_http\_v2\_create\_stream() builds a live stream and increments the active stream counter, but returns with the reusable mark still set:

| 1 2 3 4 5 6 7 | h2c->processing++; if (h2c->connection->read->timer\_set) { ngx\_del\_timer(h2c->connection->read); } return stream; | 

NGINX now has a live request on a connection that its cleanup logic still considers reusable.

The 1.30.7 and 1.31.9 fixes clear the reusable mark at stream creation with ngx\_reusable\_connection(h2c->connection, 0). Figure 1 shows the sequence in affected releases:

- A partial frame header marks the connection reusable
- NGINX creates a stream with the mark still set
- A later socket allocation drains the live connection

## Reaching the Resolver Use-After-Free

The stale reusable mark lets NGINX reclaim a live connection when it needs a free slot. In my test, a request-time DNS lookup opened a new socket and triggered the drain.

My test used an HTTP/2 proxy route with a variable upstream. The variable evaluated to a hostname that was neither a literal IP address nor a configured upstream group, so NGINX looked it up during the request. The lookup also had to open a new resolver UDP socket.

The worker opens a new UDP socket only if it has none for the selected nameserver. Cached answers and in-flight lookups also skip the socket-allocation drain I tested.

Opening the DNS socket needs a connection slot, so [ngx\_get\_connection()](https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/core/ngx_connection.c#L1206-L1269) runs a drain check first. [ngx\_drain\_connections()](https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/core/ngx_connection.c#L1404-L1458) acts once free slots fall to one sixteenth of worker\_connections or below while at least one reusable connection exists. The drain function then selects entries from the tail of the reusable queue, sets each connection's close flag, and calls its read handler:

| 1 2 | c->close = 1; c->read->handler(c->read); | 

My test client closed its socket with zero linger after completing the frame, leaving NGINX with an active request on a reset connection. When connection pressure triggered the drain, the HTTP/2 read handler tried to send GOAWAY on that socket.

A successful write would have left the request running, but the write failed with Connection reset by peer, so NGINX finalized the connection and request. The ASan free stack passes through [ngx\_http\_upstream\_check\_broken\_connection()](https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/ngx_http_upstream.c#L1371-L1410).

Request cleanup reaches [ngx\_resolve\_name\_done()](https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/core/ngx_resolver.c#L514-L602), which frees the resolver state while the original lookup still holds a pointer to it.

In [ngx\_resolve\_name\_locked()](https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/core/ngx_resolver.c#L874-L888), the DNS send runs before timeout setup. The send can drain the connection and free ctx. When the send returns, timeout setup uses the stale pointer, as the code below shows:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | if (ngx\_resolver\_send\_query(r, rn) != NGX\_OK) { /\* immediately retry once on failure \*/ rn->last\_connection++; if (rn->last\_connection == r->connections.nelts) { rn->last\_connection = 0; } (void) ngx\_resolver\_send\_query(r, rn); } if (ngx\_resolver\_set\_timeout(r, ctx) != NGX\_OK) { goto failed; } | 

If the drain freed ctx, [ngx\_resolver\_set\_timeout()](https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/core/ngx_resolver.c#L4072-L4093) reads from it:

| 1 2 3 | if (ctx->event \|\| ctx->timeout == 0) { return NGX\_OK; } | 

ASan reported that NGINX read memory from a freed DNS lookup context. The free path ran through ngx\_drain\_connections(), [ngx\_http\_v2\_finalize\_connection()](https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/v2/ngx_http_v2.c#L4955-L5040), [ngx\_http\_upstream\_finalize\_request()](https://github.com/nginx/nginx/blob/140aa942711868a8daeb95810bc9a81f272ada72/src/http/ngx_http_upstream.c#L4784-L4955) and ngx\_resolve\_name\_done(). Source review showed that, if execution continues past the reported read, ngx\_resolver\_set\_timeout() can also write ctx->event and ctx->ident through that stale pointer.

In the run where ASan reported the read, I split the 9-byte HEADERS frame header after 5 bytes. For the control, I sent the full frame header first and then the HPACK block. NGINX sent a DNS query and kept running. Figure 2 follows the calls from socket allocation to the use-after-free.

## Test Setup and Limits

I ran the ASan test in an isolated Debian 13 guest. NGINX was built from official 1.31.7 and 1.31.8 source with Clang 19.1.7, HTTP/2, ASan and UndefinedBehaviorSanitizer. I sent the HTTP/2 requests over the guest's loopback interface.

For the 1.31.8 run, I set worker\_connections to 16 and opened 13 filler connections that NGINX had not marked reusable. Table 1 shows the sanitizer results alongside the released-source review.

| **Test** | **Builds** | **Result** | 
| ASan | 1.31.7, 1.31.8 (tested before the HTTP/2 fix) | Read from freed resolver state during request-time DNS setup | 
| Source review | Released NGINX 1.30.7 and 1.31.9 source | Clears the reusable mark when NGINX creates an HTTP/2 stream | 

Table 1. HTTP/2 use-after-free tests and source review.

### Tested Conditions

Table 2 lists the conditions I used in the 1.31.8 ASan test.

| **Tested Path** | **Key Conditions** | 
| Resolver socket | Split HEADERS frame header, worker\_connections set to 16, 13 filler connections, a variable upstream hostname, a new resolver UDP socket and an abortive client close | 

Table 2. Conditions used in the 1.31.8 ASan test.

### Limits

A source build includes the HTTP/2 module only when configured with --with-http\_v2\_module. Distribution packages commonly enable it.

The ASan evidence in this article comes from builds of 1.31.7 and 1.31.8 over loopback. The 1.31.8 test configuration set worker\_connections to 16 instead of the [documented default of 512](https://nginx.org/en/docs/ngx_core_module.html#worker_connections), and ran NGINX with master\_process off. The sanitizer aborted that single process. The [public fix commit](https://github.com/nginx/nginx/commit/2df48a501d0fb8212b7d39dffeeff5876332ba59) also names upstream connection setup as a drain trigger.

## Two-VM Demonstration

The two-VM demonstration combined CVE-2026-123633 with the separate memory disclosure mentioned in the Background section. The target ran NGINX 1.31.8 with a root master and a www-data worker under a non-default configuration. Figure 3 records the running processes, version, loaded configuration path and listener.

The first attempt from the attacker VM recovered a libc address but did not open a shell; the second opened an interactive shell as www-data. The shell's hostname, IP address and boot ID match the target screenshot. Figure 4 previews the accompanying recording, which shows the same session with waiting periods sped up.

Video 1 shows the session:

Video 1. Demonstration of the attacker VM session and the interactive shell opened on the target.

## Detection and Hunting

In the ASan test, NGINX logged a connection-drain warning before the sanitizer aborted the process. The warning can also appear under ordinary connection pressure, while a worker exit can have unrelated causes. A release build may keep running after reading freed memory. Table 3 lists investigation leads for HTTP/2 reverse proxies.

| **Signal** | **What I Saw in Testing** | **What to Check** | 
| Unexpected NGINX process exit | ASan aborted the single-process NGINX test after NGINX read freed memory. | Investigate unexpected worker exits in production near HTTP/2 requests and connection pressure. A worker exit on its own is weak evidence of exploitation. | 
| Connection pressure with request-time DNS | NGINX logged "16 worker\_connections are not enough, reusing connections" at warn level during the ASan test. | Correlate the warning with resolver traffic and connection pressure on routes that resolve at request time. The warning and DNS traffic can also occur under ordinary load. | 

Table 3. Signals to use in detection and hunting.

The warning in Table 3 is logged at most once per second per worker, so one line can cover several drain calls. Because NGINX defaults to the error log level (which omits warnings), configure error\_log at the warn level (or a level that captures more detail, such as notice or info), then correlate the warning with traffic and worker state.

## Exposure Review

[CVE-2026-123633](https://www.cve.org/CVERecord?id=CVE-2026-123633) describes a use-after-free in HTTP/2 reverse proxies that are running low on worker connections. The path I reproduced used a variable proxy\_pass hostname, a configured resolver and a new UDP socket. F5's CVE description covers a broader set of HTTP/2 reverse proxies.

Check the running configuration. A master process can select another file with -c, so check its command line before assuming that the packaged path is the live one. The command nginx -T prints the on-disk configuration, which can still differ from what the running workers loaded.

I only tested proxy\_pass. Operators should also review variable targets in:

- grpc\_pass
- fastcgi\_pass
- uwsgi\_pass
- scgi\_pass

For a matching route, check the running build and how close the worker gets to its connection limit. I tested one DNS socket route, but upstream connection setup also allocates through ngx\_get\_connection(), so static upstream routes still need review.

## Mitigations

NGINX 1.30.7 and 1.31.9 fix the HTTP/2 issue. No workaround is listed in the CVE-2026-123633 record. If an upgrade must wait, the following changes could reduce exposure:

- Where the service allows it, disable HTTP/2 on exposed listeners. Check every relevant listen ... http2 parameter and, on NGINX 1.25.1 or later, any http2 on; setting in the http or server context. Either setting can keep HTTP/2 enabled. Disabling HTTP/2 can break gRPC clients and may increase connection use if other traffic falls back to HTTP/1.1. If HTTP/2 stays enabled on other listeners, the extra HTTP/1.1 connections can push the same worker closer to its worker\_connections limit.
- Raising worker\_connections gives the worker more headroom under the same traffic, but an attacker can still exhaust the extra slots and the connection-state bug remains.

Test each change before deployment. After upgrading, confirm the running worker uses a binary containing the CVE-2026-123633 fix. A configuration reload (nginx -s reload) keeps the old binary running in memory, so perform a full restart or live binary upgrade.

## Conclusion

The defect starts when an HTTP/2 connection stays marked reusable after a request begins. In my test, opening a DNS socket under connection pressure drained that live connection and freed resolver state that the request still used. ASan reported that NGINX read memory after it had been freed.

Defenders should identify affected HTTP/2 reverse proxies, look for worker exits around connection pressure, and install a fixed NGINX release or vendor backport. My resolver test shows one way to reach the use-after-free. F5's description covers HTTP/2 reverse proxies more broadly.

## Palo Alto Networks Protection and Mitigation

Palo Alto Networks customers are better protected from the threats discussed above through the following products:

- [Cortex XDR](https://docs-cortex.paloaltonetworks.com/p/XDR) and [XSIAM](https://docs-cortex.paloaltonetworks.com/p/XSIAM) are designed to detect and block post-exploitation activity, including server and process exploitation, by leveraging Behavioral Threat Protection, machine learning-driven Local Analysis, and cloud-based malware inspection to prevent the execution of both known and unknown threats.
- [Cortex Agentic Endpoint Security](https://www.koi.ai/product/endpoint) is designed to help discover every AI artifact and AI agent's activity across the agentic endpoint, assess its risk, enforce prevention and runtime controls and remediate violations.

Organizations can access tailored adversary intelligence, direct analyst consultations, and specialized exposure tracking through [Unit 42 Threat Intel Services](https://www.paloaltonetworks.com/unit42/threat-intelligence) and its [Deep and Dark Web Service](https://www.paloaltonetworks.com/resources/datasheets/unit-42-deep-and-dark-web-service).

If you think you may have been compromised or have an urgent matter, get in touch with the [Unit 42 Incident Response team](https://start.paloaltonetworks.com/contact-unit42.html) or call:

- North America: Toll Free: +1 (866) 486-4842 (866.4.UNIT42)
- UK: +44.20.3743.3660
- Europe and Middle East: +31.20.299.3130
- Asia: +65.6983.8730
- Japan: +81.50.1790.0200
- Australia: +61.2.4062.7950
- India: 000 800 050 45107
- South Korea: +82.080.467.8774

Palo Alto Networks has shared these findings with our fellow Cyber Threat Alliance (CTA) members. CTA members use this intelligence to rapidly deploy protections to their customers and to systematically disrupt malicious cyber actors. Learn more about the [Cyber Threat Alliance](https://www.cyberthreatalliance.org).

## Disclosure Timeline

| **Date** | **Event** | 
| Oct. 16, 2026 | HTTP/2 reusable connection defect documented | 
| Oct. 16, 2026 | Resolver use-after-free reproduced with ASan; sending all nine frame-header bytes first left NGINX running | 
| Nov. 1, 2026 | Use-after-free reported privately to F5 through its coordinated disclosure process | 
| Nov. 18, 2026 | NGINX 1.30.7 and 1.31.9 released with the HTTP/2 fix | 
| Nov. 18, 2026 | F5 published CVE-2026-123633 for the HTTP/2 issue | 

F5 credits memN0ps (Palo Alto Networks Unit 42) alongside Albert Ebb of Metnir (metnir.com), Nir Ohfeld at Wiz Research, Xint.io, Hrithik Ram (hmm\_hmm), and Zenneth (randomguy6407) in the CVE-2026-123633 record. Research dates in the timeline come from my notes; release dates come from the NGINX changelog.

**Vendor impact statement for CVE-2026-123633: F5 says the HTTP/2 use-after-free may cause a denial of service on an affected NGINX system when connection slots run low. F5 also says code execution may be possible if ASLR is disabled or bypassed. The CVE-2026-123633 record has the full vendor description.**

## Indicators of Compromise

*This research produced no confirmed indicators of compromise. Treat the items below as leads for investigating CVE-2026-123633 alongside the running build and HTTP/2 traffic.* 

- Unexpected shell processes running as the NGINX worker account when investigating suspected code execution
- Unexpected NGINX process termination near HTTP/2 traffic and connection pressure
- Connection-drain warnings containing "worker\_connections are not enough, reusing connections"; check the running worker\_connections value when interpreting them
