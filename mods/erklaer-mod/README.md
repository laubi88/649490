# Erklär-Mod für Claude Code (Stoische Karriere)

Ein Mod (Plugin) für Claude Code, der eine Spalte „Erklärung“ öffnet. Darin stehen auf Deutsch:

- neun Themen zur Oberfläche: Umgebung (Default, Claude Home, video-automation), Repository, Branch, Berechtigungsmodus „Auto“, Modell „Fable 5.1“, Aufwand „Hoch“, die Symbole oben rechts, die Eingabezeile, Schrägstrich-Befehle
- ein Wörterbuch Englisch → Deutsch mit dreißig Begriffen
- die gerade aktiven Werte (Modell, Projektordner)
- ein **Verbrauchsband über der Eingabe**: Gedächtnis (Kontextfenster), Fünf-Stunden-Limit, Wochenlimit, jeweils als Balken mit Prozent und Zeit bis zum Zurücksetzen, dazu die Kosten der Sitzung, wenn Claude Code sie kennt. Grün unter siebzig Prozent, gelb ab siebzig, rot ab neunzig. Es aktualisiert sich nach jedem Zug und wenn ein Limit sich um einen ganzen Punkt bewegt.

Quellen der Texte: offizielle Doku unter code.claude.com/docs (Stand 17.10.2026). Was die Doku nicht hergibt (Mikrofon, Maskottchen, Zuordnung des Globus), ist im Text so markiert.

## Was der Mod kann und was nicht

- Kann: eine Spalte in der Oberfläche öffnen, Themen per Klick oder Taste zeigen, sich mit `/erklaeren` öffnen und mit „Schließen“ schließen.
- Kann nicht: einen eigenen Schalter in die Titelleiste neben Terminal und Globus setzen. Die Titelleiste gehört der App, Mods zeichnen nur in Spalten (Panes), Bändern über der Eingabe, Statuszeile und Hinweisen.
- Der Mod läuft in der Desktop-App und im Terminal. In einer Cloud-Sitzung werden Desktop-Plugins laut Doku nicht geladen; dort muss der Mod aus dem Repo-Ordner geladen werden.

## Bedienung

| Aktion | Wie |
|---|---|
| Spalte öffnen | `/erklaeren` eingeben, oder sie öffnet sich beim Start der Sitzung von selbst |
| Thema wählen | anklicken, oder Ziffer 1 bis 9 drücken, wenn die Spalte den Fokus hat (Strg+x, dann Tab) |
| Wörterbuch | „Wörterbuch“ anklicken oder Taste w |
| zurück zur Übersicht | „Zurück“ oder Taste z |
| schließen | „Schließen“, Taste x, oder die Schließmarke der Spalte |
| Verbrauchsband verstecken | „ausblenden“ im Band |
| Verbrauchsband zurückholen | `/verbrauch` |

## Einrichten auf dem Windows-PC

Claude Code 2.1.302 oder neuer. Im Repo-Ordner starten:

```powershell
claude --plugin-dir .\mods\erklaer-mod
```

Oder dauerhaft, ohne Startparameter: in `.claude\settings.json` des Repos unter `plugins` den Ordner eintragen, so wie die Doku es für lokale Plugins beschreibt (code.claude.com/docs/en/plugins).

Prüfen:

```powershell
claude plugin validate .\mods\erklaer-mod
claude plugin test .\mods\erklaer-mod
```

Beim ersten Laden fragt Claude Code auf Englisch „Enable hot reloading for this session?“. Das heißt: „Soll der Mod sofort in dieser Sitzung geladen und bei jeder Änderung neu geladen werden?“ Antwort „Enable for this session“ = ja.

## Texte ändern

Alle Texte stehen in `hooks/inhalte.ts`. Logik in `hooks/register.tsx`, das Band in `hooks/verbrauch.tsx`. Nach einer Änderung `claude plugin validate` und `claude plugin test` laufen lassen.
