---
schema: 1
kind: threat
horizon: operational
title: "An intruder used pam_rootok to move between low-privileged identities as a deliberate forensic smokescreen — inverting what a responder infers from the authentication trail"
headline: "Root escalated once, then spent the intrusion impersonating ordinary users so the audit trail would look ordinary"
summary: >
  Group-IB's DFIR team documents a May 2026 covert Monero-mining intrusion whose defining feature is
  anti-forensics rather than the miner. Initial access came through a trusted third-party
  relationship. After escalating to root the actor abused the pam_rootok policy — which lets root use
  su without a password — to assume the identities of multiple low-privileged users, deliberately
  avoiding the root-level activity that raises SOC alerts, and planted redundant cron persistence
  across those unmonitored accounts so remediating the root compromise alone would let the implant
  regenerate. Core logging services were stopped and authentication logs tampered with, and the
  binary self-deletes after establishing a mutex, continuing to run from memory.
discovered_at: "2026-08-10T04:47:00Z"
event_date: "2026-07-30"
run_id: 2026-08-10T0411Z-intel
priority: notable
immediate_action: null
tags: [cryptocrime, organized-crime, supply-chain, botnet]
regions: [global, europe]
sectors: [public-sector, technology]
entities: [campaign:groupib-xmrig-pam-forensic-smokescreen]
techniques: [T1199, T1556.003, T1685.006, T1053.003, T1027.011, T1036.005]
affected_products: []
cves: []
sources:
  - url: "https://www.group-ib.com/blog/xmrig-covert-linux-pam-abuse/"
    publisher: "Group-IB"
    date: "2026-07-30"
    role: primary
closed_sources: []
evidence:
  - quote: "Initial access was achieved by exploiting a trusted third-party relationship, highlighting critical supply chain risks."
    publisher: "Group-IB"
  - quote: "By distributing their malicious activities and planting redundant cronjob persistence across various unmonitored standard accounts, the attackers ensured that if SOC analysts only remediated the root compromise, the botnet implant would simply regenerate from the shadowed accounts."
    publisher: "Group-IB"
  - quote: "Immediately after establishing this mutex, the malware performs a self-unlink operation. By deleting its own binary file from the disk while the process remains active, the malware transitions into a fileless state, running entirely from memory (RAM)."
    publisher: "Group-IB"
  - quote: "Alerts should be triggered immediately if root is observed rapidly transitioning into standard user accounts (USER_START events associated with pam_rootok)."
    publisher: "Group-IB"
  - quote: "The malware natively supports process masquerading via the custom -h flag, allowing it to spoof legitimate process names such as \"ssh\" in ps, top, and /proc/<pid>/comm outputs."
    publisher: "Group-IB"
verification: single-source
sourcing_note: >
  Single originating incident-response publication with no second-party corroboration of this
  intrusion. The technique described is a documented property of a standard PAM module rather than a
  novel vulnerability, which is what makes the account plausible on its own; credibility is 2 because
  nothing independent confirms the engagement.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Group-IB's incident-response team has published a May 2026 intrusion whose interesting half is not the cryptominer it ended in but the reasoning behind how the operator moved ([Group-IB, 2026-07-30](https://www.group-ib.com/blog/xmrig-covert-linux-pam-abuse/)). Initial access "was achieved by exploiting a trusted third-party relationship" — a standard user account inherited from a trusted environment — after which the actor escalated to root.

At that point the operator did something most intrusions do not: it stopped acting like root. Group-IB records that the attacker abused the `pam_rootok` policy so that `su` would assume the identities of multiple low-privileged users across the system without needing their passwords. `pam_rootok` is a legitimate, widely shipped PAM module whose entire purpose is to let the root user authenticate as anyone without a credential — nothing was exploited to make it work. What it buys the attacker is that the actions which follow appear in the authentication and audit trail as ordinary users doing ordinary things, rather than as root, which is the activity class a SOC alerts on.

The persistence design follows the same logic. Redundant cron jobs were planted across those low-privileged, unmonitored accounts, so that — in Group-IB's words — "if SOC analysts only remediated the root compromise, the botnet implant would simply regenerate from the shadowed accounts." That is an explicit bet against the standard remediation instinct of fixing the privileged account and closing the case. Alongside it, core logging services were stopped and authentication logs tampered with, and the payload unlinks its own binary immediately after taking a mutex, so it "transitions into a fileless state, running entirely from memory (RAM)."

The transferable point for this constituency is about inference, not about miners. A responder reading an authentication trail normally treats a session under a low-privileged account as evidence of limited privilege; here that inference is exactly backwards, and the identity in the log is a costume. Any Linux estate reached through a supplier or managed-service relationship — the initial-access shape Group-IB names — inherits the same exposure.

Detection, telemetry class first. Group-IB names the anchor itself: authentication and audit records showing root rapidly transitioning into standard user accounts, specifically session-start events associated with `pam_rootok`, should alert. Two supporting classes matter as much. Service-state telemetry showing the system logging or auditing daemon stopping or being modified without a corresponding change record is a signal in its own right rather than a maintenance artefact, which is why forwarding to an external, tamper-resistant collector in real time is what preserves the evidence at all. And scheduled-job telemetry across *ordinary* user accounts — not just privileged ones — is where the redundant persistence lives. **Triage:** administrators legitimately use `su` to operate as service accounts, and cron jobs under application accounts are normal; the discriminator is direction and tempo — root descending into several unrelated low-privileged identities in quick succession, with no corresponding administrative task, followed by new cron entries under those same accounts. A single `su` is noise; the fan-out is the signal. **Defender takeaway:** scope a Linux root compromise as a compromise of every account on the host, and hunt persistence under unprivileged accounts before declaring eviction — the design here assumes you will not.
