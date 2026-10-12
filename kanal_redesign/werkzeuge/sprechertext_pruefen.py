"""Prüft Sprechertexte (alles nach 'TEXT:' bis zu zwei Leerzeilen in Folge oder zur nächsten 'DATEI:') gegen die Kanalregeln.
Einzelne Leerzeilen zwischen den Sätzen sind erlaubt und beenden den Block nicht.
Aufruf: python sprechertext_pruefen.py DATEI [DATEI ...]   -> Exitcode 1 bei Verstößen."""
import re, sys
GESPERRT = ["stoa", "stoiker", "stoisch", "punkt", "stress", "job", "meeting", "team", "check",
            "coach", "boss", "feedback", "okay", "deadline", "update", "sorry", "cool"]
ABK = re.compile(r"\b(z\s?\.\s?b|usw|bzw|etc|ca|d\s?\.\s?h|u\s?\.\s?a|evtl|ggf|inkl|vgl|nr|dr|bspw)\b\.?", re.I)
fehler = 0
for pfad in sys.argv[1:]:
    zeilen = open(pfad, encoding="utf-8").read().splitlines()
    im_text, datei, saetze, woerter, leer = False, "", 0, 0, 0
    for nr, z in enumerate(zeilen, 1):
        if z.startswith("DATEI:"):
            datei, im_text = z[6:].strip(), False; continue
        if z.strip() == "TEXT:":
            im_text, leer = True, 0; continue
        if im_text and not z.strip():
            leer += 1
            if leer >= 2: im_text = False
            continue
        leer = 0
        if not im_text:
            continue
        s = z.strip(); w = s.split(); saetze += 1; woerter += len(w)
        probleme = []
        if len(w) > 12: probleme.append(f"{len(w)} Wörter")
        if re.search(r"\d", s): probleme.append("Ziffer")
        if re.search(r"[-–—]", s): probleme.append("Bindestrich")
        if ABK.search(s): probleme.append("Abkürzung")
        if len(re.findall(r"[.!?](?=\s|$)", s)) > 1: probleme.append("mehr als ein Satz")
        if not re.search(r"[.!?]$", s): probleme.append("kein Satzende")
        klein = s.lower()
        erlaubt_kanal = datei.endswith(("Outro",)) or datei == "Kanaltrailer"
        for g in GESPERRT:
            muster = r"\bstoa\b" if g == "stoa" else g
            for m in re.finditer(muster, klein):
                if g == "stoisch" and erlaubt_kanal and s == "Stoische.": continue
                probleme.append(f"gesperrt: {g}")
        if probleme:
            fehler += 1
            print(f"{pfad.split('/')[-2] if '/' in pfad else ''}/{pfad.split('/')[-1]}:{nr} [{datei}] {', '.join(sorted(set(probleme)))}: {s}")
    print(f"OK geprüft: {pfad.split('/')[-1]} ({saetze} Sätze, {woerter} Wörter, rund {woerter/125:.1f} min bei 125 Wörtern je Minute)")
print("Verstöße:", fehler)
sys.exit(1 if fehler else 0)
