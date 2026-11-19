Title: CVE-2026-90436: Apache Axis 1.x (EOL): unauthenticated remote class instantiation via SOAP fault exceptionName

URL Source: https://lists.apache.org/thread/8slf0j9gz35z56t0glt5h0ncwlbn4bdz

Markdown Content:
Severity: critical Affected versions: - Apache Axis 1.x (EOL) through 1.4 - Apache Axis 1.x (EOL) through 1.4 - Apache Axis 1.x (EOL) aac718c6035435d96b39d6aebb9c078a13af7cc8 before 41f3b4e8d04e310ca81f86b92630ab2c11d608bd Description: ** UNSUPPORTED WHEN ASSIGNED ** Deserialization of an inbound SOAP fault in Apache Axis 1.x allows unauthenticated remote class instantiation. When a SOAP <Fault> carries a <detail><exceptionName> element, Axis loads the named class and, if a String <data> element is also present, instantiates it through its String constructor before checking that it is an AxisFault. Loading alone runs the class's static initializer. With a suitable class on the application's classpath this leads to remote code execution. The fault is parsed while the engine resolves the target service, before any per-service handler chain runs, so authentication handlers configured on a service do not protect against it. This affects all Apache Axis 1.x versions through 1.4. As Axis 1 has been EOL we recommend you migrate to a different SOAP engine, such as Apache Axis 2/Java. Alternatively you could use a build of Axis with the patch from

[https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd](https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd)

applied. The Apache Axis project does not expect to create an Axis 1.x release fixing this problem. Credit: José Apari-Pantigozo from OKIOK (finder) References:

[https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd](https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd)

[https://axis.apache.org](https://axis.apache.org/)

/

[https://www.cve.org/CVERecord?id=CVE-2026-90436](https://www.cve.org/CVERecord?id=CVE-2026-90436)

--------------------------------------------------------------------- To unsubscribe, e-mail: java-user-unsubscribe@axis.apache.org For additional commands, e-mail: java-user-help@axis.apache.org

Links/Buttons:
- [ASF Mailing List Archives](https://lists.apache.org/)
- [Log in](https://lists.apache.org/oauth.html)
- [‹ Back to java-user@axis.apache.org](https://lists.apache.org/list.html?java-user@axis.apache.org:2026-11)
- [](https://lists.apache.org/thread.html/8slf0j9gz35z56t0glt5h0ncwlbn4bdz)
- [https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd](https://github.com/apache/axis-axis1-java/commit/41f3b4e8d04e310ca81f86b92630ab2c11d608bd)
- [https://axis.apache.org](https://axis.apache.org/)
- [https://www.cve.org/CVERecord?id=CVE-2026-90436](https://www.cve.org/CVERecord?id=CVE-2026-90436)
- [Apache Pony Mail](https://ponymail.apache.org/)
- [Apache Software Foundation](https://www.apache.org/)
- [GitHub repository](https://github.com/DinoSourceDK/ponee-fauxl)
- [API](https://lists.apache.org/apidocs.html)
