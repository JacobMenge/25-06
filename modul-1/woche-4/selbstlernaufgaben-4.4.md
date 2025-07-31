# Selbstlernaufgaben - Windows Troubleshooting & Log-Analyse

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.

---

## 1. Grundlagenaufgabe - Mein Troubleshooting-Glossar

**Deine Aufgabe:**  
Erstelle ein persönliches Glossar mit **8 bis 10 Begriffen**, die im Unterricht behandelt wurden – zum Beispiel Event Viewer, Event-ID, Retention, Administrative Events, Runaway-Prozess, Memory Leak, MBR, GPT, UEFI oder Troubleshooting-Methodik.

Erkläre jeden Begriff in **deinen eigenen Worten** – kurz und verständlich (1–2 Sätze pro Begriff) und ordne ihn einem passenden Themenbereich zu (**Event Viewer**, **Systemdiagnose** oder **Boot-Probleme**).

**Beispiel:**  
- **Event-ID (Event Viewer):** Eine eindeutige Nummer für bestimmte Ereignis-Typen in Windows, die dabei hilft, gleiche Probleme auf verschiedenen Computern zu identifizieren.
- **Memory Leak (Systemdiagnose):** Ein Programmfehler, bei dem Arbeitsspeicher angefordert, aber nach Gebrauch nicht wieder freigegeben wird, was zu stetig steigendem RAM-Verbrauch führt.

**Formatvorschläge:**  
- Liste, Tabelle oder kurze Textabschnitte  
- PDF, Word-Dokument, Textdatei oder Screenshot

---

## 2. Grundlagenaufgabe - Event Viewer praktisch erkunden

**Deine Aufgabe:**  
Öffne den Event Viewer auf deinem Computer und führe eine systematische Analyse durch.

**So gehst du vor:**

### Schritt 1: Event Viewer öffnen und orientieren
1. **Öffne den Event Viewer:** Windows + R → "eventvwr.msc" → Enter
2. **Mache einen Screenshot** der Hauptansicht mit der Baumstruktur links
3. **Erkunde die vier Hauptkategorien:** System, Anwendung, Sicherheit, installation

### Schritt 2: Administrative Events analysieren
1. **Navigiere zu:** Benutzerdefinierte Ansichten → Administrative Events
2. **Dokumentiere 5 verschiedene Events:**
   - Event-ID, Quelle, Schweregrad (Fehler/Warnung/Information)
   - Kurze Beschreibung: Was ist passiert?
3. **Screenshots** der interessantesten Events

### Schritt 3: Gezielt nach wichtigen Event-IDs suchen
1. **Filtere das System-Log** nach Event-ID 1074 (System-Shutdown)
2. **Filtere das Application-Log** nach Event-ID 1000 (Anwendungs-Crash)
3. **Dokumentiere deine Funde:** Wann ist der Computer das letzte Mal heruntergefahren worden? Sind Anwendungen abgestürzt?

### Was du dokumentieren sollst:
- **Screenshots** der Event Viewer Hauptansicht und der gefundenen Events
- **Tabelle** mit den 5 analysierten Administrative Events
- **Reflexion:** Was war überraschend? Welche Probleme hat dein System?

**Formatvorschläge:**  
- Word-Dokument mit eingebetteten Screenshots  
- PDF mit beschrifteten Screenshots

---

## 3. Weiterführende Selbstlernaufgabe - Performance-Problem systematisch diagnostizieren

**Deine Aufgabe:**  
Analysiere das folgende realistische Szenario mit der 5-Schritt-Troubleshooting-Methodik und entwickle eine fundierte Lösung.

### Das Szenario:
**Problemmelder:** Frau Schmidt aus der Buchhaltung  
**Meldung:** *"Seit dem Windows Update am Montag startet mein Computer sehr langsam. Programme wie Excel und Word brauchen ewig zum Öffnen. Gestern war der Computer plötzlich komplett eingefroren und musste hart neu gestartet werden."*

**System-Informationen:**
- Computer: Dell OptiPlex 7090
- RAM: 8GB DDR4
- Festplatte: 256GB SSD
- Betriebssystem: Windows 11 Pro
- Letztes Update: Windows Update KB5034441 am Montag, 28.10.2024

### Bereitgestellte Diagnose-Daten:

**Task Manager Werte (Leistung-Tab):**
- CPU-Auslastung: 15% (im Leerlauf)
- RAM-Auslastung: 78% von 8GB
- Disk-Auslastung: 95-100% dauerhaft

**Top 5 Prozesse nach Festplatten-Nutzung:**
1. `Windows Search` (SearchIndexer.exe) - 45% Disk-Auslastung
2. `System and compressed memory` - 25% Disk-Auslastung  
3. `Windows Update Medic Service` - 15% Disk-Auslastung
4. `Antimalware Service Executable` - 8% Disk-Auslastung
5. `Microsoft Office Click-to-Run` - 5% Disk-Auslastung

**Event Viewer Findings:**
- **Event-ID 6008** (System-Log, 29.10.2024, 14:23): "Das System wurde zuvor am 29.10.2024 um 14:21:47 unerwartet heruntergefahren"
- **Event-ID 7034** (System-Log, 28.10.2024): "Der Dienst Windows Search wurde unerwartet beendet"  
- **Event-ID 1000** (Application-Log, 29.10.2024): "Name der fehlerhaften Anwendung: SearchIndexer.exe"
- **Event-ID 43** (System-Log, 28.10.2024): "Windows Update Installation erfolgreich: KB5034441"

**Autostart-Programme (Task Manager):**
- Microsoft Office (Auswirkung: Hoch)
- Adobe Updater (Auswirkung: Mittel)  
- Windows Search (Auswirkung: Hoch)
- Windows Security notification icon (Auswirkung: Niedrig)
- Skype (Auswirkung: Hoch)

---

### Deine Aufgabe: Wende die 5-Schritt-Methodik an

#### Schritt 1: Problem präzise definieren
**Definiere das Problem basierend auf den gegebenen Informationen:**
- Was sind die Hauptsymptome?
- Seit wann tritt das Problem auf?
- Was ist der Zusammenhang zwischen den Symptomen?

#### Schritt 2: Informationen bewerten und zusammenfassen
**Analysiere die bereitgestellten Diagnose-Daten:**
- Was verraten die Task Manager Werte über das Problem?
- Welche Erkenntnisse liefern die Event Log Einträge?
- Gibt es einen erkennbaren Zusammenhang zwischen den Daten?

#### Schritt 3: Hypothese entwickeln
**Entwickle eine fundierte Hypothese basierend auf den Daten:**
- Was ist die wahrscheinlichste Hauptursache?
- Wie hängen Windows Update, Windows Search und die Festplatten-Auslastung zusammen?
- Formuliere eine testbare Hypothese: "Wenn X das Problem ist, dann sollte Y beobachtbar sein"

#### Schritt 4: Lösungsstrategie entwickeln
**Entwickle einen strukturierten Lösungsplan:**
- Welche 3 Schritte würdest du in welcher Reihenfolge durchführen?
- Warum ist diese Reihenfolge sinnvoll?
- Welche Risiken gibt es bei den einzelnen Schritten?

**Beispiel-Struktur für deinen Lösungsplan:**
1. **Sofortmaßnahme** (schnelle Verbesserung):
2. **Hauptlösung** (Ursache beheben):
3. **Verifikation** (Lösung testen):

#### Schritt 5: Erfolg messen und dokumentieren
**Beschreibe, wie du den Erfolg messen würdest:**
- Welche Werte sollten sich im Task Manager verbessern?
- Welche Event Log Einträge sollten verschwinden/erscheinen?
- Wie würdest du die Lösung für die Zukunft dokumentieren?

### Was du abgeben sollst:
- **Strukturierter Bericht** mit allen 5 Schritten
- **Begründete Hypothese** basierend auf den Diagnose-Daten
- **Detaillierter Lösungsplan** mit Schritt-für-Schritt-Anweisungen
- **Reflexion:** Welche Informationen waren besonders aussagekräftig? Was hättest du zusätzlich wissen wollen?

**Formatvorschläge:**  
- Strukturierter Bericht als PDF oder Word-Dokument
- Verwende Zwischenüberschriften für die 5 Schritte
- Nutze Bulletpoints für Lösungsschritte

---

## 4. Vertiefende Selbstlernaufgabe - Benutzerdefinierte Ansicht erstellen und Boot-Analyse

**Deine Aufgabe:**  
Erstelle eine Event Viewer Konfiguration für die System-Überwachung und führe eine Boot-Analyse durch.

### Teil A: Benutzerdefinierte Ansicht erstellen
1. **Erstelle eine neue benutzerdefinierte Ansicht:**
   - Name: "Kritische System-Events"
   - Filter: Nur Fehler und Warnungen der letzten 30 Tage
   - Logs: System, Application, Setup
2. **Erstelle eine zweite Ansicht:**
   - Name: "Security-Monitoring"
   - Filter: Nur Sicherheits-Events (Event-IDs 4624, 4625, 4634)
   - Zeitraum: Letzte 7 Tage

### Teil B: Boot-Analyse durchführen
1. **Analysiere den letzten System-Start:**
   - Suche Event-ID 6005 (Event Log Service gestartet)
   - Suche Event-ID 6009 (Prozessor-Informationen)
   - Dokumentiere die Boot-Zeit und Hardware-Informationen

2. **Untersuche Boot-Probleme:**
   - Filtere nach Event-ID 6008 (Unerwarteter Shutdown)
   - Analysiere Event-ID 41 (System wurde nicht ordnungsgemäß heruntergefahren)
   - Dokumentiere eventuelle Boot-Probleme der letzten 30 Tage

### Teil C: System-Gesundheitscheck
1. **Hardware-Überwachung:**
   - Öffne Device Manager (devmgmt.msc)
   - Prüfe auf Hardware-Konflikte (gelbe Dreiecke oder rote X)
   - Screenshot der Device Manager Übersicht

2. **System-Informationen sammeln:**
   - Öffne System Information (msinfo32)
   - Dokumentiere: Betriebssystem-Version, Prozessor, installierter Arbeitsspeicher
   - Prüfe auf Hardware-Ressourcenkonflikte

### Was du dokumentieren sollst:
- **Screenshots** der beiden benutzerdefinierten Ansichten
- **Boot-Analyse-Tabelle** mit Datum, Event-ID und Beschreibung
- **System-Gesundheitsbericht** basierend auf Device Manager und System Information
- **Handlungsempfehlungen:** Welche Probleme hast du gefunden und wie würdest du sie angehen?

**Formatvorschläge:**  
- Ausführlicher Bericht als PDF
- Präsentation mit detaillierten Screenshots und Analysen

---

## Abgabehinweise

- **Frist:** Sonntag, 23:59 Uhr  
- **Abgabe:** direkt über den Google Classroom zur entsprechenden Aufgabe  
- **Dateiformate:** PDF, DOCX, ODT, PNG, JPG, Textdatei oder Screenshot
- **Wichtig:** Screenshots sollten gut lesbar und aussagekräftig sein
- **Tipp:** Verwende die Windows Snipping Tool oder Snip & Sketch für saubere Screenshots

**Sicherheitshinweise:**
- Führe keine Änderungen am System durch, die du nicht verstehst
- Erstelle vor größeren Tests einen Systemwiederherstellungspunkt
- Bei Unsicherheiten lieber nachfragen als riskante Aktionen durchführen

Bei Fragen melde dich gerne im Kurs-Slackchannel.
