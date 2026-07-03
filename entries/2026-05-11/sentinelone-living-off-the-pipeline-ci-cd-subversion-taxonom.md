---
schema: 1
kind: annual-report
horizon: strategic
weekly_section: weekly-annual-reports
title: "SentinelOne — Living Off the Pipeline: CI/CD subversion taxonomy"
headline: "SentinelOne — Living Off the Pipeline: CI/CD subversion taxonomy"
summary: "SentinelOne's \"Living Off the Pipeline\" research (covered daily 2026-05-16, [SINGLE-SOURCE]) presents a three-case taxonomy of CI/CD subversion in real intrusions: TeamCity buildAgent-token theft, GitLab service-account pivot, and Contagious Interview (DPRK-aligned) build-time compromise."
discovered_at: "2026-05-11T05:00:33Z"
event_date: 2026-05-16
run_id: 2026-W20-71c96b25
priority: notable
immediate_action: null
tags:
  - supply-chain
  - identity
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:sentinelone-living-off-the-pipeline-2026"
cves: []
sources:
  - url: "https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/"
    publisher: SentinelOne Labs
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W20.md
---

SentinelOne's "Living Off the Pipeline" research (covered daily 2026-05-16, [SINGLE-SOURCE]) presents a three-case taxonomy of CI/CD subversion in real intrusions: TeamCity buildAgent-token theft, GitLab service-account pivot, and Contagious Interview (DPRK-aligned) build-time compromise. The weekly-level synthesis worth surfacing: the **three-case study generalises to a defender pattern** — CI/CD systems concentrate trust (build secrets, artifact-signing keys, deployment credentials) in machine-identity environments with weaker authentication / authorisation telemetry than human-identity environments. Combined with the Sophos NHI finding (41% of identity breaches root-caused to NHI mismanagement, above), CI/CD platforms are the highest-leverage NHI-governance attack surface for Swiss / EU public-sector DevSecOps programmes. Hunt seeds: TeamCity buildAgent re-auth events, GitLab CI job impersonation patterns, GitHub Actions OIDC-token reuse outside expected workflow scope ([daily 2026-05-16](/briefs/2026-05-16/)).
