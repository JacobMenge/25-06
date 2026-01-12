# Node.js & npm Installation - Schritt-für-Schritt Anleitung

## Übersicht

Diese Anleitung führt dich durch die Installation von **Node.js** und **npm** auf deinem Computer. Diese Werkzeuge sind die Grundlage für die React-Entwicklung.

**Was sind Node.js und npm?**

| Tool | Beschreibung | Python-Vergleich |
|------|--------------|------------------|
| **Node.js** | JavaScript-Laufzeitumgebung (führt JS außerhalb des Browsers aus) | `python` (Interpreter) |
| **npm** | Node Package Manager (installiert JavaScript-Pakete) | `pip` (Package Manager) |

**Wichtig:** Wir nutzen Node.js und npm als **Entwicklungswerkzeuge** für React - nicht als Backend! Euer Backend bleibt Python/FastAPI.

---

## Kurzanleitung (für Ungeduldige)

Wenn du es eilig hast - hier die Kurzversion:

1. Gehe zu **https://nodejs.org** und lade die **LTS-Version** herunter
2. Installiere mit den Standard-Einstellungen (Next, Next, ..., Finish)
3. **Schließe alle Terminal-Fenster** und öffne ein neues
4. Prüfe: `node --version` (sollte eine Versionsnummer zeigen)
5. Prüfe: `npm --version` (sollte eine Versionsnummer zeigen)
6. Fertig!

**Problem?** Lies die ausführliche Anleitung unten.

---

## Schritt 1: Node.js herunterladen

### 1.1 Zur Download-Seite navigieren

1. Öffne deinen Browser
2. Gehe zu: **https://nodejs.org**
3. Du siehst zwei Download-Optionen:

| Version | Beschreibung | Empfehlung |
|---------|--------------|------------|
| **LTS** (Long Term Support) | Stabile Version mit langem Support | **Diese wählen!** |
| Current | Neueste Features, weniger stabil | Nicht empfohlen |

### 1.2 Die richtige Version wählen

Klicke auf den **LTS-Button** (grün markiert). Die genaue Versionsnummer ändert sich regelmäßig - **wichtig ist nur, dass du LTS wählst**, nicht "Current".

> **Hinweis:** Welche LTS-Version aktuell ist, siehst du direkt auf nodejs.org. Die Versionsnummer (z.B. 20.x, 22.x, 24.x) spielt für diesen Kurs keine Rolle - Hauptsache LTS.

Der Download startet automatisch:
- **Windows:** `node-vXX.X.X-x64.msi`
- **Mac:** `node-vXX.X.X.pkg`
- **Linux:** Siehe spezielle Anweisungen unten

---

## Schritt 2: Installation durchführen

### Windows

1. **Doppelklick** auf die heruntergeladene `.msi`-Datei
2. Im Installer-Fenster:
   - Klicke **"Next"**
   - Akzeptiere die Lizenzvereinbarung (Häkchen setzen) → **"Next"**
   - Installationsort belassen (Standard ist ok) → **"Next"**
   - Bei "Custom Setup": Alles belassen → **"Next"**
   - Bei "Tools for Native Modules": Häkchen ist optional (für diesen Kurs nicht nötig) → **"Next"**
   - Klicke **"Install"**
   - Warte, bis die Installation abgeschlossen ist
   - Klicke **"Finish"**

### Mac

1. **Doppelklick** auf die heruntergeladene `.pkg`-Datei
2. Im Installer-Fenster:
   - Klicke **"Fortfahren"**
   - Akzeptiere die Lizenzvereinbarung → **"Fortfahren"** → **"Akzeptieren"**
   - Klicke **"Installieren"**
   - Gib dein Mac-Passwort ein, wenn gefragt
   - Warte, bis die Installation abgeschlossen ist
   - Klicke **"Schließen"**

### Linux (Ubuntu/Debian)

Es gibt zwei Möglichkeiten:

**Option A: NodeSource (einfach)**

Öffne das Terminal und führe folgende Befehle aus:

```bash
# Node.js Repository hinzufügen (für aktuelle LTS-Version)
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -

# Node.js und npm installieren
sudo apt-get install -y nodejs

# Überprüfen
node --version
npm --version
```

> **Sicherheitshinweis:** Das Script lädt und führt Code von NodeSource aus. Das ist eine vertrauenswürdige Quelle, aber du solltest dir bewusst sein, dass `curl | sudo bash` Code mit Root-Rechten ausführt. Prüfe im Zweifel erst das Script.

**Option B: nvm (empfohlen für Entwickler)**

Mit nvm (Node Version Manager) kannst du Node-Versionen einfach wechseln:

```bash
# nvm installieren
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Terminal neu starten, dann:
nvm install --lts
nvm use --lts

# Überprüfen
node --version
npm --version
```

**Vorteil von nvm:** Du kannst mehrere Node-Versionen parallel haben und einfach wechseln.

---

## Schritt 3: Installation überprüfen

### 3.1 Terminal/Eingabeaufforderung öffnen

**Windows:**
- Drücke `Windows-Taste + R`
- Tippe `cmd` und drücke Enter
- ODER: Suche nach "Eingabeaufforderung" im Startmenü
- ODER: Suche nach "PowerShell" im Startmenü

**Mac:**
- Drücke `Cmd + Leertaste`
- Tippe "Terminal" und drücke Enter
- ODER: Gehe zu Programme → Dienstprogramme → Terminal

**Linux:**
- Drücke `Strg + Alt + T`
- ODER: Suche nach "Terminal" in deinen Anwendungen

### 3.2 Versionen prüfen

Gib folgende Befehle ein und drücke nach jedem Enter:

```bash
node --version
```

**Erwartete Ausgabe:** Eine aktuelle LTS-Versionsnummer, z.B. `v20.x.x`, `v22.x.x` oder `v24.x.x`

```bash
npm --version
```

**Erwartete Ausgabe:** Eine aktuelle npm-Version (die Major-Version variiert je nach Node-Version, z.B. `10.x.x` oder `11.x.x`)

### 3.3 Erfolgreiche Installation

Wenn beide Befehle Versionsnummern ausgeben, war die Installation erfolgreich!

**Beispiel einer erfolgreichen Prüfung:**

```
C:\Users\Max> node --version
v22.11.0

C:\Users\Max> npm --version
10.9.0
```

> **Wichtig:** Die genauen Versionsnummern können bei dir anders sein - das ist OK! Hauptsache, es erscheint eine Nummer und kein Fehler.

---

## Schritt 4: Fehlerbehebung

### Problem: "node wird nicht erkannt" / "command not found"

**Ursache:** Der Pfad zu Node.js ist nicht in den Umgebungsvariablen.

**Lösung Windows:**
1. Schließe alle Terminal-Fenster
2. Starte den Computer neu
3. Öffne ein neues Terminal und versuche es erneut

Falls das nicht hilft:
1. Rechtsklick auf "Dieser PC" → "Eigenschaften"
2. Klicke auf "Erweiterte Systemeinstellungen"
3. Klicke auf "Umgebungsvariablen"
4. Unter "Systemvariablen" wähle "Path" und klicke "Bearbeiten"
5. Klicke "Neu" und füge hinzu: `C:\Program Files\nodejs\`
6. Klicke "OK" auf allen Fenstern
7. Öffne ein neues Terminal und teste erneut

**Lösung Mac/Linux:**
1. Schließe das Terminal
2. Öffne ein neues Terminal
3. Falls das nicht hilft, führe aus:
   ```bash
   # Für Bash
   echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc

   # Für Zsh (Standard auf neueren Macs)
   echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

### Problem: Alte Node.js-Version installiert

**Lösung (empfohlen):**

In den meisten Fällen kannst du einfach die **neue LTS-Version installieren** - der Installer überschreibt die alte Version automatisch sauber.

**Falls das nicht klappt:**

- **Windows:** Systemsteuerung → Programme → Node.js deinstallieren, dann neu installieren
- **Mac:** Lade den aktuellen LTS-Installer von nodejs.org herunter und führe ihn aus. Der Installer ersetzt die alte Version.
- **Linux (mit nvm):** `nvm install --lts` installiert die neue Version parallel. Mit `nvm alias default lts/*` setzt du sie als Standard.

### Problem: npm-Berechtigungsfehler (Mac/Linux)

**Lösung:**
```bash
# npm-Verzeichnis mit korrekten Berechtigungen erstellen
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'

# Für Bash:
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

# Für Zsh (Standard auf neueren Macs):
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.zshrc
source ~/.zshrc
```

> **Welche Shell hast du?** Tippe `echo $SHELL` im Terminal. Wenn `/bin/zsh` erscheint, nutze `.zshrc`. Bei `/bin/bash` nutze `.bashrc`.

### Häufige Fehlerbilder und ihre Lösungen

| Fehler | Ursache | Lösung |
|--------|---------|--------|
| `'node' is not recognized` / `command not found` | Terminal nach Installation nicht neu geöffnet | **Alle** Terminal-Fenster schließen und neu öffnen |
| Download bricht ab / sehr langsam | Proxy, VPN oder Firewall blockiert | VPN deaktivieren, ggf. IT-Admin fragen |
| `npm ERR! code EACCES` | Berechtigungsproblem | Siehe "npm-Berechtigungsfehler" oben |
| `npm run dev` funktioniert nicht | Nicht im Projektordner | Mit `cd projektname` in den richtigen Ordner wechseln |
| PowerShell: `cannot be loaded because running scripts is disabled` | Windows Execution Policy | PowerShell: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (ohne Admin) |

---

## Schritt 5: Erste Schritte mit Node.js

### 5.1 Node.js interaktiv testen (REPL)

Öffne das Terminal und tippe:

```bash
node
```

Du siehst jetzt einen interaktiven JavaScript-Interpreter (ähnlich wie `python` im Terminal):

```
Welcome to Node.js v20.10.0.
Type ".help" for more information.
>
```

Probiere einige JavaScript-Befehle:

```javascript
> console.log('Hallo Welt!')
Hallo Welt!

> 2 + 2
4

> const name = 'Max'
> `Hallo ${name}!`
'Hallo Max!'

> .exit
```

Mit `.exit` oder `Strg + C` (zweimal) verlässt du den REPL.

### 5.2 Eine JavaScript-Datei ausführen

1. Erstelle eine neue Datei `test.js` mit folgendem Inhalt:

```javascript
// test.js
const name = 'Teilnehmer';
const kurs = 'Webentwicklung';

console.log(`Hallo ${name}!`);
console.log(`Willkommen zum ${kurs}-Kurs.`);
console.log('Node.js funktioniert!');
```

2. Öffne das Terminal im gleichen Verzeichnis
3. Führe aus:

```bash
node test.js
```

**Ausgabe:**
```
Hallo Teilnehmer!
Willkommen zum Webentwicklung-Kurs.
Node.js funktioniert!
```

---

## Schritt 6: npm verstehen

### 6.1 Was ist npm?

npm ist der Package Manager für JavaScript. Er funktioniert ähnlich wie `pip` in Python:

| npm | pip | Beschreibung |
|-----|-----|--------------|
| `npm install paket` | `pip install paket` | Paket installieren |
| `npm install` | `pip install -r requirements.txt` | Alle Abhängigkeiten installieren |
| `package.json` | `requirements.txt` | Liste der Abhängigkeiten |
| `node_modules/` | `venv/lib/site-packages/` | Installierte Pakete |

### 6.2 Wichtige npm-Befehle

```bash
# Hilfe anzeigen
npm help

# Neues Projekt initialisieren (erstellt package.json)
npm init

# Paket installieren (lokal im Projekt)
npm install paketname

# Paket global installieren (systemweit)
npm install -g paketname

# Alle Abhängigkeiten aus package.json installieren
npm install

# Script aus package.json ausführen
npm run scriptname

# Entwicklungsserver starten (typisch für React)
npm run dev
```

### 6.3 Vergleich: Python-Projekt vs. JavaScript-Projekt

**Python-Projekt:**
```
mein-projekt/
├── venv/                 # Virtuelle Umgebung
├── requirements.txt      # Abhängigkeiten
├── main.py              # Hauptdatei
└── ...
```

**JavaScript/React-Projekt:**
```
mein-projekt/
├── node_modules/         # Installierte Pakete
├── package.json          # Abhängigkeiten + Scripts
├── package-lock.json     # Exakte Versionen
├── src/                  # Quellcode
│   └── App.jsx          # React-Komponente
└── ...
```

---

## Schritt 7: VS Code Erweiterungen (Optional)

Für eine bessere Entwicklungserfahrung empfehlen wir folgende VS Code Erweiterungen:

### Empfohlene Erweiterungen

| Erweiterung | Beschreibung |
|-------------|--------------|
| **ESLint** | JavaScript/React Code-Qualität prüfen |
| **Prettier** | Code automatisch formatieren |
| **ES7+ React/Redux/React-Native snippets** | Hilfreiche Code-Schnipsel für React |
| **Auto Rename Tag** | HTML/JSX Tags automatisch umbenennen |

> **Hinweis zu farbigen Klammern:** VS Code hat diese Funktion jetzt **nativ eingebaut**. Du musst keine Extension mehr installieren! Falls du es aktivieren möchtest: Einstellungen → suche nach "bracket pair" → aktiviere "Bracket Pair Colorization".

### Installation in VS Code

1. Öffne VS Code
2. Drücke `Strg + Shift + X` (Windows) oder `Cmd + Shift + X` (Mac)
3. Suche nach der Erweiterung
4. Klicke "Install"

---

## Zusammenfassung

### Was du installiert hast:

| Tool | Zweck | Befehl zum Prüfen |
|------|-------|-------------------|
| **Node.js** | JavaScript außerhalb des Browsers ausführen | `node --version` |
| **npm** | JavaScript-Pakete verwalten | `npm --version` |

### Wichtige Konzepte:

- **Node.js** ist wie `python` - ein Interpreter/Runtime
- **npm** ist wie `pip` - ein Package Manager
- **package.json** ist wie `requirements.txt` - listet Abhängigkeiten
- **node_modules/** ist wie `venv/site-packages/` - enthält installierte Pakete

### Nächste Schritte:

Mit Node.js und npm installiert, bist du bereit für:
1. JavaScript-Dateien direkt ausführen (`node datei.js`)
2. JavaScript-Pakete installieren (`npm install paket`)
3. React-Projekte erstellen und starten

---

## Checkliste

Bevor du fortfährst, stelle sicher:

- [ ] `node --version` zeigt eine Versionsnummer (egal welche LTS-Version)
- [ ] `npm --version` zeigt eine Versionsnummer
- [ ] Du kannst `node` im Terminal starten und JavaScript ausführen
- [ ] Du verstehst den Unterschied zwischen Node.js und npm

**Geschafft?** Dann bist du bereit für die JavaScript-Übungen!
