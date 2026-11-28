---
title: Unauthenticated account takeover via passkey enrollment on Login V1 and Login V2
author: Livio-A
url: https://github.com/zitadel/zitadel/security/advisories/GHSA-45f2-5q3r-xgg6
hostname: github.com
description: "### Summary ZITADEL’s hosted login UIs allowed an unauthenticated attacker who knows only a victim’s login name to register an attacker-controlled passkey (or other authenticator) on the victim’..."
sitename: GitHub
date: "2026-07-29"
categories: ['repository:247714750']
fingerprint: da75f38589babf84
language: en
image: https://opengraph.githubassets.com/c39c6ab9b20a1b26d6e2955db9055f32f5a90d14182a12e33f29b4862da4f061/zitadel/zitadel/security/advisories/GHSA-45f2-5q3r-xgg6
pagetype: object
filedate: "2026-11-28"
---
  
    ### Summary

ZITADEL’s hosted login UIs allowed an unauthenticated attacker who knows only a victim’s login name to register an attacker-controlled passkey (or other authenticator) on the victim’s account, then complete login as that user. Enrollment was accepted on an identify-only login session/request—after the username was submitted, but before any password or other primary factor was verified.

### Impact

An attacker who knows a valid login name can take over the corresponding account without knowing the password, using an existing passkey, completing MFA, or interacting with the victim.

This affects applications that authenticate users through ZITADEL’s hosted **Login V2** and/or legacy **Login V1** UI (OIDC/SAML). Existing passwords or second factors on the account do not prevent enrollment of the additional attacker-controlled authenticator.

Legitimate passkey registration via emailed init/registration codes is unaffected in intent; the vulnerability was that login flows accepted enrollment without that proof of possession (or a prior authentication).

### Affected Versions

Systems running one of the following versions are affected:

- **4.x:** `4.0.0` through `4.16.1` (including RC versions)
- **3.x:** `3.0.0` through `3.4.13` (including RC versions)

### Patches

The vulnerability has been addressed in the latest releases. Login V2 now requires a verified primary factor (or a legitimate onboarding/user-verification path) before authenticator enrollment. Login V1 no longer allows passwordless setup from an auth request and only accepts the emailed init-code registration path.

### Workarounds

The recommended solution is to upgrade to a patched version. There is no configuration that fully closes this gap on unpatched versions.

### Questions

If you have any questions or comments about this advisory, please email us at [security@zitadel.com](mailto:security@zitadel.com)

### Credits

Thanks to:

- Michael Wollner from Deutsche Telekom AG ([@Ibonok](https://github.com/Ibonok)) for reporting the Login V2 issue
- Lucas Dodgson from InfoGuard Labs ([@lucasdodgson](https://github.com/lucasdodgson)) for independently reporting the Login V1 and Login V2 issues
- [Dor Konis](https://github.com/dkonis), [Feras Daragma](https://github.com/FerasTr) and [Peleg Wasserman](https://github.com/pelegw) from GE Vernova
- Adam Korczynski from Ada Logics ([@AdamKorcz](https://github.com/AdamKorcz)) for reporting the Login V2 issue with the help of Anthropic

## Summary

ZITADEL’s hosted login UIs allowed an unauthenticated attacker who knows only a victim’s login name to register an attacker-controlled passkey (or other authenticator) on the victim’s account, then complete login as that user. Enrollment was accepted on an identify-only login session/request—after the username was submitted, but before any password or other primary factor was verified.

## Impact

An attacker who knows a valid login name can take over the corresponding account without knowing the password, using an existing passkey, completing MFA, or interacting with the victim.

This affects applications that authenticate users through ZITADEL’s hosted **Login V2** and/or legacy **Login V1** UI (OIDC/SAML). Existing passwords or second factors on the account do not prevent enrollment of the additional attacker-controlled authenticator.

Legitimate passkey registration via emailed init/registration codes is unaffected in intent; the vulnerability was that login flows accepted enrollment without that proof of possession (or a prior authentication).

## Affected Versions

Systems running one of the following versions are affected:

4.x:`4.0.0`through`4.16.1`(including RC versions)3.x:`3.0.0`through`3.4.13`(including RC versions)
## Patches

The vulnerability has been addressed in the latest releases. Login V2 now requires a verified primary factor (or a legitimate onboarding/user-verification path) before authenticator enrollment. Login V1 no longer allows passwordless setup from an auth request and only accepts the emailed init-code registration path.

4.x: Upgrade to3.x: Upgrade to
## Workarounds

The recommended solution is to upgrade to a patched version. There is no configuration that fully closes this gap on unpatched versions.

## Questions

If you have any questions or comments about this advisory, please email us at security@zitadel.com

## Credits

Thanks to:
