# Gruppenaufgaben - Windows 11 Troubleshooting
## Problem-Szenarien für Gruppenarbeit

---

## **GRUPPE A: Blue Screen Analyse**

### **Problem-Beschreibung:**
Die Marketingabteilung (8 Mitarbeiter) bekommt seit 5 Tagen regelmäßig Blue Screens auf ihren Windows 11-Arbeitsplätzen. Die Abstürze treten besonders häufig bei der Arbeit mit Adobe Creative Suite und während Microsoft Teams-Videokonferenzen auf.

### **Technische Details:**
- **Betriebssystem:** Windows 11 Pro 22H2 (Build 22621.2715)
- **Hardware:** Dell OptiPlex 7090, Intel Core i7-11700, 16GB RAM, NVIDIA RTX 3060
- **Stop-Code:** `DPC_WATCHDOG_VIOLATION` (0x00000133)
- **Begleitende Stop-Codes:** `SYSTEM_SERVICE_EXCEPTION` (0x0000003B)
- **Verursachende Dateien:** nvlddmkm.sys, dxgkrnl.sys

### **Event Viewer Befunde:**
- **System-Log, Event-ID 1001:** BugcheckCode: 307 (0x00000133)
- **System-Log, Event-ID 6008:** Das System wurde unerwartet heruntergefahren um 14:23:47
- **System-Log, Event-ID 7034:** Der Dienst "NVIDIA Display Driver Service" wurde unerwartet beendet
- **Application-Log, Event-ID 1000:** Adobe Premiere Pro, Ausnahme-Code: 0xc0000005

### **Zeitlicher Verlauf:**
- **15.11.2024:** Erste BSOD-Meldungen nach automatischem NVIDIA-Treiber-Update auf Version 546.17
- **16.11.2024:** 3 weitere BSODs, alle während GPU-intensiver Anwendungen
- **17.11.2024:** BSOD auch bei einfachen Office-Anwendungen
- **18.11.2024:** Windows Memory Diagnostic durchgeführt - keine RAM-Fehler gefunden
- **19.11.2024:** System-Wiederherstellung auf 14.11. fehlgeschlagen mit Fehler 0x80070091

### **Services-Status (services.msc):**
- **NVIDIA Display Driver Service:** Startet nicht automatisch, Status "Gestoppt"
- **Windows Audio:** Läuft normal
- **Plug and Play:** Läuft normal
- **NVIDIA GeForce Experience Service:** Status "Wird gestartet" - hängt beim Start

### **Betroffene Anwendungen:**
- Adobe Premiere Pro 2024 (häufigste Abstürze)
- Microsoft Teams (während Bildschirmfreigabe)
- Google Chrome (mit Hardware-Beschleunigung aktiviert)
- Zoom (bei Videokonferenzen)

### **Registry-Befunde (regedit):**
- **HKLM\SYSTEM\CurrentControlSet\Services\nvlddmkm:** Start-Wert = 0 (Automatisch)
- **HKLM\SOFTWARE\NVIDIA Corporation\Global:** Verschiedene Treiber-Versionen eingetragen
- **HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers:** TdrLevel = 2 (Standard)

### **Reliability Monitor Befunde:**
- **Kritische Ereignisse:** 8 System-Neustarts in 5 Tagen
- **Anwendungsfehler:** Adobe Premiere Pro - 12 Abstürze
- **Windows-Fehler:** Kernel-Power Event-ID 41 (unerwarteter Neustart)

### **Bisherige Lösungsversuche:**
- Windows Memory Diagnostic: Keine RAM-Fehler gefunden
- System-Wiederherstellung: Fehlgeschlagen 
- Abgesicherter Modus: Keine BSODs im abgesicherten Modus
- NVIDIA-Treiber deinstalliert: Windows installiert automatisch alten Treiber
- Device Manager: Grafikkarte zeigt gelbes Warndreieck

---

## **GRUPPE B: Windows Update Blockade**

### **Problem-Beschreibung:**
Die Buchhaltungsabteilung (12 Arbeitsplätze) kann seit 3 Wochen keine Windows 11-Updates mehr installieren. Alle Updateversuche schlagen mit verschiedenen Fehlercodes fehl. Der Microsoft Store funktioniert normal, nur Windows Update ist betroffen.

### **Technische Details:**
- **Betriebssystem:** Windows 11 Pro 22H2 (Build 22621.2428) - 3 Versionen veraltet
- **Hardware:** HP EliteDesk 800 G9, Intel Core i5-12500, 8GB RAM
- **Ziel-Update:** KB5032190 (November 2024 Cumulative Update)
- **Verfügbarer Speicherplatz:** 12-25GB auf C:\ (unterschiedlich pro PC)

### **Haupt-Fehlercodes:**
- **0x80070002:** "Angegebene Datei wurde nicht gefunden" (8 von 12 PCs)
- **0x8007000E:** "Nicht genügend Speicher verfügbar" (3 von 12 PCs)
- **0x80073712:** "Die Komponentenspeicher-Transaktion konnte nicht durchgeführt werden" (4 PCs)

### **Event Viewer Einträge:**
- **System-Log, Event-ID 20:** Windows Update Agent Fehler 0x80070002
- **System-Log, Event-ID 7000:** Der Dienst "Windows Update" konnte nicht gestartet werden (2 PCs)
- **System-Log, Event-ID 7034:** Windows Update-Dienst wurde unerwartet beendet
- **Application-Log, Event-ID 1000:** TiWorker.exe Absturz, Exception: 0xc0000374

### **Services-Status Analyse:**
- **Windows Update (wuauserv):** Läuft, aber hängt bei "Updates werden gesucht..." seit Stunden
- **Background Intelligent Transfer Service (BITS):** Status "Gestoppt" - startet nicht automatisch
- **Cryptographic Services (CryptSvc):** Läuft, aber sehr hohe CPU-Auslastung (25-40%)
- **Windows Update Medic Service:** Event-ID 7034 - Dienst beendet sich ständig selbst

### **Update-Historie (Windows Update-Verlauf):**
- **14.10.2024:** Letztes erfolgreiches Update KB5031354
- **21.10.2024:** KB5032007 - Installation fehlgeschlagen (0x80070002)
- **28.10.2024:** KB5032190 - Download bei 47% hängen geblieben
- **04.11.2024:** Automatische Reparatur - fehlgeschlagen
- **11.11.2024:** Windows Update Troubleshooter - "Problem konnte nicht behoben werden"

### **SoftwareDistribution-Ordner Status:**
- **Ordnergröße:** 2.8GB (viele .tmp und .partial Dateien)
- **Download-Ordner:** 1.2GB, 847 Dateien, älteste von Oktober
- **DataStore-Dateien:** Verschiedene .edb-Dateien mit Fehlern

### **Windows Update Troubleshooter Ergebnisse:**
- **Gefundene Probleme:** "Windows Update-Datenbank ist beschädigt"
- **Reparatur-Versuche:** "Update-Komponenten konnten nicht zurückgesetzt werden"
- **Status:** "Es konnten nicht alle Probleme behoben werden"

### **Task Manager Befunde:**
- **TiWorker.exe:** Hohe CPU-Auslastung (15-30%) ohne Fortschritt
- **svchost.exe (wuauserv):** 2-4% CPU, aber kein Speicher-Anstieg
- **Disk-Auslastung:** 100% während Update-Suche für 2-3 Stunden

### **Bisherige Lösungsversuche:**
- Windows Update Troubleshooter: "Problem konnte nicht vollständig behoben werden"
- SoftwareDistribution-Ordner manuell gelöscht: Temporäre Besserung, dann wieder Fehler
- Services manuell neu gestartet: Kurzzeitig Besserung, Problem kehrt zurück
- System File Checker (sfc /scannow): "Windows-Ressourcenschutz hat beschädigte Dateien gefunden, konnte jedoch einige nicht reparieren"

---

## **GRUPPE C: Microsoft Office Anwendungsabstürze**

### **Problem-Beschreibung:**
Microsoft Excel 2021 stürzt bei 9 Mitarbeitern der Personalabteilung beim Öffnen spezifischer .xlsx-Dateien ab. Die gleichen Dateien funktionieren auf anderen PCs einwandfrei. Das Problem tritt seit der Installation des Windows 11-Updates KB5031455 vor 6 Tagen auf.

### **Technische Details:**
- **Betriebssystem:** Windows 11 Pro 22H2 (Build 22621.2715)
- **Office-Version:** Microsoft Office LTSC Professional Plus 2021 (Build 14332.20447)
- **Hardware:** Lenovo ThinkCentre M90q Gen 3, Intel Core i5-12400T, 16GB RAM
- **Betroffene Dateien:** Personalstammdaten.xlsx (12MB), Gehaltsabrechnung_Nov2024.xlsx (8MB)

### **Crash-Details aus Event Viewer:**
- **Application-Log, Event-ID 1000:**
  - Anwendungsname: EXCEL.EXE, Version: 16.0.14332.20447
  - Fehlerhafte Modulname: KERNELBASE.dll
  - Ausnahmecode: 0xc0000005 (Zugriffsverletzung)
  - Offset: 0x0000000000038e0c

### **Office-Event-Protokolle:**
- **Application-Log, Event-ID 2001:** Office Software Protection Platform Fehler
- **Application-Log, Event-ID 1001:** Windows Error Reporting für Excel.exe
- **System-Log, Event-ID 1000:** Excel.exe Absturz mit ntdll.dll als fehlerhaftem Modul

### **Add-Ins Status (Excel → Datei → Optionen → Add-Ins):**
- **COM Add-Ins aktiv:** Adobe Acrobat PDFMaker Office COM Addin
- **Excel Add-Ins aktiv:** Analysis ToolPak, Solver Add-in
- **Deaktivierte Add-Ins:** Power Query (automatisch deaktiviert nach Crash)

### **Dateispezifische Details:**
- **Personalstammdaten.xlsx:** 20.000 Zeilen, 45 Spalten, 3 Pivot-Tabellen
- **Komplexe Formeln:** SVERWEIS, INDEX/VERGLEICH, Array-Formeln
- **Externe Verknüpfungen:** Links zu anderen Excel-Dateien im Netzwerk
- **VBA-Makros:** Automatische Berechnungen beim Öffnen der Datei

### **Reproduzierbarkeit:**
- **Absturz-Timing:** 15-30 Sekunden nach dem Öffnen der Datei
- **Andere Excel-Dateien:** Kleinere Dateien (unter 5MB) funktionieren normal
- **Office-Programme:** Word und PowerPoint sind nicht betroffen
- **Abgesicherter Modus:** Excel /safe - Dateien öffnen sich ohne Formatierung

### **Task Manager während Crash:**
- **Excel.exe Speicherverbrauch:** Steigt von 150MB auf 2.1GB vor Absturz
- **Handle-Count:** Excel.exe erreicht 8.500+ Handles vor Absturz
- **CPU-Auslastung:** Excel.exe 45-60% für 10-15 Sekunden, dann Absturz

### **Registry-Befunde:**
- **HKCU\Software\Microsoft\Office\16.0\Excel\Security:** Makrosicherheit = Mittel
- **HKCU\Software\Microsoft\Office\16.0\Excel\Options:** Verschiedene Excel-Optionen geändert
- **HKLM\SOFTWARE\Microsoft\Office\16.0\Excel\InstallRoot:** Installation scheint vollständig

### **Reliability Monitor:**
- **Anwendungsfehler:** Excel.exe - 15 Abstürze in 6 Tagen
- **Muster:** Alle Abstürze zwischen 09:00-11:00 Uhr (Arbeitsbeginn)
- **Windows-Updates:** KB5031455 am 13.11.2024 installiert

### **Bisherige Lösungsversuche:**
- **Office-Reparatur (Schnellreparatur):** Keine Verbesserung
- **Excel im abgesicherten Modus:** Dateien öffnen sich, aber ohne Makros und Formatierung
- **Alle Add-Ins deaktiviert:** Problem bleibt bestehen
- **Excel-Einstellungen zurückgesetzt:** Registry-Schlüssel gelöscht, keine Verbesserung
- **Office-Updates installiert:** Neueste Patches verfügbar, aber Problem bleibt

---

## **GRUPPE D: Berechtigungs- und Zugriffsprobleme**

### **Problem-Beschreibung:**
Nach einem Windows 11-Update können 14 Mitarbeiter der Vertriebsabteilung nicht mehr auf ihre Desktop-Dateien und Dokumente-Ordner zugreifen. Die Fehlermeldung "Zugriff verweigert" erscheint beim Versuch, Ordner zu öffnen oder Dateien zu bearbeiten.

### **Technische Details:**
- **Betriebssystem:** Windows 11 Pro 22H2 (Build 22621.2715)
- **Update:** KB5031455 vor 4 Tagen installiert
- **Betroffene Konten:** Lokale Windows-Konten (nicht Microsoft-Konten)
- **Hardware:** ASUS ExpertCenter D7 Mini, Intel Core i5-12400, 8GB RAM

### **Fehlermeldungen:**
- **Windows-Fehlercode 0x80070005:** "Zugriff verweigert" beim Öffnen von Desktop-Ordnern
- **"Sie benötigen Berechtigungen zur Durchführung des Vorgangs"**
- **"Wenden Sie sich an den Administrator, um Berechtigungen zu erhalten"**

### **Betroffene Ordner-Struktur:**
```
C:\Users\[benutzername]\
├── Desktop\ (4.2GB, 150+ Dateien) - Zugriff verweigert
├── Documents\ (8.7GB, 300+ Office-Dateien) - Zugriff verweigert  
├── Downloads\ (2.1GB) - Funktioniert normal
└── Pictures\ (1.5GB) - Zugriff verweigert
```

### **Event Viewer Einträge:**
- **Security-Log, Event-ID 4656:** Objekthandle angefordert - Fehler "Zugriff verweigert"
- **Security-Log, Event-ID 4625:** Anmeldefehler für Benutzer bei Ordner-Zugriff
- **System-Log, Event-ID 5061:** Cryptographic operation (eventuell Berechtigungs-bezogen)

### **NTFS-Berechtigungen (Eigenschaften → Sicherheit):**
- **Desktop-Ordner Besitzer:** SYSTEM (sollte Benutzer sein)
- **Aktuelle Berechtigungen:**
  - Administratoren: Vollzugriff ✓
  - SYSTEM: Vollzugriff ✓
  - [Benutzername]: Nicht aufgelistet ❌
  - Benutzer: Lesen ✓ (sollte Vollzugriff sein)

### **User Account Control (UAC) Status:**
- **UAC-Einstellung:** Standard (2. Stufe von 4)
- **Admin-Approval-Modus:** Aktiviert
- **Registry HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System:**
  - EnableLUA = 1 (UAC aktiviert)
  - ConsentPromptBehaviorUser = 3 (Standard)

### **Windows Defender Controlled Folder Access:**
- **Status:** Aktiviert (möglicherweise nach Update automatisch aktiviert)
- **Geschützte Ordner:** Desktop, Documents, Pictures automatisch hinzugefügt
- **Zugelassene Apps:** Microsoft Office nicht in der Liste
- **Blockierte Zugriffe:** 47 Zugriffe in letzten 4 Tagen blockiert

### **Benutzerkonten-Verwaltung (lusrmgr.msc):**
- **Benutzer-Status:** Konto aktiv, nicht gesperrt
- **Gruppen-Mitgliedschaft:** Benutzer ist Mitglied der Gruppe "Benutzer" (nicht "Administratoren")
- **Konto-Eigenschaften:** "Benutzer kann Kennwort nicht ändern" = deaktiviert

### **Registry-Befunde (regedit):**
- **HKLM\SOFTWARE\Microsoft\Windows Defender\Windows Defender Exploit Guard\Controlled Folder Access:**
  - EnableControlledFolderAccess = 1 (aktiviert)
- **HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer:**
  - NoDesktop = 0 (Desktop-Zugriff erlaubt)

### **System-Wiederherstellung:**
- **Verfügbare Wiederherstellungspunkte:** 
  - 10.11.2024 "Automatischer Wiederherstellungspunkt" (vor Update)
  - 13.11.2024 "Windows Update" (nach Problem-Update)
- **Wiederherstellung auf 10.11:** Fehlgeschlagen mit Fehler 0x80070091

### **Task Manager Prozess-Analyse:**
- **explorer.exe:** Läuft normal, normaler Speicherverbrauch
- **dwm.exe:** Desktop Window Manager funktioniert
- **winlogon.exe:** Keine Auffälligkeiten bei Anmelde-Prozess

### **Bisherige Lösungsversuche:**
- **Berechtigungen manuell gesetzt:** Rechtsklick → Eigenschaften → Sicherheit → Bearbeiten (Fehlermeldung: "Zugriff verweigert")
- **Als Administrator angemeldet:** Problem bleibt bestehen, auch Admin kann Berechtigungen nicht ändern
- **Controlled Folder Access deaktiviert:** Teilweise Verbesserung bei 4 von 14 Benutzern
- **System-Wiederherstellung:** Fehlgeschlagen
- **Benutzer zu Administratoren-Gruppe hinzugefügt:** Temporäre Lösung, aber nicht praktikabel für alle

---

## **Arbeitsauftrag für alle Gruppen:**

### **Wichtiger Hinweis:**
Ihr arbeitet nur mit den gegebenen Informationen aus dem Szenario. Ihr könnt keine eigenen Tests durchführen, sondern müsst basierend auf den Event Viewer-Einträgen, Services-Status und anderen bereitgestellten Daten eure Analyse machen.

### **1. 5-Schritt-Methodik anwenden:**
☐ **Problem definieren:** Was genau ist das Kernproblem? Wer ist betroffen?  
☐ **Informationen auswerten:** Welche Hinweise geben euch Event Viewer, Services, Registry?  
☐ **Hypothesen entwickeln:** 3 wahrscheinlichste Ursachen basierend auf den gegebenen Daten  
☐ **Lösungsstrategie entwickeln:** Welche Schritte würdet ihr in welcher Reihenfolge durchführen?  
☐ **Verifikation planen:** Wie würdet ihr prüfen, ob eure Lösung funktioniert?  

### **2. Detailanalyse erstellen:**
☐ **Event Viewer-Analyse:** Welche Event-IDs sind besonders wichtig? Was sagen sie aus?  
☐ **Services-Diagnose:** Welche Services sind problematisch und warum?  
☐ **Registry-Befunde:** Was zeigen die Registry-Einträge über die Ursache?  
☐ **Tools-Einsatz:** Welche Windows-Tools würdet ihr für Diagnose und Reparatur nutzen?  

### **3. Präsentation vorbereiten:**
☐ **Problem-Zusammenfassung:** Kernproblem in 2-3 Sätzen erklären  
☐ **Ursachen-Analyse:** Warum ist das Problem aufgetreten?  
☐ **Lösungsplan:** Konkrete Schritte zur Behebung  
☐ **Prävention:** Wie verhindert man das Problem in Zukunft?

### **Hilfsmittel:**
• Eure Tools für Digitalearbeit
• Euer Wissen über Event Viewer, Services, Registry und 5-Schritt-Methodik
• Internet-Recherche für spezifische Event-IDs und Fehlercodes
