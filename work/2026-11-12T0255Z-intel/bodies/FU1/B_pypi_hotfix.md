---
title: Products.PloneHotfix20261110
url: https://pypi.org/project/Products.PloneHotfix20261110/
hostname: pypi.org
description: Various Plone hotfixes, 2026-11-10
sitename: PyPI
date: "2026-11-10"
fingerprint: "344b8ecd8cb17090"
---
# Plone hotfix, 2026-11-10

It is a chain of several issues, which are fixed separately:

- Products.CMFEditions: missing security declarations on the conditional modifiers in portal\_modifier. Anonymous users could change their TALES condition, which is evaluated when content is versioned. See GHSA-67qm-q795-jh7h.
- Products.CMFPlone: allow\_module was used on whole modules (Products.CMFPlone.utils, Products.CMFPlone.browser.navtree, OFS.ObjectManager), which made everything those modules import available to restricted code, for example os. allow\_class could be called from restricted code. See GHSA-92qw-564p-pmg6.
- Products.MimetypesRegistry: allow\_module on the common module also made allow\_class available to restricted code. See GHSA-xcj2-cmp9-fj62.
- plone.batching: allow\_module made allow\_class and allow\_module available to restricted code. See GHSA-6hcx-c235-cxh3.
- plone.restapi: allow\_module("json") made json.dump and json.load available to restricted code. These call the protected write and read methods of any object without security checks. See GHSA-vgxm-pwch-89q6.

Each fix is only applied when the package is installed. When a package is not installed, the hotfix skips that fix and logs it.

# Compatibility

This hotfix should be applied to the following versions of Plone:

- Plone 6.2, 6.1 and 6.0, on Python 3
- Plone 5.2, on Python 2.7 and Python 3
- Plone 5.1, 5.0 and 4.3, on Python 2.7

The fixes will be included in the next releases of the affected packages. When you use fixed versions of all these packages, you do not need this hotfix, but it does no harm either.

## Plone 5.2 and older

Note that Plone 5.2 and older have been out of security support since several years.
In this case we made an exception.
If you still use such an unsupported Plone version, your site may have vulnerabilities that have been published the past few years.
You should upgrade to Plone 6 soon.
See the [Plone release schedule](https://plone.org/download/release-schedule).

## Python 3.10 and older

Python version 3.10 and older are out of security support from Python itself.
You should upgrade to Python 3.11 or higher soon.
See [python.org](https://www.python.org/downloads/).

# Installation

Choose one of these ways, then restart all Zope instances.

- Buildout: add Products.PloneHotfix20261110 to the eggs of your instance and run buildout.
- pip: pip install Products.PloneHotfix20261110.
- Manual, for old Plone versions 5.1 or earlier: copy the Products/PloneHotfix20261110 folder from the source distribution into the products directory of your instance, for example the directory that the products option of plone.recipe.zope2instance points to. No buildout run is needed.

## Plone 6.2

If you use Plone 6.2, especially if you install it using zc.buildout, you may get an error like this on startup:

ModuleNotFoundError: No module named 'Products.PageTemplates'

It can be a different module within the Products namespace. You can fix this by installing a helper package:

bin/pip install horse-with-no-namespace

See the [Plone 6.2 upgrade guide](https://6.docs.plone.org/backend/upgrading/version-specific-migration/upgrade-to-62.html#move-to-native-namespaces).

# What the hotfix changes

- Module security
- The modules that were opened with allow\_module are closed again. Only explicit names stay available to restricted code (Python Scripts, page templates, TALES expressions). Products.CMFPlone calls allow\_module in its own initialize function, which Zope calls after the hotfix is imported, and since Plone 6.0 a second time at the end of the product initialization. So the hotfix closes the modules again in its own initialize function and at the end of startup, before Zope serves any request. For compatibility with the skin scripts and templates of Plone 4.3 to 6.0 these names also stay available: PloneMessageFactory, PloneLocalesMessageFactory and Batch from Products.CMFPlone, getNavigationRoot from Products.CMFPlone.browser.navtree and isLinked from Products.CMFPlone.utils. If your own Python Scripts import other names from these modules, they now get an Unauthorized error. Declare the names you need in your own add-on with ModuleSecurityInfo(module).declarePublic(name). Never use allow\_module for this.
- AccessControl
- allow\_module, allow\_class, allow\_type, ClassSecurityInfo, ModuleSecurityInfo and setSecurityPolicy can never be called from restricted code. The same is true for the os, sys, subprocess and shutil modules.
- CMFEditions modifiers
- edit of the conditional modifiers requires the Manage portal permission, the other methods require View management screens, and the internal hooks of the size guard modifiers are private.

# Q&A

- Q: How can I confirm that the hotfix is installed correctly and my site is protected?
- A: On startup, the hotfix logs messages like these to the Zope event log: INFO \[Products.PloneHotfix20261110\] Applied accesscontrol patch (GHSA-92qw-564p-pmg6). INFO \[Products.PloneHotfix20261110\] Applied cmfplone patch (GHSA-92qw-564p-pmg6). INFO \[Products.PloneHotfix20261110\] Closed module Products.MimetypesRegistry (was opened with allow\_module). INFO \[Products.PloneHotfix20261110\] Applied mimetypesregistry patch (GHSA-xcj2-cmp9-fj62). INFO \[Products.PloneHotfix20261110\] plone.restapi is not installed: restapi patch not needed. ... INFO \[Products.PloneHotfix20261110\] Hotfix installed. INFO \[Products.PloneHotfix20261110\] Closed module Products.CMFPlone.utils (was opened with allow\_module). ... INFO \[Products.PloneHotfix20261110\] No changed modifier conditions found. The exact messages depend on the packages you use. If a patch fails, the hotfix logs an error that says “Could not apply”. This may mean that you have a non-standard installation. Please investigate.
- Q: What does the warning “POSSIBLE ATTACK: MODIFIED VERSIONING CONDITIONS FOUND” mean?
- A: At the end of startup the hotfix checks the TALES conditions of the modifiers in portal\_modifier of every Plone site. The hotfix stops new attacks, but a condition that an attacker has already changed stays in the database. If any condition differs from the default, the hotfix logs one warning instead of “No changed modifier conditions found.” You should investigate whether this difference is intentional or not.

# Changelog

## 1.0 (2026-11-10)

- Initial release.

## Metadata

## Release files for Products.PloneHotfix20261110 1.0

For a detailed explanation of source distributions (sdists) and built distributions (wheels), please see the [package formats documentation](https://packaging.python.org/en/latest/discussions/package-formats/#package-formats).

### Source distribution (sdist)

| Source distribution for Products.PloneHotfix20261110 1.0 |  |  |  |  | 
|---|---|---|---|---|
| File | Size | Uploaded | Provenance | Actions | 
|---|---|---|---|---|
|  [products\_plonehotfix20261110-1.0.tar.gz](https://files.pythonhosted.org/packages/b3/b1/2920963ca9f49d2d499ce3c54b69cf4edc40e8331f93ae1537647eb495a0/products_plonehotfix20261110-1.0.tar.gz) | 19.6 kB |  | Without provenance | [Details for products\_plonehotfix20261110-1.0.tar.gz](https://pypi.org#products_plonehotfix20261110-1.0.tar.gz) | 

### Built distribution (wheel)

| Table of built distributions (wheels) for Products.PloneHotfix20261110 1.0 |  |  |  |  | 
|---|---|---|---|---|
| File | Interpreter | ABI | Platform | Actions [Reset](https://pypi.org/project/Products.PloneHotfix20261110/#files) | 
|---|---|---|---|---|
|  [products\_plonehotfix20261110-1.0-py2.py3-none-any.whl](https://files.pythonhosted.org/packages/05/12/5f341b4a3b4ac7b6b0e2c0d5919c47dcad47345c0c227536e77611f2cf8a/products_plonehotfix20261110-1.0-py2.py3-none-any.whl) | Python 2, Python 3 | none | any | [Details for products\_plonehotfix20261110-1.0-py2.py3-none-any.whl](https://pypi.org#products_plonehotfix20261110-1.0-py2.py3-none-any.whl) | 

**Total release size:** 35.6 kB

## [Release files](https://pypi.org#files)
    / products\_plonehotfix20261110-1.0.tar.gz

| Download URL |                           [products\_plonehotfix20261110-1.0.tar.gz](https://files.pythonhosted.org/packages/b3/b1/2920963ca9f49d2d499ce3c54b69cf4edc40e8331f93ae1537647eb495a0/products_plonehotfix20261110-1.0.tar.gz)            | 
|---|---|
| Size | 19.6 kB | 
| Tags | Source | 
| SHA-256 checksum [How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode) | ```              90d22a101cca7c421b8c1236f04242a116f49b284db98e5892d401acc1b0b9c6                         ```  | 
| BLAKE2b-256 checksum [How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode) | ```              b3b12920963ca9f49d2d499ce3c54b69cf4edc40e8331f93ae1537647eb495a0                         ```  | 
| Upload date |  | 
| Uploaded using Trusted Publishing? [What is trusted publishing?](https://docs.pypi.org/trusted-publishers/) | No | 
| Uploaded via | `twine/7.0.0 CPython/3.14.10` | 

## [Release files](https://pypi.org#files)
    / products\_plonehotfix20261110-1.0-py2.py3-none-any.whl

| Download URL |                           [products\_plonehotfix20261110-1.0-py2.py3-none-any.whl](https://files.pythonhosted.org/packages/05/12/5f341b4a3b4ac7b6b0e2c0d5919c47dcad47345c0c227536e77611f2cf8a/products_plonehotfix20261110-1.0-py2.py3-none-any.whl)            | 
|---|---|
| Size | 16.1 kB | 
| Tags | Python 2 Python 3 | 
| SHA-256 checksum [How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode) | ```              fee8903fcee676f00879c32cb74b9a449836ddb13264089b323a6313fe3cbe47                         ```  | 
| BLAKE2b-256 checksum [How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode) | ```              05125f341b4a3b4ac7b6b0e2c0d5919c47dcad47345c0c227536e77611f2cf8a                         ```  | 
| Upload date |  | 
| Uploaded using Trusted Publishing? [What is trusted publishing?](https://docs.pypi.org/trusted-publishers/) | No | 
| Uploaded via | `twine/7.0.0 CPython/3.14.10` | 

## Security for Products.PloneHotfix20261110 1.0

### Provenance

**Provenance** describes where a file came from. On PyPI, provenance is shared via **attestations**, which provide a verifiable record of the build or publishing details. [View details, limitations and caveats.](https://docs.pypi.org/using-pypi/package-security/provenance/)

#### No provenance found

None of the files in this release were uploaded with provenance metadata.

### A note on package security

PyPI is a repository for distributing packages, not a service for auditing them. While third-party security researchers and our staff do their best to detect and remove malicious packages, PyPI cannot guarantee the quality, security or suitability of any given package.

To learn more about protecting yourself from malicious actors, visit our [package security documentation](https://docs.pypi.org/using-pypi/package-security/introduction/).
