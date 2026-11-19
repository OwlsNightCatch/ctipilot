Title: CVE-2026-90817 - CVE-2026-90817: REDCap Survey RCE Vulnerability

URL Source: https://www.sentinelone.com/vulnerability-database/cve-2026-90817/

Final URL: https://www.sentinelone.com/vulnerability-database/cve-2026-90817/?utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F&utm_medium=s1-site-referral#cq=i1

Published Time: 2026-09-20T13:17:44.973

Markdown Content:
## CVE-2026-90817 Overview

CVE-2026-90817 is an unauthenticated Remote Code Execution (RCE) vulnerability in REDCap, the research electronic data capture platform. The flaw exists in the survey passthrough routing logic and the Data Import processing component. An attacker who knows a valid public survey hash can manipulate HTTP requests to reach an unintended controller route and supply a crafted file-path or stream parameter during import handling. Successful exploitation allows arbitrary code execution on the REDCap server without authentication. The vulnerability affects REDCap 13.3.0 and higher and is classified under [CWE-73] External Control of File Name or Path.

> ### Critical Impact
> 
> 
> Unauthenticated attackers with knowledge of a public survey hash can execute arbitrary code on the REDCap server, exposing research and clinical data.

### Affected Products

*   REDCap 13.3.0 and higher
*   REDCap survey passthrough routing component
*   REDCap Data Import processing logic

### Discovery Timeline

*   2026-09-20 - CVE-2026-90817 published to the National Vulnerability Database (NVD)
*   2026-09-22 - Last updated in NVD database

## Technical Details for CVE-2026-90817

### Vulnerability Analysis

The vulnerability chains two weaknesses in REDCap. The first is a routing flaw in the public survey passthrough handler, which allows an unauthenticated request originating in a public survey context to invoke controller routes that should be restricted to authenticated sessions. The second is unsafe handling of user-controlled file-path and stream parameters inside the Data Import processing logic.

By combining both flaws, an attacker who possesses a valid public survey hash can reach the import controller without credentials and pass a crafted path or stream identifier. The import handler then processes attacker-controlled content in a code execution context on the server. The underlying weakness is external control of file name or path [CWE-73].

### Root Cause

The root cause is insufficient authorization enforcement on controller routes reachable through the survey passthrough layer, combined with missing validation of file-path and stream parameters accepted by the Data Import handler. Trust is derived from the presence of a public survey hash rather than from a scoped authorization check on the target action.

### Attack Vector

The attack vector is network-based and requires no authentication or user interaction. The attacker must know a valid public survey hash, which is often shared broadly for participant recruitment. Using this hash, the attacker issues an HTTP request that passes through the survey routing layer and lands on the Data Import controller with a crafted file-path or stream parameter, triggering code execution.

Refer to the [Securifera Security Advisory](https://www.securifera.com/advisories/) for additional technical details.

### Stop Remote Code Execution Before It Runs

Singularity™ Endpoint detects and blocks exploit attempts at machine speed, including zero-days and novel attack techniques.

[Stop Exploit Attempts](https://www.sentinelone.com/platform/endpoint-security/?utm_content=vulndb_cta_inline)

## Detection Methods for CVE-2026-90817

### Indicators of Compromise

*   HTTP requests targeting survey passthrough endpoints that include unexpected controller or action parameters not typically invoked from a public survey.
*   Data Import controller invocations originating from unauthenticated sessions carrying a public survey hash.
*   File-path or stream parameters containing absolute paths, protocol wrappers (php://, file://, data://), or path traversal sequences.
*   New or modified PHP files, cron entries, or web shells created under the REDCap webroot after suspicious survey requests.

### Detection Strategies

*   Inspect web server access logs for anomalous query strings on survey URLs, particularly parameters referencing import, data upload, or file handling actions.
*   Correlate public survey requests with subsequent server-side process creation events, such as php spawning shells or network utilities.
*   Alert on outbound connections from the REDCap application server to unexpected destinations following survey traffic bursts.

### Monitoring Recommendations

*   Enable verbose application logging for the survey routing layer and Data Import controller and forward events to a centralized SIEM.
*   Monitor file integrity on the REDCap web directory and configuration paths to catch unauthorized writes.
*   Track process lineage on the web server host to identify shell or interpreter execution spawned by the web process.

## How to Mitigate CVE-2026-90817

### Immediate Actions Required

*   Identify all REDCap instances running version 13.3.0 or later and prioritize patching internet-facing deployments.
*   Rotate or invalidate existing public survey hashes where feasible, since exploitation requires knowledge of a valid hash.
*   Restrict network access to the REDCap application to trusted networks or via a web application firewall (WAF) until patched.
*   Review web server and application logs for evidence of prior exploitation attempts against survey endpoints.

### Patch Information

Apply the security update issued by the REDCap vendor (Vanderbilt University) for versions 13.3.0 and higher. Consult the [Securifera Security Advisory](https://www.securifera.com/advisories/) and the official REDCap consortium release notes for the fixed version. No public exploit or CISA KEV listing has been recorded at the time of publication.

### Workarounds

*   Place REDCap behind a WAF and block requests to survey endpoints that carry controller or file-path parameters not expected by the public survey flow.
*   Disable or restrict the Data Import functionality if it is not required, and constrain its handlers to authenticated administrative sessions.
*   Enforce network segmentation so the REDCap server cannot initiate arbitrary outbound connections or reach sensitive internal services.

bash

```
# Example WAF rule concept: block suspicious parameters on survey passthrough URIs
# (adapt to your WAF syntax, e.g., ModSecurity, AWS WAF, Azure WAF)
SecRule REQUEST_URI "@rx /surveys/" \
  "chain,phase:2,deny,status:403,id:1090817,\
   msg:'CVE-2026-90817 REDCap survey passthrough abuse'"
  SecRule ARGS_NAMES|ARGS "@rx (?:php://|file://|data://|\.\./|/etc/|/var/www/)" \
    "t:lowercase,t:urlDecodeUni"
```

Links/Buttons:
- [___](https://www.sentinelone.com/vulnerability-database/cve-2026-90817/?utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F&utm_medium=s1-site-referral#)
- [Skip to main content](https://www.sentinelone.com/vulnerability-database/cve-2026-90817/?utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F&utm_medium=s1-site-referral#main-content)
- [Read More](https://www.sentinelone.com/blog/stopping-php2shell-how-sentinelone-protects-customers-from-this-attack-technique/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Experiencing a breach?](https://www.sentinelone.com/global-services/get-support-now/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Blog](https://www.sentinelone.com/blog/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Careers](https://www.sentinelone.com/careers/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [](https://www.onetrust.com/solutions/consent-and-preferences/)
- [Singularity™ PlatformUnified Enterprise Security. Machine-Speed Protection, Intelligence, and Response.](https://www.sentinelone.com/platform/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [XDRNative and Open Protection, Detection, and Response.](https://www.sentinelone.com/platform/singularity-xdr-protection/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Integrations and PartnersOne-Click Integrations to Unlock the Power of SentinelOne.](https://www.sentinelone.com/partners/singularity-marketplace/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Product Tours](https://www.sentinelone.com/tour/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Pricing & Packages](https://www.sentinelone.com/platform-packages/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Get a Demo](https://www.sentinelone.com/request-demo/?utm_content=vulndb_cta_footer&utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [See All Industries](https://www.sentinelone.com/solutions/industries/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [HealthcareProtect Patient Data. Keep Clinical Systems Online.](https://www.sentinelone.com/platform/healthcare/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Financial ServicesStop Fraud and Ransomware. Stay Audit-Ready.](https://www.sentinelone.com/platform/finance/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Federal GovernmentFedRAMP High Authorized, Mission Ready Defense for Federal Government.](https://www.sentinelone.com/platform/federal-government/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [ManufacturingDefend OT, IT, IIOT, and Supply Chains at Scale.](https://www.sentinelone.com/platform/manufacturing/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [EnergySecure OT Systems and Critical Infrastructure.](https://www.sentinelone.com/platform/energy/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Transportation and LogisticsDefend Operations Across Fleet, Port, and Rail.](https://www.sentinelone.com/platform/transportation/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Higher EducationProtect Open Networks Without Slowing Research.](https://www.sentinelone.com/platform/highereducation/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [K-12 EducationStop Ransomware. Protect Students, Staff, and Data.](https://www.sentinelone.com/platform/platform-cybersecurity-for-k12-education/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Retail and HospitalityDefend Your Brand, Customer Data, and Bottom Line.](https://www.sentinelone.com/platform/retail/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [SMB & StartupsEnterprise-Grade Defense for Fast Teams.](https://www.sentinelone.com/platform/small-business/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [State and Local GovernmentProtect Citizen Services, Infrastructure, and Public Data.](https://www.sentinelone.com/platform/state-and-local-government/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [See all solutions](https://www.sentinelone.com/solutions/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Learn More](https://www.sentinelone.com/global-services/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Threat HuntingWorld-Class Expertise and Threat Intelligence.](https://www.sentinelone.com/global-services/threat-hunting/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Managed Detection and Response24/7 Expert MDR Across Your Entire Environment.](https://www.sentinelone.com/global-services/managed-detection-and-response/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Incident Readiness and ResponseDFIR, Breach Readiness, and Compromise Assessments.](https://www.sentinelone.com/global-services/incident-readiness-and-response/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [1-855-868-3733](tel:1-855-868-3733)
- [Become a SentinelOne PartnerJoin the Global SentinelOne Ecosystem](https://partners.sentinelone.com/)
- [Explore MSSP SolutionsServices Succeed Faster with SentinelOne](https://www.sentinelone.com/partners/mssp-partners/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Form a Technology AllianceIntegrated, Enterprise-Scale Solutions](https://www.sentinelone.com/partners/technology-alliance/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Enlist a Response or Advisory TeamEnlist Pro Response and Advisory Teams](https://www.sentinelone.com/partners/cyber-risk-partners/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [SentinelOne for AWSHosted Across AWS Regions Worldwide](https://www.sentinelone.com/sentinelone-for-aws/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [SentinelOne for GoogleUnified, Autonomous Security Giving Defenders the Advantage at Global Scale](https://www.sentinelone.com/sentinelone-for-google/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Partner LocatorYour Go-to Source for Our Top Partners in Your Region](https://www.sentinelone.com/partners/partner-locator/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Why Choose SentinelOneAI-Powered Cybersecurity Built to Secure What’s Next.](https://www.sentinelone.com/why-sentinelone/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Our CustomersTrusted by the World’s Leading Companies.](https://www.sentinelone.com/customers/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Industry Awards & RecognitionTested and Proven by the Experts.](https://www.sentinelone.com/industry-recognition/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Resource Center](https://www.sentinelone.com/resources/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Webinars](https://www.sentinelone.com/resources/webinars/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Events](https://www.sentinelone.com/events/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Newsroom](https://www.sentinelone.com/press/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [About SentinelOne](https://www.sentinelone.com/company/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Leadership](https://www.sentinelone.com/company/leadership/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [S Ventures](https://www.sentinelone.com/s-ventures/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [S Foundation](https://www.sentinelone.com/s-foundation/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [FAQ](https://www.sentinelone.com/faq/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Investors Relations](https://investors.sentinelone.com/overview/default.aspx)
- [Live and On-Demand Training](https://www.sentinelone.com/global-services/university/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Guided Onboarding & Deployment](https://www.sentinelone.com/global-services/sentinelone-go/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Technical Account Management](https://www.sentinelone.com/global-services/technical-account-management/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Support Services](https://www.sentinelone.com/global-services/services-overview/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Customer Portal](https://community.sentinelone.com/)
- [Vulnerability Database](https://www.sentinelone.com/vulnerability-database/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [SentinelLABS Threat Research](https://www.sentinelone.com/labs/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Ransomware Anthology](https://www.sentinelone.com/anthology/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Cybersecurity 101](https://www.sentinelone.com/cybersecurity-101/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Supplier Hub](https://www.sentinelone.com/supplier-hub/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [The SentinelOne Annual Threat Report](https://www.sentinelone.com/threat-report/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Get Started](https://www.sentinelone.com/request-demo/?utm_content=vulndb_cta_header&utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Contact Us](https://www.sentinelone.com/contact/?utm_content=vulndb_cta_footer&utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [National Vulnerability Database](https://nvd.nist.gov/vuln)
- [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [Exploit-DB](https://www.exploit-db.com/)
- [Securifera Security Advisory](https://www.securifera.com/advisories/)
- [Stop Exploit Attempts](https://www.sentinelone.com/platform/endpoint-security/?utm_content=vulndb_cta_inline)
- [Speak to Experts](https://www.sentinelone.com/request-demo/?utm_content=vulndb_cta_sidebar)
- [CWE-73](https://cwe.mitre.org/data/definitions/73.html)
- [CVE-2024-55374: REDCap Username Enumeration Vulnerability](https://www.sentinelone.com/vulnerability-database/cve-2024-55374/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Try SentinelOne](https://www.sentinelone.com/request-demo/?utm_content=vulndb_cta_prefooter)
- [SentinelOne Status](https://status.sentinelone.com/)
- [Singularity Endpoint](https://www.sentinelone.com/platform/endpoint-security/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Singularity Cloud](https://www.sentinelone.com/platform/cloud-security/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Prompt Security](https://www.sentinelone.com/platform/securing-ai-prompt/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Singularity AI-SIEM](https://www.sentinelone.com/platform/ai-siem/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Singularity Identity](https://www.sentinelone.com/platform/identity/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Purple AI](https://www.sentinelone.com/platform/purple/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Partners](https://www.sentinelone.com/partners/partner-overview/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Legal Information](https://www.sentinelone.com/legal/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Security & Compliance](https://www.sentinelone.com/security-compliance/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Privacy Notice](https://www.sentinelone.com/legal/privacy-notice/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Terms of Use](https://www.sentinelone.com/legal/terms-of-use/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [Sitemap](https://www.sentinelone.com/sitemap/?utm_medium=s1-site-referral&utm_source=https%3A%2F%2Fwww.sentinelone.com%2Fvulnerability-database%2Fcve-2026-90817%2F)
- [More information](https://cookiepedia.co.uk/giving-consent-to-cookies)
