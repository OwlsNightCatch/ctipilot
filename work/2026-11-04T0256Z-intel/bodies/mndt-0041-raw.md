# MNDT-2026-0041

## Description
Improper neutralization of shell metacharacters in the timezone configuration field in certain Barracuda appliance products using common Barracuda code allows an authenticated administrator to inject OS commands that execute with root privileges when the crafted timezone value is subsequently processed.

## Impact
High: An authenticated administrator may inject OS commands that execute with root privileges when the crafted timezone value is subsequently processed.

## Exploitability
Medium: The attacker must first authenticate with administrative privileges.

## CVE ID
CVE-2026-111560

## Common Weakness Enumeration
* CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')

## Common Attack Pattern Enumeration and Classification
* CAPEC-88: OS Command Injection

## Details
The affected products and versions are:

* Barracuda Email Security Gateway (ESG) <= 9.4.0.27
* Barracuda Load Balancer Application Delivery Controller (ADC) versions <= 6.4.0
* Barracuda Web Application Firewall (WAF) versions <= 11.0.1
* Barracuda Web Security Gateway (WSG) versions <= 16.1.100.100
* Barracuda Message Archiver (BMA) versions <= 5.5.4.0
* Barracuda WAF Control Center (WCC) versions <= 2.2.1

## Metric
CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N (8.6)

## Disclosure Timeline
* 2026-10-15: Reported by Barracuda
* 2026-11-02: CVE published and Mandiant advisory released

## References
* [Barracuda Advisory](https://trust.barracuda.com/security/pre-authentication-authorization-bypass-command-injection)
* [cve.org CVE-2026-111560](https://www.cve.org/CVERecord?id=CVE-2026-111560)

