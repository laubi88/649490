---
name: retention-skript
description: Sprechertext für Stoische Karriere auf Zuschauerbindung bauen. Anti-43-Sekunden-Hook, CTA-Verbot bis 2:00, CTA 1 bei 30 bis 40 Prozent nach Werkzeug eins, CTA 2 bei rund 70 Prozent, Outro in den letzten rund zwanzig Sekunden. Anwenden bei jedem neuen Sprechertext.
---

# Retention-Skript

Stand 12.10.2026. Deckt sich mit den Konto-Skills `stoische-karriere-videovorlage` (Skriptaufbau, CTA-Leitfaden, CTA-Positionen) und `stoische-karriere-vidiq-regeln` (Hook). Strenger als dort ist nur das CTA-Verbot: bis 2:00 statt bis 1:00. Alle Valentino-Sprachregeln aus CLAUDE.md M2 gelten für jeden Satz.

## Zeitraster, abhängig von der Länge (Ziel acht bis zwölf Minuten)

| Teil | Lage | Länge |
|---|---|---|
| Anti-43-Sekunden-Hook (Block 1) | 0:00 bis rund 0:55 | rund fünfundfünfzig Sekunden |
| **CTA-Verbot** | **0:00 bis 2:00** | kein Daumen, keine Glocke, kein Abo, kein Kanalhinweis |
| Block 2, Block 3 (Werkzeug eins) | danach | |
| **CTA 1** | **direkt nach Werkzeug eins, bei 30 bis 40 Prozent** | rund zwanzig Sekunden |
| Block 4, Block 5 (Werkzeug zwei und drei) | | |
| **CTA 2** | **direkt nach Werkzeug drei, bei rund 70 Prozent** | rund zwanzig Sekunden |
| Block 6, Block 7 (Werkzeug vier, Schluss) | | |
| **Outro** | **am Ende, die letzten rund zwanzig Sekunden Sprechertext** | rund fünfzehn bis zwanzig Sekunden |
| Logo und Endcard | nach dem Outro | Logo vier Sekunden, Endcard zehn Sekunden (CLAUDE.md Teil B, A1 und A2) |

Rechenbeispiele (Zeit der Tonspuren ohne Endcard):

| Länge | CTA 1 (30 bis 40 %) | CTA 2 (rund 70 %) | Outro |
|---|---|---|---|
| 8:00 | 2:24 bis 3:12 | rund 5:36 | ab rund 7:40 |
| 10:00 | 3:00 bis 4:00 | rund 7:00 | ab rund 9:40 |
| 12:00 | 3:36 bis 4:48 | rund 8:24 | ab rund 11:40 |

Bei acht Minuten oder mehr liegen dreißig Prozent immer nach 2:00. Damit passen CTA-Verbot und CTA 1 zusammen. Liegt CTA 1 nach dem Schnitt trotzdem vor 2:00, ist das Video zu kurz oder Werkzeug eins zu früh. Dann Block 2 oder Block 3 ausbauen, nicht CTA 1 verschieben.

Die Zeiten stehen erst nach der Vertonung fest. Rechnen mit rund 125 Wörtern je Minute bei Valentino 0,90 (Erfahrungswert, siehe `kanal_redesign/00_Uebersicht.md`). Danach mit den gemessenen Längen aus `14_Tonspuren_Laengen` korrigieren und die Prozentwerte im Prüfprotokoll festhalten.

## Anti-43-Sekunden-Hook (0:00 bis 0:55)

Ziel: Der Zuschauer springt nicht um Sekunde dreiundvierzig ab. Dazu braucht der Hook vor dieser Stelle einen neuen Grund zum Bleiben.

| Zeit | Aufgabe |
|---|---|
| 0:00 bis 0:10 | Schmerz aus dem Alltag in drei Sätzen, Chef **und** Partnerin. Kein Gruß, kein Kanalname. |
| 0:10 bis 0:15 | Versprechen aus dem Titel, in eigenen Worten. |
| 0:15 bis 0:25 | Offene Schleife: ein konkretes Versprechen, das erst spät eingelöst wird („Das vierte Werkzeug wirkt am schnellsten.“). |
| 0:30 bis 0:43 | **Neuer Haken vor der Abbruchstelle:** eine überraschende Behauptung oder ein kurzer Befund mit Quelle, der die Erwartung bricht. |
| 0:43 bis 0:55 | Vorschau auf die Werkzeuge in einem Satz, Übergang in Block 2. |

Jede Behauptung im Hook braucht eine Quelle in `02_Quellen_Faktencheck`. Nichts erfinden.

## CTA-Texte (nach dem CTA-Leitfaden, je Video neu)

- **CTA 1:** Themenfrage, kurzer Bezug, „Darum kommt hier jede Woche ein Werkzeug dazu.“, „Wenn dich dieser Teil weitergebracht hat, lass einen Daumen hoch da.“, „Aktiviere die Glocke.“, „Und abonniere diesen Kanal.“, „Und jetzt zurück zu …“ plus eine Frage, die in Werkzeug zwei führt.
- **CTA 2:** Themenfrage als Kommentarfrage, „Beim Chef oder zu Hause?“, „Schreib es unter dieses Video.“, „Andere Männer lesen mit und merken, dass sie nicht allein sind.“, „Lass einen Daumen hoch da.“, „Aktiviere die Glocke.“, „Und abonniere diesen Kanal.“
- **Outro:** Themenfrage, ein Kernsatz, Ankündigung des nächsten Videos, „Lass einen Daumen hoch da.“, „Aktiviere die Glocke.“, „Und abonniere unseren Kanal.“, „Stoische.“, „Karriere.“
- Ein Wunsch je CTA, keine Produktwerbung. Die Sätze mit Daumen, Glocke und Abo bleiben wörtlich so, weil die Einblender A3a bis A3c darauf geschnitten werden (CLAUDE.md Teil B).

## Weitere Bindungsregeln

- Am Anfang von Werkzeug zwei und Werkzeug vier ein kurzer Neuanfang mit Nutzen, nur wenn er stimmt.
- Je Werkzeug mindestens ein Beispielsatz im Wortlaut, einmal beim Chef, einmal zu Hause.
- Die offene Schleife aus dem Hook wird sichtbar eingelöst („Hier ist das Werkzeug, das ich am Anfang versprochen habe.“).
- Block 7 enthält keine zweite Kommentarfrage.

## Format der Datei `01_Sprechertext_komplett`

```
DATEI: V15_Block1
TEXT:
Dein Chef übergeht dich in der Besprechung.

Zu Hause fragt deine Partnerin, warum du so still bist.

```

Danach prüfen: `python kanal_redesign/werkzeuge/sprechertext_pruefen.py <datei>` muss 0 Verstöße melden.
