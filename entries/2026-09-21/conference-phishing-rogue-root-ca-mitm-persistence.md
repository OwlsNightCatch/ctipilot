---
schema: 1
kind: threat
title: "A conference-targeted phishing chain installs a rogue root CA generated fresh on every host, plus a hosts-file/firewall local proxy able to fake clean VirusTotal results and to mint trusted certificates for any domain, surviving reboot"
headline: "Huntress: a fake Lenovo driver installs a working, private certificate authority into a victim's own trust store, able to fake 'clean' VirusTotal lookups"
summary: >
  A Huntress researcher was targeted post-conference by a fake CoinDesk executive persona over a legitimate Google Doc carrying a zero-click reconnaissance sidebar, in a chain that abused three code-signing certificates. The most novel component is a payload that hollows MsBuild.exe,
  generates its own self-signed certificate authority impersonating Google Trust Services, installs it
  into the system root store, and adds a hosts-file entry plus a firewall rule so a local proxy can answer
  the machine's VirusTotal lookups over fully validating HTTPS with fabricated results. The CA's
  private key sits on disk, so a trusted certificate can be minted for any domain.
discovered_at: "2026-09-21T04:45:00Z"
updated_at: null
event_date: "2026-08-19"
run_id: 2026-09-21T0410Z-intel
priority: notable
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
  Huntress Labs is the sole publisher: its 2026-08-19 technical write-up is the primary, and its
  2026-09-15 webinar recap corroborates it and carries the spoken quotes. The two differ on the
  NetSupport Manager payload's persistence, where the fuller write-up is followed, and on which Windows
  path uses ClickOnce, which the text states as a contradiction. The researchers offer no attribution
  beyond Russian-language comments in the tooling.
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
updates:
  - at: "2026-09-27T13:28:04Z"
    run_id: 2026-09-27T1308Z-audit
    type: correction
    summary: >
      The gap between Huntress's fuller technical write-up of 2026-08-19 and the 2026-09-15 recap that
      surfaced this entry is 27 days, not the 33 days first stated. The two publication dates themselves
      were correct; only the interval computed from them was wrong, and no security-relevant claim in the
      entry depended on it.
    fields: [sourcing_note, body]
  - at: "2026-09-30T06:56:12Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Priority recalibrated from high to notable: a phishing tradecraft report
      without evidence of targeting Swiss public bodies. The sourcing note is rewritten as plain provenance. The any-domain interception is restated as capability
      rather than observed behavior (Huntress saw only VirusTotal targeted), the Windows delivery
      paths the two Huntress pieces label differently are stated as a contradiction, and payload
      archive file names are removed. The summary now calls the lure a legitimate Google Doc rather
      than a compromised one, and the title describes the CA as generated fresh on every host.
    fields: [priority, sourcing_note, body, title, headline, summary]
migrated_from: null
---

A Huntress researcher was targeted after DEFCON by an X account impersonating a CoinDesk marketing executive, who sent a legitimate Google Doc carrying a custom Google Apps Script sidebar ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware) · [Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)). The sidebar runs client-side with no OAuth consent prompt, and merely opening the document while signed in, with no click or download, was enough for it to report the viewer's public IP address, geolocation, browser and whether a MetaMask, Phantom, Tron or Solana wallet extension was installed, beaconing every action through the Telegram API ([Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)). A fake "decryption failure" overlay then delivered OS-specific ClickFix instructions, each offering a choice between pasting a command or downloading a file manually ([Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)). On macOS, the pasted command launched a piped zsh chain that never delivered a payload in Huntress's testing, because the fetched URL looped through redirects. The manual download led to a disk image bundling its own Gatekeeper-bypass instructions and password prompt, which delivered a confirmed AMOS-family stealer harvesting browser, crypto-wallet, Telegram, Apple Notes, cookie and login-keychain data, plus a LaunchDaemon-installed backdoor capable of arbitrary remote commands and of turning the host into a SOCKS5 proxy ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware) · [Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)). On Windows, one path launched an encoded PowerShell command that fetched a loader, which pulled down three further payloads that were offline by the time Huntress looked but already on VirusTotal ([Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)). The other told the victim to update a "Google API Connector", an application signed with a certificate belonging to a small Norwegian company (stolen or fraudulently issued) and deployed through Microsoft's ClickOnce feature, the first of three abused code-signing certificates in the campaign ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware) · [Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)).

**Contradiction:** Huntress's two pieces assign the Windows paths differently. The 2026-08-19 write-up says the update button launches the ClickOnce installer and the manual path shows ClickFix-style instructions with an encrypted PowerShell script ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware)). The 2026-09-15 recap assigns ClickOnce to the manual download and the encoded PowerShell command to the ClickFix lure ([Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)).

In a later message, the same actor sent a second document link, this time via DropBox DocSend, that routed macOS victims to another host serving the same AMOS payload and told Windows victims to install a DocSend-branded desktop installer signed with a second stolen certificate, from Discord Inc., whose signature did not validate ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware)). The installer's DocSend flow was a non-functional distraction: a five-screen fake onboarding carousel using genuine Dropbox marketing pages that installed nothing. Huntress reconstructed the sample's command-and-control registration protocol from its bundled `@sentry/electron` module and queried the live infrastructure of a sibling campaign directly ([Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)), recovering three payload archives this way: NetSupport Manager, a TLS-intercepting local proxy and a Ledger-wallet implant. Each was downloaded encrypted, launched detached and hidden, then relaunched twenty seconds later with an elevation request. The first, NetSupport Manager, is a legitimate remote-monitoring tool reconfigured to redirect data to attacker infrastructure and disable its own chat, connect and disconnect alerts, and it carries persistence for all three payloads: a kernel-mode keyboard-filter driver, a Windows service, a Winlogon modification and its own registered COM object ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware)). The third, the Ledger-wallet implant, reuses the second payload's disguise and technique.

The most novel component is that second payload, the TLS-intercepting local proxy. Disguised as a Lenovo driver package and signed with a genuine stolen Lenovo certificate, the third abused code-signing certificate, it hollows `MsBuild.exe`, generates its own self-signed certificate authority presenting itself as "Google Trust Services CN=WR3", issues a `www.virustotal.com` leaf certificate from it, installs the CA into the system root store, adds a hosts-file entry pointing `www.virustotal.com` at the local machine and creates a local-proxy firewall rule ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware)). VirusTotal lookups from the host then reach a local proxy that answers over fully validating HTTPS and can block them or return fabricated results. VirusTotal was the only target Huntress observed, but the CA's private key is written to disk, so a trusted certificate can be minted for any domain at will ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware)). A Huntress researcher named crypto-wallet domains and antivirus update signals as targets the operator could intercept the same way ([Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)). Because the certificate authority is regenerated per infected host, blocking a specific certificate thumbprint achieves nothing. The interception process dies at reboot, but the installed root CA, the hosts-file entry and the firewall rule persist ([Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)).

**Defender takeaway:** hunt for unexpected certificate authorities in the Windows or macOS system trust store claiming to be a major public CA (Google Trust Services, DigiCert, and similar) that were not provisioned by your own PKI or MDM. A rogue self-signed CA sitting in the trust store is the persistence artifact this technique leaves behind even after the active interception process is gone. Cross-reference unexplained hosts-file entries and orphaned local-proxy firewall rules against known-good baselines rather than certificate thumbprints, since the CA regenerates per host. Any organization whose staff attend security conferences should treat unsolicited, previously-unknown-contact Google Docs carrying custom Apps Script sidebars as a live reconnaissance vector requiring no click at all.

**Triage:** a locally-installed root CA is not automatically malicious, since some legitimate enterprise MDM and TLS-inspection proxies do this deliberately. The discriminator is provenance: a root CA your own PKI or MDM inventory does not recognize as provisioned by it, especially one impersonating a well-known public CA's name, is the signal; one your MDM issued is not.

## Correction — 2026-09-27T13:28:04Z

Huntress published its fuller technical write-up on 2026-08-19 and the webinar recap on 2026-09-15, an interval of 27 days rather than the 33 days first stated ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware); [Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)). Both publication dates, and every technical claim resting on them, are unchanged.

## Correction — 2026-09-30T06:56:12Z

Huntress describes the rogue certificate authority's use only against VirusTotal lookups, as a capability: the hosts-file entry redirects `www.virustotal.com` to the local proxy ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware)). Because the authority's private key sits on disk, a trusted certificate can be minted for any domain, and crypto-wallet sites and antivirus update checks are what a Huntress researcher said the operator could intercept, not observed targets ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware) · [Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)). Huntress's two pieces also assign the ClickOnce installer and the PowerShell command to different Windows paths ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware) · [Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)). The lure was a legitimate Google Doc carrying the attacker's custom Apps Script sidebar, not a compromised document ([Huntress Labs, 2026-09-15](https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)), and the certificate authority is generated fresh on every host ([Huntress Labs, 2026-08-19](https://www.huntress.com/blog/defcon-phishing-google-doc-malware)).
