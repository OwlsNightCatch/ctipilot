---
schema: 1
kind: threat
title: "Fourteen trojanized npm packages drop RedC2 4.0's RedShell Linux implant from a module-load-time loader that needs no install hook, defeating --ignore-scripts entirely"
headline: "A plain `import` of a trojanized npm package is the whole exploit — no install hook, no exported call, no coverage from --ignore-scripts"
summary: >
  TrendAI Research published a technical analysis of fourteen trojanized npm packages — small calendar/streak
  date-math utilities — that each bundle a Linux ELF binary and a loader executed at module load time via an async
  IIFE, requiring no install hook and no exported function call. A single transitive import anywhere in a dependency
  graph is sufficient to trigger it. The dropped binary is RedShell, the native Linux implant for RedC2 4.0, a
  commodity, actively-developed cross-platform C2 framework sold on Hack Forums that ships an LLM-backed "Red Agent"
  component converting natural-language operator intent into beacon command chains.
discovered_at: "2026-08-29T04:09:36Z"
updated_at: null
event_date: "2026-08-20"
run_id: 2026-08-29T0409Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, infostealer, ai-abuse]
regions: [global]
sectors: [technology, public-sector]
entities:
  - tool:redc2
techniques: [T1195.002, T1059.004, T1053.003, T1543.002, T1572, T1620, T1552.004, T1555.003, T1573, T1090.001]
affected_products: []
cves: []
sources:
  - url: "https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/redc2-ai-powered-linux-implant"
    publisher: "TrendAI Research (Trend Micro)"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence:
  - quote: "One import anywhere in the dependency graph is sufficient, including from a transitive dependency the developer never selected."
    publisher: "TrendAI Research"
  - quote: "Certificate verification is explicitly disabled via SSL_VERIFY_NONE, meaning the malware will accept any server certificate without validation, allowing the C&C operator to use self-signed or otherwise invalid certificates freely."
    publisher: "TrendAI Research"
  - quote: "RedC2 ships with an AI assistant called Red Agent, an LLM-backed command execution layer that turns natural-language intent into framework beacon commands. It is exposed through /ra in any beacon terminal, in both the web UI and the EXT client."
    publisher: "TrendAI Research"
verification: single-source
sourcing_note: "TrendAI Research (Trend Micro) is the sole discloser of this technical analysis; no independent lab has corroborated it as of publication. The finding was surfaced via an aggregator write-up initially and traced to this vendor primary this run."
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

TrendAI (Trend Micro) Research published a technical analysis, dated 2026-08-20, of a cluster of fourteen trojanized
npm packages — small, functional calendar/streak date-math utilities such as `streak-metrics-math`, `kit-map-vim`
and `streak-map-cache` — that each bundle a Linux ELF binary alongside genuine, working date-helper code
([TrendAI Research, 2026-08-20](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/redc2-ai-powered-linux-implant)).
The package's loader re-exports the genuine helpers so the package works as advertised, then runs an async IIFE
(immediately invoked function expression) evaluated at module load: it marks the bundled binary executable, verifies
its hash against a hardcoded constant, and spawns it detached so it outlives the importing Node process
([TrendAI Research, 2026-08-20](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/redc2-ai-powered-linux-implant)).
No install hook or exported function call is involved, so `--ignore-scripts` provides no coverage, and a single
transitive import anywhere in a dependency graph — even one the developer never directly selected — is sufficient to
trigger execution ([TrendAI Research, 2026-08-20](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/redc2-ai-powered-linux-implant)).

The dropped binary is RedShell, the native Linux implant for RedC2 4.0, a modular, actively-developed cross-platform
(Windows/macOS/Linux) command-and-control framework marketed on Hack Forums. On execution, RedShell ignores SIGPIPE,
double-forks to daemonize, and connects to a hardcoded primary C2 host over TCP with aggressive keepalive tuning,
wrapping the session in TLS with certificate verification explicitly disabled — accepting any server certificate,
self-signed or otherwise, without validation — and TLS 1.2 enforced as the minimum version
([TrendAI Research, 2026-08-20](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/redc2-ai-powered-linux-implant)).
A persistent per-host installation ID is cached in a dotfile under `$HOME` so re-infection state survives restarts.
RedShell exposes a broad Linux-native command set to the operator: interactive shell execution, SSH-key and
browser-credential harvesting, database discovery, bulk exfiltration over HTTP or to third-party file-sharing
services, fileless ELF execution via `memfd_create`, arbitrary shellcode execution via `mmap`, `dlopen`-based
shared-library loading, SOCKS5 proxying and TCP port forwarding, and cross-network reverse-shell tunnelling brokered
through the C2 server; persistence is established through cron, `.bashrc`, a user-level systemd service, or an XDG
autostart entry ([TrendAI Research, 2026-08-20](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/redc2-ai-powered-linux-implant)).
The framework additionally ships an LLM-backed component RedC2's own documentation calls Red Agent — a different
tool from Wiz's own similarly-named "Red Agent" autonomous red-teaming tool, an unrelated defensive research
product — exposed via a `/ra` command in the beacon terminal, described as trained on the framework's command set
to break a single natural-language operator prompt into an ordered chain of beacon commands
([TrendAI Research, 2026-08-20](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/redc2-ai-powered-linux-implant)).

Detection concept: process-creation telemetry showing a Node.js/npm-installed package's module import immediately
spawning a detached, double-forking child process that opens an outbound TLS session accepting an invalid or
self-signed certificate without validation — legitimate npm packages that bundle native binaries (for example via
prebuilt node-gyp addons) do so at install time through a documented hook, not as a side effect of a plain import
with no exported function called. **Triage:** a package with a bundled native binary that is invoked only from
install-time hooks is routine; one invoked from a plain module-load side effect, with no install hook present at
all, is the discriminator. **Defender takeaway:** treat `--ignore-scripts` as insufficient supply-chain mitigation on
its own; pin exact package hashes in CI/CD, run dependency installs in network-egress-restricted sandboxes, and
audit transitive dependencies for bundled non-JavaScript binaries rather than relying on install-hook scanning
alone.
