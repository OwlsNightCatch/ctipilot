---
schema: 1
kind: threat
horizon: operational
title: "\"Miasma\" worm backdoors 32 Red Hat Cloud Services npm packages via OIDC trusted-publishing abuse"
headline: "\"Miasma\" worm backdoors 32 Red Hat Cloud Services npm packages via OIDC trusted-publishing abuse"
summary: >
  "Miasma" supply-chain worm compromised 32 @redhat-cloud-services npm packages via a hijacked
  maintainer GitHub account and OIDC trusted-publishing abuse, adding new GCP and Azure
  cloud-identity collectors (Wiz, 2026-06-01).
discovered_at: "2026-06-02T05:00:02Z"
updated_at: "2026-06-10T05:00:17Z"
event_date: 2026-06-01
run_id: 2026-06-02-8af85d01
priority: high
immediate_action: null
tags:
  - supply-chain
  - cloud
  - identity
  - infostealer
  - ai-abuse
regions:
  - global
sectors:
  - technology
  - public-sector
  - education
entities:
  - "campaign:mini-shai-hulud"
  - "actor:teampcp"
  - "campaign:miasma-redhat-npm-supply-chain"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages"
    publisher: Wiz Research
    role: primary
  - url: "https://www.aikido.dev/blog/red-hat-npm-packages-compromised-credential-stealing-worm"
    publisher: Aikido Security
    role: corroborating
  - url: "https://socket.dev/blog/mini-shai-hulud-campaign-hits-red-hat-cloud-services-npm-packages"
    publisher: Socket
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/red-hat-npm-packages-compromised-to-steal-developer-credentials/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://opensourcemalware.com/blog/miasma-reaches-azure"
    publisher: OpenSourceMalware — The Blight Reaches Microsoft
    role: primary
  - url: "https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html"
    publisher: "The Hacker News, 2026-06-06"
    role: corroborating
  - url: "https://thehackernews.com/2026/06/hades-pypi-attack-19-packages-poisoned.html"
    publisher: "The Hacker News, 2026-06-09"
    role: primary
  - url: "https://socket.dev/blog/shai-hulud-descends-to-hades-miasma-pypi-wave"
    publisher: "Socket, 2026-06-07"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-06-06T05:00:06Z"
    run_id: 2026-06-06-d01b95fe
    type: update
    summary: >
      UPDATE (originally covered 2026-06-02): The Miasma worm — the TeamPCP-spawned descendant of the
      Mini Shai-Hulud lineage first covered against the Red Hat @redhat-cloud-services npm namespace —
      recompromised the durabletask package and propagated into the Microsoft GitHub estate.
    fields:
      - sources
      - body
    merged_from: 2026-06-06/miasma-supply-chain-worm-reaches-73-microsoft-github-reposit
  - at: "2026-06-10T05:00:17Z"
    run_id: 2026-06-10-c84347b2
    type: update
    summary: >
      UPDATE (originally covered 2026-06-06): The Miasma/Mini-Shai-Hulud supply-chain lineage
      previously tracked across npm and GitHub has opened a PyPI front dubbed "Hades": Socket and
      others identified 37 malicious wheel artifacts across 19 packages abusing Python's .pth
      site-module startup mechanism to auto-execute …
    fields:
      - sectors
      - sources
      - tags
      - body
    merged_from: 2026-06-10/shai-hulud-miasma-supply-chain-worm-jumps-to-pypi-as-hades-3
migrated_from: briefs/2026-06-02.md
---

Threat actor cluster TeamPCP used a compromised Red Hat maintainer GitHub account to inject malicious CI/CD workflows into 32 packages in the `@redhat-cloud-services` npm namespace, poisoning 96 releases across high-traffic packages — Wiz puts the combined weekly downloads at roughly 80,000, while Aikido counts closer to 117,000 ([Wiz, 2026-06-01](https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages) · [Aikido Security, 2026-06-01](https://www.aikido.dev/blog/red-hat-npm-packages-compromised-credential-stealing-worm)). Rather than compromising developer machines directly, the attack abused GitHub Actions OIDC trusted publishing so the CI/CD pipeline itself republished backdoored packages carrying obfuscated `preinstall` hooks. The "Miasma" payload — a new variant in the Mini Shai-Hulud / Shai-Hulud lineage — sweeps for GitHub Actions secrets, npm tokens, AWS keys, SSH keys, HashiCorp Vault and Kubernetes credentials, and now adds dedicated collectors for **GCP service-account and Azure managed-identity tokens**, signalling a pivot from developer-host theft toward cloud-account takeover ([Socket, 2026-06-01](https://socket.dev/blog/mini-shai-hulud-campaign-hits-red-hat-cloud-services-npm-packages)). Wiz notes the new variant's cloud-identity focus explicitly.

**Why it matters to us:** Red Hat tooling has a broad EU public-sector DevOps footprint (OpenShift/OpenStack estates). Inventory installed `@redhat-cloud-services/*` versions across build agents and developer endpoints, alert on `preinstall` scripts spawning obfuscated `node -e` chains from `npm`/`npx` parent trees, and rotate any CI/CD cloud-identity tokens reachable from affected pipelines.

## Update — 2026-06-06T05:00:06Z

The Miasma worm — the TeamPCP-spawned descendant of the Mini Shai-Hulud lineage first covered against the Red Hat `@redhat-cloud-services` npm namespace — recompromised the `durabletask` package and propagated into the Microsoft GitHub estate. On 2026-06-05 GitHub disabled **73 repositories** across the Azure, Azure-Samples, Microsoft and MicrosoftDocs organisations in a 105-second automated terms-of-service sweep, taking the entire Azure Durable Task family (.NET, Go, Java, JS, MSSQL, Netherite, protobuf) offline ([OpenSourceMalware, 2026-06-05](https://opensourcemalware.com/blog/miasma-reaches-azure); [The Hacker News, 2026-06-06](https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html)).

The material delta from the 2026-06-02 coverage: the variant adds **Azure CLI auth-cache and managed-identity token collectors** (earlier Shai-Hulud strains targeted AWS and GitHub), and the recompromise traces to the same `durabletask` credential foothold from the May TeamPCP incident — i.e. credentials taken in May were never fully revoked. Azure Durable Task is a foundational dependency for Azure Functions / serverless workflows widely consumed in EU public-sector cloud deployments, so the downstream exposure is cloud infrastructure, not just developer machines.

Defender takeaway: audit `~/.azure/` credential stores on developer workstations and CI/CD runners that installed any affected `@azure/*` package; rotate Azure managed-identity tokens and Kubernetes service-account tokens on those systems; monitor GitHub audit logs for unexpected public-repo creation (the worm's secret-exfil-as-public-repo behaviour is what trips GitHub's automated sweep). Note the worm-vs-defender naming overlap is real here — "Miasma" is the attacker worm, not a tool.

## Update — 2026-06-10T05:00:17Z

The Miasma/Mini-Shai-Hulud supply-chain lineage previously tracked across npm and GitHub has opened a PyPI front dubbed "Hades": Socket and others identified 37 malicious wheel artifacts across 19 packages abusing Python's `.pth` site-module startup mechanism to auto-execute on interpreter start without an import ([The Hacker News, 2026-06-09](https://thehackernews.com/2026/06/hades-pypi-attack-19-packages-poisoned.html)). The payload downloads the Bun runtime from GitHub and runs triple-encrypted JavaScript that sweeps GitHub/CI tokens, npm/PyPI/cloud (AWS/GCP/Azure) keys, Kubernetes and Vault configs, SSH keys and AI-tool configs, and plants backdoor config in AI coding-assistant workspaces so future agent sessions execute attacker instructions ([Socket, 2026-06-07](https://socket.dev/blog/shai-hulud-descends-to-hades-miasma-pypi-wave)).

Affected packages spanned developer tooling and a bioinformatics cluster (relevant to university/research compute), all since removed. Hunt for `*-setup.pth` creation under `site-packages`, Bun binary downloads from `github.com/oven-sh/bun`, and the `$TMPDIR/.bun_ran` sentinel via Sysmon EID 1 with parent `python`/`pip` (T1547.013, T1059.007, T1555). Pin dependencies and install with `--ignore-scripts`; audit recently-installed PyPI packages on research endpoints.
