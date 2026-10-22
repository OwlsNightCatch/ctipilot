---
schema: 1
kind: threat
title: "Nx Console VS Code extension version 18.95.0 shipped a credential stealer, published with a contributor token stolen in the TanStack npm compromise"
headline: "Malicious Nx Console 18.95.0 stayed up to 36 minutes on two extension marketplaces, stealing developer credentials"
summary: >
  On 2026-05-18 an attacker published a malicious Nx Console 18.95.0 to the Visual Studio Marketplace
  (12:30 to 12:48 UTC) and Open VSX (12:33 to 13:09 UTC) as a legitimate core contributor, whose GitHub
  CLI OAuth token a credential stealer from the 2026-05-11 TanStack npm compromise had exfiltrated a week
  earlier. On activation the extension fetched an obfuscated payload that harvested GitHub, npm, AWS,
  Vault, Kubernetes and 1Password secrets and planted a Python backdoor; Microsoft counts 28 Marketplace
  installs and Nx about 6,000 activations, and version 18.100.0 or later is clean.
discovered_at: "2026-05-20T05:00:04Z"
event_date: 2026-05-18
run_id: 2026-05-20-a0f7b07f
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - identity
  - cloud
regions:
  - global
sectors:
  - technology
entities:
  - "incident:nx-console-vs-code-extension-18-95-0-compromised-stolen-publ"
techniques: [T1195.002, T1528, T1059.007, T1552.001, T1552.005, T1555.005, T1102.001, T1543.001, T1548.003, T1041]
affected_products:
  - "Nx Console"
cves: []
sources:
  - url: "https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w"
    publisher: "Nx (GHSA-c9j4-9m59-847w)"
    date: "2026-05-18"
    role: primary
  - url: "https://nx.dev/blog/nx-console-v18-95-0-postmortem"
    publisher: "Nx (postmortem)"
    date: "2026-05-21"
    role: primary
  - url: "https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised"
    publisher: "StepSecurity"
    date: "2026-05-18"
    role: corroborating
  - url: "https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html"
    publisher: "The Hacker News"
    date: "2026-05-19"
    role: corroborating
  - url: "https://cybersecuritynews.com/nx-console-vs-code-extension-compromised/"
    publisher: "CybersecurityNews"
    date: "2026-05-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A malicious version of Nx Console 18.95.0 was published at 12:30 PM UTC and removed soon after at 12:48 PM UTC"
    publisher: "Nx (GHSA-c9j4-9m59-847w)"
    source_url: "https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w"
  - quote: "The attacker published the malicious version as a legitimate Nx core contributor."
    publisher: "Nx (postmortem)"
    source_url: "https://nx.dev/blog/nx-console-v18-95-0-postmortem"
  - quote: "Anyone who installed v18.95.0 during the exposure window (2026-05-18, 12:30-13:09 UTC) should treat their machine as compromised and rotate credentials."
    publisher: "Nx (postmortem)"
    source_url: "https://nx.dev/blog/nx-console-v18-95-0-postmortem"
  - quote: "It also installs a persistent Python backdoor on macOS that uses the GitHub Search API as a dead-drop for receiving further commands signed with a 4096-bit RSA key."
    publisher: "StepSecurity"
    source_url: "https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised"
verification: multi-source
sourcing_note: >
  Nx's advisory and postmortem are the victim's own account of the timeline, the root cause and the
  impact counts, and StepSecurity analysed the payload independently; The Hacker News and
  CybersecurityNews restate StepSecurity.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-20.md
updates:
  - at: "2026-10-21T16:09:47Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Malicious Nx Console 18.95.0 was live from 12:30 to 12:48 UTC on the Visual Studio Marketplace and
      12:33 to 13:09 UTC on Open VSX, not in an 11-minute window, and was published with a core
      contributor's GitHub CLI token stolen in the TanStack npm compromise. The 2.2 million installs are
      the extension's total, against 28 Marketplace installs and about 6,000 activations of the bad
      version, and the analysis is rebuilt from Nx's advisory and postmortem with exposure, detection and
      takeaway guidance.
    fields: [affected_products, body, classification, entities, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title]
---

An attacker published Nx Console version 18.95.0 to the Visual Studio Marketplace at 12:30 UTC on 2026-05-18, where it stayed until 12:48 UTC, and to Open VSX from 12:33 to 13:09 UTC ([Nx GHSA-c9j4-9m59-847w, 2026-05-18](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w)); the Marketplace upload passed Microsoft's automated verification, and a maintainer caught it from the routine publisher-notification e-mail ([Nx, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). The attacker published as a legitimate core contributor whose GitHub CLI OAuth token had been exfiltrated seven days earlier by a credential stealer that arrived through the 2026-05-11 TanStack npm supply-chain compromise, and no approval gate stopped a single contributor from releasing ([Nx, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). The attacker had also planted an unsigned orphan commit in the nrwl/nx repository; the code injected into the extension runs when any workspace opens, fetches the 498 KB obfuscated payload from that commit ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised)) and installs the Bun JavaScript runtime to run it ([The Hacker News, 2026-05-19](https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html)). The payload harvests Vault, npm, AWS (including the instance and ECS metadata services), GitHub, 1Password and filesystem secrets, exfiltrates them over HTTPS, the GitHub API and DNS, writes a Python backdoor with a macOS LaunchAgent for persistence and on Linux attempts a sudoers change ([Nx, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)); the macOS backdoor takes commands signed with a 4096-bit RSA key through the GitHub Search API as a dead drop ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised)). Microsoft counts 28 Marketplace installs and Open VSX 41 downloads, while Nx's own analytics registered about 6,000 activations; the Nx CLI, the official plugins and Nx Cloud were not affected ([Nx, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)).

**Exposure:** Nx Console 18.95.0 exactly, in VS Code or a fork such as Cursor, on any machine that had the extension with auto-update enabled between 12:30 and 13:09 UTC on 2026-05-18; 18.100.0 and later are clean, and `code --list-extensions --show-versions` shows the installed version ([Nx, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)).

**Detection:** process lineage and file telemetry on developer machines: the extension's code launching a background task that runs `npx` against a package taken from a GitHub commit, a Bun runtime installed under the user profile, and a Python process running a script from a hidden directory under the user's `.local/share`, with a new LaunchAgent on macOS ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised)) ([Nx, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). On the source-control side the stolen token showed as workflow runs and bulk run deletions nobody made, which Nx says audit-log monitoring would have caught during the attacker's week in its repositories ([Nx, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). Updating the extension does not remove the backdoor or its persistence, which keep exfiltrating until they are killed and deleted ([Nx GHSA-c9j4-9m59-847w, 2026-05-18](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w)).

**Defender takeaway:** a machine that ran 18.95.0 is compromised: remove the persistence and rotate every credential reachable from it, tokens, secrets and SSH keys, then audit access logs for those accounts ([Nx GHSA-c9j4-9m59-847w, 2026-05-18](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w)). For teams that publish software, Nx's lesson is that any pipeline able to publish to a public registry must require approval gating ([Nx, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)).

## Correction — 2026-10-21T16:09:47Z

The malicious version was live on the Visual Studio Marketplace from 12:30 to 12:48 UTC and on Open VSX from 12:33 to 13:09 UTC ([Nx GHSA-c9j4-9m59-847w, 2026-05-18](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w)); 12:36 to 12:47 UTC is only the span from the maintainer's alert e-mail to the Marketplace unpublish, and Nx gives the exposure window as 12:30 to 13:09 UTC ([Nx, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). The publishing credential was a core contributor's GitHub CLI OAuth token, stolen a week earlier through the TanStack npm compromise ([Nx, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). The 2.2 million installs are the extension's total ([StepSecurity, 2026-05-18](https://www.stepsecurity.io/blog/nx-console-vs-code-extension-compromised)); only 18.95.0 was malicious, with 28 Marketplace installs by Microsoft's count and about 6,000 activations by Nx's, and the upload was not too short-lived to scan: it passed Microsoft's automated checks, basic malware scans included ([Nx, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)).
