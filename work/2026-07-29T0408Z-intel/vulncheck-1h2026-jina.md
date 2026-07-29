Title: VulnCheck State of Exploitation 1H-2026  | Blog | VulnCheck

URL Source: https://www.vulncheck.com/blog/state-of-exploitation-1h-2026

Markdown Content:
Over the past six months, we’ve seen a [significant change in vulnerability discovery and disclosure](https://www.vulncheck.com/blog/ai-assisted-vulnerability-discovery) resulting in a substantial increase in the number of CVEs disclosed. This increase has come with warnings about the increase in vulnerability discovery by Autonomous AI systems, creating a “dangerous” scenario for the software ecosystem. So, I was curious to explore: are more vulnerabilities being discovered and disclosed, resulting in more vulnerabilities being exploited? Is the rate at which vulnerabilities are being exploited faster? Are vulnerabilities being discovered with AI tools more dangerous? Or are we all feeding into the AI-Assisted vulnerability discovery hype cycle?

**Key takeaways from VulnCheck’s analysis in the First Half of 2026 include:**

*   In the first half of 2026, 23.43% of KEVs showed evidence of exploitation on or before the day the CVE was published. A slight drop percetage wise from the 28.93% of KEVs we observed in 2025.
*   At the same time, vulnerabilities appear to be being exploited faster, with the median time from CVE publication to KEV falling from 120 days in 2025 to 80 days during the first half of 2026.
*   Exploitation activity early in the CVE lifecycle remained steady, with roughly 200 CVEs becoming exploited within 31 days in the first half of 2026. Early exploitation activity has not scaled at the same pace as CVE issuance.
*   Content management systems remained the most targeted technology category, accounting for one-third of all KEVs, a more significant percentage of KEVs than we've seen historically.
*   Of 1,061 vulnerabilities attributed to AI-assisted discovery, only 14, or 1.3%, have been confirmed as exploited in the wild, roughly matching the overall exploitation rate of all vulnerabilities in the first six months of the year.
*   AI products are emerging as a new attack surface, with known exploitation affecting model-building tools, workload-scaling platforms, AI gateways, agents and workflow automation.
*   Anthropic reported more than 23,000 findings through Project Glasswing, but only 126 have resulted in published CVEs, and just one has been confirmed as exploited in the wild.

We started our research by looking at the rate at which vulnerabilities are being exploited. This analysis includes every Known Exploited Vulnerability added to [VulnCheck KEV](https://www.vulncheck.com/kev) during the first half of 2026, based on CVE publication date and earliest evidence of exploitation. We identified 495 KEVs during that period.

In 2025, [28.93% of KEVs](https://www.vulncheck.com/blog/state-of-exploitation-2026) were disclosed as exploited on or before the day the CVE was published. That figure dropped to 23.43% in the first half of 2026. At the same time, the median time from CVE publication to KEV fell from 120 days to 80 days, meaning that while there is slightly less evidence of exploitation on or before a CVE being published, vulnerabilities are reaching KEV status much faster overall.

With 23.43% of KEVs exploited on or before the day the CVE is issued, and a median of just 80 days to reach KEV status, it's clear why [CISA issued updated guidance in BOD 26-04](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk). The directive recommends prioritizing remediation based on risk and patching as aggressively as within three days when there's evidence of exploitation, automatability, high technical impact, and/or public exposure.

Looking at the past several years, vulnerability volumes have increased substantially, so we wanted to explore whether known exploited vulnerabilities were growing at a similar rate. We looked at the data in several ways.

The chart above shows the ratio of new KEVs added to VulnCheck KEV compared to the number of CVEs published during the same period. As both CVE and KEV volumes have continued to increase, the KEV-to-CVE ratio has declined over the past two years, peaking at 2.7% in the second half of 2023 and falling to 1.4% in the first half of 2026.

While the first half of 2026 saw a 10% increase in KEVs compared to the prior six months, CVE volume grew at a much faster rate of 45%, resulting in a significant drop in the KEV-to-CVE ratio. Of course, exploitation often occurs months or even years after a vulnerability is disclosed, so it's still too early to determine whether exploitation volumes will eventually follow the same growth trend as CVE issuance or level off at current rates. We'll have to wait and see how publicly available Frontier AI Cyber models continue to progress over the next year.

Next, I performed a cohort analysis looking at the publication date of the CVE for every KEV, grouped into half-year cohorts going back to 2020. This provides a view into long-term trends in vulnerability exploitation based on when CVEs were issued. The significant increase in exploited CVEs beginning in 2024 appears to closely align with the rapid growth in WordPress plugin-related KEVs after Patchstack, Wordfence, and WPScan began scaling CVE assignment for WordPress plugins.

The diagonally shaded segments represent lead time buckets that have not yet fully matured, so those bars will likely continue to grow as additional vulnerabilities are confirmed to have been exploited and new cohorts are added over time. Early exploitation activity in the first half of 2026 is holding steady rather than accelerating: roughly 200 CVEs reached KEV within 31 days of publication in 2026 H1, in line with 2024 (196) and 2025 (194). But because CVE issuance has grown so sharply over the same period, that same activity represents a smaller share of published CVEs, meaning early exploitation is not scaling at the same pace as CVE issuance. That said, this is still early analysis. Exploitation evidence often surfaces well after a CVE is published, so it will take time before we fully understand how recently published CVEs contribute to future exploitation trends.

When we look at the top technology categories being targeted by exploitation activity, Content Management Systems (CMS) stand out, accounting for one-third of all KEVs we've added in the first half of 2026. It's typical for CMS to rank as a top category, but this is a more significant percentage of KEVs than we've seen historically. There has also been a recent advisory this month from the [Australian Signals Directorate on a large scale exploitation campaign targeting website content management systems](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/large-scale-exploitation-campaign-targeting-website-content-management-systems-cms), which seems to align with the broader exploitation trend in CMS. While the large volume is associated with WordPress plugins, many CMS platforms have been targeted, including Drupal, Ghost, Kentico Xperience, and a handful of others. Given that CMS remains the single largest exploited category and shows no signs of slowing, organizations running any of these platforms should treat plugin and core patching as a standing priority.

Earlier this year, we researched Network Edge Devices in our [2026 State of Exploitation: Exploiting The Network Edge](https://www.vulncheck.com/blog/network-edge-device-report-2026). Network Edge Devices continue to be highly targeted, and the large majority of network edge device manufacturers continue to have new Known Exploited Vulnerabilities. Vendors that saw new KEV additions in the first half of the year include Cisco, Palo Alto, CheckPoint, F5, Juniper, Fortinet, SonicWall, Ubiquiti, TOTOLINK, Tenda, D-Link, Netgear, Linksys, and several others. It's also worth noting that during the first half of 2026, CISA issued [BOD 26-02, Mitigating Risk From End-of-Support Edge Devices](https://www.cisa.gov/news-events/directives/bod-26-02-mitigating-risk-end-support-edge-devices).

From a speed perspective, Security Tools (Splunk, Microsoft Defender, Trend Micro Apex One, Fortinet FortiSIEM, Fortinet FortiSandbox, Aqua Security Trivy, etc.), Developer Tools, Device Management Platforms (Ivanti EMM/Sentry, Fortinet EMS, SolarWinds, ConnectWise, Microsoft Configuration Manager, etc.), and Desktop Applications (Office, Adobe Acrobat, Weaver E-Suite, Notepad++, etc.) appeared to be exploited at a faster rate than other technology categories during the first half of 2026. This is likely due to the expansive deployments and access these technologies provide in Enterprise environments.

During the first half of 2026, we saw an increase in known exploited vulnerabilities targeting AI products. These products, many of which are open source projects, are used for model building, workload scaling, AI gateways, AI agents, AI workflow automation, and more. AI is increasingly being given access to sensitive corporate information as well as key infrastructure, often containing privileged information, and are often an easy target for Remote Code Execution (RCE), so it's logical that attackers would start experimenting with accessing these services.

We've observed exploitation activity across 10 of the 28 KEVs identified in AI systems in VulnCheck Canaries. With LangFlow, we've seen attackers gain initial access using exploits targeting both CVE-2026-0769 and CVE-2026-5027, harvest credentials, likely for services such as OpenAI and Claude, deploy cryptominers, and attempt lateral movement. Neither of these vulnerabilities have been added to CISA KEV.

Recently, we've seen a growing emphasis on AI-assisted vulnerability discovery. In April, Anthropic announced Project Glasswing, warning that AI-assisted vulnerability discovery could enable attackers to hijack systems, disrupt operations, or steal data. I immediately began [tracking disclosures attributed to Anthropic](https://github.com/patrickmgarrity/Anthropic-Credited-CVEs) to understand whether any of the vulnerabilities they discovered were ultimately exploited in the wild. While doing that, the [Berkeley Vulnerability Research Initiative](https://vuln.cs.berkeley.edu/) launched, providing another source for tracking AI-assisted vulnerability discovery. I consolidated both datasets and correlated them with VulnCheck KEV to better understand how often AI-assisted discoveries end up being exploited in the wild. Across both datasets, 1,061 vulnerabilities attributed to AI-assisted discovery. Of those, 14, or 1.3%, have been confirmed as exploited in the wild, and VulnCheck observed four of them being used against our canaries. That closely aligns with the exploitation rate we've observed across all vulnerabilities in the first half of 2026 but is lower than what we've seen historically. While AI-assisted vulnerability discovery clearly has value for both attackers and defenders, the data does not suggest that AI discovered vulnerabilities are inherently more likely to be exploited than those found through traditional methods. Instead, AI appears to increase the volume of vulnerabilities that can be discovered, giving defenders an opportunity to identify and remediate them before attackers do. Time will tell whether the rate of exploitation increases as frontier cyber models become more widely available.

With the relatively small volume of AI discovered vulnerabilities with confirmed exploitation, our main observation is that it’s early to come to any significant conclusions on what vendors / products are most likely to be exploited, however, it’s worth noting that the KEVs include both commercial (Microsoft Windows, BeyondTrust) and open source products (ghost, chef, linux, etc.). It will be interesting to watch as additional exploitation evidence surfaces.

As mentioned earlier, Anthropic generated a lot of hype around the dangers of AI-assisted vulnerability discovery, so we also looked at that claim in isolation. If you recall, [Anthropic launched a disclosure ledger](https://red.anthropic.com/2026/cvd/ledger/) in May, claiming Claude had identified 23,019 findings. What's surprising is that the disclosure ledger itself has never grown beyond the original 1,611 committed entries at launch, and Anthropic has failed to publish any updates or new disclosures despite more than 150 findings having passed their disclosure deadline as outlined in the Anthropic Coordinated Disclosure Policy. Based on the disclosure data I've collected, 126 of those findings have resulted in published CVEs, and just one of them, CVE-2026-26980, has been confirmed as exploited in the wild as of time we wrote this report. At VulnCheck, we’ve observed first-hand exploits being used against this vulnerability on [VulnCheck Canaries](https://www.vulncheck.com/blog/introducing-vulncheck-canary-intelligence).

Expanding our view into exploited vulnerabilities that were first exploited in the first half of 2026, we explored VulnCheck [Target Intelligence](https://www.vulncheck.com/product/target-intelligence) to better understand what vulnerabilities we were able to identify with hosts on the public internet that are still vulnerable. This provides visibility into the types of technologies that we know are both known to be discoverable on the internet and have vulnerabilities that have been exploited in the wild.

During the first half of 2026, of the 495 CVEs that became exploited in the wild, we observed exploitation activity for 61 KEVs in VulnCheck Canaries, which are real vulnerable hosts. Only 12 of these CVEs have been added to CISA KEV.

During this time, we also scaled [CVE issuance](https://www.vulncheck.com/advisories). Our objective is straightforward: to ensure that vulnerabilities are discoverable by defenders and that exploitation evidence is available as early as possible to mitigate the risk of exploitation. 34 of the 495 KEVs identified as exploited were published by the VulnCheck CNA. That’s a primary reason we’ve invested in contributing back to the CVE program as a CVE Numbering Authority, providing our free [vulnerability reporting service](https://www.vulncheck.com/blog/report-a-vulnerability), and offering [VulnCheck KEV](https://www.vulncheck.com/kev) as a free community service while partnering with third-party organizations and security researchers to ensure timely CVE issuance and access to evidence of exploitation.

During the first half of 2026, 79 unique sources were the first to report exploitation. The top six sources first to report include Patchstack (70 KEVs), CrowdSec (64 KEVs), ShadowServer (57 KEVs), VulnCheck (37 KEVs), Wordfence (20 KEVs), and CISA (19 KEVs).

In summary, the exploitation evidence we observed and collected in VulnCheck KEV signals that exploitation activity is sustaining from a volume and velocity perspective, and threat actors continue to target public facing technologies such as CMS and Network Edge Devices. At the same time, it appears that AI products and AI-assisted vulnerability discovery are contributing to a broader attack surface, and it will be interesting to observe the implications over time. For now, giving defenders access to more advanced frontier models is more likely to give defenders an advantage in strengthening software than to give attackers an advantage in discovering vulnerabilities before the software producers do. The data so far, including Anthropic's own stalled disclosure ledger, suggests that AI-assisted vulnerability discovery and frontier capabilities have been overhyped relative to the evidence available today. That doesn't mean the risk is imaginary. It means the impact has been real but modest, and it's worth watching closely as the technology matures rather than reacting to the hype alone.

VulnCheck is helping organizations not just to solve the vulnerability prioritization challenge - we’re working to help equip any product manager, CSIRT/PSIRT or SecOps team and Threat Hunting team to get faster and more accurate with infinite efficiency using VulnCheck solutions.

We knew that we needed better data, faster across the board, in our industry. So that’s what we deliver to the market. We’re going to continue to deliver key insights on vulnerability management, exploitation and major trends we can extrapolate from our dataset to continuously support practitioners.

Are you interested in learning more? If so, VulnCheck's [Exploit & Vulnerability Intelligence](https://vulncheck.com/product/exploit-intelligence) has broad threat actor coverage. Register and demo our data today.

Links/Buttons:
- [Learn More](https://wwv.vulncheck.com/1h-2026-state-of-exploitation-report?utm_source=vulncheck&utm_medium=website-banner&utm_content=b-2026-veir-report)
- [](https://www.youtube.com/@vulncheck)
- [Products](https://www.vulncheck.com/product)
- [Government](https://www.vulncheck.com/government)
- [Resources](https://www.vulncheck.com/resources)
- [Community](https://www.vulncheck.com/community)
- [Company](https://www.vulncheck.com/company)
- [Partners](https://www.vulncheck.com/partners)
- [Sign In / Join Sign In](https://console.vulncheck.com/)
- [Go back](https://www.vulncheck.com/blog)
- [vuln-intel](https://www.vulncheck.com/blog?tags=vuln-intel)
- [kev](https://www.vulncheck.com/blog?tags=kev)
- [significant change in vulnerability discovery and disclosure](https://www.vulncheck.com/blog/ai-assisted-vulnerability-discovery)
- [VulnCheck KEV](https://www.vulncheck.com/kev)
- [28.93% of KEVs](https://www.vulncheck.com/blog/state-of-exploitation-2026)
- [CISA issued updated guidance in BOD 26-04](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk)
- [Is the rate of vulnerability exploitation increasing at the rate of disclosure?](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026#is-the-rate-of-vulnerability-exploitation-increasing-at-the-rate-of-disclosure)
- [Is Exploitation Evidence Keeping Pace with New CVEs?](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026#is-exploitation-evidence-keeping-pace-with-new-cves)
- [What Technologies are being Targeted?](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026#what-technologies-are-being-targeted)
- [Australian Signals Directorate on a large scale exploitation campaign targeting website content management systems](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/large-scale-exploitation-campaign-targeting-website-content-management-systems-cms)
- [2026 State of Exploitation: Exploiting The Network Edge](https://www.vulncheck.com/blog/network-edge-device-report-2026)
- [BOD 26-02, Mitigating Risk From End-of-Support Edge Devices](https://www.cisa.gov/news-events/directives/bod-26-02-mitigating-risk-end-support-edge-devices)
- [How Quickly Are the Top 10 Technology Categories Being Exploited?](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026#how-quickly-are-the-top-10-technology-categories-being-exploited)
- [What AI Technologies have been Exploited?](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026#what-ai-technologies-have-been-exploited)
- [tracking disclosures attributed to Anthropic](https://github.com/patrickmgarrity/Anthropic-Credited-CVEs)
- [Berkeley Vulnerability Research Initiative](https://vuln.cs.berkeley.edu/)
- [What Products Were Exploited Using AI Discovered Vulnerabilities?](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026#what-products-were-exploited-using-ai-discovered-vulnerabilities)
- [Has Anthropic Glasswing Lived Up to the Hype it brought this year?](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026#has-anthropic-glasswing-lived-up-to-the-hype-it-brought-this-year)
- [Anthropic launched a disclosure ledger](https://red.anthropic.com/2026/cvd/ledger/)
- [VulnCheck Canaries](https://www.vulncheck.com/blog/introducing-vulncheck-canary-intelligence)
- [What KEVs in the 1h-2026 Are Exposed on the Internet?](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026#what-kevs-in-the-1h-2026-are-exposed-on-the-internet)
- [Target Intelligence](https://www.vulncheck.com/product/target-intelligence)
- [CVE issuance](https://www.vulncheck.com/advisories)
- [vulnerability reporting service](https://www.vulncheck.com/blog/report-a-vulnerability)
- [What to Expect in an AI-Assisted Vulnerability Era](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026#what-to-expect-in-an-ai-assisted-vulnerability-era)
- [About VulnCheck](https://www.vulncheck.com/company/about)
- [Exploit & Vulnerability Intelligence](https://www.vulncheck.com/product/exploit-intelligence)
- [Schedule a Demo](https://wwv.vulncheck.com/demo-request)
- [Initial Access Intelligence](https://www.vulncheck.com/product/initial-access-intelligence)
- [Canary Intelligence](https://www.vulncheck.com/product/canary-intelligence)
- [Documentation](https://docs.vulncheck.com/)
- [API](https://docs.vulncheck.com/api)
- [Open Source & Tools](https://www.vulncheck.com/open-source)
- [Changelog](https://docs.vulncheck.com/changelog)
- [Glossary](https://docs.vulncheck.com/kb)
- [Contact Support](mailto:support@vulncheck.com)
- [NVD++](https://www.vulncheck.com/nvd2)
- [VulnCheck Exploit Database (XDB)](https://www.vulncheck.com/xdb)
- [Knowledge Base](https://www.vulncheck.com/blog?tags=101)
- [Report a Vulnerability](https://www.vulncheck.com/advisories/report)
- [News and Awards](https://www.vulncheck.com/news)
- [Press Releases](https://www.vulncheck.com/press)
- [Events](https://www.vulncheck.com/events)
- [THREATCON1 Podcast](https://www.vulncheck.com/podcast)
- [Careers](https://www.vulncheck.com/careers)
- [Become a Partner](https://wwv.vulncheck.com/partner-request)
- [Register a Deal](https://wwv.vulncheck.com/partner-deal-registration)
- [Privacy Policy](https://www.vulncheck.com/privacy)
- [Terms & Conditions](https://www.vulncheck.com/terms)
- [Vulnerability Disclosure Policy](https://www.vulncheck.com/vulnerability-disclosure-policy)
- [Service Terms](https://www.vulncheck.com/service-terms)
