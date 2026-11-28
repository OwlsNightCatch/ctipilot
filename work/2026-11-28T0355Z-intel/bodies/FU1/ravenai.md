---
title: "Four Requests to Shell: Ek0ms's Cacti 0-Day Chain"
author: Ek0ms
url: https://ravenai.sh/blog/four-requests-to-shell-cacti
hostname: ravenai.sh
sitename: RavenAI
date: "2026-11-26"
fingerprint: "40d2dc59ad58a2bb"
language: en
image: https://ravenai.sh/blog/four-requests-to-shell-cacti/opengraph-image
pagetype: article
filedate: "2026-11-28"
---
[All research](https://ravenai.sh/blog)

External Research

# Four Requests to Shell: Ek0ms's Cacti 0-Day Chain

Ek0ms chained a guest profile setting, stored SQL injection, and the realtime poller into unauthenticated command execution on Cacti 1.2.31 in her lab.

## On this page

Four HTTP requests. A guest session. A shell command delivered through a graphing system's own poller.

[Ek0ms](https://github.com/ekomsSavior), publishing with Church of Malware, documented this Cacti chain as **4HTTP2ROOT**. A working unauth-RCE against **Cacti Core 1.2.31**. Her research follows a value from a guest-editable profile setting into a SQL `LIMIT` clause, then uses the resulting database write to change the command that Cacti's realtime poller executes. The [upstream research and PoC](https://github.com/ekomsSavior/Sad-Girls-0day-Club/tree/main/4http2shell) are hers; this article summarizes the path and its operating conditions.

## The four-request path

| Request | Guest-accessible action | Boundary crossed | 
|---|---|---|
| 1 | Open `auth_profile.php` | Receive a guest session and CSRF token without credentials | 
| 2 | POST `auth_profile.php?action=update_data` | Store a SQL fragment in `preview_graphs_per_page` | 
| 3 | Open `graph_view.php?action=preview` | Use the stored value in `LIMIT`; execute a stacked `UPDATE` against `poller_item` | 
| 4 | Open `graph_realtime.php?action=init` | Run the altered poller command through `popen()` | 

The first request is ordinary guest behavior. The failure is that a guest can write a value later treated as trusted SQL syntax.

## 1. A guest session can edit a numeric setting

With the guest account enabled, a fresh visitor can open the profile page and obtain a session cookie plus `csrfMagicToken`. No account credentials are needed. Ek0ms used that token to submit `name=preview_graphs_per_page` and an arbitrary `value` to the profile update action.

That setting is meant to hold a graph count. The profile write uses a prepared statement, but it does not enforce an integer value. The database faithfully stores the attacker's string; the vulnerability appears when another code path reads it back.

```text
GET  /cacti/auth_profile.php?tab=general&header=false
POST /cacti/auth_profile.php?tab=general&action=update_data&header=false
name=preview_graphs_per_page
value=1;UPDATE poller_item SET host_id=1,action=1,arg1=0x... WHERE local_data_id=1;--
```
The row identifiers above are from the lab, not universal Cacti constants. The hex value represents the command placed in `arg1`.

## 2. A stored page size becomes SQL

The preview action loads `preview_graphs_per_page` as the default `graphs` value. The request-side integer filter does not cover that database-sourced default. The value is then concatenated into a `LIMIT` fragment passed to `get_allowed_graphs()`.

```text
GET /cacti/graph_view.php?action=preview&page=1&clear=1
... LIMIT 0,1;UPDATE poller_item SET ...;--
```
Ek0ms reports that the PDO path in her test accepted the stacked statement. The appended `UPDATE` changed `poller_item.arg1`, while the HTTP response still rendered a preview page. Her writeup notes a PHP warning about a nonnumeric value, but no obvious failure in the browser response.

This is the decisive trust mistake: validation on an incoming request does not make a stored default safe. The value needs to be constrained before storage and before it enters SQL.

## 3. The realtime poller turns the write into execution

The same guest session can initialize a realtime graph. That request reaches `poller_realtime.php`, then `cmd_realtime.php`, where the poller reads the modified `arg1` and calls `exec_poll()`. The latter opens the command with `popen()`.

```text
GET /cacti/graph_realtime.php?action=init&local_graph_id=1&ds_step=10&size=90
cmd_realtime.php:  exec_poll($item['arg1'])
lib/poller.php:     popen($command, 'r')
```
The graph ID and poller item must be valid for the target. Ek0ms's [upstream shell demo](https://github.com/ekomsSavior/Sad-Girls-0day-Club/blob/main/4http2shell/4http2shell-shell.sh) uses the four-request route to stage a PHP shell, then validates it with commands such as `id` and `whoami`. The supplied lab screenshot records successful guest requests and a root shell in that configuration.

## Why the chain works

Four separate behaviors make the path possible:

1. **Guest profile updates accept an arbitrary string** for a setting that should be numeric.
2. **The stored default bypasses request validation** when the graph preview reads it.
3. **The SQL query concatenates that value into `LIMIT`**, and the tested database path executes the appended statement.
4. **The poller executes a database-stored command** that the injected `UPDATE` can replace.

The observable trail is correspondingly mundane: a guest profile update, a graph preview, and a realtime graph initialization. The malformed page-size value, a nonnumeric PHP warning, a change to `poller_item.arg1`, and any newly written shell or marker are stronger investigation pivots than the HTTP status codes alone.

## What to fix

Treat these as separate boundaries. Validate `preview_graphs_per_page` as an integer on write and on read. Bind numeric pagination values instead of concatenating them into SQL; reject stacked statements where the database driver permits configuration. Restrict guest profile writes to settings the guest actually needs. Keep poller command inputs under explicit authorization and detect unexpected changes to `poller_item`, especially `arg1`.

Ek0ms validated the chain against her Cacti 1.2.31 lab. The supplied research does not establish whether other versions, guest configurations, or database settings are exploitable. Consult her [original 4HTTP2ROOT writeup and PoC](https://github.com/ekomsSavior/Sad-Girls-0day-Club/tree/main/4http2shell) for source, reproduction details, and updates.
