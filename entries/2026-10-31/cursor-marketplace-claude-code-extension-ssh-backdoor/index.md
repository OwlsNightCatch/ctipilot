---
schema: 1
kind: incident
title: "Cursor marketplace: a tampered Claude Code extension (versions 2.1.312 and 2.1.313) planted an SSH key, a reverse tunnel and persistence for about eleven hours on 2026-10-29; uninstalling it does not remove the persistence"
headline: "Cursor marketplace served a trojanised Claude Code extension for 11 hours; uninstalling leaves the SSH backdoor"
summary: >
  Between about 09:27 and 20:35 UTC on 2026-10-29 the Cursor VS Code Extension Marketplace served a modified copy of Anthropic's Claude Code extension, versions 2.1.312 and 2.1.313 for macOS and Windows, that appends an attacker's SSH key to authorized_keys, tries to enable SSH and open a reverse tunnel, and installs persistence that outlives the extension. Coding errors made the SSH step fail on most standard-user hosts, so Cursor and Sophos say the attacker could not log in there, but the key, the persistence and a host report were still written. Anthropic told Microsoft its systems were not compromised, and no source says how the attacker published under Anthropic's name.
discovered_at: "2026-10-31T03:50:00Z"
updated_at: null
event_date: "2026-10-29"
run_id: 2026-10-31T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, vulnerabilities]
regions: [global]
sectors: [technology]
entities: ["incident:cursor-claude-code-extension-compromise-2026-10", "product:cursor", "product:anthropic-claude-code"]
techniques: [T1195.002, T1059.007, T1098.004, T1572, T1543.001, T1053.003, T1053.005, T1547.001, T1082, T1036.005]
affected_products: ["Cursor", "Anthropic Claude Code"]
cves: []
sources:
  - url: "https://cursor.com/blog/claude-code-extension-security-notice"
    publisher: "Cursor (security notice)"
    date: "2026-10-29"
    role: primary
  - url: "https://phorion.io/blog/offical-claude-code-vsx-compromise/"
    publisher: "Phorion"
    date: "2026-10-30"
    role: primary
  - url: "https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-10-30"
    role: corroborating
  - url: "https://www.sophos.com/en-us/blog/malicious-claude-code-extension-distributed-through-cursor-marketplace"
    publisher: "Sophos X-Ops"
    date: "2026-10-30"
    role: corroborating
  - url: "https://www.heise.de/news/Claude-Code-Erweiterung-im-Cursor-Marktplatz-mit-Malware-infiziert-11506368.html"
    publisher: "heise online"
    date: "2026-10-30"
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/13121"
    publisher: "NCSC Switzerland (Cyber Security Hub, post 13121)"
    date: "2026-10-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Between about 2:27am PT and 1:35pm PT today, a maliciously modified version of Anthropic’s Claude Code extension was made available in the Cursor VS Code Extension Marketplace."
    publisher: "Cursor"
    source_url: "https://cursor.com/blog/claude-code-extension-security-notice"
  - quote: "Uninstalling the extension may not be sufficient — the payload drops standalone persistence scripts that keep running."
    publisher: "Cursor"
    source_url: "https://cursor.com/blog/claude-code-extension-security-notice"
  - quote: "Anthropic confirmed to Microsoft that their systems were not compromised and they did not develop the malicious package posted in Cursor marketplace."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/"
  - quote: "A running SSH process does not necessarily mean the attacker gained access."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/"
  - quote: "Cursor identified impacted macOS and Windows packages and estimates that up to 5,000 users were affected."
    publisher: "Sophos X-Ops"
    source_url: "https://www.sophos.com/en-us/blog/malicious-claude-code-extension-distributed-through-cursor-marketplace"
verification: multi-source
sourcing_note: >
  Cursor, as the marketplace operator, is first-hand on the exposure window, the versions and its response; Phorion found the backdoor and Microsoft Threat Intelligence analysed the same code independently and agrees on its behaviour. No source says how the attacker was able to publish under Anthropic's name, and no source attributes the activity to an actor. Phorion first named only 2.1.313 and widened it to 2.1.312 and 2.1.313 after Cursor's notice. NCSC Switzerland's post of 2026-10-30 differs on where the extension was served (Open VSX, with versions pulled from npm and the VS Code marketplace); Microsoft, Cursor and Phorion place it in the Cursor marketplace only, and the entry follows them.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "On every developer endpoint that runs Cursor, check extension-install telemetry for Anthropic.claude-code 2.1.312 or 2.1.313 installed between 09:27 and 20:35 UTC on 2026-10-29; where it is found, isolate the host, remove the unauthorized SSH key, the persistence and any running tunnel process, because uninstalling the extension removes none of them, and rotate every credential reachable from the host from a trusted system."
updates: []
migrated_from: null
---

Between about 2:27am PT and 1:35pm PT on 2026-10-29 (09:27 to 20:35 UTC) a maliciously modified copy of Anthropic's Claude Code extension, versions 2.1.312 and 2.1.313 for macOS and Windows, was served from the Cursor VS Code Extension Marketplace; Cursor removed it, shut the marketplace down briefly, rotated its keys, rebuilt it and had the hosting provider take the attacker's server offline ([Cursor, 2026-10-29](https://cursor.com/blog/claude-code-extension-security-notice)). Anthropic told Microsoft its systems were not compromised and that it did not build the package, and Microsoft confirms the packages were never published to the Visual Studio Marketplace or npm ([Microsoft Threat Intelligence, 2026-10-30](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)). How the attacker published under Anthropic's name is not disclosed in any source read. Cursor estimates up to 5,000 affected users ([Sophos X-Ops, 2026-10-30](https://www.sophos.com/en-us/blog/malicious-claude-code-extension-distributed-through-cursor-marketplace)).

The injected loader runs when the extension module loads. It reports host and user data (hostname, username, operating system, home and working directories, the configured Git email, environment-variable names and public IP address), appends an attacker-controlled SSH public key to `authorized_keys`, tries to enable the local SSH service and open a reverse SSH tunnel, and installs persistence outside the extension: a LaunchAgent on macOS, and on Windows a scheduled task that asks to run as SYSTEM with a Startup-folder fallback, with background scripts retrying the tunnel about every 60 seconds ([Cursor, 2026-10-29](https://cursor.com/blog/claude-code-extension-security-notice)). Microsoft's analysis adds a user crontab entry for Linux ([Microsoft Threat Intelligence, 2026-10-30](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)). Because of coding errors the step that enables SSH fails unless Cursor was started with administrator privileges, so on most hosts the attacker could not log in through the tunnel, but the key, the persistence and the host report still happened ([Cursor, 2026-10-29](https://cursor.com/blog/claude-code-extension-security-notice)).

**Exposure:** any macOS or Windows host on which Cursor installed or auto-updated Anthropic.claude-code 2.1.312 or 2.1.313 inside the window; the code also carries Linux routines though Cursor names only macOS and Windows packages ([heise online, 2026-10-30](https://www.heise.de/news/Claude-Code-Erweiterung-im-Cursor-Marktplatz-mit-Malware-infiziert-11506368.html)). Extension-install telemetry shows the version. NCSC Switzerland carried the incident on 2026-10-30 but places the backdoored extension on Open VSX and says Anthropic pulled versions from npm and the VS Code marketplace ([NCSC Switzerland, 2026-10-30](https://security-hub.ncsc.admin.ch/#/posts/13121)); Microsoft says the packages never reached the Visual Studio Marketplace or npm, and Cursor and Phorion name the Cursor marketplace, so the entry follows them.

**Detection:** in process-creation telemetry, an editor's extension host starting `ssh` or `autossh` with remote port forwarding and no command; in file-write telemetry, an editor process modifying `authorized_keys`; and, shortly after an extension update, a new LaunchAgent, scheduled task, Startup-folder script or `@reboot` crontab entry named after system-monitoring components. Phorion advises matching the attacker key's fingerprint rather than the comment string it carries ([Phorion, 2026-10-30](https://phorion.io/blog/offical-claude-code-vsx-compromise/)). Removing the extension does not remove the persistence scripts, which keep running ([Cursor, 2026-10-29](https://cursor.com/blog/claude-code-extension-security-notice)).

**Triage:** a running SSH process is not proof the attacker got in, since both ends must allow the connection ([Microsoft Threat Intelligence, 2026-10-30](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)); administrators run tunnels too, and what separates this one is an editor extension as the parent process and persistence written to user-writable locations rather than a managed service.

**Defender takeaway:** treat a host that ran either version as backdoored whether or not the tunnel connected: remove the key, the persistence and the tunnel processes, rebuild where compromise cannot be excluded, and rotate credentials reachable from it. heise reports a cleaned release, with 2.1.314 as the minimum to install ([heise online, 2026-10-30](https://www.heise.de/news/Claude-Code-Erweiterung-im-Cursor-Marktplatz-mit-Malware-infiziert-11506368.html)).
