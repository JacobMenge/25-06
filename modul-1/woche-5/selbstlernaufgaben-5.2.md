# Selbstlernaufgaben - PowerShell Skripte erstellen (Grundlagen)

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.

---

## 1. Grundlagenaufgabe - PowerShell Skript-Glossar

**Deine Aufgabe:**

Erstelle ein persönliches Glossar mit **6 bis 8 Begriffen** aus dem heutigen PowerShell-Skript-Unterricht – zum Beispiel: Skript, Execution Policy, Write-Host, .ps1-Datei, Automatisierung, RemoteSigned, Notepad, Kommentare (#).

Erkläre jeden Begriff in **deinen eigenen Worten** (1–2 Sätze pro Begriff) und ordne ihn einem passenden Themenbereich zu (**Skript-Grundlagen**, **Sicherheit** oder **Ausgabe/Formatierung**).

**Zusätzlich:** Erkläre den Unterschied zwischen einem einzelnen PowerShell-Befehl und einem PowerShell-Skript.

**Formatvorschläge:**
- Liste, Tabelle oder kurze Textabschnitte
- PDF, Word-Dokument, Textdatei oder Screenshot

---

## 2. Grundlagenaufgabe - Mein erstes PowerShell-Skript

**Deine Aufgabe:**

Erstelle dein erstes funktionsfähiges PowerShell-Skript und dokumentiere jeden Schritt des Erstellungsprozesses.

**Kurze Wiederholung:** Ein PowerShell-Skript ist eine Textdatei mit der Endung `.ps1`, die mehrere PowerShell-Befehle enthält. Diese werden automatisch nacheinander ausgeführt, wodurch wiederkehrende Aufgaben automatisiert werden können.

**Schritt-für-Schritt-Anleitung:**

1. **Execution Policy überprüfen und setzen:**
   - Öffne PowerShell
   - Führe `Get-ExecutionPolicy` aus, um die aktuelle Einstellung zu sehen
   - Falls nötig, setze mit `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
   - **Erklärung:** Die Execution Policy ist eine Sicherheitseinstellung, die verhindert, dass unbekannte Skripte ausgeführt werden
   - Mache einen Screenshot der PowerShell mit den Befehlen

2. **Skript-Datei erstellen:**
   - Öffne Notepad (Windows-Taste → "Notepad" → Enter)
   - Schreibe folgendes Skript:
   ```powershell
   # Mein erstes PowerShell-Skript
   Write-Host "=== Willkommen zu meinem ersten Skript! ==="
   Write-Host "Zeige aktuelles Datum:"
   Get-Date
   Write-Host "Zeige aktuellen Ordner:"
   Get-Location
   Write-Host "Erstelle einen Test-Ordner..."
   New-Item -Name "Mein-Erstes-Skript" -ItemType Directory
   Write-Host "Skript erfolgreich beendet!"
   ```
   - **Wichtig:** Speichere die Datei mit der Endung `.ps1` (nicht `.txt`!)
   - Speichere als `mein-erstes-skript.ps1` auf dem Desktop

3. **Skript ausführen:**
   - Navigiere in PowerShell zum Desktop: `cd ~/Desktop`
   - Führe das Skript aus: `.\mein-erstes-skript.ps1`
   - **Erklärung:** Der Punkt und Backslash `.\` bedeutet "in diesem Ordner"
   - **Falls Fehler auftreten:** Überprüfe, ob die Execution Policy gesetzt ist und du im richtigen Ordner bist
   - Mache einen Screenshot der Ausgabe

4. **Kommentrieren**
  - Schreibe mit # Kommentare in das Skript. Erkläre in den Kommentaren mit wenigen Worten was die jeweiligen Zeilen in dem Skript machen.
5. **Ergebnis überprüfen:**
   - Überprüfe, ob der Test-Ordner erstellt wurde
   - Mache einen Screenshot des erstellten Ordners im Datei-Explorer


**Dokumentiere:**
- Screenshots aller wichtigen Schritte
- Was ist beim ersten Ausführen passiert?
- Wurden das Datum und der Ordner korrekt angezeigt?
- Wurde der Ordner "Mein-Erstes-Skript" erfolgreich erstellt?

**Formatvorschläge:**
- Word-Dokument mit Screenshots und Erklärungen
- PDF mit chronologischer Dokumentation

---

## 3. Weiterführende Selbstlernaufgabe - Arbeitsplatz-Setup Skript

**Deine Aufgabe:**

Entwickle ein praktisches Skript, das einen persönlichen digitalen Arbeitsplatz einrichtet.

**Kurze Erinnerung:** `Write-Host` gibt Text in der PowerShell aus, während `New-Item -ItemType Directory` einen neuen Ordner erstellt. Neu in dieser Aufgabe lernst du, wie man mit `-ForegroundColor` die Textfarbe ändern kann (Green, Yellow, Blue, Red, etc.).

**Dein Skript "arbeitsplatz-setup.ps1" soll:**

1. **Eine bunte Begrüßung ausgeben:**
   - Titel in blauer Farbe: "=== Arbeitsplatz-Setup gestartet ==="
   - Dein Name in grüner Farbe
   - Aktuelles Datum und Uhrzeit

2. **Zum Desktop navigieren:**
   - `Set-Location ~/Desktop` oder verwende den vollständigen Pfad: `Set-Location "$env:USERPROFILE\Desktop"`
   - **Tipp:** `Set-Location` ist das gleiche wie `cd` – beide wechseln den Ordner
   - **Falls der Desktop-Pfad nicht funktioniert:** Nutze einen anderen Ordner, z.B. `Set-Location C:\Temp`

3. **Ordnerstruktur erstellen:**
   - Hauptordner: "Mein-Arbeitsplatz-[DATUM]" (mit heutigem Datum)
   - In diesen Ordner wechseln
   - 4 Unterordner erstellen: "Projekte", "Notizen", "Dokumente", "Archiv"
   - **Hinweis:** Falls ein Ordner bereits existiert, gibt PowerShell eine Warnung aus, aber das Skript läuft weiter

4. **Erfolgsmeldung ausgeben:**
   - "Arbeitsplatz erfolgreich eingerichtet!" in gelber Farbe
   - Anzeige des vollständigen Pfads des erstellten Arbeitsplatzes

5. **Kommentare hinzufügen:**
   - Jeder wichtige Abschnitt soll mit # Kommentaren erklärt werden
   - **Erklärung:** Kommentare werden vom Computer ignoriert, helfen aber Menschen beim Verstehen des Codes

**Zusatzaufgabe:** Erweitere dein Skript um eine Info-Datei:
- Erstelle eine Datei "arbeitsplatz-info.txt" im Hauptordner
- Inhalt: "Arbeitsplatz erstellt am [DATUM] um [UHRZEIT]"
- Verwende `"Text hier" | Out-File "dateiname.txt"`

**Dokumentiere:**
- Den vollständigen Skript-Code
- Screenshot der Skript-Ausführung
- Übersicht der erstellten Ordnerstruktur
- Inhalt der Info-Datei

**Formatvorschläge:**
- PDF mit Code und Screenshots
- Word-Dokument mit strukturierter Dokumentation

---

## 4. Vorbereitungsaufgabe - Erste Schritte mit Variablen (Ausblick)

**Deine Aufgabe:**

**Hinweis:** Das Thema Variablen werden wir ausführlich **morgen** behandeln. Diese Aufgabe ist eine erste Vorbereitung und ein Ausblick. Du kannst gerne schon in die Folien von morgen schauen, um einen Vorgeschmack zu bekommen!

Experimentiere mit Variablen und beobachte, was passiert.

**Was sind Variablen? (Kurze Vorab-Erklärung):**
Variablen sind wie beschriftete Boxen, in denen du Daten speichern kannst. In PowerShell beginnen sie immer mit einem `$`-Zeichen.

**Teil A: Einfache Experimente**
Probiere diese Befehle einzeln in PowerShell aus und mache Screenshots:

1. `$name = "Dein Name hier"`
2. `Write-Host "Hallo $name!"`
3. `$zahl = 10`
4. `Write-Host "Die Zahl ist: $zahl"`
5. `$ordner = "Test-Ordner"`
6. `mkdir $ordner`

**Teil B: Beobachtungen dokumentieren**
Beantworte folgende Fragen:
- Was passiert, wenn du `$name` eintippst und Enter drückst?
- Wie wird der Text in `Write-Host "Hallo $name!"` ausgegeben?
- Welchen Namen hat der erstellte Ordner?
- Was denkst du: Wozu könnten Variablen nützlich sein?

**Teil C: Erstes Variablen-Skript (optional)**
Wenn du magst, erstelle ein kleines Skript `mein-name.ps1`:
```powershell
# Mein erstes Skript mit Variablen
$meinName = "Hier dein Name"
$lieblingsFarbe = "Blue"
Write-Host "Hallo, ich bin $meinName!" -ForegroundColor $lieblingsFarbe
Write-Host "Meine Lieblingsfarbe ist $lieblingsFarbe"
```

**Wichtiger Hinweis:** Falls etwas nicht funktioniert oder verwirrend ist – das ist völlig normal! Morgen werden wir Variablen von Grund auf richtig lernen. Diese Aufgabe soll nur neugierig machen.

**Dokumentiere:**
- Screenshots deiner Experimente
- Antworten auf die Beobachtungsfragen
- Optional: Screenshot deines ersten Variablen-Skripts
- Eine kurze Einschätzung: Was findest du an Variablen interessant?

**Formatvorschläge:**
- Kurzes PDF mit Experimenten und Beobachtungen
- Word-Dokument mit Screenshots und Antworten

---

## Abgabehinweise

- **Frist:** Sonntag, 23:59 Uhr
- **Abgabe:** direkt über den Google Classroom zur entsprechenden Aufgabe
- **Dateiformate:** PDF, DOCX, ODT, PNG, JPG, Textdatei oder .ps1-Dateien
- **Wichtig:** Bei Skript-Aufgaben sowohl den Code als auch Screenshots der Ausführung zeigen!

**Sicherheitshinweis:** 
- Führe nur Skripte aus, die du selbst geschrieben oder verstanden hast
- Bei Problemen mit der Execution Policy wende dich an den Kurs-Slackchannel

**Ausblick auf morgen:** 
Morgen vertiefen wir das Thema Variablen richtig und lernen, wie man Benutzereingaben abfragt und Skripte interaktiv macht. Die heutige Aufgabe 4 ist nur ein kleiner Vorgeschmack!

**Tipp:** Verwende aussagekräftige Kommentare in deinen Skripten - sie helfen dir selbst, wenn du das Skript später wieder anschaust!

Bei Fragen melde dich gerne im Kurs-Slackchannel.
