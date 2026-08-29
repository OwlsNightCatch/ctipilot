---
schema: 1
kind: threat
title: "Mini Shai-Hulud's GitHub Actions Pwn-Request → OIDC Token Theft Chain"
headline: "Mini Shai-Hulud's GitHub Actions Pwn-Request → OIDC Token Theft Chain"
summary: Background. Mini Shai-Hulud (the TeamPCP self-propagating npm worm) first surfaced in coverage on 2026-05-10 as a SAP CAP-package compromise.
discovered_at: "2026-05-13T05:00:14Z"
event_date: 2026-05-12
run_id: 2026-05-13-c148b9a5
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - ai-abuse
  - organized-crime
regions:
  - global
sectors:
  - public-sector
  - technology
entities:
  - "campaign:mini-shai-hulud"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem"
    publisher: "StepSecurity, 2026-05-11"
    role: primary
  - url: "https://tanstack.com/blog/npm-supply-chain-compromise-postmortem"
    publisher: "TanStack post-mortem, 2026-05-12"
    role: corroborating
  - url: "https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised"
    publisher: "Wiz, 2026-05-12"
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12558"
    publisher: "NCSC-CH Security Hub #12558, 2026-05-12"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-13.md
---

**Background.** Mini Shai-Hulud (the TeamPCP self-propagating npm worm) first surfaced in coverage on [2026-05-10](/briefs/2026-05-10/) as a SAP CAP-package compromise. The original campaign relied on attacker-published versions of dependency-chain packages catching legitimate downstream consumers; its blast-radius was bounded by which packages opted into the affected dependency graph. The 2026-05-11 second wave ( materially changes the attack pattern — it uses no infostealer of a maintainer's machine, no credential theft from the package owner; instead it abuses a class problem in GitHub Actions that lets attacker-controlled fork code reach into the privileged release workflow of an upstream repository ([StepSecurity, 2026-05-11](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem); [TanStack post-mortem, 2026-05-12](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem); [Wiz, 2026-05-12](https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised)).

**The chain in defender terms.**

1. **Reconnaissance.** The operator (`voicproducoes`, GitHub account ID 269549300, created 2026-03-19) identifies a target repository whose CI/CD configuration triggers on `pull_request_target`. That event is the privileged form of `pull_request` — it runs in the *base repository's* context with secrets and write tokens available, not the fork's sandbox. GitHub's docs flag this; many high-volume monorepos still rely on it for fork-aware CI features. Mapped to `T1593 Search Open Websites/Domains` (the operator surveys public Actions configurations).
2. **Fork-and-rename.** The operator forks the target repo (e.g. `TanStack/router`) and immediately renames the fork (`zblgg/configuration`) to evade fork-list discovery — fork-list scans against the upstream do not surface a fork that has been renamed off the original namespace. Mapped to `T1583.001 Acquire Infrastructure: Domains`-equivalent for source-control identity.
3. **Pwn-Request.** The operator submits a PR from the renamed fork. The base repo's `pull_request_target` workflow executes, but with attacker-controlled code paths reached via subtle changes the human reviewer is unlikely to read (e.g. a modified `pnpm-lock.yaml`, a new dev-dependency, or a CI helper script under `.github/`). Mapped to `T1199 Trusted Relationship` and `T1505.003 Web Shell`-equivalent for CI execution. The PR does not need to be merged — its mere existence runs the privileged workflow.
4. **Cache poisoning.** The privileged workflow run, now executing attacker-influenced code with base-repo secrets, writes a malicious pnpm store into the GitHub Actions cache key for the project's lockfile hash. The cache key is shared with the legitimate release workflow, so the legitimate `pnpm install` in the next maintainer-merged release will restore the poisoned store rather than fetch upstream tarballs. Mapped to `T1195.002 Supply Chain Compromise: Compromise Software Supply Chain`.
5. **Wait for release.** Maintainers merge legitimate PRs to `main`. The release workflow on `main` restores the poisoned cache, builds the package using the trojanised pnpm store, and reaches the publish step.
6. **OIDC-token theft via `/proc/<pid>/mem`.** At this point the release runner has been issued a short-lived GitHub Actions OIDC token by GitHub's identity provider. The token sits in the workflow process's memory but is not surfaced as an environment variable to step scripts. The attacker-controlled binary inside the poisoned pnpm store reads `/proc/<runner-pid>/mem` to scrape the token directly out of process memory. Mapped to `T1003.007 OS Credential Dumping: Proc Filesystem`.
7. **npm token exchange.** The harvested OIDC token is exchanged at npm's well-known token-exchange endpoint for a per-package publish token. Because npm trusts the OIDC issuer (GitHub Actions identity), the token-exchange is a legitimate trust-federation operation — no audit signal at the npm side distinguishes it from a normal publish. The worm uses this short-lived publish token to upload poisoned versions of every package the OIDC scope can reach. Mapped to `T1078.004 Cloud Accounts` and `T1606.002 Forge Web Credentials: SAML Tokens`-equivalent for OIDC.
8. **Provenance fraud.** Because the poisoned tarball was built *inside* the legitimate GitHub Actions runner and published via the legitimate OIDC trust path, the npm registry signs the package with a **valid SLSA Build Level 3 provenance attestation**. The "Publish Packages" step in the maintainer's workflow YAML was bypassed entirely — the publish call came from the worm — but the attestation is cryptographically valid. This is the most significant evolution: SLSA L3 was the assurance many EU procurement frameworks were starting to demand; this campaign demonstrates it is forgeable when an attacker controls *any* step in the workflow chain that produces the artefact, not just the publish step. The closest MITRE ATT&CK fit is `T1553.002 Subvert Trust Controls: Code Signing` — though no current ATT&CK sub-technique precisely maps to SLSA-L3 provenance forgery via OIDC abuse in a CI pipeline; detection-engineering playbooks should be built from the CI-side primitives rather than from a generic code-signing detection rule.
9. **Payload & propagation.** Each poisoned package contains a 2.3 MB triple-obfuscated `router_init.js` that on `postinstall` harvests AWS IMDSv2, ECS metadata, HashiCorp Vault tokens, `~/.aws`, SSH keys, npm tokens, GitHub tokens, Kubernetes service accounts, browser cookie jars and 100+ further credential paths. Exfiltration is dual-channel: the Session Protocol (decentralised, takedown-resistant) with RSA-4096-OAEP + AES-256-GCM, and a GitHub GraphQL dead-drop that commits to attacker-controlled branches (Dune-universe names) authored as `claude@users.noreply.github.com`. Persistence is installed in Claude Code's `.claude/settings.json`, VS Code's `.vscode/tasks.json`, OS-level LaunchAgents and systemd units. A `gh-token-monitor` daemon polls the GitHub API every 60 seconds and executes `rm -rf ~/` if the harvested token is revoked — a dead-man's-switch wiper.
10. **Self-spread.** With the harvested npm tokens, the worm publishes further poisoned versions to every package each compromised maintainer can reach, repeating the chain.

**What detection looks like.** No IOCs in this brief; the behaviour patterns to alert on are the durable signals:
- **CI/CD telemetry:** any GitHub Actions workflow run triggered by `pull_request_target` that wrote to the Actions cache and was not initiated by a trusted contributor. The audit-log noise is high; pin the alert to "workflow-run accessed `actions/cache/save` from a job that was reachable via fork".
- **Runner-process introspection:** any step that reads from `/proc/*/mem` from a non-`root` process on the runner. GitHub-hosted runners do not need to read `/proc/<pid>/mem` for any legitimate workflow purpose. Self-hosted runners should treat the same heuristic as a high-severity alert (Sysmon-equivalent on the runner OS).
- **npm publish anomalies:** unusual concurrency of publish events for a package family that does not normally release simultaneously (TanStack 42 packages in a 6-minute window is the visible artefact). npm's audit log surfaces this if the org has it enabled.
- **Developer-workstation post-install:** processes spawned by `npm` / `pnpm` / `yarn` `postinstall` that read `~/.aws`, `~/.ssh`, `~/.npmrc` or `/proc/self/environ` (Sysmon EID 1 with parent-image filter on the package-manager binary).
- **Dead-man's-switch awareness:** **do not revoke a suspected-compromised GitHub PAT or npm token from the affected developer machine before quarantining that machine.** Revocation triggers `rm -rf ~/`. Quarantine first; rotate from a clean host.

**Hardening — class-level fixes, not per-incident patches.**
- Pin every `pull_request_target` workflow to a SHA-locked version of every action it uses; never `@main` or `@v1`. Forks cannot influence what runs.
- Disable cache writes from any workflow that can be reached via a fork PR (`actions/cache` with `save: false` from `pull_request_target`).
- Use **separate workflows** for fork-reachable CI (sandboxed, read-only on secrets) and for release (no fork-reachable trigger).
- Audit the OIDC trust chain in your npm / PyPI / GitHub-Container-Registry organisation: scope publish trust to a specific repo *and* a specific workflow file path, not just the repo.
- For SLSA-attestation reliance: treat L3 as a *necessary* but not *sufficient* signal — pair it with a maintainer-verified `npm provenance verify` against a published expected workflow-file-path, not just the issuer. The 2026-05-11 campaign shows L3 alone is forgeable.
- Sanitise developer endpoints before token revocation (the `rm -rf ~/` dead-man's-switch). Treat any pnpm cache restore or `node_modules` directory pre-dating the disclosure as suspect.
