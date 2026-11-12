---
title: Missing security declarations on CMFEditions modifier classes
author: Mauritsvanrees
url: https://github.com/plone/Products.CMFEditions/security/advisories/GHSA-67qm-q795-jh7h
hostname: github.com
description: "### Summary Missing security declarations on CMFEditions modifier classes allow methods such as edit to be published without a permission check. ### Details ConditionalModifier and Conditi..."
sitename: GitHub
date: "2026-11-10"
categories: ['repository:2808579']
fingerprint: bcca2d7ee9bb7268
---
    ### Summary

Missing security declarations on CMFEditions modifier classes allow methods such as edit to be published without a permission check.

### Details

ConditionalModifier and ConditionalTalesModifier (Modifiers.py) and the two standard size guard modifiers AbortVersioningOfLargeFilesAndImages and SkipVersioningOfLargeFilesAndImages (StandardModifiers.py) declare no security. Methods with docstrings, including edit, are therefore publishable.

Fixed by protecting edit with Manage portal, the accessors with View management screens, and making the size guard hooks private.

Thanks to Mokrane ABDELMALEK for reporting (via the Ghent University VDP programme). [https://vdp.ugent.be/](https://vdp.ugent.be/)

Thanks to Andreas Jung for sharing extra ideas on what should be fixed.

### Proof of concept

A working proof of concept exists. There are various ways to abuse this, depending on the payload that is set in the condition.

Several other vulnerability advisories will be published on the same day, which limit the accepted payloads.

### Detecting changes

An attacker may have already changed conditions on your site.  These changes stay in the database. When you are logged in with the Manager role, you can call the new `@@check-modifier-conditions` page on the Plone site root. This compares the current settings with the default settings.  It warns when these differ, and gives the possibility to revert to the default.

Note that a difference does not necessarily mean that the site has been hacked. For example, the defaults have changed a bit over time, so your site may have an old default. Or an add-on or an admin has changed it for a valid reason.

### Fixed versions

- For Plone 6.2: upgrade to `Products.CMFEditions` 5.0.2
- For Plone 6.0 and 6.1: upgrade to `Products.CMFEditions` 4.0.7

### Impact

Missing authorization (CWE-862). An anonymous user could reach a modifier object and change its enabled state, title, TALES condition or size limits.  This user could then trigger running the payload itself, which could lead to remote code execution in combination with some other vulnerabilities published today. Or the payload could be run automatically when a user with higher privileges makes a change to content that is versioned, leading to execution of the payload with higher privileges.

## Summary

Missing security declarations on CMFEditions modifier classes allow methods such as edit to be published without a permission check.

## Details

ConditionalModifier and ConditionalTalesModifier (Modifiers.py) and the two standard size guard modifiers AbortVersioningOfLargeFilesAndImages and SkipVersioningOfLargeFilesAndImages (StandardModifiers.py) declare no security. Methods with docstrings, including edit, are therefore publishable.

Fixed by protecting edit with Manage portal, the accessors with View management screens, and making the size guard hooks private.

Thanks to Mokrane ABDELMALEK for reporting (via the Ghent University VDP programme). https://vdp.ugent.be/

Thanks to Andreas Jung for sharing extra ideas on what should be fixed.

## Proof of concept

A working proof of concept exists. There are various ways to abuse this, depending on the payload that is set in the condition.

Several other vulnerability advisories will be published on the same day, which limit the accepted payloads.

## Detecting changes

An attacker may have already changed conditions on your site. These changes stay in the database. When you are logged in with the Manager role, you can call the new

`@@check-modifier-conditions`page on the Plone site root. This compares the current settings with the default settings. It warns when these differ, and gives the possibility to revert to the default.
Note that a difference does not necessarily mean that the site has been hacked. For example, the defaults have changed a bit over time, so your site may have an old default. Or an add-on or an admin has changed it for a valid reason.

## Fixed versions

`Products.CMFEditions`5.0.2`Products.CMFEditions`4.0.7
## Impact

Missing authorization (CWE-862). An anonymous user could reach a modifier object and change its enabled state, title, TALES condition or size limits. This user could then trigger running the payload itself, which could lead to remote code execution in combination with some other vulnerabilities published today. Or the payload could be run automatically when a user with higher privileges makes a change to content that is versioned, leading to execution of the payload with higher privileges.
