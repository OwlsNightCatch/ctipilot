# extract: served via trafilatura-direct
---
title: Anthropic locks out Claude users after infostealers hijack login sessions - Help Net Security
author: Zeljka Zorz
url: https://www.helpnetsecurity.com/2026/08/31/claude-accounts-compromised-through-infostealer/
hostname: helpnetsecurity.com
description: Anthropic has started locking users out of their Claude accounts due to login sessions compromised through infostealer malware.
sitename: Help Net Security
date: "2026-08-31"
categories: ["Don't miss", 'Hot stuff', 'News']
tags: ['account hijacking', 'AI', 'Anthropic', 'malware', 'account hijacking', 'AI', 'Anthropic', 'malware']
---
# Anthropic locks out Claude users after infostealers hijack login sessions

Anthropic has started locking users out of their Claude accounts due to their login sessions having been compromised through infostealer malware.

“The malware identified in this campaign so far include Vidar, Lumma (LummaC2), StealC, RedLine and Acreed on Windows, and Atomic Stealer (AMOS) on a small number of Macs,” the company said in emails sent out to affected users last week.

“It’s general-purpose malware that typically arrives with an unofficial download or a malicious app, and it quietly copies saved passwords, login cookies in browsers, and credentials for other apps running locally. Your Claude session was likely one of the many things it collected.”

### Next steps for victims

Session theft is the new credential theft, as it allows attackers to sidestep two-factor authentication.

2FA protects the login, but once the user has logged in, the site issues their browser a session cookie that keeps them signed in so they don’t have to re-authenticate on every click. Infostealers copy that cookie and an attacker who “replays” it is treated as an already-logged-in user.

Anthropic reacted to the account hijackings by signing users out of their accounts (to invalidate compromised Claude login sessions), by removing the saved payment method, and by refunding unauthorized Claude charges.

Affected users have been [posting](https://www.reddit.com/r/ClaudeAI/comments/1w1jqsh/thank_you_anthropic_really/) screenshots of the Anthropic account suspension email on social media, complete with instructions on what to do to regain access to their Claude accounts, and how to make sure any corrective action they take is not invalidated by a still active malware infection.

“Signing you out of Claude stops the stolen sessions, but it doesn’t remove the malware,” Anthropic said, and advised victims to – first and foremost – scan for and remove found malware.

Only then should they:

- Set a new password and enable 2FA on the email account they use for Claude
- Update passwords they saved in any browser they use, and check card statements if they store payment details in the browsers
- Add a payment method again to the account, if they plan to continue using it

After the malware clean-up, users should also remove active sessions for other online services, sign out of them and then log in again to invalidate the previously active sessions.

### Users beware

Anthropic tied this attack campaign to a “bad actor” who targeted computers with malware.

“We have no reason to believe that this malware is related to Claude, installed through Claude, or related to anything you did with Claude,” the company said, and added that “phones and tablets do not appear to have been involved.”

The affected user who shared Anthropic’s email on Reddit said they traced their infostealer infection to the download of a pirated game from a Russian underground forum.

Claude users should likely also be on the lookout for copy-cat emails impersonating Anthropic and using this campaign as a pretext.

See also: [How attackers hosted a fake Claude download page on the claude.ai domain](https://www.helpnetsecurity.com/2026/07/23/anthropic-claude-artifacts-download-malware/)

**Subscribe to our breaking news e-mail alert to never miss out on the latest breaches, vulnerabilities and cybersecurity threats. [Subscribe here!](https://www.helpnetsecurity.com/newsletter/)**
