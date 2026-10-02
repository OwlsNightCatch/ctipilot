---
title: Rogue Agents Investigation — Asymmetric Security
url: https://www.asymmetricsecurity.com/newsroom/rogue-agents-investigation/
hostname: asymmetricsecurity.com
description: Our team spent 48 hours investigating reported rogue OpenAI agent activity that targeted the Australian government and other organizations, using only publicly available data.
sitename: Asymmetric Security
date: "2026-10-01"
---
# Rogue Agents Investigation

Last weekend, our team spent 48 hours investigating reported rogue OpenAI agent activity that targeted the Australian government and other organizations between March and September this year, using only publicly available data.

We found successful access to staging environments; evidence of the use of attacker reconnaissance tactics; and evidence of probing a broader set of websites, including those of the CDC, SEC, International Energy Agency, and Mayo Clinic.

We also uncovered novel tactics that enabled agents to gain full web access despite the constraints of their sandbox. Some of these tactics left records erased or inaccessible, making it impossible to rule out access to sensitive data based on public information alone.

You can access a limited portion of our dataset
[here](https://www.asymmetricsecurity.com/media/asymmetric-urlquery-reports-2026-09-26.zip).

## What were the agents doing?

The activity suggests that the agents were originally tasked with researching public health and
other data, possibly as part of an evaluation. We found evidence of searches for health and
prescription statistics from the Australian Institute of Health and Welfare (AIHW); trade figures
from the UN’s Trade and Development Body (UNCTAD); and university statistics from Data USA. When the
agents struggled to retrieve information, they used external services to circumvent the intended
limitations of their sandbox.[1](https://www.asymmetricsecurity.com#user-content-fn-1)

The activity extended beyond searching for information. The records show attempts to find exposed configuration files, create accounts, route requests through third-party services, and retrieve results through unintended channels. These tactics extend agents’ capabilities and highlight gaps in our forensic evidence.

### Mimicking web browser functionality

The agents worked around these limitations by using public web services to access websites on their
behalf. One technique combined two public services, httpbin and urlquery.[2](https://www.asymmetricsecurity.com#user-content-fn-2)

- [Httpbin](https://httpbin.org/) is a service developers use to test how their software
communicates with websites. It can turn content embedded in a specially formatted link into a web
page. The agents used this feature to create pages containing their own code without hosting a
website themselves.
- [Urlquery](https://urlquery.net/) opens submitted links in a browser and records what happens,
including the page’s title, an image of the page and the web addresses the browser contacts. It
makes public scan reports available to read and search. This meant agents could use the service
both to run their code and to retrieve the results afterwards.

The sequence of agent activity worked like this:

- The agents wrote a small program to request information from another website.
- They embedded the program in a web page and created an httpbin link that returned the page when opened.
- They had urlquery open the link. Its browser loaded the page and ran the program.
- The program copied the retrieved information into something urlquery recorded, for example, the page title (the text shown on a browser tab title).
- The agents could then retrieve the urlquery report and read the recorded information.

In summary: httpbin served the page, urlquery provided the browser, and the urlquery report returned the results. By combining these services with their fetch tool, the agents mimicked a full web browser.

### Reconnaissance

Alongside ordinary research requests, we found evidence of the use of attacker reconnaissance tactics: probes for exposed files that could reveal non-public information.

For example, archived
[requests](https://arquivo.pt/noFrame/replay/20260619194409id_/https://climatereanalyzer.org/research_tools/monthly_tseries/.git/config)
to Climate Reanalyzer targeted Git repository<sup>[3](https://www.asymmetricsecurity.com#user-content-fn-3)</sup> files (`.git/HEAD` and `.git/config`) and a
[backup copy](https://arquivo.pt/noFrame/replay/20260619131223id_/https://climatereanalyzer.org/research_tools/monthly_tseries/tseries_ajax.php.bak)
of a server-side script. We found evidence of these attempts, but none that they succeeded.

We also examined a SQL-injection
[attempt](https://arquivo.pt/noFrame/replay/20260617112600id_/https://civilrightsdata.ed.gov/api/v1.0/GetStateEstimation?survey_Year_Key=9&Measure_Id=1&State_Id=1%20OR%201=1)<sup>[4](https://www.asymmetricsecurity.com#user-content-fn-4)</sup>
against the U.S. Department of Education’s Civil Rights Data API, previously reported by
[Transluce](https://x.com/TransluceAI/status/2103718083709829557). On June 17, archived requests
tested different requests ending with `State_Id=1 OR 1=1`. If interpreted as SQL, this condition
(`1=1`) is always true and could make the database return rows beyond the intended filter. We did
not verify successful SQL injections or extraction of additional records, only attempts.

### Accessing pre-production staging environments

The records also show access to pre-production staging environments, including AIHW’s
[pre-production system](https://urlquery.net/report/596d7f21-9030-404e-a432-f6810151dbef); some of
these requests returned data. As far as we know, this data was all publicly available.

*Pseudocode: we understand pp.aihw.gov.au is the pre-production system for AIHW and
AIHW-HWE-098-PBS-ATC1-prescriptions-monthly-data.xlsx (public data) was queried.*

We saw similar activity targeting pre-production or staging environments for
[Data USA](https://urlquery.net/report/df77bf50-3c00-4bef-8bd0-5fa74f8f4619),
[IHME](https://urlquery.net/report/0ac3d9bc-c4d0-437a-958b-10575ffe61cb), and
[UNCTAD](https://arquivo.pt/noFrame/replay/20260423113925id_/https://unctadstat-api-dev.uat-unctad.org/api/reportMetadata/US.PCI/en).

### Obtaining accounts and additional capabilities

Agents attempted to create accounts with disposable email services, browser platforms, and scanning services that could support further activity. Temporary mailboxes could receive registration and verification emails, while scanning-service accounts could unlock additional features.

Beginning on June 14, records show account-creation or login attempts involving Mail.tm, Boomlify,
Browserless, and urlquery. Some email addresses submitted during these attempts contained likely
task-related abbreviations:
“[aihw](https://urlquery.net/report/41806a91-7ce0-48f8-9109-48598a589211)” for the Australian
Institute of Health and Welfare or
“[pbs](https://urlquery.net/report/21496fb6-c771-4099-b83d-b2aca5dc47eb)” for the Pharmaceutical
Benefits Scheme.

On June 19, a sign-up [request](https://urlquery.net/report/5c68d39a-ead9-4b9f-bb19-2ca0c84d2fdb)
using an AIHW-prefixed disposable-email address (`aihw1781871989@web-library.net`) was rejected
because the email domain was not allowed. Approximately 16 minutes later, another
[request](https://urlquery.net/report/41806a91-7ce0-48f8-9109-48598a589211) using an AIHW-prefixed
Gmail address (`aihw1781872244@gmail.com`<sup>[5](https://www.asymmetricsecurity.com#user-content-fn-5)</sup>) was consistent with successful registration (and
quickly evolving tactics).

Previous reports by others focus on public use of urlquery as a means by which these agents accessed the web. Our team found evidence that, over time, the agents switched from only the public use of urlquery to the creation of private accounts which could hide their search activity and data access. We see the first private account creation attempt on June 14, and the first successful account creation on June 18.

On June 20, the [records](https://urlquery.net/report/ee1e2595-a6d4-4f33-92a7-ca33f32a3d2f) also
show the creation of a Boomlify mailbox set to expire 48 hours later. Its scheduled expiry makes
associated communications unavailable for later investigation.

The possibility of private scans, together with temporary-mailbox expiry, limits what can be reconstructed from public records. It is thus impossible, based on public data alone, to definitively establish that no sensitive data was accessed. These records alone do not establish whether the account-registration attempts were intended to conceal activity (this analysis would require full model transcripts).

### Retrieving results through notifications and archives

Once code ran in a remote browser, the agents needed a way to pull down the data. In addition to placing results in scan reports, they used web archives and notification services as creative ways to exfiltrate data through third-party services.

#### Web archives

Arquivo.pt’s “Save Page Now” service can load a submitted web page and archive responses to requests made during the visit. BOCSAR archive records show agents using this process on June 21:

- The
[archive](https://arquivo.pt/wayback/20260621030909id_/https://crimetool.bocsar.nsw.gov.au/search/_count?collections=x&nonce=abc999) captured several requests to the Crime Mapping Tool with different query parameters.
- It preserved a response for later retrieval through a replay URL – a link to the archived response.

Our sample recovered a roughly 22 MB JSON response associated with this sequence. Inspection of the recovered material revealed statistical collections labelled “incident-count,” “victim-count,” and “offender-count,” alongside map tiles and schemas.

#### Notification services

Another tactic we [observed](https://urlquery.net/report/00797720-0730-4736-8e62-dab337425d62) was
the use of a push-notification service called “ntfy.” We observed agents using this service to pull
down data from AIHW’s mental-health-in-aged-care Tableau dashboard.

The sequence of agent activity worked like this:

- Agent submitted a URL containing a script to urlquery.
- The service urlquery opened a Tableau session through the proxy [seep.eu.org](http://seep.eu.org) .
- Script fetched the data needed to load the dashboard.
- Script compressed that response into a roughly 35 KB gzip file.
- Script uploaded the file to an ntfy topic as `boot.gz` .

The report records the upload request, but we could not recover the uploaded file to determine its
contents. ntfy’s [documented](https://docs.ntfy.sh/config/#message-cache) defaults retain messages
for 12 hours. The agents may have used ntfy because they could not download the data directly with
their available tools.

## Reflections on the investigation

This investigation highlighted some interesting differences between tracking a swarm of AI agents and investigating traditional threat actor groups:

- **Rapid evolution of tactics.** There was a spike in activity targeting Australian entities
between June 16 and 21. During this period, the agents rapidly cycled through tools and tactics.
For traditional threat actors this type of technique evolution happens over months or years; the
evolution of agent techniques was compressed into just days.
- **Fewer patterns.** The bursts of activity resembled the surges that can follow disclosure of a
major vulnerability. However, because the agents’ varied approaches produced a more varied set of
indicators, activity was harder to recognise and cluster.
- **Agents need to overcome more constraints.** Traditional investigations often focus on attempts
to breach a target’s defences. Here, there was an additional boundary to investigate: agents
circumventing restrictions in their own operating environment to gain the affordances needed to
act against a target. The attack chain therefore included both overcoming the agent’s constraints
and probing the target’s controls.
- **Constraints led to creativity.** Limited web access helped explain the elaborate chains of
public services used to execute code and retrieve results. Some of this apparent sophistication
came from attempts to overcome restrictions in their environment, constraints that a threat actor
controlling their own tooling would not necessarily face.
- **Alien motivations.** The activity we observed looked like it stemmed from innocent tasks which
then evolved into problematic activity, such as unauthorized account creation, bypassing
restrictions, and relaying data through third parties. Unlike investigations where a malicious
objective is apparent from the outset, our digital forensics team had to link traditional
threat-actor tactics to seemingly innocent goals.

## Further work

Further investigation could draw on evidence unavailable to our team to help establish what the agents did and why. Relevant sources include:

- Full model transcripts, including tool calls and chain of thought – investigators with access to these should analyse if the agents were deliberately using the tactics described above to cover their tracks.
- Additional records held by services the agents used, including urlquery and httpbin.
- Internal logs from targeted organizations, including records of requests received by their web servers.

## Footnotes

1. 
We do not know the exact details of the tools or restrictions available to every agent. A limited fetch tool is one possible explanation for these workarounds, but some observed activity suggests access to a shell and a web server. Remote browsers could still provide useful capabilities, such as rendering interactive dashboards or making requests from a different network location. [↩](https://www.asymmetricsecurity.com#user-content-fnref-1)
2. 
Additional sources such as [urlscan](https://urlscan.io/) and[httpbun](https://httpbun.com/) were also used to serve similar purposes.[↩](https://www.asymmetricsecurity.com#user-content-fnref-2)
3. 
Historical example: [EMERALDWHALE](https://www.sysdig.com/blog/emeraldwhale) investigation
documented exposed Git configurations leading to credential theft.[↩](https://www.asymmetricsecurity.com#user-content-fnref-3)
4. 
[SQL injection](https://wstg.owasp.org/latest/4-Web_Application_Security_Testing/07-Injection/05-SQL_Injection/) attempts to make an application interpret supplied input as database instructions.[↩](https://www.asymmetricsecurity.com#user-content-fnref-4)
5. 
We [confirmed](http://email-checker.net/) on 30 September 2026 that this email address does not
exist. Our own testing showed that urlquery allowed registration with a non-existent address and
permitted private scans without email verification. The agents therefore had no need to create
or control a Gmail mailbox to use this route. This is unsurprising: Gmail account creation is
protected by significant anti-bot controls, so an unverified sign-up path would have been the
easier option.[↩](https://www.asymmetricsecurity.com#user-content-fnref-5)
