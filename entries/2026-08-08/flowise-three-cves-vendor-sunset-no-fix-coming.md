---
schema: 1
kind: vulnerability
horizon: operational
title: "Flowise ships three new CVEs into a sunset — an unauthenticated auth bypass that defeats an earlier fix, and cross-workspace credential access, with no vendor left to patch them"
headline: "Three CVEs land on a self-hosted AI-agent builder days after its company announced it is winding down"
summary: >
  VulnCheck assigned three CVEs against Flowise ≤3.1.4 on 2026-08-06, all referencing the vendor's own sunset
  announcement as an advisory link. CVE-2026-70636 (CVSS 8.7) lets an unauthenticated caller reach the OAuth2
  credential-refresh endpoint by appending a trailing identifier that defeats prefix-based whitelist matching
  in the auth middleware — itself a bypass of the earlier fix for CVE-2026-41273. CVE-2026-67622 (8.5) lets
  an authenticated user read another workspace's credentials by supplying an arbitrary credential UUID, and
  CVE-2026-67621 (7.2) lets a view-only member drive document-store ingestion. BSI marks its advisory
  unpatched; with the company winding down, self-hosted operators own the compensating controls.
discovered_at: "2026-08-08T05:03:00Z"
event_date: "2026-08-06"
run_id: 2026-08-08T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, auth-bypass, info-disclosure, no-patch, ai-abuse, cloud]
regions: [global]
sectors: [technology, public-sector, finance]
entities: []
techniques: [T1190, T1528]
affected_products: ["FlowiseAI Flowise"]
cves:
  - id: CVE-2026-70636
    cvss: "8.7"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "Flowise through 3.1.4"
    fixed: "no fixed release published; BSI records the advisory as unpatched"
  - id: CVE-2026-67622
    cvss: "8.5"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: post-auth
    status: [no-patch]
    affected: "Flowise through 3.1.4"
    fixed: "no fixed release published; BSI records the advisory as unpatched"
  - id: CVE-2026-67621
    cvss: "7.2"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [no-patch]
    affected: "Flowise through 3.1.4"
    fixed: "no fixed release published; BSI records the advisory as unpatched"
sources:
  - url: "https://www.vulncheck.com/advisories/flowise-authentication-bypass-via-oauth2-credential-refresh-endpoint"
    publisher: "VulnCheck (CNA)"
    date: "2026-08-07"
    role: primary
  - url: "https://www.vulncheck.com/advisories/flowise-idor-in-openai-assistants-integration"
    publisher: "VulnCheck (CNA)"
    date: "2026-08-07"
    role: primary
  - url: "https://www.vulncheck.com/advisories/flowise-missing-authorization-on-document-store-mutation-endpoints"
    publisher: "VulnCheck (CNA)"
    date: "2026-08-07"
    role: primary
  - url: "https://flowiseai.com/sunset"
    publisher: "FlowiseAI"
    date: "2026-08-06"
    role: corroborating
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2703"
    publisher: "BSI CERT-Bund"
    date: "2026-08-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Flowise through 3.1.4 contains an authentication bypass vulnerability that allows unauthenticated attackers to access the OAuth2 credential refresh endpoint by exploiting prefix-based whitelist matching in the authentication middleware defined in packages/server/src/utils/constants.ts."
    publisher: "VulnCheck (CNA)"
  - quote: "This is a bypass of CVE-2026-41273."
    publisher: "VulnCheck (CNA)"
  - quote: "Ein Angreifer kann mehrere Schwachstellen in Flowise ausnutzen, um Sicherheitsvorkehrungen zu umgehen, Informationen offenzulegen und Daten zu manipulieren."
    publisher: "BSI CERT-Bund"
verification: multi-source
sourcing_note: "Scores and CWE classes are transcribed from the assigning CNA's own per-CVE advisory records (VulnCheck), cross-checked against the CVE records mirrored on OSV; an earlier summary in this run carried CVE-2026-67622 as CVSS 9.9, which the CNA record contradicts at 8.5, and the authority governs. BSI publishes a single advisory-level score of 7.7 and no per-CVE breakdown."
confidence: high
update_of: null
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
migrated_from: null
---

Flowise, the open-source visual builder for LLM and AI-agent workflows, picked up three CVEs on 2026-08-06 — and all three CVE records list the vendor's own sunset announcement ([FlowiseAI](https://flowiseai.com/sunset)) among their advisory references, which is the detail that turns a routine batch into an architecture decision.

The one that matters most needs no account. Per the assigning CNA, "Flowise through 3.1.4 contains an authentication bypass vulnerability that allows unauthenticated attackers to access the OAuth2 credential refresh endpoint by exploiting prefix-based whitelist matching in the authentication middleware defined in `packages/server/src/utils/constants.ts`" — a POST to the OAuth2 credential-refresh route with a trailing credential identifier appended slips past a check that only compares path prefixes, triggering unauthorised OAuth token rotation against credentials belonging to any workspace and potentially breaking dependent integrations ([VulnCheck, 2026-08-07](https://www.vulncheck.com/advisories/flowise-authentication-bypass-via-oauth2-credential-refresh-endpoint)). CVE-2026-70636 is scored CVSS 4.0 8.7 with integrity-only impact (`VC:N/VI:H/VA:N`) and, notably, "This is a bypass of CVE-2026-41273" — the same route has been fixed once already and the fix was incomplete ([VulnCheck, 2026-08-07](https://www.vulncheck.com/advisories/flowise-authentication-bypass-via-oauth2-credential-refresh-endpoint)).

The other two need an account but cross a tenancy boundary. CVE-2026-67622 (CWE-639, CVSS 4.0 8.5) is an insecure direct object reference in the OpenAI Assistants integration: an authenticated attacker supplies an arbitrary credential UUID to Assistants endpoints, the credential lookup performs no workspace-ownership check, and the attacker can enumerate cross-workspace assistant metadata, retrieve file and vector-store listings, and upload files into a victim workspace ([VulnCheck, 2026-08-07](https://www.vulncheck.com/advisories/flowise-idor-in-openai-assistants-integration)). CVE-2026-67621 (CWE-862, CVSS 4.0 7.2) lets a member holding only view-level permissions call the document-store upsert and refresh routes directly to trigger ingestion, refresh vector-database contents, consume embedding API credits and modify knowledge bases that downstream chatflows depend on ([VulnCheck, 2026-08-07](https://www.vulncheck.com/advisories/flowise-missing-authorization-on-document-store-mutation-endpoints)). Germany's BSI CERT-Bund carried all three on 2026-08-06 with the summary that an attacker can exploit multiple Flowise vulnerabilities to bypass security measures, disclose information and manipulate data, marking the advisory unpatched with no fixed release listed ([BSI CERT-Bund, 2026-08-06](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2703)).

No party reports exploitation of any of the three. What makes this more than a routine batch is that the usual next step does not exist: with the company winding down commercial operations, an operator waiting for a fixed release is waiting for something nobody has committed to ship, and the code remaining available for community forks is not the same thing as a maintained security response. Self-hosted AI-agent orchestration platforms have been a recurring source of pre-authentication paths — this pipeline has covered three separate confirmed-exploited Langflow flaws since mid-July — and Flowise now belongs to the subset of that class where the only remaining controls are ones the operator builds.

Detection concept: for CVE-2026-70636 the network-visible shape is an unauthenticated POST to an OAuth2 credential-refresh path carrying an extra trailing path segment beyond the route the allow-list was written for, with the resulting token rotation appearing in the OAuth provider's audit log as a refresh nobody initiated. For the two authenticated flaws, the tell is a session enumerating credential UUIDs or Assistants endpoints outside its own workspace, and a view-only account issuing document-store upsert or refresh calls at all. Hardening, in the absence of a patch: terminate the credential-refresh route at a reverse proxy that enforces authentication independently of the application, scope each workspace's provider credentials so a cross-workspace read yields keys that are separately revocable, and treat any internet-exposed Flowise instance as a candidate for removal from the perimeter rather than for patching.
