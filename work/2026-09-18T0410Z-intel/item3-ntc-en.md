---
title: Cybersecurity of Photovoltaic Systems
author: Team NTC
url: https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems
hostname: ntc.swiss
description: Die Cybersicherheit von Photovoltaikanlagen in der Schweiz ist gefährdet. Eine Analyse zeigt kritische Schwachstellen und Energiemanagementsystemen.
sitename: Nationales Testinstitut für Cybersicherheit | NTC
date: "2026-09-17"
---
# Cybersecurity of Photovoltaic Systems

Systemically Important Photovoltaic Systems: Comprehensive Cybersecurity Analysis With Concrete Recommendations

A comprehensive analysis by the National Test Institute for Cybersecurity NTC shows that Switzerland’s growing fleet of photovoltaic systems represents an underestimated attack surface for the power grid. Seven inverters and four energy management systems from eight manufacturers were tested — devices like those installed in thousands of Swiss homes. In total, the assessments produced more than 50 findings, seven of them critical and a further six rated high. The findings were reported confidentially to the manufacturers. Most responded quickly, while work to fix the vulnerabilities is still under way for some products.

A real-world pattern identified in the analysis illustrates just how concrete this risk is: On almost every inverter tested, the local control interface makes it possible — without any login — to change how much power the installation feeds into the grid, all the way down to zero. Taken on its own, this affects only a single installation. However, if an attacker gains control of a manufacturer’s cloud, the same manipulation could be triggered simultaneously across thousands of connected installations. A single solar installation on a residential roof counts for nothing on the grid — but the fleet as a whole constitutes critical infrastructure.

This creates a dangerous shift: What once required physical access to a power plant can now be achieved through centralized remote access. The greatest risk cannot be addressed through better product security alone — it arises from connecting thousands of installations to a small number of manufacturers’ clouds.

Results of the Security Analysis and Key Risk Patterns

To assess the security level of the photovoltaic technology in widespread use in Switzerland, the NTC put eleven digital products from eight manufacturers through a comprehensive technical security analysis over the course of around a year: seven inverters and four energy management systems.

In total, the assessments produced more than 50 findings, seven of them critical and a further six rated high. Five of the eleven products had at least one high or critical finding, and on four products, the NTC gained complete control over the device. The public report deliberately omits product names and technical details. Instead, it describes typical risk patterns:

- deficiencies in authentication and access control, such as default passwords

- insecure maintenance access, such as identical credentials across an entire device fleet

- missing or weak encryption of communication over local interfaces

- interfaces that cannot be disabled

Taken product by product, the security level does not differ significantly from that of other widely used connected devices. The actual risk to Switzerland’s power grid lies not in an individual device but in the dependence on a small number of manufacturers: Their cloud infrastructure is used to control the installations and provide them with firmware, and most manufacturers retain privileged maintenance access across their entire device fleet.


Recommendations for Minimizing Risk

Based on these findings, the report sets out recommendations for five audiences:

There is no simple, complete solution; every approach has advantages and disadvantages, and residual risks remain. The report is not intended as an argument against photovoltaics, but rather as a basis for their secure expansion.

The analysis was conducted on the initiative of the National Test Institute for Cybersecurity NTC, which provided the test team and a substantial share of the funding. It was supported by several organizations, most of them from the energy sector, as well as by SwissEnergy — the NTC thanks them for their contribution. To ensure the independence of the results, the manufacturers of the products tested were involved neither in product selection nor in conducting the tests and were contacted only as part of the confidential vulnerability disclosure process.

###### *The Summary Report is available in German, English, French, and Italian.*

              
            
              
                ###### Media Tracking


The publication of the Report on the Cybersecurity of Photovoltaic Systems was covered by the media. Below is a non-exhaustive list of articles on the topic:

              
            
              
                - **SRF, 16 September 2026:** Sicherheitsexperten: Blackout-Risiko wegen Solaranlagen[To the SRF article](https://www.srf.ch/news/schweiz/risiko-cyberangriffe-sicherheitsexperten-blackout-risiko-wegen-solaranlagen)
