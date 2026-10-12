---
title: Critical Unauthenticated Arbitrary File Upload Vulnerability Exploited in Bricksforge Plugin - Patchstack
author: Edouard
url: https://patchstack.com/articles/critical-unauthenticated-arbitrary-file-upload-vulnerability-exploited-in-bricksforge-plugin/
hostname: patchstack.com
description: This blog post covers a Critical unauthenticated arbitrary file upload vulnerability in the Bricksforge plugin for WordPress. Patchstack has deployed a mitigati
sitename: Patchstack
date: "2026-10-08"
categories: ['Featured', 'Security Advisories']
fingerprint: "111bd60363755681"
---
                    
                        
            [Bricksforge
            Unauthenticated Arbitrary File Upload
        
    
        
            
        
        
            
            6K
        
        
            CVSS 10.0](https://patchstack.com/database/WordPress/Plugin/bricksforge/vulnerability/wordpress-bricksforge-plugin-3-1-8-9-unauthenticated-arbitrary-file-upload-via-temporaryfileuploads-parameter-vulnerability)
        
        
    

This blog post covers a Critical unauthenticated arbitrary file upload vulnerability in the [Bricksforge](https://bricksforge.io/) plugin for WordPress. Patchstack has deployed a mitigation rule to protect against exploitation of this vulnerability. If you are a Bricksforge user, **update to at least version 3.1.8.10.**

This vulnerability is currently being targeted in the wild. Tracked as [CVE-2026-85097](https://www.cve.org/CVERecord?id=CVE-2026-85097), the issue allows unauthenticated attackers to **upload and execute arbitrary PHP code** on vulnerable WordPress websites, leading to remote code execution (RCE). It affects Bricksforge versions up to and including 3.1.8.9. A fix is available in version 3.1.8.10, and organizations running affected versions should upgrade as soon as possible.

Our telemetry shows active exploitation attempts targeting Bricksforge installations, with activity first observed on **October 7, 2026, at 21:47 UTC**.

| **CVE** | CVE-2026-85097 | 
| **Product** | Bricksforge | 
| **Vulnerability Type** | Unauthenticated Arbitrary File Upload / RCE | 
| **CVSS** | 10.0 (Critical) | 
| **Exploitation Status** | Active exploitation observed | 
| **Authentication Required** | No | 
| **Affected Versions** | ≤ 3.1.8.9 | 
| **Fixed Version** | 3.1.8.10 | 
| **Vendor Advisory** | [Bricksforge changelog](https://bricksforge.io/version-changelog/) | 
| **First Observed Exploitation** | October 7, 2026, 21:47:17 UTC | 

✌️ Our users are protected from this vulnerability. Are yours?

Identify vulnerabilities in your plugins and get recommendations for fixes.

[Request audit](https://patchstack.com/auditing/)

Protect your users, improve server health and earn additional revenue.

[Patchstack for hosts](https://patchstack.com/for-hosts/)

## **About the Bricksforge plugin**

Bricksforge is a WordPress plugin designed to extend the functionality of Bricks Builder, a visual website-building tool for WordPress. It provides additional features for building dynamic and interactive websites, including advanced forms, animations, custom interactions, dynamic data management, and backend customization.

## **How the vulnerability works**

Bricksforge validates a file’s MIME type when it is first uploaded. When a form is later submitted, however, **it trusts the file metadata the client sends.** In particular, it does not validate the `url` field inside the `temporaryFileUploads` parameter. That gap gives attackers a four-step path to code execution:

1. Request a valid nonce from the unauthenticated `bricksforge_regenerate_nonce` AJAX endpoint.
2. Upload a GIF/PHP polyglot: a file that is a valid image but also contains PHP code. It passes the MIME check and lands in the temporary upload directory.
3. Submit a form where the `file` path points to that validated image, but the `url` ends in a PHP extension.
4. Bricksforge trusts the submitted metadata and places the file’s contents at the PHP location. When that file is requested, the server executes the embedded code.

The result is arbitrary PHP execution on the server. From there, an attacker can deploy web shells, modify site content, read sensitive data, and establish persistent access.

**The code location where metadata is injected via temporaryFileUploads:**

\[…\]

*bricksforge/includes/elements/pro-forms/actions/init.php*

**The code location that subsequently allows arbitrary file uploads:**

*bricksforge/includes/ele*ments/pro-forms/actions/base.php

## **What we’re seeing**

All but one of the exploitation attempts targeted the Bricksforge REST API form submission endpoint:

`POST /wp-json/bricksforge/v1/form_submit`
The remaining request hit `/wp-admin/admin-ajax.php` with the `bricksforge_form_submit` action. Every request included a crafted `temporaryFileUploads` parameter. Here is a representative payload, normalized from the structure we observed:

```
{
  "temporaryFileUploads": [
    {
      "field": "form-field-file",
      "file": {
        "file": "/var/www/example.com/wp-content/uploads/bricksforge/tmp/img_example.gif",
        "url": "https://example.com/wp-content/uploads/bricksforge/tmp/img_example.php",
        "type": "image/gif"
      }
    }
  ]
}
```
The key signature is the mismatch: the server-side path is an image, and the destination URL is a PHP file. In 95% of captured requests, the server-side path ended in `.gif` or `.png`, and most of those paired it with a PHP-related destination URL.

Most payloads referenced files in the Bricksforge temporary directory, `/wp-content/uploads/bricksforge/tmp/`. Some aimed further. These used destination filenames matching `login_admin_*.php` to place PHP files in the regular WordPress uploads directory, such as `/wp-content/uploads/2026/10/`.

## **Payload variations**

Attackers are actively probing for ways around extension filtering. We observed four kinds of variation:

- **Alternative PHP extensions:** `.php`, `.php5`, `.php7`, `.php8`, `.phtml`, `.pht`, `.phtm`, and `.phps`.
- **Case manipulation:** `.PHP`, `.Php`, `.pHp`, and `.PHTML`.
- **Encoded extensions:** URL-encoded and double-encoded forms such as `%2ephp`, `.%70hp`, and `.%2570%2568%2570`.
- **Modified metadata:** altered or missing `path`, `name`, `originalFilename`, and `url` fields, used to test how the plugin validates and processes files.

## **Signs of coordinated, automated activity**

Two clusters stand out in our telemetry. In the first, 44 IPs sent 56 requests with identical payloads within seconds of each other. In the second, three IPs tested 25 variations of PHP extensions and encodings against the same temporary file.

Both patterns point to **automated exploitation** over rotating proxies or distributed infrastructure. They do not, on their own, attribute the activity to a single threat actor.

## **Source IP addresses**

We recorded 63 unique source IPs. The six most active accounted for about 46% of all requests:

| IP address | Network | AbuseIPDB reports | CleanTalk blacklist | 
|---|---|---|---|
| 177.75.57.20 | EXPLORERNET (Brazilian fixed-line ISP) | 8 | No | 
| 23.97.62.146 | Microsoft Azure | 1,270+ | No | 
| 84.247.60.125 | HostRoyale | 12 | Yes | 
| 38.154.185.97 | B2 Net Solutions | 11 | Yes | 
| 150.109.16.166 | Tencent | 185 | Yes | 
| 153.75.90.146 | Cloudzy (Datacenter) | 35 | Yes | 

The infrastructure is **mixed:** datacenter servers, cloud providers, VPN and proxy services, and residential or fixed-line ISP connections. The most active address, 177.75.57.20, is the outlier. It sits on a Brazilian fixed-line ISP rather than in a datacenter, and it has almost no prior abuse history.

## **Detection**

Review your HTTP and application logs for these indicators:

- Requests to `/wp-json/bricksforge/v1/form_submit` that contain a `temporaryFileUploads` parameter.
- Upload metadata where an image path (`.gif`, `.png`) is paired with a PHP-related destination URL.
- Calls to the `bricksforge_regenerate_nonce` AJAX action, followed by an upload and a form submission.
- Repeated form submissions cycling through file extensions, encodings, or capitalization.
- Unexpected PHP files in `/wp-content/uploads/bricksforge/tmp/` or any other uploads directory, especially files named `login_admin_*.php`.
- HTTP requests to newly created PHP files in upload directories.

If a site ran a vulnerable version without protection, **review historical logs** and the host itself for unexpected PHP files, unusual application activity, and unauthorized changes.

## **What to do now**

Update Bricksforge to **version 3.1.8.10 or later.** That closes the vulnerability.

If you can’t update right away, [Patchstack’s RapidMitigate rule for CVE-2026-85097](https://patchstack.com/database/WordPress/Plugin/bricksforge/vulnerability/wordpress-bricksforge-plugin-3-1-8-9-unauthenticated-arbitrary-file-upload-via-temporaryfileuploads-parameter-vulnerability) blocks these exploitation attempts at the traffic layer, without touching plugin code. The rule was live before the first attack arrived, which is the point: close the window between disclosure and exploitation, before attackers can use it.

We’re continuing to monitor this campaign for new payload variations and bypass attempts, and we’ll update this post as the activity evolves.

🤝 You can help us make the Internet a safer place

Streamline your disclosure process to fix vulnerabilities faster and comply with CRA.

[Get started for free](https://patchstack.com/for-plugins/)

Protect your users too! Improve server health and earn added revenue with proactive security.

[Patchstack for hosts](https://patchstack.com/for-hosts/)

Report vulnerabilities to our gamified bug bounty program to earn monthly cash rewards.

[Learn more](https://patchstack.com/bug-bounty/)
