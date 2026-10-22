---
schema: 1
kind: threat
title: >
  CHAINDROP: the Shai-Hulud npm worm returns through the keyv maintainer, backdoors 400+
  packages, and resolves its exfiltration endpoint from an Ethereum smart contract
headline: >
  A self-propagating npm worm reaches packages totalling 1.3 billion monthly downloads, and its C2
  address lives on-chain
summary: >
  Elastic Security Labs identified CHAINDROP on 2026-08-04, a new wave of the Shai-Hulud npm worm
  that began with the compromise of the keyv maintainer and has backdoored over 400 npm packages
  whose combined reach Elastic puts at more than 1.3 billion monthly downloads, keyv alone at over
  600 million. Execution comes from a package.json preinstall hook that downloads the Bun runtime
  to run an obfuscated 711 KB payload, which harvests over 300 credential patterns (AI-assistant
  tokens, AWS/GCP/Azure/Alibaba credentials, GitHub tokens, Vault tokens, SSH keys and Kubernetes
  service-account tokens) and self-propagates only when it finds an npm token that both carries
  package-write permission and can publish without two-factor authentication. Rather than
  hardcoding a command-and-control domain, CHAINDROP queries an Ethereum smart contract at runtime
  to resolve where to send the stolen material, so the operator rotates infrastructure without
  shipping a new payload. On 2026-10-08 a release of the tensorlake npm SDK carried the same payload
  family with valid build provenance, and Socket and OX Security describe a dead-man switch that wipes
  the owner's home directory if the stolen GitHub token is revoked before its persistence is removed.
discovered_at: "2026-08-06T04:11:48Z"
updated_at: "2026-10-11T03:39:00Z"
event_date: 2026-08-04
run_id: 2026-08-06T0411Z-intel
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - actively-exploited
  - ai-abuse
  - cloud
regions:
  - global
sectors:
  - technology
  - public-sector
  - finance
  - telco
entities:
  - "campaign:shai-hulud-chaindrop-2026-08"
techniques:
  - T1195.002
  - T1059.007
  - T1546
  - T1552.001
  - T1027
  - T1568
  - T1567.001
  - T1119
  - T1195.001
  - T1552
  - T1528
  - T1102.001
  - T1053.005
  - T1543.002
  - T1543.001
  - T1485
  - T1552.005
affected_products:
  - npm
  - GitHub Actions
cves: []
sources:
  - url: "https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain"
    publisher: Elastic Security Labs
    date: 2026-08-06
    role: primary
  - url: "https://www.ox.security/blog/a-new-infostealer-worm-hits-npm-affecting-keyv-and-cacheable/"
    publisher: OX Security
    date: 2026-08-04
    role: corroborating
  - url: "https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/"
    publisher: Palo Alto Networks Unit 42
    date: 2026-08-06
    role: primary
  - url: "https://www.socket.dev/blog/tensorlake-compromise"
    publisher: Socket
    date: 2026-10-08
    role: corroborating
  - url: "https://www.endorlabs.com/learn/tensorlake-npm-package-compromised-by-shai-hulud-in-latest-software-supply-chain-attack"
    publisher: Endor Labs
    date: 2026-10-08
    role: corroborating
  - url: "https://www.ox.security/blog/shai-hulud-here-we-go-again-tensorlake-npm-package-hit-with-malware/"
    publisher: OX Security
    date: 2026-10-08
    role: corroborating
closed_sources: []
evidence:
  - quote: keyv alone received over 600 million downloads last month
    publisher: Elastic Security Labs
  - quote: Execution is triggered via a preinstall hook in package.json.
    publisher: Elastic Security Labs
  - quote: package write permissions and the ability to publish without two-factor authentication (bypass_2fa)
    publisher: Elastic Security Labs
  - quote: "CHAINDROP does not hardcode a C2 domain; instead, it queries an Ethereum smart contract"
    publisher: Elastic Security Labs
  - quote: A massive Shai-Hulud campaign hit npm
    publisher: OX Security
  - quote: "locates the Runner.Worker process on GitHub Actions runners, opens /proc/<pid>/maps and /proc/<pid>/mem, and searches live process memory for OpenID Connect (OIDC) tokens and runner secrets."
    publisher: Palo Alto Networks Unit 42
  - quote: "This is not forged provenance. The attestation says the tarball was built in that repository by that workflow, and that is true."
    publisher: Palo Alto Networks Unit 42
  - quote: "Pivot on the Rekor log index and the workflow identity inside the certificate, not on whether the signature checks out."
    publisher: Palo Alto Networks Unit 42
  - quote: "The malicious release shipped through the project's normal GitHub Actions pipeline and even carried valid build provenance."
    publisher: Endor Labs
    source_url: "https://www.endorlabs.com/learn/tensorlake-npm-package-compromised-by-shai-hulud-in-latest-software-supply-chain-attack"
  - quote: "Revoking the stolen GitHub token while the monitor is still running triggers the dead-man switch to wipe the user's home directory, regardless of where the revocation is done."
    publisher: Socket
    source_url: "https://www.socket.dev/blog/tensorlake-compromise"
verification: multi-source
sourcing_note: >
  Two vendors reported first-hand on the same campaign two days apart and their counts differ:
  Elastic gives over 400 compromised packages and over 1.3 billion combined monthly downloads, OX
  Security gives its own larger figures from its own telemetry. The 2026-10-08 tensorlake release is
  reported by Socket, Endor Labs and OX Security: Socket matches it to this wave's file structure, while OX Security notes new
  public keys that may point to an independent actor reusing the Shai-Hulud name.
confidence: high
references: []
deep_dive: true
deep_dive_category: supply-chain
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Audit every npm publish token your organisation and its maintainers hold and revoke any that can publish without two-factor authentication: that exact token property, not package popularity, is what decides whether the worm spreads from a compromised developer to your packages."
  - "On any developer workstation or build agent that installed a package from the keyv family since 2026-08-04, or tensorlake@0.5.144 since 2026-10-08, treat the AI-assistant, cloud, GitHub, Vault, SSH and Kubernetes credentials present on that host as disclosed and rotate them; the collector sweeps over 300 credential patterns in one pass, so partial rotation leaves the operator a working set. Isolate the host before revoking its GitHub token, because OX Security reports a switch that wipes the machine when the token is revoked; on a host that ran tensorlake@0.5.144, Socket and OX Security also name a token-monitor persistence (a systemd user unit on Linux, a LaunchAgent on macOS, a scheduled task on Windows), which has to be removed before the token is revoked."
  - "Stop treating a valid npm provenance attestation as evidence a package is clean; where release pipelines gate on provenance, change the check to pin on the workflow identity inside the Fulcio certificate and the Rekor log index, which is what Unit 42 says still discriminates."
updates:
  - at: "2026-08-08T04:53:00Z"
    run_id: 2026-08-08T0409Z-intel
    type: update
    summary: >
      Unit 42's analysis of CHAINDROP, the Shai-Hulud npm worm wave covered here on 2026-08-06, adds
      two mechanics that break controls defenders currently rely on. An embedded Python helper opens
      /proc/<pid>/maps and /proc/<pid>/mem on the GitHub Actions Runner.Worker process and searches
      live memory for OIDC tokens and runner secrets, so scanning files and environment variables at
      rest does not see it. A second, single-target path trades a runner OIDC token at npm's
      trusted-publishing endpoint for a real publish credential, injects a typosquatted dependency
      without touching install scripts, and then signs the result through Fulcio and Rekor — producing
      provenance Unit 42 is explicit is not forged.
    fields:
      - actions
      - affected_products
      - evidence
      - sectors
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-08-08/chaindrop-oidc-runner-memory-theft-valid-slsa-provenance
  - at: "2026-10-11T03:39:00Z"
    run_id: 2026-10-11T0256Z-intel
    type: update
    summary: >
      A further package, tensorlake@0.5.144 (the npm SDK of an AI-agent sandbox platform), was published on 2026-10-08 with a
      Shai-Hulud-family payload through the project's normal GitHub Actions pipeline with valid build provenance; Socket and OX
      Security describe the dead-man switch that wipes the owner's home directory when the stolen GitHub token is revoked, and
      both say to remove its persistence before revoking. Socket matches the release to this wave, while OX Security says new
      keys may point to an independent actor reusing the name.
    fields:
      - actions
      - evidence
      - sources
      - sourcing_note
      - summary
      - techniques
      - body
  - at: "2026-10-11T13:55:57Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      Elastic reads the commit-message string warning against token revocation as intimidation, and OX Security calls the same string an extortion string while describing a dead man's switch separately, which Elastic does not mention; the containment paragraph now says so. Unit 42's environment check selects a single republishing path in one project and does not gate the worm as a whole, which the earlier wording implied. The locale-gate sentence gains its citation.
    fields: [body, sourcing_note]
  - at: "2026-10-21T08:24:07Z"
    run_id: 2026-10-21T0800Z-audit
    type: improvement
    summary: >
      Unit 42 found the August sample's installer for OS-level token-monitor persistence decrypted but
      never invoked, so in that sample the persistence is a latent capability rather than observed
      behaviour.
    fields: [title, summary, actions, body]
migrated_from: null
---

Elastic Security Labs identified a new Shai-Hulud campaign on 2026-08-04 that began by trojanising the monorepo of `keyv`, a widely used key-value storage library, and embedding a self-propagating worm it names CHAINDROP ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). Elastic reports over 400 unique npm packages compromised at the time of writing, and quantifies the blast radius through download volume: keyv alone received over 600 million downloads in the preceding month, with flat-cache near 580 million, cacheable-request over 137 million, cacheable over 30 million and cache-manager over 16 million ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). OX Security published its own first-hand analysis two days earlier and describes a massive Shai-Hulud campaign against npm on its own larger package and download counts ([OX Security, 2026-08-04](https://www.ox.security/blog/a-new-infostealer-worm-hits-npm-affecting-keyv-and-cacheable/)). Elastic frames the wave as the return of Shai-Hulud, and points to Dune-themed references in the payload and to its similarities with previous Shai-Hulud campaigns ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)).

**Execution.** The chain starts at a `preinstall` hook in `package.json`, abusing a legitimate npm feature that runs arbitrary commands before a package is installed and therefore needs no interaction from the victim beyond the install itself ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). Every subpackage in the keyv repository was backdoored with a dropper that checks whether the Bun JavaScript runtime is present and, if not, detects the host platform and architecture and downloads Bun directly from its official release page before using it to execute the payload; the temporary Bun directory is deleted afterwards ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). The payload is cross-platform across Linux, macOS and Windows, and is heavily obfuscated at 711 kilobytes using control-flow flattening ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). It appears under two filenames, one in packages compromised directly from the keyv monorepo and another in packages trojanised during worm propagation, which share the same hash, so the filename indicates which generation of the infection a defender is looking at ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)).

**A second infection route that does not involve installing anything.** In Visual Studio Code a `folderOpen` task under `tasks.json` runs the dropper when an infected repository is merely opened, and where the stolen credential set includes a GitHub App token the worm commits malicious hooks to up to 50 branches per accessible repository, injecting both a `.claude/settings.json` and a `.vscode/tasks.json` into each, so a developer can be infected by opening the repository ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). That is the operationally important departure: an organisation that responds to a supply-chain wave purely by pinning or freezing dependency installs has not closed the path that fires when an engineer clones and opens the repository, and the AI-assistant configuration file is a trust surface most repository review does not read.

**Collection and exfiltration.** A collector component scans over 300 unique patterns across credential stores on a developer machine, with notable targeting of AI-tooling credentials for Anthropic, Claude, Codex, Cursor, OpenAI and Gemini, alongside AWS, GCP, Azure and Alibaba Cloud credentials, GitHub personal-access tokens, JWTs and session tokens, HashiCorp Vault tokens, SSH private keys, Kubernetes service-account tokens and npm tokens ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). Harvested material is gzip-compressed, encrypted under a randomly generated AES-256-GCM key, and that key is in turn RSA-encrypted to the attacker's hardcoded public key ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). For delivery, CHAINDROP does not hardcode a command-and-control domain: it queries an Ethereum smart contract at runtime to retrieve the current exfiltration endpoint, using multiple RPC providers as fallbacks, so the operator can rotate infrastructure by updating the contract rather than by shipping a new payload ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). If that path and its successor fail, it falls back to exfiltrating through a public GitHub repository created under the victim's own account with a fixed Shai-Hulud description string ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)).

**Containment sequencing: remove the monitor before revoking.** OX Security states the malware carries a dead man's switch that deletes the current machine if the stolen GitHub token is revoked, separate from the commit-message string warning developers not to revoke the token, which OX calls an extortion string ([OX Security, 2026-08-04](https://www.ox.security/blog/a-new-infostealer-worm-hits-npm-affecting-keyv-and-cacheable/)). Elastic, which does not mention a switch, reads that revoke-warning string as an attempt to intimidate developers not to revoke the token, and its guidance is to revoke all GitHub tokens for impacted machines ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). Unit 42 found that the August sample carries an installer for OS-level token-monitor persistence (a macOS LaunchAgent and a Linux systemd user service) that was decrypted but never invoked, and says to treat OS-level persistence as latent capability, not observed behavior ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)). Socket's later analysis of a release that it matches to this wave's file structure describes the mechanism in detail, and tells responders to remove the token monitor before revoking anything (see the update of 2026-10-11 below) ([Socket, 2026-10-08](https://www.socket.dev/blog/tensorlake-compromise)). Sequence the response around it: isolating and imaging a suspected host and removing any token-monitor persistence before revoking its GitHub token loses nothing if the switch does not fire, while revoking first loses the host and its evidence if it does.

**Propagation gate.** The worm activates only when the credential sweep turns up an npm token meeting two conditions together: package-write permission, and the ability to publish without two-factor authentication ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). Given a qualifying token it enumerates every package the victim can publish to, downloads each latest tarball from the registry, and republishes it trojanised ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). That gate is the single most useful fact in the report for a defender, because it converts an unbounded ecosystem-wide risk into a property you can audit on your own accounts.

**Defender takeaway:** hunt on the execution shape rather than on package names, because the package list is a moving target and the payload hash is stable across two filenames. In process-execution telemetry with parent lineage, the signal is a package-manager install spawning a script interpreter, and specifically a newly downloaded runtime binary being fetched and executed from a temporary directory during an install and then deleted. In file-creation telemetry, look for `.vscode/tasks.json` and `.claude/settings.json` appearing or changing in repositories that no engineer edited, across many branches: the 50-branch injection is noisy in commit history in a way the install-time compromise is not. In egress telemetry, connections from build agents and developer endpoints to Ethereum RPC providers are the anomaly worth surfacing; blockchain RPC is not normal build traffic in most enterprise estates, and because it is the resolution step it happens before any exfiltration does. Elastic ships detection rules for the trojanised-install and pre/post-install script-execution patterns ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)).

**Triage:** developer and CI hosts legitimately run script interpreters from package-manager parents on every build, and legitimately download toolchains, so neither alone discriminates. The separating features are that the runtime is fetched mid-install rather than during provisioning and its directory is removed immediately afterwards; that the process reads credential stores belonging to unrelated tools (cloud CLIs, SSH, Kubernetes, AI assistants) in one burst, which no ordinary build step does; and that outbound blockchain RPC follows the credential reads in the same process tree. Any one of these is weak on its own; the sequence is the signal.

## Update — 2026-08-08T04:53:00Z

Unit 42 published its own analysis of the CHAINDROP wave on 2026-08-06, and two of its findings change what defenders can rely on rather than adding detail to what they already knew.

The first is credential theft that never touches disk. An embedded Python helper hidden inside an encrypted blob in the payload "locates the `Runner.Worker` process on GitHub Actions runners, opens `/proc/<pid>/maps` and `/proc/<pid>/mem`, and searches live process memory for OpenID Connect (OIDC) tokens and runner secrets" ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)). Ephemeral OIDC tokens exist to avoid long-lived secrets sitting in a file or a variable; reading them out of the runner's address space while they are live defeats that design, and any secret-scanning control that inspects files or environment variables at rest sees nothing.

The second is a single-target path that is worse than a forgery. Before collecting anything, the worm checks three environment variables: when it is inside GitHub Actions, in a repository whose name contains `/opensearch-js`, in a workflow whose reference contains `release-drafter.yml`, it runs only a republishing routine and exits without collecting; in an `/opensearch-js` repository with any other workflow it exits and steals nothing, staying silent in exactly the runs a maintainer is most likely to be reading ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)). In that path it asks the runner for an OIDC token scoped to `npm:registry.npmjs.org` and trades it at npm's own trusted-publishing exchange for a real publish credential: the repository's legitimate release identity becomes the attacker's. It then downloads the latest tarball, bumps the patch version and adds a single dependency line typosquatting the project's own scope, never touching install scripts at all, so detections built around preinstall hooks would miss it. Finally it requests a second OIDC token for Sigstore, obtains a Fulcio certificate, builds an in-toto SLSA v1 provenance statement over the tarball's SHA-512 hash, signs it and uploads the entry to the public Rekor transparency log ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)).

Unit 42 is explicit about what that means: "This is not forged provenance. The attestation says the tarball was built in that repository by that workflow, and that is true." Its guidance follows directly: a package having valid npm provenance does not mean the package is clean, only that the tarball came out of the workflow named in the certificate, and if that workflow is running attacker code then valid provenance is what you should expect to see. "Pivot on the Rekor log index and the workflow identity inside the certificate, not on whether the signature checks out" ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)).

Unit 42 states it did not observe this path execute and that it cannot execute anywhere except in that one workflow in that one repository, but that it is fully implemented and reachable from the payload's main entry point ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)). The worm also runs a locale gate before any collection, exiting cleanly on a Russian-language host ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)).

**Defender takeaway:** provenance attestation has been the reassuring answer to "how do we know this build is what it claims to be", and it still answers that question correctly; it just turns out that was never the question worth asking once the workflow itself is hostile. **Triage:** on self-hosted runners, a process opening `/proc/<pid>/mem` of the runner worker is not something any legitimate build step does, and it is the cleanest available discriminator; debuggers and profilers that legitimately read process memory are not part of a normal publish workflow and do not target the runner agent itself.

## Update — 2026-10-11T03:39:00Z

A further package carrying this payload family was published on 2026-10-08: tensorlake@0.5.144, the npm SDK of an AI-agent sandbox platform, went out at 01:12 UTC with a preinstall hook that runs an obfuscated loader, which in turn launches a large payload under Bun; Socket flagged it about 11 minutes later, the release has since been removed and 0.5.143 is clean ([Socket, 2026-10-08](https://www.socket.dev/blog/tensorlake-compromise); [Endor Labs, 2026-10-08](https://www.endorlabs.com/learn/tensorlake-npm-package-compromised-by-shai-hulud-in-latest-software-supply-chain-attack)). Socket says the hook and payload file names match the structure documented in the August wave ([Socket, 2026-10-08](https://www.socket.dev/blog/tensorlake-compromise)). Endor Labs reports that the release shipped through the project's normal GitHub Actions pipeline with valid build provenance after the attacker modified the main branch first, most likely through a compromised maintainer account, and notes that provenance confirms where a build came from, not that the source was clean ([Endor Labs, 2026-10-08](https://www.endorlabs.com/learn/tensorlake-npm-package-compromised-by-shai-hulud-in-latest-software-supply-chain-attack)). That is the situation the update of 2026-08-08 warned about, now on a published package. Socket reports that the payload harvests npm and GitHub tokens, AWS credentials (instance metadata, ECS, Secrets Manager and Parameter Store), a local HashiCorp Vault, Kubernetes service-account tokens and kubeconfig files, SSH keys, environment files and AI-tool configuration, resolves its endpoint from an Ethereum contract through about 30 public RPC endpoints with a GitHub fallback, and republishes itself with Sigstore provenance to packages the victim can publish ([Socket, 2026-10-08](https://www.socket.dev/blog/tensorlake-compromise)).

The dead-man switch is described in detail here. A PowerShell monitor persisted through a scheduled task that runs at logon polls the GitHub API with the stolen token and, when the token is revoked, runs an attacker-supplied handler; Socket says the revoke-wipe string in the code appeared in earlier waves ([Socket, 2026-10-08](https://www.socket.dev/blog/tensorlake-compromise)). Socket and OX Security both tell responders to isolate the host and remove the token-monitor persistence first (a systemd user unit on Linux, a LaunchAgent on macOS, a scheduled task on Windows) and only then revoke and rotate, because revoking while the monitor runs wipes the user's home directory; removing the npm dependency alone does not remove that persistence ([Socket, 2026-10-08](https://www.socket.dev/blog/tensorlake-compromise); [OX Security, 2026-10-08](https://www.ox.security/blog/shai-hulud-here-we-go-again-tensorlake-npm-package-hit-with-malware/)).

Attribution is split: Socket frames the release as part of this wave ([Socket, 2026-10-08](https://www.socket.dev/blog/tensorlake-compromise)), while OX Security reports new public keys that may indicate an independent actor or a new group using the Shai-Hulud name ([OX Security, 2026-10-08](https://www.ox.security/blog/shai-hulud-here-we-go-again-tensorlake-npm-package-hit-with-malware/)).

## Correction — 2026-10-11T13:55:57Z

Elastic reads the string the worm writes into its commit messages beside the stolen token, warning that revoking it will crash production servers, as "an attempt to intimidate developers not to revoke the GitHub token" ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)); OX Security calls the same string an extortion string and describes a dead man's switch separately ([OX Security, 2026-08-04](https://www.ox.security/blog/a-new-infostealer-worm-hits-npm-affecting-keyv-and-cacheable/)), which Elastic does not mention. Unit 42's three-variable check selects the opensearch-js republishing path: with all three set the worm republishes and exits without collecting, and in any other workflow of that project it exits without stealing; outside that project it follows its normal collection chain ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)).

## Improvement — 2026-10-21T08:24:07Z

In the August sample, the installer for OS-level token-monitor persistence (a macOS LaunchAgent and a Linux systemd user service) was decrypted but never invoked: the routine that would run it has no call site, so Unit 42 says to treat OS-level persistence as latent capability, not observed behavior ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)).
