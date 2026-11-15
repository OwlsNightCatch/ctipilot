---
schema: 1
kind: incident
title: "Cursor marketplace: a tampered Claude Code extension (versions 2.1.312 and 2.1.313) planted an SSH key, a reverse tunnel and persistence for about eleven hours on 2026-10-29; uninstalling it does not remove the persistence"
headline: "Cursor marketplace served a trojanised Claude Code extension for 11 hours; uninstalling leaves the SSH backdoor"
summary: >
  Between about 09:27 and 20:35 UTC on 2026-10-29 the Cursor VS Code Extension Marketplace served a modified copy of Anthropic's Claude Code extension, versions 2.1.312 and 2.1.313 for macOS and Windows, that appends an attacker's SSH key to authorized_keys, tries to enable SSH and open a reverse tunnel, and installs persistence that outlives the extension; coding errors made the SSH step fail on most standard-user hosts, so Cursor says the attacker could not log in there. Cursor's report of 2026-11-13 says the chain began with an access key it had issued to its vendor Fireworks AI, exposed by Fireworks, which gave the attacker a storage bucket of coding-agent traces holding some unredacted credentials, and that a stolen credential from the exposed data let the attacker write the extension straight onto the marketplace cache; Cursor says this was not a vulnerability in Anthropic's product.
discovered_at: "2026-10-31T03:50:00Z"
updated_at: "2026-11-15T04:24:16Z"
event_date: "2026-10-29"
run_id: 2026-10-31T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, vulnerabilities]
regions: [global]
sectors: [technology]
entities: ["incident:cursor-claude-code-extension-compromise-2026-10", "product:cursor", "product:anthropic-claude-code"]
techniques: [T1195.002, T1059.007, T1098.004, T1572, T1543.001, T1053.003, T1053.005, T1547.001, T1082, T1036.005, T1530, T1552, T1078.004]
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
  - url: "https://cursor.com/blog/security-incident-update"
    publisher: "Cursor (incident report)"
    date: "2026-11-13"
    role: primary
  - url: "https://fireworks.ai/security/bulletins/october-2026-security-incident-update"
    publisher: "Fireworks AI (security bulletin update)"
    date: "2026-11-09"
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
  - quote: "On October 29, using a stolen credential from the exposed data from our internal system, the attacker placed malicious, unauthorized copies of Anthropic's Claude Code extension directly on the cache used to serve the Cursor VS Code extension marketplace."
    publisher: "Cursor"
    source_url: "https://cursor.com/blog/security-incident-update"
  - quote: "The marketplace source, Open VSX, never had the malware."
    publisher: "Cursor"
    source_url: "https://cursor.com/blog/security-incident-update"
verification: multi-source
sourcing_note: >
  Cursor, as the marketplace operator, is first-hand on the exposure window, the versions, its response and, from its report of 2026-11-13, the origin of the compromise; Phorion found the backdoor and Microsoft Threat Intelligence analysed the same code independently and agrees on its behaviour. Fireworks' bulletin of 2026-11-09 describes its own intrusion and does not mention Cursor, so the link between the two rests on Cursor's report, and no source attributes the extension to an actor. Phorion first named only 2.1.313 and widened it to 2.1.312 and 2.1.313 after Cursor's notice. NCSC Switzerland's post of 2026-10-30 places the extension on Open VSX; Cursor's report says Open VSX never had the malware.
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
  - "Ask the admin of every Cursor team your organisation uses whether Cursor's email listing exposed keys arrived, and rotate every key it lists, because Cursor says coding-agent traces from sessions outside Privacy Mode held unredacted credentials."
updates:
  - at: "2026-11-15T04:24:16Z"
    run_id: 2026-11-15T0356Z-intel
    type: update
    summary: >
      Cursor's own report of 2026-11-13 gives the origin the entry lacked: an access key Cursor issued to
      its vendor Fireworks AI was exposed, the attacker copied a bucket of coding-agent traces holding
      some unredacted credentials, and a stolen credential let it write the extension onto the marketplace
      cache; Open VSX never carried it and the last attacker activity, on 2026-11-01, was blocked.
    fields: [summary, sources, evidence, techniques, actions, sourcing_note, body]
migrated_from: null
---

Between about 2:27am PT and 1:35pm PT on 2026-10-29 (09:27 to 20:35 UTC) a maliciously modified copy of Anthropic's Claude Code extension, versions 2.1.312 and 2.1.313 for macOS and Windows, was served from the Cursor VS Code Extension Marketplace; Cursor removed it, rebuilt the marketplace, rotated its keys and had the attacker's server taken offline ([Cursor, 2026-10-29](https://cursor.com/blog/claude-code-extension-security-notice)). Anthropic told Microsoft its systems were not compromised and that it did not build the package, and Microsoft confirms the packages were never published to the Visual Studio Marketplace or npm ([Microsoft Threat Intelligence, 2026-10-30](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)). Cursor's report of 2026-11-13 says the attacker wrote the copies onto the marketplace cache with a credential taken through a key exposed at its vendor Fireworks, and that at most 5,000 users potentially received the build ([Cursor, 2026-11-13](https://cursor.com/blog/security-incident-update)).

The injected loader runs when the extension module loads. It reports host and user data (hostname, username, operating system, directories, Git email, environment-variable names and public IP address), appends an attacker-controlled SSH public key to `authorized_keys`, tries to enable the local SSH service and open a reverse SSH tunnel, and installs persistence outside the extension: a LaunchAgent on macOS, and on Windows a scheduled task that asks to run as SYSTEM with a Startup-folder fallback, with background scripts retrying the tunnel about every 60 seconds ([Cursor, 2026-10-29](https://cursor.com/blog/claude-code-extension-security-notice)). Microsoft's analysis adds a user crontab entry for Linux ([Microsoft Threat Intelligence, 2026-10-30](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)). Because of coding errors the step that enables SSH fails unless Cursor was started with administrator privileges, so on most hosts the attacker could not log in through the tunnel, but the key, the persistence and the host report still happened ([Cursor, 2026-10-29](https://cursor.com/blog/claude-code-extension-security-notice)).

**Exposure:** any macOS or Windows host on which Cursor installed or auto-updated Anthropic.claude-code 2.1.312 or 2.1.313 inside the window; the code also carries Linux routines though Cursor names only macOS and Windows packages ([heise online, 2026-10-30](https://www.heise.de/news/Claude-Code-Erweiterung-im-Cursor-Marktplatz-mit-Malware-infiziert-11506368.html)). Extension-install telemetry shows the version. NCSC Switzerland's post of 2026-10-30 places the extension on Open VSX ([NCSC Switzerland, 2026-10-30](https://security-hub.ncsc.admin.ch/#/posts/13121)); Cursor says Open VSX never had it ([Cursor, 2026-11-13](https://cursor.com/blog/security-incident-update)). Cursor says coding-agent traces from sessions outside Privacy Mode were exposed for fewer than 0.05% of users, all notified, so a user with no notice was not among them ([Cursor, 2026-11-13](https://cursor.com/blog/security-incident-update)).

**Detection:** in process-creation telemetry, an editor's extension host starting `ssh` or `autossh` with remote port forwarding and no command; in file-write telemetry, an editor process modifying `authorized_keys`; and, shortly after an extension update, a new LaunchAgent, scheduled task, Startup-folder script or `@reboot` crontab entry named after system-monitoring components. Phorion advises matching the attacker key's fingerprint rather than the comment string it carries ([Phorion, 2026-10-30](https://phorion.io/blog/offical-claude-code-vsx-compromise/)). Removing the extension does not remove the persistence scripts, which keep running ([Cursor, 2026-10-29](https://cursor.com/blog/claude-code-extension-security-notice)).

**Triage:** a running SSH process is not proof the attacker got in, since both ends must allow the connection ([Microsoft Threat Intelligence, 2026-10-30](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)); administrators run tunnels too, and what separates this one is an editor extension as the parent process and persistence written to user-writable locations rather than a managed service.

**Defender takeaway:** treat a host that ran either version as backdoored whether or not the tunnel connected: remove the key, the persistence and the tunnel processes, rebuild where compromise cannot be excluded, and rotate credentials reachable from it. heise reports a cleaned release, with 2.1.314 as the minimum to install ([heise online, 2026-10-30](https://www.heise.de/news/Claude-Code-Erweiterung-im-Cursor-Marktplatz-mit-Malware-infiziert-11506368.html)).

## Update — 2026-11-15T04:24:16Z

Cursor's incident report of 2026-11-13 says an attacker obtained an access key Cursor had issued to its vendor Fireworks, which Fireworks exposed, and used it to copy a read-only storage bucket of historical coding-agent traces from sessions not in Privacy Mode; a small number of the traces held credentials that had not been redacted, and less than 0.01% of customers had API credentials exposed ([Cursor, 2026-11-13](https://cursor.com/blog/security-incident-update)). From those credentials the attacker reached select SaaS tools and, through them, archived non-production source code repositories, limited customer support data and credentials users had sent to Cursor support ([Cursor, 2026-11-13](https://cursor.com/blog/security-incident-update)). On 2026-10-29, "using a stolen credential from the exposed data from our internal system", the attacker placed the malicious copies directly on the cache that serves the marketplace; Cursor says Anthropic did not publish them, that this was not a vulnerability in Anthropic's product, that Open VSX never had the malware, that at most 5,000 users who requested specific cached versions that day potentially received the build, and that the last attacker activity, on 2026-11-01, was blocked ([Cursor, 2026-11-13](https://cursor.com/blog/security-incident-update)). Where credentials were exposed Cursor emailed team admins a list of the keys to rotate ([Cursor, 2026-11-13](https://cursor.com/blog/security-incident-update)).

Fireworks' bulletin of 2026-11-09 describes its own intrusion, which it links to a financially motivated group that sells tokens from unauthorized access to language models to illicit routing gateways ("LLMjacking"), and further activity on 2026-10-23 and 2026-10-24 after a security incident at a cloud provider that hosted its development machines; it does not mention Cursor ([Fireworks AI, 2026-11-09](https://fireworks.ai/security/bulletins/october-2026-security-incident-update)). Neither company names an actor for the extension.
