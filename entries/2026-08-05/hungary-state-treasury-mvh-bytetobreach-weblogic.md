---
schema: 1
kind: incident
horizon: operational
title: "ByteToBreach hits Hungary's State Treasury after Romania's land registry — the reported entry point is an Oracle WebLogic server left unpatched since a 2017 patch cycle"
headline: "The actor who wiped Romania's cadastre reaches a second EU government body through legacy WebLogic"
summary: >
  Hungarian outlet Telex.hu reports that the Magyar Államkincstár (State Treasury), specifically its
  Agricultural and Rural Development Office (MVH), was breached in late July 2026 by ByteToBreach — the
  same self-described financially-motivated actor already tracked here for the July 2026 attack on
  Romania's ANCPI land registry. Per cybersecurity experts Telex.hu consulted on attacker-leaked
  screenshots, entry came through an unpatched Oracle WebLogic Server whose fixes date to an October
  2017 patch cycle, escalating to Windows domain-administrator rights across a reported 116 virtual
  machines, with ransomware encrypting employee workstation files. Treasury officials state citizen
  data was not affected; Hungary's National Cybersecurity Institute is investigating.
discovered_at: "2026-08-05T04:12:23Z"
event_date: "2026-08-03"
run_id: 2026-08-05T0412Z-intel
priority: high
immediate_action: null
tags: [data-breach, ransomware, organized-crime, vulnerabilities]
regions: [europe]
sectors: [public-sector, finance]
entities: [actor:bytetobreach, incident:hungary-treasury-mvh-bytetobreach-2026-08, incident:ancpi-romania-cyberattack-2026-07]
techniques: [T1190, T1078.002, T1486]
affected_products: ["Oracle WebLogic Server"]
cves: []
sources:
  - url: "https://telex.hu/techtud/2026/08/03/magyar-allamkincstar-nki-kiberbiztonsag-kibertamadas-naih-bytetobreach"
    publisher: "Telex.hu"
    date: "2026-08-03"
    role: primary
  - url: "https://news.risky.biz/risky-bulletin-hacker-breaches-hungarys-state-treasury/"
    publisher: "Risky Bulletin (Risky Business Media)"
    date: "2026-08-05"
    role: corroborating
  - url: "https://telex.hu/techtud/2026/08/02/magyar-allamkincstar-nemzeti-kifizeto-ugynokseg-kibertamadas-orosz-szerver-titkositott-allomanyok"
    publisher: "Telex.hu"
    date: "2026-08-02"
    role: corroborating
  - url: "https://www.kelacyber.com/blog/bytetobreach-a-deep-dive-into-a-persistent-data-leak-operator/"
    publisher: "KELA"
    date: "2026-07-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The same hacker who hit and wiped Romania's land registry database has now hacked Hungary's State Treasury in another brazen intrusion into an extremely sensitive government system."
    publisher: "Risky Bulletin (Risky Business Media)"
  - quote: "A támadók gyakorlatilag minden kritikus rendszerben megszerezték a legmagasabb szintű rendszergazdai jogosultságokat"
    publisher: "Telex.hu"
verification: multi-source
sourcing_note: "No source names a CVE — Telex.hu links to an Oracle October 2017 Critical Patch Update page without identifying a specific vulnerability, so none is recorded here. The 116-virtual-machine and 229 TB figures come from cybersecurity experts' analysis of attacker-leaked screenshots rather than an official Treasury statement, and are carried as a claim under review. The Russian-server origin is asserted on the Treasury's side — Telex.hu's 2026-08-02 report attributes it to the experts' current information, and its 2026-08-03 report attributes it to the organisation — and disputed by the attacker — not the other way round; it is unconfirmed either way."
confidence: medium
update_of: null
references:
  - 2026-07-26/weekly-w30-ch-eu-public-sector-third-party-incidents
  - 2026-07-19/ancpi-romania-cadastre-cyberattack-bytetobreach
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Enumerate internet-reachable Oracle WebLogic Server instances — including ones surviving inside legacy integrations and shadow IT — and confirm each carries Critical Patch Update levels later than October 2017; an instance that does not should be treated as already compromised rather than merely unpatched."
migrated_from: null
---

Hungarian outlet Telex.hu reports that the Magyar Államkincstár — Hungary's State Treasury — was breached in late July 2026, with the intrusion confirmed by Treasury officials to Hungarian journalists over the weekend of 2026-08-01/02, and specifically affecting its Agricultural and Rural Development Office (MVH) ([Telex.hu, 2026-08-03](https://telex.hu/techtud/2026/08/03/magyar-allamkincstar-nki-kiberbiztonsag-kibertamadas-naih-bytetobreach)). Risky Bulletin frames the significance plainly: the same actor who hit and wiped Romania's land registry database has now hacked Hungary's State Treasury in another brazen intrusion into an extremely sensitive government system ([Risky Bulletin, 2026-08-05](https://news.risky.biz/risky-bulletin-hacker-breaches-hungarys-state-treasury/)). That is the part which matters beyond Hungary — this is one financially-motivated operator, assessed by KELA as likely an individual, reaching two national government bodies of two EU member states inside roughly a month ([KELA, 2026-07-17](https://www.kelacyber.com/blog/bytetobreach-a-deep-dive-into-a-persistent-data-leak-operator/)).

**The reported entry point is the transferable part, and it is not a novel technique.** Per cybersecurity experts Telex.hu consulted, who reviewed screenshots the attacker leaked, access came through an unpatched Oracle WebLogic Server, with the outlet linking to Oracle's October 2017 Critical Patch Update ([Telex.hu, 2026-08-03](https://telex.hu/techtud/2026/08/03/magyar-allamkincstar-nki-kiberbiztonsag-kibertamadas-naih-bytetobreach)). No source names a specific CVE, so none is recorded in this entry's metadata and none should be inferred from the patch-cycle reference. What the reporting does support is the shape: a public application server carrying fixes that shipped roughly nine years ago, still reachable, still in service at a national treasury.

From that foothold the attacker escalated to domain-administrator rights — Telex.hu's sources state the attackers obtained the highest-level administrative privileges in practically every critical system — and the same reporting puts the reach at 116 virtual machines and 229 TB of data, with ransomware encrypting files on employee workstations ([Telex.hu, 2026-08-03](https://telex.hu/techtud/2026/08/03/magyar-allamkincstar-nki-kiberbiztonsag-kibertamadas-naih-bytetobreach)). Those scope figures derive from the experts' reading of attacker-supplied screenshots rather than from an official statement, and should be held as a claim under review. Treasury officials state that customer and citizen data was not affected. On origin the two accounts diverge: Telex.hu reports the Treasury's own experts attributing the attack to Russian servers, while ByteToBreach disputes that characterisation, denies making a ransom demand and describes the motive as financial. Neither account is independently confirmed. Hungary's National Cybersecurity Institute is investigating and the affected servers were disconnected on discovery.

**Defender takeaway:** the actor-level read is the one to act on. This is not an advanced intrusion set — it is a repeat operator whose demonstrated method against European government bodies is finding an internet-facing application server nobody owns any more and walking in. The Romanian precedent establishes what the endgame can look like — as this pipeline recorded on 2026-07-26 from Romania's national cybersecurity directorate, that intrusion ran to compromise of the virtualization plane, enumeration of the whole virtual-machine estate, deletion of roughly a hundred of them and ransomware on the hypervisors. None of the sources cited here describes that; it is carried from the referenced prior coverage. Public-sector estates carry this exposure class disproportionately, because legacy integration servers outlive the projects that deployed them and fall out of the asset inventory while staying routable. The check is narrow and worth running this week: which internet-reachable application servers are running software whose last patch predates the current decade, and who owns them.

**Triage:** exploitation of a legacy application server looks in telemetry like the application server's own service account doing something new — a Java process spawning a command interpreter, outbound connections from a host that should only receive them, or an authentication from the server's account to a system it has never touched. On a host that has run unchanged for years, a first-of-its-kind child process or destination is a stronger signal than it would be anywhere else, precisely because the baseline is so static.
