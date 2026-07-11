---
schema: 1
kind: threat
horizon: operational
title: "Miasma supply-chain worm reaches 73 Microsoft GitHub repositories, adds Azure credential collectors"
headline: "Miasma supply-chain worm reaches 73 Microsoft GitHub repositories, adds Azure credential collectors"
summary: "UPDATE (originally covered 2026-06-02): The Miasma worm — the TeamPCP-spawned descendant of the Mini Shai-Hulud lineage first covered against the Red Hat @redhat-cloud-services npm namespace — recompromised the durabletask package and propagated into the Microsoft GitHub estate."
discovered_at: "2026-06-06T05:00:06Z"
event_date: 2026-06-06
run_id: 2026-06-06-d01b95fe
priority: notable
immediate_action: null
tags:
  - supply-chain
  - cloud
  - infostealer
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "campaign:mini-shai-hulud"
  - "actor:teampcp"
  - "campaign:miasma-redhat-npm-supply-chain"
cves: []
sources:
  - url: "https://opensourcemalware.com/blog/miasma-reaches-azure"
    publisher: OpenSourceMalware — The Blight Reaches Microsoft
    role: primary
  - url: "https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html"
    publisher: "The Hacker News, 2026-06-06"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-06-02/miasma-worm-backdoors-32-red-hat-cloud-services-npm-packages
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-06.md
---

**UPDATE (originally covered 2026-06-02):** The Miasma worm — the TeamPCP-spawned descendant of the Mini Shai-Hulud lineage first covered against the Red Hat `@redhat-cloud-services` npm namespace — recompromised the `durabletask` package and propagated into the Microsoft GitHub estate. On 2026-06-05 GitHub disabled **73 repositories** across the Azure, Azure-Samples, Microsoft and MicrosoftDocs organisations in a 105-second automated terms-of-service sweep, taking the entire Azure Durable Task family (.NET, Go, Java, JS, MSSQL, Netherite, protobuf) offline ([OpenSourceMalware, 2026-06-05](https://opensourcemalware.com/blog/miasma-reaches-azure); [The Hacker News, 2026-06-06](https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html)).

The material delta from the 2026-06-02 coverage: the variant adds **Azure CLI auth-cache and managed-identity token collectors** (earlier Shai-Hulud strains targeted AWS and GitHub), and the recompromise traces to the same `durabletask` credential foothold from the May TeamPCP incident — i.e. credentials taken in May were never fully revoked. Azure Durable Task is a foundational dependency for Azure Functions / serverless workflows widely consumed in EU public-sector cloud deployments, so the downstream exposure is cloud infrastructure, not just developer machines.

Defender takeaway: audit `~/.azure/` credential stores on developer workstations and CI/CD runners that installed any affected `@azure/*` package; rotate Azure managed-identity tokens and Kubernetes service-account tokens on those systems; monitor GitHub audit logs for unexpected public-repo creation (the worm's secret-exfil-as-public-repo behaviour is what trips GitHub's automated sweep). Note the worm-vs-defender naming overlap is real here — "Miasma" is the attacker worm, not a tool.
