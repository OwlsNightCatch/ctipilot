---
title: Deserialization in JDBC user and role services allows administrator code execution
author: Jodygarnett
url: https://github.com/geoserver/geoserver/security/advisories/GHSA-9wf2-fcgq-vxhq
hostname: github.com
description: The JDBC user group and role services read user and role property values with `ResultSet.getObject()`. An administrator could configure a service backed by an uploaded HSQLDB database whose proper...
sitename: GitHub
date: "2026-11-23"
categories: ['repository:2751199']
fingerprint: "9aa80d48da90285"
language: en
image: https://opengraph.githubassets.com/ca2f8a00ded4c84b4e269ae4bdeca1ddcac609041b316247520da26803d77baa/geoserver/geoserver/security/advisories/GHSA-9wf2-fcgq-vxhq
pagetype: object
filedate: "2026-11-25"
---
  
    The JDBC user group and role services read user and role property values with `ResultSet.getObject()`. An

administrator could configure a service backed by an uploaded HSQLDB database whose property values are serialized

Java objects. These were deserialized when users or roles were loaded, executing code.

This was reported as step 5 of an unauthenticated remote command execution chain, see

[GHSA-hgm3-wq4h-8vvq](https://github.com/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq).

### Impact

An administrator, or anyone who takes over an administrator session, can execute code with the operating system

privileges of the GeoServer process.

### Details

`JDBCUserGroupService` and `JDBCRoleService` read the property value column with `getObject()`. For an HSQLDB

`OTHER` column the driver deserializes the value with an unrestricted `ObjectInputStream`. The JDBC security module

and HSQLDB driver are part of the standard distribution, and the REST API allows an administrator to upload a

database file to the data directory and create a JDBC user group service that uses it.

### Mitigation

Limit administrator access to trusted users, and restrict access to the REST API `/rest/resource` and

`/rest/security` endpoints to trusted networks.

### Resolution

Patched for:

- GeoServer 3.0.2
- GeoServer 2.28.6
- GeoServer 2.27.7

User and role property values are now read as text. No manual steps required.

### References

The JDBC user group and role services read user and role property values with `ResultSet.getObject()`. An

administrator could configure a service backed by an uploaded HSQLDB database whose property values are serialized

Java objects. These were deserialized when users or roles were loaded, executing code.

This was reported as step 5 of an unauthenticated remote command execution chain, see

GHSA-hgm3-wq4h-8vvq.

## Impact

An administrator, or anyone who takes over an administrator session, can execute code with the operating system

privileges of the GeoServer process.

## Details

`JDBCUserGroupService` and `JDBCRoleService` read the property value column with `getObject()`. For an HSQLDB

`OTHER` column the driver deserializes the value with an unrestricted `ObjectInputStream`. The JDBC security module

and HSQLDB driver are part of the standard distribution, and the REST API allows an administrator to upload a

database file to the data directory and create a JDBC user group service that uses it.

## Mitigation

Limit administrator access to trusted users, and restrict access to the REST API `/rest/resource` and

`/rest/security` endpoints to trusted networks.

## Resolution

Patched for:

User and role property values are now read as text. No manual steps required.

## References
