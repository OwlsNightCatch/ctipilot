NOTE: this is the WebFetch tool's returned text for https://www.cisa.gov/news-events/alerts/2026/11/24/cisa-adds-three-known-exploited-vulnerabilities-catalog (cisa.gov is walled out of the container; `extract` fell through to exhausted jina keys). It is a summarised rendering, NOT the raw page body; only the strings it put inside double quotes are presented by the tool as verbatim page text and none could be confirmed against raw HTML.

**Title:** CISA Adds Three Known Exploited Vulnerabilities to Catalog
**Date:** November 24, 2026

- **CVE-2026-131914** Name as written: "Idunno AntiCsrf Deserialization of Untrusted Data Vulnerability"
- **CVE-2026-132165** Name as written: "Drupal Core Remote Code Execution Vulnerability"
- **CVE-2026-132224** Name as written: "Optimizely Web Experimentation External Control of Critical State Data Vulnerability"

Outbound (page-level body links): https://www.cve.org/CVERecord?id=CVE-2026-132224 ; https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://www.cisa.gov/known-exploited-vulnerabilities-catalog

Load-bearing quotes (verbatim per the tool):
1. Exploitation status (lead sentence, covers all three entries): "based on evidence of active exploitation"
2. BOD 26-04 requirement: "requires federal agencies to prioritize rapid remediation of high-risk vulnerabilities"
3. Forensic triage: "must check whether threat actors compromised the system before the patch was applied"

BOD 26-04 title as written: "Binding Operational Directive (BOD) 26-04: Prioritizing Security Updates Based on Risk"
Page has no standalone sentence about Optimizely beyond the list entry; no due date, affected/patched versions, attribution or victim confirmation on the page.
