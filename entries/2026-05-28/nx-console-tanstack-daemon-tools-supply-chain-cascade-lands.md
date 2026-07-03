---
schema: 1
kind: vulnerability
horizon: operational
title: Nx Console / TanStack / DAEMON Tools supply-chain cascade lands three CISA KEV entries
headline: Nx Console / TanStack / DAEMON Tools supply-chain cascade lands three CISA KEV entries
summary: "CISA added three supply-chain CVEs to KEV on 2026-05-27 — the Nx Console / TanStack / DAEMON Tools cascade. The Nx Console v18.95.0 VS Code extension compromise (CVE-2026-48027) ultimately traces to a TanStack Router npm supply-chain bug (CVE-2026-45321) that exfiltrated a contributor's GitHub CLI OAuth token; GitHub later confirmed that roughly 3,800 internal repositories and Grafana Labs were also breached. Separately, CVE-2026-8398 covers a six-week trojanisation of signed DAEMON Tools Lite builds 12.5.0.2421–12.5.0.2434 from the official vendor build pipeline."
discovered_at: "2026-05-28T05:00:11Z"
event_date: 2026-05-21
run_id: 2026-05-28-3e33200a
priority: high
immediate_action: null
tags:
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
  - url: "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"
    publisher: CISA KEV catalog
    role: corroborating
closed_sources: []
evidence:
  - quote: Background.
    publisher: ctipilot v2 brief (migrated)
verification: multi-source
sourcing_note: "migration: evidence backfilled from v2 brief body (item predates the Evidence footer field)"
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-28.md
---

**Background.** The CISA KEV adds on 2026-05-27 close a chain of disclosures across the preceding three weeks that share a single operational pattern: trusted developer-tooling-publishing pipelines (a maintainer's machine, a vendor build server, a popular VS Code marketplace listing) used to push malicious code to downstream consumers at scale ([CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog); [Nx postmortem, 2026-05-19](https://nx.dev/blog/nx-console-v18-95-0-postmortem); [GHSA-c9j4-9m59-847w, 2026-05-18](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w); [GHSA-g7cv-rxg3-hmpx, 2026-05-11](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx); [Disc Soft Limited, 2026-05-06](https://blog.daemon-tools.cc/post/security-incident); [Kaspersky, 2026-05-05](https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/); [Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)). This brief has covered the upstream story before — `campaign:mini-shai-hulud` (TeamPCP) and the 2026-05-24 Packagist `Laravel-Lang` deep dive both documented the same class of postinstall / publish-token theft chain. The Nx Console / TanStack thread is materially new because three of its CVEs were promoted to CISA KEV on the same day (2026-05-27), confirming active in-the-wild exploitation, and because GitHub's CISO Alexis Wales publicly confirmed that the resulting credential-harvest reached approximately 3,800 internal GitHub repositories along with Grafana Labs.

**The TanStack → Nx Console pivot — CVE-2026-45321 and CVE-2026-48027.**

The chain begins on or before 2026-05-11 with [GHSA-g7cv-rxg3-hmpx](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx) (CVE-2026-45321): malicious versions across approximately 42 `@tanstack/*` npm packages were published with a credential-stealing payload that read locally configured credentials and exfiltrated them — including a Nx contributor's GitHub CLI OAuth token. The Nx postmortem specifically names `@tanstack/zod-adapter@1.166.15` as the resolved malicious dependency on the compromised contributor's machine. Mapped to `T1195.002` Compromise Software Supply Chain → `T1552.001` Unsecured Credentials: Credentials In Files. Seven days later, the attacker used the stolen token to publish Nx Console v18.95.0 (CVE-2026-48027, [GHSA-c9j4-9m59-847w](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w)) via the legitimate publish path. The malicious version was live on the Visual Studio Marketplace from 12:30 to 12:48 UTC on 2026-05-18 and on Open VSX from 12:33 to 13:09 UTC. Nx Console is a VS Code extension with approximately 2.2 million reported installs; during the live window it fetched an obfuscated second-stage payload that harvested secrets from 1Password vaults, Claude Code configuration files, the developer's npm authentication, additional GitHub PATs, and AWS credentials from `~/.aws/credentials`.

The Nx postmortem maps the publish-step compromise cleanly: the stolen GitHub CLI OAuth token had `repo` and `write:packages` scope on the maintainer's machine, which was enough to push a new tag and trigger the existing publish workflow without further authentication. The CI workflow ran in GitHub-hosted runners with the regular publish secrets — no additional human-in-the-loop on the publish step. This is the same architectural class of compromise as the earlier TeamPCP `mini-shai-hulud` chain covered in `briefs/2026-05-13.md` and the Packagist `Laravel-Lang` autoloader-backdoor covered in `briefs/2026-05-24.md`: a stolen developer credential turned into automated downstream-publish without secondary review.

**CVE-2026-8398 — DAEMON Tools Lite signed-build trojanisation.**

CVE-2026-8398 covers a separate but parallel compromise of the official Disc Soft Limited build pipeline. DAEMON Tools Lite versions 12.5.0.2421 through 12.5.0.2434, distributed from 2026-04-08 through 2026-05-05, contained trojanised `DTHelper.exe`, `DiscSoftBusServiceLite.exe`, and `DTShellHlp.exe` binaries signed with a valid AVB Disc Soft code-signing certificate and beaconing to attacker infrastructure on activation ([Disc Soft Limited, 2026-05-06](https://blog.daemon-tools.cc/post/security-incident); [Kaspersky, 2026-05-05](https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/)). Kaspersky identified thousands of attempted secondary-payload installs against affected hosts during the six-week distribution window. The Disc Soft vendor advisory confirms the build infrastructure itself was compromised — the malicious binaries went through the legitimate signing path, not via a publication-credential theft. Safe version: 12.6.0+. The CVE moved to CISA KEV on 2026-05-27 on the strength of in-the-wild exploitation evidence Kaspersky and other vendors contributed.

**Downstream impact — what GitHub and Grafana Labs publicly confirmed.**

Help Net Security reported on 2026-05-21 ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)) that GitHub CISO Alexis Wales had publicly named the malicious Nx Console v18.95.0 extension as the root-cause vector for the earlier 2026 GitHub breach in which ~3,800 internal repositories were exfiltrated. Grafana Labs separately reported a breach traced to the same vector. The downstream-victim pattern is operationally significant: a single malicious VS Code extension live for 18 minutes was enough to reach internal corporate networks via developer-endpoint credential harvesting.

**Detection and hardening — what to push to operators today.**

ATT&CK mapping: `T1195.002` Compromise Software Supply Chain (publish-path compromise), `T1552.001` Unsecured Credentials: Credentials In Files (1Password / `~/.aws/credentials` / Claude Code config harvesting), `T1530` Data from Cloud Storage Object (downstream CI/CD secret reuse), `T1567` Exfiltration Over Web Service.

Detection: EDR parent-process lineage `vscode.exe` / `cursor.exe` / `windsurf.exe` spawning `node.exe` with outbound network egress to non-standard hosts (`Extension Host Worker` is the legitimate child; secondary `node.exe` workers fetching obfuscated payloads are not); audit VS Code extension marketplace installs across the developer estate against an approved-extensions allowlist; flag any installation of `nrwl.angular-console` (the Nx Console publisher ID) at a version pinned to `18.95.0`. For DAEMON Tools Lite: hunt for `DTHelper.exe` or `DTShellHlp.exe` invocations with parent-process or file-modify timestamps inside the 2026-04-08 → 2026-05-05 window and a hash that does not match the post-12.6.0 reference set (use the vendor's published file-list, do not redistribute hashes here).

Hardening: enforce an organisational policy controls list for VS Code / Cursor / Windsurf extensions (the marketplaces do not enforce mandatory code-signing on extensions); pin npm dependencies with lockfile + `--ignore-scripts` for CI/CD builds; require human approval for any package that adds or modifies `postinstall` / `preinstall` / `install` scripts; rotate every CI/CD secret, npm token, GitHub PAT, and AWS access key accessible from any host that ran an affected Nx Console version between 2026-05-18 12:30 and 13:09 UTC. For developer endpoints, treat any host that installed an extension from Open VSX or VS Code Marketplace in that window as potentially compromised — credential rotation is not optional.
