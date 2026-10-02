---
title: Ktoś twierdzi, że ukradł dane 2 milionów pacjentów gabinetów stomatologicznych i nie jest to Fingerprint | Zaufana Trzecia Strona
author: Adam Haertle
url: https://zaufanatrzeciastrona.pl/post/ktos-twierdzi-ze-ukradl-dane-2-milionow-pacjentow-gabinetow-stomatologicznych-i-nie-jest-to-fingerprint/
hostname: zaufanatrzeciastrona.pl
description: Dzisiaj, 1 października około godz. 18 skontaktował się z nami ktoś ukrywający się pod pseudonimem "HORUS" i oznajmił, że ukradł dane 2 400 000 pacjentów, 712 000 osób z personelu medycznego oraz 1 200 000 recept.
sitename: Zaufana Trzecia Strona
date: "2026-10-01"
categories: ['Włamania']
tags: ['wyciek']
---
Dzisiaj, 1 października około godz. 18 skontaktował się z nami ktoś ukrywający się pod pseudonimem "HORUS" i oznajmił, że ukradł dane 2 400 000 pacjentów, 712 000 osób z personelu medycznego oraz 1 200 000 recept. Ofiarą ataku miała być firma FELG, twórca aplikacji najczęściej wybieranej przez gabinety stomatologiczne. Na firmowej stronie widnieje informacja, że z jej narzędzi korzysta ponad 16 000 dentystów.

Zaatakowana firma potwierdziła incydent. W swoim [komunikacie](https://status.felg.cloud/incydent?lang=pl) wskazuje, że sprawca ataku podaje, iż należy do grupy "Fingerprint" odpowiedzialnej za ataki na aplikacje MyDr, Medyc i Fakturownia. Wiemy jednak, że nie jest to prawda - ataku dokonała inna osoba lub osoby. FELG dodatkowo informuje, że sprawca sam zgłosił kradzież ok. 10% "danych z bazy", lecz liczby te nie zostały do tej pory potwierdzone.

Z wiadomości otrzymanej w odpowiedzi na nasze pytania wynika, że firma dowiedziała się o incydencie 28 września około godz. 18. Wyciek może dotyczyć danych ponad 2 milionów osób, a potencjalny zakres pozyskanych informacji obejmuje dane identyfikacyjne i kontaktowe, takie jak imię, nazwisko, numer PESEL i adres, a także dane medyczne oraz informacje związane z e-receptami, e-ZLA i weryfikacją w systemie eWUŚ. Wiemy też, że sprawcy zażądali okupu od zaatakowanej firmy za nieujawnianie wykradzionych danych.

### Jak doszło do włamania (według sprawcy)

Sam sprawca (dla uproszczenia będziemy posługiwali się liczbą pojedynczą, chociaż nie wiemy, czy jest to jedna osoba) skontaktował się z nami za pomocą poczty elektronicznej, a następnie na komunikatorze Session. Według informacji, które nam przekazał, do ataku doszło już 6 września, kiedy zaczął pobierać dane z systemów ofiary. Dane pobierał za pomocą API, korzystając ze źle zabezpieczonych endpointów. Według jego opowieści wystarczyło zwiększać wartość parametru zapytania, by otrzymywać dane kolejnych pacjentów, recept czy lekarzy (podatność typu IDOR).

Endpointy były dostępne podobno tylko po zalogowaniu, ale wystarczyło założyć konto demo w systemie. Według napastnika konto demo dawało także dostęp do danych produkcyjnych innych użytkowników, a interfejs nie sprawdzał uprawnień do danych. Napastnik twierdzi, że jego atak wykryto po kilku dniach, a błędnie działający endpoint został naprawiony. Odkrył on także inne endpointy z podobnymi błędami, z których nadal przez jakiś czas korzystał.

Sprawca włamania podesłał nam taki opis endpointów, których używał:

```
pdf/payments/html/1/d/{token p=<pid>} - dokumenty płatności pacjenta: dane osobowe + dane gabinetu
/prescription/get/patient/{pid} - lista recept pacjenta
/prescription/view/html/1/id/{elid} - pełny dokument recepty
/pdf/visits/html/1/id/{token p,l} - dokumentacja wizyt
/ajax/ezla/patient/id/{pid} - e-ZLA pacjenta
/pdf/payments/html/1/d/{token c=<cid>} - katalog firm: nazwa, NIP, adres
/ajax/chat/profil/uid/{jid} - profile personelu
/chat/avatar/jid/{uid} - awatary personelu
/docs/get/id/{pid} - drzewo plików pacjenta
/ajax/prescription/doctorget/patient/{uid} - listy pacjentów lekarzy
/ewus/pdf/s/{tok}/html/1/listids/{ids} - pełne PHI + tabele eWUŚ
```
Sprawca przekazał nam także zrzut ekranu wykradzionych danych:

### Dane użytkowników, nietypowe recepty

Włamywacz przekazał nam również wybrane dane osób publicznych, które podobno znalazły się w bazie. Są to numery PESEL, adresy zamieszkania, a także nazwy placówek, z których usług korzystały te osoby.

Sprawca podesłał nam także dane recept na leki takie jak Xanax czy Ozempic, twierdząc, że znalazł wiele recept wystawianych przez stomatologów na leki, które nie są związane z leczeniem w takich gabinetach. Nie byliśmy w stanie zweryfikować tych informacji.

Próbowaliśmy zweryfikować prawdziwość wykradzionych danych, przekazując sprawcy PESEL-e ośmiu osób, które wyraziły na taki eksperyment zgodę (dziękujemy za zaufanie). Żaden ze sprawdzanych PESEL-i nie znalazł się w bazie włamywacza.

### Tożsamość sprawcy

Choć w komunikacie FELG czytamy o hakerze podającym się za członka grupy "Fingerprint", to włamywacz, z którym rozmawialiśmy, przyznał, że wspominał, że stoi za atakami na firmy MyDr i Medyc w celu zrobienia większego wrażenia na ofierze w procesie wymuszenia okupu. Nie wspominał za to wprost, że nazywa się Fingerprint. Na wszelki wypadek skontaktowaliśmy się z prawdziwym Fingerprintem, który potwierdził, że nie jest autorem tego włamania, a nawet zaoferował pomoc zaatakowanej firmie (sic!) i podkreślił, że nigdy nie żądałby okupu.

### Co dalej z danymi

Zapytaliśmy włamywacza, jakie ma plany w związku z sytuacją, w której firma zerwała negocjacje i upubliczniła informacje o włamaniu. Odpowiedział, że planuje wystawić wykradzioną bazę danych na sprzedaż na Cebulce. Dodał także, że nie planuje podobnych publicznych akcji. Ta była rzekomo wyjątkowa, ponieważ firma, którą zaatakował, przez kilka dni negocjacji tylko traciła jego czas i ostatecznie nie chciała "wykorzystać pomocnej dłoni miłych pentesterów".

### Podsumowanie

To my już wolimy akcje Fingerprinta...

## Komentarze

Ładowanie komentarzy…

Brak komentarzy. Może jakiś napiszesz?
