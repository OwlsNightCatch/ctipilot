---
schema: 1
kind: vulnerability
title: "Traefik 3.7.10 / 3.6.25 / 2.11.54 — a route identity built by joining names with hyphens lets one Kubernetes namespace silently take over another's traffic on a shared Gateway"
headline: "Traefik patches three tenant-isolation failures; the worst hijacks another namespace's routes invisibly"
summary: >
  Traefik published three advisories on 2026-08-03, fixed in 3.7.10, 3.6.25 and 2.11.54, all breaking
  tenant isolation in the shared-ingress pattern European public-sector Kubernetes platforms run. The
  most serious builds router identities by hyphen-joining namespace, name, Gateway, entry point and
  rule index — a construction that is not injective when object names contain hyphens — so two Routes
  in different namespaces can resolve to the same identity and the one loaded later silently overwrites
  the earlier. A second bypasses the allowCrossNamespace guard for TraefikService backends; a third is
  a BasicAuth cache-key collision. No CVE identifiers have been assigned.
discovered_at: "2026-08-05T04:12:23Z"
event_date: "2026-08-03"
run_id: 2026-08-05T0412Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, cloud, auth-bypass, patch-available, default-config]
regions: [global, europe]
sectors: [public-sector, finance, telco]
entities: []
techniques: [T1557, T1078]
affected_products: ["Traefik Proxy"]
cves: []
sources:
  - url: "https://github.com/traefik/traefik/security/advisories/GHSA-fgjj-px3w-67xx"
    publisher: "Traefik Labs"
    date: "2026-08-03"
    role: primary
  - url: "https://github.com/traefik/traefik/security/advisories/GHSA-62fc-8686-hfmq"
    publisher: "Traefik Labs"
    date: "2026-08-03"
    role: primary
  - url: "https://github.com/traefik/traefik/security/advisories/GHSA-6765-c87h-8mrf"
    publisher: "Traefik Labs"
    date: "2026-08-03"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0964/"
    publisher: "CERT-FR / ANSSI"
    date: "2026-08-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Two distinct Routes attached to the same Gateway with equivalent match rules can therefore produce the same identity, and the Route loaded later silently overwrites the earlier one"
    publisher: "Traefik Labs (GHSA-fgjj-px3w-67xx)"
  - quote: "For names that contain an `@` separator (that is, `@kubernetescrd` cross-namespace references) it applies only the `crossProviderNamespaces` allowlist check, and that check returns `true` by default because a `nil` allowlist means \"unrestricted\"."
    publisher: "Traefik Labs (GHSA-62fc-8686-hfmq)"
verification: multi-source
sourcing_note: "Traefik Labs' own GitHub Security Advisories are the primary for all three flaws; CERT-FR relayed them as CERTFR-2026-AVI-0964 on 2026-08-04. A national-CERT restatement of a vendor advisory is the same assessor with a second publisher rather than independent confirmation, so credibility is 2. No CVE identifiers had been assigned at the time of writing — track the GHSA identifiers."
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
  - "Upgrade Traefik to 3.7.10, 3.6.25 or 2.11.54 on any cluster where a Gateway or ingress is shared between namespaces that belong to different teams or agencies — the isolation the platform's tenancy model assumes is what is broken here."
migrated_from: null
---

Traefik Labs published three security advisories on 2026-08-03, fixed in v3.7.10, v3.6.25 and v2.11.54, and CERT-FR relayed them the following day as CERTFR-2026-AVI-0964 ([CERT-FR, 2026-08-04](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0964/)). None has a CVE identifier yet. All three break tenant isolation rather than confidentiality of the proxy itself, which makes them relevant to a specific and common deployment: the shared Kubernetes ingress, where several agencies or departments run namespaces behind one cluster gateway and the platform's security model rests on the assumption that a tenant cannot influence another tenant's routing.

**The most serious flaw is a name-collision, not a missing check.** In the Kubernetes Gateway API provider, Traefik constructs router and service identities by joining the route namespace, route name, Gateway identity, entry point and rule index with hyphens. Because Kubernetes object names may themselves contain hyphens, that construction is not injective — different inputs can produce the same string. Traefik Labs states the consequence directly: two distinct Routes attached to the same Gateway with equivalent match rules can produce the same identity, and the Route loaded later silently overwrites the earlier one ([Traefik Labs, 2026-08-03](https://github.com/traefik/traefik/security/advisories/GHSA-fgjj-px3w-67xx)). A tenant who controls the naming of their own Route objects can therefore take over traffic destined for another namespace. The word doing the work is *silently*: the victim tenant's own manifests are unchanged, so nothing in their view of the cluster indicates that their traffic is no longer arriving. It is rated CVSS 4.0 base 7.6 and affects v3.0.0–v3.6.24 and v3.7.0–v3.7.9.

The second flaw undermines the control an operator would reach for to prevent exactly this. In the Kubernetes CRD provider, the guard that rejects cross-namespace references was never applied to TraefikService backend references: for names containing an `@` separator, Traefik applies only the `crossProviderNamespaces` allowlist check, and that check returns `true` by default because a `nil` allowlist means unrestricted ([Traefik Labs, 2026-08-03](https://github.com/traefik/traefik/security/advisories/GHSA-62fc-8686-hfmq)). An operator who set `allowCrossNamespace: false` and considered the boundary enforced did not have it enforced for backend references. It is rated CVSS 4.0 base 4.8 and affects v2 up to 2.11.53 and v3 up to 3.6.24 and 3.7.9. The third, rated CVSS 4.0 base 2.1, is a BasicAuth deduplication-key collision: Traefik Labs describes the key as the delimiter-free concatenation of password and secret, so certain crafted inputs inherit another pair's verification result ([Traefik Labs, 2026-08-03](https://github.com/traefik/traefik/security/advisories/GHSA-6765-c87h-8mrf)); where a header field is configured to pass the authenticated identity to the backend, that lets a low-privilege user present a different identity.

Detection concepts, telemetry class first. Both Kubernetes flaws manifest in the control plane rather than in traffic, so the audit log is the surface: create and update events for HTTPRoute, GRPCRoute, TCPRoute, TLSRoute and TraefikService objects, correlated against Traefik's own configuration-reload records. The specific artefacts are a Route object whose name introduces an extra hyphen-delimited segment, and a router referencing a service with a cross-namespace suffix. On the data plane, the corroborating signal is a change in backend destination for an established host and path with no matching change in the owning namespace's manifests.

**Triage:** GitOps controllers create and mutate Route objects continuously and legitimately, so object churn is the baseline rather than the signal. The discriminators are whether the acting identity is the platform's reconciler service account or a tenant's own, and whether the resulting router crosses a namespace boundary at all.

**Defender takeaway:** upgrade, and treat the naming question as a platform-design control independent of the fix — where one Gateway serves multiple tenants, an admission policy that constrains tenant Route names removes the collision class rather than this instance of it. The wider pattern is worth naming, because it is the third variation this fortnight on the same theme: joining attacker-influenceable strings without a delimiter is not an identity function, and code that derives authorisation from the result is trusting the caller to be honest about who they are.
