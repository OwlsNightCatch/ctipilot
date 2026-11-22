---
schema: 1
kind: incident
title: "BundID: automated mass login attempts against Germany's federal citizen accounts lock accounts; the BSI confirms the attack, password sign-in was switched off on 16 November and returned that afternoon behind an e-mail security code, and no compromise is evidenced"
headline: "BundID: mass automated logins lock citizen accounts; BSI confirms; password sign-in now needs an e-mail code"
summary: >
  On 2026-11-16 Germany's BSI confirmed automated, mass login attempts against BundID, the federal citizen account for online administrative services: failed attempts locked accounts and triggered password-reset mails, and the federal government switched off username-and-password sign-in that morning, then restored it the same afternoon with a mandatory security code by e-mail at every password sign-in, while eID and Elster sign-in stayed open. The BSI has no indication that any account was compromised; Handelsblatt, citing government circles, calls it credential stuffing.
discovered_at: "2026-11-17T04:43:00Z"
updated_at: null
event_date: "2026-11-16"
run_id: 2026-11-17T0355Z-intel
priority: routine
immediate_action: null
tags: [identity]
regions: [dach]
sectors: [public-sector]
entities: ["incident:bundid-credential-stuffing-account-lockouts-2026-11"]
techniques: [T1110.004]
affected_products: ["BundID"]
cves: []
sources:
  - url: "https://www.heise.de/news/BundID-Massenhafte-Angriffe-fuehren-zu-Kontosperrungen-11526376.html"
    publisher: "heise online"
    date: "2026-11-16"
    role: primary
  - url: "https://www.handelsblatt.com/politik/deutschland/bundid-hackerangriff-auf-buergerkonten-mit-massenhaften-log-in-versuchen/100270238.html"
    publisher: "Handelsblatt"
    date: "2026-11-16"
    role: corroborating
  - url: "https://web.de/magazine/digital/bundid-konto-gesperrt-betroffene-42951652"
    publisher: "WEB.DE News"
    date: "2026-11-16"
    role: corroborating
  - url: "https://www.ad-hoc-news.de/wissenschaft/bundid-nach-angriffswelle-passwort-login-jetzt-nur-noch-mit-e-mail-code/70522344"
    publisher: "ad-hoc-news.de (aggregator)"
    date: "2026-11-16"
    role: corroborating
  - url: "https://www.spiegel.de/netzwelt/web/bundid-hacker-attackieren-konten-zweifaktor-authentifizierung-aktiviert-a-305b6f61-70ac-4a83-8b2c-62c4d98d13c4"
    publisher: "DER SPIEGEL"
    date: "2026-11-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Automated, mass login attempts have occurred against BundID accounts. (translated from German)"
    original: "Dabei ist es zu automatisierten, massenhaften Login-Versuchen in BundID-Konten gekommen"
    publisher: "heise online (quoting the BSI)"
    source_url: "https://www.heise.de/news/BundID-Massenhafte-Angriffe-fuehren-zu-Kontosperrungen-11526376.html"
  - quote: "The BSI currently has no indications of a compromise of BundID accounts. (translated from German)"
    original: "Auf eine Kompromittierung von BundID-Konten liegen dem BSI derzeit keine Hinweise vor"
    publisher: "heise online (quoting the BSI)"
    source_url: "https://www.heise.de/news/BundID-Massenhafte-Angriffe-fuehren-zu-Kontosperrungen-11526376.html"
  - quote: "According to current findings this is so-called credential stuffing, the Handelsblatt learned from government circles. (translated from German)"
    original: "Nach aktuellen Erkenntnissen handelt es sich um sogenanntes Credential Stuffing, erfuhr das Handelsblatt aus Regierungskreisen."
    publisher: "Handelsblatt"
    source_url: "https://www.handelsblatt.com/politik/deutschland/bundid-hackerangriff-auf-buergerkonten-mit-massenhaften-log-in-versuchen/100270238.html"
verification: multi-source
sourcing_note: >
  heise and Handelsblatt each quote a BSI spokesperson, so they trace to one assessor. The credential-stuffing label is Handelsblatt's, from unnamed government sources, not a BSI statement; the operator's own site notice is known through Spiegel's quotation of it, and the number of locked accounts is not disclosed.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-11-22T14:53:08Z"
    run_id: 2026-11-22T1407Z-audit
    type: improvement
    summary: >
      Spiegel quotes the BundID site notice of the afternoon of 2026-11-16: password sign-in returned the
      same day, with a security code sent by e-mail at every sign-in by username and password, while eID
      and Elster sign-in stayed open.
    fields: [body, headline, sources, summary, title, sourcing_note]
migrated_from: null
---

Germany's BSI confirmed to heise security and Handelsblatt on 2026-11-16 an IT security incident involving BundID accounts: automated, mass login attempts whose failures locked accounts, triggered automated mails and prompted account holders to reset their passwords ([heise, 2026-11-16](https://www.heise.de/news/BundID-Massenhafte-Angriffe-fuehren-zu-Kontosperrungen-11526376.html)). The federal government switched off username-and-password sign-in on Monday morning for security reasons ([Handelsblatt, 2026-11-16](https://www.handelsblatt.com/politik/deutschland/bundid-hackerangriff-auf-buergerkonten-mit-massenhaften-log-in-versuchen/100270238.html)), while sign-in with the online ID card (eID) and the Elster certificate stayed possible ([WEB.DE, 2026-11-16](https://web.de/magazine/digital/bundid-konto-gesperrt-betroffene-42951652)). The BSI says countermeasures it does not name repelled the attack and that it has no indication of a compromise of any account, and heise reports that locked accounts are apparently not being unlocked in bulk, so account holders must pass the password-reset flow or use another sign-in method ([heise, 2026-11-16](https://www.heise.de/news/BundID-Massenhafte-Angriffe-fuehren-zu-Kontosperrungen-11526376.html)). Handelsblatt, citing government circles, describes the attack as credential stuffing, the automated replay of credentials from earlier leaks at other services ([Handelsblatt, 2026-11-16](https://www.handelsblatt.com/politik/deutschland/bundid-hackerangriff-auf-buergerkonten-mit-massenhaften-log-in-versuchen/100270238.html)). That afternoon the BundID site notice said two-factor authentication had been switched on for all accounts, with a security code by e-mail at every sign-in by username and password ([Spiegel, 2026-11-16](https://www.spiegel.de/netzwelt/web/bundid-hacker-attackieren-konten-zweifaktor-authentifizierung-aktiviert-a-305b6f61-70ac-4a83-8b2c-62c4d98d13c4)). An aggregator attributes the credential-stuffing label to the BSI, which neither heise nor Handelsblatt does ([ad-hoc-news.de, 2026-11-16](https://www.ad-hoc-news.de/wissenschaft/bundid-nach-angriffswelle-passwort-login-jetzt-nur-noch-mit-e-mail-code/70522344)).

**Exposure:** citizen-facing or employee-facing login portals that accept a password and lock an account after repeated failures.

**Detection:** authentication logs showing a surge of failed password sign-ins spread over many usernames and sources, followed by lockout notices, password-reset mail volume and helpdesk contacts; a lockout storm is itself the alert.

**Defender takeaway:** the operator's containment was to switch off the password-only path while eID and other sign-in means stayed open, as heise and Handelsblatt report it, and to bring it back the same day only with an e-mail security code ([Spiegel, 2026-11-16](https://www.spiegel.de/netzwelt/web/bundid-hacker-attackieren-konten-zweifaktor-authentifizierung-aktiviert-a-305b6f61-70ac-4a83-8b2c-62c4d98d13c4)); a lockout-after-failures control turns credential stuffing into mass lockouts and reset mail even when no account is taken over, so settle that containment lever for your own portals before a run starts.

## Improvement — 2026-11-22T14:53:08Z

The same-day return of password sign-in now rests on the operator's own notice: on the afternoon of 2026-11-16 the BundID site said two-factor authentication had been switched on for all accounts, so every sign-in with username and password now needs a security code sent by e-mail, while sign-in with the online ID card and the Elster certificate stayed available ([Spiegel, 2026-11-16](https://www.spiegel.de/netzwelt/web/bundid-hacker-attackieren-konten-zweifaktor-authentifizierung-aktiviert-a-305b6f61-70ac-4a83-8b2c-62c4d98d13c4)).
