---
schema: 1
kind: research
title: "Claude Code's 'Yes, and don't ask again' saves the approved command, secrets included, in .claude/settings.local.json: Apiiro finds a real secret in 1,122 of 104,185 public copies of the file on GitHub, and common secret scanners miss a fifth of them"
headline: "Claude Code's don't-ask-again file leaks secrets: 1,122 public copies on GitHub hold a real one"
summary: >
  Apiiro reports that when a developer picks "Yes, and don't ask again" on a shell command that carries a password or token, Claude Code saves that exact command, secret included, in the project's
  .claude/settings.local.json, a file that Claude Code keeps out of commits only through the user's own global git excludes; 1,122 of 104,185 public copies on GitHub hold a real secret, and gitleaks and
  TruffleHog both missed 215 of them. Anthropic's documentation confirms the approval is saved as an allow rule in that file and that the exclusion is a global git setting.
discovered_at: "2026-11-08T03:30:00Z"
updated_at: null
event_date: "2026-11-05"
run_id: 2026-11-08T0256Z-intel
priority: routine
immediate_action: null
tags: [identity]
regions: [global]
sectors: [technology]
entities: []
techniques: [T1552.001]
affected_products: ["Anthropic Claude Code"]
cves: []
sources:
  - url: "https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again"
    publisher: "Apiiro"
    date: "2026-11-05"
    role: primary
  - url: "https://code.claude.com/docs/en/settings"
    publisher: "Anthropic (Claude Code settings documentation)"
    date: "2026-11-04"
    role: corroborating
  - url: "https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html"
    publisher: "The Hacker News"
    date: "2026-11-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Out of 104,185 public copies of this file on GitHub, 1,122 hold a real secret."
    publisher: "Apiiro"
    source_url: "https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again"
  - quote: "saves that exact command, secret included"
    publisher: "Apiiro"
    source_url: "https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again"
verification: single-source
sourcing_note: >
  The counts and the classification of secrets are Apiiro's own measurement of public GitHub between 2026-11-01 and 2026-11-03, and The Hacker News restates them; Apiiro did not test whether the secrets
  still work, and one organisation it notified confirmed its key had been live. Anthropic's documentation confirms the mechanism (the allow rule in the file and the global git exclude) but not the counts.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Apiiro reports that when a developer chooses "Yes, and don't ask again" on a shell command that carries a secret, Claude Code saves that exact command, secret included, in plain text in `.claude/settings.local.json` inside the project ([Apiiro, 2026-11-05](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)). Anthropic's documentation confirms that the approval is saved as an allow rule in that file, and that Claude Code adds the file to the user's global git excludes the first time it writes it, so it stays out of that user's commits ([Anthropic, 2026-11-04](https://code.claude.com/docs/en/settings)). Apiiro points out that this protection lives in one user's git settings on one machine: it does not cover a folder that becomes a repository later, a clone on another machine or a file already committed, and the rule never goes into the repository's own .gitignore ([Apiiro, 2026-11-05](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)).

Apiiro found 104,185 public copies of the file in 103,617 repositories; 1,122 of those files hold at least one secret, 1,379 distinct secrets in all: 379 database passwords, 122 Supabase service-role keys, 43 SSH logins, 42 GitHub, GitLab and npm tokens and 23 AWS keys among them ([Apiiro, 2026-11-05](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)). Counting git history, the shared settings.json and saved agent transcripts, it counts 2,539 secrets in 1,994 repositories ([Apiiro, 2026-11-05](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)). Gitleaks flagged 564 and TruffleHog 643 of the 1,122 files, and 215 were flagged by neither, mostly because a password typed after PGPASSWORD=, sshpass -p or mysql -p looks like an ordinary word in a command line ([Apiiro, 2026-11-05](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)).

**Exposure:** any repository where a developer used Claude Code and approved a command containing a password, token or key with "don't ask again", and every laptop where that was done, because the file sits in plain text there too ([Apiiro, 2026-11-05](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)). To tell, search the organisation's repositories for the two settings files and look in their history, as Apiiro advises ([Apiiro, 2026-11-05](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)).

**Detection:** in pre-commit and CI secret scanning, include git history and make sure the scanner catches passwords typed inside commands, not only known key formats ([The Hacker News, 2026-11-07](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)); history matters because removing the file does not undo the leak, older versions staying in git history and in forks ([The Hacker News, 2026-11-07](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)).

**Defender takeaway:** treat every secret found in these files as exposed and rotate it first, then stop tracking the file with `git rm --cached` and add it to the repository's own .gitignore and the organisation's templates ([Apiiro, 2026-11-05](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)).
