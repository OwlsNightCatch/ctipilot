---
title: Heap-based Buffer Overflow in TDS Prelogin Parser
author: Shardgupta
url: https://github.com/babelfish-for-postgresql/babelfish_extensions/security/advisories/GHSA-vq28-vgj3-r26w
hostname: github.com
description: "## Summary Babelfish for PostgreSQL enables users to run SQL Server workloads without modifying their applications. Babelfish is developed as an open source project using PostgreSQL's extension mo..."
sitename: GitHub
date: "2026-11-07"
categories: ['repository:420297429']
fingerprint: a7827d3a9c385ed0
---
  
    ## Summary

Babelfish for PostgreSQL enables users to run SQL Server workloads without modifying their applications. Babelfish is developed as an open source project using PostgreSQL's extension model ([https://github.com/babelfish-for-postgresql/babelfish\_extensions/](https://github.com/babelfish-for-postgresql/babelfish_extensions/)). An issue exists in the TDS connection-handshake handling where, under certain conditions, a malformed request can corrupt process memory.

## Impact

A memory-safety issue in the TDS connection-handshake code path can be triggered by a remote, unauthenticated actor sending a crafted request to the TDS endpoint. Successfully leveraging this issue can affect the confidentiality, integrity, and availability of the database process.

Impacted versions: 1.0-1.5, 2.1-2.15, 3.1-3.12, 4.0-4.8, 5.1-5.4

## Patches

This issue has been addressed in Babelfish for PostgreSQL versions 4.10, 5.6 and 6.1. We recommend upgrading to the latest version and ensuring any forked or derivative code is patched to incorporate the new fixes.

## Workarounds

Restrict network access to the TDS port (default 1433) to trusted sources using network security controls until the upgrade is applied.

## References

If you have any questions or comments about this advisory, we ask that you contact AWS Security via our [vulnerability reporting page](https://aws.amazon.com/security/vulnerability-reporting) or directly via email to [aws-security@amazon.com](mailto:aws-security@amazon.com). Please do not create a public GitHub issue.

## Summary

Babelfish for PostgreSQL enables users to run SQL Server workloads without modifying their applications. Babelfish is developed as an open source project using PostgreSQL's extension model (https://github.com/babelfish-for-postgresql/babelfish\_extensions/). An issue exists in the TDS connection-handshake handling where, under certain conditions, a malformed request can corrupt process memory.

## Impact

A memory-safety issue in the TDS connection-handshake code path can be triggered by a remote, unauthenticated actor sending a crafted request to the TDS endpoint. Successfully leveraging this issue can affect the confidentiality, integrity, and availability of the database process.

Impacted versions: 1.0-1.5, 2.1-2.15, 3.1-3.12, 4.0-4.8, 5.1-5.4

## Patches

This issue has been addressed in Babelfish for PostgreSQL versions 4.10, 5.6 and 6.1. We recommend upgrading to the latest version and ensuring any forked or derivative code is patched to incorporate the new fixes.

## Workarounds

Restrict network access to the TDS port (default 1433) to trusted sources using network security controls until the upgrade is applied.

## References

If you have any questions or comments about this advisory, we ask that you contact AWS Security via our vulnerability reporting page or directly via email to aws-security@amazon.com. Please do not create a public GitHub issue.
