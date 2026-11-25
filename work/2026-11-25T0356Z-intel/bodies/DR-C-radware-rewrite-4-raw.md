---
title: "Radware Cloud WAF: Unauthenticated Management API Exposes Log Export Credentials"
author: Anoymask
url: https://dev.to/anoymask/radware-cloud-waf-unauthenticated-management-api-exposes-log-export-credentials-4glg
hostname: dev.to
description: "Basic Information Article Title: Radware discloses breach exposing customer cloud access..."
sitename: DEV Community
date: "2026-11-25"
tags: ['security', 'threatintel', 'software', 'coding', 'development', 'engineering', 'inclusive', 'community']
fingerprint: d535e42cf16634d
language: en
image: https://media2.dev.to/dynamic/image/width=1200,height=627,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2F5q3as8vnlwoqgge4ca2i.png
pagetype: article
filedate: "2026-11-25"
---
## 
  
  Overview

- **Article**: Radware discloses breach exposing customer cloud access keys
- **Source**: BleepingComputer
- **Date**: 2026-11-24
- **Reference**: [BleepingComputer](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)
- **Products/Services**: Radware Cloud WAF, AWS S3, Azure Blob Storage, SFTP
- **Response Priority (Author's Assessment)**: critical — Customer cloud storage credentials were exposed externally, and unauthorized access attempts from unknown IPs to AWS buckets have been reported. A public RCA is not yet available.

## 
  
  In Brief

Radware's internal-only Cloud WAF management API was exposed to the internet without authentication, potentially allowing attackers to access customer contact information and log export credentials for AWS S3, Azure Blob, and SFTP for some customers.

## 
  
  Attack Flow

### 
  
  From Exposed Management API to Cloud Storage Credentials

1. An attacker connects from the internet to an accessible internal management API without authentication.
2. The API potentially exposes customer information and log export credentials for some customers, though the scope of access remains unconfirmed.
3. If the retrieved credentials are valid, connection to the customer's AWS S3, Azure Blob, or SFTP becomes possible.

## 
  
  Attacker Position and Execution Location

- External attacker reaching the public management API of Radware Cloud WAF from the internet.

## 
  
  Victim and Administrator Perspective

- **Victims**: WAF traffic processing continues, and there may be no user-facing outage.
- **Administrators**: Indicators include Radware notifications, cloud storage access alerts from unknown IPs, and the use of log export credentials.

## 
  
  Success and Failure Conditions

### 
  
  Success Conditions

- Management API is externally accessible without authentication
- Stored log export credentials are valid at the time of retrieval

### 
  
  Failure Conditions

- API blocking and mandatory authentication
- Credential rotation and revocation, least privilege, and storage-side source IP restrictions

## 
  
  Impact upon Success

- Exposure of customer contact information
- Exposure of cloud storage access keys, SAS, and SFTP credentials
- Potential unauthorized access to log storage

## 
  
  Observable Logs

- **Identity and IdP**: Use of cloud access keys, SAS, and SFTP accounts from unknown IPs
- **SaaS and Cloud**: Unusual list/get attempts on S3, Blob, and SFTP
- **Network**: Storage connections from unknown IPs since November 19

## 
  
  Attack Success Assessment

### 
  
  Confirmed in Public Information

- **Attack attempts observed (success unconfirmed)**: Public reports indicate unauthorized access to the management API and potential access to credentials as part of Radware's RCA findings. While access attempts to customer buckets from unknown IPs have been reported, data theft success remains unconfirmed. Target scope: A subset of affected Cloud WAF customers; the number has not been publicly disclosed.

### 
  
  Internal Assessment Criteria

- Evaluate exposure, authentication, initial execution, information access, and follow-on compromise based on available evidence.

## 
  
  Investigation Playbook

- **Trigger**: Radware notification, cloud provider unknown IP alert
- **Initial Checks**: Check affected services, credential types, issuance permissions, and last usage time
- **Identity and Cloud**: Revoke and reissue keys, SAS, and passwords, then investigate access logs
- **Follow-on**: Check for object list/get/write, policy changes, and token issuance
- **Containment**: Credential rotation, session revocation, storage policies, and source restrictions
- **Classification**: Separate API access, credential acquisition, storage authentication, and object access

## 
  
  Defense and Detection Ideas

- **Single Event**: Use of log-export credentials by unknown IPs
- **Time Series**: Radware incident time -> storage authentication attempt -> object operations
- **Hunting**: All log export credential usage since November 19
- **Logging Gaps**: Scope of Radware API audit logs provided to customers
- **Priority Controls**: Credential rotation, least privilege, short-lived tokens, and storage-side IP restrictions

## 
  
  Facts / Inference / Hypothesis

### 
  
  Facts

- On November 19, 2026, an internal-only management API was accessed without authentication and reached from the internet.
- Potential targets for access included customer contact information and AWS, Azure, and SFTP credentials configured by some customers for log export.
- According to BleepingComputer, Radware detected the breach approximately 10 hours after the initial unauthorized API access, blocked the source IP and API access, and revoked and reissued internal account credentials.
- Some customers reported alerts regarding access attempts to AWS log-export buckets from unknown IPs.
- According to the report, Radware stated that it had found no evidence of access to WAF traffic, certificates, end-user data, customer application traffic, or cloud DDoS data.

### 
  
  Inference

- Because external cloud credentials stored in the management plane establish a separate security boundary from the WAF itself, continued WAF operation alone does not guarantee an absence of impact.

### 
  
  Hypothesis

> No additional hypotheses. Unconfirmed items are listed under Unresolved Questions and Further Investigation.

## 
  
  MITRE ATT&CK Mapping

| ID | Technique | Confidence | Basis | 
|---|---|---|---|
| T1190 | Exploit Public-Facing Application | medium | An unauthenticated publicly exposed management API served as the unauthorized access vector. Details of the vulnerability exploit code are not public. | 
| T1530 | Data from Cloud Storage | medium | Customers reported bucket access attempts using exposed credentials. | 

## 
  
  Unresolved Questions and Further Investigation

- The number of affected customers, the scope of acquired credentials, successful cloud storage access, and the root cause of the API exposure remain undisclosed.

## 
  
  Impact on SOCs and Organizations

Organizations utilizing Radware Cloud WAF should not rely solely on waiting for notifications. They should review AWS, Azure, and SFTP access logs since November 19, rotate log export credentials, and revoke existing sessions and tokens.

## 
  
  Summary by Role

- **For SOCs**: Investigate bucket, Blob, and SFTP access from unknown IPs and Radware configuration changes since November 19.
- **For Administrators**: Rotate log export keys, SAS, and passwords, and re-verify least privilege and source restrictions.
- **For Users**: WAF protection continued, but cloud credentials stored in the management infrastructure require investigation.

## Top comments (0)
