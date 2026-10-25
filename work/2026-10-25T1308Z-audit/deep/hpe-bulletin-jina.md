Title: HPESBNW05162 rev.1 - Multiple Vulnerabilities in HPE Networking Wireless Operating Systems (AOS-10 & AOS-8)

URL Source: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us&docLocale=en_US

Published Time: Wed, 30 Sep 2026 10:28:22 GMT

Markdown Content:
**Potential Security Impact:** Local: Access Restriction Bypass; Remote: Arbitrary Code Execution, Cross-Site Scripting (XSS), memory corruption, local memory corruption, Buffer Overflow

## VULNERABILITY SUMMARY

**NOTE:** A signed text copy of this document exists at [hpe_networking_-_hpesbnw05162.txt](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.txt)

**NOTE:** A CSAF version of this document exists at [hpe_networking_-_hpesbnw05162.json](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json)

**Summary**

HPE Networking has released patches for the HPE Networking Wireless Operating Systems (AOS-8 and AOS-10) for Mobility Conductors, Controllers, Gateways, and Access Points that address multiple security vulnerabilities.

**Affected Products**

These vulnerabilities affect the following HPE Networking Wireless Operating Systems (AOS-8 and AOS-10) software versions unless specifically noted otherwise in the details section:

HPE Networking

*   Mobility Conductors 
*   Mobility Controllers
*   Mobility Gateways (Managed by HPE Networking Central)
*   AOS-10 Access Points (AOS-AP)
*   AOS-8 Instant Access Points (AOS-IAP)

Affected Software Version(s):

*   AOS-10.8.x.x: 10.8.1.1 and below
*   AOS-10.7.x.x: 10.7.2.6 and below
*   AOS-10.4.x.x: 10.4.1.13 and below
*   AOS-8.13.x.x: 8.13.3.0 and below
*   AOS-8.10.x.x: 8.10.0.23 and below

**IMPORTANT NOTE**: Any hardware, Mobility solutions (such as conductors, controllers, and gateways), access points, or virtual machines (VMs) compatible with the affected versions are vulnerable. To keep this bulletin concise, we have excluded some wireless hardware from the **Impacted Product Information** section. Therefore, the list provided below is for illustrative purposes only and does **not** include every affected hardware model.

**Unaffected Products**

Any other HPE Networking products and software versions not specifically listed above are not affected by these Vulnerabilities.

**Workaround**

To minimize the likelihood of an attacker exploiting these vulnerabilities, HPE Networking recommends that the CLI and web-based management interfaces be restricted to a dedicated layer 2 segment/VLAN and/or controlled by firewall policies at layer 3 and above along with accounting controls for tracking and logging user activities and resource usage.

**Exploitation and Public Discussion**

These vulnerabilities were generally discovered by internal security research at HPE Networking. HPE Networking is not aware of any public discussion or exploit code that targets the listed vulnerabilities as of the release date of this advisory. Customers are strongly urged to patch their instances due to the complexity, breadth, and impact of these vulnerabilities.

Please note that due to the size of the Details and References sections, these sections have been moved to the end of the document to improve readability.

**Details**

Authentication Bypass Leading to Remote Code Execution in AOS-10 (CVE-2026-79844)

Authentication bypass vulnerabilities in the affected interface of  
AOS-10 could allow an unauthenticated remote attacker to run arbitrary  
commands on the underlying host if certain preconditions outside of  
the attacker's control are met. Successful exploitation could allow an  
attacker to execute arbitrary commands on the underlying operating  
system.  
  
Internal References: VULN-1097, VULN-1232, VULN-1234, VULN-1235,  
 VULN-1239, VULN-1244  
Severity: Critical  
CVSS v3.1 Base Score: 10.0  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N  
  
Acknowledgements: Internal security research (HPE Networking).

Authentication Bypass Vulnerabilities in the PAPI Protocol of AOS-10 allow Unauthorized Access and Modification of Sensitive Data (CVE-2026-79845)

Vulnerabilities in the PAPI protocol of AOS-10 could allow an  
unauthenticated remote attacker to circumvent existing authentication  
controls. Successful exploitation could allow an attacker to gain  
administrative access, modify system configurations, and access or  
manipulate sensitive data.  
  
Internal References: VULN-1126, VULN-1264, VULN-1266, VULN-1268,  
 VULN-1273, VULN-1277  
Severity: Critical  
CVSS v3.1 Base Score: 10.0  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Command Injection Vulnerabilities in AOS-8 (CVE-2026-79846)

Command injection vulnerabilities exist in the affected interface of  
AOS-8 that could allow an unauthenticated remote attacker to run  
arbitrary commands on the underlying host if certain preconditions  
outside of the attacker's control are met. Successful exploitation  
could allow an attacker to execute arbitrary commands on the  
underlying operating system.  
  
Internal References: VULN-1168, VULN-1170, VULN-1176, VULN-1243,  
 VULN-1246, VULN-1254, VULN-1260  
Severity: Critical  
CVSS v3.1 Base Score: 10.0  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Buffer Overflow Vulnerabilities leads to Remote Code Execution in AOS-10 (CVE-2026-79847)

Buffer overflow vulnerabilities in the affected interface of  
AOS-10 could lead to unauthenticated remote code execution by  
sending specially crafted packets to the affected interface.  
Successful exploitation of this vulnerability results in the ability  
to execute arbitrary code as a privileged user on the underlying  
operating system.  
  
Internal References: VULN-1269, VULN-1272, VULN-1275, VULN-1281,  
 VULN-1285, VULN-1286, VULN-1288  
Severity: Critical  
CVSS v3.1 Base Score: 10.0  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated SQL Injection Vulnerabilities allow Remote Code Execution in AOS-8 (CVE-2026-79848, CVE-2026-79849)

Vulnerabilities in the affected interface of AOS-8 could allow an  
unauthenticated remote attacker to conduct SQL injection attacks  
against an affected AOS-8 instance. Successful exploitation could  
allow an attacker to execute arbitrary commands on the underlying  
operating system.  
  
Internal References: VULN-312, VULN-1336  
Severity: Critical  
CVSS v3.1 Base Score: 10.0  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking);  
 moonv (HPE Networking's Bug Bounty program).

Authentication Bypass Leading to Remote Code Execution in AOS-8 (CVE-2026-79850)

Vulnerabilities in the affected interface of AOS-8 could allow an  
unauthenticated remote attacker to bypass existing authentication  
controls and run arbitrary commands on the underlying host. Successful  
exploitation could allow an attacker to execute arbitrary commands as  
root on the underlying operating system leading to complete system  
compromise.  
  
Internal References: VULN-313, VULN-1214, VULN-1230, VULN-1238,  
 VULN-1240, VULN-1241, VULN-1256  
Severity: Critical  
CVSS v3.1 Base Score: 10.0  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Buffer Overflow Vulnerabilities lead to Remote Code Execution in AOS-10 (CVE-2026-79851)

Buffer overflow vulnerabilities exist in the affected interface of  
AOS-10 that could lead to unauthenticated remote code execution.  
Successful exploitation could allow an attacker to execute arbitrary  
code as a privileged user on the underlying operating system, leading  
to complete system compromise.  
  
Internal References: VULN-321, VULN-1145, VULN-1242, VULN-1324,  
 VULN-1327, VULN-1328, VULN-1329, VULN-1330,  
 VULN-1335, VULN-1337, VULN-1357  
Severity: Critical  
CVSS v3.1 Base Score: 10.0  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated SQL Injection allows Remote Code Execution in AOS Web-Based Management Interface (CVE-2026-79852)

A vulnerability in the web-based management interface of AOS could  
allow an unauthenticated remote attacker to conduct SQL injection  
attacks against the AOS instance. Successful exploitation could  
allow an attacker to execute arbitrary commands on the underlying  
operating system.  
  
Internal Reference: VULN-582  
Severity: Critical  
CVSS v3.1 Base Score: 9.8  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: moonv (HPE Networking's Bug Bounty program).

Unauthenticated Sensitive Information Disclosure leads to Remote Code Execution in AOS-10 (CVE-2026-79853)

Sensitive information disclosure vulnerabilities in the affected  
interface of AOS-10 could allow an unauthenticated remote attacker to  
obtain sensitive information from the affected system. Successful  
exploitation could allow an attacker to execute arbitrary commands on  
the underlying operating system.  
  
Internal Reference: VULN-108  
Severity: Critical  
CVSS v3.1 Base Score: 9.8  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: moonv (HPE Networking's Bug Bounty program)

Unauthenticated SQL Injection Vulnerability leads to Remote Code Execution in AOS-10 (CVE-2026-79854)

A vulnerability in the affected interface of AOS-10 could allow an  
unauthenticated remote attacker to conduct SQL injection attacks  
against the AOS-10 instance. Successful exploitation could allow an  
attacker to execute arbitrary commands on the underlying operating  
system.  
  
Internal References: VULN-1258, VULN-1325  
Severity: Critical  
CVSS v3.1 Base Score: 9.8  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Authentication Bypass in the SSH Daemon of AOS-8 leads to Complete System Compromise (CVE-2026-79855)

An authentication bypass vulnerability in the SSH daemon of AOS-8  
allows an unauthenticated remote attacker to circumvent existing  
authentication controls. Successful exploitation allows an attacker to  
gain administrative privileges leading to complete compromise of the  
AOS-8 host.  
  
Internal References: VULN-1092  
Severity: Critical  
CVSS v3.1 Base Score: 9.8  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Buffer Overflow Vulnerability leads to Authentication Bypass in AOS-8 (CVE-2026-79856)

A buffer overflow vulnerability exists in the PAPI protocol of AOS-8  
that could allow an unauthenticated remote attacker to circumvent  
existing authentication controls. Successful exploitation could allow  
an attacker to gain administrative access, modify system  
configurations, and access or manipulate sensitive data.  
  
Internal Reference: VULN-1117  
Severity: Critical  
CVSS v3.1 Base Score: 9.8  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Command Injection Vulnerability in AOS-8 PAPI Protocol (CVE-2026-79857)

There is a command injection vulnerability in the PAPI protocol  
(Aruba's access point management protocol) of AOS-8 that could lead to  
unauthenticated remote code execution by sending specially crafted  
packets to the affected UDP port. Successful exploitation of this  
vulnerability results in the ability to execute arbitrary code as a  
privileged user on the underlying operating system.  
  
Internal Reference: VULN-1267  
Severity: Critical  
CVSS v3.1 Base Score: 9.8  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated SQL Injection Vulnerability in the PAPI Protocol of AOS-8 (CVE-2026-79858)

An unauthenticated SQL injection vulnerability exists in the PAPI  
protocol in AOS-8. Successful exploitation could allow an  
unauthenticated remote attacker to obtain and modify sensitive  
information in the underlying database and to interrupt the normal  
operation of the affected service.  
  
Internal References: VULN-1282  
Severity: Critical  
CVSS v3.1 Base Score: 9.8  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Buffer Overflow Vulnerabilities lead to Remote Code Execution in AOS-8 (CVE-2026-79859)

Buffer overflow vulnerabilities exist in the affected interface of  
AOS-8 that could lead to unauthenticated remote code execution.  
Successful exploitation could allow an attacker to execute arbitrary  
code as a privileged user on the underlying operating system.  
  
Internal References: VULN-1144, VULN-1177, VULN-1236, VULN-1245,  
 VULN-1247, VULN-1248, VULN-1255, VULN-1259,  
 VULN-1333, VULN-1334  
Severity: Critical  
CVSS v3.1 Base Score: 9.8  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Buffer Overflow Vulnerabilities lead to Remote Code Execution in AOS-8 (CVE-2026-79860)

Buffer overflow vulnerabilities exist in an underlying service of  
AOS-8 that could lead to unauthenticated remote code execution by  
sending specially crafted packets destined to the PAPI (Aruba's access  
point management protocol) UDP port 8211. Successful exploitation  
could allow an attacker to execute arbitrary code as a privileged user  
on the underlying operating system.  
  
Internal References: VULN-279, VULN-1116  
Severity: Critical  
CVSS v3.1 Base Score: 9.8  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Command Injection Vulnerability in the PAPI Protocol of AOS-10 (CVE-2026-79861)

There is a command injection vulnerability in AOS-10 that could lead  
to unauthenticated remote code execution by sending specially crafted  
PAPI packets. Successful exploitation of this vulnerability  
results in the ability to execute arbitrary code as a privileged user  
on the underlying operating system.  
  
Internal References: VULN-364  
Severity: Critical  
CVSS v3.1 Base Score: 9.8  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Adjacent Buffer Overflow Vulnerabilities lead to Remote Code Execution (CVE-2026-79862, CVE-2026-79863)

Buffer overflow vulnerabilities in the affected interface of AOS-10  
or AOS-8 could allow an unauthenticated adjacent attacker to   
execute arbitrary code by sending specially crafted data to the   
affected interface. Successful exploitation could allow an attacker   
to execute arbitrary code as a privileged user on the underlying   
operating system.  
  
Internal References: VULN-1119, VULN-1120, VULN-1280, VULN-1293,  
 VULN-1297, VULN-319, VULN-328, VULN-1146,   
 VULN-1279, VULN-1309, VULN-1310, VULN-1311,   
 VULN-1332, VULN-1343, VULN-1346, VULN-1348,   
 VULN-1350, VULN-1143, VULN-1207, VULN-1251,   
 VULN-1257, VULN-1082, VULN-1167, VULN-1179,  
 VULN-92, VULN-1322, VULN-1155, VULN-1191,   
 VULN-1193, VULN-1197, VULN-1211, VULN-1212,   
 VULN-1215  
Severity: Critical  
CVSS v3.1 Base Score: 9.6  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking);  
 zzcentury (HPE Networking's Bug Bounty program).

Unauthenticated Adjacent Command Injection Vulnerability in AOS-10 (CVE-2026-79864)

Command injection vulnerabilities exist in the affected interface of  
AOS-10 that could allow an unauthenticated adjacent attacker to  
perform command injection. Successful exploitation could allow an  
attacker to execute arbitrary commands as a privileged user on the  
underlying operating system.  
  
Internal References: VULN-1138, VULN-1274  
Severity: Critical  
CVSS v3.1 Base Score: 9.6  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Adjacent Memory Corruption Vulnerability leads to Remote Code Execution in AOS-10 (CVE-2026-79865)

A memory corruption vulnerability in the affected interface of AOS-10  
could allow an unauthenticated adjacent attacker to achieve remote  
code execution. Successful exploitation could allow an attacker to  
execute arbitrary code as a privileged user on the underlying  
operating system.  
  
Internal References: VULN-1289, VULN-1253  
Severity: Critical  
CVSS v3.1 Base Score: 9.6  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Adjacent Path Traversal Vulnerability leads to Filesystem Compromise in AOS-8 (CVE-2026-79866)

An unauthenticated path traversal vulnerability exists in the PAPI  
protocol in AOS-8. Successful exploitation of this vulnerability could  
allow an unauthenticated adjacent attacker to read, modify, and delete  
files on the underlying operating system.  
  
Internal References: VULN-1123  
Severity: Critical  
CVSS v3.1 Base Score: 9.6  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Authentication Bypass Leading to Remote Code Execution in AOS-8 (CVE-2026-79867)

Authentication bypass vulnerabilities in the affected interface of  
AOS-8 could allow an unauthenticated adjacent attacker to circumvent  
existing authentication controls and run arbitrary commands on the  
underlying host. Successful exploitation could allow an attacker to  
execute arbitrary commands on the underlying operating system leading  
to complete system compromise.  
  
Internal References: VULN-1165, VULN-1166, VULN-1098, VULN-1226,  
 VULN-1331  
Severity: Critical  
CVSS v3.1 Base Score: 9.6  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Authentication Bypass Vulnerabilities lead to Complete System Compromise in AOS-8 (CVE-2026-79868)

Authentication bypass vulnerabilities in the affected interface of  
AOS-8 could allow an unauthenticated adjacent attacker to circumvent  
existing authentication controls. Successful exploitation could allow  
an attacker to gain administrative access, modify system  
configurations, and access or manipulate sensitive data, leading to  
complete compromise of the affected system.  
  
Internal References: VULN-1263, VULN-1265, VULN-1270, VULN-1276  
Severity: Critical  
CVSS v3.1 Base Score: 9.6  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Authentication Bypass Leading to Remote Code Execution in AOS-10 (CVE-2026-79869)

Authentication bypass vulnerabilities in the affected interface of  
AOS-10 could allow an unauthenticated adjacent attacker to circumvent  
existing authentication controls. Successful exploitation could allow  
an attacker to execute arbitrary commands as a privileged user on the  
underlying operating system .  
  
Internal References: VULN-322, VULN-382, VULN-1219, VULN-1220,  
 VULN-1221, VULN-1228, VULN-1231  
Severity: Critical  
CVSS v3.1 Base Score: 9.6  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Authentication Bypass leads to Unauthorized Access in AOS-8 (CVE-2026-79870)

An authentication bypass vulnerability in the PAPI protocol of AOS-8  
could allow an unauthenticated adjacent attacker to circumvent  
existing authentication controls. Successful exploitation could allow  
an attacker to gain administrative access, modify system  
configurations, access or manipulate sensitive data, and disrupt  
network operations.  
  
Internal References: VULN-1121  
Severity: Critical  
CVSS v3.1 Base Score: 9.6  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Sensitive Information Disclosure in the Command Line Interface of AOS-10 (CVE-2026-79871)

A sensitive information disclosure vulnerability in the command line  
interface of AOS-10 could allow an unauthenticated remote attacker to  
access sensitive information. Successful exploitation could allow an  
attacker to retrieve information which could be used to potentially  
gain further access to network services supported by AOS-10.  
  
Internal Reference: VULN-1113  
Severity: Critical   
CVSS v3.1 Base Score: 9.6  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Buffer Overflow Vulnerability allows Remote Code Execution in AOS-10 and AOS-8 (CVE-2026-79872)

A buffer overflow vulnerability exists in the underlying operating  
system of AOS that could lead to unauthenticated remote code  
execution by an unauthenticated remote attacker. Successful  
exploitation of this vulnerability results in the ability to execute  
arbitrary code as a privileged user on the underlying operating  
system.  
  
Internal Reference: VULN-306  
Severity: Critical  
CVSS v3.1 Base Score: 9.4  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L  
  
Acknowledgements: m0omo0d (HPE Networking's Bug Bounty program).

Unauthenticated Adjacent Authentication Bypasses in the PAPI Protocol of AOS-10 Leads to Unauthorized Administrative Access(CVE-2026-79873)

Authentication bypass vulnerabilities in the PAPI protocol of AOS-10  
could allow an unauthenticated adjacent attacker to circumvent  
existing authentication controls. Successful exploitation could allow  
an attacker to gain administrative access, modify system  
configurations, and access or manipulate sensitive data on affected  
devices.  
  
Internal References: VULN-1140, VULN-1271  
Severity: Critical  
CVSS v3.1 Base Score: 9.3  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N  
  
Acknowledgements: Internal security research (HPE Networking).

Authentication Bypass in the API allows Administrative Access of AOS-10 (CVE-2026-79874)

An authentication bypass in the API of AOS-10 allows an  
unauthenticated adjacent attacker to circumvent existing  
authentication controls. Successful exploitation could allow an  
attacker to gain administrative access, modify system configurations,  
and access or manipulate sensitive data.  
  
Internal Reference: VULN-1147  
Severity: Critical  
CVSS v3.1 Base Score: 9.3  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N  
  
Acknowledgements: Internal security research (HPE Networking).

Authentication Bypass in the PAPI Protocol of AOS-8 Allows Unauthorized Administrative Access (CVE-2026-79875)

A vulnerability has been identified in the PAPI protocol of AOS-8 that  
could potentially allow an unauthenticated adjacent attacker to  
circumvent existing authentication controls. Successful exploitation  
could allow an attacker to gain administrative access, modify system  
configurations, and access or manipulate sensitive data.  
  
Internal References: VULN-1171  
Severity: Critical  
CVSS v3.1 Base Score: 9.3  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Adjacent Sensitive Information Disclosure in AOS-10 Wi-Fi Frame Processing (CVE-2026-79876)

A sensitive information disclosure vulnerability in the Wi-Fi frame  
processing of AOS-10 could allow an unauthenticated adjacent attacker  
to access sensitive information. Successful exploitation could allow  
an attacker to retrieve information which could be used to potentially  
gain further access to network services supported by AOS-10, or to  
interrupt the normal operation of the affected service.  
  
Internal References: VULN-1302  
Severity: Critical  
CVSS v3.1 Base Score: 9.3  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Adjacent Remote Code Execution Vulnerability in AOS-10 (CVE-2026-79877)

A remote code execution vulnerability in the underlying operating  
system of AOS-10 could allow an unauthenticated adjacent attacker to  
execute arbitrary code on an affected device. Successful exploitation  
could allow an attacker to execute arbitrary commands as a privileged  
user on the underlying operating system leading to complete system  
compromise.  
  
Internal References: VULN-1084  
Severity: High  
CVSS v3.1 Base Score: 8.8  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Adjacent Command Injection Vulnerability in the AOS-8 Command Line Interface Accessed by the PAPI Protocol (CVE-2026-79878)

A command injection vulnerability in the AOS-8 command line interface  
accessed by the PAPI protocol could lead to unauthenticated remote  
code execution by an adjacent attacker sending specially crafted  
PAPI packets destined to the PAPI UDP port 8211. Successful   
exploitation could allow an attacker to execute arbitrary code   
as a privileged user on the underlying operating system.  
  
Internal References: VULN-1164  
Severity: High  
CVSS v3.1 Base Score: 8.8  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Adjacent Memory Corruption Vulnerabilities lead to Remote Code Execution in AOS-10 (CVE-2026-79879)

Memory corruption vulnerabilities in the affected interface of AOS-10  
could lead to remote code execution by an unauthenticated adjacent  
attacker. Successful exploitation could allow an attacker to execute  
arbitrary code as a privileged user on the underlying operating system

.

Internal References: VULN-325, VULN-1078, VULN-1099, VULN-1342,  
 VULN-1351, VULN-1356  
Severity: High  
CVSS v3.1 Base Score: 8.8  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Authenticated Server-Side Request Forgery leads to Remote Code Execution in AOS-8 (CVE-2026-79880)

A vulnerability in the command line interface of AOS-8 could allow an  
authenticated remote attacker with high privileges to conduct a  
server-side request forgery (SSRF) attack. Successful exploitation  
could allow an attacker to execute arbitrary commands on the  
underlying operating system.  
  
Internal References: VULN-144  
Severity: High  
CVSS v3.1 Base Score: 8.7  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:N/I:H/A:H  
  
Acknowledgements: m0omo0d (HPE Networking's Bug Bounty program).

Authentication Bypass Leading to Remote Code Execution in AOS-8 (CVE-2026-79881)

An authentication bypass vulnerability in the underlying operating  
system of AOS-8 could allow an unauthenticated remote attacker to  
circumvent existing authentication controls. Successful exploitation  
could allow an attacker to execute arbitrary code as a privileged user  
on the underlying operating system leading to complete system  
compromise.  
  
Internal References: VULN-1160  
Severity: High  
CVSS v3.1 Base Score: 8.5  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Adjacent Command Injection Vulnerability in the PAPI Protocol of AOS-10 (CVE-2026-79882)

There is a command injection vulnerability in the PAPI protocol of  
AOS-10 that could lead to unauthenticated remote code execution by an  
adjacent attacker sending specially crafted packets. Successful  
exploitation of this vulnerability could allow an attacker to execute  
arbitrary code as a privileged user on the underlying operating  
system.  
  
Internal References: VULN-1131  
Severity: High  
CVSS v3.1 Base Score: 8.3  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Adjacent Buffer Overflow Vulnerability in the PAPI Protocol leads to Sensitive Information Disclosure in AOS-10 (CVE-2026-79883)

A buffer overflow vulnerability in the PAPI protocol of HPE  
Networking AOS-10 could allow an unauthenticated adjacent attacker to  
access sensitive information. Successful exploitation could allow an  
attacker to retrieve information which could be used to potentially  
gain further access to network services supported by AOS-10, and to  
interrupt the normal operation of the affected service.  
  
Internal References: VULN-1352  
Severity: High  
CVSS v3.1 Base Score: 8.3  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Authentication Bypass leads to Sensitive Information Disclosure in AOS-8 (CVE-2026-79884)

A vulnerability in the web-based management interface of AOS-8 could  
allow an unauthenticated adjacent attacker to bypass existing  
authentication controls and access sensitive information. Successful  
exploitation could allow an attacker to gain access to some data in a  
cleartext format possibly exposing other network infrastructure to  
further compromise.  
  
Internal References: VULN-1076  
Severity: High  
CVSS v3.1 Base Score: 8.2  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:L  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated File Write Vulnerability leads to Denial-of-Service in AOS-8 (CVE-2026-79885)

An unauthenticated file write vulnerability exists in the PAPI  
protocol in AOS-8. Successful exploitation could allow an  
unauthenticated remote attacker to make limited modifications   
to files on the affected system and to disrupt the availability   
of the affected service.  
  
Internal References: VULN-1150  
Severity: High  
CVSS v3.1 Base Score: 8.2  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Buffer Overflow Vulnerability leads to Denial-of-Service in AOS-8 (CVE-2026-79886)

An unauthenticated buffer overflow vulnerability exists in the PAPI  
protocol of AOS-8. Successful exploitation could allow an  
unauthenticated remote attacker to disrupt the availability of the  
affected service on the controller, with a limited impact to its  
integrity.  
  
Internal Reference: VULN-1190  
Severity: High  
CVSS v3.1 Base Score: 8.2  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Authentication Bypass in Web Interface of AOS-8 allows Remote Command Execution (RCE) (CVE-2026-79887)

A vulnerability in the web interface of AOS-8 could allow  
an unauthenticated remote attacker to achieve remote code execution.  
Successful exploitation could lead to complete device control,  
enabling interception of network traffic and potential compromise of  
connected systems.  
  
Internal References: VULN-259  
Severity: High  
CVSSv3.1 Base Score: 8.1  
CVSSv3.1 Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Diego Gomez & David Kierznowski (HPE Networking's   
 Bug Bounty program)

Unauthenticated Buffer Overflow allows Remote Code Execution in web interface (CVE-2026-79888)

A vulnerability in a certain web interface endpoint of AOS-8  
devices could allow an unauthenticated remote attacker to trigger a  
buffer overflow. Successful exploitation could allow an  
attacker to execute arbitrary commands on the underlying operating  
System, leading to complete system compromise.  
  
Internal References: VULN-258  
Severity: High  
CVSSv3.x Overall Score: 8.1  
CVSS Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Diego Gomez & David Kierznowski (HPE Networking's   
 Bug Bounty program)

Multiple Unauthenticated Buffer Overflow vulnerabilities in AOS-8 Web Interface result in Remote Code Execution (CVE-2026-79889)

Vulnerabilities in multiple web interface endpoints of AOS-8  
devices could allow an unauthenticated remote attacker to trigger a  
buffer overflow by using specially crafted requests. Successful   
exploitation could allow an attacker to execute arbitrary commands   
on the underlying operating system, leading to complete system   
compromise.  
  
Internal References: VULN-234  
Severity: High  
CVSSv3.x Overall Score: 8.1  
CVSS Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Diego Gomez & David Kierznowski (HPE Networking's   
 Bug Bounty program)

Unauthenticated Command Injection Vulnerabilities in AOS-8 Accessed by the PAPI Protocol (CVE-2026-79890)

There are command injection vulnerabilities in AOS-8 that could lead  
to unauthenticated remote code execution by sending specially crafted  
PAPI packets. Successful exploitation of this vulnerability results   
in the ability to execute arbitrary code as a privileged user on the   
underlying operating system.  
  
Internal References: VULN-1198, VULN-1200  
Severity: High  
CVSS v3.1 Base Score: 8.1  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Buffer Overflow Vulnerability leads to Remote Code Execution in AOS-8 (CVE-2026-79891)

A buffer overflow vulnerability exists in the command line interface  
of AOS-8 that could allow an unauthenticated remote attacker to run  
arbitrary commands on the underlying host if certain preconditions  
outside of the attacker's control are met. Successful exploitation  
could allow an attacker to execute arbitrary code as a privileged user  
on the underlying operating system leading to complete system  
compromise.  
  
Internal References: VULN-1181  
Severity: High  
CVSS v3.1 Base Score: 8.1  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Authenticated Local Memory Corruption Vulnerability leads to Arbitrary Code Execution in AOS-8 (CVE-2026-79892)

A memory corruption vulnerability exists in AOS-8 that could allow an  
authenticated local attacker to execute arbitrary code. Successful  
exploitation could allow the attacker to execute arbitrary code as a  
privileged user on the underlying operating system.  
  
Internal References: VULN-1252  
Severity: High  
CVSS v3.1 Base Score: 7.8  
CVSS v3.1 Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Memory Corruption Vulnerabilities lead to Denial-of-Service in AOS-10 (CVE-2026-79893)

Memory corruption vulnerabilities in AOS-10 could allow an  
unauthenticated remote attacker to conduct a denial of service attack.  
Successful exploitation could allow an attacker to disrupt the  
availability of the affected service.  
  
Internal References: VULN-1102, VULN-1105  
Severity: High  
CVSS v3.1 Base Score: 7.5  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Denial-of-Service (DoS) Vulnerability in the PAPI Protocol of AOS-8 (CVE-2026-79894)

An unauthenticated Denial-of-Service (DoS) vulnerability exists in the  
PAPI protocol of AOS-8. Successful exploitation of this vulnerability  
results in the ability to disrupt the availability of the affected  
interface.  
  
Internal References: VULN-1262, VULN-1148  
Severity: High  
CVSS v3.1 Base Score: 7.5  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Remote Denial-of-Service (DoS) Vulnerabilities in AOS-10 (CVE-2026-79895)

Vulnerabilities in the affected interface of AOS-10 could allow an  
unauthenticated remote attacker to conduct a denial of service attack.  
Successful exploitation could allow an attacker to disrupt the  
availability of the affected interface.  
  
Internal References: VULN-1287, VULN-1304  
Severity: High  
CVSS v3.1 Base Score: 7.5  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Memory Corruption Vulnerability leads to Denial-of-Service in AOS-8 (CVE-2026-79955)

An unauthenticated memory corruption vulnerability exists in a service  
accessed via the PAPI protocol in AOS-8 that could allow an  
unauthenticated remote attacker to conduct a denial of service attack.  
Successful exploitation could allow an attacker to disrupt the  
availability of the affected service.  
  
Internal References: VULN-367  
Severity: High  
CVSS v3.1 Base Score: 7.5  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Improper Sanitization leads to Command Injection in AOS-8 Web Interface (CVE-2026-79956)

A vulnerability in the CLI command handling of the AOS-8 web   
interface could allow an authenticated remote attacker to execute   
arbitrary commands on the underlying operating system. Successful   
exploitation could allow an attacker to run unauthorized commands   
on the system, potentially leading to system compromise.  
  
Internal References: VULN-225  
Severity: High  
CVSSv3.1 Base Score: 7.2  
CVSSv3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: LIUPENG (HPE Networking's Bug Bounty program)

Authenticated Remote Code Execution allows Unauthorized System Control in Wireless Network Management Interface (CVE-2026-95704)

A vulnerability in the web-based management interface of wireless  
network management systems could allow an authenticated remote  
attacker to execute remote code. Successful exploitation could enable  
an attacker to execute arbitrary commands on the underlying operating  
system, potentially compromising system integrity and data security.  
  
Internal References: VULN-111  
Severity: High  
CVSSv3.1 Base Score: 7.2  
CVSSv3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: moonv (HPE Networking's Bug Bounty program)

Authenticated Command Injection Vulnerabilities in AOS-8 (CVE-2026-95705)

Command injection vulnerabilities in the affected interface of AOS-8  
could allow an authenticated remote attacker with high privileges to  
perform command injection. Successful exploitation could allow an  
attacker to execute commands with the privileges of the impacted  
mechanism on the underlying operating system.  
  
Internal References: VULN-17  
Severity: High  
CVSS v3.1 Base Score: 7.2  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Michael Messner, Benedikt Kuehne & Caio Adler   
 Goncalves Farias (Siemens Energy).

Authenticated Command Injection Vulnerabilities in AOS-8 (CVE-2026-95706)

Command injection vulnerabilities in the affected interface of AOS-8  
could allow an authenticated remote attacker with high privileges to  
perform command injection. Successful exploitation could allow an  
attacker to execute commands with the privileges of the impacted  
mechanism on the underlying operating system.  
  
Internal References: VULN-111  
Severity: High  
CVSS v3.1 Base Score: 7.2  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: moonv (HPE Networking's Bug Bounty program).

Authenticated Buffer Overflow Vulnerability leads to Remote Code Execution in AOS-8 (CVE-2026-95707)

A buffer overflow vulnerability in the PAPI protocol of AOS-8 could  
allow an authenticated remote attacker with high privileges to achieve  
remote code execution. Successful exploitation could allow an attacker  
to execute arbitrary code as a privileged user on the underlying  
operating system.  
  
Internal References: VULN-197  
Severity: High  
CVSS v3.1 Base Score: 7.2  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: LIUPENG (HPE Networking's Bug Bounty program).

Authenticated File Write leads to Command Injection Vulnerabilities in AOS-10 (CVE-2026-95708)

Command injection vulnerabilities exist in the affected interface of  
AOS-10 that could allow an authenticated remote attacker with high  
privileges to perform command injection. Successful exploitation could  
allow an attacker to execute arbitrary commands as a privileged user  
on the underlying operating system.  
  
Internal References: VULN-82  
Severity: High  
CVSS v3.1 Base Score: 7.2  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: zzcentury (HPE Networking's Bug Bounty program).

Authenticated Command Injection Vulnerabilities in AOS-10 (CVE-2026-95709)

Command injection vulnerabilities exist in the affected interface of  
AOS-10 that could allow an authenticated remote attacker with high  
privileges to perform command injection. Successful exploitation could  
allow an attacker to execute arbitrary commands as a privileged user  
on the underlying operating system.  
  
Internal References: VULN-233  
Severity: High  
CVSS v3.1 Base Score: 7.2  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: LIUPENG (HPE Networking's Bug Bounty program).

Unauthenticated Adjacent Buffer Overflow Vulnerability leads to Denial-of-Service in AOS-10 or AOS-8 (CVE-2026-95710)

An unauthenticated buffer overflow vulnerability exists in the   
Underlying operating system of AOS-10 or AOS-8 and could allow an   
unauthenticated adjacent attacker to conduct a denial of service   
attack. Successful exploitation could allow an attacker to disrupt   
the availability of the affected system, with a limited impact to   
the integrity of the affected component.  
  
Internal Reference: VULN-1359, VULN-332, VULN-1096, VULN-1107,   
 VULN-1137, VULN-1290, VULN-1338, VULN-1353,  
 VULN-1196  
Severity: High  
CVSS v3.1 Base Score: 7.1  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Authentication Bypass Leading to Remote Code Execution in AOS-10 Web-Based Management Interface (CVE-2026-95711)

An authentication bypass vulnerability in the web-based management  
interface of AOS-10 could allow an unauthenticated adjacent attacker  
to circumvent existing authentication controls and run arbitrary  
commands on the underlying host if certain preconditions outside of  
the attacker's control are met. Successful exploitation of this  
vulnerability could allow an attacker to execute arbitrary commands on  
the underlying operating system.  
  
Internal References: VULN-1094  
Severity: High  
CVSS v3.1 Base Score: 7.1  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Adjacent Sensitive Information Disclosure and Denial-of-Service in AOS-8 via the PAPI Protocol (CVE-2026-95712)

A sensitive information disclosure vulnerability in the PAPI protocol  
of AOS-8 could allow an unauthenticated adjacent attacker to access  
limited information handled by the affected service. Successful  
exploitation could allow an attacker to view some information and to  
disrupt the availability of the affected service.  
  
Internal References: VULN-1340  
Severity: High  
CVSS v3.1 Base Score: 7.1  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Buffer Overflow Vulnerability leads to Denial-of-Service in AOS-8 Command Line Interface (CVE-2026-95713)

An unauthenticated buffer overflow vulnerability exists in the command  
line interface of AOS-8. Successful exploitation could allow an  
unauthenticated remote attacker to disrupt the availability of the  
affected interface, along with limited access to or modification of  
some system data.  
  
Internal References: VULN-1151  
Severity: High  
CVSS v3.1 Base Score: 7.0  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Authenticated Adjacent Buffer Overflow Vulnerability leads to Remote Code Execution in AOS-10 (CVE-2026-95714)

A buffer overflow vulnerability exists in the API of AOS-10 that could  
allow an authenticated adjacent attacker with high privileges to  
achieve remote code execution. Successful exploitation could allow an  
attacker to execute arbitrary code as a privileged user on the  
underlying operating system.  
  
Internal References: VULN-1087  
Severity: Medium  
CVSS v3.1 Base Score:6.8  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Unauthenticated Local Command Injection Vulnerability in AOS-10 Command Line Interface (CVE-2026-95715)

An unauthenticated command injection vulnerability exists in the  
command line interface of AOS-10. Successful exploitation could allow  
an attacker with physical access to execute arbitrary commands as a  
privileged user on the underlying operating system leading to complete  
system compromise.  
  
Internal References: VULN-250  
Severity: Medium  
CVSS v3.1 Base Score: 6.8  
CVSS v3.1 Vector: CVSS:3.1/AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H  
  
Acknowledgements: PinkDraconian (HPE Networking's Bug Bounty program).

Authentication Bypass in the PAPI Protocol of AOS-10 allows Unauthorized Configuration Changes (CVE-2026-95716)

An authentication bypass in the PAPI protocol of AOS-10 allows an  
unauthenticated adjacent attacker to circumvent existing  
authentication controls. Successful exploitation allows an attacker to  
change the state of certain settings of a vulnerable system.  
  
Internal References: VULN-1085  
Severity: Medium  
CVSS v3.1 Base Score: 6.5  
CVSS v3.1 Vector: CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N  
  
Acknowledgements: Internal security research (HPE Networking).

Authenticated Stored Cross-Site Scripting (XSS) Vulnerability in AOS Web-Based Management Interface (CVE-2026-95717) ----------------------------------------------------------------- A stored cross-site scripting (XSS) vulnerability exists in the web-based management interface of AOS that could allow an authenticated remote attacker with high privileges to inject malicious scripts. Successful exploitation could allow an attacker to execute arbitrary script code in the context of another authenticated user's browser session.

Internal Reference: VULN-156  
 Severity: Medium  
 CVSS v3.1 Base Score: 5.5  
 CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:L/I:L/A:N  
  
 Acknowledgements: LIUPENG (HPE Networking's Bug Bounty program).

Authentication Bypass Vulnerability in the PAPI Protocol of AOS-8 (CVE-2026-95718)

An authentication bypass vulnerability in the PAPI protocol of AOS-8  
could allow an unauthenticated remote attacker to circumvent existing  
authentication controls. Successful exploitation could allow an  
attacker to make limited unauthorized modifications to certain  
settings of the affected system.  
  
Internal References: VULN-1118  
Severity: Medium  
CVSS v3.1 Base Score: 5.3  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N  
  
Acknowledgements: Internal security research (HPE Networking).

Authenticated Arbitrary File Deletion Vulnerability leads to Denial-of-Service in AOS-10 (CVE-2026-95719)

An arbitrary file deletion vulnerability exists in the command line  
interface of AOS-10 that could allow an authenticated attacker with  
administrative privileges to cause a denial of service. Successful  
exploitation could allow an attacker to crash the system, preventing  
it from rebooting without manual intervention and disrupting normal  
operation of the affected device.  
  
Internal References: VULN-154  
Severity: Medium  
CVSS v3.1 Base Score: 4.9  
CVSS v3.1 Vector: CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:N/A:H  
  
Acknowledgements: LIUPENG (HPE Networking's Bug Bounty program).

Authenticated Local Buffer Overflow Vulnerability leads to Denial-of-Service in AOS-8 (CVE-2026-95720)

A buffer overflow vulnerability exists in AOS-8 that could allow an  
authenticated attacker with administrative access to cause denial of  
service. Successful exploitation could allow an attacker to crash the  
system, preventing it from rebooting without manual intervention and  
disrupting network operations.  
  
Internal References: VULN-1365  
Severity: Medium  
CVSS v3.1 Base Score: 4.4  
CVSS v3.1 Vector: CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:N/I:N/A:H  
  
Acknowledgements: Internal security research (HPE Networking).

Authenticated Local Memory Corruption Vulnerability in AOS-8 Web-Based Management Interface (CVE-2026-95721)

A memory corruption vulnerability exists in the web-based management  
interface of AOS-8. Successful exploitation could allow an  
authenticated low privilege attacker with local access to view some  
system files and interrupt the normal operation of the affected  
service.  
  
Internal References: VULN-1194  
Severity: Low  
CVSS v3.1 Base Score: 3.3  
CVSS v3.1 Vector: CVSS:3.1/AV:L/AC:H/PR:L/UI:R/S:U/C:L/I:N/A:L  
  
Acknowledgements: Internal security research (HPE Networking).

Links/Buttons:
- [Privacy Statement](https://www.hpe.com/us/en/legal/privacy.html)
- [Support Center](https://support.hpe.com/connect/s/)
- [](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us&docLocale=en_US#resolution-4)
- [hpe_networking_-_hpesbnw05162.txt](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.txt)
- [hpe_networking_-_hpesbnw05162.json](https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json)
- [https://networkingsupport.hpe.com](https://networkingsupport.hpe.com/)
- [https://www.hpe.com/info/report-security-vulnerability](https://www.hpe.com/info/report-security-vulnerability)
- [Hewlett Packard Enterprise Product Security Response Policy](http://www.hpe.com/support/security-response-policy)
- [http://www.hpe.com/support/Subscriber_Choice](http://www.hpe.com/support/Subscriber_Choice)
- [http://www.hpe.com/support/Security_Bulletin_Archive](http://www.hpe.com/support/Security_Bulletin_Archive)
- [Feedback](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us&docLocale=en_US#doc-feedback__container)
