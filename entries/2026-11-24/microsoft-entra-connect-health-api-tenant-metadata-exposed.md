---
schema: 1
kind: incident
title: "Microsoft Entra Connect Health: an API flaw present from 2026-07-23 was exploited to read tenant metadata including administrator and technical-contact email addresses; Microsoft fixed it server-side on 2026-11-19 and warns of targeted phishing"
headline: "Entra Connect Health API flaw exploited: admin email addresses read; Microsoft warns of targeted phishing"
summary: >
  Microsoft told Entra tenants from 2026-11-20 that a flaw in the Entra Connect Health API, introduced on 2026-07-23 and found on 2026-11-09, was exploited for unauthorized read-only access to tenant metadata: administrator and technical-contact email addresses, tenant identifiers and domain names, licence tier and directory-synchronisation status. It fixed the flaw server-side on 2026-11-19, says no customer update is needed and no configuration change was found, and advises expecting targeted phishing against the exposed addresses; it has not said who exploited the flaw, how many tenants are affected or when exploitation began.
discovered_at: "2026-11-24T04:31:30Z"
updated_at: null
event_date: "2026-11-20"
run_id: 2026-11-24T0355Z-intel
priority: notable
immediate_action: null
tags: [cloud, identity, data-breach]
regions: [global]
sectors: [technology]
entities: ["incident:microsoft-entra-connect-health-api-tenant-metadata-2026-11"]
techniques: [T1190, T1589.002]
affected_products: ["Microsoft Entra Connect Health"]
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/"
    publisher: "BleepingComputer"
    date: "2026-11-21"
    role: primary
  - url: "https://www.netzwoche.ch/news/2026-11-23/angreifer-lesen-konfigurationsdaten-von-microsoft-kunden-aus"
    publisher: "Netzwoche"
    date: "2026-11-23"
    role: corroborating
closed_sources: []
evidence:
  - quote: "On 20 November 2026, we concluded our investigation and determined that unauthorized read-only access to tenant-level metadata associated with your organization had occurred."
    publisher: "Microsoft customer notification, as quoted by BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/"
  - quote: "We deployed a fix on November 19, 2026, and have notified impacted customers through Azure Service Health, providing guidance and support"
    publisher: "Microsoft spokesperson, as quoted by BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/"
  - quote: "Microsoft has not disclosed who exploited the vulnerability, how many tenants were impacted, or when the attacks first began."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/"
verification: single-source-victim
sourcing_note: >
  The facts come from Microsoft's own customer notification, quoted by BleepingComputer, and from a Microsoft spokesperson's statement to BleepingComputer; Netzwoche re-reports BleepingComputer and adds no independent source. No Microsoft-hosted page was found; the notification text is known only through BleepingComputer's quotation of it.
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
  - "Open Azure Service Health in every Entra tenant you run and look for Microsoft's 2026-11-20 security notification; where it is present, warn the administrators and technical contacts whose addresses were exposed to expect targeted phishing and social engineering, because Microsoft says the exposed addresses and tenant details can be used for targeted attacks."
updates: []
migrated_from: null
---

Microsoft told tenants through Azure Service Health, from 2026-11-20, that a vulnerability in the Microsoft Entra Connect Health API, introduced on 2026-07-23 and found on 2026-11-09, was exploited for unauthorized read-only access to tenant-level metadata ([BleepingComputer, 2026-11-21](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/)). Connect Health is the cloud service that lets administrators monitor the health of their on-premises identity infrastructure through the Entra admin center ([BleepingComputer, 2026-11-21](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/)). Microsoft deployed a server-side fix on 2026-11-19, concluded its investigation on 2026-11-20 and found no unauthorized configuration change, although the flaw could in principle also have changed Connect Health monitoring settings ([BleepingComputer, 2026-11-21](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/); [Netzwoche, 2026-11-23](https://www.netzwoche.ch/news/2026-11-23/angreifer-lesen-konfigurationsdaten-von-microsoft-kunden-aus)).

The exposed data are the email addresses of tenant technical contacts and administrator accounts, tenant IDs, display names, initial domain names, country and region codes, Entra licence tiers and directory-synchronisation status, Connect Health onboarding status, and an expired agent-registration certificate for an internal Microsoft service decommissioned in late 2024; Microsoft says passwords, password hashes, authentication tokens, valid cryptographic keys, on-premises server and Active Directory topology and Azure subscription data were not exposed ([BleepingComputer, 2026-11-21](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/)). Microsoft has not said who exploited the flaw, how many tenants are affected or when the attacks began; more than a dozen administrators reported receiving the notice, and some managed service providers received notices for several customer tenants ([BleepingComputer, 2026-11-21](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/)).

**Exposure:** any tenant that received the Azure Service Health notification; Microsoft says the flaw needs no software update or other customer remediation ([BleepingComputer, 2026-11-21](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/)).

**Detection:** the leaked data cannot be recalled, so the signal is the follow-on: mail-flow and helpdesk telemetry for phishing or social-engineering messages aimed at the exposed administrator and technical-contact addresses, and Entra sign-in and audit logs for privileged accounts and for changes to Connect Health settings; Microsoft advises reviewing the Connect Health configuration and the Entra audit and sign-in logs, and its PowerShell script shows the current values of the exposed metadata types, not what was accessed ([BleepingComputer, 2026-11-21](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/)).

**Defender takeaway:** treat the exposed administrator and technical-contact addresses as targets of tailored phishing and social engineering, tell those people, and enforce phishing-resistant MFA on privileged accounts; there is nothing to patch ([BleepingComputer, 2026-11-21](https://www.bleepingcomputer.com/news/security/microsoft-entra-connect-health-flaw-exploited-to-steal-tenant-data/)).
