---
title: "Survey Says…. Remote Code Execution: CVE-2026-90817"
author: B
url: https://www.securifera.com/blog/2026/09/27/survey-says-remote-code-execution-cve-2026-90817/
hostname: securifera.com
description: One of the things I find most exciting about AI agents, especially as a former vulnerability researcher and CTF-er, is their ability to bring some of the more creative exploit primitives I’ve encountered over the years to life against real-world targets. While AI didn't propose the solution in this example, it quickly implemented
sitename: Securifera
date: "2026-09-27"
fingerprint: af3215b4c6a80e91
---
### One of the things I find most exciting about AI agents, especially as a former vulnerability researcher and CTF-er, is their ability to bring some of the more creative exploit primitives I’ve encountered over the years to life against real-world targets. While AI didn’t propose the solution in this example, it quickly implemented and extended upon the technique after it was suggested.

### I showed an example of this in my previous [post on weaponizing ClamAV](https://www.securifera.com/blog/2026/08/07/file-drop-to-rce-cve-2026-20217/). In this post, I’ll walk through how I exploited a vulnerability I found in Vanderbilt’s REDCap survey hosting application using a technique published by [Synacktiv that abuses PHP’s filter encoding capabilities](https://www.synacktiv.com/publications/php-filters-chain-what-is-it-and-how-to-use-it).

### REDCap is freely available to internal consortium members, but the software itself is not openly distributed. Every so often, though, a member will “accidentally” publish a copy, and I was lucky enough to come across a relatively recent version.

### I pointed Codex with GPT 5.6 Sol at the REDCap source and a simple objective: find a useful path from an unauthenticated context to server-side code execution. REDCap is large, old in places, and full of routes that must work for both logged-in users and public survey participants. That makes context changes worth tracing.

## Starting with one extra decode

### REDCap’s public survey handler includes a passthrough feature that can load a small set of internal files. One allowed target is the root `index.php` dispatcher, but it is supposed to be limited to the `PdfController:index` route.

### The validation uses two representations of `__passthru`:

Copy to Clipboard

### The problem is that the code validates \_\_passthru in two different forms. PHP already URL-decodes query parameters before placing them in $\_GET, and the handler calls urldecode() again when checking the allowlist. The later route restriction, however, compares the once-decoded value directly against index.php.

### A double-encoded value causes those checks to disagree. The allowlist resolves it to index.php, while the route restriction fails to recognize it as index.php and is skipped.

Copy to Clipboard

### The handler then includes the root dispatcher with an attacker-controlled route, such as DataImportController:index.

### This is not traditional path traversal. The application loads an approved file, but two security checks interpret the same input differently because of inconsistent URL decoding.

## Reaching Data Import without a login

### Reaching the root dispatcher only passed the first boundary. REDCap still performed a route-rights check, but that check was built on the wrong user context.

### The survey handler defines `NOAUTH` and loads the project. During initialization, REDCap creates the user-rights object before assigning the survey respondent identity.

Copy to Clipboard

### The rights check treats an undefined `SUPER_USER` constant as the super-user case:

Copy to Clipboard

### The resulting rights array grants `data_import_tool => 1`, which maps directly to `DataImportController:index`. Because `NOAUTH` is defined, REDCap also skips the normal POST CSRF check.

### The result is an administrative POST route accessible through a public survey request. An attacker only needs a valid survey hash; no REDCap account, project membership, session cookie, role, or CSRF token.

### A survey hash should provide access to a survey, not administrative privileges.

## When a filename is a PHP stream

### The Data Import commit path copies `POST[fname]` directly into a local variable. It does not require a server-issued upload handle, reject URI schemes, or otherwise restrict the value before passing it to PHP file functions.

Copy to Clipboard

### We first proved this could be used to read a small portion of a arbitrary file, confirming that the server was opening the attacker-selected path.

### The more useful behavior was in csvToArray(). REDCap reads the CSV, removes a byte-order mark, and then writes the modified data back to the same caller-controlled resource.

Copy to Clipboard

### Because PHP file functions support wrappers such as php://filter, that write could be turned into a controlled byte-generation primitive. I used the technique demonstrated by Synacktiv’s PHP filter-chain generator, but not in the usual way.

### Instead of passing the generated URI directly to include() or require(), I used the generator as a byte factory. The PoC took the PHP source I wanted to write, converted it into a chain of standard PHP filters, and sent the resulting URI as fname. The generator itself never ran on the server.

### The destination was also not an empty file. It was an existing Blade cache containing compiled PHP, so leftover bytes could corrupt the payload. To handle that, the exploit used two generated filter sequences separated by dechunk.

### Conceptually, the attacker-controlled fname looked like this:

Copy to Clipboard

### The flow is easier to follow as five operations:

1. **Select the destination.** The URI’s `resource` part points to the predictable Blade cache. REDCap accepts the complete URI from `POST[fname]`.
2. **Discard the old cache bytes.** The first generated sequence emits `0 + LF + LF`, the end marker for an empty chunked message. The first `dechunk` filter consumes that marker and ignores the original cache data that follows it.
3. **Build an exact replacement.** The second generated sequence emits a valid chunked message whose body is a UTF-8 BOM followed by the selected PHP source. The final `dechunk` filter unwraps the message and leaves only those chosen bytes.
4. **Make REDCap enter its write path.** `file_get_contents()` returns `BOM || PHP`. `removeBOM()` removes the first three bytes. The before and after buffers now differ, so the CSV cleanup code calls `file_put_contents()`.
5. **Write through to the cache.** The URI declares `read=` filters only. They transform the read, but they do not transform the later write. The PHP source therefore passes directly to the underlying Blade cache file.

### The BOM was not just padding. It was what forced REDCap to perform the write. Without a removable BOM, the before-and-after buffers would match and `file_put_contents()` would never run.

### The filter-chain generator was also not the vulnerability or the execution sink. It only solved the problem of producing exact bytes. REDCap provided the attacker-controlled stream URI and read-modify-write behavior. BladeOne later provided the `include` that executed the overwritten cache.

### After the read filters completed, the buffer looked like this:

Copy to Clipboard

### REDCap removed the BOM and wrote the remaining bytes back to the same stream URI. The filters affected the read path, while the write reached the underlying resource directly.

### That turned a CSV cleanup routine into an arbitrary overwrite of any writable resource the PHP process could access.

## File write is not code execution

### The first execution attempt used a file the attacker controlled. The survey flow could create an upload, and Data Import copied it into a web temp directory with a `.php.csv` suffix. The filter chain could replace that file with exact PHP source.

### The problem was that the web server served it as `text/csv` instead of executing it.

### That was an important distinction: a PHP filter chain only gives you controlled bytes. It still needs something like `include`, `require`, a template loader, or another code-loading mechanism to turn those bytes into execution.

### Because the Data Import flow required a CSV filename, changing the upload suffix was not enough. I went back to the source and looked for a predictable file that met three requirements:

1. ### The PHP process could write it.
2. ### Its name was deterministic.
3. ### The application would later execute it through a public route.

### REDCap’s BladeOne cache matched all three.

### BladeOne stores compiled templates under `APP_PATH_TEMP/cache`, and in normal operation derives each cache filename from the SHA-1 of the view name:

Copy to Clipboard

### The view name `parcel.show` therefore maps to a deterministic `.bladec` file. The public survey routing flaw can also reach `ParcelController:show`. That action renders `parcel.show` even when no user is logged in.

### BladeOne then executes the compiled file with a normal PHP include:

Copy to Clipboard

### The cache did not need a `.php` extension. Apache did not need to execute it directly. The application included it as PHP and returned its output through the Parcel response.

## Making the cache test survivable

### Overwriting a compiled template cache is risky. A partial write can leave a persistent PHP parse error, a zero-byte file can break the view, load-balanced nodes can fall out of sync, and OPcache may continue serving stale bytecode.

### Because of that, I split the proof into two stages.

### The first stage wrote only a unique marker, no command execution and no callback. Before touching the live cache, the harness also saved a clean copy of the legitimate compiled template.

### The final proof then followed a guarded sequence:

1. ### Render the normal Parcel view and record a clean baseline.
2. ### Write the marker payload through Data Import.
3. ### Read the cache back and require an exact byte-for-byte match.
4. ### Wait for PHP bytecode revalidation.
5. ### Trigger the Parcel route once using a random secret and short timeout.
6. ### Inside the payload, rebuild and verify the trusted Blade template before allowing any command to run.
7. ### Delete the injected cache, request the view again, and verify that REDCap regenerated a clean copy.
8. ### Replay the trigger and confirm the marker is gone.

### The marker appeared once in a normal HTTP 200 response. A direct cache check then returned 404, and the next Parcel request rebuilt a clean compiled template with no marker or trigger secret.

### That demonstrated both PHP execution and successful recovery of the original cache state.

## Five faults in one chain

### The final result was CVE-2026-90817, but the exploit depended on several independently fixable defects:

| Component | Root cause | Result | 
|---|---|---|
| Survey passthrough | The allowlist and route check used different decoded values | A public request reached the general project dispatcher | 
| Project rights | User rights were calculated before the survey identity existed, and undefined `SUPER_USER` meant full rights | The public context received the Data Import privilege | 
| Data Import `fname` | A client value was trusted as a local path or PHP stream | The attacker selected resources for read and delete operations | 
| BOM normalization | Changed bytes were written back to the same selected resource | The read primitive became a controlled overwrite | 
| Blade cache | A predictable, worker-writable compiled template was included as PHP | The overwrite became code execution |
