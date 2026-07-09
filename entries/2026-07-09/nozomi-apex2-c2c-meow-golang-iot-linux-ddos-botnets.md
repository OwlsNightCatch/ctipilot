---
schema: 1
kind: threat
horizon: operational
title: "Nozomi documents two new Golang IoT/Linux DDoS botnets (Apex2, c2c/meow) built for speed and reuse over sophistication"
headline: "Two Golang DDoS botnets, Apex2 and c2c/meow, flood exposed Telnet/SSH Linux and IoT with fake-systemd persistence and passwordless-sudo escalation"
summary: >
  Nozomi Networks Labs details two Golang DDoS botnet families caught via honeypots this spring:
  Apex2 (Telnet brute-force, Linux+Windows builds, a Cloudflare-bypass HTTP flood plus UDP/TLS
  floods) and c2c/meow (SSH-delivered, escalates via passwordless sudo, persists as a fake
  systemd 'cpufreqd' service). Neither is sophisticated, but the point for defenders is the pace:
  exposed Telnet/SSH management interfaces on IoT and embedded-Linux keep getting repurposed for
  DDoS faster than before — directly relevant to OT-adjacent estates in energy, water and transport.
discovered_at: "2026-07-09T12:33:00Z"
event_date: "2026-07-06"
run_id: 2026-07-09T1211Z-intel
priority: notable
immediate_action: null
tags: [botnet, ddos, ot-ics]
regions: [global]
sectors: [energy, water, transport, telco, public-sector]
entities: [tool:apex2-botnet, tool:c2c-meow-flooder]
cves: []
sources:
  - url: "https://www.nozominetworks.com/blog/spring-botnet-floods-golang-malware-targets-exposed-iot-systems"
    publisher: "Nozomi Networks Labs"
    date: "2026-07-06"
    role: primary
  - url: "https://industrialcyber.co/ransomware/nozomi-identifies-apex2-and-c2c-golang-malware-driving-faster-iot-botnet-attacks-raising-risks-for-ot-environments/"
    publisher: "Industrial Cyber"
    date: "2026-07-09"
    role: corroborating
closed_sources: []
evidence:
  - quote: "It checks whether passwordless sudo is available by running sudo -n true and evaluating the return value. If successful, it relaunches itself with increased privileges, copies to /usr/local/bin/cpufreqd, and creates a fake systemd service named \"CPU Frequency Daemon\""
    publisher: "Nozomi Networks Labs"
  - quote: "In both cases, the emphasis is not on sophistication, but on speed, reuse and scalability."
    publisher: "Nozomi Networks Labs"
verification: single-source
sourcing_note: "Single-source: Nozomi Networks Labs original honeypot research (reliable lab, reliability B). The Industrial Cyber item and an Italian-language pickup are re-reports of the same Nozomi post, not independent corroboration, so credibility is rated 2. Nozomi's post is dated 2026-07-06 (within the run's 72h developing-window allowance); it surfaced into this window via the rotation-priority source Industrial Cyber on 2026-07-09."
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Remove Telnet and SSH management-interface exposure from internet-facing IoT and embedded-Linux devices (the initial-access vector for both families) and eliminate default/weak credentials — both botnets rely entirely on credential brute-force, not exploitation."
  - "Hunt for the c2c/meow persistence and escalation markers: systemd unit files created outside package-manager/config-management workflows (auditd on unit-file writes), a binary at /usr/local/bin/cpufreqd or a 'CPU Frequency Daemon' unit, and processes probing passwordless sudo via 'sudo -n true'."
  - "Alert on outbound plaintext-TCP-carrying-JSON to non-standard ports (the C2 channel) and segment OT-adjacent Linux systems from business-critical networks with restricted outbound connectivity to limit both C2 reach and DDoS participation."
migrated_from: null
---

Nozomi Networks Labs' AI-assisted honeypot triage flagged two Golang-based DDoS botnet samples this spring that stand out from the routine volume of Mirai-derived variants: Apex2 and c2c (distributed under the filename "meow") ([Nozomi Networks Labs, 2026-07-06](https://www.nozominetworks.com/blog/spring-botnet-floods-golang-malware-targets-exposed-iot-systems)). Apex2 is a direct structural evolution of the earlier Apex botnet: infection begins with Telnet connections and credential brute-forcing, followed by download-and-execute of the Golang payload, which registers with its C2 over a plaintext protocol (host OS/architecture) and ships builds for Linux (arm, arm64, mipsle, ppc64) and Windows (386, amd64). Its named flood commands include `cf` (an HTTP(S) flood specifically tuned to bypass Cloudflare via randomized User-Agent lists and long keep-alive timeouts), `udp`/`pps`, `discord`/`game` UDP floods, and three TLS-flood variants (`tls`, `tlsplus`, `tlsplusbypass`). c2c/meow is architecturally simpler — a Golang flooder with no built-in propagation (a separate SSH scanner handles brute-forcing and delivery) that authenticates to a hardcoded C2 over plaintext JSON-over-TCP, checks for passwordless sudo (`sudo -n true`) to self-escalate, then persists by copying itself to `/usr/local/bin/cpufreqd` and registering a fake systemd unit masquerading as a "CPU Frequency Daemon" — supporting ten flood-module types (icmp, dnsudp, udp, http, directhttp, fasthttp, betterhttp, tcp, tcphandshake, dnstcp).

Nozomi's stated point for defenders is that neither family is sophisticated — both lean on commodity Golang tooling, weak/default credentials and exposed Telnet/SSH interfaces rather than novel exploitation — and that the lack of sophistication does not reduce the risk at scale, because the build-and-deploy cycle for such botnets is getting faster. ATT&CK mapping: `T1110 Brute Force` (Telnet/SSH), `T1105 Ingress Tool Transfer`, `T1548.003 Abuse Elevation Control Mechanism: Sudo` (c2c's passwordless-sudo self-escalation), `T1543.002 Create or Modify System Process: Systemd Service` with `T1036.005 Masquerading` (the fake cpufreqd unit), and `T1498 Network Denial of Service` for the flood modules. **Defender takeaway:** this is not a novel threat but a concrete hunt package for the OT-adjacent and embedded-Linux estates in the constituency's energy, water and transport remit — the fake-systemd-service naming, the `sudo -n true` escalation probe, and plaintext-JSON C2 are all cheap, durable detections, and the durable fix is the unglamorous one of removing internet-exposed Telnet/SSH and default credentials on IoT and embedded devices.
