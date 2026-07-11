---
schema: 1
kind: threat
horizon: operational
title: "Rapid7 publishes unpatched Gogs argument-injection RCE with a Metasploit module; maintainer non-responsive"
headline: "Rapid7 publishes unpatched Gogs argument-injection RCE with a Metasploit module; maintainer non-responsive"
summary: "Rapid7 ships a working Metasploit module against an unpatched Gogs zero-day (argument injection via git rebase --exec in the rebase-merge code path; CVSSv4 9.4). The maintainer did not respond to coordinated disclosure within 90 days; ~1,141 internet-facing instances visible on Shodan. No patch. Mitigate by disabling self-registration and the rebase-merge strategy."
discovered_at: "2026-05-29T05:00:02Z"
event_date: null
run_id: 2026-05-29-c7f56b00
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - rce
  - no-patch
  - poc-public
regions:
  - global
  - europe
  - switzerland
sectors:
  - public-sector
  - education
  - technology
entities:
  - "trend:gogs-unpatched-argument-injection-rce-rapid7-metasploit"
cves: []
sources:
  - url: "https://www.rapid7.com/blog/post/ve-authenticated-rce-via-argument-injection-gogs-unfixed/"
    publisher: Rapid7 Labs — Gogs unpatched RCE
    role: primary
  - url: "https://thehackernews.com/2026/05/critical-gogs-rce-vulnerability-lets.html"
    publisher: "The Hacker News, 2026-05-28"
    role: corroborating
closed_sources: []
evidence:
  - quote: An authenticated Gogs user can achieve remote code execution on the underlying server by exploiting an argument injection vulnerability
    publisher: Rapid7 Research
  - quote: "The flaw exploits argument injection in the git rebase command during merge operations by injecting the --exec flag. No admin privileges are required; attackers only need account creation and repository access"
    publisher: The Hacker News
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
migrated_from: briefs/2026-05-29.md
---

Rapid7 Labs disclosed on 2026-05-28 [an authenticated-RCE zero-day in Gogs](https://www.rapid7.com/blog/post/ve-authenticated-rce-via-argument-injection-gogs-unfixed/), the open-source self-hosted Git service. The root cause is in the `Merge()` function inside `internal/database/pull.go`: when the *"Rebase before merging"* strategy is invoked on a pull request, Gogs passes the source-branch name unsanitised to `process.ExecDir`, bypassing the safer `git-module` wrappers. An attacker creates a branch named e.g. `--exec=<command>`; when `git rebase` runs, that flag is interpreted as a `--exec` argument and the command executes under the Gogs service account. Affected: Gogs 0.14.2 and 0.15.0+dev (commit `b53d3162`); all prior versions that support the rebase-merge strategy are likely affected too. The maintainer acknowledged the report on 2026-03-28 (reported 2026-03-17) but has not shipped a fix; Rapid7 published after the standard 90-day window expired. Rapid7 also released a full Metasploit module covering Windows and Linux targets. Shodan shows ~1,141 internet-facing Gogs instances. Class is CWE-88 argument injection — same technique family as CVE-2024-39930 / 39932 / 39933 in prior Gogs disclosures. The [Hacker News writeup](https://thehackernews.com/2026/05/critical-gogs-rce-vulnerability-lets.html) corroborates and adds that no admin privileges are required, only account creation and repository access.

**Why it matters to us:** Self-hosted Gogs is common in European public-sector code and research infrastructure as a lightweight GitHub alternative. Until a patched fork (Gitea / Forgejo) is adopted, set `DISABLE_REGISTRATION = true` in `app.ini`, disable the *Rebase before merging* strategy under instance settings, and watch for `git` child processes carrying `--exec` under the Gogs binary's process tree (Sysmon EID 1 / `auditd` EXECVE).
