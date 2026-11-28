---
schema: 1
kind: threat
title: "GhostAction returns: stolen maintainer credentials push a fake security-audit workflow into the victims' own GitHub repositories, which now harvests credentials from the entire git history"
headline: "GhostAction: fake security workflows now harvest whole git histories; rotating Actions secrets is not enough"
summary: >
  StepSecurity and Socket report that on 2026-10-08 the GhostAction campaign used the GitHub credentials of two open-source maintainers to
  commit a workflow disguised as a security audit straight to the default branch of 345 to 346 repositories, including one of an Uber-owned organisation, and that
  the workflow now sends the credentials found in the working tree and in the entire git history, besides the named Actions secrets, to a hardcoded address over plain HTTP.
  GitGuardian's own data puts the wave of 8 to 12 October at more than 30,000 repositories reached through about 1,900 compromised GitHub accounts, and says GitHub has
  prevented the workflow from running since 9 October. Between 13 and 21 October the operator pushed at least 72,026 further commits, mostly from accounts whose tokens were already used on 8 October,
  including a stealer disguised as a font file that a hidden VS Code task runs on developer machines, outside GitHub's workflow hold, and a cron job that survives cleaning the repository.
discovered_at: "2026-10-10T03:52:30Z"
updated_at: "2026-11-01T13:58:24Z"
event_date: "2026-10-08"
run_id: 2026-10-10T0255Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, identity]
regions: [global]
sectors: [technology]
entities: ["campaign:ghostaction", "product:github-actions"]
techniques: [T1078.004, T1552.001, T1048.003, T1053.003, T1059.007, T1552.005]
affected_products: ["GitHub Actions"]
cves: []
sources:
  - url: "https://www.stepsecurity.io/blog/ghostaction-returns"
    publisher: "StepSecurity"
    date: "2026-10-09"
    role: primary
  - url: "https://socket.dev/blog/ghostaction-cloud-credentials"
    publisher: "Socket"
    date: "2026-10-09"
    role: primary
  - url: "https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/"
    publisher: "GitGuardian"
    date: "2026-10-07"
    role: corroborating
  - url: "https://blog.gitguardian.com/ghostaction-x-polinrider/"
    publisher: "GitGuardian (October escalation)"
    date: "2026-10-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "confirms the exfiltration completed successfully: the attacker's server acknowledged receipt four seconds after the workflow started"
    publisher: "StepSecurity"
    source_url: "https://www.stepsecurity.io/blog/ghostaction-returns"
  - quote: "Nothing in an audit log looks anomalous unless the workflow content itself is inspected"
    publisher: "StepSecurity"
    source_url: "https://www.stepsecurity.io/blog/ghostaction-returns"
  - quote: "The approval gate is worth singling out: it is the single control observed stopping this campaign's exfiltration this week."
    publisher: "StepSecurity"
    source_url: "https://www.stepsecurity.io/blog/ghostaction-returns"
  - quote: "Rotating the secrets exfiltrated by the malicious workflow is not enough. The GitHub credential that allowed the injection in the first place must be found and revoked too, or someone else will use it again."
    publisher: "GitGuardian"
    source_url: "https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/"
  - quote: "In total, our dataset shows the threat actor targeted more than 30,000 repositories across 3,000 users and orgs."
    publisher: "GitGuardian"
    source_url: "https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/"
  - quote: "This resulted from compromising the GitHub accounts of about 1,900 users."
    publisher: "GitGuardian"
    source_url: "https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/"
  - quote: "However, GitHub started preventing the malicious workflow from running starting October 9."
    publisher: "GitGuardian"
    source_url: "https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/"
verification: multi-source
sourcing_note: >
  StepSecurity and Socket analysed the 2026-10-08 burst independently and GitGuardian documents the preceding wave and, in updates to the same post, the October wave;
  all three are security vendors whose claims rest on run logs, commit metadata and repository counts, and how the credentials were obtained is StepSecurity's and
  GitGuardian's assessment, not an observation. Socket's update of 2026-10-09 and GitGuardian's of 2026-10-13 both put the October wave in the tens of thousands of
  repositories from their own data; they differ on the number of accounts (more than 500 against about 1,900).
confidence: high
references:
  - 2026-10-07/gentlemen-affiliate-azazel-ci-cd-secrets-mcp-attacks
  - 2026-05-23/megalodon-mass-poisons-5-561-github-repos-in-a-6-hour-window
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Run an organisation-scoped GitHub code search in every organisation your teams and suppliers administer for workflow files under .github/workflows that present themselves as a security audit, a security check or an Actions security workflow and were added since 2026-08-31; any hit means assume breach: revoke the credential that committed it, rotate every secret found anywhere in the repository's git history, not only the configured Actions secrets, and check the crontab of every developer machine and self-hosted runner that opened or ran the repository since 2026-10-14 for a five-minute job that runs a remote script."
updates:
  - at: "2026-10-20T08:42:29Z"
    run_id: 2026-10-20T0835Z-audit
    type: update
    summary: >
      GitGuardian's update of 2026-10-13 counts more than 30,000 repositories and about 1,900 compromised
      GitHub accounts in the GhostAction wave of 8 to 12 October, far beyond the 345 to 346 repositories
      of the first analysed burst, and says GitHub has prevented the malicious workflow from running since
      9 October, so the waves of 10 and 12 October extracted no secrets.
    fields: [body, evidence, sourcing_note, summary]
  - at: "2026-11-01T13:58:24Z"
    run_id: 2026-11-01T1312Z-audit
    type: update
    summary: >
      GitGuardian counts at least 72,026 further GhostAction commits to 22,964 repositories between 13 and
      21 October from mostly the same unrevoked accounts, and new payloads that reach developer machines
      through a hidden VS Code task outside GitHub's workflow hold, query cloud metadata and AWS roles,
      and install a cron job that survives cleaning the repository.
    fields: [actions, body, sources, summary, techniques, evidence]
migrated_from: null
---

StepSecurity reports that on 2026-10-08 the GhostAction GitHub Actions credential-theft campaign used the accounts of two open-source maintainers to push a workflow disguised as a security improvement to 345 repositories, among them an Uber-owned repository that one maintainer could still write to ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)). The operator holds a maintainer's GitHub credential, which StepSecurity assesses as most plausibly a personal access token leaked through infostealer logs or credential dumps, then commits a workflow titled to look like a security audit straight to the default branch under the victim's own identity, unsigned and without a pull request; that push runs it, and nothing in an audit log looks anomalous unless the content is read ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)). GitGuardian says the technique remains at the core of the Mini Shai-Hulud malware family ([GitGuardian, 2026-10-07](https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/)).

The newer payload sends the named Actions secrets and every cloud, AI-provider and SaaS credential pattern found in the working tree and the entire git history to a hardcoded address over plain HTTP, so no DNS lookup occurs ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)). The wave was far larger than those first counts: GitGuardian counts more than 30,000 repositories between 8 and 12 October ([GitGuardian, 2026-10-07](https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/)) and, as lower bounds, a further 72,026 commits to 22,964 repositories from 1,792 accounts between 13 and 21 October, 1,382 of which had already pushed the 8 October payload, so the stolen tokens still work ([GitGuardian, 2026-10-27](https://blog.gitguardian.com/ghostaction-x-polinrider/)).

**Exposure:** any GitHub account whose token or session credential has leaked, every repository it can write to, and since 14 October any developer machine that opened such a repository in VS Code with the workspace trusted ([GitGuardian, 2026-10-27](https://blog.gitguardian.com/ghostaction-x-polinrider/)); StepSecurity says a workflow posing as a security audit or an Actions security workflow that appeared in a repository you maintain since 2026-08-31 means treat it as a confirmed breach ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)).

**Detection:** source-control audit logs: workflow files added straight to default branches without a pull request by a maintainer identity, unsigned commits landing in many repositories within minutes; an organisation-scoped code search with StepSecurity's published content-marker queries for security-themed workflow files; runner egress logs: an HTTP POST to a bare IP address with no preceding DNS lookup ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)). Removing the workflow does not undo the theft: StepSecurity says any secret ever committed to a repository must be treated as compromised, so treat each run as an exfiltration, scan the full history and rotate every credential found ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)); GitGuardian adds that the GitHub credential that allowed the injection must be revoked too ([GitGuardian, 2026-10-07](https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/)), and that on developer machines and self-hosted runners a crontab entry fetching and running a script from the operator's server every five minutes survives cleaning the repository ([GitGuardian, 2026-10-27](https://blog.gitguardian.com/ghostaction-x-polinrider/)).

**Triage:** the audit-log pattern separates this from a team adding a scanning workflow: no pull request, unsigned commits across many repositories, and a manual dispatch right after creation ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)).

**Defender takeaway:** search the GitHub organisations your teams and suppliers administer for security-themed workflow files and for hidden editor tasks that run on folder open; on a hit revoke the committing credential, rotate everything in the repository's full history and check the crontab of every machine that opened or ran it. StepSecurity saw requiring approval for workflow runs stop the exfiltration and names branch protection on .github/workflows so workflow changes need pull-request review ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)).

## Update — 2026-10-20T08:42:29Z

GitGuardian updated its analysis on 2026-10-13 from its own dataset: between 8 and 12 October the campaign targeted more than 30,000 repositories across 3,000 users and organisations by compromising the GitHub accounts of about 1,900 users, and tried to extract 3,174 secrets from public repositories' CI, with the largest spike on 8 and 9 October ([GitGuardian, 2026-10-07](https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/)). Socket's update of 9 October, with more than 500 accounts and tens of thousands of repositories since 7 October, is of the same order ([Socket, 2026-10-09](https://socket.dev/blog/ghostaction-cloud-credentials)). GitGuardian says GitHub started preventing the malicious workflow from running on 9 October, so the further waves it saw on 10 and 12 October, with the same payload, could not extract any secrets ([GitGuardian, 2026-10-07](https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/)); a workflow from those later waves still means the account that committed it is compromised. Part of the October victims had already been hit in the September 2025 and August 2026 waves, and GitGuardian assesses that the operator likely relies in part on secrets left unrotated since earlier campaigns ([GitGuardian, 2026-10-07](https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/)).

## Update — 2026-11-01T13:58:24Z

GitGuardian's analysis of 2026-10-27 counts, as lower bounds from its own feed, 72,026 commits from the operator to 22,964 public repositories between 13 and 21 October, 7,989 of them new victims, pushed by 1,792 accounts of which 1,382 had already pushed the 8 October payload: the tokens stolen earlier were never revoked ([GitGuardian, 2026-10-27](https://blog.gitguardian.com/ghostaction-x-polinrider/)). The campaign now ships five payload families and reaches beyond GitHub-hosted runners. One family is a Node.js stealer disguised as a font file and launched by a hidden VS Code task that runs when a developer opens the folder and trusts the workspace; it reads cloud, package-registry, Git, Kubernetes and AI-tool credential files, SSH keys and token-bearing environment variables, and since no workflow is involved, GitHub's workflow hold does not stop it. Self-hosted-runner workflows query the cloud instance metadata service for role credentials, and the revived 2025 workflow requests a GitHub OIDC token and tries to assume every AWS IAM role found in the environment ([GitGuardian, 2026-10-27](https://blog.gitguardian.com/ghostaction-x-polinrider/)). Three families install a cron job that fetches and runs a script from the operator's server every five minutes, so a developer laptop or runner that ran one stays under control after the repository is cleaned. GitGuardian found no successful run of the workflow payloads, which GitHub's hold caught ([GitGuardian, 2026-10-27](https://blog.gitguardian.com/ghostaction-x-polinrider/)). Between 22 and 26 October, loaders of a separate campaign, PolinRider, were added to GhostAction commits and force-pushed; GitGuardian sees no clear link between the two operators ([GitGuardian, 2026-10-27](https://blog.gitguardian.com/ghostaction-x-polinrider/)). It warns against reverting the attacker's "Update" commits, which restores the previous malicious version, and has seen re-infection where tokens were kept after a clean-up ([GitGuardian, 2026-10-27](https://blog.gitguardian.com/ghostaction-x-polinrider/)).
