---
schema: 1
kind: synthesis
horizon: strategic
title: >
  npm supply-chain wave status: jscrambler package compromised this week, extending the
  install-hook-evasion pattern seen in the injectivelabs SDK
headline: >
  npm supply-chain wave — jscrambler (v8.14.0-8.20.0) pushed a Rust infostealer, moving the
  dropper out of the preinstall hook to evade scanners
summary: >
  The npm supply-chain pressure this pipeline has tracked continued in 2026-W28. On 2026-07-11 the
  jscrambler npm package was compromised (v8.14.0 through 8.20.0) via a stolen publishing
  credential, pushing a Rust infostealer through an undocumented preinstall hook — then, from
  8.18.0, relocating the identical dropper into a self-executing dist/index.js function
  specifically to evade install-script scanners. It targets cloud metadata credentials, CI tokens,
  browser and AI-tool configs and wallet seeds; Socket detected it 6 minutes after publication and
  8.22.0 is clean. This mirrors the same install-hook-evasion evolution as this week's
  injectivelabs SDK compromise, though jscrambler has not been shown to self-propagate like the
  Shai-Hulud worm strain.
discovered_at: "2026-07-12T23:48:00Z"
updated_at: "2026-08-09T23:45:00Z"
event_date: 2026-07-11
run_id: 2026-07-12T2309Z-weekly
priority: high
immediate_action: null
tags:
  - supply-chain
  - data-breach
  - infostealer
  - cloud
  - ai-abuse
  - nation-state
  - organized-crime
  - north-korea-nexus
  - identity
regions:
  - global
  - europe
sectors:
  - technology
  - public-sector
  - finance
entities:
  - "incident:jscrambler-npm-supply-chain-2026"
  - "incident:injectivelabs-npm-sdk-ts-supply-chain-2026"
  - "incident:asyncapi-npm-github-actions-supply-chain-compromise-2026-07"
  - "tool:m-red-team-malware-framework"
  - "campaign:contagious-interview"
  - "malware:sandworm-mode"
  - "actor:sapphire-sleet"
  - "actor:teampcp"
  - "campaign:shai-hulud-chaindrop-2026-08"
  - "campaign:flooding-dropper-npm-2026-08"
techniques:
  - T1195.002
  - T1027
  - T1552.001
  - T1204
  - T1546
  - T1071.004
  - T1497
  - T1195.001
  - T1199
  - T1105
  - T1543.001
  - T1543.002
  - T1078.004
affected_products:
  - axios (npm)
  - GitHub Actions
  - npm
  - PyPI
  - Docker Hub
  - Sigstore
cves: []
sources:
  - url: "https://socket.dev/blog/jscrambler-supply-chain-attack"
    publisher: Socket
    role: primary
  - url: "https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/"
    publisher: Microsoft Threat Intelligence
    date: 2026-07-15
    role: primary
  - url: "https://www.elastic.co/security-labs/contagious-interview-malware-svg-steganography"
    publisher: Elastic Security Labs
    date: 2026-07-18
    role: primary
  - url: "https://www.crowdstrike.com/en-us/blog/denying-the-worm-sandworm-mode-and-ai-toolchain-supply-chain-attacks/"
    publisher: CrowdStrike
    date: 2026-07-21
    role: primary
  - url: "https://securitybrief.com.au/story/crowdstrike-warns-of-malware-targeting-ai-coding-tools"
    publisher: SecurityBrief
    date: 2026-07-22
    role: corroborating
  - url: "https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/"
    publisher: AWS Security Blog
    date: 2026-07-29
    role: primary
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/"
    publisher: Google Cloud Blog (GTIG)
    date: 2026-07-30
    role: primary
  - url: "https://cyberscoop.com/amazon-north-korea-open-source-software-attacks/"
    publisher: CyberScoop
    date: 2026-07-29
    role: corroborating
  - url: "https://socket.dev/blog/popular-npm-packages-in-the-keyv-and-cacheable-namespaces-compromised-in-active-supply-chain"
    publisher: Socket Threat Research
    date: 2026-08-04
    role: primary
  - url: "https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain"
    publisher: Elastic Security Labs
    date: 2026-08-06
    role: corroborating
  - url: "https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/"
    publisher: Palo Alto Networks Unit 42
    date: 2026-08-06
    role: corroborating
closed_sources: []
evidence:
  - quote: Starting with 8.18.0 the install hook is gone entirely—the identical dropper is instead injected as a self-executing function at the top of dist/index.js.
    publisher: Socket
  - quote: Socket detected the compromised package 6 minutes after publication.
    publisher: Socket
  - quote: "Based on analysis of command-and-control (C2) indicators and TTPs, Amazon Threat Intelligence assesses with medium confidence that these campaigns are attributable to the DPRK-linked threat actor tracked as SAPPHIRE SLEET"
    publisher: AWS Security Blog
  - quote: "In each case, the threat actor gained access by socially engineering a trusted maintainer of the package, then published a software update containing malicious code."
    publisher: AWS Security Blog
  - quote: This approach is designed to defeat scanners that evaluate packages one by one instead of reasoning about how they interact in a real dependency graph.
    publisher: AWS Security Blog
  - quote: "GTIG assesses with high confidence that the growth in very large-scale, open-source supply chain compromise campaigns, including use of worms and iterative compromises in 2025 and early 2026, represent a significant expansion in use of this tactic compared to prior years."
    publisher: Google Cloud Blog (GTIG)
  - quote: "UNC6780 (aka \"TeamPCP\") conducted extensive open source supply chain compromises targeting ecosystems like PyPI, npm, and Docker Hub. Initial infection vectors varied across incidents, and included abuse of the pull_request_target GitHub Actions trigger to obtain base repository secrets and write permissions."
    publisher: Google Cloud Blog (GTIG)
  - quote: "While the malicious versions of axios were removed from the npm registry within three hours of their release, the scope of the compromise is estimated to be broad, as the package has over 100 million weekly downloads."
    publisher: Google Cloud Blog (GTIG)
  - quote: "Setting this value to at least 24 hours (1440 minutes) ensures that freshly published, potentially poisoned packages are quarantined until the broader security community has had time to identify and remove them"
    publisher: Google Cloud Blog (GTIG)
  - quote: "Before rotating any credential, hunt for and remove the host-level dead-man's switch. Revocation is its trigger: the watcher runs eval on a remote-supplied handler the moment the stolen token returns an HTTP 4xx."
    publisher: Socket Threat Research
  - quote: "The lesson is that provenance attests build integrity, not source integrity. The npm and sigstore pipeline did exactly what it is designed to do and still produced a signed, verifiable attestation for malware, because the source it built from was already trojanized."
    publisher: Socket Threat Research
verification: multi-source
sourcing_note: >
  Two independent primaries (Socket's analysis, The Hacker News corroboration), both fetched this
  run. Reliability B, credibility 1 (corroborated). Framed as a fresh data point in the tracked
  npm-supply-chain wave, not a re-summary of the prior weekly's coverage.
confidence: high
references:
  - 2026-07-10/injectivelabs-npm-runtime-keyhook-supply-chain-evasion
  - 2026-06-29/npm-supply-chain-worms-a-sustained-wave-across-the-week
  - 2026-07-14/asyncapi-npm-supply-chain-compromise-github-actions
  - 2026-07-18/contagious-interview-ottercookie-svg-steganography
  - 2026-07-23/sandworm-mode-npm-ai-toolchain-supply-chain-worm-mcp
  - 2026-07-30/amazon-dprk-attribution-npm-typo-crypto-rehearsal
  - 2026-08-06/chaindrop-shai-hulud-npm-worm-onchain-c2-resolver
  - 2026-08-07/flooding-dropper-npm-846-packages-dns-txt-fallback
weekly_section: weekly-long-running
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Query build/CI dependency trees for jscrambler and pin it away from v8.14.0-8.20.0 (8.22.0 is clean); for any environment that installed an affected version between 2026-07-11 and remediation, rotate the credentials the stealer targets — cloud keys, CI/deploy tokens, and any secrets reachable from the build runner — and treat it as a compromise, not a risk."
  - "Audit every GitHub Actions workflow in your organisation that uses the pull_request_target trigger and confirm none exposes base-repository secrets or write permissions to code from a fork — this is the specific mechanism GTIG names UNC6780 as having abused across npm, PyPI and Docker Hub, and a workflow using that trigger runs with the base repository's privileges by design rather than by misconfiguration."
  - "Set a minimum release-age cooldown of at least 24 hours on npm and pnpm installs across CI and developer environments, so a freshly-published malicious version is quarantined during the window in which these compromises are typically caught and pulled — the malicious axios versions were removed from the registry within about three hours of release."
  - "Before revoking or rotating any npm, GitHub, cloud or SSH credential on a developer or CI host that installed an affected package, first locate and remove the token-watcher persistence Socket documents — the launch agent, the user-level systemd service and its configuration directory — because revocation is what makes the watcher execute its remote handler."
updates:
  - at: "2026-07-19T23:38:00Z"
    run_id: 2026-07-19T2310Z-weekly
    type: update
    summary: >
      Update to the prior weekly's npm supply-chain wave. This week the wave's front edge moved from
      poisoning published packages to abusing the trust machinery around them. The AsyncAPI compromise
      reached over-three-million-weekly-download packages by riding the org's own legitimate CI/CD
      release workflow, so the five trojanized versions carried cryptographically valid npm/OIDC
      provenance attestations and executed at import time (defeating --ignore-scripts). In parallel,
      the DPRK-aligned Contagious Interview campaign broadened the developer-targeting vector: a fake
      job posting delivered a trojanized Next.js repo hiding its payload as Base64 fragments across
      HTML comments in every SVG flag image, reassembled and run with eval() to evade scanners that do
      not parse SVG comment bodies. Both extend the tracked pattern the same way — the initial-access
      target is the developer and the build/trust pipeline, not just the registry — and both defeat a
      control defenders assumed held (provenance attestation; install-hook scanning). No change to the
      previously-tracked jscrambler/injectivelabs strains beyond this new front.
    fields:
      - entities
      - references
      - regions
      - sectors
      - sources
      - techniques
      - body
    merged_from: 2026-07-19/weekly-w29-npm-supply-chain-developer-targeting
  - at: "2026-07-26T23:46:00Z"
    run_id: 2026-07-26T2309Z-weekly
    type: update
    summary: >
      Update to the tracked npm / developer-ecosystem supply-chain wave. Prior weeklies followed it
      from install-hook-evasion package compromises (jscrambler, injectivelabs) to abuse of the trust
      machinery around packages (AsyncAPI riding a legitimate CI/CD release workflow to ship
      provenance-attested malicious versions; DPRK Contagious Interview targeting developers
      directly). This week CrowdStrike documented SANDWORM_MODE, which moves the front edge one layer
      further in: rather than poisoning a package or a pipeline, the multi-stage npm worm writes rogue
      Model Context Protocol (MCP) tool-provider entries into AI coding-assistant configurations
      (Cursor, VS Code, Claude Desktop, Windsurf), injects global git-template hooks for persistence,
      and exfiltrates npm/AWS/SSH credentials plus multi-provider LLM API keys — delaying activation
      48-96 hours to defeat install-versus-behaviour correlation. The transferable lesson is unchanged
      in direction but sharper in target: the developer's AI-assisted toolchain and its trust
      configuration are now the initial-access objective, and of 14 investigated behaviours
      CrowdStrike found only 2 met the bar for high-fidelity alerting because the worm's actions blend
      into legitimate developer and CI telemetry.
    fields:
      - entities
      - references
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-07-26/weekly-w30-npm-ai-toolchain-supply-chain-status
  - at: "2026-08-02T23:59:00Z"
    run_id: 2026-08-02T2311Z-weekly
    type: update
    summary: >
      Status update on the npm and developer-ecosystem supply-chain wave prior weeklies tracked from
      install-hook evasion through CI/CD trust abuse to poisoned AI-assistant tool configurations. Two
      developments this week. Amazon attributed the September 2025 debug and chalk compromises and the
      March 2026 axios compromise to a DPRK-linked cluster at medium confidence, finding maintainer
      access came from social engineering rather than a platform flaw in every case, and assessing a
      small March 2025 package compromise as a testing ground for what followed. Google's
      threat-intelligence group independently credits the same actor with the axios compromise under
      its own tracking name, and names the specific CI mechanism another cluster abused: the
      pull_request_target GitHub Actions trigger, used to obtain base-repository secrets and write
      permissions. The transferable levers are concrete — audit that trigger, and impose a release-age
      cooldown on installs.
    fields:
      - actions
      - affected_products
      - entities
      - evidence
      - references
      - sectors
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-08-02/weekly-w31-open-source-supply-chain-status
  - at: "2026-08-09T23:45:00Z"
    run_id: 2026-08-09T2315Z-weekly
    type: update
    summary: >
      Status update on the npm and developer-ecosystem supply-chain wave prior weeklies tracked from
      install-hook evasion through CI/CD trust abuse to poisoned AI-assistant tool configurations. Two
      week-level deltas beyond the operational entries. First, the 2026-08-04 compromise of the keyv
      and cacheable npm namespaces reported independently by Socket, Datadog and others is the same
      event as CHAINDROP — one wave, not two — and Socket documents a host-level dead-man's switch
      whose watcher polls the GitHub API with the stolen token and runs a remote-supplied handler the
      moment that token starts returning an HTTP 4xx, so credential rotation performed before the
      persistence is removed is itself the trigger. Second, the cross-vendor convergence sharpens the
      strategic lesson: provenance attests build integrity, not source integrity.
    fields:
      - actions
      - affected_products
      - entities
      - evidence
      - priority
      - references
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-08-09/weekly-w32-open-source-supply-chain-status
migrated_from: null
---

The software-supply-chain pressure on the npm ecosystem that this pipeline has tracked as a sustained wave continued this week, with a fresh compromise that sharpens the evasion trend rather than repeating it.

On 2026-07-11 the **jscrambler** npm package — a code-protection/obfuscation build tool — was compromised via what Socket assesses as a stolen publishing credential or compromised build pipeline: a malicious v8.14.0 pushed directly to npm, bypassing the project's normal release flow, adding an undocumented `preinstall` hook that unpacks and detached-spawns a platform-specific Rust infostealer on `npm install` alone. The stealer targets cloud metadata-endpoint credentials, Kubernetes configs, browser secrets, crypto-wallet seeds, AI coding-tool configs and messaging tokens. The notable evolution: over roughly three hours the actor pushed four more malicious releases and, "starting with 8.18.0 the install hook is gone entirely—the identical dropper is instead injected as a self-executing function at the top of dist/index.js" — moving execution out of the very hook that install-script scanners watch ([Socket, 2026-07-11](https://socket.dev/blog/jscrambler-supply-chain-attack)). Socket "detected the compromised package 6 minutes after publication"; v8.22.0 is confirmed clean ([The Hacker News, 2026-07-11](https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html)). This is the same install-hook-evasion arc as this week's injectivelabs SDK compromise, though — unlike the Shai-Hulud worm strain — jscrambler has not been shown to self-propagate to other maintainers.

**Defender takeaway:** the wave's shared lesson for any org with a CI/CD JS build chain is that install-hook scanning is now routinely bypassed, so provenance controls (pinned versions/lockfile integrity, short-lived scoped CI credentials, egress control from build runners) matter more than install-time script inspection; a runner that installed an affected jscrambler build should be treated as a credential-exposure event. **Triage:** a compromised build package shows up as a build/CI process making unexpected outbound connections or reading cloud-metadata and secret paths during `install`/`build` — behaviour a legitimate obfuscation tool has no reason to exhibit.

## Update — 2026-07-19T23:38:00Z

The prior weekly tracked the npm supply-chain wave through the jscrambler and injectivelabs compromises, whose signature was moving the dropper out of the install hook to evade scanners. This week the wave's front edge moved again — from poisoning packages to abusing the trust machinery around them, and the developer is now squarely the target. The marquee event was AsyncAPI: the attacker rode the org's own legitimate CI/CD release workflow, so the trojanized versions carried cryptographically valid npm/OIDC provenance attestations and executed at import time "even though the triggering commits were unauthorized," defeating `--ignore-scripts` ([Microsoft, 2026-07-15](https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/)) — the detailed provenance-vs-authorization lesson is in this week's incidents recap. In parallel, the DPRK-aligned Contagious Interview campaign broadened the developer-targeting vector beyond the registry entirely: Elastic documented a fake job posting delivering a trojanized Next.js repo that hides its payload as Base64 fragments inside HTML comments across every SVG flag image in an assets directory, reassembled alphabetically and run with `eval()` to evade scanners that do not parse SVG comment bodies, then running an OtterCookie-aligned credential/wallet stealer on project startup ([Elastic, 2026-07-18](https://www.elastic.co/security-labs/contagious-interview-malware-svg-steganography)). The consolidated status: the wave the pipeline tracks now spans package poisoning, CI/CD-pipeline compromise and job-interview repos, and its through-line is that the developer's build environment and the trust signals around it (attestations, install hooks, static scanners) are the surface — so branch-protection and workflow-trigger review, import-time dependency monitoring, and treating any candidate/contractor take-home repo as untrusted code are the current counters.

## Update — 2026-07-26T23:46:00Z

The npm / developer-ecosystem supply-chain wave this pipeline has tracked across prior weeklies added a distinct front this week, and the delta is the target layer.

Earlier stages of the wave moved from poisoning published packages with evasive install hooks (jscrambler, injectivelabs) to abusing the trust machinery around packages — the AsyncAPI compromise rode the org's own legitimate CI/CD release workflow so its trojanized versions carried cryptographically valid provenance attestations, and the DPRK-aligned Contagious Interview campaign targeted developers directly through fake job repos. This week's addition, CrowdStrike's SANDWORM_MODE, moves one layer further in: instead of poisoning a package or a pipeline, the multi-stage npm worm writes rogue Model Context Protocol (MCP) tool-provider entries into AI coding-assistant configurations — Cursor, VS Code, Claude Desktop and Windsurf — so the assistant itself loads and trusts an attacker-controlled tool provider, injects global git-template hooks for persistence, and exfiltrates npm, AWS and SSH credentials alongside multi-provider LLM API keys, delaying activation 48-96 hours on workstations to break the correlation between install time and malicious behaviour ([CrowdStrike, 2026-07-21](https://www.crowdstrike.com/en-us/blog/denying-the-worm-sandworm-mode-and-ai-toolchain-supply-chain-attacks/)).

**Defender takeaway:** the wave's direction is unchanged — the developer and the build/trust machinery are the initial-access target, not just the registry — but the newly-added surface is the AI coding assistant's own configuration, which most organisations do not yet monitor or baseline. CrowdStrike's own detection finding is the operative point for defenders building coverage: of 14 investigated behaviours only 2 met the bar for high-fidelity alerting, because the worm's file writes and network calls blend into legitimate developer and CI telemetry. That argues for treating AI-assistant MCP-server configuration files and global git-template hooks as monitored, change-controlled artifacts on developer endpoints, and for scoping developer-workstation credential exposure (npm tokens, cloud keys, LLM API keys) as a blast-radius question rather than assuming install-script scanning covers it. Mechanics are in the referenced operational entry.

## Update — 2026-08-02T23:59:00Z

The prior weekly tracked this wave's front edge moving into the AI coding assistant's own trust configuration. This week the wave gained something it had lacked — independent cross-vendor agreement on who is running a significant part of it, and a named CI mechanism defenders can go and check.

Amazon published an attribution assessment covering three of the ecosystem's most consequential compromises, stating that "based on analysis of command-and-control (C2) indicators and TTPs, Amazon Threat Intelligence assesses with medium confidence that these campaigns are attributable to the DPRK-linked threat actor tracked as SAPPHIRE SLEET" — a cluster it also names as STARDUST CHOLLIMA, BlueNoroff, CageyChameleon and Alluring Pisces ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)). The access mechanism is consistent and is not a platform weakness: "in each case, the threat actor gained access by socially engineering a trusted maintainer of the package, then published a software update containing malicious code." ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)). Amazon also assesses that a small March 2025 compromise served as a testing ground for the more visible operations that followed ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)), and identifies an evasion design that has direct implications for how organisations scan: the payload "is designed to defeat scanners that evaluate packages one by one instead of reasoning about how they interact in a real dependency graph" ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)).

Google's threat-intelligence group published defender-facing guidance a day later and reached the same attribution independently, attributing the activity to an actor it now calls MIDNIGHT NEPTUNE, formerly known as UNC1069 ([Google Cloud Blog, 2026-07-30](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/)). Neither vendor states the equivalence itself; the reporting on Amazon's briefing does, recording that "security researchers track the group under several names, including UNC1069, Sapphire Sleet and Stardust Chollima" ([CyberScoop, 2026-07-29](https://cyberscoop.com/amazon-north-korea-open-source-software-attacks/)) — which is what makes this two vendors looking rather than one vendor being repeated. Its own assessment of the trend is unhedged on direction: "GTIG assesses with high confidence that the growth in very large-scale, open-source supply chain compromise campaigns, including use of worms and iterative compromises in 2025 and early 2026, represent a significant expansion in use of this tactic compared to prior years." ([Google Cloud Blog, 2026-07-30](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/)).

The most immediately actionable content is a named CI mechanism belonging to a different cluster: "UNC6780 (aka \"TeamPCP\") conducted extensive open source supply chain compromises targeting ecosystems like PyPI, npm, and Docker Hub. Initial infection vectors varied across incidents, and included abuse of the pull_request_target GitHub Actions trigger to obtain base repository secrets and write permissions." ([Google Cloud Blog, 2026-07-30](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/)). That trigger is worth singling out because it is not a misconfiguration in the usual sense — `pull_request_target` runs workflow code in the context of the base repository, with its secrets, deliberately, so a workflow that checks out or executes anything from the incoming fork hands those secrets to whoever opened the pull request. It is a design that behaves exactly as documented and is very easy to use wrongly.

**Defender takeaway:** the through-line from the prior weeklies holds — the initial-access objective is the maintainer, the pipeline and the developer's own toolchain rather than the registry — but this week adds two things a Swiss or European public-sector build estate can act on directly rather than track. The first is the CI trigger above. The second is a change in how package scanning has to work: if payloads are split so that no single package looks malicious in isolation, per-package scanning returns clean by design, and the control that still functions is time — a release-age cooldown that keeps a brand-new version out of builds during the hours in which these compromises are typically noticed and pulled. GTIG names the specific control and the specific value: "setting this value to at least 24 hours (1440 minutes) ensures that freshly published, potentially poisoned packages are quarantined until the broader security community has had time to identify and remove them" ([Google Cloud Blog, 2026-07-30](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/)). The axios case is the argument for it: "while the malicious versions of axios were removed from the npm registry within three hours of their release, the scope of the compromise is estimated to be broad, as the package has over 100 million weekly downloads" ([Google Cloud Blog, 2026-07-30](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/)) — fast removal did not help, because the pull volume in those three hours was enormous.

## Update — 2026-08-09T23:45:00Z

The wave prior weeklies tracked from install-hook evasion, through abuse of the trust machinery around packages, to poisoned AI coding-assistant tool configurations produced its largest single event this week. Two things changed at week level that the day-by-day entries do not carry.

The first is that what looked like two events is one. The compromise of the keyv and cacheable npm namespaces, reported on 4 August by Socket and independently by several other vendors within roughly 48 hours, is the same wave this pipeline covered as CHAINDROP two days later: Socket traces it to a compromised maintainer account whose packages "were published with a malicious preinstall hook (setup.mjs) that downloads a standalone Bun runtime, executes an obfuscated second stage, harvests cloud and CI credentials, and republishes trojanized versions of other packages the stolen npm token can reach" ([Socket Threat Research, 2026-08-04](https://socket.dev/blog/popular-npm-packages-in-the-keyv-and-cacheable-namespaces-compromised-in-active-supply-chain)), the same mechanics Elastic and Unit 42 later detailed under the CHAINDROP name. The reach matters because of where these packages sit: keyv resolves as a transitive dependency beneath common tooling rather than as something teams install deliberately, so most affected estates never chose it.

The second delta is an operational order that inverts the standard reflex, and it is the reason this status entry exists rather than a line in the roll-up. Socket documents a host-level dead-man's switch installed alongside the credential theft — a watcher registered as a launch agent on macOS and as a lingering user-level service on Linux, polling the GitHub API with the stolen token roughly once a minute. Its instruction to responders is explicit: "Before rotating any credential, hunt for and remove the host-level dead-man's switch. Revocation is its trigger: the watcher runs eval on a remote-supplied handler the moment the stolen token returns an HTTP 4xx." Every incident-response playbook opens with credential rotation; on this campaign that step executes attacker code on the host. The corollary for anyone who has already rotated is that the switch has already fired, and the host needs treating accordingly.

Alongside that, the cross-vendor convergence hardened the strategic conclusion the operational entries reached from the other direction. Unit 42's analysis found a path that trades a runner OIDC token at npm's trusted-publishing endpoint for a real publish credential and then signs the result through the public transparency infrastructure, producing provenance it is explicit is not forged ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)). Socket states the general form: "provenance attests build integrity, not source integrity. The npm and sigstore pipeline did exactly what it is designed to do and still produced a signed, verifiable attestation for malware, because the source it built from was already trojanized." An organisation that added provenance verification to its dependency policy in the past year — a reasonable thing to have done — has a control that would have passed this package.

**Defender takeaway:** the two levers this week's evidence supports are both about ordering and neither is new tooling. Sequence the response correctly on any developer or build host that installed an affected package — persistence removal first, credential rotation second, and treat the host as compromised rather than the credential — and adjust what a passing provenance attestation is allowed to conclude in your dependency policy: it establishes that the artefact came from the declared build pipeline, and says nothing about whether the source that pipeline consumed was clean. A release-age cooldown before installs, which a prior weekly already recorded, remains the cheapest control that would have caught this class, because the malicious versions were identified within hours of publication.

**Triage:** the credential-harvesting stage runs at install time from a package manager's process tree, which is the discriminator against ordinary developer activity — build scripts legitimately spawn interpreters, but a package install that downloads and executes a fresh language runtime is not a normal build step. For the persistence, the artefacts Socket names are a user-scoped launch agent and a lingering user-level service whose job is to make an HTTP request on a timer; a periodic outbound API call from a user-level service on a developer laptop is unremarkable in isolation, and is the signal when it appeared in the same window as a package installation.
