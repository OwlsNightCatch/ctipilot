---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "Three developer-credential findings this week each show an estate auditing the wrong thing — the wrong package, the wrong incident class, and repositories nobody counted as company assets at all"
headline: "W33's supply-chain work was about scoping errors: 95% of one 'breach' traced to a different vendor, and repo theft is a secrets incident"
summary: >
  Three independent findings inside 2026-W33 converge on scoping rather than technique. SOCRadar
  re-analysed the exposure dataset behind the widely reported 2,500-organisation LiteLLM supply-chain
  breach and found 2,085 of the 2,188 identified organisations show collection activity beginning before
  the poisoned LiteLLM packages reached PyPI — the collection tracks the earlier compromise of Aqua
  Security's Trivy scanner, which LiteLLM's own CI pulled unpinned, so an estate that checked for LiteLLM
  package versions audited the wrong artefact. Wiz's incident-response team published a playbook for a
  campaign that abused compromised GitHub Personal Access Tokens, in which the actor used 102 AWS IP
  addresses in one region over roughly six hours to clone up to thousands of repositories per victim
  organisation, and argues repository theft should be handled as a credentials incident rather than a
  source-code one; a companion post reports 56% of company-impacting secrets it found across one company
  set sat in employees' personal repositories, outside enterprise scanning entirely. CERT Intrinsec's
  forensic-artefact series shows where coding-agent CLIs write plaintext provider credentials on disk.
discovered_at: "2026-08-16T23:59:00Z"
event_date: "2026-08-13"
run_id: 2026-08-16T2315Z-weekly
priority: notable
immediate_action: null
tags: [supply-chain, cloud, identity, ai-abuse]
regions: [europe, global]
sectors: [public-sector, technology]
entities:
  - actor:teampcp
  - trend:coding-agent-ci-harness-trust-boundary-2026-08
  - report:intrinsec-ai-agents-digital-forensics-series
techniques: [T1195.002, T1552.001, T1552.005, T1213.003, T1550.001, T1078.004, T1567]
affected_products: ["GitHub Enterprise Cloud", "Aqua Security Trivy", "LiteLLM", "OpenCode", "OpenAI Codex CLI"]
cves: []
sources:
  - url: "https://www.wiz.io/blog/investigating-github-pat-compromise"
    publisher: "Wiz (Customer Incident Response Team)"
    date: "2026-08-13"
    role: primary
  - url: "https://www.wiz.io/blog/securing-personal-repositories"
    publisher: "Wiz"
    date: "2026-08-13"
    role: corroborating
  - url: "https://socradar.io/blog/litellm-supply-chain-attack/"
    publisher: "SOCRadar"
    date: "2026-08-13"
    role: primary
  - url: "https://www.securityweek.com/trivy-not-litellm-behind-the-2500-org-compromise/"
    publisher: "SecurityWeek"
    date: "2026-08-14"
    role: corroborating
  - url: "https://www.intrinsec.com/en/ai-agents-digital-forensics-openai-codex-artifacts/"
    publisher: "CERT Intrinsec"
    date: "2026-07-31"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Between 09:14 and 14:55 UTC, the actor used 102 AWS IP addresses located in the ca-central-1 region to clone up to thousands of repositories per organization."
    publisher: "Wiz (Customer Incident Response Team)"
  - quote: "Repository exfiltration should be treated as more than source code theft. Repositories frequently contain cloud credentials, SaaS tokens, internal documentation, private keys, and sensitive data that can significantly increase the impact of a compromise."
    publisher: "Wiz (Customer Incident Response Team)"
  - quote: "56% of company-impacting secrets lived in employees' personal repositories, where most security programs have no visibility."
    publisher: "Wiz"
verification: multi-source
sourcing_note: >
  The Wiz findings are that vendor's own incident-response work and are single-assessor; the companion
  personal-repositories figure appears in a post that is partly a product description, and is attributed to
  Wiz Research rather than presented as an independent measurement. The Trivy re-attribution is SOCRadar's
  re-analysis, independently reported by SecurityWeek. No cited source connects the GitHub token campaign to
  the Trivy compromise and this entry asserts no link between them; the pattern claimed is a shared scoping
  failure, not a shared operator.
confidence: medium
update_of: null
references:
  - 2026-08-15/trivy-not-litellm-behind-2500-org-credential-collection
  - 2026-08-10/coding-agent-forensic-artefacts-opencode-codex-credentials
  - 2026-08-10/coding-agent-ci-harness-trust-boundary-shared-checkout
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Supply-chain research usually asks how the attacker got in. Three findings this week ask a different question, and give the same unwelcome answer: the organisations that responded to these incidents looked in the wrong place, and their audits came back clean for that reason.

The clearest case is a correction to a story most estates have already closed. SOCRadar re-analysed the exposure dataset behind the widely reported compromise of around 2,500 organisations through LiteLLM and found that 2,085 of the 2,188 identified organisations — 95% — show collection activity beginning before the poisoned LiteLLM packages reached PyPI on 24 March. The collection instead tracks the compromise of Aqua Security's Trivy scanner, whose poisoned release LiteLLM's own continuous-integration pipeline pulled unpinned ([SOCRadar, 2026-08-13](https://socradar.io/blog/litellm-supply-chain-attack/)), a re-attribution SecurityWeek reported independently ([SecurityWeek, 2026-08-14](https://www.securityweek.com/trivy-not-litellm-behind-the-2500-org-compromise/)). The operational consequence is specific and awkward: an estate that asked "did we install the affected LiteLLM versions on 24 March" asked about the wrong package on the wrong date, got a negative answer, and closed a genuine exposure. The artefact that actually needed auditing is a security scanner — a tool most CI pipelines pull by mutable tag precisely because it is a security tool and expected to be current.

Wiz's Customer Incident Response Team published the second, a technical playbook for a campaign run against multiple customer organisations that abused compromised GitHub Personal Access Tokens for mass repository exfiltration. The attack shape is worth knowing because it is loud in exactly one place: reconnaissance through GitHub API queries to enumerate everything the token could reach, a small number of validation clones, then bulk theft — "Between 09:14 and 14:55 UTC, the actor used 102 AWS IP addresses located in the ca-central-1 region to clone up to thousands of repositories per organization" ([Wiz, 2026-08-13](https://www.wiz.io/blog/investigating-github-pat-compromise)). Wiz's framing is the part that changes response practice: "Repository exfiltration should be treated as more than source code theft. Repositories frequently contain cloud credentials, SaaS tokens, internal documentation, private keys, and sensitive data that can significantly increase the impact of a compromise." An organisation that scopes this as intellectual-property loss writes a legal assessment; an organisation that scopes it as a secrets incident rotates cloud credentials and hunts for their use, which is the difference between the incident ending and continuing. A companion Wiz post reports that across the Forbes AI 50 the firm found "56% of company-impacting secrets lived in employees' personal repositories, where most security programs have no visibility" ([Wiz, 2026-08-13](https://www.wiz.io/blog/securing-personal-repositories)) — a third scoping error, this time in what counts as a company asset at all.

The week's third finding supplies the substrate the other two run on. CERT Intrinsec's forensic-artefact series for autonomous coding-agent command-line tools documents that these tools write their state to predictable per-user paths — OpenCode keeping a database of sessions, messages and workspaces alongside a file holding authentication information including API keys, and OpenAI Codex keeping authentication material in `auth.json` with the operator's prompt history in `history.jsonl` ([CERT Intrinsec, 2026-07-31](https://www.intrinsec.com/en/ai-agents-digital-forensics-openai-codex-artifacts/)). Read as an investigator's map that is useful; read as an attacker's inventory it says that any foothold on a developer or build host now reaches cleartext provider credentials at a known location, without touching a keychain or a secrets manager.

**Defender takeaway:** the common thread is that the boundary of a credentials incident is wider than the artefact that carried it, and each of these three widens it in a different direction — upstream to a dependency's own dependency, sideways from code to the secrets inside code, and outward from corporate repositories to personal ones. Two concrete review items follow from that. First, any supply-chain audit closed on a package-and-date question should be re-opened against the pipeline's own tooling: build-time scanners, actions and images pulled by mutable tag are dependencies with the same blast radius as runtime packages and are rarely inventoried as such. Second, an organisation's response plan for repository theft should already name which credential classes get rotated, because the useful window for that decision is hours and the Wiz timeline shows the theft itself completing in about six.

**Triage:** the GitHub-side observable is a shape rather than an indicator, and it is one legitimate tooling does not produce. Enterprise audit-log events showing a single token or principal issuing a burst of repository-clone or archive-download calls, spanning many repositories including ones that principal has never touched, from source addresses distributed across a narrow cloud-provider range within a short window, is anomalous by construction: continuous-integration systems clone repeatedly but from a small, stable set of known egress addresses and against the repositories they build, and a developer clones interactively at human rates. The preceding phase is quieter and worth pairing with it — a rise in API enumeration calls from a token that normally only clones. On developer and build hosts, the corresponding host-side signal is any process other than the agent itself reading those documented credential paths.
