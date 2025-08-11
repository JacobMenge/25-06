# Selbstlernaufgaben - Einführung in PowerShell

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.

---

## 1. Grundlagenaufgabe - PowerShell Navigation Glossar

**Deine Aufgabe:**

Erstelle ein persönliches Glossar mit **8 bis 10 Begriffen** aus dem heutigen PowerShell-Unterricht – zum Beispiel: Cmdlet, Pipeline, Parameter, Get-Command, Get-Help, pwd, cd, ls, mkdir .. .

Erkläre jeden Begriff in **deinen eigenen Worten** (1–2 Sätze pro Begriff) und ordne ihn einem passenden Themenbereich zu (**Navigation**, **Hilfe-System** oder **Pipeline/Objekte**).

**Zusätzlich:** Gib für jeden Navigationsbefehl (pwd, cd, ls, mkdir) sowohl die Kurzform als auch die vollständige PowerShell-Form an.

**Beispiel:**
- **pwd (Navigation):** Zeigt mir an, in welchem Ordner ich mich gerade befinde. Vollständige Form: Get-Location
- **Pipeline (Pipeline/Objekte):** Das "|"-Symbol verbindet mehrere Befehle miteinander, sodass das Ergebnis des ersten Befehls als Eingabe für den zweiten Befehl verwendet wird.

**Formatvorschläge:**
- Liste, Tabelle oder kurze Textabschnitte
- PDF, Word-Dokument, Textdatei oder Screenshot

---

## 2. Grundlagenaufgabe - Erste PowerShell Navigation

**Deine Aufgabe:**

Öffne PowerShell und führe eine geführte Navigation durch dein System durch. Dokumentiere dabei jeden Schritt mit Screenshots.

**Schritt-für-Schritt-Anleitung:**

1. **PowerShell öffnen:**
   - Nutze die Methode 2 aus dem Unterricht (Windows-Taste → "PowerShell" tippen)
   - Mache einen Screenshot des geöffneten PowerShell-Fensters

2. **Grundlegende Navigation:**
   - Verwende `pwd` um herauszufinden, wo du dich befindest
   - Nutze `ls` um zu sehen, was in deinem aktuellen Ordner ist
   - Wechsle mit `cd Desktop` auf den Desktop
   - Verwende erneut `pwd` um zu bestätigen, dass du auf dem Desktop bist

3. **Ordner erstellen und navigieren:**
   - Erstelle einen Ordner namens "PowerShell-Test" mit `mkdir PowerShell-Test`
   - Gehe in diesen Ordner mit `cd PowerShell-Test`
   - Erstelle drei Unterordner: "Dokumente", "Bilder", "Scripts"
   - Nutze `ls` um deine erstellten Ordner anzuzeigen

4. **Aufräumen:**
   - Gehe mit `cd ..` zurück zum Desktop
   - Verwende `cls` um den Bildschirm aufzuräumen

**Dokumentiere:**
- Screenshot nach jedem wichtigen Schritt
- Kurze Erklärung: Was hast du bei jedem Befehl erwartet und was ist passiert?

**Formatvorschläge:**
- Word-Dokument mit eingebetteten Screenshots
- PDF mit beschrifteten Screenshots

---

## 3. Weiterführende Selbstlernaufgabe - Das Hilfe-System meistern

**Deine Aufgabe:**

Nutze das PowerShell Hilfe-System um eigenständig neue Befehle zu entdecken und zu verstehen.

**Teil A: Befehle finden**
1. Verwende `Get-Command *location*` um alle Befehle zu finden, die mit "Location" zu tun haben
2. Nutze `Get-Command Get-*` um alle "Get"-Befehle anzuzeigen
3. Finde mit `Get-Command *file*` alle Befehle, die mit Dateien arbeiten

**Teil B: Befehle verstehen**
1. Lasse dir mit `Get-Help Get-ChildItem -Examples` Beispiele für Get-ChildItem zeigen
2. Erkunde mit `Get-Help Get-Location` was der Get-Location Befehl macht
3. Probiere Tab-Vervollständigung: Tippe "Get-Loc" und drücke Tab mehrmals

**Teil C: Objekte entdecken**
1. Führe `Get-Date | Get-Member` aus um zu sehen, was alles in einem Datum-Objekt steckt
2. Teste `Get-ChildItem | Get-Member` um die Eigenschaften von Datei-Objekten zu erkunden
3. Experimentiere mit `Get-Process | Get-Member` (zeigt laufende Programme)

**Dokumentiere für jeden Teil:**
- Screenshots der ausgeführten Befehle und deren Ausgaben
- 2-3 interessante Entdeckungen pro Teil
- Eine Erkenntnis: "Das war neu für mich" oder "Das fand ich überraschend"

**Zusatzfrage:** Finde heraus, was der Parameter `-Recurse` bei `Get-ChildItem` macht. Nutze dafür das Hilfe-System!

**Formatvorschläge:**
- PDF mit Screenshots und Erklärungen
- Word-Dokument mit strukturierter Dokumentation

---

## 4. Vertiefende Selbstlernaufgabe - Pipeline in der Praxis

**Deine Aufgabe:**

Erstelle praktische Pipeline-Kombinationen um Dateien auf deinem System zu analysieren und zu organisieren.

**Aufgabe 1: Große Dateien finden**
- Finde alle Dateien in deinem Benutzerordner, die größer als 10MB sind
- Verwende: `Get-ChildItem -Recurse | Where-Object Length -gt 10MB`
- Sortiere das Ergebnis nach Größe: `| Sort-Object Length -Descending`

**Aufgabe 2: Dateitypen analysieren**
- Analysiere alle `.txt` Dateien auf dem Desktop
- Verwende: `Get-ChildItem *.txt | Select-Object Name, Length, LastWriteTime`
- Sortiere nach dem letzten Änderungsdatum

**Aufgabe 3: Ordnerstruktur verstehen**
- Zeige nur Ordner (keine Dateien) in deinem Benutzerverzeichnis an
- Verwende: `Get-ChildItem | Where-Object PSIsContainer -eq $true`
- Alternativ: `Get-ChildItem -Directory`

**Aufgabe 4: Eigene Pipeline entwickeln**
- Entwickle eine eigene Pipeline-Kombination für eine praktische Aufgabe
- Beispiele: Finde alle PowerShell-Skripte (.ps1), oder alle Bilder (.jpg, .png), oder leere Ordner

**Für jede Aufgabe dokumentiere:**
- Den verwendeten Befehl
- Screenshot des Ergebnisses  
- Erklärung: Was macht jeder Teil der Pipeline?
- Praktischer Nutzen: Wofür könnte man das verwenden?

**Bonus-Challenge:** Kombiniere mindestens 4 Befehle in einer Pipeline für eine komplexe Analyse!

**Formatvorschläge:**
- Strukturiertes PDF mit allen vier Aufgaben
- Word-Dokument mit Code-Blöcken und Screenshots

---

## Abgabehinweise

- **Frist:** Sonntag, 23:59 Uhr
- **Abgabe:** direkt über den Google Classroom zur entsprechenden Aufgabe
- **Dateiformate:** PDF, DOCX, ODT, PNG, JPG, Textdatei oder Screenshot
- **Wichtig:** Bei PowerShell-Aufgaben immer Screenshots der Befehle UND deren Ausgaben zeigen!


Bei Fragen melde dich gerne im Kurs-Slackchannel.
