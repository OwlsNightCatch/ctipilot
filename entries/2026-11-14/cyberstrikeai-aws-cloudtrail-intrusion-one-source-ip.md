---
schema: 1
kind: threat
title: "CyberStrikeAI turned on AWS: Elastic reads one server's 16 days across eight identities in four accounts, 56 user-data reads in 141 milliseconds, and why six detections each rated medium or low and only the source address tied them together"
headline: "Elastic: CyberStrikeAI against AWS, six medium or low alerts joined only by source IP; alert on user-data bursts"
summary: "Elastic Security Labs reports that between 2026-09-30 and 2026-10-16 one server running the open-source CyberStrikeAI platform used the credentials of eight AWS identities (five IAM users, three EC2 instance roles) across four accounts, reading secrets and EC2 user data and, in one case, issuing a Systems Manager command. Every step is a call a legitimate role makes daily, so six detection rules each fired at medium or low severity and only the shared source address showed they belonged to one intrusion; Elastic does not know how the credentials were obtained and names no victim."
discovered_at: "2026-11-14T03:55:00Z"
updated_at: null
event_date: "2026-11-13"
run_id: 2026-11-14T0255Z-intel
priority: notable
immediate_action: null
tags: [cloud, ai-abuse]
regions: [global]
sectors: []
entities:
  - tool:cyberstrikeai
  - product:amazon-ec2
techniques: [T1078.004, T1087.004, T1552.005, T1555.006, T1651]
affected_products: ["Amazon Web Services IAM", "AWS Secrets Manager", "AWS Systems Manager Parameter Store", "Amazon EC2"]
cves: []
sources:
  - url: "https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion"
    publisher: "Elastic Security Labs"
    date: "2026-11-13"
    role: primary
  - url: "https://www.team-cymru.com/post/tracking-cyberstrikeai-usage"
    publisher: "Team Cymru"
    date: "2026-03-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The main activity came from app-role, an EC2 instance role in Account A. It read a secret, made one user data request, then fired a burst of 56 user data requests in 141 milliseconds."
    publisher: "Elastic Security Labs"
    source_url: "https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion"
  - quote: "Only the shared source IP showed they belonged to one intrusion."
    publisher: "Elastic Security Labs"
    source_url: "https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion"
  - quote: "We cannot prove an LLM agent was making the decisions, and we do not know how the attacker obtained the credentials."
    publisher: "Elastic Security Labs"
    source_url: "https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion"
verification: single-source
sourcing_note: "Elastic Security Labs is the only source for the intrusion, reporting its own telemetry on anonymised accounts; Team Cymru documents the tool and its servers but not this intrusion. Elastic bases the AI-assisted label on the tool attribution and the machine-speed behaviour, not on proof that a model made the decisions, and attributes the server to the tool through internet scan data."
confidence: medium
references:
  - 2026-07-09/sygnia-ai-orchestrated-aws-cloud-intrusion-72h
  - 2026-10-26/jpcert-nict-app-to-backend-api-attacks-ai-scanning-japan
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

Between 2026-09-30 and 2026-10-16 one server serving a CyberStrikeAI web interface used the credentials of eight AWS identities (five IAM users and three EC2 instance roles) across four accounts and generated 78 alerts, the first case Elastic has seen of this tooling turned on AWS ([Elastic Security Labs, 2026-11-13](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion)). It started by validating identities: GetCallerIdentity on four IAM users in three accounts within 51 minutes, three of the calls in the same second ([Elastic Security Labs, 2026-11-13](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion)). An instance role then read a secret, made one user-data request and fired 56 more in 141 milliseconds, spacing Elastic says fits tooling working through a prepared list of instance IDs ([Elastic Security Labs, 2026-11-13](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion)). On 2026-10-02 another instance role read an encrypted Systems Manager parameter and issued a SendCommand 29 seconds later, which Elastic calls the highest-risk activity; the audit log does not show the command or its outcome ([Elastic Security Labs, 2026-11-13](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion)). After 14 quiet days the server returned and revalidated credentials, including a user in a fourth account ([Elastic Security Labs, 2026-11-13](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion)). Elastic does not know how the credentials were obtained and infers that the instance-role sessions, used from an outside address, were taken from the instances, for example through SSRF or host compromise ([Elastic Security Labs, 2026-11-13](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion)). Team Cymru counted 21 unique addresses running CyberStrikeAI between 2026-01-20 and 2026-02-26 ([Team Cymru, 2026-03-02](https://www.team-cymru.com/post/tracking-cyberstrikeai-usage)).

**Exposure:** AWS accounts where IAM user keys or instance-role credentials can leave the account and the principals may read EC2 user data or Secrets Manager values or send Systems Manager commands; secrets in user data are readable by any such principal and Elastic says to treat them as exposed ([Elastic Security Labs, 2026-11-13](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion)).

**Detection:** in cloud control-plane audit logs, a burst of user-data requests from one role session; a first-time GetCallerIdentity from one external address across several users or accounts within a minute; GetSessionToken or GetSecretValue from an instance-role session whose source address is neither the instance nor your NAT; and a decrypting GetParameter followed within a minute by an SSM SendCommand from the same role ([Elastic Security Labs, 2026-11-13](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion)). Six rules fired at medium or low severity, and Elastic recommends correlating such alerts by source address over a flexible window, since the gaps between steps ran from 141 milliseconds to 14 days ([Elastic Security Labs, 2026-11-13](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion)).

**Triage:** each call is one a legitimate role makes every day, so the discriminators are the source address, the number of distinct identities, accounts or instances one address touches in minutes, and the decrypt-then-SendCommand pairing ([Elastic Security Labs, 2026-11-13](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion)).

**Defender takeaway:** correlate low and medium cloud alerts by source address, restrict `ec2:DescribeInstanceAttribute` for user data to the roles that need it, move secrets out of user data, and on a hit rotate instance-role credentials by replacing the instance profile or the instance, because stolen role credentials expire but can be reissued while the host stays compromised ([Elastic Security Labs, 2026-11-13](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion)). As of November none of the three servers served the CyberStrikeAI interface, so the indicator addresses are for retrospective hunting ([Elastic Security Labs, 2026-11-13](https://www.elastic.co/security-labs/threat-command/cyberstrikeai-aws-cloudtrail-intrusion)).
