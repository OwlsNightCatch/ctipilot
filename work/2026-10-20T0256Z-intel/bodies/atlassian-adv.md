---
title: CVE-2026-21589 - Arbitrary File Access Vulnerability impacts Multiple Products
url: https://confluence.atlassian.com/security/cve-2026-21589-arbitrary-file-access-vulnerability-impacts-multiple-products-1870495748.html
hostname: atlassian.com
sitename: Atlassian Documentation
date: "2026-10-05"
fingerprint: ae843c0566d16c0f
---
# CVE-2026-21589 - Arbitrary File Access Vulnerability impacts Multiple Products

| Summary | CVE-2026-21589 - Arbitrary File Access Vulnerability impacts Multiple Products | 
| Advisory Release Date |  | 
| Products | Bitbucket Data Center Confluence Data Center Jira Service Management Data Center Jira Software Data Center Bamboo Data Center Crowd Data Center Crucible Fisheye | 
| CVE ID | CVE-2026-21589 | 
| Related Jira Ticket(s) |  | 

## Summary of Vulnerability

All versions of Bitbucket Data Center, Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible, and Fisheye are affected by this vulnerability. This Arbitrary File Access vulnerability allows an unauthenticated attacker to access specific files within the web application root directory in affected versions. Exploitation requires prior knowledge of the target file's exact name and path; this vulnerability does not allow attackers to enumerate or list directory contents. In some configurations, there may be sensitive files present that increase your risk.

All Data Center products listed below are at risk and require immediate attention. See “What You Need to Do” for detailed instructions.

Affected Atlassian Cloud products have been patched, and our investigation has not found evidence of exploitation. No Cloud customer action is required.

### Severity

Atlassian rates the severity level of this vulnerability as Critical (**9.3** with the following vector **CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N/SC:H/SI:H/SA:H**) per our internal assessment. 

This is our assessment, and you should evaluate its applicability to your own IT environment.

### Affected Versions

This Arbitrary File Access vulnerability affects all versions prior to the listed fix versions of affected Products. Atlassian recommends patching to the fixed LTS version or later.

| Product | Affected Versions | 
|---|---|
| Bitbucket Data Center Confluence Data Center Jira Service Management Data Center Jira Software Data Center Bamboo Data Center Crowd Data Center Crucible Fisheye | All versions are affected | 

## What You Need To Do

### Immediately patch to a fixed version

Atlassian recommends that you patch each of your affected installations to fixed versions or the latest version.

| Product | Fixed Versions | 
|---|---|
| Bitbucket Data Center | 9.4.26 10.2.8 10.5.1 | 
| Confluence Data Center | 9.2.26 10.2.19 | 
| Jira Service Management Data Center | 5.12.40 10.3.26 11.3.12 | 
| Jira Software Data Center | 9.12.40 10.3.26 11.3.12 | 
| Bamboo Data Center | 10.2.24 12.1.12 | 
| Crowd Data Center | 6.3.7 7.0.3 7.1.7 7.2.4 | 
| Crucible | 4.9.15 | 
| Fisheye | 4.9.15 | 

### Apply temporary mitigations if unable to patch

Remove your instance from the internet until you can patch or apply mitigations, if possible. Instances accessible to the public internet, including those with user authentication, should be restricted from external network access until you can take action.

**Option 1: Apply a Web Application Firewall Rule, requires regex filtering (For All Affected Products)**

Apply a rule, described below, to your Web Application Firewall or proxy layer. Rule implementation instructions are dependent on your technology (e.g. reverse proxy, AWS WAF, or Cloudflare).

1. Block any URL containing this regex pattern regex filter`(?is).*(?:/|\\|::|%(?:25)*(?:2f|5c)|(?::|%(?:25)*3a){2})(?:\.|%(?:25)*2e){2}(?:/|\\|::|%(?:25)*(?:2f|5c)|(?::|%(?:25)*3a){2}|;|%(?:25)*3b|$).*` The intent of this regex is to block `..` 
`/`, `\`
`::`
2. Test that your rule blocks `..` 
`/`, `\`
`::`

#### Option 2: Block requests using Tomcat’s RewriteValve (For Confluence, JSM, Jira, Bamboo, and Crowd)

First, back up your instance. Then, for each node in your Data Center cluster:

1. Shut down the node
2. Enable Tomcat’s RewriteValve: 
  1. Locate the `server.xml` file:
    1. On Confluence, JSM, Jira, and Bamboo: `conf/server.xml`
    2. On Crowd: either `apache-tomcat/conf/Catalina/localhost/crowd.xml` or `apache-tomcat/conf/server.xml`, whichever has your application `<Context>` (see below)
  2. Make a copy of this file as a backup
  3. Inside this file identify the `<Context>` element representing the application, the `docBase` attribute will be a path including the product name; in the standard setup this will be the only `<Context>` element
  4. Add the following line within that element if it is not already there:
`<Valve className="org.apache.catalina.valves.rewrite.RewriteValve" />`
3. Install the configuration: 
  1. Locate the `WEB-INF` directory:
    1. On Confluence: `confluence/WEB-INF`
    2. On JSM/Jira: `atlassian-jira/WEB-INF`
    3. On Bamboo: `bamboo/WEB-INF` or `atlassian-bamboo/WEB-INF`
    4. On Crowd: `crowd-webapp/WEB-INF`
  2. Within this directory, check if the file `rewrite.config` exists
  3. If it exists: 
    1. Make a copy of the existing `rewrite.config` file as a backup
    2. Append the existing file with the `rewrite.config` code block provided below
  4. If it does not exist: 
    1. Create a `rewrite.config` file in the directory with the code block provided below
4. Restart the node

```
# Primary check: Tomcat's decoded, normalized request path (no query string).
RewriteCond %{REQUEST_PATH} (?is).*(?:/|\\|::|%(?:25)*(?:2f|5c)|(?::|%(?:25)*3a){2})(?:\.|%(?:25)*2e){2}(?:/|\\|::|%(?:25)*(?:2f|5c)|(?::|%(?:25)*3a){2}|;|%(?:25)*3b|$).*
RewriteRule (?s)^.*$ /?denied [F,L]
# Raw-URI fallback
RewriteCond %{REQUEST_URI} (?is).*(?:/|\\|::|%(?:25)*(?:2f|5c)|(?::|%(?:25)*3a){2})(?:\.|%(?:25)*2e){2}(?:/|\\|::|%(?:25)*(?:2f|5c)|(?::|%(?:25)*3a){2}|;|%(?:25)*3b|$).*
RewriteRule (?s)^.*$ /?denied [F,L]
```
#### Option 3: Add rule to urlrewrite.xml (For Bitbucket only)

1. First, back up your instance.
2. For a clustered system, this patch should be applied to all nodes. Similarly, apply the patch to all Bitbucket mirrors and Bitbucket mirror farm nodes.
  1. Edit the \<installation-directory>/app/WEB-INF/urlrewrite.xml file
  2. Add a new \<rule> to the top of the file, before other \<rule>s \<rule> \<from>(?is).\*(?:/|\\|::|%(?:25)\*(?:2f|5c)|(?::|%(?:25)\*3a){2})(?:\.|%(?:25)\*2e){2}(?:/|\\|::|%(?:25)\*(?:2f|5c)|(?::|%(?:25)\*3a){2}|;|%(?:25)\*3b|$).\*\</from> \<set type="status">404\</set> \<to>/mvc/error404\</to> \</rule> When the mitigation is applied, the top of the urlrewrite.xml file should look like the below: \<?xml version="1.0" encoding="utf-8"?> \<!DOCTYPE urlrewrite PUBLIC "-//tuckey.org//DTD UrlRewrite 4.0//EN" "dtds/urlrewrite4.0.dtd">\<urlrewrite decode-using="utf8"> \<rule> \<from>(?is).\*(?:/|\\|::|%(?:25)\*(?:2f|5c)|(?::|%(?:25)\*3a){2})(?:\.|%(?:25)\*2e){2}(?:/|\\|::|%(?:25)\*(?:2f|5c)|(?::|%(?:25)\*3a){2}|;|%(?:25)\*3b|$).\*\</from> \<set type="status">404\</set> \<to>/mvc/error404\</to> \</rule> \<!-- Johnson Error Pages --> \<rule> \[...\]
  3. Restart Bitbucket Data Center

### Threat detection

Atlassian cannot confirm if your instances have been affected by this vulnerability. You should engage your local security team to check all affected instances for evidence of compromise.

Paths for investigating evidence of compromise in your access logs:

- URL-decode each access-log request line (up to two decoding passes) before searching, then check for `..` immediately adjacent to `/`, `\`, or `::`; or
- Search raw (non-decoded) log lines directly using the regex above

## Support

If you did not receive an email for this advisory, and you wish to receive such emails in the future go to [https://my.atlassian.com/email](https://my.atlassian.com/email) and subscribe to Alerts emails. If you have questions or concerns regarding this advisory, please raise a support request at [https://support.atlassian.com/](https://support.atlassian.com/).

### References

| [Security Bug Fix Policy](https://www.atlassian.com/trust/security/bug-fix-policy) | As per our new policy critical security bug fixes will be back ported. We will release new maintenance releases for the versions covered by the policy instead of binary patches. **Binary patches are no longer released.** | 
| [Security Levels for Security Issues](https://www.atlassian.com/security/security-severity-levels) | Atlassian security advisories include a severity level and a CVE identifier. This severity level is based on our self-calculated CVSS score for each specific vulnerability. CVSS is an industry standard vulnerability metric. You can also learn more about CVSS at [FIRST.org](https://www.first.org/cvss/user-guide). | 
| [End of Life Policy](https://confluence.atlassian.com/support/atlassian-support-end-of-life-policy-201851003.html) | Our end of life policy varies for different products. Please refer to our EOL Policy for details. | 

## Links

For a full description of the latest versions, see the release notes for your product below.

You can download the latest version for your product from the download center:

[Confluence](http://www.atlassian.com/)and

[Scroll Viewport](https://www.k15t.com/go/scroll-viewport).
