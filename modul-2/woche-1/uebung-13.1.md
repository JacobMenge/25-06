# Multipass - Installation und VM-Einrichtung

## Was ist Multipass?

Multipass ist ein Virtualisierungs-Tool von Canonical (den Machern von Ubuntu), das speziell dafür entwickelt wurde, schnell und einfach Ubuntu-Instanzen auf Windows, macOS und Linux zu erstellen. Es ermöglicht Entwicklern, mit minimalem Aufwand isolierte Linux-Umgebungen zu erstellen.

---

## Installation von Multipass unter Windows

### Schritt 1: Systemvoraussetzungen prüfen

**Mindestanforderungen:**
- Windows 10 Version 1803 oder höher (oder Windows 11)
- 4 GB RAM (8 GB empfohlen)
- 10 GB freier Festplattenspeicher
- Virtualisierung muss im BIOS aktiviert sein

**Virtualisierung prüfen:**
1. Öffne den Task-Manager (Strg + Shift + Esc)
2. Gehe zum Tab "Leistung"
3. Klicke auf "CPU"
4. Unter "Virtualisierung" sollte "Aktiviert" stehen

> **Hinweis:** Falls "Deaktiviert" steht, musst du die Virtualisierung im BIOS aktivieren. Die genaue Vorgehensweise variiert je nach Hersteller deines Computers.

### Schritt 2: Multipass herunterladen

1. Öffne deinen Webbrowser
2. Gehe zu: **https://multipass.run**
3. Klicke auf "Download" und wähle "Windows"
4. Die Installationsdatei (ca. 200-300 MB) wird heruntergeladen

### Schritt 3: Multipass installieren

1. Navigiere zu deinem Download-Ordner
2. Doppelklicke auf die Datei `multipass-X.X.X+win-win64.exe`
3. Bestätige die Benutzerkontensteuerung mit "Ja"
4. Im Installationsassistenten:
   - Akzeptiere die Lizenzvereinbarung
   - Wähle den Installationsordner (Standard ist empfohlen)
   - Klicke auf "Install"
5. **Wichtig:** Wenn gefragt wird, ob Hyper-V aktiviert werden soll, klicke auf "Ja"
6. Nach der Installation: **Computer neu starten**

### Schritt 4: Installation überprüfen

1. Öffne die **PowerShell** oder **Eingabeaufforderung** (CMD)
   - Drücke `Windows-Taste + R`
   - Tippe `powershell` und drücke Enter

2. Gib folgenden Befehl ein:
```powershell
multipass version
```

3. Du solltest eine Ausgabe wie diese sehen:
```
multipass   1.13.0
multipassd  1.13.0
```

**Herzlichen Glückwunsch!** Multipass ist jetzt erfolgreich installiert.

---

## Einrichten einer Ubuntu VM

### Schritt 5: Erste Ubuntu-Instanz erstellen

Gib in der PowerShell folgenden Befehl ein:

```powershell
multipass launch --name meine-ubuntu-vm
```

**Was passiert hier?**
- Multipass lädt das neueste Ubuntu-Image herunter (beim ersten Mal, ca. 700 MB)
- Eine virtuelle Maschine mit dem Namen "meine-ubuntu-vm" wird erstellt
- Die VM wird automatisch gestartet

Dieser Vorgang dauert beim ersten Mal etwa 2-5 Minuten.

### Schritt 6: VM-Status überprüfen

Um zu sehen, ob deine VM läuft, gib ein:

```powershell
multipass list
```

Du solltest eine Ausgabe wie diese sehen:
```
Name                    State             IPv4             Image
meine-ubuntu-vm         Running           172.25.208.2     Ubuntu 24.04 LTS
```

### Schritt 7: Mit der VM verbinden

Um dich mit deiner Ubuntu-VM zu verbinden, verwende:

```powershell
multipass shell meine-ubuntu-vm
```

**Du bist jetzt in Ubuntu!** Die Eingabeaufforderung ändert sich zu:
```
ubuntu@meine-ubuntu-vm:~$
```

### Schritt 8: Erste Schritte in Ubuntu

Probiere diese grundlegenden Linux-Befehle aus:

```bash
# Zeige das aktuelle Verzeichnis an
pwd

# Liste alle Dateien und Ordner auf
ls -la

# Zeige Systeminformationen
uname -a

# Zeige die Ubuntu-Version
lsb_release -a

# Zeige verfügbaren Speicherplatz
df -h

# Zeige RAM-Nutzung
free -h
```

### Schritt 9: VM verlassen

Um die Ubuntu-VM zu verlassen und zu Windows zurückzukehren, gib ein:

```bash
exit
```

Du bist jetzt wieder in der Windows PowerShell.

---

## Grundlegende VM-Verwaltung

### VM stoppen

```powershell
multipass stop meine-ubuntu-vm
```

### VM starten

```powershell
multipass start meine-ubuntu-vm
```

### VM neu starten

```powershell
multipass restart meine-ubuntu-vm
```

### VM-Informationen anzeigen

```powershell
multipass info meine-ubuntu-vm
```

Dies zeigt Details wie:
- Zugewiesene Ressourcen (CPU, RAM, Disk)
- IP-Adresse
- Status
- Ubuntu-Version

### VM löschen

```powershell
multipass delete meine-ubuntu-vm
multipass purge
```

> **Achtung:** Der Befehl `purge` löscht die VM endgültig und unwiderruflich!

---

## Zusammenfassung der wichtigsten Befehle

```powershell
# VM erstellen und starten
multipass launch --name <vm-name>

# Mit VM verbinden
multipass shell <vm-name>

# Alle VMs anzeigen
multipass list

# VM-Details anzeigen
multipass info <vm-name>

# VM stoppen
multipass stop <vm-name>

# VM starten
multipass start <vm-name>

# VM löschen
multipass delete <vm-name>
multipass purge
```
