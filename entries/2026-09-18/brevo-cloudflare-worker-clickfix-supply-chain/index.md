---
schema: 1
kind: incident
title: "Brevo: a stolen, hardcoded Cloudflare API key let an attacker inject ClickFix malware and a WordPress backdoor plugin via a CDN-edge Worker into more than 100,000 customer sites, defeating origin-side integrity checks"
headline: "Brevo's own integrity checks never saw the tampering because the attacker rewrote pages at Cloudflare's edge, not on Brevo's servers"
summary: >
  Brevo (CRM/email platform, formerly Sendinblue) confirmed a stolen long-lived Cloudflare API
  key let an attacker deploy a malicious edge Worker that rewrote Brevo's own pages and three
  customer-embedded widget scripts for roughly 5.5 hours on 2026-09-14, serving a ClickFix
  clipboard-paste lure and a WordPress administrator-backdoor plugin to more than 100,000 sites
  embedding the affected scripts, without modifying any origin file.
discovered_at: "2026-09-18T05:02:00Z"
updated_at: null
event_date: "2026-09-14"
run_id: 2026-09-18T0410Z-intel
priority: high
immediate_action: null
tags: [supply-chain, phishing]
regions: [global]
sectors: [technology]
entities: ["incident:brevo-cloudflare-worker-clickfix-supply-chain-2026-09"]
techniques: [T1552.001, T1078.004, T1195.002, T1204.004]
affected_products: ["Brevo"]
cves: []
sources:
  - url: "https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up"
    publisher: "Brevo"
    date: "2026-09-17"
    role: primary
  - url: "https://sansec.io/research/brevo-supply-chain-attack"
    publisher: "Sansec"
    date: "2026-09-16"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/"
    publisher: "BleepingComputer"
    date: "2026-09-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A long-lived Cloudflare API key with full account permissions was stored in application source code and was obtained by the attacker. With it, they could create Workers, routes and DNS records on Brevo's zones without triggering an alert."
    publisher: "Brevo"
    source_url: "https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up"
  - quote: "Because the Worker rewrote responses at the edge and removed security headers such as Content-Security-Policy, our origin servers and files remained unmodified and standard integrity checks did not detect the change."
    publisher: "Brevo"
    source_url: "https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up"
  - quote: "The plugin also stores a backup copy of the last valid JavaScript URL so it can continue loading malicious code if the remote server becomes unavailable."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/"
  - quote: "the plugin contains a hardcoded authentication key that allows attackers to generate a valid login session for a WordPress administrator account without knowing the account password."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/"
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Audit the bytes actually served by every third-party embedded widget or SDK script your organization uses — external synthetic monitoring, or Subresource Integrity pinning where the vendor supports it — since an edge-level compromise of the vendor's CDN account will not show up in the vendor's own origin-side integrity checks."
updates:
  - at: "2026-09-20T13:34:04Z"
    run_id: 2026-09-20T1308Z-audit
    type: correction
    summary: >
      The scope figure was inverted. Sansec reports that Brevo served malware to visitors of its own site
      and more than 100,000 customer sites; the title, summary and analysis all said "up to 100,000" and
      the analysis called it an upper bound. It is a floor, so the entry understated the reported reach.
      The title, summary and the body sentence now state what Sansec states.
    fields: [title, summary, body]
migrated_from: null
---

Brevo (CRM/email-marketing platform, formerly Sendinblue) confirmed in a 2026-09-17 post-mortem that an attacker used a long-lived Cloudflare API key with full account permissions, hardcoded in Brevo's application source code, to create a malicious Cloudflare Worker on Brevo's own account, first misused as early as late August 2026 ([Brevo, 2026-09-17](https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up)). Brevo's own stated impact window ran 15:01 to 20:30 UTC on 2026-09-14 (5 hours 29 minutes), during which the Worker rewrote HTTP responses at the CDN edge on brevo.com and related domains, stripping security headers such as Content-Security-Policy; from 16:07 UTC the Worker additionally appended a malicious loader to three JavaScript files, the Brevo forms script, the Conversations widget and the SDK loader, that customers embed directly on their own sites, and extended the tampering to sibforms.com ([Brevo, 2026-09-17](https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up)). Because the edge rewrite never touched an origin file, Brevo's own standard integrity checks did not detect the change ([Brevo, 2026-09-17](https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up)). Visitors saw a fake Cloudflare human-verification page instructing them to press Win+R, paste and press Enter, a ClickFix lure that ran an attacker-supplied clipboard command to download Windows malware ([Brevo, 2026-09-17](https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up)), and did not activate for crawlers, developers or automated scanners ([Sansec, 2026-09-16](https://sansec.io/research/brevo-supply-chain-attack)). On WordPress sites embedding an affected widget, a logged-in administrator's browser silently installed a plugin impersonating "Web Media Optimizer" that hides itself from the plugin list, persists via the must-use-plugins directory, beacons to an attacker server for a Base64-encoded next-stage JavaScript URL, caches the last-valid URL as a fallback, and carries a hardcoded authentication key that lets the attacker generate a valid WordPress-administrator login session without the account password ([BleepingComputer, 2026-09-17](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)). Sansec independently corroborated the root cause before Brevo's own confirmation, matching Last-Modified timestamps across injected and clean asset versions and finding an SSL certificate for the attacker's infrastructure issued 2026-08-25, pinning the attacker's access to at least that date ([Sansec, 2026-09-16](https://sansec.io/research/brevo-supply-chain-attack)); Sansec states that Brevo "served malware to visitors of its own site and more than 100 thousand customer sites", the figure coming from a live search for sites embedding the affected components ([Sansec, 2026-09-16](https://sansec.io/research/brevo-supply-chain-attack)); it is a floor on the sites carrying those components, not a confirmed count of sites whose visitors received the payload. Brevo's post-mortem does not mention a separate SSO-hijacking incident it disclosed on 2026-09-10 that BleepingComputer reports led to a phishing campaign against Trezor customers, and BleepingComputer states Brevo did not respond to its question about whether the two incidents were connected ([BleepingComputer, 2026-09-17](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)).

**Defender takeaway:** any organization embedding a third-party widget or SDK should monitor the actual bytes served by that script's URL over time, external synthetic monitoring or Subresource Integrity pinning where the vendor supports it, rather than trusting the vendor's own origin-side security, since a compromised CDN-edge account can inject content into every downstream site without ever touching a file an origin-side integrity monitor would see.

**Triage:** a legitimate Brevo or Sendinblue widget script served from its normal CDN path is expected; the discriminator here is behavioral, not path-based — a fake human-verification overlay instructing a clipboard-paste-and-run action is never legitimate CDN content, and any WordPress site should treat a plugin absent from its own admin plugin list, yet present in the must-use-plugins directory, as compromised.

## Correction — 2026-09-20T13:34:04Z

Sansec's count is a floor, not a ceiling. Its write-up states that on 14 September "Brevo served malware to visitors of its own site and more than 100 thousand customer sites", linking that figure to a live search for sites embedding the affected components ([Sansec, 2026-09-16](https://sansec.io/research/brevo-supply-chain-attack)). This entry previously described the same figure as an upper bound of up to 100,000 sites, which understates the reach Sansec reported.
