Title: Next.js Ships Out-of-Band Patch for Two Critical RCE Flaws in Caching and SVG Processing

URL Source: https://thehackernews.com/2026/10/nextjs-ships-out-of-band-patch-for-two.html

Published Time: Sun, 18 Oct 2026 22:31:42 GMT

Markdown Content:
[](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9mXutJ2QPpC1NUCUZWdHjUDUGPSD3DaDY4b-T1EXbg07sNWADsV43EvUacKzn4Ohp2bRbD93t8kXBpv513XdMZEnMh8eNkY1bBaSuGICWbituq_jgWNCjQa_Cq6Ur0jInsfEwsHfdInKq4Tcp2kmfuYoCIMrgWcWwtzFlRPePDpW9gwemIkQpJXEVaHU/s1700-nu-rw-lo-l85-e365/nextjs-rce.jpg)

Next.js released an [out-of-band security update](https://nextjs.org/blog/nextjs-security-update-october-14-2026) on October 14 that fixes two critical flaws allowing unauthenticated remote code execution, along with a high-severity denial-of-service flaw.

One code-execution flaw is in React Server Components, and the other in librsvg, the open-source library Next.js uses through the sharp package to handle SVG images.

The fixes are in Next.js 16.4.1 and 15.5.28, the current Active and Maintenance long-term support (LTS) releases.

### What Was Fixed

The update covers three separate issues. Vercel, which develops Next.js, rated both code-execution flaws critical, each with a CVSS score of 9.5. The table lists the versions each issue affects and the version that fixes it.

| Issue | Affected versions | Fixed in | Who is exposed |
| --- | --- | --- | --- |
| Code execution through `use cache` ( [GHSA-673q-mjm6-r5xr](https://github.com/vercel/next.js/security/advisories/GHSA-673q-mjm6-r5xr) ) | 16.0.0 through 16.4.0 | 16.4.1 | App Router apps with Cache Components enabled, where a `use cache` function returns more than one typed array |
| Code execution through SVG images (CVE-2026-96889, [GHSA-2464-fhr4-w9xw](https://github.com/vercel/next.js/security/advisories/GHSA-2464-fhr4-w9xw) ) | 10.0.0 through 15.5.27, and 16.0.0 through 16.4.0 | 16.4.1, or 15.5.28 with `sharp` 0.35.5 or later | Apps that pass attacker-supplied SVG files to `sharp` on glibc-based Linux |
| Denial of service through Server Actions ( [GHSA-p3m5-59mp-jv5r](https://github.com/vercel/next.js/security/advisories/GHSA-p3m5-59mp-jv5r) ) | 13.0.0 through 15.5.27, and 16.0.0 through 16.4.0 | 15.5.28, 16.4.1 | App Router apps with at least one Server Action |

### Who Is Affected

The first code-execution flaw is in React Server Components, the React feature that runs user-interface components on the server. [React's advisory](https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3) covers three packages, react-server-dom-webpack, react-server-dom-parcel, and react-server-dom-turbopack, in versions 19.0.0 through 19.3.0. It describes the flaw as affecting "extremely rare cases where responses transport multiple typed arrays and an attacker-controlled value."

In a Next.js app, the trigger is a `use cache` function that returns more than one typed array, so only version 16 apps that enable Cache Components, the feature behind `use cache`, are exposed. Vercel says to upgrade even if your app has no such function.

[](https://thehackernews.uk/ai-agent-methods-d)

The second flaw is a memory bug in librsvg, the library that renders SVG images, which Next.js reaches through the bundled `sharp` package. Code execution is possible when Next.js runs on glibc-based Linux, according to the advisory.

By default, Next.js does not optimize SVG files. Serving them through the image optimizer requires turning on a setting called [`dangerouslyAllowSVG`](https://nextjs.org/docs/app/api-reference/components/image). The same library also renders images for `next/og`, the feature that builds social-preview images, when that feature runs on the Node.js runtime.

The third flaw is a denial-of-service issue. In App Router apps that define at least one Server Action, crafted requests can push one server process to full CPU use and stop it from handling other requests. Apps on the Pages Router, or with no Server Actions, are not affected.

Exposure can differ by host. Netlify [said](https://www.netlify.com/changelog/2026-10-14-nextjs-react-security-vulnerabilities/) its platform does not run the image-optimizer code path and that the flaws have limited impact on its setup, while still recommending the upgrade.

### What to Do

Upgrade to Next.js 16.4.1 if you run version 16, or 15.5.28 if you run version 15, then rebuild and redeploy.

Vercel's advisory says upgrading Next.js makes package managers supply the fixed `sharp` automatically. On version 16 that holds, because 16.4.1 requires `sharp` 0.35.5.

On version 15 it may not. 15.5.28 still accepts the older, affected `sharp` 0.34.x, and upgrading over an existing install can leave that version in place. Check with `npm ls sharp` and update `sharp` to 0.35.5 or later if it is older.

If you cannot upgrade Next.js right away, the image flaw has an interim option: make sure `sharp` is 0.35.5 or later, or block SVG rendering in `sharp` with `sharp.block({ operation: ["VipsForeignLoadSvg"] })`, as the [sharp advisory](https://github.com/advisories/GHSA-wq5f-xc86-pv6w) describes. The `use cache` and Server Actions flaws have no workaround, and only the upgrade closes them.

As of October 15, the `use cache` and Server Actions advisories had no CVE and did not appear in the npm advisory feed that `npm audit` uses, so dependency scanners may not warn you about them. The image flaw does surface, through `sharp`'s own advisory.

### Why the Image Flaw Keeps Returning

This is the third time since August that image processing in Next.js has produced a code-execution flaw. In August, a bug in libheif, reached through `sharp`, allowed code execution when the optimizer handled a crafted [AVIF image](https://thehackernews.com/2026/08/nextjs-patches-critical-avif-and.html). In September, a flaw in [`next/og`](https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html) let attacker-controlled text change the SVG it generated.

Next.js did not change its own image code this time. 16.4.1 ships the same optimizer as 16.4.0 and fixes the image flaw by raising the bundled `sharp` to 0.35.5, which carries a patched librsvg (2.63.2).

The librsvg bug, [CVE-2026-96889](https://access.redhat.com/security/cve/cve-2026-96889), was made public on September 23 and fixed in `sharp` on September 27. Red Hat scored it 7.8 and said exploiting it needs user interaction, such as opening a malicious file. Vercel rated the Next.js exposure 9.5 and reachable over the network.

[](https://thehackernews.uk/network-defense-d)

The researcher who reported the librsvg bug, Rafael B. Dias, says it is the weakness behind September's `next/og` flaw. A working exploit for that earlier flaw, built for one specific server setup, has since been published.

sharp's maintainer also warns that whether the flaw ends in code execution or only a crash can come down to the server's Node.js build, because the official Node.js binaries are not hardened against this kind of memory attack.

### Not the Same as React2Shell

The React Server Components flaw sits in the same three packages as [React2Shell](https://thehackernews.com/2025/12/critical-rsc-bugs-in-react-and-nextjs.html), the maximum-severity flaw disclosed in December 2025 that attackers exploited at scale. This one is far narrower. React describes it as affecting "extremely rare cases where responses transport multiple typed arrays and an attacker-controlled value."

As of October 15, there are no public reports that any of the three flaws fixed on October 14 has been used in attacks.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

Links/Buttons:
- [](https://twitter.com/thehackersnews)
- [](https://www.linkedin.com/company/thehackernews/)
- [](https://thehackernews.com/2026/10/nextjs-ships-out-of-band-patch-for-two.html#link_share)
- [](https://thehackernews.uk/network-defense-d)
- [ Get the Latest News](https://thehackernews.com/2026/10/nextjs-ships-out-of-band-patch-for-two.html#email-outer)
- [Webinars](https://thehackernews.com/p/upcoming-hacker-news-webinars.html)
- [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)
- [Vulnerabilities](https://thehackernews.com/search/label/Vulnerability)
- [Cyber Attacks](https://thehackernews.com/search/label/Cyber%20Attack)
- [Expert Insights](https://thehackernews.com/expert-insights/)
- [Awards](https://awards.thehackernews.com/)
- [Free eBooks](https://thehackernews.tradepub.com/)
- [About THN](https://thehackernews.com/p/about-us.html)
- [Jobs](https://thehackernews.com/p/careers-technical-writer-designer-and.html)
- [Advertise with us](https://thehackernews.com/p/advertising-with-hacker-news.html)
- [ Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](https://thehackernews.com/p/submit-news.html)
- [](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
- [](https://www.instagram.com/thehackernews/)
- [ RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
- [Next.js Ships Out-of-Band Patch for Two Critical RCE Flaws in Caching and SVG Processing](https://thehackernews.com/2026/10/nextjs-ships-out-of-band-patch-for-two.html)
- [out-of-band security update](https://nextjs.org/blog/nextjs-security-update-october-14-2026)
- [GHSA-673q-mjm6-r5xr](https://github.com/vercel/next.js/security/advisories/GHSA-673q-mjm6-r5xr)
- [GHSA-2464-fhr4-w9xw](https://github.com/vercel/next.js/security/advisories/GHSA-2464-fhr4-w9xw)
- [GHSA-p3m5-59mp-jv5r](https://github.com/vercel/next.js/security/advisories/GHSA-p3m5-59mp-jv5r)
- [React's advisory](https://github.com/react/react/security/advisories/GHSA-xqc2-xf4c-x3h3)
- [dangerouslyAllowSVG](https://nextjs.org/docs/app/api-reference/components/image)
- [said](https://www.netlify.com/changelog/2026-10-14-nextjs-react-security-vulnerabilities/)
- [sharp advisory](https://github.com/advisories/GHSA-wq5f-xc86-pv6w)
- [AVIF image](https://thehackernews.com/2026/08/nextjs-patches-critical-avif-and.html)
- [next/og](https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html)
- [CVE-2026-96889](https://access.redhat.com/security/cve/cve-2026-96889)
- [React2Shell](https://thehackernews.com/2025/12/critical-rsc-bugs-in-react-and-nextjs.html)
- [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
- [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)
- [Web Security](https://thehackernews.com/search/label/Web%20Security)
- [Researchers Demonstrate OpenBSD Root Exploit Chaining 37-Year-Old Shared-Memory Bug](https://thehackernews.com/2026/10/researchers-demonstrate-openbsd-root.html)
- [Critical PwnEscape Linux Kernel Vulnerability Lets Guest VMs Read Host Memory](https://thehackernews.com/2026/10/critical-pwnescape-linux-kernel.html)
- [ThreatsDay: Adobe RCE, DNS Wallet Theft, NVIDIA Container Escape, Self-Healing Backdoor + 23 More](https://thehackernews.com/2026/10/threatsday-adobe-rce-dns-wallet-theft.html)
- [Citizen Lab Traces Zero-Click Candiru Spyware Infections at Al Jazeera to Targeted Online Ads](https://thehackernews.com/2026/10/citizen-lab-traces-zero-click-candiru.html)
- [NGINX Fixes 5 Flaws, Including Possible RCE and a TLS Bug That May Skip Client-Cert Checks](https://thehackernews.com/2026/10/nginx-fixes-5-flaws-including-possible.html)
- [Palo Alto Networks Patches PAN-OS Authenticated RCE Flaw Amid Active Exploitation](https://thehackernews.com/2026/10/palo-alto-networks-patches-pan-os.html)
- [GhostAction Compromises About 1,900 GitHub Accounts, Targets Over 30,000 Repositories](https://thehackernews.com/2026/10/ghostaction-compromises-about-1900.html)
- [Cisco Warns of Active Attacks Exploiting New Critical Secure Email Gateway Vulnerability](https://thehackernews.com/2026/10/cisco-warns-of-active-attacks.html)
- [Langflow's Critical Authenticated RCE Flaw Targeted in 1,423 Honeypot Exploit Attempts](https://thehackernews.com/2026/10/langflows-critical-authenticated-rce.html)
- [Hackers Backdoor Nextcloud Servers Through Critical Flaw in Collabora’s Built-in CODE App](https://thehackernews.com/2026/10/hackers-backdoor-nextcloud-servers.html)
- [U.S. Shuts Down Over 40 Laptop Farms, Charges 14 in North Korean IT Worker Fraud](https://thehackernews.com/2026/10/us-shuts-down-over-40-laptop-farms.html)
- [curl Patches HTTP/2 Upload Flaw After PoC Demonstrates Client-Side Code Execution](https://thehackernews.com/2026/10/curl-patches-http2-upload-flaw-after.html)
- [Researchers Used a Public OpenAI Model to Build a $250,000 Chrome Full-Chain Exploit in Six Days](https://thehackernews.com/2026/10/researchers-used-public-openai-model-to.html)
- [AI-Found Linux Kernel Flaw Gives Local Users Root, and Can Break a Guest Out to the Host](https://thehackernews.com/2026/10/ai-found-linux-kernel-flaw-gives-local.html)
- [Microsoft Patches Record 1,413 Flaws, Including Exploited Windows Shell Bug](https://thehackernews.com/2026/10/microsoft-patches-record-1413-flaws.html)
- [OpenAI Employee Arrested for Allegedly Planting Hidden Recorder in Executive Conference Room](https://thehackernews.com/2026/10/openai-employee-arrested-for-allegedly.html)
- [Anthropic Warns Small AI Models Could Soon Form Self-Propagating IoT Botnets](https://thehackernews.com/2026/10/anthropic-warns-small-ai-models-could.html)
- [Docker Fixes Critical Two-Year-Old Hub Flaw That Let One User Push Images as Another](https://thehackernews.com/2026/10/docker-fixes-critical-two-year-old-hub.html)
- [SAP Discloses Critical CVSS 10 Flaw in Cloud SDK for Python Allowing OAuth2 Credential Theft](https://thehackernews.com/2026/10/sap-discloses-critical-cvss-10-flaw-in.html)
- [LG Smart TVs Vulnerable to Pre-Auth Root Takeover From Local Network](https://thehackernews.com/2026/10/lg-smart-tvs-vulnerable-to-pre-auth.html)
- [Attackers Heat French Supermarket Fridges Up to 50°C by Hijacking Danfoss Controllers](https://thehackernews.com/2026/10/attackers-heat-french-supermarket.html)
- [GitLab Patches CVSS 10.0 Flaw That Could Let Unauthenticated Users Run Server Code](https://thehackernews.com/2026/10/gitlab-patches-cvss-100-flaw-that-could.html)
- [⚡ Weekly Recap: Helpdesk 0-Days, Rogue Certs, ShinyHunters Arrest, AI-Fooling Malware and More](https://thehackernews.com/2026/10/weekly-recap-helpdesk-0-days-rogue.html)
- [Researchers Publish Working Exploit for Pre-Auth AnyDesk Linux Flaw That Gives Root Access](https://thehackernews.com/2026/10/researchers-publish-working-exploit-for.html)
- [Download the 2026 Agent Security Report for a Five-Step Risk Reduction Framework](https://thehackernews.uk/agent-trends-2026)
- [Get the Five-Stage Identity Maturity Roadmap for Governing AI Agents](https://thehackernews.uk/security-future-2027)
- [Benchmark Your AI Risk Priorities Against 1,600 CISOs—Download the 2026 Report](https://thehackernews.uk/future-ciso-trends)
- [No Exploit Yet? Preview the Summit Demo on Validating CVE Exposure](https://thehackernews.uk/event-2026)
- [Shadow AI to Governed AI How to Find and Control AI Agents Before They Become Insider Threats AI agents are already accessing sensitive data and systems—learn how to discover them, control their permissions, and reduce insider risk before it becomes a breach. Register](https://thehacker.news/ai-insider-threat?source=below)
- [Roadmap for AI-Ready Security Operations Evaluate Attack Surface Visibility With an AI Threat Readiness Framework Learn how to assess AI threat readiness, strengthen attack surface visibility, and prepare security operations for emerging threats in this practical webinar. Register](https://thehacker.news/ai-threat-readiness?source=below)
- [11 Real Stories: How Identity Exposure Unlocks Active Attack PathsMap cross-domain privilege escalation to sever breach routes at key choke points.](https://thehackernews.uk/xmcyber-c)
- [Governance Sets the Ceiling on Your AI Security ProgramSee the five moves that raise a Stage 2 Govern score to a defensible Stage 3.](https://thehackernews.uk/2026-ai-field)
- [FBI Cyber Division's Brett Leatherman Keynotes SANS CDI 2026, Dec 15Join SANS CEO James Lyne and the FBI on ransomware disruption and intel sharing, during SANS training in D.C.](https://thehackernews.uk/cybersecurity-defense)
- [Videos](https://thehackernews.com/videos/)
- [The Alert Fatigue Trap: Why Consolidation Only Solves Half the Problem October 12, 2026 Read ➝](https://thehackernews.com/expert-insights/2026/10/the-alert-fatigue-trap-why.html)
- [Tamnoon CEO Marina Segal on the Self-Healing Cloud: Why It Starts With a Machine That Knows When Not to Act October 12, 2026 Read ➝](https://thehackernews.com/expert-insights/2026/10/tamnoon-ceo-marina-segal-on-self.html)
- [Your Employees Are Adopting AI Faster Than You Can See It October 5, 2026 Read ➝](https://thehackernews.com/expert-insights/2026/10/your-employees-are-adopting-ai-faster.html)
- [When AI Writes the Code, Who Owns the Security Decisions? October 5, 2026 Read ➝](https://thehackernews.com/expert-insights/2026/10/when-ai-writes-code-who-owns-security.html)
- [Privacy Policy](https://thehackernews.com/p/privacy-policy.html)
