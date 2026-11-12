---
title: Plone security hotfix 20261110
author: Mauritsvanrees
url: https://community.plone.org/t/plone-security-hotfix-20261110/23313
hostname: plone.org
description: "Plone security fix 20261110: remote code execution On behalf of the Plone/Zope Security Team: today we release fixes for a remote code execution vulnerability in Plone. We announced this last week in the pre-announcement. All supported Plone versions are affected: 6.0, 6.1 and 6.2. Older versions are affected as well, back to at least Plone 4.3. Please update now. Details are public from today, and with current AI tools it may not take long to turn them into a working exploit. What is the ..."
sitename: Plone Community
date: "2026-11-10"
fingerprint: "3e3b15b69c995edc"
---
              # 

On behalf of the Plone/Zope Security Team: today we release fixes for a **remote code execution** vulnerability in Plone.

We announced this last week in the [pre-announcement](https://community.plone.org/t/pre-announcement-plone-security-fix-20261110/23303).

All supported Plone versions are affected: 6.0, 6.1 and 6.2.

Older versions are affected as well, back to at least Plone 4.3.

Please update now.

Details are public from today, and with current AI tools it may not take long to turn them into a working exploit.

## 

It is a chain of several issues, which together let an anonymous visitor run code on the server.

- `Products.CMFEditions`: the conditional modifiers in `portal_modifier` had no security declarations.
An anonymous visitor could change the TALES condition of a modifier, and then run it.
This condition is also evaluated when an editor saves versioned content, so even on its own it lets an attacker run code with the privileges of that editor.
- `Products.CMFPlone`, `Products.MimetypesRegistry` and `plone.batching` opened whole modules to restricted code with `allow_module`.
This also exposed everything these modules import.
This allowed restricted code (TALES expressions, Python Scripts) to escape the sandbox and reach modules like `os`.
- `plone.restapi` opened the `json` module from the standard library to restricted code.
Some of its functions could be used to call protected methods on any object, without having the needed permission.

Thanks to Mokrane ABDELMALEK for reporting this, via the [Ghent University VDP programme](https://vdp.ugent.be/).

Thanks also to Andreas Jung for sharing extra ideas on what should be fixed.

## 

CVE numbers have been requested and will be added to the advisories when they are assigned.

## 

You have two options:

1. **Plone 6.0, 6.1 and 6.2:** update the package versions listed below.
This is the recommended way.
2. **Any Plone version from 4.3 to 6.2:** install the hotfix package [Products.PloneHotfix20261110](https://pypi.org/project/Products.PloneHotfix20261110/). You may need to spell this as `products-plonehotfix20261110` if you have an old setuptools/buildout/pip version.

Restart all Zope instances afterwards.

Since one of the vulnerabilities is in `Products.CMFPlone`, we will also make full new releases of the 6.0, 6.1, and 6.2 series, including Docker images.  These won't be security-only, but include bug fixes.  They should be ready later today.

The workaround from the pre-announcement, blocking all urls that contain `portal_modifier` in your web server, is still a good idea.

You can keep it in place after updating.

### 

These are in Buildout notation.

If you use a pip constraints file, use a double equals sign, for example `Products.CMFPlone==6.2.3`.

#### 

```
Products.CMFPlone = 6.2.3
Products.CMFEditions = 5.0.2
Products.MimetypesRegistry = 4.0.2
plone.batching = 3.0.3
plone.restapi = 10.2.1
```

#### 

```
Products.CMFPlone = 6.1.6
Products.CMFEditions = 4.0.7
Products.MimetypesRegistry = 3.0.2
plone.batching = 2.0.8
plone.restapi = 9.15.8
```

#### 

```
Products.CMFPlone = 6.0.16
Products.CMFEditions = 4.0.7
Products.MimetypesRegistry = 3.0.2
plone.batching = 2.0.8
plone.restapi = 9.15.8
```

If you do not use `plone.restapi`, you can skip that one.

### 

The hotfix [Products.PloneHotfix20261110](https://pypi.org/project/Products.PloneHotfix20261110/) works on Plone 4.3, 5.0, 5.1, 5.2, 6.0, 6.1 and 6.2, on Python 2.7 and Python 3.

See its page on PyPI for installation instructions.

When you use the fixed versions of all the packages above, you do not need the hotfix, but it does no harm either.

Plone 5.2 and older have been out of security support for several years.

For this fix we made an exception, because of the severity.

If you still use such a version, your site likely has other known vulnerabilities, and you should upgrade to Plone 6 soon.

## 

A changed modifier condition stays in the database, also after you install the fix.

So please check this, especially if you did not block `portal_modifier` before today.

- With the updated `Products.CMFEditions`: log in as Manager and go to `@@check-modifier-conditions` on the Plone site root, for example `https://example.org/@@check-modifier-conditions`.
This compares the conditions in `portal_modifier` with the defaults, and lets you revert changed ones.
- With the hotfix: on startup, the hotfix checks the conditions in all Plone sites.
If a condition differs from the default, it logs a warning with `POSSIBLE ATTACK: MODIFIED VERSIONING CONDITIONS FOUND`.
Otherwise it logs `No changed modifier conditions found.`

A difference does not necessarily mean that your site was attacked.

The defaults have changed a bit over time, so your site may have an old default.

Or an add-on or an admin changed it for a valid reason.

But if you do not recognize the condition, treat your server as compromised.

## 

Restricted code can now only import the names that Plone itself needs from these modules.

If your own Python Scripts or templates import other names from `Products.CMFPlone`, `Products.CMFPlone.utils`, `Products.CMFPlone.browser.navtree`, `OFS.ObjectManager`, `Products.MimetypesRegistry.common` or `plone.batching`, they now get an `Unauthorized` error.

With the updated `plone.restapi` the same is true for anything from the `json` module.

The hotfix still allows `json.dumps` and `json.loads`.

You can fix this by declaring the names you need in your own add-on, for example:

```
from AccessControl import ModuleSecurityInfo
ModuleSecurityInfo("json").declarePublic("dumps", "loads")
```

Never use `allow_module` for this.

## 

If you have problems with the installation, or see regressions, please reply to this post.

If you have a security-sensitive question, or you find further security problems, please mail the Plone/Zope Security Team at [security@plone.org](mailto:security@plone.org).
