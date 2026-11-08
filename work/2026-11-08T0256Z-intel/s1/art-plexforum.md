---
title: Important Security Update for Plex Media Server v1.43.2 and earlier
author: PlexInfo
url: https://forums.plex.tv/t/important-security-update-for-plex-media-server-v1-43-2-and-earlier/942319/3
hostname: plex.tv
description: "Update: CVE details and active exploitation As promised in the original post, here are the CVE details for the issues fixed in Plex Media Server 1.43.3. ┌────────────────┬─────────────────────────────────────────────────────────────────────────────┐ │ CVE │ Summary │ ├────────────────┼─────────────────────────────────────────────────────────────────────────────┤ │ CVE-2026-96652 │ Unauthenticated server-side..."
sitename: Plex Forum
date: "2026-10-19"
tags: ['server-windows', 'player-linux', 'server-linux']
fingerprint: "952ae75399e30f86"
---
**Update: CVE details and active exploitation**

As promised in the original post, here are the CVE details for the issues fixed in Plex Media Server 1.43.3.

```
  ┌────────────────┬─────────────────────────────────────────────────────────────────────────────┐
  │      CVE       │                                   Summary                                   │
  ├────────────────┼─────────────────────────────────────────────────────────────────────────────┤
  │ CVE-2026-96652 │ Unauthenticated server-side request forgery in the player timeline endpoint │
  ├────────────────┼─────────────────────────────────────────────────────────────────────────────┤
  │ CVE-2026-96654 │ Access to internal agent functions over the loopback interface              │
  ├────────────────┼─────────────────────────────────────────────────────────────────────────────┤
  │ CVE-2026-96655 │ Disclosure of the server owner's admin token                                │
  ├────────────────┼─────────────────────────────────────────────────────────────────────────────┤
  │ CVE-2026-96656 │ Arbitrary file write to the Codecs directory through transcoder preferences │
  └────────────────┴─────────────────────────────────────────────────────────────────────────────┘
```
Chained together, these issues let an unauthenticated remote attacker run code with the privileges of the Plex Media Server process. Plex Media Server 1.43.3.10861 and later are not affected.

These vulnerabilities are being actively and widely exploited. A public proof of concept was released on October 16.

Since then, we’ve seen widespread attacks against internet-facing servers that haven’t been updated. Compromised servers have been used to run cryptocurrency miners and proxy software, which routes other people’s traffic through the victim’s internet connection.

If your server is older than 1.43.3.10861 and reachable from the internet, assume it may be compromised.

What you should do

1. Update now. Make sure your server is on 1.43.3.10861 or newer: open Plex Web, go to Settings → General, and check the version shown. Update instructions for each platform are in the original post above.
2. Check for signs of compromise:
  - Processes started by Plex Media Server that you don’t recognize, especially names like myawesomeproxy, mylovelyminer or x12345.
  - Unfamiliar .so or .dll files in the Plex Codecs folder.
  - Outbound connections to proxystream.st, or sustained high CPU use while nothing is playing.
3. If you find any of these, or you can’t rule out compromise:
  - Rebuild the server from a clean installation rather than reusing the old Plex data directory. At minimum, delete everything in the Codecs folder and check Preferences.xml for transcoder options you didn’t set.
  - Sign out of all devices from your Plex account settings, and change your Plex password.
  - Treat anything the Plex service account could reach as potentially exposed, such as mounted shares and credentials stored on the same machine or VM.
4. If you don’t need remote access, turn it off under Settings → Remote Access. Avoid forwarding port 32400 directly unless you need it.
