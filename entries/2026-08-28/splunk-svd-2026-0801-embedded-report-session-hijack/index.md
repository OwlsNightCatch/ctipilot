---
schema: 1
kind: vulnerability
title: "Splunk Enterprise August 2026 hardening release (SVD-2026-0801): three unauthenticated CVSS 9.4 flaws let anyone holding an embedded-report token hijack the report owner's session, admins included"
headline: "Splunk patches 60 CVEs; the headline path turns a shared dashboard link into a session-hijack primitive against the SIEM itself"
summary: >
  Splunk's SVD-2026-0801 (2026-08-19) fixes 60 CVEs across Splunk Enterprise 10.4/10.2/
  10.0/9.4. Three unauthenticated CVSS 9.4 flaws (CVE-2026-76310/76311/76312) let anyone holding
  an embedded-report token, or who can read the HTML of a page embedding one, download the
  report's dispatch archive, recover session material, and act as the report's owner — including
  as an admin. Separately, CVE-2026-76253 (CVSS 8.8) lets a user holding only the schedule_search
  capability run arbitrary SPL commands with system-level privilege and read every credential in
  the credential store. No exploitation is reported.
discovered_at: "2026-08-28T05:25:00Z"
updated_at: null
event_date: "2026-08-19"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, auth-bypass, pre-auth, patch-available, identity]
regions: [global]
sectors: [public-sector, finance, telco, technology]
entities: []
techniques: [T1190, T1550.001]
affected_products: ["Splunk Enterprise", "Splunk Secure Gateway"]
cves:
  - id: CVE-2026-76310
    cvss: "9.4"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Splunk Enterprise 10.4.0–10.4.1, 10.2.0–10.2.5, 10.0.0–10.0.8, 9.4.0–9.4.13"
    fixed: "10.4.2, 10.2.6, 10.0.9, 9.4.14"
  - id: CVE-2026-76311
    cvss: "9.4"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Splunk Enterprise 10.4.0–10.4.1, 10.2.0–10.2.5, 10.0.0–10.0.8, 9.4.0–9.4.13"
    fixed: "10.4.2, 10.2.6, 10.0.9, 9.4.14"
  - id: CVE-2026-76312
    cvss: "9.4"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Splunk Enterprise 10.4.0–10.4.1, 10.2.0–10.2.5, 10.0.0–10.0.8, 9.4.0–9.4.13"
    fixed: "10.4.2, 10.2.6, 10.0.9, 9.4.14"
  - id: CVE-2026-76350
    cvss: "8.8"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Splunk Enterprise 10.4.0–10.4.1, 10.2.0–10.2.5, 10.0.0–10.0.8, 9.4.0–9.4.13"
    fixed: "10.4.2, 10.2.6, 10.0.9, 9.4.14"
  - id: CVE-2026-76351
    cvss: "8.8"
    epss: null
    type: ssrf
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Splunk Secure Gateway (Splunk Enterprise 10.4.0–10.4.1, 10.2.0–10.2.5, 10.0.0–10.0.8, 9.4.0–9.4.13)"
    fixed: "10.4.2, 10.2.6, 10.0.9, 9.4.14"
  - id: CVE-2026-76253
    cvss: "8.8"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Splunk Enterprise 10.4.0–10.4.1, 10.2.0–10.2.5, 10.0.0–10.0.8, 9.4.0–9.4.13"
    fixed: "10.4.2, 10.2.6, 10.0.9, 9.4.14"
sources:
  - url: "https://advisory.splunk.com/advisories/SVD-2026-0801"
    publisher: "Splunk (SVD-2026-0801)"
    date: "2026-08-19"
    role: primary
closed_sources: []
evidence:
  - quote: "an unauthenticated user who has an embedded report token could download the associated search job dispatch archive, recover session material, and use it to access all relevant data available to the report owner and affect system integrity, including by performing administrative actions when the owner holds the \"admin\" Splunk role"
    publisher: "Splunk (SVD-2026-0801)"
  - quote: "a user that holds a role with the schedule_search capability could configure Portable Document Format (PDF) attachments in the email alert action workflow. When the email alert action runs, it could execute arbitrary Search Processing Language (SPL) commands with system-level privileges"
    publisher: "Splunk (SVD-2026-0801)"
  - quote: "a user that holds a role with the schedule_search capability could run arbitrary Search Processing Language (SPL) commands with the highest level of system privilege and read every credential stored in the credential store, which can allow for disclosure and modification of all relevant data and affect system integrity and availability"
    publisher: "Splunk (SVD-2026-0801)"
verification: single-source
sourcing_note: >
  Same-day transcription of Splunk's own advisory (vendor-PSIRT primary), single-sourced with no
  independent researcher write-up yet published. CVE-2026-76253 (CVSS 8.8, CWE-269, Privilege
  Escalation through Scheduled Search Alert Action Configuration) is the CVE that reaches the full
  credential store via privileged SPL escalation, from a schedule_search-only role — distinct from
  CVE-2026-76350's system-level SPL execution via a scheduled PDF alert action, and both are
  recorded individually here on their own stated terms. CVE-2026-76260 (CVSS 6.5, a role missing
  the correct capability can read stored credentials via a REST endpoint) is a related but
  lower-severity item not separately recorded.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Patch Splunk Enterprise to 10.4.2 / 10.2.6 / 10.0.9 / 9.4.14 now, and in the interim set allowEmbedTokenAuth = false in server.conf on any instance where embedded reports are not actively used — the three CVSS 9.4 flaws are unauthenticated for anyone holding, or able to read the page HTML for, an embedded-report token, and the compromised session can carry admin privileges."
  - "Audit which reports and dashboards are currently embedded (via allowEmbedTokenAuth or a page exposing report HTML) and owned by an admin-role account — those are the highest-value targets for CVE-2026-76310/76311/76312 and should either be re-owned to a lower-privileged account or have embedding disabled first."
  - "Review every role holding only the schedule_search capability and, until patched, remove or restrict scheduled-search alert-action authoring for those roles — CVE-2026-76253 lets a schedule_search-only user run arbitrary SPL with system-level privilege and read every credential in the credential store, which is a materially larger blast radius than the role's intended scope."
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [sourcing_note]
migrated_from: null
---

Splunk's SVD-2026-0801, published 2026-08-19, fixes 60 CVEs across Splunk Enterprise 10.4.0–10.4.1 (→10.4.2), 10.2.0–10.2.5 (→10.2.6), 10.0.0–10.0.8 (→10.0.9) and 9.4.0–9.4.13 (→9.4.14). The headline is a trio of unauthenticated CVSS 9.4 flaws (CWE-284, Improper Access Control) in Splunk's embedded-report feature: CVE-2026-76310 (Embedded Report REST API Requests), CVE-2026-76311 (Embedded Report Dispatch Archives) and CVE-2026-76312 (Embedded Reports generally). Splunk's own description of the mechanism is precise about the impact: "an unauthenticated user who has an embedded report token could download the associated search job dispatch archive, recover session material, and use it to access all relevant data available to the report owner and affect system integrity, including by performing administrative actions when the owner holds the 'admin' Splunk role" ([Splunk, SVD-2026-0801, 2026-08-19](https://advisory.splunk.com/advisories/SVD-2026-0801)). CVE-2026-76312's variant needs no token at all — reading the HTML source of any page that embeds a Splunk report is enough. Splunk's stated mitigation is `allowEmbedTokenAuth = false` in `server.conf` where embedding is unused, or turning off Splunk Web entirely for the -76312 variant.

Because Splunk is itself the SIEM many organisations run their own detection on, a session-hijack path into it is a path into the detection estate — an attacker who recovers an admin-owned embedded report's session material can act with that report owner's privileges inside the platform responders rely on to see everything else. That elevates this above an ordinary product-patch cycle regardless of Splunk's own severity framing.

Three further high-severity items round out the batch. CVE-2026-76350 (CVSS 8.8, CWE-269) lets any user holding only the `schedule_search` capability configure a PDF-attachment email-alert action that Splunk's scheduler then renders under a system-level authentication context rather than the action owner's: "a user that holds a role with the schedule_search capability could configure Portable Document Format (PDF) attachments in the email alert action workflow. When the email alert action runs, it could execute arbitrary Search Processing Language (SPL) commands with system-level privileges" ([Splunk, SVD-2026-0801, 2026-08-19](https://advisory.splunk.com/advisories/SVD-2026-0801)) — a low-privileged, schedule-only role escalating to system-wide data exposure. CVE-2026-76253 (also CVSS 8.8, CWE-269) is the same privilege class reaching further: a `schedule_search`-only role can run arbitrary SPL commands with the highest level of system privilege through scheduled-search alert-action configuration, because the search scheduler does not properly restrict user-specific alert-action settings before running them — "a user that holds a role with the schedule_search capability could run arbitrary Search Processing Language (SPL) commands with the highest level of system privilege and read every credential stored in the credential store, which can allow for disclosure and modification of all relevant data and affect system integrity and availability" ([Splunk, SVD-2026-0801, 2026-08-19](https://advisory.splunk.com/advisories/SVD-2026-0801)). CVE-2026-76351 (CVSS 8.8) is an SSRF in the Secure Gateway Report Notification REST API reachable with only schedule-level privilege, minting a system-level session token with no password. Five further RCE-class CVEs (knowledge-bundle upload, Web Manager configuration XML evaluation, federated search) and a stored-credential-exposing SPL injection via the `geostats` command round out the release; none is reported exploited.

Detection concentrates on the two access paths Splunk itself names. For the embedded-report trio: audit which reports currently have embedding enabled and who owns them, and treat any dispatch-archive download request that does not originate from Splunk's own scheduler or an authenticated interactive session as suspect — legitimate embedded-report viewing never needs the underlying dispatch archive directly. **Triage:** a normal embedded-report view renders through the web tier and never touches the raw dispatch archive path; a request that goes straight for the archive, or that arrives with a token but no corresponding active browser session, is the discriminator. For CVE-2026-76350, review scheduled email-alert actions for PDF-attachment configuration owned by low-privileged accounts — the presence of that configuration on an account holding only `schedule_search` is itself the anomaly, since the feature's system-level execution context was not intended for that privilege level.
