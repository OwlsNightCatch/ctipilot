# MNDT-2026-0042

## Description
An authentication bypass in Barracuda Email Security Gateway versions earlier than 9.4.0.030 allows an unauthenticated remote attacker to invoke a configuration-import function and restore a crafted, compatible backup archive, resulting in unauthorized modification of the appliance's global configuration.

## Impact
High: An unauthenticated remote attacker may bypass authentication and restore a crafted, compatible backup archive, resulting in unauthorized modification of the appliance's global configuration.

## Exploitability
High: The vulnerability is exposed to an unauthenticated remote attacker.

## CVE ID
CVE-2026-116606

## Common Weakness Enumeration
* CWE-288: Authentication Bypass Using an Alternate Path or Channel

## Common Attack Pattern Enumeration and Classification
* CAPEC-115: Authentication Bypass

## Details
The affected product and version is:

* Barracuda Email Security Gateway (ESG) < 9.4.0.030

## Metric
CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N (9.3)

## Disclosure Timeline
* 2026-10-22: Reported by Barracuda
* 2026-11-02: CVE published and Mandiant advisory released

## References
* [Barracuda Advisory](https://trust.barracuda.com/security/pre-authentication-authorization-bypass-command-injection)
* [cve.org CVE-2026-116606](https://www.cve.org/CVERecord?id=CVE-2026-116606)

