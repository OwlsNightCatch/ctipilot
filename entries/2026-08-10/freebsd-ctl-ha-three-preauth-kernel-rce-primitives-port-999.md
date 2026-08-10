---
schema: 1
kind: vulnerability
horizon: operational
title: "FreeBSD CTL HA — three independent pre-authentication remote kernel-code-execution primitives behind an unauthenticated failover port, and the project's answer is a manpage warning rather than a patch"
headline: "FreeBSD's storage-failover interconnect trusts whatever connects to TCP/999, and three published primitives each reach root from the wire"
summary: >
  FreeBSD's CAM Target Layer runs its High-Availability failover protocol on TCP/999 with no
  authentication of any kind — the kernel trusts whatever connects as its peer controller. Researcher
  Calif published three independent primitives behind that port, each sufficient on its own for a
  root shell from network access alone: an unchecked kernel-pointer dereference giving arbitrary
  read/write off the wire, a second wire-pointer abuse that repoints a handler function pointer, and
  a heap overflow in the scatter-gather copy loop. FreeBSD declined a code fix, adding a manpage
  warning instead on the grounds that the interconnect was never meant to be reachable from an
  untrusted network. No CVE has been assigned, working exploits are public, and the feature ships
  enabled by product design on TrueNAS Enterprise HA clusters.
discovered_at: "2026-08-10T04:42:00Z"
event_date: "2026-08-06"
run_id: 2026-08-10T0411Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, poc-public, no-patch, default-config]
regions: [global, europe]
sectors: [public-sector, energy, healthcare, technology]
entities: []
techniques: [T1210, T1059.004]
affected_products: ["FreeBSD", "TrueNAS Enterprise"]
cves: []
sources:
  - url: "https://blog.calif.io/p/the-taking-of-freebsd-one-two-three"
    publisher: "Calif"
    date: "2026-08-06"
    role: primary
  - url: "https://cgit.freebsd.org/src/commit/?id=3c8f8432"
    publisher: "FreeBSD Project"
    date: "2026-08-05"
    role: primary
closed_sources: []
evidence:
  - quote: "Once it's on, the kernel listens on a TCP port (999 by default) for its peer, with no authentication. Whatever connects is trusted as the second controller."
    publisher: "Calif"
  - quote: "NOTE: HA must be configured only on trusted networks: there is no authentication mechanism built in to the implementation, and the HA protocol effectively permits remote code execution on the peer node."
    publisher: "FreeBSD Project"
verification: multi-source
sourcing_note: >
  The researcher's write-up is the technical primary; FreeBSD's own source commit is an independent
  vendor confirmation, credits the reporter by name, and carries the manpage text quoted here. No CVE
  identifier was assigned by either party — this run confirmed that absence rather than inferring an
  identifier. Neither source states which release branches were tested.
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: network-stack-rce
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Enumerate hosts with kern.cam.ctl.ha_peer configured and confirm the HA interconnect port answers only to the paired controller's address — on TrueNAS Enterprise HA clusters this is enabled by product design, and no patch is coming, so the network path is the whole control."
migrated_from: null
---

**Background.** The CAM Target Layer is FreeBSD's in-kernel iSCSI and SCSI target subsystem — the code that makes a FreeBSD host present block storage to other machines. Its High-Availability mode exists so two controllers can act as one array, exchanging state and in-flight I/O over a private link, and the manpage documenting it carried a March 2017 date line until this disclosure changed it ([FreeBSD Project, 2026-08-05](https://cgit.freebsd.org/src/commit/?id=3c8f8432)). It is not enabled on a stock FreeBSD install — an administrator has to set `kern.cam.ctl.ha_peer` — but it is on by design wherever FreeBSD-derived storage appliances are deployed in a high-availability pair, which is where this matters for critical-infrastructure estates.

The design premise is stated plainly by the researcher: once HA is enabled, "the kernel listens on a TCP port (999 by default) for its peer, with no authentication. Whatever connects is trusted as the second controller." There is no key exchange, no handshake, and no peer validation to fall back on — which means every bug behind that port is reachable pre-authentication by anyone who can route a packet to it.

Three such bugs were reported in March and April 2026, and each is independently sufficient for kernel code execution. The first is an unchecked raw kernel pointer carried in HA data-channel messages: the receiving kernel dereferences a value the wire supplied, yielding arbitrary kernel read and write directly, and the GENERIC kernel ships without kernel address-space layout randomisation, so there is no address guessing to do. The second abuses a different untrusted wire pointer in the data-movement handler to obtain a write-only primitive, and uses it to repoint a handler function pointer — pivoting into the first bug's cleaner write path. The third is a heap overflow in the scatter-gather copy loop, where an unchecked entry count overflows a fixed 64-byte heap buffer into the adjacent allocator object; that one demands real exploitation work — grooming the slab, overwriting a callback pointer, pivoting the stack, and a return-oriented chain to clear the no-execute bit — rather than a single wire write.

What each chain finishes with is the operationally important part. Kernel shellcode creates a process and executes `/bin/sh` connected back to the attacker, and the receive thread is made to exit cleanly, so the machine stays up and serving storage. There is no crash, no panic, and no reboot — the absence of a failure signature is the point.

FreeBSD's response was not a code fix. The project's own commit, authored on 2026-08-04 and merged 2026-08-05, adds a warning to the `ctl.4` manpage stating that "HA must be configured only on trusted networks: there is no authentication mechanism built in to the implementation, and the HA protocol effectively permits remote code execution on the peer node" ([FreeBSD Project, 2026-08-05](https://cgit.freebsd.org/src/commit/?id=3c8f8432)). The maintainers' stated position is that this is a private backchannel between two controllers that was never intended to face an untrusted network, so documentation is the appropriate remedy rather than bounds checks. That is a defensible engineering position and a difficult operational one: it means the exposure is permanent, the mitigation is entirely architectural, and working exploit scripts for all three primitives are published alongside the write-up. No CVE was assigned by either the project or the researchers, so a purely CVE-driven patch or scanning process will not surface this at all.

Detection, telemetry class first. Because every primitive executes in kernel context before any userland process exists, host-based endpoint telemetry has nothing to observe until the chain has already succeeded — the usable signal is network. In flow, connection or firewall telemetry, any session to the configured HA port from a source that is not the paired controller is definitionally illegitimate, since the protocol has no authentication that could make such a connection valid; a two-address allowlist on that port turns detection into a deny-log. After a successful chain, the connect-back is an ordinary outbound session, but its parent lineage is anomalous — a shell created from kernel context rather than descending from any expected service manager — which only kernel-level instrumentation will resolve. **Triage:** legitimate HA traffic on this port is continuous, bidirectional and between exactly two known addresses, so volume and content look unremarkable; the discriminator is purely the peer address, which is why an allowlist rather than a signature is the control that works. **Defender takeaway:** treat the interconnect as an unauthenticated root shell that happens to speak a storage protocol. Put it on a dedicated non-routable segment reaching only the paired controller, verify that TrueNAS Enterprise HA deployments follow the vendor's separate-interconnect guidance rather than sharing a management or production VLAN, and do not enable `kern.cam.ctl.ha_peer` on hosts that are not actually running failover. There is no patch to wait for.
