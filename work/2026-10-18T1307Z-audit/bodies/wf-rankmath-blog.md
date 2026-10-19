Title: PSA: Malware Found in Some Rank Math SEO PRO 3.0.123 Downloads

URL Source: https://www.wordfence.com/blog/2026/10/rank-math-seo-pro-3-0-123-malware/

Published Time: 2026-10-17T03:41:48+00:00

Markdown Content:
Rank Math has disclosed that some copies of Rank Math SEO PRO version 3.0.123 contained malware. According to Rank Math, the affected version was downloaded or installed through an update between October 15, 2026 at 20:02 UTC and October 16, 2026 at 07:12 UTC.

If an affected copy of Rank Math SEO PRO 3.0.123 was active on your website, you should treat the website as compromised. Simply updating the plugin is not enough because the malware may have placed additional files, administrator accounts, or scheduled tasks elsewhere on the server.

Rank Math removed the affected files and released version 3.0.124 as the clean replacement. Version 3.0.123 by itself does not prove that a website was compromised: Rank Math limits the incident to users who downloaded or updated to the affected version during the stated period.

Website owners should check when version 3.0.123 was downloaded or installed, follow the recovery guidance below, and use [Rank Math’s security notice](https://rankmath.com/kb/pro-3-0-123-security-incident/) as the authoritative source for updates about this incident.

### Vulnerability Summary from Wordfence Intelligence

CVSS Rating  
**9.8 (Critical)**

Affected Version(s)  
**3.0.123**

Patched Version  
**3.0.124**

**Affected Software**

**Researcher(s):** Unknown

Rank Math SEO PRO for WordPress is affected by a supply-chain compromise in a subset of version 3.0.123 packages downloaded or updated between October 15, 2026 at 20:02 UTC and October 16, 2026 at 07:12 UTC. Rank Math states that the affected plugin files contained malware that could compromise a website if the plugin was activated and directs sites that activated an affected package to treat the website as compromised. The malware may establish persistent access, communicate with rank1cdn[.]com, recreate hidden backdoors on page visits, and expose WordPress credentials, database credentials, API keys, and other secrets accessible to the web server. Rank Math identifies three malicious wp_options keys, hidden PHP backdoors, unauthorized administrator accounts, a fake WordPress core file, PHP-executable .cache files, and a system cron marker as incident indicators. Only packages obtained during the vendor-confirmed window are claimed as affected; version 3.0.123 alone is not sufficient to establish compromise. Rank Math removed the affected files and released version 3.0.124 as the clean replacement.

### Who Is Affected?

Your website may be affected if it downloaded or updated to Rank Math SEO PRO 3.0.123 during the following period:

*   **Start:** October 15, 2026 at 20:02 UTC
*   **End:** October 16, 2026 at 07:12 UTC

Rank Math provides the following guidance:

*   If you installed and activated an affected copy of version 3.0.123, treat the website as compromised and complete a full recovery.
*   If you installed version 3.0.123 but never activated it, delete the affected plugin files, install version 3.0.124 from your Rank Math account, and run a security scan.
*   If you downloaded version 3.0.123 but never installed or activated it, Rank Math says there is no indication from this incident alone that your website was compromised.

Rank Math says it has records identifying users who downloaded an affected copy. If Rank Math notified you, follow its recovery instructions even if your website is now running a different version.

### What Website Owners Should Do Now

If an affected copy was activated, Rank Math recommends restoring the website and its database from a clean backup created before October 15, 2026 at 20:02 UTC. After restoring the backup, scan the website, replace passwords and other sensitive credentials that the website could access, and then install Rank Math SEO PRO 3.0.124 directly from your Rank Math account.

If a suitable backup is not available, Rank Math advises having the website cleaned manually. This work should be performed by an experienced security professional or hosting provider if you are not comfortable working with website files, the database, and server settings.

Before removing other suspicious files, complete the following steps to prevent the malware from recreating its hidden backdoor when someone visits the website:

1.   Delete the entire `rank-math-pro` plugin folder. Deactivating the plugin is not enough.
2.   Delete any entry in the WordPress `wp_options` database table whose `option_name` is `_uf6qdn2hmm`, `t8krdk990phb`, or `_np5pvf754c`.
3.   Block outgoing connections to `rank1cdn[.]com` if your hosting provider or firewall supports it.

Once the mechanism that recreates the malware has been disabled, check the rest of the website and server for the signs listed below. Reinstall WordPress, plugins, and themes from trusted sources where appropriate.

Changing passwords is essential even if the site is restored from a backup. Rank Math recommends replacing WordPress passwords, database credentials, WordPress security keys and salts, payment and email service credentials, API keys, hosting control-panel credentials, and FTP, SFTP, or SSH credentials that may have been accessible to the website. Review two-factor authentication settings for administrator accounts as well.

### What the Malware Can Do

Rank Math states that the affected plugin files contained malware that could compromise a website when the plugin was activated. The company warns that the malware can recreate a hidden backdoor when the website is visited and that the attacker may have left additional files, unauthorized administrator accounts, scheduled tasks, or server-level changes behind.

Rank Math advises site owners to assume that credentials and secrets accessible to the compromised website may have been exposed. This includes WordPress passwords, database credentials, API keys, and other stored secrets. Updating to version 3.0.124 replaces the affected Rank Math package, but it does not remove files, accounts, or scheduled tasks that the malware may already have created elsewhere.

### Indicators of Compromise

The following signs come from Rank Math’s security notice. Their presence should be investigated. Their absence does not, by itself, prove that a website is clean.

#### Network Activity

*   Outgoing connections to `rank1cdn[.]com`

#### WordPress Database

*   An entry in the `wp_options` table named `_uf6qdn2hmm`
*   An entry in the `wp_options` table named `t8krdk990phb`
*   An entry in the `wp_options` table named `_np5pvf754c`

#### Administrator Accounts

*   Unknown administrator usernames beginning with `wpsupport_`
*   Unknown accounts using an email address ending in `@wp-mail[.]net`

#### Files and Server Changes

*   `wp-includes/class-wp-cache-util.php`. Rank Math states that this is not a legitimate WordPress core file.
*   PHP files in unexpected locations, including `wp-content/mu-plugins/`, folders belonging to other plugins, the `inc/`, `includes/`, and `lib/` folders of non-default themes, and the Rank Math `includes/` folder.
*   Suspicious PHP code containing `base64_decode` with XOR loops, the key `xmmqhn`, `proc_open`, or PHP-FPM socket code.
*   Rules in a root or subdirectory `.htaccess` file that allow `.cache` files to run as PHP.
*   `.cache` files containing PHP code.
*   System scheduled tasks for the web server user containing the marker `#ms6v46`.
*   Unexpected PHP files in the WordPress `uploads` directory.

Rank Math also recommends reviewing WordPress scheduled events, SSH authorized keys, scheduled tasks belonging to other system users, running processes, and locations outside the website directory where the web server can write files.

### How to Verify the Website After Cleanup

After recovery, run a full security scan and continue watching the website for unusual behavior. Rank Math specifically recommends checking WordPress core files with:

`wp core verify-checksums`

Plugin files can be checked with:

`wp plugin verify-checksums --all`

Checksums are not available for every premium plugin, so compare those files with a clean copy downloaded directly from the developer. Monitor outgoing connections and confirm that removed files do not return. If suspicious files reappear, the cleanup is incomplete.

Download Rank Math SEO PRO 3.0.124 by navigating directly to `rankmath.com` and signing in to your account. Rank Math says it will not send login or download links by email, so treat unexpected messages containing those links as suspicious.

### Timeline

*   **October 15, 2026 at 20:02 UTC:** The affected download and update period began.
*   **October 16, 2026 at 07:12 UTC:** The affected period ended.
*   **October 16, 2026:** Rank Math published its security notice and directed affected users to install the clean version, 3.0.124, after completing the appropriate recovery steps.

### Conclusion

Rank Math says this incident affected a limited number of users who downloaded or updated to Rank Math SEO PRO 3.0.123 during a specific period. Version 3.0.123 alone is not evidence that a website was compromised. However, any website on which an affected copy was active should be treated as compromised.

If your site may be affected, first establish when version 3.0.123 was obtained. If an affected copy was active, restore the website and database from a clean backup created before the incident whenever possible. If no suitable backup is available, follow Rank Math’s manual-cleanup steps in the stated order. In either case, replace exposed credentials and other secrets, install the clean version 3.0.124, scan the full website and server, and monitor for signs that the malware has returned.

Wordfence Care and Wordfence Response customers can contact our team for help investigating and cleaning a compromised website. Our incident response team can identify and remove malware, help determine the cause of an infection, and assist with the recovery process. Learn more about [Wordfence Care](https://www.wordfence.com/products/wordfence-care/) and [Wordfence Response](https://www.wordfence.com/products/wordfence-response/).

Links/Buttons:
- [Get Help](https://www.wordfence.com/wordfence-site-cleanings/?promo_id=top-get-help&promo_name=get-site-clean&promo_creative=yellow-txt&promo_position=sw-top)
- [Create Account](https://www.wordfence.com/wp-login.php?action=register)
- [Sign In](https://www.wordfence.com/wp-login.php)
- [](https://trust.defiant.com/)
- [Products](https://www.wordfence.com/products/)
- [Wordfence Free](https://www.wordfence.com/products/wordfence-free/)
- [Wordfence Premium](https://www.wordfence.com/products/wordfence-premium/)
- [Wordfence Care](https://www.wordfence.com/products/wordfence-care/)
- [Wordfence Response](https://www.wordfence.com/products/wordfence-response/)
- [Wordfence CLI](https://www.wordfence.com/products/wordfence-cli/)
- [Wordfence Intelligence](https://www.wordfence.com/products/wordfence-intelligence/)
- [Wordfence Central](https://www.wordfence.com/products/wordfence-central/)
- [Compare Plans](https://www.wordfence.com/products/pricing/)
- [Intelligence](https://www.wordfence.com/threat-intel/)
- [All Vulnerabilities](https://www.wordfence.com/threat-intel/vulnerabilities/)
- [Plugins](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/)
- [Themes](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-themes/)
- [WordPress Core](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-core/)
- [Researchers](https://www.wordfence.com/threat-intel/vulnerabilities/researchers/)
- [Overview](https://www.wordfence.com/threat-intel/vendor/vulnerability-management-portal/)
- [Submit Vulnerability](https://www.wordfence.com/threat-intel/vulnerabilities/submit/)
- [Register](https://www.wordfence.com/threat-intel/vendor/register/)
- [Access Dashboard](https://www.wordfence.com/researcher-dashboard/)
- [Access Portal](https://www.wordfence.com/threat-intel/vendor/portal/)
- [API Access](https://www.wordfence.com/help/wordfence-intelligence/v3-accessing-and-consuming-the-vulnerability-data-feed/)
- [Webhook Integration](https://www.wordfence.com/help/wordfence-intelligence/wordfence-intelligence-webhook-notifications/)
- [Support](https://www.wordfence.com/help/)
- [Learning Center](https://www.wordfence.com/learn/)
- [Free Support](https://wordpress.org/support/plugin/wordfence/)
- [Premium Support](https://support.wordfence.com/)
- [News](https://www.wordfence.com/blog/)
- [In The News](https://www.wordfence.com/news/)
- [WP Security Mailing List](https://www.wordfence.com/subscribe-to-the-wordfence-email-list/)
- [Vulnerability Advisories](https://www.wordfence.com/vulnerability-advisories/)
- [About](https://www.wordfence.com/about-wordfence/)
- [Employment](https://www.wordfence.com/employment/)
- [Security](https://www.wordfence.com/security/)
- [CVE Request Form](https://www.wordfence.com/request-cve/)
- [Contact](https://www.wordfence.com/contact/)
- [Privacy Policy](https://www.wordfence.com/privacy-policy)
- [Terms of Service](https://www.wordfence.com/terms-of-service/)
- [Alex Thomas](https://www.wordfence.com/blog/author/wfalext/)
- [Rank Math’s security notice](https://rankmath.com/kb/pro-3-0-123-security-incident/)
- [Rank Math SEO PRO 3.0.123 - Unauthenticated Embedded Malicious Code](https://www.wordfence.com/threat-intel/vulnerabilities/id/81cd7a2c-ad0c-4dbc-b5dc-07ec866d5c1f)
- [CVE-2026-111862](https://www.cve.org/CVERecord?id=CVE-2026-111862)
- [Rank Math SEO PRO](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/seo-by-rank-math-pro)
- [Facebook](http://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.wordfence.com%2Fblog%2F2026%2F10%2Frank-math-seo-pro-3-0-123-malware%2F)
- [X (Twitter)](https://x.com/share?url=https%3A%2F%2Fwww.wordfence.com%2Fblog%2F2026%2F10%2Frank-math-seo-pro-3-0-123-malware%2F&text=PSA%3A%20Malware%20Found%20in%20Some%20Rank%20Math%20SEO%20PRO%203.0.123%20Downloads&via=wordfence)
- [LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fwww.wordfence.com%2Fblog%2F2026%2F10%2Frank-math-seo-pro-3-0-123-malware%2F)
- [Affiliate Program](https://www.wordfence.com/affiliate/)
- [Cookie Policy](https://www.wordfence.com/cookies-notice)
- [privacy@defiant.com](mailto:privacy@defiant.com)
