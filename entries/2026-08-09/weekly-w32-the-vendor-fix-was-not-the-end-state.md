---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-top-stories
title: "Six independent disclosures this week ended with the same result: the vendor's fix was applied and the estate was still exposed — a bypassable hotfix, a fix that reintroduced the bug, a patch build that was itself the affected version, and an actor observed rolling a patch back"
headline: "If you patched this week you may still be exposed — six vendors' own fixes failed to end the exposure"
summary: >
  Across 2026-W32 six unrelated products produced the same defender outcome: applying the vendor's remediation
  did not close the exposure. N-able's day-one N-central fix proved bypassable and its Hotfix 2 now supersedes
  the build this pipeline named as the remedy; Apache states CVE-2026-34486 exists because of "an error in the
  fix for CVE-2026-29146"; Adobe's Campaign Classic build 9398, shipped on 29 July as the fix for one critical
  wave, is the affected version of the next; a new Flowise CVE bypasses the fix for an earlier one; Apple
  patched a Screen Sharing authentication bypass a week after a researcher said the prior fix in that daemon
  shipped as a denial-of-service entry; and Rapid7 observed INC Ransom rolling an applied SonicWall SMA patch
  back to keep access. Version state is not eviction state.
discovered_at: "2026-08-09T23:45:00Z"
event_date: "2026-08-06"
run_id: 2026-08-09T2315Z-weekly
priority: high
immediate_action: null
tags: [vulnerabilities, actively-exploited, patch-available, ransomware, auth-bypass]
regions: [global, europe]
sectors: [public-sector, technology]
entities:
  - actor:inc-ransom
techniques: [T1190, T1072, T1219, T1572, T1601.002, T1210]
affected_products: ["N-able N-central", "Apache Tomcat", "Adobe Campaign Classic", "Flowise", "Apple macOS", "SonicWall SMA 1000"]
cves: []
sources:
  - url: "https://status.n-able.com/2026/08/06/n-central-2026-3-hotfix-2-additional-mitigation-for-cve-2026-18577/"
    publisher: "N-able"
    date: "2026-08-06"
    role: primary
  - url: "https://www.n-able.com/blog/n-central-security-update-august-2-2026"
    publisher: "N-able"
    date: "2026-08-06"
    role: primary
  - url: "https://tomcat.apache.org/security-11.html"
    publisher: "Apache Software Foundation (Tomcat security team)"
    date: "2026-04-09"
    role: primary
  - url: "https://helpx.adobe.com/security/products/campaign/apsb26-120.html"
    publisher: "Adobe PSIRT"
    date: "2026-08-03"
    role: primary
  - url: "https://helpx.adobe.com/security/products/campaign/apsb26-114.html"
    publisher: "Adobe PSIRT"
    date: "2026-07-29"
    role: primary
  - url: "https://reverse.put.as/2026/07/29/its-a-pre-auth-stupid/"
    publisher: "fG! (reverse.put.as)"
    date: "2026-07-29"
    role: corroborating
  - url: "https://www.resecurity.com/blog/article/from-wsproxy-to-root-inc-ransomware-and-sonicwall-sma-exploit-chain"
    publisher: "Resecurity"
    date: "2026-08-01"
    role: corroborating
  - url: "https://www.vulncheck.com/advisories/flowise-authentication-bypass-via-oauth2-credential-refresh-endpoint"
    publisher: "VulnCheck (CNA)"
    date: "2026-08-07"
    role: primary
  - url: "https://support.apple.com/en-us/148170"
    publisher: "Apple"
    date: "2026-08-06"
    role: primary
  - url: "https://www.darkreading.com/vulnerabilities-threats/inc-ransomware-exploits-sonicwall-sma-zero-days"
    publisher: "Dark Reading"
    date: "2026-07-17"
    role: corroborating
  - url: "https://www.sophos.com/en-us/blog/nable-ncentral-exploitation-results-in-rmm-tool-deployment"
    publisher: "Sophos X-Ops (Counter Threat Unit)"
    date: "2026-08-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This is not a duplicate of our previous communication — Hotfix 2 is required, even if you already applied the earlier hotfix. Hotfix 2 supersedes Hotfix 1 with additional hardening measures to further protect you and your customers."
    publisher: "N-able"
  - quote: "An error in the fix for CVE-2026-29146 allowed the EncryptInterceptor to be bypassed."
    publisher: "Apache Software Foundation (Tomcat security team)"
  - quote: "We observed the threat actor maintaining persistence and rolling the newly applied patch back to a vulnerable state to maintain access. A comprehensive forensic review of the firewall is required to ensure complete eviction."
    publisher: "Dark Reading"
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references:
  - 2026-08-03/cve-2026-18577-n-able-n-central-auth-bypass-exploited
  - 2026-08-05/cve-2026-34486-tomcat-encryptinterceptor-fail-open-kev
  - 2026-08-07/adobe-campaign-classic-apsb26-120-second-wave-unauth-rce
  - 2026-08-08/flowise-three-cves-vendor-sunset-no-fix-coming
  - 2026-08-08/cve-2026-65400-macos-screen-sharing-auth-state-bypass
  - 2026-07-14/sonicwall-sma1000-ssrf-cve-2026-15409-actively-exploited
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

**If you did nothing this week:** nothing changed. If you *patched* this week, six separate products could still leave you exposed — because the fix was bypassable, was superseded, was itself the affected build, or was rolled back by someone already inside.

The clearest case is the one that is actively exploited. N-able confirmed in-the-wild exploitation of an authentication bypass giving unauthenticated administrative access to the N-central RMM console, and then confirmed that its own earlier remediation had failed, issuing a second identifier for an alternative path to the same flaw that the first fix did not mitigate ([N-able, 2026-08-06](https://www.n-able.com/blog/n-central-security-update-august-2-2026)). It then shipped Hotfix 2 with language that leaves no room for interpretation — "Hotfix 2 is required, even if you already applied the earlier hotfix. Hotfix 2 supersedes Hotfix 1" ([N-able, 2026-08-06](https://status.n-able.com/2026/08/06/n-central-2026-3-hotfix-2-additional-mitigation-for-cve-2026-18577/)). This pipeline named build 2026.3.1.7 as the remedy on 3 August; that build is no longer sufficient. Between those two dates Sophos X-Ops published what the actor does with the console once it has it — reaching "high-value endpoints such as a backup server, domain controllers, and application servers" from the compromised N-central server ([Sophos X-Ops, 2026-08-04](https://www.sophos.com/en-us/blog/nable-ncentral-exploitation-results-in-rmm-tool-deployment)) — which is why upgrading the server is the start of the work rather than the end of it.

Three more cases are failures of the fix itself rather than of its coverage. The Apache Tomcat security team's own description of CVE-2026-34486, which CISA added to its exploited-vulnerabilities catalogue on 4 August, is that "an error in the fix for CVE-2026-29146 allowed the EncryptInterceptor to be bypassed" — so the affected set is limited to the releases that carried that broken fix; on the 11.x line that is 11.0.20, fixed in 11.0.21 ([Apache Tomcat, 2026-04-09](https://tomcat.apache.org/security-11.html)). Adobe published APSB26-120 on 3 August for seven flaws in on-premise Campaign Classic v7, three of them unauthenticated CVSS 10.0 paths to code execution, with the affected range given as "7.4.3 build 9398 and earlier" ([Adobe PSIRT, 2026-08-03](https://helpx.adobe.com/security/products/campaign/apsb26-120.html)) — and build 9398 is the release Adobe shipped five days earlier, in APSB26-114, to close the preceding critical wave ([Adobe PSIRT, 2026-07-29](https://helpx.adobe.com/security/products/campaign/apsb26-114.html)). In Flowise, CVE-2026-70636 lets an unauthenticated caller reach the OAuth2 credential-refresh endpoint by appending a trailing identifier that defeats prefix-based whitelist matching in the auth middleware — which VulnCheck records as a bypass of the earlier fix for CVE-2026-41273 ([VulnCheck, 2026-08-07](https://www.vulncheck.com/advisories/flowise-authentication-bypass-via-oauth2-credential-refresh-endpoint)). Apple's fifth case is adjacent rather than identical: macOS 26.6.1 and its siblings fix CVE-2026-65400, where "an attacker on the network may be able to authenticate to Screen Sharing without valid credentials" ([Apple, 2026-08-06](https://support.apple.com/en-us/148170)), one week after the reverse-engineer fG! publicly described a separate pre-authentication bug in the same `screensharingd` daemon which he says Apple had closed under a denial-of-service entry in the preceding bulletin ([fG!, 2026-07-29](https://reverse.put.as/2026/07/29/its-a-pre-auth-stupid/)) — a characterisation Apple has not endorsed.

The sixth case is the one that generalises the others, because it removes the assumption underneath all patch-state reporting. Rapid7's account of the SonicWall SMA 1000 chain is that the actor did not merely survive remediation but undid it: "We observed the threat actor maintaining persistence and rolling the newly applied patch back to a vulnerable state to maintain access. A comprehensive forensic review of the firewall is required to ensure complete eviction" ([Dark Reading, 2026-07-17](https://www.darkreading.com/vulnerabilities-threats/inc-ransomware-exploits-sonicwall-sma-zero-days)). Resecurity's parallel analysis makes the same point about artefacts rather than versions, noting that setuid binaries, Python injectors, modified init scripts and web-server configuration changes "can survive reboots and may persist after a superficial firmware upgrade if not remediated" ([Resecurity, 2026-08-01](https://www.resecurity.com/blog/article/from-wsproxy-to-root-inc-ransomware-and-sonicwall-sma-exploit-chain)).

**Defender takeaway:** a reported version number is a claim about the last thing an administrator did, not a claim about who else has access. For any product on this list that sat exposed during its window, the operation is a compromise assessment against artefacts — services registered, accounts created, init and configuration changes, tunnel clients — followed by a *re-check* of patch state after remediation, because on at least one of these the actor's move was to put the vulnerable code back. Where a vendor's advisory is the trigger for your patch cycle, subscribe to its status or hotfix channel and not only its CVE feed: two of these six supersessions were announced on a status page, not in a new advisory.

**Triage:** the benign lookalike for all of this is ordinary patch and maintenance activity, and the discriminator is authorship and sequence. A version downgrade or a firmware rollback on an edge appliance is a rare, deliberate operation — correlate every observed version regression against your own change record, and treat an unexplained one as intrusion evidence rather than administrative error. On managed-endpoint platforms, the tell is a tunnelling or remote-access client registered as a service on hosts *below* the management server rather than on the server itself, since a legitimate administrator deploys tooling from the console rather than leaving per-endpoint services behind.
