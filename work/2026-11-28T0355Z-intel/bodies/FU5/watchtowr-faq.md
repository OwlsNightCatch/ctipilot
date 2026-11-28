---
title: GeoServer CVE-2026-129245 FAQ
url: https://watchtowr.com/intelligence/geoserver-cve-2026-129245-faq/
hostname: watchtowr.com
description: "CVE-2026-129245 FAQ: affected GeoServer versions, fixes and the pre-auth RCE chain behind it. Exploited in the wild per CISA KEV."
sitename: watchTowr
date: "2026-11-25"
categories: ['Vulnerability FAQ']
tags: ['CVE-2026-120705', 'CVE-2026-129242', 'CVE-2026-129243', 'CVE-2026-129244', 'CVE-2026-129245', 'GeoServer', 'Multiple Vulnerabilities']
fingerprint: ad3ba599d80786a7
language: en
image: https://watchtowr.com/wp-content/uploads/wt-2026-og-default-1352x630-1.png
pagetype: article
filedate: "2026-11-28"
---
## What is CVE-2026-129245, CVE-2026-129242, CVE-2026-129243, CVE-2026-129244, and CVE-2026-120705?

The GeoServer predictable remember-me key vulnerability (CVE-2026-129245) affects GeoServer, an open-source server for sharing and editing geospatial data. GeoServer signed its remember-me cookies with a key stored in its data directory, which shipped with a default value. An attacker who can read that key, along with the administrator’s stored password digest, can forge a valid administrator cookie without cracking the password. GeoServer rates it CVSS v4.0 9.2.

Reading the key normally requires access to the server, but four related GeoServer vulnerabilities remove that barrier. An oversized stored query ID makes the server reveal its data directory path (CVE-2026-129244). Prefixing the service name, as in x/WFS, bypasses the admin-only rules for creating stored queries (CVE-2026-129243). Saved query text is then reparsed into XML that pulls in local files, exposing the key and password digest (CVE-2026-120705). Once signed in as administrator, a deserialization vulnerability in the JDBC user service (CVE-2026-129242) runs commands on the server.

| CVE | Description | CVSS | Exploited in the wild | 
|---|---|---|---|
| [CVE-2026-129245](https://nvd.nist.gov/vuln/detail/CVE-2026-129245) | Multiple Vulnerabilities in GeoServer | 9.2 Critical | Yes | 
| [CVE-2026-129242](https://nvd.nist.gov/vuln/detail/CVE-2026-129242) | Deserialization in the JDBC user and role services that lets an administrator achieve code execution, rated High. | Not yet scored | Not reported | 
| [CVE-2026-129243](https://nvd.nist.gov/vuln/detail/CVE-2026-129243) | Service security rules bypassed by prefixing the service name, for example x/WFS, rated High. | Not yet scored | Yes | 
| [CVE-2026-129244](https://nvd.nist.gov/vuln/detail/CVE-2026-129244) | A WFS stored query exception message that reveals the data directory path, rated Medium. | Not yet scored | Not reported | 
| [CVE-2026-120705](https://nvd.nist.gov/vuln/detail/CVE-2026-120705) | Unauthenticated XML injection through WFS GetFeatureById, rated High. | Not yet scored | Yes | 
| [CVE-2026-120701](https://nvd.nist.gov/vuln/detail/CVE-2026-120701) | Unauthenticated server-side request forgery via the WPS gs:DownloadMap process in the WPS Download extension, rated High. | Not yet scored | Not reported | 
| [CVE-2026-120706](https://nvd.nist.gov/vuln/detail/CVE-2026-120706) | Unauthenticated server-side request forgery and file read through inline VRT passed to native GDAL in the WPS extension, rated High. | Not yet scored | Not reported | 
| [CVE-2026-120704](https://nvd.nist.gov/vuln/detail/CVE-2026-120704) | Remote code execution by loading SQLite JDBC extensions in the JDBC security services, rated High. | Not yet scored | Not reported | 
| [CVE-2026-120710](https://nvd.nist.gov/vuln/detail/CVE-2026-120710) | Arbitrary file write through a GeoWebCache FileRasterFilter ZIP update, rated High. | Not yet scored | Not reported | 
| [CVE-2026-129293](https://nvd.nist.gov/vuln/detail/CVE-2026-129293) | Stored cross-site scripting through a style name shown in the style editor layer preview, rated High. | Not yet scored | Not reported | 
| [CVE-2026-120707](https://nvd.nist.gov/vuln/detail/CVE-2026-120707) | GeoFence source IP rules bypassed using the X-Forwarded-For header, rated High and limited to the GeoFence extension. | Not yet scored | Not reported | 
| [CVE-2026-120708](https://nvd.nist.gov/vuln/detail/CVE-2026-120708) | ACL plugin source IP rules bypassed using the X-Forwarded-For header, rated High. | Not yet scored | Not reported | 
| [CVE-2026-129294](https://nvd.nist.gov/vuln/detail/CVE-2026-129294) | Unauthenticated style management in the OGC API Styles community module, rated High. | Not yet scored | Not reported | 
| [CVE-2026-120703](https://nvd.nist.gov/vuln/detail/CVE-2026-120703) | The JWT Headers community module trusting the roles header without validating it, rated High. | Not yet scored | Not reported | 
| [CVE-2026-129240](https://nvd.nist.gov/vuln/detail/CVE-2026-129240) | Local file probing using a file:// schemaLocation during strict schema validation, rated Medium. | Not yet scored | Not reported | 
| [CVE-2026-120709](https://nvd.nist.gov/vuln/detail/CVE-2026-120709) | Unauthenticated server-side request forgery and file read via the legend icon URL in the printing extension, rated Medium. | Not yet scored | Not reported | 
| [CVE-2026-120702](https://nvd.nist.gov/vuln/detail/CVE-2026-120702) | CSW DirectDownload still being served for layers where the feature is disabled, rated Medium. | Not yet scored | Not reported | 

## Is CVE-2026-129245, CVE-2026-129242, CVE-2026-129243, CVE-2026-129244, and CVE-2026-120705 being exploited in the wild?

CVE-2026-129245, CVE-2026-129242, CVE-2026-129243, CVE-2026-129244, and CVE-2026-120705 is being exploited in the wild, as reported by watchTowr and CISA, which added CVE-2026-129243 to its [Known Exploited Vulnerabilities catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-129243) on November 27, 2026.

## How did CVE-2026-129245, CVE-2026-129242, CVE-2026-129243, CVE-2026-129244, and CVE-2026-120705 come to light?

The vulnerabilities were discovered by the researcher CryptoCat, who reported the full chain to the GeoServer team through a private GitHub security advisory on August 2, 2026. GeoServer shipped fixes in releases 3.0.2, 2.28.6 and 2.27.7, and published all five advisories on November 23, 2026, after GitHub assigned a CVE to each. Quikko and nteusink are also credited on the x/WFS bypass and XML injection advisories, and McCaulay Hudson, Principal Vulnerability Researcher at watchTowr was added as a reporter on the remember-me key advisory.

## How is watchTowr helping GeoServer customers?

- [Attacker Eye](https://watchtowr.com/platform/#attacker-eye), our global honeypot network, is monitoring for exploitation activity as it emerges.
- [Adversary Sight engine](https://watchtowr.com/platform/#adversary-sight) identified GeoServer instances across client environments and assessed exposure.
- [Rapid Reaction](https://watchtowr.com/use-cases/rapid-reaction/) identified exposure to this vulnerability across the watchTowr client base, giving teams the time they need to act.

## What is GeoServer?

GeoServer is an open source server for publishing, sharing and editing geospatial data using open standards such as WFS, WMS and WCS. Government agencies, utilities and mapping teams commonly expose it to the internet so applications and partners can query map layers, which puts it within direct reach of unauthenticated attackers.

## Which GeoServer versions are affected?

| Product | Affected Versions | Fixed Version | 
|---|---|---|
| GeoServer 3.0.x | >= 3.0.0, \<= 3.0.1 | 3.0.2 | 
| GeoServer 2.28.x | >= 2.28.0, \<= 2.28.5 | 2.28.6 | 
| GeoServer 2.27.x and earlier | \<= 2.27.6 | 2.27.7 | 

- The GeoServer WFS endpoint and REST API are reachable over the network.
- The stock admin account is enabled in the default user service.
- The full chain works on a default installation with no extensions or configuration changes.

Prioritize internet-facing GeoServer instances, starting with any that still run the stock admin account in the default user service, since that is the account the chain forges a session for.

## How do I fix CVE-2026-129245, CVE-2026-129242, CVE-2026-129243, CVE-2026-129244, and CVE-2026-120705?

Upgrade GeoServer to 3.0.2, 2.28.6 or 2.27.7, depending on the branch in use, since these releases fix all five vulnerabilities in the chain. Where upgrading is not immediate, GeoServer suggests blocking service values containing a slash at a proxy and removing rememberme from the web filter chain.

1. Identify every GeoServer instance and note its release branch and current version.
2. Upgrade to 3.0.2, 2.28.6 or 2.27.7, matching the branch in use.
3. Set the same GEOSERVER\_REMEMBERME\_KEY on every node in a cluster, since fixed releases generate a new random key at each start.
4. Block service parameter values that contain a slash at a reverse proxy if upgrading cannot happen straight away.
5. Remove rememberme from the web filter chain as a temporary measure until the upgrade is in place.

## How do I check GeoServer for compromise?

GeoServer’s advisories suggest checking the wfs/query and workspaces/\*/wfs/query folders in the data directory for stored queries that administrators did not create, since the chain saves a stored query to read local files. Unexpected JDBC user or role services, recently uploaded database files in the data directory, and administrator sessions created through remember-me cookies are also worth investigating.

## What other vulnerabilities does the same bulletin fix?

GeoServer’s November 2026 security update covers the four other vulnerabilities in the chain, CVE-2026-129244, CVE-2026-129243, CVE-2026-120705 and CVE-2026-129242, along with further fixes from the same releases. These include unauthenticated server-side request forgery in the WPS Download extension (CVE-2026-120701) and the printing extension (CVE-2026-120709), arbitrary file write through GeoWebCache (CVE-2026-120710), and source IP rule bypasses using the X-Forwarded-For header (CVE-2026-120707 and CVE-2026-120708).

## What types of threat actors typically exploit these vulnerabilities?

No attribution has been made public.
