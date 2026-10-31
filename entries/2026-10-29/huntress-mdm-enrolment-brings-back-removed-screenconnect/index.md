---
schema: 1
kind: threat
title: "Huntress: phished MDM enrolments in Hexnode and Rippling give attackers a management path that brings ScreenConnect back after it has been removed"
headline: "Huntress: phished MDM enrolments push ScreenConnect back after removal; the RMM is not the root of the intrusion"
summary: >
  Huntress reports several recent incidents in which phishing victims ended up with an MDM client from Hexnode or Rippling followed by an unauthorised ScreenConnect agent. In the Rippling case the
  attacker used the MDM, running with SYSTEM rights, to stage and run ScreenConnect; in the Hexnode case the managed-service provider removed ScreenConnect and it returned several hours later to
  the same relay while the Hexnode client was still installed. Huntress says the products are not at fault and that removing the RMM does not remove the management architecture behind it.
discovered_at: "2026-10-29T04:45:00Z"
updated_at: null
event_date: "2026-10-28"
run_id: 2026-10-29T0255Z-intel
priority: notable
immediate_action: null
tags: [phishing]
regions: [global]
sectors: []
entities: ["product:connectwise-screenconnect", "product:hexnode-mdm", "product:rippling-mdm"]
techniques: [T1566.002, T1204.002, T1072, T1219]
affected_products: ["Hexnode MDM", "Rippling MDM", "ConnectWise ScreenConnect"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/attackers-turn-mdm-into-remote-access"
    publisher: "Huntress"
    date: "2026-10-28"
    role: primary
closed_sources: []
evidence:
  - quote: "removing it does not remove the unauthorized management architecture that delivered it."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/attackers-turn-mdm-into-remote-access"
  - quote: "MDM enrollment should be treated as security-sensitive activity as opposed to a routine administrative task."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/attackers-turn-mdm-into-remote-access"
  - quote: "Maintain an inventory of authorized MDM products, tenants, agents, and RMM instances."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/attackers-turn-mdm-into-remote-access"
verification: single-source
sourcing_note: >
  Huntress is the only source and reports two incidents in detail out of several; it names no actor, victim sector or count beyond several, says Hexnode and Rippling are not at fault, and
  says the two MDM products are not a definitive list. In the Rippling case Huntress infers from the online management agent that the attacker had created its own tenant earlier.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "On every endpoint from which an unauthorised ScreenConnect or other RMM agent has been removed, check for a Hexnode or Rippling MDM agent or enrolment that nobody authorised and unenrol the device from that tenant, because in Huntress's Hexnode case ScreenConnect returned hours after its removal while the MDM client stayed."
updates: []
migrated_from: null
---

Huntress reports several recent incidents in which attackers used legitimate mobile-device-management platforms, not flaws in them, as a trusted management path, naming Hexnode and Rippling as the two it saw and noting the list is not definitive ([Huntress, 2026-10-28](https://www.huntress.com/blog/attackers-turn-mdm-into-remote-access)). In the first case, proposal-themed emails led a user to download an MSI named like a DocuSign installer that installed Hexnode components (gateway, agent and PostgreSQL components); ScreenConnect followed shortly after and connected to an attacker relay, the managed-service provider removed it, and it came back several hours later to the same relay while the Hexnode client was still installed ([Huntress, 2026-10-28](https://www.huntress.com/blog/attackers-turn-mdm-into-remote-access)). In the second, a receptionist clicked a link in an email about tax planning that led to a fake Teams calendar page; about a minute later a Rippling enrolment registry key appeared, the agent was downloaded into a SYSTEM profile path and installed with SYSTEM rights, and about 35 minutes after that the attacker used the MDM to stage and run a ScreenConnect installer as SYSTEM ([Huntress, 2026-10-28](https://www.huntress.com/blog/attackers-turn-mdm-into-remote-access)).

**Exposure:** a managed Windows endpoint whose user can run an installer or follow an enrolment link, in an organisation without an inventory of its authorised MDM tenants, agents and RMM instances ([Huntress, 2026-10-28](https://www.huntress.com/blog/attackers-turn-mdm-into-remote-access)).

**Detection:** the chain Huntress describes as a stronger signal is social engineering, then a new MDM enrolment, then an RMM installation, then outbound communication with an unfamiliar relay, correlated across identity, MDM, endpoint and network telemetry; in endpoint telemetry that is an MSI run from a browser download folder that installs an MDM agent, an enrolment registry key on a device nobody enrolled, a new SYSTEM-level agent in a vendor directory shortly after a click, and an RMM installed by that agent ([Huntress, 2026-10-28](https://www.huntress.com/blog/attackers-turn-mdm-into-remote-access)). A repeat of the same RMM relay after the RMM was removed, as in the Hexnode case, points to a remaining MDM client as a possible source ([Huntress, 2026-10-28](https://www.huntress.com/blog/attackers-turn-mdm-into-remote-access)).

**Triage:** a corporate enrolment started by IT looks similar in process telemetry; the discriminators are a tenant that is not in the authorised inventory, a trigger that is an emailed link or a user-run installer instead of IT's enrolment workflow, and an RMM install within minutes (an inference from Huntress's two cases).

**Defender takeaway:** treat an unexpected MDM enrolment as a security event and keep an inventory of authorised tenants; after removing a rogue RMM, unenrol the device from the unauthorised tenant, disable accounts the attacker created, revoke sessions and tokens, reset credentials and reimage the endpoint if its integrity cannot be confirmed, as Huntress advises ([Huntress, 2026-10-28](https://www.huntress.com/blog/attackers-turn-mdm-into-remote-access)).
