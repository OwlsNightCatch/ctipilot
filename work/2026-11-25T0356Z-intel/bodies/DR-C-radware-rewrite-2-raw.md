---
title: "Radware Breach: Cloud Keys Exposed and What to Do Now"
author: Team Thetechhacker
url: https://thetechhacker.com/news/radware-breach-cloud-access-keys-what-customers-should-do/
hostname: thetechhacker.com
description: A reported Radware breach may have exposed S3, Azure and SFTP log keys. What was accessed, what's unknown, and the steps customers should take now.
sitename: Thetechhacker
date: "2026-11-25"
categories: ['News']
tags: ['Cloud', 'Cybersecurity', 'Data Breach', 'Radware']
fingerprint: adfba61acd06754d
language: en
image: https://thetechhacker.com/wp-content/uploads/2026/11/Radware-Cloud-WAF.webp
pagetype: article
filedate: "2026-11-25"
---
[News](https://thetechhacker.com/news/)

# Radware Breach Reportedly Exposed Cloud Access Keys: What Customers Should Do

A reported Radware breach may have exposed S3, Azure and SFTP log keys. What was accessed, what's unknown, and the steps customers should take now.

If your website sits behind Radware’s Cloud WAF, check your log storage keys today. [BleepingComputer reports](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/) that an unauthorized party got into a Radware management system on November 19 and may have reached customer contact details. For some customers, the exposed data may include **credentials for AWS S3, Azure Blob Storage or SFTP**. The report is based on a Radware root cause analysis shared by an unnamed source. We found no public advisory from Radware, so everything below about the breach is as reported. The fix doesn’t need to wait, because rotating keys is quick and low risk.

**Quick answer:** Radware reportedly found that an internal Cloud WAF management API was **open to the internet without a login**, and someone accessed it on **November 19, 2026**. Customer contact details and, for a subset, **log export credentials** may have been accessed. Radware reportedly says traffic inspection, certificates and end users’ data weren’t exposed. If you export WAF logs to **AWS S3, Azure Blob or SFTP**, **rotate those credentials now** and review storage access logs **since at least November 19**. The number of affected customers isn’t known.

## What reportedly happened

- **How they got in:** an internal-only management API could be reached from the public internet without authentication.
- **When:** November 19. Radware reportedly detected it ten hours after the first access.
- **Radware’s response:** it blocked the source IP and API access, then revoked and replaced internal account credentials.
- **Still open:** who did it, how long the API was exposed, how many customers are affected, and whether stolen keys worked.

Some customers have reported AWS alerts about an unfamiliar IP address trying to reach their log buckets, according to BleepingComputer. The report doesn’t say any attempt succeeded. Radware is said to serve more than 12,500 customers, but that’s its total, not the number affected.

## What was and wasn’t exposed

| Data | Reported status | 
|---|---|
| Customer contact details | Potentially accessed | 
| S3, Azure Blob and SFTP log export credentials | Potentially accessed for a subset | 
| WAF traffic inspection and application traffic | Not exposed | 
| Certificates | Not exposed | 
| End users’ data | Not exposed | 
| Cloud DDoS services and data | Not exposed | 

We’d be careful with the comforting half of that table. WAF logs often hold IP addresses, URLs and request details. If someone used your key to open the bucket, your logs could be exposed even though Radware’s inspection systems weren’t.

## What Radware customers should do now

1. **Find your log export settings.** List every S3 bucket, Azure container or SFTP server that receives Radware AppSec logs.
2. **Rotate the credentials.** Follow the official steps for [AWS access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id-credentials-access-keys-update.html) or [Azure storage keys](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage). Replace SAS tokens and SFTP passwords or keys too.
3. **Delete the old keys.** A new key doesn’t help if the old one still works. Create the new key, update Radware, confirm that logs arrive, then remove the old key.
4. **Review access logs from November 19 or earlier.** Look for unknown IPs, list and download requests, and failed attempts. On AWS, see [S3 server access logs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html). If logging was off, note that gap.
5. **Shrink the permissions.** A log export key should only write to one location. If yours could read or delete, or reach other buckets, treat this as more serious.
6. **Ask Radware directly** whether your account is in the affected subset, through its [support portal](https://support.radware.com/).
7. **Expect phishing.** Exposed contact details make fake “Radware security” messages easy to write.

Steps 3 and 5 are our advice. Rotating credentials and reviewing logs is what Radware reportedly told customers “strongly” to do.

## Don’t use Radware?

The lesson still applies. Any vendor that exports data into your cloud holds a key to it. List those keys, limit what each can do, and set alerts for unfamiliar IPs. It’s the same supplier risk we saw when [malicious code reached 178 sites through Optimizely](https://thetechhacker.com/news/optimizely-security-incident-malicious-code-178-sites/). Security teams should also check the new [VMware vCenter flaw](https://thetechhacker.com/news/vmware-vcenter-cve-2026-123903-patch/), and smaller teams can work through our [data breach checklist](https://thetechhacker.com/2026/11/18/what-to-do-after-a-data-breach-checklist/).

## FAQs

### What was exposed in the Radware breach?

Customer contact details and, for a subset of customers, log export credentials for AWS S3, Azure Blob Storage or SFTP may have been accessed, BleepingComputer reports.

### Was website visitor data stolen?

Radware reportedly says end users’ data, certificates and application traffic weren’t exposed. Customers should still check whether anyone opened their exported logs.

### How many Radware customers are affected?

That isn’t known. The 12,500 figure in reports is Radware’s total customer base.

### Has Radware confirmed the breach publicly?

We found no public Radware advisory as of November 24. BleepingComputer’s report is based on a Radware root cause analysis report.

*Featured image: [Radware](https://www.radware.com/).*

*Disclosure: TheTechHacker has no paid relationship with Radware or any company mentioned here.*

## More in *News*

[View all →](https://thetechhacker.com/news/)

[NewsDigiCert Breach: Company Discloses Unauthorized Access to Business System Holding Customer DataDigiCert disclosed unauthorized access to a business system holding archived customer data. Here's what's confirmed, what's reported and what to do next.](https://thetechhacker.com/news/digicert-breach-customer-data/)

[NewsFBI Warns ARTEX AI Hacking Tool Can Breach Networks in Under Three HoursThe FBI says attackers use ARTEX, an AI hacking framework, to reach privileged access in under 3 hours. What it is, who is targeted and what to do.](https://thetechhacker.com/news/fbi-warns-artex-ai-hacking-tool/)

[NewsUber Data Breach: 149,346 Drivers Notified After License Data Stolen at AI VendorUber says 149,346 people had names, addresses, birth dates and driver license numbers stolen at an AI vendor. What happened and what drivers should do.](https://thetechhacker.com/news/uber-data-breach-drivers-license-fireworks-ai/)

## The week in tech, *minus the noise.*

New reviews, fixes and the stories that matter — once a week, straight to your inbox.

We only use your email to send the newsletter. Unsubscribe any time. See our [privacy policy](https://thetechhacker.com/privacy-policy/).

## Comments
