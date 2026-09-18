---
title: Brevo supply-chain attack injected ClickFix scripts on customer sites
author: Bill Toulas
url: https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/
hostname: bleepingcomputer.com
description: Brevo confirmed that attackers stole a Cloudflare API key and used it to inject malicious ClickFix scripts into its websites and JavaScript files embedded on customer sites to distribute malware.
sitename: BleepingComputer
date: "2026-09-17"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Brevo, ClickFix, Supply Chain, Supply Chain Attack, Website,virus removal, malware removal, computer help, technical support']
---
Brevo confirmed that attackers stole a Cloudflare API key and used it to inject malicious ClickFix scripts into its websites and JavaScript files embedded on customer sites to distribute malware.

The customer relationship management and digital marketing company says the attackers used the API key to create a malicious Cloudflare Worker that modified content at the CDN edge for approximately five and a half hours on September 14.

The attack affected pages on brevo.com, sendinblue.com, login/account/my/onboarding.brevo.com, and sibforms.com. The Cloudflare worker also modified the Brevo forms script, Brevo Conversations widget, and the Brevo SDK loader scripts that customers embed on their websites.

In a [post-mortem published today](https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up), Brevo explained that attackers obtained a long-lived Cloudflare API key with full account permissions that had been hardcoded in application source code, which allowed them to create Cloudflare Workers, routes, and DNS records across Brevo's zones without triggering an alert.

"Because the Worker rewrote responses at the edge and removed security headers such as Content-Security-Policy, our origin servers and files remained unmodified and standard integrity checks did not detect the change," explained Brevo.

The company says the key may have been compromised as early as late August, but there's no evidence of prior malicious activity.

Upon detecting the compromise, Brevo removed the Worker and its routes, defining the exposure window as between 16:07 and 20:30 UTC.

In the hours that followed, the company revoked the compromised key and credentials created with it, removed the hardcoded credential from its source code, deleted attacker-controlled hostnames, and purged its edge caches.

Brevo says app.brevo.com, its API, email delivery infrastructure, and customer account data were not affected.

## Used in ClickFix attacks

The incident was [first reported](http://sansec.io/research/brevo-supply-chain-attack) by security firm Sansec, which reported that it may have impacted up to 100,000 websites that use the affected Brevo components.

Sansec says the incident began on September 14, 2026, between 16:05 and 20:13 UTC, but has now confirmed that all malicious subdomains stopped resolving on September 15, and Brevo files are now clean.

Visitors to these websites were shown a fake Cloudflare verification page, followed by ClickFix instructions urging them to run a command on Windows.

On WordPress websites embedding an affected Brevo widget, the script also checked whether the visitor was logged in as an administrator and attempted to upload a malicious plugin from `https://cdn10.sendibt1[.]com/p/wm.zip`.

While SanSec was not able to retrieve the archive, BleepingComputer found it uploaded to [VirusTotal](https://www.virustotal.com/gui/file/f359ab0d2f732b54dd3300065f4d6553f4df1b67454b71fd81197e26f02af4a8/relations) and can confirm it pretends to be a WordPress plugin named "Web Media Optimizer" but acts as a persistent backdoor and JavaScript loader.

Other domains BleepingComputer saw distributing the malicious WordPress plugin and scripts include `https://yelahaye[.]surf` and `https://boiseno[.]club`.

Once installed, it hides itself from the WordPress plugin list, copies itself into the must-use plugins directory for persistence, and periodically contacts the attacker-controlled 'https://glegchner.com/ads.php' server.

That URL is currently returning a Base64-encoded URL pointing to JavaScript that the plugin then injects into visitors' pages. The current Base64-encoded URL decodes to `https://corralos[.]beer/a412dkoq.js`, which the site injects to fetch a ClickFix lure to display.

The plugin also stores a backup copy of the last valid JavaScript URL so it can continue loading malicious code if the remote server becomes unavailable.

Finally, the plugin contains a hardcoded authentication key that allows attackers to generate a valid login session for a WordPress administrator account without knowing the account password.

On September 10, Brevo [disclosed a different SSO-related incident](https://status.brevo.com/incidents/01M266V1CZKJQNGZRNEGFD5CQE/write-up) where attackers hijacked customer accounts and launched phishing attacks targeting customers of companies using Brevo.

One high-profile victim was cryptocurrency wallet vendor [Trezor](https://www.bleepingcomputer.com/news/security/trezor-347-000-users-targeted-in-phishing-attacks-after-brevo-breach/), which reported on September 11 that phishing attacks reached 347,000 user email addresses and successfully compromised at least 2,500.

Brevo did not respond to BleepingComputer's questions as to whether the SSO incident and the Cloudflare compromise were connected.

WordPress administrators who visited an affected site while logged in on September 14 should check for unusual plugins installed or activated that day and remove them. If found, they should also rotate administrator passwords.

## 
            [Build your security blueprint for AI-powered attacks](https://hubs.li/Q04x67m50)
        

        Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed.

[Save your seat](https://hubs.li/Q04x67m50)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
