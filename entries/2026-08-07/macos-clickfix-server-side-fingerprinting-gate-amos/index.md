---
schema: 1
kind: threat
title: "The macOS ClickFix chain now qualifies visitors server-side before showing the lure, with anti-analysis probes that detect a console rather than a sandbox"
headline: "Microsoft documents the cloaking layer in front of a ClickFix campaign — researchers and scanners get a decoy, qualified Macs get the payload"
summary: >
  Microsoft Threat Intelligence documents an evolution of the macOS ClickFix campaign delivering the MacSync and Atomic Stealer (AMOS) infostealers:
  the actor now fronts the lure with a server-side visitor-qualification gate across hundreds of algorithmically
  named domains. The gate submits browser, hardware and runtime attributes to the server for a decision, including
  a WebGL GPU query and anti-analysis probes — among them a counter incremented by a function's own toString()
  call, which detects a developer console or a log-capturing tool rather than a virtual machine. Visitors that
  pass get a counterfeit "Download for macOS" page with an obfuscated curl one-liner; everyone else gets a decoy.
discovered_at: "2026-08-07T04:41:00Z"
event_date: "2026-08-05"
run_id: 2026-08-07T0411Z-intel
priority: notable
immediate_action: null
tags: [infostealer, phishing]
regions: [global]
sectors: [public-sector, technology, finance]
entities: ["campaign:clickfix-macos-2026"]
techniques: [T1204.004, T1189, T1608.004, T1497.001, T1027, T1105, T1059.004, T1555.003, T1552.001]
affected_products: ["Apple macOS"]
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-08-05"
    role: primary
closed_sources: []
evidence:
  - quote: "Rather than immediately presenting a malicious command, the actor performs server-side victim qualification before revealing the lure, reducing visibility to researchers and automated security systems while maintaining access to intended macOS targets."
    publisher: "Microsoft Threat Intelligence"
  - quote: "The gate profiles each visitor using a combination of browser, hardware, and runtime attributes, which are submitted to the server for evaluation."
    publisher: "Microsoft Threat Intelligence"
  - quote: "The script creates a temporary function whose toString() method increases a counter, then writes that function to the console."
    publisher: "Microsoft Threat Intelligence"
  - quote: "On macOS 26.4 and later, Apple introduced a mitigation that displays a warning when a user attempts to paste a potentially malicious command into Terminal, directly addressing the ClickFix delivery mechanism."
    publisher: "Microsoft Threat Intelligence"
  - quote: "Where feasible, alert the file<word><word> domain pattern rather than maintaining a list of individual domains."
    publisher: "Microsoft Threat Intelligence"
verification: single-source
sourcing_note: >
  Single-source: Microsoft Threat Intelligence's own analysis of the campaign, which it has tracked previously.
  No second party has independently assessed this evolution, so credibility is 2 rather than 1. The payload
  families (MacSync and Atomic Stealer / AMOS) and the ClickFix delivery pattern are already-established
  elements Microsoft attributes to the same tracked activity; the new element carried here is the
  qualification gate, together with the macOS 26.4+ paste mitigation Microsoft names as the platform control.
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
actions:
  - "Roll macOS endpoints to 26.4 or later where the estate allows it: that release adds a native warning when a user pastes a potentially malicious command into Terminal, which is the delivery step this campaign depends on and the only control that engages before execution."
  - "Add a detection on the `file<word><word>` domain-generation pattern in DNS and proxy telemetry rather than a blocklist of the individual hostnames — Microsoft names this as the pivot to hunt and counted more than 250 front-end domains in one tracking window."
migrated_from: null
---

The interesting part of this campaign is no longer the lure but the doorway in front of it. Microsoft Threat Intelligence reports that the macOS ClickFix activity it has been tracking now performs visitor qualification on the server before it will show anything malicious: "Rather than immediately presenting a malicious command, the actor performs server-side victim qualification before revealing the lure, reducing visibility to researchers and automated security systems while maintaining access to intended macOS targets" ([Microsoft Threat Intelligence, 2026-08-05](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/)). The gate is hosted across a large set of algorithmically generated domains — Microsoft "confirmed more than 250 ClickFix front-end domains during the tracking window, and many followed a repeated naming pattern using the token “file” with dictionary-style words", i.e. a `file<word><word>` construction — and the decision is not made in the browser where an analyst could read it — "the gate profiles each visitor using a combination of browser, hardware, and runtime attributes, which are submitted to the server for evaluation" ([Microsoft Threat Intelligence, 2026-08-05](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/)). A visitor that fails qualification receives a decoy page or nothing at all, which is why a scanner's verdict on one of these URLs is close to worthless.

The profiling itself is broader than the usual sandbox checks. Microsoft describes collection across the browser's `navigator`, `screen`, `window`, `document`, `location` and `console` objects, a WebGL query for genuine graphics hardware, and environmental signals including timezone, iframe presence and touch-input support. Two probes stand out because they target the analyst rather than the machine. The first is a counter driven by JavaScript's own string coercion: "the script creates a temporary function whose toString() method increases a counter, then writes that function to the console" ([Microsoft Threat Intelligence, 2026-08-05](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/)). In a normal browser that counter usually stays put, because nothing serialises the function; if the developer console is open, or a headless or log-capturing tool serialises console output, the function gets converted to a string and the counter moves. The check does not ask "am I in a VM?" — it asks "is somebody reading this page's console?", which a well-built analysis harness answers in the affirmative precisely because it is instrumented. The second is prototype-tampering detection, which catches the hooking that instrumentation frameworks rely on.

A qualified visitor is served a counterfeit page presenting a "Verified Publisher" framing and a `Download for macOS` action carrying an obfuscated `curl` one-liner, in the ClickFix pattern of getting the user to paste and run a command themselves. That command retrieves a staged script from a structured path on the operator's infrastructure, and the chain ends in an infostealer — Microsoft names MacSync and Atomic Stealer (AMOS) as the families delivered — collecting credentials, browser data and cryptocurrency-wallet contents ([Microsoft Threat Intelligence, 2026-08-05](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/)).

**Defender takeaway:** treat a clean verdict on one of these URLs as no evidence at all, and move detection to the endpoint, where the gate has no vote. The user still has to paste a command into a terminal, and that action is what leaves a durable trace. Detection concepts, telemetry class first: in process-creation telemetry with parent lineage, a terminal process spawning a network-fetch utility that pipes its output into an interpreter, shortly after browser activity, is the sequence to alert on regardless of which domain served it; in egress and proxy telemetry, a fetch from a very recently registered host immediately following a user-initiated browser session is the corroborating signal Microsoft points to. There is also one network-side pivot that survives the cloaking, and it is a generation rule rather than a blocklist: Microsoft's own guidance is to "hunt the generation pattern" and, "where feasible, alert the `file<word><word>` domain pattern rather than maintaining a list of individual domains" ([Microsoft Threat Intelligence, 2026-08-05](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/)) — which is durable in a way that the individual hostnames, rotated constantly, are not. Hardening has to target the paste, not the download, because the download protections never engage: Microsoft's point is that "because execution starts from a user-run Terminal command rather than a downloaded app bundle, the flow can avoid parts of the normal macOS application trust path, including quarantine handling, code-signing evaluation, and notarization checks typically applied to downloaded applications" ([Microsoft Threat Intelligence, 2026-08-05](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/)). The platform lever that does apply is recent: "on macOS 26.4 and later, Apple introduced a mitigation that displays a warning when a user attempts to paste a potentially malicious command into Terminal, directly addressing the ClickFix delivery mechanism" ([Microsoft Threat Intelligence, 2026-08-05](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/)), so estate-wide upgrade to 26.4 or later is the one control that breaks this pattern at the delivery step. **Triage:** developers legitimately fetch install scripts with `curl` and pipe them to a shell, so the command shape alone is not the signal; the discriminators are the age and reputation of the host being fetched, the absence of the long-lived vendor domain a real install script would use, and the preceding browser navigation that supplied the command — a paste-and-run whose source was a page the user reached from an advertisement or search result, rather than a repository README they were already working in.
