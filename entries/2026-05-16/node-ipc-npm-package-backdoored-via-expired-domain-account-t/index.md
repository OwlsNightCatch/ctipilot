---
schema: 1
kind: incident
title: "node-ipc npm package backdoored via expired-domain account takeover: three malicious versions steal developer and CI credentials, flagged about three minutes after publication"
headline: "node-ipc npm package backdoored via expired-domain maintainer takeover: three malicious versions steal developer and CI credentials on require()"
summary: "node-ipc npm package (widely-used Node.js IPC library) hijacked via expired-domain account takeover; three malicious versions (9.1.6, 9.2.3, 12.0.1) exfiltrate cloud, CI/CD, SSH and Keychain credentials over DNS TXT (StepSecurity also reports an HTTPS channel that Socket did not find); rotate every secret on any workstation or CI runner that loaded one of the three versions (Socket Security, 2026-05-14 · StepSecurity, 2026-05-14)."
discovered_at: "2026-05-16T05:00:02Z"
event_date: 2026-05-14
run_id: 2026-05-16-5bc123a0
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - identity
  - data-breach
regions:
  - global
sectors:
  - technology
entities: []
techniques: [T1583.001, T1195, T1195.002, T1027, T1083, T1552.001, T1555, T1048, T1048.003]
cves: []
sources:
  - url: "https://socket.dev/blog/node-ipc-package-compromised"
    publisher: "Socket Security, 2026-05-14"
    role: primary
  - url: "https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack"
    publisher: "StepSecurity, 2026-05-14"
    role: corroborating
  - url: "https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html"
    publisher: "The Hacker News, 2026-05-14"
    role: corroborating
  - url: "https://www.csoonline.com/article/4171926/expired-domain-leads-to-supply-chain-attack-on-node-ipc-npm-package.html"
    publisher: "CSO Online, 2026-05-14"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
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
actions: []
migrated_from: briefs/2026-05-16.md
updates:
  - at: "2026-09-30T06:54:42Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Unsourced claims are removed: a named registrar, Vue CLI and webpack dependents, registry
      removal of the versions and an npm audit bypass, along with advice to run npm ci with scripts
      disabled, which does not stop a payload that fires on require(). The conflicting payload
      descriptions of Socket and StepSecurity are stated as a contradiction, so the title no longer
      asserts StepSecurity's pattern count. An attacker-controlled domain, the exfiltration DNS
      suffix, the maintainer email domain and account name and inline ATT&CK ids are removed, the
      truncated headline is rewritten, and the entry gains an ATT&CK mapping.
    fields: [body, classification, techniques, headline, summary, title]
---

On 2026-05-14, three malicious versions of the `node-ipc` npm package (9.1.6, 9.2.3 and 12.0.1) were published at the same time by a co-maintainer account with no prior publish history on the package ([StepSecurity, 2026-05-14](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack)). The account's email domain had expired on 2025-01-10 and was re-registered on 2026-05-07, a week before the attack ([The Hacker News, 2026-05-14](https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html)). Socket assesses that the new domain owner could then trigger a standard npm password reset and gain publish rights without touching the maintainer's own infrastructure ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised)). CSO counts almost 700K weekly downloads and 424 dependent projects, while StepSecurity reports over 10 million weekly downloads ([CSO Online, 2026-05-14](https://www.csoonline.com/article/4171926/expired-domain-leads-to-supply-chain-attack-on-node-ipc-npm-package.html) · [StepSecurity, 2026-05-14](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack)). The 9.x releases are fabricated from the 12.x package structure, so projects on `^9`, `~9.1.x`, `~9.2.x`, `^12` or `~12.0` ranges received a malicious build on their next install or lockfile refresh ([StepSecurity, 2026-05-14](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack)). When StepSecurity published, npm's `latest` tag pointed to 12.0.1, so an unpinned `npm install node-ipc` pulled the compromised tarball ([StepSecurity, 2026-05-14](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack)).

The payload is an 80 KB obfuscated function appended to the CommonJS bundle `node-ipc.cjs`. It runs on every `require('node-ipc')` and uses no npm lifecycle hook, so tools that only scan `preinstall` and `postinstall` scripts miss it ([StepSecurity, 2026-05-14](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack)). ESM-only consumers do not load the malicious file unless another dependency or a direct require loads `node-ipc.cjs` ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised)). The payload forks a detached child Node process that collects cloud provider credentials, SSH keys, Kubernetes tokens, GitHub CLI configuration, Terraform state, CI workflow files, `.env` files, shell history and macOS Keychain databases, gzips them and exfiltrates them ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised) · [StepSecurity, 2026-05-14](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack)). Four stacked obfuscation layers (string-array shuffling, control-flow flattening, dead-code injection and a custom reversed-nibble base-16 encoding) resist static analysis ([StepSecurity, 2026-05-14](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack)). Socket found no persistence and no second-stage download, and its scanner flagged the publish within roughly three minutes ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised)).

**Contradiction:** the analyses disagree on payload details. StepSecurity and The Hacker News describe 90+ file-path patterns, an HTTPS POST channel alongside DNS TXT exfiltration, and a SHA-256 targeting gate that leaves 12.0.1 inert except on one targeted project ([StepSecurity, 2026-05-14](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack) · [The Hacker News, 2026-05-14](https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html)). Socket counts 113 macOS and 127 Linux patterns, says the payload uses DNS TXT queries and not HTTP, HTTPS or TLS for exfiltration, and finds the same malicious file in all three versions, with a hash gate that only changes what the module exports ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised)). Treat all three versions as active stealers.

**Detection:** the payload first resolves a lookalike Azure hostname through the public resolvers 1.1.1.1 or 8.8.8.8, then sends DNS TXT queries straight to the attacker's server acting as a resolver, so the traffic never reaches corporate resolver logs ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised) · [StepSecurity, 2026-05-14](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack)). Look for DNS traffic from developer machines or CI runners to non-corporate resolvers and for large bursts of TXT queries: Socket estimates a 500 KiB archive produces about 29,400 of them ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised)). On endpoints, the payload shows as a Node process spawning a detached child Node process that runs `node-ipc.cjs` directly ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised)).

**Exposure:** any project whose lockfile, build cache or local npm cache holds 9.1.6, 9.2.3 or 12.0.1 and loads the package through CommonJS, directly or transitively ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised)).

**Defender takeaway:** on any workstation or CI runner that loaded one of the three versions, remove it, reinstall a known clean version (9.2.1 or 12.0.0), and rotate every secret present on the host: SSH keys, npm, GitHub and GitLab tokens, cloud keys, and Kubernetes, Docker registry, Terraform and database credentials ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised) · [The Hacker News, 2026-05-14](https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html)). Review dependencies by their entrypoints rather than only their install scripts, and prefer short-lived, scoped credentials in development and CI ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised)).

## Correction — 2026-09-30T06:54:42Z

No source says the malicious versions were removed from the registry: when StepSecurity published, npm's `latest` tag pointed to the malicious 12.0.1 ([StepSecurity, 2026-05-14](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack)). The payload fires on `require()` and uses no install hook, so disabling install scripts in CI does not stop it. Socket's advice is to review dependencies by their entrypoints and to rotate every secret on an affected host ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised)). Socket and StepSecurity disagree on the exfiltration channels, the pattern count and whether 12.0.1 is gated to one target ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised) · [StepSecurity, 2026-05-14](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack)), and all three versions should be treated as active. The entry previously named a domain registrar and Vue CLI and webpack tooling as dependents, which no cited source states.
