import yaml
p='entries/2026-09-30/manno-ti-commune-ransomware-safepay-claim.md'
t=open(p,encoding='utf-8').read()
def rep(old,new,count=1):
    global t
    assert t.count(old)==count,(t.count(old),old[:90])
    t=t.replace(old,new)
rep('title: "Swiss commune Manno (TI) confirms a cyberattack that encrypted part of its servers on 4 August 2026; SafePay is recorded listing the commune on a leak site on 28 September"',
    'title: "Swiss commune Manno (TI) confirms a cyberattack that encrypted part of its servers on 4 August 2026; SafePay has now published about 30 GB, which Risikomonitor reads as social-assistance decisions with AHV numbers, naturalisation files and a near-complete address book"')
rep('headline: "Manno restored from backup within an afternoon; SafePay was recorded listing the commune on 28 September"',
    'headline: "SafePay published about 30 GB from Manno: social-assistance files with AHV numbers; the commune makes no statement"')
old=t[t.index('summary: >\n'):t.index('discovered_at:')]
new='''summary: >
  The Ticino commune of Manno stated in a signed notice of 2026-09-16 that part of its servers were hit by an attack that encrypted data on
  4 August 2026; it isolated the server and restored from existing backups. SafePay, recorded on 2026-09-28 listing manno.ch on its leak
  site, has since put about 30 GB of stolen data into the darknet, and Inside IT reports of 2026-10-27 that the security firm Risikomonitor
  found social-assistance decisions with AHV numbers and health insurers from 2014 to December 2025, debt-enforcement extracts, naturalisation
  files and data on the whole population of 1,381; the commune says it will make no statement.
'''
t=t.replace(old,new)
rep('tags: [ransomware]','tags: [ransomware, data-breach]')
rep('techniques: [T1486]','techniques: [T1486, T1657]')
rep('''    date: "2026-09-29"
    role: corroborating
closed_sources: []''','''    date: "2026-09-29"
    role: corroborating
  - url: "https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027"
    publisher: "Inside IT (article of 2026-10-27, with Risikomonitor's analysis)"
    date: "2026-10-27"
    role: corroborating
closed_sources: []''')
rep('''    source_url: "https://www.inside-it.ch/tessiner-gemeinde-wird-opfer-von-cyberkriminellen-20260929"
verification: single-source-victim''','''    source_url: "https://www.inside-it.ch/tessiner-gemeinde-wird-opfer-von-cyberkriminellen-20260929"
  - quote: "SafePay has put stolen data packages from these two attacks into the darknet, about 30 gigabytes in the case of Manno (translated from German)"
    original: "Safepay hat erbeutete Datenpakete aus diesen beiden Angriffen ins Darknet gestellt – rund 30 Gigabyte im Fall von Manno"
    publisher: "Inside IT"
    source_url: "https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027"
  - quote: "documents on social-assistance decisions with name, address, monthly amount, AHV numbers and health insurer from 2014 to December 2025 (translated from German)"
    original: "Dokumente zu Sozialhilfeentscheiden mit Name, Adresse, Monatsbetrag, AHV-Nummern und Krankenkasse von 2014 bis Dezember 2025"
    publisher: "Inside IT"
    source_url: "https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027"
  - quote: "The municipality of Manno will not issue a statement in this matter. (translated from German)"
    original: "Die Gemeinde Manno wird in dieser Angelegenheit keine Stellungnahme abgeben."
    publisher: "Inside IT"
    source_url: "https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027"
verification: single-source''')
old=t[t.index('sourcing_note: >\n'):t.index('confidence:')]
new='''sourcing_note: >
  The encryption event comes from the commune's own signed notice about its own event. SafePay's role rests on a leak-site tracker's record of
  the group's listing and on Inside IT's report of 2026-10-27, the only source for the publication of the data; the contents come from an
  analysis by the security firm Risikomonitor that Inside IT relays and that has not been verified independently. The commune's notice
  names no actor and does not say whether data left the network. Inside IT's earlier article body is not readable, so only its teaser is
  cited. The restoration sentence of the PDF notice is stored with a shifted font encoding, and its plain reading is that data and operations
  were restored from existing backups during the afternoon.
'''
t=t.replace(old,new)
rep('''classification:
  reliability: A
  credibility: 2''','''classification:
  reliability: B
  credibility: 3''')
head,rest=t.split('\n---\n\n',1)
body=rest
i2=body.index('On 2026-09-28, 55 days after the encryption')
p1=body[:i2]
p1=p1.replace(' The notice names no actor, no intrusion vector, and does not say whether data left the network. Inside IT\'s teaser of 2026-09-29 calls it a ransomware attack and says a backup allowed a quick return to normal operation ([Inside IT, 2026-09-29](https://www.inside-it.ch/tessiner-gemeinde-wird-opfer-von-cyberkriminellen-20260929)). The tracker\'s leak-post screenshot shows a countdown timer of about three days eleven hours when it was captured on 2026-09-28, which points to expiry around 1 October; the post describes no dataset ([Ransomware.live, 2026-09-28](https://www.ransomware.live/id/bWFubm8uY2hAc2FmZXBheQ==)).',
 ' The notice names no actor, no intrusion vector, and does not say whether data left the network; Inside IT\'s teaser of 2026-09-29 calls it a ransomware attack and says a backup allowed a quick return to normal operation ([Inside IT, 2026-09-29](https://www.inside-it.ch/tessiner-gemeinde-wird-opfer-von-cyberkriminellen-20260929)).')
assert 'countdown' not in p1
IT='https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027'
p2=f'''On 2026-09-28, 55 days after the encryption, Ransomware.live recorded that the ransomware group SafePay had listed manno.ch on its leak site ([Ransomware.live, 2026-09-28](https://www.ransomware.live/id/bWFubm8uY2hAc2FmZXBheQ==)). Inside IT reported on 2026-10-27 that SafePay has put the stolen data into the darknet, about 30 GB in the case of Manno, and that the security firm Risikomonitor analysed it ([Inside IT, 2026-10-27]({IT})). Risikomonitor's reading, relayed by Inside IT and not verified independently: files with about 5,300 e-mail addresses and more than 2,000 identifiable persons; social-assistance decisions with name, address, monthly amount, AHV numbers and health insurer from 2014 to December 2025; debt-enforcement register extracts, naturalisation dossiers from 2018 and payment orders against tax debtors; employees' bank statements with IBANs; and mass letters, a youth-protection survey and a list of property owners with parcel and water-meter numbers that together give a near-complete address book of a commune of 1,381 inhabitants ([Inside IT, 2026-10-27]({IT})). Asked by Inside IT, the commune said it will make no statement on the publication ([Inside IT, 2026-10-27]({IT})).

**Defender takeaway:** a clean restore did not close the data-theft question here: the leak-site listing appeared 55 days after the encryption and the data was published about a month later, so a communal response to an encryption attack should keep its data-theft assessment open and plan for notification of affected persons, residents on social assistance first, and for the fraud that published AHV numbers, addresses and payment histories enable. The resident-fraud warning the commune issued belongs in the same response plan.
'''
t=head+'\n---\n\n'+p1.rstrip()+'\n\n'+p2
open(p,'w',encoding='utf-8').write(t)
fm=yaml.safe_load(head.split('---\n',1)[1])
print(len(fm['headline']))
