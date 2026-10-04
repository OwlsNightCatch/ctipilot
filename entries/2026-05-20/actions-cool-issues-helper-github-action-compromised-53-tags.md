---
schema: 1
kind: threat
title: "actions-cool/issues-helper GitHub Action compromised: 53 tags moved to imposter commits that read Runner.Worker memory, likely linked to Mini Shai-Hulud"
headline: "All 53 tags of the actions-cool/issues-helper GitHub Action were moved to imposter commits that steal runner secrets"
summary: "On 2026-05-18 all 53 version tags of the actions-cool/issues-helper GitHub Action, and all 15 of actions-cool/maintain-one-comment, were moved to imposter commits whose payload reads the Runner.Worker process memory for decrypted workflow secrets and sends them over HTTPS to an attacker-controlled domain (StepSecurity). Socket links the exfiltration domain to the Mini Shai-Hulud npm campaign; only workflows pinned to a full commit SHA were unaffected."
discovered_at: "2026-05-20T05:00:03Z"
event_date: 2026-05-18
run_id: 2026-05-20-a0f7b07f
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - cloud
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "incident:actions-cool-issues-helper-github-action-compromised-53-tag"
  - "campaign:mini-shai-hulud"
techniques: [T1195.002, T1105, T1059.006, T1003.007, T1041]
cves: []
sources:
  - url: "https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials"
    publisher: "StepSecurity, 2026-05-18"
    role: primary
  - url: "https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html"
    publisher: "The Hacker News, 2026-05-19"
    role: corroborating
  - url: "https://cybersecuritynews.com/compromised-github-action-exfiltrates-workflow-credentials/"
    publisher: "CybersecurityNews, 2026-05-19"
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
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-20.md
updates:
  - at: "2026-09-30T06:54:45Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Corrected against StepSecurity and The Hacker News. GitHub disabled the companion
      maintain-one-comment repository, not issues-helper, and Socket called the Mini Shai-Hulud link
      likely, for npm only. The Nx Console figures, an unsourced EU and Swiss scope claim, an
      unsupported credentials-in-files technique, an attacker domain and a commit hash are removed.
      Exposure, detection and takeaway lines follow StepSecurity, the event date is StepSecurity's
      2026-05-18, and a source rating is added.
    fields: [body, classification, techniques, title, headline, summary, event_date]
---

StepSecurity disclosed on 2026-05-18 that every existing tag of the `actions-cool/issues-helper` GitHub Action, 53 in total, had been moved to its own imposter commit that is not reachable from the action's default branch, and that all 15 tags of the companion `actions-cool/maintain-one-comment` action were moved the same way ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)). The payload downloads the Bun JavaScript runtime to the runner, then a `python3` child process reads the memory of the Runner.Worker process, which holds the workflow's decrypted secrets, filters the captured bytes for values flagged as secret and sends them over HTTPS to an attacker-controlled domain ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)). The 53 imposter commits carry fake "Build action for vX.Y.Z" messages in the maintainer's style and were all created within 3 minutes 16 seconds on 2026-05-18 ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)). Socket's head of threat intelligence told The Hacker News that the @antv npm compromise in the Mini Shai-Hulud campaign is likely linked to the actions-cool hack because the two share an exfiltration domain, and that "the overlap is strong enough that we're treating them as related"; GitHub has since disabled access to the maintain-one-comment repository for a terms-of-service violation ([The Hacker News, 2026-05-19](https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html)).

**Exposure:** any workflow that referenced either action by a version tag pulled the malicious code on its next run after the tags moved; "Only workflows pinned to a known-good full commit SHA are unaffected" ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)).

**Detection:** on the runner, the Bun runtime appearing under `/home/runner/.bun/bin/bun`, a `python3` child process reading `/proc/<Runner.Worker PID>/mem`, `gh auth token` and `sudo python3` executions, `tr` and `grep` pipelines filtering for secret-flagged values, and an outbound HTTPS connection to a domain outside the workflow's normal destinations ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)). In workflow definitions, an action reference that resolves to a commit matching no legitimate tag or branch head of the action's repository is the signature of this attack ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)).

**Defender takeaway:** treat any workflow run that used either action by tag on or after 2026-05-18 as a secrets exposure: rotate every secret the workflow could read, including its GitHub token, and pin third-party actions to full commit SHAs. Runner egress control is the layer that still holds when a compromised action runs: StepSecurity added the exfiltration domain to Harden-Runner's global block list, which blocks outbound connections to it even in audit mode, so that "even if a compromised action somehow runs, the credentials cannot leave the runner" ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)).

## Correction — 2026-09-30T06:54:45Z

The Hacker News reports that GitHub disabled access to the companion maintain-one-comment repository, and Socket described the link to the Mini Shai-Hulud npm campaign as likely, based on the shared exfiltration domain, rather than confirmed; no cited source ties it to PyPI ([The Hacker News, 2026-05-19](https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html)). The Nx Console extension compromise named in the earlier summary is a separate incident, and no cited source says EU or Swiss organisations were affected.
