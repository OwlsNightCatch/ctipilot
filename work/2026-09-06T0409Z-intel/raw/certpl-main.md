# extract: served via trafilatura-direct
---
title: Critical vulnerabilities in MikroTik RouterOS are being actively exploited. Immediate update recommended
url: https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
hostname: cert.pl
description: The CERT Polska team has identified and coordinated the disclosure of six vulnerabilities in MikroTik RouterOS, including two critical ones. The vulnerabilities are already being actively exploited to take over devices whose SSH service is accessible from the internet. We recommend immediately updating devices to the patched versions and verifying the configuration for signs of compromise.
sitename: Critical vulnerabilities in MikroTik RouterOS are being actively exploited. Immediate update recommended
date: "2026-09-05"
---
The CERT Polska team has identified and coordinated the disclosure of six vulnerabilities in MikroTik RouterOS. Combining two of them allows an attacker to **take full control of the device without authentication** if the device supports remote access using the SSH protocol. To make this chain easier to identify, we have given it a common name, **MikroTrick**.

In recent days we have been observing attacks against RouterOS devices accessible from the internet. We have obtained confirmation that the attackers are exploiting this combination of vulnerabilities to take full control of devices whose SSH service is accessible from public networks. It has also been confirmed that the released patches prevent the observed attacks. We recommend applying the update immediately.

The vulnerabilities we describe affect the SSH server and client, the bandwidth-test service, X.509 certificate handling, and the WebFig interface. MikroTik has released fixes in versions 7.25beta3, 7.24.2, 7.23.4, and 6.49.21, as announced in its [security bulletin](https://mikrotik.com/supportsec/september-2026-vulnerability/). Along with this update, for the first time in history, MikroTik sent a push notification to the phones of users who had the MikroTik app installed. Administrators should update their devices as soon as possible and then check the configuration for unknown users, scripts, scheduler tasks, proxy servers, and tunnels.

## Identified vulnerabilities

In the course of our research we identified six vulnerabilities in RouterOS; below we describe the three most important ones, and all of them can be found on a [dedicated page](https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve).

### CVE-2026-67276 - SSH authentication bypass (CVSS: 9.2)

RouterOS did not properly verify public keys used for SSH authentication - in particular, it did not compare the entire RSA public key assigned to a user. An attacker who knew the username and the public modulus of the user's key could craft a different key and log in via SSH without possessing the corresponding private key. The privileges obtained were equivalent to those of the targeted account.

### CVE-2026-86060 - SSH session privilege manipulation via a crafted username (CVSS: 9.2)

RouterOS did not properly handle usernames beginning with a disallowed character in the SSH login mechanism. By using a crafted username, an attacker could elevate their privileges. The resulting session had full administrative privileges in the RouterOS system.

### CVE-2026-67277 - memory disclosure and crash via bandwidth-test (CVSS: 8.8)

The bandwidth-test service allowed an unauthenticated connection to enter a state that should only be reachable after logging in. Combined with two separate flaws - disclosure of uninitialized data from the packet buffer and an integer underflow in size validation - this enabled kernel memory leakage or a remote DoS attack leading to a system restart.

## Observed attacks on RouterOS and the "Flagged" mechanism

Technical indicators and information obtained by CERT Polska through internal channels pointed to the possibility of RouterOS vulnerabilities being actively exploited in real-world attacks conducted in recent days. We now have confirmation that the combination of two of them (MikroTrick) is being exploited to take full control of devices whose SSH service is accessible from public networks. According to the information we have, updating to the latest version prevents these attacks.

In the fixed releases, MikroTik used a mechanism that, at RouterOS startup, scans the configuration for known signs of unauthorized changes, disables the recognized suspicious configuration entries, writes a critical message to the log, and sets a warning (the "Flagged" marker). This mechanism detects only selected traces left after a compromise - the absence of the marker is not proof that the device is safe. The vendor describes the details of the procedure in the [documentation of the "Flagged" mechanism](https://manual.mikrotik.com/docs/system-information-and-utilities/device-mode#flagged-status).

We cannot rule out the existence of vulnerabilities unknown to us that the vendor did not describe in the changelog. The "Flagged" marker for compromised devices should therefore be treated as an indication of a possible earlier compromise, not as proof that one of the vulnerabilities reported by CERT Polska was exploited.

If a device has been marked as compromised, assume it has been taken over: take the actions described at the end of the Recommendations section.

The observed attacks left the following markers in the RouterOS log:

```
login failure for user -2 from <ip> via ssh
user <name> added by ssh:-2@<ip>
```
An additional indicator of compromise is the presence of a highly privileged user named "ops".

Regarding the active exploitation of the vulnerability, CERT Polska’s analysis determined that the successful attacks observed so far, including the creation of the "ops" account, originated from the IP address `82.192.72.4` and have been occurring since at least 2 September. In addition, the IP address `103.102.31.18` was used in attempts to exploit the described chain.

The presence of any of these artifacts indicates an attempt to exploit the vulnerabilities and **must be investigated immediately**; at the same time, **the absence of the traces mentioned above does not rule out unauthorized activity**.

## Recommendations

We recommend updating RouterOS immediately to one of the versions containing the fixes: 7.25beta3, 7.24.2, 7.23.4, or 6.49.21. After updating, check the logs for the device compromise message and the value of the flagged marker in the output of the /system/device-mode/print command. Also verify the configuration for unknown users, scripts, and other unrecognized changes. The inspection and further steps should follow MikroTik's security bulletin and the Flagged documentation referenced therein. The absence of the marker does not rule out an earlier compromise.

If the patch cannot be installed immediately, do the following until the update is applied:

- Disable the exposed services or block access to them from all addresses outside trusted management networks. This applies in particular to SSH, WWW/WWW-SSL, and the bandwidth-test server;
- Do not initiate TLS connections from an unpatched device or use the built-in SSH clients (/system ssh and /system ssh-exec), especially when communication passes through untrusted networks or is directed at untrusted hosts.

These are only temporary measures that reduce the attack surface. They do not replace installing the patched RouterOS version.

If the "Flagged" marker, logs, configuration, or other circumstances indicate a possible compromise, the device should be isolated from the network and, before performing a reset, its logs should be secured along with the configuration. Instructions for obtaining this data are described in the CERT Polska article "MikroTik - securing logs and configuration". Information about the observed attack should be reported to the appropriate CSIRT team following their instructions.

After the material has been secured, the device should be restored to factory settings and reconfigured based on a trusted and verified configuration, and the passwords, keys, and other secrets in use should be changed. Do not blindly restore a full configuration backup originating from a potentially compromised device. The "Flagged" marker should not be cleared before the analysis is complete and the material has been secured.

## Research supported by LLMs

The vulnerabilities were discovered by the CERT Polska team using the GPT-5.5-cyber and GPT-5.6-sol models as part of the team's access to the OpenAI Government and Trust Agency Collaboration (GTAC) program.

The models were used as part of an agent-based research environment to automate the laboratory and systematically search for vulnerabilities in areas selected and supervised by the researchers.

The team prepared an isolated laboratory with MikroTik machines, documentation of their system architecture, and rules for safe test execution. The agent automated the creation and restoration of machines, downloading and comparing versions, analyzing RFCs and binary code, and building scripts that confirm the presence of vulnerabilities. Modeling protocols as state machines and checking what happens when a stage is skipped, repeated, or executed in the wrong order proved particularly effective.

This was not, however, the result of a single instruction (prompt). Every hypothesis required confirmation on a real RouterOS system, negative control tests, repetition on a machine in a clean state, and an impact assessment by the researchers. Despite the high degree of automation, the most labor-intensive parts of the project were preparing useful context about RouterOS, designing a safe laboratory and tools, choosing research directions, and then fully verifying the results, eliminating false conclusions, and documenting the real impact of each vulnerability. The models significantly accelerated analysis and hypothesis exploration, but they did not replace these stages.

## Why we are publishing now

We are publishing this information on an accelerated schedule because the patched RouterOS packages are already public, and their comparative analysis has allowed the community to reconstruct some of the fixed bugs. We limit the description to the information administrators need and do not publish exploit code or details that would make automating attacks easier.

The most important recommendation remains to update RouterOS immediately and to verify whether the device contains unknown accounts, scripts, and configuration changes.
