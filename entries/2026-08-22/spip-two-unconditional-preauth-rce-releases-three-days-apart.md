---
schema: 1
kind: vulnerability
horizon: operational
title: >
  SPIP shipped two emergency releases in three days, each fixing an unconditional
  pre-authentication RCE the vendor says is already being exploited — and only the first one has a
  CVE
headline: >
  4.4.20 fixed a flaw in every version; 4.4.21 fixed a second one in 4.4.20 itself, with no
  identifier to track it by
summary: >
  SPIP, the content-management system behind a large share of French government, municipal and
  institutional websites, published critical security releases on 17 and 20 August 2026. Each
  fixes what its maintainers describe in identical words as an unconditional, no-prerequisites
  pre-authentication remote code execution flaw, each was reported anonymously through France's
  national cybersecurity agency, each is explicitly not covered by SPIP's own built-in
  request-filtering layer, and for each the vendor states exploitation attempts have already been
  observed in the wild. The first is CVE-2026-77647, affecting all versions before 4.4.20. The
  second, scoped by the vendor to 4.4.20 itself, has no CVE identifier at all — so a
  vulnerability-management process driven by CVE feeds cannot see the newer of the two.
discovered_at: "2026-08-22T05:07:00Z"
updated_at: "2026-08-24T09:55:00Z"
event_date: 2026-08-20
run_id: 2026-08-22T0410Z-intel
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - rce
  - pre-auth
  - actively-exploited
  - patch-available
regions:
  - europe
  - switzerland
  - global
sectors:
  - public-sector
  - education
entities: []
techniques:
  - T1190
affected_products:
  - SPIP
cves:
  - id: CVE-2026-77647
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - patch-available
    affected: all versions before 4.4.20
    fixed: >
      4.4.20 (released 17 August 2026) — note that 4.4.20 is itself affected by the separate,
      unnumbered flaw fixed in 4.4.21
  - id: CVE-2026-77806
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - patch-available
    affected: >
      SPIP before 4.4.21, including 4.4.20 — the release published three days earlier as the fix for
      CVE-2026-77647
    fixed: 4.4.21
sources:
  - url: "https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-21.html"
    publisher: SPIP
    date: 2026-08-20
    role: primary
  - url: "https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-20.html"
    publisher: SPIP
    date: 2026-08-17
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1063/"
    publisher: CERT-FR / ANSSI
    date: 2026-08-21
    role: primary
  - url: "https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-63757"
    publisher: ENISA EU Vulnerability Database
    date: 2026-08-20
    role: corroborating
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1033/"
    publisher: CERT-FR / ANSSI
    date: 2026-08-24
    role: primary
closed_sources: []
evidence:
  - quote: "Cette version corrige une vulnérabilité universelle (sans conditions) pré-authentification RCE qui touche toutes les versions de SPIP."
    publisher: SPIP (4.4.20 release note)
  - quote: "Cette version corrige une vulnérabilité universelle (sans conditions) pré-authentification RCE qui touche la version 4.4.20 de SPIP."
    publisher: SPIP (4.4.21 release note)
  - quote: "Systèmes affectés SPIP versions antérieures à 4.4.21"
    publisher: CERT-FR / ANSSI
  - quote: "L'éditeur indique que cette vulnérabilité est activement exploitée."
    publisher: CERT-FR / ANSSI
  - quote: "SPIP before 4.4.20 allows unauthenticated remote attackers to execute arbitrary code, as exploited in the wild in August 2026."
    publisher: ENISA EU Vulnerability Database
verification: multi-source
sourcing_note: >
  Two vendor release notes and one national-CERT advisory, with the CVE record corroborating the
  older of the two flaws — the exploitation claim for the newer flaw is the vendor's, and CERT-FR
  attributes it to the vendor rather than asserting it independently, which is why the credibility
  rating is 2. The two releases are carried in one entry deliberately: they are three days apart,
  from one publisher, on one product, and the finding is the pair rather than either flaw alone.
  Two framings of the affected range are preserved side by side rather than reconciled, because
  both are true of different things: CERT-FR states all versions before 4.4.21 are affected, which
  holds in aggregate across both flaws, while the 4.4.21 release note scopes its own flaw
  specifically to 4.4.20 — the release that had just fixed the first one. No root cause is stated
  here for the 4.4.21 flaw because none has been published: the vendor has not said whether it is
  a bypass of the 4.4.20 fix or an unrelated flaw of the same shape, and inventing an answer to
  that would be worse than leaving it open. The root cause and score of CVE-2026-77647 are taken
  from the EU vulnerability database record, cited in place of the per-CVE data sheet this
  pipeline does not cite; that record carries the vendor's own release note and a distribution
  security advisory among its references.
confidence: high
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every SPIP site to 4.4.21 — not to 4.4.20, which the vendor states is itself affected by the second flaw — and do it as an out-of-band change: the vendor states exploitation attempts on both flaws have already been observed. Do not rely on SPIP's built-in security screen as an interim control; the vendor states in both release notes that it does not cover these flaws."
  - "Add SPIP to the manual watch list of any vulnerability-management process that triggers only on CVE identifiers: the 4.4.21 flaw has none, so a CVE-driven pipeline will report the estate clean once CVE-2026-77647 is closed while the newer flaw is still open."
  - "Re-run the vulnerability-management match on SPIP estates now that CVE-2026-77806 exists: any instance triaged between 2026-08-20 and 2026-08-24 off a CVE feed shows CVE-2026-77647 closed at 4.4.20 while the then-unnumbered second flaw left it exposed — confirm those instances are on 4.4.21, not 4.4.20."
updates:
  - at: "2026-08-24T09:55:00Z"
    run_id: 2026-08-24T0902Z-audit
    type: update
    summary: >
      The second of SPIP's two unconditional pre-authentication remote-code-execution flaws — fixed in
      4.4.21 on 2026-08-20 and covered by this pipeline on 2026-08-22 with the explicit warning that a
      CVE-keyed vulnerability-management process could not see it — now has an identifier: CERT-FR
      updated its advisory on 2026-08-24 to add CVE-2026-77806. CERT-FR carries one advisory per flaw
      and updated both the same day, adding CVE-2026-77647 for the 4.4.20 flaw to its companion
      advisory. Estates triaged between 2026-08-20 and 2026-08-24 off a CVE feed are the ones to
      re-check: they will show CVE-2026-77647 closed at 4.4.20 while the unnumbered second flaw left
      the server exposed.
    fields:
      - actions
      - cves
      - regions
      - sectors
      - sources
      - body
    merged_from: 2026-08-24/spip-second-flaw-cve-2026-77806-assigned-certfr-advisories
migrated_from: null
---

SPIP's maintainers published a critical security release on Monday 17 August 2026 and another on Thursday 20 August. The release notes describe their respective flaws in near-identical language, and the wording is unusually unhedged for a vendor bulletin: 4.4.20 fixes an unconditional, no-prerequisites pre-authentication remote code execution vulnerability affecting *all* versions of SPIP ([SPIP, 2026-08-17](https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-20.html)), and 4.4.21 fixes an unconditional, no-prerequisites pre-authentication remote code execution vulnerability affecting *version 4.4.20* — the release that had just shipped three days earlier ([SPIP, 2026-08-20](https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-21.html)). Both notes then carry the same follow-on sentence word for word: the flaw is not handled by the security screen, it is imperative to update the site very quickly, and exploitation attempts have already been observed in the wild. The security screen — SPIP's own request-filtering layer, which many administrators treat as a standing compensating control against exactly this bug class — is therefore ruled out by the vendor as a mitigation for both. Both were reported anonymously through France's national cybersecurity agency, and the earlier one credits a researcher by handle for help with the analysis and the fix ([SPIP, 2026-08-17](https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-20.html)).

Only the first of the two has an identifier. CVE-2026-77647 is the 4.4.20 fix: the EU vulnerability database record cites that release note directly, bounds the affected range as everything below 4.4.20, scores it CVSS 3.1 9.8 with an EPSS of 0.82, and states in its own description that the flaw is exploited in the wild in August 2026 ([ENISA EU Vulnerability Database, 2026-08-20](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-63757)). Its published root cause is incorrect identification of PHP open tags combined with a value-exporting function's mishandling of certain cases such as the presence of a `<` character ([ENISA EU Vulnerability Database, 2026-08-20](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-63757)). The 4.4.21 flaw has no CVE, no CWE and no published root cause; CERT-FR relayed it as an advisory the following day, recording remote code execution as the risk, giving the affected range as all versions before 4.4.21, and attributing the active-exploitation statement to the vendor rather than asserting it itself ([CERT-FR, 2026-08-21](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1063/)). Whether it is a bypass of the fix that shipped three days earlier or an independent flaw of the same shape is not something any source says, and this entry does not guess.

**Defender takeaway:** the operational trap here is the version number, not the technique. An administration that patched promptly on 17 August, closed the CVE its scanner flagged, and moved on is running 4.4.20 — the one release the vendor names as affected by the second flaw. There is no identifier for a scanner to key on, so the estate will report clean. For anyone running SPIP the correct floor is 4.4.21 and the correct posture is out-of-band, because the vendor states attempts are already being seen against both. Beyond that, no honest detection guidance is available for the newer flaw: with no published root cause there is no vulnerable component, endpoint or parameter to hunt on, and inventing one would send hunters looking in the wrong place. What is available is generic to the platform and worth doing anyway on any site that was internet-facing and below 4.4.21 in the past week: reconcile files under the SPIP document root — the compiled-template and cache directories in particular — against what the deployment should contain, and look in web-server access logs for requests that precede an unexpected PHP process spawn or a new file appearing under the document root. That is a compromise assessment rather than a detection rule, which is the right shape of work when the vendor has confirmed exploitation and withheld the mechanism.

**Triage:** a public CMS receives constant automated probing, so request volume and 404 noise separate nothing. The discriminator is what happens *after* a request rather than the request itself — a web-server worker process spawning a shell or interpreter child, or a file appearing under the document root whose modification time matches no deployment, upgrade or editorial action. On a platform this widely deployed across French-language public administration, and with the earlier flaw's CVE record already recording in-the-wild exploitation, the base rate for that sequence being benign is low.

## Update — 2026-08-24T09:55:00Z

The original entry's closing warning was that the second flaw "has no CVE identifier at all — so a vulnerability-management process driven by CVE feeds cannot see the newer of the two." That gap closed on 2026-08-24, and closing it is itself the operational delta.

CERT-FR updated its advisory for the 4.4.21 flaw on 2026-08-24 to add the identifier now assigned to it, CVE-2026-77806, and updated its companion advisory for the 4.4.20 flaw the same day to add CVE-2026-77647 ([CERT-FR, 2026-08-24](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1063/); [CERT-FR, 2026-08-24](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1033/)). CERT-FR carries one advisory per flaw — the split the original entry described in prose is now the split of the identifier records too, and the exploitation statement stands as before, attributed by CERT-FR to the vendor.

**Defender takeaway:** the window the original entry warned about is now bounded and checkable. Between 2026-08-20 and 2026-08-24 a CVE-driven process could close CVE-2026-77647 at 4.4.20 and see nothing further; from 2026-08-24 the second flaw is matchable as CVE-2026-77806 with `fixed: 4.4.21`. Re-run the match once the feed picks the identifier up, and treat any SPIP instance still on 4.4.20 as unpatched against an actively exploited flaw rather than patched against the one its ticket named.
