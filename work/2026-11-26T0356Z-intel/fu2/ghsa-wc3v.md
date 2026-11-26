---
title: Remote Code Execution via SQLite JDBC Extension Loading in GeoServer JDBC Security Configuration
author: Jodygarnett
url: https://github.com/geoserver/geoserver/security/advisories/GHSA-wc3v-48j7-xf57
hostname: github.com
description: GeoServer's JDBC user/group service, role service and authentication provider accepted an administrator supplied JDBC connection URL and DML/DDL property file paths without validation. Choosing the...
sitename: GitHub
date: "2026-11-23"
categories: ['repository:2751199']
fingerprint: "78ac0c87e21c0ad"
language: en
image: https://opengraph.githubassets.com/91021dcaeddaa92e314f73a1512afba5c88bb13fbc39ec8bc241428cc2ab4181/geoserver/geoserver/security/advisories/GHSA-wc3v-48j7-xf57
pagetype: object
filedate: "2026-11-26"
---
  
    GeoServer's JDBC user/group service, role service and authentication provider accepted an administrator supplied JDBC connection URL and DML/DDL property file paths without validation. Choosing the SQLite driver with the `enable_load_extension=true` connection parameter, together with a DML file containing `SELECT load_extension(...)`, loads a native library of the attacker's choice into the GeoServer process.

### Impact

An administrator, or anyone with access to an administrator session, can execute arbitrary code as the user running GeoServer.

- On Windows both the DML file and the extension library can be loaded from an SMB share (UNC path), so no files need to be staged on the server.
- On other platforms the attacker must first place the DML file and library on the server file system.

### Details

`AbstractJDBCService.initializeDSFromConfig()` passed the configured driver class and connection URL directly to the connection pool. `checkORCreateJDBCPropertyFile()` accepted absolute paths for the DML and DDL property files, including UNC paths. The DML statements run when the service is used, for example when listing users.

### Mitigation

Restrict access to the GeoServer administration console and REST API to trusted administrators, and do not install JDBC drivers that are not required (such as SQLite) on the GeoServer classpath.

### Resolution

JDBC security services now accept only known drivers and connection parameters for each driver, and reject absolute DML/DDL file paths. Additional parameters can be allowed with the `GEOSERVER_JDBC_EXTRA_PARAMETERS` property.

- GeoServer 2.27.7, 2.28.6, 3.0.2

### References

GeoServer's JDBC user/group service, role service and authentication provider accepted an administrator supplied JDBC connection URL and DML/DDL property file paths without validation. Choosing the SQLite driver with the `enable_load_extension=true` connection parameter, together with a DML file containing `SELECT load_extension(...)`, loads a native library of the attacker's choice into the GeoServer process.

## Impact

An administrator, or anyone with access to an administrator session, can execute arbitrary code as the user running GeoServer.

## Details

`AbstractJDBCService.initializeDSFromConfig()` passed the configured driver class and connection URL directly to the connection pool. `checkORCreateJDBCPropertyFile()` accepted absolute paths for the DML and DDL property files, including UNC paths. The DML statements run when the service is used, for example when listing users.

## Mitigation

Restrict access to the GeoServer administration console and REST API to trusted administrators, and do not install JDBC drivers that are not required (such as SQLite) on the GeoServer classpath.

## Resolution

JDBC security services now accept only known drivers and connection parameters for each driver, and reject absolute DML/DDL file paths. Additional parameters can be allowed with the `GEOSERVER_JDBC_EXTRA_PARAMETERS` property.

## References
