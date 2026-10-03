---
schema: 1
kind: incident
title: "ZeroBytes claims a third French government platform in three months: ~148.9M rows from Zéro Logement Vacant via a Metabase admin session and a cleartext production database password"
headline: "A BI tool's own admin API handed over the production database password it was supposed to protect"
summary: >
  The actor ZeroBytes, already tracked for the DGFiP tax-authority and Ministry of National
  Education intrusions, claims a third French public-sector platform compromise: Zéro Logement
  Vacant, a housing-vacancy tool run by the Ministry of Ecological Transition on beta.gouv.fr. Per
  the actor's own account, a valid Metabase administrator session exposed a production PostgreSQL
  password stored in cleartext in a database-connection description field, yielding ~148.9M raw
  rows including national property-owner and DGFiP/DataFoncier records; no government confirmation
  of scope exists, but the platform was taken offline.
discovered_at: "2026-08-31T04:55:00Z"
updated_at: null
event_date: "2026-08-25"
run_id: 2026-08-31T0411Z-intel
priority: high
immediate_action: null
tags: [data-breach]
regions: [europe]
sectors: [public-sector]
entities: ["actor:zerobytes", "incident:zero-logement-vacant-breach-2026-08", "incident:france-dgfip-tax-breach-2026-08", "incident:france-education-nationale-agent-training-breach-2026-07"]
techniques: [T1552.001, T1213]
affected_products: ["Metabase"]
cves: []
sources:
  - url: "https://www.zataz.com/zero-logement-vacant-vise-par-une-fuite-massive/"
    publisher: "ZATAZ.COM (Damien Bancal)"
    date: "2026-08-30"
    role: primary
  - url: "https://www.clubic.com/actualite-627343-zero-logement-vacant-pirate-148-9-millions-de-lignes-de-donnees-revendiquees-par-zerobytes.html"
    publisher: "Clubic (Mélina Loupia)"
    date: "2026-08-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "According to his account, initial access was obtained via a valid Metabase administrator session."
    original: "Selon son récit, l’accès initial aurait été obtenu via une session administrateur Metabase valide."
    publisher: "ZATAZ.COM"
    source_url: "https://www.zataz.com/zero-logement-vacant-vise-par-une-fuite-massive/"
  - quote: "the production PostgreSQL password was allegedly kept in cleartext in the description field of a database connection"
    original: "le mot de passe PostgreSQL de production aurait été conservé en clair dans le champ de description d’une connexion à la base"
    publisher: "ZATAZ.COM"
    source_url: "https://www.zataz.com/zero-logement-vacant-vise-par-une-fuite-massive/"
  - quote: "ZeroBytes strikes a third public service in three months"
    original: "ZeroBytes frappe un troisième service public en trois mois"
    publisher: "Clubic"
    source_url: "https://www.clubic.com/actualite-627343-zero-logement-vacant-pirate-148-9-millions-de-lignes-de-donnees-revendiquees-par-zerobytes.html"
verification: single-source
sourcing_note: "The access mechanism, row counts and person-count estimates are ZeroBytes' own unverified account, relayed by ZATAZ and independently write-up by Clubic (which itself cites FrenchBreaches and Cyberattaque.org) — neither outlet independently investigated the platform, and no government statement confirms scope. The platform being taken offline is the only independently observable corroborating fact."
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

The actor known as ZeroBytes — already tracked in this store for the DGFiP tax-authority credential intrusion and the claimed Ministry of National Education leak — claims a third French public-sector platform compromise in three months: Zéro Logement Vacant, a housing-vacancy tool built by La Fabrique numérique (Ministry of Ecological Transition) with the Agence nationale de l'habitat and hosted on beta.gouv.fr for municipal and collectivité housing officers ([ZATAZ.COM, 2026-08-30](https://www.zataz.com/zero-logement-vacant-vise-par-une-fuite-massive/)). Per the actor's own account, initial access was a valid Metabase (open-source BI tool) administrator session, which exposed the platform's full configuration: connected databases, accounts, permissions, saved queries and stored secrets, plus the ability to run native SQL against every connected database from within the tool.

The pivot that mattered came from a configuration weakness inside Metabase itself: the actor states Metabase's at-rest secret encryption was disabled, and a production PostgreSQL password had been stored in cleartext in a database connection's description field, retrievable through a call to Metabase's own admin API ([ZATAZ.COM, 2026-08-30](https://www.zataz.com/zero-logement-vacant-vise-par-une-fuite-massive/)). That password gave a direct, Metabase-independent read connection to the production instance hosted at Clever Cloud, so deleting the compromised Metabase accounts afterward did not cut off access; the credential reportedly stayed valid until rotated. Thirteen dashboards were said to be reachable with no authentication at all, some exposing email/bcrypt-hash pairs, and a JWT signing key was allegedly recoverable from platform settings.

The claimed haul totals 148,929,194 raw rows — roughly 82M from a national property-owner table and 67M from a 2024 DGFiP/DataFoncier national file (per ZATAZ: names, dates of birth, addresses and tax identifiers — [ZATAZ.COM, 2026-08-30](https://www.zataz.com/zero-logement-vacant-vise-par-une-fuite-massive/); per Clubic's own read of the same claim: property identifiers of the owners rather than tax identifiers — [Clubic, 2026-08-30](https://www.clubic.com/actualite-627343-zero-logement-vacant-pirate-148-9-millions-de-lignes-de-donnees-revendiquees-par-zerobytes.html)) — plus roughly 3,500 municipal-agent accounts and 10,729 unique emails and 6,847 unique phone numbers; deduplicated, the actor claims 48–71M distinct individuals depending on the matching method ([ZATAZ.COM, 2026-08-30](https://www.zataz.com/zero-logement-vacant-vise-par-une-fuite-massive/)). No government confirmation of scope was located, but Clubic reports the platform remains offline since the intrusion was discovered ([Clubic, 2026-08-30](https://www.clubic.com/actualite-627343-zero-logement-vacant-pirate-148-9-millions-de-lignes-de-donnees-revendiquees-par-zerobytes.html)) — a de facto acknowledgment an incident occurred, even absent a formal government statement.

**Defender takeaway:** the mechanism, not the actor, is the transferable exposure — a BI tool's own admin API returning a cleartext credential typed into a free-text connection-description field, then that credential outliving the BI account that exposed it. Any organisation running Metabase or a comparable BI tool against production data should audit connection configurations for credentials in free-text fields, enable at-rest secret encryption for the connection store, and rotate the underlying database credential — not just the BI-tool account — on any suspected BI-platform compromise, since deleting accounts alone does not invalidate an already-exposed password. Audit dashboards for anonymous/unauthenticated public sharing as a separate check; this incident reports thirteen such dashboards. This is directly transferable to Swiss federal and cantonal e-government analytics deployments running the same class of internal BI tooling against production registries.
