---
schema: 1
kind: vulnerability
title: "CISA KEV adds three unrelated Linux kernel flaws in one day: kTLS receive-path logic error, AF_ALG race condition, netfilter ebtables SNAT out-of-bounds write"
headline: "CISA lists three separate Linux kernel bugs as exploited; Red Hat says public exploits exist, with no account of use"
summary: >
  CISA added three unrelated Linux kernel CVEs to its Known Exploited Vulnerabilities catalog on
  2026-09-18: CVE-2025-39682 (kTLS receive-path logic error, network-reachable where kernel TLS is in use according to Red Hat, local according to The Hacker News), CVE-2025-39964 (AF_ALG crypto-socket race condition, local) and CVE-2026-53266 (netfilter
  bridge ebtables SNAT out-of-bounds write, local). No actor, campaign or technical account of the
  exploitation is public; Red Hat updated its advisories on 2026-09-19 to state that public exploits
  exist.
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
    cvss: "9.8 (kernel CNA / NVD, AV:N) / 7.0 (Red Hat re-score, AV:N/AC:H)"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "≤ 6.16.3 on kernels using kernel TLS; branch-dependent, see body"
    fixed: "6.1.149, 6.6.103, 6.12.44, 6.16.4"
  - id: CVE-2025-39964
    cvss: "7.8 (kernel CNA) / 5.5 (NVD re-score, availability-only)"
    epss: null
    type: dos
    vector: local
    auth: post-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "≤ 6.16.8; branch-dependent, see body"
    fixed: "5.10.245, 5.15.194, 6.1.154, 6.6.108, 6.12.49, 6.16.9"
  - id: CVE-2026-53266
    cvss: "8.8"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "≤ 6.18.35; branch-dependent, see body"
    fixed: "5.10.259, 5.15.210, 6.1.176, 6.6.143, 6.12.94, 6.18.36, 7.0.13"
sources:
  - url: "https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-one-known-exploited-vulnerability-catalog"
    publisher: "CISA"
    date: "2026-09-18"
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-two-known-exploited-vulnerabilities-catalog"
    publisher: "CISA"
    date: "2026-09-18"
    role: primary
  - url: "https://access.redhat.com/security/cve/cve-2025-39682"
    publisher: "Red Hat Product Security"
    date: "2026-09-19"
    role: corroborating
  - url: "https://access.redhat.com/security/cve/cve-2025-39964"
    publisher: "Red Hat Product Security"
    date: "2026-09-19"
    role: corroborating
  - url: "https://access.redhat.com/security/cve/cve-2026-53266"
    publisher: "Red Hat Product Security"
    date: "2026-09-19"
    role: corroborating
  - url: "https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html"
    publisher: "The Hacker News"
    date: "2026-09-19"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.1.149"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2025-08-28"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.6.103"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2025-08-28"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.12.44"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2025-08-28"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.16.4"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2025-08-28"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.10.245"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2025-10-02"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.15.194"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2025-10-02"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.1.154"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2025-09-25"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.6.108"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2025-09-25"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.12.49"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2025-09-25"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.16.9"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2025-09-25"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.10.259"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2026-06-19"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.15.210"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2026-06-19"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.1.176"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2026-06-19"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.6.143"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2026-06-19"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.12.94"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2026-06-19"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.18.36"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2026-06-19"
    role: corroborating
  - url: "https://cdn.kernel.org/pub/linux/kernel/v7.x/ChangeLog-7.0.13"
    publisher: "kernel.org (Linux stable ChangeLog)"
    date: "2026-06-19"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV catalog"
    date: "2026-09-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "CISA has added one new vulnerability to its"
    publisher: "CISA"
  - quote: "based on evidence of active exploitation"
    publisher: "CISA"
  - quote: "The corner case we missed is when the initial record comes from rx_list, and it's zero length."
    publisher: "Red Hat Product Security"
    source_url: "https://access.redhat.com/security/cve/cve-2025-39682"
verification: multi-source
sourcing_note: >
  CISA's catalog additions are the exploitation record; Red Hat's per-flaw advisories carry the flaw
  descriptions and mitigations and, as The Hacker News reports, were updated on 2026-09-19 to state
  that public exploits exist. kernel.org's stable ChangeLogs confirm the fixed releases.
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
  - "Patch the kernel ahead of the regular cycle on Linux hosts that load the tls module (CVE-2025-39682, remotely reachable), run ebtables SNAT rules that rewrite ARP hardware addresses on a bridge (CVE-2026-53266), or give less-trusted users local access (all three); where the update must wait, block the tls module from loading or remove the ARP-rewrite SNAT rules, as Red Hat advises."
updates:
  - at: "2026-09-20T13:34:54Z"
    run_id: 2026-09-20T1308Z-audit
    type: correction
    summary: >
      The sourcing note said no vendor advisory added exploitation detail beyond re-listing fixed kernel
      builds. Red Hat had already updated its advisories for all three flaws, on 2026-09-19 at 02:00 UTC,
      to acknowledge active exploitation, state that public exploits exist and tell customers to address
      them with high priority. The sourcing note and the verification value now reflect that second
      assessment, and the three NVD API endpoints previously listed as sources are replaced by Red Hat's
      own per-flaw advisory pages. Two evidence quotes attributed to those endpoints were re-checked: one
      is carried verbatim by Red Hat's page and is now attributed there, the other is on no reachable
      first-party page and is removed. The three inline citations in the analysis pointed at the same
      endpoints and now point at Red Hat's pages; the sentence on the bridge flaw is rewritten to what
      Red Hat states, because the function name and the page-fragment detail it previously carried are
      on no source the entry can cite.
    fields: [verification, sourcing_note, sources, evidence, body]
  - at: "2026-09-27T13:28:04Z"
    run_id: 2026-09-27T1308Z-audit
    type: correction
    summary: >
      The second score recorded for CVE-2025-39682 was wrong in every part. Red Hat's own CVE page
      scores it 7.0 with vector AV:N/AC:H, not 7.1, and the re-score is Red Hat's rather than NVD's;
      NVD and cve.org both publish 9.8 with AV:N. No authority scores this flaw AV:L, and the local
      attack vector the entry recorded contradicted its own analysis, which describes the flaw as
      reachable over the network on hosts using kernel TLS receive offload. The other two CVEs' score
      annotations were re-checked against the same authority and are accurate.
    fields: [cves]
  - at: "2026-09-30T07:00:04Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      The headline, summary and main text said the KEV listing was the only public evidence of
      exploitation, although Red Hat had stated on 2026-09-19 that public exploits exist. They now
      carry Red Hat's statement, without claiming Red Hat confirms active exploitation. The takeaway
      and action no longer claim that general-purpose fleets are not at elevated risk or that three
      configurations are the only exploited surfaces, the US federal deadline remark and source-file
      names no cited page carries are removed, and the fixed stable kernels cite kernel.org's
      ChangeLogs, adding 7.0.13 for CVE-2026-53266. The Hacker News' local reading of CVE-2025-39682
      is stated as a contradiction to Red Hat's remote one. CVE-2025-39964 is typed as denial of
      service, as Red Hat describes it.
    fields: [headline, summary, body, title, actions, cves, sourcing_note, sources]
migrated_from: null
---

CISA added three unrelated Linux kernel vulnerabilities to its Known Exploited Vulnerabilities catalog on 2026-09-18, in two separate alerts ([CISA, 2026-09-18](https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-one-known-exploited-vulnerability-catalog); [CISA, 2026-09-18](https://www.cisa.gov/news-events/alerts/2026/09/18/cisa-adds-two-known-exploited-vulnerabilities-catalog)), and neither alert names a ransomware campaign, an actor, or a technical account of the exploitation behind any of the three. The Hacker News reports that Red Hat has since stated of each that "there are known public exploits leveraging this vulnerability" ([The Hacker News, 2026-09-19](https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html)). CVE-2025-39682 is a logic error in the kernel's TLS receive path: a zero-length record taken from the `rx_list` queue slips past the per-`recvmsg()` record-type check, a corner case the fix describes as previously unhandled, and Red Hat says it "can be remotely triggered only when kernel TLS (CONFIG_TLS with the TLS ULP) is in use" ([Red Hat Product Security, 2026-09-19](https://access.redhat.com/security/cve/cve-2025-39682)). CVE-2025-39964 is a race condition in the AF_ALG crypto user-API socket: concurrent `sendmsg()` calls to the same socket were never given exclusive-write ownership, so request payloads interleave and corrupt per-socket state, which a local user can use to crash the system or corrupt cryptographic results ([Red Hat Product Security, 2026-09-19](https://access.redhat.com/security/cve/cve-2025-39964)). CVE-2026-53266 is an out-of-bounds write in the netfilter bridge ebtables SNAT target, where the ARP sender-hardware-address rewrite writes directly into a socket-buffer fragment backed by a splice-imported file page ([CISA KEV catalog, 2026-09-18](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)); Red Hat rates it Important and says a local attacker on a system with such bridge rules can reach privilege escalation, memory corruption or denial of service ([Red Hat Product Security, 2026-09-19](https://access.redhat.com/security/cve/cve-2026-53266)). Fixed stable kernels, each confirmed in kernel.org's release ChangeLog: CVE-2025-39682 in [6.1.149](https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.1.149), [6.6.103](https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.6.103), [6.12.44](https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.12.44) and [6.16.4](https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.16.4); CVE-2025-39964 in [5.10.245](https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.10.245), [5.15.194](https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.15.194), [6.1.154](https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.1.154), [6.6.108](https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.6.108), [6.12.49](https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.12.49) and [6.16.9](https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.16.9); CVE-2026-53266 in [5.10.259](https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.10.259), [5.15.210](https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.15.210), [6.1.176](https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.1.176), [6.6.143](https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.6.143), [6.12.94](https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.12.94), [6.18.36](https://cdn.kernel.org/pub/linux/kernel/v6.x/ChangeLog-6.18.36) and [7.0.13](https://cdn.kernel.org/pub/linux/kernel/v7.x/ChangeLog-7.0.13).

**Exposure:** CVE-2025-39682 is reachable over the network only on hosts using kernel TLS, and Red Hat's mitigation is to stop the `tls` module from loading ([Red Hat Product Security, 2026-09-19](https://access.redhat.com/security/cve/cve-2025-39682)). The other two need local access; CVE-2026-53266 also needs ebtables SNAT rules that rewrite ARP hardware addresses on a bridge, which Red Hat's mitigation disables or removes ([Red Hat Product Security, 2026-09-19](https://access.redhat.com/security/cve/cve-2026-53266)), and Red Hat lists no usable mitigation for CVE-2025-39964 ([Red Hat Product Security, 2026-09-19](https://access.redhat.com/security/cve/cve-2025-39964)).

**Contradiction:** The Hacker News describes CVE-2025-39682 as a flaw that "could allow local authenticated users to trigger memory disclosure or denial-of-service" ([The Hacker News, 2026-09-19](https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html)), whereas Red Hat states it "can be remotely triggered only when kernel TLS (CONFIG_TLS with the TLS ULP) is in use" and scores the attack vector as network ([Red Hat Product Security, 2026-09-19](https://access.redhat.com/security/cve/cve-2025-39682)). The exposure assessment above follows Red Hat's technical account of the receive path.

**Defender takeaway:** treat all three as exploited: CISA lists them on evidence of active exploitation, and Red Hat says public exploits exist and to "Address this vulnerability with high priority" ([The Hacker News, 2026-09-19](https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html)). No source says which systems the exploitation hit, so patch kernels ahead of the regular cycle first on hosts that load the `tls` module, run ebtables SNAT ARP-rewrite rules on bridges, or give less-trusted users a local shell, and apply Red Hat's module block or rule change where the update has to wait.

## Correction — 2026-09-20T13:34:54Z

Red Hat now states that public exploits exist for all three flaws. It updated its advisories for CVE-2025-39682, CVE-2025-39964 and CVE-2026-53266 on 2026-09-19 at 02:00 UTC, saying of each that "This CVE is high risk and there are known public exploits leveraging this vulnerability" and "Address this vulnerability with high priority" ([The Hacker News, 2026-09-19](https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html)). The earlier text stated that no vendor advisory added exploitation detail beyond the fixed kernel builds. How the flaws are being exploited, and whether they are chained, is still not described anywhere.

## Correction — 2026-09-27T13:28:04Z

The severity annotation recorded for CVE-2025-39682 was wrong. Red Hat's own page for the CVE publishes a base score of 7.0 with vector `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:H`, while NVD and cve.org both publish 9.8 with `AV:N/AC:L` ([Red Hat Product Security](https://access.redhat.com/security/cve/cve-2025-39682)). The entry's second figure was recorded as 7.1, attributed to NVD rather than Red Hat, and given an `AV:L` local attack vector that no authority assigns. The practical consequence was a contradiction: the analysis describes a flaw reachable over the network wherever kernel TLS receive offload terminates TLS, and an `AV:L` annotation would have told a triage reader the opposite. Only the score annotation changes; the exploitation status, the affected and fixed kernel versions, and the analysis are unchanged.

## Correction — 2026-09-30T07:00:04Z

Red Hat's statement is that public exploits exist, not a confirmation of in-the-wild use: it updated its advisories for all three flaws on 2026-09-19 to say "there are known public exploits leveraging this vulnerability" ([The Hacker News, 2026-09-19](https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html)). The Hacker News describes that update as acknowledging active exploitation, which the quoted wording does not say ([The Hacker News, 2026-09-19](https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html)). No source says which systems or configurations the exploitation used, so no class of Linux host can be ruled out as a target. The ebtables SNAT fix also shipped in the 7.0.13 stable kernel ([kernel.org, 2026-06-19](https://cdn.kernel.org/pub/linux/kernel/v7.x/ChangeLog-7.0.13)).

The Hacker News describes CVE-2025-39682 as reachable by local authenticated users ([The Hacker News, 2026-09-19](https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html)), while Red Hat says it can be triggered remotely where kernel TLS is in use ([Red Hat Product Security, 2026-09-19](https://access.redhat.com/security/cve/cve-2025-39682)). The two readings conflict, and the exposure assessment follows Red Hat's account of the receive path.
