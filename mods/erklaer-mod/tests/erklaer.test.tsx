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
