---
title: eMudhra Intermediate CA Compromise
url: https://emudhra.we-have-a-problem.com/
hostname: we-have-a-problem.com
description: The private keys of eight eMudhra intermediate CA certificates, trusted by major root programs, have been compromised. Check whether your client is affected and how to protect it.
sitename: we-have-a-problem.com
date: "2026-10-22"
fingerprint: bd0dfb16791ba6c0
---
English / [日本語（要約）](https://emudhra.we-have-a-problem.com/ja.html)

**20th October 2026**

**Update, 28th October:** the developer tools Apple ships with macOS, including `git`, `curl` and `python3`, still trust the compromised certificates, and macOS 27.2 undid user-applied fixes. [Read more.](https://emudhra.we-have-a-problem.com/apple.html)

The private keys of eight eMudhra intermediate CA certificates have been compromised. They chain to roots trusted by the Mozilla, Microsoft, Apple and Chrome root programs and by many downstream trust stores.

Root programs are run by operating system and browser vendors to vet certificate authorities and decide which ones their products trust. Trust stores are the lists of trusted root certificates that operating systems, browsers, language runtimes, libraries and applications use to verify certificates, and many are based on the root programs' lists.

To demonstrate that the keys are compromised, the original reporter Wayne signed the following message with the private key of each of the eight intermediate CAs and reported it to the Root Program Teams on the 17th of October:

We have a problem here - Wayne


[proof.zip](https://emudhra.we-have-a-problem.com/proof.zip) contains the message, and for each intermediate the certificate, its public key and a signature on the message. To verify with OpenSSL:

openssl x509 -in EM-DV-TLS-CA-G3B.crt.pem -noout -pubkey | diff - EM-DV-TLS-CA-G3B.pub.pem
openssl dgst -sha384 -verify EM-DV-TLS-CA-G3B.pub.pem -signature EM-DV-TLS-CA-G3B.sig message.txt

The root programs and many downstream trust stores have taken action to protect their users. The certificates have been blocked in Firefox and Chrome since the 17th of October, on Microsoft platforms since the 20th and on Apple products since the 22nd.

The issue was responsibly disclosed to downstream trust stores on the 19th of October. Many have already released updates or are in the process of releasing updates.

An attacker with the private key of any of the compromised intermediate CAs could impersonate any website or service.

This has already been remediated by Mozilla, Microsoft, Apple, and Chrome for their users through their tools for distributing revocation information such as [OneCRL](https://blog.mozilla.org/security/2015/03/03/revoking-intermediate-certificates-introducing-onecrl/), [CRLite](https://hacks.mozilla.org/2025/08/crlite-fast-private-and-comprehensive-certificate-revocation-checking-in-firefox/) and [CRLSets](https://www.chromium.org/Home/chromium-security/crlsets/).

The CA has also revoked the compromised intermediate certificates. However, many other clients do not consume revocation information and require software updates to ensure they no longer trust the compromised intermediates. These include applications and libraries that ship their own CA bundle, and apps built on Electron, such as Slack and Discord. Electron apps only pick up Electron's fix once they are updated to a version built on a [patched Electron release](https://emudhra.we-have-a-problem.com#patched-runtimes). Updating the operating system or browser may not be enough for these clients.

| Intermediate CA | Chains to | Result | 
|---|---|---|


A ✅ only means that the connection failed. Browsers do not tell the page why, so a network problem looks the same as a rejected certificate. To double-check, open the link in that row: if it loads without a warning page, the browser is vulnerable.

If the browser is behind a proxy that intercepts TLS, the result reflects the proxy's trust store rather than the browser's. A ❌ then means the proxy still trusts the compromised intermediates, and every client behind it remains vulnerable until the proxy is updated or disabled, even if the browser itself has been patched.

On 22nd October 2026, two chains marked *No CT* were added. Their leaf certificates were never logged to Certificate Transparency (CT), so clients that enforce CT reject them even if they still trust the intermediate. A successful connection to these hosts means the client trusts the compromised intermediates *and* does not enforce CT. As described [below](https://emudhra.we-have-a-problem.com#cause), these are the clients that can be attacked without anyone noticing.

To check curl or other command-line clients, run:

curl https://dv-g3b-emudhra.we-have-a-problem.com/
curl https://dv-g3b-aaa-emudhra.we-have-a-problem.com/

A certificate error means the client does not trust the compromised intermediates. To check whether the client also accepts certificates that were never logged to CT, run:

curl https://dv-g3b-noct-emudhra.we-have-a-problem.com/
curl https://dv-g3b-aaa-noct-emudhra.we-have-a-problem.com/

Most browsers enforce CT, but many non-browser clients, including curl, do not which places them at greater risk.

To check a trust store offline, [chains.zip](https://emudhra.we-have-a-problem.com/chains.zip) contains the certificate chain served by each of the fourteen hosts above in PEM format, plus some additional test cases and instructions for verifying them with OpenSSL.

The private keys for the intermediate certificates were incorrectly generated by the CA. This means that anyone can recover them from the certificates.

This would have been possible since the certificates were created in April 2025. There are no entries in the certificate transparency logs for these intermediates in that period, indicating that CT-enforcing clients like Firefox, Chrome, Edge and Safari could not have been attacked.

However, many clients outside of the browser ecosystem do not enforce Certificate Transparency. We do not know if attackers exploited the flawed key generation to target these clients.

Further technical information about the cause is captured in the [initial incident report](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449) in Mozilla's bug tracker.

The servers behind the [checker](https://emudhra.we-have-a-problem.com#check) record how many times each user-agent connects successfully, meaning it still trusts the compromised intermediates. Only these counts are recorded. See the [user-agent statistics](https://statistics-emudhra.we-have-a-problem.com/).

A [JSON dump](https://statistics-emudhra.we-have-a-problem.com/stats.json) with more detail, including counts for each JA4 fingerprint, is also available.

[impacted-intermediates.json](https://emudhra.we-have-a-problem.com/impacted-intermediates.json) lists the eight intermediates and their Sectigo cross-signs. [roots.json](https://emudhra.we-have-a-problem.com/roots.json) lists the roots they chain to.

Please see [this thread](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/0R3XLJL6FuE) in Mozilla's dev-security-policy forum.

Implementors may also find [chains.zip](https://emudhra.we-have-a-problem.com/chains.zip) useful as it includes additional test cases to verify that any changes are effective.

Users should update their browsers and operating systems to the latest versions as soon as possible.

| Software | Patched version | 
|---|---|
| Cloudflare CFSSL trust store | [2026.10.1](https://github.com/cloudflare/cfssl_trust/releases/tag/trust-store-2026.10.1) | 
| Composer ca-bundle | [1.4.16, 1.6.0](https://github.com/composer/ca-bundle/releases/tag/1.6.0) | 
| curl CA bundle | [2026-10-20](https://curl.se/docs/caextract.html) | 
| Elixir castore | [1.0.22](https://hex.pm/packages/castore/1.0.22) | 
| Erlang certifi | [2.18.0](https://certifi.hexdocs.pm/2.18.0/changelog.html#2-18-0-2026-10-23) | 
| Kubernetes cert-manager | [trust-pkg-debian-trixie:20250419-deb13u1.0, trust-pkg-debian-bookworm:20250419-deb12u2.0](https://cert-manager.io/docs/trust/trust-manager/#emudhra-compromise) | 
| NSS | [3.131.1](https://groups.google.com/a/mozilla.org/g/dev-tech-crypto/c/vSxZxnOMMvs) | 
| Perl Mozilla::CA | [20261020](https://metacpan.org/release/LWP/Mozilla-CA-20261020) | 
| Python certifi | [2026.10.19](https://github.com/certifi/python-certifi/releases/tag/2026.10.19) | 
| Ruby excon | [1.8.0](https://github.com/excon/excon/blob/v1.8.0/changelog.txt#L15) | 
| Rust rustls-webpki | [0.103.16](https://github.com/rustls/webpki/releases/tag/v%2F0.103.16) | 
| Rust webpki-roots / webpki-root-certs | [1.0.10](https://github.com/rustls/webpki-roots/releases/tag/v%2F1.0.10) | 

| Software | Patched version | 
|---|---|
| ArgoCD | [3.3.18](https://github.com/argoproj/argo-cd/releases/tag/v3.3.18), [3.4.12](https://github.com/argoproj/argo-cd/releases/tag/v3.4.12), [3.5.6](https://github.com/argoproj/argo-cd/releases/tag/v3.5.6), [3.6.0-rc4](https://github.com/argoproj/argo-cd/releases/tag/v3.6.0-rc4) | 
| Bazel | [7.7.2](https://github.com/bazelbuild/bazel/releases/tag/7.7.2), [8.8.2](https://github.com/bazelbuild/bazel/releases/tag/8.8.2), [9.3.1](https://github.com/bazelbuild/bazel/releases/tag/9.3.1), [10.0.0rc2](https://github.com/bazelbuild/bazel/releases/tag/10.0.0rc2) | 
| certbot | [pending](https://github.com/certbot/certbot/pull/10812) | 
| Claude Code | [2.1.303](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21303) | 
| Conda | [26.9.4](https://docs.conda.io/projects/conda/en/latest/release-notes.html#version-26.9.4) | 
| containerd | [pending](https://github.com/containerd/containerd/pull/14439) | 
| Docker cli | [29.9.2](https://github.com/docker/cli/releases/tag/v29.9.2) | 
| Docker Desktop | [4.96.2](https://docs.docker.com/desktop/release-notes/#4962) | 
| Docker Engine | [29.9.2](https://docs.docker.com/engine/release-notes/29/#2992) | 
| Git for Windows | [2.56.0.3](https://github.com/git-for-windows/git/releases/tag/v2.56.0.windows.3) | 
| GitLab | [19.5.3, 19.4.5, 19.3.7, 19.2.10, 19.1.10, 19.0.11, 18.11.14](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-3-released/) | 
| GitLab runner | [19.5.1](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-3-released/) | 
| GitHub CLI | [2.102.1](https://github.com/cli/cli/releases/tag/v2.102.1) | 
| Godot | [pending](https://github.com/godotengine/godot/pull/124724) | 
| gRPC | [1.84.1](https://github.com/grpc/grpc/releases/tag/v1.84.1), [1.85.0](https://github.com/grpc/grpc/releases/tag/v1.85.0) | 
| Immich | [3.3.5](https://github.com/immich-app/immich/releases/tag/v3.3.5) | 
| JetBrains IDEs | [2025.3–2026.3 latest updates](https://blog.jetbrains.com/security/2026/10/compromised-emudhra-certificates-ides/) | 
| JetBrains Toolbox App | [3.9.1, 3.8.2](https://blog.jetbrains.com/security/2026/10/compromised-emudhra-certificates-ides/) | 
| LibreOffice | [pending](https://gerrit.libreoffice.org/c/core/+/212892) | 
| litellm | [1.103.8](https://github.com/BerriAI/litellm/releases/tag/v1.103.8), [1.104.6](https://github.com/BerriAI/litellm/releases/tag/v1.104.6), [1.105.4](https://github.com/BerriAI/litellm/releases/tag/v1.105.4), [1.106.3](https://github.com/BerriAI/litellm/releases/tag/v1.106.3) | 
| mise | [2026.10.17](https://github.com/jdx/mise/releases/tag/v2026.10.17) | 
| mitmproxy | [12.3](https://www.mitmproxy.org/posts/releases/mitmproxy-12.3/) | 
| Obsidian | [1.14.5](https://obsidian.md/changelog/2026-10-22-desktop-v1.14.5/) | 
| pip | [26.2.2](https://github.com/pypa/pip/releases/tag/26.2.2) | 
| pixi | [0.82.1](https://github.com/prefix-dev/pixi/releases/tag/v0.82.1) | 
| Plex Media Server | [1.43.5.11079](https://forums.plex.tv/t/plex-media-server/30447/720) | 
| pypi-publish GitHub Action | [1.14.3](https://github.com/pypa/gh-action-pypi-publish/releases/tag/v1.14.3) | 
| Rustup | [1.29.2](https://blog.rust-lang.org/2026/10/20/Rustup-1.29.2/) | 
| sigstore | [4.5.1](https://github.com/sigstore/sigstore-python/releases/tag/v4.5.1) | 
| Tailscale | [1.104.2](https://tailscale.com/changelog#2026-10-21) | 
| uv | [0.13.5](https://github.com/astral-sh/uv/releases/tag/0.13.5) | 
| Visual Studio Code | [1.143.1](https://code.visualstudio.com/updates/v1_143) | 
| yt-dlp | [2026.10.26](https://github.com/yt-dlp/yt-dlp/releases/tag/2026.10.26), [WARNING: do not use self-updater](https://github.com/yt-dlp/yt-dlp/releases/tag/2026.10.21) | 

Add more at [github.com/galadran/we-have-a-problem.com](https://github.com/galadran/we-have-a-problem.com).

macOS blocks the compromised intermediates in apps that use Apple's networking and security frameworks. However, the built-in command line tools verify certificates against `/etc/ssl/cert.pem` without checking revocation. Apple has [stated](https://support.apple.com/en-us/149555) it will update that file in a future macOS update. Until then, you can remove the affected roots yourself.

Back up the file:

\[ -e /etc/ssl/cert.pem.orig \] || sudo cp -p /etc/ssl/cert.pem /etc/ssl/cert.pem.orig

Remove emSign ECC Root CA - G3. This prints nothing on success:

```
t=$(mktemp) &&
awk -v s='=== /C=IN/OU=emSign PKI/O=eMudhra Technologies Limited/CN=emSign ECC Root CA - G3' \
  '/^(===|###) /{skip=0} $0==s{skip=1} !skip' /etc/ssl/cert.pem > "$t" &&
[ -s "$t" ] && sudo install -m 0644 -o root -g wheel "$t" /etc/ssl/cert.pem; rm -f "$t"
```
This does not block the six Sectigo cross-signed intermediates, which chain to AAA Certificate Services. To block those too, also remove that root. This may break verification of unaffected websites that chain to AAA Certificate Services:

```
t=$(mktemp) &&
awk -v s='=== /C=GB/ST=Greater Manchester/L=Salford/O=Comodo CA Limited/CN=AAA Certificate Services' \
  '/^(===|###) /{skip=0} $0==s{skip=1} !skip' /etc/ssl/cert.pem > "$t" &&
[ -s "$t" ] && sudo install -m 0644 -o root -g wheel "$t" /etc/ssl/cert.pem; rm -f "$t"
```
Check the result. This lists either root if it is still in the file, and prints nothing if both were removed. If it shows an error, restore the backup:

openssl crl2pkcs7 -nocrl -certfile /etc/ssl/cert.pem | openssl pkcs7 -print\_certs -noout |
  grep -E 'emSign ECC Root CA - G3|AAA Certificate Services'

Apple has warned that until it ships its own fix, a macOS update may replace `/etc/ssl/cert.pem`. You may need to repeat these steps after each update.

The built-in `pip3`, and the `pip` in virtual environments created from the built-in `python3`, use their own outdated copy of the roots instead. To make them use the fixed system file, run:

```
F="$(/usr/bin/python3 -c 'import sysconfig; print(sysconfig.get_path("stdlib"))')/sitecustomize.py" &&
echo 'import os; os.environ.setdefault("PIP_CERT", "/etc/ssl/cert.pem")' | sudo tee -a "$F" > /dev/null &&
sudo chmod 644 "$F"
```
For nix-darwin users, please **additionally** follow NixOS instructions.

See Apple's [official guidance](https://support.apple.com/en-us/149555) for more information.

Until a distribution ships an updated `ca-certificates` package, expert users can distrust the affected roots in the system trust store. This is NOT recommended for ordinary users.

On Debian and Ubuntu, run as root:

sed -i \
  -e 's|^mozilla/emSign\_ECC\_Root\_CA\_-\_G3.crt|!&|' \
  -e 's|^mozilla/Comodo\_AAA\_Services\_root.crt|!&|' \
  /etc/ca-certificates.conf && update-ca-certificates

If you use OpenJDK from Debian or Ubuntu packages, the Java keystore at `/etc/ssl/certs/java/cacerts` is **not** refreshed when the system trust store changes, due to a [long-standing bug](https://bugs.debian.org/1069251) in `ca-certificates-java`. This applies both to the workaround above and to the updated `ca-certificates` package. Following [OpenJDK's guidance](https://openjdk.org/emudhra#debian), remove and recreate the keystore as root:

rm -f /etc/ssl/certs/java/cacerts && update-ca-certificates --fresh

On Alpine, run as root:

apk add ca-certificates &&
sed -i -e 's|^mozilla/emSign\_ECC\_Root\_CA\_-\_G3.crt|!&|' \
  /etc/ca-certificates.conf && update-ca-certificates

On Fedora, RHEL, CentOS Stream, Rocky Linux, AlmaLinux and Amazon Linux 2023, run as root:

d=/etc/pki/ca-trust/source/blocklist; \[ -d $d \] || d=/etc/pki/ca-trust/source/blacklist
trust extract --overwrite --format=pem-bundle \
  --filter='pkcs11:object=Comodo%20AAA%20Services%20root;type=cert' \
  $d/Comodo\_AAA\_Services\_root.pem &&
trust extract --overwrite --format=pem-bundle \
  --filter='pkcs11:object=emSign%20ECC%20Root%20CA%20-%20G3;type=cert' \
  $d/emSign\_ECC\_Root\_CA\_-\_G3.pem &&
update-ca-trust

On openSUSE and SLES, run as root:

d=/etc/pki/trust/blocklist; \[ -d $d \] || d=/etc/pki/trust/blacklist
trust extract --format=pem-bundle \
  --filter='pkcs11:object=Comodo%20AAA%20Services%20root;type=cert' \
  $d/Comodo\_AAA\_Services\_root.pem &&
trust extract --format=pem-bundle \
  --filter='pkcs11:object=emSign%20ECC%20Root%20CA%20-%20G3;type=cert' \
  $d/emSign\_ECC\_Root\_CA\_-\_G3.pem &&
update-ca-certificates

On Arch Linux, run as root:

trust extract --format=pem-bundle \
  --filter='pkcs11:object=emSign%20ECC%20Root%20CA%20-%20G3;type=cert' \
  /etc/ca-certificates/trust-source/blocklist/emSign\_ECC\_Root\_CA\_-\_G3.pem &&
update-ca-trust

On NixOS, add to your configuration:

security.pki.caCertificateBlacklist = \[
  "Comodo AAA Services root"
  "emSign ECC Root CA - G3"
\];

Microsoft has shipped blocks for these certificates through Windows' [automatic certificate trust list updates](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/certificate-trust#automatic-certificate-trust-list-updates). Machines that receive these updates don't need this workaround. This script lets administrators block the compromised certificates locally on machines that do not, for example those that are offline or have automatic updates disabled.

**This mitigation is not recommended for enterprise-managed devices.** Your IT department will manage the rollout; contact them before applying local changes.

Download and inspect `Block-EmudhraCompromisedCA.ps1` from the GitHub repository linked in the footer, then run it from an elevated PowerShell terminal. Requires PowerShell 5.1 or later and the built-in Windows PKI module. This command bypasses execution policy for this process only; it does not change the machine's policy. Organization-enforced policies may still prevent execution.

powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Block-EmudhraCompromisedCA.ps1

The script imports its 16 compromised intermediates and cross-signs into `LocalMachine\Disallowed` (Untrusted Certificates).

This mitigation applies to clients using the Windows operating system certificate trust stores and chain validation (including Schannel TLS and Authenticode). It adds blocks to Untrusted Certificates without modifying Trusted Root Certification Authorities. Applications using independent CA bundles still need their own updates.

Many Android devices have automatically received an update blocking the affected certificates via the Google Play services update channel.

On devices that have not received the updated blocklist, users may be able to disable the affected roots in the system trust store. Open Settings and search for **Trusted credentials**, which is often found under Security, then Encryption & credentials. In the **System** tab, tap each of the following certificates and choose **Disable**:

- **emSign ECC Root CA - G3**, listed under eMudhra Technologies Limited
- **AAA Certificate Services**, listed under Comodo CA Limited

The other eMudhra and Comodo certificates in the list are not affected and should be left enabled. Disabling AAA Certificate Services may cause errors on some websites that still chain to it. The roots can be re-enabled from the same screen once the device has received an update.

Some Android devices may not allow users to disable system-installed roots.

If you are using HarmonyOS 4.3 and earlier, you can disable system-installed roots in the same way as on other Android-based systems.

OpenHarmony-based HarmonyOS does not allow users to disable system-installed roots. No user-side workaround is available on these devices until the patched version ships.

On NetBSD 10 and later, run as root:

certctl untrust /usr/share/certs/mozilla/all/emSign\_ECC\_Root\_CA\_-\_G3.pem &&
certctl untrust /usr/share/certs/mozilla/all/Comodo\_AAA\_Services\_root.pem

On FreeBSD 14 or later, run the following commands as root:

cp /etc/ssl/certs/14bc7599.0 /usr/share/certs/untrusted/14bc7599.pem
cp /etc/ssl/certs/ee64a828.0 /usr/share/certs/untrusted/ee64a828.pem
certctl rehash

Site published by [Dennis Jackson](https://github.com/dennisjackson). This site is the work of [many contributors](https://github.com/galadran/we-have-a-problem.com/graphs/contributors) from the community. The source is on [GitHub](https://github.com/galadran/we-have-a-problem.com) and PRs are welcome. Licensed under the [Apache License, Version 2.0](https://github.com/galadran/we-have-a-problem.com/blob/main/LICENSE).
