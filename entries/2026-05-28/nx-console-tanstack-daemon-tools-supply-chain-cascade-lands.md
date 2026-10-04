---
schema: 1
kind: vulnerability
title: Nx Console / TanStack / DAEMON Tools supply-chain cascade lands three CISA KEV entries
headline: Nx Console / TanStack / DAEMON Tools supply-chain cascade lands three CISA KEV entries
summary: "CISA added three supply-chain CVEs to KEV on 2026-05-27, the Nx Console / TanStack / DAEMON Tools cascade. The Nx Console v18.95.0 VS Code extension compromise (CVE-2026-48027) traces to the TanStack npm supply-chain compromise (CVE-2026-45321), whose payload exfiltrated a contributor's GitHub CLI OAuth token. GitHub's CISO named the extension as the vector for the theft of about 3,800 GitHub internal repositories, and Grafana Labs traced its own breach to the upstream TanStack compromise. Separately, CVE-2026-8398 covers a roughly four-week trojanisation of signed DAEMON Tools Lite builds 12.5.0.2421 to 12.5.0.2434 from the vendor's build environment."
discovered_at: "2026-05-28T05:00:11Z"
event_date: 2026-05-21
run_id: 2026-05-28-3e33200a
priority: high
immediate_action: null
tags:
  - ransomware
  - supply-chain
  - vulnerabilities
  - actively-exploited
  - cisa-kev
  - identity
regions:
  - global
  - europe
sectors:
  - technology
  - public-sector
entities:
  - "actor:teampcp"
  - "campaign:mini-shai-hulud"
  - "incident:nx-console-vs-code-extension-18-95-0-compromised-stolen-publ"
  - "incident:daemon-tools-supply-chain-2026"
techniques: [T1195.002, T1552.001, T1567]
affected_products: ["Nx Console", "DAEMON Tools Lite"]
cves:
  - id: CVE-2026-48027
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
  - id: CVE-2026-45321
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
  - id: CVE-2026-8398
    cvss: n/a
    epss: null
    type: null
    vector: user-interaction
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
sources:
  - url: "https://nx.dev/blog/nx-console-v18-95-0-postmortem"
    publisher: Nx postmortem
    role: primary
  - url: "https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w"
    publisher: GitHub Security Advisory GHSA-c9j4-9m59-847w
    role: corroborating
  - url: "https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx"
    publisher: TanStack Router GHSA-g7cv-rxg3-hmpx
    role: corroborating
  - url: "https://blog.daemon-tools.cc/post/security-incident"
    publisher: Disc Soft Limited security incident notice
    role: corroborating
  - url: "https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/"
    publisher: Kaspersky DAEMON Tools analysis
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/"
    publisher: Help Net Security on GitHub root cause
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV catalog"
    date: "2026-05-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "TanStack contains an unspecified vulnerability that allowed malicious versions of the product to be published to the npm registry to publish credential-stealing malware under a trusted identity."
    publisher: "CISA KEV catalog"
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-28.md
updates:
  - at: "2026-09-30T07:16:54Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      CISA's catalog is now cited for the 2026-05-27 KEV additions, and CISA marks the Nx Console
      and TanStack compromises as used in known ransomware campaigns. Claims no source carries are
      removed: token scopes, a tag push, hosted-runner publish secrets, Claude Code or AWS
      credential-file harvesting, GitHub confirming Grafana's breach, Kaspersky supplying KEV
      evidence, a vendor statement about the signing path, a six-week window, unsigned marketplace
      extensions and an uncited Laravel-Lang comparison. The payload and GitHub-breach sentences
      cite the pages that carry them, and the detection guidance follows the postmortem's version
      check and persistence artifacts. An exposure line gives the affected versions and the reach of
      the malicious Nx Console release, Grafana's extortion is noted, and a cited takeaway closes
      the analysis. The Mini Shai-Hulud campaign and the Nx Console and DAEMON Tools incidents are
      linked. The exposure and detection lines now also cover the upstream TanStack compromise as
      TanStack's advisory describes it.
    fields: [sources, body, evidence, sourcing_note, classification, techniques, tags, summary, entities, affected_products]
---

**Background.** The CISA KEV adds on 2026-05-27 close a chain of disclosures across the preceding three weeks that share a single operational pattern: trusted developer-tooling-publishing pipelines (a maintainer's machine, a vendor build server, a popular VS Code marketplace listing) used to push malicious code to downstream consumers at scale ([CISA KEV catalog, 2026-05-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json); [Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem); [GHSA-c9j4-9m59-847w, 2026-05-18](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w); [GHSA-g7cv-rxg3-hmpx, 2026-05-11](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx); [Disc Soft Limited, 2026-05-06](https://blog.daemon-tools.cc/post/security-incident); [Kaspersky, 2026-05-05](https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/); [Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)). The TanStack compromise was carried out via Mini Shai-Hulud, TeamPCP's self-replicating worm that steals CI/CD credentials and uses them to publish infected versions of more packages ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)). Three of the chain's CVEs were added to CISA KEV on the same day (2026-05-27), confirming in-the-wild exploitation ([CISA KEV catalog, 2026-05-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)), and GitHub's CISO Alexis Wales named the malicious Nx Console extension as the vector for the theft of about 3,800 of GitHub's internal repositories ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)).

**The TanStack → Nx Console pivot: CVE-2026-45321 and CVE-2026-48027.**

The chain begins on 2026-05-11 with [GHSA-g7cv-rxg3-hmpx](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx) (CVE-2026-45321): 84 malicious versions across 42 `@tanstack/*` npm packages were published with a credential-stealing payload ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). On a Nx contributor's machine the payload read locally stored credentials and exfiltrated them, including the contributor's GitHub CLI OAuth token. The Nx postmortem names `@tanstack/zod-adapter@1.166.15` as the malicious dependency resolved on that machine ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). Seven days later, the attacker published Nx Console v18.95.0 as a legitimate Nx core contributor ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)), tracked as CVE-2026-48027 ([CISA KEV catalog, 2026-05-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). The malicious version was live on the Visual Studio Marketplace from 12:30 to 12:48 UTC on 2026-05-18 and on Open VSX from 12:33 to 13:09 UTC ([GHSA-c9j4-9m59-847w, 2026-05-18](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w)). Nx Console is a VS Code extension with 2.2 million installs ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)). The payload ran on extension activation in VS Code or a fork such as Cursor and harvested Vault tokens, npm tokens, AWS metadata-service, Secrets Manager, SSM and Web Identity credentials, GitHub tokens, the contents of an active 1Password `op` CLI session, SSH private keys, `.env` files and GCP and Docker credentials ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). The advisory describes it as an obfuscated payload that the extension fetched, and says the harvested data was exfiltrated over HTTPS, the GitHub API and DNS ([GHSA-c9j4-9m59-847w, 2026-05-18](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w)).

The advisory says the leaked credentials "allowed the attacker to run workflows on our GitHub repository as a contributor" ([GHSA-c9j4-9m59-847w, 2026-05-18](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w)). The postmortem names the gap that let this become a release: until the incident any core contributor could publish a new Nx Console version without a second human's approval, with no required-reviewer rule and no environment gate ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). A stolen developer credential therefore turned into a downstream publish without secondary review.

**CVE-2026-8398: DAEMON Tools Lite signed-build trojanisation.**

CVE-2026-8398 covers a separate but parallel compromise of Disc Soft Limited's build environment. DAEMON Tools Lite versions 12.5.0.2421 through 12.5.0.2434, circulating since 2026-04-08, contained trojanised `DTHelper.exe`, `DiscSoftBusServiceLite.exe`, and `DTShellHlp.exe` binaries signed with a valid AVB Disc Soft digital signature, which contact a command-and-control server at every system start ([Kaspersky, 2026-05-05](https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/)). Disc Soft says it found "unauthorized interference within our infrastructure" and that certain installation packages "were impacted within our build environment and were released in a compromised state". It released the clean version 12.6 on 2026-05-05 ([Disc Soft Limited, 2026-05-06](https://blog.daemon-tools.cc/post/security-incident)). Kaspersky detected several thousand attempts to install additional payloads through infected installations during the roughly four-week distribution window ([Kaspersky, 2026-05-05](https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/)). Safe version: 12.6 or later. CISA added the CVE to KEV on 2026-05-27 ([CISA KEV catalog, 2026-05-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

**Downstream impact: what GitHub and Grafana Labs publicly confirmed.**

GitHub CISO Alexis Wales named the malicious Nx Console v18.95.0 extension, installed by a GitHub employee, as the vector for GitHub's breach in which about 3,800 private repositories were exfiltrated ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)). Grafana Labs' CISO Joe McManus traced Grafana's separate GitHub breach to "a TanStack npm supply chain attack via the Mini Shai-Hulud campaign", not to Nx Console, so both breaches trace back to the TanStack compromise by different routes ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)). The malicious version was live for less than an hour (about 18 minutes on the Visual Studio Marketplace and 36 on Open VSX) ([GHSA-c9j4-9m59-847w, 2026-05-18](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w)); the postmortem's summary gives about 11 minutes for the Marketplace, counted from the maintainers' first alert ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)), and one install by a GitHub employee was enough for the attackers to reach GitHub's private repositories ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)).

**Detection and hardening: what to push to operators today.**

**Exposure:** for Nx Console, only 18.95.0 is affected, in VS Code and forks such as Cursor. Earlier and later versions are not, and 18.100.0 is the fixed release ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). The Visual Studio Marketplace reports 28 installs of 18.95.0 and Open VSX 41 downloads from 21 unique IPs, while Nx's own analytics count about 6,000 activations of that version, so Nx says anyone who had the extension with auto-update enabled between 12:30 and 13:09 UTC on 2026-05-18 should assume compromise ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). The 2.2 million installs are the extension's overall count, not those of the malicious version ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)). For DAEMON Tools Lite, the trojanised builds are 12.5.0.2421 to 12.5.0.2434, in circulation from 2026-04-08 ([Kaspersky, 2026-05-05](https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/)). Disc Soft says only the free 12.5.1 release was affected, not the paid Lite, Ultra or Pro products, and that 12.6 is clean ([Disc Soft Limited, 2026-05-06](https://blog.daemon-tools.cc/post/security-incident)). For the upstream TanStack compromise (CVE-2026-45321), TanStack says any developer or CI environment that ran an npm, pnpm or yarn install against an affected `@tanstack/*` version on 2026-05-11 should be considered compromised, with every credential the install process could reach rotated and cloud audit logs reviewed for activity from those hosts ([GHSA-g7cv-rxg3-hmpx, 2026-05-11](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx)).

**Detection:** inventory installed editor extensions on developer hosts for Nx Console at exactly version 18.95.0 (the postmortem's check lists extensions with their versions and filters on `angular-console`) ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). On hosts that ran it, look for the payload's persistence: a Python backdoor under the user profile with staging and state files in temporary directories, a LaunchAgent on macOS, attempted `/etc/sudoers` changes on Linux, and a Bun runtime installed under the user profile on Windows ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). Updating to 18.100.0 is only the first remediation step: the advisory also says to kill the backdoor processes, which actively try to exfiltrate credentials, and to delete the persistence artifacts, so check patched hosts as well ([GHSA-c9j4-9m59-847w, 2026-05-18](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w)). For DAEMON Tools Lite: hunt for `DTHelper.exe` or `DTShellHlp.exe` invocations with parent-process or file-modify timestamps inside the 2026-04-08 → 2026-05-05 window and a hash that does not match the post-12.6 reference set (compare against the indicators Kaspersky links from its write-up ([Kaspersky, 2026-05-05](https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/))). For TanStack: a pinned `@tanstack/*` version is malicious if its published manifest carries an `optionalDependencies` entry for the fictitious `@tanstack/setup` package, with an undeclared obfuscated JavaScript payload of about 2.3 MB at the package root, and the CI pipelines to audit are those that ran an install against `@tanstack/*` between 19:20 and 19:30 UTC that day ([GHSA-g7cv-rxg3-hmpx, 2026-05-11](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx)).

Hardening: enforce an organisational policy controls list for VS Code / Cursor / Windsurf extensions (the malicious upload passed the Visual Studio Marketplace's automated signing, manifest and malware checks ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem))); pin npm dependencies with lockfile + `--ignore-scripts` for CI/CD builds; require human approval for any package that adds or modifies `postinstall` / `preinstall` / `install` scripts; rotate every CI/CD secret, npm token, GitHub PAT, and AWS access key accessible from any host that ran an affected Nx Console version between 2026-05-18 12:30 and 13:09 UTC. Treat any host that installed Nx Console 18.95.0, or had Nx Console installed with auto-update enabled in VS Code or a fork such as Cursor during that window, as potentially compromised ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)).

**Defender takeaway:** one stolen developer credential became a public release because any core contributor could publish Nx Console without a second human's approval ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). For a host that installed 18.95.0, the postmortem says to treat anything reachable from it as exposed and to rotate every credential that was on disk or could have been minted during the exposure window. Its lesson for any pipeline that can publish to a public registry is to require approval gating ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)).

## Correction — 2026-09-30T07:16:54Z

CISA's Known Exploited Vulnerabilities catalog marks both CVE-2026-48027 (Nx Console) and CVE-2026-45321 (TanStack) as used in known ransomware campaigns ([CISA KEV catalog, 2026-05-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). The attackers who stole Grafana Labs' codebase through the TanStack compromise demanded payment not to release or sell it, and Grafana did not pay ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)). Credentials exposed through either compromise are best handled on the assumption that an extortion group holds them.

The Nx postmortem does not describe token scopes, a tag push or hosted-runner publish secrets. It says any core contributor could publish without a second approval ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). The harvested credentials are Vault, npm, AWS service, GitHub, 1Password `op` session, SSH, `.env`, GCP and Docker secrets ([Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem)). GitHub named Nx Console only for its own breach, while Grafana Labs traced its breach to the TanStack npm attack ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)). The DAEMON Tools trojanised builds circulated for about four weeks, from 2026-04-08 until the clean 12.6 release on 2026-05-05 ([Kaspersky, 2026-05-05](https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/); [Disc Soft Limited, 2026-05-06](https://blog.daemon-tools.cc/post/security-incident)).
