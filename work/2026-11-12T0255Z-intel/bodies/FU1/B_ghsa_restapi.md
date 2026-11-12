---
title: Restricted code can bypass permissions via json.dump/json.load
author: Mauritsvanrees
url: https://github.com/plone/plone.restapi/security/advisories/GHSA-vgxm-pwch-89q6
hostname: github.com
description: "### Summary Restricted code can bypass permissions via functions in the `json` module. ### Details `plone.restapi` calls `AccessControl.allow_module(\"json\")` when it is imported (`src/plon..."
sitename: GitHub
date: "2026-11-10"
categories: ['repository:19173345']
fingerprint: "3c33ac42ec5c7219"
---
  
    ### Summary

Restricted code can bypass permissions via functions in the `json` module.

### Details

`plone.restapi` calls `AccessControl.allow_module("json")` when it is imported (`src/plone/restapi/__init__.py`). This makes the whole `json` module from the standard library available to restricted code: Script (Python) objects, and TALES `python:` expressions in page templates and other places.

Most of the module is harmless from restricted code. But some functions could be used to call protected methods on any object, even if the current user does not have the permission that protects the method.

The declaration was added in 2015 for a customized `standard_error_message` skin script that used `json.dumps`. See commit [`1ff230c`](https://github.com/plone/plone.restapi/commit/1ff230ca572710684db20f9c8788fbc8b2671540) . That script was removed shortly after, but the `allow_module` call stayed. Nothing in `plone.restapi` needs it today, or in any release.

### Fixed versions

- For Plone 6.2: upgrade to `plone.restapi` 10.2.1
- For Plone 6.0 and 6.1: upgrade to `plone.restapi` 9.15.8 (can be used on 5.2 as well, if you are on Python 3.8).

### Impact

This is a permission bypass in restricted code (CWE-863, Incorrect Authorization). Any code that can run restricted Python in a site with `plone.restapi` installed can call protected methods on any object it can reach, without the permissions that protect those methods.

On its own this does not let anonymous users run restricted code. Running restricted code needs permission to add or edit Python scripts or templates, which only Managers have by default. The risk is that it widens what an attacker can do once they can get restricted code to run with lower privileges, through a separate injection vulnerability.

Nothing in `plone.restapi` needs this code. If you have a through-the-web script that needs JSON, you can give it access to for example only `json.dumps` and `json.loads` with `ModuleSecurityInfo("json").declarePublic("dumps", "loads")`. Those two functions do not call methods on objects that the caller passes in.

## Summary

Restricted code can bypass permissions via functions in the

`json`module.
## Details

`plone.restapi`calls`AccessControl.allow_module("json")`when it is imported (`src/plone/restapi/__init__.py`). This makes the whole`json`module from the standard library available to restricted code: Script (Python) objects, and TALES`python:`expressions in page templates and other places.
Most of the module is harmless from restricted code. But some functions could be used to call protected methods on any object, even if the current user does not have the permission that protects the method.

The declaration was added in 2015 for a customized

`standard_error_message`skin script that used`json.dumps`. See commit1ff230c. That script was removed shortly after, but the`allow_module`call stayed. Nothing in`plone.restapi`needs it today, or in any release.
## Fixed versions

`plone.restapi`10.2.1`plone.restapi`9.15.8 (can be used on 5.2 as well, if you are on Python 3.8).
## Impact

This is a permission bypass in restricted code (CWE-863, Incorrect Authorization). Any code that can run restricted Python in a site with

`plone.restapi`installed can call protected methods on any object it can reach, without the permissions that protect those methods.
On its own this does not let anonymous users run restricted code. Running restricted code needs permission to add or edit Python scripts or templates, which only Managers have by default. The risk is that it widens what an attacker can do once they can get restricted code to run with lower privileges, through a separate injection vulnerability.

Nothing in

`plone.restapi`needs this code. If you have a through-the-web script that needs JSON, you can give it access to for example only`json.dumps`and`json.loads`with`ModuleSecurityInfo("json").declarePublic("dumps", "loads")`. Those two functions do not call methods on objects that the caller passes in.
