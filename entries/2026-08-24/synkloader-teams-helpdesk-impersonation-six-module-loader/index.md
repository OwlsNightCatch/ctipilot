---
schema: 1
kind: threat
title: "SynkLoader: a Teams message from a lookalike tenant, an MSI called 'PowerShell Cleaner', and a six-module toolkit whose fake lock screen harvests the domain password its own tunnel then uses from the victim's IP"
headline: "SynkLoader pairs a fake Windows lock screen with a backconnect proxy, so the stolen domain password is used from the victim's own address"
summary: >
  Expel documented SynkLoader on 2026-08-20, a previously unidentified loader delivered by Microsoft Teams message
  from a company-styled onmicrosoft.com address impersonating the target's own IT service desk, which talks the user
  into installing an MSI presented as a "PowerShell Cleaner" hosted on Azure blob storage. Six modules blend Python,
  PowerShell, C# and C++ — some using three languages at once: a system profiler that counts Active Directory-joined
  computers, an in-memory DLL loader, PhishLocker (a counterfeit Windows lock screen that harvests the domain
  password), TrafficRedirector (a backconnect proxy), an interactive shell, and a screen-streaming module. The
  load-bearing combination is the harvested password plus the tunnel: Expel states the operator can then sign in to
  internal and external company systems without triggering alerts based on logins from unknown addresses or
  geolocations. Expel assesses at low-to-medium confidence that the toolkit belongs to a ransomware group or an
  access broker selling to one.
discovered_at: "2026-08-24T09:13:00Z"
event_date: "2026-08-20"
run_id: 2026-08-24T0410Z-intel
priority: high
immediate_action: null
tags: [phishing, identity, infostealer, ransomware, organized-crime, cloud]
regions: [global, europe]
sectors: [public-sector, technology, finance]
entities:
  - malware:synkloader
techniques: [T1566.003, T1684.001, T1204.002, T1036.005, T1620, T1059.001, T1056.002, T1090, T1113, T1082, T1057, T1007, T1018, T1078, T1584.006, T1053.005]
affected_products: ["Microsoft Teams"]
cves: []
sources:
  - url: "https://expel.com/blog/synkloader-when-you-throw-in-everything-but-the-kitchen-sink/"
    publisher: "Expel"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence:
  - quote: "The loader ships a long chain of attack tools, which bridge multiple separate programming languages, with some modules using as many as three programming languages at once."
    publisher: "Expel"
  - quote: "It can enable the threat actors to connect to internet services using the infected machine IP address, bypassing corporate IP allow-listing."
    publisher: "Expel"
  - quote: "When combined with the system password phishing model, threat actors can use the infected user’s username and password to log into both internal and external company systems, all without triggering alerts based on logins from unknown IPs or geolocations."
    publisher: "Expel"
verification: single-source
sourcing_note: >
  Single-source: Expel is the discovering party and no other publisher has covered this toolkit. The account is
  first-hand incident work — Expel found it on 2026-08-18 while investigating an EDR alert on a scheduled task,
  reverse-engineered the loader, then ran a modified build that logged rather than executed the operator's commands
  and fed back fabricated system and network details to draw the operator into a hands-on-keyboard session. The
  ransomware-or-access-broker assessment is Expel's own and is carried at its stated low-to-medium confidence. One
  claim circulating with this research — that Microsoft had earlier flagged Teams help-desk impersonation as
  increasingly common — appears nowhere in Expel's article and is not carried here. Independent corroboration of the
  delivery pattern, though not of this toolkit, arrived the same week from a national authority: Switzerland's BACS
  describes the same email-bombing-then-Teams-help-desk-impersonation chain in its half-year report.
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
actions:
  - "Restrict external and cross-tenant Microsoft Teams chat to an allow-list of federated domains, or disable it — the delivery depends on an unsolicited message from an outside tenant reaching an end user, and this is a tenant setting rather than a detection."
migrated_from: null
---

Expel published an analysis on 2026-08-20 of **SynkLoader**, a loader it found on 2026-08-18 while investigating an endpoint-detection alert on a scheduled task in a client network, and for which it could find no prior public reference ([Expel, 2026-08-20](https://expel.com/blog/synkloader-when-you-throw-in-everything-but-the-kitchen-sink/)). The name is a play on its breadth — Expel describes it as an "everything but the kitchen sink" approach — and the reason it belongs in front of a public-sector defender is the delivery, not the tooling: the operator arrives over **Microsoft Teams**, from a `<username>@<company>.onmicrosoft.com` address (the default mail domain Microsoft 365 assigns a tenant), posing as the target's own **IT service desk** under a fabricated staff name, and persuades the user to download and install an MSI presented as a "PowerShell Cleaner" and hosted on Azure blob storage — giving the download the appearance of coming from Microsoft. That inverts the direction staff are trained to be suspicious in: the lure is not an external email but an internal-looking chat from support.

Six modules follow, and Expel notes the chain "ships a long chain of attack tools, which bridge multiple separate programming languages, with some modules using as many as three programming languages at once." A **system profiler** loads a C# module carrying the name of a Microsoft Visual C++ runtime library, which exports functions to run PowerShell in memory through an embedded Python interpreter, and collects hostname, current user, privilege level, running processes, installed services, the Active Directory domain name and — the detail Expel leans on — a **count of AD-joined computers**. A **persistence module** is reached through a second fake-runtime-named DLL that maps libraries into memory without writing them to disk, and the way it installs its scheduled task is a deliberate evasion rather than an implementation detail: Expel documents it registering the task through the Task Scheduler **COM interface** rather than the command-line utility, specifically to sidestep behavioural detections that inspect command-line arguments or watch for the scheduled-task binary being invoked. That matters for hunting, because the usual high-value signal — a suspicious `schtasks` command line — is exactly what this build avoids producing. **PhishLocker** renders a counterfeit full-screen Windows lock screen to steal the user's system login credentials, going as far as retrieving the machine's real lock-screen background image from its own on-disk location and re-focusing itself to defeat Alt+Tab; Expel's analysis host gave it away because the fake mimicked Windows 11 while the machine ran Windows 10, producing visible mismatches in clock and icon placement, password-box theming and the absence of the background blur Windows applies when the password prompt has focus. **TrafficRedirector** is a backconnect proxy using a protocol resembling HTTP CONNECT: it dials out to the operator, waits for an address and port, and then forwards traffic — which Expel states "can enable the threat actors to connect to internet services using the infected machine IP address, bypassing corporate IP allow-listing," and equally lets the operator reach internal services that only listen on the LAN. An **interactive shell** polls one endpoint for commands and posts results to another. A **screen-streaming module** written in Python connects outward rather than listening, compresses screenshots and forwards mouse and keyboard input into the live session — notably *not* a hidden-desktop implementation, so the activity would be visible to a logged-on user; Expel assesses from its unusually formal comments and the absence of any matching open-source project that it was likely AI-assisted.

The two halves that matter together are PhishLocker and TrafficRedirector. Expel's own framing: "When combined with the system password phishing model, threat actors can use the infected user's username and password to log into both internal and external company systems, all without triggering alerts based on logins from unknown IPs or geolocations." A cleartext domain password is also worth more than a hash here because single sign-on turns it into access across every federated application, without the constraints of pass-the-hash or Kerberos relay. Expel assesses at low-to-medium confidence that the toolkit belongs to a ransomware group or an initial-access broker selling to one, resting that on the AD-computer count — which matters most to an actor whose profit scales with the size of the network it disrupts — and on the loader's resemblance to others previously used by such groups. Build timestamps place the components around late July 2026, and one module's debug path leaked the developer's local account name.

**Defender takeaway:** the strongest control here is a tenant configuration rather than a detection, because the chain depends on an unsolicited external Teams message reaching a user at all — restricting or disabling external and cross-tenant Teams chat removes the delivery path outright, and an allow-list of genuinely federated partner domains is usually workable. Where the message does land, the highest-value telemetry is not the MSI but the two later stages: an outbound, long-lived connection from a workstation that then carries inbound-initiated traffic to internal services is the proxy, and a successful interactive logon from an internal workstation's own address to systems that user has no history of reaching is the stolen password in use — which is exactly the case an unknown-location rule will not raise. Because the profiler enumerates AD domain and machine counts from a standard user context, an unusual burst of domain and host enumeration from a single workstation shortly after a Teams conversation with an external tenant is a good pivot.

**Triage:** a real IT service desk contacting a user over Teams and asking them to install something is not unusual, which is what makes this work — the discriminators are tenant and provenance, not behaviour. Genuine internal support messages come from a sender inside the organisation's own verified domain, not from an `onmicrosoft.com` default-domain address belonging to a different tenant, and genuine software arrives through the organisation's own management or software-distribution channel rather than as an operator-supplied link to consumer-facing cloud storage. On the endpoint, an MSI that installs an embedded Python interpreter and DLLs bearing Visual C++ runtime names outside a legitimate application directory is the anomaly; the runtime names are the masquerade, so the signal is the location and the installing parent, not the filename. For the lock-screen module, the honest discriminator is that Windows never asks a user to re-authenticate through a newly launched application: a full-screen credential prompt whose owning process is not the operating system's own logon UI is a fake, and a mismatch between the rendered lock-screen style and the host's actual Windows version is what exposed this one.
