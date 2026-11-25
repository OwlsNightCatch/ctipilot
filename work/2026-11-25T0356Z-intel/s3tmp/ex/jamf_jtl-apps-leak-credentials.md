---
title: "Jamf Threat Labs: Apps Leak Credentials And PII Over HTTP"
author: Jamf Threat Labs
url: https://www.jamf.com/blog/jtl-apps-leak-credentials/
hostname: jamf.com
description: Jamf Threat Labs found mobile apps across healthcare, retail, IoT and solar sectors leaking user credentials and PII over unencrypted HTTP. See the findings.
sitename: Jamfsoftware
date: "2026-08-11"
fingerprint: "3f20db130b92f1cd"
language: en
image: https://media.jamf.com/images/news/2026/jtl-apps-leak-credentials-update.webp?h=500&q=80&w=800
pagetype: website
filedate: "2026-11-25"
---
# Jamf Threat Labs discovers apps that leak credentials

Jamf Threat Labs have discovered a cluster of apps that are leaking sensitive information. Read on to learn more.

**Author**: Michal Rajčan and Nelson Mutua

During Jamf Threat Labs' continuous threat investigations, we came across a cluster of mobile apps leaking credentials and Personally Identifiable Information (PII) from a wide variety of industries:

- **Calm Radio**, a music-based relaxation app
- **Riello S.p.A**, an Italian manufacturing company specializing in burners and HVAC
- **Shenzhen EyBond Co., Ltd.**, a Chinese developer of solar and energy storage management platforms
- **Khazana Jewellery**, an Indian jewelry retailer
- **MiCare HealthTech Holdings**, a Malaysian healthcare management platform

We contacted developers of these apps with a responsible disclosure to fix the mentioned leaks. We have received only one reply and remediation: from Calm Radio.

As part of our standard research process, we are releasing these findings publicly as the responsible disclosure timeframe has ended.

In this blog, we take a deeper dive into the apps and the data they are leaking.

## The risks

These apps leak data over unencrypted HTTP requests while users are trying to log in to their accounts.

This means that requests with credentials in clear form (not obfuscated) are sent to the organizations’ servers unencrypted, exposing these data to all devices connected to the same network. This is especially risky in cases of users connecting to public networks.

## Calm Radio

In late 2025, Jamf Threat Labs' continuous monitoring and risk assessment triggered a credential leak alert related to the iOS app version. The developer promptly fixed the issue after our responsible disclosure with version 14.6.0 of the app.

Note: The Android app version was not affected by this issue.

During our investigation, we confirmed that the leak happened while users were trying to access paid content. Specifically, we observed user emails being leaked in plaintext, but instead of a password, the app sent an access token. This token, according to the app developers, has no tie to user passwords.

Unfortunately, even without a leaked password, an adversary can obtain access to the premium stream or use leaked tokens to craft a new request that grants access to stored Personally Identifiable Information (PII). They cannot obtain access to the account thanks to the Calm Radio app login workflow.

Because inputting PII is voluntary and not required, the consequences of a potential account compromise may range from minimal to an invasive exfiltration due to the access token leak.

In connection to the credential leak, we observed two additional leaks:

- **Any request to the affected domain was unencrypted**: Though data is open to capture, the potential for tampering is low, so consequences pose no significant threat.
- **Unencrypted call leaking session cookies**: This occurred while anonymous users made language preference requests. Anonymous users are guest users without previous login or account creation. It poses no real threat to subscribers, as they’ve already selected language preferences and anonymous users do not provide any data to leak.

In our responsible disclosure, we raised our findings to the developers, and the issues were remedied promptly. **We would like to thank and emphasize the developer’s willingness, timeliness and communication in resolving the issues we found.**

## Riello

Riello is a leading heating and cooling manufacturer for residential and commercial organizations. Its apps connect to Internet of Things (IOT) systems for residential purposes, and its systems are also used for businesses like schools, residential buildings and hospitals.

We reached out to Riello with a responsible disclosure. **As of this writing, the vulnerability has not been fixed and is still live.**

During our continuous monitoring, we came across several of Riello’s apps leaking these data via unencrypted HTTP calls.

### The affected iOS and Android apps

- BeSMART Thermostat
[Apple](https://apps.apple.com/gb/app/besmart-thermostat/id1069306521)
[Android](https://play.google.com/store/apps/details?id=com.besmart.thermostat)
- BeSMART AC
[Apple](https://apps.apple.com/us/app/besmart-ac/id1474337348)
- RiCLOUD Thermostat
[Apple](https://apps.apple.com/gb/app/ricloud-thermostat/id1130246549)
[Android](https://play.google.com/store/apps/details?id=com.riello.thermostat)
- RiCLOUD AC
[Apple](https://apps.apple.com/gb/app/ricloud-ac/id1263988263)
[Android](https://play.google.com/store/apps/details?id=com.riello.ricloud.ac)

Besides credentials and data leaks, we were able to observe unrestricted access to Riello’s API, allowing anyone without proper authorization and authentication to view and gather information about customers using the apps.

### Riello credentials leak

Registration and login requests to this domain are being sent unencrypted; they **leak any confidential data being transferred.**

### Unrestricted API access

Requests to the API are not limited or verified in any way. This means that with a simple modified request to the API, anyone can expose user information kept by Riello.

This API leak exposes:

- Full name
- Phone number
- Full address

Given the fact that users are issued a consecutive numerical value as ID, one can easily automate the API exposure to misuse by requesting all available user information sequentially. This way, BeSmart/RiCLOUD entire database of user PII will be exposed.

All of this means that more than **100k customers' PII could potentially be exposed.**

### Why these leaks matter

Data leaks of this type may not seem serious, but with login details, an attacker can gain access to an account. While having control over an account, the attacker:

- Has access to user’s personal data
- Can modify thermostat or AC settings
- Can modifying thermostat (and connected boiler) settings and potentially cause damage to the heating equipment by overheating it for prolonged time. Other potential misuse is just turning off the heating equipment when the user does not expect this (e.g. wintertime, vacations, etc.)

In case an attacker gains access to the account and obtains personal data, these data might be misused in further phishing campaigns to compromise different accounts or services.

The only requirement for the data exfiltration is the attacker sniffing traffic on the same network as the victim. This makes the attack surface rather limited, but still presents a real threat.

## Shenzhen EyBond Co., Ltd.

Shenzhen EyBond Co., Ltd., is a Chinese developer of solar and energy storage management platforms.

The following five applications are impacted across iOS and Android platforms:

### Shenzhen EyBond's credentials leakage via plaintext

These apps transmit sensitive login and registration data over unencrypted HTTP while users are authenticating or creating new accounts. This means credentials are sent in plaintext, visible to anyone on the same network. The risk is compounded by the fact that credentials are passed as URL parameters in GET requests, making them trivially readable in proxy logs, browser histories and network captures alike.

### Technical analysis

The five apps leak login details when a user is logging into their account or when they create a new account.

**SmartClient for Solar**

The SmartClient for Solar app is EyBond's primary platform for monitoring and managing solar installations. During login, the app sends an unencrypted HTTP request that exposes the following:

- Username
- Company key
- Signature and salt

SmartClient for Solar transmitting login credentials in plaintext.

### SmartESS (registration)

The credential leak in SmartESS is not limited to login. Account registration also transmits sensitive data over HTTP, exposing:

- Mobile number
- Verification code
- Signature and salt

SmartESS transmitting user registration data in plaintext.

### Smart-Meter

The Smart-Meter app, used for monitoring energy metering devices, exhibits the same vulnerability pattern as the others. During login, the following is leaked:

- Username
- Company key
- Signature and salt

Smart-Meter transmitting login credentials in plaintext.

### Security issues noted

Across all five apps, the following security deficiencies were identified:

- Unencrypted HTTP transport
- All authentication and registration traffic is transmitted over HTTP rather than HTTPS, exposing these data to any device on the same network.
- Credentials in URL parameters
- Usernames and company keys are passed as GET request URL parameters, a pattern explicitly warned against in OWASP guidance. URL parameters appear in server logs, network device logs, browser history and proxy caches: drastically increasing the attack surface.
- Signature and salt exposure

The apps do include a signature mechanism where a salt value changes per request, providing a basic layer of protection. However, the salt value is derived from input controlled by the client and readable from the URL itself. An attacker with knowledge of the signature computation logic, available via EyBond's publicly accessible API documentation, could spoof the salt value and attempt to crack passwords using pre-generated salted rainbow tables.

While executing this attack requires meaningful effort, it represents a real and viable threat. The combination of exposed salt, publicly documented signature logic and cleartext credential transmission makes the authentication mechanism weaker than it appears.

### Impact and risk assessment

EyBond's platforms are deployed in solar power plants, energy storage systems and industrial metering environments. The companies and installers using these apps often manage multi-site infrastructure on behalf of commercial or industrial clients. If an attacker captures credentials through a passive network intercept, for example, on a shared Wi-Fi at a job site or client facility, they could:

- **Log in to a victim's account** and gain visibility into the energy infrastructure they manage, including live device status, performance data and site configurations.
- **Obtain the company key,** which acts as an organizational identifier and may enable broader access to company-level resources within the platform.
- **Use registration data** (email, mobile number, verification codes) for targeted phishing or SIM-swapping attacks against the victim.
- **Pivot to downstream clients** since many users of these platforms are solar installers or ESS integrators managing multiple end-customer accounts, credential theft could cascade to compromise of those clients.

## Khazana Jewellery

Khazana Jewellery's app serves as a “savings” management app for purchasable goods from Khazana Jewellery. Users can send monthly payments to Khazana Jewellery and, after the purchase scheme completion, they can purchase jewelry or gold in value from the scheme savings.

**Jamf Threat Labs found the iOS version of the app is leaking credentials. However, the Android version of the app is safe from this issue.**

Example of a request leaking user credentials

There are several requests leaking data; the following data are leaked while users interact with the app:

- User email
- Password
- Full name
- Phone number

The app manages user payments and subscriber plans. If an attacker gets possession of the leaked credentials, they may log in to a compromised account and adjust it to their needs. This includes cancelling running subscriptions and causing unnecessary monetary harm in the form of cancellation fees.

The main risk of exposed credentials is access to the PII data stored in the app. When subscribing to a plan, a user needs to fill in personal details; these data may be misused for an advanced phishing attack or identity theft on the user.

Extent of PII requested and stored in the app:

- Full name
- Phone number
- Address
- PAN (tax) number
- ID number

Example of personal data contained in app. Source: Google Play store

## MiCare HealthTech Holdings

This [healthcare management company serves 15 million users](https://www.micarehealthtech.com/corporate.html); hence, we believe that the potential vector for misuse is not trivial.

Even though the leaky app is of low popularity and potentially kept for legacy reasons, the app remains in Apple and Android app stores and poses a real risk for users installing them.

The affected app is HBC-MED; iOS and Android versions show the same issues. This app appears to be a legacy management app and has been replaced by another app from the same developer.

Left: Old app that leaks data | Right: New app that does not leak user data

**We want to emphasize that the new app is not affected by the same flaws as the legacy one.**

Example of a request leaking user credentials

There are several requests leaking data; the following data are being leaked while interacting with the app:

- Username
- Password
- National ID
- Subscribed insurance/healthcare policy
- Device hardware specification (Android app only)

This credentials leak comes with another possibility of misuse. Given the nature of the leaky app, it is meant to manage users’ healthcare information. As clearly seen from the screenshot publicly shared in the app stores, the app has access to user personal data, medical card data and any dependent’s data. We could not confirm the extent of these data as we do not have any kind of working account for this healthcare management company. It is possible that this app has access to sensitive personal and healthcare data due to the nature of its purpose.

App’s interface showing access to data. Source: App Store for iPhone

Even though the affected users are very limited in number, **we believe this type of private data exposure is critical and deserves attention.** 

## How Jamf for Mobile helps protect against leaky apps

Jamf for Mobile’s Zero Trust Network Access (ZTNA) and Apple’s on-device content filtering capabilities protect your devices from leaky apps. Context-aware access policies and app vetting prevent the transmission of any of your company’s precious data.

Want to learn more about Jamf Threat Labs? Interested in how Jamf for Mobile can help you secure your mobile devices?
