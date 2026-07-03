---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "EU Cybersecurity Package 2026 — NIS2 amendment (COM(2026) 13) + Cybersecurity Act 2 enter EP preparatory phase; PQC obligation embedded"
headline: "EU Cybersecurity Package 2026 — NIS2 amendment (COM(2026) 13) + Cybersecurity Act 2 enter EP preparatory phase; PQC obligation embedded"
summary: "The European Commission's 20 January 2026 cybersecurity package bundles a targeted NIS2 amendment (COM(2026) 13) with a new Cybersecurity Act 2 (CSA2). Public-feedback period closed 22 April 2026 — the package is now in the European Parliament preparatory phase, with political agreement targeted for early 2027."
discovered_at: "2026-05-04T05:00:47Z"
event_date: 2026-03-27
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - eu-nexus
  - vulnerabilities
regions:
  - europe
sectors: []
entities:
  - "campaign:eu-cybersecurity-package-2026"
cves: []
sources:
  - url: "https://www.dlapiper.com/en/insights/publications/2026/02/nis2-update-eu-moves-to-harmonise-cyber-controls-refine-scope-and-add-new-in-scope-entities"
    publisher: DLA Piper — NIS2 update EU moves to harmonise cyber controls
    role: primary
  - url: "https://www.skadden.com/insights/publications/2026/03/european-commission-announces-potential-nis2-cybersecurity-reform"
    publisher: Skadden — Potential NIS2 cybersecurity reform
    role: corroborating
  - url: "https://www.globalpolicywatch.com/2026/01/european-commission-proposes-cybersecurity-act-2-new-eu-supply-chain-rules-and-certification-reforms/"
    publisher: Covington — Cybersecurity Act 2
    role: corroborating
  - url: "https://postquantum.com/security-pqc/eu-pqc-nis2/"
    publisher: PostQuantum.com — EU PQC NIS2
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W19.md
---

The European Commission's 20 January 2026 cybersecurity package bundles a targeted NIS2 amendment (COM(2026) 13) with a new Cybersecurity Act 2 (CSA2). Public-feedback period closed 22 April 2026 — the package is now in the European Parliament preparatory phase, with political agreement targeted for early 2027. Key NIS2-amendment changes obligations-relevant to Swiss / EU public-sector SOCs: (1) scope expansion to submarine data-transmission infrastructure (SDTI) operators and European Digital Identity Wallet providers as essential entities; (2) **mandatory ransomware reporting** — competent authorities can demand whether a ransom was paid, to whom, and how much, when a reported incident involves ransomware; (3) Article 21 harmonised technical requirements at Commission level create a regulatory ceiling, blocking member states from adding further technical obligations — meaning an EU certification scheme can demonstrate compliance portably; (4) new **Article 7(2)(k) mandates member-state PQC transition policies** aligned with the 2030 (critical uses) / 2035 (medium/low uses) roadmap — the first time post-quantum is an explicit named NIS2 obligation rather than implied "state of the art" interpretation ([DLA Piper, 2026-02-16](https://www.dlapiper.com/en/insights/publications/2026/02/nis2-update-eu-moves-to-harmonise-cyber-controls-refine-scope-and-add-new-in-scope-entities) · [Skadden, 2026-03-27](https://www.skadden.com/insights/publications/2026/03/european-commission-announces-potential-nis2-cybersecurity-reform) · [PostQuantum.com — EU PQC NIS2, 2026-02-13](https://postquantum.com/security-pqc/eu-pqc-nis2/)).

CSA2 introduces the EU's first horizontal ICT supply-chain security framework: the Commission designates "key ICT assets" used by NIS2-essential entities, identifies high-risk supplier countries, and may prohibit or restrict their components in those assets — directly analogous to 5G supply-chain restrictions, now extended to all essential sectors. ENISA's budget rises 75%+ and it takes on operational functions including the **European Vulnerability Database (EUVD)**, early-warning publication, and the **CRA Single Reporting Platform (SRP) — live 11 September 2026** ([Covington — Cybersecurity Act 2, 2026-01-23](https://www.globalpolicywatch.com/2026/01/european-commission-proposes-cybersecurity-act-2-new-eu-supply-chain-rules-and-certification-reforms/)). **What defenders need to do differently:** (1) inventory current "state of the art" cryptography claims that relied on implicit NIS2 interpretation — the explicit PQC Article creates a documented compliance gap supervisors can cite in audit findings; (2) plan for SRP single-report submission flow ahead of 11 September 2026 — public-sector and vendor PSIRTs operating in NIS2-essential categories will be expected to publish through this channel rather than parallel-submit to member-state CSIRTs; (3) ransomware playbooks should anticipate the documentation question chain on payment-or-not, intermediary used, amount transferred. NIS2 amendment requires 12-month transposition; CSA2 applies directly.
