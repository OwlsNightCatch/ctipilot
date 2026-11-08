---
title: "Inside the LiteLLM Hack: 153GB and 2,488 Organizations"
author: Cybersecurity research team
url: https://blog.gitguardian.com/inside-the-litellm-hack/
hostname: gitguardian.com
description: Attackers dumped everything they harvested from LiteLLM builds during a 40-minute window in March. Here is what is inside and what it says about where secrets live.
sitename: GitGuardian Blog - Take Control of Your Secrets Security
date: "2026-11-04"
tags: ['Security Research', 'Breach explained']
fingerprint: "3cc6759b4eb616c9"
---
## TL;DR

- Hudson Rock and CloudSEK confirmed the scale of the March LiteLLM PyPI hack: a 153GB archive, 433,909 files.
- 118,829 CI runner dumps trace back to 2,488 organizations across the exposed archive.
- Many dumps carry no email, domain, or hostname — unattributable, with no way to disclose.

**Update, Nov. 3, 2026**: LiteLLM faced a separate compromise in October 2026. The incident started with an administrative key exposed in a public repository. The file containing the key was deleted, but the credential itself was never revoked and remained valid for more than four months. *More details are below.*

The March compromise of `litellm` lasted about 40 minutes on PyPI. This week we learned what the attackers stole in that time.

On August 12, 2026, [<u>Hudson Rock published its analysis</u>](https://www.infostealers.com/article/largest-ai-supply-chain-breach-of-2026-litellm-hack-impacts-thousands-of-global-enterprises-claim-your-ethical-disclosure/?ref=blog.gitguardian.com) of the exfiltration archive: a 153GB RAR containing 433,909 files. Its researchers attributed 118,829 CI runner dumps to 2,488 corporate domains. [<u>CloudSEK published parallel victim research</u>](https://www.cloudsek.com/blog/ai-supply-chain-breach-2500-companies-434000-cicd-pipelines?ref=blog.gitguardian.com) on August 11, covering the same campaign from its own intelligence sources.

Neither report is about malware behavior. That was documented in March. These are about the loot.

## **The blast radius, now measured**

In [<u>March we wrote</u>](https://blog.gitguardian.com/litellm-supply-chain-attack/) about the LiteLLM supply chain attack when the infostealer harvested everything an attacker could want. We listed SSH keys, cloud credentials, Docker configuration, and crypto wallet data, and said the blast radius was likely significant. That was an inference from malware analysis. The archive turns it into counts.

On each compromised runner, the payload escalated to root. It swept SSH keys, AWS, GCP, and Azure credentials, Kubernetes service account tokens, `.env` files, and CI/CD secrets. On AI builds, it also took LLM API keys and gateway configuration, which is access to an organization's entire model stack rather than one credential.

In March we said the keys to your infrastructure were potentially in the hands of threat actors. Five months later, the qualifier is gone. 118,829 runner dumps, 2,488 organizations, one 40-minute window.

## **What is inside the dump**

Hudson Rock's write-up shows environment dumps captured mid-execution:

- `AWS_SECRET_ACCESS_KEY`
- `SALESFORCE_CLIENT_SECRET`
- `SLACK_SIGNING_SECRET`
- Azure environment credentials
- AI provider API keys
- `GITLAB_USER_EMAIL` and `CI_SERVER_FQDN`, which is how attribution can be done

In one example, Hudson Rock reports a single organization with 17 compromised pipeline dumps exposing Bitbucket deployment tokens, Elastic API keys, internal JWTs, and NPM tokens. Publishing credentials in the loot is how a supply chain incident becomes a second supply chain incident.

## **The half nobody can attribute**

The most useful finding in either report is a negative one.

Hudson Rock does not put a number on it, but reports that many dumps carry live database passwords, cloud credentials, and third-party API keys with no company email, no custom domain, and no internal hostname. Those records cannot be attributed to anyone. The organizations behind them will appear on no victim list and will receive no disclosure email.

Attributed records can still mislead. Hudson Rock describes a pipeline whose committer email ended in `@siriusxm.com`, while the environment dump pointed to `gitlab.adswizz.com` and a matching registry host. The breach sat in AdsWizz infrastructure, a SiriusXM subsidiary. Routing an alert on the email alone reaches the wrong security team.

Hudson Rock ran an ethical disclosure program. CloudSEK published a public lookup tool. Neither can notify a company it cannot name. Responsible disclosure needs an address, and a generically configured runner does not leave one. Good intentions do not close that gap.

## **Detection that does not need your name**

If disclosure cannot reach you, detection has to start in your own environment.

### Know what you had

An inventory of your [<u>non-human identities</u>](https://blog.gitguardian.com/tag/nhi/) tells you which credentials lived in those pipelines on March 24, what each one reaches, and who owns it. Without that list, "were we exposed" has no answer.

### Know what sits on the endpoint

The payload ran at Python interpreter startup, on developer laptops as readily as on CI runners. It never touched a repository. [<u>Developer Endpoint Protection</u>](http://gitguardian.com/developer-endpoint-protection?ref=blog.gitguardian.com) extends secrets detection to the machines where code actually executes, which is where this campaign collected everything it collected.

### Know what is still live

[<u>Continuous secrets detection</u>](https://www.gitguardian.com/monitor-internal-repositories-for-secrets?ref=blog.gitguardian.com) with automated validity checking turns "we might be in there somewhere" into a ranked list of credentials to rotate today.

### Know when someone uses them

This stealer collected environment variables and `.env` files, which is where [honeytokens](https://www.gitguardian.com/honeytoken?ref=blog.gitguardian.com) sit. The first time an attacker tries one, you get an alert. That signal reaches you without anyone having to identify you first, which is the gap this archive exposes.

## Update Nov 2026: An exposed LiteLLM admin key stayed valid for months before the October compromise

LiteLLM suffered a separate supply chain compromise in October 2026. It is a different attack chain from the March incident covered in this article, and no source currently links the two.

On Oct. 21, 2026, LiteLLM’s release pipeline published a malicious version, 1.107.0, to PyPI and container registries, including Docker Hub and GHCR. [<u>According to LiteLLM</u>](https://docs.litellm.ai/blog/security-incident-oct-21-2026?ref=blog.gitguardian.com), this version contained malware that steals credentials and loads remote code execution tools. PyPI quarantined the release in under two hours.

Microsoft’s analysis found that the malware ran whenever Python started on an infected machine, even in projects that never used LiteLLM. It also queried LiteLLM’s proxy database, where upstream provider keys are stored. As [<u>Deepak Gupta</u>](https://securityboulevard.com/2026/11/litellms-second-breach-began-with-a-key-nobody-revoked/?ref=blog.gitguardian.com) wrote, “*an AI gateway is a vault of other people’s keys*.”

### How a deleted key led to a hijacked release

LiteLLM’s [<u>root cause analysis</u>](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain?ref=blog.gitguardian.com) found that the attack started on May 27. A configuration file with an administrative key for an internal LiteLLM service was accidentally committed to a public repository. The team noticed and deleted the file about three hours later, **but they did not revoke the key**. As a result, the key remained active for over four months.

On Oct. 10, an attacker used the key to access the service’s API, which gave them the GitHub CLI token of a LiteLLM GitHub organization owner. This token was not limited to specific repositories. The attacker then ran workflows to steal tokens from two more maintainers. On Oct. 21, they used the owner’s token to override branch protection and build a release from a lookalike repository, then a second maintainer’s token to approve it.

### Deleting a secret does not revoke it

Removing a key from a file, or even from git history, reduces exposure but does not invalidate copies that may already exist. This is why revocation comes first in any response to a leaked secret, and why validity checks matter. They show if a leaked key still works, no matter how long ago it was leaked.

The incident also shows why the identity and access behind a credential matter. In this case, an internal service held an unscoped GitHub organization-owner token. Once the attacker gained access to that service, one forgotten key became a path to owner-level GitHub access and, ultimately, the release pipeline.

### What to do if you ran LiteLLM 1.107.0

If you installed LiteLLM 1.107.0 or pulled the latest, main-latest, or main-stable Docker images on Oct. 21, assume that every credential the machine could access is compromised. To check for the malware, do not run Python or pip in an environment that might be affected. Rebuild affected environments from trusted artifacts, then revoke exposed credentials from a clean machine. Simply uninstalling LiteLLM is not sufficient because the malicious startup files could persist outside the package itself.

Check our [<u>Remediation Guide</u>](https://www.gitguardian.com/remediation?ref=blog.gitguardian.com) for provider-specific revocation steps.
