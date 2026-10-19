---
title: OAuth2 SSRF vulnerability in SAP Cloud SDK for Python
author: Thiagob
url: https://github.com/SAP/cloud-sdk-python/security/advisories/GHSA-4mv3-jxxm-9cx2
hostname: github.com
description: The SAP Cloud SDK for Python contains an OAuth2 SSRF vulnerability affecting multi-tenant BTP applications. An attacker who controls the `tenant_subdomain` parameter can redirect OAuth2 token reque...
sitename: GitHub
date: "2026-10-13"
categories: ['repository:1187276298']
fingerprint: "9c99649bbdd1ce05"
---
  
    The SAP Cloud SDK for Python contains an OAuth2 SSRF vulnerability affecting multi-tenant BTP applications. An attacker who controls the `tenant_subdomain` parameter can redirect OAuth2 token requests to an attacker-controlled server, causing client credentials to be exfiltrated.

#### PATCH DETAILS

Version `0.45.2` validates the `tenant_subdomain` value against RFC 1123 DNS label rules before substituting it into a token URL.

#### WORKAROUND

Consumer applications can mitigate the vulnerability by validating `tenant_subdomain` against a known allowlist of registered tenant subdomains before passing it to any SDK call.

The SAP Cloud SDK for Python contains an OAuth2 SSRF vulnerability affecting multi-tenant BTP applications. An attacker who controls the

`tenant_subdomain`parameter can redirect OAuth2 token requests to an attacker-controlled server, causing client credentials to be exfiltrated.
## PATCH DETAILS

Version

`0.45.2`validates the`tenant_subdomain`value against RFC 1123 DNS label rules before substituting it into a token URL.
## WORKAROUND

Consumer applications can mitigate the vulnerability by validating

`tenant_subdomain`against a known allowlist of registered tenant subdomains before passing it to any SDK call.
