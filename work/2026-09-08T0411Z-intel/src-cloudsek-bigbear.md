# extract: served via trafilatura-direct
---
title: Tracking BigBear 2.0 Evilginx2 Phishing Campaign | CloudSEK
author: Gagan Aggarwal
url: https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign
hostname: cloudsek.com
description: CloudSEK researchers uncovered BigBear 2.0, a global Microsoft 365 phishing-as-a-service operation targeting hundreds of organizations across 40+ countries. The investigation exposed the attacker’s admin panel, affiliate network, phishing infrastructure, and thousands of stolen credentials and session cookies, revealing how modern AiTM attacks can hijack authenticated sessions even after MFA.
sitename: CloudSEK
date: "2026-09-07"
categories: ['']
---
**🚀**Introducing the CloudSEK MCP Server!

Read more

Back

CloudSEK researchers uncovered BigBear 2.0, a global Microsoft 365 phishing-as-a-service operation targeting hundreds of organizations across 40+ countries. The investigation exposed the attacker’s admin panel, affiliate network, phishing infrastructure, and thousands of stolen credentials and session cookies, revealing how modern AiTM attacks can hijack authenticated sessions even after MFA.

September 7, 2026

8

min

Subscribe to CloudSEK Resources

Get the latest industry news, threats and resources.

In June 2026, [CloudSEK’s](https://www.cloudsek.com/) TRIAD discovered **BigBear 2.0**, a rebranded Evilginx2-based phishing-as-a-service framework and was able to gain admin access to the threat actor panel. The panel was observed managing 42 VPS nodes over the campaign lifecycle — primarily hosted by The Constant Company LLC (Vultr) — configured with the "offy" phishlet targeting Microsoft 365 exclusively. The operator, using the alias "General Boss", deployed geo-matched residential proxy pools, real-time Telegram exfiltration, and automated cookie replay to bypass MFA and maintain persistent access.

The panel has exfiltrated 5,137 credential records — including 474 complete MFA-bypassed authentications, 1,032 plaintext passwords, and 4,148 session cookies — **affecting 3,331 unique victim IPs across 40+ countries** (India, France, Saudi Arabia, New Zealand, and Germany leading), with the **operation still active at the time of writing**. The multi-user PhaaS panel is leased to at least five affiliate operators identified through live Telegram exfiltration bots, each receiving stolen credentials in real time; custom JavaScript injections disable FIDO2/WebAuthn MFA and residential proxy pools bypass ipapi.is anti-bot detection. Using these, the attacker manipulates the authentication flow so the victim ends up using an alternative authentication method that is weaker or not phishing-resistant. Since late July 2026 the threat actor has deleted 26 of the 42 observed VPS nodes from the panel — evidence of active counter-forensic operations in response to detection.

**2.1 Phishlet Configuration (Evilginx2 "offy")**

The BigBear panel's default phishlet — designated "**offy**" — is configured to intercept Microsoft 365 authentication. Evilginx2 phishlets operate as man-in-the-middle (AiTM) proxies: when a victim visits the phishing URL, the engine proxies all traffic between the victim and the legitimate Microsoft login portal (login.microsoftonline.com), capturing every credential submission and session cookie in transit.

Key phishlet characteristics observed in the panel configuration:

- Subdomain template: <custom>.<phishing-domain> (e.g., login.konceptenterprises[.]com)
- Auto-provisioned Let's Encrypt SSL via HTTP-01 challenge on each subdomain
- Wildcard DNS required — *.phishing-domain points to the VPS IP
- MFA interception: Evilginx2 captures the session cookie (MFA token) after the victim completes the second factor, enabling persistent access without the one-time code
- The "offy" phishlet specifically targets the OAuth 2.0 authorization flow used by Microsoft 365, making it effective against any organization using Azure AD / Entra ID for authentication

The core technique employed is Adversary-in-the-Middle (AiTM) phishing. Unlike classical phishing that only captures passwords, Evilginx2's reverse proxy relays the entire session:

1. Step 1: Victim clicks the phishing link (typically delivered via email) and is proxied to the legitimate Microsoft login page.
2. Step 2: Victim enters email → proxy captures it and passes it to Microsoft.
3. Step 3: Victim enters password → proxy captures plaintext AND forwards to Microsoft.
4. Step 4: Victim completes MFA (TOTP, push notification, SMS) → session token issued by Microsoft is captured by the proxy.
5. Step 5: Attacker replays the captured session cookie to access the victim's mailbox, Teams, SharePoint, and all connected SaaS applications — without triggering re-authentication.

The panel's own metrics confirm this effectiveness: 80% of password entries resulted in session cookie capture, and the password-to-complete conversion rate exceeded 100%, indicating the AiTM relay captured session tokens even without explicit password entry in some cases.

**2.3 Geo-Matched Proxy Pool for Evasion**

A critical enabler for the O365 lure is the panel's residential proxy integration. BigBear 2.0 deploys 69 country-specific residential proxies that auto-match the visitor's geolocation. When a victim in India visits the phishing page, the engine routes the upstream traffic to Microsoft through an Indian residential IP address. This:

- Makes the traffic appear as a legitimate login from the victim's country
- Bypasses Microsoft's geo-anomaly detection (login from unusual location)
- Defeats datacenter/VPN/proxy IP blacklists via ipapi.is integration
- Increases the likelihood that conditional access policies are satisfied

**Diamond Model Attribution**

The Diamond Model of Intrusion Analysis provides a structured framework for understanding this campaign across four core vertices: Adversary, Infrastructure, Capability, and Victim.

 

**Adversary Profile Summary**

The adversary (alias "General Boss") operates a Phishing-as-a-Service model with at least 5 identified affiliate operators receiving stolen credentials via dedicated Telegram bots. The adversary exhibits a cybercriminal rather than state-sponsored profile:

- Phishing-as-a-Service business model — multi-user panel with admin/user roles. Five distinct Telegram bot tokens assigned to different VPS groups confirm the infrastructure was leased to affiliate actors or sub-operators, each receiving credential exfiltration to their own Telegram chat.
- No advanced evasion beyond Evilginx2 defaults (no custom rootkit, no LOLBins observed)
- Monetization likely via initial access brokerage — session cookies enable ransomware deployment, data extortion, or BEC campaigns against victim organizations
- The Telegram bot token and panel metadata did not overlap with known APT groups in open-source intelligence. However, live probing of the bot tokens successfully identified 5 Telegram users actively receiving stolen credentials — these are affiliate operators using the BigBear 2.0 PhaaS platform.

**Identified Affiliate Operators**

Live Telegram bot API probing confirmed 5 active affiliate operators receiving stolen credentials. Each operator controlled one or more VPS nodes. The table below maps Telegram identities, bot tokens, usage patterns, and the specific VPS infrastructure each operator was assigned.

**Structure Note: Panel user_id 5 functions as a reseller tier with two downstream operators (@Sunagashison with 4 nodes, @app_ham with 3 nodes). Panel user_id 6 similarly hosts two operators (@donplayer00, @Mazal100). User_id 3 (VPS "Kingkong") corresponds to the primary admin bot @comeandget_bot (revoked). User_id 2 ("FATHOM") is an individual affiliate.**

**Campaign Scale & Operational Maturity**

Multi-node VPS infrastructure (42 nodes) with centralized panel management — all nodes hosted by The Constant Company LLC (Vultr), indicating a commercial relationship rather than compromised hosts.

**Automated credential processing pipeline:** 

capture → Telegram notification → cookie.js file attachment → Cookie API replay engine. This fully automated pipeline enables near-real-time session hijacking.

Residential proxy pool (69 countries) represents significant operational investment — residential proxies cost $10–50/GB and require proxy provider relationships. The auto geo-matching feature indicates custom proxy pool management software beyond standard Evilginx2 capabilities.

Anti-analysis measures: ipapi.is integration blocks researchers using VPNs/datacenters. During analysis, the panel was only accessible via residential IPs, and multiple VPS nodes were configured with auth error responses to probing.

Real-time Telegram notifications with structured webhook format enable automated downstream processing by affiliate operators. The Telegram bot comeandget_bot[@]telegram serves as the primary C2 channel for credential exfiltration.

**Victimology & Targeting Analysis**

**India concentration analysis**: India is the most-targeted country with 658 records (12.8% of 5137 total), followed by France (463, 9.0%) and Saudi Arabia (353, ~6%). This is broadly proportionate to India's share of global Microsoft 365 licenses (~8–10%). Explanations include: (a) acquisition of Indian corporate email lists from data brokers, (b) lower adoption of phishing-resistant MFA in Indian SMEs, (c) use of English-language lures that resonate with India's English-proficient workforce, and (d) significant IT/Software sector presence in India providing high-value targets.

**Sector targeting rationale**: IT Services/MSP (151 organizations) was the dominant target sector, followed by SaaS/Technology (38), Oil & Gas (22), Pharmaceuticals (20), and Consulting (16). IT service providers are high-value targets because: 

(a) they manage client infrastructure — a single IT provider compromise can enable supply chain attacks against dozens of downstream clients, 

(b) IT staff often have privileged access to Azure AD, on-prem AD, RMM tools, and password managers.

**Spray-and-pray vs. targeted**: The broad sector distribution ( other/mixed (including Unknown)) alongside concentrated IT sector targeting suggests the attacker used both broad email list spraying (volume-based) and sector-specific lists (quality-based). The 438 unique domains spanning 40+ countries support a hybrid targeting model.

**Campaign evolution**: The original panel export- first detection (1,442 records) showed primarily Indian and European targeting. The campaign has since expanded to 5137 total records across 42 VPS nodes, with later exports adding organizations with new VPS nodes (29.06 KALA, Kingkong) and new victim organizations indicating the campaign was actively expanding its infrastructure and targeting scope.

Analysis of the live M365 phishing page captured at management[.]daengrentacar[.]com/meetings revealed three proprietary JavaScript injections patched into every proxied login page. These are not present in standard Evilginx2: 2014 they are custom BigBear 2.0 modifications.

Injection 1: 2014 FIDO2/WebAuthn Disable

window.__bb_fido_down = true;

Object.defineProperty(window, 'PublicKeyCredential', { value: undefined });

Monkey-patches navigator.credentials.get/create to reject publicKey options.

Forces hardware security key users to fall back to phishable MFA (SMS/OTP/TOTP).


Injection 2: 2014 Microsoft Anti-Phishing Telemetry Blocking

Blocklist: ['canarytokens', 'events.data.microsoft.com', 'OneCollector']

Monkeys window.fetch + XMLHttpRequest to silently drop matching requests.

MutationObserver removes matching <img> tags.

Prevents Microsoft from detecting ongoing phishing via telemetry/canary tokens.

Injection 3: 2014 Auto-KMSI (Keep Me Signed In)

Auto-checks #KmsiCheckboxField after page load.

Clicks idSIButton9 after 800ms delay.

Maximizes session cookie lifetime for extended access.

**TLS termination at proxy**: Each Evilginx2 instance terminates the victim's TLS connection at the phishing domain (using Let's Encrypt certificates). The proxy then initiates a NEW TLS connection to the real Microsoft server. This means: (a) the victim sees a valid HTTPS padlock, (b) the victim's corporate proxy/SSL inspection cannot see the traffic to Microsoft (it is encrypted between Evilginx2 and Microsoft), and (c) Microsoft's servers see the VPS IP, not the victim's IP.

**ipapi.is anti-bot integration:** The panel checks every visitor's IP against ipapi.is before serving the phishing page. If the IP is a datacenter, VPN, or proxy, the visitor is blocked. This effectively prevents automated scraping, security researcher analysis, and sandbox detection. During analysis, the panel was only accessible when routing traffic through a residential IP.

**Multi-user panel architecture:** The panel supports role-based access (user/admin). Admin users can view all VPS nodes and credentials across tenant users. This multi-tenant design is consistent with a Phishing-as-a-Service (PhaaS) business model where the infrastructure operator leases access to affiliate actors.

**Engine log streaming:** The panel provides real-time SSE (Server-Sent Events) streaming of Evilginx2 engine logs directly in the browser. This allows operators to monitor active phishing sessions as they happen, including URL requests, credential submissions, and cookie captures with millisecond latency.

Evilginx2's MFA bypass is not a vulnerability in any MFA protocol — it is an architectural limitation of how browser-based authentication works. The following details explain why all existing MFA methods (except FIDO2/WebAuthn) are equally susceptible:

**Cookie interception mechanics**: When the victim completes MFA on the proxied login page, Microsoft issues an authentication cookie (ESTSAUTH for Azure AD, AppSessionId for Outlook Web Access) in the HTTP response Set-Cookie header. Since all traffic flows through Evilginx2's proxy, the server sends this response to Evilginx2 before it reaches the victim's browser. Evilginx2 captures the cookie, stores it in the panel database, and optionally forwards a modified response to the victim (or redirects them to outlook.office.com as a cover).

**ESTSAUTH cookie structure**: The ESSTSAUTH cookie is a Microsoft-issued session token containing encrypted claims about the authentication event — including that MFA was completed. This cookie is bound to the browser session but NOT to a specific device or location. An attacker importing this cookie into their own browser inherits the full authenticated session with all associated access rights.

**Why TOTP/push are bypassed**: Time-based One-Time Passwords (TOTP) and push notification MFA verify the user's possession of a trusted device at the time of login. The proxy does not need to defeat the cryptographic challenge — it simply waits for the user to complete it on the legitimate Microsoft authentication page (which the victim sees via the proxy), then intercepts the session token issued as a result. The attacker never sees or needs the TOTP code.

**SMS MFA bypass**: SMS codes are similarly ineffective — the code is entered on the phishing page (which proxies to Microsoft), Microsoft validates it server-side, and issues the session cookie which Evilginx2 captures. The attacker never needs to know the SMS code to hijack the session.

**Why FIDO2/WebAuthn is resistant**: FIDO2 (hardware security keys, platform authenticators like Apple Face ID / Windows Hello) uses origin-bound credentials. The cryptographic assertion is tied to the origin domain (e.g., login.microsoftonline.com). When Evilginx2 proxies traffic, the origin seen by the browser is the phishing domain (login.evil-domain.com), not the real Microsoft domain. The FIDO2 assertion fails because the origin does not match the credential's registered origin. This is the only MFA method that structurally prevents AiTM phishing.

**Keepalive mechanism**: The panel includes a keepalive feature that periodically refreshes captured session cookies by reusing the refresh token, extending the window of access beyond the initial cookie expiry (typically 1–24 hours for Microsoft session tokens).

**Cookie API automation**: BigBear 2.0 exposes a REST API endpoint (/api/jobs) that accepts captured cookies and automatically replays them against the target service. This enables programmatic, bulk session hijacking without manual browser intervention.

**Refresh token theft**: When Evilginx2 captures the session cookie, it often also obtains the refresh token. Microsoft's refresh tokens are typically valid for 90 days (with sliding window), allowing persistent access even after the initial session expires.

**Post-compromise lateral movement**: With a valid session cookie, the attacker can access the Entra ID portal, enumerate applications with delegated permissions (OAuth consent grants), and potentially pivot to cloud resources (Azure, AWS, Salesforce) connected via SSO.

**Log telemetry gap**: Since the proxy terminates TLS at the phishing domain, the victim's actual IP never reaches Microsoft. Any sign-in log in Entra ID shows the VPS IP (residential proxy), not the attacker's IP, making forensic attribution difficult.

**Conditional Access bypass**: Geo-matched residential proxies defeat location-based CA policies. Device compliance policies are not evaluated because the proxy presents as a new browser session.

**MFA method irrelevance**: TOTP, push notification, SMS, and even voice call MFA are all equally vulnerable — the proxy captures the resulting session cookie regardless of MFA type.

**Email gateway evasion**: The phishing URLs use legitimate domains (compromised or lookalike) with valid SSL certificates. Without URL reputation analysis, most email gateways permit these links.

The panel's 5,137 records include 474 complete sessions with full MFA bypass, 1,032 plaintext passwords and 4,148 session cookies across 461 organizations. Each complete session represents a fully compromised Microsoft 365 account with potential access to:

- Email and calendar (mailbox takeover — BEC, data theft, internal phishing)
- Microsoft Teams (persistent communication channel compromise)
- SharePoint Online and OneDrive (document and intellectual property theft)
- Azure AD / Entra ID (potential lateral movement into cloud infrastructure)
- Connected SaaS applications (CRM, ERP, HR systems federated through Azure AD)

- **Financial fraud** : Compromised email accounts enable BEC (Business Email Compromise) against partners, suppliers, and customers — average BEC loss per incident exceeds $100K
- **Data breach** : Access to SharePoint/OneDrive exposes sensitive business data including contracts, financial records, intellectual property, and PII
- **Supply chain risk:** IT/Software providers compromised in this campaign create a downstream risk to their client organizations
- **Regulatory exposure:** GDPR (EU), DPDP Act (India), CCPA (California) and other data protection regulations impose significant penalties for credential-based breaches
- **Ransomware vector** : Session cookie access is frequently leveraged as an initial access vector for ransomware deployment

**Application Indicators**

   - HTTP header: "x-evg-token", "x-evg-server", "x-evg-session"

   - Cookie: "evginx_session", "evginx_token", "evginx_admin"

   - Cookie: "bigbear_session", "bigbear_token"

- Reset affected passwords
- Revoke session and refresh tokens
- Force user re-authentication
- Enable phishing-resistant MFA - FIDO2 or WebAuthn
- Enforce Conditional Access
- Require compliant devices

```
title: Evilginx BigBear Session Cookies
id: 0b8d50f4-fc0f-4ef5-9001
status: stable
description: Detects known Evilginx and BigBear session cookies.
logsource:
  category: webserver
detection:
  selection:
    http_cookie|contains:
      - "evginx_session"
      - "bigbear_session"
      - "evginx_admin"
  condition: selection
falsepositives:
  - Unknown
level: high
tags:
  - attack.credential-access
title: Communication With Known Evilginx Infrastructure
id: 0b8d50f4-fc0f-4ef5-9002
status: experimental
description: Detects outbound communication to known Evilginx infrastructure.
logsource:
  category: network_connection
detection:
  selection:
    destination_ip:
      - 130.94.82.180
      - 70.34.208.46
      - 130.94.113.184
      - 78.141.193.59
      - 64.176.72.180
      - 38.54.124.58
      - 208.85.18.18
  condition: selection
falsepositives:
  - IP reassignment
level: critical
tags:
  - attack.command-and-control
title: Evilginx Custom Headers
id: 0b8d50f4-fc0f-4ef5-9003
status: experimental
description: Detects uncommon Evilginx-specific HTTP headers.
logsource:
  category: proxy
detection:
  selection:
    http_headers|contains:
      - "x-evg-"
  condition: selection
falsepositives:
  - Unknown
level: high
tags:
  - attack.credential-access
title: Telegram Credential Exfiltration
id: 0b8d50f4-fc0f-4ef5-9004
status: experimental
logsource:
  category: proxy
detection:
  telegram:
    url|contains: "api.telegram.org"
  methods:
    url|contains:
      - "/sendMessage"
      - "/sendDocument"
  secrets:
    http_request_body|contains:
      - "cookie"
      - "session"
      - "password"
      - "credential"
  condition: telegram and methods and 1 of secrets
falsepositives:
  - Approved Telegram automation
level: critical
tags:
  - attack.exfiltration
title: Multiple Evilginx Indicators
id: 0b8d50f4-fc0f-4ef5-9005
status: stable
logsource:
  category: webserver
detection:
  cookies:
    http_cookie|contains:
      - "evginx_session"
      - "bigbear_session"
  headers:
    http_headers|contains:
      - "x-evg-"
  condition: cookies and headers
falsepositives:
  - Unknown
level: critical
tags:
  - attack.credential-access
```
