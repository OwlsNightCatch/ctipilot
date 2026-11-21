---
schema: 1
kind: threat
title: "Tycoon 2FA after the March 2026 takedown: operators add OAuth device-code phishing against Microsoft 365 alongside the credential-relay kit"
headline: "Tycoon 2FA adds device-code phishing: victims approve token issuance to an attacker device on genuine Microsoft pages"
summary: "eSentire reported on 2026-05-12 a late-April 2026 campaign in which Tycoon 2FA operators, still active after the March 2026 takedown, added an OAuth device-code variant alongside their credential-relay kit: an invoice lure with a Trustifi click-tracking link leads through Cloudflare Workers and encrypted JavaScript layers to a fake Microsoft CAPTCHA and a voicemail page showing a device code the operator's backend obtained. The victim pastes it at microsoft.com/devicelogin, signs in and approves MFA on genuine Microsoft infrastructure, and Microsoft issues Microsoft Authentication Broker tokens to the operator's polling client; eSentire's hunts look for device-code sign-ins and Node.js user agents in Entra ID logs."
discovered_at: "2026-05-18T05:00:04Z"
event_date: 2026-05-12
run_id: 2026-05-18-2eabc1cf
priority: high
immediate_action: null
tags:
  - phishing
  - identity
  - cloud
  - organized-crime
regions:
  - global
sectors: []
entities:
  - "campaign:tycoon2fa-oauth-device-authorization-grant-microsoft-365-post-takedown"
techniques: [T1566.002, T1204.001, T1583.007, T1027, T1622, T1497, T1528, T1550.001, T1078.004]
affected_products: ["Microsoft Entra ID", "Microsoft 365"]
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/tycoon2fa-hijacks-microsoft-365-accounts-via-device-code-phishing/"
    publisher: "BleepingComputer"
    date: "2026-05-17"
    role: primary
  - url: "https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing"
    publisher: "eSentire Threat Response Unit"
    date: "2026-05-12"
    role: primary
  - url: "https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows"
    publisher: "Microsoft Learn"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Doing so authorizes the attacker to register a rogue device with the victim’s Microsoft 365 account, giving them unrestricted access to the victim's data and services, including email, calendar, and cloud file storage."
    publisher: BleepingComputer
    source_url: "https://www.bleepingcomputer.com/news/security/tycoon2fa-hijacks-microsoft-365-accounts-via-device-code-phishing/"
  - quote: "The user's MFA worked exactly as designed. There is no proxy, no credential capture, no fake Microsoft page; everything from login.microsoftonline.com onward is authentic Microsoft infrastructure responding to authentic Microsoft authentication events."
    publisher: eSentire Threat Response Unit
    source_url: "https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing"
  - quote: "Successful device-code authentication (AuthenticationProtocol = deviceCode, ResultType = 0) from sources with no prior device-code activity."
    publisher: eSentire Threat Response Unit
    source_url: "https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing"
  - quote: "We recommend organizations get as close as possible to a unilateral block on device code flow."
    publisher: Microsoft Learn
    source_url: "https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows"
verification: single-source
sourcing_note: >
  eSentire TRU analyzed the campaign from a customer incident and BleepingComputer reports from its write-up, so the campaign rests on one assessor;
  Microsoft's Conditional Access guidance supports the hardening advice.
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-18.md
updates:
  - at: "2026-10-21T20:30:49Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Tycoon 2FA operators added an OAuth device-code variant alongside the credential-relay kit rather
      than abandoning it, and the Alibaba (US) hosting eSentire saw since about 2026-04-10 joins the
      previously documented providers instead of replacing them. The lure shows a device code fetched by
      the operator's backend and has the victim paste it at microsoft.com/devicelogin; the detection
      signals are eSentire's own (successful deviceCode sign-ins from sources with no prior device-code
      use, the Microsoft Authentication Broker AppId, node or undici user agents, ResultType 50173 after
      revocation). eSentire's hardening leads with a Conditional Access block on the device-code flow, and
      no source says that FIDO2 sign-in defeats device-code phishing.
    fields: [affected_products, body, classification, entities, event_date, evidence, headline, regions, sectors, sources, sourcing_note, summary, tags, techniques, title, verification]
---

eSentire's Threat Response Unit analyzed in late April 2026 a campaign by operators of the Tycoon 2FA phishing-as-a-service kit, which kept running after the March 2026 takedown led by Microsoft and Europol, that keeps the kit's in-browser tradecraft but ends in Microsoft's legitimate device-login flow instead of a credential-relay proxy ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)). The device-code variant runs beside the relay kit: eSentire still names the OfficeHome AppId as the primary marker of the credential-relay variant and treats the two AppIds as one detection set ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)), and BleepingComputer reports that the kit now supports device-code phishing ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/security/tycoon2fa-hijacks-microsoft-365-accounts-via-device-code-phishing/)).

The lure, a forwarded vendor-invoice reminder, carries a Trustifi click-tracking URL whose clean-reputation domain launders the link, and Trustifi redirects to a throwaway Cloudflare Workers subdomain that returns an AES-GCM-encrypted page decrypted in the browser ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)). The decrypted controller blanks the page for headless browsers and Burp, suppresses developer-tool shortcuts, redirects to microsoft.com when a debugger timing trap fires, checks the visitor's network owner against 230 cloud, sandbox, security-vendor, VPN and AI-crawler names, and stops rendering after a hardcoded expiry date ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)). A Microsoft-branded fake CAPTCHA then queries a Tycoon 2FA Check Domain, which serves suspected analysts a benign decoy website and real victims a Microsoft 365 voicemail lure ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)).

The voicemail page displays a user code that the operator's backend obtained from Microsoft's device-code endpoint, copies it and opens microsoft.com/devicelogin; the victim signs in at login.microsoftonline.com, approves the MFA push and consents to Microsoft Authentication Broker, and Microsoft issues access and refresh tokens to the operator's polling client, after which the kit sends the victim to their real Outlook inbox ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)). A victim already signed in sees no authentication step at all, only the consent prompt ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)). Because the Broker is a Microsoft first-party application it does not trigger unverified-publisher OAuth detections, and its token can be exchanged for Exchange, Graph and OneDrive tokens without further interaction ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)). The backend traffic still uses the CryptoJS AES-CBC layer with a hardcoded key and IV unchanged since eSentire's April 2025 analysis, which works as a kit fingerprint rather than protection, and the operators' token traffic came from Alibaba (US) hosting, which eSentire has seen across both kit variants since about 2026-04-10 in addition to the hosting providers documented before ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)).

**Exposure:** Microsoft Entra ID tenants that allow the OAuth device-code flow for end users; the protocol does not bind the device that requested a code to the user, so anyone who starts a device-code grant for a Microsoft first-party AppId can collect tokens from any user who consents ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)).

**Detection:** in Entra ID sign-in logs, successful device-code authentications (AuthenticationProtocol deviceCode, ResultType 0) from sources with no prior device-code activity, tokens issued to Microsoft Authentication Broker (AppId 29d9ed98-a469-4536-ade2-f981bc1d605e), and the user agents node or undici against that AppId in non-interactive sign-ins, with axios/1.x marking the credential-relay variant ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)). After revocation, repeated ResultType 50173 events with those user agents against one account show the operator still trying ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)). Revoking the session does not undo what the operator already set up: after a confirmed device-code phish eSentire revokes the refresh-token chain and reviews mailbox rules, OAuth consents and forwarding ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)).

**Triage:** a device-code sign-in alone can be a legitimate command-line tool or input-constrained device; eSentire's discriminators are a source with no prior device-code activity and Node.js user agents against the Broker AppId in non-interactive sign-ins, which it calls highly anomalous in production environments ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)).

**Defender takeaway:** block the device-code flow with Conditional Access for all users except documented exceptions: Microsoft recommends getting as close as possible to a unilateral block ([Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows)), and eSentire calls it the single control that removes this attack class for affected users ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)). eSentire adds admin consent for third-party applications, Continuous Access Evaluation and device-compliance requirements ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)).

## Correction — 2026-10-21T20:30:49Z

Tycoon 2FA operators did not move away from the credential-relay kit: eSentire still names the OfficeHome AppId as the primary marker of the relay variant and treats it and the Broker AppId as one detection set, and BleepingComputer reports that the kit now supports device-code phishing ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing); [BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/security/tycoon2fa-hijacks-microsoft-365-accounts-via-device-code-phishing/)). The Alibaba (US) hosting seen since about 2026-04-10 is an addition to the hosting providers documented before, not a replacement ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)). The lure page shows a user code obtained by the operator's backend and tells the victim to paste it at microsoft.com/devicelogin ([BleepingComputer, 2026-05-17](https://www.bleepingcomputer.com/news/security/tycoon2fa-hijacks-microsoft-365-accounts-via-device-code-phishing/)), after which the victim sees a consent prompt reading "Are you trying to sign in to Microsoft Authentication Broker?" ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)). The detection signals eSentire publishes are successful deviceCode sign-ins from sources with no prior device-code activity, tokens issued to the Microsoft Authentication Broker AppId, node or undici user agents in non-interactive sign-ins, and ResultType 50173 after revocation ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)). eSentire says the phish does not bypass MFA but changes what MFA authorizes, and recommends blocking the device-code flow with Conditional Access as the control that removes the attack class ([eSentire TRU, 2026-05-12](https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing)), in line with Microsoft's advice to get as close as possible to a unilateral block ([Microsoft Learn](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows)); no source says that FIDO2 sign-in defeats device-code phishing.
