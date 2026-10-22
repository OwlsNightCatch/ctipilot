---
schema: 1
kind: incident
title: "LiteLLM 1.107.0: the PyPI wheels and the official Docker images carried a credential stealer and a dormant remote-code loader that Python starts at every launch, published through the maintainers' own release workflow with stolen developer tokens"
headline: "LiteLLM 1.107.0 on PyPI and in the official images stole cloud and AI credentials; removing the package does not stop it"
summary: >
  On 2026-10-21 LiteLLM 1.107.0, the open-source LLM gateway, shipped with malicious Python startup files in all seven PyPI wheels
  (live 11:39 to 13:23 UTC) and in the official GHCR and Docker Hub images behind the v1.107.0, latest, main-latest and main-stable
  tags (11:46 to 14:20 UTC); they run a credential stealer at every Python start and start a background loader that could execute code
  fetched from an attacker-chosen host, though Socket saw its pointer empty at 13:01 UTC. The maintainers say the attacker used three engineers' stolen GitHub CLI OAuth tokens, apparently read
  from the logs of an internet-exposed internal LiteLLM deployment, to force-push a release-workflow change past branch protection and
  build from a look-alike repository. Wiz saw stolen AWS instance-role credentials tested about 4.5 hours after exfiltration; PyPI and
  the registries removed the release the same day and the maintainers say to pin 1.106.2 or an explicit earlier version.
discovered_at: "2026-10-22T03:44:00Z"
updated_at: null
event_date: "2026-10-21"
run_id: 2026-10-22T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, infostealer, cloud]
regions: [global]
sectors: [technology]
entities: ["product:litellm", "product:berriai-litellm"]
techniques: [T1195.001, T1195.002, T1546.018, T1552.001, T1552.004, T1552.005, T1555.003, T1102.001, T1105, T1027.013, T1140, T1528, T1078.004, T1087.004]
affected_products: ["LiteLLM"]
cves: []
sources:
  - url: "https://socket.dev/blog/litellm-compromise"
    publisher: "Socket Research Team"
    date: "2026-10-21"
    role: primary
  - url: "https://docs.litellm.ai/blog/security-incident-oct-21-2026"
    publisher: "LiteLLM maintainers (security incident post)"
    date: "2026-10-21"
    role: primary
  - url: "https://github.com/BerriAI/litellm/issues/47826"
    publisher: "GitHub issue BerriAI/litellm #47826 (Upwind report, with maintainer replies)"
    date: "2026-10-21"
    role: primary
  - url: "https://www.wiz.io/blog/litellm-compromised-steals-credentials"
    publisher: "Wiz Research"
    date: "2026-10-21"
    role: corroborating
  - url: "https://www.aikido.dev/blog/litellm-compromised-infostealer-rat"
    publisher: "Aikido Security"
    date: "2026-10-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "contains malicious Python startup files that collect cloud credentials, private keys, browser data, and authentication files for AI development tools"
    publisher: "Socket Research Team"
    source_url: "https://socket.dev/blog/litellm-compromise"
  - quote: "starting Python or pip in an affected environment to inspect or repair the installation can execute the payload again"
    publisher: "Socket Research Team"
    source_url: "https://socket.dev/blog/litellm-compromise"
  - quote: "removing the LiteLLM package directory alone does not remove those files or stop an existing process"
    publisher: "Socket Research Team"
    source_url: "https://socket.dev/blog/litellm-compromise"
  - quote: "We have identified that the malicious actions were taken through three engineers' GitHub accounts, appearing to be by way of stolen GitHub CLI OAuth tokens."
    publisher: "GitHub issue BerriAI/litellm #47826 (Upwind report, with maintainer replies)"
    source_url: "https://github.com/BerriAI/litellm/issues/47826"
  - quote: "We believe the attacker gained access to this deployment, obtained the GitHub CLI OAuth tokens from its logs, and subsequently used those credentials to compromise our release workflow."
    publisher: "LiteLLM maintainers (security incident post)"
    source_url: "https://docs.litellm.ai/blog/security-incident-oct-21-2026"
  - quote: "Each credential was checked with sts:GetCallerIdentity, followed by bedrock:ListFoundationModels and a ListModels call, consistent with LLMjacking."
    publisher: "Wiz Research"
    source_url: "https://www.wiz.io/blog/litellm-compromised-steals-credentials"
  - quote: "PyPI has now quarantined version 1.107.0."
    publisher: "Aikido Security"
    source_url: "https://www.aikido.dev/blog/litellm-compromised-infostealer-rat"
verification: multi-source
sourcing_note: >
  Socket, Upwind (in the project's own issue), Wiz and Aikido analysed the release independently and agree on the mechanism; the
  maintainers' incident post and issue replies give the attack chain, the exposure windows and the removals. The chain is the
  maintainers' own account, updated at 20:30 UTC on 2026-10-21 and still marked as under investigation, and how the attacker reached
  the internal deployment is not confirmed.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Find every host, build agent and container that installed litellm 1.107.0 from PyPI between 11:39 and 13:23 UTC on 2026-10-21, or pulled the v1.107.0, latest, main-latest or main-stable tag of the official GHCR or Docker Hub LiteLLM images between 11:46 and 14:20 UTC; treat each as compromised, inspect it with tooling that does not start Python in the affected environment, rebuild it from a reviewed artifact pinned to 1.106.2 or an image digest, and rotate every cloud, Kubernetes, registry, SSH, database and AI-provider credential it could read, including the provider keys stored in a LiteLLM proxy database."
updates: []
migrated_from: null
---

Socket reports that LiteLLM 1.107.0, an open-source LLM gateway, carries malicious Python startup files in all seven wheels, and that Upwind found the same payload in the published images ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)). A startup hook and a second startup module in the Python library directory run at every Python start without the application importing LiteLLM: the first collects cloud, Kubernetes, CI, registry and database credentials, SSH, GPG and TLS private keys, browser stores, AI-tool credential files, environment variables and, where configured, the credentials saved in a LiteLLM proxy database; the second forks a detached loader that polls a file in a GitHub repository for a domain and would execute Python downloaded from it with no signature or hash check, though at 13:01 UTC the pointer returned an empty body, which stops the loader before its download stage ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)).

The payload is not in the git tag: a packaging setting in an untagged commit pulls it into the wheel, and the container build provenance records a source repository named Berri-AI/litellm, one hyphen away from BerriAI/litellm ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)). The maintainers say stolen GitHub CLI OAuth tokens of three engineers drove the release: one account started the run, another approved it, a third deleted the workflow records, and an organisation owner's token disabled branch protection so that a change pointing the releaser at the look-alike repository could be force-pushed ([GitHub issue #47826, 2026-10-21](https://github.com/BerriAI/litellm/issues/47826); [LiteLLM, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)). They believe the tokens were read from the logs of an internet-exposed internal LiteLLM deployment, note that Claude Code can embed a user's GitHub CLI OAuth token in a response body that deployments log, and suspect, unconfirmed, a recently patched vulnerability; an embargoed fix for a vulnerability due for disclosure on 2026-10-27 goes to enterprise customers through a private registry ([LiteLLM, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)). PyPI quarantined 1.107.0 and the images were pulled the same day ([Aikido, 2026-10-21](https://www.aikido.dev/blog/litellm-compromised-infostealer-rat); [LiteLLM, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)).

**Exposure:** an environment that installed litellm 1.107.0 from PyPI between 11:39 and 13:23 UTC on 2026-10-21, or pulled the v1.107.0, latest, main-latest or main-stable tag of the official images from GHCR (until about 13:51 UTC) or Docker Hub (until 14:20 UTC); lockfiles, caches, build logs and running image digests show which ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise); [LiteLLM, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)).

**Detection:** in the cloud audit logs of every account the host could reach, a caller-identity check followed by a Bedrock model listing and IAM enumeration, made with an instance-role credential harvested from CI runners or Kubernetes nodes from an address outside your estate, which Wiz saw from 16:20 UTC on 2026-10-21 ([Wiz, 2026-10-21](https://www.wiz.io/blog/litellm-compromised-steals-credentials)); on hosts, startup hooks and sitecustomize modules in a Python library directory that your tooling did not install, a detached Python process holding a lock file, and an encrypted archive posted to a path labelled as a health check ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)). Starting Python or pip in an affected environment can run the payload again, and removing the package directory does not remove the startup files or stop a running loader ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)).

**Defender takeaway:** rotate every credential the host could reach ([LiteLLM, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)), because removing the package does not remove the startup files ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)) and stolen cloud credentials were in use within hours ([Wiz, 2026-10-21](https://www.wiz.io/blog/litellm-compromised-steals-credentials)); rebuild from a reviewed release and pin container digests ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)), and move to 1.106.2 or an explicit earlier version as the maintainers advise ([LiteLLM, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)).
