---
name: retention-skript
description: Sprechertext für Stoische Karriere auf Zuschauerbindung bauen. Anti-43-Sekunden-Hook von 0:00 bis 0:55, CTA 1 bei rund siebzig Prozent, CTA 2 bei 8:00, Outro ab 8:10.
---

# 03 Retention-Skript

Stand 12.10.2026. Ergänzt die Konto-Skills `stoische-karriere-videovorlage` (Skriptaufbau, CTA-Leitfaden) und `stoische-karriere-vidiq-regeln` (Hook). Die Zeitpunkte für CTA1, CTA2 und Outro in dieser Datei ersetzen die älteren Angaben (Rene, 12.10.2026, siehe CLAUDE.md A5). Alle Valentino-Sprachregeln aus CLAUDE.md A2 gelten für jeden Satz.

## Zeitraster (Zielwerte nach dem Schnitt)

| Zeit | Teil | Inhalt |
|---|---|---|
| 0:00–0:55 | Anti-43-Sekunden-Hook | siehe unten |
| 0:55–rund 70 % | Block 2 bis Werkzeug drei | Ursache, Denker, Werkzeug eins bis drei |
| rund 70 % | **CTA 1** | rund zwanzig Sekunden |
| danach bis 8:00 | Werkzeug vier, Schluss | Studie, Zusammenfassung, Aufgabe für die Woche |
| **8:00** | **CTA 2** | rund zehn Sekunden (siehe Hinweis) |
| **ab 8:10** | **OUTRO** | Themenfrage, Kernsatz, nächstes Video, „Stoische.“ / „Karriere.“, danach Endcard |

Bei Outro ab 8:10 liegt die Gesamtlänge bei rund 8:30 plus Endcard. Bei 8:30 liegt CTA 1 damit bei rund 5:55.

**Hinweis CTA 2:** Zwischen 8:00 und 8:10 bleiben zehn Sekunden. Der CTA-Leitfaden plant rund zwanzig. CTA 2 deshalb kurz halten: Kommentarfrage, „Schreib es unter dieses Video.“, fertig. Daumen, Glocke und Abo kommen im Outro.

Die Zeiten stehen erst nach der Vertonung fest. Rechnen mit rund 125 Wörtern je Minute bei Valentino 0,90 (Erfahrungswert aus `sprechertext_pruefen.py`), danach mit den gemessenen Längen aus `14_Tonspuren_Laengen` korrigieren.

## Anti-43-Sekunden-Hook (0:00 bis 0:55)

Ziel: Der Zuschauer springt nicht um Sekunde dreiundvierzig ab. Dazu braucht der Hook vor dieser Stelle einen neuen Grund zum Bleiben.

| Zeit | Aufgabe |
|---|---|
| 0:00–0:10 | Schmerz aus dem Alltag in drei Sätzen, Chef **und** Partnerin. Kein Gruß, kein Kanalname. |
| 0:10–0:15 | Versprechen aus dem Titel, in eigenen Worten. |
| 0:15–0:25 | Offene Schleife: ein konkretes Versprechen, das erst spät im Video eingelöst wird („Das vierte Werkzeug wirkt am schnellsten.“). |
| 0:30–0:43 | **Neuer Haken vor der Abbruchstelle:** überraschende Behauptung oder kurzer Befund mit Quelle, der die Erwartung bricht. |
| 0:43–0:55 | Vorschau auf die Werkzeuge in einem Satz, Übergang in Block 2. |

- In den ersten sechzig Sekunden kein CTA.
- Jede Behauptung im Hook braucht eine Quelle in `02_Quellen_Faktencheck`. Nichts erfinden.

## Weitere Bindungsregeln

- Am Anfang von Werkzeug zwei und Werkzeug vier ein kurzer Neuanfang mit Nutzen, nur wenn er stimmt.
- Je Werkzeug mindestens ein Beispielsatz im Wortlaut, einmal beim Chef, einmal zu Hause.
- Die offene Schleife aus dem Hook wird sichtbar eingelöst („Hier ist das Werkzeug, das ich am Anfang versprochen habe.“).
- Jede CTA und das Outro beginnen mit einer Frage aus dem Thema des Videos (CTA-Leitfaden).

## Format der Datei `01_Sprechertext_komplett`

```
DATEI: V15_Block1
TEXT:
Dein Chef übergeht dich in der Besprechung.

Zu Hause fragt deine Partnerin, warum du so still bist.

```

Danach prüfen: `python kanal_redesign/werkzeuge/sprechertext_pruefen.py <datei>` muss 0 Verstöße melden.
