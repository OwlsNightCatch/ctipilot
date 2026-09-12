---
schema: 1
kind: vulnerability
title: "miniOrange's SAML2Core library ships the same openssl_verify() tri-state authentication bypass across both its WordPress and Joomla SAML SSO products — one vendor code defect, two ecosystems, exploitation already attempted against the WordPress line"
headline: "PHP's openssl_verify() can return -1 for 'error', and treating that as valid is an unauthenticated admin login on two platforms"
summary: >
  DigitalOcean's security team caught exploitation attempts against miniOrange's WordPress SAML
  2.0 Single Sign On plugin (CVE-2026-61979, CVE-2026-15981), tracing the root cause to
  openssl_verify()'s tri-state return value being treated as a plain boolean. mySites.guru
  independently found the identical defect in miniOrange's Joomla SAML SSO extension
  (CVE-2026-77998). DigitalOcean also found the vendor silently patched six paid WordPress
  editions with no changelog or advisory, so a paid install could read as already-patched purely
  because its version number exceeded the free edition's fixed version.
discovered_at: "2026-08-28T05:58:00Z"
updated_at: null
event_date: "2026-08-21"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, auth-bypass, pre-auth, actively-exploited, poc-public, patch-available, identity]
regions: [global, europe]
sectors: [public-sector, technology]
entities: []
techniques: [T1190, T1606.002]
affected_products: ["miniOrange SAML 2.0 Single Sign On (WordPress)", "miniOrange SAML SSO for Joomla", "miniOrange OAuth Client for Joomla"]
cves:
  - id: CVE-2026-61979
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, poc-public, patch-available]
    affected: "miniOrange SAML 2.0 SSO (WordPress) Free 3.x–5.x; six paid editions silently patched with no version boundary disclosed"
    fixed: "Free 5.4.5; paid editions per DigitalOcean's own version findings (e.g. Standard 17.0.6)"
  - id: CVE-2026-15981
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, poc-public, patch-available]
    affected: "miniOrange SAML 2.0 SSO (WordPress) Free 3.x–5.x; six paid editions silently patched with no version boundary disclosed"
    fixed: "Free 5.4.5; paid editions per DigitalOcean's own version findings (e.g. Standard 17.0.6)"
  - id: CVE-2026-77998
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "miniOrange SAML SSO for Joomla, free 1.0.0–11.0.1"
    fixed: "Paid Joomla SAML editions (Basic 13.2, Standard 24.2, Premium 34.2, Enterprise 44.2) fixed 26 August; the free-line CVE record still covers only 1.0.0–11.0.1"
  - id: CVE-2026-77995
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "miniOrange OAuth Client for Joomla — free edition fixed; paid editions have no fix as of 2026-08-28"
    fixed: "3.2.0 (free edition only)"
sources:
  - url: "https://patchstack.com/articles/one-slug-seven-editions-the-miniorange-saml-sso-bug-that-let-anyone-log-in-as-your-wordpress-admin/"
    publisher: "Patchstack / DigitalOcean security team"
    date: "2026-08-21"
    role: primary
  - url: "https://mysites.guru/blog/miniorange-oauth-joomla-account-takeover/"
    publisher: "mySites.guru"
    date: "2026-08-26"
    role: primary
closed_sources: []
evidence:
  - quote: "An attacker can exploit this by setting SignatureMethod to HMAC-SHA1. As a result, the plugin allows using the trusted RSA public key PEM as the HMAC secret."
    publisher: "Patchstack / DigitalOcean security team"
  - quote: "openssl_verify() is tri-state, returning 1 for a valid signature, 0 for invalid, and -1 when OpenSSL itself errors out. The plugin loosely checked these results, and in PHP -1 is truthy (valid)."
    publisher: "Patchstack"
  - quote: "PHP's openssl_verify() does not answer yes or no. It answers one of three things: 1 if the signature is valid, 0 if it is not, and -1 if OpenSSL could not complete the check at all. That third answer is the trap."
    publisher: "mySites.guru (on the Joomla SAML SSO product, CVE-2026-77998)"
  - quote: "Exploitation has been attempted in the wild. DigitalOcean's defense-in-depth controls detected and blocked the activity on its infrastructure, and the identified indicators were shared to help strengthen detection and protection across the ecosystem."
    publisher: "Patchstack"
verification: multi-source
sourcing_note: >
  DigitalOcean's own root-cause analysis (via Patchstack) is the primary source for the WordPress
  half; mySites.guru independently confirmed the same code defect in the Joomla product, a
  distinct discovering party analysing a distinct codebase, which counts as genuine independent
  corroboration of the defect *class* rather than a relay of one assessor's finding.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Audit every miniOrange SAML or OAuth product in use — on WordPress or Joomla — and upgrade to the fixed version regardless of which platform was 'already checked': the same openssl_verify() tri-state defect exists independently in both codebases, so clearing one platform says nothing about the other. For WordPress, confirm the exact edition and build against DigitalOcean's own version findings rather than the vendor's public CVE range, since six paid editions were silently patched outside that range."
  - "For any Joomla site running the miniOrange OAuth Client extension, there is no fix for paid editions as of 2026-08-28 — restrict or disable the extension's login-cookie trust mechanism until a patch ships, since CVE-2026-77995 lets a client-supplied cookie value alone determine the logged-in account with no verification."
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [actions, cves]
migrated_from: null
---

Two independent research efforts converged on the same vendor-wide defect in miniOrange's (Xecurify) bundled SAML2Core library this week, across two different CMS ecosystems.

**WordPress (miniOrange SAML 2.0 Single Sign On plugin).** DigitalOcean's security team caught exploitation attempts on its own infrastructure via defense-in-depth controls — an anomalous admin-session attempt from outside the trusted network, using a bypass to obtain a valid admin session cookie, then blocked because admin-panel operations sit behind a separate network restriction: "exploitation has been attempted in the wild. DigitalOcean's defense-in-depth controls detected and blocked the activity on its infrastructure, and the identified indicators were shared to help strengthen detection and protection across the ecosystem" ([Patchstack, 2026-08-21](https://patchstack.com/articles/one-slug-seven-editions-the-miniorange-saml-sso-bug-that-let-anyone-log-in-as-your-wordpress-admin/)). DigitalOcean's own root-cause analysis — the first published for any paid edition — found two flaws. CVE-2026-61979 (signature algorithm confusion): the plugin lets an incoming SAML response choose its own `SignatureMethod`; setting it to HMAC-SHA1 makes the plugin use the IdP's public RSA key, fetched from IdP metadata and by definition not secret, as the HMAC secret — "an attacker can exploit this by setting SignatureMethod to HMAC-SHA1. As a result, the plugin allows using the trusted RSA public key PEM as the HMAC secret" ([Patchstack, citing DigitalOcean, 2026-08-21](https://patchstack.com/articles/one-slug-seven-editions-the-miniorange-saml-sso-bug-that-let-anyone-log-in-as-your-wordpress-admin/)) — so an attacker signs a forged assertion with a key anyone can obtain, and the plugin verifies it as genuine. CVE-2026-15981 (OpenSSL tri-state confusion): "`openssl_verify()` is tri-state, returning 1 for a valid signature, 0 for invalid, and -1 when OpenSSL itself errors out. The plugin loosely checked these results, and in PHP -1 is truthy (valid)" ([Patchstack, 2026-08-21](https://patchstack.com/articles/one-slug-seven-editions-the-miniorange-saml-sso-bug-that-let-anyone-log-in-as-your-wordpress-admin/)) — a deliberately malformed signature that trips OpenSSL's error path is accepted as valid. Both let an unauthenticated attacker forge a SAML assertion and land in `/wp-admin` as any existing user, admins included.

The public CVE records cover only the Free edition (3.x–5.x); DigitalOcean discovered the vendor silently patched six additional paid editions (Premium, Standard, two multisite/Enterprise tiers, VIP single/multisite) with no changelog entry and no public advisory, so a paid install on an unlisted version number was reported "already patched" by every vulnerability database checked, including Patchstack's own, because its version number exceeded the Free edition's fixed version. A vulnerable 16.x release additionally shows no managed-update prompt in the WordPress dashboard at all — the upgrade to 17.0.6 requires a manual plugin upload. Opportunistic scanning against miniOrange SSO endpoints has been observed from multiple VPN/datacenter/hosting IP ranges, consistent with automated exploitation attempts against every reachable installation regardless of edition. A public proof-of-concept exists for the Free edition.

**Joomla (miniOrange SAML SSO and OAuth Client extensions).** The Joomla CNA published CVE-2026-77998 (CVSS 4.0 10.0) on 2026-08-25 for miniOrange SAML SSO for Joomla — mySites.guru confirms this is the same `openssl_verify()` tri-state bug in the same vendor's Joomla product: "PHP's `openssl_verify()` does not answer yes or no. It answers one of three things: 1 if the signature is valid, 0 if it is not, and -1 if OpenSSL could not complete the check at all. That third answer is the trap" ([mySites.guru, 2026-08-26](https://mysites.guru/blog/miniorange-oauth-joomla-account-takeover/)), letting an attacker name and impersonate any account, Super User included, with a deliberately broken signature. A separate, simpler flaw, CVE-2026-77995 (CVSS 10.0, published 2026-08-24, credited to Krzysztof Zając of CERT PL), affects the miniOrange OAuth Client extension for Joomla: the extension trusts a client-supplied cookie value to determine which account a visitor is logged in as, with no verification at all (CWE-287) — setting the cookie to name an administrator makes the visitor one. Paid Joomla SAML editions (Basic 13.2, Standard 24.2, Premium 34.2, Enterprise 44.2) were fixed 26 August, the day after the free-line CVE was published, but the Joomla CVE record for CVE-2026-77998 still only covers the free 1.0.0–11.0.1 range; the paid OAuth Client editions have no fix at all as of this writing.

The same code defect class — a tri-state OpenSSL return value treated as a PHP boolean — exists independently in what appear to be two separately-maintained codebases from the same vendor, suggesting either copy-paste reuse of a flawed internal library across product lines or two independent implementations of the same well-known PHP gotcha. Either way, any organisation running any miniOrange SAML product on any platform should treat "we already checked WordPress" or "we already checked Joomla" as insufficient — the vendor's SAML verification code needs auditing wherever it appears.

**Triage:** alert on SAML `AuthnResponse` assertions whose `SignatureMethod` is HMAC-based rather than the expected RSA/DSA scheme, and on authentication log entries showing a successful SSO login immediately following a malformed or error-triggering signature-verification attempt in the web server or application log — legitimate SAML traffic never needs a signature-verification error to precede a successful login.
