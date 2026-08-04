---
schema: 1
kind: threat
horizon: operational
title: "SonicWall SMA 1000 (CVE-2026-15409/-15410) escalation: Rapid7 calls INC Ransom the dominant actor on the chain, and says it watched the actor roll an applied patch back to stay in"
headline: "A patched SMA 1000 is not evidence of eviction — Rapid7 observed the actor reverting the fix, and victims are now getting fake incident-response calls"
summary: >
  Update to this pipeline's 2026-07-18 SonicWall SMA 1000 kill-chain entry. Rapid7's director of vulnerability
  intelligence told The Hacker News on 2026-08-03 that INC Ransom "has emerged as the dominant threat actor actively
  weaponizing this vulnerability chain" — a characterisation, not a new link, since Rapid7 first attributed the activity
  to INC on 2026-07-17. Two facts change defender behaviour. Rapid7 observed the actor rolling a newly applied patch
  back to a vulnerable state to keep access, so patch state has to be re-verified after remediation and an up-to-date
  version string is not evidence of eviction. And at the extortion stage victims are receiving unsolicited email and
  telephone contact from parties offering to help with their ransomware problem. Resecurity also widens the required
  credential-rotation scope well beyond passwords and MFA seeds.
discovered_at: "2026-08-04T06:10:00Z"
event_date: "2026-08-03"
run_id: 2026-08-04T0411Z-intel
priority: high
immediate_action: null
tags: [ransomware, actively-exploited, vulnerabilities, organized-crime]
regions: [global]
sectors: [public-sector, energy, finance, healthcare, telco]
entities: ["actor:inc-ransom", "actor:uta0533", "tool:sonicwall-sma-uta0533-toolset"]
techniques: [T1601.002, T1539, T1111, T1657, T1486]
affected_products: ["SonicWall Secure Mobile Access (SMA) 1000"]
cves:
  - id: CVE-2026-15409
    cvss: "10.0"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "SMA 1000 (6210, 7210, 8200v and CMS, all hypervisors) 12.4.3-03245, 12.4.3-03387, 12.4.3-03434; 12.5.0-02283, 12.5.0-02624, 12.5.0-02800"
    fixed: "12.4.3-03453 and higher; 12.5.0-02835 and higher"
  - id: CVE-2026-15410
    cvss: "7.2"
    epss: null
    type: rce
    vector: zero-click
    auth: admin-required
    status: [exploited, cisa-kev, patch-available]
    affected: "Same SMA 1000 build list as CVE-2026-15409"
    fixed: "12.4.3-03453 and higher; 12.5.0-02835 and higher"
sources:
  - url: "https://thehackernews.com/2026/08/inc-ransomware-emerges-as-dominant.html"
    publisher: "The Hacker News"
    date: "2026-08-03"
    role: primary
  - url: "https://www.resecurity.com/blog/article/from-wsproxy-to-root-inc-ransomware-and-sonicwall-sma-exploit-chain"
    publisher: "Resecurity"
    date: "2026-08-01"
    role: primary
  - url: "https://www.securityweek.com/recent-sonicwall-vulnerabilities-exploited-in-ransomware-attacks/"
    publisher: "SecurityWeek"
    date: "2026-08-03"
    role: corroborating
  - url: "https://www.darkreading.com/vulnerabilities-threats/inc-ransomware-exploits-sonicwall-sma-zero-days"
    publisher: "Dark Reading"
    date: "2026-07-17"
    role: corroborating
  - url: "https://www.sonicwall.com/support/notices/product-notice-sma-1000-series-affected-by-multiple-vulnerabilities/kA1VN000001nv6D0AQ"
    publisher: "SonicWall"
    date: "2026-07-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "More recently, INC Ransomware has emerged as the dominant threat actor actively weaponizing this vulnerability chain."
    publisher: "The Hacker News"
  - quote: "We observed the threat actor maintaining persistence and rolling the newly applied patch back to a vulnerable state to maintain access. A comprehensive forensic review of the firewall is required to ensure complete eviction."
    publisher: "Dark Reading"
  - quote: "Setuid binaries, Python injectors, modified init scripts, and NGINX Unit configuration changes can survive reboots and may persist after a superficial firmware upgrade if not remediated. A patched appliance that still contains ROOTRUN or KNUCKLEBALL remains compromised."
    publisher: "Resecurity"
  - quote: "many of the new victims received emails, as well as phone calls from unknown organizations claiming to assist with ransomware issues"
    publisher: "Resecurity"
  - quote: "The new victims listed on INC Ransomware's DLS between July 17, 2026 and August 1, 2026 include private sector and government organizations from Australia, the US, UAE, Colombia, Switzerland, and other countries."
    publisher: "Resecurity"
verification: multi-source
sourcing_note: >
  The in-window publication event is the 2026-08-03 reporting (The Hacker News, SecurityWeek, SC Media) of Resecurity's
  2026-08-01 research, together with a named Rapid7 statement that appears only in The Hacker News and nowhere on
  Rapid7's own blog. The Resecurity research post itself and the Dark Reading report carrying the patch-rollback
  observation are both outside the 26 h window and are cited as the substantive basis for an in-window update rather
  than as fresh news. Two attribution limits matter: Rapid7's INC link dates to 2026-07-17, so the actor identification
  is not new — only the "dominant" characterisation is; and Resecurity's phrasing that "Volexity and Rapid7 have since
  linked the exploitation cluster to INC Ransomware" overstates the record, because Volexity has published no INC link
  at all and tracks the cluster only as UTA0533. The victim-geography sentence is a single-vendor characterisation of
  criminal leak-site postings, uncorroborated and not tied to this exploit chain per listing; on its own it would rate
  credibility 4, and it does not drive this entry's regions, sectors or relevance.
confidence: medium
update_of: 2026-07-18/sonicwall-sma1000-uta0533-exploitation-kill-chain
references: [2026-07-14/sonicwall-sma1000-ssrf-cve-2026-15409-actively-exploited]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "On every SMA 1000 you remediated for CVE-2026-15409/-15410, re-verify the installed firmware version now and alert on any later regression — Rapid7 observed the actor rolling an applied patch back to a vulnerable state, so the version you installed is not necessarily the version running."
  - "Widen the rotation already performed on any exposed SMA 1000 beyond account passwords and TOTP seeds to the full set the appliance handled: SMA administrator passwords, directory-service bind credentials for LDAP, RADIUS and Active Directory, every user account that authenticated during the exposure window, and all certificates and API keys configured on the appliance."
migrated_from: null
---

**UPDATE (originally covered 2026-07-18):** the earlier entry reconstructed UTA0533's appliance-to-network kill chain against SonicWall SMA 1000 and told readers to treat an exposed, unpatched appliance as compromised rather than merely vulnerable. That direction stands. Four things have moved since, and two of them change what "remediated" means.

**Who is on the chain.** Rapid7's director of vulnerability intelligence, Douglas McKee, told The Hacker News that "More recently, INC Ransomware has emerged as the dominant threat actor actively weaponizing this vulnerability chain", and that the technical correlation with the pre-disclosure cluster "indicates that a single threat actor or coordinated group is responsible for discovering and exploiting this zero-day vulnerability" ([The Hacker News, 2026-08-03](https://thehackernews.com/2026/08/inc-ransomware-emerges-as-dominant.html)). Two limits belong with that quote. Rapid7 attributed this activity to INC Ransom on 2026-07-17, hours before this pipeline's 2026-07-18 entry, which did not carry it ([Dark Reading, 2026-07-17](https://www.darkreading.com/vulnerabilities-threats/inc-ransomware-exploits-sonicwall-sma-zero-days)) — so the actor link is seventeen days old and the new element is only the *dominance* characterisation. And the overlap claim is Rapid7's alone: Volexity, which named the UTA0533 cluster, has published no INC link, so the wider framing that both firms made that connection is not supported.

**A patch you applied is not necessarily a patch that is running.** This is the finding with the most operational consequence, and no prior entry here has carried it. Rapid7's director of incident response, Brett Deroche, describes containment succeeding in most engagements but not all: "We observed the threat actor maintaining persistence and rolling the newly applied patch back to a vulnerable state to maintain access. A comprehensive forensic review of the firewall is required to ensure complete eviction." A root-level attacker resident on the appliance can undo remediation, which means the standard verification — check the version, close the ticket — reports success on a box that is still owned. Resecurity's DFIR work reaches the same conclusion from the artifact side: "Setuid binaries, Python injectors, modified init scripts, and NGINX Unit configuration changes can survive reboots and may persist after a superficial firmware upgrade if not remediated. A patched appliance that still contains ROOTRUN or KNUCKLEBALL remains compromised" ([Resecurity, 2026-08-01](https://www.resecurity.com/blog/article/from-wsproxy-to-root-inc-ransomware-and-sonicwall-sma-exploit-chain)).

**The rotation scope is wider than passwords and MFA seeds.** Rapid7 reports that the attacks used the appliance foothold to extract high-value credentials, active session databases and TOTP multi-factor-authentication seed configurations ([The Hacker News, 2026-08-03](https://thehackernews.com/2026/08/inc-ransomware-emerges-as-dominant.html)) — stolen session state and MFA seeds keep working after a password reset, which is why the rotation list matters more than it looks. The earlier entry told readers to reset account passwords and TOTP seeds. Resecurity's list of what the appliance processed or stored, and therefore what has to be replaced, extends to SMA administrator passwords, directory-service bind credentials for LDAP, RADIUS and Active Directory, user passwords for every account that authenticated during the exposure window, certificates and API keys configured on the appliance, and TOTP tokens and seeds. Bind credentials are the item most often missed, and they are the ones that grant standing directory access independent of the appliance. Where compromise is confirmed, Resecurity's guidance is to factory-reset, reimage on patched firmware and restore configuration from a backup pre-dating the vulnerable branches — a constraint SonicWall states independently in its own product notice, which limits usable backups to those predating 12.4.3-03245 and 12.5.0-02283 ([SonicWall, 2026-07-14](https://www.sonicwall.com/support/notices/product-notice-sma-1000-series-affected-by-multiple-vulnerabilities/kA1VN000001nv6D0AQ)).

**A new pressure layer at the extortion stage.** Resecurity, which has run incident response for several victims, reports that "many of the new victims received emails, as well as phone calls from unknown organizations claiming to assist with ransomware issues", using infrastructure registered shortly after the intrusion. Whether this is the same operation or opportunists reading the leak site, the effect is the same: inbound offers of help with a ransomware problem the organisation has not made public are adversary contact, and the people receiving them are often outside the security team.

**On victim geography, hold the claim loosely.** Resecurity reports that INC's leak-site listings between 2026-07-17 and 2026-08-01 "include private sector and government organizations from Australia, the US, UAE, Colombia, Switzerland, and other countries", and SecurityWeek relays that INC "has emerged as the most active one" among actors chaining the two CVEs ([SecurityWeek, 2026-08-03](https://www.securityweek.com/recent-sonicwall-vulnerabilities-exploited-in-ransomware-attacks/)). No organisation is named, no victim or authority has confirmed any listing, and Resecurity does not state that any individual listing was reached through this exploit chain — the country list and the chain are separate claims in the same report. Treat it as an unverified criminal claim rather than evidence of a Swiss compromise.

**Defender takeaway:** if you remediated an SMA 1000 in July, the job is not closed. Re-verify the running firmware version rather than trusting the change record, complete the rotation across bind credentials, certificates and API keys as well as user passwords and MFA seeds, and — where the appliance was exposed before the hotfix — treat forensic review, not version checking, as the eviction test. **Triage:** the discriminator for the rollback behaviour is a firmware version that moves *backwards*, or an appliance whose reported version stops matching the deployment record, with no change ticket behind it; benign downgrades happen but they are planned, logged and attributable to an administrator. On the appliance itself the persistence artifacts are the durable signal: an unexpected setuid ELF binary, a loader module in the Python site-packages tree, modifications to the workplace init script, and unexpected proxy routes in the appliance's own NGINX Unit configuration pointing at a loopback backend port. Hunt the route entry rather than a fixed URL, and forward appliance logs off-box, because a root-level attacker edits local ones. Where directory traffic still runs unencrypted, moving LDAP and RADIUS to encrypted transports removes the cleartext-credential harvest this actor performs with on-appliance packet capture.
