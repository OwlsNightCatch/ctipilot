Title: Understanding and Addressing CVE-2026-88779 in Citrix NetScaler ADC and Citrix NetScaler Gateway

URL Source: https://community.citrix.com/techzone-blogs/110_security-updates/understanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway/

Published Time: 2026-10-03T18:42:00-07:00

Markdown Content:
CVE-2026-88779 is a memory overflow vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway that can lead to denial of service under specific deployment conditions. The issue affects customer-managed NetScaler deployments running affected supported versions when the required preconditions are met. Customers should review their deployed versions and configurations, then install the relevant updated versions as soon as possible.

#### Affected Versions

The following supported versions are affected when the CVE preconditions (see the section “How to Determine Whether a NetScaler deployment Meets the Preconditions” below) apply:

*   NetScaler ADC and NetScaler Gateway 14.1 before 14.1-73.41

*   NetScaler ADC and NetScaler Gateway 13.1 before 13.1-64.28

*   NetScaler ADC FIPS before 14.1-73.41 FIPS

*   NetScaler ADC FIPS and NDcPP before 13.1-37.282

#### What Is the Issue?

CVE-2026-88779 is categorized as **CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer**. The vulnerability has a CVSS v4.0 base score of **8.7**. Citrix has observed targeted attacks on unmitigated NetScaler deployments which can lead to Denial of Service. If the condition is triggered repeatedly, the service may remain unavailable. Our analysis indicates that this issue affects service availability, and we have not identified an impact on the integrity of customer data. Citrix strongly urges all customers to install the latest versions as soon as possible.

The most important operational detail is that exposure depends on how the NetScaler deployment is configured. Customers should validate whether the relevant Gateway, AAA, and SAML preconditions apply to their environment.

Please note that the bulletin only applies to customer-managed NetScaler ADC and NetScaler Gateway. Citrix upgrades the Citrix-managed cloud services, including Gateway Service and Citrix-managed Adaptive Authentication, with the necessary software updates.

#### How to Determine Whether a NetScaler Deployment Meets the Preconditions

The issue is associated with NetScaler deployments that use SAML authentication in conjunction with Gateway or AAA functionality. Customers who have deployed NetScaler as a Gateway or AAA virtual server should review their NetScaler configurations to determine whether SAML authentication actions are configured.

Customers can determine whether their NetScaler deployment meets the precondition by inspecting their NetScaler configuration for entries matching either of the following:

*   Appliance is configured as a SAML SP  
add authentication samlAction
OR

*   Appliance is configured as a SAML IdP  
add authentication samlIdPProfile

#### What Customers Should Do

As a mitigation, Citrix has released signatures which can be used via the [Global Deny List](https://community.citrix.com/techzone-blogs/netscaler/netscaler-global-deny-list-always-on-protection-for-the-threats-you-havent-modeled-yet-r1254/#2_Unconditional_evaluation_in_the_request_pipeline__3e5a90) feature. This can help reduce exposure while customers validate applicability and plan an upgrade to a software version containing the fix.

The Global Deny List feature is enabled by default on NetScaler software starting with versions 14.1-60.52 and 13.1-63.21. Here are the prerequisites:

1.   You need to use NetScaler Console on-premises (with Cloud Connect) or NetScaler Console service.

1.   Please ensure that the “Virtual patching” Status is “Enabled” in the NetScaler Console configurable settings as shown below:

1.   Applicable NetScaler software versions must fall within one of the following supported version ranges:

**14.1 version range: >= 14.1-73.37 and < 14.1-73.41**

**13.1 version range: >= 13.1-64.23 and < 13.1-64.28**

Verify if Global Deny List signatures are available on your NetScaler deployment by executing the following command:

**show appfw signatures**

In the output, verify under “Name: *Default Signatures” that the Encrypted Version is displayed as a number. This signifies that a version of the signatures is available on a NetScaler deployment. The version number needs to be at least v24 as shown below:

To verify whether the Global Deny List signature is working, please execute the following command in the NetScaler CLI:

**stat denylist global AAA_REQUEST**

Also check the counters statistics for the rule evaluated and other stats, including Last Hit Time. If the value is greater than 0, the rules are working.

**IMPORTANT**: Please also note that the Global Deny List signatures can help to mitigate the vulnerability. Citrix recommends upgrading to the following software versions containing the fix as soon as possible.

*   Upgrade NetScaler ADC and NetScaler Gateway 14.1 to **14.1-73.41 or later**.

*   Upgrade NetScaler ADC and NetScaler Gateway 13.1 to **13.1-64.28 or later**.

*   Upgrade NetScaler ADC 14.1-FIPS to **14.1-73.41 FIPS or later**.

*   Upgrade NetScaler ADC 13.1-FIPS and 13.1-NDcPP to **13.1-37.282 or later**.

#### Additional Guidance

*   Citrix continues to monitor vulnerability activity and to work with the security research community through coordinated disclosure. Citrix will continue to provide timely updates as needed to help customers protect their NetScaler deployments.

*   Customers should ensure that NetScaler deployments are updated promptly, review configurations against the applicable preconditions, and follow their standard incident response processes if they identify signs of compromise.

*   Customers can block suspicious IP addresses by using the blocklist [functionality](https://docs.netscaler.com/en-us/netscaler-k8s-ingress-controller/how-to/ip-whitelist-blacklist.html) of NetScaler.

*   As part of a defense-in-depth approach, customers should review relevant network and perimeter controls and, where appropriate, use firewall rules to block traffic from IP addresses identified as sources of attack activity.

*   If you upgraded your NetScaler deployment with one of the updated software releases identified in [the security bulletin for CVE 2026-88771 through CVE 2026-88778,](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) and if you have determined that your NetScaler deployment meets the preconditions describe above, please upgrade your deployment again with the software released as part of the [security bulletin for CVE-2026-88779](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174).

*   The official [security bulletin for CVE 2026-88779](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174) is the authoritative statement concerning the security vulnerability announced in the bulletin; please refer to the bulletin as the controlling statement concerning the vulnerability.

Learn more and stay up to date

1.   Review the official [security bulletin](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174)

1.   Sign up for [security bulletin notifications](https://support.citrix.com/wolken-support/view/aboutsupport/my-support-alerts)

1.   Review the [NetScaler Secure Deployment Guide](https://docs.netscaler.com/en-us/netscaler-adc-secure-deployment.html)

1.   Use NetScaler Console [security advisory](https://docs.netscaler.com/en-us/netscaler-console-service/instance-advisory/security-advisory-dashboard.html) for your NetScaler deployments.

Last Updated on: October 3, 2026 (Pacific Daylight Time)

Links/Buttons:
- [Skip to content](https://community.citrix.com/techzone-blogs/110_security-updates/understanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway/#ipsLayout__main)
- [Citrix Community](https://community.citrix.com/)
- [Tech Zone Blogs](https://community.citrix.com/techzone-blogs/)
- [Security Updates](https://community.citrix.com/techzone-blogs/110_security-updates/)
- [All Activity](https://community.citrix.com/discover/)
- [Forgot your password/Citrix login user?](https://community.citrix.com/lostpassword/)
- [New User? Sign Up](https://community.citrix.com/register/)
- [Discussions](https://community.citrix.com/forums/)
- [Citrix DaaS](https://community.citrix.com/tech-zone/by-product/citrix-daas/)
- [Citrix Endpoint Management](https://community.citrix.com/tech-zone/by-product/citrix-endpoint-management/)
- [Citrix Observability](https://community.citrix.com/tech-zone/by-product/citrix-analytics/)
- [Citrix Secure Private Access](https://community.citrix.com/tech-zone/by-product/citrix-secure-private-access/)
- [Citrix Virtual Apps and Desktops](https://community.citrix.com/tech-zone/by-product/citrix-virtual-apps-and-desktops/)
- [NetScaler](https://community.citrix.com/tech-zone/by-product/netscaler/)
- [Citrix SecurSpaces](https://community.citrix.com/tech-zone/by-product/citrix-securspaces/)
- [Unicon](https://community.citrix.com/tech-zone/by-product/unicon/)
- [XenServer](https://community.citrix.com/tech-zone/by-product/xenserver/)
- [Tech Zone Home](https://community.citrix.com/tech-zone-home/)
- [Citrix Blogs](https://www.citrix.com/blog/)
- [Citrix Github Repository](https://github.com/citrix)
- [Citrix Product Documentation](https://docs.citrix.com/)
- [Citrix YouTube Channel](https://www.youtube.com/citrix)
- [Developer Documentation](https://developer-docs.cloud.com/)
- [Diagrams, Posters, and Stencils](https://community.citrix.com/tech-zone/design/diagrams-and-posters/)
- [NetScaler Blogs](https://www.netscaler.com/blog/)
- [NetScaler Github Repository](https://github.com/netscaler)
- [NetScaler Product Documentation](https://docs.netscaler.com/)
- [NetScaler YouTube Channel](https://www.youtube.com/@NetScaler)
- [Citrix Video Articles](https://community.citrix.com/videos/)
- [The Click Down](https://www.citrix.com/lp/the-click-down/)
- [Events](https://community.citrix.com/events/)
- [Rewards Program](https://community.citrix.com/rewards/)
- [Unsolved Topics](https://community.citrix.com/discover/7/)
- [Search](https://community.citrix.com/search/)
- [Training & Certifications](https://www.citrix.com/training-and-certifications/)
- [Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcommunity.citrix.com%2Ftechzone-blogs%2F110_security-updates%2Funderstanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway%2F)
- [{lang="reddit_text"](https://www.reddit.com/submit?url=https%3A%2F%2Fcommunity.citrix.com%2Ftechzone-blogs%2F110_security-updates%2Funderstanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway%2F&title=Understanding+and+Addressing+CVE-2026-88779+in+Citrix+NetScaler+ADC+and+Citrix+NetScaler+Gateway)
- [Share on LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcommunity.citrix.com%2Ftechzone-blogs%2F110_security-updates%2Funderstanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway%2F&title=Understanding+and+Addressing+CVE-2026-88779+in+Citrix+NetScaler+ADC+and+Citrix+NetScaler+Gateway)
- [Share on Pinterest](https://pinterest.com/pin/create/button/?url=https://community.citrix.com/techzone-blogs/110_security-updates/understanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway/&media=)
- [Share on X](https://x.com/share?url=https%3A%2F%2Fcommunity.citrix.com%2Ftechzone-blogs%2F110_security-updates%2Funderstanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway%2F)
- [Followers](https://community.citrix.com/login/)
- [](https://community.citrix.com/profile/1368-netscaler-cyber-threat-intelligence/)
- [Global Deny List](https://community.citrix.com/techzone-blogs/netscaler/netscaler-global-deny-list-always-on-protection-for-the-threats-you-havent-modeled-yet-r1254/#2_Unconditional_evaluation_in_the_request_pipeline__3e5a90)
- [functionality](https://docs.netscaler.com/en-us/netscaler-k8s-ingress-controller/how-to/ip-whitelist-blacklist.html)
- [the security bulletin for CVE 2026-88771 through CVE 2026-88778,](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096)
- [security bulletin for CVE-2026-88779](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174)
- [security bulletin notifications](https://support.citrix.com/wolken-support/view/aboutsupport/my-support-alerts)
- [NetScaler Secure Deployment Guide](https://docs.netscaler.com/en-us/netscaler-adc-secure-deployment.html)
- [security advisory](https://docs.netscaler.com/en-us/netscaler-console-service/instance-advisory/security-advisory-dashboard.html)
- [0 Comments](https://community.citrix.com/techzone-blogs/110_security-updates/understanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway/?&tab=comments)
- [Community Site Help](https://community.citrix.com/contact/)
- [Cookies](https://community.citrix.com/cookies/)
- [Citrix Tech Zone Document History](https://community.citrix.com/rss/1-citrix-tech-zone-document-history.xml/)
- [Citrix Tech Zone Blogs](https://community.citrix.com/rss/3-citrix-tech-zone-blogs.xml/)
- [Terms of Use](https://www.cloud.com/community-terms-of-use)
- [Privacy Policy](https://www.citrix.com/about/legal/privacy/)
- [Cookie Preferences](https://community.citrix.com/techzone-blogs/110_security-updates/understanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway/#)
- [Your Privacy Choices](https://app.smartsheet.com/b/form/5a4f963f77fb4acc91bb6e4a3b47cda3)
- [0 Your Cart](https://community.citrix.com/store/cart/)
