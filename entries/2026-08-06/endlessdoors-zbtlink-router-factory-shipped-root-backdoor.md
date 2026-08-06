---
schema: 1
kind: vulnerability
horizon: operational
title: "ENDLESSDOORS (CVE-2026-66747) — twenty Zbtlink router models ship from the factory with an unauthenticated root-command backdoor, and the discloser's remedy is replacement"
headline: "The implant is not an intrusion — it is a vendor component started by the vendor's own init script"
summary: >
  VulnCheck documented ENDLESSDOORS on 2026-08-05, a pre-installed remote-access implant enabled by default on
  twenty Zbtlink router and CPE models, including units rebranded under another name and sold through
  mainstream e-commerce; VulnCheck notes the true affected population might be larger than the twenty it examined. The implant is a customised build of the open-source rctl tool, launched at boot by the
  vendor's own init script and masquerading as a kernel worker thread. It registers outbound to hardcoded
  command-and-control hosts and then passes whatever the server sends straight to a shell as uid 0, with no
  handshake, key exchange or authentication of any kind, and a second command opens an interactive reverse shell.
  Because this is a shipped component rather than a memory-corruption defect, VulnCheck's guidance is to replace
  affected devices, or at minimum place them behind strict egress control and treat their LAN as untrusted. Zbtlink
  has offered nothing: VulnCheck says it did not notify the vendor, on the reasoning that there is no patch to
  coordinate.
discovered_at: "2026-08-06T04:11:48Z"
event_date: "2026-08-05"
run_id: 2026-08-06T0411Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, supply-chain, pre-auth, no-patch, default-config]
regions: [global]
sectors: [telco, public-sector]
entities:
  - tool:endlessdoors
techniques: [T1059, T1571, T1036]
affected_products: ["Zbtlink WE1026-5G-WD", "Zbtlink WE1326", "Zbtlink WE2007", "Zbtlink WE2008-DSIM", "Zbtlink WE2416", "Zbtlink WE3326", "Zbtlink WE5927", "Zbtlink WE5931", "Zbtlink WE5931AC", "Zbtlink WE826-T3-DSIM", "Zbtlink WG108", "Zbtlink WG1602", "Zbtlink WG1608-DSIM", "Zbtlink WG209", "Zbtlink WG2105", "Zbtlink WG2107", "Zbtlink WG259", "Zbtlink WG3526", "Zbtlink Z8102AX-2DSIM", "Zbtlink CPE2801"]
cves:
  - id: CVE-2026-66747
    cvss: null
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "Twenty Zbtlink router and CPE models and their rebranded equivalents, as shipped"
    fixed: "No fix offered and no vendor advisory exists. VulnCheck's stated remediation is to replace the device, or at minimum move it behind strict egress control and treat its LAN as untrusted; disabling the init script is possible with shell access but leaves the rest of the shipped image trusted."
sources:
  - url: "https://www.vulncheck.com/blog/zbt-endlessdoors"
    publisher: "VulnCheck"
    date: "2026-08-05"
    role: primary
closed_sources: []
evidence:
  - quote: "There is no handshake, no key exchange, no negotiation."
    publisher: "VulnCheck"
  - quote: "started at boot by the vendor's own init script"
    publisher: "VulnCheck"
verification: single-source
sourcing_note: >
  VulnCheck is the only party reporting this; no second researcher, CERT or vendor statement corroborates it at the
  time of writing, and Zbtlink has published no response. The finding is first-hand reverse-engineering of the
  implant and its command protocol by the discloser, and a CVE identifier has been assigned, which is why confidence
  is high despite the single source. No CVSS score is carried here because the discloser publishes none, and this
  entry does not invent one.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

VulnCheck published an analysis on 2026-08-05 of what it names ENDLESSDOORS, a remote-access implant pre-installed on twenty router and CPE models from Zbtlink (Shenzhen Zhibotong Electronics), including units sold under a rebranded name through mainstream e-commerce platforms ([VulnCheck, 2026-08-05](https://www.vulncheck.com/blog/zbt-endlessdoors)). The implant is a customised build of the open-source rctl remote-control tool. VulnCheck's framing is the point of the research: this is not a memory-corruption bug in a parser but a component in the vendor's product, started at boot by the vendor's own init script, shipped across twenty models ([VulnCheck, 2026-08-05](https://www.vulncheck.com/blog/zbt-endlessdoors)).

Operationally, the device registers itself outbound to hardcoded command-and-control hosts with a short unauthenticated message carrying a device-class label and the unit's MAC address, and from that point there is no handshake, no key exchange, no negotiation — whatever the server sends afterwards is handed to a shell and executed as uid 0, with a separate command spinning up an interactive reverse shell ([VulnCheck, 2026-08-05](https://www.vulncheck.com/blog/zbt-endlessdoors)). The implant hides in plain sight by taking the name of a kernel worker thread, which in a process listing sits alongside the genuine kernel threads it imitates ([VulnCheck, 2026-08-05](https://www.vulncheck.com/blog/zbt-endlessdoors)). Because control depends only on reaching the device's chosen server rather than on any credential, whoever controls that infrastructure — or anyone who takes it over — controls every unit that still calls home. VulnCheck's guidance is to segment or replace: for anything carrying real traffic it advises replacing the device, or at minimum moving it behind strict egress control and treating its LAN as untrusted, noting that disabling the init script with shell access still leaves you trusting the rest of an image that shipped the implant ([VulnCheck, 2026-08-05](https://www.vulncheck.com/blog/zbt-endlessdoors)). No vendor remedy exists to weigh against that: VulnCheck states it did not notify Zbtlink, because there is no patch to coordinate and an early warning would reach whoever operates the command infrastructure rather than the device owners ([VulnCheck, 2026-08-05](https://www.vulncheck.com/blog/zbt-endlessdoors)).

**Defender takeaway:** the relevance to a public-sector estate is rarely the data-centre and almost always the edge — cheap rebranded CPE turns up in branch offices, temporary sites, remote telemetry installations and home-working kits, procured outside the normal hardware channel and therefore frequently absent from the asset register. The tractable question is not "do we run Zbtlink" but "do we know what CPE terminates our remote sites", and the answer is discoverable from the network side without touching the devices. Two observable behaviours make this findable: a device masquerading as a kernel thread is distinguishable because genuine kernel threads are presented differently by the operating system than a userspace process wearing the same name, so a process listing from any managed unit separates them; and network-side, an unsolicited outbound registration from consumer-class CPE to a fixed external host, followed by an inbound-driven command channel on a high non-standard port, is not traffic that ordinary router firmware generates. Egress telemetry at the site boundary shows this even where the device itself is unmanaged.

**Triage:** routers legitimately make outbound connections for firmware update checks, NTP and vendor telemetry, so outbound-from-CPE alone is normal. The discriminators are that this connection persists as a long-lived channel rather than completing a transaction and closing, that the traffic is command-carrying in both directions rather than a fetch, and that it targets a fixed vendor-independent host on a high port rather than a documented update endpoint on standard ports.
