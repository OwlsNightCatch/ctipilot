# extract: served via jina
Title: Anthropic Users Hit by Infostealer Attacks, Session Thefts

URL Source: https://www.darkreading.com/cyberattacks-data-breaches/anthropic-users-infostealer-attacks-session-thefts

Published Time: 2026-08-31T21:08:46.000Z

Markdown Content:
3 Min Read

Source: Thaspol Sangsee via Shutterstock

Anthropic proactively signed an unknown number of users out of [Claude](https://www.darkreading.com/vulnerabilities-threats/claudy-day-trio-flaws-claude-users-data-theft) after a threat actor stole their login sessions, accessed their accounts, and consumed their allotted usage.

The attacks came to light via email alerts sent to affected users that were then posted to [social media](https://www.reddit.com/r/ClaudeAI/comments/1w1jqsh/thank_you_anthropic_really/). The theft of login sessions and unauthorized access to Claude accounts resulted from [infostealer malware](https://www.cybersecuritydive.com/news/microsoft-europol-international-takedown-infostealer-malware/823655/) on users' systems, rather than from any malware related to or installed through Claude, Anthropic said in the email notifications.

## Claude Accounts Under Attack

The AI company said it had signed affected users out of Claude and removed their saved payment methods after detecting suspicious activity on their accounts. Anthropic's ongoing investigation has found that the threat actor stole Claude login sessions using general-purpose infostealers that had previously been installed on users' systems, likely through a malicious app or unofficial download.

Related:[Hundreds of OpenAI Agents Invaded Hugging Face Servers](https://www.darkreading.com/cyberattacks-data-breaches/hundreds-openai-agents-invaded-hugging-face-servers)

“The malware identified in this campaign so far include [Vidar](https://www.darkreading.com/endpoint-security/vidar-infostealer-back-with-vengeance), Lumma (LummaC2), StealC, RedLine and Acreed on Windows, and Atomic Stealer (AMOS) on a small number of Macs,” Anthropic said in its email to affected users. It's likely that affected users have had the infostealers on their system for some time, the company noted.

The Anthropic incident is another example of attackers [shifting from stealing passwords](https://www.darkreading.com/identity-access-management-security/more-attackers-logging-in-not-breaking-in) to targeting session cookies and authentication tokens. With many organizations implementing stronger password security protocols and multifactor authentication (MFA), traditional credential theft has become harder, so attackers have increasingly begun targeting session artifacts to [hijack already-authenticated sessions](https://www.techtarget.com/cybersecurity/tip/5-common-browser-attacks-and-how-to-prevent-them) and bypass MFA altogether.

Experts have described the shift as complicating incident response because [resetting a password](https://www.darkreading.com/endpoint-security/why-resetting-passwords-no-longer-stop-attacks) alone may not cut off an attacker who already has a valid session or refresh token. In Anthropic's case, for instance, infostealers harvested Claude sessions, likely along with other sensitive information such as login cookies, saved passwords and credentials for other apps. The stolen Claude sessions allowed the attackers to access the associated accounts without having to defeat the authentication controls protecting them.

As one user, who posted Anthropic's email communication on Reddit noted, "The hacker stole all my Google Chrome credentials, including cookies and session IDs, which allowed him to bypass all two-factor authentication security measures."

Anthropic did not respond to a Dark Reading request for comment on the reported account attacks.

Related:[Russian Hackers Phish EU Officials Over Messaging Apps](https://www.darkreading.com/cyberattacks-data-breaches/russian-hackers-phish-eu-officials-messaging-apps)

## Invalidated Claude Sessions

Anthropic said signing affected users out of their Claude accounts invalidates the sessions that attackers had used to access them. Users would therefore need to log in again on their devices to regain access to Claude. The company also removed all saved payment information associated with compromised accounts, preventing threat actors from using those payment methods to incur additional charges for [Claude usage](https://aibusiness.com/generative-ai/new-dashboard-tool-lets-you-monitor-claude-usage).

In cases where threat actors had already used an affected user's payment card to pay for Claude usage, Anthropic said it had refunded the unauthorized charges. It's unclear what the threat actor used the compromised Claude accounts for.

Anthropic's email cautioned users that its decision to sign affected users out of their Claude accounts only invalidated the stolen sessions. Affected users would still need to remove the infostealer from their systems to prevent the attacker from stealing and misusing their session information once again.

"After the malware has been completely removed, secure the email account you use for Claude by setting a new password, signing out of other devices and enabling two-factor authentication," the notification said.

Related:[Dark Caracal Adds New Malware to Cyber Espionage Arsenal](https://www.darkreading.com/cyberattacks-data-breaches/dark-caracal-adds-new-malware-cyber-espionage-arsenal)

Anthropic's email also advised affected users to consider updating other saved passwords in their browsers like those associated with their work, bank accounts and other apps. It is only after users have completed these steps that they should add a payment method back to their Claude accounts.

## About the Author

[](https://www.darkreading.com/author/jai-vijayan)

Contributing Writer

Illinois-based Jai Vijayan is a veteran, award-winning technology journalist with more than 25 years of experience covering cybersecurity. His information security reporting has explored everything from ransomware, nation-state threats, and identity security to AI risk, critical infrastructure protection, software supply chain security, cloud security and emerging enterprise technologies.

Over the course of his career, Jai has written news stories, feature articles, survey reports, white papers, and e-books for enterprise and technology audiences. He has also moderated panel discussions and executive roundtables featuring CISOs, security researchers, and industry leaders.

Jai previously served as senior editor at Computerworld, where he covered information security and data-privacy issues. His work has also appeared in CSO Online, InformationWeek, The Christian Science Monitor Passcode, The Economic Times, and other publications.

His work has earned multiple industry honors, including a Joint ASBPE Excellence Award for Best Coverage of Government IT, and a Joint Jesse H. Neal Award for wireless LAN security coverage. Jai holds a Master’s degree in statistics from Bangalore University, and studied broadcasting and electronic communication at Marquette University in Milwaukee.

Links/Buttons:
- [Informa TechTarget|](https://www.informatechtarget.com/)
- [SearchSecurity](https://www.techtarget.com/searchsecurity/)
- [Cybersecurity Dive](https://www.cybersecuritydive.com/)
- [InformationWeek](https://www.informationweek.com/)
- [Channel Dive](https://www.channeldive.com/)
- [Explore our brands](https://www.informatechtarget.com/our-brands/)
- [Dark Reading Resource Library](https://www.darkreading.com/resources)
- [Black Hat News](https://www.darkreading.com/program/black-hat)
- [Omdia Cybersecurity](https://www.darkreading.com/program/omdia-cybersecurity)
- [Advertise](https://www.darkreading.com/advertise)
- [](https://www.informa.com/)
- [Newsletter Sign-Up](https://dr-resources.darkreading.com/c/pubRD.mpl?secure=1&sr=pp&_t=pp:&qf=w_defa3135&ch=drwebbutton)
- [Application Security](https://www.darkreading.com/application-security)
- [Cybersecurity Careers](https://www.darkreading.com/cybersecurity-operations/cybersecurity-careers)
- [Cloud Security](https://www.darkreading.com/cloud-security)
- [Cyber Risk](https://www.darkreading.com/cyber-risk)
- [Cyberattacks & Data Breaches](https://www.darkreading.com/cyberattacks-data-breaches)
- [Cybersecurity Analytics](https://www.darkreading.com/cybersecurity-analytics)
- [Cybersecurity Operations](https://www.darkreading.com/cybersecurity-operations)
- [Data Privacy](https://www.darkreading.com/cyber-risk/data-privacy)
- [Endpoint Security](https://www.darkreading.com/endpoint-security)
- [ICS/OT Security](https://www.darkreading.com/ics-ot-security)
- [Identity & Access Mgmt Security](https://www.darkreading.com/cybersecurity-operations/identity-access-management-security)
- [Insider Threats](https://www.darkreading.com/vulnerabilities-threats/insider-threats)
- [IoT](https://www.darkreading.com/ics-ot-security/iot)
- [Mobile Security](https://www.darkreading.com/endpoint-security/mobile-security)
- [Perimeter](https://www.darkreading.com/cybersecurity-operations/perimeter)
- [Physical Security](https://www.darkreading.com/cybersecurity-operations/physical-security)
- [Remote Workforce](https://www.darkreading.com/endpoint-security/remote-workforce)
- [Threat Intelligence](https://www.darkreading.com/threat-intelligence)
- [Vulnerabilities & Threats](https://www.darkreading.com/vulnerabilities-threats)
- [Jai Vijayan](https://www.darkreading.com/author/jai-vijayan)
- [Jacob Krell](https://www.darkreading.com/author/jacob-krell)
- [DR Global](https://www.darkreading.com/program/dr-global)
- [Asia Pacific](https://www.darkreading.com/keyword/asia-pacific)
- [Europe](https://www.darkreading.com/keyword/europe)
- [Latin America](https://www.darkreading.com/keyword/latin-america)
- [Middle East & Africa](https://www.darkreading.com/keyword/middle-east-africa)
- [Nate Nelson](https://www.darkreading.com/author/nate-nelson)
- [The Edge](https://www.darkreading.com/program/the-edge)
- [DR Technology](https://www.darkreading.com/program/dr-technology)
- [Upcoming Events](https://www.darkreading.com/events)
- [Podcasts](https://www.darkreading.com/podcasts)
- [Webinars](https://www.darkreading.com/resources?types=Webinar)
- [White Papers](https://www.darkreading.com/resources?types=Whitepaper)
- [Reports](https://www.darkreading.com/resources?page=1&types=digital+editorial+content&types=report)
- [Newsletters](https://www.darkreading.com/resources?q=newsletter)
- [Heard It From a CISO](https://www.darkreading.com/keyword/heard-it-from-a-ciso)
- [Reporters' Notebook](https://www.darkreading.com/series/reporters-notebook)
- [Dark Reading's 20th](https://www.darkreading.com/program/darkreading-20th-anniversary)
- [Videos](https://www.darkreading.com/videos)
- [Dark Reading Polls](https://www.darkreading.com/dark-reading-polls)
- [Partner Perspectives](https://www.darkreading.com/partner-perspectives)
- [Meet the Editors](https://www.darkreading.com/author)
- [About Us](https://www.darkreading.com/about-us)
- [News](https://www.darkreading.com/latest-news)
- [Claude](https://www.darkreading.com/vulnerabilities-threats/claudy-day-trio-flaws-claude-users-data-theft)
- [social media](https://www.reddit.com/r/ClaudeAI/comments/1w1jqsh/thank_you_anthropic_really/)
- [infostealer malware](https://www.cybersecuritydive.com/news/microsoft-europol-international-takedown-infostealer-malware/823655/)
- [Hundreds of OpenAI Agents Invaded Hugging Face Servers](https://www.darkreading.com/cyberattacks-data-breaches/hundreds-openai-agents-invaded-hugging-face-servers)
- [Vidar](https://www.darkreading.com/endpoint-security/vidar-infostealer-back-with-vengeance)
- [shifting from stealing passwords](https://www.darkreading.com/identity-access-management-security/more-attackers-logging-in-not-breaking-in)
- [hijack already-authenticated sessions](https://www.techtarget.com/cybersecurity/tip/5-common-browser-attacks-and-how-to-prevent-them)
- [resetting a password](https://www.darkreading.com/endpoint-security/why-resetting-passwords-no-longer-stop-attacks)
- [Claude usage](https://aibusiness.com/generative-ai/new-dashboard-tool-lets-you-monitor-claude-usage)
- [Dark Caracal Adds New Malware to Cyber Espionage Arsenal](https://www.darkreading.com/cyberattacks-data-breaches/dark-caracal-adds-new-malware-cyber-espionage-arsenal)
- [The State of Cloud Security: The Latest Challenges](https://dr-resources.darkreading.com/c/pubRD.mpl?qf=w_sysf19&ch=mod)
- [How Organizations Are Managing Incident Response](https://dr-resources.darkreading.com/c/pubRD.mpl?qf=w_forq296&ch=mod)
- [How Enterprises Are Developing Secure Applications](https://dr-resources.darkreading.com/c/pubRD.mpl?qf=w_defa10666&ch=mod)
- [Inside RSAC 2026: security leaders reveal the risks redefining your defense strategy](https://dr-resources.darkreading.com/c/pubRD.mpl?qf=w_darl22&ch=mod)
- [Essential News & Insights from Black Hat USA 2025](https://dr-resources.darkreading.com/c/pubRD.mpl?qf=w_darl25&ch=mod)
- [Access More Research](https://www.darkreading.com/resources?page=1&types=Report&types=Research+Report)
- [How to Leverage Threat Intelligence Without Drowning: The Zero Noise Approach](https://dr-resources.darkreading.com/c/pubRD.mpl?qf=w_wiza78&ch=mod)
- [Cloud Incident Response: Forensics in Distributed Environments](https://dr-resources.darkreading.com/c/pubRD.mpl?qf=w_defa11588&ch=mod)
- [Beyond the Login: Key Considerations for Evaluating Identity Security](https://dr-resources.darkreading.com/c/pubRD.mpl?qf=w_saia164&ch=mod)
- [SASE Pivot and Trends 2026: A Gartner Keynote](https://dr-resources.darkreading.com/c/pubRD.mpl?qf=w_forq299&ch=mod)
- [What Every Enterprise Should Know About Securing Cloud Assets In the Age of AI](https://dr-resources.darkreading.com/c/pubRD.mpl?qf=w_defa11519&ch=mod)
- [Cyberattacks & Data BreachesRussian Hackers Weaponize Microsoft Office Bug in Just 3 Daysby Jai VijayanFeb 03, 2026](https://www.darkreading.com/cyberattacks-data-breaches/russian-hackers-weaponize-office-bug-within-days?recipe=similar-items&source_content_id=ca01091a9a7153d382dc2017f8e8aec9)
- [Cyberattacks & Data BreachesCISA Warns of 'Ongoing' Brickstorm Backdoor Attacksby Rob WrightDec 04, 2025](https://www.darkreading.com/cyberattacks-data-breaches/cisa-ongoing-brickstorm-backdoor-attacks?recipe=similar-items&source_content_id=058ef0cfb57652bddd698609c655b901)
- [Cyberattacks & Data BreachesDeja Vu: Salesforce Customers Hacked Again, Via Gainsightby Nate NelsonNov 21, 2025](https://www.darkreading.com/cyberattacks-data-breaches/salesforce-customers-hacked-gainsight?recipe=similar-items&source_content_id=4056475ddaadba32176031a32b0b2af4)
- [Cyberattacks & Data BreachesJaguar Land Rover Shows Cyberattacks Mean (Bad) Businessby Robert LemosOct 03, 2025](https://www.darkreading.com/cyberattacks-data-breaches/jaguar-land-rover-cyberattacks-bad-business?recipe=similar-items&source_content_id=0288d8954cca9560e3e90b9cd9e68918)
- [Black Hat USA 2026 Conference Guide](https://www.techtarget.com/cybersecurity/conference/Black-Hat-2026-Key-news-takeaways-and-security-trends)
- [Rob Wright,](https://www.darkreading.com/author/robert-wright)
- [Alexander Culafi](https://www.darkreading.com/author/alexander-culafi)
- [Kristina Beek](https://www.darkreading.com/author/kristinabeek)
- [Reprints](https://info.wrightsmedia.com/informa-licensing-reprints-request)
- [Home|](https://www.informatech.com/)
- [Cookie Policy|](https://www.informatechtarget.com/privacy-policy/#cookies)
- [Privacy|](https://www.informatechtarget.com/privacy-policy)
- [Terms of Use](https://www.informatechtarget.com/terms-and-conditions/)
