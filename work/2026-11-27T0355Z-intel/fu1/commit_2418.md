---
title: "nfsd: set op->status when an operation's header cannot be encoded · torvalds/linux@241848c"
author: Chucklever
url: https://github.com/torvalds/linux/commit/241848cc774e
hostname: github.com
description: nfsd4_encode_operation() leaves op->status alone when the reply buffer has no room for the operation's opcode and status word. nfsd4_proc_compound() reads the unchanged nfs_ok as success and...
sitename: GitHub
date: "2026-08-17"
categories: ['repository:2325298']
fingerprint: "69d5033ea530b3d4"
language: en
image: https://opengraph.githubassets.com/1f318753862dab41e6c831027d983b4489087c8410ffd7bb413b550626c45701/torvalds/linux/commit/241848cc774eb1172fa867bb6a28c32cf1869c0d
pagetype: object
filedate: "2026-11-27"
---
## Repository navigation


# Commit 241848c

committed

nfsd: set op->status when an operation's header cannot be encoded

nfsd4\_encode\_operation() leaves op->status alone when the reply
buffer has no room for the operation's opcode and status word.
nfsd4\_proc\_compound() reads the unchanged nfs\_ok as success and
goes on to the next operation, so the reply counts an operation
whose result was never encoded.
Report the failure through nfsd4\_check\_resp\_size(), which the rest
of the function already uses. It returns NFS4ERR\_REP\_TOO\_BIG, or
NFS4ERR\_REP\_TOO\_BIG\_TO\_CACHE on a session, and the COMPOUND ends
at that operation.
Two paths narrow the reply buffer: nfsd4\_sequence(), which rejects
a SEQUENCE result that does not fit, and nfsd4\_encode\_splice\_read(),
which can leave a single XDR word in the head page. Whether a
COMPOUND reaches that boundary is unproven, so this is a guard
rather than a fix.
Link: [https://patch.msgid.link/20260817-jean-v1-2-9e356596ab85@kernel.org](https://patch.msgid.link/20260817-jean-v1-2-9e356596ab85@kernel.org)Signed-off-by: Chuck Lever \<cel@kernel.org>

1 parent [5d5a72e](https://github.com/torvalds/linux/commit/5d5a72e965c8b6ec870f114b9fe4961b8697732e) commit 241848c

1 file changed

Lines changed: 11 additions & 2 deletions

| Original file line number | Diff line number | Diff line change |  | 
|---|---|---|---|
|  |  |  |  | 
| `6723` | `6723` |  |  | 
| `6724` | `6724` |  |  | 
| `6725` | `6725` |  |  | 
| `6726` |  | `-` |  | 
|  | `6726` | `+` |  | 
|  | `6727` | `+` |  | 
|  | `6728` | `+` |  | 
|  | `6729` | `+` |  | 
|  | `6730` | `+` |  | 
|  | `6731` | `+` |  | 
|  | `6732` | `+` |  | 
| `6727` | `6733` |  |  | 
|  | `6734` | `+` |  | 
| `6728` | `6735` |  |  | 
| `6729` |  | `-` |  | 
|  | `6736` | `+` |  | 
|  | `6737` | `+` |  | 
| `6730` | `6738` |  |  | 
|  | `6739` | `+` |  | 
| `6731` | `6740` |  |  | 
| `6732` | `6741` |  |  | 
| `6733` | `6742` |  |  | 
|  |  |  |  | 

## 0 commit comments
