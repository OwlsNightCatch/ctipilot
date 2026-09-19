---
schema: 1
kind: vulnerability
title: "CISA KEV adds three unrelated Linux kernel flaws in one day — kTLS receive-path logic error, AF_ALG race condition, netfilter ebtables SNAT out-of-bounds write"
headline: "CISA confirms active exploitation of three separate Linux kernel bugs with no public exploitation narrative behind any of them"
summary: >
  CISA added three unrelated Linux kernel CVEs to its Known Exploited Vulnerabilities catalog on
  2026-09-18 — CVE-2025-39682 (kTLS receive-path logic error, network-reachable when kernel TLS
  offload is used), CVE-2025-39964 (AF_ALG crypto-socket race condition, local) and CVE-2026-53266
  (netfilter bridge ebtables SNAT out-of-bounds write, local) — with no named actor, campaign or
  public technical account of the exploitation behind any of the three; the KEV listing is the only
  public evidence.
discovered_at: "2026-09-19T04:33:00Z"
updated_at: null
event_date: "2026-09-18"
run_id: 2026-09-19T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, actively-exploited, cisa-kev, dos, priv-esc]
regions: [global]
sectors: [public-sector, technology]
entities: []
techniques: [T1499, T1068]
affected_products: ["Linux Kernel"]
cves:
  - id: CVE-2025-39682
    cvss: "9.8 (kernel CNA, AV:N) / 7.1 (NVD re-score, AV:L)"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "≤ 6.16.3 (kernel TLS receive-offload builds; branch-dependent — see body)"
    fixed: "6.1.149, 6.6.103, 6.12.44, 6.16.4, 6.17"
  - id: CVE-2025-39964
    cvss: "7.8 (kernel CNA) / 5.5 (NVD re-score, availability-only)"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "≤ 6.16.8 (branch-dependent — see body)"
    fixed: "5.10.245, 5.15.194, 6.1.154, 6.6.108, 6.12.49, 6.16.9"
  - id: CVE-2026-53266
    cvss: "8.8"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "≤ 6.18.35 (branch-dependent — see body)"
    fixed: "5.10.259, 5.15.210, 6.1.176, 6.6.143, 6.12.94, 6.18.36"
sources:
  - url: "https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-one-known-exploited-vulnerability-catalog"
    publisher: "CISA"
    date: "2026-09-18"
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-two-known-exploited-vulnerabilities-catalog"
    publisher: "CISA"
    date: "2026-09-18"
    role: primary
  - url: "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-39682"
    publisher: "NVD/NIST"
    date: "2026-09-19"
    role: corroborating
  - url: "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-39964"
    publisher: "NVD/NIST"
    date: "2026-09-19"
    role: corroborating
  - url: "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-53266"
    publisher: "NVD/NIST"
    date: "2026-09-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: "CISA has added one new vulnerability to its"
    publisher: "CISA"
  - quote: "based on evidence of active exploitation"
    publisher: "CISA"
  - quote: "The corner case we missed is when the initial record comes from rx_list, and it's zero length."
    publisher: "NVD/NIST"
  - quote: "If that range is still held in a nonlinear skb fragment backed by a splice-imported file page, skb_store_bits() maps the frag page and copies the new MAC address directly into it."
    publisher: "NVD/NIST"
verification: single-source-national-cert
sourcing_note: "CISA is the sole disclosing authority for all three KEV additions; no vendor (Red Hat, Ubuntu, Debian, SUSE) or research advisory adds exploitation detail beyond re-listing the fixed kernel builds, and no named actor or campaign is attached to any of the three. Carve-out applies: CISA is a high-reliability (Admiralty A) national authority disclosing its own KEV catalog action."
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Identify any Linux hosts running kernel TLS receive-offload (CONFIG_TLS with ktls enabled on the receive path), exposing AF_ALG crypto-API sockets to untrusted local users, or running bridge-netfilter ebtables SNAT with ARP-address rewrite rules — these three configurations are the only confirmed-exploited attack surfaces — and prioritize kernel patching on those hosts ahead of the standard update cycle."
updates: []
migrated_from: null
---

CISA added three unrelated Linux kernel vulnerabilities to its Known Exploited Vulnerabilities catalog on 2026-09-18, in two separate alerts ([CISA, 2026-09-18](https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-one-known-exploited-vulnerability-catalog); [CISA, 2026-09-18](https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-two-known-exploited-vulnerabilities-catalog)), and neither alert names a ransomware campaign, an actor, or a technical account of the exploitation behind any of the three; the KEV listing itself is the only public evidence that any of them has been used against a real target. CVE-2025-39682 is a logic error in the kernel's TLS receive path (`net/tls/tls_sw.c`): a peer on a connection using kernel TLS offload for receive can supply a record sequence where the initial record picked up from the socket's `rx_list` queue is itself zero-length, a corner case the fix commit describes as previously unhandled ([NVD/NIST, mirroring the kernel fix commit](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-39682)) — reachable only on hosts that terminate TLS using `CONFIG_TLS` receive offload, an uncommon but real configuration on high-throughput TLS-terminating proxies and some storage or network appliances, not a default on general-purpose servers or workstations. CVE-2025-39964 is a race condition in the AF_ALG crypto user-API socket (`crypto/af_alg.c`): concurrent `sendmsg()` calls to the same socket were never given exclusive-write ownership, letting request payloads interleave and corrupt per-socket state ([NVD/NIST, mirroring the kernel fix commit](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-39964)) — this requires local access to an AF_ALG socket, which is often restricted or entirely unloaded. CVE-2026-53266 is an out-of-bounds write in the netfilter bridge `ebt_snat` target: the optional ARP sender-hardware-address rewrite calls `skb_store_bits()` without first confirming the target range is writable, and when that range sits in a nonlinear socket-buffer fragment backed by a splice-imported file page, the write lands directly on the underlying page rather than a copy ([NVD/NIST, mirroring the kernel fix commit](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-53266)) — this requires a bridge configured with ebtables SNAT ARP-rewrite rules, plus local low-privilege access to trigger it. Fixed kernel builds: 6.1.149 / 6.6.103 / 6.12.44 / 6.16.4 / 6.17 for CVE-2025-39682; 5.10.245 / 5.15.194 / 6.1.154 / 6.6.108 / 6.12.49 / 6.16.9 for CVE-2025-39964; 5.10.259 / 5.15.210 / 6.1.176 / 6.6.143 / 6.12.94 / 6.18.36 for CVE-2026-53266.

**Defender takeaway:** CISA's remediation deadline for federal agencies is a US-FCEB compliance date and carries no weight here, but the KEV listing itself is jurisdiction-agnostic confirmation of active exploitation — treat all three as confirmed exploited despite the absence of a public narrative. The two local-access bugs (AF_ALG, ebtables SNAT ARP-rewrite) narrow the realistic exposure to hosts where an untrusted or partially-trusted local user already has a foothold; the kTLS bug is the only one reachable purely over the network, and only against hosts that have deliberately enabled kernel TLS receive offload. A general-purpose Linux server or workstation fleet on standard kernel patch cadence is not at elevated risk from any of the three; a fleet running custom bridge-netfilter appliances, kTLS-terminating proxies, or exposing AF_ALG to less-trusted users should patch those specific hosts now rather than waiting for the normal cycle.
