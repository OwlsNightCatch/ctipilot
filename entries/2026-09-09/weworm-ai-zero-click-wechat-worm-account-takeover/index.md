---
schema: 1
kind: research
title: "WeWorm: an AI-assisted zero-click worm demonstrates full WeChat account takeover on Android and iOS from a single unanswered call"
headline: "Calif builds a self-propagating zero-click WeChat worm with AI help in about nine days; Tencent fixed it before disclosure"
summary: >
  Offensive-research firm Calif disclosed WeWorm on 2026-09-08: a demonstrated zero-click worm that
  hijacks a WeChat account on Android or iOS through a single incoming VoIP call that needs no answer,
  exploiting a memory-corruption bug in WeChat's call-signaling stack. Calif says an AI-assisted workflow
  produced a working remote-code-execution exploit in about two days and the self-propagating worm in one
  further week; Tencent shipped client fixes (Android 8.0.77, iOS 8.0.76) on 2026-08-21 and blocked the
  exploit server-side, so the transferable findings are the AI capability data point and the trusted-contact
  propagation pattern, not a WeChat action item.
discovered_at: "2026-09-09T17:52:00Z"
updated_at: null
event_date: "2026-09-08"
run_id: 2026-09-09T1726Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, mobile, zero-click]
regions: [global]
sectors: [public-sector, technology]
entities: ["tool:weworm"]
techniques: [T1203]
affected_products: ["Tencent WeChat"]
cves: []
sources:
  - url: "https://calif.io/research/weworm"
    publisher: "Calif"
    date: "2026-09-08"
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/"
    publisher: "Help Net Security"
    date: "2026-09-08"
    role: corroborating
  - url: "https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html"
    publisher: "The Hacker News"
    date: "2026-09-08"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The victim does not need to answer the call, or interact with their phone at all. Even if they do answer, they hear nothing, and the exploit still succeeds."
    publisher: "Calif"
    source_url: "https://calif.io/research/weworm"
  - quote: "Working with AI, our team found the bug and wrote the first remote code execution (RCE) exploit in about two days."
    publisher: "Help Net Security"
    source_url: "https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/"
  - quote: "Checks on 8 September found no CVE identifier for the flaw and no advisory on Tencent's security response site, which lists the latest announcement as April 2022."
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html"
verification: multi-source
sourcing_note: "Calif is withholding the specific memory-corruption detail pending a conference presentation; no CVE has been assigned and Tencent has published no advisory, so the affected-version range and whether the underlying bug (versus Calif's specific exploit) is fixed cannot be independently confirmed. The AI development-time and worm-scale claims rest on Calif's own account; Tencent independently confirmed the bug is exploitable for remote command execution."
confidence: high
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

Calif, a US offensive-security research firm, published a working demonstration of WeWorm on 2026-09-08: a zero-click worm that takes over a WeChat account on Android or iOS through a single incoming voice or video call, exploiting a memory-corruption bug in WeChat's VoIP call-signaling stack (Calif is withholding the specific bug detail pending a conference talk) ([Calif, 2026-09-08](https://calif.io/research/weworm)). The exploit fires while the call is still ringing and requires no answer and no interaction: "The victim does not need to answer the call, or interact with their phone at all. Even if they do answer, they hear nothing, and the exploit still succeeds" ([Calif, 2026-09-08](https://calif.io/research/weworm)). The only prerequisite is that the caller already sits on the victim's WeChat contact list, and because WeChat grants saved contacts additional trust, a first compromised account can call and take over further contacts on its own: Calif demonstrated hop-to-hop propagation across three physical devices, each full takeover (read and send messages, place calls, act as the account owner) completing in seconds ([Calif, 2026-09-08](https://calif.io/research/weworm); [Help Net Security, 2026-09-08](https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/)).

The transferable finding is a capability data point, not an active threat. Calif states an AI-assisted workflow found the bug and produced the exploit fast, "Working with AI, our team found the bug and wrote the first remote code execution (RCE) exploit in about two days" ([Help Net Security, 2026-09-08](https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/)), with the self-propagating worm built in one further week, work it says a human team previously needed months for. This is responsibly-disclosed research, not in-the-wild activity: Calif reported the flaw to Tencent on 2026-07-24, Tencent shipped client fixes (Android 8.0.77, iOS 8.0.76) on 2026-08-21 and, per Calif, blocked the exploit on its servers for all users by 2026-08-28, requiring no user install ([The Hacker News, 2026-09-08](https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html)). No CVE has been assigned and Tencent has published no advisory: "Checks on 8 September found no CVE identifier for the flaw and no advisory on Tencent's security response site, which lists the latest announcement as April 2022" ([The Hacker News, 2026-09-08](https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html)), and Calif declined to say whether the underlying bug, versus its specific exploit, is fixed ([The Hacker News, 2026-09-08](https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html)).

**Defender takeaway:** WeChat has negligible footprint in most Swiss public-sector estates, so the value here is the pattern, not the product. A call-signaling or media stack in any messaging or collaboration platform (the same class of code in Teams, Signal, WhatsApp or a softphone) is a zero-click, no-interaction attack surface reachable by anyone the target already trusts, and a single compromised internal account then inherits that trust to reach the next. Treat contact-graph trust as a propagation vector in the threat model for approved communication tools, keep their clients on the current release, and note the wider signal that an AI-assisted workflow compressed a working mobile zero-click exploit and a self-propagating worm from months to roughly nine days.
