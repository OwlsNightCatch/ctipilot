---
title: "Agentic Attacks in the Wild: ARTEX & Offensive AI Frameworks | Wiz Blog"
author: Rami McCarthy; Hila Ramati
url: https://www.wiz.io/blog/agentic-attacks-artex-offensive-ai-frameworks
hostname: wiz.io
description: Wiz Research explores how threat actors use ARTEX and a growing ecosystem of agentic offensive frameworks in the wild, with real case studies and IOCs.
sitename: wiz.io
date: "2026-11-23"
tags: ['Research', 'AI', 'Threat Intel']
fingerprint: "9c914353a78bd166"
language: en
image: https://www.datocms-assets.com/75231/1795090007-agentic-attack-cover.png?fm=webp
pagetype: article
filedate: "2026-11-27"
---
Agentic offensive frameworks like ARTEX are driving a surge in cloud intrusions. Wiz Research shares cases from the wild, including both sides of one attack via the operator's leaked logs, an update on Black October, and the detections that catch these noisy, machine-speed attacks.

**There has been explosive growth in successful agentic attacks, just in the last three weeks**. Since publishing the Black October post, an additional **twenty** related incidents have been disclosed by vendors. Wiz’s CIRT has seen a 3x increase in engagement requests, matching the [trend across the industry](https://www.wsj.com/pro/cybersecurity/incident-response-overload-hacked-companies-have-to-stand-in-line-for-help-86e78ef6) of [overwhelming IR demand](https://www.wsj.com/pro/cybersecurity/companies-face-cyber-pain-as-hackers-press-ai-advantage-2e2669e8).

The activity we’ve observed since late September 2026 uses [ARTEX](https://www.wiz.io/blog/the-rise-of-agentic-attacks#from-artex-to-hermes-agentic-attacks-in-the-wild-3), its public forks and rebrands, and other agentic tools with a similar design.

ARTEX is only one of these frameworks: others seen in the wild include Cairn, CyberStrikeAI and HexStrike, alongside offensive use of generic harness like Hermes, as well as custom offensive harnesses. ARTEX is open source and has hundreds of forks. Activity attributed to “ARTEX” comes from multiple unrelated operators and should not be read as a single campaign or attributed to one threat actor.

## Cases

Wiz Research and CIRT have been hunting, tracking, observing, and responding to a broad set of agentic offensive frameworks attacks, some successful. In addition to [the examples we’ve previously shared](https://www.wiz.io/blog/the-rise-of-agentic-attacks#agentic-attacks-investigated-by-wiz-10), we wanted to provide some cases emblematic of what we’re seeing in this new threat environment.

### Opportunistic Campaigns Using Agentic Offensive Frameworks

The first pattern we see is broad, seemingly opportunistic attacks by actors who have gone all-in on agentic offensive frameworks. These campaigns are frequently:

1. **Proxied through residential and ISP pools**: Requests rotate through commercial residential proxy inventory, often a new exit for every single request. IP-based blocking and IOC sharing do very little.
2. **Noisy**: These agents spray passwords, create canary accounts, hammer sign-up and password-reset flows, and probe every available endpoint. They also label their own work: `pentest`, `probe`, `recon`, and incrementing task numbers show up in user agents, resource names and usernames.
3. **Vector agnostic**: The same operator will try stolen cloud keys, identity-provider OAuth flows, public sign-up flows, anonymous storage access and CI/CD trust, in parallel and across many organizations.

Once a foothold is found, it is used to explore lateral movement, harvest credentials and exfiltrate data.

We wanted to highlight a campaign, one of a dozen campaigns we’re tracking, which we have named "ARTEX-Harvester." We’ve clustered this campaign based on, among other signals, a distinctive boto3 build, incrementing Intent ID correlation cross-victim, and proxy pool usage overlap.

Between late October and mid-November 2026 we tied it, at varying confidence, to activity at more than a dozen organizations. It demonstrates exactly the patterns we highlighted. Almost every request used a different residential or ISP proxy exit - across more than 220 IPs in a single target.

Across the campaign, the same operator attempted:

1. Abuse of stolen credentials
2. Anonymous storage probing
3. Abuse of public sign-up, password-reset and sign-in flows
4. Identity-provider probing

Among the numerous attempted footholds, one success shows how these attacks progress once initial access is achieved.

1. Compromised VCS credentials allowed access to private repositories
2. The attack pivoted from CI to the cloud environment by creating branches that abused CI workload identity trust relationships.
3. Harvest workflows dumped CI-accessible secrets and Terraform state
4. Those secrets and repositories were exfiltrated

In parallel, the operator used a stolen service-account token from an application pod. That account could create privileged pods with the node's root filesystem mounted. The operator used that to deploy a "node-level collector" pod, which harvested the kubelet PKI and every projected service-account token on the node. One of those tokens, belonging to cert-manager, could read the ArgoCD secrets, leading to cluster-admin.

#### Detection

These attacks are far from stealthy. Wiz Issues captured this activity across a variety of rules that are agnostic to the usage of an Agentic Offensive Framework (see below).

Additionally, artifacts were heavily marked with agentic offensive framework self-labeling behavior, including `pentest-recon` user agents, `pentest-*` workspaces and pods, and an incrementing task intent counter (`pentest-iNNNNNN`).

Wiz Sensor caught the behavior within the cluster, including privileged container creation, `nsenter`, IMDS `kube-env` queries and drifted scripts reaching for cloud credentials.

### Targeted Attacks and Open Directories

One of the more interesting byproducts of agentic offensive frameworks is **a trend of poor operational security**. ARTEX shipped with its web console exposed to the internet by default, often still on default credentials, and many operators never lock it down: [Censys counted more than 1,400 exposed ARTEX consoles in early November](https://censys.com/blog/artex-agentic-asbestos).

The result is a steady supply of exposed command-and-control panels and open directories for threat intelligence and security firms to analyze.

Because these frameworks are agentic, those exposures reveal more than attacker actions. They capture **the attack as a narrative**: operator prompts, planner intents, agent transcripts and the model's own reasoning.

#### **Seeing Both Sides of an Attack**

This exposure occasionally grants something rare: both sides of the same intrusion. In some cases, we can pair our telemetry with the relevant attacker’s leaked logs and tools - granting a picture of not just what they did in a single incident, but what they did everywhere else, why they did it, and what they planned next.

**Here is one such anonymized case:**

Across four days in October, an attacker navigated two AWS accounts and seven EKS clusters:

- **Initial foothold**: a stolen Terraform-runner session read the kubelet kubeconfig, then created a privileged pod and a cluster-admin binding.
- **CI compromise**: remote code execution on the Jenkins controller opened a reverse shell to the attacker's server.
- **Node persistence**: a pod escape put a custom loader on the nodes. It was an `ld.so.preload` userland rootkit with a DNS-tunnel channel, disguised as a fontconfig service, and had zero detections on VirusTotal.
- **Credential use off-platform**: node, IRSA and Terraform-runner credentials were used from the attacker's own server to read Terraform state and Secrets Manager, and to open SSM sessions.

The attacker’s open directory colors in the details, across over 3,000 exposed files.

It shows activity outside the observed telemetry:

- **Identity provider**: forged admin tokens gave access to 3,392 users and their live session tokens.
- **Bastion**: beacons were pushed to 19 hosts, and the bastion's database was decrypted for 50 SSH private keys.
- **CI/CD**: GitHub Actions secrets were dumped, and the production Jenkinsfile was modified to run before its approval gate, exposing production secrets.

It also shows more about the attacker’s operations:

- **Command layer**: CyberStrikeAI ran the operation. A csai- prefix is on nearly everything the attacker created (csai-escape pods, a csai-pentest-role IAM role, a csai-probe runner).
- **Operator workspace**: an ARTEX checkout sat alongside .claude, .grok and .agents directories. The same server ran ARTEX tooling against several other organizations that month, unsuccessfully.
- **Reporting**: the operator's own auto-generated Chinese language report masks the intrusion as an "authorised red-team pentest" and claims 58 findings.
- **AI tools as targets**: Anthropic API keys were harvested from 50 hosts, and employees' AI coding-assistant session histories were mined for production SSO credentials.

Since publishing the blog post, disclosed incidents **have more than tripled**. While insufficient details have been shared to link all these incidents to any single actor, or even agentic offensive frameworks in some cases, there is a clear trend where attackers are using agentic offensive frameworks to target rich sources of LLM access and credentials.

Where victims have disclosed a root cause, the entry points are familiar.

- Stolen or leaked credentials (Zeabur, Kernel, Lightning AI, Bitrise)
- Exposed or vulnerable services (Chainstack's default-credential Grafana, NEAR AI's SGLang RCE, Northflank's API zero-day)

Increasingly, the way in was an upstream breach: keys and secrets stolen from one platform opened the next.

The impact is just as consistent. Attackers go straight for environment variables and stored customer secrets, prioritizing AI provider and cloud keys that can be validated, resold or burned on LLM usage [within hours](https://www.wiz.io/blog/black-october-for-ai-developer-platforms#case-a-24).

## Recommendations

Wiz’s [AI Threat Readiness Framework](https://www.wiz.io/platform/ai-threat-readiness) is our blueprint for how to build a security program that can stay ahead of these attacks. Defenders must put AI to work in order to leverage their context advantage against attackers and enable [real machine-speed defense](https://www.wiz.io/blog/wiz-ai-threat-readiness-operating-model) against these new tools and tactics.

### Detections

The following is a representative subset of generic rules that have been observed in relation to agentic offensive framework attacks:

- EC2 Instance Credentials Used Outside Of AWS
- ECS Task Credentials Used Outside Of AWS
- Unusual GetCallerIdentity Operation
- Unusual Mass Access Denied Activity
- Unusual Enumeration Activity by IAM User
- API Calls From Unusual Country
- API Calls by a Known Offensive Tool
- Cluster Accessed From an Unusual Country
- Unusual Mass Secret Value Retrieval
- Attempts To Create Access Token For Multiple Service Accounts
- IAM Role Assumed From New or Inactive Account
- Model access check behavior tied to previously seen attacks
- Azure Application Secret Used After Long Period of Inactivity
- GCP Service Account Key Used After A Long Period Of Inactivity
- IAM Access Key Used After Long Period of Inactivity
- Instance Created Access Token Used Outside GCP
- Permission To Impersonate Any Service Account Granted To Member

Wiz has also developed a set of behavioral detections specific to this activity. Among others, these include:

- Session or Resource Name Matching an AI Offensive Tool Naming Pattern
- AI Offensive Tool Step Counter in Session or Resource Names
- Unusual Pagination Pattern by AWS Identity From New ASO
- Activity From AI Offensive Tool IP Address Seen In Organization
- AI Offensive Tool Activity Detected Via HTTP Endpoint

We note that these rules are expected to be perishable, given the inherent pace of evolution and customization of these tools. Wiz Research continues to develop advanced detection of these attacks based on the behavioral patterns of agent-driven intrusions (their speed, breadth and systematic structure), which persist even as individual tools are renamed, rebranded or customized.

The following are an assortment of IP addresses Wiz observed conducting attacks using agentic offensive frameworks. You can [consume as a CSV](https://github.com/wiz-sec-public/wiz-research-iocs/blob/main/reports/agentic_attacks_in_the_wild_iocs.csv) from our wiz-research-iocs repository.

IP Address

Hosting Provider

Category

Observed (2026)

192.236.187\[.\]90

HostPapa

Used with stolen credentials

Nov 5 – 18

104.223.50\[.\]72

HostPapa

Used with stolen credentials

Nov 5 – 18

107.172.5\[.\]167

HostPapa

Used with stolen credentials

Nov 5 – 18

107.173.104\[.\]66

HostPapa

Used with stolen credentials

Nov 5 – 18

130.94.102\[.\]111

LIGHT NODE

Used with stolen credentials

Nov 8 – 18

130.94.103\[.\]64

LIGHT NODE

Used with stolen credentials

Nov 8 – 18

130.94.109\[.\]218

LIGHT NODE

Used with stolen credentials

Nov 8 – 18

38.60.171\[.\]222

LIGHT NODE

Used with stolen credentials

Nov 8 – 18

172.86.80\[.\]80

RouterHosting

Used with stolen credentials

Late Oct – Nov 22

172.86.82\[.\]159

RouterHosting

Used with stolen credentials

Late Oct – Nov 22

172.86.82\[.\]160

RouterHosting

Used with stolen credentials

Late Oct – Nov 22

172.86.82\[.\]161

RouterHosting

Used with stolen credentials

Late Oct – Nov 22

172.86.82\[.\]163

RouterHosting

Used with stolen credentials

Late Oct – Nov 22

172.86.82\[.\]164

RouterHosting

Used with stolen credentials

Late Oct – Nov 22

172.86.82\[.\]178

RouterHosting

Used with stolen credentials

Late Oct – Nov 22

172.86.82\[.\]179

RouterHosting

Used with stolen credentials

Late Oct – Nov 22

118.107.19\[.\]99

CTG Server

Used with stolen credentials

Nov 3 – 23

137.220.202\[.\]200

CTG Server

Used with stolen credentials

Nov 3 – 23

134.122.173\[.\]40

CTG Server

Used with stolen credentials

Nov 3 – 23

134.122.163\[.\]240

CTG Server

Used with stolen credentials

Nov 3 – 23

143.92.37\[.\]131

CTG Server

Used with stolen credentials

Nov 3 – 23

68.166.169\[.\]20

FDCservers

Used with stolen credentials

Nov 12 – 23

134.222.209\[.\]136

EGIHosting

Used with stolen credentials

Nov 12 – 23

129.80.215\[.\]35

Oracle Cloud

Used with stolen credentials

Nov 12 – 23

129.121.162\[.\]36

Oracle Cloud

Used with stolen credentials

Nov 12 – 23

43.172.40\[.\]251

Tencent Cloud

Used with stolen credentials

Nov 19 – 22

129.226.56\[.\]74

Tencent Cloud

Used with stolen credentials

Nov 19 – 22

142.86.89\[.\]21

Tencent Cloud

Used with stolen credentials

Nov 19 – 22

168.143.104\[.\]44

NTT

Used with stolen credentials

Nov 15 – 23

103.27.80\[.\]145

NTT

Used with stolen credentials

Nov 15 – 23

216.203.20\[.\]186

BL Networks

Used with stolen credentials

Nov 14 – 19

66.179.31\[.\]32

BL Networks

Used with stolen credentials

Nov 14 – 19

8.208.101\[.\]210

Alibaba Cloud

Used with stolen credentials

Sep 30 – Nov 22

8.222.148\[.\]117

Alibaba Cloud

Used with stolen credentials

Sep 30 – Nov 22

47.79.40\[.\]236

Alibaba Cloud

Used with stolen credentials

Sep 30 – Nov 22

47.84.82\[.\]39

Alibaba Cloud

Used with stolen credentials

Sep 30 – Nov 22

47.79.89\[.\]122

Alibaba Cloud

Used with stolen credentials

Sep 30 – Nov 22

58.243.42\[.\]153

China Unicom

Used with stolen credentials

Oct 31 – Nov 6

123.116.51\[.\]114

China Unicom

Used with stolen credentials

Oct 31 – Nov 6

5.181.181\[.\]168

Mynymbox

Used with stolen credentials

Late Oct – Nov 23

37.77.150\[.\]119

Proton66

Used with stolen credentials

Late Oct – Nov 23

45.76.225\[.\]196

Vultr

Used with stolen credentials

Late Oct – Nov 23

72.57.131\[.\]24

—

Used with stolen credentials

Late Oct – Nov 23

149.255.35\[.\]138

Hivelocity

Used with stolen credentials

Late Oct – Nov 23

154.86.0\[.\]28

LightLayer

Used with stolen credentials

Late Oct – Nov 23

157.22.126\[.\]128

Global Transit Systems

Used with stolen credentials

Late Oct – Nov 23

162.251.248\[.\]190

—

Used with stolen credentials

Late Oct – Nov 23

166.0.23\[.\]89

Evoxt

Used with stolen credentials

Late Oct – Nov 23

180.178.51\[.\]150

N963

Used with stolen credentials

Late Oct – Nov 23

187.77.250\[.\]192

Hostinger

Used with stolen credentials

Late Oct – Nov 23

194.59.30\[.\]231

—

Used with stolen credentials

Late Oct – Nov 23

199.19.77\[.\]84

3K33

Used with stolen credentials

Late Oct – Nov 23

45.199.130\[.\]250

Zillion Network

Used with stolen credentials

Late Oct – Nov 23

111.223.247\[.\]165

BGP Network

Used with stolen credentials

Late Oct – Nov 23

45.38.20\[.\]153

Aokigahara

Used with stolen credentials

Late Oct – Nov 23

85.193.69\[.\]250

B2 Net Solutions

Used with stolen credentials

Late Oct – Nov 23

82.29.53\[.\]185

Hosteons

Used with stolen credentials

Late Oct – Nov 23

68.68.250\[.\]114

—

ARTEX operator host

Late Oct – Nov 1

192.238.246\[.\]157

—

ARTEX operator host

Late Oct – Nov 1

104.207.150\[.\]173

Vultr

ARTEX operator host

Late Oct – Nov 1

2.26.225\[.\]135

VPSPay Networks

Stolen credentials + wide probing/spraying (match may be a failed attempt)

Oct 31 – Nov 23

109.238.87\[.\]4

B2 Net Solutions

Stolen credentials + wide probing/spraying (match may be a failed attempt)

Oct 31 – Nov 23

111.223.247\[.\]202

BGP Network

Stolen credentials + wide probing/spraying (match may be a failed attempt)

Oct 31 – Nov 23

130.94.108\[.\]151

LIGHT NODE

Stolen credentials + wide probing/spraying (match may be a failed attempt)

Oct 31 – Nov 23

161.77.116\[.\]139

RingSquared

Stolen credentials + wide probing/spraying (match may be a failed attempt)

Oct 31 – Nov 23

185.87.121\[.\]140

MDN Technology

Stolen credentials + wide probing/spraying (match may be a failed attempt)

Oct 31 – Nov 23

45.199.130\[.\]245

Zillion Network

Stolen credentials + wide probing/spraying (match may be a failed attempt)

Oct 31 – Nov 23

2.26.226\[.\]17

VPSPay Networks

Stolen credentials + wide probing/spraying (match may be a failed attempt)

Oct 31 – Nov 23

2.26.225\[.\]235

VPSPay Networks

Stolen credentials + wide probing/spraying (match may be a failed attempt)

Oct 31 – Nov 23

134.122.173\[.\]60

CTG Server

Stolen credentials + wide probing/spraying (match may be a failed attempt)

Oct 31 – Nov 23

130.94.103\[.\]197

LIGHT NODE

Stolen credentials + wide probing/spraying (match may be a failed attempt)

Oct 31 – Nov 23

76.13.169\[.\]197

Hostinger

Stolen credentials + wide probing/spraying (match may be a failed attempt)

Oct 31 – Nov 23

82.29.131\[.\]60

Hosteons

Stolen credentials + wide probing/spraying (match may be a failed attempt)

Oct 31 – Nov 23

130.94.35\[.\]151

LIGHT NODE

Stolen credentials + wide probing/spraying (match may be a failed attempt)
