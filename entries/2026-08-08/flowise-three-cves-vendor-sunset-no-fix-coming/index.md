---
schema: 1
kind: vulnerability
title: >
  Flowise ships three new CVEs into a sunset — an unauthenticated auth bypass that defeats an
  earlier fix, and cross-workspace credential access, with no vendor left to patch them
headline: >
  Three CVEs land on a self-hosted AI-agent builder days after its company announced it is winding
  down
summary: >
  VulnCheck assigned three CVEs against Flowise ≤3.1.4 on 2026-08-06, all referencing the vendor's
  own sunset announcement as an advisory link. CVE-2026-70636 (CVSS 8.7) lets an unauthenticated
  caller reach the OAuth2 credential-refresh endpoint by appending a trailing identifier that
  defeats prefix-based whitelist matching in the auth middleware — itself a bypass of the earlier
  fix for CVE-2026-41273. CVE-2026-67622 (8.5) lets an authenticated user read another workspace's
  credentials by supplying an arbitrary credential UUID, and CVE-2026-67621 (7.2) lets a view-only
  member drive document-store ingestion. BSI marks its advisory unpatched; with the company
  winding down, self-hosted operators own the compensating controls.
discovered_at: "2026-08-08T05:03:00Z"
updated_at: "2026-08-15T04:58:00Z"
event_date: 2026-08-06
run_id: 2026-08-08T0409Z-intel
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - auth-bypass
  - info-disclosure
  - no-patch
  - ai-abuse
  - cloud
  - rce
  - pre-auth
  - patch-available
regions:
  - global
sectors:
  - technology
  - public-sector
  - finance
entities: []
techniques:
  - T1190
  - T1528
affected_products:
  - FlowiseAI Flowise
  - Flowise
cves:
  - id: CVE-2026-70636
    cvss: "8.7"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - no-patch
    affected: Flowise through 3.1.4
    fixed: "no fixed release published; BSI records the advisory as unpatched"
  - id: CVE-2026-67622
    cvss: "8.5"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status:
      - no-patch
    affected: Flowise through 3.1.4
    fixed: "no fixed release published; BSI records the advisory as unpatched"
  - id: CVE-2026-67621
    cvss: "7.2"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status:
      - no-patch
    affected: Flowise through 3.1.4
    fixed: "no fixed release published; BSI records the advisory as unpatched"
  - id: CVE-2026-73487
    cvss: "9.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: "< 3.1.3"
    fixed: 3.1.3
sources:
  - url: "https://www.vulncheck.com/advisories/flowise-authentication-bypass-via-oauth2-credential-refresh-endpoint"
    publisher: VulnCheck (CNA)
    date: 2026-08-07
    role: primary
  - url: "https://www.vulncheck.com/advisories/flowise-idor-in-openai-assistants-integration"
    publisher: VulnCheck (CNA)
    date: 2026-08-07
    role: primary
  - url: "https://www.vulncheck.com/advisories/flowise-missing-authorization-on-document-store-mutation-endpoints"
    publisher: VulnCheck (CNA)
    date: 2026-08-07
    role: primary
  - url: "https://flowiseai.com/sunset"
    publisher: FlowiseAI
    date: 2026-08-06
    role: corroborating
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2703"
    publisher: BSI CERT-Bund
    date: 2026-08-06
    role: corroborating
  - url: "https://www.vulncheck.com/advisories/flowise-before-prompt-injection-rce-via-csv-agent"
    publisher: VulnCheck
    date: 2026-08-13
    role: primary
closed_sources: []
evidence:
  - quote: Flowise through 3.1.4 contains an authentication bypass vulnerability that allows unauthenticated attackers to access the OAuth2 credential refresh endpoint by exploiting prefix-based whitelist matching in the authentication middleware defined in packages/server/src/utils/constants.ts.
    publisher: VulnCheck (CNA)
  - quote: This is a bypass of CVE-2026-41273.
    publisher: VulnCheck (CNA)
  - quote: "Ein Angreifer kann mehrere Schwachstellen in Flowise ausnutzen, um Sicherheitsvorkehrungen zu umgehen, Informationen offenzulegen und Daten zu manipulieren."
    publisher: BSI CERT-Bund
  - quote: "Flowise before 3.1.3 contains a regex-based Python code validator bypass in CSV and Airtable Agent nodes that allows unauthenticated attackers to inject malicious code via prompt injection. Attackers can exploit unblocked pandas functions like pd.read_json() to exfiltrate datasets, perform SSRF against internal services, or achieve code execution through the unauthenticated prediction API."
    publisher: VulnCheck
verification: multi-source
sourcing_note: >
  Scores and CWE classes are transcribed from the assigning CNA's own per-CVE advisory records
  (VulnCheck), cross-checked against the CVE records mirrored on OSV; an earlier summary in this
  run carried CVE-2026-67622 as CVSS 9.9, which the CNA record contradicts at 8.5, and the
  authority governs. BSI publishes a single advisory-level score of 7.7 and no per-CVE breakdown.
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
  - "Inventory self-hosted Flowise instances at ≤3.1.4 and put the OAuth2 credential-refresh route behind network or proxy-level authentication now, since no fixed release is coming — the unauthenticated path is reachable by appending a trailing credential identifier to an otherwise allow-listed route prefix."
  - "Upgrade any self-hosted Flowise instance to 3.1.3 — the earlier batch's conclusion that no fix was coming does not hold for this CVE, and the exploitation path needs no credential."
updates:
  - at: "2026-08-15T04:58:00Z"
    run_id: 2026-08-15T0412Z-intel
    type: update
    summary: >
      VulnCheck assigned CVE-2026-73487 (CVSS 9.0) against Flowise before 3.1.3 on 2026-08-13, five
      days after this pipeline covered three Flowise CVEs that BSI marked unpatched with the vendor
      winding down. This one is a regex-based Python code-validator bypass in the CSV and Airtable
      Agent nodes reachable by prompt injection through the unauthenticated prediction API, and it
      does have a fixed release — so operators who concluded from the earlier batch that no fix was
      coming now have one to apply.
    fields:
      - actions
      - affected_products
      - cves
      - evidence
      - sources
      - tags
      - body
    merged_from: 2026-08-15/cve-2026-73487-flowise-prompt-injection-rce-fix-exists
migrated_from: null
---

Flowise, the open-source visual builder for LLM and AI-agent workflows, picked up three CVEs on 2026-08-06 — and all three CVE records list the vendor's own sunset announcement ([FlowiseAI](https://flowiseai.com/sunset)) among their advisory references, which is the detail that turns a routine batch into an architecture decision.

The one that matters most needs no account. Per the assigning CNA, "Flowise through 3.1.4 contains an authentication bypass vulnerability that allows unauthenticated attackers to access the OAuth2 credential refresh endpoint by exploiting prefix-based whitelist matching in the authentication middleware defined in `packages/server/src/utils/constants.ts`" — a POST to the OAuth2 credential-refresh route with a trailing credential identifier appended slips past a check that only compares path prefixes, triggering unauthorised OAuth token rotation against credentials belonging to any workspace and potentially breaking dependent integrations ([VulnCheck, 2026-08-07](https://www.vulncheck.com/advisories/flowise-authentication-bypass-via-oauth2-credential-refresh-endpoint)). CVE-2026-70636 is scored CVSS 4.0 8.7 with integrity-only impact (`VC:N/VI:H/VA:N`) and, notably, "This is a bypass of CVE-2026-41273" — the same route has been fixed once already and the fix was incomplete ([VulnCheck, 2026-08-07](https://www.vulncheck.com/advisories/flowise-authentication-bypass-via-oauth2-credential-refresh-endpoint)).

The other two need an account but cross a tenancy boundary. CVE-2026-67622 (CWE-639, CVSS 4.0 8.5) is an insecure direct object reference in the OpenAI Assistants integration: an authenticated attacker supplies an arbitrary credential UUID to Assistants endpoints, the credential lookup performs no workspace-ownership check, and the attacker can enumerate cross-workspace assistant metadata, retrieve file and vector-store listings, and upload files into a victim workspace ([VulnCheck, 2026-08-07](https://www.vulncheck.com/advisories/flowise-idor-in-openai-assistants-integration)). CVE-2026-67621 (CWE-862, CVSS 4.0 7.2) lets a member holding only view-level permissions call the document-store upsert and refresh routes directly to trigger ingestion, refresh vector-database contents, consume embedding API credits and modify knowledge bases that downstream chatflows depend on ([VulnCheck, 2026-08-07](https://www.vulncheck.com/advisories/flowise-missing-authorization-on-document-store-mutation-endpoints)). Germany's BSI CERT-Bund carried all three on 2026-08-06 with the summary that an attacker can exploit multiple Flowise vulnerabilities to bypass security measures, disclose information and manipulate data, marking the advisory unpatched with no fixed release listed ([BSI CERT-Bund, 2026-08-06](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2703)).

No party reports exploitation of any of the three. What makes this more than a routine batch is that the usual next step does not exist: with the company winding down commercial operations, an operator waiting for a fixed release is waiting for something nobody has committed to ship, and the code remaining available for community forks is not the same thing as a maintained security response. Self-hosted AI-agent orchestration platforms have been a recurring source of pre-authentication paths — this pipeline has covered three separate confirmed-exploited Langflow flaws since mid-July — and Flowise now belongs to the subset of that class where the only remaining controls are ones the operator builds.

Detection concept: for CVE-2026-70636 the network-visible shape is an unauthenticated POST to an OAuth2 credential-refresh path carrying an extra trailing path segment beyond the route the allow-list was written for, with the resulting token rotation appearing in the OAuth provider's audit log as a refresh nobody initiated. For the two authenticated flaws, the tell is a session enumerating credential UUIDs or Assistants endpoints outside its own workspace, and a view-only account issuing document-store upsert or refresh calls at all. Hardening, in the absence of a patch: terminate the credential-refresh route at a reverse proxy that enforces authentication independently of the application, scope each workspace's provider credentials so a cross-workspace read yields keys that are separately revocable, and treat any internet-exposed Flowise instance as a candidate for removal from the perimeter rather than for patching.

## Update — 2026-08-15T04:58:00Z

The earlier entry recorded three VulnCheck-assigned Flowise CVEs whose advisory links pointed at the vendor's own sunset announcement, with BSI marking its advisory unpatched and no vendor left to fix them — the operational conclusion being that self-hosted operators owned the compensating controls. A fourth CVE has now landed and it inverts that conclusion in one respect.

VulnCheck assigned CVE-2026-73487 on 2026-08-13 at CVSS 9.0, with the vector `CVSS:4.0/AV:N/AC:H/AT:N/PR:N/UI:N/VC:H/VI:L/VA:N/SC:H/SI:L/SA:N`. Flowise before 3.1.3 contains a regex-based Python code-validator bypass in the CSV and Airtable Agent nodes that lets unauthenticated attackers inject code via prompt injection, exploiting unblocked pandas functions such as `pd.read_json()` to exfiltrate datasets, perform server-side request forgery against internal services, or achieve code execution through the unauthenticated prediction API ([VulnCheck, 2026-08-13](https://www.vulncheck.com/advisories/flowise-before-prompt-injection-rce-via-csv-agent)). The delta that matters operationally is the last field of the record: there is a fixed release, 3.1.3.

Two things are worth separating. The defect class is a familiar one for this product line — a denylist implemented as a regular expression over generated Python, defeated by reaching a function the pattern does not name — and it is the same shape as the earlier auth-middleware bypass that defeated a prefix-based allowlist. The reachability is what makes it more than an application bug: the injection travels through the prediction API, which takes untrusted natural-language input by design and needs no authentication, so the attacker's input reaches the validator without any credential step in between. An agent node that turns a prompt into executed pandas code is doing exactly what it was built to do; the control that was supposed to bound it is the validator, and the validator is what broke.

The vendor's broader position has not changed — the earlier entry's reasoning about a sunset product still governs the medium-term decision — but the immediate action for anyone still running Flowise is now an upgrade rather than a compensating control. Detection concepts, telemetry class first: in application-access telemetry, unauthenticated requests to the prediction API whose payloads reference pandas entry points or file and URL-loading functions rather than the question-shaped input the flow expects; in egress telemetry from the host running Flowise, outbound requests to internal addresses or metadata endpoints originating from the Flowise process, which is the server-side-request-forgery half of the same primitive; in process-execution telemetry, any child process of the Flowise runtime.
