---
title: "Chilling Discoveries: Unpacking Vulnerabilities in Copeland XWEB Pro Controllers"
author: Amir Zaltzman
url: https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers
hostname: claroty.com
description: Team82 researched the attack surface of the Copeland XWEB Pro platform to assess its resilience against network-based attacks. Our analysis uncovered a total of 23 vulnerabilities, 21 of which are high-severity. Each issue independently poses a significant security risk and can ultimately allow an unauthenticated attac...
sitename: Claroty
date: "2026-08-09"
fingerprint: "95d364072e4941c5"
---
Amir Zaltzman

/
    
    August 9th, 2026
    
    
    
    
Modern cold-chain logistics depend on precise, uninterrupted climate control. Large distribution centers store tons of perishable food, supermarkets operate extensive refrigerated display networks, and healthcare facilities safeguard temperature-sensitive pharmaceuticals. At the center of these environments is **the supervisory controller, which coordinates refrigeration equipment and ensures stable operation.**

<u>Team82</u> **researched the attack surface of the Copeland XWEB Pro platform to assess its resilience against network-based attacks.** Our analysis uncovered a total of 23 vulnerabilities, 21 of which are high-severity. Each issue independently poses a significant security risk and can ultimately allow an unauthenticated attacker to progressively bypass the platform's security mechanisms, resulting in root-level remote code execution (RCE). As demonstrated in our live physical test environment, **a compromised supervisory controller grants an attacker the ability to physically manipulate refrigeration systems and silently spoil the contents.**

We disclosed the vulnerabilities to Copeland, which addressed them in [<u>a firmware update</u>](https://webapps.copeland.com/Dixell/Pages/SystemSoftwareUpdate), version 1.13.

In this blog, we will explain:

- Where supervisory controllers sit in the commercial refrigeration architecture
- Some details on the 23 vulnerabilities uncovered in Copeland XWEB
- Describe a real-world demonstration of the consequences of exploits against these vulnerabilities
- Our disclosure and Copeland’s remediation of the issues

Commercial refrigeration systems are typically organized in a hierarchical architecture. At the top is a supervisory controller, which connects the network to the refrigeration equipment. Through its Ethernet connection, operators can remotely monitor the system, review alarms, and configure refrigeration settings.

The supervisory controller communicates with field controllers over an RS485 serial network, typically using the Modbus protocol. A single supervisory controller can manage multiple field controllers connected in a daisy-chain configuration.

Each field controller is installed on an individual refrigeration unit and directly controls the physical equipment. It monitors temperature sensors and operates components such as compressors, cooling fans, and defrost heaters to maintain the desired temperature. In this architecture, the supervisory controller provides centralized monitoring and management, while the field controllers perform the real-time control of the refrigeration equipment.

One of the most widely deployed platforms in this space is the [<u>Copeland XWEB Pro product family, including the XWEB300D PRO and XWEB500D PRO</u>](https://webapps.copeland.com/Dixell/Content/Pages/Manuals/XWEBPRO/XWEB300D500DV.1.0INSTALLATION/XWEB300D-500D-PRO-STP-GB.pdf). These controllers manage distributed field devices, coordinating compressors, evaporators, and environmental sensors while maintaining the temperature records required for regulatory compliance.

Given the critical role these controllers play in cyber-physical systems (CPS), where they are responsible for monitoring and controlling refrigeration equipment that protects temperature-sensitive goods and infrastructure, we evaluated the security of the Copeland XWEB Pro platform to assess its resilience against both network-based attacks and attacks originating through physical interfaces. Our objective was to determine whether an attacker could compromise the platform, bypass its security controls, and influence connected field devices responsible for critical refrigeration operations.

Our research began where most do: the authentication perimeter. The XWEB Pro utilizes a Lighttpd web server, which directs incoming API requests to a centralized Lua-based middleware layer.

When a user attempts to access a protected route within a specific route group, the request is intercepted by a function named `get_authentication` to parse the HTTP Authorization: Basic header. The application expects this header to contain a defined authorization mode (`auth_mode`) such as local standard accounts or ldap. If the authentication mode is recognized, a secondary function (`user_authenticate`) verifies the credentials.

However, we discovered a profound logic flaw in how the system handled the **unexpected**. If an attacker supplied an unrecognized `auth_mode`, the user\_authenticate function did not explicitly reject the request by returning nil or false. Instead, it returned an unpopulated table: `{ user = nil, role = nil, recovery = nil }.`

In the Lua programming language, any table structure, even an empty one, evaluates as a "truthy" condition. The parent router merely checked if *something* was returned, rather than validating the contents of that something. By passing an anomalous authorization string, an attacker could trick the system into granting unauthenticated access to the administrative API. The digital bouncer had been bypassed not with a stolen key, but with a linguistic loophole.

The example below demonstrates the mechanics of this logic flaw. By manipulating the authorization header with unexpected parameters, a remote actor can subvert the authentication gate and reach internal administrative routes.

By intentionally supplying an unrecognized `auth_mode` (circumventing the expected standard or ldap parameters), an attacker manipulates the `get_authentication` function into returning a truthy (yet completely empty) authentication object. Since the routing logic only verifies the *existence* of this object rather than its contents, the attacker effortlessly bypasses the authentication gate, gaining unfettered access to the protected endpoints.

We discovered a deterministic password generation mechanism that derives administrator SSH and web interface credentials from the current date, the device's MAC address, and hard-coded cryptographic keys embedded in the firmware. Both the current date and the MAC address are publicly accessible, while the username is only used when generating user-specific recovery passwords.

An attacker who can reproduce this algorithm can derive valid administrator credentials and use them to enable and access the device's built-in SSH or Shellinabox interfaces.

The hard-coded keys used for web authentication, SSH authentication, recovery passwords, and emergency seed generation are stored in the filesystem.

The password generation mechanism operates in two distinct phases using standard key derivation functions.

- **Phase 1 (Device Key Generation):** At startup, the system derives a unique device key by hashing a static, hardcoded seed value alongside the device's MAC address.
- **Phase 2 (Daily Password Derivation):** A daily background process then hashes this device key with the current system date to produce the active administrative password (or a user-specific recovery password).

The vulnerability stems from predictable inputs. Because the seed values are identical across the product line and the variables (MAC address and date) can be obtained via unauthenticated public endpoints, an adversary can reconstruct the entire derivation chain offline.

Once an attacker bypasses authentication, either through the Lua authentication vulnerability or by deriving valid credentials from the cryptographic password generation mechanism, they gain access to the device's management functionality. Our review of these routines uncovered **19** OS command injection vulnerabilities. Across multiple API and CGI endpoints, user-controlled input was repeatedly concatenated into operating system commands without proper sanitization.

Whether importing a contact list, configuring network settings, or performing a firmware update, the backend routinely passed user-supplied data directly to Lua's system execution functions. By embedding shell metacharacters into otherwise legitimate JSON payloads or uploaded files, an attacker can force the underlying Linux operating system to execute arbitrary commands. Since these services run with elevated privileges, successful exploitation results in immediate root-level code execution on the controller.

To demonstrate the real-world impact of these vulnerabilities, we built a live physical test environment that recreates a realistic attack scenario. Starting from an Internet-exposed XWEB controller, we show how a remote attacker can compromise the device and ultimately manipulate the refrigeration system it controls.

Our demonstration shows how a remote attacker can manipulate a serially connected field controller (an XR60CX in our setup) through a compromised XWEB controller. The attacker can fully control the displayed temperature and remotely enable or disable each physical component of the refrigeration system, including the compressor, cooling fans, defrost cycle, and lighting.

For our demonstration, we built a custom DIY mini refrigerator, shown in the following illustration:

The setup consists of the mini refrigerator shown above, with the XR60CX field controller connected to the central XWEB Pro controller over a serial interface. The thermoelectric cooling module is powered through the field controller, allowing the XWEB Pro to directly control the refrigerator's cooling system. Finally, the XWEB Pro is connected to the network via its Ethernet interface, with the attacker's machine connected to the same network.

The field controller is managed by the XWEB Pro over a serial Modbus connection. To control the XR60CX through this interface, we first needed to reverse engineer its Modbus register map, because the register addresses for many functions are not publicly documented.

Using the XR60CX datasheet together with protocol analysis, we mapped each exposed function to its corresponding Modbus register and built a comprehensive register map. This enabled us to remotely control the field controller through the XWEB Pro, including manipulating the displayed temperature and controlling the refrigerator's physical components.

With the setup complete, we can now demonstrate the attack. We developed a Python proof-of-concept (PoC) that first establishes an SSH connection to the XWEB Pro using the deterministic daily administrator password generated by the password generation algorithm we uncovered.

The PoC provides two primary capabilities:

1. **Display arbitrary temperatures.** The script can set the temperature shown on the XR60CX display to any value between **-50°C and 110°C**, regardless of the actual temperature measured by the probe.

**Spoil the refrigerator contents while hiding the attack.** The script continuously updates the displayed temperature with the legitimate reading from the temperature probe while simultaneously disabling the cooling fans. As a result, the refrigerator gradually warms up and its contents spoil, even though the displayed temperature continues to appear normal and does not indicate that the cooling system has failed.

Claroty Team82 is committed to coordinated disclosure with affected vendors. Following our discoveries, we reached out to Copeland and shared our findings. Copeland worked closely and collaboratively with us to develop a comprehensive remediation strategy. The vendor successfully patched these vulnerabilities and has uploaded firmware update version 1.13 to secure affected XWEB Pro devices.

The boundary between digital networks and physical systems is exceptionally thin in operational technology (OT). As our research demonstrates, a handful of software vulnerabilities and weak credential generation mechanisms in a supervisory controller can quickly escalate into real-world physical consequences, from spoiled food to compromised temperature-sensitive medical supplies.

More broadly, these findings underscore the need for stronger cybersecurity across the commercial refrigeration industry. Predictable credentials, Internet-exposed management interfaces, and slow adoption of firmware updates continue to leave critical systems vulnerable. Improving resilience requires a defense-in-depth approach that includes timely patching, network segmentation, restricting Internet exposure, and securing the supervisory controllers at the center of these environments.

Vulnerability Researcher

Amir Zaltzman is a vulnerability researcher on Team82.

Stay in the know
        Get the Team82 Newsletter

Related Vulnerability Disclosures
    
    - 
                    [CVE-2026-24663
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an unauthenticated attacker to achieve remote code execution on the system by sending a crafted request to the libraries installation route and injecting malicious input into the request body.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 9.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-24663)
                
- 
                    [CVE-2026-21389
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by injecting malicious input into the request body sent to the contacts import route.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-21389)
                
- 
                    [CVE-2026-25111
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by injecting malicious input into requests sent to the restore route.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-25111)
                
- 
                    [CVE-2026-20742
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by injecting malicious input into requests sent to the templates route.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-20742)
                
- 
                    [CVE-2026-24517
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by injecting malicious input into requests sent to the firmware update route.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-24517)
                
- 
                    [CVE-2026-25195
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by supplying a crafted firmware update file via the firmware update route.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-25195)
                
- 
                    [CVE-2026-20910
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by injecting malicious input into the devices field of the firmware update update action to achieve remote code execution.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-20910)
                
- 
                    [CVE-2026-24689
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by injecting malicious input into the devices field of the firmware update apply action.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-24689)
                
- 
                    [CVE-2026-25109
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by injecting malicious input into the devices field when accessing the get setup route, leading to remote code execution.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-25109)
                
- 
                    [CVE-2026-20902
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by injecting malicious input into the map filename field during the map upload action of the parameters route.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-20902)
                
- 
                    [CVE-2026-24695
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by injecting malicious input into OpenSSL argument fields within requests sent to the utility route, leading to remote code execution.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-24695)
                
- 
                    [CVE-2026-25105
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by injecting malicious input into parameters of the Modbus command tool in the debug route.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-25105)
                
- 
                    [CVE-2026-24452
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by supplying a crafted template file to the devices route.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-24452)
                
- 
                    [CVE-2026-23702
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by sending malicious input injected into the server username field of the import preconfiguration action in the API V1 route.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-23702)
                
- 
                    [CVE-2026-25196
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by injecting malicious input into the Wi-Fi SSID and/or password fields can lead to remote code execution when the configuration is processed.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-25196)
                
- 
                    [CVE-2026-25721
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by injecting malicious input into the server username and/or password fields of the restore action in the API V1 route.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-25721)
                
- 
                    [CVE-2026-25037
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by configuring a maliciously crafted LCD state which is later processed during system setup, enabling remote code execution.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-25037)
                
- 
                    [CVE-2026-20764
                    An OS Command injection vulnerability exists in XWEB Pro version 1.12.1 and prior, enabling an authenticated attacker to achieve remote code execution on the system by providing malicious input via the device hostname configuration which is later processed during system setup, resulting in remote code execution.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-20764)
                
- 
                    [CVE-2026-25085
                    A vulnerability exists in Copeland XWEB Pro version 1.12.1 and prior, in which an unexpected return value from the authentication routine is later on processed as a legitimate value, resulting in an authentication bypass.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 8.6](https://claroty.com/team82/disclosure-dashboard/cve-2026-25085)
                
- 
                    [CVE-2026-21718
                    An authentication bypass vulnerability exists in Copeland XWEB Pro version 1.12.1 and prior, enabling any attackers to bypass the authentication requirement and achieve pre-authenticated code execution on the system.
Copeland XWEB 300D PRO: \<=1.12.1, Copeland XWEB 500D PRO: \<=1.12.1, Copeland XWEB 500B PRO: \<=1.12.1 are affected.
Copeland has provided a fix for the vulnerabilities and recommends users update the XWEB Pro to the latest version by going to their software update page. Alternatively, a user logged into an XWEB Pro with internet access can update XWEB Pro directly from Copeland servers via the menu SYSTEM -- Updates | Network.
                    CVSS v3: 10.0](https://claroty.com/team82/disclosure-dashboard/cve-2026-21718)
