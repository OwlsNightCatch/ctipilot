---
title: "Radware Cloud WAF Breach Exposes Azure and AWS Log-Export Credentials: Rotation Guide"
author: WindowsForum
url: https://windowsforum.com/news/radware-cloud-waf-breach-exposes-azure-and-aws-log-export-credentials-rotation-guide.453957/
hostname: windowsforum.com
description: There is a special kind of irony reserved for the security vendor that leaves an internal management door unlocked on the public internet.
sitename: Windows Forum
date: "2026-11-24"
fingerprint: "3c79ef9b4db2744d"
language: en
image: https://windowsforum.com/attachments/windowsforum-radware-cloud-waf-breach-exposes-azure-and-aws-log-export-credentials-rotation-g-webp.192633/
pagetype: article
filedate: "2026-11-25"
---
For Windows and Azure administrators, this is not a distant perimeter headline you can skim past over morning coffee. Among the exposed secrets explicitly named in Radware’s internal report are **Azure Blob Storage access keys and Shared Access Signature (SAS) tokens**, alongside **AWS S3 access keys** and **SFTP credentials**. If your organization relies on Radware’s Cloud WAF or Bot Management services and pipes telemetry into Microsoft Azure or AWS, the clock on credential rotation started ticking the moment that API went exposed.

## 
  
    
    
  
    
    
  
    
  
What Happened Inside Radware’s Cloud WAF Control Plane

Per the leaked root cause analysis cited by BleepingComputer, Radware detected the intrusion on Thursday, November 19, roughly 10 hours after the initial unauthorized access. In its own words from the report, Radware stated that an unauthorized party reached "an internal-only Cloud WAF management API that was reachable from the Public Internet without requiring authentication".

Ten hours in cloud time is an eternity—plenty of runway for automated scripts to enumerate endpoints, dump configuration records, and harvest stored integration secrets. Once Radware spotted the activity, the company moved to contain the immediate exposure:

- **Network and API lockdown:** Radware blocked the originating IP address and shut off external access to the internal management API.
- **Internal credential purge:** The company revoked and replaced all internal account credentials.
- **Customer warning:** Radware "strongly" advised affected AppSec customers (using WAF and BOT protections) to rotate their Cloud WAF log-export credentials immediately and audit storage access logs for suspicious activity dating back to at least November 19.

What remains conspicuously missing from the public record, as of November 24, 2026, is an official public advisory or regulatory filing. BleepingComputer and MLQ.ai both noted that Radware had not issued a public statement or submitted a breach disclosure to the U.S. Securities and Exchange Commission as of Tuesday afternoon, and a company spokesperson had not immediately responded to press inquiries. A check of Radware’s public SEC filings index shows no breach-related disclosure: the most recent filings are routine Schedule 13G/A ownership amendments, including one filed on November 16, 2026. Because Radware is a foreign private issuer traded on Nasdaq under the ticker RDWR, material disclosures are typically furnished via Form 6-K rather than a domestic Form 8-K, leaving customers watching both vendor portals and SEC EDGAR for formal confirmation.

Meanwhile, Radware’s public Cloud WAF status page shows routine infrastructure maintenance and localized Point-of-Presence (PoP) latency alerts across mid-to-late November, with no mention of the November 19 API exposure. That omission is not surprising—status pages track traffic uptime, not control-plane leaks—but it underscores why security teams cannot rely solely on green uptime dashboards to gauge vendor risk.

## Why "Only Log-Export Credentials" Is Still a Serious Problem

Whenever a security provider suffers a breach, the first reassuring paragraph almost always tells customers what *wasn't* touched. Radware’s report follows that script carefully: the company states that the incident did not expose WAF traffic inspection, SSL certificates, end-user data, live customer application traffic, or cloud DDoS services and data. It also reports that WAF enforcement continued without interruption and that investigators have found no evidence of tampered customer security policies.

Take that reassurance at face value—and then ask the critical follow-up question any seasoned CISO would ask: *What exactly happens when an attacker holds the keys to your WAF log-export bucket?*

Radware’s own October 2026 Data Processing Profiles for Cloud WAF and API Security spell out what flows through that integration. When customers enable Security Event Log Export or Access Log Export, Radware streams consolidated JSON files directly to the customer’s designated AWS S3 bucket, Azure Blob container, or SFTP server. Those exports capture security events across WAF, DDoS, and BOT modules, and—when access logging is active—detailed records of client transactions hitting protected applications. Depending on configuration and portal data categories, security-event metadata can include source IP addresses, user-agents, attacked URLs, request and response headers, attack payloads, and session or cookie data.

In plain English, an attacker who unlocks your log-export storage isn't just reading boring timestamps. They could be harvesting a blueprint of your web application architecture, seeing which exploits your WAF blocked (and which payloads slipped close), and potentially scraping sensitive headers or session artifacts captured in HTTP logs. Even worse, if the exposed credential is an **Azure Storage account access key**, it does not merely unlock a single log folder—Microsoft Learn documentation warns that a Shared Key grants full administrative read, write, and delete access across the *entire* storage account, plus the ability to mint new SAS tokens.

That risk is no longer purely theoretical. Radware acknowledged in its report that while it is still investigating whether exposed keys were abused, it has already received reports from customers seeing **AWS alerts for an unfamiliar IP address attempting to access their log-export buckets**. An attempted connection alert does not automatically prove data was exfiltrated—an IP block or bucket policy may have stopped the intruder cold—but it strongly suggests someone tested the stolen keys in the wild.

## The Hidden Catch in Rotating Azure and AWS Credentials

For enterprise IT teams running hybrid Microsoft and AWS environments, rotating credentials sounds like a five-minute chore until you hit the quirks of how each cloud actually invalidates secrets. Here is where many administrators trip up—especially with Azure SAS tokens.

| Exposed Credential Type | Blast Radius Risk | How to Revoke / Rotate Safely | Primary Audit Log Source | 
|---|---|---|---|
| **Azure Storage Account Key** | Full read/write/delete across the entire storage account; can sign new SAS tokens | Use dual-key rotation ( `key1` / `key2`) so logging never drops, then regenerate the exposed key | Azure Monitor `StorageBlobLogs` (`AuthenticationType == "AccountKey"`) | 
| **Azure SAS Token** | Scoped to resource/permissions in token, but acts as a bearer secret | Revoke Stored Access Policy if attached; otherwise **must rotate the signing account key** | Azure Monitor `StorageBlobLogs` (`AuthenticationType in ("SAS", "DelegationSas")`) | 
| **AWS S3 IAM Access Key** | Whatever IAM policy is attached to that IAM user (often S3 read/write) | Create secondary key, update Radware, set old key **Inactive** to test, then delete | AWS CloudTrail and Amazon S3 Server Access Logs | 
| **SFTP Credentials** | Access to target SFTP directory or server host | Rotate SFTP password or SSH key pair; update Radware portal; review IP allowlists | Host `sshd` / SFTP daemon authentication and transfer logs | 

## 1. The Azure Blob Storage Key and SAS Token Playbook

If you configured Radware Cloud WAF or CWAAP Log Exporter to push JSON logs into Azure Blob Storage, verify immediately whether you supplied a full Storage Account Key or a SAS token:

- **Check how your SAS token was minted:** Microsoft’s official Azure Storage documentation makes a sharp distinction that catches many admins off guard. If you issued an **ad hoc service SAS** or an **account SAS** without linking it to a Stored Access Policy, Azure provides *no button to revoke that individual token*. Deleting the URL from your clipboard or updating Radware’s portal does nothing to stop an attacker who already copied it. The only way to kill an ad hoc key-signed SAS before its expiration date is to **regenerate the storage account key (`key1` or `key2`) used to sign it**.
- **If you used a Stored Access Policy:** You have a cleaner exit. In the Azure portal or via PowerShell/CLI, you can delete the Stored Access Policy, rename its signed identifier, or set its expiration time into the past—immediately invalidating every SAS bound to that policy without breaking other apps using your account keys.
- **Zero-downtime rotation for Account Keys:** Because Azure Storage accounts ship with two keys (`key1` and `key2`), follow Microsoft’s two-credential rotation pattern. Identify which key Radware currently uses, regenerate the *other* (inactive) key first, update the Radware Cloud Services export configuration with the newly generated key (or a fresh, tightly scoped SAS signed by it), confirm logs are flowing, and then regenerate the previously exposed key to permanently sever attacker access.
- **Harden your Azure storage posture afterward:** Microsoft recommends disabling Shared Key authorization (`AllowSharedKeyAccess` set to `false`) wherever feasible—a setting that blocks both raw account keys and key-signed SAS tokens—and using Microsoft Entra ID or short-lived User Delegation SAS tokens instead.

## 2. Hunting for Unauthorized Azure Access Since November 19

Rotating keys stops future bleeding, but you still need to know whether anyone knocked on your Blob container between November 19 and today. If you have Azure Monitor diagnostic logging enabled for Blob Storage, open your Log Analytics workspace and query the `StorageBlobLogs` table.

Per Microsoft Learn’s monitoring reference, filtering `StorageBlobLogs` where `TimeGenerated >= datetime(2026-11-19T00:00:00Z)` and `AuthenticationType in ("AccountKey", "SAS")` lets you group requests by `CallerIpAddress`, `UserAgentHeader`, `OperationName` (such as `GetBlob` or `ListBlobs`), and `StatusText`. Even better, Azure logs a SHA-256 hash of the key and SAS signature in the `AuthenticationHash` field, allowing incident responders to correlate every operation performed by a specific token even if an attacker hops across multiple VPN or cloud IP addresses.

## 3. Rotating AWS S3 Keys and Checking Bucket Logs

For teams exporting Radware logs to Amazon S3, follow AWS’s documented IAM access key rotation sequence rather than deleting keys blindly:

- Generate a **new second access key** for the dedicated IAM user (while leaving the old key intact temporarily).
- Update the Access Key ID and Secret Access Key inside your Radware Cloud WAF export settings.
- Immediately flip the old, potentially exposed IAM key to **Inactive** in the AWS IAM console. This instantly blocks unauthorized API calls while giving you a safe rollback path if anything unexpected breaks.
- Verify Radware log delivery continues normally, then **delete** the inactive key.
- Audit **AWS CloudTrail** data events and **Amazon S3 Server Access Logs** from November 19 onward for unfamiliar caller IPs, `ListBucket` enumerations, or `GetObject` downloads—paying close attention to any denied or successful requests matching the alerts Radware warned customers about.

## The Bigger Lesson: Internal APIs Never Stay "Internal" by Accident

Beyond the immediate cleanup checklist, the Radware breach delivers an uncomfortable architectural reminder for every enterprise IT shop running hybrid cloud infrastructure. Security vendors are prime targets, and an "internal-only" API exposed to the internet without authentication is one of the oldest failure modes in modern cloud operations.

You do not need to be a global WAF provider to make that same mistake. All it takes is one misconfigured reverse proxy, an overly permissive Azure Network Security Group, or an API gateway deployment lacking a zero-trust authentication policy. As you finish rotating your Radware log-export keys this week, take an extra hour to audit your own "internal" management endpoints and verify that every storage integration—whether in Azure Blob, AWS S3, or SFTP—runs on least-privilege permissions, strict IP allowlists, and short-lived credentials. Because if a cybersecurity company can leave an unauthenticated management API sitting on the public internet for 10 hours, none of us gets to assume our internal endpoints are invisible.

*Correction (November 24, 2026): An earlier version of this article said Radware had made no new SEC submissions since a Schedule 13G/A filing on November 13, 2026. In fact, a further routine Schedule 13G/A ownership amendment was filed on November 16, 2026. No breach-related disclosure has been filed; only the filing date was wrong.*

## References

1. [Radware discloses breach exposing customer cloud access keys](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys) BleepingComputer
											 · 
											2026-11-24T12:49:05-05:00
2. [nasdaq.com](https://www.nasdaq.com/press-release/radware-h1-2026-global-threat-report-shows-web-ddos-attacks-jump-more-110-cyber) nasdaq.com
3. [microsoft.com](https://techcommunity.microsoft.com/blog/microsoft-defender-experts/cloud-forensics-why-enabling-microsoft-azure-storage-account-logs-matters/4445723) techcommunity.microsoft.com
