---
schema: 1
kind: research
title: "Okta Threat Intelligence: AI agents register on Auth0 tenants and Okta organizations with disposable addresses from the mail.tm service, whose single rotating mailbox domain makes blocklists very likely stop matching within weeks; ARTEX, Cairn, CyberStrikeAI and pentestcode each picked it at run time"
headline: "Okta: AI agents sign up with mail.tm; its rotating domain will very likely outdate blocklists within weeks"
summary: >
  Okta Threat Intelligence, with data from the P0 Labs team of Permiso (now part of Okta), reports that since June 2026, and at scale in October and November, AI agents registered accounts with disposable addresses, mostly from the mail.tm family, on Auth0 tenants and Okta organizations that allow public self-service registration. mail.tm exposes one active domain at a time through an account-free API and replaces it periodically, so a blocklist will very likely stop matching within weeks. Okta reads such sign-ups as a likely early sign that agents are tasked against an organization, and says agents often register through the Auth0 Authentication API, which can skip protections applied in Universal Login.
discovered_at: "2026-11-26T04:53:00Z"
updated_at: null
event_date: "2026-11-23"
run_id: 2026-11-26T0356Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, identity]
regions: [global]
sectors: [technology]
entities: ["tool:artex", "tool:cyberstrikeai", "product:okta", "product:auth0", "product:okta-workforce-identity", "product:okta-customer-identity"]
techniques: [T1136.003, T1585.002]
affected_products: ["Auth0", "Okta Workforce Identity", "Okta Customer Identity"]
cves: []
sources:
  - url: "https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/"
    publisher: "Okta Threat Intelligence"
    date: "2026-11-23"
    role: primary
  - url: "https://www.okta.com/newsroom/press-releases/okta-signs-definitive-agreement-to-acquire-permiso-security"
    publisher: "Okta"
    date: "2026-07-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Starting in June 2026 and accelerating at scale throughout October and November 2026, Okta Threat Intelligence observed AI agents registering accounts with disposable email addresses on Auth0 tenants and Okta organizations that allow public self-service registration."
    publisher: "Okta Threat Intelligence"
    source_url: "https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/"
  - quote: "Disposable-domain signups are therefore likely to be an early indicator that AI agents have been tasked with performing attacks against an organization."
    publisher: "Okta Threat Intelligence"
    source_url: "https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/"
  - quote: "Agents commonly register accounts by calling the Auth0 Authentication API directly, which can skip protections applied in Universal Login."
    publisher: "Okta Threat Intelligence"
    source_url: "https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/"
verification: single-source
sourcing_note: >
  Okta is the only source for the finding. Permiso, whose P0 Labs team supplied the framework tests and the attacker-tooling data set, has been part of Okta since 2026-08-26, so the joint investigation is one corporate source, and Permiso's own post could not be found. Okta gives no counts, victims, sector or region, and does not attribute the customer sign-ups to a specific framework. The post is dated 2026-11-23.
confidence: medium
references:
  - 2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse
  - 2026-11-15/artex-aws-cloudwatch-log-secret-hunting-cognito-self-signup
  - 2026-11-14/cyberstrikeai-aws-cloudtrail-intrusion-one-source-ip
  - 2026-11-18/barracuda-cloud-intrusion-vendor-held-key-artex-consistent
  - 2026-11-25/unit42-agentic-ai-attackers-web-shell-footholds
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Okta Threat Intelligence reports that since June 2026, and at scale through October and November, AI agents have registered accounts with disposable email addresses on Auth0 tenants and Okta organizations that allow public self-service registration, activity Okta calls almost certainly malicious and that customers often reported alongside attacks on their applications ([Okta, 2026-11-23](https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/)). The addresses mostly belong to the mail.tm family, a free receive-only service whose API needs no account or key and lets a script create a mailbox, obtain a token and poll for one-time codes ([Okta, 2026-11-23](https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/)). In tests by the P0 Labs team of Permiso, which Okta acquired on 2026-08-26 ([Okta, 2026-07-30](https://www.okta.com/newsroom/press-releases/okta-signs-definitive-agreement-to-acquire-permiso-security)), the ARTEX, Cairn, CyberStrikeAI and pentestcode frameworks each picked mail.tm at run time, and in a data set containing attacker tooling mail.tm appeared on 80 percent of the attacker hosts where disposable email was found ([Okta, 2026-11-23](https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/)).

mail.tm exposes only one active mailbox domain at a time and replaces it periodically, so a blocklist built from earlier domains will very likely stop matching within weeks; Okta's Auth0 telemetry shows sign-ups tracking the domain the API currently returns, and the attackers' domain changed around 2026-10-30 when the API response did. Agents also used mailinator, guerrillamail and emailnator, and at one target an agent moved to another provider when blocked, which Okta reads as agents treating disposable mail as an interchangeable capability. Okta says the use always occurred within a short window of other agentic reconnaissance and intrusion attempts against the same entities ([Okta, 2026-11-23](https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/)). Bot detection and CAPTCHA generally stopped the October mail.tm sign-ups before email verification, but Okta warns agents can solve challenges and commonly register by calling the Auth0 Authentication API directly, which can skip protections applied in Universal Login ([Okta, 2026-11-23](https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/)).

**Exposure:** an Auth0 tenant or Okta organization that allows public self-service registration. For workforce users Okta says self-service registration is a prerequisite for many of the attacks it describes and should be disabled or restricted ([Okta, 2026-11-23](https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/)).

**Detection:** in identity-provider registration telemetry, sign-up events whose email domain belongs to a disposable provider's currently active mailbox domain, kept current by polling the provider's public domain endpoint instead of a static list, as Okta advises ([Okta, 2026-11-23](https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/)).

**Triage:** the discriminator Okta supports is context: a disposable-domain sign-up read alongside other agentic reconnaissance or intrusion attempts against the same entities, not the domain alone ([Okta, 2026-11-23](https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/)).

**Defender takeaway:** on Auth0, block sign-ups through the API while allowing Universal Login and block disposable domains with Actions; on Okta Workforce Identity, disable or restrict self-service registration. Treat a disposable-domain sign-up as a prompt to look for other agentic activity against the same estate, since Okta says it gives a heads-up to look for successful intrusion attempts, and do not rely on CAPTCHA alone ([Okta, 2026-11-23](https://www.okta.com/blog/threat-intelligence/ai-agents-prefer-specific-disposable-email-services-during-ident/)).
