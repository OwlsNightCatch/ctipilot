---
schema: 1
kind: threat
horizon: operational
title: Mastra npm supply-chain compromise (easy-day-js)
headline: Mastra npm supply-chain compromise (easy-day-js)
summary: >
  Deep dive: the Mastra AI framework's entire npm namespace was backdoored. A trojanised
  easy-day-js look-alike dependency was swept as a production dependency into 140+ @mastra/*
  packages in under 90 minutes, delivering a cross-platform credential/wallet stealer; the
  publishing-account access vector is not disclosed by the primaries (JFrog, 2026-06-17).
discovered_at: "2026-06-18T05:10:36Z"
updated_at: "2026-06-21T04:55:02Z"
event_date: 2026-06-17
run_id: 2026-06-18-aa7ee817
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - identity
  - nation-state
  - north-korea-nexus
regions:
  - global
sectors:
  - technology
  - finance
entities: []
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://research.jfrog.com/post/easy-day-js/"
    publisher: JFrog Security Research
    role: primary
  - url: "https://socket.dev/blog/mastra-npm-packages-compromised"
    publisher: Socket
    role: corroborating
  - url: "https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/"
    publisher: Microsoft Threat Intelligence
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/microsoft-links-mastra-ai-supply-chain-attack-to-north-korean-hackers/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://snyk.io/blog/a-forgotten-contributor-account-compromised-the-entire-mastra-npm-package-scope/"
    publisher: Snyk
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
references: []
weekly_section: null
deep_dive: true
deep_dive_category: supply-chain
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-06-21T04:55:02Z"
    run_id: 2026-06-21-2b75e32c
    type: update
    summary: >
      Microsoft now attributes last week's Mastra npm scope compromise to North Korea's Sapphire Sleet
      (BlueNoroff) and discloses the access vector our 2026-06-18 coverage could not: a dormant
      maintainer account that retained publish rights across all 142 @mastra packages
      (BleepingComputer, 2026-06-20).
    fields:
      - sectors
      - sources
      - tags
      - body
    merged_from: 2026-06-21/mastra-npm-scope-compromise-attributed-to-north-korea-with-t
migrated_from: briefs/2026-06-18.md
---

On 2026-06-17 the entire npm namespace of Mastra — an open-source JavaScript/TypeScript framework for building AI applications, with roughly 1.1 million combined weekly downloads — was backdoored through a single poisoned transitive dependency ([JFrog, 2026-06-17](https://research.jfrog.com/post/easy-day-js/) · [Socket, 2026-06-17](https://socket.dev/blog/mastra-npm-packages-compromised)). This is a clean worked example of the failure mode that matters most for any organisation consuming open-source AI tooling: trust in a transitive dependency turns one compromised publishing path into ecosystem-wide code execution on developer and CI machines.

**Access vector.** The malicious `easy-day-js` and the wave of `@mastra/*` republishes were pushed through the project's npm publishing chain; the cited primaries (JFrog, Socket) document the result but do **not** disclose how the publishing account was obtained, so the brief makes no claim about the initial-access vector ([JFrog, 2026-06-17](https://research.jfrog.com/post/easy-day-js/)). What matters operationally is downstream regardless of vector: a trusted scope published code that executed on every consumer at install time.

**The dependency-substitution chain.** Rather than poisoning a Mastra package directly, the attacker moved the malicious behaviour one level down into a new dependency named `easy-day-js` — a trojanised look-alike of the popular `dayjs` date library. A clean version was published first so the semver caret range looked benign, then the malicious `easy-day-js@1.11.22` was published; an automated wave added it as a *production* dependency across 140+ `@mastra/*` packages, with the malicious versions published between roughly 01:15 and 02:36 UTC — under 90 minutes ([Socket, 2026-06-17](https://socket.dev/blog/mastra-npm-packages-compromised)). The two-stage timing is a deliberate attempt to defeat naive dependency-pinning checks. Maps to `T1195.002` ([Compromise Software Supply Chain](https://attack.mitre.org/techniques/T1195/002/)) layered on `T1195.001` ([Compromise Software Dependencies and Development Tools](https://attack.mitre.org/techniques/T1195/001/)).

**Execution and second stage.** The malicious package carries a `postinstall` lifecycle hook (`node setup.cjs`) that runs automatically during `npm install` / `npm ci` (`T1059.007` — [JavaScript](https://attack.mitre.org/techniques/T1059/007/)). The stage-1 loader disables TLS certificate validation (`NODE_TLS_REJECT_UNAUTHORIZED=0`), writes marker files to the OS temp directory, downloads a stage-2 Node.js payload, spawns it as a detached hidden process, and deletes `setup.cjs` to frustrate static analysis ([JFrog, 2026-06-17](https://research.jfrog.com/post/easy-day-js/)). The stage-2 is a cross-platform (Windows / macOS / Linux) backdoor that beacons host identity and enumerates installed crypto-wallet browser extensions and saved-credential stores, then polls a C2 for follow-on shell/Node commands (`T1071.001` — [Application Layer Protocol: Web](https://attack.mitre.org/techniques/T1071/001/)).

**Persistence — platform-specific, NVM/Node-masquerading.** Stage-2 installs persistence tailored to the OS: a per-user LaunchAgent on macOS (`T1543.001` — [Launch Agent](https://attack.mitre.org/techniques/T1543/001/)), a systemd *user* service on Linux (`T1543.002` — [Systemd Service](https://attack.mitre.org/techniques/T1543/002/)), and an `HKCU\…\CurrentVersion\Run` key on Windows (`T1547.001` — [Registry Run Keys](https://attack.mitre.org/techniques/T1547/001/)). The labels masquerade as Node Version Manager / Node tooling — a useful hunt concept rather than a hardcoded indicator: persistence entries that *look* like NVM/Node housekeeping but point at scripts under a user profile or `ProgramData` path are the tell.

**Detection concepts (no IOCs).** Hunt for `node` processes spawned from the OS temp directory (Sysmon EID 1 with parent `node`/`npm`/`npx` and an image path under `%TEMP%` or `/tmp`); for new per-user persistence (LaunchAgent / systemd user unit / `HKCU` Run key) created by a `node` parent immediately after a package install; and for `npm`/`node` processes making outbound TLS where certificate validation has been disabled. Reputable package-security tooling flagged `easy-day-js` within minutes of publication, so dependency-scanning telemetry is a high-signal early-warning surface.

**Hardening.** Run `npm ls easy-day-js` across all workspaces and CI runners and remove the dependency; treat any host that installed an affected `@mastra/*` version in the exposure window as compromised and rotate all secrets, tokens and wallet material present on it. Structurally: enforce `--ignore-scripts` (or vetted allowlists) for install-time lifecycle hooks in CI, require lockfile hash/integrity verification and npm provenance attestation, and as general supply-chain hygiene audit npm org membership so publish/maintainer rights stay scoped to active maintainers.

## Update — 2026-06-21T04:55:02Z

The deep dive on 2026-06-18 documented the `easy-day-js` poisoning of 140+ `@mastra` packages but noted the cited primaries did not disclose *how* the publishing account was obtained, and made no attribution. Microsoft Threat Intelligence has now closed both gaps: it attributes the operation to North Korea's **Sapphire Sleet** (BlueNoroff / UNC1069) and states the access vector was a **dormant former-contributor npm account (`ehindero`) whose publish rights across the entire `@mastra` scope were never revoked** ([BleepingComputer, 2026-06-20](https://www.bleepingcomputer.com/news/security/microsoft-links-mastra-ai-supply-chain-attack-to-north-korean-hackers/)).

Microsoft's analysis details the post-install chain — `easy-day-js` disables TLS verification, pulls a cross-platform Node.js implant that enumerates 166 cryptocurrency-wallet browser extensions and steals browser profiles, then establishes a `scdev` svchost service running as SYSTEM for boot persistence ([Microsoft Threat Intelligence, 2026-06-17](https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/)). Snyk independently confirms the dormant-account root cause and notes npm does not expire scope-publish permissions on inactivity ([Snyk, 2026-06-16](https://snyk.io/blog/a-forgotten-contributor-account-compromised-the-entire-mastra-npm-package-scope/)). The defender action shifts from "remove `easy-day-js`" to a structural control: audit your own private-registry and package-scope ACLs for dormant accounts with retained publish rights, and enforce time-bound or MFA-gated publish tokens. Microsoft notes this is Sapphire Sleet's second npm scope-takeover of 2026 (after Axios in April) — a systematised dormant-high-privilege-account hunt, not a one-off.
