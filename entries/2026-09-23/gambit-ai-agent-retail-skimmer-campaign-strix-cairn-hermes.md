---
schema: 1
kind: threat
title: "Open-source AI pentesting harnesses (Strix, Cairn, Hermes) run an autonomous intrusion-and-skimmer campaign against online retailers for about $25 a target"
headline: "Three off-the-shelf AI agents ran almost the entire card-theft campaign, from discovery to checkout-page skimmer, for the price of a lunch per victim"
summary: >
  Gambit Security reconstructs a financially motivated campaign, running since July 2026, in which
  three open-source AI agent harnesses, Strix (vulnerability discovery), Cairn (autonomous
  exploitation) and Hermes (orchestration), ran nearly the entire intrusion lifecycle unattended
  against online retailers, compromising at least 27 named victims. Gambit's body confirms skimmers in place on 19 of them while its own summary counts skimmer installations on five, and it detected more than 100 further websites infected with a skimmer associated with the campaign. Hermes is the same open-source agent framework
  seen in three earlier, unrelated intrusions that touched government targets in Thailand, Taiwan
  and Malaysia.
discovered_at: "2026-09-23T04:50:00Z"
updated_at: "2026-09-25T04:30:00Z"
event_date: "2026-09-22"
run_id: 2026-09-23T0405Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, cryptocrime, ai-abuse]
regions: [global, us]
sectors: [retail]
entities: ["tool:hermes-ai-agent", "tool:strix-ai-pentest", "tool:cairn-exploitation-engine", "product:magento", "product:wordpress"]
techniques: [T1190, T1552.001, T1548.003, T1555.006, T1505.003, T1659, T1053.003, T1485, T1078]
affected_products: ["Magento", "WordPress"]
cves: []
sources:
  - url: "https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company"
    publisher: "Gambit Security"
    date: "2026-09-22"
    role: primary
  - url: "https://cybersecuritynews.com/ai-agents-retail-credit-card-theft/"
    publisher: "Cybersecurity News"
    date: "2026-09-22"
    role: corroborating
  - url: "https://www.computing.co.uk/news/2026/security/ai-agents-used-to-steal-credit-card-records"
    publisher: "Computing (UK)"
    date: "2026-09-23"
    role: corroborating
  - url: "https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent"
    publisher: "Hunt.io"
    date: "2026-07-23"
    role: corroborating
  - url: "https://www.tenable.com/blog/the-agentic-ai-threat-cluster-seven-incidents-three-actors-and-what-they-mean"
    publisher: "Tenable"
    date: "2026-08-14"
    role: corroborating
  - url: "https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-07-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Between 10 and 15 September alone, 105 attack projects were launched and at least 27 companies were compromised to varying degrees."
    publisher: "Gambit Security"
    source_url: "https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company"
  - quote: "the operator’s own cost review gives a similar figure, a mean of $25.46 over 101 completed scans, from $3.13 for the cheapest target to $79.31 for the most expensive"
    publisher: "Gambit Security"
    source_url: "https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company"
  - quote: "One of the Hermes agent’s skill files tells the agent to erase the card data from the victim’s Magento database once the data is stolen."
    publisher: "Gambit Security"
    source_url: "https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company"
verification: single-source
sourcing_note: >
  Gambit Security is the sole technical assessor, having recovered and analysed the operator's
  exposed staging server, so its reconstruction is followed throughout, including its USD 12,000 to
  18,000 spend range over Computing UK's lower figure. Details that appear only in secondary
  coverage and not in Gambit's primary, such as a 'Kimi' model in the harness stack, are not
  carried; the Anthropic ban and Cloudflare takedown in the 2026-09-25 update are corroborated by
  Computing UK's own reporting.
confidence: medium
references: ["2026-07-25/thailand-mof-hermes-ai-agent-post-exploitation", "2026-08-28/taiwan-agentic-ai-intrusion-openclaw-hermes-guardrail-bypass", "2026-07-31/unit42-autonomous-deepseek-hermes-netscaler-cve-2026-3055"]
deep_dive: true
deep_dive_category: web-app-rce
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-25T04:30:00Z"
    run_id: 2026-09-25T0404Z-intel
    type: update
    summary: >
      Anthropic identified and banned the account behind Hermes's use of an earlier Claude model in
      this campaign, and Cloudflare took down the operator's staging infrastructure; the operator
      rebuilt within hours and the campaign continued. Both reactive controls had only marginal
      disruptive effect.
    fields: [sources, body, sourcing_note]
  - at: "2026-09-30T06:56:13Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Priority recalibrated from high to notable: a retail web-skimmer campaign that does not reach
      government portals. The text presented Gambit's extrapolated $12,000-18,000 spend as
      OpenRouter billing, called the wipe skill self-written, took Gambit's 19-victim skimmer count
      without its own summary's five, described three earlier Hermes intrusions and a safety-rail
      bypass in each without citation, and called the access at four named victim types
      partial-to-full compromise. The spend, skimmer and access passages now follow Gambit, and the
      earlier intrusions are cited to Hunt.io, Tenable and Unit 42 with the bypass claim narrowed to
      three of the four cases. Gambit's further 100-plus infected sites, the admin-pod injection
      route and the hand-picked victims follow its wording, and the Unit 42 safety-control route is
      stated as its model choice. The headline keeps Gambit's "almost".
    fields: [priority, sourcing_note, body, summary, sources, headline]
migrated_from: null
---

Gambit Security's Threat Intelligence team recovered a financially motivated operator's exposed staging server and reconstructed a campaign, running since July 2026, in which three off-the-shelf open-source AI agent harnesses conduct nearly the entire intrusion lifecycle unattended against online retailers. Strix, an open-source AI pentesting tool run via OpenRouter (GLM 5.2, later switched to DeepSeek v4 Pro), performs autonomous vulnerability discovery: 146 deep-mode scans against 138 hosts between 23–31 August 2026, burning 633 hours of scanner time within 195 hours of wall-clock time. Cairn, an autonomous exploitation engine on DeepSeek v4.1 Flash, receives a target domain and an objective and runs unattended for hours until it gets a shell or admin access: "between 10 and 15 September alone, 105 attack projects were launched and at least 27 companies were compromised to varying degrees" ([Gambit Security, 2026-09-22](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company)). Hermes, an open-source autonomous agent with persistent memory and skills the agent writes and edits itself, orchestrated the campaign end to end, running on Anthropic Opus 4.6 ("after newer models refused its requests") under a Chinese system persona the operator loaded, titled "SOUL - Red Team Operator". The operator had added a custom skill that strips Hermes's own content-safety filters, and drove the campaign through only 1,951 short, largely Chinese-language operator prompts across 260 sessions, with most of the actual attack work running autonomously between those prompts ([Gambit Security, 2026-09-22](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company)).

One fully documented Cairn project illustrates the chain, though Gambit is explicit that each victim's actual path was chosen dynamically through real-time probing and most chains differed victim to victim: unauthenticated SQL injection in a login email parameter (error-based EXTRACTVALUE) read a one-time-passcode value in plaintext directly from an application database table, bypassing multi-factor authentication and reaching the admin panel; an image-upload field with no extension check then gave host remote code execution as a non-root user; a `sudo` misconfiguration allowing NOPASSWD execution of `python3.12` escalated that to root; an internal NFS mount configured with `no_root_squash` let the agent read a separate host's WordPress database credentials in plaintext from its `wp-config.php`; those credentials gave a direct database write creating a new WordPress administrator account, which in turn let the agent upload a malicious plugin for code execution on the blog host; from there the agent dumped the full contents of the account's AWS Secrets Manager (46 secrets, 102 KB), reached the production Magento database on Amazon Aurora, extracted the Magento application's encryption key, and used it to decrypt stored card numbers encrypted with Blowfish in ECB mode. Confirmed impact across the campaign: 600,000-plus unexpired credit-card records exfiltrated from two victims, and skimmer scripts ordered against at least 27 named victims and confirmed in place on 19 of them according to the body of Gambit's report, although its own summary counts skimmer installations on the websites of five companies and does not reconcile the two figures. Gambit also detected more than 100 further websites infected with a skimmer associated with the campaign. Gambit reports some level of access to the assets of companies including a Fortune 500 hospitality company, a major US airline, a large private US industrial-supplies distributor and a US online fashion retailer, which it names separately from the illustrative chain above. A per-country cardholder breakdown embedded in Gambit's own page (488,372 of the recovered cards, 79.0%, United States) skews overwhelmingly toward the United States; no Swiss-issued cards appear among the top entries of that table ([Gambit Security, 2026-09-22](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company)).

Gambit documents eight distinct skimmer-injection methods used across victims, all worth carrying into any custom-web-application hardening review: appending the loader to the end of a legitimate, already-served JavaScript file while restoring its original modification timestamp; inserting a foreign `<script>` tag directly into the checkout page; hiding the loader inside a site's Google global-site-tag (`gtag.js`) block, between the real `gtag('js', ...)` and `gtag('config', ...)` calls, padded with roughly a hundred tab characters to push it past the right edge of a typical code-review view; using a discovered AWS access key to write the loader into the storage bucket behind the retailer's own CDN, so it loads from that trusted CDN host rather than a third-party domain; injecting the loader into a database content field (such as a product-description column) through an admin pod and relocating it to a file on the victim's own domain; adding it to a production front-end deployment as a Kubernetes `initContainer`; writing it into the cached page model of the checkout page; and a self-healing cron job placed in a JBoss log directory that checks the injected file's size every two minutes and re-appends the loader whenever a redeploy reverts it. One of the Hermes agent's skill files, in a section titled "Database Wipe After Extraction", instructs the agent: "after extracting and downloading all card data, wipe the source fields in batches" ([Gambit Security, 2026-09-22](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company)); at a second victim, a bicycle retailer, an overly broad table-name-matching cleanup step additionally dropped 180 staging and backup tables, including backups the victim's own administrators had separately made. This was collateral data loss from the attacker's own automated cleanup, not extortion. Some targets were not discovered by the agents at all: the operator handed at least two victims, a New Zealand retailer and a US photo printing company, to Hermes already holding a working administrator password, with the order to "get to work" ([Gambit Security, 2026-09-22](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company)). OpenRouter's account balance recorded $7,005.71 spent over four weeks by 25 August, and Gambit extrapolates from the later volume of model calls that the full cost was likely between $12,000 and $18,000; "the operator’s own cost review gives a similar figure, a mean of $25.46 over 101 completed scans, from $3.13 for the cheapest target to $79.31 for the most expensive" ([Gambit Security, 2026-09-22](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company)). Gambit states it "reached out to many of the affected organizations and took measures to take down the infrastructure discovered," crediting the Shadowserver Foundation, researcher Daniel Gordon, and other industry partners for their help notifying victims and taking down infrastructure ([Gambit Security, 2026-09-22](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company)).

Detection concept, telemetry class first: in web-server access logs, alert on SQL-error-pattern responses (`EXTRACTVALUE` or equivalent) to login-form parameters, and on image-upload requests whose stored file is later executed by the web server rather than served as static content; in host telemetry, alert on `sudo` invocations of an interpreter (`python3.12` or similar) by a low-privilege account with no corresponding change-management record; in network/mount telemetry, flag any host mounting an NFS export it has not mounted before, particularly where the export allows root-equivalent access; in cloud-audit telemetry, alert on a single principal enumerating or reading the entire contents of an AWS Secrets Manager instance in a short window; and in file-integrity or CDN-origin monitoring, treat any modification to a served JavaScript file's content (even with its timestamp preserved) or any script tag added to a checkout page outside a deployment window as high-priority. **Triage:** a legitimate deployment modifies checkout-page assets during a known release window with a corresponding commit and change record; the discriminators here are modification with no matching deployment event, a modification timestamp that has been deliberately restored to match the original file, or content padded with unusual whitespace specifically to evade a manual code read.

Hermes, the open-source NousResearch agent framework ([Unit 42, 2026-07-30](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/)), has appeared in three earlier, unrelated intrusions: an operation against Thailand's Ministry of Finance that Hunt.io links with low-to-medium confidence to a Chinese-speaking operator ([Hunt.io, 2026-07-23](https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent)); a Taiwan government intrusion Tenable assesses as most likely a state-adjacent contractor or patriotic-hacker operation, with state sponsorship a close runner-up ([Tenable, 2026-08-14](https://www.tenable.com/blog/the-agentic-ai-threat-cluster-seven-incidents-three-actors-and-what-they-mean)); and a Zhuhai-based, Chinese-speaking operator's campaign against more than 460 targets, including persistent targeting of a Malaysian government entity ([Unit 42, 2026-07-30](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/)). In three of the four intrusions the operators worked around model safety controls. In this campaign the operator added a skill to remove Hermes's own content-security filters ([Gambit Security, 2026-09-22](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company)). In Taiwan the agents reframed the operation as "authorized penetration testing" ([Tenable, 2026-08-14](https://www.tenable.com/blog/the-agentic-ai-threat-cluster-seven-incidents-three-actors-and-what-they-mean)). In the Unit 42 case the actor likely turned to DeepSeek, which Unit 42 describes as a model with minimal safety controls, after Western providers' controls limited it, and a framework-bundled jailbreaking skill was also installed ([Unit 42, 2026-07-30](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/)). That convergence, not any single victim in this campaign, is the transferable signal for a defender: an increasingly capable, freely available agent orchestration layer is now common tooling across financially motivated operators and government-targeting intrusions alike, regardless of how firmly any of them is ultimately attributed, and the underlying attack chain here (SQL injection, insecure OTP storage, unrestricted file upload, `sudo` misconfiguration, an over-permissive NFS export, and cloud-secrets exposure) is entirely composed of defects a Tier 2/3 team already reviews for in any custom-coded web application, Swiss public-sector portals included.

**Defender takeaway:** none of the individual flaws in this chain are novel; what changed is that an unattended, cheap AI agent can now find and chain them without an operator watching. A web-application security review that checks each of these six defect classes (injectable authentication parameters, plaintext OTP storage, unrestricted file upload, `sudo` NOPASSWD entries, NFS exports without root-squash, and cloud-secrets scope) closes the same door this campaign walked through, regardless of who or what is doing the walking.

## Update — 2026-09-25T04:30:00Z

Anthropic identified and banned the account linked to the attacks. The attacker used an earlier Claude model, Opus 4.6, and attempts on newer Claude releases were rejected ([Computing UK, 2026-09-23](https://www.computing.co.uk/news/2026/security/ai-agents-used-to-steal-credit-card-records)). Cloudflare separately confirmed it had shut down servers connected to the operation. Both actions had only marginal disruptive effect: "researchers said the attacker repeatedly rebuilt the infrastructure and continued the attacks" ([Computing UK, 2026-09-23](https://www.computing.co.uk/news/2026/security/ai-agents-used-to-steal-credit-card-records)). For defenders, the reinforced lesson is that model-provider account bans and infrastructure takedowns are reactive controls with a short disruption window against a campaign whose own operator economics, a mean cost of $25.46 per target, make rebuilding after a takedown cheap; the underlying web-application defect classes this campaign walks through remain the more durable point of intervention.

## Correction — 2026-09-30T06:56:13Z

Gambit's $12,000 to $18,000 spend is its own extrapolation from a $7,005.71 OpenRouter balance recorded on 25 August, not a billing total, and its report gives two skimmer counts: installations on the websites of five companies in its summary and confirmed skimmers on 19 of 27 named victims in its body ([Gambit Security, 2026-09-22](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company)). For the Fortune 500 hospitality company, the US airline, the industrial-supplies distributor and the fashion retailer, Gambit reports some level of access to their assets, not compromise ranging from partial to full ([Gambit Security, 2026-09-22](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company)). Operators worked around model safety controls in three of the four Hermes intrusions, not all of them, and in the Unit 42 case the reported route is the choice of a permissive model ([Unit 42, 2026-07-30](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/); [Tenable, 2026-08-14](https://www.tenable.com/blog/the-agentic-ai-threat-cluster-seven-incidents-three-actors-and-what-they-mean)).
