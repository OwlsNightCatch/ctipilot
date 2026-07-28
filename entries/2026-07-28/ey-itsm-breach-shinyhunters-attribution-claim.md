---
schema: 1
kind: incident
horizon: operational
title: "ShinyHunters claims the Ernst & Young ITSM breach and asserts the stolen third-party credentials reached Jira, GitHub and Azure"
headline: "ShinyHunters claims the EY support-platform breach and alleges reach far beyond the disclosed ticket data"
summary: >
  ShinyHunters added Ernst & Young to its leak site on 2026-07-27, claiming responsibility for the
  third-party ITSM support-platform breach EY disclosed on 2026-07-15 and telling BleepingComputer the
  credentials were obtained through a supply-chain attack and allowed it into EY's Jira, GitHub and Azure
  environments — a scope far beyond the support-ticket attachments EY acknowledged. EY has not confirmed
  the attribution or the claimed reach, and BleepingComputer states it cannot verify the actor's
  assertions. The transferable point for anyone who outsources IT helpdesk or ticketing is the claimed
  pivot itself: credentials held by a support platform are worth scoping as reaching everything they can
  authenticate to, not just the tickets they were issued for.
discovered_at: "2026-07-28T04:51:00Z"
event_date: "2026-07-27"
run_id: 2026-07-28T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, supply-chain, identity]
regions: [global]
sectors: [finance, public-sector]
entities: ["actor:shinyhunters", "incident:ey-third-party-itsm-breach-2026"]
techniques: [T1199, T1078]
affected_products: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/ernst-and-young-data-breach-claimed-by-shinyhunters-extortion-gang/"
    publisher: "BleepingComputer"
    date: "2026-07-27"
    role: primary
closed_sources: []
evidence:
  - quote: "The threat actors claimed to BleepingComputer that EY credentials were obtained through a supply-chain attack and used to breach the company. These stolen credentials allegedly allowed them to breach Ernst & Young's Jira, GitHub, and Azure environments."
    publisher: "BleepingComputer"
  - quote: "BleepingComputer has no way to verify the threat actor's claims independently, and Ernst & Young has not confirmed that ShinyHunters was behind the attack."
    publisher: "BleepingComputer"
verification: single-source
sourcing_note: "Single-source by design rather than by omission. BleepingComputer is the only outlet that both carries the leak-site listing and put the actor's claims directly to the group and to EY (reliability B). The underlying breach is already established by EY's own regulatory filings, covered here on 2026-07-19; what is new is an actor claim, and every element of it — the supply-chain credential theft, the Jira/GitHub/Azure reach, the extortion deadline — is unverified, with BleepingComputer stating so explicitly and EY declining to confirm the attribution. Credibility is therefore 3: a plausible, self-interested claim from a group with a documented 2026 track record in this exact intrusion class, corroborated by nobody."
confidence: low
update_of: 2026-07-19/ernst-young-third-party-itsm-platform-breach-client-tax-data
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-07-19):** The Ernst & Young third-party ITSM breach now has a claimed author. ShinyHunters added EY to its data-leak site on 2026-07-27, claiming it carried out the attack and threatening to publish the stolen data unless the firm makes contact by 2026-07-31 ([BleepingComputer, 2026-07-27](https://www.bleepingcomputer.com/news/security/ernst-and-young-data-breach-claimed-by-shinyhunters-extortion-gang/)). At first coverage no group had claimed the intrusion.

The substantive delta is the claimed scope. The group told BleepingComputer that EY credentials "were obtained through a supply-chain attack and used to breach the company", and that those credentials "allegedly allowed them to breach Ernst & Young's Jira, GitHub, and Azure environments" — issue tracking, source control and a cloud control plane, none of which appears in EY's own disclosure, which described support tickets that may contain client tax documents. The group declined to name the compromised third party or say what was taken, while asserting that the data EY acknowledged was exposed along with more ([BleepingComputer, 2026-07-27](https://www.bleepingcomputer.com/news/security/ernst-and-young-data-breach-claimed-by-shinyhunters-extortion-gang/)). None of this is confirmed: BleepingComputer states it "has no way to verify the threat actor's claims independently, and Ernst & Young has not confirmed that ShinyHunters was behind the attack" ([BleepingComputer, 2026-07-27](https://www.bleepingcomputer.com/news/security/ernst-and-young-data-breach-claimed-by-shinyhunters-extortion-gang/)). The report also names Experian as the provider of the 24 months of identity monitoring EY is offering affected clients, which the original coverage recorded without naming.

**Defender takeaway:** treat the claim as a scoping hypothesis rather than as news about EY. The original entry's lesson was about what accumulates inside support-ticket systems; this one is about what a support platform's credentials can reach. If a helpdesk or ITSM platform holds service-account credentials, API tokens or federated identities that also authenticate to issue tracking, source control or a cloud tenant, then a confirmed compromise of that platform is a trigger to rotate everything reachable from it and to review authentication logs in those downstream systems for the intrusion window — not merely to notify the people whose tickets were exposed. That action does not depend on whether this particular claim is true.

**Triage:** an intrusion of this shape presents in the downstream systems as valid-credential access, not as exploitation — successful authentications by a support-platform service account or an integration identity, arriving in the platform's normal window and often from plausible infrastructure. The discriminator is not the authentication itself but its reach: a support integration that has historically only ever read issue metadata suddenly enumerating repositories, cloning at volume, or touching cloud control-plane APIs is the deviation, and the baseline for "what this identity normally does" is the control that makes it visible.
