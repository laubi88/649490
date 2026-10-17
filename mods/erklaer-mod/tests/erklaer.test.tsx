import { test, expect } from 'claude-code/testing'

const PANE = {
  component: 'Pane',
  requestId: 'erklaer-mod',
  props: {
    title: 'Erklärung',
    isFocused: false,
    bodyColumns: 80,
    placement: 'dock',
    scroll: { offset: 0, bodyRows: 40 },
    view: {},
  },
} as const

test('Übersicht, Thema, Zurück und Wörterbuch auf Terminal und Desktop', async ($, on) => {
  on('session.model', () => ({ value: 'claude-fable-5-1' }))
  on('session.root', () => ({ value: '/home/user/649490' }))

  for (const surface of ['terminal', 'desktop'] as const) {
    const ui = await $.ui.mount({ plugin: 'erklaer-mod', surface, ...PANE })

    expect(await ui.find({ type: 'Button', key: 'thema-umgebung' })).toBeDefined()
    expect(await ui.find({ type: 'Button', key: 'thema-aufwand' })).toBeDefined()

    await ui.press({ key: 'thema-umgebung' })
    expect(await ui.find({ type: 'Text', text: /Umgebung: Default/ })).toBeDefined()
    expect(await ui.find({ type: 'Markdown', text: /Cloud-Umgebung/ })).toBeDefined()

    await ui.press({ key: 'zurueck' })
    expect(await ui.find({ type: 'Button', key: 'thema-modell' })).toBeDefined()

    await ui.press({ key: 'tab-woerter' })
    expect(await ui.find({ type: 'Text', text: /Berechtigungsmodus/ })).toBeDefined()

    await ui.press({ key: 'tab-themen' })
    expect(await ui.find({ type: 'Button', key: 'thema-branch' })).toBeDefined()

    await ui.unmount()
  }
})

const BAND = {
  component: 'AbovePrompt',
  props: {
    hasSurvey: false,
    isWorking: false,
    maxRows: 6,
    bodyColumns: 120,
    scroll: { offset: 0, bodyRows: 6 },
    view: {},
  },
} as const

test('Verbrauchsband zeigt Gedächtnis, 5-Stunden- und Wochenlimit', async ($, on) => {
  on('session.model', () => ({ value: 'claude-fable-5-1' }))
  on('session.root', () => ({ value: '/home/user/649490' }))
  on('clock.now', () => ({ value: Date.parse('2026-10-17T12:00:00Z') }))
  on('session.measure', (_$, e) => ({ changed: e.changed }))

  await $.session.measure({
    context: { tokens: 42000, window: 200000, percent: 21 },
    rateLimits: [
      { kind: 'seven_day', percentUsed: 12.5, resetsAt: '2026-10-20T16:00:00Z' },
      { kind: 'five_hour', percentUsed: 73, resetsAt: '2026-10-17T14:15:00Z' },
    ],
    changed: ['context', 'rateLimits'],
  })

  for (const surface of ['terminal', 'desktop'] as const) {
    const ui = await $.ui.mount({ plugin: 'erklaer-mod', surface, ...BAND })
    const alle = (await ui.findAll({ type: 'Text' })).map(t => t.text).join('\n')
    expect(alle).toMatch(/Gedächtnis[\s\S]*21 %/)
    expect(alle).toMatch(/5 Std[\s\S]*73 %[\s\S]*in 2 Std 15 Min/)
    expect(alle).toMatch(/Woche[\s\S]*13 %[\s\S]*in 3 Tg 4 Std/)
    expect(await ui.find({ type: 'Button', key: 'band-aus' })).toBeDefined()
    await ui.unmount()
  }
})
