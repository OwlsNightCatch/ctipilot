---
title: "Meet the GoodGuys: a fake expert interview phishing campaign"
author: Luke Jennings
url: https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown
hostname: pushsecurity.com
description: Push researchers are tracking a live AiTM phishing campaign that sends paid "expert interview" and webinar invitations.
sitename: Push Security
date: "2026-11-20"
categories: ['Threat research']
tags: ['AiTM phishing', 'AI attacks', 'Legitimate service abuse', 'Social engineering', 'Identity attacks', 'MFA bypass', 'Browser attacks', 'Phishing', 'Threat landscape']
fingerprint: "23a1e9590067bfa9"
language: en
image: https://pushsecurity.com/_og/s/o_cf4067a1ce5bfe99.png
pagetype: article
filedate: "2026-11-25"
---
Inside a new phishing campaign we're tracking that sends paid "expert interview" and webinar invitations impersonating big brands, including Accenture, Nvidia, SpaceX, and Google Cloud.

Push researchers are tracking a live phishing campaign that sends paid "expert interview" and webinar invitations impersonating big brands, including Accenture, Nvidia, SpaceX, and Google Cloud. The pages we've observed target work Google accounts, and the code also includes a fake Okta sign-in. We're calling it **GoodGuys**, after a hidden "GoodGuys sign-in simulation" label in every build. We think the label is a leftover from tricking an AI coding assistant past its safeguards when the kit was first built.

Indicators of compromise are provided at the end of the post.

## [Attack breakdown](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-attack-breakdown)

GoodGuys is a Vite and React web app with three screens: a captcha gate, a brand landing page, and a fake Google sign-in. Every value the victim enters goes to a separate backend host, which tells the page which screen to show next.

### [Lures and delivery](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-attack-breakdown_id-lures-and-delivery)

Each GoodGuys lure invites the recipient to a paid interview, a feedback study, or a private briefing from a well-known brand. The Accenture page offers $600 for a 45-minute expert interview, and the Nvidia page offers $500 for a 45-minute "AI Experience & Feedback Study." Every build carries the same page description: "Share your expertise with \<Brand> through a short paid expert interview."

One lure email we intercepted invited the recipient to a Google Cloud webinar. It came from interviews@hirevue\[.\]com. The email describes a session on moving AI applications into production and links to "View webinar details." That link leads to the Google Cloud skin of the kit.

Other lures reached recipients through legitimate email and event services whose accounts or link tracking the attackers had access to. We've seen click URLs from SendGrid accounts, Mandrill, Cvent, Commerce7, Phorest, Wellyx, Weave, and a click tracker on a Culver's domain. One chain went through Truescope's link tracker to a redirect page hosted on Amazon S3. Abusing legit email services, click-tracking, and link shorteners is a common way that attackers bypass sender authentication checks.

### [Captcha gate](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-attack-breakdown_id-captcha-gate)

Most skins open with a branded reCAPTCHA card which can escalate to an image challenge. The Google Cloud build copies Google's own "Our systems have detected unusual traffic from your computer network" page instead.

The page reports to the backend when the captcha is solved and sends a visitor record with the value captcha\_passed.

### [Branded landing pages](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-attack-breakdown_id-branded-landing-pages)

We've seen GoodGuys domains for eight brands: Accenture, American Express, Coca-Cola, Culver's, Google Cloud, Nvidia, SpaceX, and Spotify. Each brand gets its own landing page, built to make a work sign-in look like a normal step. You can see a selection of captures below.

The SpaceX skin copies the "Starship Product Briefing" lure from the [fake event campaign](https://pushsecurity.com/blog/ai-themed-fake-event-campaign-analysis) that Push analyzed on November 5. It keeps the same "3 months of Grok Heavy" and "SpaceX share" rewards and the same work account requirement. The kits and hosting behind the two pages are different, so we think the GoodGuys operators cloned the lure.

### [Mismatched page titles](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-attack-breakdown_id-mismatched-page-titles)

The page titles and descriptions don't always match the skins. That points to sloppy work when the operators moved the kit between brands and deployments. For example:

- The earliest captures, on paid-interview-portal\[.\]com, ran the Accenture and Spotify builds under the title "Expert Interviews | WPP Media."
- The Google Cloud build still carries the SpaceX build's wording in its page description. The operators clearly made it from a copy of the SpaceX skin and didn't finish the edit.
- The Culver's build's title is just "Expert Interviews," with no brand name. The other interview builds add the brand after the title, as in "Expert Interviews | Accenture."

### [Fake Google sign-in](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-attack-breakdown_id-fake-google-sign-in)

The fake sign-in page is a typical Google clone that is branded to remain consistent with the lure. The kit accepts only work accounts. Its fake Google sign-in rejects Gmail, Yahoo, and Outlook addresses with the message "Enter a work email address."

**Why the GoodGuys?** The sign-in card in every build carries two hidden labels: "Sign-in simulation" and "GoodGuys sign-in simulation." They sit in accessibility text that only screen readers announce, so a visitor never sees them. We think the label is a leftover from how the kit was first built. Calling the page a sign-in "simulation" for a made-up company is the kind of framing someone would use to get an AI coding assistant past its guardrails when asking it to build a phishing page. The label then stayed in every build we've collected.

## [How the sign-in gets relayed](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-how-the-sign-in-gets-relayed)

GoodGuys doesn't use a reverse proxy. The fake page handles the email and password steps itself and sends both to the attacker's backend. After the password, it shows a "Loading next step" bar and waits until the backend says which screen comes next. That might be an SMS or authenticator prompt, a "Wrong password" error, the Okta sign-in, or the end screen. The commands look built for a person at a control panel, so we think an operator replays each value against the real Google or Okta sign-in and asks the victim for whatever it asks for next. To the victim, the steps look the same as a normal Google sign-in.

Learn more about the different AiTM mechanics and techniques in our post on [the evolution of AiTM attacks in 2026](https://pushsecurity.com/blog/aitm-phishing-dom-mirroring).

The kit splits the work between two servers. The landing host only delivers the page to the victim. Everything the victim types goes to a separate backend server, and the operator's instructions come back to the page from that server over a live socket.io connection.

Once the sign-in screen loads, the page opens a socket.io channel to the backend. It sends register {role:"client", session} and waits for command {cmd, payload} messages. The client role suggests the backend also has an operator role and a panel.

| Operator command | What the victim sees | 
|---|---|
| Operator command: login\_error, password\_error | What the victim sees: "Couldn't find this account" or "Wrong password" on the Google screen | 
| Operator command: phone\_number | What the victim sees: A prompt to confirm the phone number on the account | 
| Operator command: sms\_code, sms\_code\_error | What the victim sees: A prompt for the 6-digit code sent by text | 
| Operator command: auth\_code, auth\_code\_error | What the victim sees: A prompt for the Google Authenticator code | 
| Operator command: tap\_code | What the victim sees: A 2-digit number to tap on the phone, as in Google's sign-in prompt | 
| Operator command: okta\_login, okta\_login\_error, okta\_pass\_error | What the victim sees: An Okta username and password screen, branded "Connecting to \<Brand>" and "Powered by Okta" | 
| Operator command: okta\_push | What the victim sees: "Push notification sent," with a "Send push automatically" option for Okta Verify | 
| Operator command: okta\_code, okta\_auth, okta\_sms (and their \_error forms) | What the victim sees: A prompt for an Okta Verify, Google Authenticator, or SMS code | 
| Operator command: redirect | What the victim sees: The browser goes to a URL the operator supplies | 
| Operator command: complete | What the victim sees: The "Thank you for your application!" end screen | 

Every value goes to https://\<backend>/backend/api/submit.php as JSON with four fields: session\_id, type, value, and extra. Each request carries an X-Session-ID header with the same session ID, so the browser sends a CORS preflight request first. The session ID is the current time and a random string in base 36, 13 to 15 characters long, for example mwnl9p2hdb5ip9b. The type field takes one of these values:

- visitor, sent as captcha\_passed when the gate is solved
- email, password, and phone
- sms\_code and auth\_code
- okta\_user, okta\_password, okta\_auth\_code, and okta\_sms\_code

## [Infrastructure and timeline](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-infrastructure-and-timeline)

The landing hosts change much more frequently than the backend. Each brand gets its own subdomain on a domain that sounds like recruitment or research, such as interview-experts\[.\]com, sso-interview\[.\]com, researchparticipation\[.\]com, and feedback-study\[.\]com.

- **Landing hosts:** The operators used AWS EC2 from October 13 to November 13, then moved to Vultr. Every host had its own IP address.
- **Backend:** Every build from October 13 to November 18 sent credentials to importantfuture\[.\]com (162.0.225\[.\]230, Namecheap). From November 17, the Nvidia and Google Cloud builds send credentials to hypernovaguys\[.\]com (104.207.85\[.\]90) instead.

*Key dates in the GoodGuys campaign, from the first captures to the latest backend switch.*

| Date (2026) | Event | 
|---|---|
| Date (2026): Oct 13 | Event: First captures, on paid-interview-portal\[.\]com under the "Expert Interviews \| WPP Media" title. | 
| Date (2026): Oct 15 | Event: The Okta screens appear in the builds. | 
| Date (2026): Oct 18–21 | Event: The Spotify skin appears, followed by the Culver's skin on Oct 20. | 
| Date (2026): Nov 5 | Event: The American Express skin appears. | 
| Date (2026): Nov 12 | Event: The Coca-Cola skin appears. | 
| Date (2026): Nov 13 | Event: The landing hosts move from AWS EC2 to Vultr. | 
| Date (2026): Nov 17–19 | Event: The Nvidia and Google Cloud builds switch to the new backend, hypernovaguys\[.\]com. The SpaceX skin appears on Nov 17 and the Google Cloud skin on Nov 18. | 

## [Related Evilginx activity](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-related-evilginx-activity)

We've also seen Coca-Cola interview lures that lead to a modified Evilginx 3 proxy, which relays Google's real sign-in page to target Google Ads accounts. The same operator may be behind both campaigns. They used the same abused SendGrid click tracker, on the erelease\[.\]com\[.\]au domain, in the same week, and both serve an identical Coca-Cola wordmark image. Both also pitch a paid interview to work accounts, with Google first and Okta as an option. However, the code and hosting are different, and a hijacked sending account can be shared or resold.

## [Learn more about Push](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-learn-more-about-push)

Push blocks phishing pages like GoodGuys by analyzing the page in real time in the browser, whatever the delivery vector. That includes links delivered by email, as well as links sent through messaging apps, social media, search results, and other channels. Push sees the page after the employee solves the captcha, so the gate that hides the kit from scanners doesn't hide it from Push.

Push customers are protected and don’t need to take any further action.

Book a [live demo](https://pushsecurity.com/demo) to learn more.

## [Indicators of compromise](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-indicators-of-compromise)

The operators move landing hosts every few days, so these indicators have limited value for blocking and are most useful for hunting in logs. They're current as of November 20, 2026.

### [GoodGuys domains and IP addresses](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-indicators-of-compromise_id-goodguys-domains-and-ip-addresses)

| Role | Domain | IP address | Hosting | 
|---|---|---|---|
| Role: Backend | Domain: hypernovaguys\[.\]com | IP address: 104.207.85\[.\]90 | Hosting: | 
| Role: Backend | Domain: importantfuture\[.\]com | IP address: 162.0.225\[.\]230 | Hosting: Namecheap (AS22612) | 
| Role: Landing | Domain: virtual\[.\]cloud-webinar\[.\]com | IP address: 149.248.19\[.\]152 | Hosting: Vultr | 
| Role: Landing | Domain: google\[.\]webinar-cloud\[.\]com | IP address: 80.240.29\[.\]36 | Hosting: Vultr | 
| Role: Landing | Domain: accenture\[.\]international-interviews\[.\]com | IP address: 136.244.66\[.\]163 | Hosting: Vultr | 
| Role: Landing | Domain: nvidia\[.\]feedback-study\[.\]com | IP address: 95.179.161\[.\]218 | Hosting: Vultr | 
| Role: Landing | Domain: accenture\[.\]company-interviews\[.\]com | IP address: 199.247.1\[.\]212 | Hosting: Vultr | 
| Role: Landing | Domain: spacexgrok\[.\]company-mission\[.\]com | IP address: 45.76.232\[.\]140 | Hosting: Vultr | 
| Role: Landing | Domain: accenture\[.\]internationally-interviews\[.\]com | IP address: 136.244.119\[.\]45 | Hosting: Vultr | 
| Role: Landing | Domain: cocacola-company\[.\]interviewscompany\[.\]com | IP address: 66.245.193\[.\]191 | Hosting: Vultr | 
| Role: Landing | Domain: accenture\[.\]interviews-master\[.\]com | IP address: 149.28.113\[.\]213 | Hosting: Vultr | 
| Role: Landing (likely, not captured) | Domain: fetchx\[.\]com | IP address: 149.28.113\[.\]213 | Hosting: Vultr | 
| Role: Landing | Domain: cocacola-company\[.\]insightparticipation\[.\]com | IP address: 18.225.209\[.\]245 | Hosting: AWS EC2 | 
| Role: Landing | Domain: accenture\[.\]interviewprograms\[.\]com | IP address: 54.193.109\[.\]70 | Hosting: AWS EC2 | 
| Role: Landing | Domain: accenture\[.\]interviewapplicants\[.\]com | IP address: 3.26.117\[.\]192 | Hosting: AWS EC2 | 
| Role: Landing | Domain: spotify\[.\]paidexpert-interviewsso\[.\]com | IP address: 3.101.75\[.\]151 | Hosting: AWS EC2 | 
| Role: Landing | Domain: amex\[.\]sso-expertinterviews\[.\]com | IP address: 18.144.241\[.\]196 | Hosting: AWS EC2 | 
| Role: Landing | Domain: amex\[.\]researchparticipation\[.\]com | IP address: 13.220.176\[.\]225 | Hosting: AWS (AS14618) | 
| Role: Landing | Domain: amex\[.\]sso-interview\[.\]com | IP address: 52.65.236\[.\]40 | Hosting: AWS EC2 | 
| Role: Landing | Domain: accenture\[.\]sso-interview\[.\]com | IP address: 16.171.154\[.\]236 | Hosting: AWS EC2 | 
| Role: Landing | Domain: spotify\[.\]interview-experts\[.\]com | IP address: 34.248.232\[.\]29 | Hosting: AWS EC2 | 
| Role: Landing | Domain: spotify\[.\]research-interview\[.\]com | IP address: 13.39.106\[.\]64 | Hosting: AWS EC2 | 
| Role: Landing | Domain: amex\[.\]interview-experts\[.\]com | IP address: 18.145.194\[.\]221 | Hosting: AWS EC2 | 
| Role: Landing | Domain: accenture\[.\]applicants-interviewpro\[.\]com | IP address: 16.170.214\[.\]5 | Hosting: AWS EC2 | 
| Role: Landing | Domain: spotify\[.\]global-interviews\[.\]com | IP address: 63.32.99\[.\]110 | Hosting: AWS EC2 | 
| Role: Landing | Domain: lifeatspotify\[.\]interviewhubexperts\[.\]com | IP address: 3.121.125\[.\]185 | Hosting: AWS EC2 | 
| Role: Landing | Domain: lifeatspotify\[.\]researchsessions\[.\]com | IP address: 51.20.87\[.\]142 | Hosting: AWS EC2 | 
| Role: Landing | Domain: culvers\[.\]enterprise-interviews\[.\]com | IP address: 54.253.198\[.\]124 | Hosting: AWS EC2 | 
| Role: Landing | Domain: interview-expert-portal\[.\]com, spotify\[.\]interview-expert-portal\[.\]com | IP address: 3.104.118\[.\]219 | Hosting: AWS EC2 | 
| Role: Landing | Domain: experts-interview\[.\]com, spotify\[.\]experts-interview\[.\]com | IP address: 13.60.43\[.\]28 | Hosting: AWS EC2 | 
| Role: Landing | Domain: paid-interview-portal\[.\]com, accenture\[.\]paid-interview-portal\[.\]com | IP address: 18.133.231\[.\]78 | Hosting: AWS EC2 | 

### [Evilginx proxy domains and IP addresses](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-indicators-of-compromise_id-evilginx-proxy-domains-and-ip-addresses)

All of these are on DigitalOcean except 13.63.28\[.\]157, which is on AWS and was used for one day.

| Role | Domain | IP address | 
|---|---|---|
| Role: Gate, then proxy | Domain: cocacolainterview\[.\]com, \*.login.cocacolainterview\[.\]com | IP address: 165.232.88\[.\]9 | 
| Role: Gate | Domain: cocacolacareershub\[.\]com | IP address: 165.232.88\[.\]9 | 
| Role: Lure and Okta proxy | Domain: adsbillinghub\[.\]com, \<org>-okta.login.adsbillinghub\[.\]com | IP address: 165.232.88\[.\]9 | 
| Role: Lure and Google proxy | Domain: adsbillinghub\[.\]com, login.adsbillinghub\[.\]com | IP address: 209.38.44\[.\]178 | 
| Role: Google proxy | Domain: account-secure\[.\]net | IP address: 64.226.94\[.\]90, 13.63.28\[.\]157, 209.38.44\[.\]178 | 

### [File hashes (SHA-256)](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-indicators-of-compromise_id-file-hashes-sha-256)

The bundle file name stays the same for each skin, and the hash changes with each deployment.

| File | Skin or deployment | SHA-256 | 
|---|---|---|
| File: index-DOTVDRsd.js | Skin or deployment: Google Cloud, virtual\[.\]cloud-webinar\[.\]com | SHA-256: 3afce1ae01a8b346338fe7348e3f470655ffb9fa833a5977af33aafd27241684 | 
| File: index-DOTVDRsd.js | Skin or deployment: Google Cloud, google\[.\]webinar-cloud\[.\]com | SHA-256: d870675afdddfc62ba2f01750c67fc6348341f2d2be26ee57551a67c87385e76 | 
| File: index-C7YWYun7.js | Skin or deployment: Nvidia | SHA-256: 04295570a759dc514c9833f9976d23c2876fa1bad8510b1831f7d9869683cff6 | 
| File: index-Ylpk1kKK.js | Skin or deployment: SpaceX | SHA-256: aa399ff327b8fbafbd9bd4f1054c20fb7cb9fc0ebe9ea2b8eb912f21d3606474 | 
| File: index-r\_age5TO.js | Skin or deployment: Coca-Cola | SHA-256: 9ff82e910a9291dbae97b809b87b4cd03257befbab2d35c1e2f7b8f324f3f226 | 
| File: index-B7Epk7k7.js | Skin or deployment: Accenture (5 deployments) | SHA-256: 0a7e5b83991728cb9d7d54f10a2739ccc4042e985b1b3d71446d1e204448895a, 018d0d4668f0b7bcf04dc40b07306a9705c15f5e4ffc44f8f857d7fdbac97089, 5314b4ee2356a6434124d67afa4088f30b7b4e0807131e896680f6e4492cd4a6, 6e3a95cfc4b4dd81e62ee9ab9b758aef6c6478956271dd3bc0c24d8845271f57, 51652ffe763a85b0e3240c740ac3af678c6e8f57f24c89ab4f55b43270a8ca6f | 
| File: index-Dvfp1MVj.js | Skin or deployment: Spotify (3 deployments) | SHA-256: 870bcfbee99b0fba4f4d5e92440b3f2fdb5417a6799a1bcaf5f2ebf3ba14a9cb, c02822545654341c888cce46cb0cb15b300dc7eac246e44ab24154c1ea446c75, 2d860ff34d4d074002bb963832571ba37a09d30266dca224a6168d729ea9ce42 | 
| File: index-DHxrJ5OC.js | Skin or deployment: American Express (2 deployments) | SHA-256: ee1b5fabb9d75c07564b75372b8a195bc9342a878c1d5ff465657e915cf6118a, 85979cd81142f80f8f84a12160e192760916ea3eaebee104be3db85e189c52e3 | 
| File: index-pgubi2Vx.js | Skin or deployment: Culver's | SHA-256: 8278611c63a252c7ec591ce7b7dc12090331a4183063107d10df4e1e2d9f1a7b | 
| File: index-h3zoT7B2.css | Skin or deployment: Google Cloud and SpaceX builds | SHA-256: 4028d6040fcbe75410869c9615ccda137d77f4c9a81855dc25e368e7677b620c | 
| File: index-pj2tPCmX.css | Skin or deployment: Coca-Cola and Nvidia builds | SHA-256: b5c0345aa6b0413dd004b9adf77452344b97c46e723bc5bf6c57d472cbf910c1 | 
| File: index.html | Skin or deployment: virtual\[.\]cloud-webinar\[.\]com | SHA-256: 62d86cd7e9f9196209ed79ba4403b8f65a4834ab5a06010d6ea33be2f9ebd782 | 
| File: google-cloud-logo.png | Skin or deployment: Google Cloud | SHA-256: d775a30a835fd68c36b51519b5649c4bfeb7db44c004f8818b70abc36d798137 | 
| File: cloud-experts.png | Skin or deployment: Google Cloud | SHA-256: 2360967336a462d12425140a6d6cb324996d1460b5eb25b06baaffb2f5878fda | 
| File: Coca-Cola wordmark PNG | Skin or deployment: Coca-Cola skin, and the Evilginx lure | SHA-256: 3a252766b99463844b779ff1681bf1a43f7f3b0e3571886422655b88528848e8 | 

### [Abused sending services](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown#id-indicators-of-compromise_id-abused-sending-services)

These are legitimate services whose accounts or link tracking the attackers misused.

| Service | Sender or click URL seen | 
|---|---|
| Service: HireVue | Sender or click URL seen: interviews@hirevue\[.\]com (sender of the intercepted Google Cloud lure) | 
| Service: erelease (SendGrid link branding) | Sender or click URL seen: links\[.\]erelease\[.\]com\[.\]au/ls/click | 
| Service: SendGrid | Sender or click URL seen: u4725878, u26892420, u30119751, and u6442896\[.\]ct\[.\]sendgrid\[.\]net/ls/click | 
| Service: Mandrill | Sender or click URL seen: mandrillapp\[.\]com/track/click/30770134 | 
| Service: Planned (SendGrid) | Sender or click URL seen: url565\[.\]planned\[.\]com/ls/click | 
| Service: Weave | Sender or click URL seen: url6484\[.\]marketing\[.\]sg\[.\]weavecoms\[.\]com/ls/click | 
| Service: Cvent | Sender or click URL seen: na\[.\]eventscloud\[.\]com/emarketing/go.php | 
| Service: Commerce7 | Sender or click URL seen: link\[.\]commerce7\[.\]com/ss/c/ | 
| Service: Culver's | Sender or click URL seen: l\[.\]culvers\[.\]com/s/c/ | 
| Service: Phorest | Sender or click URL seen: tracking\[.\]phorest\[.\]com/tracking/click | 
| Service: Wellyx | Sender or click URL seen: email\[.\]maileu\[.\]wellyx\[.\]com/c/ | 
| Service: Truescope, then Amazon S3 | Sender or click URL seen: tracking\[.\]truescope\[.\]com/CL0/ to amzn-s3-accentre-interviewsw\[.\]s3\[.\]us-west-1\[.\]amazonaws\[.\]com/index.html |
