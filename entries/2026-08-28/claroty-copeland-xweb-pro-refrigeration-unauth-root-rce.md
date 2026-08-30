---
schema: 1
kind: vulnerability
title: "Claroty Team82: 23 vulnerabilities in Copeland XWEB Pro supervisory refrigeration controllers chain to unauthenticated root RCE — a deterministic admin password derived from the device's own MAC address is one of THREE independent pre-auth paths"
headline: "An attacker can reconstruct admin credentials for an exposed refrigeration controller offline, then silently disable cooling while the display reports normal"
summary: >
  Claroty Team82 disclosed 23 vulnerabilities (21 high) in Copeland XWEB300D/500D/500B PRO
  supervisory refrigeration controllers. Three chain to unauthenticated root RCE: an auth-bypass
  logic flaw in the Lua authentication handler, a deterministic admin-password generator
  derivable offline from the device's MAC address and current date, and an unauthenticated OS
  command injection via the libraries installation route. 17 further, authenticated-only
  command-injection flaws are individually CVE-mapped by the source at CVSS 8.0 each. Copeland
  fixed all 23 in firmware v1.13; no exploitation reported.
discovered_at: "2026-08-28T06:52:00Z"
updated_at: null
event_date: "2026-08-09"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, auth-bypass, pre-auth, patch-available, ot-ics]
regions: [global, europe]
sectors: [healthcare, energy]
entities: []
techniques: [T1190, T1078.001, T1059]
affected_products: ["Copeland XWEB300D PRO", "Copeland XWEB500D PRO", "Copeland XWEB500B PRO"]
cves:
  - id: CVE-2026-25085
    cvss: "8.6"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — Lua user_authenticate handler"
    fixed: "Firmware 1.13"
  - id: CVE-2026-21718
    cvss: "10.0"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1; authentication bypass leading to pre-authenticated code execution (Claroty publishes no per-flaw mechanism for this id)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-24663
    cvss: "9.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — libraries installation route (unauthenticated)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-21389
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — contacts import route"
    fixed: "Firmware 1.13"
  - id: CVE-2026-25111
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — restore route"
    fixed: "Firmware 1.13"
  - id: CVE-2026-20742
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — templates route"
    fixed: "Firmware 1.13"
  - id: CVE-2026-24517
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — firmware update route"
    fixed: "Firmware 1.13"
  - id: CVE-2026-25195
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — firmware update route (crafted firmware file)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-20910
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — firmware update action (devices field)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-24689
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — firmware update apply action (devices field)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-25109
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — get setup route (devices field)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-20902
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — parameters route (map upload action)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-24695
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — utility route (OpenSSL argument fields)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-25105
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — debug route (Modbus command tool)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-24452
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — devices route (crafted template file)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-23702
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — API V1 import-preconfiguration action (server username field)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-25196
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — Wi-Fi SSID/password configuration"
    fixed: "Firmware 1.13"
  - id: CVE-2026-25721
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — API V1 restore action (server username/password fields)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-25037
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — system setup (crafted LCD state)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-20764
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB300D/500D/500B PRO firmware ≤1.12.1 — system setup (device hostname configuration)"
    fixed: "Firmware 1.13"
sources:
  - url: "https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers"
    publisher: "Claroty Team82"
    date: "2026-08-09"
    role: primary
closed_sources: []
evidence:
  - quote: "If an attacker supplied an unrecognized auth_mode, the user_authenticate function did not explicitly reject the request by returning nil or false. Instead, it returned an unpopulated table: { user = nil, role = nil, recovery = nil }."
    publisher: "Claroty Team82"
  - quote: "Because the seed values are identical across the product line and the variables (MAC address and date) can be obtained via unauthenticated public endpoints, an adversary can reconstruct the entire derivation chain offline."
    publisher: "Claroty Team82"
  - quote: "Since these services run with elevated privileges, successful exploitation results in immediate root-level code execution on the controller."
    publisher: "Claroty Team82"
  - quote: "Copeland worked closely and collaboratively with us to develop a comprehensive remediation strategy. The vendor successfully patched these vulnerabilities and has uploaded firmware update version 1.13."
    publisher: "Claroty Team82"
verification: single-source
sourcing_note: >
  Claroty Team82 is the sole source (Admiralty B research lab, routine for coordinated-disclosure
  OT research); a CISA ICS advisory reported elsewhere as ICSA-26-057-10 could not be located or
  fetched as of 2026-08-30 for a second corroborating source. Claroty's own article publishes a full 1:1
  identifier-to-endpoint-to-CVSS table for 20 of the 23 disclosed CVEs, each with its own
  per-endpoint description — all 20 are recorded individually here. The remaining three of the 23
  are referenced only in the article's aggregate "23 vulnerabilities" count with no individually
  published identifier or per-flaw detail located as of 2026-08-30, and are therefore not listed
  individually. Claroty describes the deterministic-password mechanism in narrative form without
  attaching a CVE id to it, and its table text for CVE-2026-21718 says only "an authentication
  bypass vulnerability... enabling any attackers to bypass the authentication requirement and
  achieve pre-authenticated code execution", so which identifier covers that mechanism is not
  stated by the vendor and is not asserted here.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every Copeland XWEB300D/500D/500B PRO controller to firmware v1.13 now, and treat any internet-exposed unit as a compromise-assessment candidate regardless of prior authentication controls: the deterministic-password path is fully reconstructable offline from data available at unauthenticated public endpoints, so a strong admin password alone did not protect an unpatched device."
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [sourcing_note, body]
  - at: "2026-08-30T13:12:06Z"
    run_id: 2026-08-30T1312Z-audit
    type: correction
    summary: >
      This entry stated that CVE-2026-21718 is the deterministic admin-password flaw. Claroty does
      not say that. Its per-CVE table text for that identifier is generic ("an authentication
      bypass vulnerability... enabling any attackers to bypass the authentication requirement and
      achieve pre-authenticated code execution", CVSS v3 10.0), and the narrative section that
      describes the MAC-address-and-date key derivation names no CVE id at all. The binding was an
      inference by elimination rather than a stated attribution, and a defender tracing the
      identifier to a patch note would have been misled. The mechanism description stands as reported; the id
      binding is removed from the title-adjacent claim, the CVE record's affected text, the body
      and the action, and the sourcing note now states what Claroty does and does not attribute.
    fields: [cves, sourcing_note, actions, body]
migrated_from: null
---

Claroty Team82 disclosed 23 vulnerabilities (21 rated high) in Copeland XWEB300D/500D/500B PRO supervisory refrigeration controllers (firmware ≤1.12.1), which manage field devices such as the XR60CX controller over Modbus RS-485 and Ethernet in commercial refrigeration and cold-chain deployments. Two named flaws chain to unauthenticated root RCE. CVE-2026-25085 is a logic flaw in the Lua `user_authenticate` handler: when an attacker supplies an unrecognized `auth_mode` value in the HTTP `Authorization: Basic` header, the function does not return `nil`/`false` but an unpopulated yet "truthy" table — "if an attacker supplied an unrecognized auth_mode, the user_authenticate function did not explicitly reject the request by returning nil or false. Instead, it returned an unpopulated table: { user = nil, role = nil, recovery = nil }" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)) — and the router downstream checks only that something was returned, not its contents, so the malformed request slips through unauthenticated.

One of the three pre-auth paths is a deterministic admin-password generator: the credential is derived via a key-derivation function from a hardcoded firmware seed identical across the product line, plus the device's MAC address and the current date — both obtainable from unauthenticated public endpoints or local-network broadcast — letting an attacker reconstruct valid admin credentials fully offline with zero interaction with the target: "because the seed values are identical across the product line and the variables (MAC address and date) can be obtained via unauthenticated public endpoints, an adversary can reconstruct the entire derivation chain offline" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)). A third pre-auth path, CVE-2026-24663 (CVSS 9.0), is an unauthenticated OS command injection reachable by sending a crafted request to the libraries installation route, with no authentication step to bypass at all.

The 17 further CVEs (all listed above) are individually documented OS command-injection flaws across API/CGI endpoints (contacts import, firmware update, device templates, network/Wi-Fi configuration, the Modbus debug tool, and others), each requiring prior authentication and each scored CVSS 8.0. All are served by an embedded lighttpd instance where unsanitized user input reaches Lua system-execution calls running with elevated privileges — any of the three pre-auth primitives above chains directly to root: "since these services run with elevated privileges, successful exploitation results in immediate root-level code execution on the controller" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)). Claroty built a live physical demonstration: from an internet-exposed XWEB controller, an attacker reverse-engineers the connected field controller's undocumented Modbus register map and can display a normal temperature on the supervisory UI while silently disabling cooling — spoiled food, or compromised temperature-sensitive medical supplies for pharmaceutical cold-chain. Copeland shipped firmware v1.13 through coordinated disclosure, fixing all 23 issues: "Copeland worked closely and collaboratively with us to develop a comprehensive remediation strategy. The vendor successfully patched these vulnerabilities and has uploaded firmware update version 1.13" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)); no exploitation in the wild is reported — this is coordinated vulnerability research, not an active campaign.

An anonymous, single-request path to full administrative control of internet-exposed cold-chain infrastructure demands action beyond a routine patch cycle, independent of confirmed exploitation: absence of exploitation is not evidence of safety when the exploit is a MAC address. Internet-exposed commercial refrigeration and cold-storage deployments are directly relevant to healthcare and food-safety cold-chain operations. **Triage:** the falsified-display behaviour is itself the detection challenge — since the supervisory UI can display normal readings while cooling is disabled, the durable signal is out-of-band: field-controller-level telemetry (direct Modbus reads from the XR60CX or equivalent, independent of the XWEB supervisory layer) that diverges from what the XWEB UI reports is the discriminator, and any authentication attempt using an `auth_mode` value the deployment does not use is a probe worth alerting on.

## Correction — 2026-08-30T13:12:06Z

Which CVE identifier covers the deterministic admin-password path is **not** something Claroty states, and this entry previously asserted it. Claroty's per-CVE table describes CVE-2026-21718 only as "an authentication bypass vulnerability... enabling any attackers to bypass the authentication requirement and achieve pre-authenticated code execution" with a CVSS v3 of 10.0, while the section walking through the MAC-address-and-date key derivation attaches no identifier to it ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)). The three pre-auth paths and the mechanism of each are unchanged, and so is the remediation: firmware v1.13 fixes the disclosed set. What changes is that an operator matching a specific identifier against a vendor patch note or an asset-management ticket should not expect CVE-2026-21718 to be documented anywhere as the password-derivation bug.
