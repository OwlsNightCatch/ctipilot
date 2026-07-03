---
schema: 1
kind: vulnerability
horizon: operational
title: Public PoC released for the libssh2 pre-auth heap write (CVE-2026-55200)
headline: Public PoC released for the libssh2 pre-auth heap write (CVE-2026-55200)
summary: "Two previously-covered critical CVEs now have public PoCs: libssh2 pre-auth heap write (CVE-2026-55200) and the DirtyClone Linux kernel LPE (CVE-2026-43503), the latter with a confirmed working exploit on default Debian/Fedora. Separately, the US posted a $10M bounty on the Russia-nexus Signal/WhatsApp phishing crews and added Signal Backup Recovery Key theft to the advisory — a persistent-access tactic Swiss federal officials using Signal should act on."
discovered_at: "2026-06-30T05:10:41Z"
event_date: 2026-06-29
run_id: 2026-06-30-9aaa1114
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - rce
  - pre-auth
  - poc-public
  - supply-chain
regions:
  - global
sectors:
  - technology
entities: []
cves:
  - id: CVE-2026-55200
    cvss: "9.2"
    epss: null
    type: rce
    vector: user-interaction
    auth: pre-auth
    status:
      - poc-public
      - no-patch
sources:
  - url: "https://thehackernews.com/2026/06/public-poc-released-for-critical.html"
    publisher: The Hacker News
    role: primary
  - url: "https://www.vulncheck.com/advisories/libssh2-out-of-bounds-write-via-unchecked-packet-length-in-transport-c"
    publisher: VulnCheck
    role: corroborating
  - url: "https://github.com/advisories/GHSA-r8mh-x5qv-7gg2"
    publisher: GitHub Advisory Database
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-06-28/cve-2026-55200-libssh2-heap-out-of-bounds-write-in-ssh2-tran
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-30.md
---

**UPDATE (originally covered 2026-06-28):** A public proof-of-concept scaffold for CVE-2026-55200 (CVSS 9.2) appeared on 2026-06-29, and no official libssh2 release carrying the fix has been tagged yet — the patch commit was merged to mainline on 2026-06-12 but downstream consumers must build from source or pin manually ([The Hacker News, 2026-06-29](https://thehackernews.com/2026/06/public-poc-released-for-critical.html)).

The flaw is in `ssh2_transport_read()` in `transport.c`, which fails to bound the attacker-controlled `packet_length` field during the SSH transport handshake; a `0xffffffff` value triggers an integer overflow so `malloc` allocates a tiny buffer while the subsequent write fills the full oversized packet, corrupting the heap before authentication ([VulnCheck, 2026-06-17](https://www.vulncheck.com/advisories/libssh2-out-of-bounds-write-via-unchecked-packet-length-in-transport-c)). Because libssh2 is the client linked into git, curl, PHP, and many CI/CD runners, a malicious or compromised SSH *server* can corrupt memory in connecting clients — the supply-chain/CI-CD direction is the realistic risk. Pin or rebuild libssh2 from the patched commit in pipeline images now, and surface libssh2 versions through SBOM tooling.
