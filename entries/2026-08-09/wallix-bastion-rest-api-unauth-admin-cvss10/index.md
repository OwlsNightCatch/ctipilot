---
schema: 1
kind: vulnerability
title: "WALLIX Bastion's REST API hands full appliance administration to an unauthenticated caller (CVSS 4.0 10.0) — the credential vault and session recordings included, with public technical details due in September"
headline: "An unauthenticated request to a PAM appliance's REST API yields product-administrator control of the vault it exists to protect"
summary: >
  CERT-FR relayed two WALLIX vulnerabilities to its constituency on 2026-08-06 that this pipeline had
  not covered. WSA-2026-07-0001 is a CVSS 4.0 base 10.0 authentication bypass in the WALLIX Bastion
  REST API: a remote, unauthenticated attacker with network access to the API endpoint — typically
  HTTPS/443 on any operational appliance, in any configuration — obtains full administrative
  privileges, and with them the Bastion's configuration, its vault of privileged credentials and its
  session recordings. Bastion 12.3.0–12.3.6 and 12.4.0 are affected; 12.3.7 and 12.4.1+ are patched
  and versions below 12.3.0 are not affected. WSA-2026-07-0002 (CVSS 4.0 8.7) lets an attacker with
  network access to an Access Manager portal's SAML Service Provider obtain an authenticated
  administrator session without valid credentials, reaching every target and credential that portal
  brokers. WALLIX states the reporting researchers intend to publish full technical details in
  September 2026, which puts a date on the window for patching quietly.
discovered_at: "2026-08-09T14:05:00Z"
event_date: "2026-08-06"
run_id: 2026-08-09T1315Z-audit
priority: high
immediate_action: null
tags: [vulnerabilities, auth-bypass, pre-auth, identity, patch-available, zero-click]
regions: [europe, switzerland, global]
sectors: [public-sector, finance, energy, telco]
entities: []
techniques: [T1190, T1555, T1136.001]
affected_products: ["WALLIX Bastion", "WALLIX Access Manager"]
cves: []
sources:
  - url: "https://www.wallix.com/support-services/alerts/"
    publisher: "WALLIX"
    date: "2026-07-20"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0974/"
    publisher: "CERT-FR / ANSSI"
    date: "2026-08-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A critical vulnerability has been identified in the WALLIX Bastion REST API. A remote, unauthenticated attacker with network access to the API endpoint can obtain full administrative privileges on the appliance."
    publisher: "WALLIX"
  - quote: "Successful exploitation grants complete control over the Bastion, including its configuration, its vault of privileged credentials, and its session recordings."
    publisher: "WALLIX"
  - quote: "Primary indicator — administrator creation performed by the internal service account identity. A session obtained through this vulnerability acts as an internal service account principal from the loopback address."
    publisher: "WALLIX"
verification: multi-source
sourcing_note: >
  The vendor is the sole assessor: CERT-FR's advisory relays WALLIX's bulletin and adds the affected
  Access Manager version boundaries, but contributes no independent analysis, so credibility stays at
  2 — one assessor, two publishers. Neither flaw carries a CVE identifier on either page, so `cves[]`
  is empty and the vendor's WSA identifiers are the tracking handles. The vendor bulletin is dated
  2026-07-20, seventeen days before this window; the in-window event is CERT-FR's 2026-08-06 relay,
  which is also the first time this pipeline's constituency was reached, and the September disclosure
  commitment is what makes the timing operational rather than historical.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
classification:
  reliability: A
  credibility: 2
actions:
  - "Inventory every WALLIX Bastion and move any instance on 12.3.0–12.3.6 or 12.4.0 to 12.3.7 or 12.4.1+; the flaw needs no credentials and no configuration to be present, so an operational appliance on an affected build is exposed by existing at all."
  - "On any Bastion that ran an affected build while reachable, grep /var/log/wabaudit.log (and the SIEM copy) for state-changing actions carrying client_ip=\"127.0.0.1\" — above all an action=\"add\" of type \"User\" creating a product_administrator — and treat a hit as vault compromise, not just appliance compromise."
---

Privileged-access management appliances concentrate exactly what an intruder wants, which is why a pre-authentication path to administrator on one is a different class of problem from the same bug on an ordinary web application. WALLIX's WSA-2026-07-0001 is that path: the vendor describes a REST API authentication layer that "can be induced to grant a privileged administrative session without valid credentials", classed CWE-290 (authentication bypass by spoofing) and CWE-287, scored CVSS 4.0 base 10.0 with the vector `AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H` ([WALLIX, 2026-07-20](https://www.wallix.com/support-services/alerts/)). The vendor is explicit that no precondition narrows the exposure — the flaw "affects any operational Bastion 12.3 and 12.4.0 in any configuration" and "requires no authentication, no user interaction, and no special settings" — and that what exploitation yields is the vault: "complete control over the Bastion, including its configuration, its vault of privileged credentials, and its session recordings" ([WALLIX, 2026-07-20](https://www.wallix.com/support-services/alerts/)). The affected code path entered the 12.3 branch, so 12.0.x and anything below 12.3.0 is unaffected; 12.3.7 and 12.4.1 and higher carry the fix.

The second flaw sits one layer out. WSA-2026-07-0002 (CVSS 4.0 base 8.7, `AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:H/VA:L/SC:L/SI:L/SA:N`) is an authentication bypass in the Access Manager portal's SAML Service Provider that yields an authenticated administrator session without valid credentials. WALLIX is careful about the blast radius: because the Access Manager brokers access to a fleet of Bastions, that session reaches the targets and privileged credentials the portal is configured to broker, but it does not confer administration of the Bastions themselves ([WALLIX, 2026-07-20](https://www.wallix.com/support-services/alerts/)). CERT-FR's advisory adds the version boundaries that matter for the portal: Access Manager with SAML federation configured is affected below 5.1.10, in 5.2.x below 5.2.7, and in 6.x below 6.0.4 ([CERT-FR, 2026-08-06](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0974/)). Where upgrading the portal cannot happen immediately, WALLIX names partial fencing — disabling or removing SAML federation domains not in active use, and removing or renaming Administrator-type profiles on organisations that need SAML — while stating plainly that these "reduce risk but do not fully close the flaw" ([WALLIX, 2026-07-20](https://www.wallix.com/support-services/alerts/)).

What makes this urgent rather than merely severe is a clock the vendor set itself. WALLIX withholds the exploitation mechanics deliberately — "Technical exploitation details are intentionally withheld to protect customers until patch adoption is sufficiently widespread" — but states that the independent researchers who reported the flaws "intend to publish full technical details in September 2026", after which "information useful to attackers will be in the public domain" ([WALLIX, 2026-07-20](https://www.wallix.com/support-services/alerts/)). Neither the vendor nor CERT-FR makes any statement either way about exploitation to date, and the advisory is pointed about why that silence is not reassurance: it tells customers to treat affected appliances as potentially compromised and warns that "Absence of evidence must not be interpreted as absence of compromise" ([WALLIX, 2026-07-20](https://www.wallix.com/support-services/alerts/)). A CVSS 10.0 unauthenticated bypass on an appliance class that is routinely internet-reachable, with a published disclosure date, is the shape where what is known today says little about next month.

One version boundary is worth pre-empting, because the advisory contradicts itself on it. Its affected-products table marks Bastion 12.3.7 as Patched alongside 12.4.1 and higher, and CERT-FR's advisory independently scopes the flaw to "Bastion versions 12.3.x antérieures à 12.3.7" ([CERT-FR, 2026-08-06](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0974/)) — but the vendor's own remediation section says "Upgrade to WALLIX Bastion 12.4.1 or higher. This is the only effective remediation" ([WALLIX, 2026-07-20](https://www.wallix.com/support-services/alerts/)). Two sources agree the 12.3.7 hotfix closes it; a reader who patches to 12.3.7 and then reads that sentence should know the disagreement is in the vendor's own document.

Detection is unusually tractable here because the vendor named the artefact rather than an indicator. State-changing operations on the Bastion — creating or editing users, changing configuration — are written to `/var/log/wabaudit.log` and forwarded to a SIEM where one is configured, in a structured line carrying `action`, `type`, `object`, `user`, `client_ip` and the changed fields ([WALLIX, 2026-07-20](https://www.wallix.com/support-services/alerts/)). **Triage:** a session obtained through this flaw acts as an internal service account principal from the loopback address, so the discriminator is the actor/address pair rather than the action — a state-changing `add`, `edit` or `delete` recorded with `client_ip="127.0.0.1"`, and above all a `type="User"` creation granting the `product_administrator` profile. Legitimate administrator actions are never recorded that way, because a real administrator reaches the appliance over the network from an identifiable client address. Any administrator account whose creation carries that pair is attacker-created regardless of how plausible its name looks.

**Defender takeaway:** treat an affected, reachable Bastion as potentially compromised rather than merely vulnerable — the vendor says so itself — which makes the work post-patch as important as the patch. Every credential the vault brokered while the appliance ran an affected build is a credential an unauthenticated caller could have read, and unlike a session token those do not expire when the appliance is upgraded. Rotation of the brokered secrets, not just the upgrade, is what closes the exposure.
