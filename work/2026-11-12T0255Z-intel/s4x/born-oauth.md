---
title: Phishing-Mails von geknackten M365-Konten (OAuth 2.0-Angriffe)
author: Christian Krause
url: https://borncity.com/blog/2026/11/10/phishing-mails-von-geknackten-m365-konten-oauth-2-0-angriffe/
hostname: borncity.com
description: "Ein altes Problem: Phishing-Mails von Absendern, mit denen Angreifer E-Mail-Konten von Microsoft 365 übernehmen wollen. Ein Leser hat mich aktuell auf eine solche Phishing-Kampagne in diesem Umfeld…"
sitename: Borns IT- und Windows-Blog
date: "2026-11-10"
categories: ['Cloud', 'Mail', 'Sicherheit']
tags: ['M365', 'Mail', 'Sicherheit']
fingerprint: "718cb047ccac8cf"
---
Ein altes Problem: Phishing-Mails von Absendern, mit denen Angreifer E-Mail-Konten von Microsoft 365 übernehmen wollen. Ein Leser hat mich aktuell auf eine solche Phishing-Kampagne in diesem Umfeld hingewiesen, bei dem ein Microsoft Code angezeigt und dessen Eingabe vom Nutzer in einem zweiten Fenster erwartet wird. Es handelt sich mutmaßlich um Passwort-lose OAuth 2.0-Angriffe auf Microsoft-Login-Seiten mittels Evil Tokens.


## Aktuelle Phishing-Masche auf MS365

Blog-Leser Jonathan S. hat mich zum 9. November 2026 per Mail kontaktiert und über eine Phishing-Kampagne informiert (danke dafür). Dazu schrieb er mir:

Bei uns laufen gerade wieder verstärkt Phishing-Mails aus gehackten (MS365-)Postfächern auf.


Der Leser schrieb, dass ihm eine Masche untergekommen sei, die er so auch noch nicht kannte und die er noch nicht komplett verstehe. Nachfolgend ist eine solche Phishing-Mail im Ausschnitt zu sehen, wobei einige persönliche Angaben geschwärzt wurden.

Es wird ein Angebot für ein fiktives Bauvorhaben von einem Absender per E-Mail angefordert, wobei eine PDF-Datei als Anhang mit gesendet wird. Der Blog-Leser schrieb, dass er die Hinweise in den Phishing-Mails an einem Test-Rechner durchprobiert habe. Dazu schrieb er mir, dass er Folgendes herausgefunden habe:

Soweit ich es von einem Testgerät aus durchgespielt habe, wird man auf der verlinkten Webseite aufgefordert, sich mit einem angezeigten Code bei Microsoft zu verifizieren. Mir ist bislang nicht klar geworden, was die Eingabe des Codes im Detail bewirken würde – aber es wird nichts Gutes sein.


Der Leser hat mir dann den nachfolgenden Screenshot einer Seite mit einer solchen Aufforderung zur Eingabe eines Codes zukommen lassen.

Der Benutzer erhält eine Aufforderung, sich über den Code beim eigenen Microsoft-Konto zu verifizieren. Die Seite beschreibt genau, was zu tun ist. Dann gelangt der Nutzer über *Mit Microsoft verifizieren* zur echten Microsoft Anmeldeseite (siehe folgende Abbildung).

Aber was passiert im Hintergrund, und was hat das Ganze für einen tieferen Sinn?

## Die vermutliche Aufklärung der Masche

Zu der Phishing-Masche kann ich vermutlich etwas beitragen, denn mir fiel sofort ein Blog-Beitrag vom Juni 2026 ein. Es gibt ein Phishing-as-a-Service (PhaaS)-Kit namens EvilTokens. Dieses wurde entwickelt und wird angeboten, um Microsoft 365-Konten zu kompromittieren. EvilTokens missbraucht den OAuth 2.0-Autorisierungsablauf für Geräte. Da hilft auch keine 2FA-Absicherung mehr, wenn der Nutzer sich überrumpeln lässt. Die Vorgehensweise der Angreifer in kompakter Form:

- Das Opfer erhält eine E-Mail oder Nachricht, die oft als Rechnung, geteiltes Dokument, Kalendereinladung oder SharePoint-Zugriffsanfrage getarnt ist. Der Köder besteht aus einer verlinkten Täuschungsseite, die sich als vertrauenswürdige Marke oder Dienst ausgibt (oder die oben erwähnte Anfrage).
- Klickt das Opfer auf diesen Köder, fordert die über den Link aktivierte die Phishing-Seite einen Gerätecode von Microsoft an (siehe obiger Screenshot). Der Code ist nur 15 Minuten lang gültig, daher sind Zeit und Timing hier entscheidend.
- Die Phishing-Seite zeigt dem Opfer den Code an und leitet die Person auch zum echten Anmeldeportal von Microsoft unter *microsoft.com/devicelogin* weiter. Dabei schlägt die Falle zu, da der vom Opfer dort eingegebene Code die Sitzung des Angreifers autorisiert.
- Da eine gültige Anmeldung bestätigt wird, stellt Microsoft Zugriffs- und Aktualisierungstoken für die vom Angreifer eröffnete Sitzung aus. Das Opfer hat über diesen Vorgang unwissentlich das Gerät des Angreifers autorisiert.

Die Kriminellen erhalten so Zugriff auf das Konto und können auf Unternehmens-E-Mails, Dateien, Teams, SharePoint, OneDrive und andere Microsoft 365-Ressourcen des betreffenden Kontos zugreifen. Sie können anschließend Daten von diesen Ressourcen abziehen oder BEC-Angriffe vorbereiten. Mehr Details finden sich im Blog-Beitrag [EvilTokens: Passwort-lose OAuth 2.0-Angriffe auf Microsoft-Login-Seiten](https://borncity.com/blog/2026/06/17/eviltokens-passwort-lose-oauth-2-0-angriffe-auf-microsoft-login-seiten/) vom im Juni 2026.

Funktioniert das auch, wenn ein Nitrokey für MFA genutzt wird?

Kurz gesagt:

JA!

Du authentifizierst dich auf der echten MS Seite mit deinen echten Zugangsdaten (ob PW Fingerprint Irisscan DNAScan oder Key ist da irrelevant) ein vollkommen legitimer Vorgang… da sitzt der Hacker nicht dazwischen.

Was dann passiert gibt dem Hacker aber den Zugang; wenn du den Code eingibst, authorisierst du das angreifende Gerät als legitimes Gerät… da spielt dann auch dein Key keine Rolle mehr… der wird da nicht nochmals geprüft da du dich ja bereits erfolgreich und korrekt eingelockt hast.

Das einzige, was da m. W. hilft, ist per Conditional Access "Device Code Flow" zu verbieten.

@administrathor: Hast Du uns dazu einen Link (Microsoft, o.ä.), wie das in den Conditional access policies geht?

https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows

Danke. Sehr hilfreich.

Hier findest du noch viel mehr Infos was alles möglich ist und wie du es konfigurieren musst.

https://jeffreyappel.nl/

Das ist die richtige Antwort.

Nicht mehr ganz neu, daher gibt es auch die MS CA Regel für Device Code Flow.

Für alle M365 Konten ist das die Standardempfehlung bei meinen Kunden. Man muss nur die Ausnahmen definieren, wenn man z.B. einen Meeting Raum mittels Teams Rooms Lizenz mit den Geräten verbinden will. Aber das macht man ja nur 1x und dazu gibt es ja extra Rooms User. Standard M365 Konten sollten damit nichts am Hut haben.

Die Authentifizierungsmethode nennt sich "Device Code Flow".

Und diese Authentifizierungsmethode sollte wie in dem anderen Artikel erwähnt, per Conditional Access Richtlinie in Entra geblockt werden.

Die Autorisierung und Freigabe von APPs oder Geräten in dem Bereich sollte in der Regel beim Administrator und nicht beim einzelnen Anwender liegen.

Conditional access schön und gut, Conditional access ist aber nicht für alle verfügbar (z.B. nicht in Business Basic oder Standard), sondern setzt entsprechende Lizenzen voraus.

Daher Sicherheitsstandards aktivieren (Die sauberste Lösung)

Microsoft hat die Security Defaults so konzipiert, dass sie grundlegende Sicherheitsfunktionen für Tenants ohne Premium-Lizenzen bereitstellen. Sobald Sie die Sicherheitsstandards aktivieren, wird der Device Code Flow automatisch und ausnahmslos blockiert.

Die Sicherheitsstandards sind grandios. 👍

Für alte Tenants mit Sicherheitsstandards wird der Device Code Flow aber nicht blockiert, oder?

https://learn.microsoft.com/en-us/entra/fundamentals/security-defaults erwähnt "Starting July 1, 2026, all new Microsoft Entra tenants block device code flow as part of security defaults. Applications or devices that depend on device code flow won't be able to complete sign-in while security defaults are enabled.".

Im Tenant unserer Hauptfirma war bereits eine von Microsoft erstelle Richtlinie "Block device code flow" vorhanden, wobei ich nicht mehr sicher bin, ob die von Anfang an standardmäßig aktiv war.

Im separaten (sehr viel neueren) Tenant einer unserer anderen Firmen war keine entsprechende Richtlinie vorhanden, dort habe ich jetzt selbst eine gebaut.

Danke fürs Nachschauen.

Wir haben auch gesehen, dass der Device Code Flow nur bei einem Teil der Tenants mit Sicherheitsstandards aktiv ist.

Der beste Schutz ist, keinen Account bei MS zu haben.

Wir hatten hier auch schon solche Aktionen. Sehr gut gemacht mit Mail mit der passenden Projeknummer, passender Antwort zur letzen Mail usw. KI hilft auch da…

Da musste selbst ich genau hinschauen. Aber mangels Token, das hätte geklaut werden können wäre das in keinem Fall eskaliert.

@Werner

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Sehr gut gemacht mit Mail mit der passenden Projeknummer, passender Antwort zur letzen Mail usw.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Naja da sitzen die aber bereits irgendwo in der Kette, den das kann auch keine KI herbeifabulieren….oder der Angreifer ist direkt intern…

und was würde sich da unter Linux/OS ändern? Nix!

Bei Ausschreibungen im Baugewerbe musst Du sehr viele Firmen anmailen, um überhaupt noch eine auswertbare Anzahl von Angeboten zu bekommen.

Obwohl viele, selbst kleine Firmen eine Domain (für Werbung) haben, mailen die meisten über Free-Mail-Accounts bei den üblichen Verdächtigen und viele nutzen sicher nur die Top10 der Passwortliste!

Wir bekommen überraschend viele Phishing-Mails als "Re:", welche auf Basis solcher Mails generiert wurden.

Der Name des Original-Empfängers wird verwendet, nur die E-Mail-Adresse passt so gar nicht.

Ich erzwinge darum in Thunderbird die Anzeige der E-Mail-Adressen und weise regelmäßig darauf hin, dass nur diese relevant ist.

Mit Outlook und Exchange muss ich mich zum Glück nicht aktiv beschäftigen!

Ich sehe jetzt nicht, dass Werner irgendwas von Linux geschrieben hat.

Dein Getriggert sein diesbezüglich scheint mittlerweile groteske Formen anzunehmen.

Die Mails kommen in aller Regel von gehackten Mailkonten anderer Firmen. Und wenn dort entsprechende Nachrichtenverläufe vorhanden sind, wird auch gerne direkt auf diese geantwortet.

Wenn der Angreifer bereits irgendwo in der Kette sitzt oder einer der Rechner Kompromittiert worden ist, wird es sehr schwierig egal ob du nun mit mit Linux oder Windows hantierst.

Des Spaßes halber kannst du ja mal eine Rundmail in den Verteiler senden, es ist Mitte November 2026, die Kritischen Tage an denen man besonders gut aufpassen sollte, wie…

Start Black Week Montag, 20. November 2026

Black Friday Freitag, 27. November 2026

Black Weekend 28.–29. November 2026

Cyber Monday Montag, 30. November 2026

Cyber Week (Nachläufer) 1.–5. Dezember 2026

stehen uns erst noch bevor und dann kommt noch Weihnachten und die ganzen Umtausch Aktionen im Januar 2027.

Ich kann nur sagen Leute gebt acht, sensibilisiert eure Mitarbeiter und bringt sie nicht in Letzter Sekunde in Hektik.

Die Info und eine ähnliche E-Mail (OneDrive) Link haben wir gestern auch von einem Kollegen bekommen.

War uns auch neu und sieht verdammt echt aus.

Kam von einem Kunden (gehacktes Postfach).

Hier noch zwei interessante Links von Microsoft:

https://www.microsoft.com/en-us/security/blog/2025/02/13/storm-2372-conducts-device-code-phishing-campaign/?msockid=0342e3e2210667b50e37f55f203f6668

https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/

Ist das hier eine Fake-Meldung: https://www.periculo.co.uk/cyber-security-blog/cve-2026-109469-what-we-know-so-far-about-the-microsoft-entra-flaw ?

Sieht nicht so aus. Google "wirft" mehrere Ergebnisse mit CVE-2026-109469

Der Wert von 10.0 wird aber hier aber gut erklärt: https://shattered.io/de/microsoft-patchday-november-2026-entra-cve-2026-109469/

Kann ich bestätigen. Ich habe auch eine E-Mail eines echten, gehackten M365 Kontos bekommen. Die Sache / E-Mail war mir aber gleich suspekt. Interessant ist aber, dass der verlinkte Text in meinem Fall zu miro.com weitergeleitet wurde und man dort nochmal was tun sollte, um das Board anzuschauen. Spätestens dann sollten die Alarmglocken läuten. Wie das PDF, welches man erst anschauen kann, wenn man Dinge tut. Via LinkedIn (anderer Kanal als E-Mail) habe ich den Absender dann darüber informiert.

Ja, das mit dem alternativen Kanal kann man nicht oft genug sagen. Dass die Telefonnummern in den Signaturen ausgetauscht werden, halten immer noch viele Leute für ein eher theoretisches Szenario. Wir haben das jetzt bei solchen Mails aber bereits mehrfach festgestellt, das ist also durchaus ein reales Phänomen.
