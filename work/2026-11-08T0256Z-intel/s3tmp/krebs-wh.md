---
title: Want to Rent an Internet Address at the White House?
url: https://krebsonsecurity.com/2026/11/want-to-rent-an-internet-address-at-the-white-house/
hostname: krebsonsecurity.com
sitename: krebsonsecurity.com
date: "2026-11-04"
categories: ['A Little Sunshine', 'Latest Warnings']
tags: ['AS2650', 'Ben Brundage', 'Infoblox', 'King Servers', 'Layer3 Intel', 'residential proxies', 'Spur', 'Synthient', 'Vladimir Fomenko']
fingerprint: "3f71fb11942030c3"
---
Several staffers at the White House are using computers or mobile devices equipped with residential proxy services that render their internet address available for others to rent, security experts warned today. One of the proxy services is a Russian company whose founder’s web hosting business was ground zero for cyberattacks against election systems in Arizona and Illinois in 2016.

The security firm **Layer3 Intel** said it detected multiple residential proxy nodes beaconing out from the internet address network reserved for the Executive Office of the President ([AS2650](https://ipgeolocation.io/browse/asn/AS2650)). Layer3 said the proxy activity was relatively persistent between October 5 to November 3, and that a review of the proxies available from AS2650 showed they exited from the White House network 236 times during that period.

The proxy tracking company **Synthient** [said](https://x.com/synthient/status/2118115310922518777) on Twitter/X that the activity it saw coming from AS2650 was related to multiple Windows 11 installations of a service called **Infatica**, a proxy program that is often integrated into “free” [mobile and desktop applications](https://krebsonsecurity.com/2021/03/is-your-browser-extension-a-botnet-backdoor/). Infatica’s founder **Vladimir Fomenko** is a Russian man whose hosting firm **King Servers** was home to six of the eight internet addresses used by Russia’s state security services to [compromise databases for election systems](https://edition.cnn.com/2016/08/29/politics/hackers-breach-illinois-arizona-election-systems/) in Arizona and Illinois in 2016.

There are dozens of residential proxy providers with varying degrees of legitimacy, many of them based in China or Russia. But at a minimum, they all make it simple for customers to rent someone else’s internet address as a way to anonymize their web traffic or spoof their true location. From a website’s perspective, the traffic from a proxy network user appears to originate from the rented IP address, not from the proxy service customer.

Layer3 Intel said the proxy exit nodes at the White House came from six internet addresses, on 26 of the 30 days, and that most of the activity happens in the evening, between 5 p.m. and midnight.

Incredibly, Infatica was not the only proxy service that reportedly has been reselling access to White House internet addresses: Layer3 Intel *said it found 28 separate residential proxy services were able to exit through this network*.

“This is public access,” the Layer3 Intel team [wrote](https://layer3intel.com/blog/residential-proxies-white-house-network). “Anybody can obtain it by signing up to a public residential proxy service, paying a few dollars and sending requests through it. We did not selectively target this network or try to make our probes exit from it. We caught this by chance, simply by requesting global rotating access through these services.”

The White House did not immediately respond to a request for comment.

As detailed in several stories here over the past year, residential proxy services are a major source of unwanted and often malicious traffic, including account takeover and other cybercrime activity, advertising fraud, and mass content scraping for AI projects.

They can also introduce serious security risks. In late 2025, it was discovered that cybercriminals were mass exploiting a widespread vulnerability in these services that allowed them to probe each proxy endpoint’s local network for vulnerable systems to infect with malware. In January 2026, dozens of proxy services were forced to patch their networks after Synthient Founder **Ben Brundage** showed how cybercriminals were [abusing a vulnerability](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/) in these residential proxy services to seize control over devices inside the local networks of unsuspecting users.

“Some of these resellers sell bandwidth for as low as 60 cents a Gigabyte, that means for less than a dollar you can gain access into some of the most confidential and trusted networks,” Brundage told KrebsOnSecurity. “The reseller ecosystem further enables this with any criminal able to buy access while skipping KYC \[Know Your Customer\] processes.”

All too often, these proxy services are beaconing out from employee devices brought into the workplace. App developers can embed software development kits (SDKs) provided by the residential proxy networks to monetize their software, allowing them to receive a small amount of money on each installation.

As risky as residential proxies can be for unsuspecting end users, they are all too commonly found on government and corporate networks. In a webinar in January 2026, the proxy tracking service **Spur** found residential proxies in nearly 300 government owned and operated networks, 318 utility companies, 166 healthcare companies or hospitals, and 141 companies in banking and finance. In a blog post earlier this year, the security firm **Infoblox** said it discovered that fully 65% of its customer base was querying one or more residential proxy related domains.

Incredible things happening in america rn

We may never know but I think that there are some staffers who forced the IT department to give them admin rights.

I’ve experienced that in a county courthouse. All of the judges had admin rights and the computers were set to never lock the screen. The county IT director allowed this.

Long time sysadmin here, tough to tell your boss no.

My last job was in healthcare, even with the HIPAA law (plus the HITECH changes) and training I would still see usernames and passwords written down all over the place. The owner and the CEO had laptops, which I kept telling them they needed to enable encryption on in case they were lost or stolen, would just shrug and ignore me.

I was also part of the problem, my entire career it was always get everything working first, then deal with security afterword, especially when troubleshooting. Luckily I realized that wasn’t going to cut it before something bad happened. But having to think through the security implications of a possible fix while under the pressure to get something crossed off the list really slowed me down.

I left the industry, but I haven’t seen much change. My two cents is nothing is going to change until the government comes in and starts forcing IT to be regulated like a lot of other trades.

The crazy part is IT is highly regulated in the defense industry. To the point that it is almost ridiculous. If you’re working on CUI or Classified projects, the NIST Standards are very strict. Whitelisted + vetted applications only, multiple layers of authorization for permission changes, forced encryption at every level, incredibly limited admin access, domestic servers only, FedRAMP platforms only, etc. The regs are written to be very secure. Obviously, lots of companies aren’t complying, and audits for companies in the DIB with CUI access (CMMC Phase 2) have been put on pause by the current admin, but a lot of them are indeed complying, since that’s the law. Some are spending well over half a million in a year to comply, as a medium sized business. It sucks to hear we put in all this effort, and actual government agencies and entities (White House staffers?! Have random freeware installed? Seriously?!) have poor security.

Well that didnt help stop Morpho/L1/Safran from massive gaffes leading to being relieved of a large swath of CPII, and they are a huge contract. While that is slightly out of scope of your specific reference, I think it helps reframe the perspective of absurdity (outsourcing in the first place)…

“65% of its customer base was querying one or more residential proxy related domains.”

That’s a lot of percentages.

Air gap everything

Hard to air gap the superbox a junior staffer put on the White House WiFi to watch The Last Showgirl.

FUNNY!

Also true. . .

An arc for the history books

Ahhhh another example of the security failures by our current administration.

Thank goodness the people spoke and maybe we’ve started to turn this country around.

I hear that but I don’t have much confidence in any of the dinosaurs in the White House alumni as far as cyber security standards go.

I hear that but I don’t have much confidence in any of the dinosaurs in the White House alumni as far as cyber security standards go.

It’s not a surprise. There’s already a big fat orange Russian proxy in the White House. I guess there’s no need to investigate it further.

Bro, you need to go touch grass and stop making everything in the world about trump. There is so much more out there to make fun of.

This is about the White House. The White House is where Trump is boss. It’s absurd to pretend he doesn’t matter.

HA. Sadly true.

Any easy way to determine if you have one running off your network or device?

DNS query logging and analysis is the most favored method (and easiest) even if its not perfect. This might need to be paired with capture or denial of DNS traffic destinated for “not your server” (firewalling).

Those pesky Biden era network security rules are so passé.

DNS query logging and analysis is the most favored method (and easiest) even if its not perfect. This might need to be paired with capture or denial of DNS traffic destinated for “not your server” (firewalling).

Purposefully placed? Seems so. I’m sure Putin gifted Donald some tech and Trump dutifully plugged it in to communicate w/ his master. No worries, it’s just our national security and also treason. Right?

I found the writing on this article disappointing. Initially, it gave me the impression that one or more people on the White House staff had been selling proxy access to their computers — that would be a corruption charge. But with some help from ChatGPT, I find no evidence of official corruption. What we have here is the fairly common situation of employees loading software that unbeknownst to them contained malware which opened a backdoor – one exploit of which is proxy service sold by hackers that the employees were completely unaware of. Incompetence yes, corruption no. There were 32,211 cybersecurity incidents in FY 2023 per the OFFICIAL OMB FISMA REPORT. This is unfortunately another such incident, but ChatGPT’s estimate so far is that it involved less than 10 compromised computers. Let’s take the politics and hype out of the writing.

Go outside, look up in the sky, and see if you can spot The Point as it goes flying over your head.

I really hope I am missing the joke and this is sarcasm

Hi guys, Brad’s dad here.

Sorry, we didn’t know he’d managed to get access to the internet again, obviously we are very disappointed in him for this, and voting for trump, but more so that he’s using ChatGPT to break down an article that’s obviously clear and concise.

Brad, you’re grounded, enjoy the blue wave inside without your toys.

Sincerely,

Mr Larkin

Guess nobody in threat intel knows what callbacks on guest WiFi look like. Really lame.

This administration has thrown cybersecurity out the window along with so many other programs.

How about the time early in the latest Trump fiasco when Hegseth announced a USA bombing raid on an unsecured Signal chat that included the editor of the Atlantic Magazine?

A lack of security ‘consciousness’ seems endemic in this cabal. I guess in part it is driven by the Trump ‘free pass to break the law without liability’ given to him by his Supreme Court. The law breakers he has appointed no doubt have a promise of a pardon from Trump. Of course they will have to get in line since those paying for their pardons have priority.

Is Trump a Russian Agent recruited in the 1990’s during the breakup of the USSR?

The idea of leasing out address space tied to a government block is fascinating, but the real worry is how much trust downstream networks place in who announces a prefix. If BGP origin validation is not airtight, a rented slice with a White House label is a gift to anyone doing phishing or traffic hijacks.

What struck me is how mundane the mechanism is: a staffer installs a free app, and suddenly a government IP becomes rentable inventory. Egress filtering and device policy on staff phones seem like a far cheaper fix than anything fancy at the routing layer.

Good reporting. Reputation-based allowlists treat a White House address as inherently trustworthy, and residential proxy resale quietly breaks that assumption. Defenders should probably stop giving blanket trust to any IP range based on who owns it.

I wonder how many other agencies have the same exposure and just have not been named yet. Proxy SDKs bundled into free apps are hard to spot, so an inventory of apps on managed devices would be a sensible first step.

If the software allows 3rd parties to exit the device then the 3rd parties (or at a minimum those who control the software itself) have internal access too.

Yet another reason why soon enough Human stupidity will result in AI locking us all out of control in order to maximise it’s own survival.

It’s that basic. Lifeforms evolve to survive and until now we thought we were the most intelligent.

Stopped mid-scroll on “Want to Rent an Internet Address at the White House? – Krebs on Security” at “Synthient’s depiction of the frequency of outgoing proxy traffic from the dedicat”. The concrete detail is what made me keep the tab open. Nudged me into another RNGdle round before I closed the tab.

I completely understand your concern about customizing the WordPress comments cookie consent text, and it’s great that you’ve found a way to modify it in an update-stable way. I’ve been looking for a solution to this problem for a while now, so I appreciate you sharing your approach. By the way, I’ve also come across some interesting discussions on cookie consent best practices on sites like blog.mozilla.org.
