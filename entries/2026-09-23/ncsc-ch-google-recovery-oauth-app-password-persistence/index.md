---
schema: 1
kind: threat
title: "NCSC Switzerland: Google recovery-address abuse plus a Sites-hosted phishing page plants an OAuth app-password backdoor that survives a password reset"
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
updates: []
migrated_from: null
---

NCSC Switzerland (BACS) reports a fraud chain that combines abuse of a legitimate Google account-security feature with vishing and app-password persistence. Attackers create their own Google account, register the victim's email address as its "recovery address," then generate an app password inside their own account and label it with social-engineering text impersonating a support case: "they then generated an app password in their own account and labelled it in the free-text field with: 'Kevin W. Case-ID: 834333 To view your case…'" (translated from German; NCSC Switzerland, 2026-09-22). "Google's automated system then sent an official, technically flawless security warning to the victim. Because the naming text was automatically carried into the email, it looked to the recipient as if Google were running an urgent support case with a case handler and case number" (translated from German; NCSC Switzerland, 2026-09-22). Google's recovery-notification email is itself genuine and unmodifiable by the attacker except for that free-text label, so the victim receives an authentic Google security alert that reads like an active support ticket. A follow-up vishing call from a spoofed Swiss-looking number — surviving Switzerland's mid-2026 anti-spoofing rules for foreign-originated calls — then pressures the victim to resolve the "compromise" via a phishing page hosted on the legitimate sites.google.com domain rather than accounts.google.com, which relays entered credentials to the attacker in real time. Once inside the real account, the attacker immediately provisions their own app password — a legacy credential type that bypasses two-factor authentication — giving persistent access that survives a subsequent password change: "as a result, the perpetrators retained access to the account even after a password change. In the reported case, emails and contacts continued to sync unnoticed to a device abroad for an extended period after the attack" (translated from German; NCSC Switzerland, 2026-09-22).

**Triage:** legitimate Google administrators and helpdesks never call account holders unprompted about a security case; the tell is the free-text "case ID" riding inside an otherwise-genuine Google recovery-address notification, and any login page served from sites.google.com rather than accounts.google.com. Detection and hardening: audit and restrict app-password issuance on any Google account, and treat an app-password creation event with the same sensitivity as a new OAuth grant for incident-response purposes, since it is a durable, MFA-bypassing credential that a full password rotation does not revoke.

**Defender takeaway:** a password reset alone does not evict this class of compromise; any account known to have received a Google security notification tied to an unrecognized recovery-address change should also have its app-password list audited and cleared.
