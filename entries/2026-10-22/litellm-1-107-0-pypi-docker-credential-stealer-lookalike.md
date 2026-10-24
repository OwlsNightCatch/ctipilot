---
schema: 1
kind: incident
title: "LiteLLM 1.107.0: the PyPI wheels and the official Docker images carried a credential stealer and a dormant remote-code loader that Python starts at every launch, published through the maintainers' own release workflow with stolen developer tokens"
headline: "LiteLLM 1.107.0 on PyPI and in the official images stole cloud and AI credentials; removing the package does not stop it"
summary: >
  On 2026-10-21 LiteLLM 1.107.0, the open-source LLM gateway, shipped with malicious Python startup files in all seven PyPI wheels
  (live 11:39 to 13:23 UTC) and in the official GHCR and Docker Hub images behind the v1.107.0, latest, main-latest and main-stable
  tags (11:46 to 14:20 UTC); they run a credential stealer at every Python start and start a background loader that could execute code
  fetched from an attacker-chosen host, though Socket saw its pointer empty at 13:01 UTC. The maintainers' root-cause post of 2026-10-23 says a master
  key committed to a public repository on 2026-05-27 and never revoked gave the attacker, from 2026-10-10, a GitHub organization owner's CLI token, with
  which it stole two maintainers' tokens and, on 2026-10-21, overrode branch protection to build the release from a look-alike repository; Socket independently
  found secret-stealing workflows running on 2026-10-10. Wiz saw stolen AWS instance-role credentials tested about 4.5 hours after exfiltration; PyPI and
  the registries removed the release the same day and the maintainers say to pin 1.106.2 or an explicit earlier version.
discovered_at: "2026-10-22T03:44:00Z"
updated_at: "2026-10-24T03:40:10Z"
event_date: "2026-10-21"
run_id: 2026-10-22T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, infostealer, cloud]
regions: [global]
sectors: [technology]
entities: ["product:litellm", "product:berriai-litellm"]
techniques: [T1195.001, T1195.002, T1070, T1546.018, T1552.001, T1552.004, T1552.005, T1555.003, T1102.001, T1105, T1027.013, T1140, T1528, T1078.004, T1087.004]
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
  - url: "https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain"
    publisher: "LiteLLM maintainers (root-cause post, attack chain)"
    date: "2026-10-23"
    role: primary
  - url: "https://socket.dev/blog/litellm-attack-timeline"
    publisher: "Socket Research Team (attack timeline)"
    date: "2026-10-23"
    role: corroborating
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
  - quote: "On October 10th, the threat actor used this key to gain access to our LiteLLM Agent Platform and extracted this GitHub CLI OAuth token."
    publisher: "LiteLLM maintainers (root-cause post, attack chain)"
    source_url: "https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain"
  - quote: "However, key revocation did not occur for the master key."
    publisher: "LiteLLM maintainers (root-cause post, attack chain)"
    source_url: "https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain"
  - quote: "Each credential was checked with sts:GetCallerIdentity, followed by bedrock:ListFoundationModels and a ListModels call, consistent with LLMjacking."
    publisher: "Wiz Research"
    source_url: "https://www.wiz.io/blog/litellm-compromised-steals-credentials"
  - quote: "PyPI has now quarantined version 1.107.0."
    publisher: "Aikido Security"
    source_url: "https://www.aikido.dev/blog/litellm-compromised-infostealer-rat"
verification: multi-source
sourcing_note: >
  Socket, Upwind (in the project's own issue), Wiz and Aikido analysed the release independently and agree on the mechanism; the
  maintainers' incident post and issue replies give the exposure windows and the removals, and their root-cause post of 2026-10-23,
  which calls itself the canonical account and corrects assumptions in their earlier status updates, gives the attack chain. Socket
  independently found secret-stealing workflows in the repository on 2026-10-10 from its Actions performance metrics and says it has not
  established how the attacker first obtained access; LiteLLM says its audit logs tie the token stolen on 2026-10-10 to the approval of
  the release.
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
updates:
  - at: "2026-10-24T03:40:10Z"
    run_id: 2026-10-24T0255Z-intel
    type: update
    summary: >
      The maintainers' root-cause post of 2026-10-23 replaces the earlier log-leak hypothesis: a master
      key committed to a public repository on 2026-05-27 and never revoked gave the attacker an
      organization owner's GitHub CLI token on 2026-10-10, eleven days before the release, and Socket
      independently found secret-stealing workflows running that day.
    fields: [body, evidence, sources, sourcing_note, summary, techniques]
migrated_from: null
---

Socket reports that LiteLLM 1.107.0, an open-source LLM gateway, carries malicious Python startup files in all seven wheels, and that Upwind found the same payload in the published images ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)). A startup hook and a second startup module in the Python library directory run at every Python start without the application importing LiteLLM: the first collects cloud, Kubernetes, CI, registry and database credentials, SSH, GPG and TLS private keys, browser stores, AI-tool credential files, environment variables and, where configured, the credentials saved in a LiteLLM proxy database; the second forks a detached loader that polls a file in a GitHub repository for a domain and would execute Python downloaded from it with no signature or hash check, though at 13:01 UTC the pointer returned an empty body, which stops the loader before its download stage ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)).

The payload is not in the git tag: a packaging setting in an untagged commit pulls it into the wheel, and the container build provenance records a source repository named Berri-AI/litellm, one hyphen away from BerriAI/litellm ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)). The maintainers' root-cause post of 2026-10-23, which they call the canonical account and which corrects assumptions in their earlier status updates, traces the chain to a configuration file committed on 2026-05-27 to a public repository with the master key of an experimental internal agent service; the commit was force-pushed over but the key was never revoked ([LiteLLM, 2026-10-23](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)). On 2026-10-10 the attacker used that key against the service's API, which returned the GitHub CLI OAuth token of an organization owner, not a service account and not scoped down, and from then on the attacker held owner-level access to every repository; such CLI tokens are post-2FA and exempt from GitHub's re-authentication for sensitive actions ([LiteLLM, 2026-10-23](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)). With it the attacker pushed throwaway branches whose workflows posted CI secrets to an external capture endpoint, yielding the CLI tokens of two maintainers, and deleted the workflow runs minutes later ([LiteLLM, 2026-10-23](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)). Socket found secret-exfiltration workflows running in the repository on 2026-10-10 from its Actions performance metrics, eleven days before the release attack, says it has not established how the attacker first obtained access and does not claim that the 2026-10-10 theft produced the access used on 2026-10-21, while LiteLLM says its audit logs tie the token stolen on 2026-10-10 to the approval of the release ([Socket, 2026-10-23](https://socket.dev/blog/litellm-attack-timeline)). On 2026-10-21 a push to the private release-orchestration repository with a maintainer's token was rejected by branch protection, and the owner's token then overrode it so that the build could be pointed at the look-alike repository; the owner's token dispatched the staging build, a second maintainer's token approved the production gate, a third maintainer's token deleted the run records, and the owner's token force-pushed the history clean, after the maintainers had relaxed the release rule earlier that week so that any two engineers could trigger and approve a release ([LiteLLM, 2026-10-23](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)). LiteLLM distributes an embargoed release for a vulnerability whose disclosure is scheduled for 2026-10-27 to enterprise customers through a private registry ([LiteLLM, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)). PyPI quarantined 1.107.0 and the images were pulled the same day ([Aikido, 2026-10-21](https://www.aikido.dev/blog/litellm-compromised-infostealer-rat); [LiteLLM, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)).

**Exposure:** an environment that installed litellm 1.107.0 from PyPI between 11:39 and 13:23 UTC on 2026-10-21, or pulled the v1.107.0, latest, main-latest or main-stable tag of the official images from GHCR (until about 13:51 UTC) or Docker Hub (until 14:20 UTC); lockfiles, caches, build logs and running image digests show which ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise); [LiteLLM, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)).

**Detection:** in the cloud audit logs of every account the host could reach, a caller-identity check followed by a Bedrock model listing and IAM enumeration, made with an instance-role credential harvested from CI runners or Kubernetes nodes from an address outside your estate, which Wiz saw from 16:20 UTC on 2026-10-21 ([Wiz, 2026-10-21](https://www.wiz.io/blog/litellm-compromised-steals-credentials)); on hosts, startup hooks and sitecustomize modules in a Python library directory that your tooling did not install, a detached Python process holding a lock file, and an encrypted archive posted to a path labelled as a health check ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)). In the GitHub organization audit log, short-lived throwaway branches that add a single workflow file, workflow runs deleted minutes after they ran, and branch-protection and force-push-block overrides made with an owner's token; the log records a hash of the token behind each action, which tied the stolen maintainer token to the release approval ([LiteLLM, 2026-10-23](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)). Starting Python or pip in an affected environment can run the payload again, and removing the package directory does not remove the startup files or stop a running loader ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)).

**Defender takeaway:** rotate every credential the host could reach ([LiteLLM, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)), because removing the package does not remove the startup files ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)) and stolen cloud credentials were in use within hours ([Wiz, 2026-10-21](https://www.wiz.io/blog/litellm-compromised-steals-credentials)); rebuild from a reviewed release and pin container digests ([Socket, 2026-10-21](https://socket.dev/blog/litellm-compromise)), and move to 1.106.2 or an explicit earlier version as the maintainers advise ([LiteLLM, 2026-10-21](https://docs.litellm.ai/blog/security-incident-oct-21-2026)). For your own pipelines, the root cause was a key that was removed from a public repository's history but never revoked, and an organization owner's CLI token held by an automation service; the maintainers call it an illustration of the risk of failing to rotate a potentially exposed key ([LiteLLM, 2026-10-23](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)).

## Update — 2026-10-24T03:40:10Z

The maintainers published a root-cause post on 2026-10-23 that supersedes the earlier hypothesis that the tokens were read from the logs of an internet-exposed internal deployment: their request logs show the first token came from a different service, an experimental agent platform whose master key had been committed to a public repository on 2026-05-27 and never revoked ([LiteLLM, 2026-10-23](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)). The attacker used the key on 2026-10-10 to obtain an organization owner's GitHub CLI token, so access began eleven days before the release, and the same day throwaway branches in two repositories ran workflows that posted CI secrets to an external capture endpoint and were deleted minutes later, yielding the tokens of two further maintainers ([LiteLLM, 2026-10-23](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)).

Socket found the same activity independently from the repository's Actions performance metrics, including a second run on 2026-10-12 that took 14 further secrets, and says it has not established how the attacker first obtained access ([Socket, 2026-10-23](https://socket.dev/blog/litellm-attack-timeline)). On 2026-10-21 three credentials did different jobs: the owner's token overrode branch protection and later force-pushed the history clean, a second maintainer's token approved the production gate and a third maintainer's token deleted the run records, after the maintainers had relaxed the release rule earlier that week so that any two engineers could trigger and approve a release ([LiteLLM, 2026-10-23](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)). The maintainers say they are revoking every token tied to every internal system and vendor platform, and that the attacker's activity on other systems focused on upstream inference API tokens ([LiteLLM, 2026-10-23](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain)).
