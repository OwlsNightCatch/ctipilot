---
schema: 1
kind: incident
title: "Brevo: a stolen Cloudflare API key let an attacker rewrite Brevo pages and widget scripts at the CDN edge, serving ClickFix malware and a WordPress backdoor plugin"
headline: "Brevo's own integrity checks never saw the tampering because the attacker rewrote pages at Cloudflare's edge, not on Brevo's servers"
summary: >
  Brevo (CRM/email platform, formerly Sendinblue) confirmed a stolen long-lived Cloudflare API key
  let an attacker deploy a malicious edge Worker that rewrote Brevo's own pages and three customer-embedded
  widget scripts for roughly 5.5 hours on 2026-09-14, serving a ClickFix clipboard-paste
  lure and a WordPress administrator-backdoor plugin without modifying any origin file. Sansec
  says Brevo served malware to visitors of more than 100,000 customer sites, a figure it links to
  a public source-code search for pages mentioning Brevo's domains. BleepingComputer reports the
  same research as up to 100,000 sites using the affected components.
discovered_at: "2026-09-18T05:02:00Z"
updated_at: null
event_date: "2026-09-14"
run_id: 2026-09-18T0410Z-intel
priority: notable
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
  - "On every WordPress site that loaded a Brevo forms, Conversations or SDK script on 2026-09-14 and had an administrator visit while logged in, check for any plugin installed or activated that day and compare the plugin directory on disk with the admin plugin list, because the known backdoor (impersonating \"Web Media Optimizer\") hides from that list and copies itself into the must-use-plugins directory. Remove any such plugin, invalidate all administrator sessions, change administrator passwords and review administrator accounts, because its hardcoded key mints admin logins without a password."
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
  - at: "2026-09-30T07:02:20Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      The action was generic third-party-script monitoring advice that restated the takeaway. It is
      replaced by the compromise check Brevo, Sansec and BleepingComputer give for WordPress sites
      that embedded the affected scripts. The priority moves from high to notable because a Swiss
      public body is exposed only if its site embedded Brevo widgets during a closed 5.5-hour
      window. The triage line treated every plugin missing from the admin list but present in the
      must-use-plugins directory as compromised, and now gives Sansec's checks and the plugin name.
      The title is shortened, the 100,000 figure is stated as Sansec and BleepingComputer each frame
      it, and Sansec's root-cause assessment keeps its hedge. An exposure line adds Brevo's guidance
      for anyone who ran the pasted command or logged in to Brevo that day.
    fields: [priority, actions, body, title, summary]
migrated_from: null
---

Brevo (CRM/email-marketing platform, formerly Sendinblue) confirmed in a 2026-09-17 post-mortem that an attacker used a long-lived Cloudflare API key with full account permissions, hardcoded in Brevo's application source code, to create a malicious Cloudflare Worker on Brevo's own account, first misused as early as late August 2026 ([Brevo, 2026-09-17](https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up)). Brevo's own stated impact window ran 15:01 to 20:30 UTC on 2026-09-14 (5 hours 29 minutes), during which the Worker rewrote HTTP responses at the CDN edge on brevo.com and related domains, stripping security headers such as Content-Security-Policy; from 16:07 UTC the Worker additionally appended a malicious loader to three JavaScript files, the Brevo forms script, the Conversations widget and the SDK loader, that customers embed directly on their own sites, and extended the tampering to sibforms.com ([Brevo, 2026-09-17](https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up)). Because the edge rewrite never touched an origin file, Brevo's own standard integrity checks did not detect the change ([Brevo, 2026-09-17](https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up)). Visitors saw a fake Cloudflare human-verification page instructing them to press Win+R, paste and press Enter, a ClickFix lure that ran an attacker-supplied clipboard command to download Windows malware ([Brevo, 2026-09-17](https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up)), and did not activate for crawlers, developers or automated scanners ([Sansec, 2026-09-16](https://sansec.io/research/brevo-supply-chain-attack)). On WordPress sites embedding an affected widget, a logged-in administrator's browser was used to attempt the install of a plugin impersonating "Web Media Optimizer" that hides itself from the plugin list, persists via the must-use-plugins directory, beacons to an attacker server for a Base64-encoded next-stage JavaScript URL, caches the last-valid URL as a fallback, and carries a hardcoded authentication key that lets the attacker generate a valid WordPress-administrator login session without the account password ([BleepingComputer, 2026-09-17](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)). Before Brevo's confirmation, Sansec named a breach of Brevo's Cloudflare account as the possible root cause, citing hints such as modified assets that kept the same Last-Modified dates before, during and after the incident. It also found that a certificate for an attacker-created host under a Brevo-owned domain was issued on 2026-08-25, which it says shows the attacker had write access to Brevo's DNS records ([Sansec, 2026-09-16](https://sansec.io/research/brevo-supply-chain-attack)). Sansec states that Brevo "served malware to visitors of its own site and more than 100 thousand customer sites", linking the figure to a public source-code search for pages that mention Brevo's domains ([Sansec, 2026-09-16](https://sansec.io/research/brevo-supply-chain-attack)). BleepingComputer reports the same research as up to 100,000 websites that use the affected Brevo components ([BleepingComputer, 2026-09-17](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)), so the two outlets frame the figure differently, as a floor and as a ceiling. Brevo's post-mortem does not mention a separate SSO-related incident ([Brevo, 2026-09-17](https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up)). BleepingComputer reports that Brevo disclosed that incident on 2026-09-10, that attackers hijacked customer accounts and launched phishing that reached Trezor customers, and that Brevo did not respond to its question about whether the two incidents were connected ([BleepingComputer, 2026-09-17](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)).

**Exposure:** beyond WordPress administrators, anyone who followed the fake verification prompt on 2026-09-14, within Brevo's stated impact window of 15:01 to 20:30 UTC, and ran the pasted command is exposed. Brevo says to treat that computer as compromised, disconnect it, run a full antivirus scan and change the passwords used on it, starting with the Brevo password. It also asks anyone who logged in to Brevo via brevo.com on 14 September to change their password and review their API keys ([Brevo, 2026-09-17](https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up)).

**Defender takeaway:** any organization embedding a third-party widget or SDK should monitor the actual bytes served by that script's URL over time, external synthetic monitoring or Subresource Integrity pinning where the vendor supports it, rather than trusting the vendor's own origin-side security, since a compromised CDN-edge account can inject content into every downstream site without ever touching a file an origin-side integrity monitor would see.

**Triage:** a legitimate Brevo or Sendinblue widget script served from its normal CDN path is expected, so the discriminator is behavioral, not path-based. A fake human-verification overlay instructing a clipboard-paste-and-run action is never legitimate CDN content. On WordPress, the compromise signs Sansec gives are a plugin installed or activated on 14 September, a plugin on disk that the admin screen does not list, and an access-log `POST` to `/wp-admin/update.php?action=upload-plugin` that day followed shortly by a plugin activation request ([Sansec, 2026-09-16](https://sansec.io/research/brevo-supply-chain-attack)). BleepingComputer names the known backdoor plugin "Web Media Optimizer" ([BleepingComputer, 2026-09-17](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)).

## Correction — 2026-09-20T13:34:04Z

Sansec's count is a floor, not a ceiling. Its write-up states that on 14 September "Brevo served malware to visitors of its own site and more than 100 thousand customer sites", linking that figure to a public source-code search for pages that mention Brevo's domains ([Sansec, 2026-09-16](https://sansec.io/research/brevo-supply-chain-attack)). The figure was previously described as an upper bound of up to 100,000 sites, which understates the reach Sansec reported.

## Correction — 2026-09-30T07:02:20Z

The compromise checks Sansec gives for WordPress sites are a plugin installed or activated on 14 September and a plugin on disk that the admin screen does not list ([Sansec, 2026-09-16](https://sansec.io/research/brevo-supply-chain-attack)), and BleepingComputer names the backdoor plugin "Web Media Optimizer" ([BleepingComputer, 2026-09-17](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)).

Sansec states that Brevo served malware to visitors of more than 100,000 customer sites and links the figure to a public source-code search for pages that mention Brevo's domains ([Sansec, 2026-09-16](https://sansec.io/research/brevo-supply-chain-attack)). BleepingComputer reports it as up to 100,000 websites that use the affected Brevo components ([BleepingComputer, 2026-09-17](https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)). Sansec presents the Cloudflare-account breach as a possible root cause supported by hints, not as a confirmed finding ([Sansec, 2026-09-16](https://sansec.io/research/brevo-supply-chain-attack)).
