# W33 and earlier (dedup targets) — 76 records

## 2026-08-10/bindcloak-rtlqueueworkitem-reflective-loading
date=2026-08-10 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=2026-07-26/teleshim-bindcloak-volume-serial-keying-government-espionage weekly_section=None
TITLE: UPDATE — BINDCLOAK unpacked: a modular C++ backdoor that routes every DLL load through RtlQueueWorkItem to keep LoadLibraryW off unbacked memory, assessed high-confidence an OctLurk variant
HEADLINE: Zscaler's second instalment details the toolkit's final stage and extends the campaign to Middle East energy targets
SUMMARY: Part 2 of Zscaler ThreatLabz's series on the actor behind TELESHIM and MIXEDKEY is a full teardown of BINDCLOAK, a 64-bit modular C++ backdoor whose plugin DLLs are reflectively loaded, with each import resolved by queueing LoadLibraryW through RtlQueueWorkItem specifically because a LoadLibraryW call originating from unbacked executable memory is what endpoint tooling treats as suspicious. It derives a per-victim host identifier from the computer name and volume serial number, encodes command-and-control traffic under two XOR layers over TLS, and exposes eleven commands centred on collecting and impersonating user and process tokens. ThreatLabz assesses with high confidence that BINDCLOAK is a variant of OctLurk, and reports the July 2026 campaign expanding into the Middle East energy sector.
CVES: -
ENTITIES: malware:bindcloak, malware:teleshim, tool:mixedkey, malware:octlurk
PRIMARY: https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-2

## 2026-08-10/coding-agent-ci-harness-trust-boundary-shared-checkout
date=2026-08-10 kind=research horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Coding-agent CI harnesses broke on the same trust boundary three different ways — and the two findings that matter most carry no CVE at all
HEADLINE: A validator that strips quoted text before inspecting it, and an agent instruction file rewritten between two passes of one shared checkout
SUMMARY: Novee Security's Black Hat USA 2026 write-up root-causes trust-boundary failures in AI coding-agent CI harnesses, each tested against the vendor's own public repository in default configuration. Against Claude Code Action it reports three successive rounds of patch-and-bypass, of which only the last — an allowlist entry that pre-approved a bare hostname for the fetch tool — carries CVE-2026-54316; the two more instructive rounds, a command validator that strips single-quoted content before inspecting it and a read-only allowlist exempt from path checking, carry no identifier. A Gemini CLI harness flaw is tracked as CVE-2026-12537. The third finding, an OpenAI Codex workflow whose two agent passes shared one checkout so the first could rewrite the instruction file the second treats as authoritative, has no CVE and was fixed only in the vendor's own repository.
CVES: CVE-2026-54316, CVE-2026-12537
ENTITIES: trend:coding-agent-ci-harness-trust-boundary-2026-08, trend:claude-code-action-github-issue-supply-chain
PRIMARY: https://novee.security/blog/critical-flaws-in-anthropic-google-and-openais-coding-agents/

## 2026-08-10/coding-agent-forensic-artefacts-opencode-codex-credentials
date=2026-08-10 kind=research horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: CERT Intrinsec maps where autonomous coding agents leave evidence on disk — the same session databases and token files an investigator needs are a credential-collection target
HEADLINE: OpenCode and OpenAI Codex write prompt history, per-session logs and plaintext API keys to predictable per-user paths
SUMMARY: CERT Intrinsec has begun a forensic-artefact series for autonomous coding-agent CLIs, covering OpenCode and OpenAI Codex. Both write their state under a per-user directory: OpenCode keeps a SQLite database holding sessions, messages, projects and workspaces, and a separate file holding authentication information including API keys; Codex keeps its authentication material in auth.json and the operator's prompt history in history.jsonl, alongside per-session rollout logs. Read one way this is an incident-response artefact map for a class of tooling that now runs shells on developer and CI endpoints. Read the other way it is an inventory of where an attacker with any foothold on such a host finds cleartext provider credentials and a transcript of the work.
CVES: -
ENTITIES: report:intrinsec-ai-agents-digital-forensics-series
PRIMARY: https://www.intrinsec.com/en/opencode-forensics/

## 2026-08-10/cve-2026-33824-ikeext-double-free-root-cause-published
date=2026-08-10 kind=vulnerability horizon=operational priority=notable deep_dive=False(None) update_of=2026-08-02/unit42-autonomous-campaign-confirmed-impact-was-understated weekly_section=None
TITLE: UPDATE — the root cause of CVE-2026-33824 is published: a pre-authentication double free on the IKEv2 fragment-reassembly path, reachable on UDP 500/4500 against any Windows IKEv2 responder
HEADLINE: One of the four CVEs the autonomous-agent campaign actually reached now has a mechanism, and it runs as Local System
SUMMARY: 0patch published a root-cause analysis on 2026-08-05 placing CVE-2026-33824 in ikeext.dll — the module behind the IKE and AuthIP IPsec Keying Modules service, which runs as Local System — on the IKEv2 fragment-reassembly path, where an unauthenticated attacker who can reach UDP 500/4500 on a host acting as an IKEv2 responder can free the same heap block twice. Microsoft's own record independently corroborates the CVE as a CWE-415 double free, CVSS 9.8, patched 2026-04-14 across Windows Server 2016 through 2025 and Windows 10 1607 through Windows 11 26H1, with exploitation and public disclosure both recorded as no. This closes an evidence gap on tracked ground: the campaign entry that names this CVE described it only as callbacks from three IKE VPN endpoints.
CVES: CVE-2026-33824
ENTITIES: actor:knaithe-knyuan, tool:hermes-ai-agent
PRIMARY: https://0patch.com/blog/micropatches-released-for-windows-ike-service-extensions

## 2026-08-10/cve-2026-66066-rapid7-metasploit-module-weaponisation
date=2026-08-10 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=2026-08-02/cve-2026-66066-rails-attack-chain-public-forensic-tooling weekly_section=None
TITLE: UPDATE — CVE-2026-66066 (Rails Active Storage) now has a public Metasploit module and a validated code-execution path that does not need a Marshal gadget
HEADLINE: Rapid7 reproduced the chain across five Rails lines and shipped it as a module — and states it is not aware of exploitation in the wild
SUMMARY: Rapid7 published a full technical reproduction of the Rails Active Storage arbitrary-file-read chain on 2026-08-03 and released a Metasploit module implementing it. The module creates crafted direct-upload blobs, confirms the file read, recovers and validates Rails signing material, and triggers command or native Ruby payloads. Rapid7 validated the code-execution path against Rails 8.0.5 configured with the JSON message serializer, so it does not depend on a Marshal deserialization gadget. The status change is weaponisation and automation, not attacker activity: Rapid7's own tracker states it is not aware of exploitation in the wild, and neither post claims observed scanning or intrusions.
CVES: CVE-2026-66066
ENTITIES: -
PRIMARY: https://www.rapid7.com/blog/post/ra-kindarails2shell-technical-analysis-cve-2026-66066

## 2026-08-10/esxi-busybox-ash-command-obfuscation-21-techniques
date=2026-08-10 kind=research horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: CrowdStrike catalogues 21 working command-obfuscation techniques inside VMware ESXi's BusyBox ash shell — and shell logs record the command before expansion, so the logged string is not what ran
HEADLINE: ESXi's minimal shell is expressive enough to hide commands, and its logging captures the parsing stage rather than the result
SUMMARY: CrowdStrike systematically tested command obfuscation against a live ESXi host and catalogued 21 working techniques across six classes, validated on ESX 7.0.3 with the VMware-provided BusyBox. The load-bearing finding for defenders is a logging property rather than a vulnerability: ESXi shell logs capture commands during parsing, before expansions occur, so a substitution-based command is recorded in its obfuscated form and any detection keyed on a literal string such as esxcli misses it entirely. The obfuscation capability comes largely from awk rather than the shell itself. ESXi is where ransomware operators go to encrypt an estate at once, which is what makes a blind spot in its command telemetry expensive.
CVES: -
ENTITIES: actor:akira, actor:scattered-spider
PRIMARY: https://www.crowdstrike.com/en-us/blog/crowdstrike-hunts-for-shell-command-obfuscation-vmware-esx/

## 2026-08-10/forescout-rockwell-plc-exposure-census-cellular-carrier-path
date=2026-08-10 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=2026-08-06/water-plc-lockouts-twelve-states-named-utility-confirms weekly_section=None
TITLE: UPDATE — the water-campaign exposure gets counted: 4,407 internet-facing Rockwell controllers, and 19 of the 22 in already-attacked cities sat on the same mobile carrier network
HEADLINE: Forescout puts numbers on the exposed estate, and CISA says the devices it finds have no password or a default one
SUMMARY: Forescout queried Shodan on 2026-08-03 and found 4,407 devices exposing the EtherNet/IP engineering port used by Rockwell Automation controllers, 65% in the United States with Canada and Spain next. Of the 22 it located in cities targeted by the water-utility campaign, 19 were on the same mobile carrier network reached through cellular routers, and 19 of 22 ran firmware susceptible to CVE-2017-16740 — two separate findings that share a number. Forescout cannot confirm any of those assets were compromised and states no CVE is confirmed as exploited in the campaign. CISA's acting director, interviewed at Black Hat, says exposed controllers are being found with no password or a default one, and that the agency is doing nothing on attribution right now.
CVES: -
ENTITIES: incident:minnesota-water-utilities-coordinated-cyberattack-2026-07
PRIMARY: https://www.forescout.com/blog/ot-security-analysis-exposed-devices-attacked-in-us-water-systems/

## 2026-08-10/freebsd-ctl-ha-three-preauth-kernel-rce-primitives-port-999
date=2026-08-10 kind=vulnerability horizon=operational priority=high deep_dive=True(network-stack-rce) update_of=None weekly_section=None
TITLE: FreeBSD CTL HA — three independent pre-authentication remote kernel-code-execution primitives behind an unauthenticated failover port, and the project's answer is a manpage warning rather than a patch
HEADLINE: FreeBSD's storage-failover interconnect trusts whatever connects to TCP/999, and three published primitives each reach root from the wire
SUMMARY: FreeBSD's CAM Target Layer runs its High-Availability failover protocol on TCP/999 with no authentication of any kind — the kernel trusts whatever connects as its peer controller. Researcher Calif published three independent primitives behind that port, each sufficient on its own for a root shell from network access alone: an unchecked kernel-pointer dereference giving arbitrary read/write off the wire, a second wire-pointer abuse that repoints a handler function pointer, and a heap overflow in the scatter-gather copy loop. FreeBSD declined a code fix, adding a manpage warning instead on the grounds that the interconnect was never meant to be reachable from an untrusted network. No CVE has been assigned, working exploits are public, and the feature ships enabled by product design on TrueNAS Enterprise HA clusters.
CVES: -
ENTITIES: -
PRIMARY: https://blog.calif.io/p/the-taking-of-freebsd-one-two-three

## 2026-08-10/interlock-volatility3-winpmem-credential-theft
date=2026-08-10 kind=threat horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: Interlock ran Volatility3 and WinPmem against a live endpoint to harvest credentials — the responder's own memory-forensics toolkit used in place of a commodity dumper
HEADLINE: A ransomware operator acquired a memory image and ran hashdump and cachedump offline against it, leaving traces that look like an IR engagement
SUMMARY: Sophos's incident-response team investigated a March 2026 Interlock intrusion in which the operator captured a full physical-memory image with WinPmem and then ran Volatility3's Windows credential plugins offline against that image, instead of using a commodity credential dumper on the live host. Initial access was a ClickFix paste-and-run lure reached through a search result, and the chain ran to domain-controller compromise inside roughly 26 hours including a deliberate day-long pause. The defensive problem is that both binaries are legitimate DFIR tooling, so their presence and their command shapes are indistinguishable from a real investigation on artifact alone — Sophos's own discriminator was that the customer knew of no legitimate use.
CVES: -
ENTITIES: actor:interlock, malware:nodesnake
PRIMARY: https://www.sophos.com/en-us/blog/2608-volatility-interlock/

## 2026-08-10/linux-bridge-stp-timer-uaf-no-cve-public-exploit
date=2026-08-10 kind=vulnerability horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Linux kernel bridge STP timer use-after-free — a control-flow hijack primitive with a published exploit, no CVE, and no confirmed stable backport
HEADLINE: Arming a bridge's STP timers without an interface-up guard yields a freed-object reclaim, reachable only with bridge-management privilege
SUMMARY: SSD Secure Disclosure published a use-after-free in the Linux kernel's software bridge STP implementation, submitted by two researchers during TyphoonPWN 2026. A bridge that is administratively down while kernel STP is enabled, with a port driven into the LEARNING state, arms periodic timers without an interface-up guard; the timer object is embedded in structures freed with the bridge, so reclaiming the slot with attacker-controlled data yields a control-flow hijack primitive. The precondition is bridge-management privilege — not network-reachable and not available to a plain unprivileged process — a precondition this entry assesses rather than quotes, since neither source states it. No CVE was assigned, a compilable exploit is published inline, the mainline fix landed 2026-06-30, and backport status beyond mainline is unconfirmed.
CVES: -
ENTITIES: -
PRIMARY: https://ssd-disclosure.com/linux-bridge-stp-timer-use-after-free/

## 2026-08-10/natjack-nat-trust-assumption-attack-class-two-cves
date=2026-08-10 kind=research horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: NatJack — sharing a NAT table is a trust relationship nobody declared: five named primitives against NAT state, of which only the downstream TCP hijack got a CVE on each platform
HEADLINE: Every evaluated NAT implementation fell to at least one primitive, and the Linux change is explicitly a partial mitigation rather than a fix
SUMMARY: NatJack, presented at Black Hat USA 2026, is an attack class against an unstated assumption in network address translation — that devices sharing a NAT table can trust one another. The research names five primitives: TCP session hijack by downstream spoofing, the same hijack coordinated with an upstream attacker-controlled server, DNS response hijack, disclosure of a victim's externally mapped address and port, and NAT-table exhaustion. Two CVEs were assigned and both name the downstream-spoofing hijack specifically — CVE-2026-56181 in Windows NAT affecting Hyper-V, and CVE-2026-63913 in the Linux netfilter connection-tracking state machine. The researcher records the Linux change as "not a complete fix" that increases attack complexity, and the other three primitives carry no identifier and no vendor fix at all.
CVES: CVE-2026-56181, CVE-2026-63913
ENTITIES: trend:natjack-nat-trust-assumption-attack-class
PRIMARY: https://natjack.io/

## 2026-08-10/pam-rootok-identity-shuffle-as-anti-forensics-xmrig
date=2026-08-10 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: An intruder used pam_rootok to move between low-privileged identities as a deliberate forensic smokescreen — inverting what a responder infers from the authentication trail
HEADLINE: Root escalated once, then spent the intrusion impersonating ordinary users so the audit trail would look ordinary
SUMMARY: Group-IB's DFIR team documents a May 2026 covert Monero-mining intrusion whose defining feature is anti-forensics rather than the miner. Initial access came through a trusted third-party relationship. After escalating to root the actor abused the pam_rootok policy — which lets root use su without a password — to assume the identities of multiple low-privileged users, deliberately avoiding the root-level activity that raises SOC alerts, and planted redundant cron persistence across those unmonitored accounts so remediating the root compromise alone would let the implant regenerate. Core logging services were stopped and authentication logs tampered with, and the binary self-deletes after establishing a mutex, continuing to run from memory.
CVES: -
ENTITIES: campaign:groupib-xmrig-pam-forensic-smokescreen
PRIMARY: https://www.group-ib.com/blog/xmrig-covert-linux-pam-abuse/

## 2026-08-10/retelit-qilin-italian-telco-cloud-operator-public-sector
date=2026-08-10 kind=incident horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: Qilin compromised Italian telecommunications and cloud operator Retelit on 8 June — the company confirmed it only after an investigation forced the question, and one of the three affected data centres was its certified backup site
HEADLINE: A European carrier serving 193 public administrations disclosed a two-month-old Qilin intrusion in a right-of-reply, not a press release
SUMMARY: IrpiMedia reported on 2026-08-04 that Retelit, one of Italy's largest business telecommunications and cloud operators, had been compromised in an extortion attack claimed by Qilin, with roughly 270,000 files listed on the leak site and an estimated 300 GB published across two dumps. Retelit made no announcement through its own channels; after the article ran it sent the outlet a right-of-reply confirming an 8 June 2026 attack attributed to Qilin, notified to Italy's national cybersecurity agency, CSIRT-ITA, the postal police and the data-protection authority, and scoping the damage to virtualisation infrastructure in 3 of its 38 national data centres, around 7% of distributed systems. IrpiMedia names those three as Verona, Rome and Milan — Milan being the site certified for Retelit's own backup and service continuity — and reports customers complaining of backup-recovery failure.
CVES: -
ENTITIES: actor:qilin, incident:retelit-qilin-2026
PRIMARY: https://irpimedia.irpi.eu/retelit-operatore-cloud-e-telecomunicazioni-attacco-informatico/

## 2026-08-10/unc5537-moucka-guilty-plea-saas-tenant-extortion-template
date=2026-08-10 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Connor Moucka pleads guilty over the 2024 SaaS-tenant mass-extortion campaign — 165+ victim organisations reached with stolen credentials and no vulnerability in the platform
HEADLINE: Law-enforcement closure on the campaign that set the template for cloud-tenant compromise, with the access path entirely credential-based
SUMMARY: Connor Riley Moucka pleaded guilty on 2026-08-05 to four federal counts over a February–October 2024 hacking and extortion campaign that the U.S. Department of Justice says compromised over 165 victim organisations, stole billions of customer records and produced over $2.5 million in ransom payments, with victim losses above $9.5 million affecting at least 100 million individuals. DOJ describes the target only as a U.S.-based software-as-a-service company and names no provider; the identification of the platform, the absence of enforced multi-factor authentication on the targeted tenants, and Moucka's aliases all come from KrebsOnSecurity rather than from the DOJ release. Sentencing is set for 2026-10-27.
CVES: -
ENTITIES: actor:unc5537, actor:cameron-wagenius
PRIMARY: https://www.justice.gov/opa/pr/canadian-man-pleads-guilty-hacking-us-cloud-storage-provider-and-extorting-its-customers

## 2026-08-10/wazuh-4-14-6-cluster-root-rce-preauth-authd-overflow
date=2026-08-10 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: Wazuh 4.14.6 — two cluster-protocol paths to root that bypass the CVE-2026-25770 fix, a DAPI deserialization RCE, and a pre-auth stack overflow on the enrollment port
HEADLINE: Wazuh patches root-RCE chains in the cluster protocol and a pre-auth overflow reachable on TCP/1515 under stock defaults
SUMMARY: Wazuh 4.14.6 fixes a ten-CVE cluster disclosed as individual GitHub Security Advisories and independently cross-listed by BSI. Two critical flaws (CVE-2026-49441, CVE-2026-48024) let a cluster peer holding the shared Fernet key overwrite arbitrary files on the master — including ossec.conf, reaching root — through two sibling code paths that both defeat the _ALLOWED_PREFIXES hardening added for CVE-2026-25770; CVE-2026-44901 reaches root code execution when a REST request fans out across two or more nodes; and CVE-2026-45798 is a pre-authentication stack overflow in wazuh-authd on TCP/1515, reachable with no credential under the shipped anonymous-SSL default. Affected ranges differ per flaw — from 4.0.0, 4.3.0 or 4.5.0 respectively through 4.14.5 — and all are fixed in 4.14.6, with no exploitation reported.
CVES: CVE-2026-49441, CVE-2026-48024, CVE-2026-44901, CVE-2026-45798
ENTITIES: -
PRIMARY: https://github.com/wazuh/wazuh/security/advisories/GHSA-3v57-hgvj-3vj2

## 2026-08-10/wordpress-core-xss2shell-cve-2026-64638-preauth-xss-to-rce
date=2026-08-10 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-64638 (XSS2Shell) — WordPress Core: a sanitiser disagreement on the login screen chains through DOM clobbering and a JSONP callback into administrator-minted Application Passwords and plugin upload
HEADLINE: WordPress patches a pre-auth login-screen XSS that chains to code execution, same-day in 7.0.3 with backports to 4.7.34
SUMMARY: CVE-2026-64638 is a pre-authentication reflected XSS on the WordPress login screen, disclosed by pwn.ai and patched the same day in WordPress 7.0.3 with backports across every maintained branch down to 4.7.34. wp_strip_all_tags() and the later wp_kses_post() tokenizer disagree about whether whitespace after an angle bracket starts a tag, so attacker-specified DOM nodes reach a page the first function already certified as inert; DOM clobbering plus a JSONP callback then drive a logged-in administrator's own browser into approving an Application Password, which uploads a plugin whose PHP is web-accessible without activation. Escalation needs one social-engineered click by an administrator; the XSS itself needs no authentication. No exploitation reported, and this is a distinct chain from the actively exploited WP2Shell.
CVES: CVE-2026-64638
ENTITIES: -
PRIMARY: https://wordpress.org/news/2026/08/wordpress-7-0-3-release/

## 2026-08-10/wp2root-php-uaf-copy-fail-kev-kernel-lpe-to-native-root
date=2026-08-10 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=2026-08-08/ncsc-ch-clickfix-wp2shell-etherhiding-vidar-swiss-websites weekly_section=None
TITLE: UPDATE — wp2root turns the WP2Shell foothold into fileless native root using a PHP unserialize use-after-free and the KEV-listed 'Copy Fail' kernel bug, defeating disable_functions and on-disk integrity monitoring
HEADLINE: The WordPress chain this pipeline tracks as exploited against Swiss sites now has a published route from sandboxed PHP to root
SUMMARY: Calif published wp2root on 2026-08-05, a post-exploitation chain that starts where the WP2Shell pre-auth WordPress RCE ends — sandboxed PHP execution — and reaches fileless native root even where disable_functions blocks system() and the filesystem is read-only. A use-after-free in PHP's legacy Serializable path yields native code execution that calls PHP's own system handler directly, bypassing disable_functions because that setting removes only the PHP-level name. The root step is CVE-2026-31431 ("Copy Fail"), a Linux kernel flaw that overwrites the page-cache copy of a setuid-root binary without touching the file on disk — and which has been CISA KEV-listed for confirmed exploitation since 2026-05-01, independent of this research.
CVES: CVE-2026-31431
ENTITIES: -
PRIMARY: https://blog.calif.io/p/the-wordpress-chain-massacre

## 2026-08-10/zabka-supplier-account-jira-access-confirmed
date=2026-08-10 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Żabka confirms an external service-provider account reached its ticketing system — the claimed pivot from Jira into source control and production is the seller's assertion, not the company's
HEADLINE: A supplier account reached Jira at a Polish convenience-store chain; the interesting part of the story is the part nobody has confirmed
SUMMARY: Żabka, a Polish convenience-store franchise chain, confirmed in a written statement to Polish outlets that it detected unauthorized access to technical resources supporting franchisor-franchisee information exchange, that the access came through an external service provider's account, that it was blocked immediately, and that to its current knowledge the perpetrator reached the ticketing system. It states transaction data, consumer services and loyalty app data are unaffected, and has notified its data-protection officer, the Polish regulator and law enforcement. A criminal-forum seller separately claims a far larger scope reaching source control and production infrastructure — a claim the reporting outlet explicitly frames as the attacker's own, with its proposed mechanism labelled a guess.
CVES: -
ENTITIES: incident:zabka-supplier-account-jira-gitlab-secrets-2026-07
PRIMARY: https://niebezpiecznik.pl/post/zabka-zhackowana-co-wycieklo/

## 2026-08-11/belgian-eid-connective-extension-pin-recovery-driveby-rce
date=2026-08-11 kind=research horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Belgium's eID signing extension handed any web page the card, the PIN and a drive-by RCE — an eIDAS Qualified Trust Service Provider's browser bridge that never checked the caller's origin
HEADLINE: An eIDAS-qualified eID browser bridge let any website read the card, recover the PIN and load an arbitrary DLL
SUMMARY: Bay Area Labs disclosed three chained flaws in Connective, the browser extension and native host from Nitro Software Belgium that lets web pages talk to Belgian eID and Maestro smart cards for authentication and eIDAS qualified signatures, and which the researchers say is used by 8 of Belgium's 10 largest banks and 60+ government agencies across a 2-million-user install base. Because the extension never forwarded the calling page's origin to the native host, any site or hidden iframe could replay a signed activation token and drive the card; the PIN token handed back to the page carried both the ciphertext and its own AES key with a hardcoded IV, so the eID PIN could be recovered outright; and a reader-enumeration command accepted a relative library path, turning a single site visit into arbitrary DLL execution. No CVE has been assigned, and the vendor took 146 days from first report to complete fix, shipping an incomplete one in between.
CVES: -
ENTITIES: -
PRIMARY: https://amibeingpwned.com/blog/8-in-10-banks-in-belgium

## 2026-08-11/ceva-logistics-fulfilment-breach-ten-controllers-notified
date=2026-08-11 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: One compromised contract-logistics processor put ten organisations into breach notification at once — CEVA Logistics, eight European warehouses, and a bank, a retailer and a games platform all learning from their supplier
HEADLINE: Ten organisations filed Dutch breach reports over one logistics provider's order-processing intrusion
SUMMARY: CEVA Logistics, the contract-logistics arm of CMA CGM, told affected customers on 1 August 2026 that a cyber intrusion was affecting part of its European contract-logistics operations, scoping the operational impact to eight warehouses. Because CEVA processes fulfilment data on behalf of unrelated clients, the Dutch data-protection authority has received breach reports from ten organisations over this one incident. Named downstream parties whose customers' shipping data was affected include ING, bol.com, De Bijenkorf, AFC Ajax, Ace & Tate and Valve, whose Steam hardware buyers had shipping records held by CEVA for 90 days. bol.com states two order-processing systems at one fulfilment centre were involved and that customer data may have been viewed or copied; no source names an initial-access vector, a malware family or an actor, CEVA has published no statement of its own, and its spokesperson declined to say whether any ransom demand was received.
CVES: -
ENTITIES: incident:ceva-logistics-fulfilment-breach-2026-08
PRIMARY: https://partnerplatform.bol.com/en/nadp/security-incident-logistics-partner-of-bol

## 2026-08-11/cve-2026-65400-screensharingd-remote-root-two-preauth-bugs
date=2026-08-11 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=2026-08-08/cve-2026-65400-macos-screen-sharing-auth-state-bypass weekly_section=None
TITLE: UPDATE — CVE-2026-65400 is remote root, not just an auth bypass: two independent pre-auth bugs sat in screensharingd, working exploits were rebuilt from the patch in four hours, and the two research accounts disagree on which mechanism the CVE names
HEADLINE: macOS Screen Sharing: pre-auth remote root confirmed, exploits rebuilt from the patch in hours, ~40,000 hosts exposed
SUMMARY: Update to this pipeline's 2026-08-08 entry, which carried only Apple's advisory line that an attacker on the network might authenticate to Screen Sharing without valid credentials. Three deltas change the urgency. The daemon that answers those connections runs as root, so this is a pre-authentication remote root primitive rather than a login as one user; researchers rebuilt working exploits from the 26.6.1 binary diff in about four hours, and did the same for a second, independent pre-auth bug in the same source file that Apple closed silently on 2026-07-27 with no CVE; and a researcher scan cited by Calif found roughly 40,000 Macs with Screen Sharing reachable from the internet, and Huntress separately counts tens of thousands of potentially vulnerable hosted bare-metal Macs, noting that some of those providers had not yet folded the fix into their base provisioning images. Calif and Huntress give incompatible root causes for CVE-2026-65400 itself and this entry reports both. Patch to macOS 26.6.1, 15.7.9 or 14.8.9; removing allowed accounts or the VNC password does not help.
CVES: CVE-2026-65400
ENTITIES: -
PRIMARY: https://blog.calif.io/p/no-country-for-old-passwords

## 2026-08-11/gunra-raas-fortios-mfa-backdoor-linux-prng-recoverable
date=2026-08-11 kind=threat horizon=operational priority=high deep_dive=True(ransomware-affiliate) update_of=None weekly_section=None
TITLE: Gunra ransomware-as-a-service: a joint six-agency advisory documents FortiOS edge exploitation, a persistent MFA backdoor built from one fixed OTP value, and a Linux encryptor whose keys can be reconstructed
HEADLINE: Six agencies publish the Gunra RaaS playbook — edge exploitation, an OTP-value MFA backdoor, and a recoverable Linux key
SUMMARY: The FBI, CISA, DC3, NSA, the US Secret Service and South Korea's National Police Agency published joint advisory AA26-222A on 2026-08-10 on Gunra, a Conti-derived double-extortion ransomware-as-a-service that opened an affiliate programme in January 2026 and lists victims across Europe, the Americas, the Middle East, Africa and Asia-Pacific in government services, utilities, healthcare, financial services, transport and critical manufacturing. Initial access is exploitation of the known FortiOS and FortiProxy authentication-bypass flaws CVE-2024-55591 and CVE-2025-24472 on internet-facing firewall and VPN appliances, after which the actors abuse scheduled tasks to create a persistent super-user account, and — in one case — edited the authentication-processing files on a victim's VDI authentication portal so that one attacker-chosen one-time-password value always validated, giving a durable MFA bypass that survives password resets. The advisory also records a defender-usable weakness: the Linux encryptor seeds its key generator with the system clock, so responders may reconstruct keys from file timestamps and recover data without paying.
CVES: CVE-2024-55591, CVE-2025-24472
ENTITIES: actor:gunra
PRIMARY: https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a

## 2026-08-12/cve-2026-20349-cisco-asa-ftd-ssl-vpn-dos-exploited
date=2026-08-12 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-20349 — Cisco Secure Firewall ASA/FTD: one crafted HTTP request to the Remote Access SSL VPN reloads the device, exploitation confirmed, no workaround and a three-day KEV deadline
HEADLINE: Cisco confirms active exploitation of an unauthenticated ASA/FTD VPN denial-of-service flaw with hot fixes as the only control
SUMMARY: Cisco disclosed CVE-2026-20349 on 2026-08-11 and states its PSIRT became aware of active exploitation in August 2026. Insufficient error checking when the Remote Access SSL VPN service parses HTTP requests lets an unauthenticated remote attacker send one crafted request and force the device to reload. Any ASA or FTD device with SSL listen sockets enabled is affected — IKEv2 remote access with client services, SSL VPN, or Zero Trust Network Access — across ASA 9.16 to 9.24 and FTD 7.0 to 10.0; Secure Firewall Management Center is not affected. There are no workarounds, only hot fixes, and CISA added the CVE to its KEV catalog the same day with a 14 August deadline.
CVES: CVE-2026-20349
ENTITIES: -
PRIMARY: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-dzv4mQFF

## 2026-08-12/cve-2026-62832-legacyhive-user-profile-service-patched
date=2026-08-12 kind=vulnerability horizon=operational priority=notable deep_dive=False(None) update_of=2026-07-29/legacyhive-offline-registry-hive-profile-hijack-no-fix weekly_section=None
TITLE: UPDATE — the LegacyHive profile-hijack technique reported here as having no Microsoft fix now has one: CVE-2026-62832, patched 11 August, publicly disclosed and rated 'Exploitation More Likely'
HEADLINE: August Patch Tuesday closes the Windows User Profile Service flaw Rapid7 assesses is the one behind LegacyHive
SUMMARY: The LegacyHive proof-of-concept covered here on 2026-07-29, reproduced on fully patched Windows and described at the time as having no Microsoft mitigation, appears to be fixed. Microsoft's August Patch Tuesday shipped CVE-2026-62832, an improper-link-resolution elevation-of-privilege flaw in the Windows User Profile Service rated CVSS 7.8, publicly disclosed before the patch and assessed "Exploitation More Likely". Rapid7 assesses the advisory is a solid match for the researcher's description of LegacyHive; Microsoft's record does not name the technique, so the identification is Rapid7's judgement rather than a vendor confirmation.
CVES: CVE-2026-62832
ENTITIES: actor:nightmare-eclipse, trend:nightmare-eclipse-legacyhive-profile-registry-hijack-2026-07
PRIMARY: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62832

## 2026-08-12/cve-2026-72898-metabase-sqli-cve-assigned-kev
date=2026-08-12 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally weekly_section=None
TITLE: UPDATE — the exploited Metabase zero-day now has an identifier: CVE-2026-72898 at CVSS 10.0, on CISA KEV since 11 August, with the affected ranges published per release line
HEADLINE: The Metabase SQL-injection flaw that no CVE-driven process could see is now a catalogued, KEV-listed CVE with precise version boundaries
SUMMARY: Metabase's unauthenticated SQL-injection zero-day, covered here on 2026-08-09 when no CVE existed, has been assigned CVE-2026-72898 in GitHub Security Advisory GHSA-vwf4-m7j8-wcjf at CVSS 3.1 10.0, and CISA added it to the Known Exploited Vulnerabilities catalog on 2026-08-11. The advisory publishes affected ranges per release line and confirms active exploitation in Metabase's own words. For self-hosted instances nothing about the exposure changed — but the flaw is now visible to every scanner, SBOM pipeline and CVE-keyed patch process that could not see it a week ago.
CVES: CVE-2026-72898
ENTITIES: incident:metabase-sqli-zeroday-2026-08
PRIMARY: https://github.com/metabase/metabase/security/advisories/GHSA-vwf4-m7j8-wcjf

## 2026-08-12/lazarus-operation-dream-job-cve-2026-68820-afd-fudmodule
date=2026-08-12 kind=threat horizon=operational priority=high deep_dive=True(apt-campaign) update_of=None weekly_section=None
TITLE: Lazarus burned a Windows AFD.sys zero-day (CVE-2026-68820) on European defence targets — FudModule v3.1 blinds the endpoint, and the C2 is other people's Roundcube and WordPress servers
HEADLINE: Check Point ties Operation Dream Job's 2026 wave to an exploited kernel zero-day patched on 11 August, with confirmed compromises in France and Germany
SUMMARY: Check Point Research published the analysis behind CVE-2026-68820 on 2026-08-11, the sole exploitation-detected flaw in Microsoft's August Patch Tuesday: a use-after-free race in the Windows Ancillary Function Driver for WinSock that a DPRK-linked Lazarus intrusion used to reach SYSTEM and load the FudModule v3.1 kernel rootkit. The delivery is a fake defence-sector job offer leading to a trojanised PDF viewer or a DLL-sideloading bundle; the command-and-control runs on compromised Roundcube and WordPress servers, one of them a French victim organisation later reused to phish others. Check Point records successful targeting in France and Germany, and CISA added the CVE to its Known Exploited Vulnerabilities catalog the same day.
CVES: CVE-2026-68820, CVE-2025-49113
ENTITIES: actor:lazarus-group, campaign:operation-dream-job, tool:fudmodule, malware:mistpen, malware:foresttiger, malware:troy-backdoor, tool:relayshell
PRIMARY: https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/

## 2026-08-12/n-able-n-central-storm-1175-stormencryptor
date=2026-08-12 kind=threat horizon=operational priority=high deep_dive=False(None) update_of=2026-08-09/n-able-n-central-hotfix-2-required-supersedes-hotfix-1 weekly_section=None
TITLE: UPDATE — the N-central exploitation has an actor and a payload: Microsoft assesses Storm-1175 is behind it, deploying a new ransomware strain called StormEncryptor from the day the flaw was disclosed
HEADLINE: The RMM auth-bypass chain tracked here since 3 August is now attributed to a China-linked ransomware actor with a new encryptor
SUMMARY: Microsoft Threat Intelligence reported over the weekend of 2026-08-08/09 that Storm-1175 — a financially motivated, China-linked actor previously known for high-velocity Medusa ransomware campaigns — began deploying a previously undocumented strain, StormEncryptor, on 2 August, and is likely exploiting CVE-2026-18577 in N-able N-central to do it. Microsoft has not formally confirmed the access vector; what it notes is that the deployments began the same day the flaw was disclosed. Huntress found more than half of reachable cloud-hosted N-central servers across its partner base still unpatched, and 28.6% of self-hosted instances.
CVES: CVE-2026-18577
ENTITIES: actor:storm-1175, malware:stormencryptor
PRIMARY: https://therecord.media/china-hackers-ransomware-microsoft

## 2026-08-12/project-cav3rn-google-apps-script-c2-relay
date=2026-08-12 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=2026-07-22/cavern-cav3rn-oilrig-attribution-dns-aaaa-c2-fallback weekly_section=None
TITLE: UPDATE — Project CAV3RN now decides per transaction whether to talk directly or relay through Google Apps Script, and a DNS answer's fourth octet is what makes the choice
HEADLINE: Kaspersky documents a C2 module that queries DNS before every transaction to pick its channel, and a broker DLL that hot-loads components every second
SUMMARY: Kaspersky GReAT published a further instalment on Project CAV3RN, the modular espionage framework it tracks against targets in Israel, on 2026-08-11. The new component is a .NET NativeAOT communication module that performs a DNS A-record lookup before every poll or result submission and reads the fourth octet of the answer to choose between direct HTTPS and a Google Apps Script relay, with the same DNS infrastructure able to hand back a replacement Apps Script deployment ID so the operator can rotate the Google channel without redeploying. A second new component, a broker DLL masquerading as the RNP OpenPGP library, rescans its directory every second and hot-loads higher-versioned components.
CVES: -
ENTITIES: tool:cavern-c2-framework
PRIMARY: https://securelist.com/project-cav3rn-continues/120991/

## 2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce
date=2026-08-12 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-58231 — SAP Commerce Cloud: an unauthenticated request to the Data Hub Adapter import endpoint reaches arbitrary code execution (CVSS 10.0), and the fix needs a rebuild and redeploy
HEADLINE: SAP's August patch day is led by a CVSS 10.0 pre-auth code-execution flaw in the Commerce Cloud Data Hub Adapter, fixed only by a rebuild and redeploy
SUMMARY: SAP's 2026-08-11 Security Patch Day fixes CVE-2026-58231, an improper-authorization flaw in the SAP Commerce Cloud Data Hub Adapter that Onapsis describes as insufficient authorization checks and input validation reachable without authentication, rated CVSS 10.0 and capable of arbitrary code execution. Further notes cover code injection in SAP Manufacturing Integration and Intelligence (CVE-2026-44772, 9.9; CVE-2026-44758, 9.1) and an unauthenticated memory-corruption flaw in the NetWeaver AS ABAP kernel's DIAG protocol parser (CVE-2026-34265, 9.8). No exploitation is reported by any party; Commerce Cloud fixes require rebuilding and redeploying the release rather than installing a patch, and an IP filter set is the vendor-side interim control.
CVES: CVE-2026-58231, CVE-2026-44772, CVE-2026-44758, CVE-2026-34265, CVE-2026-58243, CVE-2026-42945
ENTITIES: -
PRIMARY: https://support.sap.com/en/my-support/knowledge-base/security-notes-news/august-2026.html

## 2026-08-12/sharepoint-cve-2026-63520-55040-unauth-rce-chain-poc
date=2026-08-12 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=2026-07-15/microsoft-july-patch-tuesday-sharepoint-dynamics-followup weekly_section=None
TITLE: UPDATE — the half-patched SharePoint chain this pipeline flagged in July is now complete and public: CVE-2026-63520 ships, and Rapid7 releases the analysis and proof-of-concept for CVE-2026-55040
HEADLINE: The SharePoint Pwn2Own chain tracked as half-patched until August is now fully disclosed, with working proof-of-concept code for the auth-bypass link
SUMMARY: The SharePoint chain covered here on 2026-07-15 and flagged in the W29 outlook as half-patched until August is now complete on both halves. Microsoft's August Patch Tuesday published CVE-2026-63520, a remote code execution flaw Rapid7 states is the second of a pair that chain into a critical unauthenticated remote code execution against a vulnerable SharePoint server, and Rapid7 released a detailed technical analysis and a proof-of-concept for the first link, CVE-2026-55040, the CVSS 9.1 weak-authentication bypass Microsoft patched on 14 July. Patches exist for SharePoint Server Subscription Edition, 2019 and 2016; Microsoft records neither flaw as exploited, and rates both "Exploitation More Likely".
CVES: CVE-2026-63520, CVE-2026-55040
ENTITIES: -
PRIMARY: https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026/

## 2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix
date=2026-08-12 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: ShieldBreak — a public proof-of-concept defeats Microsoft's July fix for the RoguePlanet Defender flaw, claims 100% reliability where the original was a coin flip, and now covers Windows Server 2025
HEADLINE: Nightmare Eclipse drops a Defender privilege-escalation patch bypass on Patch Tuesday itself, with no fix available
SUMMARY: Researcher Nightmare Eclipse published ShieldBreak on 2026-08-11/12, a proof-of-concept the researcher describes as a full bypass of the patch Microsoft shipped in July for RoguePlanet (CVE-2026-50656), the Microsoft Malware Protection Engine privilege-escalation flaw that yields a SYSTEM shell on fully updated Windows. Two properties make it worse than what it replaces: it is listed with a 100 percent success rate where RoguePlanet was an unreliable race, and it is listed as tested on Windows Server 2025 alongside Windows 11 25H2, where the June exploit did not run. No patch exists, no vendor has publicly reproduced it, and Microsoft had not commented at publication.
CVES: CVE-2026-50656
ENTITIES: actor:nightmare-eclipse, trend:shieldbreak-defender-rogueplanet-patch-bypass-2026-08, trend:nightmare-eclipse-rogueplanet-defender-toctou-lpe-2026-06
PRIMARY: https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html

## 2026-08-12/stiftung-brandenburgische-gedenkstaetten-ransomware
date=2026-08-12 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: A German federal- and state-funded memorial foundation is rebuilding its entire IT from scratch after ransomware — all seven sites offline, data assumed exfiltrated, no actor named
HEADLINE: Stiftung Brandenburgische Gedenkstätten confirms encryption across every site and chooses full reconstruction over restoring from backup
SUMMARY: The Stiftung Brandenburgische Gedenkstätten, the German public-law foundation operating seven memorial sites including Sachsenhausen and Ravensbrück, disclosed on 2026-08-11 that ransomware detected on 5 August encrypted parts of its IT systems and data, and that it must currently assume attackers downloaded data first. All seven locations and the central office are affected. The foundation cut all internet and network connections and is rebuilding its IT from scratch rather than restoring from backups, working with a BSI-recommended incident-response provider. No actor, ransomware family, leak-site listing or initial-access vector has been disclosed by any party.
CVES: -
ENTITIES: incident:stiftung-brandenburgische-gedenkstaetten-ransomware-2026-08
PRIMARY: https://www.stiftung-bg.de/presse/presseinformationen/42-26-die-stiftung-wurde-opfer-eines-ransomware-angriffs/

## 2026-08-12/wesco-exfilsquad-crm-confirmation-dispute
date=2026-08-12 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=2026-07-31/exfilsquad-uk-department-for-education-pnld-breach weekly_section=None
TITLE: UPDATE — a private-sector ExfilSquad victim confirms a CRM data-exfiltration claim while disputing its severity, after the group published the data it says it took
HEADLINE: Wesco concedes a CRM incident but says no ransomware and no sensitive data at risk, after its ransom deadline expired and the data was published
SUMMARY: Wesco International confirmed to BleepingComputer on 2026-08-11 that it is investigating a claim of CRM data exfiltration by a third party after ExfilSquad — the extortion brand behind the confirmed July breaches of the UK Department for Education's portals and the Police National Legal Database — claimed 2.6 million records from its cloud CRM and, once its ransom deadline expired, published the data it says it took. Wesco found no evidence of ransomware or other malicious software and does not believe sensitive data is at risk, offering no figure of its own. Researchers have tied the group's past activity to improperly configured Microsoft Power Pages data tables; Wesco has not said how it was breached, and the only public link to Dynamics 365 is that Wesco may be using it.
CVES: -
ENTITIES: actor:exfilsquad, incident:uk-dfe-exfilsquad-breach-2026-07
PRIMARY: https://www.bleepingcomputer.com/news/security/wesco-confirms-security-incident-after-exfilsquad-claims-data-theft/

## 2026-08-13/clop-leak-site-names-44-victims-swiss-dutch-listings
date=2026-08-13 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=2026-07-27/clop-windchill-flexplm-mass-extortion-wave-cve-2026-12569 weekly_section=None
TITLE: UPDATE — Cl0p named 44 victims on its leak site in a single batch, including a Swiss and a Dutch organisation, and one vendor assesses an earlier masked batch as possibly the Windchill campaign
HEADLINE: Cl0p's leak site went from masked entries to named European victims in one batch, with no stated intrusion route
SUMMARY: A leak-site tracker first recorded 44 named Cl0p victim listings on 2026-08-12, among them a Swiss and a Dutch organisation, alongside others in Finland, the United Kingdom, Italy, Slovakia, Hungary and France. Separately, Foresiet reviewed an earlier batch of 42 masked Cl0p listings on 2026-08-10 whose advertised data categories — project repositories, CAD files, engineering drawings and product-lifecycle content — led it to assess a possible relationship with the group's PTC Windchill and FlexPLM campaign (CVE-2026-12569), while stating that leak-site information alone cannot establish the access route for any listed organisation. No named victim has confirmed a compromise, and no source links the named batch to the campaign.
CVES: CVE-2026-12569
ENTITIES: actor:clop, campaign:clop-windchill-flexplm-extortion-2026
PRIMARY: https://api.ransomware.live/v2/recentvictims

## 2026-08-13/cve-2026-45659-sharepoint-kev-ransomware-use-flagged
date=2026-08-13 kind=vulnerability horizon=operational priority=notable deep_dive=False(None) update_of=2026-07-02/cve-2026-45659-microsoft-sharepoint-server-authenticated-des weekly_section=None
TITLE: UPDATE — CISA now records the already-exploited SharePoint deserialization flaw CVE-2026-45659 as used in ransomware campaigns, changing what an unpatched farm risks
HEADLINE: A SharePoint remote-code-execution flaw exploited since July is now flagged for known ransomware campaign use in the federal catalogue
SUMMARY: CVE-2026-45659, the Site-Member-authenticated deserialization remote-code-execution flaw in Microsoft SharePoint Server that CISA added to its Known Exploited Vulnerabilities catalog on 2026-07-01 and that this pipeline covered the following day, now carries "Known" in the catalogue's ransomware-campaign-use field, checked against catalog version 2026.08.11. The exploitation itself is not new; what changed is who is using it and to what end. For an on-premises SharePoint estate the expected outcome shifts from data access to encryption and extortion, which changes recovery planning rather than patch priority — the May 2026 fix has been available for nearly three months.
CVES: CVE-2026-45659
ENTITIES: -
PRIMARY: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json

## 2026-08-13/cve-2026-58115-simatic-iot2050-node-red-unauth-root
date=2026-08-13 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-58115 — Siemens SIMATIC IoT2050 Advanced ships a Node-RED interface with no authentication, so one unauthenticated HTTP request runs code as root on an OT edge gateway (CVSS 10.0)
HEADLINE: A Siemens industrial edge gateway exposes a flow-programming interface to anyone who can reach it, with maximum privileges and no credentials required
SUMMARY: Siemens ProductCERT advisory SSA-834709 of 2026-08-11 discloses CVE-2026-58115, rated 10.0 on both CVSS 3.1 and 4.0: SIMATIC IoT2050 Advanced devices running Industrial OS with Node-RED installed do not enforce authentication on the Node-RED HTTP interface, which exposes programming nodes capable of running system commands. An unauthenticated attacker with network reach creates a flow and executes arbitrary code on the device with maximum privileges — no credentials, no user interaction, no prior foothold. All versions below V4.3.4.1 are affected; V4.3.4.1 is the fix, and Siemens offers uninstalling or hardening Node-RED as interim mitigations. No exploitation is reported.
CVES: CVE-2026-58115
ENTITIES: -
PRIMARY: https://cert-portal.siemens.com/productcert/html/ssa-834709.html

## 2026-08-13/cve-2026-59310-vcenter-syslog-traversal-confirmed-exploited
date=2026-08-13 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=2026-07-30/vmware-vmsa-2026-0006-vcenter-auth-bypass-vmxnet3-escape weekly_section=None
TITLE: UPDATE — CVE-2026-59310 (VMware vCenter Syslog traversal) crosses into confirmed compromise: 361 victim addresses in 47 countries, first beacons five days after disclosure, and Switzerland's NCSC flips the advisory to actively exploited
HEADLINE: The vCenter Syslog traversal flaw, disclosed unexploited on 29 July, now has confirmed compromises and reverse-SSH persistence
SUMMARY: CVE-2026-59310, the CVSS 9.8 directory-traversal-to-code-execution flaw in the VMware vCenter Syslog server that Broadcom fixed in VMSA-2026-0006 and that this pipeline covered on 2026-07-30 as reported unexploited, is under active exploitation. German firm QUIRSO, working an incident-response engagement, identified 361 unique victim IP addresses across 47 countries whose first contact with attacker infrastructure came on 3 August — five days after public disclosure — with persistence established through a cron entry launching the open-source reverse_ssh tool for an outbound control channel. Switzerland's NCSC updated its VMSA-2026-0006 advisory to actively exploited on 12 August. No workaround exists; patching is the only remediation, and an unpatched internet-reachable vCenter now warrants a compromise assessment rather than an upgrade alone.
CVES: CVE-2026-59310
ENTITIES: -
PRIMARY: https://medium.com/@quirso_de/active-exploitation-of-cve-2026-59310-361-victim-ips-across-47-countries-9783187cc6ff

## 2026-08-13/ico-acro-reprimand-patch-ownership-gap-segmentation
date=2026-08-13 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: UK ICO reprimands the national criminal-records office over a seven-month website compromise — outsourced patching with no internal owner was the cause, and network segmentation is what capped the damage
HEADLINE: A regulator publishes the root cause of a government-body breach: patch management was contracted out, accountability for spotting critical updates was not
SUMMARY: The UK Information Commissioner's Office reprimanded ACRO Criminal Records Office on 2026-08-12 for UK GDPR security infringements after a hacker held access to its public website and content management system from August 2022 to March 2023 and staged the data of up to 10,920 people for theft — including National Insurance numbers, passport and driving licence details, bank account information, biometric data and criminal-offence records. The ICO's stated cause is governance rather than technology: ACRO had contracted patch management to third parties without establishing who internally was responsible for identifying and monitoring critical CMS updates, and did not adequately investigate security alerts that would have surfaced the intrusion earlier. Network segmentation kept the attacker out of core systems and the ICO names it among the mitigating factors it weighed.
CVES: -
ENTITIES: incident:acro-criminal-records-office-cms-breach-2022
PRIMARY: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/08/acro-reprimanded-following-cyber-security-failings/

## 2026-08-13/mydr-poland-ehr-criminal-intrusion-confirmed-processor-gap
date=2026-08-13 kind=incident horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: MyDr, a Polish electronic health record platform serving thousands of clinics, confirms a deliberate criminal intrusion — and because it is a processor, not a controller, the people affected cannot be told directly
HEADLINE: A Polish health-records processor confirms an intrusion, and because it is not the data controller it cannot tell the affected people
SUMMARY: MyDr, one of Poland's largest electronic medical record providers, confirmed on 2026-08-12 that it was the target of a deliberate external criminal act affecting part of its data, saying the data is likely historical (2024 and earlier) and that it cannot yet state what was taken. Attackers who approached Polish outlet Zaufana Trzecia Strona claim 18,814,422 unique PESEL national identity numbers and 2.5 TB of data, and describe an access chain the outlet could not independently verify: remote code execution through an XXE flaw in PKCS#12 certificate handling, a GitHub API key, source code, then AWS. The transferable finding is structural: MyDr is a GDPR processor and the controllers are thousands of individual healthcare facilities, so affected individuals cannot be notified centrally and must wait for their own clinic.
CVES: -
ENTITIES: incident:mydr-poland-ehr-breach-2026
PRIMARY: https://pro.mydr.pl/portal-info

## 2026-08-13/sharepoint-cve-2026-55040-jwt-forgery-exploited-root-cause
date=2026-08-13 kind=vulnerability horizon=operational priority=high deep_dive=True(web-app-rce) update_of=2026-08-12/sharepoint-cve-2026-63520-55040-unauth-rce-chain-poc weekly_section=None
TITLE: UPDATE — attackers are running Rapid7's SharePoint proof-of-concept against honeypots within a day, and the published root cause is four validation failures that let an unsigned token impersonate a site administrator
HEADLINE: The SharePoint JWT bypass moved from proof-of-concept to observed attack traffic in under 24 hours, and its mechanics give defenders a specific server-side hunt
SUMMARY: CVE-2026-55040, the CVSS 9.1 pre-authentication SharePoint Server authentication bypass patched in July, was reported being attacked with Rapid7's own proof-of-concept against honeypots on 2026-08-12, roughly a day after that code was published; Microsoft still does not record the flaw as exploited and Shadowserver counts over 8,500 SharePoint servers reachable from the internet. Rapid7's technical analysis — which this pipeline flagged yesterday as published but not yet read — root-causes it to four independent validation failures in SharePoint's token-handling pipeline that together let an unauthenticated caller present an unsigned token and be accepted as any site user or administrator. The mechanics supply what the advisories could not: a server-side trace message that fires on the decisive validation failure, and an unauthenticated reconnaissance request that precedes forgery.
CVES: CVE-2026-55040
ENTITIES: incident:foitt-bit-sharepoint-breach-2026-07, incident:graubuenden-canton-sharepoint-breach-2026-08
PRIMARY: https://www.rapid7.com/blog/post/ra-microsoft-sharepoint-jwt-token-authentication-bypass-cve-2026-55040/

## 2026-08-13/windrelay-nfc-relay-spynote-rat-live-call-bank-fraud
date=2026-08-13 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: WindRelay — a purpose-built Android NFC-relay malware installed silently by a companion remote-access trojan during the fraud call itself, with per-victim app names carrying the victim's own name
HEADLINE: Group-IB documents an NFC-relay family whose install step needs no victim interaction because a paired remote-access trojan performs it mid-call
SUMMARY: Group-IB's fraud team documented WindRelay on 2026-08-12, a previously unseen Android NFC-relay malware family deployed alongside a personalised build of the SpyNote remote-access trojan during a live voice-phishing call. The victim installs only the trojan — compiled per target so its app label carries the victim's own name — after which the operator uses its accessibility permissions to install the NFC relay silently, with no screen sharing and no further victim action. Group-IB correlated 23 samples uploaded between November 2025 and July 2026 impersonating institutions in Czechia, Slovakia and Slovenia, and documents a single 13-minute call monetised twice over. The detection levers are timing and permission shape, not sample identity.
CVES: -
ENTITIES: malware:windrelay, malware:spynote
PRIMARY: https://www.group-ib.com/blog/windrelay-nfc-spynote-rat-combo-fraud/

## 2026-08-15/agentic-intrusion-escalation-chain-identity-and-authority
date=2026-08-15 kind=research horizon=operational priority=notable deep_dive=False(None) update_of=2026-07-31/elastic-hugging-face-agent-initial-access-detection-mapping weekly_section=None
TITLE: UPDATE — what the Hugging Face agent did after it got a shell: a privileged pod, root on the node, one shared broker credential bound to cluster-admin, and 181 enrollments into the corporate mesh network
HEADLINE: SentinelLabs argues agentic intrusions must be investigated as action chains bound to identity and authority
SUMMARY: SentinelLabs published a cross-incident analysis on 2026-08-13 of four 2026 agentic-AI intrusions, arguing the defining property is persistence through failure rather than sophistication, and that anyone deploying an agent should be able to state its action sequence, the identity and authority behind each action, and how fast that authority can be withdrawn. The technical substrate is Hugging Face's own timeline of the July intrusion, whose escalation chain — privileged pod to node root, a shared connector credential bound to cluster-admin, mesh-VPN enrollment — is a generic Kubernetes lesson this pipeline had not carried.
CVES: -
ENTITIES: incident:hugging-face-autonomous-ai-agent-breach-2026-07, incident:aisi-cyber-range-unsanctioned-agent-actions-2026-07, incident:anthropic-cybersecurity-eval-escape-2026-07, incident:meta-ai-eval-containment-breach-2026-08
PRIMARY: https://www.sentinelone.com/labs/the-model-is-the-malware-what-four-agentic-intrusions-tell-defenders/

## 2026-08-15/clop-windchill-philips-shell-first-victim-confirmations
date=2026-08-15 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=2026-08-13/clop-leak-site-names-44-victims-swiss-dutch-listings weekly_section=None
TITLE: UPDATE — the Cl0p Windchill wave gets its first victim confirmations: Philips says a server was hit and contained, Shell says it is investigating, and a second vendor puts JSP webshells on the compromised platforms
HEADLINE: Philips and Shell respond to Cl0p's claims, moving the PTC Windchill/FlexPLM campaign from leak-site assertion to partial victim corroboration
SUMMARY: Two organisations named in Cl0p's PTC Windchill and FlexPLM extortion batch have now responded. Philips describes an attempted cyberattack on a specific company server holding internal data, says it has been brought under control and states no impact on customer environments; Shell says it is aware of a potential incident and is investigating. ReliaQuest separately reports the actors deploying JSP webshells on compromised PLM platforms — the first post-exploitation detail published for this campaign.
CVES: CVE-2026-12569
ENTITIES: actor:clop, campaign:clop-windchill-flexplm-extortion-2026
PRIMARY: https://www.bleepingcomputer.com/news/security/shell-investigates-potential-incident-after-clop-data-theft-claims/

## 2026-08-15/cve-2026-19188-haiwell-hmi-gateway-unauth-root-rce
date=2026-08-15 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-19188 — Haiwell IoT Cloud HMI Gateway: the diagnostic ping in the web interface runs attacker-supplied shell commands as root, unauthenticated (CVSS 10.0)
HEADLINE: CISA publishes a maximum-severity, CISA-assessed-automatable command injection in an HMI gateway deployed across energy, water and manufacturing
SUMMARY: CISA advisory ICSA-26-225-02 discloses CVE-2026-19188 in the Haiwell IoT Cloud HMI Gateway: the Net Check diagnostic reachable at the /setting endpoint passes the cmdPing argument to the operating system without sanitisation, so a remote unauthenticated attacker executes arbitrary commands as root. CVSS 3.1 base 10.0, version 3.40.1.12 affected, fixed in Scada-v3.50.1.19. CISA reports the product deployed worldwide in energy, critical manufacturing and water and wastewater, records no known exploitation, and assesses it automatable.
CVES: CVE-2026-19188
ENTITIES: -
PRIMARY: https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2026/icsa-26-225-02.json

## 2026-08-15/cve-2026-73487-flowise-prompt-injection-rce-fix-exists
date=2026-08-15 kind=vulnerability horizon=operational priority=notable deep_dive=False(None) update_of=2026-08-08/flowise-three-cves-vendor-sunset-no-fix-coming weekly_section=None
TITLE: UPDATE — a fourth Flowise flaw lands, and unlike the three covered a week ago this one has a fixed version: CVE-2026-73487 reaches code execution through prompt injection into the unauthenticated prediction API
HEADLINE: CVE-2026-73487 (CVSS 9.0) bypasses Flowise's Python code validator via CSV and Airtable agent nodes — and unlike the last batch, it has a fix
SUMMARY: VulnCheck assigned CVE-2026-73487 (CVSS 9.0) against Flowise before 3.1.3 on 2026-08-13, five days after this pipeline covered three Flowise CVEs that BSI marked unpatched with the vendor winding down. This one is a regex-based Python code-validator bypass in the CSV and Airtable Agent nodes reachable by prompt injection through the unauthenticated prediction API, and it does have a fixed release — so operators who concluded from the earlier batch that no fix was coming now have one to apply.
CVES: CVE-2026-73487
ENTITIES: -
PRIMARY: https://www.vulncheck.com/advisories/flowise-before-prompt-injection-rce-via-csv-agent

## 2026-08-15/fortiweb-radius-wildcard-bypass-fortimanager-fgfm
date=2026-08-15 kind=vulnerability horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-26035 — FortiWeb: one non-default RADIUS admin setting turns any username and password into a valid GUI/CLI login, alongside an FGFM impersonation bug and a FortiClient flaw reachable by anyone who can answer a laptop's DNS
HEADLINE: Fortinet patches a FortiWeb admin-login bypass gated on a 'Wildcard' option, an FGFM impersonation flaw, and a FortiClient RCE reached via crafted DNS
SUMMARY: Fortinet patched eight vulnerabilities across its products on 2026-08-12. CVE-2026-26035 (CVSS 8.8) lets a remote unauthenticated attacker log into the FortiWeb GUI or CLI with a random username and password when Remote RADIUS Type Admin authentication has the non-default Wildcard option enabled; CVE-2026-70468 (7.3) lets an attacker with a valid certificate impersonate any FortiGate managed by a FortiManager with a specific CLI option set; and CVE-2026-70465 (7.3) lets anyone able to craft DNS responses to a Windows endpoint run code through FortiClient. Each has a vendor workaround that is a configuration change rather than an upgrade. No exploitation is reported.
CVES: CVE-2026-26035, CVE-2026-70468, CVE-2026-70466, CVE-2026-70465
ENTITIES: -
PRIMARY: https://www.fortiguard.com/psirt/FG-IR-26-158

## 2026-08-15/france-dgfip-tax-authority-credential-intrusion
date=2026-08-15 kind=incident horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: France's tax authority cut the intruders' accounts in June and July and found no data theft — it took the criminal's sale listing two months later to establish that 678,000 records had already gone
HEADLINE: DGFiP confirms a 678,000-record theft via a stolen agent account and a third party's credentials — missed by its own post-intrusion access checks
SUMMARY: France's Direction générale des Finances publiques confirmed on 2026-08-14 that intrusions in June and July 2026, using stolen credentials of a DGFiP agent and of an authorised third party, were used to view and extract data on 678,000 individuals and businesses. DGFiP cut the accounts when it detected the intrusions, but its access reviews at the time did not reveal that data had been stolen; only investigations opened after the attacker advertised the dataset on 2026-08-12 established the theft.
CVES: -
ENTITIES: incident:france-dgfip-tax-breach-2026-08, actor:zerobytes
PRIMARY: https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/

## 2026-08-15/geoserver-jsonarraycontains-unauth-sqli-zeroday-exploited
date=2026-08-15 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: GeoServer: an unauthenticated SQL injection in the jsonArrayContains filter is being exploited with no CVE and no patch — and NCSC-CH has put it in front of Swiss operators
HEADLINE: Unpatched GeoServer zero-day exploited within hours of disclosure; no vendor fix exists and exposure reduction is the only control
SUMMARY: An unauthenticated SQL injection in GeoServer's jsonArrayContains filter expression, disclosed publicly on 2026-08-12, is being attacked with no CVE assigned and no vendor patch available. watchTowr recorded hundreds of exploitation attempts from a small pool of source addresses within hours of disclosure, though the observed activity so far is scanning and probing rather than confirmed compromise. GeoServer underpins public-sector geoportals and INSPIRE spatial-data services across Europe, and Switzerland's NCSC put out its own advisory on 2026-08-14 — with exposure reduction, not patching, as the available control.
CVES: -
ENTITIES: -
PRIMARY: https://www.securityweek.com/hackers-exploiting-unpatched-geoserver-zero-day/

## 2026-08-15/jwr-phishing-framework-realtime-operator-websocket-mfa
date=2026-08-15 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: JWR: a phishing kit that puts a live operator on an encrypted WebSocket into the victim's session, reading card and code digits as they are typed and choosing which one-time-code channel to demand
HEADLINE: Talos dissects a phishing-as-a-service framework whose console streams keystrokes live and prompts for SMS, app or PIN verification on demand
SUMMARY: Cisco Talos published a technical dissection on 2026-08-13 of an undocumented phishing framework its developer brands JWR, assessed with medium confidence to be a variant of the PhaaS platform Talos tracks as The Outsider. Rather than logging credentials for later use, JWR holds an AES-CTR-encrypted WebSocket open for the whole session so the operator sees partial card numbers, passwords and verification codes as the victim types, and can direct the victim to an SMS, authenticator-app, PIN or 2FA page at the moment the code is needed.
CVES: -
ENTITIES: tool:jwr-phishing-framework, campaign:outsider-phaas-gemini-2026
PRIMARY: https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework/

## 2026-08-15/mustang-panda-coolclient-signed-kernel-driver-rootkit
date=2026-08-15 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Mustang Panda's CoolClient backdoor gains a kernel driver signed with a 2013 certificate that expired in 2014 — and it hides the malware's own C2 traffic by hooking the driver Windows uses to report network state
HEADLINE: Kaspersky documents a previously undocumented CoolClient rootkit driver, deployed only once the implant already holds SCM access and SeTcbPrivilege
SUMMARY: Kaspersky's GReAT team published on 2026-08-14 a new CoolClient backdoor variant, attributed to the actor it tracks as HoneyMyte and also known as Mustang Panda, that installs a signed kernel-mode driver as a Windows service. The driver hides processes, files, registry keys and — distinctively — strips the implant's own C2 addresses from the network information Windows returns to user-mode tools. It is deployed only where the implant already holds Service Control Manager access and SeTcbPrivilege, and follows a PlugX foothold.
CVES: -
ENTITIES: actor:mustang-panda, malware:coolclient, malware:plugx, malware:toneshell
PRIMARY: https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/

## 2026-08-15/mydr-poland-19-million-records-government-confirmed
date=2026-08-15 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=2026-08-13/mydr-poland-ehr-criminal-intrusion-confirmed-processor-gap weekly_section=None
TITLE: UPDATE — Poland's government puts the MyDr breach at nearly 19 million people and over 2 TB, and the regulator confirms the notification duty sits with the ~12,000 clinics, not the platform
HEADLINE: Deputy PM Gawkowski calls it one of Poland's largest incidents; the regulator tells the clinics that used MyDr they must notify patients themselves
SUMMARY: On the same day MyDr confirmed a deliberate criminal intrusion, Poland's Deputy Prime Minister and digital affairs minister Krzysztof Gawkowski put the stolen database at nearly 19 million people and over 2 TB, and the data-protection authority UODO stated that the obligation to notify affected individuals rests with the healthcare controllers that used MyDr's services. Around 12,000 medical facilities use the platform. The processor/controller gap the earlier entry identified is now regulator-documented.
CVES: -
ENTITIES: incident:mydr-poland-ehr-breach-2026
PRIMARY: https://notesfrompoland.com/2026/08/13/poland-hit-by-theft-of-19-million-patients-data-from-medical-platform/

## 2026-08-15/netscaler-saml-signedinfo-overflow-preauth-root-rce-not-dos
date=2026-08-15 kind=vulnerability horizon=operational priority=high deep_dive=True(firewall-vpn-rce) update_of=2026-07-01/cve-2026-8451-citrix-netscaler-adc-gateway-pre-auth-saml-mem weekly_section=None
TITLE: UPDATE — the NetScaler flaw this pipeline recorded as a denial-of-service issue is a pre-authentication root shell: watchTowr publishes the full SAML SignedInfo overflow chain, and the sibling CitrixBleed bug has been carried as actively exploited since July
HEADLINE: A NetScaler bug published as a memory-overflow issue turns out to be unauthenticated code execution as root on the packet engine
SUMMARY: watchTowr published a full exploitation chain on 2026-08-14 for a NetScaler ADC/Gateway heap overflow in SAML signature canonicalization, reaching a root shell pre-authentication — a bug whose public CVE description amounts to a "Memory Overflow". watchTowr believes but cannot confirm it is CVE-2026-8452, and NCSC-CH calls the analysis "likely related" to it. Both it and the sibling CVE-2026-8451 were fixed in the same June/July release; NCSC-CH has carried CVE-2026-8451 as actively exploited with a public proof of concept since 3 July, which this pipeline's original entry recorded as unconfirmed.
CVES: CVE-2026-8452, CVE-2026-8451
ENTITIES: -
PRIMARY: https://labs.watchtowr.com/youre-back-in-the-room-citrix-netscaler-pre-auth-rce-cve-2026-8452/

## 2026-08-15/nhsbt-transplant-data-unencrypted-pager-network
date=2026-08-15 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: NHS Blood and Transplant sent organ-offer messages naming recipients over an unencrypted pager network — and because pager broadcasts leave no receiver log, it cannot scope who received them
HEADLINE: A BBC investigation forces NHSBT to report a breach: transplant-patient identifiers broadcast in clear over a legacy paging network
SUMMARY: NHS Blood and Transplant routinely sent transplant-patient names, dates of birth, tissue-match scores and immunosuppression risk factors to hospital transplant teams over an unencrypted pager network, unaware the channel carried no encryption. It acknowledged the breach only after the BBC raised it, reported to the ICO, and has stopped. Because pager broadcasts are one-way and receivers cannot be tracked, NHSBT states it cannot establish whether the data was accessed or how many people are affected.
CVES: -
ENTITIES: incident:nhs-blood-transplant-pager-breach-2026-08
PRIMARY: https://www.bbc.co.uk/news/articles/clyj92j210do

## 2026-08-15/threema-nine-colocation-ddos-swiss-messenger-outage
date=2026-08-15 kind=incident horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Threema and its Swiss colocation partner were hit by the same adaptive DDoS wave — the attack moved to the hosting layer, and only the self-hosted customers stayed up
HEADLINE: Swiss messenger Threema loses four hours to a DDoS campaign that also hit its colocation partner; availability only, no access to systems or data
SUMMARY: Threema disclosed on 2026-08-14 that a series of large-scale DDoS attacks over two days targeted both its own infrastructure and its Swiss colocation partner Nine, leaving it unclear whether Threema was the primary target. The service was unavailable for four hours on the Tuesday evening with intermittent interruptions into Wednesday. Threema states availability only was affected, not systems or data, and that customers running Threema OnPrem on their own infrastructure were unaffected throughout.
CVES: -
ENTITIES: incident:threema-nine-ddos-2026-08
PRIMARY: https://threema.com/en/blog/outage-august-2026

## 2026-08-15/trivy-not-litellm-behind-2500-org-credential-collection
date=2026-08-15 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: The '2,500-organisation LiteLLM breach' was mostly not LiteLLM: 95% of the identified victims were collected before the poisoned packages existed, through the Trivy scanner their pipelines pulled unpinned
HEADLINE: SOCRadar's row-level re-analysis moves the blast radius upstream to a compromised security scanner — which changes what a CI/CD estate has to audit
SUMMARY: SOCRadar re-analysed the exposure dataset behind the widely reported 2,500-organisation LiteLLM supply-chain breach and found that 2,085 of the 2,188 identified organisations — 95% — had credential collection that ended before the poisoned LiteLLM packages were ever published. The collection tracks the compromise of Aqua Security's Trivy scanner instead, whose poisoned release LiteLLM's own CI pulled unpinned. An estate that checked only for the LiteLLM package versions has audited the wrong artifact.
CVES: -
ENTITIES: actor:teampcp
PRIMARY: https://socradar.io/blog/litellm-supply-chain-attack/

## 2026-08-16/cve-2026-58231-sap-commerce-cloud-exploitation-attempts
date=2026-08-16 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce weekly_section=None
TITLE: CVE-2026-58231 (SAP Commerce Cloud) — exploitation attempts reached honeypots three days after patch day with no public proof-of-concept, and NCSC-NL has issued a national advisory
HEADLINE: SAP Commerce Cloud's CVSS 10.0 Data Hub Adapter flaw is being attacked three days after patch, with no public PoC
SUMMARY: CVE-2026-58231, the CVSS 10.0 unauthenticated code-execution flaw in the SAP Commerce Cloud Data Hub Adapter that this pipeline covered on 2026-08-12 as unexploited, is now being attacked: Defused recorded the first exploitation attempts hitting its honeypot sensors on 2026-08-14, three days after SAP's patch day, and states no public proof-of-concept exists. NCSC-NL published advisory NCSC-2026-0302 on 2026-08-15 recording that attackers are actively scanning for vulnerable Data Hub Adapter systems. Shadowserver tracks over 4,200 internet-exposed instances, most in Europe and North America, and the Commerce Cloud fix only takes effect after a rebuild and redeploy — so an instance that merely took the note is still exposed.
CVES: CVE-2026-58231
ENTITIES: -
PRIMARY: https://advisories.ncsc.nl/2026/ncsc-2026-0302.html

## 2026-08-16/cve-2026-65400-screen-sharing-confirmed-exploited-monero
date=2026-08-16 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=2026-08-11/cve-2026-65400-screensharingd-remote-root-two-preauth-bugs weekly_section=None
TITLE: CVE-2026-65400 (macOS Screen Sharing) crosses into confirmed exploitation — NCSC-NL reports root obtained and a Monero miner planted on multiple systems with port 5900 reachable from the internet
HEADLINE: The macOS Screen Sharing pre-auth root flaw is being exploited: NCSC-NL confirms root access and Monero miners
SUMMARY: CVE-2026-65400, the pre-authentication flaw in the macOS Screen Sharing daemon this pipeline covered on 2026-08-08 and again on 2026-08-11 as having no confirmed in-the-wild exploitation, is now confirmed exploited. NCSC-NL revised advisory NCSC-2026-0280 on 2026-08-12 to record that it had been notified of active abuse observed on multiple systems with port 5900 reachable from the internet, and that in all of those cases root access was obtained and a Monero cryptocurrency miner was planted. Nothing about the remediation changes — macOS 26.6.1, Sequoia 15.7.9 and Sonoma 14.8.9 — but the exposed population the prior entry counted at roughly 40,000 hosts now has a confirmed outcome attached to it.
CVES: CVE-2026-65400
ENTITIES: -
PRIMARY: https://advisories.ncsc.nl/2026/ncsc-2026-0280.html

## 2026-08-16/cve-2026-71362-adobe-commerce-customer-account-takeover
date=2026-08-16 kind=vulnerability horizon=operational priority=high deep_dive=False(None) update_of=None weekly_section=None
TITLE: CVE-2026-71362 — Adobe Commerce and Magento Open Source: an unauthenticated attacker switches a customer session to another customer's account (CVSS 9.1), and a WAF vendor reports it is already blocking attempts
HEADLINE: Adobe Commerce carries an unauthenticated customer account takeover, and Sansec says its WAF is already blocking attempts
SUMMARY: Adobe published APSB26-92 on 2026-08-11 for seven flaws in Adobe Commerce, Adobe Commerce B2B and Magento Open Source, headed by CVE-2026-71362, an incorrect-authorization flaw rated CVSS 9.1 that Adobe's own table records as needing no authentication, no administrator privileges and no user interaction. Sansec reviewed the patch and states the flaw lets an attacker switch a customer session to another customer's account, and that its Shield WAF is already blocking exploitation attempts; Adobe states in the same bulletin that it is not aware of any exploits in the wild. The fix ships as isolated patch files rather than a release, so a merchant must be on the latest -p release of their line before it can be applied.
CVES: CVE-2026-71362
ENTITIES: -
PRIMARY: https://helpx.adobe.com/security/products/magento/apsb26-92.html

## 2026-08-16/evooo1bot-mirai-derivative-enterprise-exploits-socks5-relay
date=2026-08-16 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=None weekly_section=None
TITLE: Evooo1Bot: a Mirai-derived Linux botnet whose exploit arsenal reaches Confluence, WSO2 and Kubernetes ingress-nginx, and whose SSH dictionary is stocked with enterprise service accounts rather than router defaults
HEADLINE: A new Mirai-derived botnet carries enterprise exploits and a SOCKS5 relay, turning what it lands on into pivot infrastructure
SUMMARY: FortiGuard Labs documented Evooo1Bot on 2026-08-13, a previously undocumented Mirai-derived Linux botnet active since at least July 2026. What separates it from the usual Mirai derivative is reach and purpose: alongside the expected router, camera and OT-gateway exploits, its module set carries working pre-authentication chains against Atlassian Confluence, WSO2 products and the Kubernetes ingress-nginx admission controller, its SSH brute-forcer cycles enterprise service-account names rather than IoT defaults, and it ships a SOCKS5 relay and an HTTP credential sniffer — so a compromised host becomes pivot and interception infrastructure, not just a DDoS node.
CVES: -
ENTITIES: tool:evooo1bot
PRIMARY: https://www.fortinet.com/blog/threat-research/multi-functional-linux-botnet-evooo1bot

## 2026-08-16/exfilsquad-fortra-confirms-13-victims-power-pages-anon-role
date=2026-08-16 kind=threat horizon=operational priority=notable deep_dive=False(None) update_of=2026-07-31/exfilsquad-uk-department-for-education-pnld-breach weekly_section=None
TITLE: ExfilSquad's claims check out: Fortra validated the published data for 13 victims, and puts the leading access theory on Power Pages portals granting the Anonymous Users role read access to Dataverse tables
HEADLINE: Fortra confirms ExfilSquad's data is genuine across 13 victims and counts over 10,000 potentially exposed Power Pages instances
SUMMARY: Fortra's intelligence team reviewed the 382.64 GB, 27-million-record archive ExfilSquad published by torrent on 2026-08-07 and concluded the group's access claims are correct for at least 13 organisations across government, education, financial services and manufacturing — the UK Department for Education and the Police National Legal Database among them. Its leading theory for the access path is misconfigured Microsoft Power Pages portals allowing public read access, the same configuration class NCSC-CH put in front of Swiss operators on 2026-08-04; it reports finding no evidence of a vulnerability being exploited or of ransomware being deployed. Fortra identified over 10,000 potential Power Pages instances publicly accessible.
CVES: -
ENTITIES: actor:exfilsquad, incident:uk-dfe-exfilsquad-breach-2026-07
PRIMARY: https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/

## 2026-08-16/jewelbug-pdf-viewer-extension-native-messaging-webmail-hole
date=2026-08-16 kind=threat horizon=operational priority=high deep_dive=True(apt-campaign) update_of=None weekly_section=None
TITLE: Jewelbug: one script tag in a shared government webmail template put a watering hole on 15+ ministry tenants at once, and the browser extension it drops escapes the sandbox through a native-messaging host named after Microsoft Edge
HEADLINE: A hack-for-hire group hit 15+ government webmail tenants with one script tag, then escaped the browser via a fake Edge helper
SUMMARY: Symantec's Threat Hunter Team published a months-long investigation into Jewelbug, a China-based hack-for-hire group that runs government espionage and a cryptocurrency-fraud business from one control panel. Rather than breach ministries one at a time, the group compromised the shared web-hosting platform run by a state telecommunications provider and added a single script tag to the common webmail template, planting a watering hole on more than 15 government tenants simultaneously. Victims who took the fake Adobe Flash lure received the Antino backdoor, which side-loads a malicious "PDF Viewer" browser extension and registers a native-messaging host called com.microsoft.runedge — the component that turns browser-level access into command execution on the host.
CVES: -
ENTITIES: actor:jewelbug, tool:xg-web, malware:antino, malware:jewelbug-pdf-viewer-extension, malware:clientking
PRIMARY: https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage

## 2026-08-16/weekly-w33-attacking-the-record-not-the-sensor
date=2026-08-16 kind=synthesis horizon=strategic priority=high deep_dive=False(None) update_of=None weekly_section=weekly-multi-day
TITLE: Three unrelated intrusions and one research publication worked this week attacked the evidence a responder reconstructs afterwards rather than the sensor watching at the time — and two of the week's victims proved the same point from the defending side
HEADLINE: W33's evasion work targeted the record, not the alarm — a shell log that stores the wrong command, and forensics tooling as camouflage
SUMMARY: Four disclosures this pipeline worked during 2026-W33 — three of them published in the days just before it — share a property that is not ordinary defence evasion. CrowdStrike catalogued 21 distinct command-obfuscation techniques across six categories in VMware ESXi's BusyBox shell and identified the load-bearing defect as a logging property rather than a vulnerability: ESXi shell logs capture commands during parsing, before expansion, so the log preserves the obfuscated form and a search for the literal string esxcli misses the command entirely. Group-IB documented an intruder who escalated to root and then spent the intrusion impersonating ordinary users through the pam_rootok policy as a deliberate forensic smokescreen, disabling logging services and removing authentication logs. Sophos investigated an Interlock intrusion in which the operator acquired a memory image with WinPmem and ran Volatility3's credential plugins offline against it, leaving traces indistinguishable from a real investigation. A six-agency advisory records Gunra affiliates editing a victim's VDI authentication files so one attacker-chosen one-time-password value always validated. And two European public bodies showed the defensive mirror in the same week — France's tax authority whose own post-intrusion access reviews did not reveal a theft that had already happened, and a UK health body that cannot scope a disclosure because the channel keeps no receiver log.
CVES: -
ENTITIES: actor:interlock, campaign:groupib-xmrig-pam-forensic-smokescreen, actor:gunra, incident:france-dgfip-tax-breach-2026-08, incident:nhs-blood-transplant-pager-breach-2026-08
PRIMARY: https://www.crowdstrike.com/en-us/blog/crowdstrike-hunts-for-shell-command-obfuscation-vmware-esx/

## 2026-08-16/weekly-w33-clop-windchill-status
date=2026-08-16 kind=synthesis horizon=strategic priority=notable deep_dive=False(None) update_of=None weekly_section=weekly-long-running
TITLE: Cl0p PTC Windchill campaign status: the extortion wave crossed from leak-site assertion to partial victim corroboration this week — Philips and Shell responded, European organisations appeared among the named listings, and a second vendor confirmed the webshell artefact PTC had already documented
HEADLINE: Windchill campaign status — first victim responses, named European listings, and independent corroboration of the JSP webshell artefact
SUMMARY: Status update on the Cl0p mass-extortion campaign against internet-exposed PTC Windchill and FlexPLM deployments, tracked here since 27 July through CVE-2026-12569. Three in-window deltas move it from claim to partial corroboration. A leak-site tracker recorded 44 named Cl0p victim listings on 12 August, among them a Swiss and a Dutch organisation alongside others in Finland, the United Kingdom, Italy, Slovakia, Hungary and France; separately, a vendor reviewing an earlier batch of 42 masked listings assessed a possible relationship with this campaign from the advertised data categories, while stating leak-site information alone cannot establish the access route for any listed organisation. Two days later Philips said an attempted attack on a specific company server had been brought under control with no impact on customer environments, and Shell said it was aware of a potential incident and investigating — the first responses from named organisations. ReliaQuest separately reported actors deploying JSP webshells on compromised product-lifecycle platforms, which corroborates rather than introduces the artefact class: PTC itself had already documented hexadecimal-named JSP webshells under the Windchill login directory. The two victim counts in circulation differ — a leak-site tracker recorded 44 named listings, BleepingComputer counts 43 — and neither is a count of confirmed victims.
CVES: -
ENTITIES: actor:clop, campaign:clop-windchill-flexplm-extortion-2026
PRIMARY: https://www.bleepingcomputer.com/news/security/shell-investigates-potential-incident-after-clop-data-theft-claims/

## 2026-08-16/weekly-w33-compromised-party-was-not-the-notifying-party
date=2026-08-16 kind=synthesis horizon=strategic priority=high deep_dive=False(None) update_of=None weekly_section=weekly-sector-patterns
TITLE: A third party was on the access path or holding the data in all six European public-sector and critical-infrastructure disclosures this week — and where the third party held the data, the duty to notify landed on organisations with no facts to write
HEADLINE: W33's European breaches all ran through a third party, and in two of them the notification duty landed where the intrusion did not
SUMMARY: Six European disclosures across 2026-W33 share a structure rather than a sector: in each, a supplier, processor or contractor sat either on the access path into the victim or in possession of the data — and in two of them that displaced the duty to tell the affected people onto organisations that had no facts to write. Poland's MyDr, an electronic health record platform, confirmed a criminal intrusion reported at nearly 19 million people, and the data-protection authority confirmed that because MyDr is a processor the notification duty rests with the roughly 12,000 clinics that used it. One intrusion at CEVA Logistics put ten organisations into breach reporting with the Dutch regulator at once. France's tax authority was reached partly through an authorised third party's credentials. Retelit, an Italian operator serving 193 public administrations, disclosed only in a right-of-reply after a press investigation. Żabka's intrusion came through an external service provider's account. And the UK's Information Commissioner reprimanded the national criminal-records office for contracting patch management out without establishing who internally owned it.
CVES: -
ENTITIES: incident:mydr-poland-ehr-breach-2026, incident:ceva-logistics-fulfilment-breach-2026-08, incident:france-dgfip-tax-breach-2026-08, incident:retelit-qilin-2026, actor:qilin, incident:zabka-supplier-account-jira-gitlab-secrets-2026-07, incident:acro-criminal-records-office-cms-breach-2022
PRIMARY: https://notesfrompoland.com/2026/08/13/poland-hit-by-theft-of-19-million-patients-data-from-medical-platform/

## 2026-08-16/weekly-w33-developer-credential-audits-wrong-artefact
date=2026-08-16 kind=research horizon=strategic priority=notable deep_dive=False(None) update_of=None weekly_section=weekly-research
TITLE: Three developer-credential findings this week each show an estate auditing the wrong thing — the wrong package, the wrong incident class, and repositories nobody counted as company assets at all
HEADLINE: W33's supply-chain work was about scoping errors: 95% of one 'breach' traced to a different vendor, and repo theft is a secrets incident
SUMMARY: Three independent findings inside 2026-W33 converge on scoping rather than technique. SOCRadar re-analysed the exposure dataset behind the widely reported 2,500-organisation LiteLLM supply-chain breach and found 2,085 of the 2,188 identified organisations show collection activity beginning before the poisoned LiteLLM packages reached PyPI — the collection tracks the earlier compromise of Aqua Security's Trivy scanner, which LiteLLM's own CI pulled unpinned, so an estate that checked for LiteLLM package versions audited the wrong artefact. Wiz's incident-response team published a playbook for a campaign that abused compromised GitHub Personal Access Tokens, in which the actor used 102 AWS IP addresses in one region over roughly six hours to clone up to thousands of repositories per victim organisation, and argues repository theft should be handled as a credentials incident rather than a source-code one; a companion post reports 56% of company-impacting secrets it found across one company set sat in employees' personal repositories, outside enterprise scanning entirely. CERT Intrinsec's forensic-artefact series shows where coding-agent CLIs write plaintext provider credentials on disk.
CVES: -
ENTITIES: actor:teampcp, trend:coding-agent-ci-harness-trust-boundary-2026-08, report:intrinsec-ai-agents-digital-forensics-series
PRIMARY: https://www.wiz.io/blog/investigating-github-pat-compromise

## 2026-08-16/weekly-w33-disclosure-to-exploitation-interval-collapsed
date=2026-08-16 kind=synthesis horizon=strategic priority=high deep_dive=False(None) update_of=None weekly_section=weekly-top-stories
TITLE: The gap between public disclosure and working exploitation closed to days or hours across five unrelated products — a patch day, a proof-of-concept, a researcher's post and a binary diff each turned public information into a working attack inside a week
HEADLINE: Three products drew observed attacks inside three days, two more inside a week — and one working exploit was rebuilt from the patch diff in four hours
SUMMARY: Five unrelated products were reported under exploitation close behind their own disclosure in the week to 2026-08-16, and no two triggers were quite the same. Three of the five drew observed attacks inside three days: SAP Commerce Cloud's CVSS 10.0 Data Hub Adapter flaw was hitting honeypots three days after patch day with no public proof-of-concept in existence; Rapid7's SharePoint authentication-bypass write-up and exploit were being replayed against honeypots the following morning; and a GeoServer SQL injection with no CVE and no patch drew hundreds of exploitation attempts within hours of a researcher's post. The other two took longer and are the more uncomfortable pair, because both were exploited after a fix existed: a vCenter flaw disclosed unexploited on 29 July had 361 victim addresses across 47 countries, concentrated in Germany, the United States, Turkey, Iran and France, with first contact five days after disclosure; and Apple's Screen Sharing flaw, patched out of band on 6 August, was confirmed by the Dutch national CERT on 12 August with root obtained and Monero miners planted. The Screen Sharing case also carries the week's shortest interval of a different kind — one team rebuilt two working pre-authentication root exploits from the patch diffs in about four hours on 8 August, four days before that confirmation. Switzerland's NCSC published its own advisory on the GeoServer flaw while no fix existed to apply.
CVES: -
ENTITIES: -
PRIMARY: https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/

## 2026-08-16/weekly-w33-dutch-nis2-in-force-no-transition
date=2026-08-16 kind=policy horizon=strategic priority=notable deep_dive=False(None) update_of=2026-08-09/weekly-w32-nis2-enforcement-phase-netherlands-germany weekly_section=weekly-policy
TITLE: UPDATE — the Dutch NIS2 clock the prior weekly recorded as forthcoming started on 15 August, and the national CERT confirms the registration duty applies from the entry-into-force date itself with no transition window
HEADLINE: The Cyberbeveiligingswet is in force — registration is a live obligation from day one, not a deadline to work toward
SUMMARY: On 15 August 2026 the Cyberbeveiligingswet and the companion Wet weerbaarheid kritieke entiteiten entered into force, confirmed the same day by NCSC-NL, which stated the laws now apply and that organisations falling under them face new obligations. A prior weekly recorded this date as forthcoming; the delta is that it arrived and that the registration mechanics are now published. NCSC-NL's registration guidance states the duty applies from the entry into force of the Cyberbeveiligingswet on 15 August 2026 and describes no grace window, so an in-scope organisation that had not registered was out of compliance the moment the clock started. Registration runs through the national entity register, gated by eHerkenning at assurance level EH2+ or SSOnRijk for connected government bodies. For a Swiss federal SOC the obligation is Dutch, but the enforcement mechanics — portal registration with strong-authentication gating, no transition period, and supply-chain due diligence cascading onto unregulated vendors — are what Swiss suppliers selling into the Dutch and wider EU public sector will be asked to evidence.
CVES: -
ENTITIES: policy:netherlands-nis2-cyberbeveiligingswet-2026
PRIMARY: https://www.ncsc.nl/nieuws/cbw-en-wwke-nu-van-kracht

## 2026-08-16/weekly-w33-etsi-cra-harmonised-standards-approval
date=2026-08-16 kind=policy horizon=strategic priority=notable deep_dive=False(None) update_of=2026-08-02/weekly-w31-commission-cra-application-guidance weekly_section=weekly-policy
TITLE: UPDATE — the Cyber Resilience Act's conformity route entered formal approval this week: ETSI put 17 draft product-category standards out for Public Enquiry, and the procedure runs past the regulation's first reporting deadline
HEADLINE: ETSI opens approval on 17 CRA standards covering firewalls, VPNs, SIEM and PKI software — none can be relied on before 11 September
SUMMARY: On 13 August 2026 ETSI announced the availability of 17 vertical final draft standards developed under the EU Cyber Resilience Act and currently under Public Enquiry, submitted this summer to 41 member organisations across Europe including the national standardisation bodies of the European Economic Area. These are the standards intended to become Harmonised Standards, which is what would give manufacturers the CRA's presumption of conformity. The product categories are directly relevant to public-sector procurement — the EN 304 series covers browsers, password managers, antivirus, VPNs, network management systems, SIEM, boot managers, PKI certificate-issuance software, network interfaces, operating systems, routers and switches, virtualization and container platforms, firewalls, and four consumer and IoT categories. ETSI states the approval procedure runs until mid-September to mid-November 2026 depending on the vertical, which places completion at or after the CRA's first hard operational clock: the reporting obligations that begin on 11 September 2026. Until then the presumption-of-conformity route is unavailable and manufacturers demonstrate compliance by other means.
CVES: -
ENTITIES: policy:eu-cyber-resilience-act
PRIMARY: https://www.etsi.org/newsroom/press-releases/etsi-launches-approval-process-for-17-european-standards-supporting-the-cyber-resilience-act/

## 2026-08-16/weekly-w33-exfilsquad-claims-validated-status
date=2026-08-16 kind=synthesis horizon=strategic priority=notable deep_dive=False(None) update_of=None weekly_section=weekly-long-running
TITLE: ExfilSquad status: a vendor validated the group's published data across 13 victim organisations and put the access path on misconfigured Power Pages portals — reversing the assessment, recorded here two weeks ago, that its victim list was more likely fabricated
HEADLINE: ExfilSquad's claims checked out — 13 victims validated, no vulnerability involved, and 10,000+ Power Pages instances publicly reachable
SUMMARY: Status update on the ExfilSquad extortion brand, tracked here since 31 July. A prior weekly recorded a threat-intelligence vendor assessing fabrication as the more likely explanation for the group's 15-name victim list, with one confirmed government breach inside it. That assessment has now been overtaken. Fortra's intelligence team reviewed the 382.64 GB, 27-million-record archive the group published by torrent on 7 August and concluded the access claims are correct for at least 13 organisations across government, education, financial services and manufacturing, the UK Department for Education and the Police National Legal Database among them. Its leading theory for the access path is misconfigured Microsoft Power Pages portals allowing public read access — the same configuration class Switzerland's NCSC put in front of its own constituency on 4 August — and it reports finding no evidence of a vulnerability being exploited or of ransomware being deployed, while identifying over 10,000 potentially publicly accessible Power Pages instances. A private-sector victim conceded a CRM incident in the same week while disputing its severity.
CVES: -
ENTITIES: actor:exfilsquad, incident:uk-dfe-exfilsquad-breach-2026-07
PRIMARY: https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/

## 2026-08-16/weekly-w33-kernel-rootkits-edit-what-windows-reports
date=2026-08-16 kind=synthesis horizon=strategic priority=high deep_dive=False(None) update_of=None weekly_section=weekly-top-stories
TITLE: Two espionage toolsets shipped kernel-mode rootkits in the same week whose job is to edit what Windows reports to the defender's own tools — and one of them arrived on a zero-day that was patched on Tuesday
HEADLINE: Lazarus and Mustang Panda both went below the sensor in W33 — one via an exploited AFD.sys zero-day, one via a 2013 signing certificate
SUMMARY: Two unrelated state-nexus espionage disclosures inside 2026-W33 deploy kernel-mode drivers with the same objective: not to evade a detection rule, but to change the answers the operating system gives the tools that ask it. Check Point attributed an exploited Windows AFD.sys zero-day, CVE-2026-68820, to a Lazarus intrusion that used it to load FudModule v3.1 — a rootkit whose shared component set is a telemetry teardown suite covering process, thread and image notify callbacks, object and registry callbacks, minifilter removal by altitude band, and termination of the NT Kernel Logger. Microsoft patched it on 11 August and CISA catalogued it the same day; Check Point records successful targeting in Western Europe including France and Germany, and one compromised French organisation being reused to phish others. Days later Kaspersky documented a CoolClient variant attributed to Mustang Panda installing a kernel driver that hooks Nsiproxy so that C2 addresses the operator registers with the driver are filtered out of the network data Windows returns to user mode, signed with a certificate valid from August 2013 to September 2014.
CVES: -
ENTITIES: actor:lazarus-group, campaign:operation-dream-job, tool:fudmodule, actor:mustang-panda, malware:coolclient, actor:jewelbug
PRIMARY: https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/

## 2026-08-16/weekly-w33-looking-ahead
date=2026-08-16 kind=outlook horizon=strategic priority=notable deep_dive=False(None) update_of=None weekly_section=weekly-looking-ahead
TITLE: 2026-W33 looking ahead — items already in motion: a CRA reporting clock at four weeks, standards approval that will not beat it, an exploited flaw with no patch in existence, seven further flaws with no fix coming, and twelve thousand Polish clinics who each owe a notification
HEADLINE: W33 outlook — the 11 September CRA reporting start, GeoServer exploited with no vendor fix, and a notification duty split across 12,000 controllers
SUMMARY: A watch list of items already in motion at the close of ISO week 2026-W33, each with a source and a date — not predictions. The Cyber Resilience Act's reporting obligations begin on 11 September 2026, and ETSI's approval procedure for the 17 draft harmonised standards runs to mid-September or mid-November depending on the vertical, so the presumption-of-conformity route will not be available first. GeoServer's unauthenticated SQL injection is being exploited with no CVE and no vendor patch, leaving exposure reduction as the only control. Seven further flaws tracked this week have no fix at all either, including the ShieldBreak bypass of Microsoft's July Defender patch and three FreeBSD pre-authentication kernel primitives behind TCP/999. Around 12,000 Polish medical facilities each carry the duty to notify their own patients over the MyDr breach. The Dutch Cyberbeveiligingswet registration obligation is live with no transition window. Swiss federal administrative units have until 1 January 2027 to have built their own information security management system.
CVES: -
ENTITIES: policy:eu-cyber-resilience-act, policy:netherlands-nis2-cyberbeveiligingswet-2026, policy:switzerland-isv-federal-isms-deadline-2026, incident:mydr-poland-ehr-breach-2026, actor:clop, campaign:clop-windchill-flexplm-extortion-2026
PRIMARY: https://www.etsi.org/newsroom/press-releases/etsi-launches-approval-process-for-17-european-standards-supporting-the-cyber-resilience-act/

## 2026-08-16/weekly-w33-passkey-fourth-thread-documented-and-closed
date=2026-08-16 kind=research horizon=strategic priority=notable deep_dive=False(None) update_of=2026-08-09/weekly-w32-passkeys-attacked-from-three-directions weekly_section=weekly-research
TITLE: UPDATE — the fourth passkey attack thread this pipeline could not source last week is now documented, and it closed: Windows cached YubiKey assertions in cleartext where any authenticated user could read them, and the July updates broke the chain
HEADLINE: Pass-the-Passkey gets its sourcing — a readable event-log cache replayed into Entra ID, fixed as CVE-2026-34348 before the research went public
SUMMARY: A prior weekly covered three simultaneous attacks on passkeys and recorded that a fourth thread had been dropped for want of a citable source. That thread is now documented. SpecterOps principal security researcher Michael Grafnetter presented Pass-the-Passkey at Black Hat USA 2026 on 5 August; a write-up on 10 August reports that Windows stored past YubiKey signatures in cleartext where authenticated unprivileged users, including remote users, could read them, and that chaining those signatures with weaknesses in Entra ID's passkey validation allowed privileged-user impersonation despite policies requiring phishing-resistant multifactor authentication. The correction that matters is the outcome: the Windows side was fixed as CVE-2026-34348, vendor CVSS 6.5, in the July 2026 updates, SpecterOps now considers the full Windows-to-Entra chain broken because those updates make event-log assertions unusable for replay, and Microsoft says it has also applied mitigations on the relay-assertion side. What survives is the design lesson the three earlier threads already carried.
CVES: CVE-2026-34348
ENTITIES: trend:passkey-webauthn-attack-surface-2026-08
PRIMARY: https://thehackernews.com/2026/08/new-passkey-attacks-can-recover-synced.html

## 2026-08-16/weekly-w33-q2-ransomware-reports-dragos-checkpoint
date=2026-08-16 kind=annual-report horizon=strategic priority=notable deep_dive=False(None) update_of=None weekly_section=weekly-annual-reports
TITLE: Two independent Q2 2026 ransomware reports published three days apart agree the ecosystem is fragmenting without de-concentrating — and the industrial one carries a negative finding OT operators should plan against: no Q2 case reached control-system manipulation
HEADLINE: Dragos and Check Point both counted Q2: 93 active groups against a 57.6% top-ten share, and zero incidents reaching ICS Stage 2
SUMMARY: Dragos published its Industrial Ransomware Analysis for Q2 2026 on 10 August and Check Point Research published The State of Ransomware Q2 2026 on 13 August. From different vantage points — industrial-sector incidents and all leak-site victims — they describe the same structure. Dragos identified 1,140 ransomware incidents affecting industrial organisations, a 12% increase over Q1's 1,020, with manufacturing the most affected sector at 747 incidents or 65%, the United States the most impacted country at 431 incidents or 38%, and Germany the country with the greatest quarter-over-quarter increase, from 37 incidents to 68. Check Point counted 2,139 data-leak-site victims, essentially flat quarter over quarter and up 33% year over year, with the top ten groups' share falling from 71% to 57.6% while the number of active groups climbed from 71 to 93. The finding with the most direct planning consequence is Dragos's negative one: it observed no case in Q2 in which a ransomware operator reached Stage 2 of the ICS Cyber Kill Chain or directly manipulated a control system — every operational disruption followed compromise of enterprise and virtualisation systems instead.
CVES: -
ENTITIES: report:dragos-industrial-ransomware-q2-2026, report:checkpoint-state-of-ransomware-q2-2026, actor:qilin, actor:akira, campaign:the-gentlemen-ransomware-storm2697, actor:krybit
PRIMARY: https://www.dragos.com/blog/dragos-industrial-ransomware-analysis-q2-2026

## 2026-08-16/weekly-w33-russia-europe-ukraine-defence-supply-chain
date=2026-08-16 kind=research horizon=strategic priority=notable deep_dive=False(None) update_of=None weekly_section=weekly-research
TITLE: Russia's campaign against Europe's Ukraine defence supply chain is assessed to have widened from collection and sabotage to pressuring the people and firms behind it — and the cyber half is aimed at logistics data, not at the manufacturers
HEADLINE: Truesec assesses the target set has broadened past logistics disruption to the individuals and suppliers enabling European defence support
SUMMARY: Truesec published an assessment on 14 August 2026 drawing a set of separately-reported European incidents into one campaign picture: German authorities reportedly investigating surveillance of the chief executive of drone manufacturer Donaustahl and his family in late 2025 and early 2026; the 2024 US-assisted disruption of a Russian plot against Rheinmetall's chief executive; Russian publication of European drone producer addresses, which Truesec assesses as target signalling rather than disclosure; and GRU-linked cyber activity against logistics and technology companies transporting aid to Ukraine. Its judgement is that the campaign's focus "is no longer limited to intelligence collection, sabotage or disruption of logistics" and now extends to the people, facilities and supply chains that make European defence support possible. For defenders the concrete half is the cyber targeting, which Western authorities attributed to GRU Unit 26165: attempts to obtain shipment-related information including train schedules, manifests, routes, cargo contents and sender and recipient details. This is an assessment resting on reporting Truesec cites rather than on new first-hand telemetry, and is carried as such.
CVES: -
ENTITIES: -
PRIMARY: https://www.truesec.com/hub/blog/russia-targets-businesses-and-officials-behind-europes-ukraine-defence-supply-chain

## 2026-08-16/weekly-w33-vuln-status-rollup
date=2026-08-16 kind=vulnerability horizon=strategic priority=high deep_dive=False(None) update_of=None weekly_section=weekly-vuln-rollup
TITLE: 2026-W33 vulnerability status roll-up — eight flaws crossed into confirmed exploitation or the federal catalogue this week, two of them within seventy-two hours of their own disclosure, against a critical tail led by two unauthenticated CVSS 10.0 flaws in industrial edge devices
HEADLINE: W33 CVE trajectory — eight newly exploited or newly catalogued, one exploited with no identifier at all, and eight flaws with no fix in existence
SUMMARY: Consolidated status of the vulnerabilities this pipeline covered operationally in ISO week 2026-W33, each with its trajectory this week set against when it was first covered. Newly confirmed exploited or newly KEV-listed: CVE-2026-20349 (Cisco Secure Firewall ASA/FTD), CVE-2026-68820 (Windows AFD.sys, a Lazarus zero-day), CVE-2026-72898 (Metabase, CVSS 10.0), CVE-2026-59310 (VMware vCenter), CVE-2026-55040 (Microsoft SharePoint), CVE-2026-65400 (macOS Screen Sharing), CVE-2026-58231 (SAP Commerce Cloud) and CVE-2026-71362 (Adobe Commerce). CVE-2026-45659 gained a ransomware-campaign-use flag rather than a new exploitation finding. Exploited with no identifier: the GeoServer jsonArrayContains SQL injection, which also has no patch. The critical tail is led by two unauthenticated CVSS 10.0 flaws on industrial edge devices — Siemens SIMATIC IoT2050 Advanced and the Haiwell IoT Cloud HMI Gateway — and by eight flaws where no fix exists at all. Full per-flaw detail lives in the referenced operational entries; this roll-up carries only the week's trajectory.
CVES: -
ENTITIES: -
PRIMARY: https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/

## 2026-08-16/weekly-w33-water-plc-lockout-status
date=2026-08-16 kind=synthesis horizon=strategic priority=notable deep_dive=False(None) update_of=2026-08-09/weekly-w32-water-plc-lockout-status weekly_section=weekly-long-running
TITLE: UPDATE — water-sector PLC lockout status: an OT vendor's decade retrospective attributes the Minnesota controller intrusions to a CVE whose own record names a different Rockwell product family, and the campaign still has no CVE and no actor named by any investigating body
HEADLINE: Water campaign status — the first vendor CVE attribution appeared this week, and it does not match the CVE's own affected-product list
SUMMARY: Status update on the US water-sector PLC lockout campaign a prior weekly consolidated for its European exposure. The in-window delta is a sourcing problem rather than a technical one. Dragos published a decade-spanning retrospective on 13 August comparing the 2013 Bowman Dam intrusion to the July 2026 Minnesota campaign, and states the Minnesota controllers were exploitable through a known authentication bypass vulnerability, CVE-2021-22681, added to CISA's catalogue in March 2026. The catalogue date checks out. The product scope does not: CISA's own ICS advisory for that CVE is titled "Rockwell Automation Logix Controllers", describes Studio 5000 Logix Designer using a key to verify Logix controllers, and lists the affected products as RSLogix 5000 versions 16 through 20, Studio 5000 Logix Designer version 21 and later, and FactoryTalk Security — while the controllers Dragos itself names in the same piece, and that the FBI and EPA identified, are MicroLogix 1100 and 1400. No investigating body has named a CVE or an actor for these intrusions; the published technique remains reachability plus credential control, involving no vulnerability at all.
CVES: CVE-2021-22681
ENTITIES: incident:minnesota-water-utilities-coordinated-cyberattack-2026-07
PRIMARY: https://www.dragos.com/blog/water-utility-attacks-decade-of-gaps

