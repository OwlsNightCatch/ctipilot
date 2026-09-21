---
schema: 1
kind: threat
title: "A conference-targeted phishing chain installs a self-regenerating rogue root CA plus a hosts-file/firewall local proxy that fabricates clean HTTPS results for any domain, surviving reboot"
headline: "Huntress: a fake Lenovo driver installs a working, private certificate authority into a victim's own trust store to fake 'clean' HTTPS results at will"
summary: >
  A Huntress researcher was targeted post-conference by a fake CoinDesk executive persona over a
  compromised Google Doc carrying a zero-click reconnaissance sidebar, three abused stolen
  code-signing certificates, and — the most novel component — a payload that hollows MsBuild.exe,
  generates its own self-signed certificate authority impersonating Google Trust Services, installs it
  into the system root store, and adds a hosts-file entry plus a firewall rule so a local proxy answers
  HTTPS connections to any chosen domain with fabricated "clean" results and no certificate warning.
discovered_at: "2026-09-21T04:45:00Z"
updated_at: null
event_date: "2026-08-19"
run_id: 2026-09-21T0410Z-intel
priority: high
immediate_action: null
tags:
  - infostealer
  - cryptocrime
  - identity
regions:
  - global
sectors: []
entities: []
techniques:
  - T1566.003
  - T1204.002
  - T1204.004
  - T1027.010
  - T1059.001
  - T1553.002
  - T1553.004
  - T1219
  - T1546.015
  - T1102.002
  - T1071.001
  - T1518
  - T1557
affected_products: ["Google Docs / Apps Script", "Microsoft Windows", "macOS", "NetSupport Manager"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/defcon-phishing-google-doc-malware"
    publisher: "Huntress Labs"
    date: "2026-08-19"
    role: primary
  - url: "https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows"
    publisher: "Huntress Labs"
    date: "2026-09-15"
    role: corroborating
closed_sources: []
evidence:
  - quote: "VIEW is the one worth sitting with. Opening the document while signed in, clicking nothing, and downloading nothing, was enough to report the viewer's IP address, location, browser, and whether they were running a crypto wallet extension."
    publisher: "Huntress Labs"
    source_url: "https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows"
  - quote: "It hollowed MsBuild.exe and imported only kernel32, ultimately establishing what Jon called \"purpose-built and working public key infrastructure on your machine.\""
    publisher: "Huntress Labs"
    source_url: "https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows"
  - quote: "Because the CA was regenerated per host, blocking a single certificate thumbprint does nothing."
    publisher: "Huntress Labs"
    source_url: "https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows"
verification: single-source
sourcing_note: >
  Huntress Labs is the sole publisher. This entry was surfaced by Huntress's 2026-09-15
  "Tradecraft Tuesday" webinar recap, which links to Huntress's own fuller technical write-up published
  2026-08-19 — 33 days earlier, by the same research team, under the same disclosure — as "full technical
  details"; this entry cites and is fact-checked against that fuller original as its primary, with the
  recap kept as corroborating for the spoken quotes it alone carries. The two pieces diverge on one
  forensic detail (the NetSupport Manager payload's persistence mechanism): this entry follows the fuller,
  more rigorous technical write-up rather than the recap's looser spoken paraphrase. The researcher
  declines attribution beyond noting Russian-language comments in the tooling as suggestive, not
  conclusive, of a Russian-speaking operator, and this entry carries no attribution accordingly.
confidence: high
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

A Huntress researcher was targeted after DEFCON by an X account impersonating a CoinDesk marketing executive, who sent a legitimate Google Doc carrying a custom Google Apps Script sidebar ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware)). The sidebar runs client-side with no OAuth consent prompt; per Huntress's own recap of the incident, merely opening the document while signed in — no click, no download — was enough for it to silently report the viewer's public IP address, geolocation, browser, and whether a MetaMask, Phantom, Tron or Solana wallet extension was installed, beaconing every action through the Telegram Bot API ([Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)) — a reconnaissance and victim-qualification step requiring no interaction at all. A fake "decryption failure" overlay then delivered OS-specific ClickFix remediation instructions, each offering a choice between pasting a clipboard command or downloading a file manually. On macOS, the pasted command launched a piped zsh chain that never actually delivered a payload in Huntress's own testing — the fetched URL looped through repeated redirects until the browser gave up, so the actor's evident intent for that path went unconfirmed; the manual-download option instead led to a disk image bundling its own Gatekeeper-bypass instructions and password prompt, and running it delivered a confirmed AMOS-family stealer harvesting browser, crypto-wallet, Telegram, Apple Notes, cookie and login-keychain data, plus a LaunchDaemon-installed backdoor capable of arbitrary remote commands and of turning the host into a SOCKS5 proxy. On Windows, pasting the ClickFix command launched an encoded PowerShell command that fetched a loader which pulled down three further payloads; by the time Huntress analyzed the kit all three had already gone offline, and their existence is known only because copies had reached VirusTotal — no certificate or further technical detail on this particular set was recoverable. Windows victims who instead chose the manual download were led down an entirely separate route: the same fake decryption-failure message told them to update a "Google API Connector," an application signed with a certificate belonging to a small Norwegian company (either stolen or fraudulently issued) that deployed via abuse of Microsoft's ClickOnce feature — the first of the three stolen code-signing certificates Huntress recovered across the whole campaign.

In a later message, the same actor sent a second document link, this time via DropBox DocSend, that routed macOS victims to another host serving the same AMOS payload and told Windows victims to install a DocSend-branded desktop installer signed with a second stolen certificate, from Discord Inc., whose signature did not validate ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware)). That installer's own DocSend flow was itself a non-functional distraction — a five-screen fake onboarding carousel using genuine Dropbox marketing pages that installed nothing. Per Huntress's own recap, the firm reconstructed the sample's own command-and-control registration protocol from its bundled `@sentry/electron` module and queried the live infrastructure directly ([Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)), recovering three payload archives this way: `Manager.zip` (NetSupport Manager), `Localcertificate.zip` (a TLS-intercepting local proxy) and `asusdriverld.zip` (a Ledger-wallet implant) — each downloaded encrypted, launched detached and hidden, then relaunched twenty seconds later with an elevation request. The first, NetSupport Manager — a legitimate remote-monitoring tool reconfigured to redirect data to attacker infrastructure and disable its own chat/connect/disconnect alerts — carries persistence for all three payloads: a kernel-mode keyboard-filter driver, a Windows service, a Winlogon modification and its own registered COM object ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware)). The third, the Ledger-wallet implant, reuses the second payload's disguise and technique.

The most novel component is that second payload, the TLS-intercepting local proxy itself: disguised as a Lenovo driver package and signed with a genuine stolen Lenovo certificate — the third of the three abused code-signing certificates, after the Norwegian and Discord ones — it hollows `MsBuild.exe` and generates its own self-signed certificate authority presenting itself as "Google Trust Services CN=WR3" plus a fabricated `www.virustotal.com` leaf certificate, installs that CA into the system root store, adds a hosts-file entry and a local-proxy firewall rule, and thereby locally answers HTTPS connections with fabricated "clean" results and no certificate warning for any domain the operator chooses — crypto-wallet sites, antivirus update checks, or anything else ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware)). Because the certificate authority is regenerated per infected host, blocking a specific certificate thumbprint achieves nothing. The interception process itself dies at reboot, but the installed root CA, the hosts-file entry and the firewall rule all persist across reboots untouched.

**Defender takeaway:** hunt for unexpected certificate authorities in the Windows or macOS system trust store claiming to be a major public CA (Google Trust Services, DigiCert, and similar) that were not provisioned by your own PKI or MDM — a rogue self-signed CA sitting in the trust store is the persistence artifact this technique leaves behind even after the active interception process is gone. Cross-reference unexplained hosts-file entries and orphaned local-proxy firewall rules against known-good baselines rather than certificate thumbprints, since the CA regenerates per host. Any organization whose staff attend security conferences should treat unsolicited, previously-unknown-contact Google Docs carrying custom Apps Script sidebars as a live reconnaissance vector requiring no click at all.

**Triage:** a locally-installed root CA is not automatically malicious — some legitimate enterprise MDM and TLS-inspection proxies do this deliberately. The discriminator is provenance: a root CA your own PKI/MDM inventory does not recognize as provisioned by it, especially one impersonating a well-known public CA's name, is the signal; one your MDM issued is not.
