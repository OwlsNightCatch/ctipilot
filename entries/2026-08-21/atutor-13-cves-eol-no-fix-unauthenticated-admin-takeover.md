---
schema: 1
kind: vulnerability
horizon: operational
title: "Thirteen CVEs in ATutor, none of which will ever be fixed — including an unauthenticated auto-login token forgery that authenticates as any account, administrators included"
headline: "**CERT Polska discloses 13 ATutor flaws against an end-of-life product** — one is pre-auth to administrator, and no fix is coming"
summary: >
  CERT Polska published coordinated-disclosure advisories on 2026-08-20 for thirteen vulnerabilities in ATutor, an
  open-source learning content management system, confirmed against version 2.2.4. The load-bearing one is
  CVE-2026-64961: the auto-login token check exists but the values it validates are left uninitialised on some code
  paths, so an unauthenticated attacker who can work out a user's identifier and registration timestamp forges a valid
  token and authenticates as that user — administrators included — without the password. Two further flaws reach
  remote code execution as the web-server user, and an authenticated administrator can drive server-side requests at
  internal and cloud-metadata endpoints. CERT Polska states the product is no longer actively supported and the
  vulnerabilities have not been fixed, so there is no patched version for any of the thirteen and no CVSS score is
  published for any of them.
discovered_at: "2026-08-21T06:10:00Z"
event_date: "2026-08-20"
run_id: 2026-08-21T0410Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, no-patch, pre-auth, auth-bypass, rce, path-traversal, info-disclosure]
regions: [europe, global]
sectors: [education, public-sector]
entities: []
techniques: [T1190, T1505.003, T1083]
affected_products: ["ATutor"]
cves:
  - id: CVE-2026-64961
    cvss: null
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "2.2.4 confirmed; other versions untested but possibly affected"
    fixed: "none — product is no longer actively supported and the vulnerabilities have not been fixed"
  - id: CVE-2026-64966
    cvss: null
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [no-patch]
    affected: "2.2.4 confirmed; other versions untested but possibly affected"
    fixed: "none — end of life"
  - id: CVE-2026-64960
    cvss: null
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [no-patch]
    affected: "2.2.4 confirmed; other versions untested but possibly affected"
    fixed: "none — end of life"
  - id: CVE-2026-64968
    cvss: null
    epss: null
    type: ssrf
    vector: zero-click
    auth: admin-required
    status: [no-patch]
    affected: "2.2.4 confirmed; other versions untested but possibly affected"
    fixed: "none — end of life"
  - id: CVE-2026-64964
    cvss: null
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "2.2.4 confirmed; other versions untested but possibly affected"
    fixed: "none — end of life"
  - id: CVE-2026-64965
    cvss: null
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: post-auth
    status: [no-patch]
    affected: "2.2.4 confirmed; other versions untested but possibly affected"
    fixed: "none — end of life"
  - id: CVE-2026-64969
    cvss: null
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status: [no-patch]
    affected: "2.2.4 confirmed; other versions untested but possibly affected"
    fixed: "none — end of life"
  - id: CVE-2026-64963
    cvss: null
    epss: null
    type: path-traversal
    vector: zero-click
    auth: post-auth
    status: [no-patch]
    affected: "2.2.4 confirmed, where the AT_FORCE_GET_FILE option is enabled"
    fixed: "none — end of life"
  - id: CVE-2026-64967
    cvss: null
    epss: null
    type: path-traversal
    vector: zero-click
    auth: admin-required
    status: [no-patch]
    affected: "2.2.4 confirmed; other versions untested but possibly affected"
    fixed: "none — end of life"
  - id: CVE-2026-64962
    cvss: null
    epss: null
    type: logic-flaw
    vector: user-interaction
    auth: post-auth
    status: [no-patch]
    affected: "2.2.4 confirmed; other versions untested but possibly affected"
    fixed: "none — end of life"
  - id: CVE-2026-64970
    cvss: null
    epss: null
    type: xss
    vector: user-interaction
    auth: post-auth
    status: [no-patch]
    affected: "2.2.4 confirmed; other versions untested but possibly affected"
    fixed: "none — end of life"
  - id: CVE-2026-64971
    cvss: null
    epss: null
    type: xss
    vector: user-interaction
    auth: post-auth
    status: [no-patch]
    affected: "2.2.4 confirmed; other versions untested but possibly affected"
    fixed: "none — end of life"
  - id: CVE-2026-64972
    cvss: null
    epss: null
    type: xss
    vector: user-interaction
    auth: post-auth
    status: [no-patch]
    affected: "2.2.4 confirmed; other versions untested but possibly affected"
    fixed: "none — end of life"
sources:
  - url: "https://cert.pl/en/posts/2026/08/CVE-2026-64960/"
    publisher: "CERT Polska (NASK)"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence:
  - quote: "Although a token validation check is present in the auto-login functionality, the values required for token validation remain uninitialized in certain code paths. An unauthenticated attacker who can determine a user's identifier and registration timestamp can generate a valid token and authenticate as an existing user, including administrator, without knowing the password."
    publisher: "CERT Polska"
  - quote: "Product is no longer actively supported and the vulnerabilities have not been fixed. Only version 2.2.4 was tested and confirmed as vulnerable, other versions were not tested but might also be vulnerable."
    publisher: "CERT Polska"
  - quote: "An attacker with instructor privileges can upload and extract a specially crafted ZIP archive, causing files to be written outside the intended extraction directory. This allows an attacker to place a server-executable .phtml file in the web root and achieve remote code execution with web server privileges on the underlying server."
    publisher: "CERT Polska"
verification: single-source-national-cert
sourcing_note: >
  Single-source under the national-CERT carve-out: CERT Polska is the coordinating national CSIRT and the disclosing
  party for its own advisory, credited to reporters at an external testing team. Both the English and Polish renderings
  of the advisory were read and carry identical technical content. Two things the advisory deliberately does not
  contain, and which this entry therefore does not either: no CVSS score is published for any of the thirteen CVEs, so
  none is synthesised here, and no claim of in-the-wild exploitation is made. CERT Polska also names no count of live
  deployments, so this entry makes no exposure estimate. The per-CVE flaw mapping is read off the advisory's own
  per-identifier metadata and description blocks rather than paired by position.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Inventory any ATutor instance across education and research estates and take it off the public internet — there is no patched version for any of the thirteen flaws and none is coming, so exposure reduction or decommissioning is the only remediation available."
migrated_from: null
---

ATutor is an open-source learning content management system, and the reason this disclosure matters is stated in CERT Polska's own advisory rather than implied: "Product is no longer actively supported and the vulnerabilities have not been fixed. Only version 2.2.4 was tested and confirmed as vulnerable, other versions were not tested but might also be vulnerable" ([CERT Polska, 2026-08-20](https://cert.pl/en/posts/2026/08/CVE-2026-64960/)). Thirteen identifiers, CVE-2026-64960 through CVE-2026-64972, and no fixed release for any of them.

**The pre-authentication flaw is the one that decides the response.** CVE-2026-64961 is an authorization bypass through a user-controlled key, and the mechanism is a check that exists but validates nothing: "Although a token validation check is present in the auto-login functionality, the values required for token validation remain uninitialized in certain code paths. An unauthenticated attacker who can determine a user's identifier and registration timestamp can generate a valid token and authenticate as an existing user, including administrator, without knowing the password." Both inputs are guessable or discoverable rather than secret — a sequential user identifier and a registration time — which is what turns this from a theoretical token weakness into a path to the administrator account from the open internet. A sibling flaw compounds it: CVE-2026-64964 makes account-confirmation email tokens predictable through insufficiently random values.

**Two paths to code execution, both after a login.** CVE-2026-64966 is a path traversal in ZIP extraction: "An attacker with instructor privileges can upload and extract a specially crafted ZIP archive, causing files to be written outside the intended extraction directory. This allows an attacker to place a server-executable .phtml file in the web root and achieve remote code execution with web server privileges on the underlying server." CVE-2026-64960 gets there more directly — the Gameme module accepts uploads of any type or extension without restriction and stores them somewhere web-accessible before validating the content, so an authenticated user who knows a valid course identifier uploads a script and then requests it over HTTP. Chained behind CVE-2026-64961, neither of these needs a real account at all.

**The rest of the set, by class.** Server-side request forgery in the import functionality (CVE-2026-64968) lets an authenticated administrator make the server reach arbitrary internal HTTP endpoints and cloud-metadata addresses. Two further path traversals allow cross-course file access where a specific configuration option is enabled (CVE-2026-64963) and arbitrary file reads through the error-log viewer with administrative privileges (CVE-2026-64967). There is a missing authorization check on the test and question import endpoints (CVE-2026-64965), an insecure direct object reference letting any authenticated user — a student included — supply another user's member identifier in a POST request to the profile album endpoint and **permanently delete that user's profile picture, including those of instructors and administrators** (CVE-2026-64969), which is an integrity effect rather than a disclosure one, cross-site request forgery on profile update (CVE-2026-64962), and three cross-site scripting flaws: stored XSS through registration that fires when an authenticated user views the attacker's public profile (CVE-2026-64970), and reflected XSS in the restore functionality (CVE-2026-64971) and via the `popup` parameter in `preview.php`, where injecting a double quote breaks out of the attribute value to append an event handler (CVE-2026-64972).

**Why an abandoned niche product still clears the bar for this constituency.** Education and research sit inside the profiled remit, and a learning management system holds student and staff identity data while typically running as a long-lived, lightly-owned web application. The usual triage question — can we wait for the vendor's next release? — has no answer here, because the timeline is not set by exploitation signal or by a patch cadence but by the permanent absence of a maintainer. CERT Polska reports no exploitation and publishes no CVSS score for any of the thirteen, and this entry invents neither; what makes the item actionable regardless is that the exposure cannot decay.

**Detection.** With no patch to apply, the realistic controls are exposure and behaviour. For the pre-auth token forgery the signal is an authenticated session appearing for an account with no preceding credential submission — a successful auto-login request followed immediately by privileged actions, with no corresponding login-form POST or password-reset flow in the application's own access log. For the two upload paths, watch for a request writing a file with a server-executable extension into a web-served directory, followed within seconds by a GET for that same path: the request pair is the signal, and it is visible in web-server access logs without any application instrumentation. The server-side request forgery shows up as outbound HTTP from the web-application host to link-local metadata addresses or internal-only ranges, which a well-behaved learning platform never originates.

**Defender takeaway:** treat this as a decommissioning decision rather than a patch decision. Any ATutor instance reachable from the internet should come off it now — behind a VPN or authenticating reverse proxy at minimum — because the pre-authentication flaw hands over an administrator session and nothing will ever close it. Where an instance must keep running, the compensating controls that map onto the specific mechanics are: block or authenticate the auto-login endpoint at the proxy, deny execution of scripts from upload directories at the web-server layer, and egress-restrict the application host so the import-side request forgery cannot reach metadata services. Given the flaws span registration, profile, import, restore and log-viewing surfaces, a migration plan to a maintained platform is the only durable answer.
