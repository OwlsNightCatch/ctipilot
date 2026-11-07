---
schema: 1
kind: research
title: "msaRAT: Chaos ransomware's Rust RAT builds C2 through the Chrome DevTools Protocol so the malware process never opens a socket"
headline: "Talos dissects a RAT that offloads all C2 into a headless browser via CDP and WebRTC — process-to-socket attribution sees only Chrome"
summary: >
  Cisco Talos documented msaRAT, a Rust remote-access trojan used by the Chaos ransomware group whose defining
  trait is that the malware process itself never connects to the network — it drives a headless Chrome/Edge
  instance over the Chrome DevTools Protocol and tunnels C2 over a WebRTC DataChannel relayed through Cloudflare
  Workers and a Twilio TURN server. Endpoint tooling keyed on which process opened a socket sees only the browser.
discovered_at: "2026-07-24T04:36:09Z"
event_date: "2026-07-23"
run_id: 2026-07-24T0409Z-intel
priority: notable
immediate_action: null
tags: [ransomware, infostealer, cloud]
regions: [global]
sectors: [technology]
entities: [actor:chaos-ransomware, malware:msarat]
techniques: [T1071.001, T1059.007, T1090.002, T1573.001]
affected_products: []
cves: []
sources:
  - url: "https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/"
    publisher: "Cisco Talos"
    date: "2026-07-23"
    role: primary
closed_sources: []
evidence:
  - quote: "msaRAT never touches the network directly — it controls its C2 communication channel exclusively through Chrome DevTools Protocol (CDP), a browser debugging API."
    publisher: "Cisco Talos"
  - quote: "The binary contains a Cloudflare Workers endpoint, but it never makes HTTP connections to that domain itself; it offloads that work entirely to the browser."
    publisher: "Cisco Talos"
verification: single-source
sourcing_note: "Single substantive primary technical analysis from Cisco Talos (high-reliability research lab); no independent second lab report located in-window. Included on detection value, with the single-source status recorded."
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
actions: []
migrated_from: null
---

Cisco Talos documented **msaRAT**, a Rust-based remote-access trojan deployed by the **Chaos** ransomware-as-a-service group, whose architecture is built to defeat the "which process opened this socket" heuristic that endpoint tooling relies on ([Cisco Talos, 2026-07-23](https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/)). The RAT process itself opens no external network connection. Instead it launches and controls a headless Chrome/Edge instance through the **Chrome DevTools Protocol (CDP)**, a legitimate browser-debugging API: it connects to the browser's local CDP WebSocket (127.0.0.1 only), registers CDP bindings, and uses `Runtime.evaluate` to inject JavaScript that fetches STUN/TURN configuration from a Cloudflare Workers endpoint, negotiates a WebRTC PeerConnection/DataChannel (ICE plus SDP offer/answer over HTTP POST to the same Workers endpoint), and routes all subsequent C2 commands over that DataChannel through a Twilio TURN relay, double-encrypted with DTLS plus ChaCha20-Poly1305 ([Cisco Talos, 2026-07-23](https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/)). Because every externally-visible connection originates from the signed browser binary rather than the malware, network- and process-attribution telemetry shows only ordinary Chrome/Edge traffic to Cloudflare and Twilio infrastructure that most estates already allow.

**Defender takeaway:** This is a concrete, reproducible evasion pattern detection engineers can hunt for now, independent of the specific sample. The load-bearing observable is a headless-browser launch driven by a non-browser process: in process-creation telemetry with parent lineage (Sysmon EID 1, EDR process events), surface Chrome/Edge processes started with `--remote-debugging-port` (or equivalent CDP flags) whose parent is not a browser-management or user-launch context, and correlate with a local loopback WebSocket connection to that debugging port originating from an unrelated binary. **Triage:** developers and automated test harnesses legitimately drive headless Chrome over CDP, so the flag and the loopback socket alone are noisy — the discriminators are a CDP-controlled browser parented to an unexpected process (not a CI runner, IDE or test framework), on a host with no development role, immediately followed by outbound WebRTC/STUN negotiation to Cloudflare Workers and TURN infrastructure. Talos ships ClamAV and Snort coverage for the known sample, but the behavioural hunt is what survives repacking.
