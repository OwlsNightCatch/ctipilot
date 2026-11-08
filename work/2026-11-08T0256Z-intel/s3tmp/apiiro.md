Title: Coding Agents Are Leaking Your Secrets to GitHub

URL Source: https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again

Published Time: 2026-11-05

Markdown Content:
_Apiiro research found 2,539 real secrets in 1,994 public GitHub repositories: database passwords, cloud keys, API tokens, SSH root logins. Among them: a database vendor's own admin-level cloud key, a production Azure Postgres password, a Square production token, and the owner password of a medical-records database. 63 organizations, mostly software companies of all sizes, are affected. One confirmed its key had been live._

_Ask Claude Code to check a database or call an API, and the command it proposes carries the secret from your config file. It asks before running it. Pick "Yes, and don't ask again" and it saves that exact command, secret included, to `.claude/settings.local.json` inside the project folder. Nothing in the repo marks that file as private, so it gets committed with the rest of the code._

_Out of 104,185 public copies of this file on GitHub, 1,122 hold a real secret. We found 1,160 more in git history, in the shared `settings.json` teams commit on purpose, and in agent chat transcripts saved in repos._

_GitHub is just where we could count. The same file sits in plain text on every laptop where someone clicked "don't ask again." Malware already collects credentials from developer machines in bulk. The Shai-Hulud npm worm ran TruffleHog over victims' files; that same scanner flags 643 of the 1,122 files we found. And one in five of those files is flagged by neither gitleaks nor TruffleHog, usually because the secret is a password typed inside a command, not a key in a recognizable format._

## Check if you’re affected

**Is it public?** Search your GitHub organization for .claude/settings.local.json and .claude/settings.json. Each hit is a file anyone can read right now.

**Was it ever committed?** Check each repo’s git history for the file, even if it’s gone today. If history has it, so does every fork and clone.

**What's in it?** Find every copy of the file on your machine and read its allow list. Each entry is a command you approved, with whatever you typed into it: look for passwords, tokens, keys and connection strings.

**Found something:** rotate first, clean up second.

## How a secret ends up in a settings file

Developer machines hold secrets: a database connection string in a config file, cloud keys in local installations, an API token in .env. Ask Claude Code to check why login fails on staging or to run a migration, and the command it proposes carries that secret, because it can’t work without it. Claude Code asks before it runs a shell command, multiple times a session. Pick "Yes, and don't ask again" and it runs the command and adds a permission rule to `.claude/settings.local.json` in the project folder, so it won't ask again. The rule is the command string itself:

This is Claude Code's own behavior, not the model's: it happens with Anthropic's latest models too, and we reproduced it with Opus 5.5 and Fable 5.1.

The file is meant to stay on the developer’s machine, and Claude Code tries to keep it there. When it creates the file inside a git repo, it adds it to the developer's _global_ git ignore list. That covers the common case. It doesn’t cover a folder that becomes a repo later, a clone on another machine, or a file someone already committed. The rule never goes into the repo's own .gitignore, so nothing travels with the project to protect it.

Often Claude commits the file itself. In 539 of the 1,105 repos with a real secret that we traced, a commit co-authored by Claude changed the file. Those commits name every recent model, from Sonnet 4.5 to Opus 5.5.

## Who is exposed

63 organizations hold a real secret in a public allowlist. The strongest cases, all in `.claude/settings.local.json` and each checked at a pinned commit:

| Organization | What’s exposed |
| --- | --- |
| Database vendor | Its own cloud API key with manage access and no expiry claim, plus the cluster host |
| B2B startup | Production Azure Postgres password |
| Software agency | Square production access token |
| Open-source project (over 1,000 stars) | OpenAI-format API key |
| Open-source project | npm token |
| IT services firm (medical-records app) | Owner password for the app’s cloud Postgres database |
| Payments startup | Postgres password for the postgres role |

Most are companies: startups, software agencies, IT services firms. A few are established vendors, exposed through their own demo and workshop repos. Nobody meant to publish a key. The key was in a command, the command was approved, and the file was committed with everything else.

The allowlists also hold server logins: 43 SSH credentials for public servers, some of them a root password in an `sshpass` command. One university repo, for example, permanently approved a root SSH command to a public server.

## How many

Public GitHub holds 104,185 copies of .claude/settings.local.json, in 103,617 repositories. 1,122 files (1.1%) hold a real secret: a key in a known provider format, or a password or token next to a public host. Together they hold 1,379 distinct secrets: 636 provider keys and 743 passwords or tokens for public hosts.

More than a third open a database directly: 379 database passwords and 122 Supabase service-role keys. Another 103 are Supabase account tokens, which control every project in the account. The rest are mostly API tokens for third-party services and AI model keys, plus 43 SSH logins, 42 GitHub, GitLab and npm tokens, 23 AWS keys and 6 private keys.

Large allowlists drive the rate. One in ten files over 8 KB holds a real secret, against fewer than one in 500 under 500 bytes. The longer a developer has been clicking “don’t ask again”, the more the file holds.

The files are still there: every one sat on its repo’s default branch on November 2, 2026, and most have sat there a long time. In the median repo with a real secret, the file was first committed 217 days before that. In 118 repos, more than a year before.  
 Forks copy them: 211 forks of 74 repos carry the same secrets.

Deleting the file doesn’t solve it. Earlier versions of the file hold 734 real secrets, in 509 repos, that appear in no current copy, usually because the file was deleted.

Counting the file's history, the shared settings file and agent transcripts (next sections), the total comes to 2,539 distinct real secrets in 1,994 repos.

## What secret scanners miss

Generic secret scanners miss many of these. We ran **gitleaks** and **TruffleHog** over all 104,185 files. Of the 1,122 files with a real secret, gitleaks flagged 564 and TruffleHog 643; 215 were flagged by neither.

The gap is passwords inside commands. Scanners look for key formats: a provider prefix, a long random string. A password typed after `PGPASSWORD=`, `sshpass -p` or `mysql -p`, or a bearer header in a curl call, is an ordinary word in an ordinary command line, and both tools mostly let it through.

This matters beyond this file. The same password-in-a-command pattern appears wherever an agent records what it ran: transcripts, memory files, handoff notes, and a scanner tuned to key formats misses it in all of them.

## Not just one file

The allowlist is the clearest case, but agents write secrets into other files developers commit.

| File | Checked | With a real secret |
| --- | --- | --- |
| Shared .claude/settings.json | All 76,011 | 298 files |
| Agent chat transcripts (.specstory, aider, Cursor exports) | 2,523 | 120 files in 87 repos |
| Agent memory files (MEMORY.md and similar) | 1,200 | 9 repos |
| Handoff and deploy notes | 2,095 | 33 files |
| VS Code Copilot auto-approve settings | 173 | 9 repos |

Teams commit the shared settings file on purpose, and most of its secrets sit in allow rules as exact command lines. A third of the handoff notes with a secret were written by the agent itself.

The file leaks beyond GitHub too. Of 31,053 Hugging Face Spaces, 126 hold .claude/settings.local.json, and one has allow rules with a database service key and a user password. On GitLab.com, 2 of the 69 public copies we checked hold a real secret, including a GitLab access token.

The habit that leaks is the same everywhere: typing a secret into a command that an agent then records.

## On the developer's machine

Most of these files never reach GitHub. They stay on developers’ machines, and that doesn’t make them safe. The allowlist is plain JSON in the project folder.

Malware already collects credentials from developer machines in bulk. In September 2025 the [Shai-Hulud npm worm](https://sysdig.com/blog/shai-hulud-the-novel-self-replicating-worm-infecting-hundreds-of-npm-packages) downloaded TruffleHog and ran it over the victim’s files. That scanner flags 643 of the 1,122 files with a real secret. Three weeks earlier, the [malicious Nx packages](https://blog.gitguardian.com/the-nx-s1ngularity-attack-inside-the-credential-leak/) told the developer’s own Claude Code and Gemini CLI to search the disk for secrets.

The file can also leave without git: in a published npm package, a Docker image built with a copy command, a zip archive or a synced folder. And a secret approved once stays in the file until someone deletes the rule, long after the command ran.

## Prior work

This post adds the full GitHub count of secrets leakage at scale, the organization cases, the scanner gap, and the other agent files that carry the same secrets. Claude Code users have reported the mechanism in GitHub issues since August 2025 ([#5544](https://github.com/anthropics/claude-code/issues/5544), [#11982](https://github.com/anthropics/claude-code/issues/11982), [#13106](https://github.com/anthropics/claude-code/issues/13106), [#91270](https://github.com/anthropics/claude-code/issues/91270)). None got a reply from Anthropic, and three were closed automatically as inactive or duplicate. ironPeak found the same file in their own repo in February 2026 and measured 2.4% of repos with AI config folders carrying secrets in history, on a sample of 100. Lakera found credentials in 33 such files across 30 npm packages in April.

## What to do

**Developers:**

1.   If the file is tracked in a repo, untrack it with git rm --cached `.claude/settings.local.json` and add it to the repo’s own .gitignore.
2.   Rotate every credential the file has ever held. Removing it doesn’t clear git history, forks or clones.
3.   Even if the file was never committed, open it and delete every rule that contains a secret.
4.   Stop typing secrets into commands. Reference them as $VAR from whatever secrets manager you use, so the rule records $DB_URL, not the secret.
5.   Approve patterns, like `Bash(npm run:*)`, instead of literal commands.

**Security teams:**

1.   Treat agent folders: .claude/, .cursor/, .gemini/, .specstory/, agent memory files, as secret-bearing, like .env, on laptops as well as in repos.
2.   Add them to pre-commit and CI secret scanning, including history. Make sure the scanner catches passwords inside commands (PGPASSWORD=, sshpass -p, mysql -p, bearer headers), not only provider key formats.
3.   Add .claude/settings.local.json to your org’s .gitignore templates.
4.   Triage credentials paired with public hosts first: those are the ones that give access.

## Disclosure

We reported each organization case to its owner on November 2 and 3, 2026. One company confirmed its key had been live.

## Method and limits

**Collection.** All data came from read-only GitHub code and commit search on default branches, November 1 to 3, 2026. Code search returns at most 1,000 results per query, so we split the search by file size until every slice fit under the cap. That listed 104,185 .claude/settings.local.json files in 103,617 repos and 76,011 shared settings.json files, and we downloaded every one. File history covers 43,120 repos, including every repo whose commits mention removing, untracking, redacting or rotating the file, so the history count is a floor. Forks: every fork of a repo with a real secret. Transcripts, memory files, handoff notes and Copilot settings were found by searching for key prefixes and connection strings; the table gives how many we checked. We compared how 16 coding agents store approvals from their documentation; Claude Code is the only one confirmed to write the full approved command to a project file by default.

**Classification.** We use the two detector classes secret scanners use. Provider patterns match a known key format: OpenAI, Anthropic, AWS, GitHub, npm, Supabase, Stripe, Slack and others. Generic secrets are passwords and tokens without a known format; we count one only when a public host sits on the same line, as in a connection string or a PGPASSWORD= before psql -h. Rules then remove known false positives: placeholders, common default passwords, local and private hosts, keys that are public by design (Supabase anon keys, Firebase web config), the local Supabase demo key, expired tokens, and GitHub and npm tokens whose built-in checksum fails. Every remaining distinct value, 2,774 in all, was reviewed in its masked context by an independent LLM reviewer working from a written rubric. A value counts as a real secret only when the rules and the review agree: 2,539 across all sources. Memory files, handoff notes and Copilot settings were classified by the rules alone. gitleaks and TruffleHog ran without verification.

**Limits.** No credential was used or tested, and no host was contacted. "Real secret" means a credential that matches a provider format or points at a public host, not one known to be valid. Every organization case was checked at a commit-pinned link.

Links/Buttons:
- [Read](https://apiiro.com/blog/apiiro-named-a-leader-in-the-forrester-wave-agentic-development-security-tools)
- [](https://github.com/apiiro/mcp-server)
- [Back to blog](https://apiiro.com/blog)
- [Shai-Hulud npm worm](https://sysdig.com/blog/shai-hulud-the-novel-self-replicating-worm-infecting-hundreds-of-npm-packages)
- [malicious Nx packages](https://blog.gitguardian.com/the-nx-s1ngularity-attack-inside-the-credential-leak/)
- [#5544](https://github.com/anthropics/claude-code/issues/5544)
- [#11982](https://github.com/anthropics/claude-code/issues/11982)
- [#13106](https://github.com/anthropics/claude-code/issues/13106)
- [#91270](https://github.com/anthropics/claude-code/issues/91270)
- [Check if you’re affected](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again#check-if-youre-affected)
- [How a secret ends up in a settings file](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again#how-a-secret-ends-up-in-a-settings-file)
- [Who is exposed](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again#who-is-exposed)
- [How many](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again#how-many)
- [What secret scanners miss](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again#what-secret-scanners-miss)
- [Not just one file](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again#not-just-one-file)
- [On the developer's machine](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again#on-the-developers-machine)
- [Prior work](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again#prior-work)
- [What to do](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again#what-to-do)
- [Disclosure](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again#disclosure)
- [Method and limits](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again#method-and-limits)
- [ProductGuardian in Practice: How AppSec Teams Put an AI Security Engineer to WorkPublished October 29 2026](https://apiiro.com/blog/guardian-in-practice-appsec-ai-security-engineer)
- [ResearchCVE-2026-111497: Brotli Decoder Out-of-Bounds Write in .NET, PowerShell, Go and EnvoyPublished October 27 2026](https://apiiro.com/blog/brotli-decoder-out-of-bounds-write-net-powershell-go-envoy)
- [Guardian Agent](https://apiiro.com/product)
- [Protect](https://apiiro.com/product/guardian-agent/protect)
- [Prevent](https://apiiro.com/product/guardian-agent/prevent)
- [AutoFix](https://apiiro.com/product/guardian-agent/autofix)
- [AI-SAST](https://apiiro.com/product/guardian-agent/ai-sast)
- [AI-SCA](https://apiiro.com/product/guardian-agent/ai-sca)
- [SSCS](https://apiiro.com/product/guardian-agent/sscs)
- [AI-SPM](https://apiiro.com/product/guardian-agent/ai-spm)
- [AI Threat Modeling](https://apiiro.com/product/guardian-agent/ai-threat-modeling)
- [ASPM](https://apiiro.com/product/guardian-agent/aspm)
- [API Security](https://apiiro.com/product/guardian-agent/api-security)
- [Secrets Security](https://apiiro.com/product/guardian-agent/secrets-security)
- [Context Graph](https://apiiro.com/platform)
- [Software Graph](https://apiiro.com/platform/data-fabric/software-graph)
- [Risk Graph](https://apiiro.com/platform/data-fabric/risk-graph)
- [Integrations](https://apiiro.com/platform/data-fabric/integrations)
- [About](https://apiiro.com/company/about)
- [Partners](https://apiiro.com/company/partners)
- [Customers](https://apiiro.com/customers)
- [Careers](https://apiiro.com/careers)
- [Case Studies](https://apiiro.com/resources/case-studies)
- [Guides](https://apiiro.com/resources/guides)
- [Videos](https://apiiro.com/resources/videos)
- [Webinars](https://apiiro.com/resources/webinars)
- [Glossary](https://apiiro.com/glossary)
- [Operational](https://status.apiiro.com/)
- [Privacy Policy](https://apiiro.com/privacy-policy)
- [Terms of Use](https://apiiro.com/terms-of-use)
- [Cookie Policy](https://apiiro.com/cookie-policy)
