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
  command injection via the libraries installation route. 18 further, authenticated-only
  command-injection flaws score CVSS 8.0 each, and CISA's advisory adds two low-severity
  unauthenticated flaws. Copeland
  fixed all 23 in firmware v1.13; no source read reports exploitation of these flaws, but CERT-FR's alert of 2026-10-13 now
  reports numerous compromises of Copeland xweb refrigeration controllers without naming models, flaws or the entry vector.
discovered_at: "2026-08-28T06:52:00Z"
updated_at: "2026-10-14T03:45:00Z"
event_date: "2026-08-09"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, auth-bypass, pre-auth, patch-available, ot-ics]
regions: [global, europe]
sectors: [retail, healthcare]
entities: ["product:copeland-xweb300d-pro", "product:copeland-xweb500d-pro", "product:copeland-xweb500b-pro", "product:copeland-xweb"]
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
    type: auth-bypass
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
  - id: CVE-2026-3037
    cvss: "8.0"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Copeland XWEB Pro 1.12.1 and prior: MBird SMS service URL/code set via the utility route, executed during system setup (CISA ICSA-26-057-10)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-22877
    cvss: "3.7"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Copeland XWEB Pro 1.12.1 and prior: unauthenticated arbitrary file read (CISA ICSA-26-057-10)"
    fixed: "Firmware 1.13"
  - id: CVE-2026-20797
    cvss: "4.3"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Copeland XWEB Pro 1.12.1 and prior: unauthenticated stack-based buffer overflow in an API route that terminates the program (CISA ICSA-26-057-10)"
    fixed: "Firmware 1.13"
sources:
  - url: "https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers"
    publisher: "Claroty Team82"
    date: "2026-08-09"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/"
    publisher: "CERT-FR (alert CERTFR-2026-ALE-012, revised version)"
    date: "2026-10-13"
    role: corroborating
  - url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-057-10"
    publisher: "CISA (ICS advisory ICSA-26-057-10)"
    date: "2026-02-26"
    role: corroborating
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
  - quote: "CERT-FR is aware of numerous compromises of the remote refrigeration-installation controllers Danfoss AK-SM and AK-SC series as well as Copeland xweb and Dixell xweb. (translated from French)"
    original: "Le CERT-FR a connaissance de nombreuses compromissions des controleurs à distance d'installation de réfrigération Danfoss série AK-SM, AK-SC ainsi que Copeland xweb et Dixell xweb."
    publisher: "CERT-FR (alert CERTFR-2026-ALE-012, revised version)"
    source_url: "https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/"
verification: multi-source
sourcing_note: >
  Claroty Team82 found the vulnerabilities, and CISA's ICS advisory ICSA-26-057-10 of 2026-02-26 lists all 23
  identifiers with a summary and CVSS score each, so the flaws rest on two sources; CERT-FR's alert is a source only for
  compromises of the Copeland xweb product family, and it names no models, flaws or entry vector. Claroty's article
  documents 20 of the 23 with an endpoint each; the other three (CVE-2026-3037, CVE-2026-22877, CVE-2026-20797) are
  recorded from CISA's advisory. Claroty describes the deterministic-password mechanism in narrative form without
  attaching a CVE id to it (CISA maps CVE-2026-21718 to CWE-327, use of a broken or risky cryptographic algorithm,
  which fits that mechanism without binding the id to it), and its table text for CVE-2026-21718 says only "an authentication
  bypass vulnerability... enabling any attackers to bypass the authentication requirement and
  achieve pre-authenticated code execution", so which identifier covers that mechanism is not
  stated by the vendor and is not asserted here.
confidence: medium
references:
  - 2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack
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
  - at: "2026-10-14T03:45:00Z"
    run_id: 2026-10-14T0255Z-intel
    type: update
    summary: >
      CERT-FR revised its refrigeration-controller alert on 2026-10-13 to say it knows of numerous compromises of Copeland xweb controllers, in addition to Danfoss and Dixell units; it names no models, flaws or entry vector, so the earlier 'no exploitation reported' no longer describes the product family.
    fields: [summary, entities, sources, evidence, sourcing_note, references, body]
  - at: "2026-10-19T21:06:23Z"
    run_id: 2026-10-18T1307Z-audit
    type: correction
    summary: >
      CISA's ICS advisory ICSA-26-057-10, which this entry said could not be located, lists all 23
      identifiers: three missing ones are added (CVE-2026-3037, CVE-2026-22877, CVE-2026-20797),
      CVE-2026-21718 is typed as the authentication bypass both sources call it, the field-controller link
      and the register-map wording follow Claroty, the 'zero interaction' claim and the energy sector,
      which no source supports, are removed, the sourcing note records CISA's CWE for CVE-2026-21718, and
      the entry is now two-source.
    fields: [summary, sectors, cves, sources, verification, sourcing_note, body]
migrated_from: null
---

Claroty Team82 disclosed 23 vulnerabilities (21 rated high) in Copeland XWEB300D/500D/500B PRO supervisory refrigeration controllers (firmware ≤1.12.1), which manage field devices such as the XR60CX controller over Modbus on an RS-485 serial network in commercial refrigeration and cold-chain deployments. Two named flaws chain to unauthenticated root RCE. CVE-2026-25085 is a logic flaw in the Lua `user_authenticate` handler: when an attacker supplies an unrecognized `auth_mode` value in the HTTP `Authorization: Basic` header, the function does not return `nil`/`false` but an unpopulated yet "truthy" table — "if an attacker supplied an unrecognized auth_mode, the user_authenticate function did not explicitly reject the request by returning nil or false. Instead, it returned an unpopulated table: { user = nil, role = nil, recovery = nil }" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)) — and the router downstream checks only that something was returned, not its contents, so the malformed request slips through unauthenticated.

One of the three pre-auth paths is a deterministic admin-password generator: the credential is derived via a key-derivation function from a hardcoded firmware seed identical across the product line, plus the device's MAC address and the current date, both obtainable via unauthenticated public endpoints, so once an attacker has those two values, valid admin credentials can be computed offline: "because the seed values are identical across the product line and the variables (MAC address and date) can be obtained via unauthenticated public endpoints, an adversary can reconstruct the entire derivation chain offline" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)). A third pre-auth path, CVE-2026-24663 (CVSS 9.0), is an unauthenticated OS command injection reachable by sending a crafted request to the libraries installation route, with no authentication step to bypass at all.

Eighteen further CVEs (all listed above) are OS command-injection flaws across API/CGI endpoints (contacts import, firmware update, device templates, network/Wi-Fi configuration, the Modbus debug tool, the SMS service settings and others), each requiring prior authentication and each scored CVSS 8.0; Claroty documents seventeen of them ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)), and CISA's advisory adds CVE-2026-3037, injected through the MBird SMS service URL or code on the utility route ([CISA, 2026-02-26](https://www.cisa.gov/news-events/ics-advisories/icsa-26-057-10)). CISA also lists two low-severity flaws reachable without authentication: an arbitrary file read (CVE-2026-22877, CVSS 3.7) and a stack-based buffer overflow in an API route that terminates the program (CVE-2026-20797, CVSS 4.3) ([CISA, 2026-02-26](https://www.cisa.gov/news-events/ics-advisories/icsa-26-057-10)). All are served by an embedded lighttpd instance where unsanitized user input reaches Lua system-execution calls running with elevated privileges — any of the three pre-auth primitives above chains directly to root: "since these services run with elevated privileges, successful exploitation results in immediate root-level code execution on the controller" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)). Claroty built a live physical demonstration: from an internet-exposed XWEB controller, an attacker works out the connected field controller's Modbus register addresses, many of which are not publicly documented, from the XR60CX datasheet and protocol analysis, and can set the temperature shown on the XR60CX display to any value while silently disabling cooling — spoiled food, or compromised temperature-sensitive medical supplies for pharmaceutical cold-chain. Copeland shipped firmware v1.13 through coordinated disclosure, fixing all 23 issues: "Copeland worked closely and collaboratively with us to develop a comprehensive remediation strategy. The vendor successfully patched these vulnerabilities and has uploaded firmware update version 1.13" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)); no source read reports exploitation of these flaws in the wild, but CERT-FR's alert of 2026-10-13 reports numerous compromises of Copeland xweb controllers without naming models, flaws or the entry vector ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)).

An anonymous, single-request path to full administrative control of internet-exposed cold-chain infrastructure demands action beyond a routine patch cycle, independent of confirmed exploitation: absence of exploitation is not evidence of safety when the exploit is a MAC address. Internet-exposed commercial refrigeration and cold-storage deployments are directly relevant to healthcare and food-safety cold-chain operations. **Triage:** the falsified display is itself the detection challenge: Claroty shows the temperature on the XR60CX field controller's display can be set to any value, so a normal reading on the display does not show that cooling is running; any authentication attempt using an `auth_mode` value the deployment does not use is a probe worth alerting on.

## Correction — 2026-08-30T13:12:06Z

Which CVE identifier covers the deterministic admin-password path is **not** something Claroty states, and this entry previously asserted it. Claroty's per-CVE table describes CVE-2026-21718 only as "an authentication bypass vulnerability... enabling any attackers to bypass the authentication requirement and achieve pre-authenticated code execution" with a CVSS v3 of 10.0, while the section walking through the MAC-address-and-date key derivation attaches no identifier to it ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)). The three pre-auth paths and the mechanism of each are unchanged, and so is the remediation: firmware v1.13 fixes the disclosed set. What changes is that an operator matching a specific identifier against a vendor patch note or an asset-management ticket should not expect CVE-2026-21718 to be documented anywhere as the password-derivation bug.

## Update — 2026-10-14T03:45:00Z

CERT-FR revised its alert on refrigeration-controller compromises on 2026-10-13: it now says it knows of numerous compromises of the remote controllers Danfoss AK-SM and AK-SC as well as Copeland xweb and Dixell xweb, that attack campaigns are probably still ongoing, and that access should come back only through a secure VPN or protected network, with filtering to the refrigeration contractors' source addresses accepted only as an emergency measure ([CERT-FR, 2026-10-13](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)). The alert names no Copeland models, no vulnerability and no entry vector, and does not tie the compromises to Claroty's findings, so it is not established that CVE-2026-25085 or any other flaw above was used.

## Correction — 2026-10-19T21:06:23Z

CISA published an ICS advisory for these flaws on 2026-02-26, ICSA-26-057-10, contrary to the earlier statement that it could not be located; it lists all 23 identifiers with a summary and score each ([CISA, 2026-02-26](https://www.cisa.gov/news-events/ics-advisories/icsa-26-057-10)). The three not recorded before are CVE-2026-3037, an authenticated OS command injection through the MBird SMS service URL or code on the utility route (CVSS 8.0), so the authenticated command-injection flaws number eighteen, not seventeen; CVE-2026-22877, an arbitrary file read without authentication (CVSS 3.7); and CVE-2026-20797, a stack-based buffer overflow in an API route, reachable without authentication, that terminates the program (CVSS 4.3) ([CISA, 2026-02-26](https://www.cisa.gov/news-events/ics-advisories/icsa-26-057-10)). CVE-2026-21718 is an authentication bypass, as both Claroty and CISA call it, not a logic flaw ([CISA, 2026-02-26](https://www.cisa.gov/news-events/ics-advisories/icsa-26-057-10)).

Three descriptions above are corrected. The admin password is computed offline once the attacker has the MAC address and the date, which Claroty says can be obtained via unauthenticated public endpoints; the earlier "zero interaction with the target" overstated that ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)). The supervisory controller reaches its field controllers over an RS485 serial network using Modbus, and Ethernet is its own network connection, not a field-device link ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)). Claroty says the register addresses for many functions are not publicly documented and that it built the map from the XR60CX datasheet and protocol analysis ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)). The sectors now read retail and healthcare, which Claroty names through supermarkets, food distribution and healthcare facilities, in place of energy, which no source supports ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers)); with CISA's advisory the flaws rest on two sources. The remediation is unchanged.
