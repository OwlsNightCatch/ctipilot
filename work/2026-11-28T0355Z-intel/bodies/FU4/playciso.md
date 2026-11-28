---
title: "SAP Cyberattack \"Project Granite\": What Is Known, What to Do"
author: Team PlayCISO
url: https://playciso.com/blog/sap-cyberattack-project-granite-github
hostname: playciso.com
description: SAP found suspicious activity on GitHub and reportedly replaced signing keys; no sign of customer data access. What is confirmed and what to do.
sitename: PlayCISO
date: "2026-11-27"
tags: ['news', 'sap', 'supply-chain', 'software-supply-chain', 'github', 'source-code', 'token-theft', 'agentic-ai', 'agentic-attacks', 'incident-response', 'vendor-risk', 'security-leadership']
fingerprint: "4542170bcc1b574c"
language: en
image: https://playciso.com/api/og?title=SAP%20Cyberattack%20%22Project%20Granite%22%3A%20What%20Is%20Known%2C%20What%20to%20Do&subtitle=news%20%C2%B7%20sap%20%C2%B7%20supply-chain
pagetype: article
filedate: "2026-11-28"
---
[All posts](https://playciso.com/blog)

# SAP Cyberattack "Project Granite": What Is Known, What to Do

[Team PlayCISO](https://playciso.com/about)· Updated Nov 28, 2026

[AI hacking frameworks hub](https://playciso.com/hubs/ai-hacking-frameworks)

## TL;DR · the short version

SAP is handling an active security incident that DER SPIEGEL, which broke the story on 26 November 2026, says is called "Project Granite" internally. SAP says it identified suspicious activity, immediately took measures to protect customers and the security of its services, and, at the current state of its investigation, has found no indication of unauthorized access to customer business data. It has not said what the activity was, when it was found or what was affected. An internal letter to staff, reported by dpa and heise, places the suspicious activity on GitHub, and Handelsblatt, citing company sources, reports that SAP restricted GitHub access, stopped automated development processes and replaced its signing keys; SAP has not confirmed those steps. SPIEGEL's insider sources say attackers stole SAP employees' authentication tokens and used them to change and copy SAP source code on GitHub, possibly with agentic AI; SAP has not confirmed those details. No source names the attacker, the repositories or any affected product, and no report says tampered code reached customers.

[Analyse token scopes](https://playciso.com/tools/github-token-scope-analyzer)

[https://www.t-online.de/digital/aktuelles/id\_101548548/sap-meldet-it-vorfall-haben-verdaechtige-aktivitaeten-identifiziert-.html](https://www.t-online.de/digital/aktuelles/id_101548548/sap-meldet-it-vorfall-haben-verdaechtige-aktivitaeten-identifiziert-.html)

**SAP** says it has identified suspicious activity and taken immediate steps to protect its customers, and that it has so far found **no indication of unauthorized access to customer business data**. DER SPIEGEL, which broke the story on **26 November 2026**, reports that the German software company is handling an active security incident it calls **"Project Granite"**, and that, according to insiders, attackers stole employees' login tokens and used them to change and copy SAP source code on GitHub. SAP has not confirmed those details.

## Confirmed vs not yet known

**Said by SAP** (via dpa and the dts news agency):

- SAP "immediately took the necessary measures to protect its customers and ensure the security of its services."
- "Based on the current state of our investigation, we have found no indication of unauthorized access to customer business data." (Our translations from German.)
- Security measures are being developed continuously.

**Reported by DER SPIEGEL, from unnamed sources, not confirmed by SAP:**

- The incident is called "Project Granite" internally, and an internal message told staff "SAP has identified suspicious activities".
- Attackers stole SAP employees' authentication tokens and used them to change and copy SAP source code on GitHub.
- The attackers went after SAP's GitHub presence "possibly by means of agentic AI" (dpa says its own sources confirm this).
- Per dpa's sources, staff were told to check whether they needed to act, for example by changing credentials.

**Reported since, not confirmed by SAP:**

- An internal letter told staff the suspicious activity was found on GitHub, SAP's platform for developer productivity and software delivery, and asked them to check whether they needed to act, for example by changing credentials (heise, with dpa).
- SAP restricted access to GitHub, stopped automated processes in software development and replaced its signing keys (Handelsblatt, citing sources within the company).

**Circulating but not found in the German reports:** some English write-ups say SAP gave developers an internal tool to scan their code for suspicious patterns and made signed commits mandatory. Neither appears in the Handelsblatt, heise or t-online articles we read on 28 November; treat both as unconfirmed.

**Not yet known:** when SAP found the activity; which repositories were touched and whether they were public or private; whether any changed code reached a package or product release; who the attacker is; whether any authority has been notified. The two agency reports also differ: dts says SAP confirmed the cyberattack when SPIEGEL asked, while dpa (via t-online) says SAP did not at first confirm a hacker attack in those words.

## Timeline

| Date | What happened | Source | 
|---|---|---|
| "Recent days" before 26 Nov 2026 | The incident causes "considerable agitation" inside SAP; staff receive an internal notice of suspicious activity. | DER SPIEGEL via [dts](https://www.it-fachportal.de/71002-sap-von-it-sicherheitsvorfall-betroffen/) | 
| 26 Nov 2026 | DER SPIEGEL reports the hacking attack, the "Project Granite" code name, token theft and GitHub source code changes, citing insiders. | DER SPIEGEL via [dts](https://www.it-fachportal.de/71002-sap-von-it-sicherheitsvorfall-betroffen/) | 
| 26-27 Nov 2026 | SAP says it took immediate measures and has found no indication of unauthorized access to customer business data so far. | [t-online / dpa](https://www.t-online.de/digital/aktuelles/id_101548548/sap-meldet-it-vorfall-haben-verdaechtige-aktivitaeten-identifiziert-.html), [dts](https://www.it-fachportal.de/71002-sap-von-it-sicherheitsvorfall-betroffen/) | 
| 27 Nov 2026 | heise, with dpa, reports SAP's internal letter placing the activity on GitHub; Handelsblatt reports restricted GitHub access, stopped automated development and replaced signing keys. | [heise](https://www.heise.de/news/IT-Vorfall-bei-SAP-Entwicklungssysteme-betroffen-11539973.html) | 
| 27 Nov 2026 | dpa says its own sources confirm the attackers targeted SAP's GitHub presence, possibly with agentic AI. | [t-online / dpa](https://www.t-online.de/digital/aktuelles/id_101548548/sap-meldet-it-vorfall-haben-verdaechtige-aktivitaeten-identifiziert-.html) | 

## Why a GitHub incident at SAP matters to SAP customers

SAP publishes source code for many of its products' open-source parts, SDKs and tools on GitHub, and some of it ships to customers through npm and other registries. If an attacker can change code in a vendor's repository with a stolen token, the question for every customer is whether that change could reach a build they install. SAP's statement covers customer business data; it does not yet say anything about code integrity. That is the gap to watch.

It is also a reminder of how often a token is the way in. In April 2026, heise reported that malicious versions of several SAP npm packages were published in the "Mini Shai-Hulud" supply-chain campaign, which harvested developer credentials including GitHub tokens. **No source links that campaign to Project Granite.**

## Useful next, if this was relevant to you

If SPIEGEL's sources are right that AI agents were involved, SAP joins a short list of organisations where AI agents are reported to have done part of an intrusion this year, from Hugging Face to the European Commission and Swiss critical infrastructure operators. We track every case, confirmed vs reported, on the [Hacked with AI agents timeline](https://playciso.com/hubs/ai-hacking-frameworks/timeline).

## What security leaders should do this week

- **Ask your SAP account team three questions in writing:** which repositories were affected, whether any changed code was published to a registry or release, and when SAP will publish its findings. Record the answers in your vendor file.
- **List the SAP code you pull from GitHub or npm** (for example CAP, Cloud SDK, UI5 tooling, build tools) and pin builds to versions published before late November 2026 until SAP gives an all-clear. Review any SAP dependency update merged since then.
- **Verify what you install, with the new keys.** If SAP replaced its signing keys, as Handelsblatt reports, treat anything signed with the old keys as suspect until SAP says otherwise, and update the keys your CI trusts when SAP publishes the new ones. Where SAP packages carry signatures or provenance, make CI check them; the [release integrity checklist](https://playciso.com/tools/github-release-integrity-checklist) covers what to look for.
- **Check your own exposure to the same technique.** Run the [token scope analyzer](https://playciso.com/tools/github-token-scope-analyzer) on the tokens your developers and CI hold, shorten their lifetimes, and make sure your [GitHub audit log](https://playciso.com/tools/github-audit-log-monitoring) would show a token used from a new place to push code.
- **Review SAP's access into your landscape.** Support connections, RFC users and integration credentials SAP or its partners hold should be ones you can rotate in an hour.
- **Brief the board in two lines:** SAP reports a security incident with no sign so far of customer business data being accessed; we are checking whether any SAP code we use could have been changed, and have asked SAP directly.

## Practise the decision

A key supplier says "no customer data affected" before it can say anything else. What do you ask, what do you pause, and when do you tell the board? The [Vendor Breach Lab](https://playciso.com/tools/vendor-breach-lab) walks through those choices; the [third-party breach response checklist](https://playciso.com/tools/third-party-breach-response-checklist) turns them into a list. SAP's vulnerability and incident history is tracked in the [Cyber Breach Index](https://playciso.com/breach-index/sap).

## FAQ

### Was SAP hacked?

SAP says it identified suspicious activity and "immediately took the necessary measures to protect its customers and ensure the security of its services" (per dpa). DER SPIEGEL, which broke the story on 26 November 2026, reports a hacking attack that SAP handles internally as an active security incident called "Project Granite". The dts news agency says SAP confirmed the cyberattack when SPIEGEL asked; dpa, via t-online, says SAP did not at first confirm a hacker attack in those words. SAP has not said what the activity was, when it found it or which areas were affected.

### Was SAP customer data stolen?

SAP says: "Based on the current state of our investigation, we have found no indication of unauthorized access to customer business data" (per t-online, our translation). That is a statement about the investigation so far, not a final finding. No source reports customer data being taken.

### What is Project Granite?

According to DER SPIEGEL, "Project Granite" is SAP's internal code name for the incident. SAP has not commented on the name.

### What has SAP done about the GitHub incident?

Handelsblatt, citing sources within the company, reports that SAP restricted access to GitHub, stopped automated processes in software development and replaced its signing keys. SAP itself has said only that it took the necessary measures immediately; it has not confirmed these specific steps. Replacing signing keys usually means only packages signed after the incident should be treated as genuine.

### Did tampered SAP code reach customers?

No report says so, and none rules it out. SAP's statement covers customer business data only ("no indication of unauthorized access"), not code integrity, and no source names an affected repository, package or product.

### Was SAP source code stolen from GitHub?

Not confirmed. DER SPIEGEL cites an insider who says attackers stole SAP employees' authentication tokens and used them to change and copy SAP source code on GitHub. SAP has not confirmed this, and no source names the repositories, says whether they were public or private, or says whether any changed code reached a release.

### Did attackers use AI agents against SAP?

SPIEGEL's internal sources say the attackers went after SAP's GitHub presence "possibly by means of agentic AI", and dpa says its own sources confirmed this. Nobody has said how AI was used or which tools. It fits a pattern other vendors have described this autumn (see our ARTEX coverage), but no source links this incident to ARTEX or to any named group.

### Do SAP customers need to do anything?

SAP has not issued customer instructions in the reports we read. Sensible steps: watch SAP's official channels and your account team for notices; list which SAP open-source libraries, SDKs and tools you pull from GitHub or npm and pin them to versions published before late November until SAP says more; and check that SAP connections into your landscape use credentials you can rotate quickly.

### Is this linked to the Mini Shai-Hulud npm attack on SAP packages?

No source links them. In April 2026 heise reported malicious versions of several SAP npm packages in the "Mini Shai-Hulud" supply-chain campaign, which stole developer credentials including GitHub tokens. The November reports do not mention it.

## Sources

- [SAP meldet IT-Vorfall: Haben "verdächtige Aktivitäten identifiziert"](https://www.t-online.de/digital/aktuelles/id_101548548/sap-meldet-it-vorfall-haben-verdaechtige-aktivitaeten-identifiziert-.html) (t-online, with dpa and the SPIEGEL advance report, 27 Nov 2026), SAP's statements
- [SAP: IT-Sicherheitsvorfall, "haben verdächtige Aktivitäten identifiziert"](https://www.handelsblatt.com/technik/ki/sap-it-sicherheitsvorfall-haben-verdaechtige-aktivitaeten-identifiziert/100273138.html) (Handelsblatt, Christof Kerkmann, 27 Nov 2026), Project Granite and SPIEGEL's token report
- [IT-Vorfall bei SAP: Entwicklungssysteme betroffen](https://www.heise.de/news/IT-Vorfall-bei-SAP-Entwicklungssysteme-betroffen-11539973.html) (heise online, 27 Nov 2026), the internal letter and Handelsblatt's report
- [SAP von IT-Sicherheitsvorfall betroffen](https://www.it-fachportal.de/71002-sap-von-it-sicherheitsvorfall-betroffen/) (dts Nachrichtenagentur via it-fachportal.de, 26 Nov 2026)
- DER SPIEGEL, original report (26 Nov 2026), as quoted by the two agency reports above
- [Malicious npm packages: SAP software compromised](https://heise.de/-11281020) (heise, April 2026), background only

Spotted an error? [Report an error](<mailto:hello@playciso.com?subject=Correction%3A%20SAP%20Cyberattack%20%22Project%20Granite%22%3A%20What%20Is%20Known%2C%20What%20to%20Do&body=Article%3A%20https%3A%2F%2Fplayciso.com%2Fblog%2Fsap-cyberattack-project-granite-github%0A%0AWhat%20is%20wrong%20(and%20a%20source%2C%20if%20you%20have%20one)%3A%0A>). A person reads every message.

[Analyse token scopes](https://playciso.com/tools/github-token-scope-analyzer)

[Microsoft agent-framework PyPI Hijack: What to Do Nowagent-framework 1.26.1 and 1.26.2 on PyPI stole cloud and CI secrets via a .pth file on 17 Nov 2026. What Wiz found, who is hit, how to check, pin 1.26.0.](https://playciso.com/blog/microsoft-agent-framework-pypi-esrp-compromise)

[ARTEX Docker Image Backdoor: Root Shell in Login, What to DoA Docker Hub copy of the ARTEX AI pentest tool hid a root shell in its login. Badbyte saw 62 exposed consoles. What is confirmed and what to do.](https://playciso.com/blog/artex-backdoored-docker-image-root-shell)

[OVHcloud CLI Compromise and the Release-Pipeline GapOVHcloud disclosed on 19 Oct 2026 that its CLI repo was briefly compromised (v0.11.0-v0.15.0). What happened and the pipeline controls to check.](https://playciso.com/blog/ovhcloud-cli-supply-chain-compromise-release-pipeline-integrity)
