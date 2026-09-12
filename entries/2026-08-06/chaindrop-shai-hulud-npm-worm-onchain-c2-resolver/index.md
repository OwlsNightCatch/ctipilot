---
schema: 1
kind: threat
title: >
  CHAINDROP — the Shai-Hulud npm worm returns through the keyv maintainer, backdoors 400+
  packages, and resolves its exfiltration endpoint from an Ethereum smart contract
headline: >
  A self-propagating npm worm reaches packages totalling 1.3 billion monthly downloads, and its C2
  address lives on-chain
summary: >
  Elastic Security Labs identified CHAINDROP on 2026-08-04, a new wave of the Shai-Hulud npm worm
  that began with the compromise of the keyv maintainer and has backdoored over 400 npm packages
  whose combined reach Elastic puts at more than 1.3 billion monthly downloads, keyv alone at over
  600 million. Execution comes from a package.json preinstall hook that downloads the Bun runtime
  to run an obfuscated 711 KB payload, which harvests over 300 credential patterns — AI-assistant
  tokens, AWS/GCP/Azure/Alibaba credentials, GitHub tokens, Vault tokens, SSH keys and Kubernetes
  service-account tokens — and self-propagates only when it finds an npm token that both carries
  package-write permission and can publish without two-factor authentication. Rather than
  hardcoding a command-and-control domain, CHAINDROP queries an Ethereum smart contract at runtime
  to resolve where to send the stolen material, so the operator rotates infrastructure without
  shipping a new payload.
discovered_at: "2026-08-06T04:11:48Z"
updated_at: "2026-08-08T04:53:00Z"
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
verification: multi-source
sourcing_note: >
  Two vendors reported first-hand on the same campaign two days apart and their counts differ:
  Elastic gives over 400 compromised packages and over 1.3 billion combined monthly downloads, OX
  Security gives its own larger figures from its own telemetry. Each number in this entry is
  attributed to the vendor that published it rather than merged into a single total. Elastic's
  write-up carries the fuller execution-chain and C2 detail and is used as the primary.
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
  - "Audit every npm publish token your organisation and its maintainers hold and revoke any that can publish without two-factor authentication — that exact token property, not package popularity, is what decides whether the worm spreads from a compromised developer to your packages."
  - "On any developer workstation or build agent that installed a package from the keyv family since 2026-08-04, treat the AI-assistant, cloud, GitHub, Vault, SSH and Kubernetes credentials present on that host as disclosed and rotate them; the collector sweeps over 300 credential patterns in one pass, so partial rotation leaves the operator a working set. Isolate and image the host before revoking its GitHub token — OX Security reports a trigger that wipes the machine when that token is revoked, so revocation-first destroys the forensic evidence you would need."
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
migrated_from: null
---

Elastic Security Labs identified a new Shai-Hulud campaign on 2026-08-04 that began by trojanising the monorepo of `keyv`, a widely used key-value storage library, and embedding a self-propagating worm it names CHAINDROP ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). Elastic reports over 400 unique npm packages compromised at the time of writing, and quantifies the blast radius through download volume: keyv alone received over 600 million downloads in the preceding month, with flat-cache near 580 million, cacheable-request over 137 million, cacheable over 30 million and cache-manager over 16 million ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). OX Security published its own first-hand analysis two days earlier and describes a massive Shai-Hulud campaign against npm on its own larger package and download counts ([OX Security, 2026-08-04](https://www.ox.security/blog/a-new-infostealer-worm-hits-npm-affecting-keyv-and-cacheable/)). Elastic frames the wave explicitly as the return of Shai-Hulud rather than a new family, and points to the Dune-derived naming the payload reuses as the similarity to previous Shai-Hulud campaigns ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)).

**Execution.** The chain starts at a `preinstall` hook in `package.json`, abusing a legitimate npm feature that runs arbitrary commands before a package is installed and therefore needs no interaction from the victim beyond the install itself ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). Every subpackage in the keyv repository was backdoored with a dropper that checks whether the Bun JavaScript runtime is present and, if not, detects the host platform and architecture and downloads Bun directly from its official release page before using it to execute the payload; the temporary Bun directory is deleted afterwards ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). The payload is cross-platform across Linux, macOS and Windows, and is heavily obfuscated at 711 kilobytes using control-flow flattening ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). It appears under two filenames — one in packages compromised directly from the keyv monorepo, another in packages trojanised during worm propagation — which share the same hash, so the filename indicates which generation of the infection a defender is looking at ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)).

**A second infection route that does not involve installing anything.** In Visual Studio Code a `folderOpen` task under `tasks.json` runs the dropper when an infected repository is merely opened, and where the stolen credential set includes a GitHub App token the worm commits malicious hooks to up to 50 branches per accessible repository, injecting both a `.claude/settings.json` and a `.vscode/tasks.json` into each — so a developer can be infected by opening the repository ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). That is the operationally important departure: an organisation that responds to a supply-chain wave purely by pinning or freezing dependency installs has not closed the path that fires when an engineer clones and opens the repository, and the AI-assistant configuration file is a trust surface most repository review does not read.

**Collection and exfiltration.** A collector component scans over 300 unique patterns across credential stores on a developer machine, with notable targeting of AI-tooling credentials for Anthropic, Claude, Codex, Cursor, OpenAI and Gemini, alongside AWS, GCP, Azure and Alibaba Cloud credentials, GitHub personal-access tokens, JWTs and session tokens, HashiCorp Vault tokens, SSH private keys, Kubernetes service-account tokens and npm tokens ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). Harvested material is gzip-compressed, encrypted under a randomly generated AES-256-GCM key, and that key is in turn RSA-encrypted to the attacker's hardcoded public key ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). For delivery, CHAINDROP does not hardcode a command-and-control domain: it queries an Ethereum smart contract at runtime to retrieve the current exfiltration endpoint, using multiple RPC providers as fallbacks, so the operator can rotate infrastructure by updating the contract rather than by shipping a new payload ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). If that path and its successor fail, it falls back to exfiltrating through a public GitHub repository created under the victim's own account with a fixed Shai-Hulud description string ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)).

**A containment-sequencing warning the two reports do not agree on.** OX Security states the malware carries a dead man's switch that deletes the current machine if the stolen GitHub token is revoked ([OX Security, 2026-08-04](https://www.ox.security/blog/a-new-infostealer-worm-hits-npm-affecting-keyv-and-cacheable/)). Elastic's own guidance is to revoke all GitHub tokens for impacted machines and does not mention any such trigger ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). Only one vendor reports it and the other does not corroborate it, so treat it as an unconfirmed claim from a first-hand analysis rather than an established property — but sequence around it, because the cost of being wrong is asymmetric. Isolating and imaging a suspected host before revoking its GitHub token loses nothing if the switch does not exist, while revoking first loses the host and its evidence if it does.

**Propagation gate.** The worm activates only when the credential sweep turns up an npm token meeting two conditions together: package-write permission, and the ability to publish without two-factor authentication ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). Given a qualifying token it enumerates every package the victim can publish to, downloads each latest tarball from the registry, and republishes it trojanised ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)). That gate is the single most useful fact in the report for a defender, because it converts an unbounded ecosystem-wide risk into a property you can audit on your own accounts.

**Defender takeaway:** hunt on the execution shape rather than on package names, because the package list is a moving target and the payload hash is stable across two filenames. In process-execution telemetry with parent lineage, the signal is a package-manager install spawning a script interpreter, and specifically a newly downloaded runtime binary being fetched and executed from a temporary directory during an install and then deleted. In file-creation telemetry, look for `.vscode/tasks.json` and `.claude/settings.json` appearing or changing in repositories that no engineer edited, across many branches — the 50-branch injection is noisy in commit history in a way the install-time compromise is not. In egress telemetry, connections from build agents and developer endpoints to Ethereum RPC providers are the anomaly worth surfacing; blockchain RPC is not normal build traffic in most enterprise estates, and because it is the resolution step it happens before any exfiltration does. Elastic ships detection rules for the trojanised-install and pre/post-install script-execution patterns ([Elastic Security Labs, 2026-08-06](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain)).

**Triage:** developer and CI hosts legitimately run script interpreters from package-manager parents on every build, and legitimately download toolchains, so neither alone discriminates. The separating features are that the runtime is fetched mid-install rather than during provisioning and its directory is removed immediately afterwards; that the process reads credential stores belonging to unrelated tools — cloud CLIs, SSH, Kubernetes, AI assistants — in one burst, which no ordinary build step does; and that outbound blockchain RPC follows the credential reads in the same process tree. Any one of these is weak on its own; the sequence is the signal.

## Update — 2026-08-08T04:53:00Z

Unit 42 published its own analysis of the CHAINDROP wave on 2026-08-06, and two of its findings change what defenders can rely on rather than adding detail to what they already knew.

The first is credential theft that never touches disk. An embedded Python helper hidden inside an encrypted blob in the payload "locates the `Runner.Worker` process on GitHub Actions runners, opens `/proc/<pid>/maps` and `/proc/<pid>/mem`, and searches live process memory for OpenID Connect (OIDC) tokens and runner secrets" ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)). Ephemeral OIDC tokens exist to avoid long-lived secrets sitting in a file or a variable; reading them out of the runner's address space while they are live defeats that design, and any secret-scanning control that inspects files or environment variables at rest sees nothing.

The second is a single-target path that is worse than a forgery. The worm checks three environment variables and only proceeds if it finds itself inside GitHub Actions, in a repository whose name contains `/opensearch-js`, in a workflow whose reference contains `release-drafter.yml`; anywhere else in that project it exits and steals nothing, staying silent in exactly the runs a maintainer is most likely to be reading ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)). In that path it asks the runner for an OIDC token scoped to `npm:registry.npmjs.org` and trades it at npm's own trusted-publishing exchange for a real publish credential — the repository's legitimate release identity becomes the attacker's. It then downloads the latest tarball, bumps the patch version and adds a single dependency line typosquatting the project's own scope, never touching install scripts at all, so detections built around preinstall hooks would miss it. Finally it requests a second OIDC token for Sigstore, obtains a Fulcio certificate, builds an in-toto SLSA v1 provenance statement over the tarball's SHA-512 hash, signs it and uploads the entry to the public Rekor transparency log ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)).

Unit 42 is explicit about what that means: "This is not forged provenance. The attestation says the tarball was built in that repository by that workflow, and that is true." Its guidance follows directly — a package having valid npm provenance does not mean the package is clean, only that the tarball came out of the workflow named in the certificate, and if that workflow is running attacker code then valid provenance is what you should expect to see. "Pivot on the Rekor log index and the workflow identity inside the certificate, not on whether the signature checks out" ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)).

Unit 42 states it did not observe this path execute and that it cannot execute anywhere except in that one workflow in that one repository, but that it is fully implemented and reachable from the payload's main entry point ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)). The worm also runs a locale gate before any collection, exiting cleanly on a Russian-language host.

**Defender takeaway:** provenance attestation has been the reassuring answer to "how do we know this build is what it claims to be", and it still answers that question correctly — it just turns out that was never the question worth asking once the workflow itself is hostile. **Triage:** on self-hosted runners, a process opening `/proc/<pid>/mem` of the runner worker is not something any legitimate build step does, and it is the cleanest available discriminator; debuggers and profilers that legitimately read process memory are not part of a normal publish workflow and do not target the runner agent itself.
