---
schema: 1
kind: vulnerability
horizon: operational
title: "UPDATE — the NetScaler flaw this pipeline recorded as a denial-of-service issue is a pre-authentication root shell: watchTowr publishes the full SAML SignedInfo overflow chain, and the sibling CitrixBleed bug has been carried as actively exploited since July"
headline: "A NetScaler bug published as a memory-overflow issue turns out to be unauthenticated code execution as root on the packet engine"
summary: >
  watchTowr published a full exploitation chain on 2026-08-14 for a NetScaler ADC/Gateway heap overflow in SAML
  signature canonicalization, reaching a root shell pre-authentication — a bug whose public CVE description
  amounts to a "Memory Overflow". watchTowr believes but cannot confirm it is CVE-2026-8452, and NCSC-CH calls
  the analysis "likely related" to it. Both it and the sibling CVE-2026-8451 were fixed in the same June/July
  release; NCSC-CH has carried CVE-2026-8451 as actively exploited with a public proof of concept since
  3 July, which this pipeline's original entry recorded as unconfirmed.
discovered_at: "2026-08-15T05:10:00Z"
event_date: "2026-08-14"
run_id: 2026-08-15T0412Z-intel
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - rce
  - pre-auth
  - actively-exploited
  - poc-public
  - patch-available
  - identity
regions:
  - global
  - europe
  - switzerland
sectors:
  - public-sector
  - finance
  - healthcare
  - energy
  - telco
entities: []
techniques: [T1190, T1505.003, T1548.001]
affected_products:
  - Citrix NetScaler ADC
  - Citrix NetScaler Gateway
cves:
  - id: CVE-2026-8452
    cvss: "8.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - poc-public
      - patch-available
    affected: "NetScaler ADC/Gateway 14.1 before 14.1-72.61, 13.1 before 13.1-63.18; 14.1 FIPS before 14.1-72.61 and 13.1 FIPS/NDcPP before 13.1-37.272"
    fixed: "14.1-72.61, 13.1-63.18; 13.1-37.272 on the FIPS/NDcPP train"
  - id: CVE-2026-8451
    cvss: "8.8"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - poc-public
      - patch-available
    affected: "NetScaler ADC/Gateway 14.1 before 14.1-72.61, 13.1 before 13.1-63.18 (and the FIPS/NDcPP builds before 13.1-37.272), configured as SAML IdP"
    fixed: "14.1-72.61, 13.1-63.18; 13.1-37.272 on the FIPS/NDcPP train"
sources:
  - url: "https://labs.watchtowr.com/youre-back-in-the-room-citrix-netscaler-pre-auth-rce-cve-2026-8452/"
    publisher: watchTowr Labs
    date: "2026-08-14"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12739"
    publisher: "NCSC Switzerland — Cyber Security Hub"
    date: "2026-08-14"
    role: primary
closed_sources: []
evidence:
  - quote: "However, we believe this is CVE-2026-8452 given its description as a “Memory Overflow” vulnerability."
    publisher: watchTowr Labs
  - quote: "the vulnerability we’re discussing today is reachable when the Netscaler appliance is configured to use SAML as either a Service Provider (SP) or an Identity Provider (IdP)."
    publisher: watchTowr Labs
  - quote: "During signature canonicalization, earlier versions of the NetScaler solution copy attacker-controlled data from the SAML message's ds:SignedInfo element into a fixed-size global buffer, without checking whether it actually fits."
    publisher: watchTowr Labs
  - quote: "So we now have a memcpy copying from our packet to any address we want, which is a write-what-where primitive."
    publisher: watchTowr Labs
  - quote: "nsppe already runs as root, so our shellcode executes as root too."
    publisher: watchTowr Labs
  - quote: "Actively Exploited, Proof of Concept Available"
    publisher: "NCSC Switzerland — Cyber Security Hub, advisory of 2026-07-03 on CVE-2026-8451"
  - quote: "A new technical analysis, likely related to CVE-2026-8452, was published by Watchtowr"
    publisher: "NCSC Switzerland — Cyber Security Hub, update of 2026-08-14"
verification: multi-source
sourcing_note: >
  The identifier attached to the RCE chain is watchTowr's own inference and is not vendor-confirmed: watchTowr
  states it cannot be certain, and NCSC-CH describes the research as "likely related to" CVE-2026-8452. This
  entry therefore attributes the exploitation chain to the bug watchTowr analysed rather than asserting the
  mapping as fact. Citrix's own knowledge-base article CTX696604 could not be read from this environment — it
  renders as an empty client-side application shell — so the published classification of the flaw is reported
  as watchTowr characterises it and as this pipeline's own 1 July entry recorded it from that bulletin, rather
  than quoted from a vendor page this run could not open. The affected and fixed version strings — including the FIPS and NDcPP builds and their separate fixed
  release — and both CVSS figures come from the vendor's own CVE records rather than from either cited page;
  those records are not citable here under the source-pattern rule, so they are named rather than linked. The
  active-exploitation status belongs to CVE-2026-8451 and dates from NCSC-CH's advisory of 2026-07-03, not from
  this window.
confidence: high
update_of: 2026-07-01/cve-2026-8451-citrix-netscaler-adc-gateway-pre-auth-saml-mem
references: []
deep_dive: true
deep_dive_category: firewall-vpn-rce
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Verify — do not assume — that every NetScaler ADC and Gateway is actually running 14.1-72.61 or 13.1-63.18 or later, and 13.1-37.272 or later on any FIPS or NDcPP appliance, whose fixed build differs from the mainline one, and treat any instance whose upgrade was deferred because CVE-2026-8452 read as an availability-only issue as an outstanding pre-auth remote-code-execution exposure rather than an availability risk."
  - "For any appliance that was internet-reachable as a SAML Identity Provider while unpatched, run a compromise assessment rather than an upgrade alone — the sibling flaw CVE-2026-8451 leaks process memory into the response cookie and has been carried as actively exploited with a public proof of concept since 3 July, so session material and secrets resident in that memory should be treated as disclosed and rotated."
migrated_from: null
---

**UPDATE (originally covered 2026-07-01):** the original entry covered Citrix's six-CVE NetScaler bulletin and its headline flaw CVE-2026-8451, a pre-authentication memory overread in the SAML `/saml/login` parser, and described the companion CVE-2026-8452 as a denial-of-service and undefined-control-flow memory-management issue in Gateway and AAA vserver configurations. That description was faithful to the vendor's CVE record and is now known to be a serious understatement. Two deltas follow, and the second is a correction to this pipeline's own record.

**The bug published as a memory-overflow issue is a pre-authentication root shell.** watchTowr identifies its target from the public record's own wording, writing that "we believe this is CVE-2026-8452 given its description as a “Memory Overflow” vulnerability" — the same sparse framing behind the denial-of-service characterisation this pipeline carried on 1 July from Citrix's bulletin. On 2026-08-14 watchTowr Labs published a chain that ends in a root command shell, entirely pre-authentication ([watchTowr Labs, 2026-08-14](https://labs.watchtowr.com/youre-back-in-the-room-citrix-netscaler-pre-auth-rce-cve-2026-8452/)). The identifier is an inference rather than a confirmation — watchTowr says so plainly, and Switzerland's NCSC describes the work as "A new technical analysis, likely related to CVE-2026-8452, was published by Watchtowr" ([NCSC-CH, 2026-08-14](https://security-hub.ncsc.admin.ch/#/posts/12739)) — but the bug watchTowr analysed is fixed by the same release, so the operational conclusion does not depend on resolving the mapping.

**The kill chain.** The defect is in SAML signature canonicalization: "During signature canonicalization, earlier versions of the NetScaler solution copy attacker-controlled data from the SAML message's ds:SignedInfo element into a fixed-size global buffer, without checking whether it actually fits" ([watchTowr Labs, 2026-08-14](https://labs.watchtowr.com/youre-back-in-the-room-citrix-netscaler-pre-auth-rce-cve-2026-8452/)). The attacker-controlled field is the `PrefixList` attribute of the `InclusiveNamespaces` element inside the `ds:SignedInfo` block, and the copy target sits in `nsppe`, NetScaler's packet-processing engine. An oversized value overflows linearly into the header of the adjacent chunk in the appliance's network-buffer pool, corrupting that neighbour's data-pointer and freelist-link fields. The corruption becomes an attacker primitive later, when the packet engine retrieves that chunk and performs a `memcpy` using the corrupted pointer as its destination with an attacker-influenced length: "So we now have a memcpy copying from our packet to any address we want, which is a write-what-where primitive." From there the exploit is unusually cheap, because the target offers almost no mitigations — "The nsppe binary lacks almost all of the protections you'd hope to find, and the heap is executable, for reasons known only to Citrix" — so watchTowr redirected execution into shellcode placed on a heap that is both executable and at a fixed address, and "nsppe already runs as root, so our shellcode executes as root too."

Two engineering details in the chain matter to defenders more than the memory corruption does. First, an `nsppe` crash normally triggers a full appliance reboot through a watchdog process, which would destroy anything the attacker dropped; watchTowr neutralised the packet engine's crash-signal handlers so the watchdog merely respawned the process instead of rebooting the box, letting a dropped PHP webshell survive. Second, because the web server executing that webshell runs as an unprivileged account while `nsppe` runs as root, the exploit set the SUID bit on `/bin/sh` from the root shellcode so that commands issued through the webshell execute with a root effective UID ([watchTowr Labs, 2026-08-14](https://labs.watchtowr.com/youre-back-in-the-room-citrix-netscaler-pre-auth-rce-cve-2026-8452/)). The result is durable root that survives the process restart an operator would most likely dismiss as a glitch.

**Reachability.** watchTowr states the vulnerability "is reachable when the Netscaler appliance is configured to use SAML as either a Service Provider (SP) or an Identity Provider (IdP)" ([watchTowr Labs, 2026-08-14](https://labs.watchtowr.com/youre-back-in-the-room-citrix-netscaler-pre-auth-rce-cve-2026-8452/)) — which, in the deployment terms Citrix's bulletin used and this pipeline recorded on 1 July, is any appliance acting as a Gateway or AAA virtual server. That is the ordinary shape of a remote-access appliance in a European government or critical-infrastructure network, and it is broader than the sibling flaw's precondition: NCSC-CH records that one as requiring the appliance to be configured as a SAML Identity Provider specifically ([NCSC-CH, advisory of 2026-07-03](https://security-hub.ncsc.admin.ch/#/posts/12739)). Affected are NetScaler ADC and Gateway 14.1 before 14.1-72.61 and 13.1 before 13.1-63.18, and both CVE records additionally list the FIPS and NDcPP builds — 14.1 FIPS before 14.1-72.61 and 13.1 FIPS/NDcPP before 13.1-37.272, a different fixed build that an estate running certified appliances has to check for separately. Both flaws were fixed together in that June/July release. No party reports in-the-wild exploitation of the code-execution chain.

**The correction.** The original entry recorded that no in-the-wild exploitation of CVE-2026-8451 was confirmed at disclosure. NCSC-CH's advisory on that flaw, timestamped 2026-07-03, states its current exploitation status as "Actively Exploited, Proof of Concept Available", and cites reporting that it was exploited immediately after public disclosure ([NCSC-CH, advisory of 2026-07-03, updated 2026-08-14](https://security-hub.ncsc.admin.ch/#/posts/12739)). That status has stood since early July and this pipeline did not carry it — so an estate that read the 1 July entry and concluded the memory-overread flaw was unexploited was working from a stale picture for six weeks. The exploitation is not new; the record here was wrong.

**Defender takeaway:** this is a case where the vendor's severity label, not the patch, was the failure. Any estate that triaged CVE-2026-8452 as an availability bug and deferred the upgrade has been carrying an unauthenticated path to root on an internet-facing remote-access appliance. The patch that closes it is the same one already recommended six weeks ago, so for most estates the task is verification rather than remediation — and where verification fails, the pre-auth memory disclosure in the sibling flaw has been actively exploited throughout that window, which makes anything resident in the appliance's memory during that period a rotation candidate rather than a hypothetical.

**Triage:** the distinctive telemetry is a crash that does not behave like a NetScaler crash. In appliance system and error logs, an `nsppe` process restart *without* the full appliance reboot that normally follows one is the signature this exploit deliberately produces, and it is worth correlating against inbound SAML authentication attempts in the same interval. On the request side, SAML AuthnRequest and Response bodies carrying an anomalously large `InclusiveNamespaces` `PrefixList` attribute inside a `SignedInfo` block are the delivery shape — legitimate SAML messages carry short namespace-prefix lists, so length is a usable discriminator here rather than a heuristic. Where any host-level telemetry is available from the appliance, a shell process spawned by the web server is decisive: a NetScaler web server has no legitimate reason to spawn a shell, and the SUID step means the shell will carry a root effective UID under a process that should never have one.
