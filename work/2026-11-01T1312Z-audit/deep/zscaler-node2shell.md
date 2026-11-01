# extract: served via trafilatura-direct
---
title: "CVE-2026-111497: Node2Shell / HTTP2Shell | ThreatLabz"
author: Atinderpal Singh; Amir Moin
url: https://www.zscaler.com/blogs/security-research/cve-2026-111497-node2shell-http2shell-vulnerability-may-allow-rce
hostname: zscaler.com
description: ThreatLabz examines CVE-2026-111497 (Node2Shell / HTTP2Shell), observed reconnaissance and exploitation attempts, and Zscaler coverage.
sitename: Zscaler, Inc.
date: "2026-10-28"
fingerprint: "340992c9f871bf80"
---
Zscaler Blog

Get the latest Zscaler blog updates in your inbox

# CVE-2026-111497: Node2Shell / HTTP2Shell Vulnerability May Allow RCE

## Introduction

On October 21, 2026, the Node.js project disclosed CVE-2026-111497, an out-of-bounds write vulnerability in Google’s Brotli decoder used by Node.js and other software. The vulnerability is also known as *Node2Shell* and more recently as *HTTP2Shell*. The CVE score, filed by Google as the numbering authority, is 9.2 (Critical) on CVSS 4.0. The flaw can be triggered when a vulnerable process decompresses attacker-controlled Brotli data. Successful exploitation may result in process crashes, disclosure of process memory, or remote code execution (RCE). Imperva [<u>reported</u>](https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/) demonstrating code execution in fresh containers running the official Node.js 24.22.0 Linux arm64 image, with multiple attempts required in its test environment.

The vulnerable Brotli decoder may be present in a range of runtimes, libraries, and software packages, including Node.js, Bun, Python Brotli bindings, .NET, Envoy Proxy, Istio, Java brotli4j, libbrotli, curl/libcurl through Brotli dependencies, and Linux distribution packages. Applications may be exposed if they decompress attacker-controlled data using a vulnerable decoder. The vulnerability may be reachable through both inbound and outbound traffic paths. A malicious client could send a crafted request with Content-Encoding: br to a vulnerable server-side component that performs Brotli request decompression. Conversely, a malicious or compromised server could return a crafted Brotli-compressed response to a vulnerable client application that automatically decodes Brotli responses.

ThreatLabz has observed reconnaissance and exploitation attempts targeting this vulnerability through Zscaler Deception, as detailed in the [ThreatLabz Observations](https://www.zscaler.com/blogs/security-research/cve-2026-111497-node2shell-http2shell-vulnerability-may-allow-rce#threatlabz-observations) section below.

## Recommendations

Zscaler recommends the following measures to address CVE-2026-111497 and monitor for potentially related activity:

- **Patch vulnerable runtimes and libraries.** Upgrade vulnerable runtimes, packages, and infrastructure components to the patched versions listed in the Vulnerable Versions table. Prioritize services that decompress untrusted Brotli data, including internet-facing applications that accept compressed request bodies and services that fetch content from external or user-controlled URLs. Validate each vulnerable component independently. Updating the system-wide libbrotli package may not remediate applications that statically bundle Brotli or ship their own decoder copy.
- **Rebuild and redeploy containers.** Use patched base images, runtimes, and libraries, and verify the versions in running workloads. Updating a host’s libraries does not update copies bundled within container images.
- **Disable Brotli decoding where patching is delayed.** If immediate patching is not possible, disable Brotli decompression on vulnerable paths where supported, following vendor guidance and testing for application compatibility.
- **Monitor for exploitation and post-exploitation behavior. Investigate the following:** 
  - Unexpected process crashes in Node.js, Bun, Python, .NET, Envoy Proxy, or service mesh workloads.
  - Repeated malformed Brotli payloads.
  - Requests containing Content-Encoding: br to endpoints that normally do not receive compressed request bodies.
  - Abnormal memory access violations or segmentation faults.
  - Web server or application worker crashes after compressed request handling.
  - Unexpected child processes spawned by web application runtimes.
  - Unexpected outbound connections following crashes or the processing of malformed compressed input.

## Vulnerable Versions

The following table lists vulnerable versions and corresponding fixes for selected software that incorporates the Brotli decoder.

| **Product** | **Vulnerable Versions** | **Patched Versions** | 
|---|---|---|
| Google Brotli | 1.0.3 \< 1.0.10 (semver) | 1.0.10 | 
| Google Brotli | 1.1.0 \< 1.1.1 (semver) | 1.1.1 | 
| Google Brotli | 1.2.0 \< 1.2.1 (semver) | 1.2.1 | 
| Node.js | 22.0.0 - 22.23.3 | 22.23.4 | 
| Node.js | 24.0.0 - 24.22.0 | 24.22.1 | 
| Node.js | 26.0.0 - 26.12.0 | 26.12.1 | 
| Bun | \< 1.4.4 | 1.4.4 | 
| .NET | 8.0.0 - 8.0.32 | 8.0.33 | 
| .NET | 9.0.0 - 9.0.21 | 9.0.22 | 
| .NET | 10.0.0 - 10.0.13 | 10.0.14 | 
| .NET | 11.0.0-preview.1 - 11.0.0-rc.2 | 11.0.0-rc.3.26522.148 | 
| Python Brotli (PyPI) | 1.2.0 | 1.2.1 | 
| Python brotlicffi (PyPI) | 1.2.0.0 - 1.2.0.2 | 1.2.1.0 | 
| Envoy Proxy | 1.39.2, 1.38.5, 1.37.7, 1.36.11 | 1.40.0, 1.39.3, 1.38.6, 1.37.8, 1.36.12 | 
| Java brotli4j | \< 1.24.0 | 1.24.0 | 
| libbrotli (Debian) | 1.1.0-2 | 1.1.0-2+deb13u1 | 
| libbrotli | Varies by distribution | Apply vendor security updates | 

Table 1: Software versions vulnerable to CVE-2026-111497 and the corresponding patched versions.

## ThreatLabz Observations

ThreatLabz observed reconnaissance and exploitation attempts involving CVE-2026-111497 through Zscaler Deception. Within the first 24 hours following public disclosure, Zscaler Deception’s global decoy mesh observed activity from 20 source IP addresses targeting 12 customers across 402 events. Of these events, 40% involved reconnaissance and 60% involved exploitation attempts.

The table below summarizes the unique payloads associated with reconnaissance and exploitation attempts targeting CVE-2026-111497 observed through Zscaler Deception.

| **Payload Description** | **JA4 Fingerprint** | 
|---|---|
| Malformed Brotli stream headers + valid Brotli differential check + Node.js path recon | t13d4312h1\_c7886603b240\_b26ce05bbdd6 | 
| Truncated JSON Brotli + 8-byte invalid Brotli padding stream + uncompressed controls | None | 
| 22-byte & 23-byte invalid block-switch OOB-write seeds (CVE-2026-111497) | t13d251100\_b78ed14e2fd0\_ab7e3b40a677 | 
| Brotli decompression bomb / Celery stream probe + 1B controls | None | 
| Assetnote 1-byte malformed/valid Brotli differential check | Multiple observed | 
| 3-stage Node2Shell capability, Strapi & CVE-2026-111497 JSON parser probe | t13d521100\_b262b3658495\_8e6e362c5eac | 
| 14-byte Brotli {"ping":1} differential sweep | t13d1714h1\_ab0a1bf427ad\_5e078a691127 | 

Table 2: Unique payloads observed during reconnaissance and exploitation attempts targeting CVE-2026-111497.

## How It Works

Brotli is a lossless compression algorithm and data format developed by Google. It is used for HTTP compression to reduce the size of web content such as HTML, CSS, JavaScript, JSON, and API responses. Brotli-encoded HTTP content is identified by the `Content-Encoding: br` header.

Applications may use Brotli directly or through dependencies such as runtimes, frameworks, HTTP clients, and middleware. In some configurations, these components automatically decompress Brotli-encoded content without application code explicitly calling Brotli APIs.

### Vulnerability details

The flaw occurs in Brotli’s block-decoding logic. When a stream changes block type, the decoder determines the next block type and length. In vulnerable versions, there is a macro (in the fast-path logic) that does not properly check the return value of the `DecodeBlockTypeAndLength` function, which can cause the decoder to continue processing an invalid state (e.g., when provided a maliciously crafted Brotli stream). This can lead to an out-of-bounds write and be used as a primitive for RCE. The upstream fix modifies the decoder so malformed block-switch conditions return a distinct error that is propagated to the caller, stopping further decoding of the malicious Brotli stream.

### Attack chain

Exploitation of CVE-2026-111497 may follow either an inbound or outbound path, depending on where Brotli decompression occurs, as shown in the figure below. Inbound attempts use crafted Brotli-compressed HTTP request bodies while outbound attempts use crafted responses returned by an attacker-controlled or compromised server. These responses may be consumed through `fetch()`, webhook delivery, URL previews, crawlers or scrapers, and API integrations. In either path, exploitation requires attacker-controlled Brotli data to reach a vulnerable decoder, with compressed HTTP content marked by `Content-Encoding: br`.

Figure 1: Potential inbound and outbound exploitation paths for CVE-2026-111497.

## Conclusion

CVE-2026-111497 affects the Brotli decoder used by Node.js and other software. Exposure depends on whether an application passes attacker-controlled Brotli data to a vulnerable decoder. Organizations should identify vulnerable components and apply corresponding vendor updates, including updates for applications that bundle their own copy of Brotli.

Zscaler Deception has observed active reconnaissance and exploitation attempts involving this vulnerability. ThreatLabz will continue monitoring for related activity and provide updates as additional findings become available.

## Zscaler Coverage

The Zscaler ThreatLabz team has deployed protections for CVE-2026-111497 with the following signatures:

**Zscaler Private Access (ZPA) App Protection**

The following ZPA App Protection signature detects attempts to exploit CVE-2026-111497 in internal applications accessed through ZPA, including activity originating from compromised endpoints or insiders:

**Zscaler Advanced Threat Protection**

**Zscaler Deception** 

Organizations should deploy the following Zscaler Deception decoys to help detect reconnaissance and exploitation attempts:

- MLflow
- Metaflow
- Bento Frontend
- Ray Serve
- GitLab

## How Zscaler Can Help

The following table shows the typical attack stages and the mitigations recommended by Zscaler.

| **Attack Stage** | **Recommended Mitigation** | 
|---|---|
| Minimize the external attack surface | Identify internet-facing applications containing vulnerable versions using [<u>Zscaler Exposure Management</u>](https://www.zscaler.com/products-and-solutions/exposure-management). Find services running vulnerable runtimes or libraries. Reduce direct exposure by placing applications behind a Zero Trust architecture. | 
| Prevent compromise | Enable SSL/TLS inspection where appropriate. Use [<u>Advanced Threat Protection</u>](https://www.zscaler.com/products-and-solutions/advanced-threat-protection) to detect exploit attempts and suspicious payload delivery. Use [<u>ZPA App Protection</u>](https://www.zscaler.com/products-and-solutions/zscaler-appprotection) to inspect and block suspicious requests targeting private applications. | 
| Reduce outbound exploitation risk | Route server egress through [<u>Zscaler Internet Access (ZIA)</u>](https://www.zscaler.com/products-and-solutions/zscaler-internet-access) to inspect outbound traffic. Restrict application egress to approved destinations. Pay special attention to webhook, crawler, URL preview, and third-party integration services that fetch content from external or user-controlled URLs. | 
| Prevent lateral threat movement | Use [<u>ZPA</u>](https://www.zscaler.com/products-and-solutions/zscaler-private-access) to enforce least-privilege user-to-application segmentation. Use [<u>Zscaler Deception</u>](https://www.zscaler.com/products-and-solutions/deception-technology) to detect attacker movement after initial compromise. Monitor for suspicious access to internal applications following web application crashes or abnormal behavior. | 
| Detect post-exploitation activity | Use [<u>Zscaler Managed Detection & Response (MDR)</u>](https://www.zscaler.com/products-and-solutions/managed-detection-and-response) and [<u>Threat Hunting</u>](https://www.zscaler.com/products-and-solutions/managed-threat-hunting) to investigate suspicious process behavior, command execution, unusual outbound connections, container runtime anomalies, and web application worker crashes. | 
| Prevent data loss | Inspect outbound traffic across channels with [<u>Zscaler Data Loss Prevention (DLP)</u>](https://www.zscaler.com/products-and-solutions/data-loss-prevention). Monitor for unusual uploads, archive transfers, credential exposure, or data movement following suspected exploitation. | 

## 

Indicators Of Compromise (IOCs)

A list of select source IP addresses is listed in the table below. For additional [<u>IP addresses</u>](https://github.com/ThreatLabz/iocs/blob/main/http2shell/ip_addresses_http2shell.txt) and [<u>JA4 fingerprints</u>](https://github.com/ThreatLabz/iocs/blob/main/http2shell/ja4_fingerprints_http2shell.txt), please visit our GitHub ThreatLabz repository.

| **Source IP Address** | **Activity Type** | 
|---|---|
| 49\[.\]37\[.\]46\[.\]99 | Exploitation | 
| 34\[.\]10\[.\]240\[.\]142  | Exploitation | 
| 188\[.\]245\[.\]184\[.\]87 | Exploitation | 
| 52\[.\]46\[.\]50\[.\]66  | Exploitation | 
| 136\[.\]111\[.\]197\[.\]96 | Exploitation | 

## Was this post useful?

Disclaimer: This blog post has been created by Zscaler for informational purposes only and is provided "as is" without any guarantees of accuracy, completeness or reliability. Zscaler assumes no responsibility for any errors or omissions or for any actions taken based on the information provided. Any third-party websites or resources linked in this blog post are provided for convenience only, and Zscaler is not responsible for their content or practices. All content is subject to change without notice. By accessing this blog, you agree to these terms and acknowledge your sole responsibility to verify and use the information as appropriate for your needs.

## Get the latest Zscaler blog updates in your inbox

By submitting the form, you are agreeing to our [privacy policy](https://www.zscaler.com/privacy-compliance/company-privacy-policy).
