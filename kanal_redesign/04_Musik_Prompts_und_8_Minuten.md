# Musik-Prompts und 8-Minuten-Verlängerung V15 und V16

Stand: 13.10.2026. Grundlage: Renes Auftrag vom 13.10.2026. Erzeugen und Herunterladen macht Rene selbst in der Musik-App. Kein ElevenLabs.

## 1. Vier Text-to-Music-Prompts (Englisch, ohne Gesang)

Hinweise vor dem Einfügen:
- Keine Film- oder Komponistennamen in den Prompt schreiben. Viele Musikgeneratoren lehnen solche Prompts ab, und es erhöht das Risiko von Content-ID-Treffern.
- Frequenzangaben wie „2 bis 5 kHz frei lassen“ befolgen die Generatoren nicht verlässlich. Die Prompts verlangen deshalb eine dünne Mittellage ohne Melodie im Vordergrund. Die eigentliche Sprachlücke entsteht beim Mischen (Abschnitt 2).
- Jeden Prompt zwei- bis dreimal erzeugen und die beste Fassung wählen. Vor der Verwendung komplett anhören: kein Gesang, keine Stimmfetzen, kein plötzlicher Höhepunkt.

### Track 1 – Spannung und Macht (Manipulation, Grenzen, Respekt)
```
Dark cinematic thriller underscore, instrumental, no vocals. Deep sub-bass pulse on every beat at 70 BPM, subtle ticking clock-like percussion, cold analog synth drones, sparse low piano stabs. Slowly building tension that never explodes into a climax. Minor key, restrained, steady volume for background under spoken narration. Keep the midrange sparse and uncluttered, no lead melody, no strings, no choir. Seamless and loopable.
```

### Track 2 – Tiefer Fokus und Klarheit (Disziplin, Karriere, Entscheidungen)
```
Modern dark felt piano, instrumental, no vocals. Soft muted felt piano playing slow, sparse minor-key motifs in the low and middle register, warm deep analog synth pad underneath, gentle tape warmth. Calm, focused and introspective, not sad. Absolutely no strings, no violin, no cello, no drums. 65 BPM, steady dynamics, sparse midrange so a spoken voice sits clearly on top. Seamless and loopable.
```

### Track 3 – Ruhige Größe und Loslassen (Gelassenheit, Grübeln, Kritik)
```
Wide cinematic ambient soundscape, instrumental, no vocals. Slow evolving warm synth pads, deep low brass-like swells, distant soft reverb textures. A feeling of quiet grandeur and dignity, hopeful rather than sad, modal harmony leaning towards major. No foreground melody, no strings, no choir, no percussion. Very slow, steady volume, lots of space for narration. Seamless and loopable.
```

### Track 4 – Shorts-Antrieb (Spannung ab Sekunde eins)
```
Driving dark cinematic pulse for short vertical videos, instrumental, no vocals, 80 BPM. Tension from the very first second: tight sub-bass pulse in eighth notes, crisp muted percussion ticks, low synth ostinato, a subtle riser every eight bars. Confident and focused, not aggressive. No strings, no choir, no lead melody. Sparse midrange so a voice stays clear, constant energy from start to end, no intro fade. Seamless and loopable.
```

### Zuordnung (Vorschlag)
| Video | Track |
|---|---|
| V15 Was ein Mann für sich behält | Track 1 (Grenzen, Respekt) |
| V16 Kritik annehmen | Track 3 (Ruhe unter Druck) |
| Shorts | Track 4 |
| Videos zu Disziplin, Karriere, Fokus | Track 2 |

Regel „jeder Clip genau einmal“ gilt für Bilder, nicht für Musik. Trotzdem nicht alle Videos mit demselben Track unterlegen, sonst klingt der Kanal wieder gleich.

## 2. Mischen (Kanalregeln aus `stoische-karriere-vidiq-regeln`)

- Stimme minus 12 LUFS. Musik rund 22 dB unter der Stimme (zulässig 18 bis 27 dB). Seit 08.10.2026 bei Claude Code rund 29 dB, weil Rene es leiser wollte. Beim neuen, pulsierenden Material eher bei 25 bis 29 dB bleiben: Ein Sub-Bass-Puls fällt lauter auf als ein Cello.
- Sprachlücke: Musik bei 2 bis 5 kHz um 3 bis 4 dB absenken (breites Glockenfilter um 3 kHz). Beispiel ffmpeg: `equalizer=f=3000:t=q:w=0.8:g=-4`.
- Musik über die volle Länge, weich ein- und ausblenden. Kein Knacken an den Schnittstellen der Schleife.

## 3. V15 und V16 auf mindestens 8:03

### Fakten
- YouTube: Mid-Roll-Werbung lässt sich bei **monetarisierten** Videos ab **8 Minuten** einschalten (YouTube Creator-Seite „Ads and Premium“). Vorher lag die Grenze bei 10 Minuten.
- Monetarisiert heißt: Mitglied im YouTube-Partnerprogramm mit Werbeeinnahmen. Laut übereinstimmenden Berichten braucht das 1.000 Abonnenten und 4.000 öffentliche Wiedergabestunden in zwölf Monaten (oder 10 Millionen Shorts-Aufrufe in 90 Tagen). Stand 05.10.2026 hatte der Kanal 16 Abonnenten.
- Folge: Heute bringt die 8-Minuten-Marke kein Geld. Sie lohnt sich trotzdem, weil Mid-Rolls später auch bei älteren Videos eingeschaltet werden können, sobald der Kanal im Programm ist.

### Rechnung
Reihenfolge der zehn Tonspuren: Block1, Block2, Block3, CTA1, Block4, Block5, CTA2, Block6, Block7, Outro. Das sind **neun Übergänge**.

| Video | Länge jetzt | 9 × 1,0 s Pause | danach | fehlt bis 8:03 | Lösung |
|---|---|---|---|---|---|
| V15 | 7:55 | + 9 s | 8:04 | – | fertig |
| V16 | 7:52 | + 9 s | 8:01 | 2 s | Endcard um 3 s verlängern → 8:04 |

Bei 0,8 s je Übergang reicht es bei keinem Video. Deshalb 1,0 s.
Unbekannt ist, ob 7:55 und 7:52 schon Logo und Endcard enthalten. Maßgeblich ist die Dauer der fertigen Datei laut `ffprobe`, Ziel mindestens 483 Sekunden.
Endcard verlängern ist erlaubt: Der YouTube-Abspann darf 5 bis 20 Sekunden lang sein, die Endcard hat bisher 10 Sekunden.

### Achtung beim Umsetzen
1. **Regelkonflikt:** Videovorlage Abschnitt 6.3 sagt „keine künstlichen Pausen“. Die Pausen zwischen den Blöcken sind eine Ausnahme nach Renes Auftrag vom 13.10.2026. Innerhalb der Blöcke bleibt alles, wie es ist. Die Fragepausen von 1,0 s bleiben zusätzlich.
2. **Clip-Anker neu berechnen:** Jeder Block beginnt eine Sekunde später als zuvor, am Ende fast neun Sekunden später. Laut Videovorlage Abschnitt 7 erst die Pausen einsetzen, dann die Clip-Anker berechnen. Kein Clip darf in einer Pause stehen bleiben. Zu kurze Clips langsamer laufen lassen (Tempo bis 0,68), nie einfrieren.
3. **CTA-Prozente prüfen:** Nach der Verlängerung CTA1 (Soll 30 bis 40 %) und CTA2 (bei V16 65 %, Renes Entscheidung) neu ausrechnen und ins Prüfprotokoll schreiben.
4. **Pausen nicht hörbar leer:** Die Musik läuft in den Pausen weiter. Keine Stille, sonst entsteht ein Loch im Ton (Prüfung „Stille über 1,2 s“ aus Videovorlage Abschnitt 7).
5. Ausgabe wie immer: 1920×1080, 30 fps, H.264 9 Mbit/s, Schlüsselbild alle 60 Bilder, AAC 160 kbit/s. Danach komplett auf Wasserzeichen und Ruckler prüfen.
6. Kapitelzeiten im YouTube-Paket erst nach diesem Render eintragen.

Quellen:
- https://www.youtube.com/creators/earn/ads-and-premium/
- https://vidiq.com/blog/post/youtube-8-minute-mid-roll-ads
- https://www.premiumbeat.com/blog/youtube-mid-roll-ad-change/
