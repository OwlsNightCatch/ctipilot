---
schema: 1
kind: threat
title: 'WFX Phantom: stolen GitHub tokens push a CI secret stealer into repositories from 2026-11-10, steal Actions secrets, runner memory and cloud tokens, plant AWS and Azure persistence designed to outlast rotation and delete the workflow runs; StepSecurity counts more than 63,000 probe pull requests'
headline: 'WFX Phantom: stolen GitHub tokens push a CI stealer; cloud persistence meant to survive rotation; check for probe PRs'
summary: 'StepSecurity and Aikido report that from 2026-11-10 an attacker uses stolen GitHub tokens, not a GitHub Actions bug, to open probe pull requests titled "docs: dependency audit notes" and then push a stealer script into workflows, CI scripts or npm hooks where the token''s permissions allow, taking Actions secrets, runner memory and cloud credentials, planting AWS and Azure persistence and deleting the workflow runs. Counts differ by lab and time (more than 63,000 probes; at least 1,835 repositories where the payload ran); how the tokens were obtained is unknown, and no Swiss victim is named.'
discovered_at: '2026-11-13T04:04:00Z'
updated_at: null
event_date: '2026-11-10'
run_id: 2026-11-13T0256Z-intel
priority: notable
immediate_action: null
tags:
  - supply-chain
  - cloud
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - malware:wfx-phantom
  - product:github-actions
techniques:
  - T1195.002
  - T1550.001
  - T1078.004
  - T1059.004
  - T1552.001
  - T1552.005
  - T1213.003
  - T1098.001
  - T1070
affected_products:
  - GitHub Actions
cves: []
sources:
  - url: https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer
    publisher: StepSecurity
    date: '2026-11-12'
    role: primary
  - url: https://www.aikido.dev/blog/compromised-github-accounts-push-ci-secret-stealer-to-tens-of-thousands-of-repositories
    publisher: Aikido Security
    date: '2026-11-12'
    role: corroborating
  - url: https://www.endorlabs.com/learn/github-actions-supply-chain-attack-targeting-ci-secrets-at-scale
    publisher: Endor Labs
    date: '2026-11-12'
    role: corroborating
  - url: https://www.bleepingcomputer.com/news/security/hackers-compromise-4-800-github-accounts-to-steal-cloud-credentials/
    publisher: BleepingComputer
    date: '2026-11-12'
    role: corroborating
closed_sources: []
evidence:
  - quote: The attacker does not exploit a bug in GitHub Actions.
    publisher: StepSecurity
    source_url: https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer
  - quote: The pull request does nothing by itself. It tells the attacker that the token can write to the repository. If you see one, the account that opened it is compromised, even if nothing else happened.
    publisher: StepSecurity
    source_url: https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer
  - quote: The gap is the most reliable sign that the stealer ran.
    publisher: StepSecurity
    source_url: https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer
  - quote: 1,838 repos hit by v1/v2 got it again, so secrets rotated after the first wave are likely stolen again.
    publisher: Endor Labs
    source_url: https://www.endorlabs.com/learn/github-actions-supply-chain-attack-targeting-ci-secrets-at-scale
verification: multi-source
sourcing_note: StepSecurity and Aikido each hold original GitHub telemetry and Endor Labs counts infected repositories itself; their figures count different things (probe pull requests, accounts, repositories with malicious commits, repositories where the payload ran) at different times and are not comparable. StepSecurity names the campaign WFX Phantom and Aikido and BleepingComputer call it wfx-loot; the sources share the probe title, branch name, script size and start date. Aikido says forged passing status checks are active while StepSecurity found them off in all 101 copies it examined. Exfiltration indicators change between payload versions and none are carried.
confidence: high
references:
  - 2026-10-10/ghostaction-fake-audit-workflow-git-history-credential-theft
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - 'In every GitHub organisation you or your suppliers administer, search for pull requests titled "docs: dependency audit notes" and for commits titled "ci: refresh build cache", "ci: restore", "ci: cleanup", "chore: add ci helper" or "chore: add dependency audit workflow"; for each account that pushed one, revoke its tokens, rotate every secret its workflows could read and remove the AWS trust-policy changes, access keys and Azure federated credentials the stealer created, because the persistence is designed to outlast rotation.'
updates: []
migrated_from: null
---

StepSecurity reports that from 2026-11-10 an attacker uses stolen GitHub tokens of real developer and bot accounts, as a developer would, not a bug in GitHub Actions, to push a CI secret stealer into repositories those tokens can write to ([StepSecurity, 2026-11-12](https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer)). It first opens a pull request titled "docs: dependency audit notes" from a branch named wfx-docs that only proves write access; StepSecurity counts more than 63,000 such probes by 2026-11-12 ([StepSecurity, 2026-11-12](https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer)), Aikido, which tracks the campaign as wfx-loot, counts 4,837 compromised accounts and at least 1,835 repositories where the payload ran, and Endor Labs counts 8,926 infected repositories ([Aikido, 2026-11-12](https://www.aikido.dev/blog/compromised-github-accounts-push-ci-secret-stealer-to-tens-of-thousands-of-repositories); [Endor Labs, 2026-11-12](https://www.endorlabs.com/learn/github-actions-supply-chain-attack-targeting-ci-secrets-at-scale)); BleepingComputer reports that the compromised accounts included those of the US General Services Administration and the French government ([BleepingComputer, 2026-11-12](https://www.bleepingcomputer.com/news/security/hackers-compromise-4-800-github-accounts-to-steal-cloud-credentials/)).

Where the token's permissions and the repository's setup let it run, the attacker pushes a script of about 1,500 lines through an edit to an existing workflow or CI shell script, a new workflow on a short-lived branch or a hidden script that an npm hook runs, and the script collects every Actions secret, the job token, the memory of the runner worker process and credential files for the major clouds and registries, then uses the job's OIDC token to open AWS, GCP and Azure sessions ([StepSecurity, 2026-11-12](https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer)). It plants persistence meant to outlast rotation, a rewritten AWS role trust policy with new access keys and federated identity credentials on Azure applications, sends the archive over HTTP and from 2026-11-12 through a Telegram bot, and within about a minute pushes a revert commit and deletes the workflow run, leaving a gap in the run numbers that StepSecurity calls the most reliable sign the stealer ran ([StepSecurity, 2026-11-12](https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer)). How the tokens were obtained is not known: some probes came through the Fly.io GitHub App, and StepSecurity has no evidence of a breach of Fly.io ([StepSecurity, 2026-11-12](https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer)). BleepingComputer's report of Aikido's findings gives the same probe title and start date ([BleepingComputer, 2026-11-12](https://www.bleepingcomputer.com/news/security/hackers-compromise-4-800-github-accounts-to-steal-cloud-credentials/)).

**Exposure:** any account or bot with write access to repositories you own or build from whose token may be exposed (a personal access token, an OAuth grant, a GitHub App user token), and any build with cloud OIDC trust or long-lived secrets; bots that bypass branch protection raise the risk ([StepSecurity, 2026-11-12](https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer)).

**Detection:** in source-control data, pull requests titled "docs: dependency audit notes", branches named wfx-docs and commits since 2026-11-10 with the messages "ci: refresh build cache", "ci: restore", "ci: cleanup", "chore: add ci helper" or "chore: add dependency audit workflow", and in CI run history a gap in the run numbers right after one; in AWS and Azure audit logs, changes to role trust policies, newly created access keys and federated credentials named wfx-ci ([StepSecurity, 2026-11-12](https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer)).

**Triage:** a probe pull request alone shows that the account that opened it is compromised, even if nothing else happened; the payload probably ran where a commit with one of those messages is paired with a deleted run ([StepSecurity, 2026-11-12](https://www.stepsecurity.io/blog/wfx-phantom-the-github-actions-secret-stealer)).

**Defender takeaway:** treat the account behind any probe or payload commit as compromised and revoke its tokens; where the payload ran, rotation is not enough because the persistence is designed to outlast it, and Endor Labs says secrets rotated after the first wave were likely stolen again in 1,838 repositories ([Endor Labs, 2026-11-12](https://www.endorlabs.com/learn/github-actions-supply-chain-attack-targeting-ci-secrets-at-scale)).
