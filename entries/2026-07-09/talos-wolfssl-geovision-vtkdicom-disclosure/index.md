---
schema: 1
kind: vulnerability
title: "Cisco Talos batch disclosure: wolfSSL PKI name-constraint bypasses, GeoVision command injection, and a VTK-DICOM heap overflow (41 CVEs)"
headline: "Talos discloses 41 patched CVEs: wolfSSL silently ignores IP/registeredID cert name constraints, GeoVision GV-I/O boxes take a high-privilege command injection"
summary: >
  Cisco Talos published a coordinated-disclosure roundup (2026-07-09) of 41
  vendor-patched CVEs across three products relevant to this constituency: two
  wolfSSL flaws (CVSS 9.1 / 7.4) that make the embedded TLS library silently
  accept certificates violating iPAddress and registeredID name constraints —
  quietly defeating a sub-CA scoping control — plus a PKCS#7 heap overflow;
  a high-privilege (PR:H) OS command-injection cluster (CVSS 9.1) in GeoVision
  GV-I/O Box 4E physical-security hardware; an unauthenticated GeoWebPlayer
  screen-capture bug (CVSS 8.8); and a VTK-DICOM heap overflow (CVSS 8.1) on
  crafted medical-imaging files. No in-the-wild exploitation; all patched.
discovered_at: "2026-07-09T20:40:00Z"
event_date: "2026-07-09"
run_id: 2026-07-09T2009Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, ot-ics, patch-available, poc-public]
regions: [global]
sectors: [healthcare, public-sector, technology]
entities: []
techniques: [T1553, T1190, T1189, T1203]
affected_products: ["wolfSSL", "GeoVision GV-I/O Box 4E", "GeoVision GeoWebPlayer", "vtk-dicom"]
cves:
  - id: CVE-2026-7532
    cvss: "9.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available, poc-public]
    affected: "wolfSSL 5.9.1"
    fixed: "vendor-patched (see wolfSSL advisory)"
  - id: CVE-2026-5263
    cvss: "7.4"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available, poc-public]
    affected: "wolfSSL 5.9.1"
    fixed: "vendor-patched (see wolfSSL advisory)"
  - id: CVE-2026-6678
    cvss: "7.5"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available, poc-public]
    affected: "wolfSSL 5.9.1"
    fixed: "vendor-patched (see wolfSSL advisory)"
  - id: CVE-2026-12486
    cvss: "9.1"
    epss: null
    type: rce
    vector: zero-click
    auth: admin-required
    status: [patch-available, poc-public]
    affected: "GeoVision GV-I/O Box 4E 2.09"
    fixed: "vendor-patched 2026-04-28"
  - id: CVE-2026-13125
    cvss: "8.8"
    epss: null
    type: info-disclosure
    vector: user-interaction
    auth: pre-auth
    status: [patch-available, poc-public]
    affected: "GeoVision GeoWebPlayer version 1.1.1.0"
    fixed: "vendor-patched (see GeoVision advisory)"
  - id: CVE-2026-22879
    cvss: "8.1"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available, poc-public]
    affected: "VTK-DICOM 9.5.2"
    fixed: "vendor-patched (see VTK-DICOM advisory)"
sources:
  - url: "https://blog.talosintelligence.com/wolfssl-vulnerabilities/"
    publisher: "Cisco Talos"
    date: "2026-07-09"
    role: primary
  - url: "https://talosintelligence.com/vulnerability_reports/TALOS-2026-2379"
    publisher: "Cisco Talos (TALOS-2026-2379)"
    date: "2026-07-09"
    role: corroborating
  - url: "https://talosintelligence.com/vulnerability_reports/TALOS-2026-2409"
    publisher: "Cisco Talos (TALOS-2026-2409)"
    date: "2026-07-09"
    role: corroborating
  - url: "https://talosintelligence.com/vulnerability_reports/TALOS-2026-2410"
    publisher: "Cisco Talos (TALOS-2026-2410)"
    date: "2026-07-09"
    role: corroborating
  - url: "https://talosintelligence.com/vulnerability_reports/TALOS-2026-2408"
    publisher: "Cisco Talos (TALOS-2026-2408)"
    date: "2026-07-09"
    role: corroborating
  - url: "https://talosintelligence.com/vulnerability_reports/TALOS-2026-2370"
    publisher: "Cisco Talos (TALOS-2026-2370)"
    date: "2026-07-09"
    role: corroborating
  - url: "https://talosintelligence.com/vulnerability_reports/TALOS-2026-2366"
    publisher: "Cisco Talos (TALOS-2026-2366)"
    date: "2026-07-09"
    role: corroborating
closed_sources: []
evidence:
  - quote: "In some configurations wolfSSL will silently fail to add IP Address GeneralName mappings to the certificate's alternative names list, causing IP addresses outside of the permitted range to be treated as valid."
    publisher: "Cisco Talos (TALOS-2026-2409)"
  - quote: "The following function takes a string as an ip address, performs no sanitization and calls system. This is a classic command injection vulnerability. The function is reachable from both the network-exposed DVRSearch service and the Network.cgi endpoint."
    publisher: "Cisco Talos (TALOS-2026-2379)"
  - quote: "The vulnerabilities mentioned in this blog post have been patched by their respective vendors, in adherence to Cisco's third-party vulnerability disclosure policy."
    publisher: "Cisco Talos"
verification: single-source
sourcing_note: "Cisco Talos is the sole coordinating discloser across all 41 CVEs (the blog plus the per-CVE TALOS advisory pages are one publisher); the findings are corroborated only by the vendor patches Talos states have shipped. Treated as single-source pending independent write-ups."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions:
  - "If you rely on wolfSSL-based TLS validation with constrained sub-CAs, do not assume the client enforces name constraints: patch wolfSSL and review any trust model that depends on iPAddress or registeredID SAN name-constraint enforcement, which wolfSSL silently skipped."
  - "Inventory GeoVision physical-security hardware (GV-I/O boxes, DVR/NVR, GV-VMS/GV-Cloud, GeoWebPlayer) in facilities; confirm firmware is on the vendor-patched builds and that management interfaces (DVRSearch discovery, Network.cgi) are off any network reachable by untrusted hosts."
  - "For healthcare imaging pipelines that ingest external DICOM files via VTK-DICOM, patch to the fixed release and hunt for DICOM-parsing processes crashing/aborting on ingest as a sign of malformed-file submission."
migrated_from: null
---

Cisco Talos' Vulnerability Discovery & Research team published a coordinated-disclosure roundup on 2026-07-09 — three wolfSSL, 37 GeoVision (across 14 advisories) and one VTK-DICOM CVE, 41 in total, all patched by their respective vendors under Cisco's third-party disclosure policy ([Cisco Talos, 2026-07-09](https://blog.talosintelligence.com/wolfssl-vulnerabilities/)). In **wolfSSL 5.9.1** (embedded TLS for IoT/RTOS/medical/embedded devices), two X.509 name-constraint bugs let a subordinate CA issue certificates outside its permitted scope and have them accepted anyway, subverting a trust control (`T1553`): CVE-2026-7532 (CVSS 9.1) — the iPAddress SAN branch is compiled out unless `WOLFSSL_IP_ALT_NAME` is defined, silently skipping constraint enforcement for any certificate carrying an iPAddress SAN ([Talos TALOS-2026-2409, 2026-07-09](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2409)) — and CVE-2026-5263 (CVSS 7.4) — `ConfirmNameConstraints()` iterates a fixed GeneralName-type array that omits `ASN_RID_TYPE`, so registeredID SANs bypass constraint checking in every build ([Talos TALOS-2026-2410, 2026-07-09](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2410)). A third, CVE-2026-6678 (CVSS 7.5), is an integer underflow in PKCS#7 `OtherRecipientInfo` parsing that produces a heap buffer overflow with a stated path to code execution ([Talos TALOS-2026-2408, 2026-07-09](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2408)).

Talos separately disclosed 37 CVEs across GeoVision physical-security/CCTV/access-control hardware. The most severe is an OS command-injection cluster led by CVE-2026-12486 (CVSS 9.1) in **GV-I/O Box 4E 2.09**: a function builds a shell command string from an attacker-controlled IP/netmask/gateway/DNS value with no sanitisation and passes it to `system()`, reachable over the network from the DVRSearch discovery service and the `Network.cgi` endpoint — though Talos scores it `PR:H`, i.e. requiring high privileges rather than fully unauthenticated (`T1190`) ([Talos TALOS-2026-2379, 2026-07-09](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2379)). CVE-2026-13125 (CVSS 8.8) is a missing-authentication flaw in **GeoWebPlayer** version 1.1.1.0 (shipped with GV-VMS/GV-Cloud): it opens an unauthenticated WebSocket server on localhost, so any webpage a victim visits can connect and invoke screen-capture APIs to exfiltrate their screen (`T1189`) ([Talos TALOS-2026-2370, 2026-07-09](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2370)). Finally, **VTK-DICOM 9.5.2** (used to parse DICOM CT/MRI data) carries CVE-2026-22879 (CVSS 8.1), an improper-array-index heap overflow where a crafted DICOM file corrupts heap-chunk metadata and aborts the process — a client-side surface for hospital PACS/imaging pipelines that ingest external DICOM (`T1203`) ([Talos TALOS-2026-2366, 2026-07-09](https://talosintelligence.com/vulnerability_reports/TALOS-2026-2366)).

**Defender takeaway:** none of the 41 has confirmed in-the-wild exploitation and all are patched (the GeoVision fixes shipped 2026-04-28, ~3 months before this public disclosure), so this is not an out-of-band scramble — but two threads deserve more than patch-and-forget. The wolfSSL name-constraint bugs quietly defeat a PKI control organisations may believe they enforce, so any trust model leaning on constrained sub-CAs with IP/registeredID SANs warrants an internal cert-validation review, not just a library bump. And the GeoVision GV-I/O command-injection chain is a network-reachable command-injection RCE in facility hardware that turns up in public-sector and CI security stacks — the advisory rates it high-privilege, so weak or default management credentials are what turn it into a practical path; asset owners should confirm patched firmware, strong credentials, and network isolation of the management interfaces. **Triage:** for the GeoVision cluster the discriminator is a network-service process on an embedded camera/IO-box spawning a shell (network-configuration utilities via `system()`) — anomalous for that device class; for GeoWebPlayer, an unexpected local WebSocket connection originating from browser-rendered content; for VTK-DICOM, a DICOM-parsing process crashing on ingest, which should prompt a hunt for repeated malformed-file submissions.
