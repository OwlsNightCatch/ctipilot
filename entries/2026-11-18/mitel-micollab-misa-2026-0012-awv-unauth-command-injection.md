---
schema: 1
kind: vulnerability
title: "Mitel MiCollab 10.3 (10.3.0.18) and earlier, MISA-2026-0012: an unauthenticated blind command injection in the Audio, Web and Video Conferencing component (CVSS 3.1 10.0) and four more flaws there, one an XML injection that can run commands (9.0); CVE-2026-133323 and CVE-2026-133303 lead the five assigned CVE ids, patch KB000129195, Accenture APEX Labs reports exploitation before the advisory and CISA lists all five as exploited since 2026-11-25"
headline: "Mitel MiCollab AWV flaws exploited pre-advisory per Accenture APEX, CISA lists them; patching alone does not evict"
summary: >
  Mitel's advisory MISA-2026-0012 of 2026-11-16, revised on 2026-11-24 to list the CVE ids, covers five flaws in the Audio, Web and Video Conferencing (AWV) component of MiCollab 10.3 (10.3.0.18) and earlier, led by an unauthenticated blind command injection scored CVSS 3.1 10.0 (CVE-2026-133323) and an unauthenticated XML injection scored 9.0 that could run commands (CVE-2026-133303). CISA added all five to its Known Exploited Vulnerabilities catalogue on 2026-11-25 without naming an actor, victim or technique, while Mitel's own page says nothing on attacks; Accenture APEX Labs reports exploitation before Mitel's 2026-11-16 advisory, with web-shell activity at one victim before 23:00 UTC on 2026-11-15 and root within about 30 minutes, so a server patched now cannot be assumed clean. Mitel offers a patch through its portal (KB000129195) and says restricting external access to the AWV component reduces the risk; the 10.3.0.18 release that Mitel named as the fix for its July advisory is itself in the affected range.
discovered_at: "2026-11-18T05:11:00Z"
updated_at: "2026-11-27T04:52:00Z"
event_date: "2026-11-16"
run_id: 2026-11-18T0356Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, actively-exploited, cisa-kev, patch-available]
regions: [global]
sectors: [technology]
entities: ["product:mitel-micollab"]
techniques: [T1190, T1059, T1505.003, T1558.003, T1685.006, T1078.002, T1560, T1068, T1041, T1105, T1087.002, T1552.001, T1572]
affected_products: ["Mitel MiCollab"]
cves:
  - id: CVE-2026-133323
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, exploited, patch-available]
    affected: "MiCollab 10.3 (10.3.0.18) and earlier, Audio, Web and Video Conferencing component"
    fixed: "patch for release 10.3 (10.3.0.18), KB000129195, or a later release"
  - id: CVE-2026-133303
    cvss: "9.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, exploited, patch-available]
    affected: "MiCollab 10.3 (10.3.0.18) and earlier, Audio, Web and Video Conferencing component"
    fixed: "patch for release 10.3 (10.3.0.18), KB000129195, or a later release"
  - id: CVE-2026-133275
    cvss: "5.3"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, exploited, patch-available]
    affected: "MiCollab 10.3 (10.3.0.18) and earlier, Audio, Web and Video Conferencing component"
    fixed: "patch for release 10.3 (10.3.0.18), KB000129195, or a later release"
  - id: CVE-2026-133311
    cvss: "5.9"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, exploited, patch-available]
    affected: "MiCollab 10.3 (10.3.0.18) and earlier, Audio, Web and Video Conferencing component"
    fixed: "patch for release 10.3 (10.3.0.18), KB000129195, or a later release"
  - id: CVE-2026-133324
    cvss: "5.3"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, exploited, patch-available]
    affected: "MiCollab 10.3 (10.3.0.18) and earlier, Audio, Web and Video Conferencing component"
    fixed: "patch for release 10.3 (10.3.0.18), KB000129195, or a later release"
sources:
  - url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012"
    publisher: "Mitel (MISA-2026-0012)"
    date: "2026-11-16"
    role: primary
  - url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0006"
    publisher: "Mitel (MISA-2026-0006)"
    date: "2026-07-22"
    role: corroborating
  - url: "https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1547/"
    publisher: "CERT-FR (CERTFR-2026-AVI-1547)"
    date: "2026-11-17"
    role: corroborating
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4608"
    publisher: "BSI CERT-Bund (WID-SEC-2026-4608)"
    date: "2026-11-17"
    role: corroborating
  - url: "https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-4608.json"
    publisher: "BSI CERT-Bund (WID-SEC-W-2026-4608, CSAF record revision 2)"
    date: "2026-11-25"
    role: corroborating
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-130382"
    publisher: "ENISA EUVD (EUVD-2026-130382)"
    date: "2026-11-19"
    role: corroborating
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-130376"
    publisher: "ENISA EUVD (EUVD-2026-130376)"
    date: "2026-11-19"
    role: corroborating
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-130372"
    publisher: "ENISA EUVD (EUVD-2026-130372)"
    date: "2026-11-19"
    role: corroborating
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-130381"
    publisher: "ENISA EUVD (EUVD-2026-130381)"
    date: "2026-11-19"
    role: corroborating
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-130384"
    publisher: "ENISA EUVD (EUVD-2026-130384)"
    date: "2026-11-19"
    role: corroborating
  - url: "https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog"
    publisher: "CISA"
    date: "2026-11-25"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV catalogue"
    date: "2026-11-25"
    role: corroborating
  - url: "https://accenture.github.io/cyber-intelligence/micollab-exploitation/"
    publisher: "Accenture APEX Labs"
    date: "2026-11-24"
    role: corroborating
closed_sources: []
evidence:
  - quote: "could allow an unauthenticated attacker to conduct a blind command injection attack due to insufficient parameter sanitization."
    publisher: "Mitel (MISA-2026-0012)"
    source_url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012"
  - quote: "the risk may be mitigated by restricting external access to the AWV component."
    publisher: "Mitel (MISA-2026-0012)"
    source_url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012"
  - quote: "Exploiting these vulnerabilities together can significantly amplify their impact."
    publisher: "Mitel (MISA-2026-0012)"
    source_url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012"
  - quote: "Mitel MiCollab contains an improper neutralization of special elements used in an OS command (OS command injection) vulnerability in its Audio, Web, and Video Conferencing (AWV) component that could allow an unauthenticated attacker to execute arbitrary system commands."
    publisher: "CISA KEV catalogue"
    source_url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
  - quote: "We have high confidence in this judgment based on evidence from one victim organization showing web shell activity before 23:00 UTC on 15 November 2026."
    publisher: "Accenture APEX Labs"
    source_url: "https://accenture.github.io/cyber-intelligence/micollab-exploitation/"
  - quote: "A clean MiCollab log and an uncompromised perimeter proxy, on their own, do not demonstrate that a MiCollab server was unaffected."
    publisher: "Accenture APEX Labs"
    source_url: "https://accenture.github.io/cyber-intelligence/micollab-exploitation/"
verification: multi-source
sourcing_note: >
  Mitel is the disclosing vendor for its own product; CERT-FR and BSI restate its advisory. CISA's catalogue names no actor, victim, scale or flaw used, and Mitel's revision 2.0 makes no exploitation statement; Accenture APEX Labs is the single source for the exploitation details, from incident-response evidence at one victim and network telemetry at a second, and does not map them to individual flaws. EUVD's exploited-since date mirrors the listing and is not independent. CERT-FR and BSI word the affected range as versions before 10.3.0.18, while Mitel's page says 10.3 (10.3.0.18) and earlier and asks customers to upgrade to that release and apply the patch, so the vendor's wording is followed. BSI's revision 2 says active exploitation was reported and names no source for it. The APEX page carries only "Published November 2026"; its 2026-11-24 date is the page's HTTP Last-Modified header. Mitel's text for the 10.0 flaw is garbled in the original ("requires could allow") and may have lost a stated precondition. The patch article sits behind Mitel's customer portal.
confidence: high
references: ["2026-07-24/mitel-micollab-awv-unauth-command-injection"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "On every MiCollab on 10.3 (10.3.0.18) or earlier whose AWV component was reachable from outside, including through a MiVoice Border Gateway web proxy, take a forensic image first, then apply Mitel's patch KB000129195 (after moving to 10.3.0.18 where needed) and restrict external access to the Audio, Web and Video Conferencing component, then reset the LDAP connector account and any Kerberoastable service accounts and rotate administrator, SIP trunk and file-share credentials, because APEX Labs found exploitation before Mitel's advisory, root within about 30 minutes and directory credentials taken from the LDAP configuration."
updates:
  - at: "2026-11-20T05:11:16Z"
    run_id: 2026-11-20T0356Z-intel
    type: improvement
    summary: >
      MITRE assigned CVE ids to all five flaws on 2026-11-19: CVE-2026-133323 for the CVSS 10.0 command
      injection and CVE-2026-133303 for the 9.0 XML injection, with CVE-2026-133275, CVE-2026-133311 and
      CVE-2026-133324 for the three medium flaws. Mitel's advisory page still lists only its own tracking
      ids.
    fields: [title, summary, cves, sources, body, entities]
  - at: "2026-11-26T05:05:30Z"
    run_id: 2026-11-26T0356Z-intel
    type: update
    summary: >
      CISA added all five MiCollab AWV flaws, among them the unauthenticated CVSS 10.0 command injection, to its Known
      Exploited Vulnerabilities catalogue on 2026-11-25 without naming an actor, victim or technique; Mitel's advisory,
      revised to version 2.0 on 2026-11-24, now lists the CVE ids and makes no exploitation statement. Priority moves to
      high.
    fields: [title, headline, summary, priority, tags, techniques, cves, sources, evidence, verification, sourcing_note, actions, body, updated_at]
  - at: "2026-11-27T04:52:00Z"
    run_id: 2026-11-27T0355Z-intel
    type: update
    summary: >
      Accenture APEX Labs reports that the AWV flaws were exploited before Mitel's advisory and patch: web-shell activity at one
      victim before 23:00 UTC on 2026-11-15, root within about 30 minutes, directory credentials recovered from MiCollab's LDAP
      configuration and used against a domain controller, local logs edited, and a second organisation's server talking to the
      same actor since 2026-11-09. A patched server cannot be assumed clean.
    fields: [title, headline, summary, techniques, sources, evidence, sourcing_note, actions, body, updated_at]
migrated_from: null
---

Mitel's advisory MISA-2026-0012, first issued on 2026-11-16, covers five flaws in the Audio, Web and Video Conferencing (AWV) component of MiCollab 10.3 (10.3.0.18) and earlier; Mitel tracks them by internal ids and, since its revision 2.0 of 2026-11-24, lists the CVE identifiers against them ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)); MITRE published the record for CVE-2026-133323 on 2026-11-19 ([ENISA EUVD, 2026-11-19](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-130382)). MTLVULN-1864 lets an unauthenticated attacker conduct a blind command injection through insufficient parameter sanitization and is scored CVSS 3.1 10.0 with changed scope; MTLVULN-1862 lets an unauthenticated attacker leverage pre-staged malicious content for an XML injection that could run arbitrary commands, scored 9.0 with high attack complexity ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)). Three further flaws are rated Medium: an unauthenticated arbitrary file upload through weak file-type validation (MTLVULN-1861, 5.3), unauthorized access that needs a system-generated random identifier or pre-staged content (MTLVULN-1863, 5.9) and an authentication bypass (MTLVULN-1877, 5.3) ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)). Mitel says exploiting them together can significantly amplify their impact ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)).

Accenture APEX Labs reports exploitation before the advisory: web-shell activity at one victim before 23:00 UTC on 2026-11-15, root within about 30 minutes, and the credentials stored for MiCollab's LDAP connector used against a domain controller 32 minutes after the first request ([Accenture APEX Labs, 2026-11-24](https://accenture.github.io/cyber-intelligence/micollab-exploitation/)). The internet-facing reverse proxy at that victim did not stop it, and APEX does not say which of the five flaws were used ([Accenture APEX Labs, 2026-11-24](https://accenture.github.io/cyber-intelligence/micollab-exploitation/)).

The fix is a patch for release 10.3 (10.3.0.18), delivered through knowledge-base article KB000129195 on Mitel's customer portal, or an upgrade to a later release that Mitel does not name; Mitel's partners can supply it to customers without portal access ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)). Mitel's July advisory named 10.3 (10.3.0.18) as the release that fixed its earlier AWV command injection, so a system moved there in July is inside the new affected range ([Mitel, 2026-07-22](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0006)). CERT-FR lists the advisory on 2026-11-17 ([CERT-FR, 2026-11-17](https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1547/)); BSI's revision of 2026-11-25 rates it critical, says active exploitation was reported and describes a remote anonymous attacker who can manipulate files, run code with the service's rights and bypass security measures ([BSI, 2026-11-25](https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-4608.json)).

**Exposure:** MiCollab 10.3 (10.3.0.18) and earlier whose AWV component external users can reach, including through a reverse proxy or MiVoice Border Gateway web proxy, which APEX says cannot be assumed to protect it ([Accenture APEX Labs, 2026-11-24](https://accenture.github.io/cyber-intelligence/micollab-exploitation/)); Mitel assesses only supported versions and states no branch before 10.3 ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)).

**Detection:** child processes of the AWV service, new files in the component's upload paths and unauthenticated requests to conferencing endpoints that carry shell metacharacters or XML payloads, which follow from the command-injection, upload and XML-injection mechanisms the advisory names ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)). APEX adds POSTs to AWV CGI scripts from unfamiliar sources followed by requests for new files in the web pictures directory, the LDAP connector account authenticating to many domain controllers, and system logs that suddenly shrink ([Accenture APEX Labs, 2026-11-24](https://accenture.github.io/cyber-intelligence/micollab-exploitation/)).

**Defender takeaway:** apply the patch now; where that waits, restrict external access to the AWV component, the mitigation Mitel names ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)). APEX says patching alone will not close an intrusion that started earlier, and the actor filtered local logs: image the server first, compare its logs with proxy and WAF logs, and treat a suspected compromise as a directory compromise by resetting the LDAP connector account and Kerberoastable service accounts ([Accenture APEX Labs, 2026-11-24](https://accenture.github.io/cyber-intelligence/micollab-exploitation/)).

## Improvement — 2026-11-20T05:11:16Z

MITRE published CVE records for all five flaws on 2026-11-19, which Mitel's advisory page did not yet list on that date. MTLVULN-1864 is CVE-2026-133323, the blind command injection (CVSS 3.1 10.0) ([ENISA EUVD, 2026-11-19](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-130382)); MTLVULN-1862 is CVE-2026-133303, the XML injection that leverages pre-staged content (9.0) ([ENISA EUVD, 2026-11-19](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-130376)); MTLVULN-1861 is CVE-2026-133275, the file upload (5.3) ([ENISA EUVD, 2026-11-19](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-130372)); MTLVULN-1863 is CVE-2026-133311, the unauthorized access that needs an identifier or pre-staged content (5.9) ([ENISA EUVD, 2026-11-19](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-130381)); and MTLVULN-1877 is CVE-2026-133324, the authentication bypass (5.3) ([ENISA EUVD, 2026-11-19](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-130384)). Each record's score and affected range match Mitel's table, so the patch and the access restriction above are unchanged.

## Update — 2026-11-26T05:05:30Z

CISA added all five MiCollab AWV flaws to its Known Exploited Vulnerabilities catalogue on 2026-11-25 ([CISA, 2026-11-25](https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog)). The catalogue describes CVE-2026-133323 as an OS command injection in the Audio, Web and Video Conferencing component that could allow an unauthenticated attacker to execute arbitrary system commands, and lists CVE-2026-133303 (XML injection), CVE-2026-133275 (unrestricted file upload), CVE-2026-133311 (weak authentication) and CVE-2026-133324 (not failing securely) with it ([CISA KEV catalogue, 2026-11-25](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). The catalogue names no actor, victim, campaign or technique and does not say which of the five was used.

Mitel's advisory, revised to version 2.0 on 2026-11-24, lists the CVE ids against its tracking ids, still makes no exploitation statement, and adds that the security update will be included in later MiCollab releases without naming one; the affected range, the patch and the access restriction are unchanged ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)). As of that revision, no source read named an exploiting actor, a victim or the number of systems hit.

## Update — 2026-11-27T04:52:00Z

Accenture APEX Labs reports that the MISA-2026-0012 flaws were exploited before Mitel published its advisory and patch. At one victim organisation it places web-shell activity before 23:00 UTC on 2026-11-15, with high confidence, when it was still 15 November in every time zone from UTC−12 to UTC+1 and Mitel dated its advisory 16 November ([Accenture APEX Labs, 2026-11-24](https://accenture.github.io/cyber-intelligence/micollab-exploitation/)). Counted from the first observed request, the actor checked the version, bypassed authentication within a minute, had two uploads accepted at 9 minutes, ran its first web-shell command as the web service account at 12 minutes, reached root between 15 and 30 minutes with system logs reset as a side effect, and at 32 minutes used the credentials recovered from MiCollab's LDAP configuration to authenticate to a domain controller over LDAPS; it then filtered web-shell requests out of the local web, error and admin logs and, 20 to 23 hours in, dumped databases on a backup server and a database server and uploaded the archives over many short HTTPS sessions ([Accenture APEX Labs, 2026-11-24](https://accenture.github.io/cyber-intelligence/micollab-exploitation/)). APEX withholds how root was obtained and does not say which of the five flaws were used.

A second organisation's MiCollab server, on a 10.0-series release exposed to this advisory and to the July one, has held a persistent HTTPS channel to the same actor server since 2026-11-09, and APEX has not determined how it was compromised. APEX assesses that AI-assisted tooling operating on the actor's server drove parts of the intrusion, an inference from sampled traffic to two commercial AI API services that it says cannot show exactly how they were used, and it names no group ([Accenture APEX Labs, 2026-11-24](https://accenture.github.io/cyber-intelligence/micollab-exploitation/)). Mitel's advisory is unchanged at revision 2.0 and makes no exploitation statement; BSI's revision of 2026-11-25 rates it critical and says active exploitation was reported ([BSI, 2026-11-25](https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-4608.json)).
