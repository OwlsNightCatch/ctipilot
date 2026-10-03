---
schema: 1
kind: incident
title: "node-ipc npm package backdoored via expired-domain account takeover — 90+ credential categories exfiltrated, three malicious versions, ~3-minute window to detection"
headline: "node-ipc npm package backdoored via expired-domain account takeover — 90+ credential categories exfiltrated, three malicious versions, ~3-minute window to"
summary: "node-ipc npm package (widely-used Node.js IPC library) hijacked via expired-domain account takeover; three malicious versions (9.1.6, 9.2.3, 12.0.1) exfiltrate ~90 categories of cloud / CI/CD / SSH / Keychain credentials over DNS TXT and HTTPS to attacker C2; rotate any secret accessible from a workstation that installed the package on 2026-05-14 (Socket Security, 2026-05-14 · StepSecurity, 2026-05-14)."
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
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-16.md
---

On 2026-05-14, three malicious versions of the `node-ipc` npm package (versions 9.1.6, 9.2.3, and 12.0.1 — `node-ipc` is a widely-used Node.js IPC library, with [CSO Online](https://www.csoonline.com/article/4171926/expired-domain-leads-to-supply-chain-attack-on-node-ipc-npm-package.html) reporting approximately 700 K weekly downloads and inclusion as a transitive dependency in hundreds of projects including Vue CLI and various webpack tooling) were published simultaneously by the long-dormant maintainer account `atiertant`, whose registered email domain `atlantis-software.net` had expired in January 2025 and was re-registered by an attacker via Namecheap on 2026-05-07 ([Socket Security, 2026-05-14](https://socket.dev/blog/node-ipc-package-compromised) · [StepSecurity, 2026-05-14](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack) · [The Hacker News, 2026-05-14](https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html) · [CSO Online, 2026-05-14](https://www.csoonline.com/article/4171926/expired-domain-leads-to-supply-chain-attack-on-node-ipc-npm-package.html)). The attacker used the recovered domain to receive an npm password-reset email and then published the backdoored versions. The malicious payload is an 80 KB obfuscated Immediately-Invoked Function Expression appended to `node-ipc.cjs` (the CommonJS bundle); it fires unconditionally on every `require('node-ipc')` via `setImmediate()`, and notably **does not use an npm lifecycle hook** (`preinstall`, `postinstall`), which lets it bypass `npm audit` and conventional install-time scanning that only inspects lifecycle-script execution. Four-layer obfuscation (string-array shuffling, control-flow flattening, dead-code injection, custom reversed-nibble base-16 encoding) defeats static signature analysis. The collector enumerates approximately 90 file-path patterns covering AWS / Azure / GCP / OCI / DigitalOcean / Hetzner / Fly / Vercel credentials and configs, SSH private keys, Kubernetes service-account tokens, GitHub CLI configurations, npm and Git tokens, Terraform state, `.env` files, shell history, and macOS Keychain databases; data is GZIP-compressed then exfiltrated over two simultaneous channels — DNS TXT queries to the `bt.node.js` suffix and HTTPS POST to `sh.azurestaticprovider[.]net:443`. Version 12.0.1 carries an additional SHA-256 fingerprint check targeting specific high-value projects; the 9.x versions fire universally. The ESM entry point is unaffected. Socket's AI scanner flagged the publish within ~3 minutes; the malicious versions were removed from the registry shortly thereafter. MITRE ATT&CK: [T1195.002](https://attack.mitre.org/techniques/T1195/002/) Compromise Software Supply Chain, [T1555](https://attack.mitre.org/techniques/T1555/) Credentials from Password Stores, [T1048.003](https://attack.mitre.org/techniques/T1048/003/) Exfiltration Over Alternative Protocol (DNS), [T1083](https://attack.mitre.org/techniques/T1083/) File and Directory Discovery. Defender action: enumerate `node-ipc` installs (`npm ls node-ipc` across the build graph, including transitive); on any workstation or CI runner that installed one of the three flagged versions between 2026-05-14 publish time and registry removal, treat every secret available in the environment (cloud SDK profiles, SSH keys, npm / Git tokens, Kubernetes contexts) as compromised and rotate. Enforce `npm ci --ignore-scripts` in CI, pin via lockfile, and monitor for outbound DNS queries to `*.bt.node.js`.
