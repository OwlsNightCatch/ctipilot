---
schema: 1
kind: threat
title: "A Gentlemen ransomware affiliate ran his own leak site and reached his victims through stolen CI/CD secrets, with attack commands driven through an MCP server (CloudSEK)"
headline: "CloudSEK: a Gentlemen affiliate reached victims through stolen GitLab CI/CD secrets and drove attacks over MCP"
summary: >
  CloudSEK analysed two exposed servers of "Azazel", a Russian-speaking affiliate of the Gentlemen ransomware group who also
  ran his own leak site, and reports about 6 TB of stolen data from some two dozen organisations, among
  them government-adjacent infrastructure. It says every confirmed victim was reached through stolen CI/CD secrets, mainly
  GitLab variable stores and git history, that one deeper intrusion into an AI platform chained server-side request forgery, a
  recovered master key that decrypted the configuration and a token recovered from git history, and that Azazel drove attack commands through an MCP
  server on a local port. The report is a single source and names no victim.
discovered_at: "2026-10-07T04:46:00Z"
updated_at: null
event_date: "2026-10-05"
run_id: 2026-10-07T0404Z-intel
priority: notable
immediate_action: null
tags: [ransomware, organized-crime, ai-abuse]
regions: [global]
sectors: [technology, healthcare, public-sector]
entities: ["actor:azazel", "product:gitlab", "product:model-context-protocol-mcp"]
techniques: [T1190, T1552.001, T1552.004, T1213.003, T1078, T1110.002, T1530, T1567.002, T1485, T1491.001]
affected_products: ["GitLab", "Model Context Protocol (MCP)"]
cves: []
sources:
  - url: "https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files"
    publisher: "CloudSEK TRIAD"
    date: "2026-10-05"
    role: primary
closed_sources: []
evidence:
  - quote: "Every confirmed victim was reached through stolen CI/CD secrets."
    publisher: "CloudSEK TRIAD"
    source_url: "https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files"
  - quote: "Azazel registered a reverse shell handler as a tool inside an AI coding assistant via MCP, then drove attack execution through it."
    publisher: "CloudSEK TRIAD"
    source_url: "https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files"
  - quote: "Azazel recovered credentials from commits that appeared removed from the current branch."
    publisher: "CloudSEK TRIAD"
    source_url: "https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files"
verification: single-source
sourcing_note: >
  CloudSEK is the sole assessor and worked from the actor's own exposed servers; it names no victim, says it notified the
  victims it identified before publication, and the sector, country and volume figures are its own counts. Its text says more
  than two dozen victims in six countries, while the victim chart on the same page shows 22 victims across ten named countries
  and six unattributed. CloudSEK says it has not
  identified earlier public reporting of MCP used as an attack execution channel in a live criminal campaign.
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

CloudSEK reports that an exposed open directory and a misconfigured storage server revealed the operation of "Azazel", a Russian-speaking affiliate of the Gentlemen ransomware group, who used the group's tooling, negotiation channels and ransom-note template but published victims on a leak site of his own and kept the proceeds, so the Gentlemen operator lost the revenue ([CloudSEK, 2026-10-05](https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files)). Two servers held about 6 TB of stolen data from some two dozen victims, spanning logistics, insurance, pharmaceutical, AI, medical-device and government-adjacent organisations ([CloudSEK, 2026-10-05](https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files)).

Every victim outside one deeper intrusion was reached the same way: GitLab CI/CD variable stores and git history were mined for tokens, database credentials, API keys and SSH private keys with enumeration and secret-scanning tools, and one GitLab instance that served two unrelated organisations gave footholds at both ([CloudSEK, 2026-10-05](https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files)). From one CI/CD token the actor reached more than 150 databases, payment gateways and hundreds of source repositories across a SaaS platform and its clients, and at a platform hosting a government-linked financial registry it exfiltrated more than 120,000 records and then killed the PostgreSQL process and deleted the production data directory ([CloudSEK, 2026-10-05](https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files)). The deeper intrusion, into an AI platform, ran for weeks: an API that fetches user-supplied URLs server-side gave an unauthenticated route into the internal network, a recovered master key decrypted every secret in the cluster configuration, a hardcoded authentication-bypass token that had been removed from the code but stayed in git history gave lasting access, offline cracking was run against administrator hashes from the monitoring stack, and an object-storage bucket was mirrored continuously ([CloudSEK, 2026-10-05](https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files)). Ransom notes were pushed to eight surfaces, among them the login message, the SSH banner, a database configuration parameter, a database-admin login template, a repository README and an issue opened against the victim's project, and CloudSEK reports that the verification script drove these checks through an MCP server bound to a local port, an operational use of MCP as an attack execution channel of which CloudSEK has not identified earlier public reporting ([CloudSEK, 2026-10-05](https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files)).

**Exposure:** self-hosted GitLab where CI/CD variables are unmasked or unprotected or where removed secrets remain in git history, GitLab instances that run pipelines for more than one organisation, APIs that fetch user-supplied URLs without validation, and MCP servers reachable beyond strict loopback ([CloudSEK, 2026-10-05](https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files)).

**Detection:** CI/CD and repository audit logs for variable reads from unexpected addresses, service-account token use outside the normal runner infrastructure, and README or issue changes made with a pipeline token from an unusual source; object-storage and database logs for bulk mirroring or dumps to hosts outside the backup estate; MCP initialisation requests from clients outside an allowlist; and a PostgreSQL process killed and its data directory deleted after a large read ([CloudSEK, 2026-10-05](https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files)).

**Triage:** legitimate backup jobs also mirror object storage to remote destinations, so the discriminator is the destination and the source host, not the copy command itself ([CloudSEK, 2026-10-05](https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files)).

**Defender takeaway:** treat CI/CD variable stores and git history as credential stores: keep secrets in a dedicated secrets manager, mask and protect every variable, rotate tokens and audit history for removed secrets, because the actor recovered credentials from commits that no longer appeared on the current branch; never bind an MCP server beyond loopback and treat its command-execution tool as privileged with an audit trail ([CloudSEK, 2026-10-05](https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files)).
