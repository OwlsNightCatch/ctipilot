---
title: "Infrastructure Destruction Squad / BLACKNET-00: Ransomware, Firebase and ICS Tooling"
author: Ransom-ISAC Research Team
url: https://ransom-isac.org/blog/infrastructure-destruction-squad-blacknet-00/
hostname: ransom-isac.org
description: A Billie Eilish superfan, two visible operators and three tested tools sit at the centre of this assessment.
sitename: Ransom-ISAC
date: "2026-08-19"
categories: ['Threat Intelligence']
tags: ['ransomware,threat intelligence,cybersecurity,ISAC,security community,ransomware defense', 'Ransomware', 'Firebase', 'ICS', 'CNI', 'BLACKNET', 'Infrastructure Destruction Squad']
---
Core judgement

Infrastructure Destruction Squad / BLACKNET-00 combines low-confidence claims, incomplete tooling, recycled code and extensive boilerplate consistent with possible AI assistance. Most observed material demonstrates limited technical maturity, but a smaller verified subset supports practical ransomware activity, Firebase exposure discovery and ICS/SCADA reconnaissance. Defensive prioritisation should follow confirmed capability and exposure — not actor publicity.

*Figure 1: Composite BLACKNET / Infrastructure Destruction Squad reporting image used as the report lead visual.*

## Contents

## Analyst routing — where to start, by review role

This page preserves the full evidence record, including every screenshot, image and video. Every section named below is a direct link.

| Review role | Start here | Purpose | 
|---|---|---|
| SOCMINT / actor-tracking | [Actor and SOCMINT Assessment](https://ransom-isac.org#actor-and-socmint-assessment) ;[Payment Infrastructure Assessment](https://ransom-isac.org#payment-infrastructure-assessment) ;[Continuity Accounts](https://ransom-isac.org#continuity-accounts) | Operator personas, sales channels, fallback accounts, payment identifiers and claim credibility | 
| Malware analysis | [BLACKNET-00 Ransomware Builder](https://ransom-isac.org#blacknet-00-ransomware-builder) ;[Shadow Ghost Scanner](https://ransom-isac.org#shadow-ghost-scanner) ;[TRK-25 ICS Scanner](https://ransom-isac.org#trk-25-ics-scanner) | Sample behaviour, code quality, cryptography, payload capability and tool implementation gaps | 
| Detection engineering | [Indicators and Detection Context](https://ransom-isac.org#indicators-and-detection-context) ;[Host and Persistence Artifacts](https://ransom-isac.org#host-and-persistence-artifacts) ;[Network and Behavioural Indicators](https://ransom-isac.org#network-and-behavioural-indicators) ;[Detection Rules](https://ransom-isac.org#detection-rules) | Host artefacts, hashes, YARA logic, detection caveats and false-positive handling | 
| CNI / OT review | [Why This Matters](https://ransom-isac.org#why-this-matters) ;[Potential Water-Sector and CNI Relevance](https://ransom-isac.org#potential-water-sector-and-cni-relevance) ;[Operationally Relevant ICS/CNI Capabilities](https://ransom-isac.org#operationally-relevant-ics-cni-capabilities) ;[Why the Reconnaissance Output Matters](https://ransom-isac.org#why-the-reconnaissance-output-matters) | Water-sector relevance, ICS protocol coverage, exposed-service risk and escalation priorities | 

## Executive Summary

Infrastructure Destruction Squad / BLACKNET-00 is a low-maturity, highly promotional actor cluster whose public claims and advertised tooling frequently exceed the capabilities verified in the available evidence. The central defensive finding is that technically inconsistent actors can still package operationally relevant components within otherwise incomplete or exaggerated material:

1. **BLACKNET-00 ransomware builder** — misrepresents its cryptography and is recoverable in the tested build, but still encrypts files, alters endpoint policy, establishes persistence, displays ransom messaging and transmits victim telemetry.
2. **Shadow Ghost scanner** — wrapped in low-quality tkinter boilerplate, but contains a functional Firebase reconnaissance module that identifies exposed Storage, Firestore and Realtime Database deployments.
3. **TRK-25 ICS scanner** — not a credible standalone weapon, but contains reusable SCADA/HMI discovery logic, industrial protocol coverage, OT product fingerprinting and near-operational Modbus routines.

The cluster has also broadened commercially rather than technically: it now advertises DDoS-as-a-Service alongside tool and access sales, and a third-party channel has attributed a DDoS attack against an Indian telecoms operator to BLACKNET-00. No DDoS tooling was supplied for analysis, so capacity and delivery capability remain unverified.

**Recommended posture:** deprioritise unverified publicity claims, but prioritise confirmed host artefacts, exposed CNI leads and repeatable behaviour. Neither amplify the actor's marketing nor dismiss validated capability.

### Assessment at a Glance

| Component | Observed capability | Risk | Confidence | Defender action | 
|---|---|---|---|---|
| BLACKNET-00 ransomware builder | Weak but functional ransomware payload: encryption, persistence, endpoint policy changes, ransom UI and Telegram reporting | Medium | High | Detect durable host artefacts; preserve ransom note and encrypted samples because recovery is likely in the tested build | 
| Shadow Ghost scanner | Functional Firebase exposure reconnaissance inside a low-quality GUI wrapper | Medium | High | Audit Firebase Storage, Firestore and Realtime Database rules; treat findings as misconfiguration exposure, not Firebase exploitation | 
| TRK-25 ICS scanner | Reusable ICS/SCADA reconnaissance logic, protocol coverage, OT product fingerprinting and near-operational Modbus routines | Medium | Medium-high | Validate exposed OT services, monitor industrial-port scanning and assess the four hardcoded public /24 ranges | 
| DDoS-as-a-Service | Advertised paid DDoS offering; one third-party attribution of a DDoS attack against a telecoms operator. No tooling supplied for analysis | Low-medium | Low | Treat as an advertised service line, not a demonstrated capability; confirm volumetric and application-layer availability protection if named as a target | 
| Actor claims | Self-reported breach, access-sale and CNI-impact claims mixed with padded scan logs and threat-heavy marketing | Low-medium | Medium | Verify before escalation; route CNI and water-sector claims as high-priority-to-verify rather than established compromise | 

### Rating Method

Risk ratings combine demonstrated capability, operational reliability, plausible access and potential impact. **Low** denotes limited or unreliable capability; **Medium** denotes credible capability with meaningful but constrained impact or reusability; **High** denotes demonstrated, reliable capability with substantial operational impact. Confidence is assessed separately from risk and reflects the quality, independence and directness of the supporting evidence.

### Evidence and Confidence Model

| Evidence type | Used for | Analytic weight | Caveat | 
|---|---|---|---|
| Static code analysis | Ransomware builder, Shadow Ghost and TRK-25 implementation claims | High | Confirms what the available samples can do, not what every private build or later variant can do | 
| Controlled execution and demonstrations | Ransomware encryption, decryptor workflow and GUI behaviour | High | Results apply to the tested build and environment | 
| Actor screenshots and channel posts | Personas, claimed victims, sales activity, fallback handles and advertised capabilities | Medium | Useful for attribution and intent, but not proof that every claim occurred as described | 
| Public reporting and prior Ransom-ISAC analysis | Water-sector context, CARR relationship and broader CNI relevance | Medium-high | Contextualises risk; does not independently validate each actor claim | 

## Key Judgements

- **Capability is uneven, not absent.** Most advertised features are cosmetic or non-functional, but several modules support real reconnaissance, endpoint disruption or victim intimidation.
- **The CNI value is reconnaissance-led.** TRK-25’s strongest component is not destructive control; it is discovery of exposed SCADA/HMI services and OT product fingerprints that could feed later targeting.
- **The ransomware is weak but disruptive.** The tested payload uses repeating-key XOR and discloses the key locally, but its file-enumeration, persistence, policy-modification and ransom-interface logic still matter to defenders.
- **Shadow Ghost matters where Firebase is misconfigured.** It does not exploit Firebase; it identifies insecure deployments caused by permissive rules or exposed configuration.
- **The DDoS offering is commercial breadth, not new technical capability.** The cluster advertises DDoS-as-a-Service, and a third-party channel credits it with an attack on an Indian telecoms operator. No DDoS tooling was available for analysis, so capacity and reliability are unverified.
- **Claims require verification before escalation.** Victim claims are self-reported and padded. Treat CNI-related claims as high-priority-to-verify, not as established fact.
- **Detect on behaviour, not shared infrastructure.** Telegram, Firebase and Google API domains are legitimate services. Detection value comes from tooling strings, file hashes, host artefacts and protocol combinations.

## Defender Priorities

1. Remove direct internet exposure from PLCs, HMIs and other OT; require mediated, monitored remote access.
2. Audit Firebase Storage, Firestore, Authentication and Realtime Database rules for unintended anonymous access.
3. Hunt for the durable BLACKNET host artefacts and preserve ransom notes, encrypted samples and volatile telemetry for recovery.
4. Treat claimed CNI compromises and embedded public ranges as verification leads; coordinate validation and responsible disclosure with asset owners and sector authorities.
5. Use the YARA rules for controlled hunting and triage only after local compilation and benign-corpus testing.

## Actor and SOCMINT Assessment

The screenshots and videos below preserve actor-facing material and tool demonstrations collected from public or actor-controlled channels. They support assessment of branding, intent and advertised capability, but do not prove that every claimed intrusion or impact occurred as described.

Two Telegram channels sit at the centre of the activity: one oriented around CNI/ICS targeting and access brokerage, and another around BLACKNET-00 ransomware branding, tooling and sales. The accounts appear technically ambitious but operationally inconsistent: much of the material is inflated, incomplete or unreliable, while a smaller subset is functional enough to matter.

### Operator Personas and Accounts

At least two visible accounts are associated with the Infrastructure Destruction Squad and BLACKNET Telegram ecosystems. Available evidence does not establish whether they represent two distinct people, shared access to multiple accounts or one person operating several personas.

One account presents as a Billie Eilish fan and uses the handle `@blacknetransom`:

*Figure 2: Telegram profile associated with the BLACKNET-00 ransomware persona using the @blacknetransom handle.*

The operator self-identifies as Chinese, although this claim is unverified:

*Figure 3: Actor self-identification claim preserved as source material; nationality claim remains unverified.*

The actor reinforces this presentation by publishing dashboard video tool demonstrations in Mandarin Chinese:

*Figure 4: Actor-shared dashboard demonstration using Mandarin-language interface material.*

A second account is presented as @blacknetransom's brother and uses the handle `@xonsee666`:

*Figure 5: Secondary Telegram persona presented by the actor ecosystem as linked to @blacknetransom.*

Our [April 2026 advisory](https://ransom-isac.org/blog/iran-linked-hackers-water-utilities-advisory/) reported technical details regarding a sophisticated and malicious Python-based Graphical User Interface (GUI) Industrial Control System (ICS) reconnaissance and data exfiltration tool known as “TRK25-ADVANCED” — a similar functionality to a previous predecessor [Kurtlar_SCADA.exe](https://www.virustotal.com/gui/file/61219ea5cd69fb4fbf20cb304673cecfd42d2251aa3b4c7e6f6b36a52ba9013e) used by groups such as [Z-Pentest](https://www.opensanctions.org/entities/NK-ArLgZkNLv3e7mLHjDWyNgE/) and [CARR — Cyber Army of Russia](https://rewardsforjustice.net/rewards/carr-and-z-pentest/) — allied with Pro-Palestine groups during the Israel-HAMAS conflict taught to enumerate and hack into exposed industrial control systems.

Both accounts have been used to offer TRK-25 to hacker groups such as the Iraqi-nexus ‘313 Team’:

*Figure 6: Actor sales material referencing TRK-25 and alleged buyer interest.*

In July 2026, the same group — ‘313 Team’ (The Islamic Cyber Resistance in Iraq) — claimed to have used BLACKNET-00’s TRK-25 tooling in an attack on the servers of a major American news agency:

*Figure 7: Channel post in which ‘313 Team’ claims a TRK-25-enabled attack against a major American news agency; the claim is group-reported and has not been verified by Ransom-ISAC.*

TRK-25 was also offered for sale to the Iranian-nexus group ‘HEXVIOR’:

*Figure 8: Actor material showing TRK-25 offered to HEXVIOR; solicitation is not evidence that a sale completed.*

**Aliases / branding:** The group operates under several interchangeable names — “BLACKNET”, “BLACKNET-CORPORATE” and “infrastructure destruction squad” — with a primary contact handle used for sales enquiries alongside referenced X and Telegram personas.

They have also advertised their services on multiple hacker forums including Breach Forums:

*Figure 9: Forum advertising material for BLACKNET / Infrastructure Destruction Squad services and tooling.*

A Tox address has also been shared over Telegram for use if the channel or its accounts are taken down:

*Figure 10: Fallback Tox contact shared by the actor for continuity after possible account or channel takedown.*

- **TOX ID:**`05a63a33e6233cdfe2a86a49aa73148af13ab6068db82c93690827da75e64d422b`

### Continuity Accounts

| Handle | Purpose | 
|---|---|
| `@zzzzzzzzkss` | Alternative Telegram account | 
| `@ayeowetee` | Alternative Telegram account | 

Both handles were provided as continuity accounts to use if another account is removed or suspended. Treat them as linked operator identifiers; their current status has not been independently verified.

Publishing fallback handles in advance suggests deliberate account-continuity planning and an expectation of platform enforcement. Monitor and record both identifiers together rather than treating them as unrelated accounts.

### Infrastructure Destruction Squad Channel

**Telegram channel:** `@infrastructurek`

*Figure 11: Infrastructure Destruction Squad Telegram channel branding and channel context.*

**Nature of the channel:** A hacktivist-flavoured extortion and access-brokerage channel. It mixes ideological messaging with straightforward commercial activity: selling target access, tooling and stolen data. Posts alternate between breach “announcements”, bragging and price lists.

**Cultural / persona signal:** Billie Eilish references recur across the actor's visible presentation, including profile imagery and adjacent persona material. Treat this as a branding and self-presentation signal rather than attribution evidence: it may help link accounts or recognise continuity across posts, but it should not be over-weighted as a technical or geopolitical indicator.

**Primary activities observed:**

Publishing breach claims against a range of targets, typically padded with scan logs and statistics to project scale.

*Figure 12: Example breach-claim post containing actor-provided supporting material.*

Selling initial access to compromised organisations at low, fixed price points.

*Figure 13: Actor post advertising initial access for sale at a fixed price.*

Advertising custom offensive tooling (SCADA/ICS-branded utilities, a wallet/credential-stealing builder marketed as malware-as-a-service).

*Figure 14: Actor advertisement for custom offensive tooling, including SCADA/ICS-branded material.*

Occasional solicitation of buyers before conducting an operation (“we'll do X if there are buyers”), indicating a demand-driven, for-hire posture.

*Figure 15: Demand-driven solicitation post indicating a for-hire or buyer-led operational posture.*

**Targeting profile (anonymised):** Victims claimed across multiple continents and sectors, including an aerospace/defence manufacturer, a national military network, municipal water/utility and industrial-control systems, industrial-automation and agrochemical firms, a fintech/payments platform, and various exposed remote-access hosts. Targeting appears opportunistic (weak passwords, exposed management interfaces, end-of-life router firmware) rather than tied to one region or vertical, though ideological targeting language appears alongside the financial motive.

**Motivation:** Mixed. Financial (ransom demands, access and tool sales) combined with ideological/geopolitical framing in some posts.

**Tradecraft signals for analysts:** Reliance on exposed management interfaces, unauthenticated services, default/weak credentials and unpatched network-edge devices. Claims are self-reported and frequently unverifiable — scan-log padding and inflated statistics are a recurring credibility red flag.

The channel claims compromises of organisations and industrial control systems worldwide:

*Figure 16: Actor claim set presenting worldwide organisational and ICS compromise activity.*

Claimed victims include an Argentinian municipality, an Indian water-management system and a US aerospace manufacturer:

*Figure 17: Actor-provided claimed victim examples spanning municipal, water-management and aerospace targets.*

What makes this group hard to categorise is that it never converted its ransomware into a service. No affiliate structure or revenue split is evident in the observed material — the builder was released publicly rather than licensed — and income comes instead from selling tooling and access outright. That makes them a hybrid of ransomware author, toolkit vendor and, loosely, initial access broker, but never a RaaS operator. The post below shows access to an Israeli law firm offered for sale on pwnforums:

*Figure 18: Actor post offering initial access to an Israeli law firm for sale on pwnforums; the listing is actor-provided and the claimed access is unverified.*

### Ransomware BLACKNET-00

**Telegram channel:** `@Ransomwareg`

*Figure 19: Ransomware-branded Telegram channel associated with BLACKNET-00 activity.*

### Selected Targets Claimed by the Ransomware-Branded Channel

| Victim (anonymised) | Sector | Region | Claim summary | 
|---|---|---|---|
| National flag carrier | Aviation | South Asia | Claimed full network breach; exfil of system credentials, operational/maintenance systems, and aero-engine maintenance records. Access advertised for approximately US$50,000, payable in BTC, alongside a ransom threat | 
| Payments / KYC platform | Fintech | Africa-linked clientele | Claimed exfil of KYC/KYB records for 500+ corporate clients — incorporation documents, directors' identity documents, bank statements, AML policies | 
| National flag carrier | Aviation | North Africa | Claimed full compromise of an edge router via exposed SNMP; hundreds of devices and thousands of accounts affected, followed by an extended list of intended exploitation actions | 

### Analyst Notes (anonymised)

The channel posts under ransomware branding but reuses a contact handle seen in earlier activity. This supports a common operational nexus across the brandings, but does not by itself prove that a single person controls every account.

One aviation victim's data included **third-party vendor material** (an aero-engine manufacturer's maintenance reports), illustrating supply-chain data propagation — a vendor's sensitive data surfacing through a customer breach rather than a direct intrusion.

The North-African aviation post is largely a **capability-and-intent monologue** (“we can do X…”) rather than claimed completed actions. Treat that portion as stated intent, distinct from the exfiltration the actor claims to have already carried out.

Consistent with earlier dumps, access is offered **for sale**, and claims are **self-reported and unverified** — the padding and threat-heavy framing are recurring credibility flags.

They are also attempting to build a marketplace, although its viability is unproven:

*Figure 20: Actor material advertising a proposed marketplace; viability and usage are unverified.*

### BLACKNET-00 DDoS Activity

BLACKNET-00 has also expanded into DDoS-as-a-Service:

*Figure 21: Actor material advertising DDoS attacks as a paid service; pricing, capacity and delivery capability are unverified.*

In August 2026, posts in the pro-Russian channel `@rippersecchat` claimed that BLACKNET-00 had conducted a DDoS attack against an Indian telecoms operator on behalf of the pro-Palestinian group `Blackout DDoS`. Unlike most claims in this report, this one originates with a third party rather than with the actor, but it remains unverified.

*Figure 22: Post in the pro-Russian channel @rippersecchat attributing a DDoS attack against an Indian telecoms operator to BLACKNET-00; the claim is third-party and unverified.*

### Payment Infrastructure Assessment

**TRON address:** `TS7cmQrHcRtLuijLdL3CP7s5EgeN6tn7KT`

Actor material presents this as a ZixiPay receiving address. That supports apparent use of the service, but does not establish who controls the address or any ownership relationship with ZixiPay. ZixiPay's website describes a multi-asset cryptocurrency wallet, while open-source reporting links the brand to the Georgian payment service Ziqsipay, whose registration was reportedly cancelled in June 2019. Ransom-ISAC has not independently verified the current legal entity or beneficial ownership of the address.

ZixiPay, operated by ZixiPay LLC, is a custodial multi-asset cryptocurrency wallet and payment API service supporting BTC, ETH, LTC, TRX and USDT/USDC on TRC-20 and ERC-20; its corporate footprint is inconsistent across registries — public listings place the operator in Zug, Switzerland, while open-source reporting ties the same brand to the Georgian payment provider Ziqsipay, whose registration was cancelled in June 2019.

**ZixiPay:** [Official website](https://zixipay.com/)

**Calcalist / CTech:** [The crypto path: How terrorist organizations finance their activities under the radar](https://www.calcalistech.com/ctechnews/article/ll71hprpt)

*Figure 23: Crystal Intelligence - Tron Address report reviewed during the assessment.*

## Why This Matters

Claims of targeting US water supplies carry weight that most breach boasts do not, because water and wastewater systems are designated critical infrastructure and the sector is uniquely exposed. Many US utilities are small, locally run and under-resourced, yet they operate industrial control systems — particularly programmable logic controllers (PLCs) — that are frequently reachable from the open internet through the same weaknesses this actor exploits elsewhere: exposed management interfaces, default or weak credentials, and unpatched edge devices.

Variant distinction

The screenshot and actor claims below concern a separate TRK25-ADVANCED / paid build. Ransom-ISAC did not receive that build for code review. Screenshot capture, result exfiltration and claimed victim impact must not be attributed to the analysed 50508000.py sample without additional evidence.

*Figure 24: A separate TRK25-ADVANCED build, labelled “Industrial Systems Exploitation Framework”, showing scan results against a hardcoded range.*

Actor material and prior Ransom-ISAC reporting associate TRK25-ADVANCED branding with earlier Kurtlar_SCADA tooling, but this report does not establish that lineage through code-overlap analysis or repository history. Treat the relationship as a working analytic hypothesis. The separate demonstrated build appears broader than the analysed `50508000.py` sample and is presented as supporting internet-exposed PLC/SCADA/HMI discovery, default-credential testing, screenshot capture and result exfiltration. Those additional functions are actor-demonstrated rather than code-verified here. Its apparent advantage is reach against exposed, unhardened OT—not technical sophistication.

*Figure 25: Channel post claiming a water-pumping control system was compromised using the paid version of TRK25 ADVANCED SCADA; the claim is actor-reported and unverified.*

On 30 July 2026, CISA warned that it was observing a significant increase in attacks targeting internet-exposed programmable logic controllers (PLCs) in the water and wastewater systems sector. CISA, the FBI and the EPA urged operators to remove publicly exposed PLCs and other operational technology from the internet as soon as possible. The concern is physical, not just informational: unlike stolen data, manipulated control systems affect real processes — in recent incidents, threat actors modified passwords to lock out operators and disconnected PLCs by changing their IP addresses, resulting in boil-water notices and sustained manual operations. Officials also stress that organisations of all sizes are being targeted, including some with mature cybersecurity programmes.

*Figure 26: Follow-up post conceding the target had since been remediated, alongside a stated intent to name further US water systems.*

It also matters because it fits a real and escalating pattern, which raises the stakes on verification either way. A coordinated campaign targeted more than 30 Minnesota community water systems on 26–27 July 2026 and disrupted operations at some utilities. In 2023, the compromise of a Unitronics PLC at the Municipal Water Authority of Aliquippa in western Pennsylvania formed part of activity that US agencies attributed to IRGC-affiliated CyberAv3ngers. Analysts note that water and wastewater systems are increasingly becoming part of broader geopolitical cyber conflicts even when they are not the primary targets, and much of the operational technology supporting them was never designed with today's threats in mind. So a claim like this cannot be dismissed out of hand — but this actor's track record (self-reported claims, padded scan logs, threat-heavy monologues, access advertised cheaply for sale) means claims are frequently exaggerated or reframed. For a CTI report the significance is twofold: if credible, it warrants escalation to sector authorities and asset owners given the potential for physical harm; if inflated, the claim still functions as intimidation and marketing that erodes public trust and consumes responder resources. Either way it should be flagged as **high-priority-to-verify** and routed to the appropriate authorities (in the US, CISA and the water sector's information-sharing channels) rather than taken at face value.

### Sources and References

*Accessed 16 August 2026.*

- **CISA:**[CISA Urges Water and Wastewater Systems Sector to Protect OT Against Activity Targeting PLCs](https://www.cisa.gov/news-events/alerts/2026/07/30/cisa-urges-water-and-wastewater-systems-sector-protect-ot-against-activity-targeting-plcs)
- **FBI / IC3:**[Malicious Cyber Actors Targeting Water and Wastewater Sector Internet-Facing PLCs](https://www.ic3.gov/PSA/2026/PSA260730.pdf)
- **CISA:**[IRGC-Affiliated Cyber Actors Exploit PLCs in Multiple Sectors, Including US Water and Wastewater Systems Facilities](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a)
- **WaterISAC:**[Water Utility Control System Cyber Incident Advisory: Municipal Water Authority of Aliquippa](https://www.waterisac.org/tlpclear-water-utility-control-system-cyber-incident-advisory-icsscada-incident-municipal)
- **Reuters:**[Minnesota IT officials disclose coordinated cyberattack at more than 30 local water systems](https://www.reuters.com/legal/litigation/minnesota-it-officials-disclose-coordinated-cyberattack-more-than-30-local-water-2026-07-28/)
- **BleepingComputer:**[CISA warns of cyberattacks disrupting U.S. water utilities](https://www.bleepingcomputer.com/news/security/cisa-warns-of-cyberattacks-disrupting-us-water-utilities/)
- **Cybernews:**[CISA warns water utilities: Get control systems off the internet](https://cybernews.com/privacy/cisa-warning-utility-companies-internet-exposed-controls-hack/)
- **Cybersecurity Dive:**[US authorities see ‘significant escalation’ in attacks on water system devices](https://www.cybersecuritydive.com/news/us-authorities-escalation-attacks-water-system-devices/826715/)
- **TIME:**[What to Know About the U.S. Water Systems Cyberattacks](https://time.com/article/2026/08/02/what-to-know-about-the-u-s-water-systems-cyberattacks/)
- **ABC News:**[Feds warn local water systems over increased cyberattacks after Minnesota incident](https://abcnews.com/US/investigators-iran-connection-minnesota-water-system-hacks-us/story?id=135237777)
- **E&E News / POLITICO:**[CISA warns of ‘significant increase’ in cyber threats to U.S. water utilities](https://www.eenews.net/articles/cisa-warns-of-significant-increase-in-cyber-threats-to-us-water-utilities/)

## BLACKNET-00 Ransomware Builder

The operators released the builder publicly in June 2026, sharing this version — ‘0077’ — and framing it as “a small gift” to the community:

*Figure 27: Channel post releasing the builder publicly as “a small gift”.*

Ransom-ISAC obtained the builder from the channel and analysed it in an isolated environment.

### BLACKNET-00 Ransomware Construction Kit v10.0

#### Overview

The builder was demonstrated alongside the group's Payload Injector & Distributor:

*Operator demonstration of the builder alongside the group's Payload Injector & Distributor.*

The analysed builder is a 34.7 MB, PyInstaller-packaged Python 3.13 tkinter application containing 1,028 bundled files. It presents itself as a “Professional All-in-One Ransomware Builder,” but static analysis shows that many advertised functions are cosmetic, incomplete or absent. The generated C++ payload nevertheless contains a functional core capable of file encryption, system-policy modification, persistence, screenshot capture and victim reporting.

Threat rating: MEDIUM

The builder is operationally uneven, but its generated payload can encrypt files, modify endpoint policy, establish persistence, capture screenshots, transmit victim telemetry and display a ransom interface. Encryption in the tested build is recoverable.

#### Sample Metadata

| Attribute | Value | 
|---|---|
| Sample | `blacknet-00..exe` | 
| Format | PE32+ console executable, x86-64 | 
| Packaging | PyInstaller; UPX-packed | 
| Size | 34,669,202 bytes | 
| Bundled files | 1,028 | 
| Python version | 3.13 | 
| Entry point | `blacknet-00.pyc` | 
| Original source name | `blacknet-00.py` | 
| Primary class | `UltimateRansomwareBuilder` | 

#### GUI Capability Matrix

| Tab | Advertised purpose | Observed implementation | 
|---|---|---|
| General | Project name, version and output format | Configuration only | 
| Ransom Note | Wallet, contact details, message and deadline | Implemented | 
| Encryption | AES-256, AES-128, Fernet and hybrid RSA/AES choices | Selection is cosmetic; generated payload uses hardcoded XOR | 
| Targets | File extensions, directories and exclusions | Implemented | 
| System Locks | Disable Task Manager, Registry Editor, CMD and PowerShell | Implemented through generated registry commands | 
| Behaviour | Process termination, spreading and self-deletion | Partially implemented | 
| Persistence | Startup folder, Registry Run and service installation | Registry Run and scheduled-task methods implemented | 
| Wallpaper | Custom ransom wallpaper and desktop notes | Implemented | 
| Network | C2, callback URL, Tor and I2P | Configuration only; no general-purpose C2 implementation | 
| Evasion | Anti-VM, anti-debugging and sandbox detection | Minimal process-name checks | 
| Ransom Options | Double and triple extortion | Labels only | 
| Advanced | Seven stealers and file upload | UI controls without backing modules | 
| Statistics | Campaign tracking | Empty placeholder | 
| Build | Generate deployable outputs | `.py, .bat, .ps1 and .cpp` ; no compiler is bundled | 

#### Generated Payload Capability Assessment

Static analysis of the approximately 36 KB `MyRansomware.cpp` output identified a small but functional payload core.

**Implemented capabilities**

| Capability | Observed behaviour | 
|---|---|
| File encryption | Enumerates drives C: through Z:, targets more than 60 extensions and applies the repeating-XOR routine | 
| System lockdown | Generates registry commands intended to disable Task Manager, Registry Editor and CMD | 
| PowerShell interference | Uses an Image File Execution Options debugger redirect to systray.exe | 
| Process termination | Invokes taskkill against 15 security and analysis processes | 
| Persistence | Creates a Registry Run entry and scheduled task named "WindowsUpdate" | 
| Ransom interface | Displays a full-screen Win32 window with a key-entry field and countdown timer | 
| Wallpaper modification | Creates and applies a ransom-themed BMP through GDI | 
| Screenshot capture | Writes %TEMP%\screenshot_blacknet.bmp and submits the image to Telegram | 
| Victim reporting | Sends the victim identifier, hostname, username and decryption key to Telegram through WinHTTP | 
| Ransom note | Writes READ_ME_BLACKNET.txt to the desktop and includes the decryption key | 
| Anti-analysis | Checks for vmwaretray.exe and vboxservice.exe | 

**Advertised but absent or incomplete capabilities**

| Claim | Observed status | 
|---|---|
| Seven data stealers | UI controls only; no password, browser, wallet, FTP, email, VPN or messenger stealer modules identified | 
| General-purpose C2 and callback server | Settings exposed in the GUI, but no corresponding C2 implementation identified | 
| EternalBlue exploitation | No exploit implementation identified | 
| USB and network spreading | No supporting propagation logic identified | 
| Tor and I2P | Configuration labels only | 
| Double and triple extortion | Interface text without backing capability | 
| AppLocker or UAC bypass | Attempts elevation through ShellExecuteW with runas; this is not a bypass | 
| More than 50 encryption algorithms | Generated C++ retains the same repeating-XOR routine | 

The builder produces the following build-information file:

```
BLACKNET-00 Ransomware - Build Information
=========================================
Project: MyRansomware
Version: 1.0
Author: BLACKNET-00
Build Date: 2026-[redacted] [redacted]
Encryption: AES-256-CBC (Recommended)
Key Size: 256 bits
File Extension: .blacknet
Bitcoin Wallet: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
Email Contact: 
```
[\[email protected\]](https://ransom-isac.org/cdn-cgi/l/email-protection)
Amount: 0.32 BTC ($20000)
Deadline: 72 hours
Build Type: Standard Build
Compiler: g++
Optimization: -O2
Files Generated:
- MyRansomware.cpp (C++ Source Code)
- MyRansomware.exe (Executable - needs compilation)
To compile:
g++ MyRansomware.cpp -o MyRansomware.exe -mwindows -static -s -lwinhttp -lcrypt32 -lshlwapi -lws2_32 -lpsapi -lgdi32
Excluded indicator

1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa is the coinbase address of Bitcoin's genesis block—a common public placeholder, not assessed operator infrastructure. Its presence does not establish actor control or AI-assisted development. Do not block, report or ingest it as an IOC.

Compilation of the generated C++ source proceeds as follows:

*Ransom-ISAC lab recording: compiling the generated C++ source.*

Upon execution, the desktop background changes immediately and targeted files are encrypted:

*Ransom-ISAC lab recording: wallpaper replacement and file encryption on execution.*

**Critical implementation flaw:** by default, the decryption key is written directly into the ransom note:

*Ransom-ISAC lab recording: the ransom note disclosing the decryption key.*

### Encryption and Decryption — Implemented Design

**Claimed:** AES-256-CBC encryption.**Implemented:** A 32-character alphanumeric key applied as a repeating XOR sequence. No AES operation is performed by this routine.

#### Encryption Routine

At line 471 of `MyRansomware.cpp`, each plaintext byte is XORed with one byte of the key — `data[i] ^= key[i % key.length()];`. The key index wraps after 32 characters, so the same sequence is reused throughout the file:

`ciphertext[i] = plaintext[i] XOR key[i mod 32]`
This is a reversible byte transformation rather than a modern authenticated-encryption scheme. It provides no integrity protection and inherits the weaknesses of repeating-key XOR.

#### Worked Example

For the first four bytes of a DOCX file, whose ZIP header begins `50 4B 03 04`, and a key beginning `aB3x`:

| Position | Plaintext | Key byte | Ciphertext | 
|---|---|---|---|
| 0 | `0x50` | `'a' (0x61)` | `0x31` | 
| 1 | `0x4B` | `'B' (0x42)` | `0x09` | 
| 2 | `0x03` | `'3' (0x33)` | `0x30` | 
| 3 | `0x04` | `'x' (0x78)` | `0x7C` | 

The resulting ciphertext begins `31 09 30 7C`. The same 32-character key sequence then continues and repeats for the remainder of the file.

#### Decryption Routine

XOR is self-inverse, so decryption applies the same operation with the same key and byte alignment:

`plaintext[i] = ciphertext[i] XOR key[i mod 32]`
No separate decryption algorithm is required; applying the key a second time restores the original bytes.

#### Key Generation

Lines 353–358 construct a 32-character key from the 62-character alphanumeric set:

```
std::string GenerateKey() {
    const std::string chars =
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789";
    std::string key;
    for (int i = 0; i < 32; ++i) {
        key += chars[rand() % 62];
    }
    return key;
}
```
Although the output is 32 characters long, `rand()` is not a cryptographically secure pseudorandom number generator. Its effective strength depends on the runtime implementation and, critically, how it is seeded.

#### Why File Recovery Is Straightforward

1. **The key is disclosed in the ransom note.** The payload writes`Decryption Key: <key>` directly to`READ_ME_BLACKNET.txt` on the desktop. In the default build, recovery therefore requires only extracting that value and applying the XOR routine again.
2. **Repeating-key XOR is vulnerable to known plaintext.** Predictable file headers and structured content reveal the corresponding key bytes when XORed with the ciphertext. If 32 plaintext bytes are known at aligned positions, the complete key can be reconstructed. Because one key is reused across files, recovered key positions can also be combined from multiple samples.
3. **The key generator may permit seed recovery.** C`rand()` is unsuitable for cryptographic key generation. If it is seeded from a predictable value such as the current time, an analyst can enumerate plausible seeds and regenerate candidate keys. The exact work factor depends on the runtime implementation and seed source.

Recovery impact

the default ransom-note disclosure is sufficient on its own. Known-plaintext and seed-recovery techniques provide additional recovery paths if that disclosure is removed in a later build.

#### Comparison With Mature Ransomware Cryptography

| Property | BLACKNET-00 implementation | Typical mature ransomware design | 
|---|---|---|
| Data transformation | Repeating-key XOR | Modern symmetric encryption such as AES or ChaCha20 | 
| Key material | One 32-character alphanumeric string | Cryptographically generated per-file, per-host or per-session keys | 
| Key protection | Written in plaintext to the ransom note | Symmetric key wrapped with an attacker-controlled RSA or elliptic-curve public key | 
| Key reuse | Same repeating key across files | Design varies, but mature families commonly limit reuse through per-file or per-host derivation | 
| Randomness | `C rand()` | `Operating-system CSPRNG such as BCryptGenRandom` | 
| Recovery without operator material | Immediate from the ransom note; additional analytical recovery paths exist | Normally depends on a cryptographic or implementation flaw, recovered private key, or viable backup | 
| Integrity protection | None | Varies; stronger designs may authenticate encrypted data or metadata | 

### Ransom-ISAC Universal Decryptor

Ransom-ISAC developed a decryptor for files encrypted by BLACKNET-00. Although the builder advertises AES-256, generated payloads instead apply repeating-key XOR using a 32-character key produced through C `rand()`.

#### Recovery Workflow

The decryptor attempts four recovery methods in sequence:

1. **Ransom-note extraction** — searches READ_ME_BLACKNET.txt for the plaintext decryption key.
2. **Known-plaintext recovery** — compares predictable file signatures, such as`%PDF` and`\x89PNG` , with the corresponding ciphertext to recover aligned key bytes.
3. **PRNG-seed recovery** — where the payload uses`srand(time(NULL))` , enumerates plausible timestamps and reproduces candidate key sequences.
4. **Statistical recovery** — estimates the repeating-key length and likely key bytes from ciphertext patterns when no disclosed key or sufficient known plaintext is available.

If one method fails, the decryptor proceeds to the next.

Controlled-test result

the statistical fallback recovered all 277 files in the test corpus without prior knowledge of the key. This result applies to the tested BLACKNET implementation and file set; it should not be interpreted as a universal method for defeating every XOR-based scheme.

#### Broad Variant Coverage

The builder hardcodes the repeating-XOR routine into its generated C++ template. The decryptor is designed to identify the encrypted-file extension, estimate the key length and infer the likely key character set, allowing it to accommodate configuration changes without requiring a separate decryptor for every build.

*Ransom-ISAC universal decryptor recovering files encrypted by a generated BLACKNET-00 payload.*

The decryptor is available in [Ransom-ISAC's LOCKSTAR repository](https://github.com/Ransom-ISAC-Org/LOCKSTAR/tree/main/BlackNet-00) and can be run with:

`python blacknet_universal_decryptor.py --scan-dir C:\Users\FlareVM\Desktop --cleanup`
Use only on systems you own or are authorised to recover.

#### Critical Weaknesses

1. **Cryptography:** claimed AES-256, implemented repeating-key XOR, key disclosed in the ransom note, rand() key generation and no asymmetric key protection. Set out in full under**Encryption and Decryption — Implemented Design** ; not repeated here.
2. **Key exposure through Telegram:** victim telemetry includes the decryption key, creating an additional recovery and takedown opportunity if the associated account or bot is identified.
3. **External compilation required:** the builder generates source and script outputs but does not bundle a compiler for producing a Windows executable.

#### Indicators of Incomplete or Possibly AI-Assisted Development

- More than 60 features are advertised, while fewer than ten substantive capability groups are implemented.
- Encryption-selection controls do not alter the generated XOR routine.
- Seven advertised stealer modules are represented only by tkinter controls.
- Triple-extortion functionality is limited to interface text.
- The Statistics tab remains an empty placeholder.
- The builder references the `qrcode` dependency without bundling it.
- Cryptographic key generation relies on C `rand()` .
- The supplied material labels the builder as version `10.0` , but no preceding versions were identified.
- The build-information output lists Bitcoin's genesis-block coinbase address as the configured payment wallet—a common public placeholder rather than an operator-controlled address.

#### Intelligence Significance

The recoverable cryptography is the least durable finding here. The file-enumeration, persistence, policy-modification and ransom-interface components are conventional and functional, and they would survive a competent rewrite of the encryption routine: replacing the XOR loop with an authenticated cipher, a CSPRNG and an attacker-held public key is a small, well-understood change that would invalidate every recovery path described above while leaving the rest of the payload intact.

Detection should therefore anchor on the durable host artefacts — `Global\BlackNetMutex`, the `WindowsUpdate` Run key and scheduled task, `READ_ME_BLACKNET.txt`, `BlackNetRansomClass` and the `%TEMP%` BMP writes — rather than on the present encryption weakness.

## Shadow Ghost Scanner

*Figure 28: The SHADOW-GHOST ULTIMATE v4.0 desktop shortcut.*

Operator demonstration of the Shadow Ghost scanner:

*Operator demonstration of the Shadow Ghost scanner.*

*Figure 29: Shadow Ghost as advertised on Telegram.*

### Shadow Ghost Firebase Analysis — Shadow..py

Assessment

The surrounding tkinter application is low quality and contains extensive boilerplate consistent with possible AI assistance, but authorship method cannot be determined from the sample alone. Its Firebase reconnaissance module is functional and operationally relevant.

**Sample:** `Shadow..py` — a 3,403-line Python 3 / tkinter application measuring 153,549 bytes. Hashes are listed under Indicators and Detection Context.

### Firebase Reconnaissance Module (lines 664–2100)

Unlike many of the application's surrounding features, the Firebase scanner is functional. It implements five reconnaissance modes using conventional HTTP requests.

#### 1. Storage Bucket Scanner (line 1870)

For a supplied project ID, the module probes the following Firebase and Google Cloud endpoints:

```
https://firebasestorage.googleapis.com/v0/b/{project}.appspot.com/o
https://storage.googleapis.com/{project}.appspot.com
https://{project}.firebaseio.com
https://{project}.web.app
https://{project}.firebaseapp.com
```
It appends parameters including `prefix=`, `delimiter=/`, `maxResults=1000`, `alt=media` and `download=1`. On an HTTP 200 response, it parses returned JSON objects and lists discovered filenames.

#### 2. Firestore Scanner (line 1943)

The module probes both API versions:

```
https://firestore.googleapis.com/v1/projects/{project}/databases/(default)/documents
https://firestore.googleapis.com/v1beta1/projects/{project}/databases/(default)/documents
```
Where access controls permit unauthenticated reads, it enumerates returned document names.

#### 3. Authentication Endpoint Scanner (line 1986)

Using a supplied API key and project ID, the module checks:

```
https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key={api_key}
https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={api_key}
https://identitytoolkit.googleapis.com/v1/projects/{project}/accounts:lookup
https://securetoken.googleapis.com/v1/token?key={api_key}
```
An HTTP 400 response is treated as evidence that the endpoint is reachable and processing requests. This is a useful reachability signal, but it does not by itself prove an authentication weakness or unauthorised access.

#### 4. Realtime Database Scanner (line 2025)

The module tests several common Realtime Database paths:

```
https://{project}.firebaseio.com/.json
https://{project}.firebaseio.com/
https://{project}-default-rtdb.firebaseio.com/.json
https://{project}.firebaseio.com/users.json
https://{project}.firebaseio.com/data.json
```
Where security rules allow anonymous reads, the `/.json` endpoint can expose all readable RTDB content. The additional `users.json` and `data.json` probes target common collection names that may contain account records, telemetry, application data or configuration values.

#### 5. Website Firebase Configuration Scraper (line 2616)

The module parses website HTML and linked JavaScript bundles for the following Firebase configuration fields:

- `apiKey`
- `authDomain`
- `storageBucket`
- `databaseURL`
- `messagingSenderId`
- `appId`

It follows external `<script src="...">` references, retrieves each JavaScript file and searches bundled code for configuration values. If a `storageBucket` value is recovered, the module immediately tests whether the bucket permits public access.

### Compiled EXE Comparison

#### Relationship to the Source

`SHADOW-GHOST ULTIMATE v4.0.exe` is a PyInstaller-compiled build of the same `ShadowGhost` application. Static comparison indicates that it is an older, reduced version of `Shadow..py`, not a newer build with additional hidden capabilities.

#### Sample Comparison

| Property | Shadow..py | SHADOW-GHOST ULTIMATE v4.0.exe | 
|---|---|---|
| Packaging | tkinter source | tkinter application compiled with PyInstaller | 
| Primary class | `ShadowGhost` | `ShadowGhost` | 
| Displayed title | Defined in source | `SHADOW-GHOST ULTIMATE v4.0` | 
| Embedded source name | `Shadow..py` | `ggd.py` | 
| Python version | Not established | Python 3.14 | 
| Methods | 129 | Approximately 108 | 
| Size | 153,549 bytes | 19,348,892 bytes (18.5 MB) | 
| Embedded bytecode | Not applicable | `ggd.pyc` — 161,625 bytes | 

#### Capabilities Missing From the EXE

The Python source is the newer and more complete build. Compared with `Shadow..py`, the compiled EXE lacks:

- Banner collection
- Network discovery
- SSL scanning
- CMS user enumeration
- Reverse-DNS lookup
- Website screenshot capture
- Hotkey and full-screen controls
- Several clear and reset functions

#### Capabilities Shared by Both Builds

The Firebase scanner is materially identical in both versions:

| Service | Shared capability | 
|---|---|
| `firebasestorage.googleapis.com` | Storage enumeration | 
| `firestore.googleapis.com` | Firestore document-access checks | 
| `identitytoolkit.googleapis.com` | Authentication endpoint probing | 
| `securetoken.googleapis.com` | Token endpoint probing | 
| `PROJECT_ID.firebaseio.com/.json` | Realtime Database access check | 

Other shared modules include port scanning, directory brute-forcing, subdomain discovery, DNS utilities, CMS checks, CVE lookup, payload generation, hash cracking, cloud scanning, website scanning, packet sniffing and an interactive console.

#### Hidden-Capability Review

No additional malicious capability was identified in the compiled binary. The observed capa results are consistent with normal PyInstaller bootloader behaviour, including temporary-file extraction, process creation, zlib decompression and environment-variable handling. The reported “anti-VM Xen” match is assessed as a false positive caused by coincidental byte sequences in compressed data.

No command-and-control channel, persistence mechanism, exfiltration routine or keylogging capability was identified.

Assessment

The compiled EXE is a distribution-oriented PyInstaller package of the same application and appears less capable than the available Python source. The operationally relevant Firebase scanner is unchanged between builds, and no concealed capability was identified in the binary. File indicators for the compiled EXE are listed under Indicators and Detection Context.

### Potential Water-Sector and CNI Relevance

This is a conditional risk scenario, not evidence that the sample has already compromised or specifically targeted a water operator.

Where a utility or smaller CNI operator uses Firebase-backed monitoring, reporting or customer-facing dashboards, Shadow Ghost could support a basic exposure-discovery chain: scrape public Firebase configuration from a website, test Realtime Database and Storage access, and identify permissive rules exposing account records, telemetry, application data or deployment artefacts. The risk is misconfiguration, not Firebase itself.

### Technical Assessment

Operational status

Functional Firebase reconnaissance module embedded inside a low-quality GUI wrapper.

The Firebase functions use straightforward HTTP requests against documented Google APIs. The surrounding tkinter application remains verbose and likely AI-assisted, but the Firebase logic is conventional, functional and reusable. It matters because it lowers the bar for finding exposed Firebase backends, including those potentially used by smaller CNI operators.

## TRK-25 ICS Scanner

*Figure 30: TRK-25 as advertised on Telegram.*

### TRK-25 Static Analysis — 50508000.py

*Figure 31: The LoginWindow credential gate, version 2.5.0, build 2026.07.05. The credentials are hardcoded in the Python source and checked entirely client-side rather than validated against any server, so the LoginWindow gate only imitates an authenticated web portal. It provides no access control — anyone holding the file can read the values or strip the check — making the screen misleading rather than protective. Both values are listed under Operator-Shared Usage Instructions.*

Assessment

TRK-25 is an incomplete PyQt5 ICS attack toolkit. Much of the application is cosmetic, stubbed or non-functional; however, its HMI/SCADA discovery code, industrial fingerprinting and near-operational Modbus routines present a credible reconnaissance risk.

Scope

Code-verified findings in this section apply only to 50508000.py (SHA256 5f1ebc84cdee3a4e97c530ff2ffc907e903544b8b5b119f9de2e9bd035058629). The sample was assessed statically and was not executed. Capabilities shown only in separate paid or actor-demonstrated builds are identified as such and are not attributed to this file.

*Figure 32: The main 13-tab interface, showing the network-scan tab, the built-in 32-password list and the HMI defacement option.*

Operator demonstration video for TRK-25:

*Operator demonstration video for TRK-25.*

### Sample Overview

**Sample:** `50508000.py` — a 2,436-line Python 3 script measuring 102,400 bytes. The available file is truncated inside the `show_details` method, where an f-string ends mid-expression. It also lacks an `if __name__ == "__main__":` entry point and cannot launch as supplied.

#### Imports

`sys`, `os`, `socket`, `threading`, `time`, `random`, `json`, `struct`, `base64`, `ipaddress`, `subprocess`, `requests`, `re`, `datetime`, `PIL.ImageGrab` and the PyQt5 widget, core and GUI stacks.

#### Architecture

*Figure 33: TRK-25 class architecture.*

The sample defines eight principal classes:

| Class | Lines | Purpose | 
|---|---|---|
| `LoginWindow(QDialog)` | 36–286 | Hardcoded credential gate | 
| `HMIScannerWorker(QThread)` | 317–494 | Industrial HMI/SCADA scanning and banner collection | 
| `RiskAnalyzer` | 560–678 | Static risk scoring; no target connection | 
| `VNCAttackWorker(QThread)` | 681–830 | Network scanning and claimed VNC attack functions | 
| `DDOSAttackWorker(QThread)` | 832–935 | SYN, UDP, ICMP and HTTP flooding modules | 
| `ModbusAttackWorker(QThread)` | 937–1006 | Modbus TCP register and coil operations | 
| `S7AttackWorker(QThread)` | 1008–1048 | Claimed Siemens S7 PLC stop/start operations | 
| `TRK25AdvancedSCADA(QMainWindow)` | 1051–2436+ | Main 13-tab GUI | 

The GUI connects controls to more than ten methods that are never defined: `gen_vnc`, `gen_ssh`, `gen_rdp`, `deface_target`, `generate_full_report`, `export_all_data`, `show_menu`, `on_screenshot`, `clear_log` and `add_password`. Invoking any associated control would raise an `AttributeError`.

### Operationally Relevant ICS/CNI Capabilities

#### HMI/SCADA Port Scanner (lines 289–494)

This is the sample's most developed scanning component. It targets 20 web-management and industrial-protocol ports.

*Figure 34: SCADA/ICS scanning workflow.*

| Stage | What the code does | 
|---|---|
| 1. Target intake | Accepts a single IP, a CIDR range or a randomly generated /24; ranges are expanded with ipaddress.ip_network | 
| 2. Port scan | TCP connect through socket.connect_ex against the 20 industrial and web-management ports listed below | 
| 3. Banner collection | HTTP GET requests plus raw socket reads against each responding port | 
| 4. Fingerprinting | Matches returned banners against more than 50 OT vendor, product and protocol keywords | 
| 5. Vulnerability flagging | Six regular-expression patterns combined with port-based rules | 
| 6. Output | Populates the GUI results table; findings can be exported as JSON | 

The primary scanner port list is:

```
INDUSTRIAL_PORTS_HMI = [
    80, 443, 8080, 8443, 5000, 9090,
    102, 502, 44818, 20000, 4840, 47808,
    1500, 34962, 34963, 34964, 789, 1962,
    20547, 2404
]
```
**Protocol coverage:** Modbus/TCP (`502`), S7comm (`102`), EtherNet/IP (`44818`), DNP3 (`20000`), OPC UA (`4840`), BACnet (`47808`), PROFINET (`34962–34964`) and IEC 60870-5-104 (`2404`).

The scanner also contains more than 50 industrial vendor, product and protocol fingerprints:

```
INDUSTRIAL_KEYWORDS = [
    'FactoryTalk', 'Optix', 'Apron', 'Water Plant', 'Fixsus',
    'SCADA', 'HMI', 'PLC', 'Modbus', 'Siemens', 'Rockwell',
    'Schneider', 'GE', 'ABB', 'Yokogawa', 'Honeywell', 'Emerson',
    'Mitsubishi', 'Omron', 'Bosch', 'Phoenix Contact', 'WAGO',
    'Beckhoff', 'Codesys', 'Ignition', 'VTScada', 'ICONICS',
    'InduSoft', 'Citect', 'WinCC', 'Vijeo', 'iFIX', 'Wonderware',
    'Intouch', 'System Platform', 'AVEVA', 'Historian', 'OPC',
    'DNP3', 'BACnet', 'Profinet', 'EtherNet/IP', 'ControlLogix',
    'CompactLogix', 'S7', 'STEP7', 'TIA Portal', 'PCS7',
    'Cimplicity', 'Proficy', 'QuickPanel', 'Red Lion',
    'Maple Systems', 'Exor', 'Beijer', 'Weintek', 'Advantech', 'Moxa'
]
```
**Technical assessment:** This component is operationally credible and could identify internet-exposed ICS/SCADA interfaces.

**Blacklist filter:** attempts to suppress obvious non-ICS devices:

```
BLACKLIST_KEYWORDS = [
    'camera', 'CCTV', 'printer', 'thermostat',
    'smart TV', 'kiosk', 'POS', 'scanner'
]
```
#### Broader Industrial Port Scanner (lines 509–524)

A second, more comprehensive port dictionary used by the VNCAttackWorker:

```
INDUSTRIAL_PORTS = {
    'SCADA':    [502, 44818, 47808, 1911, 9600, 2455],
    'MODBUS':   [502, 503, 504, 505, 510],
    'OPC':      [4840, 4841, 4842, 4843, 4844],
    'PROFIBUS': [34962, 34963, 34964, 34965],
    'DNP3':     [20000, 19999, 20001, 20002],
    'S7':       [102, 103, 109, 110],
    'BACnet':   [47808, 47809, 47810],
    # Additional entries omitted
}
```
Across the complete dictionary, the network scanner covers more than 60 ports in 14 service categories: SCADA, Modbus, OPC, S7, DNP3, VNC, RDP, SSH, BACnet, HTTP, FTP, Telnet, SNMP and PROFINET.

#### Predefined CNI Scan Targets (lines 1426–1435)

Hardcoded target ranges loaded by a “Load Pre-Defined Targets” button:

```
78.136.96.0/24
65.109.54.0/24
85.236.254.0/24
31.40.20.0/24
192.168.1.0/24
10.0.0.0/24
172.16.0.0/24
192.168.0.0/24
10.10.0.0/24
172.31.0.0/24
```
The first four are public IP ranges — these are hardcoded reconnaissance targets. The remaining are RFC1918 private ranges.

#### Random Target Generation (lines 1439–1446)

The generator creates five arbitrary /24 networks for broad scanning:

```
def generate_random_targets(self):
    random_targets = []
    for _ in range(5):
        a = random.randint(1, 255)
        b = random.randint(1, 255)
        c = random.randint(1, 255)
        random_targets.append(f"{a}.{b}.{c}.0/24")
```
#### Industrial Default-Password List (lines 498–505)

```
DEFAULT_PASSWORDS = [
    '', '123456', 'admin', '12345678', '12345', 'password',
    '111111', '123123', '123456789', '1234567890', 'qwerty',
    '1qaz2wsx', 'abc123', 'root', 'toor', 'default',
    'scada', 'hmi', 'plc', 'operator', 'user', 'guest',
    'control', 'factory', 'industrial', 'siemens', 'rockwell',
    'allenbradley', 'modicon', 'schneider', 'dnp3', 'modbus'
]
```
### Why the Reconnaissance Output Matters

The OT/ICS concern is concentrated in three features: deliberate target selection, utility-oriented protocol coverage and product-level fingerprinting.

#### 1. Real-World-Specific Targeting

The four public networks are hardcoded rather than generated at runtime:

- 78.136.96.0/24
- 65.109.54.0/24
- 85.236.254.0/24
- 31.40.20.0/24

Their inclusion appears deliberate and warrants validation. If any of these ranges host exposed ICS/SCADA assets or belong to CNI operators, the assessment would shift from a generic hobbyist tool toward a targeted reconnaissance list.

Analytic priority

establish ownership, hosting context and exposed-service history for all four ranges. Their presence in the source is confirmed; their relationship to CNI environments is not yet established.

#### 2. Protocol Coverage Aligned to CNI Kill Chains

The port selection is not generic penetration-testing coverage. It is tuned to technologies encountered across operational environments.

*Figure 35: Protocol-to-CNI sector mapping.*

This mapping reflects common deployment contexts rather than exclusive use. Individual protocols can span multiple sectors and architectures.

The principal sector relationships are:

| Environment | Protocols and ports | Operational relevance | 
|---|---|---|
| Power generation and transmission | IEC 60870-5-104 (104), DNP3 (20000) | Telecontrol protocols used in substations, generation and grid operations | 
| Water and wastewater | Modbus/TCP (502), DNP3 (20000), OPC UA (4840) | Commonly deployed across treatment, pumping and SCADA environments | 
| Oil and gas | Modbus/TCP (502), OPC UA (4840), DNP3 (20000), S7comm (102) | Pipeline control, process automation, remote terminal units and mixed-vendor supervisory systems | 
| Manufacturing and process control | S7comm (102), EtherNet/IP (44818), OPC UA (4840) | Coverage across Siemens, Rockwell and mixed-vendor PLC ecosystems | 
| Building automation | BACnet (47808) | Discovery of HVAC and building-management systems | 

The combination of IEC 60870-5-104, DNP3, Modbus and S7comm is particularly notable because it spans utility telecontrol, water SCADA and major PLC ecosystems. This is more consistent with utility-sector reconnaissance than with a generic list of “SCADA ports.”

#### 3. Product-Level Fingerprinting

The keyword set identifies specific OT products and platforms, including `FactoryTalk Optix`, `VTScada`, `CompactLogix`, `TIA Portal`, `PCS7`, `WinCC` and `Ignition`. These names map to established product families with known vulnerabilities, deployment patterns and frequently encountered configuration weaknesses.

A banner match would not prove exploitability, but it would immediately narrow vulnerability research and identify the relevant technology stack. The scanner therefore automates the discovery and identification stages of the ICS attack lifecycle, producing output that can feed vulnerability triage and subsequent weaponisation.

Bottom line

TRK-25 is a reconnaissance feeder, not the weapon itself. A hypothetical result such as “[REDACTED]:502 — Modbus; WinCC 7.x” would constitute a targeting lead that could be handed directly into further technical assessment or attack planning.

### Other Claimed Capabilities

**Modbus TCP attack (lines 937–1006):** The module constructs requests for function codes `0x03` (read holding registers), `0x06` (write single register), `0x01` (read coils) and `0x05` (write single coil). The MBAP header is imperfect. Static analysis alone cannot establish whether a target would accept these frames; treat the module as near-operational and readily adaptable rather than confirmed functional.

**Siemens S7 PLC attack (lines 1008–1048):** The module sends a single hardcoded COTP/S7 PDU to TCP/102. Because the same payload is used for both “Stop PLC” and “Start PLC,” the two operations cannot be distinguished and at least one is necessarily incorrect. The advertised “Read Memory” and “Write Code” functions are logging stubs.

The embedded 33-byte payload is:

`\x03\x00\x00\x21\x02\xf0\x80\x32\x01\x00\x00\x04\x00\x00\x08\x00\x08\x00\x01\x12\x04\x11\x44\x01\x00\xff\x09\x00\x04\x00\x00\x00\x00`
Detection value

this sequence is a candidate network signature when observed on TCP/102 with corroborating COTP/S7 context. It should not be treated as a standalone IOC.

**DDoS module (lines 832–935):** Six modes are advertised, but several are technically flawed. The “SYN flood” completes normal TCP handshakes; UDP sends 1 KB of random data; the ICMP modes require elevated privileges; and the Slowloris routine closes connections too quickly to sustain the technique.

**VNC brute-force (lines 795–810):** The `try_vnc_attack` method is non-functional. It treats a successful TCP connection as successful authentication and never implements the VNC/RFB authentication exchange.

**HMI defacement:** The GUI exposes a “Deface HMI Interface (Replace Screen)” option, but the associated `deface_target` method is undefined.

### Code-Quality Assessment

The sample contains strong indicators of generated or copy-pasted assembly, including patterns consistent with possible AI assistance. Source structure alone cannot establish how the code was authored. The evidence includes:

1. **Fixed-boundary truncation:** the file ends at exactly 102,400 bytes, midway through an f-string in show_details. The round boundary is consistent with an export, collection or generation cutoff, although it is not independently conclusive evidence of LLM output.
2. **Undefined callbacks:** more than ten methods are referenced by PyQt .connect() calls but never defined, causing runtime failures.
3. **No entry point:** the script lacks an`if __name__ == "__main__":` block and cannot launch as supplied.
4. **UI-heavy composition:** approximately 60% of the available source consists of PyQt5 stylesheet definitions and cosmetic interface code.
5. **Superficial VNC logic:** a TCP connection is incorrectly treated as successful VNC authentication.
6. **Duplicated S7 payloads:** identical bytes are assigned to conflicting stop and start operations.
7. **Incorrect SYN-flood logic:** the implementation performs complete TCP handshakes rather than transmitting raw SYN packets.

#### Components With Credible Functionality

- HMI/SCADA banner collection and exposure discovery through HMIScannerWorker
- Near-operational Modbus TCP register and coil operations
- Basic but effective TCP connect scanning
- CIDR expansion through Python's ipaddress module
- Industrial keyword matching and vulnerability-oriented regular expressions

### Notable Strings and Metadata

- **Group identifier:**`BLACKNET-00黑手党` (“BLACKNET-00 Mafia”)
- **Build date:**`2026.07.05`
- **Window title:**`TRK25 ADVANCED SCADA`
- **Copyright:**`2026 TRK25 ADVANCED SCADA` (line 260)
- **Login warning:** “This platform is designed for hacking and disabling industrial systems and critical infrastructure. Use at your own risk — unauthorized access is a punishable crime.”
- **Status labels:**`HACK` ,`SCAN` and`DISABLE` on login;`ONLINE` ,`SCANNING` and`ALERT` in the main interface
- **Unimplemented impact labels:** “Hardware damage,” “System shutdown,” “PLC logic manipulation” and “Utility system control” appear as interface text rather than working capabilities
- **Suite context:**`50508000.py` was stored alongside`blacknet-00..exe` and`SHADOW-GHOST ULTIMATE v4.0.exe` , supporting its presentation as part of a broader BLACKNET toolset

### Overall Assessment

Threat rating: MEDIUM

TRK-25 presents a low risk as a standalone weapon, but its CNI reconnaissance components are credible, readily reusable and suitable for scanning exposed SCADA environments.

#### Standalone Weapon Capability — Low

TRK-25 is not a credible standalone weapon in its current form. The sample cannot launch because it is truncated mid-function and lacks an `if __name__ == "__main__":` entry point. More than ten GUI controls reference undefined methods and would fail immediately if invoked.

Its advertised attack functions are similarly unreliable: the VNC routine performs only a TCP connection and treats that as successful compromise; the S7 module sends identical bytes for both stop and start operations; and the claimed SYN flood completes a normal TCP handshake. The result is consistent with generated or copy-pasted assembly that prioritised a polished PyQt5 interface over functional internals; the available source does not establish whether an LLM was used.

#### CNI Reconnaissance Capability — Medium

The reconnaissance components are the substantive concern:

- A functional scanner targets 20 web-management and ICS-oriented ports spanning Modbus, S7comm, DNP3, OPC UA, BACnet, IEC 60870-5-104, EtherNet/IP and PROFINET.
- More than 50 precise OT vendor and product fingerprints include FactoryTalk Optix, VTScada and CompactLogix. Their specificity suggests OT domain knowledge or adaptation from established ICS tooling rather than generic LLM generation.
- Four public /24 networks are embedded as preloaded scan targets.
- A random-target function generates arbitrary /24 CIDR ranges for broad scanning.
- The source contains 32 default-password candidates, including ICS-specific terms such as scada, hmi, plc, siemens, rockwell and modicon.
- The Modbus register and coil read/write logic is close enough to valid protocol framing to be readily adapted, but it was not dynamically validated against a device.

#### Intelligence Significance

The primary risk is not the supplied PyQt5 application itself. An actor with basic Python proficiency could extract the relatively small functional core—approximately 200 lines of scanning and protocol logic—and integrate it into a working tool. The industrial port mappings, vendor fingerprints and target-generation logic therefore have greater intelligence value than the broken wrapper around them.

#### Confidence Assessment

- **High confidence:** The available sample is incomplete, non-launchable and contains extensive generated or copied boilerplate.
- **Medium confidence:** The industrial keyword sets, protocol-port mappings and Modbus framing were human-curated or adapted from existing ICS security tooling. Specific references such as FactoryTalk Optix, VTScada and CompactLogix indicate domain familiarity or sourcing beyond generic GUI generation.

### Operator-Shared Usage Instructions

The following execution steps and credentials were distributed alongside the tool.

#### Execution

```
cd C:\Users\Mega Store\Desktop
python 50508000.py
```
#### Hardcoded Login

| Field | Value | 
|---|---|
| Username | `BLACKNET-00黑手党` | 
| Password | `TRK25 ADVANCED SCADA` | 

The commands are reproduced as shared by the operator. The Windows path contains a space and may require quotation marks when entered manually.

## Analytic Gaps and Collection Priorities

1. Acquire and hash the separate paid TRK25-ADVANCED build, then compare its code and capabilities with 50508000.py.
2. Establish ownership, hosting context and historical OT exposure for the four embedded public /24 ranges; coordinate responsible disclosure before wider publication of confirmed vulnerable assets.
3. Identify any Telegram bot token, chat identifier or destination URL used by generated BLACKNET payloads.
4. Validate control and transaction history for the ZixiPay-presented TRON address without assuming beneficial ownership from service attribution alone.
5. Preserve source-channel identifiers, post timestamps and archived copies for material claims so future reporting can distinguish deletion, alteration and reposting.

## Indicators and Detection Context

Consolidated indicator record for this report — builder, Shadow Ghost and TRK-25 indicators are all collected here. Shared infrastructure such as Telegram, Firebase and Google API domains is not malicious on its own; use it only with corroborating tooling strings, hashes, behaviours or actor-specific context.

### Sample Hashes

| Sample | SHA256 | SHA1 | MD5 | 
|---|---|---|---|
| `blacknet-00..exe` — BLACKNET-00 builder | `10e41edc96bafe6511a06832519823d0a1bf329fecde1d7d2ab9b2eda3a27a09` | `974d8934bd369e98d3e282b2cd3cfe56f6f12ec6` | `9feebfea9b7a983b8d21757ac0d96015` | 
| `Shadow..py` — Shadow Ghost source | `90c447f864f4d66a6b99a76af0db4debf12735ebc3e35525936a4232b2df5732` | `25029760457873fe8339736534f184cea0b20535` | `f6cf915e5c2864b7ccff0a57a504dffc` | 
| `SHADOW-GHOST ULTIMATE v4.0.exe` — compiled Shadow Ghost | `85adbf2a80b13a55e19114203af3151b0fa9aaef195b316a7b18b571994be21a` | `7cf1272de9e478464807e890c68c94600930e724` | `6c3446e26d566657ea019ca1b37156d6` | 
| `50508000.py` — TRK-25 ICS scanner | `5f1ebc84cdee3a4e97c530ff2ffc907e903544b8b5b119f9de2e9bd035058629` | `18e14a1e9ba76fa8c7f89e14ea971c11307af23b` | `28c62e5e820de249ddfb9204fec31bbc` | 

#### Fuzzy and Import Hashes

| Sample | Imphash | SSDeep | 
|---|---|---|
| `blacknet-00..exe` | `351592d5ead6df0859b0cc0056827c95` | `786432:9Y0W0b4QL0LW8kIYFrHFF9W+NjKVP1U37u48MGh29kEVdg0QS8ouA:9YxhQL0LW0YFzFF9NN3rx82/QS8C` | 
| `SHADOW-GHOST ULTIMATE v4.0.exe` | `351592d5ead6df0859b0cc0056827c95` | `393216:QlcFTJasgIfUKOcgx/hqWbdXQfM6R4RmhH7fOHsnvDwHB8tf1:4cVJN58KPgxvYMc3ogEHm/` | 

Do not pivot on the shared imphash

Both executables return 351592d5ead6df0859b0cc0056827c95 because they are PyInstaller-packed — the import table belongs to the bootloader, not to the authors' code. It matches large numbers of unrelated PyInstaller binaries and is not evidence of shared authorship.

File metadata: `blacknet-00..exe` — 34,669,202 bytes, PE32+ x86-64, PyInstaller, UPX-packed, Python 3.13. `SHADOW-GHOST ULTIMATE v4.0.exe` — 19,348,892 bytes, PE32+ x86-64, PyInstaller, UPX-packed, Python 3.14, MSVC 14.44. `Shadow..py` — 153,549 bytes. `50508000.py` — 102,400 bytes.

### Host and Persistence Artifacts

| Type | Indicator | Context | 
|---|---|---|
| Mutex | `Global\BlackNetMutex` | Single-instance marker | 
| Registry Run value | `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\WindowsUpdate` | Logon persistence | 
| Scheduled task | `WindowsUpdate` | On-logon persistence | 
| Ransom note | `%USERPROFILE%\Desktop\READ_ME_BLACKNET.txt` | Includes the decryption key in the default build | 
| Wallpaper | `%TEMP%\blacknet_wall.bmp` | Ransom wallpaper | 
| Screenshot | `%TEMP%\screenshot_blacknet.bmp` | Captured prior to Telegram submission | 
| Encrypted extension | `.blacknet` | Appended to targeted files | 
| Window class | `BlackNetRansomClass` | Ransom-interface identifier | 
| IFEO redirect | `systray.exe` | Image File Execution Options debugger redirect used to block PowerShell | 

### Network and Behavioural Indicators

| Indicator | Context | 
|---|---|
| Telegram submission through WinHTTP | Victim data, screenshots and the decryption key are included in outbound reporting | 
| `BlackNet/1.0` | Generated payload User-Agent | 
| `vmwaretray.exe` ,`vboxservice.exe` | Minimal virtualisation checks | 
| `ShellExecuteW` with`runas` | UAC elevation request; not a bypass | 
| `taskkill` against 15 security and analysis processes | Defence evasion prior to encryption | 

Telegram itself is legitimate shared infrastructure. Without an associated bot token, chat identifier or destination URL, the use of Telegram should be treated as a behavioural indicator rather than a standalone network IOC.

### Actor, Contact and Payment Identifiers

| Type | Indicator | Context | 
|---|---|---|
| Telegram account | `@blacknetransom` | Primary BLACKNET-00 ransomware persona | 
| Telegram account | `@xonsee666` | Second operator; presented as the primary operator's brother | 
| Telegram channel | `@infrastructurek` | Infrastructure Destruction Squad channel | 
| Telegram channel | `@Ransomwareg` | Ransomware-branded channel | 
| Telegram account | `@zzzzzzzzkss` | Continuity account; status not independently verified | 
| Telegram account | `@ayeowetee` | Continuity account; status not independently verified | 
| Telegram channel (third party) | `@rippersecchat` | Pro-Russian channel that attributed an August 2026 DDoS attack to BLACKNET-00; not operator-controlled | 
| Criminal forum | Breach Forums | Advertising venue for services and tooling | 
| Criminal forum | pwnforums | Advertising venue for initial-access listings | 
| TOX ID | `05a63a33e6233cdfe2a86a49aa73148af13ab6068db82c93690827da75e64d422b` | Shared for use after channel or account takedown | 
|  | [\[email protected\]](https://ransom-isac.org/cdn-cgi/l/email-protection#4f082e3c7a79242e3c3b2a3d797a78790f3f3d203b202161222a) | Builder default contact | 
|  | [\[email protected\]](https://ransom-isac.org/cdn-cgi/l/email-protection#2f4d434e4c44414a5b1f1f576f48424e4643014c4042) | Generated C++ payload contact | 
| TRON (TRC-20) | `TS7cmQrHcRtLuijLdL3CP7s5EgeN6tn7KT` | Receiving address; associated with ZixiPay | 
| Bitcoin | `13TSahvLK6EGene38RQWzfUfQKkpqtRoL6` | Builder default wallet | 
| Bitcoin | `1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa` | **Not an indicator.** Bitcoin genesis-block coinbase address; do not block, report or ingest | 

### Associated and Solicited Groups

| Group | Nexus | Observed relationship | 
|---|---|---|
| CARR — Cyber Army of Russia Reborn | Russia | Named in Ransom-ISAC's April 2026 advisory as a TRK-25 purchaser | 
| Z-Pentest Alliance | Russian hacktivist | Solicited directly by the operators as a TRK-25 buyer | 
| ‘313 Team’ | Iraq | Solicited directly by the operators as a TRK-25 buyer | 
| HEXVIOR | Iran | Offered TRK-25 for sale | 
| Blackout DDoS | Pro-Palestinian | Third-party channel claims BLACKNET-00 conducted a DDoS attack on its behalf; unverified | 

Relationship indicators drawn from operator claims and channel postings. Solicitation is not evidence that a sale completed or that any listed group deployed the tool.

### Builder Defaults and Identifying Strings

| Type | Indicator | Context | 
|---|---|---|
| Ransom-screen password | `BLACKNET2000` | Embedded access value | 
| Author string | `BLACKNET-00` | Builder branding | 

```
BLACKNET-00
BLACKNET-00 ULTIMATE RANSOMWARE CONSTRUCTION KIT v10.0
BlackNet/1.0
Global\\BlackNetMutex
BlackNetRansomClass
```
### TRK-25 Hardcoded Indicators

#### Public Scan Targets

| CIDR | Context | 
|---|---|
| `78.136.96.0/24` | Hardcoded public scan range | 
| `65.109.54.0/24` | Hardcoded public scan range | 
| `85.236.254.0/24` | Hardcoded public scan range | 
| `31.40.20.0/24` | Hardcoded public scan range | 

These networks are targets embedded in the source, not confirmed operator infrastructure.

#### Credentials

- **Username:**`BLACKNET-00黑手党` — 黑手党 translates to “Mafia” in Chinese
- **Password:**`TRK25 ADVANCED SCADA`

#### Version and Build

- **Version:**`2.5.0`
- **Build:**`2026.07.05`

#### S7 Payload

`\x03\x00\x00\x21\x02\xf0\x80\x32\x01\x00\x00\x04\x00\x00\x08\x00\x08\x00\x01\x12\x04\x11\x44\x01\x00\xff\x09\x00\x04\x00\x00\x00\x00`
Candidate network signature on TCP/102 with corroborating COTP/S7 context; not a standalone IOC.

#### Referenced Vulnerability

| Reference | Name | Context | 
|---|---|---|
| `CVE-2019-0708` | BlueKeep | Referenced in exploit-method text only; no working implementation was identified | 

This is a code reference, not evidence that TRK-25 implements or successfully exploits BlueKeep.

#### Unique Industrial Ports

`102`, `502–505`, `510`, `789`, `1500`, `1911`, `1962`, `2404`, `2455`, `4840–4844`, `9600`, `20000`, `20547`, `34962–34965`, `44818`, `47808–47810`

## Detection Rules

Four YARA rules provide complementary coverage: sample-specific detection, behaviour-based ICS and Firebase reconnaissance hunting, and broad BLACKNET suite branding.

### 1. TRK25_SCADA_Tool

```
rule TRK25_SCADA_Tool {
    meta:
        description = "TRK-25 Advanced SCADA - ICS recon tool by Infrastructure Destruction Squad"
        author = "Ransom-ISAC"
        threat_group = "Infrastructure Destruction Squad"
        tlp = "CLEAR"
        sha256 = "5f1ebc84cdee3a4e97c530ff2ffc907e903544b8b5b119f9de2e9bd035058629"
        sha1 = "18e14a1e9ba76fa8c7f89e14ea971c11307af23b"
        md5 = "28c62e5e820de249ddfb9204fec31bbc"
    strings:
        $id1 = "TRK25 ADVANCED SCADA" ascii wide
        $id2 = "BLACKNET-00" ascii wide
        $id3 = "TRK25AdvancedSCADA" ascii
        $id4 = "HMIScannerWorker" ascii
        $id5 = "INDUSTRIAL_PORTS_HMI" ascii
        // BLACKNET-00黑手党 in raw UTF-8
        $cred1 = {42 4C 41 43 4B 4E 45 54 2D 30 30 E9 BB 91 E6 89 8B E5 85 9A}
        $port1 = "44818" ascii
        $port2 = "47808" ascii
        $port3 = "34962" ascii
        $port4 = "20000" ascii
        $pw1 = "allenbradley" ascii
        $pw2 = "modicon" ascii
        $pw3 = "schneider" ascii
        $keyword1 = "FactoryTalk" ascii
        $keyword2 = "VTScada" ascii
        $keyword3 = "CompactLogix" ascii
        $keyword4 = "ControlLogix" ascii
    condition:
        filesize < 500KB and
        (
            any of ($id*) or
            $cred1 or
            (3 of ($port*) and 2 of ($pw*)) or
            (3 of ($keyword*) and any of ($port*))
        )
}
```
### 2. Generic_ICS_Recon_Script

```
rule Generic_ICS_Recon_Script {
    meta:
        description = "Python script with ICS/SCADA scanning capabilities - catches TRK-25 variants and similar tools"
        author = "Ransom-ISAC"
        tlp = "CLEAR"
    strings:
        $lang1 = "import socket" ascii
        $lang2 = "import struct" ascii
        $lang3 = "connect_ex" ascii
        $proto1 = "MODBUS" ascii nocase
        $proto2 = "S7comm" ascii nocase
        $proto3 = "DNP3" ascii nocase
        $proto4 = "BACnet" ascii nocase
        $proto5 = "OPC" ascii nocase
        $proto6 = "Profinet" ascii nocase
        $proto7 = "IEC" ascii nocase
        $vendor1 = "Siemens" ascii
        $vendor2 = "Rockwell" ascii
        $vendor3 = "Schneider" ascii
        $vendor4 = "Honeywell" ascii
        $vendor5 = "Yokogawa" ascii
        $vendor6 = "Emerson" ascii
        $scan1 = "grab_banner" ascii
        $scan2 = "check_port" ascii
        $scan3 = "scan_target" ascii
        $pw1 = "scada" ascii
        $pw2 = "plc" ascii
        $pw3 = "hmi" ascii
    condition:
        filesize < 1MB and
        all of ($lang*) and
        3 of ($proto*) and
        2 of ($vendor*) and
        any of ($scan*) and
        2 of ($pw*)
}
```
### 3. BLACKNET_Suite

```
rule BLACKNET_Suite {
    meta:
        description = "BLACKNET tooling suite - catches any tool from Infrastructure Destruction Squad"
        author = "Ransom-ISAC"
        tlp = "CLEAR"
    strings:
        $s1 = "BLACKNET" ascii wide nocase
        $s2 = "SHADOW-GHOST" ascii wide nocase
        $s3 = "Infrastructure Destruction" ascii wide nocase
        $s4 = "TRK25" ascii wide nocase
        $s5 = "BLACKNET-00" ascii wide
        $s6 = {E9 BB 91 E6 89 8B E5 85 9A}  // 黑手党 (Mafia) UTF-8
    condition:
        any of them
}
```
### 4. BLACKNET_Firebase_Scanner

```
rule BLACKNET_Firebase_Scanner {
    meta:
        description = "Firebase misconfiguration scanner from the BLACKNET/Shadow suite"
        author = "Ransom-ISAC"
        tlp = "CLEAR"
        sha256 = "90c447f864f4d66a6b99a76af0db4debf12735ebc3e35525936a4232b2df5732"
    strings:
        $fb1 = "firebasestorage.googleapis.com/v0/b/" ascii
        $fb2 = ".firebaseio.com/.json" ascii
        $fb3 = "firestore.googleapis.com/v1/projects/" ascii
        $fb4 = "identitytoolkit.googleapis.com" ascii
        $fb5 = "securetoken.googleapis.com" ascii
        $fb6 = ".appspot.com/o" ascii
        $config1 = "apiKey" ascii
        $config2 = "authDomain" ascii
        $config3 = "storageBucket" ascii
        $config4 = "databaseURL" ascii
        $config5 = "messagingSenderId" ascii
        $scan1 = "log_firebase" ascii
        $scan2 = "check_firestore" ascii
        $scan3 = "check_rtdb" ascii
        $scan4 = "check_storage" ascii
        $id1 = "BLACKNET" ascii wide nocase
        $id2 = "Shadow" ascii
    condition:
        filesize < 500KB and
        (
            (3 of ($fb*) and 2 of ($config*)) or
            (3 of ($scan*) and any of ($id*)) or
            4 of ($fb*)
        )
}
```
Use this rule for hunting and triage. Firebase endpoint and configuration strings are common in legitimate applications, so matches should be validated against file context and accompanying BLACKNET identifiers.

### Coverage Summary

| Rule | Coverage | Primary use | 
|---|---|---|
| `TRK25_SCADA_Tool` | Identifiers, credentials, port combinations, default-password terms and product fingerprints | Sample-specific detection and close-variant triage | 
| `Generic_ICS_Recon_Script` | Python scanning primitives combined with industrial protocols, vendors and credential terms | Behaviour-based hunting for related ICS reconnaissance scripts | 
| `BLACKNET_Suite` | BLACKNET, SHADOW-GHOST, TRK25 and Infrastructure Destruction Squad branding | Broad suite-level hunting and triage | 
| `BLACKNET_Firebase_Scanner` | Firebase endpoints, configuration fields, scanner methods and BLACKNET/Shadow identifiers | Shadow Ghost Firebase reconnaissance hunting | 

The generic and branding rules are intended for hunting and triage. Validate matches against surrounding file context because broad protocol, vendor and branding strings can produce false positives.

Facing a cyber security incident?

If you believe your organisation has been compromised by BLACKNET-00 or a related actor, please reach out to Ransom-ISAC.
