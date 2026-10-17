// Band über der Eingabe: Kontextfenster, Fünf-Stunden-Limit, Wochenlimit.
import type { EngineInterface } from 'claude-code'

import type { Fenster, Verbrauch } from '../types'

export const BREITE = 10

export function balken(prozent: number): string {
  const p = Math.max(0, Math.min(100, prozent))
  const voll = Math.round((p / 100) * BREITE)

  return '█'.repeat(voll) + '░'.repeat(BREITE - voll)
}

export function farbe(prozent: number): 'success' | 'warning' | 'error' {
  if (prozent >= 90) return 'error'
  if (prozent >= 70) return 'warning'

  return 'success'
}

export function prozentText(prozent: number): string {
  return `${Math.round(prozent)} %`
}

/** „in 2 Std 15 Min“, „in 3 Tg 4 Std“, „jetzt“ */
export function restzeit(resetsAt: string | undefined, jetztMs: number): string {
  if (resetsAt === undefined) return ''
  const ziel = Date.parse(resetsAt)
  if (Number.isNaN(ziel)) return ''
  const min = Math.round((ziel - jetztMs) / 60000)
  if (min <= 0) return 'jetzt'
  const tage = Math.floor(min / 1440)
  const std = Math.floor((min % 1440) / 60)
  const rest = min % 60
  if (tage > 0) return `in ${tage} Tg ${std} Std`
  if (std > 0) return `in ${std} Std ${rest} Min`

  return `in ${rest} Min`
}

export function name(kind: string): string {
  if (kind === 'five_hour') return '5 Std'
  if (kind === 'seven_day') return 'Woche'
  if (kind === 'spend_limit') return 'Budget'

  return kind
}

export function fensterSortiert(fenster: readonly Fenster[]): Fenster[] {
  const rang = (k: string) => (k === 'five_hour' ? 0 : k === 'seven_day' ? 1 : 2)

  return [...fenster].sort((a, b) => rang(a.kind) - rang(b.kind))
}

export function messen(input: {
  context: { percent?: number }
  rateLimits: readonly Fenster[]
  cost?: { usd: number }
}): Verbrauch {
  return {
    kontextProzent: input.context.percent ?? null,
    fenster: fensterSortiert(input.rateLimits).map(f => ({
      kind: f.kind,
      percentUsed: f.percentUsed,
      ...(f.resetsAt === undefined ? {} : { resetsAt: f.resetsAt }),
    })),
    kostenUsd: input.cost?.usd ?? null,
  }
}

/** Zeichnet das Band; `t` ist die Elementtabelle der Oberfläche. */
export function zeichneBand(
  t: { Box: any; Text: any; Button: any },
  v: Verbrauch,
  jetztMs: number,
  ausblenden: () => void,
) {
  const { Box, Text, Button } = t
  const teile: unknown[] = []

  if (v.kontextProzent !== null) {
    teile.push(
      <Text key="kontext">
        <Text dimColor>Gedächtnis </Text>
        <Text color={farbe(v.kontextProzent)}>{balken(v.kontextProzent)}</Text>
        <Text> {prozentText(v.kontextProzent)}</Text>
      </Text>,
    )
  }
  for (const f of v.fenster) {
    const rest = restzeit(f.resetsAt, jetztMs)
    teile.push(
      <Text key={`fenster-${f.kind}`}>
        <Text dimColor>{name(f.kind)} </Text>
        <Text color={farbe(f.percentUsed)}>{balken(f.percentUsed)}</Text>
        <Text> {prozentText(f.percentUsed)}</Text>
        {rest !== '' && <Text dimColor> · neu {rest}</Text>}
      </Text>,
    )
  }
  if (v.kostenUsd !== null) {
    teile.push(
      <Text key="kosten" dimColor>
        {v.kostenUsd.toFixed(2)} $
      </Text>,
    )
  }

  return (
    <Box flexDirection="row" flexWrap="wrap" gap={2}>
      {teile}
      <Button key="band-aus" plain dimColor onPress={ausblenden}>
        ausblenden
      </Button>
    </Box>
  )
}

export async function lesen($: EngineInterface): Promise<Verbrauch> {
  return messen(await $.session.usage())
}
