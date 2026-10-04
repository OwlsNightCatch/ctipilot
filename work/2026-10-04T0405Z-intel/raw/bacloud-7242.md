---
title: MikroTik RouterOS 7.24.2 Released – Critical Security Patch, Update ASAP!
url: https://www.bacloud.com/en/blog/316/mikrotik-routeros-7.24.2-released--critical-security-patch-update-asap.html
hostname: bacloud.com
description: MikroTik on September 3, 2026, issued RouterOS 7.24.2 (stable/testing) and 7.23.4 (long-term) as “important security updates”. The company warns that while “most configurations are not at risk,...
sitename: Bacloud.com
date: "2026-09-03"
---
MikroTik on September 3, 2026, [issued](https://forum.mikrotik.com/t/7-24-2-stable-is-released/272800?) RouterOS 7.24.2 (stable/testing) and 7.23.4 (long-term) as “important security updates”. The company warns that while “most configurations are not at risk,” *“upgrading is highly recommended”*. In fact, MikroTik deliberately withholds the vulnerability details for now (“to give time to update your systems, we are not currently publishing detailed information”) – a common security practice. In short, assume the worst: these fixes are urgent and should be applied immediately. As one [MikroTik engineer put it](https://forum.mikrotik.com/t/7-23-4-long-term-is-released/272801), “Some fixes are critical. Every hour of delay is another hour of exposing your devices to risks.”

[Check out Bacloud services](https://www.bacloud.com/en)

Update: [CERT Polska](https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve/) has now disclosed additional details about the security issues addressed by MikroTik’s recent RouterOS updates. Researchers identified six vulnerabilities, including two critical flaws that can be combined in an attack chain named “MikroTrick.” This combination can allow an unauthenticated attacker to bypass SSH authentication and potentially gain full control of a MikroTik device when its SSH service is exposed to the Internet. CERT Polska also confirmed that these vulnerabilities are already being actively exploited in real-world attacks. Administrators are strongly advised to upgrade immediately to a patched release, including RouterOS 7.24.2, 7.23.4, 6.49.21, or 7.25 beta 3, and review router configurations and logs for unknown users, scripts, or other signs of compromise.

## Key Fixes and Improvements

The 7.24.2 [release notes](https://mikrotik.com/download/changelogs?channelFilter=testing) list numerous fixes across routing, networking, and management components. Highlights include:

- BGP (routing): Fixed a bug where BGP link-local next-hops were unreachable over a VRF, and a crash when disabling an unnumbered interface.
- SSH / Management: Internal SSH processes were refactored for security and stability, suggesting a patch to the SSH service. (This fuels speculation that the hidden vulnerability may involve a remote management interface.)
- Certificate Store: Corrected an issue with the built-in trust store setting (introduced in v7.22.2).
- DHCP & Networking: Improved DHCP server handling stability and added an IPv6 neighbor-discovery ping function.
- Hardware Interfaces: Resolved multiple hardware issues – e.g., LED indicators now light correctly when an interface is active, the RG650E-EU LTE modem link-up bug is fixed, and missing PoE‑Out ports on several models are restored.
- System & Services: General stability enhancements for container image extraction, SMB disk shares, Ethernet (especially hAP be³ Media), and the TFTP client. The console subsystem has a memory-leak fix for background scripts. WebFig and Winbox UI tools also received stability fixes (including a spelling correction in a Winbox label).

Each of these fixes improves both reliability and security. In particular, the SSH refactor and certificate fixes point to the kind of service that could be targeted by attackers. (Recall that earlier in July, RouterOS 7.23.2 patched a serious PPP service flaw – [CVE-2026-59108](https://www.penligent.ai/hackinglabs/cve-2026-59108/) – that could allow data leaks or code execution.) Regardless of the unknown flaw, administrators should assume any remotely accessible service might have been at risk. To be safe, double-check that Winbox, SSH and HTTP management services are firewalled or limited to trusted hosts, as recommended in MikroTik’s documentation.

## Upgrade Recommendations

[MikroTik urges](https://forum.mikrotik.com/t/7-24-2-stable-is-released/272800?) operators to upgrade ASAP. Normis (lead developer) stressed that 7.23.4/7.24.2 *“only contains important fixes”* and urged rapid updates. In practice, that means scheduling the RouterOS upgrade at the next maintenance window. Always start by backing up your configuration (e.g. `/export` and `/system backup save`). Then use System ▶ Packages ▶ Check For Updates (stable or long-term channel as appropriate) to download and install v7.24.2 (or v7.23.4). Reboot the router when prompted.

After patching, verify the new version with `/system resource print`. Also apply any available RouterBOOT firmware update (`/system routerboard upgrade`) and reboot again. Finally, confirm all interfaces and services are functioning normally.

While the patch is short (the system usually reboots in seconds), the risk of not updating is high. As noted, delaying leaves your device vulnerable. In the meantime, follow MikroTik’s best practices: restrict management access (block Winbox/SSH/WWW from the Internet, allow only trusted IPs), use strong passwords, and monitor logs for unusual login attempts. These measures help mitigate any unknown exposure until the update is applied.


## Conclusion

RouterOS 7.24.2 is a critical security update for all [MikroTik](https://www.bacloud.com/mikrotik-vps-hosting-services) routers on the v7 branch. Although most default setups may not be directly vulnerable, the flaw's undisclosed nature means everyone should update promptly. The release simultaneously updates both the stable and long-term lines (7.24.2 and 7.23.4) with the same security fixes. Don’t wait – upgrade to the latest version today, keep your devices protected, and always follow MikroTik’s guidance to stay up to date and to shield management services behind a firewall.

Sources: Official MikroTik announcements and support resources, plus community analysis.
