---
title: Restricted Python sandbox escape via allow_module of Products.MimetypesRegistry.common
author: Mauritsvanrees
url: https://github.com/plone/Products.MimetypesRegistry/security/advisories/GHSA-xcj2-cmp9-fj62
hostname: github.com
description: "### Summary Overly broad allow_module exposes all of `Products.MimetypesRegistry.common` to Restricted Python. ### Details `src/Products/MimetypesRegistry/__init__.py` calls `allow_module(..."
sitename: GitHub
date: "2026-11-10"
categories: ['repository:2479448']
fingerprint: "6a3a0cb5dd8d74d8"
---
  
    ### Summary

Overly broad allow\_module exposes all of `Products.MimetypesRegistry.common` to Restricted Python.

### Details

`src/Products/MimetypesRegistry/__init__.py` calls `allow_module("Products.MimetypesRegistry.common")`, publishing every name in that module and `Products.MimetypesRegistry` itself to restricted code instead of only `MimeTypeException`.

Fixed by declaring only that name public with `ModuleSecurityInfo.declarePublic`.

Thanks to Mokrane ABDELMALEK for reporting (via the Ghent University VDP programme). [https://vdp.ugent.be/](https://vdp.ugent.be/)

### Fixed versions

- For Plone 6.2: upgrade to `Products.MimetypesRegistry` 4.0.2
- For Plone 6.0 and 6.1: upgrade to `Products.MimetypesRegistry` 3.0.2

### Impact

The exposed names could be used to allow access to more modules and gain elevated privileges.

Affects sites where untrusted users can author restricted code.

## Summary

Overly broad allow\_module exposes all of

`Products.MimetypesRegistry.common`to Restricted Python.
## Details

`src/Products/MimetypesRegistry/__init__.py`calls`allow_module("Products.MimetypesRegistry.common")`, publishing every name in that module and`Products.MimetypesRegistry`itself to restricted code instead of only`MimeTypeException`.
Fixed by declaring only that name public with

`ModuleSecurityInfo.declarePublic`.
Thanks to Mokrane ABDELMALEK for reporting (via the Ghent University VDP programme). https://vdp.ugent.be/

## Fixed versions

`Products.MimetypesRegistry`4.0.2`Products.MimetypesRegistry`3.0.2
## Impact

The exposed names could be used to allow access to more modules and gain elevated privileges.

Affects sites where untrusted users can author restricted code.
