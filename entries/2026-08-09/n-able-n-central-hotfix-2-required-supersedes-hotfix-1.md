---
schema: 1
kind: vulnerability
horizon: operational
title: "N-able N-central Hotfix 2 (2026.3.1.10) is mandatory even for instances that already applied Hotfix 1 — and the attackers reached the managed endpoints, not just the server"
headline: "The N-central build this pipeline named as the fix has been superseded; 2026.3.1.7 is no longer sufficient"
summary: >
  N-able shipped N-central 2026.3 Hotfix 2 (build 2026.3.1.10) on 2026-08-06 and states plainly that
  it is required even for partners who already applied Hotfix 1, which it supersedes with additional
  hardening as threat actors evolve their techniques against CVE-2026-18577. That matters to anyone
  who acted on this pipeline's earlier coverage, which named build 2026.3.1.7 as the remediation.
  Reporting on 2026-08-08 adds what the attackers did with administrative access: they used
  N-central's own Take Control feature to reach systems inside the managed environment and registered
  a new service for a Cloudflare Tunnel on those devices, which keeps them in after access to the
  N-central server itself is revoked. Hosted NCOD instances are already mitigated and need no action.
discovered_at: "2026-08-09T05:08:00Z"
event_date: "2026-08-06"
run_id: 2026-08-09T0412Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, actively-exploited, cisa-kev, auth-bypass, patch-available, supply-chain]
regions: [global, europe]
sectors: [public-sector, technology]
entities: []
techniques: [T1190, T1219, T1572]
affected_products: ["N-able N-central"]
cves:
  - id: CVE-2026-18577
    cvss: "8.2"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "All versions prior to 2026.3.1.7; the vendor now requires 2026.3.1.10, which supersedes the 2026.3.1.7 hotfix."
    fixed: "N-central 2026.3.1.10 (Hotfix 2, released 2026-08-06)"
sources:
  - url: "https://status.n-able.com/2026/08/06/n-central-2026-3-hotfix-2-additional-mitigation-for-cve-2026-18577/"
    publisher: "N-able"
    date: "2026-08-06"
    role: primary
  - url: "https://thehackernews.com/2026/08/n-central-attackers-reach-managed.html"
    publisher: "The Hacker News"
    date: "2026-08-08"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This is not a duplicate of our previous communication — Hotfix 2 is required, even if you already applied the earlier hotfix. Hotfix 2 supersedes Hotfix 1 with additional hardening measures to further protect you and your customers."
    publisher: "N-able"
  - quote: "Upon gaining access to those devices, the threat actors registered a new service for a Cloudflare Tunnel, enabling persistence even after access to the N‑central server was revoked."
    publisher: "The Hacker News"
verification: multi-source
sourcing_note: >
  The vendor is the sole assessor of the exploitation activity described here; The Hacker News relays
  and quotes the vendor's statements rather than adding an independent assessment, which is why
  credibility stays at 2. The vendor's expanded indicator list and its service template for checking
  endpoints are referenced but not reproduced — this store carries no indicators.
confidence: high
update_of: 2026-08-05/n-able-n-central-post-exploitation-rmm-tunnel-driver
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade on-premises N-central to 2026.3.1.10 even where 2026.3.1.7 was already applied — the vendor states Hotfix 2 is required regardless and supersedes Hotfix 1; hosted NCOD instances need no action."
  - "Extend the compromise assessment from the N-central server to the endpoints it manages, looking specifically for a newly registered service running a Cloudflare Tunnel client, which the vendor reports survives revocation of access to the N-central server."
migrated_from: null
---

**UPDATE (originally covered 2026-08-05):** The remediation named in this pipeline's earlier coverage is no longer the endpoint. N-able published N-central 2026.3 Hotfix 2, build 2026.3.1.10, on 2026-08-06, and states that it is not a duplicate of the previous communication: Hotfix 2 is required even for partners who already applied the earlier hotfix, and it supersedes Hotfix 1 with additional hardening measures ([N-able, 2026-08-06](https://status.n-able.com/2026/08/06/n-central-2026-3-hotfix-2-additional-mitigation-for-cve-2026-18577/)). The vendor frames it as proactively expanding protections in response to ongoing monitoring of threat actors as they evolve their attack techniques, rather than as a fix for a newly identified flaw ([N-able, 2026-08-06](https://status.n-able.com/2026/08/06/n-central-2026-3-hotfix-2-additional-mitigation-for-cve-2026-18577/)). On-premises instances can upgrade directly to 2026.3.1.10 from 2025.4, 2026.1, 2026.2, 2026.3 or the 2026.3.1 Hotfix 1 build, and hosted N-central (NCOD) environments have already had the mitigations applied and require no customer action; the hotfix itself does not require agents to be upgraded to protect against CVE-2026-18577 ([N-able, 2026-08-06](https://status.n-able.com/2026/08/06/n-central-2026-3-hotfix-2-additional-mitigation-for-cve-2026-18577/)).

The second half of the delta is the blast radius. The Hacker News reports on 2026-08-08 that in the attacks N-able observed, the flaw let attackers obtain administrative access remotely and then use N-central's own Take Control feature to connect to systems inside the managed environment, where they registered a new service for a Cloudflare Tunnel that kept them in even after access to the N-central server was revoked ([The Hacker News, 2026-08-08](https://thehackernews.com/2026/08/n-central-attackers-reach-managed.html)). N-able detected the unusual activity in a customer environment on 2026-07-31 and has confirmed a limited number of customers were affected; it has published an expanded set of network indicators and a custom service template that checks Windows endpoints in N-central against known indicators, while cautioning that a clean result should not be read as a guarantee that an environment was not impacted and should sit alongside a review of logs and account activity ([The Hacker News, 2026-08-08](https://thehackernews.com/2026/08/n-central-attackers-reach-managed.html)).

**Defender takeaway:** the operational point is the version number, and it is easy to miss because nothing about the CVE changed — an organisation that patched to 2026.3.1.7 in the first days of August, saw no new CVE identifier, and moved on is running a build the vendor now says is insufficient. Treat the endpoint estate as in scope too: because the persistence was planted through the RMM's legitimate remote-control path and then anchored to an outbound tunnel service on the managed device, evicting the attacker from the management server does not evict them from the machines it manages, and the vendor's own tooling is explicitly not a clean bill of health.

**Triage:** a Cloudflare Tunnel client running as a service is not inherently malicious — it is ordinary infrastructure in plenty of estates, and RMM platforms legitimately install services on managed endpoints all day. The discriminator here is provenance and timing: the service appears on endpoints during or after the window in which the N-central server was exploitable, it was created through the RMM's own remote-control session rather than through a change ticket or a deployment policy, and it keeps beaconing after the management platform's access has been cut. Any one of those alone is weak; the sequence is the signal.
