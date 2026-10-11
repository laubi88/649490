# Style Guide – Kanal-Outro Stoische Karriere (Entwurf, wartet auf Freigabe)

Stand: 11.10.2026

## 1. Ist-Zustand: die 5 vorhandenen Clips

| Datei | Länge | Motiv | Schrift | Farbe | Ton (mean / max) |
|---|---|---|---|---|---|
| CTA1.mp4 | 8 s | Bronzemedaille, Statue mit Buch und Fackel, brennender Daumen und Glocke | Serif, Gold | Gold/Feuer | −30,9 / 0,0 dB |
| cta2.mp4 | 10 s | Steinsockel, Medaillon Athena mit Helm, Daumen und Glocke in Flammen | Serif, glühend orange | Orange/Feuer | −19,4 / −1,8 dB |
| finale_werbung.mp4 | 10 s | Steintor mit Runen, dann Berge im Sonnenuntergang | Serif, Gold | Warm/Rosa | −18,0 / 0,0 dB |
| outro.mp4 | 10 s | Steintor mit Runen und Feuerschalen, dann Berge in der Dämmerung | **Sans** (Bebas-ähnlich), Glühen | Blau/Gold | −16,2 / −1,3 dB |
| CTA_3_1080p.mp4 | 10 s | Bronzemedaille, Frau mit Fackel, Sanduhr | Serif, in Stein gemeißelt | Bronze | −34,1 / −2,4 dB |

Alle Clips: 1920×1080, **24 fps**, H.264 + AAC 48 kHz Stereo. Referenzbild: `referenz/ist_zustand_schlussbilder.jpg`.

**Befund:** Es gibt keine Einheitlichkeit. Drei verschiedene Medaillon-Figuren werden als „Logo“ benutzt, dazu zwei Schriftfamilien, drei Farbwelten und ein Ton-Pegelunterschied von etwa 18 dB. Englisch („SUBSCRIBE“) und Deutsch („ABONNIERE“) sind gemischt. Keiner der Clips lässt Platz für YouTube-Abspann-Elemente. Der Kanalname und die CTA-Buttons sind fest ins Bild gerendert. Ändern geht also nur durch neues Generieren.

Kein Clip nutzt den Kanalstil aus dem Skill (Weiß + Türkis, BebasNeue).

## 2. Ziel

Ein **einziges** Outro als Code (HyperFrames), das an jedes Langvideo angehängt wird. Texte, Farben und Zeiten bleiben änderbar, ohne neu zu generieren. Optional gibt es eine 9:16-Variante für Shorts.

## 3. Feste Vorgaben

### Format
- 1920×1080, **30 fps**, H.264 **9 Mbit/s**, Schlüsselbild alle 60 Bilder, AAC 160 kbit/s (Qualitätsregel Skill stoische-karriere-videovorlage, Abschnitt 7)
- Länge **10,0 s**
- Tonspur: AAC 48 kHz Stereo, **still**. CLAUDE.md sagt Clip-Ton 0, Musik kommt im Schnitt dazu. Die stille Spur sorgt dafür, dass sich das Outro in CapCut ohne Spurprobleme ans Video hängen lässt.
- 30 fps ist durch die Qualitätsregel bestätigt. Die 24-fps-Altclips werden beim Schnitt ohnehin auf 30 fps umgerechnet.

### Farben
| Token | Wert | Verwendung |
|---|---|---|
| `--bg` | `#0B0D0E` | Grundfläche, fast Schwarz |
| `--marmor` | dunkler Marmor-Verlauf `#15191B` → `#0B0D0E`, feine Äderung bei 6 % Deckkraft | Hintergrund |
| `--weiss` | `#F2F2EE` | Kanalname, Haupttext |
| `--tuerkis` | `#00E5FF` | Akzent: Handle, Linie, Glocke, Fokuspunkt |
| `--tuerkis-glow` | `#00E5FF` bei 35 %, Blur 18 px | nur weiches Leuchten, kein Neon |

Keine knalligen Farben, kein Feuer-Orange. **Konflikt:** Deine 5 Clips sind komplett Gold/Feuer. Der Skill schreibt Weiß + Türkis vor. Ich setze den Skill um. Falls Gold gewollt ist, muss der Skill geändert werden, nicht das Outro.

### Schrift
- **Bebas Neue** (SIL Open Font License 1.1, kommerziell frei), Datei aus `google/fonts` auf GitHub, liegt in `projekt/assets/fonts/`. Rene hat dem Download am 11.10.2026 nachträglich zugestimmt.
- Kanalname `STOISCHE KARRIERE`: 148 px, Laufweite +4 %, `--weiss`
- Handle `@Stoische.Karriere`: 56 px, Laufweite +6 %, `--tuerkis`. Das Handle bleibt in Groß-/Kleinschreibung wie auf YouTube, weil es ein Name und kein Titel ist.
- CTA-Zeile **optional, Standard: weg**. Der klickbare Abonnieren-Kreis von YouTube ist der CTA. Zusätzlicher Text daneben ist doppelt und frisst die Freifläche.
- Mindestgröße für den Handytest: Bei 1920 px Breite ist kein Text kleiner als 40 px. Auf einem 6"-Display im Querformat ergibt das etwa 2,2 mm Versalhöhe.

### Logo / Medaillon
- Quelle: Schlussbild von `CTA_3_1080p` (Frau mit Fackel und Lorbeerkranz). Dieses Bild hat **keinen eingebrannten Text**, ist frontal und gut freistellbar. Datei: `referenz/medaillon_quelle_cta3.png`
- Kreisförmig freigestellt, Bronze bleibt Bronze, dazu ein leichter Türkis-Rimlight-Ring (2 px, 60 %)
- **Offene Frage:** Welches Medaillon ist dein echtes Kanal-Logo (Profilbild)? Falls es ein anderes ist, schick mir die Datei. Ich nehme kein KI-Standbild als Logo, wenn es ein offizielles gibt.

### Bewegung
- Ruhig: Ease `cubic-bezier(0.22, 1, 0.36, 1)` (easeOutQuint), keine Bounces, kein Wackeln
- Einblendungen 0,6–1,0 s, keine schneller als 0,4 s
- Höchstens **3 Effektarten**: Fade/Blur-Reveal, langsamer Push-In (Skalierung ≤ 4 %), wenige Glutpartikel (≤ 40, Deckkraft ≤ 30 %)
- Keine Glitches, kein Kamerazittern, kein Lens Flare

## 4. YouTube-Abspann (Endscreen) – technische Grenzen

Quelle: YouTube-Hilfe, Artikel 6388789
- Der Abspann liegt in den **letzten 5–20 s** des Videos. Das Video muss **mindestens 25 s** lang sein.
- Bei 16:9 sind **bis zu 4 Elemente** möglich (Video/Playlist, Abonnieren, Kanal, Link).
- Nicht verfügbar bei „Made for Kids“ und **nicht bei Shorts**. Die 9:16-Variante ist deshalb reine Grafik ohne klickbare Elemente.

Folgerung: Das Outro hält ab Sekunde 2 **feste Freiflächen** für 2 Videokarten und den Abonnieren-Kreis frei. Dort sitzt keine Grafik, die von den Elementen verdeckt würde.

## 5. Recht
- Nur eigene Inhalte: dein Kanalname, dein Medaillon, Bebas Neue (OFL)
- Kein YouTube-Logo und kein nachgebauter YouTube-Abonnieren-Button. Der echte Button kommt über den Endscreen von YouTube.
