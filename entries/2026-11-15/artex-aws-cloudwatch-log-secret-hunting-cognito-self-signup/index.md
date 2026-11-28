---
schema: 1
kind: threat
title: "ARTEX against AWS: Datadog sees agent sessions open with anonymous S3 reads, search CloudWatch Logs for secrets with stolen long-term IAM keys, and self-register in public Cognito user pools to obtain AWS credentials"
headline: "ARTEX in AWS: CloudWatch log searches for secrets, Cognito self-sign-up for credentials; hunt CloudTrail for both"
summary: "Datadog Security Labs reports that in October 2026 operators of the ARTEX agentic penetration-testing framework worked against several AWS environments with a focus on financial data: sessions opened with anonymous S3 reads, a stolen long-term IAM key drove CloudWatch Logs FilterLogEvents searches for company names, passwords and access keys, and where no key was held the agent self-registered in a public Cognito user pool and traded the tokens for AWS credentials. Datadog says the distributions it studied do not appear to carry a cloud playbook of their own, so the steps follow the model behind them."
discovered_at: "2026-11-15T15:09:32Z"
updated_at: null
event_date: "2026-11-09"
run_id: 2026-11-15T1407Z-audit
priority: notable
immediate_action: null
tags: [cloud, ai-abuse, identity]
regions: [global]
sectors: []
entities:
  - tool:artex
techniques: [T1078.004, T1530, T1619, T1595.003, T1552, T1136.003, T1526, T1580]
affected_products: ["Amazon Cognito", "Amazon CloudWatch Logs", "Amazon S3"]
cves: []
sources:
  - url: "https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/"
    publisher: "Datadog Security Labs"
    date: "2026-11-09"
    role: primary
  - url: "https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors"
    publisher: "Wiz Research"
    date: "2026-10-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "In October 2026, Datadog observed in-the-wild activity from ARTEX, an AI-native penetration framework, against several AWS environments, with a focus on accessing financial data."
    publisher: "Datadog Security Labs"
    source_url: "https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/"
  - quote: "Before either, every session we reviewed opened with unauthenticated S3 requests."
    publisher: "Datadog Security Labs"
    source_url: "https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/"
  - quote: "We saw the agent go further, registering an account, collecting tokens, trading them for AWS credentials, then enumerating resources."
    publisher: "Datadog Security Labs"
    source_url: "https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/"
  - quote: "In this case, all of them failed because the identity pool's authenticated role did not grant the required permissions."
    publisher: "Datadog Security Labs"
    source_url: "https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/"
verification: single-source
sourcing_note: "Datadog Security Labs is the only source for the AWS sightings, from its own telemetry on unnamed accounts, and attributes them to ARTEX; Wiz independently describes the same habit of requesting a non-existent path before a guessing burst against web applications. Datadog names no victim, no actor behind these sessions and no way the long-term keys were obtained."
confidence: medium
references:
  - 2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse
  - 2026-11-14/cyberstrikeai-aws-cloudtrail-intrusion-one-source-ip
  - 2026-11-06/exposed-app-credentials-entra-signins-msp-clients-artex
  - 2026-11-08/workos-artex-agent-escaped-sandbox-internal-tool-breach
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

Datadog Security Labs reports that in October 2026 operators of ARTEX, the agentic penetration-testing framework Microsoft ties to Storm-0940, worked against several AWS environments with a focus on financial data, and that every session it reviewed opened with unauthenticated S3 reads, which CloudTrail records with a userIdentity type of AWSAccount and an accountId of anonymous, calling GetObject, ListObjects and similar read APIs ([Datadog Security Labs, 2026-11-09](https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/)). Where S3 hosted a web front end, the agent read build manifests and runtime configuration, and it requested objects named like placeholders just before bursts of key guesses ([Datadog Security Labs, 2026-11-09](https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/)), the habit Wiz saw as a request for a path that should not exist before each fuzzing run ([Wiz Research, 2026-10-22](https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors)).

With a valid long-term IAM access key, the agent's most frequent call was CloudWatch Logs FilterLogEvents, always with a limit of 1,000 events: it first searched log text for the names of cryptocurrency firms, hedge funds and invoicing terms and, in a later session on 2026-10-20, for storage links, internal addresses, database references, passwords and AKIA-style access keys ([Datadog Security Labs, 2026-11-09](https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/)).

Without a key, the agent self-registered in a public Cognito user pool, iterating against a PreSignUp Lambda that checked a tenant domain, then ran InitiateAuth, RespondToAuthChallenge, GetUser and GetTokensFromRefreshToken and traded the tokens for short-term AWS credentials, which CloudTrail shows under the CognitoIdentityCredentials role session name; some SignUp calls named the tool in the user agent ([Datadog Security Labs, 2026-11-09](https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/)). It then tried read-only discovery calls such as ListBuckets, ListSecrets, DescribeParameters, ListTopics, DescribeLogGroups, GetRestApis, DescribeRepositories and ListFunctions, all of which failed because the identity pool's authenticated role was narrow ([Datadog Security Labs, 2026-11-09](https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/)).

Datadog found hundreds of internet-exposed ARTEX consoles, often in Mandarin, and says the distributions it analysed do not appear to carry a cloud methodology of their own, so the post-exploitation playbook depends on the model in use; some versions block .gov, .gov.cn, .edu and .edu.cn targets by default ([Datadog Security Labs, 2026-11-09](https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/)).

**Exposure:** AWS accounts with long-term IAM access keys that may have leaked, applications whose public Cognito user pools allow self-registration with identity pools that vend AWS credentials to authenticated users, and S3 buckets that serve web front ends without authentication.

**Detection:** in CloudTrail and S3 access logs, anonymous read bursts that include requests for placeholder-named objects; FilterLogEvents calls with a fixed limit of 1,000 from a long-term user key; Cognito SignUp spikes with PreSignUp failures, followed by CognitoIdentityCredentials sessions issuing broad read-only discovery calls that end in access-denied errors; and instance-role credentials used from an address outside AWS, which Datadog lists among the unusual patterns to hunt ([Datadog Security Labs, 2026-11-09](https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/)).

**Triage:** FilterLogEvents is a routine call for log tooling and engineers; the discriminator is a long-term user key searching log text for credentials, internal addresses or company names at a constant page limit, from an address that key does not normally use.

**Defender takeaway:** check which Cognito user pools allow open self-registration and what their identity pools' authenticated roles can read, rotate long-term IAM keys found in code or logs, and hunt CloudTrail for the sequences above; a narrow authenticated role is what stopped the Cognito path in the case Datadog describes.
