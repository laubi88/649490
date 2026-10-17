# CLAUDE.md – Master-Regeln für den Kanal Stoische Karriere

Stand: 12.10.2026. Kanal: Stoische Karriere (@Stoische.Karriere). Stoizismus und Psychologie für Männer im Beruf und zu Hause.
Teil A (Abschnitte M0 bis M5) gilt für jede Arbeit in diesem Repo. Teil B weiter unten ist die Übergabe für Outro, Beitrags-Clips und Branding (11. und 12.10.2026). Teil A und Teil B sind aufeinander abgestimmt. Die Kürzel A1, A2, A3a bis A3c und B1 bis B3 bezeichnen immer die Clips aus Teil B, die Kürzel M0 bis M5 die Abschnitte von Teil A.

## M0. Skills: welcher wann

Die Produktions-Skills liegen als echte Claude-Code-Skills in `.claude/skills/<name>/SKILL.md` und werden automatisch erkannt.

| Aufgabe | Skill |
|---|---|
| Titel, Verpackung, Neugierlücke | `packaging-agent` |
| Thumbnail planen und erzeugen | `thumbnail-agent`, Werkzeug `thumbnail_maker.py` |
| Sprechertext, Hook, CTA-Zeitpunkte | `retention-skript` |
| Zusatzclips 46 bis 50 (Flow-Prompts) und Schnittplan | `flow-und-cta` |

Zusätzlich gelten die Konto-Skills `stoische-karriere-videovorlage`, `stoische-karriere-vidiq-regeln`, `stoische-karriere-untertitel-stil` und `opus-motion-design-hyperframes`. Die Repo-Skills widersprechen ihnen nicht. Wo sie strenger oder neuer sind, steht es in M5.

## M1. Visuelle Identität

- Bildwelt: verwitterter römischer Carrara-Marmor (Statuen, Büsten, Säulen, Torbögen) im extremen Low-Key-Licht. Fast schwarzer Hintergrund, ein hartes Kantenlicht von der Seite, tiefe Schatten, keine aufgehellten Flächen.
- Farben: nur Weiß `#FFFFFF` und Türkis `#00E5FF` als Akzent auf dunklem Marmor oder Schwarz. Kein Gold, kein Orange, kein Rot, keine weiteren Akzentfarben.
- Türkis markiert das aktive oder hervorgehobene Element: erste Thumbnail-Zeile, gesprochenes Wort im Untertitel, Quellenzeile, Abo-Symbol. Weiß ist die Grundfarbe für Text.
- Schriften, immer in Großbuchstaben:
  - Thumbnails: **Anton** (`schriften/Anton-Regular.ttf`, Lizenz `schriften/OFL.txt`).
  - Untertitel, Outro-Set, Beitrags-Clips und Kanal-Branding: **Bebas Neue** (`outro/projekt/assets/fonts/`, siehe Teil B).
- Markenzeichen: das türkise Medaillon `outro/projekt/assets/img/medaillon_tuerkis.png` (fiktive Figur, kein offizielles Logo).
- Keine modernen Gegenstände, kein echtes Gesicht, kein YouTube-Logo, kein Wasserzeichen in irgendeinem Bild.
- Video: 1920×1080 oder 1080×1920, 30 fps, H.264 9 Mbit/s, Schlüsselbild alle 60 Bilder, AAC 160 kbit/s.
- Thumbnail: 1920×1080, JPG unter 2 MB. Zeile 1 Türkis (klein), Zeile 2 Weiß (groß), zwei bis vier Wörter. Details im Skill `thumbnail-agent`.

## M2. Valentino-Sprachregeln (jeder Sprechertext)

Der Sprechertext wird mit der Stimme Valentino bei Geschwindigkeit 0,90 eingesprochen. Damit die Stimme sauber liest, gilt ohne Ausnahme:

1. **Keine Ziffern.** Jede Zahl als Wort: „vier“, „dreiundvierzig“, „zweitausendsechsundzwanzig“.
2. **Keine Bindestriche** und keine Gedankenstriche. Zusammensetzungen zusammenschreiben oder umformulieren.
3. **Höchstens zwölf Wörter pro Satz.**
4. **Genau ein Satz pro Absatz**, zwischen den Absätzen eine Leerzeile.
5. **Keine englischen Wörter.** Eindeutschen: Job → Arbeit oder Stelle, Meeting → Besprechung, Team → Mannschaft oder Kollegen, Feedback → Rückmeldung, Deadline → Frist, Boss → Chef, Coach → Trainer, Check → Prüfung, okay → gut, sorry → Entschuldigung, cool → gelassen, Update → Neuigkeit.
6. **Gesperrte Wörter streichen:** Stoa, Stoiker, stoisch, Punkt, Stress. Erlaubt bleibt „Stoizismus“.
   Einzige Ausnahme: der Kanalname im Outro als zwei Absätze „Stoische.“ und „Karriere.“. In CTA1 und CTA2 heißt es „diesen Kanal“.
7. Keine Abkürzungen (zum Beispiel statt z. B.), korrekte Umlaute.
8. Blocknamen, Überschriften und die Zeile `DATEI:` werden nie gesprochen.
9. Namen von Denkern als eigener Satz („Seneca.“). Wörtliche Zitate vorher als sinngemäß ankündigen.

Prüfung vor jeder Vertonung: `python kanal_redesign/werkzeuge/sprechertext_pruefen.py <datei>` muss 0 Verstöße melden. Das Skript prüft die Regeln 1 bis 7 zeilenweise. Englische Wörter erkennt es nur aus seiner Liste, deshalb zusätzlich selbst lesen.

## M3. Clip-Regeln

- **Clips 1 bis 45:** Standard-Marmorclips. Allgemeines Bildmaterial im Kanallook, für jedes Video frei verwendbar, wenn der Clip zum gesprochenen Inhalt passt.
- **Clips 46 bis 50:** themenspezifische Zusatzclips. Sie werden je Video neu mit englischem Prompt in Flow geplant (Format im Skill `flow-und-cta`) und in `05_Flow_Prompts_Zusatzclips_EN` des Videoordners abgelegt.
- Jeder Clip kommt pro Video genau einmal vor. Reicht das Material nicht, wird ein Zusatzclip geplant und kein Clip wiederholt.
- Vor dem Einbau jeden Clip auf Wasserzeichen prüfen: je Sekunde ein Stichbild, alle vier Ecken und die Mitte. Ein Clip mit Wasserzeichen oder Bildfehler wird ersetzt, nicht retuschiert.
- Weiche Blende 0,8 s zwischen den Clips, kein Standbild, kein Schwarzbild.
- Werbe-Einblender, Logo und Endcard: bis das neue Set aus Teil B (A1, A2, A3a bis A3c) fertig ist, die Alt-Clips laut Videovorlage Abschnitt 4.

## M4. CTA-Positionen und Videolänge

| Teil | Lage | Länge |
|---|---|---|
| Hook | 0:00 bis rund 0:55, Anti-43-Sekunden-Hook | |
| CTA-Verbot | 0:00 bis 2:00 | |
| CTA 1 | direkt nach Werkzeug eins, bei 30 bis 40 Prozent der Laufzeit | rund 20 s |
| CTA 2 | direkt nach Werkzeug drei, bei rund 70 Prozent | rund 20 s |
| Outro | am Ende, die letzten rund 20 s Sprechertext | 15 bis 20 s |
| Logo (A2) und Endcard (A1) | nach dem Outro | 4 s und 10 s |

Videolänge acht bis zwölf Minuten. Die Zeitpunkte richten sich nach der echten Länge und werden nach dem Schnitt aus den gemessenen Startzeiten nachgerechnet. Details und Rechenbeispiele im Skill `retention-skript`.

## M5. Werkzeuge, Grenzen und Entscheidungen

- `thumbnail_maker.py` (Hauptverzeichnis): Thumbnails 1920×1080 unter 2 MB, Schrift Anton. Braucht Python 3 mit Pillow und NumPy. Aufruf im Kopf der Datei und im Skill `thumbnail-agent`.
- Verboten: ElevenLabs, DaVinci Resolve. Nichts hochladen, nichts löschen, keine Kanaleinstellungen ändern ohne Renes Ja. Downloads nur mit Renes Erlaubnis (Anton: erlaubt am 12.10.2026).
- Keine Fakten, Zahlen oder Zitate erfinden. Jede Angabe mit geprüfter Quelle in `02_Quellen_Faktencheck`.
- Rhythmus: nie mehrere Videos am selben Tag.
- Musik: Bibliothek in `musik/` (Übersicht `musik/00_Musikbibliothek.md`), Prompts für neue Tracks in `kanal_redesign/04_Musik_Prompts_und_8_Minuten.md`. Filmisch, ohne Gesang, keine schwermütige Streichermusik (Rene, 13.10.2026). Zwei Videos hintereinander nie mit demselben Track.

Entscheidungen von Rene am 12.10.2026, die ältere Angaben in den Konto-Skills genauer fassen:

| Thema | Konto-Skill | Gilt jetzt |
|---|---|---|
| Erster CTA | nicht in den ersten 60 s | nicht vor 2:00 |
| Videolänge | Videovorlage: 7 bis 9 min, vidIQ-Regeln: 8 bis 12 min | 8 bis 12 min |
| Clips | „bis zu zwei“ bzw. „fünf bis acht“ Zusatzclips | Zusatzclips tragen die Nummern 46 bis 50 |

Thumbnail-Maße, Thumbnail-Farben und CTA-Positionen entsprechen unverändert den Konto-Skills und Teil B.

## M6. Sprache gegenüber Rene (Rene, 17.10.2026)

- Jede Frage und jede Auswahloption an Rene wird auf Deutsch gestellt. Englische Fachwörter bekommen die deutsche Bedeutung in Klammern dahinter.
- Zeigt das Programm selbst einen englischen Dialog (zum Beispiel „Enable hot reloading for this session?“ beim Laden eines Mods), erklärt Claude vorher oder gleich danach im Chat auf Deutsch, was der Dialog bedeutet, was die Antworten bewirken und welche Antwort Claude empfiehlt. Die Dialoge des Programms selbst kann Claude nicht übersetzen.
- Der Erklär-Mod für die Oberfläche liegt in `mods/erklaer-mod/` (Anleitung in der README dort).

---

Ab hier folgt Teil B, die bisherige Übergabe, unverändert.

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
3. **MP4, 1080×1920, als Short (Rene, 12.10.2026: ja).** Eigenes Layout, nicht das 1:1-Bild hochskaliert:
   - Hintergrund `marmor_9x16.jpg`, Medaillon Ø 260 px, Haupttext mindestens 96 px, Quellenzeile mindestens 44 px
   - Text innerhalb x 90–990 und y 250–1500. Das ist ein Richtwert gegen die Shorts-Bedienelemente, auf dem Handy prüfen.
   - Ans Ende kommt A2 in 9:16, gesprochen „Stoische Karriere“ aus der Outro-Tonspur, darunter `@Stoische.Karriere` (Shorts-Regel aus `stoische-karriere-vidiq-regeln`)
   - 30 fps, 9 Mbit/s, AAC 160 kbit/s. Musik nur, wenn Rene sie liefert. Kein ElevenLabs.
   - Der fertige Short kann danach im Beitrag als vorhandenes YouTube-Video verlinkt werden.
   - Nicht alle Shorts am selben Tag veröffentlichen. Rhythmusregel aus `stoische-karriere-vidiq-regeln`: nie mehrere Videos am selben Tag.

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
Passende Kombinationen für einen Hinweis auf ein Video (laut Transkripten, 12.10.2026): Z1 → Grübeln beenden (KseoXjgLpGo, dort zitiert), Z2 → Warum Kälte keine Stärke ist (uFUc7Ku3iMU, dort zitiert), Z5 → Wie du dich nie wieder provozieren lässt (Lresm2yBPU4, dort zitiert), Z6 → Manipulation erkennen (thematisch passend).

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
- Erledigt: Beitrags-Clips zusätzlich als Short (9:16 MP4), Rene am 12.10.2026.
- Erledigt: Texte der Teaser, Zitate und Werbung freigegeben.
- Profilbild: Rene will A und B (12.10.2026). Ein YouTube-Kanal hat aber genau **ein** Profilbild. Beide Dateien bleiben. Rene entscheidet beim Hochladen, welches aktiv ist (Empfehlung B).

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

## 8. Kanal-Redesign und Skripte (12.10.2026)

Alles in `kanal_redesign/`, Übersicht in `kanal_redesign/00_Uebersicht.md`: Kanaltexte, Kanaltrailer, V15 und V16 komplett (Sprechertext, Quellen, Short) und fünf Begleit-Shorts für ältere Videos.
Vor dem Vertonen jede Datei mit `python kanal_redesign/werkzeuge/sprechertext_pruefen.py <datei>` prüfen. Sie muss 0 Verstöße zeigen.
