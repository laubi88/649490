import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

import type { Ansicht } from '../types'
import { THEMEN, WOERTERBUCH } from './inhalte'

const PANE = 'erklaer-mod'
const TITEL = 'Erklärung'

const thema = atom({ plugin: 'erklaer-mod', key: 'thema' } as const, null as string | null)
const ansicht = atom({ plugin: 'erklaer-mod', key: 'ansicht' } as const, 'themen' as Ansicht)

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({
      name: 'erklaeren',
      description: 'Öffnet die Erklärspalte: Umgebung, Branch, Modus, Modell, Aufwand, Symbole, Wörterbuch',
    })
    void $.ui.open({ id: PANE, title: TITEL })

    return next(e)
  })

  on('command.run', { command: 'erklaeren' }, async $ => {
    const opened = await $.ui.open({ id: PANE, title: TITEL, focus: true })
    if (opened.isPlaced) return { text: 'Erklärspalte geöffnet. Ziffer drücken oder Thema anklicken.' }

    return { text: `Erklärspalte wartet: ${opened.reason}` }
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text, Button, Markdown } = $.ui.resolve(e)
    const gewaehlt = await read($, thema)
    const seite = await read($, ansicht)
    const modell = await $.session.model()
    const wurzel = await $.session.root()

    const zeigeThemen = () => void update($, ansicht, () => 'themen')
    const zeigeWoerter = () => void update($, ansicht, () => 'woerterbuch')
    const zurueck = () => void update($, thema, () => null)
    const schliessen = () => void $.ui.close({ id: PANE })

    const kopf = (
      <Box flexDirection="row" gap={1}>
        <Button key="tab-themen" hotkey="t" plain dimColor={seite !== 'themen'} onPress={zeigeThemen}>
          Themen
        </Button>
        <Button key="tab-woerter" hotkey="w" plain dimColor={seite !== 'woerterbuch'} onPress={zeigeWoerter}>
          Wörterbuch
        </Button>
        <Button key="schliessen" role="dismiss" hotkey="x" plain dimColor onPress={schliessen}>
          Schließen
        </Button>
      </Box>
    )

    if (seite === 'woerterbuch') {
      return (
        <Box flexDirection="column" gap={1}>
          {kopf}
          <Text weight="bold">Englisch → Deutsch</Text>
          <Box flexDirection="column">
            {WOERTERBUCH.map(w => (
              <Text key={w.en}>
                <Text color="claude">{w.en}</Text> = <Text weight="bold">{w.de}</Text>
                <Text dimColor> · {w.hinweis}</Text>
              </Text>
            ))}
          </Box>
        </Box>
      )
    }

    const aktiv = THEMEN.find(t => t.id === gewaehlt)
    if (aktiv !== undefined) {
      return (
        <Box flexDirection="column" gap={1}>
          {kopf}
          <Text weight="bold" key="thema-titel">{aktiv.titel}</Text>
          <Markdown text={aktiv.text} />
          <Button key="zurueck" hotkey="z" plain onPress={zurueck}>
            Zurück zur Übersicht
          </Button>
        </Box>
      )
    }

    return (
      <Box flexDirection="column" gap={1}>
        {kopf}
        <Text weight="bold">Was bedeutet was? Thema wählen:</Text>
        <Box flexDirection="column">
          {THEMEN.map(t => (
            <Button
              key={`thema-${t.id}`}
              hotkey={t.taste}
              plain
              onPress={() => void update($, thema, () => t.id)}
            >
              {t.titel}
            </Button>
          ))}
        </Box>
        <Box flexDirection="column">
          <Text dimColor>Jetzt aktiv</Text>
          <Text key="aktuell-modell">
            Modell: <Text weight="bold">{modell}</Text>
          </Text>
          <Text key="aktuell-wurzel" wrap="truncate-start">
            Projekt: <Text weight="bold">{wurzel}</Text>
          </Text>
        </Box>
        <Text dimColor>Ziffer drücken, wenn die Spalte den Fokus hat (ctrl+x tab). /erklaeren öffnet sie neu.</Text>
      </Box>
    )
  })
}
