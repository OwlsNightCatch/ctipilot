---
title: GitHub - garrettfoster13/scuzzy
url: https://github.com/garrettfoster13/scuzzy
hostname: github.com
description: Contribute to garrettfoster13/scuzzy development by creating an account on GitHub.
sitename: GitHub
date: "2026-11-02"
categories: ['repository:1443532952']
fingerprint: c89be514d7acf49
---
Python script for poking at iSCSI targets that gate access by initiator IQN. Read-only — the only SCSI command it sends is READ(10).

No dependencies, Python 3 only.

```
python3 scuzzy.py --portal <host> [--port 3260] --ini <initiator IQN> [--target <target IQN>] <command>
```
Commands:

- `probe` — discovery login + SendTargets, see what the portal gives back for an initiator
- `oracle` — test a list of candidate initiator IQNs; authorized ones leak the target IQN in the SendTargets response
- `login` — try a normal-session login against a target
- `ls` — parse GPT/NTFS/$MFT and list files on the volume
- `download` — pull a file off the volume by name or path (streams in 16K chunks, prints SHA256)

Examples:

```
python3 scuzzy.py --portal 10.10.10.10 --ini iqn.1991-05.com.microsoft:node01 probe
python3 scuzzy.py --portal 10.10.10.10 oracle --ini-list @iqns.txt
python3 scuzzy.py --portal 10.10.10.10 --ini <iqn> --target <iqn> ls --path "Cluster"
python3 scuzzy.py --portal 10.10.10.10 --ini <iqn> --target <iqn> download --path "testvm/Virtual Hard Disks/testvm.vhdx"
```
`--ini-list` takes space/comma separated IQNs or `@file` (one per line, `#` comments).

Targets that require CHAP aren't supported.
