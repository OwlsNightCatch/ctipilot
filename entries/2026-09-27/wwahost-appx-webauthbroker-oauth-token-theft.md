---
schema: 1
kind: research
title: "A sideloaded AppX package turns a Microsoft-signed web host into an OAuth token thief: the login dialog is genuine, the MFA is genuine, and the tokens go to the attacker"
headline: "Huntress: attacker JavaScript in a signed Windows AppX host drives Microsoft's own OAuth broker, so a genuine login yields MFA-surviving refresh tokens"
summary: >
  Huntress documents a post-compromise token-theft technique with no phishing page and no
  lookalike domain. An AppX package whose manifest declares WindowsRuntimeAccess="all" gives
  attacker-hosted JavaScript the full Windows Runtime surface inside a Microsoft-signed host
  process, including the legacy WebAuthenticationBroker. The JavaScript opens a genuine
  login.microsoftonline.com dialog using Microsoft Office's own first-party client ID and an
  out-of-band redirect, so the authorization code returns to the attacker rather than a browser.
  The user authenticates and completes MFA normally; the resulting refresh token keeps minting
  access tokens from any network until it is revoked. The prerequisite is Developer Mode or an
  enterprise sideloading policy; after that no admin rights, UAC prompt, SmartScreen check or
  code signature is involved.
discovered_at: "2026-09-27T13:28:04Z"
updated_at: null
event_date: "2026-09-23"
run_id: 2026-09-27T1308Z-audit
priority: notable
immediate_action: null
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
tags: [identity, cloud, info-disclosure]
regions: [global]
sectors: [public-sector]
entities: ["product:microsoft-windows", "product:microsoft-entra-id"]
techniques: [T1218, T1550.001, T1528]
affected_products: ["Microsoft Windows", "Microsoft Entra ID"]
cves: []
classification:
  reliability: B
  credibility: 2
sources:
  - url: "https://www.huntress.com/blog/stealing-oauth-tokens-through-microsofts-front-door"
    publisher: "Huntress"
    date: "2026-09-23"
    role: primary
closed_sources: []
evidence:
  - quote: "and the remote JavaScript it renders doesn't just run, it inherits the full Windows Runtime API surface, including the API that drives OAuth sign-in"
    publisher: "Huntress"
  - quote: "The user does everything right and it changes nothing"
    publisher: "Huntress"
  - quote: "It is, in effect, the victim's entire Microsoft 365 working life in one token, and unlike the session it was stolen from, it keeps working from anywhere until the refresh token is revoked."
    publisher: "Huntress"
  - quote: "No modern browser produces that string."
    publisher: "Huntress"
verification: single-source
sourcing_note: "Single technical source (Huntress original research, tested end to end by its author against a live Entra ID tenant with MFA enabled). No second party has published an independent assessment of this specific chain, and the researcher deliberately withholds the working manifest and the enumeration of other affected host binaries, so the surrounding claims about the wider host class are stated at the strength the author gives them. Recovered by the 2026-09-27 quality audit's research re-sweep after the week's fires did not surface it."
confidence: medium
actions:
  - "Turn Developer Mode off fleet-wide by GPO and scope any enterprise sideloading policy away from AllowAllTrustedApps: that toggle is the single prerequisite the whole chain needs, and without it package registration fails closed."
references: []
migrated_from: null
updates: []
---

Huntress researcher Andrew Schwartz went looking for a Microsoft-signed binary already present on every Windows machine that would fetch remote code and run it, and found the AppX web-host family ([Huntress, 2026-09-23](https://www.huntress.com/blog/stealing-oauth-tokens-through-microsofts-front-door)). `WWAHost.exe`, the Windows Web App Host, renders whatever web content an AppX package points it at. The manifest flag is what turns that into an attack: when a package's `ContentUriRules` entry carries `WindowsRuntimeAccess="all"`, the remote JavaScript loaded from that origin "doesn't just run, it inherits the full Windows Runtime API surface, including the API that drives OAuth sign-in" ([Huntress, 2026-09-23](https://www.huntress.com/blog/stealing-oauth-tokens-through-microsofts-front-door)). The API in question is the legacy `WebAuthenticationBroker`, which Microsoft has steered developers away from in favour of the Web Account Manager but which remains present and reachable from inside the AppX host.

The chain is short. A standard user registers a minimal sideloaded package with `Add-AppxPackage -Register`; attacker JavaScript then calls `WebAuthenticationBroker.authenticateAsync()` with Microsoft Office's own first-party client ID and the `urn:ietf:wg:oauth:2.0:oob` redirect URI, which is the part that matters, because an out-of-band redirect returns the authorization code to the calling application rather than to a browser. The user sees a real Microsoft sign-in dialog served from login.microsoftonline.com, rendered by a signed Microsoft process with no address bar and no browser chrome, completes the password and the MFA prompt, and the code lands in the attacker's listener to be exchanged for an access token and a refresh token. Huntress's summary of the victim's position is the whole point of the technique: "The user does everything right and it changes nothing" ([Huntress, 2026-09-23](https://www.huntress.com/blog/stealing-oauth-tokens-through-microsofts-front-door)).

The prerequisite is the constraint. Registration fails with `0x80073CFF` unless Developer Mode is enabled or an enterprise sideloading policy is in force, and enabling Developer Mode itself requires local administrator rights. Huntress is explicit that the enterprise `AllowAllTrustedApps` path is the more likely way a managed fleet ends up in the vulnerable state at scale, and notes Developer Mode is common on development machines, CI/CD runners and cloud VMs. Past that one toggle, the remaining steps run as a standard user with no further admin, no UAC prompt, no SmartScreen check and no code-signing requirement. The technique is therefore post-compromise or post-social-engineering, not an initial-access vector on its own.

What the tokens carry is what makes it worth the effort. The captured token arrived with the delegated scope set attached to Microsoft Office's client ID, spanning mail read, write and send, files across OneDrive and SharePoint, the Teams surface including channels, chats, messages and membership, directory and group read and write, and calendar and contacts, plus `AuditLog.Create`, which Huntress singles out as an unexpected capability with obvious value for muddying an investigation. Because these are delegated scopes, the effective power is the intersection of the scope and what the signed-in user could already do, so the blast radius scales with the victim's own privilege rather than granting tenant administration automatically. Huntress states the consequence plainly: "It is, in effect, the victim's entire Microsoft 365 working life in one token, and unlike the session it was stolen from, it keeps working from anywhere until the refresh token is revoked." New access tokens were obtained hours later from a different machine on a different network with no re-authentication and no MFA prompt; the refresh token survives password changes until an administrator revokes it, a revocation event fires, or Continuous Access Evaluation intervenes.

The defensive framing Huntress argues for is a class, not a binary. `WWAHost.exe` is the one host proven end to end, but the reachable surface lives in the shared Windows Runtime activation layer that every AppX host loads, and the set of hosts varies by Windows build, with at least one shipping from the packaged store rather than a system directory so that an inventory searching only system directories under-counts. "That is why patching individual binaries won't fix the problem, and why an EDR rule for `WWAHost.exe` alone is futile" ([Huntress, 2026-09-23](https://www.huntress.com/blog/stealing-oauth-tokens-through-microsofts-front-door)). The researcher deliberately publishes neither the working manifest nor an enumeration of the other hosts, and separates what was proven end to end (token theft via the OAuth broker, on Windows 11 24H2 build 26100) from what was only shown to be reachable: a native credential dialog returning plaintext credentials, DPAPI operations in the user's own key context, and protocol-handler launching, all demonstrated on an earlier build and not re-confirmed. A silent, no-interaction variant of the broker call is described as documented and expected behaviour that the author did not confirm, and should be read as an open avenue rather than a result.

**Detection:** endpoint and identity telemetry come up empty by design here, because the process is Microsoft-signed, the endpoint is Microsoft's, and the client ID is Microsoft Office's. The network leg is what separates the two. Every AppX web host renders through the legacy EdgeHTML engine, which announces itself in the user agent as `MSAppHost/3.0` paired with `Edge/18`; Chromium-based Edge retired EdgeHTML years ago, so "No modern browser produces that string" ([Huntress, 2026-09-23](https://www.huntress.com/blog/stealing-oauth-tokens-through-microsofts-front-door)). Proxy and egress logs carrying that user agent to any destination outside Microsoft-owned infrastructure are the signal, and because the rule keys on the shared rendering engine rather than a host binary name, it covers the whole class. On the endpoint, package-registration events for AppX packages that no software-distribution system deployed are the complementary tell, as is the state of the Developer Mode registry value across the fleet. In Entra ID sign-in logs the record looks like a routine Office desktop sign-in with no risk flags, and the one field that differs is the user agent Microsoft itself records for the authentication leg, `MSAuthHost` on the Trident engine rather than `MSAppHost/3.0`, which is a reason to correlate the identity and network sides rather than to rely on either alone.

**Triage:** `MSAppHost/3.0` reaching Microsoft-owned infrastructure is ordinary AppX behaviour and not a finding; the same user agent reaching an origin outside Microsoft is what has no benign explanation. Likewise, an Office sign-in from a managed device is unremarkable on its own, so the discriminator is the pairing: a successful Office-client-ID sign-in on a host that also produced outbound EdgeHTML-engine traffic to a non-Microsoft origin in the same window.

**Defender takeaway:** the prerequisite toggle is the whole control surface, so audit where Developer Mode and enterprise sideloading are enabled and remove them where they are not needed; treat developer workstations, build runners and cloud VMs as the population that most likely carries them. Where a token is suspected stolen, a password reset is not a remedy: revoke the user's refresh tokens explicitly, because the stolen token keeps working from any network until revocation, a revocation event, or Continuous Access Evaluation ends it.
