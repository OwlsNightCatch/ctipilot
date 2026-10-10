---
schema: 1
kind: threat
title: "A malicious Group Policy Object named PAYLOAD delivered domain-wide ransomware impact on Windows with no encryption binary and no endpoint persistence, while a separate binary hit ESXi and Linux servers"
headline: "Kaspersky GERT: a Group Policy Object was the whole ransomware on Windows, in a channel most EDR tools do not inspect"
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
priority: notable
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
  - url: "https://www.ransomware.live/group/payload"
    publisher: "Ransomware.live (Payload group profile)"
    role: corroborating
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
  Single-sourced to Kaspersky GERT's own incident-response engagement, which is original first-hand
  reporting; no independent second source exists for this specific incident. Kaspersky uses PAYLOAD
  both as the name of the malicious Group Policy Object and for the ransomware family whose
  ESXi/Linux sample it found in the same incident, and it does not name the operators.
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
  - "Audit domain-root and OU-linked GPOs for unexpected Files, Registry or Security Settings client-side-extension entries (ransom-note file drops, legal-notice banner rewrites, local Administrator account disablement, Windows Firewall disablement): the attack shows primarily in GPO content, GPO-creation events and SYSVOL, with the endpoint Group Policy log as a post-detonation signal."
updates:
  - at: "2026-09-30T07:03:25Z"
    run_id: 2026-09-30T0639Z-audit
    type: improvement
    summary: >
      The title is shortened, leaving the domain-root link, the every-workstation scope and the
      dark-web publication to the summary and main text. An unsourced claim that the incident is
      unrelated to the Payload leak-site group is removed, and the main text now notes that a group
      of that name runs a leak site and that no cited source ties it to this incident. A detection
      line gives Kaspersky's directory-service, SYSVOL and endpoint telemetry, and the triage line
      rests on Kaspersky's indicators rather than on Administrator-account or firewall settings
      alone. The priority moves from high to notable: a single-victim incident from April 2026 with
      a transferable technique but no tie to Switzerland. The headline and action no longer say the
      attack is invisible to endpoint tooling.
    fields: [title, sourcing_note, priority, body, sources, headline, actions]
migrated_from: null
---

Kaspersky's Global Emergency Response Team (GERT) reconstructs an April 2026 incident at a Middle East manufacturing organization in which an attacker authenticated to a FortiGate SSL VPN using a compromised credential of unconfirmed provenance, obtained Group-Policy-write privileges via an unconfirmed escalation path, and authored a malicious Group Policy Object named "PAYLOAD" linked at the domain root ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)). On every Windows workstation, the GPO used only native client-side extensions (CSEs) to achieve the operation's whole visible impact, with no encryptor of any kind: the Files CSE dropped a read-only ransom note to the desktop and the C: and D: drive roots; the Registry CSE rewrote the Windows logon legal-notice banner to ransom text; the Personalization/Desktop policy set a SYSVOL-hosted ransom image as every machine's lock screen and wallpaper; and Security Settings CSE (`GptTmpl.inf`) disabled the local Administrator account fleet-wide, alongside a second GPO disabling Windows Firewall domain-wide.

Because computer-configuration GPO settings apply only on reboot or a policy refresh cycle, the malicious policy sat cached and dormant for a full day between authoring (13 April) and mass visible impact (14 April); during that window, data exfiltration from file servers and several additional systems proceeded unnoticed. On the Windows domain-joined estate specifically, Kaspersky's forensic reconstruction found no files encrypted, no ransomware binary resident on disk, and no endpoint persistence mechanism of any kind: a detection program keyed on ransomware executables, encryption behavior, or process-level anomalies would have produced zero alerts until the ransom wallpaper appeared, post-reboot, on every affected desktop simultaneously. Kaspersky is explicit that this no-binary finding is scoped to that Windows activity: "The only ransomware we found in this incident was PAYLOAD sample targeting ESXi on Linux servers" ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)): a genuine ransomware binary was deployed, but against the organization's ESXi/Linux servers, a separate track from the GPO-only attack on Windows. The exfiltrated data was later published on the dark web, per Kaspersky's own account, confirming the extortion followed through beyond the operational-disruption phase. Kaspersky does not treat the absence of Windows-side encryption as settled: it assesses "with moderate confidence that the missing encryption reflects one of two scenarios: (1) a deliberate decision to stay below the irreversible data destruction threshold while preserving the option of a follow-on encryption phase, or (2) an operation interrupted before full execution" ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)).

Kaspersky refers to PAYLOAD operators but does not name them or the site where the data was published ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)). Ransomware.live profiles a ransomware group also called Payload that runs a leak site and, it says, uses Babuk-derived code against Windows and ESXi systems ([Ransomware.live](https://www.ransomware.live/group/payload)). No cited source establishes that this group is behind the incident Kaspersky describes.

**Detection:** Kaspersky's telemetry for this class starts with directory-service change auditing on every domain controller (Advanced Audit Policy, DS Access, Audit Directory Service Changes). Event 5137 flags a new `groupPolicyContainer` object, whose creator should be an authorized GPO administrator. Event 5136 flags changes to `gPLink` on the domain root or sensitive OUs and to a GPO's extension-name, file-system-path or version attributes, and event 5141 flags GPO deletions ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)). Kaspersky adds file-integrity monitoring of the SYSVOL `Policies` folder for unexpected image, text or script files, `ScheduledTasks.xml`, and modified `registry.pol` or `GptTmpl.inf` files not created by replication. A GPO whose SYSVOL content changes without a matching 5136 event can indicate direct template editing that bypasses the Group Policy Management Console, though misconfigured auditing can cause the same gap ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)). On endpoints, the Group Policy Operational log records policy application, and a sudden domain-wide change to the applied policy set is a strong post-detonation signal ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)).

**Triage:** for the Windows-side GPO attack, the discriminator is Group Policy content and change history, not endpoint behavior, since no encryption or binary execution occurs on those hosts. Kaspersky calls a `gPLink` change at the domain root by a non-standard account one of the most telling indicators of this attack class ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)). In this incident one new domain-root GPO combined ransom-note file drops, a ransom logon banner, a ransom wallpaper and lock screen and disablement of the local Administrator account, and a second domain-root GPO disabled Windows Firewall ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)). That combination, not an Administrator-account or firewall setting on its own, separates the attack from routine policy work. On ESXi/Linux hosts, the discriminator is the ordinary one for ransomware: an actual PAYLOAD binary execution.

**Defender takeaway:** review GPO-write/modify permissions at the domain root and any OU covering a meaningful share of the estate, since the Windows-side technique requires only that access, not code execution rights on any endpoint; make the directory-service and SYSVOL telemetry in the Detection line a primary detection surface, because on Windows this attack leaves no malicious binary or process for endpoint detection to find ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)). The GPO technique is domain/Active-Directory-architecture-generic and directly transferable to any Windows AD environment, including a government AD estate managing distributed desktop fleets through central Group Policy; ESXi/Linux hosts in the same estate still need standard ransomware-binary detection and exfiltration monitoring, since the GPO-only technique does not extend to them.

## Improvement — 2026-09-30T07:03:25Z

A ransomware group also called Payload runs a leak site, and Ransomware.live describes it as using Babuk-derived code against Windows and ESXi systems ([Ransomware.live](https://www.ransomware.live/group/payload)). Kaspersky does not name the operators of the incident it describes or the site where the data was published ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)), so no cited source establishes that the two are the same operation.

A GPO that disables the local Administrator account or Windows Firewall was described as having essentially no benign justification. Kaspersky documents those settings as part of this attack, not as a discriminator on their own, and names a domain-root `gPLink` change by a non-standard account as one of the most telling indicators ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)). Its detection guidance also includes SYSVOL file-integrity monitoring, so the attack is not invisible to file-integrity tooling ([Kaspersky Securelist, 2026-09-21](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/)).
