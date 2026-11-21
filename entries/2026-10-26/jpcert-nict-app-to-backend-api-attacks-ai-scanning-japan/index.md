---
schema: 1
kind: threat
title: "Japan's wave of personal-data theft from web systems: JPCERT/CC and NICT describe attackers who decompile the published Android app to find internal APIs, drop JSP web shells as .war files on application servers, and run AI penetration-testing platforms against exposed web applications and WSUS servers"
headline: "JPCERT/CC and NICT: attackers decompile the public app, then call internal APIs; AI platforms scan exposed web apps"
summary: >
  JPCERT/CC (alert AT-2026-0030, updated 2026-10-23) and NICT describe a wave of personal-data leaks from Japanese web systems in which
  attackers analyse the published Android app to find API endpoints and keys and then call internal management APIs the app screens never
  use, place JSP web shells as .war files on application servers behind the public web server, and, per the latest update, run AI
  penetration-testing platforms (Cairn, CyberStrikeAI, ARTEX) against internet-facing web applications, WSUS servers included. No actor is
  named, JPCERT/CC says it confirmed AI used to scan for known vulnerabilities and attack through APIs, and Macnica could not confirm AI use.
discovered_at: "2026-10-26T03:38:00Z"
updated_at: null
event_date: "2026-10-23"
run_id: 2026-10-26T0256Z-intel
priority: notable
immediate_action: null
tags: [data-breach, ai-abuse, vulnerabilities]
regions: [apac]
sectors: []
entities: ["campaign:japan-web-system-data-leak-wave-2026-09", "tool:artex", "tool:cairn-exploitation-engine"]
techniques: [T1190, T1595.002, T1552.001, T1505.003, T1090.003]
affected_products: []
cves: []
sources:
  - url: "https://www.jpcert.or.jp/at/2026/at260030.html"
    publisher: "JPCERT/CC (alert JPCERT-AT-2026-0030, updated 2026-10-23)"
    date: "2026-10-23"
    role: primary
  - url: "https://blogs.jpcert.or.jp/en/2026/10/web_api_attacks.html"
    publisher: "JPCERT/CC Eyes (attack infrastructure investigation)"
    date: "2026-10-21"
    role: primary
  - url: "https://cynex.nict.go.jp/library/261013-01.html"
    publisher: "NICT CYNEX (threat intelligence team LETTICE)"
    date: "2026-10-13"
    role: corroborating
  - url: "https://www.recordedfuture.com/blog/japan-cyber-crisis-warnings"
    publisher: "Recorded Future Insikt Group"
    date: "2026-10-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We confirmed that the attackers had used AI to scan for known vulnerabilities and carry out attacks via APIs."
    publisher: "JPCERT/CC Eyes"
    source_url: "https://blogs.jpcert.or.jp/en/2026/10/web_api_attacks.html"
  - quote: "One notable characteristic of these attacks was that the attackers analyzed Android application packages (APK files) to identify APIs and exploit them"
    publisher: "JPCERT/CC Eyes"
    source_url: "https://blogs.jpcert.or.jp/en/2026/10/web_api_attacks.html"
  - quote: "Macnica could not confirm the use of AI in these attacks."
    publisher: "Recorded Future Insikt Group"
    source_url: "https://www.recordedfuture.com/blog/japan-cyber-crisis-warnings"
verification: multi-source
sourcing_note: >
  JPCERT/CC's alert and its infrastructure investigation are first-hand, and its investigation cites NICT's team, which described the
  app-analysis attack on 2026-10-13; JPCERT/CC says the cases do not show one method used in every incident. The AI element rests on JPCERT/CC's findings on attack
  servers, and Recorded Future relays that Macnica could not confirm it.
confidence: medium
references: ["2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally", "2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse", "2026-09-23/gambit-ai-agent-retail-skimmer-campaign-strix-cairn-hermes"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

JPCERT/CC's alert of 2026-10-08, updated on 2026-10-23, says that around September 2026 Japanese organisations disclosed a run of personal-data leaks through unauthorised access, and singles out an attack type that may be increasing: systems the operator never expected strangers to reach, such as business-intelligence tools and staff-management systems, were hit alongside public apps ([JPCERT/CC, 2026-10-23](https://www.jpcert.or.jp/at/2026/at260030.html)). It does not tie them to one method and groups them in five: per-target scanning for known flaws and exposed configuration and backup files; unauthorised calls to application management APIs; the Metabase SQL injection CVE-2026-72898; .war files carrying a JSP web shell that runs commands passed in query parameters, placed on application servers reachable from the public web server; and, added on 2026-10-23, attempts through AI penetration-testing platforms it names as Cairn, CyberStrikeAI and ARTEX, including against exposed WSUS servers ([JPCERT/CC, 2026-10-23](https://www.jpcert.or.jp/at/2026/at260030.html)).

In the API case the attackers analyse the published smartphone app to find endpoints and keys, then attack internal APIs the app screens cannot reach: changing user rights, creating accounts, toggling a header or sending malformed tokens to compare responses, and blind NoSQL injection to find account data; some use API keys stolen elsewhere ([JPCERT/CC, 2026-10-23](https://www.jpcert.or.jp/at/2026/at260030.html)). NICT calls this an app-to-backend attack: the app need not be vulnerable, and backend authentication, authorisation or input-validation faults leak data ([NICT, 2026-10-13](https://cynex.nict.go.jp/library/261013-01.html)). On attack servers JPCERT/CC found Android packages, reverse-engineering tools and a Python script that answers requests with HTTP 302 redirects and appears to have been used to test for server-side request forgery ([JPCERT/CC Eyes, 2026-10-21](https://blogs.jpcert.or.jp/en/2026/10/web_api_attacks.html)).

No source names an actor. JPCERT/CC says it confirmed that the attackers used AI to scan for known vulnerabilities and attack through APIs ([JPCERT/CC Eyes, 2026-10-21](https://blogs.jpcert.or.jp/en/2026/10/web_api_attacks.html)), while Macnica could not confirm AI use ([Recorded Future, 2026-10-22](https://www.recordedfuture.com/blog/japan-cyber-crisis-warnings)). API-attack access also arrives through Tor exit nodes and residential proxies ([JPCERT/CC, 2026-10-23](https://www.jpcert.or.jp/at/2026/at260030.html)).

**Exposure:** an organisation that publishes a mobile app with a backend API, runs internet-facing web applications, or leaves BI tools, staff-management systems or WSUS servers reachable from the internet ([JPCERT/CC, 2026-10-23](https://www.jpcert.or.jp/at/2026/at260030.html)); NICT asks operators to inventory public APIs and servers and check their access logs ([NICT, 2026-10-13](https://cynex.nict.go.jp/library/261013-01.html)).

**Detection:** in API and web access logs, calls to internal or management endpoints from clients that never load the app screens, role-change and account-creation calls outside the admin console, one endpoint called in sequence with and without a header or with malformed tokens, blind NoSQL-injection-style probing of account lookups, and use of API keys extracted from the app; in web server telemetry, scans for exposed configuration and backup files and .war deployments to application servers ([JPCERT/CC, 2026-10-23](https://www.jpcert.or.jp/at/2026/at260030.html)).

**Triage:** the app's own User-Agent proves nothing, because JPCERT/CC saw attack requests carrying it; the endpoints called and the sequence (header toggling, malformed tokens, role changes) discriminate, and a TLS fingerprint that matches a generic Python client does not identify the attacker alone ([JPCERT/CC, 2026-10-23](https://www.jpcert.or.jp/at/2026/at260030.html)).

**Defender takeaway:** treat the published app package as public and test the backend for authorisation gaps on internal endpoints (IDOR and BOLA), server-side request forgery, remote code execution and SQL injection ([NICT, 2026-10-13](https://cynex.nict.go.jp/library/261013-01.html)). JPCERT/CC's measures are per-endpoint and per-method access control including non-public APIs, expiring least-privilege API tokens with fast revocation, rate limits on login, password reset, SMS and search, no long-lived secrets in apps, and no management functions on the internet ([JPCERT/CC, 2026-10-23](https://www.jpcert.or.jp/at/2026/at260030.html); [JPCERT/CC Eyes, 2026-10-21](https://blogs.jpcert.or.jp/en/2026/10/web_api_attacks.html)).
