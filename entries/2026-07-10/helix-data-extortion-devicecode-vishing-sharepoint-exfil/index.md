---
schema: 1
kind: threat
title: "'Helix' data-extortion cluster pairs manager-impersonation vishing with device-code phishing and automated SharePoint exfiltration"
headline: "ReliaQuest: new 'Helix' extortion cluster (BlackFile/ShinyHunters lineage) vishes staff into device-code sign-ins, then bulk-loots SharePoint"
summary: >
  ReliaQuest documented a previously unreported data-extortion cluster it calls Helix, assessed as a
  likely continuation of the BlackFile (UNC6671) and ShinyHunters ecosystems on shared registrar and
  hosting infrastructure. Operators phone a target impersonating their named manager (spoofed
  caller-ID), walk them through an Entra ID device-code sign-in that captures a session token without
  a password and sidesteps Conditional Access, register a new Authenticator within minutes for
  persistence, then run automated SharePoint enumeration and bulk exfiltration. SharePoint + Entra ID
  is the default identity/collaboration stack across Swiss and EU public-sector tenants, so the
  playbook is directly reachable; disabling the device-code flow is the single highest-impact control.
discovered_at: "2026-07-10T12:53:00Z"
event_date: "2026-07-08"
run_id: 2026-07-10T1228Z-intel
priority: high
immediate_action: null
tags:
  - identity
  - phishing
  - cloud
  - data-breach
  - organized-crime
regions:
  - global
sectors:
  - public-sector
  - finance
  - technology
entities:
  - actor:helix-extortion
  - actor:unc6671
  - actor:shinyhunters
techniques: [T1566.004, T1528, T1098.005, T1213.002]
affected_products: ["Microsoft SharePoint", "Microsoft Entra ID", "Microsoft 365"]
cves: []
sources:
  - url: "https://reliaquest.com/blog/threat-spotlight-helix-new-name-in-data-extortion-ecosystem"
    publisher: "ReliaQuest"
    date: "2026-07-08"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/new-helix-vishing-group-emerges-in-sharepoint-data-theft-attacks/"
    publisher: "BleepingComputer"
    date: "2026-07-09"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Helix likely emerged from the “BlackFile” and “ShinyHunters” ecosystem. Groups fragment and rebrand, but the techniques and infrastructure persist across every iteration."
    publisher: "ReliaQuest"
  - quote: "Device code phishing then sidesteps Conditional Access policies, and automated tools enumerate and mass-download SharePoint libraries before bulk exfiltration triggers an alert."
    publisher: "ReliaQuest"
  - quote: "Disabling device code authentication is the single highest-impact action."
    publisher: "ReliaQuest"
verification: multi-source
sourcing_note: >
  The kill-chain TTPs are directly observed by ReliaQuest across multiple incidents and corroborated
  by BleepingComputer; the attribution to the BlackFile/ShinyHunters ecosystem is ReliaQuest's assessment
  (shared registrar and hosting-adjacent infrastructure), stated as "likely", not confirmed attribution.
  Classification B2.
confidence: high
update_of: null
references:
  - 2026-07-10/m365-conditional-access-gaps-railway-lshiy-campaigns
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Block or tightly scope the Entra ID device-code authentication flow tenant-wide — ReliaQuest names this the single highest-impact control, because it neutralises the session-token capture regardless of how convincing the vishing pretext is."
  - "Alert on a new MFA-authenticator registration occurring within minutes of a device-code sign-in from a residential-proxy IP the account has never used — that co-occurrence is Helix's persistence artifact and is otherwise indistinguishable from normal user activity."
  - "Hunt SharePoint/Graph access logs for enumeration using contentclass:STS_Site and wildcard search queries at automation speed from a non-browser (python-requests) user-agent, followed by bulk downloads — the automated-collection stage is the most reliable fingerprint."
migrated_from: null
---

ReliaQuest's Threat Research team published (2026-07-08) a spotlight on **Helix**, a data-extortion cluster it assesses as a likely continuation of the now-fragmented **BlackFile** (UNC6671) operation and the broader **ShinyHunters** ecosystem — an assessment resting on a shared credential-harvesting-domain registrar (also used by the Scattered Spider/"The Com" community) and an exfiltration host four addresses away, on the same autonomous system, from a confirmed BlackFile address two months earlier ([ReliaQuest, 2026-07-08](https://reliaquest.com/blog/threat-spotlight-helix-new-name-in-data-extortion-ecosystem)). ReliaQuest is explicit that this is likely-ecosystem-continuation, not confirmed attribution — but "organizations already tracking those groups should treat Helix as an extension of the same data extortion campaigns."

The device-code-phishing-defeats-Conditional-Access primitive itself was covered earlier today in the Huntress Railway/LSHIY analysis (see references); Helix's contribution is the full extortion kill chain wrapped around it. Initial contact is voice phishing in which the operator impersonates the target's actual manager by name on a spoofed caller-ID and talks them through entering a device code into Chrome — the session token is captured without any password crossing the phone line, and the device-code flow bypasses Conditional Access ([ReliaQuest, 2026-07-08](https://reliaquest.com/blog/threat-spotlight-helix-new-name-in-data-extortion-ecosystem); [BleepingComputer, 2026-07-09](https://www.bleepingcomputer.com/news/security/new-helix-vishing-group-emerges-in-sharepoint-data-theft-attacks/)). Persistence is deliberately minimal and hard to spot: the operator registers a new MFA Authenticator on the account, typically within minutes of sign-in, from the same residential proxy used for access — "the only persistence artifact is a legitimate MFA registration." Sign-in infrastructure is geo-matched to the target's real city to avoid impossible-travel alerts, rotating through 15+ residential IPs against a single mailbox. Collection is automated and identical across incidents — the operator issues `contentclass:STS_Site` and wildcard SharePoint searches to inventory reachable content, then bulk-downloads, using a `python-requests` user-agent from an IP reserved for exfiltration and never used for access. Dwell before mass exfil ranged from under an hour to over a week, a deliberate tuning to each environment's value and detectability. In at least one case the operator actively tested containment after the account was disabled, re-attempting MFA registration and a password reset.

**Defender takeaway:** the identity-based entry techniques (vishing, device-code phishing, MFA-registration persistence) are now shared tradecraft across the fragmenting data-extortion ecosystem, so detections built for Helix apply to BlackFile/ShinyHunters successors too. **Triage:** legitimate device-code authentication is rare in modern tenants (mostly CLI/headless flows), and a new MFA registration or a manager phone call can each be benign alone — the signal is the *sequence* within a short window: an unfamiliar manager-impersonation call, then a device-code sign-in from a never-seen residential IP, then a new Authenticator registered minutes later, then automated `python-requests` SharePoint enumeration and bulk download disproportionate to the user's baseline.
