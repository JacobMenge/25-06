# Tag 2: SQLite anbinden + CRUD-Operationen

## Lernziele
* SQLite als persistente Datenspeicherung einrichten
* Datenbank-Tabellen erstellen
* CRUD-Operationen implementieren (Create, Read, Update, Delete)
* Mit SQL-Abfragen arbeiten und SQL-Injection vermeiden
* Daten bleiben nach Neustart der API erhalten!

---

## Theorie: Was ist SQLite?

### Was ist eine Datenbank?

**In-Memory-Daten (Tag 1)** = Post-it-Zettel → weg, wenn du aufräumst  
**SQLite-Datenbank** = Ordner im Aktenschrank → bleiben für immer

Eine Datenbank speichert strukturierte Daten dauerhaft auf der Festplatte.

### Warum SQLite?

**Vorteile:**
* **Serverlos**: Keine separate Installation nötig
* **Eine Datei = komplette Datenbank**: `notes.db` enthält alles
* **In Python eingebaut**: `import sqlite3` - fertig!
* **Perfekt für kleine bis mittlere Projekte**

| Aspekt | In-Memory (Tag 1) | SQLite (heute) |
|--------|------------------|----------------|
| **Speicherort** | RAM (flüchtig) | Festplatte (persistent) |
| **Nach Neustart** | Daten weg | Daten bleiben |
| **Einsatzgebiet** | Tests, Demos | Produktiv einsetzbar |

---

## Live-Coding Schritt für Schritt

### 1. Projekt-Vorbereitung

**Wichtig:** Stelle sicher, dass dein Virtual Environment von Tag 1 noch aktiviert ist!

```bash
# Prüfen, ob venv aktiv ist (du solltest "(venv)" im Terminal sehen)
# Falls nicht, aktivieren:

# Linux/Mac:
source venv/bin/activate

# Windows CMD:
venv\Scripts\activate

# Windows PowerShell:
.\venv\Scripts\Activate.ps1
```

SQLite ist bereits in Python enthalten, wir müssen also nichts installieren! Aber wir sollten unsere `main.py` von Tag 1 sichern:

```bash
# Mit Git sichern (empfohlen - funktioniert auf allen Systemen):
git add main.py
git commit -m "Tag 1 complete: Basic in-memory API"

# Alternativ: Manuelles Backup
# Linux/Mac: cp main.py main_tag1.py
# Windows CMD: copy main.py main_tag1.py
# Windows PowerShell: Copy-Item main.py main_tag1.py
```

---

### 2. Datenbank-Setup

Jetzt erweitern wir unsere `main.py` um Datenbank-Funktionalität. Öffne `main.py` und ersetze den Inhalt komplett:

```python
"""
Mini Notes API - Tag 2: SQLite Version
"""
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# FastAPI-App erstellen
app = FastAPI(title="Mini Notes API", version="2.0.0")

# Datenbank-Dateiname
DATABASE = "notes.db"

def init_db():
    """Datenbank initialisieren und Tabelle erstellen."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Datenbank beim Start initialisieren
init_db()
```

**Was passiert hier?**

1. **`sqlite3.connect(DATABASE)`**: Öffnet/erstellt die Datenbankdatei
2. **`cursor = conn.cursor()`**: Erstellt einen Cursor zum Ausführen von SQL-Befehlen
3. **`CREATE TABLE IF NOT EXISTS`**: Erstellt die Tabelle nur, wenn sie noch nicht existiert
   - `id`: Eindeutige ID (automatisch hochgezählt)
   - `text`: Der Notiztext (darf nicht leer sein)
   - `created_at`: Zeitstempel (wird automatisch gesetzt)
4. **`conn.commit()`**: Speichert die Änderungen
5. **`conn.close()`**: Schließt die Verbindung

**Wichtig:** Mit `uvicorn --reload` kann `init_db()` mehrfach aufgerufen werden - das ist dank `IF NOT EXISTS` aber unkritisch.

---

### 3. Root-Endpoint

Füge den Root-Endpoint hinzu:

```python
@app.get("/")
def root():
    """API-Übersicht"""
    return {
        "name": "Mini Notes API",
        "version": "2.0.0",
        "database": "SQLite",
        "endpoints": ["/notes", "/notes/{id}"]
    }
```

---

### 4. GET /notes - Alle Notizen aus der Datenbank

```python
@app.get("/notes")
def get_all_notes():
    """Alle Notizen abrufen"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Ermöglicht Dict-Zugriff
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]
```

**Was passiert hier?**

1. **`conn.row_factory = sqlite3.Row`**: Zeilen werden als Dict-ähnliche Objekte zurückgegeben (statt Tupel)
2. **`SELECT * FROM notes`**: Wähle alle Spalten aus der `notes`-Tabelle
3. **`ORDER BY id DESC`**: Sortiere nach ID, neueste zuerst
4. **`fetchall()`**: Holt alle Ergebnisse auf einmal
5. **`[dict(row) for row in rows]`**: Wandelt Rows in normale Dictionaries um

---

### 5. Pydantic Model für Validierung

Bevor wir POST implementieren, brauchen wir ein Datenmodell:

```python
class NoteCreate(BaseModel):
    """Schema für das Erstellen einer Notiz."""
    text: str
```

**Was ist Pydantic?**
- Pydantic prüft automatisch, ob die empfangenen Daten das richtige Format haben
- `text: str` bedeutet: Das Feld `text` muss vorhanden sein und ein String sein
- Wenn das Feld fehlt oder der Typ falsch ist, gibt FastAPI automatisch einen Fehler zurück

---

### 6. POST /notes - Neue Notiz erstellen

```python
@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    """Neue Notiz erstellen"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO notes (text) VALUES (?)",
        (note.text,)  # Tuple mit einem Element (Komma beachten!)
    )
    
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return {"id": new_id, "text": note.text}
```

**Was passiert hier?**

1. **`@app.post(..., status_code=201)`**: POST erstellt neue Ressourcen, 201 = "Created"
2. **`note: NoteCreate`**: Pydantic validiert automatisch
3. **`INSERT INTO notes (text) VALUES (?)`**: Fügt eine neue Zeile ein
4. **`?` als Platzhalter**: Wird durch `note.text` ersetzt
5. **`(note.text,)`**: Tuple mit einem Element - **Komma ist wichtig!**
6. **`cursor.lastrowid`**: Die ID der neu eingefügten Zeile
7. **`conn.commit()`**: Speichert die Änderungen dauerhaft

**🚨 SQL-Injection vermeiden:**

**NIEMALS so** (unsicher):
```python
cursor.execute(f"INSERT INTO notes (text) VALUES ('{note.text}')")
```

**IMMER so** (sicher):
```python
cursor.execute("INSERT INTO notes (text) VALUES (?)", (note.text,))
```

Mit `?`-Platzhaltern wird der Text automatisch escaped und ist sicher!

---

### 7. GET /notes/{note_id} - Einzelne Notiz abrufen

```python
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """Eine einzelne Notiz abrufen"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row is None:
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
    
    return dict(row)
```

**Was ist neu?**

- **`{note_id}` in der URL**: Path Parameter - FastAPI extrahiert die ID automatisch
- **`note_id: int`**: Typ-Konvertierung - bei `/notes/abc` → 422 Error
- **`fetchone()`**: Gibt nur **ein** Ergebnis zurück (oder `None`)
- **`HTTPException`**: Wirft einen 404-Fehler, wenn die Notiz nicht existiert

**Beispiele:**
- `GET /notes/1` → Notiz mit ID 1
- `GET /notes/999` → 404, wenn nicht vorhanden

---

## Mini-Aufgabe

**Aufgabe:** Implementiere `DELETE /notes/{note_id}`

Dieser soll eine Notiz aus der Datenbank löschen.

**Anforderungen:**
- Bei Erfolg: Bestätigungsnachricht zurückgeben
- Bei nicht existierender ID: HTTP 404

**Hinweise:**
- SQL: `DELETE FROM notes WHERE id = ?`
- Prüfe mit `cursor.rowcount`, ob eine Zeile gelöscht wurde

<details>
<summary>💡 Lösung anzeigen</summary>

```python
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    """Notiz löschen"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    deleted_count = cursor.rowcount
    
    conn.commit()
    conn.close()
    
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
    
    return {"message": "Notiz gelöscht", "id": note_id}
```

**Wichtig:** `cursor.rowcount` gibt an, wie viele Zeilen betroffen waren:
- `0` = nichts gelöscht (ID existierte nicht)
- `1` = eine Zeile gelöscht (Erfolg!)

</details>

---

## Übungen für Tag 2

### Übung 1: PUT /notes/{note_id} - Notiz aktualisieren

Implementiere einen Endpoint zum Aktualisieren einer bestehenden Notiz.

**Anforderungen:**
- SQL: `UPDATE notes SET text = ? WHERE id = ?`
- Bei Erfolg: Aktualisierte Notiz zurückgeben
- Bei nicht existierender ID: HTTP 404

<details>
<summary>💡 Lösung anzeigen</summary>

```python
@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteCreate):
    """Notiz aktualisieren"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE notes SET text = ? WHERE id = ?", (note.text, note_id))
    updated_count = cursor.rowcount
    conn.commit()
    
    if updated_count == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
    
    # Aktualisierte Notiz abrufen
    conn.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    row = cursor.fetchone()
    conn.close()
    
    return dict(row)
```

**Hinweis:** PUT ist die HTTP-Methode zum vollständigen Ersetzen einer Ressource.

</details>

---

### Übung 2 (Bonus): GET /notes/search - Volltextsuche

Erstelle einen Endpoint, der Notizen nach einem Suchbegriff durchsucht.

**Anforderungen:**
- Query Parameter `q` für den Suchtext
- SQL: `WHERE text LIKE ?` mit Wildcards (`%suchtext%`)

<details>
<summary>💡 Lösung anzeigen</summary>

```python
@app.get("/notes/search")
def search_notes(q: str):
    """Notizen durchsuchen"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    search_pattern = f"%{q}%"
    cursor.execute("SELECT * FROM notes WHERE text LIKE ?", (search_pattern,))
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]
```

**Hinweis:** Der f-String `f"%{q}%"` ist hier OK, weil wir ihn als Parameter übergeben!

</details>

---

## Zusammenfassung Tag 2

**Was haben wir gelernt?**

 **SQLite-Grundlagen:**
- Datenbank initialisieren und Tabellen erstellen
- Connection → Cursor → Execute → Commit → Close

 **CRUD-Operationen:**
- **C**reate: `INSERT` mit POST
- **R**ead: `SELECT` mit GET
- **U**pdate: `UPDATE` mit PUT  
- **D**elete: `DELETE` mit DELETE

 **SQL-Sicherheit:**
- `?`-Platzhalter für Parameter verwenden
- SQL-Injection vermeiden

 **FastAPI:**
- Path Parameters (`{note_id}`)
- Pydantic für Validierung
- HTTP-Statuscodes (201, 404)

 **Persistenz:**
- Daten bleiben nach Neustart erhalten!

---

## Ausblick auf Tag 3

Morgen machen wir den Code robuster und professioneller:
- **Error Handling** (try-except, bessere Fehlerbehandlung)
- **Context Manager** (`with` für automatisches Connection-Handling)
- **FastAPI Dependencies** (Dependency Injection)

---

## main.py - Finale Version Tag 2

Hier ist die finale, vollständige Version von `main.py`:

```python
"""
Mini Notes API - Tag 2: SQLite Version
Daten bleiben jetzt nach Neustart erhalten!
"""
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# FastAPI-App erstellen
app = FastAPI(title="Mini Notes API", version="2.0.0")

# Datenbank-Dateiname
DATABASE = "notes.db"

# ========================================
# Pydantic Models
# ========================================

class NoteCreate(BaseModel):
    """Schema für das Erstellen/Aktualisieren einer Notiz."""
    text: str

# ========================================
# Datenbank-Setup
# ========================================

def init_db():
    """Datenbank initialisieren und Tabelle erstellen."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Datenbank beim Start initialisieren
init_db()

# ========================================
# API Endpoints
# ========================================

@app.get("/")
def root():
    """API-Übersicht"""
    return {
        "name": "Mini Notes API",
        "version": "2.0.0",
        "database": "SQLite",
        "endpoints": ["/notes", "/notes/{id}"]
    }

@app.get("/notes")
def get_all_notes():
    """Alle Notizen abrufen"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """Eine einzelne Notiz abrufen"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row is None:
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
    
    return dict(row)

@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    """Neue Notiz erstellen"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (text) VALUES (?)", (note.text,))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"id": new_id, "text": note.text}

@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteCreate):
    """Notiz aktualisieren"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET text = ? WHERE id = ?", (note.text, note_id))
    updated_count = cursor.rowcount
    conn.commit()
    
    if updated_count == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
    
    # Aktualisierte Notiz abrufen
    conn.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row)

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    """Notiz löschen"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    deleted_count = cursor.rowcount
    conn.commit()
    conn.close()
    
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
    
    return {"message": "Notiz gelöscht", "id": note_id}
```

---

## .gitignore erweitern

Füge die Datenbank-Datei zu `.gitignore` hinzu, damit sie nicht ins Repository kommt:

```gitignore
# Virtual Environment
venv/
env/

# Python Cache
__pycache__/
*.pyc
*.pyo
*.pyd

# SQLite Datenbank
*.db
*.db-journal

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

**Warum `*.db` ignorieren?**
- Die Datenbank enthält persönliche/lokale Daten
- Jeder Entwickler sollte seine eigene lokale Datenbank haben
- In Production wird eine separate Datenbank genutzt (oft PostgreSQL)

---

## Checkliste Tag 2

- [ ] SQLite verstanden und `notes.db` erstellt
- [ ] `init_db()` implementiert
- [ ] GET /notes aus Datenbank liest
- [ ] POST /notes in Datenbank schreibt
- [ ] GET /notes/{id} einzelne Notiz zurückgibt
- [ ] DELETE /notes/{id} implementiert (Mini-Aufgabe)
- [ ] PUT /notes/{id} implementiert (Übung 1)
- [ ] API neu gestartet - Daten sind noch da! 
- [ ] Swagger UI getestet
- [ ] Code committed mit Git

**Glückwunsch! Du hast jetzt eine CRUD-API mit persistenter Datenspeicherung!** 

**Bei Fragen meldet euch bei Patrick oder mir. Viel Erfolg und bis morgen!**
