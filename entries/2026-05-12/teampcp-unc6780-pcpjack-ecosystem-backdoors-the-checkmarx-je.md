---
schema: 1
kind: vulnerability
horizon: operational
title: "TeamPCP (UNC6780 / PCPJack ecosystem) backdoors the Checkmarx Jenkins AST plugin — third Checkmarx supply-chain compromise in three months, SANDCLOCK exfiltrates every CI secret reachable from the runner"
headline: "TeamPCP (UNC6780 / PCPJack ecosystem) backdoors the Checkmarx Jenkins AST plugin — third Checkmarx supply-chain compromise in three months, SANDCLOCK"
summary: "TeamPCP (UNC6780) backdoors the Checkmarx Jenkins AST plugin — third Checkmarx supply-chain compromise in three months. Malicious plugin build 2026.5.09 published to the Jenkins Marketplace on 2026-05-09–10 deploys SANDCLOCK to exfiltrate every CI secret reachable from the runner (cloud keys, container-registry credentials, Checkmarx API tokens) (The Hacker News, 2026-05-11; Checkmarx — Ongoing Security Updates, last update 2026-05-09). Treat any pipeline that auto-updated in the window as a full secrets-compromise event."
discovered_at: "2026-05-12T05:00:06Z"
event_date: 2026-05-11
run_id: 2026-05-12-cd1ab844
priority: high
immediate_action: null
tags:
  - supply-chain
  - vulnerabilities
  - organized-crime
  - cloud
  - ai-abuse
regions:
  - global
  - europe
sectors:
  - technology
entities:
  - "tool:pcpjack-cloud-worm-2026"
  - "actor:teampcp"
cves:
  - id: CVE-2026-33634
    cvss: "9.4"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - patch-available
sources:
  - url: "https://thehackernews.com/2026/05/teampcp-compromises-checkmarx-jenkins.html"
    publisher: "The Hacker News, 2026-05-11"
    role: primary
  - url: "https://www.securityweek.com/checkmarx-jenkins-ast-plugin-compromised-in-supply-chain-attack/"
    publisher: "SecurityWeek, 2026-05-11"
    role: corroborating
  - url: "https://checkmarx.com/blog/ongoing-security-updates/"
    publisher: "Checkmarx — Ongoing Security Updates, 2026-05-09"
    role: corroborating
closed_sources: []
evidence:
  - quote: "UPDATE (TeamPCP / mini-shai-hulud first covered 2026-05-07; PCPJack worm covered 2026-05-10; this is a distinct new artefact in the same actor ecosystem): On 2026-05-09–10 (UTC) TeamPCP (UNC6780) published a backdoored build of the Checkmarx Jenkins AST plugin (version 2026.5.09, marketed under the …"
    publisher: ctipilot v2 brief (migrated)
verification: multi-source
sourcing_note: "migration: evidence backfilled from v2 brief body (item predates the Evidence footer field); migration: update target unresolved (no originally-covered date in v2 body)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-12.md
---

**UPDATE (TeamPCP / mini-shai-hulud first covered 2026-05-07; PCPJack worm covered 2026-05-10; this is a distinct new artefact in the same actor ecosystem):** On 2026-05-09–10 (UTC) TeamPCP (UNC6780) published a backdoored build of the Checkmarx Jenkins AST plugin (version `2026.5.09`, marketed under the actor's signature naming "Checkmarx-Fully-Hacked-by-TeamPCP") to the Jenkins Marketplace. Any Jenkins instance configured to auto-update the AST plugin during that window pulled the malicious build and executed the **SANDCLOCK** credential stealer in the runner context ([Checkmarx — Ongoing Security Updates, last updated 2026-05-09](https://checkmarx.com/blog/ongoing-security-updates/); [The Hacker News, 2026-05-11](https://thehackernews.com/2026/05/teampcp-compromises-checkmarx-jenkins.html); [SecurityWeek, 2026-05-11](https://www.securityweek.com/checkmarx-jenkins-ast-plugin-compromised-in-supply-chain-attack/)).

SANDCLOCK targets every secret reachable from a typical CI/CD pipeline environment: GitHub Personal Access Tokens, AWS / Azure / GCP credentials, Kubernetes service-account tokens, Docker / OCI registry credentials, SSH keys, and Checkmarx One API tokens. Affected pipelines should be treated as **full secrets-compromise** events: every credential the runner could read must be rotated and any artefact built or deployed in the window audited. Checkmarx's [ongoing-security-updates page](https://checkmarx.com/blog/ongoing-security-updates/) specifies plugin version `2.0.13-829.vc72453fa_1c16` (published December 2025) as the safe pinned version; a CVE has been issued as CVE-2026-33634 per the Checkmarx advisory. This is the **third** Checkmarx-product supply-chain compromise by this actor in three months, after the March 2026 KICS Docker image and the April 2026 VS Code extension defacement — the cadence and the actor's naming convention indicate persistent targeting of the Checkmarx product line specifically, not opportunistic distribution-channel abuse.

Mapped to [T1195.002 Compromise Software Supply Chain](https://attack.mitre.org/techniques/T1195/002/) and [T1552.001 Credentials In Files](https://attack.mitre.org/techniques/T1552/001/). The GTIG AI Threat Tracker ( attributes SANDCLOCK specifically to TeamPCP and flags the stealer as explicitly designed to harvest **LLM API keys** in addition to traditional cloud credentials — consistent with the actor's pivot to monetising stolen LLM access. Defender pivot: inventory every Jenkins plugin auto-update enabled across CI/CD estates; constrain runners to short-lived OIDC-federated credentials (no long-lived PATs in runner env) where the platform supports it; audit Checkmarx One API logs for unexpected source IPs since 2026-05-09.
