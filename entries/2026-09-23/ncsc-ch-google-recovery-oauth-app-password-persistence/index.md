---
schema: 1
kind: threat
title: "NCSC Switzerland: Google recovery-address abuse plus a Sites-hosted phishing page plants an app-password backdoor that survives a password reset"
headline: "A genuine Google security alert becomes the lure in a fraud chain that outlives a password change"
summary: >
  Switzerland's national cybersecurity authority documents a fraud chain
  where attackers register a victim's address as their own Google account's
  recovery address, then use a genuine Google security notification as a
  vishing hook to steer the victim to a Google Sites-hosted phishing page.
  Once inside the real account, attackers provision an app password — a
  legacy credential that bypasses MFA and survives a subsequent password
  change.
discovered_at: "2026-09-23T04:45:00Z"
updated_at: null
event_date: "2026-09-22"
run_id: 2026-09-23T0405Z-intel
priority: routine
immediate_action: null
tags: [phishing, identity]
regions: [switzerland]
sectors: [public-sector]
entities: ["product:google-account"]
techniques: [T1566.004, T1684.001, T1098.001]
affected_products: ["Google Account"]
cves: []
sources:
  - url: "https://www.bacs.admin.ch/de/26w38-de"
    publisher: "Bundesamt für Cybersicherheit (BACS) / NCSC Switzerland"
    date: "2026-09-22"
    role: primary
closed_sources: []
evidence:
  - quote: "They then generated an app password in their own account and labelled it in the free-text field with: \"Kevin W. Case-ID: 834333 To view your case…\"."
    original: "Anschliessend generierten sie in ihrem eigenen Konto ein App-Passwort und benannten dieses im Textfeld mit: «Kevin W. Case-ID: 834333 To view your case…»."
    publisher: "Bundesamt für Cybersicherheit (BACS) / NCSC Switzerland"
    source_url: "https://www.bacs.admin.ch/de/26w38-de"
  - quote: "Google's automated system then sent an official, technically flawless security warning to the victim. Because the naming text was automatically carried into the email, it looked to the recipient as if Google were running an urgent support case with a case handler and case number."
    original: "Googles automatisches System verschickte daraufhin eine offizielle, technisch völlig einwandfreie Sicherheitswarnung an das Opfer. Da der Benennungstext automatisch in die E-Mail übernommen wurde, sah es für die empfangende Person so aus, als führe Google einen dringenden Support-Fall mit Bearbeiter und Fallnummer."
    publisher: "Bundesamt für Cybersicherheit (BACS) / NCSC Switzerland"
    source_url: "https://www.bacs.admin.ch/de/26w38-de"
  - quote: "As a result, the perpetrators retained access to the account even after a password change. In the reported case, emails and contacts continued to sync unnoticed to a device abroad for an extended period after the attack."
    original: "Dadurch behielten die Täter selbst nach einer Passwortänderung weiterhin Zugriff auf das Konto. Im gemeldeten Fall wurden noch längere Zeit nach dem Angriff unbemerkt E-Mails und Kontakte auf ein Gerät im Ausland synchronisiert."
    publisher: "Bundesamt für Cybersicherheit (BACS) / NCSC Switzerland"
    source_url: "https://www.bacs.admin.ch/de/26w38-de"
verification: single-source-national-cert
sourcing_note: "NCSC Switzerland (BACS) is the high-reliability national CERT reporting this as its own weekly advisory for its own jurisdiction; no independent second technical assessment was located."
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T07:03:05Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      The quotations from NCSC Switzerland's weekly review now link the BACS page they come from. A
      sentence claiming the rest of Google's email cannot be altered by the attacker is narrowed to
      what BACS states, the title no longer calls the app password an OAuth credential, and the
      phishing page is described as sending credentials directly to the attackers rather than
      relaying them in real time. The triage, detection and takeaway lines now cite the BACS report
      they follow. The detection line now follows BACS's own advice on app passwords.
    fields: [body, title]
migrated_from: null
---

NCSC Switzerland (BACS) reports a fraud chain that combines abuse of a legitimate Google account-security feature with vishing and app-password persistence ([NCSC Switzerland, 2026-09-22](https://www.bacs.admin.ch/de/26w38-de)). Attackers create their own Google account, register the victim's email address as its "recovery address," then generate an app password inside their own account and label it with social-engineering text impersonating a support case: "they then generated an app password in their own account and labelled it in the free-text field with: 'Kevin W. Case-ID: 834333 To view your case…'" (translated from German; [NCSC Switzerland, 2026-09-22](https://www.bacs.admin.ch/de/26w38-de)). "Google's automated system then sent an official, technically flawless security warning to the victim. Because the naming text was automatically carried into the email, it looked to the recipient as if Google were running an urgent support case with a case handler and case number" (translated from German; [NCSC Switzerland, 2026-09-22](https://www.bacs.admin.ch/de/26w38-de)). The victim therefore receives an authentic Google security alert whose attacker-chosen label makes it read like an active support ticket ([NCSC Switzerland, 2026-09-22](https://www.bacs.admin.ch/de/26w38-de)). A follow-up vishing call from a spoofed Swiss number posing as a Google landline, which got through despite Switzerland's mid-2026 rules against spoofed Swiss numbers from abroad, then pressures the victim to resolve the "compromise" via a phishing page hosted on the legitimate sites.google.com domain rather than accounts.google.com, whose embedded form sends entered credentials directly to the attackers ([NCSC Switzerland, 2026-09-22](https://www.bacs.admin.ch/de/26w38-de)). Once inside the real account, the attacker provisions their own app password within minutes, a special access code for older applications that works without two-factor confirmation, giving persistent access that survives a subsequent password change: "as a result, the perpetrators retained access to the account even after a password change. In the reported case, emails and contacts continued to sync unnoticed to a device abroad for an extended period after the attack" (translated from German; [NCSC Switzerland, 2026-09-22](https://www.bacs.admin.ch/de/26w38-de)).

**Triage:** legitimate Google administrators and helpdesks never call account holders unprompted about a security case; the tell is the free-text "case ID" riding inside an otherwise-genuine Google recovery-address notification, and any login page served from sites.google.com rather than accounts.google.com ([NCSC Switzerland, 2026-09-22](https://www.bacs.admin.ch/de/26w38-de)). Detection and hardening: an app password works without two-factor confirmation and kept the attackers in the account after a password change, so BACS advises deleting every app password and checking recovery addresses and automatic forwarding rules ([NCSC Switzerland, 2026-09-22](https://www.bacs.admin.ch/de/26w38-de)). A newly created app password on an account is therefore an incident-response signal in its own right.

**Defender takeaway:** a password reset alone does not evict this class of compromise. Where credentials may have been entered on such a lure, NCSC Switzerland advises deleting every stored app password without exception ([NCSC Switzerland, 2026-09-22](https://www.bacs.admin.ch/de/26w38-de)).

## Correction — 2026-09-30T07:03:05Z

BACS describes the Google alert as official and technically flawless, with the attacker's app-password label carried into it automatically ([NCSC Switzerland, 2026-09-22](https://www.bacs.admin.ch/de/26w38-de)). It does not say the rest of the email cannot be altered, a claim the entry previously made. BACS also describes an app password as a special access code for older applications that works without two-factor confirmation, and says the phishing page's form sent entered credentials directly to the attackers ([NCSC Switzerland, 2026-09-22](https://www.bacs.admin.ch/de/26w38-de)).
