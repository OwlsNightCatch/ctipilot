---
schema: 1
kind: research
title: "BluePhishing: Proofpoint's proof of concept turns a consent link for a third-party Entra agent blueprint into tenant initial access, with an agent-creation permission that Proofpoint says cannot be revoked"
headline: "BluePhishing: consent to a rogue Entra agent blueprint gives tenant access, and default users can soon create blueprints"
summary: >
  Proofpoint describes BluePhishing, a research proof of concept that extends OAuth consent phishing to Microsoft Entra Agent ID: a victim who consents to an attacker's multi-tenant agent blueprint gets a blueprint principal with an agent-creation permission that Proofpoint says cannot be revoked, and the attacker then creates agent identities, up to 250 per blueprint, that inherit the consented permissions, which Microsoft's documentation says neither the Entra portal nor Microsoft Graph shows.
  Proofpoint has identified no in-the-wild activity, and Microsoft 365 message MC1506733 says default Entra users will be able to create agent blueprints from November 2026.
discovered_at: "2026-11-10T03:57:00Z"
updated_at: null
event_date: "2026-11-09"
run_id: 2026-11-10T0255Z-intel
priority: notable
immediate_action: null
tags: [identity, cloud, phishing, ai-abuse]
regions: [global]
sectors: []
entities: ["product:microsoft-entra-agent-id"]
techniques: [T1566.002, T1528, T1550.001, T1078.004, T1136.003, T1087.004]
affected_products: ["Microsoft Entra ID", "Microsoft Entra Agent ID"]
cves: []
sources:
  - url: "https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent"
    publisher: "Proofpoint"
    date: "2026-11-09"
    role: primary
closed_sources: []
evidence:
  - quote: "By default, blueprint principals were observed to have an implicit admin-consent permission, AgentIdentity.CreateAsManager, to allow the blueprint to create agent identities linked to itself."
    publisher: "Proofpoint"
    source_url: "https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent"
  - quote: "Proofpoint has not as of yet identified any in-the-wild activity"
    publisher: "Proofpoint"
    source_url: "https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent"
  - quote: "default Microsoft Entra users will be able to create agent blueprints by default from November 2026"
    publisher: "Proofpoint"
    source_url: "https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent"
verification: single-source
sourcing_note: >
  The mechanism, the permission behavior Proofpoint tested and the exposure statements are Proofpoint's own research on a proof of concept in a test tenant; no independent confirmation and no Microsoft statement on a fix were found, and Proofpoint says it notified Microsoft before publication. The Message Center item MC1506733 is cited as Proofpoint reports it.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Proofpoint presents BluePhishing, a proof of concept that extends OAuth consent phishing to Microsoft Entra Agent ID. The attacker builds an agent blueprint, the agent analogue of an app registration, in their own tenant with a client secret and permissions set to be inherited, sets its sign-in audience to work across tenants (a setting the Entra portal does not expose, so it takes Microsoft Graph, PowerShell or a manifest edit), and sends the victim a one-time consent link ([Proofpoint, 2026-11-09](https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent)). When a victim consents, a blueprint principal appears in the victim tenant with the AgentIdentity.CreateAsManager permission, which Proofpoint says cannot be revoked from the principal; the attacker then obtains an app-only Graph token for the victim tenant and creates agent identities, up to 250 per blueprint, that inherit the consented permissions ([Proofpoint, 2026-11-09](https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent)). Creating one needs the victim's tenant ID and the object ID of a sponsor user, both obtainable through documented unauthenticated lookups, and Proofpoint's tests used the Graph permissions User.Read.All and Group.Read.All ([Proofpoint, 2026-11-09](https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent)). Proofpoint, citing Microsoft's documentation, says inherited permissions are not visible in the Entra portal or in Microsoft Graph, which limits auditing what an agent identity can do; in its tests silent inheritance appeared only for delegated permissions, those granted through user consent ([Proofpoint, 2026-11-09](https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent)).

Proofpoint has identified no in-the-wild activity and says agent consent controls are less mature and less widely deployed than app consent controls; it adds that Microsoft 365 Message Center item MC1506733 says default Entra users will be able to create agent blueprints from November 2026 ([Proofpoint, 2026-11-09](https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent)).

**Exposure:** a Microsoft Entra tenant whose users or administrators can be led to approve a consent link; Proofpoint says the user consent settings that limit third-party app consent also extend to agent blueprints and their agent identities ([Proofpoint, 2026-11-09](https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent)).

**Detection:** Proofpoint says agent and blueprint events surface in the Entra audit log as app consent operations do, the creation of an agent identity blueprint as "Add application" and the creation of an agent identity as "Add service principal", and that the blueprint ID is the same in every tenant that consents to it, so a known malicious blueprint can be searched for across tenants ([Proofpoint, 2026-11-09](https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent)).

**Defender takeaway:** review the tenant's user consent settings and permission classifications before the November 2026 default lets default Entra users create agent blueprints, and look in the audit log for blueprint and agent-identity creations that nobody in IT made; no attacks have been reported, so this is a hardening decision, not an incident response.
