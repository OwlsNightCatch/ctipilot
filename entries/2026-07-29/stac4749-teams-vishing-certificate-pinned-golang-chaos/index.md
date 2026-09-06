---
schema: 1
kind: threat
title: "STAC4749 runs Teams helpdesk vishing from attacker-owned .top domains into certificate-pinned Golang implants and Chaos ransomware in under 17 hours"
headline: "Sophos tracks a Teams-vishing cluster that abandoned tenant spoofing for its own domains and pins its C2 to hardcoded issuer certificates"
summary: >
  Sophos X-Ops documented STAC4749 on 2026-07-28: operators open Microsoft Teams chats and calls posing
  as IT helpdesk staff, from their own IT-themed domains registered under the .top TLD rather than the
  spoofed onmicrosoft.com tenants used in earlier Teams-abuse campaigns, and talk victims into launching
  a remote-support tool — shifting from Quick Assist to the less-blocklisted RemSupp from April 2026.
  The follow-on Golang implants embed CA certificates and complete a TLS handshake only with C2 servers
  presenting a matching issuer, segmenting infrastructure by operational role; a PyArmor-obfuscated
  Python backdoor fetches its AES key from a public code-hosting repository at runtime. At least three
  compromises ended in Chaos ransomware, one within 17 hours of initial access. Observed cases were
  almost entirely Canadian and US, but nothing in the tradecraft is region-specific.
discovered_at: "2026-07-29T05:35:00Z"
event_date: "2026-07-28"
run_id: 2026-07-29T0408Z-intel
priority: high
immediate_action: null
tags: [ransomware, phishing, organized-crime, identity]
regions: [us, global]
sectors: [manufacturing, energy, legal-services, technology]
entities: [actor:stac4749, actor:chaos-ransomware]
techniques: [T1566.004, T1219, T1021.001, T1547.001, T1547.009, T1027, T1105, T1572, T1090, T1071.001, T1486]
affected_products: ["Microsoft Teams", "Microsoft Quick Assist", "RemSupp", "AnyDesk", "DWAgent"]
cves: []
sources:
  - url: "https://www.sophos.com/en-us/blog/chaos-in-teams-vishing"
    publisher: "Sophos X-Ops"
    date: "2026-07-28"
    role: primary
closed_sources: []
evidence:
  - quote: "STAC4749 operators created IT-themed cloud domains under the \".top\" top-level domain (TLD) and leveraged plausible employee usernames to make the accounts appear legitimate"
    publisher: "Sophos X-Ops"
  - quote: "Several of the Golang-based implants contained hard-coded CA certificates associated with issuer names such as loop-CA, connectify-CA, and james-bond-CA. These implants only established encrypted connections if the C2 server had the same issuer as the embedded certificate."
    publisher: "Sophos X-Ops"
  - quote: "Retrieved its AES key and initialization vector (IV) from a public GitHub repository and used the key to decrypt embedded configuration data and payload"
    publisher: "Sophos X-Ops"
  - quote: "In one incident, the time from initial access to ransomware deployment was less than 17 hours, consistent with prior Chaos ransomware cases observed by Sophos analysts."
    publisher: "Sophos X-Ops"
  - quote: "Sophos analysts have found no evidence linking STAC4749 activity to that group. Instead, limited hands-on-keyboard artifacts suggest a Russian-language connection."
    publisher: "Sophos X-Ops"
  - quote: "However, there is insufficient evidence for attribution."
    publisher: "Sophos X-Ops"
verification: single-source
sourcing_note: >
  Single-source: Sophos X-Ops' own MDR case data from February to June 2026, with no second lab reporting
  on this cluster — Sophos itself notes the custom-malware chain has not been reported elsewhere.
  Attribution is deliberately left where Sophos left it: it assesses with high confidence that STAC4749
  was financially motivated and either deployed ransomware directly or coordinated with affiliates, but
  states there is insufficient evidence for actor attribution, and explicitly reports finding no evidence
  linking STAC4749 to MuddyWater — the false-flag hypothesis being Rapid7's, about Chaos generally rather
  than about this cluster. A Cyrillic-keyboard-layout typo is the only nationality artifact Sophos
  reports and it declines to build attribution on it, so neither do we. Sophos's own statement that Chaos
  was reportedly launched by former BlackSuit/Royal members is carried as Sophos's characterisation.
  Case-share and sector percentages are Sophos MDR engagement statistics, not threat-landscape
  measurements. Attacker domains, implant hashes, C2 addresses and the repository holding the key are
  omitted as indicators; the domain and filename *patterns* are described because they are the
  detectable behaviour.
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
  - "Restrict Microsoft Teams external access to federated domains you have allow-listed, rather than permitting chats and calls from any external tenant — STAC4749's shift to its own registered .top-TLD domains means tenant-spoofing detections and onmicrosoft.com heuristics will not catch it."
  - "Add RemSupp to the remote-support tooling your application control blocks or alerts on: Sophos assesses the operators moved to it from Quick Assist specifically because it is less likely to appear on blocklists, so an estate that blocks only the well-known tools has an open path."
migrated_from: null
---

The initial access here is entirely social, and the interesting part is what the operators changed. Contact comes as a Microsoft Teams chat or call from an IT-support persona; Sophos observed call durations from 90 seconds to over 20 minutes, most lasting two to two and a half ([Sophos X-Ops, 2026-07-28](https://www.sophos.com/en-us/blog/chaos-in-teams-vishing)). Earlier Teams-abuse campaigns spoofed `onmicrosoft.com` tenants, which gave defenders a tractable check. STAC4749 instead registers its own IT-themed domains under the `.top` TLD and populates them with plausible first-name/last-name employee accounts ([Sophos X-Ops, 2026-07-28](https://www.sophos.com/en-us/blog/chaos-in-teams-vishing)). That moves the detection question from "is this tenant genuinely Microsoft's" to "should this external domain be able to reach our users at all" — a policy question rather than a signature one. The persuasion goal is a remote-support session: Quick Assist initially, with the cloud-based RemSupp as fallback, and from April 2026 RemSupp by preference — Sophos assesses this is likely because it is less apt to appear on application blocklists ([Sophos X-Ops, 2026-07-28](https://www.sophos.com/en-us/blog/chaos-in-teams-vishing)). Lateral movement consistently began by enabling RDP on the initial host through Windows service reconfiguration via `msconfig` ([Sophos X-Ops, 2026-07-28](https://www.sophos.com/en-us/blog/chaos-in-teams-vishing)).

Two payload design choices are worth carrying into detection engineering. First, the Python backdoor — PyArmor-obfuscated, PyInstaller-packaged, able to run shell commands, collect system information and load further Python modules — retrieves its AES key and initialisation vector from a public code-hosting repository at runtime and uses them to decrypt its embedded configuration and payload ([Sophos X-Ops, 2026-07-28](https://www.sophos.com/en-us/blog/chaos-in-teams-vishing)). The key is therefore not in the sample, which defeats static key extraction and lets the operators rotate it by editing a public page. Second, the Golang implants embed CA certificates and will complete an encrypted connection only when the C2 server presents a matching issuer; Sophos found payloads sharing an issuer consistently talked to the same servers while different issuers meant separate infrastructure, and reads this as deliberate segmentation by payload or operational role ([Sophos X-Ops, 2026-07-28](https://www.sophos.com/en-us/blog/chaos-in-teams-vishing)). The practical effect is that a TLS-terminating proxy or a researcher's redirection attempt cannot complete the handshake, so interception-based analysis and sinkholing both fail unless the issuer is reproduced. Persistence evolved visibly across the campaign: HKCU Run keys masquerading as Realtek audio components from February, joined by WinAudio-themed names from mid-May, alongside `.vbs` scripts creating Startup-folder shortcuts named to look like SecurityHealth or OneDriveUpdate, sometimes with hidden attributes ([Sophos X-Ops, 2026-07-28](https://www.sophos.com/en-us/blog/chaos-in-teams-vishing)). In ransomware cases operators added DWAgent and AnyDesk for redundant access, and in one case a standalone reverse-SOCKS proxy supporting up to a thousand concurrent connections; encryption landed nearly simultaneously across endpoints, in one incident under 17 hours from initial access ([Sophos X-Ops, 2026-07-28](https://www.sophos.com/en-us/blog/chaos-in-teams-vishing)).

**Defender takeaway:** a sub-17-hour path from a Teams call to simultaneous encryption means the containment window is a single shift, and every technical control downstream of the phone call is racing. The two places to spend effort are therefore upstream and lateral: govern which external domains can initiate Teams contact at all, and treat the enabling of RDP on a workstation — particularly via service reconfiguration rather than policy — as a high-value alert rather than a hygiene finding, because in this chain it is the pivot that turns one social-engineered endpoint into an estate-wide event. Note also that the observed victim set was 94% Canadian and US and skewed to services, manufacturing, energy and construction, with every targeted legal organisation working in intellectual-property law; none of that geography is built into the tradecraft, which needs only Teams and a legitimate RMM tool.

**Triage:** the remote-support tools in this chain are genuine software that IT departments use daily, so the tool itself discriminates nothing — and neither does the fact of an inbound Teams call. The discriminator Sophos's own guidance points at is provenance and initiative: a legitimate support session is requested by the user or arranged against an existing internal ticket, whereas this pattern is an unsolicited approach from an unrecognised external domain followed immediately by pressure to launch or install a remote-access tool. Operationally that means correlating remote-support process starts against your ticketing system, and treating a first-ever external Teams contact followed within minutes by an RMM installation as the sequence to alert on.
