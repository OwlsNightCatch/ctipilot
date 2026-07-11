---
schema: 1
kind: threat
horizon: operational
title: "Megalodon mass-poisons 5,561 GitHub repos in a 6-hour window; SysDiag + Optimize-Build workflows exfiltrate cloud credentials and OIDC tokens"
headline: "Megalodon mass-poisons 5,561 GitHub repos in a 6-hour window; SysDiag + Optimize-Build workflows exfiltrate cloud credentials and OIDC tokens"
summary: "Megalodon automated-poisoned 5,561 GitHub repos on 2026-05-18. Automated commits inject SysDiag and Optimize-Build GitHub Actions workflows that exfiltrate AWS/GCP/Azure credentials, OIDC tokens and SSH keys from CI runners; the @tiledesk/tiledesk-server npm package 2.18.6–2.18.12 carries the dormant Optimize-Build variant (SafeDep, 2026-05-21 · OX Security, 2026-05-21)."
discovered_at: "2026-05-23T05:00:02Z"
event_date: 2026-05-22
run_id: 2026-05-23-852c21c8
priority: high
immediate_action: null
tags:
  - supply-chain
  - identity
  - cloud
  - organized-crime
regions:
  - global
sectors:
  - technology
  - public-sector
  - education
entities:
  - "campaign:megalodon-mass-github-cicd-backdoor-5561-repos-sysdiag-optimize-build"
cves: []
sources:
  - url: "https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows/"
    publisher: SafeDep technical analysis
    role: primary
  - url: "https://www.ox.security/blog/megalodon-cicd-malware-github/"
    publisher: OX Security
    role: corroborating
  - url: "https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html"
    publisher: The Hacker News
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
migrated_from: briefs/2026-05-23.md
---

SafeDep and OX Security disclosed an automated mass-backdooring campaign tracked as **Megalodon** that pushed thousands of malicious commits to 5,561 distinct GitHub repositories in a roughly six-hour window on 2026-05-18, using throwaway accounts with forged committer identities such as `build-bot`, `auto-ci`, `ci-bot` and `pipeline-bot` ([SafeDep, 2026-05-21](https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows/) · [OX Security, 2026-05-21](https://www.ox.security/blog/megalodon-cicd-malware-github/) · [The Hacker News, 2026-05-22](https://thehackernews.com/2026/05/megalodon-github-attack-targets-5561.html)). Two GitHub Actions YAML variants were injected: **SysDiag**, triggered on every `push` and `pull_request` event (T1059.004 Unix Shell via CI Runner) to maximise execution frequency in active repos, and **Optimize-Build**, which replaces existing workflows with `workflow_dispatch` triggers — a dormant backdoor that the attacker can activate on demand via the GitHub REST API (T1546 Event Triggered Execution). Both variants carry a base64-encoded bash payload that the SafeDep and OX Security write-ups disassemble in detail.

On execution the payload harvests CI environment variables, `/proc/*/environ` entries, AWS credentials across configured profiles and IMDSv2 metadata, GCP access tokens via `gcloud auth print-access-token`, Azure IMDS tokens, SSH private keys from `~/.ssh/`, Docker config files, `.npmrc`, `.netrc`, Kubernetes configs, Vault tokens, Terraform credentials and — critically for CI/CD trust chains — GitHub Actions OIDC tokens (T1552.004 Private Keys; T1078.004 Cloud Accounts). The npm package `@tiledesk/tiledesk-server` versions 2.18.6–2.18.12 carries the `Optimize-Build` variant after the maintainer's GitHub repo was compromised; SafeDep's Malysis engine flagged the package. Detection vantage: audit every `.github/workflows/*.yml` for the SafeDep-published payload markers and unfamiliar committer identities on recent commits; review CI runner process trees for `aws configure list-profiles`, `gcloud auth print-access-token` and `curl http://169.254.169.254` calls outside expected infra tests. Hardening: require approval for `workflow_dispatch` on untrusted branches, gate `.github/workflows/` changes behind CODEOWNERS review, adopt OIDC-based trusted publishing to eliminate long-lived cloud credentials, and pin third-party actions to commit SHAs not branch tags.

**Why it matters to us:** any EU/CH agency, university or contractor with CI/CD reaching cloud infrastructure is exposed if a maintainer they depend on was caught in the 6-hour sweep — re-audit GitHub Actions workflows on internal forks today, and rotate any cloud credentials previously surfaced via CI runners on the affected window.
