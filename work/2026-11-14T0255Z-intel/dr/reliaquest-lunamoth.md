---
title: Luna Moth Returns, Re-Targeting Law Firms Through Access Tokens
author: ReliaQuest Threat Research
url: https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/
hostname: reliaquest.com
description: Data-extortion group “Luna Moth” (aka “Silent Ransom Group”) is going back for seconds by re-targeting law firms that likely didn’t pay its ransoms.
sitename: ReliaQuest
date: "2026-11-12"
categories: ['Threat Intelligence', 'Emerging Threats']
tags: ['blog, Cloud Security, Cyber Threats, Identity Protection, Social Engineering, Threat Intelligence, Threat Research, Threat Research - RSS']
fingerprint: "3c019c938ec98ec5"
---
*Editor’s note: This report was authored by Joseph Keyes.*

**This is external threat intelligence from the ReliaQuest Threat Research team. The findings describe threats, vulnerabilities, and attacker activity affecting third parties and the broader threat landscape—not ReliaQuest’s own environment. Nothing in this report should be interpreted as a vulnerability in ReliaQuest’s systems or data.**

### Key Points

- Extortion group “Luna Moth” (aka “Silent Ransom Group”) has targeted law firms since at least mid-2023 and is now returning to those that likely didn’t pay its first extortion demand. This time, it’s dropped its multiple remote-management tools and manual downloads. Instead, a caller persuades the target during a video call to hand over an access token, which the group then uses to bulk-download files automatically.
- This token-based exfiltration is almost certainly a new tactic for the group. The stolen token passes Conditional Access (which approves sign-ins) because its device check runs only at sign-in, not when the token is later used.
- Organizations should implement Continuous Access Evaluation (CAE) with strict location enforcement so a stolen token stops working outside the victim’s network.

Data-extortion group “Luna Moth” (aka “Silent Ransom Group”) is going back for seconds by re-targeting law firms that likely didn’t pay its ransoms the first time. The group is using a new method to steal this additional data: The group now persuades targets on remote calls to hand over **access tokens**, then uses them to bulk-download files automatically—a technique we haven’t seen it use before.

Luna Moth, which steals data without encrypting systems, has targeted law firms since at least mid-2023, previously relying on multiple remote-management tools and manual exfiltration. Now, the attacker still calls a target posing as IT support but persuades them to extract a Microsoft Graph access token (the credential that applications use to read Microsoft 365 data, such as SharePoint files) from Microsoft 365 Copilot. The group then uses that token from its own infrastructure to download files in bulk.

Because the stolen token passes MFA and Conditional Access checks, and the video-call platform used for the call is permitted in almost every organization, this technique is easy for other extortion groups to copy.

In this spotlight, we:

- Trace how the token handoff works: Luna Moth gets targets to hand over a token, then replays it from attacker infrastructure to bulk-download files.
- Examine how Luna Moth is re-targeting law firms that likely didn’t pay their original extortion demand, including the social engineering that gets victims on a call.
- Compare Luna Moth’s earlier tactics with its new ones and show how they fit a broader shift toward attacks that skip malware and failed logins.

## How Luna Moth Uses Stolen Tokens to Exfiltrate Data

Luna Moth now steals data by tricking employees into handing over a Microsoft 365 access token, which lets attackers hide the malicious activity behind what looks like the employee’s own legitimate actions. That makes it harder for security tools to catch.

Posing as IT support on a call, the attacker either takes control of the employee’s screen or walks them through copying the token out of Microsoft 365 Copilot in the application or browser. The attacker then uses it from their own server to download thousands of files in about an hour. Because the token was issued to the employee’s real, compliant device, it passes MFA and Conditional Access, which doesn’t re-check it once it’s issued.

The attack chain runs in five steps:

- **Step 1:** The attacker, posing as IT support, spoofs a number the victim trusts and persuades the user to join a video call and share their screen.
- **Step 2:** The attacker has the user open Microsoft 365 Copilot in the browser on their managed, compliant laptop.
- **Step 3:** The user is told to open the browser’s developer tools, a built-in feature meant for web developers, to find the request Copilot sends to Microsoft Graph and copy the access token it carries.
- **Step 4:** The user pastes the token into a public text-sharing (“paste”) site, where the attacker retrieves it. That gets the token to the attacker without any malware or phishing for a security tool to flag.
- **Step 5:** Within a minute, the attacker replays the token from their own server and downloads files en masse through the Microsoft Graph API.

Copilot is a useful source because it’s already signed in on a managed device and carries delegated access to the files the user can reach. A token is a bearer credential, so whoever holds it can act as the user until it expires. By default, Microsoft access tokens last 60 to 90 minutes. Continuous Access Evaluation (CAE), which lets Microsoft re-check or revoke a token mid-session, can extend supported tokens to as long as 28 hours. Tokens can also be cut off early when conditions change, such as a location change or account disablement. Either way, the default lifetime is about as long as the attackers need to pull thousands of files.

### Why MFA and Conditional Access Don’t Catch the Activity

Conditional Access doesn’t stop stolen tokens from working because it checks only when a token is issued, not each time it’s used. In these attacks, users sign in normally on compliant devices, so every check passes. Without CAE and strict location enforcement, tokens stay valid from any location until they expire. Attackers never have to authenticate, so no sign-in events are generated for their address.

This technique shares a core idea with [device-code phishing](https://reliaquest.com/blog/threat-spotlight-jalisco-toolkit-and-ai-powered-phishing-surge/): in both, the attacker persuades a user to take part in a legitimate Microsoft process that results in a valid token instead of a password. Because the user completes the sign-in themselves, MFA is satisfied for both techniques. In device-code phishing, tokens are issued to the attacker’s device. Here, they’re issued to the victim’s compliant device and then handed over.

That makes detection and threat hunting much harder, because the bulk theft passes compliant-device and MFA controls and looks like the real user’s own activity. In observed cases, attackers pulled thousands of files in about an hour, which is more than enough to support extortion, before a security team could respond.

## Luna Moth Likely Re-Targeting Law Firms It Already Extorted

Speed makes the token handoff cheap to repeat, and Luna Moth appears to be using it on its own past victims. In October and early November, the group went back to law firms it had previously extorted in May and August. Those firms appear on the group’s data-leak site, which suggests they likely didn’t pay the first extortion demand.

This re-targeting came anywhere from several weeks to months after the first extortion, and the group exfiltrated a second round of data. Luna Moth likely keeps track of which victims didn’t pay and revisits them, rather than moving on after a single extortion cycle. Refusing to pay doesn’t end the threat for law firms, and once this tactic catches on, the same risk could easily extend to organizations outside the legal sector. What’s more, a second theft adds to the client-confidentiality, notification, and reputational risks from the first.

### Social Engineering Starts with a Broken PDF and a Call

When Luna Moth recently returned to previous victims, it used an attack chain with fewer steps and fewer tools than in its first attacks, which makes it harder for defenders to detect. The latest tactics needed only a video call and a Microsoft Graph token the employee handed to the attacker, who then used it from their own server to download files in bulk.

The initial attacks began with attackers posing as IT support, who talked employees into joining a video call and then had them open a built-in Windows remote-assistance tool to hand over control of their machines. They manually exfiltrated sensitive data to personal cloud storage for extortion. This matches Luna Moth’s known approach: a phone-based lure, remote-access software, and extortion without encryption.

In the follow-on activity, the group sent a blank-subject email from a free email address with a PDF named like a business report that was deliberately invalid and crashed the viewer every time it was opened. Soon after, the attacker called the target, often on a personal number outside corporate call controls, posing as IT support responding to a “malicious email.” The broken attachment made the offer to fix it over a video call seem routine. This reverses earlier campaigns, where a fake invoice or subscription email prompted the victim to call the attacker.

Doing it over a video call now does both jobs: the call keeps the user engaged while the screen share lets the attacker direct the session. Nothing is installed, and these video call applications are signed, legitimate software, so there are no malicious files to block.

With no malware or endpoint alert, the only evidence is ordinary-looking events: a blank email, an external video call session, and Graph access from an unfamiliar address. Correlate these across email, video call, and Microsoft 365 logs, and train users to verify any unsolicited IT call through a known help-desk number.

## How Luna Moth’s Tactics Have Changed

Luna Moth’s shift is part of a broader move toward attacks that don’t require malware or failed logins. In our recent [threat report on residential proxies](https://reliaquest.com/blog/threat-spotlight-residential-proxies-mask-social-engineering-attacks/), we described social-engineering groups pairing calls to help desks with legitimate software-as-a-service (SaaS) interfaces, including Microsoft Graph activity across hundreds of sites, and **reaching their objectives within 6 to 15 minutes** of initial access. Luna Moth gets to the same place by a different route: getting users to hand over tokens instead of enrolling a device or routing activity through a residential proxy. Either way, the target is the user’s identity and cloud access, so endpoint controls miss the activity.

Over the past year, Luna Moth has simplified how it gets in and changed how it takes data out. Earlier intrusions used multiple remote-management tools, including commercial remote-support software and a built-in Windows remote-assistance tool. By late August, the group paired video calls with the built-in remote-assistance tool, and by October, the video call alone handled both the conversation and the screen control.

But the biggest change lies in exfiltration. Instead of manual downloads, file-transfer tools, or uploads to personal cloud storage—all of which ran through the endpoint—the attackers now replay stolen Copilot Graph tokens from their own infrastructure and download files through Microsoft Graph, moving the theft into the cloud.

The table below breaks down the changes:

| Area | Earlier Luna Moth Activity | New Tactics | 
|---|---|---|
| Target selection | Extort once, then move on | Return to non-paying victims | 
| Remote access | Multiple remote-management tools | A single video call used for both the conversation and screen sharing | 
| Identity abuse | No token-handoff technique described in public reporting | A token created on the user’s host and used from attacker infrastructure | 
| Exfiltration | Manual downloads, file-transfer tools to attacker servers, uploads to personal cloud storage, or emails to attacker-controlled accounts | Bulk downloads through Microsoft Graph from attacker infrastructure | 
| Lure and calls | Callback phishing and help-desk impersonation | Blank email with a deliberately broken PDF attachment, followed by a call to a personal phone from a spoofed number | 

These changes show the group adapting to the controls defenders implemented in response to earlier reporting, while keeping its core loop of phone-based social engineering followed by data theft.

Common defenses are built around stolen credentials because they assume attackers need to sign in. Token handoffs, on the other hand, skip that step, so MFA, compliant-device rules, and geographic alerts all see a normal sign-in by the real user. Defenders need controls that act after sign-in, such as continuous evaluation of tokens, fast session revocation, and detection of unusual Graph activity.

## Step Up Your Defenses

### ReliaQuest’s Approach

ReliaQuest GreyMatter, an agentic AI security operations platform, equips security teams to spot the activity detailed in this report while it’s still visible in identity and SaaS telemetry, rather than after attackers have already replayed tokens and downloaded files. A token handoff leaves little for endpoint or sign-in controls to see, so defenders need to test their coverage, correlate weak signals, and act within minutes.

**Detection at Source:** Video-call platform logs, web proxy or DNS logs, and Microsoft 365 audit logs each record part of the handoff but rarely reach a detection pipeline. Detecting at the source correlates them. A video-call screen share, a Copilot session, a visit to a text-sharing site, and Graph file access from an unfamiliar address are each ordinary on their own. Together, they can indicate a token handoff.

**GreyMatter Discover:** The token handoff works because nothing checks tokens after they’re issued. GreyMatter Discover finds identity and cloud settings that let stolen tokens work from any address, such as Conditional Access policies without CAE or strict location enforcement, before attackers do.

**GreyMatter Transit:** GreyMatter Transit identifies threats in seconds, as telemetry moves from source to storage rather than after it lands. In the observed intrusions, the first download from attacker infrastructure came about a minute after the token was copied. With attacks moving this fast, response has to keep pace with the attacker rather than wait on audit logs that can lag.

ReliaQuest detection rules align with techniques used by the groups covered in this report and help prevent similar threats in the future. Used alongside the following GreyMatter Automated Response Playbooks, organizations can contain ransomware threats in as little as five minutes:

- **Disable User + Terminate Sessions:** Cuts off the stolen token’s session and any other authenticated access once an identity is confirmed as compromised.
- **Block IP + Block Domain:** Blocks the replay infrastructure and paste sites used to pass the tokens.
- **Isolate Host:** Contains endpoints if attackers have moved beyond token theft.

### Your Action Plan

- **Enable CAE with strict location enforcement.** Conditional Access checks devices only when tokens are issued, so handed-over tokens keep working from any address. Pilot strict enforcement first, defining every egress IP address, including secure web gateway ranges, as a named location.
- **Block browser developer tools and token-inspection pages.** Disable developer tools through Group Policy on managed browsers and block Graph Explorer and the browser net-export pages (chrome://net-export and edge://net-export), because the token handoff depends on users reading tokens out of browsers.
- **Restrict remote-support and screen-sharing tools.** Allow only the tools your help desk uses, and block unapproved remote-management software where there’s no business need. Tell users that IT will never ask for developer tools or tokens and that they should verify IT requests by callback. Limit external video meetings to approved platforms and known participants.

## Key Takeaways and What’s Next

Luna Moth’s shift to token-based exfiltration is the most important change in this activity, because it moves the theft out of the endpoint and into the cloud. These attacks show again that threat actors no longer need remote-management tools or malware on the victim’s machine to achieve their objectives. In this wave of attacks, the stolen tokens were issued to users’ compliant devices, so they passed MFA and Conditional Access, and the downloads looked like the users’ own activity. Most organizations’ security controls never see an attacker sign in, so there is nothing for them to flag.

The token handoff is also cheap to run again, which links it to the group’s re-targeting of law firms that likely didn’t pay the first time around. A data-leak site listing already identifies breached firms known to hold sensitive client data, and the new attack chain needs only a call and a token. We assess with moderate confidence that Luna Moth will keep revisiting non-paying victims over the next six months because the required effort is low and the potential payoff is high. In this campaign, several firms were hit again in October and November with the same infrastructure, which points to deliberate tracking of non-payers rather than coincidence. Any organization that has received an extortion email or appeared on a data-leak site should treat a second approach as expected and brief its users now.

We assess with moderate confidence that other extortion groups will copy the token handoff over the next six months, because it needs only a convincing caller and a user at a keyboard. There’s no malware to develop and no endpoint tooling to evade, and video-call software and Microsoft 365 Copilot are widely available in most organizations. We also expect the technique to expand beyond Copilot tokens. Other applications signed in to Microsoft 365, including Microsoft’s own web apps and third-party apps that the organization has granted access to files and SharePoint sites, hold similar tokens that a user could be talked into copying, as do browser session cookies. Any of these could give an attacker the same access unless the token is bound to the device or location it was issued to. Law firms are the current focus, likely because their client data gives the group strong leverage, but other sectors holding similarly sensitive data could be targeted next.

## IOCs and Observables

The indicators and observables below come from recent intrusions and are worth blocking and hunting for, but the attacks don’t depend on them.

| Indicator | Type | Context | 
|---|---|---|
| 104.37.184\[.\]195 | IP address | Token replay and bulk file download | 
| justsendtext\[.\]xyz | Domain | Text-sharing site used to pass the stolen token | 
| SharePointScavenger/1.0 | User agent | Open-source SharePoint download tool, seen in one intrusion | 
| “\[Firm\] has lost confidential data of their clients. Very Important!” | Email subject | Extortion email sent after data theft | 

*Daxton Wirth also contributed to this report.*
