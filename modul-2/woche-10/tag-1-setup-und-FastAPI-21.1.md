# Tag 1: FastAPI Basics + Requests testen

## Lernziele
* FastAPI-Projekt aufsetzen und verstehen, wie es strukturiert ist
* Ersten Endpoint erstellen und dabei HTTP-Grundlagen verstehen
* Swagger UI als Werkzeug zum Testen nutzen
* Mit In-Memory-Daten arbeiten (als Vorbereitung für die spätere Datenbank)

---

## Theorie: Was ist FastAPI?

FastAPI ist ein **modernes Python-Web-Framework** für den Bau von APIs (Application Programming Interfaces). Eine API ist im Grunde eine Schnittstelle, über die verschiedene Programme miteinander kommunizieren können.

### Warum FastAPI?

**Vorteile:**
* **Automatische API-Dokumentation (Swagger UI)**: FastAPI generiert automatisch eine interaktive Dokumentation, in der du deine API direkt testen kannst - ohne externe Tools!
* **Typ-Validierung mit Pydantic**: Durch Python's Type Hints prüft FastAPI automatisch, ob die Daten das richtige Format haben
* **Sehr performant**: FastAPI ist eines der schnellsten Python-Frameworks überhaupt
* **Async-fähig**: Unterstützt asynchrone Programmierung für bessere Performance
* **Minimaler Boilerplate-Code**: Wenig "Drumherum-Code" nötig - du konzentrierst dich auf die Logik

### Was ist eine API?

Stell dir vor, du bist in einem Restaurant:
- **Du** bist der Client (z.B. eine Website oder App)
- **Die Küche** ist der Server/Datenbank
- **Der Kellner** ist die API - er nimmt deine Bestellung auf, gibt sie an die Küche weiter und bringt dir das Essen

Eine API ist also ein "Vermittler", der Anfragen entgegennimmt und Daten zurückgibt.

---

## Live-Coding Schritt für Schritt

### 1. Projekt-Setup

Zuerst richten wir unsere Arbeitsumgebung ein. Das ist wie das Vorbereiten deines Arbeitsplatzes, bevor du mit einem Projekt beginnst.

**Voraussetzung:** Python 3.8 oder höher muss installiert sein. Prüfe mit `python --version` oder `python3 --version`.

```bash
# Ordner erstellen und hineinwechseln
mkdir mini-api && cd mini-api

# Git initialisieren (Versionskontrolle)
git init

# Virtual Environment erstellen
python -m venv venv
```

**Jetzt Virtual Environment aktivieren - WICHTIG: Nur den für dein System passenden Befehl ausführen!**

```bash
# Linux/Mac:
source venv/bin/activate

# Windows CMD:
venv\Scripts\activate

# Windows PowerShell:
.\venv\Scripts\Activate.ps1
```

**PowerShell-Hinweis:** Falls beim Aktivieren ein Fehler wegen der Execution Policy erscheint, kannst du diese für deinen Benutzer anpassen:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
**Achtung:** In Firmenumgebungen kann dies durch Gruppenrichtlinien blockiert sein - nutze dann stattdessen die Windows CMD.

```bash
# FastAPI installieren (empfohlen: mit [standard])
pip install "fastapi[standard]"

# Alternativ (minimal):
# pip install fastapi uvicorn

# requirements.txt erstellen
pip freeze > requirements.txt
```

**Was passiert hier genau?**

1. **`mkdir mini-api && cd mini-api`**: Erstellt einen neuen Ordner und wechselt direkt hinein
2. **`git init`**: Initialisiert ein Git-Repository - damit können wir später alle Änderungen nachverfolgen
3. **`python -m venv venv`**: Erstellt ein "Virtual Environment" - eine isolierte Python-Umgebung nur für dieses Projekt
   - **Warum?** Damit sich die Pakete verschiedener Projekte nicht gegenseitig stören
4. **Virtual Environment aktivieren**: Je nach System unterschiedliche Befehle - **führe nur den für dein System passenden Befehl aus!**
   - Nach der Aktivierung siehst du `(venv)` vor deinem Terminal-Prompt
5. **`pip install "fastapi[standard]"`**: 
   - **fastapi[standard]**: Installiert FastAPI zusammen mit uvicorn und empfohlenen Extras
   - **uvicorn**: Der ASGI-Server, der unsere FastAPI-Anwendung ausführt (vergleichbar mit einem Webserver wie Apache)
   - **Alternative:** `pip install fastapi uvicorn` installiert nur das Minimum
6. **`pip freeze > requirements.txt`**: Speichert alle installierten Pakete mit ihren Versionsnummern
   - **Warum?** Damit andere (oder du auf einem anderen Computer) exakt dieselben Versionen installieren können

---

### 2. Projektstruktur

So sieht unser Projekt nach dem Setup aus:

```
mini-api/
├── venv/              # Virtual Environment (wird von Python verwaltet)
├── main.py            # Unsere Haupt-Datei mit der API-Logik
└── requirements.txt   # Liste aller benötigten Pakete
```

**Wichtig:** Der `venv/`-Ordner sollte **nicht** in Git committed werden, da er sehr groß ist und auf jedem System neu erstellt werden kann. Dafür erstellen wir später eine `.gitignore`-Datei.

---

### 3. Erste main.py erstellen

Jetzt erstellen wir unsere erste API-Datei. Öffne einen Code-Editor (VS Code, PyCharm, etc.) und erstelle die Datei `main.py`:

```python
from fastapi import FastAPI

app = FastAPI(title="Mini Notes API")

# Dummy-Daten (später: echte Datenbank)
notes = [
    {"id": 1, "text": "Erste Notiz", "created_at": "2025-12-01T10:00:00"},
    {"id": 2, "text": "Zweite Notiz", "created_at": "2025-12-01T14:30:00"},
]

@app.get("/health")
def health_check():
    """Health-Check Endpoint."""
    return {"status": "ok"}

@app.get("/notes")
def get_all_notes():
    """Gibt alle Notizen zurück."""
    return notes
```

**Code-Erklärung Zeile für Zeile:**

1. **`from fastapi import FastAPI`**: Importiert die FastAPI-Klasse
2. **`app = FastAPI(title="Mini Notes API")`**: 
   - Erstellt unsere FastAPI-Anwendung
   - `title` erscheint später in der automatischen Dokumentation
3. **`notes = [...]`**: Eine einfache Python-Liste mit Dictionaries
   - **Wichtig:** Diese Daten sind nur im Speicher (RAM)!
   - Bei jedem Neustart der API sind alle Änderungen weg
   - Das ist nur für den Anfang - morgen nutzen wir eine richtige Datenbank
4. **`@app.get("/health")`**: Ein **Decorator**, der die Funktion darunter als GET-Endpoint registriert
   - **GET** = HTTP-Methode zum Abrufen von Daten (nicht zum Ändern)
   - **"/health"** = Der Pfad/URL-Teil nach der Basis-URL
5. **`def health_check():`**: Eine normale Python-Funktion
   - Der Funktionsname ist egal für die API (wichtig ist nur der Pfad im Decorator)
6. **`return {"status": "ok"}`**: Gibt ein Python-Dictionary zurück
   - FastAPI wandelt das automatisch in JSON um!
   - JSON ist das Standard-Datenformat für APIs

**Was ist ein Health-Check Endpoint?**
Ein `/health`-Endpoint ist wie ein "Lebenszeichen" der API. Er wird oft von Monitoring-Tools genutzt, um zu prüfen, ob die API noch läuft. Er sollte immer eine schnelle, einfache Antwort geben.

---

### 4. API starten

Jetzt starten wir unsere API zum ersten Mal!

```bash
uvicorn main:app --reload
```

**Was bedeutet dieser Befehl?**

- **`uvicorn`**: Der ASGI-Server, den wir installiert haben
- **`main`**: Der Name unserer Python-Datei (ohne `.py`)
- **`app`**: Der Name der Variable, in der unsere FastAPI-Instanz steckt
- **`--reload`**: Auto-Restart bei Code-Änderungen
  - **Sehr praktisch während der Entwicklung!**
  - Sobald du `main.py` speicherst, startet der Server automatisch neu
  - **Achtung:** Nur für Development! Verbraucht mehr Ressourcen und kann instabiler sein - niemals in Production verwenden!

**Alternative (moderner):** Ab FastAPI 0.111.0 kannst du auch `fastapi dev main.py` nutzen - das macht dasselbe wie `uvicorn --reload`, aber einfacher. Wir bleiben hier bei `uvicorn`, damit du genau verstehst, was passiert.

**Was siehst du im Terminal?**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Das bedeutet: Deine API läuft jetzt auf `http://localhost:8000`!

---

### 5. Testen

Öffne deinen Browser und teste folgende URLs:

#### 🌐 Die Basis-URL:
**http://localhost:8000**
- Zeigt erstmal nur einen JSON-Fehler: `{"detail":"Not Found"}`
- Das ist normal - wir haben noch keinen Endpoint für `/` erstellt
- Das werden wir gleich in der Mini-Aufgabe beheben!

#### 📚 Swagger UI (Interaktive Dokumentation):
**http://localhost:8000/docs**

Das ist die **automatisch generierte Dokumentation**! Hier siehst du:
- Alle verfügbaren Endpoints
- Welche HTTP-Methoden sie unterstützen (GET, POST, etc.)
- Welche Parameter sie erwarten
- Du kannst die API direkt hier testen, ohne Code zu schreiben!

**Probiere es aus:**
1. Klicke auf `GET /health`
2. Klicke auf "Try it out"
3. Klicke auf "Execute"
4. Schau dir die Antwort an: `{"status": "ok"}`

**Mache dasselbe mit `GET /notes`** - du siehst deine beiden Dummy-Notizen!

#### 📖 Alternative Dokumentation (ReDoc):
**http://localhost:8000/redoc**
- Eine alternative, etwas formellere Darstellung der API-Dokumentation
- Oft bevorzugt für "offizielle" Dokumentation

---

## Mini-Aufgabe

Jetzt bist du dran! Diese Aufgabe hilft dir, das Gelernte direkt anzuwenden.

**Aufgabe:** Füge einen neuen Endpoint hinzu: `GET /`

Dieser soll eine kurze API-Beschreibung zurückgeben (1-2 Sätze als JSON).

**Anforderungen:**
1. Der Endpoint soll auf dem Root-Pfad `/` erreichbar sein
2. Er soll mindestens folgende Felder zurückgeben:
   - `name`: Name deiner API
   - `description`: Eine kurze Beschreibung

**Bonus-Aufgaben:**
1. Füge ein `version`-Feld hinzu (z.B. "1.0.0")
2. Teste den neuen Endpoint in Swagger UI
3. Committe deine Änderungen mit Git:
   ```bash
   git add main.py
   git commit -m "Add root endpoint with API description"
   ```

**Tipp:** Schau dir an, wie die `/health`- und `/notes`-Endpoints aufgebaut sind!

<details>
<summary>💡 Lösung anzeigen</summary>

```python
@app.get("/")
def root():
    """Gibt eine API-Beschreibung zurück."""
    return {
        "name": "Mini Notes API",
        "description": "Eine einfache API zum Speichern von Notizen",
        "version": "1.0.0"
    }
```

**Erklärung:**
- `@app.get("/")`: Registriert die Funktion für den Root-Pfad
- Der Docstring `"""..."""` erscheint in der Swagger-Dokumentation
- Wir geben ein Dictionary mit allen wichtigen Infos zurück
- FastAPI wandelt es automatisch in JSON um

**Erweiterte Lösung mit mehr Infos:**
```python
@app.get("/")
def root():
    """Gibt eine API-Beschreibung zurück."""
    return {
        "name": "Mini Notes API",
        "description": "Eine einfache API zum Speichern von Notizen",
        "version": "1.0.0",
        "endpoints": ["/health", "/notes"],
        "docs": "/docs"
    }
```

Jetzt kannst du auf http://localhost:8000 gehen und siehst eine schöne Übersicht!

</details>

---

## Übungen für Tag 1

Hier sind ein paar einfache Übungen, um dein Wissen zu festigen. Versuche sie selbstständig zu lösen, bevor du die Lösungen anschaust!

### Übung 1: Status-Endpoint erweitern

Erweitere den `/health`-Endpoint so, dass er auch die aktuelle Uhrzeit zurückgibt.

**Hinweis:** Du musst `datetime` importieren. Nutze `datetime.now()`.

<details>
<summary>💡 Lösung anzeigen</summary>

```python
from datetime import datetime

@app.get("/health")
def health_check():
    """Health-Check Endpoint mit Zeitstempel."""
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    }
```

**Erklärung:**
- Zuerst importieren wir `datetime` ganz oben in der Datei
- `datetime.now()` gibt das aktuelle Datum und die Uhrzeit zurück
- `.isoformat()` wandelt es in einen String im ISO-Format um (z.B. "2025-12-01T10:30:00")
- Das ist wichtig, weil JSON keine datetime-Objekte direkt unterstützt

**Beispiel-Antwort:**
```json
{
  "status": "ok",
  "timestamp": "2025-12-01T10:30:00.123456"
}
```

</details>

---

### Übung 2: Notizen zählen

Erstelle einen neuen Endpoint `GET /notes/count`, der die Anzahl der gespeicherten Notizen zurückgibt.

**Tipp:** Die Python-Funktion `len()` gibt die Länge einer Liste zurück.

**Wichtiger Hinweis für später:** Fixe Pfade wie `/notes/count` müssen **vor** dynamischen Pfaden wie `/notes/{note_id}` definiert werden, sonst wird "count" als ID interpretiert - vor allem, wenn `{note_id}` als `str` definiert ist!

<details>
<summary>💡 Lösung anzeigen</summary>

```python
@app.get("/notes/count")
def count_notes():
    """Gibt die Anzahl der Notizen zurück."""
    return {
        "count": len(notes)
    }
```

**Erklärung:**
- `len(notes)` zählt, wie viele Elemente in der `notes`-Liste sind
- Wir geben die Zahl in einem Dictionary zurück, damit es schön strukturiertes JSON ist
- Der Endpunkt könnte z.B. für Dashboard-Statistiken genutzt werden

**Beispiel-Antwort:**
```json
{
  "count": 2
}
```

**Noch besser - mit mehr Infos:**
```python
@app.get("/notes/count")
def count_notes():
    """Gibt Statistiken über die Notizen zurück."""
    return {
        "count": len(notes),
        "message": f"Es sind {len(notes)} Notizen gespeichert."
    }
```

</details>

---

### Übung 3: Erste Notiz anzeigen

Erstelle einen Endpoint `GET /notes/first`, der nur die erste Notiz aus der Liste zurückgibt.

**Tipp:** In Python greift man mit `liste[0]` auf das erste Element zu.

<details>
<summary>💡 Lösung anzeigen</summary>

```python
@app.get("/notes/first")
def get_first_note():
    """Gibt die erste Notiz zurück."""
    if len(notes) > 0:
        return notes[0]
    else:
        return {"message": "Keine Notizen vorhanden"}
```

**Erklärung:**
- Wir prüfen zuerst mit `if len(notes) > 0`, ob überhaupt Notizen existieren
- Wenn ja: `notes[0]` gibt das erste Element zurück (Listen beginnen bei Index 0)
- Wenn nein: Wir geben eine freundliche Nachricht zurück
- **Wichtig:** Diese Prüfung verhindert einen Fehler, falls die Liste leer ist!

**Beispiel-Antwort (wenn Notizen vorhanden):**
```json
{
  "id": 1,
  "text": "Erste Notiz",
  "created_at": "2025-12-01T10:00:00"
}
```

**Bessere Version mit HTTP-Statuscode:**
```python
from fastapi import HTTPException

@app.get("/notes/first")
def get_first_note():
    """Gibt die erste Notiz zurück."""
    if len(notes) > 0:
        return notes[0]
    else:
        raise HTTPException(status_code=404, detail="Keine Notizen vorhanden")
```

Mit `HTTPException` geben wir einen korrekten HTTP-404-Fehler zurück, wenn keine Notizen da sind. Das ist professioneller als nur eine Nachricht!

</details>

---

### Übung 4: .gitignore erstellen

Erstelle eine `.gitignore`-Datei, damit Git bestimmte Dateien ignoriert.

**Was soll ignoriert werden?**
- Das `venv/`-Verzeichnis (sehr groß und nicht nötig im Repository)
- `__pycache__/`-Ordner (automatisch generierte Python-Cache-Dateien)
- `.pyc`-Dateien (kompilierte Python-Dateien)

<details>
<summary>💡 Lösung anzeigen</summary>

Erstelle eine Datei namens `.gitignore` im Projekt-Root mit folgendem Inhalt:

```gitignore
# Virtual Environment
venv/
env/

# Python Cache
__pycache__/
*.pyc
*.pyo
*.pyd

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

**Erklärung:**
- **`venv/` und `env/`**: Virtual Environments (können neu erstellt werden mit `requirements.txt`)
- **`__pycache__/` und `*.pyc`**: Cache-Dateien, die Python automatisch erstellt
- **`.vscode/` und `.idea/`**: Editor-spezifische Einstellungen
- **`.DS_Store`**: macOS-spezifische Dateien
- **`Thumbs.db`**: Windows-Thumbnails

**Git-Befehle danach:**
```bash
git add .gitignore
git commit -m "Add .gitignore for Python project"
```

**Tipp:** Auf https://gitignore.io kannst du dir .gitignore-Vorlagen für verschiedene Programmiersprachen und Tools generieren lassen!

</details>

---

## Zusammenfassung Tag 1

**Was haben wir gelernt?**

 **Projekt-Setup:**
- Virtual Environment erstellen und aktivieren
- FastAPI installieren (mit `[standard]` für alle empfohlenen Extras)
- Git-Repository initialisieren

 **FastAPI-Grundlagen:**
- Eine FastAPI-Anwendung erstellen mit `FastAPI()`
- Endpoints definieren mit Decorators (`@app.get()`)
- JSON-Antworten automatisch zurückgeben

 **HTTP-Grundlagen:**
- GET-Requests zum Abrufen von Daten
- URL-Pfade (z.B. `/health`, `/notes`)
- JSON als Datenformat für APIs

 **Entwickler-Tools:**
- Swagger UI (`/docs`) zum interaktiven Testen
- ReDoc (`/redoc`) für Dokumentation
- Auto-Reload während der Entwicklung (`--reload`)

 **In-Memory-Daten:**
- Daten in einer Python-Liste speichern
- Verstehen, dass diese Daten temporär sind
- Vorbereitung für echte Datenbank (kommt morgen!)

---

## Ausblick auf Tag 2

Morgen werden wir:
- **SQLite-Datenbank** einbinden (persistente Datenspeicherung!)
- **POST-Requests** erstellen (neue Notizen hinzufügen)
- **Pydantic-Models** nutzen (Datenvalidierung)
- **CRUD-Operationen** komplett umsetzen (Create, Read, Update, Delete)
- **Path Parameters** kennenlernen (z.B. `/notes/{note_id}`)

**Deine Daten werden endlich gespeichert bleiben, auch nach Neustart!** 

---

## main.py - Finale Version Tag 1

Hier ist die finale Version von `main.py` nach allen Aufgaben:

```python
"""
Mini Notes API - Tag 1: In-Memory Version
==========================================
Dieses File zeigt die grundlegende FastAPI-Struktur
mit Dummy-Daten im Speicher.

WICHTIG: Alle Änderungen gehen verloren, wenn der Server neu startet!
Ab Tag 2 nutzen wir eine echte Datenbank.
"""
from fastapi import FastAPI, HTTPException
from datetime import datetime

# FastAPI-App erstellen mit Metadaten
app = FastAPI(
    title="Mini Notes API",
    description="Eine einfache API zum Speichern von Notizen",
    version="1.0.0"
)

# Dummy-Daten (werden bei Neustart zurückgesetzt!)
# Das ist nur temporär - morgen kommt SQLite!
notes = [
    {"id": 1, "text": "Erste Notiz", "created_at": "2025-12-01T10:00:00"},
    {"id": 2, "text": "Zweite Notiz", "created_at": "2025-12-01T14:30:00"},
]

@app.get("/")
def root():
    """
    API-Übersicht
    
    Gibt grundlegende Informationen über die API zurück.
    """
    return {
        "name": "Mini Notes API",
        "description": "Eine einfache API zum Speichern von Notizen",
        "version": "1.0.0",
        "endpoints": ["/health", "/notes", "/notes/count", "/notes/first"],
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    """
    Health-Check Endpoint
    
    Prüft, ob die API läuft und gibt einen Zeitstempel zurück.
    """
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/notes")
def get_all_notes():
    """
    Alle Notizen abrufen
    
    Gibt eine Liste aller gespeicherten Notizen zurück.
    """
    return notes

@app.get("/notes/count")
def count_notes():
    """
    Notizen zählen
    
    Gibt die Anzahl der gespeicherten Notizen zurück.
    """
    return {
        "count": len(notes),
        "message": f"Es sind {len(notes)} Notizen gespeichert."
    }

@app.get("/notes/first")
def get_first_note():
    """
    Erste Notiz abrufen
    
    Gibt die erste Notiz aus der Liste zurück.
    Falls keine Notizen vorhanden sind, wird ein 404-Fehler zurückgegeben.
    """
    if len(notes) > 0:
        return notes[0]
    else:
        raise HTTPException(
            status_code=404,
            detail="Keine Notizen vorhanden"
        )
```

** Wenn ihr Fragen habt, meldet euch bei Patrick oder mir. Viel Erfolg und bis morgen! **