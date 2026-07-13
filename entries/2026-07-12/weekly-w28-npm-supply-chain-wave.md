---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: 'npm supply-chain wave status: jscrambler package compromised this week, extending the install-hook-evasion pattern seen in the injectivelabs SDK'
headline: npm supply-chain wave — jscrambler (v8.14.0-8.20.0) pushed a Rust infostealer, moving the dropper out of the preinstall hook to evade scanners
summary: The npm supply-chain pressure this pipeline has tracked continued in 2026-W28. On 2026-07-11 the jscrambler npm package was compromised (v8.14.0 through 8.20.0) via a stolen publishing credential, pushing a Rust infostealer through an undocumented preinstall hook — then, from 8.18.0, relocating the identical dropper into a self-executing dist/index.js function specifically to evade install-script scanners. It targets cloud metadata credentials, CI tokens, browser and AI-tool configs and wallet seeds; Socket detected it 6 minutes after publication and 8.22.0 is clean. This mirrors the same install-hook-evasion evolution as this week's injectivelabs SDK compromise, though jscrambler has not been shown to self-propagate like the Shai-Hulud worm strain.
discovered_at: '2026-07-12T23:48:00Z'
event_date: 2026-07-11
run_id: 2026-07-12T2309Z-weekly
priority: notable
immediate_action: null
tags:
  - supply-chain
  - data-breach
  - infostealer
  - cloud
regions:
  - global
sectors:
  - technology
entities:
  - incident:jscrambler-npm-supply-chain-2026
  - incident:injectivelabs-npm-sdk-ts-supply-chain-2026
cves: []
techniques:
  - T1195.002
  - T1027
  - T1552.001
sources:
  - url: https://socket.dev/blog/jscrambler-supply-chain-attack
    publisher: Socket
    role: primary
  - url: https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence:
  - quote: Starting with 8.18.0 the install hook is gone entirely—the identical dropper is instead injected as a self-executing function at the top of dist/index.js.
    publisher: Socket
  - quote: Socket detected the compromised package 6 minutes after publication.
    publisher: Socket
verification: multi-source
sourcing_note: Two independent primaries (Socket's analysis, The Hacker News corroboration), both fetched this run. Reliability B, credibility 1 (corroborated). Framed as a fresh data point in the tracked npm-supply-chain wave, not a re-summary of the prior weekly's coverage.
confidence: high
classification:
  reliability: B
  credibility: 1
update_of: null
references:
  - 2026-07-10/injectivelabs-npm-runtime-keyhook-supply-chain-evasion
  - 2026-06-29/npm-supply-chain-worms-a-sustained-wave-across-the-week
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - Query build/CI dependency trees for jscrambler and pin it away from v8.14.0-8.20.0 (8.22.0 is clean); for any environment that installed an affected version between 2026-07-11 and remediation, rotate the credentials the stealer targets — cloud keys, CI/deploy tokens, and any secrets reachable from the build runner — and treat it as a compromise, not a risk.
---
The software-supply-chain pressure on the npm ecosystem that this pipeline has tracked as a sustained wave continued this week, with a fresh compromise that sharpens the evasion trend rather than repeating it.

On 2026-07-11 the **jscrambler** npm package — a code-protection/obfuscation build tool — was compromised via what Socket assesses as a stolen publishing credential or compromised build pipeline: a malicious v8.14.0 pushed directly to npm, bypassing the project's normal release flow, adding an undocumented `preinstall` hook that unpacks and detached-spawns a platform-specific Rust infostealer on `npm install` alone. The stealer targets cloud metadata-endpoint credentials, Kubernetes configs, browser secrets, crypto-wallet seeds, AI coding-tool configs and messaging tokens. The notable evolution: over roughly three hours the actor pushed four more malicious releases and, "starting with 8.18.0 the install hook is gone entirely—the identical dropper is instead injected as a self-executing function at the top of dist/index.js" — moving execution out of the very hook that install-script scanners watch ([Socket, 2026-07-11](https://socket.dev/blog/jscrambler-supply-chain-attack)). Socket "detected the compromised package 6 minutes after publication"; v8.22.0 is confirmed clean ([The Hacker News, 2026-07-11](https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html)). This is the same install-hook-evasion arc as this week's injectivelabs SDK compromise, though — unlike the Shai-Hulud worm strain — jscrambler has not been shown to self-propagate to other maintainers.

**Defender takeaway:** the wave's shared lesson for any org with a CI/CD JS build chain is that install-hook scanning is now routinely bypassed, so provenance controls (pinned versions/lockfile integrity, short-lived scoped CI credentials, egress control from build runners) matter more than install-time script inspection; a runner that installed an affected jscrambler build should be treated as a credential-exposure event. **Triage:** a compromised build package shows up as a build/CI process making unexpected outbound connections or reading cloud-metadata and secret paths during `install`/`build` — behaviour a legitimate obfuscation tool has no reason to exhibit.
