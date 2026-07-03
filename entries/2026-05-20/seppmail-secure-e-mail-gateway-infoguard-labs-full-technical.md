---
schema: 1
kind: vulnerability
horizon: operational
title: "SEPPmail Secure E-Mail Gateway — InfoGuard Labs full technical write-up; new CVE-2026-2743 (CVSS 10.0 pre-auth path traversal in LFT)"
headline: "SEPPmail Secure E-Mail Gateway — InfoGuard Labs full technical write-up; new CVE-2026-2743 (CVSS 10.0 pre-auth path traversal in LFT)"
summary: "UPDATE (originally covered 2026-05-09 deep dive on CVE-2026-44128 cluster): InfoGuard Labs — the Baar-based Swiss security firm that performed the original SEPPmail review — published its full technical write-up on 2026-05-18."
discovered_at: "2026-05-20T05:00:12Z"
event_date: null
run_id: 2026-05-20-a0f7b07f
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - rce
  - pre-auth
  - patch-available
  - path-traversal
regions:
  - switzerland
  - dach
  - europe
sectors:
  - public-sector
  - healthcare
  - finance
entities: []
cves:
  - id: CVE-2026-2743
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
sources:
  - url: "https://labs.infoguard.ch/posts/seppmail_secure_e-mail_gateway_rce_vulnerabilities_cve-2026-2743_cve-2026-7864_cve-2026-44127_cve-2026-44128/"
    publisher: "InfoGuard Labs technical analysis, 2026-05-18"
    role: primary
  - url: "https://thehackernews.com/2026/05/seppmail-secure-e-mail-gateway.html"
    publisher: "The Hacker News, 2026-05-19"
    role: corroborating
  - url: "https://cybersecuritynews.com/seppmail-gateway-flaws/"
    publisher: "CybersecurityNews, 2026-05-19"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: 2026-05-09/cve-2026-44128-et-al-seppmail-secure-email-gateway-cvss-9-3
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "**Apply SEPPmail v15.0.4 to any DACH-region deployment still on an earlier build.** CVE-2026-2743 (CVSS 10.0, pre-auth path-traversal-to-RCE via LFT) is also addressed by v15.0.4 — but if you delayed updating on the assumption disabled LFT limited exposure, re-evaluate now (InfoGuard's scan finds the majority of customer instances have LFT enabled) ([InfoGuard Labs, 2026-05-18](https://labs.infoguard.ch/posts/seppmail_secure_e-mail_gateway_rce_vulnerabilities_cve-2026-2743_cve-2026-7864_cve-2026-44127_cve-2026-44128/))."
migrated_from: briefs/2026-05-20.md
---

**UPDATE (originally covered 2026-05-09 deep dive on CVE-2026-44128 cluster):** [InfoGuard Labs](https://labs.infoguard.ch/posts/seppmail_secure_e-mail_gateway_rce_vulnerabilities_cve-2026-2743_cve-2026-7864_cve-2026-44127_cve-2026-44128/) — the Baar-based Swiss security firm that performed the original SEPPmail review — published its full technical write-up on 2026-05-18. The principal new finding is **CVE-2026-2743 (CVSS 10.0)**: a pre-authenticated path traversal in SEPPmail's **Large File Transfer (LFT)** component (`/v1/file.app` endpoint, `handle_request` function) that passes a JSON-supplied filename through `WebMailMessage::store_attachments` without sanitisation. The attacker writes arbitrary files as the `nobody` user; because `nobody` has unusual write access to `/etc/syslog.conf`, an attacker can overwrite it with a piped Perl reverse-shell one-liner and trigger a `newsyslog` rotation (15-minute cron sending `SIGHUP` to syslogd) to obtain unauthenticated RCE.

CVE-2026-2743 only affects instances with the **LFT license** enabled (exposure is detectable: `/v1/file.app` returns 404 if LFT is not provisioned). InfoGuard's Censys-driven scan suggests the majority of customer instances do have LFT enabled. The 2026-05-09 deep dive covered CVE-2026-44128 / 44125 / 44126 / 44127 / 44129 / 7864, all patched in v15.0.4; **CVE-2026-2743 is also addressed by v15.0.4** but defenders that delayed the v15.0.4 update on the assumption their LFT-disabled posture limited exposure should re-evaluate: any host running an earlier build is now a pre-auth-RCE candidate independent of the GINA V2 path. InfoGuard notes: ["The chain allows for a complete takeover of the SEPPmail appliance. Attackers can read all mail traffic and persist indefinitely on the gateway. On these virtual appliances the Blue Teams have usually no visibility."](https://labs.infoguard.ch/posts/seppmail_secure_e-mail_gateway_rce_vulnerabilities_cve-2026-2743_cve-2026-7864_cve-2026-44127_cve-2026-44128/) Apply v15.0.4 to all Swiss / DACH SEPPmail appliances immediately if any remain on an earlier build; monitor `/v1/file.app` POST requests with `../` sequences in the JSON body; alert on unexpected Perl process trees spawned by `syslogd`.
