---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "The week's tradecraft converged on abusing trusted primitives — OAuth tokens, signed binaries, native auth APIs and legitimate SaaS"
headline: "This week's tradecraft: abusing trusted primitives — OAuth tokens, signed binaries, native APIs, legit SaaS"
summary: "Five independent research disclosures this week share a through-line: attackers are increasingly operating through trusted, native mechanisms rather than custom-malware signatures — ToddyCat's Umbrij steals OAuth tokens via Chromium remote-debugging; Talos's ARToken automates M365 device-code phishing and Primary-Refresh-Token persistence; Blackpoint's Avalon chains a signed MSBuild loader with ETW/AMSI patching; Jamf's PamStealer validates stolen macOS passwords through pam_authenticate; and Mustang Panda uses Zoho WorkDrive as a dead-drop C2. Signature-based detection degrades against all of them; the hunt surface is anomalous use of the trusted mechanism."
discovered_at: "2026-07-05T23:34:00Z"
event_date: 2026-07-02
run_id: 2026-07-05T2305Z-weekly
priority: notable
immediate_action: null
tags:
  - identity
  - espionage
  - infostealer
  - phishing
regions:
  - global
sectors:
  - public-sector
  - technology
  - finance
entities:
  - "tool:toddycat-umbrij-oauth-token-theft-strd"
  - "tool:talos-artoken-eviltokens-bec-panel"
  - "tool:avalon-malware-framework"
  - "tool:pamstealer"
  - "campaign:mustang-panda-zohomurk-zoho-workdrive-deaddrop-c2"
cves: []
sources:
  - url: "https://securelist.com/toddycat-apt-umbrij-tool-and-oauth/120251/"
    publisher: Kaspersky Securelist (GReAT)
    role: primary
  - url: "https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/"
    publisher: Cisco Talos
    role: primary
  - url: "https://blackpointcyber.com/blog/avalons-path-from-legal-lure-to-crownx-ransom-capabilities/"
    publisher: Blackpoint Cyber
    role: primary
  - url: "https://www.jamf.com/blog/pamstealer-macos-infostealer-applescript-rust/"
    publisher: Jamf Threat Labs
    role: primary
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "Each tool/technique is primary single-vendor research (Kaspersky, Talos, Blackpoint, Jamf, Acronis); the convergence on abusing trusted primitives is the cross-vendor pattern that clears the weekly bar. Individual capability claims are cited to their originating lab."
confidence: high
classification:
  reliability: B
  credibility: 2
update_of: null
references:
  - "2026-07-01/kaspersky-great-toddycat-s-umbrij-automates-gmail-workspace"
  - "2026-07-02/cisco-talos-artoken-exposes-a-full-bec-as-a-service-toolkit"
  - "2026-07-04/avalon-framework-msbuild-etw-loader-crownx-ransomware"
  - "2026-07-04/pamstealer-macos-infostealer-pam-api-password-validation"
  - "2026-06-30/mustang-panda-abuses-zoho-workdrive-as-a-dead-drop-c2-channe"
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "Prioritise token-theft detections: alert on Chromium launched with remote-debugging flags by non-developer processes (Umbrij STRD), and monitor for OAuth/Primary-Refresh-Token issuance and reuse that survives password resets (ARToken device-code phishing) — password rotation alone does not evict a stolen PRT."
  - "Hunt signed-binary abuse and telemetry tampering: MSBuild and other signed LOLBins loading unexpected payloads, plus ETW/AMSI patching (in-process tampering) as a standalone high-value signal (Avalon)."
  - "For macOS fleets, alert on non-Apple processes calling pam_authenticate to validate a captured password, and on clipboard-manager impersonation (PamStealer mimicking Maccy); for network egress, treat unexpected outbound to legitimate SaaS storage (Zoho WorkDrive) from server workloads as possible dead-drop C2 (Mustang Panda)."
---

Five otherwise-unrelated research disclosures this week point the same direction: capable actors — from a Chinese APT to commodity BEC and ransomware crews — are increasingly operating *through* trusted, native mechanisms rather than dropping signatureable custom malware. For a detection-engineering audience, that is the strategic note, because it tells you where the hunt surface is moving.

**OAuth tokens as the target.** Kaspersky GReAT documented **Umbrij**, a .NET tool the ToddyCat APT uses to automate theft of Google Workspace OAuth tokens via a technique GReAT calls Shadow Token via Remote Debug (STRD) — driving Chromium's remote-debugging interface to lift live tokens ([Kaspersky Securelist, 2026-06-30](https://securelist.com/toddycat-apt-umbrij-tool-and-oauth/120251/)). Cisco Talos exposed **ARToken**, an EvilTokens-lineage BEC-as-a-service panel (80+ API endpoints) automating Microsoft 365 device-code phishing, Primary-Refresh-Token persistence that survives password resets, and mailbox/SharePoint exfiltration ([Cisco Talos](https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/)). Both defeat password-centric defences: the credential is no longer the secret worth stealing, the token is.

**Signed binaries and native APIs as the execution and validation layer.** Blackpoint's **Avalon** framework chains a signed-binary MSBuild loader with ETW/AMSI patching (in-process telemetry tampering) and the CrownX ransomware payload ([Blackpoint Cyber](https://blackpointcyber.com/blog/avalons-path-from-legal-lure-to-crownx-ransom-capabilities/)); Jamf's **PamStealer** impersonates the Maccy clipboard app and confirms a stolen macOS password through the native `pam_authenticate` API before exfiltrating it ([Jamf Threat Labs](https://www.jamf.com/blog/pamstealer-macos-infostealer-applescript-rust/)) — using the OS's own auth path to guarantee the loot is valid.

**Legitimate SaaS as C2.** Mustang Panda (TA416 / HIVE0154) used **Zoho WorkDrive** as a dead-drop C2 channel (ZOHOMURK) against government and energy targets ([Acronis TRU, 2026-06-29](https://www.acronis.com/en/tru/posts/mustang-panda-targets-indias-government-and-energy-sectors/)) — command traffic riding a trusted, hard-to-block SaaS host.

**Weekly takeaway:** the common defensive failure mode across all five is reliance on signatures and on the password as the crown jewel. The hunt has to move to *anomalous use of the trusted mechanism* — remote-debugging flags on browser processes, token issuance/reuse surviving resets, signed LOLBins loading unexpected code, ETW/AMSI tampering, native auth-API calls from non-auth processes, and server egress to consumer SaaS storage. Per-tool detail and detection concepts in § references.
