# Konnektoren, Plugins und Skills: was ist was, und was der Kanal braucht

Stand: 15.10.2026. Beobachtet in einer Claude-Code-Cloud-Sitzung an diesem Tag. Was dort verbunden war, steht unten. Später hinzugefügte Dinge fehlen, dann diese Datei ergänzen.

## Die drei Begriffe

| Begriff | Was es ist | Kostet |
|---|---|---|
| **Konnektor** | Eine Verbindung zu einem fremden Konto (Gmail, GitHub, vidIQ). Gibt Claude Werkzeuge, um dort zu lesen und zu schreiben. | Je Sitzung einmal die Liste der Werkzeugnamen im Kontext. Nicht bei jeder Nachricht neu. Dienste wie vidIQ rechnen eigene Credits ab. |
| **Plugin** | Ein Paket aus dem Katalog. Enthält Skills und bringt oft eigene Konnektoren mit, die man nicht bewusst eingeschaltet hat. | Wie Konnektoren, nur in Bündeln. Ein Plugin kann dreißig Konnektoren mitbringen. |
| **Skill** | Eine Anleitung, wie Claude eine Aufgabe erledigt. Liegt als Textdatei vor. | Nichts, solange er nicht aufgerufen wird. |

Claude sucht nicht bei jeder Nachricht alle Konnektoren ab. Der Schaden vieler Konnektoren ist ein anderer: Rauschen, Fehlgriffe beim Werkzeug, Fehlermeldungen beim Start, längere Startzeit.

**Faustregel:** Wenn du zu einem Konnektor oder Plugin nicht in einem Satz sagen kannst, wofür du es für den Kanal brauchst, trenne es.

Verwalten: Konnektoren unter https://claude.ai/customize/connectors. Plugins im Katalog derselben Einstellungen. Änderungen gelten erst für die nächste Sitzung.

## Konnektoren

### Für den Kanal nützlich, behalten

| Konnektor | Was er macht | Nutzen für Stoische Karriere |
|---|---|---|
| GitHub | Speichert dieses Repo mit allen Texten, Skripten und Regeln | Ohne ihn läuft keine Sitzung an diesem Repo |
| vidIQ | Kanaldaten, Titelwertung, Transkripte, Suchmengen; setzt Titel, Beschreibung, Tags und Veröffentlichungstermin bei vorhandenen Videos | Wichtigstes Werkzeug. Kostet Credits (Stand 12.10.2026: 127 bis 02.11.2026). Lädt **keine** Videos auf YouTube hoch. |
| Google Drive | Dateien in deiner Drive lesen und ablegen | Weg, um Videodateien vom PC in die Cloud zu bringen, wenn Claude sie prüfen soll |
| Gmail | Mails lesen, Entwürfe schreiben | Nur, wenn Claude Mails vorbereiten soll |
| OpenArt | Bilder und Videos per KI erzeugen | Büsten für Thumbnails, Marmorclips |
| Adobe | Express, Firefly, Bildbearbeitung, PDF | Hintergrund entfernen, Bilder zuschneiden, Thumbnail-Vorlagen |
| Descript | Videoschnitt über den Text, Untertitel, Export | Nur, wenn du es statt CapCut nutzt |

### Für den Kanal ohne Nutzen, trennen

| Konnektor | Was er macht |
|---|---|
| Indeed | Stellenanzeigen und Lebensläufe |
| WordPress.com | Webseiten und Blog-Beiträge |
| Microsoft Learn | Dokumentation für Programmierer |
| Google Docs, Sheets, Slides | Texte, Tabellen, Folien bei Google. Behalten nur, wenn du den Messzettel in einer Tabelle führen willst |
| Claude Docs | Gemeinsam bearbeitbare Dokumente in Claude |
| Canva | Grafiken und Vorlagen. Überschneidet sich mit Adobe, eins reicht |
| Notion | Notizen und Datenbanken. Nur behalten, wenn du Notion wirklich benutzt |

## Plugins

### Behalten

| Plugin | Was es macht | Hinweis |
|---|---|---|
| vidIQ | Zwölf Skills: Kanalprüfung, Titel und Thumbnails, Kommentarauswertung, Zuschauerbindung, Trends, Konkurrenz | Der eigene Konnektor des Plugins scheitert in der Cloud (403). Die Skills laufen über den vidIQ-Konnektor oben, es fehlt also nichts. |
| PDF-Viewer | PDFs ansehen, markieren, Formulare füllen | Harmlos, nützlich für Studien im Faktencheck |

### Deine Entscheidung

| Plugin | Was es macht | Einschätzung |
|---|---|---|
| Postiz | Beiträge auf 28 Plattformen planen, auch YouTube | Braucht ein Postiz-Konto. Für YouTube allein kein Vorteil gegenüber „Geplant“ in YouTube Studio. Nur sinnvoll mit Instagram oder TikTok. |
| ManyMotions (ai-video-editor) | Videoclips per KI erzeugen und auf einer Zeitleiste schneiden | Könnte Clips 46 bis 50 liefern. Nicht geprüft, braucht ein eigenes Konto. In der Cloud scheitert die Verbindung (403). |
| mysocial-intelligence | Marken-Dokumente, nächsten Beitrag schreiben, Kontaktaufnahme, Creator-Recherche | Für Social Media. Nicht geprüft, braucht ein eigenes Konto. |
| Adobe-Plugin (adobe-for-creativity) | Skills für PDF, Fotos, Social-Varianten | Doppelt zum Adobe-Konnektor. Eins von beiden reicht. |

### Nichts mit dem Kanal zu tun, deinstallieren

| Plugin | Was es macht |
|---|---|
| small-business | Rund 43 Konnektoren (Buchhaltung, Lohn, Steuer, CRM, Shopify, PayPal, DocuSign, HubSpot und mehr) und Skills für Rechnungen, Lohnabrechnung, Steuer, Einstellung |
| data | Datenanalyse und SQL für Firmen-Datenbanken (Amplitude, Hex, BigQuery, Definite) |
| design | Software-Design-Werkzeuge (Figma, Linear, Slack, Asana, Atlassian, Intercom) |
| figma | Benutzeroberflächen entwerfen |
| ai-ready-ds | Prüft Figma-Design-Systeme |
| productivity | Aufgabenlisten mit ClickUp und Monday |
| unity | Spiele-Engine Unity |
| abp-sensei | Programmier-Framework ABP für .NET |
| zizi-skills | Software-Entwicklung: Code-Prüfung, Datenbanken, Frontend, Git |
| workflow-audit | Prüfung von Apple-Apps (SwiftUI) |
| alice | Musikvertrieb Soundscape |
| aria | Musikvertrieb Patchline |
| potion | Private Podcast-Feeds |
| cowork-plugin-management | Eigene Plugins bauen |

## Skills, die der Kanal wirklich nutzt

| Skill | Wo | Wofür |
|---|---|---|
| packaging-agent, thumbnail-agent, retention-skript, flow-und-cta | im Repo, `.claude/skills/` | Titel, Thumbnail, Sprechertext, Zusatzclips (siehe CLAUDE.md M0) |
| stoische-karriere-videovorlage, -vidiq-regeln, -untertitel-stil | Konto-Skills | Kanalregeln |
| opus-motion-design-hyperframes | Konto-Skill | Outro, Logo, Beitrags-Clips als Code |
| capcut-studio-block-schnitt | Konto-Skill | Schnitt im CapCut Studio |
| chrome-browser, computer-use | Konto-Skills | Claude bedient deinen Browser oder PC, zum Beispiel YouTube Studio. Nichts hochladen ohne dein Ja. |
| vidiq-* (zwölf Skills) | Plugin vidIQ | Siehe oben |

## Automatisches Hochladen zu Terminen

Geht mit dem, was hier liegt, nicht vollautomatisch, und braucht keinen neuen Skill:

1. Die Videodateien liegen auf deinem PC. Kein Konnektor kann eine Datei von deiner Festplatte auf YouTube schieben.
2. vidIQ kann Titel, Beschreibung, Tags und Termin bei einem Video setzen, das schon auf YouTube liegt (fünf Credits je Aufruf). Hochladen kann es nicht.
3. Termine braucht keinen Skill: YouTube Studio hat „Geplant“ eingebaut.

Ablauf, der Arbeit spart: Du ziehst die Dateien privat in YouTube Studio. Claude trägt Titel, Beschreibung, Kapitel, Tags und Termin aus dem YouTube-Paket ein, per Claude in Chrome auf deinem PC oder per vidIQ.
