---
schema: 1
kind: vulnerability
title: "CVE-2026-133968, MONAI Label through 0.8.5: an unauthenticated path traversal in the datastore upload endpoints gives arbitrary file write and code execution, exploited since September 2026 (Amazon says Cairn AI agents found it as a zero-day against East Asian university servers); fixed in 0.8.6, authentication is off by default (CVSS 3.1 9.8)"
headline: "MONAI Label CVE-2026-133968 exploited since September: upgrade to 0.8.6; authentication is off by default"
summary: >
  The MONAI Label 0.8.6 security release of 2026-11-22 fixes CVE-2026-133968, a path traversal in the PUT /datastore/image and PUT /datastore/label endpoints of the medical-imaging annotation server that writes files anywhere the server process can write, reachable without credentials in the default configuration; the CVE record says it was exploited from September 2026. Amazon Threat Intelligence reports that a Chinese-nexus operator's Cairn AI agents found it as a zero-day, went from API mapping to arbitrary file write in about 11 minutes and later to a root shell on a university server.
discovered_at: "2026-11-22T04:42:00Z"
updated_at: null
event_date: "2026-11-20"
run_id: 2026-11-22T0355Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, zero-day, actively-exploited, pre-auth, rce, path-traversal, ai-abuse, patch-available]
regions: [global]
sectors: [education]
entities: ["product:monai-label", "tool:cairn-exploitation-engine"]
techniques: [T1595.002, T1190, T1059.006, T1546.018, T1110.003, T1090]
affected_products: ["MONAI Label"]
cves:
  - id: CVE-2026-133968
    cvss: "9.8"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "MONAI Label through 0.8.5; authentication is off by default, and with authentication on the ANNOTATOR role is enough"
    fixed: "0.8.6"
sources:
  - url: "https://github.com/Project-MONAI/MONAILabel/releases/tag/0.8.6"
    publisher: "Project MONAI (MONAI Label 0.8.6 release notes)"
    date: "2026-11-22"
    role: primary
  - url: "https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94"
    publisher: "Project MONAI (GitHub Security Advisory GHSA-qc22-rmgc-vg94)"
    date: "2026-11-18"
    role: primary
  - url: "https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/"
    publisher: "Amazon Threat Intelligence (AWS Security Blog)"
    date: "2026-11-20"
    role: primary
closed_sources: []
evidence:
  - quote: "This is a security release. All MONAI Label server deployments should upgrade."
    publisher: "Project MONAI"
    source_url: "https://github.com/Project-MONAI/MONAILabel/releases/tag/0.8.6"
  - quote: "At the time of discovery, this path traversal vulnerability in the medical imaging application did not correspond to any assigned security advisory and was unpatched."
    publisher: "Amazon Threat Intelligence"
    source_url: "https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/"
  - quote: "In about 11 minutes, the agents went from mapping the application’s API to arbitrarily writing files on the server."
    publisher: "Amazon Threat Intelligence"
    source_url: "https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/"
  - quote: "so in the default configuration any network client that can reach the server can exploit this."
    publisher: "Project MONAI"
    source_url: "https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94"
verification: multi-source
sourcing_note: >
  The CVSS 3.1 score of 9.8 is the CVE record's; Amazon's campaign dates support the exploitation since September 2026. Amazon does not name the product and links the project's advisory as the one released for the flaw it found; the advisory page still says the fix will be in the next release, which the 0.8.6 release notes of 2026-11-22 supersede. That the agents, not the operator, chose each step is Amazon's reading of the operator's exposed logs and has no second source.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every MONAI Label server to 0.8.6 (pip install -U monailabel==0.8.6, or the projectmonai/monailabel:0.8.6 image), because CVE-2026-133968 is exploited and every version through 0.8.5 is affected."
  - "On every MONAI Label 0.8.5 or older server that was reachable from an untrusted network, review it for unexpected file changes before it returns to service, starting with sitecustomize.py, authorized_keys and cron entries that the service account wrote and nobody deployed, because the upgrade does not evict an attacker who is already in."
updates:
  - at: "2026-11-22T14:43:20Z"
    run_id: 2026-11-22T1407Z-audit
    type: improvement
    internal: true
    summary: >
      The Detection line's image-parameter and dot-prefix detail comes from the project's security
      advisory, not the 0.8.6 release notes; the clause now cites the advisory beside the release notes.
    fields: [body]
migrated_from: null
---

MONAI Label 0.8.6, released on 2026-11-22 as a security release, fixes CVE-2026-133968, rated critical: `PUT /datastore/image` and `PUT /datastore/label` built the destination path from the image ID and label tag without confining it to the datastore, so a caller could write files anywhere the server process can write, in all versions up to and including 0.8.5 ([Project MONAI, 2026-11-22](https://github.com/Project-MONAI/MONAILabel/releases/tag/0.8.6)). The project's advisory adds that arbitrary file write can lead to remote code execution, for example through application code, `authorized_keys` or cron, that authentication is off by default and that with authentication on the ANNOTATOR role is enough ([Project MONAI, 2026-11-18](https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94)). The same release fixes a second path traversal in session upload: `PUT /session/?uncompress=true` extracted uploaded tar archives without checking member names, and session IDs were used as paths without validation, in all versions up to and including 0.8.5 ([Project MONAI, 2026-11-22](https://github.com/Project-MONAI/MONAILabel/releases/tag/0.8.6)).

Amazon Threat Intelligence found on 2026-09-10 a publicly reachable, unauthenticated instance of Cairn, an open-source autonomous AI penetration-testing framework, whose exposed history showed a roughly 48-hour campaign from 2026-09-08 against IP addresses of universities in East Asia outside mainland China ([Amazon Threat Intelligence, 2026-11-20](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/)). Against a medical-imaging AI application the agents mapped the API, found an upload endpoint with a filename parameter, tested it for path traversal and reached arbitrary file write in about 11 minutes; in a later session they wrote a Python reverse shell to `sitecustomize.py` and triggered a training endpoint, which started a new Python process that imported it and gave a root shell ([Amazon Threat Intelligence, 2026-11-20](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/)). The operator later gave the agents a proxy into a second university network that ran the same software, which Amazon infers it had reached through the same flaw, and Amazon assesses with moderate confidence that the actor is Chinese-nexus; the same agents ran 16 hours against a hardened Redis instance and tried more than 30,000 credential combinations against a GPU server without success ([Amazon Threat Intelligence, 2026-11-20](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/)).

**Exposure:** any MONAI Label server through 0.8.5 that untrusted clients can reach; authentication is off by default (`MONAI_LABEL_AUTH_ENABLE=False`), so any client that can connect can write files, and with authentication on the ANNOTATOR role is enough ([Project MONAI, 2026-11-22](https://github.com/Project-MONAI/MONAILabel/releases/tag/0.8.6); [Project MONAI, 2026-11-18](https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94)).

**Detection:** web or reverse-proxy access logs for PUT requests to the two datastore endpoints whose `image` parameter carries parent-directory sequences or a leading dot, which the fix neutralises or rejects, and for tar uploads to `PUT /session/` with `uncompress=true` ([Project MONAI, 2026-11-22](https://github.com/Project-MONAI/MONAILabel/releases/tag/0.8.6); [Project MONAI, 2026-11-18](https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94)); unexpected creation or change of `sitecustomize.py`, `authorized_keys` or cron entries by the service account; and a Python interpreter started by the service after a training-endpoint call that then opens an outbound connection ([Project MONAI, 2026-11-18](https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94); [Amazon Threat Intelligence, 2026-11-20](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/)).

**Defender takeaway:** upgrade to 0.8.6, which the project calls a security release for every deployment, and whatever the version keep the server off untrusted networks, turn authentication on with roles only for trusted users and run it as an unprivileged account that can write only to the datastore; on a 0.8.5 or older server that was reachable from an untrusted network, the project asks for a review for unexpected file changes before it returns to service ([Project MONAI, 2026-11-22](https://github.com/Project-MONAI/MONAILabel/releases/tag/0.8.6)). Amazon's own advice is to favour high-confidence detections that trigger automated response, because the agents ran for hours without a break ([Amazon Threat Intelligence, 2026-11-20](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/)).
