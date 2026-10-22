---
schema: 1
kind: threat
title: "NCSC-CH Week 23: three job-seeker scams, a fake interview login, reshipping identity theft and LinkedIn-to-GitHub infostealer delivery"
headline: "NCSC-CH Week 23: three job-seeker scams, a fake interview login, reshipping identity theft and LinkedIn-to-GitHub infostealer delivery"
summary: "NCSC Switzerland's Week 23 review (9 June) describes three reported cases aimed at job seekers: an interview slot confirmed through a Google Calendar entry that opens a counterfeit Google login and harvests the credentials, a fake \"Swiss social welfare\" packing job that collects identity documents for reshipping and purchase fraud, and a fake LinkedIn recruiter whose technical interview has the candidate run a small programming task from a private GitHub repository, which installs an infostealer."
discovered_at: "2026-06-10T05:00:02Z"
event_date: 2026-06-09
run_id: 2026-06-10-c84347b2
priority: notable
immediate_action: null
tags:
  - phishing
  - infostealer
  - identity
  - organized-crime
regions:
  - switzerland
sectors: []
entities:
  - "campaign:ncsc-ch-jobseeker-targeting-2026"
techniques: [T1566.002, T1566.003, T1586.001, T1684.001, T1204.002, T1555, T1539, T1005]
cves: []
sources:
  - url: "https://www.bacs.admin.ch/en/26w23-en"
    publisher: "NCSC-CH, 2026-06-09"
    role: primary
closed_sources: []
evidence: []
verification: single-source-national-cert
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T06:43:01Z"
    run_id: 2026-09-30T0634Z-audit
    type: correction
    summary: >
      NCSC presents three reported cases rather than a coordinated campaign, and none of the
      Swiss-employer emails, onboarding repository or PowerShell the analysis described, so the title,
      summary and analysis now follow the page. The citation follows the page to its new address on
      bacs.admin.ch.
    fields: [sources, techniques, classification, title, headline, summary, sectors, body]
  - at: "2026-10-11T14:02:54Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    internal: true
    summary: >
      Relabels the closing line as the Defender takeaway, the label the rest of the store uses; its text is unchanged.
    fields: [body]
  - at: "2026-10-21T08:21:59Z"
    run_id: 2026-10-21T0800Z-audit
    type: improvement
    summary: >
      The analysis gains Exposure, Detection and Triage lines for the LinkedIn-to-GitHub infostealer case,
      and the takeaway now says what to do with a device where the interview task ran. An unsourced claim
      that HR or talent teams handling candidate code are a vector is dropped, and the impersonated
      recruiter and the collection of wallet files are mapped.
    fields: [body, techniques]
migrated_from: briefs/2026-06-10.md
---

NCSC Switzerland's Week 23 review (9 June) walks through three reported cases aimed at job seekers ([NCSC-CH, 2026-06-09](https://www.bacs.admin.ch/en/26w23-en)). In the first, a job seeker was offered a phone-interview slot to confirm through a Google Calendar entry, and the confirmation opened a counterfeit Google login that sent the entered credentials to the scammers. In the second, an ad for a "Swiss social welfare" work-from-home packing job moved to WhatsApp and asked for photos of the passport, identity card, driving licence and home address. Such documents are used to order high-value goods in the victim's name, and the job itself is parcel reshipping that hides criminal proceeds. In the third, a recruiter on LinkedIn, in one case writing from a compromised but genuine-looking profile, offered a technical position and, as part of a technical interview, asked the candidate to download a private GitHub repository and complete a small programming task in it. Running the commands installed an infostealer that reads crypto wallets, stored login credentials and browser cookies. NCSC notes that attackers systematically exploit applicants' willingness to react quickly and engage with unfamiliar procedures.

**Exposure:** job seekers, and in the third case an IT professional approached on LinkedIn about a technical position, in a similar case from a compromised but genuine-looking profile ([NCSC-CH, 2026-06-09](https://www.bacs.admin.ch/en/26w23-en)). In analyst judgement an employee in job-search mode who runs such a task on a work device brings the infostealer into the corporate estate, and NCSC notes that the incident becomes particularly serious where sensitive documents are stored on the device ([NCSC-CH, 2026-06-09](https://www.bacs.admin.ch/en/26w23-en)).

**Detection:** by inference from the mechanism, process-creation telemetry with parent lineage showing a freshly downloaded or cloned repository followed within minutes by script or interpreter execution from that path (for example Sysmon event 1 with `git` or an interpreter as the parent), then a non-browser process reading browser credential and cookie stores or crypto-wallet files, the data NCSC says the infostealer took ([NCSC-CH, 2026-06-09](https://www.bacs.admin.ch/en/26w23-en)).

**Triage:** downloading a repository and running its commands is common in IT work, which is why the step raised no suspicion ([NCSC-CH, 2026-06-09](https://www.bacs.admin.ch/en/26w23-en)); by inference from the mechanism, the discriminators are the repository's origin, a private repository handed over by an external recruiter during an interview, and what follows execution, reads of credential, cookie or wallet stores by a process that is not the browser.

**Defender takeaway:** treat a device on which the interview task ran as having lost its stored login credentials, browser cookies and crypto wallets, the data the infostealer reads ([NCSC-CH, 2026-06-09](https://www.bacs.admin.ch/en/26w23-en)): revoke the sessions and rotate every credential stored on it, not only the password the user typed, since a stolen cookie carries a live session.

## Correction — 2026-09-30T06:43:01Z

NCSC Switzerland's Week 23 review presents three reported cases, not a coordinated campaign ([NCSC-CH, 2026-06-09](https://www.bacs.admin.ch/en/26w23-en)). The fake interview was a phone-interview slot confirmed through a Google Calendar entry, which opened a counterfeit Google login. The recruiter case was a technical interview in which the candidate downloaded a private GitHub repository and ran a small programming task, and running its commands installed the infostealer. The analysis had described interview-confirmation emails from Swiss employers, an onboarding or technical-assessment repository and PowerShell, which the page does not say, and it now follows the page. The citation now points at the page's new address on bacs.admin.ch, after the old ncsc.admin.ch page went dead.

## Improvement — 2026-10-21T08:21:59Z

Downloading a repository and running its commands is common in IT work, which is why the interview task raised no suspicion; once run, the infostealer secretly reads crypto wallets, stored login credentials and browser cookies, and NCSC notes the incident becomes particularly serious where sensitive documents are stored on the device ([NCSC-CH, 2026-06-09](https://www.bacs.admin.ch/en/26w23-en)). A device where the task ran should therefore be treated as having lost its stored credentials and live sessions, and the sessions need revoking along with the passwords.
