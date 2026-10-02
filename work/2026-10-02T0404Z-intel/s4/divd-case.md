---
title: DIVD-2026-00015 - Vulnerabilities in Zammad during investigation of case DIVD-2026-00014
author: Victor Pasman
url: https://csirt.divd.nl/cases/DIVD-2026-00015/
hostname: divd.nl
description: Multiple vulnerabilities found in Zammad including a Undisclosed RCE in Zammad version higher then 6.3 and a Undisclosed LPE in Zammad v1.5.0 to v7.1.0-alpha.
sitename: DIVD CSIRT
date: "2026-10-01"
---
# DIVD-2026-00015 - Vulnerabilities in Zammad during investigation of case DIVD-2026-00014

| Our reference | [DIVD-2026-00015](https://csirt.divd.nl/cases/DIVD-2026-00015) | 
| Case lead | [Victor Pasman](https://www.divd.nl/who-we-are/team/people/victor-pasman/) | 
| Researcher(s) | Earth Grob (Merlon Security) Luke Paris (Merlon Security) Tijmen van der Spijk (Merlon Security) Zohar Cochavi (Merlon Security) Alje Woltjer (Merlon Security) Mischa Rick van Geelen (DIVD) Ralph Horn (DIVD) Max van der Horst (DIVD) Frank Breedijk (DIVD) Davy Aarts (DIVD) | 
| CVE(s) |  | 
| Products | Zammad | 
| Versions | Zammad versions 6.3.0 to 6.5.4 for the RCE in Zammad. Zammad version 7.0.0 to version 7.1.3 for the RCE in Zammad, not exploitable due to environments conditions. Zammad version v1.5.0 to v7.1.0-alpha for the LPE vulnerability. | 
| Recommendation | Upgrade to Zammad version 7. | 
| Patch status | Available | 
| Workaround | N/A | 
| Status | Open | 
| Last modified | 01 Oct 2026 13:27 CEST | 

## Summary

During the investigation of case DIVD-2026-00014, two new CVEs were identified.

- CVE-2026-102489 - Zammad versions 6.3.0 to 6.5.4 are vulnerable a session hijack vulnerability that leads to remote code execution as the zammad user. The vulnerability is also present in version 7.0.0 to version 7.1.3, but not exploitable due to environment conditions.
- CVE-2026-102490 - In all versions of Zammad including the latest alpha has an vulnerability which enables the local zammad user to escalate privileges to root.

## What you can do

We advise all users of Zammad to upgrade to version 7 of Zammad or to take it offline. If you want to investigate whether you have been compromised based on our IoCs, you can download our [log check script](https://csirt.divd.nl/downloads/DIVD-2026-00015/cve-2026-102489_ioc_check_script_v2.sh) to check your Zammad logfiles for Indicators of Compromise.

## What we are doing

DIVD is actively scanning and alerting owners of vulnerable Zammad instances. We have reported the vulnerability to Zammad who are working on a fix.

## Timeline

| Date | Description | 
|---|---|
| 21 Sep 2026 | Vulnerability abused to breach DIVD | 
| 22 Sep 2026- 23 Sep 2026 | Vulnerability analysed and reproduced by DIVD team | 
| 24 Sep 2026 | Vulnerability reported to Zammad. | 
| 26 Sep 2026 | DIVD scanned for publicly available and vulnerable Zammad instances. | 
| 26 Sep 2026 | DIVD created a limited disclosure for CVE-2026-102489 & CVE-2026-102490. | 
| 26 Sep 2026 | DIVD started notifying owners of vulnerable instances. | 

	gantt
	    title DIVD-2026-00015 - Vulnerabilities in Zammad during investigation of case DIVD-2026-00014
	    dateFormat  YYYY-MM-DD
	    axisFormat  %e %b %Y
	    section Case
	    DIVD-2026-00015 - Vulnerabilities in Zammad during investigation of case DIVD-2026-00014 (still open)           :2026-09-24, 2026-10-08
	    section Events
		Vulnerability abused to breach DIVD :  milestone, 2026-09-21, 0d
				Vulnerability analysed and reproduced by DIVD team (1 days) : 2026-09-22, 2026-09-23
					Vulnerability reported to Zammad. :  milestone, 2026-09-24, 0d
				DIVD scanned for publicly available and vulnerable Zammad instances. :  milestone, 2026-09-26, 0d
				DIVD created a limited disclosure for CVE-2026-102489 & CVE-2026-102490. :  milestone, 2026-09-26, 0d
				DIVD started notifying owners of vulnerable instances. :  milestone, 2026-09-26, 0d
