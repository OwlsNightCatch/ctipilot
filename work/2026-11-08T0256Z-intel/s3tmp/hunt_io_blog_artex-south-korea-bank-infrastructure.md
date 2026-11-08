---
title: "ARTEX Exposed: Infrastructure Behind the South Korea Bank Hack"
url: https://hunt.io/blog/artex-south-korea-bank-infrastructure
hostname: hunt.io
description: Hunt.io pivots from an exposed open directory into the ARTEX campaign against South Korean banks, revealing a Hong Kong jump server, AI model routing, and exploit tooling.
sitename: Hunt Intelligence
date: "2026-11-03"
fingerprint: "9590f39ba5818311"
---
# ARTEX Exposed: Mapping the Infrastructure Behind the South Korean Bank Breaches

Published on

**Disclosure note: Hunt.io notified the relevant national CERT prior to publication. No personal records or credentials from the affected systems appear in this report.**

[Open directories](https://hunt.io/glossary/open-directories) are among the most valuable sources of insight into active threat actor operations. When an attacker misconfigures a staging server, the exposure can reveal far more than the final payload. In early October 2026, [CrowdStrike reported](https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/) that an unknown, financially motivated threat actor had used [ARTEX](https://labs.cloudsecurityalliance.org/research/csa-research-note-artex-agentic-pentest-tool-korean-banks-20/), an AI-driven autonomous penetration testing framework, in intrusions targeting South Korean financial organizations. [The Hacker News](https://thehackernews.com/2026/10/artex-ai-pentesting-tool-used-in-data.html) and [Security Affairs](https://securityaffairs.com/200661/hacking/ai-driven-tool-artex-used-in-attacks-against-south-korean-banks.html) subsequently covered the campaign, bringing wider attention to the use of AI-driven offensive tooling in real-world intrusions.

The public reporting identified a key server at 38.244.50\[.\]120, nine additional IP addresses described as proxies, and the LLM reseller domain xcai\[.\]pro.

**But the public indicators were only part of the story.**

Our investigation examines **another** infrastructure at 23.248.226\[.\]250 associated with the reported campaign.  The findings reveal a broader operational environment that includes AI model-routing components, proxy infrastructure, exploitation tooling, credential-handling scripts, and mobile-device utilities.

This research walks through the evidence, the infrastructure pivots, and the artifacts recovered from the exposed directories to show what can be learned when an investigation goes beyond the initial indicators of compromise.

## Key Takeaways

- Our investigation revealed a new open directory at 23.248.226\[.\]250 which acts as a Hong Kong-based jump server.
- The analysis found Claude Code configurations, custom model-routing shims, and 19 agent skills that supported reconnaissance, web testing, payment logic analysis, and mobile operations.
- The recovered configuration and routing scripts reference **DeepSeek**, **GLM**, and **Grok-related** components, providing evidence of a multi-model setup consistent with the reported use of alternative AI services.
- FOFA-related tooling and a proxy service at **154.201.79\[.\]246:443** provided additional infrastructure pivots, with 79 unique exit IPs observed in an initial sample of 100 identities.
- Cryptocurrency, Linux exploitation, and mobile-device artifacts were also recovered, but their direct relationship to the reported South Korean breaches remains unconfirmed.
- The recovered tooling includes reconnaissance scripts, proxy enumeration utilities, reverse SSH tunnel management, a staged JNDI/LDAP exploitation setup, Linux privilege-escalation exploits, and mobile-device tooling.
- Hunt.io pivoting expanded the set of candidates for ARTEX infrastructure through **certificate metadata**, **ARTEX malware classification**, and **HTTP title matching**, providing complementary hunting methods.

## Background and Campaign Overview

Between late September and early October 2026, [seven South Korean financial institutions](https://threatbook.io/blog/artex-attacks-south-korean-financial-institutions) experienced data breaches involving internet-facing peripheral systems. Approximately 66,000 to 67,000 individuals and around 2,200 corporations [were affected](https://asianews.network/south-korean-police-launch-major-probe-as-suspected-ai-hacks-sweep-through-banks/), with personal, employment, income, and loan-related information exposed.

[CrowdStrike](https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/) published its findings on October 7, 2026, followed by the [Genians Security Center (GSC)](https://www.genians.co.kr/blog/threat_intelligence/banking-cyber-attack) on October 12. Both reports attributed the activity to **ARTEX**, an open-source autonomous penetration testing framework developed in China and licensed under the GNU Affero General Public License version 3.0 (AGPL-3.0).

CrowdStrike assessed with moderate confidence that the operator was a single **Chinese-speaking individual** motivated by financial gain rather than an established threat group. The assessment identified **DeepSeek v4.1** Flash as the primary model, with **GLM 5.3** from **Zhipu AI** and **Grok 4.6** serving as backup models.

The infrastructure reportedly accessed these services in part through the reseller domain [xcai\[.\]pro](https://portal.hunt.io/domain/xcai.pro). Both reports described a two-server configuration, consisting of a Hong Kong-based IP address used as primary infrastructure and [38.244.50\[.\]120](https://portal.hunt.io/ip/38.244.50.120), which hosted the ARTEX console.

GSC also reported that the original **ARTEX GitHub repository and Docker image were removed** on October 11, although forks and mirrors remained available.

## Infrastructure Discovery and Initial Pivoting

Our intelligence for [38.244.50\[.\]120](https://portal.hunt.io/ip/38.244.50.120) provides a more detailed view of the infrastructure associated with the **ARTEX campaign**. The address falls within the [38.244.48.0/21](https://portal.hunt.io/ip-block/38.244.48.0/21) network and is attributed to [AS174](https://portal.hunt.io/asn/AS174), operated by Cogent Communications, LLC. Hunt.io identifies its location as Los Angeles, California, United States. The record shows seven warnings, 73 associations, 17 pivots, and 13 code search results.

Our solution lists 15 open ports, including SSH on ports 22 and 8443, HTTPS on port 443, and several HTTP services on nonstandard ports. The ARTEX login interface appears on ports 443 and 8090, with the page title displaying "**ARTEX - 自主渗透测试控制台**". Port 5918 hosts a web interface titled "**Gemini2API - 管理控制台**", served by Uvicorn, while ports 9003, 18080, and 18098 expose HTTP services identified as Python BaseHTTP servers. A **Tinyproxy service** is also identified on port 18888.

Our [AttackCapture™](https://hunt.io/features/attackcapture) platform reports 23 files totaling 6.69 MB, with no subdirectories. The captured data is associated with the host [38.244.50\[.\]120:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://38.244.50.120:8000), geolocated to Los Angeles, California, United States, and includes a recorded timestamp of **August 22, 2026**.

We have expanded the infrastructure by searching "**38.244.50\[.\]120**" in AttackCapture and found another open directory at [23.248.226\[.\]250](https://portal.hunt.io/ip/23.248.226.250) acting as a **jump server**. The code search returned 13 matching results, including configuration files containing hardcoded credential references, scripts suggesting remote file synchronization, and commands designed to download and execute remote scripts.

The second IP address, [23.248.226\[.\]250](https://portal.hunt.io/ip/23.248.226.250), is associated with [AS138415](https://portal.hunt.io/asn/AS138415) (Yancy Limited) and the network range 23.248.224.0/20. The IP is geolocated to Tung Chung, Islands, Hong Kong, and is associated with [RedLuff, LLC (redluff.com)](https://portal.hunt.io/host-radar/redluff.com). AttackCapture reports revealed **three** AttackCapture warnings for potentially malicious open directories, recorded on September 5, September 26, and October 5, 2026.

The AttackCapture associated with the second IP, [23.248.226\[.\]250](https://portal.hunt.io/attackcapture/filemanager?host=http://23.248.226.250:18099), exposes a directory containing 42 files across 2 subdirectories, with a total reported size of 105 MB. The directory was last recorded on September 26, 2026, at 14:47 and is accessible via HTTP on port 18099.

## Evidence Linking the Exposed Infrastructure to ARTEX

The most direct link between **23.248.226\[.\]250** and the published ARTEX IOC is the jump-host configuration recovered from the exposed directory at **23.248.226\[.\]250:18099**.

The directory contains a file named **.secrets** and a corresponding backup named **.secrets.bak-20260911**. These files reportedly use **Unix permission mode 600**, which restricts access to the file owner under standard Unix permission semantics. It also contains the same Chinese-language operational comment, which translates to: "**Sole source of credentials; permission 600; never paste plaintext into a session; read only the specific line when needed.**"

The additional credential fields identify other configured services, including a **Zhipu AI API key**, an **OpenAI-compatible relay key**, and **Webshare credentials**.

```
# sole source of credentials, chmod 600, never paste plaintext in a session
JUMPHOST=38.244.50.120
JUMPHOST_USER=root
JUMPHOST_PASS=[REDACTED]
ZAI_KEY=[REDACTED, Zhipu AI / GLM API key]
RELAY_KEY=sk-[REDACTED, OpenAI compatible relay key]
WEBSHARE_USER=[REDACTED]
WEBSHARE_PASS=[REDACTED]
```
                Copy
The credential-file evidence is corroborated by three shell scripts (**local-boot.sh**, **tunnel-watchdog.sh**, and **sync-memory.sh**) recovered from the same host. All three reference 38.244.50\[.\]120 and use sshpass to supply a password for SSH-based operations targeting the remote root account.

The scripts reveal three complementary functions.

- **local-boot.sh** restores a reverse SSH tunnel after startup, forwarding the local service on port 8100 to the jump host, and launches a local sing-box relay configured to listen on port 11050.
- **tunnel-watchdog.sh** checks for an existing reverse tunnel associated with port 22222 and starts it if the expected process is absent. The accompanying comment identifies the remote forwarding target as local port 48989, associated with a read-only Dufs service.
- **sync-memory.sh** copies Markdown files from a local memory directory to five destination paths on the jump host and then attempts ownership adjustments for directories associated with the grok and gemini accounts.

A **ZAI\_KEY** entry in the available file provides access to Zhipu AI's GLM models, while a tunnel defined in **local-boot.sh** is explicitly named grok2api. This architecture offers a plausible explanation for CrowdStrike's observation that multiple LLM backends were active within the same campaign.

## AI Model Routing and Runtime Configuration

A state file named **.claude.json** confirms that the harness is Claude Code itself, running base version 2.1.221, with 510 recorded startups since August 4, 2026. However, the installation is not communicating directly with Anthropic's API.

A small local proxy, **ds-models-shim.py**, addresses a compatibility issue: the official **/v1/models** endpoint returns a 404 response when queried against a non-Anthropic backend, preventing Claude Code from discovering the available models. The shim intercepts that specific request and returns a locally defined model list containing **deepseek-v4-pro** and **deepseek-flash**. All other requests are forwarded to api.deepseek.com/anthropic.

A second proxy, **xcai-effort-shim.py**, provides further insight into the setup. Its docstring describes the request-routing chain in the operator's own words, translated from Chinese: "The Gemini user path is Claude Code to CCR on port 3456, then to xcai at direct\[.\]xcai\[.\]pro, and finally to DeepSeek."

**CCR**, or **Claude Code Router**, is an open-source project that enables Claude Code to communicate with alternative model backends. The xcai\[.\]pro domain is also significant: CrowdStrike has reportedly identified it as an indicator associated with this campaign. The shim's specific function is to inject a **reasoning\_effort** field into every outgoing request. According to the operator's documentation, this parameter is necessary because the **DeepSeek** backend accessed through xcai otherwise skips its reasoning stage.

## Custom Agent Skills and Operational Workflows

The same **.claude.json** file records usage counts for 19 custom Claude Code skills, which are reusable instruction sets written by the operator for the agent. These skills provide a clear picture of the operation and the tasks the agent was designed to carry out.

They provide an overview of the operation's main activities, from reconnaissance and application analysis to mobile device automation and payment testing.

| Skill | Function | 
|---|---|
| code-audit | Reviewing source code and application configurations | 
| recon | Enumerating targets and discovering assets | 
| web-inject | Injecting payloads into web application workflows | 
| hae | Enumerating web assets and identifying the attack surface | 
| cloud-phone | Managing rented Android cloud phone instances | 
| xingjie-cloudphone | Controlling Xingjie (星界) cloud phone services | 
| hemax-adb | Automating interactions with cloud phone instances through ADB | 
| js-api-mining | Extracting internal JavaScript API calls from target websites | 
| waf-bypass | Testing methods to bypass web application firewalls | 
| web-auth | Examining authentication flows and potential bypasses | 
| tg-miniapp | Testing Telegram Mini Apps | 
| apk-download | Downloading target Android APK files | 
| oversea-cloudphone | Provisioning overseas cloud phone instances | 
| b2-archive | Archiving evidence in Backblaze B2 | 
| decompile | Decompiling APK files and other binaries | 
| apk-internal-hunting | Searching decompiled APKs for internal endpoints and exposed secrets | 
| attack-variants | Generating variations of exploit payloads | 
| file-ssrf | Testing for server-side request forgery through file handling features | 
| payment-logic | Testing payment and cash-in business logic | 

The payment-logic skill is particularly notable because a file named .secrets-cashin-test-accounts was found alongside it. The file contains three self-registered accounts with JWTs for a cash-in deposit API. A source comment describes the accounts as part of an authorized, self-built test dated September 12, 2026. Each account has its own user ID and bank account ID.

This setup is consistent with an approach to testing for insecure direct object reference (IDOR) vulnerabilities.

Genians and CrowdStrike have described similar techniques in connection with attacks against Korean loan and inquiry services.

## Reconnaissance Tooling and Staged RCE Exploitation

The same directory contains the tools used to support reconnaissance, manage proxy infrastructure, and stage a remote code execution (RCE) chain.

### FOFA Access Through a Third-Party API

**fofa2.py** is a Python client for FOFA, a Chinese cyberspace asset search engine commonly compared with Shodan and Censys. The script sends requests to the third-party service fofoapi.com. It constructs an HMAC-SHA256 signature, generates a timestamp and nonce, and submits search parameters through the service's **/api/v1/search/all** endpoint.

A comment in the source code states that the primary membership had expired and that a backup key was being used. This suggests that the operator had previously relied on a paid FOFA membership and had switched to an alternative access method.

```
def nonce():
    return hashlib.sha256(
        (UA + "1920x1080x24" + "zh-CN" + SALT).encode()
    ).hexdigest()[:32]
url = "https://fofoapi.com/api/v1/search/all?" +
      urllib.parse.urlencode(params)
### Tracking Proxy Enumeration and Exit-IP Tracking
```
                Copy
The scripts **proxypool.py** and **proxypool\_enum.py** manage and enumerate a rotating proxy service exposed at 154.201.79\[.\]246:443. The service accepts credentials following the **Default.customerNNN** naming pattern, allowing the operator to test multiple customer identities against the same endpoint.

It uses concurrent requests to identify exit IP addresses, retries failed probes, and maintains a persistent ledger linking identities to observed IP addresses and project assignments. The scripts also identify shared exit IPs and compare results across sampling rounds.

The initial sample reportedly contained **79 unique exit IP addresses** among the first 100 identities tested. This demonstrates that the service can expose multiple exit IPs through a single proxy endpoint.

The address 154.201.79\[.\]246 is also identified as a proxy-related indicator in reporting by **CrowdStrike**, **ThreatBook**, and **Cybersecurity News**.

### JNDI/LDAP Exploitation Infrastructure

Another open directory at [23.248.226\[.\]250:8001](https://portal.hunt.io/attackcapture/filemanager?host=http://23.248.226.250:8001) holds a small, self-contained JNDI and LDAP exploitation rig built on the UnboundID LDAP SDK. According to the associated logs, the chain was staged and retrieved on **October 5, 2026, at 03:42 UTC**.

The **LDAPRefServer.java** and **LDAP2.java** create an in-memory LDAP directory server that returns specially crafted Java naming references in response to search requests. The server modifies search results to include a **javaNamingReference** object with attributes specifying a Java class name, a codebase URL, and a factory class. In **LDAP2.java**, these attributes point to the Exploit class hosted at the same external address.

The supplied **Exploit.class** provides further evidence of the intended execution chain. Its static initializer invokes system commands, including id, hostname, and uname -a, and also attempts to read /etc/hostname. The resulting output is sanitized before being incorporated into a DNSLog callback hostname under **u6ud2s.dnslog.cn**.

This mechanism is designed to confirm command execution through an out-of-band DNS interaction. The compiled class also contains references to HTTP-based retrieval commands, indicating an alternative mechanism for transmitting data.

The accompanying **mux.py** script provides a single entry point for HTTP and LDAP traffic. It inspects the first bytes of each incoming connection and forwards HTTP-like requests to a local service on port 8000, while routing other connections to the LDAP service on port 1389. This arrangement allows the two services to share one listening port, provided the traffic can be classified by its initial bytes.

## Recovered Tooling and Payloads: Exchange Access and Mobile Device Operations

The files recovered from 38.244.50\[.\]120:8000 and from 23.248.226\[.\]250:8907 contained a diverse collection of scripts, binaries, source files, and configuration artifacts associated with cryptocurrency-exchange access, Linux exploitation, and mobile-device operations.

The following table summarizes the recovered artifacts and their observed or apparent functions.

| Artifact | Observed functionality or contents | 
|---|---|
| x.js | Checks for an authenticated YIIMP administrator session, tests default credentials, and includes functionality associated with initiating withdrawals. | 
| x.sh | Supports reverse-shell access, collects configuration and key files, and scans local ports associated with cryptocurrency-wallet RPC services. | 
| relay.py | Provides a listener on port 4444. | 
| server.py | Provides a service on port \`8000 associated with payload handling and data collection. | 
| tg.py | Implements Telegram-based notifications. | 
| tg.conf | Contains Telegram bot and chat configuration fields, with sensitive values redacted. | 
| shells.log | Stores shell-related log entries. | 
| BlocPalX files | Recovered files associated with the BlocPalX cryptocurrency platform. | 
| les.sh | Linux exploit suggester script. | 
| Poc2588 Exp2588 exp2588\_44 | Exploit or proof-of-concept builds associated with CVE-2022-2588. | 
| cve5054-static cve5054 variants, including v2/v3 musl builds | Multiple binaries associated with CVE-2025-5054, including statically linked or alternative-library builds. | 
| cv3p, cvx cve3493-static | Additional exploit-related binaries whose precise CVE associations or functions remain unconfirmed. | 
| aio\_uaf.c | iOS exploit-related source code referencing a use-after-free technique. | 
| poc65343\_probe.c | iOS proof-of-concept or probing source associated with identifier 65343. | 
| ios26\_probe.c | Probe source associated with iOS 26. | 
| stub.c, stub65343.c | Supporting C source files associated with the mobile proof-of-concept artifacts. | 
| Android KernelPatch tools | Utilities associated with Android kernel patching. | 
| payload-dumper-go.exe | Utility for extracting payload contents from Android firmware packages. | 
| Patched EDL firmware files | Modified firmware artifacts associated with Emergency Download Mode workflows. | 
| recv.py | Receives data on port 8082. | 
| wxapkg-watchdog.sh.\_\_rev2 | Watchdog script associated with a WeChat mini-program package. | 
| cloudphone-oversea.key | Credential or key file associated with overseas cloud-phone operations. | 

The recovered artifacts fall into two broad operational areas. The **first** concerns cryptocurrency-exchange access and web application workflows, including administrator-session checks, withdrawal functionality, shell access, and collection of configuration files. The **second** concerns Linux exploitation and mobile-device research, including kernel exploit builds, iOS proof-of-concept source files, Android firmware utilities, and cloud-phone tooling.

## Hunting ARTEX Infrastructure with Hunt.io

Four open directories provided two initial indicators: the ARTEX console host and its Hong Kong jump host. Using these indicators, Hunt.io SQL enables **three** primary hunting approaches based on certificate metadata, malware classification, and HTTP page titles.

The queries below were executed against Hunt.io during this analysis. Each query is reproduced as written, alongside its reported results and the evidence it provides.

Hunt.io supports three complementary approaches to hunting ARTEX infrastructure:

1. **Certificate pivot**: Search for the ARTEX issuer organization to identify hosts exposing the matching TLS certificate.
2. **Malware classification**: Query malware.name for ARTEX to obtain a broader set of candidate IP addresses.
3. **HTTP title matching**: Search for the exact console title, then expand the search to identify translated and modified title variants.

### Certificate-Based Infrastructure Hunting

The ARTEX console at [38.244.50\[.\]120](https://portal.hunt.io/ip/38.244.50.120/ssl-history) presented a TLS certificate with ARTEX as its issuer organization. Hunt.io's SSL history records the certificate with the following SHA-256 fingerprint:

```
        C7A884AFCD7F91408921890D9617BEF6BFAC3DAE992BC25BB9C48C0395A60842
```

The certificate's subject common name is 38.244.50.120. Its recorded validity period runs from September 25, 2026, to September 22, 2036.

Figure 15. Hunt.io SSL history for 38.244.50.120, showing the ARTEX-issued certificate on port 443 and its SHA-256 fingerprint, providing a certificate-based indicator for hunting related infrastructure.
The issuer organization provides a useful search pivot because it is a specific, distinctive string. Searching for this value can identify hosts that retain the same certificate configuration.

**SQL query**:

```
SELECT
  ip
FROM
  certificates
WHERE
  issuer.organization = 'ARTEX'
  AND timestamp gt '2026-01-01'
GROUP BY
  ip
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT%0A++ip%0AFROM%0A++certificates%0AWHERE%0A++issuer.organization+%3D+%27ARTEX%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++ip&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
The [result](https://portal.hunt.io/sql?sql=SELECT%0A++ip%0AFROM%0A++certificates%0AWHERE%0A++issuer.organization+%3D+%27ARTEX%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++ip&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results) returned 19 distinct IP addresses, including 38.244.50\[.\]120. This method is precise but limited to hosts that expose a matching certificate. Systems using a different certificate will not appear in these results.

### Hunting ARTEX Through Malware Classification

ARTEX infrastructure through the malware.name field. Searching this classification provides broader coverage than the certificate pivot because it does not require the host to retain the same certificate.

**SQL query**:

```
SELECT
  ip
FROM
  malware
WHERE
  malware.name == 'ARTEX'
  AND timestamp gt '2026-01-01'
GROUP BY
  ip
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT%0A++ip%0AFROM%0A++malware%0AWHERE%0A++malware.name+%3D%3D+%27ARTEX%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++ip&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
The [result](https://portal.hunt.io/sql?sql=SELECT%0A++ip%0AFROM%0A++malware%0AWHERE%0A++malware.name+%3D%3D+%27ARTEX%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++ip&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results) returned 1,303 distinct IP addresses. The difference demonstrates the broader coverage of Hunt.io's ARTEX classification compared with a single certificate attribute.

#### Geographic Distribution of ARTEX-Tagged IP Addresses

We have performed an aggregation to find a view of the geographic distribution of ARTEX-tagged IP addresses.

**SQL query**:

```
SELECT
  asn.country_code, uniq(ip) as hits
FROM
  malware
WHERE
  malware.name == 'ARTEX'
  AND timestamp gt '2026-01-01'
GROUP BY
  asn.country_code
ORDER BY
  hits DESC
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT%0A++asn.country_code%2C+uniq%28ip%29+as+hits%0AFROM%0A++malware%0AWHERE%0A++malware.name+%3D%3D+%27ARTEX%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++asn.country_code%0AORDER+BY%0A++hits+DESC&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
The [result](https://portal.hunt.io/sql?sql=SELECT%0A++asn.country_code%2C+uniq%28ip%29+as+hits%0AFROM%0A++malware%0AWHERE%0A++malware.name+%3D%3D+%27ARTEX%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++asn.country_code%0AORDER+BY%0A++hits+DESC&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results) shows 30 different countries having ARTEX infrastructure. The United States accounts for the largest number of IP addresses, followed by China and Hong Kong. These figures describe the country attribution of the observed IP addresses, not necessarily the physical location of the operator.

**HTTP Title-Based Infrastructure Hunting**

The ARTEX login page provides another fingerprint through its HTML document title.

The console observed at 38.244.50\[.\]120 uses the following title:

```
        ARTEX - 自主渗透测试控制台
```

This title matches the banner reported by Genians and provides a direct string for searching HTTP observations in Hunt.io.

**SQL query**:

```
SELECT
  ip
FROM
  http
WHERE
  html.head.title == 'ARTEX --- 自主渗透测试控制台'
  AND timestamp gt '2026-01-01'
GROUP BY
  ip
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT%0A++ip%0AFROM%0A++http%0AWHERE%0A++html.head.title+%3D%3D+%27ARTEX+---+%E8%87%AA%E4%B8%BB%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E6%8E%A7%E5%88%B6%E5%8F%B0%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++ip&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
The [result](https://portal.hunt.io/sql?sql=SELECT%0A++ip%0AFROM%0A++http%0AWHERE%0A++html.head.title+%3D%3D+%27ARTEX+%E2%80%94+%E8%87%AA%E4%B8%BB%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E6%8E%A7%E5%88%B6%E5%8F%B0%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++ip&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results) returned approximately 1,300 unique IP addresses. It suggests that the title-based search has broad coverage in the observed dataset.

### Expanding the Search to Localized Title Variants

A further search can identify additional console instances that use translated or slightly modified titles.

**SQL query**:

```
SELECT
  html.head.title
FROM
  http
WHERE
  html.head.title LIKE '%ARTEX%'
  AND (
    html.head.title LIKE '%--- %'
    OR html.head.title LIKE '%: %'
  )
  AND timestamp gt '2026-01-01'
GROUP BY
  html.head.title
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT%0A++html.head.title%0AFROM%0A++http%0AWHERE%0A++html.head.title+LIKE+%27%25ARTEX%25%27%0A++AND+%28%0A++++html.head.title+LIKE+%27%25---+%25%27%0A++++OR+html.head.title+LIKE+%27%25%3A+%25%27%0A++%29%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++html.head.title&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
The [result](https://portal.hunt.io/sql?sql=SELECT%0A++html.head.title%0AFROM%0A++http%0AWHERE%0A++html.head.title+LIKE+%27%25ARTEX%25%27+AND+%28html.head.title+LIKE+%27%25%E2%80%94+%25%27+OR+html.head.title+LIKE+%27%25%3A+%25%27%29%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++html.head.title&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results) returned 21 distinct title strings, of which 19 were identified as potentially relevant ARTEX console variants during the analysis.

The returned titles include English, Chinese, Korean, Japanese, Russian, Portuguese, and Vietnamese variants.

| Observed title | Language or variant | 
|---|---|
| ARTEX - 自主渗透测试控制台 | Chinese | 
| ARTEX - Autonomous security assessment console | English | 
| ARTEX: Autonomous Penetration Testing Console | English | 
| ARTEX - Console de Teste de Penetração Autônomo | Portuguese | 
| ARTEX - 자율 침투 테스트 콘솔 | Korean | 
| ARTEX - 自律型ペネトレーションテスト管理画面 | Japanese | 
| ARTEX - консоль автономного пентеста | Russian | 
| ARTEX - Bảng điều khiển kiểm thử xâm nhập tự động | Vietnamese | 

## Hunting ARTEX Open Directories via AttackCapture

The certificate, malware classification, and HTTP title pivots discussed above help identify ARTEX infrastructure at a broad level. An additional pivot through [AttackCapture's malware name search](https://hunt.io/features/attackcapture) helps narrow the results to systems where ARTEX operators may have exposed working files and supporting tools.

The search returns  [280 results](https://portal.hunt.io/attackcapture/search-result?query=ARTEX&query_type=malware_name) covering the ARTEX panel itself, other exposed services hosted on the same systems, and open directories that AttackCapture has independently flagged as malicious.

Consider the following example to illustrate how AttackCapture can be used to identify and investigate ARTEX-associated infrastructure.

### Validating an Individual Result

One of the results, **http://130.94.31\[.\]86:18888**, reveals a small open directory containing two files, agt.py and agt4.py, with a combined size of 4.05 KB. [AttackCapture's File Manager](https://portal.hunt.io/attackcapture/filemanager?host=http://130.94.31.86:18888) classifies both files as malicious.

The [host profile](https://portal.hunt.io/ip/130.94.31.86) strengthens this correlation by identifying **ARTEX** as the active malware and displaying a standing warning for a **Potential Malicious Open Directory**. The system is associated with LIGHT NODE LIMITED (AS154177), located in Seoul, South Korea.

A port scan of the same IP address provides additional context. The ARTEX panel operates on port 8787, with the HTML title ARTEX - 自主渗透测试控制台, while the open directory is accessible through the separate port 18888.

Figure 26. The IP address 130.94.31\[.\]86 shows two ports having ARTEX labels that validate our hunt.
The second example reveals an SMB reconnaissance and lateral movement toolkit whose own filenames contain an explicit reference to ARTEX.

The IP address [156.251.11\[.\]39](https://portal.hunt.io/ip/156.251.11.39) belongs to the network associated with **Tcloudnet (AS399077)**, within the IP range 156.251.11.0/24, and is geolocated to Hong Kong. Our platform flags the host as high risk, identifying **ARTEX** as active malware and recording three warnings for potentially malicious open directories on ports 18080, 18084, and 18443. Port 8787 serves the ARTEX panel, identified by the HTML title ARTEX - 自主渗透测试控制台.

The [open directory](https://portal.hunt.io/attackcapture/filemanager?host=http://156.251.11.39:18080) contains an **Impacket**-based toolkit focused on SMB and printer RPC reconnaissance, credential-based authentication, and potential lateral movement. The exposed scripts include **smbls.py**, **splenum.py**, **winregread.py**, **and winrm\_ntlm.py**. The scripts use hardcoded NTLM hashes and a machine account named **ITS-RENDER-01$** to authenticate to internal hosts and enumerate network shares, printers, and registry keys.

The strongest link between the exposed toolkit and the ARTEX name appears in **wtest.py**. It uses impacket to connect to SMB on hardcoded IPs/ports. Uses machine account ITS-RENDER-01$ with provided LM/NTHash to connect, write '**artex\_probe\_11876.txt**' to the print$ share, then attempts deletion.

This example extends the investigation beyond a correlation based on malware classification and service fingerprints. The host exposes an ARTEX-identified panel and a separate directory containing SMB reconnaissance tooling. The artex\_probe\_11876.txt filename provides an additional, direct textual association with ARTEX.

Other notable examples where Artex is found are below:

| Host | Exposed content and observed capabilities | MITRE ATT&CK techniques | 
|---|---|---|
| 202.95.14\[.\]60:18090 | A DedeCMS and FangCMS mass exploitation toolkit containing Python scripts targeting administrative upload endpoints, harvested session cookies, a Godzilla webshell generator that produces AES, Base64, and XOR obfuscated PHP stagers, and SOCKS5 proxy automation. | T1190, T1105, T1078, T1027, T1505.003 | 
| 156.251.11\[.\]39:18080 | An internal post-exploitation toolkit containing multithreaded port scanners, Impacket-based SMB enumeration with hardcoded NTLM hashes for pass-the-hash authentication, and Chisel reverse tunnels mapping public ports to internal SMB, RDP, and WinRM services. The directory also contains a WebSocket command-and-control client. | T1046, T1550.002, T1021.002, T1572, T1090 | 
| 118.107.47\[.\]11:9999 | A CAPTCHA bypass automation suite using Selenium and image processing libraries such as PIL and NumPy to solve GeeTest slider challenges. Additional components include a local proxy that strips or injects headers, AES cryptographic utilities, HTTP and SOCKS5 proxy lists, and a WinRM credential spraying script. | T1110, T1021.003, T1090, T1027, T1059.006 | 
| 212.129.221\[.\]26:8080 | An exploitation toolkit targeting a RuoYi or Spring administrative console. The scripts read an administrator token from /opt/artex/.../admin\_tokens.json, upload malicious Spring beans XML, and abuse the scheduled job API to execute shell commands through ProcessBuilder. | T1190, T1078, T1053, T1059, T1041 | 
| 149.88.85\[.\]20:8899 | CAPTCHA and OCR based login automation, AES and RSA encrypted credential payloads, a harvested administrator JWT, and scripts that create or delete accounts through an administrative API to initiate an internal WebSocket pivot. | T1078, T1110, T1098, T1027, T1046 | 

In this way, an AttackCapture's malware name search provides a useful pivot from identifying ARTEX infrastructure to examining potentially exposed operational artifacts.

## Mitigation and Defensive Recommendations

The findings highlight risks associated with exposed administrative services, reusable credentials, remote access tunnels, proxy infrastructure, and exploitation tooling.

1. Remove unnecessary public access and restrict required administrative access through approved VPNs, allowlists, or dedicated management networks.
2. Reset SSH passwords and rotate API keys, proxy credentials, service tokens, and other secrets that may have been accessible through exposed files.
3. Patch internet-facing services, validate authentication and authorization controls, and restrict sensitive administrative functions.
4. Monitor for unexpected LDAP and JNDI activity, anomalous DNS callbacks, remote script downloads, unusual process execution, and unexplained outbound connections.
5. Enforce least-privilege file permissions and use a managed secrets store for credentials required by applications.
6. Restrict access to model gateways, protect their credentials, and monitor requests for unexpected destinations, unauthorized model endpoints, and suspicious automation.
7. For managed Android and iOS environments, enforce device compliance policies, trusted firmware requirements, application controls, and monitoring for unauthorized rooting, bootloader modification, or jailbreak activity.

## MITRE ATT&CK Matrix

| Tactic | Technique | ID | 
|---|---|---|
| Reconnaissance | Active Scanning | T1595 | 
| Initial Access | Exploit Public-Facing Application | T1190 | 
| Execution | Command and Scripting Interpreter | T1059 | 
| Persistence | Scheduled Task/Job | T1053 | 
| Credential Access | Unsecured Credentials: Credentials in Files | T1552.001 | 
| Lateral Movement | Remote Services: SSH | T1021.004 | 
| Command and Control | Proxy | T1090 | 
| Command and Control | Ingress Tool Transfer | T1105 | 
| Collection | Data from Local System | T1005 | 
| Exfiltration | Exfiltration Over Web Service | T1567 | 
| Privilege Escalation | Exploitation for Privilege Escalation | T1068 | 

## Indicator of Compromise (IOC) table

| Indicator | Type | Context | 
|---|---|---|
| 38.244.50\[.\]120 | IPv4 address | ARTEX console host and SSH tunnel destination referenced in recovered configuration | 
| 23.248.226\[.\]250 | IPv4 address | Hong Kong jump host with exposed directories and supporting tooling | 
| 154.201.79\[.\]246 | IPv4 address | Proxy service used by proxy enumeration scripts; also reported by external sources cited in the draft | 
| xcai\[.\]pro | Domain | AI service reseller domain associated with the reported campaign | 
| direct\[.\]xcai\[.\]pro | Domain | Endpoint referenced in the model-routing configuration | 
| fofoapi\[.\]com | Domain | Third-party API endpoint used by the recovered FOFA client | 
| u6ud2s\[.\]dnslog\[.\]cn | Domain | DNS callback hostname referenced by the staged exploitation artifact | 
| 38.244.50.120:8000 | IP and port | Exposed directory containing scripts and supporting files | 
| 23.248.226.250:18099 | IP and port | Exposed directory containing 42 files across two subdirectories | 
| 23.248.226.250:8001 | IP and port | Directory hosting the JNDI/LDAP exploitation setup | 
| C7A884AFCD7F91408921890D9617 BEF6BFAC3DAE992BC25BB9C48C0395A60842 | SHA-256 certificate fingerprint | TLS certificate associated with 38.244.50\[.\]120, with issuer organization ARTEX | 
| ARTEX - 自主渗透测试控制台 | HTTP title | Observed ARTEX console title used for Hunt.io searches | 

## Conclusion

The investigation expands the ARTEX campaign view beyond its publicly reported infrastructure. Analysis of exposed directories associated with 38.244.50\[.\]120 and 23.248.226\[.\]250 uncovered AI model-routing components, remote access scripts, proxy management utilities, exploitation tooling, and mobile-device utilities. These artifacts indicate a broader operational environment supporting reconnaissance, exploitation, and infrastructure management.

Hunt.io queries provided additional leads through certificate metadata, malware classification, and HTTP title matching. The malware classification query returned 1,303 distinct IP addresses, while certificate and title searches offered complementary methods for identifying potentially related hosts.

These findings show the value of combining infrastructure intelligence with exposed-file analysis and source-code inspection. This approach helps investigators move beyond isolated indicators, identify relationships between operational components, and develop more targeted detection and response measures. Further validation against independent telemetry and threat intelligence will be necessary to establish the full scope of the infrastructure and its relationship to the reported activity.

[Track ARTEX across IOCs and infrastructureARTEX infrastructure is still going up right now. Start free and pivot across live certificates, malware tags and exposed directories before the next one lands in a blocklist.Start hunting now](https://hunt.io/get-started)

**Disclosure note: Hunt.io notified the relevant national CERT prior to publication. No personal records or credentials from the affected systems appear in this report.**

[Open directories](https://hunt.io/glossary/open-directories) are among the most valuable sources of insight into active threat actor operations. When an attacker misconfigures a staging server, the exposure can reveal far more than the final payload. In early October 2026, [CrowdStrike reported](https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/) that an unknown, financially motivated threat actor had used [ARTEX](https://labs.cloudsecurityalliance.org/research/csa-research-note-artex-agentic-pentest-tool-korean-banks-20/), an AI-driven autonomous penetration testing framework, in intrusions targeting South Korean financial organizations. [The Hacker News](https://thehackernews.com/2026/10/artex-ai-pentesting-tool-used-in-data.html) and [Security Affairs](https://securityaffairs.com/200661/hacking/ai-driven-tool-artex-used-in-attacks-against-south-korean-banks.html) subsequently covered the campaign, bringing wider attention to the use of AI-driven offensive tooling in real-world intrusions.

The public reporting identified a key server at 38.244.50\[.\]120, nine additional IP addresses described as proxies, and the LLM reseller domain xcai\[.\]pro.

**But the public indicators were only part of the story.**

Our investigation examines **another** infrastructure at 23.248.226\[.\]250 associated with the reported campaign.  The findings reveal a broader operational environment that includes AI model-routing components, proxy infrastructure, exploitation tooling, credential-handling scripts, and mobile-device utilities.

This research walks through the evidence, the infrastructure pivots, and the artifacts recovered from the exposed directories to show what can be learned when an investigation goes beyond the initial indicators of compromise.

## Key Takeaways

- Our investigation revealed a new open directory at 23.248.226\[.\]250 which acts as a Hong Kong-based jump server.
- The analysis found Claude Code configurations, custom model-routing shims, and 19 agent skills that supported reconnaissance, web testing, payment logic analysis, and mobile operations.
- The recovered configuration and routing scripts reference **DeepSeek**, **GLM**, and **Grok-related** components, providing evidence of a multi-model setup consistent with the reported use of alternative AI services.
- FOFA-related tooling and a proxy service at **154.201.79\[.\]246:443** provided additional infrastructure pivots, with 79 unique exit IPs observed in an initial sample of 100 identities.
- Cryptocurrency, Linux exploitation, and mobile-device artifacts were also recovered, but their direct relationship to the reported South Korean breaches remains unconfirmed.
- The recovered tooling includes reconnaissance scripts, proxy enumeration utilities, reverse SSH tunnel management, a staged JNDI/LDAP exploitation setup, Linux privilege-escalation exploits, and mobile-device tooling.
- Hunt.io pivoting expanded the set of candidates for ARTEX infrastructure through **certificate metadata**, **ARTEX malware classification**, and **HTTP title matching**, providing complementary hunting methods.

## Background and Campaign Overview

Between late September and early October 2026, [seven South Korean financial institutions](https://threatbook.io/blog/artex-attacks-south-korean-financial-institutions) experienced data breaches involving internet-facing peripheral systems. Approximately 66,000 to 67,000 individuals and around 2,200 corporations [were affected](https://asianews.network/south-korean-police-launch-major-probe-as-suspected-ai-hacks-sweep-through-banks/), with personal, employment, income, and loan-related information exposed.

[CrowdStrike](https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/) published its findings on October 7, 2026, followed by the [Genians Security Center (GSC)](https://www.genians.co.kr/blog/threat_intelligence/banking-cyber-attack) on October 12. Both reports attributed the activity to **ARTEX**, an open-source autonomous penetration testing framework developed in China and licensed under the GNU Affero General Public License version 3.0 (AGPL-3.0).

CrowdStrike assessed with moderate confidence that the operator was a single **Chinese-speaking individual** motivated by financial gain rather than an established threat group. The assessment identified **DeepSeek v4.1** Flash as the primary model, with **GLM 5.3** from **Zhipu AI** and **Grok 4.6** serving as backup models.

The infrastructure reportedly accessed these services in part through the reseller domain [xcai\[.\]pro](https://portal.hunt.io/domain/xcai.pro). Both reports described a two-server configuration, consisting of a Hong Kong-based IP address used as primary infrastructure and [38.244.50\[.\]120](https://portal.hunt.io/ip/38.244.50.120), which hosted the ARTEX console.

GSC also reported that the original **ARTEX GitHub repository and Docker image were removed** on October 11, although forks and mirrors remained available.

## Infrastructure Discovery and Initial Pivoting

Our intelligence for [38.244.50\[.\]120](https://portal.hunt.io/ip/38.244.50.120) provides a more detailed view of the infrastructure associated with the **ARTEX campaign**. The address falls within the [38.244.48.0/21](https://portal.hunt.io/ip-block/38.244.48.0/21) network and is attributed to [AS174](https://portal.hunt.io/asn/AS174), operated by Cogent Communications, LLC. Hunt.io identifies its location as Los Angeles, California, United States. The record shows seven warnings, 73 associations, 17 pivots, and 13 code search results.

Our solution lists 15 open ports, including SSH on ports 22 and 8443, HTTPS on port 443, and several HTTP services on nonstandard ports. The ARTEX login interface appears on ports 443 and 8090, with the page title displaying "**ARTEX - 自主渗透测试控制台**". Port 5918 hosts a web interface titled "**Gemini2API - 管理控制台**", served by Uvicorn, while ports 9003, 18080, and 18098 expose HTTP services identified as Python BaseHTTP servers. A **Tinyproxy service** is also identified on port 18888.

Our [AttackCapture™](https://hunt.io/features/attackcapture) platform reports 23 files totaling 6.69 MB, with no subdirectories. The captured data is associated with the host [38.244.50\[.\]120:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://38.244.50.120:8000), geolocated to Los Angeles, California, United States, and includes a recorded timestamp of **August 22, 2026**.

We have expanded the infrastructure by searching "**38.244.50\[.\]120**" in AttackCapture and found another open directory at [23.248.226\[.\]250](https://portal.hunt.io/ip/23.248.226.250) acting as a **jump server**. The code search returned 13 matching results, including configuration files containing hardcoded credential references, scripts suggesting remote file synchronization, and commands designed to download and execute remote scripts.

The second IP address, [23.248.226\[.\]250](https://portal.hunt.io/ip/23.248.226.250), is associated with [AS138415](https://portal.hunt.io/asn/AS138415) (Yancy Limited) and the network range 23.248.224.0/20. The IP is geolocated to Tung Chung, Islands, Hong Kong, and is associated with [RedLuff, LLC (redluff.com)](https://portal.hunt.io/host-radar/redluff.com). AttackCapture reports revealed **three** AttackCapture warnings for potentially malicious open directories, recorded on September 5, September 26, and October 5, 2026.

The AttackCapture associated with the second IP, [23.248.226\[.\]250](https://portal.hunt.io/attackcapture/filemanager?host=http://23.248.226.250:18099), exposes a directory containing 42 files across 2 subdirectories, with a total reported size of 105 MB. The directory was last recorded on September 26, 2026, at 14:47 and is accessible via HTTP on port 18099.

## Evidence Linking the Exposed Infrastructure to ARTEX

The most direct link between **23.248.226\[.\]250** and the published ARTEX IOC is the jump-host configuration recovered from the exposed directory at **23.248.226\[.\]250:18099**.

The directory contains a file named **.secrets** and a corresponding backup named **.secrets.bak-20260911**. These files reportedly use **Unix permission mode 600**, which restricts access to the file owner under standard Unix permission semantics. It also contains the same Chinese-language operational comment, which translates to: "**Sole source of credentials; permission 600; never paste plaintext into a session; read only the specific line when needed.**"

The additional credential fields identify other configured services, including a **Zhipu AI API key**, an **OpenAI-compatible relay key**, and **Webshare credentials**.

```
# sole source of credentials, chmod 600, never paste plaintext in a session
JUMPHOST=38.244.50.120
JUMPHOST_USER=root
JUMPHOST_PASS=[REDACTED]
ZAI_KEY=[REDACTED, Zhipu AI / GLM API key]
RELAY_KEY=sk-[REDACTED, OpenAI compatible relay key]
WEBSHARE_USER=[REDACTED]
WEBSHARE_PASS=[REDACTED]
```
                Copy
The credential-file evidence is corroborated by three shell scripts (**local-boot.sh**, **tunnel-watchdog.sh**, and **sync-memory.sh**) recovered from the same host. All three reference 38.244.50\[.\]120 and use sshpass to supply a password for SSH-based operations targeting the remote root account.

The scripts reveal three complementary functions.

- **local-boot.sh** restores a reverse SSH tunnel after startup, forwarding the local service on port 8100 to the jump host, and launches a local sing-box relay configured to listen on port 11050.
- **tunnel-watchdog.sh** checks for an existing reverse tunnel associated with port 22222 and starts it if the expected process is absent. The accompanying comment identifies the remote forwarding target as local port 48989, associated with a read-only Dufs service.
- **sync-memory.sh** copies Markdown files from a local memory directory to five destination paths on the jump host and then attempts ownership adjustments for directories associated with the grok and gemini accounts.

A **ZAI\_KEY** entry in the available file provides access to Zhipu AI's GLM models, while a tunnel defined in **local-boot.sh** is explicitly named grok2api. This architecture offers a plausible explanation for CrowdStrike's observation that multiple LLM backends were active within the same campaign.

## AI Model Routing and Runtime Configuration

A state file named **.claude.json** confirms that the harness is Claude Code itself, running base version 2.1.221, with 510 recorded startups since August 4, 2026. However, the installation is not communicating directly with Anthropic's API.

A small local proxy, **ds-models-shim.py**, addresses a compatibility issue: the official **/v1/models** endpoint returns a 404 response when queried against a non-Anthropic backend, preventing Claude Code from discovering the available models. The shim intercepts that specific request and returns a locally defined model list containing **deepseek-v4-pro** and **deepseek-flash**. All other requests are forwarded to api.deepseek.com/anthropic.

A second proxy, **xcai-effort-shim.py**, provides further insight into the setup. Its docstring describes the request-routing chain in the operator's own words, translated from Chinese: "The Gemini user path is Claude Code to CCR on port 3456, then to xcai at direct\[.\]xcai\[.\]pro, and finally to DeepSeek."

**CCR**, or **Claude Code Router**, is an open-source project that enables Claude Code to communicate with alternative model backends. The xcai\[.\]pro domain is also significant: CrowdStrike has reportedly identified it as an indicator associated with this campaign. The shim's specific function is to inject a **reasoning\_effort** field into every outgoing request. According to the operator's documentation, this parameter is necessary because the **DeepSeek** backend accessed through xcai otherwise skips its reasoning stage.

## Custom Agent Skills and Operational Workflows

The same **.claude.json** file records usage counts for 19 custom Claude Code skills, which are reusable instruction sets written by the operator for the agent. These skills provide a clear picture of the operation and the tasks the agent was designed to carry out.

They provide an overview of the operation's main activities, from reconnaissance and application analysis to mobile device automation and payment testing.

| Skill | Function | 
|---|---|
| code-audit | Reviewing source code and application configurations | 
| recon | Enumerating targets and discovering assets | 
| web-inject | Injecting payloads into web application workflows | 
| hae | Enumerating web assets and identifying the attack surface | 
| cloud-phone | Managing rented Android cloud phone instances | 
| xingjie-cloudphone | Controlling Xingjie (星界) cloud phone services | 
| hemax-adb | Automating interactions with cloud phone instances through ADB | 
| js-api-mining | Extracting internal JavaScript API calls from target websites | 
| waf-bypass | Testing methods to bypass web application firewalls | 
| web-auth | Examining authentication flows and potential bypasses | 
| tg-miniapp | Testing Telegram Mini Apps | 
| apk-download | Downloading target Android APK files | 
| oversea-cloudphone | Provisioning overseas cloud phone instances | 
| b2-archive | Archiving evidence in Backblaze B2 | 
| decompile | Decompiling APK files and other binaries | 
| apk-internal-hunting | Searching decompiled APKs for internal endpoints and exposed secrets | 
| attack-variants | Generating variations of exploit payloads | 
| file-ssrf | Testing for server-side request forgery through file handling features | 
| payment-logic | Testing payment and cash-in business logic | 

The payment-logic skill is particularly notable because a file named .secrets-cashin-test-accounts was found alongside it. The file contains three self-registered accounts with JWTs for a cash-in deposit API. A source comment describes the accounts as part of an authorized, self-built test dated September 12, 2026. Each account has its own user ID and bank account ID.

This setup is consistent with an approach to testing for insecure direct object reference (IDOR) vulnerabilities.

Genians and CrowdStrike have described similar techniques in connection with attacks against Korean loan and inquiry services.

## Reconnaissance Tooling and Staged RCE Exploitation

The same directory contains the tools used to support reconnaissance, manage proxy infrastructure, and stage a remote code execution (RCE) chain.

### FOFA Access Through a Third-Party API

**fofa2.py** is a Python client for FOFA, a Chinese cyberspace asset search engine commonly compared with Shodan and Censys. The script sends requests to the third-party service fofoapi.com. It constructs an HMAC-SHA256 signature, generates a timestamp and nonce, and submits search parameters through the service's **/api/v1/search/all** endpoint.

A comment in the source code states that the primary membership had expired and that a backup key was being used. This suggests that the operator had previously relied on a paid FOFA membership and had switched to an alternative access method.

```
def nonce():
    return hashlib.sha256(
        (UA + "1920x1080x24" + "zh-CN" + SALT).encode()
    ).hexdigest()[:32]
url = "https://fofoapi.com/api/v1/search/all?" +
      urllib.parse.urlencode(params)
### Tracking Proxy Enumeration and Exit-IP Tracking
```
                Copy
The scripts **proxypool.py** and **proxypool\_enum.py** manage and enumerate a rotating proxy service exposed at 154.201.79\[.\]246:443. The service accepts credentials following the **Default.customerNNN** naming pattern, allowing the operator to test multiple customer identities against the same endpoint.

It uses concurrent requests to identify exit IP addresses, retries failed probes, and maintains a persistent ledger linking identities to observed IP addresses and project assignments. The scripts also identify shared exit IPs and compare results across sampling rounds.

The initial sample reportedly contained **79 unique exit IP addresses** among the first 100 identities tested. This demonstrates that the service can expose multiple exit IPs through a single proxy endpoint.

The address 154.201.79\[.\]246 is also identified as a proxy-related indicator in reporting by **CrowdStrike**, **ThreatBook**, and **Cybersecurity News**.

### JNDI/LDAP Exploitation Infrastructure

Another open directory at [23.248.226\[.\]250:8001](https://portal.hunt.io/attackcapture/filemanager?host=http://23.248.226.250:8001) holds a small, self-contained JNDI and LDAP exploitation rig built on the UnboundID LDAP SDK. According to the associated logs, the chain was staged and retrieved on **October 5, 2026, at 03:42 UTC**.

The **LDAPRefServer.java** and **LDAP2.java** create an in-memory LDAP directory server that returns specially crafted Java naming references in response to search requests. The server modifies search results to include a **javaNamingReference** object with attributes specifying a Java class name, a codebase URL, and a factory class. In **LDAP2.java**, these attributes point to the Exploit class hosted at the same external address.

The supplied **Exploit.class** provides further evidence of the intended execution chain. Its static initializer invokes system commands, including id, hostname, and uname -a, and also attempts to read /etc/hostname. The resulting output is sanitized before being incorporated into a DNSLog callback hostname under **u6ud2s.dnslog.cn**.

This mechanism is designed to confirm command execution through an out-of-band DNS interaction. The compiled class also contains references to HTTP-based retrieval commands, indicating an alternative mechanism for transmitting data.

The accompanying **mux.py** script provides a single entry point for HTTP and LDAP traffic. It inspects the first bytes of each incoming connection and forwards HTTP-like requests to a local service on port 8000, while routing other connections to the LDAP service on port 1389. This arrangement allows the two services to share one listening port, provided the traffic can be classified by its initial bytes.

## Recovered Tooling and Payloads: Exchange Access and Mobile Device Operations

The files recovered from 38.244.50\[.\]120:8000 and from 23.248.226\[.\]250:8907 contained a diverse collection of scripts, binaries, source files, and configuration artifacts associated with cryptocurrency-exchange access, Linux exploitation, and mobile-device operations.

The following table summarizes the recovered artifacts and their observed or apparent functions.

| Artifact | Observed functionality or contents | 
|---|---|
| x.js | Checks for an authenticated YIIMP administrator session, tests default credentials, and includes functionality associated with initiating withdrawals. | 
| x.sh | Supports reverse-shell access, collects configuration and key files, and scans local ports associated with cryptocurrency-wallet RPC services. | 
| relay.py | Provides a listener on port 4444. | 
| server.py | Provides a service on port \`8000 associated with payload handling and data collection. | 
| tg.py | Implements Telegram-based notifications. | 
| tg.conf | Contains Telegram bot and chat configuration fields, with sensitive values redacted. | 
| shells.log | Stores shell-related log entries. | 
| BlocPalX files | Recovered files associated with the BlocPalX cryptocurrency platform. | 
| les.sh | Linux exploit suggester script. | 
| Poc2588 Exp2588 exp2588\_44 | Exploit or proof-of-concept builds associated with CVE-2022-2588. | 
| cve5054-static cve5054 variants, including v2/v3 musl builds | Multiple binaries associated with CVE-2025-5054, including statically linked or alternative-library builds. | 
| cv3p, cvx cve3493-static | Additional exploit-related binaries whose precise CVE associations or functions remain unconfirmed. | 
| aio\_uaf.c | iOS exploit-related source code referencing a use-after-free technique. | 
| poc65343\_probe.c | iOS proof-of-concept or probing source associated with identifier 65343. | 
| ios26\_probe.c | Probe source associated with iOS 26. | 
| stub.c, stub65343.c | Supporting C source files associated with the mobile proof-of-concept artifacts. | 
| Android KernelPatch tools | Utilities associated with Android kernel patching. | 
| payload-dumper-go.exe | Utility for extracting payload contents from Android firmware packages. | 
| Patched EDL firmware files | Modified firmware artifacts associated with Emergency Download Mode workflows. | 
| recv.py | Receives data on port 8082. | 
| wxapkg-watchdog.sh.\_\_rev2 | Watchdog script associated with a WeChat mini-program package. | 
| cloudphone-oversea.key | Credential or key file associated with overseas cloud-phone operations. | 

The recovered artifacts fall into two broad operational areas. The **first** concerns cryptocurrency-exchange access and web application workflows, including administrator-session checks, withdrawal functionality, shell access, and collection of configuration files. The **second** concerns Linux exploitation and mobile-device research, including kernel exploit builds, iOS proof-of-concept source files, Android firmware utilities, and cloud-phone tooling.

## Hunting ARTEX Infrastructure with Hunt.io

Four open directories provided two initial indicators: the ARTEX console host and its Hong Kong jump host. Using these indicators, Hunt.io SQL enables **three** primary hunting approaches based on certificate metadata, malware classification, and HTTP page titles.

The queries below were executed against Hunt.io during this analysis. Each query is reproduced as written, alongside its reported results and the evidence it provides.

Hunt.io supports three complementary approaches to hunting ARTEX infrastructure:

1. **Certificate pivot**: Search for the ARTEX issuer organization to identify hosts exposing the matching TLS certificate.
2. **Malware classification**: Query malware.name for ARTEX to obtain a broader set of candidate IP addresses.
3. **HTTP title matching**: Search for the exact console title, then expand the search to identify translated and modified title variants.

### Certificate-Based Infrastructure Hunting

The ARTEX console at [38.244.50\[.\]120](https://portal.hunt.io/ip/38.244.50.120/ssl-history) presented a TLS certificate with ARTEX as its issuer organization. Hunt.io's SSL history records the certificate with the following SHA-256 fingerprint:

```
        C7A884AFCD7F91408921890D9617BEF6BFAC3DAE992BC25BB9C48C0395A60842
```

The certificate's subject common name is 38.244.50.120. Its recorded validity period runs from September 25, 2026, to September 22, 2036.

Figure 15. Hunt.io SSL history for 38.244.50.120, showing the ARTEX-issued certificate on port 443 and its SHA-256 fingerprint, providing a certificate-based indicator for hunting related infrastructure.
The issuer organization provides a useful search pivot because it is a specific, distinctive string. Searching for this value can identify hosts that retain the same certificate configuration.

**SQL query**:

```
SELECT
  ip
FROM
  certificates
WHERE
  issuer.organization = 'ARTEX'
  AND timestamp gt '2026-01-01'
GROUP BY
  ip
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT%0A++ip%0AFROM%0A++certificates%0AWHERE%0A++issuer.organization+%3D+%27ARTEX%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++ip&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
The [result](https://portal.hunt.io/sql?sql=SELECT%0A++ip%0AFROM%0A++certificates%0AWHERE%0A++issuer.organization+%3D+%27ARTEX%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++ip&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results) returned 19 distinct IP addresses, including 38.244.50\[.\]120. This method is precise but limited to hosts that expose a matching certificate. Systems using a different certificate will not appear in these results.

### Hunting ARTEX Through Malware Classification

ARTEX infrastructure through the malware.name field. Searching this classification provides broader coverage than the certificate pivot because it does not require the host to retain the same certificate.

**SQL query**:

```
SELECT
  ip
FROM
  malware
WHERE
  malware.name == 'ARTEX'
  AND timestamp gt '2026-01-01'
GROUP BY
  ip
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT%0A++ip%0AFROM%0A++malware%0AWHERE%0A++malware.name+%3D%3D+%27ARTEX%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++ip&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
The [result](https://portal.hunt.io/sql?sql=SELECT%0A++ip%0AFROM%0A++malware%0AWHERE%0A++malware.name+%3D%3D+%27ARTEX%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++ip&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results) returned 1,303 distinct IP addresses. The difference demonstrates the broader coverage of Hunt.io's ARTEX classification compared with a single certificate attribute.

#### Geographic Distribution of ARTEX-Tagged IP Addresses

We have performed an aggregation to find a view of the geographic distribution of ARTEX-tagged IP addresses.

**SQL query**:

```
SELECT
  asn.country_code, uniq(ip) as hits
FROM
  malware
WHERE
  malware.name == 'ARTEX'
  AND timestamp gt '2026-01-01'
GROUP BY
  asn.country_code
ORDER BY
  hits DESC
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT%0A++asn.country_code%2C+uniq%28ip%29+as+hits%0AFROM%0A++malware%0AWHERE%0A++malware.name+%3D%3D+%27ARTEX%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++asn.country_code%0AORDER+BY%0A++hits+DESC&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
The [result](https://portal.hunt.io/sql?sql=SELECT%0A++asn.country_code%2C+uniq%28ip%29+as+hits%0AFROM%0A++malware%0AWHERE%0A++malware.name+%3D%3D+%27ARTEX%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++asn.country_code%0AORDER+BY%0A++hits+DESC&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results) shows 30 different countries having ARTEX infrastructure. The United States accounts for the largest number of IP addresses, followed by China and Hong Kong. These figures describe the country attribution of the observed IP addresses, not necessarily the physical location of the operator.

**HTTP Title-Based Infrastructure Hunting**

The ARTEX login page provides another fingerprint through its HTML document title.

The console observed at 38.244.50\[.\]120 uses the following title:

```
        ARTEX - 自主渗透测试控制台
```

This title matches the banner reported by Genians and provides a direct string for searching HTTP observations in Hunt.io.

**SQL query**:

```
SELECT
  ip
FROM
  http
WHERE
  html.head.title == 'ARTEX --- 自主渗透测试控制台'
  AND timestamp gt '2026-01-01'
GROUP BY
  ip
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT%0A++ip%0AFROM%0A++http%0AWHERE%0A++html.head.title+%3D%3D+%27ARTEX+---+%E8%87%AA%E4%B8%BB%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E6%8E%A7%E5%88%B6%E5%8F%B0%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++ip&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
The [result](https://portal.hunt.io/sql?sql=SELECT%0A++ip%0AFROM%0A++http%0AWHERE%0A++html.head.title+%3D%3D+%27ARTEX+%E2%80%94+%E8%87%AA%E4%B8%BB%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E6%8E%A7%E5%88%B6%E5%8F%B0%27%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++ip&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results) returned approximately 1,300 unique IP addresses. It suggests that the title-based search has broad coverage in the observed dataset.

### Expanding the Search to Localized Title Variants

A further search can identify additional console instances that use translated or slightly modified titles.

**SQL query**:

```
SELECT
  html.head.title
FROM
  http
WHERE
  html.head.title LIKE '%ARTEX%'
  AND (
    html.head.title LIKE '%--- %'
    OR html.head.title LIKE '%: %'
  )
  AND timestamp gt '2026-01-01'
GROUP BY
  html.head.title
```
                [Run in HuntSQL](https://portal.hunt.io/sql?sql=SELECT%0A++html.head.title%0AFROM%0A++http%0AWHERE%0A++html.head.title+LIKE+%27%25ARTEX%25%27%0A++AND+%28%0A++++html.head.title+LIKE+%27%25---+%25%27%0A++++OR+html.head.title+LIKE+%27%25%3A+%25%27%0A++%29%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++html.head.title&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results)Copy
The [result](https://portal.hunt.io/sql?sql=SELECT%0A++html.head.title%0AFROM%0A++http%0AWHERE%0A++html.head.title+LIKE+%27%25ARTEX%25%27+AND+%28html.head.title+LIKE+%27%25%E2%80%94+%25%27+OR+html.head.title+LIKE+%27%25%3A+%25%27%29%0A++AND+timestamp+gt+%272026-01-01%27%0AGROUP+BY%0A++html.head.title&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results) returned 21 distinct title strings, of which 19 were identified as potentially relevant ARTEX console variants during the analysis.

The returned titles include English, Chinese, Korean, Japanese, Russian, Portuguese, and Vietnamese variants.

| Observed title | Language or variant | 
|---|---|
| ARTEX - 自主渗透测试控制台 | Chinese | 
| ARTEX - Autonomous security assessment console | English | 
| ARTEX: Autonomous Penetration Testing Console | English | 
| ARTEX - Console de Teste de Penetração Autônomo | Portuguese | 
| ARTEX - 자율 침투 테스트 콘솔 | Korean | 
| ARTEX - 自律型ペネトレーションテスト管理画面 | Japanese | 
| ARTEX - консоль автономного пентеста | Russian | 
| ARTEX - Bảng điều khiển kiểm thử xâm nhập tự động | Vietnamese | 

## Hunting ARTEX Open Directories via AttackCapture

The certificate, malware classification, and HTTP title pivots discussed above help identify ARTEX infrastructure at a broad level. An additional pivot through [AttackCapture's malware name search](https://hunt.io/features/attackcapture) helps narrow the results to systems where ARTEX operators may have exposed working files and supporting tools.

The search returns  [280 results](https://portal.hunt.io/attackcapture/search-result?query=ARTEX&query_type=malware_name) covering the ARTEX panel itself, other exposed services hosted on the same systems, and open directories that AttackCapture has independently flagged as malicious.

Consider the following example to illustrate how AttackCapture can be used to identify and investigate ARTEX-associated infrastructure.

### Validating an Individual Result

One of the results, **http://130.94.31\[.\]86:18888**, reveals a small open directory containing two files, agt.py and agt4.py, with a combined size of 4.05 KB. [AttackCapture's File Manager](https://portal.hunt.io/attackcapture/filemanager?host=http://130.94.31.86:18888) classifies both files as malicious.

The [host profile](https://portal.hunt.io/ip/130.94.31.86) strengthens this correlation by identifying **ARTEX** as the active malware and displaying a standing warning for a **Potential Malicious Open Directory**. The system is associated with LIGHT NODE LIMITED (AS154177), located in Seoul, South Korea.

A port scan of the same IP address provides additional context. The ARTEX panel operates on port 8787, with the HTML title ARTEX - 自主渗透测试控制台, while the open directory is accessible through the separate port 18888.

Figure 26. The IP address 130.94.31\[.\]86 shows two ports having ARTEX labels that validate our hunt.
The second example reveals an SMB reconnaissance and lateral movement toolkit whose own filenames contain an explicit reference to ARTEX.

The IP address [156.251.11\[.\]39](https://portal.hunt.io/ip/156.251.11.39) belongs to the network associated with **Tcloudnet (AS399077)**, within the IP range 156.251.11.0/24, and is geolocated to Hong Kong. Our platform flags the host as high risk, identifying **ARTEX** as active malware and recording three warnings for potentially malicious open directories on ports 18080, 18084, and 18443. Port 8787 serves the ARTEX panel, identified by the HTML title ARTEX - 自主渗透测试控制台.

The [open directory](https://portal.hunt.io/attackcapture/filemanager?host=http://156.251.11.39:18080) contains an **Impacket**-based toolkit focused on SMB and printer RPC reconnaissance, credential-based authentication, and potential lateral movement. The exposed scripts include **smbls.py**, **splenum.py**, **winregread.py**, **and winrm\_ntlm.py**. The scripts use hardcoded NTLM hashes and a machine account named **ITS-RENDER-01$** to authenticate to internal hosts and enumerate network shares, printers, and registry keys.

The strongest link between the exposed toolkit and the ARTEX name appears in **wtest.py**. It uses impacket to connect to SMB on hardcoded IPs/ports. Uses machine account ITS-RENDER-01$ with provided LM/NTHash to connect, write '**artex\_probe\_11876.txt**' to the print$ share, then attempts deletion.

This example extends the investigation beyond a correlation based on malware classification and service fingerprints. The host exposes an ARTEX-identified panel and a separate directory containing SMB reconnaissance tooling. The artex\_probe\_11876.txt filename provides an additional, direct textual association with ARTEX.

Other notable examples where Artex is found are below:

| Host | Exposed content and observed capabilities | MITRE ATT&CK techniques | 
|---|---|---|
| 202.95.14\[.\]60:18090 | A DedeCMS and FangCMS mass exploitation toolkit containing Python scripts targeting administrative upload endpoints, harvested session cookies, a Godzilla webshell generator that produces AES, Base64, and XOR obfuscated PHP stagers, and SOCKS5 proxy automation. | T1190, T1105, T1078, T1027, T1505.003 | 
| 156.251.11\[.\]39:18080 | An internal post-exploitation toolkit containing multithreaded port scanners, Impacket-based SMB enumeration with hardcoded NTLM hashes for pass-the-hash authentication, and Chisel reverse tunnels mapping public ports to internal SMB, RDP, and WinRM services. The directory also contains a WebSocket command-and-control client. | T1046, T1550.002, T1021.002, T1572, T1090 | 
| 118.107.47\[.\]11:9999 | A CAPTCHA bypass automation suite using Selenium and image processing libraries such as PIL and NumPy to solve GeeTest slider challenges. Additional components include a local proxy that strips or injects headers, AES cryptographic utilities, HTTP and SOCKS5 proxy lists, and a WinRM credential spraying script. | T1110, T1021.003, T1090, T1027, T1059.006 | 
| 212.129.221\[.\]26:8080 | An exploitation toolkit targeting a RuoYi or Spring administrative console. The scripts read an administrator token from /opt/artex/.../admin\_tokens.json, upload malicious Spring beans XML, and abuse the scheduled job API to execute shell commands through ProcessBuilder. | T1190, T1078, T1053, T1059, T1041 | 
| 149.88.85\[.\]20:8899 | CAPTCHA and OCR based login automation, AES and RSA encrypted credential payloads, a harvested administrator JWT, and scripts that create or delete accounts through an administrative API to initiate an internal WebSocket pivot. | T1078, T1110, T1098, T1027, T1046 | 

In this way, an AttackCapture's malware name search provides a useful pivot from identifying ARTEX infrastructure to examining potentially exposed operational artifacts.

## Mitigation and Defensive Recommendations

The findings highlight risks associated with exposed administrative services, reusable credentials, remote access tunnels, proxy infrastructure, and exploitation tooling.

1. Remove unnecessary public access and restrict required administrative access through approved VPNs, allowlists, or dedicated management networks.
2. Reset SSH passwords and rotate API keys, proxy credentials, service tokens, and other secrets that may have been accessible through exposed files.
3. Patch internet-facing services, validate authentication and authorization controls, and restrict sensitive administrative functions.
4. Monitor for unexpected LDAP and JNDI activity, anomalous DNS callbacks, remote script downloads, unusual process execution, and unexplained outbound connections.
5. Enforce least-privilege file permissions and use a managed secrets store for credentials required by applications.
6. Restrict access to model gateways, protect their credentials, and monitor requests for unexpected destinations, unauthorized model endpoints, and suspicious automation.
7. For managed Android and iOS environments, enforce device compliance policies, trusted firmware requirements, application controls, and monitoring for unauthorized rooting, bootloader modification, or jailbreak activity.

## MITRE ATT&CK Matrix

| Tactic | Technique | ID | 
|---|---|---|
| Reconnaissance | Active Scanning | T1595 | 
| Initial Access | Exploit Public-Facing Application | T1190 | 
| Execution | Command and Scripting Interpreter | T1059 | 
| Persistence | Scheduled Task/Job | T1053 | 
| Credential Access | Unsecured Credentials: Credentials in Files | T1552.001 | 
| Lateral Movement | Remote Services: SSH | T1021.004 | 
| Command and Control | Proxy | T1090 | 
| Command and Control | Ingress Tool Transfer | T1105 | 
| Collection | Data from Local System | T1005 | 
| Exfiltration | Exfiltration Over Web Service | T1567 | 
| Privilege Escalation | Exploitation for Privilege Escalation | T1068 | 

## Indicator of Compromise (IOC) table

| Indicator | Type | Context | 
|---|---|---|
| 38.244.50\[.\]120 | IPv4 address | ARTEX console host and SSH tunnel destination referenced in recovered configuration | 
| 23.248.226\[.\]250 | IPv4 address | Hong Kong jump host with exposed directories and supporting tooling | 
| 154.201.79\[.\]246 | IPv4 address | Proxy service used by proxy enumeration scripts; also reported by external sources cited in the draft | 
| xcai\[.\]pro | Domain | AI service reseller domain associated with the reported campaign | 
| direct\[.\]xcai\[.\]pro | Domain | Endpoint referenced in the model-routing configuration | 
| fofoapi\[.\]com | Domain | Third-party API endpoint used by the recovered FOFA client | 
| u6ud2s\[.\]dnslog\[.\]cn | Domain | DNS callback hostname referenced by the staged exploitation artifact | 
| 38.244.50.120:8000 | IP and port | Exposed directory containing scripts and supporting files | 
| 23.248.226.250:18099 | IP and port | Exposed directory containing 42 files across two subdirectories | 
| 23.248.226.250:8001 | IP and port | Directory hosting the JNDI/LDAP exploitation setup | 
| C7A884AFCD7F91408921890D9617 BEF6BFAC3DAE992BC25BB9C48C0395A60842 | SHA-256 certificate fingerprint | TLS certificate associated with 38.244.50\[.\]120, with issuer organization ARTEX | 
| ARTEX - 自主渗透测试控制台 | HTTP title | Observed ARTEX console title used for Hunt.io searches | 

## Conclusion

The investigation expands the ARTEX campaign view beyond its publicly reported infrastructure. Analysis of exposed directories associated with 38.244.50\[.\]120 and 23.248.226\[.\]250 uncovered AI model-routing components, remote access scripts, proxy management utilities, exploitation tooling, and mobile-device utilities. These artifacts indicate a broader operational environment supporting reconnaissance, exploitation, and infrastructure management.

Hunt.io queries provided additional leads through certificate metadata, malware classification, and HTTP title matching. The malware classification query returned 1,303 distinct IP addresses, while certificate and title searches offered complementary methods for identifying potentially related hosts.

These findings show the value of combining infrastructure intelligence with exposed-file analysis and source-code inspection. This approach helps investigators move beyond isolated indicators, identify relationships between operational components, and develop more targeted detection and response measures. Further validation against independent telemetry and threat intelligence will be necessary to establish the full scope of the infrastructure and its relationship to the reported activity.

[Track ARTEX across IOCs and infrastructureARTEX infrastructure is still going up right now. Start free and pivot across live certificates, malware tags and exposed directories before the next one lands in a blocklist.Start hunting now](https://hunt.io/get-started)

Related Posts

Related Posts

Related Posts
