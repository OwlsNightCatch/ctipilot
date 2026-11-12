---
title: Restricted Python sandbox escape via allow_module
author: Mauritsvanrees
url: https://github.com/plone/plone.batching/security/advisories/GHSA-6hcx-c235-cxh3
hostname: github.com
description: "### Summary Overly broad allow_module exposes all of `plone.batching` to Restricted Python. ### Details `src/plone/batching/__init__.py` calls `allow_module(\"plone.batching\")`, publishing ..."
sitename: GitHub
date: "2026-11-10"
categories: ['repository:3990973']
fingerprint: "6a3a0fb1dd9d74d8"
---
  
    ### Summary

Overly broad allow\_module exposes all of `plone.batching` to Restricted Python.

### Details

`src/plone/batching/__init__.py` calls `allow_module("plone.batching")`, publishing every name in that module to restricted code instead of only `Batch`.

Fixed by declaring only that name public with `ModuleSecurityInfo.declarePublic`.

### Fixed versions

- For Plone 6.2: upgrade to `plone.batching` 3.0.3
- For Plone 6.0 and 6.1: upgrade to `plone.batching` 2.0.8

### Impact

The exposed names could be used to allow access to more modules and gain elevated privileges.

Affects sites where untrusted users can author restricted code.

## Summary

Overly broad allow\_module exposes all of

`plone.batching`to Restricted Python.
## Details

`src/plone/batching/__init__.py`calls`allow_module("plone.batching")`, publishing every name in that module to restricted code instead of only`Batch`.
Fixed by declaring only that name public with

`ModuleSecurityInfo.declarePublic`.
## Fixed versions

`plone.batching`3.0.3`plone.batching`2.0.8
## Impact

The exposed names could be used to allow access to more modules and gain elevated privileges.

Affects sites where untrusted users can author restricted code.
