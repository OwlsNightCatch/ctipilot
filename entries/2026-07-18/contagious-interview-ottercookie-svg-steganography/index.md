---
schema: 1
kind: research
title: "Contagious Interview (DPRK) hides an OTTERCOOKIE-aligned payload in SVG-comment steganography inside fake coding-interview repos"
headline: "Elastic finds a new Contagious Interview chain that splits its payload across Base64 comments in every SVG flag image and reassembles it via eval()"
summary: >
  Elastic Security Labs documented (2026-07-18) a new instance of the DPRK-aligned Contagious Interview
  campaign (tracked REF9403) after the operators targeted Elastic's own community Slack with a fake job
  posting and take-home coding project. The trojanized Next.js repo hides its payload as Base64
  fragments inside HTML comments across every SVG flag image in an assets directory; a loader script
  reassembles them alphabetically and runs them with eval(), deliberately evading scanners that do not
  parse SVG comment bodies. On project startup it runs a four-stage OTTERCOOKIE-aligned payload —
  browser/wallet credential theft, sensitive-file exfiltration, a Socket.IO RAT and a clipboard stealer
  — with zero AV detection at publication. Relevant to any team that runs candidate or contractor
  take-home coding tests.
discovered_at: "2026-07-18T04:35:00Z"
event_date: "2026-07-18"
run_id: 2026-07-18T0409Z-intel
priority: notable
immediate_action: null
tags: [nation-state, infostealer, supply-chain, north-korea-nexus]
regions: [global]
sectors: [technology, public-sector]
entities: ["campaign:contagious-interview", "tool:ottercookie"]
techniques: [T1204.002, T1027.003, T1555.003, T1552.001, T1083, T1071.001, T1115]
affected_products: []
cves: []
sources:
  - url: "https://www.elastic.co/security-labs/contagious-interview-malware-svg-steganography"
    publisher: "Elastic Security Labs"
    date: "2026-07-18"
    role: primary
closed_sources: []
evidence:
  - quote: "The payloads are split into Base64 fragments inside HTML comments across every SVG flag image inside an assets directory."
    publisher: "Elastic Security Labs"
  - quote: "These trojanized repositories at the time of writing have zero detections and are not flagged by any AV vendors"
    publisher: "Elastic Security Labs"
verification: single-source
sourcing_note: "Single-source (Elastic Security Labs), rated as such — but carried at confidence medium because Elastic reports first-hand incident visibility (its own community Slack was targeted) and the Contagious Interview / DeceptiveDevelopment campaign lineage is independently established by other labs (NTT Security, Microsoft). The specific SVG-comment-steganography variant is, per Elastic, not previously documented."
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

Elastic Security Labs disclosed a new instance of the long-running DPRK-aligned **Contagious Interview** campaign (internally tracked REF9403) after the operators targeted Elastic's own community Slack workspace with a fake job posting and a "coding challenge" project ([Elastic Security Labs, 2026-07-18](https://www.elastic.co/security-labs/contagious-interview-malware-svg-steganography)). The lure is a fully functional take-home project — a Next.js e-commerce template copied from a real open-source repository — that a candidate is asked to run. The novelty is where the payload hides: it is "split into Base64 fragments inside HTML comments across every SVG flag image inside an assets directory" ([Elastic Security Labs, 2026-07-18](https://www.elastic.co/security-labs/contagious-interview-malware-svg-steganography)). The files look like ordinary country-flag images; a JavaScript loader in the repo reassembles the comment fragments from every flag in alphabetical order, decodes them with a custom Base64 routine, and runs the result with `eval()` — deliberately avoiding `atob()` and `Buffer.from` so simple content scanners do not flag the decode. Because the project's `package.json` wires the loader into the server entry point, the payload runs on every `npm run dev` / `npm start`, and the trojanized repositories "have zero detections and are not flagged by any AV vendors" ([Elastic Security Labs, 2026-07-18](https://www.elastic.co/security-labs/contagious-interview-malware-svg-steganography)).

The payload is a four-stage chain Elastic assesses as aligned with **OTTERCOOKIE** (first documented by NTT Security in December 2024, overlapping the BEAVERTAIL lineage). Stage one enumerates browser profiles across Windows, macOS and Linux and steals saved credentials, autofill data and cryptocurrency-wallet-extension stores, masquerading its process as a benign `npm-cache` process. Stage two recursively discovers and exfiltrates sensitive files — environment files, private keys, keychains, shell histories, documents and source code. Stage three opens a persistent Socket.IO command-and-control channel giving the operator interactive shell execution, with sandbox/VM detection used to tag rather than halt on analysis machines. Stage four (Windows) drops further second-stage binaries disguised as text files and adds a clipboard stealer polling every 500 ms.

**Defender takeaway:** a single compromised developer is a viable supply-chain initial-access path, and the delivery here is a legitimate-looking runnable project rather than an obviously malicious file. Detection concept, telemetry-class first: process-creation telemetry showing `node`/`npm` spawning credential-store access or outbound network connections shortly after a project is installed and run; outbound WebSocket/Socket.IO connections from a developer workstation to non-corporate destinations; and script-content inspection for `eval()` fed by data decoded from SVG or image-comment bodies. **Triage:** legitimate take-home assessments routinely ship real runnable e-commerce/Next.js scaffolds with image assets — the discriminator is not the presence of SVGs or a Next.js project but Base64/steganographic content inside SVG comment nodes plus a loader that `eval()`s reassembled fragments on server start. Hardening: run candidate and contractor take-home projects only in disposable, network-isolated sandboxes, never on a developer's daily-driver or domain-joined workstation.
