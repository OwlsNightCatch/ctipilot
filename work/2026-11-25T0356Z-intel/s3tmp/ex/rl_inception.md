---
title: "Threat Researcher’s Notebook: SSO Vishing Campaign Associated with Emerging “Inception” Extortion Group"
author: Robert Simmons
url: https://www.reversinglabs.com/blog/threat-researchers-notebook-sso-vishing-campaign-associated-with-emerging-inception-extortion-group
hostname: reversinglabs.com
description: Software Supply Chain Security, Threat Intelligence, and Threat Analysis Solutions
sitename: ReversingLabs
date: "2026-11-23"
tags: ['Threat Research']
fingerprint: f200a6d34210e781
language: en
image: https://www.reversinglabs.com/api/media/file/Blog-Cover-Inception-1400x732.jpg
pagetype: website
filedate: "2026-11-25"
---
### Spectra Assure Free Trial

Get your 14-day free trial of Spectra Assure for Software Supply Chain Security

[Get Free Trial](https://www.reversinglabs.com/software-supply-chain-security-free-trial)

[More about Spectra Assure Free Trial](https://www.reversinglabs.com/software-supply-chain-security-free-trial)

LinkedIn

Highlights

- **Out-of-band vishing bypasses traditional email security**: The Inception extortion group has avoided standard email lures entirely, relying instead on phone-based social engineering and strictly web-only, legal-themed domains, purposely registered without MX, DKIM, or DMARC records, to compromise single sign-on (SSO) credentials.
- **Dynamic SSO kits mimic exact authentication tenants**: Analyzing 21 confirmed malicious domains revealed a highly filtered phishing kit that tailors landing pages to a target's specific identity provider: either Okta or NetIQ.
- **Infrastructure pivots expose the true scale of operations**: While Inception publicly claims only seven victim organizations on its Tor leak site, ReversingLabs leveraged shared Cloudflare nameservers and rapid evening registration patterns to uncover dozens of additional high-confidence corporate targets.
- **Protecting the identity layer requires phishing-resistant controls**: Because this campaign targets the human element, organizations should implement FIDO2 security keys, passkeys, or origin-bound authenticators.

In mid-November 2026, a newly emerged data-extortion group calling itself Inception surfaced on a Tor leak site and initially claimed five major United States organizations as victims, specifically Advanced Micro Devices, Cigna Healthcare, Henry Schein, Paychex, and PepsiCo, before most recently adding AutoZone and Lucid Motors to bring its total claimed victim count to seven. A ReversingLabs technical investigation links these extortion claims to a targeted single sign-on vishing campaign active since late October 2026 that relies on dozens of deceptive domains disguised with a legal theme. Registered in rapid evening batches and shielded behind Cloudflare, these web-only domains deploy a filtered kit that delivers tailored content to intended victims while routing visitors it is not configured to attack to the targeted organization's legitimate Okta or NetIQ sign-in flow. Shared infrastructure pivots reveal dozens of additional corporate targets that have not yet appeared on the leak site. Organizations should enforce phishing-resistant authentication, monitor for brand-themed legal domain registrations, and audit identity provider logs for anomalous sign-in activity.

Inception’s extortion operations became publicly visible on November 17, 2026, when the ransomware.live tracker indexed the group alongside its Tor data-leak site (incptbug3ziqym4rhgsj7h7hbpzt3v4ympcf42gsdb5haqq237fziaad\[.\]onion). That morning, the operators published their initial wave of five claimed victims: Advanced Micro Devices (AMD), Cigna Healthcare, Henry Schein, Paychex, and PepsiCo. The group expanded its leak site days later, listing AutoZone on November 19 and Lucid Motors on November 21, bringing the list to seven organizations. These listings represent unverified claims made by the adversary rather than independently confirmed breaches. Notably, the corresponding lure domains for these targets were registered between three and 20 days prior to their appearance on the leak site, pointing to a compressed timeline from initial infrastructure staging to public extortion. Rather than relying on traditional email lures, this operation is using voice phishing (vishing) to compromise single sign-on (SSO) credentials. Technical analysis of the adversary's domain infrastructure directly corroborates this out-of-band delivery model. None of the legal-themed lure domains tied to the campaign possess MX records, DKIM, DMARC, or any other email-related DNS configurations. Built strictly to serve web traffic, these domains cannot receive email, confirming that the operators bypass email security controls altogether and direct targets to lookalike login portals over the phone. The following figure shows the ten domain IOCs detected by ReversingLabs that correspond to victims published on the adversary’s leak site and graphed with respect to one another via the Diamond Model.

*Figure 1: Diamond Model graph of domains detected as relating to Victim organizations.*

A technical analysis by ReversingLabs of the campaign reveals twenty-one domains with direct evidence of the SSO phishing kit. These domains were identified through a combination of registration behavior and active DNS patterns. By analyzing the response content of these domains, we can link them to the phishing kit’s capabilities.

The core of this campaign relies on tailoring the landing page to the specific identity provider of the target. All the domains in the confirmed cluster are configured to filter unwanted visitors and forward them to the victim’s legitimate authentication infrastructure.

For the vast majority of the targets, this involved forwarding visitors to the organization's unique Okta tenant, such as amd.okta\[.\]com or pepsico.okta\[.\]com. In one specific case, legal-vrtx\[.\]com was observed loading the Okta sign-in widget directly.

This customization is not limited to Okta. The domain legal-lucidmotors\[.\]com diverted from the Okta pattern, sending users to a NetIQ and OpenText Access Manager sign-in path instead. This shows the adversary is actively researching their targets and adjusting their kit to copy whatever SSO platform each organization uses. The following figure shows the branded Okta and NetIQ infrastructure detected in the response content of this cluster of domains.

*Figure 2: SSO providers’ infrastructure detected in this campaign.*

Beyond the on-page behavior, these domains are linked by highly consistent patterns in registration and hosting. The bulk of the domains were registered through the NICENIC registrar, where they repeatedly utilized three specific registrant location pairs in the WHOIS data. These location pairs include North Carolina, Chile, and Bermuda. This exact registration profile directly matches the domains used for the publicly named extortion victims, establishing a firm infrastructure link between the known victims and these newly discovered targets.

*Figure 3: NICENIC registrant profiles used by this adversary.*

The operational timing further confirms a single, coordinated adversary. Every domain in this set was registered within a specific evening window between 18:00 and 00:59 UTC, with a significant cluster occurring during the 19:00 hour.

Immediately following registration, these domains moved to Cloudflare within minutes. They were staged across fifteen specific Cloudflare nameserver pairs which are probably on the same Cloudflare account. Shared nameserver pairs tightly bind the dataset together. For example, the malavika/pedro nameserver pair hosted the victim-related Cigna and Henry Schein domains alongside Duolingo, Morningstar, Western Union, Dropbox, Indeed, and Vertex. Similarly, the emerie/louis pair served Activision Blizzard, Riot Games, Expeditors, Twitch, and Carvana. Before transitioning to Cloudflare, the domains frequently shared temporary DNS configurations or default registrar nameservers. After the active phase of the campaign, many of these domains were parked back on their registrar's default servers or suspended, leaving only a few active.

This infrastructure overlap, connecting the specific registration times, the repeating NICENIC WHOIS profiles, and the shared Cloudflare accounts, demonstrates that the confirmed lure domains and the known victim domains are almost certainly part of the same operational pipeline.

While NICENIC accounted for the majority of the confirmed infrastructure, the remaining five domains were distributed across three smaller registrar setups. Two victim-related domains, legal-paychex\[.\]com and legal-pepsico\[.\]com, were registered through NameSilo using a registrant profile located in Arizona within the United States. Another pair of lures, legal-aexp\[.\]com and legal-lvmh\[.\]com, were registered at Spaceship with a registrant profile based in Delaware. Finally, the adversary registered legal-creditkarma\[.\]com at Tucows by utilizing the privacy service Njalla. Despite the variation in registrars and geographic profiles, these five domains transitioned to the same identified Cloudflare nameserver pairs shortly after registration, tying them into the broader campaign.

While the confirmed domain cluster is anchored by active redirection data, a second tier of forty-one domains can be attributed with high confidence. These domains lack active SSO targeting evidence, but they map to the campaign’s established operational patterns. Every domain in this cluster adheres to the strict naming convention of pairing a single target brand with legal terminology, and none of them possess mail configurations, indicating they were staged for vishing.

The bulk of this cluster consists of twenty-nine domains registered through NICENIC that exactly match the suspicious WHOIS registrant location pairs, North Carolina, Chile, and Bermuda, identified in our earlier analysis. Upon registration, these domains moved to the cluster of Cloudflare nameserver pairs hosting the confirmed and victim-related infrastructure. For example, legal-colpipe\[.\]com (possibly Colonial Pipeline) and legal-reddit\[.\]com were staged on the malavika/pedro nameservers, while legal-nestle\[.\]com and legal-anthropic\[.\]com surfaced on magnolia/sean.

The remaining twelve domains were registered across the smaller registrar setups but are tied to the core operation through their shared Cloudflare nameserver pairs and registration timings. The adversary often registered multiple variations of a single brand's lure across different registrars within minutes of each other.

A prime example is the staging against Henry Schein, where the victim listed NICENIC domain legal-henryschein\[.\]com was registered at 19:28 UTC on November 8, 2026, followed just thirteen minutes later by the Spaceship registration of henryschein-legal\[.\]com. The next day, the adversary registered law-henryschein\[.\]com again by Spaceship. Similar rapid multi-registrar batches were observed targeting Verisk, iHeartMedia, Wynn Resorts, Nintendo, and Paramount, showing that these disparate registrar accounts are almost certainly operated by the same hand rather than copycats.

Furthermore, nine domains in this group, including those mimicking Starbucks, Ulta, Paramount, Warner Bros., Nintendo, NBCUniversal, Jones Day, and Alaska Airlines, according to domain HTTP response content, were observed forwarding visitors directly to the targets' legitimate, benign corporate websites. This mirroring of the benign redirection behavior seen in the confirmed cluster shows that the vishing kit’s filtering mechanics are similar, effectively routing unauthorized visitors away to hide the underlying SSO phishing pages. Based on these exhaustive infrastructure and behavioral overlaps, we assess these domains to almost certainly be staged Inception resources actively targeting these brands.

A final tier of four domains matches the legal naming convention used in higher confidence clusters, evening UTC registration window, lack of email DNS records, and established registrar profiles, but remains at medium confidence. Unlike higher-confidence lures, each domain spent only one to two days on an isolated Cloudflare nameserver pair hosting no other known campaign infrastructure and lacked direct identity-provider redirection evidence.

Three of these domains mirror the cross-registrar brand pairings seen elsewhere in the campaign. On October 26, 2026, the misspelled legal-wernerbros\[.\]com (Spaceship, Delaware profile) and legal-activisionblizzard\[.\]com (NameSilo, Arizona profile) were registered one minute apart, closely bracketing higher-confidence lures for both brands. Similarly, mcdonalds-legal\[.\]com was registered at Spaceship on November 17 roughly four hours after the high confidence NICENIC lure legal-mcdonalds\[.\]com. The fourth domain, legal-everpuredata\[.\]com, followed the campaign's Tucows and Njalla privacy registration workflow on October 26 and drew malicious phishing detections in ReversingLabs dataset, though its unshared Cloudflare pair and smaller target profile prevent firmer attribution.

Because this adversary targets the identity layer rather than endpoints, defenders must prioritize phishing-resistant authentication across all identity providers, enforcing FIDO2 security keys, passkeys, or origin-bound authenticators alongside managed device restrictions and alerts for unexpected MFA changes. Since these web-only lures bypass traditional email security through phone-based social engineering, organizations should brief employees and IT help desks to reject urgent legal or compliance sign-in requests on unfamiliar domains and require strict identity verification before processing credential or MFA resets. Security teams should also monitor newly registered domains and certificate transparency logs for brand-themed legal naming patterns staged in evening UTC windows, blocking suspicious domains immediately at DNS and web proxies. Finally, defenders should hunt across DNS, proxy, and identity provider logs from October 21, 2026 onward for lookups to these indicators, cross-origin SSO referrers, or anomalous post-authentication activity, revoking active sessions and resetting credentials immediately if targeted activity is confirmed.

**legal-duolingo\[.\]com**

**activisionblizzard-legal\[.\]com**

**legal-morningstar\[.\]com**

**legal-westernunion\[.\]com**

**legal-ea\[.\]com**

**legal-dropbox\[.\]com**

**legal-riotgames\[.\]com**

**legal-indeed\[.\]com**

**legal-creditkarma\[.\]com**

**legal-vrtx\[.\]com**

**legal-aexp\[.\]com**

**legal-expeditors\[.\]com**

**legal-twitch\[.\]tv**

**legal-lvmh\[.\]com**

**legal-amd\[.\]com**

**legal-carvana\[.\]com**

**legal-pepsico\[.\]com**

**legal-caesars\[.\]com**

**legal-rbi\[.\]com**

**legal-grubhub\[.\]com**

**legal-lucidmotors\[.\]com**

**NOTE: this cluster is a victim-mapping subset intentionally overlapping with confidence**

**legal-cigna\[.\]com**

**legal-paychex\[.\]com**

**legal-henryschein\[.\]com**

**henryschein-legal\[.\]com**

**law-henryschein\[.\]com**

**legal-lucid\[.\]com**

**legal-lucidmotors\[.\]com**

**legal-autozone\[.\]com**

**legal-amd\[.\]com**

**legal-pepsico\[.\]com**

**paramount\[.\]legal**

**legal-starbucks\[.\]com**

**legal-nbcuniversal\[.\]com**

**legal-alaskaair\[.\]com**

**warnerbros-legal\[.\]com**

**legal-mcdonalds\[.\]com**

**iheartmedia-legal\[.\]com**

**verisk-law\[.\]com**

**legal-jcpenney\[.\]com**

**legal-mtb\[.\]com**

**legal-molinahealthcare\[.\]com**

**nintendo-legal\[.\]com**

**legal-anthropic\[.\]com**

**legal-tesla\[.\]com**

**legal-verisk\[.\]com**

**wynnresorts\[.\]legal**

**legal-colpipe\[.\]com**

**reddit-legal\[.\]com**

**legal-kfc\[.\]com**

**law-verisk\[.\]com**

**verisk-legal\[.\]com**

**legal-warnerbros\[.\]com**

**legaldept-amazon\[.\]com**

**legal-ssctech\[.\]com**

**legal-openai\[.\]com**

**legal-ulta\[.\]com**

**legal-nintendo\[.\]com**

**legal-nestle\[.\]com**

**legal-reddit\[.\]com**

**legal-delta\[.\]com**

**legal-nfl\[.\]com**

**legal-netflix\[.\]com**

**legal-arthrex\[.\]com**

**legal-paramount\[.\]com**

**legal-ubisoft\[.\]com**

**legal-adobe\[.\]com**

**legal-wynnresorts\[.\]com**

**legal-iheartmedia\[.\]com**

**legal-ml\[.\]com**

**legal-epicgames\[.\]com**

**legal-jonesday\[.\]com**

**legal-activisionblizzard\[.\]com**

**legal-everpuredata\[.\]com**

**legal-wernerbros\[.\]com**

**mcdonalds-legal\[.\]com**

Instagram

CISA's Java4Shell alert starts with a step most teams can't finish quickly: finding every Java runtime, including the ones vendors bundled for you.

Following ESET’s disclosure, ReversingLabs correlated CerealLoader samples across vendor names and file variants, identified additional loader candidates, and tested where common detection approaches fall short.

ReversingLabs analyzed 11 ARTEX fork-families across 3,147 unique hosting IP indicators (3,096 actionable after triage) and 184 operator binary samples spanning Linux, Windows, and macOS.
