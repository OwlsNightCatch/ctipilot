---
title: GeoServer Pre-Authentication RCE via WFS and HSQLDB
author: CryptoCat
url: https://cryptocat.me/blog/research/analysis/geoserver_preauth_rce/
hostname: cryptocat.me
description: Anonymous WFS stored queries in GeoServer leak the remember-me key and admin password digest, which is enough to forge an admin cookie and run commands through HSQLDB deserialization.
sitename: CryptoCat's Blog
date: "2026-11-23"
fingerprint: c998e740ae0282c7
language: en
image: https://cryptocat.me/blog/research/analysis/geoserver_preauth_rce/images/geoserver_preauth_rce_share.png
pagetype: article
filedate: "2026-11-25"
---
# GeoServer Pre-Authentication RCE via WFS and HSQLDB

## TL;DR

- I found unauthenticated remote command execution in GeoServer that works on a default installation.
- Prefixing the Web Feature Service (WFS) name, as in `x/WFS`, slips past the admin-only rule for stored queries. GeoServer turns escaped text in a saved query into live `xi:include` elements, which leaks the files holding the remember-me key and the admin password digest.
- Those two values forge an administrator cookie without cracking the password. As admin, the attacker points a JDBC user service at an uploaded HSQLDB database, and the bundled driver deserialises a stored value that runs commands.
- GeoServer 2.27.6 and earlier, 2.28.0 to 2.28.5, and 3.0.0 to 3.0.1 are affected. The fixes are in 2.27.7, 2.28.6 and 3.0.2, and GeoServer lists all five CVEs in the [remember-me key advisory](https://github.com/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq).

## Summary

- **Product:** GeoServer
- **Vulnerability:** Pre-Authentication Remote Command Execution via WFS and HSQLDB
- **Affected Versions:** `>= 3.0.0, <= 3.0.1`, `>= 2.28.0, <= 2.28.5`, `<= 2.27.6`
- **Fixed In:** 3.0.2, 2.28.6 and 2.27.7
- **CVSS Severity:** 9.8 (critical, reporter-assessed)
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Required Privilege:** None
- **Reported:** August 2, 2026

GeoServer published the chain as five advisories, one per independently fixable step, each scored with GeoServer's own CVSS 4.0 rating unless noted:

| Issue | Root cause | CVSS | Advisory | CVE | 
|---|---|---|---|---|
| Data-directory path in WFS exception | An overlong stored-query ID fails in the filesystem, and the WFS exception returns the full path | [6.9 (medium)](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:N/VA:N/SC:N/SI:N/SA:N) | [GHSA-4v26-c537-jvxc](https://github.com/geoserver/geoserver/security/advisories/GHSA-4v26-c537-jvxc) | [CVE-2026-129244](https://nvd.nist.gov/vuln/detail/CVE-2026-129244) | 
| `service=x/WFS` operation-security bypass | The dispatcher strips `x/`, but service security still matches the rules against `x/WFS` | [8.8 (high)](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:H/VA:L/SC:N/SI:N/SA:N) | [GHSA-rv5g-g2r9-58rj](https://github.com/geoserver/geoserver/security/advisories/GHSA-rv5g-g2r9-58rj) | [CVE-2026-129243](https://nvd.nist.gov/vuln/detail/CVE-2026-129243) | 
| Stored-query XInclude local file read | Saved query text is reparsed into XML, then reloaded with XInclude on and a resolver that allows `file:` | [8.6 (high, CVSS 3.1)](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N) | [GHSA-39mw-5chv-jh47](https://github.com/geoserver/geoserver/security/advisories/GHSA-39mw-5chv-jh47) | [CVE-2026-120705](https://nvd.nist.gov/vuln/detail/CVE-2026-120705) | 
| Predictable remember-me key | The cookie signing key is read from the data directory and ships as `geoserver` | [9.2 (critical)](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N) | [GHSA-hgm3-wq4h-8vvq](https://github.com/geoserver/geoserver/security/advisories/GHSA-hgm3-wq4h-8vvq) | [CVE-2026-129245](https://nvd.nist.gov/vuln/detail/CVE-2026-129245) | 
| JDBC user-service deserialisation | User and role properties are read with `getObject()`, so HSQLDB deserialises `OTHER` values | [8.6 (high)](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N) | [GHSA-9wf2-fcgq-vxhq](https://github.com/geoserver/geoserver/security/advisories/GHSA-9wf2-fcgq-vxhq) | [CVE-2026-129242](https://nvd.nist.gov/vuln/detail/CVE-2026-129242) | 

## Introduction

\[A\]I went through the stock GeoServer 3.0.0 distribution, looking for an anonymous request that could read its data directory. GeoServer signs remember-me cookies with the stored password digest from `users.xml` and a key that ships as `geoserver`, so reading `users.xml` would be enough to become an administrator on any install that kept that key.

Stored-query names are cleaned into filenames, and the shipped service rules only let administrators create or delete stored queries. One spelling of the service name could get past those rules.

## Root Cause Analysis

### A Filename Error Reveals the Data Directory (CVE-2026-129244)

A stored query is a named WFS query saved by GeoServer. GeoServer maps its name to a resource in [`StoredQueryProvider.java`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/wfs-core/src/main/java/org/geoserver/wfs/StoredQueryProvider.java#L177-L209), while [`toFilename()`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/wfs-core/src/main/java/org/geoserver/wfs/StoredQueryProvider.java#L235-L238) builds its filename.

```
public StoredQuery getStoredQuery(String name) {
    // ... default-query handling omitted.
    try {
        Resource res = getResourceByContext(toFilename(name)); // [1] Data-directory lookup.
        // ... ordinary missing-query and parsing logic omitted.
    } catch (Exception e) {
        throw new RuntimeException("Error accessing stored query: " + name, e);
    }
}
private Resource getResourceByContext(String filename) {
    Resource res = storedQueryDirByContext().get(filename);
    if (res.getType() == Type.RESOURCE) { // [2] Filesystem lookup.
        return res;
    }
    // ... workspace fallback omitted.
    return null;
}
// ... stored-query persistence omitted.
String toFilename(String name) {
    // remove any special characters... like ':'
    return name.replaceAll("\\W", "") + ".xml"; // [3] Adds .xml.
}
```
The `storedQuery_id` from an anonymous `GetFeature` request becomes a data-directory lookup at `[1]`, which reaches the filesystem at `[2]`. The only change made to it is at `[3]`, which strips non-word characters and adds `.xml`, so nothing limits its length. On a stock data directory, a 4,092-character identifier makes the path longer than Linux allows.

The filesystem resource wrapper catches the resulting I/O error in [`FileSystemResourceStore.java`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/platform/src/main/java/org/geoserver/platform/resource/FileSystemResourceStore.java#L415-L432).

```
@Override
public Type getType() {
    try {
        BasicFileAttributes attributes =
                java.nio.file.Files.readAttributes(file.toPath(), BasicFileAttributes.class); // [4] Fails on an overlong path.
        // ... normal resource-type handling omitted.
    } catch (NoSuchFileException e) {
        return Type.UNDEFINED;
    } catch (IOException e) {
        throw new IllegalStateException(e); // [5] Preserves the cause.
    }
}
```
The overlong path makes `readAttributes()` fail with `File name too long` at `[4]`, and `[5]` rethrows that error as the cause of an `IllegalStateException`. GeoServer's OWS exception builder then turns the whole exception chain into the public response in [`Ows11Util.java`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/ows/src/main/java/org/geoserver/ows/Ows11Util.java#L128-L130).

```
StringBuffer sb = new StringBuffer();
OwsUtils.dumpExceptionMessages(exception, sb, true); // [6] Collects nested messages.
e.getExceptionText().add(sb.toString()); // [7] Returns them publicly.
```
[`dumpExceptionMessages()`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/ows/src/main/java/org/geoserver/ows/util/OwsUtils.java#L235-L263) at `[6]` walks every nested cause, so the filesystem message, path included, ends up in the exception text returned at `[7]`. Cutting the known `/wfs/query/<identifier>.xml` suffix off that path leaves the data directory.

### Two Names for the Same WFS Service (CVE-2026-129243)

The release [`services.properties`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/data/release/security/services.properties#L4-L10) protects stored-query creation and deletion.

```
# services.properties
# If not specified in this file, a service or method will be considered unsecured
# ... unrelated examples omitted.
wfs.DropStoredQuery=ADMIN,GROUP_ADMIN
wfs.CreateStoredQuery=ADMIN,GROUP_ADMIN
```
Both rules only match a service named `wfs`.

GeoServer's dispatcher also accepts service identifiers containing a slash. [`Dispatcher.findService()`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/ows/src/main/java/org/geoserver/ows/Dispatcher.java#L1258-L1276) treats the prefix as path or workspace context.

```
Service findService(String id, String ver, String namespace) throws ServiceException {
    // ... version and service loading omitted.
    if (id.contains("/")) {
        id = id.substring(id.indexOf("/") + 1); // [8] x/WFS becomes WFS.
    }
    // ... matching setup omitted.
    for (Service sBean : services) {
        if (sBean.getId().equalsIgnoreCase(id)) {
            matches.add(sBean);
        }
    }
```
For `service="x/WFS"`, the dispatcher strips `x/` at `[8]` and finds the real WFS service. The surrounding [`service()` method](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/ows/src/main/java/org/geoserver/ows/Dispatcher.java#L649-L675) attaches that WFS service to the request, but leaves the request's service name as `x/WFS`.

The security callback in [`OperationSecurityCallback.java`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/main/src/main/java/org/geoserver/security/OperationSecurityCallback.java#L47-L67) reads that name.

```
public Operation operationDispatched(Request request, Operation operation) {
    String service = request.getService(); // [9] Still x/WFS.
    String method = request.getRequest();
    List<ServiceAccessRule> rules = dao.getRules();
    ServiceAccessRule bestMatch = null;
    for (ServiceAccessRule rule : rules) {
        if (rule.getService().equals(ServiceAccessRule.ANY)
                || rule.getService().equalsIgnoreCase(service)) { // [10] No wfs match.
            if (rule.getMethod().equals(ServiceAccessRule.ANY)
                    || rule.getMethod().equalsIgnoreCase(method)) {
                bestMatch = rule;
            }
        }
    }
    // if there is a matching rule apply it
    if (bestMatch != null) { // [11] No match, no role check.
```
The callback still has `x/WFS` at `[9]`, which never equals `wfs` at `[10]`. With no matching rule, `[11]` skips the role check, so an anonymous user can create and delete stored queries.

### XML Text Becomes XML Again (CVE-2026-120705)

XInclude lets an XML document include another resource. The stored-query request carries escaped XInclude elements inside the WFS query text.

```
<wfs:Query typeNames="">
  <xi:include xmlns:xi="http://www.w3.org/2001/XInclude"
    xmlns="" href="file:///absolute/data/security/config.xml" parse="text"/>
  <xi:include xmlns:xi="http://www.w3.org/2001/XInclude"
    xmlns="" href="file:///absolute/data/security/usergroup/default/users.xml" parse="xml"/>
</wfs:Query>
```
The request parser decodes `<` into a literal `<` character. GeoTools' [`CopyingHandler.characters()`](https://github.com/geotools/geotools/blob/d12059deca3471f92ffe8e23119ddad69325e856/modules/extension/xsd/xsd-wfs/src/main/java/org/geotools/wfs/v2_0/bindings/CopyingHandler.java#L99-L106) appends that character data directly.

```
@Override
public void characters(char[] ch, int start, int length) throws SAXException {
    // ... buffer initialisation omitted.
    buffer.append(ch, start, length); // [12] Appends decoded text unescaped.
}
```
`[12]` copies the decoded text into the query unescaped, so the stored query text now holds a literal `<xi:include .../>` string. When GeoServer persists the accepted query, [`QueryExpressionTextTypeBinding.encode()`](https://github.com/geotools/geotools/blob/d12059deca3471f92ffe8e23119ddad69325e856/modules/extension/xsd/xsd-wfs/src/main/java/org/geotools/wfs/v2_0/bindings/QueryExpressionTextTypeBinding.java#L90-L108) parses that string again.

```
QueryExpressionTextType qe = (QueryExpressionTextType) object;
if (!qe.isIsPrivate()) {
    // ... DOM and namespace setup omitted.
    SAXParser saxp = XMLUtils.newSAXParserFactory(null).newSAXParser();
    saxp.parse(new InputSource(new StringReader(qe.getValue())), h); // [13] Reparses text as markup.
    Document d = h.getDocument();
    e.appendChild(document.importNode(d.getDocumentElement(), true));
}
```
At `[13]` the literal `<` becomes markup, so the saved file contains live `xi:include` elements.

The public `DescribeStoredQueries` operation loads that file through a fresh parser in [`StoredQueryProvider.java`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/wfs-core/src/main/java/org/geoserver/wfs/StoredQueryProvider.java#L244-L254).

```
StoredQuery parseStoredQuery(Resource file) throws Exception {
    return parseStoredQuery(file, new Parser(new WFSConfiguration())); // [14] Fresh WFS parser.
}
StoredQuery parseStoredQuery(Resource file, Parser p) throws Exception {
    p.setRootElementType(WFS.StoredQueryDescriptionType);
    try (InputStream fin = file.in()) {
        StoredQueryDescriptionType q = (StoredQueryDescriptionType) p.parse(new BufferedInputStream(fin));
        return createStoredQuery(q, false);
    }
}
```
`[14]` creates a new WFS parser for each reload. GeoTools builds its SAX factory in [`XMLUtils.java`](https://github.com/geotools/geotools/blob/d12059deca3471f92ffe8e23119ddad69325e856/modules/library/xml/src/main/java/org/geotools/xml/XMLUtils.java#L935-L948) with DTD support disabled, and [`supportDTD()`](https://github.com/geotools/geotools/blob/d12059deca3471f92ffe8e23119ddad69325e856/modules/library/xml/src/main/java/org/geotools/xml/XMLUtils.java#L293-L298) ties XInclude to that flag.

```
factory.setXIncludeAware(!supportDTD); // [15] XInclude on when DTDs off.
```
That turns XInclude on at `[15]`, so the reload parser processes the `xi:include` elements.

During startup, the release [`web.xml`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/web/app/src/main/webapp/WEB-INF/web.xml#L221-L235) runs `GeoserverInitStartupListener` before the Spring context loader. The resolver-provider bean doesn't exist yet, so [the listener installs `NullEntityResolver.INSTANCE`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/main/src/main/java/org/geoserver/GeoserverInitStartupListener.java#L94-L100) in GeoTools' process-wide hints. That resolver [advertises access to all protocols and returns `null`](https://github.com/geotools/geotools/blob/d12059deca3471f92ffe8e23119ddad69325e856/modules/library/metadata/src/main/java/org/geotools/util/NullEntityResolver.java#L47-L78), which directs the parser to open the local `file:` references normally. `DescribeStoredQueries` serialises the included content into its public response.

The response contains the active `<key>` from `security/config.xml` and the `default` user service's `users.xml`, including the administrator's password digest from its `password` attribute.

### The Cookie Needs No Password Cracking (CVE-2026-129245)

GeoServer's remember-me usernames [carry the user service name](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/main/src/main/java/org/geoserver/security/rememberme/RememberMeUserDetailsService.java#L35-L43), so the stock administrator is `admin@default`. [`RememberMeUserDetailsService.java`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/main/src/main/java/org/geoserver/security/rememberme/RememberMeUserDetailsService.java#L55-L71) splits that name, loads the service and returns its user.

```
@Override
public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException, DataAccessException {
    Matcher m = TOKEN_PATTERN.matcher(username);
    // ... invalid-input handling omitted.
    String user = m.group(1).replace("\\@", "@");
    String service = m.group(2);
    try {
        GeoServerUserGroupService ugService = securityManager.loadUserGroupService(service); // [16] Selects user service.
        return new RememberMeUserDetails(ugService.loadUserByUsername(user), service); // [17] Loads its user.
    } catch (IOException e) {
        // ... error handling omitted.
    }
}
```
`default` at `[16]` is the file user service, and the XInclude read already returned its `users.xml`. [`XMLUserGroupService`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/main/src/main/java/org/geoserver/security/xml/XMLUserGroupService.java#L154-L177) passes each `password` attribute through [`createUserObject()`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/main/src/main/java/org/geoserver/security/xml/XMLUserGroupService.java#L228-L232) unchanged, so the user loaded at `[17]` carries the same digest the attacker already has.

Spring Security 7.0.5 builds the cookie signature in its [four-argument implementation](https://github.com/spring-projects/spring-security/blob/53bc6a77963209bb2a5f3efdd855b1f4a8051cc3/web/src/main/java/org/springframework/security/web/authentication/rememberme/TokenBasedRememberMeServices.java#L198-L208).

```
protected String makeTokenSignature(long tokenExpiryTime, String username, @Nullable String password,
        RememberMeTokenAlgorithm algorithm) {
    String data = username + ":" + tokenExpiryTime + ":" + password + ":" + getKey(); // [18] Uses both leaked secrets.
    try {
        MessageDigest digest = MessageDigest.getInstance(algorithm.getDigestAlgorithm());
        return new String(Hex.encode(digest.digest(data.getBytes())));
    }
    catch (NoSuchAlgorithmException ex) {
        // ... error handling omitted.
    }
}
```
`[18]` hashes the username, expiry, password digest and key. WFS has already returned the digest and the key, so an attacker can compute a valid SHA-256 signature for `admin@default` and exchange the cookie for an administrator session.

### A Database Value Becomes a Java Object (CVE-2026-129242)

With that session, an attacker can write files beneath the data directory through [`ResourceController.resourcePut()`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/restconfig/src/main/java/org/geoserver/rest/resources/ResourceController.java#L328-L379) and register a JDBC user service through [`UserGroupServiceController.post()`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/restconfig/src/main/java/org/geoserver/rest/security/UserGroupServiceController.java#L89-L95). HSQLDB ships with GeoServer 3.0.0, and [`JdbcSecurityConfigValidator.java`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/security/jdbc/src/main/java/org/geoserver/security/jdbc/JdbcSecurityConfigValidator.java#L100-L109) allows a local HSQLDB URL, so the service can point at an uploaded database.

A user lookup through the resulting JDBC service reaches this loop in [`JDBCUserGroupService.java`](https://github.com/geoserver/geoserver/blob/b9b38b94428824700ff4e48326ddde6150e50e1e/src/security/jdbc/src/main/java/org/geoserver/security/jdbc/JDBCUserGroupService.java#L171-L178).

```
ps2 = getDMLStatement("userprops.selectForUser", con);
ps2.setString(1, username);
rs2 = ps2.executeQuery();
while (rs2.next()) {
    String propName = rs2.getString(1);
    Object propValue = rs2.getObject(2); // [19] Gets property as an object.
    u.getProperties().put(propName, propValue == null ? "" : propValue);
}
```
`getObject()` at `[19]` returns whatever Java object the driver says the column holds. For HSQLDB's `OTHER` type, [`JDBCResultSet.getObject()`](https://sourceforge.net/p/hsqldb/svn/6658/tree/base/tags/2.7.2/src/org/hsqldb/jdbc/JDBCResultSet.java#l1676) in version 2.7.2 takes this branch.

```
case Types.OTHER :
case Types.JAVA_OBJECT : {
    Object o = getColumnInType(columnIndex, sourceType);
    if (o == null) {
        return null;
    }
    try {
        return ((JavaObjectData) o).getObject(); // [20] Converts bytes to an object.
    } catch (HsqlException e) {
        throw JDBCUtil.sqlException(e);
    }
}
```
`[20]` hands the stored bytes to [`JavaObjectData.getObject()`](https://sourceforge.net/p/hsqldb/svn/6658/tree/base/tags/2.7.2/src/org/hsqldb/types/JavaObjectData.java#l109).

```
public Object getObject() {
    try {
        return InOutUtil.deserialize(data); // [21] Deserialises the bytes.
    } catch (Exception e) {
        throw Error.error(ErrorCode.X_22521, e.toString());
    }
}
```
[`InOutUtil.deserialize()`](https://sourceforge.net/p/hsqldb/svn/6658/tree/base/tags/2.7.2/src/org/hsqldb/lib/InOutUtil.java#l116) at `[21]` builds a plain `ObjectInputStream`.

```
public static Serializable deserialize(byte[] ba)
throws IOException, ClassNotFoundException {
    HsqlByteArrayInputStream bi = new HsqlByteArrayInputStream(ba);
    ObjectInputStream        is = new ObjectInputStream(bi); // [22] Plain object stream.
    return (Serializable) is.readObject(); // [23] Reads attacker graph.
}
```
The stream at `[22]` has no object filter, so `readObject()` at `[23]` rebuilds whatever object graph the attacker stored, from any serialisable class on GeoServer's classpath.

## Impact

Successful exploitation runs arbitrary commands with the operating-system permissions of the GeoServer process. The chain works on a default Linux install with no extensions or configuration changes. It ran on OpenJDK 17 under Jetty 12 and on the Java 21 runtime in the official Docker image.

## Exploitation

### Preconditions

- Network access to GeoServer's WFS endpoint and REST API.
- The stock `admin` account enabled in the `default` user service.
- A Linux host, because the payload runs `/bin/sh -c`.

### PoC

The [PoC](https://github.com/Crypto-Cat/geoserver-unauth-rce-poc/blob/main/geoserver_preauth_rce.py) accompanying this writeup runs the whole chain and prints the command's output. Its HSQLDB database stores a `PriorityQueue` with a `BeanComparator`. When the queue rebuilds itself, the comparator calls `getOutputProperties()` on a JDK `TemplatesImpl`. That loads a compiled XSLT translet, and the translet's constructor runs the command.

```
python3 geoserver_preauth_rce.py -u http://127.0.0.1:18080/geoserver -c id
```
```
 [*] Probing anonymous WFS stored-query errors for the data-directory path
 [+] data directory: /opt/geoserver_data
 [*] Persisting an anonymous x/WFS stored query with deferred XInclude
 [+] DescribeStoredQueries disclosed the remember-me key and admin password digest
 [*] Forging a remember-me cookie and exchanging it for a session
 [+] administrator JSESSIONID accepted by the REST API
 [*] Uploading the HSQLDB payload database and request via REST
 [+] registered JDBC user-group service 'jdbc_geoserver_poc'
 [*] Triggering deserialisation through a user-property lookup
 [+] command executed (exit code 0)
 [+] output of: id
  ------------------------------------------------------------
uid=0(root) gid=0(root) groups=0(root)
 [*] Cleaning up
 [+] removed the staging directory and temporary JDBC service
```
This run is against the official 3.0.0 container, where GeoServer runs as root.

## Patch Diffing

### The Overlong ID No Longer Leaks the Path

[GEOS-12240](https://osgeo-org.atlassian.net/browse/GEOS-12240) changes [`StoredQueryProvider.getStoredQuery()`](https://github.com/geoserver/geoserver/blob/fe9d9b8cbe04b334c90b6afb6fdd7951992cb245/src/wfs-core/src/main/java/org/geoserver/wfs/StoredQueryProvider.java#L203-L225) in two places.

```
// StoredQueryProvider.java (getStoredQuery)
+    // an id too long to form a valid file name cannot match a stored query
+    if (name == null || isIdTooLong(name)) {
+        return null;
+    }
+
     try {
         // ... unchanged lookup and parsing omitted.
     } catch (Exception e) {
-        throw new RuntimeException("Error accessing stored query: " + name, e);
+        LOGGER.log(Level.WARNING, e, () -> "Error accessing stored query: " + name);
+        throw new RuntimeException("Error accessing stored query: " + name);
     }
```
The early return keeps an overlong ID away from `Files.readAttributes()`, and the new `throw` drops the `e` cause, so the filesystem error only reaches the log. An attacker who already knows the data-directory path doesn't need this step.

### The Service Name Is Canonicalised Before the Access Check

[`Dispatcher.service()`](https://github.com/geoserver/geoserver/blob/fe9d9b8cbe04b334c90b6afb6fdd7951992cb245/src/ows/src/main/java/org/geoserver/ows/Dispatcher.java#L651-L681) now replaces the request's service name with the resolved service ID before the security callback runs, as long as the request had one ([GEOS-12195](https://osgeo-org.atlassian.net/browse/GEOS-12195), [PR #9922](https://github.com/geoserver/geoserver/pull/9922)).

```
// Dispatcher.java (service)
     req.setServiceDescriptor(serviceDescriptor);
+    // don't set it if it was never provided in the first place
+    if (req.getService() != null) {
+        req.setService(serviceDescriptor.getId());
+    }
     return fireServiceDispatchedCallback(req, serviceDescriptor);
```
`OperationSecurityCallback` is unchanged, but it now reads `WFS` instead of `x/WFS`. The `wfs.CreateStoredQuery` and `wfs.DropStoredQuery` rules match, so the anonymous request is rejected before it can store anything.

### Stored-Query Parsing Uses the Configured Entity Resolver

[`StoredQueryProvider.parseStoredQuery()`](https://github.com/geoserver/geoserver/blob/fe9d9b8cbe04b334c90b6afb6fdd7951992cb245/src/wfs-core/src/main/java/org/geoserver/wfs/StoredQueryProvider.java#L280-L294) installs GeoServer's configured entity resolver on the reload parser ([GEOS-12199](https://osgeo-org.atlassian.net/browse/GEOS-12199), [PR #9928](https://github.com/geoserver/geoserver/pull/9928)).

```
// StoredQueryProvider.java (parseStoredQuery, getEntityResolver)
 StoredQuery parseStoredQuery(Resource file, Parser p) throws Exception {
     p.setRootElementType(WFS.StoredQueryDescriptionType);
+    EntityResolver entityResolver = getEntityResolver();
+    if (entityResolver != null) {
+        p.setEntityResolver(entityResolver);
+    }
     try (InputStream fin = file.in()) {
 // ... unchanged parsing omitted.
+private EntityResolver getEntityResolver() {
+    return catalog.getResourcePool().getEntityResolver();
+}
```
The resolver now comes from the catalog's `ResourcePool` instead of the process-wide `NullEntityResolver`. The file is still reparsed, but its `xi:include` elements can no longer open `file:` references, so `DescribeStoredQueries` has nothing to return from `config.xml` or `users.xml`.

GEOS-12199 also sets the resolver in `StoredQuery.compile()`, which parses the built-in `GetFeatureById` query. That query has its own XML injection, which [GHSA-39mw-5chv-jh47](https://github.com/geoserver/geoserver/security/advisories/GHSA-39mw-5chv-jh47) describes. GeoServer filed the stored-query XInclude read under the same advisory. The advisory also lists [GEOT-7938](https://osgeo-org.atlassian.net/browse/GEOT-7938) from GeoTools 35.2, where `PreventLocalEntityResolver` now follows allowed HTTP redirects itself and checks each destination against its allow-list.

### JDBC Property Values Are Read as Text

[GEOS-12239](https://osgeo-org.atlassian.net/browse/GEOS-12239) changes [`JDBCUserGroupService`](https://github.com/geoserver/geoserver/blob/fe9d9b8cbe04b334c90b6afb6fdd7951992cb245/src/security/jdbc/src/main/java/org/geoserver/security/jdbc/JDBCUserGroupService.java#L173-L178) to read each property value with `getString()` instead of `getObject()`.

```
// JDBCUserGroupService.java (user-property loop)
 while (rs2.next()) {
     String propName = rs2.getString(1);
-    Object propValue = rs2.getObject(2);
+    String propValue = rs2.getString(2);
     u.getProperties().put(propName, propValue == null ? "" : propValue);
 }
```
An `OTHER` value now comes back as its string form, so HSQLDB never hands the stored bytes to `ObjectInputStream`. The same change covers the bulk user-property load and every property read in [`JDBCRoleService`](https://github.com/geoserver/geoserver/blob/fe9d9b8cbe04b334c90b6afb6fdd7951992cb245/src/security/jdbc/src/main/java/org/geoserver/security/jdbc/JDBCRoleService.java#L150-L157).

### The Remember-Me Key Is No Longer Read From the Data Directory

[PR #10008](https://github.com/geoserver/geoserver/pull/10008) removes the stored key and its setter from [`RememberMeServicesConfig`](https://github.com/geoserver/geoserver/blob/fe9d9b8cbe04b334c90b6afb6fdd7951992cb245/src/main/src/main/java/org/geoserver/security/rememberme/RememberMeServicesConfig.java#L27-L56). The key now comes from `GEOSERVER_REMEMBERME_KEY`, or from a random value generated once per run.

```
// RememberMeServicesConfig.java
 private static final long serialVersionUID = 1L;
-public static final String DEFAULT_KEY = "geoserver";
+/** System or environment property that sets the remember-me cookie key across a cluster. */
+public static final String KEY_PROPERTY = "GEOSERVER_REMEMBERME_KEY";
+
+private static final int RANDOM_KEY_BYTES = 32;
+
+private static final SecureRandom SR = new SecureRandom();
+private static final String resolvedKey = resolveKey();
-String key = DEFAULT_KEY;
+static String resolveKey() {
+    String configured = GeoServerExtensions.getProperty(KEY_PROPERTY);
+    if (configured != null && !configured.isBlank()) {
+        return configured;
+    }
+    byte[] bytes = new byte[RANDOM_KEY_BYTES];
+    SR.nextBytes(bytes);
+    return HexFormat.of().formatHex(bytes);
+}
 public RememberMeServicesConfig() {}
 public RememberMeServicesConfig(RememberMeServicesConfig other) {
     super(other);
-    setKey(other.getKey());
 }
+/** Returns the key that signs the remember-me cookie, from {@link #KEY_PROPERTY} or a random value. */
 public String getKey() {
-    return key;
-}
-
-public void setKey(String key) {
-    this.key = key;
+    return resolvedKey;
 }
```
The chain read the live key, so it never depended on the shipped `geoserver` value. With the key out of the data directory, a file read no longer reveals it.

## Remediation

Upgrade to GeoServer 3.0.2, 2.28.6 or 2.27.7.

The fixed releases generate a new remember-me key each time they start, so remember-me cookies stop working after a restart. If you run a cluster and need cookies to work across nodes, set the same `GEOSERVER_REMEMBERME_KEY` on each one.

If you can't upgrade straight away, GeoServer's advisories suggest blocking `service` values that contain `/` at a proxy and removing `rememberme` from the `web` filter chain. They also suggest checking `wfs/query` and `workspaces/*/wfs/query` in the data directory for stored queries you didn't create.

## Disclosure Timeline

- **August 2, 2026:** I reported the full chain to the GeoServer team through a private GitHub security advisory, and sent a revised PoC the same day.
- **August 10, 2026:** Security team acknowledged the report.
- **August 15, 2026:** I retested the chain on the official 3.0.0 release and on 3.0.1, released the day before, and it worked on both.
- **September 14, 2026:** The service-rule bypass fix ([#9922](https://github.com/geoserver/geoserver/pull/9922)) merged.
- **September 24, 2026:** The remember-me configuration fix ([#10008](https://github.com/geoserver/geoserver/pull/10008)) merged.
- **October 12, 2026:** The stored-query entity-resolver fix ([#9928](https://github.com/geoserver/geoserver/pull/9928)) merged.
- **October 13, 2026:** The entity-resolver change was backported to 3.0.x ([#10080](https://github.com/geoserver/geoserver/pull/10080)), and GeoTools merged the accompanying [GEOT-7938](https://github.com/geotools/geotools/pull/5781) redirect hardening.
- **October 15, 2026:** The [JDBC property fix](https://github.com/geoserver/geoserver/commit/1501072adf8f45809da7a52118c56e51d09ff0af) and [WFS path-disclosure fix](https://github.com/geoserver/geoserver/commit/9170959881e270434a0d2cea026ebc7bf3f35a7f) landed on 3.0.x.
- **October 17, 2026:** GeoServer 3.0.2 released with fixes for the chain.
- **October 18, 2026:** GeoServer 2.27.7 released with the same fixes.
- **October 29, 2026:** GeoServer identified the five fixes in 3.0.2, scheduled disclosure under GEOS-12273 and asked GitHub for CVEs.
- **November 2, 2026:** GeoServer 2.28.6 released with the same fixes.
- **November 7, 2026:** At the GitHub CVE team's request, GeoServer split the report into five advisories and retitled the original one to cover the remember-me key.
- **November 16, 2026:** GitHub assigned a CVE to each of the five advisories.
- **November 23, 2026:** GeoServer published all five advisories. [Quikko](https://github.com/Quikko) and [nteusink](https://github.com/nteusink) are also credited on the `x/WFS` bypass and XML injection advisories, and [McCaulay](https://github.com/McCaulay) was added as a reporter on the remember-me key advisory.

## Conclusion

Five separate vulns took an anonymous WFS request in GeoServer to command execution as the GeoServer process. I guess you could call this GeoServer2Shell 😁
