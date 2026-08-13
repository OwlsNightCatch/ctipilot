---
schema: 1
kind: threat
horizon: operational
title: "WindRelay — a purpose-built Android NFC-relay malware installed silently by a companion remote-access trojan during the fraud call itself, with per-victim app names carrying the victim's own name"
headline: "Group-IB documents an NFC-relay family whose install step needs no victim interaction because a paired remote-access trojan performs it mid-call"
summary: >
  Group-IB's fraud team documented WindRelay on 2026-08-12, a previously unseen Android NFC-relay malware
  family deployed alongside a personalised build of the SpyNote remote-access trojan during a live
  voice-phishing call. The victim installs only the trojan — compiled per target so its app label carries
  the victim's own name — after which the operator uses its accessibility permissions to install the
  NFC relay silently, with no screen sharing and no further victim action. Group-IB correlated 23 samples
  uploaded between November 2025 and July 2026 impersonating institutions in Czechia, Slovakia and
  Slovenia, and documents a single 13-minute call monetised twice over. The detection levers are timing
  and permission shape, not sample identity.
discovered_at: "2026-08-13T05:10:00Z"
event_date: "2026-08-12"
run_id: 2026-08-13T0412Z-intel
priority: notable
immediate_action: null
tags: [mobile, phishing, organized-crime, identity]
regions: [europe]
sectors: [finance]
entities: [malware:windrelay, malware:spynote]
techniques: [T1566.004, T1204.002, T1219, T1041, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.group-ib.com/blog/windrelay-nfc-spynote-rat-combo-fraud/"
    publisher: "Group-IB"
    date: "2026-08-12"
    role: primary
closed_sources: []
evidence:
  - quote: "SpyNote’s Accessibility Service access lets the fraudster sideload and activate the NFC app silently, with no screen sharing ever triggered."
    publisher: "Group-IB"
  - quote: "We identified 23 samples uploaded to VirusTotal between November 2025 and July 2026."
    publisher: "Group-IB"
  - quote: "Alert installations of apps from non-official sources (package installer, not Play Store) that occur during an active call. This timing pattern is a strong signal on its own, independent of what the app does."
    publisher: "Group-IB"
verification: single-source
sourcing_note: >
  Group-IB is the only party to have published on this family; the finding comes from its own fraud-protection
  engagement plus correlation of samples it identified on a public malware-sharing service. No second lab has
  written it up, so the naming, the sample count and the campaign geography rest on one assessor and the
  entry carries credibility 2 rather than 1. Group-IB cites prior work by other vendors on the older
  NFCGate/NGate relay lineage as background for the category's growth; this entry does not treat that prior
  work as corroboration of WindRelay itself, which Group-IB presents as a distinct, purpose-built family.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Group-IB's fraud-protection team published an analysis on 2026-08-12 of a technique rather than a single case: a previously unseen Android NFC-relay malware family it tracks as WindRelay, deployed together with SpyNote, a long-running commodity remote-access trojan, inside a live social-engineering call ([Group-IB, 2026-08-12](https://www.group-ib.com/blog/windrelay-nfc-spynote-rat-combo-fraud/)). The pairing is the finding. Prior NFC-relay tooling in this region — the modified NFCGate builds first seen in Czechia in late 2023 and their descendants — has been documented by several vendors as standalone malware the victim is talked into installing. Here the victim installs one thing and gets two.

**The chain, as observable behaviour.** The caller impersonates a bank employee reporting a card problem and stays on the line for the whole intrusion, rather than relying on a link or a one-time code that the victim actions alone. The victim is directed to sideload an application from outside the official store. That application is SpyNote, compiled for this target: Group-IB records that its app label and package carry the victim's own name, which the builder toolkit supports natively, and describes the purpose as trust abuse — an app already bearing your name reads as proof the caller knows who you are, and removes the unfamiliar-name check victims are trained on. Once the trojan holds Android accessibility permissions, the operator uses them to install the second component: "SpyNote’s Accessibility Service access lets the fraudster sideload and activate the NFC app silently, with no screen sharing ever triggered" ([Group-IB, 2026-08-12](https://www.group-ib.com/blog/windrelay-nfc-spynote-rat-combo-fraud/)). That property is what defeats the control most banks have deployed: screen-share detection never fires, because no screen is shared.

WindRelay's requested permissions read as a design specification for the fraud rather than a grab-bag: near-field communication to capture card data at the moment the victim is asked to tap, network access to relay the captured exchange in real time to a second device the fraudster presents to a physical terminal, contacts access for onward targeting, an unusual diagnostic-dump permission for inspecting the device and its security tooling, and custom self-declared permissions that hinder interoperation with security software ([Group-IB, 2026-08-12](https://www.group-ib.com/blog/windrelay-nfc-spynote-rat-combo-fraud/)). The documented case was monetised through two channels inside one 13-minute call — a digital loan taken out through the trojan's access to the banking application, and a card-present cash-out through the relay — which Group-IB presents as a deliberate dual-monetisation pattern rather than an improvisation.

Scale and geography come from sample correlation rather than victim reports: "We identified 23 samples uploaded to VirusTotal between November 2025 and July 2026", mimicking institutions in Czechia, Slovakia and Slovenia with text localised per country, some carrying personalised interface elements including the victim's name — which Group-IB reads as evidence the operator can build per-victim applications on demand ([Group-IB, 2026-08-12](https://www.group-ib.com/blog/windrelay-nfc-spynote-rat-combo-fraud/)).

**Detection concepts.** Group-IB's own guidance is unusually concrete and centres on timing rather than identity: "Alert installations of apps from non-official sources (package installer, not Play Store) that occur during an active call. This timing pattern is a strong signal on its own, independent of what the app does." ([Group-IB, 2026-08-12](https://www.group-ib.com/blog/windrelay-nfc-spynote-rat-combo-fraud/)) Alongside it: accessibility-service grants followed within minutes by a second sideload with no screen-share session; applications granted device-administrator privileges shortly after a call begins; and building detection around permission *sets* rather than known-sample hashes, which is what catches a family that recompiles itself per victim. On the account side, the dual-monetisation shape gives a correlation rule the bank owns entirely — a loan disbursement and a card-present transaction for the same customer within a short window, which Group-IB notes is unusual for genuine activity.

**Triage:** sideloading, accessibility grants and NFC use are each individually legitimate on Android, which is why none of them alone is the signal. The discriminators the mechanism forces are sequence and timing: the install arrives from the package installer rather than the store, it happens while a call is in progress, a second install follows the accessibility grant without any user-visible remote-control session, and the newly installed application requests near-field communication together with diagnostic-dump and self-defined permissions — a combination an ordinary consumer application has no reason to hold.

**Defender takeaway:** for a bank or payment operator in this constituency, the actionable change is that screen-share detection has stopped being a sufficient proxy for remote access, because the second-stage install is performed by the first stage rather than by the victim. Two things follow. Fraud-session monitoring should treat "app installed from an unofficial source during an active call" as a first-class signal in its own right, and customer-facing guidance should name the personalised app label — an application arriving with your own name on it — as the specific tell, because it is unusual enough to be memorable and it is the exact moment the victim can still stop the chain.
