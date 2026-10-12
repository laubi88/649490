---
name: thumbnail-agent
description: Thumbnails für Stoische Karriere planen und mit thumbnail_maker.py erzeugen. Zwei bis drei Wörter, Zeile 1 Weiß, Zeile 2 Türkis #00E5FF, Schattenverlauf links, Carrara-Marmorbüste rechts.
---

# 02 Thumbnail Agent

Stand 12.10.2026. Ergänzt den Konto-Skill `stoische-karriere-vidiq-regeln` (Abschnitt Thumbnail). Wo sich beide widersprechen, gilt diese Datei (Rene, 12.10.2026), siehe CLAUDE.md A5.

## Aufbau (fest)

| Bereich | Inhalt |
|---|---|
| Links, rund 60 Prozent | dunkler Schattenverlauf, fast schwarz am Rand, weich auslaufend. Darauf der Text, linksbündig |
| Rechts | verwitterte Carrara-Marmorbüste im Low-Key-Licht, hartes Kantenlicht, Blick zum Text |
| Ecke unten rechts | frei lassen, dort steht die Videolänge |

## Text

- **Genau zwei bis drei Wörter**, auf zwei Zeilen verteilt.
- **Zeile 1 Weiß `#FFFFFF`**, kleiner. **Zeile 2 Türkis `#00E5FF`**, groß, trägt das Reibungswort.
- Großbuchstaben, Schrift Anton (Ersatz Bebas Neue), schwarze Kontur plus weicher Schatten.
- Textblock mindestens zwanzig Prozent der Bildhöhe.
- Keine Ziffern („VIER“ statt „4“), keine Bindestriche, keine englischen Wörter.
- Nicht gleich dem Titel. Höchstens ein Wort aus dem Titel. Der Text ergänzt den Titel und öffnet eine Frage.

Beispiele (Form): `WAS ER` / `VERSCHWEIGT` · `NIE MEHR` / `KLEIN` · `ER` / `SCHWEIGT`

## Bild

- Büste aus einem scharfen Standbild der eigenen Clips oder ein neues Bild (Prompt auf Englisch, ohne Text im Bild).
- Position, Nähe (Totale, Büste, Augen) und Hintergrund wechseln von Video zu Video. Nie zwei Thumbnails hintereinander mit gleicher Anordnung.
- Kein echtes Gesicht, keine modernen Dinge, kein Logo, kein Wasserzeichen.

Prompt-Vorlage für die Büste:
```
Weathered ancient Roman Carrara marble bust of a bearded man, three quarter view facing left,
extreme low key lighting, single hard rim light from the right, deep black background,
cracks and erosion in the marble, cinematic, photorealistic, 16:9, no text, no watermark, no logo
```

## Erzeugen mit `thumbnail_maker.py`

```powershell
python thumbnail_maker.py --zeile1 "WAS ER" --zeile2 "VERSCHWEIGT" --bild buese.png -o "V15 Was ein Mann für sich behält THUMBNAIL.jpg"
```

- `--bild` als PNG mit Transparenz: Büste wird rechts auf dunklen Marmor gesetzt.
- `--bild` als JPG ohne Transparenz (Standbild): füllt das Bild, Ausschnitt mit `--fokus 0` (links) bis `1` (rechts), Standard `0.75`.
- `--schrift` Pfad zu Anton-Regular.ttf. Ohne Angabe sucht das Skript `schriften/Anton-Regular.ttf`, sonst Bebas Neue aus dem Repo.
- Das Skript bricht ab bei weniger als zwei oder mehr als drei Wörtern, bei Ziffern und bei Bindestrichen.
- Ausgabe: JPG 1280×720 unter 2 MB plus `_vorschau_168px.png` zur Lesbarkeitsprüfung.

## Prüfung vor der Abgabe

1. Vorschau mit 168 px Breite: beide Zeilen lesbar.
2. Nur Weiß und Türkis im Text, Ecke unten rechts frei.
3. Wasserzeichen-Prüfung: alle vier Ecken und die Mitte in voller Größe ansehen.
4. Dateiname nach Regel: `VNN Themenname THUMBNAIL.jpg`.
5. Nach dem Hochladen durch Rene: vidIQ Thumbnail-Wertung (Ziel über 70) im Ordner notieren.
