##### SEVERITY AND IMPACT:
- Successful compromise lets remote attackers manipulate refrigeration settings through internet-exposed management interfaces, causing damage such as spoiled stock.
- **Current exploitation status**: Actively Exploited

##### AFFECTED PRODUCTS:
- Danfoss AK-SM 800 System Manager (end-of-life, no longer patched)
- Danfoss AK-SC 355 (phased out, no longer patched)
- Danfoss AK-SM 800A / AK-SM 8xxA Series (current model, when running outdated firmware)
- For specific versions, please check the references and monitor for updates.

##### VULNERABILITY DETAILS:
- **Prerequisites:** Network access to an internet-exposed controller web management interface. The likeliest targets are end-of-life or unpatched units, often with default credentials or no firewall/VPN.
- **Available Mitigations:**
    - Vendor firmware updates are available for the AK-SM 800A and fix the disclosed CVEs.
    - Newer AK-SM 800A firmware enables Strict Session Control and mandatory HTTPS by default.
    - No fixes exist for the end-of-life AK-SM 800 and AK-SC 355, and Danfoss urges replacing them.
    - **Temporary:** Disconnect controllers from the internet or tightly filter access to trusted IPs or a VPN. Require remote users to log in through a single managed entry point. Change default passwords.
    - **Temporary:** If a controller may be compromised, CERT-FR advises these steps in order:
        1. Limit access to trusted IP and service providers only.
        2. Perform a factory reset.
        3. Apply all available fixes.
        4. Rotate passwords and other secrets.
        5. Review existing accounts.
        6. Fully reconfigure the device.

##### CVEs IN THIS ADVISORY:
Alleged as potentially related:
- CVE-2025-41451 CVSS4.0: 8.7 (HIGH) - Command injection in the alarm-to-mail (SMTP) configuration, enabling post-authentication RCE
- CVE-2025-41450 CVSS3.1: 8.2 (HIGH) - Hidden "code-of-the-day" authentication bypass granting admin access
- CVE-2025-41452 CVSS4.0: 6.8 (MEDIUM) - Post-authentication Nginx configuration injection causing denial of service

##### REFERENCES:
Primary:
- Source Advisory: https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/ (CERT-FR alert on AK-SM/AK-SC compromises, in French)
- Additional Sources: https://www.cert.ssi.gouv.fr/dur/CERTFR-2025-DUR-003/ (CERT-FR hardening recommendations)

Supporting:
- News Coverage: https://thehackernews.com/2026/10/attackers-heat-french-supermarket.html
- News Coverage: https://www.securityweek.com/refrigeration-controller-hack-spoils-food-across-european-supermarkets/
- News Coverage: https://www.coolingpost.com/world-news/danfoss-moves-to-mitigate-cyberattack/ (Danfoss statement on affected AK-SM 800A units)

Related to 2025 CVEs:
- Technical Analysis: https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers (Claroty Team82 research, with detailed technical analysis of the authentication bypass, RCE and DoS flaws)
- Patch Information: https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2025-08-01/ (Danfoss advisory for the command injection fix)


*Timestamp of the Information: 13.10.2026, 16:04*

---

###### Update: 6 November 2026

**Incidents reported in Switzerland, additional controller families and healthcare impact**

Swiss media report manipulation of refrigeration controllers in Switzerland.

The updated CERT-FR alert also identifies **Copeland/Dixell XWEB**, in addition to Danfoss AK-SM and AK-SC controllers. Copeland’s guidance specifically addresses end-of-service XWEB EVO systems and recommends migration to a supported platform. Supported XWEB PRO systems must also be protected from direct internet access.

Healthcare incidents have also been reported. Refrigeration settings were altered at three sites of France’s national blood service following a cybersecurity incident involving a refrigeration equipment provider.

The public information reviewed does not establish a common attack method across these incidents or confirm exploitation of the specific Danfoss CVEs listed above.

**Recommended actions:**

- Review refrigeration management systems across all relevant operations, including equipment managed by external service providers.
- Remove direct internet access to management interfaces. Provide remote access through a secure VPN or protected network.
- Check temperature settings, defrost schedules, alarm thresholds, notification recipients and user accounts. Verify actual temperatures and test alarm delivery.
- Apply the latest supported firmware and manufacturer hardening guidance. Plan replacement of equipment that no longer receives security updates.

If compromise is suspected, coordinate containment and recovery with your refrigeration provider and security team. Follow the recovery procedure for the specific device. A factory reset alone is insufficient if the system remains vulnerable and directly accessible from the internet.

**Sources:**

- [SRF: Refrigeration incidents reported in Switzerland](https://www.srf.ch/news/schweiz/kuehlanlage-manipuliert-berner-metzgerei-opfer-von-hackerangriff-auch-volg-betroffen)
- [CERT-FR: Updated alert and mitigation guidance](https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012/)
- [The Record: French blood service incident and EFS statement](https://therecord.media/france-cyberattack-blood-refrigeration)
- [Copeland/Dixell: XWEB security and recovery guidance](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)