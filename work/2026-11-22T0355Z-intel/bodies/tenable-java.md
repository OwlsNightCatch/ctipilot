---
title: "Java4Shell (CVE-2026-114938): OpenJDK RCE Vulnerability FAQ"
author: Satnam Narang
url: https://www.tenable.com/blog/java4shell-cve-2026-114938-frequently-asked-questions-about-openjdk-rce-vulnerability
hostname: tenable.com
description: Frequently asked questions about Java4Shell (CVE-2026-114938), an OpenJDK flaw that researchers say can let attackers run code on Java apps without logging in.
sitename: Tenable®
date: "2026-11-17"
fingerprint: "95913497cff4e1cd"
---
# Java4Shell (CVE-2026-114938): Frequently asked questions about OpenJDK remote code execution vulnerability

**Java4Shell is a flaw in how Java decodes Base64 data. Calif, which found it, says it can let attackers run code on widely used Java applications without logging in. Oracle released fixed Java builds on November 17, and Calif is withholding its exploits for individual applications for now.**

### Change log

**Update November 19:** Added Tenable's product statement, which lists Tenable Enclave Security and Tenable OT as affected, and updated fixed builds from Linux distributions and other Java vendors. Noted in the Key Takeaways that there is no universal exploit, and added Keycloak's updated container images.

## **Click here to review the change log history**

**Update November 19:** Added Tenable's product statement, which lists Tenable Enclave Security and Tenable OT as affected, and updated fixed builds from Linux distributions and other Java vendors. Noted in the Key Takeaways that there is no universal exploit, and added Keycloak's updated container images.

**Update November 18:** Added reports of exploitation attempts and a working exploit, alerts from CISA and the Canadian Centre for Cyber Security, fixed builds from other Java distributions, mitigation guidance from Keycloak and an example Tenable Hexa AI prompt.

**November 17:** Original publication.

## Key takeaways

1. CVE-2026-114938, dubbed Java4Shell, is an OpenJDK memory corruption vulnerability that Oracle scores 8.1 on CVSS 3.1. Calif says its testing showed attackers could run code without logging in on applications such as Atlassian Jira and Jenkins, though Calif also says there is no universal exploit and each application needs its own.
2. As of November 18, GreyNoise has reported exploitation attempts against this flaw but has not confirmed any successful exploitation against its sensors, and VulnCheck says a working exploit is available to its customers, while Kevin Breen of Immersive reports building one.
3. Oracle released fixed builds on November 17, and according to Calif, only systems running an affected Java version on x86-64 processors that support AVX-512 VBMI can be affected.

## Background

Tenable's Research Special Operations (RSO) team has compiled this blog to answer Frequently Asked Questions (FAQ) regarding Java4Shell, a vulnerability in OpenJDK that was patched on November 17, 2026.

## FAQ

**When was Java4Shell first disclosed?**

On November 17, security firm Calif said on X that it had found and reported the flaw, and that details of Java4Shell, as Calif named it, had leaked ahead of a fix. Later that day, Oracle released its [<u>November 2026 Critical Security Patch Update (CSPU)</u>](https://www.tenable.com/blog/oracle-november-2026-critical-security-patch-update-addresses-640-cves-cve-2026-114938), and the OpenJDK Vulnerability Group published its own advisory. Calif then published its [<u>technical write-up</u>](https://calif.io/java4shell/). Oracle credits Quang Luong of Calif.io and Albert Yang for reporting the vulnerability.

Since the vulnerability has leaked: Calif discovered and reported Java4Shell (CVE-2026-114938).

We're publishing technical details by 1 PM Pacific today, after Oracle releases a patch.

Stay tuned! [https://t.co/No5hJXK1Zx](https://t.co/No5hJXK1Zx)

— Calif (@calif\_io) [November 17, 2026](https://x.com/calif_io/status/2122724367654334810?ref_src=twsrc%5Etfw)


The Cybersecurity and Infrastructure Security Agency (CISA) published an [alert](https://www.cisa.gov/news-events/alerts/2026/11/17/critical-java-vulnerability-requires-immediate-patching) about Java4Shell on November 17, with contributions from the Canadian Centre for Cyber Security (Cyber Centre). The Cyber Centre also published its own advisory, [AL26-029](https://www.cyber.gc.ca/en/alerts-advisories/al26-029-critical-vulnerability-impacting-oracle-java-cve-2026-114938).

**What is CVE-2026-114938?**

| **CVE** | **Description** | **CVSSv3.1** | 
|---|---|---|
| [<u>CVE-2026-114938</u>](https://www.tenable.com/cve/CVE-2026-114938) | OpenJDK Base64 Decoder Memory Corruption Vulnerability (Java4Shell) | 8.1 | 

CVE-2026-114938 is a memory corruption vulnerability in the part of Java that decodes Base64, a common format that applications use to send data such as login details and file uploads. Oracle assigned it a CVSS 3.1 score of 8.1 and rates its attack complexity as high. Calif says it scores 9.2 under CVSS 4.0. An attacker does not need to log in to exploit it remotely. According to Oracle, the flaw can only be exploited when an application passes untrusted data to the affected Java APIs, such as through a web service.

**Is CVE-2026-114938 among the Java fixes in Oracle's November 2026 CSPU?**

Yes. CVE-2026-114938 is addressed by one of the 11 Java SE security patches in Oracle's November 2026 CSPU, released November 17. For a breakdown of all the patches in this release, see our [<u>blog post on Oracle's November 2026 CSPU</u>](https://www.tenable.com/blog/oracle-november-2026-critical-security-patch-update-addresses-640-cves-cve-2026-114938).

**What is known about CVE-2026-114938?**

The flaw is in a performance shortcut that Java uses to decode Base64 data faster on certain Intel and AMD processors. When the shortcut receives a specially crafted Base64 string, it writes data beyond the memory it set aside. That can corrupt other information the application is holding in memory.

According to Calif, an attacker can use this flaw in two ways. The first, which Calif calls "JavaBleed," lets an attacker read the application's memory. That memory may hold secrets such as keys and tokens. The second lets an attacker run their own code on the server. Calif also says that each application needs its own exploit, and that a failed attempt can crash the application, though an attacker can often try again.

Exposure depends on the processor as well as the Java version. According to Calif, Java uses the affected code only on x86-64 processors that support a feature called AVX-512 VBMI. These include Intel Xeon processors from the Granite Rapids, Emerald Rapids, Sapphire Rapids and Ice Lake families, as well as AMD processors based on Zen 4 or newer. Calif says systems with ARM64 processors are not affected. On Linux, a system meets this requirement when its processor reports all four of the avx512f, avx512bw, avx512vbmi and bmi2 flags.

**Which versions of Java are affected?**

The OpenJDK Vulnerability Group lists the Java 17, 21, 25 and 27 release lines as affected by CVE-2026-114938. Calif says OpenJDK 17.0.6 and newer are affected. Oracle lists the following Oracle builds as affected:

| **Product** | **Affected versions (and likely earlier)** | 
|---|---|
| Oracle Java SE | 8u511b33-perf, 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3 | 
| Oracle GraalVM for JDK | 17.0.21.0.3, 21.0.13.0.3 | 
| Oracle GraalVM Enterprise Edition | 21.3.20.0.3 | 

Oracle lists only builds it supports and says earlier versions are likely also affected. The Java 8 build on Oracle's list is its Enterprise Performance Pack. The OpenJDK advisory does not list standard Java 8 or Java 11 as affected by this vulnerability.

**I don't use Oracle's Java builds. Am I affected?**

Possibly. The flaw is in OpenJDK code, and according to Calif, the following Java distributions built from OpenJDK are also vulnerable:

- Amazon Corretto
- Eclipse Temurin
- Microsoft Build of OpenJDK
- Azul Zulu
- BellSoft Liberica
- SAP SapMachine
- Red Hat OpenJDK
- Oracle OpenJDK

Each vendor releases fixed builds on its own schedule, so check with your distribution's vendor for its fixed versions.

**Which applications are known to be affected?**

[<u>Calif</u>](https://calif.io/java4shell/) says its initial testing showed that an attacker could run their own code on the following applications in their default configurations, when they run on an affected version of Java on a processor that supports AVX-512 VBMI. The list is not exhaustive, according to Calif.

| **Application** | **Calif's result** | 
|---|---|
| Keycloak | Exploitable before login | 
| Atlassian Jira | Exploitable before login | 
| Atlassian Confluence | Exploitable before login | 
| JFrog Artifactory | Exploitable before login | 
| Jenkins | Exploitable before login | 
| PingFederate | Exploitable before login | 
| Apache Kafka Broker | Exploitable after login | 
| Apache Solr | Exploitable after login | 
| Elasticsearch | Exploitable after login | 
| Gerrit | Exploitable after login | 
| Spinnaker | Exploitable after login | 

Calif also said it ran its own code on sample applications built on frameworks including Apache Struts and Spring Boot. Calif adds that everyday functions, including authentication and file uploads, can lead to the vulnerable code, so more applications than the ones Calif tested may be exposed. Calif says researcher samczsun gave it a client-side exploit, and that a Java program can be compromised when it connects over TLS to a server an attacker controls, even if the program offers no service of its own. Calif says it will publish its exploits for individual products at a later date.

**Has Java4Shell been exploited in the wild?**

As of November 18, GreyNoise has reported exploitation attempts against CVE-2026-114938, though GreyNoise has not confirmed any successful exploitation against its sensors. GreyNoise has also observed [scanning activity](https://viz.greynoise.io/tags/6c3395f5-03b7-4162-8e6a-458e46ca101b?scope=greynoise) from a publicly released scanner that checks hosts for affected Java versions. CVE-2026-114938 is not listed in CISA’s Known Exploited Vulnerabilities (KEV) catalog.

**Is there a proof-of-concept (PoC) available?**

Yes. Calif published a PoC alongside its write-up that triggers the flaw without taking control of the system. It shows whether a given Java version and processor reproduce the bug. It does not show whether a particular application is exposed.

On November 17, Kevin Breen of Immersive said on [<u>X</u>](https://x.com/KevTheHermit/status/2122829165925998824) that they had developed a working exploit for CVE-2026-114938. According to Breen, the exploit has to be adapted to each application. It works only on a vulnerable version of Java running on a processor that supports AVX-512 VBMI, and only against applications that decode Base64 data. Breen also said that Apache Tomcat's Basic authentication and the java-jwt library provide ways to exploit the flaw before a user logs in. The post does not say that the exploit has been released.

The same day, [VulnCheck](https://www.vulncheck.com/blog/java4shell) said a working exploit that can run code on an affected system is available to its customers. According to VulnCheck, crashing an affected application is easy if an attacker can reach the vulnerable code, but running code takes substantially more work. It said it does not expect the flaw to be easily or widely exploitable, though it expects attackers to find narrow paths to code execution in specific applications.

Have a functional exploit POC for CVE-2026-114938 aka Java4Shell. This is not a generic exploit and will need to be application specific, you need a CPU with AVX-512 VBMI support, vulnerable JDK Version, and the app needs to use Base64, note that tomcats basic auth and java-jwt…

— KevTheHermit (@KevTheHermit) [November 17, 2026](https://x.com/KevTheHermit/status/2122829165925998824?ref_src=twsrc%5Etfw)


**Are patches available?**

Yes. On November 17, Oracle released the following fixed builds:

| **Java line** | **Affected Oracle build** | **Fixed Oracle build** | 
|---|---|---|
| Java 8 Enterprise Performance Pack | 8u511b33-perf | 8u513-perf | 
| Java 17 | 17.0.21.0.3 | 17.0.21.1 | 
| Java 21 | 21.0.13.0.3 | 21.0.13.1 | 
| Java 25 | 25.0.5.0.3 | 25.0.5.1 | 
| Java 27 | 27.0.1.0.3 | 27.0.1.1 | 

For Oracle GraalVM, see [Oracle’s advisory](https://www.oracle.com/security-alerts/cspunov2026.html). According to the Cyber Centre, the fixed builds are 17.0.21.1 and 21.0.13.1 for GraalVM for JDK, and 21.3.20.1 for GraalVM Enterprise Edition.

Amazon Corretto and Azul Zulu have released fixed builds, and Eclipse Temurin has begun releasing them. Fixed builds of the Microsoft Build of OpenJDK are also available. As of November 19, Red Hat has released fixed OpenJDK packages for Red Hat Enterprise Linux, though it still lists some products that bundle Java, such as Red Hat build of Keycloak, as affected. Ubuntu released fixes for its openjdk-17, openjdk-21, openjdk-25 and openjdk-27 packages on November 18. Debian has fixed openjdk-21 and openjdk-25 in its stable release, Debian 13, while openjdk-17 in Debian 12 is still listed as vulnerable. Oracle’s and Eclipse Temurin’s fixed builds for Java 17, 21, 25 and 27 are 17.0.21.1, 21.0.13.1, 25.0.5.1 and 27.0.1.1. Other distributions use their own version numbers. For other Java distributions, see each vendor’s advisory.

**Are there any mitigations?**

Calif identified two Java startup options that keep the vulnerable code from running. The first, *-XX:-UseBASE64Intrinsics*, turns off the Base64 shortcut. The second, *-XX:UseAVX=2*, turns off AVX-512 instructions. According to Calif, the second option applies only to x86-64 systems, and Java on ARM processors fails to start with it. Neither Oracle nor the OpenJDK Vulnerability Group mentions these options in its advisory.

On November 18, the [Keycloak project](https://www.keycloak.org/2026/11/java4shell-vulnerability-cve-2026-114938) recommended starting its server with `-XX:-UseBASE64Intrinsics` as an interim mitigation. It said its x86-64 container images tagged 26.8.2-1 and 26.8.2-2 include an affected Java build, though the tags alone do not show whether a deployment is exploitable. As of November 19, Keycloak has updated its 26.8 container images to Red Hat OpenJDK 21.0.13.1, which Keycloak says includes the fix. The updated tags are latest, 26.8, 26.8.2 and 26.8.2-3.

**Has Java been targeted historically?**

Yes. CISA's KEV catalog includes 13 vulnerabilities in Oracle Java SE and the Java Runtime Environment (JRE), six of which are known to have been used in ransomware campaigns. Those six are:

| **CVE** | **KEV name** | **Added to KEV** | 
|---|---|---|
| [<u>CVE-2013-0431</u>](https://www.tenable.com/cve/CVE-2013-0431) | Oracle JRE Sandbox Bypass Vulnerability | May 25, 2022 | 
| [<u>CVE-2013-0422</u>](https://www.tenable.com/cve/CVE-2013-0422) | Oracle JRE Remote Code Execution Vulnerability | May 25, 2022 | 
| [<u>CVE-2013-2465</u>](https://www.tenable.com/cve/CVE-2013-2465) | Oracle Java SE Unspecified Vulnerability | March 28, 2022 | 
| [<u>CVE-2012-4681</u>](https://www.tenable.com/cve/CVE-2012-4681) | Oracle Java SE Runtime Environment (JRE) Arbitrary Code Execution Vulnerability | March 3, 2022 | 
| [<u>CVE-2012-1723</u>](https://www.tenable.com/cve/CVE-2012-1723) | Oracle Java SE Runtime Environment (JRE) Arbitrary Code Execution Vulnerability | March 3, 2022 | 
| [<u>CVE-2012-0507</u>](https://www.tenable.com/cve/CVE-2012-0507) | Oracle Java SE Runtime Environment (JRE) Arbitrary Code Execution Vulnerability | March 3, 2022 | 

**Has Tenable Research classified this vulnerability as part of Vulnerability Watch?**

Yes. CVE-2026-114938 has been classified as a "Vulnerability of Interest" as part of [<u>Vulnerability Watch</u>](https://www.tenable.com/blog/reducing-remediation-time-remains-a-challenge-how-tenable-vulnerability-watch-can-help).

**Are Tenable products affected by this vulnerability?**

Tenable has applied appropriate mitigations on affected SaaS platforms and patches are being rolled out as they’re made available. The following products are affected:

- Tenable Enclave Security
- Tenable OT

Customers are advised to follow security best practices such as network isolation and EDR protection. As patches are made available across our products, customers will be advised via [tenable.com/security](https://www.tenable.com/security).

Tenable Security Center and Tenable Nessus are not affected, because the affected Java component is not part of either product. Some customers install Java separately, and these products use it only to generate PDF reports. Tenable advises those customers to upgrade that Java installation to a vendor-patched build. The upgrade steps are in this [knowledge base article](https://connect.tenable.com/kb/tenable-nessus-knowledge-base/java4shell-cve-2026-114938-java-upgrade-recommended-for-pdf-reporting/112722), which says to pause PDF report generation, including scheduled reports, before upgrading Java.

**Has Tenable released any product coverage for this vulnerability?**

A list of Tenable plugins for this vulnerability can be found on the individual CVE page for [<u>CVE-2026-114938</u>](https://www.tenable.com/cve/CVE-2026-114938/plugins) as they're released. This link will display all available plugins for this vulnerability, including upcoming plugins in our [<u>Plugins Pipeline</u>](https://www.tenable.com/plugins/pipeline).

**How can Tenable customers find affected assets?**

Tenable One Vulnerability Management customers can go to Explore > Software to view installed software across their assets, then filter by product name and version to look for Java installations to compare against the affected versions above. Exposure also depends on the processor, as described above. Software data comes from credentialed and agent scans. For details, see [<u>Use the Software Page</u>](https://docs.tenable.com/vulnerability-management/Content/Explore/use-software-page.htm).

Tenable One Vulnerability Management customers can also use the [<u>Java Visibility and Exposures</u>](https://www.tenable.com/vulnerability-management-reports/java-visibility-and-exposures) report, which lists Java installations and the hosts where they were detected.

Tenable One Attack Surface Management customers can find internet-facing assets running Java with the filter Programming Languages contains Java. Those assets can then be scanned with other Tenable sensors to check whether they are affected by CVE-2026-114938.

With Tenable Hexa AI, Tenable One customers can tag assets with Java4Shell findings and create an exposure initiative to track remediation. Results are based on Tenable plugin detections, which check Java versions and do not account for the processor requirement described above.

An example Tenable Hexa AI prompt:

```
List any asset found vulnerable to CVE-2026-114938, state ACTIVE or RESURFACED only.
Once this is done, create a tag Java4Shell with the value "Vulnerable", and apply it to every asset from previous step.
Finally, create an exposure initiative for Java4Shell using the Java4Shell tag, with SLAs and a description, and give me the link.
```
### Get more information

**Join** <u>Tenable's Research Special Operations (RSO) Team</u> **on Tenable Connect for further discussions on the latest cyber threats.**

## Learn more

- Exposure Management
- Vulnerability Management

Tenable One

## Request a demo

The world’s leading AI-powered exposure management platform.

## Thank You

Thank you for your interest in Tenable One.

A representative will be in touch soon.

Debug:
Form ID: 7469
Form Name: one-eval

Form Class: c-form form-panel\_\_global-form c-form--mkto js-mkto-no-css js-form-hanging-label c-form--hide-comments

Form Wrapper ID: one-eval-form-wrapper

Confirmation Class: one-eval-confirmform-modal

Simulate Success
