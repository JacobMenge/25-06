# Python Installation auf Windows 11 – Schritt-für-Schritt-Anleitung

## Installationsübersicht (Nachmittag)

Diese Anleitung führt dich durch die komplette Einrichtung deiner Python-Entwicklungsumgebung:
- Python Installation
- Visual Studio Code (VS Code)
- Notwendige Extensions
- Erste Schritte mit Python

---

## Schritt 1: Python installieren

### 1.1 Python herunterladen

1. Öffne deinen Browser und gehe zu: **https://www.python.org/downloads/**
2. Die Website erkennt automatisch dein Betriebssystem (Windows)
3. Klicke auf den gelben Button **"Download Python 3.x.x"** (z.B. Python 3.12.0)
4. Die Datei `python-3.x.x-amd64.exe` wird heruntergeladen

### 1.2 Python installieren

1. Öffne die heruntergeladene `.exe`-Datei
2. **WICHTIG:** Setze ein Häkchen bei **"Add Python to PATH"** (ganz unten im Fenster)
   - ⚠️ Dieser Schritt ist entscheidend!
3. Klicke auf **"Install Now"** (empfohlene Installation)
4. Warte, bis die Installation abgeschlossen ist
5. Klicke auf **"Close"**

### 1.3 Installation überprüfen

1. Drücke `Windows + R`
2. Tippe `cmd` ein und drücke Enter
3. Gib folgende Befehle ein:

```bash
py --version
```

Du solltest etwas wie `Python 3.12.0` sehen.

```bash
py -m pip --version
```

Du solltest die Version von pip sehen (z.B. `pip 23.x.x`).

**Hinweis:** Wir verwenden `py` (Python Launcher für Windows) statt `python`, da dies zuverlässiger funktioniert – besonders wenn mehrere Python-Versionen installiert sind.

**⚠️ Falls der Microsoft Store sich öffnet:** Wenn beim Tippen von `python` der Microsoft Store aufgeht oder die Fehlermeldung "Python was not found" erscheint:
1. Gehe zu **Einstellungen** → **Apps** → **Erweiterte App-Einstellungen**
2. Klicke auf **App-Ausführungsaliase**
3. Deaktiviere **python.exe** und **python3.exe**
4. Öffne ein neues Terminal

 **Python ist jetzt installiert!**

---

## Schritt 2: Visual Studio Code installieren

### 2.1 VS Code herunterladen

1. Gehe zu: **https://code.visualstudio.com/**
2. Klicke auf **"Download for Windows"**
3. Die Datei `VSCodeUserSetup-x64-x.x.x.exe` wird heruntergeladen

### 2.2 VS Code installieren

1. Öffne die heruntergeladene `.exe`-Datei
2. Akzeptiere die Lizenzvereinbarung
3. Wähle den Installationspfad (Standard ist OK)
4. **Wichtige Optionen** (Häkchen setzen):
   -  "Zu PATH hinzufügen" (wichtig!)
   -  "Code mit Code öffnen" für Kontextmenü
   -  Unterstützte Dateitypen registrieren
5. Klicke auf **"Installieren"**
6. Nach der Installation: Klicke auf **"Fertigstellen"**

---

## Schritt 3: Python-Extension in VS Code installieren

### 3.1 VS Code öffnen

1. Starte **Visual Studio Code**
2. Beim ersten Start kannst du das Design/Theme auswählen (optional)

### 3.2 Python-Extension installieren

1. Klicke auf das **Extensions-Symbol** in der linken Seitenleiste (oder drücke `Strg + Shift + X`)
2. Suche nach **"Python"** in der Suchleiste
3. Installiere die Extension **"Python"** von Microsoft (meist die erste in der Liste)
   - Erkennbar am blauen Verifizierungs-Badge
   - Über 100 Millionen Downloads
4. Klicke auf **"Install"**
5. Warte, bis die Installation abgeschlossen ist

### 3.3 Python-Interpreter auswählen (wichtig!)

Nach der Installation der Extension musst du einmal festlegen, welchen Python-Interpreter VS Code verwenden soll:

1. Drücke `Strg + Shift + P` (öffnet die Befehlspalette)
2. Tippe **"Python: Select Interpreter"**
3. Wähle den Python-Interpreter von python.org aus (erkennbar an der Version, z.B. `Python 3.12.0 64-bit`)
4. Der ausgewählte Interpreter wird unten rechts in der Statusleiste angezeigt

**Warum?** Dies stellt sicher, dass VS Code den richtigen Python-Interpreter verwendet und nicht versehentlich einen alten oder falschen erwischt.

### 3.4 Empfohlene zusätzliche Extensions (optional)

- **Pylance**: Für bessere Code-Vervollständigung (wird automatisch mit Python-Extension installiert)

---

## Schritt 4: Erste Python-Datei erstellen

### 4.1 Arbeitsordner erstellen

1. Erstelle einen neuen Ordner auf deinem Computer, z.B.:
   - `C:\Users\DeinName\PythonProjekte`
2. Öffne VS Code
3. Klicke auf **"Ordner öffnen"** (oder `Strg + K, Strg + O`)
4. Wähle deinen neu erstellten Ordner aus

### 4.2 Erste Datei: hello.py

1. Klicke auf das **"Neue Datei"**-Symbol (oder `Strg + N`)
2. Speichere die Datei als `hello.py`:
   - Klicke auf **"Datei" → "Speichern unter"** (oder `Strg + S`)
   - Gib den Namen `hello.py` ein
   - Speichern

3. Schreibe folgenden Code in die Datei:

```python
# Mein erstes Python-Programm
print("Hallo Welt!")
print("Python auf Windows 11 funktioniert!")

# Einfache Berechnung
zahl1 = 10
zahl2 = 5
summe = zahl1 + zahl2

print(f"Die Summe von {zahl1} und {zahl2} ist: {summe}")
```

4. Speichere die Datei (`Strg + S`)

---

## Schritt 5: Code ausführen

### 5.1 Über das integrierte Terminal

1. Öffne das Terminal in VS Code:
   - Klicke auf **"Terminal" → "Neues Terminal"** (oder drücke `` Strg + ` ``)
2. Stelle sicher, dass du im richtigen Ordner bist
3. Führe deinen Code aus:

```bash
py hello.py
```

**Warum `py` statt `python`?** Der Python Launcher (`py`) ist auf Windows die zuverlässigste Methode und umgeht typische PATH- oder Store-Alias-Probleme.

### 5.2 Erwartete Ausgabe

```
Hallo Welt!
Python auf Windows 11 funktioniert!
Die Summe von 10 und 5 ist: 15
```

 **Dein erstes Python-Programm läuft!**

### 5.3 Alternative: Run-Button

- Klicke auf den **Play-Button** (▶️) oben rechts in VS Code
- Der Code wird automatisch ausgeführt

---

## Checkliste: Installation abgeschlossen 

Überprüfe, ob alle Schritte erfolgreich waren:

-  **Python installieren** – `python --version` zeigt Version an
-  **PATH aktivieren** – Python-Befehle funktionieren in CMD/PowerShell
-  **VS Code installiert** – Editor startet ohne Probleme
-  **Python-Extension** – Extension ist aktiv in VS Code
-  **Erste Datei hello.py** – Datei wurde erstellt und gespeichert
-  **Testausgabe im Terminal** – Ausgabe erscheint wie erwartet

---

## Fehlerbehebung

### Problem: "python" wird nicht erkannt oder öffnet den Microsoft Store

**Lösung 1 (empfohlen):**
- Verwende `py` statt `python`:
  ```bash
  py --version
  py hello.py
  ```

**Lösung 2 (Store-Alias deaktivieren):**
1. Gehe zu **Einstellungen** → **Apps** → **Erweiterte App-Einstellungen**
2. Klicke auf **App-Ausführungsaliase**
3. Deaktiviere **python.exe** und **python3.exe**
4. Öffne ein neues Terminal

**Lösung 3 (Neuinstallation):**
1. Deinstalliere Python
2. Installiere erneut und achte auf das Häkchen bei **"Add Python to PATH"**
3. Starte den Computer neu

### Problem: VS Code zeigt Python-Extension-Fehler

**Lösung:**
1. Öffne VS Code
2. Drücke `Strg + Shift + P`
3. Tippe: **"Python: Select Interpreter"**
4. Wähle die installierte Python-Version aus (z.B. `Python 3.12.0 64-bit`)

### Problem: Code wird nicht ausgeführt

**Lösung:**
1. Überprüfe, ob die Datei als `.py` gespeichert wurde
2. Stelle sicher, dass du im richtigen Ordner bist (im Terminal)
3. Verwende `py hello.py` statt `python hello.py`
4. Kontrolliere, ob der richtige Interpreter in VS Code ausgewählt ist (unten rechts)

### Problem: `code .` funktioniert nicht

**Lösung:**
1. Bei der VS Code-Installation muss "Zu PATH hinzufügen" aktiviert sein
2. Öffne ein **neues** Terminal (wichtig nach der Installation)
3. Versuche es erneut: `code .`

---

## Nützliche Tipps & Tricks

### Terminal-Befehle

- **Ordner direkt in VS Code öffnen:**
  ```bash
  code .
  ```
  (funktioniert nach der VS Code-Installation in jedem beliebigen Ordner)

### Pakete installieren (robust)

Verwende immer `py -m pip` statt nur `pip`:

```bash
py -m pip install numpy
py -m pip install pandas
py -m pip list  # Zeigt alle installierten Pakete
```

**Warum?** So stellst du sicher, dass pip zur richtigen Python-Version gehört.

### VS Code Shortcuts

- `Strg + Shift + P` – Befehlspalette öffnen
- `Strg + ´` – Terminal ein-/ausblenden
- `Strg + B` – Seitenleiste ein-/ausblenden
- `Strg + S` – Datei speichern
- `Strg + N` – Neue Datei
