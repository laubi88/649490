---
name: thumbnail-agent
description: Thumbnails für Stoische Karriere planen und mit thumbnail_maker.py erzeugen. 1920x1080 unter 2 MB, zwei bis vier Wörter, Zeile 1 Türkis #00E5FF, Zeile 2 Weiß, Schrift Anton, Schattenverlauf links, Carrara-Marmorbüste rechts. Anwenden bei jedem Thumbnail und beim Thumbnail-Plan im YouTube-Paket.
---

# Thumbnail Agent

Stand 12.10.2026. Deckt sich mit dem Konto-Skill `stoische-karriere-vidiq-regeln` (Abschnitt Thumbnail) und mit CLAUDE.md M1 und M5.

## Technik

- 1920×1080 (16:9), JPG, **unter 2 MB** (vom Handy hochladbar). YouTube erlaubt mobil 2 MB, am Desktop 50 MB.
- Erzeugt mit `thumbnail_maker.py` im Hauptverzeichnis.

## Aufbau

| Bereich | Inhalt |
|---|---|
| Links, rund 60 Prozent | dunkler Schattenverlauf, am Rand fast schwarz, weich auslaufend. Darauf der Text, linksbündig |
| Rechts | verwitterte Carrara-Marmorbüste im Low-Key-Licht, hartes Kantenlicht, Blick zum Text |
| Ecke unten rechts | frei lassen, dort steht die Videolänge |

## Text

- **Zwei bis vier Wörter** auf zwei Zeilen.
- **Zeile 1 Türkis `#00E5FF`**, kleiner. **Zeile 2 Weiß `#FFFFFF`**, groß, trägt das Reibungswort.
- Schrift **Anton** (`schriften/Anton-Regular.ttf`), Großbuchstaben, schwarze Kontur plus weicher Schatten.
- Textblock mindestens zwanzig Prozent der Bildhöhe. Vier lange Wörter machen die Schrift klein. Deshalb lieber zwei oder drei kurze.
- Keine Ziffern („VIER“ statt „4“), keine Bindestriche, keine englischen Wörter.
- Nicht gleich dem Titel. Höchstens ein Wort aus dem Titel. Der Text ergänzt den Titel und öffnet eine Frage.

Beispiele (Form): `WAS ER` / `VERSCHWEIGT` · `NIE MEHR` / `KLEIN` · `DEIN CHEF` / `TESTET DICH`

## Bild

- Büste aus einem scharfen Standbild der eigenen Clips oder ein neues Bild (Prompt auf Englisch, ohne Text im Bild).
- Position, Nähe (Totale, Büste, Augen) und Hintergrund wechseln von Video zu Video. Nie zwei Thumbnails hintereinander mit gleicher Anordnung.
- Karriere-Bezug, wo es passt (Marmor-Schreibtisch mit Öllampe, Torbogen, zwei Figuren gegenüber).
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

- `--bild` als PNG mit Transparenz: Die Büste wird rechts auf dunklen Marmor gesetzt.
- `--bild` als JPG ohne Transparenz (Standbild): Das Bild füllt die Fläche. Ausschnitt mit `--fokus 0` (links) bis `1` (rechts), Standard `0.75`.
- Schrift: Standard ist `schriften/Anton-Regular.ttf`. Fehlt die Datei, nimmt das Skript Bebas Neue und meldet das.
- Das Skript bricht ab bei weniger als zwei oder mehr als vier Wörtern, bei Ziffern und bei Bindestrichen. Englische Wörter erkennt es nicht.
- Ausgabe: JPG 1920×1080 unter 2 MB plus `_vorschau_168px.png` für die Lesbarkeitsprüfung.

## Shorts-Cover (Hochformat 1080×1920)

Gleiche Schrift, gleiche Farben, gleiche Wortregeln. Unterschied: Der Text darf **nie über Kopf oder Gesicht der Figur** liegen. Dafür hat das Skript drei Textlagen:

```powershell
python thumbnail_maker.py --format short --textlage rechts --zeile1 "FÜNFZEHN MINUTEN" --zeile2 "STILLE" --bild standbild.jpg -o "Short Stille COVER.jpg"
```

| `--textlage` | Lage | Für Bilder, bei denen |
|---|---|---|
| `oben` | mittig im oberen Viertel, volle Breite, Zeile 2 bis 300 px | die Figur unten oder in der unteren Hälfte steht |
| `rechts` | rechtsbündig im oberen Drittel, höchstens 58 Prozent der Breite | die Figur links steht (Kopf im linken Drittel) |
| `unten` | mittig bei rund 60 Prozent der Höhe | die Figur oben steht. Tiefer nicht: ab rund 70 Prozent liegen Titel und Bedienelemente der Shorts-Ansicht |

- Hinter dem Text legt das Skript ein weiches dunkles Band, damit Weiß und Türkis auch über hellem Marmor lesbar bleiben.
- `--bild` als PNG mit Transparenz: Büste unten links, 72 Prozent der Höhe. Als JPG: füllt die Fläche, Ausschnitt per `--fokus`.
- Das Standbild **ohne eingebrannten Text** verwenden. Ein Cover mit altem Text lässt sich nicht sauber umbauen, Wegretuschieren nur mit Renes Ja.
- Bei `rechts` wird Zeile 1 klein (rund 80 px bei zwei langen Wörtern). Lieber ein kurzes Wort in Zeile 1 oder das Bild so planen, dass die Figur unten steht und `oben` geht.
- Ausgabe: JPG 1080×1920 unter 2 MB plus `_vorschau_168px.png` (168×299, Größe im Shorts-Raster).

## Prüfung vor der Abgabe

1. Vorschau mit 168 px Breite: Beide Zeilen sind lesbar.
2. Nur Türkis und Weiß im Text, Ecke unten rechts frei.
3. Wasserzeichen-Prüfung: alle vier Ecken und die Mitte in voller Größe ansehen.
4. Dateiname nach Regel: `VNN Themenname THUMBNAIL.jpg`.
5. Nach dem Hochladen durch Rene: vidIQ-Thumbnail-Wertung (Ziel über 70) im Ordner notieren.
