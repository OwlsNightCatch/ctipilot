---
title: "Luna Moth Files: How Silent Ransom Group Operates - Check Point Blog"
author: Uriel Sigal; Security Researcher; Exposure Management Team
url: https://blog.checkpoint.com/security/how-luna-moth-runs-data-extortion-like-a-business/
hostname: checkpoint.com
description: An exposed archive attributed to Silent Ransom Group (Luna Moth) shows how a data extortion crew runs vishing, theft, and negotiation. See what it reveals.
sitename: Check Point Blog
date: "2026-10-09"
fingerprint: "57ad417df4d8240"
---
# How Luna Moth Runs Data Extortion Like a Business

**Uriel Sigal, Security Researcher, Exposure Management Team**

Around October 5, 2026, an anonymous onion site called “The Luna Moth Files” claimed to expose internal material from Silent Ransom Group (SRG), also tracked as Luna Moth and UNC3753. The package includes chat exports, a vishing document, screenshots, and a purported fake employee résumé.

Nobody knows who published it or how the archive was obtained, so we treat its claims as unverified unless independent sources back them up. The material contains no new exploit and no new malware. It does offer a view of how a social engineering-led extortion operation may organize its work.

### What was already known about Luna Moth

SRG is a financially motivated data extortion group that generally skips encryption. It persuades people to grant access, steals sensitive information, and pressures organizations to pay by threatening to publish or sell it.

Unit 42 documented the activity in 2022 as callback phishing. Personalized subscription invoices pointed recipients to attacker-controlled phone numbers, and the calls ended with victims starting remote support sessions using legitimate administration software.

Mandiant later described direct impersonation of a victim’s internal IT staff, using help desk or data migration pretexts, screen sharing, legitimate remote management tools, and consumer file-sharing services. The FBI has also reported people posing as IT personnel who tried to gain physical access after remote attempts failed.

### A service chain, not a lone caller

The chats describe a segmented operation. Target researchers and persona builders prepare business context. Callers establish authority and keep the victim engaged. Technical participants support remote sessions and data access. Negotiators and payment handlers manage monetization. The archive does not establish a formal hierarchy, but the division of labor holds across the material.

The vishing document shows how the roles connect. It tells the caller to monitor a separate group chat throughout the remote session and relay any change in the victim’s behavior. That implies a second operator working on the endpoint while the caller keeps the conversation calm. The chats also reference virtual servers intended for 3CX telephony.

In this workflow, the call acts as a control channel. It keeps the victim cooperative while access and data collection happen in parallel.

### Credibility is built before the first call

Early messages discuss long-lived domains, business email accounts, and simple commercial-looking websites. Other exchanges mention registration for commercial people-data services, followed by lists of senior personnel and requests to start calling.

The result is a caller who has researched the organization and holds an identity that survives basic scrutiny. The disclosed script then follows a deliberate arc of anxiety, reassurance, and renewed urgency, with remote access framed as a protective security check. This matches publicly documented Luna Moth behavior, and the new detail is how callers are coached to manage trust and resistance.

### A victim pipeline aimed at law firms

The chats show a commercial approach to victim management. Labels such as “CHAT,” “OFFER,” “CONTRACT,” and “GOLD” appear alongside revenue estimates, negotiation states, and requests for cryptocurrency wallets. Participants also refer repeatedly to the legal sector and an ambition to target the top 100 law firms globally.

Observed victimology supports that focus. Of the group’s 50 most recently observed victims, 42 were law firms. Across the broader dataset, Business Services accounts for 69 classifications, Finance for 22, and Real Estate for two.

### Beyond the phone

Discussions of recruitment, prospective agents, and a project called “Fake\_Employee” point to experiments with more durable human access. The site also lists a purported résumé sent to law firms and photographs it describes as field activity. These items fit the FBI’s reporting on physical access attempts.

The evidence is strongest for internal discussions and project concepts. It is weaker for the successful placement of fake employees or the identity and role of any individual shown.

### Reasons for caution

The site displays two different message totals, and its headline financial figure does not reconcile with the amounts in its own table. Claims about operator identities, confirmed payments, and deepfake use need independent corroboration. The archive is still detailed and consistent enough to offer a provisional view of the group’s operating model.

### What security teams can take from it

The central finding is organizational. Luna Moth’s edge appears to come from a repeatable process that turns researched identities and trusted business context into remote access, stolen data, and leverage. Controls aimed at malware alone will not interrupt that process.

Several practical steps follow from the workflow. Verify any inbound IT request through a separate, known channel before approving a remote session. Limit which remote access tools employees can install. Brief senior staff, especially at law firms and professional services companies, since senior personnel appear on the call lists. Monitor for lookalike domains and fabricated personas with [digital brand protection](https://cyberint.com/platform/digital-brand-protection/), and track attacker chatter and exposed personnel data through [deep and dark web monitoring](https://cyberint.com/platform/deep-dark-web-monitoring/).

If the archive is authentic, Luna Moth treats social engineering as a production process. Research creates credibility, callers convert it into access, technical operators turn access into stolen data, and negotiators turn that data into leverage. The group looks less like a conventional ransomware crew and more like a specialized data extortion business whose core platform is the coordinated manipulation of trust.

Want the full analysis? Read the complete report, including the reconstructed operating workflow and sector breakdown of observed victims. [Download “Inside the Luna Moth Files”](https://checkpoint.cyberint.com/hubfs/Social/Silent%20Ransom%20Group%20Report.pdf)

[Check Point Exposure Management](https://www.checkpoint.com/exposure-management/) brings attacker infrastructure, dark web chatter, brand impersonations, and internal telemetry into one continuously updated intelligence stream, so security teams can see how attacks unfold and act on what matters. [Explore Check Point Exposure Management Threat Intelligence](https://www.checkpoint.com/exposure-management/threat-intelligence/).
