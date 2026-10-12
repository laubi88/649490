---
name: flow-und-cta
description: Prompt-Format für die themenspezifischen Zusatzclips 46 bis 50 in Flow und Schnittplan mit CTA 1, CTA 2 und OUTRO für Stoische Karriere.
---

# 04 Flow-Prompts und Schnittplan

Stand 12.10.2026. Ergänzt die Konto-Skills `stoische-karriere-videovorlage` (Abschnitt 4 Werbeclips, 5 Bildplan, 7 Schnitt) und CLAUDE.md A3. Zeitpunkte aus `03_retention_skript.md`.

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

Block1 → Block2 → Block3 → Block4 → Block5 → **CTA1** → Block6 → Block7 → **CTA2** → **Outro** → Endcard

CTA1 liegt bei rund siebzig Prozent, CTA2 bei 8:00, Outro ab 8:10 (CLAUDE.md A5). Die genaue Lage von CTA1 hängt von den gemessenen Blocklängen ab. Wenn CTA1 nach Werkzeug drei bei rund siebzig Prozent fällt, steht er dort. Fällt er mitten in ein Werkzeug, Rene vor dem Schnitt fragen.

### Tabelle

| Nr | Zeit von | Zeit bis | Tonspur | Bild | Clip-Nr | Anker (Satz, bei dem gewechselt wird) |
|---|---|---|---|---|---|---|
| 1 | 0:00 | … | Block1 | Themenclip | 46 | erster Satz |
| … | | | | | | |
| CTA1 | … | … | CTA1 | Themenclip, ab „Wenn dich dieser Teil“ Einblender CTA1 (neu: A3a), ab „Und jetzt zurück“ Themenclip | … | „Wenn dich dieser Teil weitergebracht hat …“ |
| CTA2 | 8:00 | 8:10 | CTA2 | Themenclip, bei Daumen oder Glocke Einblender CTA2 (neu: A3b) | … | Kommentarfrage |
| OUTRO | 8:10 | … | Outro | Themenclip, ab „Lass einen Daumen hoch da.“ Outro-Werbung (neu: A3c), bei „Stoische. Karriere.“ Logo (neu: A2), danach Endcard | – | „Lass einen Daumen hoch da.“ |
| END | … | +10 s | Musik oder Stille | Endcard (neu: A1), mindestens fünf Sekunden für YouTube-Endcards | – | – |

Die Spalte Clip-Nr nennt jeden Clip genau einmal. Clips 1 bis 45 und 46 bis 50 gemischt nach Inhalt, die stärksten Clips an die stärksten Stellen (Block 1 Anfang, Denker in Block 2, Beispiel in Werkzeug eins, Anfang Werkzeug vier).

Solange das neue Outro-Set (A1 bis A3c, CLAUDE.md Teil B) nicht fertig ist, gelten die Alt-Clips `CTA1.mp4`, `cta2.mp4`, `finale werbung.mp4`, `CTA_3_1080p_20261001034923.mp4` und `outro.mp4`.

### Schnittregeln

- Weiche Blende 0,8 s zwischen allen Clips. Ist ein Clip zu kurz, läuft er langsamer (Tempo bis 0,68), er bleibt nie stehen.
- Nach jeder Frage im Sprechertext insgesamt 1,0 s Pause (Eintrag in `16_Fragepausen_Schnitt`).
- Zuerst zwanzig Sekunden Test rendern und prüfen, dann das ganze Video.
- Ausgabe 1920×1080, 30 fps, H.264 9 Mbit/s, Schlüsselbild alle 60 Bilder, AAC 160 kbit/s.
- Prüfprotokoll Wasserzeichen und Qualität in `17_Pruefprotokoll_Wasserzeichen_Qualitaet`.
