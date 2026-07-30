---
schema: 1
kind: vulnerability
horizon: operational
title: "HCSEC-2026-23 — HashiCorp Terraform MCP Server leaks its own bearer token to an attacker-supplied address, and its credential cache crosses sessions and tenants (CVE-2026-14869, CVE-2026-16496, CVE-2026-16498)"
headline: "A query parameter the middleware forgot to validate makes the Terraform MCP server hand its bearer token to any unauthenticated caller"
summary: >
  HashiCorp disclosed three flaws in terraform-mcp-server on 2026-07-28, all in the streamable-HTTP
  transport that lets AI agents drive Terraform Cloud and Enterprise. CVE-2026-14869 (CVSS 8.6) is an
  unauthenticated server-side request forgery: the middleware validated a client-supplied Terraform address
  when it arrived as an HTTP header but not as a query parameter, so an unauthenticated caller can redirect
  the server's own configured bearer token to an address it controls. CVE-2026-16496 (CVSS 8.9) lets anyone
  holding another user's session identifier execute tool calls under that user's cached Terraform client in
  stateful mode, the default when running centrally, and CVE-2026-16498 (CVSS 10.0) silently reuses one
  tenant's credentials for another tenant's requests in stateless mode. All three affect 0.2.1 through
  1.0.0 and are fixed in 1.1.0; none is reported exploited.
discovered_at: "2026-07-30T05:10:00Z"
event_date: "2026-07-28"
run_id: 2026-07-30T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, auth-bypass, info-disclosure, cloud, identity, ai-abuse, patch-available]
regions: [global]
sectors: [public-sector, finance, telco, technology]
entities: []
techniques: [T1190, T1528, T1550.001]
affected_products: ["HashiCorp Terraform MCP Server"]
cves:
  - id: CVE-2026-14869
    cvss: "8.6"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "terraform-mcp-server 0.2.1 through 1.0.0 in streamable-HTTP transport mode; stdio-only deployments are not affected."
    fixed: "1.1.0"
  - id: CVE-2026-16496
    cvss: "8.9"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "terraform-mcp-server 0.2.1 through 1.0.0 in stateful streamable-HTTP mode, which HashiCorp states is the default when running the server centrally; stdio mode and stateless HTTP mode are not affected."
    fixed: "1.1.0"
  - id: CVE-2026-16498
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "terraform-mcp-server 0.2.1 through 1.0.0 in stateless HTTP mode, where the underlying MCP library assigns no unique session identifier; stdio mode and stateful mode are not affected."
    fixed: "1.1.0"
sources:
  - url: "https://discuss.hashicorp.com/t/hcsec-2026-23-multiple-vulnerabilities-impacting-hashicorp-terraform-mcp-server/77606"
    publisher: "HashiCorp"
    date: "2026-07-28"
    role: primary
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2572"
    publisher: "BSI CERT-Bund"
    date: "2026-07-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The middleware that processed incoming HTTP requests rejected a client-supplied Terraform address when it was provided as an HTTP header, but did not apply the same check when the same value was supplied as an HTTP query parameter."
    publisher: "HashiCorp"
  - quote: "This issue affected only deployments using stateful streamable-HTTP mode, which is the default when running the server centrally; stdio mode and stateless HTTP mode were not affected."
    publisher: "HashiCorp"
  - quote: "Operators who cannot upgrade immediately should restrict network access to the streamable-HTTP listener to trusted users only and treat MCP session IDs as sensitive values."
    publisher: "HashiCorp"
verification: multi-source
sourcing_note: >
  HashiCorp's own bulletin carries no CVSS scores. Each score in this entry's CVE records was transcribed
  this run from that CVE's individual vulnerability-database record — the record that owns it, never a
  roundup — and those per-CVE pages are not cited as sources because they are derived data sheets under this
  pipeline's sourcing policy; the scores therefore appear in the structured CVE metadata rather than as
  body claims. The three flaws apply to different transport modes and are recorded per record accordingly
  rather than presented as uniformly affecting every deployment. The affected range is contradicted between
  two HashiCorp documents — the bulletin says 0.2.1 through 1.0.0 and the vendor's own per-CVE records say
  0.3.0 to below 1.1.0. Both positions are stated in the body and neither is silently preferred; the CVE
  records here keep the bulletin's wider lower bound so the entry does not under-scope an operator on 0.2.x.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Upgrade terraform-mcp-server to 1.1.0 wherever it runs over streamable-HTTP, and rotate the Terraform bearer token configured on any instance that was network-reachable: the SSRF needs no authentication and its whole purpose is to send that token to an address the caller chooses, so an exposed instance should be treated as having disclosed it."
migrated_from: null
---

The Terraform MCP server is the component that lets an AI agent or LLM tooling drive Terraform Cloud and Enterprise operations, which means it holds a Terraform bearer token and acts on that token's authority. HashiCorp disclosed three flaws in it on 2026-07-28, all confined to its streamable-HTTP transport, and BSI CERT-Bund surfaced the bulletin the following day ([BSI CERT-Bund, 2026-07-29](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2572)).

The first is a validation gap of the kind that reads as an oversight and behaves as a credential-exfiltration primitive. HashiCorp describes it precisely: "the middleware that processed incoming HTTP requests rejected a client-supplied Terraform address when it was provided as an HTTP header, but did not apply the same check when the same value was supplied as an HTTP query parameter" ([HashiCorp, 2026-07-28](https://discuss.hashicorp.com/t/hcsec-2026-23-multiple-vulnerabilities-impacting-hashicorp-terraform-mcp-server/77606)). The check existed; it was applied on one input path and not the other. Because the server pairs that address with its own configured bearer token, an unauthenticated caller who supplies an address they control receives the token — CVE-2026-14869, the highest-impact of the three for an internet-reachable deployment because it needs no credentials at all. There is no exploitation chain to build and no privilege to acquire first: the request is the attack, and what leaves is a credential that authorises infrastructure changes.

The second and third are both failures of the per-session credential cache, and which one applies depends on how the server is run. In stateful mode, the cache is keyed on session identifier without binding that session to the requesting client's own token, so a caller who obtains someone else's session identifier executes tool calls under the victim's cached Terraform client — CVE-2026-16496. HashiCorp notes the deployment shape that matters here: "this issue affected only deployments using stateful streamable-HTTP mode, which is the default when running the server centrally; stdio mode and stateless HTTP mode were not affected" ([HashiCorp, 2026-07-28](https://discuss.hashicorp.com/t/hcsec-2026-23-multiple-vulnerabilities-impacting-hashicorp-terraform-mcp-server/77606)). The default for a shared deployment is the vulnerable one, which is the relevant fact for anyone assessing exposure.

In stateless mode the same cache fails harder, and this is the most severely scored of the three. The underlying MCP library assigns no unique session identifier at all in that mode, so the cache cannot separate one caller's credentials from another's and sequential requests from different tenants silently reuse each other's Terraform client (CVE-2026-16498). No attacker is strictly required for the effect to occur — it is a server-side isolation failure that manifests between ordinary tenants, which makes it a correctness problem as much as a security one, and means a multi-tenant stateless deployment may already have crossed credentials without anyone doing anything hostile.

All three are fixed in 1.1.0. HashiCorp credits CVE-2026-16496 to Juan Pablo Martinez Kuhn of Coinspect and states that CVE-2026-14869 and CVE-2026-16498 "were identified by an internal team" ([HashiCorp, 2026-07-28](https://discuss.hashicorp.com/t/hcsec-2026-23-multiple-vulnerabilities-impacting-hashicorp-terraform-mcp-server/77606)). None is reported exploited. One discrepancy is worth carrying rather than resolving: HashiCorp's bulletin gives the affected range as 0.2.1 up to and including 1.0.0, while HashiCorp's own CVE records for all three flaws give it as 0.3.0 up to below 1.1.0. Same vendor, two lower bounds — an operator running a 0.2.x build gets a different answer depending on which HashiCorp document they consult, so treat 0.2.x as in scope until the vendor reconciles them. Where an upgrade cannot happen immediately, HashiCorp's interim guidance is to "restrict network access to the streamable-HTTP listener to trusted users only and treat MCP session IDs as sensitive values" ([HashiCorp, 2026-07-28](https://discuss.hashicorp.com/t/hcsec-2026-23-multiple-vulnerabilities-impacting-hashicorp-terraform-mcp-server/77606)) — the second half of that is the part teams tend to miss, since a session identifier that grants use of a cached credential is a bearer secret whether or not it is documented as one.

There is a pattern here worth carrying beyond this product. The vulnerable primitive in all three is a credential cache keyed on an identifier the client supplies or that the framework never guarantees to be unique, sitting behind a listener that accepts requests from anywhere. Any MCP server that holds a long-lived platform credential on behalf of agents has the same shape available to it, so the useful generalisation for a defender is to ask, of every such deployment, what the cache is keyed on and whether that key is attacker-influenceable.

Detection has two surfaces, both in logs teams usually already have. Outbound request telemetry from the MCP server host is the SSRF anchor: requests to Terraform-API-shaped destinations that are not the configured Terraform address, especially where the destination varies per inbound request rather than staying constant. Application or API-gateway access logs are the cache-abuse anchor: the same MCP session identifier appearing across distinct source addresses or distinct authenticated identities, which has no legitimate explanation in a per-user session model. Hardening is the upgrade plus listener reachability, and for stateless multi-tenant deployments, treating any period before 1.1.0 as a window in which tenant credential separation was not actually enforced.
