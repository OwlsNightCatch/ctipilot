Title: ARMORY CASTLE and BT26-05: What Security Teams Need to Know

URL Source: https://www.beyondtrust.com/blog/entry/bt26-05

Published Time: 2026-10-15T00:00:00.000Z

Markdown Content:
_**Last Updated**_ _: October 16, 2026, at 12:00 p.m. EDT_

BeyondTrust published [security advisory BT26-05](https://www.beyondtrust.com/trust-center/security-advisories/bt26-05) and CVE-2026-102764 for a critical vulnerability in Remote Support. A suspected China-nexus espionage actor exploited a zero-day vulnerability. In collaboration with our Cybersecurity team, Mandiant is publishing its [analysis of the same actor](https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust) and vulnerability today. This post covers what we know about that actor, what has been observed of their behavior, and what you should do to defend against them and other actors that exploit similar vulnerabilities. **Before we continue, if you run a self-hosted Remote Support or Privileged Remote Access appliance and have not applied the patch for BT26-05, you must do that immediately.** Remote Support was confirmed to be vulnerable to this CVE. While our internal testing has not identified any way for an attacker to exploit this vulnerability in Privileged Remote Access, PRA shares the affected code, so out of an abundance of caution, we have released the patch for PRA and recommend self-hosted Privileged Remote Access customers apply it immediately. For more details on how to patch, see [security advisory BT26-05](https://www.beyondtrust.com/trust-center/security-advisories/bt26-05).

As of today we are withholding the technical details of the vulnerability. Publishing such details while self-hosted appliances are still being patched would place customers at an increased risk level, and our priority is their safety.

## Timeline of Events

Here is a short timeline of what happened and what we will be covering below:

*   **August 29, 2026:** The actor exploited a zero-day vulnerability against a single BeyondTrust-hosted Remote Support instance and a single self-hosted Remote Support appliance.

*   **September 27, 2026:**Successful exploitation of another security device provider becomes public, which initiates a hunt in our threat intel platform for similar activity.

*   **September 28, 2026:** Our Cyber Defense team's proactive threat hunting found indications of the event involving that one customer, and we contained the instance within 27 minutes of first detection. By that evening Product Security had reproduced how the actor got in, and Engineering began working on a fix.

*   **September 30, 2026:** Mandiant shared its findings from the self-hosted customer, which confirmed what we had found on September 28. Please read Mandiant’s [publication](https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust) for more details on their investigation.

*   **October 8, 2026:** BeyondTrust released the BT26-05 patch for the exploited vulnerability to SaaS and self-hosted customers. SaaS customer instances of both Remote Support and Privileged Remote Access were automatically patched.

*   **October 15, 2026:** Coordinated disclosure of the CVE, the public advisory, this post, and Mandiant's analysis, to aid in collective defense of our customers and the marketplace.

As of the time of the last update to this blog, we are only aware of the two impacted customers mentioned above, and have not seen evidence of adversary activity since August.

## What Is ARMORY CASTLE?

We assess with moderate to high confidence that this activity belongs to the China-nexus actor Google Threat Intelligence Group (GTIG) and Mandiant track as UNC5221, which Mandiant now calls ARMORY CASTLE. CrowdStrike tracks the same cluster as WARP PANDA. Our assessment rests on tradecraft, and it is consistent with Mandiant's. This threat actor rotates its infrastructure and tooling for every victim, so attribution here rests on behavior. The indicators from one intrusion rarely survive to the next.

Public reporting describes a state-sponsored espionage operation focused on long-term intelligence collection. ARMORY CASTLE’s documented targets include legal services, SaaS providers, business-process outsourcers, technology companies, and government. GTIG assesses that targeting technology firms helps the actor feed its development of new zero-day exploits. Its operations are built for longevity and persistent access. The threat actor has historically demonstrated a high degree of operational security awareness, professional practices, and tradecraft.

## Technical Analysis and Findings

### How ARMORY CASTLE Gains Initial Access

Edge and remote-access appliances are this actor’s preferred entry points. Mandiant and GTIG have publicly attributed zero-day exploitation of Citrix NetScaler ([CVE-2023-4966](https://nvd.nist.gov/vuln/detail/cve-2023-4966)) and of Ivanti Connect Secure ([CVE-2023-46805](https://nvd.nist.gov/vuln/detail/cve-2023-46805) and [CVE-2024-21887](https://nvd.nist.gov/vuln/detail/cve-2024-21887), then [CVE-2025-0282](https://nvd.nist.gov/vuln/detail/cve-2025-0282)) to UNC5221. In 2025, Mandiant reported that the actor took an Ivanti patch for a flaw that had been rated low risk, studied it, and turned it into working remote code execution against unpatched appliances. Its most recent target was BeyondTrust Remote Support, which we are documenting with [CVE-2026-102764](https://www.cve.org/CVERecord?id=CVE-2026-102764).

The actor uses a zero-day selectively against chosen targets, and once the vulnerability is public, the actor typically moves to broad exploitation of every instance still unpatched. Mandiant's post today warns defenders to expect the same with this vulnerability, and this should inform your defense.

Our working assessment is that this actor selects high-value software targets in advance and keeps a working model of the products the actor targets in an AI context that it uses on an ongoing basis to develop exploit chains. That assessment comes from the depth of product knowledge we observed and the speed with which the actor operated. We do not have forensic proof of the use of such AI-enabled tooling, but we recommend that defenders plan as though this assessment is accurate.

This aligns with an [analysis GTIG published](https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era) two weeks ago in which GTIG reported the number of exploited vulnerabilities nearly doubled in 2026 and documented the first known zero-day exploit script built with generative AI. In that report, they attributed much of the growth to the rapid weaponization of newly disclosed flaws. The time between a flaw becoming known - and an adversary using it - keeps shrinking, a trend that is accelerating with widespread adoption of AI by threat actor groups.

### What ARMORY CASTLE Does After Initial Access

[Mandiant's analysis](https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust) documents the post-exploitation activity in detail, including the actor's custom web shell and tunneling tool. Mandiant also shares file hashes and YARA rules to aid defenders.

In our own investigation of a single affected BeyondTrust-hosted instance, the behavior matched Mandiant's account. The broad shape:

*   **Takes hands-on control.** The operator plants a web shell and works interactively through it, over the appliance's existing web server.

*   **Leverages borrowed infrastructure.** The operator connects through commercial VPN exits and compromised home and small-office routers, so its traffic looks like consumer broadband, and the operator rotates that infrastructure between victims.

*   **Rapidly escalates privileges and establishes persistence.** The operator moves to full administrative control of the appliance within minutes and installs persistence designed to survive a reboot.

*   **Targets credentials.** A remote access appliance stores and brokers privileged credentials across an estate, which makes it a credential source and a map of who connects to what. The actor reads the appliance's stored secrets and uses administrative access in the application to reach downstream systems.

*   **Covers tracks.** The operator deletes logs and its own tooling before leaving.

That last point tells you where to look. Evidence kept only on the appliance may not survive, and what is present may have been manipulated and cannot be implicitly trusted. Evidence forwarded off the appliance or available from external control planes must be present for confirmation and verification. These external logs are critical for forensic analysis support.

## BeyondTrust's Investigation and Response

On September 27, two things happened: A separate zero-day campaign against another vendor's edge appliances became public, and Mandiant sent us a brief non-specific note that put the team on alert. Our automated threat intelligence pipeline queued separate hunts for each looking for similar techniques across our SaaS fleet. That edge-appliance hunt surfaced the affected SaaS instance on September 28, and we contained it 27 minutes after the compromise was identified, with the evidence preserved.

Approximately seven hours later, Product Security had identified the entry vector and reproduced it in a lab, and Engineering began building a fix. By September 30 we had validated that fix on a test build. Product Security ran variant analysis on the surrounding code, looking for other ways an attacker could reach the same weakness, while Engineering built and tested the patch for all supported versions of Remote Support and Privileged Remote Access. We took the time to add fixes for the additional paths the variant analysis had uncovered. We retested every supported version against the expanded patch and shipped it on October 8.

Detection across the industry runs on one common model: sensors raise alerts, and an automated triage layer decides which ones reach a human. We run that model, too, with control planes monitoring multiple layers of our SaaS fleet and infrastructure globally. Our sensors fired in real time when the actor escalated privileges, but the built-in triage tool in our third-party detection platform closed those alerts as false positives. To strengthen our ability to detect and respond to similar activity in the future, we are working with the vendor to ensure automated triage tools cannot close high-severity signals independently. We are also using our own agentic hunt platforms to reverify external dispositions before closing them.

We recommend every team relying on detection capabilities provided by a third-party should set the same default, and the truth is that you need to plan to do this for your first-party tooling as well.

The layer we’ve built on top of that model is the one that found this actor. Our threat intelligence pipeline turns newly published threats into hunts across our global infrastructure and third-party telemetry sources, and those hunts run whether or not an alert has fired. Our hunts look for what an attacker does on a system, not a vendor’s verdict on an alert.

Every defender should take two lessons from this:

1.   Treat a triage verdict as one input and keep the alerts it closes in scope for your hunts.

2.   Run a hunting program that starts with threat intelligence and works on its own cadence.

Automated triage is in most security stacks now, and we must assume capable adversaries are testing their tradecraft against the same commercial tools the rest of us buy.

## Recommended Actions for Security Teams

### 1. Patch.

BeyondTrust SaaS customers have already been patched, and no further action is required. Self-hosted customers should urgently review [security advisory BT26-05](https://www.beyondtrust.com/trust-center/security-advisories/bt26-05) and take any necessary actions to maintain the security of their deployment.

### 2. Reduce exposure.

Expose only the parts of a remote access appliance that your users and customers need to reach and restrict administrative interfaces to trusted networks. Allow outbound traffic from management appliances only to the destinations they need and monitor inbound and outbound traffic.

*   Guidance on securing network connectivity with our Remote Support appliance for self-hosted customers can be found here: [B Series Appliance on-premises security | RS On-prem](https://docs.beyondtrust.com/rs/docs/on-prem-security)

*   Guidance on securing network connectivity with our Privileged Remote Access appliance for self-hosted customers can be found here: [B Series Appliance on-premises security | PRA On-prem](https://docs.beyondtrust.com/pra/docs/on-prem-security)

### 3. Get your logs off the box.

Forward appliance syslog and session events to your SIEM in near real-time. This actor deletes local logs, and off-box copies are often the only record left.

*   Guidance on forwarding appliance logs and session events to your SIEM with our Remote Support Appliance for self-hosted customers can be found here: [Syslog guide | RS](https://docs.beyondtrust.com/rs/docs/syslog)

*   Guidance on forwarding appliance logs and session events to your SIEM with our Remote Support Appliance for self-hosted customers can be found here: [Syslog guide | PRA](https://docs.beyondtrust.com/pra/docs/syslog)

### 4. Hunt for the behavior.

Indicators from one victim rarely reappear at the next, so hunt for what the actor does:

*   **Unrecognized privileged or administrative sessions** originating from residential broadband or commercial VPN addresses that you cannot tie to a known administrator or ticket.

*   **Unrecognized script files** appearing in web directories, and web service accounts spawning shells.

*   **Unauthorized account, permission, or session-policy changes**, particularly modified permissions for “Jump Items” or “Teams” on the appliance.

*   **Unexpected gaps in log forwarding** that start and end within a single session.

Mandiant's [indicators and YARA rules](https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust) cover the actor's tooling.

BeyondTrust customers can request our [threat hunting package for this actor](https://trustportal.beyondtrust.com/product/beyondtrust/threat-intelligence-reports), which includes hunts mapped to Remote Support and Privileged Remote Access telemetry, via our trust portal.

### **5. Treat brokered credentials as exposed if you find anything.**

Rotate every credential the appliance stored or injected. Watch for those accounts authenticating outside a managed session or from unfamiliar locations. Review new multi-factor registrations on privileged accounts. Image the appliance before you rebuild it.

**If you believe you have evidence of exploitation of the vulnerability, contact us with a Sev 1 support request that cites “BT26-05.”**

## The Window for Defenders is Closing Fast

You can't control when an actor of this caliber finds its next zero-day in your software stack or your supply chain. You can control how long a patch sits uninstalled, how far an attacker can see from your appliance, and whether your logs survive the attack. Those are the gaps this type of actor depends on, and closing them is the best defense you have, both to defend against this threat actor and to guard against AI-accelerated vulnerability identification and weaponization.

## Acknowledgments

Our thanks to the Mandiant and Google Threat Intelligence Group (GTIG) team, who reached out early, worked on the investigation alongside us, and held their publication until our customers had time to patch.

Links/Buttons:
- [](https://www.onetrust.com/products/cookie-consent/)
- [Platform](https://www.beyondtrust.com/products)
- [Solutions](https://www.beyondtrust.com/solutions)
- [Resources](https://www.beyondtrust.com/resources)
- [Customers](https://beyondtrustcorp.service-now.com/csm)
- [Partners](https://www.beyondtrust.com/partners)
- [About](https://www.beyondtrust.com/company/overview)
- [Watch Demo](https://www.beyondtrust.com/demos)
- [Contact Us](https://www.beyondtrust.com/contact)
- [Learn More](https://www.beyondtrust.com/demo)
- [Get Support](https://docs.beyondtrust.com/)
- [English](https://www.beyondtrust.com/blog/entry/bt26-05)
- [Deutsch](https://www.beyondtrust.com/de)
- [français](https://www.beyondtrust.com/fr)
- [español](https://www.beyondtrust.com/es)
- [português](https://www.beyondtrust.com/pt)
- [한국어](https://www.beyondtrust.com/ko)
- [Register now.](https://www.beyondtrust.com/webinars/securing-machine-ai-agent-identites)
- [Blog](https://www.beyondtrust.com/blog)
- [security advisory BT26-05](https://www.beyondtrust.com/trust-center/security-advisories/bt26-05)
- [analysis of the same actor](https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust)
- [CVE-2023-4966](https://nvd.nist.gov/vuln/detail/cve-2023-4966)
- [CVE-2023-46805](https://nvd.nist.gov/vuln/detail/cve-2023-46805)
- [CVE-2024-21887](https://nvd.nist.gov/vuln/detail/cve-2024-21887)
- [CVE-2025-0282](https://nvd.nist.gov/vuln/detail/cve-2025-0282)
- [CVE-2026-102764](https://www.cve.org/CVERecord?id=CVE-2026-102764)
- [analysis GTIG published](https://cloud.google.com/blog/topics/threat-intelligence/vulnerability-discovery-and-exploitation-trends-in-the-ai-era)
- [B Series Appliance on-premises security | RS On-prem](https://docs.beyondtrust.com/rs/docs/on-prem-security)
- [B Series Appliance on-premises security | PRA On-prem](https://docs.beyondtrust.com/pra/docs/on-prem-security)
- [Syslog guide | RS](https://docs.beyondtrust.com/rs/docs/syslog)
- [Syslog guide | PRA](https://docs.beyondtrust.com/pra/docs/syslog)
- [threat hunting package for this actor](https://trustportal.beyondtrust.com/product/beyondtrust/threat-intelligence-reports)
- [securityinquiries@beyondtrust.com](mailto:securityinquiries@beyondtrust.com)
- [press@beyondtrust.com](mailto:press@beyondtrust.com)
- [Oct 14, 2026BeyondTrust And AWS: AWS IAM Account Access Manager Support in Identity Security InsightsBlog7m](https://www.beyondtrust.com/blog/entry/aws-account-access-manager-identity-security-insights)
- [Oct 6, 2026Weaponizing Claude Code Hooks: Building a C2 Through The Skill LifecycleBlog8m](https://www.beyondtrust.com/blog/entry/claude-code-hooks-c2-skill-security)
- [Oct 1, 2026Trust the Sandbox? How I Hijacked Vertex AI Agent Engine's API Response ChannelBlog13m](https://www.beyondtrust.com/blog/entry/vertex-ai-agent-engine-sandbox-hijack)
- [Sep 28, 2026Package Name to Role Credentials in Code Interpreter: Two RCE CVEs in the AgentCore Python SDKBlog14m](https://www.beyondtrust.com/blog/entry/amazon-bedrock-agentcore-python-sdk-rce-cves)
- [Sep 25, 2026OT Remote Access Is Becoming the New Control Point for Critical InfrastructureBlog7m](https://www.beyondtrust.com/blog/entry/ot-remote-access-zero-trust)
- [Identity Security Insights](https://www.beyondtrust.com/products/identity-security-insights)
- [AI Agent Security](https://www.beyondtrust.com/products/ai-agent-security)
- [Password Safe](https://www.beyondtrust.com/products/password-safe)
- [Privileged Remote Access](https://www.beyondtrust.com/products/privileged-remote-access)
- [Endpoint Privilege Management](https://www.beyondtrust.com/products/endpoint-privilege-management)
- [Entitle](https://www.beyondtrust.com/products/entitle)
- [Total PASM](https://www.beyondtrust.com/products/total-pasm)
- [Remote Support](https://www.beyondtrust.com/products/remote-support)
- [Active Directory Bridge](https://www.beyondtrust.com/products/active-directory-bridge)
- [Workload Credentials](https://www.beyondtrust.com/products/workload-credentials)
- [By Use Case](https://www.beyondtrust.com/solutions/use-case)
- [By Industry](https://www.beyondtrust.com/solutions/industry)
- [IT Compliance](https://www.beyondtrust.com/solutions/compliance)
- [Case Studies](https://www.beyondtrust.com/channel/case-studies)
- [Competitor Comparisons](https://www.beyondtrust.com/channel/competitor-comparisons)
- [Glossary](https://www.beyondtrust.com/resources/glossary)
- [Podcast](https://www.beyondtrust.com/podcast)
- [Research & Reports](https://www.beyondtrust.com/channel/research-reports)
- [Videos & Demos](https://www.beyondtrust.com/resources/videos)
- [Webinars](https://www.beyondtrust.com/resources/webinars)
- [Identity Security Risk Assessment](https://www.beyondtrust.com/products/identity-security-insights/assessment)
- [Professional Services](https://www.beyondtrust.com/services-training/professional-services)
- [Technical Account Management](https://www.beyondtrust.com/services-training/technical-account-management)
- [Health Checks](https://www.beyondtrust.com/services-training/professional-services?service-type=Health+Check)
- [BeyondTrust University](https://www.beyondtrust.com/services-training/beyondtrust-university)
- [Customer Support](https://docs.beyondtrust.com/?_gl=1*1uy7fu1*_gcl_aw*R0NMLjE3NzQzNjQ2NjkuRUFJYUlRb2JDaE1JckthTHBlRzRrd01WLVNoRUNCMWxGQkdPRUFBWUFTQUFFZ0pNelBEX0J3RQ..*_gcl_au*MTY4Nzg3NDI3NS4xNzczNDI1NDYz#support)
- [Customer Events](https://www.beyondtrust.com/events/upcoming)
- [Find a Partner](https://www.beyondtrust.com/partners/directory)
- [Technology Alliances](https://www.beyondtrust.com/partners/technology-alliances)
- [Become a Partner](https://www.beyondtrust.com/partners/apply)
- [Job Listings48](https://www.beyondtrust.com/company/overview/careers)
- [Employee Life](https://www.beyondtrust.com/company/overview/employee-life)
- [Leadership Team](https://www.beyondtrust.com/company/overview/leadership-team)
- [Press & Media](https://www.beyondtrust.com/press/listing)
- [Awards & Recognition](https://www.beyondtrust.com/awards)
- [Trust Center](https://www.beyondtrust.com/trust-center)
- [Modern Anti-Slavery Statement](https://assets.ctfassets.net/ahmdpntb02m6/7aNrSMP8WuGkqRi1IUpWyT/54cb9dbf7b642197256d92c6fa10b1b0/Modern_Slavery_Statement_January_2026.pdf)
- [Privacy](https://www.beyondtrust.com/privacy-center)
- [Manage Cookies](https://www.beyondtrust.com/privacy-center/cookie-notice)
- [Do Not Sell My Data](https://www.beyondtrust.com/privacy-center/privacy-rights)
- [WEEE Compliance](https://www.beyondtrust.com/weee-request)
