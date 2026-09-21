# extract: served via trafilatura-direct
---
title: Google Doc Sidebar Sends Mac and Windows Users Down Different Paths to Malware | Huntress
author: Susannah Matt; Ryan Dowd; Jonathan Semon
url: https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows
hostname: huntress.com
description: "A single X DM split into two malware chains: AMOS stealer on Mac, NetSupport Manager on Windows, see the Huntress SOC analyst breakdown."
sitename: Huntress
date: "2026-09-15"
---
Many Black Hat and DEFCON attendees come home to an inbox full of DMs. While catching up on the expected post-conference networking last month, a Huntress researcher realized they were being targeted in an X exchange with someone posing as a crypto marketing executive. The threat actor sent a link to a real Google Doc with a custom sidebar designed to trick the recipient into downloading malware: an AMOS infostealer on macOS, or PowerShell loader chain on Windows.

Immediately picking up on the scam, our researcher didn't download any malware on their machine, but they did keep chatting with the threat actor, who ended up sending more malware and eventually a million-dollar offer. What started with a DM ended with a rogue certificate authority sitting in the Huntress testing environment.

While they weren't the ones to receive the DMs, Huntress SOC Analysts [__Ryan Dowd__](https://www.huntress.com/authors/ryan-dowd) and [__Jon Semon__](https://www.huntress.com/authors/jonathan-semon) did the heavy lifting in analyzing every twist in this unpredictable kill chain, and they shared their findings in this month's edition of [Tradecraft Tuesday](https://www.huntress.com/community-series/tradecraft-tuesday). 

Read their [__blog__](https://www.huntress.com/blog/defcon-phishing-google-doc-malware) for full technical details and check out highlights from the episode below. 

## The Initial DM: A friendly face, a malicious ask

On X, the threat actor posed as the head of marketing at CoinDesk, appearing to use one person's name and another's photograph. Huntress confirmed that this account reached out to multiple security researchers at the tail end of DEFCON, using a boilerplate lure themed around an upcoming crypto conference. Ryan refers to this as a "volume play" instead of specific targeting of DEFCON attendees; our analysts found posts on social media from users calling out this account for scammy behavior dating back to October 2025.

*Figure 1: The @HartmansDoeke X account that messaged our researcher, posing as CoinDesk's VP and Head of Marketing*

While several media reports and other commenters made note of the X user's imperfect English in their communications as a dead giveaway for a scammer, Ryan and Jon pushed back on that general assumption.

"I think one of the biggest things that we forget is that a lot of these threat actors are just people on the other end," Jon said. "And in the day of AI and all the other Grammarly and all the tools that are out there that people can utilize for perfect, pristine English, there is a bit of a play to be made off of broken English, more personal, natural conversation that you're having with people."

## The Google Doc: A suspicious sidebar

After some "friendly" back and forth, the threat actor sent our researcher a link to a legitimate Google Doc along with an "access key" to unlock the conference planning details.

*A demo of the malicious Google Apps Script*

The Google Doc featured a sidebar displaying a fake decryption failure message, with supposed remediation instructions for users of different operating systems, including the option to copy and paste certain commands into the Terminal. This [__ClickFix__](https://www.huntress.com/blog/dont-sweat-clickfix-techniques) lure, and the "manual update" button beside it, are what actually delivered the malware. The sidebar itself was a Google Apps Script bound to the document, so nothing had to be downloaded for it to run. Jon described the document as "a kind of a triage and a delivery mechanism. It's a funnel." 

The Apps Script ran client-side in the victim's browser, avoiding an OAuth consent prompt and ultimately collecting the victim's public IP and geolocation and scanning for MetaMask / Ethereum, Phantom, Tron, and Solana crypto wallets.

Everything collected was sent directly to the threat actor via the Telegram API; the script sent a beacon message for each of the action codes below.

*Figure 2: Action codes sent back to the action via Telegram*

`VIEW` is the one worth sitting with. Opening the document while signed in, clicking nothing, and downloading nothing, was enough to report the viewer's IP address, location, browser, and whether they were running a crypto wallet extension. Everything after that is the actor grading the target.

We found Russian comments throughout the source code as well as in PCAP files of C2 communications, supporting, but not proving, a Russian-speaking operator. We also noticed a great deal of emojis.

*Figure 3: Beacon messages landing in the actor's Telegram. This is Huntress test traffic rather than a real victim:* `203.0.113.x` *is a range reserved for documentation.*

Ryan quipped: "Those icons do give it a vibe-coded feel, to be honest, but I'm not here to judge."

Jon revisited the indefinite attribution later in the broadcast: "We can't pinpoint a single group, or say this is some APT. It could just be a guy in his house using AI to deploy malware, for all we know, or I guess a woman in her house deploying malware, too. I don't want to exclude anybody on that."

Windows and Mac users are placed on different execution paths. Mobile visitors triggered a `MOBILE` beacon and nothing else, because the actor saw no point in serving a payload to a phone.

## The macOS payload: Choose your own attack path

Ryan noted that the OS-specific instructions with multiple options might give the victim the illusion of control. Mac users who opted to paste the ClickFix commands launch a piped **zsh** chain, while users who downloaded the malware manually are presented with an Apple Disk Image (DMG) file from the attacker's own GitHub repository.

*Figure 4: Mac users recieved the payload either from a piped ZSH command or a manual download from the threat actor's GitHub repo.*

The ultimate payload appeared to be a variant of the [__AMOS__](https://www.huntress.com/blog/amos-stealer-chatgpt-grok-ai-trust) stealer that attempted to collect the following:

- Browser data
- Cryptocurrency-wallet data
- Telegram data
- Apple Notes data
- Cookie data
- macOS login-keychain information

The DMG file also included Gatekeeper-bypass instructions and a password prompt.

Figure 5: Screenshot of the Gatekeeper bypass password prompt

Describing the payload as "designed for low visibility, built for stealth and persistence," Ryan noted similarities between this AMOS variant and the [__six-stage MacSync stealer kill chain__](https://www.huntress.com/blog/macsync-stealer-rat-reverse-engineering) we covered in last month's [__Tradecraft Tuesday__](https://www.huntress.com/blog/fake-claude-macsync). 


## Windows delivery: Three stolen code-signing certs

Windows users who opened the Google Doc were led in a different direction. For the manual download, the same fake decryption failure message instructed Windows users to update a "Google API Connector," which actually launched an application signed with a certificate belonging to a small Norwegian company, either stolen or fraudulently issued. That is the first of three abused code-signing certs used in this chain.

The application took advantage of Microsoft's ClickOnce feature to deploy. As Jon put it: "Why write a custom downloader or a full-on installer for an application when you can just use Microsoft to ship it? "

After installation, an HTML Google Workspace Marketplace portal popped up to distract the victim while the malware downloaded in the background.

Windows users who fell for the ClickFix lure in the Google Doc sidebar ended up launching an encoded PowerShell command that fetched a loader, which in turn pulled down three encrypted payloads. All three were offline by the time we went looking, but all three were already on VirusTotal, so the kit had clearly run before. As an extra flourish, the execution chain presents the user with a fake "progress bar" for the supposed remediation, a touch our analysts thought was "cute."

*Figure 6: The loader script displays an "installing" window to the victim*

Ryan noted: "A lot of effort went in to make this progress bar look legitimate, more so than some of the effort we saw in other parts of this campaign, which was quite funny."

## You have one new message: A second document link and a second stolen cert

In the midst of our malware analysis, the threat actor kept sending our researcher DMs, including a link to another document, this time shared via DropBox DocSend. Once again, macOS and Windows users were routed to different paths: macOS users were sent to another host serving the same AMOS payload and Windows users were told to install a DocSend desktop application.

The installer in the Windows chain was signed with a certificate stolen from Discord Inc.; the signature did not validate.

Ultimately, nothing was actually installed from DropBox: Victims were directed through what Jon called "a little 5-screen onboarding carousel, using a real Dropbox marketing campaign, real Dropbox links and otherwise." Like the fake progress bar from earlier, these pages had no function but distraction.

Jon walked through what went on in the background: "There's three try blocks, there's three catches, and there's three silent returns. So basically, if the Git token fails, or the functions fail, or the handler running the code fails, it all just returns nothing. So, if the server's dead, or the host is rejected for some reason, or there's a full-on compromise on the machine, they all produce the exact same thing on the screen for the end user, which is basically nothing at all."

## Reconstructing communications from a dead endpoint

When the DocSend sample's endpoint returned HTTP 404, we looked for related infrastructure on the same domain, `web12api[.]com`:

Figure 7: Infrastructure related to the malicious domain

After rebuilding the registration protocol from the sample's own `@sentry/electron` module, we sent the reconstructed request to the live SignNow sibling, which returned:

- Approximately 5.5 KB of unobfuscated JavaScript
- A session token
- An archive password
- Three payload URLs

### **The recovered stage-three payloads**

- `Manager.zip` - NetSupport Manager 14.10.0004
- `Localcertificate.zip` - a TLS-intercepting local proxy
- `asusdriverld.zip` - a Ledger wallet implant

## The final stage

Before writing anything to disk, the loader captured and uploaded a full desktop screenshot. It then downloaded three password-protected archives from `eu03hub[.]com/get_file`, with the archive password included in the command-and-control response. Each executable was launched detached and hidden, then launched again 20 seconds later with `Start-Process -Verb RunAs` to request elevation.

### **Payload one: NetSupport Manager**

NetSupport Manager is a legitimate remote monitoring and management (RMM) tool that is frequently abused by threat actors. This payload was configured to redirect data to hostile infrastructure and disable chat, messaging, connect, and disconnect alerts.

Jon elaborated: "This is also what carries all the persistence for these three modules. It's got a keyboard filter driver, a Windows service, a Win logon, a `Run` key, a scheduled task to reinstall itself… all that fun junk that we see with these rogue RMM tools being abused."

During the broadcast, Ryan looked up one of the IP addresses the NetSupport Manager payload reached out to and found two new domain names registered: `GTA6Mainserver[.]com` and `GTA6Mainweb[.]com`. Whoever is on that host is now also running a Grand Theft Auto VI lure, aimed at people hunting for a leaked copy of the game. 

Read our new blog on another malware variant using a [__GTA6 lure__](https://www.huntress.com/blog/fake-gta6-download-malware-analysis). 


### **Payload two: the third stolen certificate authority**

Jon deemed the second payload the most interesting, and begrudgingly gave props to the threat actor, calling it "malicious, but good work." He then jokes: "I do think that you could have done more with it, I just pray that you never do."

Disguised as a Lenovo driver package, the payload was signed with a genuine stolen Lenovo certificate, the third abused code-signing cert in the chain. The certificate authority it goes on to build is a different thing entirely: that one it generates itself. It hollowed `MsBuild.exe` and imported only kernel32, ultimately establishing what Jon called "purpose-built and working public key infrastructure on your machine."

The payload loads two certificates:

- A self-signed certificate authority (CA) in the system root store, presenting as Google Trust Services with `CN=WR3`
- A  `www.virustotal.com` leaf certificate with a SAN list covering the legitimate domain and localhost.

Jon walked through more novel tradecraft that he and audience members described as "terrifying." It added a hosts-file entry and a `LocalProxy` firewall rule, resulting in a locally answered HTTPS connection that appeared valid, allowing the operator to block lookups or return fabricated clean results without certificate warnings. While the process itself died at reboot, the CA, hosts entry, and firewall rule persisted.

Because the CA was regenerated per host, blocking a single certificate thumbprint does nothing.

Jon drove the point home: "The fact that they could install this cert store on there, and there's no host entry, or firewall rule, or otherwise that's blocking this…if the threat actor wanted to install these other certificates for any one of the crypto domains that we've talked about, any one of the wallets that we've talked about, antivirus update signals, they could just intercept, read, or block all of those things. That's a terrifying concept to me."

### **Payload three: a Ledger wallet implant**

After paying the threat actor some compliments, Jon took this opportunity to "crap on them again." The third payload used the same crypter, Lenovo disguise, and `MsBuild` hollowing technique as the second payload. After creating a `Run` key named `Ledger Wallet Installer`, it searched for Ledger Live and Ledger Wallet installations. It hid its bot ID as sixteen hex characters in a file called app.crc32, tucked inside a real application's data folder, then started polling the actor's server for commands. We watched it poll 18 times. Every response came back empty, so the channel worked and the operator simply was not tasking the host. 

Jon continued: "The wild part about this is we have that cert store from earlier being so direct, and the persistence was broken on this part. They pointed the `Run` entry key at `msbuild` and gave it nothing. No arguments, no project files, no application to run, just a bare MS build invocation, and it just exits and dies. How do you go from this fancy cert store back to this junk?"

While this sample was the least finished component, it makes the campaign's financial and cryptocurrency-theft objectives clear.

## Lessons learned

Ryan and Jon wrapped up by three lessons to walk away with:

### **A shared Google Doc is executable content**

A container-bound Apps Script can run in the viewer's browser, report the viewer's real IP address, and avoid an OAuth consent prompt.

### **Open unknown documents while signed out**

This removes the Apps Script collection layer at no cost.

### **The rogue CA is the artifact most likely to survive cleanup**

Reimaging removes it; simply killing the process does not.

Ryan shared his perspective on the challenges of recognizing and triaging this kind of activity as a SOC analyst: "My mind definitely doesn't go to things like a rogue certificate authority in the trusted cert repository, and remediation of those kinds of artifacts is very important. A lot of these types of things would be missed during remediation, barring something like a full re-imaging of a host, which is, you know, the last thing you want to do. You want to be quite clinical in that cleanup."

## Coda: How about a million dollars instead?

As a final twist, the threat actor sent a last-ditch DM asking our researcher if they were looking for funding for any projects, claiming to have a connection willing to invest up to… *Dr. Evil voice*... one million dollars. 

*Figure 8: The threat actor's last ditch offer*

Jon had the last word: "Credit (no pun intended, or kind of pun intended) is due. They are nothing if not persistent when it comes to trying to get into people's machines. Salesman hears no, salesman changes the pitch. Say what you liked about the tradecraft, whoever is on the other end of this attack here, they don't give up."

**Like what you just read? Join us every month for Tradecraft Tuesday, our live webinar where we expose hacker techniques and talk nerdy with live demos.** __Snag your spot now!__
