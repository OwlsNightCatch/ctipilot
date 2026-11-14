---
schema: 1
kind: threat
title: "\"Ghost-Sender\": Exchange Online accepts spoofed inbound mail bypassing SPF/DKIM/DMARC when a third-party MX fronts the tenant — no vendor patch"
headline: "\"Ghost-Sender\": Exchange Online accepts spoofed inbound mail bypassing SPF/DKIM/DMARC when a third-party MX fronts the tenant — no vendor patch"
summary: "\"Ghost-Sender\" lets attackers spoof any sender into Exchange Online inboxes, bypassing SPF/DKIM/DMARC — no vendor patch. Swiss firm InfoGuard disclosed the configuration flaw affecting tenants that front EXO with a third-party MX; NCSC-CH issued an advisory (InfoGuard, 2026-06-09)."
discovered_at: "2026-06-10T05:00:01Z"
event_date: 2026-06-09
run_id: 2026-06-10-c84347b2
priority: high
immediate_action: null
tags:
  - phishing
  - identity
  - cloud
regions:
  - switzerland
  - europe
sectors:
  - public-sector
entities:
  - "campaign:ghost-sender-exchange-online-spoofing"
cves: []
sources:
  - url: "https://labs.infoguard.ch/posts/ghost-sender/"
    publisher: "InfoGuard, 2026-06-09"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12619"
    publisher: "NCSC-CH, 2026-06-09"
    role: corroborating
  - url: "https://gbhackers.com/ghost-sender-flaw-exposes-exchange-online-users/"
    publisher: "GBHackers, 2026-06-09"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-10.md
---

Swiss security firm InfoGuard Labs disclosed "Ghost-Sender" on 9 June, a configuration-layer email-spoofing weakness affecting Microsoft 365 tenants whose published MX record points to a third-party gateway (Barracuda/Proofpoint/Mimecast) rather than Microsoft ([InfoGuard, 2026-06-09](https://labs.infoguard.ch/posts/ghost-sender/)). When inbound filtering is enforced only on the MX path, an attacker who knows the target domain can connect directly to the tenant's `*.mail.protection.outlook.com` endpoint and relay messages that present as any internal or external sender; because the delivery originates from Microsoft IP space, SPF passes, DKIM has no mismatched signature to fail on, and DMARC is evaluated favourably — the spoofed mail lands in the inbox, in some cases rendering the impersonated internal user's profile picture ([NCSC-CH, 2026-06-09](https://security-hub.ncsc.admin.ch/#/posts/12619)). InfoGuard reports that across its bug-bounty sample over 20% of Exchange Online domains were exploitable and roughly half of external-MX deployments lacked the mitigation; Microsoft characterised the behaviour as a known architectural limitation and has not shipped a platform fix, while NCSC-CH issued its own advisory and Microsoft Support confirmed active abuse ([NCSC-CH, 2026-06-09](https://security-hub.ncsc.admin.ch/#/posts/12619)). This is a configuration issue (no CVE), enabling high-fidelity BEC and internal-sender impersonation against any organisation on the affected architecture.

**Why it matters to us:** the EXO-plus-external-filter topology is the dominant Microsoft 365 model in Swiss and EU public-sector environments, and there is no patch — mitigation is configuration. Add an inbound connector of type "Partner"/"On-premises" that requires the gateway's pinned TLS certificate or approved IP ranges, and a priority-0 transport rule that quarantines or rejects inbound mail not arriving via the approved external-filter connector; ensure Enhanced Filtering for Connectors (skip-listing) is configured so EXO evaluates the true originating IP. Hunt in Message Trace for mail received on the `Default Frontend` connector rather than the expected partner connector.
