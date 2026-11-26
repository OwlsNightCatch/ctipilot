---
schema: 1
kind: vulnerability
title: "Claroty Team82: Danfoss AK-SM 800A refrigeration system managers: undocumented 'code-of-the-day' authentication bypass and post-authentication command-injection RCE with thousands of publicly accessible management interfaces"
headline: "Danfoss AK-SM 800A hidden 'code-of-the-day' login is on CISA's exploited list; two post-auth flaws follow"
summary: >
  Companion disclosure to Claroty's Copeland research, same team and publish day. Danfoss AK-SM
  800A refrigeration system managers, used in supermarkets, cold-storage facilities and warehouses,
  carry an undocumented 'code-of-the-day' authentication bypass (CVE-2025-41450) that Claroty says gives a fully
  authenticated administrative session and that Danfoss and CISA describe as generating a web report with internal IPs,
  usernames and store names, a post-authenticated OS command injection in the alarm-email configuration
  (CVE-2025-41451), and an Nginx configuration-injection flaw enabling denial of service (CVE-2025-41452). Claroty's search of
  public internet-scan platforms found thousands of exposed management interfaces. CISA added CVE-2025-41450 to its Known Exploited Vulnerabilities
  catalogue on 2026-11-25 without naming a campaign.
discovered_at: "2026-08-28T06:54:00Z"
updated_at: "2026-11-26T05:07:00Z"
event_date: "2026-08-09"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, auth-bypass, actively-exploited, cisa-kev, patch-available, ot-ics]
regions: [global, europe]
sectors: [retail]
entities: []
techniques: [T1190, T1059]
affected_products: ["Danfoss AK-SM 800A"]
cves:
  - id: CVE-2025-41450
    cvss: "8.2"
    epss: null
    type: auth-bypass
    vector: user-interaction
    auth: pre-auth
    status: [cisa-kev, exploited, patch-available]
    affected: "Danfoss AK-SM 800A firmware before build 4.2"
    fixed: "Firmware build 4.2"
  - id: CVE-2025-41451
    cvss: "8.7"
    epss: null
    type: rce
    vector: user-interaction
    auth: post-auth
    status: [patch-available]
    affected: "Danfoss AK-SM 800A firmware before R4.3.1"
    fixed: "Firmware R4.3.1"
  - id: CVE-2025-41452
    cvss: "6.8"
    epss: null
    type: dos
    vector: user-interaction
    auth: post-auth
    status: [patch-available]
    affected: "Danfoss AK-SM 800A firmware before R4.3.1"
    fixed: "Firmware R4.3.1"
sources:
  - url: "https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers"
    publisher: "Claroty Team82"
    date: "2026-08-09"
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog"
    publisher: "CISA"
    date: "2026-11-25"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV catalogue"
    date: "2026-11-25"
    role: corroborating
  - url: "https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-03-01"
    publisher: "Danfoss"
    date: "2025-03-24"
    role: corroborating
  - url: "https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-08-01/"
    publisher: "Danfoss"
    date: "2025-08-01"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The application accepts a specially crafted authentication request containing a generated 'code of the day.'"
    publisher: "Claroty Team82"
  - quote: "The field value being formatted into the shell command is not sanitized according to our analysis and could potentially include OS shell directives that yield subsequent commands controlled by a potential attacker."
    publisher: "Claroty Team82"
  - quote: "An attacker could abuse it to implant arbitrary routing directives into the Internet-facing Nginx configuration."
    publisher: "Claroty Team82"
  - quote: "To understand the real-world exposure of the Danfoss AK-SM 800A, we searched publicly available internet-wide scanning platforms."
    publisher: "Claroty Team82"
  - quote: "Danfoss AK-SM 800A Series contains an improper authentication vulnerability that could allow an attacker to generate a web report exposing sensitive information, including internal IP addresses, usernames, and store names."
    publisher: "CISA KEV catalogue"
    source_url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
verification: multi-source
sourcing_note: >
  Claroty Team82 is the source for the three flaws and describes CVE-2025-41450 as giving a fully authenticated administrative session, while Danfoss's advisory DSA-2025-03-01 and CISA's catalogue describe a web report, and both are carried as the sources word them. The CVE identifiers are 2025-dated because Danfoss published its advisories on 2025-03-24 and 2025-08-01, the scores for the two post-authentication flaws are Danfoss's 8.7 and 6.8 against Claroty's v3 7.6 and 5.4, and the attack-vector ratings follow Danfoss's CVE records, which require user interaction.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade Danfoss AK-SM 800A refrigeration system managers to firmware R4.3.1 (build 4.2 closes CVE-2025-41450 alone) on every deployment, and where that cannot happen immediately take the management interface off the public internet, treating the thousands of internet-exposed devices Claroty found as a priority, because CISA lists CVE-2025-41450 as exploited."
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [body]
  - at: "2026-09-29T23:44:28Z"
    run_id: 2026-09-29T2134Z-audit
    type: improvement
    internal: true
    summary: >
      The Claroty quotation, in the evidence and in the analysis, had dropped the researchers' hedges
      ("according to our analysis", "could potentially", "a potential attacker"). Both now carry the
      sentence as Claroty wrote it. No fact changed.
    fields: [evidence, sourcing_note, body]
  - at: "2026-11-26T05:07:00Z"
    run_id: 2026-11-26T0356Z-intel
    type: update
    summary: >
      CISA added CVE-2025-41450, the code-of-the-day authentication bypass, to its Known Exploited Vulnerabilities
      catalogue on 2026-11-25 without naming a campaign; the catalogue describes it as generating a web report that
      exposes internal IP addresses, usernames and store names, while Claroty reports a full administrative session.
      Danfoss fixed it in build 4.2.
    fields: [title, headline, summary, priority, tags, sectors, cves, sources, evidence, verification, sourcing_note, actions, body, updated_at]
migrated_from: null
---

Companion disclosure to Claroty Team82's Copeland XWEB Pro research, published the same day (2026-08-09T17:59Z), covering the Danfoss AK-SM 800A refrigeration system-manager platform used in supermarkets, cold-storage facilities, warehouses and other commercial environments. Claroty found "thousands of publicly accessible management interfaces" via internet-wide scan data, using platforms including Shodan and Censys: "to understand the real-world exposure of the Danfoss AK-SM 800A, we searched publicly available internet-wide scanning platforms" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers)).

CVE-2025-41450 is a hidden, undocumented "code-of-the-day" authentication mechanism (Claroty gives CWE-287 Improper Authentication; Danfoss scores it CVSS 8.2). Claroty says the application accepts a specially crafted authentication request containing a generated "code of the day" that bypasses normal login, and that successful authentication through it "results in a fully authenticated administrative session" ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers)). Danfoss's advisory and CISA's catalogue describe the same flaw as letting an attacker generate a web report that exposes internal IP addresses, usernames and store names ([Danfoss, 2025-03-24](https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-03-01); [CISA KEV catalogue, 2026-11-25](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)), and Danfoss fixed it in firmware build 4.2 ([Danfoss, 2025-03-24](https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-03-01)). CVE-2025-41451 (CWE-77 OS Command Injection, CVSS v3 7.6) is a post-authenticated command injection in the alarm-to-email (SMTP) configuration field: a user-supplied value is formatted unsanitized into a shell command executed on the device, which Claroty used to achieve remote code execution ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers)). CVE-2025-41452 (CWE-15 External Control of System or Configuration Setting, CVSS v3 5.4) lets a post-authenticated user inject arbitrary Nginx directives via the exposed `headers.conf` include and so implant routing directives into the Internet-facing Nginx configuration, enabling denial-of-service ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers)). Danfoss shipped firmware R4.3.1 fixing CVE-2025-41451/41452 (build 4.2 for CVE-2025-41450). Danfoss's advisory scores CVE-2025-41451 at 8.7 and CVE-2025-41452 at 6.8 without naming a CVSS version ([Danfoss, 2025-08-01](https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-08-01/)), against Claroty's 7.6 and 5.4. The RCE and Nginx-injection primitives require an authenticated session. Claroty says bypassing authentication gave it the device's full administrative interface and every management function it exposed, among them email notifications, and its next finding is the command injection on the SMTP email configuration page, so on an unpatched device the bypass leads to the two post-authentication flaws ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers)).

**Triage:** Claroty says the code-of-the-day mechanism is likely intended for vendor support or maintenance, so a login by Danfoss support or by the contractor that maintains the unit is the benign lookalike and an administrative session that nobody on the operator or service-provider side opened is the signal; Claroty publishes no log field that separates them ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers)). On the post-authentication side, unexpected shell-metacharacter content in the alarm-email SMTP configuration field, or unexplained changes to the device's Nginx routing configuration, have no benign explanation for a device whose configuration should change only through documented administrative workflows.

**Exposure:** an AK-SM 800A on firmware before build 4.2 (CVE-2025-41450) or before R4.3.1 (CVE-2025-41451 and CVE-2025-41452) whose management interface is reachable from the internet; Claroty found thousands of publicly accessible management interfaces through public internet-scan platforms ([Claroty Team82, 2026-08-09](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers)), and Danfoss lists the affected range of CVE-2025-41450 as prior to version 4.2 ([Danfoss, 2025-03-24](https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-03-01)) and that of the two post-authentication flaws as prior to 4.3.1 ([Danfoss, 2025-08-01](https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-08-01/)).

**Defender takeaway:** upgrade to firmware R4.3.1 or later (build 4.2 closes only CVE-2025-41450) and take the management interface off the public internet where the upgrade cannot happen at once; CISA lists CVE-2025-41450 as exploited without naming a campaign ([CISA, 2026-11-25](https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog)).

## Update — 2026-11-26T05:07:00Z

CISA added CVE-2025-41450 to its Known Exploited Vulnerabilities catalogue on 2026-11-25 ([CISA, 2026-11-25](https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog)); the catalogue describes an improper authentication flaw that could allow an attacker to generate a web report exposing sensitive information, including internal IP addresses, usernames and store names, and names no campaign, actor or victim ([CISA KEV catalogue, 2026-11-25](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). Danfoss's advisory DSA-2025-03-01 gives the flaw CVSS 8.2, affected as AK-SM 8xxA series prior to version 4.2 and fixed by patch 4.2 ([Danfoss, 2025-03-24](https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-03-01)).
