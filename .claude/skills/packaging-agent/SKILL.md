---
name: packaging-agent
description: Klickstarke Titel für Stoische Karriere mit Reibung und Neugierlücke, höchstens sechzig Zeichen inklusive der Endung | Stoizismus. Anwenden bei jedem neuen Videotitel und im YouTube-Paket (Datei 12).
---

# Packaging Agent: Titel mit Reibung und Neugierlücke

Stand 12.10.2026. Deckt sich mit dem Konto-Skill `stoische-karriere-vidiq-regeln` (Abschnitt Titel) und ergänzt ihn um Reibung und Neugierlücke.

## Ziel

Ein Titel, der in einer Zeile drei Dinge leistet:
1. **Suchbegriff:** Problem oder Nutzen, das Männer ab fünfunddreißig tatsächlich eintippen, in den ersten vierzig Zeichen.
2. **Reibung:** ein Widerspruch oder eine Behauptung gegen die Erwartung („Warum Nettsein dich Respekt kostet“, „Schweigen schlägt jede Antwort“).
3. **Neugierlücke:** der Titel verrät, *dass* es eine Lösung gibt, aber nicht *welche*. Das Video schließt die Lücke, sonst bricht der Zuschauer ab.

## Harte Grenzen

- Höchstens **60 Zeichen inklusive** der Endung ` | Stoizismus` (13 Zeichen). Für den Kern bleiben also 47 Zeichen.
- Genau eine Zahl, gleich der Zahl der Werkzeuge im Video (normal 4). Im Titel ist die Ziffer erlaubt, die Ziffernsperre gilt für Sprechertext und Thumbnail-Text.
- Genau ein Wort in GROSSBUCHSTABEN, das Reibungswort.
- Keine Frage als Titel, keine poetischen Titel, kein Clickbait, das das Video nicht einlöst.
- Keine englischen Wörter. „stoisch bleiben“ nicht verwenden.
- Der Titel verspricht nur, was im Sprechertext wirklich steht (Lehre aus V2 „provozieren“ und V13 „Harvard-Methode“, siehe `kanal_redesign/00_Uebersicht.md`).

## Muster für Reibung

| Muster | Beispiel (nur Form, nicht übernehmen) |
|---|---|
| Gegen die Erwartung | Nett sein macht dich UNSICHTBAR: 4 Regeln |
| Fehler benennen | Der Fehler, der dich im Beruf KLEIN hält |
| Verlust | Was dich jeden Tag RESPEKT kostet |
| Kontrast Chef und Partnerin | Beim Chef stark, zu Hause STUMM? |

Die letzte Zeile ist eine Frage und deshalb nur als Thumbnail-Gedanke brauchbar, nicht als Titel.

## Ablauf

1. Thema, Werkzeugzahl und Kernsatz aus `01_Sprechertext_komplett` lesen.
2. Suchbegriff wählen (vidIQ Keyword-Daten, mit Hinweis weltweit oder Deutschland).
3. **Drei Varianten** schreiben, jede mit anderem Reibungsmuster.
4. Jede Variante zählen (Zeichen inklusive Endung) und als Tabelle ausgeben: Titel, Zeichen, Suchbegriff, Reibung, Neugierlücke.
5. Hauptvorschlag in vidIQ bewerten lassen (Ziel ab 75). Kostet Credits, nur nach Renes Ja.
6. „Vorbild:“ nennen: Konkurrenzvideo mit Titel, Kanal und Aufrufen. Abgewandelt, nie kopiert. Keine Aufrufzahl erfinden.
7. Abgleich mit dem Thumbnail: höchstens ein Wort aus dem Titel darf im Thumbnail stehen (siehe Skill `thumbnail-agent`).

## Zeichenzählung

```python
python -c "t='Nett sein macht dich UNSICHTBAR: 4 Regeln | Stoizismus'; print(len(t))"
```
