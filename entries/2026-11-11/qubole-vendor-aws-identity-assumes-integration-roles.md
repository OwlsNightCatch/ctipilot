---
schema: 1
kind: incident
title: "Qubole: an attacker used IAM credentials from a vendor-associated AWS account to assume dormant cross-account integration roles in dozens of customer accounts, then harvested secrets and validated Entra ID and Okta client credentials (Wiz and Sentra, 14 to 26 October)"
headline: "Stolen Qubole vendor credentials assumed customers' idle AWS integration roles; a source-IP condition stops it"
summary: >
  Wiz, working with Sentra and Mandiant, reports that between 2026-10-14 and 2026-10-26 an actor used IAM credentials from an AWS account associated with the data platform Qubole to assume customers' cross-account integration roles, each call carrying the correct External ID; most roles had otherwise been idle. Inside each account the actor listed resources, read Secrets Manager, Parameter Store and Lambda configuration, tested harvested AWS, Entra ID and Okta credentials with TruffleHog and downloaded S3 data, in some cases whole buckets; no victim is named, the counts range from more than a dozen to dozens, and how the vendor identities were compromised is not known.
discovered_at: "2026-11-11T03:41:30Z"
updated_at: null
event_date: "2026-11-09"
run_id: 2026-11-11T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, cloud, identity, data-breach]
regions: [global]
sectors: [technology]
entities: ["incident:qubole-aws-cross-account-role-abuse-2026-10", "tool:trufflehog", "product:qubole", "product:amazon-web-services-iam", "product:aws-secrets-manager", "product:aws-systems-manager-parameter-store", "product:aws-lambda", "product:amazon-s3"]
techniques: [T1199, T1078.004, T1580, T1619, T1555.006, T1530]
affected_products: ["Qubole", "Amazon Web Services IAM", "AWS Secrets Manager", "AWS Systems Manager Parameter Store", "AWS Lambda", "Amazon S3"]
cves: []
sources:
  - url: "https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild"
    publisher: "Wiz"
    date: "2026-11-09"
    role: primary
  - url: "https://sentra.io/blog/breaches/inside-the-qubole-supply-chain-attack"
    publisher: "Sentra"
    date: "2026-11-09"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/hackers-exploit-trusted-aws-access-to-breach-multiple-cloud-environments/"
    publisher: "BleepingComputer"
    date: "2026-11-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Working with Sentra and Mandiant, Wiz observed a threat actor using IAM credentials from an AWS account associated with Qubole between October 14 and October 26, 2026."
    publisher: "Wiz"
    source_url: "https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild"
  - quote: "Every AssumeRole request we attributed to the threat actor included an External ID, and every one succeeded."
    publisher: "Wiz"
    source_url: "https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild"
  - quote: "In this activity, a source IP condition alone would have blocked every role assumption we observed."
    publisher: "Wiz"
    source_url: "https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild"
  - quote: "Dozens of Qubole customers were impacted."
    publisher: "Sentra"
    source_url: "https://sentra.io/blog/breaches/inside-the-qubole-supply-chain-attack"
  - quote: "BleepingComputer could not find a public announcement from Qubole about this incident."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/hackers-exploit-trusted-aws-access-to-breach-multiple-cloud-environments/"
verification: multi-source
sourcing_note: >
  Wiz's incident response and Sentra's customer-side detection are separate first-hand observations of the same activity, and Wiz worked with Sentra and Mandiant. The victim count differs between passages and outlets (Sentra "dozens" and "more than a dozen", BleepingComputer "tens of companies"), no victim is named, Qubole had made no public statement when BleepingComputer looked, and the sources do not say how the Qubole IAM users were compromised. Wiz also describes a separate, unlinked use of customer-owned AWS access keys created for Qubole integrations on 8 to 11 October.
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
  - "In every AWS account, list the IAM roles whose trust policy names an external vendor account, delete those of finished integrations, pin the rest to the vendor's specific principal with an aws:SourceIp or aws:SourceVpce condition, and search CloudTrail from 2026-10-01 for AssumeRole calls into them from non-vendor network addresses, using the account identifier and session-name prefix Wiz publishes, because the actor's calls carried the correct External ID and succeeded on roles nobody was using."
updates: []
migrated_from: null
---

Wiz, working with Sentra and Mandiant, observed a threat actor using IAM credentials from an AWS account associated with Qubole, a big-data platform, between 2026-10-14 and 2026-10-26 ([Wiz, 2026-11-09](https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild)). The actor used two Qubole IAM users to call sts:AssumeRole on the cross-account integration roles that customers had created to trust Qubole's account; "every AssumeRole request we attributed to the threat actor included an External ID, and every one succeeded", most of the roles were otherwise not in use, and the traffic came from a rented hosting server and commercial VPN exits, not the AWS infrastructure where legitimate platform traffic originates ([Wiz, 2026-11-09](https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild); [Sentra, 2026-11-09](https://sentra.io/blog/breaches/inside-the-qubole-supply-chain-attack)).

Inside each account the actor enumerated resources, read Lambda function configuration, Secrets Manager and Systems Manager Parameter Store, ran TruffleHog to test AWS access keys, Entra ID service-principal client secrets and Okta client credentials it found, and then downloaded S3 data opportunistically, in some cases whole buckets in one session ([Wiz, 2026-11-09](https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild)). Wiz found no tie to other reported activity and judges the targeting opportunistic; how the Qubole IAM users were compromised is not stated. Sentra writes that dozens of Qubole customers were impacted, and BleepingComputer could not find a public Qubole announcement ([Sentra, 2026-11-09](https://sentra.io/blog/breaches/inside-the-qubole-supply-chain-attack); [BleepingComputer, 2026-11-10](https://www.bleepingcomputer.com/news/security/hackers-exploit-trusted-aws-access-to-breach-multiple-cloud-environments/)). No Swiss or public-sector victim is named, but the exposure is shared by any account that gave a data or analytics vendor a cross-account role and left it in place.

**Exposure:** any AWS account holding an IAM role whose trust policy lets a Qubole account, or any other vendor account, assume it, including roles left from integrations that ended; the roles' trust policies and last-used data show them, and Wiz publishes the vendor account identifier, the two principals and the attacker address ranges for a CloudTrail hunt back to 2026-10-01 ([Wiz, 2026-11-09](https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild)).

**Detection:** in cloud control-plane audit logs, AssumeRole events into integration roles whose calling identity is the vendor account but whose source address is not AWS infrastructure, and session names with a consistent attacker-chosen prefix; GetCallerIdentity calls from many keys within seconds and Entra ID or Okta sign-ins by service principals or clients right after, as the actor validates credentials; ListSecrets, GetSecretValue, Parameter Store and Lambda configuration reads in bursts. Object reads are absent from CloudTrail management events, so S3 data events or server access logs must be on, and Wiz says missing logs left responders unable to see what was read ([Wiz, 2026-11-09](https://www.wiz.io/blog/qubole-cross-account-access-abused-in-the-wild)).

**Triage:** legitimate vendor traffic comes from the vendor's own AWS infrastructure; the correct External ID does not discriminate, because it is logged in plaintext and often stored by the vendor, while a vendor role assumed from a consumer VPN or a hosting provider the vendor has never used is the high-signal case.

**Defender takeaway:** inventory third-party trust relationships, delete the roles of ended integrations, narrow each trusted principal to the vendor's specific principal and add a source-address or endpoint condition, which Wiz says alone would have blocked every observed assumption; after an incident, revoke the issued role sessions and rotate every secret, parameter, Lambda variable and identity-provider credential the role could read.
