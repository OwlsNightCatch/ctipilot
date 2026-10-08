---
schema: 1
kind: threat
title: "A phishing link on Microsoft's own Power BI domain slips past mail filters and installs rogue ScreenConnect clients, then, in one incident, a script replaces the first remote-management tool with a second"
headline: "Huntress: a Power BI-hosted phishing link installs rogue ScreenConnect clients; in one case a script removed the first"
summary: >
  Huntress describes a phishing campaign seen since 2026-09-10 in which an Outlook email links to a fake
  reference document on a legitimate Power BI domain; a "Download Reference" button opens an attacker page that
  fingerprints the visitor and then downloads a ScreenConnect installer. The installer deploys a rogue
  ScreenConnect client that establishes a second one, and in one incident a PowerShell script removed the first;
  Huntress could not obtain the original email, and the configuration of one of the rogue clients also appeared on 22
  other endpoints.
discovered_at: "2026-10-08T04:53:00Z"
updated_at: null
event_date: "2026-10-07"
run_id: 2026-10-08T0404Z-intel
priority: notable
immediate_action: null
tags: [phishing]
regions: [global]
sectors: []
entities: ["product:connectwise-screenconnect", "product:microsoft-power-bi"]
techniques: [T1566.002, T1219, T1059.001, T1059.003, T1053.005, T1105]
affected_products: ["Microsoft Power BI", "ConnectWise ScreenConnect"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/screenconnect-power-bi"
    publisher: "Huntress"
    date: "2026-10-07"
    role: primary
closed_sources: []
evidence:
  - quote: "Because the link points to Microsoft's real Power BI domain, it skirts through Microsoft 365 mail filters and other security gateways that trust this domain."
    publisher: "Huntress"
  - quote: "the PowerShell script also resulted in the uninstallation of the first ScreenConnect instance, in a likely effort to evade detection"
    publisher: "Huntress"
verification: single-source
sourcing_note: >
  A single first-party source: Huntress reports its own incident telemetry and a retroactive hunt; no second
  source reports the campaign, and Huntress could not obtain the original email.
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

Huntress describes a phishing campaign it has seen since 2026-09-10 in which an Outlook email carries a link that leads to a fake reference document on a legitimate Power BI domain ([Huntress, 2026-10-07](https://www.huntress.com/blog/screenconnect-power-bi)). Huntress notes that threat actors have previously abused Power BI in this way, building a real dashboard under an account of their own (usually compromised or throwaway), embedding a malicious link and setting its sharing to public, and that because the link points to Microsoft's real domain it passes Microsoft 365 mail filters and other gateways that trust that domain; it does not say how this campaign's page was set up ([Huntress, 2026-10-07](https://www.huntress.com/blog/screenconnect-power-bi)). A "Download Reference" button opens a new tab on an attacker domain that fingerprints the visitor (operating system, browser, automation indicators, cloud-provider cookies), reports victims to a Telegram bot and redirects visitors who fail its checks; after a delay a script clicks a hidden download link for a ScreenConnect installer ([Huntress, 2026-10-07](https://www.huntress.com/blog/screenconnect-power-bi)).

The installer deploys a first rogue ScreenConnect client, which establishes a second one pointed at different infrastructure ([Huntress, 2026-10-07](https://www.huntress.com/blog/screenconnect-power-bi)). In one incident the first client ran a command-shell script that launched a PowerShell script from the temp directory; that script downloaded and ran the installer for the second client and uninstalled the first, in a likely effort to evade detection, and a scheduled task re-ran it every two minutes before the attack was shut down ([Huntress, 2026-10-07](https://www.huntress.com/blog/screenconnect-power-bi)). After deployment the clients also ran a tool Huntress assessed as designed to hide the attacker's activity from the user and security software ([Huntress, 2026-10-07](https://www.huntress.com/blog/screenconnect-power-bi)). A handful of endpoints were hit from 2026-09-10, and the configuration of one of the rogue clients also appeared on 22 other endpoints in separate incidents ([Huntress, 2026-10-07](https://www.huntress.com/blog/screenconnect-power-bi)). The original email and lure wording are unknown.

**Exposure:** Microsoft 365 mailboxes where links to Power BI view pages reach users, and Windows endpoints where a user can run an installer for a remote-management tool; no sector or region is stated ([Huntress, 2026-10-07](https://www.huntress.com/blog/screenconnect-power-bi)).

**Detection:** in web proxy or mail click logs, a click on a Power BI view link followed within seconds by a new tab on an unfamiliar domain and an executable download; in endpoint process telemetry, a ScreenConnect client installer started from a browser download, a client service connecting to a ScreenConnect instance that is not the organisation's own, that client spawning a command shell and PowerShell from a temp directory, a second remote-management client appearing as the first is removed, and a scheduled task that re-runs a script every two minutes ([Huntress, 2026-10-07](https://www.huntress.com/blog/screenconnect-power-bi)).

**Triage:** ScreenConnect is legitimate where the organisation runs it; the discriminators are an instance that is not the organisation's own and an installer that arrived through a browser download from a web page rather than through IT's deployment tooling ([Huntress, 2026-10-07](https://www.huntress.com/blog/screenconnect-power-bi)).

**Defender takeaway:** treat a link on a trusted cloud-hosted domain that leads to a download as untrusted in mail protection and user-reporting workflows, restrict remote-management software to approved instances, and check endpoints with more than one remote-management client, looking back to 2026-09-10 ([Huntress, 2026-10-07](https://www.huntress.com/blog/screenconnect-power-bi)).
