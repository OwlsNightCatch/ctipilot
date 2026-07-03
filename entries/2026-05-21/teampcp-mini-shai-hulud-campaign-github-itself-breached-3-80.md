---
schema: 1
kind: incident
horizon: operational
title: "TeamPCP / Mini Shai-Hulud campaign — GitHub itself breached (~3,800 internal repos via poisoned VS Code extension), Microsoft durabletask PyPI worm propagates via AWS SSM and kubectl exec, Grafana confirms missed-token-rotation root cause"
headline: "TeamPCP / Mini Shai-Hulud campaign — GitHub itself breached (~3,800 internal repos via poisoned VS Code extension), Microsoft durabletask PyPI worm propagates"
summary: "TeamPCP breaches GitHub itself — ~3,800 internal repositories exfiltrated via a poisoned VS Code extension installed on a GitHub employee device; in parallel, the Mini Shai-Hulud worm compromised the official Microsoft durabletask PyPI package and propagates across AWS via Systems Manager SendCommand and across Kubernetes via kubectl exec (Help Net Security, 2026-05-20; Wiz, 2026-05-20)."
discovered_at: "2026-05-21T05:00:08Z"
event_date: 2026-05-20
run_id: 2026-05-21-77cdc4cd
priority: high
immediate_action: null
tags:
  - supply-chain
  - organized-crime
  - cloud
  - identity
  - data-breach
regions:
  - global
sectors:
  - technology
  - public-sector
entities:
  - "campaign:mini-shai-hulud"
  - "actor:teampcp"
cves: []
sources:
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
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-05-13/mini-shai-hulud-teampcp-worm-hits-tanstack-uipath-mistral-ai
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-21.md
---

**UPDATE (originally covered 2026-05-13 deep dive; multiple subsequent updates):** three new TeamPCP / Mini Shai-Hulud developments landed in this window — GitHub itself, the official Microsoft `durabletask` PyPI package, and the Grafana Labs root-cause disclosure.

**GitHub.** GitHub confirmed on 2026-05-20 that TeamPCP (also tracked as UNC6780) accessed approximately 3,800 internal GitHub repositories after a single GitHub employee installed a poisoned Visual Studio Code extension on their device ([The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/github-investigating-teampcp-claimed.html); [The Record, 2026-05-20](https://therecord.media/github-confirms-teampcp-hack-customers-unaffected); [Infosecurity Magazine, 2026-05-20](https://www.infosecurity-magazine.com/news/github-confirms-breach-vs-code/); [Help Net Security, 2026-05-20](https://www.helpnetsecurity.com/2026/05/20/github-breached-teampcp/)). GitHub detected and contained the breach on 2026-05-19, isolated the affected endpoint and rotated high-impact secrets; the company states there is no evidence customer data stored outside the internal repositories was accessed. **GitHub has not publicly named the malicious VS Code extension or its publisher at this writing.** TeamPCP listed the stolen repositories — including GitHub Actions internals, agentic-workflow code, Copilot internal projects, CodeQL tools, Codespaces, Dependabot, and a Rails controller managing organisations and PRs — for sale at $50,000, with LAPSUS$ announcing a joint sale and a $95,000 asking price.

**durabletask (PyPI).** Wiz Security reported on 2026-05-20 that the TeamPCP / Mini Shai-Hulud worm compromised the official Microsoft `durabletask` PyPI package via versions 1.4.1, 1.4.2 and 1.4.3 ([Wiz, 2026-05-20](https://www.wiz.io/blog/durabletask-teampcp-supply-chain-attack)). The payload is a dropper that fetches `rope.pyz` from `check.git-service[.]com`; per Wiz the second stage is a full credential stealer targeting AWS, Azure, GCP, Kubernetes and Vault credentials, 1Password and Bitwarden vaults, filesystem credentials and shell history. Propagation per Wiz: on Kubernetes hosts the worm uses `kubectl exec`; on AWS EC2 instances it propagates via AWS Systems Manager `SendCommand` against up to 5 targets per host (`T1078.004` Cloud Accounts, `T1570` Lateral Tool Transfer).

**Grafana Labs.** Grafana Labs published the post-mortem of its own TeamPCP breach on 2026-05-19, confirming the root cause was a single GitHub Actions workflow token that slipped through the rotation process after the TanStack npm supply-chain attack ([Grafana Labs, 2026-05-19](https://grafana.com/blog/grafana-labs-security-update-latest-on-tanstack-npm-supply-chain-ransomware-incident/); [BleepingComputer, 2026-05-20](https://www.bleepingcomputer.com/news/security/grafana-breach-caused-by-missed-token-rotation-after-tanstack-attack/)). Per Grafana's own post-mortem the TanStack compromise was detected on 2026-05-11 (note: BleepingComputer cites 2026-05-01 for the malicious-package consumption event — surfaced as a contradiction in § 7); Grafana rotated the bulk of its GitHub workflow tokens, but the residual unrotated token gave TeamPCP access to clone private source-code repositories (exact count not disclosed in Grafana's post-mortem). Grafana refused the extortion demand on 2026-05-16. The exfiltration scope is confirmed limited to Grafana Labs GitHub repositories (public source code, private source code and internal repos); customer production data was not affected.

**Defender takeaway:** audit VS Code extension marketplace policies and consider a managed extensions allowlist via Group Policy / MDM (the VS Code marketplace does not enforce mandatory code-signing). Hunt — Sysmon EID 1 for `code --install-extension` invocations on developer endpoints; process trees where `Code.exe` or `code-server` spawn credential-access tools (`git-credential-manager`, `aws configure`, keychain access). Audit GitHub Actions OIDC token rotation completeness after any supply-chain incident; verify GitHub secret-scanning + push-protection are enabled on every org. CI/CD pipeline logs should be searched for `durabletask` imports in the 1.4.1–1.4.3 version range; treat any host that imported a malicious version as fully compromised. Review AWS SSM `SendCommand` audit logs for invocations that do not correspond to authorised maintenance windows.
