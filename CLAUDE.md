# CLAUDE.md – Übergabe: Kanal-Outro und Beitrags-Clips für Stoische Karriere

Stand: 11.10.2026. Erstellt in einer Claude-Code-Cloud-Sitzung. Umsetzung auf Renes Windows-PC mit Claude Code.
Repo: `laubi88/649490`, Branch `claude/skill-geladen-opus-motion-3urqdf`.

## 0. Vor dem Start lesen (verbindlich)

Diese Skills gelten vollständig, diese Datei fasst sie nur zusammen:
- `opus-motion-design-hyperframes` (Ablauf: Style Guide und Shotlist, dann **auf Renes Okay warten**, dann rendern)
- `stoische-karriere-videovorlage` (Abschnitt 4 Werbeclips, Abschnitt 7 Qualität und Wasserzeichen)
- `stoische-karriere-vidiq-regeln` (Shorts-Ende, Farben, verbotene Werkzeuge)
- `stoische-karriere-untertitel-stil` (Türkis `#00E5FF`, Bebas Neue)

Harte Regeln, die hier besonders zählen:
- Farben nur Weiß `#FFFFFF` und Türkis `#00E5FF` auf dunklem Marmor oder Schwarz. Kein Gold, kein Feuer-Orange, kein Rot.
- Schrift: Bebas Neue (Datei liegt bei, Rene hat am 11.10.2026 Ja gesagt). Anton ist laut Untertitel-Skill die Thumbnail-/Overlay-Schrift. Wechsel nur, wenn Rene es sagt.
- Qualität: 1920×1080 bzw. 1080×1920, **30 fps**, H.264 **9 Mbit/s**, Schlüsselbild alle 60 Bilder, AAC 160 kbit/s.
- Kein Wasserzeichen in irgendeinem Bild. Keine Ruckler, keine Schwarzbilder, keine Artefakte.
- Verboten: ElevenLabs, DaVinci Resolve. Nichts hochladen, nichts löschen, keine Kanaleinstellungen ändern ohne Renes Ja.
- Keine Fakten oder Zitate erfinden. Jedes Zitat mit Werk und Stelle (siehe Abschnitt 4).
- Kein YouTube-Logo, kein nachgebauter YouTube-Abo-Button. Eigene, schlichte Symbole (Daumen, Glocke) sind erlaubt.

## 1. Einrichtung (einmalig)

```powershell
node -v          # muss 22 oder höher sein
ffmpeg -version  # muss vorhanden sein
cd outro\projekt
npx hyperframes@0.8.149 telemetry disable
npx hyperframes@0.8.149 doctor
```

HyperFrames ist auf 0.8.149 gepinnt, damit gleiche Eingabe gleiches Video ergibt. GSAP liegt lokal unter `outro/projekt/assets/vendor/gsap.min.js` (3.14.2, „Standard no-charge license“). Nicht per CDN laden: Lokal bleibt das Ergebnis reproduzierbar.
Die HyperFrames-Regeln (Timeline-Registrierung, `data-start`, `class="clip"`, kein `Math.random()`) stehen in `outro/projekt/CLAUDE.md`. Nach jeder Änderung `npx hyperframes@0.8.149 check`.

## 2. Vorhandenes Material

| Datei | Inhalt |
|---|---|
| `outro/STYLE_GUIDE.md` | Bestandsaufnahme der 5 Alt-Clips, Farben, Schrift, Bewegung, Abspann-Regeln |
| `outro/SHOTLIST.md` | Layout und Zeitplan der 16:9-Endcard (10 s) mit Freiflächen |
| `outro/referenz/ist_zustand_schlussbilder.jpg` | Schlussbilder der 5 Alt-Clips |
| `outro/referenz/medaillon_quelle_cta3.png` | Schlussbild aus `CTA_3_1080p_20261001034923.mp4`, Quelle des Medaillons |
| `outro/projekt/assets/img/medaillon_tuerkis.png` | Medaillon freigestellt, 720×720, eingefärbt Schwarz → `#003E46` → `#00E5FF` → Weiß (Rene: „türkis Medaillon“) |
| `outro/projekt/assets/img/medaillon_bronze.png` | dasselbe ungefärbt, nur als Rückfall |
| `outro/projekt/assets/img/marmor_16x9.jpg`, `marmor_9x16.jpg` | dunkler Marmor, prozedural erzeugt (eigenes Material, kein Stockbild) |
| `outro/projekt/assets/fonts/BebasNeue-Regular.ttf` + `OFL.txt` | Schrift mit Lizenz |
| `outro/werkzeuge/medaillon.py`, `marmor.py` | Skripte, mit denen die Bilder erzeugt wurden |

Die 5 Alt-Clips liegen bei Rene unter `Desktop\CTA 1 ,2,outro`. Sie sind **nicht** im Repo.

## 3. Auftrag A: einheitliches Kanal-Outro

### Befund
Die 5 Clips sind keine fünf Varianten desselben Outros. Laut Videovorlage, Abschnitt 4, hat jeder eine eigene Rolle:

| Rolle | Alt-Clip | Neu (Vorschlag) |
|---|---|---|
| CTA1-Einblender (Daumen, Glocke, Abo) | `CTA1.mp4` (8 s) | A3a, 8 s |
| CTA2-Einblender | `cta2.mp4` (10 s) | A3b, 8 s |
| Outro-Werbung | `finale werbung.mp4` (10 s) | A3c, 8 s |
| Logo bei „Stoische. Karriere.“ | `CTA_3_1080p….mp4` (10 s) | A2, 4 s, 16:9 **und** 9:16 |
| Endcard | `outro.mp4` (10 s) | A1, 10 s, laut `SHOTLIST.md` |

Die Regel „jeder Clip genau einmal pro Video“ gilt weiter. Deshalb bekommen A3a, A3b und A3c denselben Stil, aber unterschiedliche Bewegung oder Anordnung.

**Entschieden (Rene, 11.10.2026): das ganze Set** (A1, A2, A3a–c).

**Logo (Rene, 11.10.2026):** Die Frau mit Fackel ist eine fiktive Figur, kein offizielles Logo. Eine Logodatei gibt es nicht. Damit das Set einheitlich ist, wird in **allen** Teilen dasselbe Medaillon `medaillon_tuerkis.png` als Markenzeichen genutzt. Keine anderen Figuren (Athena, Statue mit Buch) mehr.

### A1 Endcard
Vorgaben vollständig in `outro/STYLE_GUIDE.md` und `outro/SHOTLIST.md`. Kurz:
- 10 s, Medaillon oben (Ø 260 px), `STOISCHE KARRIERE` weiß, `@Stoische.Karriere` türkis
- Ab Sekunde 2 Freiflächen für zwei Videokarten (x 150–810 und 1110–1770, y 590–961) und den Abo-Kreis (Mitte 960/775, Ø 200)
- Tonspur still (Musik kommt im Schnitt dazu)
- Zusätzlich eine Version mit Hilfsrahmen um die Freiflächen, nur zum Ausrichten im YouTube Studio
- YouTube-Regeln (YouTube-Hilfe 6388789): Abspann in den letzten 5–20 s, Video mindestens 25 s lang, bei 16:9 bis zu 4 Elemente, bei Shorts kein Abspann

### A2 Logo-Sting (ersetzt CTA_3)
- 4 s. Medaillon blendet ein (Blur → scharf), darunter `STOISCHE KARRIERE`
- 16:9 für das Longform-Outro, 9:16 für das Ende jedes Shorts. Die vidIQ-Regel verlangt dort: Name nicht abgeschnitten, darunter `@Stoische.Karriere`
- Gesprochenes „Stoische Karriere“ kommt wie bisher aus der Outro-Tonspur und wird nicht neu erzeugt

### A3 CTA-Einblender (ersetzen CTA1, cta2, finale werbung)
- 8 s, 16:9. Schlichte eigene Symbole: Daumen, Glocke, Text `ABONNIEREN` in Bebas Neue. Weiß, aktive Elemente in Türkis
- Ablauf: Daumen (0,5 s) → Glocke (2,5 s) → `ABONNIEREN` (4,5 s) → halten → Ausblenden ab 7,4 s
- Die Bildfolge muss zu den gesprochenen Sätzen „Lass einen Daumen hoch da.“ / „Aktiviere die Glocke.“ / „Und abonniere …“ passen. Nach dem Schnitt die Zeiten an die Tonspur anpassen (Variablen statt fester Werte)

## 4. Auftrag B: Beitrags-Clips (Text-Clips)

**Ziel (Rene, 11.10.2026): Veröffentlichung als YouTube-Beitrag (Community-Tab).**

Technische Grenzen laut YouTube-Hilfe (Artikel 7124474, Stand 11.10.2026):
- Ein Beitrag kann Text, bis zu **10 Bilder oder GIFs** (je **höchstens 16 MB**, JPG, PNG, GIF oder WEBP, empfohlen **1:1**), eine Umfrage oder ein **Link auf ein vorhandenes YouTube-Video** enthalten.
- Eine **MP4-Datei lässt sich nicht direkt in einen Beitrag hochladen.** Ein Video im Beitrag ist immer ein schon hochgeladenes YouTube-Video (Suche, URL oder Auswahl aus dem Kanal).

Daraus folgt das Ausgabeformat je Beitrags-Clip:
1. **Animiertes GIF, 1080×1080**, höchstens 16 MB. Bei 8–15 s und vollen 30 fps ist das bei 1080 px nicht zu halten. Deshalb 15 fps und eine eigene Palette mit Dithering (`ffmpeg palettegen`/`paletteuse`). Liegt die Datei über 16 MB, zuerst auf 12 fps gehen, erst dann auf 900×900. Marmor-Verläufe auf Streifenbildung prüfen.
2. **PNG, 1080×1080**: Schlussbild als Standbild-Alternative. Bei Zitaten ist das oft lesbarer als ein GIF.
3. Optional **MP4, 1080×1920**, als Short hochladen und danach im Beitrag verlinken. Dann kommt ans Ende A2 in 9:16 (Shorts-Regel).

Gestaltung 1:1: Hintergrund `marmor_9x16.jpg` mittig auf 1080×1080 zuschneiden oder `werkzeuge/marmor.py marmor_1x1.jpg 1080 1080` erzeugen. Medaillon Ø 200 px, Text zentriert, Haupttext mindestens 80 px, Quellenzeile mindestens 36 px, Rand 80 px rundum. Lesbarkeit im Feed prüfen: auf 400 px Breite verkleinert noch lesbar.
GIFs laufen im Feed in Endlosschleife: Das letzte Bild blendet sanft auf das erste zurück, kein harter Sprung.
Umwandlung (Beispiel): `ffmpeg -i B2_Z1.mp4 -vf "fps=15,scale=1080:1080:flags=lanczos,palettegen=stats_mode=diff" pal.png` und danach `ffmpeg -i B2_Z1.mp4 -i pal.png -lavfi "fps=15,scale=1080:1080:flags=lanczos[x];[x][1:v]paletteuse=dither=sierra2_4a" -loop 0 B2_Z1.gif`. Dateigröße prüfen (höchstens 16 MB).
**Texte freigegeben (Rene, 12.10.2026: „ja“).** Die Texte unten gelten so. Änderungen nur auf Renes Wunsch.

### B1 Teaser „Neues Video“ (10 s je Clip)
Ablauf: Frage (0–3 s) → Thema (3–6,5 s) → `NEUES VIDEO AUF DEM KANAL` (6,5–8,5 s) → `@Stoische.Karriere` (8,5–10 s).
Daten aus vidIQ (abgerufen am 11.10.2026, Kanal UCQdZS4fnVeekSV4bYzY2eHg):

| Video | ID | Länge | Frage | Thema |
|---|---|---|---|---|
| Manipulation ERKENNEN: 4 stoische Regeln \| Stoizismus | 383ATxhCPK0 | 8:18 | `MERKST DU, WANN MAN DICH LENKT?` | `MANIPULATION ERKENNEN` · `VIER REGELN` |
| Grübeln beenden: Die Harvard-Methode gegen Gedankenkarussell | KseoXjgLpGo | 8:44 | `NACHTS DREHT SICH ALLES IM KOPF?` | `GRÜBELN BEENDEN` |
| Respektlos behandelt? So änderst du das Machtverhältnis sofort | 7WD2tXnbczI | 8:13 | `WIRST DU ÜBERGANGEN?` | `RESPEKT ZURÜCKHOLEN` |

Im Beitragstext steht der Videolink `https://youtu.be/<ID>`. Ob YouTube ein GIF und einen Video-Anhang im selben Beitrag zulässt, ist nicht geprüft. Notfalls nur GIF plus Link im Text.
„Harvard“ kommt nur in den Clip-Text, wenn die Quelle in `02_Quellen_Faktencheck` des Videos steht. Bitte vorher prüfen.
Keine Ziffern im Clip-Text, also „VIER“ statt „4“, wie bei der Thumbnail-Regel.

### B2 Zitatkarten (8 s je Clip)
Ablauf: Medaillon (0–1 s) → Zitat zeilenweise (1–5 s) → Quellenzeile in Türkis (5–6 s) → halten → `@Stoische.Karriere` (7–8 s).
Alle Zitate sind eigene, sinngemäße Übersetzungen. Deshalb steht in der Quellenzeile immer „sinngemäß“. Originalstellen geprüft am 11.10.2026:

| Nr | Clip-Text | Quellenzeile | Original / Beleg |
|---|---|---|---|
| Z1 | WIR LEIDEN ÖFTER IN DER VORSTELLUNG ALS IN DER WIRKLICHKEIT | SENECA · BRIEFE AN LUCILIUS XIII · SINNGEMÄSS | Ep. 13,4: „Plura sunt, Lucili, quae nos terrent quam quae premunt, et saepius opinione quam re laboramus.“ |
| Z2 | DAS BESTE MITTEL GEGEN ZORN IST WARTEN | SENECA · ÜBER DEN ZORN II · SINNGEMÄSS | De ira II,29,1: „Maximum remedium irae mora est.“ |
| Z3 | ALLES GEHÖRT ANDEREN. NUR DIE ZEIT GEHÖRT UNS | SENECA · BRIEFE AN LUCILIUS I · SINNGEMÄSS | Ep. 1,3: „Omnia, Lucili, aliena sunt, tempus tantum nostrum est.“ |
| Z4 | WIR HABEN NICHT ZU WENIG ZEIT. WIR VERSCHWENDEN ZU VIEL | SENECA · VON DER KÜRZE DES LEBENS · SINNGEMÄSS | De brev. vitae 1,3: „Non exiguum temporis habemus, sed multum perdidimus.“ |
| Z5 | DIE BESTE RACHE IST, NICHT ZU WERDEN WIE ER | MARK AUREL · SELBSTBETRACHTUNGEN VI · SINNGEMÄSS | Med. 6,6 (in der Casaubon-Zählung 6,5) |
| Z6 | NICHT DIE DINGE BEUNRUHIGEN UNS, SONDERN UNSERE MEINUNG ÜBER SIE | EPIKTET · HANDBÜCHLEIN · SINNGEMÄSS | Encheiridion 5 |

Römische Ziffern in der Quellenzeile sind Werkangaben und keine Zahlen im Fließtext. Wenn Rene auch das nicht will, die Buchangabe weglassen.
Passende Kombinationen für einen Hinweis auf ein Video: Z1 → Grübeln beenden, Z2 → Respektlos behandelt, Z6 → Manipulation erkennen.

### B3 Kanal-Werbung (15 s)
Ablauf: `STOIZISMUS UND PSYCHOLOGIE` → `FÜR MÄNNER IM BERUF UND ZU HAUSE` → drei Wörter nacheinander `RESPEKT` · `GELASSENHEIT` · `KARRIERE` (Themensäulen A, B, C aus den vidIQ-Regeln) → `JEDE WOCHE NEUE VIDEOS` → Medaillon + `@Stoische.Karriere`.
Keine Produktwerbung, nur der Kanal. „Jede Woche neue Videos“ nur verwenden, wenn der Upload-Rhythmus das tatsächlich hält.

## 5. Ablauf und Abnahme

1. Für A und B je einen Style Guide und eine Shotlist anlegen (für A1 liegen sie schon vor). Rene vorlegen und **auf sein Okay warten**.
2. Kompositionen in `outro/projekt/` bauen (eine HTML-Datei je Clip unter `compositions/` oder eigene Projektordner). Texte als `data-composition-variables`, damit sie ohne Code-Änderung austauschbar sind.
3. `npx hyperframes@0.8.149 check` ohne Fehler.
4. Zuerst einen Clip rendern und prüfen, dann den Rest:
   `npx hyperframes@0.8.149 render --fps 30 --quality high --video-bitrate 9M -o render\NAME.mp4`
   Danach mit ffmpeg auf die Kanalnorm bringen und prüfen: Schlüsselbild alle 60 Bilder (`-g 60`), AAC 160 kbit/s, stille Tonspur falls keine vorhanden. Mit `ffprobe` gegenprüfen: Auflösung, 30 fps, Bitrate, Dauer.
5. Prüfprotokoll je Clip: ein Stichbild je Sekunde, alle Ecken und die Mitte (Wasserzeichen, Artefakte), Rechtschreibung, Handytest (auf 640 px Breite verkleinert lesbar), Farben nur Weiß und Türkis.
6. Rene fragen, unter welchem Namen gespeichert wird. Ordner nach der Regel „VNN Themenname“ gilt für Videos. Für diese Clips einen eigenen Ordner vorschlagen, z. B. `Kanal Grafik Set`.

## 6. Offene Punkte für Rene

- Erledigt: ganzes Set. Veröffentlichung der Beitrags-Clips als YouTube-Beitrag. Das Medaillon ist fiktiv und wird einheitlich als Markenzeichen genutzt.
- Beitrags-Clips zusätzlich als Short (9:16 MP4)? Für einen Beitrag reicht GIF plus PNG.
- Erledigt: Texte der Teaser, Zitate und Werbung freigegeben.
- Profilbild: A (ganzes Medaillon) oder B (Ausschnitt Kopf und Fackel)? Empfehlung B, siehe Abschnitt 7.

## 7. Kanal-Branding: Profilbild und Banner (in der Cloud-Sitzung fertig erstellt)

Dateien in `kanal_branding/`, erzeugt mit `outro/werkzeuge/branding.py` (deterministisch, Bebas Neue, Medaillon `#00E5FF`):

| Datei | Größe | Zweck |
|---|---|---|
| `profilbild_A_medaillon.png` | 800×800 | ganzes Medaillon |
| `profilbild_B_ausschnitt.png` | 800×800 | Kopf und Fackel, **Empfehlung**: bleibt bei 32–48 px erkennbar, A wird dort zum Fleck |
| `vorschau_profilbild_klein.png` | – | A und B als Kreis in 160/98/48/32 px auf hellem und dunklem Grund |
| `banner_2560x1440.jpg` | 2560×1440, rund 0,25 MB | Kanalbanner |
| `vorschau_banner_sichere_flaeche.jpg` | – | rot: sichere Fläche 1546×423 (überall sichtbar), gelb: Desktop-Streifen. Nur zur Kontrolle, nicht hochladen |

Maße (Drittquellen, die offizielle Hilfeseite 2972003 war aus der Cloud nicht erreichbar):
- Banner 16:9, mindestens 2048×1152, empfohlen 2560×1440, höchstens 6 MB. Sichere Fläche 1235×338 bei 2048×1152. Das ist dasselbe Verhältnis wie 1546×423 bei 2560×1440, die Angaben widersprechen sich also nicht.
- Profilbild 800×800 empfohlen, Anzeige als Kreis ab 98×98. Die Angaben zur Höchstgröße der Datei schwanken zwischen 2 und 15 MB. Die PNGs liegen mit 0,8 MB unter allen genannten Grenzen.

Hochladen macht Rene selbst (YouTube Studio → Anpassung → Branding). Vor dem Hochladen in der Studio-Vorschau prüfen, ob die Darstellung auf Handy, Desktop und TV passt.
