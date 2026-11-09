---
title: Kiberuzbrukumi attālināti vadāmām iekārtām - aktuālā informācija un drošības ieteikumi | CERT.LV
url: https://cert.lv/lv/2026/11/kiberuzbrukumi-attalinati-vadamam-iekartam-aktuala-informacija-un-drosibas-ieteikumi
hostname: cert.lv
description: Kopš 2026. gada oktobra Eiropā notiek kiberuzbrukumi veikalu un noliktavu saldēšanas iekārtu vadības sistēmām. Uzbrucēji attālināti maina temperatūras vai atkausēšanas iestatījumus, kā rezultātā iekārtu īpašniekam nākas pārtiku iznīcināt. Līdz 2. novembrim par incidentiem ziņots vismaz astoņās Eiropas valstīs, tostarp Igaunijā un Somijā.
sitename: CERT.LV - Informācijas Tehnoloģiju drošības incidentu novēršanas institūcija
date: "2026-11-06"
fingerprint: "7cd68e53de89b2d6"
---
# Kiberuzbrukumi attālināti vadāmām iekārtām - aktuālā informācija un drošības ieteikumi

Kopš 2026. gada oktobra Eiropā notiek kiberuzbrukumi veikalu un noliktavu saldēšanas iekārtu vadības sistēmām. Uzbrucēji attālināti maina temperatūras vai atkausēšanas iestatījumus, kā rezultātā iekārtu īpašniekam nākas pārtiku iznīcināt. Līdz 2. novembrim par incidentiem ziņots vismaz astoņās Eiropas valstīs, tostarp Igaunijā un Somijā.

CERT.LV apstiprina, ka arī Latvijā novēroti uzbrukumu mēģinājumi saldēšanas iekārtām. Veikalu ķēdes pagaidām nav skartas, bet cietusi kāda noliktava. CERT.LV brīdina, ka tādā pašā veidā var uzbrukt arī apkures katliem, ūdens sūkņiem un saules enerģijas vadības paneļiem.

**Tā kā kiberuzbrukumu risks neaprobežojas tikai ar saldēšanas iekārtām, sadarbībā ar Krīzes vadības centru apkopoti praktiski ieteikumi attālināti vadāmu iekārtu kiberdrošības stiprināšanai gan publiskajā, gan privātajā sektorā.**


## **Apdraudējuma raksturojums**

Uzbrukumos netiek izmantota viena noteikta ievainojamība. Izmanto divus galvenos ceļus:

**Tieša piekļuve no interneta.** Uzbrucēji meklē konkrēta veida iekārtas, kuru vadības panelis ir pieejams no interneta un ir neaizsargāts vai neatjaunināts. Bieži tiek izmantotas ražotāja noklusējuma vai vājas paroles.

**Piekļuve caur uzņēmuma tīklu.** Ja iekārtu vadība nav nodalīta no uzņēmuma kopējā tīkla, uzbrucējs vispirms ielaužas birojā tīklā un no tā pāriet uz iekārtām.

CERT.LV norāda, ka šādu iekārtu paroles bieži vispār netiek nomainītas. Nīderlandē skartās sistēmas nebija drošā tīklā un izmantoja noklusējuma paroles. Līdzīgu ainu apraksta arī ASV un sabiedroto kiberdrošības iestādes: uzbrucēji meklē internetā pieejamas vadības sistēmas un izmanto noklusējuma paroles ūdens, pārtikas un enerģētikas nozarē.

**Secinājums: ražotāja drošības atjauninājums vien risku nenovērš. Galvenais ir ierobežot piekļuvi internetam, nomainīt paroles un nodalīt tīklus.**


## **Preventīvie pasākumi**


### ***1.1. Potenciāli apdraudētās jomas***


| **Joma**  | **Piemēri**  | **Riska faktori**  | 
| Pārtika | Saldēšanas kameras un vitrīnas, noliktavu dzesēšana, skolu, slimnīcu un sociālās aprūpes iestāžu virtuves | Latvijā cietusi noliktava; uzbrukumi veikaliem astoņās Eiropas valstīs | 
| Veselība un farmācija | Zāļu, vakcīnu, asins un laboratoriju paraugu aukstuma iekārtas | Eksperti brīdina, ka nākamie mērķi var būt temperatūras jutīgas zāles un laboratorijas materiāli  | 
| Siltumapgāde | Katlumāju un siltummezglu vadība | CERT.LV brīdina par apkures katliem; Igaunijā 2023. gadā skartas astoņas katlumājas; Ļvivā 2024. gadā vairāk nekā 600 mājsaimniecību bija bez apkures  | 
| Ūdensapgāde un kanalizācija | Sūkņu stacijas, ūdens sagatavošanas un attīrīšanas iekārtas | CERT.LV brīdina par ūdens sūkņiem; Polijā 2025. gadā ielaušanās piecās ūdens attīrīšanas stacijās  | 
| Enerģētika | Saules paneļu un invertoru vadība (arī uz pašvaldību ēku jumtiem), apakšstacijas, rezerves ģeneratori | CERT.LV brīdina par saules enerģijas vadības paneļiem; Lietuva ierobežo invertoru attālinātu piekļuvi | 
| Hidrotehniskās | Aizvaru un vārstu vadība | Norvēģijā 2025. gadā attālināti atvērti dambja vārsti; to pamanīja pēc četrām stundām  | 
| Ēku inženiersistēmas | Ventilācija, apkure, dzesēšana, serveru telpu klimata kontrole, piekļuves kontrole, lifti | Daudzas šādas sistēmas ir vadāmas attālināti, un tās bieži ir 10–15 gadus vecas | 


###  ***1.2. Ieteicamā rīcība risku mazināšanai***


1. **Apzināt iekārtas.** Sastādīt sarakstu ar visām attālināti vadāmām iekārtām un sistēmām: kur tās atrodas, kas tās apkalpo, kā tām piekļūst.
2. **Pārbaudīt pieejamību no interneta.** Pārliecināties, ka vadības paneļi un ICS protokoli nav pieejami no interneta. Iekārtas, kurām interneta piekļuve nav nepieciešama, atvienot un izmantot vietējo vadības paneli.
3. **Drošināt attālināto piekļuvi.** Ja attālināta piekļuve tomēr ir nepieciešama, izmantot tikai VPN (virtuālo privāto tīklu) vai citu slēgtu, šifrētu savienojumu, stipras paroles un divu faktoru autentifikāciju.
4. **Nomainīt paroles.** Nomainīt visas ražotāja noklusējuma paroles; katrai iekārtai - unikāla parole. Pārbaudīt, kuriem lietotāju kontiem ir piekļuve, un dzēst liekos.
5. **Nodalīt tīklus.** Industriālās vadības sistēmām jābūt nodalītām no iestādes vai uzņēmuma kopējā tīkla, lai no biroja tīkla nebūtu iespējams nesankcionēti vadīt iekārtas vai mainīt to iestatījumus.
6. **Uzstādīt ražotāja drošības atjauninājumus.** Novecojušas iekārtas, kurām atjauninājumi vairs netiek izdoti, norobežot no pārējā tīkla ar atsevišķu maršrutētāju vai ugunsmūri, līdz tās iespējams nomainīt vai modernizēt, vai atslēgt no interneta.
7. **Pārbaudīt iestatījumus.** Pārskatīt temperatūras, atkausēšanas un citus kritiskos iestatījumus; saglabāt pareizās konfigurācijas rezerves kopiju.

*Ieteikumi balstīti arī uz Francijas CERT-FR un ASV un sabiedroto iestāžu ieteikumiem.*

**Tā kā iekārtu apkopi bieži veic ārpakalpojumu sniedzēji ar attālinātu piekļuvi, tad nepieciešams:**

1. informēt operatorus un apkopes uzņēmumus par šiem ieteikumiem un lūgt apstiprināt, ka tiek veikti preventīvie pasākumi;
2. noskaidrot, kas un kā attālināti piekļūst iekārtām, un pārliecināties, ka piekļuve notiek tikai caur drošu savienojumu un tikai pilnvarotām personām;
3. Iestādes IT drošības personāls ir informēts par iekārtu vadībai izmantotajām IP adresēm, iekārtu modeļiem, un tiem ir izsniegta iekāru uzraudzības uzņēmuma kontaktinformācija.
4. līgumos un iepirkumos iekļaut prasības par drošu attālināto piekļuvi, paroļu maiņu, drošības atjauninājumiem un pienākumu nekavējoties ziņot par incidentu;
5. pārbaudīt, vai apdrošināšana sedz kiberincidenta radītus zaudējumus.

### ***1.3. Uzraudzība un gatavība***


1. **Trauksmes signāli.** Nodrošināt automātiskus trauksmes signālus par temperatūras vai citu parametru novirzēm, arī naktī un brīvdienās. Igaunijā diennakts uzraudzība ļāva reaģēt 10 minūšu laikā, un zaudējumu nebija. Norvēģijā bez šādas uzraudzības incidentu pamanīja tikai pēc četrām stundām. Uzraudzības sistēmai jābūt nodalītai no iekārtu vadības kontrolieriem.
2. **Manuālā vadība.** Pārliecināties, ka personāls zina, kā pārslēgt iekārtas uz manuālu vadību, un to praktiski izmēģināt.
3. **Nepārtrauktības plāni.** Iekļaut darbības nepārtrauktības plānos scenāriju "attālināti vadāmas iekārtas uzbrukums", tostarp rezerves risinājumus (piem., pārtikas vai zāļu pārvietošana, alternatīva siltuma vai ūdens piegāde).
4. **Tiesiskās prasības.** Nacionālā kiberdrošības likuma subjektiem (piem., dzeramā ūdens, notekūdeņu, enerģētikas, veselības aprūpes, pārtikas ražošanas un tirdzniecības jomā) jāievēro likumā noteiktās prasības, tostarp par riska pārvaldību un ziņošanu par incidentiem CERT.LV.

### 

***1.4. Rīcība kiberincidenta gadījumā***


1. Atvienot skarto iekārtu no interneta un tīkla vai pārslēgt to uz manuālu vadību.
2. Nodrošināt pakalpojuma nepārtrauktību saskaņā ar savu plānu (piem., pārvietot pārtiku vai zāles).
3. Saglabāt žurnālus un pierādījumus; iekārtu bez vajadzības neatiestatīt, pirms tā nav dokumentēta. Pēc rūpnīcas iestatījumu atjaunošanas iekārta pirms lietošanas jāpārkonfigurē un jāaizsargā, citādi tā var tikt uzlauzta atkārtoti.
4. **Ziņot CERT.LV:** tālrunis +371 67085888 (ziņojumus pieņem diennakts režīmā); e-pasts un citi kontakti – [cert.lv](https://cert.lv/lv/kontakti)


**► [Kiberdrošības gatavības pašnovērtējuma anketa \[PDF\]](https://cert.lv/uploads/Dokumentu-paraugi/Kiberdrosibas-gatavibas-pasnovertejuma-anketa_2026.pdf)**


**\[CERT.LV sagatavotās atbildes medijiem: 04.11.2026\]**


### **1. Cik kiberuzbrukumu saldēšanas sistēmām Latvijā līdz šim ir reģistrēti? Cik veiksmīgi tie bijuši?**

Pēdējās nedēļas laikā arī Latvijā ir novēroti kiberuzbrukumu mēģinājumi saldēšanas iekārtu vadības sistēmām. CERT.LV rīcībā esošā informācija šobrīd liecina, ka neviena Latvijas veikalu ķēde šajos uzbrukumos nav cietusi, taču ir konstatēts incidents kādā noliktavā.

Kopumā Latvijas privātajā sektorā identificētas aptuveni 50 potenciāli apdraudētas saldēšanas iekārtas, kuru vadības sistēmas ir eksponētas internetā. Tas gan nenozīmē, ka visas šīs iekārtas būtu kompromitētas, tomēr šāda pieejamība būtiski palielina kiberuzbrukumu risku. CERT.LV jau ir proaktīvi apzinājusi attiecīgo iekārtu īpašniekus, informējusi par konstatētajiem riskiem un sniegusi rekomendācijas to novēršanai.

CERT.LV regulāri veic Latvijas kibertelpas skenēšanu, lai proaktīvi identificētu nedroši internetā pieejamas industriālās vadības sistēmas un savlaicīgi brīdinātu to īpašniekus, tādējādi novēršot potenciālos incidentus. Šogad vien CERT.LV palīdzējusi novērst vairāk nekā 300 ar dažāda veida industriālajām vadības sistēmām saistītu drošības apdraudējumu, kuri potenciāli varēja radīt nopietnas sekas.


### **2. Vai ir bijuši gadījumi, kad uzbrucējiem izdevies pārņemt kontroli pār saldēšanas sistēmām vai citādi traucēt to darbību? Ja jā, kādi uzņēmumi vai nozares ir bijušas skartas?**

Latvijā pagaidām ir konstatēts tikai viens incidents, kas skāris kādas noliktavas saldēšanas sistēmu. Uzbrukums tika apturēts, tādēļ radītie zaudējumi ir minimāli.


### **3. Pret kādu nozaru uzņēmumiem šādi uzbrukumi tiek vērsti visbiežāk?** 

Līdz šim tā dēvētie “saldētavu uzbrukumi” Eiropā galvenokārt bijuši vērsti pret pārtikas tirdzniecības un uzglabāšanas uzņēmumiem, taču jaunākā informācija liecina par apdraudējumu arī medicīnas nozarei. Šonedēļ publiski ziņots par incidentu Francijā, kur uzbrucēji manipulējuši ar asins plazmas uzglabāšanas iekārtu temperatūras iestatījumiem. Lai gan būtiskas sekas izdevās novērst, šis gadījums apliecina, ka līdzīgi riski pastāv arī ārstniecības iestādēm, laboratorijām, farmācijas uzņēmumiem un citām nozarēm, kurās tiek izmantotas saldēšanas iekārtu vadības sistēmas.

Tādēļ CERT.LV īpaši aicina arī privātās ārstniecības iestādes, laboratorijas, farmācijas uzņēmumus un medicīnas preču izplatītājus pārbaudīt savu industriālo vadības sistēmu drošību, īpašu uzmanību pievēršot saldēšanas un temperatūras kontroles iekārtām.

Vienlaikus jāuzsver, ka uzbrucēju mērķis var būt ne tikai saldēšanas iekārtas. Līdzīgi drošības riski var skart arī citas operacionālās tehnoloģijas jeb OT sistēmas - piemēram, apkures katlu vadības sistēmas, ūdens sūkņus, ventilācijas un klimata kontroles iekārtas, saules enerģijas sistēmu vadības paneļus un citas attālināti pārvaldāmas industriālās iekārtas.

Tādēļ šis apdraudējums jāuztver daudz plašāk nekā tikai kā uzbrukumi saldētavām. Potenciāli apdraudēts var būt jebkurš uzņēmums, kura ikdienas darbība ir atkarīga no nepietiekami aizsargātām fizisko procesu vadības sistēmām. Uzņēmumiem ir būtiski pārliecināties, ka šīs sistēmas nav tieši pieejamas no interneta, attālinātā piekļuve ir pienācīgi aizsargāta un industriālās vadības sistēmas ir nodalītas no uzņēmuma kopējā IT tīkla.


### **4. Cik nopietnu apdraudējumu šādi kiberuzbrukumi rada?**

Šādi kiberuzbrukumi var radīt ļoti nopietnas sekas, jo atšķirībā no tradicionāliem kiberincidentiem, kuru rezultātā tiek nozagti dati vai traucēta informācijas sistēmu darbība, uzbrukumi industriālajām vadības sistēmām var tieši ietekmēt fiziskos procesus un iekārtu darbību.

Uzņēmumiem tas nozīmē ne tikai iespējamu finansiālu kaitējumu, bet arī ražošanas vai pakalpojumu sniegšanas pārtraukumus, produkcijas zudumus un atsevišķos gadījumos pat cilvēku veselības un drošības apdraudējumu.

Atkarībā no konkrētās iekārtas un tās drošības mehānismiem iespējama arī pārkaršana, ugunsgrēka risks vai citi fiziskās drošības apdraudējumi.

Tādēļ industriālo vadības sistēmu kiberdršība nav tikai IT speciālistu jautājums. Tā ir būtiska uzņēmuma darbības nepārtrauktības, finansiālās stabilitātes un risku pārvaldības sastāvdaļa, kurai uzmanība jāpievērš arī uzņēmuma vadības līmenī.


### **5. Kā tehniski iespējams īstenot šādus uzbrukumus? Kādas ievainojamības vai drošības nepilnības uzbrucēji izmanto?**

Uzbrukumos saldēšanas iekārtām netiek izmantota viena konkrēta ievainojamība. Visbiežāk uzbrucēji izmanto nepietiekami aizsargātas industriālās vadības sistēmas, kurām iespējams piekļūt attālināti.

Viens no izplatītākajiem scenārijiem ir internetā pieejamu saldēšanas iekārtu vadības paneļu meklēšana. Ja šādām sistēmām ir novecojusi programmatūra, zināmas drošības ievainojamības, vājas vai ražotāja sākotnēji iestatītās paroles, uzbrucēji var iegūt nesankcionētu piekļuvi un mainīt iekārtu darbības parametrus, tostarp temperatūras iestatījumus.

Otrs iespējamais scenārijs ir piekļuve industriālajām vadības sistēmām caur uzņēmuma kopējo datortīklu. Ja industriālās iekārtas nav pienācīgi nodalītas no biroja IT infrastruktūras, uzbrucējs, kurš sākotnēji kompromitējis, piemēram, darbinieka datoru vai uzņēmuma serveri, var mēģināt piekļūt arī ražošanas vai saldēšanas iekārtu vadības sistēmām.

Lai mazinātu šādus riskus, CERT.LV aicina uzņēmumus pārliecināties, ka industriālo iekārtu vadības paneļi nav tieši pieejami no publiskā interneta. Ja attālinātā piekļuve ir nepieciešama, jāizmanto droši piekļuves risinājumi, piemēram, atbilstoši konfigurēts VPN (virtuālais privātais tīkls), daudzfaktoru autentifikācija un unikālas, drošas paroles. Tāpat būtiski regulāri pārskatīt piekļuves tiesības, ievērot ražotāju drošības rekomendācijas un savlaicīgi veikt programmatūras atjauninājumus, ievērojot industriālo sistēmu darbības specifiku.

Labā kiberdrošības prakse paredz arī industriālo vadības sistēmu nodalīšanu no uzņēmuma kopējā IT tīkla. Tas palīdz ierobežot uzbrukuma izplatīšanos un mazina risku, ka, piemēram, viena biroja darbinieka datorā nonākusi ļaunatūra varētu ietekmēt uzņēmuma ražošanas vai saldēšanas iekārtu darbību.

Uzņēmumiem ieteicams apsvērt arī neatkarīgas temperatūras kontroles sistēmas ieviešanu, jo uzbrucēji var ne tikai mainīt iekārtu temperatūru, bet arī manipulēt ar ekrānos redzamajiem rādījumiem, radot iespaidu, ka viss darbojas normāli. Tādēļ būtiski pārliecināties, vai uzņēmumam ir alternatīvs veids, kā savlaicīgi konstatēt šādas novirzes.

Ja ir notikusi industriālo vadības sistēmu kompromitēšana, aicinām ziņot CERT.LV.


### **6. Kāda informācija ir pieejama par šo uzbrukumu veicējiem un viņu motīviem? Vai ir pamats uzskatīt, ka tie ir mērķēti uzbrukumi?**

Pagaidām neviens nav publiski uzņēmies atbildību par šiem uzbrukumiem, un, cik zināms, arī neviena valsts nav pagaidām nākusi klajā ar pierādījumos balstītiem secinājumiem par uzbrucēju izcelsmi. Tomēr uzbrukumu izpildījums liecina, ka to primārais mērķis, visticamāk, nav finansiāla labuma gūšana, bet gan apzināta iekārtu darbības traucēšana un zaudējumu radīšana. Tas norāda uz iespējamu sabotāžas un ietekmes operāciju raksturu, ko nevar vērtēt atrauti no pašreizējā ģeopolitiskā konteksta. Vienlaikus jāņem vērā, ka uzbrukumi var būt mērķēti uz konkrēta veida industriālajām iekārtām, nevis iepriekš izvēlētiem uzņēmumiem.


**\[Informācija publicēta: 03.11.2026\]**

## **NKDC brīdina par kiberuzbrukumiem operacionālo tehnoloģiju sistēmām**

Vairākās Eiropas valstīs ir konstatēti kiberdrošības incidenti, kuros uzbrucēji nesankcionēti piekļuvuši veikalu saldēšanas sistēmām, radot to darbības traucējumus, kā arī būtiskus finansiālus zaudējumus. Šādu kiberuzbrukumu mēģinājumi ir fiksēti arī Latvijā.

Ņemot vērā, ka uzbrucēju mērķis var būt ne tikai saldētavu sistēmas, bet arī citas operacionālo tehnoloģiju (OT) sistēmas, piemēram, apkures katli, ūdens sūkņi vai saules enerģijas sistēmu vadības paneļi, Nacionālais kiberdrošības centrs aicina organizācijas pārliecināties, ka to izmantotās OT sistēmas nav eksponētas un tieši pieejamas internetā. Tāpat ieteicams attālinātajai piekļuvei izmantot drošus risinājumus un daudzfaktoru autentifikāciju, kā arī nodalīt OT sistēmas no organizācijas vai uzņēmuma kopējā IT tīkla.

Kiberdrošības incidentu gadījumā aicinām nekavējoties ziņot Kiberincidentu novēršanas institūcijai CERT.LV, rakstot uz [cert@cert.lv](mailto:cert@cert.lv).
