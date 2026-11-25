---
title: Service security rules bypassed with a prefixed service name such as x/WFS
author: Jodygarnett
url: https://github.com/geoserver/geoserver/security/advisories/GHSA-rv5g-g2r9-58rj
hostname: github.com
description: A `service` parameter with a prefix, such as `service=x/WFS`, was resolved to the WFS service by the dispatcher, but service security checked the unresolved name `x/WFS`. No rule matched, so opera...
sitename: GitHub
date: "2026-11-23"
categories: ['repository:2751199']
fingerprint: "13b8e5d5f5458267"
language: en
image: https://opengraph.githubassets.com/8a9583169d13df9f2c44d1fccb9ee0a96151f9bfe78d1408390e59f100a2c1f6/geoserver/geoserver/security/advisories/GHSA-rv5g-g2r9-58rj
pagetype: object
filedate: "2026-11-25"
---
  
    A `service` parameter with a prefix, such as `service=x/WFS`, was resolved to the WFS service by the dispatcher, but

service security checked the unresolved name `x/WFS`. No rule matched, so operations restricted in service security

ran without a role check. The default configuration restricts `CreateStoredQuery` and `DropStoredQuery` to

administrators, so anonymous users could create and delete WFS stored queries.

This was also reported as step 2 of a remote command execution chain, see

[GHSA-hgm3-wq4h-8vvq](https://github.com/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq).

### Impact

An unauthenticated user can call any OWS operation that is restricted only by service security rules

(**Security > Services**, `security/services.properties`). With the default rules this allows creating and deleting

WFS stored queries. Installations that restrict other operations this way, for example WFS `Transaction`, lose that

protection as well. Layer and data security rules still apply.

Stored queries created this way are the entry point for

[GHSA-39mw-5chv-jh47](https://github.com/geoserver/geoserver/security/advisories/GHSA-39mw-5chv-jh47).

### Details

`Dispatcher.findService` strips everything up to `/` from the service id to choose the service, while

`OperationSecurityCallback` matched rules against the `service` value of the request, which still held `x/WFS`.

### Mitigation

Block requests whose `service` parameter contains `/`, in the query string or in the `service` attribute of an XML

request, at a proxy in front of GeoServer.

Review the data directory `wfs/query` and `workspaces/*/wfs/query` folders for stored queries you did not create.

### Resolution

Patched for:

- GeoServer 3.0.2
- GeoServer 2.28.6
- GeoServer 2.27.7

The dispatcher now sets the request service to the resolved service id, so service security checks the service

that runs. No manual steps required.

### References

A `service` parameter with a prefix, such as `service=x/WFS`, was resolved to the WFS service by the dispatcher, but

service security checked the unresolved name `x/WFS`. No rule matched, so operations restricted in service security

ran without a role check. The default configuration restricts `CreateStoredQuery` and `DropStoredQuery` to

administrators, so anonymous users could create and delete WFS stored queries.

This was also reported as step 2 of a remote command execution chain, see

GHSA-hgm3-wq4h-8vvq.

## Impact

An unauthenticated user can call any OWS operation that is restricted only by service security rules

(**Security > Services**, `security/services.properties`). With the default rules this allows creating and deleting

WFS stored queries. Installations that restrict other operations this way, for example WFS `Transaction`, lose that

protection as well. Layer and data security rules still apply.

Stored queries created this way are the entry point for

GHSA-39mw-5chv-jh47.

## Details

`Dispatcher.findService` strips everything up to `/` from the service id to choose the service, while

`OperationSecurityCallback` matched rules against the `service` value of the request, which still held `x/WFS`.

## Mitigation

Block requests whose `service` parameter contains `/`, in the query string or in the `service` attribute of an XML

request, at a proxy in front of GeoServer.

Review the data directory `wfs/query` and `workspaces/*/wfs/query` folders for stored queries you did not create.

## Resolution

Patched for:

The dispatcher now sets the request service to the resolved service id, so service security checks the service

that runs. No manual steps required.

## References
