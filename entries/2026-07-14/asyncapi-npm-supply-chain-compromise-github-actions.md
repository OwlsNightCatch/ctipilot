---
schema: 1
kind: incident
horizon: operational
title: "AsyncAPI npm packages backdoored via a GitHub Actions pull_request_target token theft, delivering a multi-stage IPFS implant (M-RED-TEAM)"
headline: "Attacker abuses an AsyncAPI GitHub Actions pwn-request to steal a publish token and backdoor five @asyncapi npm versions with a multi-stage implant"
summary: >
  On 2026-07-14 an attacker abused a misconfigured pull_request_target GitHub Actions workflow in the
  asyncapi/generator repository to steal the AsyncAPI org's npm/service-account token and publish five
  trojanized @asyncapi package versions (generator, generator-helpers, generator-components, specs —
  together over three million downloads a week). On import the packages fetch a multi-stage IPFS-hosted
  implant that self-identifies as "M-RED-TEAM v6.4", persists, and reaches multi-channel command-and-control.
  Any CI/CD pipeline or developer host that imported an affected version should treat it as compromised
  and rotate exposed credentials.
discovered_at: "2026-07-14T12:38:00Z"
event_date: "2026-07-14"
run_id: 2026-07-14T1210Z-intel
priority: high
immediate_action: null
tags: [supply-chain, infostealer, identity]
regions: [global]
sectors: [technology, public-sector, finance]
entities: [incident:asyncapi-npm-github-actions-supply-chain-compromise-2026-07, tool:m-red-team-malware-framework, campaign:prt-scan-github-actions-pwn-request-token-theft]
techniques: [T1195.002, T1528, T1059.007, T1105, T1543.002, T1027, T1071.001]
affected_products: ["@asyncapi/generator", "@asyncapi/generator-helpers", "@asyncapi/generator-components", "@asyncapi/specs"]
cves: []
sources:
  - url: "https://www.wiz.io/blog/m-red-team-asyncapi-supply-chain-compromise-via-github-actions"
    publisher: "Wiz"
    date: "2026-07-14"
    role: primary
  - url: "https://safedep.io/asyncapi-generator-supply-chain-attack-miasma-rat/"
    publisher: "SafeDep"
    date: "2026-07-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "On July 14, 2026, an attacker opened 37 pull requests to the AsyncAPI generator repository. Almost all attempted to add a fake charity donation page."
    publisher: "Wiz"
  - quote: "The payload executes on import/require, not install."
    publisher: "Wiz"
  - quote: "The payload includes credential theft capabilities targeting browser saved passwords and cookies (Chrome, Brave, Firefox, Edge), SSH keys, npm and GitHub tokens, AWS credentials, macOS Keychain, and cryptocurrency wallets."
    publisher: "Wiz"
  - quote: "This is either a private, parallel build by the same operators or a separate group that adopted the Miasma brand after the source was published."
    publisher: "SafeDep"
verification: multi-source
sourcing_note: "Two independent same-day primary sources corroborate the core compromise — Wiz (the anchor analysis, which names the implant 'M-RED-TEAM v6.4' from its code comments) and SafeDep (which tracks the same incident, confirming the identical package/version set and the 06:58 UTC malicious commit) — so this entry is multi-source. The two disagree on the payload's self-identifying string: Wiz reports 'M-RED-TEAM v6.4', SafeDep reports 'miasma-train-p1', and SafeDep frames the Miasma-brand link more directly (a possible parallel build by the same operators) than Wiz's 'minimal resemblance' hedge — surfaced in the body so a hunting team searching code comments checks both strings. Aikido Security also reported the compromise independently but is not cited because the publisher renamed the post and its client-rendered blog would not resolve to a live URL this run. Neither cited source makes a definitive attribution; the credential-theft module's capabilities are documented but not stated to be active in this build, so this entry treats them as present-and-assume-compromise rather than confirmed mass theft."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Inventory CI/CD pipelines and developer hosts for imports of @asyncapi/generator 3.3.1, @asyncapi/generator-helpers 1.1.1, @asyncapi/generator-components 0.7.1, @asyncapi/specs 6.11.2 or 6.11.2-alpha.1 published on 2026-07-14; downgrade to the immediately preceding releases (3.3.0 / 1.1.0 / 0.7.0 / 6.11.1) and, where any affected version was imported, rotate npm, GitHub, cloud (AWS) and SSH credentials from a clean host — the implant runs on import, not install."
migrated_from: null
---

On 2026-07-14 an attacker compromised the `asyncapi/generator` GitHub repository by abusing a `pull_request_target` workflow that checked out the pull request's own code while still running "in the context of the base repository with full access to secrets" ([Wiz, 2026-07-14](https://www.wiz.io/blog/m-red-team-asyncapi-supply-chain-compromise-via-github-actions)). The attacker opened 37 pull requests — almost all a decoy adding a fake charity-donation page — while a single one (PR #2155, 05:08 UTC) carried obfuscated JavaScript that scanned the Actions runner environment for secrets and exfiltrated them to a paste-site dead drop, capturing the token of `asyncapi-bot`, a service account with organization-wide access; by 06:58 UTC the attacker pushed a malicious commit to the `next` branch and from 07:10 UTC the release workflow published five trojanized versions across four packages — `@asyncapi/generator` 3.3.1, `@asyncapi/generator-helpers` 1.1.1, `@asyncapi/generator-components` 0.7.1, and `@asyncapi/specs` 6.11.2 and 6.11.2-alpha.1 — which "combined, these packages see over three million downloads a week" ([Wiz, 2026-07-14](https://www.wiz.io/blog/m-red-team-asyncapi-supply-chain-compromise-via-github-actions)). A contributor had opened a fix for the vulnerable workflow on 2026-05-17; it was still unmerged 58 days later when the attack landed.

The injected code executes on `import`/`require`, not at install time: it spawns a detached Node child process that downloads a later stage from IPFS into a per-user application-support directory, then runs an encrypted multi-stage bundle whose runtime "explicitly self-identifies as 'M-RED-TEAM v6.4' in code comments" ([Wiz, 2026-07-14](https://www.wiz.io/blog/m-red-team-asyncapi-supply-chain-compromise-via-github-actions)). It establishes persistence via a systemd user service on Linux (with platform-specific equivalents on macOS and Windows) and beacons over multiple command-and-control channels — HTTP, Nostr relays, Ethereum smart contracts, and a libp2p mesh — accepting remote commands for file operations, directory listing and data exfiltration; its obfuscation uses `javascript-obfuscator` with a custom base64 alphabet matching prior incidents. The bundle carries credential-theft capabilities targeting saved browser passwords and cookies, SSH keys, npm and GitHub tokens, AWS credentials, the macOS Keychain and crypto wallets. Wiz notes technical fingerprints overlapping the Miasma framework (a `miasma`-branded persistence service and relay tags) and a dead-drop naming pattern matching the separately-tracked prt-scan pull-request-abuse campaign, but states that "beyond the references and initial obfuscation method the payload contains minimal resemblance to previous Miasma and Shai-Hulud payloads" and that "at this time, we are not making any definitive attribution." SafeDep, tracking the same incident, reports the payload self-identifying as `miasma-train-p1` rather than Wiz's `M-RED-TEAM v6.4` and frames the Miasma link more directly — "this is either a private, parallel build by the same operators or a separate group that adopted the Miasma brand after the source was published" ([SafeDep, 2026-07-14](https://safedep.io/asyncapi-generator-supply-chain-attack-miasma-rat/)); a team hunting code-comment strings should check for both identifiers.

**Defender takeaway.** This is a recurring 2026 pattern of `pull_request_target` "pwn request" abuse feeding npm-ecosystem backdoors, and the load-bearing control gap is a CI/CD one: any workflow that triggers on `pull_request_target` and then checks out untrusted PR code runs attacker code with access to repository secrets. Audit your own Actions workflows for that pattern, and — because the payload runs on import rather than install — a `--ignore-scripts` install policy does not neutralise it; only pinning to known-good versions and rebuilding from a clean state does.

**Triage:** a legitimate `require()` of AsyncAPI tooling performs no runtime network activity; the signal is a detached Node child process spawned from an `npm`/`node` parent at import time that reaches out to an IPFS gateway or a peer-to-peer mesh and then creates a user-level persistence service — process-lineage telemetry (a script interpreter spawning a hidden detached child with outbound egress) plus a new systemd/user-service artifact created outside a package-manager transaction is the discriminator, since benign build tooling produces neither.
