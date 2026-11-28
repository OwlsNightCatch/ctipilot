---
title: Missing second-factor check on authenticator enrollment in Login V2 (MFA bypass)
author: Livio-A
url: https://github.com/zitadel/zitadel/security/advisories/GHSA-qqv8-37gw-ww2q
hostname: github.com
description: "### Summary ZITADEL’s hosted **Login V2** UI allowed an attacker who knows a user’s first factor — typically the password — to add a new authenticator to that user’s account without completing t..."
sitename: GitHub
date: "2026-11-18"
categories: ['repository:247714750']
fingerprint: "9c7cffbb05ddc780"
language: en
image: https://opengraph.githubassets.com/e7e8c49f2832b6ba74bad732147613948a003343300580d10c1f52daadf39b29/zitadel/zitadel/security/advisories/GHSA-qqv8-37gw-ww2q
pagetype: object
filedate: "2026-11-28"
---
    ### Summary

ZITADEL’s hosted **Login V2** UI allowed an attacker who knows a user’s first factor — typically the password — to add a new authenticator to that user’s account without completing the second factor the user had already enrolled. A newly registered passkey satisfies multi-factor authentication on its own, so the attacker could then sign in with it and was never asked for the victim’s **TOTP**, **OTP-SMS**, **OTP-Email** or **U2F** factor.

Login V2 accepted authenticator enrollment as soon as the session had a verified first factor, without checking whether the second factor already enrolled on the account had been verified in that session.

### Impact

An attacker who knows a user’s password (or can sign in as the user at a linked external identity provider) can:

- **Bypass the user’s enrolled second factor** (TOTP, OTP-SMS, OTP-Email or U2F) by adding an authenticator of their own — a passkey, or another second factor they then choose at sign-in — and sign in to applications as that user.
- **Keep access after the password has been changed**, for example through an attacker-controlled passkey, which needs neither the password nor the victim’s second factor.
- **Obtain tokens that report multi-factor authentication** — after a sign-in with the attacker’s passkey, the ID token’s `amr` claim contains `mfa`, misleading relying parties that use it for step-up decisions.

The setup pages could be opened directly by their URL (for example `/ui/v2/login/passkey/set`) while the login was waiting for the second factor. Neither **Force MFA** nor disallowing passkeys in the login policy prevented this.

This affects applications that authenticate users through ZITADEL’s hosted **Login V2** UI (OIDC/SAML).

The attacker must already hold the user’s first factor; the issue does **not** reveal or bypass the password itself. Users without an enrolled second factor are not additionally exposed, as their first factor alone already grants access. **Login V1** is not affected: it only allows enrolling a second factor on its MFA setup step, which is never offered to a user who already has one.

**Scope note:** This issue affects the hosted **Login V2** UI only, for all organizations of an instance that use it; it does not cross instances. It is the authenticated counterpart to [GHSA-45f2-5q3r-xgg6](https://github.com/zitadel/zitadel/security/advisories/GHSA-45f2-5q3r-xgg6), which allowed enrollment from a session that had not verified any factor. Custom login UIs built on the Session and User APIs make this enrollment decision themselves and should likewise require the user’s enrolled second factor to be verified before registering a new authenticator.

### Affected Versions

Systems running one of the following versions are affected:

- **4.x:** `4.0.0` through `4.20.4` (including RC versions)

### Patches

The vulnerability has been addressed in the latest releases. Login V2 now only allows adding an authenticator — a passkey, TOTP, OTP-SMS, OTP-Email, U2F or a link to an external identity — when the session has verified a second factor already enrolled on the account, or was authenticated with a passkey. Users without a second factor can still set one up after their first factor, as required by **Force MFA**. In addition, the setup pages now only accept authenticator types allowed by the organization’s login policy.

### Workarounds

The recommended solution is to upgrade to a patched version. There is no configuration that fully closes this gap on unpatched versions; enabling **Force MFA** or disallowing passkeys in the login policy does **not** mitigate it.

After upgrading, administrators may want to review authenticators (passkeys, second factors and identity provider links) recently added to accounts and remove any the user does not recognize.

### Questions

If you have any questions or comments about this advisory, please email us at [security@zitadel.com](mailto:security@zitadel.com)

### Credits

Thanks to Lucas Dodgson from InfoGuard Labs ([@lucasdodgson](https://github.com/lucasdodgson)), Mario Schlipf ([@marioschlipf](https://github.com/marioschlipf)) and a security researcher who asked not to be named for independently finding and reporting the vulnerability.

## Summary

ZITADEL’s hosted **Login V2** UI allowed an attacker who knows a user’s first factor — typically the password — to add a new authenticator to that user’s account without completing the second factor the user had already enrolled. A newly registered passkey satisfies multi-factor authentication on its own, so the attacker could then sign in with it and was never asked for the victim’s **TOTP**, **OTP-SMS**, **OTP-Email** or **U2F** factor.

Login V2 accepted authenticator enrollment as soon as the session had a verified first factor, without checking whether the second factor already enrolled on the account had been verified in that session.

## Impact

An attacker who knows a user’s password (or can sign in as the user at a linked external identity provider) can:

Bypass the user’s enrolled second factor(TOTP, OTP-SMS, OTP-Email or U2F) by adding an authenticator of their own — a passkey, or another second factor they then choose at sign-in — and sign in to applications as that user.Keep access after the password has been changed, for example through an attacker-controlled passkey, which needs neither the password nor the victim’s second factor.Obtain tokens that report multi-factor authentication— after a sign-in with the attacker’s passkey, the ID token’s`amr`claim contains`mfa`, misleading relying parties that use it for step-up decisions.
The setup pages could be opened directly by their URL (for example `/ui/v2/login/passkey/set`) while the login was waiting for the second factor. Neither **Force MFA** nor disallowing passkeys in the login policy prevented this.

This affects applications that authenticate users through ZITADEL’s hosted **Login V2** UI (OIDC/SAML).

The attacker must already hold the user’s first factor; the issue does **not** reveal or bypass the password itself. Users without an enrolled second factor are not additionally exposed, as their first factor alone already grants access. **Login V1** is not affected: it only allows enrolling a second factor on its MFA setup step, which is never offered to a user who already has one.

**Scope note:** This issue affects the hosted **Login V2** UI only, for all organizations of an instance that use it; it does not cross instances. It is the authenticated counterpart to GHSA-45f2-5q3r-xgg6, which allowed enrollment from a session that had not verified any factor. Custom login UIs built on the Session and User APIs make this enrollment decision themselves and should likewise require the user’s enrolled second factor to be verified before registering a new authenticator.

## Affected Versions

Systems running one of the following versions are affected:

4.x:`4.0.0`through`4.20.4`(including RC versions)
## Patches

The vulnerability has been addressed in the latest releases. Login V2 now only allows adding an authenticator — a passkey, TOTP, OTP-SMS, OTP-Email, U2F or a link to an external identity — when the session has verified a second factor already enrolled on the account, or was authenticated with a passkey. Users without a second factor can still set one up after their first factor, as required by **Force MFA**. In addition, the setup pages now only accept authenticator types allowed by the organization’s login policy.

4.x: Upgrade to
## Workarounds

The recommended solution is to upgrade to a patched version. There is no configuration that fully closes this gap on unpatched versions; enabling **Force MFA** or disallowing passkeys in the login policy does **not** mitigate it.

After upgrading, administrators may want to review authenticators (passkeys, second factors and identity provider links) recently added to accounts and remove any the user does not recognize.

## Questions

If you have any questions or comments about this advisory, please email us at security@zitadel.com

## Credits

Thanks to Lucas Dodgson from InfoGuard Labs (@lucasdodgson), Mario Schlipf (@marioschlipf) and a security researcher who asked not to be named for independently finding and reporting the vulnerability.
