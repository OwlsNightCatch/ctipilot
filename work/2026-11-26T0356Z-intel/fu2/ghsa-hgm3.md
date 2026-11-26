---
title: Predictable remember-me key allows administrator session forgery
author: Jodygarnett
url: https://github.com/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq
hostname: github.com
description: The remember-me cookie is signed with a key, together with the user name, expiry and stored password digest. This key was read from `security/config.xml` in the data directory, and the release dat...
sitename: GitHub
date: "2026-11-23"
categories: ['repository:2751199']
fingerprint: "294ace149de74275"
language: en
image: https://opengraph.githubassets.com/025d21fb10c95640eaa3636e19de41f60cfcb11aed750ed97c92a7e1b737ac8b/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq
pagetype: object
filedate: "2026-11-26"
---
  
    The remember-me cookie is signed with a key, together with the user name, expiry and stored password digest. This key

was read from `security/config.xml` in the data directory, and the release data directory ships with the key

`geoserver`, which most installations never change. Anyone who knows the key and an administrator password digest,

for example from a file disclosure, could create a remember-me cookie that GeoServer accepts as an administrator

login, without knowing the password.

This was reported as step 4 of an unauthenticated remote command execution chain. At the request of the CVE Numbering Authority each step of the chain is fixed separately, released in GeoServer 3.0.2:

1. [CVE-2026-129244](https://github.com/geoserver/geoserver/security/advisories/GHSA-4v26-c537-jvxc): WFS stored query exception discloses data directory path
2. [CVE-2026-129243](https://github.com/geoserver/geoserver/security/advisories/GHSA-rv5g-g2r9-58rj): Service security rules bypassed with a prefixed service name such as x/WFS
3. [CVE-2026-120705](https://github.com/geoserver/geoserver/security/advisories/GHSA-39mw-5chv-jh47): Unauthenticated WFS GetFeatureById XML injection
4. CVE-2026-129245: Predictable remember-me key allows administrator session forgery
5. [CVE-2026-129242](https://github.com/geoserver/geoserver/security/advisories/GHSA-9wf2-fcgq-vxhq): Deserialization in JDBC user and role services allows administrator code execution

### Impact

An attacker who obtains an administrator password digest, through any file disclosure or a copy of the data

directory, can log in as that administrator. Changing the key in `security/config.xml` does not help when the same

file disclosure also reveals the key.

### Details

`GeoServerTokenBasedRememberMeServices` validates the cookie signature with the key from the `rememberMeService`

section of `security/config.xml`. The signature uses the stored password digest, not the password, so the digest

and key are enough to forge a cookie.

### Mitigation

Remove `rememberme` from the web filter chain (**Security > Authentication**, filter chain `web`).

Otherwise change the key in `security/config.xml` to a long random value, and protect the data directory from

disclosure.

### Resolution

Patched for:

- GeoServer 3.0.2
- GeoServer 2.28.6
- GeoServer 2.27.7

The remember-me key is no longer stored in the data directory: each node uses a random key, existing remember-me

cookies are invalidated on upgrade, and a cluster sets a shared key with the `GEOSERVER_REMEMBERME_KEY` application

property.

If you suspect exposure, change administrator passwords.

### References

The remember-me cookie is signed with a key, together with the user name, expiry and stored password digest. This key

was read from `security/config.xml` in the data directory, and the release data directory ships with the key

`geoserver`, which most installations never change. Anyone who knows the key and an administrator password digest,

for example from a file disclosure, could create a remember-me cookie that GeoServer accepts as an administrator

login, without knowing the password.

This was reported as step 4 of an unauthenticated remote command execution chain. At the request of the CVE Numbering Authority each step of the chain is fixed separately, released in GeoServer 3.0.2:

## Impact

An attacker who obtains an administrator password digest, through any file disclosure or a copy of the data

directory, can log in as that administrator. Changing the key in `security/config.xml` does not help when the same

file disclosure also reveals the key.

## Details

`GeoServerTokenBasedRememberMeServices` validates the cookie signature with the key from the `rememberMeService`

section of `security/config.xml`. The signature uses the stored password digest, not the password, so the digest

and key are enough to forge a cookie.

## Mitigation

Remove `rememberme` from the web filter chain (**Security > Authentication**, filter chain `web`).

Otherwise change the key in `security/config.xml` to a long random value, and protect the data directory from

disclosure.

## Resolution

Patched for:

The remember-me key is no longer stored in the data directory: each node uses a random key, existing remember-me

cookies are invalidated on upgrade, and a cluster sets a shared key with the `GEOSERVER_REMEMBERME_KEY` application

property.

If you suspect exposure, change administrator passwords.

## References
