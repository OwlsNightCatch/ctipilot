---
schema: 1
kind: threat
horizon: operational
title: "Three Russian-nexus clusters are taking European government, defence and academic accounts without defeating multi-factor authentication once — by walking the target through a genuine login, a genuine app password, or a genuine WhatsApp device link"
headline: "Every step is a vendor-designed flow completed voluntarily by the victim, and the accounts are usually personal ones the organisation cannot see"
summary: >
  Google Threat Intelligence Group published an analysis on 2026-08-20 of three separately tracked
  suspected Russian espionage clusters — UNC6293, UNC7005 (which GTIG states is also tracked as
  STORM-2945) and UNC5976 — targeting academia, aerospace and defence, governments and think tanks across
  Europe and the United States. None of them breaks authentication: each drives the target through a
  legitimate flow and takes what falls out. The methods are app-specific passwords typed into a
  convincing form, Microsoft and WhatsApp device-code phishing behind spoofed conference-registration
  pages, a real WhatsApp device-link QR displayed to the victim followed by a fake voice call that records
  camera and microphone, and OAuth logins that redirect into attacker-owned unverified cloud projects
  whose scripts lift the token out of the redirect URL. GTIG's own framing of the defensive problem is the
  most useful part: the targeted accounts are usually personal rather than corporate, so the organisation
  has telemetry on neither the lure nor the compromise.
discovered_at: "2026-08-22T05:09:00Z"
event_date: "2026-08-20"
run_id: 2026-08-22T0410Z-intel
priority: high
immediate_action: null
tags: [nation-state, espionage, phishing, identity, cloud, infostealer, ai-abuse, russia-nexus]
regions: [europe, us]
sectors: [public-sector, education, defense]
entities: [actor:unc6293, actor:unc5976, actor:storm-2945, actor:midnight-blizzard, tool:chocoshell-powershell-stealer, campaign:captivecrunch-storm-2945-hospitality-wifi, malware:headrush, malware:enginelight]
techniques: [T1566.001, T1566.002, T1204.001, T1204.002, T1684.001, T1528, T1550.001, T1556.006, T1098.005, T1671, T1123, T1125, T1041, T1555.003, T1539, T1497.001, T1583.001, T1583.006, T1585.002, T1137.006, T1059.001, T1588.001, T1588.007, T1090.002, T1078.004]
affected_products: ["Google Workspace", "Google Cloud", "Microsoft 365", "Microsoft Entra ID", "WhatsApp", "Microsoft Excel"]
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia/"
    publisher: "Google Threat Intelligence Group"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence:
  - quote: "Google Threat Intelligence Group (GTIG) is tracking three distinct suspected Russian cyber espionage threat clusters abusing legitimate authentication flows to target individuals working in academia, aerospace and defense, governments and think tanks across Europe, as well as academia and think tanks within the United States."
    publisher: "Google Threat Intelligence Group"
  - quote: "GTIG assesses with high confidence that these three threat clusters - UNC6293, UNC7005, and UNC5976 - possess a Russian nexus, based on high-level targeting patterns, phishing themes, and shared operational techniques."
    publisher: "Google Threat Intelligence Group"
  - quote: "We assess with moderate confidence that UNC6293 is a sub cluster of ICE RELIC (formerly APT29) responsible for initial access operations"
    publisher: "Google Threat Intelligence Group"
  - quote: "UNC7005 (aka STORM-2945) is a threat cluster identified in February 2026 that primarily targets academia, diplomatic, and nonprofit personnel across Ukraine, Western Europe, and the US"
    publisher: "Google Threat Intelligence Group"
  - quote: "In cases of app password phishing, attackers attempt to convince targets to set specific app passwords on their accounts, which the attackers then use to gain access to those accounts without needing two-factor authentication (2FA)."
    publisher: "Google Threat Intelligence Group"
  - quote: "While in 2025, the attacker requested that the victims share the app password back to them via email, in these newer operations, the attacker asked for it to be entered into an authentication form on an otherwise legitimate looking website."
    publisher: "Google Threat Intelligence Group"
  - quote: "UNC7005 also conducts device code phishing operations for both Microsoft and WhatsApp accounts."
    publisher: "Google Threat Intelligence Group"
  - quote: "The phone number is used to create a legitimate WhatsApp device link request with the attacker device, and then displays the legitimate QR and linking code to the target alongside instructions to the user to link their device."
    publisher: "Google Threat Intelligence Group"
  - quote: "If the target joins the voice call, malicious JavaScript to record target audio and video is triggered. The webpage presents a fake voice call with a ring for a limited amount of time while the audio and video are recorded."
    publisher: "Google Threat Intelligence Group"
  - quote: "If the target authenticates, they are redirected to an attacker-controlled, testing mode, unverified cloud project which is likely used to steal authentication tokens that grant the attacker access to the target account."
    publisher: "Google Threat Intelligence Group"
  - quote: "After authenticating, the target was redirected to a Google Cloud project URL. The cloud project hosted malicious scripts that retrieve the authentication token from the URL and save it for the operator to later retrieve."
    publisher: "Google Threat Intelligence Group"
  - quote: "Beginning on July 31, 2026, UNC7005 registered domains spoofing the legitimate Finnish Operations Center (FOC), which supports Finnish companies in the defense and security markets, specifically in the context of the North Atlantic Treaty Organization (NATO)."
    publisher: "Google Threat Intelligence Group"
  - quote: "UNC5976 distributed this malware using a domain that impersonated a research institute in Ukraine and may have targeted a Ukrainian aerospace and imaging company."
    publisher: "Google Threat Intelligence Group"
  - quote: "GTIG now assesses that UNC5976 is migrating away from Google infrastructure to other providers to host part of their phishing infrastructure."
    publisher: "Google Threat Intelligence Group"
  - quote: "The accounts these groups target are often personal, rather than corporate domain-joined accounts, creating a visibility gap for monitoring compromise from an organizational perspective."
    publisher: "Google Threat Intelligence Group"
  - quote: "Establish routine device audit checks for “linked devices” on both corporate and personal devices"
    publisher: "Google Threat Intelligence Group"
verification: single-source
sourcing_note: >
  One source, and a first-hand one: GTIG is reporting its own detections and disruption actions, so the
  reliability letter is B for an original research lab and the credibility number stays at 2 because no
  second party has independently assessed these clusters. Every confidence qualifier is carried as GTIG
  wrote it, in both directions. The Russian nexus is high confidence for all three clusters; the ICE RELIC
  relationship for UNC6293 and UNC7005 is moderate confidence only, and is recorded in the registry as a
  related-to edge rather than an attribution; GTIG holds UNC5976 distinct and raises possible alignment
  with other Russian services. The token-scraping mechanism is stated by GTIG only for UNC5976 and is not
  transferred onto UNC7005, whose equivalent redirect GTIG describes only as likely used to steal tokens.
  Finland appears solely as the country of the impersonated body, not as a victim geography, and
  Switzerland is not named anywhere in the post — the relevance here is profile match to GTIG's stated
  European government, academic and defence target set. GTIG publishes no ATT&CK mapping of its own; the
  frontmatter mapping is this pipeline's, with each identifier tied to a specific sentence in the post.
  The hospitality captive-portal activity GTIG references is deliberately not re-reported as new: GTIG
  credits ReliaQuest and Microsoft for it, and this pipeline already published the Microsoft account on
  2026-08-01, so only GTIG's own additions — the infrastructure linkage back to April 2026 and the
  naming of CHERRYPIE as ChocoShell — are treated as in-window findings.
confidence: high
update_of: null
references: ["2026-08-01/captivecrunch-storm-2945-hospitality-captive-portal-rat"]
deep_dive: true
deep_dive_category: identity-infra
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Audit linked devices on the accounts of the exposed population — diplomatic, policy, research and defence-industry staff — across both corporate and personal accounts, and add it as a recurring check rather than a one-off: GTIG names routine linked-device audits as its own recommendation, and a WhatsApp device link and an Entra device registration are both persistence that survives a password reset."
  - "Block app-password creation where the identity platform allows it. On Google accounts, enrolment in the Advanced Protection Program prevents app passwords from being created at all, which removes the primary access route of two of these three clusters rather than detecting it."
migrated_from: null
---

Google Threat Intelligence Group published an analysis on 2026-08-20 of three separately tracked suspected Russian espionage clusters abusing legitimate authentication flows against individuals working in academia, aerospace and defence, governments and think tanks across Europe, and academia and think tanks in the United States ([GTIG, 2026-08-20](https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia/)). The organising observation is worth stating plainly because it inverts a common assumption: not one of the methods described defeats multi-factor authentication. Each one uses a flow the identity provider designed and documented, and gets the target to complete it. GTIG assesses with high confidence that all three clusters — UNC6293, UNC7005 and UNC5976 — have a Russian nexus, on the basis of targeting patterns, phishing themes and shared operational techniques. It assesses with moderate confidence, and only moderate, that UNC6293 is a sub-cluster of ICE RELIC (formerly APT29) responsible for initial access operations, and separately that UNC7005 is another initial-access cluster connected to ICE RELIC. UNC5976 it holds distinct, raising potential alignment with alternative Russian intelligence services.

**The app password as an MFA bypass that requires no bypass.** GTIG describes attackers convincing targets to set specific app passwords on their accounts, which the attackers then use to gain access without needing two-factor authentication. The evolution since the technique was first reported in 2025 is a social-engineering refinement rather than a technical one: where the 2025 operations asked the victim to email the app password back, the newer operations ask for it to be entered into an authentication form on an otherwise legitimate-looking website ([GTIG, 2026-08-20](https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia/)). That change matters to a defender, because the first version leaves a mail artifact in a mailbox someone may be watching and the second leaves nothing but a web request from the victim's own browser. UNC6293, which continues to impersonate US State Department officials in deliberately tiny campaigns — usually fewer than five users at a time, on diplomatic and conference themes — added a second route in June 2026: OAuth phishing in which the target performs a real login at an external provider and is then asked to hand back the full redirect URL or the verification code. GTIG's sentence on the consequence is the whole technique in one line: by providing the requested verification code, the target grants UNC6293 access to the account.

**Device codes, and a device link that is genuinely a device link.** UNC7005 — which GTIG states is also tracked as STORM-2945, the cluster this pipeline already covers for its hospitality captive-portal operation — runs the broadest toolset, and GTIG states it conducts device-code phishing for both Microsoft and WhatsApp accounts ([GTIG, 2026-08-20](https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia/)). The Microsoft variant sits behind elaborate spoofed conference-registration pages, which fingerprint the visitor's system — GTIG assesses this is likely to check for an automated scanner — and, in a template revised days after GTIG began watching, added a script to detect and evade automated analysis. The WhatsApp variant is the more instructive, because there is nothing fake in the security-critical step: the phishing page takes the victim's phone number, uses it to create a legitimate WhatsApp device-link request paired to the attacker's device, and then displays the genuine QR and linking code to the target alongside instructions to link their device. Once the account is linked to the attacker's device, the page offers a further prompt — join a voice call, open an encrypted chat, or download a file. If the target joins the call, JavaScript records their audio and video while the page presents a fake ringing call for a limited time, and the recording is posted to a per-session endpoint on the attacker's infrastructure when the call "fails". GTIG states it could not assess what file may have been staged for download.

**OAuth into an unverified cloud project.** From 31 July 2026 UNC7005 registered domains spoofing the Finnish Operations Center, a body that supports Finnish companies in the defence and security markets specifically in a NATO context, and between 6 and 13 August sent targeted phishing to recipients in or related to the European defence industry. If the target authenticates, they are redirected into an attacker-controlled, testing-mode, unverified cloud project which GTIG assesses is likely used to steal authentication tokens ([GTIG, 2026-08-20](https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia/)). UNC5976 industrialises the same pattern and GTIG states its mechanism outright rather than as a likelihood: after authenticating, the target is redirected to a cloud project URL, and the project hosts malicious scripts that retrieve the authentication token from the URL and save it for the operator to retrieve later ([GTIG, 2026-08-20](https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia/)). Google interposes a warning for exactly this shape — an "unverified app" screen shown before the OAuth consent screen for unverified, testing-mode projects requesting sensitive scopes — which makes that interstitial one of the few points where a defender-visible signal exists at all. GTIG disabled the projects; within roughly three months UNC5976 stood up at least twelve new domains, and GTIG now assesses it is migrating away from Google infrastructure to other providers to host part of its phishing infrastructure. UNC5976 also delivered a malicious Excel plugin GTIG names HEADRUSH, distributed from one domain impersonating a research institute in Ukraine, and GTIG says it may have targeted a Ukrainian aerospace and imaging company — a hedge on the victim that is worth keeping, along with GTIG's own note that it was unable to determine the full extent of the infection chain.

**Detection, and the reason it is hard here.** GTIG names the structural problem itself: the accounts these groups target are often personal rather than corporate domain-joined accounts, creating a visibility gap for monitoring compromise from an organisational perspective. A compromised personal mailbox belonging to a policy adviser is then a trusted identity for phishing that adviser's colleagues, and the organisation saw neither the lure nor the compromise. What telemetry does exist sits in the identity control plane rather than on the endpoint, and each of the flows above leaves a distinct trace worth building a query around. App-password creation events are the highest-value one, because a legitimate app password is rare in a modern estate and is created by a user, not by an administrator: correlate creation events against recent inbound mail and against whether the account has any legacy client that needs one. Device-code authentication produces its own sign-in event type; on a workforce that has no kiosk or shared-device use case, device-code grants deserve to be treated as anomalies rather than as a supported path. OAuth consent grants are the third: a grant to an application in testing or unverified state, or one whose redirect target is a cloud-project domain rather than the vendor's own, is not something a user should be able to complete quietly. Device-registration and linked-device events close the set — for WhatsApp because the link *is* the compromise, and for Entra because a registered device is durable access. GTIG notes that the clusters it groups under the ICE RELIC relationship rely heavily on commercial residential proxy infrastructure for post-compromise activity, while stating separately that UNC5976 uses dedicated infrastructure rather than residential proxies. For the former that is what removes geographic improbability from the sign-in as a signal and leaves the grant and registration events carrying the weight.

**Triage:** every one of these events has a large benign population, so the discriminator is never the event alone. An app password created by a user who has no legacy mail client, minutes after an inbound message from an external sender, with the resulting session arriving from a residential address in the user's own country, is the shape to alert on — the country will match, which is precisely why country is the wrong field to key on. A device-code sign-in is normal on a conference-room display and abnormal on a laptop that has a browser. An OAuth grant to a well-known SaaS product is routine; a grant that required the user to click past an unverified-app warning is not, and the warning screen is the artifact that separates them. And a linked WhatsApp device is invisible to enterprise tooling entirely, which is why GTIG's recommendation is a periodic human check of the linked-devices list rather than a rule.

**Defender takeaway:** for this constituency the exposed population is not the whole workforce but a nameable subset — diplomatic and policy staff, researchers, defence-industry contacts, anyone whose conference attendance is public — and the exposed asset is often their personal account, outside the estate. That points the response at two things the organisation can actually do: remove the capability rather than detect its abuse where the platform allows it, which for app passwords means enrolling the exposed population in the protection tier that forbids them outright; and make linked-device and app-password review a standing item for that population rather than an incident-driven one. GTIG's report also carries a smaller signal worth noting for anyone tracking how this tooling is built: it observes that samples of the CHERRYPIE infostealer, which it says is also known as ChocoShell — the stealer this pipeline recorded in the same actor's captive-portal operation three weeks ago — contain numerous artifacts suggesting the malware is generated by a large language model. GTIG also names Go malware it calls ENGINELIGHT, for which a domain spoofing Microsoft registered in late April 2026 served as command and control for the same cluster.
