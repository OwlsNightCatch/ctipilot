---
schema: 1
kind: incident
title: "TeamUpdraft breach: stolen UpdraftCentral connection keys are used to push backdoor plugins to connected WordPress sites, with no flaw in UpdraftPlus and no CVE; deleting the keys is the fix"
headline: "Stolen UpdraftCentral keys install backdoor plugins on WordPress sites; the plugin update alone does not evict them"
summary: >
  TeamUpdraft, the vendor of the UpdraftPlus backup plugin, says unauthorised access to teamupdraft.com on 17 and 18 October probably
  exposed its customer database, including UpdraftCentral connection keys, and Patchstack and Nethemba report an attacker using those keys
  to install backdoor plugins on connected WordPress sites, which Patchstack's telemetry dates from 2026-10-18 15:32 (it gives no time zone), and that create hidden administrators. It is not
  a flaw in UpdraftPlus: the plugin obeys commands signed with a valid key, a key exists on many sites that never used the service
  because connecting a teamupdraft.com account ticks the option by default, and the update disconnects only connections made before 13:07 BST (12:07 UTC) on 18 October, so
  keys created later that day have to be deleted by hand. TeamUpdraft says the attacker used a compromised key to enter its own site, and
  Nethemba saw the stolen keys used again on 2026-10-21, after 1.26.13 shipped.
discovered_at: "2026-10-21T03:45:00Z"
updated_at: "2026-10-24T03:42:07Z"
event_date: "2026-10-18"
run_id: 2026-10-21T0256Z-intel
priority: high
immediate_action: null
tags: [supply-chain, data-breach]
regions: [global]
sectors: []
entities: ["incident:teamupdraft-updraftcentral-key-theft-2026-10", "product:wordpress"]
techniques: [T1199, T1078, T1505, T1136.001, T1098]
affected_products: ["UpdraftPlus", "UpdraftCentral", "WordPress"]
cves: []
sources:
  - url: "https://teamupdraft.com/blog/security-incident-october-2026/"
    publisher: "TeamUpdraft (post updated 2026-10-23)"
    date: "2026-10-19"
    role: primary
  - url: "https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/"
    publisher: "Patchstack"
    date: "2026-10-19"
    role: primary
  - url: "https://nethemba.com/updraftcentral-backdoor-analysis/"
    publisher: "Nethemba (living post, updated to 2026-10-23)"
    date: "2026-10-19"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/stolen-updraftcentral-keys-used-to-backdoor-wordpress-sites/"
    publisher: "BleepingComputer"
    date: "2026-10-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Over the weekend of 17-18 October we identified unauthorised access to the teamupdraft.com website."
    publisher: "TeamUpdraft (post updated 2026-10-23)"
    source_url: "https://teamupdraft.com/blog/security-incident-october-2026/"
  - quote: "We believe our customer database was accessed."
    publisher: "TeamUpdraft (post updated 2026-10-23)"
    source_url: "https://teamupdraft.com/blog/security-incident-october-2026/"
  - quote: "An attacker holding valid UpdraftCentral dashboard keys is installing backdoor plugins on connected WordPress sites."
    publisher: "Patchstack"
    source_url: "https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/"
  - quote: "This is not a vulnerability in UpdraftPlus"
    publisher: "Patchstack"
    source_url: "https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/"
  - quote: "Connecting a TeamUpdraft.com account is the other, and it happens by default."
    publisher: "Patchstack"
    source_url: "https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/"
  - quote: "Even 1.26.13 does not delete keys created on 18 October between 12:07 and 21:00 UTC"
    publisher: "Nethemba (living post, updated to 2026-10-23)"
    source_url: "https://nethemba.com/updraftcentral-backdoor-analysis/"
  - quote: "We know the attacker used a compromised key to access our site."
    publisher: "TeamUpdraft (post updated 2026-10-23)"
    source_url: "https://teamupdraft.com/blog/security-incident-october-2026/"
  - quote: "So the attacker keeps using the leaked keys."
    publisher: "Nethemba (living post, updated to 2026-10-23)"
    source_url: "https://nethemba.com/updraftcentral-backdoor-analysis/"
verification: multi-source
sourcing_note: >
  TeamUpdraft is the victim and describes its own breach and fix; Patchstack and Nethemba observed the attack on their own and
  their customers' sites, and Patchstack builds on Nethemba's first analysis. The vendor says its 1.26.13 and 2.26.13 update disconnects every connection made before 13:07 BST on 18 October, and Nethemba reads
  from the code that 1.26.12 and 2.26.12 deleted none and that 1.26.13 spares keys created on 18 October between 12:07 and 21:00 UTC;
  the roughly 400,000 sites figure is an upper bound that rests on a vendor estimate made for the June flaw. TeamUpdraft's statement that the attacker used a compromised key to enter its site, and its suspicion that AI accelerated the attack, are the vendor's own and come with no evidence; Nethemba's report of attacker commands after 1.26.13 and its reading of how UpdraftPlus Premium stores the account password come from its own sites and its review of the code, and it has not seen the pushed plugins read that password.
confidence: high
references:
  - "2026-06-14/cve-2026-10795-updraftplus-wordpress-backup-plugin-unauthent"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "On every WordPress site your organisation, its web agencies or its hosting suppliers run with UpdraftPlus, free or premium, including old municipal, campaign and project sites, check for an UpdraftCentral key (wp option get updraft_central_localkeys, or Settings > UpdraftPlus Backups > Advanced Tools > UpdraftCentral) and delete every key even if nobody remembers using UpdraftCentral, then update to 1.26.13 or 2.26.13 or later; deleting a key stops remote management only, and backups keep working."
  - "On any site where a plugin, must-use plugin or Editor account holding manage_options appears that nobody created, delete the UpdraftCentral key first, then restore the site from a backup taken before 17 October, rotate every administrator and UpdraftCentral password, the teamupdraft.com account password (which UpdraftPlus Premium can leave stored in the site database and its backups) and end all sessions."
updates:
  - at: "2026-10-24T03:42:07Z"
    run_id: 2026-10-24T0255Z-intel
    type: update
    summary: >
      TeamUpdraft says the attacker entered its site with a compromised key and suspects AI-accelerated
      tooling, and asks users to check the sites listed in their UpdraftCentral account; Nethemba saw the
      stolen keys used again on 2026-10-21 after 1.26.13 shipped and reads UpdraftPlus Premium as leaving
      the account password stored in the site database and backups.
    fields: [actions, body, evidence, sources, sourcing_note, summary]
migrated_from: null
---

TeamUpdraft says unauthorised access to teamupdraft.com on 17 and 18 October and that it believes its customer database was accessed, which holds connection keys for UpdraftCentral, UpdraftVault and UpdraftClone; it says UpdraftPlus plugin files and downloads were not affected, that the attacker used a compromised key to access its site, and that there is no evidence the attacker still has access, and it suspects, without giving evidence, that the attacker used AI to accelerate the attack ([TeamUpdraft, 2026-10-19](https://teamupdraft.com/blog/security-incident-october-2026/)). Patchstack reports that an attacker holding valid UpdraftCentral dashboard keys has been installing backdoor plugins on connected WordPress sites since 2026-10-18 at 15:32 (the page gives no time zone), and that this is not a vulnerability in UpdraftPlus: the UpdraftCentral client ships inside every copy of the plugin and executes any command signed with the dashboard's private key once the site holds a key ([Patchstack, 2026-10-19](https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/); [BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/stolen-updraftcentral-keys-used-to-backdoor-wordpress-sites/)).

The attacker sends a signed plugin.upload_plugin command as an ordinary POST to the site root and WordPress installs and activates the plugin; each delivered plugin wakes on a secret URL parameter carrying a 32-character token, creates an account with a hardcoded password, gives it the Editor role and then the manage_options and install_plugins capabilities, and logs the visitor in with a cookie, which bypasses the login form, two-factor authentication and login-protection plugins ([Patchstack, 2026-10-19](https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/)). The account stays after the plugin is removed, and early samples crash the site with an HTTP 500 and must not be repaired, because fixing the error switches the backdoor on ([Patchstack, 2026-10-19](https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/)). Nethemba adds a variant that logs the attacker in as an existing administrator without a database trace ([Nethemba, 2026-10-19](https://nethemba.com/updraftcentral-backdoor-analysis/)).

A site holds a key if it was connected to UpdraftCentral or if a teamupdraft.com account was logged in from the plugin, where the option to add the site to UpdraftCentral is ticked by default, and keys do not expire ([Patchstack, 2026-10-19](https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/)); on UpdraftPlus 1.26.4 or 2.26.4 and earlier an attacker needs no key at all, through CVE-2026-10795, fixed in 1.26.5 and 2.26.5 ([Patchstack, 2026-10-19](https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/)). BleepingComputer reports an estimate of up to about 400,000 sites ([BleepingComputer, 2026-10-20](https://www.bleepingcomputer.com/news/security/stolen-updraftcentral-keys-used-to-backdoor-wordpress-sites/); [Nethemba, 2026-10-19](https://nethemba.com/updraftcentral-backdoor-analysis/)). TeamUpdraft says UpdraftPlus 1.26.13 and 2.26.13 disconnect every UpdraftCentral connection made before 13:07 BST (12:07 UTC) on 18 October; Nethemba says 1.26.12 and 2.26.12 deleted none and that 1.26.13 does not delete keys created on 18 October between 12:07 and 21:00 UTC, which have to be deleted by hand ([TeamUpdraft, 2026-10-19](https://teamupdraft.com/blog/security-incident-october-2026/); [Nethemba, 2026-10-19](https://nethemba.com/updraftcentral-backdoor-analysis/)). Nethemba saw the attacker send UpdraftCentral commands to two of its sites on the morning of 2026-10-21, after 1.26.13 had shipped, blocked by Nethemba's own blocking plugin, with the keys already deleted, and says sites that neither run 1.26.13 or 2.26.13 nor have deleted the key by hand remain at risk ([Nethemba, 2026-10-19](https://nethemba.com/updraftcentral-backdoor-analysis/)).

**Exposure:** a WordPress site running UpdraftPlus, free or premium, that holds an UpdraftCentral key; `wp option get updraft_central_localkeys` prints it, including on sites whose owners never used UpdraftCentral ([Patchstack, 2026-10-19](https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/)). Self-hosted UpdraftCentral is not affected ([TeamUpdraft, 2026-10-19](https://teamupdraft.com/blog/security-incident-october-2026/)).

**Detection:** web server access logs for POST requests to the site root carrying an UpdraftCentral command whose user agent lacks the library version and URL that genuine dashboard traffic carries, and for GET requests with a short underscore-prefixed parameter and a 32-character token, which mean a backdoor was used; the UpdraftCentral log on the site for plugin.upload_plugin and plugin.delete_plugin commands without a matching administrator action; the plugin and must-use plugin directories on disk; and the user table for an Editor that also holds manage_options ([Patchstack, 2026-10-19](https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/); [Nethemba, 2026-10-19](https://nethemba.com/updraftcentral-backdoor-analysis/)). TeamUpdraft asks users to look at the sites listed under their UpdraftCentral account for any they did not knowingly connect since 2026-10-19 and says it is seeing a pattern of unexpected Editor roles ([TeamUpdraft, 2026-10-19](https://teamupdraft.com/blog/security-incident-october-2026/)). The backdoor account stays after the plugin is removed ([Patchstack, 2026-10-19](https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/)).

**Defender takeaway:** delete the UpdraftCentral key on every site first, then update; if a backdoor is found, delete the key before removing it or the attacker pushes a replacement, and treat the site as compromised ([Patchstack, 2026-10-19](https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/)). IP blocking is not a control, since Patchstack saw the source addresses rotate within a day ([Patchstack, 2026-10-19](https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/)). On UpdraftPlus Premium sites Nethemba reads the code as leaving the teamupdraft.com account password stored in the database, and so in backups, until add-ons are claimed with a token, although the vendor says it is removed after the first connection, a reader found it on all three of their premium sites and in backups going back to 2022, and Nethemba has not found the samples it analysed reading it; changing that account password is therefore part of the cleanup ([Nethemba, 2026-10-19](https://nethemba.com/updraftcentral-backdoor-analysis/)).

## Update — 2026-10-24T03:42:07Z

TeamUpdraft's updates of 2026-10-21 and 2026-10-22 say the attacker used a compromised key to access its site, that there is no evidence the attacker still has access, and that the speed of the exploits and the initially faulty backdoor plugins suggest AI was used to accelerate the attack, which is the vendor's inference and comes with no evidence ([TeamUpdraft, 2026-10-19](https://teamupdraft.com/blog/security-incident-october-2026/)). It asks users to look at the sites listed under their UpdraftCentral account for any they did not knowingly connect since 2026-10-19, says it is seeing a pattern of unexpected Editor roles, and stresses that UpdraftPlus Premium users should check for unexpected plugins and new administrators even if they never used UpdraftCentral ([TeamUpdraft, 2026-10-19](https://teamupdraft.com/blog/security-incident-october-2026/)).

Nethemba reports that the attacker kept going after the fix: on 2026-10-20 it tried the secret triggers of already removed backdoors on at least six sites of four administrators, and on the morning of 2026-10-21 it sent UpdraftCentral commands to two of Nethemba's sites after 1.26.13 had been released, blocked by Nethemba's own blocking plugin, with the keys no longer existing ([Nethemba, 2026-10-19](https://nethemba.com/updraftcentral-backdoor-analysis/)). A site that has a stolen key and neither updated nor deleted it by hand therefore stays exposed, and a removed backdoor is still probed. Nethemba also reads the code of UpdraftPlus Premium as storing the teamupdraft.com account password in the site database as entered and deleting it only after add-ons are claimed with a token, so it can stay in the database and in backups; a reader found it on all three of their premium sites and in backups going back to 2022, and Nethemba on one of its three, while the vendor says it is removed after the first connection and Nethemba has not found the samples it analysed reading it ([Nethemba, 2026-10-19](https://nethemba.com/updraftcentral-backdoor-analysis/)).
