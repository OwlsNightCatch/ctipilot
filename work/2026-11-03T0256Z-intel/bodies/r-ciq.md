# extract: served via trafilatura-direct
---
title: Mitigating CVE-2026-98432 on Rocky Linux 8, 9, 10, and LTS Variants
url: https://kb.ciq.com/article/security-advisories/cve-2026-98432-mitigation
hostname: ciq.com
description: CVE-2026-98432 is a use-after-free vulnerability in the Linux kernel's IPv4 TCP connection setup path (net/ipv4/afinet.c and net/ipv4/tcpipv4.c), published on…
sitename: CIQ Knowledge Base
date: "2026-10-30"
tags: ['cve', 'security', 'kernel', 'rocky linux', 'lts', 'mitigation', 'troubleshooting']
fingerprint: a7b1191259a273a7
---
## Introduction

CVE-2026-98432 is a use-after-free vulnerability in the Linux kernel's IPv4 TCP connection setup path (`net/ipv4/af_inet.c` and `net/ipv4/tcp_ipv4.c`), published on 2026-10-15.

An unauthenticated network peer can start the flaw by sending TCP SYN packets that carry IPv4 options.

This article shows you how to check whether a kernel is fixed, how to apply and remove a verified firewall rule that blocks the reachable path, and how to confirm the fix once a patched kernel ships.

It covers RLC Pro 8, 9, and 10, RLC Pro LTS 8.6, LTS 9.2, and LTS 9.6, and RLC Pro FIPS 8.6, 8.10, 9.2, and 9.6.

Patched CIQ kernels are available for all variants listed in the Patched Kernels table below.

For Rocky Linux community releases, refer to [Rocky Linux Errata](https://errata.build.resf.org/) for patched kernel availability.

The mitigation commands in this article were run and observed on RLC Pro LTS 9.6 (`5.14.0-570.60.1+26.1.el9_6_ciq`), RLC Pro LTS 8.10 (`4.18.0-553.176.1+2.1.el8_10_ciq`), RLC Pro 10 (`6.12.0-211.66.1+2.1.el10_2_ciq`), and stock Rocky Linux 9.6, 8.10, and 10.2, each with firewalld running.

## Problem

The two IPv4 destructors `inet_sock_destruct()` and `tcp_v4_reqsk_destructor()` free the stored IP options (`inet_opt` and `ireq_opt`) with a plain `kfree()` while the object can still be reachable to readers through RCU.

A retransmitted SYN or the syncookie ACK path can touch the freed options structure, which is a use-after-free.

The upstream advisory describes the impact as a system crash leading to a denial of service or potential memory corruption.

The kernel.org CNA record's scenario also lists information disclosure and out-of-bounds writes, so the two sources describe the impact differently.

The kernel.org CNA scores the CVE 9.8 (critical) with attack complexity low.

Upstream rates it 8.1 (important) with attack complexity high.

NVD shows only the 9.8 score from the CNA and has not published its own score.

Both scores are at or above the CVSS 7 threshold the [CIQ CVE FAQ](https://kb.ciq.com/article/general/cve-faq) names for remediation focus, and the same FAQ states that CIQ does not provide SLAs for CVE remediation.

Anthropic's Frontier Red Team post describes a proof-of-concept exploit, written with Claude, that sends packets to Linux servers exposing a multipath TCP (MPTCP) listener and runs arbitrary commands as root without credentials or user interaction.

That post describes the race as retryable, with a lost race failing only the handshake, and reports a proof of concept that needed 48 minutes to leak a kernel pointer and about five more minutes to reach command execution.

The Go team's announcement of the same CVE states that the demonstrated exploit requires an MPTCP listener while the underlying bug is not specific to MPTCP, and Go issue 82717 states it is currently unknown whether the vulnerability is strongly related to MPTCP.

The CVE records themselves (the kernel.org CNA mbox and the cve.org entry) contain no MPTCP wording.

This article documents the update path for the patched variants and an interim mitigation that was recommended before the fix shipped.

## Status

- **Patched kernels are available** for all CIQ variants listed in the Patched Kernels table.
- **Recommended action:** install the patched kernel with the update command in the Resolution section, reboot, and remove the interim mitigation.
- **Do not disable MPTCP alone:** with `net.mptcp.enabled=0` the vulnerable code path in plain TCP traffic stays reachable, which the testing in the Notes section shows.
- Upstream lists the Red Hat Enterprise Linux 8, 9, and 10 `kernel` packages as affected and the Red Hat Enterprise Linux 6 and 7 `kernel` packages as not affected.
- **Open a support case** if you need help confirming exposure across a fleet or tracking patch availability for a variant not listed below.

## Patched Kernels

| Variant | Patched Kernel Version | Released | 
|---|---|---|
| [RLC Pro 8](https://ciq.com/products/rocky-linux/pro/) | `kernel-4.18.0-553.178.1+2.1.el8_10_ciq` | 2026-11-01 | 
| [RLC Pro LTS 8.6](https://ciq.com/services/long-term-support/) | `kernel-4.18.0-372.32.1+40.1.el8_6_ciq` | 2026-10-31 | 
| [RLC Pro FIPS 8.6](https://ciq.com/products/rocky-linux/pro/) | `kernel-4.18.0-553.178.1+2.1.el8_6.ciqfips` | 2026-11-01 | 
| [RLC Pro FIPS 8.10](https://ciq.com/products/rocky-linux/pro/) | `kernel-4.18.0-553.178.1+2.1.el8_10_ciq` | 2026-11-01 | 
| [RLC Pro 9](https://ciq.com/products/rocky-linux/pro/) | `kernel-5.14.0-687.60.1+2.1.el9_8_ciq` | 2026-11-01 | 
| [RLC Pro LTS 9.2](https://ciq.com/services/long-term-support/) | `kernel-5.14.0-284.30.1+45.1.el9_2_ciq` | 2026-10-31 | 
| [RLC Pro LTS 9.6](https://ciq.com/services/long-term-support/) | `kernel-5.14.0-570.60.1+27.2.el9_6_ciq` | 2026-10-31 | 
| [RLC Pro FIPS 9.2](https://ciq.com/products/rocky-linux/pro/) | `kernel-5.14.0-284.30.1+45.1.el9_2_ciq` | 2026-10-31 | 
| [RLC Pro FIPS 9.6](https://ciq.com/products/rocky-linux/pro/) | `kernel-5.14.0-570.60.1+27.2.el9_6_ciq` | 2026-10-31 | 
| [RLC Pro 10](https://ciq.com/products/rocky-linux/pro/) | `kernel-6.12.0-211.68.1+2.1.el10_2_ciq` | 2026-11-01 | 

The Released dates are the kernel build dates read from the RPMs in the CIQ depot.

For Rocky Linux community releases, refer to [Rocky Linux Errata](https://errata.build.resf.org/) for patched kernel availability.

Confirm what a system is running with:

```
uname -r
```
Only the builds listed in this table were verified to carry the fix.

A kernel newer than the listed version was not verified, so check your vendor advisory and run the changelog check in the Verification section to confirm whether the fix is present.

## Resolution

On the patched variants, install the patched kernel and reboot:

```
sudo dnf update kernel*
sudo reboot
```
Confirm the running kernel matches the patched version in the Patched Kernels table, run the changelog check in the Verification section, and then remove the interim mitigation if you applied it.

### Remove the interim rule

If you loaded only the interim rule, remove it with one command:

```
sudo nft delete table inet ciq_cve_2026_98432
```
### Remove the persistent version

This block disables the unit, removes both files, and reloads systemd:

```
sudo systemctl disable --now ciq-cve-2026-98432-nft.service
sudo rm -f /etc/systemd/system/ciq-cve-2026-98432-nft.service /etc/nftables/ciq-cve-2026-98432.nft
sudo systemctl daemon-reload
```
Running the interim removal and then this block, in that order, leaves no failed unit behind.

## Mitigation

The rule in this section drops every IPv4 TCP packet whose header is longer than 20 bytes, which is exactly the packets that carry IPv4 options, before the TCP stack processes them.

The vulnerable `ireq_opt` object is only created when a SYN packet, or the ACK of the syncookie path, carries IP options, so dropping those packets removes the reachable path.

*⚠️ WARNINGThis rule changes live firewall state and drops legitimate TCP traffic that carries IP options, so test it on one non-production host first.*

*ℹ️ NOTEUse straight double quotes in the chain line exactly as printed.*

### Check whether MPTCP is enabled

MPTCP is disabled by default on the tested kernels, and the demonstrated exploit described by Anthropic requires an MPTCP listener:

```
sysctl net.mptcp.enabled
```
The output `net.mptcp.enabled = 0` means MPTCP is off, and a result of `1` means listeners may negotiate MPTCP, which matters for software built with Go 1.24 or newer, because Go programs enable MPTCP by default for listen sockets on Linux.

### Interim rule, loaded now

Run these three commands to load the rule immediately, without persistence:

```
sudo nft add table inet ciq_cve_2026_98432
sudo nft add chain inet ciq_cve_2026_98432 prerouting "{ type filter hook prerouting priority -300; policy accept; }"
sudo nft add rule inet ciq_cve_2026_98432 prerouting ip hdrlength gt 5 meta l4proto tcp counter drop
```
The rule lives in its own table, so `firewall-cmd --reload` and `systemctl restart firewalld` leave it in place.

### Persistent version

This block writes its own nftables file and its own oneshot systemd unit, checks the file with `nft -c`, and enables the unit so the rule loads at boot before the network comes up:

```
sudo tee /etc/nftables/ciq-cve-2026-98432.nft >/dev/null <<'EOF'
add table inet ciq_cve_2026_98432
delete table inet ciq_cve_2026_98432
table inet ciq_cve_2026_98432 {
  chain prerouting {
    type filter hook prerouting priority -300; policy accept;
    ip hdrlength gt 5 meta l4proto tcp counter drop
  }
}
EOF
sudo tee /etc/systemd/system/ciq-cve-2026-98432-nft.service >/dev/null <<'EOF'
[Unit]
Description=Drop IPv4 TCP packets that carry IP options (interim mitigation for CVE-2026-98432)
Wants=network-pre.target
Before=network-pre.target
[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/sbin/nft -f /etc/nftables/ciq-cve-2026-98432.nft
ExecStop=-/usr/sbin/nft delete table inet ciq_cve_2026_98432
[Install]
WantedBy=multi-user.target
EOF
sudo nft -c -f /etc/nftables/ciq-cve-2026-98432.nft
sudo systemctl daemon-reload
sudo systemctl enable --now ciq-cve-2026-98432-nft.service
```
The file starts by deleting the table and recreating it, so applying the persistent block after the interim block leaves exactly one rule.

The leading dash in `ExecStop=-` tells systemd to ignore a failing stop command, which keeps the unit from ending in a failed state when the table was already removed.

*ℹ️ NOTE**Save each multi-line block to a file and run it with `bash` instead of pasting it into a terminal.*

### Confirm the rule is loaded

For either installation option, this command prints the table with its chain at `priority raw` (nft displays the `-300` priority that way) and a counter rule:

```
sudo nft list table inet ciq_cve_2026_98432
```
If you installed the persistent version, also confirm the unit prints `active`.

The interim rule creates no unit, so skip this check for the interim rule alone:

```
systemctl is-active ciq-cve-2026-98432-nft.service
```
### Restoring the rule after nftables.service runs

The shipped `nftables.service` flushes the ruleset when it stops and removes this table with it.

*⚠️ WARNING**Running `systemctl start nftables` and then `systemctl stop nftables` removes the mitigation table while this unit still reports `active`.*

That behavior was observed on stock Rocky Linux 9.6, 8.10, and 10.2 and on RLC Pro LTS 9.6, and the rule and its drop behavior came back after restarting the unit:

```
sudo systemctl restart ciq-cve-2026-98432-nft.service
```
## Verification

Confirm the running kernel, the MPTCP default, and the rule after a reboot:

```
uname -r
sysctl net.mptcp.enabled
sudo nft list table inet ciq_cve_2026_98432
systemctl is-active ciq-cve-2026-98432-nft.service
```
On RLC Pro LTS 9.6 and RLC Pro 10, `ss -Mltn` shows a `Netid` column and lists both `tcp` and `mptcp` rows for an MPTCP listener, and on RLC Pro LTS 8.10 the same command showed only the `tcp` row in testing, so `sysctl net.mptcp.enabled` is the MPTCP check that works there.

Check the running kernel's changelog for the fix, where the first line must print `0` until a fixed kernel is running and the second must print more than `0`, or the check proves nothing:

```
rpm -q --changelog kernel-core-$(uname -r) | grep -c CVE-2026-98432
rpm -q --changelog kernel-core-$(uname -r) | grep -c CVE-20
```
The control is `CVE-20` and not the full CVE identifier, and the control must print more than 0, or the check proves nothing.

A changelog result alone is not proof that a fix is present, so also confirm the running version against the Patched Kernels table and the CIQ advisory when it appears.

The nft table and the `net.mptcp.enabled` sysctl apply to the host's own network namespace, which is known from reading the kernel source and was not tested in containers or across forwarded traffic.

## Root Cause

The vulnerability was introduced in kernel 4.4 by commit `079096f103fa`, which moved IP option ownership between request sockets and child sockets, and the two destructors kept the plain `kfree()` calls.

The upstream fix is commit `e3f33b0a1d89d738e2b913dab519226eaf76e15b`, which replaces `kfree` with `kfree_rcu` in `inet_sock_destruct()` and `tcp_v4_reqsk_destructor()`, so the free waits for an RCU grace period.

The same fix was backported to stable series 5.10.272, 5.15.223, 6.1.190, 6.6.159, 6.12.113, 6.18.56, and 7.2.10.

The commit message states IPv6 is not affected by the first issue, and that the matching `ipv6_opt` path, which only CALIPSO sets, will be addressed in a separate patch.

## Notes

- **The rule is not a complete fix.** Testing sent Record Route and Timestamp options from a second host on the same network, and other option types fall under the `ip hdrlength gt 5` match by construction, but IPv6, fragmented packets, and other delivery paths were not tested, and the CPU cost was not measured.
- **Disabling MPTCP is not enough.** With `net.mptcp.enabled=0` read back, a plain TCP listener on every tested kernel still answered a SYN carrying a Record Route option and echoed the option in the SYN-ACK.
- **The syncookie path is covered.** With `net.ipv4.tcp_syncookies=2`, a cookie ACK carrying a Record Route option was dropped by the rule as well.
- **The unit owns its files.** `/etc/nftables` is mode 700 and owned by root on the tested systems, so list it with `sudo ls` if you need to.
- **CISA KEV.** The CISA Known Exploited Vulnerabilities catalog (version 2026.10.29) held no entry for this CVE as of 2026-10-30.
- **After installing the fix.** Install the patched kernel for your variant with `sudo dnf update kernel*`, reboot, confirm `uname -r`, run the changelog check in Verification, and then remove the rule with the removal blocks above.
