---
schema: 1
kind: threat
title: "Mini Shai-Hulud hits TanStack: a pull_request_target Pwn Request, Actions cache poisoning and OIDC token theft from runner memory published 84 malicious @tanstack versions with valid provenance"
headline: "A Pwn Request, cache poisoning and runner-memory OIDC theft let attackers publish 84 malicious TanStack npm versions"
summary: "On 2026-05-11 between 19:20 and 19:26 UTC an attacker published 84 malicious versions of 42 @tanstack/* npm packages through TanStack's own release workflow by chaining a pull_request_target Pwn Request, GitHub Actions cache poisoning and extraction of the workflow's OIDC token from runner memory; no npm token was stolen (TanStack). The install-time payload steals cloud, GitHub, npm and SSH credentials, spreads to its victims' other packages and plants a service that wipes the home directory when the stolen token is revoked (StepSecurity, NCSC-CH). The compromise is CVE-2026-45321 (CVSS 9.6), in CISA's KEV catalog since 2026-05-27."
discovered_at: "2026-05-13T05:00:14Z"
event_date: 2026-05-11
run_id: 2026-05-13-c148b9a5
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - wiper
  - organized-crime
  - cloud
  - cisa-kev
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:mini-shai-hulud"
  - "actor:teampcp"
techniques: [T1190, T1195.001, T1195.002, T1059.007, T1105, T1027, T1003.007, T1528, T1550.001, T1552.001, T1552.005, T1567, T1567.001, T1546, T1543.001, T1543.002, T1036, T1485]
affected_products: ["TanStack Router", "TanStack Start"]
cves:
  - id: CVE-2026-45321
    cvss: "9.6"
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
    affected: "84 versions of 42 @tanstack/* packages published 2026-05-11 19:20 to 19:26 UTC"
    fixed: "all currently published @tanstack/* versions (the malicious versions were deprecated and removed)"
sources:
  - url: "https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem"
    publisher: "StepSecurity"
    date: "2026-05-11"
    role: primary
  - url: "https://tanstack.com/blog/npm-supply-chain-compromise-postmortem"
    publisher: "TanStack"
    date: "2026-05-11"
    role: primary
  - url: "https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx"
    publisher: "TanStack (GitHub Security Advisory)"
    date: "2026-05-11"
    role: primary
  - url: "https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised"
    publisher: "Wiz"
    date: "2026-05-12"
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12558"
    publisher: "NCSC-CH Security Hub"
    date: "2026-05-12"
    role: corroborating
  - url: "https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages/"
    publisher: "The Register"
    date: "2026-04-30"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV catalog"
    date: "2026-05-27"
    role: corroborating
  - url: "https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/"
    publisher: "GitHub Security Lab"
    date: "2021-08-03"
    role: corroborating
  - url: "https://github.com/actions/cache"
    publisher: "GitHub (actions/cache README)"
    date: null
    role: corroborating
  - url: "https://docs.npmjs.com/generating-provenance-statements"
    publisher: "npm Docs"
    date: null
    role: corroborating
closed_sources: []
evidence:
  - quote: "No npm tokens were stolen and the npm publish workflow itself was not compromised."
    publisher: TanStack
    source_url: "https://tanstack.com/blog/npm-supply-chain-compromise-postmortem"
  - quote: "Cache writes use a runner-internal token"
    publisher: TanStack
    source_url: "https://tanstack.com/blog/npm-supply-chain-compromise-postmortem"
  - quote: "Yet the packages were published during the same window."
    publisher: StepSecurity
    source_url: "https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem"
  - quote: "A compromised build step can produce a validly-attested but malicious package."
    publisher: StepSecurity
    source_url: "https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem"
  - quote: "Do not revoke these tokens before isolating and imaging the machine"
    publisher: StepSecurity
    source_url: "https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem"
  - quote: "On April 29, TeamPCP compromised four official npm packages from the SAP JavaScript and cloud application development ecosystem and published the poisoned releases between 09:55 and 12:14 UTC."
    publisher: The Register
    source_url: "https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages/"
verification: multi-source
sourcing_note: >
  TanStack's post-mortem and advisory are the primary account of the intrusion chain; StepSecurity, which detected the
  publishes, analysed the payload, and Wiz and NCSC-CH independently describe the same wave. The TeamPCP attribution is
  StepSecurity's and Wiz's; TanStack does not attribute the attack.
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-13.md
updated_at: null
updates:
  - at: "2026-10-21T16:08:09Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Mini Shai-Hulud first hit official SAP npm packages on 2026-04-29, and in the TanStack compromise of
      2026-05-11 the fork pull request added a payload file that the pull_request_target benchmark job
      built; the release job's own publish step was skipped while the malware published directly with the
      OIDC token it read from runner memory. The provenance on the malicious packages is genuine rather
      than forged, the payload runs from a prepare script of an optional git dependency and its memory
      scraper runs under sudo. The compromise is CVE-2026-45321, scored 9.6 and in CISA's KEV catalog
      since 2026-05-27, and the restore-only cache action and npm audit signatures replace a cache option
      and a command that do not exist.
    fields: [affected_products, body, classification, cves, event_date, evidence, headline, sectors, sources, sourcing_note, summary, tags, techniques, title]
---

On 2026-05-11 between 19:20 and 19:26 UTC an attacker published 84 malicious versions across 42 @tanstack/* npm packages by chaining a `pull_request_target` "Pwn Request", GitHub Actions cache poisoning across the fork and base-repository trust boundary, and extraction of an OIDC token from the runner's memory; no npm token was stolen and the publish workflow itself was not modified ([TanStack, 2026-05-11](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)). StepSecurity, which detected the publishes, and Wiz attribute the wave to TeamPCP's Mini Shai-Hulud worm, which hit UiPath, Mistral AI and other npm packages the same day, though Wiz found a payload bug that leaves the malware non-functional in the @uipath and @mistralai packages ([StepSecurity, 2026-05-11](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem); [Wiz, 2026-05-12](https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised)). The worm's first wave had compromised four official SAP npm packages on 2026-04-29 through malicious preinstall scripts ([The Register, 2026-04-30](https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages/)). The TanStack compromise is CVE-2026-45321, scored 9.6 ([TanStack advisory, 2026-05-11](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx)), which CISA added to its Known Exploited Vulnerabilities catalog on 2026-05-27 with known ransomware campaign use ([CISA KEV catalog, 2026-05-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

**The chain, from TanStack's timeline** ([TanStack, 2026-05-11](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)):

1. **Staging.** On 2026-05-10 the attacker forked TanStack/router into a repository renamed to evade fork-list searches and committed a roughly 30,000-line bundled JavaScript payload under the history package, with a fabricated author identity and a commit message that suppressed CI on push; the post-mortem names two attacker GitHub accounts.
2. **Pwn Request.** On 2026-05-11 at about 10:49 a pull request titled as a work-in-progress build simplification triggered the bundle-size and labeler workflows, both on `pull_request_target`, which needs no first-time-contributor approval. At 11:11 the benchmark job checked out the PR's merge ref and ran `pnpm install` and the bundle-size build, executing the payload.
3. **Cache poisoning.** The payload wrote into the pnpm store under the key the release workflow computes, and the cache action's post-job save stored the 1.1 GB poisoned store in the base repository's cache scope; the job's read-only `permissions:` did not stop it, because cache writes use a runner-internal token. At 11:31 the attacker force-pushed the PR back to the main branch head, leaving a zero-file change, and closed it.
4. **Detonation.** At 19:15 a re-run of the release workflow, and at 19:16 a fresh run triggered by a legitimate merge, restored the poisoned store. Attacker binaries run during the build located the Runner.Worker process, read its memory through `/proc/<pid>/maps` and `/proc/<pid>/mem`, took the OIDC token the runner mints in memory for a job with `id-token: write`, and posted the packages directly to the npm registry, using the same memory-dump script as the tj-actions/changed-files compromise of March 2025. Tests failed, so the workflow's own Publish Packages step was skipped.

The packages carry valid SLSA provenance tied to TanStack's release workflow; provenance proves which pipeline built a package, not that the pipeline behaved, so a compromised build step yields a validly attested malicious package ([StepSecurity, 2026-05-11](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)).

**The payload.** Installing an affected version resolves an optional dependency on a `github:` URL naming the TanStack repository, which GitHub serves from an orphan commit in the fork network; npm installs that commit's dependencies, including the Bun runtime, and runs its `prepare` lifecycle script, which executes a 2.3 MB obfuscated JavaScript file shipped at the tarball root and then exits with an error so npm silently discards the optional install ([TanStack advisory, 2026-05-11](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx)). Behind three obfuscation layers, it queries the AWS instance metadata service with the IMDSv2 flow and the ECS credential endpoint, reads the local Vault agent, reads files from more than 100 hardcoded paths, and in CI pipes a memory-reading script to `sudo python3` to pull every value the runner marks as secret ([StepSecurity, 2026-05-11](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)); NCSC-CH groups the paths as cloud credentials, SSH, Git, developer and AI tools, crypto wallets, VPN configurations, messaging apps, shell history and Kubernetes ([NCSC-CH, 2026-05-12](https://security-hub.ncsc.admin.ch/#/posts/12558)). It exfiltrates encrypted data through the Session messenger's file-upload network and through GitHub commits on branches named to look like Dependabot's, spreads by finding npm tokens that bypass two-factor checks, enumerating the maintainer's other packages and, in CI, exchanging the OIDC token for per-package publish tokens, and writes workflows disguised as CodeQL analysis that serialise all repository secrets ([StepSecurity, 2026-05-11](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)). Persistence is a Claude Code SessionStart hook, a VS Code folder-open task, and a LaunchAgent on macOS or systemd user service on Linux that checks the GitHub API every 60 seconds and deletes the user's home directory once the stolen token is revoked ([NCSC-CH, 2026-05-12](https://security-hub.ncsc.admin.ch/#/posts/12558)).

**Exposure:** any developer machine or CI runner that ran `npm install`, `pnpm install` or `yarn install` against an affected version on 2026-05-11 ([TanStack advisory, 2026-05-11](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx)). For maintainers, the same chain is open wherever a `pull_request_target` workflow checks out and builds fork code in a cache scope that a release job with `id-token: write` later restores ([TanStack, 2026-05-11](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)).

**Detection:** in package manifests and tarballs, an optional dependency on a `github:` URL pinned to a commit and a large JavaScript file at the package root that the `files` list does not declare; in runner process telemetry, the Bun runtime installed during `npm install` and `python3` processes reading `/proc/*/mem`; in registry and repository history, two versions of one package published minutes apart and unexpected commits on Dependabot-style branches ([StepSecurity, 2026-05-11](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)). TanStack names publishes that do not come from the workflow's defined publish step as the signal to watch for ([TanStack, 2026-05-11](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)). On hosts, added Claude Code hooks, VS Code folder-open tasks and a token-monitoring LaunchAgent or systemd user service ([NCSC-CH, 2026-05-12](https://security-hub.ncsc.admin.ch/#/posts/12558)).

**Defender takeaway:** on any host that installed an affected version, isolate and image the machine before revoking any token, because revocation triggers the wipe ([StepSecurity, 2026-05-11](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)), then rotate the AWS, GCP, Kubernetes, Vault, GitHub, npm and SSH credentials reachable from it ([TanStack, 2026-05-11](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)). For repositories, never check out or build an untrusted pull request under `pull_request_target` ([GitHub Security Lab, 2021-08-03](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/)); where a fork-reachable job needs a cache, use the separate restore action, which has no save step ([actions/cache README](https://github.com/actions/cache)); and treat `npm audit signatures` as proof of which pipeline built a package, not that it was clean ([npm Docs](https://docs.npmjs.com/generating-provenance-statements); [StepSecurity, 2026-05-11](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)).

## Correction — 2026-10-21T16:08:09Z

Mini Shai-Hulud's first wave hit four official SAP npm packages on 2026-04-29 with malicious preinstall scripts ([The Register, 2026-04-30](https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages/)). In the TanStack compromise no reconnaissance step is reported; the pull request added a bundled payload file that the `pull_request_target` benchmark job executed when it checked out and built the PR's merge ref, rather than slipping in lockfile, dependency or `.github` changes, and the release job never reached its publish step: tests failed, Publish Packages was skipped, and the malware published directly with the OIDC token it read from runner memory ([TanStack, 2026-05-11](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)). No npm token was needed for that publish, but the payload itself steals credentials and spreads with them ([StepSecurity, 2026-05-11](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)).

The SLSA provenance on the malicious packages is genuine, an attestation of a compromised pipeline rather than a forgery, and no source ties it to EU procurement ([StepSecurity, 2026-05-11](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)). The payload runs from the `prepare` script of an optional git dependency, not from `postinstall` ([TanStack advisory, 2026-05-11](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx)), and its memory scraper runs as `sudo python3`, so a filter for non-root readers of `/proc/<pid>/mem` misses it ([StepSecurity, 2026-05-11](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)). The compromise is CVE-2026-45321, scored 9.6 ([TanStack advisory, 2026-05-11](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx)) and listed by CISA as known exploited on 2026-05-27 ([CISA KEV catalog, 2026-05-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). The cache action has no `save: false` input; restore-only caching is the separate restore action ([actions/cache README](https://github.com/actions/cache)), npm verifies attestations with `npm audit signatures` ([npm Docs](https://docs.npmjs.com/generating-provenance-statements)), and GitHub Security Lab warns that combining the `pull_request_target` trigger with an explicit checkout of an untrusted pull request may lead to repository compromise ([GitHub Security Lab, 2021-08-03](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/)).
