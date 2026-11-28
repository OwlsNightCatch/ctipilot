---
schema: 1
kind: incident
title: "1Password: an attacker used an employee's corporate GitHub account to push malicious code to backend services that downloaded administrative data about a subset of customers, and copied private-repository source code and reached the CI/CD system; vaults were not affected"
headline: "1Password breach via an employee GitHub account exported customer records; vaults not affected"
summary: >
  1Password disclosed on 2026-11-25 that an attacker who had gained access to an employee's corporate GitHub account pushed malicious code to backend services, which downloaded administrative data about a subset of customers: names, email addresses, identifiers, public keys, protocol parameters and tokens embedded in some emailed invitation, provisioning and account-recovery links. The attacker also copied private-repository source code and reached the CI/CD system, and 1Password rotated every credential that may have been exposed. 1Password says vault contents, vault keys and recovery keys were not affected and the exposed tokens need an SSO sign-in or an emailed code, which it lengthened; it does not say how the account was compromised or how many customers are affected.
discovered_at: "2026-11-26T05:04:20Z"
updated_at: null
event_date: "2026-11-25"
run_id: 2026-11-26T0356Z-intel
priority: notable
immediate_action: null
tags: [data-breach, supply-chain, identity]
regions: [global]
sectors: [technology]
entities: ["incident:1password-employee-github-account-backend-compromise-2026-11", "product:1password"]
techniques: [T1078.004, T1213.003, T1528]
affected_products: ["1Password"]
cves: []
sources:
  - url: "https://1password.com/blog/update-on-nov-2026-security-incident"
    publisher: "1Password"
    date: "2026-11-25"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/1password-customer-data-stolen-after-employee-github-account-breach/"
    publisher: "BleepingComputer"
    date: "2026-11-25"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The actor used the account to access source code and push malicious code to backend services, which downloaded administrative data pertaining to our customers."
    publisher: "1Password"
    source_url: "https://1password.com/blog/update-on-nov-2026-security-incident"
  - quote: "The attacker also copied source code from private repositories and gained access to our CI/CD system."
    publisher: "1Password"
    source_url: "https://1password.com/blog/update-on-nov-2026-security-incident"
  - quote: "At no time were customer vault contents accessed by, or available to, the attacker."
    publisher: "1Password"
    source_url: "https://1password.com/blog/update-on-nov-2026-security-incident"
verification: single-source-victim
sourcing_note: >
  1Password's own incident post is the only source: BleepingComputer restates it and adds no independent observation, and the post says it will be kept current and may have been edited since first publication. The claim that no account takeover has been seen with the exposed tokens is 1Password's assertion. The post does not say how the GitHub account was compromised, when the malicious code was pushed or removed, how the activity was detected, how many customers are in the affected subset, or who the attacker is.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

1Password disclosed on 2026-11-25 that on 2026-11-19 it began investigating indications that an attacker had gained access to an employee's corporate GitHub account ([1Password, 2026-11-25](https://1password.com/blog/update-on-nov-2026-security-incident)). The attacker used the account to access source code and push malicious code to backend services, which downloaded administrative data about customers; the attacker also copied source code from private repositories and gained access to the CI/CD system, which holds infrastructure secrets, and 1Password rotated every credential that may have been exposed ([1Password, 2026-11-25](https://1password.com/blog/update-on-nov-2026-security-incident)). It says the actor had stolen a token and that vault contents, the keys that protect them, account recovery keys and its apps and browser extensions were not affected ([1Password, 2026-11-25](https://1password.com/blog/update-on-nov-2026-security-incident)).

The records taken for a subset of users, whose size is not stated, are names and email addresses, account and user identifiers, account creation and last sign-in times, public keys, Secure Remote Password protocol parameters, tokens embedded in certain emailed invitation, SCIM Bridge and Hosted Provisioning, and account-recovery links, and non-secret internal metadata ([1Password, 2026-11-25](https://1password.com/blog/update-on-nov-2026-security-incident)). Those tokens complete an invitation or recovery only together with an SSO sign-in or an emailed code, which 1Password has lengthened from six numeric digits to ten alphanumeric characters, and it says it found no evidence of account takeover with the exposed tokens; its advice to customers is caution about phishing that mentions invitations or account recovery, that it will never ask for the account password or Secret Key, keeping both safe, and reporting suspicious messages to its support address ([1Password, 2026-11-25](https://1password.com/blog/update-on-nov-2026-security-incident)). BleepingComputer adds that the harvested name and email list is useful for such phishing ([BleepingComputer, 2026-11-25](https://www.bleepingcomputer.com/news/security/1password-customer-data-stolen-after-employee-github-account-breach/)).

**Exposure:** any organisation with 1Password accounts, since users' names, sign-in addresses and identifiers were in the copied records, and especially one using SCIM provisioning or account recovery, because tokens in those emailed links were among the data; 1Password says it notified a small number of users with pending invitations or recoveries directly ([1Password, 2026-11-25](https://1password.com/blog/update-on-nov-2026-security-incident)).

**Detection:** in the identity provider's and 1Password's administrator audit records, invitation, provisioning and account-recovery events since about 2026-11-19 that no administrator or user requested; in mail-gateway logs, inbound mail that imitates 1Password invitations or recovery messages with real tenant or user details; and user reports of recovery codes nobody asked for. These checks are analysis from the data classes the post lists, which publishes no indicator.

**Triage:** a legitimate invitation or recovery message follows an administrator's or user's own action; one that arrives without it is the signal.

**Defender takeaway:** 1Password's own advice covers phishing caution, never sharing the password or Secret Key and reporting suspicious messages, and BleepingComputer says it is not requiring customers to change their account passwords or Secret Keys ([BleepingComputer, 2026-11-25](https://www.bleepingcomputer.com/news/security/1password-customer-data-stolen-after-employee-github-account-breach/)); the action is to warn users about phishing that mentions invitations or account recovery and to watch for unrequested provisioning events. For your own pipelines the mechanism is one employee source-control identity that could push to backend services and reach CI/CD, so require review on the deploy path and alert on pushes and workflow changes made with employee tokens.
