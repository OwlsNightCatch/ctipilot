---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, NetScaler ADC and Gateway: the PHP2Shell flaws reach the management GUI on the NSIP, management-enabled SNIPs and the cluster IP of every supported version, with fixes planned for 2026-10-27"
headline: "NetScaler management GUI is affected by PHP2Shell on all supported versions; fixes 2026-10-27, restrict access now"
summary: >
  NetScaler Product Security says the two PHP flaws CVE-2026-109618 and CVE-2026-109619 affect the NetScaler Management Portal,
  reached through the NSIP GUI, any SNIP that permits management access and the cluster IP GUI, on all supported software
  versions; NetScaler Console and SVM are not affected. Citrix plans fixes for all supported versions on 2026-10-27 and tells
  customers to restrict management access to trusted networks now; its post does not say whether NetScaler has been attacked.
discovered_at: "2026-10-23T03:38:00Z"
updated_at: null
event_date: "2026-10-21"
run_id: 2026-10-23T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, no-patch]
regions: [global]
sectors: []
entities: ["product:citrix-netscaler", "product:php"]
techniques: [T1190]
affected_products: ["Citrix NetScaler ADC", "Citrix NetScaler Gateway", "PHP"]
cves:
  - id: CVE-2026-109618
    cvss: "9.2 (CVSS 4.0, as stated by Citrix for the PHP flaw)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [no-patch, mitigation-only]
    affected: "NetScaler management interfaces (NSIP GUI, management-enabled SNIP, cluster IP GUI) on all supported software versions"
    fixed: "not yet released; Citrix plans fixes for all supported versions on 2026-10-27"
  - id: CVE-2026-109619
    cvss: "9.2 (CVSS 4.0, as stated by Citrix for the PHP flaw)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [no-patch, mitigation-only]
    affected: "NetScaler management interfaces (NSIP GUI, management-enabled SNIP, cluster IP GUI) on all supported software versions"
    fixed: "not yet released; Citrix plans fixes for all supported versions on 2026-10-27"
sources:
  - url: "https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/"
    publisher: "NetScaler Product Security (Citrix Tech Zone)"
    date: "2026-10-21"
    role: primary
closed_sources: []
evidence:
  - quote: "All supported NetScaler software versions are impacted."
    publisher: "NetScaler Product Security (Citrix Tech Zone)"
    source_url: "https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/"
  - quote: "Citrix plans to release fixes to address these two PHP memory safety vulnerabilities for all supported NetScaler software versions on October 27, 2026."
    publisher: "NetScaler Product Security (Citrix Tech Zone)"
    source_url: "https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/"
  - quote: "Customers should immediately restrict access to NetScaler management interfaces to trusted, limited networks."
    publisher: "NetScaler Product Security (Citrix Tech Zone)"
    source_url: "https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/"
verification: single-source
sourcing_note: >
  NetScaler Product Security's post is the first-party source for the product impact, the mitigation and the fix date; the two
  flaws themselves are in the PHP runtime and are covered by the entries listed under references. Citrix's post carries no
  statement about exploitation of NetScaler, and no fix is listed in it as of 2026-10-22.
confidence: high
references: ["2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619", "2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release", "2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev", "2026-10-04/cve-2026-88779-citrix-netscaler-saml-overflow-exploited", "2026-10-09/cve-2026-107406-citrix-netscaler-saml-idp-overflow"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "On every NetScaler, restrict GUI and API access on the NSIP, every SNIP that permits management access and the cluster IP to trusted administrative hosts with ACLs now, keeping NetScaler Console access working, and install Citrix's PHP fix on all supported versions when it ships on 2026-10-27."
updates:
  - at: "2026-10-25T13:43:27Z"
    run_id: 2026-10-25T1308Z-audit
    type: improvement
    internal: true
    summary: >
      NetScaler Product Security published the Tech Zone post on 2026-10-21 (22:23 CEST) and last updated
      it on 2026-10-22; the source date, its inline labels and event_date now give the publication date.
    fields: [sources, event_date, body]
migrated_from: null
---

NetScaler Product Security says NetScaler is affected by the two PHP memory-safety flaws CVE-2026-109618 and CVE-2026-109619 because the NetScaler Management Portal uses PHP, that Citrix is working to upgrade the PHP package, and that all supported software versions are affected ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)). Citrix describes both as critical flaws in PHP that could let an unauthenticated attacker execute code in the context of the affected PHP process, each rated 9.2 under CVSS 4.0: CVE-2026-109618 is memory corruption when PHP handles an out-of-memory condition during request processing, and CVE-2026-109619 is stale request state that persists after memory is released and is reused by a later request ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)). The affected surfaces are the NSIP GUI, any SNIP configured to permit management access and the cluster IP GUI in a cluster; NetScaler Console (service and on premises) and NetScaler SVM are not affected ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)).

Citrix plans to release fixes for all supported versions on 2026-10-27 and, until then, tells customers to restrict GUI and API access on those addresses to trusted administrative hosts or narrowly scoped management networks, to keep management interfaces off the internet behind jump hosts or tight ACLs, and to review every address that permits GUI or API management and verify that it is not broadly reachable ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)). Its WAF signature v186 covers backend applications that run PHP, while signatures that protect the NetScaler management interfaces themselves were still in development ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)).

**Exposure:** every NetScaler ADC and Gateway on a supported version whose NSIP, a management-enabled SNIP or the cluster IP answers on its GUI or API from a network that is not a trusted administrative one; a SNIP or VIP can also carry application traffic, so Citrix tells customers to scope ACLs to management protocols and ports ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)).

**Detection:** connections to the management GUI and API from addresses that are not the administrative hosts, which is also the test of whether the ACLs hold; Citrix's post publishes no detection guidance and does not say whether NetScaler has been attacked ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)).

**Defender takeaway:** apply the management ACLs now and keep a recovery path such as console access in case a rule blocks administration, then install the fixed builds on 2026-10-27; the PHP project's own fixed releases do not help an appliance owner until Citrix ships its package, and no fix is listed in Citrix's post as of 2026-10-22 ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)).
