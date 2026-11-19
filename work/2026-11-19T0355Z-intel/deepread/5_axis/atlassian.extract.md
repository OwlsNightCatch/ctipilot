---
title: CVE-2026-90436 - Remote Code Execution in Confluence Data Center
url: https://confluence.atlassian.com/security/cve-2026-90436-remote-code-execution-in-confluence-data-center-and-server-1874560038.html
hostname: atlassian.com
sitename: Atlassian Documentation
date: "2026-11-10"
fingerprint: ac4d3987eef32caa
---
# CVE-2026-90436 - Remote Code Execution in Confluence Data Center

| Summary | CVE-2026-90436 - Remote Code Execution in Confluence Data Center | 
| Advisory Release Date | Tue, Nov 9 2026 22:00 PST | 
| Products | Confluence Data Center This vulnerability has no impact on Atlassian Cloud sites, and no action is required. If your Confluence site is accessed via an [atlassian.net](https://www.atlassian.com/software) or [jira.com](https://www.atlassian.com/software/jira) domain, it is securely hosted by Atlassian and not vulnerable to this issue. | 
| CVE ID | [CVE-2026-90436](https://nvd.nist.gov/vuln/detail/CVE-2026-90436) | 
| Related Jira Ticket(s) |  | 

## Summary of Vulnerability

Confluence utilizes a third-party library Apache Axis as part of its XML-RPC and SOAP APIs. Apache Axis has published a critical vulnerability (CVE-2026-90436) that allows remote code execution.

To be vulnerable, the Confluence instance must have the ‘Remote API (XML-RPC & SOAP)’ enabled. Please note that this setting was turned off by default for new installations starting in Confluence 3.0. This feature was fully removed in Confluence 10.0.

### Severity

Atlassian rates the severity level of this vulnerability as critical (**9.3** with the following vector **CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N**) per our internal assessment.

This is our assessment, and you should evaluate its applicability to your own IT environment.

### Affected Versions

This Remote Code Execution vulnerability affects the following versions of Confluence Data Center. Atlassian recommends patching to the latest version or a fixed LTS version. Note that Confluence 10.x and above are not impacted.

| Product | Affected Versions | 
|---|---|
| Confluence Data Center | 1.x.x 2.x.x 3.x.x 4.x.x 5.x.x 6.x.x 7.x.x 8.x.x 9.x.x | 

## What You Need To Do

### **Immediately patch to a fixed version**

Atlassian recommends that you patch each of your affected installations to the latest version or one of the listed fixed versions below.

| Product | Fixed Versions | 
|---|---|
| Confluence Data Center | 9.2.28 | 

### **Apply temporary mitigations if unable to patch**

Turning off "Remote API (XMl-RPC & SOAP)" may cause certain functionality, such as scripts, automations and third-party add-ons, to stop working. You may wish to test the mitigations in a non-production environment before applying them across your sites.

1. Login to Confluence as an administrator
2. Click  (top-right menu bar) then ‘General Configuration’ and then ‘Further Configuration'. This can also be accessed via `<base_url>/admin/viewspacesconfig.action`
3. Click the ‘Edit’ button on the far right to edit the items on the screen.
4. Ensure that the checkbox is clear/unselected for 'Remote API (XML-RPC & SOAP)'
5. Click ‘Save’ at the bottom and when the page reloads, ensure that the checkbox for ‘Remote API (XML-RPC & SOAP)’ is empty/clear. You do not need to restart Confluence - the setting takes effect as soon as you click ‘Save’.

#### To validate that the mitigation is set correctly:

1. Browse to `<base_url>/plugins/servlet/soap-axis1/confluenceservice-v2`
2. If mitigation is set correctly and is working, you will see a ‘HTTP Status 403 - Forbidden’
3. If there are any issues, or if you receive a message about ‘confluenceservice-v2’ or ‘AXIS service’ then please re-check the mitigation steps above, and [contact Atlassian support](https://support.atlassian.com/contact) for further assistance.

### Threat detection

Atlassian cannot confirm if your instances have been affected by this vulnerability. You should engage your local security team to check all affected instances for evidence of compromise.

For a full description of the latest versions, see the release notes for your product below.

You can download the latest version for your product from the download center:

## Support

If you did not receive an email for this advisory, and you wish to receive such emails in the future go to [https://my.atlassian.com](https://my.atlassian.com), then click 'Email Preferences' at the top, then scroll down and subscribe to Tech Alerts emails. If you have questions or concerns regarding this advisory, please raise a support request at [https://support.atlassian.com/contact/#/](https://support.atlassian.com/contact/#/).

### References

| [Security Bug Fix Policy](https://www.atlassian.com/trust/security/bug-fix-policy) | As per our new policy critical security bug fixes will be back ported. We will release new maintenance releases for the versions covered by the policy instead of binary patches. **Binary patches are no longer released.** | 
| [Security Levels for Security Issues](https://www.atlassian.com/security/security-severity-levels) | Atlassian security advisories include a severity level and a CVE identifier. This severity level is based on our self-calculated CVSS score for each specific vulnerability. CVSS is an industry standard vulnerability metric. You can also learn more about CVSS at [FIRST.org](https://www.first.org/cvss/user-guide). | 
| [End of Life Policy](https://confluence.atlassian.com/support/atlassian-support-end-of-life-policy-201851003.html) | Our end of life policy varies for different products. Please refer to our EOL Policy for details. | 

[Confluence](http://www.atlassian.com/)and

[Scroll Viewport](https://www.k15t.com/go/scroll-viewport).
