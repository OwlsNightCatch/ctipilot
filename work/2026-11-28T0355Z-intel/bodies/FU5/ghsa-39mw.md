---
title: Unauthenticated WFS GetFeatureById XML injection
author: Jodygarnett
url: https://github.com/geoserver/geoserver/security/advisories/GHSA-39mw-5chv-jh47
hostname: github.com
description: GeoServer exposes the built-in WFS 2.0 stored query `urn:ogc:def:query:OGC-WFS::GetFeatureById` through the public `GetFeature` operation. The stored query substituted the caller's `ID` parameter i...
sitename: GitHub
date: "2026-11-23"
categories: ['repository:2751199']
fingerprint: "3d29e7366a5bf0e7"
language: en
image: https://opengraph.githubassets.com/a463012e406f51e56d080b6cc12ac4320020ebc94e75eea28c02ef861a351a48/geoserver/geoserver/security/advisories/GHSA-39mw-5chv-jh47
pagetype: object
filedate: "2026-11-28"
---
  
    GeoServer exposes the built-in WFS 2.0 stored query `urn:ogc:def:query:OGC-WFS::GetFeatureById` through the public `GetFeature` operation. The stored query substituted the caller's `ID` parameter into an XML template without escaping, then parsed the result without GeoServer's entity resolver. An unauthenticated caller could inject XML, including an `xi:include`, into the query.

### Impact

A single unauthenticated WFS request can:

- read a local text file readable by the GeoServer process;
- fetch an attacker selected HTTP or HTTPS URL (server-side request forgery);
- receive the fetched text in the `Illegal property name` error response.

No authentication, custom stored query or `CreateStoredQuery` access is required. Contents are echoed when a layer is published to anonymous users; otherwise the file is still read but not returned.

### Details

`StoredQuery.compile()` replaced the `${ID}` token in the `GetFeatureById` template (`<fes:ResourceId rid='${ID}'/>`) using plain string replacement, so quotes and angle brackets in the value could close the `rid` attribute and add new FES elements. The result was parsed with `new Parser(new WFSConfiguration())` without the catalog entity resolver used elsewhere in the class, so XInclude and external entities were resolved with ordinary URI access.

### Mitigation

Restrict or disable the WFS service for anonymous users using service security, or disable WFS if it is not required.

### Resolution

Stored query parsing now uses the GeoServer entity resolver, and the GeoTools `PreventLocalEntityResolver` checks redirects.

- GeoServer 2.27.7, 2.28.6, 3.0.2
- GeoTools 33.7, 34.6, 35.2

### References

GeoServer exposes the built-in WFS 2.0 stored query `urn:ogc:def:query:OGC-WFS::GetFeatureById` through the public `GetFeature` operation. The stored query substituted the caller's `ID` parameter into an XML template without escaping, then parsed the result without GeoServer's entity resolver. An unauthenticated caller could inject XML, including an `xi:include`, into the query.

## Impact

A single unauthenticated WFS request can:

`Illegal property name`error response.
No authentication, custom stored query or `CreateStoredQuery` access is required. Contents are echoed when a layer is published to anonymous users; otherwise the file is still read but not returned.

## Details

`StoredQuery.compile()` replaced the `${ID}` token in the `GetFeatureById` template (`<fes:ResourceId rid='${ID}'/>`) using plain string replacement, so quotes and angle brackets in the value could close the `rid` attribute and add new FES elements. The result was parsed with `new Parser(new WFSConfiguration())` without the catalog entity resolver used elsewhere in the class, so XInclude and external entities were resolved with ordinary URI access.

## Mitigation

Restrict or disable the WFS service for anonymous users using service security, or disable WFS if it is not required.

## Resolution

Stored query parsing now uses the GeoServer entity resolver, and the GeoTools `PreventLocalEntityResolver` checks redirects.

## References
