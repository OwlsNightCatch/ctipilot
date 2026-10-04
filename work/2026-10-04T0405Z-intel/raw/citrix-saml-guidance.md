Title: Security Update: Guidance for NetScaler SAML Authentication Deployments

URL Source: https://community.citrix.com/techzone-blogs/110_security-updates/security-update-guidance-for-netscaler-saml-authentication-deployments/

Published Time: 2026-10-02T15:35:00-04:00

Markdown Content:
NetScaler engineering and support teams are tracking a newly observed issue related to SAML authentication in customer-managed NetScaler deployments. This post explains what customers should review, how to determine whether the relevant configuration is present, and what mitigation options are available while planning an upgrade to a fixed build. A new [security bulletin](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174) and a new [blog](https://community.citrix.com/techzone-blogs/110_security-updates/understanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway/) has been published.

The guidance below is intended to help customers take immediate action to reduce exposure. As with any security-related issue, customers should prioritize applying the updated NetScaler builds referenced in the applicable security bulletin.

#### What is being observed

The issue is associated with NetScaler deployments that use SAML authentication in conjunction with Gateway or AAA functionality. Customers who have deployed NetScaler as a Gateway or AAA virtual server should review their NetScaler configurations to determine whether SAML authentication actions are configured.

Based on the information currently available to us, this issue is configuration dependent. Customers should search for the following configuration patterns in their NetScaler configurations to determine applicability.

The NetScaler is affected when at least one of the following SAML commands is present:

*   "add authentication samlAction.*"

*   "add authentication samlIdPProfile**.***"

#### Recommended customer action

Customers should take the following actions:

1.   Inspect the NetScaler Gateway and AAA configuration for SAML authentication action.

1.   If you are currently experiencing the impact from this issue, please contact Citrix support.

1.   Once the security bulletin is published, upgrade affected appliances to the updated software as soon as possible.

#### Frequently asked questions

##### Does this apply to all NetScaler deployments?

Based on the information currently available to us, applicability depends on the conditions described above. Customers should review whether SAML authentication actions are configured on a Gateway or AAA virtual server.

##### Is this issue related to the vulnerabilities disclosed in security bulletin number [CTX697096](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096)?

This issue is independent of the vulnerabilities disclosed in [CTX697096.](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096)

##### When is Citrix planning to announce a security bulletin for this issue?

Our teams are actively investigating this issue. We will update this blog with additional information as soon as it is available for publication.

#### Additional guidance

Customers should refer to the official NetScaler security bulletin when it becomes available for the definitive list of affected versions, fixed builds, applicability conditions, and recommended actions.

##### Monitor this article

Citrix will continue to monitor developments and respond to new information related to this vulnerability. We recommend that customers bookmark and monitor this article for the latest updates.

##### Subscribe to Security Bulletins

Citrix strongly recommends that all customers subscribe to receive alerts when a Citrix security bulletin is created or modified at [https://support.citrix.com/wolken-support/view/aboutsupport/my-support-alerts](https://support.citrix.com/wolken-support/view/aboutsupport/my-support-alerts)

**Last Updated on: October 3, 2026 (Pacific Daylight Time)**

Links/Buttons:
- [Skip to content](https://community.citrix.com/techzone-blogs/110_security-updates/security-update-guidance-for-netscaler-saml-authentication-deployments/#ipsLayout__main)
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
- [Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcommunity.citrix.com%2Ftechzone-blogs%2F110_security-updates%2Fsecurity-update-guidance-for-netscaler-saml-authentication-deployments%2F)
- [{lang="reddit_text"](https://www.reddit.com/submit?url=https%3A%2F%2Fcommunity.citrix.com%2Ftechzone-blogs%2F110_security-updates%2Fsecurity-update-guidance-for-netscaler-saml-authentication-deployments%2F&title=Security+Update%3A+Guidance+for+NetScaler+SAML+Authentication+Deployments)
- [Share on LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fcommunity.citrix.com%2Ftechzone-blogs%2F110_security-updates%2Fsecurity-update-guidance-for-netscaler-saml-authentication-deployments%2F&title=Security+Update%3A+Guidance+for+NetScaler+SAML+Authentication+Deployments)
- [Share on Pinterest](https://pinterest.com/pin/create/button/?url=https://community.citrix.com/techzone-blogs/110_security-updates/security-update-guidance-for-netscaler-saml-authentication-deployments/&media=)
- [Share on X](https://x.com/share?url=https%3A%2F%2Fcommunity.citrix.com%2Ftechzone-blogs%2F110_security-updates%2Fsecurity-update-guidance-for-netscaler-saml-authentication-deployments%2F)
- [Followers](https://community.citrix.com/login/)
- [](https://community.citrix.com/profile/3266-phil-dusome-2/)
- [security bulletin](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174)
- [blog](https://community.citrix.com/techzone-blogs/110_security-updates/understanding-and-addressing-cve-2026-88779-in-citrix-netscaler-adc-and-citrix-netscaler-gateway/)
- [CTX697096](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096)
- [https://support.citrix.com/wolken-support/view/aboutsupport/my-support-alerts](https://support.citrix.com/wolken-support/view/aboutsupport/my-support-alerts)
- [2 Comments](https://community.citrix.com/techzone-blogs/110_security-updates/security-update-guidance-for-netscaler-saml-authentication-deployments/?&tab=comments)
- [Community Site Help](https://community.citrix.com/contact/)
- [Cookies](https://community.citrix.com/cookies/)
- [Citrix Tech Zone Document History](https://community.citrix.com/rss/1-citrix-tech-zone-document-history.xml/)
- [Citrix Tech Zone Blogs](https://community.citrix.com/rss/3-citrix-tech-zone-blogs.xml/)
- [Terms of Use](https://www.cloud.com/community-terms-of-use)
- [Privacy Policy](https://www.citrix.com/about/legal/privacy/)
- [Cookie Preferences](https://community.citrix.com/techzone-blogs/110_security-updates/security-update-guidance-for-netscaler-saml-authentication-deployments/#)
- [Your Privacy Choices](https://app.smartsheet.com/b/form/5a4f963f77fb4acc91bb6e4a3b47cda3)
- [0 Your Cart](https://community.citrix.com/store/cart/)
