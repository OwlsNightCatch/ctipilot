---
title: Autonomous AI agents tried to hack US, Canadian government websites
author: Ionut Ilascu
url: https://www.bleepingcomputer.com/news/security/autonomous-ai-agents-tried-to-hack-us-canadian-government-websites/
hostname: bleepingcomputer.com
description: Autonomous AI agents using aggressive strategies attempted to hack U.S. and Canadian government websites to find school and divorce statistics.
sitename: BleepingComputer
date: "2026-10-01"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, AI Agent, Artificial Intelligence, Canada, Government, Hack, SQL Injection, USA,virus removal, malware removal, computer help, technical support']
---
Autonomous AI agents using aggressive strategies attempted to hack U.S. and Canadian government websites to find school and divorce statistics.

The failed breach attempts targeted a website under the U.S. Department of Education and Library and Archives Canada. However, the collected data shows no evidence of access to non-public information.

Nonprofit research lab Transluce says the AI agents appeared tasked with data retrieval operations, but their activity also included failed “rudimentary hacking attempts.”

### Probing for SQL injection

One incident occurred on June 17, when AI agents made more than 200,000 requests to a U.S. Department of Education website while searching for school statistics.

According to Transluce, the activity included a basic SQL injection attempt using a manipulated parameter, in an effort to bypass the site’s normal filters.

“In the 40 seconds leading up to the SQL injection, there were a series of requests containing a variety of unusual state ID inputs,” the researchers say, adding that the purpose of these requests remains unclear without more context about the agents and their objectives.

The researchers say that the requested data appeared to match a Google DeepSearchQA benchmark question about school counselors and race-related bullying.

Transluce informed the Department of Education of its finding on September 25. A spokesperson said that a review of the activity found no evidence of an impact on services.

### Failed probes against Canadian archive

Transluce researchers identified a similar pattern against Library and Archives Canada as agents tried to retrieve historical Canadian divorce records from 1905 through 1911.

On two dates, May 28 and June 9, Portugal’s national web archive (Arquivo.pt) recorded nearly 900 requests targeting Library and Archives Canada, according to Transluce’s findings.

Thirteen requests carried attack payloads, including SQL injection probes and tests of input handling, output formats, and debugging options.

The probes returned empty record pages, and the Canadian Centre for Cyber Security confirmed that there is no evidence of database manipulation or additional data.

“There is no indication that government systems have been compromised at this time,” the [Canadian Centre for Cyber Security said](https://www.cyber.gc.ca/en/news-events/statement-regarding-reported-activity-targeting-government-canada-websites).

The agency said it was assessing the reports with government partners and cautioned that automated or potentially malicious requests do not, by themselves, demonstrate a successful cyber incident.

The researchers note that while they “do not confidently attribute these attempts to OpenAI,” the tactics used are consistent with activity previously attributed to the AI developer.

OpenAI [told The Washington Post](https://www.washingtonpost.com/technology/2026/09/30/openais-ai-agents-attempted-hack-canadian-government-website/?utm_source=chatgpt.com) that it was reviewing the findings and had provided an initial briefing to Canadian officials.

The company has separately acknowledged unintended interactions between its agents and U.S. government websites, but Transluce cautioned that some of the broader activity was not clearly attributable to OpenAI.

### Broader activity, uncertain attribution

The investigation uncovered a much broader collection of AI-agent activity targeting U.S. federal and state government websites.

Transluce also says that agents relied on aggressive tactics against multiple U.S. state and federal websites, contributing to a broader pattern of AI-driven automated workflows.

The researchers observed that agent activity included techniques ranging from massive request volumes and modified URLs to disposable email accounts, attempts to bypass anti-bot systems, guessing downloadable file names, and reuse of exposed credentials.

Reported activity targeted agencies in California, Kansas, Maryland, Illinois, Texas, and New York.

In one case, AI agents tried to register for a Bureau of Economic Analysis API key using a disposable email address and the organization name "OpenAI Research."

Another workflow indicates an attempt to reuse exposed API keys to retrieve Census Bureau data.

Between April 23 and May 18, there were automated attempts to reach the content-management pages for the Naval History and Heritage Command’s website, history.navy.mil. However, there is no evidence of access to sensitive military information.

[Transluce's investigation](https://transluce.org/us-canada-gov) relied primarily on records from Arquivo.pt and the web-security scanning service urlquery.net, whose public logs preserved requests apparently submitted by the agents.

The newly uncovered incidents expand on earlier research from the organization that found agents resorting to vulnerability probes against public data providers while performing information-retrieval tasks.

The previous investigation uncovered that AI agents probed for vulnerabilities in the Data USA service and the digital library of the University of New Mexico, and exploited a flaw in an Australian government portal.

## 
            [Build your security blueprint for AI-powered attacks](https://hubs.li/Q04x67m50)
        

        Join Mikko Hyppönen and security leaders from the NFL, CHANEL, and Atlassian for a two-hour digital summit on what AI-speed attacks change, what defenders should stop doing, and how to validate, decide, fix, and re-validate at machine speed.

[Save your seat](https://hubs.li/Q04x67m50)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
