export type Ansicht = 'themen' | 'woerterbuch'

/** Ein Verbrauchsfenster, wie $.session.usage() es liefert */
export type Fenster = { kind: string; percentUsed: number; resetsAt?: string }

/** Die Messwerte für das Band über der Eingabe */
export type Verbrauch = {
  kontextProzent: number | null
  fenster: Fenster[]
  kostenUsd: number | null
}

declare module 'claude-code' {
  interface PluginState {
    'erklaer-mod': {
      /** Kennung des gewählten Themas, null = Übersicht */
      thema: string | null
      /** Welche Seite der Spalte gezeigt wird */
      ansicht: Ansicht
      /** Letzte Messung für das Band, null = noch keine */
      verbrauch: Verbrauch | null
      /** Band über der Eingabe ausgeblendet */
      bandAus: boolean
    }
  }
}
