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
updated_at: "2026-08-29T04:09:36Z"
event_date: "2026-08-05"
run_id: 2026-08-06T0411Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, supply-chain, pre-auth, no-patch, default-config]
regions: [global]
sectors: [telco, public-sector]
entities:
  - tool:endlessdoors
  - tool:darklantern
  - tool:speakingstone
techniques: [T1059, T1571, T1036, T1572]
affected_products: ["Zbtlink WE1026-5G-WD", "Zbtlink WE1326", "Zbtlink WE2007", "Zbtlink WE2008-DSIM", "Zbtlink WE2416", "Zbtlink WE3326", "Zbtlink WE5927", "Zbtlink WE5931", "Zbtlink WE5931AC", "Zbtlink WE826-T3-DSIM", "Zbtlink WG108", "Zbtlink WG1602", "Zbtlink WG1608-DSIM", "Zbtlink WG209", "Zbtlink WG2105", "Zbtlink WG2107", "Zbtlink WG259", "Zbtlink WG3526", "Zbtlink Z8102AX-2DSIM", "Zbtlink CPE2801", "ZBT-WE826-T2 and rebrands (Deep Orange)", "Digineo AC1200 Pro (ZBT WG3526 OEM, rebrand lineage match — implant presence unconfirmed)", "ALLNET ALL-WR1200AC-WRT (ZBT WG2626 OEM, rebrand lineage match — implant presence unconfirmed)", "OneX RV WIFI Route (ZBT-WE826 rebrand lineage match — implant presence unconfirmed)", "WiFlyer WG3526 (ZBT WG3526 OEM)"]
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
  - url: "https://www.vulncheck.com/blog/zbt-darklantern-speakingstone"
    publisher: "VulnCheck"
    date: "2026-08-27"
    role: primary
  - url: "https://www.heise.de/news/OEM-China-Router-von-ZBT-mit-Backdoors-11433072.html"
    publisher: "heise Security"
    date: "2026-08-28"
    role: corroborating
closed_sources: []
evidence:
  - quote: "There is no handshake, no key exchange, no negotiation."
    publisher: "VulnCheck"
  - quote: "started at boot by the vendor's own init script"
    publisher: "VulnCheck"
  - quote: "The router's default firewall explicitly allows inbound connections to this port from anywhere on the internet."
    publisher: "VulnCheck"
  - quote: "Between August 18, 2026 and August 21, 2026 we’ve identified 203 internet-facing DARKLANTERN instances across 22 countries."
    publisher: "VulnCheck"
  - quote: "390 of 392 devices are in China. 83% are on China Mobile's network."
    publisher: "VulnCheck"
verification: single-source
sourcing_note: >
  VulnCheck is the only party reporting this; no second researcher, CERT or vendor statement corroborates it at the
  time of writing, and Zbtlink has published no response. The finding is first-hand reverse-engineering of the
  implant and its command protocol by the discloser, and a CVE identifier has been assigned, which is why confidence
  is high despite the single source. No CVSS score is carried here because the discloser publishes none, and this
  entry does not invent one. The 2026-08-27 follow-up (DARKLANTERN, SPEAKINGSTONE) is likewise VulnCheck's sole,
  first-hand reverse-engineering and internet-scan/sinkhole work; heise's 2026-08-28 article is journalism relaying
  that research rather than independent technical corroboration, so the entry remains single-source.
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
updates:
  - at: "2026-08-29T04:09:36Z"
    run_id: 2026-08-29T0409Z-intel
    type: update
    summary: >
      VulnCheck published a follow-up on 2026-08-27 tracing the ZBT/Zbtlink supply chain further and finding two
      more pre-installed implants: DARKLANTERN, an unauthenticated WAN-listening command backdoor on UDP/9992
      reachable by design through the router's own default firewall rules, and SPEAKINGSTONE, a phone-home implant
      beaconing to ZBT's own Alibaba Cloud infrastructure over UDP/10000. VulnCheck's internet scan found 203
      DARKLANTERN-responsive devices across 22 countries between 18-21 August, and sinkholed SPEAKINGSTONE's
      abandoned backup domain to capture 392 beacons, 390 of them from China and 83% on China Mobile's network —
      evidence VulnCheck reads as a domestic Chinese surveillance deployment running the same firmware lineage sold
      to Americans through Amazon. Supply-chain tracing extends the confirmed OEM-rebrand list to Germany (Digineo
      AC1200 Pro, ALLNET ALL-WR1200AC-WRT) alongside existing US, Canadian and Australian rebrands, though VulnCheck
      is explicit that not every rebrand is confirmed to carry the same implants. No CVE has been assigned to
      either new implant; the follow-up post does not itself restate remediation guidance, so the original
      ENDLESSDOORS device-replacement guidance remains the only position on record.
    fields: [entities, techniques, affected_products, sources, evidence, sourcing_note, body]
migrated_from: null
---

VulnCheck published an analysis on 2026-08-05 of what it names ENDLESSDOORS, a remote-access implant pre-installed on twenty router and CPE models from Zbtlink (Shenzhen Zhibotong Electronics), including units sold under a rebranded name through mainstream e-commerce platforms ([VulnCheck, 2026-08-05](https://www.vulncheck.com/blog/zbt-endlessdoors)). The implant is a customised build of the open-source rctl remote-control tool. VulnCheck's framing is the point of the research: this is not a memory-corruption bug in a parser but a component in the vendor's product, started at boot by the vendor's own init script, shipped across twenty models ([VulnCheck, 2026-08-05](https://www.vulncheck.com/blog/zbt-endlessdoors)).

Operationally, the device registers itself outbound to hardcoded command-and-control hosts with a short unauthenticated message carrying a device-class label and the unit's MAC address, and from that point there is no handshake, no key exchange, no negotiation — whatever the server sends afterwards is handed to a shell and executed as uid 0, with a separate command spinning up an interactive reverse shell ([VulnCheck, 2026-08-05](https://www.vulncheck.com/blog/zbt-endlessdoors)). The implant hides in plain sight by taking the name of a kernel worker thread, which in a process listing sits alongside the genuine kernel threads it imitates ([VulnCheck, 2026-08-05](https://www.vulncheck.com/blog/zbt-endlessdoors)). Because control depends only on reaching the device's chosen server rather than on any credential, whoever controls that infrastructure — or anyone who takes it over — controls every unit that still calls home. VulnCheck's guidance is to segment or replace: for anything carrying real traffic it advises replacing the device, or at minimum moving it behind strict egress control and treating its LAN as untrusted, noting that disabling the init script with shell access still leaves you trusting the rest of an image that shipped the implant ([VulnCheck, 2026-08-05](https://www.vulncheck.com/blog/zbt-endlessdoors)). No vendor remedy exists to weigh against that: VulnCheck states it did not notify Zbtlink, because there is no patch to coordinate and an early warning would reach whoever operates the command infrastructure rather than the device owners ([VulnCheck, 2026-08-05](https://www.vulncheck.com/blog/zbt-endlessdoors)).

**Defender takeaway:** the relevance to a public-sector estate is rarely the data-centre and almost always the edge — cheap rebranded CPE turns up in branch offices, temporary sites, remote telemetry installations and home-working kits, procured outside the normal hardware channel and therefore frequently absent from the asset register. The tractable question is not "do we run Zbtlink" but "do we know what CPE terminates our remote sites", and the answer is discoverable from the network side without touching the devices. Two observable behaviours make this findable: a device masquerading as a kernel thread is distinguishable because genuine kernel threads are presented differently by the operating system than a userspace process wearing the same name, so a process listing from any managed unit separates them; and network-side, an unsolicited outbound registration from consumer-class CPE to a fixed external host, followed by an inbound-driven command channel on a high non-standard port, is not traffic that ordinary router firmware generates. Egress telemetry at the site boundary shows this even where the device itself is unmanaged.

**Triage:** routers legitimately make outbound connections for firmware update checks, NTP and vendor telemetry, so outbound-from-CPE alone is normal. The discriminators are that this connection persists as a long-lived channel rather than completing a transaction and closing, that the traffic is command-carrying in both directions rather than a fetch, and that it targets a fixed vendor-independent host on a high port rather than a documented update endpoint on standard ports.

## Update — 2026-08-29T04:09:36Z

VulnCheck traced the ZBT/Zbtlink supply chain further and published two additional pre-installed implants on the
same platform family ([VulnCheck, 2026-08-27](https://www.vulncheck.com/blog/zbt-darklantern-speakingstone)).
DARKLANTERN runs as the service `infosrvd` on UDP/9992, a port the router's default firewall explicitly opens to
the internet; an unauthenticated 19-byte probe returns the device's model, firmware, MAC address, SSID and public
IP, and a command packet passes an operator-supplied string directly to `system()`, where a semicolon breaks out of
the fixed command prefix into arbitrary root shell execution with no length limit or character filtering
([VulnCheck, 2026-08-27](https://www.vulncheck.com/blog/zbt-darklantern-speakingstone)). The only gating fields are
a keyed checksum computed from a hardcoded static salt and a MAC-address check that is bypassed outright by sending
an all-zero MAC. VulnCheck's internet scanner found 203 DARKLANTERN-responsive devices across 22 countries between
18 and 21 August 2026, self-reporting across 16 different router models
([VulnCheck, 2026-08-27](https://www.vulncheck.com/blog/zbt-darklantern-speakingstone)). SPEAKINGSTONE instead
beacons outbound over UDP/10000 to ZBT's own Alibaba Cloud infrastructure with a full device fingerprint, and
accepts plaintext, unauthenticated commands to run arbitrary shell commands, exfiltrate WAN PPPoE credentials,
write or read a DNS-hijack list, or open and close a reverse SSH tunnel; VulnCheck registered its abandoned
hardcoded backup domain and captured 392 beacons by 21 August — 390 from China, 83% on China Mobile's network, and
363 of them a single carrier-CPE model — which VulnCheck reads as a domestic Chinese surveillance deployment running
on the same firmware lineage sold to Americans through Amazon
([VulnCheck, 2026-08-27](https://www.vulncheck.com/blog/zbt-darklantern-speakingstone)). Supply-chain tracing via
FCC filings, trademark records and archived web pages extends the confirmed OEM-rebrand list — previously US,
Canadian and Australian units — to Germany: Digineo's AC1200 Pro and ALLNET's ALL-WR1200AC-WRT — though VulnCheck is
explicit that it has not confirmed every rebrand carries the same implants
([VulnCheck, 2026-08-27](https://www.vulncheck.com/blog/zbt-darklantern-speakingstone)). No CVE has been assigned to either new implant. The 2026-08-27 post does not restate VulnCheck's remediation
guidance or vendor-notification posture for DARKLANTERN/SPEAKINGSTONE specifically; VulnCheck's original ENDLESSDOORS
guidance — device replacement rather than a patch, and no notification to Zbtlink since there is no fix to
coordinate — is the only remediation position on record for this supply chain
([VulnCheck, 2026-08-05](https://www.vulncheck.com/blog/zbt-endlessdoors)).

Detection concept for the new implants: an unsolicited, long-lived, bidirectional command-carrying UDP channel from
consumer-class CPE to a fixed external host on a non-standard port (SPEAKINGSTONE's UDP/10000 beacon), or an
unauthenticated response to a 19-byte probe on UDP/9992 (DARKLANTERN), is not traffic ordinary router firmware
generates — egress/ingress telemetry at the site boundary surfaces this even for an unmanaged device. **Triage:**
routers legitimately make outbound connections for firmware checks, NTP and vendor telemetry, so outbound-from-CPE
alone is not a discriminator; the tell is the fixed vendor-independent destination and the bidirectional
command-carrying pattern, or an inbound-accepted session on 9992/8897 from an internet-routable source.
