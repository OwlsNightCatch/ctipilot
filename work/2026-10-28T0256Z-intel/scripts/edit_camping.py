import yaml
p='entries/2026-10-27/camping-care-tcs-camping-data-theft-php-flaw-whatsapp-fraud.md'
t=open(p,encoding='utf-8').read()
def rep(old,new,count=1):
    global t
    assert t.count(old)==count,(t.count(old),old[:90])
    t=t.replace(old,new)
rep('headline: "TCS Camping warns 15,000 guests: supplier\'s booking data stolen, tied by SRF to the PHP flaws; WhatsApp fraud under way"',
    'headline: "Camping.Care booking data stolen: TCS and a second campsite warn of WhatsApp fraud; the supplier has not confirmed a PHP link"')
rep('''  numbers are already used in fraudulent WhatsApp messages; TCS says account and IBAN data were not affected and the hole is closed.''',
'''  numbers are already used in fraudulent WhatsApp messages; TCS says account and IBAN data were not affected and the hole is closed. A
  second customer, Campingplatz Hüttenberg in canton Thurgau, has warned its guests of the same fraud in a notice that says Camping.care
  is still investigating the cause and does not mention PHP.''')
rep('''    publisher: "CISA (alert, updated 2026-10-26)"
    date: "2026-10-26"
    role: corroborating
closed_sources: []''','''    publisher: "CISA (alert, updated 2026-10-26)"
    date: "2026-10-26"
    role: corroborating
  - url: "https://www.camping-huettenberg.ch/erreichbarkeit-ueber-die-herbst-und-winterzeit-2/"
    publisher: "Campingplatz Hüttenberg (guest notice, page date 2026-10-23)"
    date: "2026-10-23"
    role: corroborating
  - url: "https://www.netzwoche.ch/news/2026-10-27/nach-angriff-ueber-php-sicherheitsluecke-nehmen-betrueger-camper-ins-visier"
    publisher: "Netzwoche"
    date: "2026-10-27"
    role: corroborating
closed_sources: []''')
rep('''    source_url: "https://www.blick.ch/wirtschaft/hackerangriff-auf-tcs-camping-15000-kunden-gewarnt/nws2bcn"
verification: single-source-victim''','''    source_url: "https://www.blick.ch/wirtschaft/hackerangriff-auf-tcs-camping-15000-kunden-gewarnt/nws2bcn"
  - quote: "Camping.care is currently investigating the cause of the incident. (translated from German)"
    original: "Camping.care untersucht derzeit die Ursache des Vorfalls."
    publisher: "Campingplatz Hüttenberg (guest notice, page date 2026-10-23)"
    source_url: "https://www.camping-huettenberg.ch/erreichbarkeit-ueber-die-herbst-und-winterzeit-2/"
  - quote: "As things stand, it must be assumed that booking data was used without authorisation. (translated from German)"
    original: "Nach aktuellem Stand ist davon auszugehen, dass Buchungsdaten unbefugt verwendet wurden."
    publisher: "Campingplatz Hüttenberg (guest notice, page date 2026-10-23)"
    source_url: "https://www.camping-huettenberg.ch/erreichbarkeit-ueber-die-herbst-und-winterzeit-2/"
  - quote: "Whether the attackers in the Camping.care incident actually exploited one of the PHP vulnerabilities is not apparent from the campsite's notice. (translated from German)"
    original: "Ob die Angreifer beim Vorfall bei Camping.care tatsächlich eine der PHP-Sicherheitslücken ausnutzten, geht aus der Mitteilung des Campingplatzes nicht hervor."
    publisher: "Netzwoche"
    source_url: "https://www.netzwoche.ch/news/2026-10-27/nach-angriff-ueber-php-sicherheitsluecke-nehmen-betrueger-camper-ins-visier"
verification: single-source-victim''')
rep('''  entry point, the date of the intrusion or an actor, and Camping.Care itself is not quoted.''','''  entry point, the date of the intrusion or an actor. Camping.Care itself is not quoted: its position reaches us through a customer's notice
  (Campingplatz Hüttenberg), which says it is investigating the cause and does not mention PHP, and Netzwoche notes that the notice does not
  say whether the PHP flaws were used.''')
rep('''TCS says account details and IBANs were not affected and that credit card data is not stored in the booking system ([SRF, 2026-10-26](https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping)).''',
'''TCS says account details and IBANs were not affected and that credit card data is not stored in the booking system ([SRF, 2026-10-26](https://www.srf.ch/sendungen/kassensturz-espresso/espresso/php-sicherheitsluecke-betrugsversuche-nach-datenleck-im-buchungssystem-fuer-tcs-camping)). A second customer, Campingplatz Hüttenberg in canton Thurgau, told its guests in a notice (page date 2026-10-23) that Camping.care had informed it of WhatsApp messages to guests of several campsites that contain real booking information and a link, that Camping.care is investigating the cause and that booking data must be assumed to have been used without authorisation; the notice does not mention PHP, and Netzwoche points out that it does not say whether the attackers used one of the PHP flaws ([Campingplatz Hüttenberg, 2026-10-23](https://www.camping-huettenberg.ch/erreichbarkeit-ueber-die-herbst-und-winterzeit-2/); [Netzwoche, 2026-10-27](https://www.netzwoche.ch/news/2026-10-27/nach-angriff-ueber-php-sicherheitsluecke-nehmen-betrueger-camper-ins-visier)).''')
rep('''and any other customer of the Camping.Care platform; Blick says it is not the only software supplier hit, and no other Camping.Care customer is named ([Blick, 2026-10-26](https://www.blick.ch/wirtschaft/hackerangriff-auf-tcs-camping-15000-kunden-gewarnt/nws2bcn)).''',
'''and any other customer of the Camping.Care platform, one of which, Campingplatz Hüttenberg, has warned its own guests; Blick says Camping.Care is not the only software supplier hit ([Blick, 2026-10-26](https://www.blick.ch/wirtschaft/hackerangriff-auf-tcs-camping-15000-kunden-gewarnt/nws2bcn); [Netzwoche, 2026-10-27](https://www.netzwoche.ch/news/2026-10-27/nach-angriff-ueber-php-sicherheitsluecke-nehmen-betrueger-camper-ins-visier)).''')
rep('''because SRF and Blick tie this theft to the PHP flaws although no source says how the intrusion happened;''','''because SRF and Blick tie this theft to the PHP flaws although the supplier says it is still investigating the cause and no source says how the intrusion happened;''')
open(p,'w',encoding='utf-8').write(t)
fm=yaml.safe_load(t.split('\n---\n',1)[0].split('---\n',1)[1]); print(len(fm['headline']))
