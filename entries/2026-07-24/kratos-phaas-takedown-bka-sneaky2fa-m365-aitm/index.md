---
schema: 1
kind: threat
title: "German BKA dismantles Kratos, the Sneaky2FA-derived AiTM phishing-as-a-service platform behind ~15,000 monthly Microsoft 365 credential-theft campaigns"
headline: "A German-led takedown removes Kratos's infrastructure — but the AiTM tradecraft and affiliate base survive, as Tycoon2FA already showed"
summary: >
  Germany's BKA, with US and Indonesian partners, seized the infrastructure of Kratos — an adversary-in-the-middle
  phishing-as-a-service platform evolved from Sneaky2FA that generated deceptive Microsoft 365 login pages,
  including browser-in-the-browser fake windows — and arrested its administrator. Roughly 1,800 subscribers ran an
  estimated 15,000 campaigns a month. The tradecraft and affiliate base, not just infrastructure, are the risk.
discovered_at: "2026-07-24T04:36:09Z"
event_date: "2026-07-20"
run_id: 2026-07-24T0409Z-intel
priority: notable
immediate_action: null
tags: [phishing, identity, law-enforcement, organized-crime]
regions: [europe, us, global]
sectors: [public-sector, finance, technology]
entities: [tool:kratos-phaas]
techniques: [T1557, T1566.002, T1539]
affected_products: ["Microsoft 365"]
cves: []
sources:
  - url: "https://www.bka.de/SharedDocs/Kurzmeldungen/DE/Kurzmeldungen/260720_Schlag_gegen_Phishing_Gruppierung_Kratos.html"
    publisher: "Bundeskriminalamt (BKA), Germany"
    date: "2026-07-20"
    role: primary
  - url: "https://www.trendmicro.com/en_us/research/26/g/kratos-takedown.html"
    publisher: "Trend Micro Research"
    date: "2026-07-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Over 1,800 criminal subscribers had rented access to Kratos and used it to run an estimated 15,000 phishing campaigns a month."
    publisher: "Trend Micro Research"
  - quote: "bedeutender Ermittlungserfolg gegen eine der weltweit gefährlichsten Phishing-as-a-Service-Gruppierung"
    publisher: "Bundeskriminalamt (BKA)"
verification: multi-source
sourcing_note: "BKA is the primary disclosing authority for its own operation; Trend Micro corroborates independently as the threat-intelligence partner that tracked Sneaky2FA's evolution into Kratos. The BKA quote is the original German ('a significant investigative success against one of the world's most dangerous phishing-as-a-service groups')."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

Germany's Bundeskriminalamt (BKA), with the Frankfurt cybercrime prosecutor (ZIT), US law enforcement and Indonesian authorities, announced on 20 July 2026 the takedown of **Kratos** — a phishing-as-a-service (PhaaS) platform that sold subscribers a turnkey adversary-in-the-middle toolkit for generating convincing Microsoft 365 authentication pages ([BKA, 2026-07-20](https://www.bka.de/SharedDocs/Kurzmeldungen/DE/Kurzmeldungen/260720_Schlag_gegen_Phishing_Gruppierung_Kratos.html)). Per BKA and Trend Micro — which had tracked Sneaky2FA's evolution into Kratos since December 2024 — the platform added browser-in-the-browser (BitB) fake login windows in November 2025 and Cloudflare Turnstile anti-bot challenges to blunt automated analysis and takedown, and ran an estimated 15,000 phishing campaigns a month across 200+ servers for roughly 1,800 subscribers ([Trend Micro, 2026-07-22](https://www.trendmicro.com/en_us/research/26/g/kratos-takedown.html)). Authorities seized the infrastructure and arrested the platform's developer/technical administrator in Indonesia ([BKA, 2026-07-20](https://www.bka.de/SharedDocs/Kurzmeldungen/DE/Kurzmeldungen/260720_Schlag_gegen_Phishing_Gruppierung_Kratos.html)).

**Defender takeaway:** A takedown removes infrastructure, not the affiliate base or the kit's code — so Swiss and European M365 tenants should expect Kratos affiliates to rebrand and re-tool rather than stand down, the pattern other AiTM phishing-as-a-service operations have followed after their own disruptions. The durable defence is against the AiTM technique class, not this brand: enforce phishing-resistant authentication (FIDO2/passkeys or certificate-based) for privileged and high-value M365 accounts, since AiTM proxies relay password and OTP but cannot replay a hardware-bound assertion, and treat a valid sign-in from an anomalous location immediately after a session-token event as a token-replay indicator. **Triage:** BitB and off-domain hosting give two concrete discriminators a real Microsoft login lacks — a "browser window" rendered as an in-page DOM overlay rather than a genuine top-level navigation to `login.microsoftonline.com`, and a Microsoft-branded login flow gated behind a Cloudflare Turnstile challenge and served from a non-Microsoft domain; either should fail a user or a URL-inspection control before credentials are entered.
