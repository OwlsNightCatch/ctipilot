---
schema: 1
kind: research
horizon: operational
title: "NatJack — sharing a NAT table is a trust relationship nobody declared: five named primitives against NAT state, of which only the downstream TCP hijack got a CVE on each platform"
headline: "Every evaluated NAT implementation fell to at least one primitive, and the Linux change is explicitly a partial mitigation rather than a fix"
summary: >
  NatJack, presented at Black Hat USA 2026, is an attack class against an unstated assumption in
  network address translation — that devices sharing a NAT table can trust one another. The research
  names five primitives: TCP session hijack by downstream spoofing, the same hijack coordinated with
  an upstream attacker-controlled server, DNS response hijack, disclosure of a victim's externally
  mapped address and port, and NAT-table exhaustion. Two CVEs were assigned and both name the
  downstream-spoofing hijack specifically — CVE-2026-56181 in Windows NAT affecting Hyper-V, and
  CVE-2026-63913 in the Linux netfilter connection-tracking state machine. The researcher records the
  Linux change as "not a complete fix" that increases attack complexity, and the other three
  primitives carry no identifier and no vendor fix at all.
discovered_at: "2026-08-10T04:57:00Z"
event_date: "2026-08-06"
run_id: 2026-08-10T0411Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, cloud, patch-available, info-disclosure, dos]
regions: [global, europe]
sectors: [public-sector, technology, telco]
entities: [trend:natjack-nat-trust-assumption-attack-class]
techniques: [T1557, T1498.001]
affected_products: ["Microsoft Windows NAT", "Microsoft Hyper-V", "Linux kernel netfilter"]
cves:
  - id: CVE-2026-56181
    cvss: "8.3"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Windows Server 2025; Windows 11 24H2, 25H2, 26H1"
    fixed: "July 2026 security update"
  - id: CVE-2026-63913
    cvss: null
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [mitigation-only]
    affected: "Linux kernel netfilter connection tracking, prior to the fixed releases"
    fixed: "Linux 7.1 plus seven stable and long-term point releases — a partial mitigation, not a complete fix"
sources:
  - url: "https://natjack.io/"
    publisher: "Malcolm Stagg"
    date: "2026-08-06"
    role: primary
  - url: "https://go.synack.com/security-research/natjack"
    publisher: "Synack Red Team"
    date: "2026-08-06"
    role: primary
  - url: "https://lore.kernel.org/linux-cve-announce/2026071946-CVE-2026-63913-9646@gregkh/T/#u"
    publisher: "Linux kernel CVE team"
    date: "2026-07-19"
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-56181"
    publisher: "Microsoft Security Response Center"
    date: "2026-07-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Certain network address translation (NAT) implementations allow downstream attackers to manipulate NAT table state entries in a manner that enables TCP session hijacking through downstream IP spoofing."
    publisher: "Malcolm Stagg"
  - quote: "CVE-2026-63913: Linux Kernel Netfilter (fixing a code flaw and applying a mitigation for the downstream spoofing attack) applied in Linux kernel 7.1 and higher. This is not a complete fix but does increase attack complexity."
    publisher: "Malcolm Stagg"
  - quote: "Origin validation error in Windows Network Address Translation (NAT) allows an unauthorized attacker to perform spoofing over an adjacent network."
    publisher: "Microsoft Security Response Center"
  - quote: "An unintended behavior in the TCP conntrack state machine allows a\nconnection to be forced into the CLOSE state using an RST packet with an\ninvalid sequence number."
    publisher: "Linux kernel CVE team"
verification: multi-source
sourcing_note: >
  The per-flaw CVE mapping was taken from the researcher's own explicit statement rather than
  inferred by pairing two identifiers against two platforms — both CVEs name the downstream-spoofing
  TCP-hijack primitive, one per platform. Affected and fixed versions come from Microsoft's own
  structured advisory record and the Linux kernel CVE announcement respectively, not from the
  research write-up; the CVSS for CVE-2026-56181 is Microsoft's own score. The Linux identifier is
  recorded as mitigation-only because the researcher states plainly that the change is not a complete
  fix. The five-primitive count is the source's own enumeration.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Identify environments where workloads of different trust levels share one NAT table — multi-tenant Hyper-V hosts, container nodes running mixed-trust workloads, shared cloud NAT gateways — and separate them; the Windows update closes its hijack path, but the Linux change is a partial mitigation and the other three primitives have no fix at all."
migrated_from: null
---

Network address translation carries an assumption almost nobody has written down: that the devices sharing a NAT table are peers who can be trusted not to interfere with each other's entries. NatJack, presented by an independent researcher working with the Synack Red Team at Black Hat USA 2026, is a systematic attack on that assumption, and independent testing found every evaluated NAT implementation vulnerable to at least one of its primitives ([Malcolm Stagg, 2026-08-06](https://natjack.io/), [Synack Red Team, 2026-08-06](https://go.synack.com/security-research/natjack)).

The research enumerates five named primitives. The first is the one that got the identifiers: "Certain network address translation (NAT) implementations allow downstream attackers to manipulate NAT table state entries in a manner that enables TCP session hijacking through downstream IP spoofing." An attacker sharing the NAT table removes or replaces the mapping for a victim's live TCP connection and redirects that traffic to itself, allowing impersonation, traffic injection, session termination and limited interception. The second is the same hijack coordinated with an attacker-controlled server upstream, which needs prior knowledge of the victim's externally mapped port — supplied conveniently by the fourth primitive, a disclosure of exactly that address and port. The third applies the mapping manipulation to DNS query and response pairs, and the fifth exhausts the NAT table outright.

Two CVEs were assigned, and the mapping between them and the flaws is explicit rather than inferred: both name the downstream-spoofing TCP hijack, one per platform. CVE-2026-56181 is Microsoft's, covering Windows NAT and affecting Hyper-V — Microsoft's own record describes an "Origin validation error in Windows Network Address Translation (NAT) allows an unauthorized attacker to perform spoofing over an adjacent network", scores it 8.3 and rates it Moderate, fixed in the July 2026 update across Windows Server 2025 and Windows 11 24H2 through 26H1 ([Microsoft Security Response Center, 2026-07-14](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-56181)). CVE-2026-63913 is the Linux kernel's, where the announcement states that "An unintended behavior in the TCP conntrack state machine allows a connection to be forced into the CLOSE state using an RST packet with an invalid sequence number", addressed in 7.1 and seven stable and long-term point releases ([Linux kernel CVE team, 2026-07-19](https://lore.kernel.org/linux-cve-announce/2026071946-CVE-2026-63913-9646@gregkh/T/#u)).

Two qualifications change what patching actually buys, and both come from the researcher rather than from either vendor. The Linux change is not a fix: it is recorded as "CVE-2026-63913: Linux Kernel Netfilter (fixing a code flaw and applying a mitigation for the downstream spoofing attack) applied in Linux kernel 7.1 and higher. This is not a complete fix but does increase attack complexity." And on severity, where Microsoft attributed its moderate rating to the attack depending on ephemeral port allocations, the researcher's own rebuttal is that the proof of concept can cover the entire ephemeral port range in a matter of seconds — a direct challenge to that mitigating factor, and the researcher's claim rather than the vendor's.

That leaves an asymmetry worth being precise about. A defender who applies both updates has closed one of five primitives outright on Windows, raised its cost on Linux, and left the DNS hijack, the port disclosure and the table-exhaustion denial of service untouched on every platform, because they have no identifier and therefore nothing to apply. The precondition for all of them is unchanged: an attacker positioned downstream of the same NAT. Where that position exists in a public-sector estate is worth enumerating deliberately — a multi-tenant hypervisor host, a container node running workloads of different trust levels behind one bridge, a shared cloud egress gateway, a guest network sharing translation with a corporate one.

Detection, telemetry class first. The researcher's own recommendation is the practical one: monitor NAT-table utilisation for anomalous growth, which is the signal for the exhaustion primitive and often a precursor to mapping manipulation. Connection-tracking telemetry showing entries for established sessions transitioning to a closed state without an orderly teardown, or reappearing against a different internal address, is the shape of the hijack — and the Linux mechanism is specifically a reset packet carrying an invalid sequence number, which is itself the anomaly to look for. Permissive connection-tracking modes that accept out-of-window packets widen the window and are worth turning off where they are not required. **Defender takeaway:** treat a shared NAT table as a shared trust boundary and place it accordingly. Patching resolves less here than usual — one primitive on one platform, partial mitigation on the other — so the durable control is architectural separation of trust levels that currently share translation state.
