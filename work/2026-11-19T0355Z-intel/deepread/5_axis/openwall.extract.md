---
title: oss-security
url: https://openwall.com/lists/oss-security/2026/11/06/12
hostname: openwall.com
sitename: "CVE-2026-90436: Apache Axis 1.x (EOL): unauthenticated remote class instantiation via SOAP fault exceptionName"
date: "2026-11-06"
fingerprint: "9a28c692e140d3da"
---
|   |  | 

|  | 

|  [Follow @Openwall on Twitter for new release announcements and other news](https://twitter.com/openwall) | 

Message-ID: \<2dcb607b-c04b-2d18-7433-c744b4549045@apache.org>
Date: Fri, 06 Nov 2026 15:32:01 +0000
From: Robert Lazarski \<robertlazarski@...che.org>
To: oss-security@...ts.openwall.com
Subject: CVE-2026-90436: Apache Axis 1.x (EOL): unauthenticated remote
 class instantiation via SOAP fault exceptionName 
Severity: critical 
Affected versions:
- Apache Axis 1.x (EOL) through 1.4
- Apache Axis 1.x (EOL) through 1.4
- Apache Axis 1.x (EOL) aac718c6035435d96b39d6aebb9c078a13af7cc8 before 41f3b4e8d04e310ca81f86b92630ab2c11d608bd
Description:
\*\* UNSUPPORTED WHEN ASSIGNED \*\* Deserialization of an inbound SOAP fault in Apache Axis 1.x allows unauthenticated remote class instantiation. When a SOAP \<Fault> carries a \<detail>\<exceptionName> element, Axis loads the named class and, if a String \<data> element is also present, instantiates it through its String constructor before checking that it is an AxisFault. Loading alone runs the class's static initializer. With a suitable class on the application's classpath this leads to remote code execution. The fault is parsed while the engine resolves the target service, before any per-service handler chain runs, so authentication handlers configured on a service do not protect against it. This affects all Apache Axis 1.x versions through 1.4.
As Axis 1 has been EOL we recommend you migrate to a different SOAP engine, such as Apache Axis 2/Java. Alternatively you could use a build of Axis with the patch from [https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd](https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd) applied. The Apache Axis project does not expect to create an Axis 1.x release fixing this problem.
Credit:
José Apari-Pantigozo from OKIOK (finder)
References:
[https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd](https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd)
[https://axis.apache.org/](https://axis.apache.org/)
[https://www.cve.org/CVERecord?id=CVE-2026-90436](https://www.cve.org/CVERecord?id=CVE-2026-90436)

[Powered by blists](https://www.openwall.com/blists/) - [more mailing lists](https://lists.openwall.net)

Please check out the
[Open Source Software Security Wiki](https://oss-security.openwall.org/wiki/), which is counterpart to this
[mailing list](https://oss-security.openwall.org/wiki/mailing-lists/oss-security).

Confused about [mailing lists](https://openwall.com/lists/) and their use?
[Read about mailing lists on Wikipedia](https://en.wikipedia.org/wiki/Electronic_mailing_list)
and check out these
[guidelines on proper formatting of your messages](https://www.complang.tuwien.ac.at/anton/mail-news-errors.html).
