---
schema: 1
kind: policy
title: "BACS publishes five security classes for authentication methods: static secrets should in principle no longer be used, and only session-bound methods resist real-time phishing"
headline: "BACS grades logins in five classes: static secrets should in principle go; session binding resists phishing"
summary: >
  Switzerland's Federal Office for Cybersecurity (BACS) published on 2026-10-19 a technology assessment that sorts
  authentication methods, tokens and services into the classes tief, mittel and hoch, with a star on mittel and hoch for
  resistance to real-time phishing. It says methods in class tief, those built on a secret that is the same at every login,
  should in principle no longer be used. The classification is non-binding and gives no basis for testing or certification;
  it is a rough guideline from the federal authority for writing authentication requirements.
discovered_at: "2026-10-20T03:36:40Z"
updated_at: null
event_date: "2026-10-19"
run_id: 2026-10-20T0256Z-intel
priority: routine
immediate_action: null
tags: [policy, identity]
regions: [switzerland]
sectors: [public-sector]
entities: []
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.bacs.admin.ch/de/26-tb-authentifizierung-de"
    publisher: "Bundesamt für Cybersicherheit (BACS)"
    date: "2026-10-19"
    role: primary
  - url: "https://www.bacs.admin.ch/dam/de/sd-web/vSjpggXgBK2W/Technologiebetrachtung_Authentifikationsverfahren_DE.pdf"
    publisher: "Bundesamt für Cybersicherheit (BACS), Technologiebetrachtung (PDF)"
    date: "2026-10-19"
    role: primary
closed_sources: []
evidence:
  - quote: "The classification offers no basis for formal testing or certification in its present form. (translated from German)"
    original: "In der vorliegenden Form bietet die Klassifikation keine Grundlage zur formalen Prüfung oder Zertifizierung."
    publisher: "Bundesamt für Cybersicherheit (BACS)"
    source_url: "https://www.bacs.admin.ch/de/26-tb-authentifizierung-de"
  - quote: "extended with regard to resistance to real-time phishing attacks (translated from German)"
    original: "im Hinblick auf Resistenz vor «Real-time Phishing»-Angriffen erweitert worden"
    publisher: "Bundesamt für Cybersicherheit (BACS)"
    source_url: "https://www.bacs.admin.ch/de/26-tb-authentifizierung-de"
verification: single-source-national-cert
sourcing_note: >
  BACS is the primary and only publisher of its own technology assessment; the PDF cover is dated September 2026 and the
  page announcing it is dated 2026-10-19. The class definitions are paraphrased from the German PDF.
confidence: high
references: []
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

BACS published on 2026-10-19 the technology assessment "Sicherheitsklassen für Authentifikationsverfahren, -mittel und -dienste", which sorts authentication methods, tokens and services into the three classes tief (low), mittel (medium) and hoch (high), with mittel and hoch each split further, five classes in all ([BACS, 2026-10-19](https://www.bacs.admin.ch/de/26-tb-authentifizierung-de)). The scheme follows the NIST authentication assurance levels 1 to 3 with slight adjustments and extends them for resistance to real-time phishing; BACS says the classification gives no basis for formal testing or certification and can serve organisations as a basis for security requirements and recommendations ([BACS, 2026-10-19](https://www.bacs.admin.ch/de/26-tb-authentifizierung-de)). In the assessment, class tief covers any method whose authentication information is static and identical at every login, such as a password or a cryptographic key, and the class does not rise when the secret travels over TLS; BACS concludes that methods in this class should in principle no longer be used ([BACS, 2026-10-19](https://www.bacs.admin.ch/dam/de/sd-web/vSjpggXgBK2W/Technologiebetrachtung_Authentifikationsverfahren_DE.pdf)). Class mittel needs authentication information generated anew for each login plus at least one further security feature, and the starred variant additionally needs session binding, which ties the session cryptographically to the authentication information or to the device, network or application; the assessment names TLS channel binding, Device Bound Session Credentials and OAuth DPoP as examples, against session hijacking, real-time phishing and adversary-in-the-middle attacks ([BACS, 2026-10-19](https://www.bacs.admin.ch/dam/de/sd-web/vSjpggXgBK2W/Technologiebetrachtung_Authentifikationsverfahren_DE.pdf)). BACS says the difference between mittel and hoch lies mainly in the use of additional hardware to store the cryptographic keys ([BACS, 2026-10-19](https://www.bacs.admin.ch/dam/de/sd-web/vSjpggXgBK2W/Technologiebetrachtung_Authentifikationsverfahren_DE.pdf)). Its annex of examples places a password, a static API key and a secret held in a cookie such as a session ID in tief; a password with an SMS code, a software authenticator app, Kerberos tickets, bearer tokens (SAML, OIDC, OAuth, JWT) and synced passkeys in mittel, the passkeys starred; and hardware OTP tokens, hardware certificates in TLS and FIDO2 without synchronisation or key export in hoch, with a footnote that SMS verification should be used only where no better alternative exists ([BACS, 2026-10-19](https://www.bacs.admin.ch/dam/de/sd-web/vSjpggXgBK2W/Technologiebetrachtung_Authentifikationsverfahren_DE.pdf)).

**Defender takeaway:** the classification binds no one and sets no deadline; it is a rough guideline (BACS's own term) that cantonal and communal bodies can use when writing authentication requirements. A login that rests on a static secret is class tief, which BACS says should in principle no longer be used, and a login resists real-time phishing and session hijacking only where it is session-bound (the starred classes) ([BACS, 2026-10-19](https://www.bacs.admin.ch/dam/de/sd-web/vSjpggXgBK2W/Technologiebetrachtung_Authentifikationsverfahren_DE.pdf)).
