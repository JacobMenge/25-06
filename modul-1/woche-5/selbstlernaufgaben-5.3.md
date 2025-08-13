# Selbstlernaufgaben - PowerShell Variablen (Grundlagen)

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.

---

## 1. Grundlagenaufgabe - Variablen verstehen (Das Boxen-Konzept)

**Deine Aufgabe:**

Lerne das Konzept von Variablen durch praktisches Experimentieren und erkläre es in deinen eigenen Worten.

**Was sind Variablen? (Ausführliche Erklärung)**

Stell dir vor, du hast viele beschriftete Boxen in deinem Zimmer:
- Eine Box mit dem Aufkleber "Name" → darin liegt ein Zettel mit "Anna"
- Eine Box mit dem Aufkleber "Alter" → darin liegt ein Zettel mit "22"
- Eine Box mit dem Aufkleber "Lieblingsfarbe" → darin liegt ein Zettel mit "Blau"

Genau so funktionieren Variablen in PowerShell! Sie sind wie digitale Boxen, in denen du Informationen speichern kannst.

**Wichtige Regeln für PowerShell-Variablen:**
- Jede Variable beginnt mit einem `$`-Zeichen (das ist wie der Aufkleber auf der Box)
- Nach dem `$` kommt der Name der Variable (ohne Leerzeichen)
- Text muss in Anführungszeichen stehen: `"Hallo"`
- Zahlen brauchen keine Anführungszeichen: `25`

**Teil A: Erste Experimente**
Öffne PowerShell und probiere diese Befehle **einzeln** aus. Mache nach jedem Befehl einen Screenshot:

1. `$name = "Max Mustermann"`
   **Erklärung:** Erstelle eine "Box" namens "name" und lege den Text "Max Mustermann" hinein

2. `$name`
   **Erklärung:** Schaue in die Box "name" hinein - PowerShell zeigt dir den Inhalt

3. `Write-Host "Hallo $name!"`
   **Erklärung:** Verwende den Inhalt der Box "name" in einem Text

4. `$alter = 25`
   **Erklärung:** Erstelle eine Box "alter" und lege die Zahl 25 hinein (ohne Anführungszeichen!)

5. `Write-Host "Du bist $alter Jahre alt"`
   **Erklärung:** Verwende den Inhalt der Box "alter" in einem Text

6. `$lieblingsfarbe = "Blue"`
   **Erklärung:** Erstelle eine Box "lieblingsfarbe" mit dem Text "Blue"

7. `Write-Host "Meine Lieblingsfarbe ist $lieblingsfarbe"`
   **Erklärung:** Verwende den Inhalt der Box in einem normalen Text

**Teil B: Beobachtungen dokumentieren**
Beantworte folgende Fragen ausführlich:
- Was passiert, wenn du nur `$name` eingibst? Warum?
- Wie wird die Variable in `Write-Host "Hallo $name!"` verwendet?
- Was ist der Unterschied zwischen `$alter = 25` (Zahl) und `$name = "Max"` (Text)?
- Erkläre in deinen eigenen Worten: Was ist eine Variable und wozu ist sie gut?
- Was würde passieren, wenn du `$name = Max` (ohne Anführungszeichen) schreibst?

**Teil C: Eigenes Experiment**
Erstelle drei eigene Variablen mit deinen echten Daten:
```powershell
$meinName = "Hier dein echter Name"
$meinAlter = 20
$meineLieblingsfarbe = "Red"
```

Gib dann alle drei Informationen in einem schönen Text aus:
```powershell
Write-Host "Ich heiße $meinName, bin $meinAlter Jahre alt und mag die Farbe $meineLieblingsfarbe"
```

**Formatvorschläge:**
- PDF oder DOCX mit den Antworten
- Word-Dokument mit Experimenten und Erklärungen

---

## 2. Grundlagenaufgabe - Variablen im Skript verwenden

**Deine Aufgabe:**

Erstelle dein erstes Skript, das Variablen verwendet, um flexibler und wiederverwendbarer zu werden.

**Wiederholung: Was sind Skripte?**
Ein Skript ist eine Datei mit der Endung `.ps1`, die mehrere PowerShell-Befehle enthält. Anstatt jeden Befehl einzeln zu tippen, schreibst du alle Befehle in eine Datei und lässt sie automatisch nacheinander ausführen.

**Warum Variablen in Skripten verwenden?**
Ohne Variablen müsstest du bei jeder Änderung das ganze Skript durchsuchen und überall den Text ändern. Mit Variablen änderst du nur eine Zeile am Anfang, und alles andere passt sich automatisch an!

**Beispiel ohne Variablen (umständlich):**
```powershell
Write-Host "Hallo Max!"
Write-Host "Max ist 25 Jahre alt"
Write-Host "Max wohnt in Berlin"
Write-Host "Tschüss Max!"
```
→ Problem: Um den Namen zu ändern, musst du 4 Zeilen bearbeiten!

**Beispiel mit Variablen (clever):**
```powershell
$name = "Max"
Write-Host "Hallo $name!"
Write-Host "$name ist 25 Jahre alt"
Write-Host "$name wohnt in Berlin"
Write-Host "Tschüss $name!"
```
→ Vorteil: Um den Namen zu ändern, bearbeitest du nur 1 Zeile!

**Erstelle ein Skript "meine-daten.ps1":**

```powershell
# Mein Daten-Skript mit Variablen
Write-Host "=== Meine persönlichen Daten ===" -ForegroundColor Blue

# Variablen definieren (hier änderst du deine Daten)
$meinName = "Hier dein Name eintragen"
$meinAlter = 20
$meinWohnort = "Deine Stadt"
$meinLieblingsessen = "Pizza"
$meinHobby = "Lesen"

# Daten ausgeben (hier musst du nichts ändern!)
Write-Host "Name: $meinName" -ForegroundColor Green
Write-Host "Alter: $meinAlter Jahre" -ForegroundColor Yellow
Write-Host "Wohnort: $meinWohnort" -ForegroundColor Cyan
Write-Host "Lieblingsessen: $meinLieblingsessen" -ForegroundColor Magenta
Write-Host "Lieblingshobby: $meinHobby" -ForegroundColor White

Write-Host "=== Daten-Ausgabe beendet ===" -ForegroundColor Blue
```

**Zusatzaufgabe:**
Erweitere das Skript um einen Ordner, der nach dir benannt ist:
```powershell
# Ordner mit meinem Namen erstellen
New-Item -Name "Profil-$meinName" -ItemType Directory
Write-Host "Ordner 'Profil-$meinName' wurde erstellt!" -ForegroundColor Green
```

**Erklärung wichtiger Punkte:**
- **Variablen-Bereich:** Alle Variablen stehen am Anfang zusammen - so findest du sie leicht
- **Wiederverwendung:** Die Variable `$meinName` wird mehrmals verwendet
- **Flexibilität:** Um alles zu ändern, bearbeitest du nur den Variablen-Bereich
- **Ordner-Namen:** `"Profil-$meinName"` kombiniert festen Text mit dem Variablen-Inhalt

**Teste dein Skript:**
1. Ändere die Variablen mit deinen echten Daten
2. Führe das Skript aus
3. Ändere nur den Namen in der Variable
4. Führe das Skript erneut aus - siehst du, wie sich alles automatisch anpasst?

**Dokumentiere:**
- Screenshot des vollständigen Skript-Codes
- Screenshot der ersten Ausführung mit deinen Daten
- Screenshot der zweiten Ausführung mit geändertem Namen
- Screenshot des erstellten Ordners
- Erkläre: Warum sind Variablen nützlicher als feste Texte im Skript?

**Formatvorschläge:**
- PDF mit Code und Ausführungs-Screenshots
- Word-Dokument mit strukturierter Dokumentation

---

## Abgabehinweise

- **Frist:** Sonntag, 23:59 Uhr
- **Abgabe:** direkt über den Google Classroom zur entsprechenden Aufgabe
- **Dateiformate:** PDF, DOCX, ODT, PNG, JPG, Textdatei oder .ps1-Dateien

**Wenn etwas nicht funktioniert:**
1. Überprüfe das `$`-Zeichen vor dem Variablennamen
2. Überprüfe die Anführungszeichen bei Text
3. Schaue dir die Fehlermeldung genau an
4. Teste die Variable einzeln: einfach `$variablenname` eingeben

Bei Fragen melde dich gerne im Kurs-Slackchannel.
