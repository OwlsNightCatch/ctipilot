Item 1 NatJack — DONE researching. Key facts:
- Primary Synack landing page (marketing, no per-CVE detail) + natjack.io (technical, explicit CVE mapping)
- CVE-2026-56181: Microsoft Windows NAT spoofing, CWE-346, CVSS 3.1 8.3 (temporal 7.2) AV:A/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H, Moderate severity per MSRC, not exploited, not publicly disclosed (MSRC), released 2026-07-14, affects Windows 11 24H2/25H2/26H1 (ARM64+x64) and Windows Server 2025 (+Server Core) - fixed versions per NVD: 24H2  CVE-2023-30305 to CVE-2023-30314 (earlier NAT sequence-number leakage TCP hijack research)
- This is genuinely new (not in prior_coverage or registry) — clears relevance bar strongly: Hyper-V and Linux netfilter both at scale in this constituency; precise CVE ids, precise affected/patched versions, precise CWE, exact vulnerable file (nf_conntrack_proto_tcp.c), attacker precondition (downstream/shared-NAT), detection concepts (nf_conntrack_tcp_loose, NAT table monitoring).

TODO Item 2 (Novee coding agent) and Item 3 (SSD bridge STP UAF) next.
