---
schema: 1
kind: incident
title: "Azure API Management Classic: a flaw let an unknown actor take secrets, named values and tokens from APIM instances; Norway's NSM names Equinor and Skagerak Energi among those hit and tells every APIM user to treat secrets as exposed and rotate them after Microsoft's 2026-11-19 mitigation"
headline: "Azure APIM Classic secrets exposed and exploited; NSM: assume compromise, rotate every token and secret"
summary: >
  Norway's NSM said on 2026-11-20 that an unknown actor actively went after access tokens, secrets and named values in Azure API Management, that the flaw hit several Norwegian organisations including Equinor and Skagerak Energi, and that it also affects other sectors and countries. Microsoft, in a customer notice quoted by SecurityWeek, identified the issue on 2026-11-18 and closed the access path on 2026-11-19, and says Classic instances were exposed before it identified the issue while v2 tiers are not affected. NSM tells every APIM user to assume secrets and named values are exposed and to rotate all tokens and secrets.
discovered_at: "2026-11-24T04:32:00Z"
updated_at: null
event_date: "2026-11-17"
run_id: 2026-11-24T0355Z-intel
priority: high
immediate_action: null
tags: [cloud, actively-exploited, data-breach]
regions: [global, nordics]
sectors: [energy, technology]
entities: ["incident:azure-api-management-classic-secrets-exposure-2026-11"]
techniques: [T1190, T1528, T1552]
affected_products: ["Azure API Management"]
cves: []
sources:
  - url: "https://nsm.no/aktuelt/nsm-deler-tiltak-mot-sarbarhet-i-azure-api-management"
    publisher: "Nasjonal sikkerhetsmyndighet (NSM, Norway)"
    date: "2026-11-20"
    role: primary
  - url: "https://www.securityweek.com/azure-flaw-exploited-to-target-secrets-at-norwegian-energy-firms/"
    publisher: "SecurityWeek"
    date: "2026-11-23"
    role: corroborating
  - url: "https://www.equinor.com/news/20261711-equinor-detected-cyber-attack"
    publisher: "Equinor"
    date: "2026-11-20"
    role: corroborating
  - url: "https://www.skagerakenergi.no/presse/pressemeldinger/skagerak-energi-utsatt-for-forsok-pa-cyberangrep"
    publisher: "Skagerak Energi"
    date: "2026-11-18"
    role: corroborating
  - url: "https://anderskristiansen.com/post/2026/apim-legacy-access/"
    publisher: "Anders Kristiansen (independent practitioner)"
    date: "2026-11-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An unknown actor has actively gone after access tokens, secrets and named values in APIM. (translated from Norwegian)"
    original: "En ukjent aktør har aktivt gått etter access tokens, secrets og named values i APIM."
    publisher: "Nasjonal sikkerhetsmyndighet (NSM, Norway)"
    source_url: "https://nsm.no/aktuelt/nsm-deler-tiltak-mot-sarbarhet-i-azure-api-management"
  - quote: "Equinor and Skagerak Energi are among the organisations that have been hit. (translated from Norwegian)"
    original: "Equinor og Skagerak Energi er blant virksomhetene som har blitt rammet."
    publisher: "Nasjonal sikkerhetsmyndighet (NSM, Norway)"
    source_url: "https://nsm.no/aktuelt/nsm-deler-tiltak-mot-sarbarhet-i-azure-api-management"
  - quote: "Everyone who has Azure API Manager must assume that their secrets and named values have been compromised. (translated from Norwegian)"
    original: "Alle som har Azure API Manager må ta utgangspunkt i at deres secrets og named values er på avveie."
    publisher: "Nasjonal sikkerhetsmyndighet (NSM, Norway)"
    source_url: "https://nsm.no/aktuelt/nsm-deler-tiltak-mot-sarbarhet-i-azure-api-management"
  - quote: "Our investigation found that customers were exposed and an unauthorized party could have used the issue to access secrets stored in Azure API Management Classic instances before Microsoft identified the security issue"
    publisher: "Microsoft customer notice, as quoted by SecurityWeek"
    source_url: "https://www.securityweek.com/azure-flaw-exploited-to-target-secrets-at-norwegian-energy-firms/"
verification: multi-source
sourcing_note: >
  NSM, the Norwegian national authority, states the exploitation, the victims and the remediation; Microsoft's customer notice is known only through SecurityWeek's quotation of it. Equinor and Skagerak Energi describe their own incidents and do not name Azure API Management; the link comes from NSM and SecurityWeek. The Equinor page was first published on 2026-11-17 and last updated on 2026-11-20, and its citation carries the last update date. No CVE id appears in any source read. Anders Kristiansen's page is dated 2026-11-21 and describes the events of 2026-11-20.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "On every Azure API Management instance, read the gateway RuntimeVersion as NSM describes (0.52.x is patched from build 31936, 0.53.x from build 31938, and v2 or Consumption-tier patterns are not affected) and, whatever the result, rotate every named value, backend credential, identity-provider client secret, subscription key and token the instance held, plus the Key Vault secrets it references, then review the Activity, gateway, Key Vault and service-principal sign-in logs for use of the old values, because NSM says to assume secrets and named values are exposed and Microsoft's notice says Classic instances were exposed before Microsoft identified the issue on 2026-11-18 and mitigated it on 2026-11-19."
updates: []
migrated_from: null
---

Norway's National Security Authority (NSM) said on 2026-11-20, in a post updated on 2026-11-23, that an unknown actor has actively gone after access tokens, secrets and named values in Azure API Management (APIM), that Equinor and Skagerak Energi are among the organisations hit, and that the flaw also affects several sectors in Norway and beyond its borders (translated from Norwegian) ([NSM, 2026-11-20](https://nsm.no/aktuelt/nsm-deler-tiltak-mot-sarbarhet-i-azure-api-management)). NSM says it is still uncertain how widely the flaw has been and is being exploited, and that it has no indication so far that compromises or attempts have affected deliveries at Norwegian organisations (translated from Norwegian) ([NSM, 2026-11-20](https://nsm.no/aktuelt/nsm-deler-tiltak-mot-sarbarhet-i-azure-api-management)).

Microsoft's customer notice, read by SecurityWeek, says Microsoft discovered the issue on 2026-11-18 and closed the access path the next day, and that an unauthorized party could have used it to reach secrets stored in Azure API Management Classic instances before Microsoft identified the issue; exposed data can include secrets stored as named values, client secrets for identity providers, subscription keys and tokens for APIM's direct management APIs, and instances on the v2 tiers are not affected ([SecurityWeek, 2026-11-23](https://www.securityweek.com/azure-flaw-exploited-to-target-secrets-at-norwegian-energy-firms/)). SecurityWeek adds that Microsoft noted Classic tiers that do not follow its documented security guidance are affected ([SecurityWeek, 2026-11-23](https://www.securityweek.com/azure-flaw-exploited-to-target-secrets-at-norwegian-energy-firms/)). Equinor reported its attack on 2026-11-17, said on 2026-11-19 that it did not appear to target Equinor specifically and on 2026-11-20 that the attack had been stopped ([Equinor, 2026-11-20](https://www.equinor.com/news/20261711-equinor-detected-cyber-attack)); Skagerak Energi reported a possible attempted attack on 2026-11-18 and said operations and production were not affected and there was no indication that information had left ([Skagerak Energi, 2026-11-18](https://www.skagerakenergi.no/presse/pressemeldinger/skagerak-energi-utsatt-for-forsok-pa-cyberangrep)). No source says how the flaw works, who the actor is or how many tenants lost secrets.

NSM tells every APIM user to assume that secrets and named values are exposed and to rotate all tokens and secrets, to map what sits behind each instance to judge the potential scope, and to check whether the instance has been updated (translated from Norwegian) ([NSM, 2026-11-20](https://nsm.no/aktuelt/nsm-deler-tiltak-mot-sarbarhet-i-azure-api-management)).

**Exposure:** NSM's guide reads the RuntimeVersion from the gateway's internal-status page: 0.52.x is patched from build 31936, 0.53.x from build 31938, lower numbers are still vulnerable, and patterns such as 0.53.4608.0 are v2 or Consumption tier and not vulnerable; an organisation whose instance is not updated is asked to contact the vendor, and one that sees signs of compromise to contact NSM (translated from Norwegian) ([NSM, 2026-11-20](https://nsm.no/aktuelt/nsm-deler-tiltak-mot-sarbarhet-i-azure-api-management)).

**Detection:** an independent practitioner's hunting map, which is not a confirmed attack chain, points to the Azure Activity log for secret-list requests and configuration changes, APIM gateway logs for newly seen subscription identifiers and tracing requests, developer-portal audit logs to see whether an unused portal is in use, Entra service-principal sign-ins for use of the app credentials APIM held, Key Vault audit logs for reads of the secrets APIM references, and Microsoft Graph activity logs; calls to the retired direct Management API do not appear in the Activity log ([Anders Kristiansen, 2026-11-21](https://anderskristiansen.com/post/2026/apim-legacy-access/)). Credentials lifted from APIM can be used against outside services, and the damage depends on each credential's permissions ([SecurityWeek, 2026-11-23](https://www.securityweek.com/azure-flaw-exploited-to-target-secrets-at-norwegian-energy-firms/)).

**Defender takeaway:** patching is not the end: treat every APIM instance as having lost the secrets it held, rotate them all and then hunt for their use; the practitioner guide also advises switching off the retired direct Management API and closing an unused developer portal ([Anders Kristiansen, 2026-11-21](https://anderskristiansen.com/post/2026/apim-legacy-access/)).
