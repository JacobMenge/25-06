# Tag 2: SQLite anbinden + CRUD-Operationen

## Lernziele
* SQLite verstehen und als persistente Datenspeicherung einrichten
* Datenbank-Tabellen erstellen und verstehen
* CRUD-Operationen implementieren (Create, Read, Update, Delete)
* Mit SQL-Abfragen arbeiten und SQL-Injection vermeiden
* POST-, PUT- und DELETE-Requests in FastAPI nutzen
* Daten bleiben nach Neustart der API erhalten!

---

## Theorie: Was ist SQLite?

### Was ist eine Datenbank?

Stell dir eine Datenbank wie einen **digitalen Aktenschrank** vor:
- **In-Memory-Daten (Tag 1)** = Post-it-Zettel auf deinem Schreibtisch → weg, wenn du aufräumst
- **SQLite-Datenbank** = Ordner im Aktenschrank → bleiben für immer, bis du sie löschst

Eine Datenbank speichert strukturierte Daten dauerhaft auf der Festplatte.

### Warum SQLite?

**SQLite ist perfekt für:**
* **Einfache bis mittlere Projekte** (bis zu Hunderttausenden von Einträgen)
* **Prototypen und MVPs** (Minimum Viable Products)
* **Desktop-Anwendungen** (z.B. Browser nutzen SQLite!)
* **Embedded Systems** und IoT-Geräte
* **Entwicklung und Testing** (bevor man zu größeren DBs wie PostgreSQL wechselt)

**Vorteile von SQLite:**
* **Serverlos**: Keine separate Datenbank-Installation nötig
* **Eine Datei = komplette Datenbank**: `notes.db` enthält alles
* **In Python eingebaut**: `import sqlite3` - keine Installation nötig!
* **Schnell**: Optimal für Read-Heavy-Workloads
* **Zuverlässig**: Wird in Milliarden von Geräten weltweit genutzt
* **ACID-konform**: Garantiert Datenkonsistenz

**Einschränkungen von SQLite:**
* **Nicht für viele gleichzeitige Schreibzugriffe** (Writes sind seriell)
* **Keine User-Management-Features** (für Production oft PostgreSQL/MySQL besser)
* **Begrenzte Größe** (theoretisch 281 TB, praktisch aber besser unter 1 GB)

### Vergleich zu Tag 1

| Aspekt | In-Memory (Tag 1) | SQLite (heute) |
|--------|------------------|----------------|
| **Speicherort** | RAM (flüchtig) | Festplatte (persistent) |
| **Nach Neustart** | Daten weg | Daten bleiben erhalten |
| **Performance** | Sehr schnell | Etwas langsamer, aber immer noch schnell |
| **Skalierbar** | Nein | Ja (bis zu einem gewissen Grad) |
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
=======================================
Jetzt mit persistenter Datenspeicherung!
Alle Daten bleiben nach Neustart erhalten.
"""
import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime

# FastAPI-App erstellen
app = FastAPI(
    title="Mini Notes API",
    description="Eine API zum Speichern von Notizen mit SQLite-Datenbank",
    version="2.0.0"
)

# Datenbank-Dateiname
DATABASE = "notes.db"

def init_db():
    """
    Initialisiert die Datenbank und erstellt die Tabelle.
    
    Wird beim Start/Import der API ausgeführt.
    Mit uvicorn --reload kann dies mehrfach passieren (bei Code-Änderungen),
    ist aber dank IF NOT EXISTS unkritisch.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Tabelle erstellen (IF NOT EXISTS = sicher, kann mehrfach aufgerufen werden)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()
    print("Datenbank initialisiert!")

# Datenbank beim Start der API initialisieren
init_db()
```

**Code-Erklärung Zeile für Zeile:**

1. **`import sqlite3`**: Python's eingebautes SQLite-Modul
2. **`DATABASE = "notes.db"`**: Name unserer Datenbank-Datei
   - Diese Datei wird automatisch erstellt, wenn sie nicht existiert
   - Sie liegt im selben Ordner wie `main.py`
3. **`def init_db():`**: Funktion zur Datenbank-Initialisierung
4. **`sqlite3.connect(DATABASE)`**: Öffnet eine Verbindung zur Datenbank
   - Wenn die Datei nicht existiert, wird sie erstellt
   - Diese Verbindung muss später mit `.close()` geschlossen werden!
5. **`cursor = conn.cursor()`**: Erstellt einen Cursor
   - Der Cursor führt SQL-Befehle aus (wie ein Zeiger in der DB)
6. **SQL-Befehl `CREATE TABLE IF NOT EXISTS`**:
   - **`CREATE TABLE`**: Erstellt eine neue Tabelle
   - **`IF NOT EXISTS`**: Nur erstellen, wenn sie noch nicht da ist (wichtig!)
   - **`id INTEGER PRIMARY KEY AUTOINCREMENT`**: 
     - `INTEGER`: Ganzzahl
     - `PRIMARY KEY`: Eindeutiger Identifikator (jede Zeile hat eine einzigartige ID)
     - `AUTOINCREMENT`: ID wird automatisch hochgezählt (1, 2, 3, ...)
   - **`text TEXT NOT NULL`**:
     - `TEXT`: String/Text
     - `NOT NULL`: Darf nicht leer sein
   - **`created_at TEXT DEFAULT CURRENT_TIMESTAMP`**:
     - `TEXT`: Wir speichern das Datum als Text
     - `DEFAULT CURRENT_TIMESTAMP`: Wird automatisch auf die aktuelle Zeit gesetzt
     - SQLite liefert das Format `YYYY-MM-DD HH:MM:SS` in UTC (z.B. "2025-12-01 10:30:00")
7. **`conn.commit()`**: Speichert die Änderungen in der Datenbank
   - **Wichtig:** Ohne `commit()` gehen Änderungen verloren!
8. **`conn.close()`**: Schließt die Verbindung
   - **Wichtig:** Immer die Verbindung schließen, sonst können Probleme entstehen!

**Was ist der Unterschied zwischen `cursor` und `connection`?**
- **Connection**: Die Verbindung zur Datenbank-Datei (wie eine Telefonleitung)
- **Cursor**: Das Werkzeug, um SQL-Befehle auszuführen (wie ein Telefonhörer)

---

### 3. Root- und Health-Endpoints beibehalten

Füge jetzt die Basic-Endpoints hinzu (diese bleiben fast unverändert):

```python
@app.get("/")
def root():
    """
    API-Übersicht
    
    Gibt grundlegende Informationen über die API zurück.
    """
    return {
        "name": "Mini Notes API",
        "description": "Eine API zum Speichern von Notizen mit SQLite-Datenbank",
        "version": "2.0.0",
        "database": "SQLite (persistent)",
        "endpoints": ["/health", "/notes", "/notes/{id}"],
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    """
    Health-Check Endpoint mit DB-Status
    
    Prüft, ob die API UND die Datenbank erreichbar sind.
    """
    # Datenbank-Verbindung testen
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM notes")
        count = cursor.fetchone()[0]
        conn.close()
        db_status = "ok"
    except Exception as e:
        db_status = f"error: {str(e)}"
        count = None
    
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "database": db_status,
        "notes_count": count
    }
```

**Neu im Health-Check:**
- Wir testen jetzt auch die Datenbank-Verbindung
- Zeigt die Anzahl der Notizen an
- Falls die DB nicht erreichbar ist, wird ein Fehler angezeigt

---

### 4. GET /notes - Alle Notizen aus der Datenbank lesen

Jetzt kommt der erste "richtige" Datenbank-Endpoint:

```python
@app.get("/notes")
def get_all_notes():
    """
    Alle Notizen abrufen
    
    Liest alle Notizen aus der SQLite-Datenbank und gibt sie zurück.
    """
    conn = sqlite3.connect(DATABASE)
    
    # row_factory ermöglicht Dict-Zugriff auf Zeilen
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    
    # Konvertiere Row-Objekte zu Dictionaries
    return [dict(row) for row in rows]
```

**Code-Erklärung:**

1. **`conn.row_factory = sqlite3.Row`**: 
   - Ohne diese Zeile bekommen wir nur Tupel zurück: `(1, "Text", "2025-12-01")`
   - Mit dieser Zeile bekommen wir Dict-ähnliche Objekte: `{"id": 1, "text": "Text", ...}`
   - Das macht die Arbeit viel einfacher!
2. **`SELECT * FROM notes ORDER BY id DESC`**:
   - `SELECT *`: Wähle alle Spalten aus
   - `FROM notes`: Aus der Tabelle "notes"
   - `ORDER BY id DESC`: Sortiere nach ID, neueste zuerst (DESC = descending)
3. **`cursor.fetchall()`**: Holt alle Ergebnisse auf einmal
   - Gibt eine Liste von Row-Objekten zurück
   - Alternative: `fetchone()` für nur ein Ergebnis
4. **`[dict(row) for row in rows]`**: List Comprehension
   - Wandelt jedes Row-Objekt in ein normales Dictionary um
   - FastAPI wandelt das dann automatisch in JSON um

**Wichtige SQL-Basics:**

| SQL-Befehl | Bedeutung | Beispiel |
|------------|-----------|----------|
| `SELECT` | Daten abrufen | `SELECT * FROM notes` |
| `INSERT` | Daten einfügen | `INSERT INTO notes (text) VALUES (?)` |
| `UPDATE` | Daten ändern | `UPDATE notes SET text = ? WHERE id = ?` |
| `DELETE` | Daten löschen | `DELETE FROM notes WHERE id = ?` |

---

### 5. Pydantic Model für Validierung

Bevor wir POST implementieren, brauchen wir ein Datenmodell:

```python
from pydantic import BaseModel, Field

class NoteCreate(BaseModel):
    """
    Schema für das Erstellen einer neuen Notiz.
    
    Pydantic validiert automatisch:
    - Feld 'text' ist vorhanden
    - Typ ist String
    - Mindestlänge ist 1 Zeichen (darf nicht leer sein)
    """
    text: str = Field(min_length=1, examples=["Einkaufen gehen: Milch, Brot, Eier"])
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "text": "Einkaufen gehen: Milch, Brot, Eier"
            }
        }
    }
```

**Was ist Pydantic?**
- Pydantic ist eine **Datenvalidierungs-Bibliothek**
- Sie prüft automatisch, ob die empfangenen Daten das richtige Format haben
- Wenn ein Feld fehlt oder falsch ist, gibt FastAPI automatisch einen Fehler zurück
- Die `Config`-Klasse fügt ein Beispiel zur Swagger-Dokumentation hinzu

**Warum ist das wichtig?**
Ohne Pydantic müsstest du manuell prüfen:
```python
if "text" not in data:
    return {"error": "text is required"}
if not isinstance(data["text"], str):
    return {"error": "text must be a string"}
if len(data["text"]) == 0:
    return {"error": "text cannot be empty"}
```

Mit Pydantic: `note: NoteCreate` - FastAPI validiert automatisch Typ, Vorhandensein und Mindestlänge! 

---

### 6. POST /notes - Neue Notiz erstellen

Jetzt implementieren wir das Erstellen von Notizen:

```python
@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    """
    Neue Notiz erstellen
    
    Erstellt eine neue Notiz in der Datenbank und gibt sie zurück.
    Der HTTP-Statuscode 201 signalisiert erfolgreiche Erstellung.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # WICHTIG: ? als Platzhalter verwenden (SQL-Injection-Schutz!)
    cursor.execute(
        "INSERT INTO notes (text) VALUES (?)",
        (note.text,)  # Tuple mit einem Element (Komma beachten!)
    )
    
    # ID der neu erstellten Notiz
    new_id = cursor.lastrowid
    
    conn.commit()
    conn.close()
    
    return {
        "id": new_id,
        "text": note.text,
        "message": "Notiz erfolgreich erstellt"
    }
```

**Code-Erklärung:**

1. **`@app.post("/notes", status_code=201)`**:
   - POST statt GET (POST = Daten erstellen/senden)
   - `status_code=201`: HTTP "Created" - zeigt erfolgreiche Erstellung an
2. **`note: NoteCreate`**: Pydantic validiert automatisch!
3. **`INSERT INTO notes (text) VALUES (?)`**:
   - Fügt eine neue Zeile in die Tabelle ein
   - `?` ist ein **Platzhalter** (wird durch `note.text` ersetzt)
4. **`(note.text,)`**: Tuple mit einem Element
   - **Wichtig:** Das Komma ist notwendig! `(note.text,)` ist ein Tuple, `(note.text)` nur eine geklammerte Variable
5. **`cursor.lastrowid`**: Die ID der gerade eingefügten Zeile
   - SQLite gibt automatisch die letzte eingefügte ID zurück
6. **`conn.commit()`**: Speichert die Änderungen
   - **Ohne commit() wird nichts gespeichert!**

**🚨 KRITISCH: SQL-Injection verhindern!**

**NIEMALS so:**
```python
# GEFÄHRLICH - SQL-Injection möglich!
cursor.execute(f"INSERT INTO notes (text) VALUES ('{note.text}')")
```

**Warum ist das gefährlich?**
Wenn `note.text` den Wert `"'); DROP TABLE notes; --"` hat, würde das Statement:
```sql
INSERT INTO notes (text) VALUES (''); DROP TABLE notes; --')
```
Das würde die gesamte Tabelle löschen!

**IMMER so:**
```python
# SICHER - Parameter-Binding
cursor.execute("INSERT INTO notes (text) VALUES (?)", (note.text,))
```

Mit `?`-Platzhaltern wird der Text automatisch escaped und ist sicher!

---

### 7. GET /notes/{note_id} - Einzelne Notiz abrufen

Jetzt implementieren wir das Abrufen einer einzelnen Notiz:

```python
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """
    Eine einzelne Notiz abrufen
    
    Gibt die Notiz mit der angegebenen ID zurück.
    Falls die ID nicht existiert, wird ein 404-Fehler zurückgegeben.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT * FROM notes WHERE id = ?",
        (note_id,)
    )
    row = cursor.fetchone()
    conn.close()
    
    if row is None:
        raise HTTPException(
            status_code=404,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    return dict(row)
```

**Neu hier: Path Parameters**

- **`{note_id}`** in der URL wird zu einem Parameter in der Funktion
- FastAPI extrahiert automatisch die ID aus der URL
- **Type Hint `note_id: int`**: FastAPI konvertiert automatisch zu Integer
  - Bei `/notes/abc` → Automatischer 422-Fehler (Validation Error)
  - Bei `/notes/5` → `note_id = 5`

**Beispiele:**
- `GET /notes/1` → `note_id = 1`
- `GET /notes/42` → `note_id = 42`
- `GET /notes/999` → 404, wenn nicht vorhanden

**`fetchone()` vs `fetchall()`:**
- **`fetchone()`**: Gibt nur **ein** Ergebnis zurück (oder `None`)
- **`fetchall()`**: Gibt eine **Liste** aller Ergebnisse zurück

---

## Mini-Aufgabe

Jetzt bist du dran! Zeit, dein Wissen anzuwenden.

**Aufgabe:** Implementiere den Endpoint `DELETE /notes/{note_id}`

Dieser soll eine Notiz aus der Datenbank löschen.

**Anforderungen:**
1. HTTP-Methode: DELETE
2. Path Parameter: `note_id` (Integer)
3. Bei Erfolg: HTTP 200 mit Bestätigungsnachricht
4. Bei nicht existierender ID: HTTP 404

**Hinweise:**
- SQL: `DELETE FROM notes WHERE id = ?`
- Prüfe mit `cursor.rowcount`, ob eine Zeile gelöscht wurde
- `rowcount == 0` bedeutet: ID existierte nicht

**Bonus:**
- Gib in der Erfolgsnachricht auch die gelöschte ID zurück
- Teste den Endpoint in Swagger UI

<details>
<summary>💡 Lösung anzeigen</summary>

```python
@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    """
    Notiz löschen
    
    Löscht die Notiz mit der angegebenen ID.
    Falls die ID nicht existiert, wird ein 404-Fehler zurückgegeben.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(
        "DELETE FROM notes WHERE id = ?",
        (note_id,)
    )
    
    # Prüfen, ob eine Zeile gelöscht wurde
    deleted_count = cursor.rowcount
    
    conn.commit()
    conn.close()
    
    if deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    return {
        "message": "Notiz erfolgreich gelöscht",
        "deleted_id": note_id
    }
```

**Erklärung:**
- **`@app.delete(...)`**: DELETE ist die HTTP-Methode zum Löschen von Ressourcen
- **`cursor.rowcount`**: Gibt an, wie viele Zeilen von der letzten Operation betroffen waren
  - Bei `DELETE`: Anzahl der gelöschten Zeilen
  - `0` = nichts gelöscht (ID existierte nicht)
  - `1` = eine Zeile gelöscht (Erfolg!)
- **Wichtig:** `commit()` nicht vergessen, sonst wird nichts gelöscht!

**Testen in Swagger UI:**
1. Öffne http://localhost:8000/docs
2. Erstelle zuerst eine Notiz mit POST /notes
3. Notiere dir die zurückgegebene ID
4. Teste DELETE /notes/{id} mit dieser ID
5. Versuche dieselbe ID nochmal zu löschen → sollte 404 geben

</details>

---

## Übungen für Tag 2

Hier sind erweiterte Übungen, um dein Verständnis zu vertiefen!

### Übung 1: PUT /notes/{note_id} - Notiz aktualisieren

Implementiere einen Endpoint zum Aktualisieren einer bestehenden Notiz.

**Anforderungen:**
- HTTP-Methode: PUT
- Path Parameter: `note_id`
- Request Body: Pydantic Model mit neuem Text
- SQL: `UPDATE notes SET text = ? WHERE id = ?`
- Bei Erfolg: Aktualisierte Notiz zurückgeben
- Bei nicht existierender ID: HTTP 404

**Hinweise:**
- Erstelle ein neues Pydantic Model `NoteUpdate` (kann identisch zu `NoteCreate` sein)
- Nutze `cursor.rowcount` um zu prüfen, ob die Notiz existierte

<details>
<summary>💡 Lösung anzeigen</summary>

```python
class NoteUpdate(BaseModel):
    """
    Schema für das Aktualisieren einer Notiz.
    """
    text: str = Field(min_length=1, examples=["Aktualisierter Text"])
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "text": "Aktualisierter Text"
            }
        }
    }

@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteUpdate):
    """
    Notiz aktualisieren
    
    Aktualisiert den Text einer existierenden Notiz.
    Falls die ID nicht existiert, wird ein 404-Fehler zurückgegeben.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # UPDATE ausführen
    cursor.execute(
        "UPDATE notes SET text = ? WHERE id = ?",
        (note.text, note_id)
    )
    
    updated_count = cursor.rowcount
    conn.commit()
    
    # Prüfen, ob die Notiz existierte
    if updated_count == 0:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    # Aktualisierte Notiz abrufen
    cursor.execute(
        "SELECT * FROM notes WHERE id = ?",
        (note_id,)
    )
    row = cursor.fetchone()
    conn.close()
    
    return dict(row)
```

**Erklärung:**
- **PUT vs POST**: PUT aktualisiert existierende Ressourcen, POST erstellt neue
- **Zwei Parameter:** `note_id` (aus URL) und `note` (aus Request Body)
- **Zwei SQL-Statements:**
  1. `UPDATE` zum Ändern
  2. `SELECT` zum Abrufen der aktualisierten Daten
- **Alternative:** Man könnte auch nur eine Bestätigungsnachricht zurückgeben

**REST-Konvention:**
- POST: Neue Ressource erstellen
- GET: Ressource abrufen
- PUT: Ressource vollständig ersetzen
- PATCH: Ressource teilweise aktualisieren
- DELETE: Ressource löschen

</details>

---

### Übung 2: GET /notes/search?q=... - Volltextsuche

Erstelle einen Endpoint, der Notizen nach einem Suchbegriff durchsucht.

**Anforderungen:**
- Query Parameter `q` für den Suchtext
- SQL: `WHERE text LIKE ?` mit Wildcards
- Gibt alle passenden Notizen zurück

**Hinweise:**
- Query Parameter: `def search_notes(q: str):`
- SQL-LIKE mit Wildcards: `f"%{q}%"` findet Text überall
- Beispiel: `/notes/search?q=Einkauf` findet "Einkaufen gehen"

<details>
<summary>💡 Lösung anzeigen</summary>

```python
@app.get("/notes/search")
def search_notes(q: str):
    """
    Notizen durchsuchen
    
    Sucht nach Notizen, die den Suchbegriff im Text enthalten.
    Groß-/Kleinschreibung wird ignoriert.
    
    Query Parameter:
    - q: Suchbegriff
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # LIKE mit Wildcards für Teilstring-Suche
    search_pattern = f"%{q}%"
    
    cursor.execute(
        "SELECT * FROM notes WHERE text LIKE ? ORDER BY id DESC",
        (search_pattern,)
    )
    rows = cursor.fetchall()
    conn.close()
    
    return {
        "query": q,
        "count": len(rows),
        "results": [dict(row) for row in rows]
    }
```

**Erklärung:**
- **Query Parameter**: FastAPI extrahiert `q` aus `?q=...` in der URL
- **SQL LIKE**: Muster-Matching für Strings
  - `%`: Wildcard für beliebige Zeichen
  - `%test%`: Findet "test" überall im String
  - `test%`: Findet Strings, die mit "test" beginnen
  - `%test`: Findet Strings, die mit "test" enden
- **`f"%{q}%"`**: Packt den Suchbegriff zwischen Wildcards
  - **Wichtig:** Der f-String ist hier OK, weil wir das Ergebnis dann als Parameter übergeben!
  - Niemals: `cursor.execute(f"... LIKE '%{q}%'")` ❌
  - Immer: `cursor.execute("... LIKE ?", (f"%{q}%",))` ✅

**Beispiel-Requests:**
- `/notes/search?q=Einkauf`
- `/notes/search?q=wichtig`
- `/notes/search?q=TODO`

**Bonus: Case-Insensitive Search (Groß-/Kleinschreibung ignorieren):**
SQLite's `LIKE` ist standardmäßig case-insensitive für ASCII-Zeichen. Für vollständige Unterstützung:
```python
cursor.execute(
    "SELECT * FROM notes WHERE LOWER(text) LIKE LOWER(?) ORDER BY id DESC",
    (search_pattern,)
)
```

</details>

---

### Übung 3: Datenbank in separates Modul auslagern

**Fortgeschritten:** Refactoring für bessere Code-Organisation.

Erstelle eine neue Datei `database.py` und lagere alle Datenbank-Funktionen aus.

**Anforderungen:**
- Neue Datei: `database.py`
- Funktionen auslagern: `init_db()`, `get_all_notes()`, `create_note()`, etc.
- In `main.py` nur noch die Endpoints (die Funktionen aus `database.py` aufrufen)

**Vorteile:**
- **Separation of Concerns**: Datenbank-Logik getrennt von API-Logik
- **Testbarkeit**: Datenbank-Funktionen können separat getestet werden
- **Wiederverwendbarkeit**: Funktionen können in anderen Projekten genutzt werden

<details>
<summary>💡 Lösung anzeigen</summary>

**database.py:**
```python
"""
Datenbank-Funktionen für die Notes API
"""
import sqlite3
from typing import Optional

DATABASE = "notes.db"

def init_db():
    """Initialisiert die Datenbank und erstellt die Tabelle."""
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
    print("Datenbank initialisiert!")

def get_all_notes() -> list:
    """Gibt alle Notizen zurück."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_note_by_id(note_id: int) -> Optional[dict]:
    """
    Gibt eine einzelne Notiz zurück.
    
    Returns:
        dict wenn gefunden, None wenn nicht gefunden
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def create_note(text: str) -> dict:
    """Erstellt eine neue Notiz und gibt sie zurück."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (text) VALUES (?)", (text,))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"id": new_id, "text": text}

def update_note(note_id: int, text: str) -> bool:
    """
    Aktualisiert eine Notiz.
    
    Returns:
        True wenn erfolgreich, False wenn ID nicht gefunden
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET text = ? WHERE id = ?", (text, note_id))
    updated_count = cursor.rowcount
    conn.commit()
    conn.close()
    return updated_count > 0

def delete_note(note_id: int) -> bool:
    """
    Löscht eine Notiz.
    
    Returns:
        True wenn erfolgreich, False wenn ID nicht gefunden
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    deleted_count = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted_count > 0
```

**main.py (vereinfacht):**
```python
"""
Mini Notes API - Tag 2: Refactored Version
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import database as db

app = FastAPI(
    title="Mini Notes API",
    description="Eine API zum Speichern von Notizen mit SQLite-Datenbank",
    version="2.0.0"
)

# Datenbank beim Start initialisieren
db.init_db()

class NoteCreate(BaseModel):
    text: str

class NoteUpdate(BaseModel):
    text: str

@app.get("/")
def root():
    """API-Übersicht"""
    return {
        "name": "Mini Notes API",
        "version": "2.0.0",
        "database": "SQLite (persistent)",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    """Health-Check mit DB-Status"""
    try:
        notes = db.get_all_notes()
        return {
            "status": "ok",
            "timestamp": datetime.now().isoformat(),
            "notes_count": len(notes)
        }
    except Exception as e:
        return {
            "status": "error",
            "timestamp": datetime.now().isoformat(),
            "error": str(e)
        }

@app.get("/notes")
def get_all_notes():
    """Alle Notizen abrufen"""
    return db.get_all_notes()

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """Eine einzelne Notiz abrufen"""
    note = db.get_note_by_id(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail=f"Notiz mit ID {note_id} nicht gefunden")
    return note

@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    """Neue Notiz erstellen"""
    return db.create_note(note.text)

@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteUpdate):
    """Notiz aktualisieren"""
    success = db.update_note(note_id, note.text)
    if not success:
        raise HTTPException(status_code=404, detail=f"Notiz mit ID {note_id} nicht gefunden")
    
    updated_note = db.get_note_by_id(note_id)
    return updated_note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    """Notiz löschen"""
    success = db.delete_note(note_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Notiz mit ID {note_id} nicht gefunden")
    
    return {
        "message": "Notiz erfolgreich gelöscht",
        "deleted_id": note_id
    }
```

**Vorteile dieser Struktur:**
1. **`main.py` ist jetzt viel kürzer** und enthält nur API-Logik
2. **`database.py` ist wiederverwendbar** und kann in anderen Projekten genutzt werden
3. **Bessere Testbarkeit**: Du kannst `database.py` unabhängig testen
4. **Klare Verantwortlichkeiten**: Jede Datei hat einen klaren Zweck

**Projekt-Struktur jetzt:**
```
mini-api/
├── venv/
├── main.py           # API-Endpoints
├── database.py       # Datenbank-Logik
├── notes.db          # SQLite-Datenbank
└── requirements.txt
```

</details>

---

## Zusammenfassung Tag 2

**Was haben wir gelernt?**

 **SQLite-Grundlagen:**
- Datenbank initialisieren mit `sqlite3.connect()`
- Tabellen erstellen mit `CREATE TABLE`
- Connection und Cursor verstehen

 **CRUD-Operationen:**
- **C**reate: `INSERT` mit POST-Endpoint
- **R**ead: `SELECT` mit GET-Endpoints
- **U**pdate: `UPDATE` mit PUT-Endpoint
- **D**elete: `DELETE` mit DELETE-Endpoint

 **SQL-Sicherheit:**
- Parametrisierte Queries mit `?`-Platzhaltern
- SQL-Injection vermeiden
- **Niemals** f-Strings direkt in SQL-Befehlen!

 **FastAPI-Features:**
- Path Parameters (`{note_id}`)
- Pydantic Models für Validierung
- HTTP-Statuscodes korrekt nutzen
- HTTPException für Fehlerbehandlung

 **Persistenz:**
- Daten bleiben nach Neustart erhalten!
- `notes.db`-Datei enthält alle Daten
- `commit()` speichert Änderungen dauerhaft

---

## Ausblick auf Tag 3

Morgen werden wir:
- **Error Handling** richtig implementieren (try-except, bessere Fehlerbehandlung)
- **SQLAlchemy** einführen (ORM = Object-Relational Mapping)
- **Async/Await** nutzen für bessere Performance
- **Beziehungen zwischen Tabellen** verstehen (1:n, m:n)
- **Context Manager** für automatisches Connection-Handling
- **Dependency Injection** in FastAPI kennenlernen

**Unser Code wird noch professioneller und wartbarer!**

---

## main.py - Finale Version Tag 2

Hier ist die finale, vollständige Version von `main.py` nach allen Übungen:

```python
"""
Mini Notes API - Tag 2: SQLite Version
=======================================
Jetzt mit persistenter Datenspeicherung!
Alle Daten bleiben nach Neustart erhalten.

CRUD-Operationen:
- CREATE: POST /notes
- READ:   GET /notes, GET /notes/{id}, GET /notes/search
- UPDATE: PUT /notes/{id}
- DELETE: DELETE /notes/{id}
"""
import sqlite3
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# FastAPI-App erstellen
app = FastAPI(
    title="Mini Notes API",
    description="Eine API zum Speichern von Notizen mit SQLite-Datenbank",
    version="2.0.0"
)

# Datenbank-Dateiname
DATABASE = "notes.db"

# ========================================
# Pydantic Models
# ========================================

class NoteCreate(BaseModel):
    """Schema für das Erstellen einer neuen Notiz."""
    text: str = Field(min_length=1, examples=["Einkaufen gehen: Milch, Brot, Eier"])
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "text": "Einkaufen gehen: Milch, Brot, Eier"
            }
        }
    }

class NoteUpdate(BaseModel):
    """Schema für das Aktualisieren einer Notiz."""
    text: str = Field(min_length=1, examples=["Aktualisierter Text"])
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "text": "Aktualisierter Text"
            }
        }
    }

# ========================================
# Datenbank-Setup
# ========================================

def init_db():
    """
    Initialisiert die Datenbank und erstellt die Tabelle.
    
    Wird beim Start/Import der API ausgeführt.
    Mit uvicorn --reload kann dies mehrfach passieren (bei Code-Änderungen),
    ist aber dank IF NOT EXISTS unkritisch.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Tabelle erstellen (IF NOT EXISTS = sicher, kann mehrfach aufgerufen werden)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()
    print("Datenbank initialisiert!")

# Datenbank beim Start der API initialisieren
init_db()

# ========================================
# API Endpoints
# ========================================

@app.get("/")
def root():
    """
    API-Übersicht
    
    Gibt grundlegende Informationen über die API zurück.
    """
    return {
        "name": "Mini Notes API",
        "description": "Eine API zum Speichern von Notizen mit SQLite-Datenbank",
        "version": "2.0.0",
        "database": "SQLite (persistent)",
        "endpoints": {
            "GET /": "API-Übersicht",
            "GET /health": "Health-Check",
            "GET /notes": "Alle Notizen abrufen",
            "GET /notes/{id}": "Einzelne Notiz abrufen",
            "GET /notes/search?q=...": "Notizen durchsuchen",
            "POST /notes": "Neue Notiz erstellen",
            "PUT /notes/{id}": "Notiz aktualisieren",
            "DELETE /notes/{id}": "Notiz löschen"
        },
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    """
    Health-Check Endpoint mit DB-Status
    
    Prüft, ob die API UND die Datenbank erreichbar sind.
    """
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM notes")
        count = cursor.fetchone()[0]
        conn.close()
        db_status = "ok"
    except Exception as e:
        db_status = f"error: {str(e)}"
        count = None
    
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "database": db_status,
        "notes_count": count
    }

@app.get("/notes")
def get_all_notes():
    """
    Alle Notizen abrufen
    
    Liest alle Notizen aus der SQLite-Datenbank und gibt sie zurück.
    Sortiert nach ID (neueste zuerst).
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

@app.get("/notes/search")
def search_notes(q: str):
    """
    Notizen durchsuchen
    
    Sucht nach Notizen, die den Suchbegriff im Text enthalten.
    
    Query Parameter:
    - q: Suchbegriff (z.B. ?q=Einkauf)
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    search_pattern = f"%{q}%"
    
    cursor.execute(
        "SELECT * FROM notes WHERE text LIKE ? ORDER BY id DESC",
        (search_pattern,)
    )
    rows = cursor.fetchall()
    conn.close()
    
    return {
        "query": q,
        "count": len(rows),
        "results": [dict(row) for row in rows]
    }

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    """
    Eine einzelne Notiz abrufen
    
    Gibt die Notiz mit der angegebenen ID zurück.
    Falls die ID nicht existiert, wird ein 404-Fehler zurückgegeben.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT * FROM notes WHERE id = ?",
        (note_id,)
    )
    row = cursor.fetchone()
    conn.close()
    
    if row is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    return dict(row)

@app.post("/notes", status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate):
    """
    Neue Notiz erstellen
    
    Erstellt eine neue Notiz in der Datenbank und gibt sie zurück.
    Der HTTP-Statuscode 201 signalisiert erfolgreiche Erstellung.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO notes (text) VALUES (?)",
        (note.text,)
    )
    
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return {
        "id": new_id,
        "text": note.text,
        "message": "Notiz erfolgreich erstellt"
    }

@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteUpdate):
    """
    Notiz aktualisieren
    
    Aktualisiert den Text einer existierenden Notiz.
    Falls die ID nicht existiert, wird ein 404-Fehler zurückgegeben.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute(
        "UPDATE notes SET text = ? WHERE id = ?",
        (note.text, note_id)
    )
    
    updated_count = cursor.rowcount
    conn.commit()
    
    if updated_count == 0:
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    cursor.execute(
        "SELECT * FROM notes WHERE id = ?",
        (note_id,)
    )
    row = cursor.fetchone()
    conn.close()
    
    return dict(row)

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    """
    Notiz löschen
    
    Löscht die Notiz mit der angegebenen ID.
    Falls die ID nicht existiert, wird ein 404-Fehler zurückgegeben.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute(
        "DELETE FROM notes WHERE id = ?",
        (note_id,)
    )
    
    deleted_count = cursor.rowcount
    conn.commit()
    conn.close()
    
    if deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    return {
        "message": "Notiz erfolgreich gelöscht",
        "deleted_id": note_id
    }
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


**Bei Fragen meldet euch bei Patrick oder mir. Viel Erfolg und bis morgen!**
