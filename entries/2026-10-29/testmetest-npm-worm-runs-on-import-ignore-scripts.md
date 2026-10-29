---
schema: 1
kind: threat
title: "testmetest: an npm worm in the Miasma and Shai-Hulud family now starts when an application imports the package, so install with --ignore-scripts no longer protects, and JFrog finds 42 third-party GitHub repositories already armed with its publisher"
headline: "SafeDep and JFrog: the testmetest npm worm now runs on import, so --ignore-scripts does not stop it; 42 repos armed"
summary: >
  SafeDep and JFrog describe an npm worm, tracked as testmetest, whose newest builds start when an application imports the package, so installing with --ignore-scripts does not stop it. It steals
  SSH, registry, cloud, CI and AI-tool credentials, publishes new patch versions of the victim's own packages, and wipes the home directory when the stolen GitHub token is revoked. SafeDep
  counts 19 packages from one operator between 2026-10-19 and 2026-10-27; JFrog found 42 armed GitHub repositories of 11 legitimate owners; neither lab names an actor.
discovered_at: "2026-10-29T04:47:00Z"
updated_at: null
event_date: "2026-10-27"
run_id: 2026-10-29T0255Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, wiper]
regions: [global]
sectors: [technology]
entities: ["campaign:testmetest-npm-worm-2026-10", "campaign:miasma-redhat-npm-supply-chain", "campaign:mini-shai-hulud", "product:npm", "product:gitlab-ci"]
techniques: [T1195.002, T1059.007, T1552.001, T1567.001, T1485, T1027, T1497.001]
affected_products: ["npm", "GitHub Actions", "GitLab CI"]
cves: []
sources:
  - url: "https://safedep.io/testmetest-npm-worm-miasma-variant"
    publisher: "SafeDep (living post, updated 2026-10-27)"
    date: "2026-10-27"
    role: primary
  - url: "https://research.jfrog.com/post/beyond-testmetest-42-hijacked-github-repos/"
    publisher: "JFrog Security Research"
    date: "2026-10-26"
    role: primary
closed_sources: []
evidence:
  - quote: "Any application that imports the package starts the worm."
    publisher: "SafeDep (living post, updated 2026-10-27)"
    source_url: "https://safedep.io/testmetest-npm-worm-miasma-variant"
  - quote: "The malicious versions steal credentials, spread to other packages and repositories, and install a wiper that deletes the home directory when the victim revokes the stolen GitHub token."
    publisher: "SafeDep (living post, updated 2026-10-27)"
    source_url: "https://safedep.io/testmetest-npm-worm-miasma-variant"
  - quote: "The payload blobs were large enough to evade the GitHub search and API paths normally used to find this kind of compromise."
    publisher: "JFrog Security Research"
    source_url: "https://research.jfrog.com/post/beyond-testmetest-42-hijacked-github-repos/"
  - quote: "SafeDep has not confirmed its exact lineage."
    publisher: "SafeDep (living post, updated 2026-10-27)"
    source_url: "https://safedep.io/testmetest-npm-worm-miasma-variant"
verification: multi-source
sourcing_note: >
  SafeDep and JFrog analysed the campaign separately and agree on the loader and payload; SafeDep reported no compromised third-party packages as of 2026-10-22, while JFrog found armed repositories
  of real owners. Neither confirms a link to the original Miasma operators, and the sharing of code with the June Miasma worm and the Mini Shai-Hulud wiper is SafeDep's observation. Package
  names, account names and domains are not carried here; SafeDep's post lists them.
confidence: high
references: ["2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Compare every lockfile and CI cache against the package list in SafeDep's post; on each host that installed or imported a listed package, disconnect it, remove persistence first and only then rotate the GitHub, npm, cloud and SSH credentials it could read, because the worm wipes the home directory when the stolen GitHub token is revoked."
updates: []
migrated_from: null
---

SafeDep counts 19 npm packages from the same operator between 2026-10-19 and 2026-10-27, eight of them published through four npm accounts, that carry a worm sharing code with the June Miasma worm and adding the token-revocation wiper of Mini Shai-Hulud; SafeDep has not confirmed the lineage, and JFrog says its evidence does not establish that the original Miasma operators are responsible ([SafeDep, 2026-10-27](https://safedep.io/testmetest-npm-worm-miasma-variant); [JFrog Security Research, 2026-10-26](https://research.jfrog.com/post/beyond-testmetest-42-hijacked-github-repos/)). The install trigger has changed twice: first a command expansion in a binding.gyp file, with no install script; then a postinstall script that loads a native addon which decodes and starts the worm; and, since SafeDep's update of 27 October, an addon that runs when an application imports the package, so a hardening step that disables install scripts does not stop it ([SafeDep, 2026-10-27](https://safedep.io/testmetest-npm-worm-miasma-variant)).

The payload exits on CIS locales and in known analysis sandboxes. It steals SSH keys, registry and Git credentials, .env files, browser logins, AI-tool, cloud, Vault and Kubernetes secrets and GitHub Actions secrets read from runner memory ([SafeDep, 2026-10-27](https://safedep.io/testmetest-npm-worm-miasma-variant)). It exfiltrates by committing encrypted data, with the victim's encrypted GitHub token, to a new public repository in the victim's own account, injects a GitLab CI job that requests npm and PyPI OIDC tokens, adds its loader to the victim's npm packages and publishes new patch versions, republishes to PyPI and RubyGems, commits a fake CodeQL workflow and AI-agent configuration files that infect the host again, and copies itself over SSH to the hosts in known_hosts ([SafeDep, 2026-10-27](https://safedep.io/testmetest-npm-worm-miasma-variant)). A persistence service checks the stolen GitHub token every 45 seconds for 48 hours and on an authentication failure deletes the home directory ([SafeDep, 2026-10-27](https://safedep.io/testmetest-npm-worm-miasma-variant)). JFrog found 42 armed third-party GitHub repositories of 11 legitimate owners with hooks for AI coding assistants and IDEs, and says the payload blobs were large enough to evade GitHub's search and API paths ([JFrog Security Research, 2026-10-26](https://research.jfrog.com/post/beyond-testmetest-42-hijacked-github-repos/)).

**Exposure:** any developer endpoint, build agent or CI runner that installed or imported one of the operator's packages, and any GitHub or GitLab account whose token such a host held ([SafeDep, 2026-10-27](https://safedep.io/testmetest-npm-worm-miasma-variant)).

**Detection:** in package metadata, a binding.gyp whose sources field runs node in a package with no C or C++ sources, a postinstall that requires a .node file and discards errors beside a large high-entropy file, and prebuilt addons with no native source; on endpoints and CI runners, a node process that downloads or finds and runs the Bun runtime and a child node process started from a temporary path named after its process ID; in GitHub and GitLab audit logs, a new public repository in a developer's own account with a generic project description, commits with a fixed automated-sync message, commits that add AI-assistant configuration files (.claude, .cursor, .gemini, .vscode tasks, CLAUDE.md or AGENTS.md), an injected CI job that requests OIDC tokens, and unexpected patch releases of your own packages ([SafeDep, 2026-10-27](https://safedep.io/testmetest-npm-worm-miasma-variant)).

**Defender takeaway:** an install that ran with scripts disabled is not clean once the package has been imported; for an affected host SafeDep's order is to disconnect it, remove persistence first, rotate all credentials, check the accounts for the repositories and commits above and reinstall the operating system ([SafeDep, 2026-10-27](https://safedep.io/testmetest-npm-worm-miasma-variant)). Because the wiper is triggered by the token's revocation, the host is isolated and cleaned before the GitHub token is revoked.
