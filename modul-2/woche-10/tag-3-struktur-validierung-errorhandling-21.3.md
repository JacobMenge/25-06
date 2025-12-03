# Tag 3: Saubere Struktur + Validierung + Error Handling

## Lernziele
* Code in Module aufteilen (Separation of Concerns)
* Eingabe-Validierung mit Pydantic Field
* Query-Parameter implementieren
* Error Handling mit try-except richtig umsetzen
* Context Manager (`with`-Statement) für sauberes Ressourcen-Management
* Wiederholungen vermeiden und Code wartbarer machen

---

## Theorie: Warum Code aufteilen?

### Das Problem mit "Alles in einer Datei"

**Vorher: Alles in main.py** 
```
main.py (200+ Zeilen)
├── API-Endpoints
├── DB-Verbindungen
├── SQL-Queries
└── Business-Logik
```

**Probleme:**
* API-Logik und Datenbank-Code sind vermischt
* Schwer zu testen - man muss immer die ganze API starten
* Unübersichtlich bei Wachstum
* Änderungen an der DB beeinflussen die API direkt
* Wiederverwendung in anderen Projekten schwierig

**Nachher: Getrennte Module** 
```
main.py (übersichtliche API-Endpoints)
db.py (alle DB-Operationen)
```

**Vorteile:**
* **Klare Verantwortlichkeiten**: Jede Datei hat einen Zweck
* **Einfacher zu verstehen**: Man muss nur die relevante Datei öffnen
* **Besser testbar**: DB-Funktionen können separat getestet werden
* **Wiederverwendbar**: `db.py` kann in anderen Projekten genutzt werden
* **Weniger Merge-Konflikte**: Im Team arbeitet jeder an anderen Dateien

### Separation of Concerns (Trennung der Zuständigkeiten)

Das ist ein grundlegendes Prinzip in der Softwareentwicklung:

**Metapher: Restaurant**
* **Kellner** (main.py) = Nimmt Bestellungen entgegen, serviert Essen
* **Koch** (db.py) = Bereitet Essen zu, kennt Rezepte
* **Lager** (notes.db) = Speichert Zutaten

Der Kellner muss nicht wissen, *wie* gekocht wird - er muss nur wissen, *was* er bestellen kann!

**Konkret für unsere API:**
* **main.py**: HTTP-Logik, Validierung (Pydantic), Statuscodes (404/500), Routing
* **db.py**: SQL-Queries, Connections, CRUD-Operationen, Datenbank-Fehlerbehandlung

### Neue Projektstruktur

```
mini-api/
├── venv/                # Virtual Environment (nicht in Git)
├── main.py              # FastAPI-Endpoints (die "API-Schicht")
├── db.py                # Datenbank-Funktionen (die "Daten-Schicht")
├── notes.db             # SQLite-Datenbank (nicht in Git)
├── requirements.txt     # Python-Abhängigkeiten
└── .gitignore          # Git-Ignore-Regeln
```

---

## Theorie: Error Handling

### Warum brauchen wir Error Handling?

**Ohne Error Handling:**
```python
def get_note_by_id(note_id: int):
    conn = sqlite3.connect(DATABASE)
    row = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
    conn.close()
    return dict(row)  # BOOM! Wenn row None ist
```

**Problem:** Wenn die Notiz nicht existiert, ist `row = None` → `dict(None)` wirft einen TypeError!

**Mit Error Handling:**
```python
def get_note_by_id(note_id: int):
    try:
        conn = sqlite3.connect(DATABASE)
        row = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
        conn.close()
        return dict(row) if row else None
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        return None
```

**Aber Achtung:** Hier bedeutet `None` zweierlei:
- Notiz mit dieser ID existiert nicht (normaler Fall)
- Es gab einen Datenbankfehler (Problem!)

**Das ist für Anfänger okay, aber nicht ideal.** Später (Übung 3) lernen wir, wie man beides unterscheidet!

### Warum ist Error Handling wichtig?

1. **Datenbank-Verbindung fehlschlägt**: Disk voll, Datei gesperrt, Rechte fehlen
2. **SQL-Query ist fehlerhaft**: Tippfehler im SQL-Befehl
3. **Daten sind inkonsistent**: z.B. NULL-Werte wo sie nicht sein sollten
4. **Ressourcen-Probleme**: Zu viele offene Connections
5. **Gleichzeitige Zugriffe**: SQLite kann bei parallelen Writes "database is locked" werfen

**Grundregel:** Alles, was mit externen Ressourcen (DB, Dateien, Netzwerk) zu tun hat, sollte in try-except eingewickelt sein!

**SQLite & Concurrency - Wichtiger Hinweis:**
FastAPI mit Uvicorn kann mehrere Requests parallel verarbeiten. SQLite ist datei-basiert und kann bei gleichzeitigen Schreibzugriffen "database is locked" Fehler werfen. Für unser Mini-Projekt ist das okay - bei Production-Projekten würde man PostgreSQL oder MySQL nutzen, oder SQLite mit `timeout=` Parametern konfigurieren.

---

## Theorie: Context Manager (with-Statement)

### Das Problem: Ressourcen vergessen zu schließen

**Schlechter Code - Klassischer Fehler:**
```python
def get_note(note_id: int):
    conn = sqlite3.connect(DATABASE)
    row = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
    
    if row is None:
        # PROBLEM: Connection wird NIE geschlossen!
        raise HTTPException(404, "Not found")
    
    conn.close()  # Diese Zeile wird nie erreicht!
    return dict(row)
```

**Was passiert hier?**
- Wenn ein Fehler auftritt (oder `raise` aufgerufen wird), springt Python sofort raus
- `conn.close()` wird übersprungen
- Die Datenbank-Verbindung bleibt offen → **Ressourcen-Leak!**
- Bei vielen Requests: Hunderte offene Connections → Server-Absturz

### Die Lösung: Context Manager (with-Statement)

**Guter Code - Automatisches Aufräumen:**
```python
def get_note(note_id: int):
    with sqlite3.connect(DATABASE) as conn:
        row = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
        
        if row is None:
            raise HTTPException(404, "Not found")
        
        return dict(row)
    # Connection wird AUTOMATISCH geschlossen - egal was passiert!
```

**Was macht `with`?**
1. **Beim Betreten** des Blocks: Ressource wird geöffnet
2. **Im Block**: Normale Ausführung
3. **Beim Verlassen** des Blocks: Ressource wird IMMER geschlossen - auch bei Fehlern!

**Metapher:** Das `with`-Statement ist wie eine automatische Tür:
- Du gehst rein → Tür öffnet sich
- Du machst, was du willst
- Du gehst raus → Tür schließt sich automatisch (auch wenn du rennst oder stolperst!)

### Weitere Beispiele für Context Manager

```python
# Datei-Handling
with open("datei.txt", "r") as f:
    content = f.read()
# Datei wird automatisch geschlossen

# Lock für Threading
with lock:
    # Kritischer Bereich
    pass
# Lock wird automatisch freigegeben
```

---

## Live-Coding Schritt für Schritt

### 1. db.py erstellen

Erstelle eine neue Datei `db.py` im Projektordner. Diese wird unsere gesamte Datenbank-Logik enthalten.

```python
"""
Datenbank-Modul für Mini Notes API
Enthält alle DB-Operationen mit Error Handling
"""
import sqlite3
from typing import Optional, List, Dict

# Konstante für den Datenbank-Dateinamen
DATABASE = "notes.db"


def get_connection():
    """
    Gibt eine DB-Verbindung zurück.
    
    Row Factory wird gesetzt, damit Zeilen als Dict-ähnliche Objekte
    zurückgegeben werden (statt als Tupel).
    
    timeout=5: Wartet bis zu 5 Sekunden, wenn DB gesperrt ist
    (hilfreich bei gleichzeitigen Schreibzugriffen)
    """
    conn = sqlite3.connect(DATABASE, timeout=5.0)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Erstellt die notes-Tabelle, falls sie nicht existiert.
    
    Diese Funktion wird beim Start der API aufgerufen.
    """
    try:
        with get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            print("Datenbank erfolgreich initialisiert")
    except sqlite3.Error as e:
        print(f"Fehler beim Initialisieren der Datenbank: {e}")
        raise


def get_all_notes(limit: int = 100, search: Optional[str] = None) -> List[Dict]:
    """
    Holt alle Notizen aus der Datenbank.
    
    Args:
        limit: Maximale Anzahl der Ergebnisse (Standard: 100)
        search: Optionaler Suchbegriff für Volltextsuche
    
    Returns:
        Liste von Notizen als Dictionaries
    """
    try:
        with get_connection() as conn:
            if search:
                # Suche mit LIKE-Pattern
                query = """
                    SELECT * FROM notes 
                    WHERE text LIKE ? 
                    ORDER BY id DESC
                    LIMIT ?
                """
                rows = conn.execute(query, (f"%{search}%", limit)).fetchall()
            else:
                # Alle Notizen ohne Filter
                query = "SELECT * FROM notes ORDER BY id DESC LIMIT ?"
                rows = conn.execute(query, (limit,)).fetchall()
            
            return [dict(row) for row in rows]
    
    except sqlite3.Error as e:
        print(f"Fehler beim Abrufen der Notizen: {e}")
        return []


def get_note_by_id(note_id: int) -> Optional[Dict]:
    """
    Holt eine einzelne Notiz anhand der ID.
    
    Args:
        note_id: Die ID der Notiz
    
    Returns:
        Dictionary mit der Notiz oder None, wenn nicht gefunden
    """
    try:
        with get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM notes WHERE id = ?",
                (note_id,)
            ).fetchone()
            
            return dict(row) if row else None
    
    except sqlite3.Error as e:
        print(f"Fehler beim Abrufen der Notiz {note_id}: {e}")
        return None


def create_note(text: str) -> Optional[int]:
    """
    Erstellt eine neue Notiz.
    
    Args:
        text: Der Notiz-Text
    
    Returns:
        Die ID der neuen Notiz oder None bei Fehler
    """
    try:
        with get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO notes (text) VALUES (?)",
                (text,)
            )
            conn.commit()
            return cursor.lastrowid
    
    except sqlite3.Error as e:
        print(f"Fehler beim Erstellen der Notiz: {e}")
        return None


def update_note(note_id: int, text: str) -> bool:
    """
    Aktualisiert eine bestehende Notiz.
    
    Args:
        note_id: Die ID der zu aktualisierenden Notiz
        text: Der neue Notiz-Text
    
    Returns:
        True bei Erfolg, False wenn Notiz nicht existiert oder Fehler
    """
    try:
        with get_connection() as conn:
            cursor = conn.execute(
                "UPDATE notes SET text = ? WHERE id = ?",
                (text, note_id)
            )
            conn.commit()
            return cursor.rowcount > 0
    
    except sqlite3.Error as e:
        print(f"Fehler beim Aktualisieren der Notiz {note_id}: {e}")
        return False


def delete_note(note_id: int) -> bool:
    """
    Löscht eine Notiz.
    
    Args:
        note_id: Die ID der zu löschenden Notiz
    
    Returns:
        True bei Erfolg, False wenn Notiz nicht existiert oder Fehler
    """
    try:
        with get_connection() as conn:
            cursor = conn.execute(
                "DELETE FROM notes WHERE id = ?",
                (note_id,)
            )
            conn.commit()
            return cursor.rowcount > 0
    
    except sqlite3.Error as e:
        print(f"Fehler beim Löschen der Notiz {note_id}: {e}")
        return False
```

**Was ist neu hier?**

1. **Type Hints überall:**
   - `-> Optional[Dict]`: Funktion gibt entweder ein Dictionary oder None zurück
   - `-> List[Dict]`: Funktion gibt eine Liste von Dictionaries zurück
   - `-> bool`: Funktion gibt True/False zurück
   - **Warum?** Macht den Code selbstdokumentierend und IDE kann besser helfen

2. **Docstrings:**
   - Jede Funktion hat eine Beschreibung
   - `Args:` erklärt die Parameter
   - `Returns:` erklärt, was zurückgegeben wird
   - **Warum?** Andere (und du selbst in 6 Monaten) verstehen den Code schneller

3. **Context Manager (`with`):**
   - `with get_connection() as conn:` öffnet und schließt automatisch
   - Connection wird IMMER geschlossen, auch bei Fehlern
   - **Kein** `conn.close()` mehr nötig!

4. **Error Handling (einfache Version):**
   - Jede Funktion ist in `try-except` eingepackt
   - Bei DB-Fehlern wird eine Fehlermeldung ausgegeben
   - Die Funktion gibt einen "sicheren" Rückgabewert zurück (None, [], False)
   - **Einschränkung:** DB-Fehler und "nicht gefunden" sehen gleich aus!
   - **In Übung 3** lernen wir die professionellere Variante

5. **Optional[...] aus typing:**
   - Zeigt explizit: "Kann None sein!"
   - z.B. `Optional[Dict]` = entweder ein Dictionary ODER None
   - Hilft IDEs bei Warnungen ("Du prüfst nicht auf None!")

---

### 2. main.py aufräumen

Jetzt passen wir `main.py` an, um `db.py` zu nutzen:

```python
"""
Mini Notes API - Tag 3: Strukturierte und robuste Version
Saubere Code-Aufteilung + Validierung + Error Handling
"""
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional
import db  # Unser DB-Modul importieren

# FastAPI-App mit Metadaten erstellen
app = FastAPI(
    title="Mini Notes API",
    description="Eine strukturierte API mit Validierung und Error Handling",
    version="3.0.0"
)

# Datenbank beim Start initialisieren
db.init_db()


# ========================================
# Pydantic Models für Validierung
# ========================================

class NoteCreate(BaseModel):
    """
    Schema für das Erstellen/Aktualisieren einer Notiz.
    
    Pydantic validiert automatisch:
    - text muss vorhanden sein
    - text muss zwischen 1 und 500 Zeichen lang sein
    """
    text: str = Field(
        min_length=1,
        max_length=500,
        description="Der Notiz-Text (1-500 Zeichen)"
    )


# ========================================
# API Endpoints
# ========================================

@app.get("/")
def root():
    """API-Übersicht"""
    return {
        "name": "Mini Notes API",
        "version": "3.0.0",
        "features": [
            "Modular structure",
            "Input validation",
            "Error handling",
            "Query parameters"
        ],
        "endpoints": {
            "get_all": "GET /notes?limit=10&search=wichtig",
            "get_one": "GET /notes/{id}",
            "create": "POST /notes",
            "update": "PUT /notes/{id}",
            "delete": "DELETE /notes/{id}"
        }
    }


@app.get("/health")
def health():
    """Health-Check Endpoint"""
    return {"status": "ok"}


@app.get("/notes")
def get_notes(
    limit: int = Query(100, ge=1, le=100, description="Maximale Anzahl (1-100)"),
    search: Optional[str] = Query(None, min_length=2, description="Suchbegriff (min. 2 Zeichen)")
):
    """
    Alle Notizen abrufen mit optionalen Filtern.
    
    Query Parameters:
    - limit: Maximale Anzahl der Ergebnisse (1-100, Standard: 100)
    - search: Suchbegriff für Volltextsuche (optional, mind. 2 Zeichen)
    
    Beispiele:
    - GET /notes
    - GET /notes?limit=10
    - GET /notes?search=wichtig
    - GET /notes?limit=5&search=einkauf
    """
    notes = db.get_all_notes(limit=limit, search=search)
    return notes


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """
    Eine einzelne Notiz abrufen.
    
    Path Parameter:
    - note_id: Die ID der Notiz (muss eine Zahl sein)
    """
    note = db.get_note_by_id(note_id)
    
    if note is None:
        raise HTTPException(
            status_code=404,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    return note


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    """
    Neue Notiz erstellen.
    
    Body: JSON mit 'text' Feld (1-500 Zeichen)
    
    Beispiel:
    {
        "text": "Zahnarzttermin am Freitag"
    }
    """
    new_id = db.create_note(note.text)
    
    if new_id is None:
        raise HTTPException(
            status_code=500,
            detail="Fehler beim Erstellen der Notiz"
        )
    
    return {"id": new_id, "text": note.text}


@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteCreate):
    """
    Notiz aktualisieren.
    
    Path Parameter:
    - note_id: Die ID der zu aktualisierenden Notiz
    
    Body: JSON mit neuem 'text' Feld
    """
    success = db.update_note(note_id, note.text)
    
    if not success:
        raise HTTPException(
            status_code=404,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    # Aktualisierte Notiz zurückgeben
    updated_note = db.get_note_by_id(note_id)
    
    if updated_note is None:
        # Sollte nicht passieren, aber sicherheitshalber
        raise HTTPException(
            status_code=500,
            detail="Fehler beim Laden der aktualisierten Notiz"
        )
    
    return updated_note


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    """
    Notiz löschen.
    
    Path Parameter:
    - note_id: Die ID der zu löschenden Notiz
    """
    success = db.delete_note(note_id)
    
    if not success:
        raise HTTPException(
            status_code=404,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    return {"message": "Notiz erfolgreich gelöscht", "id": note_id}
```

**Was ist hier neu?**

1. **`import db` und `from typing import Optional`:**
   - Importiert unser neues Datenbank-Modul
   - `Optional[str]` für Query-Parameter die None sein können
   - Alle DB-Details sind versteckt in `db.py`

2. **Pydantic Field mit Constraints:**
   - `min_length=1`: Mindestens 1 Zeichen (keine leeren Notizen!)
   - `max_length=500`: Maximal 500 Zeichen
   - `description`: Wird in Swagger UI angezeigt

3. **Query-Parameter mit Validierung:**
   - `Query(100, ge=1, le=100)`: Validiert limit zwischen 1 und 100
   - `Optional[str] = Query(None)`: Optional, kann fehlen
   - FastAPI erkennt automatisch: "Nicht im Pfad → Query Parameter!"
   - **Verhindert:** `/notes?limit=999999` → gibt Validierungsfehler
   - Aufruf: `/notes?limit=10&search=wichtig`

4. **Besseres Error Handling:**
   - `if note is None:` → prüft, ob DB-Funktion etwas zurückgegeben hat
   - `raise HTTPException`: Gibt einen korrekten HTTP-Fehler zurück
   - Status Codes: 404 (Not Found), 500 (Server Error), 201 (Created)
   - **Achtung:** Mit unserer aktuellen DB-Implementierung können DB-Fehler als 404 erscheinen (siehe Übung 3)

5. **Ausführliche Docstrings:**
   - Jeder Endpoint erklärt, was er tut
   - Parameter werden dokumentiert
   - Beispiele werden gezeigt
   - **Alles erscheint automatisch in Swagger UI!**

---

### 3. Query-Parameter im Detail

Query-Parameter sind die Werte nach dem `?` in einer URL.

**Beispiele:**
```
/notes                          → limit=100, search=None
/notes?limit=10                 → limit=10, search=None
/notes?search=wichtig           → limit=100, search="wichtig"
/notes?limit=5&search=einkauf   → limit=5, search="einkauf"
```

**Einfache Query-Parameter (ohne Validierung):**
```python
from typing import Optional

@app.get("/notes")
def get_notes(limit: int = 100, search: Optional[str] = None):
    #             ^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^^
    #             Parameter nicht im Pfad → Query Parameter!
    pass
```

**Query-Parameter mit Validierung (empfohlen):**
```python
from fastapi import Query
from typing import Optional

@app.get("/notes")
def get_notes(
    limit: int = Query(100, ge=1, le=100),  # Zwischen 1 und 100
    search: Optional[str] = Query(None, min_length=2)  # Mind. 2 Zeichen
):
    pass
```

**FastAPI macht automatisch:**
* Typ-Konvertierung: `limit` wird zu int konvertiert
* Validierung: Wenn `limit="abc"` oder `limit=999` → 422 Validation Error
* Optionale Parameter: `= 100` oder `= None` macht sie optional
* Dokumentation: Erscheinen in Swagger UI mit Typ und Default

**Query() Parameter:**
* `ge` = greater or equal (größer oder gleich)
* `le` = less or equal (kleiner oder gleich)
* `min_length` / `max_length` = für Strings
* `description` = Beschreibung für Swagger UI

**Vergleich: Path vs. Query Parameter:**
```python
# Path Parameter (MUSS vorhanden sein)
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    pass
# Aufruf: /notes/42

# Query Parameter (optional mit Default)
@app.get("/notes")
def get_notes(limit: int = 100):
    pass
# Aufruf: /notes oder /notes?limit=10
```

---

### 4. Validierung mit Pydantic Field

Pydantic ermöglicht sehr präzise Validierung:

```python
from pydantic import BaseModel, Field

class NoteCreate(BaseModel):
    text: str = Field(
        min_length=1,      # Mindestens 1 Zeichen
        max_length=500,    # Maximal 500 Zeichen
        description="Der Notiz-Text"
    )
```

**Was passiert bei Validierungs-Fehlern?**

**Beispiel 1: Leerer Text**
```json
POST /notes
{
  "text": ""
}
```

**Antwort: 422 Unprocessable Entity**
```json
{
  "detail": [{
    "type": "string_too_short",
    "loc": ["body", "text"],
    "msg": "String should have at least 1 character",
    "input": "",
    "ctx": {"min_length": 1}
  }]
}
```

**Beispiel 2: Zu langer Text**
```json
POST /notes
{
  "text": "A" * 501  // 501 Zeichen
}
```

**Antwort: 422 Unprocessable Entity**
```json
{
  "detail": [{
    "type": "string_too_long",
    "loc": ["body", "text"],
    "msg": "String should have at most 500 characters",
    "input": "AAA...",
    "ctx": {"max_length": 500}
  }]
}
```

**Weitere nützliche Field-Constraints:**
```python
from pydantic import Field, EmailStr

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=20, pattern="^[a-zA-Z0-9_]+$")
    email: EmailStr  # Automatische Email-Validierung
    age: int = Field(ge=18, le=120)  # ge = greater or equal, le = less or equal
    website: str = Field(default=None, regex="^https?://")  # Optionales Feld mit Pattern
```

---

## Mini-Aufgabe

**Aufgabe:** Erweitere `db.py` um eine Funktion `get_notes_count()`

Diese Funktion soll die Gesamtanzahl der Notizen in der Datenbank zurückgeben.

**Anforderungen:**
* SQL: `SELECT COUNT(*) FROM notes`
* Return-Typ: `int`
* Mit try-except Error Handling
* Mit Context Manager

**Bonus:** Erstelle auch einen neuen Endpoint `GET /notes/count` in `main.py`

<details>
<summary>Lösung anzeigen</summary>

**In db.py:**
```python
def get_notes_count() -> int:
    """
    Gibt die Gesamtanzahl der Notizen zurück.
    
    Returns:
        Anzahl der Notizen oder 0 bei Fehler
    """
    try:
        with get_connection() as conn:
            result = conn.execute("SELECT COUNT(*) FROM notes").fetchone()
            return result[0]  # COUNT(*) gibt ein Tupel zurück: (count,)
    
    except sqlite3.Error as e:
        print(f"Fehler beim Zählen der Notizen: {e}")
        return 0
```

**In main.py:**
```python
@app.get("/notes/count")
def count_notes():
    """
    Anzahl der Notizen abrufen.
    
    Gibt die Gesamtzahl aller gespeicherten Notizen zurück.
    """
    count = db.get_notes_count()
    return {
        "count": count,
        "message": f"Es sind {count} Notizen gespeichert."
    }
```

**Erklärung:**
* `COUNT(*)` ist eine SQL-Aggregat-Funktion, die die Anzahl der Zeilen zählt
* `fetchone()` gibt ein Tupel zurück: `(42,)` wenn 42 Notizen existieren
* Mit `result[0]` greifen wir auf den ersten (und einzigen) Wert zu
* Bei Fehler geben wir `0` zurück (sicherer als `None`)

</details>

---

## Übungen für Tag 3

### Übung 1: Validierung mit Pydantic Model (fortgeschritten)

Wir haben bereits `Query()` für die Validierung genutzt. Eine alternative, fortgeschrittenere Methode ist ein Pydantic-Model für Query-Parameter.

**Aufgabe:** Erstelle ein Pydantic-Model `NoteFilter` und nutze es mit Dependency Injection.

**Anforderungen:**
* `limit` muss zwischen 1 und 100 liegen
* `search` ist optional, aber wenn vorhanden, mindestens 2 Zeichen
* Nutze `Depends()` für Dependency Injection

<details>
<summary>Lösung anzeigen</summary>

```python
from pydantic import BaseModel, Field
from typing import Optional

class NoteFilter(BaseModel):
    """Schema für Query-Parameter beim Abrufen von Notizen."""
    limit: int = Field(
        default=100,
        ge=1,  # greater or equal
        le=100,  # less or equal
        description="Maximale Anzahl der Ergebnisse"
    )
    search: Optional[str] = Field(
        default=None,
        min_length=2,
        description="Suchbegriff (min. 2 Zeichen)"
    )

# In main.py verwenden:
@app.get("/notes")
def get_notes(filters: NoteFilter = Depends()):
    notes = db.get_all_notes(limit=filters.limit, search=filters.search)
    return notes
```

**Hinweis:** `Depends()` ist eine FastAPI-Funktion für Dependency Injection. Das ist etwas fortgeschrittener, aber sehr mächtig für komplexere Anwendungen!

**Einfachere Version ohne Depends:**
```python
@app.get("/notes")
def get_notes(
    limit: int = Field(default=100, ge=1, le=100),
    search: Optional[str] = Field(default=None, min_length=2)
):
    notes = db.get_all_notes(limit=limit, search=search)
    return notes
```

</details>

---

### Übung 2: Logging statt print

Ersetze alle `print()`-Statements in `db.py` durch Python's `logging`-Modul.

**Warum Logging?**
* Professioneller als `print()`
* Log-Level (DEBUG, INFO, WARNING, ERROR)
* Kann in Dateien geschrieben werden
* Wird in Production oft gebraucht

<details>
<summary>Lösung anzeigen</summary>

**Am Anfang von db.py hinzufügen:**
```python
import logging

# Logger konfigurieren
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
```

**print() ersetzen durch logger:**
```python
def init_db():
    """Erstellt die notes-Tabelle, falls sie nicht existiert."""
    try:
        with get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            logger.info("Datenbank erfolgreich initialisiert")
    except sqlite3.Error as e:
        logger.error(f"Fehler beim Initialisieren der Datenbank: {e}")
        raise

def get_note_by_id(note_id: int) -> Optional[Dict]:
    """Holt eine einzelne Notiz anhand der ID."""
    try:
        with get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM notes WHERE id = ?",
                (note_id,)
            ).fetchone()
            
            return dict(row) if row else None
    
    except sqlite3.Error as e:
        logger.error(f"Fehler beim Abrufen der Notiz {note_id}: {e}")
        return None
```

**Log-Levels:**
* `logger.debug()`: Detaillierte Debug-Informationen
* `logger.info()`: Bestätigung, dass alles wie erwartet funktioniert
* `logger.warning()`: Etwas Unerwartetes passiert, aber funktioniert noch
* `logger.error()`: Ernstes Problem, Funktion konnte nicht ausgeführt werden
* `logger.critical()`: Sehr ernstes Problem, Programm kann möglicherweise nicht weiterlaufen

</details>

---

### Übung 3: DB-Fehler vs. "Nicht gefunden" unterscheiden (wichtig!)

**Problem:** In unserer aktuellen Implementierung geben die DB-Funktionen bei Fehlern `None`/`False`/`[]` zurück - genau wie bei "nicht gefunden". Das führt zu falschen HTTP-Status-Codes!

**Beispiel des Problems:**
```python
# In db.py:
def get_note_by_id(note_id: int):
    try:
        # ... DB-Query
        return dict(row) if row else None
    except sqlite3.Error:
        return None  # Problem: Sieht aus wie "nicht gefunden"!

# In main.py:
note = db.get_note_by_id(42)
if note is None:
    raise HTTPException(404, "Not found")  # Falsch bei DB-Fehler!
```

**Aufgabe:** Implementiere eine bessere Fehlerbehandlung, die unterscheidet zwischen:
1. **Ressource nicht gefunden** → 404
2. **Datenbankfehler** → 500

**Zwei Lösungsansätze:**

<details>
<summary>Lösung A: DB-Fehler durchreichen (einfacher)</summary>

**In db.py - Lass DB-Fehler durchgehen:**
```python
def get_note_by_id(note_id: int) -> Optional[Dict]:
    """
    Holt eine einzelne Notiz anhand der ID.
    
    Returns:
        Dictionary mit der Notiz oder None wenn nicht gefunden
    
    Raises:
        sqlite3.Error: Bei Datenbankfehlern
    """
    # Kein try-except! Fehler werden nach oben durchgereicht
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM notes WHERE id = ?",
            (note_id,)
        ).fetchone()
        
        return dict(row) if row else None
```

**In main.py - Fange DB-Fehler ab:**
```python
import sqlite3

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """Eine einzelne Notiz abrufen."""
    try:
        note = db.get_note_by_id(note_id)
        
        if note is None:
            raise HTTPException(404, f"Notiz {note_id} nicht gefunden")
        
        return note
    
    except sqlite3.Error as e:
        # Echter Datenbankfehler!
        raise HTTPException(500, "Datenbankfehler aufgetreten")
```

**Vorteil:** Klar getrennt - 404 nur bei "nicht gefunden", 500 bei DB-Fehler  
**Nachteil:** Jeder Endpoint muss try-except haben

</details>

<details>
<summary>Lösung B: Custom Exception + Global Handler (professioneller)</summary>

**Schritt 1: Eigene Exception definieren (z.B. in db.py):**
```python
class DatabaseError(Exception):
    """Custom Exception für Datenbankfehler."""
    pass

def get_note_by_id(note_id: int) -> Optional[Dict]:
    """Holt eine einzelne Notiz anhand der ID."""
    try:
        with get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM notes WHERE id = ?",
                (note_id,)
            ).fetchone()
            
            return dict(row) if row else None
    
    except sqlite3.Error as e:
        # Werfe unsere eigene Exception
        raise DatabaseError(f"Fehler beim Abrufen der Notiz {note_id}: {e}")
```

**Schritt 2: Global Exception Handler in main.py:**
```python
from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)

@app.exception_handler(db.DatabaseError)
async def database_exception_handler(request: Request, exc: db.DatabaseError):
    """Globaler Handler für Datenbankfehler."""
    logger.error(f"DB-Fehler bei {request.method} {request.url}: {exc}")
    
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Ein Datenbankfehler ist aufgetreten",
            "path": str(request.url)
        }
    )
```

**Schritt 3: Endpoints bleiben sauber:**
```python
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """Eine einzelne Notiz abrufen."""
    note = db.get_note_by_id(note_id)  # Kann DatabaseError werfen
    
    if note is None:
        raise HTTPException(404, f"Notiz {note_id} nicht gefunden")
    
    return note
```

**Vorteil:** Saubere Trennung, Endpoints brauchen kein try-except  
**Nachteil:** Etwas mehr Setup-Code

</details>

**Welche Lösung wählen?**
* **Für kleine Projekte:** Lösung A (einfacher)
* **Für größere Projekte:** Lösung B (wartbarer, professioneller)

**Wichtig:** Beide Lösungen sind besser als die aktuelle Version, die DB-Fehler als 404 ausgibt!



---

### Übung 4 (Bonus): Connection Pool

Für sehr viele gleichzeitige Anfragen wäre ein Connection Pool sinnvoll. Recherchiere, was ein Connection Pool ist und wie man ihn in Python umsetzt.

**Hinweis:** Für SQLite ist das weniger relevant (da Datei-basiert), aber für PostgreSQL/MySQL wichtig!

<details>
<summary>Hintergrundwissen</summary>

**Was ist ein Connection Pool?**

Stell dir vor, du hast ein Restaurant:
* **Ohne Pool**: Für jeden Gast wird ein neuer Tisch aufgebaut und danach wieder abgebaut
* **Mit Pool**: Es gibt 10 feste Tische, die zwischen den Gästen wiederverwendet werden

**Connection Pool:**
* Erstellt X Datenbankverbindungen beim Start
* Wenn eine Anfrage kommt, wird eine freie Connection aus dem Pool genommen
* Nach der Nutzung wird sie zurück in den Pool gelegt (nicht geschlossen!)
* Spart Zeit: Connection aufbauen ist teuer!

**Für SQLite:**
SQLite unterstützt keine echten parallelen Schreibzugriffe, daher ist ein Pool hier weniger sinnvoll.

**Für PostgreSQL/MySQL:**
```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

# Connection Pool mit SQLAlchemy
engine = create_engine(
    "postgresql://user:password@localhost/dbname",
    poolclass=QueuePool,
    pool_size=10,        # Max. 10 Connections im Pool
    max_overflow=20,     # Zusätzlich 20 temporäre Connections erlaubt
    pool_timeout=30,     # 30 Sekunden warten auf freie Connection
)

def get_connection():
    return engine.connect()
```

**Vorteile:**
* Schnellere Anfragen (keine neue Connection-Aufbau jedes Mal)
* Ressourcen-Kontrolle (max. X Connections)
* Automatisches Recycling defekter Connections

</details>

---

## Zusammenfassung Tag 3

**Was haben wir gelernt?**

**Code-Strukturierung:**
- Module erstellen (`db.py`, `main.py`)
- Separation of Concerns umsetzen
- Import und Verwendung eigener Module

**Validierung mit Pydantic:**
- `Field()` mit Constraints (`min_length`, `max_length`)
- Type Hints für bessere Code-Qualität
- Automatische Fehler bei ungültigen Daten

**Query-Parameter:**
- Optionale Parameter mit Defaults
- URL-Format: `/notes?limit=10&search=test`
- Automatische Typ-Konvertierung und Validierung

**Error Handling:**
- `try-except` für alle DB-Operationen
- Sichere Rückgabewerte bei Fehlern
- HTTPException für korrekte HTTP-Status-Codes
- **Wichtig:** In unserer einfachen Variante werden DB-Fehler und "nicht gefunden" gleich behandelt (siehe Übung 3 für professionellere Lösung mit korrekten 404/500 Status-Codes)

**Context Manager:**
- `with`-Statement für automatisches Cleanup
- Ressourcen werden IMMER freigegeben
- Verhindert Connection-Leaks

**Best Practices:**
- Docstrings für Dokumentation
- Type Hints für Typsicherheit
- Logging statt print (Übung)
- Konsistente Fehlerbehandlung

---

## Ausblick auf Tag 4

Morgen werden wir noch professioneller:

**Geplante Themen:**
* **Async/Await**: Asynchrone DB-Operationen für bessere Performance
* **Dependency Injection**: Wiederverwendbare Abhängigkeiten
* **Middleware**: Logging, CORS, Request-Timing
* **Testing**: Unittests für API und DB-Funktionen
* **Environment Variables**: Konfiguration aus .env-Datei

**Besonders spannend: Testing!**
Wir werden lernen, wie man:
* Endpoints automatisch testet
* Eine Test-Datenbank nutzt
* Mocks für DB-Funktionen erstellt

---

## Finale Code-Versionen

### db.py - Finale Version Tag 3

```python
"""
Datenbank-Modul für Mini Notes API - Tag 3
Enthält alle DB-Operationen mit Error Handling und Context Manager
"""
import sqlite3
from typing import Optional, List, Dict

DATABASE = "notes.db"


def get_connection():
    """
    Gibt eine DB-Verbindung mit Row Factory zurück.
    
    timeout=5: Wartet bis zu 5 Sekunden, wenn DB gesperrt ist
    (hilfreich bei gleichzeitigen Schreibzugriffen)
    
    Returns:
        sqlite3.Connection mit row_factory = sqlite3.Row
    """
    conn = sqlite3.connect(DATABASE, timeout=5.0)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Erstellt die notes-Tabelle, falls sie nicht existiert.
    
    Raises:
        sqlite3.Error: Bei Datenbankfehlern
    """
    try:
        with get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT NOT NULL,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            print("Datenbank erfolgreich initialisiert")
    except sqlite3.Error as e:
        print(f"Fehler beim Initialisieren der Datenbank: {e}")
        raise


def get_all_notes(limit: int = 100, search: Optional[str] = None) -> List[Dict]:
    """
    Holt alle Notizen mit optionalen Filtern.
    
    Args:
        limit: Maximale Anzahl der Ergebnisse
        search: Optionaler Suchbegriff für Volltextsuche
    
    Returns:
        Liste von Notizen als Dictionaries
    """
    try:
        with get_connection() as conn:
            if search:
                query = """
                    SELECT * FROM notes 
                    WHERE text LIKE ? 
                    ORDER BY id DESC
                    LIMIT ?
                """
                rows = conn.execute(query, (f"%{search}%", limit)).fetchall()
            else:
                query = "SELECT * FROM notes ORDER BY id DESC LIMIT ?"
                rows = conn.execute(query, (limit,)).fetchall()
            
            return [dict(row) for row in rows]
    
    except sqlite3.Error as e:
        print(f"Fehler beim Abrufen der Notizen: {e}")
        return []


def get_note_by_id(note_id: int) -> Optional[Dict]:
    """
    Holt eine einzelne Notiz anhand der ID.
    
    Args:
        note_id: Die ID der Notiz
    
    Returns:
        Dictionary mit der Notiz oder None, wenn nicht gefunden
    """
    try:
        with get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM notes WHERE id = ?",
                (note_id,)
            ).fetchone()
            
            return dict(row) if row else None
    
    except sqlite3.Error as e:
        print(f"Fehler beim Abrufen der Notiz {note_id}: {e}")
        return None


def create_note(text: str) -> Optional[int]:
    """
    Erstellt eine neue Notiz.
    
    Args:
        text: Der Notiz-Text
    
    Returns:
        Die ID der neuen Notiz oder None bei Fehler
    """
    try:
        with get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO notes (text) VALUES (?)",
                (text,)
            )
            conn.commit()
            return cursor.lastrowid
    
    except sqlite3.Error as e:
        print(f"Fehler beim Erstellen der Notiz: {e}")
        return None


def update_note(note_id: int, text: str) -> bool:
    """
    Aktualisiert eine bestehende Notiz.
    
    Args:
        note_id: Die ID der zu aktualisierenden Notiz
        text: Der neue Notiz-Text
    
    Returns:
        True bei Erfolg, False wenn Notiz nicht existiert oder Fehler
    """
    try:
        with get_connection() as conn:
            cursor = conn.execute(
                "UPDATE notes SET text = ? WHERE id = ?",
                (text, note_id)
            )
            conn.commit()
            return cursor.rowcount > 0
    
    except sqlite3.Error as e:
        print(f"Fehler beim Aktualisieren der Notiz {note_id}: {e}")
        return False


def delete_note(note_id: int) -> bool:
    """
    Löscht eine Notiz.
    
    Args:
        note_id: Die ID der zu löschenden Notiz
    
    Returns:
        True bei Erfolg, False wenn Notiz nicht existiert oder Fehler
    """
    try:
        with get_connection() as conn:
            cursor = conn.execute(
                "DELETE FROM notes WHERE id = ?",
                (note_id,)
            )
            conn.commit()
            return cursor.rowcount > 0
    
    except sqlite3.Error as e:
        print(f"Fehler beim Löschen der Notiz {note_id}: {e}")
        return False


def get_notes_count() -> int:
    """
    Gibt die Gesamtanzahl der Notizen zurück.
    
    Returns:
        Anzahl der Notizen oder 0 bei Fehler
    """
    try:
        with get_connection() as conn:
            result = conn.execute("SELECT COUNT(*) FROM notes").fetchone()
            return result[0]
    
    except sqlite3.Error as e:
        print(f"Fehler beim Zählen der Notizen: {e}")
        return 0
```

---

### main.py - Finale Version Tag 3

```python
"""
Mini Notes API - Tag 3: Strukturierte und robuste Version
=========================================================
Features:
- Modulare Code-Struktur (main.py + db.py)
- Input-Validierung mit Pydantic
- Query-Parameter mit Validierung (limit, search)
- Error Handling mit try-except
- Context Manager für DB-Connections
"""
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional
import db

# FastAPI-App erstellen
app = FastAPI(
    title="Mini Notes API",
    description="Eine strukturierte API mit Validierung und Error Handling",
    version="3.0.0"
)

# Datenbank beim Start initialisieren
db.init_db()


# ========================================
# Pydantic Models
# ========================================

class NoteCreate(BaseModel):
    """Schema für das Erstellen/Aktualisieren einer Notiz."""
    text: str = Field(
        min_length=1,
        max_length=500,
        description="Der Notiz-Text (1-500 Zeichen)"
    )


# ========================================
# API Endpoints
# ========================================

@app.get("/")
def root():
    """API-Übersicht mit allen verfügbaren Endpoints"""
    return {
        "name": "Mini Notes API",
        "version": "3.0.0",
        "features": [
            "Modular structure",
            "Input validation",
            "Error handling",
            "Query parameters"
        ],
        "endpoints": {
            "get_all": "GET /notes?limit=10&search=wichtig",
            "get_one": "GET /notes/{id}",
            "create": "POST /notes",
            "update": "PUT /notes/{id}",
            "delete": "DELETE /notes/{id}",
            "count": "GET /notes/count"
        }
    }


@app.get("/health")
def health():
    """Health-Check Endpoint"""
    return {"status": "ok"}


@app.get("/notes")
def get_notes(
    limit: int = Query(100, ge=1, le=100, description="Maximale Anzahl (1-100)"),
    search: Optional[str] = Query(None, min_length=2, description="Suchbegriff (min. 2 Zeichen)")
):
    """
    Alle Notizen abrufen mit optionalen Filtern.
    
    Query Parameters:
    - limit: Maximale Anzahl der Ergebnisse (1-100, Standard: 100)
    - search: Suchbegriff für Volltextsuche (optional, mind. 2 Zeichen)
    
    Beispiele:
    - GET /notes
    - GET /notes?limit=10
    - GET /notes?search=wichtig
    - GET /notes?limit=5&search=einkauf
    """
    notes = db.get_all_notes(limit=limit, search=search)
    return notes


@app.get("/notes/count")
def count_notes():
    """
    Anzahl der Notizen abrufen.
    
    Gibt die Gesamtzahl aller gespeicherten Notizen zurück.
    """
    count = db.get_notes_count()
    return {
        "count": count,
        "message": f"Es sind {count} Notizen gespeichert."
    }


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """
    Eine einzelne Notiz abrufen.
    
    Path Parameter:
    - note_id: Die ID der Notiz (muss eine Zahl sein)
    """
    note = db.get_note_by_id(note_id)
    
    if note is None:
        raise HTTPException(
            status_code=404,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    return note


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    """
    Neue Notiz erstellen.
    
    Body: JSON mit 'text' Feld (1-500 Zeichen)
    
    Beispiel:
    {
        "text": "Zahnarzttermin am Freitag"
    }
    """
    new_id = db.create_note(note.text)
    
    if new_id is None:
        raise HTTPException(
            status_code=500,
            detail="Fehler beim Erstellen der Notiz"
        )
    
    return {"id": new_id, "text": note.text}


@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteCreate):
    """
    Notiz aktualisieren.
    
    Path Parameter:
    - note_id: Die ID der zu aktualisierenden Notiz
    
    Body: JSON mit neuem 'text' Feld
    """
    success = db.update_note(note_id, note.text)
    
    if not success:
        raise HTTPException(
            status_code=404,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    # Aktualisierte Notiz zurückgeben
    updated_note = db.get_note_by_id(note_id)
    
    if updated_note is None:
        # Sollte nicht passieren, aber sicherheitshalber
        raise HTTPException(
            status_code=500,
            detail="Fehler beim Laden der aktualisierten Notiz"
        )
    
    return updated_note


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    """
    Notiz löschen.
    
    Path Parameter:
    - note_id: Die ID der zu löschenden Notiz
    """
    success = db.delete_note(note_id)
    
    if not success:
        raise HTTPException(
            status_code=404,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    return {"message": "Notiz erfolgreich gelöscht", "id": note_id}
```

---

## Projekt-Struktur Tag 3

So sieht euer Projekt jetzt aus:

```
mini-api/
├── venv/                # Virtual Environment (nicht in Git)
├── main.py              # API-Endpoints (ca. 120 Zeilen)
├── db.py                # Datenbank-Funktionen (ca. 150 Zeilen)
├── notes.db             # SQLite-Datenbank (nicht in Git)
├── requirements.txt     # Python-Abhängigkeiten
└── .gitignore          # Git-Ignore-Regeln
```

**Vergleich zu Tag 2:**
* **Vorher:** Eine Datei, 200+ Zeilen, alles vermischt
* **Jetzt:** Zwei Dateien, jede hat klare Verantwortung, einfach zu warten

---

## Checkliste Tag 3

- [ ] `db.py` erstellt mit allen DB-Funktionen
- [ ] `main.py` aufgeräumt und db-Modul importiert
- [ ] Context Manager (`with`) verstanden und angewendet
- [ ] Error Handling in allen DB-Funktionen
- [ ] Pydantic Field mit Validierung implementiert
- [ ] Query-Parameter `limit` und `search` funktionieren
- [ ] `GET /notes/count` Endpoint erstellt (Mini-Aufgabe)
- [ ] Code ist sauber strukturiert und dokumentiert
- [ ] Swagger UI getestet
- [ ] Änderungen mit Git committed

**Bonus:**
- [ ] Logging statt print implementiert (Übung 2)
- [ ] Custom Exception Handler erstellt (Übung 3)
- [ ] Type Hints überall verwendet

---

## Best Practices Zusammenfassung

** Code-Organisation:**
* Eine Datei = Eine Verantwortung
* Module statt Copy-Paste
* Imports am Anfang der Datei

** Error Handling:**
* Try-except für alle externen Operationen
* Sichere Rückgabewerte (None, [], False)
* Spezifische Exceptions abfangen (`sqlite3.Error`)

** Ressourcen-Management:**
* Context Manager für DB-Connections
* Keine manuellen `close()`-Aufrufe mehr
* Automatisches Cleanup garantiert

** Dokumentation:**
* Docstrings für alle Funktionen
* Type Hints für Parameter und Return
* Beispiele in der Dokumentation

** API-Design:**
* Korrekte HTTP-Status-Codes (200, 201, 404, 500)
* Beschreibende Fehlermeldungen
* Query-Parameter für Filter
* Path-Parameter für Ressourcen-IDs

---


**Bei Fragen meldet euch bei Patrick oder mir. Viel Erfolg und bis morgen!**
