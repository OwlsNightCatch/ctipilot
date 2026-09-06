---
schema: 1
kind: incident
title: "Rhysida claims Stuttgart municipal-data theft for 5 BTC; city denies a confirmed incident"
headline: "Rhysida claims Stuttgart municipal-data theft for 5 BTC; city denies a confirmed incident"
summary: "The Rhysida ransomware-as-a-service group listed Landeshauptstadt Stuttgart — the Baden-Württemberg state capital (~600,000 residents) — on its dark-web leak site in mid-May 2026 (DeXpose dates the listing to 2026-05-19; Heise (2026-05-21) covers the leak-site listing and Stuttgart's response without anchoring the …"
discovered_at: "2026-05-23T05:00:04Z"
event_date: 2026-05-21
run_id: 2026-05-23-852c21c8
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
  - organized-crime
regions:
  - europe
  - dach
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.heise.de/en/news/Cyber-gang-Rhysida-claims-data-theft-from-Stuttgart-city-11301876.html"
    publisher: Heise Online (EN)
    role: primary
  - url: "https://www.dexpose.io/rhysida-ransomware-targets-landeshauptstadt-stuttgart/"
    publisher: DeXpose
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
migrated_from: briefs/2026-05-23.md
---

The Rhysida ransomware-as-a-service group listed **Landeshauptstadt Stuttgart** — the Baden-Württemberg state capital (~600,000 residents) — on its dark-web leak site in mid-May 2026 (DeXpose dates the listing to 2026-05-19; Heise (2026-05-21) covers the leak-site listing and Stuttgart's response without anchoring the original posting date), demanding 5 Bitcoin (~€333,000) for exclusive access to allegedly stolen documents and publishing heavily downscaled previews of scanned invoices and faxes attributed to Stuttgart's administrative systems ([Heise Online (EN), 2026-05-21](https://www.heise.de/en/news/Cyber-gang-Rhysida-claims-data-theft-from-Stuttgart-city-11301876.html) · [DeXpose, 2026-05-20](https://www.dexpose.io/rhysida-ransomware-targets-landeshauptstadt-stuttgart/)). The city's response is measured: published material is "currently being examined together with the responsible authorities" and Stuttgart has "no indications of a cyber incident at this time", with further comment declined while investigation continues. No vulnerability or initial access vector has been disclosed; the claim appears to be data-exfiltration-only with city portals and operational systems unaffected, consistent with Rhysida's pattern since the British Library (2023) and the German charity Welthungerhilfe (2025).

Defender vantage with the city's denial in mind: confidence in the claim is **MEDIUM** — the only corroboration is press coverage of the leak-site listing itself. Hunt rather than respond: Rhysida tends to gain initial access through phishing (T1566) or external VPN exploitation (T1133), executes living-off-the-land via `cmd.exe` / PowerShell with scheduled-task persistence, and stages data in unusual directories before exfiltration (T1074.001). DACH municipal SOCs should treat the listing as a forcing function to re-check VPN patch levels, password-spray detection on the on-prem identity edge, and any unexplained outbound bursts from file servers and DFS shares since 2026-05-10. South Korean researchers' 2024 free Rhysida decryptor exploited an encryption flaw that the group has since reworked; no current decryptor is publicly known for 2026 variants if encryption does follow.

**Why it matters to us:** German municipal targeting bleeds into Swiss DACH context (shared partner networks, fediplomatic exchanges); the Stuttgart pattern — data theft only, leak-site posting, city denies — is increasingly common and the right response is hunt-without-confirming, not wait-for-a-victim-statement.
