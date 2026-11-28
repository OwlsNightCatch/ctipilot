---
schema: 1
kind: threat
title: "Luna Moth returns to law firms that likely did not pay, with a token handoff: a video-call 'IT support' agent has the employee copy a Microsoft Graph access token out of Microsoft 365 Copilot through browser developer tools, then bulk-downloads files from the attacker's own server (ReliaQuest)"
headline: "ReliaQuest: Luna Moth has staff hand over a Graph token from Copilot on a video call; no sign-in event follows"
summary: "ReliaQuest reports that the data-extortion group Luna Moth (Silent Ransom Group) returned in October and early November to law firms it had extorted in May and August, using a technique it calls almost certainly new for the group: on a video call posing as IT support the attacker has the employee open Microsoft 365 Copilot, copy the Microsoft Graph access token out of the browser's developer tools and paste it to a text-sharing site, then replays it from its own server and downloads thousands of files in about an hour. The token was issued to the victim's compliant device, so no sign-in event is generated for the attacker's address; ReliaQuest is the only source and names no victim or country."
discovered_at: "2026-11-14T03:55:10Z"
updated_at: null
event_date: "2026-11-12"
run_id: 2026-11-14T0255Z-intel
priority: notable
immediate_action: null
tags: [phishing, identity]
regions: [global]
sectors: [legal-services]
entities:
  - actor:silent-ransom-group
  - product:microsoft-graph
techniques: [T1566.004, T1684.001, T1528, T1550.001, T1530]
affected_products: ["Microsoft 365", "Microsoft Graph"]
cves: []
sources:
  - url: "https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/"
    publisher: "ReliaQuest"
    date: "2026-11-12"
    role: primary
closed_sources: []
evidence:
  - quote: "This token-based exfiltration is almost certainly a new tactic for the group."
    publisher: "ReliaQuest"
    source_url: "https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/"
  - quote: "Attackers never have to authenticate, so no sign-in events are generated for their address."
    publisher: "ReliaQuest"
    source_url: "https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/"
  - quote: "In the observed intrusions, the first download from attacker infrastructure came about a minute after the token was copied."
    publisher: "ReliaQuest"
    source_url: "https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/"
verification: single-source
sourcing_note: "ReliaQuest is the only source; the report is its external threat intelligence about third parties, with no victim, count or country named, and no other vendor or authority confirms the token technique or the re-targeting of non-payers. ReliaQuest also sells the platform it recommends. The group name and the UNC3753 alias come from earlier reporting on the group, not from this report."
confidence: medium
references:
  - 2026-06-06/luna-moth-silent-ransom-group-unc3753-vishing-to-physical-ac
  - 2026-05-28/fbi-flash-csa-260526-silent-ransom-group-sends-operatives-ph
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

ReliaQuest says Luna Moth, also called Silent Ransom Group, has targeted law firms since at least mid-2023 and in October and early November went back to firms it had extorted in May and August; those firms appear on the group's leak site, which ReliaQuest says suggests they likely did not pay, and the group exfiltrated a second round of data ([ReliaQuest, 2026-11-12](https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/)). The approach reverses the group's earlier flow: a blank-subject email from a free address carries a deliberately invalid PDF that crashes the viewer, and the attacker then calls the target, often on a personal number outside corporate call controls, posing as IT support responding to a "malicious email" ([ReliaQuest, 2026-11-12](https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/)). By late August the group paired video calls with a built-in remote-assistance tool, and by October the video call alone carried both the conversation and the screen control ([ReliaQuest, 2026-11-12](https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/)).

On the call the attacker has the employee open Microsoft 365 Copilot in the browser on a managed, compliant laptop, open the browser's developer tools to find the request Copilot sends to Microsoft Graph and copy the access token it carries, and paste the token into a public text-sharing site where the attacker retrieves it ([ReliaQuest, 2026-11-12](https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/)). Within a minute the attacker replays the token from its own server and downloads files en masse through the Graph API, thousands in about an hour ([ReliaQuest, 2026-11-12](https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/)). The stolen token passes Conditional Access because the device check runs only at sign-in, not when the token is later used, and, unlike device-code phishing, the token is issued to the victim's compliant device and then handed over ([ReliaQuest, 2026-11-12](https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/)). Nothing is installed, and the video-call applications are signed legitimate software ([ReliaQuest, 2026-11-12](https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/)).

**Exposure:** a Microsoft 365 tenant whose staff can open browser developer tools and take calls from outside IT, with Microsoft 365 Copilot reachable in the browser; ReliaQuest says law firms are the current focus and other sectors holding similarly sensitive data could be next ([ReliaQuest, 2026-11-12](https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/)).

**Detection:** with no malware or endpoint alert, the evidence is ordinary-looking events, a blank email, an external video-call session and Graph access from an unfamiliar address, which ReliaQuest says to correlate across email, video-call and Microsoft 365 logs; a video-call screen share, a Copilot session, a visit to a text-sharing site and Graph file access from an unfamiliar address are each ordinary alone and together can indicate a token handoff ([ReliaQuest, 2026-11-12](https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/)). Video-call platform logs, web proxy or DNS logs and Microsoft 365 audit logs each record part of the handoff but rarely reach a detection pipeline ([ReliaQuest, 2026-11-12](https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/)).

**Defender takeaway:** disable developer tools through Group Policy on managed browsers and block Graph Explorer and the browser net-export pages, because the handoff depends on users reading tokens out of browsers; pilot Continuous Access Evaluation with strict location enforcement, defining every egress address including secure web gateway ranges as a named location; and tell staff that IT will never ask for developer tools or tokens and that they should verify IT requests by callback ([ReliaQuest, 2026-11-12](https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/)). ReliaQuest notes that default Microsoft access tokens last 60 to 90 minutes and that Continuous Access Evaluation can extend supported tokens to as long as 28 hours ([ReliaQuest, 2026-11-12](https://reliaquest.com/blog/threat-spotlight-luna-moth-returns-re-targeting-law-firms-through-access-tokens/)).
