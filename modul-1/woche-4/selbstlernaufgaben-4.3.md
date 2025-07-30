# Selbstlernaufgaben - Windows System-Administration & Registry

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.

---

## 1. Grundlagenaufgabe – Mein System-Administration Glossar

**Deine Aufgabe:**  
Erstelle ein persönliches Glossar mit **8 bis 10 Begriffen**, die heute im Unterricht behandelt wurden – zum Beispiel Registry, Windows Services, Root Keys, RPC, Service-Abhängigkeiten, DHCP, Umgebungsvariablen oder Start-Typen.

Erkläre jeden Begriff in **deinen eigenen Worten** – kurz und verständlich (1–2 Sätze pro Begriff) und ordne ihn einem passenden Themenbereich zu (**Registry** oder **Services**).

**Formatvorschläge:**  
- Liste, Tabelle oder kurze Textabschnitte  
- PDF, Word-Dokument, Textdatei oder Screenshot

---

## 2. Grundlagenaufgabe – Registry Editor praktisch nutzen

**Deine Aufgabe:**  
Führe eine sichere Registry-Exploration durch und dokumentiere deine Erkenntnisse mit detaillierten Screenshots.

**⚠️ WICHTIGER SICHERHEITSHINWEIS:** Du wirst NUR schauen und dokumentieren – niemals etwas ändern, löschen oder neue Werte erstellen!

### Schritt 1: Registry Editor öffnen und Vollbackup erstellen

**Registry öffnen:**
1. Drücke **Windows-Taste + R** → Es öffnet sich der "Ausführen"-Dialog
2. Tippe **regedit** ein und drücke **Enter**
3. Falls eine Benutzerkontensteuerung erscheint, klicke **Ja**
4. Der Registry Editor öffnet sich (Fenster mit Baumstruktur links, Details rechts)

**Vollbackup erstellen (UNBEDINGT als erstes machen!):**
1. Klicke oben in der Menüleiste auf **Datei**
2. Wähle **Exportieren...** aus dem Dropdown-Menü
3. Im Dialog "Registry-Datei exportieren":
   - Bei "Exportbereich" wähle **Alle** (nicht "Ausgewählte Verzweigung")
   - Wähle einen Speicherort (z.B. Desktop)
   - Gib einen Namen ein: `Registry_Backup_DATUM` (z.B. Registry_Backup_30_07_2025)
   - Klicke **Speichern**
4. **Warte**, bis der Export abgeschlossen ist (kann 1-2 Minuten dauern)
5. Mache einen **Screenshot** des gespeicherten Backup-Files

### Schritt 2: Navigation zu den verschiedenen Registry-Pfaden

**Was sind Registry-Pfade?** Ähnlich wie Ordnerpfade auf der Festplatte (C:\Windows\System32) gibt es in der Registry hierarchische Pfade, die mit einem Root Key beginnen und durch Backslashes getrennt sind.

#### Pfad 1: Autostart-Programme finden
1. **Navigiere zu:** `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
   - Klicke links auf **HKEY_CURRENT_USER** (falls nicht schon geöffnet)
   - Klicke auf den kleinen **Pfeil** oder **Dreieck** neben "SOFTWARE" 
   - Klicke auf den Pfeil neben **Microsoft**
   - Klicke auf den Pfeil neben **Windows**
   - Klicke auf den Pfeil neben **CurrentVersion**
   - (...)
   - Klicke auf **Run** (ohne Pfeil - das ist der finale Ordner)

2. **Dokumentiere:**
   - Mache einen **Screenshot** der rechten Seite (zeigt die Autostart-Programme)
   - **Erklärung:** Hier stehen alle Programme, die beim Windows-Start automatisch für den aktuellen Benutzer starten
   - Liste die Programme auf, die du siehst (Name und Pfad)
   - **Datentypen:** Die meisten Einträge sind vom Typ REG_SZ (Text-String)

#### Pfad 2: System-Hardware-Informationen
1. **Navigiere zu:** `HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System`
   - Klicke links auf **HKEY_LOCAL_MACHINE**
   - Öffne **HARDWARE** → **DESCRIPTION** → **System**

2. **Dokumentiere:**
   - Screenshot der Systeminformationen
   - **Erklärung:** Hier speichert Windows Informationen über die Hardware-Konfiguration
   - Welche Informationen siehst du? (CPU, BIOS, etc.)
   - Notiere dir interessante Werte wie "SystemBiosVersion" oder "VideoBiosVersion"

#### Pfad 3: Dateizuordnungen verstehen
1. **Navigiere zu:** `HKEY_CLASSES_ROOT\.pdf`
   - Klicke auf **HKEY_CLASSES_ROOT**
   - Scrolle nach unten zu **.pdf** (alphabetisch sortiert bei den Punkten)
   - Klicke auf **.pdf**

2. **Dokumentiere:**
   - Screenshot des .pdf-Eintrags
   - **Erklärung:** HKEY_CLASSES_ROOT verwaltet Dateierweiterungen und bestimmt, welches Programm welche Dateitypen öffnet
   - Welcher Wert steht im "(Standard)"-Eintrag? (Das ist das verknüpfte Programm)
   - Schaue dir auch andere Dateierweiterungen an (z.B. .txt, .docx)

### Schritt 3: Berechtigungen verstehen

**Was sind Registry-Berechtigungen?** Wie bei Dateien und Ordnern haben auch Registry-Schlüssel Berechtigungen, die bestimmen, wer sie lesen, ändern oder löschen darf.

1. **Berechtigungen anzeigen:**
   - Gehe zurück zu `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
   - **Rechtsklick** auf den **Run**-Ordner (in der linken Baumansicht)
   - Wähle **Berechtigungen...** aus dem Kontextmenü

2. **Dokumentiere:**
   - Screenshot des Berechtigungen-Dialogs
   - Welche Benutzer/Gruppen haben Zugriff?
   - Welche Arten von Berechtigungen gibt es? (Vollzugriff, Lesen, etc.)
   - **Erklärung:** "Vollzugriff" bedeutet lesen, schreiben und löschen. "Lesen" bedeutet nur anzeigen ohne Änderungen.


### Schritt 4: Registry Editor sicher schließen
1. Klicke auf **Datei** → **Beenden** oder schließe das Fenster mit dem **X**
2. Keine Änderungen wurden gemacht, daher keine Speicher-Aufforderung

### Was du dokumentieren sollst:
- **Screenshots** aller besuchten Registry-Pfade
- **Erkläre**, was du in jedem Pfad gefunden hast
- **Liste** mindestens 3 Autostart-Programme auf
- **Beschreibe** die Hardware-Informationen, die du gesehen hast
- **Dokumentiere** die Berechtigungsstruktur eines Registry-Schlüssels
- **Reflexion:** Was war überraschend? Was hast du Neues gelernt?

**Formatvorschläge:**  
- Word-Dokument mit eingebetteten Screenshots  
- PDF mit beschrifteten Screenshots  
- PowerPoint-Präsentation mit Erklärungen

---

## 3. Grundlagenaufgabe – Windows Services verstehen

**Deine Aufgabe:**  
Öffne die Services-Verwaltung (`services.msc`) und analysiere wichtige System-Services.

**Erstelle eine Tabelle mit folgenden Services:**
- Windows Audio
- DHCP Client  
- DNS Client
- Windows Update
- Themes

**Für jeden Service dokumentiere:**
- Aktueller Status (Gestartet/Beendet)
- Start-Typ (Automatisch/Manuell/Deaktiviert)
- Beschreibung (was macht der Service?)
- Abhängigkeiten (falls vorhanden)

**Zusatzfrage:** Erkläre den Unterschied zwischen "Automatisch" und "Automatisch (Verzögert)" beim Start-Typ.

**Formatvorschläge:**  
- Tabelle in Word/Excel oder als Screenshot  
- PDF-Dokument

---

## 4. Vertiefende Selbstlernaufgabe – Service-Troubleshooting Szenario

**Deine Aufgabe:**  
Stelle dir vor, ein Benutzer meldet: "Mein Computer hat keine Internetverbindung, aber das Netzwerkkabel ist angeschlossen."

**Entwickle einen systematischen Troubleshooting-Plan:**

1. **Welche Services würdest du als erstes überprüfen?** (Mindestens 3 Services nennen und begründen)
2. **Beschreibe Schritt für Schritt**, wie du die Service-Diagnose durchführst:
   - Wo checkst du den Service-Status?
   - Wie startest du einen gestoppten Service neu?
   - Wo findest du Fehlermeldungen?
3. **Service-Abhängigkeiten:** Erkläre, warum manche Services andere Services zum Funktionieren brauchen
4. **Präventive Maßnahmen:** Wie konfigurierst du Services für automatische Wiederherstellung bei Fehlern?

**Formatvorschläge:**  
- Schritt-für-Schritt-Anleitung als PDF  
- Flussdiagramm oder strukturierte Liste

---

## Abgabehinweise

- **Frist:** Sonntag, 23:59 Uhr  
- **Abgabe:** direkt über den Google Classroom zur entsprechenden Aufgabe  
- **Dateiformate:** PDF, DOCX, ODT, PNG, JPG, Textdatei oder Screenshot usw. ..
- **Wichtig:** Bei Registry-Arbeiten immer zuerst Backup erstellen!

Bei Fragen melde dich gerne im Kurs-Slackchannel.
