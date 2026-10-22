P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
ES = 'https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing'
BC = 'https://www.bleepingcomputer.com/news/security/tycoon2fa-hijacks-microsoft-365-accounts-via-device-code-phishing/'
CA = 'https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows'
DC = 'https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code'
SK = 'https://blog.sekoia.io/tycoon-2fa-an-in-depth-analysis-of-the-latest-version-of-the-aitm-phishing-kit/'
ENTRY = {
 'entry': '2026-05-18/tycoon2fa-after-the-march-2026-takedown-oauth-device-authori',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'summary; body Background paragraph',
   'claim': 'Tycoon2FA PhaaS pivots from credential-relay AiTM to OAuth 2.0 Device Authorization Grant abuse / the kit\'s operators have moved away from credential-relay AiTM and are now abusing the legitimate OAuth 2.0 Device Authorization Grant flow',
   'defect': 'The kit added a device-code variant; the credential-relay variant continues. eSentire runs parallel detections for both variants and says the delivery tradecraft is unchanged from the credential-relay variant; BleepingComputer says the kit "now supports" device-code phishing.',
   'ground_truth': 'AppId 4765445b-... (OfficeHome) remains the primary AppId for the credential-relay variant ... Both AppIds together form a parallel detection set covering both kit variants. / The Tycoon2FA phishing kit now supports device-code phishing attacks (BleepingComputer)',
   'ground_truth_url': ES,
   'fix': 'Tycoon2FA operators added an OAuth device-code variant alongside the credential-relay AiTM kit.',
   'class': 'factual-error'},
  {'where': 'body Attack chain paragraph (ASN sentence)',
   'claim': 'eSentire records the underlying hosting ASN rotated to AS45102 (Alibaba Cloud) from 2026-04-10 onward, replacing previously documented ASNs.',
   'defect': 'eSentire says the opposite: AS45102 is an operator-side ASN (token acquisition and refresh-token reuse) to be added parallel to, not replacing, the previously documented set.',
   'ground_truth': 'AS45102 should be treated as an active addition to the post-takedown Tycoon 2FA ASN watchlist, parallel to (not replacing) the previously documented set / AS45102 ... is an active operator-side ASN observed in this campaign and across the Tycoon 2FA kit since approximately April 10, 2026.',
   'ground_truth_url': ES,
   'fix': 'eSentire saw operator-side token acquisition and refresh-token reuse from Alibaba (US) hosting since about 2026-04-10, in addition to the previously documented hosting providers.',
   'class': 'factual-error'},
  {'where': 'body Attack chain paragraph (quoted prompt)',
   'claim': 'instructing the victim to *"complete sign-in by visiting `microsoft.com/devicelogin` and entering this code: AB12-CDEF"*',
   'defect': 'This quoted prompt text appears in neither eSentire nor BleepingComputer; it is an invented illustration presented as a quotation. eSentire describes a voicemail-themed Microsoft 365 lure page after the Check Domain gate.',
   'ground_truth': 'The phishing page retrieves a Microsoft OAuth device code from the attacker\'s backend and instructs the victim to copy and paste it to \'microsoft.com/devicelogin\' (BleepingComputer) / Visitors who pass the Check Domain are shown a Microsoft 365 voicemail-themed lure. (eSentire)',
   'ground_truth_url': BC,
   'fix': 'Paraphrase without quotation marks: the lure page shows a device code fetched from the operator backend and tells the victim to paste it at microsoft.com/devicelogin.',
   'class': 'factual-error'},
  {'where': 'body Hunt / detection concepts paragraph',
   'claim': 'Per eSentire\'s TRU analysis: query Entra ID sign-in logs for `AuthenticationProtocol = "deviceCode"` paired with `ClientAppUsed = "Microsoft Authentication Broker"` ...; alert on any device-code authentication from foreign ASNs against high-privilege users ...; correlate ... (`Add OAuth2PermissionGrant`); on the email layer hunt for inbound mail containing the literal string `microsoft.com/devicelogin` paired with a device-code-shaped substring',
   'defect': 'Most of this list is not in eSentire: no high-privilege/foreign-ASN rule, no OAuth2PermissionGrant correlation, no email-body string hunt; ClientAppUsed does not hold an application name. It also drops eSentire\'s strongest discriminators: the "node" and "undici" user agents against the Broker AppId in non-interactive sign-ins, errorCode 50173 for post-revocation activity, and the OfficeHome AppId for the relay variant.',
   'ground_truth': 'Successful device-code authentication (AuthenticationProtocol = deviceCode, ResultType = 0) from sources with no prior device-code activity. AppId 29d9ed98-a469-4536-ade2-f981bc1d605e (Microsoft Authentication Broker) is the impersonated OAuth client ... UserAgent strings "node" and "undici" against AppId 29d9ed98 in non-interactive sign-in logs are direct fingerprints of the operator\'s Node.js automation backend.',
   'ground_truth_url': ES,
   'fix': 'Detection per eSentire: successful deviceCode sign-ins (ResultType 0) from sources with no prior device-code use; Microsoft Authentication Broker AppId 29d9ed98-... in sign-in logs; "node"/"undici" (device-code variant) or axios/1.x (relay variant) user agents in non-interactive sign-ins; errorCode 50173 with Node.js user agents after revocation. Mark any other hunts as the entry\'s own.',
   'class': 'factual-error'},
  {'where': 'body Hunt / detection concepts paragraph (kit fingerprint sentence)',
   'claim': 'the Tycoon2FA browser stage retains the hardcoded CryptoJS AES-CBC key `1234567890123456` first documented in the kit\'s 2024 build, and the fake CAPTCHA layer still embeds the same Cloudflare-anti-bot bypass JavaScript across the rebuilt infrastructure',
   'defect': 'eSentire ties the unchanged CryptoJS layer to its April 2025 "Phish & Chips" analysis; the cited 2024 Sekoia analysis does not carry this key. No source mentions a "Cloudflare-anti-bot bypass JavaScript"; eSentire says the CAPTCHA page repeats the Layer 2 anti-analysis stack. The literal key is a kit artifact the IOC rule may treat as an indicator.',
   'ground_truth': 'This is byte-for-byte identical to the encryption layer documented in the April 2025 "Phish & Chips" blog and confirmed unchanged in the April 2026 infrastructure update. / The page repeats the entire anti-analysis stack from Layer 2',
   'ground_truth_url': ES,
   'fix': 'The backend calls use a CryptoJS AES-CBC layer with a hardcoded key and IV unchanged since eSentire\'s April 2025 analysis, which eSentire treats as a kit fingerprint; the fake CAPTCHA page repeats the anti-analysis checks. Do not print the key.',
   'class': 'factual-error'},
  {'where': 'body ATT&CK mapping paragraph (last sentence); Hardening paragraph (FIDO2 sentence)',
   'claim': 'Every MFA method except FIDO2 / WebAuthn with phishing-resistant attestation is vulnerable to this attack class ... / Migrate high-privilege users to FIDO2 / WebAuthn ... the attacker cannot complete it because the FIDO2 origin-binding fails on a non-matching browser session.',
   'defect': '(low confidence on the contradiction; no fetched source discusses FIDO2) No source says FIDO2 stops device-code phishing, and the mechanism the sources describe cuts against it: the victim authenticates on genuine Microsoft sign-in pages, so origin binding has nothing to reject. eSentire\'s control is blocking device code flow, which it says "eliminates the entire attack class".',
   'ground_truth': 'everything from login.microsoftonline.com onward is authentic Microsoft infrastructure responding to authentic Microsoft authentication events / Implement Microsoft Entra Conditional Access policies that block OAuth Device Code authentication flows for end-users ... This single control eliminates the entire attack class for affected users.',
   'ground_truth_url': ES,
   'fix': 'Remove both FIDO2 claims; lead the hardening with the Conditional Access device-code block, consent restriction, CAE with refresh-token revocation, and device compliance (eSentire).',
   'class': 'factual-error'},
  {'where': 'evidence[1]',
   'claim': '"The user\'s MFA worked exactly as designed. There is no proxy, no credential capture, no fake Microsoft page."',
   'defect': 'The quote is cut at a semicolon and closed with a period, dropping the qualifier that limits "no fake Microsoft page" to the steps from login.microsoftonline.com onward; the chain does include a fake Microsoft CAPTCHA page earlier.',
   'ground_truth': 'The user\'s MFA worked exactly as designed. There is no proxy, no credential capture, no fake Microsoft page; everything from login.microsoftonline.com onward is authentic Microsoft infrastructure responding to authentic Microsoft authentication events.',
   'ground_truth_url': ES,
   'fix': 'Quote the full sentence.',
   'class': 'imprecision'},
  {'where': 'body Attack chain paragraph; Hardening paragraph',
   'claim': 'finally the victim lands on a fake Microsoft CAPTCHA / "Check Domain" page ... calling the OAuth Device Authorization Grant endpoint (`/oauth2/v2.0/devicecode`) on the victim\'s tenant ... MFA fires and succeeds against the victim\'s own MFA method (push, OTP, SMS) / Microsoft recommends this as a tenant-wide default ... almost never for desktop or browser users ... Microsoft never sends device codes via email',
   'defect': 'The CAPTCHA page and the Check Domain gate are separate steps (CAPTCHA click, then a GET to the Check Domain, then the voicemail lure). eSentire says the device code matches codes issued by the /common/ endpoint and observed only an authenticator push. Microsoft\'s page recommends getting "as close as possible to a unilateral block" and allowing the flow only for documented cases such as legacy tooling; "almost never for desktop or browser users", "CLI tools" and "Microsoft never sends device codes via email" are not in any source.',
   'ground_truth': 'We recommend organizations get as close as possible to a unilateral block on device code flow. ... Only allow device code flow in well documented and secured use cases, like legacy tooling that can\'t be updated.',
   'ground_truth_url': CA,
   'fix': 'Separate the CAPTCHA and Check Domain steps; say the code comes from the common device-code endpoint; cite Microsoft\'s wording for the block recommendation; drop the unsourced Microsoft-behavior claim.',
   'class': 'imprecision'},
  {'where': 'body (uncited clauses)',
   'claim': 'Attack chain, Hunt / detection concepts and Hardening paragraphs',
   'defect': 'Beyond the Background paragraph and the Microsoft documentation links, the analysis carries no inline citation to eSentire or BleepingComputer although most clauses come from them.',
   'ground_truth': 'eSentire carries the Trustifi redirect, Cloudflare Workers, AES-GCM layer, fake CAPTCHA, Microsoft Authentication Broker AppId and the deviceCode sign-in signal.',
   'ground_truth_url': ES,
   'fix': 'Cite eSentire on each attack-chain and detection clause.',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1566.002', 'behavior': 'Invoice-themed lure email with a Trustifi click-tracking URL', 'url': ES},
   {'id': 'T1204.001', 'behavior': 'Victim clicks the tracking link and passes through the redirect chain', 'url': ES},
   {'id': 'T1583.007', 'behavior': 'Throwaway Cloudflare Workers subdomain serves the encrypted next stage', 'url': ES},
   {'id': 'T1027', 'behavior': 'AES-GCM-encrypted payload decrypted in the browser with SubtleCrypto and written to the DOM', 'url': ES},
   {'id': 'T1622', 'behavior': 'Debugger timing trap redirects to microsoft.com when a debugger is attached', 'url': ES},
   {'id': 'T1497', 'behavior': 'Detection of automation frameworks, sandboxes, VPNs and security-vendor ASNs, with redirection of analysis environments', 'url': BC},
   {'id': 'T1528', 'behavior': 'Victim enters an attacker-obtained device code at microsoft.com/devicelogin and consents to Microsoft Authentication Broker; tokens are issued to the attacker device', 'url': ES},
   {'id': 'T1550.001', 'behavior': 'Operator reuses refresh tokens from Node.js automation; Broker tokens exchanged for Exchange, Graph and OneDrive', 'url': ES},
   {'id': 'T1078.004', 'behavior': 'Sustained access to the victim Microsoft 365 account (email, calendar, cloud storage)', 'url': BC},
  ],
  'note': 'All ids checked active; T1656 (Impersonation) is revoked in v20 and was not used.',
  'rating': {'reliability': 'B', 'credibility': 2, 'basis': 'eSentire TRU is an original research/MDR team reporting its own analysis; BleepingComputer restates eSentire. One assessor; the wider device-code trend is corroborated by Proofpoint and Push Security as cited by BleepingComputer, but not this campaign.'},
  'exposure': [
   {'quote': 'The attack begins when a victim clicks a Trustifi click-tracking URL in a lure email and culminates in the victim unknowingly granting OAuth tokens to an attacker-controlled device through Microsoft\'s legitimate device-login flow at microsoft.com/devicelogin.', 'url': ES},
   {'quote': 'it appears in Entra telemetry as a normal Microsoft application - not as an unknown third-party OAuth app - so it does not trigger the unverified-publisher detections that catch many OAuth phishing campaigns.', 'url': ES},
  ],
  'detection': [
   {'quote': 'Successful device-code authentication (AuthenticationProtocol = deviceCode, ResultType = 0) from sources with no prior device-code activity.', 'url': ES},
   {'quote': 'UserAgent strings "node" and "undici" against AppId 29d9ed98 in non-interactive sign-in logs are direct fingerprints of the operator\'s Node.js automation backend.', 'url': ES},
   {'quote': 'After a confirmed device-code phish, revoking the refresh-token chain via Revoke-AzureADUserAllRefreshToken terminates persistence.', 'url': ES},
  ],
  'triage': [
   {'quote': 'Their appearance against the Microsoft Authentication Broker AppId in non-interactive sign-in logs is highly anomalous in production environments and is, in practice, a strong post-compromise indicator.', 'url': ES},
  ],
  'takeaway': [
   {'quote': 'Implement Microsoft Entra Conditional Access policies that block OAuth Device Code authentication flows for end-users, allowing them only for explicitly defined developer or device-onboarding scenarios. This single control eliminates the entire attack class for affected users.', 'url': ES},
   {'quote': 'We recommend organizations get as close as possible to a unilateral block on device code flow.', 'url': CA},
  ],
  'bodies': [P + 'ty-bc.txt', P + 'ty-esentire.txt', P + 'ty-sekoia.txt', P + 'ty-ms-devicecode.txt', P + 'ty-ms-ca.txt', P + 'ty-proofpoint.txt'],
 },
 'possible_twin_outside_batch': 'entries/2026-05-27/tycoon-2fa-after-the-march-2026-takedown-two-tier-aitm-opera (Tycoon 2FA post-takedown activity; check whether it is the same finding or a distinct relay-variant report)',
}
CLAIMS = '''
d7331851a9 ¦ ok ¦ https://www.bleepingcomputer.com/news/security/tycoon2fa-hijacks-microsoft-365-accounts-via-device-code-phishing/ ¦ "Despite an international law enforcement operation disrupting the Tycoon2FA phishing platform in March" ... now supports device-code phishing
b059ce21b9 ¦ F4 ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ OfficeHome AppId "remains the primary AppId for the credential-relay variant"; parallel detection set for both variants (added, not pivoted)
3d7a707228 ¦ ok ¦ https://blog.sekoia.io/tycoon-2fa-an-in-depth-analysis-of-the-latest-version-of-the-aitm-phishing-kit/ ¦ Sekoia 2024-03-25: "Tycoon 2FA has become one of the most widespread adversary-in-The-Middle (AiTM) phishing kits"
52d5e580ae ¦ F4 ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ late April 2026 campaign confirmed; kit did not move away from credential relay (both variants tracked; tradecraft "virtually unchanged from the credential-relay variant")
0f4600fd53 ¦ F3 ¦ https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-device-code ¦ MS doc: POST .../{tenant}/oauth2/v2.0/devicecode (generic); Broker impersonation is eSentire's, which says codes match those issued by the /common/ endpoint
9ec44a41bb ¦ ok ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ T1566.002 fits: Trustifi click-tracking URL embedded in an invoice-themed email
7456dda857 ¦ ok ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ T1528 fits: victim unknowingly grants OAuth tokens to an attacker-controlled device
12c8f667df ¦ ok ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ T1550.001 fits: sustained refresh-token reuse phase; Broker tokens exchanged for other resources
d1c0128c64 ¦ ok ¦ https://www.bleepingcomputer.com/news/security/tycoon2fa-hijacks-microsoft-365-accounts-via-device-code-phishing/ ¦ T1078.004 fits: unrestricted access to the victim's data and services, including email, calendar, and cloud file storage
8ffa4b0625 ¦ ok ¦ https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows ¦ Conditions > Authentication Flows > Device code flow; Grant > Block access
d3602887ee ¦ F5 ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ "There is no proxy"; but eSentire gives sign-in-time discriminators (deviceCode from sources with no prior use, node/undici UAs), so "indistinguishable until token used" overstated
f6efd348ff ¦ F4 ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ AS45102 "parallel to (not replacing) the previously documented set", operator-side; CAPTCHA and Check Domain are separate steps
22c39798df ¦ F4 ¦ https://www.bleepingcomputer.com/news/security/tycoon2fa-hijacks-microsoft-365-accounts-via-device-code-phishing/ ¦ quoted prompt "complete sign-in by visiting ... AB12-CDEF" in no source; BC: instructs the victim to copy and paste it to microsoft.com/devicelogin
9568112988 ¦ F5 ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ Microsoft polls for an authenticator-app push approval ... issues access and refresh tokens (push only observed; OTP/SMS not stated)
cf62852a6f ¦ F5 ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ Successful device-code authentication (AuthenticationProtocol = deviceCode, ResultType = 0) from sources with no prior device-code activity
71ee1a5533 ¦ F5 ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ The user's MFA worked exactly as designed ... granting OAuth tokens to an attacker-controlled device
4b18651d00 ¦ F4 ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ (low confidence) no source discusses FIDO2; victim authenticates on genuine login.microsoftonline.com, eSentire's fix is the device-code block
b91de0873a ¦ F4 ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ eSentire hunts: AppId 29d9ed98 + "node"/"undici" UAs, errorCode 50173, deviceCode ResultType 0; no high-privilege/foreign-ASN, OAuth2PermissionGrant or email-string hunt
8b498b73db ¦ F4 ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ CryptoJS layer "identical to ... April 2025 Phish & Chips blog" (Sekoia 2024 does not carry the key); no "Cloudflare-anti-bot bypass JavaScript"
2e502e4961 ¦ F5 ¦ https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows ¦ Include all users (recommended); recommend excluding emergency access and service accounts / service principals
36a28a24a8 ¦ F5 ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ Enable Continuous Access Evaluation (CAE) so that token revocation propagates in near real time
e859783d65 ¦ F4 ¦ https://www.esentire.com/blog/tycoon-2fa-operators-adopt-oauth-device-code-phishing ¦ (low confidence) no source says FIDO2 origin binding defeats the flow; authentication happens on authentic Microsoft infrastructure
05789d9000 ¦ F5 ¦ null ¦ "Microsoft never sends device codes via email" stated by no fetched source
'''
