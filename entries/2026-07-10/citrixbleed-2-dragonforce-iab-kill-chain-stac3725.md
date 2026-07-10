---
schema: 1
kind: threat
horizon: operational
title: "CitrixBleed 2 (CVE-2025-5777) weaponised into a repeatable IAB kill chain ending in DragonForce ransomware (STAC3725)"
headline: "Huntress reconstructs a productised CitrixBleed 2-to-DragonForce runbook: token theft, a registry-symlink SYSTEM escalation, then ransomware"
summary: >
  Huntress reconstructed a single, mechanically identical intrusion chain across at least six unrelated organisations in H1 2026, run by an initial-access broker (tracked by Sophos as STAC3725): pre-auth session-token theft via CitrixBleed 2 (CVE-2025-5777) on internet-facing Citrix NetScaler Gateway/AAA appliances, a portable registry-symlink local-privilege-escalation tool that abuses the Group Policy engine and the AppMgmt service to reach SYSTEM, ScreenConnect/Zoho Assist persistence, and — in the most progressed case — DragonForce ransomware. Any organisation running an unpatched NetScaler Gateway must patch and terminate all live sessions, because stolen tokens survive patching.
discovered_at: "2026-07-10T04:36:19Z"
event_date: "2026-07-09"
run_id: 2026-07-10T0409Z-intel
priority: high
immediate_action: null
tags: [ransomware, vulnerabilities, actively-exploited, pre-auth, lpe, identity]
regions: [global]
sectors: [public-sector, energy, healthcare, finance, telco]
entities: [actor:dragonforce, campaign:stac3725-citrixbleed2-iab-dragonforce]
techniques: [T1190, T1550.001, T1068, T1112, T1136.001, T1098, T1219, T1003, T1570, T1486, T1070]
affected_products: ["Citrix NetScaler ADC", "Citrix NetScaler Gateway"]
cves:
  - id: CVE-2025-5777
    cvss: null
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "NetScaler ADC/Gateway configured as a Gateway (VPN/ICA-Proxy/CVPN/RDP-Proxy) or AAA virtual server"
    fixed: "per Citrix's NetScaler security bulletin for CVE-2025-5777 (specific fixed builds not restated in the sources cited here)"
sources:
  - url: "https://www.huntress.com/blog/citrixbleed-2-dragonforce-ransomware"
    publisher: "Huntress"
    date: "2026-07-09"
    role: primary
  - url: "https://www.itsecurityguru.org/2026/07/09/citrixbleed-2-exploited-in-repeatable-attack-chain-culminating-in-dragonforce-ransomware-researchers-find/"
    publisher: "IT Security Guru"
    date: "2026-07-09"
    role: corroborating
  - url: "https://www.sophos.com/en-us/blog/qemu-abused-to-evade-detection-and-enable-ransomware-delivery"
    publisher: "Sophos X-Ops"
    date: "2026-04-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "By spraying enough of those requests, an adversary can then sift through the heap fragments for valid session tokens of someone who is currently logged in."
    publisher: "Huntress"
  - quote: "The cleanup serves to evade detection: by leaving the registry indistinguishable from its pre-exploit state, the tool removes the artifacts a responder would normally key on."
    publisher: "Huntress"
  - quote: "Huntress assesses with high confidence that the activity is the work of an initial access broker (IAB) weaponising CVE-2025-5777 to gain footholds in Citrix environments before selling or handing off access, ultimately for the purpose of ransomware deployment."
    publisher: "IT Security Guru"
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: firewall-vpn-rce
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Patch every internet-facing NetScaler ADC/Gateway to the fixed build in Citrix's NetScaler security bulletin for CVE-2025-5777 now, and after patching terminate ALL active ICA/PCoIP and AAA sessions — tokens harvested via CVE-2025-5777 remain valid across the patch."
  - "Hunt NetScaler ns.log for a burst of AAA LOGIN_FAILED events carrying binary/unprintable User values from a single source IP, and for any authenticated session driven from an IP that has no preceding successful authentication."
  - "Forward NetScaler logs off-box to a SIEM before hunting — on-device ns.log rotates fast enough to lose the evidence."
  - "Alert on gpupdate followed closely by an AppMgmt (Application Management) service start and a new SYSTEM-context process, and on net user / net localgroup Administrators account creation outside change management."
  - "Inventory endpoints for unexpected ScreenConnect, Zoho Assist, Netbird or Atera installs not tied to a sanctioned RMM deployment."
migrated_from: null
---

Across the first half of 2026 the Huntress Tactical Response unit worked at least six intrusions at unrelated organisations that reproduced the same seven-step kill chain so faithfully that analysts could predict the next artefact before pulling the log — the basis for their high-confidence assessment that an initial-access broker (IAB) has productised the path from an internet-facing Citrix box to domain-wide encryption, a cluster Sophos independently tracks as STAC3725 ([Huntress, 2026-07-09](https://www.huntress.com/blog/citrixbleed-2-dragonforce-ransomware); [Sophos X-Ops, 2026-04-16](https://www.sophos.com/en-us/blog/qemu-abused-to-evade-detection-and-enable-ransomware-delivery)). Initial access is pre-auth exploitation of CitrixBleed 2 (`CVE-2025-5777`), a memory over-read in NetScaler ADC/Gateway configured as a Gateway or AAA virtual server: a POST to the login endpoint (`/p/u/doAuthentication.do` and equivalents) with the login form variable present but empty makes the appliance serialise roughly 127 bytes of adjacent process memory into the response, and sprayed at volume this yields live session tokens (`T1190`, `T1550.001`). In one reconstructed case a user authenticated normally over LDAP+MFA from a known-good IP at 13:07 UTC; twenty-one minutes later the same session was driven from the attacker's IP with no successful authentication from that IP anywhere in the logs — token replay, with MFA already satisfied and therefore irrelevant ([Huntress, 2026-07-09](https://www.huntress.com/blog/citrixbleed-2-dragonforce-ransomware)).

The privilege-escalation primitive is what makes the cluster unmistakable, because the hijacked session usually belongs to an unprivileged employee and the operator carries a portable, unsigned LPE tool (dropped to working paths such as `C:\temp` and renamed per victim — `eng.exe`, `legal.exe`, `as.exe` — often inside a password-protected archive pulled from `temp.sh`). The tool plants a `REG_LINK` `SymbolicLinkValue` under the RdpBus device-class key `{28d78fad-5a12-11d1-ae5b-0000f803a8c2}` that redirects into the Group Policy state hierarchy (`T1112`); running `gpupdate` forces the SYSTEM-context Group Policy engine to write through the planted link into a protected key, and `sc start AppMgmt` then makes the Service Control Manager relaunch the dropper as `NT AUTHORITY\SYSTEM`, which creates a backdoor administrator via `net user … /add` and `net localgroup Administrators … /add` (`T1068`, `T1136.001`, `T1098`). AppMgmt is chosen because it is always present, normally dormant, and plausibly related to policy processing. Before detonating, the tool snapshots the original key tree and restores it afterwards, leaving the registry indistinguishable from its pre-exploit state to erase the artefacts a responder would key on (`T1070`). Persistence then rides legitimate remote-management software — ScreenConnect and Zoho Assist, in one case Netbird plus Atera (`T1219`) — and in the most advanced case the operator used PsExec, Impacket and Mimikatz for lateral movement and credential access (`T1003`, `T1570`) before deploying DragonForce ransomware, contained to a single host (`T1486`). Huntress declines a firm DragonForce-affiliate-versus-IAB attribution given the tactic overlap, and ruled out an alternative NetScaler session-management race-condition flaw because the affected build and the required already-authenticated session to race against did not fit the evidence.

**Defender takeaway:** patch NetScaler to the fixed builds and, critically, terminate every live session afterwards — harvested tokens survive the patch, which is the single most common post-patch reinfection path for this bug. On the appliance, the load-bearing detection is not the paired diagnostic breadcrumbs ("Login request is not expected to be encrypted", "X509 cert not found"), which Huntress calls necessary but nowhere near sufficient, but the binary/unprintable data leaking through the ns.log AAA `LOGIN_FAILED` User field and — the cleanest signal — an authenticated session that has no corresponding successful login event. A default Citrix behaviour also fingerprints the operator: published-desktop sessions auto-create client printer mappings that embed the client workstation name (the same `WIN-` hostnames recurred case after case), correlatable by pivoting the `Microsoft-Windows-TerminalServices-LocalSessionManager/Operational` channel (source IP + session ID) against the `MetaFrameEvents` provider in the Application log (session ID + leaked client name). **Triage:** a NetScaler login flood looks like ordinary password spraying and is routinely dismissed as such — the discriminator is that the "usernames" are leaked heap memory (unprintable bytes, X.509/ASN.1 fragments, internal `Citrix-ns-orig-srcip` proxy headers), not guessed account names; and on the endpoint, a `gpupdate` → `AppMgmt` start → new-SYSTEM-process → local-admin-creation sequence within seconds is the signal, whereas legitimate Group Policy refreshes do not spawn a fresh SYSTEM binary that immediately creates an account.
