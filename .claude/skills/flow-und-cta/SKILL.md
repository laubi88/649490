---
name: flow-und-cta
description: Prompt-Format für die themenspezifischen Zusatzclips 46 bis 50 in Flow und Schnittplan mit CTA 1, CTA 2 und OUTRO für Stoische Karriere. Anwenden bei 05_Flow_Prompts_Zusatzclips_EN und 15_Schnittplan.
---

# Flow-Prompts und Schnittplan

Stand 12.10.2026. Deckt sich mit dem Konto-Skill `stoische-karriere-videovorlage` (Abschnitt 3 CTA-Positionen, 4 Werbeclips, 5 Bildplan, 7 Schnitt) und CLAUDE.md M3 und M4. Zeitpunkte aus dem Skill `retention-skript`.

## Teil 1: Zusatzclips 46 bis 50

Clips 1 bis 45 sind Standard-Marmorclips. Clips 46 bis 50 entstehen je Video neu und zeigen das Thema des Videos. Ablage: `05_Flow_Prompts_Zusatzclips_EN` im Videoordner.

### Prompt-Format (je Clip ein Block, Prompt auf Englisch)

```
CLIP 46
Einsatz: Block 3, ab dem Satz „Beim Chef klingt das so.“
Länge: 8 s, 16:9, 1080p, keine Tonspur nötig
Inhalt (Deutsch, eine Zeile): Marmorstatue eines Mannes sitzt allein am Kopfende eines Steintischs.

PROMPT:
[Subject] Weathered ancient Roman Carrara marble statue of a man in a toga, seated alone at the head of a long stone table,
[Action] slowly lifting his head and looking straight ahead, subtle and calm movement,
[Setting] dark Roman hall with columns fading into black,
[Light] extreme low key lighting, single hard cool rim light from the left, deep shadows, faint turquoise reflection,
[Camera] slow dolly in, eye level, shallow depth of field,
[Style] photorealistic, cinematic, 24 mm, film grain subtle,
[Exclude] no text, no letters, no logo, no watermark, no modern objects, no real human face, no color other than marble white, black and a hint of turquoise

PRÜFUNG: Wasserzeichen (Ecken und Mitte, je Sekunde), Hände und Gesicht, Flackern, Sprünge
```

Regeln:
- Alle fünf Prompts folgen den Feldern Subject, Action, Setting, Light, Camera, Style, Exclude.
- Licht immer Low-Key mit hartem Kantenlicht, Material immer verwitterter Carrara-Marmor.
- Eine ruhige, langsame Bewegung je Clip. Keine schnellen Schnitte im Clip, kein Text im Bild.
- Jeder Zusatzclip passt zu genau einer Stelle im Sprechertext und steht im Schnittplan an dieser Stelle.
- Clip mit Wasserzeichen oder Bildfehler wird neu erzeugt, nicht retuschiert und nicht wiederholt.

## Teil 2: Schnittplan (`15_Schnittplan`)

### Reihenfolge der Tonspuren

Block1 → Block2 → Block3 → **CTA1** → Block4 → Block5 → **CTA2** → Block6 → Block7 → **Outro** → Logo → Endcard

- Bis 2:00 kein CTA und kein CTA-Einblender.
- CTA1 direkt nach Werkzeug eins (Block 3), Soll 30 bis 40 Prozent der Laufzeit.
- CTA2 direkt nach Werkzeug drei (Block 5), Soll rund 70 Prozent.
- Outro am Ende, die letzten rund zwanzig Sekunden Sprechertext. Das Logo startet bei „Stoische.“, danach folgt die Endcard.

Nach dem Schnitt die echten Prozentwerte aus den gemessenen Startzeiten ausrechnen und im Prüfprotokoll notieren. Liegt ein CTA außerhalb des Sollbereichs, Rene vor dem Endrender fragen, statt Blöcke eigenmächtig umzustellen.

### Tabelle

| Nr | Zeit von | Zeit bis | Tonspur | Bild | Clip-Nr | Anker (Satz, bei dem gewechselt wird) |
|---|---|---|---|---|---|---|
| 1 | 0:00 | … | Block1 | Themenclip | 46 | erster Satz |
| … | | | | | | |
| CTA1 | … (30 bis 40 %, nicht vor 2:00) | +rund 20 s | CTA1 | Themenclip, ab „Wenn dich dieser Teil“ Einblender CTA1 (neu: A3a), ab „Und jetzt zurück“ Themenclip | … | „Wenn dich dieser Teil weitergebracht hat …“ |
| CTA2 | … (rund 70 %) | +rund 20 s | CTA2 | Themenclip, ab „Lass einen Daumen hoch da.“ Einblender CTA2 (neu: A3b) | … | „Lass einen Daumen hoch da.“ |
| OUTRO | … (letzte rund 20 s Sprechertext) | Ende Outro | Outro | Themenclip, ab „Lass einen Daumen hoch da.“ Outro-Werbung (neu: A3c), bei „Stoische. Karriere.“ Logo (neu: A2), danach Endcard | – | „Lass einen Daumen hoch da.“ |
| LOGO | bei „Stoische.“ im Outro | +4 s | Ende der Outro-Tonspur (gesprochen „Stoische. Karriere.“) | Logo-Sting (neu: A2) | – | „Stoische.“ |
| END | nach dem Logo | +10 s | Musik oder Stille | Endcard (neu: A1). YouTube-Abspann in den letzten 5 bis 20 s | – | – |

Die Spalte Clip-Nr nennt jeden Clip genau einmal. Clips 1 bis 45 und 46 bis 50 gemischt nach Inhalt, die stärksten Clips an die stärksten Stellen (Block 1 Anfang, Denker in Block 2, Beispiel in Werkzeug eins, Anfang Werkzeug vier).

Solange das neue Outro-Set (A1 bis A3c, CLAUDE.md Teil B) nicht fertig ist, gelten die Alt-Clips `CTA1.mp4`, `cta2.mp4`, `finale werbung.mp4`, `CTA_3_1080p_20261001034923.mp4` und `outro.mp4`.

### Schnittregeln

- Weiche Blende 0,8 s zwischen allen Clips. Ist ein Clip zu kurz, läuft er langsamer (Tempo bis 0,68), er bleibt nie stehen.
- Nach jeder Frage im Sprechertext insgesamt 1,0 s Pause (Eintrag in `16_Fragepausen_Schnitt`).
- Zuerst zwanzig Sekunden Test rendern und prüfen, dann das ganze Video.
- Ausgabe 1920×1080, 30 fps, H.264 9 Mbit/s, Schlüsselbild alle 60 Bilder, AAC 160 kbit/s.
- Prüfprotokoll Wasserzeichen und Qualität in `17_Pruefprotokoll_Wasserzeichen_Qualitaet`.
