---
schema: 1
kind: synthesis
horizon: strategic
title: "TeamPCP → PCPJack — cloud-worm successor evicting prior operator artefacts"
headline: "TeamPCP → PCPJack — cloud-worm successor evicting prior operator artefacts"
summary: >
  Current state: SentinelLabs documented PCPJack on 2026-05-07 as a worm-class framework that
  evicts and deletes existing TeamPCP artefacts on compromise (giving the framework its name),
  then deploys six Python modules harvesting credentials from Docker, Kubernetes, Redis, MongoDB,
  RayML, and dozens of cloud / SaaS …
discovered_at: "2026-05-04T05:00:37Z"
updated_at: "2026-05-26T05:00:05Z"
event_date: 2026-05-10
run_id: 2026-W19-a5788b22
priority: high
immediate_action: null
tags:
  - organized-crime
  - cloud
  - vulnerabilities
  - actively-exploited
  - supply-chain
  - infostealer
  - ai-abuse
  - data-breach
  - ransomware
  - botnet
  - identity
  - nation-state
  - wiper
regions:
  - global
  - europe
sectors:
  - technology
  - public-sector
entities:
  - "campaign:mini-shai-hulud"
  - "tool:pcpjack-cloud-worm-2026"
  - "actor:teampcp"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.sentinelone.com/labs/cloud-worm-evicts-teampcp-and-steals-credentials-at-scale/"
    publisher: SentinelLabs — Cloud worm evicts TeamPCP
    role: primary
  - url: "https://thehackernews.com/2026/05/pcpjack-credential-stealer-exploits-5.html"
    publisher: The Hacker News — PCPJack credential stealer
    role: corroborating
  - url: "https://www.securityweek.com/pcpjack-worm-removes-teampcp-infections-steals-credentials/"
    publisher: SecurityWeek — PCPJack worm
    role: corroborating
  - url: "https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem"
    publisher: "StepSecurity, 2026-05-11"
    role: primary
  - url: "https://tanstack.com/blog/npm-supply-chain-compromise-postmortem"
    publisher: "TanStack post-mortem, 2026-05-12"
    role: corroborating
  - url: "https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised"
    publisher: "Wiz, 2026-05-12"
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12558"
    publisher: "NCSC-CH Security Hub #12558, 2026-05-12"
    role: corroborating
  - url: "https://techcrunch.com/2026/05/14/openai-says-hackers-stole-some-data-after-latest-code-security-issue/"
    publisher: "TechCrunch, 2026-05-14"
    role: primary
  - url: "https://therecord.media/openai-asks-macos-users-to-update-tanstack-npm"
    publisher: "The Record, 2026-05-14"
    role: corroborating
  - url: "https://www.ox.security/blog/new-actors-deploy-shai-hulud-clones-teampcp-copycats-are-here/"
    publisher: OX Security
    role: primary
  - url: "https://thehackernews.com/2026/05/four-malicious-npm-packages-deliver.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://isc.sans.edu/diary/rss/32994"
    publisher: SANS Internet Storm Center
    role: corroborating
  - url: "https://checkmarx.com/blog/ongoing-security-updates/"
    publisher: Checkmarx
    role: corroborating
  - url: "https://thehackernews.com/2026/05/github-investigating-teampcp-claimed.html"
    publisher: The Hacker News
    role: primary
  - url: "https://www.wiz.io/blog/durabletask-teampcp-supply-chain-attack"
    publisher: Wiz Security
    role: corroborating
  - url: "https://grafana.com/blog/grafana-labs-security-update-latest-on-tanstack-npm-supply-chain-ransomware-incident/"
    publisher: Grafana Labs
    role: corroborating
  - url: "https://therecord.media/github-confirms-teampcp-hack-customers-unaffected"
    publisher: The Record
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/grafana-breach-caused-by-missed-token-rotation-after-tanstack-attack/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/05/20/github-breached-teampcp/"
    publisher: Help Net Security
    role: corroborating
  - url: "https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/"
    publisher: "Unit 42, 2026-05-21"
    role: primary
  - url: "https://isc.sans.edu/diary/33016"
    publisher: "SANS Internet Storm Center, 2026-05-25"
    role: primary
  - url: "https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html"
    publisher: "The Hacker News, 2026-05-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: One of the packages (chalk-tempalte) is a direct clone of the Shai-Hulud worm open-sourced by TeamPCP with modified C2 infrastructure
    publisher: The Hacker News
  - quote: Checkmarx officially confirmed that a tampered plugin (version 2026.5.09) had been published to the Jenkins Marketplace ... This is the third TeamPCP compromise of Checkmarx in three months
    publisher: SANS Internet Storm Center
verification: multi-source
sourcing_note: null
confidence: high
references: []
weekly_section: weekly-long-running
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-05-13T05:00:11Z"
    run_id: 2026-05-13-c148b9a5
    type: update
    summary: >
      Mini Shai-Hulud worm re-detonates. TeamPCP poisoned 160+ npm package versions including
      @tanstack/ (42 packages, ~12M weekly downloads), @uipath/ (60+), @mistralai/* and
      @opensearch-project/opensearch via a pull_request_target → pnpm-cache poisoning →
      /proc/<pid>/mem OIDC-token theft chain that produced valid SLSA Build Level 3 provenance on the
      trojanised tarballs. UiPath is widely used in EU public-sector RPA; SAP HotNews #3747787
      acknowledges CAP-package impact (StepSecurity, 2026-05-11; TanStack post-mortem, 2026-05-12).
    fields:
      - priority
      - sectors
      - sources
      - tags
      - body
    merged_from: 2026-05-13/mini-shai-hulud-teampcp-worm-hits-tanstack-uipath-mistral-ai
  - at: "2026-05-15T05:00:09Z"
    run_id: 2026-05-15-58b94fbd
    type: update
    summary: >
      UPDATE (originally covered 2026-05-13): OpenAI disclosed on approximately 2026-05-13 that two
      employee devices were compromised through the TanStack npm supply-chain attack (Mini Shai-Hulud
      / TeamPCP, first covered in this brief series on 2026-05-12 and 2026-05-13) and that the
      compromise affected OpenAI's macOS …
    fields:
      - sources
      - tags
      - body
    merged_from: 2026-05-15/teampcp-mini-shai-hulud-openai-named-as-victim-code-signing
  - at: "2026-05-19T05:00:07Z"
    run_id: 2026-05-19-2505c918
    type: update
    summary: >
      TeamPCP/Shai-Hulud copycat wave begins — first imitator drops Phantom Bot DDoS and
      SSH/cloud-credential stealers in four typosquatted npm packages (OX Security, 2026-05-17).
      chalk-tempalte is a direct clone of the leaked Shai-Hulud worm source code that Datadog Security
      Labs analysed on 2026-05-13.
    fields:
      - evidence
      - regions
      - sources
      - tags
      - body
    merged_from: 2026-05-19/teampcp-shai-hulud-first-copycat-wave-phantom-bot-ssh-cloud
  - at: "2026-05-21T05:00:08Z"
    run_id: 2026-05-21-77cdc4cd
    type: update
    summary: >
      TeamPCP breaches GitHub itself — ~3,800 internal repositories exfiltrated via a poisoned VS Code
      extension installed on a GitHub employee device; in parallel, the Mini Shai-Hulud worm
      compromised the official Microsoft durabletask PyPI package and propagates across AWS via
      Systems Manager SendCommand and across Kubernetes via kubectl exec (Help Net Security,
      2026-05-20; Wiz, 2026-05-20).
    fields:
      - sources
      - tags
      - body
    merged_from: 2026-05-21/teampcp-mini-shai-hulud-campaign-github-itself-breached-3-80
  - at: "2026-05-22T05:00:06Z"
    run_id: 2026-05-22-5b90d5a1
    type: update
    summary: >
      UPDATE (originally covered 2026-05-19, updated 2026-05-21): Unit 42 (Palo Alto Networks) and
      StepSecurity published concurrent technical analyses on 2026-05-21 of the TeamPCP Mini
      Shai-Hulud npm supply-chain campaign, establishing the defining novelty of this wave: the first
      documented case of malicious npm …
    fields:
      - sources
      - tags
      - body
    merged_from: 2026-05-22/teampcp-mini-shai-hulud-unit-42-and-stepsecurity-confirm-sls
  - at: "2026-05-26T05:00:05Z"
    run_id: 2026-05-26-ae9d0d4b
    type: update
    summary: >
      UPDATE (originally covered 2026-05-21, consolidated weekly update): SANS ISC handler Kenneth
      Hartman documents three material escalations in the TeamPCP / Mini Shai-Hulud supply-chain
      campaign through 2026-05-24 (SANS Internet Storm Center, 2026-05-25).
    fields:
      - sources
      - tags
      - body
    merged_from: 2026-05-26/teampcp-mini-shai-hulud-framework-open-sourced-microsoft-pyp
migrated_from: briefs/weekly/2026-W19.md
---

Current state: SentinelLabs documented **PCPJack** on 2026-05-07 as a worm-class framework that evicts and deletes existing TeamPCP artefacts on compromise (giving the framework its name), then deploys six Python modules harvesting credentials from Docker, Kubernetes, Redis, MongoDB, RayML, and dozens of cloud / SaaS services (AWS, Azure, GCP, GitHub, Slack, HashiCorp Vault, 1Password). Propagation targets are pulled from Common Crawl Parquet files rather than ad-hoc scanning — far broader curated attack surface than typical opportunistic worms. Weaponises five public CVEs simultaneously ([CVE-2025-29927](https://nvd.nist.gov/vuln/detail/CVE-2025-29927) Next.js, [CVE-2025-55182](https://nvd.nist.gov/vuln/detail/CVE-2025-55182) React2Shell, [CVE-2026-1357](https://nvd.nist.gov/vuln/detail/CVE-2026-1357) WPVivid, [CVE-2025-9501](https://nvd.nist.gov/vuln/detail/CVE-2025-9501) W3 Total Cache, [CVE-2025-48703](https://nvd.nist.gov/vuln/detail/CVE-2025-48703) CWP). The TeamPCP → PCPJack succession overlay is the operational specific worth tracking: SentinelLabs explicitly states there is no evidence yet of a direct operator-level connection, while the eviction logic implies operators familiar with TeamPCP's target population. Defenders running self-hosted Next.js, React-server-actions stacks, WordPress with WPVivid Backup or W3 Total Cache, or CentOS Web Panel with internet-reachable FileManager should treat all five CVEs as actively weaponised ([SentinelLabs, 2026-05-07](https://www.sentinelone.com/labs/cloud-worm-evicts-teampcp-and-steals-credentials-at-scale/) · [The Hacker News, 2026-05-07](https://thehackernews.com/2026/05/pcpjack-credential-stealer-exploits-5.html) · [SecurityWeek, 2026-05-08](https://www.securityweek.com/pcpjack-worm-removes-teampcp-infections-steals-credentials/) · [daily 2026-05-10](/briefs/2026-05-10/)). The earlier TeamPCP "Mini Shai-Hulud" SAP CAP npm worm (covered 2026-05-06) used Claude Code SessionStart hooks and VSCode tasks for propagation — that thread is separate from PCPJack's CVE-chain propagation but the same operator population is tracked.

## Update — 2026-05-13T05:00:11Z

Between 19:20 and 19:26 UTC on 2026-05-11, TeamPCP's Mini Shai-Hulud self-propagating worm executed its largest campaign to date, compromising 160+ malicious versions across `@tanstack/*` (42 packages including `@tanstack/react-router` at ~12M weekly downloads), `@uipath/*` (60+ packages), `@mistralai/*`, `@opensearch-project/opensearch`, `@squawk/*`, `@draftlab/*` and `@tallyui/*`, plus two PyPI packages ([StepSecurity analysis, 2026-05-11](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem); [TanStack post-mortem, 2026-05-12](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem); [Wiz, 2026-05-12](https://www.wiz.io/blog/mini-shai-hulud-strikes-again-tanstack-more-npm-packages-compromised); [NCSC-CH Security Hub #12558, 2026-05-12](https://security-hub.ncsc.admin.ch/#/posts/12558)).

The novel attack chain (decomposed in § 5) is materially different from the 2026-05-10 SAP-CAP campaign: the operator (`voicproducoes`, GitHub account ID 269549300) submitted a poisoned PR to a target repository that triggered a `pull_request_target` workflow, used that privileged workflow to seed a malicious pnpm store into the GitHub Actions cache, then waited for legitimate maintainer merges to main — the release workflow restored the poisoned cache, attacker-controlled binaries extracted GitHub Actions OIDC tokens from `/proc/<pid>/mem`, and the worm used npm's token-exchange endpoint to publish trojanised package versions **with valid SLSA Build Level 3 provenance attestations**. The provenance bypass is the most significant evolution — SLSA L3 was the supply-chain assurance many EU public-sector procurement frameworks were starting to rely on, and this campaign demonstrates it is forgeable without abusing the package's own publish step.

Operational delta for defenders: SAP Note #3747787 (HotNews) acknowledges CAP-package impact and ships a clean version list. UiPath impact is the highest-priority public-sector signal — UiPath RPA is widely deployed in Swiss federal e-government automation and EU agency back-offices; review `package-lock.json` / `pnpm-lock.yaml` in every UiPath-using pipeline against the StepSecurity / Wiz package-version manifest. **Before revoking any GitHub PAT or npm token, sanitise the developer machine first** — token revocation triggers the worm's `gh-token-monitor` dead-man's switch that executes `rm -rf ~/` on the affected workstation. Mapped to `T1195.002 Supply Chain Compromise: Compromise Software Supply Chain`, `T1552.001 Unsecured Credentials: Credentials in Files`, `T1078.004 Cloud Accounts`.

## Update — 2026-05-15T05:00:09Z

OpenAI disclosed on approximately 2026-05-13 that two employee devices were compromised through the TanStack npm supply-chain attack (Mini Shai-Hulud / TeamPCP, first covered in this brief series on 2026-05-12 and 2026-05-13) and that the compromise affected OpenAI's macOS code-signing certificates ([TechCrunch, 2026-05-14](https://techcrunch.com/2026/05/14/openai-says-hackers-stole-some-data-after-latest-code-security-issue/) · [The Record, 2026-05-14](https://therecord.media/openai-asks-macos-users-to-update-tanstack-npm)).

The attackers exfiltrated "limited credential material" from internal source code repositories accessible to the two affected employees; OpenAI states no customer data, production systems, or core intellectual property were accessed. Critically, the certificate used to sign OpenAI's macOS desktop applications (ChatGPT for macOS and related apps) was among the compromised material, triggering an emergency certificate rotation. OpenAI is requiring all macOS app users to update to the latest version before **June 12, 2026**, after which older builds will lose functionality and macOS Gatekeeper notarization will block apps signed with the compromised certificate. Enterprise MDM administrators with OpenAI macOS apps in their managed fleet should push a forced update immediately. Threat attribution is unofficially assessed as TeamPCP (the same actor behind the broader TanStack worm), consistent with prior reporting on the actor's OIDC token theft and credential exfiltration goals.

## Update — 2026-05-19T05:00:07Z

Three concurrent developments show the TeamPCP / Shai-Hulud campaign has entered an open-source-imitator phase following Datadog Security Labs' 2026-05-13 analysis of the leaked Shai-Hulud worm source code. First, OX Security disclosed on 2026-05-17 four malicious npm packages published by `deadcode09284814` — `chalk-tempalte`, `@deadcode09284814/axios-util`, `axois-utils`, and `color-style-utils` — combined weekly downloads ~3,000 ([OX Security, 2026-05-17](https://www.ox.security/blog/new-actors-deploy-shai-hulud-clones-teampcp-copycats-are-here/); [The Hacker News, 2026-05-18](https://thehackernews.com/2026/05/four-malicious-npm-packages-deliver.html)). `chalk-tempalte` is a near-unmodified clone of the leaked Shai-Hulud worm with a modified C2 server and a new attacker-controlled key embedded in the code — the two primary sources disagree on whether this is a public or private key (; `axois-utils` bundles "Phantom Bot," a Golang HTTP/TCP/UDP/Reset-flood DDoS tool with Windows Startup folder and Linux scheduled-task persistence that survives package removal; the other two harvest SSH keys, cloud-provider credentials (AWS/GCP/Azure), and cryptocurrency wallet data.

Second, SANS ISC synthesised a 2026-05-18 campaign update confirming that Checkmarx officially acknowledged on 2026-05-11 that its Jenkins AST Scanner plugin had been trojanised — version `2026.5.09`, compromise window 2026-05-09 01:25 UTC to 2026-05-10 08:47 UTC — making this TeamPCP's third confirmed Checkmarx intrusion in three months ([SANS Internet Storm Center, 2026-05-18](https://isc.sans.edu/diary/rss/32994); [Checkmarx, 2026-05-12](https://checkmarx.com/blog/ongoing-security-updates/)). Hundreds of Jenkins controllers installed the malicious plugin before removal; remediated builds `2.0.13-848` and `2.0.13-847` are safe. CxSAST on-premise was unaffected; the cloud-integrated `checkmarx/ast-github-action`, `checkmarx/kics-github-action`, and VS Code extensions were all trojaned.

Third, SentinelLabs disclosed on 2026-05-07 — also folded into the SANS ISC summary — "PCPJack," a rival cloud worm that scans for exposed Docker, Kubernetes, Redis, MongoDB and RayML services and chains five CVEs (CVE-2025-29927 Next.js middleware auth bypass; CVE-2025-55182 Next.js Server Actions deserialization; CVE-2026-1357 WPVivid arbitrary file upload; CVE-2025-9501 W3 Total Cache RCE; CVE-2025-48703 CentOS Web Panel command injection) for initial access, then explicitly kills TeamPCP processes and removes TeamPCP artefacts before harvesting credentials — assessed by SentinelLabs with moderate confidence as possibly a former TeamPCP affiliate. Defender takeaway for the Swiss/EU public-sector SOC: developer endpoints and CI/CD runners with installed Checkmarx plugin should be audited for plugin versions outside the known-safe SHA range during the 2026-05-09 → 2026-05-10 window; `npm audit` and SBOM scans should flag the `deadcode09284814` author/scope; egress from CI runners to `*.lhr.life` hostnames is a high-fidelity hunt pivot for the npm worm wave; Docker/Kubernetes/Redis/MongoDB endpoints exposed to the internet should be inventoried and removed from public exposure (PCPJack's scan list). MITRE T1195.002 (Supply Chain Compromise), T1552.001 (Credentials in Files), T1041 (Exfiltration over C2 Channel).

## Update — 2026-05-21T05:00:08Z

Three new TeamPCP / Mini Shai-Hulud developments landed in this window — GitHub itself, the official Microsoft `durabletask` PyPI package, and the Grafana Labs root-cause disclosure.

**GitHub.** GitHub confirmed on 2026-05-20 that TeamPCP (also tracked as UNC6780) accessed approximately 3,800 internal GitHub repositories after a single GitHub employee installed a poisoned Visual Studio Code extension on their device ([The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/github-investigating-teampcp-claimed.html); [The Record, 2026-05-20](https://therecord.media/github-confirms-teampcp-hack-customers-unaffected); [Infosecurity Magazine, 2026-05-20](https://www.infosecurity-magazine.com/news/github-confirms-breach-vs-code/); [Help Net Security, 2026-05-20](https://www.helpnetsecurity.com/2026/05/20/github-breached-teampcp/)). GitHub detected and contained the breach on 2026-05-19, isolated the affected endpoint and rotated high-impact secrets; the company states there is no evidence customer data stored outside the internal repositories was accessed. **GitHub has not publicly named the malicious VS Code extension or its publisher at this writing.** TeamPCP listed the stolen repositories — including GitHub Actions internals, agentic-workflow code, Copilot internal projects, CodeQL tools, Codespaces, Dependabot, and a Rails controller managing organisations and PRs — for sale at $50,000, with LAPSUS$ announcing a joint sale and a $95,000 asking price.

**durabletask (PyPI).** Wiz Security reported on 2026-05-20 that the TeamPCP / Mini Shai-Hulud worm compromised the official Microsoft `durabletask` PyPI package via versions 1.4.1, 1.4.2 and 1.4.3 ([Wiz, 2026-05-20](https://www.wiz.io/blog/durabletask-teampcp-supply-chain-attack)). The payload is a dropper that fetches `rope.pyz` from `check.git-service[.]com`; per Wiz the second stage is a full credential stealer targeting AWS, Azure, GCP, Kubernetes and Vault credentials, 1Password and Bitwarden vaults, filesystem credentials and shell history. Propagation per Wiz: on Kubernetes hosts the worm uses `kubectl exec`; on AWS EC2 instances it propagates via AWS Systems Manager `SendCommand` against up to 5 targets per host (`T1078.004` Cloud Accounts, `T1570` Lateral Tool Transfer).

**Grafana Labs.** Grafana Labs published the post-mortem of its own TeamPCP breach on 2026-05-19, confirming the root cause was a single GitHub Actions workflow token that slipped through the rotation process after the TanStack npm supply-chain attack ([Grafana Labs, 2026-05-19](https://grafana.com/blog/grafana-labs-security-update-latest-on-tanstack-npm-supply-chain-ransomware-incident/); [BleepingComputer, 2026-05-20](https://www.bleepingcomputer.com/news/security/grafana-breach-caused-by-missed-token-rotation-after-tanstack-attack/)). Per Grafana's own post-mortem the TanStack compromise was detected on 2026-05-11 (note: BleepingComputer cites 2026-05-01 for the malicious-package consumption event — surfaced as a contradiction in § 7); Grafana rotated the bulk of its GitHub workflow tokens, but the residual unrotated token gave TeamPCP access to clone private source-code repositories (exact count not disclosed in Grafana's post-mortem). Grafana refused the extortion demand on 2026-05-16. The exfiltration scope is confirmed limited to Grafana Labs GitHub repositories (public source code, private source code and internal repos); customer production data was not affected.

**Defender takeaway:** audit VS Code extension marketplace policies and consider a managed extensions allowlist via Group Policy / MDM (the VS Code marketplace does not enforce mandatory code-signing). Hunt — Sysmon EID 1 for `code --install-extension` invocations on developer endpoints; process trees where `Code.exe` or `code-server` spawn credential-access tools (`git-credential-manager`, `aws configure`, keychain access). Audit GitHub Actions OIDC token rotation completeness after any supply-chain incident; verify GitHub secret-scanning + push-protection are enabled on every org. CI/CD pipeline logs should be searched for `durabletask` imports in the 1.4.1–1.4.3 version range; treat any host that imported a malicious version as fully compromised. Review AWS SSM `SendCommand` audit logs for invocations that do not correspond to authorised maintenance windows.

## Update — 2026-05-22T05:00:06Z

Unit 42 (Palo Alto Networks) and StepSecurity published concurrent technical analyses on 2026-05-21 of the TeamPCP Mini Shai-Hulud npm supply-chain campaign, establishing the defining novelty of this wave: the first documented case of malicious npm packages carrying valid SLSA Build Level 3 provenance attestations ([Unit 42, 2026-05-21](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/)). Attackers compromised TanStack's legitimate GitHub Actions CI/CD pipeline's trusted OIDC identity mid-workflow — without stealing developer credentials — making the SLSA attestation genuine while the package payload was malicious. This invalidates "package carries valid provenance attestation" as a sufficient supply-chain integrity gate.

The execution chain runs `tanstack_runner.js` under the Bun JavaScript runtime, enumerating stored credentials including `gh auth token` capture (`T1552.001 Unsecured Credentials: Credentials In Files`); stolen npm tokens and GitHub PATs are used to backdoor every package the victim account can publish (`T1650 Acquire Access`), making the worm self-propagating across the npm ecosystem. By end of the 2026-05-11 wave, 373 malicious package versions across 169 npm packages and PyPI mirrors were active ([Unit 42, 2026-05-21](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/)).

Defender actions from this technical update: (a) SLSA attestation verification is now insufficient as a sole gate — add runtime behavioural scanning of npm install scripts alongside provenance checks; (b) Pin GitHub Actions to commit SHAs, not mutable tags, to prevent mid-workflow OIDC identity hijack; (c) If pipelines ran `npm publish` during 2026-05-11 to 2026-05-12, rotate npm tokens and GitHub PATs and audit owned packages for unauthorised versions; (d) In environments where Bun is not an approved runtime, flag any `bun` or `bun.js` process execution from a CI runner context (Sysmon EID 1 process-name filter).

## Update — 2026-05-26T05:00:05Z

SANS ISC handler Kenneth Hartman documents three material escalations in the TeamPCP / Mini Shai-Hulud supply-chain campaign through 2026-05-24 ([SANS Internet Storm Center, 2026-05-25](https://isc.sans.edu/diary/33016)). First, the complete TeamPCP framework was published to a public GitHub repository on/around 2026-05-22 — Datadog Security Labs' static analysis (reported by ISC) describes a modular TypeScript/Bun toolkit for credential harvesting, supply-chain poisoning and encrypted exfiltration whose README carries the strings "Love - TeamPCP" and "Change keys and C2 as needed" — and operational copycat forks appeared within hours, commoditising the kit and injecting attribution noise.

Second, an `@antv` npm wave pushed 639 malicious versions across 323 packages, including high-traffic libraries such as `echarts-for-react` (~1.1M weekly downloads) and `size-sensor` (~4.2M weekly downloads); 42 of the packages displayed **forged Sigstore verification badges in the npm UI** ([The Hacker News, 2026-05-19](https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html)). Read against the campaign's earlier abuse of genuine SLSA Build Level 3 attestations produced by hijacked pipelines, package provenance is now under attack from both directions at once — real attestations from compromised CI and fake badges rendered by the registry UI. Third, three versions of `durabletask` (1.4.1–1.4.3) on PyPI — Microsoft's official Azure Durable Functions SDK — were trojanised, and ISC reports the second-stage payload includes a **Linux disk wiper** ([`T1485`](https://attack.mitre.org/techniques/T1485/)), expanding the campaign's capability from credential theft to data destruction.

Defender takeaway: treat any `echarts-for-react` / `size-sensor` build pulled in the affected window as compromised; **stop treating an npm Sigstore badge or a displayed SLSA attestation as an install-time safety signal** — verify provenance out-of-band against a known-good pipeline. `durabletask` consumers should audit build-runner logs for unexpected outbound connections and destructive disk operations (Sysmon EID 11 for anomalous file-deletion patterns, EID 3 for unexpected `node`/`python` egress from CI workers). Pin exact versions and verify lockfile hashes. The open-sourcing means PBKDF2-salt and dead-drop-string lineage will now also fire on unrelated copycats — behavioural detection on the install-time execution chain is more durable than any static artefact.
