---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, NetScaler ADC and Gateway: the PHP2Shell flaws reach the management GUI on the NSIP, management-enabled SNIPs and the cluster IP of every supported version; fixed in 14.1-73.49, 13.1-64.32 and the FIPS and NDcPP builds"
headline: "NetScaler's PHP2Shell fix is out: 14.1-73.49, 13.1-64.32 and FIPS builds; restrict management access until installed"
summary: >
  NetScaler Product Security says the two PHP flaws CVE-2026-109618 and CVE-2026-109619 affect the NetScaler Management Portal,
  reached through the NSIP GUI, any SNIP that permits management access and the cluster IP GUI, on all supported software
  versions; NetScaler Console and SVM are not affected. Citrix's bulletin now names the fixed builds, 14.1-73.49, 13.1-64.32,
  14.1-FIPS 14.1-73.49 FIPS and 13.1-FIPS and 13.1-NDcPP 13.1.37.286 and later, and tells customers to immediately restrict management
  access to trusted networks; no source reports an attack on NetScaler, although CISA added both PHP flaws to its
  Known Exploited Vulnerabilities catalog on 2026-10-26.
discovered_at: "2026-10-23T03:38:00Z"
updated_at: "2026-10-28T03:37:38Z"
event_date: "2026-10-21"
run_id: 2026-10-23T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, cisa-kev, patch-available]
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
    status: [cisa-kev, patch-available]
    affected: "NetScaler management interfaces (NSIP GUI, management-enabled SNIP, cluster IP GUI) on all supported software versions"
    fixed: "ADC and Gateway 14.1-73.49 and later, 13.1-64.32 and later of 13.1; ADC 14.1-FIPS 14.1-73.49 FIPS and later; ADC 13.1-FIPS and 13.1-NDcPP 13.1.37.286 and later"
  - id: CVE-2026-109619
    cvss: "9.2 (CVSS 4.0, as stated by Citrix for the PHP flaw)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available]
    affected: "NetScaler management interfaces (NSIP GUI, management-enabled SNIP, cluster IP GUI) on all supported software versions"
    fixed: "ADC and Gateway 14.1-73.49 and later, 13.1-64.32 and later of 13.1; ADC 14.1-FIPS 14.1-73.49 FIPS and later; ADC 13.1-FIPS and 13.1-NDcPP 13.1.37.286 and later"
sources:
  - url: "https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/"
    publisher: "NetScaler Product Security (Citrix Tech Zone)"
    date: "2026-10-21"
    role: primary
  - url: "https://support.citrix.com/external/article/CTX697263"
    publisher: "Citrix security bulletin CTX697263"
    date: "2026-10-22"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog (version 2026.10.26)"
    date: "2026-10-26"
    role: corroborating
  - url: "https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1394/"
    publisher: "CERT-FR"
    date: "2026-10-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Cloud Software Group strongly urges customers of NetScaler ADC and NetScaler Gateway to install the following updated versions as soon as possible"
    publisher: "Citrix security bulletin CTX697263"
    source_url: "https://support.citrix.com/external/article/CTX697263"
  - quote: "All supported NetScaler software versions are impacted."
    publisher: "NetScaler Product Security (Citrix Tech Zone)"
    source_url: "https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/"
  - quote: "Citrix has released fixes to address these two PHP memory safety vulnerabilities for all supported NetScaler software versions."
    publisher: "NetScaler Product Security (Citrix Tech Zone)"
    source_url: "https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/"
  - quote: "Customers should immediately restrict access to NetScaler management interfaces to trusted, limited networks."
    publisher: "NetScaler Product Security (Citrix Tech Zone)"
    source_url: "https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/"
  - quote: "Citrix NetScaler ADC and Citrix NetScaler Gateway 14.1-73.49 and later releases"
    publisher: "Citrix security bulletin CTX697263"
    source_url: "https://support.citrix.com/external/article/CTX697263"
  - quote: "NetScaler ADC versions 13.1.x earlier than 13.1-64.32"
    original: "NetScaler ADC versions 13.1.x antérieures à 13.1-64.32"
    publisher: "CERT-FR"
    source_url: "https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1394/"
verification: single-source
sourcing_note: >
  NetScaler Product Security's post is the first-party source for the product impact and the mitigation, and Citrix's bulletin CTX697263
  (revised 2026-10-27) for the fixed builds, which CERT-FR's notice restates; the two flaws themselves are in the PHP runtime. Neither Citrix page carries a statement about exploitation of NetScaler. The listing of
  both PHP flaws in CISA's Known Exploited Vulnerabilities catalog comes from the catalog itself.
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
  - "Install NetScaler ADC and Gateway 14.1-73.49, 13.1-64.32, 14.1-FIPS 14.1-73.49 FIPS or 13.1-FIPS and 13.1-NDcPP 13.1.37.286 (or later) on every appliance whose NSIP, a management-enabled SNIP or the cluster IP answers on its GUI or API, internet-reachable ones first; until each has its build, restrict GUI and API access on those addresses to trusted administrative hosts with ACLs, keeping NetScaler Console access working."
updates:
  - at: "2026-10-25T13:43:27Z"
    run_id: 2026-10-25T1308Z-audit
    type: improvement
    internal: true
    summary: >
      NetScaler Product Security published the Tech Zone post on 2026-10-21 (22:23 CEST) and last updated
      it on 2026-10-22; the source date, its inline labels and event_date now give the publication date.
    fields: [sources, event_date, body]
  - at: "2026-10-27T03:41:15Z"
    run_id: 2026-10-27T0256Z-intel
    type: update
    summary: >
      CISA added both PHP flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26; no source
      reports an attack on NetScaler, and Citrix's bulletin still names no fixed build, so restricting
      management access remains the control.
    fields: [cves, evidence, headline, sources, sourcing_note, summary, tags]
  - at: "2026-10-28T03:37:38Z"
    run_id: 2026-10-28T0256Z-intel
    type: update
    summary: >
      Citrix revised bulletin CTX697263 on 2026-10-27 to name the fixed builds (14.1-73.49, 13.1-64.32,
      the 14.1-FIPS and the 13.1-FIPS and NDcPP builds), which CERT-FR restates; no source reports an
      attack on NetScaler.
    fields: [title, headline, summary, tags, cves, sources, evidence, sourcing_note, actions, body]
migrated_from: null
---

NetScaler Product Security says NetScaler is affected by the two PHP memory-safety flaws CVE-2026-109618 and CVE-2026-109619 because the NetScaler Management Portal uses PHP and that all supported software versions are affected; the post, last updated on 2026-10-27, now says Citrix has released fixes for all supported versions ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)). Citrix describes both as critical flaws in PHP that could let an unauthenticated attacker execute code in the context of the affected PHP process, each rated 9.2 under CVSS 4.0: CVE-2026-109618 is memory corruption when PHP handles an out-of-memory condition during request processing, and CVE-2026-109619 is stale request state that persists after memory is released and is reused by a later request ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)). The affected surfaces are the NSIP GUI, any SNIP configured to permit management access and the cluster IP GUI in a cluster; NetScaler Console (service and on premises) and NetScaler SVM are not affected ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)).

Citrix's bulletin CTX697263, revised on 2026-10-27, now urges customers to install NetScaler ADC and Gateway 14.1-73.49 or later, 13.1-64.32 or later of 13.1, ADC 14.1-FIPS 14.1-73.49 FIPS or later, and ADC 13.1-FIPS and 13.1-NDcPP 13.1.37.286 or later, and lists NetScaler Console as not impacted ([Citrix, 2026-10-22](https://support.citrix.com/external/article/CTX697263)); CERT-FR's notice of 2026-10-27 gives the same first fixed builds ([CERT-FR, 2026-10-27](https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1394/)). Citrix tells customers to restrict GUI and API access on those addresses to trusted administrative hosts or narrowly scoped management networks, to keep management interfaces off the internet behind jump hosts or tight ACLs, and to review every address that permits GUI or API management and verify that it is not broadly reachable ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)).

**Exposure:** every NetScaler ADC and Gateway on a supported version whose NSIP, a management-enabled SNIP or the cluster IP answers on its GUI or API from a network that is not a trusted administrative one; a SNIP or VIP can also carry application traffic, so Citrix tells customers to scope ACLs to management protocols and ports ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)).

**Detection:** connections to the management GUI and API from addresses that are not the administrative hosts, which is also the test of whether the ACLs hold; Citrix's post publishes no detection guidance and does not say whether NetScaler has been attacked ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)).

**Defender takeaway:** install the fixed builds now, appliances whose management addresses are reachable from outside the administrative network first; the PHP project's own fixed releases do not help an appliance owner, because the fix ships in Citrix's package. Until a build is installed, apply the management ACLs and keep a recovery path such as console access in case a rule blocks administration ([NetScaler Product Security, 2026-10-21](https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)).

## Update — 2026-10-27T03:41:15Z

CISA added both PHP flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26, as flaws in PHP rather than as a NetScaler finding ([CISA KEV, 2026-10-26](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). No source reports an attack on NetScaler through them. Citrix's bulletin CTX697263, whose revision history ends on 2026-10-22, still lists NetScaler ADC and Gateway as impacted, points to the Tech Zone post for mitigation and names no fixed build ([Citrix, 2026-10-22](https://support.citrix.com/external/article/CTX697263)), so the management-interface restriction stays the control until Citrix lists a fixed build.

## Update — 2026-10-28T03:37:38Z

Citrix revised bulletin CTX697263 on 2026-10-27 to name fixed builds: NetScaler ADC and Gateway 14.1-73.49 and later, 13.1-64.32 and later of 13.1, ADC 14.1-FIPS 14.1-73.49 FIPS and later, and ADC 13.1-FIPS and 13.1-NDcPP 13.1.37.286 and later ([Citrix, 2026-10-22](https://support.citrix.com/external/article/CTX697263)). CERT-FR's notice of 2026-10-27 lists the same first fixed builds for ADC and Gateway ([CERT-FR, 2026-10-27](https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1394/)). Neither page says NetScaler has been attacked, and no source reports an attack on it.
