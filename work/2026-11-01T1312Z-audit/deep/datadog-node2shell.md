# extract: served via trafilatura-direct
---
title: "Node2Shell: Reproducing CVE-2026-111497 in the Node.js Brotli decoder | Datadog Security Labs"
author: Sebastian Obregoso
url: https://securitylabs.datadoghq.com/articles/node2shell-cve-2026-111497-nodejs-brotli-decoder/
hostname: datadoghq.com
description: We reproduced CVE-2026-111497, an out-of-bounds write in the Brotli decoder bundled with Node.js and other runtimes, and explain how to detect and remediate it.
sitename: Datadoghq
date: "2026-10-29"
fingerprint: "3c1d950529260690"
---
## [Key points and observations](https://securitylabs.datadoghq.com#key-points-and-observations)

- On October 21, 2026, Node.js released fixes for [CVE-2026-111497](https://nvd.nist.gov/vuln/detail/CVE-2026-111497), an out-of-bounds write in its bundled Brotli decoder. The upstream flaw sits in the Google Brotli C library, so the blast radius reaches Python, Bun, .NET, Java brotli4j, Envoy, and Istio. Every affected runtime now has a fix available.
- We reproduced the flaw on the official Node.js 24.22.0 image and verified that the patched build rejects the same bytes.
- Capturing an application-level trace is difficult because the process continues running despite memory corruption.
- Only patching fixes this vulnerability. The application process decodes the data, so neither the web server nor a web application firewall (WAF) ever sees the malicious content. An edge rule that rejects Brotli-compressed request bodies is a useful tripwire and nothing more.

## [What happened](https://securitylabs.datadoghq.com#what-happened)

On October 21, 2026, Node.js [released security updates](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) for CVE-2026-111497, an out-of-bounds write in the Brotli decoder. The CVE record gives the flaw a Common Vulnerability Scoring System (CVSS) v4.0 score of 9.2, or Critical, while Node.js rates its severity as High. Node.js 22.23.4, 24.22.1, and 26.12.1 contain the fix, and end-of-life release lines carry the same vulnerable decoder but have no patch.

What looked like a Node.js problem on day one turned out to be far broader. Most runtimes embed the upstream Google Brotli C library, where the bug lives. Over the following week many consumers of that decoder shipped its own advisory:

| Product | Affected | First fixed release | 
|---|---|---|
| Node.js 22, 24, and 26 | Before 22.23.4, 24.22.1, and 26.12.1 | 22.23.4, 24.22.1, 26.12.1 | 
| Google Brotli | 1.0.3 through 1.0.9, 1.1.0, and 1.2.0 | 1.0.10, 1.1.1, 1.2.1 | 
| Python Brotli and brotlicffi | 1.2.0 and earlier | 1.2.1 and 1.2.1.0 | 
| Bun | 1.0.21 through 1.4.3 | 1.4.4 | 
| Java brotli4j | 1.23.0 and earlier | 1.24.0 | 
| .NET 8, 9, and 10 | Before the October 25, 2026 out-of-band update | 8.0.33, 9.0.22, 10.0.14 | 
| Envoy and Istio | All releases before the first fix in each supported branch | Envoy: 1.36.12, 1.37.8, 1.38.6, 1.39.3, 1.40.0; Istio: 1.29.9, 1.30.6, 1.31.2 (first fixed in each branch) | 

Two details deserve special attention. Java's brotli4j bundles its own native Brotli build inside its jars, so patching the operating system's libbrotli does not fix it. Bun executables built with bun `build \--compile` embed the runtime and stay vulnerable until they are rebuilt.

Before the disclosure, [Imperva demonstrated](https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/) code execution on the official Node.js 24.22.0 Linux ARM64 image. Their exploit needed several attempts and was not released. A public proof of concept appeared on October 22, 2026. On standard builds it produces a crash and a limited memory read. As of October 29, 2026, there have been confirmed in-the-wild exploitation, and CISA's known exploited vulnerabilities catalog now [lists the CVE](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-111497).

## [How to know if you're affected](https://securitylabs.datadoghq.com#how-to-know-if-youre-affected)

A service is exposed when it decompresses Brotli data that an attacker controls, which comes through two common paths. A few additional considerations apply to both.

### [Outbound requests (the quiet path)](https://securitylabs.datadoghq.com#outbound-requests-the-quiet-path)

Outbound requests are the harder path to see. Node.js's built-in `fetch()` decodes a `Content-Encoding: br` response automatically, whether or not the request asked for Brotli. The `axios`, `got`, and `node-fetch` clients advertise and decode Brotli by default. Any feature that fetches URLs supplied by users, such as webhooks, link previews, and feed readers, enables an attacker to force the encoding selection server side since the attacker controls the response headers, and `fetch()` decodes a body labeled `br` even when the application explicitly forces `Accept-Encoding: identity`.

In our testing, no exception surfaced at runtime: one crafted stream completed with an empty body and an HTTP 200, and the only visible signals were CPU usage and, under concurrency, a starved threadpool that still answered health checks.

The same holds outside Node.js: Python HTTP clients decode Brotli responses automatically whenever `Brotli` or `brotlicffi` is installed, even if application code never imports the package.

### [Inbound requests (the visible path)](https://securitylabs.datadoghq.com#inbound-requests-the-visible-path)

Inbound attacks are easier to observe. A compressed request body is a recognizable attack surface, your reverse proxy or WAF can see the `Content-Encoding: br` header, and the framework parser is a known place to audit. Express 5 and body-parser 2.x accept Brotli-compressed request bodies by default in their JSON, raw, text, and URL-encoded parsers, and Koa and NestJS inherit the behavior. Express 4 rejects those bodies with an HTTP 415, and a bare Node.js HTTP server does not decompress anything. Parsers mounted before authentication expose the decoder to unauthenticated requests.

### [Other considerations](https://securitylabs.datadoghq.com#other-considerations)

Both paths share a versioning trap: `process.versions.brotli` still reports 1.2.0 on the patched Node.js 24.22.1, because the cherry-picked fix does not bump the embedded version string. `process.version` is reliable only for official distributions from [nodejs.org](http://nodejs.org).

If you cannot patch immediately, set `inflate: false` on Express 5 and body-parser 2.x parsers, or reject `Content-Encoding: br` at the reverse proxy. These measures only mitigate the risk, as patching is the only complete solution. These mitigations could also break the functionality as they reject all compressed request bodies, do nothing for the outbound path, and break compressed bodies sent by legitimate clients.

## [How the vulnerability works](https://securitylabs.datadoghq.com#how-the-vulnerability-works)

A Brotli stream is divided into blocks, and the decoder moves to a new block only when the current block's length budget runs out. A 23 MB stream of otherwise ordinary commands drains that budget while producing no output, and its closing commands request a block switch that the format forbids. These steps are where the attacker does the proper setup to exploit the bug.

In the next stage, we see the impact of the vulnerability. In Brotli 1.2.0, `DecodeBlockTypeAndLength()` returns a boolean, and it answers two different questions with the same "false" value: "this stream is malformed" and "I need more input". Callers cannot tell the two apart, and on the decoder's fast path the return value is dropped entirely.

The two arms then diverge. The first path is an overflow where the decoder parks the unconsumed bytes in a small internal buffer while it waits for more input. The copy has no bound check, so bytes past the end of the buffer land in adjacent decoder state. The write happens inside a single heap allocation, so the tooling built to catch memory corruption never sees it, and the process keeps running. The other path is that it keeps spinning. The decoder retries the forbidden switch in a loop, which pins a CPU core inside a single call that never returns: a one-request denial of service.

## [From memory corruption to code execution](https://securitylabs.datadoghq.com#from-memory-corruption-to-code-execution)

In this case, memory corruption has impactful consequences. The corrupted decoder state controls where the decoder reads from and writes to next, so a crafted stream can redirect both operations.

This gives an attacker two primitives:

- **A repeatable read of heap memory** that leaves through the decompressed response.
- **A redirected write.** In our lab, we aimed it at an unmapped page and produced a deterministic crash.

Both primitives are real. The read primitive is the most operationally interesting, because heap bytes returning over the wire are the first step of a staged attack.

Three obstacles stand between these primitives and a shell:

1. **The addresses move.** The heap layout that the corruption targets is randomized and changes between requests, so what one request leaks, the next request can’t reliably use.
2. **The corruption bytes are also the decoder's input.** The decoder consumes the bytes that steer the corruption again as it continues, so the values an attacker needs are constrained by the values the decoder will accept. This is the deepest structural obstacle we found.
3. **A managed runtime stands in the way.** Between the corrupted C state and control flow sits the machinery of a language runtime with its own allocator, its own compiled code, and its own defenses, none of which the original C library was designed around.

After measuring all three obstacles, we assess that the flaw is exploitable and that the gap between these primitives and reliable code execution is engineering effort. This matches Imperva's report of successful execution after several attempts on the official Node.js 24.22.0 image.

## [How the patch addresses the flaw](https://securitylabs.datadoghq.com#how-the-patch-addresses-the-flaw)

The patch is small and precise. The block-switch helper now returns a real error code, and both code paths treat a failed check as a hard stop instead of a request for more input. It rejects a crafted stream with a format error (`-17`) before anything is written to the decoder's state.

The release timeline is the troubling part. The fix was committed to the upstream Brotli repository on February 27, 2026, but the fixed library releases did not ship until October 21, 2026. For eight months, anyone who downloaded Brotli, or a runtime that embeds it, received the vulnerable version even though the corrected code sat in the public repository. The release also ships without a regression test or a changelog entry for this fix.

## [How to detect exploitation](https://securitylabs.datadoghq.com#how-to-detect-exploitation)

This CVE involves no attacker-controlled infrastructure, so there are no conventional indicators. Detection rests on behavioral signals, and no single signal is conclusive. Correlate across three layers.

#### [**Decoder error signals**](https://securitylabs.datadoghq.com#decoder-error-signals)

The vulnerable and patched builds respond differently to the same malicious bytes. Both responses appear in application logs and APM error spans and the error you see depends on whether the build is patched. On a vulnerable build, Node.js returns `Z_BUF_ERROR` with the message "unexpected end of file". On a patched build, Node.js returns `ERR__ERROR_FORMAT_BLOCK_SWITCH`, and Python returns "brotli: decoder is unhealthy". The vulnerable signal also appears for benign truncated input so you have to still look a little closer and differentiate the benign truncated input vs real attacks.

#### [**Process signals**](https://securitylabs.datadoghq.com#process-signals)

A worker that exits with signal 139 (SIGSEGV) right after a Brotli transfer is a crash attempt, and a process pinned at 100% CPU inside a decompression call is the spin arm. Correlate on workload identity (the container, pod, or service) and not the process ID, because the process that crashed is gone and a successful attempt may not crash at all. The strongest signal is behavioral: a shell or new outbound connections from the same workload.

#### [**The disclosure channel**](https://securitylabs.datadoghq.com#the-disclosure-channel)

Decompressed output that contains bytes the client never sent is the read primitive in action. Investigate any such output immediately. Because the leaked heap memory leaves through the decompressed response, start by listing the endpoints that return or reflect decompressed content back to the caller, such as echo, preview, conversion, or proxy features.

#### [**What does not work**](https://securitylabs.datadoghq.com#what-does-not-work)

- Payload byte signatures, because the attacker-controlled parts of the stream change per target and the exploit is the decode process itself, not the decompressed content.
- Content matching at the WAF, because the web server forwards compressed bytes and never decodes them.
- Body-size limits, because the tested middleware counts decompressed bytes, so the 23 MB compressed trigger still reaches the decoder.

## [How Datadog can help](https://securitylabs.datadoghq.com#how-datadog-can-help)

[Datadog Cloud Security Management](https://docs.datadoghq.com/security/cloud_security_management/vulnerabilities/) tracks [CVE-2026-111497](https://app.datadoghq.com/security/csm/vm?query=%40status%3Aopen%20%28%40advisory.cve%3ACVE-2026-111497%20OR%20%40advisory.id%3ADDSA-261023-132226%20OR%20%40advisory.aliases%3ACVE-2026-111497%29) and the related vendor advisories as vulnerability findings on hosts and container images, so your patching status lives in one place.

[Datadog Code Security](https://docs.datadoghq.com/security/code_security/) reports the [vulnerable services](https://app.datadoghq.com/security/code-security/sca?query=%40status%3Aopen%20%28%40advisory.cve%3ACVE-2026-111497%20OR%20%40advisory.id%3ADDSA-261023-132226%29) that ship dependency inventories. Its [library inventory](https://app.datadoghq.com/security/code-security/inventory/libraries) identifies which services to prioritize: those running Express 5, body-parser 2.x, or Koa parsers, and those using HTTP clients that auto-decode Brotli.

[Datadog Application Performance Monitoring (APM)](https://docs.datadoghq.com/tracing/) helps you hunt for attempts. This query requires capturing `Content-Encoding`, which is not set by default in Node.js spans, so make sure to check how the language tracer you are using behaves. For example in Node.js it can be enabled by including `content-encoding` in `DD_TRACE_HEADER_TAGS`. Pivot on the services that accept `Content-Encoding: br` request bodies using [this query](https://app.datadoghq.com/apm/traces?query=%40_top_level%3A1%20%40language%3A%28nodejs%20OR%20node%20OR%20javascript%29%20%40http.request.headers.content-encoding%3Abr&agg_m=count&agg_m_source=base&agg_t=count&cols=service%2Cresource_name%2C%40duration%2C%40http.method%2C%40http.status_code%2C%40_span.count%2C%40_duration.by_service&fromUser=false&graphType=span_list&historicalData=false&messageDisplay=inline&query_translation_version=v0&shouldShowLegend=true&sort=desc&spanType=service-entry&storage=driveline&trace_group_by_from=a&traceQuery=&view=spans&viz=stream&start=1793289067996&end=1793289967996&paused=false), and review services that fetch user-supplied URLs. Decoder failures surface as APM error spans correlated with the request and the client address. The process telemetry that the Datadog Agent collects shows a crashed attempt as a worker restart with exit code 139.

[Datadog Workload Protection](https://docs.datadoghq.com/security/workload_protection/) includes coverage through the CVE-2026-111497 Node2Shell Exploit Content Pack. This pack includes a new security policy with three Agent rules that cover post-exploitation that surfaces a [CVE-2026-111497 Node2Shell exploitation detected](https://docs.datadoghq.com/security/default_rules/def-000-538/) signal.

[Datadog Cloud SIEM](https://www.datadoghq.com/product/cloud-siem/) includes two detections that identify command execution associated with Node2Shell exploitation:

- [Shell spawned by web server](https://docs.datadoghq.com/security/default_rules/def-000-9h1/) detects shells, download utilities, and reconnaissance commands launched by web servers or web processes. It uses process activity events with parent process information.
- [Shell spawned by web process](https://docs.datadoghq.com/security/default_rules/def-000-gn1/) uses Linux auditd logs to detect shells or download utilities executed in a web server context.

## [Conclusion](https://securitylabs.datadoghq.com#conclusion)

[CVE-2026-111497](https://nvd.nist.gov/vuln/detail/CVE-2026-111497) shows how a single unchecked return value in a widely shared C library can ripple across nearly every major runtime. Because the decoder runs inside the application's own process, the flaw sidesteps the defenses most teams rely on.  The eight months between the upstream fix and its release are a reminder that a fix in a public repository protects no one until it ships.

Exploitation has been confirmed, which further proves the primitives are real and the path to code execution is a matter of effort. Patch to Node.js 22.23.4, 24.22.1, or 26.12.1 or your vendor's fixed package, rebuild container images, restart every process, and inventory the other Brotli consumers in your environment.
