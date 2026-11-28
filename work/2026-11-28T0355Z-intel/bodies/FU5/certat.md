---
title: Kritische Sicherheitslücken in NGINX Plus und NGINX Open Source - Updates verfügbar
url: https://www.cert.at/de/warnungen/2026/11/kritische-sicherheitslucken-in-nginx-plus-und-nginx-open-source-updates-verfugbar
hostname: cert.at
sitename: CERT.at
date: "2026-11-18"
fingerprint: "2dad15e9e6f7dd84"
language: de
filedate: "2026-11-28"
---
# Kritische Sicherheitslücken in NGINX Plus und NGINX Open Source - Updates verfügbar

18\. November 2026

## Beschreibung

In NGINX Plus und NGINX Open Source existieren mehrere Sicherheitslücken in den Modulen `ngx_http_v2_module` (HTTP/2), `ngx_http_v3_module` (HTTP/3) und `ngx_mail_proxy_module` (Mail-Proxy). Es handelt sich um Use-after-free-Schwachstellen sowie einen Heap-Buffer-Overflow, deren Ausnutzung zum Absturz von Worker-Prozessen und unter bestimmten Voraussetzungen zur Ausführung von beliebigem Code führen kann. F5 bewertet die Schwachstellen nach CVSS v4.0 als kritisch.

CVE-Nummer(n): CVE-2026-123007, CVE-2026-121810, CVE-2026-123633, CVE-2026-113425

CVSS Base Score: jeweils 8.1 (CVSS v3.1) bzw. 9.2 (CVSS v4.0)

## Auswirkungen

Durch Ausnutzen der Schwachstellen können Angreifer:innen aus der Ferne NGINX-Worker-Prozesse zum Absturz bringen (Denial-of-Service) oder deren Speicher korrumpieren. Auf Systemen, auf denen Address Space Layout Randomization (ASLR) deaktiviert ist oder ASLR umgangen werden kann, ist laut F5 zudem die Ausführung von beliebigem Code möglich.

Die Voraussetzungen unterscheiden sich je nach Schwachstelle:

- CVE-2026-123007: Konfigurationen, die HTTP/2 verwenden. Bei der Verarbeitung bestimmten Datenverkehrs kann das Flow-Control-Window den zulässigen Schwellwert überschreiten, was zu einem Heap-Buffer-Overflow führen kann.
- CVE-2026-121810: Konfigurationen, die HTTP/3 verwenden. Die Schwachstelle ist aus der Ferne und ohne Authentifizierung ausnutzbar; der Erfolg hängt zusätzlich von Bedingungen ab, die außerhalb der Kontrolle der Angreifer:innen liegen.
- CVE-2026-123633: Konfigurationen, die HTTP/2 für Client-Verbindungen verwenden und Anfragen an ein Backend weiterleiten. Die Schwachstelle ist durch eine speziell präparierte Anfrage ausnutzbar, wenn dem Worker-Prozess nur noch wenige `worker_connections` zur Verfügung stehen.
- CVE-2026-113425: Konfigurationen, in denen NGINX als Mail-Proxy eingesetzt wird. Die Schwachstelle ist durch eine speziell präparierte Mail-Sitzung ausnutzbar.

## Betroffene Systeme

- NGINX Open Source
  - 1.31.0 bis 1.31.8 (alle vier Schwachstellen)
  - CVE-2026-123007: 1.9.5 bis 1.30.6
  - CVE-2026-121810: 1.25.0 bis 1.30.6
  - CVE-2026-123633: 1.19.7 bis 1.30.6
  - CVE-2026-113425: 0.5.33 bis 1.30.6
- NGINX Plus 37.x
  - CVE-2026-123007 und CVE-2026-121810: 37.1.0 bis 37.2.0.1 sowie 37.0.0 bis 37.0.7.1
  - CVE-2026-123633: 37.1.0 bis 37.2.0 sowie 37.0.0 bis 37.0.6.1
  - CVE-2026-113425: 37.1.0 bis 37.2.0 sowie 37.0.0 bis 37.0.7
- NGINX Plus Rx
  - R34 bis R36 (alle vier Schwachstellen)
  - R33 (nur CVE-2026-113425)

Für F5 Distributed Cloud und NGINX One Console ist laut F5 noch nicht geklärt, ob sie betroffen sind.

## Abhilfe

F5 stellt Updates bereit, die alle vier Schwachstellen beheben:

- NGINX Open Source 1.31.9 bzw. 1.30.7
- NGINX Plus 37.3.0.1 bzw. 37.0.8.1

NGINX Plus 37.2.0.1 und 37.0.7.1 enthalten bereits einen Fix für CVE-2026-123633, sind jedoch weiterhin von CVE-2026-123007 und CVE-2026-121810 betroffen.

Für NGINX Plus R33 bis R36 sind derzeit keine Updates verfügbar. F5 empfiehlt hier ein Upgrade auf eine Version mit Fix.

Als Mitigation für CVE-2026-113425 empfiehlt F5, die Mail-Listener auf vertrauenswürdige Netzwerke zu beschränken. Für die übrigen drei Schwachstellen nennt F5 keine Mitigationen.

## Hinweis

Generell empfiehlt CERT.at, sämtliche Software aktuell zu halten und dabei insbesondere auf automatische Updates zu setzen. Regelmäßige Neustarts stellen sicher, dass diese auch zeitnah aktiviert werden.

## Informationsquelle(n):

*K000163926: NGINX ngx\_http\_v2\_module vulnerability CVE-2026-123007 (Englisch)
[https://my.f5.com/manage/s/article/K000163926](https://my.f5.com/manage/s/article/K000163926)*

*K000163927: NGINX ngx\_http\_v3\_module vulnerability CVE-2026-121810 (Englisch)
[https://my.f5.com/manage/s/article/K000163927](https://my.f5.com/manage/s/article/K000163927)*

*K000163928: NGINX ngx\_http\_v2\_module vulnerability CVE-2026-123633 (Englisch)
[https://my.f5.com/manage/s/article/K000163928](https://my.f5.com/manage/s/article/K000163928)*

*K000163931: NGINX ngx\_mail\_proxy\_module vulnerability CVE-2026-113425 (Englisch)
[https://my.f5.com/manage/s/article/K000163931](https://my.f5.com/manage/s/article/K000163931)*

*https://nginx2root.com/ (English)
[https://nginx2root.com/](https://my.f5.com/manage/s/article/K000163931)*
