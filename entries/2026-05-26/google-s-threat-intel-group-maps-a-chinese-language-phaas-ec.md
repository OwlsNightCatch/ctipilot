---
schema: 1
kind: research
title: "Google's threat-intel group maps a Chinese-language PhaaS ecosystem doing real-time OTP relay over RCS/iMessage"
headline: "Google's threat-intel group maps a Chinese-language PhaaS ecosystem doing real-time OTP relay over RCS/iMessage"
summary: "Google's threat-intel group details a Chinese-language PhaaS ecosystem performing real-time OTP relay over RCS/iMessage that defeats TOTP and SMS MFA — a live admin panel re-submits the victim's OTP on the real portal inside its validity window, and end-to-end-encrypted RCS/iMessage delivery bypasses carrier SMS filtering; Europe is explicitly named as a targeted region. FIDO2/WebAuthn is the countermeasure that removes the exposure (Google Threat Intelligence Group, 2026-05-25)."
discovered_at: "2026-05-26T05:00:04Z"
event_date: 2026-05-25
run_id: 2026-05-26-ae9d0d4b
priority: high
immediate_action: null
tags:
  - phishing
  - identity
  - organized-crime
  - ai-abuse
  - china-nexus
regions:
  - global
  - europe
sectors:
  - finance
  - public-sector
  - retail
entities: []
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/chinese-language-phishing-services/"
    publisher: "Google Threat Intelligence Group, 2026-05-25"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-26.md
---

Google Threat Intelligence Group published a teardown of around a dozen current Chinese-language phishing-as-a-service (PhaaS) offerings — case-studied through "YY Lai Yu" (YY来鱼) — whose shared headline capability is **real-time OTP relay**: a live operator admin panel captures the one-time code the victim types into a spoofed page and re-submits it on the genuine portal inside its validity window, completing the login and defeating TOTP- and SMS-based MFA without a classic reverse-proxy AiTM stack ([Google Threat Intelligence Group, 2026-05-25](https://cloud.google.com/blog/topics/threat-intelligence/chinese-language-phishing-services/)). `[SINGLE-SOURCE]` — GTIG primary research at time of writing. Two delivery and evasion properties make it operationally distinct: lures ride **RCS and iMessage**, whose end-to-end encryption blocks carrier-level SMS content filtering ([`T1566.002`](https://attack.mitre.org/techniques/T1566/002/)); and the kits use Puppeteer-driven AI page cloning to emit per-campaign-unique HTML/JS that frustrates signature-based phishing detection. Captured card-plus-OTP material is immediately provisioned into contactless wallet tokens for high-value transactions ([`T1111`](https://attack.mitre.org/techniques/T1111/) MFA interception). GTIG names Europe among explicitly targeted regions (alongside the Americas, Australia and the Middle East), notes targeting across 119 countries, and links UNC5814 to the Darcula PhaaS component; the infrastructure is rented, so victimology is buyer-driven rather than fixed to the Japan-heavy template library.

**Why it matters to us:** any CH/EU financial institution, e-government SSO portal or public-service login that relies on TOTP or SMS as its second factor is in scope — OTP relay neutralises both. FIDO2/WebAuthn (hardware keys or synced passkeys) removes the exposure entirely because the cryptographic assertion is bound to the legitimate origin and cannot be relayed; where FIDO2 cannot yet be deployed, bind the MFA validation to the original login session (IP/device) so a relayed OTP from a different ASN fails. Detection concept: correlate the IP/ASN seen at OTP issuance against the IP/ASN that consumes it within the SSO/IdP logs — an AiTM relay shows the victim's address on the phishing page and the operator's address on the real portal; alert on OTPs consumed seconds after issuance from a different ASN, and on contactless-wallet provisioning immediately following a credential submission from an unrecognised device.
