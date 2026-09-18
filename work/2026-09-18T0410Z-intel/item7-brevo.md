---
title: Security Incident - ClickFix - Brevo Status
url: https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3
hostname: brevo.com
description: The issue has been resolved and all systems are safe. A post-mortem has been published.
sitename: Brevo Status
date: "2026-09-14"
---
Write-up

Security Incident - ClickFix

Post-mortem: malicious "ClickFix" script served via Brevo's Cloudflare account

Date: 14 September 2026 Impact window: 15:01 to 20:30 UTC, 5h29 Status: Resolved. Hardening ongoing.

Summary

On 14 September 2026, an attacker used a compromised Brevo Cloudflare API key to deploy a Cloudflare Worker on our account. For about five and a half hours, the Worker injected a malicious script into pages of brevo.com and sibforms.com and into three JavaScript files that customers embed on their own websites. The script showed selected visitors a fake "Cloudflare, verify you are human" page that instructed them to paste and run a command on their computer, a social-engineering technique known as ClickFix. Brevo's application at app.brevo.com was not affected. No Brevo systems were modified at their source, the content was altered in transit at our CDN edge.

What customers and visitors may have seen

A full-screen Cloudflare-branded page, sometimes appearing right after a genuine Cloudflare checkbox, asking the visitor to press Win+R, then Ctrl+V, then Enter. Following those steps ran a command placed on the clipboard by the script, which downloaded malware onto the visitor's Windows computer. The page was shown selectively, so most visitors and repeat visits saw nothing.

On WordPress sites that embedded a Brevo widget, if a visitor was logged in as a WordPress administrator, the script also attempted to silently install and activate a plugin on that site.

Affected surfaces and window (UTC, 14 September)

The ClickFix was active on following URLs from 16:07 UTC until 20:30.

- brevo.com, sendinblue.com, login/account/my/onboarding.brevo.com
- sibforms.com and the Brevo forms script
- Brevo Conversations widget, Brevo SDK loader

Not affected: app.brevo.com, the Brevo API, email sending, and customer account data held in Brevo.

Timeline (UTC, 14 September)

- 14:23 Attacker creates the first hostname used to serve the script, on a Brevo-owned domain.
- 14:28 Attacker deploys the Worker and tests it on low-traffic Brevo domains.
- 14:42 Worker routed to brevo.com.
- 15:01 Worker routed to all of brevo.com. Impact begins.
- 16:07 Worker updated to also append a loader to the three embedded JavaScript files, and routed to sibforms.com.
- 19:33 Security incident opened, investigation begins.
- 20:30 Malicious Worker and its routes removed. Compromised API key and the credentials created with it revoked. Injection stops. Impact ends.
- 20:42 Independent verification confirms all affected pages and scripts are clean.
- Following hours Attacker hostnames deleted, edge caches purged.
- 15 September Customer notification begins.

Our investigation indicates the key was first misused in late August 2026. We have found no injection of malicious content into customer-facing pages before 14 September.

Root cause

A long-lived Cloudflare API key with full account permissions was stored in application source code and was obtained by the attacker. With it, they could create Workers, routes and DNS records on Brevo's zones without triggering an alert. Because the Worker rewrote responses at the edge and removed security headers such as Content-Security-Policy, our origin servers and files remained unmodified and standard integrity checks did not detect the change.

What we have done

- Removed the malicious Worker, its routes, and all attacker-created hostnames.
- Revoked the compromised key and all credentials created with it, and reviewed every credential and member on the Cloudflare account.
- Purged edge caches and verified every affected page and script serves clean content.
- Removed the hardcoded credential from source code and replaced it with narrowly scoped, short-lived tokens.

What we are changing

- Adopting HashiCorp Vault as the single store for all Cloudflare keys and tokens, with automatic rotation and no credentials in source code or configuration files.
- Alerting on every Cloudflare audit event that changes Workers, routes, DNS or account access, reviewed by the security team.
- Cloudflare logs streamed to our security monitoring platform.
- Integrity protection for versioned embedded assets where technically possible, and regular external scanning of our public pages and scripts for injected content.
- A review of all third-party edge configurations across Brevo domains.

What we ask you to do

- If you or a visitor ran the pasted command, treat that computer as compromised: disconnect it, run a full antivirus scan, and change passwords used on it, starting with your Brevo password.
- If your WordPress site is loading Brevo scripts and an administrator visited it on 14 September while logged in, check for any plugin installed or activated that day, remove it, and change administrator passwords.
- If you logged in to Brevo via brevo.com on 14 September, change your password and review your API keys as a precaution.
- The Conversations widget, SDK and forms are safe to use. They were never modified at their source.

We are sorry for the concern and disruption this caused.
