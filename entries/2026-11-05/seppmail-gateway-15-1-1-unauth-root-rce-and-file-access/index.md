---
schema: 1
kind: vulnerability
title: "CVE-2026-114424 and CVE-2026-114425, SEPPmail Secure Email Gateway before 15.1.1: an unauthenticated mail sender can reach root command execution through a replacement rule and root file access through Large File Transfer, with three more flaws fixed in the same release and no fix for the 15.0 branch (CVSS 4.0 9.2)"
headline: "SEPPmail gateway: unauthenticated sender reaches root RCE or file access; fixed in 15.1.1, 15.0.x has no fix"
summary: >
  SEPPmail's patch release 15.1.1 of 2026-11-03 fixes five flaws in the Secure Email Gateway, with NCSC.ch as the CNA: CVE-2026-114424 lets an
  unauthenticated remote sender run operating-system commands as root through an active address-replacement rule that uses message-derived
  data, and CVE-2026-114425 lets one disclose, move or delete files as root when Large File Transfer is enabled (both CVSS 4.0 9.2). The
  vendor says 15.0.7 was the last 15.0 release, so 15.0.x gateways must move to the 15.1 branch; no source reports exploitation.
discovered_at: "2026-11-05T03:58:00Z"
updated_at: null
event_date: "2026-11-03"
run_id: 2026-11-05T0255Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [switzerland, dach]
sectors: []
entities: ["product:seppmail-secure-e-mail-gateway"]
techniques: [T1190, T1059]
affected_products: ["SEPPmail Secure E-Mail Gateway"]
cves:
  - id: CVE-2026-114424
    cvss: "9.2 (CVSS 4.0)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure Email Gateway before 15.1.1, 15.0.x included; reachable only where an active rule uses message-derived replacement data and its search condition matches"
    fixed: "15.1.1 (patch release of 2026-11-03); no 15.0.x fix, 15.0.7 of 2026-09-02 is the last 15.0 release"
  - id: CVE-2026-114425
    cvss: "9.2 (CVSS 4.0)"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure Email Gateway before 15.1.1, 15.0.x included; reachable only where Large File Transfer is enabled and the message reaches an affected secure-mail processing path"
    fixed: "15.1.1 (patch release of 2026-11-03); no 15.0.x fix"
  - id: CVE-2026-114426
    cvss: "8.7 (CVSS 4.0)"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure Email Gateway before 15.1.1, 15.0.x included"
    fixed: "15.1.1 (patch release of 2026-11-03); no 15.0.x fix"
  - id: CVE-2026-114421
    cvss: "8.3 (CVSS 4.0)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure Email Gateway before 15.1.1, 15.0.x included; GINA webmail accounts that were created but not registered and still have an empty initial password"
    fixed: "15.1.1 (patch release of 2026-11-03); no 15.0.x fix"
  - id: CVE-2026-114420
    cvss: "6.9 (CVSS 4.0)"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SEPPmail Secure Email Gateway before 15.1.1, 15.0.x included; GINA web interface account selection"
    fixed: "15.1.1 (patch release of 2026-11-03); no 15.0.x fix"
sources:
  - url: "https://docs.seppmail.com/en/20_revision-history.html"
    publisher: "SEPPmail GmbH (revision history)"
    date: "2026-11-03"
    role: primary
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116781"
    publisher: "ENISA EUVD (CNA text of NCSC.ch, CVE-2026-114424)"
    date: "2026-11-04"
    role: primary
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116782"
    publisher: "ENISA EUVD (CNA text of NCSC.ch, CVE-2026-114425)"
    date: "2026-11-04"
    role: primary
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116796"
    publisher: "ENISA EUVD (CNA text of NCSC.ch, CVE-2026-114426)"
    date: "2026-11-04"
    role: corroborating
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116798"
    publisher: "ENISA EUVD (CNA text of NCSC.ch, CVE-2026-114421)"
    date: "2026-11-04"
    role: corroborating
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116797"
    publisher: "ENISA EUVD (CNA text of NCSC.ch, CVE-2026-114420)"
    date: "2026-11-04"
    role: corroborating
  - url: "https://docs.seppmail.com/en/07_mi_04_home.html"
    publisher: "SEPPmail GmbH (administration guide, Home page, undated)"
    date: "2026-11-05"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An unauthenticated remote sender can execute operating-system commands in the mail-processing worker context when an active rule uses message-derived replacement data and its search condition matches. The validated worker context was root."
    publisher: "ENISA EUVD (CNA text of NCSC.ch, CVE-2026-114424)"
    source_url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116781"
  - quote: "An unauthenticated remote sender can cause the mail-processing worker to disclose, move, or delete an accessible regular file when LFT is enabled and the message reaches an affected secure-mail processing path. The validated workers ran as root."
    publisher: "ENISA EUVD (CNA text of NCSC.ch, CVE-2026-114425)"
    source_url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116782"
  - quote: "This release will be the last release in the 15.0 branch and enable the update to version 15.1."
    publisher: "SEPPmail GmbH (revision history)"
    source_url: "https://docs.seppmail.com/en/20_revision-history.html"
verification: single-source
sourcing_note: >
  NCSC.ch, the CNA for this Swiss vendor, and SEPPmail's own revision history describe the same five flaws, so they count as one assessor. The
  exposure conditions come from the CNA text. SEPPmail's page lists the scores of CVE-2026-114420 and CVE-2026-114421 the other way round
  from the CNA records, and the CNA vectors support the CNA scores, which the CVE records here carry. The vendor page's own description of the two GINA
  flaws is one shared text, and no source reports exploitation, a public proof of concept, or whether the SEPPmail Cloud service was affected.
confidence: high
references:
  - 2026-05-09/cve-2026-44128-et-al-seppmail-secure-email-gateway-cvss-9-3
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every SEPPmail Secure Email Gateway to 15.1.1 now, moving 15.0.x gateways to the 15.1 branch because 15.0.7 is the last 15.0 release, and check each gateway's active address-replacement rules for values taken from the message and its Large File Transfer setting, the two conditions the CNA names."
updates: []
migrated_from: null
---

SEPPmail's revision history lists patch release 15.1.1 of 2026-11-03 with five security fixes in the Secure Email Gateway, all for versions before 15.1.1 ([SEPPmail, 2026-11-03](https://docs.seppmail.com/en/20_revision-history.html)). Two are unauthenticated and rated 9.2: in CVE-2026-114424 attacker-influenced replacement text in sender or recipient address-replacement rules is evaluated as Perl code, so a remote sender can run operating-system commands in the mail-processing worker when an active rule uses message-derived replacement data and its search condition matches, and the validated worker context was root ([ENISA EUVD, 2026-11-04](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116781)); in CVE-2026-114425 a file path supplied in the attachment metadata of an incoming message lets the worker disclose, move or delete an accessible file when Large File Transfer is enabled, also as root ([ENISA EUVD, 2026-11-04](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116782)). CVE-2026-114426 lets an unauthenticated attacker exhaust workers and disk because the upload interface processed data before checking authentication ([ENISA EUVD, 2026-11-04](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116796)), and two flaws in the GINA webmail let an unauthenticated attacker take over a created but unregistered account with an empty initial password (CVE-2026-114421) and enumerate email addresses through an unescaped LDAP filter (CVE-2026-114420) ([ENISA EUVD, 2026-11-04](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116798); [ENISA EUVD, 2026-11-04](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116797)). The vendor says 15.0.7 of 2026-09-02 is the last release of the 15.0 branch, so the fix for a 15.0.x gateway is the move to 15.1 ([SEPPmail, 2026-11-03](https://docs.seppmail.com/en/20_revision-history.html)). None of the sources read reports exploitation.

**Exposure:** a SEPPmail Secure Email Gateway before 15.1.1; the Home page of the administration interface shows the running version in the System section as "Firmware version" ([SEPPmail, retrieved 2026-11-05](https://docs.seppmail.com/en/07_mi_04_home.html)). CVE-2026-114424 applies where an active rule uses message-derived replacement data, and CVE-2026-114425 where Large File Transfer is enabled ([ENISA EUVD, 2026-11-04](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116781); [ENISA EUVD, 2026-11-04](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-116782)).

**Detection:** no source publishes an indicator. What the mechanism implies, not stated by a source: a child process or shell started by the mail-processing worker after inbound mail whose sender or recipient strings reach a replacement rule, and file operations by the Large File Transfer worker outside its storage area, both running as root.

**Defender takeaway:** upgrade to 15.1.1, moving 15.0.x gateways to the 15.1 branch because 15.0 gets no fix, and until then review which active replacement rules use values taken from the message and whether Large File Transfer is enabled, the two conditions the CNA names ([SEPPmail, 2026-11-03](https://docs.seppmail.com/en/20_revision-history.html)). Because the worker runs as root, a gateway that was exposed with such a rule or with Large File Transfer enabled warrants a compromise check.
