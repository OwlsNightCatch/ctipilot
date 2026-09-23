---
schema: 1
kind: vulnerability
title: >
  CVE-2026-67279 / CVE-2026-86060 — MikroTik RouterOS "MikroTrick": an SSH rekey-during-
  authentication state-confusion bypass chained with a crafted-username privilege escalation
  reaches unauthenticated full device takeover, actively exploited
headline: >
  CERT Polska confirms active exploitation of an unauthenticated SSH takeover chain against
  internet-exposed MikroTik RouterOS devices
summary: >
  CERT Polska coordinated disclosure of six MikroTik RouterOS vulnerabilities on 2026-09-05 and
  confirms active exploitation of two of them — CVE-2026-67279 and CVE-2026-86060 — chained to
  take full unauthenticated control of any device whose SSH service is reachable from the
  internet, regardless of configuration. CVE-2026-67279, an SSH rekey-during-authentication
  state-confusion bug, affects RouterOS 6.0.0 before 6.49.21, 7.0.0 before 7.23.4 and 7.24 before
  7.24.2; a separate, narrower RSA-key-impersonation flaw (CVE-2026-67276) was wrongly associated
  with this chain in earlier reporting and is not confirmed exploited. Fixed in 6.49.21, 7.23.4,
  7.24.2 and 7.25beta3 (2026-09-03); administrators must update immediately and audit
  configuration for unknown users regardless of the vendor's post-update compromise check.
discovered_at: "2026-09-06T04:35:00Z"
updated_at: "2026-09-11T04:46:00Z"
event_date: "2026-09-05"
run_id: 2026-09-06T0409Z-intel
priority: critical
immediate_action:
  title: "Patch every internet-reachable MikroTik RouterOS device now and audit for unauthorized accounts"
  action: >
    CERT Polska has independent confirmation of ongoing, successful attacks against MikroTik
    RouterOS devices whose SSH service is reachable from the internet, running since at least
    2026-09-02 and continuing as of publication. Update to 6.49.21, 7.23.4, 7.24.2 or 7.25beta3
    immediately; where an update cannot land within hours, remove SSH, WWW/WWW-SSL and the
    bandwidth-test service from any interface reachable outside a trusted management network.
    After updating, check the system log for the compromise markers and the device's own
    "Flagged" status, and inspect the configuration for unrecognized users, scripts, scheduler
    tasks, proxies and tunnels regardless of what the Flagged check reports.
tags: [vulnerabilities, rce, auth-bypass, pre-auth, actively-exploited, zero-day, cisa-kev]
regions: [global]
sectors: [public-sector, technology, telco]
entities: ["trend:mikrotik-routeros-mikrotrick-2026-09", "product:mikrotik-routeros"]
techniques: [T1190, T1068, T1136.001, T1557, T1005, T1499.004]
affected_products: ["MikroTik RouterOS"]
cves:
  - id: CVE-2026-67276
    cvss: "9.2"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "7.9 before 7.23.4; 7.24 before 7.24.2"
    fixed: "7.23.4 (LTS) / 7.24.2 (stable) / 7.25beta3"
  - id: CVE-2026-86060
    cvss: "9.2"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev]
    affected: "6.0.0 before 6.49.21; 7.0.0 before 7.23.4; 7.24 before 7.24.2"
    fixed: "6.49.21 (LTS) / 7.23.4 (LTS) / 7.24.2 (stable) / 7.25beta3"
  - id: CVE-2026-67277
    cvss: "8.8"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev]
    affected: "6.0.0 before 6.49.21; 7.0.0 before 7.23.4; 7.24 before 7.24.2"
    fixed: "6.49.21 (LTS) / 7.23.4 (LTS) / 7.24.2 (stable) / 7.25beta3"
  - id: CVE-2026-67278
    cvss: "6.3"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "7.0.0 before 7.23.4; 7.24 before 7.24.2"
    fixed: "7.23.4 (LTS) / 7.24.2 (stable) / 7.25beta3"
  - id: CVE-2026-67279
    cvss: "6.9"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited]
    affected: "6.0.0 before 6.49.21; 7.0.0 before 7.23.4; 7.24 before 7.24.2"
    fixed: "6.49.21 (LTS) / 7.23.4 (LTS) / 7.24.2 (stable) / 7.25beta3"
  - id: CVE-2026-67281
    cvss: "8.7"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "7.20 before 7.23.4; 7.24 before 7.24.2"
    fixed: "7.23.4 (LTS) / 7.24.2 (stable) / 7.25beta3"
sources:
  - url: "https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/"
    publisher: "CERT Polska (NASK)"
    date: "2026-09-05"
    role: primary
  - url: "https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve"
    publisher: "CERT Polska (NASK) — per-CVE detail page"
    date: "2026-09-05"
    role: primary
  - url: "https://mikrotik.com/supportsec/september-2026-vulnerability/"
    publisher: "MikroTik (vendor security bulletin)"
    date: "2026-09-03"
    role: primary
  - url: "https://npratley.net/reversing-mikrotiks-silent-patch-the-routeros-7-23-4-fix-they-wouldnt-explain/"
    publisher: "Nick Pratley (independent reverse-engineering write-up)"
    date: "2026-09-04"
    role: corroborating
  - url: "https://cert.pl/en/posts/2026/09/mikrotrick-technical-analysis/"
    publisher: "CERT Polska (NASK) — technical analysis"
    date: "2026-09-22"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV"
    date: "2026-09-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "MikroTik RouterOS contains a missing authenticaion for critical function vulnerability which allows kernel memory disclosure and denial of service in the btest service."
    publisher: "CISA KEV"
    source_url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
  - quote: "We have obtained confirmation that the attackers are exploiting this combination of vulnerabilities to take full control of devices whose SSH service is accessible from public networks. It has also been confirmed that the released patches prevent the observed attacks."
    publisher: "CERT Polska"
    source_url: "https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/"
  - quote: "RouterOS did not properly verify public keys used for SSH authentication - in particular, it did not compare the entire RSA public key assigned to a user."
    publisher: "CERT Polska"
    source_url: "https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/"
  - quote: "Because signature verification uses the client-supplied key, an attacker knowing an authorized RSA modulus can supply a key with exponent one, forge a valid signature, and open an SSH command channel as the target user without the private key."
    publisher: "CERT Polska (NASK) — per-CVE detail page"
    source_url: "https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve"
  - quote: "Exploitation requires an unauthenticated SSH session to reach the RouterOS login helper."
    publisher: "CERT Polska (NASK) — per-CVE detail page"
    source_url: "https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve"
  - quote: "the successful attacks observed so far, including the creation of the \"ops\" account"
    publisher: "CERT Polska"
    source_url: "https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/"
  - quote: "This mechanism detects only selected traces left after a compromise - the absence of the marker is not proof that the device is safe."
    publisher: "CERT Polska (NASK)"
    source_url: "https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/"
verification: multi-source
sourcing_note: >
  CERT Polska is both the discovering researcher and the coordinating national CERT for this
  disclosure — a single organization wearing both roles, but corroborated independently by
  MikroTik's own vendor bulletin (which confirms the fixed versions and the "Flagged" mechanism
  without confirming exploitation itself) and by an independent researcher's reverse-engineering
  of the patch diff, which reproduced the crafted-username privilege-mask override in a controlled
  test but states plainly that it did not reproduce a credential-free way to make RouterOS accept
  the crafted username in the first place — leaving CERT Polska's own combination of the two CVEs,
  rather than the researcher's account, as this entry's basis for the unauthenticated attack path.
confidence: high
references: []
deep_dive: true
deep_dive_category: firewall-vpn-rce
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Update every MikroTik RouterOS device to 6.49.21, 7.23.4, 7.24.2 or 7.25beta3 now; where SSH, WWW/WWW-SSL or the bandwidth-test service are reachable from outside a trusted management network and an immediate update is not possible, remove that reachability first."
  - "After updating, check the system log for a device-compromise message and the /system/device-mode/print Flagged status, and audit the configuration for any user, script, scheduler task, proxy server or tunnel you do not recognize — the Flagged marker only catches known post-compromise traces and its absence does not clear a device."
updates:
  - at: "2026-09-11T04:46:00Z"
    run_id: 2026-09-11T0410Z-intel
    type: update
    summary: >
      CISA added CVE-2026-67277 (the bandwidth-test kernel-memory-disclosure/DoS flaw among the
      four lower-severity CVEs in this disclosure) to its Known Exploited Vulnerabilities catalog
      on 2026-09-10, confirming active in-the-wild exploitation — this entry previously stated
      none of the four lower-severity CVEs was confirmed separately exploited. Separately, this
      entry's per-CVE `affected` field had wrongly applied all three RouterOS branches (6.0.0,
      7.0.0, 7.24) uniformly to all six CVEs; cross-checked against CERT Polska's own per-CVE page
      and the MITRE CVE record, only CVE-2026-86060, CVE-2026-67277 and CVE-2026-67279 genuinely
      carry all three branches — CVE-2026-67276 (the exploited chain's entry-point flaw) starts at
      7.9, CVE-2026-67278 at 7.0.0, and CVE-2026-67281 at 7.20, none of them reaching the 6.x
      branch. Corrected per-CVE and fixed frontmatter summary accordingly.
    fields: [summary, cves, sources, evidence, body]
  - at: "2026-09-23T04:35:00Z"
    run_id: 2026-09-23T0405Z-intel
    type: correction
    summary: >
      CERT Polska's own technical write-up (2026-09-22) corrects this entry's account of the
      exploited chain: CVE-2026-67276 is not the chain's entry point and is not confirmed
      exploited as part of MikroTrick — it is a separate, narrower RSA-key-impersonation flaw
      needing a known account and modulus in advance, limited to that one account. The actual,
      configuration-independent entry point is CVE-2026-67279, an SSH rekey-during-authentication
      state-confusion bug that lets an unauthenticated client reach channel handling without ever
      completing authentication. Corrected the title, summary, the two CVE records' exploitation
      status and the body's mechanism description accordingly, and added the RouterOS Flagged
      mechanism's exact trigger condition.
    fields: [title, summary, tags, cves, sources, entities, body]
migrated_from: null
---

CERT Polska (NASK) coordinated disclosure of six MikroTik RouterOS vulnerabilities on 2026-09-05, naming the combination that yields unauthenticated full device takeover "MikroTrick," and states plainly that it has independent confirmation of ongoing, successful attacks against RouterOS devices whose SSH service is reachable from the internet ([CERT Polska, 2026-09-05](https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/)). The exploited chain combines two flaws in RouterOS's SSH authentication path. CVE-2026-67279 (CVSS 6.9) is a protocol state-confusion defect: when a client initiates an SSH key re-exchange before completing user authentication, the RouterOS SSH server "unconditionally moved from the temporary rekey state to channel handling instead of resuming the interrupted authentication," accepting a session channel despite never sending `SSH_MSG_USERAUTH_SUCCESS` ([CERT Polska, technical analysis, 2026-09-22](https://cert.pl/en/posts/2026/09/mikrotrick-technical-analysis/)). This does not by itself grant an authenticated identity or any privilege, but it is the precondition CVE-2026-86060 (CVSS 9.2, CWE-88 argument injection) then abuses: RouterOS's login helper accepts a username beginning with a hyphen as a command-line option rather than literal text, so a username of "-2" makes the helper read a replacement username and policy mask from file descriptor 2 — the same pseudoterminal the SSH channel already controls — letting the attacker supply their own privilege mask over the SSH channel itself and escalate to full administrative privilege ([CERT Polska, technical analysis, 2026-09-22](https://cert.pl/en/posts/2026/09/mikrotrick-technical-analysis/)). No credential, no key, and no completed authentication stands between internet reach to the SSH port and full device compromise. A third, narrower flaw, CVE-2026-67276, was wrongly associated with this chain in some earlier reporting; CERT Polska's own technical write-up states it "is a separate vulnerability that allows an attacker to impersonate a user authenticated with an RSA key," requiring the target account name and RSA modulus in advance and granting access only to that one account — "significantly less suitable for a mass attack that works regardless of device configuration" ([CERT Polska, technical analysis, 2026-09-22](https://cert.pl/en/posts/2026/09/mikrotrick-technical-analysis/)) — and it is not confirmed separately exploited.

An independent researcher's reverse-engineering of the silent 2026-09-03 patch traces the mechanics of the crafted-username step in more detail: the SSH daemon invokes a legacy login helper via a system call, passing the authenticated username and a decimal policy-mask value as trailing positional arguments, and that helper's undocumented legacy transport treats any positional argument beginning with a hyphen as a file-descriptor number, reading up to 4096 bytes from it and splitting the result on null bytes into a replacement identity and a replacement policy mask (Nick Pratley, 2026-09-04). The researcher reproduced full policy-mask override once a username matching this pattern was accepted, but did not reproduce a stock, credential-free way to make SSH accept that username in the first place — leaving CERT Polska's combination of the two coordinated CVEs, rather than this third-party analysis, as the authoritative description of the unauthenticated attack path. CERT Polska's own investigation of the observed intrusions found the operators create a highly-privileged local account after exploitation, with the log sequence recording a failed login for a numeric pseudo-user immediately followed by that user's creation over the same SSH session, and states this activity has been occurring since at least 2026-09-02 ([CERT Polska, 2026-09-05](https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/)).

Three further CVEs round out the coordinated disclosure at lower severity, alongside CVE-2026-67276 above. CVE-2026-67277 (CVSS 8.8) lets an unauthenticated client reach the bandwidth-test service's post-authentication code path; combined with disclosure of uninitialized kernel packet-buffer contents and an integer-underflow size-validation bug, this yields kernel memory leakage or a remote denial-of-service that restarts the device ([CERT Polska, CVE detail page, 2026-09-05](https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve)); CISA added it to its Known Exploited Vulnerabilities catalog on 2026-09-10, confirming active in-the-wild exploitation ([CISA KEV, catalogue version 2026.09.10](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). CVE-2026-67278 and CVE-2026-67281 are not confirmed separately exploited. CVE-2026-67278 (CVSS 6.3) lets an attacker who can intercept or redirect an outbound RouterOS TLS connection forge a trusted intermediate certificate for arbitrary hostnames, because RouterOS accepts malformed RSA/PKCS#1 v1.5 signatures during X.509 validation and its trust store ships a root CA with public exponent 3 — enabling TLS server impersonation against the device's own outbound connections without the root's private key. CVE-2026-67281 (CVSS 8.7) is an unauthenticated file-read in the WebFig `/jsproxy` path: a newly allocated session retains a stale, uninitialized pointer used for file-authorization checks, and an attacker who can influence allocator state and supplies parent-directory traversal components in an encrypted URI can escape the WebFig file namespace and disclose root-owned files, including credential-bearing configuration stores.

All six are fixed in RouterOS 7.25beta3, 7.24.2, 7.23.4 and 6.49.21, released 2026-09-03; MikroTik pushed a first-ever in-app push notification to administrators alongside the release ([CERT Polska, 2026-09-05](https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/)). The fixed releases add a startup "Flagged" self-check that scans configuration for known post-compromise traces, disables recognized suspicious entries, and logs a critical warning — but CERT Polska is explicit that this mechanism detects only selected traces left after a compromise, and its absence is not proof that a device is safe ([CERT Polska, 2026-09-05](https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/)).

CERT Polska states the six flaws were found using an agentic research environment built on OpenAI's GPT-5.5-cyber and GPT-5.6-sol models under the OpenAI Government and Trust Agency Collaboration program, automating protocol-state-machine modelling and binary-diff hypothesis generation inside an isolated RouterOS lab, with every hypothesis confirmed on real hardware before publication ([CERT Polska, 2026-09-05](https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/)) — a national CERT's AI-augmented research pipeline producing an actively-exploited, pre-auth full-device-takeover chain.

Detection concept, telemetry class first: on-device system-log review is the primary hunt surface here, since these are commodity routers with no EDR agent. Alert on any SSH login-failure log entry for a non-standard, negative-looking numeric pseudo-username, especially one immediately followed within the same session window by a new-user-creation log entry — CERT Polska's own observed intrusions show exactly this sequence. Independently alert on creation of any locally-administered account with full or administrative group membership that does not correlate to a known change-management action. For the WebFig file-disclosure path, web-access logs showing `/jsproxy` requests carrying encoded parent-directory traversal sequences are the anchor; for the bandwidth-test flaw, unexpected inbound connections to that service from unauthenticated sources, or device reboots correlated with such connections, are the observable. **Triage:** a device's own "Flagged" status is a useful positive signal but never a negative one — treat it as one input alongside the log markers above, not as a clearance check, per the vendor and CERT Polska's shared caution.

**Defender takeaway:** patch every internet-reachable RouterOS device now regardless of whether it shows signs of compromise, and treat any device that was running an unpatched, internet-exposed SSH service before 2026-09-03 as a compromise-assessment target — an unpatched update alone evicts the vulnerability but not anything already taken through it. Until every device is patched, remove SSH, WWW/WWW-SSL and the bandwidth-test service from any interface reachable outside a trusted management network, and do not originate outbound TLS connections or use RouterOS's built-in SSH client from an unpatched device toward untrusted networks or hosts, which the certificate-forgery flaw can otherwise abuse.

## Update — 2026-09-11T04:46:00Z

CISA added CVE-2026-67277 — the bandwidth-test kernel-memory-disclosure and denial-of-service flaw among this disclosure's four lower-severity CVEs — to its Known Exploited Vulnerabilities catalog on 2026-09-10, describing it as a "missing authenticaion for critical function vulnerability which allows kernel memory disclosure and denial of service in the btest service" ([CISA KEV, catalogue version 2026.09.10](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). CERT Polska's own technical analysis states CVE-2026-86060 was added to KEV the same day alongside it ([CERT Polska, technical analysis, 2026-09-22](https://cert.pl/en/posts/2026/09/mikrotrick-technical-analysis/)). CVE-2026-67277's KEV addition confirms active in-the-wild exploitation of a third vulnerability in the coordinated disclosure, beyond the two (CVE-2026-67279, CVE-2026-86060) CERT Polska had already reported exploited directly; the remaining three lower-severity CVEs (CVE-2026-67276, CVE-2026-67278, CVE-2026-67281) are still not confirmed separately exploited by any source. The remediation is unchanged — all six flaws share the same fixed releases (6.49.21, 7.23.4, 7.24.2, 7.25beta3) already covered by this entry's patch guidance. Separately, per-CVE affected-version ranges have been corrected: only CVE-2026-67277, CVE-2026-67279 and CVE-2026-86060 reach back to the 6.x branch (6.0.0 before 6.49.21); the narrower RSA-impersonation flaw, CVE-2026-67276, affects only 7.9 before 7.23.4 and 7.24 before 7.24.2, so a device on the 6.x branch is not exposed to that specific attack path ([CERT Polska, CVE detail page, 2026-09-05](https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve)) — it remains reachable via CVE-2026-86060 and the other lower-severity flaws that do affect that branch, so the same patch guidance applies to all versions regardless.

## Correction — 2026-09-23T04:35:00Z

CERT Polska's own technical analysis of MikroTrick ([CERT Polska, 2026-09-22](https://cert.pl/en/posts/2026/09/mikrotrick-technical-analysis/)) states plainly that "some publications incorrectly associated CVE-2026-67276 with the MikroTrick chain" — it "is a separate vulnerability that allows an attacker to impersonate a user authenticated with an RSA key," requiring the target account name and RSA modulus in advance and granting access only to that one account, "significantly less suitable for a mass attack that works regardless of device configuration." This entry previously named CVE-2026-67276 as the chain's forged-signature entry point; that attribution is wrong, and CERT Polska does not confirm CVE-2026-67276 as separately exploited in the wild. The actual, configuration-independent entry point is CVE-2026-67279: "vulnerable versions of the RouterOS SSH server handled a rekey initiated during user authentication incorrectly. When the rekey finished, the server unconditionally moved from the temporary rekey state to channel handling instead of resuming the interrupted authentication" ([CERT Polska, technical analysis, 2026-09-22](https://cert.pl/en/posts/2026/09/mikrotrick-technical-analysis/)) — reaching a session channel despite never completing authentication, the precondition CVE-2026-86060's crafted "-2" username then abuses to set an attacker-controlled policy mask. The exploitation status is corrected accordingly: CVE-2026-67276 moves from exploited to patch-available and CVE-2026-67279 moves from patch-available to exploited, both now classed as auth-bypass. Separately, the fixed releases' Flagged self-check specifically watches at startup for an "ops" account newly created in the privileged "full" group, disabling it and logging a warning when found — a more precise trigger than this entry previously stated.
