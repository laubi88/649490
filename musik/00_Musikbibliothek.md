# Musikbibliothek Stoische Karriere

Stand: 13.10.2026. Ziel (Rene): einen Vorrat an filmischer Hintergrundmusik anlegen, damit nicht für jedes Video neu erzeugt werden muss.
Alle Tracks ohne Gesang. Prompts für weitere Tracks: `kanal_redesign/04_Musik_Prompts_und_8_Minuten.md`.

## Bestand

| Datei | Stimmung | Für | Länge | Quelle |
|---|---|---|---|---|
| `M01_Spannung_und_Macht.mp3` | dunkler, kühler Film-Puls, ruhiger Mittelteil | V15, Manipulation, Grenzen, Respekt | 2:56 | vidIQ, 13.10.2026 |
| `M02_Kuehler_Abstand.mp3` | Glocken und Flächen, danach dichter | V16, Gelassenheit | 2:56 | vidIQ, 13.10.2026 |
| `M03_Shorts_Puls.mp3` | treibender tiefer Puls, Riser | Shorts | 2:52 | vidIQ, 13.10.2026 |

Format: MP3, 44,1 kHz, Stereo, 192 kbit/s. vidIQ liefert die Dateien mit der Endung `.wav`, sie sind aber MP3. Hier ohne Neukodierung als `.mp3` gespeichert, Metadaten entfernt.
Lizenz laut vidIQ: „original, royalty-free background-music track“. Erzeugt mit Renes vidIQ-Konto. Vor dem ersten Upload einmal in den vidIQ-Bedingungen nachlesen, ob die kommerzielle Nutzung auf YouTube ausdrücklich erlaubt ist.

## Prüfung (ffmpeg, 13.10.2026)

| Datei | Lautheit | True Peak | Stille über 1,2 s | Sprachbereich 2 bis 5 kHz |
|---|---|---|---|---|
| M01 | −13,4 LUFS | +0,9 dBTP | keine | rund 19 dB unter den Tiefen |
| M02 | −12,2 LUFS | +1,4 dBTP | keine | rund 12 dB unter den Tiefen |
| M03 | −14,4 LUFS | +0,6 dBTP | keine | rund 17 dB unter den Tiefen |

- True Peak über 0 dB: leichte Übersteuerung in der Quelldatei. Unter der Stimme (Musik 22 bis 29 dB leiser) unhörbar. Für Teile ohne Sprache vorher auf −1 dBTP absenken.
- Gesang lässt sich im Spektrum nicht sicher ausschließen. Jeden Track einmal ganz anhören.
- M02 ist unruhiger als bestellt: Das Spektrum (`M02_spektrum.png`) zeigt nach etwa 30 Sekunden einen dichten, breitbandigen Teil. Anhören. Passt er nicht, für V16 lieber M01 nehmen oder Track 8 bzw. 3 aus den Prompts in Google erzeugen.
- Alle drei enden mit einer Ausblendung. Für acht Minuten drei Durchläufe mit 3 Sekunden Überblendung aneinanderhängen (ffmpeg `acrossfade=d=3`).

## Ablage und Benennung neuer Tracks

- Dateiname: `MNN_Stimmung.mp3`, fortlaufend nummeriert.
- In die Tabelle oben eintragen: Stimmung, Zweck, Länge, Quelle mit Datum.
- Pro Video notieren, welcher Track lief (im Schnittplan des Videos). Zwei Videos hintereinander nicht mit demselben Track.

## vidIQ-Credits

Ein Track kostet 25 Credits. Nach diesen drei Tracks bleiben 52 Credits bis zur Auffüllung am 02.11.2026. Weitere Tracks deshalb vorerst in Google erzeugen und hier ablegen.
