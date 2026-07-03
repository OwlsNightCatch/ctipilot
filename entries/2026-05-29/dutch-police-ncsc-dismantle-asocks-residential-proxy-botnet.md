---
schema: 1
kind: threat
horizon: operational
title: "Dutch Police + NCSC dismantle Asocks residential-proxy botnet (~17 M devices, 200 NL-hosted servers seized)"
headline: "Dutch Police + NCSC dismantle Asocks residential-proxy botnet (~17 M devices, 200 NL-hosted servers seized)"
summary: "Dutch Police and NCSC seize 200 servers and dismantle the Asocks residential-proxy botnet (~17 million enrolled devices, NL-hosted C2). Asocks joins the recent string of disrupted residential-proxy networks — SocksEscort, Aisuru/Kimwolf, FirstVPN, IPIDEA, RapperBot — and defenders relying on Asocks exit-node blocklists should re-tune residential-proxy correlation rules now that the network is offline."
discovered_at: "2026-05-29T05:00:04Z"
event_date: null
run_id: 2026-05-29-c7f56b00
priority: high
immediate_action: null
tags:
  - law-enforcement
  - botnet
  - organized-crime
  - eu-nexus
regions:
  - europe
  - global
sectors:
  - public-sector
  - finance
  - telco
entities:
  - "campaign:dutch-police-ncsc-asocks-residential-proxy-takedown"
cves: []
sources:
  - url: "https://www.politie.nl/nieuws/2026/mei/28/06-politie-en-ncsc-halen-groot-botnetwerk-offline.html"
    publisher: Politie.nl — Politie en NCSC halen groot botnetwerk offline
    role: primary
  - url: "https://nltimes.nl/2026/05/28/ncsc-dutch-police-disrupt-global-botnet-controlled-via-netherlands-based-servers"
    publisher: NL Times
    role: corroborating
  - url: "https://news.risky.biz/risky-bulletin-dutch-police-take-down-giant-botnet-of-17-million-devices/"
    publisher: Risky Business News
    role: corroborating
closed_sources: []
evidence:
  - quote: "The Cybercrime Team of the Police Unit The Hague, together with the National Cyber Security Centre (NCSC), successfully dismantled a large Asocks botnet made up of at least 17 million compromised consumer devices around the world."
    publisher: NL Times citing Dutch Police and NCSC official statements
  - quote: "Investigators identified 200 servers used to run the infrastructure, all of which were physically based in the Netherlands."
    publisher: NL Times
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
migrated_from: briefs/2026-05-29.md
---

On 2026-05-28 the [Cybercrime Team of the Dutch Politie Unit The Hague and the NCSC.nl jointly took down the Asocks residential-proxy infrastructure](https://www.politie.nl/nieuws/2026/mei/28/06-politie-en-ncsc-halen-groot-botnetwerk-offline.html). Investigators identified and seized 200 control servers physically hosted at a Netherlands-based provider; the operation was triggered by a security-researcher tip routed through NCSC.nl to Politie ([NL Times English summary](https://nltimes.nl/2026/05/28/ncsc-dutch-police-disrupt-global-botnet-controlled-via-netherlands-based-servers); [Risky Business News bulletin](https://news.risky.biz/risky-bulletin-dutch-police-take-down-giant-botnet-of-17-million-devices/)). The Asocks network covertly enrolled victim devices — computers, routers, tablets, smartphones, IoT — using malware tied to the PROXYLIB Go-based library and rented bandwidth to criminal customers for spam, phishing, credential-stuffing and DDoS. Reported total: ~17 million enrolled endpoints globally. Residential-proxy services like Asocks are the standard infrastructure layer behind source-IP-anonymised credential stuffing, account takeover and consent-grant phishing against public-facing login portals and VPN concentrators.

**Defender takeaway:** for a few weeks expect a measurable drop in Asocks-sourced traffic; per the Risky Bulletin write-up, Asocks joins a list of previously-disrupted residential-proxy networks (SocksEscort, Aisuru/Kimwolf, FirstVPN, IPIDEA, RapperBot), and operator migration to whichever survivors absorb the displaced demand will lag the takedown. Re-validate any blocklists keyed on Asocks exit-node ranges and retune residential-IP-burst detections (CGNAT, consumer-ISP RDNS) on M365 / Entra ID / VPN sign-in logs.
