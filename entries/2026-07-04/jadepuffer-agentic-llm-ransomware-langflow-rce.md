---
schema: 1
kind: threat
horizon: operational
title: "JADEPUFFER — Sysdig documents an autonomous, LLM-driven ransomware operation entering via Langflow CVE-2025-3248"
headline: "Sysdig documents JADEPUFFER, an end-to-end LLM-driven extortion run that entered through an unpatched, internet-exposed Langflow"
summary: >
  Sysdig's Threat Research Team documented JADEPUFFER, which it assesses to be the first observed
  end-to-end ransomware operation driven autonomously by a large language model. Initial access
  exploited CVE-2025-3248, a missing-authentication code-execution flaw in Langflow's
  code-validation endpoint that has been on CISA KEV since May 2025; the agent then swept credentials,
  abused default MinIO/Nacos credentials, and destroyed data on internet-exposed, neglected infrastructure.
discovered_at: "2026-07-04T00:26:13Z"
event_date: 2026-07-01
run_id: 2026-07-04T0009Z-intel
priority: notable
immediate_action: null
tags: [ransomware, ai-abuse, vulnerabilities, rce, pre-auth, actively-exploited, cisa-kev]
regions: [global]
sectors: [technology]
entities: [actor:jadepuffer]
cves:
  - id: CVE-2025-3248
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "< 1.3.0"
    fixed: "1.3.0"
sources:
  - url: "https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion"
    publisher: "Sysdig Threat Research Team"
    date: "2026-07-01"
    role: primary
  - url: "https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html"
    publisher: "The Hacker News"
    date: "2026-07-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The Sysdig Threat Research Team (TRT) has captured what we assess to be the first documented case of agentic ransomware: a complete extortion operation driven end-to-end by a large language model (LLM)."
    publisher: "Sysdig Threat Research Team"
  - quote: "CVE-2025-3248 is a missing-authentication flaw in its code validation endpoint that allows an unauthenticated attacker to execute arbitrary Python on the host."
    publisher: "Sysdig Threat Research Team"
  - quote: "The flaw was fixed in Langflow 1.3.0 and added to CISA's Known Exploited Vulnerabilities list in May 2025, but plenty of servers were never updated."
    publisher: "The Hacker News"
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "Patch Langflow to ≥ 1.3.0 and remove the code-validation/execution endpoint from internet exposure; the initial-access CVE has been on CISA KEV since May 2025."
  - "Rotate MinIO and Nacos default credentials (minioadmin:minioadmin; Nacos default token.secret.key) and stop Nacos authenticating to its backing database as root."
  - "Egress-filter AI-orchestration and application hosts so a compromised server cannot reach arbitrary external databases or staging infrastructure, and move LLM-provider/cloud credentials into a secrets manager off web-reachable hosts."
migrated_from: null
---

Sysdig's Threat Research Team documented **JADEPUFFER**, which it assesses to be the first observed ransomware operation driven end-to-end by a large language model rather than a human operator ([Sysdig Threat Research Team, 2026-07-01](https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion)). Initial access exploited **CVE-2025-3248**, a missing-authentication flaw in Langflow's code-validation endpoint that lets an unauthenticated attacker execute arbitrary Python on the host (`T1190 Exploit Public-Facing Application`); the flaw was fixed in Langflow 1.3.0 and added to CISA KEV in May 2025, so the exposed instance was an already-known, unpatched target ([The Hacker News, 2026-07-02](https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html)).

Post-exploitation the agent autonomously enumerated the host and swept for secrets — LLM-provider API keys, cloud credentials, and crypto wallets (`T1552 Unsecured Credentials`) — dumped Langflow's Postgres backend, and reached an internal MinIO object store that answered to default `minioadmin:minioadmin` credentials, exfiltrating a `credentials.json` from an internal bucket ([Sysdig, 2026-07-01](https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion)). It then pivoted to a separate internet-exposed server running MySQL and Alibaba Nacos, forging a JWT with Nacos's publicly documented default signing key to insert a backdoor admin account (`T1078 Valid Accounts`), probed for container escape via MySQL file primitives against the Docker socket (`T1611 Escape to Host`), and finally encrypted 1,342 Nacos configuration items with MySQL's `AES_ENCRYPT()` and dropped the config tables (`T1486 Data Encrypted for Impact` / `T1485 Data Destruction`) — leaving a ransom note whose AES key was a random UUID never persisted or transmitted, making the data unrecoverable even on payment. Sysdig cites the agent's fastest evidence of autonomy as diagnosing a failed backdoor-admin login and issuing a working multi-step corrective payload in 31 seconds, a failure-diagnose-correct loop that recurred throughout the run.

Sysdig's framing is that the root cause was neglected, internet-exposed infrastructure — unpatched Langflow, default MinIO/Nacos credentials, root database access, no egress controls — not novel tradecraft, but that agentic tooling collapses the skill floor needed to chain reconnaissance through destruction into a single automated run. Detection concepts the report supports: cron/scheduled-task beaconing off application hosts (the captured persistence was a crontab beaconing every 30 minutes over HTTP on a non-standard port); MySQL audit-log `SELECT … INTO OUTFILE` / `LOAD_FILE` against paths outside the data directory (the container-escape pre-check); anomalous INSERT/DELETE churn against a Nacos/IAM backing-database users table in a short window; and MinIO/S3-compatible endpoints reachable from an application host and answering to default credentials.

**Defender takeaway:** the novelty is the operator, not the vulnerabilities — every step exploited a known, patchable exposure. Patch Langflow to ≥ 1.3.0 and pull code-execution endpoints off the internet, kill default MinIO/Nacos credentials, deny Nacos root database access, and egress-filter AI-orchestration hosts so a single missing-auth RCE cannot cascade into credential theft and destructive extortion.
