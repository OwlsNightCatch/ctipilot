---
title: "Rank Math PRO 3.0.123 Security Incident: How to Secure Your Website » Rank Math"
url: https://rankmath.com/kb/pro-3-0-123-security-incident/
hostname: rankmath.com
description: We recently identified a security issue affecting a limited number of users who downloaded Rank Math PRO v3.0.123 between October 15, 2026, at 20:02 UTC and
sitename: Rank Math
date: "2026-10-16"
categories: ['Troubleshooting']
fingerprint: bc03ae0209670788
---
We recently identified a security issue affecting a limited number of users who downloaded Rank Math PRO v3.0.123 between October 15, 2026, at 20:02 UTC and October 16, 2026, at 07:12 UTC.

The affected plugin files contained malware that could compromise your website if the plugin was activated. We immediately removed the affected files and released a clean version, Rank Math PRO v3.0.124.

**If you downloaded or updated to the affected version during this period, follow the instructions below to secure your website.** We understand that security issues can be concerning, and we’re here to help you work through the necessary steps.

## 1. Check if your website is affected

First, log in to your WordPress admin area and navigate to **Plugins** to check your installed Rank Math PRO version.

- **You installed and activated version 3.0.123 during the affected period:** Treat your website as compromised and follow the recovery steps in Section 2.
- **You installed version 3.0.123 but never activated it:** Delete the affected plugin files, install the clean version 3.0.124 from your Rank Math account, and run a security scan as a precaution.
- **You downloaded version 3.0.123 but did not install or activate it:** There is no indication from this incident alone that your website was compromised. If you’re unsure whether the affected files were installed or activated, [contact our support team](https://rankmath.com/support/) for assistance.

If you’ve received an email from us, then please follow the steps we’ve discussed below.

## 2. Secure your website

If you activated the affected version, we recommend restoring your website and database from a backup created before the incident began.

### Option 1: Restore from a clean backup

If you have a backup created before October 15<sup>th</sup> 20:02 UTC / 22:02 CEST /16:02 EDT, which equates to October 16<sup>th</sup> 01:32 IST, this is our recommended recovery option.

1. **Restore your website and database** from a backup created before the affected period began.
2. **Run a security scan** using a reputable security tool such as [Wordfence](https://wordpress.org/plugins/wordfence/) or [Sucuri](https://wordpress.org/plugins/sucuri-scanner/).
3. **Change all passwords and credentials.** Assume any secrets on your site are exposed, and change all passwords, database credentials, API keys etc. Follow Section 4 below to review and replace potentially exposed credentials.
4. **Install the clean version of Rank Math PRO.** Download version 3.0.124 from your Rank Math account and install it after restoring your website.

**If you’re unsure how to restore a backup, contact your hosting provider for assistance.**

### Option 2: Clean your website manually

If restoring from a clean backup isn’t possible, you’ll need to remove the malware and check your website for other changes made by the attacker.

**Important:** Follow these steps in order. The malware can recreate its hidden backdoor whenever someone visits the website. Removing suspicious files before disabling the mechanism that recreates them may not resolve the issue.

If you’re not comfortable working with website files, databases, or server settings, we strongly recommend asking your hosting provider or a qualified security professional to perform these steps.

#### Step 1: Stop the malware from rebuilding itself

Complete all the following actions before proceeding to Step 2.

1. **Delete the entire Rank Math PRO plugin folder.** Using your hosting file manager or FTP, locate and delete the `rank-math-pro` folder. Deactivating the plugin alone is not sufficient.
2. **Remove the malicious database entry.** Open your WordPress database using a tool such as phpMyAdmin. In the `wp_options` table, find and delete the entry whose `option_name` matches one of the following values:
  - `_uf6qdn2hmm`
  - `t8krdk990phb`
  - `_np5pvf754c`
3. **Block the malicious domain if possible.** If your hosting provider or firewall supports it, block outgoing connections to `rank1cdn.com`.

Only proceed to the next step after completing these actions.

#### Step 2: Find and remove other malicious changes

The attacker may have left additional files, accounts, or server-level changes behind. Check each of the following areas.

**Hidden backdoor files**

Check these locations for suspicious PHP files:

- `wp-content/mu-plugins/`
- Folders belonging to other plugins
- The `inc/`, `includes/`, and `lib/` folders of non-default themes
- The Rank Math `includes/` folder

Look for PHP code containing `base64_decode` combined with XOR loops, the key `xmmqhn`, `proc_open`, or PHP-FPM socket code.

A security plugin or your hosting provider can help search for these indicators and remove any malicious files.

**Unknown administrator accounts**

Review your WordPress users and check for unfamiliar accounts with administrator privileges. Look for suspicious usernames beginning with `wpsupport_` followed by random characters, or accounts using email addresses ending in `@wp-mail[.]net`.

Remove any accounts confirmed to be malicious or unauthorized.

You can also list administrator accounts using WP-CLI:

`wp user list --role=administrator`

**Fake WordPress core file**

Check for the following file:

`wp-includes/class-wp-cache-util.php`

This is not a legitimate WordPress core file. If present, remove it and run:

`wp core verify-checksums`

Reinstall WordPress core files from an official source to ensure that no other core files have been altered.

**The .htaccess file and suspicious .cache files**

Check the `.htaccess` file in your website’s root directory and any subdirectories. Look for rules that allow `.cache` files to execute as PHP code.

Search your server for `.cache` files containing PHP code and investigate any suspicious findings.

**Scheduled tasks and cron jobs**

Review the system crontab for the web server user and look for entries tagged `#ms6v46`.

Also, use WP-CLI to review scheduled WordPress events:

`wp cron event list`

Investigate and remove any malicious scheduled tasks.

**Other plugins, themes, and uploaded files**

- Reinstall plugins and themes from their official sources, comparing them with clean copies where possible.
- Check the `uploads/` directory for PHP files, which generally should not be present there.
- Investigate any unexpected or modified files before removing them.

**The server environment**

The attacker may have made changes outside your WordPress installation. Review:

- SSH `authorized_keys` files
- Crontabs belonging to other system users
- Running processes
- Locations outside the website directory where the web server user has write access

If you use shared hosting and cannot access these areas, ask your hosting provider to investigate them.

#### Step 3: Change all passwords and credentials

**This step is essential, even if you restore your website from a backup.**

As a precaution, assume that credentials and secrets accessible to the compromised website may have been exposed. Replace them with new, secure values.

Review and rotate the following:

- **All passwords:** Change relevant passwords, including WordPress accounts and other credentials accessible to the compromised site.
- **Database credentials:** Update the database username and password configured in `wp-config.php`.
- **WordPress security keys and salts:** Regenerate the keys and salts in `wp-config.php`.
- **API keys and service credentials:** Replace payment gateway keys, SMTP credentials, API keys, and other secrets stored in website settings or configuration files.
- **Hosting and server access:** Change hosting control panel, FTP/SFTP, and SSH passwords or credentials. Review secrets stored in environment variables.
- **Two-factor authentication:** Review two-factor authentication for administrator accounts and reset it where necessary.

Update your website configuration and connected services with the new credentials wherever required. If you’re unsure which credentials need to be replaced, ask your hosting provider or security professional to help review them.

#### Step 4: Verify your website is clean

After completing the cleanup:

1. Run a security scan using a reputable tool such as Wordfence or Sucuri.
2. Verify WordPress core files using:`wp core verify-checksums`
3. Verify installed plugin files using:`wp plugin verify-checksums --all` Note that checksum verification may not be available for every plugin, particularly premium plugins. Use a clean copy from the official source to verify files when checksums are unavailable.
4. Monitor outgoing connections and check for suspicious activity over the following days.
5. Check whether any files you removed reappear.

If suspicious files return or you notice unusual activity, the cleanup may be incomplete. Revisit Step 2 and ask your hosting provider or security professional to investigate further.

## 3. Install the clean version of Rank Math PRO

Once you’ve completed the applicable recovery steps, install the clean version of Rank Math PRO, **v3.0.124**.

To download it, visit `rankmath.com` directly and log in to your account. Navigate to your downloads and download the updated plugin.

Some users may be unable to log in and may need to reset their account password.

For your security, always navigate to `rankmath.com` directly. We will never send login or download links by email. Treat unsolicited emails asking you to click a password-reset or download link as suspicious.

## 4. Need help?

We understand how important your website’s security is. Our team is giving this incident our full attention and is taking steps to reduce the risk of similar incidents in the future.

If you need assistance identifying the appropriate recovery steps or have concerns about your website, contact us at [**\[email protected\]**](https://rankmath.com/cdn-cgi/l/email-protection#2e5d5b5e5e415c5a6e5c4f4045434f5a46004d4143) or [open a support ticket here](https://rankmath.com/support/).

Please include relevant details about your Rank Math PRO version and the recovery steps you’ve already completed so our team can better understand your situation.

We’re committed to helping you secure your website and appreciate your patience as we work through this incident.
