---
title: "Gestohlene Token: Secret-Stealer in Tausenden GitHub-Repositories"
author: Heise Online; Robert Lippert
url: https://www.heise.de/news/Gestohlene-Token-Secret-Stealer-in-Tausenden-GitHub-Repositories-11524706.html
hostname: heise.de
description: Über gekaperte GitHub-Konten richten Angreifer Hintertüren bei AWS und Azure ein. Secrets auszutauschen reicht deshalb nicht.
sitename: Heise Online
date: "2026-11-13"
categories: ['IT']
tags: ['Aikido', 'Amazon Web Services', 'GitHub', 'GitHub Actions', 'IT', 'Open Source', 'Security']
fingerprint: "82dafe9b87c92743"
language: de
image: https://heise.cloudimg.io/v7/_www-heise-de_/imgs/18/5/2/0/1/3/8/6/shutterstock_1569354004-42eff2fc6e8e8a4b.jpg?func=bound&height=1200&org_if_sml=1&q=85&width=1200
pagetype: website
filedate: "2026-11-28"
---
# Gestohlene Token: Secret-Stealer in Tausenden GitHub-Repositories

Über gekaperte GitHub-Konten richten Angreifer Hintertüren bei AWS und Azure ein. Secrets auszutauschen reicht deshalb nicht.

- Robert Lippert

Mit gestohlenen Zugriffstoken für GitHub-Konten schleusen unbekannte Angreifer seit Dienstag Schadcode in Repositories ein, der die Secrets aus GitHub Actions und Cloudzugangsdaten abgreift.

Das Sicherheitsunternehmen Aikido zählt im Rahmen der  [auf den Namen wfx-loot](https://www.aikido.dev/blog/compromised-github-accounts-push-ci-secret-stealer-to-tens-of-thousands-of-repositories) getauften Kampagne bereits 4837 übernommene Konten, über die die Angreifer 61.764 Repositories attackiert haben. In mehr als 1800 Fällen sollen Workflows den Schadcode bereits ausgeführt haben.

Die Angreifer nutzen anscheinend keine Lücke in GitHub Actions aus, sondern missbrauchen die Schreibrechte gestohlener Token. Woher diese stammen, ist nur teilweise geklärt. [Laut Fly.io](https://community.fly.io/t/security-github-tokens-exposed-by-apps-deployed-from-github/29070) wurden Token seiner GitHub-App missbraucht, die aus öffentlich erreichbaren .git/config-Dateien stammten; der Hoster widerruft sie. Eine Stellungnahme von GitHub liegt noch nicht vor.

Das Sicherheitsunternehmen SafeDep hat [Schadcode-Commits](https://safedep.io/blog/github-actions-wfx-credential-stealer) bereits in über 8000 öffentlichen Repositories gefunden. Noch am Donnerstagmittag listete die GitHub-Suche mehr als 66.000 der typischen Test-Pull-Requests, rund 4300 davon vom selben Tag.

[Ähnlich wie zuletzt beim Wurm testmetest](https://www.heise.de/news/Angreifer-kapern-42-GitHub-Repositories-fuer-npm-Wurm-Kampagne-testmetest-11503164.html) erreichen Angreifer laut Aikido über Mitwirkenden- und Organisationsrechte mit über 10.000 Test-Pull-Requests auch Repositories, die den übernommenen Konten nicht selbst gehören. Damit können auch Organisationen betroffen sein, deren eigene Zugangsdaten gar nicht gestohlen wurden. Dürfen die Workflows eines Repositorys auf AWS oder Azure zugreifen, nutzt der Schadcode die erbeuteten Zugänge, um Hintertüren in den Cloudkonten einzurichten.

### Spuren oft binnen einer Minute verwischt

Die Angreifer lassen ihren Opfern kaum Zeit zu reagieren. Sie öffnen zunächst einen Pull Request, um die Schreibrechte zu bestätigen. Dann folgt der eigentliche Schadcode: ein Shellskript, das die Angreifer in einen bestehenden Workflow einfügen, als neuen Workflow ablegen oder in npm-Projekten bei jeder Installation starten lassen.

Meist schon innerhalb einer Minute machen die Angreifer die Änderungen rückgängig und löschen den Workflow-Lauf samt Logs. Oft weist nur eine fehlende Laufnummer auf den Angriff hin. Eine Branch-Protection für vorgeschriebene Status-Checks kann das Skript mit gefälschten Erfolgsmeldungen aushebeln. Aikido zufolge setzt das Skript solche gefälschten Status-Checks tatsächlich ab; in den von SafeDep untersuchten Proben war diese Funktion dagegen nicht aktiviert.

Neben Token für KI-Dienste wie OpenAI, Anthropic oder Cursor fischt das eingeschleuste Skript insbesondere die Secrets aus GitHub Actions ab, außerdem Zugangsdaten für Clouddienste, Container-Umgebungen, Paketregister und SSH.

Haben die Bedrohungsakteure erst einmal Zugang zu Sitzungen bei AWS, Google Cloud und Azure, geht der Angriff weiter: Bei AWS öffnet das Skript eine IAM-Rolle für jedes AWS-Konto, in Azure trägt es zusätzliche Anmeldewege für Workflows aus dem kompromittierten Repository ein. Erbeutete Daten schickte das Skript laut Aikido in dieser Kampagne per HTTP an Server der Angreifer. SafeDep fand in untersuchten Payloads zudem eine Exfiltration über Telegram.

### Selbsttest: Ein Pull Request verrät das gekaperte Konto

Entwicklerinnen und Entwickler, die seit Dienstag einen Branch `wfx-docs`, den Pull-Request `docs: dependency audit notes` oder Commits wie `ci: refresh build cache`, `chore: add ci helper` und `chore: add dependency audit workflow` in ihren Repositories finden, sollten das zugehörige Konto als kompromittiert ansehen, auch wenn noch kein Schadcode folgte. Verdächtig sind laut den Sicherheitsforschern von Aikido zudem kurzlebige Branches, die mit chore/ beginnen und auf acht Zufallszeichen enden. Betroffene sollten Token, OAuth-Freigaben und SSH-Schlüssel ihres Kontos widerrufen.

Wurde bereits Schadcode ausgeführt, müssen Betroffene neben dem Austausch der Secrets auch die Hintertüren eigens entfernen, etwa AWS-Rollen, die jedem Konto vertrauen, oder in Azure Federated Credentials mit dem Präfix `wfx-ci-`. Wer `npm install` auf einem betroffenen Commit ausgeführt hat, muss auch den eigenen Rechner als kompromittiert betrachten.

Der Schadcode gelangte auch in Paketdistributionen. Aikido nennt das Packagist-Paket `digitalelvis/neuronai-studio` 3.14.3 sowie die Go-Modul-Versionen `github.com/onuragtas/docker-env` v1.0.278 und v1.0.280. SafeDep führt darüber hinaus `github.com/onuragtas/redock`, eine weitere docker-env-Version und eine über den Go-Modul-Proxy verfügbare Pseudo-Version von `github.com/vkuznet/gocurl` auf. Bei den Go-Modulen liegt der Schadcode in einer GitHub-Actions-Workflow-Datei; ein gewöhnlicher Go-Build führt diese nicht aus. Wer ein solches Modul lediglich als Go-Abhängigkeit einbindet, ist dadurch wahrscheinlich nicht betroffen.

([mro](mailto:manuel.masiero@heise.de))
