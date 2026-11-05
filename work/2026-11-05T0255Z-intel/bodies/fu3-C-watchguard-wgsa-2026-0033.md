---
title: Linux Kernel IPv4 Use-After-Free Vulnerability (CVE-2026-98432)
url: https://psirt.watchguard.com/WGSA-2026-0033/
hostname: watchguard.com
sitename: psirt.watchguard.com
date: "2026-11-03"
fingerprint: a523795ec8a0de85
---
[#](https://psirt.watchguard.com/WGSA-2026-0033/)

# Linux Kernel IPv4 Use-After-Free Vulnerability (CVE-2026-98432)

## Summary [#](https://psirt.watchguard.com#summary)

A use-after-free vulnerability, tracked as CVE-2026-98432, was disclosed in the IPv4 networking code of the Linux kernel. The kernel frees IP option structures right away while other kernel code may still be reading them. That can cause memory corruption when the kernel builds TCP SYN-ACK responses for pending connections, or when it moves pending connections between sockets. Connection migration is used when net.ipv4.tcp\_migrate\_req=1 is set or a BPF reuseport program is attached. A remote unauthenticated attacker can trigger memory corruption, kernel crash, and potential remote code execution (RCE) by sending specially crafted IPv4 TCP packets.

WatchGuard has investigated and found the following products run a vulnerable version of the Linux Kernel and are potentially affected by CVE-2026-98432: - Firebox Fireware OS - WatchGuard AP - Dimension

While Fireware OS and WatchGuard AP run vulnerable versions of the Linux kernel, they do not enable MPTCP and are not affected by the remote code execution (RCE) exploit chain circulating online.

WatchGuard Dimension runs on a vulnerable version of the Ubuntu operating system but without MPTCP enabled. We will update this advisory when a fix is available from Ubuntu.

## CVE identifiers [#](https://psirt.watchguard.com#cves)

| CVE ID | Description | CVSS | 
|---|---|---|
| [CVE-2026-98432](https://www.cve.org/CVERecord?id=CVE-2026-98432) | In the Linux kernel, the following vulnerability has been resolved: ipv4: free inet\_opt and ireq\_opt after an RCU grace period tcp\_v4\_syn\_recv\_sock() transfers ownership of ireq->ireq\_opt to the child socket (newinet->inet\_opt) without copying it. Another cpu can concurrently process a retransmitted SYN for the same request socket, and send a SYNACK from tcp\_check\_req(). tcp\_v4\_send\_synack() and inet\_csk\_route\_req() read ireq->ireq\_opt under rcu\_read\_lock() only, and ip\_build\_and\_send\_pkt() and ip\_options\_build() then read opt->optlen twice. Note that the SYNACK timer itself is not an issue: it holds a reference on its request socket, and inet\_csk\_reqsk\_queue\_drop() calls timer\_delete\_sync() before the child can be freed. Since commit 079096f103fa ("tcp/dccp: install syn\_recv requests into ehash table"), request sockets are processed without holding the listener lock, so nothing prevents the child socket from being freed while the SYNACK is still being built. TCP child sockets do not have SOCK\_RCU\_FREE, and inet\_sock\_destruct() frees inet\_opt with a plain kfree(), leading to a use-after-free in ip\_options\_build(). A similar issue exists with request socket migration (net.ipv4.tcp\_migrate\_req=1, or a BPF\_SK\_REUSEPORT\_SELECT\_OR\_MIGRATE program). reqsk\_timer\_handler() clones the request socket with inet\_reqsk\_clone(), so that the old request socket and its clone share the same ireq\_opt, then reqsk\_migrate\_reset() clears the pointer in the old one. Another cpu holding a reference on the old request socket can still be using these options (sending a SYNACK, or creating a child in tcp\_v4\_syn\_recv\_sock()) when the clone is freed, and tcp\_v4\_reqsk\_destructor() also uses a plain kfree(). Readers already use RCU, and other paths replacing inet\_opt (do\_ip\_setsockopt(), cipso\_v4\_sock\_setattr()...) already use kfree\_rcu(). Use kfree\_rcu() in inet\_sock\_destruct() and tcp\_v4\_reqsk\_destructor() as well. IPv6 is not affected by the first issue, because tcp\_v6\_syn\_recv\_sock() duplicates the options. tcp\_v6\_reqsk\_destructor() has the same migration issue with ipv6\_opt, which is only set by CALIPSO. This will be addressed in a separate patch. | 9.8 | 

## Product status [#](https://psirt.watchguard.com#products)

| Product | Affected | Not affected | 
|---|---|---|
| Dimension | >= 2.0 | — | 
| Fireware OS |  |  | 
| Default | 2025.1, >= 12.0 | — | 
| WatchGuard AP | >= 1.0 | — | 

## Solution [#](https://psirt.watchguard.com#solution)

| Product | Status | Resolved Version | 
|---|---|---|
| Firebox Fireware OS | Potentially Affected | Unresolved | 
| WatchGuard AP | Potentially Affected | Unresolved | 
| Dimension | Potentially Affected | Unresolved |
