# Tag 3: Saubere Struktur + Validierung + Error Handling

## Lernziele
* Code in Module aufteilen (Separation of Concerns)
* Error Handling mit try-except richtig umsetzen
* Context Manager (`with`-Statement) für sauberes Ressourcen-Management
* Eingabe-Validierung mit Pydantic Field verstehen und anwenden
* Query-Parameter implementieren und validieren
* Wiederholungen vermeiden und Code wartbarer machen

---

## Theorie: Type Hints - Was ist das und warum?

### Python ohne Type Hints

Python ist eine **dynamisch typisierte** Sprache. Das bedeutet:

```python
# Python erlaubt dies alles ohne Probleme:
x = 5              # x ist ein Integer
x = "Hallo"        # Jetzt ist x ein String
x = [1, 2, 3]      # Jetzt ist x eine Liste
x = {"key": "value"}  # Jetzt ist x ein Dictionary
```

**Das ist gleichzeitig gut und schlecht:**

**Gut:**
- Schnell zu schreiben
- Flexibel
- Weniger Code

**Schlecht:**
- Fehler erst zur Laufzeit
- Schwer zu verstehen was erwartet wird
- IDE kann weniger helfen

**Beispiel-Problem:**
```python
def get_user_name(user):
    return user["name"]

# Was ist user? Ein Dictionary? Ein Objekt?
# Was gibt die Funktion zurück? Einen String?
# Wir wissen es nicht!
```

### Type Hints - Die Lösung

**Type Hints** sind Typ-Annotationen, die dem Code sagen, welche Typen erwartet werden:

```python
def get_user_name(user: dict) -> str:
    return user["name"]

# Jetzt ist klar:
# - user ist ein Dictionary
# - Die Funktion gibt einen String zurück
```

**Wichtig:** Type Hints ändern NICHTS am Verhalten von Python!
- Python ignoriert sie zur Laufzeit
- Der Code läuft genauso wie vorher
- Sie sind nur für Entwickler und Tools

### Grundlegende Type Hints

**Einfache Typen:**
```python
name: str = "Max"           # String
age: int = 25               # Integer (Ganzzahl)
height: float = 1.75        # Float (Dezimalzahl)
is_active: bool = True      # Boolean (True/False)
```

**In Funktionen:**
```python
def greet(name: str) -> str:
    #         ^^^^^      ^^^
    #         Parameter  Rückgabe-Typ
    return f"Hallo, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def is_adult(age: int) -> bool:
    return age >= 18
```

**Ohne Rückgabewert:**
```python
def print_hello() -> None:
    #                ^^^^
    #                Gibt nichts zurück
    print("Hallo!")
```

### Der `typing` Modul - Für komplexere Typen

Für Listen, Dictionaries, optionale Werte usw. brauchen wir das `typing` Modul:

```python
from typing import List, Dict, Optional
```

Lass uns jeden einzeln durchgehen:

---

### 1. Optional[Type] - "Kann auch None sein"

**Das Problem:**
```python
def get_note(note_id: int) -> dict:
    # Was wenn die Notiz nicht gefunden wird?
    # Wir geben None zurück, aber dict sagt "immer ein Dictionary"!
    if note_exists(note_id):
        return {"id": note_id, "text": "..."}
    else:
        return None  # Widerspruch!
```

**Die Lösung: Optional[Type]**
```python
from typing import Optional

def get_note(note_id: int) -> Optional[dict]:
    #                          ^^^^^^^^
    #                          "Entweder dict ODER None"
    if note_exists(note_id):
        return {"id": note_id, "text": "..."}
    else:
        return None  # Jetzt ist es klar!
```

**Optional[X] bedeutet: "Entweder X oder None"**

```python
# Weitere Beispiele:
name: Optional[str] = None          # Kann String oder None sein
age: Optional[int] = get_age()      # Kann int oder None sein

def find_user(id: int) -> Optional[dict]:
    # Gibt entweder ein Dictionary zurück oder None
    pass
```

**Warum ist das wichtig?**
```python
# OHNE Optional - IDE warnt nicht:
def get_note(note_id: int) -> dict:
    return None  # Keine Warnung!

note = get_note(42)
print(note["text"])  # CRASH wenn None!

# MIT Optional - IDE warnt:
def get_note(note_id: int) -> Optional[dict]:
    return None  # OK!

note = get_note(42)
print(note["text"])  # IDE warnt: "note könnte None sein!"

# Richtig:
note = get_note(42)
if note is not None:
    print(note["text"])  # Sicher!
```

---

### 2. List[Type] - "Liste mit bestimmtem Inhalt"

**Das Problem:**
```python
def get_all_notes() -> list:
    # Eine Liste - aber was ist DRIN?
    # Strings? Dictionaries? Zahlen?
    return [...]
```

**Die Lösung: List[Type]**
```python
from typing import List

def get_all_notes() -> List[dict]:
    #                      ^^^^^^^^^
    #                      "Liste von Dictionaries"
    return [
        {"id": 1, "text": "Erste Notiz"},
        {"id": 2, "text": "Zweite Notiz"}
    ]
```

**List[X] bedeutet: "Eine Liste, in der nur X-Objekte sind"**

```python
# Weitere Beispiele:
numbers: List[int] = [1, 2, 3, 4]           # Liste von Integers
names: List[str] = ["Anna", "Bob", "Carl"]  # Liste von Strings
users: List[dict] = [{"name": "Max"}, ...]  # Liste von Dicts

def get_ids() -> List[int]:
    return [1, 2, 3]

def get_names() -> List[str]:
    return ["Anna", "Bob"]
```

**Verschachtelte Listen:**
```python
# Liste von Listen:
matrix: List[List[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Liste von Optional-Werten:
maybe_numbers: List[Optional[int]] = [1, 2, None, 4]
```

---

### 3. Dict[KeyType, ValueType] - "Dictionary mit bestimmten Typen"

**Das Problem:**
```python
def get_note() -> dict:
    # Ein Dictionary - aber mit welchen Keys? Welchen Values?
    return {"id": 1, "text": "Hallo"}
```

**Die Lösung: Dict[KeyType, ValueType]**
```python
from typing import Dict

def get_note() -> Dict[str, str]:
    #                  ^^^^^^^^^^^^
    #                  Keys: Strings, Values: Strings
    return {"text": "Hallo", "author": "Max"}

def get_note_with_id() -> Dict[str, int | str]:
    #                            Keys: Strings, Values: int ODER str
    return {"id": 1, "text": "Hallo"}
```

**Dict[K, V] bedeutet: "Dictionary mit Keys vom Typ K und Values vom Typ V"**

```python
# Weitere Beispiele:
ages: Dict[str, int] = {"Max": 25, "Anna": 30}
# Keys sind Strings, Values sind ints

scores: Dict[str, float] = {"Max": 9.5, "Anna": 8.7}
# Keys sind Strings, Values sind floats

config: Dict[str, bool] = {"debug": True, "verbose": False}
# Keys sind Strings, Values sind bools

# Mit Optional:
users: Dict[int, Optional[str]] = {1: "Max", 2: None, 3: "Anna"}
# Keys sind ints, Values sind entweder Strings oder None
```

---

### 4. Kombinationen - List[Dict], Optional[List[Dict]]

Jetzt wird es interessant - wir können Type Hints kombinieren:

**List[Dict[str, str]] - "Liste von Dictionaries"**
```python
from typing import List, Dict

def get_all_notes() -> List[Dict[str, str]]:
    #                      ^^^^^^^^^^^^^^^^^
    #                      Liste von Dictionaries
    #                      (Keys: str, Values: str)
    return [
        {"id": "1", "text": "Erste Notiz"},
        {"id": "2", "text": "Zweite Notiz"}
    ]
```

**Schritt-für-Schritt-Erklärung:**
```python
# 1. Wir haben ein Dictionary:
note: Dict[str, str] = {"id": "1", "text": "Hallo"}

# 2. Wir haben mehrere davon in einer Liste:
notes: List[Dict[str, str]] = [
    {"id": "1", "text": "Erste"},
    {"id": "2", "text": "Zweite"}
]

# 3. Als Rückgabewert:
def get_notes() -> List[Dict[str, str]]:
    return notes
```

**Optional[List[Dict]] - "Kann None sein, oder eine Liste von Dicts"**
```python
from typing import Optional, List, Dict

def search_notes(query: str) -> Optional[List[Dict[str, str]]]:
    #                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #                              Entweder:
    #                              - None (nichts gefunden)
    #                              - Liste von Dictionaries
    if not query:
        return None  # Keine Suche
    
    results = [{"id": "1", "text": "Match"}]
    return results
```

**Schritt-für-Schritt:**
```python
# Von innen nach außen lesen:

Dict[str, str]
# Ein Dictionary mit String-Keys und String-Values

List[Dict[str, str]]
# Eine Liste davon

Optional[List[Dict[str, str]]]
# Das Ganze kann auch None sein
```

---

### Praktische Beispiele aus unserer API

**Beispiel 1: get_note_by_id**
```python
from typing import Optional, Dict

def get_note_by_id(note_id: int) -> Optional[Dict]:
    #                  ^^^^ Parameter-Typ
    #                                   ^^^^^^^^^^^^^^ Rückgabe-Typ
    """
    Holt eine Notiz.
    
    Args:
        note_id: int - Die ID (muss eine Ganzzahl sein)
    
    Returns:
        Optional[Dict] - Entweder ein Dictionary (Notiz gefunden)
                        oder None (nicht gefunden)
    """
    # ... DB-Query
    if row:
        return {"id": 1, "text": "..."}  # Dict
    else:
        return None  # None
```

**Was passiert hier?**
1. `note_id: int` → Parameter muss ein Integer sein
2. `-> Optional[Dict]` → Gibt entweder Dictionary oder None zurück
3. IDE weiß: "Diese Funktion kann None zurückgeben!"
4. IDE warnt bei `note["text"]` ohne None-Check

**Beispiel 2: get_all_notes**
```python
from typing import List, Dict

def get_all_notes() -> List[Dict]:
    #                      ^^^^^^^^^
    #                      Liste von Dictionaries
    """
    Holt alle Notizen.
    
    Returns:
        List[Dict] - Eine Liste, in der jedes Element ein Dictionary ist
    """
    rows = [
        {"id": 1, "text": "Erste"},
        {"id": 2, "text": "Zweite"}
    ]
    return rows
```

**Was passiert hier?**
1. `-> List[Dict]` → Gibt eine Liste zurück
2. Jedes Element in der Liste ist ein Dictionary
3. Nie None (immer eine Liste, auch wenn leer: `[]`)

**Beispiel 3: create_note**
```python
from typing import Optional

def create_note(text: str) -> Optional[int]:
    #               ^^^^ Parameter
    #                                  ^^^^^^^^^ Rückgabe
    """
    Erstellt eine Notiz.
    
    Args:
        text: str - Der Notiz-Text (muss String sein)
    
    Returns:
        Optional[int] - ID der neuen Notiz (int)
                       oder None bei Fehler
    """
    try:
        # ... DB Insert
        return 42  # Die neue ID
    except:
        return None  # Fehler
```

**Was passiert hier?**
1. `text: str` → Parameter muss String sein
2. `-> Optional[int]` → Gibt int (ID) oder None zurück
3. IDE weiß: "Könnte None sein, prüfen!"

---

### Warum sind Type Hints wichtig?

**1. Selbstdokumentierender Code**
```python
# OHNE Type Hints - unklar:
def process_user(data):
    return data["name"]

# MIT Type Hints - sofort klar:
def process_user(data: Dict[str, str]) -> str:
    return data["name"]
```

**2. IDE-Unterstützung (Autocomplete)**
```python
from typing import Dict

def get_note() -> Dict[str, str]:
    return {"id": "1", "text": "Hallo"}

note = get_note()
note.  # IDE zeigt automatisch: .get(), .keys(), .values() etc.
```

**3. Frühe Fehlererkennung**
```python
from typing import Optional

def get_note(id: int) -> Optional[dict]:
    return None

# IDE warnt SOFORT:
note = get_note(42)
print(note["text"])  # Warnung: "note könnte None sein!"

# Richtig:
note = get_note(42)
if note:
    print(note["text"])  # OK!
```

**4. Bessere Zusammenarbeit im Team**
```python
# Kollege schreibt:
def get_users() -> List[Dict[str, str]]:
    pass

# Du verstehst sofort ohne Doku:
# - Gibt Liste zurück
# - Liste enthält Dictionaries
# - Dict-Keys und Values sind Strings
```

---

### Häufige Fehler mit Type Hints

**Fehler 1: Type Hint vergessen zu importieren**
```python
# FALSCH:
def get_notes() -> List[dict]:  # NameError: List ist nicht definiert

# RICHTIG:
from typing import List

def get_notes() -> List[dict]:
    pass
```

**Fehler 2: Optional vergessen**
```python
# FALSCH - aber läuft trotzdem:
def get_note(id: int) -> dict:
    return None  # Lüge! Es ist kein dict!

# RICHTIG:
from typing import Optional

def get_note(id: int) -> Optional[dict]:
    return None  # Ehrlich!
```

**Fehler 3: Type Hints verwechseln**
```python
# FALSCH:
notes: dict = [{"id": 1}]  # Liste, kein dict!

# RICHTIG:
from typing import List, Dict

notes: List[Dict] = [{"id": 1}]
```

**Fehler 4: Verschachtelung falsch**
```python
# FALSCH:
def get_notes() -> List[dict[str, str]]:  # Kleinbuchstabe dict in []

# RICHTIG:
from typing import List, Dict

def get_notes() -> List[Dict[str, str]]:  # Großbuchstabe Dict aus typing
```

---

### Type Hints in unserer API - Komplett-Beispiel

```python
from typing import Optional, List, Dict
import sqlite3

def get_all_notes(
    limit: int = 100,              # Parameter: int mit Default
    search: Optional[str] = None   # Parameter: Optional string
) -> List[Dict]:                   # Rückgabe: Liste von Dicts
    """
    Holt alle Notizen.
    
    Args:
        limit: Maximale Anzahl (int)
        search: Suchbegriff (str oder None)
    
    Returns:
        Liste von Dictionaries (immer eine Liste, auch wenn leer)
    """
    try:
        # ... DB-Query
        rows = [{"id": 1, "text": "Test"}]
        return rows  # List[Dict]
    except:
        return []  # Leere Liste, nicht None!


def get_note_by_id(note_id: int) -> Optional[Dict]:
    """
    Holt eine Notiz.
    
    Args:
        note_id: Die ID (int)
    
    Returns:
        Dictionary wenn gefunden, None sonst
    """
    # ... DB-Query
    if found:
        return {"id": note_id}  # Dict
    else:
        return None  # None


def create_note(text: str) -> Optional[int]:
    """
    Erstellt eine Notiz.
    
    Args:
        text: Der Notiz-Text (str)
    
    Returns:
        ID der neuen Notiz (int) oder None bei Fehler
    """
    try:
        # ... DB Insert
        return 42  # int
    except:
        return None  # None
```

**Zusammengefasst:**
- `from typing import Optional, List, Dict` → Importiere spezielle Type Hints
- `Optional[X]` → "X oder None"
- `List[X]` → "Liste von X"
- `Dict[K, V]` → "Dictionary mit Keys K und Values V"
- `-> Typ` nach Funktion → Rückgabe-Typ
- `: Typ` nach Parameter → Parameter-Typ

**Merksatz:** Type Hints sind wie Schilder an einer Straße - sie sagen dir, wo es langgeht, aber sie zwingen dich nicht, sie zu befolgen. Sie helfen dir und anderen, den Code zu verstehen!

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

## Live-Coding Teil 1: Basis-Refactoring

In diesem ersten Schritt konzentrieren wir uns auf:
1. Code in Module aufteilen
2. Error Handling implementieren
3. Context Manager nutzen

**Noch OHNE:**
- Query-Parameter
- Pydantic Field Validierung

Das machen wir dann in Teil 2!

### 1. db.py erstellen (Basis-Version)

Erstelle eine neue Datei `db.py` im Projektordner. Diese wird unsere gesamte Datenbank-Logik enthalten.

```python
"""
Datenbank-Modul für Mini Notes API - Tag 3
Enthält alle DB-Operationen mit Error Handling und Context Manager
"""
import sqlite3
from typing import Optional, List, Dict
#               ^^^^^^^^^^^^^^^^^^^^
#               Type Hints für komplexe Typen:
#               - Optional: "Kann auch None sein"
#               - List: "Eine Liste"
#               - Dict: "Ein Dictionary"

# Konstante für den Datenbank-Dateinamen
DATABASE = "notes.db"
```

**Imports erklärt:**
- `import sqlite3` → SQLite-Datenbank Modul (in Python eingebaut)
- `from typing import ...` → Type Hints für bessere Code-Dokumentation
  - `Optional` → Für Werte die None sein können
  - `List` → Für Listen mit bestimmtem Inhalt
  - `Dict` → Für Dictionaries mit bestimmten Typen

---

```python
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


def get_all_notes() -> List[Dict]:
    """
    Holt alle Notizen aus der Datenbank.
    
    Returns:
        Liste von Notizen als Dictionaries
    """
    try:
        with get_connection() as conn:
            rows = conn.execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
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

1. **Type Hints überall (jetzt verstehen wir sie!):**
   ```python
   def get_all_notes() -> List[Dict]:
   #                      ^^^^^^^^^
   #                      Rückgabe-Typ: Liste von Dictionaries
   
   def get_note_by_id(note_id: int) -> Optional[Dict]:
   #                  ^^^^^^^^^^^^     ^^^^^^^^^^^^^^^^
   #                  Parameter: int   Rückgabe: Dict oder None
   
   def create_note(text: str) -> Optional[int]:
   #               ^^^^^^^^^     ^^^^^^^^^^^^^^^
   #               Parameter     Rückgabe: int (ID) oder None
   
   def update_note(note_id: int, text: str) -> bool:
   #               ^^^^^^^^^^^^  ^^^^^^^^^^     ^^^^
   #               Parameter 1   Parameter 2    Rückgabe: True/False
   ```
   
   **Warum?** 
   - Macht den Code selbstdokumentierend
   - IDE zeigt Warnungen bei falscher Nutzung
   - Andere verstehen sofort, was erwartet wird
   
   **Erinnerung:**
   - `-> List[Dict]` = Gibt immer eine Liste zurück (auch wenn leer: `[]`)
   - `-> Optional[Dict]` = Gibt entweder Dictionary oder None zurück
   - `-> Optional[int]` = Gibt entweder eine Zahl oder None zurück
   - `-> bool` = Gibt True oder False zurück

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

### 2. main.py aufräumen (Basis-Version)

Jetzt passen wir `main.py` an, um `db.py` zu nutzen. Wir verwenden noch das **einfache Pydantic Model aus Tag 2** (ohne Field-Validierung):

```python
"""
Mini Notes API - Tag 3.1: Strukturierte Version (Basis)
Saubere Code-Aufteilung + Error Handling + Context Manager
"""
from fastapi import FastAPI, HTTPException
#                   ^^^^^^^  ^^^^^^^^^^^^^
#                   FastAPI  Für HTTP-Fehler (404, 500, etc.)

from pydantic import BaseModel
#                    ^^^^^^^^^
#                    Für Datenvalidierung

import db  # Unser DB-Modul importieren
#      ^^
#      Jetzt können wir db.get_all_notes() etc. aufrufen
```

**Imports erklärt:**
- `from fastapi import FastAPI, HTTPException`
  - `FastAPI` → Die Haupt-Klasse für unsere API
  - `HTTPException` → Zum Werfen von HTTP-Fehlern (404, 500 etc.)
- `from pydantic import BaseModel` → Basis für Daten-Validierung
- `import db` → Unser eigenes Datenbank-Modul
  - Wir können jetzt `db.get_all_notes()`, `db.create_note()` etc. nutzen
  - Alles aus der `db.py` Datei ist jetzt verfügbar

---

```python
app = FastAPI(
    title="Mini Notes API",
    description="Eine strukturierte API mit Error Handling",
    version="3.0.0"
)

# Datenbank beim Start initialisieren
db.init_db()


# ========================================
# Pydantic Models (Basis-Version)
# ========================================

class NoteCreate(BaseModel):
    """
    Schema für das Erstellen/Aktualisieren einer Notiz.
    
    Einfache Version: Nur Typ-Prüfung, keine weiteren Constraints.
    """
    text: str


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
            "Error handling",
            "Context Manager"
        ],
        "endpoints": {
            "get_all": "GET /notes",
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
def get_notes():
    """Alle Notizen abrufen."""
    notes = db.get_all_notes()
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
    
    Body: JSON mit 'text' Feld
    
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

**Was ist hier neu gegenüber Tag 2?**

1. **`import db`:**
   - Importiert unser neues Datenbank-Modul
   - Wir können jetzt `db.get_all_notes()` usw. aufrufen
   - Alle DB-Details sind versteckt in `db.py`

2. **Einfaches Pydantic Model:**
   - Noch keine Field-Constraints
   - Nur Typ-Prüfung: `text` muss ein String sein
   - **Das erweitern wir gleich in Teil 2!**

3. **Besseres Error Handling:**
   - `if note is None:` → prüft, ob DB-Funktion etwas zurückgegeben hat
   - `raise HTTPException`: Gibt einen korrekten HTTP-Fehler zurück
   - Status Codes: 404 (Not Found), 500 (Server Error), 201 (Created)
   - **Achtung:** Mit unserer aktuellen DB-Implementierung können DB-Fehler als 404 erscheinen

4. **Sicherheits-Check in update_note:**
   - Prüft, ob `updated_note` None ist (könnte bei DB-Fehler passieren)
   - Gibt dann 500 statt falschem 200 zurück

**Jetzt testen:**
```bash
uvicorn main:app --reload
```

Öffne http://localhost:8000/docs und teste alle Endpoints!

**Was funktioniert jetzt besser?**
- Code ist sauberer strukturiert
- DB-Connections werden garantiert geschlossen
- Fehler werden abgefangen (wenn auch nicht perfekt unterschieden)

**Was fehlt noch?**
- Validierung (leerer Text erlaubt, zu lange Texte erlaubt)
- Query-Parameter (z.B. Limit, Suche)

**Das machen wir jetzt!**

---

## Theorie: Eingabe-Validierung mit Pydantic Field

### Warum brauchen wir Validierung?

**Problem ohne Validierung:**
```python
class NoteCreate(BaseModel):
    text: str
```

**Was wird akzeptiert?**
- Leere Strings: `""` → Notiz ohne Inhalt!
- Extrem lange Texte: `"A" * 1000000` → 1 Million Zeichen!
- Nur Leerzeichen: `"     "` → Nutzlose Notiz!

**Folgen:**
- Schlechte User Experience
- Datenbank-Probleme (zu große Einträge)
- Potenzielle Security-Probleme

### Pydantic Field - Die Lösung

Pydantic bietet `Field()` für präzise Validierung:

```python
from pydantic import BaseModel, Field

class NoteCreate(BaseModel):
    text: str = Field(
        min_length=1,      # Mindestens 1 Zeichen
        max_length=500,    # Maximal 500 Zeichen
        description="Der Notiz-Text (1-500 Zeichen)"
    )
```

**Was passiert jetzt automatisch?**

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
  "text": "A... (501 Zeichen)"
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

**Beispiel 3: Gültiger Text**
```json
POST /notes
{
  "text": "Einkaufen: Milch, Brot, Eier"
}
```

**Antwort: 201 Created**
```json
{
  "id": 1,
  "text": "Einkaufen: Milch, Brot, Eier"
}
```

### Alle Field-Parameter im Überblick

```python
from pydantic import BaseModel, Field

class Example(BaseModel):
    # String-Validierung
    name: str = Field(
        min_length=3,           # Mindestens 3 Zeichen
        max_length=50,          # Maximal 50 Zeichen
        pattern="^[a-zA-Z ]+$", # Regex: nur Buchstaben und Leerzeichen
        description="Der Name"
    )
    
    # Zahlen-Validierung
    age: int = Field(
        ge=0,           # Greater or Equal (>=)
        le=150,         # Less or Equal (<=)
        gt=-1,          # Greater Than (>) - Alternative zu ge
        lt=151,         # Less Than (<) - Alternative zu le
        description="Das Alter"
    )
    
    # Float-Validierung
    price: float = Field(
        ge=0.0,
        le=999999.99,
        description="Der Preis"
    )
    
    # Optionale Felder
    nickname: str = Field(
        default=None,       # Kann fehlen
        min_length=2,
        max_length=20
    )
    
    # Dokumentation
    email: str = Field(
        description="E-Mail-Adresse des Nutzers",
        # examples funktioniert nicht zuverlässig über Pydantic-Versionen
    )
```

**Wichtige Parameter:**

**Für Strings:**
- `min_length`: Mindest-Zeichenanzahl
- `max_length`: Maximal-Zeichenanzahl
- `pattern`: Regex-Pattern (z.B. für E-Mail, Telefon)

**Für Zahlen (int, float):**
- `ge`: Greater or Equal (>=)
- `le`: Less or Equal (<=)
- `gt`: Greater Than (>)
- `lt`: Less Than (<)

**Allgemein:**
- `description`: Erscheint in Swagger UI
- `default`: Standardwert (macht Feld optional)

### Warum ist das besser als manuelle Prüfung?

**Ohne Field (manuell):**
```python
@app.post("/notes")
def create_note(note: NoteCreate):
    if len(note.text) == 0:
        raise HTTPException(400, "Text darf nicht leer sein")
    if len(note.text) > 500:
        raise HTTPException(400, "Text zu lang")
    # ... Rest der Logik
```

**Probleme:**
- Viel Boilerplate-Code
- Fehleranfällig (vergisst man leicht)
- Muss in jedem Endpoint wiederholt werden
- Nicht in Swagger UI dokumentiert

**Mit Field (automatisch):**
```python
class NoteCreate(BaseModel):
    text: str = Field(min_length=1, max_length=500)

@app.post("/notes")
def create_note(note: NoteCreate):
    # Validierung ist schon passiert!
    # Code ist kürzer und sauberer
    new_id = db.create_note(note.text)
    # ...
```

**Vorteile:**
- Einmal definieren, überall gültig
- Automatische Fehler-Responses
- Automatisch in Swagger UI sichtbar
- Konsistent über alle Endpoints

---

## Theorie: Query-Parameter - Ausführlich erklärt

### Was sind Query-Parameter?

Query-Parameter sind die Werte nach dem `?` in einer URL. Sie werden genutzt, um **optionale Informationen** an einen Endpoint zu übergeben.

**Anatomie einer URL mit Query-Parametern:**
```
https://api.example.com/notes?limit=10&search=wichtig&sort=desc
                        ─────────────────────────────────────
                        Diese Teil sind die Query-Parameter
```

**Aufbau:**
- Beginnen mit `?`
- Format: `key=value`
- Mehrere Parameter mit `&` verbunden
- Alle Parameter sind **optional** (außer man macht sie required)

### Beispiele aus echten APIs

**Google Suche:**
```
https://www.google.com/search?q=python&lang=de&safe=active
                                │      │       │
                                │      │       └─ Sichere Suche
                                │      └─ Sprache (Deutsch)
                                └─ Suchbegriff
```

**YouTube:**
```
https://www.youtube.com/results?search_query=fastapi&sp=EgIQAQ%253D%253D
                                  │                   │
                                  │                   └─ Filter (Videos)
                                  └─ Suchbegriff
```

**Unsere API:**
```
http://localhost:8000/notes?limit=10&search=wichtig
                             │         │
                             │         └─ Nur Notizen mit "wichtig"
                             └─ Maximal 10 Ergebnisse
```

### Query-Parameter vs. Path-Parameter

**Path-Parameter** (aus Tag 2):
```python
@app.get("/notes/{note_id}")
def get_note(note_id: int):
    pass

# Aufruf: /notes/42
# note_id ist PFLICHT, ohne funktioniert die Route nicht
```

**Query-Parameter** (neu):
```python
@app.get("/notes")
def get_notes(limit: int = 100):
    pass

# Aufruf: /notes           → limit = 100 (Default)
# Aufruf: /notes?limit=10  → limit = 10
# limit ist OPTIONAL
```

**Wann welches?**

| Aspekt | Path-Parameter | Query-Parameter |
|--------|----------------|-----------------|
| **Position** | Teil des Pfades | Nach dem `?` |
| **Pflicht** | Ja | Nein (mit Default) |
| **Verwendung** | Identifiziert Ressource | Filtert/Modifiziert Antwort |
| **Beispiel** | `/users/123` | `/users?role=admin&active=true` |
| **REST-Konvention** | Für IDs, eindeutige Identifier | Für Filter, Sortierung, Pagination |

### Query-Parameter in FastAPI definieren

**Einfache Query-Parameter:**
```python
from typing import Optional

@app.get("/notes")
def get_notes(
    limit: int = 100,                  # Optional mit Default
    search: Optional[str] = None       # Optional ohne Default
):
    """
    Beispiele:
    - /notes                    → limit=100, search=None
    - /notes?limit=10           → limit=10, search=None
    - /notes?search=wichtig     → limit=100, search="wichtig"
    - /notes?limit=5&search=x   → limit=5, search="x"
    """
    pass
```

**FastAPI macht automatisch:**

1. **Typ-Konvertierung:**
```
/notes?limit=10    → limit wird zu int(10)
/notes?limit=abc   → 422 Validation Error!
```

2. **Optional vs. Required:**
```python
def get_notes(limit: int):           # Required! Fehlt → 422
def get_notes(limit: int = 100):     # Optional mit Default
def get_notes(limit: Optional[int]): # Optional, kann None sein
```

3. **Automatische Dokumentation:**
- Erscheint in Swagger UI
- Mit Typ, Default-Wert, "Required" Status

### Query-Parameter mit Validierung

**Problem ohne Validierung:**
```python
@app.get("/notes")
def get_notes(limit: int = 100):
    # User kann /notes?limit=999999 aufrufen!
    # Oder /notes?limit=-1
    pass
```

**Lösung mit Query():**
```python
from fastapi import Query
from typing import Optional

@app.get("/notes")
def get_notes(
    limit: int = Query(
        default=100,           # Standardwert
        ge=1,                  # Mindestens 1
        le=100,                # Maximal 100
        description="Maximale Anzahl der Ergebnisse"
    ),
    search: Optional[str] = Query(
        default=None,          # Kann fehlen
        min_length=2,          # Wenn vorhanden, mind. 2 Zeichen
        max_length=50,         # Maximal 50 Zeichen
        description="Suchbegriff für Volltextsuche"
    )
):
    """
    Validierung passiert automatisch!
    
    /notes?limit=0      → 422 Error (ge=1 verletzt)
    /notes?limit=999    → 422 Error (le=100 verletzt)
    /notes?search=x     → 422 Error (min_length=2 verletzt)
    """
    pass
```

**Query() Parameter:**
```python
Query(
    default=...,           # Standardwert (oder ... für required)
    ge=1,                  # Greater or Equal (>=)
    le=100,                # Less or Equal (<=)
    gt=0,                  # Greater Than (>)
    lt=101,                # Less Than (<)
    min_length=2,          # Min. Länge (Strings)
    max_length=50,         # Max. Länge (Strings)
    pattern="^[a-zA-Z]+$", # Regex-Pattern
    description="...",     # Swagger-Dokumentation
    alias="q",             # URL-Alias: ?q=... statt ?search=...
)
```

### Praxisbeispiele für Query-Parameter

**Beispiel 1: Pagination**
```python
@app.get("/notes")
def get_notes(
    page: int = Query(1, ge=1, description="Seitennummer"),
    page_size: int = Query(20, ge=1, le=100, description="Einträge pro Seite")
):
    offset = (page - 1) * page_size
    # SELECT * FROM notes LIMIT page_size OFFSET offset
```

Aufrufe:
- `/notes` → Seite 1, 20 Einträge
- `/notes?page=3` → Seite 3, 20 Einträge
- `/notes?page=2&page_size=50` → Seite 2, 50 Einträge

**Beispiel 2: Sortierung**
```python
@app.get("/notes")
def get_notes(
    sort_by: str = Query("created_at", pattern="^(created_at|text|id)$"),
    order: str = Query("desc", pattern="^(asc|desc)$")
):
    # SELECT * FROM notes ORDER BY {sort_by} {order}
```

Aufrufe:
- `/notes` → sortiert nach created_at, absteigend
- `/notes?sort_by=text&order=asc` → sortiert nach Text, aufsteigend

**Beispiel 3: Filter kombinieren**
```python
@app.get("/notes")
def get_notes(
    search: Optional[str] = Query(None, min_length=2),
    created_after: Optional[str] = Query(None, pattern="^\d{4}-\d{2}-\d{2}$"),
    created_before: Optional[str] = Query(None, pattern="^\d{4}-\d{2}-\d{2}$"),
    limit: int = Query(100, ge=1, le=100)
):
    # SELECT * FROM notes
    # WHERE text LIKE ? AND created_at > ? AND created_at < ?
    # LIMIT ?
```

Aufrufe:
- `/notes?search=wichtig` → Nur "wichtig" enthaltende Notizen
- `/notes?created_after=2025-01-01` → Nur ab 2025
- `/notes?search=bug&limit=5` → Kombinierte Filter

### Best Practices für Query-Parameter

**DO's:**
- Immer Defaults angeben für optionale Parameter
- Validierung mit `Query()` nutzen
- Sprechende Namen (`search` statt `q`, außer bei sehr bekannten Abkürzungen)
- Dokumentation in `description` schreiben

**DON'Ts:**
- Zu viele Query-Parameter (mehr als 5-6 wird unübersichtlich)
- Pflicht-Parameter als Query-Parameter (besser Path oder Body)
- Unklar was der Parameter macht (`?x=1` ist schlecht)

---

## Live-Coding Teil 2: Validierung und Query-Parameter hinzufügen

Jetzt erweitern wir unseren Code aus Teil 1 um:
1. Pydantic Field Validierung
2. Query-Parameter für Filtering

### 1. db.py erweitern (Query-Parameter Support)

Wir fügen der `get_all_notes()` Funktion Parameter hinzu:

```python
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
```

**Was ist neu?**
- `limit` Parameter: Begrenzt Anzahl der Ergebnisse
- `search` Parameter: Filtert nach Text mit SQL `LIKE`
- Pattern `f"%{search}%"`: Findet "wichtig" in "sehr wichtig heute"

### 2. main.py erweitern (vollständige Version)

Jetzt die vollständige Version mit Pydantic Field und Query-Parametern:

```python
"""
Mini Notes API - Tag 3.2: Vollständige Version
Alle Features: Struktur + Error Handling + Validierung + Query-Parameter
"""
from fastapi import FastAPI, HTTPException, Query
#                   ^^^^^^^  ^^^^^^^^^^^^^  ^^^^^
#                   FastAPI  HTTP-Fehler    Query-Parameter Validierung

from pydantic import BaseModel, Field
#                    ^^^^^^^^^  ^^^^^
#                    Basis      Feld-Validierung

from typing import Optional
#                  ^^^^^^^^
#                  Für "kann None sein" Type Hints

import db  # Unser Datenbank-Modul
```

**Neue Imports erklärt:**
- `Query` von FastAPI → Für Query-Parameter Validierung
  - Ermöglicht `limit: int = Query(100, ge=1, le=100)`
- `Field` von Pydantic → Für Feld-Validierung in Models
  - Ermöglicht `text: str = Field(min_length=1, max_length=500)`
- `Optional` von typing → Für Type Hints die None sein können
  - Ermöglicht `search: Optional[str]` → "str oder None"

---

```python
app = FastAPI(
    title="Mini Notes API",
    description="Eine strukturierte API mit Validierung und Error Handling",
    version="3.0.0"
)

# Datenbank beim Start initialisieren
db.init_db()


# ========================================
# Pydantic Models mit Field-Validierung
# ========================================

class NoteCreate(BaseModel):
    """
    Schema für das Erstellen/Aktualisieren einer Notiz.
    
    Pydantic validiert automatisch:
    - text muss vorhanden sein (Required)
    - text muss zwischen 1 und 500 Zeichen lang sein
    - Leerzeichen am Anfang/Ende werden nicht gezählt
    """
    text: str = Field(
        min_length=1,
        max_length=500,
        description="Der Notiz-Text (1-500 Zeichen)"
    )
    
    # Pydantic v2: Config als class attribute
    class Config:
        # Beispiel für Swagger UI
        json_schema_extra = {
            "examples": [
                {
                    "text": "Einkaufen: Milch, Brot, Eier"
                },
                {
                    "text": "Zahnarzttermin am Freitag um 14:00"
                }
            ]
        }


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
            "Input validation (Pydantic Field)",
            "Error handling",
            "Query parameters (limit, search)",
            "Context Manager"
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
    limit: int = Query(
        default=100,
        ge=1,
        le=100,
        description="Maximale Anzahl der Ergebnisse (1-100)"
    ),
    search: Optional[str] = Query(
        default=None,
        min_length=2,
        max_length=50,
        description="Suchbegriff für Volltextsuche (min. 2 Zeichen)"
    )
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
    
    Validierung:
    - limit < 1 oder > 100 → 422 Error
    - search mit 1 Zeichen → 422 Error
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
    
    Beispiele:
    ✓ Gültig:
    {
        "text": "Zahnarzttermin am Freitag"
    }
    
    ✗ Ungültig:
    {
        "text": ""
    }
    → 422 Error: "String should have at least 1 character"
    
    {
        "text": "A" * 501
    }
    → 422 Error: "String should have at most 500 characters"
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
    
    Body: JSON mit neuem 'text' Feld (1-500 Zeichen)
    
    Auch hier gilt die Validierung:
    - Leerer Text → 422 Error
    - Zu langer Text → 422 Error
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

**Was ist komplett neu in dieser Version?**

1. **Pydantic Field Validierung:**
   ```python
   text: str = Field(min_length=1, max_length=500, description="...")
   ```
   - Leere Notizen werden abgelehnt
   - Zu lange Notizen werden abgelehnt
   - Automatische Fehler-Responses

2. **Query-Parameter mit Validierung:**
   ```python
   limit: int = Query(default=100, ge=1, le=100, description="...")
   search: Optional[str] = Query(default=None, min_length=2, ...)
   ```
   - `limit` zwischen 1 und 100
   - `search` mindestens 2 Zeichen (wenn vorhanden)
   - Automatische Validierung

3. **Ausführliche Dokumentation:**
   - Jeder Endpoint erklärt alle Parameter
   - Beispiele für gültige und ungültige Inputs
   - Direkt in Swagger UI sichtbar

**Jetzt testen:**
```bash
uvicorn main:app --reload
```

Öffne http://localhost:8000/docs und teste:

**Query-Parameter testen:**
- `/notes` → Alle Notizen (max 100)
- `/notes?limit=5` → Nur 5 Notizen
- `/notes?limit=0` → 422 Error! (ge=1 verletzt)
- `/notes?limit=999` → 422 Error! (le=100 verletzt)
- `/notes?search=test` → Notizen mit "test"
- `/notes?search=a` → 422 Error! (min_length=2 verletzt)

**Pydantic Validierung testen:**
- POST mit `{"text": ""}` → 422 Error!
- POST mit `{"text": "A" * 501}` → 422 Error!
- POST mit `{"text": "Gültig"}` → 201 Created!

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

### Übung 4 (Bonus): Pagination implementieren

Implementiere echte Pagination mit `page` und `page_size` statt nur `limit`.

**Anforderungen:**
- `page`: Seitennummer (ab 1)
- `page_size`: Einträge pro Seite (1-100)
- SQL: `LIMIT page_size OFFSET (page-1)*page_size`

<details>
<summary>Hintergrundwissen</summary>

**Was ist Pagination?**

Statt alle Daten auf einmal zu laden:
```
GET /notes → 10.000 Notizen auf einmal!
```

Laden wir sie seitenweise:
```
GET /notes?page=1&page_size=20 → Notizen 1-20
GET /notes?page=2&page_size=20 → Notizen 21-40
GET /notes?page=3&page_size=20 → Notizen 41-60
```

**Warum?**
* Schnellere Responses
* Weniger Speicher-Verbrauch
* Bessere User Experience

**SQL für Pagination:**
```sql
-- Seite 1 (Einträge 1-20)
SELECT * FROM notes LIMIT 20 OFFSET 0

-- Seite 2 (Einträge 21-40)
SELECT * FROM notes LIMIT 20 OFFSET 20

-- Seite 3 (Einträge 41-60)
SELECT * FROM notes LIMIT 20 OFFSET 40
```

**Formel:**
```
OFFSET = (page - 1) * page_size
```

**Implementierung:**
```python
# In db.py
def get_all_notes(page: int = 1, page_size: int = 20) -> List[Dict]:
    offset = (page - 1) * page_size
    
    try:
        with get_connection() as conn:
            rows = conn.execute(
                "SELECT * FROM notes ORDER BY id DESC LIMIT ? OFFSET ?",
                (page_size, offset)
            ).fetchall()
            return [dict(row) for row in rows]
    
    except sqlite3.Error as e:
        print(f"Fehler: {e}")
        return []

# In main.py
@app.get("/notes")
def get_notes(
    page: int = Query(1, ge=1, description="Seitennummer"),
    page_size: int = Query(20, ge=1, le=100, description="Einträge pro Seite")
):
    notes = db.get_all_notes(page=page, page_size=page_size)
    
    # Bonus: Total Count für Frontend
    total = db.get_notes_count()
    total_pages = (total + page_size - 1) // page_size  # Aufrunden
    
    return {
        "notes": notes,
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total": total,
            "total_pages": total_pages
        }
    }
```

</details>

---

## Zusammenfassung Tag 3

**Was haben wir gelernt?**

**Type Hints:**
- Was Type Hints sind und warum Python sie hat
- `from typing import Optional, List, Dict`
- `Optional[Type]` für Werte die None sein können
- `List[Type]` für Listen mit bestimmtem Inhalt
- `Dict[KeyType, ValueType]` für typisierte Dictionaries
- `-> Type` für Rückgabewerte von Funktionen
- Warum Type Hints Code besser lesbar und wartbar machen

**Code-Strukturierung:**
- Module erstellen (`db.py`, `main.py`)
- Separation of Concerns umsetzen
- Import und Verwendung eigener Module

**Validierung mit Pydantic:**
- `Field()` mit Constraints (`min_length`, `max_length`)
- Type Hints für bessere Code-Qualität
- Automatische Fehler bei ungültigen Daten
- Warum Validierung wichtig ist

**Query-Parameter:**
- Was sind Query-Parameter und wann nutzt man sie
- Query-Parameter vs. Path-Parameter
- Validierung mit `Query()`
- Praxisbeispiele (Pagination, Filter, Sortierung)

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
- Type Hints für alle Funktionen und Parameter
- Docstrings für Dokumentation
- Type Hints für Typsicherheit
- Logging statt print (Übung)
- Konsistente Fehlerbehandlung

**Type Hints Best Practices:**
- Immer `Optional[Type]` nutzen wenn None möglich ist
- `List[Dict]` statt nur `list` für klare Typisierung
- Type Hints in Docstrings wiederholen zur Verdeutlichung
- IDE-Warnungen bei Type-Fehlern beachten

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
#               ^^^^^^^^  ^^^^  ^^^^
#               Type Hints für bessere Dokumentation

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
    #                 ^^^ Typ       ^^^^^^^^^^^^^^^^^^^^^^^^     ^^^^^^^^^^
    #                 Parameter     Optional: str oder None      Rückgabe: Liste von Dicts
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
    #                  ^^^ Typ      ^^^^^^^^^^^^^^^^
    #                  Parameter    Rückgabe: Dict oder None
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
    #               ^^^ Typ    ^^^^^^^^^^^^^^^
    #               Parameter  Rückgabe: int (ID) oder None
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
    #               ^^^ Typ    ^^^ Typ     ^^^^
    #               Param 1    Param 2     Rückgabe: True/False
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
    #               ^^^ Typ      ^^^^
    #               Parameter    Rückgabe: True/False
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
    #                    ^^^^^
    #                    Rückgabe: int (Anzahl)
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
- Input-Validierung mit Pydantic Field
- Query-Parameter mit Validierung (limit, search)
- Error Handling mit try-except
- Context Manager für DB-Connections
"""
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional
#               ^^^^^^^^
#               Für Type Hints: "kann None sein"
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
        #    ^^^ Type Hint: text muss ein String sein
        min_length=1,
        max_length=500,
        description="Der Notiz-Text (1-500 Zeichen)"
    )
    
    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "text": "Einkaufen: Milch, Brot, Eier"
                },
                {
                    "text": "Zahnarzttermin am Freitag um 14:00"
                }
            ]
        }


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
    #      ^^^ Type Hint: limit ist ein int
    search: Optional[str] = Query(None, min_length=2, max_length=50, description="Suchbegriff (min. 2 Zeichen)")
    #       ^^^^^^^^^^^^^^ Type Hint: search ist entweder str oder None
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
    # db.get_all_notes() gibt List[Dict] zurück
    return notes


@app.get("/notes/count")
def count_notes():
    """
    Anzahl der Notizen abrufen.
    
    Gibt die Gesamtzahl aller gespeicherten Notizen zurück.
    """
    count = db.get_notes_count()
    # db.get_notes_count() gibt int zurück
    return {
        "count": count,
        "message": f"Es sind {count} Notizen gespeichert."
    }


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    #            ^^^ Type Hint: note_id ist ein int
    """
    Eine einzelne Notiz abrufen.
    
    Path Parameter:
    - note_id: Die ID der Notiz (muss eine Zahl sein)
    """
    note = db.get_note_by_id(note_id)
    # db.get_note_by_id() gibt Optional[Dict] zurück
    # (entweder ein Dictionary oder None)
    
    if note is None:
        raise HTTPException(
            status_code=404,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    return note


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    #               ^^^^ Type Hint: note ist ein NoteCreate-Objekt
    """
    Neue Notiz erstellen.
    
    Body: JSON mit 'text' Feld (1-500 Zeichen)
    
    Beispiel:
    {
        "text": "Zahnarzttermin am Freitag"
    }
    """
    new_id = db.create_note(note.text)
    # db.create_note() gibt Optional[int] zurück
    # (entweder die neue ID oder None bei Fehler)
    
    if new_id is None:
        raise HTTPException(
            status_code=500,
            detail="Fehler beim Erstellen der Notiz"
        )
    
    return {"id": new_id, "text": note.text}


@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteCreate):
    #               ^^^ Typ   ^^^^ Type Hints für beide Parameter
    """
    Notiz aktualisieren.
    
    Path Parameter:
    - note_id: Die ID der zu aktualisierenden Notiz
    
    Body: JSON mit neuem 'text' Feld
    """
    success = db.update_note(note_id, note.text)
    # db.update_note() gibt bool zurück (True/False)
    
    if not success:
        raise HTTPException(
            status_code=404,
            detail=f"Notiz mit ID {note_id} nicht gefunden"
        )
    
    # Aktualisierte Notiz zurückgeben
    updated_note = db.get_note_by_id(note_id)
    # db.get_note_by_id() gibt Optional[Dict] zurück
    
    if updated_note is None:
        # Sollte nicht passieren, aber sicherheitshalber
        raise HTTPException(
            status_code=500,
            detail="Fehler beim Laden der aktualisierten Notiz"
        )
    
    return updated_note


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    #               ^^^ Type Hint: note_id ist ein int
    """
    Notiz löschen.
    
    Path Parameter:
    - note_id: Die ID der zu löschenden Notiz
    """
    success = db.delete_note(note_id)
    # db.delete_note() gibt bool zurück
    
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
├── main.py              # API-Endpoints (ca. 150 Zeilen)
├── db.py                # Datenbank-Funktionen (ca. 180 Zeilen)
├── notes.db             # SQLite-Datenbank (nicht in Git)
├── requirements.txt     # Python-Abhängigkeiten
└── .gitignore          # Git-Ignore-Regeln
```

**Vergleich zu Tag 2:**
* **Vorher:** Eine Datei, 200+ Zeilen, alles vermischt
* **Jetzt:** Zwei Dateien, jede hat klare Verantwortung, einfach zu warten

---

## Checkliste Tag 3

- [ ] Type Hints verstanden (`Optional`, `List`, `Dict`)
- [ ] Type Hints in eigenen Funktionen genutzt
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
- [ ] DB-Fehler vs "nicht gefunden" unterschieden (Übung 3)
- [ ] Type Hints überall korrekt verwendet

---

## Best Practices Zusammenfassung

**Code-Organisation:**
* Eine Datei = Eine Verantwortung
* Module statt Copy-Paste
* Imports am Anfang der Datei

**Error Handling:**
* Try-except für alle externen Operationen
* Sichere Rückgabewerte (None, [], False)
* Spezifische Exceptions abfangen (`sqlite3.Error`)

**Ressourcen-Management:**
* Context Manager für DB-Connections
* Keine manuellen `close()`-Aufrufe mehr
* Automatisches Cleanup garantiert

**Dokumentation:**
* Docstrings für alle Funktionen
* Type Hints für Parameter und Return
* Beispiele in der Dokumentation

**API-Design:**
* Korrekte HTTP-Status-Codes (200, 201, 404, 500)
* Beschreibende Fehlermeldungen
* Query-Parameter für Filter
* Path-Parameter für Ressourcen-IDs
* Validierung mit Pydantic Field

---

**Glückwunsch! Du hast jetzt eine professionelle, wartbare API-Struktur!**

**Bei Fragen meldet euch bei Patrick oder mir. Viel Erfolg und bis morgen!**
