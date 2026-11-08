---
title: Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public Copies on GitHub
author: The Hacker News
url: https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html
hostname: thehackernews.com
description: Claude Code saves secrets in approved commands, exposing 2,539 credentials across 1,994 public GitHub repositories, Apiiro finds.
sitename: The Hacker News
date: "2026-11-07"
categories: ['Article']
fingerprint: af3011da67a70ac6
---
Passwords and API keys that developers typed into commands they approved in Claude Code are sitting in public GitHub repositories, where anyone can read them.

When a user selects "**Yes, and don't ask again**," Anthropic's AI coding assistant can save the command, word-for-word, including the secret, in a project settings file.

Software security company Apiiro said yesterday that 1,122 public copies of that file hold at least one secret, though it did not test whether any still work. One company the researchers notified earlier this week confirmed its key had been live.

The file is .claude/settings.local.json. Removing it from a project does not undo the leak, because older versions stay in git history and in forks of the repository. The researchers' advice is to rotate first: change every password, token, and key the file has ever held, then clean up.

### How a Secret Lands in the File

By default, Claude Code asks before it runs most shell commands. If the user picks "Yes, and don't ask again," it saves an allow rule in .claude/settings.local.json inside the project, according to its [permissions documentation](https://code.claude.com/docs/en/permissions). Matching commands then run without asking in later sessions.

The rule covers only what the prompt offered. Sometimes that is a pattern, such as npm test \*, and sometimes one exact command. When it is the exact command, any password or token typed into it is saved too, in plain text.

In public files, the researchers found saved commands with the secret still inside, and they reproduced the behavior with the latest models, Opus 5.5 and Fable 5.1.

Claude Code tries to keep the file out of git. The first time it writes the file in a git repository, it adds the file to the user's global git excludes, its [settings documentation](https://code.claude.com/docs/en/settings) says. Git on that computer then ignores the file in every repository.

That protection stays in one user's git settings on one computer. It does nothing for a file that was already committed, the researchers say. Claude Code never adds the file to the project's own .gitignore, so the protection does not travel with the project.


In 539 of the 1,105 repositories the researchers traced, a commit listing Claude as a co-author changed the file. They take this to mean Claude often commits the file itself.

### What Apiiro Found

Apiiro's search of public GitHub found 104,185 copies of the file in 103,617 repositories, its [research write-up](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) shows. About 1.1% of them, or 1,122 copies, hold at least one secret. Together they hold 1,379 different secrets.

A value counted as a secret when it matched a known key format, or when a password or token sat beside the address of a public server. An AI reviewer also had to agree. The researchers do not say whether anyone has used these secrets.

More than a third of the secrets open a database directly, including 379 database passwords. Others include 43 SSH logins for public servers, 42 tokens for GitHub, GitLab and npm, and 23 AWS keys.

Among the owners of these files are 63 organizations, mostly software companies of all sizes. The strongest cases include a database vendor's own admin-level cloud key and the owner password of a medical-records database, the researchers say.

As of Monday, every file with a secret was still on its repository's default branch, and in half of those repositories it had been there for at least 217 days.

Older versions of the file contain 734 more secrets across 509 repositories that are not present in any current copy, usually because the file was deleted. Forks spread the files further: 211 forks of 74 repositories carry the same secrets as the originals.

Secrets also sit in 298 of 76,011 copies of the shared .claude/settings.json file, which teams commit on purpose, mostly inside allow rules. Including those, the older versions, and saved agent chat logs, the total is 2,539 secrets across 1,994 repositories.

Of 16 coding agents whose documentation the researchers compared, Claude Code is the only one confirmed to save the full approved command in a project file by default.

### What to Do

For developers, the researchers recommend these steps:

1. Search your GitHub organization for .claude/settings.local.json and .claude/settings.json, and check each repository's git history for them, even where the files are gone.
2. Rotate every password, token and key the files have ever held, before cleaning up.
3. Stop tracking the local file with git rm --cached .claude/settings.local.json, and add it to the repository's own .gitignore.
4. Open the file on your own computer, even if it was never committed, and delete every rule that contains a secret.
5. Keep secrets out of commands. Refer to them as variables from a secrets manager, such as $DB\_URL, so the saved rule holds the variable name and not the secret.
6. Approve patterns, such as Bash(npm run:\*), instead of single commands.

Copies that never reach GitHub still matter, the researchers say. The file is plain JSON in the project folder, and it can also be left inside an npm package, a Docker image, a zip archive, or a synced folder.

Malware has previously looked for secrets on developer machines. In September 2025, the [Shai-Hulud worm](https://thehackernews.com/2025/09/40-npm-packages-compromised-in-supply.html) ran the TruffleHog secret scanner over infected computers, and the scanner flagged more than half of the files as secret.

Common secret scanners miss many of these files. The researchers ran gitleaks and TruffleHog over every copy, without the tools' verification step. Of the 1,122 files with a secret, gitleaks flagged 564 and TruffleHog 643, and neither flagged 215.

Most misses are passwords typed inside commands. Scanners look for known key formats, and a password after PGPASSWORD=, sshpass -p , or mysql -p looks like an ordinary word in an ordinary command line.

For security teams, the researchers recommend:

- Treat agent folders such as .claude/, .cursor/, .gemini/ and .specstory/, and agent memory files, as holding secrets, like .env files, on laptops as well as in repositories.
- Add them to pre-commit and CI secret scanning, including git history, and make sure the scanner catches passwords inside commands, not only known key formats.
- Add .claude/settings.local.json to the organization's .gitignore templates.
- Check credentials paired with a public server first, because those are the ones that give access.

### Earlier Reports

Claude Code users have reported this behavior before. An [earlier bug report](https://github.com/anthropics/claude-code/issues/5544), filed on August 11, 2025, said approved commands with API keys and tokens were being stored word for word in settings.local.json.

An automated bot closed that report as "not planned" on January 3, after 60 days without activity.

As of today, the four related reports the researchers cite have all been closed by the same bot, the most recent yesterday. None got a reply from Anthropic, they say.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
