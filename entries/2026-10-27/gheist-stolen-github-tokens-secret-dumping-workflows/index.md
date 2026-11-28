---
schema: 1
kind: threat
title: "Gheist: stolen GitHub tokens plant a secret-dumping workflow in every repository they reach; GitHub's July approval hold stops it on public github.com repositories but not on private ones or GitHub Enterprise Server"
headline: "Gheist abuses stolen GitHub tokens to dump secrets through Actions; GitHub's hold covers public repositories only"
summary: >
  Wiz Research has tracked since 2026-09-15 an automated campaign, Gheist, that uses stolen GitHub tokens to commit a secret-dumping
  Actions workflow to every repository each token can reach, more than 13,500 branches from more than 850 accounts. GitHub's approval
  hold of 2026-07-28 stops the workflow on public github.com repositories, but not on private repositories or GitHub Enterprise Server,
  where Wiz saw the runs complete and the organizations' own workflows assume AWS roles on the attacker branches.
discovered_at: "2026-10-27T03:54:00Z"
updated_at: null
event_date: "2026-10-25"
run_id: 2026-10-27T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, identity, cloud, infostealer]
regions: [global]
sectors: [technology]
entities: ["campaign:gheist", "product:github-enterprise-server"]
techniques: [T1550.001, T1078, T1213.003, T1552, T1567, T1070, T1611]
affected_products: ["GitHub Actions", "GitHub Enterprise Server"]
cves: []
sources:
  - url: "https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles"
    publisher: "Wiz Research"
    date: "2026-10-25"
    role: primary
  - url: "https://github.blog/changelog/2026-07-28-github-actions-holds-potentially-malicious-workflows-for-approval/"
    publisher: "GitHub (changelog)"
    date: "2026-07-28"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We have recovered more than 13,500 planted branches from more than 850 compromised accounts, ranging from personal projects to enterprise organizations' private repositories."
    publisher: "Wiz Research"
    source_url: "https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles"
  - quote: "GitHub masks secret values in logs only when they appear verbatim."
    publisher: "Wiz Research"
    source_url: "https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles"
  - quote: "Unfortunately, that hold doesn't apply to private repositories or GitHub Enterprise Server."
    publisher: "Wiz Research"
    source_url: "https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles"
  - quote: "This protection currently applies to public repositories on github.com only."
    publisher: "GitHub (changelog)"
    source_url: "https://github.blog/changelog/2026-07-28-github-actions-holds-potentially-malicious-workflows-for-approval/"
verification: single-source
sourcing_note: >
  The campaign and its scale are Wiz Research's own telemetry and tracking; GitHub's changelog corroborates only the scope of the
  approval hold. Wiz traces the stolen tokens to infostealer logs and earlier supply-chain compromises without naming an operator.
confidence: medium
references:
  - "2026-10-10/ghostaction-fake-audit-workflow-git-history-credential-theft"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "In every GitHub organisation your teams or suppliers administer, private repositories and GitHub Enterprise Server included, search for branches named ci-sync- plus six random characters that add only the workflow file sync-check.yml, and for any workflow run on them; for every hit, rotate all repository, organisation and environment secrets that repository could read and revoke the token that pushed the commit, because deleting the run or the branch does not undo the exposure."
updates: []
migrated_from: null
---

Wiz Research has tracked since 2026-09-15 a campaign it calls Gheist, after the user agent on its API calls, that uses stolen GitHub access tokens to create a branch and commit a workflow named sync-check in every repository each token can reach: more than 13,500 planted branches from more than 850 compromised accounts, from personal projects to private enterprise repositories ([Wiz, 2026-10-25](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles)). Wiz traces the tokens to infostealer logs and earlier supply-chain compromises ([Wiz, 2026-10-25](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles)). The push triggers the workflow, which prints the repository's secrets, and those of any deployment environment, into its own run log; GitHub masks secret values only when they appear verbatim, so a base32-encoded value prints in full, the tool downloads the log through the GitHub API and deletes the run seconds later, and because the secrets leave through GitHub's own API there is no attacker domain or connection to block ([Wiz, 2026-10-25](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles)). In enterprise organizations the tool cycled through the tokens of several users and automation accounts within minutes and cloned private repositories before planting the workflow; hours later cloud credentials from the same organization were used to enumerate AWS Secrets Manager ([Wiz, 2026-10-25](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles)). Around 2026-10-19 the second variant added a job for repositories with a self-hosted runner that searches the host, and through the Docker socket its root filesystem, for tokens, private keys, environment files and Terraform state; Wiz calls the job buggy ([Wiz, 2026-10-25](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles)).

Since 2026-07-28 GitHub holds potentially malicious workflow runs in public repositories until a collaborator approves them, and every public Gheist run Wiz checked stayed held; the hold applies to public repositories on github.com only and not to GitHub Enterprise Server ([Wiz, 2026-10-25](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles); [GitHub, 2026-07-28](https://github.blog/changelog/2026-07-28-github-actions-holds-potentially-malicious-workflows-for-approval/)). In private repositories and GitHub Enterprise environments Wiz saw runs on the attacker branches complete and be deleted, and cloud audit logs showed the organizations' own workflows running on those branches and assuming AWS roles ([Wiz, 2026-10-25](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles)). As of 2026-10-24 Wiz called the attack ongoing and distinct from the earlier GhostAction campaign ([Wiz, 2026-10-25](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles)).

**Exposure:** organizations whose developers or automation accounts hold GitHub tokens that an infostealer or earlier compromise could have exposed, above all with private repositories, GitHub Enterprise Server, cloud OIDC workflows or self-hosted runners ([Wiz, 2026-10-25](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles)).

**Detection:** in GitHub audit logs, workflow runs on a branch named ci-sync- plus six random characters that were deleted within a minute of completing, and API activity with the user agent gheist; in cloud audit logs, role assumptions whose OIDC subject names such a branch, which shows Actions ran on an attacker branch even where GitHub logs are not collected; on self-hosted runners, the helper files Wiz lists ([Wiz, 2026-10-25](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles)).

**Triage:** the planted commit is unsigned but authored as the token's owner, so the author name alone proves nothing; one new workflow file with a fixed commit message on a branch the owner did not create is the pattern ([Wiz, 2026-10-25](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles)).

**Defender takeaway:** rotate every secret available to a repository where a planted branch exists, revoke the tokens that pushed the commits and check their owners' devices for infostealers, treat a self-hosted runner host and its instance role as compromised if a planted branch ran there, and scope OIDC trust to protected branches or environments with required reviewers on environments that hold production secrets ([Wiz, 2026-10-25](https://www.wiz.io/blog/gheist-attempted-scaled-abuse-of-stolen-github-tokens-stumbles)).
