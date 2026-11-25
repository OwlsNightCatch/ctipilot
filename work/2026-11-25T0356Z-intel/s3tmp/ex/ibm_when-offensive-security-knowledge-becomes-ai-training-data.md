---
title: When offensive security knowledge becomes AI training data
author: Patrick Fussell
url: https://www.ibm.com/think/x-force/when-offensive-security-knowledge-becomes-ai-training-data
hostname: ibm.com
description: AI is reshaping offensive security by turning public research, tools and techniques into training data, potentially lowering the barrier for adversaries. In response, practitioners may move advanced tradecraft out of public view, challenging a field long defined by open sharing.
sitename: When offensive security knowledge becomes AI training data
date: "2026-05-21"
tags: ['Training data', 'IBM X-Force', 'Adversary simulation', 'Red teams']
fingerprint: bf53933c9ea786d9
language: en
image: https://www.ibm.com/content/dam/worldwide-content/creative-assets/ibs/ul/persona-based-imagery/f3/46/gettyimages-2210368336.jpg/_jcr_content/renditions/cq5dam.web.1280.1280.jpeg
pagetype: website
filedate: "2026-11-25"
---
Published 21 May 2026

For as long as offensive security has existed as a discipline, sharing has been baked into the culture. Early generations of hackers traded zines and bulletin-board system (BBS) files (e.g., Phrack). Bugtraq turned into Full Disclosure. Metasploit became the universal language for thinking about how to build and launch an exploit. Backtrack (now Kali) shipped a ready-to-go toolkit so anyone could spin up an attacker box in an afternoon instead of spending hours crawling the web for code to compile.

The unspoken contract was simple: if you figured something out you contributed back to that same community through conference talks and writing blogs. If you built something useful, you shared it. The community grew smarter together, and defenders eventually caught up.

That spirit hasn’t gone anywhere, yet. But we may be at the beginning of a slow shift away from the days when everyone was willing to share everything in open forums.

Walk through any DEF CON village or read any reputable red team blog, and you can trace a direct line back to that original ethos. Think about the projects that shaped how you see hacking, from Nmap to BloodHound.

Techniques like [Kerberoasting](https://www.ibm.com/think/topics/kerberoasting), NTLM relaying and DLL sideloading became widely understood because somebody wrote the original post, somebody else built the tool and a third person developed detections. Over time, new researchers continued to build on those original ideas.

This cycle strengthened the field. It gave junior practitioners a clear path to learning and gave defenders a fair shot at understanding what they were up against.

The downside to this culture is obvious. Every offensive security tool released into the wild eventually gets picked up by actors using it outside of authorized engagements. Common command-and-control frameworks have appeared in ransomware operations. Mimikatz became a staple in nation-state intrusions almost immediately after its release. Cracked versions, modified forks and lookalike payloads have always followed the genuine releases.

This is the long-running Offensive Security Tooling (OST) debate. One camp argues that publishing offensive tools lowers the barrier for adversaries and accelerates harm. The other argues that defenders need that same tooling, that obscurity is not security and that capable adversaries are going to figure it out anyway, often without publishing their work. Both sides make valid points. I’ve landed somewhere in the middle: the value of capability sharing among professionals usually outweighs the downside, provided we’re thoughtful about how loudly we publish and who the actual audience is.

That balance has held for a long time. I’m not sure it’s going to hold much longer.

What changed is evident if you’ve been paying any attention to AI over the last couple of years. Every public blog post, GitHub repo, conference recording and tweet thread breaking down a new technique can become [training data](https://www.ibm.com/think/topics/training-data). Many models are built by crawling the internet and ingesting data, including our open offensive security research.

Those models then transform the data into something anyone can leverage to quickly develop attacker-related assets. The gap between knowing a technique exists and being able to execute is narrowing.

This is important because, six years ago, sharing a technique still required skill to operationalize it. Less experienced adversaries had to read carefully, set up a lab, debug failures and build muscle memory. That learning process created a natural delay that defenders could use to their advantage.

Today, an adversary with a half decent model and a bit of patience can stitch together attack chains that once required years of experience. The training data we generously contribute is the fuel enabling this shift.

What I expect to see in coming years is a gradual migration of serious offensive security work into more closed environments. Not in a cloak-and-dagger sense, but more in line with how certain medical or financial communities have always operated.

The deeper conversations, the ones between individuals that really understand the field, will move to more trusted forums: invite-only Slack workspaces, vetted Discord servers and other small private channels where tradecraft is shared with the expectation that it won’t be indexed, scraped or absorbed into the next model release.

You can already see early signs of this shift. Conference sessions where speakers talk about techniques but omit full code releases. Tooling distributed through closed beta programs, to known operators, rather than landing on GitHub. Vendors that work hard to vet who can access their platforms.

I don’t see this as the end of public sharing. The data that we all used to learn, when we were new, is still out there. This is data I like to refer to as the training pipeline material and the foundational tradecraft. But the leading-edge work, the novel chains, unpatched primitives and tooling that impacts real engagements, will increasingly slip behind a veil that didn’t exist as clearly before.

In this shift, there is a tradeoff. Unfortunately, we lose some of the open culture that made this field unique. Newer operators may find it harder to break in, because the valuable knowledge won’t appear in a Google search result. Vendor security teams that relied heavily on public research, to build detections, will need to invest more in private partnerships.

But there are substantial gains to be made as well. Tradecraft that genuinely matters remains effective for longer. The capability gap between professional operators and those without deeper investment in the field widens back out. Defenders working in trust-based circles, those committed to improving their own skillsets and defending the networks their responsible for, gain access to earlier and richer information than public sources would typically provide.

The community will figure out where to draw new lines, we always do. But the era where the default answer to “Should I publish this?” was automatically yes is likely coming to an end. The new default is a pause, a thought about audience, and a willingness to keep some things in the room.

Join security leaders who rely on the Think Newsletter for curated news on AI, cybersecurity, data and automation. Learn fast from expert tutorials and explainers—delivered directly to your inbox twice weekly. See the [IBM Privacy Statement](https://www.ibm.com/privacy).
