---
title: "TeamUpdraft security incident: What customers need to know"
author: Joe Whittaker
url: https://teamupdraft.com/blog/security-incident-october-2026/
hostname: teamupdraft.com
description: On 18 October 2026, we detected unauthorised access to teamupdraft.com. Read our security notice and the steps customers should take to protect their accounts and connected services.
sitename: TeamUpdraft
date: "2026-10-19"
categories: ['Company news']
fingerprint: f1202149db666e9
---
# TeamUpdraft security incident: What customers need to know

## Security incident on teamupdraft.com: what happened, what we’ve done, and what you need to do

[Section titled Security incident on teamupdraft.com: what happened, what we’ve done, and what you need to do](https://teamupdraft.com#security-incident-on-teamupdraft-com-what-happened-what-we%e2%80%99ve-done-and-what-you-need-to-do)

*Last updated: 23nd October 2026 05:26 BST. We may update this page as our investigation continues.*


**Update 22nd Oct 14:42BST –**

Our support form was back up and available on our site late last night.

We’re asking our users to continue to be vigilant. It’s especially worth logging into [UpdraftCentral via ‘My Account](https://teamupdraft.com/my-account/updraftcentral-remote-control/)‘ and looking at the sites listed there.

If a site is listed that you didn’t knowingly connect since the 19th Oct, please check it for signs of compromise.

Here are some things to check on those sites:

- Any unusual/unexpected users (we’re seeing a pattern of unexpected ‘editor’ roles especially
- Any unrecognised plugins
- IPs you don’t recognise in the logs

If in doubt, please contact our customer support team.

**Update 21st Oct 15:35BST –**

We want to emphasise the importance for users of UpdraftPlus Premium to check your websites for signs of unusual activity. This could range from unexpected plugins to new admins. This is worth checking even if you’ve never used UpdraftCentral.

Secondly, in light of the ongoing issue affecting the PHP foundation – we’re taking our support form temporarily offline. Customers wishing to contact support can do so via the support forums. https://teamupdraft.com/support/ Choose between “premium support forums” and “ask for help (users of free plugins).

**Update 21st Oct 10:23BST –**

We just wanted to update you with a quick tl;dr list of established facts. As this is an ongoing incident, we don’t have all the answers yet – we’ll get them to you as soon as we do.

- We immediately took steps to lock down access and secure our site – there’s currently no evidence the attacker still has access
- We know the attacker used a compromised key to access our site.
- The speed of the exploits following the breach combined with the initially faulty backdoor plugins suggest that the hackers used AI to accelerate their attack.
- We have bought in an external leading cyber security firm to assist as an extra precaution (as well as our-in-house experts).
- We have contacted the relevant authorities (including the police) about this and are co-operating with them as they investigate.
- The update to UpdraftPlus pushed on the 19th (1.26.13 & 2.26.13) automatically disconnects user sites from UpdraftCentral by revoking connection keys.
- The attacker exploited the connection to users’ sites to create admin accounts, install malicious plugins etc – the extent of that is unknown so it’s important to check your sites for unexpected plugins, activity and users.

**Update 20th Oct 16:25BST –**

We’ve seen reports on other publications suggesting there is an ongoing attack. To be clear – the unauthorised access was resolved and an update to UpdraftPlus (1.26.13 and 2.26.13) published just after 10pm BST on the 19th revoked UpdraftCentral connection keys thus blocking any access across that vector. WordPress.org have pushed that out to all users so you don’t need to manually update (though it’s always worth checking you’re on the latest version).

It’s still important that users check over their sites for suspicious activities as listed in this blog post.

 **Original post**

Over the weekend of 17-18 October we identified unauthorised access to the teamupdraft.com website. Our team responded straight away and worked through the night to contain it – we closed the access route, signed out every account and replaced the keys and credentials that could have been affected.

This page explains what happened, what we have already done to protect you, and the steps to take for each of our products. Most users only need to change their password. If you use UpdraftCentral, please read that section and act on it today.

## What happened

[Section titled What happened](https://teamupdraft.com#what-happened)

We believe our customer database was accessed. It holds:

- names, email addresses, billing addresses and order history
- account passwords, stored only in hashed (scrambled) form and never in plain text
- two-factor authentication settings
- connection keys for UpdraftCentral, UpdraftVault and UpdraftClone

We do not store any card details. All card payments are handled by Stripe and PayPal.

The UpdraftPlus plugin itself and its downloads were not affected. Backups sent to your own remote storage, such as Google Drive, Dropbox or Amazon S3, are not affected. However, if your site was accessed through UpdraftCentral, please also re-authorise your remote storage and change any storage access keys, as a precaution.

Self-hosted UpdraftCentral is not affected.

## What we have already done

[Section titled What we have already done](https://teamupdraft.com#what-we-have-already-done)

- Closed the access route, deployed a fix for the underlying weakness, and continued to strengthen the website’s security
- Signed out every teamupdraft.com account and reset login security across the site
- Released UpdraftPlus 1.26.13 (free) and 2.26.13 (Premium), which automatically disconnect every UpdraftCentral connection made before 13:07 BST on 18 October, so the old keys stop working
- Disconnected every site from UpdraftVault and issued new credentials
- Replaced every UpdraftClone client key
- Rotated our keys with payment providers and other connected services
- Put additional monitoring in place, which we will keep running while we investigate
- Reported the incident to the Information Commissioner’s Office (ICO) and other relevant authorities

## What you need to do

[Section titled What you need to do](https://teamupdraft.com#what-you-need-to-do)

### Everyone with a teamupdraft.com account

[Section titled Everyone with a teamupdraft.com account](https://teamupdraft.com#everyone-with-a-teamupdraft-com-account)

1. Change your teamupdraft.com password. Type teamupdraft.com into your browser rather than following a link.
2. If you use the same password anywhere else, change it there too.
3. If you use two-factor authentication on teamupdraft.com, reset it in My Account.
4. Be cautious of unexpected emails that claim to be from us. We will never ask for your password or keys.

### UpdraftCentral (cloud) users: please do this today

[Section titled UpdraftCentral (cloud) users: please do this today](https://teamupdraft.com#updraftcentral-cloud-users-please-do-this-today)

Your UpdraftCentral connection keys can send commands to your connected sites, so please secure each site directly. For each site:

1. Log in to the site’s own WordPress dashboard, not through UpdraftCentral.
2. Update UpdraftPlus to version 1.26.13 (free) or 2.26.13 (Premium) or later.
3. Disconnect it from UpdraftCentral: go to Settings > UpdraftPlus > Advanced Tools > UpdraftCentral and delete the connection key.
4. Go to Users and check for any administrator accounts you don’t recognise. Remove them.
5. Go to Plugins, including the Must-Use tab if you can see it, and check for anything you don’t recognise. Remove it.
6. Change the passwords for all administrator accounts on the site.
7. If you find anything suspicious, consider restoring the site from a backup taken before 17 October.
8. Reconnect the site to UpdraftCentral.

UpdraftPlus 1.26.13 and 2.26.13 automatically disconnect the old connections, so please update every site, including any you don’t manage day to day. If you have already reconnected a site using the steps above, the update will not disconnect it again.

If you reconnect a site using the steps above, the update will not disconnect it again. We will update this page as soon as the release is available.

### UpdraftVault users

[Section titled UpdraftVault users](https://teamupdraft.com#updraftvault-users)

All sites have been disconnected from UpdraftVault, so backups won’t reach Vault until you reconnect. For each site:

1. Log in to the site’s WordPress dashboard and go to Settings > UpdraftPlus > Settings.
2. Under remote storage, click UpdraftVault, then under “Already got space?” click Connect.
3. Enter your teamupdraft.com email and your new password, then click Connect.
4. Click Save Changes, then run a manual backup to confirm it’s working.

### UpdraftClone users

[Section titled UpdraftClone users](https://teamupdraft.com#updraftclone-users)

Every client key has been replaced and the old keys no longer work. If you’ve never created a client key, you don’t need to do anything. If you’ve shared keys with your own clients, copy the new keys from My Account > UpdraftClone > UpdraftClone Key Management and send them on. Any clone using an old key will fail.

### Free UpdraftPlus users without a teamupdraft.com account

[Section titled Free UpdraftPlus users without a teamupdraft.com account](https://teamupdraft.com#free-updraftplus-users-without-a-teamupdraft-com-account)

You don’t need to take any action, though we always recommend keeping UpdraftPlus up to date. We recommend bookmarking this page for updates.

## Support

[Section titled Support](https://teamupdraft.com#support)

We know you trust us with your sites and backups, and we’re sorry for the concern this causes. Premium customers can contact us through the [Premium Support form](https://teamupdraft.com/support/premium-support-form). Everyone else can find updates on this page.

### About the author

#### Joe Whittaker

Joe heads up the Product, Marketing and Support function at TeamUpdraft. He’s a copywriter at heart but loves thinking about and solving complex problems. When not working, Joe likes to detox from his screen by visiting ancient monuments, spending time with his family and serving in his local church.

## Categories

## TeamUpdraft

We’re the team behind some of the WordPress community’s most loved WordPress plugins.

Developers, designers and website owners trust us to back up, migrate, optimize and secure more than **5 million WordPress websites worldwide**.

### More stories

- 
                    [All-In-One Security 5.5.0 brings clearer firewall logs and stronger login protection](https://teamupdraft.com/blog/all-in-one-security-5-5-0-release/)                    
                                            
                All-In-One Security 5.5.0 introduces dedicated firewall audit and debug logs, stronger protection for login lockouts, safer upgrades for larger sites, and a range of usability improvements to help secure and manage your WordPress website.
- 
                    [UpdraftPlus reaches 4 million active installations](https://teamupdraft.com/blog/updraftplus-4-million-active-installations/)                    
                                            
                UpdraftPlus has reached 4 million active installations. Thank you to the site owners, agencies and contributors who helped us get here.
- 
                    [UpdraftPlus 1.26.8: Easier setup and stronger security](https://teamupdraft.com/blog/updraftplus-1-26-8/)                    
                                            
                UpdraftPlus 1.26.8 makes getting started easier with a new onboarding wizard, plus stronger security and more reliable remote backups.
- 
                    [WP-Optimize 4.7.0: See Your Site’s Performance at a Glance](https://teamupdraft.com/blog/wp-optimize-4-7-0/)                    
                                            
                WP-Optimize 4.7.0 introduces a new dashboard overview, making it easier to see your site’s optimisation status at a glance. T
