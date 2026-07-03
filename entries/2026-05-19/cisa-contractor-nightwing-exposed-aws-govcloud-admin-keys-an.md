---
schema: 1
kind: incident
horizon: operational
title: "CISA contractor (Nightwing) exposed AWS GovCloud admin keys and internal credentials in public GitHub repo for ~6 months"
headline: "CISA contractor (Nightwing) exposed AWS GovCloud admin keys and internal credentials in public GitHub repo for ~6 months"
summary: "CISA contractor (Nightwing) exposed AWS GovCloud admin keys and internal credentials for ~6 months via public GitHub repo (Krebs on Security, 2026-05-18). GitGuardian found credentials to three GovCloud accounts, plaintext passwords for dozens of internal CISA systems, and the LZ-DSO Artifactory build-package repo; keys validated live 48h after takedown."
discovered_at: "2026-05-19T05:00:02Z"
event_date: 2026-05-19
run_id: 2026-05-19-2505c918
priority: high
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - identity
  - cloud
regions:
  - us
  - global
sectors:
  - public-sector
  - defense
entities: []
cves: []
sources:
  - url: "https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/"
    publisher: Krebs on Security
    role: primary
  - url: "https://gizmodo.com/the-worst-leak-that-ive-witnessed-u-s-cybersecurity-agency-leaves-its-digital-keys-out-in-public-on-github-2000760330"
    publisher: Gizmodo
    role: corroborating
closed_sources: []
evidence:
  - quote: one of the most egregious government data leaks in recent history
    publisher: Krebs on Security
  - quote: "Passwords stored in plain text in a csv, backups in git, explicit commands to disable GitHub secrets detection feature"
    publisher: Guillaume Valadon / GitGuardian via Krebs on Security
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
migrated_from: briefs/2026-05-19.md
---

A Nightwing government contractor used a public GitHub repository named "Private-CISA" as a personal sync mechanism between work and home machines, exposing highly-privileged credentials for CISA / DHS infrastructure from approximately 2025-11-13 to 2026-05-15 — about six months ([Krebs on Security, 2026-05-18](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/); [Gizmodo, 2026-05-19](https://gizmodo.com/the-worst-leak-that-ive-witnessed-u-s-cybersecurity-agency-leaves-its-digital-keys-out-in-public-on-github-2000760330)). GitGuardian researcher Guillaume Valadon surfaced the repository on 2026-05-15. Exposed material included administrative credentials for three Amazon AWS GovCloud accounts, plaintext usernames and passwords (`AWS-Workspace-Firefox-Passwords.csv`) for dozens of internal CISA systems, SSH keys and cloud tokens, and credentials to CISA's internal Artifactory code-package repository ("LZ-DSO" — Landing Zone DevSecOps). The contractor had deliberately disabled GitHub's default push-protection secret scanning. Independent researcher Philippe Caturegli (Seralys) validated AWS keys against live GovCloud accounts at high privilege and confirmed the keys remained valid for at least 48 hours after the repository was taken down. CISA acknowledged a ~one-third workforce reduction from buyouts and resignations under the Trump administration may have weakened oversight of contractor behaviour.

**Why it matters to us:** Caturegli identified the Artifactory access as the highest-impact exposure — write access to a national cybersecurity agency's build-package repo would enable backdoor insertion into anything CISA built or deployed (T1195.002 Supply Chain Compromise: Compromise Software Supply Chain). The transferable lesson for EU/CH national CERT operators is independent of US politics: contractors and integrators with write access to NCSC / BSI / ANSSI build pipelines must be subject to organisation-level GitHub push-protection that administrators cannot disable, mandatory short-lived OIDC role assumption (no long-lived AWS keys), Artifactory access-log SIEM integration with off-hours bulk-download anomaly detection, and quarterly secret-scanning sweeps of contractor personal repos under contract. T1552.001 (Credentials In Files) / T1552.004 (Private Keys).
