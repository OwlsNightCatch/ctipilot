---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: Microsoft 365 account-takeover tradecraft converged this week on auth flows Conditional Access rarely covers — device-code, AiTM, ROPC and manager-impersonation vishing all beat MFA without breaking it
headline: M365 identity attacks converged this week — device-code, AiTM PhaaS, ROPC spray and vishing all bypass MFA/Conditional Access by sidestepping it
summary: 'Four independent 2026-W28 disclosures describe the same M365 account-takeover pattern from different angles: Huntress'' root-cause comparison of the Railway (device-code) and LSHIY (ROPC spray) campaigns, where 55 of 78 LSHIY-compromised accounts had CA policies requiring MFA that failed on scoping gaps; the Forg365 AiTM phishing-as-a-service kit; and the Helix data-extortion cluster pairing manager-impersonation vishing with device-code phishing. None defeats MFA cryptographically — each exploits an auth flow (device-code, ROPC/legacy, token replay) that a typical Conditional Access policy does not gate. Every M365 tenant should block device-code and ROPC where unused and confirm CA covers all cloud apps and client-app types.'
discovered_at: '2026-07-12T23:24:00Z'
event_date: 2026-07-10
run_id: 2026-07-12T2309Z-weekly
priority: high
immediate_action: null
tags:
  - identity
  - phishing
  - cloud
  - auth-bypass
  - data-breach
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
entities:
  - campaign:railway-device-code-phishing-m365-2026
  - campaign:lshiy-ropc-azure-cli-password-spray-2026
  - actor:helix-extortion
  - tool:forg365-phaas
cves: []
sources:
  - url: https://www.huntress.com/blog/conditional-access-misconfigurations
    publisher: Huntress
    role: primary
  - url: https://zerobec.com/blog/inside-forg365-telegram-distributed-sneaky2fa-style-phaas
    publisher: ZeroBEC
    role: primary
  - url: https://reliaquest.com/blog/threat-spotlight-helix-new-name-in-data-extortion-ecosystem
    publisher: ReliaQuest
    role: primary
closed_sources: []
evidence:
  - quote: Device code phishing is effective because it doesn't try to beat MFA. It sidesteps it.
    publisher: Huntress
  - quote: Of the 78 compromised accounts, 55 had active Conditional Access policies requiring MFA.
    publisher: Huntress
verification: multi-source
sourcing_note: Three independent research primaries (Huntress, ZeroBEC, ReliaQuest) describe the same class of Conditional-Access-sidestepping M365 attack from separate campaigns; the cross-day convergence is the synthesis, not a single vendor claim. Reliability B, credibility 1 (the pattern is corroborated across independent reporters).
confidence: high
classification:
  reliability: B
  credibility: 1
update_of: null
references:
  - 2026-07-10/m365-conditional-access-gaps-railway-lshiy-campaigns
  - 2026-07-10/forg365-m365-phaas-aitm-devicecode-forgcookie
  - 2026-07-10/helix-data-extortion-devicecode-vishing-sharepoint-exfil
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - Block the OAuth device-code flow (and ROPC / legacy auth) for every M365 user population that does not require it, and set Conditional Access to fail-closed so an uncovered client-app type or cloud app cannot silently skip MFA.
  - 'Hunt Entra sign-in logs for the sidestep signatures: device-code grants to unmanaged devices, ROPC/`/token`-endpoint authentication against Azure CLI, and successful sign-ins from accounts whose CA policy should have required MFA but recorded none.'
---
Four separate 2026-W28 disclosures describe one problem: Microsoft 365 account takeover is increasingly achieved not by defeating multi-factor authentication but by choosing an authentication path that Conditional Access commonly fails to gate. Huntress' comparative root-cause analysis of two campaigns made the mechanism explicit — "device code phishing is effective because it doesn't try to beat MFA. It sidesteps it," and in the ROPC-based LSHIY campaign "of the 78 compromised accounts, 55 had active Conditional Access policies requiring MFA" that still failed, because legacy/ROPC authentication through the `/token` endpoint never reaches the authorization endpoint where CA is enforced ([Huntress, 2026-07-10](https://www.huntress.com/blog/conditional-access-misconfigurations)). The same week, ZeroBEC documented **Forg365**, a Telegram-distributed adversary-in-the-middle phishing-as-a-service kit purpose-built to relay M365 auth and steal session cookies ([ZeroBEC, 2026-07-10](https://zerobec.com/blog/inside-forg365-telegram-distributed-sneaky2fa-style-phaas)), and ReliaQuest profiled the **Helix** data-extortion cluster pairing manager-impersonation vishing with device-code phishing before SharePoint exfiltration ([ReliaQuest, 2026-07-10](https://reliaquest.com/blog/threat-spotlight-helix-new-name-in-data-extortion-ecosystem)). Read together with the week's ShinyHunters/Odido vishing attribution, the through-line is a maturing, commoditised identity-attack economy targeting the same tenant surface.

**Why this is a cross-day pattern, not four items:** device-code phishing, AiTM cookie theft, ROPC spraying and impersonation vishing are distinct techniques, but they exploit the *same* structural gap — a Conditional Access posture that assumes MFA coverage it does not actually enforce across every flow, client-app type and cloud app. A tenant that hardened against one of these this week is not hardened against the others.

**Defender takeaway:** treat Conditional Access coverage completeness — not the presence of an MFA requirement — as the control to audit; block device-code and ROPC/legacy auth for populations that do not need them, and verify no cloud app or client-app type is exempt. **Triage:** a legitimate device-code grant comes from a genuine input-constrained device enrolment the user initiated; the attack signature is a device-code grant to an unmanaged/unexpected device shortly after a phishing lure, or successful authentication via ROPC/`/token` against Azure CLI from an account and location with no history of CLI use.
