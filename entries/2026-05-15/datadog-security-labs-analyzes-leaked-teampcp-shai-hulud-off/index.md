---
schema: 1
kind: threat
title: "Datadog analyses TeamPCP's open-sourced Shai-Hulud framework: credential and runner-memory theft, IDE and Claude Code hook persistence, OIDC npm publishing and a wipe-on-revocation daemon"
headline: "TeamPCP open-sourced its Shai-Hulud framework; Datadog maps its theft, persistence and npm-poisoning code"
summary: "On 2026-05-12 a GitHub repository signed \"Love - TeamPCP\" published what Datadog Security Labs assesses as the complete source of the Shai-Hulud offensive framework; GitHub removed it soon after, but not before it was forked. Datadog's static analysis of 2026-05-13 finds a TypeScript and Bun toolkit that harvests more than 100 credential file paths, cloud, Kubernetes and Vault secrets and GitHub Actions runner memory, poisons repositories with VS Code and Claude Code hooks and npm packages with stolen tokens or a workflow's OIDC token, exits on Russian-locale systems, and installs a daemon that deletes the home directory when a stolen GitHub token is revoked."
discovered_at: "2026-05-15T05:00:10Z"
event_date: 2026-05-12
run_id: 2026-05-15-58b94fbd
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - wiper
  - organized-crime
regions:
  - global
sectors:
  - technology
entities:
  - "actor:teampcp"
  - "tool:datadog-shai-hulud-framework-2026-05"
  - "campaign:mini-shai-hulud"
techniques: [T1195.002, T1059.004, T1059.007, T1003.007, T1552.001, T1552.005, T1552.007, T1528, T1550.001, T1546, T1543.001, T1543.002, T1027, T1614.001, T1041, T1102.001, T1567.001, T1485]
affected_products: []
cves: []
sources:
  - url: "https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/"
    publisher: "Datadog Security Labs"
    date: "2026-05-13"
    role: primary
closed_sources: []
evidence:
  - quote: "The repository's README explicitly states: \"Love - TeamPCP\" and \"Change keys and C2 as needed.\""
    publisher: Datadog Security Labs
    source_url: "https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/"
  - quote: "This appears to have been removed by GitHub shortly after publishing, though not in time to prevent multiple forks."
    publisher: Datadog Security Labs
    source_url: "https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/"
  - quote: "the framework installs a daemon (`gh-token-monitor`) that runs `rm -rf ~/` if your token is revoked. Disable it first, then rotate credentials."
    publisher: Datadog Security Labs
    source_url: "https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/"
verification: single-source
sourcing_note: "Datadog Security Labs is the only source: its static analysis of the released code, which it maps to payloads other researchers analysed in the wild."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-15.md
updated_at: null
updates:
  - at: "2026-10-21T20:34:33Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      The repository that published the Shai-Hulud framework source is signed "Love - TeamPCP", and GitHub
      removed it after it had been forked. Datadog's analysis finds no pull_request_target or
      expression-injection exploitation in the code: the framework harvests credentials where it already
      runs, reads Runner.Worker memory, poisons repositories and npm packages with stolen tokens, and uses
      a workflow's OIDC token only in a release workflow it was hardcoded to target. Datadog's compromise
      checks include disabling the wipe-on-revocation daemon before rotating tokens.
    fields: [affected_products, body, classification, entities, event_date, evidence, headline, sources, sourcing_note, summary, tags, techniques, title]
---

On 2026-05-12 a GitHub repository appeared with what Datadog Security Labs assesses as the complete source code of the Shai-Hulud offensive framework attributed to TeamPCP; its README reads "Love - TeamPCP" and "Change keys and C2 as needed", its commits are authored as TeamPCP_OSS, and GitHub removed it shortly after publication, though not before it was forked several times ([Datadog Security Labs, 2026-05-13](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)). Datadog maps the source directly to compiled payloads seen in the wild, including those of the TanStack and UiPath compromises, and finds 19 of the 22 TeamPCP techniques described in earlier reporting implemented in it ([Datadog Security Labs, 2026-05-13](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)).

The modular TypeScript and Bun toolkit exits on systems with a Russian locale, then reads OS-specific lists of more than 100 sensitive file paths, runs `gh auth token` and captures the process environment, and in GitHub Actions on Linux feeds a script to `sudo python3` that reads the Runner.Worker process memory for values marked secret; further providers walk the AWS credential chain including instance and container metadata, read every Kubernetes secret in every namespace and enumerate Vault ([Datadog Security Labs, 2026-05-13](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)). Data leaves AES-256-GCM encrypted over HTTPS to a campaign domain, with a fallback domain found through signed GitHub commits and, failing that, new public GitHub repositories used as dead-drops ([Datadog Security Labs, 2026-05-13](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)). Stolen GitHub tokens are used to commit VS Code folder-open tasks and Claude Code SessionStart hooks to every branch of the victim's repositories, stolen npm tokens to republish the victim's packages with a `preinstall` loader, and, in a release workflow it was hardcoded to target, the workflow's OIDC token to publish a poisoned package with genuine Sigstore provenance; where it attaches a stolen token it installs a LaunchAgent or systemd user service that checks the token every minute and runs `rm -rf ~/` once it is revoked ([Datadog Security Labs, 2026-05-13](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)).

**Exposure:** CI/CD pipelines, developer workstations and cloud environments open to the documented techniques, in particular Runner.Worker memory extraction, instance and container metadata collection and IDE hook persistence; with the code public, other actors can reuse the playbook ([Datadog Security Labs, 2026-05-13](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)).

**Detection:** on hosts, a `gh-token-monitor` LaunchAgent or systemd user service, and Claude Code `SessionStart` hooks or VS Code `folderOpen` tasks that run a `setup.mjs` loader; in repositories, commits on any branch under a spoofed `claude` identity that add these hook and loader files; under stolen tokens, new public repositories with Dune-themed names; in npm, unexpected patch releases of your packages that add a `preinstall` script; in GitHub Actions, a disguised workflow that dumps the repository's secrets, followed by deleted workflow runs and branches ([Datadog Security Labs, 2026-05-13](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)).

**Defender takeaway:** before revoking any GitHub token on a suspect host, disable the token-monitoring daemon, then rotate credentials; yank any package version that gained an unexpected `preinstall` script ([Datadog Security Labs, 2026-05-13](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)).

## Correction — 2026-10-21T20:34:33Z

The published repository's README reads "Love - TeamPCP" and "Change keys and C2 as needed", its commits are authored as TeamPCP_OSS, and GitHub removed the repository shortly after publication, though not before it was forked, so the code remains available to other actors ([Datadog Security Labs, 2026-05-13](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)). Datadog's analysis describes no pull-request exploitation, `pull_request_target` targeting or expression-injection capability in the code. The framework harvests credentials where it already runs, reads Runner.Worker memory, poisons repository branches and npm packages with stolen tokens, and uses a workflow's own OIDC token only inside a release workflow and for a package it was hardcoded to target, so that path was manually targeted while the token-driven spread is opportunistic ([Datadog Security Labs, 2026-05-13](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)).

The analysis also documents what defenders need for a compromise check: an exit on Russian-locale systems, a daemon that deletes the home directory when a stolen GitHub token is revoked and must be disabled before rotation, and the hook files, commits and npm releases it leaves behind ([Datadog Security Labs, 2026-05-13](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)).
