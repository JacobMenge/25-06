# Git und Python - Versionierung Basics

## Übersicht

In dieser Übung lernst du:
- **Git installieren und einrichten** - Die Entwicklungsumgebung vorbereiten
- **Repository-Konzept** - Was ist ein Repository und wie funktioniert es
- **Grundlegender Workflow** - Status, Add, Commit verstehen
- **Mit Remote arbeiten** - Clone, Push, Pull verwenden
- **Python-Code versionieren** - Praktische Anwendung mit echten Code-Beispielen

---

## Übersicht nach Schwierigkeitsgrad

### GRUNDLAGEN

Diese Übungen decken die fundamentalen Git-Konzepte ab:

- **Übung 1**: Git installieren und konfigurieren
- **Übung 2**: Erstes Repository erstellen und verstehen
- **Übung 3**: Der Git-Workflow - Änderungen tracken
- **Übung 4**: Mit GitHub arbeiten - Remote Repository
- **Übung 5**: Kompletter Workflow mit Python-Datei

**Empfehlung:** Mache alle Grundlagen-Übungen in Reihenfolge. Git lernt man am besten durch praktisches Üben!

### FORTGESCHRITTEN

Diese Übung kombiniert alle Konzepte in einem kleinen Projekt:

- **Bonus-Übung**: Mini-Python-Projekt mit Git versionieren

**Empfehlung:** Diese Übung setzt voraus, dass du die Grundlagen verstanden hast. Sie simuliert einen realistischen Entwicklungs-Workflow.

---

## Was ist Git?

### Die Grundidee

Stell dir vor, du schreibst an einem Python-Programm. Du machst Änderungen, und plötzlich funktioniert etwas nicht mehr. **Wie kommst du zur letzten funktionierenden Version zurück?**

Oder: Du arbeitest im Team an einem Projekt. **Wie können mehrere Personen gleichzeitig am gleichen Code arbeiten, ohne sich gegenseitig zu überschreiben?**

**Git löst diese Probleme!**

Git ist ein **Versionskontrollsystem** - es:
- Speichert die Geschichte deines Codes (wie ein Zeitstrahl)
- Ermöglicht Rücksprünge zu früheren Versionen
- Macht Zusammenarbeit möglich
- Zeigt, wer was wann geändert hat

### Warum Git lernen?

1. **Sicherheit**: Keine Angst mehr vor Änderungen - du kannst immer zurück
2. **Professionell**: Alle Entwickler nutzen Git
3. **Zusammenarbeit**: Standard für Team-Projekte
4. **Portfolio**: GitHub zeigt deine Projekte
5. **Backup**: Code ist sicher gespeichert

### Git vs. GitHub - Was ist der Unterschied?

**Git:**
- Software auf deinem Computer
- Verwaltet deine Code-Versionen lokal
- Funktioniert komplett offline

**GitHub:**
- Website im Internet
- Speichert deine Repositories online
- Ermöglicht Zusammenarbeit
- Wie "Google Drive für Code"

**Analogie:**
- Git = Word (das Programm auf deinem Computer)
- GitHub = OneDrive (der Online-Speicher)

---

## Teil 1: Installation und Setup

### Empfohlene Tools für Windows 11

Für diese Übung empfehlen wir folgendes Setup (besonders für Anfänger):

**1. Git for Windows**
- Herunterladen von [git-scm.com](https://git-scm.com)
- Installiere mit Standard-Einstellungen
- Enthält automatisch:
  - Git Bash (Linux-ähnliche Kommandozeile)
  - Git Credential Manager (GCM) - Login via Browser, kein kompliziertes Passwort nötig!

**2. Visual Studio Code (VS Code)**
- Kostenloser Code-Editor von Microsoft
- Herunterladen von [code.visualstudio.com](https://code.visualstudio.com)
- Hat eingebaute Git-Unterstützung (keine Kommandozeile nötig!)
- Optional: Extension "GitHub Pull Requests and Issues"

**3. GitHub Desktop (Alternative zur Kommandozeile)**
- Grafische Oberfläche für Git
- Herunterladen von [desktop.github.com](https://desktop.github.com)
- Perfekt für Einsteiger, die die Kommandozeile scheuen

### Git installieren (Windows 11 – empfohlen)

1) **Git for Windows** von [git-scm.com](https://git-scm.com) → Setup mit **Standard-Einstellungen** (enthält Git Bash + Git Credential Manager).
2) **VS Code** von [code.visualstudio.com](https://code.visualstudio.com) → Standardinstallation.
3) [Optional] **GitHub Desktop** von [desktop.github.com](https://desktop.github.com).

**Nach der Installation prüfen:**
- VS Code öffnen → **Strg + `** (Backtick, Taste links neben der 1) → oben im Terminal **Git Bash** wählen
- `git --version` ausführen (z. B. `git version 2.x.x`)

Du solltest etwas sehen wie: `git version 2.45.0`

**Wichtig:** Die genaue Versionsnummer ist egal, solang eine Version angezeigt wird.

### Git Bash als Standard-Terminal in VS Code

1. VS Code → **Strg + `** (Backtick)
2. Terminal-Dropdown (❯) rechts → **Select Default Profile** → **Git Bash**
3. **+** (neues Terminal) → jetzt läuft Git in Git Bash

---

## Übung 1: Git installieren und konfigurieren

**Schwierigkeitsgrad: GRUNDLAGEN**

**Aufgabe:**

1. **Git installieren** (falls noch nicht geschehen)
   - Befolge die Anleitung oben für dein Betriebssystem
   - Überprüfe die Installation mit `git --version`

2. **Git konfigurieren** (WICHTIG - nur einmal nötig!)
   
   Öffne Git Bash und führe aus:
   
   ```bash
   git config --global user.name "Dein Name"
   git config --global user.email "deine@email.de"
   git config --global init.defaultBranch main
   git config --global core.autocrlf true
   git config --global core.editor "code --wait"
   ```
   
   Überprüfe die Konfiguration: `git config --list`

3. **Arbeitsverzeichnis erstellen**
   - Erstelle einen Ordner `git-python-uebung` auf deinem Desktop
   - **Option A (VS Code):** File → Open Folder → Ordner auswählen
   - **Option B (Terminal):** Navigiere in diesen Ordner

**Hinweise:**
- Die E-Mail sollte die sein, die du später für GitHub nutzt
- `--global` bedeutet: Diese Einstellungen gelten für alle deine Git-Repositories
- `init.defaultBranch main` sorgt dafür, dass neue Repositories "main" statt "master" verwenden
- `core.autocrlf true` verhindert Probleme mit Zeilenenden unter Windows
- Du musst diese Konfiguration nur **einmal** machen!

<details>
<summary>Schritt-für-Schritt Lösung anzeigen</summary>

```bash
# Schritt 1: Version überprüfen
git --version
# Ausgabe: git version 2.x.x

# Schritt 2: Git konfigurieren (alle Befehle auf einmal)
git config --global user.name "Max Mustermann"
git config --global user.email "max.mustermann@example.com"
git config --global init.defaultBranch main
git config --global core.autocrlf true
git config --global core.editor "code --wait"

# Schritt 3: Konfiguration überprüfen
git config --list
# Du solltest sehen:
# user.name=Max Mustermann
# user.email=max.mustermann@example.com
# init.defaultbranch=main
# core.autocrlf=true
# core.editor=code --wait
# ... weitere Einstellungen ...

# Spezifische Werte anzeigen
git config user.name
git config user.email

# Schritt 4: Arbeitsverzeichnis erstellen

# === OPTION A: Mit VS Code (empfohlen für Anfänger) ===
# 1. VS Code öffnen
# 2. File → Open Folder
# 3. Desktop navigieren → "New Folder" klicken
# 4. Name: git-python-uebung
# 5. Ordner öffnen
# 6. Terminal in VS Code öffnen (Strg + `, Backtick)

# === OPTION B: Im Git Bash Terminal ===
cd ~/Desktop
mkdir git-python-uebung
cd git-python-uebung

# Aktuellen Pfad anzeigen
pwd
# Sollte den Pfad zu deinem Ordner zeigen
```

**Erklärungen:**

```
1. GIT --VERSION:
   - Zeigt installierte Git-Version
   - Bestätigt erfolgreiche Installation
   - Version muss nicht aktuellste sein

2. GIT CONFIG:
   - Konfiguriert Git für deinen Computer
   - --global: Gilt für alle Projekte
   - --local: Nur für aktuelles Projekt (ohne --global)

3. USER.NAME UND USER.EMAIL:
   - Wird bei jedem Commit gespeichert
   - Zeigt, wer Änderungen gemacht hat
   - Bei GitHub: E-Mail sollte übereinstimmen

4. GIT CONFIG --LIST:
   - Zeigt alle Einstellungen
   - Kann lang sein - das ist normal
   - Nur user.name und user.email sind jetzt wichtig

5. ARBEITSVERZEICHNIS:
   - Git arbeitet mit Ordnern
   - Jedes Projekt = ein Ordner
   - Du musst im richtigen Ordner sein!

6. CD (CHANGE DIRECTORY):
   - Navigiert zwischen Ordnern
   - cd ..     → Ein Ordner höher
   - cd name   → In Ordner "name"
   - pwd       → Zeigt aktuellen Pfad

7. MKDIR (MAKE DIRECTORY):
   - Erstellt neuen Ordner
   - mkdir mein-ordner

8. WARUM KONFIGURATION WICHTIG IST:
   - Git "signiert" jeden Commit mit Name/E-Mail
   - Zeigt Authoren-Historie
   - Wichtig für Team-Arbeit
   - Auf GitHub: Commits werden deinem Profil zugeordnet
```

**Typische Fehler:**

```
❌ FEHLER: "git: command not found"
   → Git ist nicht installiert oder nicht im PATH
   → Lösung: Git neu installieren, Terminal neu starten

❌ FEHLER: Falsche E-Mail gesetzt
   → Später auf GitHub stimmen Commits nicht überein
   → Lösung: Neu konfigurieren mit richtigem config-Befehl

❌ FEHLER: Nicht im richtigen Ordner
   → Git-Befehle funktionieren nicht wie erwartet
   → Lösung: Mit pwd prüfen, mit cd navigieren

❌ FEHLER: Leerzeichen im Namen ohne Anführungszeichen
   → git config --global user.name Max Mustermann (Falsch)
   → git config --global user.name "Max Mustermann" (Richtig)
```

</details>

---

### Selbstcheck: Teil 1

1. Warum braucht Git deinen Namen und E-Mail?
2. Was bedeutet `--global` bei git config?
3. Wie überprüfst du, ob Git richtig installiert ist?

<details>
<summary>Antworten anzeigen</summary>

1. Jeder Commit wird mit Autor und E-Mail gespeichert - zeigt, wer was geändert hat.
2. Die Einstellung gilt für alle Repositories auf deinem Computer, nicht nur für eins.
3. Mit `git --version` im Terminal - es sollte eine Versionsnummer erscheinen.

</details>

---

## Intermezzo: VS Code und GitHub Desktop - Alternativen zur Kommandozeile

Bevor wir weitermachen: Du kannst Git auf **drei Arten** nutzen:

1. **Terminal/Git Bash** - Kommandozeile (was wir hauptsächlich zeigen)
2. **VS Code** - Grafische Oberfläche im Editor
3. **GitHub Desktop** - Dedizierte Git-App

**Empfehlung für Anfänger:** Lerne zuerst die Kommandozeile (Git Bash), um die Konzepte zu verstehen. Danach kannst du zu VS Code oder GitHub Desktop wechseln.

### Git in VS Code nutzen (Quick Start)

VS Code hat Git bereits eingebaut! So funktioniert es:

**1. Repository initialisieren:**
- Ordner in VS Code öffnen (File → Open Folder)
- Linke Seitenleiste: **Source Control** Icon (drei verbundene Punkte)
- Button: **"Initialize Repository"** klicken
- Fertig! `.git` Ordner wurde erstellt

**2. Änderungen committen:**
- Dateien ändern → Änderungen erscheinen in Source Control
- Häkchen neben Datei = **Staging** (entspricht `git add`)
- Commit-Message oben eingeben
- **"Commit"** Button klicken (entspricht `git commit`)

**3. Mit GitHub verbinden:**
- Nach erstem Commit erscheint: **"Publish Branch"**
- Klicken → Browser öffnet sich für GitHub Login
- Repository wird automatisch auf GitHub erstellt!

**4. Weitere Änderungen synchronisieren:**
- **Sync** Button (Cloud-Symbol oben) = Pull + Push in einem
- Oder **"..."** Menü → Pull / Push einzeln

**Wichtige VS Code Git-Symbole:**
- `M` = Modified (geändert)
- `U` = Untracked (neu, noch nicht getrackt)
- `A` = Added (zum Commit hinzugefügt)
- `D` = Deleted (gelöscht)

### Git mit GitHub Desktop (Quick Start)

GitHub Desktop ist eine benutzerfreundliche Alternative:

**1. Lokales Repository verbinden:**
- File → Add local repository
- Ordner `git-python-uebung` auswählen
- **"Publish repository"** → GitHub-Konto auswählen
- Public/Private wählen

**2. Workflow:**
- **Changes** Tab: Zeigt alle Änderungen
- Häkchen = Staging (automatisch alle ausgewählt)
- **Summary** eingeben (Commit-Message)
- **"Commit to main"** klicken
- **"Push origin"** Button klicken

**3. Änderungen holen:**
- **"Fetch origin"** (prüft auf Updates)
- **"Pull origin"** (lädt Updates herunter)

**Für diese Übung:** Wir zeigen hauptsächlich Terminal-Befehle, weil du so die Konzepte besser verstehst. Aber alle Übungen funktionieren auch mit VS Code oder GitHub Desktop!

### VS Code: 0-auf-100 ohne Terminal

1. Ordner öffnen → **Source Control** → **Initialize Repository**
2. `.gitignore` + `.gitattributes` anlegen und speichern
3. Änderungen: Häkchen (Stage) → Commit-Nachricht → **Commit**
4. **Publish Branch** → Browser-Login (Git Credential Manager) → fertig
5. Sync-Button (Cloud) = Pull + Push

### GitHub Desktop: GUI-Alternative

1. **File → Add local repository...** (bestehenden Ordner hinzufügen)
2. **Publish repository** (Public/Private wählen)
3. **Changes** → Summary → **Commit to main** → **Push origin**
4. **Fetch/Pull origin** vor neuem Push

---

## Teil 2: Repository-Konzept

### Was ist ein Repository?

Ein **Repository** (oft "Repo" abgekürzt) ist ein Projekt mit Git-Versionierung.

**Stell dir vor:**
- Ein normaler Ordner mit Code-Dateien
- PLUS ein versteckter `.git` Ordner
- Dieser `.git` Ordner speichert die gesamte Historie

**Analogie:**
Ein Buch mit allen Entwürfen:
- Der Ordner = Das aktuelle Kapitel
- `.git` = Alle vorherigen Versionen des Kapitels

### Repository initialisieren

Mit `git init` wird ein Ordner zum Repository:

```bash
mkdir mein-projekt
cd mein-projekt
git init
# Ausgabe: "Initialized empty Git repository in ..."
```

**Was passiert?**
- `.git` Ordner wird erstellt (versteckt)
- Git kann jetzt Änderungen tracken
- Der Ordner ist jetzt ein Repository

**Wichtig:**
- `git init` nur einmal pro Projekt!
- Nicht in Ordnern mit bereits vorhandenem `.git` ausführen
- `.git` niemals manuell löschen (gesamte Historie geht verloren)

### Repository-Status prüfen

```bash
git status
```

**Zeigt:**
- Welche Dateien geändert wurden
- Welche Dateien "staged" sind (bereit für Commit)
- Welcher Branch aktiv ist
- Ob du mit Remote synchron bist

**Tipp:** `git status` ist der wichtigste Befehl! Nutze ihn oft, um zu sehen, wo du stehst.

---

## Übung 2: Erstes Repository erstellen

**Schwierigkeitsgrad: GRUNDLAGEN**

**Aufgabe:**

1. **Repository initialisieren**
   - Du solltest bereits im `git-python-uebung` Ordner sein (oder in VS Code geöffnet haben)
   - **Terminal:** Initialisiere ein Git-Repository mit `git init`
   - **VS Code:** Source Control → "Initialize Repository"
   - Überprüfe mit `git status` (Terminal) oder Source Control Tab (VS Code)

2. **.gitignore erstellen (WICHTIG - vor dem ersten Commit!)**
   - Erstelle eine Datei `.gitignore` im Projekt-Ordner
   - Füge folgende Zeilen ein:
     ```
     __pycache__/
     *.pyc
     *.pyo
     *.pyd
     env/
     venv/
     ```
   - Diese Datei sagt Git, welche Dateien NICHT getrackt werden sollen

3. **.gitattributes erstellen (Windows-spezifisch)**
   - Erstelle eine Datei `.gitattributes` im Projekt-Ordner
   - Füge folgende Zeilen ein:
     ```
     *.py text eol=lf
     *.md text eol=lf
     ```
   - Verhindert Probleme mit unterschiedlichen Zeilenenden (Windows vs. Linux/Mac)

4. **Konfigurationsdateien committen**
   - Prüfe Status: `git status`
   - Stage die Dateien: `git add .gitignore .gitattributes`
   - Commit: `git commit -m "Initialer Commit mit Projektkonfiguration"`

5. **Erste Python-Datei erstellen**
   - Erstelle eine Datei `hello.py`
   - Schreibe hinein: `print("Hallo Git!")`
   - Prüfe erneut mit `git status`

6. **Verstehen, was Git sieht**
   - Git sollte die neue Datei als "untracked" anzeigen
   - Das bedeutet: Git kennt die Datei, trackt sie aber noch nicht

**Hinweise:**
- **.gitignore** ist wichtig! Verhindert, dass Python-Cache und virtuelle Umgebungen ins Repository kommen
- **.gitattributes** verhindert Zeilenenden-Chaos zwischen Windows und Linux/Mac
- Die Konfigurationsdateien sollten im **ersten Commit** sein, bevor du Code hinzufügst
- Du kannst die Dateien mit VS Code, Notepad++ oder im Terminal erstellen
- Dateien, die mit `.` beginnen, sind auf Windows evtl. versteckt - aber Git sieht sie!

<details>
<summary>Schritt-für-Schritt Lösung anzeigen</summary>

```bash
# Schritt 1: Im richtigen Ordner sein
pwd
# Sollte .../git-python-uebung zeigen

# Schritt 2: Repository initialisieren
git init
# Ausgabe: Initialized empty Git repository in /pfad/zu/git-python-uebung/.git/

# WICHTIG: Durch init.defaultBranch main ist der Branch bereits "main"
# KEIN "git branch -M main" nötig!

# Schritt 3: Status prüfen
git status
# Ausgabe:
# On branch main
# No commits yet
# nothing to commit (create/copy files and use "git add" to track)

# Schritt 4: .gitignore erstellen (WICHTIG - vor dem ersten Code!)
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
*.pyo
*.pyd
env/
venv/
EOF

# Oder in VS Code: Neue Datei erstellen, Namen .gitignore, Inhalt einfügen

# Inhalt prüfen
cat .gitignore

# Schritt 5: .gitattributes erstellen (Windows-Zeilenenden)
cat > .gitattributes << 'EOF'
*.py text eol=lf
*.md text eol=lf
EOF

# Inhalt prüfen
cat .gitattributes

# Schritt 6: Status nach Konfigurationsdateien
git status
# Ausgabe:
# Untracked files:
#   .gitattributes
#   .gitignore

# Schritt 7: Konfigurationsdateien committen
git add .gitignore .gitattributes
git status
# Dateien sind jetzt grün (staged)

git commit -m "Initialer Commit mit Projektkonfiguration"
# Ausgabe:
# [main (root-commit) a1b2c3d] Initialer Commit mit Projektkonfiguration
#  2 files changed, X insertions(+)
#  create mode 100644 .gitattributes
#  create mode 100644 .gitignore

# Schritt 8: Python-Datei erstellen
# Option A: Mit Terminal
echo 'print("Hallo Git!")' > hello.py

# Option B: Mit VS Code
code hello.py
# Dann in VS Code: print("Hallo Git!") eingeben und speichern

# Datei anschauen (optional)
cat hello.py
# Ausgabe: print("Hallo Git!")

# Schritt 9: Status erneut prüfen
git status
# Ausgabe:
# On branch main
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         hello.py
# nothing added to commit but untracked files present (use "git add" to track)

# Versteckte Dateien anzeigen (optional)
ls -la
# Oder in VS Code: Explorer zeigt .gitignore und .gitattributes
```

**Erklärungen:**

```
1. GIT INIT:
   - Erstellt .git Ordner (versteckt)
   - Initialisiert leeres Repository
   - Nur EINMAL pro Projekt nötig
   - Macht den Ordner zu einem "Git Repository"
   - Branch heißt automatisch "main" (wegen unserer globalen Konfiguration)

2. .GIT ORDNER:
   - Enthält komplette Git-Historie
   - Normalerweise versteckt
   - NIEMALS manuell bearbeiten oder löschen!
   - Zu sehen mit: ls -a (zeigt versteckte Dateien)

3. .GITIGNORE - WARUM WICHTIG:
   - Sagt Git, welche Dateien NICHT getrackt werden sollen
   - __pycache__/ → Python-Cache-Ordner (wird automatisch erstellt)
   - *.pyc → Kompilierte Python-Dateien
   - env/, venv/ → Virtuelle Python-Umgebungen (zu groß für Git!)
   
   WICHTIG: Diese Dateien ändern sich ständig und sind nicht Teil deines Codes
   → Sollten NICHT ins Repository
   → Jeder erstellt sie lokal selbst

4. .GITATTRIBUTES - WINDOWS-PROBLEM:
   - Windows nutzt CRLF (\r\n) für Zeilenenden
   - Linux/Mac nutzen LF (\n) für Zeilenenden
   - Kann zu Problemen führen beim gemeinsamen Arbeiten
   
   *.py text eol=lf
   → Sagt Git: Python-Dateien immer mit LF speichern
   → Egal ob auf Windows, Mac oder Linux entwickelt wird
   → Team arbeitet konfliktfrei zusammen!
   
   core.autocrlf true (in config)
   → Git konvertiert automatisch beim Checkout/Commit
   → Auf Windows siehst du CRLF, im Repo ist LF

5. REIHENFOLGE WICHTIG:
   1. git init
   2. .gitignore + .gitattributes erstellen
   3. Diese ZUERST committen
   4. Dann Code hinzufügen
   
   Warum? Vermeidet, dass versehentlich Cache-Dateien committet werden!

6. GIT STATUS - ERSTE AUSGABE:
   "On branch main"
   → Du bist auf dem Haupt-Branch
   → Früher "master", heute "main"
   → Dank init.defaultBranch main Konfiguration
   
   "No commits yet"
   → Noch keine Versionen gespeichert
   
   "nothing to commit"
   → Keine Dateien zum Versionieren vorhanden

7. PYTHON-DATEI ERSTELLEN:
   - Kann mit jedem Editor gemacht werden
   - echo 'code' > datei.py ist eine Terminal-Alternative
   - > überschreibt Datei (Vorsicht!)
   - >> würde anhängen
   
   VS Code Alternative:
   - Neue Datei erstellen (Strg+N)
   - Code eingeben
   - Speichern als hello.py

8. GIT STATUS - NACH DATEI-ERSTELLUNG:
   "Untracked files:"
   → Git sieht die Datei, trackt sie aber nicht
   
   "use 'git add <file>...'"
   → Git sagt dir, was als nächstes zu tun ist
   
   hello.py wird rot angezeigt (in farbigen Terminals)
   → Bedeutet: Nicht getrackt

9. UNTRACKED:
   - Git SIEHT die Datei
   - Git SPEICHERT sie aber noch nicht
   - Wir müssen sie mit "git add" zum Tracking hinzufügen
   - Das kommt in der nächsten Übung!

10. VERSTECKTE DATEIEN:
    - Dateien mit . am Anfang sind "versteckt"
    - Windows Explorer zeigt sie evtl. nicht
    - Git und VS Code sehen sie trotzdem
    - Im Terminal: ls -la zeigt alle Dateien

11. WARUM ZWEI KONFIGURATIONSDATEIEN?
    .gitignore: Lokal (was nicht ins Repo soll)
    .gitattributes: Team-weit (wie Dateien behandelt werden)
    
    Beide sollten IMMER im Repo sein
    → Andere Teammitglieder profitieren auch
    → Vermeidet viele Probleme

12. CODE > .GITIGNORE UND ÖFFNEN:
    - In VS Code: Neue Datei wird sofort erstellt
    - Code-Befehl im Terminal öffnet VS Code
    - Praktisch für schnelles Editieren
```

**Was wir gelernt haben:**

```
✓ Ein Repository ist ein Ordner mit .git
✓ git init macht einen Ordner zum Repository
✓ git status zeigt den aktuellen Zustand
✓ "Untracked" bedeutet: Git sieht die Datei, speichert sie aber nicht
✓ Git gibt hilfreiche Hinweise, was als nächstes zu tun ist
```

</details>

---

### Selbstcheck: Teil 2

1. Was macht `git init`?
2. Was bedeutet "untracked file"?
3. Warum solltest du den `.git` Ordner nicht löschen?

<details>
<summary>Antworten anzeigen</summary>

1. Erstellt ein Git-Repository im aktuellen Ordner (fügt `.git` Ordner hinzu).
2. Git kennt die Datei, aber verfolgt ihre Änderungen noch nicht - sie muss erst mit `git add` hinzugefügt werden.
3. Der `.git` Ordner enthält die GESAMTE Historie deines Projekts - wenn du ihn löschst, ist alles weg!

</details>

---

## Teil 3: Der Git-Workflow

### Die drei Bereiche

Git arbeitet mit drei Bereichen:

```
Working Directory  →  Staging Area  →  Repository
(Arbeitsbereich)      (Vorbereitung)    (Geschichte)
```

**1. Working Directory (Arbeitsverzeichnis):**
- Deine Dateien, wie du sie siehst
- Wo du arbeitest und Änderungen machst

**2. Staging Area (Bereitstellung):**
- Vorschau für den nächsten Commit
- "Ausgewählte" Änderungen, die gespeichert werden sollen
- Wie ein Einkaufswagen vor der Kasse

**3. Repository (Versionsspeicher):**
- Die dauerhafte Geschichte
- Alle Commits
- Wie ein Archiv

### Der Workflow in 4 Schritten

```bash
# 1. Status prüfen - Wo stehe ich?
git status

# 2. Änderungen zur Staging Area hinzufügen
git add dateiname.py
# Oder alle Änderungen:
git add .

# 3. Commit erstellen - Änderungen dauerhaft speichern
git commit -m "Beschreibung der Änderung"

# 4. Erneut Status prüfen
git status
```

### Git Add - Änderungen stagen

```bash
# Einzelne Datei
git add hello.py

# Mehrere Dateien
git add file1.py file2.py

# Alle Änderungen
git add .

# Alle Python-Dateien
git add *.py
```

**Wichtig:** `git add .` fügt ALLE Änderungen im aktuellen Ordner hinzu. Das ist praktisch, aber pass auf, dass du keine ungewollten Dateien hinzufügst!

### Git Commit - Version speichern

```bash
git commit -m "Erste Version von hello.py"
```

**Commit-Message Regeln:**
- Kurz und aussagekräftig
- Im Imperativ ("Füge hinzu" nicht "Fügte hinzu")
- Beschreibt WAS und WARUM
- Erste Zeile max. 50 Zeichen
- Englisch oder Deutsch (sei konsistent)

**Gute Beispiele:**
```bash
git commit -m "Füge Begrüßungsfunktion hinzu"
git commit -m "Behebe Fehler in Berechnung"
git commit -m "Aktualisiere Dokumentation"
```

**Schlechte Beispiele:**
```bash
git commit -m "änderungen"
git commit -m "asdf"
git commit -m "probiere was aus"
```

### Commit-Historie ansehen

```bash
# Alle Commits anzeigen
git log

# Kompakte Darstellung
git log --oneline

# Mit Grafik
git log --oneline --graph
```

---

## Übung 3: Der Git-Workflow - Erste Commits

**Schwierigkeitsgrad: GRUNDLAGEN**

**Aufgabe:**

1. **Erste Datei commiten**
   - Die `hello.py` sollte noch "untracked" sein
   - Füge sie zur Staging Area hinzu: `git add hello.py`
   - Prüfe Status: `git status`
   - Erstelle ersten Commit: `git commit -m "Erste Version: Einfache Begrüßung"`
   - Prüfe erneut Status: `git status`

2. **Änderung machen und commiten**
   - Ändere `hello.py`, füge eine zweite Zeile hinzu: `print("Git ist toll!")`
   - Prüfe Status: `git status`
   - Stage die Änderung: `git add hello.py`
   - Commit: `git commit -m "Füge zweite Ausgabe hinzu"`

3. **Neue Datei erstellen und commiten**
   - Erstelle `rechner.py` mit:
     ```python
     x = 5
     y = 3
     summe = x + y
     print("Summe:", summe)
     ```
   - Stage und commite in einem Durchgang
   - Nutze eine aussagekräftige Commit-Message

4. **Historie ansehen**
   - Zeige alle Commits mit `git log`
   - Zeige kompakte Version mit `git log --oneline`

**Hinweise:**
- `git status` vor und nach jedem Schritt hilft beim Verstehen
- Staged Dateien werden grün angezeigt, unstaged rot
- Jeder Commit bekommt eine eindeutige ID (Hash)

<details>
<summary>Schritt-für-Schritt Lösung anzeigen</summary>

```bash
# ===== TEIL 1: Erste Datei commiten =====

# Status prüfen
git status
# hello.py sollte als "Untracked" erscheinen (rot)

# Zur Staging Area hinzufügen
git add hello.py

# Status erneut prüfen
git status
# Ausgabe:
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#         new file:   hello.py
# hello.py ist jetzt grün (staged)

# Ersten Commit erstellen
git commit -m "Erste Version: Einfache Begrüßung"
# Ausgabe:
# [main (root-commit) a1b2c3d] Erste Version: Einfache Begrüßung
#  1 file changed, 1 insertion(+)
#  create mode 100644 hello.py

# Status nach Commit
git status
# Ausgabe:
# On branch main
# nothing to commit, working tree clean


# ===== TEIL 2: Änderung machen =====

# Datei bearbeiten
echo 'print("Git ist toll!")' >> hello.py
# >> fügt Zeile hinzu, > würde überschreiben!

# Oder mit Editor: Öffne hello.py und füge zweite Zeile hinzu

# Datei anschauen
cat hello.py
# Ausgabe:
# print("Hallo Git!")
# print("Git ist toll!")

# Status prüfen
git status
# Ausgabe:
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#         modified:   hello.py
# Datei ist rot (geändert, aber nicht staged)

# Was wurde geändert?
git diff hello.py
# Zeigt die Änderungen:
# +print("Git ist toll!")

# Änderung stagen
git add hello.py

# Status prüfen
git status
# Jetzt grün (staged)

# Commiten
git commit -m "Füge zweite Ausgabe hinzu"


# ===== TEIL 3: Neue Datei =====

# Neue Datei erstellen
cat > rechner.py << 'EOF'
x = 5
y = 3
summe = x + y
print("Summe:", summe)
EOF

# Oder mit Editor: Erstelle rechner.py mit dem Code

# Status
git status
# rechner.py ist untracked (rot)

# Stagen und commiten
git add rechner.py
git commit -m "Füge einfachen Rechner hinzu"


# ===== TEIL 4: Historie ansehen =====

# Ausführliche Log-Ansicht
git log
# Ausgabe:
# commit 3def456... (HEAD -> main)
# Author: Dein Name <deine@email.de>
# Date:   ...
#
#     Füge einfachen Rechner hinzu
#
# commit 2abc123...
# Author: Dein Name <deine@email.de>
# Date:   ...
#
#     Füge zweite Ausgabe hinzu
#
# commit 1xyz789...
# Author: Dein Name <deine@email.de>  
# Date:   ...
#
#     Erste Version: Einfache Begrüßung

# Kompakte Ansicht
git log --oneline
# Ausgabe:
# 3def456 Füge einfachen Rechner hinzu
# 2abc123 Füge zweite Ausgabe hinzu
# 1xyz789 Erste Version: Einfache Begrüßung

# Log beenden (falls zu lang)
# Drücke 'q' zum Beenden
```

**Erklärungen:**

```
1. GIT ADD:
   - Verschiebt Dateien vom Working Directory zur Staging Area
   - "Markiert" Änderungen für den nächsten Commit
   - Änderungen können mehrfach gestaged werden
   - Analogie: Dinge in den Einkaufswagen legen

2. STAGING AREA:
   - Vorschau für den Commit
   - Nur das was hier ist, wird committed
   - Erlaubt gezielte Commits (nicht alle Änderungen auf einmal)
   - Sehr mächtig, wenn man es versteht!

3. GIT STATUS - FARBCODES:
   Rot:   Geändert ODER neu, aber nicht staged
   Grün:  Staged, bereit für Commit
   (In Terminals ohne Farbe: Beachte die Überschriften)

4. GIT COMMIT:
   - Erstellt einen "Snapshot" des Staging-Bereichs
   - Bekommt eindeutige ID (Hash, z.B. a1b2c3d)
   - Speichert Autor, Datum, Message
   - Ist dauerhaft (kann zurückgeholt werden)

5. COMMIT-MESSAGE:
   -m "Nachricht"
   - Beschreibt WAS geändert wurde
   - Imperativ: "Füge hinzu" (nicht "Hinzugefügt")
   - Kurz aber aussagekräftig
   - Wird in Historie angezeigt

6. ROOT-COMMIT:
   [main (root-commit) a1b2c3d]
   - Erster Commit in Repository
   - "root" = Wurzel des Baums
   - Nachfolgende Commits zeigen nur Hash

7. WORKING TREE CLEAN:
   "nothing to commit, working tree clean"
   → Alle Änderungen sind committed
   → Arbeitsverzeichnis = Repository
   → Guter Zustand!

8. GIT DIFF:
   - Zeigt Unterschiede zwischen Versionen
   - Ohne Argument: Unstaged vs. letzter Commit
   - Grün (+): Hinzugefügt
   - Rot (-): Entfernt
   - Hilfreich vor dem Commit!

9. GIT LOG:
   - Zeigt Commit-Historie
   - Neueste Commits oben
   - Jeder Commit hat:
     * Eindeutigen Hash
     * Autor
     * Datum
     * Message
   
   --oneline: Kompakte Darstellung
   - Nur Hash (kurz) und Message
   - Übersichtlicher bei vielen Commits

10. >> VS. >:
    >> = Anhängen an Datei
    > = Überschreiben der Datei
    Vorsicht mit >!

11. HEAD:
    - Zeiger auf aktuellen Commit
    - In Log: "HEAD -> main"
    - HEAD = Wo du gerade bist
```

**Was wir gelernt haben:**

```
✓ git add verschiebt Änderungen zur Staging Area
✓ git commit speichert Staging Area dauerhaft
✓ git status zeigt Zustand (rot = unstaged, grün = staged)
✓ git log zeigt Historie
✓ Commits haben eindeutige IDs (Hashes)
✓ Gute Commit-Messages sind wichtig!
✓ Working tree clean = guter Zustand
```

**Typische Fehler:**

```
❌ FEHLER: Commit ohne Message
   git commit
   → Öffnet Editor (kann verwirrend sein)
   → Lösung: Immer -m "Message" nutzen
   → Falls passiert: Editor schließen mit :q (vim) oder Ctrl+X (nano)

❌ FEHLER: Datei vergessen zu stagen
   git commit -m "Neue Funktion"
   → Aber git add vergessen
   → Commit ist leer oder unvollständig
   → Lösung: Immer git status VOR commit prüfen

❌ FEHLER: Alle Dateien stagen wollen, aber Tippfehler
   git add *
   → In manchen Shells funktioniert das anders
   → Lösung: Nutze git add . (sicherer)

❌ FEHLER: Schlechte Commit-Message
   git commit -m "fix"
   → Keine Information, was gefixt wurde
   → Später keine Ahnung, was es war
   → Lösung: Aussagekräftige Messages!
```

</details>

---

### Selbstcheck: Teil 3

1. Was ist der Unterschied zwischen `git add` und `git commit`?
2. Warum ist die Staging Area nützlich?
3. Wie siehst du, welche Dateien bereit für einen Commit sind?

<details>
<summary>Antworten anzeigen</summary>

1. `git add` bereitet Änderungen vor (Staging), `git commit` speichert sie dauerhaft in der Historie.
2. Du kannst gezielt auswählen, welche Änderungen zusammen in einen Commit sollen - nicht alles auf einmal.
3. Mit `git status` - staged Dateien sind grün markiert unter "Changes to be committed".

</details>

---

## Benötigte Konzepte für Teil 4

Bevor wir mit Remote-Repositories arbeiten, hier die wichtigsten Begriffe:

### Remote Repository

Ein **Remote Repository** ist eine Kopie deines Repositories auf einem Server (z.B. GitHub).

**Vorteile:**
- **Backup:** Code ist online gesichert
- **Zusammenarbeit:** Andere können am Code mitarbeiten
- **Zugriff:** Von überall auf den Code zugreifen
- **Portfolio:** Projekte öffentlich zeigen

### GitHub Account erstellen

Gehe zu [github.com](https://github.com) und erstelle einen kostenlosen Account.

**Tipp:** Nutze die gleiche E-Mail wie in deiner Git-Konfiguration!

### Die wichtigsten Remote-Befehle

```bash
# Remote-Repository hinzufügen
git remote add origin URL

# Änderungen hochladen
git push origin main

# Änderungen herunterladen
git pull origin main

# Repository klonen
git clone URL
```

### Origin und Main

**origin:**
- Standard-Name für das Remote-Repository
- Nur ein Name, könnte auch anders heißen
- Wie ein Lesezeichen zur GitHub-URL

**main:**
- Name des Haupt-Branches
- Früher "master", heute meist "main"
- Deine Haupt-Entwicklungslinie

---

## Übung 4: Mit GitHub arbeiten

**Schwierigkeitsgrad: GRUNDLAGEN**

**Aufgabe:**

**Vorbereitung auf GitHub:**
1. Gehe zu [github.com](https://github.com) und melde dich an
2. Klicke auf "New repository" (oder das +-Symbol oben rechts)
3. Repository-Name: `git-python-uebung`
4. Beschreibung: "Meine erste Git+Python Übung"
5. Wähle "Public" (oder "Private" wenn du es privat halten willst)
6. **WICHTIG:** NICHT "Initialize with README" anklicken!
7. Klicke "Create repository"

**Im Terminal:**
1. **Remote hinzufügen**
   - GitHub zeigt dir Befehle nach Erstellung
   - Kopiere die URL deines Repositories
   - Füge Remote hinzu: `git remote add origin URL`
   - Prüfe: `git remote -v`

2. **Hochladen (Push)**
   - Pushe deine Commits: `git push -u origin main`
   - `-u` bedeutet "upstream setzen" (nur beim ersten Mal nötig)
   
   **WICHTIG - Authentifizierung:**
   - **Windows (Git Credential Manager):** Ein Browser-Fenster öffnet sich automatisch
   - Melde dich dort bei GitHub an
   - **KEIN** Passwort im Terminal eingeben!
   - Die Anmeldung wird gespeichert - beim nächsten Mal kein Login nötig
   
   **Falls das Browser-Fenster nicht öffnet:**
   - Terminal-Fenster offen lassen
   - Manuell zu GitHub gehen und anmelden
   - Zurück zum Terminal - sollte jetzt funktionieren

3. **Auf GitHub überprüfen**
   - Aktualisiere die GitHub-Seite
   - Du solltest deine Dateien und Commits sehen!
   - .gitignore und .gitattributes sollten sichtbar sein

4. **Änderung machen und pushen**
   - Ändere `hello.py`: Füge `print("Jetzt auch auf GitHub!")` hinzu
   - Stage, commite und pushe die Änderung
   - Überprüfe auf GitHub

> **Best Practice:** Nutze **Pull (Fast-Forward only)**, um ungeplante Merge-Commits zu vermeiden:  
> Terminal: `git pull --ff-only`  
> VS Code: **F1 → „Git: Pull (Rebase)"** oder **Sync**  
> GitHub Desktop: **Fetch origin** → **Pull origin**

**Hinweise:**
- Die URL ist entweder HTTPS (einfacher für Anfänger) oder SSH
- Bei HTTPS: Git Credential Manager (GCM) öffnet Browser automatisch
- **Windows-Nutzer:** Wenn Browser-Login funktioniert, ist alles richtig!
- Bei Problemen: Stelle sicher, dass Git for Windows aktuell ist

<details>
<summary>Schritt-für-Schritt Lösung anzeigen</summary>

```bash
# ===== AUF GITHUB (im Browser) =====

# 1. Zu github.com navigieren
# 2. Anmelden
# 3. Klick auf "New repository" (grüner Button)
# 4. Ausfüllen:
#    - Repository name: git-python-uebung
#    - Description: Meine erste Git+Python Übung
#    - Public/Private: Public wählen
#    - KEIN Haken bei "Initialize with README"
# 5. "Create repository" klicken

# GitHub zeigt jetzt eine Seite mit Setup-Anweisungen
# → Kopiere die URL aus "Quick setup" (z.B. https://github.com/username/git-python-uebung.git)


# ===== IM TERMINAL =====

# Status checken (sollte clean sein)
git status

# Alle Commits anzeigen
git log --oneline
# Du solltest deine 3 Commits sehen

# Remote hinzufügen
git remote add origin https://github.com/DEIN-USERNAME/git-python-uebung.git
# Ersetze DEIN-USERNAME mit deinem GitHub-Namen!

# Remote überprüfen
git remote -v
# Ausgabe:
# origin  https://github.com/DEIN-USERNAME/git-python-uebung.git (fetch)
# origin  https://github.com/DEIN-USERNAME/git-python-uebung.git (push)

# Ersten Push durchführen
git push -u origin main

# === WICHTIG: AUTHENTIFIZIERUNG (WINDOWS) ===
# Git Credential Manager (GCM) öffnet automatisch deinen Browser
# → Melde dich dort bei GitHub an
# → KEIN Passwort im Terminal eingeben!
# → Nach dem Login: Fenster schließen, zurück zum Terminal
# → Push wird automatisch fortgesetzt

# Falls Browser sich NICHT öffnet:
# → Terminal-Fenster OFFEN LASSEN
# → Manuell zu github.com gehen und anmelden
# → Zurück zum Terminal - sollte weiterlaufen

# Ausgabe (nach erfolgreicher Authentifizierung):
# Enumerating objects: 9, done.
# Counting objects: 100% (9/9), done.
# ...
# To https://github.com/DEIN-USERNAME/git-python-uebung.git
#  * [new branch]      main -> main
# Branch 'main' set up to track remote branch 'main' from 'origin'.


# ===== ÜBERPRÜFUNG AUF GITHUB =====
# Aktualisiere die Browser-Seite
# Du solltest sehen:
# - hello.py
# - rechner.py
# - Deine Commit-Messages
# - "3 commits" oben


# ===== ÄNDERUNG MACHEN UND PUSHEN =====

# hello.py ändern
echo 'print("Jetzt auch auf GitHub!")' >> hello.py

# Anschauen
cat hello.py
# Sollte jetzt 3 Zeilen haben

# Standard-Workflow
git status
# Ausgabe: modified: hello.py (rot)

git add hello.py

git status
# Ausgabe: modified: hello.py (grün)

git commit -m "Füge GitHub-Begrüßung hinzu"

# Jetzt pushen (jetzt OHNE -u, das war nur beim ersten Mal nötig)
git push
# ODER explizit:
git push origin main

# Ausgabe:
# Enumerating objects: 5, done.
# ...
# To https://github.com/DEIN-USERNAME/git-python-uebung.git
#    a1b2c3d..e4f5g6h  main -> main


# ===== FINALE ÜBERPRÜFUNG =====
# Aktualisiere GitHub im Browser
# - Sollte jetzt 4 commits zeigen
# - hello.py sollte 3 Zeilen haben
# - Neueste Commit-Message sollte sichtbar sein
```

**Erklärungen:**

```
1. GITHUB REPOSITORY ERSTELLEN:
   "New repository"
   → Erstellt leeres Remote-Repository
   → Wie ein leerer Ordner in der Cloud
   
   "Initialize with README": NICHT anklicken!
   → Würde Commit erstellen
   → Unser lokales Repo hat bereits Commits
   → Würde zu Konflikten führen

2. GIT REMOTE:
   - Verbindung zwischen lokalem und Remote-Repository
   - "origin" ist Standard-Name (kann aber anders sein)
   - Speichert die URL
   
   git remote add origin URL
   → Fügt Remote mit Namen "origin" hinzu
   
   git remote -v
   → Zeigt alle Remotes (-v = verbose)
   → fetch: Zum Herunterladen
   → push: Zum Hochladen

3. GIT PUSH:
   git push -u origin main
   
   push: Hochladen
   -u: Set upstream (Tracking-Branch setzen)
   origin: Wohin pushen (Remote-Name)
   main: Welcher Branch
   
   -u NUR beim ersten Mal!
   → Danach reicht: git push

4. UPSTREAM / TRACKING:
   -u setzt "upstream branch"
   → Verbindet lokalen "main" mit Remote "main"
   → Git merkt sich: "main" gehört zu "origin/main"
   → Nachfolgende Befehle einfacher

5. AUTHENTICATION:
   HTTPS-URL: Braucht Authentifizierung
   
   Username: GitHub-Name
   Password: NICHT dein Login-Passwort!
           → Personal Access Token (PAT)
   
   PAT erstellen:
   GitHub → Settings → Developer settings
   → Personal access tokens → Generate new token

6. SSH VS. HTTPS:
   HTTPS: https://github.com/user/repo.git
   → Einfacher für Anfänger
   → Git Credential Manager (GCM) übernimmt Login
   → Browser öffnet sich automatisch
   → Keine Passwörter im Terminal!
   
   SSH: git@github.com:user/repo.git
   → Kein Browser-Login nötig
   → Braucht SSH-Key-Setup
   → Fortgeschritten
   
   EMPFEHLUNG für Windows: HTTPS + GCM!

7. GIT CREDENTIAL MANAGER (GCM):
   → Bei Git for Windows automatisch dabei
   → Öffnet Browser für GitHub-Login
   → Speichert Anmeldedaten sicher in Windows
   → Beim nächsten Push: Kein Login mehr nötig!
   
   So funktioniert es:
   1. git push
   2. Browser öffnet sich
   3. Bei GitHub anmelden
   4. Browser schließen
   5. Terminal macht automatisch weiter
   
   WICHTIG: Terminal-Fenster NICHT schließen während Login!

8. [NEW BRANCH]:
   * [new branch]      main -> main
   → Lokaler "main" wurde zu Remote "main"
   → Beim ersten Push
   → Danach: Fast-forward oder Merge

9. GIT PUSH (NACHFOLGENDE):
   git push
   → Reicht nach dem ersten Push mit -u
   → Git weiß: main gehört zu origin/main
   → Kürzer und einfacher!

10. REMOTE-TRACKING:
   "Branch 'main' set up to track..."
   → Lokaler main ist jetzt verbunden
   → git status zeigt ob synchron
   → git pull weiß, woher holen

10. WORKFLOW MIT REMOTE:
    1. Änderungen lokal machen
    2. git add
    3. git commit
    4. git push
    
    → Änderungen sind jetzt online!
```

**Was wir gelernt haben:**

```
✓ Remote Repository auf GitHub erstellen
✓ Lokales Repo mit Remote verbinden (git remote add)
✓ Commits hochladen (git push)
✓ Upstream-Branch setzen (-u beim ersten Push)
✓ Workflow: Edit → Add → Commit → Push
```

**Typische Fehler:**

```
❌ FEHLER: "Initialize with README" ausgewählt
   → Remote hat Commit, den lokal nicht gibt
   → Konflikt beim Push
   → Lösung: Lösche GitHub-Repo und erstelle neu OHNE README

❌ FEHLER: Browser-Fenster geschlossen während GCM-Login
   → Authentication failed
   → Terminal wartet auf Browser-Login
   → Lösung: 
     1. Terminal NICHT schließen
     2. Manuell zu github.com gehen, anmelden
     3. git push erneut versuchen
     4. Oder: Strg+C im Terminal, dann neu: git push

❌ FEHLER: "Authentication failed" trotz richtigem Login
   → GCM hat alte/falsche Credentials gespeichert
   → Lösung:
     Windows: Start → "Credential Manager"
     → Windows-Anmeldeinformationen
     → "git:https://github.com" suchen und löschen
     → git push erneut versuchen

❌ FEHLER: Browser öffnet sich nicht
   → GCM kann Browser nicht starten
   → Lösung:
     1. Terminal offen lassen
     2. Manuell https://github.com/login öffnen
     3. Anmelden
     4. Zurück zum Terminal
     5. Sollte jetzt weiterlaufen

❌ FEHLER: Push rejected
   → Remote hat Änderungen, die lokal nicht sind
   → Häufig bei Team-Arbeit
   → Lösung: git pull, dann git push

❌ FEHLER: Remote-Name falsch
   git push origin2 main
   → origin2 existiert nicht
   → Lösung: Prüfe mit git remote -v

❌ FEHLER: Branch-Name falsch
   git push origin master
   → Aber Branch heißt main
   → Lösung: Prüfe mit git branch

❌ FEHLER: Vor dem Push nicht committed
   git push
   → Unstaged changes werden nicht gepusht
   → Lösung: Erst add, commit, dann push

❌ FEHLER: .gitignore und .gitattributes nicht auf GitHub
   → Vergessen zu committen
   → Lösung: 
     git add .gitignore .gitattributes
     git commit -m "Füge Konfigurationsdateien hinzu"
     git push
```

</details>

---

### Selbstcheck: Teil 4

1. Was ist der Unterschied zwischen lokalem Repository und Remote Repository?
2. Wofür steht "origin"?
3. Warum nutzt man `-u` beim ersten Push?

<details>
<summary>Antworten anzeigen</summary>

1. Lokal = auf deinem Computer, Remote = auf einem Server (z.B. GitHub) - wie Backup in der Cloud.
2. "origin" ist der Standard-Name für das Remote-Repository - ein Lesezeichen zur GitHub-URL.
3. `-u` setzt den Upstream-Branch und verbindet deinen lokalen Branch mit dem Remote-Branch - danach reicht `git push` ohne weitere Argumente.

</details>

---

## Teil 5: Clone und Pull

### Repository klonen

`git clone` kopiert ein bestehendes Repository:

```bash
git clone https://github.com/username/repo.git
```

**Was passiert?**
- Komplettes Repository wird heruntergeladen
- Alle Commits, alle Dateien
- Remote ist automatisch als "origin" gesetzt
- Du kannst sofort anfangen zu arbeiten

**Wann verwendet man clone?**
- Fremde Projekte herunterladen
- Eigene Projekte auf neuem Computer
- Team-Projekt beitreten

### Änderungen holen

`git pull` holt Änderungen vom Remote:

```bash
git pull origin main
# Oder einfach:
git pull
```

**Was passiert?**
- Lädt neue Commits herunter
- Fügt sie in dein lokales Repository ein
- Aktualisiert deine Dateien

**Wann verwendet man pull?**
- Vor dem Arbeiten (immer!)
- Wenn andere gepusht haben
- Regelmäßig, um synchron zu bleiben

### Fast-Forward Only (Empfohlen für Anfänger)

**Problem:** `git pull` kann automatisch Merge-Commits erstellen, was verwirrend ist.

**Lösung:** Nutze Fast-Forward Only:

```bash
# Sicherer als normales git pull
git pull --ff-only

# Oder in VS Code: Command Palette (F1)
# → "Git: Pull (Rebase)"
```

**Was ist der Unterschied?**
- `git pull` → Erstellt Merge-Commit wenn nötig
- `git pull --ff-only` → Funktioniert nur wenn "sauberer" Fast-Forward möglich
- Bei Konflikten: Klare Fehlermeldung statt automatischem Merge

**Für diese Übung:** Nutze `git pull --ff-only` oder VS Code Sync - beides ist sicherer!

### Pull vor Push!

**Wichtige Regel:** Immer `pull` vor `push`!

```bash
# Guter Workflow:
git pull          # Erst holen
# Arbeiten...
git add .
git commit -m "..."
git pull          # Nochmal holen (falls andere inzwischen gepusht haben)
git push          # Dann pushen
```

> **Best Practice:** Nutze **Pull (Fast-Forward only)**, um ungeplante Merge-Commits zu vermeiden:  
> Terminal: `git pull --ff-only`  
> VS Code: **F1 → „Git: Pull (Rebase)"** oder **Sync**  
> GitHub Desktop: **Fetch origin** → **Pull origin**

---

## Übung 5: Kompletter Workflow mit Clone und Pull

**Schwierigkeitsgrad: GRUNDLAGEN**

**Aufgabe:**

In dieser Übung simulierst du Arbeit an zwei verschiedenen Orten:

**Teil A - Änderung auf GitHub (simuliert "andere Person"):**
1. Gehe zu deinem Repository auf GitHub
2. Klicke auf `rechner.py`
3. Klicke auf das Stift-Symbol (Edit)
4. Füge eine neue Zeile hinzu: `print("Differenz:", x - y)`
5. Scrolle runter zu "Commit changes"
6. Message: "Füge Differenz-Berechnung hinzu"
7. Klicke "Commit changes"

**Teil B - Änderung lokal holen:**
1. In deinem Terminal: `git status` (sollte "clean" sein)
2. `git log --oneline` (zeigt noch nicht den neuen Commit)
3. `git pull` (holt die Änderung von GitHub)
4. `cat rechner.py` (die neue Zeile sollte da sein!)
5. `git log --oneline` (jetzt ist der neue Commit sichtbar)

**Teil C - Lokale Änderung und Push:**
1. Erstelle neue Datei `multiplikation.py`:
   ```python
   a = 7
   b = 8
   ergebnis = a * b
   print("Produkt:", ergebnis)
   ```
2. Kompletter Workflow: Status → Add → Commit → Pull → Push
3. Überprüfe auf GitHub

**Hinweise:**
- Dieser Workflow simuliert Team-Arbeit
- In der Praxis: Kollegen pushen, du pullst
- Immer vor dem Push pullen!

<details>
<summary>Schritt-für-Schritt Lösung anzeigen</summary>

```bash
# ===== TEIL A: Änderung auf GitHub =====
# (Im Browser auf github.com)

# 1. Navigiere zu deinem Repository
# 2. Klicke auf rechner.py
# 3. Klicke auf Stift-Symbol rechts oben (Edit this file)
# 4. Füge am Ende hinzu:
#    print("Differenz:", x - y)
# 5. Scrolle nach unten
# 6. "Commit changes" Section:
#    - Commit message: "Füge Differenz-Berechnung hinzu"
#    - Optional: Extended description leer lassen
#    - "Commit directly to main branch" sollte ausgewählt sein
# 7. Klicke "Commit changes" (grüner Button)

# GitHub zeigt jetzt den neuen Commit
# rechner.py hat jetzt 5 Zeilen


# ===== TEIL B: Änderung lokal holen =====
# (Im Terminal)

# Aktuellen Status
git status
# Ausgabe:
# On branch main
# Your branch is behind 'origin/main' by 1 commit
# (use "git pull" to update your local branch)
# → Git weiß bereits, dass Remote neuer ist!

# Log anschauen (noch ohne neuen Commit)
git log --oneline
# Zeigt nur die 4 lokalen Commits

# Änderungen holen
git pull
# Ausgabe:
# remote: Enumerating objects: 5, done.
# ...
# Updating a1b2c3d..e4f5g6h
# Fast-forward
#  rechner.py | 1 +
#  1 file changed, 1 insertion(+)

# EMPFOHLEN: Mit Fast-Forward Only (sicherer für Anfänger)
git pull --ff-only
# Funktioniert genauso, gibt aber Fehler bei Konflikten
# Statt automatisch zu mergen

# Alternative in VS Code:
# F1 → "Git: Pull (Rebase)" 
# Oder: Sync-Button (macht pull + push automatisch)

# Datei anschauen
cat rechner.py
# Ausgabe:
# x = 5
# y = 3
# summe = x + y
# print("Summe:", summe)
# print("Differenz:", x - y)    ← NEU!

# Log erneut anschauen
git log --oneline
# Zeigt jetzt 5 Commits (der neue ist dabei)

# Python-Code testen
python3 rechner.py
# Ausgabe:
# Summe: 8
# Differenz: 2


# ===== TEIL C: Lokale Änderung und Push =====

# Neue Datei erstellen
cat > multiplikation.py << 'EOF'
a = 7
b = 8
ergebnis = a * b
print("Produkt:", ergebnis)
EOF

# Oder mit Editor erstellen

# Status
git status
# Ausgabe:
# Untracked files:
#   multiplikation.py

# Hinzufügen
git add multiplikation.py

# Status
git status
# Ausgabe:
# Changes to be committed:
#   new file:   multiplikation.py

# Commiten
git commit -m "Füge Multiplikation hinzu"

# VOR dem Push: Nochmal pullen (Best Practice!)
git pull
# Ausgabe:
# Already up to date.
# → Gut, keine neuen Änderungen

# Jetzt pushen
git push

# Ausgabe:
# Enumerating objects: 4, done.
# ...
# To https://github.com/username/git-python-uebung.git
#    e4f5g6h..i7j8k9l  main -> main


# ===== ÜBERPRÜFUNG =====

# Im Browser auf GitHub:
# → Repository aktualisieren
# → Sollte jetzt 3 Dateien zeigen:
#   - hello.py
#   - rechner.py
#   - multiplikation.py (NEU!)
# → "6 commits" sollte oben stehen
# → Neueste Commit-Message: "Füge Multiplikation hinzu"

# multiplikation.py anklicken
# → Sollte den Code zeigen

# "6 commits" anklicken
# → Zeigt komplette Historie
# → Commit "Füge Differenz-Berechnung hinzu" von GitHub
# → Commit "Füge Multiplikation hinzu" von lokal

# Finale Überprüfung lokal
git log --oneline
# Sollte 6 Commits zeigen

git status
# Sollte "clean" sein
```

**Erklärungen:**

```
1. ÄNDERUNG AUF GITHUB:
   → Simuliert, dass ein Teammitglied gepusht hat
   → In Realität: Kollege macht Änderungen
   → Du musst diese Änderungen holen
   
   Web-Editor auf GitHub:
   → Praktisch für kleine Änderungen
   → Erstellt automatisch Commit
   → Nicht ideal für größere Änderungen

2. GIT PULL:
   git pull origin main
   
   → Holt Commits vom Remote
   → Fügt sie in lokales Repo ein
   → Aktualisiert Arbeitsverzeichnis
   
   Besteht eigentlich aus zwei Befehlen:
   git fetch (Commits holen)
   git merge (Commits einbauen)
   → Für Anfänger: pull reicht!

3. FAST-FORWARD:
   "Fast-forward"
   → Dein lokaler Branch war hinterher
   → Keine Konflikte
   → Git "spult vor" zu neuem Stand
   → Einfachster Fall!

4. BRANCH IS BEHIND:
   "Your branch is behind 'origin/main'"
   → Git vergleicht lokal mit Remote
   → Zeigt Unterschiede
   → Gibt Hinweis: git pull

5. 1 INSERTION(+):
   "1 file changed, 1 insertion(+)"
   → Statistik der Änderung
   → + = Zeile hinzugefügt
   → - = Zeile gelöscht
   → Übersicht was passiert ist

6. ALREADY UP TO DATE:
   → Kein Pull nötig, alles aktuell
   → Gut vor dem Push
   → Bedeutet: Keine Konflikte

7. WORKFLOW MIT PULL:
   1. git pull       ← Start mit aktualisieren
   2. Arbeiten
   3. git add
   4. git commit
   5. git pull       ← Nochmal vor Push
   6. git push       ← Hochladen
   
   Punkt 5 wichtig!
   → Jemand könnte inzwischen gepusht haben

8. WARUM PULL VOR PUSH?
   → Verhindert Konflikte
   → Garantiert, dass du auf aktuellem Stand bist
   → Bei Konflikt: Lokal lösen, nicht auf GitHub
   → Best Practice!

9. COMMIT-AUTOR:
   Commits auf GitHub:
   → Autor ist dein GitHub-Account
   → Wenn E-Mail übereinstimmt: Wird dir zugeordnet
   → Zeigt in Historie deinen Namen

10. SYNCHRONISATION:
    Lokales Repo ← git pull → Remote Repo
    Lokales Repo → git push → Remote Repo
    
    → Bidirektionale Synchronisation
    → Wie Dropbox, aber mit Versionen
    → Zusammenarbeit möglich
```

**Was wir gelernt haben:**

```
✓ Änderungen auf GitHub machen (Web-Editor)
✓ Änderungen mit git pull holen
✓ Fast-forward verstehen
✓ Workflow: Pull → Work → Commit → Pull → Push
✓ git status zeigt ob behind/ahead
✓ Lokale und Remote-Änderungen zusammenführen
```

**Typische Fehler:**

```
❌ FEHLER: Push ohne vorheriges Pull
   git push
   → "rejected" Fehler
   → Remote hat Änderungen, die lokal nicht sind
   → Lösung: git pull, dann git push

❌ FEHLER: Pull mitten in Änderungen
   → Uncommitted changes
   → Git will nicht pullen
   → Lösung: Erst committen, dann pullen
   → Oder: git stash (fortgeschritten)

❌ FEHLER: Falscher Branch
   git pull origin master
   → Aber Branch heißt main
   → Holt falsche/n Branch
   → Lösung: Prüfe Branch-Namen

❌ FEHLER: Merge-Konflikt
   → Beide haben gleiche Zeile geändert
   → Git kann nicht automatisch mergen
   → Lösung: Konflikt manuell lösen (später lernen)
   → Vorbeugung: Kommunikation im Team!

❌ FEHLER: Pull nach Änderungen vergessen
   → Lokale Änderung
   → Direkt commit + push
   → Konflikt!
   → Lösung: Immer vor Commit pullen
```

**Real-World-Szenario:**

```
Montag Morgen:
1. git pull          ← Hol Änderungen vom Wochenende
2. Arbeiten am Code
3. git add .
4. git commit
5. git pull          ← Kollege hat inzwischen auch gepusht
6. git push

Nachmittag:
1. git pull          ← Hol neue Änderungen
2. Weiterarbeiten
...

→ Regel: VOR der Arbeit und VOR dem Push immer pull!
```

</details>

---

### Selbstcheck: Teil 5

1. Was macht `git pull`?
2. Warum sollte man vor dem Push pullen?
3. Was ist der Unterschied zwischen Änderungen auf GitHub machen und lokal?

<details>
<summary>Antworten anzeigen</summary>

1. Holt neue Commits vom Remote-Repository und fügt sie in dein lokales Repository ein.
2. Um Konflikte zu vermeiden - wenn jemand inzwischen gepusht hat, musst du diese Änderungen erst holen.
3. Auf GitHub = direkter Commit auf dem Remote, lokal = musst noch pushen, um es online zu synchronisieren.

</details>

---

## Bonus-Übung: Mini-Python-Projekt mit Git versionieren

**Schwierigkeitsgrad: FORTGESCHRITTEN**

**Hinweis:** Diese Übung kombiniert alles, was du gelernt hast. Sie simuliert einen realistischen Entwicklungs-Workflow.

### Aufgabe

Erstelle ein kleines Python-Projekt **Schritt für Schritt** mit Git:

**Projekt: Einfacher Taschenrechner**

**Phase 1 - Projekt-Setup:**
1. Erstelle neuen Ordner `taschenrechner-projekt`
2. Navigiere hinein und initialisiere Git
3. Erstelle `.gitignore` Datei mit Inhalt:
   ```
   __pycache__/
   *.pyc
   *.pyo
   *.pyd
   .Python
   env/
   venv/
   ```
4. Erstelle `.gitattributes` Datei mit Inhalt:
   ```
   *.py text eol=lf
   *.md text eol=lf
   ```
5. Commite beide Dateien: `git add .gitignore .gitattributes` und `git commit -m "Initialer Commit mit Projektkonfiguration"`

**Phase 2 - Basis-Funktionen:**
1. Erstelle `addition.py`:
   ```python
   zahl1 = 10
   zahl2 = 5
   ergebnis = zahl1 + zahl2
   print("Addition:", ergebnis)
   ```
2. Commite: "Füge Addition hinzu"

3. Erstelle `subtraktion.py`:
   ```python
   zahl1 = 10
   zahl2 = 5
   ergebnis = zahl1 - zahl2
   print("Subtraktion:", ergebnis)
   ```
4. Commite: "Füge Subtraktion hinzu"

**Phase 3 - Erweiterung:**
1. Erstelle `hauptprogramm.py`:
   ```python
   print("=== Taschenrechner ===")
   a = 15
   b = 3
   
   print("Addition:", a + b)
   print("Subtraktion:", a - b)
   print("Multiplikation:", a * b)
   print("Division:", a / b)
   ```
2. Commite: "Füge Hauptprogramm mit allen Operationen hinzu"

**Phase 4 - Dokumentation:**
1. Erstelle `README.md`:
   ```markdown
   # Taschenrechner-Projekt
   
   Ein einfacher Taschenrechner in Python.
   
   ## Dateien
   - addition.py: Addiert zwei Zahlen
   - subtraktion.py: Subtrahiert zwei Zahlen  
   - hauptprogramm.py: Vollständiger Rechner
   
   ## Verwendung
   python3 hauptprogramm.py
   ```
2. Commite: "Füge README hinzu"

**Phase 5 - GitHub:**
1. Erstelle Repository auf GitHub: `taschenrechner-projekt`
2. Verbinde mit Remote
3. Pushe alle Commits
4. Überprüfe auf GitHub

**Phase 6 - Änderung simulieren:**
1. Ändere auf GitHub das README (füge ein Emoji hinzu 🧮)
2. Pull lokal
3. Füge lokal eine Zeile in `hauptprogramm.py` hinzu:
   ```python
   print("Rechner beendet!")
   ```
4. Commite: "Füge Abschluss-Nachricht hinzu"
5. Pull (um sicher zu gehen)
6. Push

<details>
<summary>Vollständige Lösung anzeigen</summary>

```bash
# ===== PHASE 1: Projekt-Setup =====

# Ordner erstellen
cd ~/Desktop
mkdir taschenrechner-projekt
cd taschenrechner-projekt

# Git initialisieren
git init
# Ausgabe: Initialized empty Git repository...

# .gitignore erstellen
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
EOF

# .gitattributes erstellen
cat > .gitattributes << 'EOF'
*.py text eol=lf
*.md text eol=lf
EOF

# Prüfen
cat .gitignore
cat .gitattributes

# Ersten Commit
git add .gitignore .gitattributes
git status
git commit -m "Initialer Commit mit Projektkonfiguration"
git log --oneline


# ===== PHASE 2: Basis-Funktionen =====

# Addition erstellen
cat > addition.py << 'EOF'
zahl1 = 10
zahl2 = 5
ergebnis = zahl1 + zahl2
print("Addition:", ergebnis)
EOF

# Status und Commit
git status
git add addition.py
git commit -m "Füge Addition hinzu"

# Testen
python3 addition.py
# Ausgabe: Addition: 15

# Subtraktion erstellen
cat > subtraktion.py << 'EOF'
zahl1 = 10
zahl2 = 5
ergebnis = zahl1 - zahl2
print("Subtraktion:", ergebnis)
EOF

# Commit
git add subtraktion.py
git commit -m "Füge Subtraktion hinzu"

# Testen
python3 subtraktion.py
# Ausgabe: Subtraktion: 5

# Log anschauen
git log --oneline
# 3 Commits sollten sichtbar sein


# ===== PHASE 3: Erweiterung =====

# Hauptprogramm erstellen
cat > hauptprogramm.py << 'EOF'
print("=== Taschenrechner ===")
a = 15
b = 3

print("Addition:", a + b)
print("Subtraktion:", a - b)
print("Multiplikation:", a * b)
print("Division:", a / b)
EOF

# Status
git status
# Sollte hauptprogramm.py als untracked zeigen

# Hinzufügen und committen
git add hauptprogramm.py
git commit -m "Füge Hauptprogramm mit allen Operationen hinzu"

# Testen
python3 hauptprogramm.py
# Ausgabe:
# === Taschenrechner ===
# Addition: 18
# Subtraktion: 12
# Multiplikation: 45
# Division: 5.0


# ===== PHASE 4: Dokumentation =====

# README erstellen
cat > README.md << 'EOF'
# Taschenrechner-Projekt

Ein einfacher Taschenrechner in Python.

## Dateien
- addition.py: Addiert zwei Zahlen
- subtraktion.py: Subtrahiert zwei Zahlen
- hauptprogramm.py: Vollständiger Rechner

## Verwendung
python3 hauptprogramm.py
EOF

# Commit
git add README.md
git commit -m "Füge README hinzu"

# Übersicht über alle Dateien
ls -la
# Sollte zeigen:
# .git/
# .gitignore
# README.md
# addition.py
# subtraktion.py
# hauptprogramm.py

# Log
git log --oneline
# 5 Commits


# ===== PHASE 5: GitHub =====

# Auf GitHub (im Browser):
# 1. New repository
# 2. Name: taschenrechner-projekt
# 3. KEIN README
# 4. Create repository
# 5. URL kopieren

# Remote hinzufügen
git remote add origin https://github.com/DEIN-USERNAME/taschenrechner-projekt.git

# Remote prüfen
git remote -v

# Pushen
git push -u origin main
# Alle 5 Commits werden hochgeladen

# Auf GitHub überprüfen
# → Sollte alle Dateien und Commits zeigen


# ===== PHASE 6: Änderung simulieren =====

# AUF GITHUB:
# 1. README.md öffnen
# 2. Edit klicken
# 3. In erste Zeile ändern zu: "# Taschenrechner-Projekt 🧮"
# 4. Commit: "Füge Emoji zu README hinzu"

# LOKAL IM TERMINAL:

# Pull
git pull
# Ausgabe:
# Updating a1b2c3d..e4f5g6h
# Fast-forward
#  README.md | 2 +-
#  1 file changed, 1 insertion(+), 1 deletion(-)

# README anschauen
cat README.md
# Emoji sollte da sein!

# Hauptprogramm erweitern
echo 'print("Rechner beendet!")' >> hauptprogramm.py

# Anschauen
cat hauptprogramm.py
# Sollte neue Zeile am Ende haben

# Standard-Workflow
git status
git add hauptprogramm.py
git commit -m "Füge Abschluss-Nachricht hinzu"

# Vor Push: Nochmal pull (Best Practice!)
git pull
# Already up to date

# Push
git push

# Überprüfung auf GitHub
# → 7 Commits
# → hauptprogramm.py hat neue Zeile
# → README hat Emoji

# Finale Tests
python3 hauptprogramm.py
# Sollte jetzt "Rechner beendet!" am Ende ausgeben

git log --oneline
# Sollte 7 Commits zeigen

git status
# Should be clean
```

**Erklärungen:**

```
1. .GITIGNORE:
   → Sagt Git, welche Dateien NICHT getrackt werden sollen
   → __pycache__/: Python-Cache-Ordner
   → *.pyc: Kompilierte Python-Dateien
   → Wichtig: Keine generierten/temporären Dateien versionieren!

2. WARUM .GITIGNORE WICHTIG IST:
   → Hält Repository sauber
   → Keine Konflikte bei generierten Dateien
   → Kleinere Repository-Größe
   → Professioneller Standard

3. SCHRITTWEISES COMMITTEN:
   → Jede Datei einzeln committen
   → Sinnvolle Commit-Messages
   → Historie erzählt Geschichte des Projekts
   → Leichter zurückzuverfolgen

4. README.MD:
   → Markdown-Format
   → Wird auf GitHub schön formatiert angezeigt
   → # = Überschrift
   → ## = Unter-Überschrift
   → - = Listenpunkt
   → Dokumentiert dein Projekt

5. PROJEKTSTRUKTUR:
   taschenrechner-projekt/
   ├── .git/                    (versteckt)
   ├── .gitignore
   ├── README.md
   ├── addition.py
   ├── subtraktion.py
   └── hauptprogramm.py
   
   → Übersichtlich
   → Gut dokumentiert
   → Professionell

6. WORKFLOW ZUSAMMENFASSUNG:
   1. Lokal arbeiten
   2. Oft committen (kleine, logische Einheiten)
   3. Regelmäßig pullen
   4. Pushen wenn Feature fertig
   5. Immer pull vor push

7. COMMIT-FREQUENZ:
   ✓ Nach jeder abgeschlossenen Änderung
   ✓ Wenn Code funktioniert
   ✓ Vor Pausen/Feierabend
   ✗ Nicht: Nur einmal am Tag
   ✗ Nicht: Alle Änderungen auf einmal

8. WARUM MEHRERE KLEINE DATEIEN?
   → Zeigt Git-Workflow
   → In Realität: Oft besser als eine große Datei
   → Modularität
   → Leichter zu versionieren

9. ECHO MIT >>:
   echo 'text' >> datei
   → Hängt an (append)
   → Praktisch für kleine Ergänzungen
   → Alternativ: Editor verwenden

10. GIT LOG --ONELINE:
    → Übersicht über Projekt-Entwicklung
    → Zeigt Entwicklungs-Geschichte
    → Bei großen Projekten: Hunderte von Commits
    → Gute Messages = Gute Doku!
```

**Best Practices die wir angewendet haben:**

```
✓ .gitignore von Anfang an
✓ Sinnvolle Commit-Messages
✓ Kleine, fokussierte Commits
✓ README für Dokumentation
✓ Pull vor Push
✓ Regelmäßige Status-Checks
✓ Testing nach Änderungen
✓ Saubere Projektstruktur
```

**Realistisches Projekt-Szenario:**

```
Tag 1: Setup
→ Repository erstellen
→ .gitignore anlegen
→ Erste Dateien committen

Tag 2-5: Entwicklung
→ Features hinzufügen
→ Regelmäßig committen
→ Pushen wenn Feature fertig
→ Pull wenn Team-Mitglieder pushen

Tag 6: Dokumentation
→ README schreiben
→ Code kommentieren
→ Finale Tests

Tag 7: Release
→ Letzter Pull
→ Finaler Commit
→ Push
→ Tag erstellen (git tag v1.0)

→ Projekt ist online und versioniert!
```

**Erweiterungsideen für Übung:**

```
1. Mehr Operationen:
   - potenz.py (Potenzen)
   - wurzel.py (Wurzeln)

2. Bessere Struktur:
   - Ordner für verschiedene Rechner-Typen

3. Interaktivität:
   - input() für Benutzereingaben

4. Tests:
   - test_addition.py
   - Automatische Tests (später lernen)

→ Mit jedem Feature: Neuer Commit!
→ Git macht es einfach zu erweitern
```

</details>

---

## Zusammenfassung

### Git - Das Wichtigste

**Repository:**
- Projekt mit Versionskontrolle
- `.git` Ordner speichert Historie
- `git init` erstellt Repository

**Workflow:**
```bash
git status              # Wo stehe ich?
git add datei.py        # Änderungen stagen
git commit -m "..."     # Änderungen committen
git pull --ff-only      # Herunterladen (sicher)
git push                # Hochladen
```

**Arbeitsrhythmus:**  
`status → add → commit → pull (ff-only) → push`

**Drei Bereiche:**
```
Working Directory → Staging Area → Repository
      (Arbeit)        (Auswahl)      (Geschichte)
```

**Remote:**
- GitHub = Online-Speicher
- `origin` = Standard-Name für Remote
- `git remote add origin URL` verbindet
- `git push` lädt hoch
- `git pull` lädt herunter

### Wichtige Befehle

**Setup:**
```bash
git config --global user.name "Name"
git config --global user.email "email"
git init
```

**Basis-Workflow:**
```bash
git status
git add .
git commit -m "Nachricht"
git log --oneline
```

**Mit Remote:**
```bash
git remote add origin URL
git push -u origin main
git pull
git clone URL
```

**Hilfe:**
```bash
git --version
git status
git log
git remote -v
```

### Goldene Regeln

1. **Oft committen**
   - Kleine, logische Einheiten
   - Funktionierender Code

2. **Gute Commit-Messages**
   - Beschreibend
   - Imperativ
   - "Füge hinzu" nicht "Hinzugefügt"

3. **Pull vor Push**
   - Immer aktualisieren vor dem Hochladen
   - Konflikte vermeiden

4. **Status ist dein Freund**
   - `git status` oft nutzen
   - Zeigt, wo du stehst
   - Gibt Tipps

5. **.gitignore nutzen**
   - Keine generierten Dateien
   - Keine persönlichen Dateien
   - Sauber halten

### Typische Fehler und Lösungen

**Problem: "Nothing to commit"**
→ Vergessen `git add`
→ Lösung: Erst add, dann commit

**Problem: "Push rejected"**
→ Remote hat neuere Commits
→ Lösung: `git pull`, dann `git push`

**Problem: "Untracked files"**
→ Neue Dateien noch nicht hinzugefügt
→ Lösung: `git add datei` oder `git add .`

**Problem: "Modified files"**
→ Änderungen noch nicht committed
→ Lösung: `git add` und `git commit`

**Problem: Falscher Branch**
→ Oft "master" statt "main"
→ Lösung: `git branch` zum Prüfen

**Problem: Authentication failed**
→ Falsches Passwort (braucht Token)
→ Lösung: Personal Access Token erstellen

### Git + Python Best Practices

**1. .gitignore für Python:**
```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
```

**2. README.md erstellen:**
```markdown
# Projektname
Beschreibung

## Installation
Schritte

## Verwendung
Beispiele
```

**3. Sinnvolle Commits:**
```
✓ "Füge Login-Funktion hinzu"
✓ "Behebe Division-durch-Null Fehler"
✓ "Aktualisiere README"

✗ "update"
✗ "fix"
✗ "asdf"
```

**4. Ordnerstruktur:**
```
projekt/
├── .git/
├── .gitignore
├── README.md
├── main.py
├── utils.py
└── tests/
```

### Wann welchen Befehl?

**Projekt starten:**
```bash
git init              # Neues Projekt
git clone URL         # Bestehendes Projekt
```

**Während der Arbeit:**
```bash
git status            # Oft!
git add datei         # Nach Änderungen
git commit -m "..."   # Wenn Feature fertig
```

**Mit Team arbeiten:**
```bash
git pull              # Vor Arbeitsbeginn
git pull              # Vor jedem Push
git push              # Wenn fertig
```

**Überblick:**
```bash
git log --oneline     # Commits sehen
git remote -v         # Remotes sehen
git branch            # Branches sehen (später)
```

### Nächste Schritte

Nach diesen Basics kannst du lernen:
- **Branches**: Parallele Entwicklung
- **Merge**: Branches zusammenführen
- **Pull Requests**: Code-Review auf GitHub
- **Conflicts**: Konflikte lösen
- **Tags**: Versionen markieren
- **Stash**: Änderungen temporär speichern
- **Reset**: Commits rückgängig machen

**Aber:** Beherrsche erst die Basics! Alles baut darauf auf.

---

## Troubleshooting - Häufige Probleme unter Windows

### Problem: "fatal: not a git repository"

**Ursache:** Du bist nicht im richtigen Ordner

**Lösung:**
```bash
# Im Terminal: Zeige aktuellen Pfad
git rev-parse --show-toplevel
```
**In VS Code:** File → Open Folder → git-python-uebung auswählen

---

### Problem: "Updates were rejected..."

**Ursache:** Remote hat Änderungen, die du lokal nicht hast

**Lösung:**
```bash
# Terminal: Pull mit Fast-Forward
git pull --ff-only
git push
```
**VS Code:** Sync-Button  
**GitHub Desktop:** Fetch origin → Pull origin → Push origin

---

### Problem: "Authentication failed"

**Ursache:** Git Credential Manager (GCM) funktioniert nicht richtig

**Lösung:**
- **Fenster offen lassen** – Login erfolgt im Browser (Git Credential Manager)
- Falls Browser sich nicht öffnet: Terminal offen lassen, manuell zu github.com gehen und anmelden
- **Sonst:** Windows „Anmeldeinformationsverwaltung" öffnen → Eintrag `git:https://github.com` suchen und löschen → erneut pushen

---

### Problem: "warning: LF will be replaced by CRLF"

**Ursache:** Zeilenenden-Unterschied zwischen Windows und Linux/Mac

**Lösung:**
- **Unkritisch unter Windows** – Dateien werden automatisch konvertiert
- `.gitattributes` beibehalten (wie in Übung 2 gezeigt)

---

### Problem: Befehle wie `cat`, `echo` funktionieren nicht

**Ursache:** Du bist in CMD/PowerShell statt Git Bash

**Lösung:**
- **In VS Code:** Unten rechts auf "powershell" klicken → **"Git Bash"** auswählen (siehe Setup-Anleitung oben)

**Alternative:** Nutze VS Code zum Datei-Erstellen statt Terminal-Befehlen (`code dateiname.py`)

---

## Tipps für die Praxis

1. **Gewöhne dir den Workflow an**
   - `status → add → commit → pull (ff-only) → push`
   - Wird zur zweiten Natur
   - Wie Autofahren: Anfangs bewusst, später automatisch

2. **Commits sind billig**
   - Commite oft!
   - Lieber zu viele als zu wenige
   - Du kannst später zusammenfassen (squash)

3. **Lies die Ausgaben**
   - Git gibt hilfreiche Hinweise
   - "use 'git add'..." etc.
   - Meistens steht da die Lösung

4. **Backup durch Git**
   - Auf GitHub = sicher gespeichert
   - Computer kaputt? Code ist sicher!
   - Wie Cloud-Backup für Code

5. **GitHub erkunden**
   - Schaue dir andere Projekte an
   - Lerne von fremdem Code
   - Sieh dir Commit-Messages an

6. **Bei Problemen:**
   - `git status` ist der Anfang
   - Google: "git [dein Problem]"
   - Sehr gute Dokumentation online
   - Stack Overflow hilft

7. **Übung macht den Meister**
   - Erstelle Übungsprojekte
   - Probiere Befehle aus
   - Git kann fast alles rückgängig machen

8. **README ist wichtig**
   - Dokumentiere deine Projekte
   - Hilft dir selbst später
   - Zeigt Professionalität

9. **Regelmäßig pullen**
   - Vor Arbeitsbeginn
   - Vor Pausen
   - Vor Feierabend
   - Synchron bleiben!

10. **Hab keine Angst**
    - Git ist sehr sicher
    - Fast alles kann wiederhergestellt werden
    - Commits gehen nicht verloren
    - Einfach ausprobieren!

