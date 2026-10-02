---
title: Nowe włamanie "Fingerprinta" - ofiarą firma Fakturownia.pl | Zaufana Trzecia Strona
author: Adam Haertle
url: https://zaufanatrzeciastrona.pl/post/nowe-wlamanie-fingerprinta-ofiara-firma-fakturowniapl/
hostname: zaufanatrzeciastrona.pl
description: Otrzymaliśmy wiarygodne informacje wskazujące na to, że "Fingerprint", stojący za włamaniami do dwóch serwisów medycznych, tym razem dobrał się do infrastruktury jednej z największych firm oferujących usługi fakturowania, prowadzenia księgowości czy magazynu online. Z Fakturownia.pl wykradł wiele in...
sitename: Zaufana Trzecia Strona
date: "2026-09-29"
categories: ['Włamania']
tags: ['wyciek']
---
Otrzymaliśmy wiarygodne informacje wskazujące na to, że "Fingerprint", stojący za włamaniami do dwóch serwisów medycznych, tym razem dobrał się do infrastruktury jednej z największych firm oferujących usługi fakturowania, prowadzenia księgowości czy magazynu online. Z Fakturownia.pl wykradł wiele informacji dotyczących klientów, w tym podobno także wiele wystawionych faktur.

Dzisiejszego poranka "Fingerprint", który z jakiegoś powodu wybrał sobie naszą redakcję jako punkt kontaktowy, umożliwiający przekazywanie doniesień o jego najnowszych osiągnięciach, poinformował nas, że wykradł 6 TB faktur. Chwilę później przekazał nam zrzuty ekranu wskazujące, że uzyskał dostęp do danych firmy Fakturownia.pl.

Otrzymaliśmy trzy dowody dostepu do systemów Fakturowni.

Pierwszy to folder aplikacji, w którym widać różne charakterystyczne nazwy plików wskazujące, że sprawca miał dostep do serwera aplikacyjnego.

Drugi to pogląd listy klientów firmy, a w zasadzie jej wycinek.

Trzeci, wskazujący na szeroki dostęp do danych, to lista plików, których nazwy wskazują na to, że jest to wyeksportowana baza danych zawierająca informacje potrzebne do funkcjonowania firmy takiej jak Fakturownia - przypuszczalnie jednego z głównych repozytoriów wiedzy o klientach.

### Co jeszcze przekazał nam "Fingerprint"

Dodatkowo "Fingerprint" poinformował nas, że pozyskał 6 TB faktur - tej informacji nie byliśmy w stanie zweryfikować. Przeprosił też, że "musiał pobrać dane", ponieważ jego doświadczenie wskazuje, że gdyby tych danych nie pobrał, to nikt by się zgłoszeniem błędów nie zainteresował. Dowiedzieliśmy się także, że dane pobrał do swojego własnego środowiska, a serwery, przez które dane wytransferował, służyły jedynie do tunelowania ruchu.

Zapytany o to, jak dostał się do Fakturowni, odpowiedział, że wykorzystał tzw. wyrocznię czasową (nie sprecyzował, ale pewnie chodzi o time-based blind SQL injection, czyli zgadywanie wartości w bazie danych na podstawie czasu odpowiedzi na zapytania) do wyciągnięcia klucza głównego (master key) Ruby, a następnie sfałszowania za jego pomocą ciasteczka, dzięki któremu osiągnął zdalne wykonanie kodu na serwerze. Brzmi to skomplikowanie, ale z drugiej strony jest możliwym scenariuszem realnego ataku.

Dodał także, że celowo nie usuwał logów, by firma mogła prześledzić przebieg ataku i nauczyć się lepiej zabezpieczać dane swoich klientów.

### Reakcja Fakturowni

Firma zareagowała bardzo sprawnie i uczciwie. Przed chwilą na jej stronie [pojawił się komunikat](https://fakturownia.pl/incydent), z którego wynika, że mogły zostać wykradzione:

- dane kont firm i użytkowników, w tym skróty haseł,
- tokeny sesji, tokeny API i tokeny integracji generowane po stronie Fakturowni,
- rachunki bankowe, dane o płatnościach,
- dane kontrahentów klientów (wszystkich) i dane z faktur (częściowo, prawdopodobnie do 2023 roku),
- klucze i hasła systemowe aplikacji.

Firma wykonała także w bardzo krótkim czasie od otrzymania informacji o incydencie szereg czynności:

- Rozpoczęła pracę nad zabezpieczeniem danych i dostępów.
- Prowadzi rotację kluczy aplikacji i haseł usług.
- Uruchomiła nowe serwery aplikacji i odcięła dostęp osobom nieuprawnionym.
- Rozpoczęła analizę incydentu wspólnie z zewnętrznymi specjalistami ds. bezpieczeństwa i wprowadziła szereg dodatkowych zabezpieczeń, w tym dot. generowania plików PDF.
- Zgłosilła incydent na Policję (Centralne Biuro Zwalczania Cyberprzestępczości), CERT Polska oraz do Prezesa Urzędu Ochrony Danych Osobowych.

## Komentarze

Ładowanie komentarzy…

Brak komentarzy. Może jakiś napiszesz?
