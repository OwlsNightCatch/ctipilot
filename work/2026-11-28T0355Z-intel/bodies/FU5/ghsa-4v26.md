---
title: WFS stored query exception discloses data directory path
author: Jodygarnett
url: https://github.com/geoserver/geoserver/security/advisories/GHSA-4v26-c537-jvxc
hostname: github.com
description: A WFS stored query request with an overlong id returned an exception report containing the absolute data directory path. This was reported as step 1 of an unauthenticated remote command executi...
sitename: GitHub
date: "2026-11-23"
categories: ['repository:2751199']
fingerprint: b0eac1e660f8567
language: en
image: https://opengraph.githubassets.com/26ac9c9035206dcdad711c2e1cd3ae1877ca3f84fae5d34cbf5d90109da01d7a/geoserver/geoserver/security/advisories/GHSA-4v26-c537-jvxc
pagetype: object
filedate: "2026-11-28"
---
  
    A WFS stored query request with an overlong id returned an exception report containing the absolute data directory

path.

This was reported as step 1 of an unauthenticated remote command execution chain, see

[GHSA-hgm3-wq4h-8vvq](https://github.com/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq).

### Impact

An unauthenticated user learns the absolute data directory path. This is not harmful by itself, but other attacks

need it, for example to build `file:` references to data directory files.

### Details

The stored query id is mapped to a file name in the data directory. An id longer than the file system name limit

failed with a file system error, and the WFS exception report included the error message with the full path.

### Mitigation

None needed beyond upgrading; the path alone gives no access.

### Resolution

Patched for:

- GeoServer 3.0.2
- GeoServer 2.28.6
- GeoServer 2.27.7

Overlong stored query ids are rejected with a short error, and file system errors are logged instead of returned to

the client. No manual steps required.

### References

A WFS stored query request with an overlong id returned an exception report containing the absolute data directory

path.

This was reported as step 1 of an unauthenticated remote command execution chain, see

GHSA-hgm3-wq4h-8vvq.

## Impact

An unauthenticated user learns the absolute data directory path. This is not harmful by itself, but other attacks

need it, for example to build `file:` references to data directory files.

## Details

The stored query id is mapped to a file name in the data directory. An id longer than the file system name limit

failed with a file system error, and the WFS exception report included the error message with the full path.

## Mitigation

None needed beyond upgrading; the path alone gives no access.

## Resolution

Patched for:

Overlong stored query ids are rejected with a short error, and file system errors are logged instead of returned to

the client. No manual steps required.

## References
