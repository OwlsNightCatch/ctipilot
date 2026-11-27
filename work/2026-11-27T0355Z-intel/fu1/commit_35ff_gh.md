---
title: "nfsd: preflight SEQUENCE replies before accepting a slot · torvalds/linux@35ff1a7"
author: Jj-Anssi
url: https://github.com/torvalds/linux/commit/35ff1a7a7e3835c3e974bc5c45d335897564ceae
hostname: github.com
description: nfsd4_sequence() narrows the reply buffer to the session's cached reply limit before it accepts the slot seqid. A client may negotiate ca_maxresponsesize_cached down to NFSD_MIN_HDR_SEQ_SZ, and...
sitename: GitHub
date: "2026-08-17"
categories: ['repository:2325298']
fingerprint: "6b12782ce4a84bde"
language: en
image: https://opengraph.githubassets.com/5924825cf38fe61019eb8c6945785a98250eb4f93ac477259748522d1253c4da/torvalds/linux/commit/35ff1a7a7e3835c3e974bc5c45d335897564ceae
pagetype: object
filedate: "2026-11-27"
---
## Repository navigation


# Commit 35ff1a7

nfsd: preflight SEQUENCE replies before accepting a slot

nfsd4\_sequence() narrows the reply buffer to the session's cached
reply limit before it accepts the slot seqid. A client may negotiate
ca\_maxresponsesize\_cached down to NFSD\_MIN\_HDR\_SEQ\_SZ, and
nfsd4\_alloc\_slot() then gives every slot a zero-length sl\_data\[\]. A
COMPOUND tag can fill that narrowed buffer until it holds the
SEQUENCE opcode but not the status word that follows.
nfsd4\_encode\_operation() returns without running
nfsd4\_encode\_sequence(), so cstate.data\_offset stays zero. It leaves
op->status at nfs\_ok as well, so the COMPOUND is treated as having
succeeded.
nfsd4\_store\_cache\_entry() declines to cache a lone SEQUENCE that
returned an error. That test reads the status the operation
reported, so it passes here. The copy starts at offset zero and
takes the whole reply, RPC and COMPOUND headers included, into the
zero-length sl\_data\[\]. The COMPOUND tag is copied along with it, so
the client picks most of the bytes written past the end of the slot:
  BUG: KASAN: slab-out-of-bounds in read\_bytes\_from\_xdr\_buf+0x1bc/0x390
  Write of size 80 at addr ffff888003a549cd by task kunit\_try\_catch/24
   \_\_asan\_memcpy+0x38/0x60
   read\_bytes\_from\_xdr\_buf+0x1bc/0x390
   nfsd4\_sequence\_done+0x5b0/0x810
   nfs4svc\_encode\_compoundres+0x1bf/0x240
Check that the fixed-size SEQUENCE result, plus room for a following
operation's error status, fits the negotiated limit before narrowing
the buffer and consuming the slot seqid. The slot and its reply
cache are left unchanged, as RFC 8881 Section 2.10.6.1.2 requires of
an error returned from SEQUENCE.
Fixes: [`47ee529`](https://github.com/torvalds/linux/commit/47ee52986472dba068e8223cbaf1b65d74238781)("nfsd4: adjust buflen to session channel limit") Cc: stable@vger.kernel.org Assisted-by: Codex:gpt-5 Signed-off-by: Jérémy Jean \<Jeremy.Jean@oss.cyber.gouv.fr> Tested-by: Mayank Jangid (OpenSec Intelligence) \<mayank.jangid.moon@gmail.com> Link:

[https://patch.msgid.link/20260817-jean-v1-1-9e356596ab85@kernel.org](https://patch.msgid.link/20260817-jean-v1-1-9e356596ab85@kernel.org)Signed-off-by: Chuck Lever \<cel@kernel.org>

1 parent [e27c632](https://github.com/torvalds/linux/commit/e27c63245903402ccfdb46c576462981a7e032e3) commit 35ff1a7

1 file changed

Lines changed: 18 additions & 1 deletion

| Original file line number | Diff line number | Diff line change |  | 
|---|---|---|---|
|  |  |  |  | 
| `5044` | `5044` |  |  | 
| `5045` | `5045` |  |  | 
| `5046` | `5046` |  |  | 
|  | `5047` | `+` |  | 
| `5047` | `5048` |  |  | 
| `5048` | `5049` |  |  | 
| `5049` | `5050` |  |  | 
|  |  |  |  | 
| `5053` | `5054` |  |  | 
| `5054` | `5055` |  |  | 
| `5055` | `5056` |  |  | 
|  | `5057` | `+` |  | 
| `5056` | `5058` |  |  | 
| `5057` | `5059` |  |  | 
| `5058` | `5060` |  |  | 
|  |  |  |  | 
| `5130` | `5132` |  |  | 
| `5131` | `5133` |  |  | 
| `5132` | `5134` |  |  | 
| `5133` |  | `-` |  | 
|  | `5135` | `+` |  | 
|  | `5136` | `+` |  | 
|  | `5137` | `+` |  | 
|  | `5138` | `+` |  | 
|  | `5139` | `+` |  | 
|  | `5140` | `+` |  | 
|  | `5141` | `+` |  | 
|  | `5142` | `+` |  | 
|  | `5143` | `+` |  | 
|  | `5144` | `+` |  | 
|  | `5145` | `+` |  | 
|  | `5146` | `+` |  | 
|  | `5147` | `+` |  | 
|  | `5148` | `+` |  | 
|  | `5149` | `+` |  | 
|  | `5150` | `+` |  | 
| `5134` | `5151` |  |  | 
| `5135` | `5152` |  |  | 
| `5136` | `5153` |  |  | 
|  |  |  |  | 

## 0 commit comments
