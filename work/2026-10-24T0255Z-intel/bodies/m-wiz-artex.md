---
title: "ARTEX in the Wild: Storm-0940 Expands Targeting of IT and Software Vendors | Wiz Blog"
author: Sapir Federovsky; Rami McCarthy
url: https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors
hostname: wiz.io
description: Wiz Research is tracking an ARTEX-using actor, overlapping with Storm-0940, across multiple targeted software vendors. Learn how the AI agent attacks Okta, Entra, and Cognito, and what it left behind in the logs.
sitename: wiz.io
date: "2026-10-22"
tags: ['Research', 'Threat Intel']
fingerprint: "2fd302c968dfb0bd"
---
ARTEX in the Wild: Storm-0940 Expands Targeting of IT and Software Vendors

Wiz Research is tracking an ARTEX-using actor, overlapping with Storm-0940, across multiple targeted software vendors. Learn how the AI agent attacks Okta, Entra, and Cognito, and what it left behind in the logs.

Throughout October 2026, we identified an actor using tooling associated with ARTEX, an autonomous AI penetration-testing agent, to target multiple IT and software vendors. The activity focused on identity providers (Okta, Entra, Cognito) and abuse of Microsoft 365 integrations. We observed repeated attempts to uncover authentication bypasses, enumerate APIs, and access customer data (of the targeted vendors) across multiple environments.

However, we have additionally observed the same infrastructure, tooling, and attack patterns targeting the sector as a whole. Pivoting on identified TTPs and IOCs, we have also identified the same actor expanding their attempted supply chain compromises into other software sectors.

In this blog, we will describe the repeatable patterns and methodologies the ARTEX-using actor applied across multiple environments and cloud providers, with examples taken from real world attacks.

What is ARTEX?

ARTEX is an open-source autonomous penetration testing framework. A Chinese developer published it on GitHub in July 2026, and it won Baidu's "Agent+" red team challenge that September. In practice, an operator supplies a target and an objective. A planner agent then chooses the next step, worker agents run tools like nmap, curl, and Impacket, and every result feeds a shared graph of assets and findings.

Across the investigated environments, we observed a consistent sequence of reconnaissance and attack attempts:

Map the application: Download JavaScript bundles, exposed source maps, runtime configurations, and Swagger/OpenAPI documentation to discover internal API routes and application functionality.

Probe authentication: Repeatedly initiate sign-in flows, manipulate OAuth callbacks and state parameters, test unsigned JWTs, and probe SSO and Microsoft 365-specific endpoints.

Attack identity providers and login flows: Password-spray corporate Okta and Entra ID environments, and target internal and proprietary application login pages.

Test tenant isolation: Register accounts using disposable email addresses where possible, then manipulate predictable identifiers to probe for broken access controls and unauthorized cross-tenant data access.

Adapt to defense mechanisms: Rotate IP addresses when blocked, and constantly circulate user agents.

What it looked like in the logs

We analyzed these attack patterns using HTTP access logs collected via Wiz Agentless Workload Detection, alongside identity provider logs such as AWS Cognito events, Entra sign-in activity, and Okta authentication logs.

Targeting Internal Applications

The agent's first move across all observed instances of the attack was always to read the application itself. Requests like these showed up minutes after first contact:

GET /packs/js/main-3a9f...js.mapGET /assets/config.jsonGET /env.jsGET /swagger/?format=openapi

Not long after, it started calling internal API routes by name. The only place those route names appear is in the source maps it had just downloaded.

Account recovery got the same treatment. The agent checked which usernames existed, then hammered the reset endpoints:

GET /Account/ValidateUserName?UserName=adminPOST /api/v1/Users/GeneratePasswordResetToken → 204POST /forgot\_password

Where it could sign up, it did, using a throwaway mailbox from a free temporary-email service. Then, it immediately tried to look at someone else's data:

Before every fuzzing run, it checked what a baseline "not found" response looked like:

GET /zzz-nonexistent-xyz123

Targeting OAuth Identity Providers

When probing Microsoft OAuth flows, the agent directly manipulated the callback endpoint by injecting fabricated authorization codes and malformed state parameters, while also attempting to bypass authentication using unsigned JWTs:

GET /sign\_in/oauth/microsoft/callback?code=AAAA&state=notvalidb64!!GET /sso?jwt=eyJhbGciOiJub25lIn0.eyJlbWFpbCI6InRlc3RAdGVzdC5jb20ifQ.

That second token simply decodes to {"alg":"none"} and {"email":"test@test.com"}. The agent bombarded more than 60 variations of SSO routes with this payload in just two minutes.

On AWS Cognito, we observed patterns mirroring the account recovery abuse seen in proprietary apps. This activity was reflected in events like InitiateAuth, ForgotPassword, and ResendConfirmationCode. These requests originated from the same mix of user agents observed in earlier attacks, including benign-looking programmatic clients like boto and python-urllib.

The agent also attempted to provision new identities directly, invoking the AWS Cognito SignUp API while cycling through its pool of user agents.

Password Spraying

We also tracked a massive password spray campaign across many of the observed targets. The activity was IDP-agnostic, hitting both Entra and Okta, and displayed several unique, AI-driven characteristics.

The attacks targeted hundreds of users and were executed in highly coordinated bursts. Each burst featured:

Dedicated user agents: A unique user-agent string was assigned to each burst, distinct from those used in previous waves.

Precise timing: The median gap between authentication attempts was strictly one second.

Sustained execution: Individual bursts lasted anywhere from 20 to 60 minutes.

Role-based targeting: The agent primarily focused on accounts belonging to software engineers.

Repeated attempts: Some individual users were subjected to more than a dozen login attempts.

Relentless by Design

The activity was persistent and highly automated. Some sessions lasted 24–30 hours, and when IPs were blocked, new addresses appeared within minutes.

In one session, the agent cycled through a dozen variations of the same SSO endpoint (/sso, /sso/, /sso/login, /sso/jwt, /jwt/sso…), each with and without the same forged token, at a rate of about one request per second. When a login page started rate-limiting the activity, the agent simply switched to a different endpoint on the same host and carried on.

We observed more than 15 different user-agent strings across the victims:

Python-based clients and curl;

Truncated Chrome strings and headless browsers with seemingly random version numbers.

More distinctive, self-describing identifiers, such as ReconProbe/1.0.

This variety, combined with the consistent attack patterns and ARTEX-related indicators, helped us connect the activity across multiple organizations.

Although most of these attempts failed, the true threat lies in the methodology. While a human attacker is bound by time constraints and fatigue, an autonomous agent does not give up. It simply continues to iterate until it finds a single weak point.

A clearly agentic attack

None of the individual techniques observed are novel. However, together the agent behind this attack is illuminated. There are a few clear signals:

Steps were chained automatically: when sign-up was open, it registered with a disposable mailbox, confirmed the account, and immediately requested another company's data.

Each automated step used the output of the last one: internal API routes are called by name minutes after pulling the source maps

Adaptation was automatic: when a login page started rate-limiting, the agent moved to a different endpoint on the same host. When an IP was blocked, a new one appeared within minutes.

Not all attacks were logical: a human attacker of this skill level is unlikely to spend their time testing generic payloads on the heavily scrutinized Microsoft OAuth flows.

Staying Ahead of AI-Powered Attacks

As AI makes reconnaissance and exploitation attempts faster and easier to scale, defenders need to shorten the gap between exposure and remediation. Learn more about how to prepare with Wiz's AI Threat Readiness Framework.

In addition, Wiz's AI Red Agent continuously and autonomously conducts offensive tests, helping reduce exposure at the speed of AI - evening the scales.

In a new incident, a malicious version (1.107.0) of the LiteLLM package was uploaded to PyPI and Docker on October 21. The malicious version includes a credential stealer targeting browser, cloud and AI secrets as well as a dormant C2 capability.

Enable native runtime protection for GKE in just one click. The Wiz Runtime Sensor add-on now automates deployment and credential management while delivering predictable, kernel-level eBPF threat detection for your GKE Kubernetes fleets.

Get a personalized demo

Ready to see Wiz in action?

"Best User Experience I have ever seen, provides full visibility to cloud workloads."

David EstlickCISO

"Wiz provides a single pane of glass to see what is going on in our cloud environments."

Adam FletcherChief Security Officer

"We know that if Wiz identifies something as critical, it actually is."

Greg PoniatowskiHead of Threat and Vulnerability Management
