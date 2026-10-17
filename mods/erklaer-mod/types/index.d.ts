export type Ansicht = 'themen' | 'woerterbuch'

declare module 'claude-code' {
  interface PluginState {
    'erklaer-mod': {
      /** Kennung des gewählten Themas, null = Übersicht */
      thema: string | null
      /** Welche Seite der Spalte gezeigt wird */
      ansicht: Ansicht
    }
  }
}
