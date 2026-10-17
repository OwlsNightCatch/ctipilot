---
schema: 1
kind: incident
title: "A self-registered account and an unrestricted upload turn a shared recreation-management platform into a webshell and card-data foothold, and the actor returns after cleanup"
headline: "Huntress: a member account plus an .aspx upload gave an attacker webshells on three servers and a hunt for card data"
summary: >
  Huntress observed from 2026-09-10 a threat actor compromising three web servers of a shared recreation-management
  platform by registering a member account and uploading .aspx webshells into the member-files directory, then
  searching for database credentials and cardholder data. After one server went back into production prematurely, the
  actor returned with the same account and planted a credential-harvesting script in the login page's jQuery file.
  Huntress names no vendor or CVE.
discovered_at: "2026-10-04T04:40:00Z"
updated_at: null
event_date: "2026-09-10"
run_id: 2026-10-04T0405Z-intel
priority: notable
immediate_action: null
tags: [data-breach]
regions: [global]
sectors: [public-sector]
entities: ["incident:recreation-platform-webshell-municipal-tenants-2026-09"]
techniques: [T1190, T1505.003, T1059.003, T1059.001, T1083, T1033, T1082, T1552.001, T1005, T1036.005, T1070.006, T1056.003]
affected_products: []
cves: []
sources:
  - url: "https://www.huntress.com/blog/parks-recreation-platform-webshell-attack"
    publisher: "Huntress"
    date: "2026-09-30"
    role: primary
closed_sources: []
evidence:
  - quote: "register a member account, upload a malicious file, and turn it into a webshell."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/parks-recreation-platform-webshell-attack"
  - quote: "When the third server was put back into production prematurely, the threat actor returned with a vengeance."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/parks-recreation-platform-webshell-attack"
  - quote: "creating their own account on the platform and finding a flaw in the upload function"
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/parks-recreation-platform-webshell-attack"
verification: single-source
sourcing_note: >
  One first-hand source: Huntress's SOC observations on three servers. Huntress does not name the platform vendor, a
  CVE or the affected organizations, and no independent report was found. The actor's likely location and the
  suggestion that some scripts were AI-generated are Huntress's own inferences.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Huntress observed on 2026-09-10 a threat actor compromising multiple tenants of a shared recreation-management platform with one repeatable method: "register a member account, upload a malicious file, and turn it into a webshell" ([Huntress, 2026-09-30](https://www.huntress.com/blog/parks-recreation-platform-webshell-attack)). Huntress's summary calls the three compromised web servers municipal and says the actor aimed to steal payment data; the post names neither the platform vendor nor a CVE. On the first server the actor spent roughly six hours on failed unauthenticated attempts (login brute force, IIS 8.3 tilde enumeration, WebDAV verbs, upload-handler bypasses, forced browsing); what worked was registering an account and uploading 14 files into the member-files directory, the .aspx ones as webshells ([Huntress, 2026-09-30](https://www.huntress.com/blog/parks-recreation-platform-webshell-attack)).

Through the webshells, run from the IIS worker process, the actor enumerated the host and IIS sites, read configuration files for connection strings and keys, connected to the database with the harvested SQL credentials, searched files for card data and read a payment gateway's plain-text webhook logs to extract card numbers, expiry dates and card verification codes ([Huntress, 2026-09-30](https://www.huntress.com/blog/parks-recreation-platform-webshell-attack)). On a third server it uploaded five webshells, copied them under names resembling site assets, set their timestamps to match web.config and probed the payment-module folders ([Huntress, 2026-09-30](https://www.huntress.com/blog/parks-recreation-platform-webshell-attack)).

When that server was put back into production prematurely, the actor returned with the same registered account, re-uploaded webshells and appended an obfuscated loader to a jQuery file that the authentication page loads, intending to turn every browser that loads the page into an encrypted command client that evaluates pushed code and harvests credentials in real time ([Huntress, 2026-09-30](https://www.huntress.com/blog/parks-recreation-platform-webshell-attack)). Huntress deduces from a Simplified Chinese locale in a PowerShell user-agent that the actor is most likely based in China, and says script comments suggest AI-generated code. It does not state how many cards were exposed or whether any data left the servers.

**Exposure:** any web platform that lets an anonymous visitor self-register and then upload files into a directory served by IIS with script execution enabled; with no vendor or CVE named, check whether a member upload directory accepts .aspx files and executes them ([Huntress, 2026-09-30](https://www.huntress.com/blog/parks-recreation-platform-webshell-attack)).

**Detection:** web and application telemetry first: a new member registration followed by uploads into the member-files directory, .aspx files appearing in an upload folder, and the IIS worker process spawning cmd.exe or powershell.exe for host and configuration discovery. Later signs are web-root files whose timestamps were copied from web.config, a static script asset loaded by the login page that differs from the deployed package, and PowerShell and JavaScript written to the Windows temp folder as base64 files and then decoded ([Huntress, 2026-09-30](https://www.huntress.com/blog/parks-recreation-platform-webshell-attack)).

**Triage:** legitimate member uploads of documents and images land in the same directory; the discriminator is a script-capable extension there, or a file there that is requested directly and then spawns child processes ([Huntress, 2026-09-30](https://www.huntress.com/blog/parks-recreation-platform-webshell-attack)).

**Defender takeaway:** review citizen-facing booking or payment portals that allow self-registration and upload for script execution in the upload directory, payment modules sharing a server with general tenants, and webhook logs holding card data in plain text on the web server. On a cleaned server, remove the actor's registered accounts, fix the upload handler and rotate the SQL credentials in readable configuration files before it returns to production; the actor came back with the same account ([Huntress, 2026-09-30](https://www.huntress.com/blog/parks-recreation-platform-webshell-attack)).
