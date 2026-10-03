---
schema: 1
kind: threat
title: "An attacker achieves domain-wide ransomware impact on every Windows workstation with zero encryption binary and zero endpoint persistence, entirely through a malicious Group Policy Object named \"PAYLOAD\" linked at the domain root, while a separate PAYLOAD binary hits ESXi/Linux servers and exfiltrated data surfaces on the dark web"
headline: "Kaspersky GERT: a Group Policy Object was the whole ransomware on Windows, and it left nothing for an EDR to alert on until the wallpaper changed"
summary: >
  Kaspersky's Global Emergency Response Team reconstructs an April 2026 incident at a Middle East
  manufacturing organization in which an attacker with GPO-write privileges authored a Group Policy Object
  that dropped ransom notes, disabled the local Administrator account and replaced the lock-screen wallpaper
  domain-wide across every Windows workstation, plus a second, independently deployed Group Policy Object
  that disabled Windows Firewall, using only native Group
  Policy client-side extensions: no ransomware binary, no file encryption and no endpoint persistence on
  any Windows system. Separately, the same incident deployed an actual PAYLOAD ransomware binary against
  the organization's ESXi/Linux servers, and data exfiltrated from file servers was later published on the
  dark web.
discovered_at: "2026-09-29T05:00:00Z"
updated_at: null
event_date: "2026-04-14"
run_id: 2026-09-29T0405Z-intel
priority: high
immediate_action: null
tags: [ransomware, identity]
regions: [middle-east, global]
sectors: [manufacturing]
entities: []
techniques: [T1078, T1133, T1484.001, T1686, T1531, T1491.001, T1005, T1657]
affected_products: ["Microsoft Active Directory Group Policy", "Fortinet FortiGate SSL VPN", "VMware ESXi"]
cves: []
sources:
  - url: "https://securelist.com/tr/payload-ransomware-via-group-policy/121335/"
    publisher: "Kaspersky Securelist (Kaspersky GERT)"
    date: "2026-09-21"
    role: primary
closed_sources: []
evidence:
  - quote: "an encryptionless, binary-less operation that abused Active Directory mechanisms for managing Group Policy Objects"
    publisher: "Kaspersky Securelist (Kaspersky GERT)"
    source_url: "https://securelist.com/tr/payload-ransomware-via-group-policy/121335/"
  - quote: "The only ransomware we found in this incident was PAYLOAD sample targeting ESXi on Linux servers. Besides that, data exfiltration was observed originating from the file servers and several additional systems, and was later published on the dark web."
    publisher: "Kaspersky Securelist (Kaspersky GERT)"
    source_url: "https://securelist.com/tr/payload-ransomware-via-group-policy/121335/"
  - quote: "we assess with moderate confidence that the missing encryption reflects one of two scenarios: (1) a deliberate decision to stay below the irreversible data destruction threshold while preserving the option of a follow-on encryption phase, or (2) an operation interrupted before full execution"
    publisher: "Kaspersky Securelist (Kaspersky GERT)"
    source_url: "https://securelist.com/tr/payload-ransomware-via-group-policy/121335/"
verification: single-source
sourcing_note: >
  Single-sourced to Kaspersky GERT's own incident-response engagement (Admiralty B, original first-hand IR
  reporting); no independent second source exists for this specific incident. This actor/technique is
  unrelated to the pre-existing registry entity actor:payload-ransomware (the Zurich-area data-centre
  leak-site extortion group first tracked 2026-08-20): the name "PAYLOAD" here is Kaspersky's label for the
  malicious Group Policy Object itself, not a claimed actor brand, and no entity key is registered for it to
  avoid conflating two unrelated intrusions that happen to share a name.
confidence: high
references: []
deep_dive: true
deep_dive_category: ransomware-affiliate
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Audit domain-root and OU-linked GPOs for unexpected Files, Registry or Security Settings client-side-extension entries (ransom-note file drops, legal-notice banner rewrites, local Administrator account disablement, Windows Firewall disablement): this technique's entire attack is visible in GPO content and GPO-creation events, not in endpoint telemetry."
updates: []
migrated_from: null
---

Kaspersky's Global Emergency Response Team (GERT) reconstructs an April 2026 incident at a Middle East manufacturing organization in which an attacker authenticated to a FortiGate SSL VPN using a compromised credential of unconfirmed provenance, obtained Group-Policy-write privileges via an unconfirmed escalation path, and authored a malicious Group Policy Object named "PAYLOAD" linked at the domain root ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)). On every Windows workstation, the GPO used only native client-side extensions (CSEs) to achieve the operation's whole visible impact, with no encryptor of any kind: the Files CSE dropped a read-only ransom note to every desktop and drive root; the Registry CSE rewrote the Windows logon legal-notice banner to ransom text; the Personalization/Desktop policy set a SYSVOL-hosted ransom image as every machine's lock screen and wallpaper; and Security Settings CSE (`GptTmpl.inf`) disabled the local Administrator account fleet-wide, alongside a second GPO disabling Windows Firewall domain-wide.

Because computer-configuration GPO settings apply only on reboot or a policy refresh cycle, the malicious policy sat cached and dormant for a full day between authoring (13 April) and mass visible impact (14 April); during that window, data exfiltration from file servers and several additional systems proceeded unnoticed. On the Windows domain-joined estate specifically, Kaspersky's forensic reconstruction found no files encrypted, no ransomware binary resident on disk, and no endpoint persistence mechanism of any kind: a detection program keyed on ransomware executables, encryption behavior, or process-level anomalies would have produced zero alerts until the ransom wallpaper appeared, post-reboot, on every affected desktop simultaneously. Kaspersky is explicit that this no-binary finding is scoped to that Windows activity: "The only ransomware we found in this incident was PAYLOAD sample targeting ESXi on Linux servers" ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)): a genuine ransomware binary was deployed, but against the organization's ESXi/Linux servers, a separate track from the GPO-only attack on Windows. The exfiltrated data was later published on the dark web, per Kaspersky's own account, confirming the extortion followed through beyond the operational-disruption phase. Kaspersky does not treat the absence of Windows-side encryption as settled: it assesses "with moderate confidence that the missing encryption reflects one of two scenarios: (1) a deliberate decision to stay below the irreversible data destruction threshold while preserving the option of a follow-on encryption phase, or (2) an operation interrupted before full execution" ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)).

**Triage:** for the Windows-side GPO attack, the discriminator is not endpoint behavior but Group Policy content and change history, since no encryption or binary execution occurs on those hosts. A domain-root or high-scope GPO created or modified outside a change-managed window, especially one touching the Files, Registry, Security Settings or Personalization CSEs simultaneously, is the signal; ordinary administrative GPO changes rarely touch all four categories in a single object, and a GPO disabling the local Administrator account or Windows Firewall domain-wide has essentially no benign justification. On ESXi/Linux hosts, the discriminator is the ordinary one for ransomware: an actual PAYLOAD binary execution.

**Defender takeaway:** review GPO-write/modify permissions at the domain root and any OU covering a meaningful share of the estate, since the Windows-side technique requires only that access, not code execution rights on any endpoint; enable auditing on GPO creation and linking events (Group Policy Management Console / SYSVOL change auditing) as a primary detection surface, because this class of attack is invisible to EDR and file-integrity tooling by construction on Windows. The GPO technique is domain/Active-Directory-architecture-generic and directly transferable to any Windows AD environment, including a government AD estate managing distributed desktop fleets through central Group Policy; ESXi/Linux hosts in the same estate still need standard ransomware-binary detection and exfiltration monitoring, since the GPO-only technique does not extend to them.
