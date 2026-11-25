---
title: The Rise and Rise of DarkSword attacks
url: https://www.iverify.com/blog/the-rise-and-rise-of-darksword-attacks
hostname: iverify.com
description: Discover how DarkSword and Coruna malware attacks exploit Optimizely to target major brands. Learn key security steps to protect your iOS devices.
sitename: iVerify
date: "2026-11-17"
fingerprint: e5fe285fa992c447
language: en
image: https://framerusercontent.com/images/m7fDooAr1lfawDtv45jS1U2Zew.png?width=1024&height=576
pagetype: website
filedate: "2026-11-25"
---
**Update, November 18, 2026:** In response to the wave of unprecedented cyberattacks in recent weeks, we’re making **iVerify Basic, our consumer app for individuals,** free permanently. Available on iOS and Android.

*iVerify Basic is a separate consumer-focused mobile security application designed for individual users who want to check their personal device for signs of compromise on a semi-regular basis. It is not a replacement for our enterprise-grade, fleet-level detection. Looking to protect your entire organization? Book a demo of iVerify Enterprise.*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Since iVerify broke the [news](https://www.iverify.com/blog/darksword-ios-exploit-kit-explained) in March this year about DarkSword infecting iPhones and the subsequent leak of the source code to GitHub, [the exploit kit has proliferated among criminal groups](https://www.iverify.com/blog/proliferation-of-coruna-and-darksword), many of whom evolved its code to [add new functionality](https://www.iverify.com/blog/darksword-variant-threat-research) including pilfering additional crypto wallets. DarkSword operators are getting smarter about how they deploy it, and this doesn’t require subject matter expertise or LLM assistance; they are mirroring playbooks we saw run on desktop years ago.

On October 21st in joint publication with Report URI we disclosed information on DarkSword operators using advertising networks; [ads](https://www.iverify.com/blog/malvertising-coruna-darksword-iphone-exploits). Malvertisements are nothing new in cybersecurity. They’ve long been part of the desktop threat model because they allow adversaries to target the populations they are likely to have the highest success rate with the lures these targets are most likely to click on. For DarkSword, this means criminal actors can specifically go after users who are running vulnerable iOS versions and have an interest in crypto. The upfront cost is higher for the threat actor but almost guarantees a profit off every ad served.

Report URI detailed a [new DarkSword and Coruna attack](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) that abused [Optimizely](https://www.optimizely.com/), a service many of the world’s largest brands use to serve A/B content on their websites to make sure they produce the best web content and experience. Report URI found 178 major brands had been impacted (see list of brands in the appendix), though about 15% of them had technology deployed that mitigated this attack, meaning visitors to those sites would not have been affected. The deployed variants were still identical to those previously seen which 11% of iPhones are still vulnerable to by Apple’s most recently reported figures.

Due to the size of these brands, that figure translates to an estimated 16 to 45 million potential victims. This range takes into account the unique visitors per month across all of the named properties, divided by the volume of traffic specific to mobile, further filtered by the percentage of devices still running vulnerable versions of iOS, with the lower number reflecting global visitors where about 1 in 4 people use iPhones and the latter specific to North America where iPhones represent about 60% of the market.

On Nov 17th after Report-URI had reported this incident to Optimizely, they posted this security update [https://status.optimizely.com/incidents/ftw0fh9wx43z?ref=blog.report-uri.com](https://status.optimizely.com/incidents/ftw0fh9wx43z?ref=blog.report-uri.com)

# Key Takeaways

- **DarkSword and Coruna victims don’t get Apple Threat Notifications.** To our knowledge, not one device we detected under DarkSword or Coruna attack received an Apple Threat Notification (ATN), the warning Apple sends to users it believes are being successfully or unsuccessfully targeted. ATNs appear overly focused on nation-state threats like Pegasus and Paragon, a well-known commercial spyware tool. Additionally, threat actors are getting better at cleaning up their tracks and the traces that do remain age off the device faster, so the evidence effectively goes dark after a few days. By the time an ATN is received, high-confidence data would have disappeared anyway.
- **Threat actors are continuing to throw resources at DarkSword and Coruna.** New campaigns are caught monthly. Newer variants have scaffolding in place to support newer iOS versions, signaling intent to try and make them forward compatible, but to date, we haven’t seen any successful attempts on devices running iOS past 18.7. While there is evidence that LLMs are being used to improve the code and find new vulnerabilities, actually chaining these together into a working exploit is still reserved for people who really know what they are doing. However, it’s not safe to assume that forward-compatible versions don’t exist and just haven’t been spotted yet.
- **The economics of exploitation are changing.** The assumption so far has been that all of these attacks are for older versions of iOS, but researchers have demonstrated novel hacks that bypass lockdown mode and Memory Integrity Enforcement with the aid of frontier AI. Skilled bad actors could be using similar techniques to create their own attacks now, but it’s only a matter of time before open-weight models will be able to provide these capabilities to anyone who can afford the tokens to do it.

# What should I do?

iVerify has the same recommendation for this attack as all other Coruna and DarkSword attacks.

1. Add the IOCs to your DNS or web filtering solution to block them
2. Make sure your iOS-based devices are all running 26.3 or higher or 18.7.7 if you are unable to update devices to latest
3. Make sure you have deployed iVerify Enterprise to your iOS fleet, DarkSword detection requires near real-time monitoring

**Only protecting an individual device?** Update to iOS 26.3 or later and download iVerify Basic for free to monitor your personal device (available on iOS and Android).

# Appendix

## List of brands affected.

This comes from the [Report-URI blog post](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)

### By sector

| **Sector** | **Orgs** | **Examples** | 
|---|---|---|
| Banking & Finance | 32 | Paychex, HSBC US, Equifax, SmartAsset, HSBC Hong Kong | 
| Technology & SaaS | 23 | Zoom, Bitly, Salesforce, GitLab, Optimizely | 
| Retail & Fashion | 20 | IKEA, ASOS, Mattel, American Eagle, Scheels | 
| Streaming & Entertainment | 12 | Peacock, D&D Beyond, Wizards of the Coast, NOW TV, Zattoo | 
| News & Media | 10 | CNN, BBC, Fox News, NPR, CTV News | 
| Airlines & Travel | 9 | Alaska Airlines / Hawaiian Airlines, Transavia, Air France-KLM, KLM Netherlands, Trafalgar | 
| Healthcare & Pharma | 8 | Invisalign, Takeda, Covetrus, iTero (Align), Covetrus Pharmacy | 
| Industrial & Manufacturing | 8 | Fluke, eMaint (Fluke), Fluke Networks, Vaillant Germany, Fluke Process Instruments | 
| Telecoms | 7 | Virgin Media, Virgin Media O2, Vodafone Australia, O2, TPG Telecom | 
| Crypto & Trading | 6 | Ledger, IG, OANDA / Coinpass, interactive investor, TMS Brokers | 
| Insurance | 6 | Asurion / uBreakiFix, Mutual of Omaha, Admiral, Securian Financial, eRenterPlan | 
| Property & Real Estate | 6 | Buildium (managebuilding.com), Loft Living apartments, Buildium, HireAHelper, Flytte.no (and sister comparison sites) | 
| Food & Hospitality | 5 | Restaurant ordering sites (order.online), Heineken, Home Chef, Starbucks Canada, Cinnabon | 
| Home & Smart Home | 5 | Resideo, Honeywell Home, myQ (Chamberlain), Chamberlain, First Alert | 
| Nonprofit & Civic | 4 | Change.org, ASPCA, UNICEF USA, DonorsChoose | 
| Gambling | 4 | Betsson, PokerStars, tombola, Betfred | 
| Professional Services | 4 | Freshfields, CohnReznick, Baringa, Cro Metrics | 
| Logistics & Shipping | 3 | ShipStation / ShipEngine, Stamps.com, ShipEngine | 
| Automotive | 3 | Lucid Motors, O'Brien Glass, Chevrolet dealer network (Bill Rapp and others) | 
| Education | 3 | Walden University, Perlego, Chamberlain University | 

### Detailed List of Brands

#### Banking & Finance (32)

| **Organisation** | **Domains** | 
|---|---|
| Paychex | www.paychex.com | 
| HSBC US | www.us.hsbc.com | 
| Equifax | equifax.com, my.equifax.com, signin.my.equifax.com, www.equifax.com | 
| SmartAsset | smartasset.com | 
| HSBC Hong Kong | www.hsbc.com.hk | 
| ABN AMRO | www.abnamro.de, www.abnamro.nl, www.abnamromeespierson.be | 
| TaxAct | www.taxact.com | 
| HSBC Mexico | www.hsbc.com.mx | 
| HSBC Singapore | www.insurance.hsbc.com.sg | 
| NetCredit | www.netcredit.com | 
| Associated Bank | www.associatedbank.com | 
| S-Pankki | www.s-pankki.fi | 
| Equifax Canada | my.equifax.ca, www.equifax.ca | 
| Equifax UK | equifax.co.uk | 
| The Work Number (Equifax) | theworknumber.com | 
| Funding Circle | fundingcircle.com, www.fundingcircle.com | 
| HSBC Australia | www.hsbc.com.au | 
| CashNetUSA | www.cashnetusa.com | 
| OnDeck | www.ondeck.com | 
| ICS Cards | www.icscards.nl | 
| HSBC UAE | www.hsbc.ae | 
| HSBC Malaysia | www.hsbc.com.my, www.hsbcamanah.com.my | 
| Rest Super | rest.com.au | 
| HSBC Taiwan | www.hsbc.com.tw | 
| HSBC Vietnam | www.hsbc.com.vn | 
| HSBC Egypt | www.hsbc.com.eg | 
| HSBC Philippines | www.hsbc.com.ph | 
| SmartAdvisor Match (SmartAsset) | smartadvisormatch.com | 
| Compare Club | compareclub.com.au | 
| ABN AMRO Lease | abnamrolease.com | 
| Energy Scout | energyscout.com.au | 
| Hang Seng Investment | www.hangsenginvestment.com | 

#### Technology & SaaS (23)

| **Organisation** | **Domains** | 
|---|---|
| Zoom | www.zoom.com, zoom.com, zoom.us | 
| Bitly | arcg.is, bit.ly, bitly.com | 
| Salesforce | evergage.com, exacttarget.com, pardot.com, salesforce-scrt.com +4 more | 
| GitLab | about.gitlab.com, gitlab.com | 
| Optimizely | home.optimizely.com, login.optimizely.com, optimizely.com, prep.login.optimizely.com +1 more | 
| Mixpanel | mixpanel.com | 
| Typeform | typeform.com, www.typeform.com | 
| InMotion Hosting | www.inmotionhosting.com | 
| Wasabi | wasabi.com, wasabisys.com | 
| Perforce / Zend / Puppet | www.perforce.com, www.puppet.com, zend.com | 
| Tableau | www.tableau.com | 
| Hootsuite | hootsuite.com, www.hootsuite.com | 
| Smartsheet | de.smartsheet.com, es.smartsheet.com, fr.smartsheet.com, help.smartsheet.com +2 more | 
| MuleSoft | mulesoft.com, www.mulesoft.com | 
| Thales / Imperva | community-cybersec.thalesgroup.com, imperva.com | 
| Tricentis | www.tricentis.com | 
| Web Hosting Hub | www.webhostinghub.com | 
| QR Code Generator | login.qr-code-generator.com, www.qr-code-generator.com | 
| ServiceChannel | preview.servicechannel.com, servicechannel.com, servicechannel.us | 
| Brandfolder | brandfolder.com | 
| Intelex | www.intelex.com | 
| Enverus | www.enverus.com | 
| Accruent | www.accruent.com | 

#### Retail & Fashion (20)

| **Organisation** | **Domains** | 
|---|---|
| IKEA | client.home-design.ikea.com | 
| ASOS | asos.com | 
| Mattel | creations.mattel.com | 
| American Eagle | www.ae.com | 
| Scheels | scheels.com, www.scheels.com | 
| Ariat | www.ariat.com | 
| American Girl | www.americangirl.com | 
| StackSocial | www.stacksocial.com | 
| Crocs India | www.crocs.in | 
| Levi's Japan | levi.jp | 
| Todd Snyder | www.toddsnyder.com | 
| Levi's Indonesia | levi.co.id | 
| Just Russel | app.brt-4076-credits-in-order-summary.justrussel.de, app.rph-487-customer-can-switch-their-pet-to.justrussel.be, app.rph-487-customer-can-switch-their-pet-to.justrussel.com, app.rph-487-customer-can-switch-their-pet-to.justrussel.fr +1 more | 
| Loloi Rugs | www.loloirugs.com | 
| Levi's Australia | levis.com.au | 
| Levi's Malaysia | levi.com.my | 
| Levi's Philippines | levi.com.ph | 
| Levi's Singapore | levi.com.sg | 
| Levi's Korea | levi.co.kr | 
| Levi's New Zealand | levis.co.nz | 

#### Streaming & Entertainment (12)

| **Organisation** | **Domains** | 
|---|---|
| Peacock | peacocktv.com, www.peacocktv.com | 
| D&D Beyond | dndbeyond.com, www.dndbeyond.com | 
| Wizards of the Coast | secretlair.wizards.com | 
| NOW TV | nowtv.com, www.nowtv.com | 
| Zattoo | zattoo.com | 
| Crave | www.crave.ca | 
| Starz | www.starz.com | 
| SkyShowtime | www.skyshowtime.com | 
| Bravo | www.bravotv.com | 
| SeaWorld | buschgardens.com, seaworld.com | 
| WOW (Sky Deutschland) | www.wowtv.de | 
| NOW Italia | [www.nowtv.it](http://www.nowtv.it/) | 

#### News & Media (10)

| **Organisation** | **Domains** | 
|---|---|
| CNN | cnn.com, edition.cnn.com, us.cnn.com, www.cnn.com | 
| BBC | www.bbc.co.uk, www.bbc.com | 
| Fox News | www.foxnews.com | 
| NPR | legacy-s1.npr.org, legacy.stage.npr.org, media.stage.npr.org, s-s1-origin.npr.org | 
| CTV News | www.ctvnews.ca | 
| Fox Sports | foxsports.com | 
| BNN Bloomberg / CP24 | www.bnnbloomberg.ca, www.cp24.com | 
| TSN | www.tsn.ca | 
| Top Gear | www.topgear.com | 
| BBC Earth | [www.bbcearth.com](http://www.bbcearth.com/) | 

#### Airlines & Travel (9)

| **Organisation** | **Domains** | 
|---|---|
| Alaska Airlines / Hawaiian Airlines | www.alaskaair.com, www.hawaiianairlines.com | 
| Transavia | www.transavia.com | 
| Air France-KLM | liberia.klm.com, russia.airfrance.com, www.klm.be, wwws.airfrance.fr | 
| KLM Netherlands | deal.klm.nl | 
| Trafalgar | www.trafalgar.com | 
| Contiki | www.contiki.com | 
| Insight Vacations | www.insightvacations.com | 
| The Travel Corporation | uat.costco.ttc.com | 
| Costsaver | [www.costsavertour.com](http://www.costsavertour.com/) | 

#### Healthcare & Pharma (8)

| **Organisation** | **Domains** | 
|---|---|
| Invisalign | invisalign.com, www.invisalign.com | 
| Takeda | www.takeda.com | 
| Covetrus | covetrus.com | 
| iTero (Align) | itero.com | 
| Covetrus Pharmacy | eastfieldveterinary.covetruspharmacy.com | 
| myCovetrus | www.mycovetrus.com | 
| RaySafe (Fluke) | www.raysafe.com | 
| Takeda Oncology | [www.takedaoncology.com](http://www.takedaoncology.com/) | 

#### Industrial & Manufacturing (8)

| **Organisation** | **Domains** | 
|---|---|
| Fluke | fluke.com | 
| eMaint (Fluke) | www.emaint.com | 
| Fluke Networks | www.flukenetworks.com | 
| Vaillant Germany | www.vaillant.de | 
| Fluke Process Instruments | www.flukeprocessinstruments.com | 
| Fluke Biomedical | www.flukebiomedical.com | 
| Landauer | www.landauer.com | 
| Vaillant Spain | [www.vaillant.es](http://www.vaillant.es/) | 

#### Telecoms (7)

| **Organisation** | **Domains** | 
|---|---|
| Virgin Media | virginmedia.com, www.virginmedia.com | 
| Virgin Media O2 | virginmediao2.co.uk, www.virginmediao2.co.uk | 
| Vodafone Australia | www.vodafone.com.au | 
| O2 | o2.co.uk, www.o2.co.uk | 
| TPG Telecom | www.tpg.com.au | 
| Mint Mobile | www.mintmobile.com | 
| TalkTalk | talktalk.co.uk, www.talktalk.co.uk | 

#### Crypto & Trading (6)

| **Organisation** | **Domains** | 
|---|---|
| Ledger | ledger.com, www.ledger.com | 
| IG | www.ig.com | 
| OANDA / Coinpass | oanda.com, www.oanda.com | 
| interactive investor | www.ii.co.uk | 
| TMS Brokers | www.tms.pl | 
| Betashares | [www.betashares.com.au](http://www.betashares.com.au/) | 

#### Insurance (6)

| **Organisation** | **Domains** | 
|---|---|
| Asurion / uBreakiFix | www.asurion.com, www.ubreakifix.com | 
| Mutual of Omaha | moocat.mutualofomaha.com, www.mutualofomaha.com | 
| Admiral | www.admiral.com | 
| Securian Financial | www.securian.com | 
| eRenterPlan | erenterplan.com | 
| AKA (Danish unemployment fund) | www.aka.dk | 

#### Property & Real Estate (6)

| **Organisation** | **Domains** | 
|---|---|
| Buildium (managebuilding.com) | headwayassetsllc.managebuilding.com | 
| Loft Living apartments | theapartmentsatkeltonstation.loftliving.com | 
| Buildium | www.buildium.com | 
| HireAHelper | qa2.hireahelper.com | 
| Flytte.no (and sister comparison sites) | flytte.no | 
| MovingPlace | [unionplus-qa4.movingplace.com](http://unionplus-qa4.movingplace.com/) | 

#### Food & Hospitality (5)

| **Organisation** | **Domains** | 
|---|---|
| Restaurant ordering sites (order.online) | order.online | 
| Heineken | www.heineken.com | 
| Home Chef | www.homechef.com | 
| Starbucks Canada | www.starbucks.ca | 
| Cinnabon | www.cinnabon.com | 

#### Home & Smart Home (5)

| **Organisation** | **Domains** | 
|---|---|
| Resideo | resideo.com, www.resideo.com | 
| Honeywell Home | www.honeywellhome.com | 
| myQ (Chamberlain) | www.myq.com | 
| Chamberlain | www.chamberlain.com | 
| First Alert | [www.firstalert.com](http://www.firstalert.com/) | 

#### Nonprofit & Civic (4)

| **Organisation** | **Domains** | 
|---|---|
| Change.org | www.change.org | 
| ASPCA | aspca.org, dev-cloudflare.aspca.org, secure.aspca.org, www.aspca.org | 
| UNICEF USA | www.unicefusa.org | 
| DonorsChoose | www.donorschoose.org | 

#### Gambling (4)

| **Organisation** | **Domains** | 
|---|---|
| Betsson | betsson.bet.ar, www.betsson.co, www.betsson.com, www.betsson1002.com | 
| PokerStars | www.pokerstars.com, www.pokerstars.de, www.pokerstars.fr, www.pokerstars.pt +1 more | 
| tombola | tombola.co.uk, tombolaarcade.co.uk, www.tombola.co.uk, www.tombola.it +1 more | 
| Betfred | www.betfred.com | 

#### Professional Services (4)

| **Organisation** | **Domains** | 
|---|---|
| Freshfields | www.freshfields.com | 
| CohnReznick | www.cohnreznick.com | 
| Baringa | www.baringa.com | 
| Cro Metrics | crometrics.com | 

#### Logistics & Shipping (3)

| **Organisation** | **Domains** | 
|---|---|
| ShipStation / ShipEngine | shipstation.com, www.shipstation.com | 
| Stamps.com | www.stamps.com | 
| ShipEngine | www.shipengine.com | 

#### Automotive (3)

| **Organisation** | **Domains** | 
|---|---|
| Lucid Motors | lucidmotors.com | 
| O'Brien Glass | www.obrien.com.au | 
| Chevrolet dealer network (Bill Rapp and others) | www.billrappchevy.com | 

#### Education (3)

| **Organisation** | **Domains** | 
|---|---|
| Walden University | www.waldenu.edu | 
| Perlego | www.perlego.com | 
| Chamberlain University | www.chamberlain.edu | 

## IOCs

| **IOC / Domain** | 
|---|
| 1688360\[.\]cc | 
| 1y69gy2mdzaltz1\[.\]icu | 
| 3601688\[.\]cc | 
| 5vobauua3ojpklx\[.\]icu | 
| 6xicduvopkxpyev\[.\]icu | 
| eil786npto9u5bq\[.\]icu | 
| gm38duxoihbmy5o\[.\]icu | 
| hrufvf7xb3ntctm\[.\]icu | 
| je4ft3gn8vxudum\[.\]icu | 
| l7bcsnwc7nzr3uo\[.\]icu | 
| linkforge\[.\]cc | 
| p55abnw2pnsz0bo\[.\]icu | 
| q1ls1ho9x7wsxlu\[.\]icu | 
| ryf3e5p7rf8slv8\[.\]icu | 
| sl6zirn8wu7kggn\[.\]icu | 
| so23nhowskohk67\[.\]icu | 
| webshell\[.\]lol | 

## Attacker wallets:

| **Cryptocurrency** | **Wallet Address** | 
|---|---|
| BTC | 19g9rZcPeiz8rUvyWpTRyXXhPnjsWrc3kW | 
| ETH/EVM | 0xC4026b06D82b0F0B363eda0642D61CfbDc17884e | 
| TRON | THvs6p56XkUiMkJeSc51cAP64u2RsTYqxa | 
| SOL | FVtL8NMYS9PA1v3HE67XUGCtGA9JaZUvqav2fU2LrV5n | 
| TON | UQAgM1VqSZQiJLSG5w-ovurq5CZdxLEK3\_7CMmwALTA5e09p | 
| LTC | ltc1q3wp7g6ds0ggg6fl6kncpa4sepn0q3qfacgred5 | 
| BCH | qzkaaf8n6grmpr0d9lx8xutn3r9lk722f566hhpe58 | 
| DOGE | DBEGrxRF7KMSuhTS4c1MFviStU6efdMnu5 | 

Subscribe to our blog to receive the latest research and industry trends delivered straight to your inbox. Our blog content covers sophisticated mobile threats, unpatched vulnerabilities, smishing, and the latest industry news to keep you informed and secure.
