---
schema: 1
kind: threat
title: "actions-cool/issues-helper GitHub Action compromised in Mini Shai-Hulud: 53 tags moved to imposter commits that read Runner.Worker memory, re-enabled in September with the tags intact"
headline: "The compromised actions-cool GitHub Actions were re-enabled in September with malicious tags and ran the payload again"
summary: "On 2026-05-18 all 53 version tags of the actions-cool/issues-helper GitHub Action, and all 15 of actions-cool/maintain-one-comment, were moved to imposter commits whose payload reads the Runner.Worker process memory for decrypted workflow secrets and sends them over HTTPS to an attacker-controlled domain (StepSecurity); Socket places the compromise in the Mini Shai-Hulud campaign. GitHub disabled both repositories on 2026-05-19 but they became reachable again on 2026-09-16 with the malicious tags intact, so tag-referencing workflows ran the payload again and SafeDep counted six newly infected repositories by 2026-09-24, until GitHub disabled both again by 2026-09-25 (Socket, The Hacker News). Only workflows pinned to a full commit SHA from before 2026-05-18 were unaffected."
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
techniques: [T1195.002, T1105, T1059.006, T1003.007, T1041, T1204.002]
cves: []
sources:
  - url: "https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials"
    publisher: "StepSecurity"
    date: "2026-05-18"
    role: primary
  - url: "https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html"
    publisher: "The Hacker News"
    date: "2026-05-19"
    role: corroborating
  - url: "https://cybersecuritynews.com/compromised-github-action-exfiltrates-workflow-credentials/"
    publisher: "CybersecurityNews"
    date: "2026-05-19"
    role: corroborating
  - url: "https://socket.dev/blog/mini-shai-hulud-actions"
    publisher: "Socket"
    date: "2026-09-24"
    role: corroborating
  - url: "https://thehackernews.com/2026/09/compromised-github-actions-came-back.html"
    publisher: "The Hacker News"
    date: "2026-09-25"
    role: corroborating
closed_sources: []
evidence:
  - quote: "GitHub security team disabled both repositories on May 19, 2026, one day after the malicious content was introduced."
    publisher: Socket
    source_url: "https://socket.dev/blog/mini-shai-hulud-actions"
  - quote: "On September 16, 2026, both repositories became accessible again. Their release tags were not cleaned up first."
    publisher: Socket
    source_url: "https://socket.dev/blog/mini-shai-hulud-actions"
  - quote: "have been disabled on GitHub again, so workflows referencing them now fail at job setup instead of running the payload."
    publisher: Socket
    source_url: "https://socket.dev/blog/mini-shai-hulud-actions"
  - quote: "The payload steals the CI secrets. Then it commits Claude Code and VS Code hooks into the repository."
    publisher: The Hacker News (quoting SafeDep)
    source_url: "https://thehackernews.com/2026/09/compromised-github-actions-came-back.html"
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
actions:
  - "Find every workflow in your GitHub organisations that references actions-cool/issues-helper or actions-cool/maintain-one-comment by tag; where either ran successfully on 2026-05-18 to 05-19 or 2026-09-16 to 09-25, rotate every secret that workflow could read and check the repository's commits since 2026-09-16 for added Claude Code or VS Code hook files, then remove the action or pin it to a full commit SHA from before 2026-05-18."
migrated_from: briefs/2026-05-20.md
updated_at: "2026-10-20T08:49:45Z"
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
  - at: "2026-10-20T08:49:45Z"
    run_id: 2026-10-20T0835Z-audit
    type: update
    summary: >
      Both compromised actions-cool GitHub Actions became reachable again on 2026-09-16 with their
      malicious tags intact, so workflows referencing them by tag ran the payload again; SafeDep found six
      more infected repositories by 2026-09-24, with the payload now also planting Claude Code and VS Code
      hooks, and GitHub disabled both again by 2026-09-25. GitHub had disabled both repositories, not only
      maintain-one-comment, on 2026-05-19.
    fields: [actions, body, evidence, headline, sources, summary, techniques, title]
---

StepSecurity disclosed on 2026-05-18 that every existing tag of the `actions-cool/issues-helper` GitHub Action, 53 in total, had been moved to its own imposter commit that is not reachable from the action's default branch, and that all 15 tags of the companion `actions-cool/maintain-one-comment` action were moved the same way ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)). The payload downloads the Bun JavaScript runtime to the runner, then a `python3` child process reads the memory of the Runner.Worker process, which holds the workflow's decrypted secrets, filters the captured bytes for values flagged as secret and sends them over HTTPS to an attacker-controlled domain ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)). The 53 imposter commits carry fake "Build action for vX.Y.Z" messages in the maintainer's style and were all created within 3 minutes 16 seconds on 2026-05-18 ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)). Socket's head of threat intelligence told The Hacker News that the @antv npm compromise in the Mini Shai-Hulud campaign is likely linked to the actions-cool hack because the two share an exfiltration domain, and that "the overlap is strong enough that we're treating them as related" ([The Hacker News, 2026-05-19](https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html)). GitHub's security team disabled both repositories on 2026-05-19 but left the malicious tags in place; both became reachable again on 2026-09-16, so every workflow referencing either action by tag ran the payload again until GitHub disabled them a second time by 2026-09-25 ([Socket, 2026-09-24](https://socket.dev/blog/mini-shai-hulud-actions)). SafeDep found six more repositories infected through issues-helper between 2026-09-20 and 09-24, with the payload also committing Claude Code and VS Code hooks that run on a developer's machine when the project is opened ([The Hacker News, 2026-09-25](https://thehackernews.com/2026/09/compromised-github-actions-came-back.html)).

**Exposure:** any workflow that referenced either action by a version tag pulled the malicious code on its next run after the tags moved; "Only workflows pinned to a known-good full commit SHA are unaffected" ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)). That happened on 2026-05-18 to 05-19 and again from 2026-09-16 until the second disable by 2026-09-25, and for issues-helper alone GitHub's dependency graph lists about 15,000 dependent repositories ([Socket, 2026-09-24](https://socket.dev/blog/mini-shai-hulud-actions)).

**Detection:** on the runner, the Bun runtime appearing under `/home/runner/.bun/bin/bun`, a `python3` child process reading `/proc/<Runner.Worker PID>/mem`, `gh auth token` and `sudo python3` executions, `tr` and `grep` pipelines filtering for secret-flagged values, and an outbound HTTPS connection to a domain outside the workflow's normal destinations ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)). In workflow definitions, an action reference that resolves to a commit matching no legitimate tag or branch head of the action's repository is the signature of this attack ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)). In workflow run history, runs of either action that start succeeding after a stretch of job-setup failures, or whose duration jumps from seconds to minutes, with runner logs showing Bun being set up for the action ([Socket, 2026-09-24](https://socket.dev/blog/mini-shai-hulud-actions)); in repository history, commits from 2026-09-16 onward that nobody can account for ([Socket, 2026-09-24](https://socket.dev/blog/mini-shai-hulud-actions)), in particular added Claude Code or VS Code hook configuration ([The Hacker News, 2026-09-25](https://thehackernews.com/2026/09/compromised-github-actions-came-back.html)).

**Triage:** an issue-housekeeping action has no reason to install a separate JavaScript runtime or run a multi-minute script; a scheduled workflow that switches from failing in seconds to running for minutes without any change to its own code means the tagged action became downloadable again ([Socket, 2026-09-24](https://socket.dev/blog/mini-shai-hulud-actions)).

**Defender takeaway:** treat any workflow run that used either action by tag on 2026-05-18 to 05-19 or from 2026-09-16 to 09-25 as a secrets exposure: rotate every secret the workflow could read, review what its GitHub token was allowed to do, audit the repository for commits from 2026-09-16 onward, and remove the actions or pin them to a full commit SHA verified to predate 2026-05-18 ([Socket, 2026-09-24](https://socket.dev/blog/mini-shai-hulud-actions)). Disabling a repository leaves its tags untouched, so a later re-enable reactivates the compromise without any change to your own workflow file; SHA pinning removes that dependency ([Socket, 2026-09-24](https://socket.dev/blog/mini-shai-hulud-actions)). Runner egress control is the layer that still holds when a compromised action runs: StepSecurity added the exfiltration domain to Harden-Runner's global block list, which blocks outbound connections to it even in audit mode, so that "even if a compromised action somehow runs, the credentials cannot leave the runner" ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/actions-cool-issues-helper-github-action-compromised-all-tags-point-to-imposter-commit-that-exfiltrates-ci-cd-credentials)).

## Correction — 2026-09-30T06:54:45Z

The Hacker News reports that GitHub disabled access to the companion maintain-one-comment repository, and Socket described the link to the Mini Shai-Hulud npm campaign as likely, based on the shared exfiltration domain, rather than confirmed; no cited source ties it to PyPI ([The Hacker News, 2026-05-19](https://thehackernews.com/2026/05/github-actions-supply-chain-attack.html)). The Nx Console extension compromise named in the earlier summary is a separate incident, and no cited source says EU or Swiss organisations were affected.

## Update — 2026-10-20T08:49:45Z

Socket reported on 2026-09-24 that GitHub's security team had disabled both actions-cool/issues-helper and actions-cool/maintain-one-comment on 2026-05-19, not only maintain-one-comment, and that both became reachable again on 2026-09-16, between 09:09 and 16:16 UTC, with every release tag still pointing at the content introduced on 2026-05-18, so any workflow referencing either action by tag ran the payload again on its next run; Socket could not determine why they were re-enabled ([Socket, 2026-09-24](https://socket.dev/blog/mini-shai-hulud-actions)). Socket places the compromise in the May 2026 Mini Shai-Hulud campaign and notes that GitHub's dependency graph lists about 15,000 dependent repositories for issues-helper alone ([Socket, 2026-09-24](https://socket.dev/blog/mini-shai-hulud-actions)). SafeDep found six more repositories infected through issues-helper between 2026-09-20 and 09-24, and says the payload steals the CI secrets and then commits Claude Code and VS Code hooks into the repository, which run the malware on the machine of a developer who pulls the change and opens the project ([The Hacker News, 2026-09-25](https://thehackernews.com/2026/09/compromised-github-actions-came-back.html)). GitHub disabled both repositories again by 2026-09-25, so referencing workflows now fail at job setup ([Socket, 2026-09-24](https://socket.dev/blog/mini-shai-hulud-actions); [The Hacker News, 2026-09-25](https://thehackernews.com/2026/09/compromised-github-actions-came-back.html)).
