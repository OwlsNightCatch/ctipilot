---
schema: 1
kind: vulnerability
horizon: operational
title: "CVE-2026-7849 and 19 more — Phoenix Contact CHARX SEC-3xxx EV charging controllers: unauthenticated command injection as root, unsigned firmware updates, and no fix released at disclosure"
headline: "CERT@VDE publishes 20 CVEs in Phoenix Contact EV charging controllers with the fixing firmware unreleased — segmentation is the only control to 12 August"
summary: >
  CERT@VDE published VDE-2026-008 on 2026-07-30 covering 20 vulnerabilities in the firmware of
  Phoenix Contact CHARX SEC-3000, SEC-3050, SEC-3100 and SEC-3150 EV charging controllers, all
  versions below firmware 1.9.1. Five carry CVSS 3.1 9.8 with an unauthenticated network vector,
  including command injection into the system configuration that executes as root (CVE-2026-7849),
  a firmware update path that validates only a CRC32 checksum with no cryptographic signature
  verification (CVE-2026-44104), and missing authentication on the OCPP agent service that lets a
  remote attacker reconfigure the charge point's backend connection (CVE-2026-44101). The remediating
  firmware 1.9.1 was not available when the advisory published — Phoenix Contact committed to shipping
  it no later than 2026-08-12 — so for roughly two weeks the vendor's only offered control is running
  the devices in closed networks behind a firewall.
discovered_at: "2026-08-02T13:55:00Z"
event_date: "2026-07-30"
run_id: 2026-08-02T1309Z-audit
priority: high
immediate_action: null
tags: [vulnerabilities, ot-ics, rce, pre-auth, auth-bypass, no-patch, dos]
regions: [europe, global, dach]
sectors: [energy, transport, public-sector]
entities: []
techniques: [T1190, T1542.001]
affected_products: ["Phoenix Contact CHARX SEC-3000", "Phoenix Contact CHARX SEC-3050", "Phoenix Contact CHARX SEC-3100", "Phoenix Contact CHARX SEC-3150"]
cves:
  - id: CVE-2026-7849
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [no-patch, mitigation-only]
    affected: "Read from the affected-products table of CERT@VDE VDE-2026-008: CHARX SEC-3000 (1139022), SEC-3050 (1139018), SEC-3100 (1139012) and SEC-3150 (1138965), firmware below FW 1.9.1. Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, weakness CWE-77."
    fixed: "Per the advisory's remediation block, firmware 1.9.1 addresses the vulnerabilities but was NOT yet available at publication: Phoenix Contact states it will be released no later than 2026-08-12, via the download section of each product page."
  - id: CVE-2026-44104
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [no-patch, mitigation-only]
    affected: "Same four models below FW 1.9.1; CWE-347, the basemodule firmware update process validates only a CRC32 checksum with no cryptographic signature verification."
    fixed: "Firmware 1.9.1, unreleased at publication; committed no later than 2026-08-12."
  - id: CVE-2026-44101
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [no-patch, mitigation-only]
    affected: "Same four models below FW 1.9.1; CWE-306, missing authentication on the CHARX OCPP Agent service."
    fixed: "Firmware 1.9.1, unreleased at publication; committed no later than 2026-08-12."
  - id: CVE-2026-44090
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [no-patch, mitigation-only]
    affected: "Same four models below FW 1.9.1; CWE-306, the MQTT broker is reachable without authentication and is protected from external access only by the device firewall."
    fixed: "Firmware 1.9.1, unreleased at publication; committed no later than 2026-08-12."
  - id: CVE-2026-44108
    cvss: "9.8"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [no-patch, mitigation-only]
    affected: "Same four models below FW 1.9.1; CWE-696, the firewall terminates prematurely during shutdown because of script execution order."
    fixed: "Firmware 1.9.1, unreleased at publication; committed no later than 2026-08-12."
sources:
  - url: "https://certvde.com/en/advisories/VDE-2026-008/"
    publisher: "CERT@VDE"
    date: "2026-07-30"
    role: primary
closed_sources: []
evidence:
  - quote: "Due to improper neutralization of special elements, an unauthenticated remote attacker is able to inject a command into the system configuration which is subsequently executed as root."
    publisher: "CERT@VDE"
  - quote: "The updated firmware will be made available as soon as possible, but no later than August 12, 2026."
    publisher: "CERT@VDE"
  - quote: "Due to a flaw in the execution order of scripts during shutdown, the firewall is terminated prematurely during system shutdown. This creates a temporary window in which internal services may become externally accessible, potentially allowing an unauthenticated remote attacker to connect to these services, resulting in full system compromise."
    publisher: "CERT@VDE"
verification: single-source
sourcing_note: "Single source, deliberately not claimed under the national-CERT carve-out: CERT@VDE is the coordinating CERT for German industrial-automation vendors rather than a national CERT, so the carve-out does not apply even though it published VDE-2026-008 as Phoenix Contact's coordinated disclosure and is the first-party authority for every id, score, vector, weakness and version boundary here — all read from the advisory's structured per-CVE blocks and affected-products table. The advisory credits ZDI for reporting and CERT@VDE for coordination. Only 5 of the 20 CVEs are carried in cves[]: the unauthenticated CVSS 9.8 set that drives the disposition. No independent second party has published analysis, so credibility is 2."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Locate every CHARX SEC-3000/3050/3100/3150 controller in your estate and confirm none answers from outside the charging network — the vendor's only offered control until firmware 1.9.1 ships is closed-network operation behind a firewall, and one of the flaws makes the on-device firewall itself unavailable for a window during every shutdown."
  - "Put a calendar item on 2026-08-12 to check each product's download page for firmware 1.9.1 and schedule the update — the advisory names that date as the vendor's committed release deadline, and until it lands there is nothing to patch."
migrated_from: null
---

This is a recovery published by the 2026-08-02 weekly quality audit: the advisory landed inside the audit window and no entry covered it.

An advisory that lands before its own fix is unusual enough to change the defender's task from patching to containment, and this one lands with five unauthenticated CVSS 9.8 issues. The most direct is CVE-2026-7849: "Due to improper neutralization of special elements, an unauthenticated remote attacker is able to inject a command into the system configuration which is subsequently executed as root" ([CERT@VDE, 2026-07-30](https://certvde.com/en/advisories/VDE-2026-008/)) — no credential, no interaction, root on the controller. CVE-2026-44104 is the one with the longest tail: the basemodule firmware update process validates a "CRC32 checksum without cryptographic signature verification", and "This allows an unauthenticated remote attacker to install a modified firmware, resulting in full system compromise." A CRC32 is an accidental-corruption check, not an authenticity check, and firmware an attacker chose survives every subsequent reboot and legitimate update cycle — which is why this flaw outlives the patch for any device compromised before 1.9.1 is applied.

Two more are about services that were never meant to be reachable. CVE-2026-44101 removes authentication from the CHARX OCPP Agent, the component that speaks the Open Charge Point Protocol to the operator's backend: a remote attacker can reconfigure which backend the charge point talks to, which the advisory records as leading to denial of service and disclosure of confidential data. CVE-2026-44090 leaves the MQTT broker reachable without authentication, "protected from external access by a firewall" and nothing else. And CVE-2026-44108 undermines exactly that firewall: "Due to a flaw in the execution order of scripts during shutdown, the firewall is terminated prematurely during system shutdown. This creates a temporary window in which internal services may become externally accessible, potentially allowing an unauthenticated remote attacker to connect to these services, resulting in full system compromise." The vendor's stated mitigation is a firewall, and one of the twenty flaws is that the firewall goes away during every shutdown — so the mitigation has to be enforced by the network, not by the device.

The constituency nexus is direct rather than analogical. Public EV charging sits across two of the profiled sectors at once — energy, because charge points are grid-edge load, and transport, because municipal and fleet charging is increasingly run by cantonal and communal operators or their contractors. Phoenix Contact is a German industrial-automation supplier with a wide European installed base, and CHARX SEC controllers are the charge-point control units rather than back-office software, so the affected devices are physically distributed, frequently connected over operator or mobile networks, and rarely in a mature patch cycle. Phoenix Contact's own framing is that the "charging controllers are designed and developed for the use in closed industrial networks" — which is a statement about intended deployment, and worth checking against how they actually got deployed.

**Defender takeaway:** for the next fortnight this is purely an exposure-reduction exercise, because there is nothing to install. Enumerate CHARX SEC-3xxx units — including any reached through an integrator's cellular modem and therefore absent from the asset register — and confirm that neither the web interface, the OCPP agent, nor the MQTT broker answers from outside the charging network. Enforce that upstream of the device: the shutdown-window flaw means the controller's own firewall cannot be the boundary you rely on. Where an operator's backend connection crosses the public internet, that path is the one to broker through a gateway rather than expose. Then treat 12 August as a hard date rather than a hope, and validate the firmware image against the vendor's published hash when it ships — the signature-verification flaw means the device itself will not tell you whether what you are installing is genuine.

**Triage:** these devices produce very little telemetry, so the discriminators live on the network rather than the host. Legitimate OCPP traffic goes from the charge point to one known operator backend on a stable endpoint; a reconfiguration attack shows up as the same device suddenly establishing OCPP or WebSocket sessions to a different destination, which is a single-field comparison against an expected-backend list and needs no deep inspection. Legitimate MQTT on these units is local to the charging installation; an MQTT connection sourced from outside the charging VLAN is not a tuning question. And an unscheduled reboot followed by a firmware version that does not match the change record is the manifestation of the unsigned-update flaw — worth an inventory-diff job rather than an alert rule, since a charge point that quietly changed firmware version is the observable that matters and no log on the device will report it.
