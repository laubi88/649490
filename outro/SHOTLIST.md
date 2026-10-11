# Shotlist – Kanal-Outro Stoische Karriere (Entwurf, wartet auf Freigabe)

Format 1920×1080 · 30 fps · 10,0 s · eine durchgehende Einstellung, kein Schnitt

## Layout (Pixel, Ursprung oben links)

```
 0 ┌──────────────────────────────────────────────────────────────┐
   │                        ( Medaillon )                          │  Mitte x 960, y 200, Ø 260
   │                                                               │
420│                    STOISCHE KARRIERE                          │  Bebas 148 px, weiß, Grundlinie y 470
490│                    @Stoische.Karriere                         │  Bebas 56 px, türkis, Grundlinie y 535
558│                ─────────────────────────                      │  Linie 520 × 2 px, türkis
590│  ┌───────────────────┐                 ┌───────────────────┐  │
   │  │  FREI: Video A    │     ( FREI )    │  FREI: Video B    │  │  Videos: 660 × 371 px
   │  │  x 150–810        │   Abo-Kreis     │  x 1110–1770      │  │  Abo-Kreis: Mitte 960/775, Ø 200
   │  │  y 590–961        │                 │  y 590–961        │  │
961│  └───────────────────┘                 └───────────────────┘  │
1080└──────────────────────────────────────────────────────────────┘  unten 119 px frei für die Player-Leiste
```

## Zeitplan

| # | Zeit (s) | Element | Bewegung |
|---|---|---|---|
| 1 | 0,0–0,6 | Hintergrund | Schwarz → dunkler Marmor, Fade |
| 2 | 0,3–1,5 | Medaillon | Blur 20→0 px, Deckkraft 0→1, Skalierung 0,96→1,00 |
| 3 | 0,9–1,9 | Türkis-Linie | zeichnet sich von der Mitte nach außen (0→520 px) |
| 4 | 1,1–2,0 | `STOISCHE KARRIERE` | Laufweite +20 % → +4 %, Deckkraft 0→1 |
| 5 | 1,5–2,3 | `@Stoische.Karriere` | Deckkraft 0→1, y +12→0 px |
| 6 | 2,0–9,4 | Halten | Medaillon-Push-In 1,00→1,03, Türkis-Rimlight „atmet“ (35 %↔25 %, Periode 4 s), ≤ 40 Glutpartikel steigen langsam |
| 7 | 9,4–10,0 | alles | Fade auf Schwarz |

Freiflächen: Ab Sekunde 2,0 liegt in den drei FREI-Zonen nur Marmor-Hintergrund, keine Partikel.

## YouTube-Studio-Einstellung danach
- Abspann-Start = Videoende − 8 s (= Outro-Sekunde 2,0), Dauer 8 s
- Element 1: Video „Neuestes Video“ → Zone links
- Element 2: Video „Für Zuschauer am besten geeignet“ → Zone rechts
- Element 3: Abonnieren → Kreis Mitte

## Lieferumfang nach Freigabe
1. `render/outro_16x9.mp4` – das fertige Outro
2. `render/outro_16x9_positionshilfe.mp4` – gleiche Datei mit dünnen Hilfsrahmen um die Freiflächen, **nur** zum Ausrichten im YouTube Studio, nicht zum Hochladen
3. `render/vorschau/` – Standbilder bei 0,5 / 1,5 / 2,5 / 6,0 / 9,7 s plus Handy-Test (auf 640 px verkleinert)
4. HyperFrames-Projektcode, damit Texte und Farben später ohne Neugenerierung änderbar bleiben
5. Optional: `render/outro_shorts_9x16.mp4`, 4 s, nur Medaillon, Name und Handle, ohne Freiflächen (Shorts haben keinen Abspann)
