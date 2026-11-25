---
title: Sleep, Beacon, Steal, Repeat - The Story of P7 DarkSword Variant
url: https://www.iverify.com/blog/darksword-variant-threat-research
hostname: iverify.com
description: Discover P7 DarkSword, a new iOS spyware variant with improved stealth, keychain and crypto-wallet theft, and two-way C2 communication.
sitename: iVerify
date: "2026-10-08"
fingerprint: "5894dae7db35fcb"
language: en
image: https://framerusercontent.com/images/tT0VpZHJC6tetKbeH6jML3v8QJA.png?width=1024&height=576
pagetype: website
filedate: "2026-11-25"
---
[Blog](https://www.iverify.com/blog)

# Sleep, Beacon, Steal, Repeat - The Story of P7 DarkSword Variant

iVerify Threat Intelligence Team

## **Executive Summary**

In August 2026 we investigated a [DarkSword](https://www.iverify.com/blog/darksword-ios-exploit-kit-explained) infection that turned out to be a previously unseen variant, which we call P7 DarkSword. The name P7 comes from the threat actor’s use of the `p7_` variable prefix in modifications to original DarkSword’s code. Compared with the variants we usually observe, P7 reduces its on-device footprint, adds on-device keychain and crypto-wallet theft, and adds two way C2 communication with the attacker's infrastructure. This post describes the investigation, the variant's capabilities, and the indicators that can be used to detect it.

## **The Investigation**

In August 2026, we received an alert about a DarkSword infection on one of our customers' devices. The detection differed slightly from the usual DarkSword detections we observe. With the customer's consent, we began the incident response process and obtained additional forensic artifacts, which confirmed that this was an unknown DarkSword variant. Around the time of the infection, we also observed additional suspicious files being created in the `/private/var/tmp` directory. We continued the investigation to answer the customer's specific questions and to recover a spyware sample.

In parallel, we used the [Validin](https://www.validin.com/) platform to hunt for [Coruna and DarkSword variants](https://www.iverify.com/blog/proliferation-of-coruna-and-darksword) in the wild, with custom tooling to automatically fetch all exploit and implant content from the results. While the forensic investigation was still underway, we isolated this variant in the Validin results using known filesystem artifacts from the infected phone. Shortly afterward, we extracted a suspicious domain matching the suspected infection timeline; the content hosted there appeared to be a different version of the same spyware family. By analyzing this version's code, we determined that unlike many of the AI-assisted variants we have observed, its authors had invested real effort in modifying it, and their changes demonstrated competence.

## **P7 DarkSword**

P7 DarkSword improves on earlier variants in three areas:

- **Stealth.** It eliminates debug logging over HTTP requests and syslog, and reduces the number of process injections.
- **Stability.** It uses browser localStorage to prevent re-exploitation.
- **Functionality.** It extracts keychain data into JSON on the phone for exfiltration (previous DarkSword versions copied and exfiltrated the keychain database to process on the attacker's infrastructure) and supports advanced two-way C2 communication.

## **C2 Communication**

The implant is injected into the SpringBoard process, which handles all communication with the attacker's infrastructure.

| **Endpoint** | **Description** | 
| POST /beacon | Tasking poll (every 15 seconds) | 
| POST /result | Raw file exfiltration | 
| POST /a | Registration | 
| POST /event | Heartbeat | 
| POST /u | Installed applications inventory exfiltration | 
| POST /nb | Notes exfiltration | 
| POST /p | Photos exfiltration | 
| POST /war | Keychain + Wallets exfiltration | 

The core of the C2 communication is the `/beacon` request, sent every 15 seconds (the interval is configurable from the C2 via the `sleep` command). The response contains commands to execute on the victim's phone.

**Commands:**

In addition to the generic `execute_command` dispatcher, which accepts shell-style subcommands, the implant implements dedicated command handlers:

| **Command** | **Description** | 
| execute\_command | ls, dir, cat, type, pwd, cd, mkdir, md, rm, del, cp, copy, mv, move, ren, stat, chmod, touch, ln, readlink, find, head, tail, wc, grep, du, file, hexdump, whoami, id, uname, hostname, df, date, echo, ps, memdump, ifconfig, ipconfig, netstats, netstat, connections, conn, httpspy, spy, download, photos, apps, upload, file\_upload, eval, exec, js, help, ? | 
| ls | Lists directory contents. | 
| download | Reads a file from the device and uploads it to C2. | 
| photos | Walks /var/mobile/Media/DCIM and uploads photo files. | 
| apps | Enumerates app containers under /var/mobile/Containers/Data/Application and extracts bundle IDs from metadata plists. | 
| exec | Executes arbitrary JavaScript directly inside the implant runtime. | 
| file\_upload | Recursively scans one or more paths and uploads matching files. | 
| basic\_info | Collects device/system metadata and sends it to C2. | 
| disk\_scan | Recursively scans the filesystem from /, records metadata for files/directories/symlinks, writes a report, and uploads it. | 
| ios\_app\_data | Finds app sandbox and app-group containers for requested bundle IDs and uploads selected app files. | 
| wallet\_extract | Extracts wallet-related data for imToken wallet app. | 
| wallet\_scan | Scans for installed wallet apps. | 
| memo\_scan | Finds Apple Notes databases such as NoteStore.sqlite or notes.sqlite and uploads it. | 
| photo\_scan | Queries Photos.sqlite for recent photos, computes MD5 hashes, and uploads the photo files. | 
| sleep | Changes the beacon polling interval. | 
| exit | Breaks out of the beacon loop and stops the agent. | 

## **Indicators of compromise**

### **Network indicators:**

**Exploit URLs:**

- `hxxps://cdn[.]gotoiphone[.]com`
- `hxxps://mzpo30[.]cam/assets/js/group[.]html`

**C2 servers:**

- `hxxps://agdx53[.]cc`
- `hxxps://js[.]gotoiphone[.]com/ios18`

**C2 communication:**

All requests are `POST` over `HTTP/1.0` with a hardcoded User-Agent: `Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1`. Content-Type `boundary=------HqBound` for endpoint `/p` is also a hardcoded value. The attackers leverage HTTPS, but without strict certificate validation.

| **Endpoint** | **HTTP Headers** | 
| /beacon, /result, /event, /a, /u, /nb, /war | POST /beacon HTTP/1.0 Host: agdx53\[.\]cc Content-Type: application/json User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 18\_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1 Content-Length: \<json\_body\_length> | 
| /p | POST /p HTTP/1.0 Host: agdx53\[.\]cc Content-Type: multipart/form-data; boundary=------HqBound User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 18\_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1 Content-Length: \<multipart\_body\_length> | 

**sha256 hashes of exploit components:**

| **Module** | **hxxps://cdn\[.\]gotoiphone\[.\]com** | **hxxps://mzpo30\[.\]cam/assets/js/group\[.\]html** | 
| rce\_loader.js | c9f8bf92af34239f68e6be9bed945d6e9b4e2d5fc6883a501bc85e3c88a761b7 | eb6da327d5e456a594a066fda2140234ffad305fb204556477718dfce31afe81 | 
| rce\_module.js | f9b3ea20bdd1a8650d31b6053c87a1d684ff86a64212662f1850f9e67fb5521b | 92c7d246d2c163c076f783dcc19f87f5b9b9ac301b106b87a7aaea9346ce0052 | 
| rce\_module\_18.6.js | 37efaa4237a28a4be411d40de80b2935be5b8c4e6731ee1f858c609142a87445 | 37efaa4237a28a4be411d40de80b2935be5b8c4e6731ee1f858c609142a87445 | 
| rce\_module\_18.7.js | e709457ac7fc6a00a1d7940ff8c1ec5370678b4f47fd7942180517bd2f1421cb | 73fb3a5a03e630f36deb2c31b77f2e48289c90d2e840746715ebf2c5847584d4 | 
| rce\_worker\_18.4.js | 489e0e59c1a1fbe92aa692a700b32eb84b47c8f9c757fe61325c028a3a6caeef | 71fe83847cdaf8c4d6c1aca90078dc4021cb96010062279d26338f06b4a7ba06 | 
| rce\_worker\_18.5.js | 9b6ca11dcd1c6c57ef056a1f6452a38fb1c2ead452057755db37a921ac63b1be | N/A | 
| rce\_worker\_18.6.js | 7bec1ec0337c12aa49b83e40f3b7659d9d332ecbd1fd209fd1b948086ec2768c | 4df20a173ae6da2291fd66cb28a165958a9a6f5998ef9a19e4e143b120f1a844 | 
| rce\_worker\_18.7.js | N/A | 77238255f541274ed0c8c1e5e0ffe034532a210a3aaba94d63a05a3499362022 | 
| sbx0\_main\_18.4.js | 49a279c21493e24fcd5c6ce6d898e194a7252da5851e8ff7b7715b97137861fe | a5ca944459c08038bfabf7ddbfc6ec2505ef0dc22b987569ed295f7378f30d59 | 
| sbx1\_main.js | f97aa214f10ede8c93acaae0bd975d945fda3fdb8a98af2977ca168467bdf214 | c1b05dd8e7d060d2a40a859211528e90e62d0dc378f8af831933fe59122490dd | 
| pe\_worker.js | e7d3a07164d26f31e6305639119942d5ae26a7056c2fc86441ecd6b5ae9e17b6 | 30286dc1fe4ecee65c890a4f2058cc01d2c7c55298cd7a078425e50ae2053579 | 

**sha256 hashes of extracted implant components:**

| **Module** | **hxxps://cdn\[.\]gotoiphone\[.\]com** | **hxxps://mzpo30\[.\]cam/assets/js/group\[.\]html** | 
| c2\_agent.js | c6587d10462c81c66c0798378710f492c7725a91d86c8e541cf66211bff4abff | 46a3234bf6589e73e1a6d52ce5979e3149ccaa2af7202228fd907b807cc4debc | 
| keychain\_copier.js | 47c2d77f0b15b9f2b237ba534e6dd4392f57d3c75a16fea2dc1b7fa25d312794 | f0f0aa82a03bf4835864a5b7f7ba38e537f3f81e82b3db311ac0d80b4b4b022e | 
| free\_thread.js | 56ac6331f874118692dc8a1250a31c0340a5642adad8a431b33ba1d9c2865afb | 56ac6331f874118692dc8a1250a31c0340a5642adad8a431b33ba1d9c2865afb | 
| loader.js | 225377bb96b9ec642042d6e6379d3ac908edd08dc5dca6df7ac5f68d407b6e16 | d554f534fad7822cbde9ca7d9f6efe8a7e0f5786ccee60f8db6dad340a2a6f80 | 
| MigFilterBypassThread.js | 48aacf46ad8b7f619d7f4346c330abfbda14a34ed3eb98c215a5ef5fb36e2171 | 48aacf46ad8b7f619d7f4346c330abfbda14a34ed3eb98c215a5ef5fb36e2171 | 

### **On-device indicators**

**Browser localStorage:**

| **URL** | **localStorage variables** | 
| cdn\[.\]gotoiphone\[.\]com | lab\_device\_uuid | 
| \_\_ds\_inflight\_worker |  | 
| \_\_ds\_inflight\_ts |  | 
| \_*ds\_crash\_count*\<worker> |  | 
| \_\_ds\_skip\_workers |  | 
| \_*ds\_crash\_mid*\<worker> |  | 
| mzpo30\[.\]cam | \_x\_pe\_done | 
| \_x\_try |  | 
| \_x\_try\_ts |  | 
| \_x\_ok |  | 

**Unique file system artifacts:**

| **File Path** | **Description** | 
| /private/var/tmp/keychain\_c2\_dump.json.tmp | In-progress keychain dump | 
| /private/var/tmp/keychain\_c2\_dump.json | Final keychain dump | 
| /private/var/tmp/keychain\_c2\_dump.done | 4-byte marker file ("done") signaling dump readiness to c2\_agent | 
| /private/var/tmp/p7\_debug.log | Debug/progress journal of the spyware's "P7" keychain-theft phase. | 
| /private/var/tmp/c2\_wallet\_debug.log | Debug trace of the keychain-decryption pipeline | 
| /private/var/tmp/\_hq\_notestore | Copy of victim’s Apple Notes (/private/var/mobile/Containers/Shared/AppGroup/\<UUID>/NoteStore.sqlite) database. | 
| /private/var/tmp/\_hq\_notestore-wal | Copy of victim’s Apple Notes (/private/var/mobile/Containers/Shared/AppGroup/\<UUID>/NoteStore.sqlite-wal) database. | 
| /private/var/tmp/\_hq\_notestore-shm | Copy of victim’s Apple Notes (/private/var/mobile/Containers/Shared/AppGroup/\<UUID>/NoteStore.sqlite-shm) database. | 
| /var/mobile/Library/Caches/ios\_disk\_scan.txt /var/mobile/ios\_disk\_scan.txt | Output of the disk\_scan handler. Uploaded in chunks, then unlinked. | 
| /private/var/tmp/notes.sqlite | Copy of Apple Notes SQLite database from /private/var/mobile/Library/Notes/notes.sqlite | 
| /private/var/tmp/notes.sqlite-wal | Copy of Apple Notes SQLite database from /private/var/mobile/Library/Notes/notes.sqlite-wal | 
| /private/var/tmp/notes.sqlite-shm | Copy of Apple Notes SQLite database from /private/var/mobile/Library/Notes/notes.sqlite-shm | 

## **Conclusion**

P7 DarkSword shows that DarkSword operators are actively iterating on the implant. Unlike the many AI-assisted variants we observe, the P7 authors understood the code they were modifying: their changes reduced the implant's footprint while extending its theft capabilities. Incident response processes and forensic investigation for partial or heuristic detections can result in new discoveries and improved detection.

Please find indicators of compromise for other Coruna and DarkSword variants below:

### DarkSword Domains (iframe host : darksword host) - self means same origin

| https://1\[.\]482319\[.\]xyz:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://1\[.\]517413\[.\]xyz:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://1\[.\]604446\[.\]xyz:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| http://103\[.\]193\[.\]173\[.\]41:8888 : (self) | 
| https://103\[.\]200\[.\]125\[.\]188:443 : (self) | 
| http://103\[.\]200\[.\]125\[.\]188:80 : (self) | 
| http://103\[.\]226\[.\]155\[.\]200:8000 : (self) | 
| http://103\[.\]226\[.\]155\[.\]201:8000 : (self) | 
| http://103\[.\]39\[.\]79\[.\]232:8080 : (self) | 
| http://103\[.\]73\[.\]160\[.\]115:8090 : (self) | 
| https://149\[.\]88\[.\]67\[.\]47:443 : (self) | 
| http://152\[.\]53\[.\]169\[.\]187:8888 : (self) | 
| http://156\[.\]245\[.\]145\[.\]11:8888 : (self) | 
| https://156\[.\]252\[.\]63\[.\]106:443 : (self) | 
| https://156\[.\]252\[.\]63\[.\]107:443 : (self) | 
| https://156\[.\]252\[.\]63\[.\]108:443 : (self) | 
| https://156\[.\]252\[.\]63\[.\]110:443 : (self) | 
| http://16\[.\]59\[.\]214\[.\]49:8080 : (self) | 
| https://162\[.\]4\[.\]136\[.\]30:443 : (self) | 
| https://177\[.\]2\[.\]184\[.\]26:443 : (self) | 
| https://178\[.\]landexuan\[.\]site:443 : (self) | 
| http://178\[.\]landexuan\[.\]site:80 : (self) | 
| https://18\[.\]118\[.\]213\[.\]237:443 : (self) | 
| http://18\[.\]118\[.\]213\[.\]237:8080 : (self) | 
| https://18\[.\]ushop168\[.\]cc:443 : (self) | 
| https://192\[.\]253\[.\]229\[.\]191:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| http://194\[.\]59\[.\]30\[.\]222:8000 : https://ad-track\[.\]live | 
| http://2\[.\]26\[.\]22\[.\]89:81 : (self) | 
| https://202\[.\]146\[.\]222\[.\]253:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://202\[.\]8\[.\]120\[.\]249:443 : (self) | 
| http://202\[.\]8\[.\]120\[.\]249:8000 : (self) | 
| https://38\[.\]190\[.\]250\[.\]151:443 : (self) | 
| http://38\[.\]22\[.\]89\[.\]117:80 : (self) | 
| http://38\[.\]55\[.\]193\[.\]43:80 : (self) | 
| http://39\[.\]104\[.\]56\[.\]125:80 : (self) | 
| http://3z4\[.\]xyz:80 : (self) | 
| https://45\[.\]207\[.\]210\[.\]78:443 : https://mollquest\[.\]top | 
| https://47\[.\]129\[.\]224\[.\]84:443 : (self) | 
| http://47\[.\]74\[.\]61\[.\]39:80 : (self) | 
| https://47\[.\]80\[.\]242\[.\]98:443 : (self) | 
| https://5\[.\]zalandoweb\[.\]com:443 : (self) | 
| https://51\[.\]91\[.\]100\[.\]96:443 : (self) | 
| https://64\[.\]81\[.\]30\[.\]49:443 : (self) | 
| http://66\[.\]154\[.\]103\[.\]112:8080 : (self) | 
| http://8\[.\]209\[.\]248\[.\]215:80 : (self) | 
| https://8r03l\[.\]com:443 : (self) | 
| http://91\[.\]208\[.\]122\[.\]42:8080 : (self) | 
| http://93\[.\]152\[.\]221\[.\]37:8080 : (self) | 
| https://96\[.\]ip-51-91-100\[.\]eu:443 : (self) | 
| https://a\[.\]buffbuff\[.\]cam:443 : (self) | 
| https://a01\[.\]ai-poolion\[.\]cc:443 : (self) | 
| https://admin\[.\]catcoinglobal\[.\]top:443 : (self) | 
| https://admin\[.\]hbwney\[.\]com:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://af\[.\]sdfg54dsf8gdfg\[.\]com:443 : (self) | 
| https://agent\[.\]catcoinglobal\[.\]top:443 : (self) | 
| https://ai-poolion\[.\]cc:443 : (self) | 
| https://asajkdjkxsiasdjaguge\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://aswdczayiwaiwi\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://asxcdskdwedgugefy\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://bookpan\[.\]net:443 : (self) | 
| http://bookpan\[.\]net:80 : (self) | 
| https://bostaiwanline\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://bsadxgugefy\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://bsasdxdaqguge\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://bsdaxguge\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://bsoozasyoudao\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://bssdazguge\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://c1\[.\]8r03l\[.\]com:443 : (self) | 
| https://c2\[.\]ios\[.\]catcoinglobal\[.\]top:443 : (self) | 
| https://c2\[.\]shopreviewt\[.\]top:443 : (self) | 
| http://c2\[.\]shopreviewt\[.\]top:80 : (self) | 
| https://cadsacdsguge02\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://caibaoh\[.\]com:443 : (self) | 
| https://cdn\[.\]gotoiphone\[.\]com:443 : (self) | 
| http://cdn\[.\]gotoiphone\[.\]com:80 : (self) | 
| https://cdngoogle\[.\]vip:443 : (self) | 
| https://cdngsnsaassefgagugefanyi\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://cgwin\[.\]bet:443 : https://nuih22\[.\]cc | 
| https://cgwin\[.\]com:443 : https://nuih22\[.\]cc | 
| https://cgwin\[.\]game:443 : https://nuih22\[.\]cc | 
| https://cgwin\[.\]io:443 : https://nuih22\[.\]cc | 
| https://cgwin06\[.\]com:443 : https://nuih22\[.\]cc | 
| https://cgwin1\[.\]com:443 : https://nuih22\[.\]cc | 
| https://cgwin2\[.\]com:443 : https://nuih22\[.\]cc | 
| https://cgwin3\[.\]com:443 : https://nuih22\[.\]cc | 
| https://cgwin7\[.\]vip:443 : https://nuih22\[.\]cc | 
| https://cgwinclub\[.\]com:443 : https://nuih22\[.\]cc | 
| https://cgwinplay\[.\]com:443 : https://nuih22\[.\]cc | 
| https://cgwinvip\[.\]com:443 : https://nuih22\[.\]cc | 
| https://cj\[.\]catcoinglobal\[.\]top:443 : (self) | 
| https://colorbytedance\[.\]qzz\[.\]io:443 : https://mollquest\[.\]top | 
| https://daasxzdwqaguge01\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://darksword\[.\]bitbrowserpro\[.\]com:443 : (self) | 
| https://darksword\[.\]botiq\[.\]site:443 : (self) | 
| http://darksword\[.\]botiq\[.\]site:80 : (self) | 
| http://darksword\[.\]trxkk\[.\]com:80 : (self) | 
| https://dermatologie-klinik\[.\]st2\[.\]al:443 : (self) | 
| https://df45gdf48g\[.\]com:443 : (self) | 
| https://disnasaskdjaxksjgg01\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://dominonew\[.\]onaylarim\[.\]com:443 : (self) | 
| https://ds\[.\]hxdgcx\[.\]online:443 : (self) | 
| https://dsaxsaddfanyi\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://dsw\[.\]webtest\[.\]eu\[.\]cc:443 : (self) | 
| https://dsxaszxleidian\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://ggcheonegoovnfgg\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://hbwney\[.\]com:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://hi-metaverse\[.\]online:443 : (self) | 
| https://i1\[.\]9kym\[.\]com:443 : (self) | 
| http://i1\[.\]9kym\[.\]com:80 : (self) | 
| https://ios\[.\]buqiu\[.\]site:443 : (self) | 
| http://ios\[.\]buqiu\[.\]site:80 : (self) | 
| https://ios\[.\]eseu\[.\]top:443 : (self) | 
| http://ios\[.\]eseu\[.\]top:80 : (self) | 
| https://ios\[.\]vdvd2026\[.\]com:443 : (self) | 
| http://ios\[.\]vdvd2026\[.\]com:80 : (self) | 
| https://ios\[.\]vocc\[.\]top:443 : (self) | 
| https://ios26\[.\]crowdsec\[.\]site:443 : (self) | 
| http://ios26\[.\]crowdsec\[.\]site:80 : (self) | 
| https://ios33\[.\]crowdsec\[.\]site:443 : (self) | 
| http://ios33\[.\]crowdsec\[.\]site:80 : (self) | 
| https://ioscx\[.\]wanyebao\[.\]cn:443 : (self) | 
| https://kajskdwekdxchsdgugefy02\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://km\[.\]8r03l\[.\]com:443 : (self) | 
| https://lbbsedxyifanyi\[.\]icu:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://lbbsedxyiwaiwai\[.\]icu:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://lbbssougoushurufa\[.\]icu:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://lbbsxdmeituxiu\[.\]icu:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://lbbsxdsougouliulanqi\[.\]icu:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://lbbsxwangyiyun\[.\]icu:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://lbbzadcfssdxxtg\[.\]icu:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://likeshare\[.\]shop:443 : (self) | 
| https://m\[.\]catcoinglobal\[.\]top:443 : (self) | 
| https://maomao7\[.\]com:443 : https://nuih22\[.\]cc | 
| https://mollquest\[.\]top:443 : (self) | 
| http://mollquest\[.\]top:80 : (self) | 
| https://ngjhgghdsftujfdshdhsguge\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://noor-alaziz\[.\]online:443 : (self) | 
| https://qaswedcameitu01\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qazxswdguge02\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qishuicisnyinyueyin\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qishuifeiqishuiyinyue\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qishuigoyintye\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qishuiwushyinshx\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qishuyinyuezhuhz\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmasedfxleidian\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmasxwedmeitu\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmazsdqatd\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmbsaasdzaqishui\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmbsadxdyiwaiwai\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmbszasdqyoudao\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmdadxiangrikui\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmqxzasqishui\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmsdazsliuguge03\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmsdsaaguge\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmswedyoudao\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmswsdayiwaiwai\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmyinyueaaqishui\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmyinyueqishui\[.\]icu:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmyxdfsyoudao\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://qmzsxdmeitu\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://rr\[.\]hbwney\[.\]com:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://sadsxsayiwaiwai\[.\]icu:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://samsdqafeiji\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://sansdesougou\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://saswsasyifanyi\[.\]icu:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://sdfaswasleidian01\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://sdxcsdeaguge\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://sdxfdabiteliuanqi\[.\]icu:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://sdyineng\[.\]net:443 : (self) | 
| http://sdyineng\[.\]net:80 : (self) | 
| https://sex\[.\]dwelling\[.\]eu\[.\]cc:443 : https://nuih22\[.\]cc | 
| https://ssdjskdcasdjafdfkgugellq01\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://sufiok\[.\]work:443 : (self) | 
| https://supachok-lazycat\[.\]pages\[.\]dev:443 : https://supachok\[.\]thelazycat\[.\]dpdns\[.\]org | 
| https://supachok\[.\]thelazycat\[.\]dpdns\[.\]org:443 : (self) | 
| https://svz6\[.\]xyz:443 : (self) | 
| https://t3ios\[.\]com:443 : (self) | 
| https://te1egsdxinn\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://te1eguuxsnrnn\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| http://test\[.\]ipqqq\[.\]com:80 : (self) | 
| https://tt\[.\]8s\[.\]lv:443 : (self) | 
| http://upswingcrmsucks\[.\]com:80 : (self) | 
| https://v1\[.\]io92jujjs33\[.\]com:443 : (self) | 
| https://wassksdyiwaiwai01\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://web3a\[.\]cc:443 : (self) | 
| http://web3a\[.\]cc:80 : (self) | 
| https://wsadaxiangrikui\[.\]icu:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://wsasaklsdkjasgugeliulan\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://wuyexufanyi\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://wuyexuleidian\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://wuyexumeitu\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://wuyexuqishui\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://wuyexuxiangrikui\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://wuyexuyiwaiwai\[.\]top:443 | 
| https://wuyexuyoudao\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://wuyqxuguge\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://www\[.\]ai-poolion\[.\]cc:443 : https://a01\[.\]ai-poolion\[.\]cc | 
| https://www\[.\]catcoinglobal\[.\]top:443 : (self) | 
| https://www\[.\]dermatologie-klinik\[.\]st2\[.\]al:443 : https://dermatologie-klinik\[.\]st2\[.\]al | 
| https://www\[.\]ffethy\[.\]work:443 : (self) | 
| https://www\[.\]global-orions\[.\]com:443 : (self) | 
| https://www\[.\]hbwney\[.\]com:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://www\[.\]hi-metaverse\[.\]online:443 : (self) | 
| https://www\[.\]luttyd\[.\]work:443 : (self) | 
| https://www\[.\]noor-alaziz\[.\]online:443 : (self) | 
| https://www\[.\]sufiok\[.\]work:443 : (self) | 
| https://xmkeji\[.\]vip:443 : https://cdnbing\[.\]vip, https://cdngoogle\[.\]vip | 
| https://xp2026nb\[.\]xyz:443 : (self) | 
| https://xp2026nb01\[.\]xyz:443 : (self) | 
| https://xsadcasyiwaiwai\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://xsaindazguge1\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://xsazqdfaafeiji\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://xsdianzqmguge\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://xsjazscedguge03\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://xskjaaisdkajsxcgugefy\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://xslaksdjkalkssdguge11\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://xsskjhjawsdjhfggfanyi\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://y1waixinneutwai\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://yibncwaixwewai\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://yifanfanyifan\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://yifanytenyi\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://yifyuanytai\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://yixue\[.\]linqingkeji\[.\]com:443 : (self) | 
| http://yixue\[.\]linqingkeji\[.\]com:80 : (self) | 
| https://yiygdfanwesyi\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://yiyuxxfanyi\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://ytzsadguge1\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://yxpf8899\[.\]vip:443 : https://cdnbing\[.\]vip, https://cdngoogle\[.\]vip | 
| https://yyifanyifanyi\[.\]top:443 : https://cf\[.\]r5dz2dz88wuideu\[.\]xyz | 
| https://zhifu\[.\]tronide\[.\]cc:443 : (self) | 
| https://zyydif\[.\]work:443 : (self) | 

### DarkSword hashes - rce\_loader.js

| 03ca87f29b5c32267bf0fdce031be47085af319379aa1780814ba3d495a7851c | 

| 04e2ad33dd5211b0525ff663bc20b006b450684475522c452531c57426f09e73 | 
| 0a9b3ac11e9f69a6d945839e31d432709213168f3702367578d009550b6054ac | 
| 0e2635c9d4b14cf38a6144b4a014a030a0fffe3477319aa74ed15a76e2d4b19f | 
| 0e536bb4bd693dc0eea9b29e632d193c57f99d94bc386e6530227a5edb3a6b51 | 
| 109b260ecb41aecbcfbf9554d592f7f5b1ead6ba564136925e3f4f578e17431f | 
| 132297876d91ebde254116331ecb9f33ce176fee8e8628c9b708b3940bbfb8cc | 
| 14102d8ef79ce81c7b5338ff214ccce8e03d171507b5194581d2f6248e77640e | 
| 1924a6b62d18e5e8f38aacca685907596464c39f6b8b807f983452b049f38d30 | 
| 1b37e227cd3a86c9a32833a0e8cf5b12282e4bb67cd8a19b123d69bb46cc8ceb | 
| 1e453a7a7a828fff78d4051c4d9759cd46849705ee6d0f1977f6a6ec3c0cbac1 | 
| 21edb01800823dc9930558738b250d7c8811b7a7d2f660cbca181c16be41881e | 
| 2504cf3053bc52b57de0bfeb2f3e4cc47bb0ffbbf051e8e4a1c81b0c507af9bf | 
| 2a71a53198bc2762cd7fc9bec20c56e06bf5d8d37646c57c53cd45da9ad0d786 | 
| 2cd312b6017456d172376d7fc68ddd8fc3a6e56b8c2be7608c63fd5ddfc66f15 | 
| 2f5f28607b58f03fe9bf0d2c92c89bfd28dda723b5adc4af45ff7224bc4ad555 | 
| 36c4eb8e9c7662952da3dae3e91a60e512c23c2ee78a79c5e7e5ab3fc7ea10e7 | 
| 43f3712ca8b3ccebee8701b330ddace47e9b94bbf018ef4afaf92a86bb5a795c | 
| 4bfcb14b617eb59173e9c99973264187a1c99ac2e34cff03a9dbf5ac5669ee63 | 
| 51c97bb87fd20f3eb499b4b2b58fdfe611cfb96c4d9bca69d58ea6c97af6cd90 | 
| 5244d2b9f9c7ed10cde43aab3eb1d3c270139c0f559a01fdb46fc7a764daeac1 | 
| 55dd762cb8b89ca64a8944e5087e494bbd9d756206f68cb80200c2ffd6d9a628 | 
| 574896bf6cc42fe0f67611195320847a688f3684e3cbdf514b8a9112de9fafd2 | 
| 594943dcdff3604d1c88028c8360f5ddb2f45ab39bc8cda84c2573cf1eae44a7 | 
| 636a3ec6d4549d6d27476087f661496a9b0acb8a98d82913e863c0397d44dfda | 
| 662039e299dfd553fcd933c493bb2364b387169bae0cc026e7c32e7fc2649735 | 
| 6b4f2a3dc2fc72c3851373479070ff5b8c2864c9868bf97cea36c152a0a68778 | 
| 6dca9cbe1df8b2cb8a56cb22be824d8e95117861cbb42ead3eca76cefb95ecbc | 
| 6f712f1d75c009417de2d71b55d6111c2637f59d86bb5b864b5b19528e763463 | 
| 71945cd309bc38e9de229f419e5680bd6186711e3ec7d6364944ac32e6fa8389 | 
| 725caf3bd2cad20d10aaea8bacf2f0b1f88f27f3b9cb999cf8ed5f85af939d54 | 
| 83adb97a2f1c56e390966fc00993eaf8545832dd5209b58e7aa6ec8d815a11cc | 
| 986818b96a595c1a2ba78eaad68614b33a050aafbfb3269345200acb570f1f85 | 
| 9d9268c3826d262d5184c55e913b324d533eba85d710240ab43e4bfe04f82010 | 
| 9da02faaad63081d431beed4184f2eb0e18abbba6c698b404bb56fa4705c00fa | 
| a7f2006941914a4a657c800d83f31a7a3a4696ee433794b24dd227de12413f54 | 
| b3b14a34e5618a96f8b9ab3c6de454cea261a5d8bf81d4f9a9d3ff56d8c7d87d | 
| b43a113fbb34f1f5af550ae5a5aad6e0b280241b33751693cce84e231cd0e70d | 
| b8f760e17f18f50468e46b6cdadb97498dbd17f5450d346983233bdfd28e0416 | 
| c7785e65d6d239d70be029acdfa377dcdd05f172fa523ead058a94d159eb4e3b | 
| c9f8bf92af34239f68e6be9bed945d6e9b4e2d5fc6883a501bc85e3c88a761b7 | 
| cad515acfb300dfe0f3477b16e816a371c256ebfb8b8ba2f4692194cf66b5ca4 | 
| d1f6fd7cc61502264869198e95ffb5a73f2cff693a2b6e94fac7390da8aad148 | 
| e9790dd41cf88b59b331f8e06204aea358ff8dfe198fc3db1a3f453831b112c5 | 
| eb6da327d5e456a594a066fda2140234ffad305fb204556477718dfce31afe81 | 
| f371a009e780d4a1a50922302e9e326f1a365a995363e389cb2d5651726bb15a | 
| f8d196b3ac1859ef427abf7a3e261a7899e9a9d8231b2d94b8f24cf6f962a1d9 | 
| fc03ef357b3b35abf357d983f15cce0a1aef726decdc71d40383142d216be68c | 
| ffa051e9a1739176acddd4e2f9c9dde933a6cf219c218c8cc3bf83051c4cb071 | 

### RCE Module

| 057dce1e1889ba092eea71c1bdb0ac5530587a781fe6baa7efe6eaf78f997d33 | 
| 13447e5d8f626f90605df56714cc16e761abc8e546a08957896f37e4c45779ca | 
| 2a5f5ad08018a86cef9938a398092840a5a9a5a92411c8d48f04bc26cd416d4c | 
| 3221be2e8c5d8377e46713db33766ff53f03248eace4e1a8175f1961eded1c57 | 
| 3de32b8c7e659b609ac69d4d3391b12f722e06ea84c2786e7883ed524ba5ebcc | 
| 48e8e864aecb0f1af3af68327bbbcac89ef4cf075730cabd519386ca93b29bd5 | 
| 57a1b12d7462635d83ce071b9d350e4324e89be1a72bb9b66493ba4694621932 | 
| 65b281b35d6e1cbb8f16d590eb87e28875e04fad0d5fe0fa7ac65537279d13b8 | 
| 6e82f1087c6c82ad4eec88e4212ce12d10a408ec48d0abc276e65cc9ee227083 | 
| 70a0aa9032eddb4d90085a0cb39041f39b39e15a5c1392167dbb2353caa87c68 | 
| 8e18a00caa8baca83ff2cc0e7041c4b8f88207ae4336fe8b846af12109b2a47e | 
| 92c7d246d2c163c076f783dcc19f87f5b9b9ac301b106b87a7aaea9346ce0052 | 
| a881baa07ad364438738c1891efe2e1c8917683e95a74b71352f1ee3d7b143f1 | 
| b632bd0dafd94829f2fdd7c7bfacf16f5ff6ef7356348515f0a5cf6b2de0f1c1 | 
| be484f619c473caf4529c1ec4416b7366471cf59abf40474432ff9f991ff0578 | 
| c8c93227acc75447cc7d35044c01573a2d9c004c548e68a4edfc48273a3c71b1 | 
| dde31918e1c7d51f24b85b4fe67460f50f56d17b34fd286a5df5e060b2b48c03 | 
| f5c5550685cecdc50c051efb75ae3a4ee55aaa44ec591c6764797c7975c36b22 | 
| f9b3ea20bdd1a8650d31b6053c87a1d684ff86a64212662f1850f9e67fb5521b | 

### RCE Worker 18.4

| 0651e729ed4abe55afa0359c5f625c98fcd63aee4d32b8d2ba81c866c38d817d | 
| 06d6b1321627c5b2105a0e128c264c3ccba336076498a09f45cb4769d5cb3a26 | 
| 0b207a6d221a711003060c56bcc32bb0fd597ebcb0c60b087fa7fb290c40e0cd | 
| 148172bedf3a6f107850ebf620c69e8f50c226b186916a3e2be314f39a3e1fa3 | 
| 1adbba274192cc0656e6aef03cbbd57c98de718a18a425ae386461eeab8eea8b | 
| 1fd368be2bbc4b6be9384c02916b58edd701c6aae2a916531805bd1364a932f9 | 
| 258ad04ea0447217969dc708464eaf2c63e31d29958435f4a737f57a2c412b8a | 
| 411498193e55135c1fb0f194d9bcd4658fe2bf39d0354550160517ff3a16932c | 
| 489e0e59c1a1fbe92aa692a700b32eb84b47c8f9c757fe61325c028a3a6caeef | 
| 520faab07af79537c2c5e8f98685cccd2d773efc6364cf45989f664e017f2078 | 
| 5250bc484832d2f8d8186a424a1e3e04cd7b1172e50b391ce6adb5212840948f | 
| 53f19ab227ad7b68636aa6c4e9f0a23aaadc89c1229af1d4be5ea98c830485d3 | 
| 63046cc3c0eef94bc5b9f1813c356e62572aebb847b90a6b831d5b5f47bf0520 | 
| 6ee459565b4d856b56a450646a4fc38c8a9865ea88f253dad4e692dc39a553d0 | 
| 71fe83847cdaf8c4d6c1aca90078dc4021cb96010062279d26338f06b4a7ba06 | 
| 7dcbefd115c6fa73a51cf411cecb793bc99aaccc332de57437a6cde62d3870c3 | 
| b2b35ee5138a0978c7c88952bc2c6ae141edc213e4be957c94a5180284660558 | 
| bdbd61aa7be2945bcd657a1c6f9f84b6d26cf2c044eb84103bb48c1b356e084f | 
| c68a3612e326dac1f866c348451da717fecc16bb9924e5f4e4bf643fc137a3b8 | 
| d2347b2bcac168731176b49a9e4f0b71a27c1e13a3c4570feb8be67002e19f06 | 
| df123c0e20c6f2dbe21595d8ddf08fc5eef8607aaf4f10c86e80b84a7d0c846b | 
| ea5a65a285afd7e9c04f5b3da6f662fb1252d4a120bbaed1d126116ca61742bc | 
| f2798a29540c85e73f5c6e98cfd25438c54601eba1ff23a2271cfe9ea9087e02 | 

### RCE Worker 18.6

| 0a408f48180d451a2113a8e95eb5604a3dfe55508f39b609b5e2fbe107475cae | 
| 0d5e58d8c1be525e85d4b6fc5c11fa80c4c3f46ae2297a63914d477cdfa248a7 | 
| 1d5328a228b0f8d083ad93104b062f54ea49caca1e8ad0022f44954bf4f4d26e | 
| 2a0281f2e5a6cfbcfd6ce26a8b37a676f8d2b8c6982559a30c543db58f58803b | 
| 2fd1193d84336332309379c654bf9051c417ee015338a50890a326bc1e342157 | 
| 342bd8354054fb620cffa347bebb193e5b0e5b058274bea88a7df53917d3582d | 
| 423395277fc9bbb71ffbc91e30fb40c62776687a5eaef0631999021bcebbcb5d | 
| 498397ef45ba336b7c2193f0824bf707700453e25b5d78d6bb2edc1b5500dee7 | 
| 4df20a173ae6da2291fd66cb28a165958a9a6f5998ef9a19e4e143b120f1a844 | 
| 4eb2ee9f493f8537ac2b6b32ab7db86c159d4dd176b70ca51498b5d52ee0bfd6 | 
| 53bdeb41c5db4782f17478701526bd71799215287c309e88e381acbf6ce46374 | 
| 6f2b565e876105358d2d146dac3ae1f08e36fea92b9dfd7564d3731bfce45777 | 
| 72d184a998c8f96acbeee45be60b219bc7c6152237d3847f312e980720769402 | 
| 79948aa4c697ed82719ea8d938e6d4eca299206225ff66ae2ec6065697ce80e0 | 
| 7a0013a5f95ca3b0d6cfa5becf22ca07664674957f8f50d752544091cf9e0904 | 
| 7bec1ec0337c12aa49b83e40f3b7659d9d332ecbd1fd209fd1b948086ec2768c | 
| 7c6c3e8dfdb0c865cc762db4caa1ef450428c4259f8cc46169c861856e950e26 | 
| 8ae6236093053615aa394505584fa70ed5a2c87adc83c8731209f7f6ec3c0945 | 
| 900a2153f3b21cd70fdb3ab543c78ee169645c9196b39e740ca944992d8ffec6 | 
| 9032afdb1be64833f65cd59decbc1f98f3db2e23288dd9786dd0c52bf0345f2d | 
| afa3f3feda4b91410c8b05fe210ebd42650f6f075c56140babd06028ed7fd562 | 
| b6ec9b8d4bcd2816e6f0bb5c619ba0d4b4b04b2a0109bab2de6e096cd6dcad46 | 
| b8d70b81fe64191b0c6451be52972c32dad5735487f4f994b4bb11175178f9c5 | 
| be98ac3f82f4080ea8ac7afe653e624b92f175636ddc45bc7e582df2bb0d8eb3 | 
| c901228c1723fa0684c5f462ec3a8944ddb61e53f868d631ba8ed52a6f6e8250 | 
| cb26e2d9612d1564de84a9f0f159ff456355250dfe115962b522881f07021622 | 
| e059cd4188acb797557d164f72f2c5091920b21442cb2e75625ff8c1df07c3e3 | 
| e5ff1c98683fca9a992dd18d95e14798ac8604dcfe1776f727cd04e08f4a3870 | 
| e92ea424081c6acb48842a33d8261ac681cdf186022b0ba2ffac89d3bd463317 | 
| f06ad320ef7b3ab295fe0531f798896354d2949ddfd9cc20d9b16e0835b70835 | 
| f2798a29540c85e73f5c6e98cfd25438c54601eba1ff23a2271cfe9ea9087e02 | 
| f314e686c099ef3a1e9dd54b84f06efb3de1b5333275c18f48e8299abe1a5e79 | 

### Sbx0\_main\_18.4

| 0b225dca8e95026fa86d91fd8d3fee5a0eca0748bda469b72189f9cddba66577 | 
| 7a90b749a92d9d64fcbe388748d6255640ea504c8bb4b42c7c6aab4498f04aeb | 
| c346c484763d2665f6b48ad6dccc2b5d44fa140206571c420209c82d1db20616 | 
| eeca1b204641c89db19179444aa36c5fbe5850a3a8624a0a75df37efb736a478 | 

### Sbx1\_main.js

| 820da54789dbab454b11e3869796e5242135975952404e994d73928d0b219224 | 
| 8a19edd7aaf6f062640b04287395183a46166f6c7eba0db36a55cbb0715ee004 | 
| 91b54a084cbadef88134bc53bf5dfa630e94e64abb6811d1b10a936815f80524 | 
| 9b8d047ad14c882b34786b3625a286f470f754208f9a741978e383d0dbe4d5fc | 
| d7f6139ab6770f896849b80964fc36bde64631b0826a5dfb8f245bf973bfca1a | 

### Pe\_main.js

| 02c5caad6c3de465cf786feff6b66c351f407ee5c2b3e51071e1d6f441f5f69e | 
| 02fe8debdfe60ce3b7e7d923dc1fb2fbb5bd2741a55de06e52c63065902eed2f | 
| 06a146ec12fe6b3132ef2846e33822d10f50deab177943c0b33d090dccf3c7b6 | 
| 0f7e999aeea7def93529ea440000b246af25f1760cfb78c494ff337f8e12c14e | 
| 11f95db767706c4c5a62e2a7610cbfe8414c554545a1bdbd6eab2eb24baf6ae3 | 
| 211cce7e068182197dddd13b875e4a79464da586221fe28039c4497d725fb493 | 
| 2240e5e66a2a762323fdcf9a312250ee1f324068afb255d2c1c0e8c331789615 | 
| 2a57da5725714280af2298e403689d741a56b97aaef5448a120219ba089106ce | 
| 331fbf8ca3493265a4aeb5688f484f9d19689faac65661ffc6fcbc25bd413452 | 
| 360176f060b95979314927dd2ff2be50288a7b155dc97055f4f4d25022e66f08 | 
| 375a6e6108dcd232b5962b66a1fff6d68d06d87ec04f7eb53369caccca69ca25 | 
| 384dd53321cbc7802d720a8ff1451da201f55e80fedb6aa397c000999a141c12 | 
| 398613c137334b01ef3501964f149c7bc0a9084f466d6855e70f8b1fae2aebe0 | 
| 4493e2d716236df7a5eaad2bff5d6eb2b955aeea8351d9ddb804bece8c9e1dbc | 
| 49c3194d628c27c10fd100a44ca90d3bb3566bad0012616bf9b618b758b9ca4a | 
| 4d2f99d413618ffb8e4c4667629632d8820344aaba7bf4b766ddae061b677dbd | 
| 4e8306898b117326d21f8fcaa4c2902e59ea0455a2948976b62b38c80b12c24e | 
| 56ebe30d532391aa4cf53bdc5b561ce20c2f2985981d5f74cf47050255abe838 | 
| 6689305dd5f78f2645bddd77b98618222840b1c28ad65600cddff62422a16120 | 
| 6c03d7783997bd1d58b9e365295f5bdedef618e9a9ffaf0e7bf1ce2cfbb055ba | 
| 758728d95794e249564d7e43944a79a7d624aa6f129e4c6f554bbceb7a34f3ce | 
| 767b751cba0328d48107792f8b4ca0c00a0464e7fb9f6930050c8a41c36cd237 | 
| 77d1c507afc69f81f627c67baa3093d8840ef22e8a06c955ae35ea3cc0306c1b | 
| 8a2ff35934685c368ee8a559c00f3d2b96c63d9f1692a292bbb3b167e4afac80 | 
| 9ca53528ee7ded91e5798d8546711de8adc8f57850accdab6fbeff2b54a5c796 | 
| 9f7bca7383fa3fb4d85cffc6eee075910b25725f2db392a5dcf6983684ceba4b | 
| adaea69b65a1e00ef88c5eeaa835e524d6a072cebf153dc4eb5f5d8302a95418 | 
| b9a8e6185f9a8f1bba318b40ffa1c94073c78756352505244cf39375af049d15 | 
| bda8e802b581d2360aff3443dd39acef4675a2345e67ef0c3bd535557a7a6362 | 
| c15359210c9922f0020503b97eb2f457e6d3959af551590c25de03e415168931 | 
| d42ba9d9d648fefc0cc39ac9df5059726d7ee8f4616455febbbb470a17306ea4 | 
| d4bb6a913776be02454b6a1ecc99ac5b7dc459e8075988d8cd0aae86a6d24fcf | 
| eafa1eb732d2a0e38b98d5eae0ac6fb520b6d544dad69844b1cf20a9a35334b1 | 
| eedf9d39f63fc62cf545ac2a004bb6c72b2c7e405dbcdfa404b83118145f58ef | 
| fe4d3098d5548a29159af095ed0f8ece59162d3b284e875a160f550edbbf19b6 | 

### C2 URLs

| http\[:\]//103\[.\]226\[.\]155\[.\]200\[:\]8882 | 
| http\[:\]//178\[.\]landexuan\[.\]site\[:\]8882 | 
| http\[:\]//18\[.\]118\[.\]213\[.\]237\[:\]8080 | 
| http\[:\]//18\[.\]hhpp666\[.\]xyz\[:\]80 | 
| http\[:\]//194\[.\]59\[.\]30\[.\]222\[:\]8882 | 
| http\[:\]//202\[.\]8\[.\]120\[.\]249\[:\]8882 | 
| http\[:\]//66\[.\]154\[.\]103\[.\]112\[:\]8080 | 
| http\[:\]//a01\[.\]ai-poolion\[.\]cc\[:\]80 | 
| http\[:\]//a6cthflpd8xih09\[.\]fit\[:\]80 | 
| http\[:\]//ai-poolion\[.\]cc\[:\]80 | 
| http\[:\]//bauking\[.\]ch\[:\]80 | 
| http\[:\]//c2\[.\]ios\[.\]catcoinglobal\[.\]top\[:\]8882 | 
| http\[:\]//darksword\[.\]bitbrowserpro\[.\]com\[:\]443 | 
| http\[:\]//darksword\[.\]botiq\[.\]site\[:\]80 | 
| http\[:\]//dsreceiver\[.\]onaylarim\[.\]com\[:\]80 | 
| http\[:\]//dsw\[.\]webtest\[.\]eu\[.\]cc\[:\]443 | 
| http\[:\]//i1\[.\]9kym\[.\]com\[:\]8882 | 
| http\[:\]//ios\[.\]eseu\[.\]top\[:\]8882 | 
| http\[:\]//ios99\[.\]crowdsec\[.\]site\[:\]8882 | 
| http\[:\]//iosadmin\[.\]wanyebao\[.\]cn\[:\]443 | 
| http\[:\]//iosqbranch-bzbtegd6efhqbxc4\[.\]swedencentral-01\[.\]azurewebsites\[.\]net\[:\]8882 | 
| http\[:\]//solutionsresults\[.\]com\[:\]8882 | 
| http\[:\]//sqwas\[.\]shapelie\[.\]com\[:\]8882 | 
| http\[:\]//zuchee\[.\]cn\[:\]8882 | 
| https\[:\]//178\[.\]landexuan\[.\]site\[:\]8881 | 
| https\[:\]//18\[.\]118\[.\]213\[.\]237\[:\]8080 | 
| https\[:\]//18\[.\]hhpp666\[.\]xyz\[:\]443 | 
| https\[:\]//194\[.\]59\[.\]30\[.\]222\[:\]8881 | 
| https\[:\]//66\[.\]154\[.\]103\[.\]112\[:\]8080 | 
| https\[:\]//a01\[.\]ai-poolion\[.\]cc\[:\]443 | 
| https\[:\]//a6cthflpd8xih09\[.\]fit\[:\]443 | 
| https\[:\]//oxmfnhyg | 
| https\[:\]//ai-poolion\[.\]cc\[:\]443 | 
| https\[:\]//bauking\[.\]ch\[:\]80 | 
| https\[:\]//c2\[.\]ios\[.\]catcoinglobal\[.\]top\[:\]8881 | 
| https\[:\]//darksword\[.\]bitbrowserpro\[.\]com\[:\]443 | 
| https\[:\]//darksword\[.\]botiq\[.\]site\[:\]443 | 
| https\[:\]//dsreceiver\[.\]onaylarim\[.\]com\[:\]443 | 
| https\[:\]//dsw\[.\]webtest\[.\]eu\[.\]cc\[:\]443 | 
| https\[:\]//i1\[.\]9kym\[.\]com\[:\]8881 | 
| https\[:\]//ios\[.\]eseu\[.\]top\[:\]8881 | 
| https\[:\]//ios99\[.\]crowdsec\[.\]site\[:\]8881 | 
| https\[:\]//iosadmin\[.\]wanyebao\[.\]cn\[:\]443 | 
| https\[:\]//iosqbranch-bzbtegd6efhqbxc4\[.\]swedencentral-01\[.\]azurewebsites\[.\]net\[:\]8881 | 
| https\[:\]//solutionsresults\[.\]com\[:\]8881 | 
| https\[:\]//sqwas\[.\]shapelie\[.\]com\[:\]8881 | 
| https\[:\]//zuchee\[.\]cn\[:\]8881 | 
| dsw\[.\]webtest.eu\[.\]cc | 

Subscribe to our blog to receive the latest research and industry trends delivered straight to your inbox. Our blog content covers sophisticated mobile threats, unpatched vulnerabilities, smishing, and the latest industry news to keep you informed and secure.
