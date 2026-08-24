---
schema: 1
kind: vulnerability
horizon: operational
title: "SPIP shipped two unconditional pre-authentication RCE fixes three days apart, and the second one closes a flaw in the release that fixed the first (CVE-2026-77647 and CVE-2026-77806)"
headline: "Patching SPIP to 4.4.20 was not enough — 4.4.21 fixes a second unconditional pre-auth RCE in 4.4.20 itself, and neither flaw is caught by SPIP's security screen"
summary: >
  SPIP released 4.4.20 on 2026-08-17 for an unauthenticated remote code execution flaw — later assigned
  CVE-2026-77647 — telling operators in the same bulletin that exploitation attempts had already been
  observed in the wild, then released 4.4.21 on
  2026-08-20 for a second unconditional pre-authentication RCE that affects 4.4.20 — the release that was
  supposed to be the fix. CERT-FR carries one advisory per flaw and records that the vendor reports active
  exploitation; both advisories were updated on 2026-08-24 to add their identifiers, CVE-2026-77647 for the
  first and CVE-2026-77806 for the second. Both bulletins state
  the flaw is not covered by SPIP's built-in security screen, and neither describes the mechanism, so a
  stopgap filter is not an option and there is no payload signature to hunt for.
  SPIP is widely deployed across French-speaking public administration, so any estate that patched to
  4.4.20 and stopped is still exposed and must go to 4.4.21.
discovered_at: "2026-08-24T09:55:00Z"
event_date: "2026-08-20"
run_id: 2026-08-24T0902Z-audit
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, actively-exploited, patch-available]
regions: [europe, global]
sectors: [public-sector, education]
entities: []
techniques: [T1190, T1059]
affected_products: ["SPIP"]
cves:
  - id: CVE-2026-77647
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "SPIP before 4.4.20"
    fixed: "4.4.20 — but see the body and CVE-2026-77806: a second unconditional pre-auth RCE affects 4.4.20 itself and is fixed only in 4.4.21"
  - id: CVE-2026-77806
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "SPIP before 4.4.21, including 4.4.20 — the release published three days earlier as the fix for CVE-2026-77647"
    fixed: "4.4.21"
sources:
  - url: "https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-21.html?lang=fr"
    publisher: "SPIP (éditeur)"
    date: "2026-08-20"
    role: primary
  - url: "https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-20.html?lang=fr"
    publisher: "SPIP (éditeur)"
    date: "2026-08-17"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1063/"
    publisher: "CERT-FR / ANSSI"
    date: "2026-08-24"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1033/"
    publisher: "CERT-FR / ANSSI"
    date: "2026-08-24"
    role: primary
evidence:
  - quote: "Cette version corrige une vulnérabilité universelle (sans conditions) pré-authentification RCE qui touche la version 4.4.20 de SPIP."
    publisher: "SPIP (éditeur)"
    url: "https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-21.html?lang=fr"
  - quote: "Cette faille n’est pas prise en charge par l’écran de sécurité."
    publisher: "SPIP (éditeur)"
    url: "https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-20.html?lang=fr"
  - quote: "Il est impératif de mettre très rapidement votre site à jour, des tentatives d’exploitation de la faille ont déjà été constatées dans la nature."
    publisher: "SPIP (éditeur)"
    url: "https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-20.html?lang=fr"
  - quote: "L'éditeur indique que cette vulnérabilité est activement exploitée."
    publisher: "CERT-FR / ANSSI"
    url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1063/"
verification: single-source
sourcing_note: >
  All four sources — the vendor's two release bulletins and CERT-FR's two advisories — were fetched in this
  run. **Identifier provenance follows the shape CERT-FR itself uses: one advisory per flaw, each updated on
  2026-08-24 to add its identifier.** CERTFR-2026-AVI-1033 carries CVE-2026-77647 for the 4.4.20 flaw;
  CERTFR-2026-AVI-1063 carries CVE-2026-77806 for the 4.4.21 flaw. Neither vendor bulletin names any
  identifier at all, so the CERT advisories are the citable authority for the identifier-to-flaw binding.
  Both 9.8 base scores are the CVE records' own CNA-assigned values, carried in frontmatter for the machine
  surface and not restated in the body, because this pipeline does not cite per-CVE aggregator pages as
  sources. On corroboration: both flaws were reported anonymously via ANSSI per the bulletins, and CERT-FR
  attributes the exploitation statement explicitly to the vendor ("L'éditeur indique…") — so CERT-FR is a
  second publisher of the vendor's assessment rather than a second assessor, which is why credibility is 2
  rather than 1. **Neither vendor bulletin nor either advisory describes the defect's mechanism**, so this
  entry does not either: an earlier draft attributed a var_export()/PHP-tag root cause to the 4.4.20 bulletin,
  which contains no such text — that description belongs to the CVE record, which is not citable here, and it
  was removed rather than mis-sourced.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
classification:
  reliability: A
  credibility: 2
actions:
  - "Inventory every SPIP installation and upgrade to 4.4.21 — not 4.4.20. An estate that applied the 2026-08-17 release for CVE-2026-77647 is still exposed to a second unconditional pre-authentication RCE that the 2026-08-20 release fixes."
  - "For any SPIP instance that was internet-reachable and unpatched between 2026-08-17 and the upgrade, treat it as a compromise-assessment candidate rather than a patching task: both flaws yield pre-authentication code execution as the web server user, and the vendor reports exploitation was already under way."
---

SPIP published two critical security releases three days apart, and the relationship between them is the finding. The 2026-08-17 release, 4.4.20, fixes a flaw reported anonymously via ANSSI and described by the vendor as an unconditional pre-authentication remote code execution affecting **all** SPIP versions, with the same bulletin telling operators that "des tentatives d’exploitation de la faille ont déjà été constatées dans la nature" ([SPIP, 2026-08-17](https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-20.html?lang=fr)). CERT-FR published a separate advisory for the 4.4.20 flaw and updated it on 2026-08-24 to add the identifier CVE-2026-77647 ([CERT-FR, 2026-08-24](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1033/)). Neither bulletin describes the defect's mechanism, and this entry does not speculate about it — what the vendor publishes is the severity class, the reach and the fact that its own security screen does not cover it. The 2026-08-20 release, 4.4.21, then states plainly that it "corrige une vulnérabilité universelle (sans conditions) pré-authentification RCE qui touche la version 4.4.20 de SPIP" — a second unconditional pre-authentication RCE in the release that had just shipped as the fix ([SPIP, 2026-08-20](https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-21.html?lang=fr)). CERT-FR issued its advisory for the second flaw the following day, records that the vendor reports it actively exploited, and updated that advisory on 2026-08-24 to add the identifier now assigned to it, CVE-2026-77806 ([CERT-FR, 2026-08-24](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1063/)).

The word "universelle (sans conditions)" is doing real work: unlike flaws that need a specific plugin, template or configuration, this one has no stated precondition beyond running the affected version, and the 4.4.20 bulletin puts its reach at every SPIP version ([SPIP, 2026-08-17](https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-20.html?lang=fr)). Both bulletins add that the flaw "n’est pas prise en charge par l’écran de sécurité" — SPIP’s security screen, the centralised request-filtering layer many operators rely on as a stopgap between disclosure and patching, does not stop it ([SPIP, 2026-08-17](https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-20.html?lang=fr)). The vendor does not say why, and no cited source describes the defect, so the honest reading stops there: the screen inspects requests, and whatever this bug is, it is not something the screen recognises in one. That a second flaw of the same severity class landed in the release that fixed the first is consistent with an incomplete first fix, but neither bulletin says so and this entry does not claim it.

Detection has to work without a payload signature, because no cited source publishes the mechanism — and that constraint is itself the useful finding, since it is also why the security screen cannot help. Telemetry-class first: in process-execution telemetry with parent lineage, the pivot that turns code execution into an intrusion is the web server account (`www-data`, `apache`) spawning a shell or interpreter beneath the SPIP process tree outside a deployment or cron context. In file-integrity telemetry, new or modified PHP under SPIP's cache and template directories is the usual landing place for persistence in this CMS. In web access logs, the tractable question is not which parameter carried the payload but which SPIP instances were reachable and unpatched during the exposure window, and what those instances served afterwards. Because exploitation is pre-authentication, authentication logs will show nothing: an absence of suspicious logins is not evidence of absence.

**Triage:** SPIP's own template and cache machinery legitimately writes PHP into cache directories, so a new PHP file there is not by itself the signal. The discriminators are a cache-directory write that is not attributable to a content edit or a template recompilation, and any interpreter or shell process whose parent is the web server rather than a scheduled task or the operator's own deployment tooling. Legitimate SPIP request traffic also carries angle brackets in editorial content fields; what separates it is the combination with an unauthenticated session and a subsequent process-lineage event.

**Defender takeaway:** the operational trap is a patch record that reads as complete. A vulnerability-management process tracking CVE-2026-77647 marks itself done at 4.4.20, and for the week between the 4.4.20 release and 2026-08-24, when CERT-FR added CVE-2026-77806 to its advisory, the second flaw had no identifier on the advisory surface a European defender is most likely to be reading. Any estate triaged in that window is the one to re-check: it will show a closed CVE and an exposed server. Go to 4.4.21 by version number rather than by CVE closure, and note the wider lesson for the constituency: SPIP is widely deployed across French-speaking public administration, including communal and cantonal sites, and two unconditional pre-auth RCEs with reported exploitation inside four days is the profile of a flaw wave that reaches small operators with no patch window and no security screen that helps.
