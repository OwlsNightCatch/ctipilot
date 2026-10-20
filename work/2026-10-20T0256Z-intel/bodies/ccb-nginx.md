---
title: "WARNING: Heap-Based Buffer Overflows in NGINX Plus and NGINX Open Source Can Be Exploited to Cause Denial of Service or Code Execution, Patch Immediately!"
url: https://ccb.belgium.be/advisories/warning-heap-based-buffer-overflows-nginx-plus-and-nginx-open-source-can-be-exploited
hostname: belgium.be
sitename: ccb.belgium.be
date: "2026-10-19"
fingerprint: ed7f2d5376c06ca7
---
# WARNING: Heap-Based Buffer Overflows in NGINX Plus and NGINX Open Source Can Be Exploited to Cause Denial of Service or Code Execution, Patch Immediately!

**Last update:** 19/10/2026

**Affected software:**

- NGINX Open Source 0.1.29 to 1.30.5 and 1.31.0 to 1.31.6 (CVE-2026-15176)
- NGINX Open Source 1.30.0 to 1.30.5 and 1.31.2 to 1.31.6 (CVE-2026-93479)
- NGINX Plus R33 to R36, 37.0.0 to 37.0.5, and 37.1.0 (both CVEs)

**Type:** CWE-122: Heap-based Buffer Overflow

**CVE/CVSS:**

- CVE-2026-15176: CVSS 9.2 (CVSS:4.0/AV:N/AC:H/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)
- CVE-2026-93479: CVSS 9.2 (CVSS:4.0/AV:N/AC:H/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)

## Source

**Vendor:**

## Risk

NGINX is a widely used web server, reverse proxy and load balancer that handles web traffic for a large number of websites and online services.

If exploited, these vulnerabilities could allow an unauthenticated remote attacker to crash the NGINX worker process, disrupting the services it delivers (Availability). On systems where Address Space Layout Randomization (ASLR) is disabled or can be bypassed, an attacker could also execute code, which may lead to unauthorized access to sensitive information (Confidentiality) and modification of data or system behavior (Integrity).

## Technical Details

**CVE-2026-15176** is a heap-based buffer overflow in the ngx\_http\_core\_module. It affects configurations where a location uses the alias directive together with rewrite and a set or return directive referencing the $request\_filename variable, or where $request\_filename is used in an access log format directive.

An unauthenticated attacker can trigger the overflow by sending crafted HTTP requests, under conditions beyond the attacker’s control.

**CVE-2026-93479** is a heap-based buffer overflow in the evaluation of string expressions. It affects configurations where a map directive uses regex matching and the root directive or access log format references the map’s regex capture variables before referencing the map output variable.

The same result can be achieved by using a non-cacheable variable in a string expression under certain conditions. An unauthenticated attacker can trigger the overflow by sending crafted HTTP requests, under conditions beyond the attacker’s control.

## Recommended Actions

### Patch

The Centre for Cybersecurity Belgium strongly recommends installing updates for vulnerable devices with the highest priority after thorough testing.

### Monitor/Detect

The CCB recommends organizations upscale monitoring and detection capabilities to identify any related suspicious activity and ensure a swift response in case of an intrusion.

In case of an intrusion, you can report an incident via [https://ccb.belgium.be/en/cert/report-incident](https://ccb.belgium.be/en/cert/report-incident).

While patching appliances or software to the newest version may protect against future exploitation, it does not remediate historic compromise.
