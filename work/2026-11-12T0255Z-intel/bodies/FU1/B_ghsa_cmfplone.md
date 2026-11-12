---
title: Overly broad allow_module declarations in Products.CMFPlone expose imported names to restricted code
author: Mauritsvanrees
url: https://github.com/plone/Products.CMFPlone/security/advisories/GHSA-92qw-564p-pmg6
hostname: github.com
description: "### Summary Plone opened entire internal modules to restricted code (for example Script (Python) edited through the web), instead of exposing only the functions that are actually needed. ###..."
sitename: GitHub
date: "2026-11-10"
categories: ['repository:2452759']
fingerprint: "8e3b8632ee156478"
---
  
    ### Summary

Plone opened entire internal modules to restricted code (for example Script (Python) edited through the web), instead of exposing only the functions that are actually needed.

### Details

`Products.CMFPlone` calls `AccessControl.allow_module()` on `Products.CMFPlone.utils`, `Products.CMFPlone.browser.navtree` and `OFS.ObjectManager`. `allow_module()` makes every name in a module importable from restricted code (for example Script (Python), through `guarded_import`), instead of exposing only the functions that are actually needed.

As a result, helper objects that these modules merely import from other packages were reachable as well, which widened the attack surface for no reason.

The fix replaces the blanket permissions with an explicit list of the public names, and the module OFS.ObjectManager is no longer opened at all. Regression tests verify that the intended functions still work and that the extra names are no longer accessible.

The fix also adds defense-in-depth hardening by explicitly disallowing access to some dangerous functions and modules, so they can't be accidentally made public again.

Thanks to Mokrane ABDELMALEK for reporting (via the Ghent University VDP programme). [https://vdp.ugent.be/](https://vdp.ugent.be/)

### Impact

The exposed names could be used to allow access to more modules and gain elevated privileges.

Who is affected: Sites where untrusted or low-trust users can author restricted code. These are users with a role that allows creating or editing Script (Python) or similar.

## Summary

Plone opened entire internal modules to restricted code (for example Script (Python) edited through the web), instead of exposing only the functions that are actually needed.

## Details

`Products.CMFPlone`calls`AccessControl.allow_module()`on`Products.CMFPlone.utils`,`Products.CMFPlone.browser.navtree`and`OFS.ObjectManager`.`allow_module()`makes every name in a module importable from restricted code (for example Script (Python), through`guarded_import`), instead of exposing only the functions that are actually needed.
As a result, helper objects that these modules merely import from other packages were reachable as well, which widened the attack surface for no reason.

The fix replaces the blanket permissions with an explicit list of the public names, and the module OFS.ObjectManager is no longer opened at all. Regression tests verify that the intended functions still work and that the extra names are no longer accessible.

The fix also adds defense-in-depth hardening by explicitly disallowing access to some dangerous functions and modules, so they can't be accidentally made public again.

Thanks to Mokrane ABDELMALEK for reporting (via the Ghent University VDP programme). https://vdp.ugent.be/

## Impact

The exposed names could be used to allow access to more modules and gain elevated privileges.

Who is affected: Sites where untrusted or low-trust users can author restricted code. These are users with a role that allows creating or editing Script (Python) or similar.
