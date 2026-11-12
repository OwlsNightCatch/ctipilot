---
title: Protecting Firefox users following the compromise of eMudhra intermediate certificates – Mozilla Security Blog
author: Christoph Kerschbaumer
url: https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates
hostname: mozilla.org
description: On Saturday, October 17, at 20:06 UTC, Mozilla received a report that private keys associated with eight eMudhra intermediate certificates had been compromised. These keys could allow attackers to issue ...
sitename: Mozilla Security Blog
date: "2026-10-20"
categories: ['Security']
fingerprint: fd6ee1863cb0f66d
license: Creative Commons license
---
On Saturday, October 17, at 20:06 UTC, Mozilla received a report that private keys associated with eight eMudhra intermediate certificates had been compromised. These keys could allow attackers to issue fraudulent HTTPS certificates for websites they do not control. An attacker who could intercept a user’s connection could use those certificates to impersonate websites and potentially read or modify traffic.

Mozilla engineers responded immediately, blocking the affected certificates in Firefox using [OneCRL](https://blog.mozilla.org/security/2015/03/03/revoking-intermediate-certificates-introducing-onecrl/), Mozilla’s centralized list of revoked certificates. OneCRL delivers this protection without requiring users to update or restart Firefox.

By 22:59 UTC that same day, in less than 3 hours after we received the report, the updated OneCRL distribution was complete for all Firefox users with standard configurations.

Today, we are also releasing [Firefox 158.0.1](https://www.firefox.com/en-US/firefox/158.0.1/releasenotes/) for Desktop and Android, along with [Firefox ESR 115.43.1](https://www.firefox.com/en-US/firefox/115.43.1/releasenotes/) and [Firefox ESR 153.5.1](https://www.firefox.com/en-US/firefox/153.5.1/releasenotes/). These releases will distribute this protection for a minority of users whose custom settings may have prevented them from receiving the OneCRL update.

We are also updating the trusted certificate list in NSS ([NSS 3.131.1](https://groups.google.com/a/mozilla.org/g/dev-tech-crypto/c/vSxZxnOMMvs)) to remove the root certificate that signed the affected intermediates. Firefox is already protected through OneCRL, but this additional update helps protect other applications that use Mozilla’s trust store or versions derived from it and do not receive OneCRL updates.

Mozilla believes everyone has a fundamental right to security and privacy online. We remain committed to defending those rights and acting quickly to protect users.

Transparency is essential to trust. We will share more information as soon as circumstances allow.

**Update added October 21:** On Wednesday, October 21, at 08:29 UTC, we released an additional update for Firefox for Android ([158.0.2](https://www.firefox.com/en-US/firefox/android/158.0.2/releasenotes/)) to fix an issue where some clients were not applying changes to the bundled OneCRL blocklist immediately after startup.
