---
title: "VSA-2026-056: ipv4 - free inet_opt and ireq_opt after an RCU grace period (CVE-2026-98432) | Vates VMS Documentation"
url: https://docs.vates.tech/security-advisories/advisories/2026/vates-sa-2026-056
hostname: vates.tech
description: "2026-11-03 / Critical severity / XCP-ng 8.3 and Xen Orchestra Appliance affected, an adversary can take over Dom0 through a use-after-free in the kernel IPv4 TCP connection handling."
sitename: docs.vates.tech
date: "2026-11-04"
categories: ['2026', 'Previous 2026']
fingerprint: e586e93ddcb0d256
---
# VSA-2026-056: ipv4 - free inet\_opt and ireq\_opt after an RCU grace period (CVE-2026-98432)

| **Published** | **Updated** | **Severity** | **CVSS 4.0** | **Affected products** | 
|---|---|---|---|---|
| 2026-11-03 | 2026-11-04 | ⚫ Critical | Not available yet | - XCP-ng 8.3 / Xen Orchestra Appliance | 

A use-after-free vulnerability has been disclosed in the Linux kernel's IPv4 TCP connection handling (CVE-2026-98432), together with a public exploit that achieves remote code execution. For Vates products, we classify the impact as **Critical**. For details on how we assign severity levels, see our [Severity Levels Explained page](https://docs.vates.tech/security-advisories/security#severity-levels).

## Summary[](https://docs.vates.tech#summary)

CVE-2026-98432 is a use-after-free in the kernel's IPv4 TCP connection handling. `tcp_v4_syn_recv_sock()` transfers ownership of `ireq->ireq_opt` to the child socket (`newinet->inet_opt`) without copying it. Another CPU can concurrently process a retransmitted SYN for the same request socket and send a SYNACK from `tcp_check_req()`. `tcp_v4_send_synack()` and `inet_csk_route_req()` read `ireq->ireq_opt` under `rcu_read_lock()` only, and `ip_build_and_send_pkt()` and `ip_options_build()` then read `opt->optlen` twice.

Since commit 079096f103fa ("tcp/dccp: install syn\_recv requests into ehash table"), request sockets are processed without holding the listener lock, so nothing prevents the child socket from being freed while the SYNACK is still being built. TCP child sockets do not have `SOCK_RCU_FREE`, and `inet_sock_destruct()` frees `inet_opt` with a plain `kfree()`, leading to a use-after-free in `ip_options_build()`.

## Impact[](https://docs.vates.tech#impact)

An adversary who can send crafted TCP traffic (options in IPV4 header length) on the host can trigger a use-after-free (UAF), which can lead to arbitrary code execution with kernel privileges in Dom0 or Xen Orchestra Appliance operating system. A compromise of Dom0 results in full compromise of the host system, including all guest domains. Also, a compromise of Xen Orchestra Appliance results in full compromise of management stack and therefore of all managed pools.

A public exploit has been published by Anthropic. It leverages an MPTCP listener to achieve remote code execution. The underlying bug is not specific to MPTCP but the exploit does not affect XCP-ng.

## Status[](https://docs.vates.tech#status)

- Released

## Affected Versions[](https://docs.vates.tech#affected-versions)

- **XCP-ng 8.3:** Affected.
- **Xen Orchestra Appliance**: Affected.

## Mitigation[](https://docs.vates.tech#mitigation)

If Global Private Network (GPN) are used after modifying iptables rules, it will save in /etc/sysconfig/iptables and persist in the configuration

Interim mitigations have been published by other Linux distributions, for example by AlmaLinux that drop inbound TCP packets that carry IPv4 options with an nftables rule.

The rule drops every incoming IPv4 TCP packet whose header contains IP options. It reads the IHL field (IPv4 header length, in 32-bit words) and matches values 6 to 15 (a standard IPv4 packet has an IHL of 5) meaning any header longer than the standard 20 bytes. It sits in the raw table PREROUTING chain. So, packets are dropped before connection tracking and before the kernel parses the options.

**Without IP options, the vulnerable code path cannot be reached.**

### XCP-ng[](https://docs.vates.tech#xcp-ng)

```
iptables -t raw -I PREROUTING -p tcp -m u32 --u32 "0>>24&0xF=6:15" -j DROP
```
Once the instructions in the Resolution section have been applied, you may remove the iptables rule if it exists in `/etc/sysconfig/iptables`. (Note: If GPN is not in use, this rule is non-persistent after a reboot).

```
iptables -t raw -D PREROUTING -p tcp -m u32 --u32 "0>>24&0xF=6:15" -j DROP
sed -i '/6:15/d' /etc/sysconfig/iptables
```
### Xen Orchestra Appliance[](https://docs.vates.tech#xen-orchestra-appliance)

```
sudo nft -f - <<'EOF'
add table ip cve_2026_98432
delete table ip cve_2026_98432
table ip cve_2026_98432 {
    chain prerouting {
        type filter hook prerouting priority -300; policy accept;
        meta l4proto tcp ip hdrlength > 5 counter drop
    }
}
EOF
```
Once the instructions in the Resolution section have been applied, you may remove the nftables rule.

```
sudo nft delete table ip cve_2026_98432
```
## Resolution[](https://docs.vates.tech#resolution)

A reboot is required for the updated kernel to take effect on XCP-ng and Xen Orchestra Appliance.

As of 2026-11-03, the `kernel` package for XCP-ng 8.3 have been updated to address this issue. In Xen Orchestra Appliance, the `linux` package is handled by `unattended-upgrades`.

List of packages fixing this issue:

- **XCP-ng 8.3**:
  - `kernel-4.19.19-8.0.46.14.xcpng8.3`
- **Xen Orchestra Appliance**:
  - `6.1.190-1`

## Credits[](https://docs.vates.tech#credits)

This issue was discovered by Anthropic using Claude.
