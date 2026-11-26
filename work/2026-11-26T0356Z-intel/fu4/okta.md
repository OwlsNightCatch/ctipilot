---
title: AI agents prefer specific disposable email services during identity attacks
url: https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/
hostname: okta.com
description: A joint investigation by Okta Threat Intelligence and Permiso's P0 Labs has identified that when asked to create accounts for security testing purposes, AI agents almost universally choose the services of one specific provider.
sitename: Okta
date: "2026-11-23"
tags: ['Credential Stuffing', 'Threat Intelligence', 'Password Spray', 'Fraudulent Registration', 'Blog Post', 'AI']
fingerprint: a5d121d30843b2c5
language: en
image: https://www.okta.com/content/dam/okta-www/en_us/blog/threat-intelligence/agents-prefer-disposable-email-service/11192026-AI-Agents-Disposable-Emails.png
pagetype: website
filedate: "2026-11-26"
---
## Executive Summary

A joint investigation by Okta Threat Intelligence and Permiso's P0 Labs has identified that when asked to create accounts for security testing purposes, AI agents frequently choose the services of one specific family of disposable email services.

Starting in June 2026 and accelerating at scale throughout October and November 2026, Okta Threat Intelligence observed AI agents registering accounts with disposable email addresses on Auth0 tenants and Okta organizations that allow public self-service registration. This activity is almost certainly malicious and was often observed by customers reporting attacks on their applications.

The registered email addresses belonged primarily to domains associated with mail\[.\]tm, which provisions receive-only inboxes through a free, public and well-documented API and rotates the mailbox domains it offers. P0 Labs observed the ARTEX, Cairn, CyberStrikeAI and pentestcode frameworks each selecting mail\[.\]tm at run time rather than from packaged agent tooling, probing which disposable domains a target accepts and only falling back to other providers when blocked.

The use of these services always occurred within a short window of activity that included other agentic reconnaissance and intrusion attempts against the same entities. Disposable-domain signups are therefore likely to be an early indicator that AI agents have been tasked with performing attacks against an organization.

## Threat Analysis

Okta Threat Intelligence observed the following mailbox domains used against Auth0 tenants and Okta organizations that support public self-service registration.

- uberip\[.\]com
- maxxspace\[.\]com
- fldubai\[.\]com

mail\[.\]tm and the services that share its API currently expose one active mailbox domain at a time through the public /domains endpoint.

Each domain returned by api\[.\]mail\[.\]tm/domains replaced the one before it: maxxspace\[.\]com was the sole domain returned on September 13, 2026, and fldubai\[.\]com has been the sole domain returned since October 30, 2026.

In a data set containing attacker tooling, P0 Labs identified mail\[.\]tm use on eighty percent of attacker hosts where disposable email was found, spanning the ARTEX, Cairn, CyberStrikeAI and pentestcode frameworks.

mail\[.\]tm provides receive-only disposable inboxes at no cost. An address is provisioned on first request, in the browser or through the API, and the API requires no account registration or key. Its REST API, defined in the machine-friendly OpenAPI specification, allows a mailbox to be created, a token obtained and messages polled for one-time codes entirely from a script.

We reported agentic use of these domains in a [earlier threat advisory](https://security.okta.com/product/oktathreatintelligence/agentic-attack-tools-used-to-accelerate-reconnaissance-of-identity-flows), and Okta Threat Intelligence's analysis of the [swarmtraces data set](https://swarmtraces.org) indicates agentic use of the mail\[.\]tm family as early as June 2026.

### Why agents converge on the same API-driven services

Our research demonstrates that AI agents very likely select mail\[.\]tm at run time rather than from packaged tooling. We can say this because four distinct autonomous penetration testing frameworks — ARTEX, Cairn, CyberStrikeAI and pentestcode — each arrived at the same email provider independently during tests by P0 Labs.

Both properties described above — no account registration or preexisting API key, and a documented REST API that can be driven entirely from a script — remove the setup cost that would otherwise make a provider impractical for an agent to adopt mid-task. P0 Labs and Okta Threat Intelligence recently analyzed open directories on attacker infrastructure, which included an agent's reasoning and tool output. The example below shows an agent reaching for mail\[.\]tm after a similar service failed:

```
1secmail API is gone (404). Try mail.tm (needs account creation 
via API — possible programmatically): POST 
https://api.mail.tm/accounts {address, password} then get token, 
then poll /messages. Domains available via GET /domains.
```
Let's try mail.tm. Or use mail.gw. Let me try mail.tm API.
Alternatively use "temporary-mail" services with public inbox 
like mailinator: https://www.mailinator.com/api/v2/domains/public/inboxes/... 
requires API token now.

Let's try mail.tm quickly.

Next, the agent ran this curl command:

curl -sS --max-time 20 "https://api.mail.tm/domains"

And recieved the following response:

```
{
```
"@context": "\/contexts\/Domain",

"@type": "hydra:Collection",

"hydra:totalItems": 1,

```
 "hydra:member": [{
```
"id": "6aa6b995482bea6f4a97f585",

"domain": "maxxspace.com",

"isActive": true,

"isPrivate": false,

"createdAt": "2026-09-13T00:00:00+00:00",

"updatedAt": "2026-09-13T00:00:00+00:00"

}\]

}

This response is significant for our analysis because it demonstrates that when an agent polled the mail\[.\]tm API on September 13, 2026, the service responded with a single domain: maxxspace\[.\]com.

As we have tracked agentic-driven account registrations, we noticed a change in the email domains used starting around October 30, 2026, when we began frequently observing the domain fldubai\[.\]com. When the domain in the API response changed, so too did the attackers' email domain.

The response also reveals that mail\[.\]tm is using the [Hydra Vocabulary](https://www.markus-lanthaler.com/hydra/), which is an open source framework designed for autonomous machine navigation. This allows agents to easily interact with mail\[.\]tm without writing custom code. Additionally, Hydra was released in 2013 as an open source tool and [included](https://index.commoncrawl.org/CC-MAIN-2014-10-index?url=www.markus-lanthaler.com%2Fhydra%2F&output=json) in the October 2014 [Common Crawl](https://index.commoncrawl.org) index, meaning that it is almost certainly in training data for all AI models we observed being used.

### Registration and probing in Auth0 and Okta logs

Because mail\[.\]tm exposes only one active mailbox domain at a time and replaces it periodically, a blocklist built from previously observed domains will very likely stop matching within weeks of being compiled. Our analysis of Auth0 telemetry supports this: signup activity tracks the domain currently returned by the mail\[.\]tm API.

Bot detection and CAPTCHA challenges were generally effective in stopping the observed activity. Sign-up attempts using mail\[.\]tm addresses in October 2026 were unable to pass an Auth0 bot-challenge and never reached email verification. CAPTCHA cannot stop all attempts, as agents can solve challenges based on things like images or proof-of-work. CAPTCHA challenges should not be viewed as a sufficient defense on their own.

### Disposable email providers are interchangeable

The mail\[.\]tm family was dominant but not exclusive. Agents also used mailinator, reading one-time codes through its API, as well as guerrillamail and emailnator. The substitutions matter more than the inventory:

- We observed an agent that found 1secmail returning errors pivoting immediately to mail\[.\]tm
- We observed an agent blocked at one target moved from mail\[.\]tm to tempmail\[.\]lol, and the APIs of temp-mail\[.\]io and dropmail\[.\]me were tested without being adopted.

Agents very likely treat disposable mail as an interchangeable capability and select on whichever API responds, which is consistent with provider choice being made during a task rather than fixed in tooling. These observations are drawn from attacker-side logs, and our conclusions are corroborated by analysis of our own telemetry.

## Recommendations

Tracking these patterns can assist in identifying when AI agents are targeting a specific organization. While these email domains are predominantly used in account registration/reconnaissance activity, we have observed that this account registration activity often occurs along with other agentic reconnaissance and intrusion attempts. Therefore, identifying use of these disposable email addresses with known agentic patterns can assist organizations in determining if they are being targeted by agents, giving them a heads-up that they need to look for successful intrusion attempts.

### Threat Intelligence

- Poll provider APIs like api\[.\]mail\[.\]tm/domains to receive a list of currently active disposable email domains.
- Continually update email domain reputation from open source intelligence services and your own logs.

### Auth0

- [Block signups from disposable domains using Auth0 Actions](https://support.auth0.com/center/s/article/Block-or-deny-user-sign-up-by-email-domain).
- Implement [detections](https://github.com/auth0/auth0-customer-detections/blob/5b3940da41120c9303cb4beae31526aa3e45862c/detections/risk_of_signup_fraud_by_disposable_domains.yml#L2) to monitor your tenant for signups from disposable email domains favored by attackers. Further detections are provided in the [Auth0 detection catalog](https://github.com/auth0/auth0-customer-detections/) on GitHub.
- Delete fraudulently registered accounts as soon as they are identified. If you identify a large number of fraudulent users, engage Auth0 support for assistance.
- [Block signups via API when allowing signups via Auth0 Universal Login](https://support.auth0.com/center/s/article/block-signups-via-api-while-allowing-signups-via-auth0-universal-login). Agents commonly register accounts by calling the Auth0 Authentication API directly, which can skip protections applied in Universal Login.
- Layer bot detection with CAPTCHA challenges, rate limiting and the recommended controls above. For tenants seeing this activity, CAPTCHA should be viewed as one layer in a defense-in-depth strategy.

### Okta Workforce Identity

- Allowing self-service registration is a prerequisite for many of the attacks described in this advisory. Disable or restrict it for workforce users.
- Deny or require higher assurance for requests from rarely-used networks. Okta [network zones](https://help.okta.com/en-us/content/topics/security/network/network-zones.htm) allow administrators to set policies that deny access to Okta-protected resources by geolocation (country), ASN, IP, or IP service category. IP service categories match IPs to known anonymizing services (VPNs, proxies).

### Okta Customer Identity

- Detect and deactivate disposable email addresses used in self-service registrations using [Okta Customer Detections](https://github.com/okta/customer-detections/tree/cda718c3d3868778122cf25f7bd5a7fdf9d11db3/workflows/deactivate_ssr_users).
- Implement [self-service registration policies](https://help.okta.com/OIE/en-us/content/topics/itp/ssr-policy.htm) to block malicious agent signup using disposable email domains and further block registration from [risky network providers](https://help.okta.com/OIE/en-us/content/topics/itp/ssr-policy-configure.htm).
- Layer bot detection with CAPTCHA challenges, rate limiting and the recommended controls above. For organizations seeing this activity, CAPTCHA should be viewed as one layer in a defense-in-depth strategy.

## Further Reading

- Agentic attack tools accelerate reconnaissance of identity flows ([https://www.okta.com/blog/threat-intelligence/agentic-attack-tools-used-to-accelerate-reconnaissance-of-identi/](https://www.okta.com/blog/threat-intelligence/agentic-attack-tools-used-to-accelerate-reconnaissance-of-identi/))
- Multi-agent attack tools leave no stone unturned ([https://www.okta.com/blog/threat-intelligence/multi\_agent\_attack\_tools\_leave\_no\_stone\_unturned/](https://www.okta.com/blog/threat-intelligence/multi_agent_attack_tools_leave_no_stone_unturned/))

- AI-agent attack probed API misconfigurations (requires sign-in by security contact)
([https://security.okta.com/product/oktathreatintelligence/ai-agent-attack-probed-api-misconfigurations](https://security.okta.com/product/oktathreatintelligence/ai-agent-attack-probed-api-misconfigurations))
- Agentic attacks target overprivileged clients, insecure OAuth grants (requires sign-in by security contact)
([https://security.okta.com/product/oktathreatintelligence/agentic-attacks-target-overprivileged-clients-insecure-oauth-grants)](https://security.okta.com/product/oktathreatintelligence/agentic-attacks-target-overprivileged-clients-insecure-oauth-grants)

## A note on estimative language

Okta’s Threat Intelligence teams use the following terms to express likelihood or probability as outlined in the US Office of the Director of National Intelligence, Intelligence Community Directive 203 - Analytic Standards.

| Likelihood | Almost no chance | Very unlikely | Unlikely | Roughly even chance | Likely | Very likely | Almost certain(ly) | 
| Probability | Remote | Highly improbable | Improbable | Roughly even odds | Probable | Highly Probable | Nearly Certain | 
| Percentage | 1-5% | 5-20% | 20-45% | 45-55% | 55-80% | 80-95% | 95-99% | 


*Katie Nickels and Grayson Schermerhorn contributed to this research.*

*This advisory is provided for informational purposes only, without warranty or liability, does not constitute professional advice, and should not be relied upon to address every aspect of the subject discussed herein. Each customer remains solely responsible for consulting qualified advisors, evaluating its own cybersecurity risks, and selecting and implementing the security practices most appropriate for its specific operational needs.*
