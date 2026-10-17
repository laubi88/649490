// Inhalte des Erklär-Mods. Nur Text, keine Logik.
// Quellen (geprüft am 17.10.2026): code.claude.com/docs/en/desktop, /permission-modes,
// /model-config, /cloud-environments, /claude-code-on-the-web, platform.claude.com/docs/en/models/overview.
// Was die Dokumentation nicht hergibt, ist im Text als „nicht dokumentiert“ markiert.

export type Thema = {
  id: string
  taste: string
  titel: string
  text: string
}

export const THEMEN: readonly Thema[] = [
  {
    id: 'umgebung',
    taste: '1',
    titel: 'Umgebung: Default, Claude Home, video-automation',
    text: [
      '**Umgebung** (englisch: environment) ist der Rechner, auf dem Claude arbeitet. Die App kennt Lokal, Cloud, SSH und WSL.',
      '',
      '- **Wolken-Symbol, „Default“**: Cloud-Umgebung bei Anthropic, automatisch angelegt, Netzwerk auf Stufe „Trusted“ (GitHub, Paketquellen). Das Repository wird dort frisch geklont. Deine Dateien auf dem PC (Desktop, Clips, Alt-Videos) sieht sie **nicht**. Kein @-Erwähnen von Dateien, kein Dateifenster, keine Desktop-Plugins. Läuft weiter, wenn du die App schließt. Nach einigen Minuten Leerlauf pausiert der Rechner; später kann er abgeräumt werden, der Chat bleibt, Hintergrundarbeit nicht. Nur was per `git push` ins Repository geht, ist sicher.',
      '- **Laptop-Symbol, „Claude Home“ / „video-automation“**: lokale Umgebungen auf deinem Windows-PC. Claude sieht deine Dateien, kann ffmpeg, HyperFrames und Python starten und rendern. Zwei Einträge heißt: zwei lokale Ordner oder Einstellungen, die du angelegt hast.',
      '',
      '**Wofür welche?**',
      '- Cloud: Sprechertexte, Titel, Quellenprüfung, Skripte im Repo, alles was nur Text und das Repository braucht.',
      '- Lokal: Rendern (Outro, Beitrags-Clips, Thumbnails), Schnittvorbereitung, alles was deine Clips auf dem Desktop braucht.',
      '',
      '„Umgebung auswählen“ gilt für die **nächste** Sitzung; eine laufende Sitzung bleibt, wo sie ist.',
    ].join('\n'),
  },
  {
    id: 'repo',
    taste: '2',
    titel: 'Ordner-Symbol: laubi88/649490 (Repository)',
    text: [
      '**Repository** (kurz: Repo) ist dein Projektordner mit Versionsverlauf bei GitHub. „laubi88“ ist dein GitHub-Name, „649490“ der Name des Repos.',
      '',
      'Darin liegen CLAUDE.md, die Skills, die Skripte, die Musikbibliothek, das Outro-Projekt und das Kanal-Redesign. Alles, was Claude dort ändert und per `git push` hochlädt, ist dauerhaft gesichert und von jeder Umgebung aus erreichbar.',
    ].join('\n'),
  },
  {
    id: 'branch',
    taste: '3',
    titel: 'Verzweigungs-Symbol: claude/… (Branch)',
    text: [
      '**Branch** (deutsch: Zweig) ist eine eigene Arbeitslinie im Repository. Die Hauptlinie heißt meist `main`.',
      '',
      'Jede Claude-Sitzung arbeitet auf einem eigenen Zweig, zum Beispiel `claude/skill-geladen-opus-motion-3urqdf`. Der Name ist automatisch vergeben und bedeutet nichts.',
      '',
      '**Ablauf:** Claude ändert Dateien auf dem Zweig → **Commit** (Speicherpunkt mit Beschreibung) → **Push** (Hochladen zu GitHub) → **Pull Request** (Antrag, den Zweig in `main` zu übernehmen) → **Merge** (Zusammenführen).',
      '',
      'Solange nicht gemergt wurde, sieht `main` die Änderungen nicht. Zwei Sitzungen auf zwei Zweigen können sich deshalb widersprechen.',
    ].join('\n'),
  },
  {
    id: 'modus',
    taste: '4',
    titel: '„Auto“: Berechtigungsmodus',
    text: [
      'Der **Berechtigungsmodus** (englisch: permission mode) legt fest, wie oft Claude vor einer Aktion um Erlaubnis fragt. Die Auswahl merkt sich die App je Ordner.',
      '',
      '- **Manual** (in der Einstellungsdatei `default`): fragt vor jeder Dateiänderung und jedem Befehl, du siehst den Unterschied und nimmst an oder lehnst ab.',
      '- **Accept edits**: Dateiänderungen und einfache Dateibefehle (Ordner anlegen, kopieren, verschieben) laufen ohne Nachfrage, andere Befehle werden abgefragt.',
      '- **Plan**: Claude liest nur und legt einen Plan vor, ändert keinen Quelltext. Gilt nur für die laufende Sitzung.',
      '- **Auto**: keine Routinefragen. Ein zweites Prüfmodell schaut jede Aktion vorher an und blockt, was über den Auftrag hinausgeht, fremde Systeme anfasst oder aus gelesenem Fremdinhalt stammt. Nach drei Blocks hintereinander oder zwanzig insgesamt pausiert Auto und fragt wieder. Die Doku sagt wörtlich: keine Sicherheitsgarantie.',
      '- **Bypass permissions**: fragt nie. Erscheint nur, wenn du es in den Einstellungen freischaltest. Nur für abgeschottete Container gedacht.',
      '',
      '**Für dich:** „Auto“ für Textarbeit im Repo ist passend. Für alles, was deinen Kanal oder deine Clips berührt, gilt trotzdem CLAUDE.md: nichts hochladen, nichts löschen ohne dein Ja.',
    ].join('\n'),
  },
  {
    id: 'modell',
    taste: '5',
    titel: '„Fable 5.1“: das Modell',
    text: [
      'Das **Modell** ist das Sprachmodell, das die Sitzung antreibt. Claude-5-Familie, von stark und teuer nach schnell und günstig (Preis je Million Textbausteine, Eingabe / Ausgabe):',
      '',
      '- **Fable 5.1**: stärkstes Modell, langsamste Antwort, zehn / fünfzig Dollar. Für anspruchsvolles Denken und lange Arbeitsketten. Ist auf keinem Tarif die Voreinstellung und kann Nutzungsguthaben kosten.',
      '- **Opus 5.5**: vier / zwanzig Dollar, mittlere Geschwindigkeit. Laut Doku der empfohlene Ausgangspunkt für die meisten Aufgaben und die Voreinstellung in Claude Code.',
      '- **Sonnet 5.5**: zwei / zehn Dollar, schnell. Beste Mischung aus Tempo und Können für tägliche Arbeit.',
      '- **Haiku 5.5**: ab zehn Cent / fünfzig Cent, am schnellsten. Für einfache Massenaufgaben wie Sortieren und Einordnen.',
      '',
      '**Für dich:**',
      '- Fable oder Opus: Sprechertexte mit allen Valentino-Regeln, Faktenprüfung, Schnittplan, Fehlersuche im Render-Projekt.',
      '- Sonnet: kleine Änderungen, Umbenennen, Prüfprotokolle, kurze Fragen.',
      '- Haiku: Kleinkram wie Listen sortieren oder eine Datei suchen.',
      '',
      'Faustregel: Je mehr Regeln gleichzeitig gelten müssen, desto stärker das Modell. Ein Thumbnail-Text mit vier Wörtern braucht kein Fable. Wechsel mit `/model`.',
    ].join('\n'),
  },
  {
    id: 'aufwand',
    taste: '6',
    titel: '„Hoch“: Denkaufwand (Effort)',
    text: [
      '**Aufwand** (englisch: effort) steuert, wie tief das Modell nachdenkt, bevor es antwortet. Fünf Stufen: **Niedrig, Mittel, Hoch, Sehr hoch, Maximal** (low, medium, high, xhigh, max).',
      '',
      '- Höher: prüft mehr Sonderfälle, kontrolliert sich mehr, braucht länger und mehr Textbausteine.',
      '- Niedriger: liefert schneller einen Anfang, gut für einfache Aufgaben.',
      '- Genaue Faktoren für Zeit und Kosten je Stufe nennt die Doku nicht.',
      '',
      '**Für dich:**',
      '- Niedrig/Mittel: Datei kopieren, Tippfehler, kurze Antwort.',
      '- Hoch: Sprechertext schreiben, Quellen prüfen, Schnittplan rechnen.',
      '- Sehr hoch/Maximal: schwere Planung, zum Beispiel ein ganzes Videopaket oder eine Fehlersuche im Render-Projekt.',
    ].join('\n'),
  },
  {
    id: 'oben',
    taste: '7',
    titel: 'Oben rechts: Terminal, Globus, Fenster',
    text: [
      '- **>_ Terminal** (Strg+`): öffnet die Befehlszeile im Arbeitsordner der Sitzung. Sie teilt sich die Umgebung mit Claude, du kannst dort selbst Befehle tippen.',
      '- **Globus**: laut Doku gibt es in der Titelleiste eine Schaltfläche „Browser“ (Strg+Umschalt+B), die ein Browserfenster in der App öffnet, zum Beispiel für eine Vorschau. Dass der Globus genau diese Schaltfläche ist, steht nicht in der Doku; es ist die einzige, die passt.',
      '- Je nach Fensterbreite liegen dort auch „Changes“ (Änderungen als Unterschied) und ein Menü „⋮“ mit weiteren Fenstern wie „Files“.',
      '- **Strich, Doppelfenster, X**: Fenster verkleinern, vergrößern, schließen. Schließen beendet eine Cloud-Sitzung nicht; sie läuft weiter.',
    ].join('\n'),
  },
  {
    id: 'eingabe',
    taste: '8',
    titel: 'Eingabezeile: Plus, Mikrofon, Maskottchen, Kreis',
    text: [
      '- **+** links: Dateien und Bilder anhängen, Schrägstrich-Befehle, Verbindungen (Connectors) und Plugins. Bilder gehen auch per Ziehen und Ablegen.',
      '- **Mikrofon** rechts: Spracheingabe. In der Doku nicht beschrieben, die Funktion kennst du aus eigener Nutzung.',
      '- **Orangenes Pixelwesen**: in der Doku nicht beschrieben. Nach allem, was sichtbar ist, ein Maskottchen ohne eigene Funktion.',
      '- **Kreis ganz rechts** neben „Hoch“: laut Doku sitzt neben der Modellauswahl ein **Nutzungsring**. Er zeigt den Füllstand des Kontextfensters (Gedächtnis dieser Sitzung) und den Verbrauch deines Tarifs. Voll bedeutet: Claude fasst die Unterhaltung zusammen und verliert Details.',
    ].join('\n'),
  },
  {
    id: 'befehle',
    taste: '9',
    titel: 'Schrägstrich-Befehle, Skills, Mods',
    text: [
      'Ein Text, der mit **/** beginnt, ist ein Befehl an Claude Code, kein Auftrag an das Modell.',
      '',
      '- `/model`: Modell wechseln. `/config`: Einstellungen. `/clear`: Unterhaltung leeren.',
      '- `/erklaeren`: diese Spalte öffnen.',
      '- Skills aus deinem Repo: `/packaging-agent`, `/thumbnail-agent`, `/retention-skript`, `/flow-und-cta`. Sie laden die Regeln aus `.claude/skills/`.',
      '',
      '**Skill** = Anleitung, die Claude bei einer bestimmten Aufgabe liest. **Mod** (Plugin) = Erweiterung, die die Oberfläche oder das Verhalten von Claude Code ändert, so wie diese Spalte.',
    ].join('\n'),
  },
]

export type Wort = { en: string; de: string; hinweis: string }

export const WOERTERBUCH: readonly Wort[] = [
  { en: 'Environment', de: 'Umgebung', hinweis: 'Rechner, auf dem Claude arbeitet (Cloud oder dein PC)' },
  { en: 'Default', de: 'Standard / Voreinstellung', hinweis: 'bei Umgebungen: die automatisch angelegte Cloud' },
  { en: 'Repository / Repo', de: 'Projektordner mit Verlauf', hinweis: 'liegt bei GitHub' },
  { en: 'Branch', de: 'Zweig', hinweis: 'eigene Arbeitslinie im Repo' },
  { en: 'Commit', de: 'Speicherpunkt', hinweis: 'Änderung mit Beschreibung festhalten' },
  { en: 'Push', de: 'Hochladen', hinweis: 'Commits zu GitHub schicken' },
  { en: 'Pull Request (PR)', de: 'Übernahmeantrag', hinweis: 'Zweig in main übernehmen lassen' },
  { en: 'Merge', de: 'Zusammenführen', hinweis: 'zwei Zweige vereinen' },
  { en: 'Session', de: 'Sitzung', hinweis: 'ein Chat mit eigener Umgebung und eigenem Zweig' },
  { en: 'Prompt', de: 'Eingabe / Auftrag', hinweis: 'das, was du Claude schreibst' },
  { en: 'Token', de: 'Textbaustein', hinweis: 'Recheneinheit, etwa drei Viertel eines Wortes' },
  { en: 'Context window', de: 'Kontextfenster', hinweis: 'das Gedächtnis einer Sitzung' },
  { en: 'Usage ring', de: 'Nutzungsring', hinweis: 'der Kreis neben dem Modell' },
  { en: 'Permission mode', de: 'Berechtigungsmodus', hinweis: 'wie oft Claude fragt' },
  { en: 'Manual', de: 'Von Hand', hinweis: 'Modus: vor allem fragen' },
  { en: 'Accept edits', de: 'Änderungen annehmen', hinweis: 'Modus: Dateiänderungen ohne Frage' },
  { en: 'Plan mode', de: 'Planmodus', hinweis: 'nur lesen und planen, nichts ändern' },
  { en: 'Bypass permissions', de: 'Berechtigungen umgehen', hinweis: 'Modus: nie fragen' },
  { en: 'Effort', de: 'Aufwand', hinweis: 'Denktiefe des Modells' },
  { en: 'Model', de: 'Modell', hinweis: 'Fable, Opus, Sonnet, Haiku' },
  { en: 'Skill', de: 'Anleitung', hinweis: 'Regeln für eine Aufgabe' },
  { en: 'Plugin / Mod', de: 'Erweiterung', hinweis: 'ändert Oberfläche oder Verhalten' },
  { en: 'Connector', de: 'Verbindung', hinweis: 'Anschluss an Dienste wie Gmail oder vidIQ' },
  { en: 'Hook', de: 'Haken', hinweis: 'läuft automatisch bei einem Ereignis' },
  { en: 'Tool', de: 'Werkzeug', hinweis: 'was Claude aufruft: Datei lesen, Befehl starten' },
  { en: 'Worktree', de: 'Arbeitskopie', hinweis: 'zweiter Ordner desselben Repos' },
  { en: 'Terminal', de: 'Befehlszeile', hinweis: 'Textfenster für Befehle' },
  { en: 'Changes', de: 'Änderungen', hinweis: 'Fenster mit dem Unterschied vorher/nachher' },
  { en: 'Thumbnail', de: 'Vorschaubild', hinweis: 'das Bild im YouTube-Feed' },
  { en: 'Render', de: 'Berechnen / Ausgeben', hinweis: 'aus Projekt eine Videodatei machen' },
]
